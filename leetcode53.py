def maxSubArray(nums):
    positive = []
    numPositive = 0
    maxNum = nums[0]
    for i in range(len(nums)):
        if nums[i] > 0:
            positive.append(i)
            numPositive += 1
        if nums[i] > maxNum:
            maxNum = nums[i]
    if numPositive <= 1:
        return maxNum
    preSum = 0
    maxSum = maxNum
    for i in range(1,len(positive)):
        start = positive[i-1]
        end = positive[i]
        partSum = sum(nums[start:end+1])
        localPreSum = sum(nums[start:end])
        if preSum > 0:
            partSum += preSum
            localPreSum += preSum
        if partSum > maxSum:
            maxSum = partSum
        preSum = localPreSum
    return maxSum

nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
print maxSubArray(nums)