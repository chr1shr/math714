# Include the configuration file setting the compiler and flags, from the top
# level C++ tutorial directory
include ../config.mk

all: main

# The main program requires the pre-built function in the binary add.o object
# file
main: main.cc add.o
	$(cxx) $(cflags) -o main main.cc add.o

# Builds the binary add.o object from the separate add.cc implementation file
add.o: add.cc add.hh
	$(cxx) $(cflags) -c add.cc

# Special rule so that "make clean" removes the executable and object file
clean:
	rm -f main add.o

# Tells the GNU Make that "clean" is a 'phony target', meaning that clean is
# not the name of a program to be built
.PHONY: clean
