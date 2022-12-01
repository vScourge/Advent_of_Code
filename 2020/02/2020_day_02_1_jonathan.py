input_file = open('input.txt').read().splitlines()
print(input_file)
validCount = 0
entries = []
policiesList = []
passwordsList = []
boundsList = []
lettersList = []
minList = []
maxList = []
for line in input_file:
	entries.append(line.split(":"))
print(entries)
#splitting up the policies from passwords
for [policy, password] in entries:
	policiesList.append(policy)
	passwordsList.append(password.strip())
#print(policiesList)
#print(passwordsList)
#separating the bounds from the letters
for substring in policiesList:
	bounds = substring.split(' ')[0]
	boundsList.append(bounds)
	letters = substring.split(' ')[1]
	lettersList.append(letters)
#separating upper and lower bounds
for bound in boundsList:
	bounds_split = bound.split('-')
	bMin = int(bounds_split[0])
	bMax = int(bounds_split[1])
	minList.append(bMin)
	maxList.append(bMax)
print(minList)
print(maxList)
#Part 1 Code
#for i in range(len(passwordsList)):
								#password = passwordsList[i]
								#letter = lettersList[i]
								#mincount = minList[i]
								#maxcount = maxList[i]
								#instances = password.count(letter)
								#if instances <= maxcount:
												#if instances >= mincount
																#validCount = validCount + 1
#print(validCount)
#Part 2 Code
eitherCorrect = 0
bothCorrect = 0

for i in range(len(passwordsList)):
	password = passwordsList[i]
	letter = lettersList[i]
	firstPos = password[minList[i]-1]
	secondPos = password[maxList[i]-1]
	if firstPos == letter or secondPos == letter:
		eitherCorrect += 1
	if firstPos == letter and secondPos == letter: 
		bothCorrect += 1
validCount = eitherCorrect - bothCorrect

print( validCount )










