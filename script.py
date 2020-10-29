import random


def generateDNASequence():
    listOfGenomes = ["T", "G", "C", "A"]
    for i in range(40):
        dnaSequence = (random.choice(listOfGenomes))
        print(dnaSequence, end="")
    return dnaSequence


def applyGammaRadiation(dnaSequence):
    pass
    chance = random.randint(0, 100)
    if (chance >= 50):
        # Wrong 1
        # placeInDNA = random.randint(0, 40)
        placeInDNA = random.randint(0, 39)
        if (dnaSequence[placeInDNA] == 'T'):
            listOfGenomes = ["G", "C", "A"]
            randomGenome = (random.choice(listOfGenomes))
            mutatedSequence = dnaSequence.replace(randomGenome, dnaSequence[placeInDNA])
            return mutatedSequence
        elif (dnaSequence[placeInDNA] == 'G'):
            listOfGenomes = ["T", "C", "A"]
            randomGenome = (random.choice(listOfGenomes))
            mutatedSequence = dnaSequence.replace(randomGenome, dnaSequence[placeInDNA])
            return mutatedSequence
        elif (dnaSequence[placeInDNA] == 'C'):
            listOfGenomes = ["T", "G", "A"]
            randomGenome = (random.choice(listOfGenomes))
            mutatedSequence = dnaSequence.replace(randomGenome, dnaSequence[placeInDNA])
            return mutatedSequence
        elif (dnaSequence[placeInDNA] == 'A'):
            listOfGenomes = ["T", "G", "A"]
            randomGenome = (random.choice(listOfGenomes))
            mutatedSequence = dnaSequence.replace(randomGenome, dnaSequence[placeInDNA])
            return mutatedSequence
    elif (chance < 50):
        return dnaSequence


def detectMutation(dna1, mutatedDna):
    length = len(dna1)
    mutation = 0
    for x in range(length):
        dna2 = dna1[x - 1]
        dna3 = mutatedDna[x - 1]
        if dna2 == dna3:
            print(" ")
        else:
            print("^")
            mutation += 1
        if mutation > 0:
            print("mutation Detected")
        else:
            print("no Mutation Detected")


dnaSequence = generateDNASequence()
mutatedSequence = applyGammaRadiation(dnaSequence)
detectMutation(dnaSequence, mutatedSequence)
