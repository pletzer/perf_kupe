# Tuning the SPECFEM3D community code


## Overview 

Through a few simple steps, we show how to improve the performance of a community finite element code, SPECFEM3D,  on the NeSI Cray XC-50 system (Skylake processor 2.4GHz) installed at the National Institute for Water and Atmospheric Research (NIWA), New Zealand. 

We assume that you have your programming environment set, we'll show the build steps for
```
module load PrgEnv-cray
module load craype-x86-skylake
```

Other programming environments are:
```
module swap PrgEnv-cray PrgEnv-gnu
module load craype-craype-broadwell
```

```
module swap PrgEnv-cray PrgEnv-gnu
module load gcc/6.1.0
module load craype-craype-skylake
```

```
module swap PrgEnv-cray PrgEnv-gnu
module load gcc/7.1.0
module load craype-craype-skylake
```

and 

```
module swap PrgEnv-cray PrgEnv-intel
module load craype-craype-skylake
```


The steps to build and run SPECFEM3D are:
```
git clone --recursive https://github.com/geodynamics/specfem3d.git
cd specfem3d
mkdir build-cray
cd build-cray
../configure FC=ftn CC=cc CXX=CC MPIFC=ftn MPICC=cc MPICXX=CC --with-mpi 
make
```

Our test case is ```homogeneous_halfspace```:
```
cd ../EXAMPLES/homogeneous_halfspace
```
Use Slurm script [run_this_script.sh](run_this_script.sh) to submit the job 
```
sbatch  run_this_script.sh
```
You will need to adapt the ```--account``` directive to your project account number.

The test involves generating the database and running SPECFEM3D on 4 processors.


## Results and summary

The results below were obtained choosing different compilers and CPU targets. For instance, "Gnu 4.9.2" means that modules ```PrgEnv-gnu``` and ```gcc/4.9.3``` were loaded. Target x86-64 is the default; other options are ```craype-broadwell``` and ```craype-x86-skylake```. Load ```craype-x86-skylake``` to take advatange of AVX-512 vectorization. AVX-512 instruction sets are supported by Intel and Cray compilers, and by Gnu compilers from version 6.1.0 onwards. 

As of January 30 2018, the master branch SPECFEM3D will not compile with the Cray compilers due to a symbol clash where "si" is used both to declare integer types and as a real variable. The corrected files can be found here:
 * [anisotropic_parametrisation_mod.f90](anisotropic_parametrisation_mod.f90)
 * [elastic_tensor_tools_mod.f90](elastic_tensor_tools_mod.f90)



| Compiler         | Target      | Time (s) |  Speed improvement |
|------------------|-------------|----------|---------|
| Gnu 4.9.3        | x86-64      | 271      |   0     |
| Gnu 4.9.3        | broadwell   | 245      |  11%    |
| Gnu 7.1.0        | broadwell   | 192      |  41%    |
| Gnu 7.1.0        | x86-skylake | 185      |  46%    |
| Intel 17.0.4.196 | x86-skylake | 237      |  14%    |
| Cray 8.6.2       | x86-skylake | 179      |  51%    |


![Speedup](004-specfem3d-speedup-ap.png)




