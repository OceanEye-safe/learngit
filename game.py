import random

print('-----------fish_c----------')
secret = random.randint(1,10)
temp = input('guess which number is he thought:')
guess = int(temp)

while guess != secret:
    temp=input('oops ,wrong number,please try again')
    guess=int(temp)
    if guess == secret:
        print('bingo!')
    else:
        if guess > secret:
            print('too big')
        else:
            print('too small')

print('GAME OVER')
print('now update to V2 version')