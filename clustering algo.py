dataset=[
    [0,0,1,0,0],
    [0,0,1,1,0],
    [1,0,1,0,1],
    [2,1,1,0,1],
    [2,2,0,0,1],
    [2,2,0,1,0],
    [1,2,0,1,1],
    [0,1,1,0,0],
    [0,2,0,0,1],
    [2,1,0,0,1],
    [0,1,0,1,1],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [2,1,1,1,0]
]

mp=dict()

for i in range(len(dataset)):
    row = dataset[i]
    y=row[-1]
    if y not in mp:
        mp[y]=list()
    mp[y].append(row)

for label in mp:
    print(label)
    for row in mp[label]:
        print(row)

test=[2,1,0,1]
probYes =1
countYes=0
totalYes=0

for row in dataset:
    if row[-1]==1:
        countYes+=1
    totalYes+=1


print("Total yes: {}/{}".format(countYes,totalYes))
probYes*=countYes/totalYes

for i in range(len(test)):
    countYes=0
    totalYes=0
    for row in mp[1]:
        if test[i]==row[i]:
            countYes+=1
        totalYes+=1
    print("for feature {}: {}/{}".format(i+1,countYes,totalYes))
    probYes*=countYes/totalYes

probNo=1
countNo=0
totalNo=0


for row in dataset:
    if row[-1]==0:
        countNo+=1
    totalNo+=1

print("Total no: {}/{}".format(countNo,totalNo))
probNo*=countNo/totalNo

for i in range(len(test)):
    countNo=0
    totalNo=0
    for row in mp[0]:
        if test[i]==row[i]:
            countNo +=1
        totalNo+=1
    print("for feature {}: {}/{}".format(i+1,countNo,totalNo))
    probNo*=countNo/totalNo

print("Probability of playing golf: {:.2f}%".format(probYes/(probYes+probNo)*100))