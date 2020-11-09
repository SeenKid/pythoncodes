#coding:utf-8

import random
import string
import os
import time

randomletters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


os.system("color a")

print('''         # #                   # #        
       # #     # # # # # # #     # #      
     # # # # # # # # # # # # # # # # #    
     # # # # # # # # # # # # # # # # #    
     # # # # # # # # # # # # # # # # #    
   # # # # # # # # # # # # # # # # # # #  
   # # # # # # # # # # # # # # # # # # #  
   # # # # #     # # # # #     # # # # #  
   # # # #         # # #         # # # #  
 # # # # #         # # #         # # # # #
 # # # # # #     # # # # #     # # # # # #
 # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # #
 # # # # #     # # # # # # #     # # # # #
     # # # #                   # # # #    
       # # # #               # # # #
''')


def gen_token(length):
    letters = randomletters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

number = input("\n\nHow many tokens do you want ? ")

try: number = int(number)

except:
	print("\n\nPlease put a correct number.")

else:

	file = "tokens.txt"

	file = open("tokens.txt", "w")


	for i in range(number):
		result = gen_token(24)
		result2 = gen_token(6)
		result3 = gen_token(27)
		file.write(f"\n{result}.{result2}.{result3}")
	
	file.close()

	print("\n\nTokens placed on \"tokens.txt\"")

	time.sleep(100)

