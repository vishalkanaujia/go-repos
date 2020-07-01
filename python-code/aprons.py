'''
Background:

There are N airport aprons numbered from 1..N, located in sequential, equidistant manner. Any apron can be either empty or already assigned. As aircraft is landed, apron will be assigned to aircraft. When aircraft takes off, corresponding apron will become empty. Post landing, aircraft can approach apron from two gates, Gate A entering from apron 1 and gate B entering from apron N.

With an assumption that, time required to reach gate A or gate B from landing station is same, apron assignment algorithm assigns a gate (either A or B) and empty apron number X (1 <= X <= N) to aircraft, such that, aircraft have to travel minimal distance to reach the apron (to save time for passengers). Apron assignment algorithm prefers Gate A over Gate B in case of collision. If all aprons are assigned, aircraft is redirected to other terminal.
 

Problem:

You will be given:
1. Number of airport aprons (N) on first line.
2. Sequence of events in a limited time frame, with each event on new line. Event is described with event ID and aircraft name separated by space. Event ID could be aircraft landing at the airport (L) or aircraft taking off from the airport (T). If all aprons are assigned, aircraft is redirected to other terminal.

You have to design and implement apron assignment algorithm using efficient data structures so that apron assignment is optimal. Based on the designed algorithm, for each landed aircraft, you have to output the gate and apron number (separated by a space, each on new line) assigned to aircraft. If all aprons are assigned, output "REDIRECT".

Notes:
You can read input from file.
Assume that all aprons are empty in the beginning.
"REDIRECT"ed aircrafts are not considered for further assignment.

Sample input/output:
Input:

10
L SGP-506
L HAN-278
L BKK-398
L HAN-279
L SGP-507
T HAN-278
L KLA-237
L DEL-346
T HAN-279
L DEL-347
L HAN-280
L BKK-399
L KLA-238
T HAN-280
T BKK-398
L SGP-508
L DEL-348
L KLA-239
L BKK-400
T SGP-506
L HAN-281

Output:
A 1
B 10
A 2
B 9
A 3
B 10
B 8
B 9
A 4
B 7
A 5
A 2
A 4
B 6
REDIRECT
A 1
'''

# The approach is as following
'''
Maintain a mapping of each flight number to the apron assigned in a hash
Keep heaps of aprons from both gates.
'''
import heapq

class Schedule:
    def __init__(self):
        self.heapA = []
        self.heapB = []
        
def findClosestApron(self, apronsA, apronsB, size):
    self.heapA = heapq.heapify(apronsA)
    self.heapB = heapq.heapify(apronsB)

    minA = heapq.heappop(self.heapA)
    minB = heapq.heappop(self.heapB)
    minBNormalized = size + minB
    
    if size(self.heapA) < 1:
        return -1, "REDIRECT"
    
    if minA <= (minBNormalized):
        heapq.heappush(minB)
        return minA, "A"
    else:
        heapq.heappush(minA)
        return minB, "B"

def updateAprons(self, apronsA, apronsB, apron):
    heapq.heappush(self.heapA, apron)
    heapq.heappush(self.heapB, apron)

def findGate(self, schedules, apronCount):
    flightsInfo = {}
    apronsA = [x for x in range(1, apronCount+1)]
    apronsB = [-x for x in range(1, apronCount+1)]
    
    for schedule in schedules:
        event, flightNo = schedule
        if event == "L":
            flightsInfo.setdefault(flightNo, event)
            apron, gate = findClosestApron(apronsA, apronsB)
            if apronCount != -1:
                flightsInfo[flightNo] = apron
                return gate
            else:
                return "REDIRECT"
        if event == "T":
            apron = flightsInfo[flightNo]
            updateAprons(apronsA, apronsB, apron)
            del flightsInfo[flightNo]