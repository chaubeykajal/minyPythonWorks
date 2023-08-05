from lib2to3.pygram import Symbols
import random
import string
letters= string.ascii_letters
nums="0123456789"
specials="+-*&%$#@!"
Symbols= letters+specials+nums
len= int(input("enetr the pass. length: "))
password=''.join(random.sample(Symbols,len))

print(password)

