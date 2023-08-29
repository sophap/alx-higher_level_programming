#include <Python.h>
#include <float.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to PyObject (Python list)
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		int alloc;
		PyListObject *list = (PyListObject *)p;
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;

		alloc = list->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %d\n", alloc);

		for (i = 0; i < size; i++)
		{
			const char *item_type = list->ob_item[i]->ob_type->tp_name;

			printf("Element %ld: %s\n", i, item_type);
			if (strcmp(item_type, "bytes") == 0)
				print_python_bytes(list->ob_item[i]);
			if (strcmp(item_type, "float") == 0)
				print_python_float(list->ob_item[i]);
		}
	}
	else
	{
		printf("[*] Python list info\n");
		fprintf(stderr, "[ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Pointer to PyObject (Python bytes)
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		unsigned char size;
		const char *string = PyBytes_AsString(p);
		Py_ssize_t i;

		printf("[.] bytes object info\n");
		printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", string);

		if (((PyVarObject *)p)->ob_size > 10)
			size = 10;
		else
			size = ((PyVarObject *)p)->ob_size + 1;

		printf("  first %d bytes: ", size);
		for (i = 0; i < size; i++)
			printf(" %02x", string[i] & 0xFF);
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: Pointer to PyObject (Python float)
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		double value = PyFloat_AsDouble(p);

		printf("[.] float object info\n");
		printf("  value: %.15g\n", value);
	}
	else
	{
		printf("[.] float object info\n");
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
	}
}
