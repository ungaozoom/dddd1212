marks =[90,25,67,45,80]

number =0
for mark in marks:
    number= number+1
    if mark <60 :
        continue
    print("%d번 학생 축하합니다 합격입니다" %number)

 
    add=0
    for i in range(1,11):
        add = add+i
        print

a= [1,2,3,4]
result =[num*3 for num in a]
print (result)

b= [1,2,3,4]
result2 = [num*3 for num in a if num%2 ==0 ]
print(result2)

def add(a , b):
    return a+b

print (add(3, 6))


def say():
    return('hi')

print(say())

def dd(a,b):
    print('%d, %d 의 합은 %d 입니다 .'%(a,b,a+b))

b= dd(3,4)
b
print(b)

 

for i in range(20):
    print (i, end=(''))
    