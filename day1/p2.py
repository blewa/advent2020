# read the file
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

# cleanup/cast as int
cleaned_input = [int(i.rstrip()) for i in input]

#loop it!
for a in cleaned_input:
    for b in cleaned_input:
        for c in cleaned_input:
            if b + a + c == 2020:
                print(b*a*c)
                exit()