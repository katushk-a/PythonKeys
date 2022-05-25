import random
from time import time

def giveNumberOfKeys(n):
    return pow(2, n)
    
def generateRandomKey(n):
    resultString = ''
    for l in range(n):
        resultString += str(random.choice([0,1]))
    return resultString
    
def bruteForce(n):
    length = len(n)
    wrongAnswers = []
    slot = ''
    run = True
    variants = [0, 1]
    timebefore = int(time() * 1000)
    while run:
        slot = ''
        for i in range(length):
            slot += str(random.choice(variants))
        if slot not in wrongAnswers:
            if slot != n:
                wrongAnswers.append(slot)
            else:
                run = False
    timeafter = int(time() * 1000)
    return timeafter - timebefore


numbers = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
print('Numbers of keys and a random key:')   
for n in numbers:
    print('{0} bits: '.format(n))
    print('Number of keys:')
    print(giveNumberOfKeys(n))
    print("A random key: ")
    r = generateRandomKey(n)
    print(r)
    print("Time for brute force: ")
    print('{0} ms'.format(bruteForce(r)))
    print('')
    