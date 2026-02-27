### Optimization Methods in Finance

Gerard Cornuejols
Reha T¨ut¨unc¨u

Carnegie Mellon University, Pittsburgh, PA 15213 USA


January 2006


2


Foreword
Optimization models play an increasingly important role in financial decisions. Many computational finance problems ranging from asset allocation
to risk management, from option pricing to model calibration can be solved
efficiently using modern optimization techniques. This course discusses several classes of optimization problems (including linear, quadratic, integer,
dynamic, stochastic, conic, and robust programming) encountered in financial models. For each problem class, after introducing the relevant theory
(optimality conditions, duality, etc.) and efficient solution methods, we discuss several problems of mathematical finance that can be modeled within
this problem class. In addition to classical and well-known models such
as Markowitz’ mean-variance optimization model we present some newer
optimization models for a variety of financial problems.


Acknowledgements
This book has its origins in courses taught at Carnegie Mellon University
in the Masters program in Computational Finance and in the MBA program
at the Tepper School of Business (G´erard Cornu´ejols), and at the Tokyo Institute of Technology, Japan, and the University of Coimbra, Portugal (Reha
T¨ut¨unc¨u). We thank the attendants of these courses for their feedback and
for many stimulating discussions. We would also like to thank the colleagues
who provided the initial impetus for this project, especially Michael Trick,
John Hooker, Sanjay Srivastava, Rick Green, Yanjun Li, Lu´ıs Vicente and
Masakazu Kojima. Various drafts of this book were experimented with in
class by Javier Pe˜na, Fran¸cois Margot, Miroslav Karamanov and Kathie
Cameron, and we thank them for their comments.


# Contents

1 Introduction 9
1.1 Optimization Problems . . . . . . . . . . . . . . . . . . . . . . 9
1.1.1 Linear Programming . . . . . . . . . . . . . . . . . . . 10
1.1.2 Quadratic Programming . . . . . . . . . . . . . . . . . 11
1.1.3 Conic Optimization . . . . . . . . . . . . . . . . . . . 11
1.1.4 Integer Programming . . . . . . . . . . . . . . . . . . 12
1.1.5 Dynamic Programming . . . . . . . . . . . . . . . . . 13
1.2 Optimization with Data Uncertainty . . . . . . . . . . . . . . 13
1.2.1 Stochastic Programming . . . . . . . . . . . . . . . . . 13
1.2.2 Robust Optimization . . . . . . . . . . . . . . . . . . . 14
1.3 Financial Mathematics . . . . . . . . . . . . . . . . . . . . . . 15
1.3.1 Portfolio Selection and Asset Allocation . . . . . . . . 16
1.3.2 Pricing and Hedging of Options . . . . . . . . . . . . . 18
1.3.3 Risk Management . . . . . . . . . . . . . . . . . . . . 19
1.3.4 Asset/Liability Management . . . . . . . . . . . . . . 20


2 Linear Programming: Theory and Algorithms 21
2.1 The Linear Programming Problem . . . . . . . . . . . . . . . 21
2.2 Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.3 Optimality Conditions . . . . . . . . . . . . . . . . . . . . . . 26
2.4 The Simplex Method . . . . . . . . . . . . . . . . . . . . . . . 29
2.4.1 Basic Solutions . . . . . . . . . . . . . . . . . . . . . . 30
2.4.2 Simplex Iterations . . . . . . . . . . . . . . . . . . . . 33
2.4.3 The Tableau Form of the Simplex Method . . . . . . . 37
2.4.4 Graphical Interpretation . . . . . . . . . . . . . . . . . 40
2.4.5 The Dual Simplex Method . . . . . . . . . . . . . . . 41
2.4.6 Alternatives to the Simplex Method . . . . . . . . . . 43


3 LP Models: Asset/Liability Cash Flow Matching 45
3.1 Short Term Financing . . . . . . . . . . . . . . . . . . . . . . 45
3.1.1 Modeling . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.1.2 Solving the Model with SOLVER . . . . . . . . . . . . 48
3.1.3 Interpreting the output of SOLVER . . . . . . . . . . 51
3.1.4 Modeling Languages . . . . . . . . . . . . . . . . . . . 52
3.1.5 Features of Linear Programs . . . . . . . . . . . . . . 53
3.2 Dedication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
3.3 Sensitivity Analysis for Linear Programming . . . . . . . . . 56


3


4 CONTENTS


3.3.1 Short Term Financing . . . . . . . . . . . . . . . . . . 56
3.3.2 Dedication . . . . . . . . . . . . . . . . . . . . . . . . 61
3.4 Case Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64


4 LP Models: Asset Pricing and Arbitrage 67
4.1 The Fundamental Theorem of Asset Pricing . . . . . . . . . . 67
4.1.1 Replication . . . . . . . . . . . . . . . . . . . . . . . . 69
4.1.2 Risk-Neutral Probabilities . . . . . . . . . . . . . . . . 70
4.1.3 The Fundamental Theorem of Asset Pricing . . . . . . 72
4.2 Arbitrage Detection Using Linear Programming . . . . . . . . 73
4.3 Additional Exercises . . . . . . . . . . . . . . . . . . . . . . . 76
4.4 Case Study: Tax Clientele Effects in Bond Portfolio Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80


5 Nonlinear Programming: Theory and Algorithms 83
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
5.2 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5.3 Univariate Optimization . . . . . . . . . . . . . . . . . . . . . 86
5.3.1 Binary search . . . . . . . . . . . . . . . . . . . . . . . 86
5.3.2 Newton’s Method . . . . . . . . . . . . . . . . . . . . . 90
5.3.3 Approximate Line Search . . . . . . . . . . . . . . . . 93
5.4 Unconstrained Optimization . . . . . . . . . . . . . . . . . . . 95
5.4.1 Steepest Descent . . . . . . . . . . . . . . . . . . . . . 95
5.4.2 Newton’s Method . . . . . . . . . . . . . . . . . . . . . 99
5.5 Constrained Optimization . . . . . . . . . . . . . . . . . . . . 102
5.5.1 The generalized reduced gradient method . . . . . . . 105
5.5.2 Sequential Quadratic Programming . . . . . . . . . . . 110
5.6 Nonsmooth Optimization: Subgradient Methods . . . . . . . 111


6 NLP Models: Volatility Estimation 113
6.1 Volatility Estimation with GARCH Models . . . . . . . . . . 113
6.2 Estimating a Volatility Surface . . . . . . . . . . . . . . . . . 117


7 Quadratic Programming: Theory and Algorithms 123
7.1 The Quadratic Programming Problem . . . . . . . . . . . . . 123
7.2 Optimality Conditions . . . . . . . . . . . . . . . . . . . . . . 124
7.3 Interior-Point Methods . . . . . . . . . . . . . . . . . . . . . . 126
7.4 The Central Path . . . . . . . . . . . . . . . . . . . . . . . . . 129
7.5 Interior-Point Methods . . . . . . . . . . . . . . . . . . . . . . 130
7.5.1 Path-Following Algorithms . . . . . . . . . . . . . . . 130
7.5.2 Centered Newton directions . . . . . . . . . . . . . . . 131
7.5.3 Neighborhoods of the Central Path . . . . . . . . . . . 133
7.5.4 A Long-Step Path-Following Algorithm . . . . . . . . 136
7.5.5 Starting from an Infeasible Point . . . . . . . . . . . . 136
7.6 QP software . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
7.7 Additional Exercises . . . . . . . . . . . . . . . . . . . . . . . 137


CONTENTS 5


8 QP Models: Portfolio Optimization 139
8.1 Mean-Variance Optimization . . . . . . . . . . . . . . . . . . 139
8.1.1 Example . . . . . . . . . . . . . . . . . . . . . . . . . . 141
8.1.2 Large-Scale Portfolio Optimization . . . . . . . . . . . 146
8.1.3 The Black-Litterman Model . . . . . . . . . . . . . . . 149
8.1.4 Mean-Absolute Deviation to Estimate Risk . . . . . . 153
8.2 Maximizing the Sharpe Ratio . . . . . . . . . . . . . . . . . . 155
8.3 Returns-Based Style Analysis . . . . . . . . . . . . . . . . . . 158
8.4 Recovering Risk-Neural Probabilities from Options Prices . . 160
8.5 Additional Exercises . . . . . . . . . . . . . . . . . . . . . . . 164
8.6 Case Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166


9 Conic Optimization Tools 169
9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
9.2 Second-order cone programming: . . . . . . . . . . . . . . . . 169
9.2.1 Ellipsoidal Uncertainty for Linear Constraints . . . . . 171
9.2.2 Conversion of quadratic constraints into second-order
cone constraints . . . . . . . . . . . . . . . . . . . . . 173
9.3 Semidefinite programming: . . . . . . . . . . . . . . . . . . . 174
9.3.1 Ellipsoidal Uncertainty for Quadratic Constraints . . . 176
9.4 Algorithms and Software . . . . . . . . . . . . . . . . . . . . . 177


10 Conic Optimization Models in Finance 179
10.1 Tracking Error and Volatility Constraints . . . . . . . . . . . 179
10.2 Approximating Covariance Matrices . . . . . . . . . . . . . . 182
10.3 Recovering Risk-Neural Probabilities from Options Prices . . 185
10.4 Arbitrage Bounds for Forward Start Options . . . . . . . . . 187
10.4.1 A Semi-Static Hedge . . . . . . . . . . . . . . . . . . . 188


11 Integer Programming: Theory and Algorithms 193
11.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
11.2 Modeling Logical Conditions . . . . . . . . . . . . . . . . . . 194
11.3 Solving Mixed Integer Linear Programs . . . . . . . . . . . . 197
11.3.1 Linear Programming Relaxation . . . . . . . . . . . . 197
11.3.2 Branch and Bound . . . . . . . . . . . . . . . . . . . . 198
11.3.3 Cutting Planes . . . . . . . . . . . . . . . . . . . . . . 206
11.3.4 Branch and Cut . . . . . . . . . . . . . . . . . . . . . 210


12 IP Models: Constructing an Index Fund 213
12.1 Combinatorial Auctions . . . . . . . . . . . . . . . . . . . . . 213
12.2 The Lockbox Problem . . . . . . . . . . . . . . . . . . . . . . 214
12.3 Constructing an Index Fund . . . . . . . . . . . . . . . . . . . 217
12.3.1 A Large-Scale Deterministic Model . . . . . . . . . . . 218
12.3.2 A Linear Programming Model . . . . . . . . . . . . . 221
12.4 Portfolio Optimization with Minimum Transaction Levels . . 222
12.5 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
12.6 Case Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224


6 CONTENTS


13 Dynamic Programming Methods 225
13.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
13.1.1 Backward Recursion . . . . . . . . . . . . . . . . . . . 228
13.1.2 Forward Recursion . . . . . . . . . . . . . . . . . . . . 231
13.2 Abstraction of the Dynamic Programming Approach . . . . . 232
13.3 The Knapsack Problem. . . . . . . . . . . . . . . . . . . . . . 235
13.3.1 Dynamic Programming Formulation . . . . . . . . . . 235
13.3.2 An Alternative Formulation . . . . . . . . . . . . . . . 236
13.4 Stochastic Dynamic Programming . . . . . . . . . . . . . . . 237


14 DP Models: Option Pricing 239
14.1 A Model for American Options . . . . . . . . . . . . . . . . . 239
14.2 Binomial Lattice . . . . . . . . . . . . . . . . . . . . . . . . . 241
14.2.1 Specifying the parameters . . . . . . . . . . . . . . . . 242
14.2.2 Option Pricing . . . . . . . . . . . . . . . . . . . . . . 243


15 DP Models: Structuring Asset Backed Securities 247
15.1 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
15.2 Enumerating possible tranches . . . . . . . . . . . . . . . . . 251
15.3 A Dynamic Programming Approach . . . . . . . . . . . . . . 252
15.4 Case Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253


16 Stochastic Programming: Theory and Algorithms 255
16.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
16.2 Two Stage Problems with Recourse . . . . . . . . . . . . . . . 256
16.3 Multi Stage Problems . . . . . . . . . . . . . . . . . . . . . . 258
16.4 Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . 260
16.5 Scenario Generation . . . . . . . . . . . . . . . . . . . . . . . 263
16.5.1 Autoregressive model . . . . . . . . . . . . . . . . . . 263
16.5.2 Constructing scenario trees . . . . . . . . . . . . . . . 265


17 SP Models: Value-at-Risk 271
17.1 Risk Measures . . . . . . . . . . . . . . . . . . . . . . . . . . 271
17.2 Minimizing CVaR . . . . . . . . . . . . . . . . . . . . . . . . 274
17.3 Example: Bond Portfolio Optimization . . . . . . . . . . . . . 276


18 SP Models: Asset/Liability Management 279
18.1 Asset/Liability Management . . . . . . . . . . . . . . . . . . . 279
18.1.1 Corporate Debt Management . . . . . . . . . . . . . . 282
18.2 Synthetic Options . . . . . . . . . . . . . . . . . . . . . . . . 285
18.3 Case Study: Option Pricing with Transaction Costs . . . . . 288
18.3.1 The Standard Problem . . . . . . . . . . . . . . . . . . 289
18.3.2 Transaction Costs . . . . . . . . . . . . . . . . . . . . 290


19 Robust Optimization: Theory and Tools 293
19.1 Introduction to Robust Optimization . . . . . . . . . . . . . . 293
19.2 Uncertainty Sets . . . . . . . . . . . . . . . . . . . . . . . . . 294
19.3 Different Flavors of Robustness . . . . . . . . . . . . . . . . . 296


CONTENTS 7


19.3.1 Constraint Robustness . . . . . . . . . . . . . . . . . . 296
19.3.2 Objective Robustness . . . . . . . . . . . . . . . . . . 297
19.3.3 Relative Robustness . . . . . . . . . . . . . . . . . . . 299
19.3.4 Adjustable Robust Optimization . . . . . . . . . . . . 301
19.4 Tools and Strategies for Robust Optimization . . . . . . . . . 302
19.4.1 Sampling . . . . . . . . . . . . . . . . . . . . . . . . . 303
19.4.2 Conic Optimization . . . . . . . . . . . . . . . . . . . 303
19.4.3 Saddle-Point Characterizations . . . . . . . . . . . . . 305


20 Robust Optimization Models in Finance 307
20.1 Robust Multi-Period Portfolio Selection . . . . . . . . . . . . 307
20.2 Robust Profit Opportunities in Risky Portfolios . . . . . . . . 311
20.3 Robust Portfolio Selection . . . . . . . . . . . . . . . . . . . . 313
20.4 Relative Robustness in Portfolio Selection . . . . . . . . . . . 315
20.5 Moment Bounds for Option Prices . . . . . . . . . . . . . . . 317
20.6 Additional Exercises . . . . . . . . . . . . . . . . . . . . . . . 318


A Convexity 321


B Cones 323


C A Probability Primer 325


D The Revised Simplex Method 329


8 CONTENTS


## Chapter 1

# Introduction

Optimization is a branch of applied mathematics that derives its importance
both from the wide variety of its applications and from the availability of
efficient algorithms. Mathematically, it refers to the minimization (or maximization) of a given objective function of several decision variables that
satisfy functional constraints. A typical optimization model addresses the
allocation of scarce resources among possible alternative uses in order to
maximize an objective function such as total profit.
Decision variables, the objective function, and constraints are three essential elements of any optimization problem. Problems that lack constraints
are called unconstrained optimization problems, while others are often referred to as constrained optimization problems. Problems with no objective
functions are called feasibility problems. Some problems may have multiple
objective functions. These problems are often addressed by reducing them
to a single-objective optimization problem or a sequence of such problems.
If the decision variables in an optimization problem are restricted to
integers, or to a discrete set of possibilities, we have an integer or discrete
optimization problem. If there are no such restrictions on the variables, the
problem is a continuous optimization problem. Of course, some problems
may have a mixture of discrete and continuous variables. We continue with
a list of problem classes that we will encounter in this book.

#### 1.1 Optimization Problems


We start with a generic description of an optimization problem. Given a
function f (x) : IR [n] → IR and a set S ⊂ IR [n], the problem of finding an
x [∗] ∈ IR [n] that solves
minx f (x) (1.1)
s.t. x ∈ S

is called an optimization problem (OP). We refer to f as the objective function and to S as the feasible region. If S is empty, the problem is called
infeasible. If it is possible to find a sequence x [k] ∈ S such that f (x [k] ) →−∞
as k → +∞, then the problem is unbounded. If the problem is neither infeasible nor unbounded, then it is often possible to find a solution x [∗] ∈ S


9


10 CHAPTER 1. INTRODUCTION


that satisfies
f (x [∗] ) ≤ f (x), ∀x ∈ S.

Such an x [∗] is called a global minimizer of the problem (OP). If


f (x [∗] ) < f (x), ∀x ∈ S, x ̸= x [∗],

then x [∗] is a strict global minimizer. In other instances, we may only find an
x [∗] ∈ S that satisfies

f (x [∗] ) f (x), x S Bx [∗] (ε)
≤ ∀ ∈ ∩

for some ε > 0, where Bx [∗] (ε) is the open ball with radius ε centered at x [∗],
i.e.,
Bx [∗] (ε) = x : x x [∗] < ε .
{ ∥                   - ∥ }

Such an x [∗] is called a local minimizer of the problem (OP). A strict local
minimizer is defined similarly.
In most cases, the feasible set S is described explicitly using functional
constraints (equalities and inequalities). For example, S may be given as


S := x : gi(x) = 0, i and gi(x) 0, i,
{ ∈E ≥ ∈I}

where E and I are the index sets for equality and inequality constraints.
Then, our generic optimization problem takes the following form:


( ) minx f (x)
OP
gi(x) = 0, i (1.2)
∈E
gi(x) 0, i .
≥ ∈I

Many factors affect whether optimization problems can be solved efficiently. For example, the number n of decision variables, and the total number of constraints |E| + |I|, are generally good predictors of how difficult
it will be to solve a given optimization problem. Other factors are related
to the properties of the functions f and gi that define the problem. Problems with a linear objective function and linear constraints are easier, as are
problems with convex objective functions and convex feasible sets. For this
reason, instead of general purpose optimization algorithms, researchers have
developed different algorithms for problems with special characteristics. We
list the main types of optimization problems we will encounter. A more
complete list can be found, for example, on the Optimization Tree available
from http://www-fp.mcs.anl.gov/otc/Guide/OptWeb/.


1.1.1 Linear Programming


One of the most common and easiest optimization problems is linear optimization or linear programming (LP). It is the problem of optimizing a linear
objective function subject to linear equality and inequality constraints. This
corresponds to the case in where the functions f and gi are all linear. If
OP
either f or one of the functions gi is not linear, then the resulting problem
is a nonlinear programming (NLP) problem.


1.1. OPTIMIZATION PROBLEMS 11


The standard form of the LP is given below:


( ) minx c [T] x
LP
Ax = b (1.3)
x ≥ 0,

where A ∈ IR [m][×][n], b ∈ IR [m], c ∈ IR [n] are given, and x ∈ IR [n] is the variable
vector to be determined. In this book, a k-vector is also viewed as a k × 1
matrix. For an m × n matrix M, the notation M [T] denotes the transpose
matrix, namely the n×m matrix with entries Mij [T] [=][ M][ji][.] [As an example, in]
the above formulation c [T] is a 1 × n matrix and c [T] x is the 1 × 1 matrix with
�entry [�][n] j=1 [c][j][x][j][.] [The] [objective] [in] [(1.3)] [is] [to] [minimize] [the] [linear] [function]
n
j=1 [c][j][x][j][.]
As with OP, the problem LP is said to be feasible if its constraints are
consistent and it is called unbounded if there exists a sequence of feasible vectors {x [k] } such that c [T] x [k] →−∞. When LP is feasible but not unbounded
it has an optimal solution, i.e., a vector x that satisfies the constraints and
minimizes the objective value among all feasible vectors.
The best known (and most successful) methods for solving LPs are the
interior-point and simplex methods.


1.1.2 Quadratic Programming


A more general optimization problem is the quadratic optimization or the
quadratic programming (QP) problem, where the objective function is now
a quadratic function of the variables. The standard form QP is defined as
follows:
( ) minx 21 [x][T][ Qx][ +][ c][T][ x]
QP
Ax = b (1.4)
x ≥ 0,

where A ∈ IR [m][×][n], b ∈ IR [m], c ∈ IR [n], Q ∈ IR [n][×][n] are given, and x ∈ IR [n] .
Since x [T] Qx = [1] [one] [can] [assume] [without] [loss] [of] [generality]

2 [x][T][ (][Q][ +][ Q][T][ )][x][,]
that Q is symmetric, i.e. Qij = Qji.
The objective function of the problem QP is a convex function of x
when Q is a positive semidefinite matrix, i.e., when y [T] Qy ≥ 0 for all y
(see the Appendix for a discussion on convex functions). This condition is
equivalent to Q having only nonnegative eigenvalues. When this condition
is satisfied, the QP problem is a convex optimization problem and can be
solved in polynomial time using interior-point methods. Here we are referring
to a classical notion used to measure computational complexity. Polynomial
time algorithms are efficient in the sense that they always find an optimal
solution in an amount of time that is guaranteed to be at most a polynomial
function of the input size.


1.1.3 Conic Optimization


Another generalization of (LP) is obtained when the nonnegativity constraints x ≥ 0 are replaced by general conic inclusion constraints. This is


12 CHAPTER 1. INTRODUCTION


called a conic optimization (CO) problem. For this purpose, we consider
a closed convex cone C (see the Appendix for a brief discussion on cones)
in a finite-dimensional vector space X and the following conic optimization
problem:
( ) minx c [T] x
CO
Ax = b (1.5)
x ∈ C.

When X = IR [n] and C = IR [n] + [,] [this] [problem] [is] [the] [standard] [form] [LP.] [How-]
ever, much more general nonlinear optimization problems can also be formulated in this way. Furthermore, some of the most efficient and robust
algorithmic machinery developed for linear optimization problems can be
modified to solve these general optimization problems. Two important subclasses of conic optimization problems we will address are: (i) second-order
cone optimization, and (ii) semidefinite optimization. These correspond to
the cases when C is the second-order cone:



Cq := {x = (x1, x2, . . ., xn) ∈ IR [n] : x [2] 1 [≥] [x] 2 [2] [+][ . . .][ +][ x] n [2] [, x][1] [≥] [0][}][,]



and the cone of symmetric positive semidefinite matrices:













x11 x1n

     - · ·
... ... ...
xn1 xnn

     - · ·



n n T
 ∈ IR × : X = X, X is positive semidefinite



.








Cs :=



X =










When we work with the cone of positive semidefinite matrices, the standard
inner products used in c [T] x and Ax in (1.5) are replaced by an appropriate
inner product for the space of n-dimensional square matrices.



1.1.4 Integer Programming


Integer programs are optimization problems that require some or all of the
variables to take integer values. This restriction on the variables often makes
the problems very hard to solve. Therefore we will focus on integer linear
programs, which have a linear objective function and linear constraints. A
pure integer linear program is given by:

( ) minx c [T] x
ILP
Ax ≥ b (1.6)
x ≥ 0 and integral,

where A ∈ IR [m][×][n], b ∈ IR [m], c ∈ IR [n] are given, and x ∈ IN [n] is the variable
vector to be determined.
An important case occurs when the variables xj represent binary decision
variables, that is x ∈{0, 1} [n] . The problem is then called a 0–1 linear
program.
When there are both continuous variables and integer constrained variables, the problem is called a mixed integer linear program:



( ) minx c [T] x
MILP
Ax ≥ b
x ≥ 0
xj IN for j = 1, . . ., p.
∈



(1.7)


1.2. OPTIMIZATION WITH DATA UNCERTAINTY 13


where A, b, c are given data and the integer p (with 1 ≤ p < n) is also part
of the input.


1.1.5 Dynamic Programming


Dynamic programming refers to a computational method involving recurrence relations. This technique was developed by Richard Bellman in the
early 1950’s. It arose from studying programming problems in which changes
over time were important, thus the name “dynamic programming”. However, the technique can also be applied when time is not a relevant factor
in the problem. The idea is to divide the problem into “stages” in order to
perform the optimization recursively. It is possible to incorporate stochastic
elements into the recursion.

#### 1.2 Optimization with Data Uncertainty


In all the problem classes we discussed so far (except dynamic programming),
we made the implicit assumption that the data of the problem, namely the
parameters such as Q, A, b and c in QP, are all known. This is not always the
case. Often, the problem parameters correspond to quantities that will only
be realized in the future, or cannot be known exactly at the time the problem
must be formulated and solved. Such situations are especially common in
models involving financial quantities such as returns on investments, risks,
etc. We will discuss two fundamentally different approaches that address
optimization with data uncertainty. Stochastic programming is an approach
used when the data uncertainty is random and can be explained by some
probability distribution. Robust optimization is used when one wants a
solution that behaves well in all possible realizations of the uncertain data.
These two alternative approaches are not problem classes (as in LP, QP,
etc.) but rather modeling techniques for addressing data uncertainty.


1.2.1 Stochastic Programming


The term stochastic programming refers to an optimization problem in which
some problem data are random. The underlying optimization problem might
be a linear program, an integer program, or a nonlinear program. An important case is that of stochastic linear programs.
A stochastic program with recourse arises when some of the decisions
(recourse actions) can be taken after the outcomes of some (or all) random events have become known. For example, a two-stage stochastic linear
program with recourse can be written as follows:



maxx a [T] x + E[maxy(ω) c(ω) [T] y(ω)]
Ax = b
B(ω)x + C(ω)y(ω) = d(ω)
x ≥ 0, y(ω) ≥ 0,



(1.8)



where the first-stage decisions are represented by vector x and the secondstage decisions by vector y(ω), which depend on the realization of a random


14 CHAPTER 1. INTRODUCTION


event ω. A and b define deterministic constraints on the first-stage decisions x, whereas B(ω), C(ω), and d(ω) define stochastic linear constraints
linking the recourse decisions y(ω) to the first-stage decisions. The objective function contains a deterministic term a [T] x and the expectation of the
second-stage objective c(ω) [T] y(ω) taken over all realization of the random
event ω.
Note that, once the first-stage decisions x have been made and the random event ω has been realized, one can compute the optimal second-stage
decisions by solving the following linear program:


f (x, ω) = max c(ω) [T] y(ω)
C(ω)y(ω) = d(ω) − B(ω)x (1.9)
y(ω) ≥ 0,

Let f (x) = E[f (x, ω)] denote the expected value of the optimal value of this
problem. Then, the two-stage stochastic linear program becomes


max a [T] x + f (x)
Ax = b (1.10)
x ≥ 0,

Thus, if the (possibly nonlinear) function f (x) is known, the problem reduces to a nonlinear programming problem. When the data c(ω), B(ω),
C(ω), and d(ω) are described by finite distributions, one can show that f is
piecewise linear and concave. When the data are described by probability
densities that are absolutely continuous and have finite second moments,
one can show that f is differentiable and concave. In both cases, we have
a convex optimization problem with linear constraints for which specialized
algorithms are available.


1.2.2 Robust Optimization


Robust optimization refers to the modeling of optimization problems with
data uncertainty to obtain a solution that is guaranteed to be “good” for
all possible realizations of the uncertain parameters. In this sense, this
approach departs from the randomness assumption used in stochastic optimization for uncertain parameters and gives the same importance to all
possible realizations. Uncertainty in the parameters is described through uncertainty sets that contain all (or most) possible values that can be realized
by the uncertain parameters.
There are different definitions and interpretations of robustness and the
resulting models differ accordingly. One important concept is constraint
robustness, often called model robustness in the literature. This refers to
solutions that remain feasible for all possible values of the uncertain inputs.
This type of solution is required in several engineering applications. Here
is an example adapted from Ben-Tal and Nemirovski. Consider a multiphase engineering process (a chemical distillation process, for example) and
a related process optimization problem that includes balance constraints
(materials entering a phase of the process cannot exceed what is used in


1.3. FINANCIAL MATHEMATICS 15


that phase plus what is left over for the next phase). The quantities of the
end products of a particular phase may depend on external, uncontrollable
factors and are therefore uncertain. However, no matter what the values of
these uncontrollable factors are, the balance constraints must be satisfied.
Therefore, the solution must be constraint robust with respect to the uncertainties of the problem. Here is a mathematical model for finding constraint
robust solutions: Consider an optimization problem of the form:


(OPuc) minx f (x) (1.11)
G(x, p) ∈ K.

Here, x are the decision variables, f is the (certain) objective function, G
and K are the structural elements of the constraints that are assumed to
be certain and p are the uncertain parameters of the problem. Consider an
uncertainty set U that contains all possible values of the uncertain parameters p. Then, a constraint robust optimal solution can be found by solving
the following problem:

(CROP [)] minx f (x) (1.12)
G(x, p) ∈ K, ∀p ∈U.

A related concept is objective robustness, which occurs when uncertain
parameters appear in the objective function. This is often referred to as
solution robustness in the literature. Such robust solutions must remain
close to optimal for all possible realizations of the uncertain parameters.
Consider an optimization problem of the form:


(OPuo) minx f (x, p) (1.13)
x ∈ S.

Here, S is the (certain) feasible set and f is the objective function that depends on uncertain parameters p. Assume as above that U is the uncertainty
set that contains all possible values of the uncertain parameters p. Then,
an objective robust solution is obtained by solving:


( ) minx S maxp f (x, p). (1.14)
OROP ∈ ∈U

Note that objective robustness is a special case of constraint robustness.
Indeed, by introducing a new variable t (to be minimized) into uo and
OP
imposing the constraint f (x, p) t, we get an equivalent problem to uo.
≤ OP
The constraint robust formulation of the resulting problem is equivalent to
OROP.
Constraint robustness and objective robustness are concepts that arise
in conservative decision making and are not always appropriate for optimization problems with data uncertainty.

#### 1.3 Financial Mathematics


Modern finance has become increasingly technical, requiring the use of sophisticated mathematical tools in both research and practice. Many find the


16 CHAPTER 1. INTRODUCTION


roots of this trend in the portfolio selection models and methods described
by Markowitz in the 1950’s and the option pricing formulas developed by
Black, Scholes, and Merton in the late 1960’s. For the enormous effect these
works produced on modern financial practice, Markowitz was awarded the
Nobel prize in Economics in 1990, while Scholes and Merton won the Nobel
prize in Economics in 1997.
Below, we introduce topics in finance that are especially suited for mathematical analysis and involve sophisticated tools from mathematical sciences.


1.3.1 Portfolio Selection and Asset Allocation


The theory of optimal selection of portfolios was developed by Harry Markowitz
in the 1950’s. His work formalized the diversification principle in portfolio
selection and, as mentioned above, earned him the 1990 Nobel prize for
Economics. Here we give a brief description of the model and relate it to
QPs.
Consider an investor who has a certain amount of money to be invested
in a number of different securities (stocks, bonds, etc.) with random returns. For each security i = 1, . . ., n, estimates of its expected return µi
and variance σi [2] [are given.] [Furthermore, for any two securities][ i][ and][ j][, their]
correlation coefficient ρij is also assumed to be known. If we represent the
proportion of the total funds invested in security i by xi, one can compute the
expected return and the variance of the resulting portfolio x = (x1, . . ., xn)
as follows:
E[x] = x1µ1 + . . . + xnµn = µ [T] x,


and

     V ar[x] = ρijσiσjxixj = x [T] Qx

i,j


where ρii 1, Qij = ρijσiσj, and µ = (µ1, . . ., µn).
≡
The portfolio vector x must satisfy [�] i [x][i] [=] [1] [and] [there] [may] [or] [may]
not be additional feasibility constraints. A feasible portfolio x is called
efficient if it has the maximal expected return among all portfolios with the
same variance, or alternatively, if it has the minimum variance among all
portfolios that have at least a certain expected return. The collection of
efficient portfolios form the efficient frontier of the portfolio universe.
Markowitz’ portfolio optimization problem, also called the mean-variance
optimization (MVO) problem, can be formulated in three different but equivalent ways. One formulation results in the problem of finding a minimum
variance portfolio of the securities 1 to n that yields at least a target value
R of expected return. Mathematically, this formulation produces a convex
quadratic programming problem:



minx x [T] Qx
e [T] x = 1
µ [T] x ≥ R
x ≥ 0,



(1.15)


1.3. FINANCIAL MATHEMATICS 17


where e is an n-dimensional vector all of which components are equal to
1. The first constraint indicates that the proportions xi should sum to 1.
The second constraint indicates that the expected return is no less than the
target value and, as we discussed above, the objective function corresponds
to the total variance of the portfolio. Nonnegativity constraints on xi are
introduced to rule out short sales (selling a security that you do not have).
Note that the matrix Q is positive semidefinite since x [T] Qx, the variance of
the portfolio, must be nonnegative for every portfolio (feasible or not) x.


As an alternative to problem (1.15), we may choose to maximize the
expected return of a portfolio while limiting the variance of its return. Or,
we can maximize a risk-adjusted expected return which is defined as the
expected return minus a multiple of the variance. These two formulations
are essentially equivalent to (1.15) as we will see in Chapter 8.


The model (1.15) is rather versatile. For example, if short sales are permitted on some or all of the securities, then this can be incorporated into
the model simply by removing the nonnegativity constraint on the corresponding variables. If regulations or investor preferences limit the amount
of investment in a subset of the securities, the model can be augmented with
a linear constraint to reflect such a limit. In principle, any linear constraint
can be added to the model without making it significantly harder to solve.


Asset allocation problems have the same mathematical structure as portfolio selection problems. In these problems the objective is not to choose
a portfolio of stocks (or other securities) but to determine the optimal investment among a set of asset classes. Examples of asset classes are large
capitalization stocks, small capitalization stocks, foreign stocks, government
bonds, corporate bonds, etc. There are many mutual funds focusing on
specific asset classes and one can therefore conveniently invest in these asset classes by purchasing the relevant mutual funds. After estimating the
expected returns, variances, and covariances for different asset classes, one
can formulate a QP identical to (1.15) and obtain efficient portfolios of these
asset classes.


A different strategy for portfolio selection is to try to mirror the movements of a broad market population using a significantly smaller number of
securities. Such a portfolio is called an index fund. No effort is made to
identify mispriced securities. The assumption is that the market is efficient
and therefore no superior risk-adjusted returns can be achieved by stock
picking strategies since the stock prices reflect all the information available
in the marketplace. Whereas actively managed funds incur transaction costs
which reduce their overall performance, index funds are not actively traded
and incur low management fees. They are typical of a passive management
strategy. How do investment companies construct index funds? There are
numerous ways of doing this. One way is to solve a clustering problem where
similar stocks have one representative in the index fund. This naturally leads
to an integer programming formulation.


18 CHAPTER 1. INTRODUCTION


1.3.2 Pricing and Hedging of Options


We first start with a description of some of the well-known financial options.
A European call option is a contract with the following conditions:


  - At a prescribed time in the future, known as the expiration date, the
holder of the option has the right, but not the obligation to


  - purchase a prescribed asset, known as the underlying, for a

  - prescribed amount, known as the strike price or exercise price.

A European put option is similar, except that it confers the right to sell
the underlying asset (instead of buying it for a call option). An American
option is like a European option, but it can be exercised anytime before the
expiration date.
Since the payoff from an option depends on the value of the underlying
security, its price is also related to the current value and expected behavior
of this underlying security. To find the fair value of an option, we need
to solve a pricing problem. When there is a good model for the stochastic
behavior of the underlying security, the option pricing problem can be solved
using sophisticated mathematical techniques.
Option pricing problems are often solved using the following strategy. We
try to determine a portfolio of assets with known prices which, if updated
properly through time, will produce the same payoff as the option. Since the
portfolio and the option will have the same eventual payoffs, we conclude
that they must have the same value today (otherwise, there is arbitrage)
and we can therefore obtain the price of the option. A portfolio of other
assets that produces the same payoff as a given financial instrument is called
a replicating portfolio (or a hedge) for that instrument. Finding the right
portfolio, of course, is not always easy and leads to a replication (or hedging)
problem.
Let us consider a simple example to illustrate these ideas. Let us assume
that one share of stock XYZ is currently valued at $40. The price of XYZ
a month from today is random. Assume that its value will either double or
halve with equal probabilities.



S0=$40 [���] HHH*j



80=S1(u)


20=S1(d)



Today, we purchase a European call option to buy one share of XYZ stock
for $50 a month from today. What is the fair price of this option?
Let us assume that we can borrow or lend money with no interest between today and next month, and that we can buy or sell any amount of the
XYZ stock without any commissions, etc. These are part of the “frictionless
market” assumptions we will address later. Further assume that XYZ will
not pay any dividends within the next month.
To solve the option pricing problem, we consider the following hedging
problem: Can we form a portfolio of the underlying stock (bought or sold)


1.3. FINANCIAL MATHEMATICS 19


and cash (borrowed or lent) today, such that the payoff from the portfolio at
the expiration date of the option will match the payoff of the option? Note
that the option payoff will be $30 if the price of the stock goes up and $0
if it goes down. Assume this portfolio has ∆shares of XYZ and $B cash.
This portfolio would be worth 40∆+B today. Next month, payoffs for this
portfolio will be:



P0=40∆+B [���] HHH*j


Let us choose ∆and B such that


80∆+ B = 30


20∆+ B = 0,



80∆+B=P1(u)


20∆+B=P1(d)



so that the portfolio replicates the payoff of the option at the expiration
date. This gives ∆= [1] [B] [=] [which] [is] [the] [hedge] [we] [were] [looking]

2 [and] [−][10,]
for. This portfolio is worth P0 = 40∆+ B =$10 today, therefore, the fair
price of the option must also be $10.


1.3.3 Risk Management


Risk is inherent in most economic activities. This is especially true of financial activities where results of decisions made today may have many
possible different outcomes depending on future events. Since companies
cannot usually insure themselves completely against risk, they have to manage it. This is a hard task even with the support of advanced mathematical
techniques. Poor risk management led to several spectacular failures in the
financial industry during the 1990’s (e.g., Barings Bank, Long Term Capital
Management, Orange County).
A coherent approach to risk management requires quantitative risk measures that adequately reflect the vulnerabilities of a company. Examples of
risk measures include portfolio variance as in the Markowitz MVO model,
the Value-at-Risk (VaR) and the expected shortfall (also known as conditional Value-at-Risk, or CVaR)). Furthermore, risk control techniques need
to be developed and implemented to adapt to rapid changes in the values
of these risk measures. Government regulators already mandate that financial institutions control their holdings in certain ways and place margin
requirements for “risky” positions.
Optimization problems encountered in financial risk management often
take the following form. Optimize a performance measure (such as expected
investment return) subject to the usual operating constraints and the constraint that a particular risk measure for the company’s financial holdings
does not exceed a prescribed amount. Mathematically, we may have the
following problem:
maxx µ [T] x
RM[x] γ
≤ (1.16)
e [T] x = 1
x ≥ 0.


20 CHAPTER 1. INTRODUCTION


As in the Markowitz MVO model, xi represent the proportion of the total
funds invested in security. The objective is the expected portfolio return and
µ is the expected return vector for the different securities. RM[x] denotes
the value of a particular risk measure for portfolio x and γ is the prescribed
upper limit on this measure. Since RM[x] is generally a nonlinear function
of x, (1.16) is a nonlinear programming problem. Alternatively, we can
minimize the risk measure while constraining the expected return of the
portfolio to achieve or exceed a given target value R. This would produce a
problem very similar to (1.15).


1.3.4 Asset/Liability Management


How should a financial institution manage its assets and liabilities? A static
mean-variance optimizing model, such as the one we discussed for asset allocation, fails to incorporate the multiple liabilities faced by financial institutions. Furthermore, it penalizes returns both above and below the mean.
A multi-period model that emphasizes the need to meet liabilities in each
period for a finite (or possibly infinite) horizon is often required. Since liabilities and asset returns usually have random components, their optimal
management requires tools of “Optimization under Uncertainty” and most
notably, stochastic programming approaches.
Let Lt be the liability of the company in period t for t = 1, . . ., T . Here,
we assume that the liabilities Lt are random with known distributions. A
typical problem to solve in asset/liability management is to determine which
assets (and in what quantities) the company should hold in each period
to maximize its expected wealth at the end of period T. We can further
assume that the asset classes the company can choose from have random
returns (again, with known distributions) denoted by Rit for asset class i in
period t. Since the company can make the holding decisions for each period
after observing the asset returns and liabilities in the previous periods, the
resulting problem can be cast as a stochastic program with recourse:

maxx   - E[ [�] i [x][i,T] []]
i [(1 +][ R][it][)][x][i,t][−][1] i [x][i,t] = Lt, t = 1, . . ., T (1.17)

[−] [�]
xi,t 0 i, t.
≥ ∀

The objective function represents the expected total wealth at the end of
the last period. The constraints indicate that the surplus left after liability
Lt is covered will be invested as follows: xi,t invested in asset class i. In this
formulation, xi,0 are the fixed, and possibly nonzero initial positions in the
different asset classes.


## Chapter 2

# Linear Programming: Theory and Algorithms

#### 2.1 The Linear Programming Problem

One of the most common and fundamental optimization problems is the linear optimization, or linear programming (LP) problem. LP is the problem
of optimizing a linear objective function subject to linear equality and inequality constraints. A generic linear optimization problem has the following
form:

minx c [T] x
a [T] i [x] = bi, i ∈E (2.1)
a [T] i [x] ≥ bi, i ∈I,

where E and I are the index sets for equality and inequality constraints,
respectively. Linear programming is arguably the best known and the most
frequently solved optimization problem. It owes its fame mostly to its great
success; real world problems coming from as diverse disciplines as sociology,
finance, transportation, economics, production planning, and airline crew
scheduling have been formulated and successfully solved as LPs.
For algorithmic purposes, it is often desirable to have the problems structured in a particular way. Since the development of the simplex method for
LPs the following form has been a popular standard and is called the standard form LP:


minx c [T] x
Ax = b (2.2)
x ≥ 0.

Here A ∈ IR [m][×][n], b ∈ IR [m], c ∈ IR [n] are given, and x ∈ IR [n] is the variable
vector to be determined as the solution of the problem.
The standard form is not restrictive: Inequalities other than nonnegativity constraints can be rewritten as equalities after the introduction of a
so-called slack or surplus variable that is restricted to be nonnegative. For


21


22CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS



example,
min x1 x2

         -         2x1 + x2 12
≤
x1 + 2x2 9
≤
x1 0, x2 0
≥ ≥

can be rewritten as



min x1 x2

  -   2x1 + x2 + x3 = 12
x1 + 2x2 + x4 = 9
x1 0, x2 0, x3 0, x4 0.
≥ ≥ ≥ ≥



(2.3)


(2.4)



Variables that are unrestricted in sign can be expressed as the difference of
two new nonnegative variables. Maximization problems can be written as
minimization problems by multiplying the objective function by a negative
constant. Simple transformations are available to rewrite any given LP
in the standard form above. Therefore, in the rest of our theoretical and
algorithmic discussion we assume that the LP is in the standard form.



Exercise 2.1 Write the following linear program in standard form.


min x2
x1 + x2 1
≥
x1 x2 0

     - ≤
x1, x2 unrestricted in sign.


Answer:


After writing xi = yi zi, i = 1, 2 with yi 0 and zi 0 and introducing

       - ≥ ≥
surplus variable s1 for the first constraint and slack variable s2 for the second
constraint we obtain:


min y2 z2

          y1 z1 + y2 z2 s1 = 1

     -      -      y1 z1 y2 + z2 + s2 = 0

     -      y1 0, z1 0, y2 0, z2 0, s1 0, s2 0.
≥ ≥ ≥ ≥ ≥ ≥


Exercise 2.2 Write the following linear program in standard form.


max 4x1 + x2 x3

       x1 + 3x3 6
≤
3x1 + x2 + 3x3 9
≥
x1 0, x2 0, x3 unrestricted in sign.
≥ ≥

Recall the following definitions from the Chapter 1: The LP (2.2) is
said to be feasible if its constraints are consistent and it is called unbounded
if there exists a sequence of feasible vectors {x [k] } such that c [T] x [k] →−∞.
When we talk about a solution (without any qualifiers) to (2.2) we mean
any candidate vector x ∈ IR [n] . A feasible solution is one that satisfies the
constraints, and an optimal solution is a vector x that satisfies the constraints
and minimizes the objective value among all feasible vectors. When LP is
feasible but not unbounded it has an optimal solution.


2.2. DUALITY 23


Exercise 2.3
(a) Write a 2-variable linear program that is unbounded.
(b) Write a 2-variable linear program that is infeasible.


Exercise 2.4 Draw the feasible region of the following 2-variable linear
program.


max 2x1 x2

     x1 + x2 1
≥
x1 x2 0

     - ≤
3x1 + x2 6
≤
x1 0, x2 0.
≥ ≥

Determine the optimal solution to this problem by inspection.


The most important questions we will address in this chapter are the
following: How do we recognize an optimal solution and how do we find such
solutions? One of the most important tools in optimization to answer these
questions is the notion of a dual problem associated with the LP problem
(2.2). We describe the dual problem in the next subsection.

#### 2.2 Duality


Consider the standard form LP in (2.4) above. Here are a few alternative
feasible solutions:




[9] [15]

2 [,] 2



(x1, x2, x3, x4) = (0, [9]



Objective value =
2 [,][ 0)] - 2 [9]



2 2 2

(x1, x2, x3, x4) = (6, 0, 0, 3) Objective value = 6
                     
(x1, x2, x3, x4) = (5, 2, 0, 0) Objective value = 7
                     


Since we are minimizing, the last solution is the best among the three feasible
solutions we found, but is it the optimal solution? We can make such a claim
if we can, somehow, show that there is no feasible solution with a smaller
objective value.
Note that the constraints provide some bounds on the value of the objective function. For example, for any feasible solution, we must have


x1 x2 2x1 x2 x3 = 12

      -      - ≥−      -      -      
using the first constraint of the problem. The inequality above must hold
for all feasible solutions since xi’s are all nonnegative and the coefficient
of each variable on the LHS are at least as large as the coefficient of the
corresponding variable on the RHS. We can do better using the second
constraint:
x1 x2 x1 2x2 x4 = 9

      -       - ≥−       -       -       
and even better by adding a negative third of each constraint:



x1 x2 x1 x2

- - ≥ - - - [1] 3



3 [1] [(][x][1][ + 2][x][2][ +][ x][4][) =][ −] 3 [1]



3 [x][4]



=

 - [1] 3




[1] 3 [(2][x][1][ +][ x][2][ +][ x][3][)][ −] [1] 3




[1] 3 [x][3][ −] [1] 3



3 [(12 + 9) =][ −][7][.]


24CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


This last inequality indicates that for any feasible solution, the objective
function value cannot be smaller than -7. Since we already found a feasible solution achieving this bound, we conclude that this solution, namely
(x1, x2, x3, x4) = (5, 2, 0, 0) must be an optimal solution of the problem.
This process illustrates the following strategy: If we find a feasible solution to the LP problem, and a bound on the optimal value of problem such
that the bound and the objective value of the feasible solution coincide, then
we can conclude that our feasible solution is an optimal solution. We will
comment on this strategy shortly. Before that, though, we formalize our
approach for finding a bound on the optimal objective value.
Our strategy was to find a linear combination of the constraints, say with
multipliers y1 and y2 for the first and second constraint respectively, such
that the combined coefficient of each variable forms a lower bound on the
objective coefficient of that variable. Namely, we tried to choose multipliers
y1 and y2 associated with constraints 1 and 2 such that


y1(2x1+x2 +x3)+y2(x1+2x2 +x4) = (2y1+y2)x1+(y1 +2y2)x2+y1x3+y2x4


provides a lower bound on the optimal objective value. Since xi’s must be
nonnegative, the expression above would necessarily give a lower bound if
the coefficient of each xi is less than or equal to the corresponding objective
function coefficient, or if:


2y1 + y2 1
≤            y1 + 2y2 1
≤            y1 0
≤
y2 0.
≤

Note that the objective coefficients of x3 and x4 are zero. Naturally, to
obtain the largest possible lower bound, we would like to find y1 and y2 that
achieve the maximum combination of the right-hand-side values:


max 12y1 + 9y2.


This process results in a linear programming problem that is strongly related
to the LP we are solving. We want to



max 12y1 + 9y2
2y1 + y2 1
≤       y1 + 2y2 1
≤       y1 0
≤
y2 0.
≤



(2.5)



This problem is called the dual of the original problem we considered. The
original LP in (2.2) is often called the primal problem. For a generic primal
LP problem in standard form (2.2) the corresponding dual problem can be
written as follows:

(LD) maxy b [T] y (2.6)
A [T] y ≤ c,


2.2. DUALITY 25


where y ∈ IR [m] . Rewriting this problem with explicit dual slacks, we obtain
the standard form dual linear programming problem:


( ) maxy,s b [T] y
LD
A [T] y + s = c (2.7)
s ≥ 0,

where s ∈ IR [n] .


Exercise 2.5 Consider the following LP:


min 2x1 + 3x2
x1 + x2 5
≥
x1 1
≥
x2 2.
≥

Prove that x [∗] = (3, 2) is the optimal solution by showing that the objective
value of any feasible solution is at least 12.


Next, we make some observations about the relationship between solutions of the primal and dual LPs. The objective value of any primal feasible
solution is at least as large as the objective value of any feasible dual solution. This fact is known as the weak duality theorem:


Theorem 2.1 (Weak Duality Theorem) Let x be any feasible solution
to the primal LP (2.2) and y be any feasible solution to the dual LP (2.6).
Then
c [T] x ≥ b [T] y.


Proof:
Since x ≥ 0 and c − A [T] y ≥ 0, the inner product of these two vectors must
be nonnegative:


(c − A [T] y) [T] x = c [T] x − y [T] Ax = c [T] x − y [T] b ≥ 0.


The quantity c [T] x − y [T] b is often called the duality gap. The following
three results are immediate consequences of the weak duality theorem.


Corollary 2.1 If the primal LP is unbounded, then the dual LP must be
infeasible.


Corollary 2.2 If the dual LP is unbounded, then the primal LP must be
infeasible.


Corollary 2.3 If x is feasible for the primal LP, y is feasible for the dual
LP, and c [T] x = b [T] y, then x must be optimal for the primal LP and y must
be optimal for the dual LP.


26CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


Exercise 2.6 Show that the dual of the linear program


minx c [T] x
Ax ≥ b
x ≥ 0

is the linear program
maxy b [T] y
A [T] y ≤ c
y ≥ 0.

Exercise 2.7 We say that two linear programming problems are equivalent if one can be obtained from the other by (i) multiplying the objective
function by -1 and changing it from min to max, or max to min, and/or (ii)
multiplying some or all constraints by -1. For example, min{c [T] x : Ax ≥ b}
and max{−c [T] x : −Ax ≤−b} are equivalent problems. Find a linear program which is equivalent to its own dual.


Exercise 2.8 Give an example of a linear program such that it and its dual
are both infeasible.


Exercise 2.9 For the following pair of primal-dual problems, determine
whether the listed solutions are optimal.



min 2x1 + 3x2 max 30y1 + 10y2

            2x1 + 3x2 30 2y1 + y2 + y3 2
≤       - ≤
x1 + 2x2 10 3y1 + 2y2 y3 3
≥       -       - ≤
x1 x2 0 y1, y2, y3 0.

   - ≥ ≥
x1, x2 0
≥



(a) x1 = 10, x2 = [10] 3



(a) x1 = 10, x2 = 3 [;] [y][1] [= 0][,] [y][2] [= 1][,] [y][3] [= 1][.]

(b) x1 = 20, x2 = 10; y1 = 1, y2 = 4, y3 = 0.
           (c) x1 = [10] 3 [,] [x][2] [=] [10] 3 [;] [y][1] [= 0][,] [y][2] [=] 3 [5] [,] [y][3] [=] [1] 3 [.]



3 [,] [x][2] [=] [10] 3



3 [;] [y][1] [= 0][,] [y][2] [=] 3 [5]



3 [5] [,] [y][3] [=] [1] 3



3 [.]


#### 2.3 Optimality Conditions

Corollary 2.3 in the previous section identified a sufficient condition for optimality of a primal-dual pair of feasible solutions, namely that their objective
values coincide. One natural question to ask is whether this is a necessary
condition. The answer is yes, as we illustrate next.


Theorem 2.2 (Strong Duality Theorem) If the primal (dual) problem
has an optimal solution x (y), then the dual (primal) has an optimal solution
y (x) such that c [T] x = b [T] y.


The reader can find a proof of this result in most standard linear programming textbooks (see Chv´atal [19] for example). A consequence of the Strong
Duality Theorem is that, if both the primal LP problem and the dual LP
have feasible solutions then they both have optimal solutions and for any primal optimal solution x and dual optimal solution y we have that c [T] x = b [T] y.


2.3. OPTIMALITY CONDITIONS 27


The strong duality theorem provides us with conditions to identify optimal solutions (called optimality conditions): x ∈ IR [n] is an optimal solution
of (2.2) if and only if

1. x is primal feasible: Ax = b, x ≥ 0, and there exists a y ∈ IR [m] such
that

2. y is dual feasible: A [T] y ≤ c, and

3. there is no duality gap: c [T] x = b [T] y.


Further analyzing the last condition above, we can obtain an alternative
set of optimality conditions. Recall from the proof of the weak duality
theorem that c [T] x − b [T] y = (c − A [T] y) [T] x ≥ 0 for any feasible primal-dual
pair of solutions, since it is given as an inner product of two nonnegative
vectors. This inner product is 0 (c [T] x = b [T] y) if and only if the following
statement holds: For each i = 1, . . ., n, either xi or (c A [T] y)i = si is zero.
                        This equivalence is easy to see. All the terms in the summation on the RHS
of the following equation are nonnegative:



0 = (c − A [T] y) [T] x =



�n

(c A [T] y)ixi
  i=1



Since the sum is zero, each term must be zero. Thus we found an alternative
set of optimality conditions: x ∈ IR [n] is an optimal solution of (2.2) if and
only if

1. x is primal feasible: Ax = b, x ≥ 0, and there exists a y ∈ IR [m] such
that

2. y is dual feasible: s := c − A [T] y ≥ 0, and

3. complementary slackness: for each i = 1, . . ., n we have xisi = 0.


Exercise 2.10 Consider the linear program


min 5x1 + 12x2 + 4x3
x1 + 2x2 + x3 = 10
2x1 x2 + 3x3 = 8

         x1 0, x2 0, x3 0.
≥ ≥ ≥

You are given the information that x2 and x3 are positive in the optimal
solution. Use the complementary slackness conditions to find the optimal
dual solution.


Exercise 2.11 Consider the following linear programming problem:


max 6x1 + 5x2 + 4x3 + 5x4 + 6x5
x1 + x2 + x3 + x4 + x5 3
≤
5x1 + 4x2 + 3x3 + 2x4 + x5 14
≤

x1 0, x2 0, x3 0, x4 0, x5 0
≥ ≥ ≥ ≥ ≥

Solve this problem using the following strategy:


28CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


a) Find the dual of the above LP. The dual has only two variables. Solve
the dual by inspection after drawing a graph of the feasible set.


b) Now using the optimal solution to the dual problem, and complementary slackness conditions, determine which primal constraints are
active, and which primal variables must be zero at an optimal solution.
Using this information determine the optimal solution to the primal
problem.


Exercise 2.12 Using the optimality conditions for


minx c [T] x
Ax = b
x ≥ 0,

deduce that the optimality conditions for


maxx c [T] x
Ax ≤ b
x ≥ 0

are Ax ≤ b, x ≥ 0 and there exists y such that A [T] y ≥ c, y ≥ 0, c [T] x = b [T] y.

Exercise 2.13 Consider the following investment problem over T years,
where the objective is to maximize the value of the investments in year
T . We assume a perfect capital market with the same annual lending and
borrowing rate r - 0 each year. We also assume that exogenous investment
funds bt are available in year t, for t = 1, . . ., T . Let n be the number of
possible investments. We assume that each investment can be undertaken
fractionally (between 0 and 1). Let atj denote the cash flow associated
with investment j in year t. Let cj be the value of investment j in year T
(including all cash flows subsequent to year T discounted at the interest rate
r).
The linear program that maximizes the value of the investments in year
T is the following. Denote by xj the fraction of investment j undertaken,
and let yt be the amount borrowed (if negative) or lent (if positive) in year
t. max nj=1 [c][j][x][j] [+][ y][T]
j=1 [a][1][j][x][j] [+][ y][1] b1

      - [�][n] ≤
j=1 [a][tj][x][j] bt for t = 2, . . ., T

   - [�][n] [−] [(1 +][ r][)][y][t][−][1][ +][ y][t] ≤
0 xj 1 for j = 1, . . ., n.
≤ ≤

(i) Write the dual of the above linear program.
(ii) Solve the dual linear program found in (i). [Hint: Note that some of
the dual variables can be computed by backward substitution.]
(iii) Write the complementary slackness conditions.
(iv) Deduce that the first T constraints in the primal linear program
hold as equalities.
(v) Use the complementary slackness conditions to show that the solution
obtained by setting xj = 1 if cj + [�][T] t=1 [(1] [+] [r][)][T][ −][t][a][tj] [>] [0,] [and] [x][j] [=] [0]
otherwise, is an optimal solution.


2.4. THE SIMPLEX METHOD 29


(vi) Conclude that the above investment problem always has an optimal
solution where each investment is either undertaken completely or not at
all.

#### 2.4 The Simplex Method


The best known and most successful methods for solving LPs are interiorpoint methods (IPMs) and the simplex method. We discuss the simplex
method here and postpone our discussion IPMs till we study quadratic programming problems, as IPMs are also applicable to quadratic programs and
other more general classes of optimization problems.
We introduce the essential elements of the simplex method using a simple
bond portfolio selection problem.


Example 2.1 A bond portfolio manager has $100,000 to allocate to two
different bonds; one corporate and one government bond. The corporate bond
has a yield of 4%, a maturity of 3 years and an A rating from a rating agency
that is translated into a numerical rating of 2 for computational purposes. In
contrast, the government bond has a yield of 3%, a maturity of 4 years and
rating of Aaa with the corresponding numerical rating of 1 (lower numerical
ratings correspond to higher quality bonds). The portfolio manager would like
to allocate her funds so that the average rating for the portfolio is no worse
than Aa (numerical equivalent 1.5) and average maturity of the portfolio is
at most 3.6 years. Any amount not invested in the two bonds will be kept in
a cash account that is assumed to earn no interest for simplicity and does not
contribute to the average rating or maturity computations [1] . How should the
manager allocate her funds between these two bonds to achieve her objective
of maximizing the yield from this investment?
Letting variables x1 and x2 denote the allocation of funds to the corporate
and government bond respectively (in thousands of dollars) we obtain the
following formulation for the portfolio manager’s problem:



max Z = 4x1 + 3x2
subject to:
x21x +1+ xx22 ≤ 100



1 2 1.5

100
3x1+4x2 ≤



1 2 3.6

100
≤
x1, x2 0.
≥



We first multiply the second and third inequalities by 100 to avoid fractions.
After we add slack variables to each of the functional inequality constraints
we obtain a representation of the problem in the standard form, suitable for
the simplex method [2] . For example, letting x3 denote the amount we keep


1In other words, we are assuming a quality rating of 0–”perfect” quality, and maturity
of 0 years for cash.
2This representation is not exactly in the standard form since the objective is maximization rather than minimization. However, any maximization problem can be transformed
into a minimization problem by multiplying the objective function by -1. Here, we avoid


30CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


as cash, we can rewrite the first constraint as x1 + x2 + x3 = 100 with
the additional condition of x3. Continuing with this strategy we obtain the
following formulation:



max Z = 4x1 + 3x2
subject to:
x1 + x2 + x3 = 100
2x1 + x2 + x4 = 150
3x1 + 4x2 + x5 = 360
x1, x2, x3, x4, x5 0.
≥


2.4.1 Basic Solutions


Let us consider a general LP problem in the following form:



(2.8)



max c x (2.9)

Ax ≤ b (2.10)

x ≥ 0, (2.11)

where A is an m × n matrix, b is an m-dimensional column vector and c is
an n-dimensional row vector. The n-dimensional column vector x represents
the variables of the problem. (In the bond portfolio example we have m = 3
and n = 2.) Here is how we can represent these vectors and matrices:



a11 a12 . . . a1n
a21 a22 . . . a2n
... ... ... ...
am1 am2 . . . amn









b1
b2
...
bm








     -     , c = c1 c2 . . . cn,







, b =




A =









x1
x2
...
xn



, 0 =







.








0
0
...
0







x =









Next, we add slack variables to each of the functional constraints to get the
augmented form of the problem. Let xs denote the vector of slack variables



xn+1
xn+2
...
xn+m









xs =









and let I denote the m × m identity matrix. Now, the constraints in the
augmented form can be written as




- - [�]
x
A, I
xs











≥ 0. (2.12)



= b,




x
xs



such a transformation to leave the objective function in its natural form–it should be
straightforward to adapt the steps of the algorithm in the following discussion to address
minimization problems.


2.4. THE SIMPLEX METHOD 31



There are many potential solutions to system (2.12). Let us focus on the




     -      - [�]
x
equation A, I
xs







= b. By choosing x = 0 and xs = b, we imme


diately satisfy this equation–but not necessarily all the inequalities. More
generally, we can consider partitions of the augmented matrix [A, I] [3] :

             -              -              -              A, I ≡ B, N,


where B is an m m square matrix that consists of� linearly� independent
×







columns of [A, I]. If we partition the variable vector




x
xs



in the same way




x
xs







≡








xB
xN



,



we can rewrite the equality constraints in (2.12) as




- - [�]
xB
B, N
xN







= BxB + NxN = b,



or by multiplying both sides by B [−][1] from left,


xB + B [−][1] NxN = B [−][1] b.


By our construction, the following three systems of equations are equivalent
in the sense that any solution to one is a solution for the other two:




- - [�]
x
A, I
xs







= b,



BxB + NxN = b
xB + B [−][1] NxN = B [−][1] b


Indeed, the second and third linear systems are just other representations
of the first one in terms of the matrix B. As we observed above, an obvious
solution to the last system (and therefore, to the other two) is xN = 0,
xB = B [−][1] b. In fact, for any fixed values of the components of xN we can
obtain a solution by simply setting


xB = B [−][1] b − B [−][1] NxN. (2.13)


One can think of xN as the independent variables that we can choose
freely, and once they are chosen, the dependent variables xB are determined
uniquely. We call a solution of the systems above a basic solution if it is of
the form
xN = 0, xB = B [−][1] b,


3Here, we are using the notation U ≡ V to indicate that the matrix V is obtained from
the matrix U by permuting its columns. Similarly, for column vectors u and v, u ≡ v
means that v is obtained from u by permuting its elements.


32CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


for some basis matrix B. If in addition, xB = B [−][1] b ≥ 0, the solution
xB = B [−][1] b, xN = 0 is a basic feasible solution of the LP problem above.
The variables xB are called the basic variables, while xN are the nonbasic variables. Geometrically, basic feasible solutions correspond to extreme
points of the feasible set {x : Ax ≤ b, x ≥ 0}. Extreme points of a set are
those that cannot be written as a convex combination of two other points
in the set.
The objective function� Z = c x�can be represented similarly using the
basis partition. Let c = cB, cN represent the partition of the objective
vector. Now, we have the following sequence of equivalent representations
of the objective function equation:



Z = c x Z c x = 0

         
 - ⇔  - − [�]




  -   - [�]
xB
Z cB, cN
 - xN







= 0



Z − cB xB − cN xN = 0

Now substituting xB = B [−][1] b − B [−][1] NxN from (2.13) we obtain

Z − cB (B [−][1] b − B [−][1] NxN) − cN xN = 0Z − (cN − cBB [−][1] N) xN = cBB [−][1] b

Note that the last equation does not contain the basic variables. This representation allows us to determine the net effect on the objective function
of changing a nonbasic variable. This is an essential property used by the
simplex method as we discuss in the following subsection. The vector of
objective function coefficients cN − cBB [−][1] N corresponding to the nonbasic
variables is often called the vector of reduced costs since they contain the
cost coefficients cN “reduced” by the cross effects of the basic variables given
by cBB [−][1] N.


Exercise 2.14 Consider the following linear programming problem:


max 4x1 + 3x2
3x1 + x2 9
≤
3x1 + 2x2 10
≤
x1 + x2 4
≤
x1 0, x2 0.
≥ ≥


First, transform this problem into the standard form. How many basic
solutions does the standard form problem have? What are the basic feasible
solutions and what are the extreme points of the feasible region?


Exercise 2.15 A plant can manufacture five products P1, P2, P3, P4 and
P5. The plant consists of two work areas: the job shop area A1 and the
assembly area A2. The time required to process one unit of product Pj in
work area Ai is pij (in hours), for i = 1, 2 and j = 1, . . ., 5. The weekly
capacity of work area Ai is Ci (in hours). The company can sell all it
produces of product Pj at a profit of sj, for i = 1, . . ., 5.


2.4. THE SIMPLEX METHOD 33


The plant manager thought of writing a linear program to maximize
profits, but never actually did for the following reason: From past experience, he observed that the plant operates best when at most two products
are manufactured at a time. He believes that if he uses linear programming,
the optimal solution will consist of producing all five products and therefore
it will not be of much use to him. Do you agree with him? Explain, based
on your knowledge of linear programming.


Answer: The linear program has two constraints (one for each of the work
areas). Therefore, at most two variables are positive in a basic solution.
In particular, this is the case for an optimal basic solution. So the plant
manager is mistaken in his beliefs. There is always an optimal solution of
the linear program in which at most two products are manufactured.


2.4.2 Simplex Iterations


A key result of linear programming theory is that when a linear programming
problem has an optimal solution, it must have an optimal solution that is
an extreme point. The significance of this result lies in the fact that when we
are looking for a solution of a linear programming problem we can focus on
the objective value of extreme point solutions only. There are only finitely
many of them, so this reduces our search space from an infinite space to a
finite one.
The simplex method solves a linear programming problem by moving
from one extreme point to an adjacent extreme point. Since, as we discussed
in the previous section, extreme points of the feasible set correspond to basic
feasible solutions (BFSs), algebraically this is achieved by moving from one
BFS to another. We describe this strategy in detail in this section.
The process we mentioned in the previous paragraph must start from an
initial BFS. How does one find such a point? While finding a basic solution
is almost trivial, finding feasible basic solutions can be difficult. Fortunately,
for problems of the form (2.9), such as the bond portfolio optimization
problem (2.8) there is a simple strategy. Choosing





, xB =





x3
 x4
x5





, N =





1 1
 2 1
5 10





, xN =




x1
x2







B =





1 0 0
 0 1 0
0 0 1



we get an initial basic feasible solution (BFS) with xB = B [−][1] b = [100, 150, 360] [T] .
The objective value for this BFS is 4 · 0 + 3 · 0 = 0.


Once we obtain a BFS, we first need to determine whether this solution
is optimal or whether there is a way to improve the objective value. Recall
that the basic variables are uniquely determined once we choose to set the
nonbasic variables to a specific value, namely zero. So, the only way to
obtain alternative solutions is to modify the values of the nonbasic variables.
We observe that both the nonbasic variables x1 and x2 would improve the
objective value if they were introduced into the basis. Why? The initial basic


34CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS



feasible solution has x1 = x2 = 0 and we can get other feasible solutions by
increasing the value of one of these two variables. To preserve feasibility of
the equality constraints, this will require adjusting the values of the basic
variables x3, x4, and x5. But since all three are strictly positive in the initial
basic feasible solution, it is possible to make x1 strictly positive without
violating any of the constraint, including the nonnegativity requirements.
None of the variables x3, x4, x5 appear in the objective row. Thus,
we only have to look at the coefficient of the nonbasic variable we would
increase to see what effect this would have on the objective value. The
rate of improvement in the objective value for x1 is 4 and for x2 this rate
is only 3. While a different method may choose the increase both of these
variables simultaneously, the simplex method requires that only one nonbasic
variable is modified at a time. This requirement is the algebraic equivalent
of the geometric condition of moving from one extreme point to an adjacent
extreme point. Between x1 and x2, we choose the variable x1 to enter the
basis since it has a faster rate of improvement.
The basis holds as many variables as there are equality constraints in the
standard form formulation of the problem. Since x1 is to enter the basis, one
of x3, x4, and x5 must leave the basis. Since nonbasic variables have value
zero in a basic solution, we need to determine how much to increase x1 so
that one of the current basic variables becomes zero and can be designated
as nonbasic. The important issue here is to maintain the nonnegativity of all
basic variables. Because each basic variable only appears in one row, this is
an easy task. As we increase x1, all current basic variables will decrease since
x1 has positive coefficients in each row [4] . We guarantee the nonnegativity of
the basic variables of the next iteration by using the ratio test. We observe
that
increasing x1 beyond 100/1=100 x3 < 0,
⇒
increasing x1 beyond 150/2=75 x4 < 0,
⇒
increasing x1 beyond 360/3=120 x5 < 0,
⇒

so we should not increase x1 more than min{100, 75, 120} = 75. On the other
hand if we increase x1 exactly by 75, x4 will become zero. The variable x4
is said to leave the basis. It has now become a nonbasic variable.
Now we have a new basis: x3, x1, x5 . For this basis we have the fol{ }
lowing basic feasible solution:



















100
 150
360



 =





,





















x3
 x1
x5



1 −1/2 0
 0 1/2 0
0 −3/2 1





25
 75
135



B =



1 1 0
 0 2 0
0 3 1



, xB =



1
 = B− b =




x2
x4











N =





1 0
 1 1
4 0





, xN =



=




0
0



.



4If x1 had a zero coefficient in a particular row, then increasing it would not effect
the basic variable in that row. If, x1 had a negative coefficient in a row, then as x1 was
being increased the basic variable of that row would need to be increased to maintain the
equality in that row; but then we would not worry about that basic variable becoming
negative.


2.4. THE SIMPLEX METHOD 35


After finding a new feasible solution, we always ask the question ‘Is this
the optimal solution, or can we still improve it?’. Answering that question
was easy when we started, because none of the basic variables were in the
objective function. Now that we have introduced x1 into the basis, the
situation is more complicated. If we now decide to increase x2, the objective
row coefficient of x2 does not tell us how much the objective value changes
per unit change in x2, because changing x2 requires changing x1, a basic
variable that appears in the objective row. It may happen that, increasing
x2 by 1 unit does not increase the objective value by 3 units, because x1
may need to be decreased, pulling down the objective function. It could
even happen that increasing x2 actually decreases the objective value even
though x2 has a positive coefficient in the objective function. So, what do
we do? We could still do what we did with the initial basic solution if x1
did not appear in the objective row and the rows where it is not the basic
variable. To achieve this, all we need to do is to use the row where x1 is the
basic variable (in this case the second row) to solve for x1 in terms of the
nonbasic variables and then substitute this expression for x1 in the objective
row and other equations. So, the second equation


2x1 + x2 + x4 = 150


would give us:



2 [1] [x][2][ −] [1] 2



x1 = 75
     - 2 [1]



2 [x][4][.]



Substituting this value in the objective function we get:



Z = 4x1 + 3x2 = 4(75
           - [1] 2




[1] 2 [x][2][ −] [1] 2




[+] [3][x][2] [=] [300] [+] [x][2]
2 [x][4][)] [−] [2][x][4][.]



Continuing the substitution we get the following representation of the original bond portfolio problem:


max Z
subject to:
Z x2 + 2x4 = 300

     - 12 [x][2] 12 [x][4] + x3 = 25
12 [x][2] −+ 12 [x][4] + x1 = 75
52 [x][2] 32 [x][4] + x5 = 135

         x2, x4, x3, x1, x5 0.
≥

This representation looks exactly like the initial system. Once again, the
objective row is free of basic variables and basic variables only appear in the
row where they are basic, with a coefficient of 1. Therefore, we now can tell
how a change in a nonbasic variables would effect the objective function:
increasing x2 by 1 unit will increase the objective function by 1 unit (not 3!)
and increasing x4 by 1 unit will decrease the objective function by 2 units.
Now that we represented the problem in a form identical to the original,
we can repeat what we did before, until we find a representation that gives


36CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


the optimal solution. If we repeat the steps of the simplex method, we find
that x2 will be introduced into the basis next, and the leaving variable will
be x3. If we solve for x1 using the first equation and substitute for it in the
remaining ones, we get the following representation:


max Z
subject to:
Z + 2x3 + x4 = 350
2x3 x4 + x2 = 50

         x3 + x4 + x1 = 50

       5x3 + x4 + x5 = 10

       x3, x4, x2, x1, x5 0.
≥


Once again, notice that this representation is very similar to the tableau
we got at the end of the previous section. The basis and the basic solution
that corresponds to the system above is:





, xB =





x2
 x1
x5





2 −1 0
 −1 1 0
−5 1 1











100
 150
360





 =





50
 50
10





,



B =





1 1 0
 1 2 0
4 3 1






1
 = B− b =





, xN =




x3
x4











N =





1 0
 0 1
0 0



=




0
0



.



At this point we can conclude that this basic solution is the optimal
solution. Let us try to understand why. From the objective function row of
our final representation of the problem we have that for any feasible solution
x = (x1, x2, x3, x4, x5), the objective function Z satisfies


Z + 2x3 + x4 = 350.


Since x3 0 and x4 0 is also required, this implies that in every feasible
≥ ≥
solution
Z ≤ 350.

But we just found a basic feasible solution with value 350. So this is the
optimal solution.
More generally, recall that for any BFS x = (xB, xN), the objective value
Z satisfies
Z − (cN − cBB [−][1] N) xN = cBB [−][1] b

If for a BFS xB = B [−][1] b ≥ 0, xN = 0, we have

cN − cBB [−][1] N ≤ 0,

then this solution is an optimal solution since it has objective value Z = cBB [−][1] b
whereas, for all other solutions, xN ≥ 0 implies that Z ≤ cBB [−][1] b.


2.4. THE SIMPLEX METHOD 37


Exercise 2.16 What is the solution to the following linear programming
problem:


Max z = c1x1 + c2x2 + · · · + cnxn
s.t. a1x1 + a2x2 + · · · + anxn ≤ b,

0 xi ui (i = 1, 2, . . ., n),
≤ ≤

Assume that all the data elements (ci, ai, and ui) are strictly positive and
the coefficients are arranged such that:



c1
a1 ≥ a [c][2] 2



.
an



. . .
a [c][2] 2 ≥ ≥ a [c][n] n



Write the problem in standard form and apply the simplex method to it.
What will be the steps of the simplex method when applied to this problem,
i.e., in what order will the variables enter and leave the basis?


2.4.3 The Tableau Form of the Simplex Method


In most linear programming textbooks, the simplex method is described using tableaus that summarize the information in the different representations
of the problem we saw above. Since the reader will likely encounter simplex
tableaus elsewhere, we include a brief discussion for the purpose of completeness. To study the tableau form of the simplex method, we recall the
bond portfolio example of the previous subsection. We begin by rewriting
the objective row as
Z 4 x1 3 x2 = 0

         -         
and represent this system using the following tableau:

|Basic<br>var.|⇓<br>x x x x x<br>1 2 3 4 5|Col3|
|---|---|---|
|Z|-4<br>-3<br>0<br>0<br>0|0|
|x3<br>⇐<br>x4<br>x5|1<br>1<br>1<br>0<br>0<br>2∗<br>1<br>0<br>1<br>0<br>3<br>4<br>0<br>0<br>1|100<br>150<br>360|



This tableau is often called the simplex tableau. The columns labeled by
each variable contain the coefficients of that variable in each equation, including the objective row equation. The leftmost column is used to keep
track of the basic variable in each row. The arrows and the asterisk will be
explained below.


Step 0. Form the initial tableau.


Once we have formed this tableau we look for an entering variable, i.e., a
variable that has a negative coefficient in the objective row and will improve
the objective function if it is introduced into the basis. In this case, two
of the variables, namely x1 and x2, have negative objective row coefficients.


38CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


Since x1 has the most negative coefficient we will pick that one (this is indicated by the arrow pointing down on x1), but in principle any variable with
a negative coefficient in the objective row can be chosen to enter the basis.


Step 1. Find a variable with a negative coefficient in the first row (the
objective row). If all variables have nonnegative coefficients in the objective
row, STOP, the current tableau is optimal.


After we choose x1 as the entering variable, we need to determine a leaving variable. The leaving variable is found by performing a ratio test. In the
ratio test, one looks at the column that corresponds to the entering variable,
and for each positive entry in that column computes the ratio of that positive
number to the right hand side value in that row. The minimum of these ratios tells us how much we can increase our entering variable without making
any of the other variables negative. The basic variable in the row that gives
the minimum ratio becomes the leaving variable. In the tableau above the
column for the entering variable, the column for the right-hand-side values,
and the ratios of corresponding entries are



 x1

1
 2
5





,



RHS


100
 150
360





,



ratio
100/1
150/2
360/3



, min
{ [100] 1




[150]
1 [,] 2



2



∗
, [360]

3

[}][ = 75][,]



and therefore x4, the basic variable in the second row, is chosen as the
leaving variable, as indicated by the left-pointing arrow in the tableau.
One important issue here is that, we only look at the positive entries in
the column when we perform the ratio test. Notice that if some of these
entries were negative, then increasing the entering variable would only increase the basic variable in those rows, and would not force them to be
negative, therefore we need not worry about those entries. Now, if all of the
entries in a column for an entering variable turn out to be zero or negative,
then we conclude that the problem must be unbounded ; we can increase the
entering variable (and the objective value) indefinitely, the equalities can be
balanced by increasing the basic variables appropriately, and none of the
nonnegativity constraints will be violated.


Step 2. Consider the column picked in Step 1. For each positive entry
in this column, calculate the ratio of the right-hand-side value to that entry.
Find the row that gives minimum such ratio and choose the basic variable
in that row as the leaving variable. If all the entries in the column are zero
or negative, STOP, the problem is unbounded.


Before proceeding to the next iteration, we need to update the tableau
to reflect the changes in the set of basic variables. For this purpose, we
choose a pivot element, which is the entry in the tableau that lies in the
intersection of the column for the entering variable (the pivot column), and
the row for the leaving variable (the pivot row ). In the tableau above, the


2.4. THE SIMPLEX METHOD 39


pivot element is the number 2, marked with an asterisk. The next job is
pivoting. When we pivot, we aim to get the number 1 in the position of the
pivot element (which can be achieved by dividing the entries in the pivot
row by the pivot element), and zeros elsewhere in the pivot column (which
can be achieved by adding suitable multiples of the pivot row to the other
rows, including the objective row). All these operations are row operations
on the matrix that consists of the numbers in the tableau, and what we are
doing is essentially Gaussian elimination on the pivot column. Pivoting on

|bove yields:|Col2|Col3|
|---|---|---|
|Basic<br>var.|⇓<br>x1<br>x2<br>x3<br>x4<br>x5||
|Z|0<br>-1<br>0<br>2<br>0<br>|300|
|⇐<br>x3<br>x1<br>x5|0<br>1/2∗<br>1<br>-1/2<br>0<br>1<br>1/2<br>0<br>1/2<br>0<br>0<br>5/2<br>0<br>-3/2<br>1|25<br>75<br>135|



Step 3. Find the entry (the pivot element) in the intersection of the
column picked in Step 1 (the pivot column) and the row picked in Step 2
(the pivot row). Pivot on that entry, i.e., divide all the entries in the pivot
row by the pivot element, add appropriate multiples of the pivot row to the
others in order to get zeros in other components of the pivot column. Go to
Step 1.


If we repeat the steps of the simplex method, this time working with the
new tableau, we first identify x2 as the only candidate to enter the basis.
Next, we do the ratio test:



min
{ 1 [25] /2 [∗]




[75]
1 [25] /2 [∗] [,] 1/




[75] [135]

1/2 [,] 5/2



5/2 [}][ = 50][,]



so x3 leaves the basis. Now, one more pivot produces the optimal tableau:

|Basic<br>var.|x x x x x<br>1 2 3 4 5|Col3|
|---|---|---|
|Z|0<br>0<br>2<br>1<br>0|350|
|x2<br>x1<br>x5|0<br>1<br>2<br>-1<br>0<br>1<br>0<br>-1<br>1<br>0<br>0<br>0<br>-5<br>1<br>1|50<br>50<br>10|



This solution is optimal since all the coefficients in the objective row are
nonnegative.


Exercise 2.17 Solve the following linear program by the simplex method.


max 4x1 + x2 x3

            x1 + 3x3 6
≤
3x1 + x2 + 3x3 9
≤
x1 0, x2 0, x3 0.
≥ ≥ ≥


40CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


Answer:








|Col1|x x x s s<br>1 2 3 1 2|Col3|
|---|---|---|
|Z|−4<br>−1<br>1<br>0<br>0|0|
|s1<br>s2|1<br>0<br>3<br>1<br>0<br>3<br>1<br>3<br>0<br>1|6<br>9|
|Z|0<br>1<br>3<br>5<br>0<br>4<br>3<br><br>|12|
|s1<br>x1|0<br>−1<br>3<br>2<br>1<br>−1<br>3<br>1<br>1<br>3<br>1<br>0<br>1<br>3|3<br>3|



The optimal solution is x1 = 3, x2 = x3 = 0.


Exercise 2.18 Solve the following linear program by the simplex method.


max 4x1 + x2 x3

            x1 + 3x3 6
≤
3x1 + x2 + 3x3 9
≤
x1 + x2 x3 2

            - ≤
x1 0, x2 0, x3 0.
≥ ≥ ≥


Exercise 2.19 Suppose the following tableau was obtained in the course
of solving a linear program with nonnegative variables x1, x2, x3 and two
inequalities. The objective function is maximized and slack variables x4 and
x5 were added.

|Basic<br>var.|x x x x x<br>1 2 3 4 5|Col3|
|---|---|---|
|Z|0<br>a<br>b<br>0<br>4|82|
|x4<br>x1|0<br>-2<br>2<br>1<br>3<br>1<br>-1<br>3<br>0<br>-5|c<br>3|



Give conditions on a, b and c that are required for the following statements
to be true:
(i) The current basic solution is a basic feasible solution.
Assume that the condition found in (i) holds in the rest of the exercise.
(ii) The current basic solution is optimal.
(iii) The linear program is unbounded (for this question, assume that
b > 0).
(iv) The current basic solution is optimal and there are alternate optimal
solutions (for this question, assume that a > 0).


2.4.4 Graphical Interpretation


Figure 2.1 shows the feasible region for Example 2.1. The five inequality
constraints define a convex pentagon. The five corner points of this pentagon
(the black dots on the figure) are the basic feasible solutions: each such
solution satisfies two of the constraints with equality.


2.4. THE SIMPLEX METHOD 41



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-40-0.png)















Figure 2.1: Graphical interpretation of the simplex iterations


Which are the solutions explored by the simplex method? The simplex
method starts from the basic feasible solution (x1 = 0, x2 = 0) (in this
solution, x1 and x2 are the nonbasic variables. The basic variables x3 =
100, x4 = 150 and x5 = 360 correspond to the constraints that are not
satisfied with equality). The first iteration of the simplex method makes x1
basic by increasing it along an edge of the feasible region until some other
constraint is satisfied with equality. This leads to the new basic feasible
solution (x1 = 75, x2 = 0) (in this solution, x2 and x4 are nonbasic, which
means that the constraints x2 0 and 2x1 + x2 150 are satisfied with
≥ ≤
equality). The second iteration makes x2 basic while keeping x4 nonbasic.
This correspond to moving along the edge 2x1 + x2 = 150. The value x2 is
increased until another constraint becomes satisfied with equality. The new
solution is x1 = 50 and x2 = 50. No further movement from this point can
increase the objective, so this is the optimal solution.


Exercise 2.20 Solve the linear program of Exercise 2.14 by the simplex
method. Give a graphical interpretation of the simplex iterations.


Exercise 2.21 Find basic solutions of Example 2.1 that are not feasible.
Identify these solutions in Figure 2.1.


2.4.5 The Dual Simplex Method


The previous sections describe the primal simplex method, which moves
from a basic feasible solution to another until all the reduced costs are
nonpositive. There are certain applications where the dual simplex method
is faster. In contrast to the primal simplex method, this method keeps the
reduced costs nonpositive and moves from a basic (infeasible) solution to
another until a basic feasible solution is reached.
We illustrate the dual simplex method on an example. Consider Exam

42CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


ple 2.1 with the following additional constraint.


6x1 + 5x2 ≤ 500

Adding a slack variable x6, we get 6x1 +5x2 + x6 = 500. To initialize the
dual simplex method, we can start from any basic solution with nonpositive
reduced costs. For example, we can start from the optimal solution that
we found in Section 2.4.3, without the additional constraint, and make x6
basic. This gives the following tableau.

|Basic<br>var.|x x x x x x<br>1 2 3 4 5 6|Col3|
|---|---|---|
|Z|0<br>0<br>2<br>1<br>0<br>0|350|
|x2<br>x1<br>x5<br>x6|0<br>1<br>2<br>-1<br>0<br>0<br>1<br>0<br>-1<br>1<br>0<br>0<br>0<br>0<br>-5<br>1<br>1<br>0<br>6<br>5<br>0<br>0<br>0<br>1|50<br>50<br>10<br>500|



Actually, this tableau is not yet in the right format. Indeed, x1 and x2
are basic and therefore their columns in the tableau should be unit vectors.
To restore this property, it suffices to eliminate the 6 and 5 in the row of
x6 by subtracting appropriate multiples of the rows of x1 and x2. This now
gives the tableau in the correct format.

|Basic<br>var.|x x x x x x<br>1 2 3 4 5 6|Col3|
|---|---|---|
|Z|0<br>0<br>2<br>1<br>0<br>0|350|
|x2<br>x1<br>x5<br>x6|0<br>1<br>2<br>-1<br>0<br>0<br>1<br>0<br>-1<br>1<br>0<br>0<br>0<br>0<br>-5<br>1<br>1<br>0<br>0<br>0<br>-4<br>-1<br>0<br>1|50<br>50<br>10<br>-50|



Now we are ready to apply the dual simplex algorithm. Note that the
current basic solution x1 = 50, x2 = 50, x3 = x4 = 0, x5 = 10, x6 = 50

                    is infeasible since x6 is negative. We will pivot to make it nonnegative. As
a result, variable x6 will leave the basis. The pivot element will be one of
the negative entry in the row of x6, namely -4 or -1. Which one should we
choose in order to keep all the reduced costs nonnegative? The minimum
ratio between 2 1 [the] [variable] [that] [enters] [the] [basis][.]
4 [and] 1 [determines]
|− | |− |
Here the minimum is 2 [1] [, which means that][ x][3][ enters the basis.] [After pivoting]

on -4, the tableau becomes:


|Basic<br>var.|x x x x x x<br>1 2 3 4 5 6|Col3|
|---|---|---|
|Z|0<br>0<br>0<br>0.5<br>0<br>0.5|325|
|x2<br>x1<br>x5<br>x3|0<br>1<br>0<br>-1.5<br>0<br>0.5<br>1<br>0<br>0<br>1.25<br>0<br>-0.25<br>0<br>0<br>0<br>2.25<br>1<br>-1.25<br>0<br>0<br>1<br>0.25<br>0<br>-0.25|25<br>62.5<br>72.5<br>12.5|


2.4. THE SIMPLEX METHOD 43


The corresponding basic solution is x1 = 62.5, x2 = 25, x3 = 12.5,
x4 = 0, x5 = 72.5, x6 = 0. Since it is feasible and all reduced costs are
nonpositive, this is the optimum solution. If there had still been negative
basic variables in the solution, we would have continued pivoting using the
rules outlined above: the variable that leaves the basis is one with a negative
value, the pivot element is negative, and the variable that enters the basis
is chosen by the minimum ratio rule.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-42-0.png)













Figure 2.2: Graphical interpretation of the dual simplex iteration


Exercise 2.22 Solve the following linear program by the dual simplex method,
starting from the solution found in Exercise 2.17.


max 4x1 + x2 x3

            x1 + 3x3 6
≤
3x1 + x2 + 3x3 9
≤
x1 + x2 x3 2

            - ≤
x1 0, x2 0, x3 0.
≥ ≥ ≥


2.4.6 Alternatives to the Simplex Method


Performing a pivot of the simplex method is extremely fast on today’s computers, even for problems with thousands of variables and hundreds of constraints. This explains the success of the simplex method. However, for
large problems, the number of iterations also tends to be large. At the time
of this writing, LPs with tens of thousands of constraints and 100,000 or
more variables are generally considered large problems. Such models are
not uncommon in financial applications and can often be handled by the
simplex method.
Although the simplex method demonstrates satisfactory performance for
the solution of most practical problems, it has the disadvantage that, in the
worst case, the amount of computing time (the so-called worst-case complexity) can grow exponentially in the size of the problem. Here size refers


44CHAPTER 2. LINEAR PROGRAMMING: THEORY AND ALGORITHMS


to the space required to write all the data in binary. If all the numbers are
bounded (say between 10 [−][6] and 10 [6] ), a good proxy for the size of a linear
program is the number of variables times the number of constraints. One of
the important concepts in the theoretical study of optimization algorithms
is the concept of polynomial-time algorithms. This refers to an algorithm
whose running time can be bounded by a polynomial function of the input
size for all instances of the problem class that it is intended for. After it
was discovered in the 1970s that the worst case complexity of the simplex
method is exponential (and, therefore, that the simplex method is not a
polynomial-time algorithm) there was an effort to identify alternative methods for linear programming with polynomial-time complexity. The first such
method, called the ellipsoid method was developed by Yudin and Nemirovski
in 1979. The same year Khachiyan [41] proved that the ellipsoid method is
a polynomial-time algorithm for linear programming. But the more exciting
and enduring development was the announcement by Karmarkar in 1984
that an Interior Point Method (IPM) can solve LPs in polynomial time.
What distinguished Karmarkar’s IPM from the ellipsoid method was that,
in addition to having this desirable theoretical property, it could solve some
real-world LPs much faster than the simplex method. These methods use a
different strategy to reach the optimum, generating iterates in the interior of
the feasible region rather than at its extreme points. Each iteration is fairly
expensive, but the number of iterations needed does not depend much on
the size of the problem and is often less than 50. As a result, interior point
methods can be faster than the simplex method for large scale problems.
Most state-of-the-art linear programming packages (Cplex, Xpress, OSL,
etc.) give you the option to solve your linear programs by either method.
We present interior point methods in Chapter 7, in the context of solving
quadratic programs.


## Chapter 3

# LP Models: Asset/Liability Cash Flow Matching

#### 3.1 Short Term Financing

Corporations routinely face the problem of financing short term cash commitments. Linear programming can help in figuring out an optimal combination of financial instruments to meet these commitments. To illustrate
this, consider the following problem. For simplicity of exposition, we keep
the example very small.


A company has the following short term financing problem.

|Month|Jan|Feb|Mar|Apr|May|Jun|
|---|---|---|---|---|---|---|
|Net Cash Flow|-150|-100|200|-200|50|300|



Net cash flow requirements are given in thousands of dollars. The company has the following sources of funds


  - A line of credit of up to $100K at an interest rate of 1% per month,

  - In any one of the first three months, it can issue 90-day commercial
paper bearing a total interest of 2% for the 3-month period,


  - Excess funds can be invested at an interest rate of 0.3% per month.

There are many questions that the company might want to answer. What
interest payments will the company need to make between January and
June? Is it economical to use the line of credit in some of the months? If so,
when? How much? Linear programming gives us a mechanism for answering
these questions quickly and easily. It also allows to answer some “what if”
questions about changes in the data without having to resolve the problem.
What if Net Cash Flow in January were -200 (instead of -150)? What if the
limit on the credit line were increased from 100 to 200? What if the negative
Net Cash Flow in January is due to the purchase of a machine worth 150
and the vendor allows part or all of the payment on this machine to be made
in June at an interest of 3% for the 5-month period? The answers to these


45


46CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


questions are readily available when this problem is formulated and solved
as a linear program.
There are three steps in applying linear programming: modeling, solving,
and interpreting.


3.1.1 Modeling


We begin by modeling the above short term financing problem. That is,
we write it in the language of linear programming. There are rules about
what one can and cannot do within linear programming. These rules are in
place to make certain that the remaining steps of the process (solving and
interpreting) can be successful.
Key to a linear program are the decision variables, objective, and constraints.


Decision Variables. The decision variables represent (unknown) decisions to be made. This is in contrast to problem data, which are values that
are either given or can be simply calculated from what is given. For the
short term financing problem, there are several possible choices of decision
variables. We will use the following decision variables: the amount xi drawn
from the line of credit in month i, the amount yi of commercial paper issued
in month i, the excess funds zi in month i and the company’s wealth v in
June. Note that, alternatively, one could use the decision variables xi and
zi only, since excess funds and company’s wealth can be deduced from these
variables.


Objective. Every linear program has an objective. This objective is
to be either minimized or maximized. This objective has to be linear in
the decision variables, which means it must be the sum of constants times
decision variables. 3x1 10x2 is a linear function. x1x2 is not a linear

       function. In this case, our objective is simply to maximize v.


Constraints. Every linear program also has constraints limiting feasible
decisions. Here we have three types of constraints: (i) cash inflow = cash
outflow for each month, (ii) upper bounds on xi and (iii) nonnegativity of
the decision variables xi, yi and zi.
For example, in January (i = 1), there is a cash requirement of $150.
To meet this requirement, the company can draw an amount x1 from its
line of credit and issue an amount y1 of commercial paper. Considering the
possibility of excess funds z1 (possibly 0), the cash flow balance equation is
as follows.
x1 + y1 z1 = 150

           
Next, in February (i = 2), there is a cash requirement of $100. In addition,
principal plus interest of 1.01x1 is due on the line of credit and 1.003z1 is
received on the invested excess funds. To meet the requirement in February,
the company can draw an amount x2 from its line of credit and issue an
amount y2 of commercial paper. So, the cash flow balance equation for
February is as follows.


x2 + y2 1.01x1 + 1.003z1 z2 = 100

       -        

3.1. SHORT TERM FINANCING 47


Similarly, for March we get the following equation:


x3 + y3 1.01x2 + 1.003z2 z3 = 200

       -       -       

For the months of April, May, and June, issuing a commercial paper is
no longer an option, so we will not have variables y4, y5, and y6 in the
formulation. Furthermore, any commercial paper issued between January
and March requires a payment with 2% interest 3 months later. Thus, we
have the following additional equations:


x4 1.02y1 1.01x3 + 1.003z3 z4 = 200

    -     -     x5 1.02y2 1.01x4 + 1.003z4 z5 = 50

    -     -     -     1.02y3 1.01x5 + 1.003z5 v = 300

    -     -     -     
Note that xi is the balance on the credit line in month i, not the incremental
borrowing in month i. Similarly, zi represents the overall excess funds in
month i. This choice of variables is quite convenient when it comes to writing
down the upper bound and nonnegativity constraints.


0 xi 100
≤ ≤
yi 0
≥
zi 0.
≥

Final Model. This gives us the complete model of this problem:


max v
x1 + y1 z1 = 150

                 x2 + y2 1.01x1 + 1.003z1 z2 = 100

         -          x3 + y3 1.01x2 + 1.003z2 z3 = 200

         -          -          x4 1.02y1 1.01x3 + 1.003z3 z4 = 200

      -      -      x5 1.02y2 1.01x4 + 1.003z4 z5 = 50

      -      -      -      1.02y3 1.01x5 + 1.003z5 v = 300

      -      -      -      x1 100
≤
x2 100
≤
x3 100
≤
x4 100
≤
x5 100
≤
xi, yi, zi 0.
≥

Formulating a problem as a linear program means going through the
above process of clearly defining the decision variables, objective, and constraints.


Exercise 3.1 How would the formulation of the short-term financing problem above change if the commercial papers issued had a 2 month maturity
instead of 3?


48CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


Exercise 3.2 A company will face the following cash requirements in the
next eight quarters (positive entries represent cash needs while negative
entries represent cash surpluses).

|Q1|Q2|Q3|Q4|Q5|Q6|Q7|Q8|
|---|---|---|---|---|---|---|---|
|100|500|100|-600|-500|200|600|-900|



The company has three borrowing possibilities.


  - a 2-year loan available at the beginning of Q1, with a 1% interest per
quarter.


  - The other two borrowing opportunities are available at the beginning
of every quarter: a 6-month loan with a 1.8% interest per quarter, and
a quarterly loan with a 2.5% interest for the quarter.


Any surplus can be invested at a 0.5% interest per quarter.
Formulate a linear program that maximizes the wealth of the company
at the beginning of Q9.


Exercise 3.3 A home buyer in France can combine several mortgage loans
to finance the purchase of a house. Given borrowing needs B and a horizon of
T months for paying back the loans, the home buyer would like to minimize
his total cost (or equivalently, the monthly payment p made during each
of the next T months). Regulations impose limits on the amount that can
be borrowed from certain sources. There are n different loan opportunities
available. Loan i has a fixed interest rate ri, a length Ti T and a maximum
≤
amount borrowed bi. The monthly payment on loan i is not required to be
the same every month, but a minimum payment mi is required each month.
However the total monthly payment p over all loans is constant. Formulate
a linear program that finds a combination of loans that minimizes the home
buyer’s cost of borrowing. [Hint: In addition to variables xti for the payment
on loan i in month t, it may be useful to introduce a variable for the amount
of outstanding principal on loan i in month t.]


3.1.2 Solving the Model with SOLVER


Special computer programs can be used to find solutions to linear programming models. The most widely available program is undoubtedly SOLVER,
included in all recent versions of the Excel spreadsheet program. Here are
other suggestions:


  - MATLAB has a linear programming solver that can be accessed with
the command linprog. Type help linprog to find out details.


  - Even if one does not have access to any linear programming software,
it is possible to solve linear programs (and other optimization problems) using the website
http://www-neos.mcs.anl.gov/neos/


3.1. SHORT TERM FINANCING 49


This is the website for the Network Enabled Optimization Server. Using the JAVA submission tool on this site, one can submit a linear
programming problem (in some standard format) and have a remote
computer solve his/her problem using one of the several solver options.
The solution is then transmitted to the submitting person by e-mail.


  - A good open source LP code written in C is CLP available from the
following website at the time of this writing:
http://www.coin-or.org/


SOLVER, while not a state of the art code (which can cost upwards of
$10,000 per copy) is a reasonably robust, easy-to-use tool for linear programming. SOLVER uses standard spreadsheets together with an interface
to define variables, objective, and constraints.


Here are a brief outline and some hints and shortcuts on how to create
a SOLVER spreadsheet:


  - Start with a spreadsheet that has all of the data entered in some
reasonably neat way.


In the short term financing example, the spreadsheet might contain
the cash flows, interest rates and credit limit.


  - The model will be created in a separate part of the spreadsheet. Identify one cell with each decision variable. SOLVER will eventually put
the optimal values in these cells.


In the short term financing example, we could associate cells $B$2 to
$B$6 with variables x1 to x5 respectively, cells $C$2 to $C$4 with the
yi variables, cells $D$2 to $D$6 with the zi variables and, finally, $E$2
with the variable v.


  - A separate cell represents the objective. Enter a formula that represents the objective.


For the short term financing example, we might assign cell $B$8 to the
objective function. Then, in cell $B$8, we enter the function = $E$2.


This formula must be a linear formula, so, in general, it must be of the
form: cell1*cell1’ + cell2*cell2’ + ..., where cell1, cell2
and so on contain constant values and cell1’, cell2’ and so on are
the decision variable cells.


  - We then have a cell to represent the left hand side of each constraint
(again a linear function) and another cell to represent the right hand
side (a constant).


In the short term financing example, cells $B$10 to $B$15 might contain the amounts generated through financing, for each month, and
cells $D$10 to $D$15 the cash requirements for each month. For example, cell $B$10 would contain the function = $C$2 + $B$2 -$D$2
and cell $D$10 the value 150. Similarly, rows 16 to 20 could be used
to write the credit limit constraints.


50CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


Helpful Hint: Excel has a function sumproduct() that is designed
for linear programs. sumproduct(a1..a10,b1..b10) is identical to
a1*b1+a2*b2+a3*b3+...+a10*b10. This function can save much time
and aggravation. All that is needed is that the length of the first range
be the same as the length of the second range (so one can be horizontal
and the other vertical).


Helpful Hint: It is possible to assign names to cells and ranges (under
the Insert-Name menu). Rather than use a1..a10 as the variables,
you can name that range var (for example) and then use var wherever
a1..a10 would have been used.


  - We then select Solver under the Tools menu. This gives a form to
fill out to define the linear program.


  - In the ‘‘Set Cell’’ box, select the objective cell. Choose Maximize
or Minimize.


  - In the ‘‘By Changing Cells’’, put in the range containing the variable cells.


  - We next add the constraints. Press the ‘‘Add...’’ button to add
constraints. The dialog box has three parts for the left hand side, the
type of constraint, and the right hand side. Put the cell references
for a constraint in the form, choose the right type, and press ‘‘Add’’.
Continue until all constraints are added. On the final constraint, press
‘‘OK’’.


Helpful Hint: It is possible to include ranges of constraints, as long as
they all have the same type. c1..e1 <= c3..e3 means c1 <= c3, d1
<= d3, e1 <= e3. a1..a10 >= 0 means each individual cell must be
greater than or equal to 0.


  - Push the options button and toggle the ‘‘Assume Linear Model’’
in the resulting dialog box. This tells Excel to call a linear rather than
a nonlinear programming routine so as to solve the problem more efficiently. This also gives you sensitivity ranges, which are not available
for nonlinear models.


Note that, if you want your variables to assume nonnegative values
only, you need to specify this in the options box (alternatively, you
can add nonnegativity constraints in the previous step, in your constraints).


  - Push the Solve button. In the resulting dialog box, select ‘‘Answer’’
and ‘‘Sensitivity’’. This will put the answer and sensitivity analysis in two new sheets. Ask Excel to ‘‘Keep Solver values’’, and
your worksheet will be updated so that the optimal values are in the
variable cells.


3.1. SHORT TERM FINANCING 51


Exercise 3.4 Solve the linear program formulated in Exercise 3.2 with your
favorite software package.


3.1.3 Interpreting the output of SOLVER


If we were to solve the short-term financing problem above using SOLVER,
the solution is given in the ‘‘Answer’’ report that looks as follows.


Target Cell (Max)

Original Final
Cell Name Value Value
$B$8 Objective 0 92.49694915


Adjustable Cells

Original Final
Cell Name Value Value
$B$2 x1 0 0
$B$3 x2 0 50.98039216
$B$4 x3 0 0
$B$5 x4 0 0
$B$6 x5 0 0
$C$2 y1 0 150
$C$3 y2 0 49.01960784
$C$4 y3 0 203.4343636
$D$2 z1 0 0
$D$3 z2 0 0
$D$4 z3 0 351.9441675
$D$5 z4 0 0
$D$6 z5 0 0
$E$2 v 0 92.49694915


Constraints

Cell
Cell Name Value Formula Slack
$B$10 January 150 $B$10 = $D$10 0
$B$11 February 100 $B$11 = $D$11 0
$B$12 March −200 $B$12 = $D$12 0
$B$13 April 200 $B$13 = $D$13 0
$B$14 May −50 $B$14 = $D$14 0
$B$15 June −300 $B$15 = $D$15 0
$B$16 x1limit 0 $B$16 <= $D$16 100
$B$17 x2limit 50.98039216 $B$17 <= $D$17 49.01960784
$B$18 x3limit 0 $B$18 <= $D$18 100
$B$19 x4limit 0 $B$19 <= $D$19 100
$B$20 x5limit 0 $B$20 <= $D$20 100


This report is fairly easy to read: the company’s wealth v in June will
be $92,497. This is reported in Final Value of the Objective (recall that


52CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


our units are in $1000). To achieve this, the company will issue $150,000 in
commercial paper in January, $49,020 in February and $203,434 in March.
In addition, it will draw $50,980 from its line of credit in February. Excess
cash of $351,944 in March will be invested for just one month. All this is
reported in the Adjustable Cells section of the report. For this particular
application, the Constraints section of the report does not contain anything
useful. On the other hand, very useful information can be found in the
sensitivity report. This will be discussed in Section 3.3.


Exercise 3.5 Formulate and solve the variation of the short-term financing problem you developed in Exercise 3.1 using SOLVER. Interpret the
solution.


Exercise 3.6 Recall Example 2.1. Solve the problem using your favorite
linear programming solver. Compare the output provided by the solver to
the solution we obtained in Chapter 2.


3.1.4 Modeling Languages


Linear programs can be formulated using modeling languages such as AMPL,
GAMS, MOSEL or OPL. The need for these modeling languages arises because the Excel spreadsheet format becomes inadequate when the size of the
linear program increases. A modeling language lets people use common notation and familiar concepts to formulate optimization models and examine
solutions. Most importantly, large problems can be formulated in a compact
way. Once the problem has been formulated using a modeling language, it
can be solved using any number of solvers. A user can switch between solvers
with a single command and select options that may improve solver performance. The short term financing model would be formulated as follows (all
variables are assumed to be nonnegative unless otherwise specified).


DATA
LET T=6 be the number of months to plan for
L(t) = Liability in month t=1,...,T
ratex = monthly interest rate on line of credit
ratey = 3-month interest rate on commercial paper
ratez = monthly interest rate on excess funds
VARIABLES
x(t) = Amount drawn from line of credit in month t
y(t) = Amount of commercial paper issued in month t
z(t) = Excess funds in month t
OBJECTIVE (Maximize wealth in June)
Max z(6)
CONSTRAINTS
Month(t=1:T): x(t) - (1+ratex)*x(t-1) + y(t) - (1+ratey)*y(t-3)
-z(t) +(1+ratez)*z(t-1) = L(t)
Month(t=1:T-1): x(t) < 100


3.1. SHORT TERM FINANCING 53


Boundary conditions on x: x(0)=x(6) =0
Boundary conditions on y: y(-2)=y(-1)=y(0)=y(4)=y(5)=y(6) =0
Boundary conditions on z: z(0) =0
END


Exercise 3.7 Formulate the linear program of Exercise 3.3 with one of the
modeling languages AMPL, GAMS, MOSEL or OPL.


3.1.5 Features of Linear Programs


Hidden in each linear programming formulation are a number of assumptions. The usefulness of an LP model is directly related to how closely reality
matches up with these assumptions.
The first two assumptions are due to the linear form of the objective
and constraint functions. The contribution to the objective of any decision
variable is proportional to the value of the decision variable. Similarly,
the contribution of each variable to the left hand side of each constraint
is proportional to the value of the variable. This is the Proportionality
Assumption.
Furthermore, the contribution of a variable to the objective and constraints is independent of the values of the other variables. This is the
Additivity Assumption. When additivity or proportionality assumptions are
not satisfied, a nonlinear programming model may be more appropriate. We
discuss such models in Chapters 5 and 6.
The next assumption is the Divisibility Assumption: is it possible to
take any fraction of any variable? A fractional production quantity may be
worrisome if we are producing a small number of battleships or be innocuous
if we are producing millions of paperclips. If the Divisibility Assumption is
important and does not hold, then a technique called integer programming
rather than linear programming is required. This technique takes orders
of magnitude more time to find solutions but may be necessary to create
realistic solutions. We discuss integer programming models and methods in
Chapters 11 and 12.
The final assumption is the Certainty Assumption: linear programming
allows for no uncertainty about the input parameters such as the cash-flow
requirements or interest rates we used in the short-term financing model.
Problems with uncertain parameters can be addressed using stochastic programming or robust optimization approaches. We discuss such models in
Chapters 16 through 20.
It is very rare that a problem will meet all of the assumptions exactly.
That does not negate the usefulness of a model. A model can still give
useful managerial insight even if reality differs slightly from the rigorous
requirements of the model.


Exercise 3.8 Give an example of an optimization problem where the proportionality assumption is not satisfied.


54CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


Exercise 3.9 Give an example of an optimization problem where the additivity assumption is not satisfied.


Exercise 3.10 Consider the LP model we develop for the cash-flow matching problem in Section 3.2. Which of the linear programming assumptions
used for this formulation is the least realistic one? Why?

#### 3.2 Dedication


Dedication or cash flow matching is a technique used to fund known liabilities
in the future. The intent is to form a portfolio of assets whose cash inflows
will exactly offset the cash outflows of the liabilities. The liabilities will
therefore be paid off, as they come due, without the need to sell or buy
assets in the future. The portfolio is formed today and then held until
all liabilities are paid off. Dedicated portfolios usually only consist of riskfree non-callable bonds since the portfolio future cash inflows need to be
known when the portfolio is constructed. This eliminates interest rate risk
completely. It is used by some municipalities and small pension funds. For
example, municipalities sometimes want to fund liabilities stemming from
bonds they have issued. These pre-refunded municipal bonds can be taken
off the books of the municipality. This may allow them to evade restrictive
covenants in the bonds that have been pre-refunded and perhaps allow them
to issue further debt.
It should be noted however that dedicated portfolios cost typically from
3% to 7% more in dollar terms than do “immunized” portfolios that are
constructed based on matching present value, duration and convexity of the
assets and of the liabilities. The present value of the liability stream Lt
Lt
for t = 1, . . ., T is P = [�][T] t=1 (1+rt�) [t] [,] [where] [r][t] [denotes] [the] [risk-free] [rate]

inP1 �yearTt=1 (1+tt.(t+1)rItst) [t] L [+2] t duration [.] [Intuitively,] is D [duration] = P1 Tt=1 [is] (1+ [the] tLrtt [average] ) [t] [and] [its][(discounted)][convexity] [time][is] [C] [at][=]

which the liabilities occur, whereas convexity, a bit like variance, indicates
how concentrated the cash flows are over time. For a portfolio that consists
only of risk-free bonds, the present value P [∗] of the portfolio future cash
inflows can be computed using the same risk-free rate rt (this would not be
the case for a portfolio containing risky bonds). Similarly for the duration
D [∗] and convexity C [∗] of the portfolio future cash inflows. An “immunized”
portfolio can be constructed based on matching P [∗] = P, D [∗] = D and
C [∗] = C. Portfolios that are constructed by matching these three factors are
immunized against parallel shifts in the yield curve, but there may still be
a great deal of exposure and vulnerability to other types of shifts, and they
need to be actively managed, which can be costly. By contrast, dedicated
portfolios do not need to be managed after they are constructed.
When municipalities use cash flow matching, the standard custom is to
call a few investment banks, send them the liability schedule and request
bids. The municipality then buys its securities from the bank that offers the
lowest price for a successful cash flow match.


3.2. DEDICATION 55


Assume that a bank receives the following liability schedule:

|Year 1|Year 2|Year 3|Year 4|Year 5|Year 6|Year 7|Year 8|
|---|---|---|---|---|---|---|---|
|12, 000|18, 000|20, 000|20, 000|16, 000|15, 000|12, 000|10, 000|



The bonds available for purchase today (Year 0) are given in the next
table. All bonds have a face value of $100. The coupon figure is annual. For
example, Bond 5 costs $98 today, and it pays back $4 in Year 1, $4 in Year
2, $4 in Year 3 and $104 in Year 4. All these bonds are widely available and
can be purchased in any quantities at the stated price.

|Bond|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|Price<br>Coupon<br>MaturityYear|102<br>5<br>1|99<br>3.5<br>2|101<br>5<br>2|98<br>3.5<br>3|98<br>4<br>4|104<br>9<br>5|100<br>6<br>5|101<br>8<br>6|102<br>9<br>7|94<br>7<br>8|



Formulate and solve a linear program to find the least cost portfolio of
bonds to purchase today, to meet the obligations of the municipality over
the next eight years. To eliminate the possibility of any reinvestment risk,
we assume a 0% reinvestment rate.


Using a modeling language, the formulation might look as follows.


DATA
LET T=8 be the number of years to plan for.
LET N=10 be the number of bonds available for purchase today.
L(t) = Liability in year t=1,...,T
P(i) = Price of bond i, i=1,...,N
C(i) = Annual coupon for bond i, i=1,...,N
M(i) = Maturity year of bond i, i=1,...,N
VARIABLES
x(i) = Amount of bond i in the portfolio
z(t) = Surplus at the end of year t, for t=0,...,T
OBJECTIVE (Minimize cost)
Min z(0) + SUM(i=1:N) P(i)*x(i)
CONSTRAINTS Year(t=1:T):
SUM(i=1:N | M(i) - t-1) C(i)*x(i) + SUM(i=1:N | M(i) = t) 100*x(i)
-z(t) + z(t-1) = L(t)
END


Exercise 3.11 Solve the dedication linear program above using an LP software package and verify that we can optimally meet the municipality’s liabilities for $93,944 with the following portfolio: 62 Bond1, 125 Bond3, 152
Bond4, 157 Bond5, 123 Bond6, 124 Bond8, 104 Bond9 and 93 Bond10.


56CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


Exercise 3.12 A small pension fund has the following liabilities (in million
dollars):

|Year1|Year2|Year3|Year4|Year5|Year6|Year7|Year8|Year9|
|---|---|---|---|---|---|---|---|---|
|24|26|28|28|26|29|32|33|34|



It would like to construct a dedicated bond portfolio. The bonds available for purchase are the following:

|Bond|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|Price<br>Coupon<br>MaturityYear|102.44<br>5.625<br>1|99.95<br>4.75<br>2|100.02<br>4.25<br>2|102.66<br>5.25<br>3|87.90<br>0.00<br>3|85.43<br>0.00<br>4|83.42<br>0.00<br>5|103.82<br>5.75<br>5|


|Bond|9|10|11|12|13|14|15|16|
|---|---|---|---|---|---|---|---|---|
|Price<br>Coupon<br>MaturityYear|110.29<br>6.875<br>6|108.85<br>6.5<br>6|109.95<br>6.625<br>7|107.36<br>6.125<br>7|104.62<br>5.625<br>8|99.07<br>4.75<br>8|103.78<br>5.5<br>9|64.66<br>0.00<br>9|



Formulate an LP that minimizes the cost of the dedicated portfolio,
assuming a 2% reinvestment rate. Solve the LP using your favorite software
package.

#### 3.3 Sensitivity Analysis for Linear Programming


The optimal solution to a linear programming model is the most important
output of LP solvers, but it is not the only useful information they generate.
Most linear programming packages produce a tremendous amount of sensitivity information, or information about what happens when data values
are changed.
Recall that in order to formulate a problem as a linear program, we had
to invoke a certainty assumption: we had to know what value the data took
on, and we made decisions based on that data. Often this assumption is
somewhat dubious: the data might be unknown, or guessed at, or otherwise
inaccurate. How can we determine the effect on the optimal decisions if the
values change? Clearly some numbers in the data are more important than
others. Can we find the “important” numbers? Can we determine the effect
of estimation errors?
Linear programming offers extensive capabilities for addressing these
questions. We give examples of how to interpret the SOLVER output. To
access the information in SOLVER, one can simply ask for the sensitivity
report after optimizing. Rather than simply giving rules for reading the
reports, we show how to answer a set of questions from the output.


3.3.1 Short Term Financing


The Solver sensitivity report looks as follows.


3.3. SENSITIVITY ANALYSIS FOR LINEAR PROGRAMMING 57


Adjustable Cells

Final Reduced Objective Allowable Allowable
Cell Name Value Cost Coefcient Increase Decrease
$B$2 x1 0 −0.0032 0 0.0032 1E + 30
$B$3 x2 50.98 0 0 0.0032 0
$B$4 x3 0 −0.0071 0 0.0071 1E + 30
$B$5 x4 0 −0.0032 0 0.0032 1E + 30
$B$6 x5 0 0 0 0 1E + 30
$C$2 y1 150 0 0 0.0040 0.0032
$C$3 y2 49.02 0 0 0 0.0032
$C$4 y3 203.43 0 0 0.0071 0
$D$2 z1 0 −0.0040 0 0.0040 1E + 30
$D$3 z2 0 −0.0071 0 0.0071 1E + 30
$D$4 z3 351.94 0 0 0.0039 0.0032
$D$5 z4 0 −0.0039 0 0.0039 1E + 30
$D$6 z5 0 −0.007 0 0.007 1E + 30
$E$2 v 92.50 0 1 1E + 30 1


Constraints

Final Shadow Constraint Allowable Allowable
Cell Name Value Price R.H.Side Increase Decrease
$B$10 January 150 −1.0373 150 89.17 150
$B$11 February 100 −1.030 100 49.020 50.980
$B$12 March −200 −1.020 −200 90.683 203.434
$B$13 April 200 −1.017 200 90.955 204.044
$B$14 May −50 −1.010 −50 50 52
$B$15 June −300 −1 −300 92.497 1E + 30
$B$16 x1 0 0 100 1E + 30 100
$B$17 x2 50.98 0 100 1E + 30 49.020
$B$18 x3 0 0 100 1E + 30 100
$B$19 x4 0 0 100 1E + 30 100
$B$20 x5 0 0 100 1E + 30 100


The key columns for sensitivity analysis are the Reduced Cost and
Shadow Price columns in SOLVER. The shadow price u of a constraint
C has the following interpretation:


If the right hand side of the constraint C changes by an amount ∆, the
optimal objective value changes by u∆, as long as the amount of change
∆is within the allowable range.


For a linear program, the shadow price u is an exact figure, as long
as the amount of change ∆is within the allowable range given in the last
two columns of the SOLVER output. When the change ∆falls outside this
range, the rate of change in the optimal objective value changes and the


58CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


shadow price u cannot be used. When this occurs, one has to resolve the
linear program using the new data.
Next, we consider several examples of sensitivity questions and demonstrate how they can be answered using shadow prices and reduced costs.


  - For example, assume that Net Cash Flow in January were -200 (instead
of    - 150). By how much would the company’s wealth decrease at the
end of June?


The answer is in the shadow price of the January constraint, u =
−1.0373. The RHS of the January constraint would go from 150 to
200, an increase of ∆= 50, which is within the allowable increase
(89.17). So the company’s wealth in June would decrease by 1.0373    50,000 = $ 51,865.


  - Now assume that Net Cash Flow in March were 250 (instead of 200).
By how much would the company’s wealth increase at the end of June?

Again, the change ∆= −50 is within the allowable decrease (203.434),
so we can use the shadow price u = −1.02 to calculate the change in
objective value. The increase is (-1.02)    - (-50) = $51,000.


  - Assume that the credit limit were increased from 100 to 200. By how
much would the company’s wealth increase at the end of June?


In each month, the change ∆= 100 is within the allowable increase
( +∞) and the shadow price for the credit limit constraint is u = 0.
So there is no effect on the company’s wealth in June. Note that
non-binding constraints–such as the credit limit constraint for months
January through May–always have zero shadow price.


  - Assume that the negative Net Cash Flow in January is due to the
purchase of a machine worth $150,000. The vendor allows the payment
to be made in June at an interest rate of 3% for the 5-month period.
Would the company’s wealth increase or decrease by using this option?
What if the interest rate for the 5-month period were 4%?


The shadow price of the January constraint is -1.0373. This means
that reducing cash requirements in January by $1 increases the wealth
in June by $1.0373. In other words, the break even interest rate for
the 5-month period is 3.73%. So, if the vendor charges 3%, we should
accept, but if he charges 4% we should not. Note that the analysis is
valid since the amount ∆= −150 is within the allowable decrease.

  - Now, let us consider the reduced costs. The basic variables always
have a zero reduced cost. The nonbasic variables (which by definition
take the value 0) have a nonpositive reduced cost and, frequently their
reduced cost is strictly negative. There are two useful interpretations
of the reduced cost c, for a nonbasic variable x.


First, assume that x is set to a positive value ∆instead of its optimal
value 0. Then, the objective value is changed by c∆. For example,


3.3. SENSITIVITY ANALYSIS FOR LINEAR PROGRAMMING 59


what would be the effect of financing part of the January cash needs
through the line of credit? The answer is in the reduced cost of variable
x1. Because this reduced cost -0.0032 is strictly negative, the objective
function would decrease. Specifically, each dollar financed through the
line of credit in January would result in a decrease of $0.0032 in the
company’s wealth v in June.


The second interpretation of c is that its magnitude |c| is the minimum
amount by which the objective coefficient of x must be increased in
order for the variable x to become positive in an optimal solution.
For example, consider the variable x1 again. Its value is zero in the
current optimal solution, with objective function v. However, if we
changed the objective to v + 0.0032x1, it would now be optimal to use
the line of credit in January. In other words, the reduced cost on x1
can be viewed as the minimum rebate that the bank would have to
offer (payable in June) to make it attractive to use the line of credit
in January.


Exercise 3.13 Recall Example 2.1. Determine the shadow price and reduced cost information for this problem using an LP software package. How
would the solution change if the average maturity of the portfolio is required
to be 3.3 instead of 3.6?


Exercise 3.14 Generate the sensitivity report for Exercise 3.2 with your
favorite LP solver.
(i) Suppose the cash requirement in Q2 is 300 (instead of 500). How
would this affect the wealth in Q9?
(ii) Suppose the cash requirement in Q2 is 100 (instead of 500). Can the
sensitivity report be used to determine the wealth in Q9?
(iii) One of the company’s suppliers may allow differed payments of $ 50
from Q3 to Q4. What would be the value of this?


Exercise 3.15 Workforce Planning: Consider a restaurant that is open
seven days a week. Based on past experience, the number of workers needed
on a particular day is given as follows:

|Day|Mon Tue Wed Thu Fri Sat Sun|
|---|---|
|Number|14<br>13<br>15<br>16<br>19<br>18<br>11|



Every worker works five consecutive days, and then takes two days off,
repeating this pattern indefinitely. How can we minimize the number of
workers that staff the restaurant?


Let the days be numbers 1 through 7 and let xi be the number of workers
who begin their five day shift on day i. The linear programming formulation
is as follows.


60CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


          Minimize i [x][i]
Subject to
x1 + x4 + x5 + x6 + x7 ≥ 14
x1 + x2 + x5 + x6 + x7 ≥ 13
x1 + x2 + x3 + x6 + x7 ≥ 15
x1 + x2 + x3 + x4 + x7 ≥ 16
x1 + x2 + x3 + x4 + x5 ≥ 19
x2 + x3 + x4 + x5 + x6 ≥ 18
x3 + x4 + x5 + x6 + x7 ≥ 11
xi 0 (for all i)
≥


Sensitivity Analysis The following table gives the sensitivity report for
the solution of the workforce planning problem.


Adjustable Cells
Final Reduced Objective Allowable Allowable
Cell Name Value Cost Coefficient Increase Decrease
$B$14 Shift1 4 0 1 0.5 1
$B$15 Shift2 7 0 1 0 0.333333
$B$16 Shift3 1 0 1 0.5 0
$B$17 Shift4 4 0 1 0.5 0
$B$18 Shift5 3 0 1 0 0.333333
$B$19 Shift6 3 0 1 0.5 1
$B$20 Shift7 0 0.333333 1 1E+30 0.333333


Constraints
Final Shadow Constraint Allowable Allowable
Cell Name Value Price R.H. Side Increase Decrease
$B$24 Monday 14 0.333333 14 1.5 6
$B$25 Tuesday 17 0 13 4 1E+30
$B$26 Wednesday 15 0.333333 15 6 3
$B$27 Thursday 16 0 16 3 4
$B$28 Friday 19 0.333333 19 4.5 3
$B$29 Saturday 18 0.333333 18 1.5 6
$B$30 Sunday 11 0 11 4 1


Answer each of the following questions independently of the others.


1. What is the current total number of workers needed to staff the restaurant?


3.3. SENSITIVITY ANALYSIS FOR LINEAR PROGRAMMING 61


2. Due to a special offer, demand on Thursdays increases. As a result,
18 workers are needed instead of 16. What is the effect on the total
number of workers needed to staff the restaurant?


3. Assume that demand on Mondays decreases: 11 workers are needed
instead of 14. What is the effect on the total number of workers needed
to staff the restaurant?


4. Every worker in the restaurant is paid $1000 per month. So the objective function in the formulation can be viewed as total wage expenses
(in thousand dollars). Workers have complained that Shift 4 is the
least desirable shift. Management is considering increasing the wages
of workers on Shift 4 to $1100. Would this change the optimal solution? What would be the effect on total wage expenses?


5. Shift 2, on the other hand, is very desirable (Sundays off while on duty
Fridays and Saturdays, which are the best days for tips). Management
is considering reducing the wages of workers on Shift 1 to $900 per
month. Would this change the optimal solution? What would be the
effect on total wage expenses?


6. Management is considering introducing a new shift with the days off
on Tuesdays and Sundays. Because these days are not consecutive,
the wages will be $1200 per month. Will this increase or reduce the
total wage expenses?


3.3.2 Dedication


We end this section with the sensitivity report of the dedication problem
formulated in Section 3.2.


62CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


Adjustable Cells

Final Reduced Objective Allowable Allowable
Cell Name Value Cost Coefcient Increase Decrease
$B$5 x1 62.13612744 0 102 3 5.590909091
$B$6 x2 0 0.830612245 99 1E + 30 0.830612245
$B$7 x3 125.2429338 0 101 0.842650104 3.311081442
$B$8 x4 151.5050805 0 98 3.37414966 4.712358277
$B$9 x5 156.8077583 0 98 4.917243419 17.2316607
$B$10 x6 123.0800686 0 104 9.035524153 3.74817022
$B$11 x7 0 8.786840002 100 1E + 30 8.786840002
$B$12 x8 124.1572748 0 101 3.988878399 8.655456271
$B$13 x9 104.0898568 0 102 9.456887408 0.860545483
$B$14 x10 93.45794393 0 94 0.900020046 1E + 30
$H$4 z0 0 0.028571429 1 1E + 30 0.028571429
$H$5 z1 0 0.055782313 0 1E + 30 0.055782313
$H$6 z2 0 0.03260048 0 1E + 30 0.03260048
$H$7 z3 0 0.047281187 0 1E + 30 0.047281187
$H$8 z4 0 0.179369792 0 1E + 30 0.179369792
$H$9 z5 0 0.036934059 0 1E + 30 0.036934059
$H$10 z6 0 0.086760435 0 1E + 30 0.086760435
$H$11 z7 0 0.008411402 0 1E + 30 0.008411402
$H$12 z8 0 0.524288903 0 1E + 30 0.524288903


Constraints

Final Shadow Constraint Allowable Allowable
Cell Name Value Price R.H.Side Increase Decrease
$B$19 year1 12000 0.971428571 12000 1E + 30 6524.293381
$B$20 year2 18000 0.915646259 18000 137010.161 13150.50805
$B$21 year3 20000 0.883045779 20000 202579.3095 15680.77583
$B$22 year4 20000 0.835764592 20000 184347.1716 16308.00686
$B$23 year5 16000 0.6563948 16000 89305.96314 13415.72748
$B$24 year6 15000 0.619460741 15000 108506.7452 13408.98568
$B$25 year7 12000 0.532700306 12000 105130.9798 11345.79439
$B$26 year8 10000 0.524288903 10000 144630.1908 10000


Exercise 3.16 Analyze the solution tables above and


  - Interpret the shadow price in year t (t = 1, . . ., 8)

  - Interpret the reduced cost of bond i (i = 1, . . ., 10)

Interpret the reduced cost of each surplus variable zt (t = 0, . . ., 7)

  

Answers:


  - The shadow price in Year t is the cost of the bond portfolio that can
be attributed to a dollar of liability in Year t. For example, each dollar


3.3. SENSITIVITY ANALYSIS FOR LINEAR PROGRAMMING 63


of liability in Year 3 is responsible for $ 0.883 in the cost of the bond
portfolio. Note that, by setting the shadow price in Year t equal to
(1+1rt) [t] [,] [we] [get] [a] [term] [structure] [of] [interest rates.] [Here] [r][3] [= 0][.][0423.] [In]
Figure 3.3.2 we plot the term structure of interest rates we compute
from this solution. How does this compare with the term structure of
Treasury rates?



10


9


8


7


6


5


4


3



Term structure of interest rates implied by the cash−flow matching example



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-62-0.png)

2
1 2 3 4 5 6 7 8

Maturity (years)



Figure 3.1: Interest rates implied by shadow prices


  - The reduced cost of bond i indicates by how much bond i is overpriced
for inclusion in the optimal portfolio. For example, bond 2 would have
to be $ 0.83 lower, at $ 98.17, for inclusion in the optimal portfolio.


Exercise 3.17 Note that the optimal solution has no holdings in
Bond 7 which matures in Year 5, despite the $16,000 liability in Year
5. This is likely due to a mispricing of this bond at $100. What would
be a more realistic price for this bond?


Answer: Row 7 of the “Adjustable Cells” table indicates that variable
x7, corresponding to Bond 7 holdings, will become positive only if the
price is reduced by 8.786 or more. So, a more realistic price for this
bond would be just above $91. By checking the reduced costs, one
may sometimes spot errors in the data!


The reduced cost of the surplus variable zt indicates what the interest

  rate on cash reinvested in Year t would have to be in order to keep
excess cash in Year t.


Exercise 3.18 Generate the sensitivity report for Exercise 3.12.


64CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


(i) Suppose that the liability in Year 3 is 29 (instead of 28). What would
be the increase in cost of the dedicated portfolio?
(ii) Draw a graph of the term structure of interest rates implied by the
shadow prices.
(iii) Bond 4 is not included in the optimal portfolio. By how much would
the price of Bond 4 have to decrease for Bond 4 to become part of the optimal
portfolio?
(iv) The fund manager would like to have 10000 units of Bond 3 in the
portfolio. By how much would this increase the cost of the portfolio?
(v) Is there any bond that looks badly mispriced?
(vi) What interest rate on cash would make it optimal to include cash
as part of the optimal portfolio?

#### 3.4 Case Study


We are currently in year i. A municipality sends you the following liability
stream (in million dollars) in years i + 1 to i + 8:

|6/15/i + 1|12/15/i + 1|6/15/i + 2|12/15/i + 2|6/15/i + 3|12/15/i + 3|
|---|---|---|---|---|---|
|6|6|9|9|10|10|


|6/15/i + 4|12/15/i + 4|6/15/i + 5|12/15/i + 5|6/15/i + 6|12/15/i + 6|
|---|---|---|---|---|---|
|10|10|8|8|8|8|


|6/15/i + 7|12/15/i + 7|6/15/i + 8|12/15/i + 8|
|---|---|---|---|
|6|6|5|5|



Your job:


  - Value the liability using the Treasury curve.

  - Identify between 30 and 50 assets that are suitable for a dedicated
portfolio (non-callable bonds, treasury bills or notes). Explain why
they are suitable. You can find current data on numerous web sites
such as www.bondsonline.com


  - Set up a linear program to identify a lowest cost dedicated portfolio
of assets (so no short selling) and solve with Excel’s solver (or any
other linear programming software that you prefer). What is the cost
of your portfolio? Discuss the composition of your portfolio. Discuss
the assets and the liabilities in light of the Sensitivity Report. What
is the term structure of interest rates implied by the shadow prices?
Compare with the term structure of Treasury rates. (Hint: refer to
Section 3.3.2.)


3.4. CASE STUDY 65


  - Set up a linear program to identify a lowest cost portfolio of assets (no
short selling) that matches present value, duration and convexity (or
a related measure) between the liability stream and the bond portfolio. Solve the linear program with your favorite software. Discuss the
solution. How much would you save by using this immunization strategy instead of dedication? Can you immunize the portfolio against
nonparallel shifts of the yield curve? Explain.


  - Set up a linear program to identify a lowest cost portfolio of assets (no
short selling) that combines a cash matching strategy for the liabilities
in the first 3 years and an immunization strategy based on present
value, duration and convexity for the liabilities in the last 5 years.
Compare the cost of this portfolio with the cost of the two previous
portfolios.


  - The municipality would like you to make a second bid: what is your
lowest cost dedicated portfolio of riskfree bonds if short sales are allowed? Discuss the feasibility of your solution.


66CHAPTER 3. LP MODELS: ASSET/LIABILITY CASH FLOW MATCHING


## Chapter 4

# LP Models: Asset Pricing and Arbitrage

#### 4.1 Derivative Securities and The Fundamental The- orem of Asset Pricing

One of the most widely studied problems in financial mathematics is the
pricing of derivative securities, also known as contingent claims. These are
securities whose price depends on the value of another underlying security.
Financial options are the most common examples of derivative securities.
For example, a European call option gives the holder the right to purchase
an underlying security for a prescribed amount (called the strike price) at a
prescribed time in the future, known as the expiration or exercise date. The
exercise date is also known as the maturity date of the derivative security.
Recall the similar definitions of European put options as well as American
call and put options from Section 1.3.2.
Options are used mainly for two purposes: speculation and hedging. By
speculating on the direction of the future price movements of the underlying security, investors can take (bare) positions in options on this security.
Since options are often much cheaper than their underlying security, this bet
results in much larger earnings in relative terms if the price movements happen in the expected direction compared to what one might earn by taking
a similar position in the underlying. Of course, if one guesses the direction
of the price movements incorrectly, the losses are also much more severe.
The more common and sensible use of options is for hedging. Hedging
refers to the reduction of risk in an investor’s overall position by forming
a suitable portfolio of assets that are expected to have opposing risks. For
example, if an investor holds a share of XYZ and is concerned that the price
of this security may fall significantly, she can purchase a put option on XYZ
and protect herself against price levels below a certain threshold–the strike
price of the put option.
Recall the option example in the simple one-period binomial model of
Section 1.3.2. Below, we summarize some of the information from that
example:


67


68 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE


We consider the share price of XYZ stock which is currently valued at
$40. A month from today, we expect the share price of XYZ to either double
or halve, with equal probabilities. We also consider a European call option
on XYZ with a strike price of $50 which will expire a month from today.
The payoff function for the call is shown in Figure 4.1.



70


60


50


40


30


20


10


0



European call option payoff function



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-67-0.png)

−10
−10 10 30 50 70 90 110 120

Share price of XYZ



Figure 4.1: Piecewise linear payoff function for a call option


We assume that interest rates for cash borrowing or lending are zero and
that any amount of XYZ shares can be bought or sold with no commission.



(80 − 50) [+] = 30

(20 − 50) [+] = 0



S0=$40 HHH [���] j*



80=20=SS11((ud)) and C0=? [���] HHH*j



In Section 1.3.2 we obtained a fair price of $10 for the option using a
replication strategy and the no-arbitrage principle. Two portfolios of securities that have identical future payoffs under all possible realizations of the
random states must have the same value today. In the example, the first
portfolio is the option while the second one is the portfolio of [1]

2 [share of XYZ]
and -$10 in cash. Since we know the current value of the second portfolio,
we can deduce the fair price of the option. To formalize this approach, we
first give a definition of arbitrage:


Definition 4.1 An arbitrage is a trading strategy


  - that has a positive initial cash flow and has no risk of a loss later (type
A), or


  - that requires no initial cash input, has no risk of a loss, and a positive
probability of making profits in the future (type B).


4.1. THE FUNDAMENTAL THEOREM OF ASSET PRICING 69


In the example, any price other than $10 for the call option would lead
to a type A arbitrage–guaranteed profits at the initial time point and no
future obligations. We do not need to have a guarantee of profits for type B
arbitrage–all we need is a guarantee of no loss, and a positive probability of
a gain. Prices adjust quickly so that arbitrage opportunities cannot persist
in the markets. Therefore, in pricing arguments it is often assumed that
arbitrage opportunities do not exist.


4.1.1 Replication


In the above example, we formulated and solved the following question to
determine the fair price of an option: Can we form a portfolio of the underlying security (long or short) and cash (borrowed or lent) today, such that
the payoff of the portfolio at the expiration date of the option will match
the payoff of the option? In other words, can we replicate the option using
a portfolio of the underlying security and cash?
Let us work in a slightly more general setting. Let S0 be the current price
of the underlying security and assume that there are two possible outcomes
at the end of the period: S1 [u] [=] [S][0][ ·][ u] [and] [S] 1 [d] [=] [S][0][ ·][ d][.] [Assume] [u] [>] [d][.] [We]
also assume that there is a fixed interest rate of r on cash positions for the
given period. Let R = 1 + r.
Now we consider a derivative security which has payoffs of C1 [u] [and] [C] 1 [d]
in the up and down states respectively:



S0 [���] 


S1 [u] [=][ S][0][ ·][ u]



C1 [u]



HHHj



S1 [d] [=][ S][0][ ·][ d] C0 =? [���] HHH*j



HHHj



jS1 [d] [=][ S][0][ ·][ d] jC1 [d]

To price the derivative security, we will replicate its payoff. For replication consider a portfolio of ∆shares of the underlying and $B cash. For
what values of ∆and B does this portfolio have the same payoffs at the
expiration date as the derivative security?
In the “up” state, the replicating portfolio will have value ∆S0 u + BR
                                                         and in the “down” state it will be worth ∆S0 d + BR. Therefore, for perfect

                                   replication, we need to solve the following simple system of equations:



∆S0 u + BR = C1 [u]
                         ∆S0 · d + BR = C1 [d][.]

We obtain:

∆ = C1 [u] 1

[−] [C][d]
S0(u d)
                  
B = uC1 [d] 1

[−] [dC][u]
R(u d) [.]
                  
Since this portfolio is worth S0∆+ B today, that should be the price of the
derivative security as well:

C0 = C1 [u] [−] [C] 1 [d] + [uC] 1 [d] [−] [dC] 1 [u]
u − d R(u − d)


70 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE



1
=
R




- R − d 1 [+] [u][ −] [R] 1 .
u d [C][u] u d [C][d]
  -  


4.1.2 Risk-Neutral Probabilities


Let




[R][ −] [d] and pd = [u][ −] [R]

u − d u − d



pu = [R][ −] [d]



u d [.]
 


Note that we must have d < R < u to avoid arbitrage opportunities as
indicated in the following simple exercise.



Exercise 4.1 Let S0 be the current price of a security and assume that
there are two possible prices for this security at the end of the current
period: S1 [u] [=] [S][0] [·][ u] [and] [S] 1 [d] [=] [S][0] [·][ d][.] [(Assume] [u] [>] [d][.)] [Also] [assume] [that]
there is a fixed interest rate of r on cash positions for the given period. Let
R = 1 + r. Show that there is an arbitrage opportunity if u > R > d is not
satisfied.


An immediate consequence of this observation is that both pu  - 0 and
pd - 0. Noting also that pu +pd = 1 one can interpret pu and pd as probabilities. In fact, these are the so-called risk-neutral probabilities (RNPs) of up
and down states, respectively. Note that they are completely independent
from the physical probabilities of these states.
The price of any derivative security can now be calculated as the present
value of the expected value of its future payoffs where the expected value is
taken using the risk-neutral probabilities.
In our example above u = 2, d = [1] [r] [= 0] [so] [that] [R][ = 1.] [Therefore:]

2 [and]



pu = [1][ −] [1][/][2]




[1] and pd = 2 − 1 [2]

3 2 − 1/2 [=] 3



3 [.]




[1][ −] [1][/][2] [1]

2 − 1/2 [=] 3



As a result, we have



1
S0 = 40 = 1 [+][ p][d][S] 1 [d][) =] [1]
R [(][p][u][S][u] 3

1
C0 = 10 = 1 [+][ p][d][C] 1 [d][) =] [1]
R [(][p][u][C][u] 3




[1] [2]

3 [80 +] 3

[1] [2]

3 [30 +] 3



3 [0][,]



3 [20][,]



as expected. Using risk neutral probabilities we can also price other derivative securities on the XYZ stock. For example, consider a European put
option on the XYZ stock struck at $60 and with the same expiration date
as the call of the example.



We can easily compute:



*P1 [u] [= max][{][0][,][ 60][ −] [80][}][ = 0]
P0 =? [���] HHHjP1 [d] [= max][{][0][,][ 60][ −] [20][}][ = 40]



1
P0 = 1 [+][ p][d][P][ d] 1 [) =] [1]
R [(][p][u][P][ u] 3




[1] [2]

3 [0 +] 3




[2] [80]

3 [40 =] 3



3 [,]



without needing to replicate the option again.


4.1. THE FUNDAMENTAL THEOREM OF ASSET PRICING 71


Exercise 4.2 Compute the price of a binary (digital) call option on the
XYZ stock that pays $1 if the XYZ price is above the strike price of $50.


Exercise 4.3 Assume that the XYZ stock is currently priced at $40. At
the end of the next period, the XYZ price is expected to be in one of the
following two states: S0 u or S0 d. We know that d < 1 < u but do not
                   -                   know d or u. The interest rate is zero. If a European call option with strike
price $50 is priced at $10 while a European call option with strike price $40
is priced at $13. If we assume that these prices do not contain any arbitrage
opportunities, what is the fair price of a European put option with a strike
price of $40?
Hint: First note that u - [5] 4 [–otherwise] [the] [first] [call] [would] [be] [worthless.]

Then we must have 10 = pu(S0 u 50) and 13 = pu(S0 u 40). From

                          -                          -                          -                          these equations determine pu and then u and d.


Exercise 4.4 Assume that the XYZ stock is currently priced at $40. At
the end of the next period, the XYZ price is expected to be in one of the
following two states: S0 u or S0 d. We know that d < 1 < u but do not
                   -                   know d or u. The interest rate is zero. European call options on XYZ with
strike prices of $30, $40, $50, and $60 are priced at $10, $7, $ [10] [and] [$0.]

3 [,]
Which one of these options is mispriced? Why?


Remark 4.1 Exercises 4.3 and 4.4 are much simplified and idealized examples of the pricing problems encountered by practitioners. Instead of a
set of possible future states for prices which may be difficult to predict, they
must work with a set of market prices for related securities. Then, they must
extrapolate prices for an unpriced security using no-arbitrage arguments.


Next we move from our binomial setting to a more general setting and
let
Ω= ω1, ω2, . . ., ωm (4.1)
{ }

be the (finite) set of possible future “states”. For example, these could be
prices for a security at a future date.
For securities S [i], i = 0 . . . n, let S1 [i] [(][ω][j][)] [denote] [the] [price] [of] [this] [security]
in state ωj at time 1. Also let S0 [i] [denote the current (time 0) price of security]
S [i] . We use i = 0 for the “riskless” security that pays the interest rate r ≥ 0
between time 0 and time 1. It is convenient to assume that S0 [0] [= 1 and that]
S1 [0][(][ω][j][) =][ R][ = 1 +][ r,][ ∀][j][.]


Definition 4.2 A risk-neutral probability measure on the set Ω= ω1, ω2, . . ., ωm
{ }
is a vector of positive numbers (p1, p2, . . ., pm) such that


�m

pj = 1
j=1


and for every security S [i], i = 0, . . ., n,











 = [1] ˆE[S1 [i] []][.]

R



S0 [i] [=] [1]

R



�m




pjS1 [i] [(][ω][j][)]
j=1


72 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE


Above, E [ˆ] [S] denotes the expected value of the random variable S under
the probability distribution (p1, p2, . . ., pm).


4.1.3 The Fundamental Theorem of Asset Pricing


In this section we state the first fundamental theorem of asset pricing and
prove it for finite Ω. This proof is a simple exercise in linear programming
duality that also utilizes the following well-known result of Goldman and
Tucker on the existence of strictly complementary optimal solutions of LPs:


Theorem 4.1 (Goldman and Tucker [30]) When both the primal and
dual linear programming problems


( ) minx c [T] x
LP
Ax = b (4.2)
x ≥ 0

and
( ) maxy b [T] y
LD (4.3)
A [T] y ≤ c,

have feasible solutions, they have optimal solutions satisfying strict complementarity, i.e., there exist x [∗] and y [∗] optimal for the respective problems
such that
x [∗] + (c − A [T] y [∗] ) > 0.

Now, we are ready to prove the following theorem:


Theorem 4.2 (The First Fundamental Theorem of Asset Pricing)
A risk-neutral probability measure exists if and only if there is no arbitrage.


Proof:
We provide the proof for the case when the state space Ωis finite and is
given by (4.1). We assume without loss of generality that every state has
a positive probability of occuring (since states that have no probability of
occuring can be removed from Ω.) Given the current prices S0 [i] [and the future]
prices S1 [i] [(][ω][j][)] [in] [each] [state] [ω][j][,] [for] [securities] [0] [to] [n][,] [consider] [the] [following]
linear program with variables xi, for i = 0, . . ., n:

      minx �ni=0 [S] ni=01 [i] [(][ω][S][j] 0 [)][i] [x][x][i][i] ≥ 0, j = 1, . . ., m. (4.4)

Note that type-A arbitrage corresponds to a feasible solution to this LP with
a negative objective value. Since x = (x1, . . ., xn) with xi = 0, i is a feasible
∀
solution, the optimal objective value is always non-positive. Furthermore,
since all the constraints are homogeneous, if there exists a feasible solution
such that [�] S0 [i] [x][i] [<][ 0 (this corresponds to type-A arbitrage), the problem is]
unbounded. In other words, there is no type-A arbitrage if and only if the
optimal objective value of this LP is 0.
Suppose that there is no type-A arbitrage. Then, there is no type-B
arbitrage if and only if all constraints are tight for all optimal solutions of


4.2. ARBITRAGE DETECTION USING LINEAR PROGRAMMING 73


(4.4) since every state has a positive probability of occuring. Note that these
solutions must have objective value 0.
Consider the dual of (4.4):


       maxp       - mj=1 [0][p][j]
mj=1 [S] 1 [i] [(][ω][j][)][p][j] = S0 [i] [,] i = 0, . . ., n, (4.5)
pj 0, j = 1, . . ., m.
≥


Since the dual objective function is constant at zero for all dual feasible
solutions, any dual feasible solution is also dual optimal.
When there is no type-A arbitrage, (4.4) has an optimal solution. Now,
Theorem 2.2–Strong Duality Theorem–indicates that the dual must have
a feasible solution. If there is no type-B arbitrage either, Goldman and
Tucker’s theorem indicates that there exists a feasible and therefore optimal
dual solution p [∗] such that p [∗] - 0. This follows from strict complementarity
with primal constraints [�][n] i=1 [S] 1 [i] [(][ω][j][)][x][i] [≥] [0] [which] [are] [tight.] [From] [the] [dual-]
nconstraint corresponding to i = 0, we have that [�][m] j=1 [p] j [∗] [=] R [1] [.] [Multiplying]

p [∗] by R one obtains a risk-neutral probability distribution. Therefore, the
“no arbitrage” assumption implies the existence of RNPs.
The converse direction is proved in an identical manner. The existence
of a RNP measure implies that (4.5) is feasible, and therefore its dual,
(4.4) must be bounded, which implies that there is no type-A arbitrage.
Furthermore, since we have a strictly feasible (and optimal) dual solution,
any optimal solution of the primal must have tight constraints, indicating
that there is no type-B arbitrage.

#### 4.2 Arbitrage Detection Using Linear Program- ming


The linear programming problems (4.4) and (4.5) formulated in the proof of
Theorem 4.2 can naturally be used for detection of arbitrage opportunities.
However, as we discussed above, this argument works only for finite state
spaces. In this section, we discuss how LP formulations can be used to
detect arbitrage opportunities without limiting consideration to finite state
spaces. The price we pay for this flexibility is the restriction on the selection
of the securities: we only consider the prices of a set of derivative securities
written on the same underlying with same maturity. This discussion is based
on Herzel [38].
Consider an underlying security with a current, time 0, price of S0 and a
random price S1 at time 1. Consider n derivative securities written on this
security that mature at time 1, and have piecewise linear payoff functions
Ψi(S1), each with a single breakpoint Ki, for i = 1, . . ., n. The obvious
motivation is the collection of calls and puts with different strike prices
written on this security. If, for example, the i-th derivative security were
a European call with strike price Ki, we would have Ψi(S1) = (S1 Ki) [+] .
                            We assume that the Kis are in increasing order, without loss of generality.
Finally, let S0 [i] [denote] [the] [current] [price] [of] [the] [i][-th] [derivative] [security.]


74 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE


Consider a portfolio x = (x1, . . ., xn) of the derivative securities 1 to n
and let Ψ [x] (S1) denote the payoff function of the portfolio:



Ψ [x] (S1) :=



�n

Ψi(S1)xi. (4.6)
i=1



The cost of forming the portfolio x at time 0 is given by


�n

S0 [i] [x][i][.] (4.7)
i=1


To determine whether a static arbitrage opportunity exists in the current
prices S0 [i] [, we consider the following problem:] [What is the cheapest portfolio]
of the derivative securities 1 to n whose payoff function Ψ [x] (S1) is nonnegative for all S1 [0, )? Non-negativity of Ψ [x] (S1) corresponds to “no future
∈ ∞
obligations” part of the arbitrage definition. If the minimum initial cost of
such a portfolio is negative, then we have a type-A arbitrage.
Since all Ψi(S1)s are piecewise linear, so is Ψ [x] (S1). It will have up to
n breakpoints at points K1 through Kn. Observe that a piecewise linear
function is nonnegative over [0, ∞) if and only if it is nonnegative at 0 and
at all the breakpoints, and if the slope of the function is nonnegative to the
right of the largest breakpoint. From our notation, Ψ [x] (S1) is nonnegative
for all non-negative values of S1 if and only if

1. Ψ [x] (0) ≥ 0,

2. Ψ [x] (Kj) 0, j,
≥ ∀

3. and [(Ψ [x] ) [′] + [(][K][n][)]][ ≥] [0.]


Now consider the following linear programming problem:




       minx - ni=1 [S] 0 [i] [x][i]
�ni=1 [(Ψ][i][(][K][n][ + 1)]    - [ −] ni=1ni [Ψ] =1 [Ψ][i][(][Ψ][i][K][(][K][i][n][(0)][j][))][)][x][x][x][i][i][i] ≥≥ 000, j = 1, . . ., n
≥



(4.8)



Since all Ψi(S1)’s are piecewise linear, the quantity Ψi(Kn + 1) Ψi(Kn)
                           gives the right-derivative of Ψi(S1) at Kn. Thus, the expression in the last
constraint is the right derivative of Ψ [x] (S1) at Kn. The following observation
follows from our arguments above:


Proposition 4.1 There is no type-A arbitrage in prices S0 [i] [if] [and] [only] [if]
the optimal objective value of (4.8) is zero.


Similar to the previous section, we have the following result:


Proposition 4.2 Suppose that there are no type-A arbitrage opportunities
in prices S0 [i] [.] [Then,] [there] [are] [no] [type-B] [arbitrage] [opportunities] [if] [and] [only]
if the dual of the problem (4.8) has a strictly feasible solution.


4.2. ARBITRAGE DETECTION USING LINEAR PROGRAMMING 75


Exercise 4.5 Prove Proposition 4.2.


Next, we focus on the case where the derivative securities under consideration are European call options with strikes at Ki for i = 1, . . ., n, so that
Ψi(S1) = (S1 Ki) [+] . Thus
      
Ψi(Kj) = (Kj Ki) [+] .

            

In this case, (4.8) reduces to the following problem:


minx c [T] x
(4.9)
Ax ≥ 0,

       -        where c [T] = S01 [,] [. . ., S] 0 [n] and



K2 K1 0 0 0
 -  - · ·
K3 K1 K3 K2 0 0
 -  -  - · ·
... ... ... ... ...
Kn K1 Kn K2 Kn K3 0
  -  -  -  - · ·
1 1 1  - · · 1






. (4.10)




A =









This formulation is obtained by removing the first two constraints of (4.8)
which are redundant in this particular case.
Using this formulation and our earlier results, one can prove a theorem
giving necessary and sufficient conditions for a set of call option prices to
contain arbitrage opportunities:


Theorem 4.3 Let K1 < K2 < < Kn denote the strike prices of Eu
                               - · ·
ropean call options written on the same underlying security with the same
maturity. There are no arbitrage opportunities if and only if the prices S0 [i]
satisfy the following conditions:


1. S0 [i] [>][ 0][,] [i][ = 1][, . . ., n]

2. S0 [i] [> S] 0 [i][+1], i = 1, . . ., n − 1

3. The function C(Ki) := S0 [i] [defined] [on] [the] [set] [{][K][1][, K][2][, . . ., K][n][}] [is] [a]
strictly convex function.


Exercise 4.6 Use Proposition 4.2 to show that there are no arbitrage opportunities for the option prices in Theorem 4.3 if and only if there exists strictly positive scalars y1, . . ., yn satisfying yn = S0 [n][,] [y][n][−][1] [=] [(][S] 0 [n][−][1] S0 [n][)][/][(][K][n][ −] [K][n][−][1][),] [and]

yi = [S] 0 [i] [−] [S] 0 [i][+1] 0        - S0 [i][+2] [, i][ = 1][, . . ., n][ −] [2][.]
K [i][+1] K [i] K [i][+2] K [i][+1]

[−] [S][i][+1]

       -       
Use this observation to prove Theorem 4.3


76 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE





Convexity violation



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-75-0.png)

Strike Price



Figure 4.2: Nonconvexity in the call price function indicates arbitrage


As an illustration of Theorem 4.3, consider the scenario in Exercise 4.4:
XYZ stock is currently priced at $40. European call options on XYZ with
strike prices of $30, $40, $50, and $60 are priced at $10, $7, $ [10] [and] [$0.]

3 [,]
Do these prices exhibit an arbitrage opportunity? As we see in Figure 4.2,
the option prices violate the third condition of the Theorem and therefore
must carry an arbitrage opportunity.


Exercise 4.7 Construct a portfolio of the options in the example above
that provides a type-A arbitrage opportunity.

#### 4.3 Additional Exercises


Exercise 4.8 Consider the linear programming problem (4.9) that we developed to detect arbitrage opportunities in the prices of European call options with a common underlying security and common maturity (but different strike prices). This formulation implicitly assumes that the i [th] call can
be bought or sold at the same current price of S0 [i] [.] [In] [real] [markets,] [there] [is]
always a gap between the price a buyer pays for a security and the amount
the seller collects called the bid-ask spread.
Assume that the ask price of the i [th] call is given by Sa [i] [while] [its] [bid]
price is denoted by Sb [i] [with] [S] a [i] [>] [S] b [i][.] [Develop] [an] [analogue] [of] [the] [LP] [(4.9)]
in the case where we can purchase the calls at their ask prices or sell them
at their bid prices. Consider using two variables for each call option in your
new LP.


Exercise 4.9 Consider all the call options on the S&P 500 index that expire on the same day, about three months from the current date. Their


4.3. ADDITIONAL EXERCISES 77


current prices can be downloaded from the website of the Chicago Board of
Options Exchange at www.cboe.com or several other market quote websites.
Formulate the linear programming problem (4.9) (or, rather the version
you developed for Exercise 4.8 since market quotes will include bid and ask
prices) to determine whether these prices contain any arbitrage opportunities. Solve this linear programming problem using an LP software.
Sometimes, illiquid securities can have misleading prices since the reported price corresponds to the last transaction in that security which may
have happened several days ago, and if there were to be a new transaction,
this value would change dramatically. As a result, it is quite possible that
you will discover false “arbitrage opportunities” because of these misleading
prices. Repeat the LP formulation and solve it again, this time only using
prices of the call options that have had a trading volume of at least 100 on
the day you downloaded the prices.


Exercise 4.10 (i) You have $20,000 to invest. Stock XYZ sells at $20 per
share today. A European call option to buy 100 shares of stock XYZ at $15
exactly six months from today sells for $1000. You can also raise additional
funds which can be immediately invested, if desired, by selling call options
with the above characteristics. In addition, a 6-month riskless zero-coupon
bond with $100 face value sells for $90. You have decided to limit the
number of call options that you buy or sell to at most 50.
You consider three scenarios for the price of stock XYZ six months from
today: the price will be the same as today, the price will go up to $40, or
drop to $12. Your best estimate is that each of these scenarios is equally
likely. Formulate and solve a linear program to determine the portfolio of
stocks, bonds, and options that maximizes expected profit.


Answer: First, we define the decision variables.
B = number of bonds purchased,
S = number of shares of stock XYZ purchased,
C = number of call options purchased (if  - 0) or sold (if < 0).


The expected profits (per unit of investment) are computed as follows.



Bonds: 10
Stock XYZ: [1]



Stock XYZ:

3 [(20 + 0][ −] [8) = 4]
Call Option: [1] [(1500] [500]



3 [(1500][ −] [500][ −] [1000) = 0]



Therefore, we get the following linear programming formulation.


max 10B + 4S
90B + 20S + 1000C ≤ 20000 (budget constraint)
C ≤ 50 (limit on number of call options purchased)
C ≥ −50 (limit on number of call options sold)
B ≥ 0, S ≥ 0 (nonnegativity).


Solving (using SOLVER, say), we get the optimal solution B = 0, S =
3500, C = -50 with an expected profit of $14,000.


78 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE


Note that, with this portfolio, the profit is not positive under all scenarios. In particular, if the price of stock XYZ goes to $40, a loss of $5000 will
be incurred.


(ii) Suppose that the investor wants a profit of at least $2000 in any of the
three scenarios. Write a linear program that will maximize the investor’s
expected profit under this additional constraint.


Answer: This can be done by introducing three additional variables.
Pi = profit in scenario i
The formulation is now the following.


max 1 + 1 + 1
3 [P][1] 3 [P][2] 3 [P][3]
90B + 20S + 1000C ≤ 20000
10B + 20S + 1500C = P1
10B 500C = P2

            10B 8S 1000C = P3

        -         P1 2000
≥
P2 2000
≥
P3 2000
≥
C ≤ 50
C ≥ −50
B ≥ 0, S ≥ 0.

(iii) Solve this linear program with SOLVER to find out the expected profit.


How does it compare with the earlier figure of $14,000?


Answer: The optimum solution is to buy 2,800 shares of XYZ and sell 36
call options. The resulting expected worth in six months will be $31,200.
Therefore, the expected profit is $11,200 (=$31,200 - 20,000).


(iv) Riskless profit is defined as the largest possible profit that a portfolio is
guaranteed to earn, no matter which scenario occurs. What is the portfolio
that maximizes riskless profit for the above three scenarios?


Answer: To solve this question, we can use a slight modification of the
previous model, by introducing one more variable.
Z = riskless profit.
Here is the formulation.


max Z
90B + 20S + 1000C ≤ 20000
10B + 20S + 1500C = P1
10B 500C = P2

            10B 8S 1000C = P3

        -         P1 Z
≥
P2 Z
≥
P3 Z
≥
C ≤ 50
C ≥ −50
B ≥ 0, S ≥ 0.


4.3. ADDITIONAL EXERCISES 79


The result is (obtained using SOLVER) a riskless profit of $7272. This
is obtained by buying 2,273 shares of XYZ and selling 25.45 call options.
The resulting expected profit is $9,091 in this case.


Exercise 4.11 Arbitrage in the Currency Market
Consider the global currency market. Given two currencies, say the Yen
and the USDollar, there is an exchange rate between them (about 118 Yens
to the Dollar in February 2006). It is axiomatic of arbitrage-free markets
that there is no method of converting, say, a Dollar to Yens then to Euros,
then Pounds, and to Dollars so that you end up with more than a dollar.
How would you recognize when there is an arbitrage opportunity?
The following are actual trades made on February 14, 2002.

|from|Col2|Dollar|Euro|Pound|Yen|
|---|---|---|---|---|---|
|into|Dollar<br>Euro<br>Pound<br>Yen|1.1486<br>.7003<br>133.38|.8706<br>.6097<br>116.12|1.4279<br>1.6401<br>190.45|.00750<br>.00861<br>.00525|



For example, one dollar converted into euros yielded 1.1486 euros. It is
not obvious from the chart above, but in the absence of any conversion costs,
the Dollar-Pound-Yen-Dollar conversion actually makes $0.0003 per dollar
converted while changing the order to Dollar-Yen-Euro-Dollar loses about
$0.0002 per dollar converted. How can one formulate a linear program to
identify such arbitrage possibilities?


Answer:
VARIABLES
DE = quantity of dollars changed into euros
DP = quantity of dollars changed into pounds
DY = quantity of dollars changed into yens
ED = quantity of euros changed into dollars
EP = quantity of euros changed into pounds
EY = quantity of euros changed into yens
PD = quantity of pounds changed into dollars
PE = quantity of pounds changed into euros
PY = quantity of pounds changed into yens
YD = quantity of yens changed into dollars
YE = quantity of yens changed into euros
YP = quantity of yens changed into pounds
D = quantity of dollars generated through arbitrage
OBJECTIVE
Max D
CONSTRAINTS
Dollar: D + DE + DP + DY - 0.8706*ED - 1.4279*PD - 0.00750*YD =
1
Euro: ED + EP + EY - 1.1486*DE - 1.6401*PE - .00861*YE = 0


80 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE


Pound: PD + PE + PY - 0.7003*DP - 0.6097*EP - 0.00525*YP = 0
Yen: YD + YE + YP - 133.38*DY - 116.12*EY - 190.45*PY = 0
BOUNDS
D < 10000
END
Solving this linear program, we find that, in order to gain $10,000 in
arbitrage, we have to change about $34 million dollars into euros, then
convert these euros into yens and finally change the yens into dollars. There
are other solutions as well. The arbitrage opportunity is so tiny ($0.0003 to
the dollar) that, depending on the numerical precision used, some LP solvers
do not find it, thus concluding that there is no arbitrage here. An interesting
example illustrating the role of numerical precision in optimization solvers!

#### 4.4 Case Study: Tax Clientele Effects in Bond Portfolio Management


The goal is to construct an optimal tax-specific bond portfolio, for a given
tax bracket, by exploiting the price differential of an after-tax stream of cash
flows. This objective is accomplished by purchasing at the ask price “underpriced” bonds (for the specific tax bracket), while simultaneously selling
at the bid price “overpriced” bonds. The following model was proposed by
E.I. Ronn [62]. See also S.M. Schaefer [64].
Let


J = {1, . . ., j, . . ., N } = set of riskless bonds.

Pj [a] [=] [asked] [price] [of] [bond] [j]

Pj [b] [=] [bid] [price] [of] [bond] [j]

Xj [a] [=] [amount] [of] [bond] [j] [bought]

Xj [b] [=] [amount] [of] [bond] [j] [sold] [short,] [and]

We make the natural assumption that Pj [a] [> P][ b] j [.] [The] [objective] [function]
of the program is



�N

Pj [a][X] j [a] (4.11)
j=1



Z = max



�N

j=1 Pj [b][X] j [b] [−]



since the long side of an arbitrage position must be established at ask prices
while the short side of the position must be established at bid prices. Now
consider the future cash-flows of the portfolio.



�N

a [1] j [X] j [b] (4.12)
j=1



C1 =



�N

a [1] j [X] j [a]
j=1 [−]



�N

a [t] j [X] j [b][,] (4.13)
j=1



For t = 2, . . ., T, Ct = (1 + ρ)Ct 1 +

             


�N

a [t] j [X] j [a]
j=1 [−]


4.4. CASE STUDY: TAX CLIENTELE EFFECTS IN BOND PORTFOLIO MANAGEMENT81


where ρ = Exogenous riskless reinvestment rate

a [t] j = coupon and/or principal payment on bond j at time t.


For the portfolio to be riskless, we require


Ct 0 t = 1, . . ., T. (4.14)
≥

Since the bid-ask spread has been explicitly modeled, it is clear that Xj [a]

[≥] [0]
and Xj [b] [are] [required.] [Now] [the] [resulting] [linear] [program] [admits] [two]
possible solutions. [≥] [0] Either all bonds are priced to within the bid-ask spread,
i.e. Z = 0, or infinite arbitrage profits may be attained, i.e. Z = ∞. Clearly
any attempt to exploit price differentials by taking extremely large positions
in these bonds would cause price movements: the bonds being bought would
appreciate in price; the bonds being sold short would decline in value. In
order to provide a finite solution, the constraints Xj [a] [and] [X] j [b] [are]
imposed. Thus, with [≤] [1] [≤] [1]

0 ≤ Xj [a][,] [X] j [b] [≤] [1] j = 1, . . ., N, (4.15)

the complete problem is now specified as (4.11)-(4.15).


Taxes
The proposed model explicitly accounts for the taxation of income and
capital gains for specific investor classes. This means that the cash flows
need to be adjusted for the presence of taxes.
For a discount bond (i.e. when Pj [a] [<] [100),] [the] [after-tax] [cash-flow] [of]
bond j in period t is given by


a [t] j [=][ c] j [t] [(1][ −] [τ] [)][,]


where c [t] j is the semiannual coupon payment

and τ is the ordinary income tax rate.


At maturity, the j [th] bond yields


a [t] j [= (100][ −] [P][ a] j [)(1][ −] [g][) +][ P][ a] j [,]


where g is the capital gains tax rate.
For premium bond (i.e. when Pj [a] [>] [100),] [the] [premium] [is] [amortized]
against ordinary income over the life of the bond, giving rise to an after-tax
coupon payment of







j
c [t] j [−] [100]

[−] [P][ a] nj



j
(1 τ ) + [P][ a] [−] [100]
 - nj







a [t] j [=]



where nj is the number of coupon payments remaining to maturity.
A premium bond also makes a nontaxable repayment of


a [t] j [= 100]


82 CHAPTER 4. LP MODELS: ASSET PRICING AND ARBITRAGE


at maturity.


Data
The model requires that the data contain bonds with perfectly forcastable cash flows. All callable bonds are excluded from the sample. For
the same reason, flower bonds of all types are excluded. Thus, all noncallable
bonds and notes are deemed appropriate for inclusion in the sample.
Major categories of taxable investors are Domestic Banks, Insurance
Companies, Individuals, Nonfinancial Corporations, Foreigners. In each
case, one needs to distinguish the tax rates on capital gains versus ordinary income.
The fundamental question to arise from this study is: does the data
reflect tax clientele effects or arbitrage opportunities?
Consider first the class of tax-exempt investors. Using current data, form
the optimal “purchased” and “sold” bond portfolios. Do you observe the
same tax clientele effect as documented by Schaefer for British government
securities; namely, the “purchased” portfolio contains high coupon bonds
and the “sold” portfolio is dominated by low coupon bonds. This can be
explained as follows: The preferential taxation of capital gains for (most)
taxable investors causes them to gravitate towards low coupon bonds. Consequently, for tax-exempt investors, low coupon bonds are “overpriced” and
not desirable as investment vehicles.
Repeat the same analysis with the different types of taxable investors.
Do you observe:


1. a clientele effect in the pricing of US Government investments, with
tax-exempt investors, or those without preferential treatment of capital gains, gravitating towards high coupon bonds?


2. that not all high coupon bonds are desirable to investors without preferential treatment of capital gains? Nor are all low coupon bonds
attractive to those with preferential treatment of capital gains. Can
you find reasons why this may be the case?



The dual price, say ut, associated with constraint (4.13) represents the
present value of an additional dollar at time t. Explain why. It follows that
ut may be used to compute the term structure of spot interest rates Rt,
given by the relation




  1
Rt =
ut




- 1
t

 - 1.



Compute this week’s term structure of spot interest rates for tax-exempt
investors.


## Chapter 5

# Nonlinear Programming: Theory and Algorithms

#### 5.1 Introduction

So far, we focused on optimization problems with linear constraints and a
linear objective function. Linear functions are “nice”–they are smooth and
predictable. Consequently, we were able to use specialized and highly efficient techniques for their solution. Many realistic formulations of optimization problems however, do not fit into this nice structure and require more
general methods. In this chapter we study general optimization problems of
the form
( ) minx f (x)
OP
gi(x) = 0, i (5.1)
∈E
gi(x) 0, i .
≥ ∈I

where f and gi are functions of IR [n] IR, and are index sets for the
→ E I
equality and inequality constraints respectively. Such optimization problems
are often called nonlinear programming problems, or nonlinear programs.
There are many problems where the general framework of nonlinear programming is needed. Here are some illustrations:


1. Economies of scale: In many applications costs or profits do not
grow linearly with the corresponding activities. In portfolio construction, an individual investor may benefit from economies of scale as
fixed costs of trading become negligible for larger trades. Conversely,
an institutional investor may suffer from diseconomies of scale if a
large trade has an unfavorable market impact on the security traded.
Realistic models of such trades must involve nonlinear objective or
constraint functions.


2. Probabilistic elements: Nonlinearities frequently arise when some
of the coefficients in the model are random variables. For example,
consider a linear program where the right–hand sides are random. To


83


84CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


illustrate, suppose the LP has two constraints:


maximize c1x1 + . . . + cnxn
a11x1 + . . . + a1nxn ≤ b1
a21x1 + . . . + a2nxn ≤ b2

where the coefficients b1 and b2 are independently distributed and
Gi(y) represents the probability that the random variable bi is at least
as large as y. Suppose you want to select the variable x1, . . ., xn so
that the joint probability of both the constraints being satisfied is at
least β:


P [a11x1 + . . . + a1nxn ≤ b1] × P [a21x1 + . . . + a2nxn ≤ b2] ≥ β.

Then this condition can be written as the following set of constraints:

−y1 + a11x1 + . . . + a1nxn = 0
−y2 + a21x1 + . . . + a2nxn = 0
G1(y1) G2(y2) β,
× ≥

where this product leads to nonlinear restrictions on y1 and y2.


3. Value-at-Risk: The Value-at-Risk is a risk measure that focuses on
rare events. For example, for a random variable X that represents
daily loss from an investment portfolio, VaR would be the largest loss
that occurs with a specified frequency such as once per year. Given
a probability level α, say α = 0.99, the Value-at-Risk VaRα(X) of
a random variable X with a continuous distribution function is the
value γ such that P (X ≤ γ) = α. As such, VaR focuses on the
tail of the distribution of the random variable X. Depending on the
distributional assumptions for portfolio returns, the problem of finding
a portfolio that minimizes VaR can be a highly nonlinear optimization
problem.


4. Mean-Variance Optimization: Markowitz’s MVO model introduced
in Section 1.3.1 is a quadratic program: the objective function is
quadratic and the constraints are linear. In Chapter 7 we will present
an interior point algorithm for this class of nonlinear optimization
problems.


5. Constructing an index fund: In integer programming applications,
such as the model discussed in Section 12.3 for constructing an index
fund, the “relaxation” can be written as a multivariate function that
is convex but non-differentiable. Subgradient techniques can be used
to solve this class of nonlinear optimization problems.


In contrast to linear programming, where the simplex method can handle most instances and reliable implementations are widely available, there
is not a single preferred algorithm for solving general nonlinear programs.
Without difficulty, one can find ten or fifteen methods in the literature and
the underlying theory of nonlinear programming is still evolving. A systematic comparison between different methods and packages is complicated


5.2. SOFTWARE 85


by the fact that a nonlinear method can be very effective for one type of
problem and yet fail miserably for another. In this chapter, we sample a few
ideas:


1. the method of steepest descent for unconstrained optimization,


2. Newton’s method,


3. the generalized reduced-gradient algorithm,


4. sequential quadratic programming,


5. subgradient optimization for nondifferentiable functions.


We address the solution of two special classes of nonlinear optimization
problems, namely quadratic and conic optimization problems in Chapters 7
and 9. For these problem classes, interior-point methods (IPMs) are very
effective. While IPMs are heavily used for general nonlinear programs also,
we delay their discussion until Chapter 7.

#### 5.2 Software


Some software packages for solving nonlinear programs are:


1. CONOPT, GRG2, Excel’s SOLVER (all three are based on the generalized reduced-gradient algorithm),


2. MATLAB optimization toolbox, SNOPT, NLPQL (sequential quadratic
programming),


3. MINOS, LANCELOT (Lagrangian approach),


4. LOQO, MOSEK, IPOPT (Interior point algorithms for the KKT conditions, see Section 5.5).


The Network Enabled Optimization Server (NEOS) website we already
mentioned in Chapter 2 and available at


http://www-neos.mcs.anl.gov/neos


provides access to many academic and commercial nonlinear optimization
solvers. In addition, the Optimization Software Guide based on the book by
Mor´e and Wright [52] and available from


http://www-fp.mcs.anl.gov/otc/Guide/SoftwareGuide


lists information on more than 30 nonlinear programming packages.
Of course, as is the case for linear programming, you will need a modeling
language to work efficiently with large nonlinear models. Two of the most
popular are GAMS and AMPL. Most of the optimizers described above accept models written in either of these mathematical programming languages.


86CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS

#### 5.3 Univariate Optimization


Before discussing optimization methods for multivariate and or constrained
problems, we start with a description of methods for solving univariate equations and optimizing univariate functions. These methods, often called line
search methods are important components to many nonlinear programming
algorithms.


5.3.1 Binary search


Binary search is a very simple idea for numerically solving the nonlinear
equation f (x) = 0, where f is a function of a single variable.
For example, suppose we want to find the maximum of g(x) = 2x [3]  - e [x] .
For this purpose we need to identify the critical points of the function,
namely, those points that satisfy the equation g [′] (x) = 6x [2] - e [x] = 0. But
there is no closed form solution to this equation. So we solve the equation
numerically, through binary search. Letting f (x) := g [′] (x) = 6x [2] - e [x], we
first look for two points, say a, b, such that the signs of f (a) and f (b) are
opposite. Here a = 0 and b = 1 would do since f (0) = −1 and f (1) ≈ 3.3.
Since f is continuous, we know that there exists an x with 0 < x < 1 such
that f (x) = 0. We say that our confidence interval is [0,1]. Now let us try
the middle point x = 0.5. Since f (0.5) ≈−0.15 < 0 we know that there is
a solution between 0.5 and 1 and we get the new confidence interval [0.5,
1.0]. We continue with x = 0.75 and since f (0.75) > 0 we get the confidence
interval [0.5,0.75]. Repeating this, we converge very quickly to a value of x
where f (x) = 0. Here, after 10 iterations, we are within 0.001 of the real
value.
In general, if we have a confidence interval of [a, b], we evaluate f ( [a][+][b]

2 [)]
to cut the confidence interval in half.
Binary search is fast. It reduces the confidence interval by a factor of
2 for every iteration, so after k iterations the original interval is reduced to
(b − a) × 2 [−][k] . A drawback is that binary search only finds one solution. So,
if g had local extrema in the above example, binary search could converge
to any of them. In fact, most algorithms for nonlinear programming are
subject to failure for this reason.


Example 5.1 Binary search can be used to compute the internal rate of
return (IRR) r of an investment. Mathematically, r is the interest rate that
satisfies the equation


F1 F2 F3 FN

[+] [+][ . . .][ +] [= 0]
1 + r [+] (1 + r) [2] (1 + r) [3] (1 + r) [N]

[−] [C]


where


Ft = cash flow in year t

N = number of years


C = cost of the investment


5.3. UNIVARIATE OPTIMIZATION 87


For most investments, the above equation has a unique solution and
therefore the IRR is uniquely defined, but one should keep in mind that this
is not always the case. The IRR of a bond is called its yield. As an example,
consider a 4-year non-callable bond with a 10% coupon rate paid annually
and a par value of $1000. Such a bond has the following cash flows:


In Yr. t Ft
1 $ 100
2 100
3 100
4 1100


Suppose this bond is now selling for $900. Compute the yield of this bond.


The yield r of the bond is given by the equation


100 100 100 1100

[+] [+]
1 + r [+] (1 + r) [2] (1 + r) [3] (1 + r) [4]

[−] [900 = 0]


Let us denote by f (r) the left-hand-side of this equation. We find r such
that f (r) = 0 using binary search.
We start by finding values (a, b) such that f (a)  - 0 and f (b) < 0.
In this case, we expect r to be between 0 and 1. Since f (0) = 500 and
f (1) = −743.75, we have our starting values.
Next, we let c = 0.5 (the midpoint) and calculate f (c). Since f (0.5) =
−541.975, we replace our range with a = 0 and b = 0.5 and repeat. When
we continue, we get the following table of values:


Table 5.1: Binary search to find the IRR of a non-callable bond

|Iter.|a c b|f(a) f(c) f(b)|
|---|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12|0<br>0.5<br>1<br>0<br>0.25<br>0.5<br>0<br>0.125<br>0.25<br>0.125<br>0.1875<br>0.25<br>0.125<br>0.15625<br>0.1875<br>0.125<br>0.140625<br>0.15625<br>0.125<br>0.132813<br>0.140625<br>0.132813<br>0.136719<br>0.140625<br>0.132813<br>0.134766<br>0.136719<br>0.132813<br>0.133789<br>0.134766<br>0.133789<br>0.134277<br>0.134766<br>0.133789<br>0.134033<br>0.134277|500<br>-541.975<br>-743.75<br>500<br>-254.24<br>-541.975<br>500<br>24.85902<br>-254.24<br>24.85902<br>-131.989<br>-254.24<br>24.85902<br>-58.5833<br>-131.989<br>24.85902<br>-18.2181<br>-58.5833<br>24.85902<br>2.967767<br>-18.2181<br>2.967767<br>-7.71156<br>-18.2181<br>2.967767<br>-2.39372<br>-7.71156<br>2.967767<br>0.281543<br>-2.39372<br>0.281543<br>-1.05745<br>-2.39372<br>0.281543<br>-0.3883<br>-1.05745|



According to this computation the yield of the bond is approximately r =
13.4%. Of course, this routine sort of calculation can be easily implemented
on a computer.


88CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


Exercise 5.1 Find a root of the polynomial f (x) = 5x [4] - 20x + 2 in the
interval [0,1] using binary search.


Exercise 5.2 Compute the yield on a 6-year non-callable bond that makes
5% coupon payments in years 1,3, and 5, coupon payments of 10% in years
2 and 4, and pays the par value in year 6.


Exercise 5.3 The well-known Black-Scholes-Merton option pricing formula
has the following form for European call option prices:


C(K, T ) = S0Φ(d1) Ke [−][rT] Φ(d2),
                  
where




[S][0] [σ][2]

K [) + (][r][ +] 2



d1 = log( [S] K [0]



σ ~~√~~

T,



2 [)][T]



d2 = d1 σ ~~√~~
     


,
T



and Φ(·) is the cumulative distribution function for the standard normal distribution. r in the formula represents the continuously compounded risk-free
and constant interest rate and σ is the volatility of the underlying security
that is assumed to be constant. Given the market price of a particular option and an estimate for the interest rate r, the unique value of the volatility
parameter σ that satisfies the pricing equation above is called the implied
volatility of the underlying security. Calculate the implied volatility of a
stock currently valued at $20 if a European call option on this stock with
a strike price of $18 and a maturity of 3 months is worth $2.20. Assume a
zero interest rate and use binary search.


Golden Section Search


Golden section search is similar in spirit to binary search. It can be used
to solve a univariate equation as above, or to compute the maximum of
a function f (x) defined on an interval [a, b]. The discussion here is for the
optimization version. The main difference between the golden section search
and the binary search is in the way the new confidence interval is generated
from the old one.
We assume that


(i) f is continuous


(ii) f has a unique local maximum in the interval [a, b].


The golden search method consists in computing f (c) and f(d) for a <
d < c < b.


  - If f (c)  - f (d), the procedure is repeated with the interval (a, b) replaced by (d, b).


  - If f (c) < f (d), the procedure is repeated with the interval (a, b) replaced by (a, c).


5.3. UNIVARIATE OPTIMIZATION 89



Remark 5.1 The name “golden section” comes from a certain choice of c
whereand d that yir = ~~√~~ el5−ds fast convergence, namely1 = .618034 . . .. This is the c =golden a+r(b−ratio,a) andalready d = b+knownr(a−bto),



5−1



where r = 2− = .618034 . . .. This is the golden ratio, already known to

the ancient Greeks.



Example 5.2 Find the maximum of the function x [5] - 10x [2] + 2x in the
interval [0, 1].


In this case, we begin with a = 0 and b = 1. Using golden section search,
that gives d = 0.382 and c = 0.618. The function values are f (a) = 0,
f (d) = −0.687, f (c) = −2.493, and f (b) = −7. Since f (c) < f (d), our new
range is a = 0, b = .618. Recalculating from the new range gives d = .236,
c = .382 (note that our current c was our previous d: it is this reuse of
calculated values that gives golden section search its speed). We repeat this
process to get the following table:


Table 5.2: Golden section search in Example 5.2.

|Iter.|a d c b|f(a) f(d) f(c) f(b)|
|---|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21|0<br>0.382<br>0.618<br>1<br>0<br>0.2361<br>0.382<br>0.618<br>0<br>0.1459<br>0.2361<br>0.382<br>0<br>0.0902<br>0.1459<br>0.2361<br>0<br>0.0557<br>0.0902<br>0.1459<br>0.0557<br>0.0902<br>0.1115<br>0.1459<br>0.0557<br>0.077<br>0.0902<br>0.1115<br>0.077<br>0.0902<br>0.0983<br>0.1115<br>0.0902<br>0.0983<br>0.1033<br>0.1115<br>0.0902<br>0.0952<br>0.0983<br>0.1033<br>0.0952<br>0.0983<br>0.1002<br>0.1033<br>0.0983<br>0.1002<br>0.1014<br>0.1033<br>0.0983<br>0.0995<br>0.1002<br>0.1014<br>0.0995<br>0.1002<br>0.1007<br>0.1014<br>0.0995<br>0.0999<br>0.1002<br>0.1007<br>0.0995<br>0.0998<br>0.0999<br>0.1002<br>0.0998<br>0.0999<br>0.1<br>0.1002<br>0.0999<br>0.1<br>0.1001<br>0.1002<br>0.0999<br>0.1<br>0.1<br>0.1001<br>0.0999<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1|0<br>-0.6869<br>-2.4934<br>-7<br>0<br>-0.0844<br>-0.6869<br>-2.4934<br>0<br>0.079<br>-0.0844<br>-0.6869<br>0<br>0.099<br>0.079<br>-0.0844<br>0<br>0.0804<br>0.099<br>0.079<br>0.0804<br>0.099<br>0.0987<br>0.079<br>0.0804<br>0.0947<br>0.099<br>0.0987<br>0.0947<br>0.099<br>0.1<br>0.0987<br>0.099<br>0.1<br>0.0999<br>0.0987<br>0.099<br>0.0998<br>0.1<br>0.0999<br>0.0998<br>0.1<br>0.1<br>0.0999<br>0.1<br>0.1<br>0.1<br>0.0999<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1<br>0.1|



Exercise 5.4 One of the most fundamental techniques of statistical analysis is the method of maximum likelihood estimation. Given a sample set
of independently drawn observations from a parametric distribution, the estimation problem is to determine the values of the distribution parameters
that maximize probability that the observed sample set comes from this
distribution.
Consider, for example, the observations x1 = 0.24, x2 = 0.31, x3 = 2.3,
                    and x4 = 1.1 sampled from a normal distribution. If the mean of the

   

90CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


distribution is known to be 0, what is the maximum likelihood estimate
of the standard deviation, σ? Construct the log-likelihood function and
maximize it using golden section search.


5.3.2 Newton’s Method


The main workhorse of many optimization algorithms is a centuries old
technique for the solution of nonlinear equations developed by Sir Isaac
Newton. We will discuss the multivariate version of Newton’s method later.
We focus on the univariate case first. For a given nonlinear function f we
want to find an x such that
f (x) = 0.


Assume that f is continuously differentiable and that we currently have an
estimate x [k] of the solution (we will use superscripts for iteration indices in
the following discussion). The first order (i.e., linear) Taylor series approximation to the function f around x [k] can be written as follows:


f (x [k] + δ) ≈ fˆ(δ) := f (x [k] ) + δf [′] (x [k] ).


This is equivalent to saying that we can approximate the function f by the
line f [ˆ] (δ) that is tangent to it at x [k] . If the first order approximation f [ˆ] (δ)
were perfectly good, and if f [′] (x [k] ) ̸= 0, the value of δ that satisfies

fˆ(δ) = f (x [k] ) + δf [′] (x [k] ) = 0


would give us the update on the current iterate x [k] necessary to get to the
solution. This value of δ is computed easily:


δ =

           - f [f] [(] ( [x] x [k][k][)] ) [.]

[′]


The expression above is called the Newton update and Newton’s method
determines its next estimate of the solution as


x [k][+1] = x [k] + δ = x [k]

             - f [f] [(] ( [x] x [k][k][)] ) [.]

[′]

Since f [ˆ] (δ) is only an approximation to f (x [k] +δ), we do not have a guarantee
that f (x [k][+1] ) is zero, or even small. However, as we discuss below, when x [k]

is close enough to a solution of the equation f (x) = 0, x [k][+1] is even closer.
We can then repeat this procedure until we find an x [k] such that f (x [k] ) = 0,
or in most cases, until f (x [k] ) becomes reasonably small, say, less than some
pre-specified ε > 0.
There is an intuitive geometric explanation of the procedure we just
described: We first find the line that is tangent to the function at the current
iterate, then we calculate the point where this line intersects the x-axis, and
we set the next iterate to this value and repeat the process. See Figure 5.1
for an illustration.


5.3. UNIVARIATE OPTIMIZATION 91



1000


800


600


400


200


0






|Col1|f(r)<br>tangent<br>f(0)=500<br>f’(0)=−5000|
|---|---|
||x0=0<br>x1=0.1|



−0.05 0 0.05 0.1 0.15 0.2

r



Figure 5.1: First step of Newton’s method in Example 5.3


Example 5.3 Let us recall Example 5.1 where we computed the IRR of an
investment. Here we solve the problem using Newton’s method. Recall that
the yield r must satisfy the equation


100 100 1100

f (r) = [100]

[+] [+]
1 + r [+] (1 + r) [2] (1 + r) [3] (1 + r) [4]

[−] [900 = 0][.]


The derivative of f (r) is easily computed:


100 200 300 4400
f [′] (r) = − (1 + r) [2] [−] (1 + r) [3] [−] (1 + r) [4] [−] (1 + r) [5] [.]


We need to start Newton’s method with an initial guess, let us choose
x [0] = 0. Then



x [1] = x [0]

   - f [f] [(0)] (0)

[′]



f [′] (0)



500
= 0
  - 5000 [= 0][.][1]

   


We mentioned above that the next iterate of Newton’s method is found by calculating the point where the line tangent to f at the current iterate intersects
the axis. This observation is illustrated in Figure 5.1.
Since f (x [1] ) = f (0.1) = 100 is far from zero we continue by substituting
x [1] into the Newton update formula to obtain x [2] = 0.131547080371 and so
on. The complete iteration sequence is given in Table 5.3.


A few comments on the speed and reliability of Newton’s method are
in order. Under favorable conditions, Newton’s method converges very fast


92CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


Table 5.3: Newton’s method for Example 5.3

|k|xk|f(xk)|
|---|---|---|
|0<br>1<br>2<br>3<br>4<br>5|0.000000000000<br>0.100000000000<br>0.131547080371<br>0.133880156946<br>0.133891647326<br>0.133891647602|500.000000000000<br>100.000000000000<br>6.464948211497<br>0.031529863053<br>0.000000758643<br>0.000000000000|



to a solution of a nonlinear equation. Indeed, if x [k] is sufficiently close to a
solution x [∗] and if f [′] (x [∗] ) ̸= 0, then the following relation holds:

x [k][+1] x [∗] C(x [k] x [∗] ) [2] with C = [f][ ′′][(][x][∗][)] (5.2)

      - ≈      - 2f (x [∗] )

[′]

(5.2) indicates that, the error in our approximation (x [k] - x [∗] ) is approximately squared in each iteration. This behavior is called the quadratic
convergence of Newton’s method. Note that the number of correct digits
is doubled in each iteration of the example above and the method required
much fewer iterations than the simple bisection approach.
However, when the ‘favorable conditions’ we mentioned above are not
satisfied, Newton’s method may fail to converge to a solution. For example,
consider f (x) = x [3] - 2x +2. Starting at 0, one would obtain iterates cycling
between 1 and 0. Starting at a point close to 1 or 0, one similarly gets
iterates alternating in close neighborhoods of 1 and 0, without ever reaching
the root around -1.76. Therefore, it often has to be modified before being
applied to general problems. Common modifications of Newton’s method
include the line-search and trust-region approaches. We briefly discuss line
search approaches in Section 5.3.3. More information on these methods can
be found in standard numerical optimization texts such as [55].
Next, we derive a variant of Newton’s method that can be applied to univariate optimization problems. If the function to be minimized/maximized
has a unique minimizer/maximizer and is twice differentiable, we can do
the following. Differentiability and the uniqueness of the optimizer indicate
that x [∗] maximizes (or minimizes) g(x) if and only if g [′] (x [∗] ) = 0. Defining f (x) = g [′] (x) and applying Newton’s method to this function we obtain
iterates of the following form:



x [k][+1] = x [k]

    - f [f] [(] ( [x] x [k][k][)]

[′]



f [f] [(] ( [x] x [k][k][)] ) [=][ x][k][ −] g [g][′′][′][(] ( [x] x [k][k][)]

[′]



g [′′] (x [k] ) [.]



Example 5.4 Let us apply the optimization version of Newton’s method
to Example 5.2. Recalling that f (x) = x [5] - 10x [2] + 2x, we have f [′] (x) =
5x [4] - 20x + 2 and f [′′] (x) = 20(x [3] - 1). Thus, the Newton update formula is
given as



x [k][+1] = x [k]

   - [5(][x] 20(( [k][)][4][ −] x [k] ) [20][3] [x][k] 1) [ + 2]



.
20((x [k] ) [3] - 1)


5.3. UNIVARIATE OPTIMIZATION 93


Table 5.4: Iterates of Newton’s method in Example 5.4

|k|xk|f(xk)|f ′(xk)|
|---|---|---|---|
|0<br>1<br>2<br>3|0.000000000000<br>0.100000000000<br>0.100025025025<br>0.100025025034|0.000000000000<br>0.100010000000<br>0.100010006256<br>0.100010006256|2.000000000000<br>0.000500000000<br>0.000000000188<br>0.000000000000|



Starting from 0 and iterating we obtain the sequence given in Table 5.4.


Once again, observe that Newton’s method converged very rapidly to the solution and generated several more digits of accuracy than the golden section
search. Note however that the method would have failed if we had chosen
x [0] = 1 as our starting point.


Exercise 5.5 Repeat Exercises 5.2, 5.3, and 5.4 using Newton’s method.


Exercise 5.6 We derived Newton’s method by approximating a given function f using the first two terms of its Taylor series at the current point xk.
When we use Taylor series approximation to a function, there is no a priori
reason that tells us to stop at two terms. We can consider, for example,
using the first three terms of the Taylor series expansion of the function and
get a quadratic approximation. Derive a variant of Newton’s method that
uses this approximation to determine the roots of the function f . Can you
determine the rate of convergence for this new method, assuming that the
method converges?


5.3.3 Approximate Line Search


When we are optimizing a univariate function, sometimes it is not necessary
to find the minimizer/maximizer of the function very accurately. This is
especially true when the univariate optimization is only one of the steps
in an iterative procedure for optimizing a more complicated function. This
happens, for example, when the function under consideration corresponds to
the values of a multivariate function along a fixed direction. In such cases,
one is often satisfied with a new point that provides a sufficient amount
of improvement over the previous point. Typically, a point with sufficient
improvement can be determined much quicker than the exact minimizer of
the function which results in a shorter computation time for the overall
algorithm.
The notion of “sufficient improvement” must be formalized to ensure
that such an approach will generate convergent iterates. Say we wish to
minimize the nonlinear, differentiable function f (x) and we have a current
estimate x [k] of its minimizer. Assume that f [′] (x [k] ) < 0 which indicates that
the function will decrease by increasing x [k] . Recall the linear Taylor series
approximation to the function:

f (x [k] + δ) ≈ fˆ(δ) := f (x [k] ) + δf [′] (x [k] ).


94CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


The derivative of the function f [′] (x [k] ) gives a prediction of the decrease in
the function value as we move forward from x [k] . If f has a minimizer, we
can not expect that it will decrease forever as we increase x [k] like its linear
approximation above. We can require, however, that we find a new point
such that the improvement in the function value is at least a fraction of the
improvement predicted by the linear approximation. Mathematically, we
can require that


f (x [k] + δ) ≤ f (x [k] ) + µδf [′] (x [k] ) (5.3)

where µ ∈ (0, 1) is the desired fraction. This sufficient decrease requirement is often called the Armijo-Goldstein condition. See Figure 5.2 for an
illustration.


δ


Figure 5.2: Armijo-Goldstein sufficient decrease condition


Among all step sizes satisfying the sufficient decrease condition, one
would typically prefer as large a step size as possible. However, trying
to find the maximum such step size accurately will often be too time consuming and will beat the purpose of this approximation approach. A typical
strategy used in line search is backtracking. We start with a reasonably large
initial estimate. We check whether this step size satisfies condition (5.3). If
it does, we accept this step size, modify our estimate and continue. If not,
we backtrack by using a step size that is a fraction of the previous step size
we tried. We continue to backtrack until we obtain a step size satisfying the
sufficient decrease condition. For example, if the initial step size is 5 and
we use the fraction 0.8, first backtracking iteration will use a step size of 4,
and then 3.2 and so on.


Exercise 5.7 Consider the function f (x) = 4 [1] [x][4] [−] [x][2] [+ 2][x][ −] [1.] [We] [want]

to minimize this function using Newton’s method. Verify that starting at a
point close to 0 or 1 and using Newton’s method, one would obtain iterates
alternating between close neighborhoods of 0 and 1 and never converge. Apply Newton’s method to this problem with the Armijo-Goldstein condition



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-93-0.png)
5.4. UNCONSTRAINED OPTIMIZATION 95


and backtracking starting from the point 0. Use µ = .5 and a backtracking
ratio of 0.9. Experiment with other values of µ ∈ (0, 1) and the backtracking
ratio.


Exercise 5.8 Re-solve Exercise 5.4 using the optimization version of Newton’s method with line search and backtracking. Use µ = .1 and a backtracking ratio of 0.8.


Exercise 5.9 As Figure 5.2 illustrates the Armijo-Goldstein condition disallows step sizes that are too large and beyond which the predictive power
of the gradient of the function is weak. Backtracking strategy balances this
by trying to choose as large an acceptable value of the step size as possible,
ensuring that the step size is not too small. Another condition, called the
Wolfe condition, rules out step sizes that are too small by requiring that


∥f [′] (x [k] + δ)∥≤ η∥f [′] (x [k] )∥

for some η ∈ [0, 1]. The motivation for this condition is the following:
For a differentiable function f, minimizers (or maximizers) will occur at
points where the derivative of the function is zero. The Wolfe condition
seeks points whose derivatives are closer to zero than the current point.
Interpret the Wolfe condition geometrically on Figure 5.2. For function
f (x) = 1 [+] [2][x] [with] [current] [iterate] [x][k] [=] [0][.][1] [determine] [the]
4 [x][4] [−] [x][2] [−] [1]
Newton update and calculate which values of the step size satisfy the Wolfe
condition for η = [1] [and] [also] [for] [η] [=] [3] [.]



4 [1] [and] [also] [for] [η] [=] [3] 4



4 [.]


#### 5.4 Unconstrained Optimization

We now move on to nonlinear optimization problems with multiple variables. First, we will focus on problems that have no constraints. Typical
examples of unconstrained nonlinear optimization problems arise in model
fitting and regression. The study of unconstrained problems is also important for constrained optimization as one often solves a sequence of unconstrained problems as subproblems in various algorithms for the solution of
constrained problems.
We use the following generic format for unconstrained nonlinear programs we consider in this section:


min f (x), where x = (x1, . . ., xn).


For simplicity, we will restrict our discussion to minimization problems.
These ideas can be trivially adapted for maximization problems.


5.4.1 Steepest Descent


The simplest numerical method for finding a minimizing solution is based on
the idea of going downhill on the graph of the function f . When the function
f is differentiable, its gradient always points in the direction of fastest initial


96CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


increase and the negative gradient is the direction of fastest decrease. This
suggests that, if our current estimate of the minimizing point is x [∗], moving
in the direction of −∇f (x [∗] ) is desirable. Once we choose direction, deciding
how far we should move along this direction is determined using line search.
The line search problem is a univariate problem that can be solved, perhaps
in an approximate fashion, using the methods of the previous section. This
will provide a new estimate of the minimizing point and the procedure can
be repeated.
We illustrate this approach on the following example:


min f (x) = (x1 2) [4] + exp(x1 2) + (x1 2x2) [2] .
            -             -             

The first step is to compute the gradient of the function, namely the vector
of the partial derivatives of the function with respect to each variable:







∇f (x) =




4(x1 2) [3] + exp(x1 2) + 2(x1 2x2)
   -    -    4(x1 2x2)

    -     


. (5.4)



Next, we need to choose a starting point. We arbitrarily select the point
x [0] = [0, 3] [⊤] . Now we are ready to compute the steepest descent direction
at point x [0] . It is the direction opposite to the gradient vector computed at
x [0], namely







d [0] = −∇f (x [0] ) =




44 + e [−][2]



−24



.



If we move from x [0] in the direction d [0], using a step size α we get a new
point x [0] + αd [0] (α = 0 corresponds to staying at x [0] ). Since our goal is
to minimize f, we will try to move to a point x [1] = x [0] + αd [0] where α is
chosen to approximately minimize the function along this direction. For this
purpose, we evaluate the value of the function f along the steepest descent
direction as a function of the step size α:


φ(α) := f (x [0] + αd [0] ) = ([0 + (44 + e [−][2] )α] − 2) [4] + exp([0 + (44 + e [−][2] )α] − 2)

+([0 + (44 + e [−][2] )α] − 2[3 − 24α]) [2]


Now, the optimal value of α can be found by solving the one–dimensional
minimization problem min φ(α).
This minimization can be performed through one of the numerical line
search procedures of the previous section. Here we use the approximate line
search approach with sufficient decrease condition we discussed in Section
5.3.3. We want to choose a step size alpha satisfying


φ(α) ≤ φ(0) + µαφ [′] (0)

where µ ∈ (0, 1) is the desired fraction for the sufficient decrease condition.
We observe that the derivative of the function φ at 0 can be expressed as


φ [′] (0) = ∇f (x [0] ) [T] d [0] .


5.4. UNCONSTRAINED OPTIMIZATION 97


This is the directional derivative of the function f at point x [0] and direction
d [0] . Using this identity the sufficient decrease condition on function φ can
be written in terms of the original function f as follows:

f (x [0] + αd [0] ) ≤ f (x [0] ) + µα∇f (x [0] ) [T] d [0] . (5.5)

The condition (5.5) is the multivariate version of the Armijo-Goldstein condition (5.3).
As discussed in Section 5.3.3, the sufficient decrease condition (5.5) can
be combined with a backtracking strategy. For this example, we use µ = 0.3
for the sufficient decrease condition and apply backtracking with an initial
trial step size of 1 and a backtracking factor of β = 0.8. Namely, we try step
sizes 1, 0.8, 0.64, 0.512 and so on, until we find a step size of the form 0.8 [k]

that satisfied the Armijo-Goldstein condition. The first five iterates of this
approach as well as the 20th iterate are given in Table 5.5. For completeness,
one also has to specify a termination criterion for the approach. Since the
gradient of the function must be the zero vector at an unconstrained minimizer, most implementations will use a termination criterion of the form
∥∇f (x)∥≤ ε where ε - 0 is an appropriately chosen tolerance parameter.
Alternatively, one might stop when successive iterations are getting very
close to each other, that is when ∥x [k][+1] - x [k] ∥≤ ε for some ε - 0. This
last condition indicates that progress has stalled. While this may be due
to the fact that iterates approached the optimizer and can not progress any
more, there are instances where the stalling is due to the high degree of
nonlinearity in f .


Table 5.5: Steepest descent iterations

|k|(xk, xk) (dk, dk) αk ∥∇f(xk+1)∥<br>1 2 1 2|
|---|---|
|0<br>1<br>2<br>3<br>4<br>5<br>...<br>20|(0.000, 3.000)<br>(43.864, -24.000)<br>0.055<br>3.800<br>(2.412, 1.681)<br>(0.112, -3.799)<br>0.168<br>2.891<br>(2.430, 1.043)<br>(-2.544, 1.375)<br>0.134<br>1.511<br>(2.089, 1.228)<br>(-0.362, -1.467)<br>0.210<br>1.523<br>(2.013, 0.920)<br>(-1.358, 0.690)<br>0.168<br>1.163<br>(1.785, 1.036)<br>(-0.193, -1.148)<br>0.210<br>1.188<br>...<br>...<br>...<br>...<br>(1.472, 0.736)<br>(-0.001, 0.000)<br>0.134<br>0.001|



A quick examination of Table 5.5 reveals that the signs of the second coordinate of the steepest descent directions change from one iteration to the
next in most cases. What we are observing is the zigzagging phenomenon,
a typical feature of steepest descent approaches that explain their slow convergence behavior for most problems. When we pursue the steepest descent
algorithm for more iterations, the zigzagging phenomenon becomes even
more pronounced and the method is slow to converge to the optimal solution x [∗] ≈ (1.472, 0.736). Figure 5.3 shows the steepest descent iterates
for our example superimposed on the contour lines of the objective function. Steepest descent directions are perpendicular to the contour lines and


98CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


zigzag between the two sides of the contour lines, especially when these lines
create long and narrow corridors. It takes more than 30 steepest descent
iterations in this small example to achieve ∥∇f (x)∥≤ 10 [−][5] . In summary,
while the steepest descent approach is easy to implement and intuitive, and
has relatively cheap iterations, it can also be quite slow to converge to solutions.


1.6


1.4


1.2


1


0.8


0.6


0.4


0 0.5 1 1.5 2 2.5


Figure 5.3: Zigzagging Behavior in the Steepest Descent Approach


Exercise 5.10 Consider a differentiable multivariate function f (x) that we
wish to minimize. Let xk be a given estimate of the solution, and consider
the first order Taylor series expansion of the function around xk:


fˆ(δ) = f (xk) + f (x) [⊤] δ.
∇

The quickest decrease in f [ˆ] starting from xk is obtained in the direction that
solves
min fˆ(δ)
∥δ∥ ≤ 1

Show that the solution δ [∗] = α∇f (x) with some α < 0, i.e., the opposite
direction to the gradient is the direction of steepest descent.


Exercise 5.11 Recall the maximum likelihood estimation problem we considered in Exercise 5.4. While we maintain the assumption that the observed
samples come from a normal distribution, we will no longer assume that we
know the mean of the distribution to be zero. In this case, we have a two parameter (mean µ and standard deviation σ) maximum likelihood estimation
problem. Solve this problem using the steepest descent method.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-97-0.png)
5.4. UNCONSTRAINED OPTIMIZATION 99


5.4.2 Newton’s Method


There are several numerical techniques for modifying the method of steepest
descent that reduce the propensity of this approach to zigzag, and thereby
speed up convergence. Steepest descent method uses the gradient of the
objective function, only a first-order information on the function. Improvements can be expected by employing second-order information on the function, that is by considering its curvature. Methods using curvature information include Newton’s method that we have already discussed in the
univariate setting. Here, we describe the generalization of this method to
multivariate problems.
Once again, we begin with the version of the method for solving equations: We will look at the case where there are several equations involving
several variables:
f1(x1, x2, . . ., xn) = 0
f2(x1, x2, . . ., xn) = 0
... ... (5.6)
fn(x1, x2, . . ., xn) = 0

Let us represent this system as


F (x) = 0,


where x is a vector of n variables, and F (x) is IR [n] -valued function with
components f1(x), . . ., fn(x). We repeat the procedure in Section 5.3.2:
First, we write the first order Taylor’s series approximation to the function
F around the current estimate x [k] :

F (x [k] + δ) ≈ Fˆ(δ) := F (x [k] ) + ∇F (x [k] )δ. (5.7)

Above, ∇F (x) denotes the Jacobian matrix of the function F, i.e., ∇F (x)
has rows ( f1(x)) [⊤], . . ., ( fn(x)) [⊤], the transposed gradients of the func∇ ∇
tions f1 through fn. We denote the components of the n-dimensional vector
x using subscripts, i.e. x = (x1, . . ., xn). Let us make these statements
more precise:



∂f1 ∂f1
∂x1 ∂xn

     - · ·
... ... ...
∂fn ∂fn
∂x1 ∂xn

     - · ·





 .



F (x1, . . ., xn) =
∇









As before, F [ˆ] (δ) is the linear approximation to the function F by the hyperplane that is tangent to it at the current point x [k] . The next step is to find
the value of δ that would make the approximation equal to zero, i.e., the
value that satisfies:

F (x [k] ) + ∇F (x [k] )δ = 0.

Notice that what we have on the right-hand-side is a vector of zeros and
the equation above represents a system of linear equations. If ∇F (x [k] ) is
nonsingular, the equality above has a unique solution given by

δ = −∇F (x [k] ) [−][1] F (x [k] ),


100CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


and the formula for the Newton update in this case is:


x [k][+1] = x [k] + δ = x [k] −∇F (x [k] ) [−][1] F (x [k] ).


Example 5.5 Consider the following problem:











F (x) = F (x1, x2) =




f1(x1, x2)
f2(x1, x2)



=




x1x2 − 2x1 + x2 − 2
(x1) [2] + 2x1 + (x2) [2]  - 7x2 + 7



= 0



First we calculate the Jacobian:


F (x1, x2) =
∇




x2 − 2 x1 + 1
2x1 + 2 2x2 − 7







.



If our initial estimate of the solution is x0 = (0, 0), then the next point
generated by Newton’s method will be:







(x [1] 1 [,][ x][1] 2 [)] = (x [0] 1 [,][ x][0] 2 [)][ −]




x [0] 2 [−] [2] x [0] 1 [+ 1]
2x [0] 1 [+ 2]  - 2x [0] 2 [−] [7]




- 1 �

 - −2
7




[5]
12 [7] [,] 6




- 1 �

 - x [0] 1 [x][0] 2 [−] [2][x] 1 [0] [+][ x] 2 [0] [−] [2]
(x [0] 1 [)][2][ + 2][x][0] 1 [+ (][x] 2 [0][)][2][ −] [7][x][0] 2 [+ 7]




= (0, 0) −




−2 1
2 −7




[7]

12 [,][ −] [5] 6



= (0, 0) ( [7]
    


6 [5] [) = (][−] [7]



6 [)][.]



Optimization Version


When we use Newton’s method for unconstrained optimization of a twice
differentiable function f (x), the nonlinear equality system that we want to
solve is the first order necessary optimality condition ∇f (x) = 0. In this
case, the functions fi(x) in (5.6) are the partial derivatives of the function
f . That is,


∂f
fi(x) = (x1, x2, . . ., xn).
∂xi


Writing



∂f
∂x1 [(][x][1][,][ x][2][, . . .,][ x][n][)]
∂f
∂xi [(][x][1][,][ x][2][, . . .,][ x][n][)]
...
∂f
∂xn [(][x][1][,][ x][2][, . . .,][ x][n][)]



f1(x1, x2, . . ., xn)
f2(x1, x2, . . ., xn)
...
fn(x1, x2, . . ., xn)












= ∇f (x),







=




F (x1, x2, . . ., xn) =









we observe that the Jacobian matrix F (x1, x2, . . ., xn) is nothing but the
∇
Hessian matrix of function f :



∂ [2] f ∂ [2] f
∂x1∂x1 ∂x1∂xn

        - · ·
... ... ...
∂ [2] f ∂ [2] f
∂xn∂x1 ∂xn∂xn

        - · ·





 = 2f (x).
∇



F (x1, x2, . . ., xn) =
∇








5.4. UNCONSTRAINED OPTIMIZATION 101


Therefore, the Newton direction at iterate x [k] is given by

δ = −∇ [2] f (x [k] ) [−][1] ∇f (x [k] ) (5.8)

and the Newton update formula is

x [k][+1] = x [k] + δ = x [k] −∇f [2] (x [k] ) [−][1] ∇f (x [k] ).

For illustration and comparison purposes, we apply this technique to the
example problem of Section 5.4.1. Recall that the problem was to


min f (x) = (x1 2) [4] + exp(x1 2) + (x1 2x2) [2]
            -             -             
starting from x [0] = (0, 3) [⊤] .
The gradient of f was given in (5.4) and the Hessian matrix is given
below:







∇ [2] f (x) =




12(x1 2) [2] + exp(x1 2) + 2 4
   -    -    −4 8



. (5.9)



Thus, we calculate the Newton direction at x [0] = (0, 3) [⊤] as follows:








     0

δ = f (
−∇ [2] 3







) [−][1] ∇f (







) = −




- 1 �

 - −44 + e [−][2]

24








0
3




50 + e [−][2] −4
−4 8



=




0.662
−2.669



.



We list the first five iterates in Table 5.6 and illustrate the rapid progress
of the algorithm towards the optimal solution in Figure 5.4. Note that the
ideal step size for Newton’s method is almost always one. In our example,
this step size always satisfied the sufficient decrease condition and was chosen
in each iteration. Newton’s method identifies a point with ∥∇f (x)∥≤ 10 [−][5]

after 7 iterations.

|Col1|Table 5.6: Newton iterations|
|---|---|
|k|(xk<br>1, xk<br>2)<br>(dk<br>1, dk<br>2)<br>αk<br>∥∇f(xk+1)∥|
|0<br>1<br>2<br>3<br>4<br>5|(0.000, 3.000)<br>(0.662, -2.669)<br>1.000<br>9.319<br>(0.662, 0.331)<br>(0.429, 0.214)<br>1.000<br>2.606<br>(1.091, 0.545)<br>(0.252, 0.126)<br>1.000<br>0.617<br>(1.343, 0.671)<br>(0.108, 0.054)<br>1.000<br>0.084<br>(1.451, 0.726)<br>(0.020, 0.010)<br>1.000<br>0.002<br>(1.471, 0.735)<br>(0.001, 0.000)<br>1.000<br>0.000|



Despite its excellent convergence behavior close to a solution, Newton’s
method is not always the best option, especially for large-scale optimization.
Often the Hessian matrix is expensive to compute at each iteration. In such
cases, it may be preferable to use an approximation of the Hessian matrix
instead. These approximations are usually chosen in such a way that the
solution of the linear system in (5.8) is much cheaper that what it would be
with the exact Hessian. Such approaches are known as quasi-Newton methods. Most popular variants of quasi-Newton methods are BFGS and DFP


102CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


1.6


1.4


1.2


1


0.8


0.6


0.4


0 0.5 1 1.5 2 2.5


Figure 5.4: Rapid convergence of Newton’s method


methods. These acronyms represent the developers of these algorithms in
the late 60s and early 70s. Detailed information on quasi-Newton approaches
can be found in, for example, [55].



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-101-0.png)

Exercise 5.12 Repeat Exercise 5.11, this time using the optimization version of Newton’s method. Use line-search with µ = [1] [in] [Armijo-Goldstein]



sion of Newton’s method. Use line-search with µ = [Armijo-Goldstein]

2 [in]
condition and a backtracking ratio of β = [1] [.]



2 [.]


#### 5.5 Constrained Optimization

We now move on to the more general case of nonlinear optimization problems
with constraints. Specifically, we consider an optimization problem given
by a nonlinear objective function and/or nonlinear constraints. We can
represent such problems in the following generic form:


minx f (x)
gi(x) = 0, i (5.10)
∈E
gi(x) 0, i .
≥ ∈I

In the remainder of this section we assume that f and gi, i are all
∈E ∪I
continuously differentiable functions.
An important tool in the study of constrained optimization problems is
the Lagrangian function. To define this function, one associates a multiplier
λi–the so-called Lagrange multiplier–with each one of the constraints. For
problem (5.10) the Lagrangian is defined as follows:

       (x, λ) := f (x) λigi(x). (5.11)
L       
i∈E∪I


5.5. CONSTRAINED OPTIMIZATION 103


Essentially, we are considering an objective function that is penalized for
violations of the feasibility constraints. For properly chosen values of λi,
minimizing the unconstrained function L(x, λ) is equivalent to solving the
constrained optimization problem (5.10). This equivalence is the primary
reason for our interest in the Lagrangian function.
One of the most important theoretical issues related to this problem
is the identification of necessary and sufficient conditions for optimality.
Collectively, these conditions are called the optimality conditions and are
the subject of this section.
Before presenting the optimality conditions for (5.10) we first discuss a
technical condition called regularity that is encountered in the theorems that
follow:


Definition 5.1 Let x be a vector satisfying gi(x) = 0, i and gi(x)
∈E ≥
0, i . Let be the set of indices for which gi(x) 0 is satisfied
∈I J ⊂I ≥
with equality. Then, x is a regular point of the constraints of (5.10) if the
gradient vectors gi(x) for i are linearly independent.
∇ ∈E ∪J

Constraints corresponding to the set E ∪J in the definition above,
namely, the constraints for which we have gi(x) = 0, are called the active
constraints at x.
We discussed two notions of optimality in Chapter 1, local and global.
Recall that a global optimal solution to (5.10) is a vector x [∗] that is feasible
and satisfies f (x [∗] ) ≤ f (x) for all feasible x. In contrast, a local optimal
solution x [∗] is feasible and satisfies f (x [∗] ) ≤ f (x) for all feasible x in the set
{x : ∥x − x [∗] ∥≤ ε} for some ε - 0. So, a local solution must be better
than all the feasible points in a neighborhood of itself. The optimality
conditions we consider below identify local solutions only, which may or may
not be global solutions to the problem. Fortunately, there is an important
class of problems where local and global solutions coincide, namely convex
optimization problems. See Appendix A for a discussion on convexity and
convex optimization problems.



Theorem 5.1 (First Order Necessary Conditions) Let x [∗] be a local
minimizer of the problem (5.10) and assume that x [∗] is a regular point for
the constraints of this problem. Then, there exists λi, i such that
∈E ∪I




  ∇f (x [∗] ) −



λi gi(x [∗] ) = 0 (5.12)
∇
i∈E∪I



λi 0, i (5.13)
≥ ∈I



λigi(x [∗] ) = 0, i . (5.14)
∈I



Note that the expression on the left hand side of (5.12) is the gradient
of the Lagrangian function L(x, λ) with respect to the variables x. First
order conditions are satisfied at local minimizers as well as local maximizers
and saddle points. When the objective and constraint functions are twice
continuously differentiable, one can eliminate maximizers and saddle points
using curvature information on the functions. As in Theorem 5.1, we consider the Lagrangian function L(x, λ) and use the Hessian of this function


104CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


with respect to the x variables to determine the collective curvature in the
objective function as well as the constraint functions at the current point.


Theorem 5.2 (Second Order Necessary Conditions) Assume that f
and gi, i are all twice continuously differentiable functions. Let x [∗]
∈E ∪I

be a local minimizer of the problem (5.10) and assume that x [∗] is a regular
point for the constraints of this problem. Then, there exists λi, i
∈E ∪I
satisfying (5.12)–(5.14) as well as the following condition:

      f (x [∗] ) λi gi(x [∗] ) (5.15)
∇ [2]      - ∇ [2]

i∈E∪I

is positive semidefinite on the tangent subspace of active constraints at x [∗] .


The last part of the theorem above can be restated in terms of the Jacobian of the active constraints. Let A(x [∗] ) denote the Jacobian of the active
constraints at x [∗] and let N (x [∗] ) be a null-space basis for A(x [∗] ). Then, the
last condition of the theorem above is equivalent to the following condition:








  f (x [∗] ) λi gi(x [∗] )
∇ [2] - ∇ [2]

i∈E∪I







N [T] (x [∗] )



N (x [∗] ) (5.16)



is positive semidefinite.
The satisfaction of the second order necessary conditions does not always
guarantee the local optimality of a given solution vector. The conditions that
are sufficient for local optimality are slightly more stringent and a bit more
complicated since they need to consider the possibility of degeneracy.


Theorem 5.3 (Second Order Sufficient Conditions) Assume that f and
gi, i are all twice continuously differentiable functions. Let x [∗] be a
∈E ∪I
feasible and regular point for the constraints of the problem (5.10). Let A(x [∗] )
denote the Jacobian of the active constraints at x [∗] and let N (x [∗] ) be a nullspace basis for A(x [∗] ). If there exists λi, i satisfying (5.12)–(5.14)
∈E ∪I
as well as
gi(x [∗] ) = 0, i implies λi            - 0, (5.17)
∈I

and








  f (x [∗] ) λi gi(x [∗] )
∇ [2] - ∇ [2]

i∈E∪I







N [T] (x [∗] )



N (x [∗] ) is positive definite (5.18)



then x [∗] is a local minimizer of the problem (5.10).


The conditions listed in Theorems 5.1, 5.2, and 5.3 are often called
Karush-Kuhn-Tucker (KKT) conditions, after their inventors.
Some methods for solving constrained optimization problems formulate
a sequence of simpler optimization problems whose solutions are used to
generate iterates progressing towards the solution of the original problem.
These “simpler” problems can be unconstrained, in which case they can be
solved using the techniques we saw in the previous section. We discuss such


5.5. CONSTRAINED OPTIMIZATION 105


a strategy in Section 5.5.1. In other cases, the simpler problem solved is
a quadratic programming problem and can be solved using the techniques
of Chapter 7. The prominent example of this strategy is the sequential
quadratic programming method that we discuss in Section 5.5.2.


Exercise 5.13 Recall the definition of the quadratic programming problem
given in Chapter 1:

( ) minx 12 [x][T][ Qx][ +][ c][T][ x]
QP
Ax = b (5.19)
x ≥ 0,

where A ∈ IR [m][×][n], b ∈ IR [m], c ∈ IR [n], Q ∈ IR [n][×][n] are given, and x ∈
IR [n] . Assume that Q is symmetric and positive definite. Derive the KKT
conditions for this problem. Show that the second order necessary conditions
are also sufficient given our assumptions.


Exercise 5.14 Consider the following optimization problem:

min f (x1, x2) = −x1 − x2 − x1x2 + [1] 2 [x] 1 [2] [+][ x] 2 [2]

s.t. x1 + x [2] 2 3,
≤
and (x1, x2) 0.
≥

List the Karush-Kuhn-Tucker optimality conditions for this problem. Verify that x [∗] = (2, 1) is a local optimal solution to this problem by finding
Lagrange multipliers λi satisfying the KKT conditions in combination with
x [∗] . Is x [∗] = (2, 1) a global optimal solution?


5.5.1 The generalized reduced gradient method


In this section, we introduce an approach for solving constrained nonlinear
programs. It builds on the method of steepest descent method we discussed
in the context of unconstrained optimization. The idea is to reduce the
number of variables using the constraints and then to solve this reduced and
unconstrained problem using the steepest descent method.


Linear Equality Constraints
First we consider an example where the constraints are linear equations.


min f (x) = x [2] 1 + x2 + x [2] 3 + x4
g1(x) = x1 + x2 + 4x3 + 4x4 4 = 0

                g2(x) = x1 + x2 + 2x3 2x4 + 2 = 0.

       -       
It is easy to solve the constraint equations for two of the variables in
terms of the others. Solving for x2 and x3 in terms of x1 and x4 gives


x2 = 3x1 + 8x4 − 8 and x3 = −x1 − 3x4 + 3.

Substituting these expressions into the objective function yields the following
reduced problem:


106CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


min f (x1, x4) = x [2] 1 [+ (3][x][1][ + 8][x][4][ −] [8) + (][−][x][1][ −] [3][x][4][ + 3)][2][ +][ x][4][.]
This problem is unconstrained and therefore it can be solved by the
method of steepest descent, see Section 5.4.1.


Nonlinear Equality Constraints
Now consider the possibility of approximating a problem where the constraints are nonlinear equations by a problem with linear equations, which
can then be solved like the preceding example. To see how this works, consider the following example, which is similar to the preceding one but has
constraints that are nonlinear.


Example 5.6


min f (x) = x [2] 1 + x2 + x [2] 3 + x4
g1(x) = x [2] 1 + x2 + 4x3 + 4x4 4 = 0

                g2(x) = x1 + x2 + 2x3 2x [2] 4 + 2 = 0.

       -       
We use the Taylor series approximation to the constraint functions at
the current point ¯x:


g(x) ≈ g(¯x) + ∇g(¯x)(x − ¯x) [T] .

This gives



x1 x¯1
 x2 x¯2
 x3 x¯3
 x4 x¯4
 












g1(x) ≈ (¯x [2] 1 [+ ¯][x][2][ + 4¯][x][3][ + 4¯][x][4][ −] [4) + (2¯][x][1][,][ 1][,][ 4][,][ 4)]


≈ 2¯x1x1 + x2 + 4x3 + 4x4 − (¯x [2] 1 [+ 4) = 0]













and
g2(x) ≈−x1 + x2 + 2x3 − 4¯x4x4 + (¯x [2] 4 [+ 2) = 0][.]

The idea of the generalized reduced gradient algorithm (GRG) is to solve
a sequence of subproblems, each of which uses a linear approximation of the
constraints. In each iteration of the algorithm, the constraint linearization
is recalculated at the point found from the previous iteration. Typically,
even though the constraints are only approximated, the subproblems yield
points that are progressively closer to the optimal point. A property of the
linearization is that, at the optimal point, the linearized problem has the
same solution as the original problem.
The first step in applying GRG is to pick a starting point. Suppose
that we start with x [0] = (0, −8, 3, 0), which happens to satisfy the original
constraints. It is possible to start from an infeasible point as we discuss
later on. Using the approximation formulas derived earlier, we form our
first approximation problem as follows.
min f (x) = x [2] 1 [+][ x][2][ +][ x] 3 [2] [+][ x][4]
g1(x) = x2 + 4x3 + 4x4 − 4 = 0
g2(x) = −x1 + x2 + 2x3 + 2 = 0.


5.5. CONSTRAINED OPTIMIZATION 107


Now we solve the equality constraints of the approximate problem to
express two of the variables in terms of the others. Arbitrarily selecting x2
and x3, we get


x2 = 2x1 + 4x4 8 and x3 =
            -             - 2 [1] [x][1][ −] [2][x][4][ + 3][.]


Substituting these expressions in the objective function yields the reduced
problem
min f (x1, x4) = x [2] 1 [+ (2][x][1][ + 4][x][2][ −] [8) + (][−] [1] 2 [x][1][ −] [2][x][4][ + 3)][2][ +][ x][4][.]

Solving this unconstrained minimization problem yields x1 = 0.375,

                   x4 = 0.96875. Substituting in the equations for x2 and x3 gives x2 = 4.875
                            and x3 = 1.25. Thus the first iteration of GRG has produced the new point
x [1] = (−0.375, −4.875, 1.25, 0.96875).
To continue the solution process, we would re-linearize the constraint
functions at the new point, use the resulting system of linear equations
to express two of the variables in terms of the others, substitute into the
objective to get the new reduced problem, solve the reduced problem for
x [2], and so forth. Using the stopping criterion ∥x [k][+1] - x [k] ∥ < T where
T = 0.0025, we get the results summarized in Table 5.7.

|k|(xk, xk, xk, xk) f(xk) ∥xk+1 −xk∥<br>1 2 3 4|
|---|---|
|0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8|<br>(0.000, -8.000, 3.000, 0.000)<br>1.000<br>3.729<br>(-0.375, -4.875, 1.250, 0.969)<br>-2.203<br>0.572<br>(-0.423, -5.134, 1.619, 0.620)<br>-1.714<br>0.353<br>(-0.458, -4.792, 1.537, 0.609)<br>-1.610<br>0.022<br>(-0.478, -4.802, 1.534, 0.610)<br>-1.611<br>0.015<br>(-0.488, -4.813, 1.534, 0.610)<br>-1.612<br>0.008<br>(-0.494, -4.818, 1.534, 0.610)<br>-1.612<br>0.004<br>(-0.497, -4.821, 1.534, 0.610)<br>-1.612<br>0.002<br>(-0.498, -4.823, 1.534, 0.610)<br>-1.612|



Table 5.7: Summarized results


This is to be compared with the optimum solution which is


x [∗] = (−0.500, −4.825, 1.534, 0.610)

and has an objective value of -1.612. Note that, in Table 5.7, the values of
the function f (x [k] ) are sometimes smaller than the minimum value for k = 1,
and 2. How is this possible? The reason is that the points x [k] computed by
GRG are usually not feasible to the constraints. They are only feasible to a
linear approximation of these constraints.


Now we discuss the method used by GRG for starting at an infeasible
solution: a phase 1 problem is solved to construct a feasible one. The objective function for the phase 1 problem is the sum of the absolute values
of the violated constraints. The constraints for the phase 1 problem are the
non-violated ones. Suppose we had started at the point x [0] = (1, 1, 0, 1) in


108CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


our example. This point violates the first constraint but satisfies the second,
so the phase 1 problem would be
min |x [2] 1 [+][ x][2][ + 4][x][3][ + 4][x][4][ −] [4][|]
−x1 + x2 + 2x3 − 2x [2] 4 [+ 2] = 0.
Once a feasible solution has been found by solving the phase 1 problem,
the method illustrated above is used to find an optimal solution.



Linear Inequality Constraints
Finally, we discuss how GRG solves problems having inequality constraints as well as equalities. At each iteration, only the tight inequality
constraints enter into the system of linear equations used for eliminating
variables (these inequality constraints are said to be active). The process
is complicated by the fact that active inequality constraints at the current
point may need to be released in order to move to a better solution. We
illustrate the ideas on the following example.
min f (x1, x2) = (x1 − 2 [1] [)][2] + (x2 − [5] 2 [)][2]



2 [)][2] + (x2 2

[1] - [5]




[5] 2 [)][2]



x1 x2 0

 - ≥
x1 0
≥
x2 0
≥
x2 2.
≤



3


2


1



GRG iterates



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-107-0.png)









x1





Figure 5.5: Progress of the Generalized Reduced Gradient Algorithm


The feasible set of this problem is shown in Figure 5.5. The arrow in the
figure indicate the feasible hyperplanes dictated by each constraint. Suppose
that we start from x [0] = (1, 0). This point satisfies all the constraints. As
can be seen from Figure 5.5, x1 x2 0, x1 0 and x2 2 are inactive,
             - ≥ ≥ ≤
whereas the constraint x2 0 is active. We have to decide whether x2
≥
should stay at its lower bound or be allowed to leave its bound.


f (x [0] ) = (2x [0] 1 2
∇ [−] [1][,][ 2][x][0] [−] [5) = (1][,][ −][5)][.]


5.5. CONSTRAINED OPTIMIZATION 109


This indicates that we will get the largest decrease in f if we move in the
direction d [0] = f (x [0] ) = ( 1, 5), i.e. if we decrease x1 and increase
−∇     x2. Since this direction is towards the interior of the feasible region, we
decide to release x2 from its bound. The new point will be x [1] = x [0] + α [0] d [0],
for some α [0] - 0. The constraints of the problem induce an upper bound
on α [0], namely α [0] ≤ 0.8333. Now we perform a line search to determine
the best value of α [0] in this range. It turns out to be α [0] = 0.8333, so
x [1] = (0.8333, 0.8333); see Figure 5.5.
Now, we repeat the process: the constraint x1 x2 0 has become

               - ≥
active whereas the others are inactive. Since the active constraint is not a
simple upper or lower bound constraint, we introduce a surplus variable, say
x3, and solve for one of the variables in terms of the others. Substituting
x1 = x2 + x3, we obtain the reduced optimization problem



2 [)][2][ + (][x][2][ −] [5] 2

[1]



min f (x2, x3) = (x2 + x3 2
            - [1]



0 x2 2
≤ ≤
x3 0.
≥




[5] 2 [)][2]



The reduced gradient is


∇f (x2, x3) = (2x2 + 2x3 − 1 + 2x2 − 5, 2x2 + 2x3 − 1)
= ( 2.667, 0.667) at point (x2, x3) [1] = (0.8333, 0).

       

Therefore, the largest decrease in f occurs in the direction (2.667, −0.667),
that is when we increase x2 and decrease x3. But x3 is already at its lower
bound, so we cannot decrease it. Consequently, we keep x3 at its bound,
i.e. we move in the direction d [1] = (2.667, 0) to a new point (x2, x3) [2] =
(x2, x3) [1] + α [1] d [1] . A line search in this direction yields α [1] = 0.25 and
(x2, x3) [2] = (1.5, 0). The same constraints are still active so we may stay
in the space of variables x2 and x3. Since


f (x2, x3) = (0, 2) at point (x2, x3) [2] = (1.5, 0)
∇

is perpendicular to the boundary line at the current solution x [2] and points
towards the exterior of the feasible region, no further decrease in f is possible. We have found the optimal solution. In the space of original variables,
this optimal solution is x1 = 1.5 and x2 = 1.5.
This is how some of the most widely distributed nonlinear programming
solvers, such as Excel’s SOLVER, GINO, CONOPT, GRG2 and several
others, solves nonlinear programs, with just a few additional details such
as the Newton-Raphson direction for line search. Compared with linear
programs, the problems that can be solved within a reasonable amount of
computational time are typically smaller and the solutions produced may not
be very accurate. Furthermore, the potential non-convexity in the feasible
set or in the objective function may generate local optimal solutions which
are far from a global solution. Therefore, the interpretation of the output
of a nonlinear program requires more care.


110CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS


Exercise 5.15 Consider the following optimization problem:

min f (x1, x2) = −x1 − x2 − x1x2 + [1] 2 [x] 1 [2] [+][ x] 2 [2]

s.t. x1 + x [2] 2 3,
≤
x [2] 1 = 3,

[−] [x][2]
(x1, x2) 0.
≥

Find a solution to this problem using the generalized reduced gradient approach.


5.5.2 Sequential Quadratic Programming


Consider a general nonlinear optimization problem:


minx f (x)
gi(x) = 0, i (5.20)
∈E
gi(x) 0, i .
≥ ∈I

To solve this problem, one might try to capitalize on the good algorithms
available for solving the more structured and easier quadratic programs
(see Chapter 7). This is the idea behind sequential quadratic programming.
At the current feasible point x [k], the problem (5.20) is approximated by a
quadratic program: a quadratic approximation of the Lagrangian function is
computed as well as linear approximations of the constraints. The resulting
quadratic program is of the form



where



min f (x [k] ) [T] (x x [k] ) + [1]
∇  - 2 [(][x][ −] [x][k][)][T] [B][k][(][x][ −] [x][k][)]

gi(x [k] ) [T] (x x [k] ) + gi(x [k] ) = 0 for all i (5.21)
∇  - ∈E
gi(x [k] ) [T] (x x [k] ) + gi(x [k] ) 0 for all i
∇  - ≥ ∈I


B [k] = ∇xx [2] [L][(][x][k][, λ][k][)]



is the Hessian of the Lagrangian function (5.11) with respect to the x variables and λ [k] is the current estimate of the Lagrange multipliers.
This problem can be solved with one of the specialized algorithms for
quadratic programming problems such as the interior-point methods we discuss in Chapter 7. The optimal solution of the quadratic program is used to
determine a search direction. Then a line search or trust region procedure
is performed to determine the next iterate.
Perhaps the best way to think of sequential quadratic programming is as
an extension of the optimization version of Newton’s method to constrained
problems. Recall that the optimization version of Newton’s method uses a
quadratic approximation to the objective function and defines the minimizer
of this approximation as the next iterate, much like what we described for the
SQP method. Indeed, for an unconstrained problem, the SQP is identical to
Newton’s method. For a constrained problem, the optimality conditions for
the quadratic problem we solve in SQP correspond to the Newton direction
for the optimality conditions of the original problem at the current iterate.


5.6. NONSMOOTH OPTIMIZATION: SUBGRADIENT METHODS 111


Sequential quadratic programming iterates until the solution converges.
Much like Newton’s method, the SQP approaches are very powerful, especially if equipped with line search or trust region methodologies to navigate
the nonlinearities and nonconvexities. We refer the reader to the survey of
Boggs and Tolle [14] and the text by Nocedal and Wright [55] for further
details on the sequential quadratic programming approach.


Exercise 5.16 Consider the following nonlinear optimization problem with
equality constraints:


min f (x) = x [2] 1 + x2 + x [2] 3 + x4
g1(x) = x [2] 1 + x2 + 4x3 + 4x4 4 = 0

                g2(x) = x1 + x2 + 2x3 2x [2] 4 + 2 = 0.

       -       
Construct the quadratic programming approximation (5.21) for this problem
at point x [0] = (0, −8, 3, 0) and derive the KKT conditions for this quadratic
programming problem.

#### 5.6 Nonsmooth Optimization: Subgradient Meth- ods


In this section, we consider unconstrained nonlinear programs of the form


min f (x)


where x = (x1, . . ., xn) and f is a nondifferentiable convex function. Optimality conditions based on the gradient are not available since the gradient
is not defined in this case. However, the notion of gradient can be generalized as follows. A subgradient of f at point x [∗] is a vector s [∗] = (s [∗] 1 [, . . ., s] n [∗] [)]
such that
s [∗] (x − x [∗] ) ≤ f (x) − f (x [∗] ) for every x.

When the function f is differentiable, the subgradient is identical to the
gradient. When f is not differentiable at point x, there are typically many
subgradients at x. For example, consider the convex function of one variable


f (x) = max{1 − x, x − 1} = |x − 1|.

As is evident from Figure 5.6 this function is nondifferentiable at the point
x = 1 and it is easy to verify that any vector s such that −1 ≤ s ≤ 1 is
a subgradient of f at point x = 1. Some of these subgradients and the
linear approximations defined by them are shown in Figure 5.6. Note that
each subgradient of the function at a point defines a linear “tangent” to the
function that stays always below the plot of the function–this is the defining
property of subgradients.
Consider a nondifferentiable convex function f . The point x [∗] is a minimum of f if and only if f has a zero subgradient at x [∗] . In the above
example, 0 is a subgradient of f at point x [∗] = 1 and therefore this is where
the minimum of f is achieved.


112CHAPTER 5. NONLINEAR PROGRAMMING: THEORY AND ALGORITHMS



3


2.5


2


1.5


1


0.5


0


−0.5


−1


−1.5



A simple nonsmooth function and subgradients



−2

|s=0|f(x)=|x−1||
|---|---|
|s=−2/3<br>**s=1/2**<br>|s=−2/3<br>**s=1/2**<br>|

−1 −0.5 0 0.5 1 1.5 2 2.5 3

x



Figure 5.6: Subgradients provide under-estimating approximations to functions


The method of steepest descent can be extended to nondifferentiable
convex functions by computing any subgradient direction and using the opposite direction to make the next step. Although subgradient directions are
not always directions of ascent, one can nevertheless guarantee convergence
to the optimum point by choosing the step size appropriately.
A generic subgradient method can be stated as follows.


1. Initialization: Start from any point x [0] . Set i = 0.
2. Iteration i: Compute a subgradient s [i] of f at point x [i] . If s [i] is 0
or close to 0, stop. Otherwise, let x [i][+1] = x [i] αis [i], where αi - 0 denotes a

             step size, and perform the next iteration.


Several choices of the step size αi have been proposed in the literature.
Tocreasedguaranteevery slowlyconvergence(for exampleto the optimum,αi 0 suchthe thatstep size [�] i [α] α [i] i [=] needs [+][∞] to [will] be [do).] de→
But the slow decrease in αi results in slow convergence of xi to the optimum.
In practice, in order to get fast convergence, the following choice is popular:
start from α0 = 2 and then half the step size if no improvement in the objective value f (x [i] ) is observed for k consecutive iterations (k = 7 or 8 is often
used). This choice is well suited when one wants to get close to the optimum
quickly and when finding the exact optimum is not important (this is the
case in integer programming applications where subgradient optimization is
used to obtain quick bounds in branch-and-bound algorithms). With this in
mind, a stopping criterion that is frequently used in practice is a maximum
number of iterations (say 200) instead of “s [i] is 0 or close to 0”.
We will see in Chapter 12 how subgradient optimization is used in a
model to construct an index fund.


## Chapter 6

# NLP Models: Volatility Estimation

Volatility is a term used to describe how much the security prices, market
indices, interest rates, etc. move up and down around their mean. It is measured by the standard deviation of the random variable that represents the
financial quantity we are interested in. Most investors prefer low volatility
to high volatility and therefore expect to be rewarded with higher long-term
returns for holding higher volatility securities.
Many financial computations require volatility estimates. Mean-variance
optimization trades off the expected return and volatility of a portfolio of securities. Celebrated option valuation formulas of Black, Scholes, and Merton
(BSM) involve the volatility of the underlying security. Risk management
revolves around the volatility of the current positions. Therefore, accurate
estimation of the volatilities of security returns, interest rates, exchange rates
and other financial quantities is crucial to many quantitative techniques in
financial analysis and management.
Most volatility estimation techniques can be classified as either a historical or an implied method. One either uses historical time series to infer
patterns and estimates the volatility using a statistical technique, or considers the known prices of related securities such as options that may reveal
the market sentiment on the volatility of the security in question. GARCH
models exemplify the first approach while the implied volatilities calculated
from the BSM formulas are the best known examples of the second approach.
Both types of techniques can benefit from the use of optimization formulations to obtain more accurate volatility estimates with desirable characteristics such as smoothness. We discuss two examples in the remainder of this
chapter.

#### 6.1 Volatility Estimation with GARCH Models


Empirical studies analyzing time series data for returns of securities, interest
rates, and exchange rates often reveal a clustering behavior for the volatility of the process under consideration. Namely, these time series exhibit


113


114 CHAPTER 6. NLP MODELS: VOLATILITY ESTIMATION


high volatility periods alternating with low volatility periods. These observations suggest that future volatility can be estimated with some degree of
confidence by relying on historical data.
Currently, describing the evolution of such processes by imposing a stationary model on the conditional distribution of returns is one of the most
popular approaches in the econometric modeling of financial time series.
This approach expresses the conventional wisdom that models for financial returns should adequately represent the nonlinear dynamics that are
demonstrated by the sample autocorrelation and cross-correlation functions
of these time series. ARCH (autoregressive conditional heteroscedasticity)
and GARCH (generalized ARCH) models of Engle [25] and Bollerslev [15]
have been popular and successful tools for future volatility estimation. For
the multivariate case, rich classes of stationary models that generalize the
univariate GARCH models have also been developed; see, for example, the
comprehensive survey by Bollerslev et al. [16].
The main mathematical problem to be solved in fitting ARCH and
GARCH models to observed data is the determination of the best model
parameters that maximize a likelihood function, i.e., an optimization problem. Typically, these models are presented as unconstrained optimization
problems with recursive terms. In a recent study, Altay-Salih et al. [1] argue that because of the recursion equations and the stationarity constraints,
these models actually fall into the domain of nonconvex, nonlinearly constrained nonlinear programming. This study shows that using a sophisticated nonlinear optimization package (sequential quadratic programming
based FILTER method of Fletcher and Leyffer [28] in their case) they are
able to significantly improve the log-likelihood functions for multivariate
volatility (and correlation) estimation. While this study does not provide a
comparison of forecasting effectiveness of the standard approaches to that of
the constrained optimization approach, the numerical results suggest that
constrained optimization approach provides a better prediction of the extremal behavior of the time series data; see [1]. Here, we briefly review this
constrained optimization approach for expository purposes.
We consider a stochastic process Y indexed by natural numbers. Yt, its
value at time t, is an n-dimensional vector of random variables. Autoregressive behavior of these random variables is modeled as:



Yt =



�m

φiYt i + εt (6.1)

   i=1



where m is a positive integer representing the number of periods we look
back in our model and εt satisfies


E[εt|ε1, . . ., εt−1] = 0.

While these models are of limited value, if at all, in the estimation of the
actual time series (Yt), they have been shown to provide useful information
for volatility estimation. For this purpose, GARCH models define


ht := E[ε [2] t

[|][ε][1][, . . ., ε][t][−][1][]]


6.1. VOLATILITY ESTIMATION WITH GARCH MODELS 115


in the univariate case and


Ht := E[εtε [T] t

[|][ε][1][, . . ., ε][t][−][1][]]

in the multivariate case. Then one models the conditional time dependence
of these squared residuals in the univariate case as follows:



�p

βjht−j. (6.2)
j=1



ht = c +



�q

αiε [2] t i [+]

   i=1



This model is called GARCH(p, q). Note that ARCH models correspond to
choosing p = 0.
The generalization of the model (6.2) to the multivariate case can be
done in a number of ways. One approach is to use the operator vech to
turn the matrices Ht and εtε [T] t [into vectors.] [The operator][ vech][ takes an][ n][×][n]
symmetric matrix as an input and produces an [n][(][n][+1)] -dimensional vector

2
as output by stacking the elements of the matrix on and below the diagonal
on top of each other. Using this operator, one can write a multivariate
generalization of (6.2) as follows:



�p

Bjvech(Ht−j)(6.3).
j=1



vech(Ht) = vech(C) +



�q

Aivech(εt iε [T] t i [) +]

     -      i=1



In (6.3), Ai’s and Bj’s are square matrices of dimension [n][(][n] 2 [+1)] and C is an

n × n symmetric matrix.
After choosing a superstructure for the GARCH model, that is, after
choosing p and q, the objective is to determine the optimal parameters φi,
αi, and βj. Most often, this is achieved via maximum likelihood estimation.
If one assumes a normal distribution for Yt conditional on the historical
observations, the log-likelihood function can be written as follows [1]:




- [T] 2




[T] 2 [log 2][π][ −] 2 [1]



�T



2



log ht
t=1 - 2 [1]



2



�T


t=1



ε [2] t, (6.4)
ht



in the univariate case and




- [T] 2




[T] 2 [log 2][π][ −] 2 [1]



�T



2



log det Ht
t=1 - 2 [1]



2



�T

ε [T] t [H] t [−][1] εt (6.5)
t=1



in the multivariate case.


Exercise 6.1 Show that the function in (6.4) is a difference of convex func
t
tions by showing that log ht is concave and h [ε][2] t [is] [convex] [in] [ε][t] [and] [h][t][.] [Does]
the same conclusion hold for the function in (6.5)?


Now, the optimization problem to solve in the univariate case is to maximize the log-likelihood function (6.4) subject to the model constraints (6.1)
and (6.2) as well as the condition that ht is nonnegative for all t since


116 CHAPTER 6. NLP MODELS: VOLATILITY ESTIMATION


ht = E[ε [2] t [In] [the] [multivariate] [case] [we] [maximize] [(6.5)] [subject]

[|][ε][1][, . . ., ε][t][−][1][].]
to the model constraints (6.1) and (6.3) as well as the condition that Ht is a
positive semidefinite matrix for all t since Ht defined as E[εtε [T] t

[|][ε][1][, . . ., ε][t][−][1][]]
must necessarily satisfy this condition. The positive semidefiniteness of the
matrices Ht can either be enforced using the techniques discussed in Chapter 9 or using a reparametrization of the variables via Cholesky-type LDL [T]

decomposition as discussed in [1].
An important issue in GARCH parameter estimation is the stationarity properties of the resulting model. There is a continuing debate about
whether it is reasonable to assume that the model parameters for financial
time series are stationary over time. It is, however, clear that the estimation
and forecasting is easier on stationary models. A sufficient condition for the
stationarity of the univariate GARCH model above is that αi’s and βj’s as
well as the scalar c are strictly positive and that



�q

αi +
i=1



�p

βj < 1, (6.6)
j=1



see, for example, [33]. The sufficient condition for the multivariate case is
more involved and we refer the reader to [1] for these details.
Especially in the multivariate case, the problem of maximizing the loglikelihood function with respect to the model constraints is a difficult nonlinear, non-convex optimization problem. To find a quick solution, more
tractable versions of the model (6.3) have been developed where the model
is simplified by imposing additional structure on the matrices Ai and Bj such
as diagonality. While the resulting problems are easier to solve, the loss of
generality from their simplifying assumptions can be costly. As Altay-Salih
et al. demonstrate, using the full power of state-of-the-art constrained optimization software, one can solve the more general model in reasonable computational time (at least for bivariate and trivariate estimation problems)
with much improved log-likelihood values. While the forecasting efficiency
of this approach is still to be tested, it is clear that sophisticated nonlinear
optimization is emerging as a valuable tool in volatility estimation problems
that use historical data.


Exercise 6.2 Consider the model in (6.3) for the bivariate case when q = 1
and p = 0 (i.e., an ARCH(1) model). Explicitly construct the nonlinear programming problem to be solved in this case. The comparable simplification
of the BEKK representation [3] gives


Ht = C [T] C + A [T] εt 1ε [t] t 1 [A.]

                -                
Compare these two models and comment on the additional degrees of freedom in the NLP model. Note that the BEKK representation ensures the
positive semidefiniteness of Ht by construction at the expense of lost degrees
of freedom.


Exercise 6.3 Test the NLP model against the model resulting from the
BEKK representation in the previous exercise using daily return data for


6.2. ESTIMATING A VOLATILITY SURFACE 117


two market indices, e.g., S & P 500 and FTSE 100, and an NLP solver.
Compare the optimal log-likelihood values achieved by both models and
comment.

#### 6.2 Estimating a Volatility Surface


The discussion in this section is largely based on the work of Coleman, Kim,
Li, and Verma, see [21, 20].
The BSM equation for pricing European options is based on a geometric Brownian motion model for the movements of the underlying security.
Namely, one assumes that the underlying security price St at time t satisfies


dSt

= µdt + σdWt (6.7)
St


where µ is the drift, σ is the (constant) volatility, and Wt is the standard
Brownian motion. Using this equation and some standard assumptions
about the absence of frictions and arbitrage opportunities, one can derive
the BSM partial differential equation for the value of a European option on
this underlying security. Using the boundary conditions resulting from the
payoff structure of the particular option, one determines the value function
for the option. Recall from Exercise 5.3 that the price of a European call
option with strike K and maturity T is given by:


C(K, T ) = S0Φ(d1) Ke [−][rT] Φ(d2), (6.8)
                  
where




[S][0] [σ][2]

K [) + (][r][ +] 2



d1 = log( [S] K [0]



σ ~~√~~

T,



2 [)][T]



d2 = d1 σ ~~√~~
     


,
T



and Φ(·) is the cumulative distribution function for the standard normal
distribution. r in the formula represents the continuously compounded riskfree and constant interest rate and σ is the volatility of the underlying
security that is assumed to be constant. Similarly, the European put option
price is given by


P (K, T ) = Ke [−][rT] Φ( d2) S0Φ( d1). (6.9)

            -            -            
The risk-free interest rate r, or a reasonably close approximation to it is often
available, for example from Treasury bill prices in US markets. Therefore,
all one needs to determine the call or put price using these formulas is a
reliable estimate of the volatility parameter σ. Conversely, given the market
price for a particular European call or put, one can uniquely determine the
volatility of the underlying asset implied by this price, called its implied
volatility, by solving the equations above with the unknown σ. Any one of
the univariate equation solving techniques we discussed in Section 5.3 can
be used for this purpose.


118 CHAPTER 6. NLP MODELS: VOLATILITY ESTIMATION


Empirical evidence against the appropriateness of (6.7) as a model for
the movements of most securities is abundant. Most studies refute the assumption of a volatility that does not depend on time or underlying price
level. Indeed, studying the prices of options with same maturity but different strikes, researchers observed that the implied volatilities for such options often exhibit a “smile” structure, i.e., higher implied volatilities away
from the money in both directions, decreasing to a minimum level as one
approaches the at-the-money option from in-the-money or out-of-the-money
strikes. This is clearly in contrast with the constant (flat) implied volatilities
one would expect had (6.7) been an appropriate model for the underlying
price process.
There are many models that try to capture the volatility smile including
stochastic volatility models, jump diffusions, etc. Since these models introduce non-traded sources of risk, perfect replication via dynamic hedging as
in BSM approach becomes impossible and the pricing problem is more complicated. An alternative that is explored in [21] is the one-factor continuous
diffusion model:


dSt

= µ(St, t)dt + σ(St, t)dWt, t [0, T ] (6.10)
St ∈


where the constant parameters µ and σ of (6.7) are replaced by continuous
and differentiable functions µ(St, t) and σ(St, t) of the underlying price St
and time t. T denotes the end of the fixed time horizon. If the instantaneous
risk-free interest rate r is assumed constant and the dividend rate is constant,
given a function σ(S, t), a European call option with maturity T and strike
K has a unique price. Let us denote this price with C(σ(S, t), K, T ).
While an explicit solution for the price function C(σ(S, t), K, T ) as in
(6.8) is no longer possible, the resulting pricing problem can be solved efficiently via numerical techniques. Since µ(S, t) does not appear in the generalized BSM partial differential equation, all one needs is the specification of
the function σ(S, t) and a good numerical scheme to determine the option
prices in this generalized framework.
So, how does one specify the function σ(S, t)? First of all, this function
should be consistent with the observed prices of currently or recently traded
options on the same underlying security. If we assume that we are given
market prices of m call options with strikes Kj and maturities Tj in the
form of bid-ask pairs (βj, αj) for j = 1, . . ., n, it would be reasonable to
require that the volatility function σ(S, t) is chosen so that


βj C(σ(S, t), Kj, Tj) αj, j = 1, . . ., n. (6.11)
≤ ≤


To ensure that (6.11) is satisfied as closely as possible, one strategy is to
minimize the violations of the inequalities in (6.11):



min
σ(S,t)∈H



�n

[βj C(σ(S, t), Kj, Tj)] [+] + [C(σ(S, t), Kj, Tj) αj] [+] . (6.12)

  -   j=1


6.2. ESTIMATING A VOLATILITY SURFACE 119


Above, H denotes the space of measurable functions σ(S, t) with domain
IR [+] × [0, T ] and u [+] = max{0, u}. Alternatively, using the closing prices
Cj for the options under consideration, or choosing the mid-market prices
Cj = (βj +αj)/2, we can solve the following nonlinear least squares problem:



min
σ(S,t)∈H



�n

(C(σ(S, t), Kj, Tj) Cj) [2] . (6.13)
          j=1



This is a nonlinear least squares problem since the function C(σ(S, t), Kj, Tj)
depends nonlinearly on the variables, namely the local volatility function
σ(S, t).
While the calibration of the local volatility function to the observed
prices using the objective functions in (6.12) and (6.13) is important and desirable, there are additional properties that are desirable in the local volatility function. Arguably, the most common feature sought in existing models
is smoothness. For example, in [46] authors try to achieve a smooth volatility
function by appending the objective function in (6.13) as follows:



min
σ(S,t)∈H



�n

(C(σ(S, t), Kj, Tj) Cj) [2] + λ σ(S, t) 2. (6.14)
          - ∥∇ ∥
j=1



Here, λ is a positive trade-off parameter and 2 represents the L [2] -norm.
∥· ∥
Large deviations in the volatility function would result in a high value for
the norm of the gradient function and by penalizing such occurrences, the
formulation above encourages a smoother solution to the problem. The most
appropriate value for the trade-off parameter λ must be determined experimentally. To solve the resulting problem numerically, one must discretize
the volatility function on the underlying price and time grid. Even for a
relatively coarse discretization of the St and t spaces, one can easily end up
with an optimization problem with many variables.
An alternative strategy is to build the smoothness into the volatility
function by modeling it with spline functions. To define a spline function, the
domain of the function is partitioned into smaller subregions and then, the
spline function is chosen to be a polynomial function in each subregion. Since
polynomials are smooth functions, spline functions are smooth within each
subregion by construction and the only possible sources of nonsmoothness
are the boundary regions between subregions. When the polynomial is of a
high enough degree, the continuity and differentiability of the spline function
at the boundaries between subregions can be ensured by properly choosing
the polynomial function coefficients. This strategy is similar to the model
we consider in more detail in Section 8.4, except that here we model the
volatility function rather than the risk-neutral density and also we generate
a function that varies over time rather than an estimate at a single point
in time. We defer a more detailed discussion of spline functions to Section
8.4. The use of the spline functions not only guarantees the smoothness of
the resulting volatility function estimates but also reduces the degrees of
freedom in the problem. As a consequence, the optimization problem to be


120 CHAPTER 6. NLP MODELS: VOLATILITY ESTIMATION


solved has much fewer variables and is easier. This strategy is proposed in

[21] and we review it below.
We start by assuming that σ(S, t) is a bi-cubic spline. While higher-order
splines can also be used, cubic splines often offer a good balance between
flexibility and complexity. Next we choose a set of spline knots at points
( S [¯] j, t [¯] j) for j = 1, . . ., k. If the value of the volatility function at these points
is given by σ¯j := σ( S [¯] j, t [¯] j), the interpolating cubic spline that goes through
these knots and satisfies a particular end condition is uniquely determined.
For example, in Section 8.4 we use the natural spline end condition which
sets the second derivative of the function at the knots at the boundary
of the domain to zero to obtain our cubic spline approximations uniquely.
Therefore, to completely determine the volatility function as a natural bicubic spline and to determine the resulting call option prices we have k
degrees of freedom represented with the choices σ¯ = (¯σ1, . . ., ¯σk).
Let Σ(S, t, ¯σ) the bi-cubic spline local volatility function obtained setting σ( S [¯] j, t [¯] j)’s to σ¯j. Let C(Σ(S, t, ¯σ), S, t) denote the resulting call price
function. The analog of the objective function (6.13) is then



min
σ¯∈IR [k]



�n

(C(Σ(S, t, ¯σ), Kj, Tj) Cj) [2] . (6.15)
           j=1



One can introduce positive weights wj for each of the terms in the objective function above to address different accuracies or confidence in the call
prices Cj. We can also introduce lower and upper bounds li and ui for the
volatilities at each knot to incorporate additional information that may be
available from historical data, etc. This way, we form the following nonlinear
least-squares problem with k variables:



min f (σ) :=
σ¯∈IR [k]



�n

wj (C(Σ(S, t, ¯σ), Kj, Tj) − Cj) [2] (6.16)
j=1



s.t. l ≤ σ¯ ≤ u.


It should be noted that the formulation above will not be appropriate if
there are many more knots than prices, that is if k is much larger than n. In
this case, the problem will be underdetermined and solutions may exhibit
consequences of “over-fitting”. It is better to use fewer knots than available
option prices.
The problem (6.16) is a standard nonlinear optimization problem except
that the term C(Σ(S, t, ¯σ), Kj, Tj) in the objective function depends on the
decision variables σ¯ in a complicated and non-explicit manner. Since most
of the nonlinear optimization methods we discussed in the previous chapter require at least the gradient of the objective function (and sometimes
its Hessian matrix as well), is potentially troublesome. Without an explicit
expression for f, its gradient must be either estimated using a finite difference scheme or using automatic differentiation. Coleman et al. implement
both alternatives and report that local volatility functions can be estimated
very accurately using these strategies. They also test the hedging accuracy


6.2. ESTIMATING A VOLATILITY SURFACE 121


of different delta-hedging strategies, one using a constant volatility estimation and another using the local volatility function produced by the strategy
above. These tests indicate that the hedges obtained from the local volatility
function are significantly more accurate.


Exercise 6.4 The partial derivative ∂f (x)/∂xi of the function f (x) with
respect to the i-th coordinate of the x vector can be estimated as



(x)

∂xi ≈ [f] [(][x][ +][ he] h [i][)][ −] [f] [(][x][)]



∂f (x)



,
h



where ei denotes the i-th unit vector. Assuming that f is continuously differentiable, provide an upper bound on the estimation error from this finite
difference approximation using Taylor series expansion for the function f
around x. Next, compute a similar bound for the alternative finite difference formula given by



(x)

∂xi ≈ [f] [(][x][ +][ he][i][)][ −] 2h [f] [(][x][ −] [he][i][)]



∂f (x)



.
2h



Comment on the potential advantages and disadvantages of these two approaches.


122 CHAPTER 6. NLP MODELS: VOLATILITY ESTIMATION


## Chapter 7

# Quadratic Programming: Theory and Algorithms

#### 7.1 The Quadratic Programming Problem

As we discussed in the introductory chapter, quadratic programming (QP)
refers to the problem of minimizing a quadratic function subject to linear
equality and inequality constraints. In its standard form, this problem is
represented as follows:


( ) minx 21 [x][T][ Qx][ +][ c][T][ x]
QP
Ax = b (7.1)
x ≥ 0,

where A ∈ IR [m][×][n], b ∈ IR [m], c ∈ IR [n], Q ∈ IR [n][×][n] are given, and x ∈ IR [n] .
QPs are special classes of nonlinear optimization problems and contain linear
programming problems as special cases.
Quadratic programming structures are encountered frequently in optimization models. For example, ordinary least squares problems which are
used often in data fitting are QPs with no constraints. Mean-variance optimization problems developed by Markowitz for the selection of efficient
portfolios are QP problems. In addition, QP problems are solved as subproblems in the solution of general nonlinear optimization problems via sequential quadratic programming (SQP) approaches; see Section 5.5.2.
Recall that, when Q is a positive semidefinite matrix, i.e., when y [T] Qy ≥
0 for all y, the objective function of problem QP is a convex function of x.
Since the feasible set is a polyhedral set (i.e., a set defined by linear constraints) it is a convex set. Therefore, when Q is positive semidefinite, the
QP (7.1) is a convex optimization problem. As such, its local optimal solutions are also global optimal solutions. This property is illustrated in Figure
7.1 where the contours of a quadratic function with a positive semidefinite
Q are contrasted with those of an indefinite Q.


Exercise 7.1 Consider the quadratic function f (x) = c [T] x + [1]

2 [x][T][ Qx][, where]
the matrix Q is n by n and symmetric.


123


124CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS



4


3


2


1


0


−1


−2


−3



4


3


2


1


0


−1


−2


−3



Contours of a convex function



Contours of a nonconvex function



−4
−4 −3 −2 −1 0 1 2 3 4

x1



−4
−4 −3 −2 −1 0 1 2 3 4

x1



Figure 7.1: Contours of positive semidefinite and indefinite quadratic functions


a. Prove that if x [T] Qx < 0 for some x, then f is unbounded below.


b. Prove that if Q is positive semidefinite (but not positive definite), then
either f is unbounded below or it has an infinite number of solutions.


c. True or false: f has a unique minimizer if and only if Q is positive
definite.


As in linear programming, we can develop a dual of quadratic programming problems. The dual of the problem (7.1) is given below:


( ) maxx,y,s b [T] y 12 [x][T][ Qx]
QD    A [T] y          - Qx + s = c (7.2)
x, s ≥ 0.


Note that, unlike the case of linear programming, the variables of the primal
quadratic programming problem also appear in the dual QP.

#### 7.2 Optimality Conditions


One of the fundamental tools in the study of optimization problems is the
Karush-Kuhn-Tucker theorem that gives a list of conditions which are necessarily satisfied at any (local) optimal solution of a problem, provided that
some mild regularity assumptions are satisfied. These conditions are commonly called KKT conditions and were already discussed in the context of
general nonlinear optimization problems in Section 5.5.
Applying the KKT theorem to the QP problem (7.1), we obtain the
following set of necessary conditions for optimality:


Theorem 7.1 Suppose that x is a local optimal solution of the QP given
in (7.1) so that it satisfies Ax = b, x ≥ 0 and assume that Q is a positive
semidefinite matrix. Then, there exist vectors y and s such that the following


7.2. OPTIMALITY CONDITIONS 125


conditions hold:



A [T] y − Qx + s = c (7.3)



s ≥ 0 (7.4)



xisi = 0, i. (7.5)
∀



Furthermore, x is a global optimal solution.


Note that the positive semidefiniteness condition related to the Hessian
of the Lagrangian function in the KKT theorem is automatically satisfied
for convex quadratic programming problems, and therefore is not included
in Theorem 7.1.


Exercise 7.2 Show that in the case of a positive definite Q, the objective function of (7.1) is strictly convex, and therefore, must have a unique
minimizer.


Conversely, if vectors x, y and s satisfy conditions (7.3)-(7.5) as well as
primal feasibility conditions


Ax = b (7.6)

x ≥ 0 (7.7)

then, x is a global optimal solution of (7.1). In other words, conditions
(7.3)-(7.7) are both necessary and sufficient for x, y, and s to describe a
global optimal solution of the QP problem.
In a manner similar to linear programming, optimality conditions (7.3)(7.7) can be seen as a collection of conditions for


1. primal feasibility: Ax = b, x ≥ 0,

2. dual feasibility: A [T] y − Qx + s = c, s ≥ 0, and

3. complementary slackness: for each i = 1, . . ., n we have xisi = 0.


Using this interpretation, one can develop modifications of the simplex
method that can also solve convex quadratic programming problems (Wolfe’s
method). We do not present this approach here. Instead, we describe an
alternative algorithm that is based on Newton’s method; see Section 5.4.2.


Exercise 7.3 Consider the following quadratic program


min x1x2 + x [2] 1 + 32 [x] 2 [2] + 2x [2] 3
+ 2x1 + x2 + 3x3
subject to x1 + x2 + x3 = 1
x1 x2 = 0

           x1 0, x2 0, x3 0.
≥ ≥ ≥



Is the quadratic objective function convex? Show that x [∗] = ( [1]




[1] [1]

2 [,] 2



Is the quadratic objective function convex? Show that x [∗] = ( [is] [an]

2 [,] 2 [,][ 0)]

optimal solution to this problem by finding vectors y and s that satisfy the
optimality conditions jointly with x [∗] .


126CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS

#### 7.3 Interior-Point Methods


In 1984, Karmarkar proved that an Interior-Point Method (IPM) can solve
LPs in polynomial time. The two decades that followed the publication
of Karmarkar’s paper have seen a very intense effort by the optimization
research community to study theoretical and practical properties of IPMs.
One of the early discoveries was that IPMs can be viewed as modifications
of Newton’s method that are able to handle inequality constraints. Some of
the most important contributions were made by Nesterov and Nemirovski
who showed that the IPM machinery can be applied to a much larger class
of problems than just LPs [54]. Convex quadratic programming problems,
for example, can be solved in polynomial time, as well as many other convex
optimization problems using IPMs. For most instances of conic optimization
problems we discuss in Chapter 9 and 10, IPMs are by far the best available
methods.
Here, we will describe a variant of IPMs for convex quadratic programming. For the QP problem in (7.1) we can write the optimality conditions
in matrix form as follows:





0
 0
0





, (x, s) ≥ 0. (7.8)



F (x, y, s) =





A [T] y − Qx + s − c
 Ax − b
XSe





 =



Above, X and S are diagonal matrices with the entries of the x and s vectors,
respectively, on the diagonal, i.e., Xii = xi, and Xij = 0, i = j, and similarly
̸
for S. Also, as before, e is an n-dimensional vector of ones.
The system of equations F (x, y, s) = 0 has n+m+n variables and exactly
the same number of constraints, i.e., it is a “square” system. Because of the
nonlinear equations xisi = 0 we cannot solve this system using linear system
solution methods such as Gaussian elimination. But, since the system is
square we can apply Newton’s method. In fact, without the nonnegativity
constraints, finding (x, y, s) satisfying these optimality conditions would be
a straightforward exercise by applying Newton’s method.
The existence of nonnegativity constraints creates a difficulty. The existence and the number of inequality constraints are among the most important factors that contribute to the difficulty of the solution of any optimization problem. Interior-point approaches use the following strategy to handle
these inequality constraints: One first identifies an initial solution (x [0], y [0], s [0] )
that satisfies the first two (linear) blocks of equations in F (x, y, s) = 0 but
not necessarily the third block XSe = 0, and also satisfies the nonnegativity
constraints strictly, i.e., x [0] - 0 and s [0] - 0. Notice that a point satisfying
some inequality constraints strictly lies in the interior of the region defined
by these inequalities–rather than being on the boundary. This is the reason
why the method we are discussing is called an interior-point method.
Once we find such an (x [0], y [0], s [0] ) we try to generate new points (x [k], y [k], s [k] )
that also satisfy these same conditions and get progressively closer to satisfying the third block of equations. This is achieved via careful application
of a modified Newton’s method.


7.3. INTERIOR-POINT METHODS 127


Let us start by defining two sets related to the conditions (7.8):

F := {(x, y, s) : Ax = b, A [T] y − Qx + s = c, x ≥ 0, s ≥ 0} (7.9)

is the set of feasible points, or simply the feasible set. Note that, we are
using a primal-dual feasibility concept here. More precisely, since x variables
come from the primal QP and (y, s) come from the dual QP, we impose both
primal and dual feasibility conditions in the definition of F. If (x, y, s) ∈F
also satisfy x > 0 and s > 0 we say that (x, y, s) is a strictly feasible solution
and define

F [o] := {(x, y, s) : Ax = b, A [T] y − Qx + s = c, x > 0, s > 0} (7.10)

to be the strictly feasible set. In mathematical terms, F [o] is the relative
interior of the set F.
IPMs we discuss here will generate iterates (x [k], y [k], s [k] ) that all lie in F [o] .
Since we are generating iterates for both the primal and dual problems,
this version of IPMs are often called primal-dual interior-point methods.
Using this approach, we will obtain solutions for both the primal and dual
problems at the end of the solution procedure. Solving the dual may appear
to be a waste of time since we are only interested in the solution of the
primal problem. However, years of computational experience demonstrated
that primal-dual IPMs lead to the most efficient and robust implementations
of the interior-point approach. Intuitively speaking, this happens because
having some partial information on the dual problem in the form of the
dual iterates (y [k], s [k] ) helps us make better and faster improvements on the
iterates of the primal problem.
Iterative optimization algorithms have two essential components:

  - a measure that can be used to evaluate and compare the quality of
alternative solutions and search directions


  - a method to generate a better solution, with respect to the measure
just mentioned, from a non-optimal solution.


As we stated before, IPMs rely on Newton’s method to generate new
estimates of the solutions. Let us discuss this more in depth. Ignore the
inequality constraints in (7.8) for a moment, and focus on the nonlinear
system of equations F (x, y, s) = 0. Assume that we have a current estimate
(x [k], y [k], s [k] ) of the optimal solution to the problem. The Newton step from
this point is determined by solving the following system of linear equations:







J(x [k], y [k], s [k] )



∆x [k]
 ∆y [k]



∆y [k]

∆s [k]





 = −F (x [k], y [k], s [k] ), (7.11)



where J(x [k], y [k], s [k] ) is the Jacobian of the function F and [∆x [k], ∆y [k], ∆s [k] ] [T]

is the search direction. First, we observe that





 (7.12)



J(x [k], y [k], s [k] ) =





−Q A [T] I
 A 0 0
S [k] 0 X [k]


128CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS



where, X [k] and S [k] are diagonal matrices with the components of the vectors
x [k] and s [k] along their diagonals. Furthermore, if (x [k], y [k], s [k] ) ∈F [o], then











F (x [k], y [k], s [k] ) =



0
 0
X [k] S [k] e



 (7.13)



and the Newton equation reduces to
  





0
 0
−X [k] S [k] e





 . (7.14)







∆x [k]
 ∆y [k]



∆y [k]

∆s [k]



−Q A [T] I
 A 0 0
S [k] 0 X [k]











 =



Exercise 7.4 Consider the quadratic programming problem given in Exer



                          cise 7.3 and the current primal-dual estimate of the solution x [k] = 1 [1]
3 [,] 3



3



�T,




   y [k] = 1, [1]




[1] [1]

3 [,] 3



2



�T , and sk = 1 [1]
2 [,] 2



�T

[1] . Is (xk, yk, sk) ? How about o?

2 [,][ 2] ∈F F



Form and solve the Newton equation for this problem at (x [k], y [k], s [k] ).



In the standard Newton method, once a Newton step is determined in
this manner, it is added to the current iterate to obtain the new iterate. In
our case, this action may not be permissible, since the Newton step may
take us to a new point that does not necessarily satisfy the nonnegativity
constraints x ≥ 0 and s ≥ 0. In our modification of Newton’s method, we
want to avoid such violations and therefore will seek a step-size parameter
αk (0, 1] such that x [k] + αk∆x [k] - 0 and s [k] + αk∆s [k] - 0. Note that
∈
the largest possible value of αk satisfying these restrictions can be found
using a procedure similar to the ratio test in the simplex method. Once we
determine the step-size parameter, we choose the next iterate as


(x [k][+1], y [k][+1], s [k][+1] ) = (x [k], y [k], s [k] ) + αk(∆x [k], ∆y [k], ∆s [k] ).


If a value of αk results in a next iterate (x [k][+1], y [k][+1], s [k][+1] ) that is also in,
F [o]
we say that this value of αk is permissible.


Exercise 7.5 What is the largest permissable stepsize αk for the Newton
direction you found in Exercise 7.4?


A naive modification of Newton’s method as we described above is, unfortunately, not very good in practice since the permissible values of αk
eventually become too small and the progress toward the optimal solution
stalls. Therefore, one needs to modify the search direction as well as adjusting the step size along the direction. The usual Newton search direction
obtained from (7.14) is called the pure Newton direction. We will consider
modifications of pure Newton directions called centered Newton directions.
To describe such directions, we first need to discuss the concept of the central
path.


7.4. THE CENTRAL PATH 129

#### 7.4 The Central Path


The central path C is a trajectory in the relative interior of the feasible
region F [o] that is very useful for both the theoretical study and also the
implementation of IPMs. This trajectory is parameterized by a scalar τ - 0,
and the points (xτ, yτ, sτ ) on the central path are obtained as solutions of
the following system:



F (xτ, yτ, sτ ) =





0
 0
τe





, (xτ, sτ ) > 0. (7.15)



Then, the central path C is defined as

= (xτ, yτ, sτ ) : τ        - 0 . (7.16)
C { }

The third block of equations in (7.15) can be rewritten as


(xτ )i(sτ )i = τ, i.
∀

The similarities between (7.8) and (7.15) are evident. Note that instead
of requiring that x and s are complementary vectors as in the optimality
conditions (7.8), we require their component products to be all equal. Note
that as τ → 0, the conditions (7.15) defining the points on the central path
approximate the set of optimality conditions (7.8) more and more closely.
The system (7.15) has a unique solution for every τ   - 0, provided that F [o]

is nonempty. Furthermore, when [o] is nonempty, the trajectory (xτ, yτ, sτ )
F
converges to an optimal solution of the problem (7.1). Figure 7.2 depicts a
sample feasible set and its central path.


Feasible
The Central
region
Path


Optimal
solution


Figure 7.2: The Central Path



Exercise 7.6 Recall the quadratic programming problem given in Exercise




                          7.3 and the current primal-dual estimate of the solution x [k] = 1 [1]
3 [,] 3



3




[1] [1]

3 [,] 3



�T,


130CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS




   y [k] = 1, [1]

2



�T - �T
, and sk = 1 [1] . Verify that (xk, yk, sk) is not on the
2 [,] 2 [,][ 2]



central path. Find a vector xˆ such that (ˆx, y [k], s [k] ) is on the central path.
What value of τ does this primal dual solution correspond to?

#### 7.5 Interior-Point Methods


7.5.1 Path-Following Algorithms


The observation that points on the central path converge to optimal solutions of the primal-dual pair of quadratic programming problems suggests
the following strategy for finding such solutions: In an iterative manner,
generate points that approximate central points for decreasing values of the
parameter τ . Since the central path converges to an optimal solution of
the QP problem, these approximations to central points should also converge to a desired solution. This simple idea is the basis of path-following
interior-point algorithms for optimization problems.
The strategy we outlined in the previous paragraph may appear confusing in a first reading. For example, one might ask why we do not approximate or find the solutions of the optimality system (7.8) directly rather
than generating all these intermediate iterates leading to such a solution.
Or, one might wonder, why we would want to find approximations to central points, rather than central points themselves. Let us respond to these
potential questions. First of all, there is no good and computationally cheap
way of solving (7.8) directly since it involves nonlinear equations of the form
xisi = 0. As we discussed above, if we apply Newton’s method to the equations in (7.8), we run into trouble because of the additional nonnegativity
constraints. While we also have bilinear equations in the system defining
the central points, being somewhat safely away from the boundaries defined
by nonnegativity constraints, central points can be computed without most
of the difficulties encountered in solving (7.8) directly. This is why we use
central points for guidance.
Instead of insisting that we obtain a point exactly on the central path,
we are often satisfied with an approximation to a central point for reasons
of computational efficiency. Central points are also defined by systems of
nonlinear equations and additional nonnegativity conditions. Solving these
systems exactly (or very accurately) can be as hard as solving the optimality
system (7.8) and therefore would not be an acceptable alternative for a practical implementation. It is, however, relatively easy to find a well-defined
approximation to central points–see the definition of the neighborhoods of
the central path below–especially those that correspond to larger values of τ .
Once we identify a point close to a central point on C, we can do a clever and
inexpensive search to find another point which is close to another central
point on C, corresponding to a smaller value of τ . Furthermore, this idea
can be used repeatedly, resulting in approximations to central points with
progressively smaller τ values, allowing us to approach an optimal solution
of the QP we are trying to solve. This is the essence of the path-following
strategies.


7.5. INTERIOR-POINT METHODS 131


7.5.2 Centered Newton directions


We say that a Newton step used in an interior-point method is a pure Newton
step if it is a step directed toward the optimal point satisfying F (x, y, s) =

[0, 0, 0] [T] . Especially at points close to the boundary of the feasible set,
pure Newton directions can be poor search directions as they may point to
the exterior of the feasible set and lead to small admissible stepsizes. To
avoid such behavior, most interior-point methods take a step toward points
on the central path C corresponding to predetermined value of τ . Since such
directions are aiming for central points, they are called centered directions.
Figure 7.3 depicts a pure and centered Newton direction from a sample
iterate.

Feasible
region



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-130-0.png)









Figure 7.3: Pure and centered Newton directions


A centered direction is obtained by applying Newton update to the following system:





 =





0
 0
0





 . (7.17)



Fˆ(x, y, s) =





A [T] y − Qx + s − c
 Ax − b
XSe − τe



Since the Jacobian of F [ˆ] is identical to the Jacobian of F, proceeding as in
equations (7.11)–(7.14), we obtain the following (modified) Newton equation
for the centered direction:





−Q A [T] I
 A 0 0
S [k] 0 X [k]











∆x [k] c
 ∆yc [k]
∆s [k] c





 =





0
 0
τe − X [k] S [k] e





 . (7.18)



We used the subscript c with the direction vectors to note that they are
centered directions. Notice the similarity between (7.14) and (7.18).
One crucial choice we need to make is the value of τ to be used in
determining the centered direction. To illustrate potential strategies for


132CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS


this choice, we first define the following measure often called the duality
gap, or the average complementarity:



(7.19)
n [.]



µ = µ(x, s) :=




n
i=1 [x][i][s][i]




[x][i][s][i]

= [x][T][ s]
n n



Note that, when (x, y, s) satisfy the conditions Ax = b, x ≥ 0 and A [T] y Qx + s = c, s ≥ 0, then (x, y, s) are optimal if and only if µ(x, s) = 0. If
µ is large, then we are far away from the solution. Therefore, µ serves as
a measure of optimality for feasible points–the smaller the duality gap, the
closer the point to optimality.
For a central point (xτ, yτ, sτ ) we have




n
i=1 [τ]

= τ.
n



µ(xτ, sτ ) =




n
i=1 [(][x][τ] [)][i][(][s][τ] [)][i]

=
n



Because of this identity, we associate the central point (xτ, yτ, sτ ) with all
feasible points (x, y, s) satisfying µ(x, s) = τ . All such points can be regarded
as being at the same “level” as the central point (xτ, yτ, sτ ). When we
choose a centered direction from a current iterate (x, y, s), we have the
possibility of choosing to target a central point that is (i) at a lower level than
our current point (τ < µ(x, s)), (ii) at the same level as our current point
(τ = µ(x, s)), or (iii) at a higher level than our current point (τ - µ(x, s)).
In most circumstances, the third option is not a good choice as it targets
a central point that is “farther” than the current iterate to the optimal
solution. Therefore, we will always choose τ ≤ µ(x, s) in defining centered
directions. Using a simple change in notation, the centered direction can
now be described as the solution of the following system:
     











∆x [k] c
 ∆yc [k]
∆s [k] c



 =







−Q A [T] I
 A 0 0
S [k] 0 X [k]













0
 0
σ [k] µ [k] e − X [k] S [k] e



, (7.20)



where µ [k] := µ(x [k], s [k] ) = [(][x][k][)][T][ s][k] and σ [k] [0, 1] is a user defined quantity

n
∈
describing the ratio of the duality gap at the target central point and the
current point.
When σ [k] = 1 (equivalently, τ = µ [k] in our earlier notation), we have
a pure centering direction. This direction does not improve the duality
gap and targets the central point whose duality gap is the same as our
current iterate. Despite the lack of progress in terms of the duality gap,
these steps are often desirable since large step sizes are permissible along
such directions and points get well-centered so that the next iteration can
make significant progress toward optimality. At the other extreme, we have
σ [k] = 0. This, as we discussed before, corresponds to the pure Newton
step, also called the affine-scaling direction. Practical implementations often
choose intermediate values for σ [k] .
We are now ready to describe a generic interior-point algorithm that uses
centered directions:


Algorithm 7.1 Generic Interior Point Algorithm


7.5. INTERIOR-POINT METHODS 133


0. Choose (x [0], y [0], s [0] ) ∈F [o] . For k = 0, 1, 2, . . . repeat the following steps.



1. Choose σ [k] [0, 1], let µ [k] = [(][x][k][)][T][ s][k]

n

∈



. Solve
n







∆x [k]
 ∆y [k]



∆y [k]

∆s [k]



−Q A [T] I
 A 0 0
S [k] 0 X [k]



















0
 0
σ [k] µ [k] e − X [k] S [k] e





 .



 =



2. Choose α [k] such that


x [k] + α [k] ∆x [k]         - 0, and s [k] + α [k] ∆s [k]         - 0.


Set


(x [k][+1], y [k][+1], s [k][+1] ) = (x [k], y [k], s [k] ) + αk(∆x [k], ∆y [k], ∆s [k] ),


and k = k + 1.


Exercise 7.7 Compute the centered Newton direction for the iterate in
Exercise 7.4 for σ [k] = 1, 0.5, and 0.1. For each σ [k], compute the largest
permissable stepsize along the computed centered direction and compare
your findings with that of Exercise 7.5.


7.5.3 Neighborhoods of the Central Path


Variants of interior-point methods differ in the way they choose the centering parameter σ [k] and the step-size parameter α [k] in each iteration. Pathfollowing methods aim to generate iterates that are approximations to central points. This is achieved by a careful selection of the centering and
step-size parameters. Before we discuss the selection of these parameters we
need to make the notion of “approximate central points” more precise.
Recall that central points are those in the set F [o] that satisfy the additional conditions that xisi = τ, i, for some positive τ . Consider a central
∀
point (xτ, yτ, sτ ). If a point (x, y, s) approximates this central point, we
would expect that the Euclidean distance between these two points is small,
i.e.,
(x, y, s) (xτ, yτ, sτ )
∥            - ∥

is small. Then, the set of approximations to (xτ, yτ, sτ ) may be defined as:


(x, y, s) : (x, y, s) (xτ, yτ, sτ ) ε, (7.21)
{ ∈F [o] ∥       - ∥≤ }

for some ε ≥ 0. Note, however, that it is difficult to obtain central points
explicitly. Instead, we have their implicit description through the system
(7.17). Therefore, a description such as (7.21) is of little practical/algorithmic
value when we do not know (xτ, yτ, sτ ). Instead, we consider descriptions
of sets that imply proximity to central points. Such descriptions are often


134CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS


called the neighborhoods of the central path. Two of the most commonly
used neighborhoods of the central path are:



2(θ) := (x, y, s) : XSe µe θµ, µ = [x][T][ s] (7.22)
N { ∈F [o] ∥   - ∥≤ n [}][,]

for some θ ∈ (0, 1) and

N−∞(γ) := {(x, y, s) ∈F [o] : xisi ≥ γµ ∀i, µ = [x] n [T][ s] [}][,] (7.23)

for some γ ∈ (0, 1). The first neighborhood is called the 2-norm neighborhood while the second one the one-sided ∞-norm neighborhood (but often
called the −∞-norm neighborhood, hence the notation). One can guarantee
that the generated iterates are “close” to the central path by making sure
that they all lie in one of these neighborhoods. If we choose θ = 0 in (7.22)
or γ = 1 in (7.23), the neighborhoods we defined degenerate to the central
path C.


Exercise 7.8 Show that 2(θ1) 2(θ2) when 0 < θ1 θ2 < 1, and that
N ⊂N ≤
N−∞(γ1) ⊂N−∞(γ2) for 0 < γ2 ≤ γ1 < 1.

Exercise 7.9 Show that N2(θ) ⊂N−∞(γ) if γ ≤ 1 − θ.


As hinted in the last exercise, for typical values of θ and γ, the 2-norm
neighborhood is often much smaller than the −∞-norm neighborhood. Indeed,



n 1

µ

 


x1s1



∥XSe − µe∥≤ θµ ⇔


which, in turn, is equivalent to



����������



1 1 1

µ
x2s2 - 1

µ

  ...
xnsn



≤ θ, (7.24)



����������



�n


i=1




- xisi �2
1 θ [2] .
µ  - ≤




[i][s][i] [x][i][s][i][−][µ]

µ µ

Therefore, [−][1 =] a



In this last expression, the quantity [x][i][s][i]



In this last expression, the quantity [i] [i] [i] [i][−] is the relative deviation

µ µ

of xisi’s from their average value µ. Therefore, [−][1 =] a point is in the 2-norm
neighborhood only if the sum of the squared relative deviations is small.
Thus, 2(θ) contains only a small fraction of the feasible points, even when
N
θ is close to 1. On the other hand, for the −∞-norm neighborhood, the only
requirement is that each xisi should not be much smaller than their average
value µ. For small (but positive) γ, (γ) may contain almost the entire
N−∞
set F [o] .
In summary, 2-norm neighborhoods are narrow while the −∞-norm
neighborhoods are relatively wide. The practical consequence of this observation is that, when we restrict our iterates to be in the 2-norm neighborhood of the central path as opposed to the −∞-norm neighborhood, we have


7.5. INTERIOR-POINT METHODS 135


much less room to maneuver and our step-sizes may be cut short. Figure 7.4
illustrates this behavior. For these reasons, algorithms using the narrow 2norm neighborhoods are often called short-step path-following methods while
the methods using the wide −∞-norm neighborhoods are called long-step
path-following methods



**Narrow Neighborhood**


**Path**



**Wide Neighborhood**


**Path**



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-134-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-134-1.png)

Figure 7.4: Narrow and wide neighborhoods of the central path


The price we pay for the additional flexibility with wide neighborhoods
come in the theoretical worst-case analysis of algorithms using such neighborhoods. When the iterates are restricted to the 2-norm neighborhood, we
have a stronger control of the iterates as they are very close to the central
path– a trajectory with many desirable theoretical features. Consequently,
we can guarantee that even in the worst case the iterates that lie in the
2-norm neighborhood will converge to an optimal solution relatively fast.
In contrast, iterates that are only restricted to a −∞-norm neighborhood
can get relatively far away from the central path and may not possess its
nice theoretical properties. As a result, iterates may “get stuck” in undesirable corners of the feasible set and the convergence may be slow in these
worst-case scenarios. Of course, the worst case scenarios rarely happen and
typically (on average) we see faster convergence with long-step methods than
with short-step methods.


Exercise 7.10 Verify that the iterate given in Exercise 7.4 is in N ( [1]

2 [).]

−∞

What is the largest γ such that this iterate lies in N (γ)?
−∞


Exercise 7.11 Recall the centered Newton directions in Exercise 7.7 as well
as the pure Newton direction in Exercise 7.5. For each direction, compute
the largest αk such that the updated iterate remains in N ( 2 [1] [).]
−∞


136CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS


7.5.4 A Long-Step Path-Following Algorithm


Next, we formally describe a long-step path following algorithm that specifies
some of the parameter choices of the generic algorithm we described above.


Algorithm 7.2 Long-Step Path-Following Algorithm


0. Given γ ∈ (0, 1), 0 < σmin < σmax < 1, choose (x [0], y [0], s [0] ) ∈N−∞(γ).
For k = 0, 1, 2, . . . repeat the following steps.



1. Choose σ [k] [σmin, σmax], let µ [k] = [(][x][k] n [)][T][ s][k]
∈





0
 0
σ [k] µ [k] e − X [k] S [k] e



. Solve
n







∆x [k]
 ∆y [k]



∆y [k]

∆s [k]





 .



−Q A [T] I
 A 0 0
S [k] 0 X [k]

















 =



2. Choose α [k] such that


(x [k], y [k], s [k] ) + αk(∆x [k], ∆y [k], ∆s [k] ) ∈N−∞(γ).


Set


(x [k][+1], y [k][+1], s [k][+1] ) = (x [k], y [k], s [k] ) + αk(∆x [k], ∆y [k], ∆s [k] ),


and k = k + 1.


7.5.5 Starting from an Infeasible Point


Both the generic interior-point method and the long-step path-following
algorithm we described above require that one starts with a strictly feasible
iterate. This requirement is not practical since finding such a starting point
is not always a trivial task. Fortunately, however, we can accommodate
infeasible starting points in these algorithms with a small modification of
the linear system we solve in each iteration.
For this purpose, we only require that the initial point (x [0], y [0], s [0] ) satisfy
the nonnegativity restrictions strictly: x [0] - 0 and s [0] - 0. Such points
can be generated trivially. We are still interested in solving the following
nonlinear system:





0
 0
0





, (7.25)



Fˆ(x, y, s) =





A [T] y − Qx + s − c
 Ax − b
XSe − τe





 =



as well as x ≥ 0, s ≥ 0. As in (5.7), the Newton step from an infeasible point
(x [k], y [k], s [k] ) is determined by solving the following system of linear equations:







J(x [k], y [k], s [k] )



∆x [k]
 ∆y [k]



∆y [k]

∆s [k]





 = −F [ˆ] (x [k], y [k], s [k] ), (7.26)


7.6. QP SOFTWARE 137



which reduces to


−Q A [T] I
 A 0 0
S [k] 0 X [k]









∆x [k]
 ∆y [k]



∆y [k]

∆s [k]











b − Ax [k]

[k]





 . (7.27)





 =



c + Qx [k]  - A [T] y [k]  - s [k]
 b Ax [k]



τe − X [k] S [k] e



We no longer have zeros in the first and second blocks of the right-handside vector since we are not assuming that the iterates satisfy Ax [k] = b and
A [T] y [k] - Qx [k] + s [k] = c. Replacing the linear system in the two algorithm
descriptions above with (7.27) we obtain versions of these algorithms that
work with infeasible iterates. In these versions of the algorithms, search for
feasibility and optimality are performed simultaneously.

#### 7.6 QP software


As for linear programs, there are several software options for solving practical quadratic programming problems. Many of the commercial software
options are very efficient and solve very large QPs within seconds or minutes. A survey of nonlinear programming software, which includes software
designed for QPs, can be found at


http://www.lionhrtpub.com/orms/surveys/nlp/nlp.html


The Network Enabled Optimization Server (NEOS) website and the Optimization Software Guide website we mentioned when we discussed NLP
software are also useful for QP solvers. LOQO is a very efficient and robust interior-point based software for QPs and other nonlinear programming
problems. It is available from


http://www.orfe.princeton.edu/ loqo


OOQP is an object-oriented C++ package, based on a primal-dual interiorpoint method, for solving convex quadratic programming problems. It contains code that can be used ”out of the box” to solve a variety of structured
QPs, including general sparse QPs, QPs arising from support vector machines, Huber regression problems, and QPs with bound constraints. It is
available for free from the following website:


http://www.cs.wisc.edu/ swright/ooqp

#### 7.7 Additional Exercises


Exercise 7.12 In the study of interior-point methods for solving quadratic
programming problems we encountered the following matrix:





,



M :=





−Q A [T] I
 A 0 0
S [k] 0 X [k]


138CHAPTER 7. QUADRATIC PROGRAMMING: THEORY AND ALGORITHMS



where (x [k], y [k], s [k] ) is the current iterate, X [k] and S [k] are diagonal matrices
with the components of the vectors x [k] and s [k] along their diagonals. Recall
that M is the Jacobian matrix of the function that defines the optimality
conditions of the QP problem. This matrix appears in linear systems we
need to solve in each interior-point iteration. We can solve these systems
only when M is nonsingular. Show that M is necessarily nonsingular when
A has full row rank and Q is positive semidefinite. Provide an example
with a Q matrix that is not positive semidefinite (but A matrix has full row
rank) such that M is singular. (Hint: To prove non-singularity of M when
Q is positive semidefinite and A has full row rank, consider a solution of the
system      







∆x
 ∆y
∆s



 =







−Q A [T] I
 A 0 0
S [k] 0 X [k]

















0
 0
0



 .



It is sufficient to show that the only solution to this system is ∆x = 0, ∆y =
0, ∆s = 0. To prove this, first eliminate ∆s variables from the system, and
then eliminate ∆x variables.)


Exercise 7.13 Consider the following quadratic programming formulation
obtained from a small portfolio selection model:












minx [x1 x2 x3 x4]





0.01 0.005 0 0
0.005 0.01 0 0
0 0 0.04 0
0 0 0 0














x1
x2
x3
x4


s1
s2
s3
s4

















=




x1 + x2 + x3 = 1

−x2 + x3 + x4 = 0.1

x1, x2, x3, x4 0.
≥

We have the following iterate for this problem:



x1
x2
x3
x4









1/3
1/3
1/3
0.1



0.004
0.003
0.0133
0.001






=






    
, y = y1
 y2






.












x =









=




0.001
−0.001



, s =



Verify that (x, y, s) ∈F [o] . Is this point on the central path? Is it on
(0.1)? How about (0.05)? Compute the pure centering (σ = 1)
N−∞ N−∞
and pure Newton (σ = 0) directions from this point. For each direction,
find the largest step-size α that can be taken along that direction without
leaving the neighborhood (0.05)? Comment on your results.
N−∞


Exercise 7.14 Implement the long-step path-following algorithm given in
Section 7.5.4 using σmin = 0.2, σmax = 0.8, γ = 0.25. Solve the quadratic
programming problem in Exercise 7.13 starting from the iterate given in that
exercise using your implementation. Experiment with alternative choices for
σmin, σmax and γ.


## Chapter 8

# QP Models: Portfolio Optimization

#### 8.1 Mean-Variance Optimization

Markowitz’ theory of mean-variance optimization (MVO) provides a mechanism for the selection of portfolios of securities (or asset classes) in a manner
that trades off the expected returns and the risk of potential portfolios. We
explore this model in more detail in this chapter.
Consider assets S1, S2, . . ., Sn (n 2) with random returns. Let µi and
≥
σi denote the expected return and the standard deviation of the return of
asset Si. For i = j, ρij denotes the correlation coefficient of the returns
of assets Si and Sj. Let µ = [µ1, . . ., µn] [T], and Σ = (σij) be the n n
×
symmetric covariance matrix with σii = σi [2] [and] [σ][ij] [=] [ρ][ij][σ][i][σ][j] [for] [i] [=] [j][.]
Denoting by xi the proportion of the total funds invested in security i, one
can represent the expected return and the variance of the resulting portfolio
x = (x1, . . ., xn) as follows:


E[x] = x1µ1 + . . . + xnµn = µ [T] x,


and

     Var[x] = ρijσiσjxixj = x [T] Σx,

i,j


where ρii 1.
≡
Since variance is always nonnegative, it follows that x [T] Σx ≥ 0 for any
x, i.e., Σ is positive semidefinite. In this section, we will assume that it
is in fact positive definite, which is essentially equivalent to assuming that
there are no redundant assets in our collection S1, S2, . . ., Sn. We further
assume that the set of admissible portfolios is a nonempty polyhedral set
and represent it as X := {x : Ax = b, Cx ≥ d}, where A is an m × n matrix,
b is an m-dimensional vector, C is a p × n matrix and d is a p-dimensional
vector. In particular, one of the constraints in the set X is

�n

xi = 1.
i=1


139


140 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION



Linear portfolio constraints such as short-sale restrictions or limits on asset/sector allocations are subsumed in our generic notation X for the polyhedral feasible set.
Recall that a feasible portfolio x is called efficient if it has the maximal
expected return among all portfolios with the same variance, or alternatively, if it has the minimum variance among all portfolios that have at
least a certain expected return. The collection of efficient portfolios form
the efficient frontier of the portfolio universe. The efficient frontier is often
represented as a curve in a two-dimensional graph where the coordinates
of a plotted point corresponds to the standard deviation and the expected
return of an efficient portfolio.
When we assume that Σ is positive definite, the variance is a strictly
convex function of the portfolio variables and there exists a unique portfolio
in X that has the minimum variance; see Exercise 7.2. Let us denote this
portfolio with xmin and its return µ [T] xmin with Rmin. Note that xmin is an
efficient portfolio. We let Rmax denote the maximum return for an admissible
portfolio.
Markowitz’ mean-variance optimization (MVO) problem can be formulated in three different but equivalent ways. We have seen one of these
formulations in the first chapter: Find the minimum variance portfolio of
the securities 1 to n that yields at least a target value of expected return
(say b). Mathematically, this formulation produces a quadratic programming problem:
minx 12 [x][T][ Σ][x]
µ [T] x R
≥ (8.1)
Ax = b
Cx ≥ d.

The first constraint indicates that the expected return is no less than the
target value R. Solving this problem for values of R ranging between Rmin
and Rmax one obtains all efficient portfolios. As we discussed above, the
objective function corresponds to one half the total variance of the portfolio.
The constant 1 [added] [for] [convenience] [in] [the] [optimality] [conditions–it]
2 [is]
obviously does not affect the optimal solution.
This is a convex quadratic programming problem for which the first order
conditions are both necessary and sufficient for optimality. We present these
conditions next. xR is an optimal solution of problem (8.1) if and only if
there exists λR IR, γE IR [m], and γI IR [p] satisfying the following
∈ ∈ ∈
conditions:
ΣxR λRµ A [T] γE C [T] γI = 0,
           -           -           µ [T] xR ≥ R, AxR = b, CxR ≥ d, (8.2)
λR 0, λR(µ [T] xR R) = 0,
≥        γI ≥ 0, γI [T] [(][Cx][R][ −] [d][) = 0][.]



(8.1)



(8.2)



The two other variations of the MVO problem are the following:



maxx µ [T] x
x [T] Σx ≤ σ [2]

Ax = b
Cx ≥ d.



(8.3)


8.1. MEAN-VARIANCE OPTIMIZATION 141


maxx µ [T] x − 2 [δ] [x][T][ Σ][x]

Ax = b (8.4)
Cx ≥ d.


In (8.3), σ [2] is a given upper limit on the variance of the portfolio. In (8.4),
the objective function is a risk-adjusted return function where the constant δ
serves as a risk-aversion constant. While (8.4) is another quadratic programming problem, (8.3) has a convex quadratic constraint and therefore is not
a QP. This problem can be solved using the general nonlinear programming
solution techniques discussed in Chapter 5. We will also discuss a reformulation of (8.3) as a second-order cone program in Chapter 10. This opens the
possibility of using specialized and efficient second-order cone programming
methods for its solution.


Exercise 8.1 What are the Karush-Kuhn-Tucker optimality conditions for
problems (8.3) and (8.4)?


Exercise 8.2 Consider the following variant of (8.4):


maxx µ [T] x η ~~√~~ x [T] Σx
               
Ax = b (8.5)
Cx ≥ d.


For each η, let x [∗] (η) denote the optimal solution of (8.5). Show that there
exists a δ - 0 such that x [∗] (η) solves (8.4) for that δ.


8.1.1 Example


We apply Markowitz’s MVO model to the problem of constructing a longonly portfolio of US stocks, bonds and cash. We will use historical return
data for these three asset classes to estimate their future expected returns.
We note that most models for MVO combine historical data with other
indicators such as earnings estimates, analyst ratings, valuation and growth
metrics, etc. Here we restrict our attention to price based estimates for
expositional simplicity. We use the S&P 500 index for the returns on stocks,
the 10-year Treasury bond index for the returns on bonds, and we assume
that the cash is invested in a money market account whose return is the
1-day federal fund rate. The annual times series for the “Total Return” are
given below for each asset between 1960 and 2003.


142 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION






|Year|Stocks Bonds MM|
|---|---|
|1960<br>1961<br>1962<br>1963<br>1964<br>1965<br>1966<br>1967<br>1968<br>1969<br>1970<br>1971<br>1972<br>1973<br>1974<br>1975<br>1976<br>1977<br>1978<br>1979<br>1980<br>1981|20.2553<br>262.935<br>100.00<br>25.6860<br>268.730<br>102.33<br>23.4297<br>284.090<br>105.33<br>28.7463<br>289.162<br>108.89<br>33.4484<br>299.894<br>113.08<br>37.5813<br>302.695<br>117.97<br>33.7839<br>318.197<br>124.34<br>41.8725<br>309.103<br>129.94<br>46.4795<br>316.051<br>137.77<br>42.5448<br>298.249<br>150.12<br>44.2212<br>354.671<br>157.48<br>50.5451<br>394.532<br>164.00<br>60.1461<br>403.942<br>172.74<br>51.3114<br>417.252<br>189.93<br>37.7306<br>433.927<br>206.13<br>51.7772<br>457.885<br>216.85<br>64.1659<br>529.141<br>226.93<br>59.5739<br>531.144<br>241.82<br>63.4884<br>524.435<br>266.07<br>75.3032<br>531.040<br>302.74<br>99.7795<br>517.860<br>359.96<br>94.8671<br>538.769<br>404.48|


|Year|Stocks Bonds MM|
|---|---|
|1982<br>1983<br>1984<br>1985<br>1986<br>1987<br>1988<br>1989<br>1990<br>1991<br>1992<br>1993<br>1994<br>1995<br>1996<br>1997<br>1998<br>1999<br>2000<br>2001<br>2002<br>2003|115.308<br>777.332<br>440.68<br>141.316<br>787.357<br>482.42<br>150.181<br>907.712<br>522.84<br>197.829<br>1200.63<br>566.08<br>234.755<br>1469.45<br>605.20<br>247.080<br>1424.91<br>646.17<br>288.116<br>1522.40<br>702.77<br>379.409<br>1804.63<br>762.16<br>367.636<br>1944.25<br>817.87<br>479.633<br>2320.64<br>854.10<br>516.178<br>2490.97<br>879.04<br>568.202<br>2816.40<br>905.06<br>575.705<br>2610.12<br>954.39<br>792.042<br>3287.27<br>1007.84<br>973.897<br>3291.58<br>1061.15<br>1298.82<br>3687.33<br>1119.51<br>1670.01<br>4220.24<br>1171.91<br>2021.40<br>3903.32<br>1234.02<br>1837.36<br>4575.33<br>1313.00<br>1618.98<br>4827.26<br>1336.89<br>1261.18<br>5558.40<br>1353.47<br>1622.94<br>5588.19<br>1366.73|



Let Iit denote the above “Total Return” for asset i = 1, 2, 3 and t =
0, . . . T, where t = 0 corresponds to 1960 and t = T to 2003. For each asset
i, we can convert the raw data Iit, t = 0, . . ., T, into rates of returns rit,
t = 1, . . ., T, using the formula


rit = [I][i,t][ −] [I][i,t][−][1] .

Ii,t−1


8.1. MEAN-VARIANCE OPTIMIZATION 143






|Year|Stocks Bonds MM|
|---|---|
|1983<br>1984<br>1985<br>1986<br>1987<br>1988<br>1989<br>1990<br>1991<br>1992<br>1993<br>1994<br>1995<br>1996<br>1997<br>1998<br>1999<br>2000<br>2001<br>2002<br>2003|22.56<br>1.29<br>9.47<br>6.27<br>15.29<br>8.38<br>31.17<br>32.27<br>8.27<br>18.67<br>22.39<br>6.91<br>5.25<br>-3.03<br>6.77<br>16.61<br>6.84<br>8.76<br>31.69<br>18.54<br>8.45<br>-3.10<br>7.74<br>7.31<br>30.46<br>19.36<br>4.43<br>7.62<br>7.34<br>2.92<br>10.08<br>13.06<br>2.96<br>1.32<br>-7.32<br>5.45<br>37.58<br>25.94<br>5.60<br>22.96<br>0.13<br>5.29<br>33.36<br>12.02<br>5.50<br>28.58<br>14.45<br>4.68<br>21.04<br>-7.51<br>5.30<br>-9.10<br>17.22<br>6.40<br>-11.89<br>5.51<br>1.82<br>-22.10<br>15.15<br>1.24<br>28.68<br>0.54<br>0.98|


|Year|Stocks Bonds MM|
|---|---|
|1961<br>1962<br>1963<br>1964<br>1965<br>1966<br>1967<br>1968<br>1969<br>1970<br>1971<br>1972<br>1973<br>1974<br>1975<br>1976<br>1977<br>1978<br>1979<br>1980<br>1981<br>1982|26.81<br>2.20<br>2.33<br>-8.78<br>5.72<br>2.93<br>22.69<br>1.79<br>3.38<br>16.36<br>3.71<br>3.85<br>12.36<br>0.93<br>4.32<br>-10.10<br>5.12<br>5.40<br>23.94<br>-2.86<br>4.51<br>11.00<br>2.25<br>6.02<br>-8.47<br>-5.63<br>8.97<br>3.94<br>18.92<br>4.90<br>14.30<br>11.24<br>4.14<br>18.99<br>2.39<br>5.33<br>-14.69<br>3.29<br>9.95<br>-26.47<br>4.00<br>8.53<br>37.23<br>5.52<br>5.20<br>23.93<br>15.56<br>4.65<br>-7.16<br>0.38<br>6.56<br>6.57<br>-1.26<br>10.03<br>18.61<br>-1.26<br>13.78<br>32.50<br>-2.48<br>18.90<br>-4.92<br>4.04<br>12.37<br>21.55<br>44.28<br>8.95|



Let Ri denote the random rate of return of asset i. From the above historical
data, we can compute the arithmetic mean rate of return for each asset:



r¯i = [1]

T



�T

rit,
t=1



which gives

|Col1|Stocks Bonds MM|
|---|---|
|Arithmetic mean ¯ri|12.06 %<br>7.85 %<br>6.32 %|



Since the rates of return are multiplicative over time, we prefer to use
the geometric mean instead of the arithmetic mean. The geometric mean is
the constant yearly rate of return that needs to be applied in years t = 0
through t = T −1 in order to get the compounded Total Return IiT, starting
from Ii0. The formula for the geometric mean is:




- [1]
T

 - 1.



µi =


We get the following results.




�T

(1 + rit)
t=1


144 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION

|Col1|Stocks Bonds MM|
|---|---|
|Geometric mean µi|10.73 %<br>7.37 %<br>6.27 %|



We also compute the covariance matrix:



cov(Ri, Rj) = [1]

T



�T

(rit r¯i)(rjt r¯j).
t=1 - 


|Covariance|Stocks Bonds MM|
|---|---|
|Stocks<br>Bonds<br>MM|0.02778<br>0.00387<br>0.00021<br>0.00387<br>0.01112<br>-0.00020<br>0.00021<br>-0.00020<br>0.00115|


It is interesting to compute the volatility of the rate of return on each

   asset σi = cov(Ri, Ri):


|Col1|Stocks Bonds MM|
|---|---|
|Volatility|16.67 %<br>10.55 %<br>3.40 %|



and the correlation matrix ρij = [cov] σ [(] i [R] σ [i] j [,R][j] [)] :

|Correlation|Stocks Bonds MM|
|---|---|
|Stocks<br>Bonds<br>MM|1<br>0.2199<br>0.0366<br>0.2199<br>1<br>-0.0545<br>0.0366<br>-0.0545<br>1|



Setting up the QP for portfolio optimization


min 0.02778x [2] S [+ 2][ ·][ 0][.][00387][x][S][x][B] [+ 2][ ·][ 0][.][00021][x][S][x][M]
+0.01112x [2] B [+ 0][.][00115][x][2] M
0 [−] .1073 [2][ ·][ 0] x [.] S [00020] + 0.0737 [x][B][x][M] xB + 0.0627xM ≥ R
xS + xB + xM = 1
xS, xB, xM 0
≥



(8.6)



and solving it for R = 6.5% to R = 10.5% with increments of 0.5% we get
the optimal portfolios shown in Table 8.1.1 and the corresponding variance.
The optimal allocations on the efficient frontier are also depicted in the
right-hand-side graph in Figure 8.1.


Based on the first two columns of Table 8.1.1, the left-hand-side graph
of Figure 8.1 plots the maximum expected rate of return R of a portfolio
as a function of its volatility (standard deviation). This curve is the efficient frontier we discussed earlier. Every possible portfolio of consisting
of long positions in stocks, bonds, and money market investments is represented by a point lying on or below the efficient frontier in the standard
deviation/expected return plane.


8.1. MEAN-VARIANCE OPTIMIZATION 145

|Rate of Return R|Variance|Stocks Bonds MM|
|---|---|---|
|0.065<br>0.070<br>0.075<br>0.080<br>0.085<br>0.090<br>0.095<br>0.100<br>0.105|0.0010<br>0.0014<br>0.0026<br>0.0044<br>0.0070<br>0.0102<br>0.0142<br>0.0189<br>0.0246|0.03<br>0.10<br>0.87<br>0.13<br>0.12<br>0.75<br>0.24<br>0.14<br>0.62<br>0.35<br>0.16<br>0.49<br>0.45<br>0.18<br>0.37<br>0.56<br>0.20<br>0.24<br>0.67<br>0.22<br>0.11<br>0.78<br>0.22<br>0<br>0.93<br>0.07<br>0|



Table 8.1: Efficient Portfolios



10.5


10


9.5


9


8.5


8


7.5


7


6.5
2 4 6 8 10 12 14 16

Standard Deviation (%)


|Col1|Stocks<br>Bonds<br>MM|
|---|---|
|||
|||



0
6.5 7 7.5 8 8.5 9 9.5 10 10.5

Expected return of efficient portfolios (%)



100


90


80


70


60


50


40


30


20


10





![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-144-0.png)

Figure 8.1: Efficient Frontier and the Composition of Efficient Portfolios


Exercise 8.3 Solve Markowitz’s MVO model for constructing a portfolio
of US stocks, bonds and cash using arithmetic means, instead of geometric
means as above. Vary R from 6.5 % to 12 % with increments of 0.5 % .
Compare with the results obtained above.


Exercise 8.4 In addition to the three securities given earlier (S&P 500
Index, 10-year Treasury Bond Index and Money Market), consider a 4th
security (the NASDAQ Composite Index) with following “Total Return”:


146 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION








|Year|NASDAQ|
|---|---|
|1990<br>1991<br>1992<br>1993<br>1994<br>1995<br>1996<br>1997<br>1998<br>1999<br>2000<br>2001<br>2002<br>2003|373.84<br>586.34<br>676.95<br>776.80<br>751.96<br>1052.1<br>1291.0<br>1570.3<br>2192.7<br>4069.3<br>2470.5<br>1950.4<br>1335.5<br>2003.4|


|Year|NASDAQ|
|---|---|
|1960<br>1961<br>1962<br>1963<br>1964<br>1965<br>1966<br>1967<br>1968<br>1969<br>1970<br>1971<br>1972<br>1973<br>1974|34.461<br>45.373<br>38.556<br>46.439<br>57.175<br>66.982<br>63.934<br>80.935<br>101.79<br>99.389<br>89.607<br>114.12<br>133.73<br>92.190<br>59.820|


|Year|NASDAQ|
|---|---|
|1975<br>1976<br>1977<br>1978<br>1979<br>1980<br>1981<br>1982<br>1983<br>1984<br>1985<br>1986<br>1987<br>1988<br>1989|77.620<br>97.880<br>105.05<br>117.98<br>151.14<br>202.34<br>195.84<br>232.41<br>278.60<br>247.35<br>324.39<br>348.81<br>330.47<br>381.38<br>454.82|



Construct a portfolio consisting of the S&P 500 index, the NASDAQ
index, the 10-year Treasury bond index and cash, using Markowitz’s MVO
model. Solve the model for different values of R.


Exercise 8.5 Repeat the previous exercise, this time assuming that one
can leverage the portfolio up to 50% by borrowing at the money market
rate. How do the risk/return profiles of optimal portfolios change with this
relaxation? How do your answers change if the borrowing rate for cash is
expected to be 1% higher than the lending rate?


8.1.2 Large-Scale Portfolio Optimization


In this section, we consider practical issues that arise when the MeanVariance model is used to construct a portfolio from a large underlying
family of assets. For concreteness, let us consider a portfolio of stocks constructed from a set of n stocks with known expected returns and covariance
matrix, where n may be in the hundreds or thousands.


Diversification
In general, there is no reason to expect that solutions to the Markowitz
model will be well diversified portfolios. In fact, this model tends to produce
portfolios with unreasonably large weights in certain asset classes and, when
short positions are allowed, unintuitively large short positions. This issue
is well documented in the literature, including the paper by Green and
Hollifield [34] and is often attributed to estimation errors. Estimates that
may be slightly “off” may lead the optimizer to chase phantom low-risk highreturn opportunities by taking large positions. Hence, portfolios chosen by
this quadratic program may be subject to idiosyncratic risk. Practitioners
often use additional constraints on the xi’s to insure themselves against
estimation and model errors and to ensure that the chosen portfolio is well
diversified. For example, a limit m may be imposed on the size of each xi,
say


8.1. MEAN-VARIANCE OPTIMIZATION 147


xi m for i = 1, . . ., n.
≤

One can also reduce sector risk by grouping together investments in
securities of a sector and setting a limit on the exposure to this sector. For
example, if mk is the maximum that can be invested in sector k, we add the
constraint


     
xi mk.
≤
i in sector k

Note however that, the more constraints one adds to a model, the more
the objective value deteriorates. So the above approach to producing diversification, at least ex ante, can be quite costly.


Transaction Costs
We can add a portfolio turnover constraint to ensure that the change
between the current holdings x [0] and the desired portfolio x is bounded by
h. This constraint is essential when solving large mean-variance models
since the covariance matrix is almost singular in most practical applications
and hence the optimal decision can change significantly with small changes
in the problem data. To avoid big changes when reoptimizing the portfolio,
turnover constraints are imposed. Let yi be the amount of asset i bought
and zi the amount sold. We write



xi x [0] i yi 0,
 - [≤] [y][i][,] ≥

x [0] i zi 0,

[−] [x][i] [≤] [z][i][,] ≥



�n



(yi + zi) ≤ h.
i=1



Instead of a turnover constraint, we can introduce transaction costs directly into the model. Suppose that there is a transaction cost ti proportional
to the amount of asset i bought, and a transaction cost t [′] i [proportional to the]
amount of asset i sold. Suppose that the portfolio is reoptimized once per
period. As above, let x [0] denote the current portfolio. Then a reoptimized
portfolio is obtained by solving



�n

σijxixj
j=1



min



�n


i=1



subject to
�n

i=1(µixi − tiyi − t [′] i [z][i][)][ ≥] [R]

�n

xi = 1
i=1

xi x [0] i for i = 1, . . ., n
       - [≤] [y][i]

x [0] i for i = 1, . . ., n

[−] [x][i] [≤] [z][i]


148 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


yi 0 for i = 1, . . ., n
≥

zi 0 for i = 1, . . ., n
≥

xi unrestricted for i = 1, . . ., n.


Parameter Estimation
The Markowitz model gives us an optimal portfolio assuming that we
have perfect information on the µi’s and σij’s for the assets that we are
considering. Therefore, an important practical issue is the estimation of the
µi’s and σij’s.
A reasonable approach for estimating these data is to use time series
of past returns (rit= return of asset i from time t 1 to time t, where

               i = 1, . . ., n, t = 1, . . ., T ). Unfortunately, it has been observed that small
changes in the time series rit lead to changes in the µi’s and σij’s that often
lead to significant changes in the “optimal” portfolio.
Markowitz recommends using the β’s of the securities to calculate the
µi’s and σij’s as follows. Let


rit = return of asset i in period t, i = 1, . . ., n, and t = 1, . . ., T,

rmt = market return in period t,

rft = return of risk-free asset in period t.


We estimate βi by a linear regression based on the capital asset pricing
model
rit rft = βi(rmt rft) + εit
           -           
where the vector εi represents the idiosyncratic risk of asset i. We assume
that cov(εi, εj) = 0. The β’s can also be purchased from financial research
groups and risk model providers.


Knowing βi, we compute µi by the relation


µi E(rf ) = βi(E(rm) E(rf ))
          -           
and σij by the relation


σij = βiβjσm [2] for i = j
̸

σii = βi [2][σ] m [2] [+][ σ] ε [2] i
where σm [2] [denotes] [the] [variance] [of] [the] [market] [return] [and] [σ] ε [2] i [the] [variance] [of]
the idiosyncratic risk.


But the fundamental weakness of the Markowitz model remains, no matter how cleverly the µi’s and σij’s are computed: The solution is extremely
sensitive to small changes in the data. Only one small change in one µi
may produce a totally different portfolio x. What can be done in practice
to overcome this problem, or at least reduce it? Michaud [51] recommends
to resample returns from historical data to generate alternative µ and σ


8.1. MEAN-VARIANCE OPTIMIZATION 149


estimates, to solve the MVO problem repeatedly with inputs generated this
way, and then to combine the optimal portfolios obtained in this manner.
Robust optimization approaches provide an alternative strategy to mitigate
the input sensitivity in MVO models; we discuss some examples in Chapters
19 and 20. Another interesting approach is considered in the next section.


Exercise 8.6 Express the following restrictions as linear constraints:
(i) The β of the portfolio should be between 0.9 and 1.1 .
(ii) Assume that the stocks are partitioned by capitalization: large,
medium and small. We want the portfolio to be divided evenly between
large and medium cap stocks, and the investment in small cap stocks to be
between two and three times the investment in large cap stocks.


Exercise 8.7 Using historical returns of the stocks in the DJIA, estimate
their mean µi and covariance matrix. Let R be the median of the µis.
(i) Solve Markowitz’s MVO model to construct a portfolio of stocks from
the DJIA that has expected return at least R.
(ii) Generate a random value uniformly in the interval [0.95µi, 1.05µi],
for each stock i. Resolve Markowitz’s MVO model with these mean returns,
instead of µis as in (i). Compare the results obtained in (i) and (ii).
(iii) Repeat three more times and average the five portfolios found in (i),
(ii) and (iii). Compare this portfolio with the one found in (i).


8.1.3 The Black-Litterman Model


Black and Litterman [13] recommend to combine the investor’s view with
the market equilibrium, as follows.
The expected return vector µ is assumed to have a probability distribution that is the product of two multivariate normal distributions. The first
distribution represents the returns at market equilibrium, with mean π and
covariance matrix τ Σ, where τ is a small constant and Σ = (σij) denotes
the covariance matrix of asset returns (Note that the factor τ should be
small since the variance τσi [2] [of] [the] [random] [variable] [µ][i] [is] [typically] [much]
smaller than the variance σi [2] [of] [the] [underlying] [asset] [returns).] [The] [second]
distribution represents the investor’s view about the µi’s. These views are
expressed as
Pµ = q + ε

where P is a k × n matrix and q is a k-dimensional vector that are provided
by the investor and ε is a normally distributed random vector with mean
0 and diagonal covariance matrix Ω(the stronger the investor’s view, the
smaller the corresponding ωi = Ωii).
The resulting distribution for µ is a multivariate normal distribution
with mean


µ¯ = [(τ Σ) [−][1] + P [T] Ω [−][1] P ] [−][1] [(τ Σ) [−][1] π + P [T] Ω [−][1] q]. (8.7)


Black and Litterman use ¯µ as the vector of expected returns in the Markowitz
model.


150 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


Example 8.1 Let us illustrate the Black-Litterman approach on the example of Section 8.1.1. The expected returns on Stocks, Bonds and Money
Market were computed to be

|Col1|Stocks Bonds MM|
|---|---|
|Market Rate of Return|10.73 %<br>7.37 %<br>6.27 %|



This is what we use for the vector π representing market equilibrium. In
practice, π is obtained from the vector of shares of global wealth invested
in different asset classes via reverse optimization. We need to choose the
value of the small constant τ . We take τ = 0.1. We have two views that we
would like to incorporate into the model. First, we hold a strong view that
the Money Market rate will be 2% next year. Second, we also hold the view
that S&P 500 will outperform 10-year Treasury Bonds by 5% but we are not
as confident about this view. These two views can be expressed as follows


µM = 0.02 strong view: ω1 = 0.00001 (8.8)



µS µB = 0.05 weaker view: ω2 = 0.001

 
    -    -    -    














Thus P =




0 0 1
1 −1 0



, q =




0.02
0.05



and Ω=




0.00001 0
0 0.001



.



Applying formula (8.7) to compute µ¯, we get



|Col1|Stocks Bonds MM|
|---|---|
|Mean Rate of Return ¯µ|11.77 %<br>7.51 %<br>2.34 %|


We solve the same QP as in (8.6) except for the modified expected return
constraint:



min 0.02778x [2] S [+ 2][ ·][ 0][.][00387][x][S][x][B] [+ 2][ ·][ 0][.][00021][x][S][x][M]
+0.01112x [2] B [+ 0][.][00115][x][2] M
0 [−] .1177 [2][ ·][ 0] x [.] S [00020] + 0.0751 [x][B][x][M] xB + 0.0234xM ≥ R
xS + xB + xM = 1
xS, xB, xM 0
≥



(8.9)



Solving for R = 4.0% to R = 11.5% with increments of 0.5% we now get
the optimal portfolios and the efficient frontier depicted in Table 8.1.3 and
Figure 8.2.


Exercise 8.8 Repeat the example above, with the same investor’s views,
but adding the 4th security of Exercise 8.4 (the NASDAQ Composite Index).


Black and Litterman give the following intuition for their approach using
the following example. Suppose we know the true structure of the asset returns: For each asset, the return is composed of an equilibrium risk premium
plus a common factor and an independent shock.


Ri = πi + γiZ + νi


8.1. MEAN-VARIANCE OPTIMIZATION 151

|Rate of Return R|Variance|Stocks Bonds MM|
|---|---|---|
|0.040<br>0.045<br>0.050<br>0.055<br>0.060<br>0.065<br>0.070<br>0.075<br>0.080<br>0.085<br>0.090<br>0.095<br>0.100<br>0.105<br>0.110<br>0.115|0.0012<br>0.0015<br>0.0020<br>0.0025<br>0.0032<br>0.0039<br>0.0048<br>0.0059<br>0.0070<br>0.0083<br>0.0096<br>0.0111<br>0.0133<br>0.0163<br>0.0202<br>0.0249|0.08<br>0.17<br>0.75<br>0.11<br>0.21<br>0.68<br>0.15<br>0.24<br>0.61<br>0.18<br>0.28<br>0.54<br>0.22<br>0.31<br>0.47<br>0.25<br>0.35<br>0.40<br>0.28<br>0.39<br>0.33<br>0.32<br>0.42<br>0.26<br>0.35<br>0.46<br>0.19<br>0.38<br>0.49<br>0.13<br>0.42<br>0.53<br>0.05<br>0.47<br>0.53<br>0<br>0.58<br>0.42<br>0<br>0.70<br>0.30<br>0<br>0.82<br>0.18<br>0<br>0.94<br>0.06<br>0|



Table 8.2: Black-Litterman Efficient Portfolios



12


11


10


9


8


7


6


5


4
2 4 6 8 10 12 14 16

Standard Deviation (%)



100


90


80


70


60


50


40


30


20


10


|Col1|Stocks<br>Bonds<br>MM|
|---|---|
|||



0
4 5 6 7 8 9 10 11

Expected return of efficient portfolios (%)





![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-150-0.png)

Figure 8.2: Efficient Frontier and the Composition of Efficient Portfolios
using the Black-Litterman approach


where


Ri = the return on the ith asset,

πi = the equilibrium risk premium on the ith asset,

Z = a common factor,

γi = the impact of Z on the ith asset,

νi = an independent shock to the ith asset.


The covariance matrix Σ of asset returns is assumed to be known. The
expected returns of the assets are given by:


µi = πi + γiE[Z] + E[νi].


152 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


While a consideration of the equilibrium motivates the Black-Litterman
model, they do not assume that E[Z] and E[νi] are equal to 0 which would
indicate that the expected excess returns are equal to the equilibrium risk
premiums. Instead, they assume that the expected excess returns µi are
unobservable random variables whose distribution is determined by the distribution of E[Z] and E[νi]’s. Their additional assumptions imply that the
covariance matrix of expected returns is τ Σ for some small positive scalar
τ . All this information is assumed to be known to all investors.
Investors differ in the additional, subjective informative they have about
future returns. They express this information as their “views” such as “I
expect that asset A will outperform asset B by 2%”. Coupled with a measure
of confidence, such views can be incorporated into the equilibrium returns
to generate conditional distribution of the expected returns. For example,
if we assume that the equilibrium distribution of µ is given by the normal
distribution N(π, τ Σ) and views are represented using the constraint Pµ = q
(with 100% confidence), the mean µ¯ of the normal distribution conditional
on this view is obtained as the optimal solution of the following quadratic
optimization problem:


min (µ π) [T] (τ Σ) [−][1] (µ π)
              -              - (8.10)
s.t. µA µB = q.
              
Using the KKT optimality conditions presented in Section 5.5, the solution
to the above minimization problem can be shown to be


µ¯ = π + (τ Σ)P [T] [P (τ Σ)P [T] ] [−][1] (q − Pπ). (8.11)


Exercise 8.9 Prove that µ¯ in (8.11) solves (8.10) using KKT conditions.


Of course, one rarely has 100% confidence in his/her views. In the more
general case, the views are expressed as Pµ = q + ε where P and q are
given by the investor as above and ε is an unobservable normally distributed
random vector with mean 0 and diagonal covariance matrix Ω. A diagonal
Ωcorresponds to the assumption that the views are independent. When
this is the case, µ¯ is given by the Black-Litterman formula


µ¯ = [(τ Σ) [−][1] + P [T] Ω [−][1] P ] [−][1] [(τ Σ) [−][1] π + P [T] Ω [−][1] q],


as stated earlier. We refer to the Black and Litterman paper for additional
details and an example of an international portfolio [13].


Exercise 8.10 Repeat Exercise 8.4, this time using the Black-Litterman
methodology outlined above. Use the expected returns you computed in
Exercise 8.4 as equilibrium returns and incorporate the view that NASDAQ
stocks will outperform the S & P 500 stocks by 4% and that the average
of NASDAQ and S & P 500 returns will exceed bond returns by 3%. Both
views are relatively strong and are expressed with ω1 = ω2 = 0.0001.


8.1. MEAN-VARIANCE OPTIMIZATION 153


8.1.4 Mean-Absolute Deviation to Estimate Risk


Konno and Yamazaki [43] propose a linear programming model instead of
the classical quadratic model. Their approach is based on the observation
that different measures of risk, such a volatility and L1-risk, are closely
related, and that alternate measures of risk are also appropriate for portfolio
optimization.
The volatility of the portfolio return is



σ =






�E[(



�n

(Ri µi)xi) [2] ]
i=1 


�n



where Ri denotes the random return of asset i, and µi denotes its mean.
The L1-risk of the portfolio return is defined as



w = E[|



�n

(Ri µi)xi ].
i=1 - |



Theorem 8.1 (Konno and Yamazaki) If (R1 ~~�~~, . . ., Rn) are multivariate

normally distributed random variables, then w = 2
π [σ][.]


Proof:
Let (µ1, . . ., µn) be the mean of (R1, . . ., Rn). Also let Σ = (σij) IR [n][×][n] be
∈

[59]the covariance matrix of (with mean [�] µixi andR1standard, . . ., Rn).deviationThen [�] Rixi is normally distributed



~~��~~
σ(x) =

i




~~�~~

σijxixj.
j



Therefore w = E[|U |] where U ∼ N (0, σ).



u 2

2σ [2] (x) du = ~~√~~ 2



2σ [2] (x) du =



1
w(x) = ~~√~~ 2πσ(x)




+∞



+∞ |u|e− 2σu [2][2] (

−∞



2πσ(x)




+∞




2
π [σ][(][x][)][.]



+∞ ue− 2σu [2][2] (

0



This theorem implies that minimizing σ is equivalent to minimizing w
when (R1, . . ., Rn) is multivariate normally distributed. With this assumption, the Markowitz model can be formulated as



min E[|



�n

(Ri µi)xi ]
i=1 - |



subject to
�n

µixi R
≥
i=1

�n

xi = 1
i=1

0 xi mi for i = 1, . . ., n.
≤ ≤


154 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


Whether (R1, . . ., Rn) has a multivariate normal distribution or not, the
above Mean-Absolute Deviation (MAD) model constructs efficient portfolios
for the L1-risk measure. Let rit be the realization of random variable Ri
during period t for t = 1, . . ., T, which we assume to be available through
the historical data or from future projection. Then



�T

rit
t=1



µi = [1]

T



µi = [1]



Furthermore


E[|



(Ri µi)xi ] = [1]
i=1 - | T



�n



�n

(rit µi)xi
i=1 - |



T



�T

|
t=1



Note that the absolute value in this expression makes it nonlinear. But
it can be linearized using additional variables. Indeed, one can replace |x|
by y + z where x = y − z and y, z ≥ 0. When the objective is to minimize
y + z, at most one of y or z will be positive. Therefore the model can be
rewritten as



min



�T

yt + zt
t=1



subject to



yt zt =
 


�n

(rit µi)xi for t = 1, . . ., T
i=1 


�n

µixi R
≥
i=1

�n

xi = 1
i=1

0 xi mi for i = 1, . . ., n
≤ ≤

yt 0, zt 0 for t = 1, . . ., T
≥ ≥

This is a linear program! Therefore this approach can be used to solve
large scale portfolio optimization problems.


Example 8.2 We illustrate the approach on our 3-asset example, using the
historical data on stocks, bonds and cash given in Section 8.1.1. Solving the
linear program for R = 6.5% to R = 10.5% with increments of 0.5 % we
get the optimal portfolios and the efficient frontier depicted in Table 8.2 and
Figure 8.3.
In the above table, we computed the variance of the MAD portfolio for
each level R of the rate of return. These variances can be compared with
the results obtained in Section 8.1.1 for the MVO portfolio. As expected,
the variance of a MAD portfolio is always at least as large as that of the
corresponding MVO portfolio. Note however that the difference is small.
This indicates that, although the normality assumption of Theorem 8.1 does
not hold, minimizing the L1-risk (instead of volatility) produces comparable
portfolios.


8.2. MAXIMIZING THE SHARPE RATIO 155

|Rate of Return R|Variance|Stocks Bonds MM|
|---|---|---|
|0.065<br>0.070<br>0.075<br>0.080<br>0.085<br>0.090<br>0.095<br>0.100<br>0.105|0.0011<br>0.0015<br>0.0026<br>0.0046<br>0.0072<br>0.0106<br>0.0144<br>0.0189<br>0.0246|0.05<br>0.01<br>0.94<br>0.15<br>0.04<br>0.81<br>0.25<br>0.11<br>0.64<br>0.32<br>0.28<br>0.40<br>0.42<br>0.32<br>0.26<br>0.52<br>0.37<br>0.11<br>0.63<br>0.37<br>0<br>0.78<br>0.22<br>0<br>0.93<br>0.07<br>0|



Table 8.3: Konno-Yamazaki Efficient Portfolios



10.5


10


9.5


9


8.5


8


7.5


7


6.5
2 4 6 8 10 12 14 16

Standard Deviation (%)



100


90


80


70


60


50


40


30


20


10


|Col1|Stocks<br>Bonds<br>MM|
|---|---|
|||



0
6.5 7 7.5 8 8.5 9 9.5 10 10.5

Expected return of efficient portfolios (%)





![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-154-0.png)

Figure 8.3: Efficient Frontier and the Composition of Efficient Portfolios
using the Konno-Yamazaki approach


Exercise 8.11 Add the 4th security of Exercise 8.4 (the NASDAQ Composite Index) to the 3-asset example. Solve the resulting MAD model for
varying values of R. Compare with the portfolios obtained in Exercise 8.4.

#### 8.2 Maximizing the Sharpe Ratio


Consider the setting in Section 8.1. Recall that we denote with Rmin and
Rmax the minimum and maximum expected returns for efficient portfolios.
Let us define the function

σ(R) : [Rmin, Rmax] → IR, σ(R) := (x [T] R [Σ][x][R][)][1][/][2][,]

where xR denotes the unique solution of problem (8.1). Since we assumed
that Σ is positive definite, it is easy to show that the function σ(R) is strictly
convex in its domain. The efficient frontier is the graph


E = (R, σ(R)) : R [Rmin, Rmax] .
{ ∈ }

We now consider a riskless asset whose return is rf 0 with probability
≥
1. We will assume that rf < Rmin, which is natural since the portfolio xmin
has a positive risk associated with it while the riskless asset does not.


156 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


Return/risk profiles of different combinations of a risky portfolio with
the riskless asset can be represented as a straight line—a capital allocation
line (CAL)—on the standard deviation vs. mean graph; see Figure 8.4. The
optimal CAL is the CAL that lies below all the other CALs for R > rf since
the corresponding portfolios will have the lowest standard deviation for any
given value of R > rf . Then, it follows that this optimal CAL goes through
a point on the efficient frontier and never goes above a point on the efficient
frontier. In other words, the slope of the optimal CAL is a sub-derivative
of the function σ(R) that defines the efficient frontier. The point where the
optimal CAL touches the efficient frontier corresponds to the optimal risky
portfolio.


rf


Figure 8.4: Capital Allocation Line



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-155-0.png)

Alternatively, one can think of the optimal CAL as the CAL with the
smallest slope. Mathematically, this can be expressed as the portfolio x that
maximizes the quantity



h(x) = [µ][T] [x][ −] [r][f]



(x [T] Σx) [1][/][2] [,]



among all x ∈ S. This quantity is precisely the reward-to-volatility ratio
introduced by Sharpe to measure the performance of mutual funds [68]. This
quantity is now more commonly known as the Sharpe ratio. The portfolio
that maximizes the Sharpe ratio is found by solving the following problem:



maxx µ [T] x−rf
(x [T] Σx) [1][/][2]
Ax = b
Cx ≥ d.



(8.12)



In this form, this problem is not easy to solve. Although it has a nice polyhedral feasible region, its objective function is somewhat complicated, and
worse, it is possibly non-concave. Therefore, (8.12) is not a convex optimization problem. The standard strategy to find the portfolio maximizing
the Sharpe ratio, often called the optimal risky portfolio, is the following:
First, one traces out the efficient frontier on a two dimensional return vs.
standard deviation graph. Then, the point on this graph corresponding to
the optimal risky portfolio is found as the tangency point of the line going through the point representing the riskless asset and is tangent to the


8.2. MAXIMIZING THE SHARPE RATIO 157


efficient frontier. Once this point is identified, one can recover the composition of this portfolio from the information generated and recorded while
constructing the efficient frontier.
Here, we describe a direct method to obtain the optimal risky portfolio by
constructing a convex quadratic programming problem equivalent to (8.12).
We need two assumptions: First, we assume that [�][n] i=1 [x][i] [= 1 for any feasible]
portfolio x. This is a natural assumption since the xis are the proportions
of the portfolio in different asset classes. Second, we assume that there
exists a feasible portfolio xˆ with µ [T] xˆ - rf –if all feasible portfolios have
expected return bounded by the risk-free rate, there is no need to optimize,
the risk-free investment dominates all others.


Proposition 8.1 Given a set X of feasible portfolios with the properties
that e [T] x = 1, x and xˆ, µ [T] x > rˆ f, the portfolio x [∗] with the max∀ ∈X ∃ ∈X
imum Sharpe ratio in this set can be found by solving the following problem


min y [T] Σy s.t. (y, κ) [+], (µ rf e) [T] y = 1, (8.13)
∈X             

where




[+] := x IR [n], κ IR κ > 0, [x]
X { ∈ ∈ | κ



If (y, κ) solves (8.13), then x [∗] = [y]

κ [.]



(8.14)
κ

[∈X} ∪] [(0][,][ 0)][.]



Problem (8.13) is a quadratic program and can be solved using the methods
discussed in Chapter 7. Proof:
By our second assumption, it suffices to consider only those x for which
(µ rf e) [T] x > 0. Let us make the following change of variables in (8.12):
 
1
κ =
(µ rf e) [T] x
                 y = κx.



Then, ~~√~~



Then, ~~√~~ x ~~�~~ [T] Σx = κ [1] ~~�~~ y [T] Σy and the objective function of (8.12) can be writ
ten as 1/ y [T] Σy in terms of the new variables. Note also that



x [T] Σx = [1]



(µ rf e) [T] x > 0, x κ > 0, [y]
 - ∈X ⇔ κ [∈X] [,]



and
1
κ = [= 1]
(µ rf e) [T] x
            - [⇔] [(][µ][ −] [r][f] [e][)][T][ y]

given y/κ = x. Thus, (8.12) is equivalent to


min y [T] Σy s.t. κ > 0, (y, κ), (µ rf e) [T] y = 1.
∈X              
Since (µ rf e) [T] y = 1 rules out (0,0) as a solution, replacing κ > 0, (y, κ)
    - ∈

set a closed set.


158 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


Exercise 8.12 Show that X [+] is a cone. If X = {x|Ax ≥ b, Cx = d},
show that X [+] = {(x, κ)|Ax - bκ ≥ 0, Cx - dκ = 0, κ ≥ 0}. What if
X = {x : ∥x∥≤ 1}?


Exercise 8.13 Find the Sharpe ratio maximizing portfolio of the four assets
in Exercise 8.4 assuming that the risk-free return rate is 3% by solving the
QP (8.13) resulting from its reformulation. Verify that the CAL passing
through the point representing the standard deviation and the expected
return of this portfolio is tangent to the efficient frontier.

#### 8.3 Returns-Based Style Analysis


In two very influential articles, Sharpe described how constrained optimization techniques can be used to determine the effective asset mix of a fund
using only the return time series for the fund and contemporaneous time
series for returns of a number of carefully chosen asset classes [66, 67]. Often, passive indices or index funds are used to represent the chosen asset
classes and one tries to determine a portfolio of these funds and indices
whose returns provide the best match for the returns of the fund being analyzed. The allocations in the portfolio can be interpreted as the fund’s style
and consequently, this approach has become to known as returns-based style
analysis, or RBSA.
RBSA provides an inexpensive and timely alternative to fundamental
analysis of a fund to determine its style/asset mix. Fundamental analysis
uses the information on actual holdings of a fund to determine its asset
mix. When all the holdings are known, the asset mix of the fund can be
inferred easily. However, this information is rarely available, and when it is
available, it is often quite expensive and several weeks or months old. Since
RBSA relies only on returns data which is immediately available for publicly
traded funds, and well-known optimization techniques, it can be employed
in circumstances where fundamental analysis cannot be used.
The mathematical model for RBSA is surprisingly simple. It uses the
following generic linear factor model: Let Rt denote the return of a security–
usually a mutual fund, but can be an index, etc.–in period t for t = 1, . . ., T
where T corresponds to the number of periods in the modeling window.
Further, let Fit denote the return on factor i in period t, for i = 1, . . ., n,
t = 1, . . ., T . Then, Rt can be represented as follows:


Rt = w1tF1t + w2tF2t + . . . + wntFnt + εt (8.15)

= Ftwt + εt, t = 1, . . ., T.


In this equation, wit quantities represent the sensitivities of Rt to each one of
the n�factors, and εt�representsT the� non-factor return.� We use the notation

wt = w1t, . . ., wnt and Ft = F1t, . . ., Fnt .
The linear factor model (8.15) has the following convenient interpretation
when the factor returns Fit correspond to the returns of passive investments,
such as those in an index fund for an asset class: One can form a benchmark


8.3. RETURNS-BASED STYLE ANALYSIS 159


portfolio of the passive investments (with weights wit), and the difference
between the fund return Rt and the return of the benchmark portfolio Ftwt is
the non-factor return contributed by the fund manager using stock selection,
market timing, etc. In other words, εt represents the additional return
resulting from active management of the fund. Of course, this additional
return can be negative.


The benchmark portfolio return interpretation for the quantity Ftwt suggests that one should choose the sensitivities (or weights) wit such that they
are all nonnegative and sum to one. With these constraints in mind, Sharpe
proposes to choose wit to minimize the variance of the non-factor return
εt. In his model, Sharpe restricts the weights to be constant over the period in consideration� so�Tthat wit does not depend on t. In this case, we

use w = w1, . . ., wn to denote the time-invariant factor weights and
formulate the following quadratic programming problem:


minw IR [n] var(εt) = var(Rt Ftw)
∈         - −n
s.t. i=1 [w][i] = 1 (8.16)
wi 0, i.
≥ ∀


The objective of minimizing the variance of the non-factor return εt
deserves some comment. Since we are essentially formulating a tracking
problem, and since εt represents the “tracking error”, one may wonder why
we do not minimize the magnitude of this quantity rather than its variance.
Since the Sharpe model interprets the quantity εt as a consistent management effect, the objective is to determine a benchmark portfolio such that
the difference between fund returns and the benchmark returns is as close
to constant (i.e., variance 0) as possible. So, we want the fund return and
benchmark return graphs to show two almost parallel lines with the distance
between these lines corresponding to manager’s consistent contribution to
the fund return. This objective is almost equivalent to choosing weights in
order to maximize the R-square of this regression model. The equivalence
is not exact since we are using constrained regression and this may lead to
correlation between εt and asset class returns.


The objective function of this QP can be easily computed:



�2


 


1
var(Rt w [T] Ft) =
   - T



�T



(Rt w [T] Ft) [2]
t=1 - 


��
T
t=1 [(][R][t][ −] [w][T][ F][t][)]

T



�2



1
=
T

 - [∥][R][ −] [Fw][∥][2][ −]




e [T] (R − Fw)







T [2]



T



w




R [T] F




[T] F

T - [e] T [T][ R][2]



=




∥R∥ [2]



∥ [2]

T - [(][e][T] T [ R][2] [)][2]




    T [1][2] [F][ T][ ee][T][ F] w.



T [2] [e][T][ F]




  1
+w [T]
T [F][ T][ F] [−] T [1]




- 2


160 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


Above, we introduced and used the notation



F11 . . . Fn1
... ... ...
F1T FnT

      - · ·





 =









R1
...
RT





F1


   - · ·
FT











, and F =



R =









and e denotes a vector of ones of appropriate size. Convexity of this quadratic
function of w can be easily verified. Indeed,



I
 - [ee] T [T]







1
T [F][ T][ F] [−] T [1]




  
[1]

T [F][ T]




[=] [1]
T [1][2] [F][ T][ ee][T][ F] T



F, (8.17)



and the symmetric matrix M = I T in the middle of the right-hand-side
               - [ee][T]

expression above is a positive semidefinite matrix with only two eigenvalues:
0 (multiplicity 1) and 1 (multiplicity T −1). Since M is positive semidefinite,
so is F [T] MF and therefore the variance of εt is a convex quadratic function
of w. Therefore, the problem (8.16) is convex quadratic programming problem and is easily solvable using well-known optimization techniques such as
interior-point methods we discussed in Chapter 7.


Exercise 8.14 Implement the returns-based style analysis approach to determine the effective asset mix of your favorite mutual fund. Use the following asset classes as your “factors”: Large growth stocks, large value stocks,
small growth stocks, small value stocks, international stocks, and fixed income investments. You should obtain time series of returns representing
these asset classes from on-line resources. You should also obtain a corresponding time series of returns for the mutual fund you picked for this
exercise. Solve the problem using 30 periods of data (i.e., T = 30).

#### 8.4 Recovering Risk-Neural Probabilities from Op- tions Prices


Recall our discussion on risk-neutral probability measures in Section 4.1.2.
There, we considered a one-period economy with n securities. Current prices
of these securities are denoted by S0 [i] [for] [i] [=] [1][, . . ., n][.] [At] [the] [end] [of] [the]
current period, the economy will be in one of the states from the state space
Ω. If the economy reaches state ω ∈ Ωat the end of the current period,
security i will have the payoff S1 [i] [(][ω][).] We assume that we know all S0 [i] [’s]
and S1 [i] [(][ω][)’s] [but] [do] [not] [know] [the] [particular] [terminal] [state] [ω][,] [which] [will] [be]
determined randomly.
Let r denote the one-period (riskless) interest rate and let R = 1 + r.
A risk neutral probability measure (RNPM) is defined as the probability
measure under which the present value of the expected value of future payoffs
of a security equals its current price. More specifically,


(discrete case:) on the state space Ω= ω1, ω2, . . ., ωm, an RNPM

  - { }
is a vector of positive numbers p1, p2, . . ., pm such that


8.4. RECOVERING RISK-NEURAL PROBABILITIES FROM OPTIONS PRICES161



1. [�][m] j=1 [p][j] [= 1,]




 R [1] mj=1 [p][j][S] 1 [i] [(][ω][j][)][,]

[∀][i.]



2. S0 [i] [=] R [1]




- (continuous case:) on the state space Ω= (a, b) an RNPM is a
density function p : Ω IR+ such that
→




  1. ab [p][(][ω][)][dω] [= 1,]




 R [1] ab [p][(][ω][)][S] 1 [i] [(][ω][)][dω,] [∀][i.]



2. S0 [i] [=] R [1]



Also recall the following result from Section 4.1.2 that is often called the
First Fundamental Theorem of Asset Pricing:


Theorem 8.2 A risk-neutral probability measure exists if and only if there
are no arbitrage opportunities.


If we can identify a risk-neutral probability measure associated with a
given state space and a set of observed prices we can price any security
for which we can determine the payoffs for each state in the state space.
Therefore, a fundamental problem in asset pricing is the identification of a
RNPM consistent with a given set of prices. Of course, if the number of
states in the state space is much larger than the number of observed prices,
this problem becomes under-determined and we cannot obtain a sensible
solution without introducing some additional structure into the RNPM we
seek. In this section, we outline a strategy that guarantees the smoothness
of the RNPM by constructing it through cubic splines. We first describe
spline functions briefly:
Consider a function f : [a, b] → IR to be estimated using its values
fi = f (xi) given on a set of points xi, i = 1, . . ., m + 1. It is assumed that
{ }
x1 = a and xm+1 = b.
A spline function, or spline, is a piecewise polynomial approximation
S(x) to the function f such that the approximation agrees with f on each
node xi, i.e., S(xi) = f (xi), i.
∀
The graph of a spline function S contains the data points (xi, fi) (called
knots) and is continuous on [a, b].
A spline on [a, b] is of order n if (i) its first n   - 1 derivatives exist on each
interior knot, (ii) the highest degree for the polynomials defining the spline
function is n.
A cubic (third order) spline uses cubic polynomials of the form fi(x) =
αix [3] + βix [2] + γix + δi to estimate the function in each interval [xi, xi+1] for
i = 1, . . ., m. A cubic spline can be constructed in such a way that it has
second derivatives at each node. For m + 1 knots (x1 = a, . . . xm+1 = b) in

[a, b] there are m intervals and, therefore 4m unknown constants to evaluate.
To determine these 4m constants we use the following 4m equations:


fi(xi) = f (xi), i = 1, . . ., m, and fm(xm+1) = f (xm+1), (8.18)

fi−1(xi) = fi(xi), i = 2, . . ., m, (8.19)

fi [′] −1 [(][x][i][) =][ f][ ′] i [(][x][i][)][,] [i][ = 2][, . . ., m,] (8.20)

fi [′′] −1 [(][x][i][) =][ f][ ′′] i [(][x][i][)][,] [i][ = 2][, . . ., m,] (8.21)

f1 [′′][(][x][1][) = 0 and][ f][ ′′] m [(][x][m][+1][) = 0][.] (8.22)


162 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


The last condition leads to a so-called natural spline.
We now formulate a quadratic programming problem with the objective
of finding a risk-neutral probability density function (described by cubic
splines) for future values of an underlying security that best fits the observed
option prices on this security.
We choose a security for consideration, say a stock or an index. We
then fix an exercise date–this is future the date for which we will obtain a
probability density function of the price of our security. Finally, we fix a
range [a, b] for possible terminal values of the price of the underlying security
at the exercise date of the options and an interest rate r for the period
between now and the exercise date. The inputs to our optimization problem
are current market prices CK of call options and PK for put options on the
chosen underlying security with strike price K and the chosen expiration
date. This data is easily available from newspapers and online sources. Let
C and P, respectively, denote the set of strike prices K for which reliable
market prices CK and PK are available. For example, may denote the
C
strike prices of call options that were traded on the day the problem is
formulated.
Next, we fix a super-structure for the spline approximation to the riskneutral density, meaning that we choose how many knots to use, where to
place the knots and what kind of polynomial (quadratic, cubic, etc.) functions to use. For example, we may decide to use cubic splines and m + 1
equally spaced knots. The parameters of the polynomial functions that comprise the spline function will be the variables of the optimization problem
we are formulating. For cubic splines with m + 1 knots, we will have 4m
variables (αi, βi, γi, δi) for i = 1, . . ., m. Collectively, we will represent these
variables with y. For all y chosen so that the corresponding polynomial
functions fi satisfy the equations (8.19)–(8.22) above, we will have a particular choice of a natural spline function defined on the interval [a, b] [1] . Let
py( ) denote this function. Imposing the following additional restrictions we

   make sure that py is a probability density function:


py(x) 0, x [a, b] (8.23)

          - ≥ ∀ ∈
b

py(ω)dω = 1. (8.24)
a


The constraint (8.24) is a linear constraint on the variables (αi, βi, γi, δi) of
the problem and can be enforced as follows:



�ns


s=1




xs+1

fs(ω)dω = 1. (8.25)
xs



On the other hand, enforcing condition (8.23) is not straightforward as
it requires the function to be nonnegative for all values of x in [a, b]. Here,


1Note that we do not impose the conditions (8.18), because the values of the probability
density function we are approximating are unknown and will be determined as a solution
of an optimization problem.


8.4. RECOVERING RISK-NEURAL PROBABILITIES FROM OPTIONS PRICES163


we relax condition (8.23), and require the cubic spline approximation to be
nonnegative only at the knots:


py(xi) 0, i = 1, . . ., m. (8.26)
≥


While this relaxation simplifies the problem greatly, we cannot guarantee
that the spline approximation we generate will be nonnegative in its domain. We will discuss in Chapter 10.3 a more sophisticated technique that
rigorously enforces condition (8.23).
Next, we define the discounted expected value of the terminal value of
each option using py as the risk-neutral density function:



1
CK(y) :=
1 + r

1
PK(y) :=
1 + r




b



(ω K) [+] py(ω)dω, (8.27)
a 
b

(K ω) [+] py(ω)dω. (8.28)
a 



b



Then, CK(y) is the theoretical option price if py is the true risk-neutral
probability measure and
(CK CK(y)) [2]

          
is the squared difference between the actual option price and this theoretical
value. Now consider the aggregated error function for a given y:




- 
(CK CK(y)) [2] +

   K∈C K∈P




  E(y) :=



(PK PK(y)) [2]

   K∈P



The objective now is to choose y such that conditions (8.19)–(8.22) of
spline function description as well as (8.26) and (8.24) are satisfied and E(y)
is minimized. This is essentially a constrained least squares problem.
We choose the number of knots and their locations so that the knots
form a superset of . Let x0 = a, x1, . . ., xm = b denote the locations
C ∪P
of the knots. Now, consider a call option with strike K and assume that
K coincides with the location of the jth knot, i.e., xj = K. Recall that y
denotes collection of variables (αi, βi, γi, δi) for i = 1, . . ., m. Now, we can
derive a formula for CK(y):




         b
(1 + r)CK(y) =



Sy(ω)(ω K) [+] dω
a 



xi



=


=


=



�m


i=1



�m


i=j+1

�m


i=j+1



Sy(ω)(ω K) [+] dω
xi−1 



xi


xi−1




- αiω [3] + βiω [2] + γiω + δi (ω K)dω.
            



xi

Sy(ω)(ω K)dω
xi−1 


It is easily seen that this expression for CK(y) is a linear function of the
components (αi, βi, γi, δi) of the y variable. A similar formula can be derived


164 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


for PK(y). The reason for choosing the knots at the strike prices is the third
equation in the sequence above—we can immediately ignore some of the
terms in the summation and the (·) [+] function is linear (and not piecewise
linear) in each integral.
Now, it is clear that the problem of minimizing E(y) subject to spline
function conditions, (8.26) and (8.24) is a quadratic optimization problem
and can be solved using the techniques of the previous chapter.

#### 8.5 Additional Exercises


Exercise 8.15 Recall the mean-variance optimization problem we considered in Section 8.1:



minx x [T] Σx
µ [T] x ≥ R
Ax = b
Cx ≥ d.



(8.29)



Now, consider the problem of finding the feasible portfolio with smallest
overall variance, without imposing any expected return constraint:


minx x [T] Σx
Ax = b (8.30)
Cx ≥ d.


(i) Does the optimal solution to (8.30) give an efficient portfolio? Why?


(ii) Let xR, λR IR, γE IR [m], and γI IR [p] satisfy the optimality
∈ ∈ ∈
conditions of (8.29) (see system (8.2)). If λR = 0, show that xR is an
optimal solution to (8.30). (Hint: What are the optimality conditions
for (8.30)? How are they related to (8.2)?)


Exercise 8.16 Classification problems are among the important classes of
problems in financial mathematics that can be solved using optimization
models and techniques. In a classification problem we have a vector of
“features” describing an entity and the objective is to analyze the features
to determine which one of the two (or more) “classes” each entity belongs
to. For example, the classes might be “growth stocks” and “value stocks”,
and the entities (stocks) may be described by a feature vector that may
contain elements such as stock price, price-earnings ratio, growth rate for
the previous periods, growth estimates, etc.
Mathematical approaches to classification often start with a “training”
exercise. One is supplied with a list of entities, their feature vectors and
the classes they belong to. From this information, one tries to extract a
mathematical structure for the entity classes so that additional entities can
be classified using this mathematical structure and their feature vectors. For
two-class classification, a hyperplane is probably the simplest mathematical
structure that can be used to “separate” the feature vectors of these two


8.5. ADDITIONAL EXERCISES 165


different classes. Of course, a hyperplane is often not sufficient to separate
two sets of vectors, but there are certain situations it may be sufficient.
Consider feature vectors ai IR [n] for i = 1, . . ., k1 corresponding to class
∈
1, and vectors bi IR [n] for i = 1, . . ., k2 corresponding to class 2. If these
∈
two vector sets can be linearly separated, there exists a hyperplane w [T] x = γ
with w ∈ IR [n], γ ∈ IR such that

w [T] ai γ, for i = 1, . . ., k1
≥
w [T] bi γ, for i = 1, . . ., k2.
≤

To have a “strict” separation, we often prefer to obtain w and γ such that


w [T] ai γ + 1, for i = 1, . . ., k1
≥
w [T] bi γ 1, for i = 1, . . ., k2.
≤         
In this manner, we find two parallel lines (w [T] x = γ +1 line and w [T] x = γ −1)
that form the boundary of the class 1 and class 2 portion of the vector space.
This type of separation is shown in Figure 8.5.



3.5


3


2.5


2


1.5


1


0.5


0


−0.5



Strict separation



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-164-0.png)







−1
−0.5 0 0.5 1 1.5 2 2.5 3 3.5 4


Figure 8.5: Linear separation of two classes of data points


There may be several such parallel lines that separate the two classes.
Which one should one choose? A good criterion is to choose the lines that
have the largest margin (distance between the lines).


a) Consider the following quadratic problem:


minw,γ w 2
∥ ∥ [2]
a [T] i [w] ≥ γ + 1, for i = 1, . . ., k1 (8.31)
b [T] i [w] ≤ γ − 1, for i = 1, . . ., k2.

Show that the objective function of this problem is equivalent to maximizing the margin between the lines w [T] x = γ + 1 and w [T] x = γ − 1.


166 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


b) The linear separation idea we presented above can be used even when
the two vector sets ai and bi are not linearly separable. (Note
{ } { }
that linearly inseparable sets will result in an infeasible problem in
formulation (8.31).) This is achieved by introducing a nonnegative
“violation” variable for each constraint of (8.31). Then, one has two
objectives: to minimize the total of the violations of the constraints of
(1) and to maximize the margin. Develop a quadratic programming
model that combines these two objectives using an adjustable parameter that can be chosen in a way to put more weight on violations or
margin, depending on one’s preference.


Exercise 8.17 The classification problems we discussed in the previous exercise can also be formulated as linear programming problems, if one agrees
to use 1-norm rather than 2-norm of w in the objective function. Recall that
∥w∥1 = [�] i [|][w][i][|][.] [Show] [that] [if] [we] [replace] [∥][w][∥] 2 [2] [with] [∥][w][∥][1] [in] [the] [objective]
function of (1), we can write the resulting problem as an LP. Show also
that, this new objective function is equivalent to maximizing the distance
between w [T] x = γ + 1 and w [T] x = γ − 1 if one measures the distance using
∞-norm (∥g∥∞ = maxi |gi|).

#### 8.6 Case Study


Investigate the performance of one of the variations on the classical Markowitz
model proposed by Michaud, or Black-Litterman or Konno-Yamazaki.
Possible suggestions:

  - Choose 30 stocks and retrieve their historical returns over a meaningful
horizon.


  - Use the historical information to compute expected returns and the
variance-covariance matrix for these stock returns.


  - Set up the model and solve it with MATLAB or Excel’s Solver for
different levels R of expected return. Allow for short sales and include
no diversification constraints.


  - Recompute these portfolios with no short sales and various diversification constraints.


  - Compare portfolios constructed in period t (based on historical data
up to period t) by observing their performance in period t + 1, using
the actual returns from period t + 1.


  - Investigate how sensitive the optimal portfolios that you obtained are
to small changes in the data. For example, how sensitive are they to
a small change in the expected return of the assets?

  - You currently own the following portfolio: x [0] i [=] [0][.][20] [for] [i] [=] [1][, . . .,][ 5]
and x [0] i [=] [0] [for] [i] [=] [6][, . . .,][ 30.] [Include] [turnover] [constraints] [to] [reopti-]
mize the portfolio for a fixed level R of expected return and observe
the dependency on h, the total turnover allowed for reoptimization.


8.6. CASE STUDY 167


  - You currently own the following portfolio: x [0] i [=] [0][.][20] [for] [i] [=] [1][, . . .,][ 5]
and x [0] i [=] [0] [for] [i] [=] [6][, . . .,][ 30.] [Reoptimize] [the] [portfolio] [considering]
transaction costs for buying and selling. Solve for a fixed level R of
expected return and observe the dependency on transaction costs.


168 CHAPTER 8. QP MODELS: PORTFOLIO OPTIMIZATION


## Chapter 9

# Conic Optimization Tools

#### 9.1 Introduction

In this chapter and the next, we address conic optimization problems and
their applications in finance. Conic optimization refers to the problem of
minimizing or maximizing a linear function over a set defined by linear
equalities and cone membership constraints. Cones are defined and discussed
in Appendix B. While they are not as well known or as widely used as
their close relatives linear and quadratic programming, conic optimization
problems continue to grow in importance thanks to their wide applicability
and the availability of powerful methods for their solution.
We recall the definition of a standard form conic optimization problem
that was provided in the Chapter 1:


( ) minx c [T] x
CO
Ax = b (9.1)
x ∈ C.


Here, C denotes a closed convex cone in a finite-dimensional vector space
X.
When X = IR [n] and C = IR [n] + [,] [this] [problem] [is] [the] [standard] [form] [lin-]
ear programming problem. Therefore, conic optimization is a generalization of linear optimization. In fact, it is much more general than linear
programming since we can use non-polyhedral (i.e., nonlinear) cones C in
the description of these problems and formulate certain classes of nonlinear
convex objective functions and nonlinear convex constraints. In particular,
conic optimization provides a powerful and unifying framework for problems
in linear programming (LP), second-order cone programming (SOCP), and
semidefinite programming (SDP). We describe these two new and important
classes of conic optimization problems in more detail:

#### 9.2 Second-order cone programming:


SOCPs involve the second-order cone which is defined by the property that
for each of its members the first element is at least as large as the Euclidean


169


170 CHAPTER 9. CONIC OPTIMIZATION TOOLS


norm of the remaining elements. This corresponds to the case where C is
the second-order cone (also known as the quadratic cone, Lorenz cone, and
the ice-cream cone):


Cq := x = (x1, x2, . . ., xn) IR [n] : x1 (x2, . . ., xn) . (9.2)
{ ∈ ≥∥ ∥}


A portion of the second-order cone in 3 dimensions for x1 [0, 1] is
∈
depicted in Figure 9.1. As seen from the figure, the second-order cone in
three dimensions resembles an ice-cream cone that stretches to infinity. We
observe that by “slicing” the second-order cone, i.e., by intersecting it with
a hyperplane at different angles we can obtain spherical and ellipsoidal sets.
Any convex quadratic constraint can be expressed using the second-order
cone (or its rotations) and one or more hyperplanes.


{(x1, x2, x3): x1 ≥ ||(x2, x3)||}


1


0.8


0.6


0.4


0.2


0
1



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-169-0.png)



1











−1





x3



x2





Figure 9.1: The second-order cone


Exercise 9.1 Another important cone that appears in conic optimization
formulations is the rotated quadratic cone defined as follows:



Cq [r] [:=][ {][(][x][1][, x][2][, x][3][, . . ., x][n][) : 2][x][1][x][2]

[≥]



�n

x [2] j [, x][1][, x][2] (9.3)
j=3 [≥] [0][.][}][.]



Show thatCq where xy1 = (= x ~~√~~ 112, x [(][x] 2 [1], x [+] 3 [ x], . . ., x [2][),] [y][2] n) [=] ∈ ~~√~~ C12q [r][(][x][if and only if][1] [and][ y] [y][= (][j] [=][y][1][, y][x][j][2][, j][, y][=][3][, . . ., y][3][, . . ., n.][n][)][ ∈]

[x][2][),]



2 [(][x][1] [+][ x][2][),] [y][2] [=] ~~√~~ 1



Cq where y1 = ~~√~~ 2 [(][x][1] [+][ x][2][),] [y][2] [=] ~~√~~ 2 [(][x][1] [and] [y][j] [=] [x][j][, j] [=] [3][, . . ., n.]

[−] [x][2][),]
The vector y given here is obtained by rotating the vector x by 45 degrees
in the plane defined by the first two coordinate axes. In other words, each
element of the cone Cq [r] [can] [be] [mapped] [to] [a] [corresponding] [element] [of] [C][q]
through a 45 degree rotation (Why?). This is why the cone Cq [r] [is] [called] [the]
rotated quadratic cone.


9.2. SECOND-ORDER CONE PROGRAMMING: 171


Exercise 9.2 Show that the problem


3
min x 2
s.t. x ≥ 0, x ∈ S

is equivalent to the following problem:


min t
s.t. x ≥ 0, x ∈ S
x [2] ≤ t · u
u [2] ≤ x.

Express the second problem as an SOCP using Cq [r][.]


Exercise 9.3 Consider the following optimization problem:



3 3

min c1x1 + c2x2 + d1x12 [+][ d][2][x] 22

s.t. a11x1 + a12x2 = b1,
x1, x2 0,
≥



min c1x1 + c2x2 + d1x



3
2
1 [+][ d][2][x]



where d1, d2 - 0. The nonlinear objective function of this problem is a
convex function. Write this problem as a conic optimization problem with
a linear objective function and convex cone constraints.
HINT: Use the previous exercise.


A recent review of second-order cone programming models and methods is provided in [26]. One of the most common uses of second-order
cone programs in financial applications is in the modeling and treatment of
parameter uncertainties in optimization problems. After generating an appropriate description of the uncertainties, robust optimization models seek
to find solutions to such problems that will perform well under many scenarios. As we will see in Chapter 19, ellipsoidal sets are among the most
popular structures used for describing uncertainty in such problems and the
close relationship between ellipsoidal sets and second-order cones make them
particularly useful. We illustrate this approach in the following subsection.


9.2.1 Ellipsoidal Uncertainty for Linear Constraints


Consider the following single-constraint linear program:


min c [T] x
s.t. a [T] x + b ≥ 0.

We consider the setting where the objective function is certain but the constraint coefficients are uncertain. We assume that the constraint coefficients

[a; b] belong to an ellipsoidal uncertainty set:



U = {[a; b] = [a [0] ; b [0] ] +



�k

uj[a [j] ; b [j] ], u 1 .
∥ ∥≤ }
j=1


172 CHAPTER 9. CONIC OPTIMIZATION TOOLS


Our objective is to find a solution that minimizes the objective function
among the vectors that are feasible for all [a; b] ∈U. In other words, we
want to solve
min c [T] x
s.t. a [T] x + b ≥ 0, ∀[a; b] ∈U.


For a fixed x the “robust” version of the constraint is satisfied if and
only if


0 min min (9.4)
≤ [a;b] [a][T][ x][ +][ b][ ≡] u: u 1 [α][ +][ u][T][ β,]
∈U ∥ ∥≤


where α = (a [0] ) [T] x + b [0] and β = (β1, . . ., βk) with βj = (a [j] ) [T] x + b [j] .
The second minimization problem in (9.4) is easy. Since α is constant, all
we need to do is to minimize u [T] β subject to the constraint ∥u∥≤ 1. Recall
that for the angle θ between vectors u and β the following trigonometric
equality holds:

u [T] β
cos θ =
∥u∥∥β∥ [,]

or u [T] β = ∥u∥∥β∥ cos θ. Since ∥β∥ is constant, this expression is minimized
when ∥u∥ = 1 and cos θ = −1. This means that u points in the opposite
direction from β, namely −β. Normalizing to satisfy the bound constraint
we obtain u [∗] = [Substituting this value we find]

β

      - ∥ [β] ∥ [as shown in Figure 9.2.]



�k

((a [j] ) [T] x + b [j] ) [2], (9.5)
j=1



min

[a;b] [a][T][ x][ +][ b][ =][ α][ −∥][β][∥] [= (][a][0][)][T][ x][ +][ b][0][ −]
∈U




~~�~~

~~�~~






and we obtain the robust version of the inequality a [T] x + b ≥ 0 as



�k

((a [j] ) [T] x + b [j] ) [2] ≥ 0. (9.6)
j=1



(a [0] ) [T] x + b [0] 










It is now easy to observe that (9.6) can be written equivalently using the
second-order cone:


zj = (a [j] ) [T] x + b [j], j = 0, . . . k

(z0, z1, . . ., zk) Cq
∈


The approach outlined above generalizes to multiple constraints as long
as the uncertainties are constraint-wise, that is, if the uncertainty sets of
parameters in different constraints are unrelated. Thus, robust optimization
models for uncertain linear constraints with ellipsoidal uncertainty leads
to SOCPs. The strategy outlined above is well-known and is used in, for
example, [7].


9.2. SECOND-ORDER CONE PROGRAMMING: 173


2



1.5


1


0.5


0


−0.5


−1


−1.5



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-172-0.png)





−2
−2 −1.5 −1 −0.5 0 0.5 1 1.5 2


Figure 9.2: Minimization of a linear function over a circle


9.2.2 Conversion of quadratic constraints into second-order
cone constraints


The second-order cone membership constraint (x0, x1, . . ., xk) Cq can be
∈ [ˆ]
written equivalently as the combination of a linear and a quadratic constraint:
x0 0, x [2] 0 1 k
≥ [−] [x][2] [−] [. . .][ −] [x][2] [≥] [0][.]

Conversely, any convex quadratic constraint of an optimization problem can
be rewritten using second-order cone membership constraints. When we
have access to a reliable solver for second-order cone optimization, it may
be desirable to convert convex quadratic constraints to second-order cone
constraints. Fortunately, a simple recipe is available for these conversions.
Consider the following quadratic constraint:


x [T] Qx + 2p [T] x + γ ≤ 0. (9.7)


This is a convex constraint if the function on the left-hand-side is convex
which is true if and only if Q is a positive semidefinite matrix. Let us assume
Q is positive definite for simplicity. In that case, there exists an invertible
matrix, say R, satisfying Q = RR [T] . For example, the Cholesky factor of Q
satisfies this property. Then, (9.7) can be written as


(R [T] x) [T] (R [T] x) + 2p [T] x + γ ≤ 0. (9.8)

Define y = (y1, . . ., yk) [T] = R [T] x + R [−][1] p. Then, we have


y [T] y = (R [T] x) [T] (R [T] x) + 2p [T] x + p [T] Q [−][1] p.


174 CHAPTER 9. CONIC OPTIMIZATION TOOLS


Thus, (9.8) is equivalent to


∃y s.t. y = R [T] x + R [−][1] p, y [T] y ≤ p [T] Q [−][1] p − γ.


From this equivalence, we observe that the constraint (9.7) can be satisfied
only if p [T] Q [−][1] p − γ ≥ 0–we will assume that this is the case.
Now, it is straightforward to note that (9.7) is equivalent to the following
set of linear equations coupled with a second-order cone constraint:









y1
...
yk




  y0 = p [T] Q [−][1] p γ,
        




 = R [T] x + R [−][1] p,



(y0, y1, . . ., yk) Cq.
∈



Exercise 9.4 Rewrite the following convex quadratic constraint in “conic
form”, i.e., as the intersection of linear equality constraints and a secondorder cone constraint:


10x [2] 1 [+ 2][x][1][x][2] [+ 5][x][2] 2 [+ 4][x][1] [+ 6][x][2] [+ 1][ ≤] [0][.]


Exercise 9.5 Discuss how the approach outlined in this section must be
modified to address the case when Q is positive semidefinite but not positive
definite. In this case there still exists a matrix R satisfying Q = RR [T] . But
R is no longer invertible and we can no longer define the vector y as above.

#### 9.3 Semidefinite programming:


In SDPs, the set of variables are represented by a symmetric matrix which
is required to be in the cone of positive semidefinite matrices in addition to
satisfying a system of linear equations. We say that a matrix M ∈ IR [n][×][n]

is positive semidefinite if y [T] My ≥ 0 for all y ∈ IR [n] . When M is symmetric, this is equivalent to M having eigenvalues that are all nonnegative. A
stronger condition is positive definiteness. M is positive definite if y [T] My - 0
for all y ∈ IR [n] with the exception of y = 0. For symmetric M, positive definiteness is equivalent to the positivity of all of its eigenvalues.
Since multiplication by a positive number preserves the positive semidefiniteness property, the set of positive semidefinite matrices is a cone. In fact,
it is a convex cone. The cone of positive semidefinite matrices of a fixed
dimension (say n) is defined as follows:



x11 x1n

     - · ·
... ... ...
xn1 xnn

     - · ·






. (9.9)







n n
 ∈ IR × : X ⪰ 0



Cs [n] [:=]






X =










Above, the notation X ⪰ 0 means that X is a symmetric positive semidefinite matrix. We provide a depiction of the cone of positive semidefinite


9.3. SEMIDEFINITE PROGRAMMING: 175


matrices of dimension 2 in Figure 9.3. The diagonal elements X11 and X22
of a 2-dimensional symmetric matrix are shown on the horizontal axes while
the off-diagonal element X12 = X21 is on the vertical axis. Symmetric
two-dimensional matrices whose elements lie inside the shaded region are
positive semidefinite matrices. As the nonnegative orthant and the secondorder cone, the cone of positive semidefinite matrices has a point or a corner
at the origin. Also note the convexity of the cone and the nonlinearity of its
boundary.


X=[X11 X12; X21 X22] positive semidefinite


1


0.8


0.6


0.4



0.2


0


−0.2


−0.4


−0.6


−0.8


−1
1



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-174-0.png)



1


X11



X22





Figure 9.3: The cone of positive semidefinite matrices


Semidefinite programming problems arise in a variety of disciplines. The
recent review by Todd provides an excellent introduction to their solution
methods and the rich set of applications [70]. One of the common occurrences of semidefiniteness constraints results from the so-called S-procedure,
which is a generalization of the well-known S-lemma [58]:


Lemma 9.1 Let Fi(x) = x [T] Aix + 2 + b [T] i [x][ +][ c][i][,] [i][ = 0][,][ 1][, . . ., p] [be] [quadratic]
functions of x ∈ IR [n] . Then,

Fi(x) 0, i = 1, . . ., p F0(x) 0
≥ ⇒ ≥



if there exist λi 0 such that
≥

        A0 b0
b [T] 0 c0












Ai bi
b [T] i ci







�p

λi
i=1



⪰ 0.



If p = 1, converse also holds as long as x0 s.t. F1(x0) > 0.
∃

The S-procedure provides a sufficient condition for the implication of a
quadratic inequality by other quadratic inequalities. Furthermore, this condition is also a necessary condition in certain special cases. This equivalence


176 CHAPTER 9. CONIC OPTIMIZATION TOOLS


can be exploited in robust modeling of quadratic constraints as we illustrate
next.


9.3.1 Ellipsoidal Uncertainty for Quadratic Constraints


This time we consider a convex-quadratically constrained problem where the
objective function is certain but the constraint coefficients are uncertain:


min c [T] x
s.t. −x [T] (A [T] A)x + 2b [T] x + γ ≥ 0, ∀[A; b; γ] ∈U,

where A ∈ IR [m][×][n], b ∈ IR [n] and γ is a scalar. We again consider the case
where the uncertainty set is ellipsoidal:



U = {[A; b; γ] = [A [0] ; b [0] ; γ [0] ] +



�k

uj[A [j] ; b [j] ; γ [j] ], u 1 .
∥ ∥≤ }
j=1



To reformulate the robust version of this problem we use the S-procedure
described above. The robust version of our convex quadratic inequality can
be written as


[A; b; γ] ∈U ⇒−x [T] (A [T] A)x + 2b [T] x + γ ≥ 0. (9.10)


This is equivalent to the following expression:



�k

A [j] uj) [T] x+2(b [0] +
j=1



�k



�k

b [j] uj) [T] x+(γ [0] +
j=1



�k



�k

γ [j] uj) 0.
≥
j=1



∥u∥≤ 1 ⇒−x [T] (A [0] +



�k

A [j] uj)(A [0] +
j=1



(9.11)
Defining A(x) : IR [n] → IR [m][×][k] as

                -                 A(x) = A [1] x|A [2] x| . . . |A [k] x,



b(x) : IR [n] → IR [k] as




    b(x) = x [T] b [1] x [T] b [2] . . . x [T] b [k][�][T] + [1]



2




γ [1] γ [2] . . . γ [k][�][T] - A(x) [T] A [0] x



and
γ(x) = γ [0] + 2(b [0] ) [T] x − x [T] (A [0] ) [T] A [0] x

and rewriting ∥u∥≤ 1 as −u [T] Iu + 1 ≥ 0 we can simplify (9.11) as follows:

−u [T] Iu + 1 ≥ 0 ⇒−u [T] A(x) [T] A(x)u + 2b(x) [T] u + γ(x) ≥ 0. (9.12)


Now we can apply Lemma 9.1 with p = 1, A1 = I, b1 = 0, c1 = 1 and
A0 = A(x) [T] A(x), b0 = b(x) and c0 = γ(x). Thus, the robust constraint
(9.12) can be written as







∃λ ≥ 0 s.t.




γ(x) − λ b(x) [T]

b(x) A(x) [T] A(x) − λI



⪰ 0. (9.13)


9.4. ALGORITHMS AND SOFTWARE 177


Thus, we transformed the robust version of the quadratic constraint into
a semidefiniteness constraint for a matrix that depends on the variables x
and also a new variable λ. However, because of the term A(x) [T] A(x), this
results in a nonlinear semidefinite optimization problem, which is difficult
and beyond the immediate territory of most conic optimization algorithms.
Fortunately, however, the semidefiniteness condition above is equivalent to
the following semidefiniteness condition:









 ⪰ 0 (9.14)



∃λ ≥ 0 s.t.



γ [′] (x) − λ b [′] (x) [T] (A [0] x) [T]
 b [′] (x) λI A(x) [T]



b [′] (x) λI A(x) [T]



A [0] x A(x) I



where

          b [′] (x) = x [T] b [1] x [T] b [2] . . . x [T] b [k][�][T] + [1]

2




γ [1] γ [2] . . . γ [k][�][T]



and
γ [′] (x) = γ [0] + 2(b [0] ) [T] x.


Since all of A(x), b [′] (x) and γ [′] (x) are linear in x, we obtain a linear semidefinite optimization problem from the reformulation of the robust quadratic
constraint via the S-procedure. For details of this technique and many other
useful results for reformulation of robust constraints, we refer the reader to

[7].


Exercise 9.6 Verify that (9.11) is equivalent to (9.10).


Exercise 9.7 Verify that (9.13) and (9.14) are equivalent.

#### 9.4 Algorithms and Software


Since most conic optimization problem classes are special cases of nonlinear
programming problems, they can be solved using general nonlinear optimization strategies we discussed in Chapter 5. As in linear and quadratic
programming problems, the special structure of conic optimization problems
allows the use of specialized and more efficient methods that take advantage of this structure. In particular, many conic optimization problems can
be solved efficiently using the generalizations of sophisticated interior-point
algorithms for linear and quadratic programming problems. These generalizations of interior-point methods are based on the ground-breaking work of
Nesterov and Nemirovski [54] as well as the theoretical and computational
advances that followed their work.
During the past decade, an intense theoretical and algorithmic study
of conic optimization problems produced a number of increasingly sophisticated software products for several problem classes including SeDuMi [69]
and SDPT3 [72] which are freely available. Interested readers can obtain
additional information on such software by following the software link of the
following page dedicated to semidefinite programming and maintained by
Christoph Helmberg:


178 CHAPTER 9. CONIC OPTIMIZATION TOOLS


http://www-user.tu-chemnitz.de/~helmberg/semidef.html
There are also commercial software products that address conic optimization problems. For example, MOSEK (www.mosek.com) provides a
powerful engine for second-order and linear cone optimization. AXIOMA’s
(www.axiomainc.com) portfolio optimization software employs a conic optimization solver that handles convex quadratic constraints as well as ellipsoidal uncertainties among other things.


## Chapter 10

# Conic Optimization Models in Finance

Conic optimization problems are encountered in a wide array of fields including truss design, control and system theory, statistics, eigenvalue optimization, and, antenna array weight design. Robust optimization formulations of
many convex programming problems also lead to conic optimization problems, see, e.g. [7, 8]. Furthermore, conic optimization problems arise as
relaxations of hard combinatorial optimization problems such as the maxcut problem. Finally, some of the most interesting applications of conic
optimization are encountered in financial mathematics and we will address
several examples in this chapter.

#### 10.1 Tracking Error and Volatility Constraints


In most quantitative asset management environments, portfolios are chosen
with respect to a carefully selected benchmark. Typically, the benchmark is
a market index, reflecting a particular market (e.g., domestic or foreign), or
a segment of the market (e.g., large cap growth) the investor wants to invest
in. Then, the portfolio manager’s problem is to determine an index tracking
portfolio with certain desirable characteristics. An index tracking portfolio
intends to track the movements of the underlying index closely with the
ultimate goal of adding value by beating the index. Since this goal requires
departures from the underlying index, one needs to balance the expected
excess return (i.e., expected return in excess of the benchmark return) with
the variance of the excess returns.
The tracking error for a given portfolio with a given benchmark refers to
the difference between the returns of the portfolio and the benchmark. If the
return vector is given by r, the weight vector for the benchmark portfolio
is denoted by xBM, and the weight vector for the portfolio is x, then this
difference is given as:


r [T] x r [T] xBM = r [T] (x xBM ).
            -            

While some references in the literature define tracking error as this quantity,


179


180 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE


we will prefer to refer to it as the excess return. Using the common conventions, we define tracking error as a measure of variability of excess returns.
The ex ante, or predicted tracking error of the portfolio (with respect to the
risk model given by Σ) is defined as follows:

        TE(x) := (x xBM ) [T] Σ(x xBM ). (10.1)
                -                
In contrast, the ex-post, or realized, tracking error is a statistical dispersion
measure for the realized excess returns, typically the standard deviation of
regularly (e.g., daily) observed excess returns.
In benchmark relative portfolio optimization, we solve mean-variance optimization problems where expected absolute return and standard deviation
of returns are replaced by expected excess return and the predicted tracking
error. For example, variance constrained MVO problem (8.3) is replaced by
the following formulation:



maxx µ [T] (x xBM )
          (x xBM ) [T] Σ(x xBM ) TE [2]
    -     - ≤

Ax = b
Cx ≥ d,



(10.2)



where x = (x1, . . ., xn) is the variable vector whose components xi denote
the proportion of the total funds invested in security i, µ and Σ are the
expected return vector and the covariance matrix, and A, b, C, and d are
the coefficients of the linear equality and inequality constraints that define
feasible portfolios. The objective is to maximize the expected excess return
while limiting the portfolio tracking error to a predefined value of TE.
Unlike the formulations (8.1) and (8.4) that have only linear constraints,
this formulation is not in standard quadratic programming form and therefore can not be solved directly using efficient and widely available QP algorithms. The reason for this is the existence of a nonlinear constraint, namely
the constraint limiting the portfolio tracking error. So, if all MVO formulations are essentially equivalent as we argued before, why would anyone use
the “harder” formulations with the risk constraint?
As Jorion observes [40], ex post returns are “enormously noisy measures
of expected returns” and therefore investors may not be able or willing
to determine minimum acceptable expected return levels, or risk-aversion
constants–inputs required for problems (8.1) and (8.4)–with confidence. Jorion [40] notes that “it is much easier to constrain the risk profile, either before or after the fact–which is no doubt why investors give managers tracking
error constraints.”
Fortunately, the tracking error constraint is a convex quadratic constraint which means that we can rewrite this constraint in conic form as we
saw in the previous chapter. If the remaining constraints are linear as in
(10.2), the resulting problem is a second-order cone optimization problem
that can be solved with specialized methods.
Furthermore, in situations where the control of multiple measures of risk
is desired the conic reformulations can become very useful. In [40], Jorion observes that MVO with only a tracking error constraint may lead to


10.1. TRACKING ERROR AND VOLATILITY CONSTRAINTS 181



portfolios with high overall variance. He considers a model where a variance
constraint as well as a tracking error constraint is imposed for optimizing the
portfolio. When no additional constraints are present, Jorion is able to solve
the resulting problem since analytic solutions are available. His approach,
however, does not generalize to portfolio selection problems with additional
constraints such as no-shorting limitations, or exposure limitations to such
factors as size, beta, sectors or industries. The strength of conic optimization models, and in this particular case, of second-order cone programming
approaches is that the algorithms developed for them will work for any combination of linear equality, linear inequality, and convex quadratic inequality
constraints. Consider, for example, the following generalization of the models in [40]:
maxx ~~√~~ x [T] µΣ [T] xx σ



x [T] Σx σ

≤
(x xBM ) [T] Σ(x xBM ) TE
  -   - ≤
Ax = b
Cx ≥ d.



(10.3)



This problem can be rewritten as a second-order cone programming problem
using the conversions outlined in Section 9.2.2. Since Σ is positive semidefinite, there exists a matrix R such that Σ = RR [T] . Defining


y = R [T] x

z = R [T] x R [T] xBM
                 
we see that the first two constraints of (10.3) are equivalent to (y0, y) Cq,
∈
(z0, z) Cq with y0 = σ and z0 = TE. Thus, (10.3) is equivalent to the
∈
following second-order cone program:



maxx µ [T] x
Ax = b
Cx ≥ d
R [T] x − y = 0
R [T] x z = R [T] xBM
     y0 = σ
z0 = TE
(y0, y) Cq, (z0, z) Cq
∈ ∈



(10.4)



Exercise 10.1 Second-order cone formulations can also be used for modeling a tracking error constraint under different risk models. For example, if we
had k alternative estimates of the covariance matrix denoted by Σ1, . . ., Σk
and wanted to limit the tracking error with respect to each estimate we
would have a sequence of constraints of the form

~~�~~
(x xBM ) [T] Σi(x xBM ) TEi, i = 1, . . ., k.
        -         - ≤

Show how these constraints can be converted to second-order cone constraints.


182 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE


Exercise 10.2 Using historical returns of the stocks in the DJIA, estimate
their mean µi and covariance matrix. Let R be the median of the µis. Find
an expected return maximizing long-only portfolio of Dow Jones constituents
that has (i) a tracking error of 10% or less, and (ii) a volatility of 20% or
less.

#### 10.2 Approximating Covariance Matrices


The covariance matrix of a vector of random variables is one of the most
important and widely used statistical descriptors of the joint behavior of
these variables. Covariance matrices are encountered frequently is financial
mathematics, for example, in mean-variance optimization, in forecasting, in
time-series modeling, etc.
Often, true values of covariance matrices are not observable and one
must rely on estimates. Here, we do not address the problem of estimating covariance matrices and refer the reader, e.g., to Chapter 16 in [48].
Rather, we consider the case where a covariance matrix estimate is already
provided and one is interested in determining a modification of this estimate
that satisfies some desirable properties. Typically, one is interested finding
the smallest distortion of the original estimate that achieves these desired
properties.
Symmetry and positive semidefiniteness are structural properties shared
by all “proper” covariance matrices. A correlation matrix satisfies the additional property that its diagonal consists of all ones. Recall that a symmetric
and positive semidefinite matrix M ∈ IR [n][×][n] satisfies the property that

x [T] Mx ≥ 0, ∀x ∈ IR [n] .


This property is equivalently characterized by the nonnegativity of the eigenvalues of the matrix M .
In some cases, for example when the estimation of the covariance matrix
is performed entry-by-entry, the resulting estimate may not be a positive
semidefinite matrix, that is it may have negative eigenvalues. Using such
an estimate would suggest that some linear combinations of the underlying
random variables have negative variance and possibly result in disastrous
results in mean-variance optimization. Therefore, it is important to correct
such estimates before they are used in any financial decisions.
Even when the initial estimate is symmetric and positive semidefinite, it
may be desirable to modify this estimate without compromising these properties. For examples, if some pairwise correlations or covariances appear
counter-intuitive to a financial analyst’s trained eye, the analyst may want
to modify such entries in the matrix. All these variations of the problem of
obtaining a desirable modification of an initial covariance matrix estimate
can be formulated within the powerful framework of semidefinite optimization and can be solved with standard software available for such problems.
We start the mathematical treatment of the problem by assuming that
we have an estimate Σ [ˆ] ∈S [n] of a covariance matrix and that Σ [ˆ] is not


10.2. APPROXIMATING COVARIANCE MATRICES 183


necessarily positive semidefinite. Here, S [n] denotes the space of symmetric
n × n matrices. An important question in this scenario is the following:
What is the “closest” positive semidefinite matrix to Σ? [ˆ] For concreteness,
we use the Frobenius norm of the distortion matrix as a measure of closeness:

         
~~�~~
dF (Σ, Σ) := [ˆ] (Σij            - Σ [ˆ] ij) [2] .

i,j


Now we can state the closest covariance matrix problem as follows: Given
ˆΣ ∈S [n],
minΣ dF (Σ, Σ) [ˆ]
(10.5)
Σ Cs [n]
∈

where Cs [n] [is] [the] [cone] [of] [n][ ×][ n] [symmetric] [and] [positive] [semidefinite] [matrices]
as defined in (9.9). Notice that the decision variable in this problem is
represented as a matrix rather than a vector as in all previous optimization
formulations we considered.
Furthermore, introducing a dummy variable t, we can rewrite the last
problem above as:
min t
dF (Σ, Σ) [ˆ] ≤ t
Σ ∈ Cs [n][.]

It is easy to see that the inequality dF (Σ, Σ) [ˆ] t can be written as a second≤
order cone constraint, and therefore, the formulation above can be transformed into a conic optimization problem.
Variations of this formulation can be obtained by introducing additional
linear constraints. As an example, consider a subset E of all (i, j) covariance
pairs and lower/upper limits lij, uij (i, j) E that we wish to impose on
∀ ∈
these entries. Then, we would need to solve the following problem:


min dF (Σ, Σ) [ˆ]
lij Σij uij, (i, j) E (10.6)
≤ ≤ ∀ ∈
Σ ∈ Cs [n][.]

When E consists of all the diagonal (i, i) elements and lii = uii = 1, i,
∀
we get the correlation matrix version of the original problem. For example,
three-dimensional correlation matrices have the following form:





, Σ ∈ Cs [3][.]



Σ =





1 x y
 x 1 z
y z 1



The feasible set for this instance is shown in Figure 10.2.



Example 10.1 We consider the following estimate of the correlation matrix
of 4 securities:



1.0 0.8 0.5 0.2
0.8 1.0 0.9 0.1
0.5 0.9 1.0 0.7
0.2 0.1 0.7 1.0



. (10.7)








ˆΣ =








184 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE


1


0.5


0


−0.5


−1
1



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-183-0.png)



1











−1



−1





y −1 x



Figure 10.1: The feasible set of the nearest correlation matrix problem in
3-dimensions


This, in fact, is not a valid correlation matrix; its smallest eigenvalue is
negative: λmin = 0.1337. Note, for example, the high correlations between
       assets 1 and 2 as well as assets 2 and 3. This suggests that 1 and 3 should
be highly correlated as well, but they are not. Which entry should one adjust
to find a valid correlation matrix?
We can approach this problem using formulation (10.6) with E consisting
of all the diagonal (i, i) elements and lii = uii = 1, i. Solving the result∀
ing problem, for example, using SDPT3 [72], we obtain (approximately) the
following nearest correction to Σ [ˆ] :



1.00 0.76 0.53 0.18
0.76 1.00 0.82 0.15
0.53 0.82 1.00 0.65
0.18 0.15 0.65 1.00






.




Σ =









Exercise 10.3 Use a semidefinite optimization software package to verify
that Σ given above is the solution to (10.5) when Σ [ˆ] is given by (10.7).


Exercise 10.4 Resolve the problem above, this time imposing the constraint that Σ23 = Σ32 0.85.
≥


One can consider several variations on the “plain vanilla” version of the
nearest correlation matrix problem. For example, if we would rather keep
some of the entries of the matrix Σ [ˆ] constant, we can expand the set E to
contain those elements with matching lower and upper bounds. Another
possibility is to weight the changes in different entries, for example if estimates of some entries are more trust-worthy than others.


10.3. RECOVERING RISK-NEURAL PROBABILITIES FROM OPTIONS PRICES185


Another important variation of the original problem is obtained by placing lower limits on the smallest eigenvalue of the correlation matrix. Even
when we have a valid (positive semidefinite) correlation matrix estimate,
having small eigenvalues in the matrix can be undesirable as they lead to
unstable portfolios. Indeed, the valid correlation matrix we obtained above
has a positive but very small eigenvalue, which would in fact be exactly
zero in exact arithmetic. Hauser and Zuev consider models where minimum
eigenvalue of the covariance matrix is maximized and use the matrices in a
robust optimization setting [37].


Exercise 10.5 We want to find the nearest symmetric matrix to Σ in (10.7) [ˆ]
whose smallest eigenvalue is at least 0.25. Express this problem as a semidefinite optimization problem. Solve it using an SDP software package.


All these variations are easily handled using semidefinite programming
formulations and solved using semidefinite optimization software. As such,
semidefinite optimization presents a new tool for asset managers that was
not previously available at this level of sophistication and flexibility. While
these tools are not yet available as commercial software packages, many
academic products are freely available; see the link given in Section 9.4.

#### 10.3 Recovering Risk-Neural Probabilities from Op- tions Prices


In this section, we revisit our study of the risk-neutral density estimation
problem in Section 8.4. Recall that the objective of this problem is to
estimate an implied risk-neutral density function for the future price of an
underlying security using the prices of options written on that security. Representing the density function using cubic splines to ensure its smoothness,
and using a least-squares type objective function for the fit of the estimate
with the observed option prices, we formulated an optimization problem in
Section 8.4.
One issue that we left open in Section 8.4 is the rigorous enforcement of
the nonnegativity of the risk-neutral density estimate. While we heuristically handled this issue by enforcing the nonnegativity of the cubic splines
at the knots, it is clear that a cubic function that is nonnegative at the endpoints of an interval can very well become negative in between and therefore,
the heuristic technique of Section 8.4 may be inadequate. Here we discuss an
alternative formulation that is based on necessary and sufficient conditions
for ensuring the nonnegativity of a single variable polynomial in intervals.
This characterization is due to Bertsimas and Popescu [10] and is stated in
the next proposition.


Proposition 10.1 (Proposition 1 (d),[10]) The polynomial g(x) = [�][k] r=0 [y][r][x][r]

satisfies g(x) ≥ 0 for all x ∈ [a, b] if and only if there exists a positive


186 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE



semidefinite matrix X = [xij]i,j=0,...,k such that

  


xij = 0, ℓ = 1, . . ., k, (10.8)
i,j:i+j=2ℓ−1



��
k − r
ℓ   - m







k+�m−ℓ




 
xij =
i,j:i+j=2ℓ



�ℓ




r
m



a [r][−][m] b [m], (10.9)



m=0



yr
r=m



ℓ = 0, . . ., k, (10.10)



X ⪰ 0. (10.11)







In the statement of the proposition above, the notation




r
m



stands for



r! [X] [indicates] [that] [the] [matrix] [X] [is] [symmetric] [and] [positive]
m!(r−m)! [and] [⪰] [0]
semidefinite. For the cubic polynomials fs(x) = αsx [3] + βsx [2] + γsx + δs that
are used in the formulation of Section 8.4, the result can be simplified as
follows:


Corollary 10.1 The polynomial fs(x) = αsx [3] + βsx [2] + γsx + δs satisfies
fs(x) 0 for all x [xs, xs+1] if and only if there exists a 4 4 matrix
≥ ∈ ×
X [s] = [x [s] ij []][i,j][=0][,...,][3] [such] [that]



x [s] ij = 0, if i + j is 1 or 5,
x [s] 03 [+][ x] 12 [s] [+][ x] 21 [s] [+][ x] 30 [s] = 0,
x [s] 00 = αsx [3] s [+][ β][s][x] s [2] [+][ γ][s][x][s] [+][ δ][s][,]
x [s] 02 [+][ x] 11 [s] [+][ x] 20 [s] = 3αsx [2] s [x][s][+1] [+][ β][s][(2][x][s][x][s][+1] [+][ x][2] s [)]
+ γs(xs+1 + 2xs) + 3δs,
x [s] 13 [+][ x] 22 [s] [+][ x] 31 [s] = 3αsxsx [2] s+1 [+][ β][s][(2][x][s][x][s][+1][ +][ x] s [2] +1 [)]
+ γs(xs + 2xs+1) + 3δs,
x [s] 33 = αsx [3] s+1 [+][ β][s][x] s [2] +1 [+][ γ][s][x][s][+1][ +][ δ][s][,]
X [s] ⪰ 0.



(10.12)



Observe that the positive semidefiniteness of the matrix X [s] implies that
the first diagonal entry x [s] 00 [is] [nonnegative,] [which] [corresponds] [to] [our] [earlier]
requirement fs(xs) 0. In light of Corollary 10.1, we see that introducing
≥
the additional variables X [s] and the constraints (10.12), for s = 1, . . ., ns,
into the earlier quadratic programming problem in Section 8.4, we obtain
a new optimization problem which necessarily leads to a risk-neutral probability distribution function that is nonnegative in its entire domain. The
new formulation has the following form:


min E(y) s.t. (8.19), (8.20), (8.21), (8.22), (8.25), [(10.12), s = 1, . . ., ns].
y,X [1],...,X [ns]

(10.13)
All constraints in (10.13), with the exception of the positive semidefiniteness constraints X [s] 0, s = 1, . . ., ns, are linear in the optimization
⪰
variables (αs, βs, γs, δs) and X [s], s = 1, . . ., ns. The positive semidefiniteness
constraints are convex constraints and thus the resulting problem can be reformulated as a convex semidefinite programming problem with a quadratic
objective function.


10.4. ARBITRAGE BOUNDS FOR FORWARD START OPTIONS 187


For appropriate choices of the vectors c, fi, gk [s][,] [and] [matrices] [Q] [and] [H] k [s][,]
we can rewrite problem (10.13) in the following equivalent form:

miny,X 1,...,X ns c [T] y + [1] 2 [y][T][ Qy]

s.t. fi [T] [y] [=][ b][i][,] [i][ = 1][, . . .,][ 3][n][s][,]



Hk [s] [= 0][,] [k] [= 1][,][ 2][,] [s][ = 1][, . . ., n][s][,]

[•][ X] [s]



(gk [s][)][T][ y][ +][ H] k [s] [•][ X] [s] [= 0][,] [k] [= 3][,][ 4][,][ 5][,][ 6][,] [s][ = 1][, . . ., n][s][,]



X [s] 0, s = 1, . . ., ns,
⪰
(10.14)
where - denotes the trace matrix inner product.
We should note that standard semidefinite optimization software such as
SDPT3 [72] can solve only problems with linear objective functions. Since
the objective function of (10.14) is quadratic in y a reformulation is necessary
to solve this problem using SDPT3 or other SDP solvers. We can replace the
objective function with min t where t is a new artificial variable and impose
the constraint t c [T] y + [1] [This] [new] [constraint] [can] [be] [expressed] [as]
≥ 2 [y][T][ Qy][.]



the constraint t c [T] y + [1] [This] [new] [constraint] [can] [be] [expressed] [as]
≥ 2 [y][T][ Qy][.]

a second-order cone constraint after a simple change of variables; see, e.g.,

[49]. This final formulation is a standard form conic optimization problem

- a class of problems that contain semidefinite programming and secondorder cone programming as special classes. Since SDPT3 can solve standard
form conic optimization problems we used this formulation in our numerical
experiments.



Exercise 10.6 Express the constraint t c [T] y + [1] [using] [linear] [con-]

2 [y][T][ Qy]

≥

straints and a second-order cone constraint.

#### 10.4 Arbitrage Bounds for Forward Start Options


When pricing securities with complicated payoff structures, one of the strategies analysts use is to develop a portfolio of “related” securities in order to
form a super (or sub) hedge and then use no-arbitrage arguments to bound
the price of the complicated security. Finding the super or sub hedge that
gives the sharpest no-arbitrage bounds is formulated as an optimization
problem. We considered an similar approach in Section 4.2 when we used
linear programming models for detecting arbitrage possibilities in prices of
European options with a common underlying asset and same maturity.
In this section, we consider the problem of finding arbitrage bounds for
prices of forward start options using prices of standard options expiring
either at the activation or expiration date of the forward start option. As
we will see this problem can be solved using semidefinite optimization. The
tool we use to achieve this is the versatile result of Bertsimas and Popescu
given in Proposition 10.1.
A forward start option is an advance purchase, say at time T0, of a put
or call option that will become active at some specified future time, say T1.
These options are encountered frequently in employee incentive plans where
an employee may be offered an option on the company stock that will be


188 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE


available after the employee remains with the company for a predetermined
length of time. A premium is paid at T0, and the underlying security and
the expiration date (T2) are specified at that time. Let S1 and S2 denote
the spot price of the underlying security at times T1 and T2, respectively.

The strike price is described as a known function of S1 but is unknown
at T0. It is determined at T1 when the option becomes active. Typically,
it is chosen to be the value of the underlying asset at that time, i.e., S1, so
that the option is at-the-money at time T1. More generally, the strike can
be chosen as γS1 for some positive constant γ. We address the general case
here. The payoff to the buyer of a forward start call option at time T2 is
max(0, S2 γS1) = (S2 γS1) [+], and similarly it is (γS1 S2) [+] for puts.
    -     -     
Our primary objective is to find tightest possible no-arbitrage bounds
(i.e., maximize the lower bound and minimize the upper bound) by finding
the best possible sub- and super-replicating portfolios of European options
of several strikes with exercise dates at T1 and also others with exercise dates
at T2. We will also consider the possibility of trading the underlying asset
at time T1 in a self-financing manner (via risk-free borrowing/lending). For
concreteness, we limit our attention to the forward start call option problem
and only consider calls for replication purposes. Since we allow the shorting
of calls, the omission of puts does not lose generality.


We show how to (approximately) solve the following problem: Find the
cheapest portfolio of the underlying (traded now and/or at T1), cash, calls
expiring at time T1, and calls expiring at time T2, such that the payoff from
the portfolio always is at least max(0, S2 φ(S1)), no matter what S1 and
                 S2 turn out to be. There is a similar lower bound problem which can be
solved identically.


For simplification, we assume throughout the rest of this discussion that
the risk-free interest rate r is zero and that the underlying does not pay
any dividends. We also assume throughout the discussion that the prices of
options available for replication are arbitrage-free which implies the existence
of equivalent martingale measures consistent with these prices. Furthermore,
we ignore trading costs.


10.4.1 A Semi-Static Hedge


For replication purposes, we assume that a number of options expiring at
T1 and T2 are available for trading. Let K1 [1] [<] [K] 2 [1] [<] [. . .] [<] [K] m [1] [denote] [the]
strike prices of options expiring at T1 and K1 [2] [<] [K] 2 [2] [<] [. . .] [<] [K] n [2] [denote]
the strike prices of the options expiring at T2. Let p [1] = (p [1] 1 [, . . ., p] m [1] [)] [and]
p [2] = (p [2] 1 [, . . ., p] n [2] [)] [denote] [the] [(arbitrage] [free)] [prices] [of] [these] [options] [at] [time]
T0.

We assume that K1 [1] [=] [0,] [so] [that] [the] [first] [”call”] [is] [the] [underlying] [itself]
and p [1] 1 [=] [S][0][,] [the] [price] [of] [the] [underlying] [at] [T][0][.] [For] [our] [formulation,] [let]
x = (x1, x2, . . ., xm) and y = (y1, y2, . . ., yn) correspond to the positions in
the T1 and T2-expiry options in our portfolio. Let B denote the cash position


10.4. ARBITRAGE BOUNDS FOR FORWARD START OPTIONS 189


in the portfolio at time T0. Then the cost of this portfolio is



�n

p [2] j [y][j] [+][ B.] (10.15)
j=1



c(x, y, B) :=



�m

p [1] i [x][i] [+]
i=1



With only positions in these call options, we would have a static hedge.
To improve the bounds, we consider a semi-static hedge that is rebalanced
at time T1 through the purchase of underlying shares whose quantity is
determined based on the price of the underlying at that time. If f (S1)
shares of the underlying is purchased at time T1 and if this purchase is
financed by risk-free borrowing, our overall position would have the final
payoff of:



g(S1, S2) := gS(S1, S2) + f (S1)(S2 S1) (10.16)

m n −



�n



(S2 Kj [2][)][+][y][j] [+][ B][ +][ f] [(][S][1][)(][S][2]
j=1 - [−] [S][1][)][.]



=



�m



(S1 Ki [1][)][+][x][i] [+]
i=1 


Exercise 10.7 Verify equation (10.16).


Then, we would find the lower and upper bounds on the price of the
forward start option by solving the following problems:


u := minx,y,B,f c(x, y, B) (10.17)
s.t. g(S1, S2) (S2 γS1) [+], S1, S2 0
≥          - ∀ ≥

The inequalities in this optimization problem ensure the super-replication
properties of the semi-static hedge we constructed. Unfortunately, there are
infinitely many constraints indexed by the parameters S1 and S2. Therefore,
(10.17) is a semi-infinite linear optimization problems and can be difficult.
Fortunately, however, the constraint functions are expressed using piecewiselinear functions of S1 and S2. The breakpoints for these functions are at the
strike sets {K1 [1][, . . ., K] m [1] [}] [and] [{][K] 1 [2][, . . ., K] n [2][}][.] [The] [right-hand-side] [function]
(S2 γS1) [+] has breakpoints along the line S2 = γS1. The remaining diffi  culty is about the specification of the function f . By limiting our attention
to functions f that are piecewise linear we will obtain a conic optimization
formulation.
A piecewise linear function f (S1) is determined by its values at the breakpoints: zi = f (Ki [1][) for][ i][ = 1][, . . ., m][ and its slope past][ K] m [1] [the last breakpoint]
given by λz = f (Km [1] [+ 1)][ −] [f] [(][K] m [1] [).]
Thus, we approximate f (S1) as



f (S1) =




zi + (S1 Ki [1][)] K [z] i [1][i] +1 [+1][−][−][K][z][i]
     


zm + (S1 − Km [1] [)][λ][z] if S1 ≥ Km [1] [.]



K [z] i [1][i] +1 [+1][−][−][K][z][i] i [1] if S1 ∈ [Ki [1][, K] i [1] +1 [)][,]



Next, we consider a decomposition of the nonnegative orthant (S1, S2
≥
0) into a grid with breakpoints at Ki [1][’s and][ K] j [2][’s such that the payoff function]


190 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE


is linear in each box Bij = [Ki [1][, K] i [1] +1 []][ ×][ [][K] j [2][, K] j [2] +1 []:]



(S2 Kl [2][)][+][y][l] [+][ B][ + (][S][2]
l=1 - [−] [S][1][)][f] [(][S][1][)]



g(S1, S2) =


=



�n

(S1 Kk [1][)][+][x][k] [+]
k=1 


�i

(S1 Kk [1][)][x][k] [+]
k=1 


�n



zi + (S1 Ki [1][)] [z][i][+1][ −] [z][i]
    - Ki [1] +1 i

[−] [K][1]







�j

(S2 Kl [2][)][y][l] [+][ B][ + (][S][2]
l=1 - [−] [S][1][)]







Recall that we want to super-replicate the payoff (S2 γS1) [+] . This is

                the term g(S1, S2) must exceed for all S1, S2. When we consider the box
Bij := [Ki [1][, K] i [1] +1 []][ ×][ [][K] j [2][, K] j [2] +1 []] [there] [are] [three] [possibilities] [involving] [γ][;] [see]
also Figure 10.4.1:



0



i+1 i


i+1


|Case 2: S2 = γS1, γ > K Kj2 + 11<br>i<br>Case 3: S2 = γS1<br>2<br>n<br>2<br>+1<br>Case 1:<br>1<br>2|Col2|Col3|
|---|---|---|
|2<br>|||
|1<br><br><br>~~+1~~|||
|2<br><br><br>|||
||||



0 = K1 [1] Ki [1] Ki [1] +1 Km [1]


Figure 10.2: Three possible relative positions of the S2 = γS1 line


1. S2  - γS1 for all (S1, S2) Bij. Then, we replace (S2 γS1) [+] with
∈           (S2 γS1).
    
2. S2 < γS1 for all (S1, S 2) Bij. Then, we replace (S2 γS1) [+] with
            - ∈             0.


3. Otherwise, we replace g(S1, S2) (S2 γS1) [+] with the two inequalities
≥                g(S1, S2) (S2 γS1) and g(S1, S2) 0.
≥       - ≥

In all cases, we remove the nonlinearity on the RHS. Now, we can rewrite
the super-replication inequality


g(S1, S2) (S2 γS1)+, (S1, S2) Bij as (10.18)
≥            - ∀ ∈

αij(w)S1 [2] [+][ β][ij][(][w][)][S][1][ +][ δ][ij][(][w][)][S][1][S][2][ +][ ϵ][ij][(][w][)][S][2][ +][ η][ij][(][w][)][ ≥] [0][,][ ∀][(][S][1][, S][2][)][ ∈] (10.19) [B][ij]


where w = (x, y, z, B) represents the variables of the problem collectively
and the constants αij etc. are linear functions of these variables that are
easily obtained. In Case 3, we have two such inequalities rather than one.
Thus, the super-replication constraints in each box are polynomial inequalities that must hold within these boxes. This is very similar to the
situation addressed by Proposition 10.1 with the important distinction that
these polynomial inequalities are in two variables rather than one.


10.4. ARBITRAGE BOUNDS FOR FORWARD START OPTIONS 191


Next, observe that for a fixed value of S1, the function on the left-handside of inequality (10.19) is linear in S2. Let us denote this function with
hij(S1, S2). Since it is linear in S2, for a fixed value of S1, hij will assume its
minimum value in the interval [Kj [2][, K] j [2] +1 []] [either] [at] [S][2] [=][ K] j [2] [or] [S][2] [=][ K] j [2] +1 [.]
Thus, if hij(S1, Kj [2][)] [≥] [0] [and] [h][ij][(][S][1][, K] j [2] +1 [)] [≥] [0,] [then] [h][ij][(][S][1][, S][2][)] [≥] [0][,][ ∀][S][2] [∈]

[Kj [2][, K] j [2] +1 []][.] [As] [a] [result,] [h][ij][(][S][1][, S][2][)] [≥] [0][,][ ∀][(][S][1][, S][2][)] [∈] [B][ij] [is] [equivalent] [to] [the]
following two constraints:


Hij [l] [(][S][1][) :=][ h][ij][(][S][1][, K] j [2][)] ≥ 0, ∀S1 ∈ [Ki [1][, K] i [1] +1 []][,]

Hij [u] [(][S][1][) :=][ h][ij][(][S][1][, K] j [2] +1 [)] ≥ 0, ∀S1 ∈ [Ki [1][, K] i [1] +1 []]


The situation is illustrated in Figure 10.4.1. Instead of satisfying the inequality on the whole box as in the left-hand-side figure, we only need to
consider two line segments as in the right-hand-side figure.



0





0




|2<br>n<br>2<br>+1<br>Bij<br>1<br>2|Col2|Col3|
|---|---|---|
|2<br>|||
|1<br><br><br>~~+1~~|Bij||
|2<br><br><br>|||
||||


|2<br>n<br>2<br>+1<br>Bij<br>1<br>2|Col2|Col3|
|---|---|---|
|2<br>|||
|1<br><br><br>~~+1~~|Bij||
|2<br><br><br>|||
||||



0 = K1 [1] Ki [1] Ki [1] +1 Km [1]



0 = K1 [1] Ki [1] Ki [1] +1 Km [1]



Figure 10.3: Super-replication constraints in the box Bij and on the line
segments


The bivariate polynomial inequality is reduced to two univariate polynomial inequalities. Now, we can use the Bertsimas/Popescu result and
represent this inequality efficiently. In summary, the super-replication constraints can be rewritten using a finite number of linear constraints and
semidefiniteness constraints. Since Hij [l] [and] [H] ij [u] [are] [quadratic] [polynomials]
in S1, semidefiniteness constraints are on 3 3 matrices (see Proposition
×
10.1) and are easily handled with semidefinite programming software.


192 CHAPTER 10. CONIC OPTIMIZATION MODELS IN FINANCE


## Chapter 11

# Integer Programming: Theory and Algorithms

#### 11.1 Introduction

A linear programming model for constructing a portfolio of assets might produce a solution with 3,205.7 shares of stock XYZ and similarly complicated
figures for the other assets. Most portfolio managers would have no trouble
rounding the value 3,205.7 to 3,205 shares or even 3,200 shares. In this case,
a linear programming model would be appropriate. Its optimal solution can
be used effectively by the decision maker, with minor modifications. On the
other hand, suppose that the problem is to find the best among many alternatives (for example, a traveling salesman wants to find a shortest route
going through 10 specified cities). A model that suggests taking fractions of
the roads between the various cities would be of little value. A 0,1 decision
has to be made (a road between a pair of cities is either on the shortest
route or it is not), and we would like the model to reflect this.
This integrality restriction on the variables is the central aspect of integer programming. From a modeling standpoint, integer programming has
turned out to be useful in a wide variety of applications. With integer
variables, one can model logical requirements, fixed costs and many other
problem aspects. Many software products can change a linear programming
problem into an integer program with a single command.
The downside of this power, however, is that problems with more than a
thousand variables are often not possible to solve unless they show a specific
exploitable structure. Despite the possibility (or even likelihood) of enormous computing times, there are methods that can be applied to solving
integer programs. The most widely used is “branch and bound” (it is used,
for example, in SOLVER). More sophisticated commercial codes (CPLEX
and XPRESS are currently two of the best) use a combination of “branch
and bound” and another complementary approach called “cutting plane”.
Open source software codes in the COIN-OR library also implement a combination of branch and bound and cutting plane, called “branch and cut”
(such as cbc, which stands for COIN Branch and Cut or bcp, which stands
for Branch, Cut and Price). The purpose of this chapter is to describe some


193


194CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


of the solution techniques. For the reader interested in learning more about
integer programming, we recommend Wolsey’s introductory book [74]. The
next chapter discusses problems in finance that can be modeled as integer programs: combinatorial auctions, constructing an index fund, portfolio
optimization with minimum transaction levels.
First we introduce some terminology. An integer linear program is a linear program with the additional constraint that some of, or all, the variables
are required to be integer. When all variables are required to be integer the
problem is called a pure integer linear program. If some variables are restricted to be integer and some are not then the problem is a mixed integer
linear program, denoted MILP. The case where the integer variables are restricted to be 0 or 1 comes up surprisingly often. Such problems are called
pure (mixed) 0–1 linear programs or pure (mixed) binary integer linear programs. The case of an NLP with the additional constraint that some of the
variables are required to be integer is called MINLP is receiving an increasing amount of attention from researchers. In this chapter, we concentrate
on MILP.

#### 11.2 Modeling Logical Conditions


Suppose we wish to invest $19,000. We have identified four investment opportunities. Investment 1 requires an investment of $6,700 and has a net
present value of $8,000; investment 2 requires $10,000 and has a value of
$11,000; investment 3 requires $5,500 and has a value of $6,000; and investment 4 requires $3,400 and has a value of $4,000. Into which investments
should we place our money so as to maximize our total present value? Each
project is a “take it or leave it” opportunity: It is not allowed to invest
partially in any of the projects. Such problems are called capital budgeting
problems.
As in linear programming, our first step is to decide on the variables.
In this case, it is easy: We will use a 0–1 variable xj for each investment.
If xj is 1 then we will make investment j. If it is 0, we will not make the
investment.
This leads to the 0–1 programming problem:


max 8x1 + 11x2 + 6x3 + 4x4
subject to
6.7x1 + 10x2 + 5.5x3 + 3.4x4 ≤ 19
xj = 0 or 1.


Now, a straightforward “bang for buck” suggests that investment 1 is the
best choice. In fact, ignoring integrality constraints, the optimal linear programming solution is x1 = 1, x2 = 0.89, x3 = 0, x4 = 1 for a value of $21,790.
Unfortunately, this solution is not integral. Rounding x2 down to 0 gives a
feasible solution with a value of $12,000. There is a better integer solution,
however, of x1 = 0, x2 = 1, x3 = 1, x4 = 1 for a value of $21,000. This
example shows that rounding does not necessarily give an optimal solution.


11.2. MODELING LOGICAL CONDITIONS 195


There are a number of additional constraints we might want to add. For
instance, consider the following constraints:


1. We can only make two investments.


2. If investment 2 is made, then investment 4 must also be made.


3. If investment 1 is made, then investment 3 cannot be made.


All of these, and many more logical restrictions, can be enforced using
0–1 variables. In these cases, the constraints are:


1. x1 + x2 + x3 + x4 ≤ 2

2. x2 x4 0
    - ≤

3. x1 + x3 ≤ 1.


Solving the model with SOLVER


Modeling an integer program in SOLVER is almost the same as modeling a
linear program. For example, if you placed binary variables x1, x2, x3, x4 in
cells $B$5:$B$8, simply Add the constraint
$B$5:$B$8 Bin
to your other constraints in the SOLVER dialog box. Note that the Bin
option is found in the small box where you usually indicate the type of
inequality: =, <= or >=. Just click on Bin. That’s all there is to it!


It is equally easy to model an integer program within other commercial
codes. The formulation might look as follows.


! Capital budgeting example
VARIABLES
x(i=1:4)
OBJECTIVE
Max: 8*x(1) + 11*x(2) + 6*x(3) + 4*x(4)
CONSTRAINTS
Budget: 6.7*x(1) + 10*x(2) + 5.5*x(3) + 3.4*x(4) < 19
BOUNDS
x(i=1:4) Binary
END


Exercise 11.1 As the leader of an oil exploration drilling venture, you must
determine the best selection of 5 out of 10 possible sites. Label the sites
s1, s2, . . ., s10 and the expected profits associated with each as p1, p2, . . ., p10.


(i) If site s2 is explored, then site s3 must also be explored. Furthermore,
regional development restrictions are such that


(ii) Exploring sites s1 and s7 will prevent you from exploring site s8.


196CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


(iii) Exploring sites s3 or s4 will prevent you from exploring site s5.


Formulate an integer program to determine the best exploration scheme and
solve with SOLVER.


Solution:  max 10j=1 [p][j][x][j]
subject to

     10j=1 [x][j] = 5
x2 x3 0
          - ≤
x1 + x7 + x8 ≤ 2
x3 + x5 ≤ 1
x4 + x5 ≤ 1
xj = 0 or 1 for j = 1, . . ., 10.


Exercise 11.2 Consider the following investment projects where, for each
project, you are given its NPV as well as the cash outflow required during
each year (in million dollars).

|Col1|NPV|Year 1 Year 2 Year 3 Year 4|
|---|---|---|
|Project 1<br>Project 2<br>Project 3<br>Project 4<br>Project 5<br>Project 6<br>Project 7<br>Project 8<br>Project 9<br>Project 10|30<br>30<br>20<br>15<br>15<br>15<br>15<br>24<br>18<br>18|12<br>4<br>4<br>0<br>0<br>12<br>4<br>4<br>3<br>4<br>4<br>4<br>10<br>0<br>0<br>0<br>0<br>11<br>0<br>0<br>0<br>0<br>12<br>0<br>0<br>0<br>0<br>13<br>8<br>8<br>0<br>0<br>0<br>0<br>10<br>0<br>0<br>0<br>0<br>10|



No partial investment is allowed in any of these projects. The firm has
18 million dollars available for investment each year.
(i) Formulate an integer linear program to determine the best investment
plan and solve with SOLVER.
(ii) Formulate the following conditions as linear constraints.


  - Exactly one of Projects 4, 5, 6, 7 must be invested in.

  - If Project 1 is invested in, then Project 2 cannot be invested in.

  - If Project 3 is invested in, then Project 4 must also be invested in.

  - If Project 8 is invested in, then either Project 9 or Project 10 must
also be invested in.


  - If either Project 1 or Project 2 is invested in, then neither Project 8
nor Project 9 can be invested in.


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 197

#### 11.3 Solving Mixed Integer Linear Programs


Historically, the first method developed for solving MILP’s was based on
cutting planes (adding constraints to the underlying linear program to cut off
noninteger solutions). This idea was proposed by Gomory in 1958. Branch
and bound was proposed in 1960 by Land and Dong. It is based on dividing
the problem into a number of smaller problems (branching) and evaluating
their quality based on solving the underlying linear programs (bounding).
Branch and bound has been the most effective technique for solving MILP’s
in the following forty years or so. However, in the last ten years, cutting
planes have made a resurgence and are now efficiently combined with branch
and bound into an overall procedure called branch and cut. This term was
coined by Padberg and Rinaldi in 1987. All these approaches involve solving
a series of linear programs. So that is where we begin.


11.3.1 Linear Programming Relaxation


Given a mixed integer linear program


(MILP) min c [T] x
Ax ≥ b
x ≥ 0
xj integer for j = 1, . . ., p


there is an associated linear program called the relaxation formed by dropping the integrality restrictions:


(R) min c [T] x
Ax ≥ b
x ≥ 0.

Since R is less constrained than MILP, the following are immediate:


  - The optimal objective value for R is less than or equal to the optimal
objective for MILP.


  - If R is infeasible, then so is MILP.

  - If the optimal solution x [∗] of R satisfies x [∗] j [integer for][ j] [= 1][, . . ., p][, then]
x [∗] is also optimal for MILP.


So solving R does give some information: it gives a bound on the optimal
value, and, if we are lucky, may give the optimal solution to MILP. However,
rounding the solution of R will not in general give the optimal solution of
MILP.


Exercise 11.3 Consider the problem


max 20x1 + 10x2 + 10x3
2x1 + 20x2 + 4x3 ≤ 15
6x1 + 20x2 + 4x3 = 20
x1, x2, x3 0 integer.
≥


198CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


Solve its linear programming relaxation. Then, show that it is impossible to
obtain a feasible integral solution by rounding the values of the variables.


Exercise 11.4 (a) Compare the feasible solutions of the three following
integer linear programs:


(i) max 14x1 + 8x2 + 6x3 + 6x4
28x1 + 15x2 + 13x3 + 12x4 ≤ 39
x1, x2, x3, x4 0, 1,
∈{ }


(ii) max 14x1 + 8x2 + 6x3 + 6x4
2x1 + x2 + x3 + x4 ≤ 2
x1, x2, x3, x4 0, 1,
∈{ }


(iii) max 14x1 + 8x2 + 6x3 + 6x4
x2 + x3 + x4 ≤ 2
x1 + x2 ≤ 1
x1 + x3 ≤ 1
x1 + x4 ≤ 1
x1, x2, x3, x4 0, 1 .
∈{ }


(b) Compare the relaxations of the above integer programs obtained by
replacing x1, x2, x3, x4 0, 1 by 0 xj 1 for j = 1, . . ., 4. Which is the
∈{ } ≤ ≤
best formulation among (i), (ii) and (iii) for obtaining a tight bound from
the linear programming relaxation?


11.3.2 Branch and Bound


An example:


We first explain branch and bound by solving the following pure integer
linear program (see Figure 11.1).


max x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1, x2 0
≥
x1, x2 integer.


The first step is to solve the linear programming relaxation obtained
by ignoring the last constraint. The solution is x1 = 1.5, x2 = 3.5 with
objective value 5. This is not a feasible solution to the integer program
since the values of the variables are fractional. How can we exclude this
solution while preserving the feasible integral solutions? One way is to
branch, creating two linear programs, say one with x1 1, the other with
≤
x1 2. Clearly, any solution to the integer program must be feasible to
≥
one or the other of these two problems. We will solve both of these linear
programs. Let us start with


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 199


x1



3.5



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-198-0.png)

1.5 x2



Figure 11.1: A two-variable integer program


max x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1 1
≤
x1, x2 0.
≥


The solution is x1 = 1, x2 = 3 with objective value 4. This is a feasible
integral solution. So we now have an upper bound of 5 as well as a lower
bound of 4 on the value of an optimum solution to the integer program.
Now we solve the second linear program


max x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1 2
≥
x1, x2 0.
≥


The solution is x1 = 2, x2 = 1.5 with objective value 3.5. Because this
value is worse that the lower bound of 4 that we already have, we do not
need any further branching. We conclude that the feasible integral solution
of value 4 found earlier is optimum.
The solution of the above integer program by branch and bound required
the solution of three linear programs. These problems can be arranged in a
branch-and-bound tree, see Figure 11.2. Each node of the tree corresponds
to one of the problems that were solved.
We can stop the enumeration at a node of the branch-and-bound tree
for three different reasons (when they occur, the node is said to be pruned).


  - Pruning by integrality occurs when the corresponding linear program
has an optimum solution that is integral.


200CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS






|x = 1.5, x = 3.5<br>1 2<br>z = 5<br>x ≤ 1 x ≥ 2<br>1 1<br>x = 1, x = 3 x = 2, x = 1.5<br>1 2 1 2<br>z = 4 z = 3.5|Col2|
|---|---|
|x1 = 1, x2 = 3<br>z = 4|x1 = 2, x2 = 1.5<br>z = 3.5|



Prune by integrality Prune by bounds


Figure 11.2: Branch-and-bound tree


  - Pruning by bounds occurs when the objective value of the linear program at that node is worse than the value of the best feasible solution
found so far.


  - Pruning by infeasibility occurs when the linear program at that node
is infeasible.


To illustrate a larger tree, let us solve the same integer program as above,
with a different objective function:


max 3x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1, x2 0
≥
x1, x2 integer.


The solution of the linear programming relaxation is x1 = 1.5, x2 =
3.5 with objective value 8. Branching on variable x1, we create two linear
programs. The one with the additional constraint x1 1 has solution
≤
x1 = 1, x2 = 3 with value 6 (so now we have an upper bound of 8 and a lower
bound of 6 on the value of an optimal solution of the integer program). The
linear program with the additional constraint x2 2 has solution x1 = 2,
≥
x2 = 1.5 and objective value 7.5. Note that the value of x2 is fractional, so
this solution is not feasible to the integer program. Since its objective value
is higher than 6 (the value of the best integer solution found so far), we need
to continue the search. Therefore we branch on variable x2. We create two
linear programs, one with the additional constraint x2 2, the other with
≥
x2 1, and we solve both. The first of these linear programs is infeasible.
≤
The second is


max 3x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1 2
≥
x2 1
≤
x1, x2 0.
≥


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 201


The solution is x1 = 2.125, x2 = 1 with objective value 7.375. Because
this value is greater than 6 and the solution is not integral, we need to
branch again on x1. The linear program with x1 3 is infeasible. The one
≥
with x1 2 is
≤

max 3x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1 2
≥
x2 1
≤
x1 2
≤
x1, x2 0.
≥

The solution is x1 = 2, x2 = 1 with objective value 7. This node is
pruned by integrality and the enumeration is complete. The optimal solution
is the one with value 7. See Figure 11.3.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-200-0.png)



















Prune by integrality



Prune



Figure 11.3: Branch-and-bound tree for modified example


The branch-and-bound algorithm:


Consider a mixed integer linear program


(MILP) zI = min c [T] x
Ax ≥ b
x ≥ 0
xj integer for j = 1, . . ., p.


202CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


The data are an n-vector c, an m × n matrix A, an m-vector b and an
integer p such that 1 ≤ p ≤ n. The set I = {1, . . ., p} indexes the integer
variables whereas the set C = {p + 1, . . ., n} indexes the continuous variables. The branch-and-bound algorithm keeps a list of linear programming
problems obtained by relaxing the integrality requirements on the variables
and imposing constraints such as xj uj or xj lj. Each such linear
≤ ≥
program corresponds to a node of the branch-and-bound tree. For a node
Ni, let zi denote the value of the corresponding linear program (it will be
convenient to denote this linear program by Ni as well). Let denote the
L
list of nodes that must still be solved (i.e. that have not been pruned nor
branched on). Let zU denote an upper bound on the optimum value zI (initially, the bound zU can be derived from a heuristic solution of (MILP), or
it can be set to +∞).



0. Initialize
= MILP, zU = +, x [∗] = .
L { } ∞ ∅



1. Terminate?
If L = ∅, the solution x [∗] is optimal.



2. Select node
Choose and delete a problem Ni from .
L



3. Bound
Solve Ni. If it is infeasible, go to Step 1. Else, let x [i] be its solution and
zi its objective value.

4. Prune
If zi zU, go to Step 1.
≥
If x [i] is not feasible to (MILP), go to Step 5.
If x [i] is feasible to (MILP), let zU = zi, x [∗] = x [i] and delete from all
L
problems with zj zU . Go to Step 1.
≥

5. Branch
¿From Ni, construct linear programs Ni [1][, . . ., N][ k] i [with] [smaller] [feasible]
regions whose union contains all the feasible solutions of (MILP) in Ni.
Add Ni [1][, . . ., N][ k] i [to] [L] [and] [go] [to] [Step] [1.]



4. Prune
If zi zU, go to Step 1.
≥
If x [i] is not feasible to (MILP), go to Step 5.
If x [i] is feasible to (MILP), let zU = zi, x [∗] = x [i] and delete from all
L
problems with zj zU . Go to Step 1.
≥



Various choices are left open by the algorithm, such as the node selection
criterion and the branching strategy. We will discuss some options for these
choices. Even more important to the success of branch-and-bound is the
ability to prune the tree (Step 4). This will occur when zU is a good upper
bound on zI and when zi is a good lower bound. For this reason, it is
crucial to have a formulation of (MILP) such that the value of its linear
programming relaxation zLP is as close as possible to zI. To summarize,
four issues need attention when solving MILP’s by branch and bound.


Formulation (so that the gap zI zLP is small).

  -  
Heuristics (to find a good upper bound zU ).

  
  - Branching.


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 203


  - Node selection.


We defer the formulation issue to Section 11.3.3 on cutting planes. This
issue will also be addressed in Chapter 12. Heuristics can be designed either
as stand alone (an example will be given in Section 12.3) or as part of
the branch-and-bound algorithm (by choosing branching and node selection
strategies that are more likely to produce feasible solutions x [i] to (MILP)
in Step 4). We discuss branching strategies first, followed by node selection
strategies and heuristics.


Branching
Problem Ni is a linear program. A way of dividing its feasible region is
to impose bounds on a variable. Let x [i] j [be] [one] [of] [the] [fractional] [values] [for]
j = 1, . . ., p, in the optimal solution x [i] of Ni (we know that there is such
a j, since otherwise Ni would have been pruned in Step 4 on account of x [i]

being feasible to (MILP)). ¿From problem Ni, we can construct two linear
programs Nij [−] [and] [N][ +] ij [that] [satisfy] [the] [requirements] [of] [Step] [5] [by] [adding]
the constraints xj ≤⌊x [i] j [⌋] [and] [x][j] [≥⌈][x] j [i] [⌉] [respectively] [to] [N][ i][.] [This] [is] [called]
branching on a variable. The advantage of branching on a variable is that
the number of constraints in the linear programs does not increase, since
linear programming solvers treat bounds on variables implicitly.
An important question is: On which variable xj should we branch, among
the j = 1, . . ., p such that x [i] j [is] [fractional?] To answer this question, it
would be very helpful to know the increase Dij [−] [in] [objective] [value] [between]
Ni and Nij [−][,] [and] [D] ij [+] [between] [N][i] [and] [N][ +] ij [.] [A] [good] [branching] [variable] [x][j]
at node N [i] is one for which both Dij [−] [and] [D] ij [+] [are] [relatively] [large] [(thus]
tightening the lower bound zi, which is useful for pruning). For example,
researchers have proposed to choose j = 1, . . ., p such that min(Dij [−][, D] ij [+][)] [is]
the largest. Others have proposed to choose j such that Dij [−] [+][ D] ij [+] [is] [the]
largest. Combining these two criteria is even better, with more weight on
the first.
The strategy which consists in computing Dij [−] [and] [D] ij [+] [explicitly] [for]
each j is called strong branching. It involves solving linear programs that
are small variations of Ni by performing dual simplex pivots (recall Section 2.4.5), for each j = 1, . . ., p such that x [i] j [is] [fractional] [and] [each] [of] [the]
two bounds. Experiments indicate that strong branching reduces the size
of the enumeration tree by a factor of 20 or more in most cases, relative to
a simple branching rule such as branching on the most fractional variable.
Thus there is a clear benefit to spending time on strong branching. But the
computing time of doing it at each node Ni, for every fractional variable x [i] j [,]
may be too high. A reasonable strategy is to restrict the j’s that are evaluated to those for which the fractional part of x [i] j [is] [closest] [to] [0.5] [so] [that] [the]
amount of computing time spent performing these evaluations is limited.
Significantly more time should be spent on these evaluations towards the
top of the tree. This leads to the notion of pseudocosts that are initialized
at the root node and then updated throughout the branch-and-bound tree.


204CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


Let fj [i] [=] [x][i] j [−⌊][x] j [i] [⌋] [be] [the] [fractional] [part] [of] [x][i] j [,] [for] [j] [=] [1][, . . . p][.] [For] [an]
index j such that fj [i] [>][ 0,] [define] [the] [down] [pseudocost] [and] [up] [pseudocost] [as]

Pj [−] [=] Dfjij [−][i] and Pj [+] [=] 1Dij [+] fj [i]
                     
respectively. Benichou et al [9] observed that the pseudocosts tend to remain fairly constant throughout the branch-and-bound tree. Therefore the
pseudocosts need not be computed at each node of the tree. They are estimated instead. How are they initialized and how are they updated in the
tree? A good way of initializing the pseudocosts is through strong branching
at the root node or other nodes of the tree when a variable becomes fractional for the first time. The down pseudocost Pj [−] is updated by averaging

the observations Dfjij [−][i] over all the nodes of the tree where xj was branched

on. Similarly for the up pseudocost Pj [+][.] [The] [decision] [of] [which] [variable]
to branch on at a node Ni of the tree is done as follows. The estimated
pseudocosts Pj [−] and Pj [+] are used to compute estimates of Dij [−] [and] [D] ij [+] [at]
node Ni, namely Dij [−] [=] [P][ −] j [f][ i] j [and] [D] ij [+] [=] [P][ +] j [(1][ −] [f][ i] j [)] [for] [each] [j] [=] [1][, . . ., p]
such that fj [i] [>] [0.] [Among] [these] [candidates,] [the] [branching] [variable] [x][j] [is]
chosen to be the one with largest min(Dij [−][, D] ij [+][)] [(or] [other] [criteria] [such] [as]
those mentioned earlier).


Node selection
How does one choose among the different problems Ni available in Step 2
of the algorithm? Two goals need to be considered: finding good feasible
solutions (thus decreasing the upper bound zU ) and proving optimality of
the current best feasible solution (by increasing the lower bound as quickly
as possible).
For the first goal, we estimate the value of the best feasible solution in
each node Ni. For example, we could use the following estimate:



Ei = zi +



�p

min(Pj [−][f][ i] j [, P][ +] j [(1][ −] [f][ i] j [))]
j=1



based on the pseudocosts defined above. This corresponds to rounding the
noninteger solution x [i] to a nearby integer solution and using the pseudocosts
to estimate the degradation in objective value. We then select a node Ni
with the smallest Ei. This is the so-called “best estimate criterion” node
selection strategy.
For the second goal, the best strategy depends on whether the first goal
has been achieved already. If we have a very good upper bound zU, it
is reasonable to adopt a depth-first search strategy. This is because the
linear programs encountered in a depth-first search are small variations of
one another. As a result they can be solved faster in sequence, using the
dual simplex method initialized with the optimal solution of the father node
(about 10 times faster, based on empirical evidence). On the other hand,
if no good upper bound is available, depth-first search is wasteful: it may


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 205


explore many nodes with a value zi that is larger than the optimum zI. This
can be avoided by using the “best bound” node selection strategy, which
consists in picking a node Ni with the smallest bound zi. Indeed, no matter
how good a solution of (MILP) is found in other nodes of the branch-andbound tree, the node with the smallest bound zi cannot be pruned by bounds
(assuming no ties) and therefore it will have to be explored eventually. So
we might as well explore it first. This strategy minimizes the total number
of nodes in the branch-and-bound tree.
The most successful node selection strategy may differ depending on the
application. For this reason, most MILP solvers have several node selection
strategies available as options. The default strategy is usually a combination of the “best estimate criterion” (or a variation) and depth-first search.
Specifically, the algorithm may dive using depth-first search until it reaches
an infeasible node Ni or it finds a feasible solution of (MILP). At this point,
the next node might be chosen using the “best estimate criterion” strategy,
and so on, alternating between dives in a depth-first search fashion to get
feasible solutions at the bottom of the tree and the “best estimate criterion”
to select the next most promising node.


Heuristics
Heuristics are useful for improving the bound zU, which helps in Step
4 for pruning by bounds. Of course, heuristics are even more important
when the branch-and-bound algorithm is too time consuming and has to be
terminated before completion, returning a solution of value zU without a
proof of its optimality.
We have already presented all the ingredients needed for a diving heuristic: Solve the linear programming relaxation, use strong branching or pseudocosts to determine a branching variable; then compute the estimate Ei
at each of the two sons and move down the branch corresponding to the
smallest of the two estimates. Solve the new linear programming relaxation
with this variable fixed and repeat until infeasibility is reached or a solution
of (MILP) is found. The diving heuristic can be repeated from a variety of
starting points (corresponding to different sets of variables being fixed) to
improve the chance of getting good solutions.
An interesting idea that has been proposed recently to improve a feasible
solution of (MILP) is called local branching [27]. This heuristic is particularly suited for MILP’s that are too large to solve to optimality, but where
the linear programming relaxation can be solved in reasonable time. For
simplicity, assume that all the integer variables are 0,1 valued. Let x¯ be a
feasible solution of (MILP) (found by a diving heuristic, for example). The
idea is to define a neighborhood of x¯ as follows:


�p

xj x¯j k
|                          - | ≤
j=1


where k is an integer chosen by the user (for example k = 20 seems to work
well), to add this constraint to (MILP) and apply your favorite MILP solver.
Instead of getting lost in a huge enumeration tree, the search is restricted to


206CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS



the neighborhood of x¯ by this constraint. Note that the constraint should
be linearized before adding it to the formulation, which is easy to do:

    -     



 - 
xj +
j∈I: x¯j =0 j∈I: x¯j



(1 xj) k.
     - ≤
j∈I: x¯j =1



If a better solution than x¯ is found, the neighborhood is redefined relatively
to this new solution, and the procedure is repeated until no better solution
can be found.


Exercise 11.5 Consider an investment problem as in Section 11.2. We have
$14,000 to invest among four different investment opportunities. Investment
1 requires an investment of $7,000 and has a net present value of $11,000;
investment 2 requires $5,000 and has a value of $8,000; investment 3 requires
$4,000 and has a value of $6,000; and investment 4 requires $3,000 and has
a value of $4,000. As in Section 11.2, these are “take it or leave it” opportunities and we are not allowed to invest partially in any of the projects. The
objective is to maximize our total value given the budget constraint. We do
not have any other (logical) constraints.
We formulate this problem as an integer program using 0–1 variables xj
for each investment. As before, xj is 1 if make investment j and 0 if we do
not. This leads to the following formulation:


Max 11x1 + 8x2 + 6x3 + 4x4
7x1 + 5x2 + 4x3 + 3x4 ≤ 14
xj = 0 or 1.


The linear relaxation solution is x1 = 1, x2 = 1, x3 = 0.5, x4 = 0 with a
value of 22. Since x3 is not integer, we do not have an integer solution yet.
Solve this problem using the branch-and-bound technique.


Exercise 11.6 Solve the 3 integer linear programs of Exercise 11.4 using
your favorite solver. In each case, report the number of nodes in the enumeration tree. Is it related to the tightness of the linear programming relaxtion
studied in Exercise 11.4 (b)?


Exercise 11.7 Modify the branch-and-bound algorithm so that it stops as
soon as it has a feasible solution that is guaranteed to be within p % of the
optimum.


11.3.3 Cutting Planes


In order to solve the mixed integer linear program


(MILP) min c [T] x
Ax ≥ b
x ≥ 0
xj integer for j = 1, . . ., p


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 207


a possible approach is to strengthen the linear programming relaxation


(R) min c [T] x
Ax ≥ b
x ≥ 0.

by adding valid inequalities for (MILP). When the optimal solution x [∗] of the
strengthened linear program is valid for (MILP), then x [∗] is also an optimal
solution of (MILP). Even when this does not occur, the strengthened linear
program may provide better lower bounds in the context of a branch-andbound algorithm. How do we generate valid inequalities for (MILP)?
Gomory [31] proposed the following approach. Consider nonnegative
variables xj for j I C, where xj must be integer valued for j I. We
∈ ∪ ∈
allow the possibility that C = ∅. Let

     -     



- 
ajxj +
j∈I j∈C



ajxj = b (11.1)
j∈C



be an equation satisfied by these variables. Assume that b is not an integer
and let f0 be its fractional part, i.e. b = b + f0 where 0 < f0 < 1. For
⌊ ⌋
j I, let aj = aj + fj where 0 fj < 1. Replacing in (11.1) and moving
∈ ⌊ ⌋ ≤
sums of integer products to the right, we get:

  -   -   



 - 
fjxj +
j∈I: fj ≤f0 j∈I: fj




 - 
(fj 1)xj +

    j∈I: fj >f0 j∈C



ajxj = k + f0
j∈C



where k is some integer.
Using the fact that k ≤−1 or k ≥ 0, we get the disjunction







1 fj
 


aj
xj 1
f0 ≥



j∈I: fj ≤f0



fj xj
f0 


j∈I: fj >f0



fj  
xj +
f0



j∈C



OR




 

j∈I: fj ≤f0



fj  xj +
1 f0
 - j∈I: fj >f0



1 fj  - xj
1 f0 
j C

 - ∈



aj
xj 1.
1 f0 ≥
 


This is of the form [�] j [a] j [1][x][j] [≥] [1 or][ �] j [a] j [2][x][j] [≥] [1 which implies][ �] [max(][a] j [1][, a][2] j [)][x][j] [≥]
1 for x ≥ 0.
Which is the largest of the two coefficients in our case? The answer
is easy since one coefficient is positive and the other is negative for each
variable.







aj xj
f0 


j∈C: aj <0



aj
xj 1.
1 f0 ≥
 


1 fj  - xj +
1 f0

j C: a

 - ∈



j∈C: aj >0



j∈I: fj ≤f0



fj xj +
f0



j∈I: fj >f0



(11.2)
Inequality (11.2) is valid for all x 0 that satisfy (11.1) with xj integer for
≥
all j ∈ I. It is called the Gomory mixed integer cut (GMI cut).


Let us illustrate the use of Gomory’s mixed integer cuts on the 2-variable
example of Figure 11.1. Recall that the corresponding integer program is


208CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


max z = x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
x1, x2 0
≥
x1, x2 integer.


We first add slack variables x3 and x4 to turn the inequality constraints into
equalities. The problem becomes:


z x1 x2 = 0

 - −x1 + x2 + x3 = 2
8x1 + 2x2 + x4 = 19
x1, x2, x3, x4 0
≥
x1, x2, x3, x4 integer.


Solving the linear programming relaxation by the simplex method (Section 2.4), we get the optimal tableau:


z + 0.6x3 + 0.2x4 = 5
x2 + 0.8x3 + 0.1x4 = 3.5
x1 − 0.2x3 + 0.1x4 = 1.5
x1, x2, x3, x4 0
≥

The corresponding basic solution is x3 = x4 = 0, x1 = 1.5, x2 = 3.5 and
z = 5. This solution is not integer. Let us generate the Gomory mixed
integer cut corresponding to the equation


x2 + 0.8x3 + 0.1x4 = 3.5


found in the final tableau. We have f0 = 0.5, f1 = f2 = 0, f3 = 0.8 and
f4 = 0.1. Applying formula (11.2), we get the GMI cut

1 − 0.8 [0][.][1] i.e. 2x3 + x4 5.
1 0.5 [x][3][ +] 0.5 [x][4] [≥] [1][,] ≥
       
We could also generate a GMI cut from the other equation in the final
tableau x1 0.2x3 + 0.1x4 = 1.5. It turns out that, in this case, we get

   exactly the same GMI cut. We leave it to the reader to verify this.
Since x3 = 2 + x1 x2 and x4 = 19 x1 2x2, we can express the above
          -          -          GMI cut in the space (x1, x2). This yields


3x1 + 2x2 ≤ 9.


Adding this cut to the linear programming relaxation, we get the following formulation (see Figure 11.4).


max x1 + x2
−x1 + x2 ≤ 2
8x1 + 2x2 ≤ 19
3x1 + 2x2 ≤ 9
x1, x2 0
≥


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 209


x1



3.5



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-208-0.png)



x2



1.5



Figure 11.4: Formulation strengthened by a cut


Solving this linear program by the simplex method, we find the basic
solution x1 = 1, x2 = 3 and z = 4. Since x1 and x2 are integer, this is the
optimal solution to the integer program.


Exercise 11.8 Consider the integer program


max 10x1 + 13x2
10x1 + 14x2 ≤ 43
x1, x2 0
≥
x1, x2 integer.


(i) Introduce slack variables and solve the linear programming relaxation
by the simplex method. (Hint: You should find the following optimal
tableau:


min x2 + x3
x1 + 1.4x2 + 0.1x3 = 4.3
x1, x2 0
≥


with basic solution x1 = 4.3, x2 = x3 = 0.)


(ii) Generate a GMI cut that cuts off this solution.


(iii) Multiply both sides of the equation x1 + 1.4x2 + 0.1x3 = 4.3 by the
constant k = 2 and generate the corresponding GMI cut. Repeat for
k = 3, 4 and 5. Compare the five GMI cuts that you found.


(iv) Add the GMI cut generated for k = 3 to the linear programming
relaxation. Solve the resulting linear program by the simplex method.
What is the optimum solution of the integer program?


210CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


Exercise 11.9 (a) Consider the 2-variable mixed integer set


S := (x, y) IN IR+ : x y b
{ ∈ ×              - ≤ }

where b IR. Let f0 = b b . Show that
∈ −⌊ ⌋

1
x y b
             - 1 f0 ≤⌊ ⌋
               
is a valid inequality for S.
(b) Consider the mixed integer set


S := (x, y) IN [n] IR [p] + [:][ a][T][ x][ −] [g][T][ y]
{ ∈ × [≤] [b][}]

where a IR [n], g IR [p] and b IR. Let f0 = b b and fj = aj aj .
∈ ∈ ∈ −⌊ ⌋ −⌊ ⌋
Show that



�n




[j] 1

[−] [f][0][)] )xj +

1 f0 1 f0
 - 


�n

( aj + [(][f][j] [−] [f][0][)][+]
⌊ ⌋ 1 f0
j=1





gjyj b
≤⌊ ⌋
j:gj <0



is a valid inequality for S.


11.3.4 Branch and Cut


The best software packages for solving MILPs use neither pure branch-andbound nor pure cutting plane algorithms. Instead they combine the two
approaches in a method called branch and cut. The basic structure is essentially the same as branch and bound. The main difference is that, when
a node Ni is explored, cuts may be generated to strengthen the formulation, thus improving the bound zi. Some cuts may be local (i.e. valid only
at node Ni and its descendants) or global (valid at all the nodes of the
branch-and-bound tree). Cplex and Xpress are two excellent commercial
branch-and-cut codes. cbc (COIN branch and cut) and bcp (branch, cut
and price) are open source codes in the COIN-OR library.
Below, we give an example of an enumeration tree obtained when running
the branch-and-cut algorithm of a commercial code on an instance with 89
binary variables and 28 constraints. Nodes of degree two (other than the
root) occur when one the sons can be pruned immediately by bounds or
infeasibility.


11.3. SOLVING MIXED INTEGER LINEAR PROGRAMS 211


Figure 11.5: A branch-and-cut enumeration tree



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-210-0.png)
212CHAPTER 11. INTEGER PROGRAMMING: THEORY AND ALGORITHMS


## Chapter 12

# Integer Programming Models: Constructing an Index Fund

This chapter presents several applications of integer linear programming:
combinatorial auctions, the lockbox problem and index funds. We also
present a model of integer quadratic programming: portfolio optimization
with minimum transaction levels.

#### 12.1 Combinatorial Auctions


In many auctions, the value that a bidder has for a set of items may not be
the sum of the values that he has for individual items. It may be more or it
may be less. Examples are equity trading, electricity markets, pollution right
auctions and auctions for airport landing slots. To take this into account,
combinatorial auctions allow the bidders to submit bids on combinations of
items.
Specifically, let M = {1, 2, . . ., m} be the set of items that the auctioneer
has to sell. A bid is a pair Bj = (Sj, pj) where Sj M is a nonempty set
⊆
of items and pj is the price offer for this set. Suppose that the auctioneer
has received n bids B1, B2, . . ., Bn. How should the auctioneer determine
the winners in order to maximize his revenue? This can be done by solving
an integer program. Let xj be a 0,1 variable that takes the value 1 if bid
Bj wins, and 0 if it looses. The auctioneer maximizes his revenue by solving
the integer program:



max




   subject to



�n

pjxj
i=1



xj 1 for i = 1, . . ., m
≤
j: i∈Sj



xj = 0 or 1 for j = 1, . . ., n.



The constraints impose that each item i is sold at most once.


213


214 CHAPTER 12. IP MODELS: CONSTRUCTING AN INDEX FUND


For example, if there are four items for sale and the following bids have
been received: B1 = ( 1, 6), B2 = ( 2, 3), B3 = ( 3, 4, 12), B4 =
{ } { } { }
( 1, 3, 12), B5 = ( 2, 4, 8), B6 = ( 1, 3, 4, 16), the winners can be de{ } { } { }
termined by the following integer program:



max 6x1 + 3x2 + 12x3 + 12x4 + 8x5 + 16x6
subject to x1 + x4 + x6 ≤ 1



x2 + x5 ≤ 1



x3 + x4 + x6 ≤ 1

x3 + x5 + x6 ≤ 1



xj = 0 or 1 for j = 1, . . ., 6.



In some auctions, there are multiple indistinguishable units of each item
for sale. A bid in this setting is defined as Bj = (λ [j] 1 [, λ][j] 2 [, . . ., λ] m [j] [;][ p][j][)] [where]
λ [j] i [is] [the] [desired] [number] [of] [units] [of] [item] [i] [and] [p][j] [is] [the] [price] [offer.] [The]
auctioneer maximizes his revenue by solving the integer program:



max




   subject to



�n

pjxj
i=1



λ [j] i [x][j] ui for i = 1, . . ., m
≤
j: i∈Sj



xj = 0 or 1 for j = 1, . . ., n.



where ui is the number of units of item i for sale.


Exercise 12.1 In a combinatorial exchange, both buyers and sellers can
submit combinatorial bids. Bids are like in the multiple item case, except
that the λ [j] i [values] [can] [be] [negative,] [as] [can] [the] [prices] [p][j][,] [representing] [selling]
instead of buying. Note that a single bid can be buying some items while
selling other items. Write an integer linear program that will maximize the
surplus generated by the combinatorial exchange.

#### 12.2 The Lockbox Problem


Consider a national firm that receives checks from all over the United States.
Due to the vagaries of the U.S. Postal Service, as well as the banking system,
there is a variable delay from when the check is postmarked (and hence the
customer has met her obligation) and when the check clears (and when the
firm can use the money). For instance, a check mailed in Pittsburgh sent to
a Pittsburgh address might clear in just 2 days. A similar check sent to Los
Angeles might take 4 days to clear. It is in the firm’s interest to have the
check clear as quickly as possible since then the firm can use the money. In
order to speed up this clearing process, firms open offices (called lockboxes)
in different cities to handle the checks.


12.2. THE LOCKBOX PROBLEM 215


For example, suppose we receive payments from 4 regions (West, Midwest, East, and South). The average daily value from each region is as
follows: $600,000 from the West, $240,000 from the Midwest, $720,000 from
the East, and $360,000 from the South. We are considering opening lockboxes in Los Angeles, Pittsburgh, Boston, and/or Houston. Operating a
lockbox costs $90,000 per year. The average days from mailing to clearing
is given in Table 12.1. Which lockboxes should we open?

|From|L.A. Pittsburgh Boston Houston|
|---|---|
|West<br>Midwest<br>East<br>South|2<br>4<br>6<br>6<br>4<br>2<br>5<br>5<br>6<br>5<br>2<br>5<br>7<br>5<br>6<br>3|



Table 12.1: Clearing Times


First we must calculate the lost interest for each possible assignment.
For example, if the West sends its checks to a lockbox in Boston, then on
average there will be $3,600,000 (= 6 × $600, 000) in process on any given
day. Assuming an investment rate of 5%, this corresponds to a yearly loss
of $180,000. We can calculate the losses for the other combinations in a
similar fashion to get Table 12.2.

|From|L.A. Pittsburgh Boston Houston|
|---|---|
|West<br>Midwest<br>East<br>South|60<br>120<br>180<br>180<br>48<br>24<br>60<br>60<br>216<br>180<br>72<br>180<br>126<br>90<br>108<br>54|



Table 12.2: Lost Interest (’000)


To formulate the problem as an integer linear program, we will use the
following variables. Let yj be a 0–1 variable that is 1 if lockbox j is opened
and 0 if it is not. Let xij be 1 if region i sends its checks to lockbox j.


The objective is to minimize total yearly costs:


60x11 + 120x12 + 180x13 + 180x14 + 48x21 + . . . + 90y1 + 90y2 + 90y3 + 90y4.


Each region must be assigned to one lockbox:


     
xij = 1 for all i.
j


The regions cannot send checks to closed lockboxes. For lockbox 1 (Los
Angeles), this can be written as:


x11 + x21 + x31 + x41 ≤ 4y1.


216 CHAPTER 12. IP MODELS: CONSTRUCTING AN INDEX FUND


Indeed, suppose that we do not open a lockbox in L.A. Then y1 is 0, so all of
x11, x21, x31, and x41 must also be. On the other hand, if we open a lockbox
in L.A., then y1 is 1 and there is no restriction on the x values.
We can create constraints for the other lockboxes to finish off the integer
program. For this problem, we would have 20 variables (4 y variables, 16 x
variables) and 8 constraints. This gives the following integer program:


MIN 60 X11 + 120 X12 + 180 X13 + 180 X14 + 48 X21
+ 24 X22 + 60 X23 + 60 X24 + 216 X31 + 180 X32
+ 72 X33 + 180 X34 + 126 X41 + 90 X42 + 108 X43
+ 54 X44 + 90 Y1 + 90 Y2 + 90 Y3 + 90 Y4
SUBJECT TO
X11 + X12 + X13 + X14 = 1
X21 + X22 + X23 + X24 = 1
X31 + X32 + X33 + X34 = 1
X41 + X42 + X43 + X44 = 1
X11 + X21 + X31 + X41      - 4 Y1 <= 0
X12 + X22 + X32 + X42      - 4 Y2 <= 0
X13 + X23 + X33 + X43      - 4 Y3 <= 0
X14 + X24 + X34 + X44      - 4 Y4 <= 0
ALL VARIABLES BINARY


If we ignore integrality, we get the solution x11 = x22 = x33 = x44 = 1,
y1 = y2 = y3 = y4 = 0.25 and the rest equals 0. Note that we get no useful
information out of this linear programming solution: all 4 regions look the
same.
The above is a perfectly reasonable 0–1 programming formulation of the
lockbox problem. There are other formulations, however. For instance,
consider the sixteen constraints of the form


xij yj.
≤

These constraints also force a region to only use open lockboxes. It might
seem that a larger formulation is less efficient and therefore should be
avoided. This is not the case! If we solve the linear program with the
above constraints, we get the solution x11 = x21 = x33 = x43 = y1 = y3 = 1
with the rest equal to zero. In fact, we have an integer solution, which must
therefore be optimal! Different integer programming formulations can have
very different properties with respect to their linear programming relaxations. As a general rule, one prefers an integer programming formulation
whose linear programming relaxation provides a tight bound.


Exercise 12.2 Consider a lockbox problem where cij is the cost of assigning
region i to a lockbox in region j, for j = 1, . . ., n. Suppose that we wish to
open exactly q lockboxes where q is a given integer, 1 ≤ q ≤ n.
(a) Formulate as an integer linear program the problem of opening q
lockboxes so as to minimize the total cost of assigning each region to an
open lockbox.


12.3. CONSTRUCTING AN INDEX FUND 217


(b) Formulate in two different ways the constraint that regions cannot
send checks to closed lockboxes.
(c) For the following data,



0 4 5 8 2
4 0 3 4 6
5 3 0 1 7
8 4 1 0 4
2 6 7 4 0















q = 2 and (cij) =















compare the linear programming relaxations of your two formulations in
question (b).

#### 12.3 Constructing an Index Fund


An old and recurring debate about investing lies in the merits of active versus passive management of a portfolio. Active portfolio management tries
to achieve superior performance by using technical and fundamental analysis as well as forecasting techniques. On the other hand, passive portfolio
management avoids any forecasting techniques and rather relies on diversification to achieve a desired performance. There are 2 types of passive
management strategies: “buy and hold” or “indexing”. In the first one,
assets are selected on the basis of some fundamental criteria and there is
no active selling or buying of these stocks afterwards (see the sections on
Dedication in Chapter 3 and Portfolio Optimization in Chapter 8). In the
second approach, absolutely no attempt is made to identify mispriced securities. The goal is to choose a portfolio that mirrors the movements of
a broad market population or a market index. Such a portfolio is called
an index fund. Given a target population of n stocks, one selects q stocks
(and their weights in the index fund), to represent the target population as
closely as possible.
In the last twenty years, an increasing number of investors, both large
and small, have established index funds. Simply defined, an index fund is a
portfolio designed to track the movement of the market as a whole or some
selected broad market segment. The rising popularity of index funds can be
justified both theoretically and empirically.


  - Market Efficiency: If the market is efficient, no superior risk-adjusted
returns can be achieved by stock picking strategies since the prices reflect all the information available in the marketplace. Additionally,
since the market portfolio provides the best possible return per unit
of risk, to the extent that it captures the efficiency of the market via
diversification, one may argue that the best theoretical approach to
fund management is to invest in an index fund.


  - Empirical Performance: Considerable empirical literature provides
strong evidence that, on average, money managers have consistently
underperformed the major indexes. In addition, studies show that, in


218 CHAPTER 12. IP MODELS: CONSTRUCTING AN INDEX FUND


most cases, top performing funds for a year are no longer amongst the
top performers in the following years, leaving room for the intervention
of luck as an explanation for good performance.


  - Transaction Cost: Actively managed funds incur transaction costs,
which reduce the overall performance of these funds. In addition,
active management implies significant research costs. Finally, fund
managers may have costly compensation packages that can be avoided
to a large extent with index funds.


Here we take the point of view of a fund manager who wants to construct
an index fund. Strategies for forming index funds involve choosing a broad
market index as a proxy for an entire market, e.g. the Standard and Poor list
of 500 stocks (S & P 500). A pure indexing approach consists in purchasing
all the issues in the index, with the same exact weights as in the index.
In most instances, this approach is impractical (many small positions) and
expensive (rebalancing costs may be incurred frequently). An index fund
with q stocks, where q is substantially smaller than the size n of the target
population seems desirable. We propose a large-scale deterministic model for
aggregating a broad market index of stocks into a smaller more manageable
index fund. This approach will not necessarily yield mean/variance efficient
portfolios but will produce a portfolio that closely replicates the underlying
market population.


12.3.1 A Large-Scale Deterministic Model


We present a model that clusters the assets into groups of similar assets
and selects one representative asset from each group to be included in the
index fund portfolio. The model is based on the following data, which we
will discuss in more detail later:


ρij = similarity between stock i and stock j.


For example, ρii = 1, ρij 1 for i = j and ρij is larger for more similar
≤
stocks. An example of this is the correlation between the returns of stocks
i and j. But one could choose other similarity indices ρij.



�n

ρijxij
j=1



(M ) Z = max


subject to



�n


i=1



�n

yj = q
j=1



�n

xij = 1 for i = 1, . . ., n
j=1



xij yj for i = 1, . . ., n; j = 1, . . ., n
≤

xij, yj = 0 or 1 for i = 1, . . ., n; j = 1, . . ., n.


12.3. CONSTRUCTING AN INDEX FUND 219


The variables yj describe which stocks j are in the index fund (yj = 1
if j is selected in the fund, 0 otherwise). For each stock i = 1, . . ., n, the
variable xij indicates which stock j in the index fund is most similar to i
(xij = 1 if j is the most similar stock in the index fund, 0 otherwise).
The first constraint selects q stocks in the fund. The second constraint
imposes that each stock i has exactly one representative stock j in the fund.
The third constraint guarantees that stock i can be represented by stock j
only if j is in the fund. The objective of the model maximizes the similarity
between the n stocks and their representatives in the fund.
Once the model has been solved and a set of q stocks has been selected
for the index fund, a weight wj is calculated for each j in the fund:



wj =



�n

Vixij
i=1



where Vi is the market value of stock i. So wj is the total market value of
the stocks “represented” by stock j in the fund. The fraction of the index
fund to be invested in stock j is proportional to the stock’s weight wj, i.e.


wj

~~�~~
n
f =1 [w][f]


Note that, instead of the objective function used in (M ), one could have
used an objective� function that takes the weights wj directly into account,
n
such as [�][n] i=1 j=1 [V][i][ρ][ij][x][ij][.] [The] [q] [stocks] [in] [the] [index] [fund] [found] [by] [this]
variation of Model (M ) would still need to be weighted as explained in the
previous paragraph.


Data Requirements


We need a coefficient ρij which measures the similarity between stocks
i and j. There are several ways of constructing meaningful coefficients ρij.
One approach is to consider the time series of stock prices over a calibration
period T and to compute the correlation between each pair of assets.


Testing the Model


Stocks comprising the S&P 500 were chosen as the target population
to test the model. A calibration period of sixty months was used. Then a
portfolio of 25 stocks was constructed using model (M ) and held for periods
ranging from three months to three years. The following table gives the ratio
of the population’s market value (normalized) to the index fund’s market
value. A perfect index fund would have a ratio equal unity.


Solution Strategy


Branch-and-bound is a natural candidate for solving model (M ). Note
however that the formulation is very large. Indeed, for the S&P 500, there
are 250,000 variables xij and 250,000 constraints xij yj. So the linear pro≤
gramming relaxation needed to get upper bounds in the branch-and-bound


220 CHAPTER 12. IP MODELS: CONSTRUCTING AN INDEX FUND

|Length|Ratio|
|---|---|
|1 QTR<br>2 QTR<br>1 YR<br>3 YR|1.006<br>.99<br>.985<br>.982|



Table 12.3: Performance of a 25 stock index fund


algorithm is a very large linear program to solve. It turns out, however, that
one does not need to solve this large linear program to obtain good upper
bounds. Cornu´ejols, Fisher and Nemhauser [22] proposed using the following Lagrangian relaxation, which is defined for any vector u = (u1, . . ., un):



�n



ρijxij +
j=1



�n



�n

xij)
j=1



L(u) = max


subject to



�n


i=1



yj = q
j=1



�n

ui(1
   i=1



xij yj for i = 1, . . ., n
≤
j = 1, . . ., n
xij, yj = 0 or 1 for i = 1, . . ., n
j = 1, . . ., n.


Property 1: L(u) ≥ Z, where Z is the maximum for model (M ).


Exercise 12.3 Prove Property 1.


The objective function L(u) may be equivalently stated as



�n

(ρij ui)xij +

  j=1



�n

ui.
i=1



�n


i=1



Let


and


Then


Property 2:



L(u) = max


(ρij ui) [+] =

 



(ρij ui) if ρij ui  - 0

  -   0 otherwise



Cj =



�n

(ρij ui) [+] .

  i=1



�n

ui
i=1



L(u) = max



�n

Cjyj +
j=1



subject to



�n

yj = q
j=1



yj = 0 or 1 for j = 1, . . ., n.


12.3. CONSTRUCTING AN INDEX FUND 221


Exercise 12.4 Prove Property 2.


Property 3: In an optimal solution of the Lagrangian relaxation, yj is
equal to 1 for the q largest values of Cj, and the remaining yj are equal to
0. Furthermore, if ρij ui - 0, then xij = yj and otherwise xij = 0.

      

Exercise 12.5 Prove Property 3.


Interestingly, the set of q stocks corresponding to the q largest values
of Cj can also be used as a heuristic solution for model (M ). Specifically,
construct an index fund containing these q stocks and assign each stock
i = 1, . . ., n to the most similar stock in this fund. This solution is feasible
to model (M ), although not necessarily optimal. This heuristic solution
provides a lower bound on the optimum value Z of model (M ). As previously
shown, L(u) provides an upper bound on Z. So for any vector u, we can
compute quickly both a lower bound and an upper bound on the optimum
value of (M ). To improve the upper bound L(u), we would like to solve the
nonlinear problem
min L(u).


How does one minimize L(u)? Since L(u) is nondifferentiable and convex,
one can use the subgradient method (see Section 5.6). At each iteration,
a revised set of Lagrange multipliers u and an accompanying lower bound
and upper bound to model (M ) are computed. The algorithm terminates
when these two bounds match or when a maximum number of iterations
is reached (It is proved in [22] that min L(u) is equal to the value of the
linear programming relaxation of (M ). In general, min L(u) is not equal to
Z, and therefore it is not possible to match the upper and lower bounds).
If one wants to solve the integer program (M ) to optimality, one can use a
branch-and-bound algorithm, using the upper bound min L(u) for pruning
the nodes.


12.3.2 A Linear Programming Model


In this section, we consider a different approach to constructing an index
fund. It can be particularly useful as one tries to rebalance the portfolio at
minimum cost. This approach assumes that we have identified important
characteristics of the market index to be tracked. Such characteristics might
be the fraction fi of the index in each sector i, the fraction of companies with
market capitalization in various ranges (small, medium, large), the fraction
of companies that pay no dividends, the fraction in each region etc. Let us
assume that there are m such characteristics that we would like our index
fund to track as well as possible. Let aij = 1 if company j has characteristic
i and 0 if it does not.
Let xj denote the optimum weight of asset j in the portfolio. Assume
that initially, the portfolio has weights x [0] j [.] [Let][ y][j] [denote the fraction of asset]


222 CHAPTER 12. IP MODELS: CONSTRUCTING AN INDEX FUND


j bought and zj the fraction sold. The problem of rebalancing the portfolio
at minimum cost is the following:



min



�n

(yj + zj)
j=1



subject to
�n

aijxj = fi for i = 1, . . ., m
j=1

�n

xj = 1
j=1



xj x [0] j for j = 1, . . ., n

 - [≤] [y][j]

x [0] j for j = 1, . . ., n

[−] [x][j] [≤] [z][j]

yj 0 for j = 1, . . ., n
≥

zj 0 for j = 1, . . ., n
≥

xj 0 for j = 1, . . ., n.
≥


#### 12.4 Portfolio Optimization with Minimum Trans- action Levels

When solving the classical Markowitz model, the optimal portfolio often
contains positions xi that are too small to execute. In practice, one would
like a solution of
minx 21 [x][T][ Qx]
µ [T] x R
≥ (12.1)
Ax = b
Cx ≥ d.

with the additional property that


xj               - 0 xj lj (12.2)
⇒ ≥

where lj are given minimum transaction levels. This constraint states that,
if an investment is made in a stock, then it must be “large enough”, for
example at least 100 shares. Because the constraint (12.2) is not a simple
linear constraint, it cannot be handled directly by quadratic programming.
This problem is considered by Bienstock [11]. He also considers the
portfolio optimization problem where there is an upper bound on the number
of positive variables, that is


xj         - 0 for at most K distinct j = 1, . . ., n. (12.3)


Requirement (12.2) can easily be incorporated within a branch-andbound algorithm: First solve the basic Markowitz model (12.1) using the
usual algorithm (see Chapter 7). Let x [∗] be the optimal solution found. If no
minimum transaction level constraint (12.2) is violated by x [∗], then x [∗] is also


12.5. EXERCISES 223


optimum to (12.1)-(12.2) and we can stop. Otherwise, let j be an index for
which (12.2) is violated by x [∗] . Form two subproblems, one obtained from
(12.1) by adding the constraint xj = 0, and the other obtained from (12.1)
by adding the constraint xj lj. Both are quadratic programs that can
≥
be solved using the usual algorithms of Chapter 7. Now we check whether
the optimum solutions to these two problems satisfy the transaction level
constraint (12.2). If a solution violates (12.2) for index k, the corresponding
problem is further divided by adding the constraint xk = 0 on one side and
xk lk on the other. A branch-and-bound tree is expanded in this way.
≥
The constraint (12.3) is a little more tricky to handle. Assume that there
is a given upper bound uj on how much can be invested in stock j. That
is, we assume that constraints xj uj are part of the formulation (12.1).
≤
Then, clearly, constraint (12.3) implies the weaker constraint






j



xj
K. (12.4)
uj ≤



We add this constraint to (12.1) and solve the resulting quadratic program.
Let x [∗] be the optimal solution found. If x [∗] satisfies (12.3), it is optimum to
(12.1)-(12.3) and we can stop. Otherwise, let k be an index for which xk - 0.
Form two subproblems, one obtained from (12.1) by adding the constraint
xk = 0 (down branch), and the other obtained from (12.1) by adding the
xj
constraint [�] j=k uj [(up] [branch).] [The] [branch-and-bound] [tree] [is]
developped recursively. [≤] [K] When [−] [1] a set T of variables has been branched up,
the constraint added to the basic model (12.1) becomes






j̸∈T



xj
K T .
uj ≤ −| |


#### 12.5 Exercises

Exercise 12.6 You have $ 250,000 to invest in the following possible investments. The cash inflows/outflows are as follows:

|Col1|Year 1 Year 2 Year 3 Year 4|
|---|---|
|Investment 1<br>Investment 2<br>Investment 3<br>Investment 4<br>Investment 5|−1.00<br>1.18<br>−1.00<br>1.22<br>−1.00<br>1.10<br>−1.00<br>0.14<br>0.14<br>1.00<br>−1.00<br>0.20<br>1.00|



For example, if you invest one dollar in Investment 1 at the beginning of
Year 1, you receive $ 1.18 at the beginning of Year 3. If you invest in any
of these investments, the required minimum level is $ 100,000 in each case.
Any or all the available funds at the beginning of a year can be placed in a
money market account that yields 3 % per year. Formulate a mixed integer
linear program to maximize the amount of money available at the beginning
of Year 4. Solve the integer program using your favorite solver.


224 CHAPTER 12. IP MODELS: CONSTRUCTING AN INDEX FUND


Exercise 12.7 You currently own a portfolio of eight stocks. Using the
Markowitz model, you computed the optimal mean/variance portfolio. The
weights of these two portfolios are shown in the following table:


You would like to rebalance your portfolio in order to be closer to the
M/V portfolio. To avoid excessively high transaction costs, you decide to
rebalance only three stocks from your portfolio. Let xi denote the weight
of stock i in your rebalanced portfolio. The objective is to minimize the
quantity


x1 0.02 + x2 0.05 + x3 0.25 + . . . + x8 0.12
|        - | |        - | |        - | |        - |

which measures how closely the rebalanced portfolio matches the M/V portfolio.
Formulate this problem as a mixed integer linear program. Note that
you will need to introduce new continuous variables in order to linearize the
absolute values and new binary variables in order to impose the constraint
that only three stocks are traded.

#### 12.6 Case Study


The purpose of this project is to construct an index fund that will track a
given segment of the market. First, choose a segment of the market and
discuss the collection of data. Compare different approaches for computing
an index fund: Model (M) solved as a large integer program, Lagrangian
relaxations and the subgradient approach, the linear programming approach
of Section 12.3.2, or others. The index fund should be computed using an
in-sample period and evaluated on an out-of-sample period.


## Chapter 13

# Dynamic Programming Methods

#### 13.1 Introduction

Decisions must often be made in a sequential manner when the information
used for these decisions is revealed through time. In that case, decisions
made at an earlier time may affect the feasibility and performance of later
decisions. In such environments, myopic decisions that try to optimize only
the impact of the current decision are usually suboptimal for the overall
process. To find optimal strategies one must consider current and future decisions simultaneously. These types of multi-stage decision problems are the
typical settings where one employs dynamic programming, or DP. Dynamic
programming is a term used both for the modeling methodology and the solution approaches developed to solve sequential decision problems. In some
cases the sequential nature of the decision process is obvious and natural,
in other cases one reinterprets the original problem as a sequential decision
problem. We will consider examples of both types below.
Dynamic programming models and methods are based on Bellman’s
Principle of Optimality, namely that for overall optimality in a sequential
decision process, all the remaining decisions after reaching a particular state
must be optimal with respect to that state. In other words, if a strategy
for a sequential decision problem makes a sub-optimal decision in any one
of the intermediate stages, it cannot be optimal for the overall problem.
This principle allows one to formulate recursive relationships between the
optimal strategies of successive decision stages and these relationships form
the backbone of DP algorithms.
Common elements of DP models include decision stages, a set of possible
states in each stage, transitions from states in one stage to states in the next,
value functions that measure the best possible objective values that can be
achieved starting from each state, and finally the recursive relationships
between value functions of different states. For each state in each stage, the
decision maker needs to specify a decision she would make if she were to reach
that state and the collection of all decisions associated with all states form
the policy or strategy of the decision maker. Transitions from the states of a


225


226 CHAPTER 13. DYNAMIC PROGRAMMING METHODS


given stage to those of the next may happen as a result of the actions of the
decision-maker, as a result of random external events, or a combination of
the two. If a decision at a particular state uniquely determines the transition
state, the DP is a deterministic DP. If probabilistic events also affect the
transition state, then one has a stochastic DP. We will discuss each one of
these terms below.
Dynamic programming models are pervasive in the financial literature.
The best-known and most common examples are the tree or lattice models
(binomial, trinomial, etc.) used to describe the evolution of security prices,
interest rates, volatilities, etc. and the corresponding pricing and hedging
schemes. We will discuss several such examples in the next chapter. Here,
we focus on the fundamentals of the dynamic programming approach and
for this purpose, it is best to start with an example.
We consider a capital budgeting problem. A manager has $ 4 million to
allocate to different projects in three different regions where her company
operates. In each region, there are a number of possible projects to consider
with estimated costs and projected profits. Let us denote the costs with cj’s
and profits with pj’s. The following table lists the information for possible
project options; both the costs and the profits are given in millions of dollars.

|Project|Region 1<br>c p<br>1 1|Region 2<br>c p<br>2 2|Region 3<br>c p<br>3 3|
|---|---|---|---|
|1<br>2<br>3<br>4|0<br>0<br>1<br>2<br>2<br>4<br>4<br>10|0<br>0<br>1<br>3<br>3<br>9<br>—<br>—|0<br>0<br>1<br>2<br>2<br>5<br>—<br>—|



Table 13.1: Project costs and profits


Note that the projects in the first row with zero costs and profits correspond to the option of doing nothing in that particular region. The manager’s objective is to maximize the total profits from projects financed in all
regions. She will choose only one project from each region.
One may be tempted to approach this problem using integer programming techniques we discussed in the previous two chapters. Indeed, since
there is a one-to-one correspondence between the projects available at each
region and their costs, letting xi denote the investment amount in region
i, we can formulate an integer programming problem with the following
constraints:


x1 + x2 + x3 ≤ 4

x1 0, 1, 2, 4, x2 0, 1, 3, x3 0, 1, 2 .
∈{ } ∈{ } ∈{ }


The problem with this approach is, the profits are not linear functions of
the variables xi. For example, for region 3, while the last project costs twice
as much as the the second one, the expected profits from this last project
is only two and half times that of the second project. To avoid formulating
a nonlinear integer programming problem which can be quite difficult, one


13.1. INTRODUCTION 227


might consider a formulation that uses a binary variable for each project
in each region. For example, we can use binary decision variables xij to
represent whether project j in region i is to be financed. This results in an
integer linear program but with many more variables.
Another strategy we can consider is total enumeration of all investment
possibilities. We have 4 choices for the first region, and 3 choices for each of
the second and third regions. Therefore, we would end up with 4×3×3 = 36
possibilities to consider. We can denote these possibilities with (x1, x2, x3)
where, for example, (2, 3, 1) corresponds to the choices of the second, the
third and the first projects in regions 1, 2, and 3, respectively. We could
evaluate each of these possibilities and then pick the best one. There are
obvious problems with this approach, as well.
First of all, for larger problems with many regions and/or many options in each region, the total number of options we need to consider will
grow very quickly and become computationally prohibitive. Further, many
of the combinations are not feasible with respect to the constraints of the
problem. In our example, choosing the third project in each region would
require 2 + 3 + 2 = 7 million dollars, which is above the $4 million budget,
and therefore is an infeasible option. In fact, only 21 of the 36 possibilities
are feasible in our example. In an enumeration scheme, such infeasibilities
will not be detected in advance leading to inefficiencies. Finally, an enumeration scheme does not take advantage of the information generated during
the investigation of other alternatives. For example, after discovering that
(3, 3, 1) is an infeasible option, we should no longer consider the more expensive (3, 3, 2) or (3, 3, 3). Unfortunately, the total enumeration scheme will
not take advantage of such simple deductions.
We will approach this problem using the dynamic programming methodology. For this purpose, we will represent our problem in a graph. The
construction of this graph representation is not necessary for the solution
procedure; it is provided here for didactic purposes. We will use the root
node of the graph to correspond to stage 0 with $4 million to invest and use
the pair (0,4) to denote this node. In stage 1 we will consider investment
possibilities in region 1. In stage 2, we will consider investment possibilities
in regions 1 and 2, and finally in stage 3 we will consider all three regions.
Throughout the graph, nodes will be denoted by pairs (i, j) where i represents the stage and j represents the particular state of that stage. States
in stage i will correspond to the different amounts of money left after some
projects are already funded in regions 1 through i. For example, the node
(2,3) in stage 2 of the graph represents the state of having $3 million left for
investment after funding projects in regions 1 and 2.
The branches in the graphical representation correspond to the projects
undertaken in a particular region. Say we are at node (i, j) meaning that
we have already considered regions 1 to i and have j million dollars left
for investment. Then, the branch corresponding to project k in the next
region will take us to the node (i + 1, j [′] ) where j [′] equals j minus the cost of
project k. For example, starting from node (1,3), the branch corresponding
to project 2 in the second region will take us to node (2,2). For each one


228 CHAPTER 13. DYNAMIC PROGRAMMING METHODS


of these branches, we will use the expected profit from the corresponding
project as the weight of the branch. The resulting graph is shown in Figure
13.1. Now the manager’s problem is to find the largest weight path from
node (0,4) to a third stage node.









![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-227-0.png)









































0 1 2 3 Periods


Figure 13.1: Graphical representation of the 3-region capital budgeting problem


At this point, we can proceed in two alternative ways: using either a
backward or a forward progression on the graph. In the backward mode,
we first identify the largest weight path from each one of the nodes in stage
2 to a third stage node. Then using this information and the Principle of
Optimality, we will determine the largest weight paths from each of the
nodes in stage 1 to a third stage node, and finally from node (0,4) to a third
stage node. In contrast, the forward mode will first determine the largest
weight path from (0,4) to all first stage nodes, then to all second stage nodes
and finally to all third stage nodes. We illustrate the backward method first
and then the forward method.


Exercise 13.1 Formulate an integer linear program for the capital budgeting problem with project costs and profits given in Table 13.1.


13.1.1 Backward Recursion


For each state, or node, we keep track of the largest profit that can be
collected starting from that state. These quantities form what we will call
the value function associated with each state. For the backward approach,
we start with stage 3 nodes. Since we are assuming that any money that
is not invested in regions 1 through 3 will generate no profits, the value
function for each one of the stage 3 states is zero and there are no decisions
associated with these states.
Next, we identify the largest weight paths from each one of the second
stage nodes to the third stage nodes. It is clear that for nodes (2,4), (2,3),
and (2,2) the best alternative is to choose project 3 of the third region and


13.1. INTRODUCTION 229


collect an expected profit of $5 million. Since node (2,1) corresponds to the
state where there is only $1 million left for investment, the best alternative
from the third region is project 2, with the expected profit of $2 million. For
node (2,0), the only alternative is project 1 (“do nothing”) with no profit.
We illustrate these choices in Figure 13.2.







![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-228-0.png)



















2 3


Figure 13.2: Optimal allocations from stage 2 nodes


For each node, we indicated the value function associated with that node
in a box on top of the node label in Figure 13.2. Next, we determine the
value function and optimal decisions for each one of the first stage nodes.
These computations are slightly more involved, but still straightforward. Let
us start with node (1,4). From Figure 13.1 we see that one can reach the
third stage nodes via one of (2,4), (2,3), and (2,1). The maximum expected
profit on the paths through (2,4) is 0+5=5, the sum of the profit on the
arc from (1,4) to (2,4), which is zero, and the largest profit from (2,4) to a
period 3 node. Similarly, we compute the maximum expected profit on the
paths through (2,3) and (2,1) to be 3+5=8, and 9+2=11. The maximum
profit from (1,4) to a stage three node is then


max{0 + v(2, 4), 3 + v(2, 3), 9 + v(2, 1)} = {0 + 5, 3 + 5, 9 + 2} = 11

which is achieved by following the path (1, 4) → (2, 1) → (3, 0). After
performing similar computations for all period 1 nodes we obtain the node
values and optimal branches given in Figure 13.3.
Finally, we need to compute the best allocations from node (0,4) by
comparing the profits along the branches to first stage nodes and the best
possible profits starting from those first period nodes. To be exact, we
compute


max{0+v(1, 4), 2+v(1, 3), 4+v(1, 2), 10+v(1, 0)} = {0+11, 2+9, 4+5, 10+0} = 11.


Therefore, the optimal expected profit is $11 million and is achieved on
either of the two alternative paths (0, 4) → (1, 4) → (2, 1) → (3, 0) and
(0, 4) → (1, 3) → (2, 0) → (3, 0). These paths correspond to the selections
of project 1 in region 1, project 3 in region 2, and project 2 in region 3 in


230 CHAPTER 13. DYNAMIC PROGRAMMING METHODS





![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-229-0.png)





















1



2



Figure 13.3: Optimal allocations from stage 1 nodes


the first case, and project 2 in region 1, project 3 in region 2, and project 1
in region 3 in the second case. Figure 13.4 summarizes the whole process.
The optimal paths are shown using thicker lines.







![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-229-1.png)





1































0



2 3



Figure 13.4: Optimal paths from (0,4) to (3,0)


Exercise 13.2 Construct a graphical representation of a 5-region capital
budgeting problem with the project costs and profits given in Table 13.2.
Exactly one project must be chosen in each region and there is a total budget
of 10. Solve by backward recursion.

|Project|Region 1<br>c p<br>1 1|Region 2<br>c p<br>2 2|Region 3<br>c p<br>3 3|Region 4<br>c p<br>4 4|Region 5<br>c p<br>5 5|
|---|---|---|---|---|---|
|1<br>2<br>3|1<br>8<br>2<br>15<br>3<br>25|3<br>20<br>2<br>14<br>1<br>7|2<br>15<br>4<br>26<br>5<br>40|0<br>3<br>1<br>10<br>3<br>25|1<br>6<br>2<br>15<br>3<br>22|



Table 13.2: Project costs and profits


13.1. INTRODUCTION 231


13.1.2 Forward Recursion


Next, we explore the “forward” method. In this case, in the first step we
will identify the best paths from (0, 4) to all nodes in stage 1, then best
paths from (0, 4) to all stage 2 nodes, and finally to stage 3 nodes. The first
step is easy since there is only one way to get from node (0, 4) to each one
of the stage 1 nodes, and hence all these paths are optimal. Similar to the
backward method, we will keep track of a value function for each node. For
node (i, j), its value function will represent the highest total expected profit
we can collect from investments in regions 1 through i if we want to have $j
million left for future investment. For (0, 4) the value function is zero and
for all stage 1 nodes, they are equal to the weight of the tree branch that
connects (0, 4) and the corresponding node.





![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-230-0.png)

1



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-230-1.png)









2









0 1



Figure 13.5: Optimal paths between stage 0, stage 1 and stage 2 nodes


For most of the second stage nodes, there are multiple paths from (0, 4)
to that corresponding node and we need to determine the best option. For
example, let us consider the node (2, 2). One can reach (2, 2) from (0, 4)
either via (1, 3) or (1, 2). The value function at (2, 2) is the maximum of
the following two quantities: The sum of the value function at (1, 3) and the
weight of the branch from (1, 3) to (2, 2), and, the sum of the value function
at (1, 2) and the weight of the branch from (1, 2) to (2, 2):


v(2, 2) = max{v(1, 3) + 3, v(1, 2) + 0} = max{2 + 3, 4 + 0} = 5.

After similar calculations we identify the value function at all stage 2 nodes
and the corresponding optimal branches one must follow. The results are
shown on the right side of Figure 13.5.
Finally, we perform similar calculations for stage 3 nodes. For example,
we can calculate the value function at (3, 0) as follows:


v(3, 0) = max{v(2, 2)+5, v(2, 1)+2, v(2, 0)+0} = {5+5, 9+2, 11+0} = 11.

Optimal paths for all nodes are depicted in Figure 13.6. Note that there are
three alternative optimal ways to reach node (3, 2) from (0, 4).


232 CHAPTER 13. DYNAMIC PROGRAMMING METHODS



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-231-0.png)

2









































3



0 1



Figure 13.6: Optimal paths from (0,4) to all nodes


Clearly, both the forward and the backward method identified the two
alternative optimal paths between (0, 4) and (3, 0). However, the additional
information generated by these two methods differ. In particular, studying
Figures 13.4 and 13.6, we observe that while the backward method produces
the optimal paths from each node in the tree to the final stage nodes, in
contrast, the forward method produces the optimal paths from the initial
stage node to all nodes in the tree. There may be situations where one
prefers to have one set of information above the other and this preference
dictates which method to use. For example, if for some reason the actual
transition state happens to be different from the one intended by an optimal
decision, it would be important to know what to do when in a state that is
not on the optimal path. In that case, the paths generated by the backward
method would have the answer.


Exercise 13.3 Solve the capital budgeting problem of Exercise 13.2 by forward recursion.

#### 13.2 Abstraction of the Dynamic Programming Ap- proach


Before proceeding with additional examples, we study the common characteristics of dynamic programming models and methods. In particular, we
will identify the aspects of the example considered in the previous section
that qualified our approach as dynamic programming.
We already mentioned the sequential nature of the decision-making process as the most important ingredient of a DP problem. Every DP model
starts with the identification of stages that correspond to the order of the
decisions to be made. There is an initial stage (for a forward recursion)
or final stage (for a backward recursion) for which the optimal decisions


13.2. ABSTRACTION OF THE DYNAMIC PROGRAMMING APPROACH233


are immediately or easily available and do not depend on decisions of other
stages. In our example in Section 13.1, the number of regions considered for
different project options constituted the stages of our formulation. Stage 0
was the initial stage and stage 3 the final stage.
Each stage consists of a number of possible states. In allocation problems, states are typically used to represent the possible levels of availability
for scarce resources in each stage. In financial binomial lattice models, states
may correspond to spot prices of assets.
In many cases, the set of states in each particular stage is finite or at
least, discrete. Such DPs are categorized as discrete DPs in contrast to
continuous DPs that may have a continuum of states in each stage. In the
example of Section 13.1, the states represented the amount of money still
available for investment at the end of that particular stage. For consistency
with our earlier example, we continue to denote states of a DP formulation
with the pair (i, j) where i specifies the stage and j specifies the particular
state in that stage.
A DP formulation must also specify a decision set for each one of the
states. As with states, decision sets may be discrete or continuous. In
our example in Section 13.1, the decision sets were formed from the set of
possible projects in each stage. Because of feasibility considerations, decision
sets are not necessarily identical for all states in a given stage. For example,
while the decision set consists of region 2 projects 1, 2, and 3 for state (1, 4),
the decision set for state (1, 0) is the singleton corresponding to project 1
(do nothing). We denote the decision set associated with state (i, j) with
S(i, j).
In a deterministic DP, a choice d made from the decision set S(i, j)
uniquely determines what state one transitions to. We call this state the
transition state associated with the particular state (i, j) and decision d ∈
S(i, j) and use the notation T ((i, j), d) to denote this state. Furthermore,
there is a cost (or benefit, for a maximization problem) associated with each
transition that we indicate with c ((i, j), d). In our example in the previous
section, from state (2, 1), we can either transition to state (3, 1) by choosing
project 1 with an associated profit of 0, or to state (3, 0) by choosing project
2 with an associated profit of 2.
In our example above, all the transition states from a given state were
among the states of the next stage. Although this is common, it is not required. All that is necessary for the DP method to function is that all the
transition states from a given state are in the later stages whose computations are already completed. So, for example, in a five stage formulation,
transition states of a state in stage 2 can be in any one of stages 3, 4, and 5.
A value function keeps track of the costs (or benefits) accumulated optimally from the initial stage up to a particular state (in the forward method)
or from a particular state to the final stage (in the backward method). Each
such quantity will be called the value of the corresponding state. We use
the notation v(i, j) to denote the value of the state (i, j).
The Principle of Optimality implies a recursive relationship between the
values of states in consecutive stages. For example, in the backward method,


234 CHAPTER 13. DYNAMIC PROGRAMMING METHODS


to compute the optimal decision at and the value of a particular state, all
we need to do is to compare the following quantity for each transition state
of that state: the value of the transition state plus the cost of transitioning
to that state. Namely, we do the following computation:


v(i, j) = min [((][i, j][)][, d][)) +][ c][ ((][i, j][)][, d][)][}][.] (13.1)
d (i,j) [{][v][ (][T]
∈S

In a benefit maximization problem as in our example in the previous section,
the values would be the benefits rather than costs and the min in (13.1) would
be replaced by a max. Equation (13.1) is known as the Bellman equation and
is a discrete-time deterministic special case of the Hamilton-Jacobi-Bellman
(HJB) equation often encountered in optimal control texts.
To illustrate the definitions above and equation (13.1), let us explicitly
perform one of the calculations of the example in the previous section. Say,
in the backward method we have already calculated the values of the states
in stage 2 (5, 5, 5, 2, and 0, for states (2,4), (2,3), (2,2), (2,1), and (2,0),
respectively) and we intend to compute the value of the state (1,3). We first
identify the decision set for (1,3): S(1, 3) = {1, 2, 3}, i.e., projects 1, 2, and
3. The corresponding transition states are easily determined:


T ((1, 3), 1) = (2, 3), T ((1, 3), 2) = (2, 2), T ((1, 3), 3) = (2, 0).


The associated benefits (or expected profits, in this case) are


c ((1, 3), 1) = 0, c ((1, 3), 2) = 3, c ((1, 3), 3) = 9.


Now we can derive the value of state (1,3):



v(1, 3) = max [((1][,][ 3)][, d][)) +][ c][ ((1][,][ 3)][, d][)][}]
d (1,3) [{][v][ (][T]
∈S



= max{v (T ((1, 3), 1)) + c ((1, 3), 1), v (T ((1, 3), 2)) + c ((1, 3), 2),



. . . v (T ((1, 3), 3)) + c ((1, 3), 3)}



= max{v(2, 3) + 0, v(2, 2) + 3, v(2, 0) + 9}



= max{5 + 0, 5 + 3, 0 + 9} = 9,



and the corresponding optimal decision at (1,3) is project 3. Note that for
us to be able to compute the values recursively as above, we must be able
to compute the values at the final stage without any recursion.
If a given optimization problem can be formulated with the ingredients
and properties outlined above, we can solve it using dynamic programming
methods. Most often, finding the right formulation of a given problem, and
specifying the stages, states, transitions, and recursions in a way that fits
the framework above is the most challenging task in the dynamic programming approach. Even when a problem admits a DP formulation, there may
be several alternative ways to do this (see, for example, Section 13.3) and
it may not be clear which of these formulations would produce the quickest
computational scheme. Developing the best formulations for a given optimization problem must be regarded as a form of art and in our opinion,
is best learned through examples. We continue in the next section with a
canonical example of both integer and dynamic programming.


13.3. THE KNAPSACK PROBLEM. 235

#### 13.3 The Knapsack Problem.


A traveler has a knapsack that she plans to take along for an expedition.
Each item she would like to take with her in the knapsack has a given size
and a value associated with the benefit the traveler receives by carrying that
item. Given that the knapsack has a fixed and finite capacity, how many of
each of these items should she put in the knapsack to maximize the total
value of the items in the knapsack? This is the well-known and well-studied
integer program called the knapsack problem. It has the special property
that it only has a single constraint other than the nonnegative integrality
condition on the variables.
We recall the investment problem considered in Exercise 11.5 in Chapter
11 which is an instance of the knapsack problem. We have $14,000 to invest
among four different investment opportunities. Investment 1 requires an
investment of $7,000 and has a net present value of $11,000; investment 2
requires $5,000 and has a value of $8,000; investment 3 requires $4,000 and
has a value of $6,000; and investment 4 requires $3,000 and has a value of
$4,000.
As we discussed in Chapter 11, this problem can be formulated and
solved as an integer program, say using the branch and bound method.
Here, we will formulate it using the DP approach. To make things a bit
more interesting, we will allow the possibility of multiple investments in the
same investment opportunity. The effect of this modification is that the
variables are now general integer variables rather than 0–1 binary variables
and therefore the problem


Max 11x1 + 8x2 + 6x3 + 4x4
7x1 + 5x2 + 4x3 + 3x4 ≤ 14
xj 0 an integer, j
≥ ∀

is an instance of the knapsack problem. We will consider two alternative
DP formulations of this problem. For future reference, let yj and pj denote
the cost and the net present value of investment j (in thousands of dollars),
respectively, for j = 1 to 4.


13.3.1 Dynamic Programming Formulation


One way to approach this problem using the dynamic programming methodology is by considering the following question that already suggests a recursion: If I already know how to allocate i thousand dollars to the investment
options optimally for all i = 1, . . ., k − 1, can I determine how to optimally
allocate k thousand dollars to these investment option? The answer to this
question is yes, and building the recursion equation is straightforward.
The first element of our DP construction is the determination of the
stages. The question in the previous paragraph suggests the use of stages
0, 1, . . ., up to 14, where stage i corresponds to the decisions that need to
be made with j thousand dollars left to invest. Note that we need only one
state per stage and therefore can denote stages/states using the single index
i. The decision set at state j is the set of investments we can afford with the


236 CHAPTER 13. DYNAMIC PROGRAMMING METHODS


j thousand dollars we have left for investment. That is, (i) = d : yd i .
S { ≤ }
The transition state is given by T (i, d) = i yd and the benefit associated
                   with the transition is c(i, d) = pd. Therefore, the recursion for the value
function is given by the following equation:


v(i) = max
d:yd≤i [{][v][(][i][ −] [y][d][) +][ p][d][}][.]

Note that S(i) = ∅ and v(i) = 0 for i = 0, 1, and 2 in our example.


Exercise 13.4 Using the recursion given above, determine v(i) for all i
from 0 to 14 and the corresponding optimal decisions.


13.3.2 An Alternative Formulation


As we discussed in Section 13.2, dynamic programming formulation of a
given optimization problem need not be unique. Often, there exists alternative ways of defining the stages, states, and obtaining recursions. Here we
develop an alternative formulation of our investment problem by choosing
stages to correspond to each one of the investment possibilities.
So, we will have four stages, i = 1, 2, 3, and 4. For each stage i, we
will have states j corresponding to the total investment in opportunities i
through 4. So, for example, in the fourth stage we will have states (4,0),
(4,3), (4,6), (4,9), and (4,12), corresponding to 0, 1, 2, 3, and 4 investments
in the fourth opportunity.
The decision to be made at stage i is the number of times one invests in
the investment opportunity i. Therefore, for state (i, j), the decision set is
given by

(i, j) = d [j] d, d non-negative integer .
S { | yi ≥ }


The transition states are given by T ((i, j), d) = (i +1, j yid) and the value
                         function recursion is:


v(i, j) = max
d (i,j) [{][v][(][i][ + 1][, j][ −] [y][i][d][) +][ p][i][d][}][.]
∈S


Finally, note that v(4, 3k) = 4k for k = 0, 1,2,3, and 4.


Exercise 13.5 Using the DP formulation given above, determine v(0, 14)
and the corresponding optimal decisions. Compare your results with the
optimal decisions from Exercise 13.4.


Exercise 13.6 Formulate a dynamic programming recursion for the following shortest path problem. City O (the origin) is in Stage 0, one can go from
any city i in Stage k − 1 to any city j in Stage k for k = 1, . . . N . The distance between such cities i and j is denoted by dij. City D (the destination)
is in Stage N . The goal is to find a shortest path from the origin O to the
destination D.


13.4. STOCHASTIC DYNAMIC PROGRAMMING 237

#### 13.4 Stochastic Dynamic Programming


So far, we have only considered dynamic programming models that are deterministic, meaning that given a particular state and a decision from its
decision set, the transition state is known and unique. This is not always the
case for optimization problems involving uncertainty. Consider a blackjack
player trying to maximize his earnings by choosing a strategy or a commuter
trying to minimize her commute time by picking the roads to take. Suppose
the blackjack player currently holds 12 (his current “state”) and asks for
another card (his “decision”). His next state may be a “win” if he gets a
9, a “lose” if he gets a 10, or “15 (and keep playing)” if he gets a 3. The
state he ends up in depends on the card he receives, which is beyond his
control. Similarly, the commuter may choose Road 1 over Road 2, but her
actual commute time will depend on the current level of congestion on the
road she picks, a quantity beyond her control.
Stochastic dynamic programming addresses optimization problems with
uncertainty. The DP methodology we discussed above must be modified to
incorporate uncertainty. This is done by allowing multiple transition states
for a given state and decision. Each one of the possible transition states is
assigned a probability associated with the likelihood of the corresponding
state being reached when a certain decision is made. Since the costs are not
certain anymore, the value function calculations and optimal decisions will
be based on expected values.
We have the following formalization: Stages and states are defined as
before, and a decision set associated with each state. Given a state (i, j) and
d ∈S(i, j), a random event will determine the transition state. We denote
with R ((i, j), d) the set of possible outcomes of the random event when we
make decision d at state (i, j). For each possible outcome r ∈R ((i, j), d) we
denote the likelihood of that outcome with p ((i, j), d, r). We observe that
the probabilities p ((i, j), d, r) must be nonnegative and satisfy

   
p ((i, j), d, r) = 1, ∀(i, j) and ∀d ∈S(i, j).
r∈R((i,j),d)


When we make decision d at state (i, j) and when the random outcome
r is realized, we transition to the state T ((i, j), d, r) and the cost (or benefit) associated with this transition is denoted by c ((i, j), d, r). The value
function v(i, j) computes expected value of the costs accumulated and must
satisfy the following recursion:



p ((i, j), d, r) [v (T ((i, j), d, r)) + c ((i, j), d, r)]
r∈R((i,j),d)



(13.2))]
 [.]








v(i, j) = min
d∈S(i,j)















As before, in a benefit maximization problem, the min in (13.2) must be
replaced by a max.
In some problems, the uncertainty is only in the transition costs and not
in the transition states. Such problems can be handled in our notation above
by letting R ((i, j), d) correspond to the possible outcomes for the cost of


238 CHAPTER 13. DYNAMIC PROGRAMMING METHODS


the transition. The transition state is independent from the random event,
that is T ((i, j), d, r1) = T ((i, j), d, r2) for all r1, r2 ((i, j), d). The cost
∈R
function c ((i, j), d, r) reflects the uncertainty in the problem.


Exercise 13.7 Recall the investment problem we discussed in Section 13.3.
We have $14,000 to invest in four different options which cost yj thousand
dollars for j = 1 to 4. Here we introduce the element of uncertainty to
the problem. While the cost of investment j is fixed at yj (all quantities
in thousands of dollars), its net present value is uncertain because of the
uncertainty of future cash-flows and interest rates. We believe that the net
present value of investment j has a discrete uniform distribution in the set
pj 2, pj 1, pj, pj +1, pj +2 . We want to invest in these investment options
{ - - }
in order to maximize the expected net present value of our investments.
Develop a stochastic DP formulation of this problem and solve it using the
recursion (13.2).


## Chapter 14

# DP Models: Option Pricing

The most common use of dynamic programming models and principles in
financial mathematics is through the lattice models. The binomial lattice has
become an indispensable tool for pricing and hedging of derivative securities.
We study the binomial lattice in Section 14.2 below. Before we do that,
however, we will show how the dynamic programming principles lead to
optimal exercise decisions in a more general model than the binomial lattice.

#### 14.1 A Model for American Options


For a given stock, let Sk denote its price on day k. We can write


Sk = Sk 1 + Xk

              

where Xk is the change in price from day k 1 to day k. The random walk
                   model for stock prices assumes that the random variables Xk are independent
and identically distributed, and are also independent of the known initial
price S0. We will also assume that the distribution F of Xk has a finite
mean µ.
Now consider an American call option on this stock: Purchasing such
an option entitles us to buy the stock at a fixed price c on any day between
today (let us call it day 0) and day N, when the option expires. We do
not have to ever exercise the option, but if we do at a time when the stock
price is S, then our profit is S - c. What exercise strategy maximizes our
expected profit? We assume that the interest rate is zero throughout the
life of the option for simplicity.
Let v(k, S) denote the maximum expected profit when the stock price is
S and the option has k additional days before expiration. In our dynamic
programming terminology, the stages are k = 0, 1, 2, . . ., N and the state
in each stage is S, the current stock price. Note that stage 0 corresponds
to day N and vice versa. In contrast to the DP examples we considered in
the previous chapter, we do not assume that the state space is finite in this
model. That is, we are considering a continuous DP here, not a discrete
DP. The decision set for each state has two elements, namely “exercise”
or “do not exercise”. The “exercise” decision takes one to the transition


239


240 CHAPTER 14. DP MODELS: OPTION PRICING


state “option exercised” which should be placed at stage N for convenience.
The immediate benefit from the “exercise” decision is S − c. If we “do not
exercise” the option in stage k, we hold the option for at least one more
period and observe the random shock x to the stock price which takes us to
state S + x in stage k − 1.
Given this formulation, our value function v(k, S) satisfies the following
recursion: v(k, S) = max{S − c, v(k − 1, S + x)dF (x)}

with the boundary condition


v(0, S) = max{S − c, 0}.

For the case that we are considering (American call options), there is
no closed form formula for v(k, S). However dynamic programming can be
used to compute a numerical solution. In the remainder of this section, we
use the recursion formula to derive the structure of the optimal policy.


Exercise 14.1 Using induction on k, show that v(k, S) - S is a nonincreasing function of S.


Solution The fact that v(0, S) − S is a nonincreasing function of S follows
from the definition of v(0, S). Assume now v(k - 1, S) - S is a nonincreasing
function of S. Using the recursion equation, we get




            v(k, S) − S = max{−c, (v(k − 1, S + x) − S) dF (x)}




      -      = max{−c, (v(k − 1, S + x) − (S + x)) dF (x) + xdF (x)}




        = max{−c, µ + (v(k − 1, S + x) − (S + x)) dF (x)},




          recalling that µ = xdF (x) denotes the expected value of the random variable x representing daily shocks to the stock price.
For any x, the function v(k  - 1, S + x)  - (S + x) is a nonincreasing
function of S, by the induction hypothesis. It follows that v(k, S) − S is a
nonincreasing function of S. End of solution.



Theorem 14.1 The optimal policy for an American call option has the
following form:
There are nondecreasing numbers s1 s2 . . . sk . . . sN such that,
≤ ≤ ≤ ≤
if the current stock price is S and there are k days until expiration, then one
should exercise the option if and only if S sk.
≥

Proof:
It follows from the recursion equation that if v(k, S) ≤ S - c, then it is
optimal to exercise the option when the stock price is S and there remain
k days until expiration. Indeed this yields v(k, S) = S - c, which is the
maximum possible under the above assumption. Define


sk = min S : v(k, S) = S c .
{              - }


14.2. BINOMIAL LATTICE 241


If no S satisfies v(k, S) = S c, then sk is defined as + . From the exercise
             - ∞
above, it follows that


v(k, S) S v(k, sk) sk = c
             - ≤             -             
for any s sk since v(k, S) S is nonincreasing. Therefore it is optimal to
≥    exercise the option with k days to expiration whenever S sk. Since v(k, S)
≥
is nondecreasing in k, it immediately follows that sk is also nondecreasing
in k, i.e., s1 s2 . . . sk . . . sN .
≤ ≤ ≤ ≤


A consequence of the above result is that, when µ  - 0, it is always
optimal to wait until the maturity date to exercise an American call option.
The optimal policy described above becomes nontrivial when µ < 0 however.


Exercise 14.2 A put option is an agreement to sell an asset for a fixed
price c (the strike price). An American put option can be exercised at any
time up to the maturity date. Prove a Theorem similar to Theorem 14.1
for American put options. Can you deduce that it is optimal to wait until
maturity to exercise a put option when µ > 0?

#### 14.2 Binomial Lattice


If we want to buy or sell an option on an asset (whether a call or a put, an
American, European, or another type of option), it is important to determine the fair value of the option today. Determining this fair value is called
option pricing. The option price depends on the structure of the movements
in the price of the underlying asset using information such as the volatility
of the underlying asset, the current value of the asset, the dividends if any,
the strike price, the time to maturity and the riskless interest rate. Several approaches can be used to determine the option price. One popular
approach uses dynamic programming on a binomial lattice that models the
price movements of the underlying asset. Our discussion here is based on
the work of Cox, Ross, and Rubinstein [23].
In the binomial lattice model, a basic period length is used, such as a
day or a week. If the price of the asset is S in a period, the asset price
can only take two values in the next period. Usually, these two possibilities
are represented as uS and dS where u - 1 and d < 1 are multiplicative
factors (u stands for up and d for down). The probabilities assigned to
these possibilities are p and 1 − p respectively, where 0 < p < 1. This can
be represented on a lattice (see Figure 14.1).
After several periods, the asset price can take many different values.
Starting from price S0 in period 0, the price in period k is u [j] d [k][−][j] S0 if there
are j up moves and k j down moves. The probability of an up move is

                             -                             p whereas that of a down − move is 1 p and there are kj possible paths to
                reach the corresponding node. Therefore the probability that the price is

             -              u [j] d [k][−][j] S0 in period k is kj pj(1 p)k−j. This is the binomial distribution.
              As k increases, this distribution converges to the normal distribution.


242 CHAPTER 14. DP MODELS: OPTION PRICING


u [3] S



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-241-0.png)











0 1 2 3 Period


Figure 14.1: Asset price in the binomial lattice model


14.2.1 Specifying the parameters



To specify the model completely, one needs to choose values for u, d and p.
This is done by matching the mean and volatility of the asset price to the
mean and volatility of the above binomial distribution. Because the model
is multiplicative (the price S of the asset being either uS or dS in the next
period), it is convenient to work with logarithms.
Let Sk denote the asset price in periods k = 0, . . ., n. Let µ and σ be the
mean and volatility of ln(Sn/S0) (we assume that this information about the
asset is known). Let ∆= [1] [denote] [the] [length] [between] [co][ns][ecutive] [periods.]



asset is known). Let ∆= n [denote] [the] [length] [between] [co][ns][ecutive] [periods.]

Then the mean and volatility of ln(S1/S0) are µ∆and σ ~~√~~ ∆respectively. In



Then the mean and volatility of ln(S1/S0) are µ∆and σ ∆respectively. In

the binomial lattice, we get by direct computation that the mean and variance of ln(S1/S0) are p ln u+(1 p) ln d and p(1 p)(ln u ln d) [2] respectively.

         -         -         Matching these values we get two equations:



p ln u + (1 − p) ln d = µ∆

p(1 − p)(ln u − ln d) [2] = σ [2] ∆.



Note that there are three parameters but only two equations, so we can set
d = 1/u as in [23]. Then the equations simplify to



(2p − 1) ln u = µ∆



4p(1 − p)(ln u) [2] = σ [2] ∆.



Squaring the first and adding it to the second, we get (ln u) [2] = σ [2] ∆+(µ∆) [2] .
This yields



√
u = e



σ [2] ∆+(µ∆) [2]



d = e [−] ~~[√]~~



σ [2] ∆+(µ∆) [2]



1 1
p = ~~�~~ ).
2 [(1 +] σ [2]
1 +
µ [2] ∆


14.2. BINOMIAL LATTICE 243


When ∆is small, these values can be approximated as



~~√~~
u = e [σ]



∆



~~√~~
d = e [−][σ]



∆



p = 1 [µ]
2 [(1 +] σ



σ



~~√~~ ∆).



As an example, consider a binomial model with 52 periods of a week
each. Consider a stock with current known price S0 and random price S52 a
year from today. We are given the mean µ and volatility σ of ln(S52/S0), say
µ = 10% and σ = 30%. What are the parameters u, d and p of the binomial
lattice? Since ∆= 1 [small,] [we] [can] [use] [the] [second] [set] [of] [formulas:]
52 [is]



~~√~~
u = e [0][.][30][/]



52 = 0.9592



52 = 1.0425 and d = e [−][0][.][30][/] ~~√~~




[1] 0.10

2 [(1 +] 0.30 ~~√~~



p = [1]



52 [) = 0][.][523]



14.2.2 Option Pricing


Using the binomial lattice described above for the price process of the underlying asset, the value of an option on this asset can be computed by dynamic
programming, using backward recursion, working from the maturity date T
(period n) back to period 0 (the current period). The stages of the dynamic
program are the periods k = 0, . . ., N and the states are the nodes of the
lattice in a given period. Thus there are k + 1 states in stage k, which we
label j = 0, . . ., k. The nodes in stage N are called the terminal nodes.
¿From a nonterminal node j, we can go either to node j + 1 (up move) or
to node j (down move) in the next stage. So, to reach node j at stage k we
must make exactly j up moves, and k − j down moves between stage 0 and
stage k.
We denote by v(k, j) the value of the option in node j of stage k. The
value of the option at time 0 is then given by v(0, 0). This is the quantity
we have to compute in order to solve the option pricing problem.
The option values at maturity are simply given by the payoff formulas,
i.e., max(S − c, 0) for call options and max(c - S, 0) for put options, where c
denotes the strike price and S is the asset price at maturity. Recall that, in
our binomial lattice after N time steps, the asset price in node j is u [j] d [N] [−][j] S0.
Therefore the option values in the terminal nodes are:


v(N, j) = max(u [j] d [N] [−][j] S0 c, 0) for call options,
                
v(N, j) = max(c u [j] d [N] [−][j] S0, 0) for put options.
             
We can compute v(k, j) knowing v(k + 1, j) and v(k + 1, j + 1). Recall
(Section 4.1.1) that this is done using the risk neutral probabilities




[R][ −] [d] and pd = [u][ −] [R]

u − d u − d



pu = [R][ −] [d]



u d [.]
 

244 CHAPTER 14. DP MODELS: OPTION PRICING


where R = 1 + r and r is the one-period return on the risk-free asset. For
European options, the value of fk(j) is

v(k, j) = [1]

R [(][p][u][v][(][k][ + 1][, j][ + 1) +][ p][d][v][(][k][ + 1][, j][))][ .]


For an American call option, we have

v(k, j) = max [1]
{ R [(][p][u][v][(][k][ + 1][, j][ + 1) +][ p][d][v][(][k][ + 1][, j][))][, u][j][d][k][−][j][S][0][ −] [c][}]


and for an American put option, we have

v(k, j) = max [1]
{ R [(][p][u][v][(][k][ + 1][, j][ + 1) +][ p][d][v][(][k][ + 1][, j][))][, c][ −] [u][j][d][k][−][j][S][0][}][.]


Let us illustrate the approach. We wish to compute the value of an
American put option on a stock. The current stock price is $100. The
strike price is $98 and the expiration date is 4 weeks from today. The yearly
volatility of the logarithm of the stock return is σ = 0.30. The risk-free
interest rate is 4 %.



0


0


0


5.99


13.33



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-243-0.png)





















0 1 2 3 4 Period


Figure 14.2: Put option pricing in a binomial lattice


We consider a binomial lattice with N = 4; see Figure 14.2. To get an
accurate answer one would need to take a much larger value of N . Here the
purpose is just to illustrate the dynamic programming recursion and N = 4
will suffice for this purpose. We recall the values of u and d computed in
the previous section:


u = 1.0425 and d = 0.9592


14.2. BINOMIAL LATTICE 245


In period N = 4, the stock price in node j is given by u [j] d [4][−][j] S0 = 1.0425 [j] 0.9592 [4][−][j] 100
and therefore the put option payoff is given by:


v(4, j) = max(98 − 1.0425 [j] 0.9592 [4][−][j] 100, 0).


That is v(4, 0) = 13.33, v(4, 1) = 5.99 and v(4, 2) = v(4, 3) = v(4, 4) = 0.
Next, we compute the stock price in period k = 3. The one-period return
on the risk-free asset is r = [0][.][04] [and] [thus] [R][ = 1][.][00077.]

52 [= 0][.][00077]
Accordingly, the risk neutral probabilities are



pu = [1][.][00077][ −] [0][.][9592]




[.][00077][ −] [0][.][9592]

[and] [p][d] [=] [1][.][0425][ −] [1][.][00077]
1.0425 − 0.9592 [= 0][.][499][,] 1.0425 − 0.9592



1.0425 0.9592 [= 0][.][501][.]
   


We deduce that, in period 3, the stock price in node j is


1
v(3, j) = max
{ 1.00077 [(0][.][499][v][(4][, j][+1)+0][.][501][v][(4][, j][))][,][ 98][−][1][.][0425][j][0][.][9592][3][−][j][100][}][.]

That is v(3, 0) = max{9.67, 9.74} = 9.74 (as a side remark, note that it is
optimal to exercise the American option before its expiration in this case),
v(3, 1) = max{3.00, 2.08} = $ 3.00 and v(3, 2) = v(3, 3) = 0. Continuing
the computations going backward, we compute v(2, j) for j = 0, 1, 2, then
v(1, j) for j = 0, 1 and finally v(0, 0). See Figure 14.2. The option price is
v(0, 0) = $ 2.35.
Note that the approach we outlined above can be used with various types
of derivative securities with payoff functions that may make other types of
analysis difficult.


Exercise 14.3 Compute the value of an American put option on a stock
with current price equal to $ 100, strike price equal to $ 98 and expiration
date 5 weeks from today. The yearly volatility of the logarithm of the stock
return is σ = 0.30. The risk-free interest rate is 4%. Use a binomial lattice
with N = 5.


Exercise 14.4 Compute the value of an American call option on a stock
with current price equal to $ 100, strike price equal to $ 102 and expiration
date 4 weeks from today. The yearly volatility of the logarithm of the stock
return is σ = 0.30. The risk-free interest rate is 4%. Use a binomial lattice
with N = 4.


Exercise 14.5 Computational exercise: Repeat Exercises 14.3 and 14.4 using a binimial lattice with N = 1000.


246 CHAPTER 14. DP MODELS: OPTION PRICING


## Chapter 15

# DP Models: Structuring Asset Backed Securities

The structuring of collateralized mortgage obligations will give us an opportunity to apply the dynamic programming approach studied in Chapter
13.
Mortgages represent the largest single sector of the US debt market,
surpassing even the federal government. In 2000, there were over $5 trillion
in outstanding mortgages. Because of the enormous volume of mortgages
and the importance of housing in the US economy, numerous mechanisms
have been developed to facilitate the provision of credit to this sector. The
predominant method by which this has been accomplished since 1970 is securitization, the bundling of individual mortgage loans into capital market
instruments. In 2000, $2.3 trillion of mortgage-backed securities were outstanding, an amount comparable to the $2.1 trillion corporate bond market
and $3.4 trillion market in federal government securities.
A mortgage-backed security (MBS) is a bond backed by a pool of mortgage loans. Principal and interest payments received from the underlying
loans are passed through to the bondholders. These securities contain at
least one type of embedded option due to the right of the home buyer to
prepay the mortgage loan before maturity. Mortgage payers may prepay for
a variety of reasons. By far the most important factor is the level of interest
rates. As interest rates fall, those who have fixed rate mortgages tend to
repay their mortgages faster.
MBS were first packaged using the pass-through structure. The passthrough’s essential characteristic is that investors receive a pro rata share
of the cash flows that are generated by the pool of mortgages - interest,
scheduled amortization and principal prepayments. Exercise of mortgage
prepayment options has pro rata effects on all investors. The pass-through
allows banks that initiate mortgages to take their fees up front, and sell
the mortgages to investors. One troublesome feature of the pass-through
for investors is that the timing and level of the cash flows are uncertain.
Depending on the interest rate environment, mortgage holders may prepay
substantial portions of their mortgage in order to refinance at lower interest
rates.


247


248CHAPTER 15. DP MODELS: STRUCTURING ASSET BACKED SECURITIES


A collateralized mortgage obligation (CMO) is a more sophisticated
MBS. The CMO rearranges the cash flows to make them more predictable.
This feature makes CMO’s more desirable to investors. The basic idea behind a CMO is to restructure the cash-flows from an underlying mortgage
collateral (pool of mortgage loans) into a set of bonds with different maturities. These two or more series of bonds (called “tranches”) receive sequential,
rather than pro rata, principal pay down. Interest payments are made on
all tranches (except possibly the last tranche, called Z tranche or “accrual”
tranche). A two tranche CMO is a simple example. Assume that there is
$100 in mortgage loans backing two $50 tranches, say tranche A and tranche
B. Initially, both tranches receive interest, but principal payments are used
to pay down only the A tranche. For example, if $1 in mortgage scheduled
amortization and prepayments is collected in the first month, the balance
of the A tranche is reduced (paid down) by $1. No principal is paid on the
B tranche until the A tranche is fully retired, i.e. $50 in principal payments
have been made. Then the remaining $50 in mortgage principal pays down
the $50 B tranche. In effect, the A or “fast-pay” tranche has been assigned all
of the early mortgage principal payments (amortization and prepayments)
and reaches its maturity sooner than would an ordinary pass-through security. The B or “slow-pay” tranche has only the later principal payments and
it begins paying down much later than an ordinary pass-through security.
By repackaging the collateral cash-flow in this manner, the life and risk
characteristics of the collateral are restructured. The fast-pay tranches are
guaranteed to be retired first, implying that their lives will be less uncertain,
although not completely fixed. Even the slow-pay tranches will have less
cash-flow uncertainty than the underlying collateral. Therefore the CMO
allows the issuer to target different investor groups more directly than when
issuing pass-through securities. The low maturity (fast-pay) tranches may
be appealing to investors with short horizons while the long maturity bonds
(slow-pay) may be attractive to pension funds and life insurance companies.
Each group can find a bond which is better customized to their particular
needs.
A by-product of improving the predictability of the cash flows is being
able to structure tranches of different credit quality from the same mortgage
pool. With the payments of a very large pool of mortgages dedicated to the
“fast-pay” tranche, it can be structured to receive a AAA credit rating even
if there is a significant default risk on part of the mortgage pool. This high
credit rating lowers the interest rate that must be paid on this slice of the
CMO. While the credit rating for the early tranches can be very high, the
credit quality for later tranches will necessarily be lower because there is
less principal left to be repaid and therefore there is increased default risk
on slow-pay tranches.
We will take the perspective of an issuer of CMO’s. How many tranches
should be issued? Which sizes? Which coupon rates? Issuers make money
by issuing CMO’s because they can pay interest on the tranches that is lower
than the interest payments being made by mortgage holders in the pool. The
mortgage holders pay 10 or 30-year interest rates on the entire outstanding


15.1. DATA 249


principal, while some tranches only pay 2, 4, 6 and 8-year interest rates plus
an appropriate spread.
The convention in mortgage markets is to price bonds with respect to
their weighted average life (WAL), which is much like duration, i.e.



WAL =



�T

tPt
t=1

�T

Pt
t=1



where Pt is the principal payment in period t (t = 1, . . ., T ).
A bond with a WAL of 3 years will be priced at the 3 year treasury
rate plus a spread, while a bond with a WAL of 7 years will be priced at
the 7 year treasury rate plus a spread. The WAL of the CMO collateral is
typically high, implying a high rate for (normal) upward sloping rate curves.
By splitting the collateral into several tranches, some with a low WAL and
some with a high WAL, lower rates are obtained on the fast-pay tranches
while higher rates result for the slow-pay. Overall, the issuer ends up with
a better (lower) average rate on the CMO than on the collateral.

#### 15.1 Data


When issuing a CMO, several restrictions apply. First it must be demonstrated that the collateral can service the payments on the issued CMO
tranches under several scenarios. These scenarios are well defined and standardized, and cover conditional prepayment models (see below) as well as
the two extreme cases of full immediate prepayment and no prepayment at
all. Second, the tranches are priced using their expected WAL. For example,
a tranche with a WAL between 2.95 and 3.44 will be priced at the 3-year
Treasury rate plus a spread that depends on the tranche’s rating. For a
AAA rating, the spread might be 1% whereas for a BB rating, the spread
might be 2%.
The following table contains the payment schedule for a $100 Million pool
of 10-year mortgages with 10 % interest, assuming the same total payment
(interest + scheduled amortization) each year. It may be useful to remember
that, if the outstanding principal is Q, interest is r and amortization occurs
over k years, the scheduled amortization in the first year is


Qr
(1 + r) [k] 1 [.]

           

Exercise 15.1 Derive this formula, using the fact that the total payment
(interest + scheduled amortization) is the same for years 1 through k.


Here Q = 100 r = 0.10 and k = 10, thus the scheduled amortization in
the first year is 6.27. Adding the 10 % interest payment on Q, the total
payments (interest + scheduled amortization) are $16.27 M per year.


250CHAPTER 15. DP MODELS: STRUCTURING ASSET BACKED SECURITIES

|Period (t)|Interest<br>(I )<br>t|Scheduled<br>Amortization<br>(P )<br>t|Outstanding<br>Principal<br>(Q )<br>t|
|---|---|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|10.00<br>9.37<br>8.68<br>7.92<br>7.09<br>6.17<br>5.16<br>4.05<br>2.83<br>1.48|6.27<br>6.90<br>7.59<br>8.35<br>9.19<br>10.11<br>11.12<br>12.22<br>13.45<br>14.80|93.73<br>86.83<br>79.24<br>70.89<br>61.70<br>51.59<br>40.47<br>28.25<br>14.80<br>0|



Total 100.00


The above table assumes no prepayment. Next we want to analyze the
following scenario: a conditional prepayment model reflecting the 100% PSA
(Public Securities Association) industry-standard benchmark. For simplicity, we present a yearly PSA model, even though the actual PSA model
is defined monthly. The rate of mortgage prepayments is 1% of the outstanding principal at the end of the first year. At the end of the second
year, prepayment is 3% of the outstanding principal at that time. At the
end of the third year, it is 5% of the outstanding principal. For each later
year t ≥ 3, prepayment is 6% of the outstanding principal at the end of
year t. Let us denote by PPt the prepayment in year t. For example,
in year 1, in addition to the interest payment I1 = 10 and the amortization payment A1 = 6.27, there is a 1 % prepayment on the 100 - 6.27 =
93.73 principal remaining after amortization. That is, there is a prepayment
PP1 = 0.9373 collected at the end of year 1. Thus the principal pay down
is P1 = A1 + PP1 = 6.27 + 0.9373 = 7.2073 in year 1. The outstanding
principal at the end of year 1 is Q1 = 100 7.2073 = 92.7927. In year 2, the

            interest paid is I2 = 9.279 (that is 10% of Q1), the amortization payment is
A2 = (1 [Q] . [1] 10) [×][0][9][.][10] 1 [= 6][.][8333] [and] [the] [prepayment] [is] [PP][2] [= 2][.][5788] [(that] [is] [3%] [of]

    Q1 − A2) and the principal pay down is P2 = A2 + PP2 = 9.412, etc.

Exercise 15.2 Construct the table containing It, Pt and Qt to reflect the
above scenario.


Loss multiple and required buffer
In order to achieve a high quality rating, tranches should be able to sustain higher than expected default rates without compromising payments to
the tranche holders. For this reason, credit ratings are assigned based on
how much money is “behind” the current tranche. That is, how much outstanding principal is left after the current tranche is retired, as a percentage
of the total amount of principal. This is called the “buffer”. Early tranches


15.2. ENUMERATING POSSIBLE TRANCHES 251


receive higher credit ratings since they have greater buffers, which means
that the CMO would have to experience very large default rates before their
payments would be compromised. A tranche with AAA rating must have
a buffer equal to six times the expected default rate. This is referred to as
the “loss multiple”. The loss multiples are as follows:


The required buffer is computed by the following formula:


Required Buffer = WAL   - Expected Default Rate   - Loss Multiple


Let us assume a 0.9% expected default rate, based on foreclosure rates
reported by the M&T Mortgage Corporation in 2004. With this assumption,
the required buffer to get a AAA rating for a tranche with a WAL of 4 years
is 4 × 0.009 × 6 = 21.6%.

Exercise 15.3 Construct the table containing the required buffer as a function of rating and WAL, assuming a 0.9% expected default rate.


Coupon Yields and Spreads
Each tranche is priced based on a credit spread to the current treasury
rate for a risk-free bond of that approximate duration. These rates appear
in the next table, based on the yields on U.S. Treasuries as of 10/12/04.
The reader can get more current figures from on-line sources. Spreads on
corporate bonds with similar credit ratings would provide reasonable figures.

|Period (t)|Risk-Free<br>Spot|Credit Spread in Basis Points|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Period (t)|Risk-Free<br>Spot|AAA|AA|A|BBB|BB|B|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|2.18 %<br>2.53 %<br>2.80 %<br>3.06 %<br>3.31 %<br>3.52 %<br>3.72 %<br>3.84 %<br>3.95 %<br>4.07 %|13<br>17<br>20<br>26<br>31<br>42<br>53<br>59<br>65<br>71|43<br>45<br>47<br>56<br>65<br>73<br>81<br>85<br>90<br>94|68<br>85<br>87<br>90<br>92<br>96<br>99<br>106<br>112<br>119|92<br>109<br>114<br>123<br>131<br>137<br>143<br>151<br>158<br>166|175<br>195<br>205<br>220<br>235<br>245<br>255<br>262<br>268<br>275|300<br>320<br>330<br>343<br>355<br>373<br>390<br>398<br>407<br>415|


#### 15.2 Enumerating possible tranches


We are going to consider every possible tranche: since there are 10 possible
maturities t and t possible starting dates j with j ≤ t for each t, there


252CHAPTER 15. DP MODELS: STRUCTURING ASSET BACKED SECURITIES


are 55 possible tranches. Specifically, tranche (j, t) starts amortizing at the
beginning of year j and ends at the end of year t.



Exercise 15.4 From the principal payments Pt that you computed in Exercise 15.2, construct a table containing WALjt for each possible combination
(j, t).



�10
For each of the 55 possible tranches (j, t), compute the buffer ~~�~~ k=10t+1 [P][k]
k=1 [P][k] [.]



If there is no buffer, the corresponding tranche is a Z-tranche. When there
is a buffer, calculate the Loss Multiple from the formula: Required Buffer
= WAL - Expected Default Rate * Loss Multiple. Finally construct a table
containing the credit rating for each tranche that is not a Z-tranche.
For each of the 55 tranches, construct a table containing the appropriate
coupon rate cjt (no coupon rate on a Z-tranche). As described earlier, these
rates depend on the WAL and credit rating just computed.



Define Tjt to be the present value of the payments on a tranche (j, t).
Armed with the proper coupon rate cjt and a full curve of spot rates rt, Tjt
is computed as follows. In each year k, the payment Ck for tranche (j, t) is
equal to the coupon rate cjt times the remaining principal, plus the principal
payment made to tranche (j, t) if it is amortizing in year k. The present
value of Ck is simply equal to (1+Crkk) [k] [.] [Now] [T][jt] [is] [obtained] [by] [summing] [the]
present values of all the payments going to tranche (j, t).

#### 15.3 A Dynamic Programming Approach


Based on the above data, we would like to structure a CMO with four
sequential tranches A, B, C, Z. The objective is to maximize the profits
from the issuance by choosing the size of each tranche. In this section, we
present a dynamic programming recursion for solving the problem.
Let t = 1, . . ., 10 index the years. The states of the dynamic program
will be the years t and the stages will be the number k of tranches up to
year t.
Now that we have the matrix Tjt, we are ready to describe the dynamic
programming recursion. Let


v(k, t) = Minimum present value of total payments to bondholders in years


1 through t when the CMO has k tranches up to year t.


Obviously, v(1, t) is simply T1t. For k 2, the value v(k, t) is computed
≥
recursively by the formula:


v(k, t) = min
j=k 1,...,t 1 [(][v][(][k][ −] [1][, j][) +][ T][j][+1][,t][)][.]

           -           

For example, for k = 2 and t = 4, we compute v(1, j) + Tj+1,4 for each
j = 1, 2, 3 and we take the minimum. The power of dynamic programming becomes clear as k increases. For example, when k = 4, there is no
need to compute the minimum of thousands of possible combinations of 4


15.4. CASE STUDY 253


tranches. Instead, we use the optimal structure v(3, j) already computed
in the previous stage. So the only enumeration is over the size of the last
tranche.


Exercise 15.5 Compute v(4, 10) using the above recursion. Recall that
v(4, 10) is the least cost solution of structuring the CMO into four tranches.
What are the sizes of the tranches in this optimal solution? To answer this
question, you will need to backtrack from the last stage and identify how
the minimum leading to v(4, 10) was achieved at each stage.


Exercise 15.6 The dynamic programming approach presented in this section is based on a single prepayment model. How would you deal with
several scenarios for prepayment and default rates, each occuring with a
given probability?

#### 15.4 Case Study


Repeat the above steps for a pool of mortgages using current data. Study
the influence of the expected default rate on the profitability of structuring
your CMO. What other factors have a significant impact on profitability?


254CHAPTER 15. DP MODELS: STRUCTURING ASSET BACKED SECURITIES


## Chapter 16

# Stochastic Programming: Theory and Algorithms

#### 16.1 Introduction

In the introductory chapter and elsewhere, we argued that many optimization problems are described by uncertain parameters. There are different ways of incorporating this uncertainty. We consider two approaches:
Stochastic programming in the present chapter and robust optimization in
Chapter 19. Stochastic programming assumes that the uncertain parameters
are random variables with known probability distributions. This information
is then used to transform the stochastic program into a so-called deterministic equivalent which might be a linear program, a nonlinear program or an
integer program (see Chapters 2, 5 and 11 respectively).
While stochastic programming models have existed for several decades,
computational technology has only recently allowed the solution of realistic size problems. The field continues to develop with the advancement of
available algorithms and computing power. It is a popular modeling tool for
problems in a variety of disciplines including financial engineering.
The uncertainty is described by a certain sample space Ω, a σ-field of
random events and a probability measure P (see Appendix C). In stochastic programming, Ωis often a finite set ω1, . . ., ωS . The corresponding
{ }
probabilities p(ωk) ≥ 0 satisfy [�][S] k=1 [p][(][ω][k][)] [=] [1.] [For] [example,] [to] [represent]
the outcomes of flipping a coin twice in a row, we would use four random
events Ω= {HH, HT, TH, TT }, each with probability 1/4, where H stands
for Head and T stands for Tail.
Stochastic programming models can include anticipative and/or adaptive decision variables. Anticipative variables correspond to those decisions
that must be made here-and-now and cannot depend on the future observations/partial realizations of the random parameters. Adaptive variables
correspond to wait-and-see decisions that can be made after some (or, sometimes all) of the random parameters are observed.
Stochastic programming models that include both anticipative and adaptive variables are called recourse models. Using a multi-stage stochastic programming formulation, with recourse variables at each stage, one can model


255


256CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


a decision environment where information is revealed progressively and the
decisions are adapted to each new piece of information.
In investment planning, each new trading opportunity represents a new
decision to be made. Therefore, trading dates where investment portfolios
can be rebalanced become natural choices for decision stages, and these problems can be formulated conveniently as multi-stage stochastic programming
problems with recourse.

#### 16.2 Two Stage Problems with Recourse


In Chapter 1, we have already seen a generic form of a two-stage stochastic
linear program with recourse:



maxx a [T] x + E[maxy(ω) c(ω) [T] y(ω)]
Ax = b
B(ω)x + C(ω)y(ω) = d(ω)
x ≥ 0, y(ω) ≥ 0.



(16.1)



In this formulation, the first-stage decisions are represented by vector
x. These decisions are made before the random event ω is observed. The
second-stage decisions are represented by vector y(ω). These decisions are
made after the random event ω has been observed, and therefore the vector y is a function of ω. A and b define deterministic constraints on the
first-stage decisions x, whereas B(ω), C(ω), and d(ω) define stochastic constraints linking the recourse decisions y(ω) to the first-stage decisions x.
The objective function contains a deterministic term a [T] x and the expectation of the second-stage objective c(ω) [T] y(ω) taken over all realizations of
the random event ω.
Notice that the first-stage decisions will not necessarily satisfy the linking constraints B(ω)x + C(ω)y(ω) = d(ω), if no recourse action is taken.
Therefore, recourse allows one to make sure that the initial decisions can be
“corrected” with respect to this second set of feasibility equations.
In Section 1.2.1, we also argued that problem (16.1) can be represented
in an alternative manner by considering the second-stage or recourse problem
that is defined as follows, given x, the first-stage decisions:


f (x, ω) = max c(ω) [T] y(ω)
C(ω)y(ω) = d(ω) − B(ω)x (16.2)
y(ω) ≥ 0.


Let f (x) = E[f (x, ω)] denote the expected value of this optimum. If the
function f (x) is available, the two-stage stochastic linear program (16.1)
reduces to a deterministic nonlinear program:


max a [T] x + f (x)
Ax = b (16.3)
x ≥ 0.


16.2. TWO STAGE PROBLEMS WITH RECOURSE 257


Unfortunately, computing f (x) is often very hard, especially when the
sample space Ωis infinite. Next, we consider the case where Ωis a finite
set.
Assume that Ω= ω1, . . ., ωS and let p = (p1, . . ., pS) denote the
{ }
probability distribution on this sample space. The S possibilities ωk, for
k = 1, . . ., S are also called scenarios. The expectation of the second-stage
objective becomes:



E[max =
y(ω) [c][(][ω][)][T] [y][(][ω][)]]



�S

pk max
k=1 y(ωk) [c][(][ω][k][)][T][ y][(][ω][k][)]



For brevity, we write ck instead of c(ωk), etc. Under this scenario approach the two-stage stochastic linear programming problem (16.1) takes
the following form:



maxx a [T] x + [�][S] k=1 [p][k] [max][y] k [c] k [T] [y][k]
Ax = b
Bkx + Ckyk = dk for k = 1, . . . S
x ≥ 0
yk 0 for k = 1, . . ., S.
≥



(16.4)



Note that there is a different second stage decision vector yk for each scenario
k. The maximum in the objective is achieved by optimizing over all variables
x and yk simultaneously. Therefore, this optimization problem is:



maxx,y1,...,yS a [T] x + p1c [T] 1 [y][1] + . . . + pSc [T] S [y][S]
Ax = b
B1x + C1y1 = d1
... ... ...
BSx + CSyS = dS
x, y1, . . . yS 0.
≥



(16.5)



This is a deterministic linear programming problem called the deterministic
equivalent of the original uncertain problem. This problem has S copies
of the second-stage decision variables and therefore, can be significantly
larger than the original problem before we considered the uncertainty of the
parameters. Fortunately, however, the constraint matrix has a very special
sparsity structure that can be exploited by modern decomposition based
solution methods (see Section 16.4).


Exercise 16.1 Consider an investor with an initial wealth W0. At time 0,
the investor constructs a portfolio comprising one riskless asset with return
R1 in the first period and one risky asset with return R1 [+] [with] [probability]
0.5 and R1 [−] [with] [probability 0.5.] [At] [the] [end] [of] [the] [first] [period,] [the] [investor]
can rebalance her portfolio. The return in the second period is R2 for the
riskless asset, while it is R2 [+] [with probability 0.5 and][ R] 2 [−] [with probability 0.5]
for the risky asset. The objective is to meet a liability L2 = 0.9 at the end
of Period 2 and to maximize the expected remaining wealth W2. Formulate
a 2-stage stochastic linear program that solves the investor’s problem.


258CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


Exercise 16.2 In Exercise 3.2, the cash requirement in quarter Q1 is known
to be 100 but, for the remaining quarters, the company considers 3 equally
likely scenarios:
Q2 Q3 Q4 Q5 Q6 Q7 Q8
Scenario 1 450 100 −650 −550 200 650 −850
Scenario 2 500 100 −600 −500 200 600 −900
Scenario 3 550 150 −600 −450 250 600 −800

Formulate a linear program that maximizes the expected wealth of the
company at the end of quarter Q8.

#### 16.3 Multi Stage Problems


In a multi-stage stochastic program with recourse, the recourse decisions
can be taken at several points in time, called stages. Let n ≥ 2 be the
number of stages. The random event ω is a vector (o1, . . ., on−1) that gets
revealed progressively over time. The first-stage decisions are taken before
any component of ω is revealed. Then o1 is revealed. With this knowledge,
one takes the second-stage decisions. After that, o2 is revealed, and so on,
alternating between a new component of ω beeing revealed and new recourse
decisions beeing implemented. We assume that Ω= ω1, . . ., ωS is a finite
{ }
set. Let pk be the probability of scenario ωk, for k = 1, . . ., S.
Some scenarios ωk may be identical in their first components and only
become differentiated in the later stages. Therefore it is convenient to introduce the scenario tree, which illustrates how the scenarios branch off at each
stage. The nodes are labelled 1 through N, where node 1 is the root. Each
node is in one stage, where the root is the unique node in stage 1. Each
node i in stage k ≥ 2 is adjacent to a unique node a(i) in stage k − 1. Node
a(i) is called the father of node i. The paths from the root to the leaves
(in stage n) represent the scenarios. Thus the last stage has as many nodes
as scenarios. These nodes are called the terminal nodes. The collection
of scenarios passing through node i in stage k have identical components
o1, . . ., ok−1.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-257-0.png)







4 scenarios



Stage 1 2 3


Figure 16.1: A scenario tree with 3 stages and 4 scenarios


16.3. MULTI STAGE PROBLEMS 259


In Figure 16.1, Node 1 is the root, Nodes 4, 5, 6 and 7 are the terminal
nodes. The father of Node 6 is Node 2, in other words a(6) = 2.
Associated with each node i is a recourse decision vector xi. For a node i
is stage k, the decisions xi are taken based on the information that has been
revealed up to stage k. Let qi be the sum of the probabilities pk over all the
scenarios ωk that go through node i. Therefore qi is the probability of node
i, conditional on being in Stage k. The multi-stage stochastic program with
recourse can be formulated as follows:




      maxx1,...,xN Ni=1 [q][i][c] i [T] [x][i]
Ax1 = b
Bixa(i) + Cixi = di for i = 2, . . ., N
xi 0.
≥



(16.6)



In this formulation, A and b define deterministic constraints on the firststage decisions x1, whereas Bi, Ci, and di define stochastic constraints linking the recourse decisions xi in node i to the recourse decisions xa(i) in its
father node. The objective function contains a term c [T] i [x][i] [for] [each] [node.]
To illustrate, we present formulation (16.6) for the example of Figure 16.1. The terminal nodes 4 to 7 correspond to scenarios 1 to 4 respectively. Thus we have q4 = p1, q5 = p2, q6 = p3 and q7 = p4, where pk is
the probability of scenario k. We also have q2 = p1 + p2 + p3, q3 = p4 and
q2 + q3 = 1.


max c [T] 1 [x][1] +q2c [T] 2 [x][2] +q3c [T] 3 [x][3] +p1c [T] 4 [x][4] +p2c [T] 5 [x][5] +p3c [T] 6 [x][6] p4c [T] 7 [x][7]
Ax1 = b
B2x1 +C2x2 = d2
B3x1 +C3x3 = d3
B4x2 +C4x4 = d4
B5x2 +C5x5 = d5
B6x2 +C6x6 = d6
B7x3 +C7x7 = d7
xi 0.
≥


Note that the size of the linear program (16.6) increases rapidly with the
number of stages. For example, for a problem with 10 stages and a binary
tree, there are 1024 scenarios and therefore the linear program (16.6) may
have several thousand constraints and variables, depending on the number
of variables and constraints at each node. Modern commercial codes can
handle such large linear programs, but a moderate increase in the number
of stages or in the number of branches at each stage could make (16.6) too
large to solve by standard linear programming solvers. When this happens,
one may try to exploit the special structure of (16.6) to solve the model (see
Section 16.4).


Exercise 16.3 In Exercise 3.2, the cash requirements in quarters Q1, Q2,
Q3, Q6 and Q7 are known. On the other hand, the company considers two


260CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


equally likely (and independent) possibilities for each of the quarters Q4,
Q5 and Q8, giving rise to eight equally likely scenarios. In quarter Q4, the
cash inflow will be either 600 or 650. In quarter Q5, it will be either 500 or
550. In quarter Q8, it will be either 850 or 900. Formulate a linear program
that maximizes the expected wealth of the company at the end of quarter
Q8.


Exercise 16.4 Develop the linear program (16.6) for the following scenario
tree.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-259-0.png)







4 scenarios



Stage 1 2 3

#### 16.4 Decomposition


The size of the linear program (16.6) depends on the number of decision
stages and the branching factor at each node of the scenario tree. For
example, a 4-stage model with 25 branches at each node has 25 × 25 ×
25 × 25 = 390625 scenarios. Increasing the number of stages and branches
quickly results in an explosion of dimensionality. Obviously, the size of
(16.6) can be a limiting factor in solving realistic problems. When this
occurs, it becomes essential to take advantage of the special structure of the
linear program (16.6). In this section, we present a decomposition algorithm
for exploiting this structure. It is called Benders decomposition or, in the
stochastic programming literature, the L-shaped method.
The structure that we really want to exploit is that of the two-stage
problem (16.5). So we start with (16.5). We will explain subsequently how
to deal with the general multi-stage model (16.6). The constraint matrix of
(16.5) has the following form:














A
B1 C1
... ...
BS CS








 .




Note that the blocks C1, . . ., CS of the constraint matrix are only interrelated through the blocks B1, . . ., BS which correspond to the first-stage


16.4. DECOMPOSITION 261


decisions. In other words, once the first-stage decisions x have been fixed,
(16.5) decomposes into S independent linear programs. The idea of Benders
decomposition is to solve a “master problem” involving only the variables x
and a series of independent “recourse problems” each involving a different
vector of variables yk. The master problem and recourse problems are linear
programs. The size of these linear programs is much smaller than the size
of full model (16.5). The recourse problems are solved for a given vector x
and their solutions are used to generate inequalities that are added to the
master problem. Solving the new master problem produces a new x and the
process is repeated. More specifically, let us write (16.5) as


maxx a [T] x + P1(x) + . . . + PS(x)
Ax = b (16.7)
x ≥ 0

where, for k = 1, . . . S,


Pk(x) = maxyk pkc [T] k [y][k]
Ckyk = dk Bkx (16.8)
                    yk 0.
≥


The dual linear program of the recourse problem (16.8) is:


Pk(x) = minuk u [T] k [(][d][k][ −] [B][k][x][)]
(16.9)
Ck [T] [u][k]

[≥] [p][k][c][k][.]

For simplicity, we assume that the dual (16.9) is feasible, which is the
case of interest in applications. The recourse linear program (16.8) will be
solved for a sequence of vectors x [i], for i = 0, . . .. The initial vector x [0] might
be obtained by solving


maxx a [T] x
Ax = b (16.10)
x ≥ 0.

For a given vector x [i], two possibilities can occur for the recourse linear
program (16.8): either (16.8) has an optimal solution or it is infeasible.


If (16.8) has an optimal solution yk [i] [, and][ u][i] k [is the corresponding optimal]
dual solution, then (16.9) implies that


Pk(x [i] ) = (u [i] k [)][T][ (][d][k]

[−] [B][k][x][i][)]

and, since
Pk(x) (u [i] k [)][T][ (][d][k]
≤ [−] [B][k][x][)]

we get that
Pk(x) ≤ (u [i] k [)][T][ (][B][k][x][i][ −] [B][k][x][) +][ P][k][(][x][i][)][.]

This inequality, which is called an optimality cut, can be added to the current
master linear program. Initially, the master linear program is just (16.10).


262CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


If (16.8) is infeasible, then the dual problem is unbounded. Let u [i] k [a]
direction wherepkck. Since we (16.9) is unbounded,are only interested ini.e.first-stage(u [i] k [)][T][ (][d][k][ −] decisions [B][k][x][i][)][ <][ 0] x that [and][ C] leadk [T] [u] k [i] to [≥]
feasible second-stage decisions yk, the following feasibility cut can be added
to the current master linear program:


(u [i] k [)][T][ (][d][k]

[−] [B][k][x][)][ ≥] [0][.]


After solving the recourse problems (16.8) for each k, we have the following lower bound on the optimal value of (16.5):


LB = a [T] x [i] + P1(x [i] ) + . . . + PS(x [i] )


where we set Pk(x [i] ) = if the corresponding recourse problem is infeasi−∞
ble.
Adding all the optimality and feasibility cuts found so far (for j =
0, . . ., i) to the master linear program, we obtain:


      maxx,z1,...,zS a [T] x + Sk=1 [z][k]
Ax = b
zk ≤ (u [j] k [)][T] [(][B][k][x][j] [−] [B][k][x][) +][ P][k][(][x][j][)] [for] [some] [pairs] [(][j, k][)]
0 ≤ (u [j] k [)][T] [(][d][k][ −] [B][k][x][)] for the remaining pairs (j, k)
x ≥ 0.

Denoting by x [i][+1], z1 [i][+1], . . ., zS [i][+1] an optimal solution to this linear program
we get an upper bound on the optimal value of (16.5):


UB = a [T] x [i][+1] + z1 [i][+1] + . . . + zS [i][+1] .


Benders decomposition alternately solves the recourse problems (16.8) and
the master linear program with new optimality and feasibility cuts added
at each iteration until the gap between the upper bound UB and the lower
bound LB falls below a given threshold. One can show that UB - LB
converges to zero in a finite number of iterations. See, for instance, the
book of Birge and Louveaux [12], pages 159-162.


Benders decomposition can also be used for multi-stage problems (16.6)
in a straightforward way: The stages are partitioned into a first set that
gives rise to the “master problem” and a second set that gives rise to the
“recourse problems”. For example in a 6-stage problem, the variables of the
first 2 stages could define the master problem. When these variables are
fixed, (16.6) decomposes into separate linear programs each involving variables of the last 4 stages. The solutions of these recourse linear programs
provide optimality or feasibility cuts that can be added to the master problem. As before, upper and lower bounds are computed at each iteration and
the algorithm stops when the difference drops below a given tolerance. Using this approach, Gondzio and Kouwenberg [32] were able to solve an asset
liability management problem with over 4 million scenarios, whose linear


16.5. SCENARIO GENERATION 263


programming formulation (16.6) had 12 million constraints and 24 million
variables. This linear program was so large that storage space on the computer became an issue. The scenario tree had 6 levels and 13 branches at
each node. In order to apply two-stage Benders decomposition, Gondzio
and Kouwenberg divided the 6 period problem into a first stage problem
containing the first 3 periods and a second stage containing periods 4 to
6. This resulted in 2,197 recourse linear programs, each involving 2,197
scenarios. These recourse linear programs were solved by an interior point
algorithm. Note that Benders decomposition is ideally suited for parallel
computations since the recourse linear programs can be solved simultaneously. When the solution of all the recourse linear programs is completed
(which takes the bulk of the time), the master problem is then solved on
one processor while the other processors remain idle temporarily. Gondzio
and Kouwenberg tested a parallel implementation on a computer with 16
processors and they obtained an almost perfect speedup, that is a speedup
factor of almost k when using k processors.

#### 16.5 Scenario Generation


How should one generate scenarios in order to formulate a deterministic
equivalent formulation (16.6) that accurately represents the underlying stochastic program? There are two separate issues. First, one needs to model the
correlation over time among the random parameters. For a pension fund,
such a model might relate wage inflation (which influences the liability side)
to interest rates and stock prices (which influence the asset side). Mulvey

[53] describes the system developed by Towers Perrin, based on a cascading
set of stochastic differential equations. Simpler autoregressive models can
also be used. This is discussed below. The second issue is the construction
of a scenario tree from these models: A finite number of scenarios must
reflect as accurately as possible the random processes modeled in the previous step, suggesting the need for a large number of scenarios. On the other
hand, the linear program (16.6) can only be solved if the size of the scenario
tree is reasonably small, suggesting a rather limited number of scenarios. To
reconcile these two conflicting objectives, it might be crucial to use variance
reduction techniques. We address these issues in this section.


16.5.1 Autoregressive model


In order to generate the random parameters underlying the stochastic program, one needs to construct an economic model reflecting the correlation
between the parameters. Historic data may be available. The goal is to generate meaningful time series for constructing the scenarios. One approach
is to use an autoregressive model.
Specifically, if rt denotes the random vector of parameters in period t,
an autoregressive model is defined by:


rt = D0 + D1rt 1 + . . . + Dprt p + ϵt

             -             

264CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


where p is the number of lags used in the regression, D0, D1, . . ., Dp are
time independent constant matrices which are estimated through statistical
methods such as maximum likelihood, and ϵt is a vector of i.i.d. random
disturbances with mean zero.
To illustrate this, consider the example of Section 8.1.1. Let st, bt and
mt denote the rates of return of stocks, bonds and the money market, respectively, in year t. An autoregressive model with p = 1 has the form:





st

 bt
mt







 =





d1

 d2
d3







+





d11 d12 d13

 d21 d22 d23
d31 d32 d33













 st−1
 bt−1
mt−1







+





ϵ [s] t

 ϵ [b] t
ϵ [m] t







 t = 2, . . ., T



In particular, to find the parameters d1, d11, d12, d13 in the first equation


st = d1 + d11st−1 + d12bt−1 + d13mt−1 + ϵ [s] t


one can use standard linear regression tools that minimize the sum of the
squared errors ϵ [s] t [.] [Within] [an] [Excel] [spreadsheet] [for] [instance,] [one] [can] [use]
the function LINEST. Suppose that the rates of return on the stocks are
stored in cells B2 to B44 and that, for bonds and the money market, the
rates are stored in columns C and D, rows 2 to 44 as well. LINEST is an
array formula. Its first argument contains the known data for the left hand
side of the equation (here the column st), the second argument contains the
known data in the right hand side (here the columns st−1, bt−1 and mt−1).
Typing LINEST(B3:B44, B2:D43,,) one obtains the following values of the
parameters:


d1 = 0.077, d11 = 0.058, d12 = 0.219, d13 = 0.448.
            

Using the same approach for the other two equations we get the following
autoregressive model:


st = 0.077 − 0.058st−1 + 0.219bt−1 + 0.448mt−1 + ϵ [s] t

bt = 0.047 − 0.053st−1 − 0.078bt−1 + 0.707mt−1 + ϵ [b] t

mt = 0.016 + 0.033st−1 − 0.044bt−1 + 0.746mt−1 + ϵ [m] t

The option LINEST(B3:B44, B2:D43,,TRUE) provides some useful statistics, such as the standard error of the estimate st. Here we get a standard
error of σs = 0.173. Similarly, the standard error for bt and mt are σb = 0.108
and σm = 0.022 respectively.


Exercise 16.5 Instead of an autoregressive model relating the rates of returns rt, bt and mt, construct an autoregressive model relating the logarithms of the returns gt = log(1 + rt), ht = log(1 + bt) and kt = log(1 + mt).
Use one lag, i.e. p = 1. Solve using LINEST or your prefered linear regression
tool.


16.5. SCENARIO GENERATION 265


Exercise 16.6 In the above autoregressive model, the coefficients of mt−1
are significantly larger than those of st−1 and bt−1. This suggests that these
two variables might not be useful in the regression. Resolve the example
assuming the following autoregressive model:


st = d1 + d13mt−1 + ϵ [s] t

bt = d2 + d23mt−1 + ϵ [b] t

mt = d3 + d33mt−1 + ϵ [m] t


16.5.2 Constructing scenario trees


The random distributions relating the various parameters of a stochastic
program must be discretized to generate a set of scenarios that is adequate
for its deterministic equivalent. Too few scenarios may lead to approximation errors. On the other hand, too many scenarios will lead to an explosion
in the size of the scenario tree, leading to an excessive computational burden. In this section, we discuss a simple random sampling approach and two
variance reduction techniques: adjusted random sampling and tree fitting.
Unfortunately, scenario trees constructed by these methods could contain
spurious arbitrage opportunities. We end this section with a procedure to
test that this does not occur.


Random sampling


One can generate scenarios directly from the autoregressive model introduced in the previous section:


rt = D0 + D1rt 1 + . . . + Dprt p + ϵt

             -             

where ϵt N (0, Σ) are independently distributed multivariate normal dis∼
tributions with mean 0 and covariance matrix Σ.
In our example, Σ is a 3 × 3 diagonal matrix, with diagonal entries
σs, σb and σm. Using the parameters σs = 0.173, σb = 0.108, σm = 0.022
computed earlier, and a random number generator, we obtained ϵ [s] t [=][ −][0][.][186,]
ϵ [b] t [= 0][.][052] [and] [ϵ][m] t [= 0][.][007.] [We] [use] [the] [autoregressive] [model] [to] [get] [rates] [of]
return for 2004 based on the known rates of returns for 2003 (see Table in
Section 8.1.1):


s2004 = 0.077 0.058 0.2868+0.219 0.0054+0.448 0.0098 0.186 = 0.087

     - × × ×     -     
b2004 = 0.047 0.053 0.2868 0.078 0.0054+0.707 0.0098+0.052 = 0.091

     - ×     - × ×

m2004 = 0.016+0.033 0.2868 0.044 0.0054+0.746 0.0098+0.007 = 0.040
×       - × ×

These are the rates of return for one of the branches from node 1. For each
of the other branches from node 1, one generates random values of ϵ [s] t [,] [ϵ][b] t
and ϵ [m] t and computes the corresponding values of s2004, b2004 and m2004.
Thirty branches or so may be needed to get a reasonable approximation
of the distribution of the rates of return in stage 1. For a problem with


266CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


3 stages, 30 branches at each stage represent 27,000 scenarios. With more
stages, the size of the linear program (16.6) explodes. Kouwenberg [45]
performed tests on scenario trees with fewer branches at each node (such as
a 5-stage problem with branching structure 10-6-6-4-4, meaning 10 branches
at the root, then 6 branches at each node in the next stage and so on)
and he concluded that random sampling on such trees leads to unstable
investment strategies. This occurs because the approximation error made by
representing parameter distributions by random samples can be significant
in a small scenario tree. As a result the optimal solution of (16.6) is not
optimal for the actual parameter distributions. How can one construct a
scenario tree that more accurately represents these distributions, without
blowing up the size of (16.6)?


Adjusted random sampling


An easy way of improving upon random sampling is as follows. Assume
that each node of the scenario tree has an even number K = 2k of branches.
Instead of generating 2k random samples from the autoregressive model,
generate k random samples only and use the negative of their error terms
to compute the values on the remaining k branches. This will fit all the odd
moments of the distributions correctly. In order to fit the variance of the
distributions as well, one can scale the sampled values. The sampled values
are all scaled by a multiplicative factor until their variance fits that of the
corresponding parameter.
As an example, corresponding to the branch with ϵ [s] t [=][ −][0][.][186,][ ϵ] t [b] [= 0][.][052]
and ϵ [m] t = 0.007 at node 1, one would also generate another branch with
ϵ [s] t [= 0][.][186,][ ϵ] t [b] [=][ −][0][.][052 and][ ϵ] t [m] [=][ −][0][.][007.] [For this branch the autoregressive]
model gives the following rates of return for 2004:


s2004 = 0.077 0.058 0.2868+0.219 0.0054+0.448 0.0098+0.186 = 0.285

     - × × ×



b2004 = 0.047 0.053 0.2868 0.078 0.0054+0.707 0.0098 0.052 = 0.013

     - ×     - × ×     -     


m2004 = 0.016+0.033 0.2868 0.044 0.0054+0.746 0.0098 0.007 = 0.026
×       - × ×       


Suppose that the set of ϵ [s] t [generated] [on] [the] [branches] [leaving] [from] [node] [1]
has standard deviation 0.228 but the corresponding parameter should have
standard deviation 0.165. Then the ϵ [s] t [would] [be] [scaled] [down] [by] 0 [0] . [.] 228 [165] [on]



standard deviation 0.165. Then the ϵt [would] [be] [scaled] [down] [by] 0.228 [on]

all the branches from node 1. For example, instead of ϵ [s] t [=] [−][0][.][186] [on] [the]
branch discussed earlier, one would use ϵ [s] t [=] [−][0][.][186] [0] 0 [.] . [165] 228 [=] [−][0][.][135.] [This]



branch discussed earlier, one would use ϵ [s] t [=] [−][0][.][186] 0.228 [=] [−][0][.][135.] [This]

corresponds to the following rate of return:



s2004 = 0.077 0.058 0.2868+0.219 0.0054+0.448 0.0098 0.135 = 0.036

     - × × ×     -     
The rates of returns on all the branches from node 1 would be modified in
the same way.


Tree fitting


How can one best approximate a continuous distribution by a discrete distribution with K values? In other words, how should one choose values vk


16.5. SCENARIO GENERATION 267


and their probabilities pk, for k = 1, . . ., K, in order to approximate the
given distribution as accurately as possible? A natural answer is to match
as many of the moments as possible. In the context of a scenario tree, the
problem is somewhat more complicated since there are several correlated
parameters at each node and there is interdependence between periods as
well. Hoyland and Wallace [39] propose to formulate this fitting problem as
a nonlinear program. The fitting problem can be solved either at each node
separately or on the overall tree. We explain the fitting problem at a node.
Let Sl be the values of the statistical properties of the distributions that one
desires to fit, for l = 1, . . ., s. These might be the expected values of the
distributions, the correlation matrix, the skewness and kurtosis. Let vk and
pk denote the vector of values on branch k and its probability, respectively,
for k = 1, . . ., K. Let fl(v, p) be the mathematical expression of property l
for the discrete distribution (for example, the mean of the vectors vk, their
correlation, skewness and kurtosis). Each property has a positive weight wl
indicating its importance in the desired fit. Hoyland and Wallace formulate
the fitting problem as


       minv,p �l [w][l][(][f][l][(][v, p][)][ −] [S][l][)][2]
k [p][k] [= 1] (16.11)
p ≥ 0

One might want some statistical properties to match exactly. As an example,
consider again the autoregressive model:


rt = D0 + D1rt 1 + . . . + Dprt p + ϵt

             -             

where ϵt N (0, Σ) are independently distributed multivariate normal dis∼
tributions with mean 0 and covariance matrix Σ. To simplify notation, let
us write ϵ instead of ϵt. The random vector ϵ has distribution N (0, Σ) and
we would like to approximate this continuous distribution by a finite number
of disturbance vectors ϵ [k] occuring with probability pk, for k = 1, . . ., K. Let
ϵ [k] q [denote] [the] [q][th] [component] [of] [vector] [ϵ][k][.] [One] [might] [want] [to] [fit] [the] [mean]
of ϵ exactly and its covariance matrix as well as possible. In this case, the
fitting problem is:


       -       l l
minϵ1,...,ϵK,p q=1 r=1 [(][�][K] k=1 [p][k][ϵ] q [k][ϵ][k] r

       K [−] [Σ][qr][)][2]
�k=1 [p][k][ϵ][k] [= 0]
k [p][k] [= 1]
p ≥ 0


Arbitrage-free scenario trees


Approximating the continuous distributions of the uncertain parameters by a
finite number of scenarios in the linear programming (16.6) typically creates
modeling errors. In fact, if the scenarios are not chosen properly or if their
number is too small, the supposedly “linear programming equivalent” could
be far from being equivalent to the original stochastic program. One of the
most disturbing aspects of this phenomenon is the possibility of creating


268CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


arbitrage opportunities when constructing the scenario tree. When this
occurs, model (16.6) might produce unrealistic solutions that exploit these
arbitrage opportunities. Klaassen [42] was the first to address this issue. In
particular, he shows how arbitrage opportunities can be detected ex post in
a scenario tree. When such arbitrage opportunities exist, a simple solution is
to discard the scenario tree and to construct a new one with more branches.
Klaassen [42] also discusses what constraints to add to the nonlinear program
(16.11) in order to preclude arbitrage opportunities ex ante. The additional
constraints are nonlinear, thus increasing the difficulty of solving (16.11).
We present below Klassen’s ex post check.
Recall that there are two types of arbitrage (Definition 4.1). We start we
Type A. An arbitrage of Type A is a trading strategy with an initial positive
cash flow and no risk of loss later. Let us express this at a node i of the
scenario tree. Let r [k] denote the vectors of rates of return on the branches
connecting node i to its sons in the next stage, for k = 1, . . ., K. There exists
an arbitrage of Type A if there exists an asset allocation x = (x1, . . ., xQ)
at node i such that
�Q

xq < 0
q=1



and



�Q

xqrq [k] for all k = 1, . . ., K.
q=1 [≥] [0]



To check whether such an allocation x exists, it suffices to solve the linear
program
�Q
minx q=1 [x][q]
�Q (16.12)
q=1 [x][q][r] q [k] [≥] [0] for all k = 1, . . ., K.

There is an arbitrage opportunity of Type A at node i if and only if this
linear program is unbounded.
Next we turn to Type B. An arbitrage of Type B requires no initial cash
input, has no risk of a loss and a positive probability of making profits in the
future. At node i of the scenario tree, this is expressed by the conditions:



�Q

xq = 0,
q=1



�Q

xqrq [k] for all k = 1, . . ., K
q=1 [≥] [0]



and



�Q

xqrq [k] [>][ 0] for at least one k = 1, . . ., K.
q=1



These conditions can be checked by solving the linear program

�Q
maxx q=1 [x][q][r] q [k]
�Qq=1 [x][q] [= 0] (16.13)
�Q
q=1 [x][q][r] q [k] [≥] [0] for all k = 1, . . ., K.


16.5. SCENARIO GENERATION 269


There is an arbitrage opportunity of Type B at node i if and only if this
linear program is unbounded.


Exercise 16.7 Show that the linear program (16.12) is always feasible.
Write the dual linear program of (16.12). Let uk be the dual variable
associated with the kth constraint of (16.12).
Recall that a feasible linear program is unbounded if and only if its dual
is infeasible. Show that there is no arbitrage of Type A at node i if and only
if there exists uk 0, for k = 1, . . ., K such that
≥

�K

ukrq [k] [= 1] for all q = 1, . . ., Q.
k=1


Similarly, write the dual of (16.13). Let v0, vk, for k = 1, . . ., K be the
dual variables. Write necessary and sufficient conditions for the nonexistence
of arbitrage of Type B at node i, in terms of vk, for k = 0, . . ., K.
Modify the nonlinear program (16.11) in order to formulate a fitting
problem at node i that contains no arbitrage opportunities.


270CHAPTER 16. STOCHASTIC PROGRAMMING: THEORY AND ALGORITHMS


## Chapter 17

# SP Models: Value-at-Risk and Conditional Value-at-Risk

In this chapter, we discuss Value-at-Risk, a widely used measure of risk
in finance, and its relative Conditional Value-at-Risk. We then present an
optimization model that optimizes a portfolio when the risk measure is the
Conditional Value-at-Risk instead of the variance of the portfolio as in the
Markowitz model. This is acheived through stochastic programming. In this
case, the variables are anticipative. The random events are modeled by a
large but finite set of scenarios, leading to a linear programming equivalent
of the original stochastic program.

#### 17.1 Risk Measures


Financial activities involve risk. Our stock or mutual fund holdings carry
the risk of losing value due to market conditions. Even money invested in
a bank carries a risk–that of the bank going bankrupt and never returning
the money let alone some interest. While individuals generally just have to
live with such risks, financial and other institutions can and very often must
manage risk using sophisticated mathematical techniques. Managing risk
requires a good understanding of quantitative risk measures that adequately
reflect the vulnerabilities of a company.
Perhaps the best-known risk measure is Value-at-Risk (VaR) developed
by financial engineers at J.P. Morgan. VaR is a measure related to percentiles of loss distributions and represents the predicted maximum loss with
a specified probability level (e.g., 95%) over a certain period of time (e.g.,
one day). Consider, for example, a random variable X that represents loss
from an investment portfolio over a fixed period of time. A negative value
for X indicates gains. Given a probability level α, α-VaR of the random
variable X is given by the following relation:


VaRα(X) := min γ : P (X γ) 1 α . (17.1)
{ ≥ ≤                - }


271


272 CHAPTER 17. SP MODELS: VALUE-AT-RISK


When the loss distribution is continuous, VaRα(X) is simply the loss such
that
P (X VaRα(X)) = α.
≤

The following figure illustrates the 0.95-VaR on a portfolio loss distribution plot:


1.4



1.2


1


0.8


0.6


0.4


0.2


0







|x 10 −4 VaR|Col2|
|---|---|
|5%<br>P(X)|5%<br>P(X)|
|||


VaR0.95(X)



VaR is widely used by people in the financial industry and VaR calculators are common features in most financial software. Despite this popularity, VaR has one important undesirable property–it lacks subadditivity.
Risk measures should respect the maxim “diversification reduces risk” and
therefore, satisfy the following property: “The total risk of two different
investment portfolios does not exceed the sum of the individual risks.” This
is precisely what we mean by saying that a risk measure should be a subadditive function, i.e., for a risk measure f, we should have


f (x1 + x2) ≤ f (x1) + f (x2), ∀x1, x2.

Consider the following simple example that illustrates that diversification
can actually increase the risk measured by VaR:


Example 17.1 Consider two independent investment opportunities each returning a $1 gain with probability 0.96 and $2 loss with probability 0.04.
Then, 0.95-VaR for both investments are -1. Now consider the sum of these
two investment opportunities. Because of independence, this sum has the
following loss distribution: $4 with probability 0.04 × 0.04 = 0.0016, $1 with
probability 2 × 0.96 × 0.04 = 0.0768, and -$2 with probability 0.96 × 0.96 =
0.9216. Therefore, the 0.95-VaR of the sum of the two investments is 1,
which exceeds -2, the sum of the 0.95-VaR values for individual investments.


An additional difficulty with VaR is in its computation and optimization. When VaR is computed by generating scenarios, it turns out to be a


17.1. RISK MEASURES 273


non-smooth and non-convex function of the positions in the investment portfolio. Therefore, when one tries to optimize VaR computed in this manner,
multiple local optimizers are encountered, hindering the global optimization
process.
Another criticism of VaR is that it pays no attention to the magnitude
of losses beyond the VaR value. This and other undesirable features of
VaR led to the development of alternative risk measures. One well-known
modification of VaR is obtained by computing the expected loss given that
the loss exceeds VaR. This quantity is often called conditional Value-at-Risk
or CVaR. There are several alternative names for this measure in the finance
literature including Mean Expected Loss, Mean Shortfall, and Tail VaR. We
now describe this risk measure in more detail and discuss how it can be
optimized using linear programming techniques when the loss function is
linear in the portfolio positions. Our discussion follows parts of articles by
Rockafellar and Uryasev [61, 73].
We consider a portfolio of assets with random returns. We denote the
portfolio choice vector by x and the random events by the vector y. Let
f (x, y) denote the loss function when we choose the portfolio x from a set
X of feasible portfolios and y is the realization of the random events. We
assume that the random vector y has a probability density function denoted
by p(y).
For a fixed decision vector x, we compute the cumulative distribution
function of the loss associated with that vector x:




      Ψ(x, γ) := p(y)dy. (17.2)

f (x,y)<γ



Then, for a given confidence level α, the α-VaR associated with portfolio x
is given by


VaRα(x) := min γ IR : Ψ(x, γ) α . (17.3)
{ ∈ ≥ }

We define the α-CVaR associated with portfolio x as:



1
CVaRα(x) :=
1 − α







f (x, y)p(y)dy. (17.4)
f (x,y)≥VaRα(x)


f (x, y)p(y)dy
f (x,y)≥VaRα(x)



Note that,



1
CVaRα(x) =
1 − α



1
≥ 1 α
   








VaRα(x)p(y)dy
f (x,y)≥VaRα(x)



VaRα(x)
=







1 − α



VaRα(x),
≥



p(y)dy
f (x,y)≥VaRα(x)



i.e., CVaR of a portfolio is always at least as big as its VaR. Consequently,
portfolios with small CVaR also have small VaR. However, in general minimizing CVaR and VaR are not equivalent.


274 CHAPTER 17. SP MODELS: VALUE-AT-RISK


For a discrete probability distribution (where event yj occurs with probability pj, for j = 1, . . ., n), the above definition of CVaR becomes



1
CVaRα(x) =
1 − α




 
pjf (x, yj)
j:f (x,yj)≥VaRα(x)



Example:
Suppose we are given the loss function f (x, y) for a given decision x as
f (x, y) = −y where y = 75 − j with probability 1 % for j = 0, . . ., 99. We
would like to determine the Value-at-Risk VaRα(x) for α = 95%. We have
VaR95%(x) = 20 since the loss is 20 or more with probability 5 %.
To compute the Conditional Value-at-Risk, we use the above formula:
CVaR95%(x) = 0.105 [(20 + 21 + 22 + 23 + 24)][ ×][ 1% = 22][.]


Exercise 17.1 (a) Compute the 0.90-VaR and 0.90-CVaR for the rates of
return of stocks between 1961 and 2003 (see Section 8.1.1 for the data).
(b) Compute the 0.90-VaR and 0.90-CVaR for the rates of return of
bonds and a money market account. Again use the data of Section 8.1.1.


Exercise 17.2 Give an example showing that CVaR is not subadditive.

#### 17.2 Minimizing CVaR


Since the definition of CVaR involves the VaR function explicitly, it is difficult to work with and optimize this function. Instead, we consider the
following simpler auxiliary function:



1
Fα(x, γ) := γ +
1 − α





f (x,y)≥γ (f (x, y) − γ) p(y)dy. (17.5)



Alternatively, we can write Fα,x(γ) as follows:



1
Fα(x, γ) = γ +
1 − α




(f (x, y) − γ) [+] p(y)dy, (17.6)



where a [+] = max{a, 0}. This function, viewed as a function of γ, has the
following important properties that make it useful for the computation of
VaR and CVaR:


1. Fα(x, γ) is a convex function of γ.


2. VaRα(x) is a minimizer over γ of Fα(x, γ).


3. The minimum value over γ of the function Fα(x, γ) is CVaRα(x).


Exercise 17.3 Prove the properties of Fα,x(γ) stated above.


17.2. MINIMIZING CVAR 275


As a consequence of the listed properties, we immediately deduce that,
in order to minimize CVaRα(x) over x, we need to minimize the function
Fα(x, γ) with respect to x and γ simultaneously:


min [min] (17.7)
x X [CVaR][α][(][x][) =] x X,γ [F][α][(][x, γ][)][.]
∈ ∈

Consequently, we can optimize CVaR directly, without needing to compute
VaR first. If the loss function f (x, y) is a convex (linear) function of the
portfolio variables x, then Fα(x, γ) is also a convex (linear) function of x.
In this case, provided the feasible portfolio set X is also convex, the optimization problems in (17.7) are smooth convex optimization problems that
can be solved using well known optimization techniques for such problems
(see Chapter 5).
Often it is not possible or desirable to compute/determine the joint density function p(y) of the random events in our formulation. Instead, we may
have a number of scenarios, say ys for s = 1, . . ., S, which may represent
some historical values of the random events or some values obtained via
computer simulation. We will assume that all scenarios have the same probability. In this case, we obtain the following approximation to the function
Fα(x, γ) by using the empirical distribution of the random events based on
the available scenarios:



1
F˜α(x, γ) := γ +
(1 − α)S



�S

(f (x, ys) γ) [+] . (17.8)
     s=1



Compare this definition to (17.6). Now, the problem minx X CVaRα(x) can
∈
be approximated by replacing Fα(x, γ) with F [˜] α(x, γ) in (17.7):



1
min
x∈X,γ [γ][ +] (1 − α)S



�S

(f (x, ys) γ) [+] . (17.9)
     s=1



To solve this optimization problem, we introduce artificial variables zs to
replace (f (x, ys) γ) [+] . This is achieved by imposing the constraints zs
       - ≥
f (x, ys) γ and zs 0:
    - ≥




     minx,z,γ γ + (1−1α)S Ss=1 [z][s]
s.t. zs 0, s = 1, . . ., S,
≥
zs f (x, ys) γ, s = 1, . . ., S,
≥         x ∈ X.



(17.10)



Note that the constraints zs f (x, ys) γ and zs 0 alone cannot ensure
≥         - ≥
that zs = (f (x, ys) γ) [+] = max f (x, ys) γ, 0 since zs can be larger than
        - {         - }
both right-hand-sides and be still feasible. However, since we are minimizing
the objective function which involves a positive multiple of zs, it will never be
optimal to assign zs a value larger than the maximum of the two quantities
f (x, ys) γ and 0, and therefore, in an optimal solution zs will be precisely
    (f (x, ys) γ) [+], justifying our substitution.
    In the case that f (x, y) is linear in x, all the expressions zs f (x, ys) γ
≥                  represent linear constraints and therefore the problem (17.10) is a linear


276 CHAPTER 17. SP MODELS: VALUE-AT-RISK


programming problem that can be solved using the simplex method or alternative LP algorithms.


Other optimization problems arise naturally within the context of risk
management. For example, risk managers often try to optimize a performance measure (e.g., expected return) while making sure that certain risk
measures do not exceed a threshold value. When the risk measure is CVaR,
the resulting optimization problem is:


maxx µ [T] x
s.t. CVaRαj (x) Uαj, j = 1, . . ., J (17.11)
≤
x ∈ X.

Above, J is an index set for different confidence levels used for CVaR computations and Uαj represents the maximum tolerable CVaR value at the
confidence level α [j] . As above, we can replace the CVaR functions in the
constraints of this problem with the function Fα(x, γ) as above and then
approximate this function using the scenarios for random events. This approach results in the following approximation of the CVaR-constrained problem (17.11):



maxx,z,γ  - µ [T] x
1 S
s.t. γ + (1 α [j] )S s=1 [z][s] Uαj, j = 1, . . ., J,

       - ≤
zs 0, s = 1, . . ., S,
≥
zs f (x, ys) γ, s = 1, . . ., S,
≥           x ∈ X.

#### 17.3 Example: Bond Portfolio Optimization



(17.12)



A portfolio of risky bonds might be characterized by a large likelihood of
small earnings, coupled with a small chance of loosing a large amount of
the investment. The loss distribution is heavily skewed and, in this case,
standard mean-variance analysis to characterize market risk is inadequate.
VaR and CVaR are more appropriate criteria for minimizing portfolio credit
risk. Credit risk is the risk of a trading partner not fulfilling their obligation
in full on the due date or at any time thereafter. Losses can result both from
default and from a decline in market value stemming from downgrades in
credit ratings. A good reference is the paper of Anderson, Mausser, Rosen
and Uryasev [2].
Anderson, Mausser, Rosen and Uryasev consider a portfolio of 197 bonds
from 29 different countries with a market value of $ 8.8 billion and duration
of approximately 5 years. Their goal is to rebalance the portfolio in order
to minimize credit risk. That is they want to minimize losses resulting from
default and from a decline in market value stemming from downgrades in
credit ratings (credit migration). The loss due to credit migration is simply

f (x, y) = (b − y) [T] x

where b are the future values of each bond with no credit migration and y
are the future values with credit migration (so y is a random vector). The


17.3. EXAMPLE: BOND PORTFOLIO OPTIMIZATION 277


one-year portfolio credit loss was generated using a Monte Carlo simulation:
20,000 scenarios of joint credit states of obligators and related losses. The
distribution of portfolio losses has a long fat tail. The authors rebalanced the
portfolio by minimizing CVaR. The set X of feasible porfolios was described
by the following constraints. Let xi denote the weight of asset i in the
portfolio. Upper and lower bounds were set on each xi:

li ≤�xi ≤ ui i = 1, . . ., n
i [x][i] [= 1]

To calculate the efficient frontier, the expected portfolio return was set
to at least R:

 i [µ][i][x][i]

[≥] [R]

To summarize, the linear program (17.10) to be solved was as follows:

       minx,z,γ γ + (1−1α)S Ss=1 [z][s]
subject to zs i [(][b][i] for s = 1, . . ., S
≥ [�] [−] [y][is][)][x][i] [−] [γ]
zs 0 for s = 1, . . ., S
≥
l�i ≤ xi ≤ ui i = 1, . . ., n
�i [x][i] [= 1]
i [µ][i][x][i]

[≥] [R]

Consider α = 99%. The original bond portfolio had an expected portfolio
return of 7.26%. The expected loss was 95 million dollars with a standard
deviation of 232 million. The VaR was 1.03 billion dollars and the CVaR
was 1.32 billion.
After optimizing the portfolio (with expected return of 7.26%), the expected loss was only 5 thousand dollars, with a standard deviation of 152
million. The VaR was reduced to 210 million and the CVaR to 263 million
dollars. So all around, the characteristics of the portfolio were much improved. Positions were reduced in bonds from Brazil, Russia and Venezuela,
whereas positions were increased in bonds from Thailand, Malaysia and
Chile. Positions in bonds from Colombia, Poland and Mexico remained
high and each accounted for about 5 % of the optimized CVaR.


278 CHAPTER 17. SP MODELS: VALUE-AT-RISK


## Chapter 18

# Stochastic Programming Models: Asset/Liability Management

#### 18.1 Asset/Liability Management

Financial health of any company, and in particular those of financial institutions, is reflected in the balance sheets of the company. Proper management
of the company requires attention to both sides of the balance sheet–assets
and liabilities. Asset/Liability Management (ALM) offers sophisticated
mathematical tools for an integrated management of assets and liabilities
and is the focus of many studies in financial mathematics.
ALM recognizes that static, one period investment planning models
(such as mean-variance optimization) fail to incorporate the multi-period
nature of the liabilities faced by the company. A multi-period model that
emphasizes the need to meet liabilities in each period for a finite (or possibly
infinite) horizon is often required. Since liabilities and asset returns usually
have random components, their optimal management requires tools of “Optimization under Uncertainty” and most notably, stochastic programming
approaches.
We recall the ALM setting we introduced in Section 1.3.4: Let Lt be
the liability of the company in year t for t = 1, . . ., T . The Lt’s are random
variables. Given these liabilities, which assets (and in which quantities)
should the company hold each year to maximize its expected wealth in year
T ? The assets may be domestic stocks, foreign stocks, real estate, bonds,
etc. Let Rit denote the return on asset i in year t. The Rit’s are random
variables. The decision variables are:


xit = market value invested in asset i in year t.


The decisions xit in year t are made after the random variables Lt and Rit
are realized. That is, the decision problem is multistage, stochastic, with
recourse. The stochastic program can be written as follows.


279


280 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT


max E[ [�] i [x][iT] []]
subject to

      asset accumulation: i [(1 +][ R][it][)][x][i,t][−][1][ −] [�] i [x][it] [=] [L][t] for t = 1, . . ., T
xit 0.
≥

The constraint says that the surplus left after liability Lt is covered will
be invested as follows: xit invested in asset i. In this formulation, x0,t are the
fixed, and possibly nonzero initial positions in different asset classes. The
objective selected in the model above is to maximize the expected wealth
at the end of the planning horizon. In practice, one might have a different
objective. For example, in some cases, minimizing Value at Risk (VaR)
might be more appropriate. Other priorities may dictate other objective
functions.
To address the issue of the most appropriate objective function, one must
understand the role of liabilities. Pension funds and insurance companies
are among the most typical arenas for the integrated management of assets
and liabilities through ALM. We consider the case of a Japanese insurance
company, the Yasuda Fire and Marine Insurance Co, Ltd, following the work
of Cari˜no, Kent, Myers, Stacy, Sylvanus, Turner, Watanabe, and Ziemba

[17]. In this case, the liabilities are mainly savings-oriented policies issued
by the company. Each new policy sold represents a deposit, or inflow of
funds. Interest is periodically credited to the policy until maturity, typically
three to five years, at which time the principal amount plus credited interest
is refunded to the policyholder. The crediting rate is typically adjusted
each year in relation to a market index like the prime rate. Therefore, we
cannot say with certainty what future liabilities will be. Insurance business
regulations stipulate that interest credited to some policies be earned from
investment income, not capital gains. So, in addition to ensuring that the
maturity cash flows are met, the firm must seek to avoid interim shortfalls in
income earned versus interest credited. In fact, it is the risk of not earning
adequate income quarter by quarter that the decision makers view as the
primary component of risk at Yasuda.
The problem is to determine the optimal allocation of the deposited
funds into several asset categories: cash, fixed rate and floating rate loans,
bonds, equities, real estate and other assets. Since we can revise the portfolio allocations over time, the decision we make is not just among allocations
today but among allocation strategies over time. A realistic dynamic asset/liability model must also account for the payment of taxes. This is
made possible by distinguishing between interest income and price return.
A stochastic linear program is used to model the problem. The linear
program has uncertainty in many coefficients. This uncertainty is modeled
through a finite number of scenarios. In this fashion, the problem is transformed into a very large scale linear program of the form (16.6). The random
elements include price return and interest income for each asset class, as well
as policy crediting rates.
We now present a multistage stochastic program that was developed for
The Yasuda Fire and Marine Insurance Co., Ltd. Our presentation follows
the description of the model as stated in [17].


18.1. ASSET/LIABILITY MANAGEMENT 281


Stages are indexed by t = 0, 1, . . ., T .
Decision variables of the stochastic program:


xit = market value in asset i at t,

wt = interest income shortfall at t 1,
≥

vt = interest income surplus at t 1.
≥

Random variables appearing in the stochastic linear program: For t ≥ 1,



RPit = price return of asset i from t 1 to t,
                 


RIit = interest income of asset i from t 1 to t,
                   


Ft = deposit inflow from t 1 to t,
             


Pt = principal payout from t 1 to t,
              


It = interest payout from t 1 to t,
              


gt = rate at which interest is credited to policies from t 1 to t,
                          


Lt = liability valuation at t.



Parameterized function appearing in the objective:


ct = piecewise linear convex cost function.


The objective of the model is to allocate funds among available assets to
maximize expected wealth at the end of the planning horizon T less expected
penalized shortfalls accumulated through the planning horizon.


max E[ [�] i [x][iT] [−] [�] t [T] =1 [c][t][(][w][t][)]]
subject to

       asset accumulation: �i [x][it][ −] [�] i [(1 +][ RP][it][ +][ RI][it][)][x][i,t][−][1] [=] [F][t][ −] [P][t][ −] [I][t] for t = 1, . . ., T
interest income shortfall: i [RI][it][x][i,t][−][1] + wt − vt = gtLt−1 for t = 1, . . ., T
xit 0, wt 0, vt 0.
≥ ≥ ≥
(18.1)
Liability balances and cash flows are computed so as to satisfy the liability accumulation relations.


Lt = (1 + gt)Lt 1 + Ft Pt It for t 1.

            -             -             - ≥

The stochastic linear program (18.1) is converted into a large linear program using a finite number of scenarios to deal with the random elements
in the data. Creation of scenario inputs is made in stages using a tree. The
tree structure can be described by the number of branches at each stage.
For example, a 1-8-4-4-2-1 tree has 256 scenarios. Stage t = 0 is the initial
stage. Stage t = 1 may be chosen to be the end of Quarter 1 and has 8
different scenarios in this example. Stage t = 2 may be chosen to be the end
of Year 1, with each of the previous scenarios giving rise to 4 new scenarios,
and so on. For the Yasuda Fire and Marine Insurance Co., Ltd., a problem
with 7 asset classes and 6 stages gives rise to a stochastic linear program


282 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT


(18.1) with 12 constraints (other than nonnegativity) and 54 variables. Using 256 scenarios, this stochastic program is converted into a linear program
with several thousand constraints and over 10,000 variables. Solving this
model yielded extra income estimated to about US$ 80 million per year for
the company.


Exercise 18.1 Discuss the relevance of the techniques from Chapter 16 in
the solution of the Yasuda Fire and Marine Insurance Co., such as scenario
generation (correlation of the random parameters over time, variance reduction techniques in constructing the scenario tree), decomposition techniques
to solve the large-scale linear programs.


18.1.1 Corporate Debt Management


A closely related problem to the asset/liability management (ALM) problem
in corporate financial planning is the problem of debt management. Here
the focus is on retiring (paying back) outstanding debt at minimum cost.
More specifically, corporate debt managers must make financial decisions to
minimize the costs and risks of borrowing to meet debt financing requirements. These requirements are often determined by the firm’s investment
decisions. Our discussion in this subsection is based on the article [24].
Debt managers need to choose the sources of borrowing, types of debts
to be used, timing and terms of debts, whether the debts will be callable [1],
etc., in a multi-period framework where the difficulty of the problem is
compounded by the fact that the interest rates that determine the cost
of debt are uncertain. Since interest rate movements can be modeled by
random variables this problem presents an attractive setting for the use of
stochastic programming techniques. Below, we discuss a deterministic linear
programming equivalent of stochastic LP model for the debt management
problem.
We consider a multi-period framework with T time periods. We will use
the indices s and t ranging between 0 (now) and T (termination date, or
horizon) to denote different time periods in the model. We consider K types
of debt that are distinguished by market of issue, term and the presence
(or absence) of call option available to the borrower. In our notation, the
superscript k ranging between 1 and K will denote the different types of
debt being considered.
The evolution of the interest rates are described using a scenario tree.
We denote by ej = ej1, ej2, . . ., ejT, j = 1, . . ., J a sample path of this scenario tree which corresponds to a sequence of interest rate events. When
a parameter or variable is contingent on the event sequence ej we use the
notation (ej) (see below).
The decision variables in this model are the following:


1A callable debt is a debt security whose issuer has the right to redeem the security
prior to its stated maturity date at a price established at the time of issuance, on or after
a specified date.


18.1. ASSET/LIABILITY MANAGEMENT 283


  - Bt [k][(][e][j][):] [dollar] [amount] [at] [par][2] [of] [debt] [type] [k] [B][orrowed] [at] [the] [begin-]
ning of period t.


  - Os,t [k] [(][e][j][):] [dollar amount at par of debt type][ k] [borrowed in period][ s][ and]
Outstanding at the beginning of period t.


  - Rs,t [k] [(][e][j][):] [dollar amount at par of debt type][ k] [borrowed in period][ s][ and]
Retired (paid back) at the beginning of period t.


St(ej): dollar value of Surplus cash held at the beginning of period t.

  

Next, we list the input parameters to the problem:


  - rs,t [k] [(][e][j][):] [interest] [payment] [in] [period] [t] [per] [dollar] [outstanding] [of] [debt]
type k issued in period s.


  - ft [k][:] [issue] [costs] [(excluding] [premium] [or] [discount)] [per] [dollar] [borrowed]
of debt type k issued in period t.


  - gs,t [k] [(][e][j][):] [retirement] [premium] [or] [discount] [per] [dollar] [for] [debt] [type] [k]
issued in period s, if retired in period t [3] .


it(ej): interest earned per dollar on surplus cash in period t.

  
p(ej): probability of the event sequence ej. Note that p(ej) 0, j

  - ≥ ∀
and [�][J] j=1 [p][(][e][j][) = 1.]


Ct: cash requirements for period t, which can be negative to indicate

  an operating surplus.


Mt: maximum allowable cost of debt service in period t.

  
  - qt [k][(][Q] t [k][):] [minimum] [(maximum)] [borrowing] [of] [debt] [type] [k] [in] [period] [t][.]

Lt(ej)(Ut(ej)): minimum (maximum) dollar amount of debt (at par)

  retired in period t.


The objective function of this problem is expressed as follows:








�K


k=1



�T


t=1




- �� 1 + gt,T [k] [(][e][j][)] Ot,T [k] [(][e][j][)][ −] [R] t,T [k] [(][e][j][)] + (1 − fT [k][)][B] T [k] [(][e][j][)]



min



�J

p(ej)
j=1



.



(18.2)
This function expresses the expected retirement cost of the total debt outstanding at the end of period T .
We complete the description of the deterministic equivalent of the stochastic LP by listing the constraints of the problem:


2At a price equal to the par (face) value of the security; the original issue price of a
security.
3These parameters are used to define call options and to value the debt portfolio at
the end of the planning period.


284 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT


  - Cash Requirements: For each time period t = 1, . . ., T and scenario
path j = 1, . . ., J:



�� 1 − ft [k] Bt [k][(][e][j][) + (1 +][ i][t][−][1][(][e][j][))][ S][t][−][1][(][e][j][)]



Ct + St(ej) =



�K


k=1




- - - - [�]
rs,t [k] [(][e][j][)][O] s,t [k] [(][e][j][)][ −] 1 + gs,t [k] [(][e][j][)] Rs,t [k] [(][e][j][)]







�t−1


s=0



.



This balance equation indicates that the difference between cash available (new net borrowing, surplus cash from previous period and the
interest earned on this cash) and the debt payments (interest on outstanding debt and cash outflows on repayment) should equal the cash
requirements plus the surplus cash left for this period.


- Debt Balance Constraints: For j = 1, . . ., J, t = 1, . . ., T, s =
0, . . ., t − 2, and k = 1, . . . K:

Os,t [k] [(][e][j][)][ −] [O] s,t [k] 1 [(][e][j][) +][ R] s,t [k] 1 [(][e][j][)] = 0

            -            
Ot [k] 1,t [(][e][j][)][ −] [B] t [k] 1 [(][e][j][)][ −] [R] t [k] 1,t [(][e][j][)] = 0

       -        -        

- Maximum cost of debt: For j = 1, . . ., J, t = 1, . . ., T, and k =
1, . . . K:



�t−1


s=1




- rs,t [k] [(][e][j][)][O] s,t [k] [(][e][j][)][ −] [i][t][−][1][(][e][j][)][S][t][−][1][(][e][j][)] ≤ Mt.




- Borrowing limits: For j = 1, . . ., J, t = 1, . . ., T, and k = 1, . . . K:

qt [k] [≤] [B] t [k][(][e][j][)][ ≤] [Q] t [k][.]

- Payoff limits: For j = 1, . . ., J and t = 1, . . ., T :



�t−1

Rs,t [k] [(][e][j][)][ ≤] [U][t][(][e][j][)][.]
s=0



Lt(ej)
≤



�K


k=1




  - Nonnegativity: For j = 1, . . ., J, t = 1, . . ., T, s = 0, . . ., t − 2, and
k = 1, . . . K:


Bt [k][(][e][j][)][ ≥] [0][,] Os,t [k] [(][e][j][)][ ≥] [0][,] Rs,t [k] [(][e][j][)][ ≥] [0][,] St(ej) ≥ 0.


In the formulation above, we used the notation of the article [24]. However, since the parameters and variables dependent on ej can only depend on the portion of the sequence that is revealed by a certain time,
a more precise notation can be obtained using the following ideas. First, let
e [t] j [=][ e][j][1][, e][j][2][, . . ., e][jt][, j] [= 1][, . . ., J, t][ = 1][, . . ., T] [,] [i.e.,] [e][t] j [represents] [the] [portion]
of ej observed by time period t. Then, one replaces the expressions such as
St(ej) with St(e [t] j [),] [etc.]


18.2. SYNTHETIC OPTIONS 285

#### 18.2 Synthetic Options


An important issue in portfolio selection is the potential decline of the portfolio value below some critical limit. How can we control the risk of downside
losses? A possible answer is to create a payoff structure similar to a European call option.
While one may be able to construct a diversified portfolio well suited
for a corporate investor, there may be no option market available on this
portfolio. One solution may be to use index options. However exchangetraded options with sufficient liquidity are limited to maturities of about
three months. This makes the cost of long-term protection expensive, requiring the purchase of a series of high priced short-term options. For large
institutional or corporate investors, a cheaper solution is to artificially produce the desired payoff structure using available resources. This is called a
“synthetic option strategy”.
The model is based on the following data.


W0 = investor’s initial wealth,
T = planning horizon,
R = riskless return for one period,
Rt [i] = return for asset i at time t,
θt [i] = transaction cost for purchases and sales of asset i at time t.

The Rt [i][’s] [are] [random,] [but] [we] [know] [their] [distributions.]


The variables used in the model are the following.

x [i] t = amount allocated to asset i at time t,
A [i] t = amount of asset i bought at time t,
Dt [i] = amount of asset i sold at time t,
αt = amount allocated to riskless asset at time t.


We formulate a stochastic program that produces the desired payoff at
the end of the planning horizon T, much in the flavor of the stochastic
programs developed in the previous two sections. Let us first discuss the
constraints.
The initial portfolio is


α0 + x [1] 0 [+][ . . .][ +][ x] 0 [n] [=][ W][0][.]


The portfolio at time t is


x [i] t [=][ R] t [i][x][i] t 1 [+][ A] t [i] t for t = 1, . . ., T

          - [−] [D][i]



�n

(1 θt [i][)][D] t [i] for t = 1, . . ., T.
  i=1



αt = Rαt−1 −



�n

(1 + θt [i][)][A][i] t [+]
i=1



One can also impose upper bounds on the proportion of any risky asset
in the portfolio:



0 x [i] t [+]
≤ [≤] [m][t][(][α][t]



�n



x [j] t [)][,]
j=1


286 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT


where mt is chosen by the investor.


The value of the portfolio at the end of the planning horizon is:



v = RαT 1 +
     


�n

(1 θT [i] [)][R] T [i] [x] T [i] 1 [,]
  -   i=1



where the summation term is the value of the risky assets at time T .


To construct the desired synthetic option, we split v into the riskless
value of the portfolio Z and a surplus z ≥ 0 which depends on random
events. Using a scenario approach to the stochastic program, Z is the worstcase payoff over all the scenarios. The surplus z is a random variable that
depends on the scenario. Thus


v = Z + z


z ≥ 0.

We consider Z and z as variables of the problem, and we optimize them
together with the asset allocations x and other variables described earlier.
The objective function of the stochastic program is


max E(z) + µZ


where µ ≥ 1 is the risk aversion of the investor. The risk aversion µ is given
data.
When µ = 1, the objective is to maximize expected return.
When µ is very large, the objective is to maximize “riskless profit” as
we defined it in Chapter 4 (Exercise 4.10).


As an example, consider an investor with initial wealth W0 = 1 who
wants to construct a portfolio comprising one risky asset and one riskless
asset using the “synthetic option” model described above. We write the
model for a two-period planning horizon, i.e. T = 2. The return on the
riskless asset is R per period. For the risky asset, the return is R1 [+] [with]
probability .5 and R1 [−] [with] [the] [same] [probability] [at] [time] [t] [=] [1.] [Similarly,]
the return of the risky asset is R2 [+] [with probability .5 and][ R] 2 [−] [with the same]
probability at time t = 2. The transaction cost for purchases and sales of
the risky asset is θ.


There are 4 scenarios in this example, each occurring with probability
.25, which we can represent by a binary tree. The initial node will be
denoted by 0, the up node from it by 1 and the down node by 2. Similarly
the up node from node 1 will be denoted by 3, the down node by 4, and
the successors of 2 by 5 and 6 respectively. Let xi, αi denote the amount of
risky asset and of riskless asset respectively in the portfolio at node i of this
binary tree. Z is the riskless value of the portfolio and zi is the surplus at
node i. The linear program is:


18.2. SYNTHETIC OPTIONS 287


max .25z3 + .25z4 + .25z5 + .25z6 + µZ
subject to
initial portfolio: α0 + x0 = 1
rebalancing constraints: x1 = R1 [+][x][0][ +][ A][1][ −] [D][1]
α1 = Rα0 − (1 + θ)A1 + (1 − θ)D1
x2 = R1 [−][x][0][ +][ A][2][ −] [D][2]
α2 = Rα0 − (1 + θ)A2 + (1 − θ)D2
payoff: z3 + Z = Rα1 + (1 θ)R2 [+][x][1]
                      z4 + Z = Rα1 + (1 θ)R2 [−][x][1]
                      z5 + Z = Rα2 + (1 θ)R2 [+][x][2]
                      z6 + Z = Rα2 + (1 θ)R2 [−][x][2]
                      nonnegativity: αi, xi, zi, Ai, Di 0.
≥


Example: An interesting paper discussing synthetic options is the paper of
Y. Zhao and W.T. Ziemba [75]. Zhao and Ziemba apply the synthetic option
model to an example with 3 assets (cash, bonds and stocks) and 4 periods
(a one-year horizon with quarterly portfolio reviews). The quarterly return
on cash is constant at ρ = 0.0095. For stocks and bonds, the expected logarithmic rates of returns are s = 0.04 and b = 0.019 respectively. Transaction
costs are 0.5% for stocks and 0.1% for bonds. The scenarios needed in the
stochastic program are generated using an auto regression model which is
constructed based on historical data (quarterly returns from 1985 to 1998;
the Salomon Brothers bond index and S&P 500 index respectively). Specifically, the auto regression model is


 st = 0.037 0.193st 1 + 0.418bt 1 0.172st 2 + 0.517bt 2 + ϵt
       -        -        -        -        -        bt = 0.007 0.140st 1 + 0.175bt 1 0.023st 2 + 0.122bt 2 + ηt
       -        -        -        -        -        where the pair (ϵt, ηt) characterizes uncertainty. The scenarios are generated
by selecting 20 pairs of (ϵt, ηt) to estimate the empirical distribution of one
period uncertainty. In this way, a scenario tree with 160,000 (= 20 × 20 ×
20 × 20) paths describing possible outcomes of asset returns is generated for
the 4 periods.
The resulting large scale linear program is solved. We discuss the results
obtained when this linear program is solved for a risk aversion of µ = 2.5:
The value of the terminal portfolio is always at least 4.6% more than the
initial portfolio wealth and the distribution of terminal portfolio values is
skewed to larger values because of dynamic downside risk control. The
expected return is 16.33% and the volatility is 7.2%. It is interesting to
compare these values with those obtained from a static Markowitz model:
The expected return is 15.4% for the same volatility but no minimum return
is guaranteed! In fact, in some scenarios, the value of the Markowitz portfolio
is 5% less at the end of the one-year horizon than it was at the beginning.
It is also interesting to look at an example of a typical portfolio (one
of the 160,000 paths) generated by the synthetic option model (the linear
program was set up with an upper bound of 70 % placed on the fraction of
stocks or bonds in the portfolio):


288 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT

|Col1|Cash Stocks Bonds|Portfolio value<br>at end of period|
|---|---|---|
|Period 1<br>2<br>3<br>4|12%<br>18%<br>70%<br>41%<br>59%<br>70%<br>30%<br>30%<br>70%|100<br>103<br>107<br>112<br>114|



Exercise 18.2 Computational exercise: Develop a synthetic option model
in the spirit of that used by Zhao and Ziemba, adapted to the size limitation
of your linear programming solver. Compare with a static model.

#### 18.3 Case Study: Option Pricing with Transaction Costs


A European call option on a stock with maturity T and strike price X gives
the right to buy the stock at price X at time T . The holder of the option
will not exercise this option if the stock has a price S lower than X at time
T . Therefore the value of a European call option is max(S - X, 0). Since
S is random, the question of pricing the option correctly is of interest. The
Black Scholes Merton Option Pricing model relates the price of an option
to the volatility of the stock return. The assumptions are that the market
is efficient and that the returns are lognormal. ¿From the volatility σ of
the stock return, one can compute the option price for any strike price X.
Conversely, from option prices one can compute the implied volatility σ. For
a given stock, options with different strike prices should lead to the same σ
(if the assumptions of the Black Scholes Merton model are correct).
The aim of the model developed in this section is to examine the extent
to which market imperfections can explain the deviation of observed option
prices from the Black Scholes Merton Option Pricing model. One way to
measure the deviation of the Black Scholes Merton model from observed
option prices is through the “volatility smile”: for a given maturity date, the
implied volatility of a stock computed by the Black Scholes Merton model
from observed option prices at different strike prices is typically not constant,
but instead often exhibits a convex shape as the strike price increases (the
“smile”). One explanation for the deviation is that the smile occurs because
the Black Scholes Merton model assumes the ability to rebalance portfolios
without costs imposed either by the inability to borrow or due to a bid-ask
spread or other trading costs. Here we will look at the effect of transaction
costs on option prices.
The derivation of the Black Scholes Merton formula is through a replicating portfolio containing the stock and a riskless bond. If the market is
efficient, we should be able to replicate the option payoff at time T by rebalancing the portfolio between now and time T, as the stock price evolves.
Rather than work with a continuous time model, we discretize this process.


18.3. CASE STUDY: OPTION PRICING WITH TRANSACTION COSTS289


This discretization is called the binomial approximation to the Black Scholes Merton Option Pricing model. In this model, we specify a time period
∆between trading opportunities and postulate the behavior of stock and
bond prices along successive time periods. The binomial model assumes
that in between trading periods, only two possible stock price movements
are possible.


a) There are N stages in the tree, indexed 0, 1 . . ., N, where stage 0 is
the root of the tree and stage N is the last stage. If we divide the
maturity date T of an option by N, we get that the length of a stage
is ∆= T/N .


b) Label the initial node k0.


c) For a node k = k0, let k [−] be the node that is the immediate predecessor
of k.


d) Let S(k) be the stock price at node k and let B(k) be the bond price
at node k.


e) We assume that the interest rate is fixed at the annualized rate r so
that B(k) = B(k [−] )e [r][∆] .



f) Letting σ denote the volatility of the stock return, we use the standard
parametrization u = e [σ] ~~√~~ ∆ and d = 1/u. So S(k) = S(k−)eσ ~~√~~ ∆ if an



∆ and d = 1/u. So S(k) = S(k−)eσ ~~√~~



parametrization u = e [σ] ∆ and d = 1/u. So S(k) = S(k−)eσ ∆ if an

uptick occurs from k [−] to k and S(k) = S(k [−] )e [−][σ] ~~√~~ ∆ if a downtick



uptick occurs from k [−] to k and S(k) = S(k [−] )e [−][σ] ∆ if a downtick

occurs.



g) Let n(k) be the quantity of stocks at node k and let m(k) be the
quantity of bonds at k.


18.3.1 The Standard Problem


In the binomial model, we have dynamically complete markets. This means
that by trading the stock and the bond dynamically, we can replicate the
payoffs (and values) from a call option. The option value is simply the cost of
the replicating portfolio, and the replicating portfolio is self-financing after
the first stage. This means that after we initially buy the stock and the
bond, all subsequent trades do not require any additional money and, at the
last stage, we reproduce the payoffs from the call option.
Therefore, we can represent the option pricing problem as the following
linear program. Choose quantities n(k) of the stock, quantities m(k) of the
bond at each nonterminal node k to


(5) min n(k0)S(k0) + m(k0)B(k0)
subject to
rebalancing constraints: n(k [−] )S(k) + m(k [−] )B(k) ≥ n(k)S(k) + m(k)B(k)
for every node k = k0
replication constraints: n(k [−] )S(k) + m(k [−] )B(k) ≥ max(S(k) − X, 0)
for every terminal node k


290 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT


where k [−] denotes the predecessor of k.
Note that we do not impose nonnegativity constraints since we will typically have a short position in the stock or bond.


Exercise 18.3 For a nondividend paying stock, collect data on 4 or 5 call
options for the nearest maturity (but at least one month). Calculate the
implied volatility for each option. Solve the standard problem (5) when the
number of stages is 7 using the implied volatility of the at-the-money option
to construct the tree.


18.3.2 Transaction Costs


To model transaction costs, we consider the simplest case where there are
no costs of trading at the initial and terminal nodes, but there is a bid-ask
spread on stocks at other nodes. So assume that if you buy a stock at node
k, you pay S(k)(1+ θ) while if you sell a stock, you receive S(k)(1 - θ). This
means that the rebalancing constraint becomes


n(k [−] )S(k) + m(k [−] )B(k) ≥ n(k)S(k) + m(k)B(k) + |n(k) − n(k [−] )|θS(k).


There is an absolute value in this constraint. So it is not a linear constraint. However it can be linearized as follows. Define two nonnegative
variables:


x(k) = number of stocks bought at node k, and


y(k) = number of stocks sold at node k.


The rebalancing constraint now becomes:


n(k [−] )S(k) + m(k [−] )B(k) ≥ n(k)S(k) + m(k)B(k) + (x(k) + y(k))θS(k)
n(k) − n(k [−] ) = x(k) − y(k)
x(k) ≥ 0, y(k) ≥ 0.


Note that this constraint leaves the possibility of simultaneously buying
and selling stocks at the same node. But obviously this cannot improve the
objective function that we minimize in (5), so we do not need to impose a
constraint to prevent it.
The modified formulation is:


(6) min n(k0)S(k0) + m(k0)B(k0)
subject to
rebalancing constraints: n(k [−] )S(k) + m(k [−] )B(k) ≥ n(k)S(k) + m(k)B(k)
+(x(k) + y(k))θS(k) for every node k = k0
n(k) n(k [−] ) = x(k) y(k) for every node k = k0
                -                replication constraints: n(k [−] )S(k) + m(k [−] )B(k) ≥ max(S(k) − X, 0)
for every terminal node k
nonnegativity: x(k) 0, y(k) 0 for every node k = k0.
≥ ≥


18.3. CASE STUDY: OPTION PRICING WITH TRANSACTION COSTS291


Exercise 18.4 Repeat the exercise in Section 18.3.1 allowing for transaction costs, with different values of θ, to see if the volatility smile can be
explained by transaction costs. Specifically, given a value for σ and for θ,
calculate option prices and see how they match up to observed prices. Try
θ = 0.001, 0.005, 0.01, 0.02, 0.05.


292 CHAPTER 18. SP MODELS: ASSET/LIABILITY MANAGEMENT


## Chapter 19

# Robust Optimization: Theory and Tools

#### 19.1 Introduction to Robust Optimization

In many optimization models the inputs to the problem are either not known
at the time the problem must be solved, are computed inaccurately, or
otherwise uncertain. Since the solutions obtained can be quite sensitive to
these inputs, one serious concern is that we are solving the wrong problem,
and that the solution we find is far from optimal for the correct problem.
Robust optimization refers to the modeling of optimization problems
with data uncertainty to obtain a solution that is guaranteed to be “good”
for all or most possible realizations of the uncertain parameters. Uncertainty
in the parameters is described through uncertainty sets that contain many
possible values that may be realized for the uncertain parameters. The size
of the uncertainty set is determined by the level of desired robustness.
Robust optimization can be seen as a complementary alternative to sensitivity analysis and stochastic programming. Robust optimization models
can be especially useful in the following situations:


  - Some of the problem parameters are estimates and carry estimation
risk.


  - There are constraints with uncertain parameters that must be satisfied
regardless of the values of these parameters.


  - The objective function or the optimal solutions are particularly sensitive to perturbations.


  - The decision-maker cannot afford to low-probability but high-magnitude
risks.


Recall from Chapter 1 that there are different definitions and interpretations of robustness; the resulting models and formulations differ accordingly.
In particular, we can distinguish between constraint robustness and objective
robustness. In the first case, data uncertainty puts the feasibility of potential solutions at risk. In the second, feasibility constraints are fixed and the


293


294 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS


uncertainty of the objective function affects the proximity of the generated
solutions to optimality.
Both the constraint and objective robustness models we considered in
the introduction have a worst-case orientation. That is, we try to optimize
the behavior of the solutions under the most adverse conditions. Following
Kouvelis and Yu [44], we call solutions that optimize the worst-case behavior under uncertainty absolute robust solutions. While such conservatism
is necessary in some optimization settings, it may not be desirable in others. Absolute robustness is not always consistent with a decision theoretic
approach and with common utility functions. An alternative is to seek robustness in a relative sense.
In uncertain decision environments, people whose performance is judged
relative to their peers will want to make decisions that avoid falling severely
behind their competitors under all scenarios rather than protecting themselves against the worst-case scenarios. For example, a portfolio manager
will be considered successful in a down market as long as she loses less than
her peers or a benchmark. These considerations motivate the concept of
relative robustness which we discuss in Section 19.3.3.
Another variant of the robust optimization models called adjustable robust optimization are attractive in multi-period models. To motivate these
models one can consider a multi-period uncertain optimization problem
where uncertainty is resolved progressively through periods. We assume
that a subset of the decision variables can be chosen after these parameters
are observed in a way to correct the sub-optimality of the decisions made
with less information in earlier stages. In spirit, these models are closely
related to two (or multi-) stage stochastic programming problems with recourse. They were introduced by Guslitzer and co-authors [35, 5] and we
summarize this approach in Section 19.3.4.
Each different interpretation of robustness and each different description
of uncertainty leads to a different robust optimization formulation. These
robust optimization problems often are or at least appear to be more difficult than their non-robust counterparts. Fortunately, many of them can be
reformulated in a tractable manner. While it is difficult to expect a single
approach to handle each one of the different variations in a unified manner, a close study of the existing robust optimization formulations reveals
many common threads. In particular, methods of conic optimization appear frequently in the solution of robust optimization problems. We review
some of the most commonly used reformulation techniques used in robust
optimization at the end of the chapter.

#### 19.2 Uncertainty Sets


In robust optimization, the description of the uncertainty of the parameters
is formalized via uncertainty sets. Uncertainty sets can represent or may
be formed by difference of opinions on future values of certain parameters,
alternative estimates of parameters generated via statistical techniques from
historical data and/or Bayesian techniques, among other things.


19.2. UNCERTAINTY SETS 295


Common types of uncertainty sets encountered in robust optimization
models include the following:


  - Uncertainty sets representing a finite number of scenarios generated
for the possible values of the parameters:


= p1, p2, . . ., pk .
U { }

  - Uncertainty sets representing the convex hull of a finite number of
scenarios generated for the possible values of the parameters (these
are sometimes called polytopic uncertainty sets):


= conv(p1, p2, . . ., pk).
U

  - Uncertainty sets representing an interval description for each uncertain
parameter:
U = {p : l ≤ p ≤ u}.

Confidence intervals encountered frequently in statistics can be the
source of such uncertainty sets.


  - Ellipsoidal uncertainty sets:

U = {p : p = p0 + Mu, ∥u∥≤ 1}

These uncertainty sets can also arise from statistical estimation in the
form of confidence regions, see [29]. In addition to their mathematically compact description, ellipsoidal uncertainty sets have the nice
property that they smoothen the optimal value function [65].


It is a non-trivial task to determine the uncertainty set that is appropriate for a particular model as well as the type of uncertainty sets that lead to
tractable problems. As a general guideline, the shape of the uncertainty set
will often depend on the sources of uncertainty as well as the sensitivity of
the solutions to these uncertainties. The size of the uncertainty set, on the
other hand, will often be chosen based on the desired level of robustness.
When uncertain parameters reflect the “true” values of moments of random variables, as is the case in mean-variance portfolio optimization, we
simply have no way of knowing these unobservable true values exactly since.
In such cases, after making some assumptions about the stationarity of these
random processes we can generate estimates of these true parameters using
statistical procedures. Goldfarb and Iyengar, for example, show that if we
use a linear factor model for the multivariate returns of several assets and
estimate the factor loading matrices via linear regression, the confidence regions generated for these parameters are ellipsoidal sets and they advocate
their use in robust portfolio selection as uncertainty sets [29]. To generate interval type uncertainty sets, T¨ut¨unc¨u and Koenig use bootstrapping
strategies as well as moving averages of returns from historical data [71].
The shape and the size of the uncertainty set can significantly affect the robust solutions generated. However with few guidelines backed by theoretical
and empirical studies, their choice remains an art form at the moment.


296 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS

#### 19.3 Different Flavors of Robustness


In this section we discuss each one of the robust optimization models we
mentioned above in more detail. We start with model robustness.


19.3.1 Constraint Robustness


One of the most important concepts in robust optimization is constraint
robustness. This refers to situations where the uncertainty is in the constraints and we seek solutions that remain feasible for all possible values of
the uncertain inputs. This type of solutions are required in many engineering
applications. Typical instances include multi-stage problems where the uncertain outcomes of earlier stages have an effect on the decisions of the later
stages and the decision variables must be chosen to satisfy certain balance
constraints (e.g., inputs to a particular stage can not exceed the outputs of
the previous stage) no matter what happens with the uncertain parameters
of the problem. Therefore, our solution must be constraint-robust with respect to the uncertainties of the problem. Here is a mathematical model
for finding constraint-robust solutions: Consider an optimization problem
of the form:
minx f (x) (19.1)
G(x, p) ∈ K.

Here, x are the decision variables, f is the (certain) objective function, G
and K are the structural elements of the constraints that are assumed to be
certain and p are the possibly uncertain parameters of the problem. Consider an uncertainty set U that contains all possible values of the uncertain
parameters p. Then, a constraint-robust optimal solution can be found by
solving the following problem:

minx f (x) (19.2)
G(x, p) ∈ K, ∀p ∈U.

As (19.2) indicates, the robust feasible set is the intersection of the feasible sets S(p) = {x : G(x, p) ∈ K} indexed by the uncertainty set U.
We illustrate this in Figure 19.1 for an ellipsoidal feasible set with U =
p1, p2, p3, p4, where pi correspond to the uncertain center of the ellipse.
{ }
There are no uncertain parameters in the objective function of the problem (19.2). This, however, is not a restrictive assumption. An optimization
problem with uncertain parameters in both the objective function and constraints can be easily reformulated to fit the form in (19.2). In fact,

minx f (x, p) (19.3)
G(x, p) ∈ K

is equivalent to the problem:


mint,x t
t − f (x, p) ≥ 0, (19.4)
G(x, p) ∈ K.

This last problem has all its uncertainties in its constraints.


19.3. DIFFERENT FLAVORS OF ROBUSTNESS 297



5


4


3


2


1


0


−1


−2


−3


−4



Robust feasible set



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-296-0.png)







−5
−5 −4 −3 −2 −1 0 1 2 3 4 5


Figure 19.1: Constraint robustness


Exercise 19.1 Show that if S(p) = {x : G(x, p) ∈ K} is convex for all
p, then the robust feasible set S := [�] p [S][(][p][)] [is] [also] [convex.] [If] [S][(][p][)] [is]
∈U
polyhedral for all p, is S necessarily polyhedral?


19.3.2 Objective Robustness


Another important robustness concept is objective robustness. This refers
to solutions that will remain close to optimal for all possible realizations of
the uncertain problem parameters. Since such solutions may be difficult to
obtain, especially when uncertainty sets are relatively large, an alternative
goal for objective robustness is to find solutions whose worst-case behavior
is optimized. The worst-case behavior of a solution corresponds to the value
of the objective function for the worst possible realization of the uncertain
data for that particular solution.
We now develop a mathematical model that addresses objective robustness. Consider an optimization problem of the form:


minx f (x, p) (19.5)
x ∈ S.

Here, S is the (certain) feasible set and f is the objective function that
depends on uncertain parameters p. As before, U denotes the uncertainty
set that contains all possible values of the uncertain parameters p. Then,
an objective robust solution can be obtained by solving:


minx S maxp f (x, p). (19.6)
∈ ∈U


We illustrate objective robustness problem (19.6) in Figure 19.2. In this
example, the feasible set S is the real line, the uncertainty set is U =


298 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS


p1, p2, p3, p4, p5, and the objective function f (x, pi) is a convex quadratic
{ }
function whose parameters pi determine its shape. Note that the robust
minimizer is different from the minimizers of each f (x, pi) which are denoted by x [∗] i [in] [the] [figure.] [In] [fact,] [none] [of] [the] [x][∗] i [’s] [is] [particularly] [close] [to]
the robust minimizer.



120


100


80


60


40


20


0



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-297-0.png)





Objective Robustness









−20
−8 −6  -  - −2 x* x*  - 4 6 8



x*1=x*2 −2 x*5 x*4 x*3



Figure 19.2: Objective robustness


As the argument at the end of the previous subsection shows, objective
robustness can be seen as a special case of constraint robustness via a reformulation. However, it is important to distinguish between these two problem
variants as their “natural” robust formulations lead to two different classes
of optimization formulations, namely semi-infinite and min-max optimization problems respectively. This way, different methodologies available for
these two problem classes can be readily used for respective problems.


Exercise 19.2 In Chapter 8, for a given constant λ, expected return vector
µ, and a positive definite covariance matrix Σ we considered the following
mean-variance optimization problem:


max (19.7)
x [µ][T][ x][ −] [λx][T][ Σ][x,]
∈X

where X = {x : e [T] x = 1} with e = [1 1 . . . 1] [T] . Here, we consider the
situation where we assume Σ to be certain and given but µ is assumed to
be uncertain. For a fixed µ let z(µ) represent the optimal value of this
problem. Determine z(µ) as an explicit function of µ. Verify that z(µ) is a
quadratic function. Is it convex? Let U represent the uncertainty set for µ
and formulate the objective robustness problem.


19.3. DIFFERENT FLAVORS OF ROBUSTNESS 299


19.3.3 Relative Robustness


The focus of constraint and objective robustness models on an absolute measure of worst-case performance is not consistent with risk tolerances of many
decision makers. Instead, we may prefer to measure the worst case in a relative manner, relative to the best possible solution under each scenario. This
leads us to the notion of relative robustness.
Consider the following optimization problem:


minx f (x, p) (19.8)
x ∈ S.

where p is uncertain with uncertainty set U. To simplify the description,
we restrict our attention to the case with objective uncertainty and assume
that the constraints are certain.
Given a fixed p ∈U, let z [∗] (p) denote the optimal value function, i.e.

z [∗] (p) = min f (x, p) s.t. x S.
x ∈


Furthermore, we define the optimal solution map


x [∗] (p) = arg min f (x, p) s.t. x S.
x ∈

Note that z [∗] (p) can be extended-valued and x [∗] (p) can be set-valued.
To motivate the notion of relative robustness we first define a measure
of regret associated with a decision after the uncertainty is resolved. If we
choose x as our vector and p is the realized value of the uncertain parameter,
the regret associated with choosing x instead of an element of x [∗] (p) is defined
as:
r(x, p) = f (x, p) − z [∗] (p) = f (x, p) − f (x [∗] (p), p). (19.9)

Note that the regret function is always nonnegative and can also be regarded
as a measure of the “benefit of hindsight”.
Now, for a given x in the feasible set we consider the maximum regret
function:


R(x) := max (19.10)
p [r][(][x, p][) = max] p [f] [(][x, p][)][ −] [f] [(][x][∗][(][p][)][, p][)][.]
∈U ∈U


A relative robust solution to problem (19.8) is a vector x that minimizes
the maximum regret:


min (19.11)
x S [max] p [f] [(][x, p][)][ −] [z][∗][(][p][)][.]
∈ ∈U


While they are intuitively attractive, relative robust formulations can
also be significantly more difficult than the standard absolute robust formulations. Indeed, since z [∗] (p) is the optimal value function and involves
an optimization problem itself, problem (19.11) is a three-level optimization
problem as opposed to the two-level problems in absolute robust formulations. Furthermore, the optimal value function z [∗] (p) is rarely available in
analytic form, is typically non-smooth and is often hard to analyze. Another


300 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS


difficulty is that, if f is linear in p as is often the case, then z [∗] (p) is a concave
function. Therefore, the inner maximization problem in (19.11) is a convex
maximization problem and is difficult for most U.
A simpler variant of (19.11) can be constructed by deciding on the maximum level of regret to be tolerated beforehand and by solving a feasibility
problem instead with this level imposed as a constraint. For example, if we
decide to limit the maximum regret to R, the problem to solve becomes the
following: Find an x satisfying G(x) ∈ K such that

f (x, p) − z [∗] (p) ≤ R, ∀p ∈U


If desired, one can then use bi-section on R to find the its optimal value.
Another variant of relative robustness models arises when we measure
the regret in terms of the proximity of our chosen solution to the optimal
solution set rather than in terms of the optimal objective values. For this
model, consider the following distance function for a given x and p:


d(x, p) = inf (19.12)
x∗∈x∗(p) [∥][x][ −] [x][∗][∥][.]

When the solution set is a singleton, there is no optimization involved in the
definition. As above, we then consider the maximum distance function:


D(x) := max inf (19.13)
p [d][(][x, p][) = max] p x x (p)
∈U ∈U ∗∈ ∗ [∥][x][ −] [x][∗][∥][.]


For relative robustness in this new sense, we seek x that


min (19.14)
x S [max] p [d][(][x, p][)][.]
∈ ∈U


This variant is an attractive model for cases where we have time to revise
our decision variables x, perhaps only slightly, once p is revealed. In such
cases, we will want to choose an x that will not need much perturbation
under any scenario, i.e., we seek the solution to (19.14). This model can
also be useful for multi-period problems where revisions of decisions between
periods can be costly. Portfolio rebalancing problems with transaction costs
are examples of such settings.


Exercise 19.3 Formulate the relative robustness formulation for the optimization problem discussed in Exercise 19.2. Comment on the consequences
of the convexity of the function z [∗] (µ). Show that the relative robustness
problems for = p1, p2, . . ., pk and = conv(p1, p2, . . ., pk) are equivaU { } U
lent.


Exercise 19.4 Recall the setting in Exercise 19.2. Let x [∗] (µ) denote the
unique optimal solution of the problem for a given µ and obtain an explicit
expression for x [∗] (µ). Using this expression, formulate the variant of the
relative robustness problem given in (19.14).


19.3. DIFFERENT FLAVORS OF ROBUSTNESS 301


19.3.4 Adjustable Robust Optimization


Robust optimization formulations we saw above assume that the uncertain parameters will not be observed until all the decision variables are
determined and therefore do not allow for recourse actions that may be
based on realized values of some of these parameters. This is not always
the appropriate model for uncertain optimization problems. In particular,
multi-period decision models involve uncertain parameters some of which
are revealed during the decision process. After observing these parameters,
later stage decisions can respond to this new information and can correct
any sub-optimality resulting from less desirable outcomes in the uncertain
parameters. Adjustable robust optimization (ARO) formulations model
these decision environment and allow recourse action. These models are
closely related to, and in fact, partly inspired by the multi-stage stochastic
programming formulations with recourse.
ARO models were recently introduced in [5, 35] for uncertain linear programming problems. Consider, for example, the two-stage linear optimization problem given below whose first-stage decision variables x [1] need to be
determined now, while the second-stage decision variables x [2] can be chosen
after the uncertain parameters of the problem A [1], A [2], and b are realized:


min [:][ A][1][x][1][ +][ A][2][x][2] (19.15)
x [1],x [2][{][c][T][ x][1] [≤] [b][}][.]


Note that the second stage variables x [2] do not appear in the objective
function–this is what Ben-Tal et al. call the “normalized” form of the problem [5]. Problems with objective functions involving variables x [2] can be
reformulated as in (19.15) after introducing an artificial variable; see Exercise 19.5. Therefore, we can focus on this simpler and convenient form
without loss of generality.
Let U denote the uncertainty set for parameters A [1], A [2], and b. The
standard constraint robust optimization formulation for this problem seeks
to find vectors x [1] and x [2] that optimize the objective function and satisfy
the constraints of the problem for all possible realizations of the constraint
coefficients. In this formulation, both sets of variables must be chosen before
the uncertain parameters can be observed and therefore cannot depend on
these parameters. Consequently, the standard robust counterpart of this
problem can be written as follows:


min [:][ ∃][x][2] [:][ A][1][x][1][ +][ A][2][x][2] (19.16)
x [1] [{][c][T][ x][1] [∀][(][A][1][, A][2][, b][)][ ∈U] [≤] [b][}][.]

Note that this formulation is equivalent to the formulation we saw before,
i.e.
min [:][ A][1][x][1][ +][ A][2][x][2] (19.17)
x [1],x [2][{][c][T][ x][1] [≤] [b,][ ∀][(][A][1][, A][2][, b][)][ ∈U}][.]


We prefer (19.16) since it illustrates the difference between this formulation
and the adjustable version more clearly.
In contrast, the adjustable robust optimization formulation allows the
choice of the second-period variables x [2] to depend on the realized values of


302 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS


the uncertain parameters. As a result, the adjustable robust counterpart
problem is given as follows:


min [:][ ∀][(][A][1][, A][2][, b][)][ ∈U][,]
x [1] [{][c][T][ x][1] [∃][x][2] [≡] [x][2][(][A][1][, A][2][, b][) :][ A][1][x][1][ +][ A][2][x][2] [≤] [b][}][.]

(19.18)
The feasible set of the second problem is larger than that of the first
problem in general and therefore, the model is more flexible. ARO models
can be especially useful when robust counterparts are unnecessarily conservative. The price to pay for this additional modeling flexibility appears
to be the increased difficulty of the resulting ARO formulations. Even for
problems where the robust counterpart is tractable, it can happen that the
ARO formulation leads to an NP-hard problem. One of the factors that contribute to the added difficulty in ARO models is the fact that the feasible
set of the recourse actions (second-period decisions) depends not only on the
realization of the uncertain parameters but also the first-period decisions.
One way to overcome this difficulty is to consider simplifying assumptions
either on the uncertainty set, or on the dependence structure of recourse
actions to uncertain parameters. For example, if the recourse actions are
restricted to be affine functions of the uncertain parameters. While this restriction will likely give us suboptimal solutions, it may be the only strategy
to obtain tractable formulations.


Exercise 19.5 Consider the following adjustable robust optimization problem:


min 1 [x][1] [+] [c] 2 [T] [x][2] [:][ ∀][(][A][1][, A][2][, b][)][ ∈U][,]
x [1] [{][c][T] [∃][x][2] [≡] [x][2][(][A][1][, A][2][, b][) :][ A][1][x][1][ +] [A][2][x][2] [≤] [b][}][.]


Show how this problem can be expressed in the “normalized” form (19.18)
after introducing an artificial variable.

#### 19.4 Tools and Strategies for Robust Optimization


In this section we review a few of the commonly used techniques for the solution of robust optimization problems. The tools we discuss are essentially
reformulation strategies for robust optimization problems so that they can
be rewritten as a deterministic optimization problem with no uncertainty.
In these reformulations, we look for economy so that the new formulation is
not much bigger than the original, “uncertain” problem and tractability so
that the new problem can be solved efficiently using standard optimization
methods.
The variety of the robustness models and the types of uncertainty sets
rule out a unified approach. However, there are some common threads and
the material in this section can be seen as a guide to the available tools
which can be combined or appended with other techniques to solve a given
problem in the robust optimization setting.


19.4. TOOLS AND STRATEGIES FOR ROBUST OPTIMIZATION 303


19.4.1 Sampling


One of the simplest strategies for achieving robustness under uncertainty
is to sample several scenarios for the uncertain parameters from a set that
contains possible values of these parameters. This sampling can be done
with or without using distributional assumptions on the parameters and
produces a robust optimization formulation with a finite uncertainty set.
If uncertain parameters appear in the constraints, we create a copy of
each such constraint corresponding to each scenario. Uncertainty in the
objective function can be handled in a similar manner. Recall, for example,
the generic uncertain optimization problem given in (19.3):


minx f (x, p) (19.19)
G(x, p) ∈ K


If the uncertainty set is a a finite set, i.e., = p1, p2, . . ., pk, the robust
U U { }
formulation is obtained as follows:


mint,x t
t f (x, pi) 0, i = 1, . . ., k, (19.20)
            - ≥
G(x, pi) K, i = 1, . . ., k.
∈


Note that no reformulation is necessary in this case and the duplicated
constraints preserve the structural properties (linearity, convexity, etc.) of
the original constraints. Consequently, when the uncertainty set is a finite
set the resulting robust optimization problem is larger but theoretically no
more difficult than the non-robust version of the problem. The situation
is somewhat similar to stochastic programming formulations. Examples of
robust optimization formulations with finite uncertainty sets can be found,
e.g., in the recent book by Rustem and Howe [63].


19.4.2 Conic Optimization


Moving from finite uncertainty sets to to continuous sets such as intervals or
ellipsoids presents a theoretical challenge. The robust version of an uncertain
constraint that has to be satisfied for all values of the uncertain parameters
in a continuous set results in a semi-infinite optimization formulation. These
problems are called semi-infinite since there are infinitely many constraints–
indexed by the uncertainty set–but only finitely many variables.
Fortunately, it is possible to reformulate certain semi-infinite optimization problems using a finite set of conic constraints. Such reformulations
were already introduced in Chapter 9. We recall two constraint robustness
examples from that chapter:


  - The robust formulation for the linear programming problem

min c [T] x
(19.21)
s.t. a [T] x + b ≥ 0


304 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS


where the uncertain parameters [a; b] belong to the ellipsoidal uncertainty set



U = {[a; b] = [a [0] ; b [0] ] +



�k

uj[a [j] ; b [j] ], u 1
∥ ∥≤ }
j=1



is equivalent to the following second-order cone program:


minx,z c [T] x
s.t. a [T] j [x][ +][ b][j] = zj, j = 0, . . ., k,
(z0, z1, . . ., zk) Cq
∈

where Cq is the second-order cone defined in (9.2).


- The robust formulation for the quadratically constrained optimization
problem
min c [T] x
(19.22)
s.t. −x [T] (A [T] A)x + 2b [T] x + γ ≥ 0

where the uncertain parameters [A; b; γ] belong to the ellipsoidal uncertainty set



U = {[A; b; γ] = [A [0] ; b [0] ; γ [0] ] +



�k

uj[A [j] ; b [j] ; γ [j] ], u 1
∥ ∥≤ }
j=1



is equivalent to the following semidefinite program:



min
x,z [0],...,z [k],y,λ [c][T][ x]



s.t. A [j] x = z [j], j = 0, . . ., k,
(b [j] ) [T] x = y [j], j = 0, . . ., k,
λ 0,
 ≥   



[1] . . . y [k] + [1]

2 [γ][1] 2














        - [�]
γ [0] + 2y [0] λ y [1] + [1] . . . y [k] + [1] (z [0] ) [T]

 -  2 [γ][1] 2 [γ][k] 




        γ [0] + 2y [0] λ y [1] + [1]

2

 - 



2  - [�]

z [0] z [1] . . . z [k] I




[1]

2 [γ][k]









⪰ 0.



(z [1] ) [T]
...
(z [k] ) [T]



 λI

















y [1] + [1]



y [1] + [1]

2 [γ][1]
...
y [k] + [1] [γ][k]



Exercise 19.6 Consider a simple, two-variable LP with nonnegative variables and a single uncertain constraint a1x1 + a2x2 + b ≥ 0. [a1, a2, b] belong
to the following uncertainty set:



= [a1, a2, b] [a1, a2, b] = [1, 1, 1] + u1[ [1]
U { | 2



3 [,][ 0]][,][ ∥][u][∥≤] [1][}][.]




[1] [1]

2 [,][ 0][,][ 0] +][ u][2][[0][,] 3



Determine the robust formulation of this constraint and the projection of
the robust feasible set to the (x1, x2) space. Try to approximate this set
using the sampling strategy outlined above. Comment on the number of
samples required until the approximate robust feasible set is a relatively
good approximation of the true robust feasible set.


19.4. TOOLS AND STRATEGIES FOR ROBUST OPTIMIZATION 305


Exercise 19.7 When A = 0 for the quadratically constrained problem
(19.22) above, the problem reduces to a linearly constrained problem. Verify
that when A [j] = 0 for all j = 0, 1, . . ., k in the uncertainty set U, the robust
formulation of this problem reduces to the robust formulation of the linearly
constrained problem.


Exercise 19.8 Note that the quadratically constrained optimization problem given above can alternatively be parameterized as follows:


min c [T] x
s.t. −x [T] Σx + 2b [T] x + γ ≥ 0

where we used a positive semidefinite matrix Σ instead of A [T] A in the constraint definition. How can we define an ellipsoidal uncertainty set for this
parameterization of the problem? What are the potential advantages and
potential problems with using this parameterization?


19.4.3 Saddle-Point Characterizations


For the solution of problems arising from objective uncertainty, the robust
solution can be characterized using saddle-point conditions when the original problem satisfies certain convexity assumptions. The benefit of this
characterization is that we can then use algorithms such as interior-point
methods already developed and available for saddle-point problems.
As an example of this strategy consider the problem (19.5) from Section
19.3.2 and its robust formulation reproduced below:


minx S maxp f (x, p). (19.23)
∈ ∈U


We note that the dual of this robust optimization problem is obtained
by changing the order of the minimization and maximization problems:


max (19.24)
p [min] x S [f] [(][x, p][)][.]
∈U ∈


From standard results in convex analysis we have the following conclusion:


Lemma 19.1 If f (x, p) is a convex function of x and concave function of
p, if S and U are nonempty and at least one of them is bounded the optimal
values of the problems (19.23) and (19.24) coincide and there exists a saddle
point (x [∗], p [∗] ) such that


f (x [∗], p) ≤ f (x [∗], p [∗] ) ≤ f (x, p [∗] ), ∀x ∈ S, p ∈U.


This characterization is the basis of the robust optimization algorithms
given in [36, 71].


306 CHAPTER 19. ROBUST OPTIMIZATION: THEORY AND TOOLS


## Chapter 20

# Robust Optimization Models in Finance

As we discussed in the previous chapter, robust optimization formulations
address problems with input uncertainty. Since many financial optimization
problems involve future values of security prices, interest rates, exchange
rates, etc. which are not known in advance but can only be forecasted or
estimated, such problems fit perfectly into the framework of robust optimization. In this chapter, we give examples of robust optimization formulations
for a variety of financial optimization problems including portfolio selection,
risk management, and derivatives pricing/hedging.
We start with the application of constraint-robust optimization approach
to a multi-period portfolio selection problem:

#### 20.1 Robust Multi-Period Portfolio Selection


This section is adapted from an article by Ben-Tal, Margalit, and Nemirovski [6]. We consider an investor who currently holds the portfolio
x [0] = (x [0] 1 [, . . ., x] n [0] [),] [where] [x][0] i [denotes] [the] [number] [of] [shares] [of] [asset] [i] [in] [the]
portfolio, for i = 1, . . ., n. Also, let x [0] 0 [denote] [her] [cash] [holdings.] [She] [wants]
to determine how to adjust her portfolio in the next L investment periods
to maximize her total wealth at the end of period L.
We use the following decision variables to model this multi-period portfolio selection problem: b [l] i [denotes] [the] [number] [of] [additional] [shares] [of] [asset]
i bought at the beginning of period l and s [l] i [denotes] [the] [number] [of] [asset] [i]
shares sold at the beginning of period l, for i = 1, . . ., n and l = 1, . . ., L.
Then, the number of shares of asset i in the portfolio at the beginning of
period l, denoted x [l] i [,] [is] [given] [by] [the] [following] [simple] [equation:]

x [l] i [=][ x] i [l][−][1]      - s [l] i [+][ b] i [l][,] i = 1, . . ., n, l = 1, . . ., L. (20.1)

Let Pi [l] [denote] [the] [price] [of] [a] [share] [of] [asset] [i] [in] [period] [l][.] We make the
assumption that the cash account earns no interest so that P0 [l] [= 1][,][ ∀][l][.] [This]
is not a restrictive assumption–we can always reformulate the problem in
this way after a change of numeraire.


307


308 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE


We assume that proportional transaction costs are paid on asset purchases and sales and denote them with αi [l] [and] [β] i [l] [for] [sales] [and] [purchases,]
respectively, for asset i and period l. We assume that αi [l][’s] [and] [β] i [l][’s] [are] [all]
known at the beginning of period 0, although they can vary from period
to period and from asset to asset. Transaction costs are paid from the investor’s cash account and therefore, we have the following balance equation
for the cash account:



�n

(1 + βi)Pi [l][b] i [l][, l][ = 1][, . . ., L.]
i=1



x [l] 0 [=][ x][l] 0 [−][1] +



�n

i=1(1 − αi)Pi [l][s] i [l] [−]



This balance condition indicates that the cash available at the beginning
of period l is the sum of last period’s cash holdings and the proceeds from
sales (discounted by transaction costs) minus the cost of new purchases.
For technical reasons, we will replace the equation above with an inequality,
effectively allowing the investor “burn” some of her cash if she wishes to:



�n

(1 + βi)Pi [l][b] i [l][, l][ = 1][, . . ., L.]
i=1



x [l] 0 0 +

[≤] [x][l][−][1]



�n

i=1(1 − αi)Pi [l][s] i [l] [−]



The objective of the investor is to maximize her total wealth at the end
of period L. This objective can be represented as follows:



max



�n

Pi [L][x] i [L][.]
i=0



If we assume that all the future prices Pi [l] [are] [known] [at] [the] [time] [this]
investment problem is to be solved, we obtain the following deterministic
optimization problem:




  maxx,s,b ni=0 [P][ L] i [x] i [L]
x [l] 0 ≤ x [l] 0 [−][1] + [�][n] i=1 [(1][ −] [α][i][)][P][ l] i [s] i [l] [−] [�] i [n] =1 [(1 +][ β][i][)][P][ l] i [b] i [l][,]
x [l] i = x [l] i [−][1] - s [l] i [+][ b] i [l][,] i = 1, . . ., n,
s [l] i 0, i = 1, . . ., n,
≥
b [l] i 0, i = 1, . . ., n,
≥
x [l] i 0, i = 0, . . ., n,
≥










l = 1, . . ., L.



(20.2)
This is a linear programming problem that can be solved easily using the
simplex method or interior-point methods. The nonnegativity constraints
imposed by Ben-Tal et al. [6] on x [l] i [’s disallow short positions and borrowing.]
We note that these constraints are not essential to the model and some or all
of them can be removed to allow short sales on a subset of the assets or to
allow borrowing. Observe that the investor would, of course, never choose
to burn money if she is trying to maximize her final wealth. Therefore,
the cash balance inequalities will always be satisfied with equality in any
optimal solution of this problem.
In a realistic setting, we do not know Pi [l][’s] [in] [advance] [and] [therefore] [can-]
not solve the optimal portfolio allocation problem as the linear program we
developed above. Instead, we will develop a robust optimization model that


20.1. ROBUST MULTI-PERIOD PORTFOLIO SELECTION 309


incorporates the uncertainty in Pi [l][’s] [in] [(20.2).] [Since] [the] [objective] [function]
involves uncertain parameters Pi [L][,] [we] [first] [reformulate] [the] [problem] [as] [in]
(19.4) to move all the uncertainty to the constraints:



maxx,s,b,t�t
t ≤ ni=0 [P][ L] i [x] i [L]
x [l] 0 ≤ x [l] 0 [−][1] + [�][n] i=1 [(1][ −] [α][i][)][P][ l] i [s] i [l] [−] [�] i [n] =1 [(1 +][ β][i][)][P][ l] i [b] i [l][,]
x [l] i = x [l] i [−][1] - s [l] i [+][ b] i [l][,] i = 1, . . ., n,
s [l] i 0, i = 1, . . ., n,
≥
b [l] i 0, i = 1, . . ., n,
≥
x [l] i 0, i = 0, . . ., n,
≥










l = 1, . . ., L.



(20.3)
The first two constraints of this reformulation are the constraints that are
affected by uncertainty and we would like to find a solution that satisfies
these constraints for most possible realizations of the uncertain parameters
Pi [l][.] [To] [determine] [the] [robust] [version] [of] [these] [constraints,] [we] [need] [to] [choose]
an appropriate uncertainty set for these uncertain parameters. For this
purpose, we follow a 3-σ approach common in engineering and statistical
applications.
Future prices can be assumed to be random quantities. Let us denote



P1 [l]
...
Pn [l]



l
 with µ =



µ [l] 1
...
µ [l] n



 and its

















the expected value of the vector P [l] =









covariance matrix with V [l] . First, consider the constraint:



t ≤



�n

Pi [L][x] i [L][.]
i=0



Letting x [L] = (x [L] 1 [, . . ., x] n [L][), the expected value and the standard deviation of]
the rig�ht-hand-side expression are given by x [L] 0 [+(][µ][L][)][T][ x][L] [=][ x][L] 0 [+] [�] i [n] =1 [µ] i [L][x] i [L]
and (x [L] ) [T] V [L] x [L] . If Pi [L] [quantities] [are] [normally] [distributed,] [by] [requiring]

~~�~~
t ≤ E(RHS) − 3 STD(RHS) = x [L] 0 [+ (][µ][L][)][T][ x][L][ −] [3] (x [L] ) [T] V [L] x [L] (20.4)

             we would guarantee that the (random) inequality t ≤ ni=0 [P][ L] i [x] i [L] [would]
be satisfied more than 99% of the time. Therefore, we regard (20.4) as the
“robust” version of t ≤ [�] i [n] =0 [P][ L] i [x] i [L][.]
We can apply a similar logic to other constraints affected by uncertainty:



�n

(1 + βi)Pi [l][b] i [l][,] [l] [= 1][, . . ., L]
i=1



x [l] 0 0

[−] [x][l][−][1] ≤



�n

i=1(1 − αi)Pi [l][s] i [l] [−]



�n



where we moved x [l] 0 [−][1] to the left-hand-side to isolate the uncertain terms
on the right-hand-side of the inequality. In this case, the expected value
and the variance of the right-hand-side expression are given by the following
formulas:







= (µ [l] ) [T] Dα [l] [s][l][ −] [(][µ][l][)][T][ D] β [l] [b][l]



�n

(1 + βi)Pi [l][b] i [l]
i=1



�n



E




�n



i=1(1 − αi)Pi [l][s] i [l] [−]


310 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE




            - [�]

[�] s [l]
= (µ [l] ) [T] Dα [l] −Dβ [l] b [l]







,



and


Var




�n

i=1(1 − αi)Pi [l][s] i [l] [−]



=



�n

(1 + βi)Pi [l][b] i [l]
i=1



�T Dα [l]
Dβ [l]

  







        - [�]
s [l]
V [l][ �] Dα [l] −Dβ [l] b [l]








s [l]

b [l]



.



Above, Dα and Dβ are the diagonal matrices



(1 + β1 [l] [)]
...
(1 + βn [l] [)]











 .



Dα :=





(1 − α1 [l] [)]

 ...

(1 − αn [l] [)]





, and Dβ :=



Also, s [l] = (s [l] 1 [, . . ., s] n [l] [)][T][,] [and] [b][l] [= (][b][l] 1 [, . . ., b] n [l] [)][T][ .] [Replacing]



�n

(1 + βi)Pi [l][b] i [l][, l][ = 1][, . . ., L]
i=1



x [l] 0 0

[−] [x][l][−][1] ≤



�n

i=1(1 − αi)Pi [l][s] i [l] [−]



with

                - [�]

[�] s [l]
x [l] 0 [−][x][l] 0 [−][1] ≤ (µ [l] ) [T] Dα [l] −Dβ [l] b [l]




~~�~~ T ~~�~~
Dα [l]
Dβ [l]

  





~~�~~








 
 - ~~�~~

 
 - s [l]

3

- b [l]




~~�~~




  -  - ~~[�]~~
s [l]
V [l] Dα [l] −Dβ [l] b [l]



we obtain a “robust” version of the constraint. Once again, assuming normality in the distribution of the uncertain parameters, by satisfying this
robust constraint we can guarantee that the original constraint will be satisfied with probability more than 0.99.
The approach above corresponds to choosing the uncertainty sets for the
uncertain parameter vectors P [l] in the following manner:

    U [l] := {P [l] : (P [l]  - µ [l] ) [T] (V [l] ) [−][1] (P [l]  - µ [l] ) ≤ 3}, l = 1, . . ., L. (20.5)

The complete uncertainty set U for all the uncertain parameters is the Cartesian product of the sets U [l] defined as U = U [1] × . . . × U [L] .


Exercise 20.1 Let U [L] be as in (20.5). Show that



t ≤



�n

Pi [L][x] i [L][,] ∀P [L] ∈U [L]
i=0



if and only if




    t ≤ (µ [L] ) [T] x [L] - 3 (x [L] ) [T] V [L] x [L] .



Thus, our 3-σ approach is equivalent to the robust formulation of this constraint using an appropriate uncertainty set.
(Hint: You may first want to show that


U [L] = {µ [L] + (V [L] ) [1][/][2] u : ∥u∥≤ 3}.)


20.2. ROBUST PROFIT OPPORTUNITIES IN RISKY PORTFOLIOS311


The resulting problem has nonlinear constraints, because of the squareroots and quadratic terms within the square-roots as indicated in Exercise
20.1. Fortunately, however, these constraints can be written as second order
cone constraints and result in a second order cone optimization problem.


Exercise 20.2 A vector (y [0], y [1] ) ∈ IR×IR [k] belongs to the k +1 dimensional
second-order cone if it satisfies the following inequality:


y [0] y [1] 2.
≥∥ ∥


Constraints of the form above are called second-order cone constraints. Show
that the constraint

          t ≤ (µ [L] ) [T] x [L]           - 3 (x [L] ) [T] V [L] x [L]


can be represented as a second-order cone constraint using an appropriate
change of variables. You can assume that V [L] is a given positive definite
matrix.

#### 20.2 Robust Profit Opportunities in Risky Port- folios


Consider an investment environment with n financial securities whose future
price vector r ∈ IR [n] is a random variable. Let p ∈ IR [n] represent the current prices of these securities. Consider an investor who chooses a portfolio
x = (x1, . . ., xn) where xi denote the number of shares of security i in the
portfolio. If x satisfies
p [T] x < 0


meaning that the portfolio is formed with negative cash flow (by pocketing
money) and if the realization r˜ at the end of the investment period of the
random variable r satisfies
r˜ [T] x ≥ 0

meaning that the portfolio has a nonnegative value at the end, then the
investor would get to keep the money pocketed initially, and perhaps even
more. A type A arbitrage opportunity would correspond to the situation
when the ending portfolio value is guaranteed to be nonnegative, i.e., when
the investor can choose a portfolio x such that p [T] x < 0 and


Prob[r [T] x ≥ 0] = 1. (20.6)


Since arbitrage opportunities generally do not persist in financial markets, one might be interested in the alternative and weaker profitability
notion where the nonnegativity of the final portfolio is not guaranteed but
is highly likely. Consider, for example, the following relaxation of (20.6):


Prob[r [T] x ≥ 0] ≥ 0.99. (20.7)


312 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE


This approach can be formalized using a similar construction to what we
have seen in Section 20.1. Let µ and Σ represent the expected future price
vector and covariance matrix of the random vector r. Then, E(r [T] x) = µ [T] x
and STD(r [T] x) = ~~√~~ x [T] Σx.



Exercise 20.3 If r is a Gaussian random vector with mean µ and covariance
matrix Σ, then



Prob[r [T] x ≥ 0] ≥ 0.99 ⇔ µ [T] x − θ√



x [T] Σx ≥ 0,



where θ = Φ [−][1] (0.99) and Φ [−][1] (·) is the inverse map of standard normal
cumulative distribution function.


As Exercise 20.3 indicates, the inequality (20.6) can be relaxed as

µ [T] x − θ√x [T] Σx ≥ 0,



where θ determines the likelihood of the inequality being satisfied. Therefore, if we find an x satisfying



µ [T] x − θ√



x [T] Σx ≥ 0, p [T] x < 0



for a large enough positive value of θ we have an approximation of an arbitrage opportunity called a robust profit opportunity in [57]. Note that, by
relaxing the constraint p [T] x < 0 as p [T] x ≤ 0 or using p [T] x ≤−ε for some
ε - 0, we obtain a conic feasibility system. Therefore, the resulting system can be solved using the conic optimization approaches. These ideas are
explored in detail in [56, 57].



Exercise 20.4 Consider the robust profit opportunity formulation for a
given θ: µ [T] x − θ√x [T] Σx ≥ 0, p [T] x ≤ 0. (20.8)

In this exercise, we investigate the problem of finding the largest θ for which
(20.8) has a solution other than the zero vector. Namely, we want to solve



maxs.t. θ,x µ [T] x − θ√x [T] Σxθ ≥ 0, (20.9)

p [T] x ≤ 0.



This problem is no longer a convex optimization problem (Why?). However,
we can rewrite the first constraint as

µ [T] x
~~√~~ x [T] Σx ≥ θ.


Using the strategy we employed in Section 8.2, we can take advantage of the
homogeneity of the constraints in x and impose the normalizing constraint
x [T] Σx = 1 to obtain the following equivalent problem:



maxθ,x θ
s.t. µ [T] x − θ ≥ 0,
p [T] x ≤ 0,
x [T] Σx = 1.



(20.10)


20.3. ROBUST PORTFOLIO SELECTION 313


While we got rid of the fractional terms, we now have a nonlinear equality
constraint that creates nonconvexity for the optimization. We can now relax
the constraint x [T] Σx = 1 as x [T] Σx ≤ 1 and obtain a convex optimization
problem.
maxθ,x θ
s.t. µ [T] x θ 0,
                 - ≥ (20.11)
p [T] x ≤ 0,
x [T] Σx ≤ 1.

This relaxation can be expressed in conic form and solved using the methods
discussed in Chapter 9. However, this relaxation we solve is not equivalent
to (20.9) and its solution need not be a solution to that problem in general.
Find sufficient conditions under which the optimal solution of (20.11) satisfies x [T] Σx ≤ 1 with equality and therefore the relaxation is equivalent to
the original problem.


Exercise 20.5 Note that the fraction ~~√~~ µx [T][T] xΣx [in] [the] [θ][-maximization] [exer-]

cise above resembles the Sharpe ratio. Assume that one of the assets in
consideration is a riskless asset which has a return of rf . Show that the θmaximization problem is equivalent to maximizing the Sharpe ratio in this
case.

#### 20.3 Robust Portfolio Selection


This section is adapted from an article by T¨ut¨unc¨u and Koenig [36]. Recall
that Markowitz’ mean-variance optimization problem can be stated in the
following form that combines the reward and risk in the objective function:


max (20.12)
x [µ][T][ x][ −] [λx][T][ Σ][x.]
∈X

Here µi is an estimate of the expected return of security i, σii is the variance
of this return, σij is the covariance between the returns of securities i and j,
λ is a risk-aversion constant used to trade-off the reward (expected return)
and risk (portfolio variance). The set X is the set of feasible portfolios
which may carry information on short-sale restrictions, sector distribution
requirements, etc. Since such restrictions are typically predetermined, we
can assume that the set X is known without any uncertainty at the time
the problem is solved.
Recall that solving the problem above for different values of λ we can
obtain the efficient frontier of the set of feasible portfolios. The optimal
portfolio will be different for individuals with different risk-taking tendencies, but it will always be on the efficient frontier.
One of the limitations of this model is its need to accurately estimate
the expected returns and covariances. In [4], Bawa, Brown, and Klein argue that using estimates of the unknown expected returns and covariances
leads to an estimation risk in portfolio choice, and that methods for optimal
selection of portfolios must take this risk into account. Furthermore, the
optimal solution is sensitive to perturbations in these input parameters—a


314 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE


small change in the estimate of the return or the variance may lead to a
large change in the corresponding solution, see, for example, [50, 51]. This
property of the solutions is undesirable for many reasons. Most importantly,
results can be unintuitive and the performance often suffers as the inaccuracies in the inputs lead to severely inefficient portfolios. If the modeler
wants to periodically rebalance the portfolio based on new data, she may
incur significant transaction costs to do so as small changes in inputs may
dictate large changes in positions. Furthermore, using point estimates of the
expected return and covariance parameters do not respond to the needs of
a conservative investor who does not necessarily trust these estimates and
would be more comfortable choosing a portfolio that will perform well under
a number of different scenarios. Of course, such an investor cannot expect to
get better performance on some of the more likely scenarios, but may prefer
to accept that in exchange for insurance against more extreme cases. All
these arguments point to the need of a portfolio optimization formulation
that incorporates robustness and tries to find a solution that is relatively
insensitive to inaccuracies in the input data. Since all the uncertainty is in
the objective function coefficients, we seek an objective robust portfolio, as
outlined in the previous chapter.
For robust portfolio optimization we consider a model that allows return
and covariance matrix information to be given in the form of intervals. For
example, this information may take the form “the expected return on security j is between 8% and 10%” rather than claiming that it is, say, 9%.
Mathematically, we will represent this information as membership in the
following set:


U = {(µ, Σ) : µ [L] ≤ µ ≤ µ [U], Σ [L] ≤ Σ ≤ Σ [U], Σ ⪰ 0}, (20.13)

where µ [L], µ [U], Σ [L], Σ [U] are the extreme values of the intervals we just mentioned. Recall that the notation Σ ⪰ 0 indicates that the matrix Σ is a
symmetric and positive semidefinite matrix. This restriction is necessary
for Σ to be a valid covariance matrix.
The uncertainty intervals in (20.13) may be generated in different ways.
An extremely cautious modeler may want to use historical lows and highs
of certain input parameters as the range of their values. In a linear factor model of returns, one may generate different scenarios for factor return
distributions and combine these scenarios to generate the uncertainty set.
Different analysts may produce different estimates for these parameters and
one may choose the extreme estimates as the endpoints of the intervals. One
may choose a confidence level and then generate estimates of covariance and
return parameters in the form of prediction intervals.
Using the objective robustness model in (19.6), we want to find a portfolio that maximizes the objective function in (20.12) in the worst case
realization of the input parameters µ and Σ from their uncertainty set U in
(20.13). Given these considerations the robust optimization problem takes
the following form
max [min] (20.14)
x (µ,Σ) [µ][T][ x][ −] [λx][T][ Σ][x][}][.]
∈X [{] ∈U


20.4. RELATIVE ROBUSTNESS IN PORTFOLIO SELECTION 315


Since U is bounded, using classical results of convex analysis [60], it is easy
to show that (20.14) is equivalent to its dual where the order of the min and
the max is reversed:


min [max]
x∈X [{] (µ,Σ)∈U [−][µ][T][ x][ +][ λx][T][ Σ][x][}][.]

Furthermore, the solution to (20.14) is a saddle-point of the function f (x, µ, Σ) =
µ [T] x − λx [T] Σx and can be determined using the technique outlined in [36].


Exercise 20.6 Consider a special case of problem (20.14) where we make
the following assumptions


  - x ≥ 0, ∀x ∈X (i.e., X includes no-shorting constraints)

  - Σ [U] is positive semidefinite.

Under these assumptions, show that (20.14) reduces to the following singlelevel maximization problem:



max
x∈X




µ [L][�][T] x − λx [T] Σ [U] x. (20.15)



Observe that this new problem is a simple concave quadratic maximization
problem and can be solved easily using, for example, interior-point methods.
(Hint: Note that the objective function of (20.14) is separable in µ and Σ
and that x [T] Σx = [�] i,j [σ][ij][x][ij] [with] [x][ij] [=][ x][i][x][j] [when] [x][ ≥] [0.)]

[≥] [0]

#### 20.4 Relative Robustness in Portfolio Selection


We consider the following simple portfolio optimization example derived
from an example in [18]:



Example 20.1
max µ1x1 + µ2x2 + µ3x3
TE(x1, x2, x3) 0.10
≤
x1 + x2 + x3 = 1
x1 0, x2 0, x3 0.
≥ ≥ ≥

where



(20.16)



~~~~

x1 0.5
   x2 0.5
  x3



T ~~[]~~



0.1764 0.09702 0
 0.09702 0.1089 0
0 0 0



~~~~

x1 0.5
   x2 0.5
  x3



~~~~





~~~~





TE(x1, x2, x3) =












~~~~





This is essentially a two-asset portfolio optimization problem where the third
asset (x3) represents proportion of the funds that are not invested. The first
two assets have standard deviations of 42% and 33% respectively and a
correlation coefficient of 0.7. The “benchmark” is the portfolio that invests
funds half-and-half in the two assets. The function TE(x) represents the
tracking error of the portfolio with respect to the half-and-half benchmark


316 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE


and the first constraint indicates that this tracking error should not exceed
10%. The second constraint is the budget constraint, the third enforces no
shorting. We depict the projection of the feasible set of this problem onto
the space spanned by variables x1 and x 2 in Figure 20.4.
                  

1


0.9


0.8


0.7


0.6


0.5


0.4


0.3


0.2


0.1


0
0 0.2 0.4 0.6 0.8 1

x1


Figure 20.1: The feasible set of the MVO problem in (20.16)


We now build a relative robustness model for this portfolio problem.
We assume that the covariance matrix estimate is certain. We consider
a simple uncertainty set for expected return estimates consisting of three
scenarios represented with arrows in Figure 20.2. These three scenarios
correspond to the following values for (µ1, µ2, µ3): (6, 4, 0), (5, 5, 0), and
(4, 6, 0). The optimal solution when (µ1, µ2, µ3) = (6, 4, 0) is (0.831, 0.169, 0)
with an objective value of 5.662. Similarly, when (µ1, µ2, µ3) = (4, 6, 0) the
optimal solution is (0.169, 0.831, 0) with an objective value of 5.662. When
(µ1, µ2, µ3) = (5, 5, 0) all points between the previous two optimal solutions
are optimal with a shared objective value of 5.0. Therefore, the relative
robust formulation for this problem can be written as follows:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-315-0.png)

minx,t t
5.662 − (6x1 + 4x2) ≤ t
5.662 − (4x1 + 6x2) ≤ t
5.0 − (5x1 + 5x2) ≤ t
TE(x1, x2, x3) 0.10
≤
x1 + x2 + x3 = 1
x1 0, x2 0, x3 0.
≥ ≥ ≥



(20.17)



Instead of solving the problem where the optimal regret level is a variable
(t in the formulation), an easier strategy is to choose a level of regret that
can be tolerated and find portfolios that do not exceed this level of regret


20.5. MOMENT BOUNDS FOR OPTION PRICES 317


in any scenario. For example, choosing a maximum tolerable regret level of
0.75 we get the following feasibility problem:



Find x
s.t. 5.662 − (6x1 + 4x2) ≤ 0.75
5.662 − (4x1 + 6x2) ≤ 0.75
5.0 − (5x1 + 5x2) ≤ 0.75
TE(x1, x2, x3) 0.10
≤
x1 + x2 + x3 = 1
x1 0, x2 0, x3 0.
≥ ≥ ≥



(20.18)



This problem and its feasible set of solutions is illustrated in Figure 20.2.
The small shaded triangle represents the portfolios that have a regret level
of 0.75 or less under all three scenarios.



1


0.9


0.8


0.7


0.6


0.5


0.4


0.3


0.2


0.1



Relative robustness



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-316-0.png)







0
0 0.2 0.4 0.6 0.8 1

x1



Figure 20.2: Set of solutions with regret less than 0.75 in Example 20.1


Exercise 20.7 Interpret the objective function of (20.17) geometrically in
Figure 20.2. Verify that the vector x [∗] = (0.5, 0.5, 0) solves (20.17) with the
maximum regret level of t [∗] = 0.662.

#### 20.5 Moment Bounds for Option Prices


To price derivative securities, a common strategy is to first assume a stochastic process for the future values of the underlying process and then derive
a differential equation satisfied by the price function of the derivative security that can be solved analytically or numerically. For example, this is the
strategy used in the derivation of the Black-Scholes-Merton (BSM) formula
for European options.


318 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE


The prices obtained in this manner are sensitive to the model assumptions made to determine them. For example, the removal of the constant
volatility assumption used in the BSM derivation deems the resulting pricing
formulas incorrect. Since there is uncertainty in the correctness of the models or model parameters used for pricing derivatives, robust optimization
can be used as an alternative approach.
One variation considered in the literature assumes that we have reliable
estimates of the first few moments of the risk-neutral density of the underlying asset price but have uncertainty with respect to the actual shape of this
density. Then, one asks the following question: What distribution for the
risk neutral density with pre-specified moments produces the highest/lowest
price estimate for the derivative security? This is the approach considered in

[10] where the authors argue that the convex optimization models provide a
natural framework for addressing the relationship between option and stock
prices in the absence of distributional information for the underlying price
dynamics.
Another strategy, often called arbitrage pricing, or robust pricing, makes
no model assumptions at all and tries to produce lower and upper price
bounds by examining the known prices of related securities such as other
options on the same underlying, etc. This is the strategy we employed for
pricing forward start options in Section 10.4. Other examples of this strategy
include the work of Laurence and Wang [47].
Each one of these considerations lead to optimization problems. Some of
these problems are easy. For example, one can find an arbitrage bound for
a (possibly exotic) derivative security from a static super- or sub-replicating
portfolio by solving a linear optimization problem. Other robust pricing
and hedging problems can appear quite intractable. Fortunately, modern
optimization models and methods continue to provide efficient solution techniques for an expanding array of financial optimization problems including
pricing and hedging problems.

#### 20.6 Additional Exercises


Exercise 20.8 Recall that we considered the following two-stage stochastic
linear program with recourse in Section 16.2.



max (c [1] ) [T] x [1] + E[max c [2] (ω) [T] x [2] (ω)]
A [1] x [1] = b [1]

B [2] (ω)x [1] + A [2] (ω)x [2] (ω) = b [2] (ω)
x [1] ≥ 0, x [2] (ω) ≥ 0.



(20.19)



In this problem, it was assumed the uncertainty in ω was of “random” nature, and therefore, the stochastic programming approach was appropriate.
Now consider the case where ω is not a random variable but is known to
belong to an uncertainty set U. Formulate a two-stage robust linear program
with recourse using the ideas developed in Section 20.1. Next, assume that
B [2] and A [2] are certain (they do not depend on ω), but b [2] and c [2] are uncertain and depend affinely on ω: b [2] (ω) = b [2] + Pω and c [2] (ω) = c [2] + Rω,


20.6. ADDITIONAL EXERCISES 319


where b [2], c [2], P, R are (certain) vectors/matrices of appropriate dimension.
CanAlso,youassumesimplifythattheU =two-stage{ω : [�] irobust [d][i][w] i [2] [≤] linear [1][}] [for] program [some] [positive] with recourse [constants] under [d][i][.]
these assumptions?


Exercise 20.9 For a given constant λ, expected return vector µ, and a
positive definite covariance matrix Σ consider the following MVO problem:


max (20.20)
x [µ][T][ x][ −] [λx][T][ Σ][x,]
∈X

where X = {x : e [T] x = 1} with e = [1 1 . . . 1] [T] . Let z(µ, Σ) represent
the optimal value of this problem. Determine z(µ, Σ) as an explicit function
of µ and Σ. Next, assume that µ and Σ are uncertain and belong to the
uncertainty set := (µi, Σi) : i = 1, . . ., m, i.e., we have a finite number
U { }
of scenarios for µ and Σ. Assume also that z(µi, Σi) > 0 i. Now formulate
∀
the following robust optimization problem: Find a feasible portfolio vector
x such that the objective value with this portfolio under each scenario is
within 10% of the optimal objective value corresponding to that scenario.
Discuss how this problem can be solved. What would be a good objective
function for this problem?


320 CHAPTER 20. ROBUST OPTIMIZATION MODELS IN FINANCE


## Appendix A

# Convexity

Convexity is an important concept in mathematics, and especially in optimization, that is used to describe certain sets and certain functions. Convex
sets and convex functions are related but separate mathematical entities.
Let x and y be given points in some vector space. Then, for any λ ∈ [0, 1],
the point λx + (1 − λ)y is called a convex combination of x and y. The set
of all convex combinations of x and y is the line segment joining these two
points.
A subset S of a given vector space X is called a convex set if x ∈ S,
y ∈ S, and λ ∈ [0, 1] always imply that λx + (1 − λ)y ∈ S. In other words,
a convex set is characterized by the following property: for any two given
points in the set, the line segment connecting these two points lies entirely
in the set.
Polyhedral sets (or polyhedra) are sets defined by linear equalities and
inequalities. So, for example, the feasible region of a linear optimization
problem is a polyhedral set. It is a straightforward exercise to show that
polyhedral sets are convex.
Given a convex set S, a function f : S → IR is called a convex function
if ∀x ∈ S, y ∈ S and λ ∈ [0, 1] the following inequality holds:

f (λx + (1 − λ)y) ≤ λf (x) + (1 − λ)f (y).

We say that f is a strictly convex function if x ∈ S, y ∈ S and λ ∈ (0, 1)
implies the following strict inequality:


f (λx + (1 − λ)y) < λf (x) + (1 − λ)f (y).

A function f is concave if −f is convex. Equivalently, f is concave, if
∀x ∈ S, y ∈ S and λ ∈ [0, 1] the following inequality holds:

f (λx + (1 − λ)y) ≥ λf (x) + (1 − λ)f (y).

A function f is strictly concave if −f is strictly convex.
Given f : S → IR with S ⊂ X, epi(f )–the epigraph of f, is the following
subset of X × IR:

epi(f ) := {(x, r) : x ∈ S, f (x) ≤ r}.


321


322 APPENDIX A. CONVEXITY



f is a convex function if and only if epi(f ) is a convex set.
For a twice-continuously differentiable function f : S → IR with S ⊂ IR,
we have a simple characterization of convexity: f is convex on S if and only
if f [′′] (x) ≥ 0, ∀x ∈ S. For multivariate functions, we have the following
generalization: If f : S → IR with S ⊂ IR [n] is twice-continuously differentiable, then f is convex on S if and only if ∇ [2] f (x) is positive semidefinite for all x S. Here, f (x) denotes the (symmetric) Hessian matrix
of f ; namely, ∈� 2f (x)� ∇ [2] ∂ [2] f (x) [Recall] [that] [a] [symmetric] [matrix]
∇ ij [=] ∂xi∂xj [,][ ∀][i, j][.]

H ∈ IR [n][×][n] is positive semidefinite (positive definite) if y [T] Hy ≥ 0, ∀y ∈ IR [n]

(y [T] Hy - 0, ∀ y ∈ IR [n], y = 0).
The following theorem is one of the many reasons for the importance of
convex functions and convex sets for optimization:


Theorem A.1 Consider the following optimization problem:


(OP) minx f (x) (A.1)
s.t. x ∈ S

If S is a convex set and if f is a convex function of x on S, then all local
optimal solutions of OP are also global optimal solutions.


## Appendix B

# Cones

A cone is a set that is closed under positive scalar multiplication. In other
words, a set C is a cone if λx ∈ C for all λ ≥ 0 and x ∈ C. A cone is called
pointed if it does not include any lines. We will generally be dealing with
closed, convex, and pointed cones. Here are a few important examples:


Cl := x IR [n] : x 0, the non-negative orthant. In general, any set

  - { ∈ ≥ }
of the form C := {x ∈ IR [n] : Ax ≥ 0} for some matrix A ∈ IR [m][×][n] is
called a polyhedral cone. The subscript l is used to indicate that this
cone is defined by linear inequalities.


Cq := x = (x0, x1, . . ., xn) IR [n][+1] : x0 (x1, . . ., xn), the

  - { ∈ ≥∥ ∥}
second-order cone. This cone is also called the quadratic cone (hence
the subscript q), Lorentz cone, and the ice-cream cone.








x11 x1n

     - · ·
... ... ...
xn1 xnn

     - · ·



n n T
 ∈ IR × : X = X, X is positive semidefinite



,








Cs :=







X =










the cone of symmetric positive semidefinite matrices.



If C is a cone in a vector space X with an inner product denoted by ⟨·, ·⟩,
then its dual cone is defined as follows:


C [∗] := {x ∈ X : ⟨x, y⟩≥ 0, ∀y ∈ C}.

It is easy to see that the nonnegative orthant in IR [n] (with the usual inner
product) is equal to its dual cone. The same holds for the second-order
cone and the cone of symmetric positive semidefinite matrices, but not for
general cones.
The polar cone is the negative of the dual cone, i.e.,


C [P] := {x ∈ X : ⟨x, y⟩≤ 0, ∀y ∈ C}.


323


324 APPENDIX B. CONES


## Appendix C

# A Probability Primer

One of the most basic concepts in probability theory is a random experiment,
which is an experiment whose outcome can not be determined in advance. In
most cases, however, one has a (possibly infinite) set of all possible outcomes
of the event; we call this set the sample space of the random experiment. For
example, flipping a coin is a random experiment, so is the score of the next
soccer game between Japan and Korea. The set Ω= {heads, tails} is the
sample space of the first experiment, Ω= IN × IN with IN = {0, 1, 2, . . .} is
the sample space for the second experiment.
Another important concept is an event: a subset of the sample space.
It is customary to say that an event occurs if the outcome of the random
experiment is in the corresponding subset. So, “Japan beats Korea” is an
event for the second random experiment of the previous paragraph. A class
F of subsets of a sample space Ωis called a field if it satisfies the following
conditions:


i) Ω ∈F,

ii) A ∈F implies that A [c] ∈F, where A [c] is the complement of A,

iii) A, B ∈F implies A ∪ B ∈F.

The second and third conditions are known as closure under complements
and (finite) unions. If, in addition, F satisfies

iv) A1, A2, . . . implies i=1 [A][i]
∈F ∪ [∞] [∈F][,]

then F is called a σ-field. The condition (iv) is closure under countable
unions. Note that, for subtle reasons, Condition (iii) does not necessarily
imply Condition (iv).
A probability measure or distribution P is a real-valued function defined
on a field F (whose elements are subsets of the sample space Ω), and satisfies
the following conditions


i) 0 ≤ P (A) ≤ 1, for ∀A ∈F,

ii) P (∅) = 0, and P (Ω) = 1,


325


326 APPENDIX C. A PROBABILITY PRIMER


iii) If A1, A2, . . . is a sequence of disjoint sets in and if i=1 [A][i]
F ∪ [∞] [∈F][, then]



P (∪i [∞] =1 [A][i][) =]



�∞

P (Ai).
i=1



The last condition above is called countable additivity.
A probability measure is said to be discrete if Ωhas countably many (and
possibly finite) number of elements. A density function f is a nonnegative
valued integrable function that satisfies

             
f (x)dx = 1.
Ω


A continuous probability distribution is a probability defined by the following relation:




      P [X ∈ A] =



f (x)dx,
A



for a density function f .
The collection Ω, F (a σ-field in Ω), and P ( a probability measure on
F) is called a probability space.
Now we are ready to define a random variable. A random variable X is
a real-valued function defined on the set Ω [1] . Continuing with the soccer
example, the difference between the goals scored by the two teams is a
random variable, and so is the “winner”, a function which is equal to, say,
1 if the number of goals scored by Japan is higher, 2 if the number of goals
scored by Korea is higher, and 0 if they are equal. A random variable is said
to be discrete (respectively, continuous) if the underlying probability space
is discrete (respectively, continuous).
The probability distribution of a random variable X is, by definition, the
probability measure PX in the probability space (Ω,, P ):
F


PX(B) = P [X B].
∈


The distribution function F of the random variable X is defined as:


F (x) = P [X ≤ x] = P [X ∈ (−∞, x]] .


For a continuous random variable X with the density function f,

                x
F (x) = f (x)dx

−∞

and therefore f (x) = d
dx [F] [(][x][).]
A random vector X = (X1, X2, . . ., Xk) is a k-tuple of random variables,
or equivalently, a function from Ωto IR [k] that satisfies a technical condition


1Technically speaking, for X to be a random variable, it has to satisfy the condition that
for each B ∈B, the Euclidean Borel field on IR, the set {ω : X(ω) ∈ B} =: X [−][1] (B) ∈F .
This is a purely technical requirement which is met for discrete probability spaces (Ωis
finite or countably infinite) and by any function that we will be interested in.


327


similar to the one mentioned in the footnote. The joint distribution function
F of random variables X1, . . ., Xk is defined by


F (x1, . . ., xk) = PX[X1 x1, . . ., Xk xk].
≤ ≤


In the special case of k = 2 we have


F (x1, x2) = PX[X1 x1, X2 x2].
≤ ≤


Given the joint distribution function of random variables X1 and X2, their
marginal distribution functions are given by the following formulas:


FX1(x1) = x2lim→∞ [F] [(][x][1][, x][2][)]


and
FX2(x2) = x1lim→∞ [F] [(][x][1][, x][2][)][.]

We say that random variables X1 and X2 are independent if


F (x1, x2) = FX1(x1)FX2(x2)


for every x1 and x2.
The expected value (expectation, mean) of the random variable X is
defined by




     E[X] =



xdF (x)
Ω



=



��

  - x∈Ω [xP] [[][X] [=][ x][]] if X is discrete
Ω [xf] [(][x][)][dx] if X is continuous



(provided that the integrals exist) and is denoted by E[X]. For a function
g(X) of a random variable, the expected value of g(X) (which is itself a
random variable) is given by




     E[g(X)] =




      xdFg(x) =
Ω



g(x)dF (x).
Ω



The variance of a random variable X is defined by

                   Var[X] = E (X E[X]) [2][�]
                 
= E[X [2] ] − (E[X]) [2] .


The standard deviation of a random variable is the square-root of its variance.
For two jointly distributed random variables X1 and X2, their covariance
is defined to be


Cov(X1, X2) = E [(X1 E[X1])(X2 E[X2])]
                -                 
= E[X1X2] E[X1]E[X2]
                  

328 APPENDIX C. A PROBABILITY PRIMER



The correlation coefficient of two random variables is the ratio of their covariance to the product of their standard deviations.
For a collection of random variables X1, . . ., Xn, the expected value of
the sum of these random variables is equal to the sum of their expected
values: - 






E




�n



Xi
i=1



=



�n



E[Xi].
i=1



The formula for the variance of the sum of the random variables X1, . . ., Xn
is a bit more complicated:







Cov(Xi, Xj).
1≤i<j≤n



Var




�n

Xi
i=1



=



�n



�n 
Var[Xi] + 2
i=1 1 i<j


## Appendix D

# The Revised Simplex Method

As we discussed in Chapter 2, in each iteration of the simplex method, we
first choose an entering variable looking at the objective row of the current
tableau, and then identify a leaving variable by comparing the ratios of the
numbers on the right-hand-side and the column for the entering variable.
Once these two variables are identified we update the tableau. Clearly, the
most time-consuming job among these steps of the method is the tableau
update. If we can save some time on this bottleneck step then we can make
the simplex method much faster. The revised simplex method is a variant of
the simplex method developed with precisely that intention.


The crucial question here is whether it is necessary to update the whole
tableau in every iteration. To answer this question, let us try to identify
what parts of the tableau are absolutely necessary to run the simplex algorithm. As we mentioned before, the first task in each iteration is to find an
entering variable. Let ue recall how we do that. In a maximization problem,
we look for a nonbasic variable with a positive rate of improvement. In
terms of the tableau notation, this translates into having a negative coefficient in the objective row, where Z is the basic variable.


To facilitate the discussion below let us represent a simplex tableau in an
algebraic form, using the notation from Section 2.4.1. As before, we consider
a linear programming problem of the form:


max c x

Ax ≤ b

x ≥ 0.


After adding the slack variables and choosing them as the initial set of basic
variables we get the following “initial” or “original” tableau:


329


330 APPENDIX D. THE REVISED SIMPLEX METHOD


|Current<br>basic<br>variables|Coefficient of|Col3|Col4|RHS|
|---|---|---|---|---|
|Current<br>basic<br>variables|Z|Original<br>nonbasics|Original<br>basics|Original<br>basics|
|Z|1|−c|0|0|
|xB|0|A|I|b|



Note that we wrote the objective function equation Z = c x as Z − c x = 0
to keep variables on the left-hand-side and the constants on the right. In
the matrix form this can be written as:








1 −c 0
0 A I




 - []



Z
 x
xs







 =




0
b



.



Pivoting, which refers to the algebraic operations performed by the simplex
method in each iteration to get a representation of the problem in a particular form, can be expressed in matrix form as a premultiplication of the
original matrix representation of the problem with an appropriate matrix.
If the current basis matrix is B, the premultuplying matrix happens to be
the following:

            -             1 cBB [−][1]







0 B [−][1]



.



Multiplying this matrix with the matrices in the matrix form of the equations
above we get:

   - ��   -   -   1 cBB [−][1] 1 c 0 1 cBB [−][1] A c cBB [−][1]












1 cBB [−][1] A − c cBB [−][1]

[1] [1]



0 B [−][1] A B [−][1]



,



0 B [−][1]



��
1 −c 0
0 A I



=



and

        1 cBB [−][1]

0 B [−][1]



��
0
b











=




cBB [−][1] b
B [−][1] b



which gives us the matrix form of the set of equations in each iteration
represented with respect to the current set of basic variables:




cBB [−][1] b
B [−][1] b




1 cBB [−][1] A − c cBB [−][1]

0 B [−][1] A B [−][1]




- []

Z
 x
xs





 =







In the tableau form, this is observed in the following tableau:


|Current<br>basic<br>variables|Coefficient of|Col3|Col4|RHS|
|---|---|---|---|---|
|Current<br>basic<br>variables|Z|Original<br>nonbasics<br>|Original<br>basics<br>|Original<br>basics<br>|
|Z|1|cBB−1A −c|cBB−1|cBB−1b|
|xB|0|<br>B−1A|B−1|B−1b|


331


Equipped with this algebraic representation of the simplex tableau, we
continue our discussion of the revised simplex method. Recall that, for a
maximization problem, an entering variable must have a negative objective
row coefficient. Using the tableau above, we can look for entering variables
by checking whether:


1. cBB [−][1] ≥ 0

2. cBB [−][1] A − c ≥ 0

Furthermore, we only need to compute the parts of these vectors corresponding to nonbasic variables, since the parts corresponding to basic variables
will be zero. Now, if both inequalities above are satisfied, we stop concluding that we found an optimal solution. If not, we pick a nonbasic variable,
say xk, for which the updated objective row coefficient is negative, to enter the basis. So in this step we use the updated objective function row.


Next step is to find the leaving variable. For that, we use the updated
column k for the variable xk and the updated right-hand-side vector.
If the column that corresponds to xk in the original tableau is Ak, then the
updated column is A [¯] k = B [−][1] Ak and the updated RHS vector is b [¯] = B [−][1] b.


Next, we make a crucial observation: For the steps above, we do not need
to calculate the updated columns for the nonbasic variables that are not selected to enter the basis. Notice that, if there are a lot of nonbasic variables
(which would happen if there were many more variables than constraints)
this would translate into substantial savings in terms of computation time.
However, we need to be able to compute A [¯] k = B [−][1] Ak which requires the
matrix B [−][1] . So, how do we find B [−][1] in each iteration? Taking the inverse
from scratch in every iteration would be too expensive, instead we can keep
track of B [−][1] in the tableau as we iterate the simplex method. We will also
keep track of the updated RHS b [¯] = B [−][1] b. Finally, we will keep track of
the expression π = cBB [−][1] . Looking at the tableau in the previous page,
we see that the components of π are just the updated objective function
coefficients of the initial basic variables. The components of the vectors π
are often called the shadow prices, or dual prices.


Now we are ready to give an outline of the revised simplex method:


Step 0. Find an initial feasible basis B and compute B [−][1], b [¯] = B [−][1] b,
and π = cBB [−][1] .


Now assuming that we are given the current basis B and we know B [−][1],
¯b = B [−][1] b, and π = cBB [−][1] let us try to describe the iterative steps of the
revised simplex method:


Step 1. For each nonbasic variable xi calculate c¯i = ci cBB [−][1] Ai =
                         ci πAi. If c¯i 0 for all nonbasic variables xi, then STOP, the current

 - ≤


332 APPENDIX D. THE REVISED SIMPLEX METHOD


basis is optimal. Otherwise choose a variable xk such that c¯k - 0.


Step 2. Compute the updated column A [¯] k = B [−][1] Ak and perform the
ratio test, i.e., find

¯bi
min .
a¯ik>0 [{] a¯ik }

Here a¯ik and [¯] bi denote the i [th] entry of the vectors A [¯] k and b [¯], respectively. If
a¯ik 0 for every row i, then STOP, the problem is unbounded. Otherwise,
≤
choose the basic variable of the row that gives the minimum ratio in the ratio
test (say row r) as the leaving variable.


The pivoting step is where we achieve the computational savings:


Step 3. Pivot on the entry a¯rk in the following truncated tableau:

|Current<br>basic<br>variables|Coefficient of|Col3|RHS|
|---|---|---|---|
|Current<br>basic<br>variables|xk|Original<br>basics<br>|Original<br>basics<br>|
|Z<br>|−¯ck<br>|π = cBB−1|cBB−1b|
|...<br>xBr<br>...|...<br>¯ark<br>...|B−1|B−1b|



Replace the current values of B [−][1], [¯] b, and π with the matrices and vectors
that appear in their respective positions after pivoting. Go back to Step 1.


Once again, notice that when we use the revised simplex method, we
work with a truncated tableau. This tableau has m +2 columns; m columns
corresponding to the initial basic variables, one for the entering variable, and
one for the right hand side. In the standard simplex method, we work with
n + 1 columns, n of them for all variables, and one for the RHS vector. For
a problem that has many more variables (say, n = 50, 000) than constraints
(say, m = 10, 000) the savings are very significant.


An Example
Now we apply the revised simplex method described above to a linear
programming problem. We will consider the following problem:


Maximize Z = x1 + 2x2 + x3 2x4

            subject to:
2x1 + x2 + x3 + 2x4 + x6 = 2

     x1 + 2x2 + x3 + x5 + x7 = 7

      x1 + x3 + x4 + x5 + x8 = 3


x1, x2, x3, x4, x5, x6, x7, x8 0.
≥

The variables x6, x7, and x8 form a feasible basis and we will start the
algorithm with this basis. Then the initial simplex tableau is as follows:


333


Once a feasible basis B is determined, the first thing to do in the revised
simplex method is to calculate the quantities B [−][1], [¯] b = B [−][1] b, and π =
cBB [−][1] . Since the basis matrix B for the basis above is the identity, we
calculate these quantities easily:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-332-0.png)

B [−][1] = I,









,



¯b = B [−][1] b =



2
 7
3



π = cBB [−][1] = [0 0 0] I = [0 0 0].



Above, I denotes the identity matrix of size 3. Note that, cB, i.e., the
sub-vector of the objective function vector c = [1 2 1 - 2 0 0 0 0] [T] that
corresponds to the current basic variables, consists of all zeroes.
Now we calculate c¯i values for nonbasic variables using the formula c¯i =
ci πAi, where Ai refers to the i [th] column of the initial tableau. So,
 






−2
 −1
1







c¯1 = c1 πA1 = 1 [0 0 0]
   -    






 = 1,




 = 2,



c¯2 = c2 πA2 = 2 [0 0 0]
   -    


1
 2
0



and similarly,
c¯3 = 1, c¯4 = 1, c¯5 = 0.
                
The quantity c¯i is often called the reduced cost of the variable xi and it tells
us the rate of improvement in the objective function when xi is introduced
into the basis. Since c¯2 is the largest of all c¯i values we choose x2 as the
entering variable.


To determine the leaving variable, we need to compute the updated
column A [¯] 2 = B [−][1] A2:





1
 2
0





 .





 =



A¯2 = B [−][1] A2 = I





1
 2
0



Now using the updated right-hand-side vector [¯] b = [2 7 3] [T] we perform the
ratio test and find that x6, the basic variable in the row that gives the minimum ratio has to leave the basis. (Remember that we only use the positive


334 APPENDIX D. THE REVISED SIMPLEX METHOD


entries of A [¯] 2 in the ratio test, so the last entry, which is a zero, does not
participate in the ratio test.)


Up to here, what we have done was exactly the same as in regular simplex, only the language was different. The next step, the pivoting step, is
going to be significantly different. Instead of updating the whole tableau, we
will only update a reduced tableau which has one column for the entering
variable, three columns for the initial basic variables, and one more column
for the RHS. So, we will use the following tableau for pivoting:


As usual we pivot in the column of the entering variable and try to get
a 1 in the position of the pivot element, and zeros elsewhere in the column.
After pivoting we get:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-333-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-333-1.png)

Now we can read the basis inverse B [−][1], updated RHS vector [¯] b, and the
shadow prices π for the new basis from this new tableau. Recalling the
algebraic form of the simplex tableau we discussed above, we see that the new
basis inverse lies in the columns corresponding to the initial basic variables,
so











B [−][1] =



1 0 0
 −2 1 0
0 0 1



 .



Updated values of the objective function coefficients of initial basic variables
and the updated RHS vector give us the π and [¯] b vectors we will use in the
next iteration:











¯b =



2
 3
3



, π = [2 0 0].



Above, we only updated five columns and did not worry about the four
columns that correspond to x1, x3, x4, and x5. These are the variables that
are neither in the initial basis, nor are selected to enter the basis in this
iteration.


335


Now, we repeat the steps above. To determine the new entering variable,
we need to calculate the reduced costs c¯i for nonbasic variables:







c¯1 = c1 πA1 = 1 [2 0 0]
   -    


−2
 −1
1







1
 1
1





 = 5




 = −1,



c¯3 = c3 πA3 = 1 [2 0 0]
   -    


and similarly,

c¯4 = 6, c¯5 = 0, and c¯6 = 2.

        -        
When we look at the c¯i values we find that only x1 is eligible to enter. So,
         we generate the updated column A [¯] 1 = B [−][1] A1:











−2
 −1
0





 =





−2
 3
1





 .



A¯1 = B [−][1] A1 =





1 0 0
 −2 1 0
0 0 1



The ratio test indicates that x7 is the leaving variable:




[3]

[3] 3 [,] 1



min
{ [3] 3



1 [}][ = 1][.]



Next, we pivot on the following tableau:


And we obtain:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-334-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-334-1.png)











Once again, we read new values of B [−][1], [¯] b, and π from this tableau:







2 0
3 3

- [1] 3 13 0

- [2] 2 [1]





4
 1
2





, π = [ 5

   - [4] 3 3 [0]]



B [−][1] =



3

 - [1]


[2]



3 13 0

[2] 23 3 1

 - [1]





, ¯b =



3 1


336 APPENDIX D. THE REVISED SIMPLEX METHOD


We start the third iteration by calculating the reduced costs:







5

c¯3 = c3 πA3 = 1 [
   -    -    - [4] 3 3 [0]]



1
 1
1









 = 2
3



 = 2
3 [,]



5

c¯4 = c4 πA4 = 2 [
   -    -    -    - [4] 3 3 [0]]



2
 0
1



and similarly,



c¯5 =
  - [2] 3



c¯6 = [4]

[2] 3 [,] 3




[4] [and] [c][¯][7] [=][ −] [5]

3 [,] 3



3 [.]



So, x6 is chosen as the next entering variable. Once again, we calculate the
updated column A [¯] 6:







3 23 0

- [1] 1 0

3 3

- [2] 2 [1]





1
 0
0





 =







3


3

- [2] 2



3
2
3



A¯6 = B [−][1] A6 =



3

 - [1]


[2]



1 0
3 3

[2] 2 1

3 3

 - [1]









3

 - [1]


[2]





 .



1
3



The ratio test indicates that x8 is the leaving variable, since it is the basic
variable in the only row where A [¯] 6 has a positive coefficient. Now we pivot
on the following tableau:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-335-0.png)













Pivoting yields:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v1/Optimization Methods in Finance_assets/Optimization-Methods-in-Finance.pdf-335-1.png)

The new value of the vector π is given by:



π = [0 1 2].


Using π we compute


c¯3 = c3 πA3 = 1 [0 1 2]
          -           

c¯4 = c4 πA4 = 2 [0 1 2]
          -          -          


2
 0
1







1
 1
1









 = −2



 = −4


337







c¯5 = c5 πA5 = 0 [0 1 2]
   -    

c¯7 = c7 πA7 = 0 [0 1 2]
   -    

c¯8 = c8 πA8 = 0 [0 1 2]
   -    


0
 1
1



0
 0
1







0
 1
0









 = −3



 = −1



 = −2



Since all the ¯ci values are negative we conclude that the last basis is optimal.
The optimal solution is:


x1 = 3, x2 = 5, x6 = 3, x3 = x4 = x5 = x7 = x8 = 0, and, z = 13.


Exercise D.1 Consider the following linear programming problem:


max Z = 20x1 + 10x2
x1 x2 + x3 = 1

         3x1 + x2 + x4 = 7


x1 0, x2 0, x3 0, x4 0.
≥ ≥ ≥ ≥

The initial simplex tableau for this problem is given below:

|Basic<br>var.|Coefficient of|Col3|RHS|
|---|---|---|---|
|Basic<br>var.|Z|x1<br>x2<br>x3<br>x4|x1<br>x2<br>x3<br>x4|
|Z|1|-20<br>-10<br>0<br>0|0|
|x3<br>x4|0<br>0|1<br>-1<br>1<br>0<br>3<br>1<br>0<br>1|1<br>7|



Optimal set of basic variables for this problem happen to be x2, x3 .
{ }
Write the basis matrix B for this set of basic variables and determine its
inverse. Then, using the algebraic representation of the simplex tableau
given in Chapter D, determine the optimal tableau corresponding to this
basis.


Exercise D.2 One of the insights of the algebraic representation of the
simplex tableau we considered in Chapter D is that, the simplex tableau
at any iteration can be computed from the initial tableau and the matrix
B [−][1], the inverse of the current basis matrix. Using this insight, one can
easily answer many types of “what if” questions. As an example, consider
the LP problem given in the previous exercise. What would happen if the
right-hand-side coefficients in the initial representation of the example above
were 2 and 5 instead of 1 and 7? Would the optimal basis x2, x3 still be
{ }
optimal? If yes, what would the new optimal solution and new optimal
objective value be?


338 APPENDIX D. THE REVISED SIMPLEX METHOD


# Bibliography


[1] A. Altay-Salih, M. C¸. Pınar, and S. Leyffer. Constrained nonlinear programming for volatility estimation with garch models. SIAM Review,
45(3):485–503, September 2003.


[2] F. Anderson, H. Mausser, D. Rosen, and S. Uryasev. Credit risk optimization with conditional value-at-risk criterion. Mathematical Programming B, 89:273–291, 2001.


[3] Y. Baba, R. F. Engle, D. Kraft, and K. F. Kroner. Multivariate simultaneous generalized arch. Technical report, Department of Economics,
University of California San Diego, 1989.


[4] V. S. Bawa, S. J. Brown, and R. W. Klein. Estimation Risk and Optimal
Portfolio Choice. North-Holland, Amsterdam, Netherlands, 1979.


[5] A. Ben-Tal, A. Goyashko, E. Guslitzer, and A. Nemirovski. Adjustable
robust solutions of uncertain linear programs. Mathematical Programming, 99(2):351–376, 2004.


[6] A. Ben-Tal, T. Margalit, and A. N. Nemirovski. Robust modeling
of multi-stage portfolio problems. In H. Frenk, K. Roos, T. Terlaky,
and S. Zhang, editors, High Performance Optimization, pages 303–328.
Kluwer Academic Publishers, 2002.


[7] A. Ben-Tal and A. N. Nemirovski. Robust convex optimization. Mathematics of Operations Research, 23(4):769–805, 1998.


[8] A. Ben-Tal and A. N. Nemirovski. Robust solutions of uncertain linear
programs. Operations Research Letters, 25(1):1–13, 1999.


[9] M. B´enichou, J.M. Gauthier, Girodet P., G. Hentges, G. Ribi`ere, and
Vincent O. Experiments in mixed-integer linear programming. Mathematical Programming, 1:76–94, 1971.


[10] D. Bertsimas and I. Popescu. On the relation between option and stock
prices: A convex programming approach. Operations Research, 50:358–
374, 2002.


[11] D. Bienstock. Computational study of a family of mixed-integer
quadratic programming problems. Mathematical Programming A,
74:121–140, 1996.


339


340 BIBLIOGRAPHY


[12] J.R. Birge and F. Louveaux. Introduction to Stochastic Programming.
Springer, 1997.


[13] F. Black and R. Litterman. Global portfolio optimization. Financial
Analysts Journal, pages 28–43, 1992.


[14] P. T. Boggs and J. W. Tolle. Sequential quadratic programming. Acta
Numerica, 4:1–51, 1996.


[15] T. Bollerslev. Generalized autoregressive conditional heteroskedasticity.
Journal of Econometrics, 31:307–327, 1986.


[16] T. Bollerslev, R. F. Engle, and D. B. Nelson. Garch models. In R. F.
Engle and D. L. McFadden, editors, Handbook of Econometrics, volume 4, pages 2961–3038. Elsevier, 1994.


[17] D. R. Cari˜no, T. Kent, D. H. Myers, C. Stacy, M. Sylvanus, A.L. Turner,
K. Watanabe, and W. Ziemba. The Russell-Yasuda Kasai model: An
asset/liability model for a Japanese insurance company using multistage
stochastic programming. Interfaces, 24:29–49, 1994.


[18] S. Ceria and R. Stubbs. Robust portfolio selection... submitted, 2005.


[19] V. Chv´atal. Linear Programming. W. H. Freeman and Company, New
York, 1983.


[20] T. F. Coleman, Y. Kim, Y. Li, and A. Verma. Dynamic hedging in a
volatile market. Technical report, Cornell Theory Center, 1999.


[21] T. F. Coleman, Y. Li, and A. Verma. Reconstructing the unknown
volatility function. Journal of Computational Finance, 2(3):77–102,
1999.


[22] G. Cornu´ejols, M. L. Fisher, and G. L. Nemhauser. Location of bank
accounts to optimize float: An analytic study of exact and approximate
algorithms. Management Science, 23:789–810, 1977.


[23] J. Cox, S. Ross, and M. Rubinstein. Option pricing: A simplified approach. Journal of Financial Economics, 7(3):229–263, 1979.


[24] M. A. H. Dempster and A. M. Ireland. A financial expert decision
support system. In G. Mitra, editor, Mathematical Models for Decision
Support, volume F48 of NATO ASI Series, pages 415–440. 1988.


[25] R. F. Engle. Autoregressive conditional heteroskedasticity with estimates of the variance of the u.k. inflation. Econometrica, 50:987–1008,
1982.


[26] Alizadeh F. and D. Goldfarb. Second-order cone programming. Mathematical Programming.


[27] M. Fischetti and Lodi A. Local branching. Mathematical Programming
B, 98:23–47, 2003.


BIBLIOGRAPHY 341


[28] R. Fletcher and S. Leyffer. User manual for FILTER/SQP. University
of Dundee, Dundee, Scotland, 1998.


[29] D. Goldfarb and G. Iyengar. Robust portfolio selection problems. Mathematics of Operations Research, 28:1–38, 2003.


[30] A. J. Goldman and A. W. Tucker. Linear Equalities and Related Systems, chapter Theory of linear programming, pages 53–97. Princeton
University Press, Princeton, NJ, 1956.


[31] R. Gomory. An algorithm for the mixed integer problem. Technical
report, Technical Report RM-2597, The Rand Corporation, 1960.


[32] J. Gondzio and Kouwenberg R. High performance for asset liability
management. Operations Research, 49:879–891, 2001.


[33] C. Gourieroux. ARCH Models and Financial Applications. Springer
Ser. Statist. Springer-Verlag, New York, 1997.


[34] R. Green and B. Hollifield. When will mean-variance efficient portfolios
be well-diversified. Journal of Finance, 47:1785–1810, 1992.


[35] E. Guslitser. Uncertainty-immunized solutions in linear programming.
Master’s thesis, The Technion, Haifa, 2002.


[36] B. Halldorsson and R. H. T¨ut¨unc¨u. An interior-point method for a
class of saddle point problems. Journal of Optimization Theory and
Applications, 116(3):559–590, 2003.


[37] R. Hauser and D. Zuev. Robust portfolio optimisation using maximisation of min eigenvalue methodology. Presentation at the Workshop
on Optimization in Finance, Coimbra, Portugal, July 2005.


[38] S. Herzel. Arbitrage opportunities on derivatives: A linear programming approach. Technical report, Department of Economics, University
of Perugia, 2000.


[39] K. Hoyland and Wallace S. W. Generating scenario trees for multistage
decision problems. Management Science, 47:295–307, 2001.


[40] P. Jorion. Portfolio optimization with tracking error constraints. Financial Analysts Journal, 59(5):70–82, September/October 2003.


[41] L. G. Khachiyan. A polynomial algorithm in linear programming. Soviet
Mathematics Doklady, 20:191–194, 1979.


[42] P. Klaassen. Comment on ”generating scenario trees for multistage
decision problems”. Management Science, 48:1512–1516, 2002.


[43] H. Konno and H. Yamazaki. Mean-absolute deviation portfolio optimization model and its applications to tokyo stock market. Management Science, 37:519–531, 1991.


342 BIBLIOGRAPHY


[44] P. Kouvelis and G. Yu. Robust Discrete Optimization and its Applications. Kluwer Academic Publishers, Amsterdam, 1997.


[45] R. Kouwenberg. Scenario generation and stochastic programming models for asset liability management. European Journal of Operational
Research, 134:279–292, 2001.


[46] R. Lagnado and S. Osher. Reconciling differences. Risk, 10:79–83, 1997.


[47] P. Laurence and T. H. Wang. What’s a basket worth? Risk, 17(2):73–
78, 2004.


[48] R. Litterman and Quantitative Resources Group. Modern Investment
Management: An Equilibrium Approach. John Wiley and Sons, 2003.


[49] M.S. Lobo, L.Vandenberghe, S. Boyd, and H. Lebret. Applications of
second-order cone programming. Linear Algebra and Its Applications,
284:193–228, 1998.


[50] R. O. Michaud. The Markowitz optimization enigma: Is optimized
optimal? Financial Analysts Journal, 45:31–42, 1989.


[51] R. O. Michaud. Efficient Asset Management. Harvard Business School
Press, Boston, Massachusetts, 1998.


[52] J.J. Mor´e and S. J. Wright. Optimization Software Guide. SIAM, 1993.


[53] J.M. Mulvey. Generating scenarios for the Towers Perrin investment
system. Interfaces, 26:1–15, 1996.


[54] Yu. Nesterov and A. Nemirovski. Interior-Point Polynomial Algorithms
in Convex Programming. SIAM, Philadelphia, Pennsylvania, 1994.


[55] J. Nocedal and S. J. Wright. Numerical Optimization. Springer-Verlag,
1999.


[56] M. Pınar. Minimum risk arbitrage with risky financial contracts. Technical report, Bilkent University, Ankara, Turkey, 2001.


[57] M. Pınar and R. H. T¨ut¨unc¨u. Robust profit opportunities in risky
financial portfolios. Operations Research Letters, 33(4):331–340, 2005.


[58] I. P´olik and T. Terlaky. S-lemma: A survey. Technical Report 2004/14,
AdvOL, McMaster University, Department of Computing and Software,
2004.


[59] C.R. Rao. Linear Stastistical Inference and its Applications. John Wiley
and Sons, New York, NY, 1965.


[60] R. T. Rockafellar. Convex Analysis. Princeton University Press, Princeton, NJ, 1970.


[61] R. T. Rockafellar and S. Uryasev. Optimization of conditional valueat-risk. The Journal of Risk, 2:21–41, 2000.


BIBLIOGRAPHY 343


[62] E. I. Ronn. A new linear programming approach to bond portfolio
management. Journal of Financial and Quantitative Analysis, 22:439–
466, 1987.


[63] B. Rustem and M. Howe. Algorithms for Worst-Case Design and Applications to Risk Management. Princeton University Press, 2002.


[64] S. M. Schaefer. Tax induced clientele effects in the market for british
government securities. Journal of Financial Economics, 10:121–159,
1982.


[65] K. Sch¨ottle and R. Werner. Benefits and costs of robust conic optimization. Technical report, T. U. M¨unchen, 2006.


[66] W. F. Sharpe. Determining a fund’s effective asset mix. Investment
Management Review, pages 59–69, December 1988.


[67] W. F. Sharpe. Asset allocation: Management style and performance
measurement. Journal of Portfolio Management, pages 7–19, Winter
1992.


[68] W.F. Sharpe. The Sharpe ratio. Journal of Portfolio Management,
Fall:49–58, 1994.


[69] J. F. Sturm. Using sedumi 1.02, a matlab toolbox for optimization over
symmetric cones. Optimization Methods and Software, 11-12:625–653,
1999.


[70] M. J. Todd. Semidefinite optimization. Acta Numerica, 10:515–560,
2001.


[71] R. H. T¨ut¨unc¨u and M. Koenig. Robust asset allocation. Annals of
Operations Research, 132:157–187, 2004.


[72] R. H. T¨ut¨unc¨u, K. C. Toh, and M. J. Todd. Solving semidefinitequadratic-linear programs using SDPT3. Mathematical Programming,
95:189–217, 2003.


[73] S. Uryasev. Conditional value-at-risk: Optimization algorithms and
applications. Financial Engineering News, 14:1–6, 2000.


[74] L.A. Wolsey. Integer Programming. John Wiley and Sons, New York,
NY, 1988.


[75] Y. Zhao and W. T. Ziemba. The Russell-Yasuda Kasai model: A
stochastic programming model using a endogenously determined worst
case risk measure for dynamic asset allocation. Mathematical Programming B, 89:293–309, 2001.


# Index

0–1 linear program, 12, 194


absolute robust, 294
accrual tranche, 248
active constraint, 103
adaptive decision variables, 255
adjustable robust optimization, 301
adjusted random sampling, 266
ALM, 279
American option, 18, 239, 244
anticipative decision variables, 255
arbitrage, 68
arbitrage pricing, 318
arbitrage-free scenario trees, 267
Armijo-Goldstein condition, 94
ARO, 301
asset allocation, 16
asset/liability management, 20, 279
autoregressive model, 263


backward recursion in DP, 228
basic feasible solution, 32
basic solution, 30
basic variable, 32
basis matrix, 32
Bellman equation, 234
Bellman’s principle of optimality,
225
benchmark, 179
Benders decomposition, 260
beta of a security, 148
binary integer linear program, 194
binary search, 86
binomial distribution, 241
binomial lattice, 241
Black Sholes Merton option pricing formula, 117
Black-Litterman model, 149
branch and bound, 201
branch and cut, 210



branching, 198, 203
Brownian motion, 117
BSM formula, 117


CAL, 156
call option, 18
callable debt, 282
capital allocation line, 156
capital budgeting, 194, 226
cash flow matching, 54
centered direction, 131
central path, 129
CMO, 247
collateralized mortgage obligation,
247
combinatorial auction, 213
complementary slackness, 27
concave function, 321
conditional prepayment model, 250
conditional value-at-risk, 273
cone, 323
conic optimization, 12, 169
constrained optimization, 102
constraint robustness, 14, 296
constructing an index fund, 217
constructing scenario trees, 265
contingent claim, 67
convex combination, 321
convex function, 321
convex set, 321
convexity of bond portfolio, 54
corporate debt management, 282
correlation, 328
covariance, 327
covariance matrix approximation,
182
credit migration, 276
credit rating, 248
credit risk, 276
credit spread, 251



344


INDEX 345



cubic spline, 161
cutting plane, 206
CVaR, 273


decision variables, 46
dedicated portfolio, 54
dedication, 54
default risk, 248
density function, 326
derivative security, 67
deterministic DP, 226
deterministic equivalent of an SP,
257
diffusion model, 118
discrete probability measure, 326
distribution function, 326
diversified portfolio, 146
dual cone, 323
dual of an LP, 24
dual QP, 124
dual simplex method, 41
duality gap, 25, 132
duration, 54
dynamic program, 13, 225


efficient frontier, 16
efficient portfolio, 16
ellipsoidal uncertainty set, 295
entering variable, 37
European option, 18
exercise price of an option, 18
expectation, 327
expected portfolio return, 16
expected value, 327
expiration date of an option, 18
extreme point, 32


feasibility cut, 262
feasible solution of an LP, 22
first order necessary conditions for
NLP, 103
formulating an LP, 47
forward recursion in DP, 231
forward start option, 187
Frobenius norm, 183
Fundamental Theorem of Asset Pricing, 72


GARCH model, 113



generalized reduced gradient, 105
geometric mean, 143
global optimum, 10
GMI cut, 207
golden section search, 88
Gomory mixed integer cut, 207
gradient, 96


hedge, 18
Hessian matrix, 100
heuristic for MILP, 205


idiosyncratic risk, 148
implied volatility, 117
independent random variables, 327
index fund, 217
index tracking, 179
infeasible problem, 9
insurance company ALM problem,
280
integer linear program, 12
integer program, 193
interior-point method, 126
internal rate of return, 86
IPM, 126
IRR, 86


Jacobian matrix, 99
joint distribution function, 327


Karush-Kuhn-Tucker conditions, 104
KKT conditions, 104
knapsack problem, 235
knot, 161


L-shaped method, 260
Lagrange multiplier, 102
Lagrangian function, 102
lagrangian relaxation, 220
leaving variable, 38
line search, 93
linear factor model, 158
linear optimization, 10
linear program, 10, 21
linear programming relaxation of
an MILP, 197
local optimum, 10
lockbox problem, 214
Lorenz cone, 170


346 INDEX



loss function, 273
loss multiple, 251
LP, 21


marginal distribution function, 327
market return, 148
Markowitz model, 139
master problem, 261
maturity date of an option, 67
maximum regret, 299
MBS, 247
mean, 327
mean-absolute deviation model, 153
mean-variance optimization, 16, 139
Michaud’s resampling approach, 148
MILP, 194
mixed integer linear program, 12,
194
model robustness, 14
modeling, 46
modeling logical conditions, 194
mortgage-backed security, 247
multi-stage stochastic program with
recourse, 258
MVO, 139


Newton’s method, 90, 99
NLP, 83
node selection, 204
nonbasic variable, 32
nonlinear program, 10, 83


objective function, 9
objective robustness, 15, 297
optimal solution of an LP, 22
optimality cut, 261
optimization problem, 9
option pricing, 18, 243


pass-through MBS, 247
path-following algorithm, 130
pay down, 248
payoff, 243
pension fund, 280
pivoting in simplex method, 38
polar cone, 323
polyhedral cone, 323
polyhedral set, 321



polyhedron, 321
polynomial time algorithm, 11
polynomial-time algorithm, 44
portfolio optimization, 16, 139
portfolio optimization with minimum transaction levels, 222
positive semidefinite matrix, 11
prepayment, 250
present value, 54
primal linear program, 24
probability distribution, 325
probability measure, 325
probability space, 326
pruning a node, 199
pure integer linear program, 12, 194
pure Newton step, 131
put option, 18


quadratic convergence, 92
quadratic program, 11, 123


random event, 325
random sampling, 265
random variable, 326
ratio test, 38
RBSA, 158
rebalancing, 289
recourse decision, 258
recourse problem, 261
reduced cost, 32, 58, 333
regular point, 103
relative interior, 127
relative robustness, 299
replicating portfolio, 18
replication, 69, 289
required buffer, 251
return-based style analysis, 158
revised simplex method, 329
risk management, 19
risk measure, 19
risk-neutral probabilities, 70
riskless profit, 78
robust multi-period portfolio selection, 307
robust optimization, 14, 293
robust portfolio optimization, 314
robust pricing, 318


INDEX 347



saddle point, 305
sample space, 325
scenario generation, 263
scenario tree, 258
scheduled amortization, 249
second order necessary conditions
for NLP, 104
second order sufficient conditions
for NLP, 104
second-order cone program, 169
securitization, 247
self-financing, 289
semi-definite program, 174
sensitivity analysis, 56
sequential quadratic programming,
110
shadow price, 57, 331
Sharpe ratio, 155
short sale, 17
simplex method, 38
simplex tableau, 37
slack variable, 21
software for NLP, 85
SOLVER spreadsheet, 49
spline, 161
stage in DP, 232
standard deviation, 327
standard form LP, 21
state in DP, 233
steepest descent, 95
stochastic DP, 237
stochastic linear program, 13
stochastic program, 13, 256
stochastic program with recourse,
13
strict global optimum, 10
strict local optimum, 10
strictly convex function, 321
strictly feasible, 127
strike price, 18
strong branching, 203
strong duality, 26
subgradient, 111
surplus variable, 21
symmetric matrix, 11
synthetic option, 285



terminal node, 258
tracking error, 180
tranche, 248
transaction cost, 147, 290
transition state, 233
transpose matrix, 11
tree fitting, 266
turnover constraint, 147
two stage stochastic program with
recourse, 256
type A arbitrage, 68
type B arbitrage, 68


unbounded problem, 9
uncertainty set, 294
unconstrained optimization, 95
underlying security, 18


value-at-risk, 271
VaR, 271
variance, 327
variance of portfolio return, 16
volatility estimation, 113
volatility smile, 118


WAL, 249
weak duality, 25
weighted average life, 249


yield of a bond, 87


zigzagging, 97


