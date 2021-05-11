TGname = input('Enter the name of the tutor group: ') #Tutor group name
TGstdNum = 0 #Tutor Group Amount of students
TGcddNum=0 #Tutor group amount of candidates
TGcdd = []  #array of candidates
TGvotes = [0, 0, 0, 0] #counts of vote per candidate
vtrNo = []  #voter Number (like student number)
abstained = 0 
winners = [] #array for the winners
voteNo = 0

def getTGstdNum(): 
    #function for amount of students
    global TGstdNum
    TGstdNum = input('Enter the number of students in the tutor group:')
    while not TGstdNum.isnumeric():
        TGstdNum = input("Please only enter numbers. Enter the number of students in the tutor group: ")
    return int(TGstdNum)

def getTGcddNum():      
    #function for amount of candidates
    global TGcddNum
    TGcddNum = input('Enter the number of candidates (max 4):')
    while not TGcddNum.isnumeric():
        TGcddNum = input('Please only enter numbers. Enter the number of candidates (max 4):')
    return int(TGcddNum)

def voting(): 
    #getting input of votes per voter number
    global abstained
    global TGstdNum
    global TGcddNum
    global TGcdd
    global voteNo
    
    print('0. Abstain') #prints 0. abstain
    for j in range(0, int(TGcddNum)): #index starts at 0
        print(str(j+1)+'. '+str(TGcdd[j])) #index + 1, candidate name presented looks like 1. example_name
    vote = input('Enter your choice: ')
    while not vote.isnumeric():
        vote = input('Please only enter numbers. Enter your choice: ')

    while int(vote) > int(TGcddNum):
             vote = input('Please only enter numbers. Enter your choice between 0 and ' + str(len(TGcddNum) + 1) + ': ')
             while not vote.isnumeric():
                vote = input('Please only enter numbers. Enter your choice: ')
    
    if int(vote) == 0 : 
        #checks for abstained votes
        abstained+=1
    else:
        TGvotes[int(vote)-1] += 1 #inputs the vote into the vote array
        voteNo += 1

def getVtrNo(): #function for getting votes while checking voter number
    global vtrNo
    response = input('Enter your voter number: ') #checks vtrNO
    while not response.isnumeric():
        response = input('It can only be a whole number, please enter again: ')
    while response in vtrNo:
        #if vtrNo is already given once, it won't accept
        print('You have already voted')
        response = input('Enter your voter number: ')
    vtrNo.append(response) #adds voter number to the array of voter numbers
    voting() 
    return

#while not(28<=getTGstdNum()<=35): 
while not(getTGstdNum()<=35): #for now      
    #checks if amount of students is between 28 and 35
    print('Please try again. Minimum number of students is 28 and maximum is 35')

while not(1<=getTGcddNum()<=4):        
    #checks if the amount of candidates is in the required slot
    print('Please try again')

for i in range(0, int(TGcddNum)):
    #save candidate names
    TGcdd.append(input('Enter the name of candidate '+str(i+1)+': '))

for i in range(0,int(TGstdNum)):
    #get votes while checking voter number
    getVtrNo()

def printResults():
    global winners
    print('\n\n----------- The Voting Results for '+TGname+' -----------') #Results for that tutor group
    print('\nNumber of votes cast: ',voteNo)
    print('Abstained votes: '+str(abstained)+'\n\n\n') #print amount of students abstained

    for i in range(0, int(TGcddNum)): #show results for each candidate from the amount of candidates
        print(str(i+1)+'. '+str(TGcdd[i])+': '+str(TGvotes[i])+' votes, ', str(round((TGvotes[i]/voteNo * 100)*100)/100) + '% of votes casted.\n') #index at 0, voter was given at 1 ad onwards; gets candidate name; gets candidate votes

    mx = max(TGvotes) #searches for winner by the maximum value in the votes

    for i in range(0, int(TGcddNum)): #getting index of the winners
        if TGvotes[i] == mx: #if candidate belongs to the winners, add it 
            winners.append(TGcdd[i])


    print('The winner(s) is/are '+str(', '.join(winners))) #print winners
printResults()

while len(winners)>1:

    TGcddNum = int(len(winners))
    TGcdd = winners
    vtrNo = []
    TGvotes = [0, 0, 0, 0]
    abstained = 0 
    voteNo = 0
    winners = []
    print('\nThere is a tie, casting another vote...\n')
    for i in range(0,int(TGstdNum)):
        #get votes while checking voter number
        getVtrNo()
    printResults()