aDict = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}
def howMany(aDict):
    collect = []
    for e in aDict.values():
        for i in range(len(e)):
            collect.append(e[i])
            print collect
    return len(collect)
