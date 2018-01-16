Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 18/4
4.5
>>> 18//4
4
>>> 18%4
2
>>> 5*5*5
125
>>> 5**3
125
>>> tuna = 5
>>> tuna
5
>>> bacan = 20
>>> tuna/bacan
0.25
>>> "Zhou WENTAO"
'Zhou WENTAO'
>>> 'Zhou WENTAO'
'Zhou WENTAO'
>>> 'I don't think he is'
SyntaxError: invalid syntax
>>> "I don't think he is"
"I don't think he is"
>>> 'I don\'t think he is'
"I don't think he is"
>>> 'He said: "He is from China"'
'He said: "He is from China"'
>>> print('I am from China')
I am from China
>>> print("I am from China")
I am from China
>>> print('c:\users\name\Wentao')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> print('c:\users\name\Wentao')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> print(r'c:\users\name\Wentao')
c:\users\name\Wentao
>>> print("c:\users\name\Wentao")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> name='Wentao'
>>> name *5
'WentaoWentaoWentaoWentaoWentao'
>>> name
'Wentao'
>>> name * 5
'WentaoWentaoWentaoWentaoWentao'
>>> "Zhou " + name
'Zhou Wentao'
>>> 
>>> 
>>> user = "Zhou Wentao"
>>> user[0]
'Z'
>>> user[-1]
'o'
>>> user[-5]
'e'
>>> user[2:5]
'ou '
>>> user[:5]
'Zhou '
>>> user[2:]
'ou Wentao'
>>> len("afffdadfaf")
10
>>> len(user)
11
>>> len(:)
SyntaxError: invalid syntax
>>> user(:)
SyntaxError: invalid syntax
>>> user[:]
'Zhou Wentao'
>>> 
>>> 
>>> 
>>> players = [20,30,49,58,60,70]
>>> players
[20, 30, 49, 58, 60, 70]
>>> players[5]
70
>>> players[3]
58
>>> players[3] = 40
>>> players
[20, 30, 49, 40, 60, 70]
>>> players + [99,100]
[20, 30, 49, 40, 60, 70, 99, 100]
>>> players
[20, 30, 49, 40, 60, 70]
>>> players[:3]
[20, 30, 49]
>>> players[:3]=[0,0]
>>> players
[0, 0, 40, 60, 70]
>>> players[:3] = []
>>> players
[60, 70]
>>> players.append(200)
>>> players
[60, 70, 200]
>>> players.append(200,300)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    players.append(200,300)
TypeError: append() takes exactly one argument (2 given)
>>> players[:]
[60, 70, 200]
>>> players[:]=[]
>>> players
[]
>>> players = [1,2,3,4,5,6]
>>> players=[]
>>> players
[]
>>> 
