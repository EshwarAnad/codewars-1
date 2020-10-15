def next_id(arr):
    if len(arr)!=0:
        arr.sort()
        for i in range(max(arr)+2):
            if i not in arr:
                return i
    else:
        return 0
