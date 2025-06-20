class Solution(object):
    def twoSum(self, nums, target):
        """
        Given a list of integers `nums` and an integer `target`,
        return the indices of the two numbers such that they add up to `target`.

        Constraints (from the problem):
        • Exactly one valid answer exists.
        • You may not use the same element twice.

        Complexity
        ----------
        Time  : O(n)   – one pass through `nums`
        Space : O(n)   – hash map to store seen numbers
        """

        # ----------------------------------------
        # 1)  Create an empty dictionary (hash map)
        #     Key   -> number we've seen so far
        #     Value -> index of that number in `nums`
        # ----------------------------------------
        lookup = {}

        # ----------------------------------------
        # 2)  Iterate over the array with enumerate
        #     `i` is the current index
        #     `x` is the current value at nums[i]
        # ----------------------------------------
        for i, x in enumerate(nums):

            # a) Compute the value we need to reach the target with `x`
            comp = target - x

            # b) If that complementary value has been seen before,
            #    it's already in `lookup`. We’ve found the answer!
            if comp in lookup:
                # Return indices as a list (any order is fine)
                return [lookup[comp], i]

            # c) Otherwise, record the current number and its index
            #    so it can serve as a complement for future elements.
            lookup[x] = i

        # We never reach this point because the problem guarantees
        # there is always exactly one solution.
