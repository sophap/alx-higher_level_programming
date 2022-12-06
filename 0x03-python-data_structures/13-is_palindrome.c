#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if linked list is palindrome
 * @head: the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int length;
	int count = 0;
	int i;
	listint_t *ptr;

	if (!head || !*head)
		return (1);

	ptr = *head;

	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}

	length = count + 1;
	int *arr = malloc(sizeof(int) * length);

	ptr = *head;
	count = 0;
	while (ptr != NULL)
	{
		arr[count] = ptr->n;
		count++;
		ptr = ptr->next;
	}
	for (i = 0; i < count / 2; i++)
	{
		if (arr[i] == arr[(count - 1) - i])
		{
			continue;
		}
		else
		{
			return (0);
		}
	}
	free(arr);
	return (1);
}
