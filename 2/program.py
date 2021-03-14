TGname = input('enter the name of the tutor group: ')
TGstdNum = int(input('enter the number of students in the tutor group:'))
TGcddNum = int(input('enter the number of candidates (max 4):'))
TGcdd = []
TGvotes = [0, 0, 0, 0]

for i in range(0, TGcddNum):
    TGcdd.append(input('enter the name of candidate '+str(i+1)+': '))

for i in range(0, TGstdNum):
    for j in range(0, TGcddNum):
        print(str(j+1)+'. '+str(TGcdd[j]))
    TGvotes[int(input('enter your choice: '))-1] += 1

print('\n\nThe Voting Results for '+TGname)
for i in range(0, TGcddNum):
    print(str(i+1)+'. '+str(TGcdd[i])+': '+str(TGvotes[i])+'votes')

mx = max(TGvotes)
winners = []
for i in range(0, TGcddNum):
    if TGvotes[i] == mx:
        winners.append(TGcdd[i])
print('\nThe winner(s) is/are '+str(', '.join(winners)))
