import random
#   Lavels
easy = random.randint(1,50)
normal = random.randint(1,100)
hard = random.randint(1,500)
ultra = random.randint(1,1000)

#    Lavel suggetions

#     if statement numbers

e1 = 10
e2 = 12
e3 = 10
e4 = 8
a = '''
       easy = 1 to 50
       10 guesses 
       
       normal = 1 to 100
       12 gusses

       hard = 1 to 500
       10 gusses

       ultra = 1 to 1000
       8 gusses
       '''
#     Starter fail fix

print(a)
b = input("Enter Your Difficulty :- ")

while True:
    if b == 'easy' or b == 'normal' or b == 'hard' or b == 'ultra':
        break
    else:
        print("invelid difficulty , try again ")
        b = input("Enter Your Difficulty :- ")
        continue      

left = "Chances Left = "

#     if statements big small

big = "Too Big \ "
small = "Too Small \ "

#     if statemants

guess = int(input("Take a number :- "))

#     Easy Lavel

while b == "easy":
    e1 = e1 - 1
    br = (big) + left + str(e1)
    sr = (small) + left + str(e1)
    if guess == easy:
        print("You Gussed Right , You Won The Game!!")
        break
    if e1 == 0:
        print("Your all chanses is Finished , Game Over")
        print("ans = " + str(easy))
        break
    if guess > easy:
        print(br)
        guess = int(input("Take a number :- "))
    elif guess < easy:
        print(sr)
        guess = int(input("Take a number :- "))

#     Normal Lavel

while b == "normal":
    e2 = e2 - 1
    br = (big) + left + str(e2)
    sr = (small) + left + str(e2)
    if guess == normal:
        print("You Gussed Right , You Won The Game!!")
        break
    if e2 == 0:
        print("Your all chanses is Finished , Game Over")
        print("ans = " + str(normal))
        break
    if guess > normal:
        print(br)
        guess = int(input("Take a number :- "))
    elif guess < normal:
        print(sr)
        guess = int(input("Take a number :- "))

#     Hard lavel

while b == "hard":
    e3 = e3 - 1
    br = (big) + left + str(e3)
    sr = (small) + left + str(e3)
    if guess == hard:
        print("You Gussed Right , You Won The Game!!")
        break
    if e3 == 0:
        print("Your all chanses is Finished , Game Over")
        print("ans = " + str(hard))
        break
    if guess > hard:
        print(br)
        guess = int(input("Take a number :- "))
    elif guess < hard:
        print(sr)
        guess = int(input("Take a number :- "))

#       Ultra Lavel

while b == "ultra":
    e4 = e4 - 1
    br = (big) + left + str(e4)
    sr = (small) + left + str(e4)
    if guess == ultra:
        print("You Gussed Right , You Won The Game!!")
        break
    if e4 == 0:
        print("Your all chanses is Finished , Game Over")
        print("ans = " + str(ultra))
        break
    if guess > ultra:
        print(br)
        guess = int(input("Take a number :- "))
    elif guess < ultra:
        print(sr)
        guess = int(input("Take a number :- "))
