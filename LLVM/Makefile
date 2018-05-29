hello.o: 

# Py2 flags
PYFLAGS = $(shell python-config --cflags)
# C only
PYFLAGS := $(subst -Wstrict-prototypes,,$(PYFLAGS))

# LLVM flags
LLFLAGS = $(shell llvm-config --cxxflags)

CXXFLAGS += $(PYFLAGS) $(LLFLAGS)
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $^
