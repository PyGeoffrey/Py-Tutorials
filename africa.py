inFile = open('africa.txt', 'r')          # open africa.txt for reading in
countries = inFile.readlines()            # read all lines into a list
inFile.close()                            # close the file
countries.sort()                          # sort in alphabetical order
longestLength = 0  # initialize longest length
for country in countries:
    if len(country) - 1 > longestLength:    # found new longest length
        longestLength = len(country) - 1  # save the new longest length

outFile = open('africasorted.txt', 'w')   # open the output file
for country in countries:
    country = country.strip('\n')
    outputLine = country
    outputLine += ' ' * (longestLength - len(country))  # padding
    outputLine += ' '  # space between name and digit(s)
    if len(country) < 10:
        outputLine += ' '   # extra space for single-digit numbers
    outputLine += str(len(country)) + '\n'
    outFile.write(outputLine)
outFile.close()