testList = [1,2,3,2,5,6,7,8]

def if_empty(list):
    if list == []:
        return(0)
    else:
        pass

def mean(list):
    if_empty(list)
    funcListMean = sum(list) / len(list)
    return funcListMean

def median(list):
    if_empty(list)
    funcListMiddlePosition = len(list) // 2
    funcListMedian = list[funcListMiddlePosition]
    return funcListMedian


def mode(list):
    if_empty(list)
    funcHighestCount = 0
    for number in list:
        count = list.count(number)
        if count > funcHighestCount:
            funcHighestCount = count
            funcListMode = number
    return funcListMode

listMean = mean(testList)
listMedian = median(testList)
listMode = mode(testList)

print("List: ", testList)
print("Mode: ", listMode)
print("Median: ", listMedian)
print("Mean: ", listMean)
