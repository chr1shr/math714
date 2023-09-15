include ../config.mk

all: driver

objs: matrix.o
src=$(patsubst %.o,%.cc,$(objs))

# Include the file dependencies
-include Makefile.dep

# A Makefile target to refresh the dependency file
depend:
	$(cxx) $(iflags) -MM $(src) >Makefile.dep

%.o: %.cc
	$(cxx) $(cflags) -c $<

driver: driver.cc matrix.o
	$(cxx) $(cflags) -o $@ $^

clean:
	rm -f $(objs) driver

.PHONY: clean depend
