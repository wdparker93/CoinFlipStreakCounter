import random

numberOfGlobalStreaks = 0
for i in range(10000):
    numStreaks = 0
    flipRecord = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            flipRecord.append('H')
        else:
            flipRecord.append('T')
    counter = 0
    streakCounter = 0
    while counter < (len(flipRecord) -1):
        value = flipRecord[counter]
        if flipRecord[counter + 1] == value:
            counter += 1
            streakCounter += 1
            if streakCounter >= 6:
                numStreaks += 1
        else:
            counter += 1
            streakCounter = 0
    if numStreaks >= 1:
        numberOfGlobalStreaks += 1

print('A >= 6-long streak of either heads or tails happens ' + str(numberOfGlobalStreaks/100) + '% of the time.')
