# 연습문제 - 제어문, 반복문
# 1. shirt

# 2. i=1
# ans=0
# while(i<=100):
#     if i%4==0:
#         ans+=i
#     i+=1
# print(ans)

# 3. i=1
# ans=0
# for i in range(1,101):
#     if(i%5==0):
#         ans+=i
# print(ans)

# 4. py_score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# total =0
# count=0
# for a in py_score:
#     if a>=60:
#         total +=a
#         count +=1
# average = total / count
# print(average)

# 5.for j in range(2,10):
#     for i in range(1,10):
# 	    print(j, "*", i, '=', j*i)

# 6.sentence = '다들 파이썬은 어떠신가요 파이썬은 나중에 다른 곳에서도 많이 쓰인답니다 파이썬은 다른 언어보다 코딩 하기 쉬워요 멋사 멋사 화이팅'
# dic = {}
# sentences = sentence.split()
# for word in sentences:
#     if(word in dic): #이미 있음
#         su = dic[word]
#         dic[word] = su+1
#     else: #없으면 딕셔너리 삽입
#         dic[word] = 1
# for word in dic:
#     print('\''+word+'\'','=',dic[word])
