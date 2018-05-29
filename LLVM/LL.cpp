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

#include <sys/stat.h>

#include <llvm-c/Core.h>

/// @defgroup llmodule Module
/// @brief compilation module (single object file)
/// @{

/// llvm::Module wrapper
struct llModule {
	/// construct module using LLVM C API
	llModule(std::string value, std::string triplet)
		: value(value),triplet(triplet)
	{
		module = LLVMModuleCreateWithName(value.c_str());
		builder = LLVMCreateBuilder();
		LLVMSetTarget(module, triplet.c_str());
		#ifdef _LL_MKDIR
			// make module directory
			mkdir(value.c_str(),S_IRWXU);
			// create Makefile for module compile
			mk = fopen((value+"/Makefile").c_str(),"w");
			fprintf(mk,"%s.S: %s.bc\n\tllc -o $@ $<\n",value.c_str(),value.c_str());
			fflush(mk);
			// create bitcode source file
			bc = fopen((value+"/"+value+".bc").c_str(),"w");
		#endif // _LL_MKDIR
	}
	/// cleanup module
	~llModule() {
		LLVMDisposeModule(module);
		#ifdef _LL_MKDIR
			fclose(mk);
			fprintf(bc,LLVMPrintModuleToString(module));
			fclose(bc);
		#endif // _LL_MKDIR
	}

	/// print print string representation
	std::string __repr__() {
		return "<module:"+value+"> '''\n"+\
				LLVMPrintModuleToString(module)+\
				"\n'''\n"; }
	/// `module:value`
	std::string value;

	/// target triplet
	std::string triplet;

	/// wrapped `llvm::module`
	LLVMModuleRef module;

	/// basic block builder
	LLVMBuilderRef builder;

	/// Makefile
	FILE *mk;
	/// Makefile file name with path
	char *mkname;
	/// bitcode
	FILE *bc;
	/// bitcode file name with path
	char *bcname;

};

/// @}

/// @defgroup lltype Type
/// @brief types
/// @{

/// type
struct llType {
	/// reference to LLVM wrapped type
	LLVMTypeRef lltype;
	/// type size requested in bits
	uint8_t size;
};

struct llVoid:llType {
	llVoid() { size=0; }
	std::string __repr__() { return "<type:void>"; }
};

/// integer number type
struct llInt:llType {
	/// select appropriate LLVM integer type from size
	llInt(uint8_t size) { this->size = size; lltype = LLVMIntType(size); }
	/// print in form `<type:i16>`
	std::string __repr__() {
		char S[0x100]; sprintf(S,"<type:i%i>",size);
		return std::string(S); }
};

/// float point number type
struct llFloat:llType {
	/// select appropriate LLVM float type from size
	llFloat(uint8_t size) {
		if (size <= 0x10)
			this->size = 0x10, lltype = LLVMFloatType();
		else if (size <= 0x20)
			this->size = 0x20, lltype = LLVMDoubleType();
		else if (size <= 80)
			this->size = 80, lltype = LLVMX86FP80Type();
		else throw;
	}
	/// print in form `<type:f16>`
	std::string __repr__() {
		char S[0x100]; sprintf(S,"<type:f%i>",size);
		return std::string(S); }
};

/// @}

/// Boost.Python interface
BOOST_PYTHON_MODULE( LL )
{
    class_<Hello>("Hello")
//    	.def("hello", &Hello::hello)
	;
    def("hello", &hello);

    class_<llModule>("Module", init<std::string,std::string>( args("name","triplet") ))
    	.def("__repr__",&llModule::__repr__)
    ;

    class_<llType>("Type");

    class_<llVoid>("Void", init<>())
		.def("__repr__",&llVoid::__repr__)
    ;

    class_<llInt>("Int", init<uint8_t>( args("size") ))
		.def("__repr__",&llInt::__repr__)
    ;
    class_<llFloat>("Float", init<uint8_t>( args("size") ))
		.def("__repr__",&llFloat::__repr__)
    ;

}

/// @}
