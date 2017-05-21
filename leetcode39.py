def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    All = []
    Results = []
    Index = {}
    for i in range(len(candidates)):
        if candidates[i] == target:
            Results.append([candidates[i]])
            i -= 1
            break
        Index[candidates[i]] = i
        All.append([candidates[i]])
    i += 1
    while All != []:
        LocalResults = []
        for EachArray in All:
            MaxNumber = EachArray[-1]
            for EachKey in candidates[Index[MaxNumber]:i]:
                if sum(EachArray) + EachKey == target:
                    Results.append(EachArray + [EachKey])
                elif sum(EachArray) + EachKey < target:
                    LocalResults.append(EachArray +[EachKey])
        All = LocalResults
    return Results

nums = [2,3,7]
print combinationSum(nums,18)