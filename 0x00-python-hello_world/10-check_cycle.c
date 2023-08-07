#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *str, *tmp;
	
	if (list == NULL)
		return (0);

	str = list;
	tmp = list->next;

	while (tmp != NULL && tmp->next != NULL)
	{
		if (str == tmp)
			return (1);

		 str = str->next;
		 tmp = tmp->next->next;
	}
	return (0);
}
