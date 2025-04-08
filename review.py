# print('hello')
# print('데이터사이언스')

# print('100')
# print('%d'%100)

# print('100+100')
# print('%d'%(100+100))

# print('%d / %d = %d'%(200,100,200/100))

# print('%d'%110.1234)
# print('%f'%10.123456)
# print('%s'%'데이터')

# x = 1
# y = 2.3
# z = 'minji'

# print('%d %f %s' %(x,y,z))
# print(x,y,z)

# print('안녕하세요\n')
# print('안녕하세요\t 저는....')
# print('\\\'출력\\')

# price = 100
# print(price, '원')
# print(price, '원',sep='')

# year = 2024
# month = 3
# day = 30
# print(year, month, day, sep='/')

# var1 = 100
# var2 = 3.14
# var3 = '파이썬'
# var4 = True

# print(int(var1))
# print(float(var2))
# print(str(var3))
# print(bool(var4))

# x = 10
# y = 5.5
# z = x+y

# print(z)
# print(float(z))

# a = '동덕여대 데이터사이언스'
# print(a)
# print(str(a))

# b = '동덕' + '데이터'+ '사이언스'
# print(b)

# x = (100 > 10)
# print(x)

# math = 100
# science = 90
# print((math+science)/2)

# age = int(input('너 몇살?'))
# print(age+10)

# print('## 택배를 보내기 위한 정보를 입력하세요. ##')
# name = input('받는 사람:')
# address = input('주소: ')
# weight = int(input('무게(g): '))

# print('받는사람 ==> %s'%name)
# print('주소 ==> %s'%address)
# print('배송비 ==> ',weight*5,'원')


# num1 = int(input('숫자1:'))
# num2 = int(input('숫자2:'))
# print(num1*num2)



#### 2장
# print('hello',end=' ')
# print('I\'m tony')

# print(1,3,5,7,sep='+',end='=')
# print(1+3+5+7)

# math = 92
# science = 87
# english = 94

# print('수학,과학,영어 점수는 각각 %d점,%d점,%d점입니다'%(math,science,english))
# print('%s score: %d'%('math',math))
# print('%s score: %d'%('science',science))
# print('%s score: %d'%('english',english))


# math = int(input())
# python = int(input())
# mean_score = (math+python)/2

# print('수학 점수는 %s, 파이썬 점수는 %s 입니다.'%(math, python))
# print('그리고 평균 점수는 %f점 입니다.'%mean_score)

# n1 = 5
# n2 = 3

# sum = n1 + n2
# mul = n1 * n2
# div = n1 / n2
# quo = n1 // n2
# rem = n1 % n2
# square = n1 ** n2

# print('두 수의 합은 %d이지~'%sum)
# print('n1을 n2로 나눈 몫은 %d, 나머지는 %d이지~'%(quo,rem))
# print('n1의 n2승은 %d이지~'%(square))

# a =2
# b =4
# c =6
# print(-a+b+c)
# print(2*b-c+a)
# print(a/b*c)



# x = '100'
# y = '100.123'
# z = '99.4'

# print(int(x), float(y)+1)

# a = 100
# b = 100.1

# print(str(a)+'1')
# print(str(b)+'2')

# pi = 3.14159265
# r = int(input())

# length = 2*r*pi
# area = pi*(r**2)

# print('원의 둘레는 %f, 넓이는 %f 입니다.'%(length,area))

# k = '어려워요'
# k += '!'
# print(k)

# a = 10
# print('a =',a)
# a *= 3 + 2

# print('a=',a)



### 3장
##예시1
# password = 'data'
# answer = input('비밀번호를 입력해주세요.:')

# if(password == answer):
#     print('correct')


##예시2
# num = int(input('숫자 하나 입력해주세요: '))

# if(num % 2 ==0):
#     print('짝수')


##예시3
# math = 83
# science = 90

# if(math >= 80 and science >=80): 
#     print('합격')

##예시4
# math = 83
# science = 90
# if(math < 85 or science < 85):
#     print('탈락')


##예시5
# num = int(input('숫자입력: '))

# if(num % 5 ==0 and num % 7 ==0):
#     print('35의 배수')


##예시6
# math = 83
# science = 90

# if(math > science):
#     print(math)
# else:
#     print(science)


##예시7
# num = int(input('숫자 입력: '))

# if(num % 2 ==0 and num>10):
#     print('x')
# else:
#     print('o')

##예시8
# year = int(input('연도를 입력하세요: '))

# if(year % 4 ==0 and year %100 !=0 or year % 400 == 0):
#     print('%d년은 윤년입니다.'%year)
# else: 
#     print('%d년은 윤년이 아닙니다.'%year)

##중첩 if
# x = int(input('숫자를 입력 ==> '))
# if x > 100:
#     if x < 1000:
#         print('100보다 크고 1000보다 작군요')
#     else:
#         print('1000보다 크군요')
# else:
#     print('100보다 작군요')


##예시9
# price = int(input('주문금액: '))

# if price < 10000:
#     print('배달 불가 출력')
# elif price < 30000:
#     print(price * 0.1)
# elif price < 50000:
#     print(price * 0.05)
# else:
#     print('배달비 무료 출력')



##예시10
# user_number = int(input('1부터 100 사이의 숫자를 입력하세요.: '))
# answer = 42

# if user_number < answer:
#     print('더 큰 숫자를 입력하세요!')
# elif user_number > answer:
#     print('더 작은 숫자를 입력하세요!')
# else:
#     print('정답입니다! 축하합니다!')





### 4장
# for i in range(3):
#     print('안녕~~~\n')

# for i in range(0,11,1):
#     print(i,end='')


###예시1
# for i in range(5):
#     print('**********')

##예시2
# for i in range(1,6,1):
#     print('*'*i)

##예시3
# for i in range(6):
#     print('*'*(5-i))


##예시4
# for i in range(1,31):
#     if i % 3 == 0:
#         print(i)

###for 문
# res = 0

# for i in range(1,11,1):
#     res += i

# print('1에서 10까지의 합 =\n',res)

###예시5
# res = 1
# num = int(input('2이상의 숫자를 입력해 주세요 : '))

# for i in range(2,num+1,1):
#     res *= i
# print(res)
    
# res = 0

# for i in range(1000,2001,1):
#     if i % 2 == 1 :
#         res = res + i

# print('1000에서 2000까지의 홀수의 합 = \n', res)

###예시6

# dan = int(input('구구단 몇 단을 계산할까요?: '))

# for i in range (1,10,1):
#     print('%d x %d = %d '%(dan,i,dan*i))

###예시7
# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))

###while문
# res = 0
# for i in range(1,11,1):
#     res = res+ i
# print('1에서 10까지의 합 = \n', res)

# i = 1
# res = 0
# while i < 11:
#     res = res + i
#     i = i + 1

# print('1에서 10까지의 합 = \n', res)

# i = 0

# while i < 5:
#     print('*'*10)
#     i = i + 1






