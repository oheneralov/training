from collections import defaultdict

import re

def sort_logs_by_service(log_text):
    # Regex to extract log components
    log_pattern = r"^(.*?)\s+(INFO|WARN|ERROR|DEBUG)\s+\[(.*?)\]\s+(.*)$"
    
    logs = []
    for line in log_text.strip().splitlines():
        match = re.match(log_pattern, line)
        if match:
            timestamp, level, service, message = match.groups()
            # convert string to object
            logs.append({
                "timestamp": timestamp,
                "level": level,
                "service": service,
                "message": message,
                "original": line
            })

    # Sort by service name
    sorted_logs = sorted(logs, key=lambda x: x["service"])

    # Return sorted original log lines
    return [entry["original"] for entry in sorted_logs]

with open('log.txt', 'r') as f:
    dict = defaultdict(str)
    log_text = f.read()
    print(sort_logs_by_service(log_text))
    # save to file
    with open('sorted_log.txt', 'w') as sorted_file:
        sorted_file.write('\n'.join(sort_logs_by_service(log_text)))


from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(3,5)
    host = "https://google.com"

    @task
    def index(self):
        self.client.get(self.host)


from collections import Counter

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


text = "machinelearning"
sorted_text = ''.join(sorted(text, reverse=True))
print(sorted_text)

# sort numbers in list
def sort_numbers_desc(arr):
    return sorted(arr, reverse=True)


#. Get letters count in a string
def letter_counts(text):
    counts = {}
    for char in text:
        if char.isalpha():  # consider letters only
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1
    return counts

from collections import Counter

text = "machinelearning"
letter_counts = Counter(text)
print(letter_counts)

# group by date and sort by price
from collections import defaultdict

def group_by_date_sorted_by_price(items):
    grouped = defaultdict(list)
    for item in items:
        grouped[item['date']].append(item)
    
    # Sort each group by price
    for date in grouped:
        grouped[date].sort(key=lambda x: x['price'])
    
    return dict(grouped)

"""
data = [
    {'date': '2025-06-01', 'price': 20, 'item': 'B'},
    {'date': '2025-06-01', 'price': 10, 'item': 'A'},
    {'date': '2025-06-01', 'price': 15, 'item': 'C'},
    {'date': '2025-06-02', 'price': 10, 'item': 'D'},
    {'date': '2025-06-02', 'price': 5,  'item': 'E'},
]

grouped = group_by_date_sorted_by_price(data)
for date, items in grouped.items():
    print(f"{date}: {items}")

"""


# 1. Two Sum
def two_sum(nums, target):
    """Find two numbers that add up to a target."""
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# 2. Palindrome Number
def is_palindrome_number(x):
    """Check if an integer is a palindrome."""
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# 3. Roman to Integer
def roman_to_integer(s):
    """Convert a Roman numeral to an integer."""
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        current_value = roman_map[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total

# 4. Longest Common Prefix
def longest_common_prefix(strs):
    """Find the longest common prefix among a list of strings."""
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# 5. Valid Parentheses
def is_valid_parentheses(s):
    """Check if parentheses in a string are valid."""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# 6. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    """Merge two sorted linked lists into one."""
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next

# 7. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    """Remove duplicates from sorted array in-place."""
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index

# 8. Remove Element
def remove_element(nums, val):
    """Remove all instances of a given value in-place."""
    write_index = 0
    for num in nums:
        if num != val:
            nums[write_index] = num
            write_index += 1
    return write_index

# 9. Implement strStr()
def str_str(haystack, needle):
    """Find the index of the first occurrence of a substring."""
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

# 10. Search Insert Position
def search_insert(nums, target):
    """Return the index to insert a target value."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 11. Length of Last Word
def length_of_last_word(s):
    """Return the length of the last word in a string."""
    return len(s.strip().split()[-1])

# 12. Plus One
def plus_one(digits):
    """Add one to a number represented by a list of digits."""
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# 13. Add Binary
def add_binary(a, b):
    """Add two binary strings."""
    return bin(int(a, 2) + int(b, 2))[2:]

# 14. Climbing Stairs
def climbing_stairs(n):
    """Count ways to climb stairs taking 1 or 2 steps at a time."""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# 15. Sqrt(x)
def sqrt_x(x):
    """Return the integer square root of a non-negative integer."""
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

# 16. Single Number
def single_number(nums):
    """Find the number that appears once in a list where others appear twice."""
    result = 0
    for num in nums:
        result ^= num
    return result

# 17. Valid Anagram
def is_valid_anagram(s, t):
    """Check if two strings are anagrams."""
    return sorted(s) == sorted(t)

# 18. Binary Search
def binary_search(nums, target):
    """Implement the binary search algorithm."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 19. Guess Number Higher or Lower
def guess_number(n, pick):
    """Use binary search to guess a number."""
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if mid == pick:
            return mid
        elif mid < pick:
            left = mid + 1
        else:
            right = mid - 1

# 20. First Bad Version
def first_bad_version(n, is_bad_version):
    """Find the first bad version using binary search."""
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left

# 21. Intersection of Two Arrays II
def intersect(nums1, nums2):
    """Find the intersection of two arrays including duplicates."""
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result

# 22. Move Zeroes
def move_zeroes(nums):
    """Move all zeroes to the end of the array in-place."""
    write_index = 0
    for num in nums:
        if num != 0:
            nums[write_index] = num
            write_index += 1
    for i in range(write_index, len(nums)):
        nums[i] = 0

# 23. Find the Difference
def find_the_difference(s, t):
    """Find the extra letter added in a shuffled string."""
    counts_s = Counter(s)
    counts_t = Counter(t)
    for char in counts_t:
        if counts_t[char] != counts_s.get(char, 0):
            return char

# 24. Relative Ranks
def find_relative_ranks(score):
    """Assign ranks to athletes based on their scores."""
    sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
    ranks = [""] * len(score)
    for i, (index, _) in enumerate(sorted_scores):
        if i == 0:
            ranks[index] = "Gold Medal"
        elif i == 1:
            ranks[index] = "Silver Medal"
        elif i == 2:
            ranks[index] = "Bronze Medal"
        else:
            ranks[index] = str(i + 1)
    return ranks

# 25. Fizz Buzz
def fizz_buzz(n):
    """Return a list of strings with FizzBuzz rules."""
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# 26. Detect Capital
def detect_capital_use(word):
    """Check if capital usage in a word is correct."""
    return word.isupper() or word.islower() or word.istitle()

# 27. Reverse String
def reverse_string(s):
    """Reverse a string in-place."""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 28. Reverse Words in a String III
def reverse_words(s):
    """Reverse each word in a sentence."""
    return ' '.join(word[::-1] for word in s.split())

# 29. Max Consecutive Ones
def find_max_consecutive_ones(nums):
    """Find the maximum number of consecutive 1s in a binary array."""
    max_count = count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

# 30. Count and Say
def count_and_say(n):
    """Generate the nth term of the count-and-say sequence."""
    result = "1"
    for _ in range(n - 1):
        current = []
        count = 1
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1
            else:
                current.append(f"{count}{result[i - 1]}")
                count = 1
        current.append(f"{count}{result[-1]}")
        result = ''.join(current)
    return result

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
