def find_missing(a, b):
    missing = []
    for i in a:
        t = 0
        for i2 in b:
            if i2 == i:
                t = 1
                break
                
        if t == 0:
            missing.append(i)
    print(f"The missing number is {missing}")

find_missing([4,12,9,5,6,13,16],[4,9,12,6])