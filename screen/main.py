import re

r, c = map(int, input().split())

if r == 1:
    mainLine = input()
elif r == 2:
    topLine = input()
    mainLine = input()
elif r == 3:
    topLine = input()
    mainLine = input()
    bottomLine = input()

newMainLine = mainLine

squareRootRanges = []
fractionRanges = []

fraction = re.compile("=+")
squareRootStart = re.compile(r"\\/")
squareRootBody = re.compile("_+")

if r >= 2:
    for match in re.finditer(squareRootBody, topLine):
        squareRootRanges.append((match.start(), match.end()))

startIndex = 0

while True:
    match = re.search(fraction, mainLine[startIndex:])
    if match is None:
        break
    startIndex = match.end() + 1
    newFrac = '(' + topLine[match.start():match.end()] + ')' + '/' + '(' + bottomLine[match.start():match.end()] + ')'
    newMainLine = newMainLine[:match.start()] + newFrac + newMainLine[match.end():]

print(newMainLine)