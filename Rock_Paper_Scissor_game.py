import random
# Rock paper scissor game
def gamewin(comp,you):
    if comp == you:
       return None
    elif comp == 'R':
        if you == 'S':
           return False
        elif you == 'P':   
           return True
    elif comp == 'P':
        if you == 'R':
            return False
        elif you == 'S':
            return True
    elif comp == 'S':
        if you == 'P':
            return False
        elif you == 'R':
            return True

print("comp turn: Rock (R) ,Paper (P) ,Scissor (S) ?")


randNum = random.randint(1,3)
if randNum ==1:
   comp ='R'
elif randNum ==2:
   comp = 'P'
elif randNum ==3:
   comp ='S'

you = input("your turn: Rock (R) ,Paper (P) ,Scissor (S) ? ")


print(f"comp choice {comp}")
print(f"your choice {you}")

a = gamewin(comp,you)



if a == None:
   print("The game is tie")
elif a:
    print("you win! ")
else:
    print("You lose! ") 