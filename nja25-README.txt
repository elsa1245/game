NetID: nja25

SUMMARY: 
I incorporated multiple helper functions, as well as functions for evaluating duplicate states and performing other statistical tests as part of this assignment. All trials of my script were run against the greedy player. My script runs out of time for max depth > 3, but summary stats for depth = 4 that are listed below are taken from the script's last iteration run before timing out. Time limit would have to be adjusted for my script to be successful with max depth greater than 3.

****DISCLAIMER*****: Heuristic used for minimax in 'minimax_function()' is not mine. I give all credit to the creators of the project at the following webpage:

http://www.cs.cornell.edu/~yuli/othello/othello.html


RESULTS:

1. Minimax:

Depth 2		nodes: 2046	duplicates: 363		avg. branch: 6.16	runtime/iteration: 0.066 seconds

Depth 3		nodes: 11718	duplicates: 1386		avg. branch: 8.49	runtime/iteration: 0.45 seconds

Depth 4		nodes: 50791	duplicates: 4960		avg. branch: 9.57	runtime/iteration: 4.12 seconds



2. Alpha-Beta Pruning

Depth 2		nodes: 2046	duplicates: 363		avg. branch: 6.16	runtime/iteration: 0.066 seconds

Depth 3		nodes: 7406	duplicates: 1386		avg. branch: 5.37	runtime/iteration: 0.24 seconds

Depth 4		nodes: 41609	duplicates: 7297		avg. branch: 5.47	runtime/iteration: 2.61 seconds


We observe that summary stats are identical between minimax and alpha-beta when depth = 2, implying that the effects of alpha-beta pruning are not pronounced enough to make a difference when max depth is limited to be shallow. When depth is increased, however, statistics improve considerably under alpha-beta treatment, even though the script runs out of time. We observe, for example, that alpha-beta at depth = 3 yields nearly a 50% reduction in runtime per iteration as compared to minimax. Alpha-beta treatment also reduces average branching factor and number of nodes expanded at depths 3 and 4.