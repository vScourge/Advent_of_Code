import sys
import re
import copy

def readFile(fileName):
    records = []
    with open(fileName) as file:
        for line in file:
            line = str(line.strip())
            line = re.findall(r'[ns]*[we]', line)
            records.append(line)
    return records

def makeKey(x, y):
    return str(x) + ',' + str(y)

def main(fileName):
    records = readFile(fileName)
    flipped = {}
    for i in range(-50, 51):
        for j in range(-50, 51):
            if (i + j) % 2 == 0:
                key = str(i) + ',' + str(j)
                flipped[key] = 'White'
    for record in records:
        x = 0
        y = 0
        for i in record:
            if i == 'ne':
                x += 1
                y += 1
            elif i == 'e':
                x += 2
            elif i == 'se':
                x += 1
                y -= 1
            elif i == 'nw':
                x -= 1
                y += 1
            elif i == 'w':
                x -= 2
            elif i == 'sw':
                x -= 1
                y -= 1
        key = str(x) + ',' + str(y)
        if key not in flipped.keys():
            flipped[key] = 'Black'
        else:
            if flipped[key] == 'Black':
                flipped[key] = 'White'
            else:
                flipped[key] = 'Black'
    temp = {}
    for c in range(100):
        for i in flipped.keys():
            x = int(i[0:i.index(',')])
            y = int(i[i.index(',') + 1:])
            around = [makeKey(x + 1, y + 1), makeKey(x + 2, y), makeKey(x + 1, y - 1), makeKey(x - 1, y + 1), makeKey(x - 2, y), makeKey(x - 1, y - 1)]
            count = 0
            for j in around:
                if j in flipped.keys():
                    if flipped[j] == 'Black':
                        count += 1
                else:
                    temp[j] = 'White'
            if flipped[i] == 'Black':
                if count == 0 or count > 2:
                    temp[i] = 'White'
                else:
                    temp[i] = 'Black'
            else:
                if count == 2:
                    temp[i] = 'Black'
                else:
                    temp[i] = 'White'
        flipped = copy.deepcopy(temp)
    count = 0
    for i in flipped.keys():
        if flipped[i] == 'Black':
            count += 1
    print(count)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        fileName = 'input.txt'
    else:
        fileName = sys.argv[1]
    main(fileName)