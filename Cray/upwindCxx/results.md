# How to squeeze C++ performance on kupe using the Cray compiler

Through a few simple steps, we show how to improve the performance of a C++ code on the Cray XC-50 system (Skylake processor 2.4GHz) installed at the National Institute for Water and Atmospheric Research (NIWA), New Zealand. 

Our example, upwindCxx, is a finite difference code written in C++ which advects a bubble on a 3D periodic grid using a low order upwind algorithm. 


upwindCxx is included in the fidibench test suite, We'll start with downloading and building the code:

```
git clone https://github.com/pletzer/fidibench
cd fidibench
mkdir build
cmake ..
make
```
This will compile the code using default compiler options. 

To run upwindCxx using 40 OpenMP threads, type 
```
cd upwind/cxx
module load slurm
sbatch upwindCxx_kupe_40.sl
```


