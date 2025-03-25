#https://inf-ege.sdamgia.ru/problem?id=59805
for n in  range(3,10000+1):
     s = '5' + '2'*n
     while '52' in s or '1122' in s or '2222' in s:
         s = s.replace('52', '1' ,1)
         s = s.replace('2222','5', 1)
         s = s.replace('1122','25',1)
     sm = sum(map(int, s))
     if sm ==88:
         print (n)
