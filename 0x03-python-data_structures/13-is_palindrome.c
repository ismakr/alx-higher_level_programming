#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the linkedlist
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *end;
	listint_t *start;
	int *arr;
	int num;
	int i, j;

	end = *head;
	start = *head;
	num  = 0;
	while (end != NULL)
	{
		num += 1;
		end = end->next;
	}
	arr = malloc(sizeof(int) * num);
	i = 0;
	while (start != NULL)
	{
		arr[i] = start->n;
		start = start->next;
		i++;
	}
	i = 0;
	j = num - 1;
	while (i < j)
	{
		if (arr[i] == arr[j])
		{
			j--;
			i++;
		}
		else
			return (0);
	}
	return (1);
}
