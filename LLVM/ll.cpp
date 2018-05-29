// LLVM/Python wrapper
#include <Python.h>

static PyMethodDef methods[] = {
{NULL,NULL,0,NULL}};

PyMODINIT_FUNC initll() { Py_InitModule("ll", methods); }
