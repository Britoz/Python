f = open('new.txt', 'r')
passFILE = open('passFILE.txt', 'w')
failFILE = open('failFILE.txt', 'w')

# TODO: read all files
for line in f:
    line_split = line.split()

    # TODO: only print which is 'P'
    if line_split[2] == 'P':
        passFILE.write(line)
    else:
        failFILE.write(line)

# TODO: close file after use
f.close()
passFILE.close()
failFILE.close()