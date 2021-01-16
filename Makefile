CC      = gcc
CFLAGS += -Wall -g -O4
LDLIBS += -lm -lrt

all: stencil_seq stencil_omp

stencil_seq: stencil.c
	$(CC) $(CFLAGS) $(LDLIBS) stencil.c -o stencil_seq

stencil_omp: stencil_omp.c
	$(CC) $(CFLAGS) $(LDLIBS) -fopenmp stencil_omp.c -o stencil_omp

clean:
	-rm stencil

mrproper: clean
	-rm *~

archive: stencil.c Makefile
	( cd .. ; tar czf stencil.tar.gz stencil/ )

