import random
a = [random.randrange(0,100000) for p in range (0,1001)]


def bubblesort(arr):
	switched = False;
	for index in range(0,len(arr) - 1):
		if (arr[index] > arr[index + 1]):
			arr[index],arr[index + 1] = arr[index + 1],arr[index]
			switched = True;
 	if switched is True:
 		bubblesort(arr);
 		return arr;

print bubblesort(a);