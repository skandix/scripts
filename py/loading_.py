def waiting(data):
    clearTerm()
    chrs = ["\\", "|", "/", "-"]
    for j in chrs:
        print ("{0} {1}".format(data, j))
        time.sleep(0.5)
