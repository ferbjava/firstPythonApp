print("Program will remove unneeded lines in bpmn2 files")
filename = "bpmn2.xml"

def checkLabels(line):
    global writeLine, lines2skip
    label = line.find("BPMNLabel")
    if label != -1:
        l = len(line)
        endingSlash = line.find("/")
        if endingSlash == -1:
            line2 = lines[index + 2]
            sndEndingSlash = line2.strip().find("/")
            endingLabel = line2.find("BPMNLabel")
            if sndEndingSlash == 1 and endingLabel != -1:
                writeLine = False
                lines2skip = 2
        elif (l - endingSlash) == 3:
            writeLine = False


with open(filename, "r") as f:
    lines = f.readlines()
with open(filename, "w") as f:
    lines2skip = 0
    for index, line in enumerate(lines):
        writeLine = True
        if lines2skip > 0:
            print("line ", index + 1, " removed:", line)
            lines2skip -= 1
            continue

        checkLabels(line)

        if writeLine:
            f.write(line)
        else:
            print("line ", index + 1, " removed:", line)

