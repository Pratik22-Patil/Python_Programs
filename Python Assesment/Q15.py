def Greater(nums):
    for i in range(nums):
        if i > 50 and i % 2 == 0:
            print(i)
        else:
            return None

nums = [10, 47, 53, 60, 33]   
result = Greater(nums)         
print(result)