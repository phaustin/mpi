#!/usr/bin/env python

from mpi4py import MPI
import numpy as np
from configobj import ConfigObj
import argparse

def convertDict(config_object):
   """I need to get the configuration data
      into a form that can be broadcast to all
      processors, so 
      convert the configuration object into
      a nested dictionary
   """
   outDict={}
   vals=config_object['fluxes']
   outDict["fluxes"]={}
   for key,value in vals.items():
      outDict["fluxes"][key]=value
   vals=config_object['radiances']
   outDict['radiances']={}
   for key,value in vals.items():
      outDict["radiances"][key]=value
   return outDict

parser = argparse.ArgumentParser()
comm = MPI.COMM_WORLD
#
# total number of processors
#
size = comm.Get_size()
#
# id of this processor
#
rank = comm.Get_rank()

if rank == 0:
   #
   # we only want to read the input data once
   #
   parser.add_argument('configfile', type=str,help="name of configuration file")
   args=parser.parse_args()
   config = ConfigObj(args.configfile,unrepr=True)
   inputvals=convertDict(config)
else:
   inputvals=None
#
# broadcast this dictionary from processor 0 to all processors
#
indata = comm.bcast(inputvals, root=0)
print "processor: ",rank, "has received: ",indata
#
# now scatter data out to the different processors, do
# something with it, and gather it back on processor 0
#
if rank == 0:
   #
   # some fake input data
   #
   outdata=np.zeros([size*5,],dtype=np.float)
   #split into a list with an item for each processor
   outvectors=np.array_split(outdata,size)
else:
   outvectors=None
#
# scatter the data from root to all processors
#
data = comm.scatter(outvectors, root=0)
#
# each processor does something unique to the
# data (for this example just tag it so
# we know who did the work
#
data=data + rank +1
#
# now gather the indvidual results back
# into a list
#
fulldata=comm.gather(data, root=0)
if rank == 0:
   print "We're done, here is the answer: "
   print fulldata

