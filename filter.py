from os import walk

_, _, filenames = next(walk("results"))

print(filenames)

file1 = open('cdbc.lst', 'r')
Lines = file1.readlines()
file1.close()

# filtering
filtered = []
for line in Lines:
    if any(filename[:-4] in line for filename in filenames):
        continue
    filtered.append(line)

file2 = open('cdbc.filtered.lst', 'w')
file2.writelines(filtered)
file2.close()