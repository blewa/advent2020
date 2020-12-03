# read the file
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

validcount = 0
invalidcount = 0

for line in input:
    entry = line.rstrip().split(' ')

    # just substring out the min and max and oetter
    counts = entry[0].split("-")
    min_count = int(counts[0])
    max_count = int(counts[1])
    test_letter = entry[1][0]
    
    if entry[2].count(test_letter) >= min_count and entry[2].count(test_letter) <= max_count:
        validcount += 1
    else:
        invalidcount += 1

print("Valid: \t" + str(validcount))
print("Invalid:\t" + str(invalidcount))