# Math/CS 714 - Introduction to C++
This directory contains files from the C++ tutorial. They demonstrate some of
the features of the C++ language, and compare it to interpreted languages such
as Python.

- **hello_world.cc** - Prints "Hello World!", a standard first example for
  starting any new programming language

- **print_styles.cc** - Demonstrates the C-style and C++-style print commands

- **cube_func.cc** - Demonstrates a function to compute the cube of a number.

- **ridders_array.cc** - Fills a table of inverse cosine values using Ridders'
  method, and times the results.

- **ridders_array.py** - The equivalent Python program to ridders\_array.cc,
  used for a speed comparison.

The directory **multi_proj** demonstrates how to split a C++ program across
several different file. The directory **matrices** contains some basic
routines for matrix computations.

## GNU Make
The C++ tutorial also introduced [GNU Make](https://www.gnu.org/software/make/)
which can simplify the compilation of large projects split across multiple files.
Each directory and subdirectory contains a **Makefile** that can automatically
compile all the executables by typing `make` on the command line.

Since the C++ compiler and compilation flags may vary from system to system,
the Makefiles look for a common configuration file called **config.mk**
in the top-level directory to specify the compiler name and flags.

A template configration is provided in **config.mk.template**. It specifies
`g++` as the compiler, which is available on many computing platforms. To use
the Makefiles, first copy the template using the command
```Shell
cp config.mk.template config.mk
```
Then edit the **config.mk** file for use with your compiler and system.

## Credit
This material is derived from previous C++ tutorials given by current and
former Ph.D. students in the Rycroft Group, including Dan Fortunato, Nick
Boffi, Nick Derr, and Michael Emanuel.
