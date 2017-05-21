def halfSearch( nums, target, i ,j):
    if i>j:
        return -1
    p = (i+j)/2
    if nums[p]>target:
        return halfSearch(nums,target,i,p-1)
    elif nums[p]<target:
        return halfSearch(nums,target,p+1,j)
    else:
        return p
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    Length = len(nums)
    if nums[0]<=nums[Length -1]:
        return halfSearch(nums, target, 0, Length-1)
    p = 0
    q = Length -1
    while p < q:
        i = (p+q)/2
        if nums[i] < nums[Length-1]:
            q = i-1
        elif nums[i] >= nums[0]:
            p = i+1
    r  = p
    print r
    if nums[r]<=nums[Length-1]:
        MinIndex = r
    else:
        MinIndex = r+1
    print MinIndex
    if target >= nums[0]:
        return halfSearch(nums,target,0,MinIndex-1)
    else:
        return halfSearch(nums,target,MinIndex,Length-1)

nums = [8,9,2,3,4]
print search(nums,9)
