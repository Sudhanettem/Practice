num = [1,2,3]

def add(a):
    return a+2

result = lambda a : a*2

print(result(8))


#map() , filter(), reduce()
# def test(a):
#     return a*2

rslt = map(lambda a:a*2 , num)
for item in rslt :
    print(item)


#filter() filter the list or any objects based on the lambda expression

lst = [1,2,3,4,5,6,7]

rslt2 = filter(lambda a : a%2 == 0 , lst)

for itm in rslt2 :
    print(itm)


#reduce is used to work with the list 
from functools import reduce
lst_tup = [("breakfast" , 20),
           ("lunch",50),
           ("dinner" ,30)]

total = reduce(lambda a,b : a+b ,lst_tup)

print(total)