#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print information about a bytes object
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i = -1;
	char *byte;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	byte = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", byte);
	size = size > 10 ? 10 : size + 1;
	printf("  first %d bytes:", size);
	while (size--)
		printf(" %.2x", (unsigned char) *byte++);
	printf("\n");
}

/**
 * print_python_float - print information about a float object
 * @p: python object
 */
void print_python_float(PyObject *p)
{
	chat *buff;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buff = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval), 'r', 0,
	     Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	fflush(stdout);

}

/**
 * print_python_list - print information about a list object
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i = -1;
	PyObject *obj;

	printf("[*] Python list info\n");

	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %lld\n", ((PyListObject *)p)->allocated));
	while (++i < size)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, obj->ob_type->tp_name);
		if (PyFloat_Check(obj))
			print_python_float(obj);
		else if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
