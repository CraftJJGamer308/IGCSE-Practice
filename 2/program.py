TGname = input('enter the name of the tutor group: ')
TGstdNum = 0

def getTGstdNum():
    global TGstdNum
    TGstdNum =int(input('enter the number of students in the tutor group:'))
    return TGstdNum

# while not(28<=getTGstdNum()<=35): 
while not(getTGstdNum()<=35): #for now
    print('Please try again')

TGcddNum=0

def getTGcddNum():
    global TGcddNum
    TGcddNum = int(input('enter the number of candidates (max 4):'))
    return TGcddNum

while not(1<=getTGcddNum()<=4):
    print('please try again')
print(TGcddNum)
TGcdd = []
TGvotes = [0, 0, 0, 0]

for i in range(0, TGcddNum):
    TGcdd.append(input('enter the name of candidate '+str(i+1)+': '))


vtrNo = []
abstained = 0

def voting():
    global abstained
    global TGstdNum
    global TGcddNum
    global TGcdd
    print('0. obstain')
    for j in range(0, TGcddNum):
        print(str(j+1)+'. '+str(TGcdd[j]))
    vote = int(input('enter your choice: '))
    
    if vote ==0:
        abstained+=1
        return
    TGvotes[vote-1] += 1

def getStdNo():
    global vtrNo
    response = int(input('enter your voter number: '))
    while (response in vtrNo):
        print('you have already voted')
        response = int(input('enter your voter number: '))
    vtrNo.append(response)
    voting()
    return

for i in range(0,TGstdNum):
    getStdNo()

print('\n\nThe Voting Results for '+TGname)

for i in range(0, TGcddNum):
    print(str(i+1)+'. '+str(TGcdd[i])+': '+str(TGvotes[i])+' votes')

mx = max(TGvotes)
winners = []
for i in range(0, TGcddNum):
    if TGvotes[i] == mx:
        winners.append(TGcdd[i])

print('\nabstained votes: '+str(abstained))
print('The winner(s) is/are '+str(', '.join(winners)))