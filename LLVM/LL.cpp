/// @file
/// @brief LLVM/Python wrapper
/// @defgroup ll LLVM c89

#include <boost/python.hpp>
using namespace boost::python;

std::string hello() { return "Hello LL"; }

class Hello {};

#include <llvm/IR/Module.h>


BOOST_PYTHON_MODULE(LL)
{
    class_<Hello>("Hello")
//    	.def("hello", &Hello::hello)
	;
    def("hello", &hello);
}
