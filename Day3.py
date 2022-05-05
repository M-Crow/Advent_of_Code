

# Input handling
with open("day3.txt") as fin:
    data = [i for i in fin.read().strip().split("\n")]


# Transform binary string into integer
def binary_to_int(binaryStr):
    return int(binaryStr, 2)


# Part 1 - Finding the Power Consumption
def part1():
    gammaRate = []
    epsilonRate = []

    # Iterate through every character in a bitString
    for i in range(0, len(data[0])):
        zeros = 0
        ones = 0


        # Iterate through all bitstrings 
        for bitString in data:

            # Add amounts of zeros and ones
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1

        
        # Check for most common
        if zeros > ones:
            gammaRate.append('0')
            epsilonRate.append('1')
        elif ones > zeros:
            gammaRate.append('1')
            epsilonRate.append('0')


    # Turn lists into bitStrings
    gammaRate = ''.join(gammaRate)
    epsilonRate = ''.join(epsilonRate)


    # Return power consumption
    powerConsumption = binary_to_int(gammaRate) * binary_to_int(epsilonRate)
    return powerConsumption
            


# Part 2 - Finding the Life Support Rating
def part2():
    
    # Finding Oxygen Generator Rating
    firstData = data.copy()
    
    # Iterate through shortened data
    i = 0
    while len(firstData) > 1:
        zeros = 0
        ones = 0

        # Binary counter
        for bitString in firstData:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1

        # List shortener
        if zeros > ones:
            firstData = [bitString for bitString in firstData if bitString[i] == '0']
        else:
            firstData = [bitString for bitString in firstData if bitString[i] == '1']

        i += 1

    oxygenRating = ''.join(firstData) 

    # Finding the CO2 Scrubber Rating
    secondData = data.copy()

    # Iterate through shortened data
    i = 0 
    while len(secondData) > 1:
        zeros = 0
        ones = 0

        # Binary counter
        for bitString in secondData:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1

        # List shortener
        if zeros > ones:
            secondData = [bitString for bitString in secondData if bitString[i] == '1']
        else:
            secondData = [bitString for bitString in secondData if bitString[i] == '0']

        i += 1

    carbonRating = ''.join(secondData)


    return binary_to_int(oxygenRating) * binary_to_int(carbonRating )



print("Answer to part 1: ", part1())
print("Answer to part 2: ", part2())

