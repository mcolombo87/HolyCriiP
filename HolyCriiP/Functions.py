
def converHashToNum(hashKey):
    dictionary = { "0" : 1, "1" : 2, "2" : 3, "3" : 4, "4" : 5, "5" : 6, "6" : 7, "7": 8, "8" : 9, "9" : 10, 
                  "a" : 11, "b" : 12, "c" : 13, "d" : 14, "e" : 15, "f" : 16 }
    count = 1
    accumulator = 0
    for i in hashKey:
        accumulator = accumulator + (dictionary[i] * count)
        count += 1
    return accumulator