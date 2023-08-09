#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle in it.
 * @list: beginning of the node pointer
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *now, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	now = list;
	check = now->next;

	while (now != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (now == check)
			return (1);
	now = now->next;
		check = check->next->next;
	}
	return (0);
}
