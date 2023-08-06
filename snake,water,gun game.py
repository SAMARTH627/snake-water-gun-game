import random

def swg(c,m):
    print("computer choose: ", c)
    if(c==m):
        return None
    if(c=='s' and m =='g'):
        return True
    elif(c=='w' and m == 's'):
        return True
    elif(c=='g' and m =='w'):
        return True
    else:
        return False
    
choice = ('s', 'w', 'g')
'''
s - snake
w - water
g - gun
'''
comp = random.randint(0, 2)
comp = choice[comp] #comp = 0 >>> s , comp = 1 >>> w, comp = 2 >>> g
mine = input('Choose either s, w or g: ')

win = swg(comp,mine)
if win is None:
    print("match is drawn")
if win:
    print("you won")
else:
    print("you loss")