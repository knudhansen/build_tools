import sys

pycpInput = sys.argv[1]
pycpOutput = sys.argv[2]

print("in: %s -> out: %s" % (pycpInput, pycpOutput))

inFile = open(pycpInput)
outFile = open(pycpOutput, 'w')

for line in inFile.readlines():
    outFile.write(line)
