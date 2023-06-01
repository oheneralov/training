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



/*
palindrome
*/

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const xAsStr = x.toString();
    const reverseX = xAsStr.split('').reverse();
    return xAsStr === reverseX.join('');
    
};

