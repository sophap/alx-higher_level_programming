#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * print_python_list - prints a python list
 * @p: argument coming in
 * Return: 0
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		PyObject *element;
		Py_ssize_t x;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (x = 0; x < size; x++)
		{
			element = PyList_GetItem(p, x);
			printf("Element %ld: %s\n", x, Py_TYPE(element)->tp_name);
		}
	}
}

/**
 * print_python_bytes - prints python bytes objects
 * @p: argument coming in
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		char *string = PyBytes_AsString(p);
		Py_ssize_t x;

		printf("[.] bytes object info\n");
		printf(" size: %ld\n", size);
		printf(" trying string: %s\n", string);

		if (size > 10)
			size = 10;
		printf(" first %ld bytes:", size + 1);
		for (x = 0; x <= size; x++)
			printf(" %02x", string[x] & 0xFF);
		printf("\n");
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
	}
}
