import time
import emoji
class player:
    def __init__(self,cb,deltamt):
        self.cb = cb
        self.deltamt = deltamt
    def get_cb(self):
        return self.cb
    def modcb(self):
        self.cb += self.deltamt
from random import *
stbal = int(input('Enter your starting balance: '))
curb = stbal
print('\n\nWelcome to the Slot Machine Game!')
print('Your start with a balance of',stbal)

p1 = player(curb,0)
ch = 'y'
lst = [':dog_face:',':bell:',':cat_face:',':pizza:',':bomb:']
def decfate(obj,lst,amt):
    #p1 = player(curb,0)
    if lst[0] == lst[1] == lst[2]:
        print('You won Rs.',10 * amt,'!!')
        obj = player(obj.get_cb(),10*amt)
        obj.modcb()
    elif lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]:
        print('You won Rs.', 2 * amt,'!!')
        obj = player(obj.get_cb(),2*amt)
        obj.modcb()
    else:
        print('You lose your bet amount')
        obj = player(obj.get_cb(),-amt)
        obj.modcb()
    return obj
while ch=='y' and p1.get_cb()>0:
    print('\nCurrent balance:', p1.get_cb())
    betamt = int(input('Enter your bet amount: '))
    while betamt > p1.get_cb():
        betamt = int(input('Please enter a bet within your balance:'))
    reel = choices(lst, k=3)
    print('|',end=' ')
    for r in reel:
        time.sleep(1)
        print(emoji.emojize(r),end=' | ')
    print()
    time.sleep(1)
    p1 = decfate(p1,reel,betamt)
    if p1.get_cb()==0:
        print('Oops! You have exhausted your balance :(')
        break
    ch = input('\nDo you want to play again? (y/n): ')




