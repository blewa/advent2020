# read the file
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

validcount = 0
invalidcount = 0

for line in input:
    entry = line.rstrip().split(' ')

    positions = entry[0].split("-")
    p1 = int(positions[0]) - 1
    p2 = int(positions[1]) - 1
    test_letter = entry[1][0]
    
    # so an xor in python with strings is not "easy"...need to learn a more elegant way.
    if (entry[2][p1] == test_letter and not entry[2][p2] == test_letter) or (not entry[2][p1] == test_letter and entry[2][p2] == test_letter):
        validcount += 1
    else:
        invalidcount += 1

print("Valid: \t" + str(validcount))
print("Invalid:\t" + str(invalidcount))