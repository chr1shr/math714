# Include the configuration file
include ../config.mk

# Lists of files to be built
objs=
src=$(patsubst %.o,%.cc,$(objs))
execs=music_fft

all: $(objs) $(execs)

# Include the file dependencies
-include Makefile.dep

# A Makefile target to refresh the dependency file
depend:
	$(cxx) -MM $(src) >Makefile.dep

# A Makefile target to remove all the built files
clean:
	rm -f $(objs) $(execs)

%.o: %.cc
	$(cxx) $(cflags) $(fftw_iflags) -c $<

music_fft: music_fft.cc
	$(cxx) $(cflags) $(fftw_iflags) -o $@ $^ $(fftw_lflags)

.PHONY: clean depend
