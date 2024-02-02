import math
#1
r = float(input())
p = math.pi * r * r
print("P= " + str(p))

#2
def n_plus_n(n):
    nn=n
    nnn=n
    print(n+nn+nnn)

n_plus_n(2)

#3
def amout_of_list():
    a=[1,2,3,4,5,6,7,8,9]
    print(sum(a))

amout_of_list()

#4
def multiplied_list ():
    a = [1,2,3,4,5,6,7,8,9]
    aa = []
    for i in a:
        aa.append(i*2)
        print(aa)


multiplied_list()

#5
def least_number_in_list():
    a = [1,2,3,4,5,6,7,8,9]
    print(min(a))

least_number_in_list()