#include <stdlib.h>
#include "lists.h"

/**
 *check_cycle - checks if a singlg linkeed list has a cycle
 *@list: a singly linked list to be checked
 *
 *Return: no clycle (0), cycle(1)
 */

int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (list == NULL || list->next == NULL)
		return(0);

	a = list->next;
	b = list->next->next;

	while (a && b && b->next)
	{
		if (a == b)
			return (1);

		a = a->next;
		b = b->next->next;
	}
	return (0);
}
