#include <Python.h>

PyObject *hello( PyObject *self, PyObject *args, PyObject *kwargs )
{
	PyObject *result = NULL;

	char *who=NULL;
	static char *keywords[] = {"who", NULL};

	if (!PyArg_ParseTupleAndKeywords(args, kwargs, "s", keywords, &who))
		return NULL;

	result = PyString_FromString("Hello ");
	PyString_Concat(&result, PyString_FromString(who));
	return result;
}

static PyMethodDef methods[] = {
	{ "hello", (PyCFunction) hello, METH_KEYWORDS, "hello doc" },
{NULL,NULL,0,NULL}};

PyMODINIT_FUNC inithello() {
	(void) Py_InitModule("hello", methods);
	if (PyErr_Occurred())
		PyErr_SetString(PyExc_ImportError, "init_hello failed");
}
