bitstruct.ll: bitstruct.c
	clang -S -emit-llvm $<

test: LL.so
	python test.py

CXX		?= g++
OBJDUMP	?= objdump 

L += -lboost_python
L += $(shell llvm-config --libs core ) -ltinfo
#--system-libs

CXXFLAGS += $(shell python-config --includes)
CXXFLAGS += -shared -fPIC

%.so: %.cpp Makefile
	$(CXX) $(CXXFLAGS) -o $@ $< $(L)
	$(OBJDUMP) -x $@ > $@.objdump
