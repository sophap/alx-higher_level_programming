#include "lists.h"

/**
 * is_palindrome - function to check if a singly linked list is a palindrome
 * @head: pointer to the first node in the linked list
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head, *temp = *head, *prev = NULL, *str;
	listint_t *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp != NULL && temp->next != NULL)
	{
		temp = temp->next->next;
		str = ptr->next;
		ptr->next = prev;
		prev = ptr;
		ptr = str;	
	}

	if (temp != NULL)
		second_half = ptr->next;
	else
		second_half = ptr;

	while (prev != NULL && second_half != NULL)
	{
		if (prev->n != second_half->n)
			return (0);
		prev = prev->next;
		second_half = second_half->next;
	}
	return (1);
}
