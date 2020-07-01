
c = 0
def countOneBS(row, start, end):
    global c
    if row[start] == 0:
        return 0

    if row[end] == 1:
        return end - start + 1

    mid = start+ (end - start) // 2
    if c == 50:
        return 0
    else:
        c += 1
    print("mid=", mid, "start=", start, "end=", end)
    return countOneBS(row, start, mid) + countOneBS(row, mid + 1, end)

#l = [1,1,1,0,0,0]
#l = [1,0,0,0,0]
#l = [1,1,1,1,0]
l = [1,1,0,0,0]
print(countOneBS(l, 0, len(l) - 1))
