#creating empty list
dict=[]

Candidate1 =0
Candidate2 =0
Candidate3 =0
Candidate4 =0
Candidate5 =0



chance =5 #int(input("Enter number of voters"))     #varies according to cences

while chance>=1:
    Voter_name=input("Enter the name of the voter :- ")
    dict.append(Voter_name)
    print("1-Candidate 1\n2-Candidate 2\n3-Candidate 3\n4-Candidate 4\n5-Candidate 5")
    choice=int(input("Enter your choice:- "))
    if  choice==1:
        Candidate1 = Candidate1+1
    elif choice==2:
        Candidate2 = Candidate2+1
    elif choice==3:
        Candidate3 = Candidate3+1
    elif choice==4:
        Candidate4 = Candidate4+1
    elif choice==5:
        Candidate5 = Candidate5+1
    else:
        print ("Invalid input, please enter 1,2,3,4 or 5.")
        chance+=1
        dict.remove(Voter_name)
    chance-=1
    

if Candidate1>Candidate2 & Candidate3 & Candidate4 & Candidate5:
    print("\n!!!!!Candidate 1 is the winner.!!!!!\n")
elif Candidate2>Candidate1 & Candidate3 & Candidate4 & Candidate5:
    print("!!!!!Candidate 2 is the winner.!!!!!\n")  
elif Candidate3>Candidate2 & Candidate1 & Candidate4 & Candidate5:
    print("!!!!!Candidate 3 is the winner.!!!!!\n")
elif Candidate4>Candidate2 & Candidate3 & Candidate1 & Candidate5:
    print("!!!!!Candidate 4 is the winner.!!!!!\n")
elif Candidate5>Candidate2 & Candidate3 & Candidate4 & Candidate1:
    print("!!!!!Candidate 5 is the winner.!!!!!\n")
elif Candidate1==Candidate2 or Candidate2==Candidate3 or Candidate3==Candidate4 or Candidate4==Candidate5 or Candidate5==Candidate1:
    print("There is a draw in the election\n")

#Results of the elections
print("~~~The voting trends of the elections~~~")
print("Votes for candidate 1 is",Candidate1)
print("Votes for candidate 2 is",Candidate2)
print("Votes for candidate 3 is",Candidate3)
print("Votes for candidate 4 is",Candidate4)
print("Votes for candidate 5 is",Candidate5)

#for viewing the voters
def voters():
    print (dict)
    
voters()

#For seacrching a voters name
'''
def Votername(name):
    if name in dict:
        print("Already voted")
    else:
        print("Remaining to vote")
        
#Votername("Name")
'''
