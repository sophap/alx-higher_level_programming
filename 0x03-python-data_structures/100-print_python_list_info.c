#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, x;

	if (!PyList_Check(p))
       	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		printf("Element %zd: %s\n", x, Py_TYPE(list->ob_item[x])->tp_name);
	}
}
