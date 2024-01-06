data_structures
The main difference between tuples and lists is that tuples can't be changed after they're created, but lists can be modified. Tuples use less memorythan lists. They are also a bit faster, especially when you're just looking up values. So, if you have data that you don't want to change, it's better to use tuples instead of lists.<br>
--Tuple--<br>
[1] tuple items are enclosed in parentheses(but you can remove it)<br>
[2] tuple are ordred<br>
[3] tuple are immutable you cant add or delete<br>
[4] tuple items is not unique<br>
[5] tuple can have different data types<br>
<br>
***************************************************************<br>
<br>
different techniques to copy a list:<br>
	The assignment operator<br>
	The slicing syntax<br>
	The list.copy() method<br>
	The copy.copy() function<br>
	The copy.deepcopy() function<br>
to copy a list without changing the original use list.copy() instead of the assignment operator method<br>
<br>
you can convert list to string using .join function "".join(list)<br>
