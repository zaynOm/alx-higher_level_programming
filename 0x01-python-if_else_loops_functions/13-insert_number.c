#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node = *head;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node)
	{
		if (node->n < number && node->next->n > number)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}
	node->next = new;
	return (new);
}
