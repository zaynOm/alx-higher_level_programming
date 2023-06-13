#include "Python.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *lobj = (PyListObject *) p;
	long i = 0, size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lobj->allocated);

	while (i < size)
		printf("Element %d: %s\n", i, lobj->ob_item[i++]->tp_name);
}
