# CMPS 2200 Assignment 3
## Answers

**Name:** Viv Heurtevant


Place all written answers from `assignment-03.md` here for easier grading.

IMPORTANT NOTE REGARDING FAST ALIGN: I was unable to find the tie breaking condition that satisfied all test cases, so I chose algorithm that prefers insertion in S in the case of tie. When testing, I found that kookaburra and book have opposite tie priorities so I was unsure how to satisfy both.

**1a)** Given a $N$ dollars, state a greedy algorithm for producing
as few coins as possible that sum to $N$.

The greedy algorithm would be to choose the largest such k such that $2^k \leq N$. Then, add this $2^k$ to our list and subtract its amount from $N$. We then repeat this process for the reduced N, until N is 0. This is notably the same process used for converting a decimal number to binary due to each coin being some power of 2.


**1b)** Prove that this algorithm is optimal by proving the greedy
  choice and optimal substructure properties.

Greedy choice- We define the greedy choice as taking the largest $2^k$ such that $2^k <= N$. If we chose a larger value of of $k$ it would go over our total, and if we choose a smaller value, $k_*$, such that $k_*$ is $k-j$ where $1 \leq j \leq k$ then we would need $2^k=2^{k_*}2^{j}$ coins to represent the same amount, resulting in an additional $2^j$ coins to our list. So by choosing the largest $k$ we are able to minimize the amount of coins added to the list.

Optimal substructure- We want to show that after the greedy choice, $N'=N-2^k$ can also be solved optimally and will give optimal solution for $N$.

Let the remaining sum of coins of $N-2^k$ be denoted R, so our solution is $S=2^k + R$, where $S$ is the optimal solution we proved from Greedy choice. Now, we assume that R is not optimal for N, meaning there exists a different subproblem $R_*$ such that $|R_*|< |R|$. Then the new solution, $S_* = 2^k + R_*$. However, $|S_*|=1+|R_*| < 1+|R| = |S|$. This implies that the new solution uses less coins, which contradicts the property that S is optimal.So, if we have the optimal solution $S$ with the greedy choice property, then it follows that the subproblems $R$ can be solved with this property.

**1c)** What is the work and span of your algorithm?

Finding the largest power of $2^k$ can be done by taking the floor of $\log_2(N)$, which is constant. We remove this amount each time, giving the relation: $W(N)=W(N-2^{\log_2(N)})+1$ (Where the log operation is floored each time).
The problem is a balanced recursion, and we see that the depth of the problem will be $O(log_n)$ (The optimal choice will be guaranteed to be above half of the size of N each time, otherwise there is a larger k we could choose so we reduce the problem slightly in half each time. It is balanced because it stays 1 node per level and we have same amt.of work at each level. )so our total work is $O(log_n)$

This problem is fully sequential so we base the span on the longest dependency chain, which we deduced from the work will be $log_n$ so the span is $O(log_n)$.

**2a)** You realize the greedy algorithm you devised above doesn't
  work in Fortuito. Give a simple counterexample that shows that the
  greedy algorithm does not produce the fewest number of coins.
  
Suppose we have coins with values ${1,3,4}$ and want to make 6 cents. The greedy choice would be to choose $4$ and then two $1$ coins, which is a three coin solution. However, the optimal solution is to only pick two $3$ cent coins even though $3$ is not the highest value. So greedy fails.

**2b)** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.

  Suppose some coin $c$ is in the optimal solution $N$. Then the solution is $N= c + R$, where R is the remaining amount of change to be made. It then follows that $R$ is the optimal solution for the subproblem $N-c$. 

  For contradiction, we assume that $R$ is not optimal for $N-c$ and there is a better solution $R_*$. Then $|R_*| < |R|$. So $|S_*|=1+|R_*|< |S|= 1 + |R|$ Which means $|S_*|< |S|$, which contradicts that $S$ is the optimal solution. 

  **2c)** Use this optimal substructure property to design a
  dynamic programming algorithm for this problem. If you used top-down
  or bottom-up memoization to avoid recomputing solutions to
  subproblems, what is the work and span of your approach?

We can use an array to store iterative results in the bottom-up solution to prevent recomputing subprolems. For each $N \in [0,1,....N]$, where we can compute $T[n]=min(1+T[n-c],T[n]) for all coin values c.

The work of this problem would be linear, as we consider $N$ cases with C subproblems. We could write W= O(|C|*N) to be precise, as the work will depend on both N and C. The span of the problem will grow linearly with the amount of distinct subproblems, which is around $N+1$, so we can see the span will be $O(n).$
