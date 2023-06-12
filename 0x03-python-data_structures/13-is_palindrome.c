#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *node = (*head);
	int *nums, i = 0, len = 0;

	if (!*head || !(*head)->next)
		return (1);

	nums = malloc(sizeof(int));

	while (node)
	{
		nums[len] = node->n;
		node = node->next;
		len++;
		nums = realloc(nums, sizeof(int) * len + 1);
	}

	while (i < len)
	{
		if (nums[i++] != nums[(len--) - 1])
		{
			free(nums);
			return (0);
		}
	}
	
	free(nums);
	return (1);
}
