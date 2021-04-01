sentence = '다들 파이썬은 어떠신가요 파이썬은 나중에 다른 곳에서도 많이 쓰인답니다 파이썬은 다른 언어보다 코딩 하기 쉬워요 멋사 멋사 화이팅'
dic = {}
sentences = sentence.split()
for word in sentences:
    if(word in dic): #이미 있음
        su = dic[word]
        dic[word] = su+1
    else: #없으면 딕셔너리 삽입
        dic[word] = 1
    
for word in dic:
    print('\''+word+'\'','=',dic[word])