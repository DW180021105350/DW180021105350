Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = eval(input())
6
>>> b = a // 2 + 1
>>> c=1
>>> for i in range (b):
      print((" " * ((a-c)//2)) + ("*" * c) +(" " * ((a-c)//2)))
      c+= 2
