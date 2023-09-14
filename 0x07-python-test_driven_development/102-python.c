#define PY_SSIZE_T_CLEAN
#include <Python.h>
/**
 * print_python_string - prints a python string
 * @p: python string
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	const char *value = PyUnicode_AsUTF8(p);
	Py_UNICODE *unicode_str = PyUnicode_AsUnicode(p);
	Py_ssize_t length = PyUnicode_GetLength(p);

	printf("  type: compact ");

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("ascii\n");
	}
	else
	{
		printf("unicode object\n");
	}

	printf("  length: %ld\n", length);
	printf("  value: %s\n", value);
}
