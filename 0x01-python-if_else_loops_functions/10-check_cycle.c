#include "lists.h"

/**
 * check_cycle - linked list with cycle
 * @list: check linked list
 *
 * Return: 0 if doesnt , 1 if the list has acycle
 */
int check_cycle(listint_t *list)
{
	listin_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
