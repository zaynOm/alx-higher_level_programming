#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *node = (*head);
	int *nums, i = 0, len = 0;

	nums = malloc(sizeof(int));

	while (node)
	{
		nums[len] = node->n;
		node = node->next;
		len++;
	}

	while (i < len)
	{
		if (nums[i++] != nums[(len--) - 1])
			return (0);
	}

	return (1);
}
