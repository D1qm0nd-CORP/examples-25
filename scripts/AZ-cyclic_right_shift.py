#FIX 9/10

nums = input().split()
last = nums[len(nums)-1]
nums.remove(last)
nums = [last] + nums

for x in nums:
    print(x, end=" ")
