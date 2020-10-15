def find_multiples(integer, limit):
    a=[]
    for i in range(integer,limit+1):
        if i%integer==0:
            a.append(i)
    return a
