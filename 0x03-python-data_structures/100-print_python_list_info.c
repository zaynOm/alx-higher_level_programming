#include "Python.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *obj = (PyListObject *) p;
	long long i = -1, size;

	size = (long long) Py_SIZE(p);
	printf("[*] Size of the Python List = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long) obj->allocated);
	while (++i < size)
		printf("Element %lld: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
