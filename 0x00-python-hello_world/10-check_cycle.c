#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks a linked list in a cycle
 * @list: linked list to check
 * Return: no cycle = 0, cycle = 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
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
