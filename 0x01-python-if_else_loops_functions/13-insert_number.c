#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first value in the singly linked list
 * @number: value to be inserted into the linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head;
	listint_t *ptr = NULL;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (temp != NULL && temp->n < number)
	{
		ptr = temp;
		temp = temp->next;
	}

	if (ptr == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		ptr->next = new;
		new->next = temp;
	}

	return (new);
}
