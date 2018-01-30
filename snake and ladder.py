#snake and ladder program
import random
count = 0
while(count<=100):
    a=input("enter 'r' to roll the dice:")
    if(a=='r'):
        r=random.randint(1,6)
        count=count+r
        print(count)
        print(r)
        if (count==8):
            count=37
            print("climb up the ladder")
        elif (count==13):
            count=34
            print("climb up the ladder")
        elif (count==40):
            count=68
            print("climb up the ladder")
        elif (count==52):
            count=81
            print("climb up the ladder")
        elif (count==76):
            count=97
            print("climb up the ladder")
        elif (count==11):
            count=2
            print("ah! come down, the snake bit")
        elif (count==25):
            count=4
            print("ah! come down, the snake bit")
        elif (count==38):
            count=9
            print("ah! come down, the snake bit")
        elif (count==65):
            count=46
            print("ah! come down, the snake bit")
        elif (count==89):
            count=70
            print("ah! come down, the snake bit")
        elif (count==93):
            count=64
            print("ah! come down, the snake bit")        
        elif (count==100):
            print("the player won")
            break
        
while(count>100):
    print("invalid! roll the dice again")
    break
