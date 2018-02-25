def function():
    l1 =[1,3,4,5,6,6,78,9,90,0,0,0,0]
    l2 = [3,3,4]
    l = l1+l2
    dic = dict.fromkeys(l)
    return list(dic.keys())


def function2():
    lis1 = [2,10,100,51,93,80,0,1,7]
    x = 100
    y = 80
    sum1 = 0
    flag = 1
    for i in lis1:
        if x == i:
          flag = 0
        elif y == i:
            flag = 1
        if flag == 1:
            sum1 += i
    return sum1


def prime_num():
    prime_lis = []
    for prime in range(100):
        for i in range(2,prime):
            if prime % i == 0:
                break
        else:
            prime_lis.append(prime)
    return prime_lis


def sorting_func():
    l = [1,57,90,7,9,3,89,58,100,101,99,102]
    return sorted(l,reverse=True)[2]



from collections import Counter
def func():
    l =[3,4,5,6,6,9,9,0,0,0,0,3,4,5,1]
    for keys,value in Counter(l).items():

            if keys == 1:
                print (value)
                x =  int(value)
    return x
