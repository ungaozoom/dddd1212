money = 2000
card = True
if money>=3000 or card : 
    print ("택시를타고가라")
    print ('응가')
else : 
    print('걸어가라')

pocket = ['paper','money','coin']

if 'money' in pocket : 
    print ("택시타고가")
else :
    print ('처 걸어가 ')
    
treehit= 0
while treehit < 10:
    treehit = treehit+1
    print('나무를 %d번 찍엇습니다' % treehit)
    if treehit ==10:
        print ('나무 넘어갑니다')


prompt ='''
1.add
2.del
3.list
4.quitt

enter number: '''


number = 0
while number !=4:
    print(prompt)
    number =int(input())


coffee = 10
money = 300
while money:
    print('돈을받았으니 커피를 줍니다')
    coffee = coffee-1
    print('남은 커피의 양은 %d 입니다' % coffee)
    if coffee ==0:
        print('커피가 다 떨어졋으니 판매를 중단합니다')
        break
    