target_key = 0

import random
result = random.randint(1, 50)

while True:
    target_key = int(input("password: "))
    if target_key == result:
        print("Access Granted")
        break
    else:
        print("try again")
