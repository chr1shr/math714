# Include the configuration file, setting the name of the C++ compiler, and
# setting the compilation flags
include ../config.mk

all: driver mat_timing

# List of object files to be built. The "src" variable is set to a list of all
# corresponding implementation files.
objs=matrix.o
src=$(patsubst %.o,%.cc,$(objs))

# Include the file dependencies
-include Makefile.dep

# A Makefile target to refresh the dependency file
depend:
	$(cxx) $(cflags) -MM $(src) >Makefile.dep

# General rule for building any object file from its corresponding
# implementation file
%.o: %.cc
	$(cxx) $(cflags) -c $<

# Rule to build the executables
driver: driver.cc matrix.o
	$(cxx) $(cflags) -o $@ $^

mat_timing: mat_timing.cc matrix.o
	$(cxx) $(cflags) -o $@ $^

# Special rule so that "make clean" removes all of the compiled files
clean:
	rm -f $(execs) driver mat_timing

# Tells the GNU Make that "clean" and "depend" are 'phony targets', meaning
# that they are not the name of a program to be built
.PHONY: clean depend
