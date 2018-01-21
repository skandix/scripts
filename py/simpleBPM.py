from time import sleep, time

avgTap = []

while True:
    start = time()
    tap = raw_input()
    if tap == "":
        diff = time() - start
        avgTap.append(diff)
        avgTapElem = (sum(avgTap)/len(avgTap))
        print "\nDiff:{}\nAvg:{}\nBPM:{}\nAvgBPM:{}".format(diff, avgTapElem,60/diff, 60/avgTapElem)
    elif tap == 'q':
        break
