Here are **10 of the most frequently asked algorithm questions** in JavaScript technical interviews, especially for frontend or full-stack roles:

---

### 1. **Two Sum**

**Problem:** Given an array of numbers and a target, return the indices of two numbers that add up to the target.
**Topic:** Hash Map
**Example:**
function getIndicesOf2Sum(numsArr, target) {
  const map = {};
  for (let i = 0; i < numsArr.length; i++) {
    const currentElem = numsArr[i];
    const diff = target - currentElem;
    if (map[diff] !== undefined) {
      return [map[diff], i];
    }
    map[currentElem] = i;
  }
}

const result  = getIndicesOf2Sum([1, 2, 0, 7, 15], 9);
console.log(result); // Output: [0, 1]

### 2. **Reverse a String**

**Problem:** Reverse a given string.
**Topic:** String manipulation

```js
function reverseString(str) {
  return str.split('').reverse().join('');
}
```

---

### 3. **Palindrome Check**

**Problem:** Check if a string is a palindrome.

```js
function isPalindrome(str) {
  str = str.replace(/[^a-z0-9]/gi, '').toLowerCase();
  return str === str.split('').reverse().join('');
}
```

---

### 4. **Fibonacci Sequence**

**Problem:** Return the `n`th Fibonacci number.
**Topic:** Recursion or DP

```js
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

---

### 5. **Factorial**

**Problem:** Find the factorial of a number.

```js
function factorial(n) {
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
```

---

### 6. **Valid Anagram**

**Problem:** Check if two strings are anagrams of each other.

```js
function isAnagram(s, t) {
  return s.split('').sort().join('') === t.split('').sort().join('');
}
```

---

### 7. **Merge Two Sorted Arrays**

**Problem:** Merge two sorted arrays into one sorted array.

```js
function mergeSortedArrays(arr1, arr2) {
  const merged = [];
  let i = 0, j = 0;
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) merged.push(arr1[i++]);
    else merged.push(arr2[j++]);
  }
  return merged.concat(arr1.slice(i)).concat(arr2.slice(j));
}
```

---

### 8. **Remove Duplicates from Array**

**Problem:** Remove duplicates from an array.

```js
function removeDuplicates(arr) {
  return [...new Set(arr)];
}
```

---

### 9. **Maximum Subarray (Kadane’s Algorithm)**

**Problem:** Find the contiguous subarray with the largest sum.

```js
function maxSubArray(nums) {
  let max = nums[0], curr = nums[0];
  for (let i = 1; i < nums.length; i++) {
    curr = Math.max(nums[i], curr + nums[i]);
    max = Math.max(max, curr);
  }
  return max;
}
```

---

### 10. **Binary Search**

**Problem:** Search for a target in a sorted array.

```js
function binarySearch(arr, target) {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    else if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}

Here are **common JavaScript interview questions related to sorting and grouping arrays**, along with example code snippets:

---

## 🔢 **Sorting Questions**

### 1. **Sort Numbers Ascending / Descending**

**Question:** Sort an array of numbers in ascending or descending order.

```js
const nums = [3, 1, 4, 1, 5, 9];

// Ascending
nums.sort((a, b) => a - b);

// Descending
nums.sort((a, b) => b - a);
```

---

### 2. **Sort Strings Alphabetically**

**Question:** Sort an array of strings alphabetically (case-insensitive).

```js
const words = ['banana', 'Apple', 'cherry'];
words.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
```

---

### 3. **Sort by Object Property**

**Question:** Sort an array of objects by a property, like age or name.

```js
const people = [
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 25 }
];

people.sort((a, b) => a.age - b.age); // Sort by age ascending
```

---

### 4. **Custom Sort (e.g., Even Numbers First)**

**Question:** Sort array so even numbers come before odd.

```js
const nums = [1, 2, 3, 4, 5, 6];
nums.sort((a, b) => (a % 2) - (b % 2));
```

---

## 🧮 **Grouping Questions**

### 5. **Group by Property**

**Question:** Group array of objects by a property (e.g., group users by role).

```js
const users = [
  { name: 'Alice', role: 'admin' },
  { name: 'Bob', role: 'user' },
  { name: 'Charlie', role: 'admin' }
];

const grouped = users.reduce((acc, user) => {
  (acc[user.role] = acc[user.role] || []).push(user);
  return acc;
}, {});
```

