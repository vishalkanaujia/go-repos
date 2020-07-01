def substrings(str):
    size = len(str)
    for i in range(1, size):
        # pick the start index
        for start in range(0, size):
            sub = str[start:start+i]
            print(sub)

substrings("abcd")




