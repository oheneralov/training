"""
/*
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++){
        for (let j = i + 1; j < nums.length; j++){

            if(nums[i] + nums[j] === target) {
                return [i, j]
            }

        }
    }
    
};

/*
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const result = Array.from(new Set(nums))
    nums.forEach((elem, index, arr) => arr[index] = result[index])
    
    return result.length;
};

"""

"""
palindrome
"""

"""
 * @param {number} x
 * @return {boolean}
"""
def isPalindrome(x):
    xAsStr = str(x);
    reverseX = xAsStr[::-1];
    return xAsStr == reverseX; 

print(isPalindrome(123))
print(isPalindrome(121))


"""
remove duplicates
"""
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist) 


# 1. Remove any duplicates from a List:
def remove_duplicates():
    mylist = ["a", "b", "a", "c", "c"]
    mylist = list(dict.fromkeys(mylist))
    print(mylist)

#or
# 1. using set() to remove duplicated from list
def remove_duplicates2():
    test_list = list(set(mylist))

# 1. using list comprehension to remove duplicated from list
def remove_duplicates3():
    res = []
    [res.append(x) for x in mylist if x not in res]

### Time Complexity: O(n)
### Space Complexity: O(n)

#R 2. Reverse the string "Hello World":
def reverse_string():
    txt = "Hello World"[::-1]
    print(txt)

# 3.  add 2 numbers
def add_2_numbers():
    x = input("Type a number: ")
    y = input("Type another number: ")
    sum = int(x) + int(y)
    print("The sum is: ", sum)

# 4.  count frequency of words in a list
def freq_words():
    str=input("Enter a string")
    li=str.split()
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

# 4. Python Cyclically Rotate an Array by One Using List Slicing
def cyclicRotate(input):
    print([input[-1]] + input[0:-1])

# 5. Numbers in a list within a given range
def count(list1, l, r):     
    # x for x in list1 is same as traversal in the list
    # the if condition checks for the number of numbers in the range 
    # l to r 
    # the return is stored in a list
    # whose length is the answer
    return len(list(x for x in list1 if l <= x <= r))

# 6. Count the number of 1 bits in python
def count_bits(i):
    print(bin(i))
    # 0b1100100
    print(i.bit_count())

def bit_count2(self):
    return bin(self).count("1")

# 7. Bubble sort in Python
"""
Time Complexity	 
Best	O(n)
Worst	O(n2)
Average	O(n2)
"""
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# 8. function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


# 9. Given an array of integers nums and an integer target,
# return the indices of the two numbers that add up to the target.
# Solution 1: Brute Force Approach. Time Complexity: O(n²)
class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
  
"""
Solution 2: Two-Pass Hash Table
Explanation
We use a dictionary to reduce the time complexity. First, we add each element and its index to a dictionary.
Then, we iterate through the array again and check if each element’s complement (target — element) exists in the dictionary.
Time Complexity: O(n)
Python Code:
"""
class Solution2(object):
  def twoSum(self, nums, target):
    numMap = {}
    for i, num in enumerate(nums):
        numMap[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []
  
  
class Solution3(object):
    def twoSum(self, nums, target):
      numMap = {}
      for i, num in enumerate(nums):
          complement = target - num
          if complement in numMap:
            return [numMap[complement], i]
          numMap[num] = i
      return []
    
# Stack implementation in python
# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()

 
# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    cyclicRotate(input)
    count_bits(100)
    data = [-2, 45, 0, 11, -9]
    bubbleSort(data)
    print(data)

    data = [8, 7, 2, 1, 0, 9, 6]
    print("Unsorted Array")
    print(data)

    size = len(data)

    quickSort(data, 0, size - 1)

    print('Sorted Array in Ascending Order:')
    print(data)

    stack = create_stack()
    push(stack, str(1))
    push(stack, str(2))
    push(stack, str(3))
    push(stack, str(4))
    print("popped item: " + pop(stack))
    print("stack after popping an element: " + str(stack))

# A simple Python program to introduce a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)



# A simple Python program for traversal of a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next


# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node

    llist.printList()

# balanced brackets.

# function to check if
# brackets are balanced


def areBracketsBalanced(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"

    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")








