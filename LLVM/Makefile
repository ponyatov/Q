test: hello.so ll.so
	python test.py

CXX		?= g++
OBJDUMP	?= objdump 

# Py2 flags
PYFLAGS = $(shell python-config --cflags)
# C only
PYFLAGS := $(subst -Wstrict-prototypes,,$(PYFLAGS))

## LLVM flags
#LLFLAGS = $(shell llvm-config --cxxflags)

CXXFLAGS += $(PYFLAGS) $(LLFLAGS) -g0
%.so: %.cpp Makefile
	$(CXX) $(CXXFLAGS) -shared -fPIC -o $@ $< 
	$(OBJDUMP) -x $@ > $@.objdump
