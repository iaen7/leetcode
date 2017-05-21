def groupAnagrams(strs):
    dicWord = {}
    res = []
    curPosition = -1
    for str in strs:
        listStr = []
        for alpha in str:
            listStr.append(alpha)
        listStr.sort()
        repStr = ''
        for alpha in listStr:
            repStr = repStr + alpha
        if dicWord.has_key(repStr):
            index = dicWord[repStr]
            res[index].append(str)
        else:
            curPosition += 1
            dicWord[repStr] = curPosition
            res.append([str])
    return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strs)