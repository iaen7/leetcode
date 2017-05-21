def generateParenthesis(n):
    LeftIndex = leftIndex(n)
    Result = []
    for eachLeftIndex in LeftIndex:
        String = ''
        for i in range(0,2*n):
            if i in eachLeftIndex:
                String +='('
            else:
                String +=')'
        Result.append(String)
    return Result
    

def leftIndex(n):
    if n == 1:
        return [[0]]
    else:
        LastLeftIndex = leftIndex(n-1)
        NewLeftIndex = []
        for LeftIndex in LastLeftIndex:
            LocalMax = LeftIndex[-1]
            LeftGreaterRight = 2*n-3-LocalMax
            for j in range(LocalMax+1,LocalMax+2+LeftGreaterRight):
                GLeftIndex = LeftIndex + [j]
                NewLeftIndex.append(GLeftIndex)
    return NewLeftIndex
print generateParenthesis(3)
