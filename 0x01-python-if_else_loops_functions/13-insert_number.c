#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts a node in a linked list
 * @head: pointer to the first element in the node
 * @num: node to be added
 * Return: the address to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = malloc(sizeof(listint_t));
	listint_t *prev;
	listint_t *h;

	h = *head;
	if (ptr == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}

	ptr->n = number;

	if (*head == NULL)
	{
		ptr->next = NULL;
		*head = ptr;
	}
	else
	{
		ptr->next = h;
		if (h == *head)
			*head = ptr;
		else
			prev->next = ptr;	
	}
	return (ptr);
}
