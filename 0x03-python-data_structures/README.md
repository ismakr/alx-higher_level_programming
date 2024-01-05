data_structures
The main difference between tuples and lists is that tuples can't be changed after they're created, but lists can be modified. Tuples use less memory than lists. They are also a bit faster, especially when you're just looking up values. So, if you have data that you don't want to change, it's better to use tuples instead of lists.
***************************************************************
different techniques to copy a list:
	The assignment operator
	The slicing syntax
	The list.copy() method
	The copy.copy() function
	The copy.deepcopy() function
to copy a list without changing the original use list.copy() instead of the assignment operator method
