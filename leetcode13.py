def romanToInt(s):
    Length = len(s)
    Number = 0
    for i in range(0,Length):
        if s[i] == 'M':
            Number += 1000
        elif s[i] == 'C':
            if i<Length-1 and (s[i+1] == 'M' or s[i+1] == 'D'):
                Number -= 100
            else:
                Number += 100
        elif s[i] == 'D':
            Number += 500
        elif s[i] == 'X':
            if i<Length-1 and (s[i+1] == 'C' or s[i+1] == 'L'):
                Number -= 10
            else:
                Number += 10
        elif s[i] == 'L':
            Number += 50
        elif s[i] == 'I':
            if i<Length-1 and (s[i+1]=='X' or s[i+1] == 'V'):
                Number -= 1
            else:
                Number += 1
        elif s[i] == 'V':
            Number += 5
    return Number

s = 'MMMCMXCIX'
print romanToInt(s)
