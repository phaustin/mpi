To run the examples:

1) make sure that your python is the correct one:

~/repos/mpi phil@owl% type python
python is hashed (/home/phil/usr64/bin/python)

2) make sure that the python scripts are executable

~/repos/mpi phil@owl% ls -ltd *py
-rwxr-xr-x 1 phil users  277 Nov 16 17:12 test_helloworld.py
-rwxr-xr-x 1 phil users 2035 Nov 16 17:11 test_gather_scatter.py

3) make sure that mpirun is in your path:

~/repos/mpi phil@owl% type mpirun
mpirun is hashed (/usr/lib64/openmpi/1.4-gcc/bin/mpirun)

4) here's what I get:

~/repos/mpi phil@owl% mpirun -np 4 test_helloworld.py
Hello, World! I am process 0 of 4 on owl.eos.ubc.ca.
Hello, World! I am process 1 of 4 on owl.eos.ubc.ca.
Hello, World! I am process 2 of 4 on owl.eos.ubc.ca.
Hello, World! I am process 3 of 4 on owl.eos.ubc.ca.

~/repos/mpi phil@owl% mpirun -np 4 test_gather_scatter.py  inputvals.cfg
processor:  0 has received:  {'fluxes': {'F0': 350.0, 'g': 0.80000000000000004, 'cldtau': 0.29999999999999999, 'ntaubins': 50, 'nphotons': 250000, 'outprefix': 'thin', 'phi0_deg': 0.0, 'theta0_deg': 50.0, 'ssa': 0.98999999999999999}, 'radiances': {'hitheta': 80.0, 'nphibins': 30, 'lowtheta': 0.0, 'hiphi': 360.0, 'lowphi': 0, 'nthetabins': 20}}
processor:  1 has received:  {'fluxes': {'F0': 350.0, 'g': 0.80000000000000004, 'cldtau': 0.29999999999999999, 'ntaubins': 50, 'nphotons': 250000, 'outprefix': 'thin', 'phi0_deg': 0.0, 'theta0_deg': 50.0, 'ssa': 0.98999999999999999}, 'radiances': {'hitheta': 80.0, 'nphibins': 30, 'lowtheta': 0.0, 'hiphi': 360.0, 'lowphi': 0, 'nthetabins': 20}}
processor:  3 has received:  {'fluxes': {'F0': 350.0, 'g': 0.80000000000000004, 'cldtau': 0.29999999999999999, 'ntaubins': 50, 'nphotons': 250000, 'outprefix': 'thin', 'phi0_deg': 0.0, 'theta0_deg': 50.0, 'ssa': 0.98999999999999999}, 'radiances': {'hitheta': 80.0, 'nphibins': 30, 'lowtheta': 0.0, 'hiphi': 360.0, 'lowphi': 0, 'nthetabins': 20}}
processor:  2 has received:  {'fluxes': {'F0': 350.0, 'g': 0.80000000000000004, 'cldtau': 0.29999999999999999, 'ntaubins': 50, 'nphotons': 250000, 'outprefix': 'thin', 'phi0_deg': 0.0, 'theta0_deg': 50.0, 'ssa': 0.98999999999999999}, 'radiances': {'hitheta': 80.0, 'nphibins': 30, 'lowtheta': 0.0, 'hiphi': 360.0, 'lowphi': 0, 'nthetabins': 20}}
We're done, here is the answer: 
[array([ 1.,  1.,  1.,  1.,  1.]), array([ 2.,  2.,  2.,  2.,  2.]), array([ 3.,  3.,  3.,  3.,  3.]), array([ 4.,  4.,  4.,  4.,  4.])]


