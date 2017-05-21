def canJump(nums):
    totalLen = len(nums)
    curPosition = 0
    canReach = 0
    while curPosition <= canReach and canReach < totalLen - 1:
        if nums[curPosition] + curPosition > canReach:
            canReach = nums[curPosition] + curPosition
        if canReach >= totalLen -1 :
            return True
        curPosition += 1
    if canReach >= totalLen - 1:
        return True
    return False

nums = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
print canJump(nums)
print canJump(nums2)