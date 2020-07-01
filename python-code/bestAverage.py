def prepareAverage(records):
    scoreDict = {}

    for record in records:
        ID = record[0]
        score = int(record[1])

        if ID in scoreDict:
            total = scoreDict[ID][0]
            count = scoreDict[ID][1]

            count += 1
            total += score

            scoreDict[ID][1] = count
            scoreDict[ID][0] = total
        else:
            scoreDict[ID] = [score, 1]

    maxAvg = 0
    bestID = None
    for ID in scoreDict:
        record = scoreDict[ID]
        average = record[0]/record[1]
        if maxAvg < average:
            maxAvg = average
            bestID = ID

    print(maxAvg, bestID)


records = [["A", "7"], ["B", "100"], ["C", "50"], ["B", "50"]]
print(prepareAverage(records))
