def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    Count = 0
    Length = len(s)
    DicCount =[]
    for i in range(0,Length):
        if s[i] == '(':
            Count += 1
        else:
            Count -= 1
        DicCount.append(Count)
    LongSub = 0
    LocalLongSub = 0
    print DicCount
    for i in range(0,Length):
        if DicCount[i] < 0:
            LocalLongSub = 0
        elif DicCount[i]>0:
            LocalLongSub += 1
        else:
            LocalLongSub += 1
            if LocalLongSub > LongSub:
                LongSub = LocalLongSub
    return LongSub

s = '()'
print longestValidParentheses(s)
