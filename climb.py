'''
Problem Breakdown
Alice can climb either 1 step or M steps at a time.
We need to determine the minimum number of climbs required to reach exactly N steps.
Approach
Maximize Larger Steps:

To minimize the total number of climbs, Alice should maximize the number of M-step climbs because climbing more steps at once will reduce the total number of climbs.
Calculate the Number of M-Climbs:

We can use as many M-step climbs as possible. The number of such climbs is N // M.
Calculate the Remaining Steps:

After using as many M-step climbs as possible, Alice might have some remaining steps. The number of these remaining steps is N % M.
Total Climbs:

The total number of climbs is the sum of the number of M-step climbs plus the number of remaining 1-step climbs.'''
def minimum_climbs(N, M):
    # Number of M-climbs
    m_climbs = N // M
    
    # Remaining steps after taking maximum possible M-climbs
    remaining_steps = N % M
    
    # Total climbs = M-climbs + remaining 1-climbs
    total_climbs = m_climbs + remaining_steps
    
    return total_climbs

# Sample Input
N, M = map(int, input().split())

# Output the minimum number of climbs
print(minimum_climbs(N, M))
