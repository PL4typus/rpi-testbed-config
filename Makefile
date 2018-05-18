# Sample Makefile using the cross-gcc from the buildroot toolchain
# Modifiy according to your needs
# This Makefile assumes a certain working directory structure:
# 
# This makefile should be located in the src directory.
#
# Inlude files are in sub-directory include, accessed with $(IDIR)
# Object files are in sub-directory obj, accessed with $(ODIR)
# Lib files are in sub-directory lib, accessed with $(LDIR) (commented for now (commented for now)
#
# Author: Pierre-Louis Palant for CRoCS muni

IDIR =../include
CC=arm-buildroot-linux-gnueabihf-gcc
CFLAGS=-I$(IDIR)

ODIR=obj
#LDIR =../lib

# Libraries to specify to gcc (ex: -lm for math, -lpthread, etc.)

#LIBS=-lm

_DEPS = hellomake.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = hellomake.o hellofunc.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.c $(DEPS)
		$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
		gcc -o $@ $^ $(CFLAGS) #$(LIBS)

.PHONY: clean

clean:
		rm -f $(ODIR)/*.o *~ core *.swp $(IDIR)/*~ 
		
