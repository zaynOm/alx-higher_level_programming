#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *node = (*head);
	int nums[2048], i = 0, len = 0;

	if (!*head || !(*head)->next)
		return (1);

	while (node)
	{
		nums[len++] = node->n;
		node = node->next;
	}

	while (i < len)
	{
		if (nums[i++] != nums[(len--) - 1])
			return (0);
	}

	return (1);
}
