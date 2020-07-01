def prefixSum(A):
    n = len(A)
    prefix = [0]*(n + 1)
    
    for k in range(1, n+1):
        prefix[k] = prefix[k - 1] + A[k - 1]
    print(prefix)
    return prefix

def maxMushrooms(A, k, m):
    prefix = prefixSum(A)
    l = len(A)
    org_k = k
    answer = 0
    
    start = k
    
    # case 1. Move forward
    end = min(k + m, l-1)
    pdiff = prefix[end+1] - prefix[start]
    print(pdiff, prefix[end+1], prefix[start])
    answer = max(answer, pdiff)
    
    # case 2 Move left
    end = k
    
    start = k - min(k, m)
    pdiff = prefix[end+1] - prefix[start]
    print(pdiff, prefix[end+1], prefix[start])
    answer = max(answer, pdiff)
    
    # case 3: Mix left & right
    
    # At position k you can go back least of both.
    # k = 4 m = 2, you can't move more than given moves i.e. 2
    # k= 1 m = 10 you can't move more than 1 move.
    max_ops = min(m, k) 
    
    while max_ops > 0:
        start = k - max_ops
        #print("start={}".format(start))
        
        print("remaining steps m={} consumes={}".format(m, (2 * max_ops)))
        # m - (2 * max_ops) can have negative value.
        # m = 6, max_ops = 4 diff = 6 - (2*4) this means
        # no operations remain to move right from position k.
        # So the end is k itself.
        end = min(k +  max(0, m - (2 * max_ops)), l-1)
        print("end={}".format(end))

        pdiff = prefix[end+1] - prefix[start]
        print(start, end+1, prefix[start], prefix[end+1])
        answer = max(answer, pdiff)
        max_ops -= 1

    print("answer={}".format(answer))
    
A = [2,3,1,7,5,1,3,9]
k = 4
m = 6 
#maxMushrooms(A, k, m)

A = [9,1,1,1,1,1,9]
k = 3
m = 4
#maxMushrooms(A, k, m)

A = [9,2,1,1,1,1,9]
k = 3
m = 10
print(A)
maxMushrooms(A, k, m)