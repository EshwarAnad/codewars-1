def iq_test(numbers):
    n=numbers.split()
    n_c=[]
    for i in n:
        if int(i)%2==0:
            n_c.append("even")
        else:
            n_c.append("odd")
    if n_c.count("even")>n_c.count("odd"):
        return n_c.index("odd")+1
    else:
        return n_c.index("even")+1
