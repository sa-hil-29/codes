def missingNumber(nums):
    n = len(nums)
    sum = 0
    for num in nums:
        sum += num
    missing = (n * (n+1))//2 - sum
    return missing

print(missingNumber([0,1]))
      
