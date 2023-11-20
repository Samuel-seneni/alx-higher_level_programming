#include <stdlib.h>
#include <python.h>
#include <stdio.h>
/**
 * print_python_float - prints the PyFloatObject
 * @p: the PyObject
 * Return: string
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 *
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, x = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (x < size + 1 && x < 10)
	{
		printf(" %02hhx", string[x]);
		x++;
	}
	printf("\n");
}
/**
 * print_python_list - print the PyListObject
 * @p: the PyObject
 * Return: error message
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *product;
	int x = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (x < size)
		{
			product = PyList_GET_ITEM(p, x);
			printf("Element %d: %s\n", x, product->ob_type->tp_name);
			if (PyBytes_Check(product))
				print_python_bytes(product);
			else if (PyFloat_Check(product))
				print_python_float(product);
			x++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
