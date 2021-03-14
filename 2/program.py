TGname = input('enter the name of the tutor group: ') #Tutor group name
TGstdNum = 0 #Tutor Group Amount of students

def getTGstdNum(): 
    #function for amount of students
    global TGstdNum
    TGstdNum =int(input('enter the number of students in the tutor group:'))
    return TGstdNum

# while not(28<=getTGstdNum()<=35): 
while not(getTGstdNum()<=35): #for now      
    #checks if amount of students is between 28 and 35
    print('Please try again')

TGcddNum=0 #Tutor group amount of candidates

def getTGcddNum():      
    #function for amount of candidates
    global TGcddNum
    TGcddNum = int(input('enter the number of candidates (max 4):'))
    return TGcddNum

while not(1<=getTGcddNum()<=4):        
    #checks if the amount of candidates is in the required slot
    print('please try again')
     
print(TGcddNum)


TGcdd = []  #array of candidates
TGvotes = [0, 0, 0, 0] #counts of vote per candidate

for i in range(0, TGcddNum):
    #enter candidate names
    TGcdd.append(input('enter the name of candidate '+str(i+1)+': '))


vtrNo = []  #voter Number (like student number)
abstained = 0 

def voting(): 
    #getting input of votes per voter number
    global abstained
    global TGstdNum
    global TGcddNum
    global TGcdd
    
    
    print('0. abstain') #prints 0. abstain
    for j in range(0, TGcddNum): #index starts at 0
        print(str(j+1)+'. '+str(TGcdd[j])) #index + 1, candidate name presented looks like 1. asdfjaslf
    vote = int(input('enter your choice: '))
    
    if vote ==0: 
        #checks for abstained votes
        abstained+=1
    else:
        TGvotes[vote-1] += 1 #inputs the vote into the vote array

def getVtrNo(): #function for getting votes while checking voter number
    global vtrNo
    response = int(input('enter your voter number: ')) #checks vtrNO
    while (response in vtrNo):
        #if vtrNo is already given once, it won't accept
        print('you have already voted')
        response = int(input('enter your voter number: '))
    vtrNo.append(response) #adds voter number to the array of voter numbers
    voting() 
    return

for i in range(0,TGstdNum):
    #get votes while checking voter number
    getVtrNo()

print('\n\nThe Voting Results for '+TGname) #Results for that tutor group

for i in range(0, TGcddNum): #show results for each candidate from the amount of candidates
    print(str(i+1)+'. '+str(TGcdd[i])+': '+str(TGvotes[i])+' votes') #index at 0, voter was given at 1 ad onwards; gets candidate name; gets candidate votes

mx = max(TGvotes) #searches for winner by the maximum value in the votes
winners = [] #array for the winners
for i in range(0, TGcddNum): #getting index of the winners
    if TGvotes[i] == mx: #if candidate belongs to the winners, add it 
        winners.append(TGcdd[i])

print('\nabstained votes: '+str(abstained)) #print amount of students abstained
print('The winner(s) is/are '+str(', '.join(winners))) #print winners
