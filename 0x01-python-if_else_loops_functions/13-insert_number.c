#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the linked list
 * @number: integer to add
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node = *head;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	while (node)
	{
		if (node->n < number && node->next->n > number)
		{
			new->next = node->next;
			node->next = new;
			break;
		}
		node = node->next;
	}
	return (new);
}
