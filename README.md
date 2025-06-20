

```markdown
# 🧠 LeetCode Solutions

Welcome to my repository of solved LeetCode problems! This is part of my personal DSA learning journey and my **100 Days of LeetCode Challenge**.

---

## ✅ Solved Problems

| Day | Problem | Difficulty | Topic | Solution |
|-----|---------|------------|--------|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Arrays, Hash Table | [View Code](./Arrays/0001_Two_Sum.py) |

---

## 📌 Problem: Two Sum

### 📝 Description:

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that they add up to the target.

- You may **assume that each input would have exactly one solution**
- You **may not use the same element twice**
- You can return the answer **in any order**

---

### 💡 Examples:

#### ✅ Example 1:
```

Input: nums = \[2,7,11,15], target = 9
Output: \[0,1]
Explanation: Because nums\[0] + nums\[1] == 9, we return \[0, 1].

```

#### ✅ Example 2:
```

Input: nums = \[3,2,4], target = 6
Output: \[1,2]

```

#### ✅ Example 3:
```

Input: nums = \[3,3], target = 6
Output: \[0,1]

```

---

### 📏 Constraints:
- 2 <= nums.length <= 10⁴  
- -10⁹ <= nums[i] <= 10⁹  
- -10⁹ <= target <= 10⁹  
- **Only one valid answer exists**

---

### 🔍 Follow-up:
> Can you come up with an algorithm that is less than O(n²) time complexity?

---

## 🔧 My Approach:

We use a **hash map (dictionary)** to keep track of numbers we've seen and their indices.

### ✅ Steps:
1. Loop through the array using `enumerate()`
2. For each number `x`, check if `target - x` is already in the dictionary
3. If yes, return the indices: `[lookup[target - x], current_index]`
4. Otherwise, store `x` in the dictionary with its index

### 🧠 Time Complexity:
- **O(n)** — one pass through the array with constant time dictionary lookups

---

⭐ *If you like this repo, don’t forget to star it and follow along!*
```

---


