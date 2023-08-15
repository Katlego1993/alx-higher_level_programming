#include <Python.h>

/**
 * print_python_list_info - Prints basic of Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int s, al, a;
	PyObject *obj;

	s = Py_SIZE(p);
	al = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", al);

	for (a = 0; a < size; a++)
	{
		printf("Element %d: ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
