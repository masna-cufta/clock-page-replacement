import random

numProcesses = 3
pagesPerProcess = 4
numAccesses = 20  
numFrames = 5       
frames = [None] * numFrames
refBits = [0] * numFrames
clockHand = 0
table = {}
for pid in range(1, numProcesses + 1):
    table[pid] = {}
    for page in range(pagesPerProcess):
        table[pid][page] = None

def printState():
    print("Frames status:")
    for i in range(numFrames):
        if frames[i] is None:
            print("  Frame", i, ": [free]")
        else:
            pid, page = frames[i]
            print("  Frame", i, ": [", pid, ":", page, "]")
    print("Ref bits:", refBits)
    print("Clock hand position:", clockHand)
    print()

def findVictim():
    global clockHand
    while 1:
        if refBits[clockHand] == 0:
            victim = clockHand
            clockHand = (clockHand + 1) % numFrames
            return victim
        else:
            refBits[clockHand] = 0
            clockHand = (clockHand + 1) % numFrames

def HitOrMiss(pid, pageNum):
    global frames, refBits, table

    print("Process", pid, "performs access on page", pageNum)

    frameIndex = table[pid][pageNum]

    if frameIndex is not None:
        print("HIT:")
        print("  Page", pageNum, "of process", pid, "is already in frame", frameIndex)
        refBits[frameIndex] = 1
    else:
        print("MISS:")
        freeFrame = None
        for idx in range(numFrames):
            if frames[idx] is None:
                freeFrame = idx
                break

        if freeFrame is not None:
            print("  Found free frame:", freeFrame)
            victimFrame = freeFrame
        else:
            print("  No free frames, using clock algorithm")
            victimFrame = findVictim()
            oldPid, oldPage = frames[victimFrame]
            print("  Removing page", oldPage, "of process", oldPid, "from frame", victimFrame)
            table[oldPid][oldPage] = None

        frames[victimFrame] = (pid, pageNum)
        table[pid][pageNum] = victimFrame
        refBits[victimFrame] = 1
        print("  Loaded page", pageNum, "of process", pid, "into frame", victimFrame)

    printState()

def simulate():
    for i in range(1, numAccesses + 1):
        print("    Access number", i)
        pid = random.randint(1, numProcesses)
        pageNum = random.randint(0, pagesPerProcess - 1)
        HitOrMiss(pid, pageNum)

if __name__ == "__main__":
    print("Simulation with", numFrames, "frames,", numProcesses, "processes and", pagesPerProcess, "pages each")
    printState()
    simulate()
