'''
CHALLENGE: LOOP THE LOOP
# ./images_breadboard/01_breadboard.png

1. Can you change the loop back into a definite loop again? 
2. Can you add a second definite loop to the program? 
3. How would you add a loop within a loop, and how would you expect that to work?
'''

# 1
import utime

num = 0

print("Loop one starting!")
while num < 5:
    print("Loop one running!")
    utime.sleep(1)
    num += 1
print("Loop one finished!")

# 2
print("Loop two starting!")
while num > 0:
    print("Loop two running, reverse!")
    utime.sleep(1)
    num -= 1
print("Loop two finished!")

# 3
for i in range(1, 3):
    print(f"Table of {i}")
    while num < 5:
        print(f"{i} * {num} = {i*num}")
        num += 1
    num = 0
