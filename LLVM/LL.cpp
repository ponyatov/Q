/// @file
/// @brief LLVM/Python wrapper
/// @defgroup ll LLVM
/// @brief LLVM/Python wrapper
/// @{

#include <boost/python.hpp>
using namespace boost::python;

/// @brief simple `hello` function
/// @returns std::string
std::string hello() { return "Hello LL"; }

/// demo `hello` class
class Hello {};

#include <llvm/IR/Module.h>

/// Boost.Python interface
BOOST_PYTHON_MODULE(LL)
{
    class_<Hello>("Hello")
//    	.def("hello", &Hello::hello)
	;
    def("hello", &hello);
}

/// @}
