# Merge sort algorithm

def merge(left, right):
  """Lists merge function"""

  merged = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  merged.extend(left[i:])
  merged.extend(right[j:])

  return merged

def merge_sort(nums):
  """Sort by splitting recursively"""

  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2
  left = nums[:mid]
  right = nums[mid:]

  left_sort = merge_sort(left)
  right_sort = merge_sort(right)

  merged_sort = merge(left_sort, right_sort)
  return merged_sort

nums_list = [100, 5, 54, 86, 41, 90, 32, 1, 22]
print(f"Sorted list: {merge_sort(nums_list)}")
