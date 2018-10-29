#include <Python.h>


int fib(int n)
{
    if (n <= 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fib(n - 1) + fib(n - 2);
}

static PyObject* pyfib(PyObject* self, PyObject* args)
{
    int n;

    if(!PyArg_ParseTuple(args, "i", &n))
        Py_INCREF(Py_None);
        return Py_None;

    return Py_BuildValue("i", fib(n));
}

static PyMethodDef fibMethods[] = {
    { "fib", fib, METH_VARARGS, "count element" },
    { "pyfib", pyfib, METH_VARARGS, "Call fib function" },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibModule = {
    PyModuleDef_HEAD_INIT,
    "fibModule",
    "Fibonacci Module",
    -1,
    fibMethods
};

PyMODINIT_FUNC PyInit_fibModule(void)
{
    return PyModule_Create(&fibModule);
}
 
