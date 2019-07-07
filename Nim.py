import random

def newmove(pos0,pos1,pos2):
    if pos0==0 and pos1!=0 and pos2!=0:
            new=random.choice([1,2])#Random move between 1 and 2 since 0 is empty
    elif pos0!=0 and pos1!=0 and pos2==0:
            new=random.choice([0,1])#Random move between 0 and 1 since 2 is empty
    elif pos0==0 and pos1==0 and pos2!=0:
            new=2#Next move is restricted to 2
    elif pos0!=0 and pos1==0 and pos2==0:
            new=0#Next move is restricted to 0
    elif pos0==0 and pos1!=0 and pos2==0:
            new=1#Next move is restricted to 1
    elif pos0!=0 and pos1==0 and pos2!=0:
            new=random.choice([0,2])#Random move is restricted to 0 and 2 since 1 is empty
    else:
            new=random.choice([0,1,2])

    return new

#Picks a random integer between 1 and the number of sticks left in pile
def pickInt(p0,p1,p2,n):
    if n==0:
        return random.randint(1,int(p0))
    elif n==1:
        return random.randint(1,int(p1))
    else :#n==2:
        return random.randint(1,int(p2))
    
#Returns if a current board state is a terminal state  
def Terminal(s):
    a=[]
    tot=0
    a.append(int(s[1]))
    a.append(int(s[2]))
    a.append(int(s[3]))

    for x in range(0,3):
        tot+= a[x]
    #print("Total: ",tot)
    if tot==0:
    
        return True
    else:
        return False

def qL(n,sboard,q):
    print(n)
    for x in range(0,n):
        board=sboard
        while Terminal(board)==False:
            #Updating array[4]
            p=board[0]
            pos0=int(board[1])
            pos1=int(board[2])
            pos2=int(board[3])
            pilePicked=newmove(pos0,pos1,pos2)
            nexB=list(board)
            nexB[4]=(str(pilePicked))
            board=''.join(nexB)
            
            
            #Updating array[5]
            nexB=list(board)
            p=board[0]
            pos0=int(board[1])
            pos1=int(board[2])
            pos2=int(board[3])
            pile=int(board[4])
            stickpick=pickInt(pos0,pos1,pos2,pile)
            nexB[5]=(str(stickpick))
            board=''.join(nexB)
            
            #Updating the board with random picks made by Comp
            nexB=board
            p=board[0]
            pos0=int(board[1])
            pos1=int(board[2])
            pos2=int(board[3])
            pile=int(board[4])
            take=int(board[5])
            
            if pile==0:
                pos0=pos0-take
            elif pile==1:
                pos1=pos1-take
            else:
                pos2=pos2-take
            
            if p=="A":
                p="B"
            else:
                p="A"
            nexB=p+str(pos0)+str(pos1)+str(pos2)
            
            #Terminal state rewards
            if nexB=="A000":
                reward=1000
            elif nexB=="B000":
                reward=-1000
            else:
                reward=0
            #For A values    
            if board[0]=="A":
                if board not in q:
                    q[board]=0
                    #print("added:",board)
                if Terminal(board)==False:
                    minimum=1000
                else:
                    minimum=1000
                minimum
                #All possible states with first pile>0 
                if pos0>0:
                    i=0
                    for i in range(0,pos0):
                        nexB=p+str(pos0)+str(pos1)+str(pos2)+"0"+str(pos0-i)
                        i+=1
                        if nexB in q:
                            if minimum>q[nexB]:
                                minimum=q[nexB]
                #All possible states with second pile>0                
                if pos1>0:
                    i=0
                    for i in range(0,pos1):
                        nexB=p+str(pos0)+str(pos1)+str(pos2)+"1"+str((pos1-i))
                        i+=1
                        if nexB in q:
                            if minimum>q[nexB]:
                                minimum=q[nexB]
                #All possible states with third pile>0                
                if pos2>0:
                    i=0
                    for i in range(0,pos2):
                        nexB=p+str(pos0)+str(pos1)+str(pos2)+"2"+str((pos2-i))
                        i+=1
                        if nexB in q:
                            if minimum>q[nexB]:
                                minimum=q[nexB]
                    
                q[board]=q[board]+(reward+(.9*(minimum)-q[board]))
                #print (reward, minimum,q)
                #Updating q[board] and board
                board=nexB
            #For B values:
            else:
                #print("Board: ",board)
                if board not in q:
                    q[board]=0
                    #print("added:",board)
                if Terminal(board)==False:
                    maximum=-1000
                else:
                    maximum=-1000
                
                if pos0>0:
                    i=0
                    for i in range(0,pos0):
                        nexB=p+str(pos0)+str(pos1)+str(pos2)+"0"+str(pos0-i)
                        i+=1
                        
                        if nexB in q:
                            if maximum<q[nexB]:
                                maximum=q[nexB]
                                
                #All possible states with second pile>0
                if pos1>0:
                    i=0
                    for i in range(0,pos1):
                        nexB=p+str(pos0)+str(pos1)+str(pos2)+"1"+str(pos1-i)
                        i+=1
                        
                        if nexB in q:
                            if maximum<q[nexB]:
                                maximum=q[nexB]
                #All possible states with third pile>0
                if pos2>0:
                    i=0
                    for i in range(0,pos2):
                        nexB=p+str(pos0)+str(pos1)+str(pos2)+"2"+str(pos2-i)
                        i+=1
                        
                        if nexB in q:
                            if maximum<q[nexB]:
                                maximum=q[nexB]
            
                q[board]=q[board]+(reward+(.9*(maximum)-q[board]))
                #print(reward, maximum,q)
                #print("Board: ",board)
                board=nexB            
            
    for item in q:
        #print("a")
        print(item+" "+str(q[item]))
        
