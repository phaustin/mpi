#!/usr/bin/env python
"""
Parallel Hello World
"""

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

output= "Hello, World! I am process %d of %d on %s."  \
         % (rank, size, name)


