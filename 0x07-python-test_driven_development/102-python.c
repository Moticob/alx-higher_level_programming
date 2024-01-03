#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{
    PyObject *str, *repr;

    (void)repr;
    printf("[.] string object info\n");

    if (strcmp(p->ob_type->tp_name, "str"))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    repr = PyObject_Repr(p);
    str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

    Py_ssize_t length = PyUnicode_GET_SIZE(p);
    printf("  length: %ld\n", length);

    const char *value_str = PyBytes_AsString(str);
    Py_ssize_t i = 0;

    printf("  value: ");

    while (i < length)
    {
        putchar(value_str[i]);
        i++;
    }

    printf("\n");
}

