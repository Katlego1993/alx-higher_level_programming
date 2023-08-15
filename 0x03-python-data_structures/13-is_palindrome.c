#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a linked listint_t .
 * @head: A pointer head to reverse.
 *
 * Return: A pointer of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a list is a palindrome.
 * @head: A pointer of the linked list.
 *
 * Return: 0 if not palindome or 1 if its palindrome 
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t s = 0, a;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		s++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (a = 0; a < (s / 2) - 1; a++)
		tmp = tmp->next;

	if ((s % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}

