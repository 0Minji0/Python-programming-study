##1번
#  print('hello, World!!')


##2번
# print('I love python!!')


##3번
# num = float(input())
# print('%.1f' %num)


##4번
# a = int(input())
# b = int(input())
# print(a+b)


##5번
# a = int(input())
# b = int(input())
# print('%d + %d = %d' %(a,b,a+b))
# print('%d - %d = %d' %(a,b,a-b))
# print('%d * %d = %d' %(a,b,a*b))
# print('%d / %d = %f' %(a,b,a/b))


##6번
# print('I am a student\n')
# print('^^ Nice to meet you~\t')


##7번
# name = str(input('당신의 이름은?'))
# age = int(input('당신의 나이는?'))
# height = int(input('당신의 키는?'))
# print('이름은 %s, 나이는 %d살, 키는 %dcm입니다' %(name, age, height))


###8번
# num = int(input())
# print(int(num**0.5))
# print(num**2)
# print(num**3)


##9번  답: 9-1
# a = 5
# b = 2
# c = a//b

# print('c = %d' %c)


##10번 답: 10-1
# x = 'Python'
# y = 3
# z = x*y

# print(z)


##11번 답:11-3
# x = 'Hello'
# y = 10
# z = x + y
# print(z)


##12번 답:12-1
# price = 1500
# print(price, '원', sep='')


##13번 답:13-1
# x = 7
# y = 2
# z = x / y
# print('결과: %d' %z)


##14번 답: 14-4


##15번 답: 15-1
# a = 10
# b = 5
# c = a // b

# print('결과: %d' %c)


##16번
# num = int(input())
# if num == 0:
#     print('0입니다.')
# elif num > 0 :
#     print('양수입니다.')
# else:
#     print('음수입니다.')


##17번
# age = int(input())
# if age >= 18:
#     print('adult')
# else:
#     print('teen')


##18번
# grade = int(input())
# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >=70:
#     print('c')
# elif grade >= 60:
#     print('D')
# else:
#     print('F')


##19번
# time = int(input())
# if time < 12:
#     print('오전')
# elif time >= 12:
#     print('오후')


##20번
a = int(input())
b = int(input())
c = int(input())

if a>b:
    print(a)
elif a>c:
    print(a)
elif a<b:
    print(b)
elif(b>c):
    print(b)
elif b<c:
    print(c)
elif a<c:
    print(c)


##21번
# a = int(input())
# b = int(input())

# if (a+b) %2 == 1:
#     print('홀수입니다.')
# elif (a+b) %2 ==0:
#     print('짝수입니다.')


##22번
# num = int(input())

# if num % 3 ==0 and num %5 ==0:
#     print('FizzBuzz')
# else:
#     print(num)


##23번
# year = int(input())
# if year % 4 ==0 and year % 100 != 0 or year % 400 ==0:
#     print('윤년입니다.')
# else:
#     print('윤년이 아닙니다.')


##24번
# a = int(input())
# b = int(input())

# if (a-b) >= 10 or (b-a) >= 10:
#     print('차이가 10이상입니다.')
# elif ((a-b) < 10 and (a-b) !=0)or ((b-a) < 10 and (b-a) !=0):
#     print('차이가 10미만입니다.')
# elif a == b:
#     print('두 수는 같습니다.')


##25번
# a = int(input())
# b = int(input())
# c = int(input())

# if a % 2 ==0 and b % 2 ==0 and c % 2 ==0 :
#     print('모두 짝수입니다.')
# elif a % 2 ==1 and b % 2 ==1 and c % 2 ==1 :
#     print('모두 홀수입니다.')
# elif a == 0 or b ==0 or c ==0:
#     print('0은 포함될 수 없습니다.')
# elif ((a+b+c) % 2 ==1 or (a+b+c) % 2 ==0):
#     print('홀수와 짝수가 섞여 있습니다.')







