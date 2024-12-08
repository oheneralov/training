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


# 10. Creating a stack
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

# 11. A simple Python program to introduce a linked list

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



# 12. A simple Python program for traversal of a linked list

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

# 13.  balanced brackets.

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

# 14. A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)        
    while not myQueue.isEmpty():
        print(myQueue.delete())


customers = []
customers.append((2, "Harry")) #no sort needed here because 1 item. 
customers.append((3, "Charles"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((1, "Riya"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((4, "Stacy"))
customers.sort(reverse=True)
while customers:
     print(customers.pop(0))
#Will print names in the order: Stacy, Charles, Harry, Riya. 

# 15. importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))

# Python program to introduce Binary Tree

# 16. A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Node(1)
''' following is the tree after above statement
        1
    / \
    None None'''

root.left     = Node(2);
root.right     = Node(3);

''' 2 and 3 become left and right children of 1
        1
        / \
        2     3
    / \ / \
None None None None'''


root.left.left = Node(4);
'''4 becomes left child of 2
        1
    /     \
    2         3
    / \     / \
4 None None None
/ \
None None'''

# 17. Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):

    if root:

        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)

# 18. Python program to print level
# order traversal using Queue

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):

    # Base Case
    if root is None:
        return
    
    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
    
        # Print front of queue and
        # remove it from queue
        print (queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)


# find the missing number in an array of integers from 1 to n (where the array has n−1 elements).
# JS
function findMissingNumber(arr, n) {
    // Calculate the expected sum of numbers from 1 to n
    const expectedSum = (n * (n + 1)) / 2;
    // Calculate the actual sum of elements in the array
    const actualSum = arr.reduce((sum, num) => sum + num, 0);
    // The missing number is the difference
    return expectedSum - actualSum;
}
const arr = [1, 2, 4, 5, 6];  // n = 6
console.log(findMissingNumber(arr, 6));  // Output: 3


# python
def find_missing_number(arr, n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference
    return expected_sum - actual_sum

# Example usage
arr = [1, 2, 4, 5, 6]  # n = 6
print(find_missing_number(arr, 6))  # Output: 3

// JavaScript program to print level
// order traversal using Queue

class Node {
    constructor(key) {
        this.data = key;
        this.left = null;
        this.right = null;
    }
}

// Iterative method to print the
// level order traversal of a binary tree
function printLevelOrder(root) {

    if (root === null) return;

    // Create an empty queue for
    // level order traversal
    const queue = [];

    // Enqueue root
    queue.push(root);

    while (queue.length > 0) {
    
        // Print front of queue and
        // remove it from queue
        const node = queue.shift();
        console.log(node.data);

        // Enqueue left child
        if (node.left !== null) {
            queue.push(node.left);
        }

        // Enqueue right child
        if (node.right !== null) {
            queue.push(node.right);
        }
    }
}

const root = new Node(1);
root.left = new Node(2);
const root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);
printLevelOrder(root);



# Python program to print level
# order traversal using Queue

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):

    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printLevelOrder(root)
