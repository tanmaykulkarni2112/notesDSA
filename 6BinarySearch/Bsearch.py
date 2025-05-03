arr = [1,2,3,4,6,7,888,999,1000,1010,3221,5555,9809]

def Bsearch(arrName, target):
    N = len(arrName)
    l = 0
    r = N - 1
    while l <= r:
        mid = l + ((r - l) // 2)
        if arrName[mid] == target:
            return True
        elif arrName[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

result = Bsearch(arr, 3221)
print(result)    