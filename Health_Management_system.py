def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("Enter 1 for Exercise and 2 for Food-diet\n"))
        if(c==1):
            value = input("type here\n")
            with open('pranali_exe.txt',"a") as op:
                op.write(str([(getdate())]) + ' : '+ value+'\n') 
            print("Succefulley written")
            

        elif(c==2):
            value = input("type here\n")
            with open("pranali_food.txt","a") as op:
                op.write(str([str(getdate())]) + ": "+ value + "\n")
            print("successfully written")
    elif k == 2:
        c = int(input("Enter 1 for Exercise and 2 for Food-diet\n"))
        if(c==1):
            value = input("type here\n")
            with open('Anurag_exe.txt',"a") as op:
                op.write(str([str(getdate())]) + ' : '+ value+'\n') 
            print("Succefulley written")

        elif(c==2):
            value = input("type here\n")
            with open("Anurag_food.txt","a") as op:
                op.write(str([str(getdate())]) + ": "+ value + "\n")
            print("successfully written")
    elif k == 3:
        c = int(input("Enter 1 for Exercise and 2 for Food-diet\n"))
        if(c==1):
            value = input("type here\n")
            with open('pradip_exe.txt',"a") as op:
                op.write(str([str(getdate())]) + ' : '+ value+'\n') 
            print("Succefulley written")

        elif(c==2):
            value = input("type here\n")
            with open("pradip_food.txt","a") as op:
                op.write(str([str(getdate())]) + ": "+ value + "\n")
            print("successfully written")
    else: 
        print("please enter valid input 1(Pranali), 2(Anurag) , 3(Hammad)")

def retrive(k):
    if k==1:
        c = int(input("Enter 1 for Exercise and 2 for Food-diet\n"))
        if c==1:
            with open("pranali_exe.txt") as op:
                for i in op:
                    print(i,end='')
        elif c==2:
            with open("pranali_food.txt") as op:
                for i in op:
                    print(i,end='')
                
    
    elif k==2:
        c = int(input("Enter 1 for Exercise and 2 for Food-diet\n"))
        if c==1:
            with open("Anurag_exe.txt") as op:
                for i in op:
                    print(i,end='')
        elif c==2:
            with open("Anurag_food.txt") as op:
                for i in op:
                    print(i,end='')
    elif k==3:
        c = int(input("Enter 1 for Exercise and 2 for Food-diet\n"))
        if c==1:
            with open("pradip_exe.txt") as op:
                for i in op:
                    print(i,end='')
        elif c==2:
            with open("pradip_food.txt") as op:
                for i in op:
                    print(i,end='')

    else:
        print("please enter valid input: Pranali , Anurag , pradip") 

print("HEALTH MANAGEMENT SYSYTEM")   
a = int(input("Press 1 for log and 2 for retrive : "))

if a == 1:
    b = int(input("1 for pranali, 2 for Anurag, 3 for Pradip: "))
    take(b)
else:
    b = int(input("1 for pranali, 2 for Anurag, 3 for Pradip: "))
    retrive(b)



        


