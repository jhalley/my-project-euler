def pe63():
    count = 0
     
    for i in range(1,1000):
        temp = 1
        while True:
            if not len(str(temp**i)) < i: break
            else: temp += 1
        while True:
            if len(str(temp**i)) > i: break
            else:
                count += 1
                temp += 1

    return count

print pe63()
