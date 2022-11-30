#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list
 * Return: 0 if there is no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *str = list;

	while (ptr && str && str->next)
	{
		ptr = ptr->next;
		str = str->next->next;
		if (ptr == str)
		{
			return (1);
		}
	}
	return (0);
}
