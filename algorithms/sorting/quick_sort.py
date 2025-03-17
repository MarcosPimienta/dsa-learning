# Quick sort algorithm

def quick_sort(nums):
  """Sort by recursion and concatenation"""

  if len(nums) <= 1:
    return nums

  pivot = nums[len(nums)//2]
  left = [i for i in nums if i < pivot]
  mid = [i for i in nums if i == pivot]
  right = [i for i in nums if i > pivot]

  return quick_sort(left) + mid + quick_sort(right)

nums_list = [100, 5, 54, 86, 41, 90, 32, 1, 22]
print(f"Sorted list quick: {quick_sort(nums_list)}")