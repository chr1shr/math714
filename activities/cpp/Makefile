# Include the configuration file, setting the name of the C++ compiler, and
# setting the compilation flags
include config.mk

# List of executables to build
execs=hello_world ridders_array cube_func print_styles 

# Specifies what targets should be build when 'make' is called
all: $(execs)

# Makefile rules specifying the dependencies and compiler commands. $@ is
# shorthand for the target (i.e. the executable to be built) and $< is a
# shorthand for the first dependency (i.e. the C++ source code file). $^ can
# also be used a shorthand for all dependencies.
hello_world: hello_world.cc
	$(cxx) $(cflags) -o $@ $<

cube_func: cube_func.cc
	$(cxx) $(cflags) -o $@ $<

print_styles: print_styles.cc
	$(cxx) $(cflags) -o $@ $<

ridders_array: ridders_array.cc
	$(cxx) $(cflags) -o $@ $<

# Special rule so that "make clean" removes all of the compiled executables
clean:
	rm -f $(execs)

# Tells the GNU Make that "clean" is a 'phony target', meaning that clean is
# not the name of a program to be built
.PHONY: clean