def gameplay(board,q):
    yN="y"
    temp=board
    while yN=="y":
        playerF=int(input("Who moves first, (1) User or (2) Computer? "))
        board=temp#Resetting board every game
        if playerF==1:#To keep track of User/Computer and A/B
            curmove=1
        else:
            curmove=2
            
        while Terminal(board)==False:
            if board not in q:
                    q[board]=0
            
            if playerF==1 and curmove==1 or playerF==1 and curmove==2:
                #User playing case
                if playerF==1 and curmove==1:
                    ab="A"
                else:
                    ab="B"
                pos0=board[1]
                pos1=board[2]
                pos2=board[3]
                print("Player ",ab," (User's) turn. The board is ["+pos0+","+pos1+","+pos2+"]")
                pilenum=int(input("Pick a pile: 0,1 or 2 "))
                stickpick=int(input("How many sticks do you wish to remove from that pile? "))
                #Subtracting sticks picked from sticks available
                if pilenum==0:
                    pos0=int(pos0)-stickpick
                    pos0=str(pos0)
                elif pilenum==1:
                    pos1=int(pos1)-stickpick
                    pos1=str(pos1)
                else:
                    pos2=int(pos2)-stickpick
                    pos2=str(pos2)
                board=ab+pos0+pos1+pos2
                curmove=2
                playerF=2
                #Update AB
            elif playerF==2 and curmove==2:
                #Computer trying to maximise
                pos0=board[1]
                pos1=board[2]
                pos2=board[3]
                print("Player "+board[0]+" (Computer's) turn. The board is ["+pos0+","+pos1+","+pos2+"]")
                maxval=-10000
                pos0=int(pos0)
                pos1=int(pos1)
                pos2=int(pos2)
                
                
                if pos0>0:
                    i=0
                    for i in range(0,pos0):
                        nexB=board[0]+str(pos0)+str(pos1)+str(pos2)+"0"+str(pos0-i)
                        i+=1
                        if q[nexB]>maxval:
                            maxval=q[nexB]
                            smartboard=nexB
                if pos1>0:
                    i=0
                    for i in range(0,pos1):
                        nexB=board[0]+str(pos0)+str(pos1)+str(pos2)+"1"+str(pos1-i)
                        i+=1
                        if q[nexB]>maxval:
                            maxval=q[nexB]
                            
                            smartboard=nexB
                
                if pos2>0:
                    i=0
                    for i in range(0,pos2):
                        nexB=board[0]+str(pos0)+str(pos1)+str(pos2)+"2"+str(pos2-i)
                        i+=1
                        print(q[nexB])
                        if q[nexB]>maxval:
                            maxval=q[nexB]
                            smartboard=nexB
                cpick1=smartboard[4]
                cpick2=smartboard[5]
                print("Computer chooses pile "+cpick1+" and removes "+cpick2+ "sticks")
                if int(cpick1)==0:
                    pos0=pos0-int(cpick2)
                elif int(cpick1)==1:
                    pos1=pos1-int(cpick2)
                else:
                    pos2=pos2-int(cpick2)
                nexB="B"+str(pos0)+str(pos1)+str(pos2)
                playerF=1
                board=nexB
            elif playerF==2 and curmove==1:
                #Computer playing to minimize
                pos0=board[1]
                pos1=board[2]
                pos2=board[3]
                print("Player"+board[0]+"(Computer's) turn. The board is ["+pos0+","+pos1+","+pos2+"]")
                minval=10000
                pos0=int(pos0)
                pos1=int(pos1)
                pos2=int(pos2)
                
                if pos0>0:
                    i=0
                    for i in range(0,pos0):
                        nexB=board[0]+str(pos0)+str(pos1)+str(pos2)+"0"+str(pos0-i)
                        i+=1
                        if q[nexB]<minval:
                            minval=q[nexB]
                            smartboard=nexB
                            
                if pos1>0:
                    i=0
                    for i in range(0,pos1):
                        nexB=board[0]+str(pos0)+str(pos1)+str(pos2)+"1"+str(pos1-i)
                        i+=1
                        if q[nexB]<minval:
                            minval=q[nexB]
                            smartboard=nexB
                            
                if pos2>0:
                    i=0
                    for i in range(0,pos2):
                        nexB=board[0]+str(pos0)+str(pos1)+str(pos2)+"2"+str(pos2-i)
                        i+=1
                        if q[nexB]<maxval:
                            maxval=q[nexB]
                            smartboard=nexB
                
                cpick1=smartboard[4]
                cpick2=smartboard[5]
                print("Computer chooses pile "+cpick1+" and removes "+cpick2+ "sticks")
                if int(cpick1)==0:
                    pos0=pos0-int(cpick2)
                elif int(cpick1)==1:
                    pos1=pos1-int(cpick2)
                else:
                    pos2=pos2-int(cpick2)
                nexB="A"+str(pos0)+str(pos1)+str(pos2)
                board=nexB
                playerF=1
            if Terminal(board)==True:
                if board[0]=="A":
                    print("Winner is A: ",board)
                else:
                    print("Winner is B: ",board)
                    print("Would you like to play again?")
                    yN=input("y for yes and n for no")
    
        
            
        
    
def main():
    
    pile0=int(input("Please enter number of sticks in pile 1: "))
    pile1=int(input("Please enter number of sticks in pile 2: "))
    pile2=int(input("Please enter number of sticks in pile 3: "))

    n=int(input("Number of games to simulate? "))

    print("Initial board is ",pile0,"-",pile1,"-",pile2,", simulating ",n," games.")

    a="A"
    
    initboard=a+str(pile0)+str(pile1)+str(pile2)+"5"+"5"
    q={}
    qL(n,initboard,q)
    gameplay(initboard,q)
    
    
main()
    
