def generateParenthesis(n):
    if n == 1:
        return ['()']
    else:
        Result = []
        Union = generateParenthesis(n-1)
        for Element in Union:
            NewString = '('
            NewString += Element
            NewString += ')'
            if NewString not in Result:
                Result.append(NewString)
        for i in range(1,n):
            j = n-i
            Union1 = generateParenthesis(i)
            Union2 = generateParenthesis(j)
            for String1 in Union1:
                for String2 in Union2:
                    NewString = String1+String2
                    if NewString not in Result:
                        Result.append(NewString)
    return Result

print generateParenthesis(100)