---

### 6. **Group Numbers by Even/Odd**

**Question:** Group numbers into even and odd arrays.

```js
const nums = [1, 2, 3, 4, 5];

const grouped = nums.reduce((acc, num) => {
  const key = num % 2 === 0 ? 'even' : 'odd';
  (acc[key] = acc[key] || []).push(num);
  return acc;
}, {});
```

---

### 7. **Group Words by First Letter**

**Question:** Group words by their starting letter.

```js
const words = ['apple', 'banana', 'apricot', 'blueberry'];

const grouped = words.reduce((acc, word) => {
  const first = word[0];
  (acc[first] = acc[first] || []).push(word);
  return acc;
}, {});
```

---

### 8. **Count Frequency of Elements**

**Question:** Count how many times each value appears in an array.

```js
const items = ['apple', 'banana', 'apple', 'orange'];

const frequency = items.reduce((acc, item) => {
  acc[item] = (acc[item] || 0) + 1;
  return acc;
}, {});
```

---

Here’s a **simple and clear example of prototypical inheritance in JavaScript**, using constructor functions and prototypes—**a common interview topic**.

---

## 🔧 **Example: Animal → Dog**

```js
// Parent constructor
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function() {
  return `${this.name} makes a noise.`;
};

// Child constructor
function Dog(name, breed) {
  Animal.call(this, name); // Call parent constructor
  this.breed = breed;
}

// Inherit from Animal
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Add Dog-specific method
Dog.prototype.bark = function() {
  return `${this.name} barks loudly!`;
};

// Usage
const dog1 = new Dog('Rex', 'German Shepherd');

console.log(dog1.speak()); // Rex makes a noise.
console.log(dog1.bark());  // Rex barks loudly!
console.log(dog1 instanceof Dog);     // true
console.log(dog1 instanceof Animal);  // true
```

---

## ✅ Key Concepts Demonstrated

* `Animal.call(this, name)` lets `Dog` inherit properties from `Animal`.
* `Object.create(Animal.prototype)` sets up the prototype chain.
* `Dog.prototype.constructor = Dog` restores the constructor reference.
* `dog1` inherits from both `Dog.prototype` and `Animal.prototype`.

---

### Bonus: ES6 Class Equivalent

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a noise.`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }

  bark() {
    return `${this.name} barks loudly!`;
  }
}
```

Here are **basic implementations in JavaScript** for:

1. ✅ **Stack**
2. 🌳 **Binary Tree (with node insertion)**
3. 🔁 **Binary Tree Traversals** (preorder, inorder, postorder, level-order)

---

## ✅ 1. Stack (LIFO)

```js
class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    return this.items.pop();
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }
}

// Usage
const stack = new Stack();
stack.push(10);
stack.push(20);
console.log(stack.pop()); // 20
console.log(stack.peek()); // 10
```

---

## 🌳 2. Binary Tree (with insert)

```js
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const newNode = new TreeNode(value);
    if (!this.root) return (this.root = newNode);

    const queue = [this.root];
    while (queue.length) {
      const current = queue.shift();
      if (!current.left) {
        current.left = newNode;
        return;
      } else if (!current.right) {
        current.right = newNode;
        return;
      }
      queue.push(current.left, current.right);
    }
  }
}
```

---

## 🔁 3. Binary Tree Traversals

### 🔼 Preorder (Root → Left → Right)

```js
function preorder(node) {
  if (!node) return;
  console.log(node.value);
  preorder(node.left);
  preorder(node.right);
}
```

### 🔽 Inorder (Left → Root → Right)

```js
function inorder(node) {
  if (!node) return;
  inorder(node.left);
  console.log(node.value);
  inorder(node.right);
}
```

### ⬇️ Postorder (Left → Right → Root)

```js
function postorder(node) {
  if (!node) return;
  postorder(node.left);
  postorder(node.right);
  console.log(node.value);
}
```

### 🌐 Level-order (BFS)

```js
function levelOrder(root) {
  if (!root) return;
  const queue = [root];
  while (queue.length) {
    const node = queue.shift();
    console.log(node.value);
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
}
```

---

## 🧪 Example Usage

```js
const tree = new BinaryTree();
tree.insert(1);
tree.insert(2);
tree.insert(3);
tree.insert(4);
tree.insert(5);

console.log("Inorder:");
inorder(tree.root);
```


