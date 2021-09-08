#made by SeenKid

import random
import string
import os
import time

randomletters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@_-.,=)(/&%ç*"+'


os.system("color a")


def gen_pass(length):
    letters = randomletters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

number = input("\n\nHow many passwords do you want ? ")

try: number = int(number)

except:
	print("\n\nPlease put a correct number.")

else:

	file = "pass.txt"

	file = open("pass.txt", "w")


	for i in range(number):
		result = gen_pass(24)
		result2 = gen_pass(6)
		result3 = gen_pass(27)
		file.write(f"\n{result}{result2}{result3}")
	
	file.close()

	print("\n\nPasswords placed on \"pass.txt\"")

	time.sleep(100)

