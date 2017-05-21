def intToRoman(num):
    One = num % 10
    num = num/10
    Ten = num % 10
    num = num/10
    Hundred = num % 10
    num = num/10
    Thousand = num % 10
    num = num/10

    Roman = ''
    if Thousand > 0:
        for i in range(0,Thousand):
            Roman += 'M'
    if Hundred == 9:
        Roman += 'CM'
    elif Hundred <=8 and Hundred >=5:
        Roman += 'D'
        for i in range(0,Hundred-5):
            Roman += 'C'
    elif Hundred == 4:
        Roman += 'CD'
    elif Hundred >= 0 and Hundred <= 3:
        for i in range(0,Hundred):
            Roman += 'C'
    
    if Ten == 9:
        Roman += 'XC'
    elif Ten <=8 and Ten >=5:
        Roman += 'L'
        for i in range(0,Ten-5):
            Roman += 'X'
    elif Ten == 4:
        Roman += 'XL'
    elif Ten >= 0 and Ten <= 3:
        for i in range(0,Ten):
            Roman += 'X'

    if One == 9:
        Roman += 'IX'
    elif One <=8 and One >=5:
        Roman += 'V'
        for i in range(0,One-5):
            Roman += 'I'
    elif One == 4:
        Roman += 'IV'
    elif One >= 0 and One <= 3:
        for i in range(0,One):
            Roman += 'I'
    return Roman


num = 3888
print intToRoman(num)
