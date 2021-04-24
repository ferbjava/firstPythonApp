print("Program will remove unneeded lines in bpmn2 files")
filename = "bpmn2.xml"
with open(filename, "r") as f:
    lines = f.readlines()
with open(filename, "w") as f:
    lines2skip = 0
    for index, line in enumerate(lines):
        writeLine = True
        if lines2skip > 0:
            continue
        label = line.find("BPMNLabel")
        if label != -1:
            l = len(line)
            endingSlash = line.find("/")
            if endingSlash == -1:
                writeLine = True
            elif (l - endingSlash) == 3:
                writeLine = False
        if writeLine:
            f.write(line)
