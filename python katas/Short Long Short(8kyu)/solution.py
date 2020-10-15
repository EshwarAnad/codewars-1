def solution(a, b):
    s=l=""
    if len(a)>len(b):
        l=a
        s=b
    else:
        l=b
        s=a
    return s+l+s
