import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def med_top_down(S, T, MED={}):
    ## look up the memory
    if (S, T) in MED:
        return MED[(S, T)]
    ## base cases
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    ## recursive cases
    if S[0] == T[0]:  # If first characters are the same, move to the next
        MED[(S, T)] = med_top_down(S[1:], T[1:], MED)
    else:
        insert = med_top_down(S, T[1:], MED) + 1  # Insert a character
        delete = med_top_down(S[1:], T, MED) + 1  # Delete a character
        MED[(S, T)] = min(insert, delete)
    
    return MED[(S, T)]
    
def fast_MED(S, T):
    s = len(S)
    t = len(T)

    dp = [[0]*(t+1) for _ in range(s+1)] # Intializes Array

    for i in range(s+1): #Base cases.
        dp[i][0] = i  
    for j in range(t+1):
        dp[0][j] = j   
        
    for i in range(1, s+1):
        for j in range(1, t+1):
            if S[i-1] == T[j-1]:       # Characters match, no change needed
                dp[i][j] = dp[i-1][j-1]
            else:                       # Checks previous subproblems to see if inserting or deleting is better
                dp[i][j] = 1 + min(
                    dp[i][j-1],    # insert
                    dp[i-1][j]     # delete
                )
    return (dp[s][t]) #The optimum solution
    
def fast_align_MED(S, T):

    #Start by building table
    s = len(S)
    t = len(T)

    dp = [[0]*(t+1) for _ in range(s+1)] # Intializes Array

    for i in range(s+1): #Base cases.
        dp[i][0] = i  
    for j in range(t+1):
        dp[0][j] = j   
        
    for i in range(1, s+1):
        for j in range(1, t+1):
            if S[i-1] == T[j-1]:       # Characters match, no change needed
                dp[i][j] = dp[i-1][j-1]
            else:                       # Checks previous subproblems to see if inserting or deleting is better
                dp[i][j] = 1 + min(
                    dp[i][j-1],    # insert
                    dp[i-1][j]     # delete
                )

    aligned_S = []
    aligned_T = []
    i, j = s, t
    #Start with optimum solution and backtrack 
    while i > 0 or j > 0:
        # Match
        if i > 0 and j > 0 and S[i-1] == T[j-1]:
            aligned_S.append(S[i-1])
            aligned_T.append(T[j-1])
            i -= 1
            j -= 1
        # Prefer insertion into S (dash in S) in case of tie
        elif j > 0 and (i == 0 or dp[i][j-1] <= dp[i-1][j]):
            aligned_S.append('-')
            aligned_T.append(T[j-1])
            j -= 1
        else:
            # Otherwise deletion from S is optimal (dash in T)
            aligned_S.append(S[i-1])
            aligned_T.append('-')
            i -= 1
    
    return ''.join(reversed(aligned_S)), ''.join(reversed(aligned_T)) #Reverses (built backwards) and concatenates into string

