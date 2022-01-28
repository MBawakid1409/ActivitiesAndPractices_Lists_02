# Activities & Practices

# 01 "Every Three Numbers"
# Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter. Here is what we need to do:

# 1. Define the function to accept one parameter for our starting number
# 2. Calculate the numbers between the starting number and 100 while incrementing by 3
# 3. Store the numbers in a list
# 4. Return the list

# Create a function called [every_three_nums] that has one parameter named [start].
# The function should return a list of every third number between [start] and [100] (inclusive). For example, [every_three_nums(91)] should return the list [[91, 94, 97, 100]]. If [start] is greater than [100], the function should return an empty list.

# Hint: We can generate the numbers in a certain range by a certain increment using the [range()] function. In order to convert the range sequence into a list, we can pass it into the [list()] function.

print("'Every Three Numbers' challenge")
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
# Note: I clicked on "View Solution"
print("--------------------------------")

# 02 "Remove Middle"
# Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index should be removed from the list. Here are the steps:

# 1. Define the function to accept three parameters: the list, the starting index, and the ending index
# 2. Get all elements before the starting index
# 3. Get all elements after the ending index
# 4. Combine the two partial lists into the result
# 5. Return the result

# Create a function named [remove_middle] which has three parameters named [lst], [start], and [end].
# The function should return a list where all elements in [lst] with an index between [start] and [end] (inclusive) have been removed.
# For example, the following code should return [[4, 23, 42]] because elements at indices [1], [2], and [3] have been removed:
# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

# Hint: To make this problem easier, we can use slicing. For example, if we wanted all elements up to a certain index we can use lst[:index] and to get all elements after a certain index we can use lst[index+1:].

print("'Remove Middle' challenge")
def remove_middle(lst, start, end):
  list1 = lst[:start] + lst[end+1:]
  return list1
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))  
print("--------------------------------")
# Note: I've kept thinking about a solution for some time until I clicked on "View Solution" 

# 03 "More Frequent Item"
# Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

# 1. Define the function to accept three parameters: the list, the first item, and the second item
# 2. Count the number of times [item1] shows up in our list
# 3. Count the number of times [item2] shows up in our list
# 4. If [item1] shows up more, return [item1]. Otherwise, return [item2]

# Create a function named [more_frequent_item] that has three parameters named [lst], [item1], and [item2].
# Return either [item1] or [item2] depending on which item appears more often in [lst].
# If the two items appear the same number of times, return [item1].
print("'More Frequent Item' challenge")
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  return item2 

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))   
print("--------------------------------")

# 04 "Double Index"
# Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

# 1. Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
# 2. Test if the index is invalid. If its invalid then return the original list
# 3. If the list is valid then get all values up to the index and store it as a new list
# 4. Append the value at the index times 2 to the new list
# 5. Add the rest of the list from the index onto the new list
# 6. Return the new list

# Create a function named [double_index] that has two parameters: a list named [lst] and a single number named [index].
# The function should return a new list where all elements are the same as in [lst] except for the element at [index]. The element at [index] should be double the value of the element at [index] of the original [lst].
# If [index] is not a valid index, the function should return the original list.
# For example, the following code should return [[1,2,6,4]] because the element at index [2] has been doubled:
# double_index([1, 2, 3, 4], 2)
# After writing your function, un-comment the call to the function that we’ve provided for you to test your results.

# Hint: We can use slicing to get the values up to an index [lst[0:index]] and from an index to the end [lst[index+1:]]. Also, to append to the end of a list we can use the [append()] function.

print("'Double Index' challenge")
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
print("--------------------------------")
# Note: I've kept thinking about a solution for some time until I clicked on "View Solution" 

# 05 "Middle Item"
# For the final code challenge, we are going to create a function that finds the middle item from a list of values. This will be different depending on whether there are an odd or even number of values. In the case of an odd number of elements, we want this function to return the exact middle value. If there is an even number of elements, it returns the average of the middle two elements. Here is what we need to do:

# 1. Define the function to accept one parameter for our list of numbers
# 2. Determine if the length of the list is even or odd
# 3. If the length is even, then return the average of the middle two numbers
# 4. If the length is odd, then return the middle number

# Create a function called [middle_element] that has one parameter named [lst].
# If there are an odd number of elements in [lst], the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

# Hint: Remember to use modulus % to determine if a number is divisible by 2. If len(lst) % 2 == 0 then the number is even. If we divide the length of the list by 2 we can get the middle element index. We then need to convert that value into an integer and access element at that index. This will look something like: lst[int(len(lst)/2)].
print("'Middle Item' challenge")
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))    
print("--------------------------------")
# Note: I've kept thinking about a solution for some time until I clicked on "View Solution" 