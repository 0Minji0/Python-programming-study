### 학번: 20230394             이름: 김민지


#print('안녕')


# for i in range(1,11): 
#     print(i, end='+')
    
 

### 예시1 ###
### coding here ###

# for i in range(5):
#     print('*' * 10)

### 예시2 ###
# for i in range(1, 6) :
#     print('*' * i)

### 예시3 ###

# for i in range(6) :
#     print('*' * (5-i))

### 예시4 ###
# for i in range(1,31):
#     if i % 3 ==0 :
#         print(i)

### 예시
# res = 0
# for i in range(1,11):
#     res += i
    
# print(res)


### 예시5 ###
# num = int(input('2 이상의 숫자를 입력해 주세요 : '))
# ### coding here ###

# res = 1
# for i in range (1, num+1):
#     res *= i

# print(res)    

### 예시 

# res1 = 0
# res2 = 1
# for i in range(1,101):
#     if i % 2 == 1:
#         res1 += i
#     else:
#         res2 *= i

# print(res1,res2)



### 예시6 ###

# i = 0
# dan = 0

# dan = int(input('구구단 몇 단을 계산할까요? : '))

# for i in range (1,10)  :
#     print('%d x %d = %d'%(dan,i,dan*i))

### 중첩 for 문

# for i in range(3):
#     for j in range(5):
#         print(i,j)
#     print('hello')


### 예시7 ###

# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))
        
#### while
# res = 0
# i = 1

# while i < 11:
#     res += i
#     i += 2

# print(res)


# for i in range (1,11):
#     res += i

# print(res)


### 예시8 ###
### coding here ###

# for i in range(5):
#     print('*' * 10)

# i = 0
# while i < 5:
#     print('*' * 10)
#     i = i + 1


### break 문
# for i in range(10):
#     print(i)
#     if i >5: break

# res = 0
# for i in range(1,11):
#     res += i
#     if res> 40: break   ### 8까지 더하면 40인데 9를 더하고 45 넘어? 응 (그리고 나서  나오는 거임)

# print(res)


###continue 문
# for i  in range(1,31):
#     if i % 3 != 0:
#         continue
#     print(i)

# for i in range(1,31):
#     if i % 2 ==1:
#         continue
#     print(i)

# i = 1
# while i < 31:
#     if i % 2 !=0:
#         i += 1
#         continue
#     print(i)
#     i += 1
        


### 예시9 ###
### coding here ###

# res = 0

# for i in range (1,101):
#     res += i
# print(res)


### 예시10 ###
### coding here ###

gcm =1

# for i in range(1,31):
#     if 30 % i == 0 and 75 % i == 0:
#         gcm = i

i = 1
while i < 31:
    if 30 % i == 0 and 75 % i == 0:
        gcm = i
    i += 1     

print(gcm)