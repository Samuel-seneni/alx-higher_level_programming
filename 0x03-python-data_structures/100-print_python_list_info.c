#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints info about python lists
 * @p: address of python project
 */
void print_python_list_info(PyObject *p)
{
	int x;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; x < Py_SIZE(p); x++)
		printf("Element %d: %s\n", x, Py_TYPE(PyList_GetItem(p, x))->tp_name);
}
