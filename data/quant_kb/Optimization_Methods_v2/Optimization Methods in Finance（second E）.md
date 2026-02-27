![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-0-full.png)
**Optimization Methods in Finance**


Optimization methods play a central role in financial modeling. This textbook is devoted
to explaining how state-of-the-art optimization theory, algorithms, and software can be
used to efficiently solve problems in computational finance. It discusses some classical
mean–variance portfolio optimization models as well as more modern developments
such as models for optimal trade execution and dynamic portfolio allocation with transaction costs and taxes. Chapters discussing the theory and efficient solution methods for
the main classes of optimization problems alternate with chapters discussing their use
in the modeling and solution of central problems in mathematical finance.
This book will be interesting and useful for students, academics, and practitioners
with a background in mathematics, operations research, or financial engineering.
The second edition includes new examples and exercises as well as a more detailed
discussion of mean–variance optimization, multi-period models, and additional material
to highlight the relevance to finance.


**Gérard** **Cornuéjols** is a Professor of Operations Research at the Tepper School of
Business, Carnegie Mellon University. He is a member of the National Academy of
Engineering and has received numerous prizes for his research contributions in integer
programming and combinatorial optimization, including the Lanchester Prize, the
Fulkerson Prize, the Dantzig Prize, and the von Neumann Theory Prize.


**Javier** **Peña** is a Professor of Operations Research at the Tepper School of Business,
Carnegie Mellon University. His research explores the myriad of challenges associated
with large-scale optimization models and he has published numerous articles on optimization, machine learning, financial engineering, and computational game theory. His
research has been supported by grants from the National Science Foundation, including
a prestigious CAREER award.


**Reha Tütüncü** is the Chief Risk Officer at SECOR Asset Management and an adjunct
professor at Carnegie Mellon University. He has previously held senior positions at
Goldman Sachs Asset Management and AQR Capital Management focusing on quantitative portfolio construction, equity portfolio management, and risk management.


# **Optimization Methods in Finance**

#### Second Edition

GÉRARD CORNUÉJOLS


Carnegie Mellon University, Pennsylvania


JAVIER PEÑA


Carnegie Mellon University, Pennsylvania


REHA TÜTÜNCÜ


SECOR Asset Management


University Printing House, Cambridge CB2 8BS, United Kingdom


One Liberty Plaza, 20th Floor, New York, NY 10006, USA


477 Williamstown Road, Port Melbourne, VIC 3207, Australia


314–321, 3rd Floor, Plot 3, Splendor Forum, Jasola District Centre, New Delhi – 110025, India


79 Anson Road, #06–04/06, Singapore 079906


Cambridge University Press is part of the University of Cambridge.


It furthers the University’s mission by disseminating knowledge in the pursuit of
education, learning, and research at the highest international levels of excellence.


www.cambridge.org
Information on this title: www.cambridge.org/9781107056749
DOI: 10.1017/9781107297340


First edition © Gérard Cornuéjols and Reha Tütüncü 2007
Second edition © Gérard Cornuéjols, Javier Peña and Reha Tütüncü 2018


This publication is in copyright. Subject to statutory exception
and to the provisions of relevant collective licensing agreements,
no reproduction of any part may take place without the written
permission of Cambridge University Press.


First published 2007
Second edition 2018


Printed and bound in Great Britain by Clays Ltd, Elcograf S.p.A.


_A catalogue record for this publication is available from the British Library._


ISBN 978-1-107-05674-9 Hardback


Additional resources for this publication at www.cambridge.org/9781107056749


Cambridge University Press has no responsibility for the persistence or accuracy
of URLs for external or third-party internet websites referred to in this publication
and does not guarantee that any content on such websites is, or will remain,
accurate or appropriate.


### **Contents**

_Preface_ _page_ xi


**Part** **I** **Introduction** 1


**1** **Overview** **of** **Optimization** **Models** 3
1.1 Types of Optimization Models 4
1.2 Solution to Optimization Problems 7
1.3 Financial Optimization Models 8
1.4 Notes 10


**2** **Linear** **Programming:** **Theory** **and** **Algorithms** 11
2.1 Linear Programming 11
2.2 Graphical Interpretation of a Two-Variable Example 15
2.3 Numerical Linear Programming Solvers 16
2.4 Sensitivity Analysis 17
2.5 *Duality 20
2.6 *Optimality Conditions 23
2.7 *Algorithms for Linear Programming 24
2.8 Notes 30
2.9 Exercises 31


**3** **Linear** **Programming** **Models:** **Asset–Liability** **Management** 35
3.1 Dedication 35
3.2 Sensitivity Analysis 38
3.3 Immunization 38
3.4 Some Practical Details about Bonds 41
3.5 Other Cash Flow Problems 44
3.6 Exercises 47
3.7 Case Study 51


**4** **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing** 53
4.1 Arbitrage Detection in the Foreign Exchange Market 53
4.2 The Fundamental Theorem of Asset Pricing 55
4.3 One-Period Binomial Pricing Model 56


vi **Contents**


4.4 Static Arbitrage Bounds 59

4.5 Tax Clientele Effects in Bond Portfolio Management 63

4.6 Notes 65

4.7 Exercises 65


**Part** **II** **Single-Period** **Models** 69


**5** **Quadratic** **Programming:** **Theory** **and** **Algorithms** 71

5.1 Quadratic Programming 71

5.2 Numerical Quadratic Programming Solvers 74

5.3 Sensitivity Analysis 75

5.4 *Duality and Optimality Conditions 76

5.5 *Algorithms 81

5.6 Applications to Machine Learning 84

5.7 Exercises 87


**6** **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization** 90

6.1 Portfolio Return 90

6.2 Markowitz Mean–Variance (Basic Model) 91

6.3 Analytical Solutions to Basic Mean–Variance Models 95

6.4 More General Mean–Variance Models 99

6.5 Portfolio Management Relative to a Benchmark 103

6.6 Estimation of Inputs to Mean–Variance Models 106

6.7 Performance Analysis 112

6.8 Notes 115

6.9 Exercises 115

6.10 Case Studies 121


**7** **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation** 124

7.1 Black–Litterman Model 126

7.2 Shrinkage Estimation 129

7.3 Resampled Efficiency 131

7.4 Robust Optimization 132

7.5 Other Diversification Approaches 133

7.6 Exercises 135


**8** **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms** 140

8.1 Mixed Integer Programming 140

8.2 Numerical Mixed Integer Programming Solvers 143

8.3 Relaxations and Duality 145

8.4 Algorithms for Solving Mixed Integer Programs 150

8.5 Exercises 157


**Contents** vii


**9** **Mixed** **Integer** **Programming** **Models:** **Portfolios** **with** **Combinatorial**
**Constraints** 161
9.1 Combinatorial Auctions 161
9.2 The Lockbox Problem 163
9.3 Constructing an Index Fund 165
9.4 Cardinality Constraints 167
9.5 Minimum Position Constraints 168
9.6 Risk-Parity Portfolios and Clustering 169
9.7 Exercises 169
9.8 Case Study 171


**10** **Stochastic** **Programming:** **Theory** **and** **Algorithms** 173
10.1 Examples of Stochastic Optimization Models 173
10.2 Two-Stage Stochastic Optimization 174
10.3 Linear Two-Stage Stochastic Programming 175
10.4 Scenario Optimization 176
10.5 *The L-Shaped Method 177
10.6 Exercises 179


**11** **Stochastic** **Programming** **Models:** **Risk** **Measures** 181
11.1 Risk Measures 181
11.2 A Key Property of CVaR 185
11.3 Portfolio Optimization with CVaR 186
11.4 Notes 190
11.5 Exercises 190


**Part** **III** **Multi-Period** **Models** 195


**12** **Multi-Period** **Models:** **Simple** **Examples** 197
12.1 The Kelly Criterion 197
12.2 Dynamic Portfolio Optimization 198
12.3 Execution Costs 201
12.4 Exercises 209


**13** **Dynamic** **Programming:** **Theory** **and** **Algorithms** 212
13.1 Some Examples 212
13.2 Model of a Sequential System (Deterministic Case) 214
13.3 Bellman’s Principle of Optimality 215
13.4 Linear–Quadratic Regulator 216
13.5 Sequential Decision Problem with Infinite Horizon 218
13.6 Linear–Quadratic Regulator with Infinite Horizon 219
13.7 Model of Sequential System (Stochastic Case) 221
13.8 Notes 222
13.9 Exercises 222


viii **Contents**


**14** **Dynamic** **Programming** **Models:** **Multi-Period** **Portfolio** **Optimization** 225
14.1 Utility of Terminal Wealth 225
14.2 Optimal Consumption and Investment 227
14.3 Dynamic Trading with Predictable Returns and Transaction Costs 228
14.4 Dynamic Portfolio Optimization with Taxes 230
14.5 Exercises 234


**15** **Dynamic** **Programming** **Models:** **the** **Binomial** **Pricing** **Model** 238
15.1 Binomial Lattice Model 238
15.2 Option Pricing 238
15.3 Option Pricing in Continuous Time 244
15.4 Specifying the Model Parameters 245
15.5 Exercises 246


**16** **Multi-Stage** **Stochastic** **Programming** 248
16.1 Multi-Stage Stochastic Programming 248
16.2 Scenario Optimization 250
16.3 Scenario Generation 255
16.4 Exercises 259


**17** **Stochastic** **Programming** **Models:** **Asset–Liability** **Management** 262
17.1 Asset–Liability Management 262
17.2 The Case of an Insurance Company 263
17.3 Option Pricing via Stochastic Programming 265
17.4 Synthetic Options 270
17.5 Exercises 273


**Part** **IV** **Other** **Optimization** **Techniques** 275


**18** **Conic** **Programming:** **Theory** **and** **Algorithms** 277
18.1 Conic Programming 277
18.2 Numerical Conic Programming Solvers 282
18.3 Duality and Optimality Conditions 282
18.4 Algorithms 284
18.5 Notes 287
18.6 Exercises 287


**19** **Robust** **Optimization** 289
19.1 Uncertainty Sets 289
19.2 Different Flavors of Robustness 290
19.3 Techniques for Solving Robust Optimization Models 294
19.4 Some Robust Optimization Models in Finance 297
19.5 Notes 302
19.6 Exercises 302


**Contents** ix


**20** **Nonlinear** **Programming:** **Theory** **and** **Algorithms** 305
20.1 Nonlinear Programming 305
20.2 Numerical Nonlinear Programming Solvers 306
20.3 Optimality Conditions 306
20.4 Algorithms 308
20.5 Estimating a Volatility Surface 315
20.6 Exercises 319


**Appendices** 321


**Appendix** **Basic** **Mathematical** **Facts** 323
A.1 Matrices and Vectors 323
A.2 Convex Sets and Convex Functions 324
A.3 Calculus of Variations: the Euler Equation 325


**References** 327


**Index** 334


### **Preface**

The use of sophisticated mathematical tools in modern finance is now commonplace. Researchers and practitioners routinely run simulations or solve differential
equations to price securities, estimate risks, or determine hedging strategies.
Some of the most important tools employed in these computations are optimization algorithms. Many computational finance problems ranging from asset
allocation to risk management, from option pricing to model calibration, can
be solved by optimization techniques. This book is devoted to explaining how
to solve such problems efficiently and accurately using the state of the art in
optimization models, methods, and software.
Optimization is a mature branch of applied mathematics. Typical optimization
problems have the goal of allocating limited resources to alternative activities in
order to maximize the total benefit obtained from these activities. Through
decades of intensive and innovative research, fast and reliable algorithms
and software have become available for many classes of optimization problems. Consequently, optimization is now being used as an effective management and decision-support tool in many industries, including the financial
industry.
This book discusses several classes of optimization problems encountered in
financial models, including linear, quadratic, integer, dynamic, stochastic, conic,
and nonlinear programming. For each problem class, after introducing the relevant theory (optimality conditions, duality, etc.) and efficient solution methods,
we discuss several problems of mathematical finance that can be modeled within
this problem class.
The second edition includes a more detailed discussion of mean–variance optimization, multi-period models, and additional material to highlight the relevance
to finance.
The book’s structure has also been clarified for the second edition; it is now
organized in four main parts, each comprising several chapters. Part I guides
the reader through the solution of asset liability cash flow matching using linear programming techniques, which are also used to explain asset pricing and
arbitrage. Part II is devoted to single-period models. It provides a thorough
treatment of mean–variance portfolio optimization models, including derivations
of the one-fund and two-fund theorems and their connection to the capital asset
pricing model, a discussion of linear factor models that are used extensively


xii **Preface**


in risk and portfolio management, and techniques to deal with the sensitivity of
mean–variance models to parameter estimation. We discuss integer programming
formulations for portfolio construction problems with cardinality constraints, and
we explain how this is relevant to constructing an index fund. The final chapters
of Part II present a stochastic programming approach to modeling measures of
risk other than the variance, including the popular value at risk and conditional
value at risk.
Part III of the book discusses multi-period models such as the iconic Kelly criterion and binomial lattice models for asset pricing as well as more elaborate and
modern models for optimal trade execution, dynamic portfolio optimization with
transaction costs and taxes, and asset–liability management. These applications
showcase techniques from dynamic and stochastic programming.
Part IV is devoted to more advanced optimization techniques. We introduce
conic programming and discuss applications such as the approximation of covariance matrices and robust portfolio optimization. The final chapter of Part IV
covers one of the most general classes of optimization models, namely nonlinear
programming, and applies it to volatility estimation.
This book is intended as a textbook for Master’s programs in financial engineering, finance, or computational finance. In addition, the structure of chapters,
alternating between optimization methods and financial models that employ
these methods, allows the book to be used as a primary or secondary text
in upper-level undergraduate or introductory graduate courses in operations
research, management science, and applied mathematics. A few sections are
marked with a ‘ _∗_ ’ to indicate that the material they contain is more technical
and can be safely skipped without loss of continuity.
Optimization algorithms are sophisticated tools and the relationship between
their inputs and outputs is sometimes opaque. To maximize the value from using
these tools and to understand how they work, users often need a significant
amount of guidance and practical experience with them. This book aims to
provide this guidance and serve as a reference tool for the finance practitioners
who use or want to use optimization techniques.
This book has benefited from the input provided by instructors and students
in courses at various institutions. We thank them for their valuable feedback
and for many stimulating discussions. We would also like to thank the colleagues
who provided the initial impetus for this book and colleagues who collaborated
with us on various research projects that are reflected in the book. We especially
thank Kathie Cameron, the late Rick Green, Raphael Hauser, John Hooker,
Miroslav Karamanov, Mark Koenig, Masakazu Kojima, Vijay Krishnamurthy,
Miguel Lejeune, Yanjun Li, Fran¸cois Margot, Ana Margarida Monteiro, Mustafa
Pınar, Sebastian Pokutta, Sanjay Srivastava, Michael Trick, and Lu´ıs Vicente.


## **Part I** **Introduction**


## 1 Overview of Optimization Models

Optimization is the process of finding the _best_ way of making decisions that
satisfy a set of constraints. In mathematical terms, an optimization model is a
problem of the form


min _f_ ( **x** )
**x** (1.1)

s.t. **x** _∈X_ _,_


where _f_ : R _[n]_ _→_ R and _X_ _⊆_ R _[n]_ .
Model (1.1) has three main components, namely the vector of _decision_ _vari-_
_ables_ **x** :=      - _x_ 1 _· · ·_ _xn_ �T _∈_ R _n_ ; the _objective_ _function_ _f_ ( **x** ); and the _constraint_
_set_ or _feasible region X_ . The constraint set is often expressed in terms of equalities
and inequalities involving additional functions. More precisely, the constraint set
_X_ is often of the form


_X_ = _{_ **x** _∈_ R _[n]_ : _gi_ ( **x** ) = _bi,_ for _i_ = 1 _, . . ., m,_ and _hj_ ( **x** ) _≤_ _dj,_ for _j_ = 1 _, . . ., p},_
(1.2)
for some _gi, hj_ : R _[n]_ _→_ R _,_ _i_ = 1 _, . . ., m,_ _j_ = 1 _, . . ., p_ . When this is the case, the
optimization problem (1.1) is usually written in the form


min _f_ ( **x** )
**x**

s.t. _gi_ ( **x** ) = _bi,_ for _i_ = 1 _, . . ., m_
_hj_ ( **x** ) _≤_ _dj,_ for _j_ = 1 _, . . ., p,_


or in the more concise form


min _f_ ( **x** )
**x**

s.t. **g** ( **x** ) = **b**
**h** ( **x** ) _≤_ **d** _._


We will use the following terminology. A _feasible_ _point_ or _feasible_ _solution_ to
(1.1) is a point in the constraint set _X_ . An _optimal_ _solution_ to (1.1) is a feasible
point that attains the best possible objective value; that is, a point **x** _[∗]_ _∈X_
such that _f_ ( **x** _[∗]_ ) _≤_ _f_ ( **x** ) for all **x** _∈X_ _._ The _optimal_ _value_ of (1.1) is the value
of the objective function at an optimal solution; that is, _f_ ( **x** _[∗]_ ) where **x** _[∗]_ is an
optimal solution to (1.1). If the feasible region _X_ is of the form (1.2) and **x** _∈X_,
the _binding_ _constraints_ at **x** are the equality constraints and those inequality
constraints that hold with equality at **x** . The term _active_ _constraint_ is also often
used in lieu of “binding constraint”. The problem (1.1) is _infeasible_ if _X_ = _∅_ . On


4 **Overview** **of** **Optimization** **Models**


the other hand, (1.1) is _unbounded_ if there exist **x** _k_ _∈X_ _,_ _k_ = 1 _,_ 2 _, . . ._, such that
_f_ ( **x** _k_ ) _→−∞._


**1.1** **Types** **of** **Optimization** **Models**


For optimization models to be of practical interest, their computational tractability, that is, the ability to find the optimal solution efficiently, is a critical issue.
Particular structural assumptions on the objective and constraints of the problem
give rise to different classes of optimization models with various degrees of
computational difficulty. We should note that the following is only a partial classification based on the current generic tractability of various types of optimization
models. However, what is “tractable” in some specific context may be more
nuanced. Furthermore, tractability evolves as new algorithms and technologies
are developed.


**Convex** **optimization:** These are problems where the objective _f_ ( **x** ) is a convex function and the constraint set _X_ is a convex set. This class of
optimization models is tractable most of the time. By this we mean that
a user can expect any of these models to be amenable to an efficient algorithm. We will emphasize this class of optimization models throughout
the book.
**Mixed** **integer** **optimization:** These are problems where some of the variables
are restricted to take integer values. This restriction makes the constraint set _X_ non-convex. This class of optimization models is somewhat
tractable a fair portion of the time. By this we mean that a model of this
class may be solvable provided the user does some judicious modeling
and has access to high computational power.
**Stochastic** **and** **dynamic** **optimization:** These are problems involving random and time-dependent features. This class of optimization models
is tractable only in some special cases. By this we mean that, unless
some specific structure and assumptions hold, a model of this class
would typically be insoluble with any realistic amount of computational
power at our disposal. Current research is expected to enrich the class
of tractable models in this area.


The modeling of time and uncertainty is pervasive in almost every financial
problem. The various types of optimization problems that we will discuss are
based on how they deal with these two issues. Generally speaking, _static_ _models_
are associated with simple single-period models where the future is modeled as
a single stage. By contrast, in _multi-period_ models the future is modeled as a
sequence, or possibly as a continuum, of stages. With regard to uncertainty,
_deterministic_ _models_ are those where all the defining data are assumed to be
known with certainty. By contrast, _stochastic_ _models_ are ones that incorporate
probabilistic or other types of uncertainty in the data.


**1.1** **Types** **of** **Optimization** **Models** 5


A good portion of the models that we will present in this book will be convex
optimization models due to their favorable mathematical and computational
properties. There are two special types of convex optimization problems that we
will use particularly often: _linear_ and _quadratic_ programming, the latter being an
extension of the former. These two types of optimization models will be discussed
in more detail in Chapters 2 and 5. We now present a high-level description
of four major classes of optimization models: linear programming, quadratic
programming, mixed integer programming, and stochastic optimization.


Linear Programming


A linear programming model is an optimization problem where the objective is a
linear function and the constraint set is defined by finitely many linear equalities
and linear inequalities. In other words, a linear program is a problem of the form


min **c** [T] **x**
**x**

s.t. **Ax** = **b**
**Dx** _≥_ **d**


for some vectors **c** _∈_ R _[n]_ _,_ **b** _∈_ R _[m]_ _,_ **d** _∈_ R _[p]_ and matrices **A** _∈_ R _[m][×][n]_ _,_ **D** _∈_ R _[p][×][n]_ _._
The term _linear optimization_ is sometimes used in place of linear programming.
The wide popularity of linear programming is due in good part to the availability
of very efficient algorithms. The two best known and most successful methods
for solving linear programs are the _simplex_ _method_ and _interior-point_ _methods._
We briefly discuss these algorithms in Chapter 2.


Quadratic Programming


Quadratic programming, also known as quadratic optimization, is an extension
of linear programming where the objective function includes a quadratic term.
In other words, a quadratic program is a problem of the form


min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **Ax** = **b**
**Dx** _≥_ **d**


for some vectors and matrices **Q** _∈_ R _[n][×][n]_, **c** _∈_ R _[n]_, **b** _∈_ R _[m]_, **d** _∈_ R _[p]_, **A** _∈_ R _[m][×][n]_,
**D** _∈_ R _[p][×][n]_ . It is customary to assume that the matrix **Q** is symmetric. This
assumption can be made without loss of generality since


**x** [T] **Qx** = **x** [T][ ˜] **Qx**



where **Q** [˜] = [1]



**Q** [˜] = [1] 2 [(] **[Q]** [ +] **[ Q]** [T][),] [which] [is] [clearly] [a] [symmetric] [matrix.]

We note that a quadratic function [1] **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** [is] [convex]



We note that a quadratic function [1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** [is] [convex] [if] [and] [only] [if] [the]

matrix **Q** is positive semidefinite ( **x** [T] **Qx** _≥_ 0 for all _x_ _∈_ R _[n]_ ). In this case the
above quadratic program is a convex optimization problem and can be solved


6 **Overview** **of** **Optimization** **Models**


efficiently. The two best known methods for solving convex quadratic programs
are _active-set_ _methods_ and _interior-point_ _methods._ We briefly discuss these algorithms in Chapter 5.


Mixed Integer Programming


A mixed-integer program is an optimization problem that restricts some or all of
the decision variables to take integer values. In particular, a mixed integer linear
programming model is a problem of the form


min **c** [T] **x**
**x**

s.t. **Ax** = **b**
**Dx** _≥_ **d**
_xj_ _∈_ Z _,_ _j_ _∈_ _J_


for some vectors and matrices **c** _∈_ R _[n]_, **b** _∈_ R _[m]_, **d** _∈_ R _[p]_, **A** _∈_ R _[m][×][n]_, **D** _∈_ R _[p][×][n]_

and some _J_ _⊆{_ 1 _, . . ., n}_ .
An important case occurs when the model includes _binary_ variables, that is,
variables that are restricted to take values 0 or 1. As we will see, the inclusion
of this type of constraint increases the modeling power but comes at a cost in
terms of computational tractability. It is noteworthy that the computational and
algorithmic machinery for solving mixed integer programs has vastly improved
during the last couple of decades. The main classes of methods for solving
mixed integer programs are _branch_ _and_ _bound_, _cutting_ _planes_, and a combination
of these two approaches known as _branch_ _and_ _cut_ . We briefly discuss these
algorithms in Chapter 8.


Stochastic Optimization


Stochastic optimization models are optimization problems that account for randomness in their objective or constraints. The following formulation illustrates
a generic type of stochastic optimization problem


min E( _F_ ( **x** _, ω_ ))
**x**

**x** _∈X_ _._


In this problem the set of decisions **x** must be made before a random outcome
_ω_ occurs. The goal is to optimize the expectation of some function that depends
on both the decision vector **x** and the random outcome _ω._ A variation of this formulation, that has led to important developments, is to replace the expectation
by some kind of _risk_ _measure_ _ϱ_ in the objective:


min _ϱ_ ( _F_ ( **x** _, ω_ ))
**x**

**x** _∈X_ _._


There are numerous refinements and variants of the above two formulations. In
particular, the class of _two-stage_ _stochastic_ _optimization_ _with_ _recourse_ has been


**1.2** **Solution** **to** **Optimization** **Problems** 7


widely studied in the stochastic programming community. In this setting a set
of decisions **x** must be made in stage one. Between stage one and stage two
a random outcome _ω_ occurs. At stage two we have the opportunity to make
some second-stage _recourse_ decisions **y** ( _ω_ ) that may depend on the random
outcome _ω_ .
The two-stage stochastic optimization problem with recourse can be formally
stated as
min _f_ ( **x** ) + E[ _Q_ ( **x** _, ω_ )]
**x**

**x** _∈X_ _._


The _recourse_ term _Q_ ( **x** _, ω_ ) depends on the first-stage decisions **x** and the random
outcome _ω_ . It is of the form


_Q_ ( **x** _, ω_ ) := min _g_ ( **y** ( _ω_ ) _, ω_ )
**y** ( _ω_ )

**y** ( _ω_ ) _∈Y_ ( **x** _, ω_ ) _._


The second-stage decisions **y** ( _ω_ ) are _adaptive_ to the random outcome _ω_ because
they are made after _ω_ is revealed. The objective function in a two-stage stochastic
optimization problem contains a term for the stage-one decisions and a term for
the stage-two decisions where the latter term involves an expectation over the
random outcomes. The intuition of this objective function is that the stage-one
decisions should be made considering what is to be expected in stage two.
The above two-stage setting generalizes to a multi-stage context where the
random outcome is revealed over time and decisions are made dynamically at
multiple stages and can adapt to the information revealed up to their stage.


**1.2** **Solution** **to** **Optimization** **Problems**


The solution to an optimization problem can often be characterized in terms of
a set of _optimality_ _conditions._ Optimality conditions are derived from the mathematical relationship between the objective and constraints in the problem. Subsequent chapters discuss optimality conditions for various types of optimization
problems. In special cases, these optimality conditions can be solved analytically
and used to infer properties about the optimal solution. However, in many cases
we rely on numerical solvers to obtain the solution to the optimization models.
There are numerous software vendors that provide solvers for optimization
problems. Throughout this book we will illustrate examples with two popular
solvers, namely Excel Solver and the MATLAB [®] -based optimization modeling
framework CVX. Excel and MATLAB files for the examples and exercises in the
book are available at:


www.andrew.cmu.edu/user/jfp/OIFbook/


Both Excel Solver and CVX enable us to solve small to medium-sized problems
and are fairly easy to use. There are far more sophisticated solvers such as the


8 **Overview** **of** **Optimization** **Models**


commercial solvers IBM [®] -ILOG [®] CPLEX [®], Gurobi, FICO [®] Xpress, and the ones
available via the open-source projects COIN-OR or SCIP.
Optimization problems can be formulated using modeling languages such as
AMPL, GAMS, MOSEL, or OPL. The need for these modeling languages arises
when the size of the formulation is large. A modeling language lets people use
common notation and familiar concepts to formulate optimization models and
examine solutions. Most importantly, large problems can be formulated in a
compact way. Once the problem has been formulated using a modeling language,
it can be solved using any number of solvers. A user can switch between solvers
with a single command and select options that may improve solver performance.


**1.3** **Financial** **Optimization** **Models**


In this book we will focus on the use of optimization models for financial problems
such as portfolio management, risk management, asset and liability management,
trade execution, and dynamic asset management. Optimization models are also
widely used in other areas of business, science, and engineering, but this will not
be the subject of our discussion.


Portfolio Management


One of the best known optimization models in finance is the portfolio selection
model of Markowitz (1952). Markowitz’s mean–variance approach led to major
developments in financial economics including Tobin’s mutual fund theorem
1
(Tobin, 1958) and the capital asset pricing model of Treynor, Sharpe (1964),
Lintner (1965), and Mossin (1966). Markowitz was awarded the Nobel Prize in
Economics in 1990 for the enormous influence of his work in financial theory and
practice. The gist of this model is to formalize the principle of diversification
when selecting a portfolio in a universe of risky assets. As we discuss in detail in
Chapter 6, Markowitz’s mean–variance model and a wide range of its variations
can be stated as a quadratic programming problem of the form

min **x** 12 _[γ][ ·]_ **[ x]** [T] **[Vx]** _[ −]_ _**[μ]**_ [T] **[x]**

**Ax** = **b** (1.3)
**Dx** _≥_ **d** _._


The vector of decision variables **x** in model (1.3) represents the portfolio holdings.
These holdings typically represent the percentages invested in each asset and
thus are often subject to the full investment constraint **1** [T] **x** = 1. Other common
constraints include the long-only constraint **x** _≥_ **0**, as well as restrictions related
to sector or industry composition, turnover, etc. The terms **x** [T] **Vx** and _**μ**_ [T] **x** in
the objective function are respectively the variance, which is a measure of risk,


1
“Toward a theory of market value of risky assets”. Unpublished manuscript, 1961.


**1.3** **Financial** **Optimization** **Models** 9


and the expected return of the portfolio defined by **x** . The risk-aversion constant
_γ_ _>_ 0 in the objective determines the tradeoff between risk and return of the
portfolio.


Risk Management


Risk is inherent in most economic activities. This is especially true of financial
activities where results of decisions made today may have many possible different
outcomes depending on future events. Since companies cannot usually insure
themselves completely against risk, they have to manage it. This is a hard task
even with the support of advanced mathematical techniques. Poor risk management led to several spectacular failures in the financial industry in the 1990s
(e.g., Barings Bank, Long Term Capital Management, Orange County). It was
also responsible for failures and bailouts of a number of institutions (e.g., Lehman
Brothers, Bear Stearns, AIG) during the far more severe global financial crisis of
2007–2008. Regulations, such as those prescribed by the Basel Accord (see Basel
Committee on Banking Supervision, 2011), mandate that financial institutions
control their risk via a variety of measurable requirements. The modeling of regulatory constraints as well as other risk-related constraints that the firm wishes
to impose to prevent vulnerabilities can often be stated as a set of constraints


**RM** ( **x** ) _≤_ **b** _._ (1.4)


The vector **x** in (1.4) represents the holdings in a set of risky securities. The
entries of the vector-valued function **RM** ( **x** ) represent one or more measures of
risk and the vector **b** represents the acceptable upper limits on these measures.
The set of risk management constraints (1.4) may be embedded in a more
elaborate model that aims to optimize some kind of performance measure such
as expected investment return.
In Chapter 2 we discuss a linear programming model for optimal bank planning
under Basel III regulations. In this case the components of the function **RM** ( **x** )
are linear functions of **x** . In Chapter 11 we discuss more sophisticated risk
measures such as value at risk and conditional value at risk that typically make
**RM** ( **x** ) a nonlinear function of **x** .


Asset and Liability Management


How should a financial institution manage its assets and liabilities? A static
model, such as the Markowitz mean–variance portfolio selection model, fails
to incorporate the multi-period nature of typical liabilities faced by financial
institutions. Furthermore, it penalizes returns both above and below the mean.
A multi-period model that emphasizes the need to meet liabilities in each
period for a finite (or possibly infinite) horizon is often more appropriate. Since
liabilities and asset returns usually have random components, their optimal
management requires techniques to optimize under uncertainty such as stochastic
optimization.


10 **Overview** **of** **Optimization** **Models**


We discuss several asset and liability management models in Chapters 3, 16,
and 17. A generic asset and liability management model can often be formulated
as a stochastic programming problem of the form


max E( _U_ ( **x** ))
**x**

**Fx** = **L** (1.5)
**Dx** _≥_ **0** _._


The vector **x** in (1.5) represents the investment decisions for the available assets
at the dates in the planning horizon. The vector **L** in (1.5) represents the
liabilities that the institution faces at the dates in the planning horizon. The
constraints **Fx** = **L**, **Dx** _≥_ **0** represent the cash flow rules and restrictions
applicable to the assets during the planning horizon. The term _U_ ( **x** ) in the
objective function is some appropriate measure of utility. For instance, it could
be the value of terminal wealth at the end of the planning horizon. In general,
the components **F** _,_ **L** _,_ **D** are discrete-time random processes and thus (1.5) is
a multi-stage stochastic programming model with recourse. In Chapter 3 we
discuss some special cases of (1.5) with no randomness.


**1.4** **Notes**


George Dantzig was the inventor of linear programming and author of many
related articles as well as a classical reference on the subject (Dantzig, 1963). A
particularly colorful and entertaining description of the diet problem, a classical
linear programming model, can be found in Dantzig (1990).
Boyd and Vandenberghe (2004) give an excellent exposition of convex optimization appropriate for senior or first-year graduate students in engineering.
This book is freely available at:


www.stanford.edu/~boyd/cvxbook/


Ragsdale (2007) gives a practical exposition of optimization and related
spreadsheet models that circumvent most technical issues. It is appropriate for
senior or Master’s students in business.


## 2 Linear Programming: Theory and Algorithms

Linear programming is one of the most significant contributions to computational
mathematics made in the twentieth century. This chapter introduces the main
ideas behind linear programming theory and algorithms. It also introduces two
easy-to-use solvers.


**2.1** **Linear** **Programming**


A _linear_ _program_ is an optimization problem whose objective is to minimize or
maximize a linear function subject to a finite set of linear equality and linear
inequality constraints. By flipping signs if necessary, a linear program can always
be written in the generic form:


min **c** [T] **x**
**x**

s.t. **Ax** = **b**
**Dx** _≥_ **d**


for some vectors and matrices **c** _∈_ R _[n]_ _,_ **b** _∈_ R _[m]_ _,_ **d** _∈_ R _[p]_ _,_ **A** _∈_ R _[m][×][n]_ _,_ **D** _∈_ R _[p][×][n]_ _._
The terms _linear_ _programming_ _model_ or _linear_ _optimization_ _model_ are also used
to refer to a linear program. We will use these terms interchangeably throughout
the book.
The following two simplified portfolio construction examples illustrate the use
of linear programming as a modeling tool.


**Example** **2.1** (Fund allocation) You would like to allocate $80,000 among four
mutual funds that have different expected returns as well as different weights in
large-, medium- and small-capitalization stocks.


Capitalization Fund 1 Fund 2 Fund 3 Fund 4


Large 50% 30% 25% 60%
Medium 30% 10% 40% 20%
Small 20% 60% 35% 20%


Exp. return 10% 15% 16% 8%


12 **Linear** **Programming:** **Theory** **and** **Algorithms**


The allocation must contain at least 35% large-cap, 30% mid-cap, and 15%
small-cap stocks. Find an acceptable allocation with the highest expected return
assuming you are only allowed to hold long positions in the funds.


This problem can be formulated as the following linear programming model.


_Linear_ _programming_ _model_ _for_ _fund_ _allocation_
**Variables:**


_xi_ : amount (in $1000s) invested in fund _i_ for _i_ = 1 _, . . .,_ 4 _._


**Objective:**


max 0 _._ 10 _x_ 1 + 0 _._ 15 _x_ 2 + 0 _._ 16 _x_ 3 + 0 _._ 08 _x_ 4 _._


**Constraints:**

0 _._ 50 _x_ 1 + 0 _._ 30 _x_ 2 + 0 _._ 25 _x_ 3 + 0 _._ 60 _x_ 4 _≥_ 0 _._ 35 _∗_ 80 (large-cap)
0 _._ 30 _x_ 1 + 0 _._ 10 _x_ 2 + 0 _._ 40 _x_ 3 + 0 _._ 20 _x_ 4 _≥_ 0 _._ 30 _∗_ 80 (mid-cap)
0 _._ 20 _x_ 1 + 0 _._ 60 _x_ 2 + 0 _._ 35 _x_ 3 + 0 _._ 20 _x_ 4 _≥_ 0 _._ 15 _∗_ 80 (small-cap)
_x_ 1 + _x_ 2 + _x_ 3 + _x_ 4 = 80 (money to allocate)
_x_ 1 _, . . ., x_ 4 _≥_ 0 (long-only positions).


**Example** **2.2** (Bond allocation) A bond portfolio manager has $100,000 to
allocate to two different bonds: a corporate bond and a government bond. These
bonds have the following yield, risk level, and maturity:


Bond Yield Risk level Maturity


Corporate 4% 2 3 years
Government 3% 1 4 years


The portfolio manager would like to allocate the funds so that the average risk
level of the portfolio is at most 1.5 and the average maturity is at most 3.6 years.
Any amount not invested in the bonds will be kept in a cash account that is
assumed to generate no interest and does not contribute to the average risk level
or maturity. In other words, assume cash has zero yield, zero risk level, and zero
maturity.
How should the manager allocate funds to the two bonds to maximize yield?
Assume the portfolio can only include long positions.


This problem can be formulated as the following linear programming model.


_Linear_ _programming_ _model_ _for_ _bond_ _allocation_
**Variables:**


_x_ 1 _, x_ 2: amounts (in $1000s) invested in the corporate and government


bonds respectively.


**Objective:**


max 4 _x_ 1 + 3 _x_ 2 _._


**2.1** **Linear** **Programming** 13



**Constraints:**
_x_ 1 + _x_ 2 _≤_ 100 (total funds)
2 _x_ 1 + _x_ 2



_≤_ 1 _._ 5 (risk level)
100
3 _x_ 1 + 4 _x_ 2



_≤_ 3 _._ 6 (maturity)
100



_x_ 1 _, x_ 2 _≥_ 0 (long-only positions)


or equivalently


max 4 _x_ 1 + 3 _x_ 2
s.t.
_x_ 1 + _x_ 2 _≤_ 100 (total funds)
2 _x_ 1 + _x_ 2 _≤_ 150 (risk level)
3 _x_ 1 + 4 _x_ 2 _≤_ 360 (maturity)
_x_ 1 _, x_ 2 _≥_ 0 (long-only positions).


The linear programming model in Example 2.1 can be written more concisely
using matrix–vector notation as follows:


max **r** [T] **x**
s.t. **Ax** = **b**
**Dx** _≥_ **d**
**x** _≥_ **0** _,_



0 _._ 10
0 _._ 15
0 _._ 16
0 _._ 08



⎡

0 _._ 5 0 _._ 3 0 _._ 25 0 _._ 6
⎣0 _._ 3 0 _._ 1 0 _._ 4 0 _._ 2
0 _._ 2 0 _._ 6 0 _._ 35 0 _._ 2



⎤


⎦, and



⎤


    -     , **A** = 1 1 1 1, **b** = 80, **D** =
⎥⎥⎦



where **r** =



⎡

⎢⎢⎣



**d** =



⎡

28
⎣24
12



⎤


⎦.



Likewise, the linear programming model in Example 2.2 can be written as


max **r** [T] **x**
s.t. **Ax** _≤_ **b**
**x** _≥_ **0** _,_



⎤


⎦, and **b** =



⎡

100
⎣150
360



⎤


⎦.




   -    4
for **r** =, **A** =
3



⎡

1 1
⎣2 1
3 4



A linear programming model is in _standard_ _form_ if it is written as follows:


min **c** [T] **x**
s.t. **Ax** = **b**
**x** _≥_ **0** _._


The standard form is a kind of formatting convention that is used by some
solvers. It is also particularly convenient to describe the most popular algorithms
for solving linear programming, namely the simplex and interior-point methods.


14 **Linear** **Programming:** **Theory** **and** **Algorithms**


The standard form is not restrictive. Any linear program can be rewritten in
standard form. In particular, inequality constraints (other than non-negativity)
can be rewritten as equality constraints after the introduction of a so-called _slack_
or _surplus_ variable. For instance, the linear program from Example 2.2 can be
written as


max 4 _x_ 1 + 3 _x_ 2
s.t.
_x_ 1 + _x_ 2 + _x_ 3 = 100
2 _x_ 1 + _x_ 2 + _x_ 4 = 150
3 _x_ 1 + 4 _x_ 2 + _x_ 5 = 360
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _, x_ 5 _≥_ 0 _._


More generally, a linear program of the form


min **c** [T] **x**
s.t. **Ax** _≤_ **b**
**x** _≥_ **0**


can be rewritten as


min **c** [T] **x**
s.t. **Ax** + **s** = **b**
**x** _,_ **s** _≥_ **0** _._


It can then be rewritten, using matrix notation, in the following standard form:



�T �
**x**
**s**








   **c**
min
**0**




   -    - [�] **x**
s.t. **A** **I**
**s**




    
- - [�] **x**
**A** **I** = **b**
**s**

- **x**

_≥_ **0** _._

**s**




_≥_ **0** _._



Unrestricted variables can be expressed as the difference of two new non-negative
variables. For example, consider the linear program


min **c** [T] **x**
s.t. **Ax** _≤_ **b** _._


The unrestricted variable **x** can be replaced by **u** _−_ **v** where **u** _,_ **v** _≥_ **0** . Hence the
above linear program can be rewritten as


min **c** [T] ( **u** _−_ **v** )
s.t. **A** ( **u** _−_ **v** ) _≤_ **b**
**u** _,_ **v** _≥_ **0** _._


**2.2** **Graphical** **Interpretation** **of** **a** **Two-Variable** **Example** 15


It can also be rewritten, after adding slack variables and using matrix notation,
in the following standard form:



⎡



⎤


⎦



T ⎡



**u**
⎣ **v**
**s**



⎤


⎦



min



**c**
⎣ _−_ **c**
**0**



⎡

   -    s.t. **A** _−_ **A** **I** ⎣



⎤


⎦ = **b**



⎡



⎤



**u**
⎣ **v**
**s**



**u**
⎣ **v**
**s**



⎦ _≥_ **0** _._



**2.2** **Graphical** **Interpretation** **of** **a** **Two-Variable** **Example**


Banks need to consider regulations when determining their business strategy. In
this section, we consider the Basel III regulations (Basel Committee on Banking Supervision, 2011). We present a simplified example following the paper of
Pokutta and Schmaltz (2012). Consider a bank with total deposits _D_ and loans
_L_ . The loans may default and the deposits are exposed to early withdrawal. The
bank holds capital _C_ in order to buffer against possible default losses on the
loans, and it holds a liquidity reserve _R_ to buffer against early withdrawals on
the deposits. The balance sheet of the bank satisfies _L_ + _R_ = _D_ + _C_ . Normalizing
the total assets to 1, we have _R_ = 1 _−_ _L_ and _C_ = 1 _−_ _D_ . Basel III regulations
require banks to satisfy four minimum ratio constraints in order to buffer against
different types of risk:



**Capital** **ratio:** _[C]_



**Capital** **ratio:** _L_ _[≥]_ _[r]_ [1]

**Leverage** **ratio:** _C_ _≥_ _r_ 2



**Liquidity** **coverage** **ratio:** _[R]_



_D_ _[≥]_ _[r]_ [3]



**Net** **stable** **funding** **ratio:** _[αD]_ [ +] _[ C]_



_≥_ _r_ 4,
_L_



where the ratios _r_ 1 _, r_ 2 _, r_ 3 _, r_ 4 _, α_ are computed for each bank based on the riskiness
of its loans and the likelihood of early withdrawals on deposits. To illustrate,
consider a bank with _r_ 1 = 0 _._ 3, _r_ 2 = 0 _._ 1, _r_ 3 = 0 _._ 25, _r_ 4 = 0 _._ 7, _α_ = 0 _._ 3. Expressing
the four ratio constraints in terms of the variables _D_ and _L_, we get


_D_ + 0 _._ 3 _L ≤_ 1
_D_ _≤_ 0 _._ 9
0 _._ 25 _D_ + _L ≤_ 1
0 _._ 7 _D_ + 0 _._ 7 _L ≤_ 1 _._


Figure 2.1 displays a plot of the feasible region of this system of inequalities in
the plane ( _D, L_ ).
Given this feasible region, the objective of the bank is to maximize the margin
income _mDD_ + _mLL_ that it makes on its products; where _mD_ is the margin that


16 **Linear** **Programming:** **Theory** **and** **Algorithms**



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-28-0.png)













0 1


**Figure** **2.1** Basel III regulations


the bank makes on its deposits and _mL_ is the margin charged on its loans. For
example, if _mD_ = 0 _._ 02 and _mL_ = 0 _._ 03, the best solution that satisfies all the
constraints corresponds to the vertex _D_ = 0 _._ 571 _, L_ = 0 _._ 857 on the boundary of
the feasible region, at the intersection of the lines 0 _._ 25 _D_ + _L_ = 1 and 0 _._ 7 _D_ +
0 _._ 7 _L_ = 1. This means that the bank should have 57.1% of its liabilities in deposits
and 42.9% in capital, and it should have 85.7% of its assets in loans and the
remaining 14.3% in liquidity reserve. The fact that an optimal solution occurs
at a vertex of the feasible region is a property of linear programs that extends
to higher dimensions than 2: To find an optimal solution of a linear program,
it suffices to restrict the search to vertices of the feasible region. This geometric
insight is the basis of the simplex method, which goes from one vertex of the
feasible region to an adjacent one with a better objective value until it reaches
an optimum. An algebraic description of the simplex method that can be coded
on a computer is presented in Section 2.7.1.


**2.3** **Numerical** **Linear** **Programming** **Solvers**


There are a variety of both commercial and open-source software packages for
linear programming. Most of these packages implement the algorithms described
in Section 2.7 below. Next we illustrate two of these solvers by applying them to
Example 2.1.


Excel Solver


Figure 2.2 displays a printout of an Excel spreadsheet implementation of the
linear programming model for Example 2.1 as well as the dialog box obtained
when we run the Excel add-in Solver. The spreadsheet model contains the three


**2.4** **Sensitivity** **Analysis** 17


components of the linear program. The decision variables are in the range B4:E4.
The objective is in cell F3. The left- and right-hand sides of the equality constraint are in the cells F4 and H4 respectively. Likewise, the left- and righthand sides of the three inequality constraints are in the ranges F8:F10 and
H8:H10 respectively. These components are specified in the Solver dialog box.
In addition, the Solver options are used to indicate that this is a linear model
and that the variables are non-negative.


**Figure** **2.2** Spreadsheet implementation and the Solver dialog box for the fund
allocation model


MATLAB CVX


Figure 2.3 displays a CVX script for the same problem. The script can be run
provided the freely available CVX toolbox is installed.


Either Excel Solver or MATLAB CVX find the following optimal solution to
the problem in Example 2.1:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-29-0.png)

0 _._ 0000
12 _._ 6316
46 _._ 3158
21 _._ 0526



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-29-1.png)

⎤


_,_
⎥⎥⎦



**x** _[∗]_ =



⎡

⎢⎢⎣



and the corresponding optimal objective value 10.9895 (recall that the units are
in $1000s).


**2.4** **Sensitivity** **Analysis**


In addition to the optimal solution, the process of solving a linear program also
generates some interesting _sensitivity information_ via the so-called _shadow prices_


18 **Linear** **Programming:** **Theory** **and** **Algorithms**


**Figure** **2.3** MATLAB CVX code for the fund allocation model


or _dual_ _values_ associated with the constraints. Assume that the constraints of a
linear program, and hence the shadow prices, are indexed by _i_ = 1 _, . . ., m_ . The
_shadow_ _price yi_ _[∗]_ [of the] _[ i]_ [th constraint has the following sensitivity interpretation:]


If the right-hand side of the _i_ th constraint changes by Δ, then the optimal
value of the linear program changes by Δ _· yi_ _[∗]_ [as] [long] [as] [Δ] [is] [within] [a]
certain range.


Both Excel Solver and MATLAB CVX compute the shadow prices implicitly.
To make this information explicit in Excel Solver we request a sensitivity report
after running it as shown in Figure 2.4.


**Figure** **2.4** Requesting sensitivity report in Solver


Figure 2.5 displays the sensitivity report for Example 2.1.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-30-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-30-1.png)
**2.4** **Sensitivity** **Analysis** 19


**Figure** **2.5** Sensitivity report


The values _yi_ _[∗]_ [can] [be] [found] [in] [the] [column] [labeled] [“Shadow] [Price”.] [In] [addi-]
tion, the “Allowable Increase” and “Allowable Decrease” columns indicate the
range of change for each right-hand side of a constraint where the sensitivity
analysis holds. For example, if the right-hand side of the large-capitalization
constraint


0 _._ 5 **x** 1 + 0 _._ 3 **x** 2 + 0 _._ 25 **x** 3 + 0 _._ 6 **x** 4 _≥_ 28


changes from 28 to 28+Δ, then the optimal value changes by _−_ 0 _._ 231579 _·_ Δ. This
holds provided Δ is within the allowable range [ _−_ 6 _._ 6666 _,_ 6] _._ If the requirement
on large-cap stocks is reduced from 35% to 30%, the change in right-hand side is
Δ = _−_ 0 _._ 05 _∗_ 80 = _−_ 4, which is within the allowable range. Therefore the optimal
objective value increases by _−_ 0 _._ 231579 _·_ ( _−_ 4) = 0 _._ 926316. Because our units are
in $1000, this means that the expected return on an optimal portfolio would
increase by $926.32 if we relaxed the constraint on large-cap stocks by 5%, from
35% to 30%.

The shadow prices of the non-negativity constraints are the “Reduced Cost”
displayed in the initial part of the sensitivity report. This is also the convention
for more general lower and upper bounds on the decision variables. Observe that
in Example 2.1 the reduced costs of the non-zero variables are zero. The reduced
costs also have a deeper meaning in the context of the simplex algorithm for
linear programming as described in Section 2.7.1 below.

A linear programming model is _non-degenerate_ if all of the allowable increase
and allowable decrease limits are positive. The above linear programming model
is non-degenerate.

In CVX this information can also be obtained by including a few additional
pieces of code to save the dual information in the dual variables y,z as shown
in Figure 2.6.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-31-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-31-1.png)
20 **Linear** **Programming:** **Theory** **and** **Algorithms**


**Figure** **2.6** MATLAB CVX code with dual variables


Both solvers yield the following dual values: **y** _[∗]_ = 0 _._ 22, **z** _[∗]_ =



⎡

_−_ 0 _._ 231579
⎣ _−_ 0 _._ 005263
0



⎤


⎦ _._



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-32-0.png)

We note that some solvers may flip the sign of the dual values. In particular,



⎡



⎤



the output of the above CVX code yields the values _−_ 0 _._ 22 and



0 _._ 231579
⎣0 _._ 005263
0



⎦ _._ It is



important to be mindful of this subtlety when interpreting the dual information.
The ambiguity can be easily resolved by thinking in terms of sensitivity analysis.
In this particular example, it is clear that the shadow price of the first constraint
should be non-negative as more capital should lead to a higher return. Likewise,
it is clear that the shadow prices of the other constraints should be non-positive
as more stringent diversification constraints, e.g., higher percentage in large cap,
reduces the set of feasible portfolios and hence can only lead to portfolios with
return less than or equal to the optimal return of the original problem.


**2.5** ***Duality**


Every linear program has an associated _dual_ linear programming problem. The
properties of these two linear programs and how they are related to each other
have deep implications. In particular, duality enables us to answer the following
kinds of questions:


_•_ Can we recognize an optimal solution?

_•_ Can we construct an algorithm to find an optimal solution?

_•_ Can we assess how suboptimal a current feasible solution is?


The attentive reader may have noticed that dual variables were already mentioned in Section 2.4 when discussing sensitivity analysis with CVX. This is not a


**2.5** ***Duality** 21


coincidence. There is a close connection between duality and sensitivity analysis.
The vector of shadow prices of the constraints of a linear program corresponds
precisely to the optimal solution of its dual.
Consider the following linear program in standard form, which we shall refer
to as the _primal_ problem:

min **c** [T] **x**
s.t. **Ax** = **b** (2.1)
**x** _≥_ **0** _._


The following linear program is called the _dual_ problem:


max **b** [T] **y**
(2.2)
s.t. **A** [T] **y** _≤_ **c** _._


Sometimes it is convenient to rewrite the constraints in the dual problem as
equality constraints by means of slack variables. That is, problem (2.2) can also
be written as
max **b** [T] **y**
s.t. **A** [T] **y** + **s** = **c** (2.3)
**s** _≥_ **0** _._


There is a deep connection between the primal and dual problems. The next
result follows by construction.


**Theorem** **2.3** (Weak duality) _Assume_ **x** _is_ _a_ _feasible_ _point_ _for_ (2.1) _and_ **y** _is_ _a_
_feasible_ _point_ _for_ (2.2) _._ _Then_


**b** [T] **y** _≤_ **c** [T] **x** _._


_Proof_ Under the assumptions on **x** and **y** it follows that


**b** [T] **y** = ( **Ax** ) [T] **y** = ( **A** [T] **y** ) [T] **x** _≤_ **c** [T] **x** _._


The following (not so straightforward) result also holds.


**Theorem** **2.4** (Strong duality) _Assume_ _one_ _of_ _the_ _problems_ (2.1) _or_ (2.2) _is_
_feasible._ _Then_ _this_ _problem_ _is_ _bounded_ _if_ _and_ _only_ _if_ _the_ _other_ _one_ _is_ _feasible._ _In_
_that_ _case_ _both_ _problems_ _have_ _optimal_ _solutions_ _and_ _their_ _optimal_ _values_ _are_ _the_
_same._


We refer the reader to Bertsimas and Tsitsiklis (1997) or Chv´atal (1983) for
a proof of Theorem 2.4. This result is closely related to the following classical
properties of linear inequality systems.


**Theorem** **2.5** _Assume_ **A** _∈_ R _[m][×][n]_ _and_ **b** _∈_ R _[m]_ _._ _In_ _each_ _of_ _the_ _following_ _cases_
_exactly_ _one_ _of_ _the_ _systems_ (I) _or_ (II) _has_ _a_ _solution_ _but_ _not_ _both._


(a) _Farkas’s_ _lemma_


**Ax** = **b** _,_ **x** _≥_ **0** _,_ (I)


**A** [T] **y** _≤_ **0** _,_ **b** [T] **y** _<_ 0 _._ (II)


22 **Linear** **Programming:** **Theory** **and** **Algorithms**


(b) _Gordan’s_ _theorem_


**Ax** = **0** _,_ **x** ≩ **0** _,_ (I)


**A** [T] **y** _>_ **0** _._ (II)


(c) _Stiemke’s_ _theorem_


**Ax** = **0** _,_ **x** _>_ **0** _,_ (I)


**A** [T] **y** ≩ **0** _._ (II)


The equivalence between Theorems 2.4 and 2.5 is explored in Exercises 2.11
and 2.12.
We next present a derivation of the dual problem via the so-called Lagrangian
function. This derivation has the advantage of introducing an important concept
that we will encounter again in later chapters. Associated with the optimization
problem (2.1) consider the _Lagrangian_ function defined by


_L_ ( **x** _,_ **y** _,_ **s** ) := **c** [T] **x** + **y** [T] ( **b** _−_ **Ax** ) _−_ **s** [T] **x** _._


The constraints of (2.1) can be encoded using the Lagrangian function via the
following observation: For a given vector **x**

             **c** T **x** if **Ax** = **b** and **x** _≥_ **0**
max **sy** _≥,_ **s0** _L_ ( **x** _,_ **y** _,_ **s** ) = + _∞_ otherwise.


Therefore the primal problem (2.1) can be written as


min **x** [max] **sy** _≥,_ **s0** _L_ ( **x** _,_ **y** _,_ **s** ) _._ (2.4)


On the other hand, observe that _L_ ( **x** _,_ **y** _,_ **s** ) = **b** [T] **y** + ( **c** _−_ **A** [T] **y** _−_ **s** ) [T] **x** _._ Hence for
a given pair of vectors ( **y** _,_ **s** )

              **b** T **y** if **A** [T] **y** + **s** = **c**
min
**x** _[L]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ s]** [) =] _−∞_ otherwise.


The dual problem is obtained by flipping the order of the min and max operations
in (2.4). Indeed, observe that the dual problem (2.3) can be written as


max **sy** _≥,_ **s0** min **x** _[L]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ s]** [)] _[.]_


A similar procedure can be applied to obtain the dual of a linear program that
is not necessarily in standard form. For example, the primal problem


min **c** [T] **x**
s.t. **Ax** _≥_ **b** (2.5)
**x** _≥_ **0**


can be written as


min max
**x** **y** _≥_ 0 _,_ **s** _≥_ **0** _[L]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ s]** [)] _[,]_


**2.6** ***Optimality** **Conditions** 23


for _L_ ( **x** _,_ **y** _,_ **s** ) = **c** [T] **x** + **y** [T] ( **b** _−_ **Ax** ) _−_ **s** [T] **x** _._ In this case the dual problem is


max
**y** _≥_ 0 _,_ **s** _≥_ **0** [min] **x** _[L]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ s]** [)] _[,]_


and can be rewritten as


max **b** [T] **y**
**y**



s.t. **A** [T] **y** _≤_ **c**
**y** _≥_ **0** _._



(2.6)



Again the weak and strong duality properties hold for the pair of problems (2.5)
and (2.6).
Consider the linear programming model of Example 2.1, namely


max **r** [T] **x**
**x**



s.t. **Ax** = **b**
**Dx** _≥_ **d**
**x** _≥_ **0** _._


We give a derivation for its dual. Observe that (2.7) can be recast as


max **x** **y** min _,_ **w** _,_ **s** _L_ ( **x** _,_ **y** _,_ **w** _,_ **s** )
**w** _≥_ 0 _,_ **s** _≥_ **0**


for


_L_ ( **x** _,_ **y** _,_ **w** _,_ **s** ) = **r** [T] **x** + **y** [T] ( **b** _−_ **Ax** ) + **w** [T] ( **Dx** _−_ **d** ) + **s** [T] **x**

= **b** [T] **y** _−_ **d** [T] **w** + **x** [T] ( **r** _−_ **A** [T] **y** + **D** [T] **w** + **s** ) _._


It follows that its dual **y** min _,_ **w** _,_ **s** max **x** _L_ ( **x** _,_ **y** _,_ **s** _,_ **z** ) can be rewritten as
**w** _≥_ 0 _,_ **s** _≥_ **0**


min **b** [T] **y** _−_ **d** [T] **w**
**y** _,_ **z**

s.t. **A** [T] **y** _−_ **D** [T] **w** _≥_ **r**
**w** _≥_ **0** _._



(2.7)


(2.8)



An alternative way to obtain the dual (2.8) is to rewrite (2.7) in standard form
and derive its standard dual. The latter turns out to be equivalent to (2.8). (See
Exercise 2.6.)


**2.6** ***Optimality** **Conditions**


Consider again the linear programming problem (2.1). A powerful consequence
of Theorem 2.4 is a set of _optimality_ _conditions_ that completely characterize the
solutions to both (2.1) and (2.2).


24 **Linear** **Programming:** **Theory** **and** **Algorithms**


**Theorem 2.6** (Optimality conditions) _The vectors_ **x** _∈_ R _[n]_ _and_ ( **y** _,_ **s** ) _∈_ R _[m]_ _×_ R _[n]_

_are_ _respectively_ _optimal_ _solutions_ _to_ (2.1) _and_ (2.3) _if_ _and_ _only_ _if_ _they_ _satisfy_ _the_
_following_ _system_ _of_ _equations_ _and_ _inequalities:_



**A** [T] **y** + **s** = **c**
**Ax** = **b**
**x** _,_ **s** _≥_ **0**
_xisi_ = 0 _,_ _i_ = 1 _, . . ., n._



(2.9)



The equations _xisi_ = 0 are known as the complementary slackness conditions. They imply that, if a dual constraint ( **A** [T] **y** ) _i_ _≤_ _ci_ holds strictly (that is,
( **A** [T] **y** ) _i_ _<_ _ci_ ), then the corresponding primal variable _xi_ must be 0. And conversely, if _xi_ _>_ 0, the corresponding dual constraint is tight, that is, ( **A** [T] **y** ) _i_ = _ci_ .
The optimality conditions (2.9) provide an avenue for constructing algorithms
to solve the linear programming problems (2.1) and (2.3). To lay the groundwork
for discussing them, we next state two interesting results concerning the optimal
solutions of a linear programming problem and its dual.


**Theorem** **2.7** (Strictly complementary solutions) _Assume_ **A** _∈_ R _[m][×][n]_ _is_ _full_ _row_
_rank,_ **b** _∈_ R _[m]_ _,_ _and_ **c** _∈_ R _[n]_ _are_ _such_ _that_ _both_ (2.1) _and_ (2.2) _are_ _feasible._ _Then_
_there_ _exist_ _optimal_ _solutions_ **x** _[∗]_ _to_ (2.1) _and_ ( **y** _[∗]_ _,_ **s** _[∗]_ ) _to_ (2.3) _such_ _that_


**x** _[∗]_ + **s** _[∗]_ _>_ **0** _._


For a matrix **A** and a subset _B_ of its columns, let **A** _B_ denote the submatrix of
**A** containing the columns in _B_ . For a square non-singular matrix **D**, the notation
**D** _[−]_ [T] stands for ( **D** _[−]_ [1] ) [T] .


**Theorem** **2.8** (Optimal basic feasible solutions) _Assume_ **A** _∈_ R _[m][×][n]_ _is_ _full_ _row_
_rank,_ **b** _∈_ R _[m]_ _,_ _and_ **c** _∈_ R _[n]_ _are_ _such_ _that_ _both_ (2.1) _and_ (2.2) _are_ _feasible._ _Then_
_there_ _exists_ _a_ _partition_ _B ∪_ _N_ = _{_ 1 _, . . ., n}_ _with_ _|B|_ = _m_ _and_ **A** _B_ _non-singular,_
_such_ _that_

**x** _[∗]_ _B_ [=] **[ A]** _B_ _[−]_ [1] **[b]** _[,]_ **x** _[∗]_ _N_ [=] **[ 0]** _[,]_ **y** _[∗]_ = **A** _[−]_ _B_ [T] **[c]** _[B]_


_are_ _optimal_ _solutions_ _to_ (2.1) _and_ (2.2) _respectively._


**2.7** ***Algorithms** **for** **Linear** **Programming**


We next sketch the two main algorithmic schemes for solving linear programs,
namely the _simplex_ _method_ and _interior-point_ _methods._ Our discussion of these
two important topics is only intended to give the reader a basic understanding
of the main solution techniques for linear programming. For a more detailed and
thorough discussion of these two classes of algorithms, see Bertsimas and Tsitsiklis (1997), Boyd and Vandenberghe (2004), Chv´atal (1983), Renegar (2001),
and Ye (1997).
We follow the usual convention of assuming that the problem of interest is in
standard form as in (2.1) and (2.3) and _A_ has full row rank.


**2.7** ***Algorithms** **for** **Linear** **Programming** 25


2.7.1 The Simplex Method


One of the most popular algorithms for linear programming is the _simplex_
_method._ It generates a sequence of iterates that satisfy **Ax** = **b** _,_ **x** _≥_ **0**, **A** [T] **y** + **s** =
**c** and _xisi_ = 0, with _i_ = 1 _, . . ., n_ . Each iteration of the algorithm aims to make
progress towards satisfying **s** _≥_ **0** . Theorem 2.6 guarantees that the algorithm
terminates with an optimal solution when this goal is attained. The _dual_ simplex
method is a variant that generates a sequence of iterates satisfying **Ax** = **b**,
**A** [T] **y** + **s** = **c**, **s** _≥_ **0**, and _xisi_ = 0, for _i_ = 1 _, . . ., n_ . Each iteration of the
algorithm aims to make progress towards satisfying **x** _≥_ **0** .
The simplex method relies on the property stated in Theorem 2.8. The gist of
the method is to search for an _optimal_ _basis_ ; that is, a subset _B_ _⊆{_ 1 _, . . ., n}_ as
in Theorem 2.8. To motivate and describe the algorithm we next introduce some
terminology and key observations.
A _basis_ is a subset _B_ _⊆{_ 1 _, . . ., n}_ such that _|B|_ = _m_ and **A** _B_ is a nonsingular matrix. A basis _B_ defines the _basic_ _solution_ **x** ¯ = (¯ **x** _B,_ ¯ **x** _N_ ) where **x** ¯ _B_ =
**A** _[−]_ _B_ [1] **[b]** _[,]_ **[x]** [¯] _[N]_ [=] **[0]** [.] [Observe] [that] **[x]** [¯] [solves] [the] [system] [of] [equations] **[Ax]** [=] **[b]** _[.]_ [The]
vector **x** ¯ is a _basic_ _feasible_ _solution_ if in addition **x** ¯ _≥_ 0. A basis _B_ also defines
the _reduced_ _cost_ **c** ¯ = **c** _−_ **A** [T] **A** _[−]_ _B_ [T] **[c]** _[B][.]_ [The] [following] [fact] [suggests] [the] [main] [idea]
for the simplex method.


**Proposition 2.9** _Assume B_ _⊆{_ 1 _, . . ., n}_ _is_ _a_ _basis._ _Let_ **x** ¯ _and_ **c** ¯ _be_ _respectively_
_the_ _corresponding_ _basic_ _solution_ _and_ _reduced_ _cost_ _vector._ _If_ **x** ¯ _≥_ 0 _and_ **c** ¯ _≥_ 0 _then_
**x** ¯ _is_ _an_ _optimal_ _solution_ _to_ (2.1) _._ _Furthermore,_ _in_ _this_ _case_ **y** ¯ = **A** _[−]_ _B_ [T] **[c]** [¯] _[B]_ _[is]_ _[an]_
_optimal_ _solution_ _to_ (2.2) _._


An _optimal_ _basis_ is a basis that satisfies the conditions **x** ¯ _≥_ 0 and ¯ **c** _≥_ 0 stated
above. Given a basis _B_ that is not optimal, the main idea of the simplex method
is to generate a better basis by replacing an index from _B_ . To that end, a possible
avenue is as follows. Suppose _B_ is a basis with a basic feasible solution **x** ¯. If _B_
is not an optimal basis, then _c_ ¯ _j_ _<_ 0 for some _j_ _̸∈_ _B_ . Thus for _α_ _>_ 0 the point
**x** ( _α_ ) defined by

**x** _B_ ( _α_ ) = **x** ¯ _B_ _−_ _α_ **A** _[−]_ _B_ [1] **[A]** _[j][,]_

_xj_ ( _α_ ) = _α,_ _xi_ ( _α_ ) = 0 for all other indices _i ̸∈_ _B ∪{j}_


satisfies

**c** [T] **x** ( _α_ ) = **c** [T] **x** ¯ + _αc_ ¯ _j_ _<_ **c** [T] **x** ¯ _._


Hence we can get a point with better (lower) objective value than the current
basic feasible solution _x_ ¯. We would like this new point to remain feasible. Unless
the problem is unbounded, there is a length _α_ _[∗]_ _≥_ 0 that makes one of the current
basic components _ℓ_ of **x** drop to zero while keeping all of them non-negative.
When _α_ _[∗]_ _>_ 0, a basis with a better basic feasible solution can be obtained by
replacing _ℓ_ with _j_ . The simplex method modifies the basis in this way, even in the
degenerate case when _α_ _[∗]_ = 0, which may occur in some iterations. Algorithm 2.1
gives a formal description of the simplex method.


26 **Linear** **Programming:** **Theory** **and** **Algorithms**


**Algorithm** **2.1** The simplex method

1: start with a basis _B_ _⊆{_ 1 _, . . ., n}_ such that **x** ¯ is a basic feasible solution

2: **while** **c** ¯ _̸≥_ **0** **do**



3: choose an index _j_ such that _c_ ¯ _j_ _<_ 0



4: compute **u** = **A** _[−]_ _B_ [1] **[A]** _[j]_
5: **if** **u** _≤_ **0** **then** HALT; the problem is unbounded **end** **if**



_x_ ¯ _i_
6: let _α_ _[∗]_ := min = _[x]_ [¯] _[ℓ]_
_i_ : _ui>_ 0 _ui_ _uℓ_



_i_ : _ui>_ 0 _ui_ _uℓ_

7: form a new basis by replacing _ℓ_ with _j_



8: update the basic feasible solution by replacing **x** ¯ with **x** ( _α_ _[∗]_ )

9: **end** **while**


Observe that the basic feasible solution ¯ **x** and the reduced cost ¯ **c** corresponding
to a basis _B_ satisfy **x** ¯ _N_ = **0** and **c** ¯ _B_ = **0** where _N_ = _{_ 1 _, . . ., n} \ B_ . Hence the
simplex method only needs to keep track of **x** ¯ _B_ and **c** ¯ _N_ . We next illustrate the
simplex method in the linear programming model from Example 2.2. If we start
with the initial basis _B_ = _{_ 3 _,_ 4 _,_ 5 _}_ the algorithm proceeds as follows.


                   - �T                   - �T
**Iteration** **1:** _B_ = _{_ 3 _,_ 4 _,_ 5 _},_ **x** ¯ _B_ = _x_ ¯3 _x_ ¯4 _x_ ¯5 = 100 150 360 _,_ **c** ¯ _N_ =

     - �T     -     _c_ ¯1 _c_ ¯2 = _−_ 4 _−_ 3 _̸≥_ **0** _._ Choose _j_ = 1 as the new index to enter




              -               -               - �T
the basis. Compute **u** = _u_ 3 _u_ 4 _u_ 5 = **A** _[−]_ _B_ [1] **[A]** _[j]_ [=] 1 2 3 and



= _[x]_ [¯][4]
2 _u_ 4



_x_ ¯ _i_
_α_ _[∗]_ := min = [150]
_i_ : _ui>_ 0 _ui_ 2



. Hence _ℓ_ = 4 is the index leaving the
_u_ 4



basis. Update the basis and basic feasible solution to _B_ = _{_ 3 _,_ 1 _,_ 5 _}_ and

   - �T    - �T
**x** ¯ _B_ = _x_ ¯3 _x_ ¯1 _x_ ¯5 = 25 75 135 .




                    - �T                    - �T
**Iteration** **2:** _B_ = _{_ 3 _,_ 1 _,_ 5 _},_ **x** ¯ _B_ = _x_ ¯3 _x_ ¯1 _x_ ¯5 = 25 75 135 _,_ **c** ¯ _N_ =

     -     -     - �T
_c_ ¯2 _c_ ¯4 = _−_ 1 0 _̸≥_ **0** _._ Choose _j_ = 2 as the new index to enter



the basis. Compute **u** = - _u_ 3 _u_ 1 _u_ 5�T = **A** _−B_ 1 **[A]** _[j]_ [=] �1 _/_ 2 1 _/_ 2 5 _/_ 2�T




[25] _[x]_ [¯][3]

1 _/_ 2 [=] _u_ 3



_x_ ¯ _i_
and _α_ _[∗]_ := min = [25]
_i_ : _ui>_ 0 _ui_ 1 _/_



. Hence _ℓ_ = 3 is the index leaving the
_u_ 3



basis. Update the basis and basic feasible solution to _B_ = _{_ 2 _,_ 1 _,_ 5 _}_ and

        - �T        - �T
_x_ ¯ _B_ = _x_ ¯2 _x_ ¯1 _x_ ¯5 = 50 50 10 .

                    - �T                    - �T
**Iteration** **3:** _B_ = _{_ 2 _,_ 1 _,_ 5 _},_ _x_ ¯ _B_ = _x_ ¯2 _x_ ¯1 _x_ ¯5 = 50 50 10 _,_ **c** ¯ _N_ =

     - �T     - �T
_c_ 3 _c_ 4 = 2 1 _≥_ **0** _._ Hence _B_ is an optimal basis and


                   - �T
**x** ¯ = 50 50 0 0 10


is an optimal solution.


Notice how, geometrically, the simplex iterations move from one vertex of the
feasible region to an adjacent vertex until an optimum solution is identified. See
Figure 2.7.


**2.7** ***Algorithms** **for** **Linear** **Programming** 27



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-39-0.png)



**Figure** **2.7** Simplex iterations


2.7.2 Dual Simplex Method











The above version of the simplex method is a _primal_ _version_ that generates
primal feasible iterates and aims for dual feasibility. The _dual_ _simplex_ _method_
generates dual feasible iterates and aims for primal feasibility. The logic behind
the algorithm is similar. Suppose _B_ is a basis with reduced cost **c** ¯ _≥_ **0** _._ This
means that **y** ¯ = **A** _[−]_ _B_ [T] **[c]** _[B]_ [is] [a] [dual] [feasible] [solution] [with] [slack] **[c]** [¯][ =] **[ c]** _[ −]_ **[A]** [T] **[y]** _[≥]_ **[0]** [.]
If _B_ is not an optimal basis, then _x_ ¯ _ℓ_ _<_ 0 for some _ℓ_ _∈_ _B._ Let **e** _ℓ_ _∈_ R _[n]_ denote the
vector with _ℓ_ th component equal to 1 and all others equal to 0. For _α_ _>_ 0 the
vector **y** ( _α_ ) defined by

**y** ( _α_ ) = **y** ¯ _−_ _α_ **A** _[−]_ _B_ [T] **[e]** _[ℓ]_


satisfies


**b** [T] **y** ( _α_ ) = **b** [T] **y** ¯ _−_ _αx_ ¯ _ℓ_ _>_ **b** [T] **y** ¯ _._


Observe that the slack of **y** ( _α_ ) is


**c** ( _α_ ) = ¯ **c** + _α_ **A** [T] **A** _[−]_ _B_ [T] **[e]** _[ℓ][.]_


Hence we can get a point with better (lower) objective value than the current
basic feasible solution **x** ¯ _._ Unless the problem is unbounded, there is a length
_α_ _[∗]_ _≥_ 0 that makes one of the non-basic components _j_ of **c** ( _α_ ) drop to zero while
keeping all of them non-negative. In this case a basis with a better dual solution
can be obtained by replacing _ℓ_ with _j_ . Algorithm 2.2 gives a formal description
of the dual simplex method.
We illustrate the dual simplex in the following variation of Example 2.2.
Suppose we add the constraint


6 _x_ 1 + 5 _x_ 2 _≤_ 500 _._


28 **Linear** **Programming:** **Theory** **and** **Algorithms**


**Algorithm** **2.2** Dual simplex method

1: start with a basis _B_ _⊆{_ 1 _, . . ., n}_ such that the reduced cost ¯ **c** is non-negative

2: **while** **x** ¯ _̸≥_ **0** **do**

3: choose an index _ℓ_ _∈_ _B_ such that _x_ ¯ _ℓ_ _<_ 0



4: compute **v** = **A** [T] **A** _[−]_ _B_ [T] _[e][ℓ]_
5: **if** **v** _≥_ **0** **then** HALT; the problem is unbounded **end** **if**



_c_ ¯ _i_
6: let _α_ _[∗]_ := min _[c]_ [¯] _[j]_
_i_ : _vi<_ 0 _|vi|_ [=] _|vj_



_i_ : _vi<_ 0 _|vi|_ _|vj|_

7: form a new basis by replacing _ℓ_ with _j_



8: update the dual feasible solution by replacing **y** ¯ with **y** ( _α_ _[∗]_ )

9: **end** **while**


After adding the relevant new slack variable the new linear program is


min _−_ 4 _x_ 1 _−_ 3 _x_ 2
s.t.
_x_ 1 + _x_ 2 + _x_ 3 = 100
2 _x_ 1 + _x_ 2 + _x_ 4 = 150
3 _x_ 1 + 4 _x_ 2 + _x_ 5 = 360
6 _x_ 1 + 5 _x_ 2 + _x_ 6 = 500
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _, x_ 5 _, x_ 6 _≥_ 0 _._


If we start with the initial basis _B_ = _{_ 1 _,_ 2 _,_ 5 _,_ 6 _}_ the algorithm proceeds as
follows.

                   - �T                    - �T
**Iteration** **1:** _B_ = _{_ 1 _,_ 2 _,_ 5 _,_ 6 _}_, **c** ¯ _N_ = _c_ ¯3 _c_ ¯4 = 2 1 _≥_ **0**, and

            - �T             - �T
**x** ¯ _B_ = _x_ ¯1 _x_ ¯2 _x_ ¯5 _x_ ¯6 = 50 50 10 _−_ 50 _̸≥_ **0** _._



Choose _ℓ_ = 6 as the index to leave the basis. Compute **v** = **A** [T] **A** _[−]_ _B_ [T] _[e][ℓ]_ [=]
�0 0 _−_ 4 _−_ 1 0 1�T and _α∗_ := min _c_ ¯ _i_ [2] _[c]_ [¯][3] [Hence] _[j]_ [= 3]
_i_ : _vi<_ 0 _|vi|_ [=] 4 [=] _|v_ 3 _|_ [.]

is the index entering the basis. Update the basis, reduced cost, and basic

                         -                          -                          - �T
solution respectively to _B_ = _{_ 1 _,_ 2 _,_ 5 _,_ 3 _},_ _c_ ¯ _N_ = _c_ ¯4 _c_ ¯6 = 0 _._ 5 0 _._ 5 _,_

       - �T       - �T
and **x** ¯ _B_ = _x_ ¯1 _x_ ¯2 _x_ ¯5 _x_ ¯3 = 62 _._ 5 25 72 _._ 5 12 _._ 5 . The new
basic solution is non-negative and hence it is an optimal solution.




[2] _[c]_ [¯][3]

4 [=] _|v_ 3




[Hence] _[j]_ [= 3]
_|v_ 3 _|_ [.]



is the index entering the basis. Update the basis, reduced cost, and basic

                         -                          -                          - �T
solution respectively to _B_ = _{_ 1 _,_ 2 _,_ 5 _,_ 3 _},_ _c_ ¯ _N_ = _c_ ¯4 _c_ ¯6 = 0 _._ 5 0 _._ 5 _,_



2.7.3 Interior-Point Methods


In contrast to the simplex method, interior-point methods generate a sequence
of iterates that satisfy **x** _,_ **s** _>_ **0** . Each iteration of the algorithm aims to make
progress towards satisfying **Ax** = **b** _,_ **A** [T] **y** + **s** = **c** _,_ and _xisi_ = 0 _,_ _i_ = 1 _, . . ., n._
Throughout this section we use the following notational convention: Given
a vector **x** _∈_ R _[n]_, let **X** _∈_ R _[n][×][n]_ denote the diagonal matrix defined by _Xii_ =
_xi,_ _i_ = 1 _, . . ., n_, and let **1** _∈_ R _[n]_ denote the vector whose components are all ones.


**2.7** ***Algorithms** **for** **Linear** **Programming** 29



The optimality conditions (2.9) can be restated as
⎡ ⎤ ⎡ ⎤



⎤



⎡



⎤



**A** [T] **y** + **s** _−_ **c**
⎣ **Ax** _−_ **b**
**XS1**



⎦ =



**0**
⎣ **0**
**0**



⎦ _,_ **x** _,_ **s** _≥_ **0** _._



Given _μ_ _>_ 0, let ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) be the solution to the following perturbed
version of the above optimality conditions:
⎡ ⎤ ⎡ ⎤



⎤



⎡



**0**
⎣ **0**
_μ_ **1**



⎤



**A** [T] **y** + **s** _−_ **c**
⎣ **Ax** _−_ **b**
**XS1**



⎦ =



⎦ _,_ **x** _,_ **s** _>_ **0** _._



The first condition above can be written as **r** _μ_ ( **x** _,_ **y** _,_ **s** ) = **0** for the _residual_ _vector_



**r** _μ_ ( **x** _,_ **y** _,_ **s** ) :=



⎡ ⎤

**A** [T] **y** + **s** _−_ **c**
⎣ **Ax** _−_ **b** ⎦ _._
**XS1** _−_ _μ_ **1**



The _central_ _path_ is the set _{_ ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) : _μ >_ 0 _}_ . It is intuitively clear that
( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) converges to an optimal solution to both (2.1) and (2.3) as _μ_
goes to 0. This suggests the following algorithmic strategy: Suppose ( **x** _,_ **y** _,_ **s** ) is
“near” ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) for some _μ >_ 0. Use ( **x** _,_ **y** _,_ **s** ) to move to a better point
( **x** [+] _,_ **y** [+] _,_ **s** [+] ) “near” ( **x** ( _μ_ [+] ) _,_ **y** ( _μ_ [+] ) _,_ **s** ( _μ_ [+] )) for some _μ_ [+] _< μ_ .
It can be shown that if a point ( **x** _,_ **y** _,_ **s** ) is on the central path, then the
corresponding value of _μ_ satisfies **x** [T] **s** = _nμ._ Likewise, given **x** _,_ **s** _>_ **0**, define


_μ_ ( **x** _,_ **s** ) := **[x]** [T] **[s]**

_n_ _[.]_



To move from a current point ( **x** _,_ **y** _,_ **s** ) to a new point, we use the so-called
_Newton_ _step_ ; that is, the solution to the following system of equations:
⎡ ⎤ ⎡ ⎤ ⎡ ⎤



⎤


⎦



⎡



Δ **x**
⎣Δ **y**
Δ **s**



⎤



⎦ =



⎡



**c** _−_ **A** [T] **y** _−_ **s**
⎣ **b** _−_ **Ax**
_μ_ **1** _−_ **XS1**



⎤



**0** **A** [T] **I**
⎣ **A** **0** **0**
**S** **0** **X**



⎦ _._ (2.10)



Algorithm 2.3 presents a template for an interior-point method.


**Algorithm** **2.3** Interior-point method

1: choose **x** [0] _,_ **s** [0] _>_ 0

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve the Newton system (2.10) for ( **x** _,_ **y** _,_ **s** ) = ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ) and _μ_ :=
0 _._ 1 _μ_ ( **x** _[k]_ _,_ **s** _[k]_ )

4: choose a step length _α ∈_ (0 _,_ 1] and set ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) = ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ )+
_α_ (Δ **x** _,_ Δ **y** _,_ Δ **s** )

5: **end** **for**


30 **Linear** **Programming:** **Theory** **and** **Algorithms**


The step length _α_ in step 4 should be chosen so that **x** _[k]_ [+1] _,_ **s** _[k]_ [+1] _>_ 0 and
the size of **r** _μ_ ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) is sufficiently smaller than **r** _μ_ ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ). A _line-_
_search_ _procedure_ as the one described in Algorithm 2.4 is a popular strategy for
choosing the step length _α_ .


**Algorithm** **2.4** Line search to select the step length _α_

1: let _α_ max := max _{α_ : ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ) + _α_ (Δ **x** _,_ Δ **y** _,_ Δ **s** ) _≥_ 0 _}_

2: start with _α_ := 0 _._ 99 _α_ max
3: **while** _∥_ **r** _μ_ (( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ) + _α_ (Δ **x** _,_ Δ **y** _,_ Δ **s** )) _∥≥_ (1 _−_ 0 _._ 01 _α_ ) _∥_ **r** _μ_ ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ) _∥_ **do**

4: _α_ := _α/_ 2

5: **end** **while**


In contrast to the primal and dual simplex methods, which in principle generate either primal or dual feasible iterates and terminate after finitely many
iterations, interior-point methods typically generate infeasible iterates and converge to the optimal solution in the limit. In practice, the convergence is so fast
that in a few iterations the algorithm yields iterates that are within machine
precision of an exact optimal solution. The algorithm can also be enhanced to
detect infeasibility. It relies on the fact that when the primal or dual problem is
infeasible,When applied to Example 2.2 starting fromthe norm of the residual **r** _μ_ ( **x** _,_ **y** _,_ **s x** ) cannot [0] = **s** [0] =be�100driven _· · ·_ to zero.100�T _,_ **y** 0 =

**0**, the above interior-point algorithm generates the following sequence of iterates.
(For ease of notation we only display the first two entries of each iterate.)


Iteration 0 1 2 _· · ·_ 8 9


_x_ 1 100 19.7084 17.2976 _· · ·_ 49.9383 49.9962
_x_ 2 100 57.3930 41.6795 _· · ·_ 50.0436 50.0011


**2.8** **Notes**


The simplex method was developed by George Dantzig (1963). Clever implementations of the simplex method, such as the _revised_ _simplex_ and _simplex_ _tableau_,
perform iterations far more efficiently than what a naive recalculation of the
basic solution and reduced cost from scratch at each iteration would involve.
Detailed discussions on these implementations and other related issues can be
found in the books by Bertsimas and Tsitsiklis (1997) and Chv´atal (1983).
Interior-point methods for linear programming were introduced in a landmark paper by Karmarkar (1984) and subsequently triggered a massive burst of
research in optimization during the 1990s and early 2000s. The books by Renegar
(2001), Ye (1997), and Roos et al. (2005) present the main developments on this
topic.


**2.9** **Exercises** 31


State-of-the-art linear programming solvers such as CPLEX, MOSEK, Gurobi,
and others use implementations of both the simplex and interior-point methods.
These solvers can easily solve linear programs with millions of variables and
constraints.


**2.9** **Exercises**


**Exercise** **2.1** Draw the feasible region of the following two-variable linear
program:

max 2 _x_ 1 _−_ _x_ 2
_x_ 1 + _x_ 2 _≥_ 1
_x_ 1 _−_ _x_ 2 _≤_ 0
3 _x_ 1 + _x_ 2 _≤_ 6
_x_ 1 _, x_ 2 _≥_ 0 _._


Determine the optimal solution to this problem by inspection.


**Exercise** **2.2** Consider the following two-variable linear program:


min 2 _x_ 1 + 3 _x_ 2
_x_ 1 + _x_ 2 _≥_ 5
_x_ 1 _≥_ 1
_x_ 2 _≥_ 2 _._

            -            3
Prove that **x** _[∗]_ = is an optimal solution by showing that the objective value
2

of any feasible solution is at least 12. Hint: Use an appropriate combination of
the constraints.


**Exercise** **2.3** Consider the linear programming problem


max **c** [T] **x**
**Ax** _≤_ **b**
**x** _≥_ **0** _,_



where




  -   -   1 1 1 1 1 3
**A** = _,_ **b** =
5 4 3 2 1 14





      -      _,_ **c** [T] = 6 5 4 3 5 4 _._



Solve this problem using the following strategy:


(a) Find the dual of the above primal linear program. The dual has only two
variables. Solve the dual by inspection after drawing a graph of its feasible
set.
(b) Using the optimal solution to the dual problem and the optimality conditions, determine what primal constraints are binding and what primal variables must be zero at an optimal solution. Using this information, determine
the optimal solution to the primal linear program.


32 **Linear** **Programming:** **Theory** **and** **Algorithms**


**Exercise** **2.4**


(a) Give an example of a two-variable linear program that is infeasible.
(b) Give an example of a two-variable linear program that is unbounded.


**Exercise** **2.5** Consider the linear programming problem


max _c_ 1 _x_ 1 + _· · ·_ + _cnxn_
s.t. _a_ 1 _x_ 1 + _· · ·_ + _anxn_ = _b_
_x_ 1 _, . . ., xn_ _≥_ 0 _,_


where _b >_ 0 and _cj, aj_ _>_ 0 _,_ _j_ = 1 _, . . ., n_ . Characterize the optimal solution(s) to
this problem. Could there be more than one?


**Exercise** **2.6**


(a) Write the linear programming model in Example 2.1 (fund allocation) in
standard form. More precisely, show that for suitable **A** [˜], **b** [˜], **c** ˜, **x** ˜ the linear
programming model in Example 2.1 can be rewritten as


min **c** ˜ [T] **x** ˜
**x** ˜
**A** ˜ **x** ˜ = **b** ˜
**x** ˜ _≥_ **0** _._


Hint: Introduce additional variables.
(b) Show that the standard dual of the model in part (a), namely


max **b** ˜ [T] **y** ˜
**y** ˜

**A** ˜ [T] **y** ˜ _≤_ **c** ˜ _,_


is equivalent to (2.8).


**Exercise** **2.7** Consider the linear programming problem (2.5). In principle the
dual of this problem can be obtained as follows: First, rewrite it in standard
form (2.1) by using slack variables. Then obtain the “standard” dual, as in (2.2),
for the problem rewritten in this standard form. Prove that the dual problem
obtained in this fashion is equivalent to (2.6).


**Exercise** **2.8** Consider the following investment problem over _T_ years, where
the objective is to maximize the value of the investments in year _T_ . We assume
a perfect capital market with the same annual lending and borrowing rate _r_ _>_ 0
each year. We also assume that exogenous investment funds _bt_ are available in
year _t_, for _t_ = 1 _, . . ., T_ . Let _n_ be the number of possible investments. We assume
that each investment can be undertaken fractionally (between 0 and 1). Let _atj_
denote the cash flow associated with investment _j_ in year _t_ . Let _cj_ be the value of
investment _j_ in year _T_ (including all cash flows subsequent to year _T_ discounted
at the interest rate _r_ ).
The linear program that maximizes the value of the investments in year _T_ is
the following. Denote by _xj_ the fraction of investment _j_ undertaken, and let _yt_
be the amount borrowed (if negative) or lent (if positive) in year _t_ :


**2.9** **Exercises** 33




- _n_



max


_s.t._ _−_


_−_



_cjxj_ + _yT_

_j_ =1



_atjxj_ _−_ (1 + _r_ ) _yt−_ 1 + _yt_ _≤_ _bt_ for _t_ = 2 _, . . ., T_

_j_ =1




- _n_



_a_ 1 _jxj_ + _y_ 1 _≤_ _b_ 1

_j_ =1




- _n_



0 _≤_ _xj_ _≤_ 1 for _j_ = 1 _, . . ., n._


(a) Write the dual of the above linear program.
(b) Solve the dual linear program found in part (a).
Hint: Note that some of the dual variables can be computed by backward
substitution.
(c) Write the complementary slackness conditions.
(d) Deduce that the first _T_ constraints in the primal linear program hold as
equalities.
(e) Use the complementary slackness conditions to show that the solution
obtained by setting _xj_ = 1 if _cj_ + [�] _[T]_ _t_ =1 [(1] [+] _[r]_ [)] _[T][ −][t][a][tj]_ _[>]_ [0,] [and] _[x][j]_ [=] [0]
otherwise, is an optimal solution.
(f) Conclude that the above investment problem always has an optimal solution
where each investment is either undertaken completely or not at all.


**Exercise** **2.9** Consider the following variation of Exercise 2.5 where there are
upper bounds _ui_ on each of the variables:


max _c_ 1 _x_ 1 + _· · ·_ + _cnxn_
s.t. _a_ 1 _x_ 1 + _· · ·_ + _anxn_ _≤_ _b_
0 _≤_ _xi_ _≤_ _ui_ for _i_ = 1 _, . . ., n._


Assume that _b_ _>_ 0 and all _ai, ci, ui_ are also strictly positive for _i_ = 1 _, . . ., n_ .
Furthermore, assume
_c_ 1 _≥_ _[c]_ [2] _≥· · · ≥_ _[c][n]_ _._
_a_ 1 _a_ 2 _an_


Write the problem in standard form and apply the simplex method to it. What
steps will the simplex method take? In other words, in what order will the
variables enter and leave the basis?


**Exercise** **2.10** Install and get acquainted with CVX. This package is freely
available and extremely easy to install and use. It can be downloaded from
http://cvxr.com/cvx/download/.
Write a MATLAB script that takes as inputs an _m_ _×_ _n_ matrix **A** _,_ an _m_  dimensional vector **b**, and an _n_ -dimensional vector **c** and solves the optimization
problem

min **c** [T] **x**
s.t. **Ax** = **b**
**x** _≥_ **0** _._




_[c]_ [2] _≥· · · ≥_ _[c][n]_

_a_ 2 _an_



_._
_an_


34 **Linear** **Programming:** **Theory** **and** **Algorithms**


(a) Test your script on instances generated as follows:


>> m=1, n=5, b=1, c=ones(n,1), A=rand(m,n);


and


>> m=1, n=5, b=1, c=rand(n,1), A=ones(m,n);


Are the results consistent with your answer to Exercise 2.5?
(b) Test your script on instances generated as follows:


>> m=2, n=6, b=rand(m,1), c=rand(n,1), A=rand(m,n);

>> m=2, n=10, b=rand(m,1), c=rand(n,1), A=rand(m,n);

>> m=4, n=10, b=rand(m,1), c=rand(n,1), A=rand(m,n);

>> m=4, n=20, b=rand(m,1), c=rand(n,1), A=rand(m,n);


Do you notice anything peculiar about the number of non-zero entries in the
optimal solution **x** in each case?


**Exercise** **2.11** Use Theorem 2.4 to prove Theorem 2.5. To that end, proceed
as follows.


(a) (Farkas’s lemma) Consider the linear programming problem


min **b** [T] **y**
s.t. **A** [T] **y** _≤_ **0** _._


Show that the dual of this problem is


max 0
s.t. **Ax** = **b**
**x** _≥_ **0** _._


Now apply Theorem 2.4.
(b) (Gordan’s theorem) Proceed as in (a) but this time start with the linear
programming problem


max _t_
s.t. **A** [T] **y** _−_ **1** _t ≥_ **0** _._


(c) (Stiemke’s theorem) Proceed as in (a) and (b) but this time start with the
linear programming problem


max _t_
s.t. **Ax** = **0**
**x** _−_ **1** _t ≥_ **0** _._


**Exercise** **2.12** Use Theorem 2.5 to prove Theorem 2.4.


**Exercise** **2.13** To break the circular argument in the above two exercises,
prove Theorem 2.5 using the following _hyperplane_ _separation_ _theorem_ : If _S_ _⊆_ R _[n]_

is closed and convex and **x** _̸∈_ _S_ then there exists a hyperplane separating **x** and
_S_ . That is, there exists **a** _∈_ R _[n]_ _\ {_ **0** _}_ and _b ∈_ R such that **a** [T] **x** _< b ≤_ **a** [T] **y** for all
**y** _∈_ _S_ .


## 3 Linear Programming Models: Asset–Liability Management

This chapter presents a classical application of linear programming to covering
known liabilities by constructing a dedicated fixed-income portfolio. When the
liabilities span multiple years, the model assumes that the only sources of risk
are changes in the term structure of interest rates. We also discuss a short-term
financing problem.


**3.1** **Dedication**


Consider the problem of funding a stream of liabilities that extends over the
future. Assume the forecast of liabilities is accurate. This problem arises in
certain practical situations such as the liabilities of a pension fund. It also
arises in non-financial institutions planning acquisitions, expansion, or product
development. A _dedicated_ bond portfolio is a portfolio of bonds constructed today
and whose cash flows offset the liabilities.


**Example** **3.1** (Bond dedication) Suppose a pension fund needs to cover some
liabilities in the next six years. Cash requirements (in million $) are:


Year 1 2 3 4 5 6


Required 100 200 800 100 800 1200


Suppose the pension fund can invest in ten government bonds with the cash
flows and current prices in Table 3.1.
Find the least expensive portfolio of bonds whose cash flows will be sufficient
to cover the cash requirements. Assume surplus cash can be carried from one
year to the next but earn no interest.


We can formulate this problem as the following linear programming model.


_Linear_ _programming_ _model_ _for_ _bond_ _dedication_
**Variables:**

_xj_ : amount of bonds _j_ in the portfolio, for _j_ = 1 _, . . .,_ 10;
_st_ : surplus cash in year _t_, for _t_ = 1 _, . . .,_ 6.


36 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


**Table** **3.1**


Year
1 2 3 4 5 6 Price


Bond 1 10 10 10 10 10 110 109
Bond 2 7 7 7 7 7 107 94.8
Bond 3 8 8 8 8 8 108 99.5
Bond 4 6 6 6 6 106 93.1
Bond 5 7 7 7 7 107 97.2
Bond 6 5 5 5 105 92.9
Bond 7 10 10 110 110
Bond 8 8 8 108 104
Bond 9 7 107 102
Bond 10 100 95.2


**Objective:**


min 109 _x_ 1 + 94 _._ 8 _x_ 2 + _· · ·_ + 102 _x_ 9 + 95 _._ 2 _x_ 10 _._


**Constraints:**


10 _x_ 1 + 7 _x_ 2 + _· · ·_ + 7 _x_ 9 + 100 _x_ 10 = 100 + _s_ 1
10 _x_ 1 + 7 _x_ 2 + _· · ·_ + 107 _x_ 9 + _s_ 1 = 200 + _s_ 2
...
110 _x_ 1 + 107 _x_ 2 + 108 _x_ 3 + _s_ 5 = 1200 + _s_ 6
_xj_ _≥_ 0 _,_ _j_ = 1 _, . . .,_ 10
_st_ _≥_ 0 _,_ _t_ = 1 _, . . .,_ 6 _._


Notice that we can write the equality constraints also as


10 _x_ 1 + 7 _x_ 2 + _· · ·_ + 7 _x_ 9 + 100 _x_ 10 _−s_ 1 = 100
10 _x_ 1 + 7 _x_ 2 + _· · ·_ + 107 _x_ 9 + _s_ 1 _−_ _s_ 2 = 200
...
110 _x_ 1 + 107 _x_ 2 + 108 _x_ 3 + _s_ 5 _−_ _s_ 6 = 1200
_xj_ _≥_ 0 _,_ _j_ = 1 _, . . .,_ 10
_st_ _≥_ 0 _,_ _t_ = 1 _, . . .,_ 6 _,_


or as


10 _x_ 1 + 7 _x_ 2 + _· · ·_ + 7 _x_ 9 + 100 _x_ 10 _−_ 100 = _s_ 1
10 _x_ 1 + 7 _x_ 2 + _· · ·_ + 107 _x_ 9 + _s_ 1 _−_ 200 = _s_ 2
...
110 _x_ 1 + 107 _x_ 2 + 108 _x_ 3 + _s_ 5 _−_ 1200 = _s_ 6
_xj_ _≥_ 0 _,_ _j_ = 1 _, . . .,_ 10
_st_ _≥_ 0 _,_ _t_ = 1 _, . . .,_ 6 _._


In general, for a given problem with liabilities projected over _m_ points in time
over the future, the stream of liabilities is a vector:


**3.1** **Dedication** 37


Date 1 2 _· · ·_ _m_


Required _L_ 1 _L_ 2 _· · ·_ _Lm_


Suppose we can use _n_ bonds with the following cash flows and prices:


Date 1 2 _· · ·_ _m_ Prices


Bond 1 _F_ 11 _F_ 21 _· · ·_ _Fm_ 1 _p_ 1
... ... ...
Bond _j_ _F_ 1 _j_ _F_ 2 _j_ _· · ·_ _Fmj_ _pj_
... ...
Bond _n_ _F_ 1 _n_ _F_ 2 _n_ _· · ·_ _Fmn_ _pn_


The linear programming formulation of the cash matching problem is as follows.


_Linear_ _programming_ _model_ _for_ _bond_ _dedication_ _(general_ _version)_
**Variables:**
_xj_ : amount of bonds _j_ in the portfolio, for _j_ = 1 _, . . ., n_ ;
_st_ : surplus cash in year _t_, for _t_ = 1 _, . . ., m_ .


**Linear** **programming** **model:**


    - _n_



min


s.t.



_pjxj_

_j_ =1



_F_ 1 _jxj_ _−_ _s_ 1 = _L_ 1

_j_ =1




- _n_




- _n_



_Ftjxj_ + _st−_ 1 _−_ _st_ = _Lt,_ _t_ = 2 _, . . ., m_

_j_ =1



_xj_ _≥_ 0 _,_ _j_ = 1 _, . . ., n_
_st_ _≥_ 0 _,_ _t_ = 1 _, . . ., m._


The problem can be written more concisely as follows:


min **p** [T] **x**
s.t. **Fx** + **Rs** = **L**
**x** _≥_ **0**
**s** _≥_ **0** _,_



where


**F** =



⎡

⎢⎣



_,_



⎤

_−_ 1 0 0 0 _· · ·_ 0
1 _−_ 1 0 0 _· · ·_ 0
0 1 _−_ 1 0 _· · ·_ 0
... ... ... ... ... ...
0 _· · ·_ 0 1 _−_ 1 0 ⎥⎥⎥⎥⎥⎥⎥⎥⎦
0 0 _· · ·_ 0 1 _−_ 1



⎤

_F_ 11 _· · ·_ _F_ 1 _n_
... ... ... ⎥⎦ _,_ **R** =
_Fm_ 1 _· · ·_ _Fmn_



⎡

⎢⎢⎢⎢⎢⎢⎢⎢⎣


38 **Linear** **Programming** **Models:** **Asset–Liability** **Management**



_p_ 1
...
_pn_



⎡

⎢⎣



_L_ 1
...
_Lm_



⎤

⎥⎦ _,_ **L** =



⎤

⎥⎦ _._



**p** =



⎡

⎢⎣



**3.2** **Sensitivity** **Analysis**


As noted in Section 2.4, when a linear programming model is solved, the dual
solution yields a great deal of _sensitivity_ _information_, or information about what
happens when data values are changed. Recall the sensitivity interpretation
associated with the _shadow_ _price._ Assume _λ_ is the shadow price of a constraint:


If the right-hand side of a constraint changes by Δ, then the optimal
objective value changes by _λ ·_ Δ, as long as the change of the right-hand
side is within the allowable increase or decrease.


This concept is particularly insightful in the bond dedication problem. In a
nutshell, the sensitivity information of the linear optimization model leads to an
_implied_ _term_ _structure_ as we next explain. Recall our linear programming model
for portfolio dedication:


     - _n_



min


s.t.



_F_ 1 _jxj_ _−_ _s_ 1 = _L_ 1

_j_ =1



_pjxj_

_j_ =1




- _n_




- _n_



_Ftjxj_ + _st−_ 1 _−_ _st_ = _Lt,_ _t_ = 2 _, . . ., m_

_j_ =1



_xj_ _≥_ 0 _,_ _j_ = 1 _, . . ., n_
_st_ _≥_ 0 _,_ _t_ = 1 _, . . ., m._


The shadow price of constraint at time _t_ is the extra amount of money needed
today to cover an extra unit of liability at time _t_ . In other words, the shadow price
_λt_ gives the discount factor for time _t_ . The current portfolio therefore _implies_
the following term structure of interest rates:


1
_rt_ =
( _λt_ ) [1] _[/t]_ _[−]_ [1] _[.]_


**3.3** **Immunization**


Consider again the problem of covering a stream of liabilities ( _L_ 1 _, . . ., Lm_ ) due at
_m_ different dates in the future. In principle, the stream of liabilities is equivalent
to a lump sum of cash today equal to its present value, obtained by discounting
the future liabilities. Setting aside an amount equal to this present value seems
simpler than constructing a dedicated portfolio. A problem with this approach


**3.3** **Immunization** 39


is that it is fully exposed to interest-rate risk. By contrast, a dedicated portfolio
is not subject to interest-rate risk since it matches the liabilities at the time they
occur. _Immunization_ is an approach that reduces interest-rate risk as compared
to the simple-minded present value approach, but it does not completely protect
against it as dedication would. The advantage is that immunized portfolios
are typically cheaper than dedicated portfolios. The idea is simple: construct
a portfolio with the same present value as the stream of liabilities, and further
require that this present value has the same sensitivity to changes in interest
rates as the stream of liabilities.
More precisely, suppose _r_ 1 _, . . ., rm_ is the _term_ _structure_ of risk-free interest
rates. This means that the value _rt_ is the yield on a risk-free zero-coupon bond
with maturity _t_ . In other words, _rt_ is the interest rate that applies to money
invested between now and time _t_ . By discounting each of the cash flows with the
appropriate discount rate, it follows that the present value (PV) of a stream of
cash flows ( _F_ 1 _, . . ., Fm_ ) _,_ where _Ft_ occurs at time _t_, is


_F_ 1 _F_ 2 _Fm_
PV = 1 + _r_ 1 + (1 + _r_ 2) [2] [+] _[ · · ·]_ [ +] (1 + _rm_ ) _[m]_ _[.]_


If interest rates shift by _δ_, we get


_F_ 1 _F_ 2 _Fm_
PV( _δ_ ) = 1 + _r_ 1 + _δ_ [+] (1 + _r_ 2 + _δ_ ) [2] [+] _[ · · ·]_ [ +] (1 + _rm_ + _δ_ ) _[m]_ _[.]_



Notice that

        PV( _δ_ ) _−_ PV _≈−δ_ (1 + _F r_ 1 1) [2] [+] (1 +2 _F r_ 22) [3] [+] _[ · · ·]_ [ +] (1 + _mF rmm_ ) _[m]_ [+1]


This motivates the following concept.





_._



**Definition** **3.2** The Fisher–Weil dollar duration (DD) of the stream of cash
flows ( _F_ 1 _, . . ., Fm_ ) is



DD :=




- _m_


_t_ =1



_tFt_
(1 + _rt_ ) _[t]_ [+1] _[.]_



An _immunized_ _portfolio_ is a portfolio of bonds whose present value and duration match those of the stream of liabilities. In optimization terms, this corresponds to a portfolio that satisfies the following constraints:


     - _n_

PV _jxj_ = PV _L_

_j_ =1

     - _n_

DD _jxj_ = DD _L._

_j_ =1


A closer look at the difference between PV and PV( _δ_ ) suggests that we can
get an even better matching of sensitivity to changes in the term structure by
looking at second-order terms:


40 **Linear** **Programming** **Models:** **Asset–Liability** **Management**




 - _m_

[1]

2 _[δ]_ [2]



_t_ =1



PV( _δ_ ) _−_ PV _≈−δ_




- _m_


_t_ =1



_tFt_

[1]
(1 + _rt_ ) _[t]_ [+1] [+] 2



_t_ ( _t_ + 1) _Ft_
(1 + _rt_ ) _[t]_ [+2] _[.]_



This leads to the so-called Fisher–Weil _dollar_ _convexity_ (DC) of ( _F_ 1 _, . . ., Fm_ ):



DC :=




- _m_


_t_ =1



_t_ ( _t_ + 1) _Ft_
(1 + _rt_ ) _[t]_ [+2] _[,]_



as well as the Fisher–Weil _convexity_ (C):



1
C :=
PV




- _m_


_t_ =1



_t_ ( _t_ + 1) _Ft_
(1 + _rt_ ) _[t]_ [+2] _[.]_



A portfolio can therefore be further immunized by matching present value, dollar
duration, and dollar convexity:


     - _n_

PV _jxj_ = PV _L_

_j_ =1

     - _n_

DD _jxj_ = DD _L_ (3.1)

_j_ =1

     - _n_

DC _jxj_ _≥_ DC _L._

_j_ =1


Here the subindices _j_ = 1 _, . . ., n_ and _L_ refer to the bonds and liabilities respectively. Note that since having net positive convexity is favorable, the last constraint is an inequality constraint.
The immunization constraints (3.1) are generally less stringent than the bond
dedication constraints, namely




- _n_



_F_ 1 _jxj_ _−_ _s_ 1 = _L_ 1

_j_ =1




- _n_



_Ftjxj_ + _st−_ 1 _−_ _st_ = _Lt,_ _t_ = 2 _, . . ., m_

_j_ =1



(3.2)



_xj_ _≥_ 0 _,_ _j_ = 1 _, . . ., n_
_st_ _≥_ 0 _,_ _t_ = 1 _, . . ., m._


Indeed, if the surplus variables _st,_ _t_ = 1 _, . . ., m_, are all zero in (3.2), then
some straightforward algebra shows that any _x_ 1 _, . . ., xn_ satisfying (3.2) also
satisfies (3.1).
The previous discussion assumes that interest is compounded at discrete time
intervals, e.g., annually or semiannually. In some practical circumstances cash
flows may occur at irregular times. In those cases it could be more convenient to
assume that interest is continuously compounded. Suppose _rt_ is the _continuously_


**3.4** **Some** **Practical** **Details** **about** **Bonds** 41


_compounded_ spot rate for a risk-free zero-coupon bond with maturity _t_ . Then the
present value of a stream of cash flows ( _F_ 1 _, . . ., Fm_ ) is



PV =


Consequently its dollar duration is


DD =


and its dollar convexity is




- _m_

_Fte_ _[−][t][·][r][t]_ _._

_t_ =1




- _m_

_tFte_ _[−][t][·][r][t]_ _,_

_t_ =1



DC =




- _m_

_t_ [2] _Fte_ _[−][t][·][r][t]_ _._

_t_ =1



A nice feature of continuous compounding is that the formulas for an irregular
stream of cash flows ( _Ft_ 1 _, . . ., Ftm_ ) are very similar:



PV =




- _m_

_Fti_ _e_ _[−][t][i][·][r][ti]_ _,_

_i_ =1



DD =


DC =




- _m_

_tiFti_ _e_ _[−][t][i][·][r][ti]_ _,_

_i_ =1




- _m_

_t_ [2] _i_ _[F][t]_ _i_ _[e][−][t][i][·][r][ti]_ _[.]_
_i_ =1



The kind of immunization via duration and convexity enforced by the constraints (3.1) provides hedging against parallel shocks in the term structure.
This implicitly assumes a _one-factor_ interest risk model. There are enhancements
based on a _multi-factor_ interest risk model. Two popular ones are the _key-rate_
_model_ and the _shift–twist–butterfly_ model as discussed in Tuckman (2002). The
logic of immunization naturally extends to a multi-factor interest risk model. In
such a context an immunized portfolio should be hedged against changes in each
of the risk factors.


**3.4** **Some** **Practical** **Details** **about** **Bonds**


There are certain details about the way bonds are quoted and traded in actual
exchanges. The discussion below applies only to plain vanilla treasury bonds. For
a more detailed discussion, see Fabozzi (2004) or Tuckman (2002).


42 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


Principal Value, Coupon Payments, Clean and Dirty Prices


The _principal_ _value_, or _par,_ or _principal_ of a bond is the amount that the issuer
agrees to repay the bondholder. The _term_ _to_ _maturity_ of a bond is the time
remaining until principal payment. The _maturity_ _date_ of a bond is that date
when the issuer will pay the principal.
The _coupon_ _rate_ or _nominal_ _rate_ of a bond is the annual interest that the
issuer pays the bondholder. Treasury bonds pay their coupons semiannually. For
example, a bond with an 8% coupon rate and a principal of $1,000 will pay a
$40 installment to the holder every six months. At the maturity date, it will pay
the $40 installment plus the $1,000 principal.
When an investor purchases a bond between coupon payments, the investor
must compensate the seller of the bond for the coupon interest earned since the
last coupon payment. This is called the _accrued_ _interest_ and is computed based
on the proportion of time since the last coupon payment. The convention for
United States treasuries is not to include the accrued interest in the price quote.
This price is called the _clean_ _price_ or simply the _price._ It is customary to present
the price quote as a percentage of the par value of the bond. The clean price
plus the accrued interest is called the _dirty_ _price_ or _full_ _price._
For example, suppose that on February 15, 2051 investor _B_ buys a treasury
bond with $10,000 face value, 5.5% coupon rate that matures on January 31,
2053. In this case the coupon payment is $275 = 2.75% of $10,000 and the
accrued interest is
15
181 _[·]_ [ 275 = 22] _[.]_ [79] _[.]_


Suppose the price quote on February 15, 2051 is 101.145. Then the full price of
the bond, that is, the price paid by the buyer to the seller, is $10,114.5+$22.79
= $10,137.29.


Yield Curve and Term Structure


Recall that the _yield_ of a bond is the interest rate that makes the discounted
value of the cash flows match the current price of the bond. By convention,
the yield is quoted on an annual basis. The _treasury_ _yield_ _curve_ is the curve of
yields for _on-the-run_ (most recently auctioned) treasuries. It should be noted
that the yield curve is not the same as the term structure of interest rates. This
is the case because treasuries with maturity greater than one year are not zerocoupon bonds. Indeed, the term structure of interest rates is actually a theoretical
construct that must be estimated from actual bonds.
There are various ways of estimating the term structure. A quick and dirty
(perhaps too dirty) approach is to ignore the difference described above and to
use the yield curve as a proxy for the term structure of interest rates.
A second approach is to use the following _bootstrapping_ approach: Use several
coupon-bearing bonds with various maturities. Determine the spot rate implied


**3.4** **Some** **Practical** **Details** **about** **Bonds** 43


by the bond with the shortest maturity. Use that knowledge to compute the spot
rate implied by the bond with the next shortest maturity and so on. For example,
suppose we have a 0.5-year 5.25% bill, a 1-year 5.75% note, and a 1.5-year 6%
note. For simplicity assume they all are trading at par. Let _z_ 1 _, z_ 2 _, z_ 3 denote the
one-half annualized 0.5-year, 1-year, and 1.5-year spot rates.
Using the 0.5-year bond, we readily get


_z_ 1 = 0 _._ 0525 _·_ 0 _._ 5 = 0 _._ 02625 _._


Using $100 as par, the cash flows for the 1-year bond are


0.5-year: 0 _._ 0575 _·_ 100 _·_ 0 _._ 5 = 2 _._ 875
1-year: 0 _._ 0575 _·_ 100 _·_ 0 _._ 5 + 100 = 102 _._ 875.


Now compute its present value using the spot rates _z_ 1 _, z_ 2 and equate that to its
current price:




[2] _[.]_ [875] + [102] _[.]_ [875]

1 + _z_ 1 (1 + _z_ 2)



100 = [2] _[.]_ [875]



(1 + _z_ 2) [2] _[.]_



Because we already know _z_ 1, we can solve for _z_ 2 and obtain


_z_ 2 = 0 _._ 028786 _._


Repeat with the 1.5-year bond: Using $100 as par, the cash flows for the 1.5-year
bond are


0.5-year: 0 _._ 06 _·_ 100 _·_ 0 _._ 5 = 3
1-year: 0 _._ 06 _·_ 100 _·_ 0 _._ 5 = 3
1.5-year: 0 _._ 06 _·_ 100 _·_ 0 _._ 5 + 100 = 103 _._


Now compute its present value using the spot rates _z_ 1 _, z_ 2 _, z_ 3 and equate that to
its current price:


3 3 103
100 = 1 + _z_ 1 + (1 + _z_ 2) [2] [+] (1 + _z_ 3) [3] _[.]_


Because we already know _z_ 1 _, z_ 2, we can solve for _z_ 3 and obtain


_z_ 3 = 0 _._ 030063097 _._


Thus the annualized spot rates are


_r_ 0 _._ 5 = 0 _._ 0525 _,_ _r_ 1 = 0 _._ 057572 _,_ _r_ 2 = 0 _._ 06012 _._


Yet a third, and much more elaborate, approach to estimating the term structure is to take into consideration all bonds with similar characteristics available
in the market and perform an elaborate regression model. This approach requires
advanced statistical techniques and is beyond the scope of this book. For a related
discussion see Campbell et al. (1997) and Heath et al. (1992)
It should also be noted that the previous two estimation approaches only give
spot rates at specific points in time. The spot rates at other times can be obtained
by interpolation. The simplest type of interpolation is piecewise linear.


44 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


**3.5** **Other** **Cash** **Flow** **Problems**


The dedication model discussed in Section 3.1 belongs to the broader class of
_cash_ _flow_ _problems_ . A firm faces a stream of both positive (inflows) and negative
(outflows) flows of cash. The negative flows are considered liabilities that must
be met when they occur. To meet the liabilities, the firm can purchase a variety
of instruments each with a different cash flow pattern.
The following _short-term_ _financing_ _problem_ is of this kind. Corporations
routinely face the problem of financing short-term cash commitments. Linear
programming can help in figuring out an optimal combination of financial
instruments to meet these commitments. For illustration, consider the following
problem. For the sake of exposition, we keep the example small.


**Example** **3.3** (Short-term financing) A company has the following short-term
financing problem (net cash flow requirements are given in $1000s).


Month J F M A M J


Net cash flow _−_ 150 _−_ 100 200 _−_ 200 50 300


The company has the following sources of funds:


_•_ A line of credit of up to $100,000 at an interest rate of 1% per month.


_•_ It can issue 90-day commercial paper bearing a total interest of 2% for the
3-month period.


_•_ Each month excess funds can be invested at an interest rate of 0.3% per
month.


There are many questions that the company might want to answer. Is it economical to use the line of credit in some of the months? If so, when? How much?
What interest payments will the company need to make between January and
June? Linear programming gives us a mechanism for answering these questions
quickly and easily.


_Linear_ _programming_ _model_ _for_ _short-term_ _financing_ _problem_


**Variables:**


_xj_ : amount drawn from the line of credit in month _j_, for _j_ = 1 _, . . .,_ 5


_yj_ : amount of commercial paper issued in month _j_, for _j_ = 1 _, . . .,_ 3


_zj_ : excess funds in month _j_, for _j_ = 1 _, . . .,_ 6.


**Objective:**


max _z_ 6 _._


**3.5** **Other** **Cash** **Flow** **Problems** 45


**Constraints:** Cash balance constraints in each month and bounds on _xj_, _yj_
and _zj_ :


_x_ 1 + _y_ 1 _−_ _z_ 1 = 150
_x_ 2 + _y_ 2 _−_ 1 _._ 01 _x_ 1 + 1 _._ 003 _z_ 1 _−_ _z_ 2 = 100
_x_ 3 + _y_ 3 _−_ 1 _._ 01 _x_ 2 + 1 _._ 003 _z_ 2 _−_ _z_ 3 = _−_ 200
_x_ 4 _−_ 1 _._ 02 _y_ 1 _−_ 1 _._ 01 _x_ 3 + 1 _._ 003 _z_ 3 _−_ _z_ 4 = 200
_x_ 5 _−_ 1 _._ 02 _y_ 2 _−_ 1 _._ 01 _x_ 4 + 1 _._ 003 _z_ 4 _−_ _z_ 5 = _−_ 50

_−_ 1 _._ 02 _y_ 3 _−_ 1 _._ 01 _x_ 5 + 1 _._ 003 _z_ 5 _−_ _z_ 6 = _−_ 300
_xj_ _≤_ 100 for _j_ = 1 _, . . .,_ 5
_xj_ _≥_ 0 for _j_ = 1 _, . . .,_ 5
_yj_ _≥_ 0 for _j_ = 1 _, . . .,_ 3
_zj_ _≥_ 0 for _j_ = 1 _, . . .,_ 5 _._


Solving this linear program using either Excel Solver or MATLAB CVX, we
obtain the following optimal solution:



0
0
351 _._ 944
0
0
92 _._ 497



0
0
0
0
52



⎡

150
⎣ 100
151 _._ 944



⎤

⎥⎥⎥⎥⎥⎥⎥⎦



⎤


_,_ **y** _[∗]_ =
⎥⎥⎥⎥⎦



⎡

⎢⎢⎢⎢⎢⎢⎢⎣



_._



**x** _[∗]_ =



⎡

⎢⎢⎢⎢⎣



⎤


⎦ _,_ **z** _[∗]_ =



Thus the company can attain an optimal wealth of $92,497 in June. To achieve
this, the company will issue $150,000 in commercial paper in January, $100,000
in February and $151,944 in March. In addition, it will draw $52,000 from its
line of credit in May. Excess cash of $351,944 in March will be invested for one
month.
Figure 3.1 displays the Excel Solver sensitivity report for this model.
The key columns for sensitivity analysis are the “Reduced Cost” and “Shadow
Price” columns. Recall that the _shadow price u_ of a constraint _C_ has the following
interpretation:


If the right-hand side of the constraint _C_ changes by an amount Δ, the
optimal objective value changes by _u ·_ Δ as long as Δ is within a certain
range.


The above sensitivity information allows us to perform various kinds of “what
if” analysis.


_•_ For example, assume that net cash flow in January were _−_ 200 (instead of

_−_ 150). By how much would the wealth of the company decrease at the
end of June? The answer is in the shadow price of the January constraint,
_u_ = _−_ 1 _._ 0373. The right-hand side of the January constraint would go
from 150 to 200, an increase of Δ = 50, which is within the allowable


46 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


**Figure** **3.1** Sensitivity report for short-term financing model


increase (89.17). So the wealth of the company in June would decrease by
1 _._ 0373 _·_ 50 _,_ 000 = $51 _,_ 865 _._

_•_ Now assume that net cash flow in March were 250 (instead of 200). By how
much would the wealth of the company increase at the end of June? Again,
the change Δ = _−_ 50 is within the allowable decrease (151.944), so we can
use the shadow price _u_ = _−_ 1 _._ 02 to calculate the change in objective value.
The increase is ( _−_ 1 _._ 02) _·_ ( _−_ 50) = $51 _,_ 000 _._

_•_ Assume that the negative net cash flow in January is due in part to the
purchase of a machine worth $100,000. The vendor allows the payment to
be made in June at an interest rate of 3% for the 5-month period. Would
the wealth of the company increase or decrease by using this option? What
if the interest rate for the 5-month period were 4%? The shadow price of the
January constraint is _−_ 1 _._ 0373 _._ This means that reducing cash requirements
in January by $1 increases the wealth in June by $1.0373. In other words,
the break-even interest rate for the 5-month period is 3.73%. So, if the
vendor charges 3%, we should accept, but if he charges 4% we should not.
Note that the analysis is valid since the amount Δ = _−_ 100 is within the
allowable decrease.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-58-1.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-58-2.png)
**3.6** **Exercises** 47


Next, let us consider the reduced costs. Recall that these are the shadow prices
of the upper and lower bounds placed directly on the variables. The reduced cost
of a variable is non-zero only when the variable is equal to one of its bounds.
Assume _x_ is equal to its lower bound _b_ and its reduced cost is _c_ . There are two
useful interpretations of the reduced cost _c_ .


_•_ First, if the value of _x_ is set to a value _b_ + Δ for Δ _>_ 0 instead of its optimal
value _b_ then the objective value is changed by _c ·_ Δ. For example, what
would be the effect of financing part of the January cash needs through the
line of credit? The answer is in the reduced cost of the first variable. Because
this reduced cost _−_ 0 _._ 0032 is strictly negative, the objective function would
decrease. Specifically, each dollar financed through the line of credit in
January would result in a decrease of $3.2 in the wealth of the company in
June.

_•_ The second interpretation of _c_ is that its magnitude _|c|_ is the minimum amount
by which the objective coefficient of _x_ must be changed in order for the
variable _x_ to move away from its bound in an optimal solution. For example,
consider the first variable again. Its value is zero in the current optimal
solution, with objective function _z_ 6. However, if we changed the objective
to _z_ 6+0 _._ 0032 _x_ 1, it would now be optimal to use the line of credit in January.
In other words, the reduced cost on _x_ 1 can be viewed as the minimum rebate
that the bank would have to offer (payable in June) to make it attractive
to use the line of credit in January.


**3.6** **Exercises**


**Exercise** **3.1** You need to create a portfolio to cover the following stream of
liabilities for the next six future dates:


Date 1 2 3 4 5 6


Required 500 200 800 200 800 1200


You may purchase the bonds in Table 3.2.
The term structure of risk-free interest rates is:


Date 1 2 3 4 5 6


Rate 5.04% 5.94% 6.36% 7.18% 7.89% 8.39%


(a) Formulate a linear programming model to find the lowest-cost long-only
dedicated portfolio that covers the stream of liabilities with the bonds above.
Assume surplus balances can be carried from one date to the next but earn
no interest. What is the cost of your portfolio? What is the composition of
your portfolio?


48 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


**Table** **3.2**


Year
Bond 1 2 3 4 5 6 Price


1 10 10 10 10 10 110 109
2 7 7 7 7 7 107 94.8
3 8 8 8 8 8 108 99.5
4 6 6 6 6 106 93.1
5 7 7 7 7 107 97.2
6 6 6 6 106 96.3
7 5 5 5 105 92.9
8 10 10 110 110
9 8 8 108 104
10 6 6 106 101
11 10 110 107
12 7 107 102
13 100 95.2


(b) Formulate a linear programming model to find the lowest-cost portfolio that
matches the present value and dollar duration of the stream of liabilities.
What is the cost of your portfolio? How do the two present values change
if interest rates decrease by one percentage point? How do they change if
interest rates increase by one percentage point? How do they change if the
interest rates in dates 1 and 2 decrease by one percentage point, the rates in
dates 3, 4, and 5 remain the same, and the rate in date 6 increases by one
percentage point?


(c) Use the linear programming sensitivity information from part (a) to determine the implied term structure of interest rates.


(d) Suppose that the stream of liabilities changes to:


Date 1 2 3 4 5 6


Required 100 200 800 500 800 1200


Find the new optimal dedicated portfolio and determine the new implied
term structure. Is it different from the one you obtained in part (c)? Can
you provide an intuitive explanation for the difference or lack thereof?


(e) Assume the liabilities occur at irregular time intervals:


Date 1.25 2.5 3.5 4.5 5.75 6.5


Required 500 200 800 200 800 1200


(i) Repeat part (b) for this irregular stream of liabilities.


**3.6** **Exercises** 49


You will need to do some kind of interpolation to estimate the term
structure at the relevant times. You will also need to make an assumption
about how to discount at irregular time intervals.


(ii) Repeat part (a) for this irregular stream of liabilities.


(f) Formulate a linear programming model to find the lowest-cost long-only
dedicated portfolio that covers the stream of liabilities:


Date 1 2 3 4 5 6


Required 500 200 800 400 700 900


with the following new set of bonds:


Bond 1 2 3 4 5 6 Price Rating


1 10 10 10 10 10 110 108 B
2 7 7 7 7 7 107 94 B
3 8 8 8 8 8 108 99 B
4 6 6 6 6 106 92.7 B
5 7 7 7 7 107 96.6 B
6 6 6 6 106 95.9 B
7 5 5 5 105 92.9 A
8 10 10 110 110 A
9 8 8 108 104 A
10 6 6 106 101 A
11 10 110 107 A
12 7 107 102 A
13 100 95.2 A


This time assume that at most 50% of your portfolio’s value can be in
bonds rated B. Again, assume surplus balances can be carried from one date
to the next but earn no interest. What is the cost of your portfolio? What
is the composition of your portfolio?


**Exercise 3.2** Suppose today is November 30, 2052. A pension fund will need to
cover the following stream of liabilities over the subsequent four years (in million
dollars):

|5/31/53|11/30/53|5/31/54|11/30/54|5/31/55|11/30/55|5/31/56|11/31/56|
|---|---|---|---|---|---|---|---|
|12|10|10|10|9|9|9|15|



To cover these liabilities, the pension fund intends to use a portfolio comprised
of the following 14 US treasury notes:


50 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


Description Coupon Maturity date Clean price


US TREAS NTS 3.500% 05/31/2053 3.5 5/31/53 101.563
US TREAS NTS 0.500% 05/31/2053 0.5 5/31/53 100.188
US TREAS NTS 2.000% 11/30/2053 2 11/30/53 101.746
US TREAS NTS 0.250% 11/30/2053 0.25 11/30/53 100.078
US TREAS NTS 2.250% 05/31/2054 2.25 5/31/54 102.941
US TREAS NTS 0.250% 05/31/2054 0.25 5/31/54 100.023
US TREAS NTS 2.125% 11/30/2054 2.125 11/30/54 103.656
US TREAS NTS 0.250% 11/30/2054 0.25 11/30/54 100.016
US TREAS NTS 2.125% 05/31/2055 2.125 5/31/55 104.461
US TREAS NTS 1.375% 11/30/2055 1.375 11/30/55 103.031
US TREAS NTS 3.250% 05/31/2056 3.25 5/31/56 109.738
US TREAS NTS 1.750% 05/31/2056 1.75 5/31/56 104.570
US TREAS NTS 2.750% 11/30/2056 2.75 11/30/56 108.879
US TREAS NTS 0.875% 11/30/2056 0.875 11/30/56 101.516


(a) Compute the dirty (full) price of each of the above 14 bonds. For consistency,
assume today is November 30, 2052.


(b) Formulate a linear programming model to find the lowest-cost dedicated
portfolio that covers the stream of liabilities. To eliminate the possibility of
any interest risk, assume a 0% reinvestment rate on cash balances carried
from one date to the next. Assume no short sales are allowed. What is the
cost of your portfolio? What is the composition of your portfolio?


(c) Use the linear programming sensitivity information from part (b) to determine the term structure of interest rates implied by the portfolio.


**Exercise** **3.3** Prove that, if _s_ 1 = _s_ 2 = _· · ·_ = _sm_ = 0 in (3.2), each of the
immunization constraints in (3.1) is implied by the dedication constraints (3.2).


**Exercise** **3.4** A company will face the following cash requirements in the
next eight quarters (positive entries represent cash needs while negative entries
represent cash surpluses):

|Q1|Q2|Q3|Q4|Q5|Q6|Q7|Q8|
|---|---|---|---|---|---|---|---|
|100|500|100|_−_600|_−_500|200|600|_−_900|



The company has three borrowing possibilities.


_•_ A 2-year loan available at the beginning of Q1, with a 1% interest per quarter.


_•_ The other two borrowing opportunities are available at the beginning of every
quarter: a 6-month loan with a 1.8% interest per quarter, and a quarterly
loan with a 2.5% interest for the quarter.


_•_ Any surplus can be invested at a 0.5% interest per quarter.


**3.7** **Case** **Study** 51


Formulate a linear program that maximizes the wealth of the company at the
beginning of Q9.


**Exercise 3.5** Generate the sensitivity report for Exercise 3.4 with your favorite
LP solver.


(a) Suppose the cash requirement in Q2 is 300 (instead of 500). How would this
affect the wealth in Q9?
(b) Suppose the cash requirement in Q2 is 100 (instead of 500). Can the sensitivity report be used to determine the wealth in Q9?
(c) One of the company’s suppliers may allow deferred payments of $50 from
Q3 to Q4. What would be the value of this?


**Exercise** **3.6** A home buyer can combine several mortgage loans to finance
the purchase of a house. Regulations impose limits on the amount that can be
borrowed from certain sources as well as a limit on the total reimbursement each
month. Let _B_ be the borrowing needs and _T_ the number of months over which the
loans will be paid back. There are _n_ different loan opportunities available. Loan
_i_ has a fixed interest rate _ri_, a length _Ti_ _≤_ _T_ and a maximum amount borrowed
_bi_ . The monthly payment on loan _i_ is not required to be the same every month,
but a minimum payment _mi_ is required each month. Furthermore, we would like
the total monthly payment _p_ over all loans to be constant. Formulate a linear
program that finds a combination of loans that minimizes the home buyer’s cost
of borrowing.
Hint: In addition to variables _xti_ for the payment on loan _i_ in month _t_, it may
be useful to introduce a variable for the amount of outstanding principal on loan
_i_ in month _t_ .


**3.7** **Case** **Study**


Let _y_ denote the current year. A municipality sends you the following liability
stream (in million dollars):

|12/15/y|6/15/y+1|12/15/y+1|6/15/y+2|12/15/y+2|6/15/y+3|12/15/y+3|6/15/y+4|
|---|---|---|---|---|---|---|---|
|11|9|8|7|9|10|9|12|


|12/15/y+4|6/15/y+5|12/15/y+5|6/15/y+6|12/15/y+6|6/15/y+7|12/15/y+7|6/15/y+8|
|---|---|---|---|---|---|---|---|
|9|6|5|7|9|7|8|7|



_Questions_
1. Determine the current term structure of treasury rates, and find the present
value, dollar duration, and dollar convexity of the stream of liabilities. Please
explain the main steps (interest rates, discount factors, compounding, etc.)
followed in your calculations. You can find current data on numerous websites
such as

http://finance.yahoo.com/bonds

http://fixedincome.fidelity.com/fi/FILanding


52 **Linear** **Programming** **Models:** **Asset–Liability** **Management**


2. Identify at least 30 fixed-income assets that are suitable for a dedicated
portfolio. Use assets that are considered risk-free, e.g., US government noncallable treasury bonds, treasury bills, or treasury notes. Display a succinct
summary of the main characteristics of the bonds you chose (prices, coupon
rates, maturity dates).
3. Formulate a linear programming model to find the lowest-cost dedicated
portfolio that covers the stream of liabilities. To eliminate the possibility
of any interest risk, assume a 0% reinvestment rate on cash balances carried
from one date to the next. Assume no short sales are allowed. What is the
cost of your portfolio? What is the composition of your portfolio?
4. Use the linear programming sensitivity information to determine the term
structure of interest rates implied by the portfolio. Use a plot to compare it
with the current term structure of treasury rates.
5. Formulate a linear programming model to find the lowest-cost portfolio that
matches the present value, dollar duration, and dollar convexity of the stream
of liabilities. Assume no short sales are allowed. What is the cost of your
portfolio? How much would you save by using this immunization strategy
instead of dedication? Is your portfolio immunized against non-parallel shifts
in the term structure? Explain why or why not.
6. Combine a cash matching strategy for the liabilities during the first three
years and an immunization strategy based on present value, duration and
convexity for the liabilities during the last five years. Compare the cost of
this portfolio with the cost of the two previous portfolios.
7. The municipality would like you to make a second bid: What is your best
dedicated portfolio of risk-free bonds you can create if short sales are allowed?
Did you find arbitrage opportunities? Did you take into consideration the
bid–ask spread? Did you set limits on the transaction amounts? Discuss the
practical feasibility of your solution.


## 4 Linear Programming Models: Arbitrage and Asset Pricing

In this chapter, we prove the fundamental theorem of asset pricing and we give
several applications, from arbitrage detection in the foreign exchange market, to
pricing of options, and clientele effects in bond portfolio management.


**4.1** **Arbitrage** **Detection** **in** **the** **Foreign** **Exchange** **Market**


The foreign exchange market includes the trading of currencies. It is one of the
markets with largest trading volume. Given two currencies at any particular time,
say the US dollar and the euro, there are two exchange rates between them: one
dollar will buy _r_ 1 euros, and one euro will buy _r_ 2 dollars. It is evident that an
arbitrage opportunity would arise if _r_ 1 _r_ 2 _>_ 1 since one could simultaneously
convert 1 dollar into _r_ 1 euros and the _r_ 1 euros into _r_ 1 _r_ 2 _>_ 1 dollars. These two
transactions would net _r_ 1 _r_ 2 _−_ 1 dollars without any risk.
An interesting related question is: Can one detect a similar type of arbitrage opportunity involving more than two currencies? In particular, consider
the following hypothetical exchange rates among the currencies USD (US Dollars), EUR (Euros), GBP (British Pounds), AUD (Australian Dollars), and JPY
(Japanese Yen).


USD EUR GBP AUD JPY


USD 1 0.639 0.537 1.0835 98.89
EUR 1.564 1 0.843 1.6958 154.773
GBP 1.856 1.186 1 2.014 184.122
AUD 0.9223 0.589 0.496 1 91.263
JPY 0.01011 0.00645 0.00543 0.01095 1


A simple verification shows that there are no arbitrage opportunities involving
only two currencies. However, could there be one involving more than two currencies? Could you simply eyeball such an opportunity? If you cannot, can you
prove that such an opportunity does not exist?
We next show how to answer these questions using linear programming. For
convenience, use _i_ = 1 _, . . .,_ 5 to index the above five currencies USD, EUR,
GBP, AUD, and JPY in that order. We let _aij_ denote the exchange rate from


54 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


currency _i_ to currency _j_ . For instance _a_ 34 = 2 _._ 014 and _a_ 25 = 154 _._ 773 _._ To model
a set of transactions with potential for arbitrage, consider the following decision
variables:


_•_ _xij_ : amount of currency _i_ converted to currency _j_ .

_•_ _yk_ : net amount of currency _k_ after all transactions.


These variables are related via the following constraints:



�5

_xkj,_ _k_ = 1 _, . . .,_ 5 _._

_j_ =1



_yk_ =



�5

_aikxik −_

_i_ =1



An arbitrage would exist if there is a set of transactions so that after all transactions the net amount for each currency is non-negative and at least one of them
is strictly positive. To find such a set of transactions we could solve the following
linear programming problem:


max _y_ 1



�5

_xkj,_ _k_ = 1 _, . . .,_ 5

_j_ =1



s.t. _yk_ =



�5

_aikxik −_

_i_ =1



_xij_ _≥_ 0
_yk_ _≥_ 0 _._


However, if there is indeed an arbitrage opportunity, then the above problem
would be unbounded. We can easily amend the above model so that the arbitrage
can be revealed by introducing a bound on the objective function:


max _y_ 1



�5

_xkj,_ _k_ = 1 _, . . .,_ 5

_j_ =1



s.t. _yk_ =



�5

_aikxik −_

_i_ =1



_y_ 1 _≤_ 1
_xij_ _≥_ 0
_yk_ _≥_ 0 _._


Solving this linear programming model, we find that indeed there are arbitrage
opportunities. However, to obtain $1 in arbitrage, we have to exchange about
1669.172 US dollars into 1066.601 euros, then convert these euros into 899.1446
pounds, then convert these pounds into 1810.877 Australian dollars, and finally
change these Australian dollars into 1670.172 US dollars. The arbitrage opportunity is so tight that, depending on the numerical precision used, a linear
programming solver may not find it. Furthermore, even if a solver does find
it, the tightness of the arbitrage may render it impractical when accounting for
market frictions such as transaction costs.


**4.2** **The** **Fundamental** **Theorem** **of** **Asset** **Pricing** 55


**4.2** **The** **Fundamental** **Theorem** **of** **Asset** **Pricing**


One of the most widely studied problems in financial mathematics is the pricing
of _contingent_ _claims_ . These are securities whose price depends on the value of
another _underlying_ _security_ . Under the assumption of no arbitrage, the price of
such a contingent claim should match the price of a portfolio that replicates the
payoff of the contingent claim. This basic principle underlies the powerful option
pricing machinery dating back to the pioneering work of Merton (1973) and Black
and Scholes (1973). The absence of arbitrage and the replication argument can
be cleverly stated in terms of a so-called _risk-neutral_ _probability_ _measure_ . The
latter concept can be equivalently stated in terms of a _stochastic_ _discount_ _factor_
or a _positive_ _linear_ _pricing_ _rule._
We next use linear programming duality to give a formal derivation of the
equivalence between the absence of arbitrage and the existence of a risk-neutral
probability measure for the special case of a simple economy in a single-period

                                       - �T
framework. Assume the economy contains _m_ assets. Let **S** 0 := _S_ 0 [1] _· · ·_ _S_ 0 _[m]_

denote the vector of prices per share of the _m_ assets at time 0 (beginning of the
period). Assume there are      - _n_ possible states Ω = _{_      - _ω_ T1 _, . . ., ωn}_ at time 1 (end of
the period). Let **S** 1( _ωj_ ) = _S_ 1 [1][(] _[ω][j]_ [)] _· · ·_ _S_ 1 _[m]_ [(] _[ω][j]_ [)] denote the vector of prices
per share of the _m_ assets at time 1 in state _ωj_ .
An _arbitrage_ _opportunity_ in this economy is an opportunity to make money
without any cost and without any risk. Mathematically, an arbitrage opportunity
is a portfolio of the _m_ assets that has non-positive cost, yields non-negative
payoffs in all future states, and in addition either has strictly negative cost
or generates a strictly positive payoff in some future state. In other words, an
arbitrage portfolio is a set of holdings _y_ 1 _, . . ., ym_ in the _m_ assets such that

**S** [T] 0 **[y]** _[ ≤]_ [0] _[,]_ **S** 1( _ωj_ ) [T] **y** _≥_ 0 _,_ _j_ = 1 _, . . ., n_


and such that at least one of these inequalities is strict.
A _positive_ _linear_ _pricing_ _rule_ is a set of positive numbers _x_ 1 _, . . ., xn_ such that

      - _n_



**S** 0 =



**S** 1( _ωj_ ) _xj,_ _i_ = 1 _, . . ., m._

_j_ =1



**Proposition 4.1** _In the above single-period economy with m assets and n future_
_states there is no arbitrage if and only if there exists a positive linear pricing rule._

          -          _Proof_ Let **S** := **S** 1( _ω_ 1) _· · ·_ **S** 1( _ωn_ ) _._ An arbitrage portfolio is precisely a
solution to the following system of inequalities:

                 - �T
**S** _−_ **S** 0 **y** ≩ **0** _._ (4.1)


Similarly, a positive linear pricing rule is precisely a solution to the following
system of inequalities:

**Sx** = **S** 0 (4.2)
**x** _>_ **0** _._


56 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


Observe that (4.2) has a solution if and only if the following system of inequalities
has a solution:

                       -                        **S** _−_ **S** 0 **u** = **0** (4.3)
**u** _>_ **0** _._


Hence it suffices to show that (4.1) does not have a solution if and only if (4.3)
has a solution. This readily follows from Theorem 2.5(c).


The existence of a positive linear pricing rule can be equivalently stated in
terms of a stochastic discount factor or in terms of a risk-neutral measure. In
both of these interpretations the set of future states Ω = _{ω_ 1 _, . . ., ωn}_ is seen as
a probability space. Assume Ω is endowed with a probability measure P. Then
the future payoff of each asset _i_ can be seen as a random variable _Si_ : Ω _→_ R. A
_stochastic_ _discount_ _factor_ is a random variable _D_ : Ω _→_ R such that



**S** 0 = E( _D_ **S** 1) =




- _n_

_D_ ( _ωj_ ) **S** 1( _ωj_ )P( _ωj_ ) _,_ _i_ = 1 _, . . ., m._

_j_ =1



For convenience, assume there is a risk-free asset in the above economy; that is,
an asset _i_ such that _S_ 0 _[i]_ [=] [1] [and] _[S]_ 1 _[i]_ [(] _[ω][j]_ [)] [=] [1 +] _[ r]_ [for] _[j]_ [=] [1] _[, . . ., n.]_ [A] _[risk-neutral]_
_probability_ _measure_ is a probability measure Q in the space Ω = _{ω_ 1 _, . . ., ωn}_
such that



1 1
**S** 0 = E�( **S** 1) =
1 + _r_ 1 + _r_




- _n_

**S** 1( _ωj_ )Q( _ωj_ ) _._

_j_ =1



Here E [�] indicates that the expectation is taken with respect to the risk-neutral
probability measure Q, as opposed to the original probability measure P _._
We can now formally state the fundamental theorem of asset pricing.


**Theorem 4.2** (Fundamental theorem of asset pricing) _Consider the above single-_
_period_ _economy_ _with_ _n_ _future_ _states_ _and_ _m_ _assets,_ _one_ _of_ _which_ _is_ _risk-free._ _The_
_following_ _conditions_ _are_ _equivalent:_


(i) _There_ _are_ _no_ _arbitrage_ _opportunities._
(ii) _There_ _exists_ _a_ _positive_ _linear_ _pricing_ _rule._
(iii) _There_ _exists_ _a_ _positive_ _stochastic_ _discount_ _factor._
(iv) _There_ _exists_ _a_ _risk-neutral_ _probability_ _measure._


Proposition 4.1, which gives the equivalence between (i) and (ii), provides the
crux of the proof of Theorem 4.2. The proofs of the other equivalences are a
straightforward exercise.


**4.3** **One-Period** **Binomial** **Pricing** **Model**


This section illustrates the _pricing_ of a contingent claim on an underlying risky
security in a simple one-period binomial model. This model provides the building


**4.3** **One-Period** **Binomial** **Pricing** **Model** 57


block for the powerful and widely used multi-period _binomial_ _pricing_ _model_ that
we will discuss in Chapter 15.
Consider a single-period economy with a risk-free asset and a risky asset. Let
_r_ denote the risk-free rate and _S_ 0 denote the price per share of the risky asset
at time 0. Assume there are two possible future states Ω = _{H, T_ _}_ at time 1.
Assume the price per share of the risky asset at time 1 is _S_ 1( _H_ ) = _u · S_ 0 in state
_H_ and _S_ 1( _T_ ) = _d · S_ 0 in state _T_ for some “up” and “down” factors _u > d >_ 0:




  _S_ 0 [���]

HHHj



_S_ 1( _H_ ) = _uS_ 0


_S_ 1( _T_ ) = _dS_ 0



In this economy there is no arbitrage if and only if _u >_ 1 + _r_ _> d_ and in this
case the risk-neutral probability measure should satisfy


1 _S_ 0
_S_ 0 =
1 + _r_ [(][Q][(] _[H]_ [)] _[S]_ [1][(] _[H]_ [) +][ Q][(] _[T]_ [)] _[S]_ [2][(] _[T]_ [)) =] 1 + _r_ [(][Q][(] _[H]_ [)] _[u]_ [ +][ Q][(] _[T]_ [)] _[d]_ [)]

1 = Q( _H_ ) + Q( _T_ ) _._


Therefore,



Q( _H_ ) = [1 +] _[ r][ −]_ _[d]_



_._ (4.4)
_u −_ _d_




_[ r][ −]_ _[d]_

_,_ Q( _T_ ) = _[u][ −]_ [1] _[ −]_ _[r]_
_u −_ _d_ _u −_ _d_



It is customary to write _p_ ˜ := Q( _H_ ) and _q_ ˜ := 1 _−_ _p_ ˜ = Q( _T_ ) as shorthand for the
risk-neutral probabilities and _p_ = P( _H_ ) and _q_ = 1 _−_ _p_ = P( _T_ ) for the actual
probabilities:
Consider the problem of pricing a _contingent_ _claim_ on the risky asset with the
following payoff structure:



_V_ 0 =? [���] 
HHHj



_V_ 1( _H_ )


_V_ 1( _T_ )



For example, the contingent claim could be a _European_ _call_ _option_  - that is,
a contract with the following conditions. At time 1, the _holder_ of the option has
the right, but not the obligation, to purchase a share of the risky asset, known
as the _underlying_ _security_, for a prescribed amount, known as the _strike_ _price._
Thus the payoff of a European call option with strike _K_ is _V_ 1 = ( _S_ 1 _−_ _K_ ) [+] :=
max _{S_ 1 _−_ _K,_ 0 _}_ . The payoff structure of this option in our one-period binomial
model is as follows:



_V_ 0 =? [���] 
HHHj



_V_ 1( _H_ ) = ( _uS_ 0 _−_ _K_ ) [+]


_V_ 1( _T_ ) = ( _dS_ 0 _−_ _K_ ) [+]



A _European_ _put_ _option_ is a similar contract, except that it confers the right to
sell the underlying security for a prescribed strike price.
The fundamental theorem of asset pricing implies that the fair price _V_ 0 of a
general contingent claim with payoffs _V_ 1( _H_ ) and _V_ 1( _T_ ) is


58 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


1
_V_ 0 =
1 + _r_ [(˜] _[pV]_ [1][(] _[H]_ [) + ˜] _[qV]_ [1][(] _[T]_ [))] _[.]_


Furthermore, the binomial pricing model yields the following _delta-hedging_ formula to construct a portfolio of the underlying risky asset and the risk-free asset
that replicates the payoff of the contingent claim. At time 0 construct a portfolio
with Δ shares of the underlying risky asset and _B_ shares of the risk-free asset
where



Δ := _[V]_ [1][(] _[H]_ [)] _[ −]_ _[V]_ [1][(] _[T]_ [)]




_[V]_ [1][(] _[H]_ [)] _[ −]_ _[V]_ [1][(] _[T]_ [)] _[V]_ [1][(] _[H]_ [)] _[ −]_ _[V]_ [1][(] _[T]_ [)]

_S_ 1( _H_ ) _−_ _S_ 1( _T_ ) [=] _S_ 0( _u −_ _d_ )




_[H]_ [)] _[ −]_ _[V]_ [1][(] _[T]_ [)]

_,_ _B_ := _[uV]_ [1][(] _[T]_ [)] _[ −]_ _[dV]_ [1][(] _[H]_ [)]
_S_ 0( _u −_ _d_ ) (1 + _r_ )( _u −_ _d_ )



_._
(1 + _r_ )( _u −_ _d_ )



A straightforward verification shows that this portfolio replicates the payoff of
the contingent claim. That is, the payoff of the portfolio (Δ _, B_ ) is as follows:



Δ _S_ 0 + _B_ [���] HHH*j



Δ _S_ 1( _H_ ) + (1 + _r_ ) _B_ = _V_ 1( _H_ )


Δ _S_ 1( _T_ ) + (1 + _r_ ) _B_ = _V_ 1( _T_ )



Thus the value of this replicating portfolio at time 0 must be _V_ 0 to rule out
arbitrage. Indeed, the value of the replicating portfolio at time 0 is

Δ _S_ 0 + _B_ = [(1 +] _[ r]_ [)(] _[V]_ [1][(] _[H]_ [)] _[ −]_ _[V]_ [1][(] _[T]_ [)) +] _[ uV]_ [1][(] _[T]_ [)] _[ −]_ _[dV]_ [1][(] _[H]_ [)]

(1 + _r_ )( _u −_ _d_ )

1
=
1 + _r_ [(˜] _[pV]_ [1][(] _[H]_ [) + ˜] _[qV]_ [1][(] _[T]_ [)) =] _[ V]_ [0] _[.]_


**Example** **4.3** Suppose stock XYZ has share price _S_ 0 = 40 today. Suppose the
share price of stock XYZ a month from today will either double or halve with
equal probabilities:



_S_ 0 = 40 [���] 
HHHj



_S_ 1( _H_ ) = 80


_S_ 1( _T_ ) = 20



Assume also that the one-month risk-free rate is zero. Consider a European
call option to buy one share of XYZ stock for $50 a month from today. What is
the fair price of this option?


In Example 4.3 we have _u_ = 2 _, d_ = 12 [and] _[r]_ [=] [0.] [Thus] [the] [risk-neutral]
probabilities are _p_ ˜ = [1] 3 [and] _[q]_ [˜] [=] [2] 3 _[.]_ [ Next, observe that a month from now the call]

option with strike price $50 will be worth $30 = $80 _−_ $50 in the _H_ state and it
will be worthless in the _T_ state. Thus the fair price of the option is the price of
the following contract:



? [���] HHH*j



(80 _−_ 50) [+] = 30


(20 _−_ 50) [+] = 0



The fundamental theorem of asset pricing implies that the fair price of this
contract is

30 _·_ _p_ ˜ + 0 _·_ ˜ _q_ = 30 _·_ [1]

3 [= 10] _[.]_


**4.4** **Static** **Arbitrage** **Bounds** 59


Furthermore, from the delta-hedging formula it follows that a replicating portfolio can be constructed by buying [1] 2 [share of stock XYZ and borrowing 10 shares of]

the risk-free asset. Observe that the value of this replicating portfolio at time 0 is


1
2 _[·]_ [ 40] _[ −]_ [10 = 10] _[.]_


Using the risk-neutral probability measure we can also price other derivative
securities on the XYZ stock. For example, consider a European put option on
the XYZ stock with strike price $60 and with the same expiration date:



? [���] HHH*j



(60 _−_ 80) [+] = 0


(60 _−_ 20) [+] = 40



It readily follows that the fair price of this option is




[2] [80]

3 [=] 3



0 _·_ _p_ ˜ + 40 _·_ ˜ _q_ = 40 _·_ [2]



3 _[.]_



Observe that in the one-period binomial pricing model the risk-neutral probability is unique and the payoff of any contingent claim can be replicated via
delta-hedging. In general, uniqueness of the risk-neutral probability corresponds
to _completeness_ of the market. The latter concept means that the payoff of any
contract can be replicated with a portfolio of the existing underlying assets in
the economy as detailed in Exercise 4.6.


**4.4** **Static** **Arbitrage** **Bounds**


The no-arbitrage approach discussed in Section 4.2 has the drawback that it
assumes only a finite number of possible future states. In this section, we do not
make this assumption. Instead, we assume that there is a finite set of derivative
securities written on the same underlying asset and with the same maturity.
We show how the no-arbitrage approach can be used to obtain so-called _static_
_arbitrage_ _bounds_ on the price of a new derivative security implied by the prices
of the other derivative securities. As in Section 4.2, the gist of this approach is
to use linear programming to detect arbitrage opportunities in a single-period
economy. This discussion is based on Herzel (2005).
Consider an underlying security with a (random) price _ST_ at a future time _T_ .
Consider _n_ derivative securities written on this security that mature at time _T_,
and have _piecewise_ _linear_ payoff functions Ψ _i_ ( _ST_ ), each with a single breakpoint
_Ki_, for _i_ = 1 _, . . ., n_ . The obvious motivation is the collection of calls and puts
written on the underlying security with strike prices _Ki,_ _i_ = 1 _, . . ., n_ . More
precisely, if the _i_ th derivative security were a European call with strike price _Ki_,
we would have Ψ _i_ ( _ST_ ) = ( _ST −_ _Ki_ ) [+] . If it were a European put with strike price
_Ki_, we would have Ψ _i_ ( _ST_ ) = ( _Ki −_ _ST_ ) [+] .


60 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


We shall assume without loss of generality that the _Ki_ s are in increasing order.
portfolioAlso, we let **x** = _pi_          - _x_ denote1 _· · ·_ the _xn_ current�T of thepricederivativeof the _i_ thsecuritiesderivative1 tosecurity. _n_ and letConsiderΨ **x** ( _ST_ )a
denote the payoff function of the portfolio:



Ψ **[x]** ( _ST_ ) =


The cost of the portfolio **x** is given by




- _n_

Ψ _i_ ( _ST_ ) _xi._

_i_ =1




      - _n_

_pixi._ (4.5)

_i_ =1


To determine whether there exists an arbitrage opportunity in the above set
of _n_ derivative securities, we consider the following question: Is it possible to
construct a portfolio of the derivative securities 1 _, . . ., n_ with negative cost and
whose payoff function Ψ **[x]** ( _ST_ ) at time _T_ is non-negative for all _ST_ _∈_ [0 _, ∞_ )?
Since non-negativity of Ψ **[x]** ( _ST_ ) corresponds to “no future obligations” such a
portfolio would be an arbitrage opportunity.
Since all Ψ _i_ ( _ST_ )s are piecewise linear, so is Ψ **[x]** ( _ST_ ) with breakpoints in
_K_ 1 _, . . ., Kn_ . Note that a piecewise linear function is non-negative over [0 _, ∞_ )
if and only if it is non-negative at 0 and all the breakpoints, and if the slope
of the function is non-negative to the right of the largest breakpoint. In other
words, Ψ **[x]** ( _ST_ ) is non-negative for all _ST_ _≥_ 0 if and only if the following three
conditions hold:


(i) Ψ **[x]** (0) _≥_ 0,
(ii) Ψ **[x]** ( _Kj_ ) _≥_ 0 _,_ _j_ = 1 _, . . ., n_,
(iii) [(Ψ **[x]** ) _[′]_ + [(] _[K][n]_ [)]] _[ ≥]_ [0.]


These three conditions can be written as the following system of linear
inequalities:




- _n_



Ψ _i_ (0) _xi_ _≥_ 0

_i_ =1




- _n_



(4.6)




- _n_



Ψ _i_ ( _Kj_ ) _xi_ _≥_ 0 _,_ _j_ = 1 _, . . ., n_

_i_ =1



(Ψ _i_ ( _Kn_ + 1) _−_ Ψ _i_ ( _Kn_ )) _xi_ _≥_ 0 _._

_i_ =1



Since all Ψ _i_ ( _ST_ )s are piecewise linear, the quantity Ψ _i_ ( _Kn_ + 1) _−_ Ψ _i_ ( _Kn_ ) gives
the right derivative of Ψ _i_ ( _ST_ ) at _Kn_ and the expression in the last constraint is
the right derivative of Ψ **[x]** ( _ST_ ) at _Kn_ . The system of linear inequalities (4.6) can
be more succinctly written as


**Kx** _≥_ **0**


**4.4** **Static** **Arbitrage** **Bounds** 61



for



Ψ1(0) _· · ·_ Ψ _n_ (0)
Ψ1( _K_ 1) _· · ·_ Ψ _n_ ( _K_ 1)
... ...
Ψ1( _Kn_ ) _· · ·_ Ψ _n_ ( _Kn_ )
Ψ1( _Kn_ + 1) _−_ Ψ1( _Kn_ ) _· · ·_ Ψ _n_ ( _Kn_ + 1) _−_ Ψ( _Kn_ )



⎤


_._
⎥⎥⎥⎥⎥⎦



**K** :=



⎡

⎢⎢⎢⎢⎢⎣



It thus follows that the above type of arbitrage opportunity exists if and only if
the following problem has a solution:


**Kx** _≥_ **0** _,_ **p** [T] **x** _<_ 0 _._


Next, we focus on the special case where the derivative securities under consideration are European call options with strikes _Ki_ for _i_ = 1 _, . . ., n_ . In this case
Ψ _i_ ( _ST_ ) = ( _ST_ _−_ _Ki_ ) [+] and hence


Ψ _i_ ( _Kj_ ) = ( _Kj_ _−_ _Ki_ ) [+] _._


In this case, (4.6) can be written as


**Ax** _≥_ **0** (4.7)



for



⎤



_K_ 2 _−_ _K_ 1 0 0 _· · ·_ 0
_K_ 3 _−_ _K_ 1 _K_ 3 _−_ _K_ 2 0 _· · ·_ 0
... ... ... ... ...
_Kn −_ _K_ 1 _Kn −_ _K_ 2 _Kn −_ _K_ 3 _· · ·_ 0
1 1 1 _· · ·_ 1



_._
⎥⎥⎥⎥⎥⎦



**A** =



⎡

⎢⎢⎢⎢⎢⎣



This formulation is obtained by removing the first two constraints of (4.6) which
are redundant in this particular case. Using this formulation, we obtain the
following theorem giving necessary and sufficient conditions for a set of call
option prices to contain no arbitrage opportunities.


**Theorem** **4.4** _Let_ _K_ 1 _≤_ _K_ 2 _≤· · ·_ _≤_ _Kn_ _denote_ _the_ _strike_ _prices_ _of_ _European_
_call_ _options_ _written_ _on_ _the_ _same_ _underlying_ _security_ _with_ _the_ _same_ _maturity._ _For_
_i_ = 1 _, . . ., n_ _let_ _pi_ _denote_ _the_ _price_ _of_ _the_ _ith_ _call_ _option._ _There_ _are_ _no_ _arbitrage_
_opportunities_ _if_ _and_ _only_ _if_ _the_ _prices_ _pi,_ _i_ = 1 _, . . ., n,_ _satisfy_ _the_ _following_
_conditions:_


(i) 0 _≤_ _pn_ _≤_ _pn−_ 1 _≤· · · ≤_ _p_ 1 _._
(ii) _The piecewise linear_ _function C_ : [ _K_ 1 _, Kn_ ] _→_ R _with breakpoints_ _K_ 1 _, . . ., Kn_
_defined_ _by_ _C_ ( _Ki_ ) := _pi,_ _i_ = 1 _, . . ., n,_ _is_ _convex._


The previous approach can be further extended to infer both lower and upper
bounds on the current price _p_ new of a new derivative with maturity _T_ and payoff
Ψnew( _ST_ ) given prices of other derivatives on the same underlying security and
with the same maturity. As before, assume Ψnew( _ST_ ) and Ψ _i_ ( _ST_ ) are piecewise


62 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


linear functions each with a single breakpoint _K_ and _Ki,_ _i_ = 1 _, . . ., n_, respectively. Assume _K_ 1 _≤_ _K_ 2 _≤· · ·_ _≤_ _Kn_ and let _pi_ denote the current price of the
_i_ th derivative security.
Assume there is no arbitrage involving the _n_ derivatives with payoffs Ψ _i_ ( _ST_ ),
for _i_ = 1 _, . . ., n_ . The previous reasoning applied to the larger set of _n_ + 1
derivatives shows that there is no arbitrage if and only if the following two
conditions hold:


                             - �T

_•_ First, _p_ new _≥_ **p** [T] **x** for any portfolio **x** = _x_ 1 _· · ·_ _xn_ such that


Ψnew( _ST_ ) _≥_ Ψ **[x]** ( _ST_ ) for all _ST_ _≥_ 0 _._


                              - �T

_•_ Second, _p_ new _≤_ **p** [T] **x** for any portfolio **x** = _x_ 1 _· · ·_ _xn_ such that


Ψnew( _ST_ ) _≤_ Ψ **[x]** ( _ST_ ) for all _ST_ _≥_ 0 _._


In words, the first condition states that the price of the new derivative has to be
at least as large as the price of any sub-replicating portfolio of the old securities.
Likewise, the second condition states that the price of the new derivative has
to be at most as large as the price of any super-replicating portfolio of the
old securities. The above two conditions automatically yield the following static
arbitrage bounds on _p_ .


_**Lower**_ _**bound**_ **:**


_p_ _[ℓ]_ new [:= max] **p** [T] **x**
s.t. Ψnew( _ST_ ) _≥_ Ψ **[x]** ( _ST_ ) for all _ST_ _≥_ 0 _._


_**Upper**_ _**bound**_ **:**


_p_ _[u]_ new [:= min] **p** [T] **x**
s.t. Ψnew( _ST_ ) _≤_ Ψ **[x]** ( _ST_ ) for all _ST_ _≥_ 0 _._


The piecewise linearity of Ψnew( _ST_ ) and Ψ _i_ ( _ST_ ) _,_ _i_ = 1 _, . . ., n,_ implies that both
inequalities Ψnew( _ST_ ) _≥_ Ψ **[x]** ( _ST_ ) for all _ST_ _≥_ 0, and Ψnew( _ST_ ) _≥_ Ψ **[x]** ( _ST_ ) for
all _ST_ _≥_ 0 can be formulated as a finite system of linear inequalities. Therefore,
both the upper and lower static arbitrage bounds can be formulated as linear programming models. In particular, for the special case where Ψ _i_ ( _ST_ ) = ( _ST −Ki_ ) [+],
for _i_ = 1 _, . . ., n,_ and Ψnew( _ST_ ) = ( _ST_ _−_ _K_ ) [+] with _K_ 1 _≤_ _K_ _≤_ _Kn_ the static arbitrage upper bound _p_ _[u]_ new [on] _[ p]_ [ can be written as the following linear programming]
model (Exercise 4.10):


_p_ _[u]_ new [:= min] **p** [T] **x**
(4.8)
s.t. **Ax** _≥_ **b** _,_


**4.5** **Tax** **Clientele** **Effects** **in** **Bond** **Portfolio** **Management** 63



where


**A** =



⎡

⎢⎢⎢⎢⎢⎣



_,_ **b** =
⎥⎥⎥⎥⎥⎦



( _K_ 2 _−_ _K_ ) [+]

( _K_ 3 _−_ _K_ ) [+]
...
( _Kn −_ _K_ ) [+]

0



_K_ 2 _−_ _K_ 1 0 0 _· · ·_ 0
_K_ 3 _−_ _K_ 1 _K_ 3 _−_ _K_ 2 0 _· · ·_ 0
... ... ... ... ...
_Kn −_ _K_ 1 _Kn −_ _K_ 2 _Kn −_ _K_ 3 _· · ·_ 0
1 1 1 _· · ·_ 1



⎤



⎤


_._
⎥⎥⎥⎥⎥⎦



⎡

⎢⎢⎢⎢⎢⎣



**4.5** **Tax** **Clientele** **Effects** **in** **Bond** **Portfolio** **Management**


This section presents a model proposed by Ronn (1987) to elicit _clientele_ _effects_
induced by taxes in the bond market. Related models were also proposed by
Hodges and Schaefer (1977) and Schaefer (1982). The crux of the model is to
formulate a linear program that exploits the price differential of bonds given
their after-tax cash flows. To do so, the model finds a long–short portfolio that
simultaneously buys “underpriced” bonds and sells “overpriced” bonds while
ensuring non-negative cash flows throughout the lives of the bonds.
Next we describe the details of the model. Assume the bond market includes
_N_ bonds with the following characteristics:


_•_ The ask and bid prices of bond _j_ are _p_ _[a]_ _j_ [and] _[p][b]_ _j_ [respectively] [for] _[j]_ [= 1] _[, . . ., N.]_

_•_ Each unit of bond _j_ generates a cash flow _a_ _[t]_ _j_ [at] [date] _[t]_ [for] _[j]_ [=] [1] _[, . . ., N]_
and _t_ = 1 _, . . ., T._ These cash flows are after-tax coupon and/or principal
payments.


_•_ The minimal risk-free reinvestment rate at future dates _t_ = 1 _, . . ., T_ is _ρ_ .


_Linear_ _programming_ _model_ _for_ _tax_ _clientele_ _effects_ _in_ _the_ _bond_ _market_


**Variables:**


_x_ _[a]_ _j_ [:] [number] [of] [units] [of] [bond] _[j]_ [bought,] [for] _[j]_ [= 1] _[, . . ., N]_

_x_ _[b]_ _j_ [:] [number] [of] [units] [of] [bond] _[j]_ [sold,] [for] _[j]_ [= 1] _[, . . ., N]_


_zt_ : surplus cash flow at date _t_, for _t_ = 1 _, . . ., T_ .


**Objective:**




- _N_

_p_ _[a]_ _j_ _[x]_ _j_ _[a][.]_
_j_ =1



max




- _N_

_p_ _[b]_ _j_ _[x][b]_ _j_ _[−]_
_j_ =1


64 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


**Constraints:** Cash balance constraints in each date and bounds on _x_ _[a]_ _j_ _[, x]_ _j_ _[b][,]_
and _zt_ :




- _N_

_a_ [1] _j_ _[x][b]_ _j_
_j_ =1



_z_ 1 =




- _N_

_a_ [1] _j_ _[x][a]_ _j_ _[−]_
_j_ =1




- _N_

_a_ _[t]_ _j_ _[x][b]_ _j_ _[,]_ for _t_ = 2 _, . . ., T_
_j_ =1



_zt_ = (1 + _ρ_ ) _zt−_ 1 +




- _N_

_a_ _[t]_ _j_ _[x][a]_ _j_ _[−]_
_j_ =1



_x_ _[a]_ _j_ _[, x]_ _j_ _[b]_ _≥_ 0 _,_ for _j_ = 1 _, . . ., N_
_zt_ _≥_ 0 _,_ for _t_ = 1 _, . . ., T_
_x_ _[a]_ _j_ _[, x]_ _j_ _[b]_ _≤_ 1 _,_ for _j_ = 1 _, . . ., N._
(4.9)


Some comments are in order. The above objective function is the net difference
between the value of the short positions and long positions of the portfolio. The
short positions have to settle at the bid prices whereas the long positions have
to settle at the ask prices. Because of this distinction, the constraints _x_ _[a]_ _j_ _[, x]_ _j_ _[b]_ _[≥]_ [0]
are required. To ensure that the portfolio is risk-free, we require the surplus cash
flows _zt_ to be non-negative for each date _t_ .
The resulting linear program admits two main types of solutions. Either all
bonds are priced within the bid–ask spread. In that case the optimal value of
the linear program is zero and it is trivially attained by not taking any short or
long positions. On the other hand, if there are exploitable price differentials in
the bonds, the linear program chooses long and short holdings so as to maximize
the difference between the values of the long and short positions. In that case
the optimal value is positive. To avoid unbounded values, the model includes the
upper bounds _x_ _[a]_ _j_ _[, x]_ _j_ _[b]_ _[≤]_ [1] [on] [the] [long] [and] [short] [holdings.]
Note that the model requires bonds with perfectly forecastable cash flows.
Thus, non-callable bonds and notes are deemed appropriate, but callable bonds
are excluded.
The proposed model explicitly accounts for the taxation of income and capital
gains for specific investor classes. This means that the cash flows need to be
adjusted for the presence of taxes. For a discount bond (that is, when _p_ _[a]_ _j_ _[<]_ [ 100),]
the after-tax cash flow of bond _j_ at date _t_ is


_a_ _[t]_ _j_ [=] _[ c]_ _j_ _[t]_ [(1] _[ −]_ _[τ]_ [)] _[,]_

where _c_ _[t]_ _j_ [is] [the] [coupon] [payment] [at] [date] _[t]_ [and] _[τ]_ [is] [the] [ordinary] [income] [tax] [rate.]
At maturity, the after-tax cash flow of bond _j_ is


_a_ _[t]_ _j_ [= (100] _[ −]_ _[p]_ _j_ _[a]_ [)(1] _[ −]_ _[g]_ [) +] _[ p]_ _j_ _[a][,]_


where _g_ is the capital gains tax rate.
On the other hand, for a premium bond (that is, when _p_ _[a]_ _j_ _[>]_ [ 100), the premium]
is amortized against ordinary income over the life of the bond, giving rise to an
after-tax coupon payment of




  _j_ _[−]_ [100]
_a_ _[t]_ _j_ [=] _c_ _[t]_ _j_ _[−]_ _[p][a]_




_j_ _[−]_ [100]
(1 _−_ _τ_ ) + _[p][a]_



_,_
_nj_



_nj_


**4.7** **Exercises** 65


where _nj_ is the number of coupon payments remaining to maturity.
A premium bond also makes a non-taxable repayment of


_a_ _[t]_ _j_ [= 100]


at maturity.
Major categories of taxable investors are domestic banks, insurance companies,
individuals, non-financial corporations, and foreigners. In each case, one needs
to distinguish the tax rates on capital gains versus ordinary income.
As an example, consider tax-exempt investors. For this class of investors,
Schaefer (1982) observed that the “purchased” portfolio contains high coupon
bonds and the “sold” portfolio is dominated by low coupon bonds. This can be
explained as follows: The preferential taxation of capital gains for (most) taxable
investors causes them to gravitate towards low coupon bonds. Consequently, for
tax-exempt investors, low coupon bonds are “overpriced” and not desirable as
investment vehicles.


**4.6** **Notes**


The fundamental theorem of asset pricing is central to the mathematical finance
literature. The connection between arbitrage and risk-neutral pricing underlies
the classical work of Merton (1973) and Black and Scholes (1973). More explicit
and formal statements on the relation between absence of arbitrage and existence
of stochastic discount factors in single-period as well as in multi-period settings
were developed by Ross (1976), Harrison and Kreps (1979), and Harrison and
Pliska (1981). The textbooks by Back (2010), Duffie (2001), and Shreve (2000)
give a detailed treatment of this important topic.


**4.7** **Exercises**


**Exercise** **4.1** The Excel spreadsheet “Exercise 4.1 FX model” gives crosscurrency exchange rates among the currencies USD, EUR, GBP, AUD, and JPY.
Use a linear programming model to detect if these exchange rates contain an
arbitrage opportunity. To do so, use the following decision variables:


_xij_ : amount of currency _i_ converted to currency _j_ .
_yk_ : net amount of currency _k_ after all transactions.


Is there an arbitrage opportunity? If the answer is yes, then describe it, for
example: “Convert 1000 USD to EUR then to JPY then back to USD to net
1 USD without putting money in.”


**Exercise** **4.2** Let _S_ 0 be the current share price of a “risky” security and
assume that there are two possible share prices for this security at a future


66 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


time _T_ : _ST_ ( _u_ ) = _S_ 0 _· u_ and _ST_ ( _d_ ) = _S_ 0 _· d_, where _u_ _>_ _d_ _>_ 0. Assume there is
also a “risk-free” security with current share price 1 and future share price 1 + _r_
at time _T_ . Show that there is no arbitrage opportunity involving the risky and
risk-free securities if and only if _u >_ 1 + _r_ _> d_ .


**Exercise** **4.3** Assume that the XYZ stock is currently priced at $40. At the
end of the next period, the price of XYZ is expected to be in one of the following
two states: 40 _· u_ or 40 _· d_ . We know that _d_ _<_ 1 _<_ [5] 4 _[<]_ _[u]_ [but] [we] [do] [not] [know]

_d_ or _u_ . The interest rate is zero. If a European call option with strike price $50
is priced at $10 while a European call option with strike price $40 is priced at
$13, and we assume that these prices do not contain any arbitrage opportunities,
what is the fair price of a European put option with a strike price of $40?


**Exercise** **4.4** Assume that the XYZ stock is currently priced at $40. At the
end of the next period, the price of XYZ is expected to be in one of the following
two states: 40 _· u_ or 40 _· d_ . We know that _d <_ 1 _< u_ but we do not know _d_ or _u_ .
The interest rate is _r_ = 0. European call options on XYZ with strike prices of
$30, $40, $50, and $60 are priced at $10, $7, $10/3, and $0. Which one of these
options is mispriced? Why?


**Exercise** **4.5** Prove the equivalences (ii) _⇔_ (iii) _⇔_ (iv) in Theorem 4.2.


**Exercise** **4.6** Consider the setting of Proposition 4.1. Assume there is no
arbitrage and thus a positive linear pricing rule exists.


(a) Show that the linear pricing rule is unique if and only if the matrix **S** has
full column rank.
(b) Consider a new asset with payoff _S_ 1 _[m]_ [+1] ( _ωj_ ) per share in state _ωj_ at time 1.
Show that if the linear pricing rule is unique then there exists a portfolio

           - �T
**y** = _y_ 1 _· · ·_ _ym_ of the _m_ old assets that replicates the payoff of the new
asset; that is,

     - _m_

_S_ 1 _[i]_ [(] _[ω][j]_ [)] _[y][i]_ [=] _[ S]_ 1 _[m]_ [+1] ( _ωj_ ) _,_ _j_ = 1 _, . . ., n._
_i_ =1


(c) Conclude that to rule out arbitrage, the price _S_ 0 _[m]_ [+1] at time 0 of the new
asset must be equal to



**S** [T] 0 **[y]** [ =]


**Exercise** **4.7** Prove Theorem 4.4.




- _m_

_S_ 0 _[i]_ _[y][i][.]_
_i_ =1



**Exercise** **4.8** Both Theorem 4.4 and the linear programming model (4.8)
implicitly assume that the _i_ th call can be bought or sold at the same price _pi_ .
In real markets, there is always a gap between the price a buyer pays for a
security and the amount the seller collects called the _bid–ask_ _spread_ .


**4.7** **Exercises** 67


Assume that the ask price of the _i_ th call is _p_ _[a]_ _i_ [and] [its] [bid] [price] [is] _[p][b]_ _i_ [with]
_p_ _[a]_ _i_ _[> p]_ _i_ _[b]_ [.] [Develop] [analogs] [of] [Theorem] [4.4] [and] [of] [(4.8)] [in] [the] [case] [where] [we] [can]
only purchase the calls at their ask prices or sell them at their bid prices.


**Exercise 4.9** Consider all the call options on the S&P 500 index or on a highly
traded security that expire on the same day, about three months from today.
Their current prices can be downloaded from the website of the Chicago Board
of Options Exchange at www.cboe.com or several other market quote websites.
Formulate the linear programming problem (4.7) (or, rather, the version you
developed for Exercise 4.8 since market quotes will include bid and ask prices)
to determine whether these prices contain any arbitrage opportunities.
Sometimes, illiquid securities (those that are not traded very often) can have
misleading prices since the reported price corresponds to the last transaction
in that security, which may have happened several days ago, and if there were
to be a new transaction, this value would change dramatically. As a result, it
is quite possible that you will discover false “arbitrage opportunities” because
of these misleading prices. Repeat this exercise but this time use only prices
of call options that have had a trading volume of at least 100 on the day you
downloaded the prices.


**Exercise** **4.10** Prove that, for the special case where Ψ _i_ ( _ST_ ) = ( _ST_ _−_ _Ki_ ) [+],
with _i_ = 1 _, . . ., n,_ and Ψnew( _ST_ ) = ( _ST_ _−_ _K_ ) [+] with _K_ 1 _≤_ _K_ _≤_ _Kn_, the
static arbitrage upper bound _p_ _[u]_ new [on] _[p]_ [can] [be] [written] [as] [the] [following] [linear]
programming model:

_p_ _[u]_ new [:= min] **p** [T] **x**
s.t. **Ax** _≥_ **b** _,_


where



_K_ 2 _−_ _K_ 1 0 0 _· · ·_ 0
_K_ 3 _−_ _K_ 1 _K_ 3 _−_ _K_ 2 0 _· · ·_ 0
... ... ... ... ...
_Kn −_ _K_ 1 _Kn −_ _K_ 2 _Kn −_ _K_ 3 _· · ·_ 0
1 1 1 _· · ·_ 1



_,_ **b** =
⎥⎥⎥⎥⎥⎦



( _K_ 2 _−_ _K_ ) [+]

( _K_ 3 _−_ _K_ ) [+]
...
( _Kn −_ _K_ ) [+]

0



⎤



⎤


_._
⎥⎥⎥⎥⎥⎦



⎡

⎢⎢⎢⎢⎢⎣



**A** =



⎡

⎢⎢⎢⎢⎢⎣



**Exercise** **4.11** The purpose of this exercise is to see whether the results
observed by Schaefer (1982) (see Section 4.5) occur in the current bond market.
Only use non-callable bonds and notes.
Consider first the class of tax-exempt investors. Using current data, form the
optimal “purchased” and “sold” bond portfolios using the linear program presented in Section 4.5. Do you observe the same tax clientele effect as documented
by Schaefer for British government securities; namely, the “purchased” portfolio
contains high coupon bonds and the “sold” portfolio is dominated by low coupon
bonds.


68 **Linear** **Programming** **Models:** **Arbitrage** **and** **Asset** **Pricing**


Repeat the same analysis with different types of taxable investors.


(a) Is there a clientele effect in the pricing of US government investments,
with tax-exempt investors, or those without preferential treatment of capital
gains, gravitating towards high coupon bonds?
(b) Do you observe that not all high coupon bonds are desirable to investors
without preferential treatment of capital gains? Nor are all low coupon bonds
attractive to those with preferential treatment of capital gains. Can you find
reasons why this may be the case?


The dual price, say _ut_, associated with the cash balance constraint at date _t_ in
(4.9) represents the present value of an additional dollar at time _t_ . Explain why.
It follows that _ut_ may be used to compute the term structure of spot interest
rates _Rt_, given by the relation




  1
_Rt_ =
_ut_



�1 _/t_

_−_ 1 _._



Compute this week’s term structure of spot interest rates for tax-exempt
investors.


## **Part II** **Single-Period Models**


## 5 Quadratic Programming: Theory and Algorithms

**5.1** **Quadratic** **Programming**


A _quadratic_ _program_ is an optimization problem whose objective is to minimize
or maximize a quadratic function subject to a finite set of linear equality and
inequality constraints. By flipping signs if necessary, a quadratic program can be
written in the generic form:


min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **Ax** = **b** (5.1)
**Dx** _≥_ **d**


for some vectors and matrices **c** _∈_ R _[n]_, **b** _∈_ R _[m]_, **d** _∈_ R _[p]_, **A** _∈_ R _[m][×][n]_, **D** _∈_ R _[p][×][n]_,
**Q** _∈_ R _[n][×][n]_ . As observed in Chapter 1 we may assume that **Q** is a symmetric
matrix. The term _quadratic programming model_ is also used to refer to a quadratic
program. We will use these terms interchangeably throughout the book.
Quadratic programming models arise in a variety of practical contexts. The
seminal _mean–variance_ _model_ of Markowitz and most of its variants for portfolio
selection are quadratic programs as we illustrate in Example 5.1 below and
discuss in full detail in Chapter 6. The popular ordinary least-squares and lasso
estimation procedures in linear regression are also quadratic programs. Quadratic
programs are also often solved as subproblems in the solution of more general
nonlinear optimization problems.
Observe that the constraint set in (5.1) is convex since it is a system of
linear inequalities. Furthermore, the objective function of (5.1) is convex when
**Q** is a positive semidefinite matrix. Throughout this chapter we assume that
**Q** is symmetric and positive semidefinite. Therefore problem (5.1) is a convex
program.
A quadratic programming model is in _standard_ _form_ if it is written as follows:


min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **Ax** = **b** (5.2)
**x** _≥_ **0** _._


**Example 5.1** (Asset allocation) Assume the one-year returns of the asset classes
large stocks, small stocks, and bonds have the following correlations and standard
deviations:


72 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


Large Small Bonds Standard deviation


Large 1 0.6 0.2 0.12
Small 0.6 1 0.5 0.20
Bonds 0.2 0.5 1 0.05


Determine the asset allocation of minimum risk, that is, find a portfolio comprised of these three asset classes whose return has the lowest standard deviation.
Assume the portfolio can only hold long positions in each of the asset classes.


This problem can be formulated as a quadratic programming model. To that
end, first construct the _covariance_ _matrix_ **V** of asset returns: this is the matrix
whose ( _i, j_ ) entry is the covariance of asset _i_ and asset _j_ ; that is, _ρij_ _· σi_ _· σj._
Using matrix notation and ‘ _◦_ ’ to denote the componentwise product of matrices,
the covariance matrix can be computed as



⎡



⎡



0 _._ 0144 0 _._ 024 0 _._ 006
⎣ 0 _._ 024 0 _._ 04 0 _._ 01
0 _._ 006 0 _._ 01 0 _._ 0025



0 _._ 12
⎣0 _._ 20
0 _._ 05



⎤

           ⎦ [�] 0 _._ 12 0 _._ 20 0 _._ 05



**V** =


=


=



1 0 _._ 6 0 _._ 2
⎣0 _._ 6 1 0 _._ 5
0 _._ 2 0 _._ 5 1



0 _._ 0144 0 _._ 0144 0 _._ 0012
⎣0 _._ 0144 0 _._ 04 0 _._ 005
0 _._ 0012 0 _._ 005 0 _._ 0025



⎡



1 0 _._ 6 0 _._ 2
⎣0 _._ 6 1 0 _._ 5
0 _._ 2 0 _._ 5 1



⎤


⎦ _◦_


⎤


⎦ _◦_



⎡



⎤


⎦



⎡



⎤



⎦ _._



We are now ready to describe the quadratic programming formulation for
the above asset allocation problem. (A more detailed discussion is given in
Chapter 6.)


_Quadratic_ _programming_ _model_ _for_ _asset_ _allocation_
**Variables:**
_xi_ : percentage of the portfolio invested in asset _i_ for _i_ = 1 _,_ 2 _,_ 3 _._
**Objective** **(minimize** **the** **variance** **of** **the** **portfolio** **return):**



min min
**x** **[x]** [T] **[Vx]** [ =] _x_ 1 _,x_ 2 _,x_ 3




0 _._ 0144 _x_ [2] 1 [+ 0] _[.]_ [04] _[x]_ 2 [2] [+ 0] _[.]_ [0025] _[x]_ 3 [2] [+ 0] _[.]_ [0288] _[x]_ [1] _[x]_ [2]




            + 0 _._ 0024 _x_ 1 _x_ 3 + 0 _._ 01 _x_ 2 _x_ 3



**Constraints:**


_x_ 1 + _x_ 2 + _x_ 3 = 1 (percentages add up to one)
_x_ 1 _, x_ 2 _, x_ 3 _≥_ 0 (long-only positions).


Observe that even in this small example the quadratic objective is much
more concise and easier to write using matrix notation.


We now discuss the special case of a convex quadratic program without constraints. As Example 5.3 below illustrates, this kind of model arises naturally in
the ordinary least-squares procedure.


**5.1** **Quadratic** **Programming** 73


Consider a quadratic program without constraints:


min **x** 21 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** _[.]_ (5.3)


The optimality conditions in this case are as follows.


**Theorem** **5.2** _Let_ **c** _∈_ R _[n]_ _,_ **Q** _∈_ R _[n][×][n]_ _and_ _assume_ **Q** _is_ _symmetric_ _and_ _positive_
_semidefinite._ _If_ (5.3) _is_ _bounded,_ _then_ _it_ _attains_ _its_ _minimum._ _Furthermore,_ _a_
_point_ **x** _∈_ R _[n]_ _is_ _an_ _optimal_ _solution_ _to_ (5.3) _if_ _and_ _only_ _if_


**Qx** + **c** = **0** _._ (5.4)


When **Q** is positive definite, the problem (5.3) has the unique minimizer **x** =

_−_ **Q** _[−]_ [1] **c** _._ When **Q** is positive semidefinite but not positive definite, the matrix **Q**
is singular and the problem (5.3) is either unbounded or has multiple solutions.


**Example** **5.3** (Ordinary least squares) Assume ( **x** _i, yi_ ), for _i_ = 1 _, . . ., N,_ is
a random sample drawn from the joint distribution of _X, Y_ where _X, Y_ are
respectively R _[p]_ -valued and R-valued random variables. Using the _training_ _data_
( **x** _i, yi_ ), with _i_ = 1 _, . . ., N,_ estimate a vector of coefficients _**β**_ for the linear model


_Y_ = _**β**_ [T] _X_ + _ϵ._


The most popular approach to this problem is to find the estimate of _**β**_ that
solves the following least-squares problem:




 - _N_

min ( _**β**_ [T] **x** _i −_ _yi_ ) [2] _._
_**β**_

_i_ =1



Observe that


 - _N_

( _**β**_ [T] **x** _i −_ _yi_ ) [2] = ( **X** _**β**_ _−_ **y** ) [T] ( **X** _**β**_ _−_ **y** ) = _**β**_ [T] **X** [T] **X** _**β**_ _−_ 2 **y** [T] **X** _**β**_ + **y** [T] **y**

_i_ =1



for



⎡

⎢⎣



_y_ 1
...
_yN_



⎤

⎥⎦ _,_ **y** =



⎤

⎥⎦ _._



**X** =



⎡

**x** [T] 1

⎢⎣ ...

**x** [T] _N_



Hence the least-squares problem can be formulated as follows.


_Quadratic_ _programming_ _formulation_ _for_ _least-squares_ _estimation._
**Variables:**
_**β**_ : vector of coefficients in the linear model _Y_ = _**β**_ [T] _X_ + _ϵ._

**Objective:**

min 12 _**[β]**_ [T] **[Q]** _**[β]**_ _[ −]_ **[b]** [T] _**[β]**_ _[,]_
_**β**_


where **Q** := **X** [T] **X**, **b** = **X** [T] **y** _._
**Constraints:** None.


74 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


By applying Theorem 5.2 we obtain the widely known solution to the
least-squares problem:


_**β**_ ˆ := **Q** _[−]_ [1] **b** = ( **X** [T] **X** ) _[−]_ [1] **X** [T] **y** _,_


provided the _N × p_ matrix **X** has full column rank. This latter condition usually
holds in the typical practical situation when there are more observations than
predictor variables; that is, when _N_ _>_ _p_ . However, the case _N_ _<_ _p_ occurs
as well. In this kind of situation the matrix **X** is never full column rank so
the ordinary least-squares approach is not appropriate. Section 5.6.2 describes
two popular variants for this kind of situation, namely _ridge_ _regression_ and
_lasso_ _regression,_ both of which can be seen as modifications of the ordinary
least-squares procedure.


**5.2** **Numerical** **Quadratic** **Programming** **Solvers**


As with linear programming, there are a variety of highly efficient, fast, and
reliable commercial and open-source software packages for convex quadratic
programming. Most of these packages implement versions of the algorithms
sketched in Section 5.5 below. We illustrate two of these solvers by applying
them to Example 5.1.


Excel Solver


Figure 5.1 displays a printout of an Excel spreadsheet implementation of the
quadratic programming model for Example 5.1 as well as the dialog box obtained
when we run the Excel add-in Solver. The spreadsheet model contains the three
components of the quadratic program. The decision variables are in the range
B20:D20. The objective function is in cell E22. The Excel formula in this cell,
using matrix operations, is as follows:


MMULT(B20 : D20 _,_ MMULT(B16 : D18 _,_ TRANSPOSE(B20 : D20))) _._


The left-hand and right-hand sides of the equality constraint are in cells E20 and
G20 respectively.


MATLAB CVX



Figure 5.2 displays a CVX script for the same problem. The script can be run
provided the freely available CVX toolbox is installed.
Using either of these solvers we obtain the optimal solution to the problem in
Example 5.1:



⎡



⎤



**x** _[∗]_ =



0 _._ 0897
⎣ 0
0 _._ 9103



⎦ _._


**5.3** **Sensitivity** **Analysis** 75


**Figure** **5.1** Spreadsheet implementation and the Solver dialog box for the asset
allocation model


**Figure** **5.2** MATLAB CVX code for the asset allocation model


**5.3** **Sensitivity** **Analysis**


As is the case for linear programming, the process of solving a quadratic program
also generates some interesting _sensitivity information_ via the so-called _Lagrange_
_multipliers_ associated with the constraints. Assume the constraints of a quadratic
program, and hence the Lagrange multipliers, are indexed by _i_ = 1 _, . . ., m_ .
The _Lagrange_ _multiplier_ _yi_ _[∗]_ [of] [the] _[i]_ [th] [constraint] [has] [the] [following] [sensitivity]
interpretation:


If the right-hand side of the _i_ th constraint changes by Δ, then the optimal
value of the quadratic program changes by approximately Δ _·_ _yi_ _[∗]_ [for]
small Δ.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-87-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-87-1.png)
76 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


Unlike the shadow prices of a linear program, the Lagrange multipliers only
give an approximation of the change in the optimal objective value. The situation
is akin to how the derivative of a quadratic (or more general nonlinear) function
at a particular point gives an approximation of the change in the function value
when that point changes.
Both Excel Solver and MATLAB CVX compute the Lagrange multipliers
implicitly. To make this information explicit in Excel Solver, we request a
sensitivity report after running Solver as shown in Figure 5.3.


**Figure** **5.3** Requesting sensitivity report in Solver


Figure 5.4 displays the sensitivity report for Example 5.1. The values _yi_ _[∗]_ [can]
be found in the column labeled “Lagrange Multiplier”. In CVX this information
can also be obtained by including a line of code to save the dual information y
as shown in Figure 5.5. Both solvers yield the dual value **y** _[∗]_ = 0 _._ 0047669 _._


**5.4** ***Duality** **and** **Optimality** **Conditions**


As in linear programming, there is a _dual_ quadratic program associated with
every _primal_ quadratic programming problem, and this dual can be obtained via
the Lagrangian function. Throughout this section consider the _primal_ quadratic



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-88-0.png)
**5.4** ***Duality** **and** **Optimality** **Conditions** 77


**Figure** **5.4** Sensitivity report


**Figure** **5.5** MATLAB CVX code with dual variables


program

min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **Ax** = **b** (5.5)
**Dx** _≥_ **d** _,_


where **c** _∈_ R _[n]_, **Q** _∈_ R _[n][×][n]_, **A** _∈_ R _[m][×][n]_, **b** _∈_ R _[m]_, **D** _∈_ R _[p][×][n]_, **d** _∈_ R _[p]_, and **Q** is
symmetric and positive semidefinite.
The _Lagrangian_ _function_ associated with (5.5) is


_L_ ( **x** _,_ **y** _,_ **s** ) := [1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** [ +] **[ y]** [T][(] **[b]** _[ −]_ **[Ax]** [) +] **[ s]** [T][(] **[d]** _[ −]_ **[Dx]** [)] _[.]_


The constraints of (5.5) can be encoded via the Lagrangian function through the
following observation: For a given vector **x**

        12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** if **Ax** = **b** and **Dx** _≥_ **d**
max **sy** _≥,_ **s0** _L_ ( **x** _,_ **y** _,_ **s** ) = + _∞_ otherwise.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-89-1.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-89-4.png)
78 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


Therefore the primal problem (5.5) can be written as


min **x** [max] **sy** _≥,_ **s0** _L_ ( **x** _,_ **y** _,_ **s** ) _._


The dual problem is obtained by flipping the order of the min and max operations:


max **sy** _≥,_ **s0** min **x** _[L]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ s]** [)] _[.]_


It is easy to see that the dual problem can be written as follows:



max **x** _,_ **y** _,_ **s** **b** [T] **y** + **d** [T] **s** _−_ [1] 2 **[x]** [T] **[Qx]**

s.t. **A** [T] **y** + **D** [T] **s** _−_ **Qx** = **c**
**s** _≥_ **0** _._



(5.6)



In particular, when the primal problem is in standard form (5.2), the dual
problem is


max **x** _,_ **y** _,_ **s** **b** [T] **y** _−_ [1] 2 **[x]** [T] **[Qx]**

s.t. **A** [T] **y** _−_ **Qx** + **s** = **c**
**s** _≥_ **0** _._


Observe that the dual problem of a quadratic program is again a quadratic
program. Note that, unlike the case of linear programming, some primal-like
variables **x** also appear in the dual problem. As in linear programming, there is
a deep connection between the primal problem (5.5) and its dual (5.6). The next
result follows by construction.


**Theorem 5.4** (Weak duality) _Assume_ **x** _is a feasible point for_ (5.5) _and_ (˜ **x** _,_ **y** _,_ **s** )
_is_ _a_ _feasible_ _point_ _for_ (5.6) _._ _Then_



**b** [T] **y** + **d** [T] **s** _−_ [1]




[1] 2 **[x]** [˜][T] **[Q][x]** [˜] _[ ≤]_ 2 [1]




[1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** _[.]_



_Proof_ If **x** and (˜ **x** _,_ **y** _,_ **s** ) satisfy the above assumptions then



**b** [T] **y** + **d** [T] **s** _−_ [1]




[1] 2 **[x]** [˜][T] **[Q][x]** [˜] _[ ≤]_ [(] **[Ax]** [)][T] **[y]** [ + (] **[Dx]** [)][T] **[s]** _[ −]_ 2 [1]




[1] 2 **[x]** [˜][T] **[Q][x]** [˜]



= ( **A** [T] **y** + **D** [T] **s** ) [T] **x** _−_ [1] 2 **[x]** [˜][T] **[Q][x]** [˜]



= ( **c** + **Qx** ˜) [T] **x** _−_ [1] 2 **[x]** [˜][T] **[Q][x]** [˜]




[1]

2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** _[ −]_ [1] 2



= [1]




[1] 2 [(] **[x]** _[ −]_ **[x]** [˜][)][T] **[Q]** [(] **[x]** _[ −]_ **[x]** [˜][)]



_≤_ [1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** _[.]_



The following much deeper result also holds.


**5.4** ***Duality** **and** **Optimality** **Conditions** 79


**Theorem** **5.5** (Strong duality) _Assume_ _one_ _of_ _the_ _problems_ (5.5) _or_ (5.6) _is_
_feasible._ _Then_ _this_ _problem_ _is_ _bounded_ _if_ _and_ _only_ _if_ _the_ _other_ _one_ _is_ _feasible._ _In_
_that_ _case_ _both_ _problems_ _have_ _optimal_ _solutions_ _and_ _their_ _optimal_ _values_ _are_ _the_
_same._


We refer the reader to G¨uler (2010) or Nocedal and Wright (2006) for a proof
of Theorem 5.5. This result is closely tied to certain kinds of _separation_ _theorems_
for convex sets. For details see G¨uler (2010, chapters 6 and 11). A powerful
consequence of Theorem 5.5 is the following characterization of the solutions to
both (5.5) and (5.6).


**Theorem** **5.6** (Optimality conditions) _The_ _vectors_ **x** _∈_ R _[n]_ _and_ (˜ **x** _,_ **y** _,_ **s** ) _∈_ R _[n]_ _×_
R _[m]_ _×_ R _[p]_ _are_ _optimal_ _solutions_ _to_ (5.5) _and_ (5.6) _respectively_ _if_ _and_ _only_ _if_
**Qx** = **Qx** ˜ _and_



**Qx** + **c** _−_ **A** [T] **y** _−_ **D** [T] **s** = **0**
**Ax** _−_ **b** = **0**
**Dx** _−_ **d** _≥_ **0**
**s** _≥_ **0**
( **Dx** _−_ **d** ) _isi_ = 0 _,_ _i_ = 1 _, . . ., p._



(5.7)



For a quadratic program in standard form (5.2), the optimality conditions (5.7)
can be written as follows:




_−_ **Qx** + **A** [T] **y** + **s** = **c**
**Ax** = **b**
**x** _≥_ **0**
**s** _≥_ **0**
_xisi_ = 0 _,_ _i_ = 1 _, . . ., n._



(5.8)



Observe that (5.8) nicely extends the optimality conditions (2.9) for linear programming in standard form.
The optimality conditions (5.7) can be seen as “saddle-point” conditions for
the Lagrangian function


_L_ ( **x** _,_ **y** _,_ **s** ) = [1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** [ +] **[ y]** [T][(] **[b]** _[ −]_ **[Ax]** [) +] **[ s]** [T][(] **[d]** _[ −]_ **[Dx]** [)] _[.]_


We next discuss the special case of a quadratic program with equality constraints only. Consider the problem

min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** (5.9)

s.t. **Ax** = **b** _,_


where **c** _∈_ R _[n]_, **Q** _∈_ R _[n][×][n]_, **A** _∈_ R _[m][×][n]_, **b** _∈_ R _[m]_, and **Q** is symmetric and positive
semidefinite. In this case the optimality conditions (5.7) simplify to


**Qx** + **c** _−_ **A** [T] **y** = **0**
(5.10)
**Ax** _−_ **b** = **0** _._


80 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


The optimality conditions (5.10) in turn can be stated in terms of the Lagrangian
function of (5.9):


_L_ ( **x** _,_ **y** ) = [1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** [ +] **[ y]** [T][(] **[b]** _[ −]_ **[Ax]** [)] _[.]_


Indeed observe that (5.10) can be succinctly written as


_∇L_ ( **x** _,_ **y** ) = **0** _._


When **Q** is positive definite and **A** has full row rank, problem (5.9) has a unique
minimizer **x** and a unique Lagrange multiplier **y** given by




**x**
**y**




- **Q** _−_ **A** [T]
=

**A** **0**




- _−_ 1 � 
_−_ **c**

_._

**b**



In particular, if **Q** is positive definite and **A** has full row rank, then the minimizer
and vector of Lagrange multipliers for the problem



are respectively



min **x** 12 **[x]** [T] **[Qx]** (5.11)

s.t. **Ax** = **b**


**x** _[∗]_ = **Q** _[−]_ [1] **A** [T] ( **AQ** _[−]_ [1] **A** [T] ) _[−]_ [1] **b**

**y** _[∗]_ = ( **AQ** _[−]_ [1] **A** [T] ) _[−]_ [1] **b** _._



**Example** **5.7** (Asset allocation) Consider the same problem as in Example 5.1
but assume this time that the portfolio is allowed to hold short positions.


The formulation for this modification of Example 5.1 is straightforward: just
drop the non-negativity constraint on the variables. Thus we obtain the quadratic
programming model

min **x** 12 **[x]** [T] **[Vx]**

s.t. **1** [T] **x** = 1 _._


From the above discussion it readily follows that the optimal solution and
Lagrange multiplier are


1
**x** _[∗]_ =
**1** [T] **V** _[−]_ [1] **1** **[V]** _[−]_ [1] **[1]**

1
_y_ _[∗]_ =
**1** [T] **V** _[−]_ [1] **1** _[.]_


For the particular value of **V** in Example 5.1 we get the following optimal solution
and Lagrange multiplier



⎤


⎦ _,_ _y_ _[∗]_ = 0 _._ 001897074 _._



**x** _[∗]_ =



⎡

0 _._ 1934
⎣ _−_ 0 _._ 1406
0 _._ 9472


**5.5** ***Algorithms** 81


**5.5** ***Algorithms**


We next sketch extensions of the two main algorithmic schemes for linear programming discussed in Chapter 2. The first scheme, namely _active-set_ _methods_,
can be seen as an analog of the simplex method. The second scheme, namely
interior-point methods, is a straightforward extension from the linear programming to the quadratic programming context.


5.5.1 Active-Set Methods


Active-set methods are based on the following key observation. Assume **x** ¯ is an
optimal solution to (5.5) and


_I_ := _{i_ = 1 _, . . ., p_ : ( **Dx** ¯ _−_ **d** ) _i_ = 0 _}._


Then the optimality conditions (5.7) can be rewritten as



**Qx** + **c** _−_ **A** [T] **y** _−_ **D** [T] _I_ **[s]** _[I]_ = **0**
**Ax** _−_ **b** = **0**
**D** _I_ **x** _−_ **d** _I_ = **0**
**s** _I_ _≥_ **0** _._



(5.12)



If we ignore the last constraint **s** _I_ _≥_ **0**, the remaining conditions in (5.12) are
precisely the optimality conditions of the problem


min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **Ax** = **b** (5.13)
**D** _I_ **x** = **d** _I_ _._


This suggests an algorithmic strategy to solve (5.5): guess the _active_ _set_ _I_
and solve the subproblem (5.13). If the solution **x** ¯ to this subproblem satisfies
the other conditions in (5.7) then stop. Otherwise, make a new guess for _I_ .
Algorithm 5.1 gives a possible version of this strategy.
Each main iteration of Algorithm 5.1 requires solving the following subproblem
for some current trial solution **x** ¯ and trial active set _I_ :


minΔ **x** 21 [(Δ] **[x]** [)][T] **[Q]** [Δ] **[x]** [ + (] **[Q][x]** [¯][ +] **[ c]** [)][T][Δ] **[x]**

s.t. **A** Δ **x** = **0** (5.14)
**D** _I_ Δ **x** = **0** _._


To update the trial solution we also need to compute the step length











_α_ := min



1 _,_ min
_i̸∈I_
**D** _i_ Δ **x** _<_ 0



**d** _i −_ **D** _i_ Δ **x**

**D** _i_ Δ **x**



_._ (5.15)


82 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


**Algorithm** **5.1** Active-set method

1: choose **x** 0 feasible for (5.5) and _I_ 0 _⊆{i_ : **D** _i_ **x** 0 = **d** _i,_ _i_ = 1 _, . . ., p}_

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve (5.14) for _I_ = _Ik_ and **x** ¯ = **x** _k_
4: **if** Δ **x** = 0 **then**

5: compute the Lagrange multipliers ¯ **s** _I_ of (5.14) for _I_ = _Ik_ and **x** ¯ = **x** _k_
6: **if** ¯ **s** _I_ _≥_ **0** **then** HALT **x** ¯ is an optimal solution to (5.5)

7: **else**

8: let _j_ := arg min _i∈I_ ¯ **s** _i_, _Ik_ +1 := _Ik\{j}_, and **x** _k_ +1 := **x** _k_
9: **end** **if**

10: **else**

11: compute _α_ via (5.15) for _I_ = _Ik_ and let **x** _k_ +1 := **x** _k_ + _α_ Δ **x**

12: **if** _αk_ has a blocking constraint _j_ **then** _Ik_ +1 := _Ik ∪{j}_

13: **else** _Ik_ +1 := _Ik_
14: **end** **if**

15: **end** **if**

16: **end** **for**


We say that the step length _α_ computed in (5.15) has a _blocking_ _constraint_,
_j_ _̸∈_ _I_, if



_<_ 1 _._
**D** _j_ Δ **x**



_α_ = min
_i̸∈I_
**D** _i_ Δ **x** _<_ 0



**d** _i −_ **D** _i_ Δ **x**



_−_ **D** _i_ Δ **x** = **[d]** _[j]_ _[−]_ **[D]** _[j]_ [Δ] **[x]**

**D** _i_ Δ **x** **D** _j_ Δ **x**



And we say that _α_ has no blocking constraints when



_α_ = 1 _<_ min
_i̸∈I_
**D** _i_ Δ **x** _<_ 0



**d** _i −_ **D** _i_ Δ **x**

_._
**D** _i_ Δ **x**



5.5.2 Interior-Point Methods



For notational convenience and without loss of generality we assume that the
problem of interest is in standard form (5.2).
As in the linear programming case (Section 2.7.3), interior-point methods
generate a sequence of iterates that satisfy **x** _,_ **s** _>_ **0** . Each iteration of the
algorithm aims to make progress towards satisfying _−_ **Qx** + **A** [T] **y** + **s** = **c**, **Ax** = **b** _,_
and _xisi_ = 0, with _i_ = 1 _, . . ., n._
As before we use the following notational convention: Given a vector **x** _∈_ R _[n]_,
let **X** _∈_ R _[n][×][n]_ denote the diagonal matrix defined by _Xii_ = _xi_, with _i_ = 1 _, . . ., n,_
and let **1** _∈_ R _[n]_ denote the vector whose components are all 1s. The optimality
conditions (5.8) can be restated as
⎡ ⎤ ⎡ ⎤



⎤



⎡



⎤




_−_ **Qx** + **A** [T] **y** + **s** _−_ **c**
⎣ **Ax** _−_ **b**
**XS1**



⎦ =



**0**
⎣ **0**
**0**



⎦ _,_ **x** _,_ **s** _≥_ **0** _._


**5.5** ***Algorithms** 83



Given _μ_ _>_ 0, let ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) be the solution to the following perturbed
version of the above optimality conditions:
⎡ ⎤ ⎡ ⎤



⎤



⎡



⎤




_−_ **Qx** + **A** [T] **y** + **s** _−_ **c**
⎣ **Ax** _−_ **b**
**XS1**



⎦ =



**0**
⎣ **0**
_μ_ **1**



⎦ _,_ **x** _,_ **s** _>_ **0** _._



The first condition above can be written as **r** _μ_ ( **x** _,_ **y** _,_ **s** ) = **0** for the _residual_ _vector_



⎤


⎦ _._



**r** _μ_ ( **x** _,_ **y** _,_ **s** ) :=



⎡

_−_ **Qx** + **A** [T] **y** + **s** _−_ **c**
⎣ **Ax** _−_ **b**
**XS1** _−_ _μ_ **1**



The _central_ _path_ is the set _{_ ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) : _μ >_ 0 _}_ . It is intuitively clear that
( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) converges to an optimal solution to both (5.2) and its dual.
This suggests the following algorithmic strategy. Suppose ( **x** _,_ **y** _,_ **s** ) is “near”
( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **s** ( _μ_ )) for some _μ_ _>_ 0. Use ( **x** _,_ **y** _,_ **s** ) to move to a better point
( **x** [+] _,_ **y** [+] _,_ **s** [+] ) “near” ( **x** ( _μ_ [+] ) _,_ **y** ( _μ_ [+] ) _,_ **s** ( _μ_ [+] )) for some _μ_ [+] _< μ_ .
It can be shown that if a point ( **x** _,_ **y** _,_ **s** ) is on the central path, then the
corresponding value of _μ_ satisfies **x** [T] **s** = _nμ._ Likewise, given **x** _,_ **s** _>_ **0**, define


_μ_ ( **x** _,_ **s** ) := **[x]** [T] **[s]**

_n_ _[.]_



To move from a current point ( **x** _,_ **y** _,_ **s** ) to a new point, we use the so-called
_Newton_ _step_ ; that is, the solution to the system of equations
⎡ ⎤ ⎡ ⎤ ⎡ ⎤



⎡



Δ **x**
⎣Δ **y**
Δ **s**



⎦ =



⎡




_−_ **Q** **A** [T] **I**
⎣ **A** **0** **0**
**S** **0** **X**



⎤


⎦



⎤



⎤



**c** + **Qx** _−_ **A** [T] **y** _−_ **s**
⎣ **b** _−_ **Ax**
_μ_ **1** _−_ **XS1**



⎦ _._ (5.16)



Algorithm 5.2 presents a template for an interior-point method.


**Algorithm** **5.2** Interior-point method for quadratic programming

1: choose **x** [0] _,_ **s** [0] _>_ 0

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve the Newton system (5.16) for ( **x** _,_ **y** _,_ **s** ) = ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ) and _μ_ :=
0 _._ 1 _μ_ ( **x** _[k]_ _,_ **s** _[k]_ )

4: choose a step length _α ∈_ (0 _,_ 1] and set ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) = ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ )+
_α_ (Δ **x** _,_ Δ **y** _,_ Δ **s** )

5: **end** **for**


The step length _α_ in step 4 should be chosen so that **x** _[k]_ [+1] _,_ **s** _[k]_ [+1] _>_ 0 and
the size of **r** _μ_ ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) is sufficiently smaller than **r** _μ_ ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ ). A linesearch procedure such as the one described in Algorithm 2.4 in Chapter 2 can
be used for choosing the step length _α_ .


84 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


**5.6** **Applications** **to** **Machine** **Learning**


We next discuss some iconic applications of quadratic programming to machine
learning. We must note that the literature on optimization models in machine
learning is vast and continues to grow at a rapid pace. For a more detailed
discussion on this timely subject, we refer the reader to the excellent textbooks
by Friedman et al. (2001), Sra et al. (2012), and Vapnik (2013).


5.6.1 Binary Classification and Support Vector Machines


Classification problems constitute an important class of problems in financial
mathematics that can be solved using optimization models and techniques. In a
classification problem we have a vector of features describing an entity and the
goal is to analyze these features to determine which class each entity belongs to,
among two (or more) classes. For example, the classes might be “growth stocks”
and “value stocks”, and the entities (stocks) may be described by a feature vector
that contains elements such as stock price, price–earnings ratio, growth rate for
the previous periods, growth estimates, etc.
Mathematical approaches to classification often start with a training exercise.
One is supplied with a list of entities, their feature vectors, and the classes they
belong to. From this information, one tries to extract a mathematical structure
for the entity classes so that additional entities can be classified using this
mathematical structure and their feature vectors. For two-class classification,
a hyperplane is probably the simplest mathematical structure that can be used
to separate the feature vectors of these two different classes. Of course, there
may not be any hyperplane that separates two sets of vectors. When such a
hyperplane exists, we say that the two sets can be linearly separated.
Consider feature vectors **a** _i_ _∈_ R _[n]_ for _i_ = 1 _, . . ., k_ 1 corresponding to class 1,
and vectors **b** _i_ _∈_ R _[n]_ for _i_ = 1 _, . . ., k_ 2 corresponding to class 2. If these two vector
sets can be linearly separated, a hyperplane **w** [T] **x** = _γ_ exists with **w** _∈_ R _[n]_ _, γ_ _∈_ R
such that


**w** [T] **a** _i_ _≥_ _γ,_ for _i_ = 1 _, . . ., k_ 1
**w** [T] **b** _i_ _≤_ _γ,_ for _i_ = 1 _, . . ., k_ 2 _._


To have a “strict” separation, we often prefer to obtain _w_ and _γ_ such that


**w** [T] **a** _i_ _≥_ _γ_ + 1 _,_ for _i_ = 1 _, . . ., k_ 1
**w** [T] **b** _i_ _≤_ _γ −_ 1 _,_ for _i_ = 1 _, . . ., k_ 2 _._


In this manner, we find two parallel lines ( **w** [T] **x** = _γ_ + 1 and **w** [T] **x** = _γ −_ 1) that
form the boundaries of the class 1 and class 2 portions of the vector space; see
Figure 5.6.
There may be several such parallel lines that separate the two classes. Which
one should one choose? A good criterion is to choose the lines that have the


**5.6** **Applications** **to** **Machine** **Learning** 85



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-97-0.png)







**Figure** **5.6** Linear separation of two classes of data points


largest margin (distance between the lines). In machine learning, this type of
classification model is known as a _support_ _vector_ _machine_ (Friedman et al., 2001;
Vapnik, 2013).


(i) Consider the following quadratic problem:



min _∥_ **w** _∥_ [2] 2
**w** _,γ_
**a** [T] _i_ **[w]** _≥_ _γ_ + 1 _,_ for _i_ = 1 _, . . ., k_ 1
**b** [T] _i_ **[w]** _≤_ _γ −_ 1 _,_ for _i_ = 1 _, . . ., k_ 2 _._



(5.17)



The objective function of this problem is equivalent to maximizing the
margin between the lines **w** [T] **x** = _γ_ + 1 and **w** [T] **x** = _γ −_ 1 (see Exercise 5.6).


(ii) The linear separation idea we presented above can be used even when
the two vector sets _{_ **a** _i}_ and _{_ **b** _i}_ are not linearly separable. (Note that
linearly inseparable sets will result in an infeasible problem in formulation
(5.17).) This is achieved by introducing a non-negative violation variable
for each constraint of (5.17). Then, one has two objectives: to minimize
the total of the constraint violations and to maximize the margin. One
can formulate a quadratic programming model that combines these two
objectives using an adjustable parameter that can be chosen in a way to
put more weight on violations or margin, depending on one’s preference (see
Exercise 5.7).


86 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


5.6.2 Ridge and Lasso Regression


Recall the regression problem described in Example 5.3, namely to estimate the
linear model


_Y_ = _**β**_ [T] _X_ + _ϵ,_


where _X_ and _Y_ are R _[p]_ -valued and R-valued random variables, by using some
_training_ _data_ ( **x** _i, yi_ ), with _i_ = 1 _, . . ., N_ .
We next discuss the case when _N_ _< p_ . This case poses a classical and modern
challenge in data science. Indeed, this kind of case is increasingly common
as modern technology facilitates the collection of data. The expression _high-_
_dimensional_ _problems_ in the data science literature (Friedman et al., 2001) is
often used to describe problems where _p_ _≫_ _N_ . Examples of high-dimensional
problems abound in computational biology and genomics, and other instances
will likely emerge. In those contexts _N_ corresponds to the number of individuals,
e.g., patients, in some study. Due to physical limitations, _N_ may only be of
the order of a few hundred. In contrast, the number of features _p_ that can be
gathered, e.g., gene measurements, could be of the order of tens of thousands.
When _p_ _<_ _N_ the _p × p_ matrix **X** [T] **X** has rank at most _N_ _<_ _p_ and thus the
least-squares approach


min 2
_**β**_ _[∥]_ **[X]** [T] _**[β]**_ _[ −]_ **[y]** _[∥]_ [2]


is inadequate because the optimality conditions lead to an underdetermined
system of equations


( **X** [T] **X** ) _**β**_ = **X** [T] **y** _._


We next describe two popular modifications to the ordinary least-squares
approach that aim to rectify this difficulty, namely _ridge_ _regression_ and _lasso_
_regression_ .
Ridge regression adds a quadratic penalty term to the objective function in
the least-squares model


min _∥_ **X** [T] _**β**_ _−_ **y** _∥_ [2] 2 [+] _[ λ][∥]_ _**[β]**_ _[∥]_ 2 [2] _[,]_ (5.18)
_**β**_


where _λ >_ 0 is a tuning parameter. The effect of the penalty term is to shrink the
regression coefficients towards zero. The magnitude of _λ_ determines the shrinking
effect. In the limit when _λ_ _→∞_ the solution to the ridge regression model is
_**β**_ = **0** . On the other hand, when _λ_ = 0 ridge regression and ordinary least
squares coincide.
The optimality conditions for (5.18) yield the following system of equations:


( **X** [T] **X** + _λ_ **I** ) _**β**_ _−_ **X** [T] **y** = **0** _._


Thus the solution to (5.18) is


_**β**_ = ( **X** [T] **X** + _λ_ **I** ) _[−]_ [1] **X** [T] **y** _._


**5.7** **Exercises** 87


On the other hand, the lasso regression model, proposed in a seminal paper
by Tibshirani (1996), adds a 1-norm penalty term to the objective function in
the least-squares model


min _∥_ **X** [T] _**β**_ _−_ **y** _∥_ [2] 2 [+] _[ λ][∥]_ _**[β]**_ _[∥]_ [1] _[,]_ (5.19)
_**β**_


where _λ_ _>_ 0 is a tuning parameter. The effect of the penalty term is again to
shrink the regression coefficients towards zero. However, the properties of the
1-norm have a far more interesting effect. The penalty term _λ∥_ _**β**_ _∥_ 1 makes some
of the regression coefficients be _equal_ _to_ zero. In particular, the solutions to the
lasso regression model (5.19) are typically sparse and the level of sparsity is
controlled by the tuning parameter _λ_ . Lasso regression can be formulated as a
quadratic program (see Exercise 5.9). Unlike ridge regression, there is no closedform formula for the solution to lasso regression.


**5.7** **Exercises**


**Exercise** **5.1** Assume **c** _∈_ R _[n]_ and **Q** _∈_ R _[n][×][n]_ is symmetric. Show that the
function

_f_ ( **x** ) = [1] 2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**


is convex if and only if **Q** is positive semidefinite.
Assume **c** _∈_ R _[n]_ and **Q** _∈_ R _[n][×][n]_ is symmetric and positive semidefinite but not
positive definite. Show that the problem


min **x** 21 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**


is either bounded or has infinitely many optimal solutions.


**Exercise** **5.2** Let **c** _∈_ R _[n]_ . Show that the solution to

min **x** 12 _[∥]_ **[x]** _[∥]_ 2 [2] _[−]_ **[c]** [T] **[x]**

s.t. **1** [T] **x** = 1
**x** _≥_ **0**


is


**x** = ( _λ_ **1** + **c** ) [+] _,_


where _λ ∈_ R is a suitable threshold value such that **1** [T] ( _λ_ **1** + **c** ) [+] = 1.


**Exercise** **5.3** Let **c** _,_ **d** _∈_ R _[n]_ . Assume **d** _>_ **0** and **D** = (Diag( **d** )). Show that the
solution to
min **x** 12 **[x]** [T] **[D]** _[−]_ [1] **[x]** _[ −]_ **[c]** [T] **[x]**

s.t. **1** [T] **x** = 1
**x** _≥_ **0**


88 **Quadratic** **Programming:** **Theory** **and** **Algorithms**


is


**x** = ( _λ_ **d** + **Dc** ) [+] _,_


where _λ ∈_ R is a suitable threshold value such that **1** [T] ( _λ_ **d** + **Dc** ) [+] = 1.


**Exercise** **5.4** Write a CVX MATLAB script that takes as inputs **c** _∈_ R _[n]_, **Q** _∈_
R _[n][×][n]_, **A** _∈_ R _[m][×][n]_, **b** _∈_ R _[m]_ and solves the optimization problem


min 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**
s.t. **Ax** = **b**
**x** _≥_ **0** _._


Test your script on instances generated as follows:


>> m=1, n=5, c=randn(n,1), Q=eye(n), A=ones(m,n), b=1;


and


>> m=1, n=5, c=randn(n,1), Q=diag(rand(n,1)), A=ones(m,n), b=1;


Are the results consistent with Exercises 5.2 and 5.3?


**Exercise** **5.5** Consider a quadratic program with non-negativity inequality
constraints only:

min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** (5.20)

s.t. **x** _≥_ **0** _._


There is some intuition behind the optimality conditions: at an optimal solution
the non-negativity constraints split into binding and non-binding constraints.
The former behave like equality constraints whereas the latter can be treated as
if they did not exist. Suppose _I_ _⊆{_ 1 _, . . ., n}_ is the set of binding constraints and
_J_ = _{_ 1 _, . . ., n} \ I_ . This reasoning suggests that we think of the problem


min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **x** _I_ = **0** _,_


whose optimality conditions are


( **Qx** + **c** ) _I_ _−_ **s** _I_ = **0**
( **Qx** + **c** ) _J_ = **0** (5.21)
**x** _I_ = **0** _._


Prove that this intuition is indeed correct.


**Exercise 5.6** Consider the quadratic problem (5.17) presented in Section 5.6.1.


(a) Show that the objective function of this problem is equivalent to maximizing
the margin between the lines **w** [T] **x** = _γ_ + 1 and **w** [T] **x** = _γ −_ 1.
(b) Write the optimality conditions for problem (5.17).
(c) Write the dual.


**5.7** **Exercises** 89


**Exercise** **5.7** The linear separation idea presented in Section 5.6.1 can be used
even when the two vector sets _{_ **a** _i}_ and _{_ **b** _i}_ are not linearly separable. This
is achieved by introducing a non-negative violation variable for each constraint
of (5.17). Then, one has two objectives: to minimize the total of the constraint
violations and to maximize the margin. Develop a quadratic programming model
that combines these two objectives using an adjustable parameter that can be
chosen in a way to put more weight on violations or margin, depending on one’s
preference.


**Exercise** **5.8** The classification problems discussed in the two previous exercises can also be formulated as linear programming problems, if one agrees to
use the 1-norm rather than the 2-norm of **w** in the objective function. Recall
that _∥_ **w** _∥_ 1 = [�] _i_ _[|][w][i][|]_ [.] [Show] [that] [if] [we] [replace] _[∥]_ **[w]** _[∥]_ [2] 2 [by] _[∥]_ **[w]** _[∥]_ [1] [in] [the] [objective]
function of (5.17), we can write the resulting problem as a linear program. Show
also that this new objective function is equivalent to maximizing the distance
between **w** [T] **x** = _γ_ + 1 and **w** [T] **x** = _γ −_ 1 if one measures the distance using the
_∞_ -norm _∥_ **g** _∥∞_ = max _i |gi|_ .


**Exercise** **5.9** Show that the lasso regression model (5.19) can be equivalently
formulated as
min **x** 12 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]**

s.t. **Dx** _≥_ **d**


for some suitable **Q** _,_ **c** _,_ **D** _,_ **d** .


## 6 Quadratic Programming Models: Mean–Variance Optimization

**6.1** **Portfolio** **Return**


Consider an investment environment where there is a universe of _n_ risky assets.
In the next few chapters we will be concerned with a _one-period_ model of the
problem of investing in these _n_ risky assets. Assume a portfolio must be selected

                                  - �T
at some initial time _t_ 0 and held until time _t_ . Let **v** 0 = _v_ 1 _,_ 0 _· · ·_ _vn,_ 0 and **v** =

      - �T
_v_ 1 _· · ·_ _vn_ denote the vectors of asset prices at times _t_ 0 and _t_ respectively.
The vector **v** 0 is known whereas **v** is a vector of random variables. A vector
**h** _∈_ R _[n]_ of share holdings in each of the assets defines a portfolio whose values at
time _t_ 0 and _t_ are _W_ 0 := **v** 0 [T] **[h]** [ and] _[ W]_ [:=] **[ v]** [T] **[h]** [ respectively. The value] _[ W]_ [0] [is known]
at time _t_ 0 whereas _W_ is a random variable. The gist of portfolio construction is
to choose **h** to optimize some measure of satisfaction on the random variable _W_ .
It is customary to use the initial portfolio value _W_ 0 as a reference and to write
the above problem in terms of the portfolio return


_[−]_ _[W]_ [0]
_rP_ = _[W]_ _._

_W_ 0


The return of asset _i_, which is the same as that of a portfolio entirely invested
in asset _i_, is similarly defined as

_ri_ = _[v][i][ −]_ _[v][i,]_ [0] _._

_vi,_ 0


Instead of the vector of holdings **h** _∈_ R _[n]_, the portfolio construction problem is
often stated in terms of percentage holdings **x** _∈_ R _[n]_ where

_xi_ = _[h]_ _W_ _[i][v][i,]_ 0 [0] = ~~�~~ _njh_ =1 _iv_ _[h]_ _i,_ _[j]_ 0 _[v][j,]_ [0] _._


Observe that _W_ = **v** [T] **h** can be equivalently written as



_rP_ =




- _n_

_rixi_ = **r** [T] **x** _._

_i_ =1



In spite of its wide popularity, this convention runs into difficulties in some
cases. For example, the above quantity _rP_ does not make sense for a long–short
portfolio associated with a pairs trading strategy. More broadly, the quantity _rP_
does not make sense for a situation where the initial value of a portfolio _W_ 0 is


**6.2** **Markowitz** **Mean–Variance** **(Basic** **Model)** 91


zero as when one enters a futures contract or constructs a long–short portfolio
with equal long and short cash positions.
As Meucci (2005, 2010) nicely puts it, this difficulty can be amended by
assuming that returns are measured relative to some predefined _basis_ _value_ _b_ as
opposed to the initial portfolio value _W_ 0. In some cases, it is natural to choose
_b_ = _W_ 0 but it is more proper to think of _b_ as a general reference point. To make
this idea more precise, we associate with each asset and portfolio a basis _b_ that
satisfies the following four properties:


_•_ The basis _b_ for a long position of an asset is positive.

_•_ The basis _b_ is measured in the same unit as the asset values.

_•_ The basis is homogeneous: the basis of _k_ shares of an asset is _k_ times the basis
of one share.

_•_ The basis is known at time _t_ 0.


Equipped with this concept, we get a formal and unambiguous definition of asset
and portfolio returns:




_[v][i,]_ [0] _[−]_ _[W]_ [0]

_,_ _rP_ = _[W]_
_bi_ _bP_



_ri_ = _[v][i][ −]_ _[v][i,]_ [0]



_._
_bP_



Likewise, we obtain a formal and unambiguous definition of percentage holdings:


_xi_ = _[h][i][b][i]_ _._

_bP_


Once again, the identity _W_ = **v** [T] **h** can be equivalently written as


_rP_ = **r** [T] **x** _._

                       - �T
Throughout this chapter **x** = _x_ 1 _· · ·_ _xn_ will denote the vector of percentage holdings of a portfolio in a universe of _n_ risky assets. When it is applicable
and evident from the context, we shall assume the usual basis values _bi_ = _vi,_ 0
and _bP_ = _W_ 0 respectively.


**6.2** **Markowitz** **Mean–Variance** **(Basic** **Model)**


Markowitz’s key insight into the above one-period investment problem was to
consider the expected value and standard deviation of the return as measures of
performance and risk respectively. The portfolio selection problem can then be
formally stated as a quadratic programming model. To simplify our discussion
of this model, we will proceed in three incremental steps. First, we will look at
the case when there are only two assets; second, we will look at the case when
there are three risky assets; and finally, we will see the general case with any
number of risky assets.


92 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


Two Assets


Suppose we are combining two assets whose random returns are _r_ 1 and _r_ 2. Let


_μ_ 1 := E( _r_ 1) _,_ _μ_ 2 := E( _r_ 2) _,_


and

_σ_ 1 [2] [:= var(] _[r]_ [1][)] _[,]_ _σ_ 2 [2] [= var(] _[r]_ [2][)] _[,]_ _σ_ 12 = cov( _r_ 1 _, r_ 2) = _ρ · σ_ 1 _· σ_ 2 _._


In this case a _portfolio_ of these two assets is determined by the proportion
invested in one of the two assets. Let _x_ denote the proportion in asset 1. Thus
the portfolio return is


_rP_ = _x · r_ 1 + (1 _−_ _x_ ) _· r_ 2 _,_


the portfolio expected return is


_μP_ := E( _rP_ ) = _x ·_ E( _r_ 1) + (1 _−_ _x_ ) _·_ E( _r_ 2)
= _x · μ_ 1 + (1 _−_ _x_ ) _· μ_ 2 _,_


and the portfolio variance is


_σP_ [2] [=] _[ x]_ [2] _[σ]_ 1 [2] [+ (1] _[ −]_ _[x]_ [)][2] _[σ]_ 2 [2] [+ 2] _[ ·][ x]_ [(1] _[ −]_ _[x]_ [)] _[ ·][ ρ][ ·][ σ]_ [1] _[·][ σ]_ [2] _[.]_


In the special case when one of the assets, say asset 2, is the asset with risk-free
return _rf_ we get


_μP_ = _x · μ_ 1 + (1 _−_ _x_ ) _· rf_ = _rf_ + ( _μ_ 1 _−_ _rf_ ) _x,_ _σP_ [2] [=] _[ x]_ [2] _[σ]_ 1 [2] _[.]_


In this case the portfolio selection is particularly simple: a target level of expected
return _μP_ corresponds to one particular portfolio obtained by choosing _x_ =
( _μP_ _−_ _rf_ ) _/_ ( _μ_ 1 _−_ _rf_ ). The situation with three assets leads to a more interesting
situation.


Three Risky Assets


Suppose now that there are three assets with random returns _r_ 1 _, r_ 2 _,_ and _r_ 3. As
before, let

_μj_ = E( _rj_ ) _,_ _σj_ [2] [:= var(] _[r][j]_ [)] for _j_ = 1 _,_ 2 _,_ 3 _,_


and


_σij_ := cov( _ri, rj_ ) = _ρij_ _· σi · σj_ for _i, j_ = 1 _,_ 2 _,_ 3 _._


Now a portfolio determines the holdings in the three assets. Let _xj_ denote
the proportion (weight) invested in asset _j_, for _j_ = 1 _,_ 2 _,_ 3 _._ Notice that these
proportions should add up to one if the portfolio is fully invested in the three
assets:


_x_ 1 + _x_ 2 + _x_ 3 = 1 _._


Similar to what we did before, the portfolio return is


_rP_ = _r_ 1 _x_ 1 + _r_ 2 _x_ 2 + _r_ 3 _x_ 3 _._


**6.2** **Markowitz** **Mean–Variance** **(Basic** **Model)** 93


So the portfolio expected return is


_μP_ = _μ_ 1 _x_ 1 + _μ_ 2 _x_ 2 + _μ_ 3 _x_ 3 _,_


and the portfolio variance is


_σP_ [2] [=] _[ σ]_ 1 [2] _[x]_ [2] 1 [+] _[ σ]_ 2 [2] _[x]_ [2] 2 [+] _[ σ]_ 3 [2] _[x]_ [2] 3 [+ 2(] _[σ]_ [12] _[x]_ [1] _[x]_ [2] [+] _[ σ]_ [23] _[x]_ [2] _[x]_ [3] [+] _[ σ]_ [13] _[x]_ [1] _[x]_ [3][)] _[.]_


Observe that now there are multiple portfolios that can achieve a target expected
level of return. A portfolio is _efficient_ if it has minimum risk for a given target
return, or equivalently, if it has the maximum expected return for a given target
risk. This naturally leads to the following quadratic programming formulation.
To find a portfolio of minimum risk (variance) with expected return _at_ _least_ _μ_ ¯
solve the following _mean–variance_ _optimization_ _model_ :



�3


_i_ =1



�3

_σijxixj_

_j_ = _i_ +1



min
**x**



�3

_σiix_ [2] _i_ [+ 2]
_i_ =1



s.t. _μ_ 1 _x_ 1 + _μ_ 2 _x_ 2 + _μ_ 3 _x_ 3 _≥_ _μ_ ¯
_x_ 1 + _x_ 2 + _x_ 3 = 1 _._


The _efficient frontier_ is the set of efficient portfolios. The efficient frontier is often
“visualized” by plotting the expected return against the standard deviation of
the efficient portfolios. To generate portfolios on the efficient frontier, we can
minimize variance, for varying target return _μ_ ¯:



�3


_i_ =1



�3

_σijxixj_

_j_ = _i_ +1



min
**x**



�3

_σiix_ [2] _i_ [+ 2]
_i_ =1



s.t. _μ_ 1 _x_ 1 + _μ_ 2 _x_ 2 + _μ_ 3 _x_ 3 _≥_ _μ_ ¯
_x_ 1 + _x_ 2 + _x_ 3 = 1 _._


We can also maximize return, for varying target variance _σ_ ¯ [2] _>_ 0:


max _μ_ 1 _x_ 1 + _μ_ 2 _x_ 2 + _μ_ 3 _x_ 3
**x**



�3

_σijxixj_ _≤_ _σ_ ¯ [2]

_j_ = _i_ +1



s.t.



�3 �3

_σiix_ [2] _i_ [+ 2]
_i_ =1 _i_ =1



_x_ 1 + _x_ 2 + _x_ 3 = 1 _._


Or we can maximize quadratic _utility_, for varying risk aversion _γ_ _>_ 0:



�� [3]

_σiix_ [2] _i_ [+ 2]
_i_ =1



�3


_i_ =1



�3 
_σijxixj_

_j_ = _i_ +1



max _μ_ 1 _x_ 1 + _μ_ 2 _x_ 2 + _μ_ 3 _x_ 3 _−_ _[γ]_
**x** 2



max _μ_ 1 _x_ 1 + _μ_ 2 _x_ 2 + _μ_ 3 _x_ 3 _−_ _[γ]_
**x** 2



s.t. _x_ 1 + _x_ 2 + _x_ 3 = 1 _._


Any Number of Risky Assets


Let us now take a leap to the most general case. Assume we have _n_ risky assets.
Let **r** _∈_ R _[n]_ be the _n_ -dimensional random vector of returns, i.e., _ri_ denotes the


94 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


return of asset _i_ between times _t_ 0 and _t_ . Let _**μ**_ _∈_ R _[n]_ denote the vector of expected
returns, and **V** _∈_ R _[n][×][n]_ denote the return covariance matrix. More precisely,



_μ_ 1
...
_μn_



⎡

_σ_ 11 _· · ·_ _σ_ 1 _n_

⎢⎣ ... ... ...

_σn_ 1 _· · ·_ _σnn_



⎤

⎥⎦ _,_



⎤

⎥⎦ _,_ **V** =



_**μ**_ =



⎡

⎢⎣



where _μi_ := E( _ri_ ) _,_ _σij_ := cov( _ri, rj_ ) _,_ _i, j_ = 1 _, . . ., n._
From the linearity properties of expectation, it follows that the expected return

                     - �T
and variance of a given portfolio **x** = _x_ 1 _· · ·_ _xn_ of the risky assets are
respectively



_**μ**_ [T] **x** =




- _n_

_μjxj_

_j_ =1



and




- _n_

_σijxixj_ =

_j_ =1




- _n_

_σiix_ [2] _i_ [+ 2]
_i_ =1




- _n_


_i_ =1




- _n_

_σijxixj._

_j_ = _i_ +1



**x** [T] **Vx** =




- _n_


_i_ =1



The problem of selecting a portfolio can be formally stated as a tradeoff between
these two components. A fully invested portfolio is _efficient_ if it has minimum
risk for a given level of return, or equivalently if it has maximum expected return
for a given level of risk.
A fully invested efficient portfolio can then be characterized as the solution to
the following quadratic program:



max **x** _**μ**_ [T] **x** _−_ [1] 2




[1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**



(6.1)
**1** [T] **x** = 1



for some risk-aversion coefficient _γ_ _>_ 0.
The set of efficient portfolios can also be obtained as the set of solutions to
the quadratic program:

min **x** [T] **Vx**
**x**

s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯ (6.2)
**1** [T] **x** = 1 _,_


and also as the set of solutions to



max _**μ**_ [T] **x**
**x**



**x** [T] **Vx** _≤_ _σ_ ¯ [2] (6.3)

**1** [T] **x** = 1



s.t. **x** [T] **Vx** _≤_ _σ_ ¯ [2]



by varying _μ_ ¯ and _σ_ ¯ respectively. The exercises at the end of the chapter sketch
how to give a formal proof of the equivalence of the above three models.
We shall refer to the equivalent mean–variance models (6.1), (6.2), and (6.3) as
the _basic mean–variance models_ as they include only the following three essential
components: mean and variance of return, and the full investment constraint.
Observe that these three optimization models are convex because the quadratic
function **x** _�→_ **x** [T] **Vx** is convex as the covariance matrix **V** is positive semidefinite.


**6.3** **Analytical** **Solutions** **to** **Basic** **Mean–Variance** **Models** 95


Section 6.3 below details several interesting insights that can be gained from the
solution to these basic mean–variance models.
As we discuss later in this chapter, the types of mean–variance models used
in portfolio construction typically include a number of additional constraints.


Asset Allocation and Security Selection


There are two distinct levels of portfolio analysis that are amenable to mean–
variance models. The conventional _top-down_ investment approach to portfolio
construction consists of two main steps, namely _asset_ _allocation_ and _security_
_selection_ .
On the one hand, the _asset_ _allocation_ decision is concerned with portfolio
choices among broad asset classes. At the coarsest level, these asset classes could
be stocks, bonds, and cash. At a more refined level, some of these broad asset
classes could be subdivided. For instance, stocks can be divided according to
geography or market capitalization. The asset allocation decision involves only
a small number of assets, typically ranging from a handful to a dozen or so. It
generally involves simple constraints such as budget constraints and upper and
lower bounds on individual positions.
On the other hand, the _security selection_ decision is concerned with the specific
securities within each particular asset class. For instance, if the relevant asset
class is equities in the S&P 500 market index, then the security selection problem
is concerned with the specific portfolio holdings at the individual stock level.
The security selection problem typically involves a large number of securities,
ranging from a few hundred to potentially thousands. It also involves a myriad
of constraints and is often formulated relative to a predefined _benchmark,_ as we
discuss in more detail in Section 6.5.


**6.3** **Analytical** **Solutions** **to** **Basic** **Mean–Variance** **Models**


The solution to the basic mean–variance models described in Section 6.2 can
be characterized by relying on the tools introduced in Chapter 5. Throughout
this section we assume that the covariance matrix of asset returns **V** is positive
definite. In particular, **V** _[−]_ [1] exists.


Minimum Risk and Characteristic Portfolios


Consider the simplified version of (6.1) that is obtained in the limit when _γ_ _→∞_ :


min **x** [T] **Vx**
**x** (6.4)

**1** [T] **x** = 1 _._


96 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


The model (6.4) corresponds to the problem of finding the minimum-risk fully
invested portfolio. We discussed this problem in Example 5.7 where the optimal
solution was shown to be


1
**x** _[∗]_ =
**1** [T] **V** _[−]_ [1] **1** **[V]** _[−]_ [1] **[1]** _[.]_


A related problem that is often of interest is to find the minimum-risk portfolio
with unit exposure to a vector of _attributes_ **a** associated with the assets. As
we will see later, some interesting attributes could be the betas of the assets
relative to a benchmark, the asset volatilities, or the asset expected returns. The
_characteristic_ _portfolio_ of a vector of attributes **a** is the solution to the problem


min **x** [T] **Vx**
**x** (6.5)

**a** [T] **x** = 1 _._


Using the solution of (5.9) obtained in Chapter 5, it follows that the solution to
(6.5) is


1
**x** _[∗]_ =
**a** [T] **V** _[−]_ [1] **a** **[V]** _[−]_ [1] **[a]** _[.]_

Observe that a characteristic portfolio **x** _[∗]_ = (1 _/_ **a** [T] **V** _[−]_ [1] **a** ) **V** _[−]_ [1] **a** is not necessarily
fully invested as its components may not necessarily add up to one. Observe that
the variance of the characteristic porfolio **x** _[∗]_ = (1 _/_ **a** [T] **V** _[−]_ [1] **a** ) **V** _[−]_ [1] **a** is


1
( **x** _[∗]_ ) [T] **Vx** _[∗]_ =
**a** [T] **V** _[−]_ [1] **a** _[.]_


Two-Fund Separation Theorem


Consider the basic mean–variance model



max **x** _**μ**_ [T] **x** _−_ [1] 2




[1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**



(6.6)
**1** [T] **x** = 1



for some risk-aversion coefficient _γ_ _>_ 0. We next derive an interesting result
often called the _two-fund separation theorem_ . The theorem states that every fully
invested efficient portfolio is a combination of two particular efficient portfolios.
Applying the optimality conditions (5.10) from Theorem 5.6 to problem (6.6)
we obtain the solution


1 1
**x** _[∗]_ = _λ ·_
**1** [T] **V** _[−]_ [1] _**μ**_ **[V]** _[−]_ [1] _**[μ]**_ [ + (1] _[ −]_ _[λ]_ [)] _[ ·]_ **1** [T] **V** _[−]_ [1] **1** **[V]** _[−]_ [1] **[1]**


where _λ_ = **1** [T] **V** _[−]_ [1] _**μ**_ _/γ_ . The following _two-fund_ _theorem_ readily follows.


**Theorem 6.1** (Two-fund theorem) _Consider model_ (6.6) _for some γ_ _>_ 0 _. There_
_exist_ _two_ _efficient_ _portfolios_ _(funds),_ _namely_


1 1

_[and]_
**1** [T] **V** _[−]_ [1] _**μ**_ **[V]** _[−]_ [1] _**[μ]**_ **1** [T] **V** _[−]_ [1] **1** **[V]** _[−]_ [1] **[1]** _[,]_


**6.3** **Analytical** **Solutions** **to** **Basic** **Mean–Variance** **Models** 97


_such_ _that_ _every_ _efficient_ _portfolio,_ _that_ _is,_ _every_ _solution_ _to_ (6.6) _,_ _is_ _a_ _combina-_
_tion_ _of_ _these_ _two_ _portfolios._


Observe that one of the two portfolios in the two-fund theorem is the minimumrisk portfolio (1 _/_ **1** [T] **V** _[−]_ [1] **1** ) **V** _[−]_ [1] **1** and the other one is a multiple of the characteristic portfolio (1 _/_ _**μ**_ [T] **V** _[−]_ [1] _**μ**_ ) **V** _[−]_ [1] _**μ**_ of the vector of attributes _**μ**_ .


One-Fund Separation Theorem


We next derive the _one-fund_ or _mutual_ _fund_ separation theorem. This result is
similar in spirit to the two-fund separation theorem. It states that if there is a
risk-free asset, then every efficient portfolio is a combination of the risk-free asset
and a particular fund.
Consider the case when, in addition to the universe of _n_ risky assets, there
is an additional asset _n_ + 1 with risk-free return _rf_ . In this case, problem (6.1)
extends as follows



**x** max _,xn_ +1 _**μ**_ [T] **x** + _rf_ _· xn_ +1 _−_ [1] 2




[1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**



(6.7)
**1** [T] **x** + _xn_ +1 = 1 _._



By substituting _xn_ +1 = 1 _−_ **1** [T] **x** in the objective and dropping the constraint,
problem (6.7) can be rewritten as the following unconstrained optimization
problem:

max **x** ( _**μ**_ _−_ _rf_ **1** ) [T] **x** _−_ [1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]** _[.]_


Applying the optimality conditions (5.4) from Theorem 5.2, we obtain the following solution to (6.7):


1

**x** _[∗]_ = _γ_ [1] _[·]_ **[ V]** _[−]_ [1][(] _**[μ]**_ _[ −]_ _[r][f]_ **[1]** [) =] _[ λ][ ·]_ **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) **[V]** _[−]_ [1][(] _**[μ]**_ _[ −]_ _[r][f]_ **[1]** [)] _[,]_ _[x][∗]_ _n_ +1 [= 1] _[ −]_ **[1]** [T] **[x]** _[∗][,]_


where _λ_ = **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) _/γ_ . The following _one-fund_ _theorem_ readily follows.


**Theorem** **6.2** (One-fund theorem) _Suppose_ _the_ _investment_ _universe_ _includes_
_n_ _risky_ _assets_ _and_ _a_ _risk-free_ _asset._ _Then_ _there_ _exists_ _a_ _fully_ _invested_ _efficient_
_portfolio_ _(fund)_ _namely_


1
**1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) **[V]** _[−]_ [1][(] _**[μ]**_ _[ −]_ _[r][f]_ **[1]** [)]


_such that every efficient portfolio – that is, every solution to_ (6.7) _for some γ_ _>_ 0

_–_ _is_ _a_ _combination_ _of_ _this_ _portfolio_ _and_ _the_ _risk-free_ _asset._


The portfolio [1 _/_ **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** )] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) is called the _tangency_ _port-_
_folio_ . This name is motivated by the geometric interpretation illustrated in
Figure 6.1. Consider the plot of expected return versus standard deviation for
the efficient frontier portfolios. The portfolio [1 _/_ **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** )] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** )
lies exactly at the tangency point on this frontier defined by the straight line


98 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


emerging from the point (0 _, rf_ ). The point (0 _, rf_ ) corresponds to the expected
return versus standard deviation of the risk-free asset. The tangency line is also
known as the _capital_ _allocation_ _line_ (CAL) as it corresponds to portfolios with
different allocations of capital between the tangency portfolio and the risk-free
asset.


_rf_


0


**Figure** **6.1** Tangency portfolio


Capital Asset Pricing Model (CAPM)


Under suitable equilibrium assumptions the tangency portfolio discussed above
yields the main mathematical foundation for the capital asset pricing model
(CAPM), a fundamental asset pricing model in financial economics. The key
step in this derivation is that, in equilibrium, the tangency portfolio is precisely
the market portfolio **x** _M_ . That is,


1
**x** _M_ = **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) **[V]** _[−]_ [1][(] _**[μ]**_ _[ −]_ _[r][f]_ **[1]** [)] _[.]_ (6.8)


From (6.8) we readily obtain


1
**Vx** _M_ = **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) [(] _**[μ]**_ _[ −]_ _[r][f]_ **[1]** [)] _[,]_ (6.9)


and

( _**μ**_ _−_ _rf_ **1** ) [T] **x** _M_ _μM_ _−_ _rf_
**x** [T] _M_ **[Vx]** _[M]_ [=] **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) [=] **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) _[,]_ (6.10)


where _μM_ = _**μ**_ [T] **x** _M_ is the expected value of the market portfolio return.
Combining (6.9) and (6.10) we get



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-110-0.png)


           1
_**μ**_ _−_ _rf_ **1** = **1** [T] **V** _[−]_ [1] ( _**μ**_ _−_ _rf_ **1** ) **Vx** _M_ = **Vx** _M_
**x** [T] _M_ **[Vx]** _[M]_




( _μM −_ _rf_ ) = _**β**_ _·_ ( _μM −_ _rf_ ) _,_


(6.11)


**6.4** **More** **General** **Mean–Variance** **Models** 99


where _**β**_ = (1 _/_ **x** [T] _M_ **[Vx]** _[M]_ [)] **[Vx]** _[M]_ [.] [The] [above] [can] [be] [equivalently] [stated] [as]

_μj_ _−_ _rf_ = _βj_ ( _μM_ _−_ _rf_ ) _,_ where _βj_ = _[σ][j,M]_ for _j_ = 1 _, . . ., n._ (6.12)

_σM_ [2]


Equation (6.11) or its equivalent (6.12) is the formal statement of the capital
asset pricing model (CAPM). The CAPM postulates that the excess return of
asset _j_ is determined entirely by its beta coefficient times the excess return of
the market.
In the expression (6.12), _σj,M_ denotes the covariance between the return of
asset _j_ and the return of the market portfolio, and _σM_ [2] [denotes] [the] [variance] [of]
the market portfolio return. The last two quantities in turn have the following
expressions in terms of the covariance matrix **V** :


_σj,M_ = cov( _rj, rM_ ) = ( **Vx** _M_ ) _j,_ _σM_ [2] [= var(] _[r][M]_ [) =] **[ x]** _M_ [T] **[Vx]** _[M]_ _[.]_


**6.4** **More** **General** **Mean–Variance** **Models**


The basic mean–variance model discussed in the previous section provides the
foundation of modern portfolio theory. However, when mean–variance models
are used as a normative tool in portfolio construction, it is common to use
modifications of the basic model by including additional constraints and possibly
additional terms in the objective.


Common Constraints


Aside from a target expected return or a target variance, the only portfolio
constraint in the basic mean–variance model is the full investment constraint


**1** [T] **x** = 1 _._


Furthermore, this constraint disappears if the portfolio is allowed to include
holdings in a risk-free asset. In both cases the individual portfolio holdings could
in principle take arbitrary positive and negative values as there is no explicit
restriction on them. This motivates the following types of constraints that are
often included in a mean–variance model:


_•_ Budget constraints, such as fully invested portfolios.

_•_ Upper and/or lower bounds on the size of individual positions.

_•_ Upper and/or lower bounds on exposure to industries or sectors.

_•_ Leverage constraints such as long-only, or 130/30 constraints.

_•_ Turnover constraints.


The above types of constraints replace the single portfolio constraint


**1** [T] **x** = 1


100 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


by a more elaborate set of constraints of the form


**Ax** = **b**
**Dx** _≥_ **d** _._


Consequently, we get the following general version of the basic mean–variance
model (6.1):



max **x** _**μ**_ [T] **x** _−_ [1] 2




[1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**



**Ax** = **b** (6.13)
**Dx** _≥_ **d** _._



The set of portfolios obtained via the model (6.13) can also be obtained via the
following two equivalent models. The first one enforces a target expected return:


min **x** [T] **Vx**
**x**



s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯
**Ax** = **b**
**Dx** _≥_ **d** _._


The second one enforces a target variance of return:


max _**μ**_ [T] **x**
**x**

s.t. **x** [T] **Vx** _≤_ _σ_ ¯ [2]

**Ax** = **b**
**Dx** _≥_ **d** _._



(6.14)


(6.15)



The models (6.13), (6.14), and (6.15) are still convex quadratic optimization
models. Unlike the basic mean–variance model, they generally do not have an
analytical closed-form solution due to the additional inequality constraints. However, they can be solved numerically very efficiently via optimization solvers.
We next discuss how some of the above five types of constraints can be
incorporated into a mean–variance model. The first three types of constraints
have straightforward formulations. We concentrate on the last two, namely,
leverage constraints and turnover constraints. A long-only constraint can readily
be enforced via **x** _≥_ 0. A relaxed version of this constraint, popular in certain
contexts, is not to rule out leverage altogether but to limit it. For instance, a
“130/30” leverage constraint means that the total value of the holdings in short
positions must be at most 30% of the portfolio value. In general, suppose that
we want the value of the total short positions to be at most _L_ . This means that
we want to enforce the following restriction:




- _n_

min( _xj,_ 0) _≥−L_ _⇔_

_j_ =1




- _n_

max( _−xj,_ 0) _≤_ _L._

_j_ =1



Although this is a correct mathematical formulation of the constraint, it is not
ideal for computational purposes because of the non-smooth terms max( _−xj,_ 0).


**6.4** **More** **General** **Mean–Variance** **Models** 101


In particular, if a constraint were written in this form the resulting mean–
variance model would not be a quadratic program. To formulate this constraint
efficiently in the quadratic optimization model, we trade terms of the form
max( _−xj,_ 0) for new terms involving possibly new variables� and linear inequal-�T

ities. To that end, add the new vector of variables **y** = _y_ 1 _· · ·_ _yn_ and
constraints


**x** _≥−_ **y**

     - _n_

_yj_ _≤_ _L_

_j_ =1


**y** _≥_ **0** _._


A _turnover_ constraint is a constraint on the total change in the portfolio
positions. This constraint is generally included as a way to limit certain kinds
of costs such as taxes and transaction costs. Suppose that we have an initial

         - �T
portfolio **x** [0] = _x_ [0] 1 _· · ·_ _x_ [0] _n_ and we want to ensure that the new portfolio
incurs a total turnover no larger than _h_ . This means that we want to enforce the
restriction

     - _n_

_|x_ [0] _j_ _[−]_ _[x][j][| ≤]_ _[h.]_
_j_ =1


To formulate this constraint efficiently in the quadratic optimization model, add

                 - �T
the new vector of variables **y** = _y_ 1 _· · ·_ _yn_ and constraints


_xj_ _−_ _x_ [0] _j_ _[≤]_ _[y][j]_


_x_ [0] _j_ _[−]_ _[x][j]_ _[≤]_ _[y][j]_

      - _n_

_yj_ _≤_ _h_

_j_ =1



(see Exercise 6.3). The total turnover


_two-sided_ turnover.


Maximizing the Sharpe Ratio




- _n_

_|x_ [0] _j_ _[−]_ _[x][j][|]_ [is] [also] [sometimes] [called] [the]
_j_ =1



The three equivalent mean–variance models (6.13), (6.14), and (6.15) define a
frontier of efficient portfolios. These portfolios are determined by some optimal
tradeoff of expected return and variance, or equivalently, standard deviation of
return. The ratio of expected return to standard deviation, called _Sharpe_ _ratio_
or _reward-to-risk_ _ratio,_ singles out the efficient portfolio that offers the highest
reward per measure of risk.


102 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


**Definition** **6.3** (Sharpe ratio) _The_ Sharpe ratio _of_ _a_ _given_ _portfolio_ **x** =

      - �T
_x_ 1 _· · ·_ _xn_ _is_ _the_ _ratio_ _of_ _its_ _expected_ _return_ _to_ _its_ _volatility_ _(standard_
_deviation)_ _of_ _return:_


_**μ**_ [T] **x**
_Sharpe_ _ratio_ := ~~_√_~~ _._

**x** [T] **Vx**


As we further elaborate in the next sections, sometimes _**μ**_ may not necessarily
stand for the vector of expected _absolute_ returns but instead it may make sense
for _**μ**_ to stand for the vector of expected _relative_ returns. In particular, if there is
a risk-free asset, in the above definition of the Sharpe ratio it is usual to assume
that _**μ**_ stands for the vector of expected _excess_ returns. The _excess_ _return_ of an
asset is simply the difference of its return and the risk-free return.
As an alternative or a complement to the equivalent mean–variance models (6.13), (6.14), and (6.15), consider the problem of finding the efficient portfolio
with maximum Sharpe ratio. The natural formulation for this problem is the
following:



_**μ**_ [T] **x**
max ~~_√_~~
**x** **x** [T] **Vx**

s.t. **Ax** = **b**
**Dx** _≥_ **d** _._



(6.16)



This natural formulation is evidently not a quadratic optimization model. Furthermore, the formulation is not convex as the objective function is not convex.
We next show that this problem can be recast as a quadratic convex optimization
problem via a suitable _homogenization_ . To this end, make the following mild
assumptions:


_•_ There is a feasible portfolio **x** such that _**μ**_ [T] **x** _>_ 0.


_•_ The matrices **A** _,_ **D** and vector _**μ**_ satisfy the following technical condition:


**Az** = **0** _,_ **Dz** _≥_ **0** _⇒_ _**μ**_ [T] **z** _≤_ 0 _._


The latter condition readily holds when the following stronger but easier
to verify condition holds:


**Az** = **0** _,_ **Dz** _≥_ **0** _⇒_ **z** = **0** _._


The above assumptions ensure the soundness of the approach described next. To
see what goes wrong when these assumptions do not hold, see the exercises at
the end of the chapter.
The gist of the reformulation of (6.16) as a quadratic optimization problem
is the following _homogenization_ . Consider the change of variables obtained by
putting **z** := _κ_ **x** _,_ where _κ_ _>_ 0 is a new scalar variable. The problem (6.16) can


**6.5** **Portfolio** **Management** **Relative** **to** **a** **Benchmark** 103


be rewritten as



_**μ**_ [T] **z**
max ~~_√_~~
**z** _,κ_ [T]



**z** _,κ_ **z** [T] **Vz**

s.t. **A** **[z]** [=] **[ b]**



(6.17)



_κ_ [=] **[ b]**

**[z]**

_κ_ _[≥]_ **[d]**



**D** **[z]**



_κ >_ 0 _._



The assumption _**μ**_ [T] **x** _>_ 0 for some feasible **x** implies that we can choose _κ_ _>_ 0
such that _**μ**_ [T] **z** = 1. Using this together with the second assumption, it follows
that the problem (6.17) is equivalent to


min **z** [T] **Vz**
**z** _,κ_



s.t. _**μ**_ [T] **z** = 1
**Az** _−_ **b** _κ_ = **0**
**Dz** _−_ **d** _κ_ _≥_ **0**
_κ_ _≥_ 0 _._



(6.18)



As the exercises at the end of the chapter detail, this approach also yields the
following characterization of the portfolio with maximum Sharpe ratio in the
case when we only include the full investment constraint **1** [T] **x** = 1.


**Proposition** **6.4** _Suppose_ _the_ _minimum-risk_ _portfolio_ (1 _/_ **1** [T] **V** _[−]_ [1] **1** ) **V** _[−]_ [1] **1** _has_
_positive_ _expected_ _return;_ _that_ _is,_ _**μ**_ [T] **V** _[−]_ [1] **1** _>_ 0 _._ _Then_ _the_ _solution_ _to_ _the_ _following_
_maximum_ _Sharpe_ _ratio_ _problem_



_is_ _the_ _tangency_ _portfolio_



_**μ**_ [T] **x**
max ~~_√_~~
**x** **x** [T] **Vx** (6.19)

s.t. **1** [T] **x** = 1


1
**x** _[∗]_ =
**1** [T] **V** _[−]_ [1] _**μ**_ **[V]** _[−]_ [1] _**[μ]**_ _[.]_



**6.5** **Portfolio** **Management** **Relative** **to** **a** **Benchmark**


In an investment portfolio, the _security selection_ problem is concerned with determining the holdings of specific securities within a given asset class. It is customary
to manage and evaluate the portfolio of securities relative to some predefined
_benchmark_ _portfolio_ that represents a particular asset class. The benchmark
portfolio provides a reference point. It serves the role of the _market_ _portfolio_
if the investment universe is restricted to the particular asset class that the
benchmark represents. The management of a portfolio of securities relative to a
benchmark could be _passive_ or _active_ . The goal of the former is to replicate the
benchmark whereas the goal of the latter is to beat the benchmark.


104 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


Systematic (Beta) and Individual (Alpha) Returns


Both passive and active management rely on a fundamental decomposition of
individual securities return into _systematic_ and _individual_ (or _residual_ ) components. The former is the component of return that can be explained by the
security exposure to the benchmark. The latter is the component of return that
is idiosyncratic to the individual security.
To make the above decomposition more precise, assume the investment universe determined by a particular asset class includes _n_ individual securities. Let
_ri_ denote the excess return of security _i_ for _i_ = 1 _, . . ., n._ Let _rB_ denote the excess
return of the benchmark.
The return of security _i_ can be decomposed via the following linear regression
model:


_ri_ = _βirB_ + _θi,_


where _θi_ is the component of return uncorrelated to _rB_ ; that is, cov( _rB, θi_ ) = 0.
The coefficient _βi_ is the _beta_ of security _i_ relative to the benchmark _B_ and is
given by

_βi_ := [cov(] _[r][i][, r][B]_ [)]

var( _rB_ ) _[.]_


The term _βirB_ is the _systematic_ component of return of security _i_ . The term _θi_
is the _residual_ component of return of security _i_ . The _alpha_ of security _i_ is the
expected value of the residual return _θi_ :


_αi_ = E( _θi_ ) _._

                                       - �T
Consider a portfolio of securities with percentage holdings **x** = _x_ 1 _· · ·_ _xn_ .
The above type of decomposition also applies to the portfolio return


_rP_ := **r** [T] **x** = _r_ 1 _x_ 1 + _· · ·_ + _rnxn._


That is, we can decompose the portfolio return _rP_ as


_rP_ = _βP rB_ + _θP,_


where the systematic and residual components of the portfolio return are respectively

_βP rB_ = ( _**β**_ [T] **x** ) _rB_ = ( _β_ 1 _x_ 1 + _· · ·_ + _βnxn_ ) _rB_


and

_θP_ = _**θ**_ [T] **x** = _θ_ 1 _x_ 1 + _· · ·_ + _θnxn._


Furthermore, it is easy to see that the beta and alpha of the portfolio are
respectively

_βP_ = _**β**_ [T] **x** = _β_ 1 _x_ 1 + _· · ·_ + _βnxn_


and

_αP_ = E( _θP_ ) = _**α**_ [T] **x** = _α_ 1 _x_ 1 + _· · ·_ + _αnxn._


**6.5** **Portfolio** **Management** **Relative** **to** **a** **Benchmark** 105


Active Return, Tracking Error, Information Ratio

                           - �T
Consider a portfolio with percentage holdings **x** = _x_ 1 _· · ·_ _xn_ . The _active_
_return_ of the portfolio is the difference between the portfolio return and the
benchmark return:

**r** [T] **x** _−_ _rB._

                         -                         If the portfolio of benchmark holdings is **x** _[B]_ = _x_ _[B]_ 1 _· · ·_ _x_ _[B]_ _n_, then _rB_ = **r** [T] **x** _[B]_

and thus the active return can also be written as


**r** [T] **x** _−_ _rB_ = **r** [T] ( **x** _−_ **x** _[B]_ ) _._


The vector **x** _−_ **x** _[B]_ is the vector of _active_ _holdings_ of the portfolio.
The _active_ _risk_ or _tracking_ _error_ _ψ_ [2] of a portfolio is the standard deviation of
the portfolio active return. In other words,


_ψ_ [2] := var( **r** [T] ( **x** _−_ **x** _[B]_ )) _._


Some straightforward matrix calculations show that if **V** is the covariance matrix
of securities returns, then


_ψ_ [2] = var( **r** [T] ( **x** _−_ **x** _[B]_ )) = ( **x** _−_ **x** _[B]_ ) [T] **V** ( **x** _−_ **x** _[B]_ ) _._


A straightforward calculation also shows that the active risk can be decomposed
as

_ψ_ [2] = ( _βP_ _−_ 1) [2] _σB_ [2] [+] _[ ω]_ _P_ [2] _[,]_

where _σB_ [2] [=] [var(] _[r][B]_ [)] [and] _[ω]_ _P_ [2] [=] [var(] _[θ][P]_ [ ).] [The] [first] [term] [(] _[β][P]_ _[−]_ [1)][2] _[σ]_ _B_ [2] [is] [the]
component of active risk due to the _active_ _beta_ _βP_ _−_ 1 of the portfolio. The
second term _ωP_ [2] [is] [the] [portfolio] _[residual]_ _[risk]_ [.] [Observe] [that] [the] [active] [risk] [and]
residual risk are the same when _βP_ = 1.
The _information_ _ratio_ is a cousin of the Sharpe ratio defined in Section 6.2.


**Definition** **6.5** (Information ratio) The information ratio ( _IR_ ) of a portfolio
_P_ is the ratio of expected residual return to volatility (standard deviation) of
residual return:

_IRP_ := _[α][P]_ _._

_ωP_


Portfolio Optimization with Benchmark Considerations


The consideration of a benchmark in portfolio construction typically leads to
mean–variance models that include some adjustments and constraints induced
by the benchmark.
The following are some of the most common adjustments and constraints when
a mean–variance model is used for portfolio construction relative to a benchmark:


_•_ Use expected residual returns _**α**_ [T] **x** instead of expected total return _**μ**_ [T] **x** .

_•_ Use active risk _ψ_ [2] = ( **x** _−_ **x** _[B]_ ) [T] **V** ( **x** _−_ **x** _[B]_ ) instead of total risk **x** [T] **Vx** .


106 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


_•_ Bounds on the size of _active_ _positions_ . These adjustments and constraints are
typically of the form


_Li_ _≤_ _xi −_ _x_ _[B]_ _i_ _[≤]_ _[U][i][,]_ _[i]_ [ = 1] _[, . . ., n,]_


that restrict the deviations between the portfolio holdings and the benchmark holdings.

_•_ Bounds on the beta of the portfolio. Again this type of constraint is typically
of the form

_L ≤_ _**β**_ [T] **x** _−_ 1 _≤_ _U._


As an example, the optimization problem might be



max _**α**_ [T] **x**
**x**

s.t. ( **x** _−_ **x** _[B]_ ) [T] **V** ( **x** _−_ **x** _[B]_ ) _≤_ _ψ_ [¯][2]

**1** [T] **x** = 1
_L ≤_ _**β**_ [T] **x** _−_ 1 _≤_ _U._


**6.6** **Estimation** **of** **Inputs** **to** **Mean–Variance** **Models**



(6.20)



The estimation of input parameters, namely the covariance matrix of returns **V**
and the vector of total expected returns _**μ**_ or residual expected returns _**α**_, is one
of the most critical and challenging steps in the use of mean–variance models. We
next describe some of the central ideas that underlie most popular approaches
to this fundamental problem. A comprehensive treatment of this subject is well
beyond the scope of this book. Thus we only describe the key building blocks of
_factor_ _models._ We refer the reader to the textbooks of Grinold and Kahn (1999)
and Litterman (2003) and to the articles by Rosenberg (1974) and Ledoit and
Wolf (2003, 2004) as well as the references therein for further details on the
vast variety of techniques and approaches that can be used for estimating the
mean–variance input parameters **V** and _**μ**_ .
Throughout this section assume the investment universe has _n_ assets and let _ri_
denote the _excess_ _return_ of asset _i_ for _i_ = 1 _, . . ., n_ . Let **r** _∈_ R _[n]_ denote the vector
of excess returns. A rudimentary approach to estimate _**μ**_ and **V** via sample
means and sample covariances is based on historical data. More precisely, given
a time series of realized excess returns **r** (1) _,_ **r** (2) _, . . .,_ **r** ( _T_ ) _,_ the vectors of sample
means and sample covariance are respectively




- _T_

( **r** ( _t_ ) _−_ _**μ**_ ˆ )( **r** ( _t_ ) _−_ _**μ**_ ˆ ) [T] _._

_t_ =1



_**μ**_ ˆ := [1]

_T_




- _T_ 1

**r** ( _t_ ) _,_ **V** ˆ :=
_T_ _−_ 1
_t_ =1



The vector _**μ**_ ˆ and matrix **V** [ˆ] provide estimates of _**μ**_ and **V** . However, these
estimators have three major shortcomings:


_•_ The sample mean and sample covariance do not incorporate other data that
could contain useful forecasting information.


**6.6** **Estimation** **of** **Inputs** **to** **Mean–Variance** **Models** 107


_•_ For an investment universe with _n_ assets, there are a total of _n_ + [1] 2 _[n]_ [(] _[n]_ [ + 1)]
= 12 _[n]_ [(] _[n]_ [+] [3)] [different] [parameters] [to] [estimate.] [Although] [this] [could] [be]
manageable for a small asset allocation model, it is not viable for an
equity portfolio management model, as the number of securities _n_ in a
stock universe could easily range in the hundreds or thousands.

_•_ The sample mean and sample covariance inevitably contain a fair amount of
estimation errors, which, as we further explain in the next chapter, are
magnified by the mean–variance optimizer.


The first two shortcomings above can be largely mitigated by assuming some
kind of structure in the portfolio returns **r**, as the following subsections detail.
The next chapter is devoted entirely to the third shortcoming.


Single-Factor Model


The task of estimating a risk model can be drastically simplified by assuming
that each asset has two components of risk: market risk and residual risk. This is
a _single-factor_ _risk_ _model_ . Historically this model was introduced by Sharpe as
an intellectual precursor of the capital asset pricing model (CAPM). The model
assumes that excess returns are decomposed as in the following regression model:


_ri_ = _βirM_ + _θi._


Here _βi_ is the beta of asset _i_, and _θi_ is its residual return, uncorrelated with
_rM_ . The model also assumes that the residual returns _θi_ are uncorrelated with
each other. The rationale for the model is that a single common factor _rM_,
typically the return of the market portfolio, accounts for all of the common
shocks between pairs of assets. The parameter _βi_ is also called the _factor_ _loading_
or _factor_ _exposure_ of asset _i_ . The component _θi_ is also called the _residual_ or
_specific_ return of asset _i_, as it is the portion of _ri_ not accounted for by the
common factor _rM_ .
A bit of algebra shows that in this model the expected return of asset _i_ is


E( _ri_ ) = _βi_ E( _rM_ ) + E( _θi_ ) _,_


the covariance between two different assets _i_ and _j_ is


cov( _ri, rj_ ) = _βiβjσM_ [2] _[,]_


and the variance of asset _i_ is


var( _ri_ ) = _βi_ [2] _[σ]_ _M_ [2] [+] _[ ω]_ _i_ [2] _[,]_


where _σM_ [2] [= var(] _[r][M]_ [)] _[,]_ _[ω]_ _i_ [2] [= var(] _[θ][i]_ [).]
Using matrix–vector notation, the single-factor risk model assumption can be
succinctly written as


**r** = _**β**_ _rM_ + _**θ**_


108 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


and the vector of expected returns and covariance matrix can be written as

E( **r** ) = _**β**_ E( _rM_ ) + E( _**θ**_ ) _,_ **V** = _σM_ [2] _**[ββ]**_ [T][ +] **[ D]** _[,]_


where **D** is the diagonal matrix **D** = diag( _ω_ 1 [2] _[, . . ., ω]_ _n_ [2] [) = cov(] _**[θ]**_ [).]
We observe that under the single-factor model, the estimation of the covariance
matrix only requires the estimation of _**β**_ _, σM_ [2] _[,]_ [ and] **[ D]** [. That is a total of] _[ n]_ [+1+] _[n]_ [ =]
2 _n_ + 1 parameters in contrast to the [1] 2 _[n]_ [(] _[n]_ [ + 1)] [parameters] [for] [a] [non-structured]

covariance matrix. The particular structure of the covariance matrix for a singlefactor risk model also enables the derivation of some interesting properties of
minimum-risk portfolios. (See the exercises at the end of the chapter.)
A basic estimation of the parameters of a single-factor model can be performed
as follows. Assume we have some historical data of realized returns **r** (1) _, . . .,_ **r** ( _T_ )
as well as the corresponding returns for the factor **r** _M_ (1) _, . . ., rM_ ( _T_ ). Use these
data to run _n_ simple linear regressions


_ri_ = _αi_ + _βirM_ + _ϵi,_ _i_ = 1 _, . . ., n._


Each of these linear regressions yields estimates _β_ [ˆ] _i_ of _βi_, _α_ ˆ _i_ of E( _θi_ ), and _ω_ ˆ _i_ of
var( _ϵi_ ) = var( _θi_ ). Using the historical data _rM_ (1) _, . . ., rM_ ( _T_ ) for the factor, we
can also obtain an estimate _σ_ ˆ _M_ [2] [of] [var(] _[r][M]_ [).]
The above basic regression method can be enhanced to produce more accurate
estimates. In particular, it is known that the quality of the estimates of _**β**_ can
be improved via a _shrinkage_ _procedure_ as explained by Blume (1975). The basic
idea, which can be traced back to the classical work of Stein (1956), is that
improved estimates on _**β**_ can be obtained by taking a convex combination of the
raw estimates _**β**_ [ˆ] and **1** :

(1 _−_ _τ_ ) _**β**_ [ˆ] + _τ_ **1** _,_


for some shrinkage factor _τ_ . The articles of Ledoit and Wolf (2003, 2004) elaborate further on using shrinkage for improved estimates of the covariance matrix.
Efron and Morris (1977) present a related and entertaining discussion of shrinkage estimation applied to baseball statistics.
The estimates of _σM_ and of _ωi_ can also be improved by using techniques
such as exponential smoothing and generalized autoregressive conditional heteroskedasticity (GARCH) (Campbell et al., 1997; Engle, 1982).
The CAPM is related to, although not the same as, a single-factor risk model.
In the context of a single-factor model where the factor is the market portfolio
_rM_, the CAPM postulates


E( _ri_ ) = _βi_ E( _rM_ ) _._


In other words, the expected value of the asset-specific return is zero. The CAPM
thus gives a straightforward estimation procedure for the vector of expected
returns _**μ**_ = E( **r** ), namely _**μ**_ ˆ := _**β**_ [ˆ] _μ_ ˆ _M_, where _**β**_ [ˆ] and _μ_ ˆ _M_ are estimates of _**β**_ and
E( _rM_ ) respectively. As we discuss in Section 6.6 below, other alternatives for
estimating expected returns are often used in equity portfolio management.


**6.6** **Estimation** **of** **Inputs** **to** **Mean–Variance** **Models** 109


Constant Correlation Models


A second way of imposing structure on the asset returns is to assume that the correlation between any two different assets in the investment universe is the same.
Under this assumption, the estimation of the covariance matrix only requires
an estimate of each individual asset volatility _σi_ and the average correlation _ρ_
between different pairs of assets. This yields a “quick and dirty” estimate of the
covariance matrix given by


cov( _ri, rj_ ) = _ρσiσj,_ _i ̸_ = _j._


In this model the estimation of the covariance matrix only requires estimates of
_**σ**_ and _ρ_ . That is a total of _n_ + 1 parameters.
Under the reasonable assumption that _ρ_ _>_ 0, the constant correlation model
can be seen as the following kind of single-factor model with predetermined
factor loadings. Assume the following single-factor model for volatility _scaled_
excess returns:
_ri_
= _f_ + _θi,_
_σi_


where _f_ is a common factor to all scaled returns and _θi_ is a specific scaled
return on asset _i_ . It is easy to see that this particular single-factor model yields
a constant correlation model with _ρ_ being the variance of the single factor _f_ .
Using matrix notation, the constant correlation covariance matrix can be
written as


**V** = _ρ_ _**σσ**_ [T] + (1 _−_ _ρ_ )diag( _**σ**_ ) [2] _._


A basic estimation procedure for this model is straightforward: first, using historical data, compute estimates _σ_ ˆ _i_ of _σi_ and estimates _ρ_ ˆ _ij_ of each correlation _ρij_
for all _i ̸_ = _j_ . Finally, take the average



1
_ρ_ ˆ :=
_n_ ( _n −_ 1)





_ρ_ ˆ _ij_

_i_ = _j_



as an estimate of _ρ._


Multiple-Factor Models


Multiple-factor models are a generalization of the single-factor model discussed
above. These models are based on the assumption that the return of each asset
can be explained by a small collection of common factors in addition to some
other specific return. Aside from simplifying the estimation task, multiple-factor
models provide a useful breakdown of risk, incorporate some economic logic,
and are fairly flexible. The majority of quantitative money managers rely on
multi-factor models provided by third-party vendors such as MSCI, Axioma,
Northfield, etc. for the management of equity portfolios.


110 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


A multi-factor model assumes that excess returns are as follows:


       - _K_



_ri_ =



_Bikfk_ + _ui,_

_k_ =1



where


_•_ _ri_ : excess return of asset _i_

_•_ _Bik_ : exposure of asset _i_ to factor _k_

_•_ _fk_ : rate of return of factor _k_

_•_ _ui_ : specific (or residual) return of asset _i_ .


It is convenient to rewrite the relation above in matrix form as


**r** = **Bf** + **u** _._


A bit of matrix algebra shows that the expected value and covariance of **r** are
respectively


E[ **r** ] = **B** E[ **f** ] + E[ **u** ] _,_ **V** = **BFB** [T] + Δ _,_


where **F** = cov( **f** ) and Δ = cov( **u** ). Observe that Δ is diagonal since the _ui_ are
assumed to be uncorrelated with each other.
The construction and estimation of a multi-factor model hinges on the choice
of factors. For an equity universe, the following three main classes of factors are
commonly used:


_•_ Macroeconomic factors: inflation, economic growth, etc.

_•_ Fundamental factors: earning/price, dividend yield, market cap, etc.

_•_ Statistical factors: principal component analysis, hidden factors.


Empirical evidence suggests that the second type of fundamental factors works
better than the other two (Connor, 1995). This is also the prevalent class of
factors used by most risk model providers. In this approach we have


**r** = **Bf** + **u** _,_


where the matrix of factor loadings **B** is predetermined. The estimation of the
corresponding covariance matrix is as follows. Using historical data for the asset
returns, infer the corresponding historical data for factor returns by solving each
of the weighted least-squares problems


min( **r** ( _t_ ) _−_ **Bf** ( _t_ )) [T] **D** _[−]_ [1] ( **r** ( _t_ ) _−_ **Bf** ( _t_ )) _._


The matrix **D** is a diagonal matrix whose entries are estimates of the asset
variances. A common proxy is to use instead the reciprocal of the market capitalizations of the assets. The solution to this weighted least-squares problem is


**f** ( _t_ ) = ( **BD** _[−]_ [1] **B** [T] ) _[−]_ [1] **B** [T] **D** _[−]_ [1] **r** ( _t_ ) _._


**6.6** **Estimation** **of** **Inputs** **to** **Mean–Variance** **Models** 111


Each row of the matrix ( **BD** _[−]_ [1] **B** [T] ) _[−]_ [1] **B** [T] **D** _[−]_ [1] can be interpreted as a _factor_
_mimicking_ portfolio.
Equipped with this historical data of factor returns, we can estimate the factor
covariance matrix. The residuals **u** ( _t_ ) := **r** ( _t_ ) _−_ **Bf** ( _t_ ) can then be used to estimate
the covariance matrix Δ of asset-specific returns.
The connection between the CAPM and single-factor models has an analogous
counterpart in the context of multi-factor models, namely the _arbitrage_ _pricing_
_theory_ (APT). A combination of an arbitrage argument and the assumption that
the set of factors **f** account for all of the common shocks to the returns of all
assets in the investment universe implies that


E( **r** ) = **B** E( **f** ) _._


Like the CAPM, the APT model also yields a straightforward estimation procedure for _**μ**_ = E( **r** ).


Estimation of Alpha


In a benchmark-relative context, an estimate of expected residual returns _**α**_ is
typically the relevant estimate instead of an estimate of expected total return _**μ**_ .
According to the CAPM or the more general APT model, the expected residual
returns are zero. However, numerous articles have documented certain _anomalies_
that are systematically associated with the over- and underperformance of the
return of securities after controlling for their systematic component of return.
Some of these anomalies include the SMB (small minus big market capitalization)
and HML (high minus low book-to-price) factors introduced in the classical
article by Fama and French (1992).
A generic approach for generating alpha is to rely on _signals_ unveiled via
a judicious type of analysis. A signal could be an empirical observation such as
_momentum_ that suggests that the recent performance (good or bad) of individual
securities will persist in the near term. A signal could also be a financial principle
such as “firms with low book-to-price ratio will outperform” or “firms with higher
earnings per share will outperform”.
The following is a reasonable and popular rule of thumb for transforming a
signal into a forecast of alpha (for a detailed discussion see Grinold and Kahn
(1999)):


alpha = (residual volatility) _·_ IC _·_ score _._


Here the _residual volatility_ is the standard deviation of residual return. The _score_
is a numerical score associated with the signal. The score is assumed to be scaled
so that its cross-sectional mean and standard deviation are respectively 0 and 1.
Finally, the _information_ _coefficient_ IC is a measure of the forecasting quality of
the signal; that is, the correlation between the raw signal score and the residual
return.


112 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


In addition to proper scaling, the signal score should be _neutralized_ so that
the alphas do not include biases or undesirable bets on the benchmark or on risk
factors. As we illustrate in the exercises at the end of the chapter, neutralization
can be achieved in various ways, as there are multiple portfolios that hedge out
a bet on the benchmark or on other risk factors.


**6.7** **Performance** **Analysis**


How can the performance of a portfolio manager be evaluated? Are the _ex_ _post_
results due to skill or luck? The goal of performance analysis is to answer
these questions. The efficient market hypothesis suggests that skillful active
management is impossible. However, there is considerable evidence against the
efficient market hypothesis (Shleifer, 2000).
Empirical results also suggest that an _average_ active fund manager underperforms their benchmark on a risk-adjusted basis. Furthermore, empirical evidence
also shows that good performance does not persist: The winners this year are
almost as likely to be winners or losers next year. These are bleak conclusions
about asset management. So how could we tell which asset managers are the
good ones?
The fundamental goal of performance analysis is to separate skill from luck.
The simplest type of performance analysis is a cross-sectional comparison of
returns over some time period. This would distinguish winners from losers.
However, these kinds of comparisons have several drawbacks. First, they typically
do not represent the complete universe of investment managers but only those
in existence during a specific time period. They generally contain survivorship
bias. Perhaps worst of all, cross-sectional comparisons do not adjust for risk. By
contrast, time-series analysis of returns can do a better job at separating skill
from luck by measuring both return and risk. An even more complete picture
can be obtained via time-series analysis of returns and portfolio holdings.


Return-Based Performance Analysis (Basic)


The development of the CAPM and the notion of market efficiency in the 1960s
encouraged academics to tackle the problem of performance analysis. According
to the CAPM, consistent exceptional returns are unlikely. Academics devised
tests to check if the theory was correct. As a byproduct the first performance
analysis techniques emerged. One approach, proposed by Jensen, consists of
regressing the time series of _realized_ portfolio excess returns against benchmark
excess return:


_rP_ ( _t_ ) = _αP_ + _βP rB_ ( _t_ ) + _ϵP_ ( _t_ ) _._


_Jensen’s_ _alpha_ is simply the intercept _αP_ of this regression. According to the
CAPM, this intercept is zero. The regression yields not only alpha and beta,


**6.7** **Performance** **Analysis** 113


but _t_ -statistics that give information about their statistical significance. The
_t-statistic_ for _αP_ is

_αP_
_t_ -stat =
SE( _αP_ ) _[.]_


As a rule of thumb, a _t_ -statistic of 2 or more indicates that the performance of
the portfolio is due to skill rather than luck. Assuming normality, the probability
of observing such a large _t_ -statistic purely by chance is smaller than 5%.
The _t_ -statistic and the information ratio are closely related. The main difference between them is that the information ratio is annualized. By contrast, the
_t_ -statistic scales with the number of years of data. If we observe returns over a
period of _T_ years, the information ratio is approximately the _t_ -statistic divided
by the square root of the number of years of observation:


_IR ≈_ _[t]_ [-stat] ~~_√_~~ _._

_T_


The standard error of the information ratio is approximately


1
SE( _IR_ ) _≈_ ~~_√_~~ _._

_T_


A simple alternative to Jensen’s approach is to compare Sharpe ratios for the
portfolio and the benchmark. A portfolio with


_r_ ¯ _P_

_>_ _[r]_ [¯] _[B]_ _,_
_σP_ _σB_



where _r_ ¯ denotes mean excess return over the period, has demonstrated positive
performance. Once again, the statistical significance of this relationship is relevant for distinguishing luck from skill. If we assume that the standard errors of
the portfolio and benchmark volatilities are fairly small compared to _r_ ¯ standard
_√_
errors, then the standard error of the Sharpe ratio is approximately 1 _/_ _N_, where

_N_ is the number of observations. Hence a statistically significant demonstration
of skill occurs when




~~�~~
2
_N_ _[.]_



_r_ ¯ _P_ _−_ _[r]_ [¯] _[B]_ _>_ 2
_σP_ _σB_



Return-Based Style Analysis


_Style_ _analysis_ was developed by Nobel laureate William Sharpe (1992). The
popularity of this concept was aided by a study (Brinson et al., 1991) concluding
that 91.5% of the variation in returns of 82 mutual funds could be explained
by the allocation to bills, stocks, and bonds. Later studies considering asset
allocation across a broader range of asset classes have shown that as much as
97% of fund returns can be explained by asset allocation alone.
Style analysis attempts to determine the effective asset mix of a fund using
only the time series of returns for the fund and for a number of carefully chosen


114 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


asset classes. Like a factor model approach, style analysis assumes that portfolio
returns have the form


       - _m_



_rP_ ( _t_ ) =



_wjfj_ ( _t_ ) + _uP_ ( _t_ ) _,_

_j_ =1



where the _fj_ ( _t_ ) are the returns of _m_ benchmark asset classes. The holdings
_wj,_ _j_ = 1 _, . . ., m_, represent the _style_ of the portfolio. That is, the effective allocation to the _m_ asset classes that could be replicated via a passive portfolio. The
term _uP_ ( _t_ ) represents the _selection_ _return_ ; that is, the portion of the portfolio
return that style cannot explain. The effective holdings can be estimated via the
quadratic program


min var( _uP_ ( _t_ ))
**w**

     - _m_



(6.21)



s.t.



_wj_ = 1

_j_ =1

_wj_ _≥_ 0 _,_ _j_ = 1 _, . . ., m._



Notice that there are two key differences between this model and conventional
multiple regression. First, the weights are constrained to be non-negative and to



add up to 1. Second, instead of minimizing the sum of squared errors




- _T_

_uP_ ( _t_ ) [2] _,_
_t_ =1



we minimize the variance of these quantities. The reason for the first restriction is
that the _wj_ are to be interpreted as an effective asset allocation representing the
style of the fund. In essence, they create a fund-specific benchmark. The reason
for the second restriction is that we want to allow for a non-zero selection effect
by the fund manager. The model finds the style that minimizes the variance of
this effect. Once the optimal weights are determined, the average value of _uP_ ( _t_ )
gives the value added by the manager’s selection skills, which can be negative or
positive.
Assume the data available for style analysis are the return time series _rP_ ( _t_ ) _,_
_f_ 1( _t_ ) _, . . ., fm_ ( _t_ ) for _t_ = 1 _, . . ., T_ . For ease of notation, put



⎡ ⎤

_f_ 1(1) _· · ·_ _fm_ (1)

⎢⎣ ... ... ... ⎥⎦ _,_ **1** :=

_f_ 1( _T_ ) _· · ·_ _fm_ ( _T_ )



⎤

1
... ⎥⎦ _._
1



**r** :=



⎡ ⎤

_rP_ (1)

⎢⎣ ... ⎥⎦ _,_ **F** :=

_rP_ ( _T_ )



⎡

⎢⎣



Then the objective function in (6.21) can be written as




[1]

_T_ _[∥]_ **[r]** _[ −]_ **[Fw]** _[∥]_ [2] _[ −]_ _T_ [1]



var ( **r** _−_ **Fw** ) = [1]




 _∥_ **r** _∥_ 2
=



_T_ [2]



_T_ [2] [(] **[1]** [T][(] **[r]** _[ −]_ **[Fw]** [))][2]



_∥_ 2

_−_ [(] **[1]** [T] **[r]** [)][2]
_T_ _T_ [2]




  -  _T_ [1] **[11]** [T] **F** **w** _._




- **r** T **F**

_−_ 2 _−_ **[1]** [T] **[r]**
_T_ _T_ [2]




  -  1
+ **w** [T] _T_ **[F]** [T] _I_ _−_ _T_ [1]




   
[T] **[r]**

_T_ [2] **[1]** [T] **[F]** **w**


**6.9** **Exercises** 115


Style analysis provides an improvement tool for measuring performance. The
constructed style usually tracks the performance of the fund more accurately
than a predefined benchmark. Style analysis has also some limitations. For
instance, the weights may not necessarily match the style disclosed by the fund
manager. However, as Sharpe puts it: “If it acts like a duck, it is ok to assume it is
a duck.” Style analysis also makes the simplifying assumptions that the weights
are constant. This is clearly not the case in actively managed funds, even without
active trading. There exist some variations of style analysis that allow for weights
to change. The model gets a bit more technical because it needs to incorporate
some “regularization” term that prevents the weights from changing too much
too often.


**6.8** **Notes**


The mean–variance model was introduced in the seminal article of Markowitz
1
(1952). The CAPM was developed by Treynor, Sharpe (1964), Lintner (1965),
and Mossin (1966), by building on the mean–variance approach of Markowitz.
In recognition of their work on portfolio choice and the CAPM, Sharpe and
Markowitz were jointly awarded the 1990 Nobel Prize in Economics. Both Lintner and Mossin passed away before 1990 and Treynor’s manuscript was never
published.
The textbook by Grinold and Kahn (1999) is a classical reference in active
portfolio management. In their textbook, Grinold and Kahn developed and relied
extensively on characteristic portfolios.


**6.9** **Exercises**


**Exercise** **6.1** The purpose of this exercise is to prove the two-fund theorem
(Theorem 6.1).


(a) Find the Lagrangian function _L_ ( **x** _, θ_ ) for (6.1).
(b) Solve the optimality conditions _∇L_ ( **x** _, θ_ ) = **0** to conclude that the optimal
solution to (6.1) is


1 1
**x** _[∗]_ = _λ ·_
**1** [T] **V** _[−]_ [1] _**μ**_ **[V]** _[−]_ [1] _**[μ]**_ [ + (1] _[ −]_ _[λ]_ [)] _[ ·]_ **1** [T] **V** _[−]_ [1] **1** **[V]** _[−]_ [1] **[1]**


where _λ_ = **1** [T] **V** _[−]_ [1] _**μ**_ _/γ_ .


**Exercise** **6.2** Assume _**μ**_ and **V** are respectively the vector of expected returns
and covariance matrix of _n_ risky assets. Assume _V_ is non-singular and _μ_ ¯ _>_
_**μ**_ [T] **V** _[−]_ [1] **1** _/_ **1** [T] **V** _[−]_ [1] **1** . Consider the mean–variance optimization problem


1
“Toward a theory of market value of risky assets”. Unpublished manuscript, 1961.


116 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


min **x** [T] **Vx**
s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯ (6.22)
**1** [T] **x** = 1 _._


Now consider the following variations:


max _**μ**_ [T] **x**
s.t. **x** [T] **Vx** _≤_ _σ_ ¯ [2] (6.23)

**1** [T] **x** = 1 _,_


and
max _**μ**_ [T] **x** _−_ [1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**

(6.24)
s.t. **1** [T] **x** = 1 _._


Let **x** _[∗]_ be the optimal solution to (6.22). Find appropriate values of _σ_ ¯ and _γ_ so
that the optimal solutions to (6.23) and (6.24) are also **x** _[∗]_ .


**Exercise** **6.3** Prove that

       - _n_

_|x_ [0] _j_ _[−]_ _[x][j][| ≤]_ _[h]_
_j_ =1

                           - �T
if and only if there exists a vector **y** = _y_ 1 _· · ·_ _yn_ such that


_xj_ _−_ _x_ [0] _j_ _[≤]_ _[y][j]_


_x_ [0] _j_ _[−]_ _[x][j]_ _[≤]_ _[y][j]_

       - _n_

_yj_ _≤_ _h._

_j_ =1


**Exercise** **6.4** Prove that under the two assumptions made in Section 6.4, the
maximum Sharpe ratio problem (6.16) is indeed equivalent to (6.18).


**Exercise** **6.5** The purpose of this exercise is to prove Proposition 6.4.
Assume the covariance matrix of asset returns **V** is positive definite and the
minimum- risk portfolio (1 _/_ **1** [T] **V** _[−]_ [1] **1** ) **V** _[−]_ [1] **1** has positive expected return; that
is, _**μ**_ [T] **V** _[−]_ [1] **1** _>_ 0.


(a) Show that (6.19) can be rewritten as follows:


min **z** [T] **Vz**
**z** _,κ_



s.t. _**μ**_ [T] **z** = 1
**1** [T] **z** _−_ _κ_ = 0
_κ_ _>_ 0 _._


(b) Show that the solution to (6.25) is


1
**z** _[∗]_ =
_**μ**_ [T] **V** _[−]_ [1] _**μ**_ **[V]** _[−]_ [1] _**[μ]**_

_κ_ _[∗]_ = **1** [T] **z** _[∗]_ _._



(6.25)


**6.9** **Exercises** 117


(c) Use part (b) to conclude that the solution to (6.19) is indeed


1
**x** _[∗]_ =
**1** [T] **V** _[−]_ [1] _**μ**_ **[V]** _[−]_ [1] _**[μ]**_ _[.]_


(d) *Show that if _**μ**_ [T] **V** _[−]_ [1] **1** _<_ 0 then (6.19) is bounded but does not attain
its maximum value. Use this fact to illustrate why the two assumptions
made in Section 6.4 cannot simply be dropped without making some other
assumptions.


**Exercise** **6.6** The Excel spreadsheet “Exercise 6.6 Six Stocks” provides hypothetical estimates of the expected return and variance–covariance matrix for a
set of six stocks.


(a) Set up a quadratic programming model to determine the long-only minimumvariance portfolio that can be constructed with the six stocks. What is the
expected return of your minimum-variance portfolio?

(b) Set up the classical Markowitz model with long-only constraints. Solve your
model for at least six different levels of expected return ranging from the
level found in part (a) up to the largest expected return level for which
there are feasible portfolios. What is the value of such largest return level?

Use your results to generate the expected return versus standard deviation
plot for the efficient frontier.

(c) Assume the “benchmark” is a portfolio equally divided among the six stocks.
Compute the beta of each stock (with respect to this benchmark) and the
consensus (i.e., CAPM) returns assuming the risk-free rate is zero.

(d) Assume that your current portfolio is the benchmark, i.e., it is equally
divided among the six stocks. Include an additional total turnover constraint
of 70% in the model from part (b). Determine the new optimal portfolio for
a desired expected return somewhere in the middle of the range used in
part (b). Is it possible to find portfolios with any return level in the range
in part (b)? If it is not, can you explain why?

(e) Find the portfolio with maximum Sharpe ratio subject to all constraints in
part (d). Again, assume the risk-free rate is zero.


**Exercise** **6.7** The Excel spreadsheet “Exercise 6.7 Twenty Stocks” contains
estimated expected values, standard deviations, and correlations of monthly
returns for a set of 20 large-capitalization stocks from the S&P 500.


(a) Find the fully invested long-only portfolio with minimum variance.

Find the numerical values of the first two and last two positions in your
portfolio (i.e., those of BOL, NE, and XTO, ABC). These numbers are
between 0 and 1.


Find the numerical value of the variance of the portfolio (in bps [2] ).


118 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


(b) Assume the benchmark is an equally weighted portfolio of the 20 assets.
Determine the beta of each asset relative to this benchmark.


Find the numerical values of the beta of the first two stocks and last stock.

(c) Find the fully invested long-only portfolio with highest expected return that
satisfies the following constraints:

_•_ The size of every position is at most 10%.

_•_ The portfolio has beta equal to 1.

Find the numerical values of the first and last positions in your portfolio.

Find the numerical value of the expected return of the portfolio (in bps).

(d) Assume the risk-free rate is zero. Find the fully invested long-only portfolio
with highest Sharpe ratio that satisfies the following constraints:

_•_ The size of every position is at most 10%.

_•_ The portfolio has beta equal to 1.

Find the numerical values of the positions 15 and 16 in your portfolio (i.e.,
those of LH and R).

Find the numerical value of the Sharpe ratio of the portfolio.


**Exercise** **6.8** Suppose _M_ is the market portfolio in a universe of securities.
According to the CAPM, the excess return of each security is given by


_ri_ = _βirM_ + _ϵi,_


where _ϵi_ is the zero-mean, security-specific risk, and _rM_ is the market excess
return. For simplicity assume the risk-free rate is zero.
Suppose that via a thorough security analysis a manager identifies an active
portfolio _A_ whose return is


_rA_ = _αA_ + _βArM_ + _ϵA_ ;


let _ωA_ [2] [= var(] _[ϵ][A]_ [)] [denote] [the] [residual] [variance] [of] [the] [active] [portfolio] _[A]_ [.]
Consider a portfolio _P_ obtained by investing a proportion _w_ in the active
portfolio _A_ and the remaining proportion 1 _−_ _w_ in the market portfolio:


_rP_ ( _w_ ) = _wrA_ + (1 _−_ _w_ ) _rM_ _._


(a) Find the expressions for the expected return and variance of the portfolio _P_ .
(b) Assume _βA_ = 1, _αA_ _>_ 0, and _μM_ _>_ 0. Show that the portfolio _P_ with
highest Sharpe ratio is attained for the following proportion value:

_w_ 0 = _[α][A][/ω]_ _A_ [2] _._
_μM_ _/σM_ [2]


Furthermore, show that, for this proportion value, the Sharpe ratio of the
portfolio is



�2
_._




      _μM_
_SP_ [2] [=] _[ S]_ _M_ [2] [+] _[ IR]_ _A_ [2] [=]
_σM_



�2 _αA_
+
_ωA_


**6.9** **Exercises** 119


**Exercise** **6.9** Suppose the covariance matrix of a universe of _N_ stocks has the
following _single-factor_ _risk_ _model_ form:

**V** = _σM_ [2] _**[ββ]**_ [T][ +] **[ D]** _[.]_

Here _σM_ [2] [is] [the] [single-factor] [risk,] _**[β]**_ [=] - _β_ 1 _· · ·_ _βN_ �T _∈_ R _N_ is the vector of
stock loadings on that factor, and **D** = diag( _ω_ 1 [2] _[, . . ., ω]_ _N_ [2] [)] [where] [each] _[ω]_ _i_ [2] [is] [the]
idiosyncratic risk of stock _i_ for _i_ = 1 _, . . ., N_ .


(a) Recall that the Sherman–Morrison–Woodbury matrix inverse formula is

( **A** + **uv** _[⊤]_ ) _[−]_ [1] = **A** _[−]_ [1] _−_ **[A]** _[−]_ [1] **[uv]** _[⊤]_ **[A]** _[−]_ [1]

1 + **v** _[⊤]_ **A** _[−]_ [1] **u**

provided **A** _[−]_ [1] exists and 1 + **v** _[⊤]_ **A** _[−]_ [1] **u** _̸_ = 0. Use this formula to show that

**V** _[−]_ [1] = **D** _[−]_ [1] _−_ _σM_ [2] _·_ **D** _[−]_ [1] _**ββ**_ [T] **D** _[−]_ [1] _._
1 + _σM_ [2] _**[β]**_ [T] **[D]** _[−]_ [1] _**[β]**_


(b) *Using (a) conclude that the holdings of the minimum-variance fully invested
portfolio (1 _/_ **1** [T] **V** _[−]_ [1] **1** ) _·_ **V** _[−]_ [1] **1** are given by





_,_ _i_ = 1 _, . . ., N,_



_xi_ = _[σ]_ _MV_ [2]
_ωi_ [2]




1 _−_ _[β][i]_

_βLS_



where

1
_σMV_ [2] [=]
**1** [T] **V** _[−]_ [1] **1**

is the variance of the minimum-variance portfolio and _βLS_ is the following
_long–short_ _threshold_ _beta:_


_M_ _**[β]**_ [T] **[D]** _[−]_ [1] _**[β]**_
_βLS_ = [1 +] _[ σ]_ [2] _._
_σM_ [2] _**[β]**_ [T] **[D]** _[−]_ [1] **[1]**


(c) *Show that the holdings of the _long-only_ minimum-variance portfolio of the
_N_ stocks are given by an expression similar to that in part (b) above:



�+
_,_ _i_ = 1 _, . . ., N,_



_xi_ = _[σ]_ _LMV_ [2]

_ωi_ [2]




1 _−_ _[β][i]_

_βL_



where _σLMV_ [2] [is] [the] [variance] [of] [the] [long-only] [minimum-variance] [portfolio]
and _βL_ is a suitable long-only threshold beta.


**Exercise 6.10** Suppose the covariance matrix of a set of assets has the following
_constant-correlation_ form: for some _ρ ∈_ (0 _,_ 1)


**V** _ii_ = _σi_ [2] _[,]_ **[V]** _[ij]_ [=] _[ ρσ][i][σ][j][,]_ [for] _[i]_ [ = 1] _[, . . ., n,]_ [and] _[j]_ [= 1] _[, . . ., n,]_ [with] _[i][ ̸]_ [=] _[ j.]_


In matrix form, we can write the above constant-correlation matrix as follows:


**V** = _ρ_ _**σσ**_ [T] + (1 _−_ _ρ_ )Diag( _**σ**_ ) [2] _,_


where _**σ**_ is the vector with components _σi,_ _i_ = 1 _, . . ., n_ .


120 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


(a) Use the Sherman–Morrison–Woodbury formula to show that


1 _ρ_
**V** _[−]_ [1] =
1 _−_ _ρ_ [Diag(] _**[θ]**_ [)][2] _[ −]_ (1 _−_ _ρ_ )(1 + ( _n −_ 1) _ρ_ ) _**[θθ]**_ [T] _[,]_


where _**θ**_ is the vector with components _θi_ = 1 _/σi,_ _i_ = 1 _, . . ., n_ .
(b) Conclude that the holdings _xi,_ _i_ = 1 _, . . ., n_, of the fully invested, minimumrisk portfolio are as follows:

_xi_ = ~~�~~ _nyi_ _,_
_j_ =1 _[y][j]_



where




- _n_


_j_ =1



_σi_
_σj_



1
_yi_ = (1 _−_ _ρ_ ) _σi_ [2]



⎡

_ρ_
⎣1 _−_
(1 _−_ _ρ_ )(1 + ( _n −_ 1) _ρ_ )



⎤


⎦ _._



(c) Assume all of the assets have the same volatility: that is, _σ_ 1 = _σ_ 2 = _· · ·_ =
_σn_ = _σ._ Prove that the variance of the fully invested portfolio of minimum
variance is

_σ_ min [2] [=] _[σ]_ [2][(1 + (] _[n][ −]_ [1)] _[ρ]_ [)] _._

_n_

**Exercise** **6.11** The purpose of this exercise is to detail the derivation of _factor_
_portfolios_ used in the construction of risk models. Consider the following factor
model for a vector of returns


**r** = **Bf** + **u** _,_


where **B** is a given matrix of factor loadings and the factors **f** are to be constructed. A common approach to construct the factors **f** is to solve the following
kind of weighted least-squares problem:


min ( **r** _−_ **Bf** ) [T] **D** _[−]_ [1] ( **r** _−_ **Bf** ) _,_ (6.26)
**f**


where **D** is a symmetric (often diagonal) positive definite matrix.


(a) Show that the gradient of the multivariate function **f** _�→_ ( **r** _−_ **Bf** ) [T] **D** _[−]_ [1] ( **r** _−_
**Bf** ) is

2( **B** [T] **D** _[−]_ [1] **B** ) **f** _−_ 2 **B** [T] **D** _[−]_ [1] **r** _._


(b) Conclude that the solution to (6.26) is


**f** = ( **B** [T] **D** _[−]_ [1] **B** ) _[−]_ [1] **B** [T] **D** _[−]_ [1] **r** _._


(c) Consider the special case when **B** = **b** has only one column, i.e., there is only
one factor _f_ . Conclude that in this case the above optimal _f_ is the return of
the following “characteristic portfolio”:

1
**b** [T] **D** _[−]_ [1] **b** **[D]** _[−]_ [1] **[b]** _[.]_


(d) Consider again part (c) and the very special case when the entries of **b** are 1
(a “buy” list) and _−_ 1 (a “sell” list) and **D** is a diagonal matrix. Show that
in this case the characteristic portfolio in part (c) is a long–short portfolio


**6.10** **Case** **Studies** 121


with long holdings in the “buy list” and short holdings in the “sell list”.
Describe the values of the portfolio holdings when **D** = **I** .


**Exercise** **6.12** Consider two portfolio managers. One has 25 years of performance history, with a realized Sharpe ratio of 0.5. The other one has only four
years of performance history but with a realized Sharpe ratio of 0.75. Which
one would you prefer to invest in and why? The objective is to minimize the
likelihood that you will lose money. Returns can be assumed to be stationary
and normally distributed.


**6.10** **Case** **Studies**


Asset Allocation


The goal of this case study is to apply and test mean–variance optimization
models as a tool for asset allocation.


(1) Choose between four and ten asset classes and collect their monthly, quarterly, or annual historical returns over a meaningful horizon (several years
or decades). Collect also any other relevant data that may help you forecast
expected returns. Briefly discuss why you would like to choose these assets
and why the selected horizon is appropriate.
(2) Use the first 67% portion of your data to compute the expected returns and
the variance–covariance matrix for these assets. (Use the remaining 33% for
out-of-sample testing.)
(3) Set up the classical Markowitz model without short sales and solve it in
Excel Solver or MATLAB for various levels of expected return.
(4) Evaluate, compare, and report your results in-sample and out-of-sample.
(5) Discuss the results of your model.


Covariance Estimation


The goal of this case study is to compare various approaches to covariance
estimation and risk diversification.


(1) Select a universe of at least 25 stocks. Some possible choices are the Dow
Jones Industrial Average, the S&P 100, and the Nasdaq 100. If you feel
ambitious, you may choose a larger universe. Your purpose is to construct
the most diversified fully invested portfolio in this universe. Collect weekly
or monthly historical returns for securities in your universe over a horizon
of a few years.
(2) Use the first 67% portion of historical data for “model calibration” (estimates
of covariance matrix) and the remaining 33% for out-of-sample testing.
(3) Use the in-sample data to generate the following two estimates of the covariance matrix: the sample covariance, and a single-factor model covariance.
For the latter, you need to choose a suitable benchmark portfolio. Some


122 **Quadratic** **Programming** **Models:** **Mean–Variance** **Optimization**


reasonable choices are a value-weighted portfolio and an equally weighted
portfolio.

(4) Using the two estimates of the covariance matrices computed in (3), find
minimum-risk fully invested portfolios (both long–short and long-only).

(5) Compare the results of your models on out-of-sample data. Generate plots
of the value of the different portfolios on out-of-sample data.

(6) Repeat (5) using a rolling-time window assuming that all portfolios are
rebalanced monthly. Compare these models with value-weighted and equally
weighted portfolios.

Report statistics such as out-of-sample mean and standard deviation of
results, and average portfolio turnover. Comment on your results.


Active Portfolio Management


The goal of this case study is to apply mean–variance optimization as a tool for
active portfolio management. If you are well versed with the Bloomberg terminal,
you may use Bloomberg’s portfolio analytics capabilities PORT.


(1) Choose at least 20 securities within an asset class (e.g., stocks in the Dow
Jones, the S&P 500, the NASDAQ, or the Russell 3000) and find their
weekly or monthly historical returns over a meaningful horizon. Collect also
relevant additional data for alpha estimation. For instance, Fama–French
factors (book-to-market ratio, size, momentum), or any other factors that
you can use to rank your stocks. Briefly discuss your selection of securities
and data.

(2) Choose a suitable “benchmark portfolio”. For instance, if you chose stocks
from the S&P 500, a reasonable benchmark would be a value-weighted
portfolio of the sets of selected assets.

(3) Use the first 67% portion of historical data for “model calibration” (estimates
of covariance matrix, betas, alphas, etc.) and the remaining 33% for out-ofsample testing.

(4) Use the in-sample data to estimate the covariance matrix, betas and alphas
of your stocks. The most straightforward way to estimate the betas of your
stocks is via linear regression. This would also give you a rudimentary estimate of the alphas. However, these are “realized” estimates, i.e., they are
backward looking. Instead you may try to forecast alphas (i.e., be forward
looking) via one of the following approaches:


_•_ Momentum factor: rank stocks according to how they have performed in
the recent three to twelve months.

_•_ Other factors: rank stocks according to other factors such as the Fama–
French factors, price-to-earnings ratio, debt-to-equity ratio, or some
combination of these.


**6.10** **Case** **Studies** 123


(5) Set up an optimization model with the goal of constructing portfolios that
outperform the benchmark. Discuss your selection of objective and constraints in your model.
(6) Test the results of your model on out-of-sample data. You may want to
do this for various combinations of constraint levels (e.g., small and large
levels of tracking errors, small and large levels of active positions, turnover
constraint). The most interesting way of doing this is via a “rolling-time
window”. To that end, proceed as follows:
(a) Partition the out-of-sample data into _m_ equally sized time intervals, e.g.,
month-long intervals.
(b) Using the estimates from (4), find the optimal portfolio. Assume you
hold this portfolio over the first of the _m_ out-of-sample time intervals.
(c) Next, shift the in-sample time window used in step (b). Keep the
length of the in-sample time window unchanged. Use this new in-sample
time window to update your estimates of covariance matrix, betas,
and alphas. Find the new optimal portfolio. Assume you will hold this
portfolio over the next out-of-sample time interval.
(d) Repeat step (c) until you reach the last ( _m_ th) out-of-sample time
interval.
Report and comment on your results.


## 7 Sensitivity of Mean–Variance Models to Input Estimation

One of the most salient drawbacks of mean–variance optimization is its high
sensitivity to the estimation of input parameters. The sensitivity is due to the
very nature of the optimization process: if there are assets whose returns appear
to be superior, the portfolios generated by an optimization procedure will try to
take advantage of these apparently superior assets by overweighting the holdings
on those positions. Unfortunately in a practical setting there is inevitable noise
in the estimation of inputs to a mean–variance model. Small perturbations in the
values of the inputs may lead to large swings in the composition of the portfolio.
This unfortunate phenomenon is basically due to the fact that the optimizer is
overly responsive given the quality of the inputs typical in portfolio construction.
A related phenomenon is the fact that the composition of portfolios is often
non-intuitive. Theoretical and empirical evidence indicates that the estimate of
expected returns is more critical than the estimate of the covariance matrix.

The sensitivity of mean–variance models to input estimation manifests itself
in the differences among the _true_, _estimated_, and _actual_ efficient frontiers, terms
coined by Broadie (1993). The true efficient frontier is the one computed with
the true (unobservable) expected returns and covariance matrix. The estimated
frontier is the one computed with estimates of these parameters. The actual
frontier is defined as follows: take the portfolios in the estimated frontier and
calculate their true expected returns and variances. The actual frontier always
lies below the true frontier. In principle the estimated frontier may lie anywhere
with respect to the true frontier. However, due to the optimization process, if the
estimation errors have zero mean, the estimated frontier is likely to lie above the
true frontier. In that case the actual frontier would be well below the estimated
frontier. Equivalently, the _ex_ _post_ performance of estimated efficient portfolios
would typically be substantially worse than their _ex_ _ante_ performance suggested
by the mean–variance model. Figure 7.1 illustrates the typing relative placement
of the three frontiers.

The following specific example illustrates the sensitivity of mean–variance
models to the quality of the inputs.

Consider a simple portfolio optimization problem with three assets whose
expected returns and covariance matrix are



⎡

0 _._ 250 0 _._ 225 0 _._ 045
⎣0 _._ 225 0 _._ 250 0 _._ 045
0 _._ 045 0 _._ 045 0 _._ 090



⎤


⎦ _._ (7.1)



_**μ**_ =



⎡

0 _._ 11
⎣0 _._ 10
0 _._ 05



⎤


⎦ _,_ **V** =


**Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation** 125


actual


0


**Figure** **7.1** Efficient frontiers


Figure 7.2 displays the composition of long-only efficient portfolios for this
problem.


**Figure** **7.2** Area chart of long-only efficient portfolios for _**μ**_ and **V** as in (7.1)


The picture makes sense from the pure optimization standpoint: assets 1 and 2
are similar but the expected return of asset 1 is slightly larger. Hence for higher
target expected returns, the efficient portfolios have a much larger holding in
asset 1 than in asset 2. However, from the portfolio construction standpoint this
is unintuitive: assets 1 and 2 are very similar and, for all practical purposes,
exchangeable because the slight difference could easily be due to estimation
error. Therefore, it would be more intuitive for the positions of these two assets
to be roughly the same. We can also look at the problem in a different way:
Suppose the expected returns of assets 1 and 2 were slightly perturbed so that
they are swapped. Then the composition of the efficient portfolios would change
drastically. This again is a fairly counterintuitive and unnatural behavior.
The input sensitivity of mean–variance models is a central issue in portfolio
management and has been a subject of intense study. There is a tremendous
upside potential in finding appropriate ways of harnessing the power of portfolio
optimization without getting caught on this major shortcoming. We will next



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-137-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-137-2.png)
126 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**


describe some of the most popular techniques that aim at mitigating this problem. The techniques can be classified in two main categories. The first category of
techniques tries to improve the quality of the inputs to the portfolio optimization
problem. The second category of techniques aims to tweak the optimization procedure. One of the most widely used techniques in the first category is the _Black–_
_Litterman_ _model_ introduced by Fisher Black and Bob Litterman at Goldman
Sachs Asset Management. We will discuss this technique in some detail. We will
also briefly describe another related technique based on Bayesian adjustments.
We will subsequently discuss some techniques in the second category, namely
_resampled_ _efficiency_ and _robust_ _optimization._


**7.1** **Black–Litterman** **Model**


The basic idea of the Black–Litterman model is to tilt the market equilibrium
returns to incorporate an investor’s views. In principle a classical mean–variance
model requires estimates of expected returns for all assets in the investment
universe considered. This is typically an enormous task. Investment managers
are unlikely to have detailed knowledge of all securities at their disposal. Typically, they have a specific area of expertise. Furthermore, some modern trading
strategies are associated not with _absolute_ but with _relative_ rankings of securities.
For instance, a pairs trading strategy corresponds to a forecast that one stock will
outperform another one. The key insight of Black and Litterman was that there is
a suitable way of combining the investor’s views with the market equilibrium. The
exposition of the Black–Litterman model below is based on Black and Litterman
(1992), Fabozzi et al. (2007), and Litterman (2003).


Basic Assumption and Starting Point


The Black–Litterman model is an equilibrium-based model, meaning that the
expected returns of the assets should be consistent with the market equilibrium
unless the investor has some specific views. In other words, an investor without
any views on the market should hold the market. We shall let _**π**_ denote the
equilibrium return vector, and **V** the covariance matrix of the asset returns.
The true expected return vector _**μ**_ is unknown. As a starting point, we assume
that the equilibrium return vector serves as a reasonable _prior_ estimate of the
true return vector in the sense that


_**μ**_ _∼_ _N_ ( _**π**_ _,_ **Q** ) _._


That is, _**μ**_ is a multi-normal random vector with expected value _**π**_ and covariance
matrix **Q** . The matrix **Q** represents the confidence on the equilibrium returns as
an estimate of expected returns.


**7.1** **Black–Litterman** **Model** 127


Expressing Investors’ Views


A key ingredient of the Black–Litterman model is to incorporate investors’ views
on the expected returns. The framework is fairly flexible. An investor may have a
few different views, each of them involving either a single asset (an absolute view)
or several assets (a relative view). Formally, a collection of views is expressed as


**P** _**μ**_ = **q** + _**ϵ**_ _,_ _**ϵ**_ _∼_ _N_ ( **0** _,_ **Ω** ) _._


Each row in the equation **P** _**μ**_ = **q** + _**ϵ**_ is a view that represents a forecast. The
term _**ϵ**_ represents the degree of confidence in the views. The covariance matrix **Ω**
is typically a diagonal matrix. A weak view is a view with large variance; a strong
view is a view with small variance. In the extreme, a certain view is a view with
zero variance. Each of the views can be _absolute_ or _relative_ as described above.
For a concrete example, consider an asset allocation problem with seven asset
classes: Australia, Canada, France, Germany, Japan, United Kingdom, United
States. Suppose we have two views:


_•_ Return on Germany will be 12%.

_•_ UK will outperform US by 2%.


These views can be expressed as


_μ_ 4 = 12% + _ϵ_ 1
_μ_ 6 _−_ _μ_ 7 = 2% + _ϵ_ 2 _._


In matrix notation this corresponds to **P** _**μ**_ = **q** + _**ϵ**_ for




       -       -       0 0 0 1 0 0 0 12%
**P** = _,_ **q** =
0 0 0 0 0 1 _−_ 1 2%


Merging Investors’ Views and Market Equilibrium




- _,_ _**ϵ**_ = _ϵ_ 1
_ϵ_ 2





_._



The key insight of the Black–Litterman model is a proper way to combine the
investor’s views with the prior market equilibrium. First, consider the simpler
case when the views are assumed to be certain; that is, **Ω** = **0** or equivalently
the vector of expected returns must be tilted to satisfy the views **P** _**μ**_ = **q** _._ In
this case the _posterior_ estimate of _**μ**_ given the prior _**μ**_ _∼_ _N_ ( _**π**_ _,_ **Q** ) and the views
**P** _**μ**_ = **q** is


_**μ**_ ˆ = _**π**_ + **QP** [T] ( **PQP** [T] ) _[−]_ [1] ( **q** _−_ **P** _**π**_ ) _._ (7.2)


Some matrix algebra shows that indeed **P** _**μ**_ ˆ = **q** . That is, the posterior estimate
satisfies the views **P** _**μ**_ = **q** _._
In the more general case when the views are not certain, the _posterior_ estimate
of _**μ**_ given the prior _**μ**_ _∼_ _N_ ( _**π**_ _,_ **Q** ) and the views **P** _**μ**_ = **q** + _**ϵ**_, with _**ϵ**_ _∼_ _N_ ( **0** _,_ **Ω** ), is


_**μ**_ ˆ = _**π**_ + **QP** [T] ( **PQP** [T] + **Ω** ) _[−]_ [1] ( **q** _−_ **P** _**π**_ ) _._ (7.3)


128 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**


When **Ω** is non-singular, _**μ**_ ˆ also has the following equivalent expression:


_**μ**_ ˆ = ( **Q** _[−]_ [1] + **P** [T] **Ω** _[−]_ [1] **P** ) _[−]_ [1] ( **Q** _[−]_ [1] _**π**_ + **P** [T] **Ω** _[−]_ [1] **q** ) _._ (7.4)


Observe that the expression (7.2) for certain views can be recovered from (7.3)
by taking **Ω** = **0** .
We next give a derivation of the formula (7.4) for the posterior estimate of
_**μ**_ when **Ω** is non-singular. The exercises at the end of the chapter show how
the derivation can be tweaked for any **Ω** . Stack the two equations for the market
equilibrium _**π**_ = _**μ**_ + _**ϵπ**_, _**ϵπ**_ _∼_ _N_ ( **0** _,_ **Q** ), and for the investor’s views **q** = **P** _**μ**_ + _**ϵ**_ **q**,
_**ϵ**_ **q** _∼_ _N_ ( **0** _,_ **Ω** ) as


**y** = **M** _**μ**_ + _**ϵ**_ _,_ _**ϵ**_ _∼_ _N_ ( **0** _,_ **Σ** )



for




  _**π**_
**y** =
**q**




- **I**
_,_ **M** =
**P**




- - **Q** **0**
_,_ **Σ** = _._
**0** **Ω**



The estimation problem can be stated as the following weighted least-squares
problem:

min ( **y** _−_ **M** _**μ**_ ) [T] **Σ** _[−]_ [1] ( **y** _−_ **M** _**μ**_ ) _._
_**μ**_


The optimality conditions for this problem yield


2 **M** [T] **Σ** _[−]_ [1] **M** _**μ**_ _−_ 2 **M** [T] **Σ** _[−]_ [1] **y** = **0** _._


Hence we obtain


_**μ**_ ˆ = ( **M** [T] **Σ** _[−]_ [1] **M** ) _[−]_ [1] **M** [T] **Σ** _[−]_ [1] **y**

= ( **Q** _[−]_ [1] + **P** [T] **Ω** _[−]_ [1] **P** ) _[−]_ [1] ( **Q** _[−]_ [1] _**π**_ + **P** [T] **Ω** _[−]_ [1] **q** )

= _**π**_ + **QP** [T] ( **PQP** [T] + **Ω** ) _[−]_ [1] ( **q** _−_ **P** _**π**_ ) _._


We end this section with a couple of general remarks.
First we note that the Black–Litterman model can be thought of as an “inverse
optimization problem”: If one views the market equilibrium as the optimum
solution of a portfolio optimization problem, what data would produce this
outcome? In particular, given investor views, what choice of _**μ**_ would best fit the
market equilibrium solution? This leads to the least-squares problem formulated
above, whose solution _**μ**_ ˆ has the expression (7.3) that we just computed. This
“inverse optimization” philosophy was proposed by Bertsimas et al. (2012). It has
the added flexibility of allowing investor views on volatility and market dynamics.
We also note that the analysis in the Black–Litterman model relies heavily
on the assumption that the error term _ϵ_ _∼_ _N_ ( **0** _,_ **Q** ) is normally distributed.
When this is not the case, the Black–Litterman framework is still meaningful
but the analysis is more complex and a closed-form solution like (7.3) does
not usually exist. However, a numerical solution may be possible using the
nonlinear programming algorithms discussed in Chapters 18 and 20 (Kocuk and
Cornu´ejols, 2017).


**7.2** **Shrinkage** **Estimation** 129


**7.2** **Shrinkage** **Estimation**


Another approach to improve the quality of estimated expected returns is based
on _shrinkage_ _estimators._ These types of estimators are rooted in the classical
finding of Stein (1956) that biased estimators may, in a formal fashion, be
superior to the unbiased sample mean. As we detail below, the central idea
is that the estimation can be improved by _shrinking_ the sample mean towards a
target. The non-technical article of Efron and Morris (1977) gives an enlightening
discussion of an application of this approach to the estimation of baseball batting
averages.
To formalize ideas, consider the problem of estimating the mean of an _N_      dimensional multivariate normal variable **r** _∼_ _N_ ( _**μ**_ _,_ **V** ) from a set of observations
**r** 1 _, . . .,_ **r** _T_ . For a given estimate _**μ**_ ˆ, consider the quadratic loss function


_L_ (ˆ _**μ**_ _,_ _**μ**_ ) := ( _**μ**_ _−_ _**μ**_ ˆ ) [T] **V** _[−]_ [1] ( _**μ**_ _−_ _**μ**_ ˆ ) _._ (7.5)


For a given loss function, the _risk_ of an estimator is E( _L_ (ˆ _**μ**_ _,_ _**μ**_ )), where the expectation is taken over the space of samples **r** 1 _, . . .,_ **r** _T_ . An estimator is _inadmissible_
if there exists another estimator with lower risk.
For the quadratic loss function (7.5) and _N_ = 1 _,_ 2, it is known that the optimal
estimator is the sample mean ¯ **r** := (1 _/T_ )( **r** 1 + _· · ·_ + **r** _T_ ). By contrast, for _N_ _>_ 2,
the _James–Stein_ shrinkage estimator


_**μ**_ ˆ _JS_ := (1 _−_ _w_ )¯ **r** + _w μ_ 0 **1**


has lower risk than the sample mean ¯ **r** for




   _N_ _−_ 2
_w_ = min 1 _,_
_T_ (¯ **r** _−_ _μ_ 0 **1** ) [T] **V** (¯ **r** _−_ _μ_ 0 **1** )





_._



Here _T_ is the number of observations, and _μ_ 0 is an arbitrary number. The vector
_μ_ 0 **1** and the weight _w_ are referred to as the _shrinkage_ _target_ and _shrinkage_
_factor_ respectively. Although some choices of _μ_ 0 are better than others, what is
surprising is that in theory _μ_ 0 could be any fixed number. This fact is called the
_Stein_ _paradox_ .
The James–Stein shrinkage estimator can be seen as a combination of two
estimators:


(1) an estimator with little or no structure (like the sample mean);

(2) an estimator with a lot of structure (the shrinkage target).


The exact combination of these two estimators is determined by a certain _shrink-_
_age_ _intensity_ . As we discuss below, this same shrinkage approach has been
successfully applied to obtain improved estimators of covariance matrices and
beta exposures.
The following shrinkage estimator proposed by Jorion (1986) is fairly popular
in the financial literature. The estimator was derived via an empirical Bayesian


130 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**


approach. As a shrinkage target, use the vector _μ_ 0 **1** for

_μ_ 0 := [¯] **[r]** [T] **[V]** _[−]_ [1] **[1]**

**1** [T] **V** _[−]_ [1] **1** _[,]_


and as a shrinkage intensity, use


_N_ + 2
_w_ :=
_N_ + 2 + _T_ (¯ **r** _−_ _μ_ 0 **1** ) [T] **V** _[−]_ [1] (¯ **r** _−_ _μ_ 0 **1** ) _[.]_


Shrinkage can also be applied to other estimation problems. For instance,
Ledoit and Wolf (2003, 2004) propose shrinkage approaches for covariance estimation in the same spirit as the James–Stein shrinkage estimator: shrink the
sample covariance matrix **V** [¯] (an unstructured estimator) towards a highly structured target estimator **V** 0:


**V** ˆ _LW_ := (1 _−_ _w_ ) ¯ **V** + _w_ **V** 0 _._


The shrinkage target estimator **V** 0 could be a single-factor estimator, an estimator of the covariance matrix with constant correlation, a diagonal matrix, or
a multiple of the identity matrix.
Shrinkage is also routinely used for estimating benchmark exposures in a
stock universe. Let _ri,_ _i_ = 1 _, . . ., N_, denote the excess returns of stocks in the
investment universe and _rB_ denote the excess return of the benchmark. Recall
that the beta of stock _i_ captures the benchmark portion of the return on stock
_i_ via the linear model


_ri_ = _βirB_ + _θi._


The value of _βi_ is the benchmark exposure of stock _i_ . Given historical realizations
of _ri_, for _i_ = 1 _, . . ., N_, and _rB_, we can obtain estimates _β_ [ˆ] _i_ of _βi_ for _i_ = 1 _, . . ., N_
via ordinary least-squares linear regression. The forecasts given by these natural
estimators tend to overestimate the betas of stocks with high benchmark exposure and underestimate the betas of the stocks with low benchmark exposure.
Improved forecasts can be obtained by shrinking the betas obtained from the
least-squares procedures towards one (the benchmark beta):


_**β**_ ˆ = (1 _−_ _w_ )¯ _**β**_ + _w_ **1** _,_


where _**β**_ [¯] denotes the vector of beta estimates from the least-squares procedure.
A common rule of thumb in the above shrinkage estimators of covariance
matrix and vector of betas is to use a shrinkage intensity _w_ = 1 _/_ 2 for estimates based on 60-month long historical data. A thorough discussion on the
appropriate choice of shrinkage intensity can be found in Ledoit and Wolf (2003,
2004) and Blume (1975). Portfolio optimization can be viewed as a stochastic
optimization problem (see Chapter 10). Shrinkage is relevant in this more general
context as well (Davarnia and Cornu´ejols, 2017).
The exercises at the end of this chapter suggest some computational experiments that illustrate the effectiveness of shrinkage estimators.


**7.3** **Resampled** **Efficiency** 131


**7.3** **Resampled** **Efficiency**


A different approach to address the sensitivity of mean–variance optimization to
estimation error is to apply the _bootstrap technique_ from statistics. The bootstrap
technique is a method to estimate standard errors and confidence intervals of
statistics of a dataset via random resampling from the dataset with replacement.

The application of bootstrapping to mean–variance optimization was initially
explored by Jorion (1992) and later further developed and marketed by Michaud
and Michaud (2008). The basic idea is to consider the joint problem of parameter
estimation and portfolio construction as a statistical procedure: the efficient portfolios can be seen as a statistic on a set of financial data used for estimation. The
_resampled_ _efficiency_ technique proposed by Michaud and Michaud proceeds by
applying bootstrapping to this statistical process. Suppose there is a procedure
that estimates the vector of expected returns and covariance from historical
data. Use the available data to produce these estimates and compute efficient
portfolios. Repeat this same process either by sampling from these estimates, or
by bootstrapping the available data to obtain new estimates of expected returns
and covariances. All these estimates are statistically equivalent. For each of them,
we can generate the corresponding set of efficient portfolios. The collection of all
of these portfolios forms some sort of _equivalence_ _region._ We would like to take
some average of the equivalence region so that the effects of estimation error
are mitigated. However, it is not obvious how to average since the equivalence
region contains portfolios with low and high variance. We do not want to mix
“apples and oranges”. Michaud and Michaud’s suggestion is to average portfolios
that are in some equivalent risk-return bucket. To that end, we propose the
following procedure: For each efficient frontier, save _m_ evenly distributed efficient
portfolios. Rank them 1 to _m_ . Then take averages of same-rank portfolios from
all efficient frontiers.

This resampling procedure can be more precisely described as follows (see
Algorithm 7.1). Suppose we have a procedure to produce estimates _**μ**_ ˆ and **V** [ˆ]
from a history of _T_ periods of historical data.


**Algorithm** **7.1** Resampling procedure

1: **for** _i_ = 1 _, . . ., S_ **do**

2: simulate a new history of _T_ periods by resampling the original history

3: use the simulated history to generate new estimates _**μ**_ ˆ _i_ and **V** [ˆ] _i_
4: use _**μ**_ ˆ _i_ and **V** [ˆ] _i_ to generate _m_ equally spaced efficient portfolios
**x** 1 _,i, . . .,_ **x** _m,i_
5: **end** **for**


To generate the _resampled_ _efficient_ _portfolios_, take averages of equally ranked


132 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**


efficient portfolios generated above:



**x** _j,_ resampled := [1]

_S_




- _S_

**x** _j,i._

_i_ =1



The _resampled_ _efficient_ _frontier_ is the expected return versus standard deviation
chart of the resampled efficient portfolios with the original estimates _**μ**_ ˆ and **V** [ˆ] .
There are a number of limitations to resampling (Scherer, 2002). The entire
process is only a heuristic; there is no sound theory to support why the process
should mitigate the effects of estimation error. The methodology does have the
feature of generating portfolios that look well diversified, and this is generally
well received. However, this feature can be attributed to the role of variability
in the averaging process. The process is intense computationally, as it multiplies
the work involved in conventional mean–variance optimization. Furthermore, the
procedure does not provide any clear mechanism to facilitate the incorporation
of views as in the Black–Litterman model.


**7.4** **Robust** **Optimization**


Robust optimization is a fairly recent development that considers uncertainty in
some parameters directly in the optimization problem. The general idea of robust
optimization is to generate a solution that is _good_ for _all_ possible realizations
of the uncertain parameters. Consider a minimization problem with inequality
constraints
min _f_ ( **x** _,_ **p** )
**x** (7.6)

s.t. _gi_ ( **x** _,_ **p** ) _≤_ 0 _,_ _i_ = 1 _, . . ., m._


Here the vector **p** stands for some parameters that define the objective and
constraints functions.
Consider first the case when the uncertain parameters occur in the constraints
only. Assume that the set of parameters **p** is uncertain but it is known to be in
some uncertainty set _U_ . In this case a _robust_ version of (7.6) is one where the
optimization is performed over points that are feasible for all possible realizations
of the uncertain parameters **p** _∈U_ ; that is,


min _f_ ( **x** )
**x**

s.t. max _[i]_ [ = 1] _[, . . ., m.]_
**p** _∈U_ _[g][i]_ [(] **[x]** _[,]_ **[ p]** [)] _[ ≤]_ [0] _[,]_


On the other hand, consider the case when the uncertain parameters occur in
the objective only. In this case a robust version of (7.6) is one that finds the
solution that would be best, given the worst possible realization of the uncertain
parameters **p** _∈U_ ; that is,


min _f_ ( **x** _,_ **p** )
**x** [max] **p** _∈U_

s.t. _gi_ ( **x** ) _≤_ 0 _,_ _i_ = 1 _, . . ., m._


**7.5** **Other** **Diversification** **Approaches** 133


If uncertain parameters occur in both the objective and constraints, then the
robust version is as follows:


min _f_ ( **x** _,_ **p** )
**x** [max] **p** _∈U_

s.t. max _[i]_ [ = 1] _[, . . ., m.]_
**p** _∈U_ _[g][i]_ [(] **[x]** _[,]_ **[ p]** [)] _[ ≤]_ [0] _[,]_


As we detail in Chapter 19, for suitable types of uncertainty sets the above robust
versions can be rewritten as an optimization problem that is manageable albeit
via more involved optimization machinery.


**7.5** **Other** **Diversification** **Approaches**


The challenges associated with expected return estimation and the input sensitivity of mean–variance models have given rise to quantitative portfolio construction
approaches that eschew expected return estimation and focus on managing risk
only. We next discuss some popular approaches of this kind that have led to
the development of a variety of investment products in the asset management
industry.
Assume **V** is the covariance matrix of asset returns in some investment universe
and _**σ**_ is the vector of volatilities (standard deviations) of the asset returns. In
particular, the diagonal entries of **V** are the squares of the entries of _**σ**_ _._
The _minimum-risk_ portfolio is the portfolio in the efficient frontier of minimum
variance. In the absence of constraints, this portfolio is the solution to the
following quadratic programming model:


min **x** [T] **Vx**
**x**

s.t. **1** [T] **x** = 1 _._


That is,


1
**x** _[∗]_ =
**1** [T] **V** _[−]_ [1] **1** **[V]** _[−]_ [1] **[1]** _[.]_


For the special case **V** = **I** (the _N_ _×_ _N_ identity matrix) the minimum-risk
portfolio is the so-called _equally_ _weighted_ _portfolio_

_x_ _[∗]_ _i_ [=] [1] _i_ = 1 _, . . ., N,_

_N_ _[,]_


where _N_ is the number of assets in the universe.
On the other hand, if **V** is diagonal, that is, **V** = diag( _**σ**_ ) [2], then the portfolio
components are proportional to the inverse of the squares of the volatilities:

_x_ _[∗]_ _i_ [=] ~~�~~ _N_ 1 _/σi_ [2] _,_ _i_ = 1 _, . . ., N._
_i_ =1 [1] _[/σ]_ _i_ [2]


In particular, this portfolio is the _value-weighted_ _portfolio_ if the capitalization of
asset _i_ is used as a proxy for 1 _/σi_ [2][.]


134 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**



We next discuss two more recent diversification approaches, namely _risk parity_
and _maximum_ _diversification._ To that end, we first discuss the related concept
of _risk_ _contribution._ Observe that the risk (standard deviation) of a portfolio
**x** = ( _x_ 1 _, . . ., xN_ ) is given by



_√_
_σP_ ( **x** ) =



**x** [T] **Vx** _._



If we compute the partial derivative of this portfolio with respect to _xi_, we obtain
the _marginal_ _contribution_ _to_ _risk_ of asset _i_ :



_MCRi_ ( **x** ) = _[∂σ][P]_ [ (] **[x]** [)]




_[P]_ [ (] **[x]** [)] = ~~_√_~~ ( **Vx** ) _i_

_∂xi_ **x** [T]



_,_ _i_ = 1 _, . . ., N._
**x** [T] **Vx**



The _contribution_ _to_ _risk_ of asset _i_ is:

_CRi_ ( **x** ) = _xi · MCRi_ ( **x** ) = _[x]_ ~~_√_~~ _[i][ ·]_ [ (] **[Vx]** [)] _[i]_ _,_ _i_ = 1 _, . . ., N._

**x** [T] **Vx**



Observe that

    - _N_



**x** [T] **Vx** = _σP_ ( **x** ) _._




- _N_ ~~_√_~~

_CRi_ ( **x** ) =

_i_ =1



Consequently, we say that **x** is a _risk-parity_ portfolio if all the assets in the
portfolio have the same contribution to risk; that is, if

_CRi_ ( **x** ) = _[σ][P]_ [ (] **[x]** [)] _,_ _i_ = 1 _, . . ., N._

_N_

Again, in the special case when **V** = diag( _**σ**_ ) [2], the fully invested risk-parity
portfolio is

1 _/σi_
_x_ _[∗]_ _i_ [=] ~~�~~ _N_ _,_ _i_ = 1 _, . . ., N._
_i_ =1 [1] _[/σ][i]_


For a general covariance matrix **V** and portfolio constraints, it may not be
possible to attain perfect risk parity. In this case, we can instead minimize some
kind of measure of _deviation from risk parity._ Here are some choices for examples
of these kinds of measures proposed in the literature:




- _N_

( _xi ·_ ( **Vx** ) _i −_ _xj_ _·_ ( **Vx** ) _j_ ) [2]

_j_ =1



_DRP_ 1( **x** ) =




- _N_


_i_ =1




_xi ·_ ( **Vx** ) _i_

_−_ [1]
**x** [T] **Vx** _N_



_DRP_ 2( **x** ) =




- _N_


_i_ =1



_N_



_xi ·_ ( **Vx** ) _i_
����

[T]



_DRP_ 3( **x** ) =




- _N_


_i_ =1



_·_ ( **Vx** ) _i_

_−_ [1]
**x** [T] **Vx** _N_



�2


_._
����



The optimization problem associated with minimizing any of these deviation
measures is in general quite a bit more challenging than other mean–variance
models, as these problems are not convex. The development of efficient numerical


**7.6** **Exercises** 135


algorithms to solve these kinds of optimization problems is a topic of current
research.
Another approach to diversification is _maximum_ _diversification_ (Choueifaty
and Coignard, 2008). More precisely, maximize the diversification ratio


_**σ**_ [T] **x**
~~_√_~~ _,_

**x** [T] **Vx**


where _**σ**_ is the vector of asset volatilities. A motivation for this approach can
be given as follows: Observe that the diversification ratio is proportional to
the Sharpe ratio if _**μ**_ is proportional to _**σ**_ _._ Hence maximizing diversification
is equivalent to maximizing the Sharpe ratio under the assumption that the
expected returns of the assets are proportional to their volatilities.
In the absence of other constraints, the fully invested maximum diversification
portfolio is the solution to the optimization problem


_**σ**_ [T] **x**
min ~~_√_~~
**x** **x** [T] **Vx** (7.7)

s.t. **1** [T] **x** = 1 _._


In the special case when **V** = diag( _**σ**_ ) [2], the solution to (7.7) coincides with the
fully invested risk-parity portfolio:


1 _/σi_
_x_ _[∗]_ _i_ [=] ~~�~~ _N_ _,_ _i_ = 1 _, . . ., N._
_i_ =1 [1] _[/σ][i]_


**7.6** **Exercises**


**Exercise** **7.1** The purpose of this exercise is to provide a derivation of the
Black–Litterman posterior formula.



(a) Consider the case when views are certain; that is, when **Ω** = **0** . In this case
if we stack the equations for the prior and for the views we get

           -           -           -           _**π**_ **q** = _**μ**_ + **P** _**μ ϵπ**_ _,_ _**ϵπ**_ _∼_ _N_ ( **0** _,_ **Q** ) _._




- = _**μ**_ + _**ϵπ**_
**P** _**μ**_




_,_ _**ϵπ**_ _∼_ _N_ ( **0** _,_ **Q** ) _._



The estimation problem can then be stated as the following constrained
weighted least-squares problem:


min ( _**π**_ _−_ _**μ**_ ) [T] **Q** _[−]_ [1] ( _**π**_ _−_ _**μ**_ )
_**μ**_

s.t. **P** _**μ**_ = **q** _._


(i) Write down the optimality conditions for this constrained problem.

(ii) Show that after solving the optimality conditions we obtain


_**μ**_ ˆ = _**π**_ + **QP** [T] ( **PQP** [T] ) _[−]_ [1] ( **q** _−_ **P** _**π**_ ) _._


136 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**


                   -                    (b) Now consider the case **Ω** = **Ω0** 11 **00** _,_ where **Ω** 11 is non-singular. This

corresponds to the case when the views can be split in two blocks and the
second block of views are certain:




   -   -   **P** 1 _**μ**_ **q** 1 + _**ϵ**_ 1
**P** _**μ**_ = =
**P** 2 _**μ**_ **q** 2




_,_ _**ϵ**_ 1 _∼_ _N_ ( **0** _,_ **Ω** 11) _._



In this case if we stack the equations for the prior and for the views we
get
⎡ ⎤ ⎡ ⎤



⎡





_._




- **Q** **0**
_∼_ _N_ ( **0** _,_ **Σ** ) _,_ **Σ** =
**0** **Ω** 11



_**π**_
⎣ **q** 1
**q** 2



⎤



⎤




  ⎦ _,_ _**ϵπ**_
_**ϵ**_ 1



⎦ =



_**μ**_ + _**ϵπ**_
⎣ **P** 1 _**μ**_ + _**ϵ**_ 1
**P** 2 _**μ**_



The estimation problem can then be stated as the following constrained
weighted least-squares problem:



�T - _**π**_ _−_ _**μ**_
**Σ** _[−]_ [1]
**q** 1 _−_ **P** 1 _**μ**_



min
_**μ**_




_**π**_ _−_ _**μ**_
**q** 1 _−_ **P** 1 _**μ**_



s.t. **P** 2 _**μ**_ = **q** 2 _._


(i) Write down the optimality conditions for this constrained problem.

(ii) Show that after solving the optimality conditions we obtain


_**μ**_ ˆ = _**π**_ + **QP** [T] ( **PQP** [T] + **Ω** ) _[−]_ [1] ( **q** _−_ **P** _**π**_ ) _._


(c) *Reduce the case when **Ω** is a general covariance matrix to the case discussed in step (b). To that end, use the following fact from matrix algebra:
if **Ω** is symmetric and positive semidefinite, then there exists an orthogonal
matrix **U** and a diagonal matrix **Λ** with non-negative entries such that
**Ω** = **UΛU** [T] . Use **U** to make a _change_ _of_ _variables_ so as to write the views
as in step (b) and conclude that the expression (7.3) for the posterior _**μ**_ ˆ
holds.


**Exercise** **7.2** The purpose of this exercise is to explore the effect of estimation error on the computation of efficient portfolios by comparing the “true”,
“estimated”, and “actual” efficient frontiers. To that end, assume the expected
return and covariance matrix in the Excel spreadsheet “Exercise 7.2 & 7.3 Eight
Assets” are the “true” values for the expected returns and covariances for a set
of eight assets. These are _monthly_ expected returns and covariances.
Next, using these “true” values and assuming a multivariate normal distribution for the returns, generate monthly returns for ten years. You may find the
MATLAB multivariate normal random number generator mvnrnd useful for this
purpose.


(a) Compute the sample mean and the sample covariance matrix of the returns
you generated.


**7.6** **Exercises** 137


(b) Compute at least ten long-only efficient portfolios along the efficient frontier
based on the estimates found in part (a). Choose efficient portfolios whose
expected returns range from that of the long-only minimum-variance portfolio to that of the long-only portfolio with maximum expected returns. Save
these efficient portfolios.

(c) Now compute the “actual” expected returns and standard deviations for the
portfolios found in step (b). These are the values of true expected returns
and standard deviation of these portfolios.

(d) On the same figure plot the “estimated” efficient frontier found in (b), the
“actual” frontier from step (c), and the “true” frontier (the one we would
get if we used the true parameters).

(e) Repeat the above steps (generate a ten-year history, estimate, compute efficient portfolios) a few times. What do you observe?


**Exercise 7.3** The Excel spreadsheet “Exercise 7.2 & 7.3 Eight Assets” provides
monthly expected returns and covariance matrix for eight asset classes.


(a) Find the long-only portfolio with maximum Sharpe ratio, assuming a zero
risk-free interest rate.

(b) Assume your initial portfolio is equally divided among the eight asset classes.
Repeat step (a) but under the additional restriction that the two-sided
turnover is at most 60%.

(c) Assume the benchmark is an equally divided portfolio and the risk-free
interest rate is zero. Find the vector of equilibrium returns _**π**_ .

(d) Suppose an investor has the following two views:

View 1: the return on Euro bonds will be 0.40%.

View 2: the return on an equally weighted portfolio of USA and UK stocks
will be 1.2%.

Use the Black–Litterman model to merge these views with the equilibrium
returns. Assume the investor has total confidence in the views.


**Exercise** **7.4** Consider the problem of finding the _maximum_ _diversified_ fully
invested portfolio in a universe of _n_ risky assets:


_**σ**_ [T] **x**
max ~~_√_~~
**x** **x** [T] **Vx**


s.t. **1** [T] **x** = 1 _._


Here _**σ**_ is the vector of assets volatilities and **V** is the covariance matrix.


(a) Show that the maximum diversified portfolio (i.e., the solution to the above
problem) is


1
**x** _MD_ :=
**1** [T] **V** _[−]_ [1] _**σ**_ _[·]_ **[ V]** _[−]_ [1] _**[σ]**_ _[.]_


138 **Sensitivity** **of** **Mean–Variance** **Models** **to** **Input** **Estimation**


(b) Use part (a) to show that


**x** _MD_ := _[σ]_ _MD_ [2] _·_ **V** _[−]_ [1] _**σ**_ _,_
_σA_


where _σMD_ and _σA_ are respectively the volatility of **x** _MD_ and the weighted
average volatility of the assets in **x** _MD_ . In other words,


_σMD_ [2] [=] **[ x]** _MD_ [T] **[Vx]** _[MD][,]_ _σA_ = _**σ**_ [T] **x** _MD._


(c) Suppose the covariance matrix has the following _constant-correlation_ form:
For some _ρ ∈_ (0 _,_ 1)


**V** _ii_ = _σi_ [2] _[,]_ **[V]** _[ij]_ [=] _[ ρσ][i][σ][j][,]_ [for] _[i]_ [ = 1] _[, . . ., n,]_ [and] _[j]_ [= 1] _[, . . ., n,]_ [with] _[i][ ̸]_ [=] _[ j.]_


In matrix form, we can write the above constant-correlation matrix as follows:


**V** = _ρ_ _**σσ**_ [T] + (1 _−_ _ρ_ )Diag( _**σ**_ ) [2] _,_


where _**σ**_ is the vector with components _σi,_ _i_ = 1 _, . . ., n_ .


Show that in this case the holdings of the maximum diversified portfolio
**x** _MD_ are given by


1
_xi_ = ~~�~~ _ni_ =1 [1] _[/σ][i]_ _·_ _σ_ [1] _i_ _,_ _i_ = 1 _, . . ., n._


**Exercise** **7.5** The purpose of this exercise is to visualize how the covariance
matrix gets distorted when it is estimated using a finite set of observations. The
exercise also explores how a shrinkage technique of Ledoit and Wolf can mitigate
this kind of distortion.


(a) Assume _n_ = 10 assets have returns that follow a multivariate normal distribution with expected returns equal to zero and _true_ covariance matrix equal
to the _n × n_ diagonal matrix



0 _._ 8
0 _._ 85
...

1 _._ 2
1 _._ 25



⎤


_._
⎥⎥⎥⎥⎥⎦



**V** =



⎡

⎢⎢⎢⎢⎢⎣



(The diagonal entries are equally spaced at 0.05 intervals.)


Generate _T_ = 120 samples **r** _t,_ _t_ = 1 _, . . ., T_, from this joint distribution.
Each of these samples **r** _t_ _∈_ R [10] is drawn from the ten-dimensional multivariate normal distribution _N_ ( **0** _,_ **V** ). You may find the MATLAB multivariate
normal random number generator mvnrnd useful for this purpose.


**7.6** **Exercises** 139


(i) Use the _T_ samples to estimate the sample covariance matrix **V** [ˆ] as
follows. Let ¯ **r** := (1 _/T_ ) [�] _[T]_ _t_ =1 **[r]** _[t][,]_ **[z]** _[t]_ [:=] **[ r]** _[t][ −]_ [¯] **[r]** _[,]_ _[t]_ [ = 1] _[, . . ., T,]_ [and]



**V** ˆ := [1]

_T_




- _T_

**z** _t_ **z** [T] _t_ _[.]_
_t_ =1



Plot the eigenvalues both of the true covariance matrix **V** and of the
estimated covariance **V** [ˆ] on the same plot. Do you observe anything
peculiar?
(ii) Using the estimated covariance **V** [ˆ] find the estimated minimum-risk fully
invested portfolio **x** ˆ. Compute the _estimated_ minimum variance **x** ˆ [T][ ˆ] **Vx** ˆ,
the _actual_ minimum variance **x** ˆ [T] **Vx** ˆ, and the _true_ minimum variance
( **x** _[∗]_ ) [T] **Vx** _[∗]_, where **x** _[∗]_ is the true minimum-risk fully invested portfolio
for **V** . What do you observe?
(iii) Repeat parts (i) and (ii) several times (anywhere from a handful to a
few thousand times). What do you observe?
(b) We will next apply the shrinkage technique of Ledoit and Wolf. To that end,
let _λi,_ _i_ = 1 _, . . ., n_, denote the eigenvalues of the sample covariance matrix
**V** ˆ and _λ_ ¯ := (1 _/n_ ) [�] _[n]_ _i_ =1 _[λ][i]_ [.] [Define] **[C]** [ :=] _[λ]_ [¯] **[I]** [and]




- _T_



trace(( **z** _t_ **z** [T] _t_ _[−]_ **[V]** [ˆ] [)][2][)]
_t_ =1



⎞


⎟
⎟
⎟⎟ _._
⎠



1
_T_



_,_ 1
trace(( **V** [ˆ] _−_ **C** ) [2] )



_α_ := min



⎛


⎜
⎜
⎜
⎜
⎝



1
_T_ _[·]_



Finally consider the shrunken matrix


**V** ¯ := (1 _−_ _α_ ) ˆ **V** + _α_ **C** _._


(i) Plot the eigenvalues of the true covariance matrix **V**, of the sample
covariance **V** [ˆ], and of the shrunken covariance **V** [¯] on the same plot.
What do you observe now?
(ii) Using the shrunken covariance **V** [¯] find the estimated minimum-risk fully
invested portfolio **x** ¯. Compute the _estimated_ minimum variance **x** ¯ [T][ ¯] **Vx** ¯,
the _actual_ minimum variance **x** ¯ [T] **Vx** ¯, and the _true_ minimum variance
( **x** _[∗]_ ) [T] **Vx** _[∗]_, where **x** _[∗]_ is the true minimum-risk fully invested portfolio
for **V** . What do you observe? Are the results any different from part
(a)(ii)?
(iii) Repeat parts (i) and (ii) several times (anywhere from a handful to a
few thousand times). What do you observe? Are the results any different
from part (a)(iii)?


## 8 Mixed Integer Programming: Theory and Algorithms

**8.1** **Mixed** **Integer** **Programming**


The types of optimization models that we have discussed so far, namely linear
and quadratic programming, allow variables to take a continuum of values. In
particular, the numerical solutions to these kinds of models may have fractional
values. For instance, the solution to a portfolio construction model could suggest
a plan to purchase 3205.76 shares of stock XYZ. In many cases it is natural to
round this value and to interpret it as a suggestion to purchase 3205 or even
3200 shares of stock XYZ. However, if a variable in an optimization model is
associated with choosing among two or more alternatives, for example, as in the
capital budgeting problem described below, then a model that suggests taking
fractions of each of the alternatives would be of limited value. Instead, a _binary_
decision, namely “to choose” or “not to choose”, needs to be made for each
alternative.
In general, an _integer_ _variable_ in an optimization model is a variable that is
restricted to take integer values only. A _mixed_ _integer_ _program_ is an optimization
problem with the constraint that some of the variables must take integer values.
In particular a _mixed_ _integer_ _linear_ _program_ is a problem of the form


min **c** [T] **x**
**x**



s.t. **Ax** = **b**
**Dx** _≥_ **d**
_xj_ _∈_ Z _,_ _j_ _∈_ _J_



(8.1)



for some vectors **c** _∈_ R _[n]_, **b** _∈_ R _[m]_, **d** _∈_ R _[p]_, matrices **A** _∈_ R _[m][×][n]_, **D** _∈_ R _[p][×][n]_, and
subset _J_ _⊆{_ 1 _, . . ., n}_ of the variables. When all variables are restricted to be
integer, that is, when _J_ = _{_ 1 _, . . ., n}_, the problem (8.1) is called a _pure_ _integer_
_linear_ _program_ .
An important case occurs when a model includes _binary_ variables; that is,
variables that are restricted to take the value 0 or 1. When all the variables in
a mixed integer program are of this kind, it is called a _binary_ _program_ . As the
examples below show, binary variables enable the modeling of important realistic
features such as logical constraints, cardinality and threshold constraints, and
others. However, this improvement in modeling power comes with a tradeoff in
computational cost. The presence of a significant number of integer variables in


**8.1** **Mixed** **Integer** **Programming** 141


an optimization problem can make it extremely difficult or impossible to solve
unless there is a specific exploitable structure.


**Example 8.1** (Capital budgeting) Suppose we have a capital of 19 million dollars
for long-term investment and have identified four investment opportunities with
the following investment requirements and net present values (in million dollars):


Investment 1 Investment 2 Investment 3 Investment 4


Required investment 7 10 6 3
Net present value 9 11 7 4


What investments should we choose to maximize our total net present value?
Each investment is a “take it or leave it” opportunity: the investment must be
funded entirely or not at all.


This problem can be formulated as the following binary linear programming
model.


_Binary_ _linear_ _programming_ _model_ _for_ _capital_ _budgeting_

**Variables:**

     1 if investment _i_ is undertaken
_xi_ = 0 otherwise for _i_ = 1 _, . . .,_ 4 _._


**Objective,** **in** **millions** **of** **dollars:**


max 9 _x_ 1 + 11 _x_ 2 + 7 _x_ 3 + 4 _x_ 4


**Constraints:**


7 _x_ 1 + 10 _x_ 2 + 6 _x_ 3 + 3 _x_ 4 _≤_ 19 (budget constraint)
_xi_ _∈{_ 0 _,_ 1 _}_ for _i_ = 1 _, . . .,_ 4 (binary variables).


The optimal solution to the _linear_ _programming_ _relaxation_ of this model,
obtained by _relaxing_ the binary constraints _xi_ _∈{_ 0 _,_ 1 _}_, for _i_ = 1 _, . . .,_ 4, to
0 _≤_ _xi_ _≤_ 1, for _i_ = 1 _, . . .,_ 4, is



⎤


_._
⎥⎥⎦



**x** _[∗]_ =



⎡

1
0 _._ 3

⎢⎢⎣ 1

1



This is not a feasible solution as _x_ _[∗]_ 2 [is] [not] [binary.] [If] [we] [round] _[x][∗]_ 2 [to] [0] [we] [get] [a]
feasible solution. However, a better (and in fact the optimal) solution is



⎤

0
1

_._

1⎥⎥⎦
1



**x** _[∗]_ =



⎡

⎢⎢⎣


142 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


This could be counterintuitive as Investment 1 has the best “bang for the buck”;
that is, has the highest ratio of net present value to investment requirement.
The presence of binary variables also readily enables the modeling of logical
restrictions. For example, the logical restriction


If Investment 2 is made then Investment 4 must also be made


can be modeled via the constraint


_x_ 2 _≤_ _x_ 4 _._


Similarly, the logical constraint


If Investment 1 is made then Investment 3 must not be made


can be modeled via the constraint


_x_ 1 + _x_ 3 _≤_ 1 _._


**Example** **8.2** (Clustering) Clustering is a popular technique in data analysis.
It is concerned with partitioning a collection of objects into subsets or “clusters”
so that the objects within each cluster are more closely related with each other
than with objects assigned to different clusters. Suppose we wish to partition a
collection of _N_ objects into _K_ _<_ _N_ clusters based on some kind of similarity
measure:


_ρij_ = similarily measure between objects _i, j._


To give a financial flavor to this example, assume the objects to be clustered are
_N_ stocks and the similarity measure _ρij_ is the correlation between the returns
of stocks _i_ and _j_ .


We next describe a possible approach to the above clustering problem via
binary programming. This approach is closely related to the popular _K_ -median
problem. Before diving into the binary programming formulation, we describe
some of the main ideas. Assume the objects are indexed 1 _, . . ., N_ and are to
be partitioned into the _K_ clusters _C_ 1 _, . . ., CK_ . A key idea is to designate an
element _jℓ_ in each cluster _Cℓ_ as the _centroid_ of cluster _Cℓ_ . This choice suggests
the following natural measure of the similarity within cluster _Cℓ_ :

       
_ρi,jℓ_
_i∈Cℓ_


and in turn it gives the following overall measure of the quality of the clusters
_C_ 1 _, . . ., CK_ :




- _K_


_ℓ_ =1





_ρi,jℓ_ _._
_i∈Cℓ_



The following crucial observation is key in our formulation. The centroid _jℓ_
_represents_ the elements in cluster _Cℓ_ . Indeed, each cluster contains precisely the
objects assigned to its centroid, and the clusters are completely determined by


**8.2** **Numerical** **Mixed** **Integer** **Programming** **Solvers** 143


the choice of the centroids. These ideas are formalized in the following binary
linear programming model.



_Binary_ _linear_ _programming_ _model_ _for_ _clustering_
**Variables:**




  1 if _j_ is a centroid
_yj_ = 0 otherwise for _j_ = 1 _, . . ., N._




  1 if _i_ is represented by _j_
_xij_ = 0 otherwise for _i, j_ = 1 _, . . ., N._



**Objective:**


**Constraints:**


 - _N_




- _N_

_ρijxij._

_i_ =1



max




- _N_


_j_ =1



_yj_ = _K_ (choose _K_ centroids)

_j_ =1

   - _N_

_xij_ = 1 _,_ for _i_ = 1 _, . . ., N_ (each object must be
_j_ =1 represented by one centroid)
_xij_ _≤_ _yj,_ for _i, j_ = 1 _, . . ., N_ ( _i_ is represented by _j_
only if _j_ is a centroid)
_xij, yj_ _∈{_ 0 _,_ 1 _}_ for _i, j_ = 1 _, . . ., N_ (binary variables).


Another correct formulation is obtained if we replace the third set of _N_ [2]

constraints


_xij_ _≤_ _yj,_ for _i, j_ = 1 _, . . ., N_


with the set of _N_ constraints


     - _N_

_xij_ _≤_ _Nyj,_ for _j_ = 1 _, . . ., N._

_i_ =1


**8.2** **Numerical** **Mixed** **Integer** **Programming** **Solvers**


Excel Solver


The steps required for solving a mixed integer (or binary) linear program in
Excel Solver are nearly identical to those for solving linear programs. The only
new step is to state that some variables are integer (or binary).
Figure 8.1 displays a printout of an Excel spreadsheet implementation of the
binary linear programming model for Example 8.1 as well as the dialog box
obtained when we run the Excel add-in Solver. The spreadsheet model contains the three components of the binary program. The decision variables are


144 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


in the range B7:E7. The left-hand side of the budget constraint is in cell B9
and the objective function is in cell B10. The Excel formulas in cells B9 and B10
are SUMPRODUCT(B4:E4,B7:E7) and SUMPRODUCT(B5:E5,B7:E7) respectively. In
addition to these components, notice the constraint


$B$7:$E$7 = binary


in the Solver dialog box.


**Figure** **8.1** Spreadsheet implementation and the Solver dialog box for the capital
budgeting model


MATLAB CVX


Figure 8.2 displays a CVX script for the same problem.


**Figure** **8.2** MATLAB CVX code for capital budgeting model


Using either of these solvers we obtain the optimal solution:



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-156-0.png)

![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-156-1.png)

⎤

0
1

_._

1⎥⎥⎦
1



**x** _[∗]_ =



⎡

⎢⎢⎣


**8.3** **Relaxations** **and** **Duality** 145


**8.3** **Relaxations** **and** **Duality**


A _relaxation_ of an optimization model


min _f_ ( **x** )
**x**

s.t. **x** _∈X_


is another optimization model


min _f_ ˜( **x** )
**x**

s.t. **x** _∈_ _X_ [˜]


that satisfies _X_ _⊆_ _X_ [˜] and _f_ [˜] ( _x_ ) _≤_ _f_ ( _x_ ) for _x ∈X_ . In other words, a relaxation is
a less stringent optimization model obtained by “relaxing” some of the original
constraints and “relaxing” its objective function. Relaxation plays a central role
in a variety of algorithms for solving mixed integer programs. We next describe
two widely used types of relaxations for mixed integer programming, namely
_linear_ _programming_ and _Lagrangian_ relaxations.


8.3.1 Linear Programming Relaxation


The _linear_ _programming_ _relaxation_ of the mixed integer linear program (8.1) is
the linear program obtained by dropping the integrality constraints; that is,


min **c** [T] **x**
**x**

s.t. **Ax** = **b** (8.2)
**Dx** _≥_ **d** _._


Similarly, the linear programming relaxation of a mixed binary linear program


min **c** [T] **x**
**x**



is the linear program



s.t. **Ax** = **b**
**Dx** _≥_ **d**
_xj_ _∈{_ 0 _,_ 1 _},_ _j_ _∈_ _J_


min **c** [T] **x**
**x**

s.t. **Ax** = **b**
**Dx** _≥_ **d**
0 _≤_ _xj_ _≤_ 1 _,_ _j_ _∈_ _J._



(8.3)


(8.4)



The proof of the following proposition is straightforward and we leave it as an
exercise.


**Proposition** **8.3** _Consider_ _the_ _mixed_ _integer_ _program_ (8.1) _and_ _its_ _linear_
_programming_ _relaxation_ (8.2) _._ _Then_ _the_ _following_ _facts_ _hold._


(a) _The_ _optimal_ _value_ _of_ _the_ _relaxation_ (8.2) _is_ _less_ _than_ _or_ _equal_ _to_ _the_ _optimal_
_value_ _of_ _the_ _mixed_ _integer_ _linear_ _program_ (8.1) _._


146 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


(b) _If_ _the_ _relaxation_ (8.2) _is_ _infeasible,_ _then_ _so_ _is_ _the_ _mixed_ _integer_ _linear_ _pro-_
_gram_ (8.1) _._
(c) _If_ _the_ _optimal_ _solution_ **x** _[∗]_ _of_ _the_ _relaxation_ (8.2) _satisfies_ _x_ _[∗]_ _j_ _[∈]_ [Z] _[for]_ _[j]_ _[∈]_ _[J]_
_then_ **x** _[∗]_ _is_ _also_ _an_ _optimal_ _solution_ _to_ _the_ _mixed_ _integer_ _linear_ _program_ (8.1) _._


The analogous facts also hold for the mixed binary linear program (8.3) and
its linear relaxation (8.4). Proposition 8.3 suggests a possible avenue for solving
(8.1): solve the (more tractable) linear programming relaxation (8.2). If this
solution satisfies the relevant integrality constraints, then we have solved (8.1).
If not, the lower bound obtained by solving (8.2) provides valuable information.
For instance, if we can find a feasible solution to (8.1), then the quality of this
solution can be assessed by comparing it with the lower bound obtained from
solving (8.2). The sections below elaborate on this idea. In particular, Section 8.4
sketches algorithms that solve mixed linear integer programs by systematically
solving a sequence of linear programming relaxations.
Proposition 8.3 also leads to the following somewhat counterintuitive conclusion about integer programming formulations. As noted in Example 8.2, there
could be several correct and thus equivalent integer linear programming formulations to a given problem. Among them, it is generally better to have a formulation
with a “tight” linear programming relaxation. Typically, a formulation with more
constraints has a tighter linear programming relaxation and hence might be easier
to solve.


8.3.2 Lagrangian Relaxation


The Lagrangian framework discussed in previous chapters can be extended to
obtain relaxations of an optimization model. The intuitive idea is to obtain a
relaxation of a model by shifting a set of “difficult” constraints to the objective.
To be more precise, consider an optimization problem of the form


min **c** [T] **x**
**x**

s.t. **Ax** = **b** (8.5)
**x** _∈X_ _,_


where the combined set of constraints **Ax** = **b**, **x** _∈X_ is “difficult” but the set of
constraints **x** _∈X_ is “easy”. (We will discuss a concrete example of this situation
in Section 8.3.3.) A relaxation for (8.5) can be obtained as follows. Assume **u** is
a vector of suitable dimension and consider the following problem without the
difficult constraints:


_L_ ( **u** ) := min **c** [T] **x** + **u** [T] ( **b** _−_ **Ax** )
**x** (8.6)

s.t. **x** _∈X_ _._


The problem (8.6) is a _Lagrangian_ _relaxation_ of (8.5). The following proposition
is in the same spirit as Proposition 8.3. Again, its proof is straightforward and
we leave it as an exercise.


**8.3** **Relaxations** **and** **Duality** 147


**Proposition** **8.4** _Consider_ _the_ _optimization_ _problem_ (8.5) _and_ _its_ _Lagrangian_
_relaxation_ (8.6) _for_ _some_ _vector_ **u** _._ _Then_ _the_ _following_ _facts_ _hold._


(a) _The_ _optimal_ _value_ _L_ ( **u** ) _of_ _the_ _relaxation_ (8.6) _is_ _less_ _than_ _or_ _equal_ _to_ _the_
_optimal_ _value_ _of_ (8.5) _._

(b) _If_ _the_ _optimal_ _solution_ **x** _[∗]_ _of_ _the_ _relaxation_ (8.6) _satisfies_ **Ax** _[∗]_ = **b** _then_ **x** _[∗]_

_is_ _also_ _an_ _optimal_ _solution_ _to_ (8.5) _._


The _Lagrangian_ _dual_ of (8.5) is the problem of finding the best Lagrangian
relaxation


max _L_ ( **u** ) _,_
**u**


where _L_ ( **u** ) is the optimal value of (8.6). We note that the function **u** _�→_ _L_ ( **u** )
is concave; that is, **u** _�→−L_ ( **u** ) is convex. Thus the Lagrangian dual is a convex
optimization problem.
The Lagrangian relaxation and Lagrangian dual also extend to problems where
the set of difficult constraints involves both equalities and inequalities. We simply
need to be a bit careful about the sign of the multipliers for the inequality
constraints. Consider the optimization problem


min **c** [T] **x**
**x**



s.t. **Ax** = **b**
**Dx** _≥_ **d**
**x** _∈X_ _._



(8.7)



Given vectors **u** _,_ **v** of suitable dimension with **v** _≥_ **0** we obtain the following
Lagrangian relaxation:


_L_ ( **u** _,_ **v** ) := min **c** [T] **x** + **u** [T] ( **b** _−_ **Ax** ) + **v** [T] ( **d** _−_ **Dx** )
**x** (8.8)

s.t. **x** _∈X_ _._


We have the following extended version of Proposition 8.4.


**Proposition** **8.5** _Consider_ _the_ _optimization_ _problem_ (8.7) _and_ _its_ _Lagrangian_
_relaxation_ (8.8) _for_ _some_ _vectors_ **u** _,_ **v** _with_ **v** _≥_ **0** _._ _Then_ _the_ _following_ _facts_ _hold._


(a) _The_ _optimal_ _value_ _L_ ( **u** _,_ **v** ) _of_ _the_ _relaxation_ (8.8) _is_ _less_ _than_ _or_ _equal_ _to_ _the_
_optimal_ _value_ _of_ (8.7) _._

(b) _If the optimal solution_ **x** _[∗]_ _of the relaxation_ (8.8) _satisfies_ **Ax** _[∗]_ = **b** _,_ **Dx** _[∗]_ _≥_ **d** _,_
_and_ **v** [T] ( **Dx** _[∗]_ _−_ **d** ) = 0 _,_ _then_ **x** _[∗]_ _is_ _also_ _an_ _optimal_ _solution_ _to_ (8.7) _._


The Lagrangian dual of (8.7) is


max _L_ ( **u** _,_ **v** )
**u** _,_ **v**

s.t. **v** _≥_ **0** _._


148 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


8.3.3 A Heuristic based on Lagrangian Relaxation for Clustering


We next describe a particularly successful application of Lagrangian relaxation
for the clustering problem introduced in Example 8.2, namely,




- _N_

_ρijxij_

_j_ =1



_Z_ := max


s.t.




- _N_


_i_ =1

- _N_



_yj_ = _K_

_j_ =1

- _N_

_xij_ = 1 for _i_ = 1 _, . . ., N_

_j_ =1

_xij_ _≤_ _yj_ for _i, j_ = 1 _, . . ., N_
_xij, yj_ _∈{_ 0 _,_ 1 _}_ for _i, j_ = 1 _, . . ., N._



(8.9)



The above model can be solved by general-purpose solvers such as Excel
Solver or CVX, or even commercial solvers like Gurobi or CPLEX, only for relatively small values of _N_ . One of the main difficulties is that the model involves
_N_ [2] + _N_ binary variables and _N_ [2] + _N_ + 1 constraints. For a modest value of
_N_ like _N_ = 100, the model becomes unmanageable if tackled by a standard
solver. At the same time, in practical clustering problem instances _N_ can easily
range in the hundreds or thousands. A heuristic based on Lagrangian relaxation
developed by Cornu´ejols et al. (1977) can compute approximate solutions to (8.9)
for virtually unlimited values of _N_ . We next describe the main ideas behind this
heuristic. Consider the following Lagrangian relaxation to (8.9): given a vector

          - �T
of multipliers **u** = _u_ 1 _· · ·_ _uN_ let




- _N_

_xij_

_j_ =1




- _N_

_ρijxij_ +

_j_ =1




- _N_

_ui_

_i_ =1






1 _−_







_L_ ( **u** ) := max
**x** _,_ **y**


s.t.




- _N_


_i_ =1

- _N_



_yj_ = _K_

_j_ =1

_xij_ _≤_ _yj,_ _i, j_ = 1 _, . . ., N_
_xij, yj_ = 0 or 1 _,_ _i, j_ = 1 _, . . ., N._



(8.10)



This Lagrangian relaxation has moved the “difficult” constraints [�] _[N]_ _j_ =1 _[x][ij]_ [=]
1, with _i_ = 1 _, . . ., N_, to the objective via the multipliers **u** and has kept the
remaining constraints as the “easy” ones. This Lagrangian relaxation satisfies
the following key properties:


**Property** **1:** _L_ ( **u** ) _≥_ _Z_, where _Z_ is the optimal value of (8.9). This is an
immediate consequence of Proposition 8.3.


**8.3** **Relaxations** **and** **Duality** 149


**Property** **2:** For a given **u**, (8.10) is easy to solve. To see this, first notice that




- _N_

( _ρij_ _−_ _ui_ ) _xij_ +

_j_ =1




- _N_

_ui_

_i_ =1



_L_ ( **u** ) := max
**x** _,_ **y**


s.t.




- _N_


_i_ =1

- _N_



_yj_ = _K_

_j_ =1

_xij_ _≤_ _yj,_ _i, j_ = 1 _, . . ., N_
_xij, yj_ _∈{_ 0 _,_ 1 _},_ _i, j_ = 1 _, . . ., N._



Given **y**, this shows that _xij_ should be set to its upper bound _yj_ or to its
lower bound 0, depending on whether the objective coefficient _ρij_ _−_ _ui_
of _xij_ is positive or negative. Therefore _L_ ( **u** ) can be rewritten as




- _N_

_ui_

_i_ =1



_L_ ( **u** ) = max
**y**


s.t.




- _N_

_Cjyj_ +

_j_ =1

- _N_

_yj_ = _K_

_j_ =1



(8.11)



_yj_ _∈{_ 0 _,_ 1 _},_ _j_ = 1 _, . . ., N_


for _Cj_ := [�] _[N]_ _i_ =1 [max(0] _[, ρ][ij]_ _[−]_ _[u][i]_ [)] _[.]_ [Finally,] [observe] [that] [the] [solution] [to]
(8.11) is readily computable: Sort the _Cj_ in decreasing order, say _Cj_ 1 _≥_
_Cj_ 2 _≥· · ·_ _≥_ _CjN_ . The optimal solution to (8.11) is obtained by setting
_y_ �¯ _j_ 1 _K_ = _· · ·_ = _y_ ¯ _jK_ = 1 and the remaining _y_ ¯ _j_ s to zero. We get _L_ ( **u** ) =
_t_ =1 _[C][j][t]_ [+][ �] _i_ _[N]_ =1 _[u][i]_ [.]


**Property** **3:** Based on the optimal solution **y** ¯ of _L_ ( **u** ) obtained in Property 2,
one can get a heuristic ( _ad_ _hoc_ ) solution (¯ **x** _,_ ¯ **y** ) for (8.9) and an assessment of how good it is.


_•_ Each **u** gives the upper bound _L_ ( **u** ) _≥_ _Z_ and the following heuristic
feasible solution **x** ¯ to (8.9). Let **y** ¯ solve (8.11). Next, for each
_i_ = 1 _, . . ., N_, assign _i_ to the most similar centroid among the _K_
centroids such that _y_ ¯ _j_ = 1. That is, let _j_ ( _i_ ) = argmax _j_ :¯ _yj_ =1 _ρij_ and
let **x** ¯ be as follows:


            1 if _j_ = _j_ ( _i_ )
_x_ ¯ _ij_ = 0 otherwise.


_•_ If [�] _i,j_ _[ρ][ij]_ [ ¯] _[x][ij]_ [and] _[L]_ [(] **[u]** [)] [are] [close] [to] [each] [other,] [then] [we] [have] [a] [near-]
optimal solution. To see this, observe thatThus if [�] _i,j_ _[ρ][ij]_ [ ¯] _[x][ij]_ [and] _[L]_ [(] **[u]** [)] [are] [close] [to] [each][�] _i,j_ [other,] _[ρ][ij]_ [ ¯] _[x][ij]_ [they] _[≤]_ _[Z]_ [must] _[≤]_ _[L]_ [(] **[u]** [be][).]
close to the optimal value _Z_ as well.


150 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


_•_ To get the best upper bound _L_ ( **u** ) together with a heuristic solution
of the above kind, solve


min
**u** _[L]_ [(] **[u]** [)] _[.]_


This turns out to be a manageable convex optimization problem.
In particular, it is amenable to a _subgradient_ algorithm that we
describe in Chapter 20.


**8.4** **Algorithms** **for** **Solving** **Mixed** **Integer** **Programs**


The modeling power of mixed integer programming comes with some cost. Mixed
integer programming belongs to the class of _NP-hard_ computational problems
(Conforti et al., 2014). In layman’s terms, this means that, unlike convex optimization problems, which can be solved with fast and reliable numerical algorithms, the same cannot be expected for mixed integer programs. The algorithms
that we describe next can in principle solve any mixed integer linear programs in
finitely many steps. However, the NP-hardness of integer programming implies
that for some problem instances the computational cost incurred by these algorithms could be insurmountable even for any foreseeable amount of computational power.
The two most popular generic methods for solving mixed integer linear
programs are _cutting_ _planes_ and _branch_ _and_ _bound_ . Both of these methods rely
extensively on linear programming relaxations. A cutting plane is a new linear
constraint to the linear programming relaxation that “cuts off” non-integer
solutions without cutting off any feasible solution of the original mixed integer
linear program. The method of cutting planes was proposed by Dantzig et
al. (1954) in the context of the traveling-salesman problem, and by Gomory
(1958, 1960) for pure integer linear programs and mixed integer linear programs,
respectively. The method is based on solving a sequence of increasingly tighter
linear programming relaxations by adding cutting planes until a solution to the
mixed integer linear program is found. On the other hand, Land and Doig (1960)
proposed a “branch-and-bound” method to solve mixed integer linear programs.
Branch and bound is an enumerative procedure based on dividing the original
problem into a number of smaller problems (branching) and evaluating their
quality based on their linear programming relaxations (bounding). Branch and
bound was the most effective technique for solving mixed integer linear programs
for multiple decades. However, in the 1990s, cutting planes made a resurgence.
Current state-of-the-art integer programming solvers combine cutting planes
and branch and bound into an overall procedure called “branch and cut”, a term
coined in Padberg and Rinaldi (1987).


**8.4** **Algorithms** **for** **Solving** **Mixed** **Integer** **Programs** 151


8.4.1 Branch-and-Bound Method


The gist of the branch-and-bound method can be easily grasped via a couple of
examples. Consider the following integer linear program (see Figure 8.3):



(8.12)



_x_ 1



max _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 _≤_ 2
8 _x_ 1 + 2 _x_ 2 _≤_ 19
_x_ 1 _, x_ 2 _≥_ 0
_x_ 1 _, x_ 2 _∈_ Z _._


_x_ 2



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-163-0.png)

**Figure** **8.3** A two-variable integer program


**Step** **1.** Solve the linear programming relaxation of (8.12), namely


max _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 _≤_ 2
8 _x_ 1 + 2 _x_ 2 _≤_ 19
_x_ 1 _, x_ 2 _≥_ 0 _._

                - �T
The solution is **x** ¯ = 1 _._ 5 3 _._ 5 with objective value 5. Thus 5 is an

                                    - �T
upper bound on the optimal value of (8.12). The vector **x** ¯ = 1 _._ 5 3 _._ 5

is not a feasible solution to (8.12) since the entries of **x** ¯ are fractional.
How can we exclude this fractional solution while preserving the feasible
integral solutions? One way is to _branch_ : create two new linear programs,
one with the additional constraint _x_ 1 _≤_ 1, and the other with the
additional constraint _x_ 1 _≥_ 2. Clearly, any solution to the integer program
must be feasible to one or the other of these two problems. We will solve
both of these linear programs.


152 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


**Step** **2.** Solve the first of the two new linear programs:


max _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 _≤_ 2
8 _x_ 1 + 2 _x_ 2 _≤_ 19
_x_ 1 _≤_ 1
_x_ 1 _, x_ 2 _≥_ 0 _._


                      - �T
The solution is **x** ¯ = 1 3 with objective value 4. This is a feasible
integral solution to (8.12). So now we have the upper bound 5 and the
lower bound 4 on the optimal value of (8.12).

**Step** **3.** Solve the second new linear program:


max _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 _≤_ 2
8 _x_ 1 + 2 _x_ 2 _≤_ 19
_x_ 1 _≥_ 2
_x_ 1 _, x_ 2 _≥_ 0 _._


                      - �T
The solution is **x** ¯ = 2 1 _._ 5 with objective value 3.5. Because this
value is worse than the lower bound of 4 that we already have, we do not

                                            - �T
need any further branching. We conclude that the vector **x** ¯ = 1 3

with objective value 4 found in Step 2 is an optimal solution to (8.12).


The solution of the above integer program by branch and bound required the
solution of three linear programs. These problems can be arranged in a _branch-_
_and-bound_ _tree_, see Figure 8.4. Each _node_ of the tree corresponds to one of the
problems that were solved.



|x = 1.5, x = 3.5<br>1 2<br>z = 5<br>x ≤1 x ≥2<br>1 1<br>x = 1, x = 3 x = 2, x = 1.5<br>1 2 1 2<br>z = 4 z = 3.5|Col2|
|---|---|
|_x_1 = 1, _x_2 = 3<br>_z_ = 4|_x_1 = 2, _x_2 = 1_._5<br>_z_ = 3_._5|


**Figure** **8.4** Branch-and-bound tree for (8.12)





We can stop the enumeration at a node of the branch-and-bound tree for three
different reasons (when they occur, the node is said to be _pruned_ ).


**Pruning** **by** **integrality** occurs when the corresponding linear program has an
optimal solution that is integral. This occurred in Step 2 in the above
example.


**8.4** **Algorithms** **for** **Solving** **Mixed** **Integer** **Programs** 153


**Pruning** **by** **bounds** occurs when the objective value of the linear program at
that node is worse than the value of the best feasible solution found so
far. This occurred in Step 3 in the above example.
**Pruning** **by** **infeasibility** occurs when the linear program at that node is infeasible. This did not occur in any of the steps in the above example.


We next illustrate the branch-and-bound method is a slightly modified instance
that leads to a larger branch-and-bound tree. Consider the integer linear program:



max 3 _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 _≤_ 2
8 _x_ 1 + 2 _x_ 2 _≤_ 19
_x_ 1 _, x_ 2 _≥_ 0
_x_ 1 _, x_ 2 _∈_ Z _._


Figure 8.5 depicts the branch-and-bound tree for this problem.



(8.13)



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-165-0.png)









**Figure** **8.5** Branch-and-bound tree for (8.13)


Algorithm 8.1 sketches the branch-and-bound method for a general mixed
integer linear program of the form (8.1). The branch-and-bound method keeps a
list of linear programming problems obtained by relaxing the integrality requirements on the variables and imposing constraints such as _xj_ _≤_ _uj_ or _xj_ _≥_ _lj_ . Each
such linear program corresponds to a _node_ of the branch-and-bound tree. It will
be convenient to let _Ni_ denote both a node and its corresponding linear program
in the branch-and-bound tree. Let **x** _[i]_ and _zi_ denote respectively the optimal
solution and optimal value of the linear program _Ni_ with the convention _zi_ = _∞_


154 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


if _Ni_ is infeasible. Let _N_ 0 denote the root node of the branch-and-bound tree: it
corresponds to the linear programming relaxation (8.2) of (8.1). Throughout the
algorithm we let _L_ denote the list of nodes that must still be solved. These are
the nodes that have not been pruned nor branched on. Throughout the algorithm
**x** _[∗]_ denotes the best feasible solution found so far and _zU_ its objective value. The
value _zU_ is also the best upper bound on the optimal value _z_ of (8.1) so far.
Initially, the bound _zU_ can be derived from a heuristic solution to (8.1), or it
can be set to + _∞_ if no heuristic solution is available.


**Algorithm** **8.1** Branch-and-bound method

1: _L_ := _{N_ 0 _}_, _zU_ := + _∞_, **x** _[∗]_ := _∅_ _(initialization)_

2: **if** _L_ = _∅_ **then** HALT and **return** the vector **x** _[∗]_ **end** **if** _(termination)_

3: choose and delete a node _Ni_ from _L_ and solve it _(select_ _next_ _node_ _to_ _solve)_

4: **if** _zi_ _≥_ _zU_ **then** go to step 2 **end** **if** _(prune_ _Ni)_

5: **if** **x** _[i]_ is feasible for (8.1) **then** _(update_ _upper_ _bound_ _and_ _prune)_
_zU_ := _zi_ ; **x** _[∗]_ := **x** _[i]_

delete from _L_ all nodes _Nk_ with _zk_ _≥_ _zU_
go to step 2

6: **else** _(branch_ _from_ _Ni)_
choose _j_ _∈_ _J_ such that _x_ ¯ _[i]_ _j_ _[̸∈]_ [Z]
branch on variable _xj,_ that is, construct two new linear programs
_Ni_ [1][:] [add] [the] [new] [constraint] _[x][j]_ _[≤⌊][x]_ [¯] _[i]_ _j_ _[⌋]_ [to] _[N][i]_
_Ni_ [2][:] [add] [the] [new] [constraint] _[x][j]_ _[≥⌈][x]_ [¯] _[i]_ _j_ _[⌉]_ [to] _[N][i]_
add _Ni_ [1] _[, N]_ [ 2] _i_ [to] _[L]_ [and] [go] [to] [step] [2]

7: **end** **if**


There are a variety of strategies for node selection (step 3) and for branching
(step 6). Even more important to the success of branch and bound is the ability
to prune the tree (steps 4 and 5). This will occur when _zU_ is a good upper
bound and when _zi_ is a good lower bound. For this reason, it is crucial to have a
formulation of (8.1) whose linear programming relaxation has an optimal value
_zLP_ as close as possible to the optimal value _z_ of (8.1).


8.4.2 Cutting-Plane Method


A _valid_ _inequality_ for a mixed integer linear program is a linear inequality
that is satisfied by all feasible solutions. A _cutting_ _plane_ of a mixed integer
linear program is a valid inequality that cuts off some solutions to its linear
programming relaxation.
As we noted in Proposition 8.3, if an optimal solution of the linear programming relaxation satisfies the integrality constraints of a mixed integer linear
program, then it is an optimal solution to the mixed integer linear program.
The gist of cutting-plane methods is the observation that, when the latter does


**8.4** **Algorithms** **for** **Solving** **Mixed** **Integer** **Programs** 155



not occur, the linear programming relaxation can be strengthened by adding a
cutting plane that cuts off its optimal solution.
Gomory (1960) proposed the following approach for solving mixed integer
linear programs. Assume the variables in the problem are non-negative and
satisfy the equality constraint

     -     



- 
_ajxj_ +
_j∈J_ _j̸∈J_



_ajxj_ = _b._ (8.14)
_j̸∈J_



Assume that _b_ is not an integer and let _f_ 0 be its fractional part, i.e. _b_ = _⌊b⌋_ + _f_ 0,
where 0 _< f_ 0 _<_ 1. For _j_ _∈_ _J_, let _aj_ = _⌊aj⌋_ + _fj_, where 0 _≤_ _fj_ _<_ 1. Replacing in
(8.14) and moving sums of integer products to the right, we get

  -   -   



 - 
_fjxj_ +
_j∈J_ : _fj_ _≤f_ 0 _j∈J_ : _fj_




 - 
( _fj_ _−_ 1) _xj_ +
_j∈J_ : _fj_ _>f_ 0 _j̸∈J_



_ajxj_ = _k_ + _f_ 0 _,_
_j̸∈J_



where _k_ is some integer. Using the fact that _k_ _≤−_ 1 or _k_ _≥_ 0, we must have
either



11 _− −_ _ff_ 0 _j_ _xj_ _−_ - _j̸∈J_




  
_−_


_j∈J_ : _fj_ _≤f_ 0


or

   


_fj_  1 _−_ _f_ 0 _xj_ + _j∈J_ : _fj_ _>f_ 0



1 _−_ _fj_



1 _−ajf_ 0 _xj_ _≥_ 1



_−_ _fj_ 
_xj_ +
_f_ 0



_j∈J_ : _fj_ _≤f_ 0



_fj_ _xj_ _−_ _f_ 0 _j∈J_ : _fj_ _>f_ 0



_j̸∈J_



_aj_ _xj_ _≥_ 1 _._
_f_ 0



This is of the form [�] _j_ _[c][j][x][j]_ _[≥]_ [1 or][ �] _j_ _[d][j][x][j][ ≥]_ [1, which implies][ �] _j_ [max(] _[c][j][, d][j]_ [)] _[x][j]_ _[≥]_
1 because the variables _xj_ are non-negative.
Which is the larger of the two coefficients _cj_ and _dj_ in our case? The answer
is easy since one coefficient is positive and the other is negative for each variable
_xj_ . Therefore, we get




 

_j∈J_ : _fj_ _≤f_ 0



_fj_ _xj_ +
_f_ 0 _j∈J_ : _fj_ _>f_ 0



1 _−_ _fj_ 1 _−_ _f_ 0 _xj_ + _j̸∈J_ : _aj_ _>_ 0



_aj_ _xj_ _−_ _f_ 0 _̸∈J_ : _aj_ _<_ 0



1 _−ajf_ 0 _xj_ _≥_ 1 _._



(8.15)
Inequality (8.15) is valid for all **x** _≥_ 0 that satisfy (8.14) with _xj_ integer for
_j_ _∈_ _J_ . It is called a _Gomory_ _mixed_ _integer_ _cut_ .
We illustrate the use of Gomory cuts on problem (8.12). To that end, we first
add slack variables _x_ 3 and _x_ 4 to turn the inequality constraints into equalities:


max _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 + _x_ 3 = 2
8 _x_ 1 + 2 _x_ 2 + _x_ 4 = 19
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _≥_ 0
_x_ 1 _, x_ 2 _∈_ Z _._


Solving the linear programming relaxation by the simplex method we get the


156 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


optimal basis _B_ = _{_ 1 _,_ 2 _}_ and so the constraints of the linear programming
relaxation can be written as


_x_ 1 _−_ 0 _._ 2 _x_ 3 + 0 _._ 1 _x_ 4 = 1 _._ 5
_x_ 2 + 0 _._ 8 _x_ 3 + 0 _._ 1 _x_ 4 = 3 _._ 5
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _≥_ 0 _._


The corresponding basic solution is _x_ 3 = _x_ 4 = 0, _x_ 1 = 1 _._ 5, _x_ 2 = 3 _._ 5 with
objective value _z_ = 5. This solution is not integer. Let us generate the Gomory
cut corresponding to the equation


_x_ 1 _−_ 0 _._ 2 _x_ 3 + 0 _._ 1 _x_ 4 = 1 _._ 5 _._


We have _f_ 0 = 0 _._ 5, _f_ 1 = _f_ 2 = 0, _a_ 3 = _−_ 0 _._ 2 and _a_ 4 = 0 _._ 1. Applying formula
(8.15), we get the Gomory cut


0 _._ 2

[0] _[.]_ [1] _[≥]_ [1] _[,]_ i.e., 2 _x_ 3 + _x_ 4 _≥_ 5 _._
1 _−_ 0 _._ 5 _[x]_ [3][ +] 0 _._ 5 _[x]_ [4]


Since _x_ 3 = 2+ _x_ 1 _−_ _x_ 2 and _x_ 4 = 19 _−_ _x_ 1 _−_ 2 _x_ 2, we can express the above Gomory
cut in terms of _x_ 1 _, x_ 2:


3 _x_ 1 + 2 _x_ 2 _≤_ 9 _._


**Figure** **8.6** Formulation strengthened by a cut


Adding this cut to the linear programming relaxation, we get the following



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-168-0.png)
**8.5** **Exercises** 157


strengthened linear programming relaxation (see Figure 8.6):


max _x_ 1 + _x_ 2
s.t. _−x_ 1 + _x_ 2 _≤_ 2
8 _x_ 1 + 2 _x_ 2 _≤_ 19
3 _x_ 1 + 2 _x_ 2 _≤_ 9
_x_ 1 _, x_ 2 _≥_ 0 _._


The optimal solution to this linear program is _x_ 1 = 1, _x_ 2 = 3 with objective
value _z_ = 4. Since _x_ 1 and _x_ 2 are integer, this is the optimal solution to (8.12).


**8.5** **Exercises**


**Exercise** **8.1** As the leader of an oil exploration drilling venture, you must
determine the best selection of four out of eight possible sites. Label the sites
_s_ 1 _, s_ 2 _, . . ., s_ 8 and the expected profits associated with each as _p_ 1 _, p_ 2 _, . . ., p_ 8.


(a) If site _s_ 3 is explored, then sites _s_ 1 and _s_ 2 must also be explored. Furthermore,
regional development restrictions are such that


(b) exploring sites _s_ 6 _and_ _s_ 7 will prevent you from exploring site _s_ 8;

(c) exploring at least one of the sites _s_ 3 _or_ _s_ 4 will prevent you from exploring
site _s_ 5.


The eight expected profits are _pi_ = _i_ for _i_ = 1 _, . . .,_ 8. Formulate an integer
program to determine the best exploration scheme and solve numerically with
Solver.


**Exercise 8.2** Consider the following projects for possible investments. For each
project, you are given the NPV as well as the cash outflows required during each
year (in millions of dollars).


NPV Year 1 Year 2 Year 3 Year 4


Project 1 30 12 4 4 0
Project 2 30 0 12 4 4
Project 3 20 3 4 4 4
Project 4 15 10 0 0 0
Project 5 15 0 11 0 0
Project 6 15 0 0 12 0
Project 7 15 0 0 0 13
Project 8 24 8 8 0 0
Project 9 18 0 0 10 4
Project 10 18 0 0 4 10


No partial investment is allowed in any of these projects. The firm has 18 million
dollars available for investment each year.


158 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


(a) Formulate an integer linear program to determine the best investment plan.
(b) Formulate the following conditions as linear constraints.
(i) Exactly one of the projects 4, 5, 6, 7 must be invested in.
(ii) If Project 1 is invested in, then Project 2 cannot be invested in.
(iii) If Project 3 is invested in, then Project 4 must also be invested in.
(iv) If Project 8 is invested in, then either Project 9 or Project 10 or both
must also be invested in.
(v) If either Project 1 or Project 2 is invested in, then neither Project 9
nor Project 10 can be invested in.


**Exercise** **8.3** Consider the problem


max 20 _x_ 1 + 10 _x_ 2 + 10 _x_ 3
s.t. 2 _x_ 1 + 20 _x_ 2 + 4 _x_ 3 _≤_ 15
6 _x_ 1 + 20 _x_ 2 + 4 _x_ 3 = 20
_x_ 1 _, x_ 2 _, x_ 3 _≥_ 0
_x_ 1 _, x_ 2 _, x_ 3 _∈_ Z _._


Solve its linear programming relaxation. Then, show that it is impossible to
obtain a feasible integral solution by rounding the values of the variables.


**Exercise** **8.4**


(a) Compare the feasible solutions of the following three integer linear programs:


max 14 _x_ 1 + 8 _x_ 2 + 6 _x_ 3 + 6 _x_ 4
s.t. 28 _x_ 1 + 15 _x_ 2 + 13 _x_ 3 + 12 _x_ 4 _≤_ 39 (i)
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _∈{_ 0 _,_ 1 _},_


max 14 _x_ 1 + 8 _x_ 2 + 6 _x_ 3 + 6 _x_ 4
s.t. 2 _x_ 1 + _x_ 2 + _x_ 3 + _x_ 4 _≤_ 2 (ii)
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _∈{_ 0 _,_ 1 _},_



max 14 _x_ 1 + 8 _x_ 2 + 6 _x_ 3 + 6 _x_ 4
s.t. 2 _x_ 1 + _x_ 2 + _x_ 3 + _x_ 4 _≤_ 2
_x_ 1 + _x_ 2 _≤_ 1
_x_ 1 + _x_ 3 _≤_ 1
_x_ 1 + _x_ 4 _≤_ 1
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _∈{_ 0 _,_ 1 _}._



(iii)



(b) Compare the relaxations of the above integer linear programs obtained by
replacing _x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _∈{_ 0 _,_ 1 _}_ by 0 _≤_ _xj_ _≤_ 1 for _j_ = 1 _, . . .,_ 4. Which is the
best formulation among (i), (ii), (iii) for obtaining a tight bound from the
linear programming relaxation?


**Exercise** **8.5** Prove Proposition 8.3.


**Exercise** **8.6** Prove Proposition 8.4.


**8.5** **Exercises** 159


**Exercise** **8.7** Prove that the function **u** _�→_ _L_ ( **u** ) defined in (8.6) is a concave
function.


**Exercise** **8.8** Prove Proposition 8.5.


**Exercise** **8.9** Let _zLP_ denote the value of the linear programming relaxation
(8.2) and let _zLD_ be the Lagrangian dual of the following Lagrangian relaxation
of (8.1):

_L_ ( **u** ) := min **c** [T] **x** + **u** [T] ( **b** _−_ **Ax** )
**x**

s.t. **Dx** _≥_ **d**
_xj_ _∈_ Z _,_ _j_ _∈_ _J._


Prove that _zLP_ _≤_ _zLD_ .


**Exercise** **8.10** Use the branch-and-bound method to solve the binary linear
programming model:


max 8 _x_ 1 + 11 _x_ 2 + 6 _x_ 3 + 4 _x_ 4
s.t. 6 _._ 7 _x_ 1 + 10 _x_ 2 + 5 _._ 5 _x_ 3 + 3 _._ 4 _x_ 4 _≤_ 19
8 _x_ 1 + 2 _x_ 2 _≤_ 19
_x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _∈{_ 0 _,_ 1 _}._


Compare the number of nodes in the branch-and-bound tree with the following
naive brute-force enumeration approach: check each of the 2 [4] = 16 possible

        - �T
values of **x** = _x_ 1 _x_ 2 _x_ 3 _x_ 4 with _xi_ _∈{_ 0 _,_ 1 _}_, for _i_ = 1 _, . . .,_ 4, and pick the
best feasible solution among them.


**Exercise** **8.11** Solve the integer linear programs of Exercise 8.4 using your
favorite solver. In each case, report the number of nodes in the enumeration
tree. Is it related to the tightness of the linear programming relaxation studied
in Exercise 8.4(b)?


**Exercise** **8.12** Modify the branch-and-bound method (Algorithm 8.1) so that
it stops as soon as it has found a feasible solution that is guaranteed to be within
5% of the optimum.


**Exercise** **8.13** Consider the integer program


max 10 _x_ 1 + 13 _x_ 2
s.t. 10 _x_ 1 + 14 _x_ 2 _≤_ 43
_x_ 1 _, x_ 2 _≥_ 0
_x_ 1 _, x_ 2 _∈_ Z _._


(a) Introduce a slack variable and solve the linear programming relaxation by
the simplex method.
Hint: You should find the following optimal tableau:


max _x_ 2 + _x_ 3
s.t. _x_ 1 + 1 _._ 4 _x_ 2 + 0 _._ 1 _x_ 3 = 4 _._ 3
_x_ 1 _, x_ 2 _, x_ 3 _≥_ 0


160 **Mixed** **Integer** **Programming:** **Theory** **and** **Algorithms**


with basic solution _x_ 1 = 4 _._ 3, _x_ 2 = _x_ 3 = 0.
(b) Generate a Gomory mixed integer (GMI) cut that cuts off this solution.
(c) Multiply both sides of the equation _x_ 1 +1 _._ 4 _x_ 2 +0 _._ 1 _x_ 3 = 4 _._ 3 by the constant
_k_ = 2 and generate the corresponding GMI cut. Repeat for _k_ = 3 _,_ 4 and 5.
Compare the five GMI cuts that you found.
(d) Add the GMI cut generated for _k_ = 3 to the linear programming relaxation.
Solve the resulting linear program by the simplex method. What is the
optimum solution of the integer program?


## 9 Mixed Integer Programming Models: Portfolios with Combinatorial Constraints

This chapter presents several applications of integer and mixed integer programming, namely combinatorial auctions, the lockbox problem, constructing an
index fund, and portfolio optimization with cardinality and threshold constraints.
All of these applications involve combinatorial features that can be modeled via
binary variables.


**9.1** **Combinatorial** **Auctions**


A _combinatorial_ _auction_ is an auction that involves the concurrent sale of multiple items. Examples include Federal Communications Commission (FCC) spectrum auctions, electricity markets, pollution right auctions, and auctions for
airport landing slots. In these kinds of auctions, bidders have preferences for
sets of items usually called _bundles_ . The value that a bidder has for a bundle
may not necessarily be equal to the sum of the values that the bidder has for
individual items in the bundle. To take the bidders’ preferences into consideration, combinatorial auctions allow bidders to submit bids on combinations of
items.
Specifically, let _M_ be the set of items that the auctioneer has to sell and _N_
the set of bidders. A _bid_ is a pair ( _S, bj_ ( _S_ )) where _S_ _⊆_ _M_, for _j_ _∈_ _N_, and _bj_ ( _S_ )
is the price that bidder _j_ is willing to pay for the bundle _S_ . The _combinatorial_
_auction_ _problem_ or _winner_ _selection_ _problem_ is the problem of identifying which
bids should be accepted to maximize the auctioneer’s revenue. This problem can
be formulated as a binary linear program.


_Binary_ _linear_ _programming_ _model_ _for_ _the_ _combinatorial_ _auction_ _problem_
**Variables:**

           1 if bundle _S_ is allocated to bidder _j_
_x_ ( _S, j_ ) =
0 otherwise


for _S_ _⊆_ _M, j_ _∈_ _N._



**Objective:**




 max


_S⊆M_





_bj_ ( _S_ ) _x_ ( _S, j_ ) _._
_j∈N_


162 **Mixed** **Integer** **Programming:** **Portfolios** **with** **Constraints**



**Constraints:**

  

_S⊆M_ : _i∈S_





_x_ ( _S, j_ ) _≤_ 1 for _i ∈_ _M_
_j∈N_ (allocated bundles do not overlap).
_x_ ( _S, j_ ) _∈{_ 0 _,_ 1 _}_ for _S_ _⊆_ _M,_ _j_ _∈_ _N_
(binary variables).



In some combinatorial auctions, bidders are awarded at most one of the bundles
that they bid on, even when these bundles are disjoint. This is easy to model by
adding the constraint

 
_x_ ( _S, j_ ) _≤_ 1 for _j_ _∈_ _N_ (each bidder receives at most one bundle).

_S⊆M_


For example, if there are four items for sale and the following bids have been
received: _B_ 1 = ( _{_ 1 _},_ 6), _B_ 2 = ( _{_ 2 _},_ 3), _B_ 3 = ( _{_ 3 _,_ 4 _},_ 12), _B_ 4 = ( _{_ 1 _,_ 3 _},_ 12),
_B_ 5 = ( _{_ 2 _,_ 4 _},_ 8), _B_ 6 = ( _{_ 1 _,_ 3 _,_ 4 _},_ 16), the winners can be determined by the
following integer program:


max 6 _x_ 1 + 3 _x_ 2 + 12 _x_ 3 + 12 _x_ 4 + 8 _x_ 5 + 16 _x_ 6
s.t. _x_ 1 + _x_ 4 + _x_ 6 _≤_ 1 (item 1 is allocated at most once)
_x_ 2 + _x_ 5 _≤_ 1 (item 2 is allocated at most once)
_x_ 3 + _x_ 4 + _x_ 6 _≤_ 1 (item 3 is allocated at most once)
_x_ 3 + _x_ 5 + _x_ 6 _≤_ 1 (item 4 is allocated at most once)
_xj_ _∈{_ 0 _,_ 1 _}_ for _j_ = 1 _, . . .,_ 6 _._


If bids _B_ 4 and _B_ 5 come from the same bidder who wants at most one of these
two bundles, it suffices to add the constraint


_x_ 4 + _x_ 5 _≤_ 1 _._



If there are multiple units _ui_ of each item _i_ _∈_ _M_, then a bid can be more
broadly defined as a pair ( _λ, bj_ ( _λ_ )) where _λ_ is an _M_ -vector with entries _λi_ _∈_
_{_ 0 _,_ 1 _, . . ., ui},_ _i ∈_ _M_, that indicates the desired number of units _λi_ of each item
_i_ _∈_ _M_ . Let Λ denote the set of all these _M_ -vectors. The previous model is
replaced by




 max

_λ_    - _∈_ Λ

s.t.







_λ∈_ Λ



_bj_ ( _λ_ ) _x_ ( _λ, j_ )
_j∈N_



_j_ - _∈N_



_λ∈_ Λ



_λix_ ( _λ, j_ ) _≤_ _ui_ for _i ∈_ _M_
_j∈N_



_x_ ( _λ, j_ ) _∈{_ 0 _,_ 1 _}_ for _λ ∈_ Λ _,_ _j_ _∈_ _N._


There are further variations of the above formulations that incorporate additional
features such as constraints on the kinds of bids the auctioneer accepts and
constraints on the kinds of bundles that can be allocated to bidders (De Vries
and Vohra, 2003). The gist of these models is essentially the same as those
discussed above.


**9.2** **The** **Lockbox** **Problem** 163


**9.2** **The** **Lockbox** **Problem**


Consider a national firm that receives checks from all over the United States. Due
to the vagaries of the Postal Service, as well as the banking system, there is a variable delay from when the check is postmarked (and hence the customer has met
her obligation) and when the check clears (and when the firm can use the money).
For instance, a check mailed in Pittsburgh sent to a Pittsburgh address might
clear in just two days. A similar check sent to Los Angeles (L.A.) might take four
days to clear. It is in the interest of the firm to have the check clear as quickly as
possible since then the firm can use the money. In order to speed up this clearing,
firms open offices (called lockboxes) in different cities to handle the checks.


**Example** **9.1** Suppose we receive payments from four regions (West, Midwest, East, and South). The average daily value from each region is as follows:
$300,000 from the West, $120,000 from the Midwest, $360,000 from the East,
and $180,000 from the South. We are considering opening lockboxes in L.A.,
Cincinnati, Boston, and/or Houston. Operating a lockbox costs $90,000 per year.
The average days from mailing to clearing is given in Table 9.1. Which lockboxes
should we open?


From L.A. Cincinnati Boston Houston


West 2 4 6 6
Midwest 4 2 5 5
East 6 5 2 5
South 7 5 6 3


**Table** **9.1** Clearing times


First we must calculate the losses due to lost interest for each possible assignment. For example, if the West sends to Boston, then on average there will be
$1,800,000 (= 6 _×_ $300 _,_ 000) in process on any given day. Assuming an investment
rate of 10%, this corresponds to a yearly loss of $180,000. We can calculate the
losses for the other possibilities in a similar fashion to get Table 9.2.


From L.A. Cincinnati Boston Houston


West 60 120 180 180
Midwest 48 24 60 60
East 216 180 72 180
South 126 90 108 54


**Table** **9.2** Lost interest (’000)


The intuition for the formulation of the lockbox problem is similar to that of
the formulation of the _K_ -median model for clustering discussed in Chapter 8.
We use a set of binary variables to model the lockboxes to open and another set
of binary variables to model what lockbox serves each region.


164 **Mixed** **Integer** **Programming:** **Portfolios** **with** **Constraints**



_Binary_ _linear_ _programming_ _model_ _for_ _the_ _lockbox_ _problem_
**Variables:**




  1 if lockbox _j_ is opened
_yj_ = 0 otherwise for _j_ = 1 _, . . .,_ 4 _._




  1 if region _i_ is served by lockbox _j_
_xij_ = 0 otherwise for _i, j_ = 1 _, . . .,_ 4 _._



**Objective:** **minimize** **total** **yearly** **costs**


�4



�4

_yj,_

_j_ =1



min



_cijxij_ + 90

_i,j_ =1



where _cij_ is the ( _i, j_ ) entry in Table 9.2.
**Constraints:**


  - _N_

_xij_ = 1 _,_ for _i_ = 1 _, . . .,_ 4
_j_ =1 (each region must be assigned to one lockbox)
_xij_ _≤_ _yj,_ for _i, j_ = 1 _, . . .,_ 4
(region _i_ is assigned to lockbox _j_ only if _j_ is opened)
_xij, yj_ _∈{_ 0 _,_ 1 _}_ for _i, j_ = 1 _, . . .,_ 4
(binary variables).


As we observed for the binary programming formulation for clustering discussed in Example 8.2, the above formulation would also be correct if we replaced
the 4 [2] = 16 constraints
_xij_ _≤_ _yj,_ _i, j_ = 1 _, . . .,_ 4 _,_


with the four constraints
�4

_xij_ _≤_ 4 _yj,_ _j_ = 1 _, . . .,_ 4 _._

_i_ =1

However, we should note that the solution to the linear programming relaxation
of the first formulation (with more constraints) is


_x_ 11 = _x_ 21 = _x_ 33 = _x_ 43 = _y_ 1 = _y_ 3 = 1 _,_ and all other variables zero,


which has binary entries and hence is an optimal solution to the binary linear
programming model. Therefore the firm should open two lockboxes, one in the
Eastern region and one in the West.
By contrast, the solution to the linear programming relaxation of the second
formulation (with fewer constraints) is


_x_ 11 = _x_ 22 = _x_ 33 = _x_ 44 = 1 _,_ _y_ 1 = _y_ 2 = _y_ 3 = _y_ 4 = 0 _._ 25 _,_


and all other variables zero,


which does not give any useful information about the binary linear programming
model.
This example highlights how different equivalent integer programming formulations can have very different properties with respect to their associated linear
program.


**9.3** **Constructing** **an** **Index** **Fund** 165


**9.3** **Constructing** **an** **Index** **Fund**


An old and recurring debate about investing lies in the merits of active versus
passive management of a portfolio. Active portfolio management tries to achieve
superior performance by using technical and fundamental analysis. On the other
hand, passive portfolio management relies entirely on diversification to achieve
a desired performance. There are two types of passive management strategies:
“buy and hold” or “indexing”. In the first one, assets are selected on the basis of
some fundamental criteria and there is no active selling or buying of these stocks
afterwards (see the chapters on dedication (Chapter 3) and portfolio optimization
(Chapter 6)). In the second approach, absolutely no attempt is made to identify
mispriced securities. The goal is to choose a portfolio that mirrors the movements
of a broad market population or a market index. Such a portfolio is called an
index fund. Given a target population of _n_ stocks, one selects _K_ stocks (and
their weights in the index fund) to represent the target population as closely as
possible.
In the last 30 years, an increasing number of investors, both large and small,
have established index funds. Simply defined, an index fund is a portfolio
designed to track the movement of the market as a whole or some selected
broad market segment. The rising popularity of index funds can be justified
both theoretically and empirically.


**Market** **efficiency:** If the market is efficient, no superior risk-adjusted returns
can be achieved by stock picking strategies since the prices reflect all the
information available in the marketplace. Additionally, since the market
portfolio provides the best possible return per unit of risk, to the extent
that it captures the efficiency of the market via diversification, one may
argue that the best theoretical approach to fund management is to invest
in an index fund.
**Empirical** **performance:** Considerable empirical literature provides strong
evidence that, on average, money managers have consistently underperformed the major indices. In addition, studies show that, in most
cases, top performing funds for a year are no longer amongst the top
performers in the following years, leaving room for the intervention of
luck as an explanation for good performance.
**Transaction** **cost:** Actively managed funds incur transaction costs, which
reduce the overall performance of these funds. In addition, active
management implies significant research costs. Finally, fund managers
may have costly compensation packages that can be avoided to a large
extent with index funds.


Here we take the point of view of a fund manager who wants to construct an
index fund. Strategies for forming index funds involve choosing a broad market
index as a proxy for an entire market, e.g. the Standard & Poor’s list of 500
stocks (S&P 500). A pure indexing approach consists in purchasing all the issues


166 **Mixed** **Integer** **Programming:** **Portfolios** **with** **Constraints**


in the index, with the same exact weights as in the index. In most instances,
this approach is impractical (many small positions) and expensive (rebalancing
costs may be incurred frequently). An index fund with _K_ stocks, where _K_ is
substantially smaller than the size _n_ of the target population, seems desirable.
The clustering approach introduced in Chapter 8 can be used to aggregate the
stocks in a broad market into a smaller more manageable index fund. This
approach will not necessarily yield mean/variance-efficient portfolios but will
produce a portfolio that closely replicates the underlying market population.
We describe a two-step heuristic approach for constructing an index fund.
First, select _K_ stocks to be included in the portfolio. Second, determine weights
for these stocks so that the portfolio is as close as possible to the benchmark.
The motivation for this two-step approach is that each of the stocks selected in
the portfolio is a proxy for a portion of stocks in the index.
The first step, that is, the selection of the _K_ stocks to be included in the
portfolio, can be formulated as the binary linear programming formulation for
clustering for Example 8.2 in Chapter 8. Recall that the model is based on the
following data:


_ρij_ = similarity between stock _i_ and stock _j._


An example of this is the correlation between the returns of stocks _i_ and _j_ . But
one could choose other similarity measures _ρij_ .
Recall the binary linear programming formulation for the clustering problem:




- _n_

_ρijxij_

_j_ =1



max


s.t.




- _n_


_i_ =1

- _n_



_yj_ = _K_

_j_ =1

- _n_



_xij_ = 1 for _i_ = 1 _, . . ., n_

_j_ =1

_xij_ _≤_ _yj_ for _i, j_ = 1 _, . . ., n_
_xij, yj_ _∈{_ 0 _,_ 1 _}_ for _i, j_ = 1 _, . . ., n._


As discussed in Chapter 8, the variables _yj_ describe which stocks _j_ are in the
portfolio ( _yj_ = 1 if _j_ is selected in the portfolio, 0 otherwise). For each stock
_i_ = 1 _, . . ., n_, the variable _xij_ indicates which stock _j_ in the portfolio is most
similar to _i_ ( _xij_ = 1 if _j_ is the most similar stock in the portfolio, 0 otherwise).
Once the set of _K_ stocks has been selected, a simple approach to the second
step of portfolio construction is as follows. Assume _j_ 1 _, . . ., jK_ are the selected
stocks and _C_ 1 _, . . ., CK_ are the corresponding clusters. That is, _Cℓ_ is the set of
stocks represented by stock _jℓ_ for _ℓ_ = 1 _, . . ., K._ Set the weight of each selected
stock _jℓ,_ _ℓ_ = 1 _, . . ., K_, proportional to the total market capitalization of the


stocks in _Cℓ_ :



**9.4** **Cardinality** **Constraints** 167


_,_ _ℓ_ = 1 _, . . ., K,_



_xjℓ_ :=





_Vi_
_i∈Cℓ_

- _n_

_Vi_

_i_ =1



where _Vi_ is the market capitalization of stock _i_ .
The second step can alternatively be tackled via a linear or a quadratic
programming model. The variables in the model are the portfolio weights on
the selected stocks. A reasonable objective is to minimize a measure associated
with the quality of tracking such as active risk      - this would lead to a quadratic
programming problem. Alternatively, one can minimize mean absolute deviation
and obtain a linear programming problem. The constraints could include bounds
on beta, sector exposures, and other attributes to find weights of the selected
stocks so that the portfolio is as close as possible to the benchmark.


**9.4** **Cardinality** **Constraints**


In this section, we present a different approach for tracking a basket of assets, e.g.,
an index, with a small group of stocks. In contrast to the two-step approach in the
previous section, we model the index replication problem in one step, as a mixed
integer programming problem with cardinality constraints. For concreteness,
consider that case when we want to track a benchmark with a portfolio containing
a predetermined maximum number of stocks. Assume **x** _B_ is the vector of holdings
in the benchmark, and **x** is the vector of holdings in the portfolio. Suppose we
want to include at most _K_ stocks in the tracking portfolio. If we have an estimate
of the covariance matrix of the universe of stocks in the index, then the problem
can be informally stated as follows:



min ( **x** _−_ **x** _B_ ) [T] **V** ( **x** _−_ **x** _B_ )
s.t. **1** [T] **x** = 1
**x** _≥_ 0
_xj_ _>_ 0 for at most _K_ distinct _j_ = 1 _, . . ., n._



(9.1)



In order to model the problem formally, we introduce a new set of binary variables
whose role is to model the logical condition of whether each particular stock is
included in the portfolio:


          _yj_ = 10 ifotherwise _xj_ _>_ 0 _._


168 **Mixed** **Integer** **Programming:** **Portfolios** **with** **Constraints**


The problem (9.1) can be reformulated as the following mixed quadratic program:



min ( **x** _−_ **x** _B_ ) **V** ( **x** _−_ **x** _B_ )
s.t. **1** [T] **x** = 1
_xj_ _≤_ _yj_ for _j_ = 1 _, . . ., n_

 - _n_

_yj_ _≤_ _K_

_j_ =1

**x** _≥_ 0
_yj_ _∈{_ 0 _,_ 1 _}_ for _j_ = 1 _, . . ., n._



(9.2)



Observe that the _linking_ constraint _xj_ _≤_ _yj_ in (9.2) is a mathematical way of
whenencoding the logical connection between _yj_ = 1. Furthermore, the constraint _xj_ and [�] _[n]_ _j_ =1 _yj_ : the variable _[y][j]_ _[≤]_ _[K]_ [enforces] _xj_ is positive only [the] [condition]
that at most _K_ of the **x** variables are positive.
Consider now a more general mean–variance model with cardinality constraints where we now allow short positions:



min **x** [T] **Vx**
s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯
**Ax** = **b**
**Cx** _≥_ **d**
_xj_ = 0 for at most _K_ distinct _j_ = 1 _, . . ., n._



(9.3)



The above approach extends provided that there is a lower bound _ℓj_ and an
upper bound _uj_ on the value of each holding _xj_ for _j_ = 1 _, . . ., n_ . In this case
the cardinality constraint can be formulated via a new set of binary variables
_yj,_ _j_ = 1 _, . . ., n,_ together with the linking constraints


_ℓjyj_ _≤_ _xj_ _≤_ _ujyj_ for _j_ = 1 _, . . ., n._


The problem (9.3) can be reformulated as the following mixed quadratic program:



min **x** [T] **Vx**
s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯
**Ax** = **b**
**Cx** _≥_ **d**
_ℓjyj_ _≤_ _xj_ _≤_ _ujyj_ for _j_ = 1 _, . . ., n_

      - _n_

_yj_ _≤_ _K_

_j_ =1

_yj_ _∈{_ 0 _,_ 1 _}_ for _j_ = 1 _, . . ., n._


**9.5** **Minimum** **Position** **Constraints**



(9.4)



The same kind of linking constraints _ℓjyj_ _≤_ _xj_ _≤_ _ujyj_ used in the mixed
binary programming formulation (9.4) can be used to enforce another common
practical consideration: _minimum_ _position_ _constraints_ . Although diversification


**9.7** **Exercises** 169


into a broad universe of assets generally has merits, there is a potential downside:
some positions may become very small. Too many small positions typically generate higher research and monitoring costs. Consequently, investment managers
enforce minimum position constraints. This means that if a stock _j_ is included in
the portfolio, then the holding _xj_ in that stock must surpass a minimum threshold _ℓj_ _>_ 0. Consider a general mean–variance model with minimum position
constraints:



min **x** [T] **Vx**
s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯
**Ax** = **b**
**Cx** _≥_ **d**
_xj_ _>_ 0 _⇒_ _xj_ _≥_ _ℓj_ for _j_ = 1 _, . . ., n._



(9.5)



Provided there is an upper bound _uj_ on the value of each holding _xj_, for _j_ =
1 _, . . ., n,_ and proceeding as above, the problem (9.5) can be reformulated as the
following mixed quadratic program:



min **x** [T] **Vx**
s.t. _**μ**_ [T] **x** _≥_ _μ_ ¯
**Ax** = **b**
**Cx** _≥_ **d**
_ℓjyj_ _≤_ _xj_ _≤_ _ujyj_ for _j_ = 1 _, . . ., n_
_yj_ _∈{_ 0 _,_ 1 _}_ for _j_ = 1 _, . . ., n._


**9.6** **Risk-Parity** **Portfolios** **and** **Clustering**



(9.6)



Consider a situation where you are trying to construct a risk-parity portfolio as
explained in Section 7.5. We would like to allocate equal risk to a set of assets, but
several of them may be very similar. By using the risk-parity strategy directly,
you end up overweighting the characteristics those assets share. Instead, you can
cluster the assets first, and then allocate risk evenly to each cluster. This is more
consistent with the spirit of “risk parity”. This first step can be accomplished
using the clustering approach suggested in Example 8.2.


**9.7** **Exercises**


**Exercise** **9.1** In a combinatorial exchange, both buyers and sellers can submit
combinatorial bids. Bids are like in the multiple item case, except that the values
_λi_ can be negative, as can the prices _pj_ ( _λ_ ), representing selling instead of buying.
Note that a single bid can be buying some items while selling other items.
Write an integer linear program that will maximize the surplus generated by
the combinatorial exchange.


170 **Mixed** **Integer** **Programming:** **Portfolios** **with** **Constraints**


**Exercise 9.2** You have $250,000 to invest in the following possible investments.
The cash inflows/outflows are as follows:


Year 1 Year 2 Year 3 Year 4

Investment 1 _−_ 1 _._ 00 1 _._ 18
Investment 2 _−_ 1 _._ 00 1 _._ 22
Investment 3 _−_ 1 _._ 00 1 _._ 10
Investment 4 _−_ 1 _._ 00 0 _._ 14 0 _._ 14 1 _._ 00
Investment 5 _−_ 1 _._ 00 0 _._ 20 1 _._ 00


For example, if you invest one dollar in Investment 1 at the beginning of
Year 1, you receive $1.18 at the beginning of Year 3. If you invest in any of these
investments, the required minimum level is $100,000 in each case. Any or all
the available funds at the beginning of a year can be placed in a money market
account that yields 3% per year. Formulate a mixed integer linear program to
maximize the amount of money available at the beginning of Year 4. Solve the
integer program using your favorite solver.


**Exercise** **9.3** Consider a lockbox problem where _cij_ is the cost of assigning
region _i_ to a lockbox in region _j_, for _i, j_ _∈{_ 1 _, . . ., n}_ . Suppose that we wish to
open exactly _K_ lockboxes where _K_ is a given integer, 1 _≤_ _K_ _≤_ _n_ .


(a) Formulate as an integer linear program the problem of opening _K_ lockboxes
so as to minimize the total cost of assigning each region to an open lockbox.

(b) Formulate in two different ways the constraint that regions cannot send
checks to closed lockboxes.

(c) For the following data



0 4 5 8 2
4 0 3 4 6
5 3 0 1 7
8 4 1 0 4
2 6 7 4 0



⎤


_,_
⎥⎥⎥⎥⎦



_K_ = 2 and ( _cij_ ) =



⎡

⎢⎢⎢⎢⎣



compare the linear programming relaxations of your two formulations in
part (b).


**Exercise** **9.4** You currently own a portfolio of eight stocks. Using the
Markowitz model, you computed the optimal mean–variance portfolio. The
weights of these two portfolios are shown in the following table:


Stock _A_ _B_ _C_ _D_ _E_ _F_ _G_ _H_


Your portfolio 0 _._ 12 0 _._ 15 0 _._ 13 0 _._ 10 0 _._ 20 0 _._ 10 0 _._ 12 0 _._ 08

M/V portfolio 0 _._ 02 0 _._ 05 0 _._ 25 0 _._ 06 0 _._ 18 0 _._ 10 0 _._ 22 0 _._ 12


You would like to rebalance your portfolio in order to be closer to the mean–
variance portfolio. To avoid excessively high transaction costs, you decide to


**9.8** **Case** **Study** 171


rebalance only three stocks from your portfolio. Let _xi_ denote the weight of
stock _i_ in your rebalanced portfolio. The objective is to minimize the quantity


_|x_ 1 _−_ 0 _._ 02 _|_ + _|x_ 2 _−_ 0 _._ 05 _|_ + _|x_ 3 _−_ 0 _._ 25 _|_ + _· · ·_ + _|x_ 8 _−_ 0 _._ 12 _|,_


which measures how closely the rebalanced portfolio matches the mean–variance
portfolio.
Formulate this problem as a mixed integer linear program. Note that you will
need to introduce new continuous variables in order to linearize the absolute
values and new binary variables in order to impose the constraint that only
three stocks are traded.


**9.8** **Case** **Study**


The goal of this case study is to construct a parsimonious fund that tracks a
pre-specified market index.


(1) Choose a stock market index (with at least 25 stocks) to be tracked. Some
possible choices are the Dow Jones Industrial Average, the S&P 100, and
the Nasdaq 100. If you feel ambitious, you may choose a larger index.
Collect recent historical data over a meaningful horizon. Make sure you
include more observations (ideally many more) than the number of stocks in
the index. A reasonable choice is a few years (two or three) of weekly data,
or a few more (six or seven) of monthly data. For larger indices, you may
want to consider daily data.
Use the first 70% of your data for calibrating your model; that is, for
parameter estimation, choice of stocks, choice of weights, etc. Use the remaining 30% for out-of-sample testing.
(2) Use some kind of clustering or variable selection approach to choose a small
subset of stocks from the investment universe. Complete the process by
assigning weights to the selected stocks using the following simple rule:
Mimic the weighting method used in the index. For example, for a marketvalue-weighted index, assign the weight of each selected stock according to
the market value of all the stocks that it represents. You can also attempt
to replicate various attributes of the market index, such as exposure to
particular sectors, industries, etc.
(3) Compare the performance of the constructed fund and that of the actual
stock market index. To this end, test the results of your model(s) on out-ofsample data. This is more interesting if done via a rolling-time window.
(4) Construct index funds with different number of stocks. Compare their performance.
(5) Study the effect of rebalancing the index fund by periodical adjustment of
the weights of the selected stocks. Try different periods for rebalancing: one
week, one month, etc.


172 **Mixed** **Integer** **Programming:** **Portfolios** **with** **Constraints**


(6) Propose some alternative models and compare their results with those of
the basic model. You may want to consider combinations of the following
possible variations. Be as creative as you wish:
(i) Use a weighted objective function in the stock selection problem.
(ii) Use a second optimization problem to assign the weights. For example,
you can set the weights to minimize the tracking error (active variance)
between the fund and the overall index.
(iii) Match attributes of the index such as beta, and/or exposures to factors
such as industries, sectors, etc.


## 10 Stochastic Programming: Theory and Algorithms

_Stochastic_ _optimization_ is concerned with optimizing decision variables under
uncertainty. As an example, Markowitz’s mean–variance model can be seen as
a stochastic optimization model. Stochastic optimization covers a wide class of
models in a variety of disciplines. It is often associated with the terms dynamic
programming, stochastic programming, and stochastic control, among others. We
devote several chapters to this important and vast topic. This chapter concentrates on _single-period_ / _two-stage_ models. This provides a foundation for more
general _multi-period_ / _multi-stage_ models that will be discussed in Chapters 12
through 16.


**10.1** **Examples** **of** **Stochastic** **Optimization** **Models**


The next three examples inherently involve making decisions under uncertainty.


**Example** **10.1** (The newsvendor problem) A vendor purchases a particular
commodity to satisfy some demand that occurs later over some time period.
The demand _D_ is random. The per-unit ordering cost, back-ordering cost, and
holding costs are known to be _c_, _p_, and _h,_ respectively. The total cost incurred
by the vendor if he purchases _x_ units and the demand turns out to be _D_ is


_F_ ( _x, D_ ) = _c · x_ + _p ·_ max( _D −_ _x,_ 0) + _h ·_ max( _x −_ _D,_ 0) _._


The problem is to decide the order quantity _x_ that minimizes the expected total
cost E[ _F_ ( _x, D_ )].


**Example** **10.2** (Utility-based optimization) An investor with endowment _W_ 0
needs to decide how to invest this initial capital over a planning horizon. The
investor’s preferences for her final wealth _W_ are expressed via a concave utility
function _U_ ( _W_ ). Assume **r** is the vector of random returns on the assets that the
investor can purchase over the planning horizon. The investor wishes to choose
a portfolio **x** _∈X_ that maximizes the expected utility E[ _U_ ( _W_ )] of her final
wealth _W_ :


_W_ = _W_ 0(1 + **r** [T] **x** ) _._


174 **Stochastic** **Programming:** **Theory** **and** **Algorithms**


**Example** **10.3** (Optimal consumption and investment) An individual may consume some portion _C_ 0 of her initial endowment _W_ 0 now and invest the remaining
capital _W_ 0 _−_ _C_ 0 for consumption at a future time. Assume **r** is the vector of
random returns on the assets in which she can invest her remaining capital
_W_ 0 _−_ _C_ 0. Investing in a portfolio **x** will thus produce a random wealth _W_ =
( _W_ 0 _−_ _C_ 0)(1 + **r** [T] **x** ). What should her consumption _C_ 0 and investment decisions
**x** _∈X_ be to maximize her total expected utility


_U_ 0( _C_ 0) + E[ _U_ 1( _W_ )] _._


**10.2** **Two-Stage** **Stochastic** **Optimization**


Consider the following generic type of optimization problem under uncertainty.
At time 0 we need to make a set of decisions **x** subject to some constraint set
_X_ . Between time 0 and time 1 a random outcome _ω_ is revealed. Our goal is to
choose **x** to minimize the expectation of some objective function _F_ ( **x** _, ω_ ) that
depends both on **x** as well as on the random outcome _ω._ This generic _stochastic_
_optimization_ problem has the following formal formulation:


min E( _F_ ( **x** _, ω_ ))
**x** (10.1)

**x** _∈X_ _._


The particular form of _F_ ( **x** _, ω_ ) may define various types of problems, as we saw
in Examples 10.1, 10.2, and 10.3. The function _F_ ( **x** _, ω_ ) could be more involved:
In a problem with _recourse_ the function _F_ ( **x** _, ω_ ) depends on decisions that can
be made _after_ the uncertainty _ω_ is revealed.
_Stochastic_ _optimization_ _with_ _recourse_ is a refinement of the generic formulation (10.1). In this class of problems a first set of decisions **x** must be made _here_
_and_ _now_ at time 0. Between time 0 and time 1 a random outcome _ω_ occurs.
Then at time 1 we have the opportunity to make a new round of _wait-and-see_
decisions **y** ( _ω_ ) after the random _ω_ is revealed. This leads to a _two-stage stochastic_
_optimization_ _with_ _recourse_ problem formally stated as follows:


min _f_ ( **x** ) + E[ _Q_ ( **x** _, ω_ )]
**x** (10.2)

**x** _∈X_ _._


The recourse term _Q_ ( **x** _, ω_ ) depends on the initial set of decisions **x** and on the
random outcome _ω_, and it is of the form


_Q_ ( **x** _, ω_ ) := min _g_ ( **y** ( _ω_ ) _, ω_ )
**y** ( _ω_ )

**y** ( _ω_ ) _∈Y_ ( **x** _, ω_ ) _._


The set of decisions **y** ( _ω_ ) are the _recourse_ _decisions._ They are _adaptive_ to the
random outcome _ω_ . This means that unlike **x** they are allowed to depend on _ω_ .


**10.3** **Linear** **Two-Stage** **Stochastic** **Programming** 175


**Example** **10.4** (Newsvendor problem revisited) In this case the total cost is


_F_ ( _x, D_ ) = _c · x_ + _p ·_ max( _D −_ _x,_ 0) + _h ·_ max( _x −_ _D,_ 0) _._


We want to solve


min
_x≥_ 0 [E][[] _[F]_ [(] _[x, D]_ [)] = min] _x≥_ 0 [(] _[c][ ·][ x]_ [ +][ E][ [] _[p][ ·]_ [ max(] _[D][ −]_ _[x,]_ [ 0) +] _[ h][ ·]_ [ max(] _[x][ −]_ _[D,]_ [ 0)])]


= min
_x≥_ 0 [(] _[c][ ·][ x]_ [ +][ E][[] _[Q]_ [(] _[x, D]_ [)])] _[,]_


where the recourse term _Q_ ( _x, D_ ) is


_Q_ ( _x, D_ ) := min _py_ + _hz_
_y,z_

s.t. _y_ _≥_ _D −_ _x_
_z_ _≥_ _x −_ _D_
_y, z_ _≥_ 0 _._


Note that here the recourse decisions _y_ and _z_ are easy to compute once the
demand _D_ and the number of units purchased _x_ are known, namely _y_ = ( _D−x_ ) [+]

and _z_ = ( _x −_ _D_ ) [+] .


Sometimes it is preferable to consider a more general model obtained by
replacing the objective E( _F_ ( **x** _, ω_ )) in (10.1) with _ϱ_ ( _F_ ( **x** _, ω_ )) where _ϱ_ ( _·_ ) is a realvalued function. In particular, it is common to let _ϱ_ ( _·_ ) be a _risk_ _measure_ as
illustrated in the following example. We formally define and discuss risk measures
in more detail in Chapter 11.


**Example** **10.5** (Mean–variance revisited) Let **r** denote the vector of random
asset returns in an investment universe and let _**μ**_ and **V** denote respectively the
expected value and covariance matrix of **r** . The classic mean–variance model

min **x** 12 _[γ][ ·]_ **[ x]** [T] **[Vx]** _[ −]_ _**[μ]**_ [T] **[x]**

**x** _∈X_


can be written as the stochastic optimization problem


min _ϱ_ ( **r** [T] **x** )
**x**

**x** _∈X_


for the risk measure _ϱ_ defined by


_ϱ_ ( _Z_ ) = [1] 2 _[γ][ ·][ σ]_ [2][(] _[Z]_ [)] _[ −]_ [E][(] _[Z]_ [)] _[.]_


**10.3** **Linear** **Two-Stage** **Stochastic** **Programming**


A _linear_ _two-stage_ _stochastic_ _program_ is a problem of the form


min **c** [T] **x** + E[ _Q_ ( **x** _, ω_ )]
**x**

s.t. **Ax** = **b**
**x** _≥_ **0** _,_


176 **Stochastic** **Programming:** **Theory** **and** **Algorithms**


where the recourse term _Q_ ( **x** _, ω_ ) is the value of another linear program:


_Q_ ( **x** _, ω_ ) := min **q** ( _ω_ ) [T] **y** ( _ω_ )
**y**

s.t. **T** ( _ω_ ) **x** + **W** ( _ω_ ) **y** ( _ω_ ) = **h** ( _ω_ )
**y** ( _ω_ ) _≥_ 0 _._


Here the parameters **q** ( _ω_ ) _,_ **T** ( _ω_ ) _,_ **W** ( _ω_ ) _,_ **h** ( _ω_ ) are random, and _ω_ represents a
random outcome _ω_ _∈_ Ω that is revealed between stage 0 and stage 1. It is
customary and convenient to think of _ω_ itself as the array of random parameters
_ω_ = ( **q** _,_ **T** _,_ **W** _,_ **h** ). The vector **x** represents the first-stage decisions. These must be
made without knowing the random draw _ω_ . The vector **y** ( _ω_ ) denotes the secondstage decisions. These may depend on the random draw _ω_ . To ease notation, this
type of problem is often written in the following form:



min E[ **c** [T] **x** + **q** [T] **y** ]
s.t. **Ax** = **b**
**Tx** + **Wy** = **d**
**x** _≥_ **0**
**y** _≥_ **0** _,_



(10.3)



but we should keep in mind that the tuple of uncertain parameters _ω_ =
( **q** _,_ **T** _,_ **W** _,_ **h** ) is revealed between time 0 and time 1 and the recourse variables **y**
may depend on this outcome.


**10.4** **Scenario** **Optimization**


_Scenario_ _optimization_ is a computational approach to stochastic optimization.
The gist of this approach is to assume a discrete distribution for the random
outcome. More precisely, assume the set of possible random outcomes is a discrete probability space Ω = _{ω_ 1 _, . . ., ωS},_ with probability distribution _pk_ =
P( _ωk_ ) _,_ _k_ = 1 _, . . ., S._ The elements in Ω are the possible realizations or _scenarios_


_ωk_ = ( **q** _k,_ **T** _k,_ **W** _k,_ **h** _k_ )


of the stochastic components of the model.
Under this assumption, the stochastic optimization problem (10.3) can be
written as the following _deterministic_ _equivalent_ :



min **c** [T] **x** +
**x** _,_ **y** _k_




- _S_

_pk_ ( **q** [T] _k_ **[y]** _[k]_ [)]
_k_ =1



s.t. **Ax** = **b**
**T** _k_ **x** + **W** _k_ **y** _k_ = **h** _k_ for _k_ = 1 _, . . ., S_
**x** _≥_ **0**
**y** _k_ _≥_ **0** for _k_ = 1 _, . . ., S._



(10.4)



The deterministic equivalent problem has _S_ copies of the second-stage decision
variables and hence can be significantly larger than the original problem before


**10.5** ***The** **L-Shaped** **Method** 177


we considered the uncertainty of the parameters. Fortunately, the constraint
matrix has a very special sparsity structure that can be exploited as we explain
in Section 10.5 below.


**Example** **10.6** (Newsvendor problem revisited) Suppose the demand _D_ in the
newsvendor problem has a discrete distribution. More precisely, suppose the
scenarios for the demand _D_ are _D_ 1 _, . . ., DS_ and P( _D_ = _Di_ ) = _pi_ for _i_ = 1 _, . . ., S._
Hence the newsvendor problem min [where]
_x≥_ 0 [E][[] _[F]_ [(] _[x, D]_ [)]]


_F_ ( _x, D_ ) = _c · x_ + _p ·_ max( _D −_ _x,_ 0) + _h ·_ max( _x −_ _D,_ 0)


has the following deterministic equivalent:




- _S_

_pizi_

_k_ =1



min _c · x_ + _p ·_
_x,_ **y** _,_ **z**




- _S_

_piyi_ + _h ·_

_k_ =1



s.t. _yi_ _≥_ _Di −_ _x,_ _i_ = 1 _, . . ., S_
_zi_ _≥_ _x −_ _Di,_ _i_ = 1 _, . . ., S_
_x ≥_ 0
**y** _,_ **z** _≥_ 0 _._


**10.5** ***The** **L-Shaped** **Method**



The constraint matrix of (10.4) has the following form:
⎡ ⎤



⎢⎢⎢⎣



**A**
**T** 1 **W** 1
... ...
**T** _S_ **W** _S_



⎤

⎥⎥⎥⎦



Observe that the blocks **W** 1 _, . . .,_ **W** _S_ of the constraint matrix are only interrelated through the blocks **T** 1 _, . . .,_ **T** _S_ which correspond to the first-stage decisions.
In other words, once the first-stage decisions **x** have been fixed, (10.4) decomposes
into _S_ independent linear programs. The _Benders_ _decomposition_ _method_ is an
algorithm that takes advantage of this type of structure. This method is also
called the _L-shaped_ _method_ in the stochastic programming literature. The idea
behind this method is to solve a “master problem” involving only the variables **x**
and a series of independent “recourse problems” each involving a different vector
of variables **y** _k_ . The master problem and recourse problems are linear programs.
The size of these linear programs is much smaller than the size of the full model
(10.4). The recourse problems are solved for a given vector **x** and their solutions
are used to generate inequalities that are added to the master problem. Solving
the new master problem produces a new **x** and the process is repeated. More
specifically, let us write (10.4) as


178 **Stochastic** **Programming:** **Theory** **and** **Algorithms**


min **c** [T] **x** + _P_ 1( **x** ) + _· · ·_ + _PS_ ( **x** )
**x**

s.t. **Ax** = **b** (10.5)
**x** _≥_ **0**


where



_Pk_ ( **x** ) = min _pk_ **q** [T] _k_ **[y]** _[k]_
**y** _k_

s.t. **W** _k_ **y** _k_ = **h** _k −_ **T** _k_ **x**
**y** _k_ _≥_ **0**


for _k_ = 1 _, . . ., S_ . The dual of the linear program (10.6) is:



(10.6)



_Pk_ ( **x** ) = max ( **h** _k −_ **T** _k_ **x** ) [T] **u** _k_
**u** _k_ (10.7)

s.t. **W** _k_ [T] **[u]** _[k]_ _[≤]_ _[p][k]_ **[q]** _[k][.]_


For simplicity, assume (10.7) is feasible, which is the case of interest in many
applications. The recourse linear program (10.6) will be solved for a sequence of
vectors **x** _[i]_, for _i_ = 0 _,_ 1 _,_ 2 _, . . ._ . The initial vector **x** [0] can be obtained by solving


min **c** [T] **x**
**x**

s.t. **Ax** = **b** (10.8)
**x** _≥_ **0** _._


For a given vector **x** _[i]_, two possibilities can occur for the recourse linear program
(10.6): either (10.6) has an optimal solution or it is infeasible.
If (10.6) has an optimal solution **y** _k_ _[i]_ [, and] **[ u]** _[i]_ _k_ [is the corresponding optimal dual]
solution, then (10.7) implies that


_Pk_ ( **x** ) _≥_ ( **u** _[i]_ _k_ [)][T][(] **[T]** _[k]_ **[x]** _[i][ −]_ **[T]** _[k]_ **[x]** [) +] _[ P][k]_ [(] **[x]** _[i]_ [)] _[.]_


This inequality, which is called an _optimality_ _cut_, can be added to the current
master linear program. Initially, the master linear program is just (10.8).
If (10.6) is infeasible, then the dual problem is unbounded. Let **u** _[i]_ _k_ [be] [a]
direction where (10.7) is unbounded, that is, ( **h** _k −_ **T** _k_ **x** _[i]_ ) [T] **u** _[i]_ _k_ _[>]_ [ 0] [and] **[W]** _k_ [T] **[u]** _[i]_ _k_ _[≤]_
_pk_ **q** _k_ . Since we are only interested in first-stage decisions **x** that lead to feasible
second-stage decisions **y** _k_, the following _feasibility cut_ can be added to the current
master linear program:


( **u** _[i]_ _k_ [)][T][(] **[h]** _[k]_ _[−]_ **[T]** _[k]_ **[x]** [)] _[ ≤]_ [0] _[.]_


After solving the recourse problems (10.6) for each _k_, we have the following
upper bound on the optimal value of (10.4):


_UB_ = **c** [T] **x** _[i]_ + _P_ 1( **x** _[i]_ ) + _· · ·_ + _PS_ ( **x** _[i]_ ) _,_


where we set _Pk_ ( **x** _[i]_ ) = + _∞_ if the corresponding recourse problem is infeasible.


**10.6** **Exercises** 179


Adding all the optimality and feasibility cuts found so far (for _j_ = 0 _, . . ., i_ ) to
the master linear program, we obtain:



min **c** [T] **x** +
**x** _,z_ 1 _,...,zS_




- _S_

_zk_

_k_ =1



s.t. **Ax** = **b**
( **u** _[j]_ _k_ [)][T][(] **[T]** _[k]_ **[x]** _[j]_ _[−]_ **[T]** _[k]_ **[x]** [) +] _[ P][k]_ [(] **[x]** _[j]_ [)] _[ ≤]_ _[z][k]_ for some pairs ( _j, k_ )
( **u** _[j]_ _k_ [)][T][(] **[h]** _[k][ −]_ **[T]** _[k]_ **[x]** [)] _[ ≤]_ [0] for the remaining pairs ( _j, k_ )
**x** _≥_ **0** _._


Denoting by **x** _[i]_ [+1] _, z_ 1 _[i]_ [+1] _, . . ., zS_ _[i]_ [+1] an optimal solution to this linear program, we
get a lower bound on the optimal value of (10.4):


_LB_ = **c** [T] **x** _[i]_ [+1] + _z_ 1 _[i]_ [+1] + _· · ·_ + _zS_ _[i]_ [+1] _._


The Benders decomposition method alternately solves the recourse problems
(10.6) and the master linear program with new optimality and feasibility cuts
added at each iteration until the gap between the upper bound _UB_ and the lower
bound _LB_ falls below a given threshold. It can shown that _UB_ _−LB_ converges to
zero and indeed reaches zero after finitely many iterations. For details see Birge
and Louveaux (1997, chapter 5).


**10.6** **Exercises**


**Exercise** **10.1** Consider the utility-based portfolio optimization described in
Example 10.2. Suppose **r** has a multivariate normal distribution and the investor
has logarithmic utility function


_U_ ( _W_ ) = log( _W_ ) _._


Suppose _X_ is a convex set. Prove that the utility maximization problem


max E( _U_ ( _W_ ))
s.t. _W_ = _W_ 0 _·_ (1 + **r** [T] **x** )
**x** _∈X_


is equivalent to the mean–variance problem


min 12 _[γ]_ [˜] _[ ·]_ **[ x]** [T] **[Vx]** _[ −]_ _**[μ]**_ [T] **[x]**
**x** _∈X_


for some suitable level of risk aversion _γ_ ˜.


**Exercise** **10.2** Repeat the above exercise when the investor has power utility
function

1
_U_ ( _W_ ) =
1 _−_ _γ_ _[·][ W]_ [ 1] _[−][γ]_


for some risk-aversion constant _γ_ _>_ 0 _,_ _γ_ = 1.


180 **Stochastic** **Programming:** **Theory** **and** **Algorithms**


**Exercise** **10.3** Consider the newsvendor problem described in Example 10.1.
Suppose the demand _D_ has a continuous cumulative distribution function Φ;
that is, Φ( _x_ ) = P( _D_ _≤_ _x_ ) _._ Show that the solution to the newsvendor problem


min
_x≥_ 0 [(] _[c][ ·][ x]_ [ +][ E][ [] _[p][ ·]_ [ max(] _[D][ −]_ _[x,]_ [ 0) +] _[ h][ ·]_ [ max(] _[x][ −]_ _[D,]_ [ 0)])]



is




   _p −_ _c_
_x_ _[∗]_ = Φ _[−]_ [1]
_p_ + _h_





_._



**Exercise** **10.4** The purpose of this exercise is to formalize the optimality cut
described in Section 10.5. For **x** = **x** _[i]_ assume (10.6) has an optimal solution **y** _k_ _[i]_ [,]
and let **u** _[i]_ _k_ [be] [the] [corresponding] [optimal] [dual] [solution.]

(a) Show that _Pk_ ( **x** _[i]_ ) = ( **u** _[i]_ _k_ [)][T][(] **[h]** _[k][ −]_ **[T]** _[k]_ **[x]** _[i]_ [).]
(b) Show that _Pk_ ( **x** ) _≥_ ( **u** _[i]_ _k_ [)][T][(] **[h]** _[k][ −]_ **[T]** _[k]_ **[x]** [)] [for] [all] **[x]** [.]
(c) Conclude that _Pk_ ( **x** ) _≥_ ( **u** _[i]_ _k_ [)][T][(] **[T]** _[k]_ **[x]** _[i][ −]_ **[T]** _[k]_ **[x]** [) +] _[ P][k]_ [(] **[x]** _[i]_ [)] [for] [all] **[x]** [.]


## 11 Stochastic Programming Models: Risk Measures

This chapter discusses several popular risk measures. In particular, we introduce
two widely used risk measures, _value_ _at_ _risk_ and its refinement _conditional_
_value_ _at_ _risk._ We show that the problem of finding a portfolio that minimizes
conditional value at risk is amenable to stochastic programming techniques.


**11.1** **Risk** **Measures**


In the classical Markowitz model, variance (equivalently standard deviation) is
used as a measure of risk. This measure of risk is relatively easy to compute, and,
as we have seen in Chapter 6, leads to a quadratic programming model when we
are interested in finding efficient portfolios.
As we illustrate below, variance has some shortcomings as a measure of risk.
This has motivated the introduction of other risk measures.


Dispersion Measures


Let _r_ denote the (random) return of an asset. The variance


_σ_ [2] = var( _r_ ) = E(( _r −_ _μ_ ) [2] )


is a measure of _dispersion_ of the distribution of _r_ . Another dispersion measure
is the _mean_ _absolute_ _deviation_ (MAD) favored by Konno and Yamazaki (1991):


E( _|r −_ _μ|_ ) _._


For the special case of normally distributed returns, the mean absolute deviation
and the standard deviation are equivalent. Indeed, the following property is a
straightforward exercise in probability:

~~�~~
**Proposition** **11.1** _If_ _r_ _∼_ _N_ ( _μ, σ_ [2] ) _then_ E( _|r −_ _μ|_ ) = 2 _/π σ._


A major difference between mean absolute deviation and standard deviation
is their sensitivity to outliers. The mean absolute deviation is more robust
to outliers. When the distribution of joint returns is represented via a set of
scenarios, the computation of efficient portfolios for the mean absolute deviation
can be formulated as a linear program. This offers an alternative with potential


182 **Stochastic** **Programming** **Models:** **Risk** **Measures**


advantages as we will show next. Suppose the investment universe has _n_ assets
with (random) returns _r_ 1 _, r_ 2 _, . . ., rn_ . Let _μj_ = E( _rj_ ) _,_ _j_ = 1 _, . . ., n._
Recall the portfolio optimization problem that finds the minimum-variance
portfolio among a set of portfolios _X_ :

�� �2 [�]
min var( **r** [T] **x** ) = E ( **r** _−_ _**μ**_ ) [T] **x**
**x**

s.t. **x** _∈X_ _._



Consider now the model obtained by using instead the mean absolute deviation
as a measure of risk:



min E ���( **r** _−_ _**μ**_ )T **x** ���
**x**



(11.1)
s.t. **x** _∈X_ _._



Not only does the computation of efficient portfolios based on formulation (11.1)
involve solving a linear program as opposed to a quadratic program, but also
the linear program solves the problem directly over the set of scenarios thereby
circumventing the estimation of the covariance matrix.


Mean Absolute Deviation via Scenario Optimization

                                - �T
Assume the possible scenarios for the vector of returns **r** = _r_ 1 _· · ·_ _rn_ are


              - �T
**r** _[k]_ = _r_ 1 _[k]_ _· · ·_ _rn_ _[k]_ _,_ _k_ = 1 _, . . ., S,_


and scenario _k_ occurs with probability _pk,_ _k_ = 1 _, . . ., S_ . Then we can write the
above mean absolute deviation model (11.1) as


    - _S_



min
**x** _,_ **w**



_pkwk_

_k_ =1



s.t. _wk_ = _|_ ( **r** _[k]_ _−_ _**μ**_ ) [T] **x** _|_ for _k_ = 1 _, . . ., S_
**x** _∈X_ _._


We now turn this formulation into a linear program as follows:


    - _S_



min
**x** _,_ **w**



_pkwk_

_k_ =1



s.t. _wk_ _≥_ ( **r** _[k]_ _−_ _**μ**_ ) [T] **x** for _k_ = 1 _, . . ., S_
_wk_ _≥−_ ( **r** _[k]_ _−_ _**μ**_ ) [T] **x** for _k_ = 1 _, . . ., S_
**x** _∈X_ _._


Note that, because _pk_ _>_ 0 for _k_ = 1 _, . . ., S_ and the objective is minimized, _wk_ in
an optimal solution satisfies at equality the constraint with the larger right-hand
side, that is, _wk_ = _|_ ( **r** _[k]_ _−_ _**μ**_ ) [T] **x** _|_ .


**11.1** **Risk** **Measures** 183


Downside Risk Measures


Dispersion measures, such as variance and mean absolute deviation, measure the
degree of uncertainty in the random return. These measures treat both positive
and negative deviations from the mean as equally risky. In particular, these types
of measures are blind to skewed distributions.
We will next discuss two popular downside risk measures: _value_ _at_ _risk_ and
_conditional_ _value_ _at_ _risk._ Value at risk (VaR) was first introduced by a team
at J.P. Morgan and made available through RiskMetrics. VaR is used by many
financial institutions to track and report the market risk exposure of their trading
portfolios.
VaR is a measure of the worst possible loss that a portfolio may sustain with
a pre-specified likelihood. For that reason, VaR is generally measured in dollar
terms, instead of percentage units. The formal definition is as follows. Assume
that _Y_ is a (random) loss function, and _α ∈_ (0 _,_ 1) is a confidence level (typically
99%, 95%, or 90%). The _α_ value at risk of _Y_ is the (1 _−_ _α_ ) quantile of _Y_ ; that
is, the value _γ_ such that


P( _Y_ _≥_ _γ_ ) = 1 _−_ _α._


We shall denote this value by VaR _α_ ( _Y_ ).
The value at risk has the following interpretation. Given a loss function _Y_ and
a confidence level _α_ _∈_ (0 _,_ 1), the loss _Y_ will exceed _γ_ with probability (1 _−_ _α_ ).
In the special case when the loss function is normally distributed, it is easy to
compute VaR via well-known quantiles of the normal distribution.


**Example** **11.2** If _Y_ _∼_ _N_ ( _μ, σ_ [2] ) then


VaR0 _._ 95( _Y_ ) = _μ_ + 1 _._ 645 _σ,_ VaR0 _._ 99( _Y_ ) = _μ_ + 2 _._ 33 _σ._


When _Y_ has a discrete distribution, VaR can be computed by sorting the
values of _Y_ as detailed in the following example.


**Example** **11.3** Assume there are _S_ possible scenarios for the loss _Y_ :


P( _Y_ = _yk_ ) = _pk,_ _k_ = 1 _, . . ., S,_


where


_y_ 1 _≤_ _y_ 2 _≤· · · ≤_ _yS._


Then


VaR _α_ ( _Y_ ) = _yK_ _,_


where _K_ is the smallest index such that


     - _S_

_pi_ _≥_ 1 _−_ _α._

_i_ = _K_


184 **Stochastic** **Programming** **Models:** **Risk** **Measures**


In spite of its wide popularity, VaR is known to have the following two major
shortcomings (see the exercises at the end of this chapter):


_•_ VaR is not “subadditive”: The VaR of two positions combined may be greater
than the sum of the VaR of each, meaning that diversification can actually
increase VaR.


_•_ VaR does not distinguish loss size beyond the VaR threshold.


These deficiencies of VaR led Artzner et al. (1999) to propose the following formal
set of properties that a reasonable risk measure _ρ_ ( _Y_ ) of a loss function _Y_ should
satisfy:


_•_ Monotonicity: If _Y_ _≥_ 0 then _ρ_ ( _Y_ ) _≥_ 0 _._


_•_ Subadditivity: _ρ_ ( _Y_ + _Z_ ) _≤_ _ρ_ ( _Y_ ) + _ρ_ ( _Z_ ) _._


_•_ Positive homogeneity: For _c >_ 0, _ρ_ ( _cY_ ) = _cρ_ ( _Y_ ) _._


_•_ Translational invariance: For any _c ∈_ R, _ρ_ ( _Y_ + _c_ ) = _ρ_ ( _Y_ ) + _c._


A risk measure is _coherent_ if it satisfies the above four properties. Neither
standard deviation nor VaR are coherent. However, there is a modification of VaR
that is coherent, namely the _conditional_ _value_ _at_ _risk_ introduced by Rockafellar
and Uryasev (2000). Conditional value at risk (CVaR) is also known as expected
tail loss.
CVaR can be motivated as follows. Since VaR _α_ ( _Y_ ) is the most we can lose
with probability _α_, it is equivalent to saying that with probability (1 _−_ _α_ ) the
loss _Y_ will be at least VaR _α_ ( _Y_ ). CVaR is the answer to the following question:
What should we expect the value of that loss to be? More precisely, CVaR is
defined as follows. Given a loss function _Y_ and confidence level _α_ _∈_ (0 _,_ 1), the
conditional value at risk is the expected loss _Y_, conditional on this loss being at
least VaR _α_ ( _Y_ ):


E( _Y |Y_ _≥_ VaR _α_ ( _Y_ )) _._


We shall denote this expected value as CVaR _α_ ( _Y_ ) _._
Again, in the special case when the loss function is normally distributed, it is
easy to compute CVaR by using properties of the quantiles and expected tails
of the normal distribution.


**Example** **11.4** If _Y_ _∼_ _N_ ( _μ, σ_ [2] ) then


CVaR0 _._ 95( _Y_ ) = _μ_ + 2 _._ 06 _σ,_ CVaR0 _._ 99( _Y_ ) = _μ_ + 2 _._ 67 _σ._


When _Y_ has a discrete distribution, CVaR can be computed by sorting the
values of _Y_ .


**11.2** **A** **Key** **Property** **of** **CVaR** 185


**Example 11.5** Assume _Y_ takes values _yk,_ _k_ = 1 _, . . ., S,_ in _S_ possible scenarios:


P( _Y_ = _yk_ ) = _pk,_ _k_ = 1 _, . . ., S,_


where


_y_ 1 _≤_ _y_ 2 _≤· · · ≤_ _yS._


Then



1
CVaR _α_ ( _Y_ ) = 1 _−_ _α_


where _K_ is the smallest index such that




- _S_

_piyi,_

_i_ = _K_




       - _S_

_pi_ = 1 _−_ _α._

_i_ = _K_


Note that here we may have to split the probability _pK_ .


**11.2** **A** **Key** **Property** **of** **CVaR**


We next present a key property of CVaR that makes it possible to solve portfolio
optimization problems with CVaR via convex optimization.



**Proposition** **11.6** _Assume_ _Y_ _is_ _a_ _loss_ _function._ _Then_ _for_ _α ∈_ (0 _,_ 1)



CVaR _α_ ( _Y_ ) = min
_γ_




- 1
_γ_ + _[−]_ _[γ,]_ [ 0)]] _._
1 _−_ _α_ [E][[max(] _[Y]_



_Furthermore,_ _the_ _optimal_ _solution_ _(i.e.,_ _the_ _minimizer)_ _γ_ ¯ _of_ _this_ _problem_ _is_
VaR _α_ ( _Y_ ) _._


As consequence of Proposition 11.6, it follows that CVaR is subadditive.
Indeed, CVaR is a coherent risk measure (see exercises at the end of the chapter
for details). Another consequence of Proposition 11.6 is that CVaR can be
computed as the following linear two-stage stochastic program:


CVaR _α_ ( _Y_ ) = min [ _γ_ + E ( _Q_ ( _γ, Y_ ))] _,_
_γ_


where



More concisely



1
_Q_ ( _γ, Y_ ) := min
_z_ 1 _−_ _α_ _[·][ z]_

s.t. _z_ _≥_ _Y_ _−_ _γ_
_z_ _≥_ 0 _._


1
CVaR _α_ ( _Y_ ) = min _γ_ +
_γ,z_ 1 _−_ _α_ _[·]_ [ E][(] _[z]_ [)]

s.t. _z_ _≥_ _Y_ _−_ _γ_
_z_ _≥_ 0 _._


186 **Stochastic** **Programming** **Models:** **Risk** **Measures**


In this formulation the first-stage and second-stage decision variables are _γ_ and _z_
respectively. Notice that _z_ is adapted to the random outcome _Y_ . In the particular
case when _Y_ is discrete and takes values _yk_, for _k_ = 1 _, . . ., S,_ in _S_ possible
scenarios (not necessarily sorted):


P( _Y_ = _yk_ ) = _pk,_ _k_ = 1 _, . . ., S,_


we obtain the following linear programming formulation for CVaR _α_ ( _Y_ ).


**Variables:**


_γ, z_ 1 _, . . ., zS._


**Linear** **programming** **formulation** **of** **CVaR:**



1
min _γ_ +
_γ,_ **z** 1 _−_ _α_




- _S_

_pkzk_

_k_ =1



s.t. _zk_ _≥_ _yk −_ _γ,_ for _k_ = 1 _, . . ., S_
_zk_ _≥_ 0 _,_ for _k_ = 1 _, . . ., S._


An advantage of this formulation is that it allows us to minimize the
CVaR of a portfolio via linear programming as we next explain.


**11.3** **Portfolio** **Optimization** **with** **CVaR**


The discussion in this section is based on Andersson et al. (2001). This study
uses CVaR for measuring and controlling the credit risk of a portfolio of bonds.
The loss function of interest is the loss due to credit risk; that is, the loss that the
portfolio may suffer due to default or credit migration in its positions. This type
of loss function is characterized by having a large likelihood of no loss and a small
likelihood of a substantial loss. The loss distribution is heavily skewed. In this
case, standard mean–variance analysis to characterize market risk is inadequate.
VaR and CVaR are more appropriate criteria for minimizing portfolio credit risk.


Distribution of Future Values for One Single Bond


Consider a risky bond and a fixed time horizon, e.g., one year. The future value of
the bond depends on the forward curve that applies to its coupon payments. The
forward curve in turn depends on the current rating of the bond. The _benchmark_
future value of the bond is the future value of the bond if there is no change on
its credit rating. However, in the event of credit migration, the future value of
the bond may differ from the benchmark value. In particular, if the credit rating
deteriorates, the coupon payments will be subject to higher discount values and
the future value of the bond will be lower than its benchmark value.
For a concrete illustration, suppose the one-year forward interest curves for
the S&P credit ratings are as follows:


**11.3** **Portfolio** **Optimization** **with** **CVaR** 187


Category Year 1 Year 2 Year 3 Year 4


AAA 0.036 0.0417 0.0473 0.0512
AA 0.0365 0.0422 0.0478 0.0517
A 0.0372 0.0432 0.0493 0.0532
BBB 0.041 0.0467 0.0525 0.0563
BB 0.0555 0.0602 0.0678 0.0727
B 0.0605 0.0702 0.0803 0.0852
CCC 0.1505 0.1502 0.1403 0.1352


Suppose the probabilities of credit rating migration for A, BBB, and B in one
year are as follows:


Rating at year end


Initial rating AAA AA A BBB BB B CCC Default


A 0.09% 2.27% 91.05% 5.52% 0.74% 0.26% 0.01% 0.06%
BBB 0.02% 0.33% 5.95% 86.93% 5.30% 1.17% 0.12% 0.18%
B 0.00% 0.11% 0.24% 0.43% 6.48% 83.47% 4.07% 5.20%


Assuming a 50% recovery rate in default, the possible future values of a fiveyear, 6% BBB bond with face value 100 are as follows:


Year-end rating Future value Probability


AAA 109.352908 0.0002
AA 109.1723709 0.0033
A 108.6429921 0.0595
BBB 107.5309439 0.8693
BB 102.0063855 0.053
B 98.08591318 0.0117
CCC 83.6257912 0.0012
Default 50 0.0018


For example, for BBB rated bonds, the future value 107.5309439 was obtained
as follows:




      1 1 1 1
107 _._ 5309439 = 6 _·_ 1 + 1 _._ 041 [+] 1 _._ 0467 [2] [+] 1 _._ 0525 [3] [+] 1 _._ 0563 [4]


Credit Risk Optimization for a Portfolio of Bonds




1
+ 100 _·_ 1 _._ 0563 [4] _[.]_



Now suppose we construct a portfolio of risky bonds. Assume there are _n_ risky
bonds and let _xj_ be the percentage of portfolio invested in bond _j_ . Then the loss
function of our portfolio is


188 **Stochastic** **Programming** **Models:** **Risk** **Measures**



_Y_ ( **x** ) := ( **b** _−_ _**ω**_ ) [T] **x** =




- _n_

( _bj_ _−_ _ωj_ ) _xj,_

_j_ =1



where each _bj_ is the future bond value of bond _j_ with no credit migration, and
_ωj_ is the (random) possible future bond value of bond _j_ with credit migration.
Suppose we want to select the portfolio in the constraint set _X_ with minimum
CVaR _α_ . In other words, we want to solve


min CVaR _α_ ( _Y_ ( **x** ))
**x**

**x** _∈X_ _._


Suppose that the possible scenarios for the vector of future bond values _**ω**_ =

- �T
_ω_ 1 _· · ·_ _ωn_ are

              - �T
_**ω**_ _[k]_ = _ω_ 1 _[k]_ _· · ·_ _ωn_ _[k]_ _,_ _k_ = 1 _, . . ., S._


Then by Proposition 11.6, this problem has the following formulation:



1
min _γ_ +
_γ,_ **x** _,_ **z** 1 _−_ _α_




- _S_

_pkzk_

_k_ =1



s.t. _zk_ _≥_ ( **b** _−_ _**ω**_ _[k]_ ) [T] **x** _−_ _γ,_ _k_ = 1 _, . . ., S_


_zk_ _≥_ 0 _,_ _k_ = 1 _, . . ., S_
**x** _∈X_
_γ_ free.



(11.2)



If the constraint set _X_ is defined by linear constraints, then (11.2) is a linear
program.


Scenario Generation in the Credit-Risk Example


When there is a single bond, the probability distribution of the possible future
values of the bond depends on the probability of credit migration and the bond
value in each of these scenarios. For instance, for the S&P ratings, the scenarios
correspond to the ratings AAA, AA, A, BBB, BB, B, CCC, and default. The
likelihood of each of these scenarios is given by the migration matrix, which
estimates the probability of migrating from one rating to the others over a
specified time period.
The discrete distribution readily yields the set of possible scenarios for the
bond. Scenarios can also be generated via _normal_ _sampling_ as Figure 11.1 suggests (assuming we are working with a BB bond).


More precisely, normal sampling goes as follows:


_•_ compute _Z_ -scores associated with the probabilities of each of the scenarios,


![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-201-0.png)



**11.3** **Portfolio** **Optimization** **with** **CVaR** 189



_Z_ Def _Z_ CCC _Z_ B _Z_ BB _Z_ BBB _Z_ A _Z_ AA


Asset return over one year


**Figure** **11.1**


_•_ draw samples from a standard normal distribution,

_•_ use the _Z_ -scores to determine the sampled scenario.


Some interesting challenges arise in the scenario generation when we need
to work with multiple bonds. Under the simple assumption that the credit
migrations are statistically independent, we can generate scenarios via discrete
sampling or independent normal sampling. Notice that, although discrete, the
joint probability distribution for a set of ten or more bonds is extremely large.
Hence it is generally impractical to exhaustively generate the entire set of scenarios.
In the case when credit migrations are correlated, the scenario generation
problem becomes more interesting. In this case a possible solution is to use
correlated normal sampling. That is, draw samples from a correlated joint multivariate random variable. Then map each of the components in the random
sample to a possible credit rating of the bonds. Some statistical packages, like
the statistics toolbox in MATLAB, readily provide routines to sample from correlated multivariate normal variables. However, it is easy to generate correlated
normal sampling from independent normal sampling. More precisely, to sample
from a general _n_ -dimensional normal distribution _N_ ( _**μ**_ _,_ **V** ) _,_ proceed as follows:


_•_ Let **LL** [T] = **V** be the Cholesky factorization of the covariance matrix **V** .

_•_ Sample _n_ standard independent normals _xi_ _∼_ _N_ (0 _,_ 1).

_•_ Put **y** = _**μ**_ + **Lx** _._

_•_ The resulting variable **y** has the desired distribution **y** _∼_ _N_ ( _**μ**_ _,_ **V** ).


Solution of a Real-World Bond Example


Andersson et al. (2001) considered a portfolio of 197 bonds from 29 different
countries with a market value of $8.8 billion and duration of approximately


190 **Stochastic** **Programming** **Models:** **Risk** **Measures**


five years. Their goal was to rebalance the portfolio in order to minimize credit
risk. The one-year portfolio credit loss was generated using a Monte Carlo
simulation: 20,000 scenarios of joint credit states of obligators and related losses.
The distribution of portfolio losses had a long fat tail, as expected. The authors
rebalanced the portfolio by minimizing CVaR using formulation (11.2). For _α_ =
99%, the original bond portfolio had an expected portfolio return of 7 _._ 26%. The
expected loss was 95 million dollars with a standard deviation of 232 million. The
VaR was 1.03 billion dollars and the CVaR was 1.32 billion. After optimizing the
portfolio (with expected return of 7 _._ 26%), the expected loss was only 5000 dollars,
with a standard deviation of 152 million. The VaR was reduced to 210 million and
the CVaR to 263 million dollars. So all around, the characteristics of the portfolio
were much improved. Positions were reduced in bonds from Brazil, Russia, and
Venezuela, whereas positions were increased in bonds from Thailand, Malaysia,
and Chile. Positions in bonds from Colombia, Poland, and Mexico remained high
and each accounted for about 5% of the optimized portfolio.


**11.4** **Notes**


As early as the 1970s and 1980s, some major financial institutions developed
internal systems for risk management. The best known of these systems was
RiskMetrics developed in the late 1980s at J.P. Morgan when chairman Dennis
Weatherstone requested his staff provide a “4:15pm” daily one-page report
measuring and explaining the risks and potential losses over the next 24 hours
across the bank’s entire portfolio. The RiskMetrics system featured and
popularized the use of value at risk as a risk measure. The interest in a rigorous
treatment of risk measures led a set of prominent scholars to develop a formal
theory of _coherent_ _measures_ _of_ _risk_ in a landmark paper (Artzner et al., 1999).
Conditional value at risk is one of the most popular coherent measures of risk.


**11.5** **Exercises**


**Exercise 11.1** Construct a counterexample to show that VaR is not necessarily
subadditive. In other words, construct two loss functions _Y, Z_ and a confidence
level _α ∈_ (0 _,_ 1) so that


VaR _α_ ( _Y_ + _Z_ ) _>_ VaR _α_ ( _Y_ ) + VaR _α_ ( _Z_ ) _._


**Exercise** **11.2** Show that a coherent risk measure _ρ_ satisfies: if _X_ _≥_ _Y_ then
_ρ_ ( _X_ ) _≥_ _ρ_ ( _Y_ ).
Hint: Use the monotonicity and subadditivity of coherent risk measures.


**Exercise** **11.3** The purpose of this exercise is to prove Proposition 11.6 under
some additional assumptions. Assume _Y_ is a continuous loss function with density _f_ ( _y_ ) and _α ∈_ (0 _,_ 1). Let _g_ ( _γ_ ) be defined as


1
_g_ ( _γ_ ) := _γ_ +
1 _−_ _α_



**11.5** **Exercises** 191


- _∞_

max( _y −_ _γ,_ 0) _f_ ( _y_ ) _dy._
_−∞_



(a) Show that



1
_g_ _[′]_ ( _γ_ ) = 1 _−_
1 _−_ _α_




- _∞_

_f_ ( _y_ ) _dy._
_γ_



(b) Let _γ_ ¯ be the minimizer of the optimization problem


min _g_ ( _γ_ ) _._
_γ_


Use part (a) to show that


VaR _α_ ( _Y_ ) = _γ._ ¯


(c) Let _γ_ ¯ be as in part (b). Use parts (a) and (b) to show that


CVaR _α_ ( _Y_ ) = _g_ (¯ _γ_ ) _._


**Exercise 11.4** Use Proposition 11.6 to prove that CVaR is subadditive; that is,


CVaR _α_ ( _Y_ + _W_ ) _≤_ CVaR _α_ ( _Y_ ) + CVaR _α_ ( _W_ )


for any two loss functions _Y, W_ and _α ∈_ (0 _,_ 1) _._


**Exercise** **11.5**



(a) Suppose a loss function _Y_ has normal distribution with mean _μ_ and variance
_σ_ [2] ; that is, _Y_ _∼_ _N_ ( _μ, σ_ [2] ). For _α_ _∈_ (0 _,_ 1) determine both VaR _α_ ( _Y_ ) and
CVaR _α_ ( _Y_ ) in terms of the standard normal cumulative function




   - _x_
Φ( _x_ ) =



_−∞_



1
~~_√_~~

2 _π_ _[e][−][t]_ [2] _[/]_ [2] _[dt.]_



In particular, show that


VaR0 _._ 95( _Y_ ) = _μ_ + 1 _._ 645 _σ,_ CVaR0 _._ 95( _Y_ ) = _μ_ + 2 _._ 06 _σ._



(b) Suppose a loss function _Y_ has lognormal distribution with log mean _μ_
and log variance _σ_ [2], that is, log( _Y_ ) _∼_ _N_ ( _μ, σ_ [2] ) _._ For _α_ _∈_ (0 _,_ 1) determine
both VaR _α_ ( _Y_ ) and CVaR _α_ ( _Y_ ) in terms of the standard normal cumulative
function




   - _x_
Φ( _x_ ) =



_−∞_



1
~~_√_~~

2 _π_ _[e][−][t]_ [2] _[/]_ [2] _[dt.]_



**Exercise** **11.6** The Excel spreadsheet “Exercise 11.6 Twelve Portfolios” provides scenarios (based on historical data) for the joint annual returns of 12
industry portfolios in the US market.


(a) Any given portfolio attains its “worst” return in some scenario. For example,
a “NoDur” portfolio attained its worst return in 1931 whereas a “Hlth”
portfolio attained its worst return in scenario 1929.
Find a long-only portfolio that maximizes the worst possible return.


192 **Stochastic** **Programming** **Models:** **Risk** **Measures**


(b) Find the long-only portfolio that maximizes the expected return while ensuring that its worst possible return is no lower than 2% below what you found
in part (a).


**Exercise** **11.7** The Excel spreadsheet “Exercise 11.7 Three Bonds” provides a
(hypothetical) discrete distribution for the future value of three different bonds.
In each case, the first value is the “benchmark” future value in the case of
no credit quality change. For simplicity assume the three bonds have the same
current value, say $100.
The spreadsheet also has the joint distribution for the future values of the
three bonds (64 = 4 _∗_ 4 _∗_ 4 possible scenarios) assuming that the probability
distributions are independent.


                          - �T
(a) For a given bond portfolio **x** = _x_ 1 _x_ 2 _x_ 3, use the loss function discussed in Section 11.3,



_Y_ = ( **b** _−_ _**ω**_ ) [T] **x** =



�3

( _bj_ _−_ _ωj_ ) _xj,_

_j_ =1



where _bj_ is the benchmark future value of bond _j_, and _ωj_ is the random
future value of bond _j_ for _j_ �= 1 _,_ 2 _,_ 3 _._ Determine�T the VaR0 _._ 95 and CVaR0 _._ 95
values of the portfolio **x** = 0 _._ 4 0 _._ 1 0 _._ 5 .

                                  - �T
(b) Set up a CVaR optimization model to find a portfolio **x** = _x_ 1 _x_ 2 _x_ 3

with _xj_ _≥_ 0 _,_ _x_ 1 + _x_ 2� + _x_ 3 = 1, with�T the same benchmark future value as

that of the portfolio 0 _._ 4 0 _._ 1 0 _._ 5, and with minimum CVaR0 _._ 95. What
is the VaR0 _._ 95 value of the optimal portfolio? What is the optimal portfolio?


**Exercise** **11.8** The Excel spreadsheet “Exercise 11.8 Six Bonds” provides a
(hypothetical) discrete distribution for the annual return of six different bonds.
The return of each individual bond only has two possible values. The first
value is the “benchmark” return in the case of no credit quality downgrade. The
second value is the return in the case of credit downgrade.
The Excel file also contains the joint distribution for the returns of the six
bonds (64 = 2 [6] possible scenarios) assuming that the probability distributions
are independent.
Suppose you currently have $100 and need to fulfill an obligation of $115 in
a year. You intend to invest the $100 in the six bonds to try to meet the $115
obligation. You realize that because of the bonds’ credit risks you may not be
able to meet this financial goal in some scenarios. In such a case you will need
extra money to cover the _shortfall_ ; that is, the difference between the obligation
and whatever you can cover. For instance, if the bond portfolio in a year is worth
$105 _<_ $115, then the shortfall would be $10 = $115 _−_ $105. On the other hand,
if the bond portfolio in a year is $120 _>_ $115, then the shortfall would be zero.


**11.5** **Exercises** 193


(a) Formulate a linear programming model to determine how much should be
invested in each bond so that the expected value of the shortfall a year from
now is minimized. Assume the portfolio must be long-only.
Formulate your linear programming model in Excel and solve it.
What is the composition of the optimal portfolio, that is, the amount of
money in bond _i_, for _i_ = 1 _, . . .,_ 6?
What is the expected value of the shortfall?
What is the value of the worst (largest) possible shortfall?
(b) Define the _loss_ _function_ of your bond portfolio as the value of the liability
minus the value of your portfolio.
(i) Compute the numerical value of CVaR0 _._ 95 of this loss function if your
portfolio is equally divided among the six bonds.
(ii) Find the long-only portfolio of these six bonds that minimizes CVaR0 _._ 95.
What is the optimal CVaR0 _._ 95 value of this portfolio?


## **Part III** **Multi-Period Models**


## 12 Multi-Period Models: Simple Examples

The next few chapters will be devoted to _multi-period_ _models_ . Unlike the singleperiod models we have discussed so far, multi-period models incorporate the
dynamic nature inherent when decisions are made at different stages. The decisions to be made at each particular stage can adapt to information collected
in previous stages. In this chapter we discuss the following fundamental multiperiod models: the Kelly criterion for repeated gambles, dynamic portfolio optimization with myopic strategies, and optimal scheduling of trades to control
execution costs. The strong assumptions made in these models allow us to solve
them with relatively simple techniques. Subsequent chapters will introduce more
involved techniques for multi-period models, namely _dynamic_ _programming_ and
_stochastic programming_ . We will rely on these techniques to tackle more elaborate
financial optimization models.


**12.1** **The** **Kelly** **Criterion**


The Kelly criterion is a classical formula derived to maximize the average rate
of growth of a gambler’s fortune in a sequence of bets published in the landmark paper by Kelly (1956). The formula has appeal among some investment
professionals. In particular, there are claims that many successful investors,
including Edward Thorp, Warren Buffett, and Bill Gross, use Kelly-like methods.
The popular book _Fortune’s_ _Formula_ (Poundstone, 2005) gives a non-technical
and engaging description of the Kelly criterion and its role in gambling and
investing.
The Kelly formula can be explained as follows. Suppose a gambler can enter
a bet with two possible outcomes: lose the entire amount bet or win the amount
bet. Assume the probability of winning is _p_ . Suppose a gambler starts with some
initial wealth _W_ 0 and can take this gamble repeatedly. What fraction of her
current wealth should she bet each time?
To answer this question, let _Wn_ be the gambler’s wealth after _n_ gambles. The
rate of growth of the gambler’s fortune is




[1] _[W][n]_

_n_ [log] _W_ 0



_g_ = [1]



_._
_W_ 0


198 **Multi-Period** **Models:** **Simple** **Examples**


Suppose the gambler bets a fraction _f_ of her current wealth each time. Then


_Wn_ = (1 + _f_ ) _[k]_ (1 _−_ _f_ ) _[n][−][k]_ _W_ 0 _,_


where _k_ is the number of wins (out of the _n_ gambles).
Therefore we get




_[k]_ _[n][ −]_ _[k]_

_n_ [log(1 +] _[ f]_ [) +] _n_



_g_ = _[k]_



log(1 _−_ _f_ ) _._
_n_



Taking expectations, we get


E( _g_ ) = _p_ log(1 + _f_ ) + (1 _−_ _p_ ) log(1 _−_ _f_ ) _._


This function of _f_ attains its maximum at _f_ = 2 _p −_ 1. That is, by betting the
fraction 2 _p −_ 1 each time, the gambler maximizes the _expected_ growth rate _g_ .
The above reasoning and formula can be extended to gambles where the payoff
does not necessarily match the amount bet, and to gambles with a non-binary
outcome. We can indeed see the Kelly criterion as a special case of the dynamic
portfolio optimization model discussed next.


**12.2** **Dynamic** **Portfolio** **Optimization**


Our first dynamic portfolio optimization model concerns the expected utility
of final wealth, assuming the portfolio can be rebalanced at intermediate steps.
More specifically, suppose that an investor starts at _t_ = 0 with an initial endowment _W_ 0. At times _t_ = 0 _, . . ., T_ _−_ 1 the investor invests her wealth _Wt_ in a
portfolio of one risk-free asset and any number of risky assets. The investor’s
goal is to maximize the utility of terminal wealth _U_ ( _WT_ ) at time _T_ for a suitable
utility function _U_ ( _W_ ). We next describe a formal model for this dynamic portfolio optimization problem. To that end, we introduce the following convenient
notation:


_•_ _Rt_ +1 = gross random returns of the assets in period [ _t, t_ + 1] _,_


_Rf,t_ +1 = gross risk-free return in period [ _t, t_ + 1] _,_


_Rp,t_ +1 = gross random return of the investor’s portfolio in period [ _t, t_ + 1].

_•_ Decision variables: **x** _t_ = holdings (percentages) in the risky assets at time _t_ .

_•_ Inter-temporal constraints (also known as law of motion):


_Wt_ +1 = _Wt · Rp,t_ +1

                 -                  = _Wt ·_ _Rf,t_ +1 + ( _Rt_ +1 _−_ _Rf,t_ +1 **1** ) [T] **x** _t_ _,_ _t_ = 0 _, . . ., T_ _−_ 1 _._


_•_ Objective: max E[ _U_ ( _WT_ )].


**12.2** **Dynamic** **Portfolio** **Optimization** 199


12.2.1 Optimality of Myopic Policies


The solution of a multi-period model typically requires dynamic or stochastic
programming techniques that we will cover in later chapters. However, under
suitable assumptions the above model is sufficiently simple that we can solve it
directly. Observe that the final accumulated wealth at stage _T_ is



_WT_ = _W_ 0 _·_




- _T_

_Rp,t._

_t_ =1



We will primarily consider the class of constant relative risk-aversion utilities
given by the _power utility U_ ( _W_ ) = _W_ [1] _[−][γ]_ _/_ (1 _−_ _γ_ ) with risk aversion _γ_ _>_ 0 _,_ _γ_ = 1
and the _logarithmic_ _utility_ _U_ ( _W_ ) = log( _W_ ). Observe that log( _W_ ) = lim _γ→_ 1
_W_ [1] _[−][γ]_ _/_ (1 _−_ _γ_ ).
For a power utility _U_ ( _W_ ) = _W_ [1] _[−][γ]_ _/_ (1 _−_ _γ_ ) we get



(1 _−_ _γ_ ) _· U_ ( _WT_ ) = _WT_ [1] _[−][γ]_ = _W_ 0 [1] _[−][γ]_ _·_


For logarithmic utility _U_ ( _W_ ) = log( _W_ ) _,_ we get


       - _T_




- _T_

_Rp,t_ [1] _[−][γ][.]_
_t_ =1



_U_ ( _WT_ ) = log( _W_ 0) +



log( _Rp,t_ ) _._

_t_ =1



From these expressions for the utility of final wealth, we can readily reach the
following conclusions:


_•_ If the risk-free return _Rf,t_ = _Rf_ is the same for _t_ = 1 _, . . ., T_ and the risky
returns _Rt_ are independent for _t_ = 1 _, . . ., T_, then each **x** _t_ is the solution to
a single-period problem. In other words, a _myopic_ policy is optimal.

_•_ If the risk-free return _Rf,t_ = _Rf_ is the same for _t_ = 1 _, . . ., T_ and the
risky returns _Rt_ are independent and identically distributed (i.i.d.) for
_t_ = 1 _, . . ., T_, then all **x** _t_ are the same.

_•_ For _U_ ( _W_ ) = log( _W_ ) _,_ a myopic policy is optimal regardless of the distribution
of the returns _Rt, Rf,t,_ for _t_ = 1 _, . . ., T_ .


The above conclusions can be related to the following two classical puzzles of
finance (Kritzman, 2002):


_•_ Half stocks all the time or all stocks half the time?

_•_ Time diversification: Is it true that lengthening the investment horizon reduces
risk?


The first puzzle can be more precisely stated as follows. Suppose there is a
risky asset “stocks” with expected return _μ_ and standard deviation _σ_, and a
risk-free asset with return _r_ _<_ _μ_ . Consider the following two possible dynamic
investment strategies:


_•_ balanced strategy (50%, 50%) in every period;

_•_ switching strategy (100%, 0%) half of the time and (0%, 100%) the other half.


200 **Multi-Period** **Models:** **Simple** **Examples**


Suppose the risk-free return is constant, the stock returns are i.i.d. across time,
and an investor has a power utility. Which of the two strategies is preferable?
The second puzzle can be more precisely stated as follows. Suppose there is
a risky asset “stocks” with expected return _μ_ and standard deviation _σ_, and a
risk-free asset with return _r_ _<_ _μ_ . Suppose the risk-free return is constant, the
stock returns are i.i.d. across time, and an investor has a power utility with risk
aversion _γ_ _>_ 0. Is it true that if the investor’s investment horizon is _T_ _≫_ 1 then
she should initially hold a higher percentage of her portfolio in stocks than if her
horizon is _T_ = 1? In his book, Kritzman (2002) expertly discusses the answers
to these puzzles as well as a few others.


12.2.2 An Example Where a Myopic Policy Is Not Optimal


It is important to understand that the above conclusion concerning the optimality of myopic policies relies on strong assumptions on the asset returns, the
investor’s utility, and the fact that the investor only receives an initial endowment
at time 0 and maximizes her utility of wealth at the final time _T_ . The following
simple example illustrates a case when a myopic policy is not optimal.


_•_ Consider a three-stage (two-period) problem, i.e., _T_ = 2.

_•_ At _t_ = 0 we can invest in a one-period bond or a two-period zero-coupon
bond.

_•_ At _t_ = 0 we know that the risk-free interest rate is _Rf,_ 1 = 1 _._ 1.

_•_ At _t_ = 0 we know that at _t_ = 1 the risk-free interest rate will be as follows:

             1 _._ 12 with prob 1 _/_ 2 _,_
_Rf,_ 2 = 1 _._ 08 with prob 1 _/_ 2 _._


_•_ The one-period bond is a contract that can be entered at _t_ = 0 and delivers
$1 _._ 1 at time _t_ = 1 for each dollar invested.

_•_ The two-period bond is a contract that can be entered at _t_ = 0 and delivers
$1 _._ 2096 at time _t_ = 2 for each dollar invested. The value of the two-period
bond at time _t_ = 1 depends on the risk-free interest rate at that time. Its
value _V_ at _t_ = 1 per dollar invested is the 1 _._ 2096 final payout discounted
at the applicable rate:



1 _._ 2096

= 1 _._ 12 with prob 1 _/_ 2 _._
1 _._ 08



_V_ =



⎧
⎪⎨


⎪⎩



1 _._ 2096

= 1 _._ 08 with prob 1 _/_ 2 _,_
1 _._ 12




_•_ A myopic investor is one with investment horizon _T_ = 1; a long-term investor
is one with investment horizon _T_ = 2.

_•_ What would a risk-averse myopic investor do at time 0?

_•_ What would a risk-averse long-term investor do at time 0?


**12.3** **Execution** **Costs** 201


**12.3** **Execution** **Costs**


The efficient management of trading costs is a challenge to all institutional
investors. These costs are associated with commissions, bid–ask spreads, opportunity costs of waiting, and the price impact of trading. These types of costs
generally have a substantial impact on investment performance. For instance,
a classical study of P´erold (1988) shows that a hypothetical “paper” portfolio
constructed according to Value Line rankings outperforms the market by almost
20% during the period from 1965 to 1986. However, the actual portfolio     - the
Value Line Fund      - outperformed the market by only 2.5% per year. The difference between these figures arises from execution costs. This “implementation
shortfall” is surprisingly large and highlights the importance of execution-cost
control, particularly for institutional investors whose trades often constitute a
large fraction of the average trading volume of many stocks. A common and
intuitive practice is to spread large execution orders over a period of time, e.g.,
a few hours or days. This scheduling of trades aims to find a balance between
two conflicting objectives: on the one hand, fast execution generates large market
impact and consequently generates large costs. These costs are related to liquidity
as well as leakage of information. On the other hand, delayed execution reduces
market impact but comes at the expense of greater uncertainty and opportunity
risk. Suitable models of price dynamics and market impact lead to insightful
conclusions on the tradeoff faced between these extremes.
One of the first formal models for trade execution was proposed by Bertsimas
and Lo (1998) and is based on dynamic programming techniques. As we will
see, their model shows that, under suitable conditions, the naive strategy of
dividing a large order equally across the trading period minimizes expected
trading cost. However, the model concentrates on expected cost only and does
not take into consideration the risk (variance) of trading costs. This led Almgren
and Chriss (2000) to propose a model that finds an optimal tradeoff between
expected cost and risk. We next discuss the Almgren–Chriss trade execution
model in detail. In its original form, this model can be presented in a relatively simple conceptual framework. Furthermore, the Almgren–Chriss model
underlies several more elaborate execution models developed over the last few
years.


12.3.1 Almgren–Chriss Trade Execution Model


We first introduce formal definitions associated with a trading strategy and price
dynamics for the execution of a sell program for a single security. The definitions
and model for a buy program are similar.
Assume we hold a block of _X_ units of a security that needs to be liquidated
by time _T_ . Divide the time interval [0 _, T_ ] into _N_ intervals of length _τ_ := _T/N_,
and define the discrete times _tk_ = _kτ_, for _k_ = 0 _,_ 1 _, . . ., N._


202 **Multi-Period** **Models:** **Simple** **Examples**


Define a _trading_ _trajectory_ as a vector

                      - �T
**x** = _x_ 0 _x_ 1 _· · ·_ _xN_ _._


Here _xk_ = the number of units that we plan to hold at time _tk_ . We have _boundary_
_conditions_ associated with our initial holding, i.e., _x_ 0 = _X_, and liquidation at
time _T_, i.e., _xN_ = 0.
The trading trajectory implies a _trade_ _list_

                        - �T
**y** = _y_ 1 _· · ·_ _yN_ _,_



where _yk_ = _xk−_ 1 _−_ _xk_ . Each _yk_ is the number of units sold in the time interval

[ _tk−_ 1 _, tk_ ] _._
An _execution_ _trading_ _strategy_ is a rule for determining the trade size _yk_ given
the information available at time _tk−_ 1.
We also need a model for the price dynamics of the security. Assume the
initial security price (at time 0) is _S_ 0. The security price evolves according to
two exogenous factors, volatility and drift, and one endogenous factor, market
impact. Volatility and drift are assumed to be the result of market forces that
occur independently of our trading. On the other hand, as market participants
begin to detect the volume we are selling, they naturally adjust their bids downward. We distinguish two types of market impact: _temporary_ and _permanent_ .
Temporary impact is the change in price in a single time interval due to the
imbalance between supply and demand occurring as a result of our trading.
Permanent impact is the equilibrium change in price due to our trading that
lasts for the entire life of our liquidation.
Assume the security price evolves according to a discrete arithmetic random
walk in addition to a term that accounts for permanent impact. The security
price at time _tk_ is given by




          _Sk_ = _Sk−_ 1 + _στ_ [1] _[/]_ [2] _ξk −_ _τg_ _yk_
_τ_







for _k_ = 1 _, . . ., N._ Here _σ_ represents the asset volatility, _ξk_ _∼_ _N_ (0 _,_ 1), and the
permanent impact _g_ ( _v_ ) depends on the average rate of trading _v_ = _yk/τ_ during
the interval [ _tk−_ 1 _, tk_ ].
We next incorporate the temporary market impact. The intuition is that a
trader that liquidates _yk_ units during the interval [ _tk−_ 1 _, tk_ ] may see the price
decrease as a result of limited liquidity. We assume that this effect is short-lived
and in particular liquidity returns after each time interval. To model this impact,
we incorporate a price impact function _h_ ( _v_ ) that affects the actual price per share
received for trade _yk_ :




      _S_ ˜ _k_ = _Sk−_ 1 _−_ _h_ _yk_
_τ_




_._



However, the effect of _h_ ( _v_ ) does not appear in the next market price _Sk_ .
Given the above trading model, we can compute the execution cost resulting
from trading along a certain trajectory. The _captured value_ of a trading trajectory


**12.3** **Execution** **Costs** 203


is the total revenue obtained after liquidation. Some straightforward calculations
show that this equals




_._ (12.1)



�� - _N_ - _yk_
_xk −_ _ykh_

_τ_
_k_ =1




- _N_

_S_ ˜ _kyk_ = _S_ 0 _X_ +

_k_ =1




- _N_


_k_ =1




- _στ_ [1] _[/]_ [2] _ξk −_ _τg_ _yk_
_τ_



The _total_ _cost_ _of_ _trading_ or _implementation_ _shortfall_ is the difference between
the initial book value of the position and the captured value:




- _N_


_k_ =1



��
_xk._





_−_




- _N_ - _yk_

_ykh_
_τ_
_k_ =1




- _στ_ [1] _[/]_ [2] _ξk −_ _τg_ _yk_
_τ_



_C_ ( **x** ) = _S_ 0 _X_ _−_




- _N_

_S_ ˜ _kyk_ =

_k_ =1



Consequently, given the above price dynamics, it follows that the expected
shortfall E( **x** ) and variance of shortfall _V_ ( **x** ) are respectively



��




- _yk_
+ _τg_
_τ_




- _yk_
_ykh_
_τ_



E( **x** ) := E( _C_ ( **x** )) =




- _N_


_k_ =1



and




  - _N_
_V_ ( **x** ) = _σ_ [2] _τx_ [2] _k_ _[.]_

_k_ =1



The units of E( **x** ) are dollars, and the units of _V_ ( **x** ) are dollars squared.
For simplicity of exposition, we will make the following assumptions:


_•_ the temporary impact function is linear _h_ ( _v_ ) = _ηv_ ;

_•_ there is no permanent impact;

_•_ _τ_ = 1.


It is possible to extend the model and results when these assumptions are relaxed.
Under the above assumptions, the expected shortfall is




- _N_

_yk_ [2] _[.]_
_k_ =1



E( **x** ) =




- _N_

_ykh_ ( _yk_ ) = _η_

_k_ =1



Consider the problem of finding the trading trajectory that minimizes expected
shortfall:



min _η_
**y**




- _N_

_yk_ [2]
_k_ =1



s.t.




- _N_

_yk_ = _X._

_k_ =1



It is easy to see that the solution to this problem is the equally divided trade list


_yk_ = _[X]_ _[k]_ [= 1] _[, . . ., N.]_

_N_ _[,]_


204 **Multi-Period** **Models:** **Simple** **Examples**


This corresponds to the _linear_ trajectory


_[−]_ _[k]_
_xk_ = _[N]_ _X,_ _k_ = 1 _, . . ., N._

_N_


This linear trajectory has a natural connection to the so-called volume-weighted
average price (VWAP) strategy. The VWAP over the trading period [0 _, T_ ] is
defined as

       - _N_



VWAP :=



_VkSk_

_k_ =1

- _N_

_Vk_

_k_ =1



=




- _N_

_ukSk._

_k_ =1



Here _Vk_ stands for the volume traded during the _k_ th time interval [ _tk−_ 1 _, tk_ ] and
_uk_ stands for the percentage of daily volume traded during the same interval.
The VWAP strategy trades in proportion to the traded volume during an
interval, i.e., it is the following strategy:


_yk_ := _ukX._


It is easy to see that the VWAP strategy minimizes expected shortfall when the
temporary impact function is linear in the fraction of total volume traded, i.e.,
when _h_ ( _yk_ ) = _η ·_ ( _yk/Vk_ ).
Observe that the linear trajectory


_[−]_ _[k]_
_xk_ = _[N]_ _X,_ _k_ = 1 _, . . ., N_

_N_


has expected shortfall

E( **x** ) = _η_ _[X]_ [2]

_N_

and variance

_[−]_ [1)(2] _[N]_ _[−]_ [1)]
_V_ ( **x** ) = [(] _[N]_ _σ_ [2] _X_ [2] _._

6 _N_


Consider the extreme urgency strategy that liquidates the entire position during
the first period:


_y_ 1 = _X,_ _y_ 2 = _· · ·_ = _yN_ = 0 _,_ _x_ 1 = _· · ·_ = _xN_ = 0 _._


This trajectory has variance zero and expected shortfall _ηX_ [2] .


12.3.2 Efficient Frontier of Optimal Execution


The two execution strategies above suggest that we consider a tradeoff between
the two objectives E( **x** ) and _V_ ( **x** ). In analogy to Markowitz’s mean–variance
framework, Almgren and Chriss (2000) define an execution strategy to be _effi-_
_cient_ if no other strategy has both lower expected shortfall and lower variance.


**12.3** **Execution** **Costs** 205


Just like in the mean–variance context, there are several equivalent formulations
for efficient execution strategies. A computationally convenient formulation is:


min E( **x** ) + _λV_ ( **x** )
**x**

s.t. _x_ 0 = _X_ (12.2)
_xN_ = 0


for some risk-aversion parameter _λ_ _>_ 0. For convenience, put _U_ ( **x** ) := E( **x** ) +
_λV_ ( **x** ). We can think of _U_ as a “disutility” function. Using the expressions for
expected value and variance of shortfall, we obtain




- _N_



_x_ [2] _k_ _[.]_
_k_ =1



_U_ ( **x** ) = _η_




- _N_ - _N_

( _xk −_ _xk−_ 1) [2] + _λσ_ [2]

_k_ =1 _k_ =1



In particular, _U_ ( **x** ) = E( **x** ) + _λV_ ( **x** ) is a convex quadratic function. The optimality conditions for (12.2) are


_∂U_
( **x** ) = 2( _λσ_ [2] + 2 _η_ ) _xk −_ 2 _η_ ( _xk−_ 1 + _xk_ +1) = 0 _,_
_∂xk_


for _k_ = 1 _,_ 2 _, . . ., N_ _−_ 1, together with the boundary conditions


_x_ 0 = _X,_ _xN_ = 0 _._



The latter system of equations can be written as
⎡



⎡

⎢⎢⎢⎣



_x_ 1
_x_ 2
...
_xN_ _−_ 1



⎤

⎥⎥⎥⎥⎥⎦



⎡

⎢⎢⎢⎣



_X_
0
...
0



⎤


=
⎥⎥⎥⎦



⎤

⎥⎥⎥⎦



⎢⎢⎢⎢⎢⎣



2 + _λσ_ [2] _/η_ _−_ 1 0 _· · ·_ 0

_−_ 1 2 + _λσ_ [2] _/η_ _−_ 1 _· · ·_ 0
... ... ... ... ...
0 _· · ·_ _−_ 1 2 + _λσ_ [2] _/η_ _−_ 1
0 _· · ·_ 0 _−_ 1 2 + _λσ_ [2] _/η_



and _x_ 0 = _X,_ _xN_ = 0 _._
For _N_ large, the discussion below shows that the solution to this system of
equations is approximately


_[−]_ _[j]_ [))]
_xj_ = [sinh(] _[κ]_ [(] _[N]_ _· X,_ _j_ = 0 _,_ 1 _, . . ., N,_

sinh( _κN_ )


where _κ_ is the _urgency_ parameter,



_κ_ :=




~~�~~
_λσ_ [2]

_η_ _[.]_



Efficient Frontier in Continuous Time


We can extend the results from the previous section to the continuous-time
setting. The mathematics is a bit cleaner and more elegant. This is an idealized
model where we assume that the trade can be executed continuously over the
time interval [0 _, T_ ] _._


206 **Multi-Period** **Models:** **Simple** **Examples**


In this case we need to determine a continuous trading trajectory _x_ ( _t_ ) _,_ _t_ _∈_

[0 _, T_ ] _,_ with boundary conditions _x_ (0) = _X,_ _x_ ( _T_ ) = 0. We extend the security
price dynamics to the continuous-time setting. Again, for simplicity we shall
assume that there is only temporary impact. The price dynamics for the market
price is an arithmetic Brownian motion


_S_ ( _t_ ) = _S_ (0) + _σB_ ( _t_ ) _,_


and the actual execution price received at time _t_ is


_S_ ˜( _t_ ) = _S_ ( _t_ ) _−_ _ηy_ ( _t_ ) _,_



where _y_ ( _t_ ) := _−x_ ˙ ( _t_ ) is the rate of execution at time _t_ .
From properties of the stochastic integral, we get the following expression for
the execution shortfall:




       - _T_
_C_ ( _x_ ) = _XS_ (0) _−_



_T_ - _T_

_x_ ˙ ( _t_ ) [2] _dt −_ _σ_
0 0



_T_ - _T_

_S_ ˜( _t_ ) _y_ ( _t_ ) _dt_ = _η_
0 0



_x_ ( _t_ ) _dB_ ( _t_ ) _._
0



Therefore the expected shortfall E( _x_ ) and variance of shortfall _V_ ( _x_ ) are as
follows:



_T_ - _T_

_x_ ˙ ( _t_ ) [2] _dt,_ _V_ ( _x_ ) = _σ_ [2]
0 0




    - _T_
E( _x_ ) = _η_



_x_ ( _t_ ) [2] _dt._
0



An efficient execution trajectory is the solution to the following problem:



min
_x_ ( _t_ )




- _T_

( _η_ ˙ _x_ ( _t_ ) [2] + _λσ_ [2] _x_ ( _t_ ) [2] ) _dt_
0



s.t. _x_ (0) = _X_
_x_ ( _T_ ) = 0 _._


This is a problem in _calculus_ _of_ _variations_ . The _Euler_ _equation_ for this problem (see formula (A.1) in Section A.3) yields the following ordinary differential
equation:



with boundary conditions



_x_ ¨( _t_ ) = _[λσ]_ [2] _· x_ ( _t_ ) _,_

_η_


_x_ (0) = _X,_ _x_ ( _T_ ) = 0 _._



The solution to this differential equation is


_[−]_ _[t]_ [))]
_x_ ( _t_ ) = [sinh(] _[κ]_ [(] _[T]_ _· X,_ _t ∈_ [0 _, T_ ] _,_

sinh( _κT_ )


where _κ_ is an “urgency” parameter, defined by



_κ_ :=




_λσ_ [2]

_η_ _[.]_



The parameter _κ_ has the following nice interpretation. The reciprocal _θ_ := 1 _/κ_ is
measured in units of time and can be interpreted as the “half-life” of the trade.


**12.3** **Execution** **Costs** 207


More precisely, when _T_ _→∞_, the trade is reduced by a factor of _e_ = 2 _._ 71828 _. . ._
by time _θ_ .
It is insightful to verify the units of the various parameters of our model. The
units of _σ_ [2] _, η,_ and _λ_ are as follows:


currency [2]
_σ_ [2] :

volume [2] _·_ time


_η_ : [currency] _[ ·]_ [ time]

volume [2]


1
_λ_ :
currency _[.]_



Recall that the urgency parameter is


_κ_ =




~~�~~
_λσ_ [2]

_η_ _[.]_



Therefore, the units of _θ_ = 1 _/κ_ are indeed units of time.


Multiple-Security Portfolios


The previous execution model and results can be extended to the case when

                        - �T
we need to liquidate a whole portfolio _X_ = _X_ 1 _· · ·_ _Xm_ of _m_ securities.
In� this case, the� _trading_ T _trajectory_ is a sequence of _m_ -dimensional vectors **x** _k_ =
_x_ 1 _k_ _· · ·_ _xmk_ _, for_ _k_ = 0 _, . . ., N_ . The trade list is also a sequence of _m_ dimensional vectors **y** _k_ = **x** _k−_ 1 _−_ **x** _k,_ _k_ = 1 _, . . ., N_ .
For simplicity we shall assume that there is only a linear temporary impact
and _τ_ = 1. Hence the security prices _Sk_ follow a multi-dimensional random walk:


_Sk_ = _Sk−_ 1 + _ξk._


Here _ξk_ _∼_ _N_ (0 _,_ Σ), where Σ is the covariance matrix of the _m_ security prices.
We assume Σ to be symmetric and positive definite.
The prices actually received are


_S_ ˜ _k_ = _Sk −_ _H_ **y** _k,_


where _H_ is symmetric and positive semidefinite.
Proceeding as before, we get the following expressions for expected shortfall
and variance of shortfall respectively:




- _N_

( **x** _k −_ **x** _k−_ 1) [T] _H_ ( **x** _k −_ **x** _k−_ 1)

_k_ =1



E( **x** ) =




- _N_

**y** _k_ [T] _[H]_ **[y]** _[k]_ [=]
_k_ =1



and



_V_ ( **x** ) =




- _N_

**x** [T] _k_ [Σ] **[x]** _[k][.]_
_k_ =1


208 **Multi-Period** **Models:** **Simple** **Examples**


Now the set of efficient trading strategies is characterized by the solutions to the
quadratic program:


min E( **x** ) + _λV_ ( **x** )
**x**

s.t. **x** 0 = _X_
**x** _N_ = 0 _._


This is again a convex quadratic optimization problem. Its solution is



2 _H_ + _λ_ Σ _−H_ 0 _· · ·_ 0
_−H_ 2 _H_ + _λ_ Σ _−H_ _· · ·_ 0
... ... ... ... ...
0 _· · ·_ _−H_ 2 _H_ + _λ_ Σ _−H_
0 _· · ·_ 0 _−H_ 2 _H_ + _λ_ Σ



⎤ _−_ 1 ⎡



⎥⎥⎥⎥⎥⎦



⎡

⎢⎢⎢⎢⎢⎣



⎢⎢⎢⎣



⎡

**x** 1
**x** 2

⎢⎢⎢⎣ ...

**x** _N_ _−_ 1



⎤


=
⎥⎥⎥⎦



⎤

⎥⎥⎥⎦



_HX_
0
...
0



and **x** 0 = _X,_ **x** _N_ = **0** _._
Unlike for the one-security model, the above solution may not necessarily
satisfy the monotonicity constraints **x** _k_ _≤_ **x** _k−_ 1, with _k_ = 1 _, . . ., N_ . This means
that the above strategy may have trades that are “buys” at intermediate steps,
even though the execution is meant to liquidate a vector of positions. If this
possibility is not desirable, we can introduce the constraints **x** _k_ _≤_ **x** _k−_ 1, for _k_ =
1 _, . . ., N,_ into the optimization problem for efficient trajectories. The resulting
model no longer has a closed-form solution but it is still a quadratic program.
For particularly large portfolios, the size of the quadratic programs poses an
interesting computational challenge.


Adaptive Strategies


The models described above in discrete and continuous time assume _static_ trajectories. That is, the trajectories do not respond to changes during execution. It
is conceivable that an adaptive strategy that depends on the initial portion of the
trajectory could do better. In order to solve these kinds of optimization problems
we need to rely on _dynamic_ _programming_ techniques. These are generally more
challenging optimization problems. The next chapter introduces this powerful
technique.


12.3.3 Trade Execution Models in Practice


A trade execution model used by an institutional investor typically includes
other bells and whistles that we have not discussed, such as short-term alpha,
spread, permanent impact, and temporary impact. These additional features
can be incorporated in the model discussed in Section 12.3.1. An important
empirical observation is that, instead of a linear market impact, other forms
of market impact such as 1 _/_ 2 or 3 _/_ 5 powers of volume traded appear to be
more appropriate. In these cases the optimal execution problem is no longer a
quadratic program but it is still a convex program.


**12.4** **Exercises** 209


The estimation of market impact is a challenging practical problem. One
difficulty is the need for data at the execution level. Furthermore, even when
such data are available, market impact is not directly observable. Instead, we can
only observe the total realized impact, which includes permanent and temporary
impact as well as some random noise. Almgren et al. (2005) estimate the market
impact using linear regression, based on a large dataset of US equity brokerage
executions from Citigroup. The model is used to calibrate a version of the
Almgren–Chriss model with nonlinear temporary costs and is validated with
out-of-sample backtesting.


**12.4** **Exercises**


**Exercise** **12.1** Show that the Kelly criterion can be seen as a special case of
the dynamic portfolio optimization problem with the logarithmic utility of the
final wealth and a peculiar pair of risk-free and risky assets. Conclude that if
the payoff for each dollar invested is _b_ instead of 1, then the optimal fraction to
bet is
( _b_ + 1) _p −_ 1

_._
_b_


**Exercise** **12.2** Consider the following variation of the Kelly criterion. Suppose
at each betting round the gambler can bet on _two_ _independent_ _gambles._ For each
of the two gambles the following applies: if a gambler bets one dollar, then she
wins one dollar with probability _p_ and loses the dollar she bet with probability
1 _−_ _p_ .
Suppose the gambler starts with some initial wealth _W_ 0 and repeatedly bets on
the above two gambles. Determine the fractions _f_ 1 _, f_ 2 of wealth that she should
bet at each round in each of the two gambles to maximize the average growth
rate of her wealth.


**Exercise 12.3** Recall the example described in Section 12.2.2. You may choose
to prove the statements below formally or to verify them numerically. For the
latter, you may use the Excel spreadsheet “Exercise 12.3 Two Periods”.


(a) Suppose a myopic investor is risk-neutral; that is, her objective is to maximize E( _W_ 1) by investing her initial wealth in a long-only portfolio composed
of the one-period and the two-period bonds. Show that the investor would
be indifferent between the one- and the two-period bonds. In other words,
any long-only portfolio is optimal for the investor.
(b) Suppose a myopic investor has power utility with� risk-aversion� parameter

_γ_ _>_ 0; that is, her objective is to maximize E _W_ 1 [1] _[−][γ]_ _/_ (1 _−_ _γ_ ) . Show that
the investor would prefer to hold her entire portfolio in the one-period bond.
(c) Suppose a long-term investor is risk-neutral; that is, her objective is to
maximize the expected wealth E( _W_ 2) at time 2. Show that the investor


210 **Multi-Period** **Models:** **Simple** **Examples**


would choose to place her entire portfolio in the one-period bond at _t_ = 0
and roll it over at the risk-free rate at _t_ = 1.
(d) Suppose a long-term investor has power utility with risk-aversion parameter�      
_γ_ _>_ 1; that is, her objective is to maximize E _W_ 2 [1] _[−][γ]_ _/_ (1 _−_ _γ_ ) . Show that
the investor would prefer to hold part of her entire portfolio in the two-period
bond. Furthermore, show that the higher the risk aversion _γ_, the higher the
holding in the two-period bond.


**Exercise** **12.4** Prove identity (12.1) in the Almgren–Chriss model.


**Exercise** **12.5** Consider the following variation of the one-asset trading model
of Almgren and Chriss. Assume the security price at period _k_ is


_Sk_ = _Sk−_ 1 + _ξk_


and the actual security price received at period _k_ is


_S_ ˜ _k_ = _Sk−_ 1 _−_ _hk_ ( _yk_ ) _,_


where _hk_ ( _yk_ ) = _cyk/vk,_ _c_ is a constant, and _vk_ is the volume traded during the
_k_ th interval [ _k −_ 1 _, k_ ].


(a) Write down the expression for the shortfall, as a function of the trading

              - �T              - �T
trajectory _x_ 0 _x_ 1 _· · ·_ _xN_ and/or the trading list _y_ 1 _· · ·_ _yN_ .
(b) Write down the formulation for the problem of finding the trading list

        - �T
_y_ 1 _· · ·_ _yN_ that minimizes expected shortfall.
(c) Prove that the solution to the problem in part (b) is the VWAP strategy


_vk_
_yk_ = ~~�~~ _N_ _X,_ _k_ = 1 _, . . ., N._
_j_ =1 _[v][j]_


**Exercise** **12.6** Suppose today (year _t_ = 0) you have an initial endowment
_W_ 0 = $10 _,_ 000. Now (beginning of year 0), and at the beginning of the next 19
years, you can allocate your wealth to two investment choices:


1. A risk-free asset “cash” that generates a 5% annual return.

2. A risky asset “stocks” with annual return that is normally distributed with
mean 10% and standard deviation 20%.


Let _W_ 20 denote the endowment at the end of the 20-year investment period
(i.e., beginning of year 20).
Consider the following three investment strategies:


1. Buy and hold: Invest the initial endowment 50% in cash and 50% in stocks
and never rebalance.

2. Balanced: Rebalance the portfolio at the beginning of every year to a 50%
cash and 50% stocks mix.

3. Switching: Alternate each year between 100% cash and 100% stocks.


**12.4** **Exercises** 211


The Excel spreadsheet “Exercise 12.6 Twenty Years” contains a random sample of the risk-free and risky returns over a 20-year period.


(a) Compute the total accumulated return achieved by each of the three strategies. That is,
_W_ 20 _−_ 1 _._

_W_ 0


(b) Compute the annualized return achieved by each of the three strategies.
That is,

          - �1 _/_ 20
_W_ 20 _−_ 1 _._
_W_ 0


(c) Use your favorite simulation software to generate 10,000 random samples of
the risk-free and risky returns over a 20-year period. Report the sample mean
and sample variance of the total accumulated return and of the annualized
return for each of the three strategies.
(d) Produce charts (e.g., histograms) to visualize the distribution of total accumulated and annualized returns achieved by the three strategies. Which
strategy seems to have a higher expected annualized return? Which one
seems to have a higher variance of annualized return?
(e) Which strategy would you prefer? Why?


## 13 Dynamic Programming: Theory and Algorithms

Dynamic programming is an approach to model and solve multi-period decision
problems. The fundamental principle of dynamic programming is the _Bellman_
_equation_, a certain kind of optimality condition. As we detail in this chapter, the
central idea of the Bellman equation is to break down a multi-stage problem into
multiple two-stage problems. Under suitable conditions, the Bellman equation
yields a recursion that helps in characterizing the solution and in computing it.
Before embarking on a formal description, we illustrate the dynamic programming approach via some examples.


**13.1** **Some** **Examples**


**Example** **13.1** (Matches puzzle) Suppose there are 30 matches on a table and
I play the following game with a clever opponent: I begin by picking up 1, 2,
or 3 matches. Then my opponent must pick 1, 2, or 3 matches. We continue
alternating until the last match is picked up. The player who picks up the last
match loses. How can I (the first player) be sure of winning?


_Solution._ If I can ensure that it will be my opponent’s turn when 1 match remains,
I certainly win. Let us work backwards one step: If I can ensure that it will be
my opponent’s turn when 5 matches remain, I will also win. The reason for this
is that no matter what he does when there are 5 matches left, I can make sure
that when he has his next turn, only 1 match will remain. Hence it is clear
that I win if I can force my opponent to play when 5 matches remain. We can
continue working backwards and conclude that I will ensure victory if I can force
my opponent to play when 5, 9, 13, 17, 21, 25, or 29 matches remain. Since
the game starts with 30 matches on the table, I can ensure victory by picking
1 match at the beginning, bringing the number down to 29.


**Example** **13.2** (Knapsack problem) Given a set of items, each with a certain
weight and value, select the collection of items with total maximum value such
that their total weight does not exceed some fixed weight limit _W_ .


_Solution._ Let _wt_ _>_ 0 and _vt_ _>_ 0 be the weight and value respectively of item _t_ for
_t_ = 1 _, . . ., n_ . The knapsack problem can be formulated as an integer program and


**13.1** **Some** **Examples** 213


solved via the technique covered in Chapter 8.2. We next illustrate an alternative
approach via dynamic programming. Consider the problem as a sequence of
binary decisions _xt_ _∈{_ 0 _,_ 1 _}_ corresponding to “include” or “do not include”
item _t_ for _t_ = 1 _, . . ., n_ . To find the optimal selection of items, we can work
“backwards” as we did in the matches puzzle. Let _Wt_ be the remaining amount
of weight available at stage _t_ = 1 _, . . ., n_ with _W_ 1 = _W_, and let _Jt_ ( _Wt_ ) denote
the value of an optimal collection of items if we started selecting items at stage _t_
with remaining weight limit _Wt_ . The value function _Jt_ ( _Wt_ ) satisfies the following
backward recursion for _t_ = 1 _,_ 2 _, . . ., n −_ 1:

    _Jt_ ( _Wt_ ) = _J_ max _t_ +1 _{_ ( _WJt_ +1 _t_ ) ( _Wt_ ) _, Jt_ +1( _Wt −_ _wt_ ) + _vt}_ ifif _wwtt_ _> W≤_ _Wtt._ (13.1)


Our goal is to obtain the value _J_ 1( _W_ ) and the corresponding optimal collection
of items. The steps that lead to _J_ 1( _W_ ) in the above recursion are tied to the
optimal decisions _x_ _[∗]_ _t_ [for] _[t]_ [=] [1] _[, . . ., n][ −]_ [1.] [On] [the] [one] [hand,] _[x][∗]_ _t_ [=] [0] [corresponds]
to _Jt_ ( _Wt_ ) = _Jt_ +1( _Wt_ ); that is, do not select item _t_ . On the other hand, _x_ _[∗]_ _t_ [=] [1]
corresponds to _Jt_ ( _Wt_ ) = _Jt_ +1( _Wt −_ _wt_ ) + _vt._ Observe that for 0 _≤_ _Wn_ _≤_ _W_ the
last-stage value function satisfies

          _Jn_ ( _Wn_ ) = 0 _vn_ ifif _wwnn_ _> W≤_ _Wnn._


**Example** **13.3** (Optimal consumption problem) Assume that now (beginning
of year 0) you have an initial amount of wealth _W_ 0 _>_ 0. At the beginning of
year _t_ you choose to consume _Ct_ dollars and invest the rest of your wealth in
one-year treasury bills. You can consume at most the wealth available in year _t_ .
Consuming _Ct_ in year _t_ provides a utility _U_ ( _Ct_ ). On the other hand, each dollar
invested in one-year treasury bill yields 1+ _r_ dollars cash at the beginning of the
next year. Suppose you want to maximize your total utility of consumption over
the next _T_ years:

      - _T_



max
_C_ 0 _,...,CT_



_U_ ( _Ct_ ) _._

_t_ =0



How much should you consume each year?


_Solution._ The key to solving the optimal consumption problem is again to work
“backwards” in time just like we did in the matches puzzle and knapsack problem.
Let _Wt_ denote the amount of wealth available at the beginning of year _t_ and let
_Jt_ ( _Wt_ ) be the total utility of consumption from year _t_ to year _T_ if we start at year
_t_ with wealth _Wt_ . The value function _Jt_ ( _Wt_ ) satisfies the following backwards
recursion for _t_ = 0 _,_ 1 _,_ 2 _, . . ., T_ _−_ 1:


_Jt_ ( _Wt_ ) = max (13.2)
0 _≤Ct≤Wt_ _[{][J][t]_ [+1][((] _[W][t][ −]_ _[C][t]_ [)] _[ ·]_ [ (1 +] _[ r]_ [)) +] _[ U]_ [(] _[C][t]_ [)] _[}]_

and the maximizer _Ct_ _[∗]_ [is] [the] [optimal] [consumption] [level] [at] [year] _[t]_ [.] [Observe] [that]
for _WT_ _≥_ 0 the last-stage value function satisfies


_JT_ ( _WT_ ) = _U_ ( _WT_ )


214 **Dynamic** **Programming:** **Theory** **and** **Algorithms**


attained at the optimal consumption level _CT_ _[∗]_ [=] _[ W][T]_ [ .]


**13.2** **Model** **of** **a** **Sequential** **System** **(Deterministic** **Case)**


We next introduce the formal notation and terminology of dynamic programming. The presentation follows the approach popularized in the classical book of
Bertsekas (2005). For ease of exposition, we first consider the deterministic case.
That is, the context without random components.
A _sequential_ _system_ is defined by the following elements.


**Stages:** These are the points in time when decisions are made. We will normally
consider _t_ = 0 _,_ 1 _, . . ., T_ or _t_ = 1 _,_ 2 _, . . ., T_ .
**States:** The state of the system at a particular stage is the information that is
relevant for subsequent decisions. We will generally denote the state at
stage _t_ as **s** _t_, for _t_ = 0 _,_ 1 _, . . ., T_ . Sometimes it is convenient to include
also a “final state” **s** _T_ +1.
**Decisions:** These are also called controls or actions that we can make at each
stage and that affect the behavior of the system. We will generally denote
the decisions as **x** _t_, for _t_ = 0 _,_ 1 _, . . ., T_ .
**Law** **of** **motion:** This defines how the state of the system evolves. A general
law of motion has the form


**s** _t_ +1 = _ft_ ( **s** _t,_ **x** _t_ ) _,_ _t_ = 0 _,_ 1 _, . . ., T._


Assume we are interested in optimizing some overall objective function


      - _T_

_gt_ ( **s** _t,_ **x** _t_ ) + _gT_ +1( **s** _T_ +1) _,_ (13.3)

_t_ =0


where each _gt_ ( **s** _t,_ **x** _t_ ), for _t_ = 0 _,_ 1 _, . . ., T,_ and _gT_ +1( **s** _T_ +1) is some cost or reward
per stage. This defines a _sequential_ _decision_ _problem_ : find **x** _t_, for _t_ = 0 _,_ 1 _, . . ., T,_
to minimize the total cost or maximize the reward (13.3).
Both Examples 13.2 and 13.3 can be readily stated in this framework.


_Dynamic_ _programming_ _formulation_ _for_ _the_ _knapsack_ _problem_
**Stages:** _t_ = 1 _,_ 2 _, . . ., n._
**State** **at** **stage** _t_ **:** remaining weight capacity _Wt_ .
**Decision** **at** **stage** _t_ **:** binary variable _xt_ _∈{_ 0 _,_ 1 _}_ indicating whether to include
item _t_ or not. This decision is constrained to be _xt_ = 0 if _wt_ _> Wt_ as in
this case the weight of item _t_ exceeds the remaining weight capacity.
**Law** **of** **motion:** the remaining weight capacity at stage _t_ + 1 is the one from
stage _t_ reduced by _wt_ if item _t_ is included. Otherwise they are the same.
More precisely,


_Wt_ +1 = _Wt −_ _wtxt,_ _t_ = 1 _,_ 2 _, . . ., n −_ 1 _._


**13.3** **Bellman’s** **Principle** **of** **Optimality** 215


**Objective:** maximize the total value of the selected items


       - _n_



max
_t_ =1 _,...,n_



_vtxt._

_t_ =1



_Dynamic_ _programming_ _formulation_ _for_ _the_ _optimal_ _consumption_ _problem_
**Stages:** _t_ = 0 _,_ 1 _,_ 2 _, . . ., T._
**State** **at** **stage** _t_ **:** available wealth _Wt_ . It is also convenient to assume that
terminal wealth _WT_ +1 = 0.
**Decision** **at** **stage** _t_ **:** consumption _Ct_ _∈_ [0 _, Wt_ ].
**Law** **of** **motion:** the wealth at stage _t_ + 1 is the portion of wealth from stage _t_
that was not consumed increased by a factor 1 + _r_ . More precisely,


_Wt_ +1 = ( _Wt −_ _Ct_ )(1 + _r_ ) _,_ _t_ = 0 _,_ 1 _,_ 2 _, . . ., T._


**Objective:** maximize the total utility of consumption


       - _T_



max
_C_ 0 _,...,CT_


**13.3** **Bellman’s** **Principle** **of** **Optimality**



_U_ ( _Ct_ ) _._

_t_ =0



The heart of dynamic programming is a principle of optimality due to Bellman.
Its flavor was suggested by the solutions to Examples 13.1, 13.2, and 13.3.
To state the principle precisely, we need a bit of notation. Suppose we are
maximizing total reward







_J_ ( **s** 0) := max
**x** 0 _,...,_ **x** _T_





 - _T_

_gt_ ( **s** _t,_ **x** _t_ ) + _gT_ +1( **s** _T_ +1)

_t_ =0



Consider the “tail problem” that starts at stage _t_ :

         
     - _T_



_._




_._



_Jt_ ( **s** _t_ ) := max
**x** _t,...,_ **x** _T_



_gτ_ ( **s** _τ_ _,_ **x** _τ_ ) + _gT_ +1( **s** _T_ +1)

_τ_ = _t_



_Bellman’s optimality principle_ can be stated as follows. The value-to-go functions
_Jt_ ( _st_ ) satisfy the recursive relationship


_Jt_ ( **s** _t_ ) = max _{gt_ ( **s** _t,_ **x** _t_ ) + _Jt_ +1( _ft_ ( **s** _t,_ **x** _t_ )) _} ._ (13.4)
**x** _t_


The recursive relationship (13.4) is called the _Bellman_ _equation._ Observe that
the recursive relationships (13.1) and (13.2) are exactly the Bellman equation
(13.4) in the particular context of Examples 13.2 and 13.3 respectively.
There is a certain jargon associated with the solution to a sequential decision
problem and Bellman’s optimality principle. The function _Jt_ ( **s** _t_ ) is called the
_value-to-go_ _function_ _at_ _stage_ _t._ If the objective is to minimize a total cost,


216 **Dynamic** **Programming:** **Theory** **and** **Algorithms**


sometimes it is called the _cost-to-go_ _function_ . The solution **x** _[∗]_ _t_ [(] **[s]** _[t]_ [)] [of] [Bellman’s]
equation (13.4) at stage _t_ is called an _optimal decision rule at stage t._ Notice that
this solution depends on the state **s** _t_ at stage _t_ . The vector of optimal decision
rules ( **x** _[∗]_ 0 [(] _[·]_ [)] _[, . . .,]_ **[ x]** _[∗]_ _T_ [(] _[·]_ [))] [is] [called] [the] _[optimal]_ _[policy]_ [.]
Bellman’s optimality principle can be phrased as:


If ( **x** _[∗]_ 0 [(] _[·]_ [)] _[, . . .,]_ **[ x]** _[∗]_ _T_ [(] _[·]_ [))] [is] [an] [optimal] [policy] [for] [the] [entire] [problem,] [then]
( **x** _[∗]_ _t_ [(] _[·]_ [)] _[, . . .,]_ **[ x]** _T_ _[∗]_ [(] _[·]_ [))] [is] [an] [optimal] [policy] [for] [the] [tail] [problem] [beginning] [at]
stage _t_ .


**13.4** **Linear–Quadratic** **Regulator**


We next illustrate Bellman’s optimality principle with a popular model from
control engineering called the _linear–quadratic_ _regulator_ . It provides the foundation for a model of dynamic investment with transaction costs and predictable
returns that we will discuss in the next chapter. The linear–quadratic regulator
is a model for the problem of steering the location **s** _t_ of an object towards the
origin via a control input **u** _t_ . Instead of a constraint on the location of the object,
the linear–quadratic regulator imposes a penalty for deviating from the origin.
Assume the states and controls evolve according to the following linear law of
motion:


**s** _t_ +1 = **As** _t_ + **Bu** _t,_ _t_ = 0 _,_ 1 _, . . ., N_ _−_ 1 _._


Assume we have a quadratic cost function


_N_             - _−_ 1

( **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [) +] **[ s]** _N_ [T] **[Qs]** _[N]_ _[,]_
_t_ =0


where **Q** _,_ **R** are symmetric positive definite matrices of appropriate sizes.
The goal is to determine the optimal sequence of controls **u** _t, t_ = 0 _,_ 1 _, . . ., N_ _−_ 1 _,_
that minimize the above cost when the initial position of the object is _s_ 0:







_J_ ( **s** 0) := min
**u** 0 _,...,_ **u** _N_ _−_ 1




_N_ - _−_ 1

( **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [) +] **[ s]** _N_ [T] **[Qs]** _[N]_
_t_ =0



_._



We next apply the backwards dynamic programming principle. For the last stage
_N_ we evidently have


_JN_ ( **s** _N_ ) = **s** [T] _N_ **[Qs]** _[N]_ _[.]_


**13.4** **Linear–Quadratic** **Regulator** 217


For stage _N_ _−_ 1 we have the Bellman equation



_JN_ _−_ 1( **s** _N_ _−_ 1) = min
**u** _N_ _−_ 1


= min
**u** _N_ _−_ 1


= min
**u** _N_ _−_ 1




- **s** [T] _N_ _−_ 1 **[Qs]** _[N]_ _[−]_ [1] [+] **[ u]** [T] _N_ _−_ 1 **[Ru]** _[N]_ _[−]_ [1] [+] _[ J][N]_ [(] **[s]** _[N]_ [)]

**s** [T] _N_ _−_ 1 **[Qs]** _[N]_ _[−]_ [1] [+] **[ u]** [T] _N_ _−_ 1 **[Ru]** _[N]_ _[−]_ [1]

                  + ( **As** _N_ _−_ 1 + **Bu** _N_ _−_ 1) [T] **Q** ( **As** _N_ _−_ 1 + **Bu** _N_ _−_ 1)

**s** [T] _N_ _−_ 1 **[Qs]** _[N]_ _[−]_ [1] [+] **[ s]** [T] _N_ _−_ 1 **[A]** [T] **[QAs]** _[N]_ _[−]_ [1] [+ 2] **[s]** [T] _N_ _−_ 1 **[A]** [T] **[QBu]** _[N]_ _[−]_ [1]

            + **u** [T] _N_ _−_ 1 [(] **[R]** [ +] **[ B]** [T] **[QB]** [)] **[u]** _[N]_ _[−]_ [1] _._



The latter is a convex quadratic function of **u** _N_ _−_ 1. To find its minimum, we
compute its gradient and equate it to zero to obtain:


2 **B** [T] **QAs** _N_ _−_ 1 + 2( **R** + **B** [T] **QB** ) **u** _N_ _−_ 1 = **0** _._


Thus, the optimal control at stage _N_ _−_ 1 is


**u** _[∗]_ _N_ _−_ 1 [=] _[ −]_ [(] **[R]** [ +] **[ B]** [T] **[QB]** [)] _[−]_ [1] **[B]** [T] **[QAs]** _[N]_ _[−]_ [1] [=] **[ L]** _[N]_ _[−]_ [1] **[s]** _[N]_ _[−]_ [1] _[,]_


where


**L** _N_ _−_ 1 = _−_ ( **R** + **B** [T] **QB** ) _[−]_ [1] **B** [T] **QA** _._


Plugging this value of **u** _[∗]_ _N_ _−_ 1 [in] [the] [above] [expression] [for] _[J][N]_ _[−]_ [1][(] **[s]** _[N]_ _[−]_ [1][)] [we] [get]


_JN_ _−_ 1( **s** _N_ _−_ 1) = **s** [T] _N_ _−_ 1 **[Qs]** _[N]_ _[−]_ [1] [+] **[ s]** [T] _N_ _−_ 1 **[A]** [T] **[QAs]** _[N]_ _[−]_ [1]

_−_ **s** [T] _N_ _−_ 1 **[A]** [T] **[QB]** [(] **[R]** [ +] **[ B]** [T] **[QB]** [)] _[−]_ [1] **[B]** [T] **[QAs]** _[N]_ _[−]_ [1]
= **s** [T] _N_ _−_ 1 **[K]** _[N]_ _[−]_ [1] **[s]** _[N]_ _[−]_ [1] _[,]_


where


**K** _N_ _−_ 1 = **Q** + **A** [T] ( **Q** _−_ **QB** ( **R** + **B** [T] **QB** ) _[−]_ [1] **B** [T] **Q** ) **A** _._


Next we will prove by induction that


_Jt_ ( **s** _t_ ) = **s** [T] _t_ **[K]** _[t]_ **[s]** _[t][,]_ **[u]** _[∗]_ _t_ [=] **[ L]** _[t]_ **[s]** _[t][,]_


where


**K** _N_ = **Q** _,_

**K** _t_ = **Q** + **A** [T] ( **K** _t_ +1 _−_ **K** _t_ +1 **B** ( **R** + **B** [T] **K** _t_ +1 **B** ) _[−]_ [1] **B** [T] **K** _t_ +1) **A** _,_ _t_ = _N_ _−_ 1 _, . . .,_ 0 _,_


and


**L** _t_ = _−_ ( **R** + **B** [T] **K** _t_ +1 **B** ) _[−]_ [1] **B** [T] **K** _t_ +1 **A** _,_ _t_ = _N_ _−_ 1 _, . . .,_ 0 _._


218 **Dynamic** **Programming:** **Theory** **and** **Algorithms**


We already showed that the above holds for _t_ = _N −_ 1. Assume that it holds for
_t_ + 1. At stage _t_ we have the Bellman equation



_Jt_ ( **s** _t_ )


= min
**u** _t_


= min
**u** _t_


= min
**u** _t_




- **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [+] _[ J][t]_ [+1][(] **[s]** _[t]_ [+1][)]

- **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [+ (] **[As]** _[t]_ [+] **[ Bu]** _[t]_ [)][T] **[K]** _[t]_ [+1][(] **[As]** _[t]_ [+] **[ Bu]** _[t]_ [)]

- **s** [T] _t_ **[Qs]** _[t]_ [+] **[ s]** [T] _t_ **[A]** [T] **[K]** _[t]_ [+1] **[As]** _[t]_ [+ 2] **[s]** [T] _t_ **[A]** [T] **[K]** _[t]_ [+1] **[Bu]** _[t]_ [+] **[ u]** [T] _t_ [(] **[R]** [ +] **[ B]** [T] **[K]** _[t]_ [+1] **[B]** [)] **[u]** _[t]_ _._



The latter is a convex quadratic function of **u** _t_ . To find its minimum, we compute
its gradient and equate it to zero to obtain:


2 **B** [T] **K** _t_ +1 **As** _t_ + 2( **R** + **B** [T] **K** _t_ +1 **B** ) **u** _t_ = **0** _._


Thus, the optimal control at stage _t_ is

**u** _[∗]_ _t_ [=] _[ −]_ [(] **[R]** [ +] **[ B]** [T] **[K]** _[t]_ [+1] **[B]** [)] _[−]_ [1] **[B]** [T] **[K]** _[t]_ [+1] **[As]** _[t]_ [=] **[ L]** _[t]_ **[s]** _[t][,]_


where

**L** _t_ = _−_ ( **R** + **B** [T] **K** _t_ +1 **B** ) _[−]_ [1] **B** [T] **K** _t_ +1 **A** _._

Plugging this value of **u** _[∗]_ _t_ [in] [the] [above] [expression] [for] _[J][t]_ [(] **[s]** _[t]_ [)] [we] [get]

_Jt_ ( **s** _t_ ) = **s** [T] _t_ **[Qs]** _[t]_ [+] **[ s]** [T] _t_ **[A]** [T] **[K]** _[t]_ [+1] **[As]** _[t]_ _[−]_ **[s]** [T] _t_ **[A]** [T] **[K]** _[t]_ [+1] **[B]** [(] **[R]** [ +] **[ B]** [T] **[K]** _[t]_ [+1] **[B]** [)] _[−]_ [1] **[B]** [T] **[K]** _[t]_ [+1] **[As]** _[t]_
= **s** [T] _t_ **[K]** _[t]_ **[s]** _[t][,]_


where


**K** _t_ = **Q** + **A** [T] ( **K** _t_ +1 _−_ **K** _t_ +1 **B** ( **R** + **B** [T] **K** _t_ +1 **B** ) _[−]_ [1] **B** [T] **K** _t_ +1) **A** _._


**13.5** **Sequential** **Decision** **Problem** **with** **Infinite** **Horizon**


Infinite horizon problems are often appropriate models for problems where there
is no terminal stage, such as investments for an endowment or a foundation. They
are also often appropriate to model problems with very long time horizons. The
infinite horizon setting tends to simplify some issues since the dependence of the
value function on _t_ can be eliminated.
Consider an infinite horizon problem whose law of motion is of the form


**s** _t_ +1 = _f_ ( **x** _t,_ **s** _t_ )


and whose objective function is



max
**x** 0 _,_ **x** 1 _,..._




- _∞_

_θ_ _[t]_ _· g_ ( **x** _t,_ **s** _t_ ) _,_

_t_ =0



where _θ_ _∈_ (0 _,_ 1) is a given discount factor. Define the value-to-go function _V_ ( _·_ ) as



_V_ ( **s** 0) := max
**x** 0 _,_ **x** 1 _,..._




- _∞_

_θ_ _[t]_ _· g_ ( **x** _t,_ **s** _t_ ) _._

_t_ =0


**13.6** **Linear–Quadratic** **Regulator** **with** **Infinite** **Horizon** 219


Observe that at any intermediate stage _t_ we have



_V_ ( **s** _t_ ) := max
**x** _t,_ **x** _t_ +1 _,..._




- _∞_

_θ_ _[τ]_ _[−][t]_ _· g_ ( **x** _τ_ _,_ **s** _τ_ ) _._

_τ_ = _t_



Thus, in this case the Bellman equation can be written as


_V_ ( **s** _t_ ) = max
**x** _t_ _[g]_ [(] **[x]** _[t][,]_ **[ s]** _[t]_ [) +] _[ θ][ ·][ V]_ [ (] **[s]** _[t]_ [+1][)] _[.]_


**13.6** **Linear–Quadratic** **Regulator** **with** **Infinite** **Horizon**


Consider now the infinite horizon version of the linear–quadratic regulator that
we discussed in Section 13.4. The goal now is to determine the optimal sequence
of controls **u** _t,_ _t_ = 0 _,_ 1 _, . . .,_ that minimizes the following cost:



_V_ ( **s** 0) := min
**u** 0 _,_ **u** 1 _,..._




- 
 - _∞_

( **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [)]
_t_ =0



_._



A common technique to solve the Bellman equation (and similar differential
equations) is “ansatz”, which can be loosely described as “make an educated
guess and later verify”. In this problem, we try the following quadratic ansatz
for the form of the value function:


_V_ ( **s** _t_ ) = **s** [T] _t_ **[Ks]** _[t]_


for some symmetric positive definite matrix **K** .
With this educated guess we now apply the Bellman equation (infinite horizon
case):



_V_ ( **s** _t_ ) = min
**u** _t_


= min
**u** _t_


= min
**u** _t_




- **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [+] _[ V]_ [ (] **[s]** _[t]_ [+1][)]

- **s** [T] _t_ **[Qs]** _[t]_ [+] **[ u]** [T] _t_ **[Ru]** _[t]_ [+ (] **[As]** _[t]_ [+] **[ Bu]** _[t]_ [)][T] **[K]** [(] **[As]** _[t]_ [+] **[ Bu]** _[t]_ [)]

- **s** [T] _t_ **[Qs]** _[t]_ [+] **[ s]** [T] _t_ **[A]** [T] **[KAs]** _[t]_ [+ 2] **[s]** [T] _t_ **[A]** [T] **[KBu]** _[t]_ [+] **[ u]** [T] _t_ [(] **[R]** [ +] **[ B]** [T] **[KB]** [)] **[u]** _[t]_ _._



The latter is a convex quadratic function of **u** _t_ . To find its minimum, we compute
its gradient and equate it to zero to obtain:


2 **B** [T] **KAs** _t_ + 2( **R** + **B** [T] **KB** ) **u** _t_ = **0** _._


Thus, the optimal control at stage _t_ is


**u** _[∗]_ _t_ [=] _[ −]_ [(] **[R]** [ +] **[ B]** [T] **[KB]** [)] _[−]_ [1] **[B]** [T] **[KAs]** _[t]_ [=] **[ Ls]** _[t][,]_


where

**L** = _−_ ( **R** + **B** [T] **KB** ) _[−]_ [1] **B** [T] **KA** _._


220 **Dynamic** **Programming:** **Theory** **and** **Algorithms**


Plugging this value of **u** _[∗]_ _t_ [in] [the] [above] [Bellman] [equation] [we] [get]

_V_ ( **s** _t_ ) = **s** [T] _t_ **[Qs]** _[t]_ [+] **[ s]** [T] _t_ **[A]** [T][(] **[K]** _[ −]_ **[KB]** [(] **[R]** [ +] **[ B]** [T] **[KB]** [)] _[−]_ [1] **[B]** [T] **[K]** [)] **[As]** _[t][.]_


Hence for the above guess to be correct, we must have:


**K** = **Q** + **A** [T] ( **K** _−_ **KB** ( **R** + **B** [T] **KB** ) _[−]_ [1] **B** [T] **K** ) **A** _._


This is the so-called _Ricatti_ _equation_ . Under suitable assumptions on **Q** _,_ **R** _,_ **A** _,_ **B** _,_
this equation is known to have a unique symmetric positive definite solution **K** .
Consider the following special case: **A** = **B** = **I** and **R** = _λ_ **Q** with _λ_ _>_ 0 _._ In
this case the law of motion is


**s** _t_ +1 = **s** _t_ + **u** _t_


and the Ricatti equation is


**K** = **Q** + **K** _−_ **K** ( _λ_ **Q** + **K** ) _[−]_ [1] **K** _._


We thus obtain

**Q** = **K** ( _λ_ **Q** + **K** ) _[−]_ [1] **K** _._


To solve for **K**, try to find a solution of the form **K** = _a_ **Q** . Plugging this in the
above equation yields

_a_ [2]
1 =

_λ_ + _a_ _[.]_



This is a quadratic equation in _a_ with two roots, but only one that is positive,
namely



~~_√_~~
_a_ = [1 +]



1 + 4 _λ_
_._
2



Therefore we get


and consequently



~~_√_~~
1 +
**L** = _−_



_√_

1 + 4 _λ_

**K** = _a_ **Q** = [1 +] **Q** _,_

2



1 + 4 _λ_ **[I]** _[.]_



1 + 1 + 4 _λ_

~~_√_~~
2 _λ_ + 1 + 1 + 4



In particular, the optimal control at time _t_ is



~~_√_~~
1 +
**u** _t_ = _−_



1 + 4 _λ_ **[s]** _[t][.]_



1 + 1 + 4 _λ_

~~_√_~~
2 _λ_ + 1 + 1 + 4



Note that when _λ_ = 0, there is no direct cost associated with the control variable
**u** _t_ and therefore it is optimal to select **u** _t_ to minimize the cost of **s** _t_ +1 = **s** _t_ +
**u** _t,_ which is given by **s** [T] _t_ +1 **[Qs]** _[t]_ [+1][.] [Clearly,] [this] [is] [minimized] [when] **[s]** _[t]_ [+1] [=] [0,] [or]
equivalently, when **u** _t_ = _−_ **s** _t_ . On the other hand, for _λ_ _>_ 0, the cost _λ_ **u** [T] _t_ **[Qu]** _[t]_
keeps **u** _t_ from reaching all the way to _−_ **s** _t_ . Instead, **u** _t_ is a scalar multiple of _−_ **s** _t_,
where the scalar multiple is less than 1. In addition, the larger _λ_, the higher the
cost of the control variable **u** _t_, and therefore the smaller this scalar multiple.


**13.7** **Model** **of** **Sequential** **System** **(Stochastic** **Case)** 221


**13.7** **Model** **of** **Sequential** **System** **(Stochastic** **Case)**


The above dynamic programming machinery has a straightforward extension to a
more general context that includes a stochastic component in the law of motion.
A _stochastic_ _sequential_ _system_ is an extension of the deterministic case. Like a
deterministic sequential system, the main components of a stochastic sequential
system are stages, states, decisions, and law of motion. The first three are exactly
as before. On the other hand, the law of motion of a stochastic sequential system
is of the more general form


**s** _t_ +1 = _ft_ ( **s** _t,_ **x** _t, ωt_ ) _,_ _t_ = 0 _,_ 1 _, . . ., T._


As before, **s** _t,_ **x** _t_ are the state and action at stage _t_ and **s** _t_ +1 is the state at stage
_t_ + 1. In addition, _ωt_ is some random disturbance that occurs at stage _t_ .
Assume we are interested in optimizing some overall objective function



E




- 
- _T_

_gt_ ( **s** _t,_ **x** _t, ωt_ ) + _gT_ +1( **s** _T_ +1)

_t_ =0



_,_ (13.5)



where each _gt_ ( **s** _t,_ **x** _t, ωt_ ) _,_ _t_ = 0 _,_ 1 _, . . ., T,_ and _gT_ +1( **s** _T_ +1) is a cost or a reward
per stage. This defines a _stochastic_ _sequential_ _decision_ _problem_ : find **x** _t,_ _t_ =
0 _,_ 1 _, . . ., T,_ to minimize or maximize the expected total cost or reward (13.5).
Bellman’s optimality principle also extends in a natural fashion. Suppose we
are maximizing the expected reward




        
   - _T_

_J_ ( **s** 0) := max E _gt_ ( **s** _t,_ **x** _t, ωt_ ) + _gT_ +1( **s** _T_ +1)
**x** 0 _,...,_ **x** _T_

_t_ =0







_._





Consider the “tail problem” that starts at stage _t_ :



_Jt_ ( **s** _t_ ) := max E
**x** _t,...,_ **x** _T_





- _T_

_gτ_ ( **s** _τ_ _,_ **x** _τ_ _, ωτ_ ) + _gT_ +1( **s** _T_ +1)

_τ_ = _t_



_._



_Bellman’s optimality principle_ can be stated as follows. The value-to-go functions
_Jt_ ( _st_ ) satisfy the following Bellman equation:


_Jt_ ( _st_ ) = max E _t_ [ _gt_ ( _st, xt, ωt_ ) + _Jt_ +1( _ft_ ( _st, xt, ωt_ ))] _._ (13.6)
_xt_


The stochastic case also has an infinite horizon version. Consider an infinite
horizon problem with a law of motion of the form


**s** _t_ +1 = _f_ ( **x** _t,_ **s** _t, ωt_ )


and objective function







max
**x** 0 _,_ **x** 1 _,..._ [E]





- _∞_

_θ_ _[t]_ _· g_ ( **x** _t,_ **s** _t, ωt_ )

_t_ =0



_,_


222 **Dynamic** **Programming:** **Theory** **and** **Algorithms**



where _θ_ _∈_ (0 _,_ 1) is a given discount factor.
Define the value-to-go function _V_ ( _·_ ) as







_V_ ( **s** 0) := max
**x** 0 _,_ **x** 1 _,..._ [E]





- _∞_



_θ_ _[t]_ _· g_ ( **x** _t,_ **s** _t, ωt_ )

_t_ =0



_._



Observe that at any intermediate stage _t_ we have







_V_ ( **s** _t_ ) := max
**x** _t,_ **x** _t_ +1 _,..._ [E]





- _∞_



_θ_ _[τ]_ _[−][t]_ _· g_ ( **x** _τ_ _,_ **s** _τ_ _, ωτ_ )

_τ_ = _t_



_._



In this case the Bellman equation can be written as


_V_ ( **s** _t_ ) = max
**x** _t_ [E] _[t]_ [ [] _[g]_ [(] **[x]** _[t][,]_ **[ s]** _[t][, ω][t]_ [) +] _[ θ][ ·][ V]_ [ (] **[s]** _[t]_ [+1][)]] _[ .]_


**13.8** **Notes**


Dynamic programming was introduced by Bellman (1954, 1957), who stated
the fundamental principle of optimality. Dynamic programming is pervasive in
many disciplines, including finance, economics, biology, management, etc. The
book of Bertsekas (2005) is a popular modern reference on this topic. The book
by Porteus (2002) gives a treatment on dynamic programming with focus on
inventory theory.


**13.9** **Exercises**


**Exercise** **13.1** Consider the following puzzle. There are 40 matches on a table.
You begin by picking up 1, 2, 3, or 4 matches. Then your opponent must pick 1,
2, 3, or 4 matches. The two of you continue taking turns until the last match is
picked up. The player who picks up the last match loses.


(a) Can you find a strategy that guarantees your victory? If so, how?
(b) What if the initial number of matches is 39, 38, 37, or 36 instead of 40?
(c) Suppose the game starts with 40 matches and you and your opponent take
turns as above but the player who picks up the last match wins. Can you
find a strategy that guarantees your victory? If so, how?


**Exercise** **13.2** Consider the following capital budgeting example from
Chapter 8:


max 9 _x_ 1 + 11 _x_ 2 + 7 _x_ 3 + 4 _x_ 4
s.t. 7 _x_ 1 + 10 _x_ 2 + 6 _x_ 3 + 3 _x_ 4 _≤_ 19
_xi_ _∈{_ 0 _,_ 1 _},_ _i_ = 1 _, . . .,_ 4 _._

                                         - �T
Observe that this is a knapsack problem. Prove that the vector **x** _[∗]_ = 0 1 1 1

is an optimal solution to this problem by showing that it satisfies the Bellman
equation.


**13.9** **Exercises** 223


**Exercise** **13.3** Consider the optimal consumption problem described in
Example 13.3. Suppose the consumer has a logarithmic utility of consumption
_U_ ( _Ct_ ) = log( _Ct_ ).


(a) Show that the optimal consumption and value-to-go function at stage _T_ are
respectively _CT_ _[∗]_ [(] _[W][T]_ [ ) =] _[ W][T]_ [and] _[J][T]_ [ (] _[W][T]_ [ ) = log(] _[W][T]_ [ )] _[.]_
(b) Assume _r_ = 0. Use the Bellman equation and induction to show that the
optimal consumption and value-to-go function at stages _t_ = 0 _,_ 1 _, . . ., T_ _−_ 1
are respectively _Ct_ ( _Wt_ ) = _W_ 0 _/_ ( _T_ _−_ _t_ + 1) and _Jt_ ( _Wt_ ) = ( _T −_ _t_ +1) log( _Wt_ ) _._
(c) Assume _r_ _>_ 0. Use the Bellman equation and induction to find the optimal
consumption and value-to-go function at stages _t_ = 0 _,_ 1 _, . . ., T_ _−_ 1.


**Exercise** **13.4** Consider the following infinite horizon variation of the previous
consumption problem. Assume the consumer lives forever and her objective is to
maximize the following total discounted utility of consumption


     - _∞_

_θ_ _[t]_ _·_ log( _Ct_ )

_t_ =0


for some _θ_ _∈_ (0 _,_ 1). Use the following educated guess (“ansatz”) for the optimal
value function:


_V_ ( _Wt_ ) = _a ·_ log( _Wt_ ) + _b_


for some constants _a, b_ with _a_ _>_ 0. Use the Bellman equation to verify this
educated guess and determine the optimal consumption rule _Ct_ _[∗]_ [(] _[W][t]_ [) and optimal]
value function _V_ ( _Wt_ ) (that is, the values of _a_ and _b_ ). For simplicity, assume _r_ = 0.


**Exercise** **13.5** Consider the following variation of the optimal consumption
problem described in Example 13.3. At each stage _t_ the amount of non-consumed
wealth _Wt_ _−_ _Ct_ can be split between treasury bills and an index fund. Funds
placed in treasury bills earn an annual risk-free return _r_ _>_ 0 whereas the funds
placed in the index fund earn a risky return _rt_ with expected value E( _rt_ ) = _μ > r_
and variance var( _rt_ ) = _σ_ [2] _>_ 0 _._ Assume the returns are i.i.d. across different
periods.
Use dynamic programming to formulate the following optimal investment and
consumption problem: Determine the consumption _Ct_ _∈_ [0 _, Wt_ ] and fraction of
wealth _xt_ _∈_ R invested in the index fund at stage _t_ = 0 _,_ 1 _, . . ., T_ that maximize
the total expected utility of consumption







max E
_C_ 0 _,...,CT_
_x_ 0 _,...,xT_





- _T_

_U_ ( _Ct_ )

_t_ =0



over the next _T_ years. Proceed as follows.


(a) Write the law of motion; that is, the equation that describes the state _Wt_ +1
in terms of the state _Wt_ and decisions _Ct, xt_ at stage _t_ .
(b) Write the Bellman equation for the value-to-go function _Jt_ ( _Wt_ ).


224 **Dynamic** **Programming:** **Theory** **and** **Algorithms**


(c) Consider the special case of logarithmic utility of consumption _U_ ( _Ct_ ) =
log( _Ct_ ). Use the Bellman equation and induction to determine the optimal
consumption _Ct_ _[∗]_ [and] [investment] [fraction] _[x][∗]_ _t_ [as] [well] [as] [the] [value-to-go] [func-]
tion _Jt_ ( _Wt_ ) at stage _t_ for _t_ = 0 _,_ 1 _, . . ., T._
(d) Indicate how your model changes if the fraction of wealth _xt_ invested in the
index fund at each stage _t_ is subject to the constraint _xt_ _∈_ [0 _,_ 1]. (That is,
no leverage is allowed in the investment portfolio.)


## 14 Dynamic Programming Models: Multi-Period Portfolio Optimization

This chapter describes four types of dynamic portfolio optimization problems
that are amenable to dynamic programming technology. The first two deal
respectively with optimization of final wealth and its extension, optimal
consumption and investment. These two classical models date back multiple
decades. The last two problems are much more modern developments. One of
them is a model for dynamic trading when returns are predictable and trading
is costly. The other one is a model for dynamic portfolio optimization that
incorporates capital gains taxes.


**14.1** **Utility** **of** **Terminal** **Wealth**


Let us revisit the dynamic portfolio optimization model with initial endowment
and utility of terminal wealth that we discussed in Chapter 12. However, this
time we consider a more general setting where there are forecasting variables
available at each stage. Such forecasting variables could be associated with a
factor model. For instance, they could be macroeconomic indicators, or certain
measurable parameters of a particular asset or firm.
As before, suppose that an investor starts at _t_ = 0 with an initial endowment
_W_ 0. At times _t_ = 0 _, . . ., T −_ 1 the investor invests her wealth _Wt_ in a portfolio of
risk-free and risky assets. The investor’s goal is to maximize the expected utility
of terminal wealth _U_ ( _WT_ ) at time _T_ for some utility function _U_ ( _·_ ). Define the
following convenient notation:


_•_ _Rf,t_ +1 = gross risk-free return in period [ _t, t_ + 1];

_•_ **r** _t_ +1 = vector of excess returns of the risky assets in period [ _t, t_ + 1];

_•_ _Rp,t_ +1 = gross random return of the investor’s portfolio in period [ _t, t_ + 1];

_•_ **z** _t_ = forecasting state variables available at stage _t_ ;

_•_ _Wt_ = wealth at stage _t_ .


We have the inter-temporal budget constraint:


_Wt_ +1 = _Wt · Rp,t_ +1 = _Wt ·_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)] _[,]_ _t_ = 0 _, . . ., T_ _−_ 1 _._


The specific components of this sequential decision problem are as follows:


**Stages:** these are _t_ = 0 _, . . ., T_ _−_ 1.


226 **Dynamic** **Programming** **Models:** **Multi-Period** **Optimization**


**State** **at** **stage** _t_ **:** this is ( _Wt,_ **z** _t_ ).
**Decision** **variables** **at** **stage** _t_ **:** these are the vector **x** _t_ of portfolio holdings
(percentages) in the risky assets.
**Law** **of** **motion:** this is the same as the above inter-temporal constraint


_Wt_ +1 = _Wt ·_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)] _[,]_ _[t]_ [ = 0] _[, . . ., T]_ _[−]_ [1] _[.]_


We next apply Bellman’s optimality principle. In this case the value-to-go
function is



_Jt_ ( _Wt,_ **z** _t_ ) = max
**x** _t,...,_ **x** _T −_ 1 [E] _[t]_ [(] _[U]_ [(] _[W][T]_ [ ))]











��



= max
**x** _t,...,_ **x** _T −_ 1 [E] _[t]_


At the final stage _T_ we get



_T_ - _−_ 1

( _Rf,τ_ +1 + **r** [T] _τ_ +1 **[x]** _[τ]_ [)]
_τ_ = _t_



_U_



_Wt ·_



_._



_JT_ ( _WT,_ **z** _T_ ) = _U_ ( _WT_ ) _._


For earlier stages, we have the Bellman equation


_Jt_ ( _Wt,_ **z** _t_ ) = max
**x** _t_ [E] _[t]_ [ [] _[J][t]_ [+1][(] _[W][t]_ [+1] _[,]_ **[ z]** _[t]_ [+1][)]]

                 -                  = max _Jt_ +1( _Wt_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)] _[,]_ **[ z]** _[t]_ [+1][)] _._
**x** _t_ [E] _[t]_


In the special case of power utility _U_ ( _W_ ) = _W_ [1] _[−][γ]_ _/_ (1 _−_ _γ_ ), where _γ_ _>_ 0 _,_ we
rewrite the Bellman equation as follows. Define _ψt_ ( **z** _t_ ) := _Jt_ (1 _,_ **z** _t_ ). Then it is
easy to see that the Bellman equation is equivalent to

                -                 _ψt_ ( **z** _t_ ) = max E _t_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)][1] _[−][γ]_ _[·][ ψ][t]_ [+1][(] **[z]** _[t]_ [+1][)] _._
**x** _t_


We can draw the following interesting conclusions from here. On the one hand,
if **r** _t_ +1 and **z** _t_ +1 are independent at time _t_, then the term on the right-hand side
above satisfies

          -          E _t_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)][1] _[−][γ]_ _[·][ ψ][t]_ [+1][(] **[z]** _[t]_ [+1][)]

             = E _t_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)][1] _[−][γ]_ [�] _·_ E _t_ ( _ψt_ +1( **z** _t_ +1)) _._ (14.1)


Thus, to find **x** _t_ we need to solve




= max E _t_ [ _U_ ( _Rp,t_ +1)] _._
**x** _t_



max E _t_
**x** _t_




- ( _Rf,t_ +1 + **r** T _t_ +1 **[x]** _[t]_ [)][1] _[−][γ]_

1 _−_ _γ_



In this case the optimal policy is myopic.
On the other hand, if **r** _t_ +1 and **z** _t_ +1 are correlated, then (14.1) no longer holds.
In this case **x** _t_ may include some kind of “inter-temporal hedging component”.
The intuition is that the correlation between **r** _t_ +1 and **z** _t_ +1 would induce some
kind of serial dependence in our returns. In other words, the current forecasted
return **r** _t_ +1 conveys information about future returns. Unlike the myopic strategy,
the optimal dynamic strategy incorporates this serial dependence.


**14.2** **Optimal** **Consumption** **and** **Investment** 227


**14.2** **Optimal** **Consumption** **and** **Investment**


Consider an extension of the previous dynamic portfolio optimization model
where the goal is to maximize an expected utility that combines two terms:
consumption along the planning horizon and terminal wealth. The latter component is sometimes called _bequest_ .
There are three key differences from the previous model. First, there is an
additional decision variable _Ct_ _∈_ [0 _, Wt_ ] at each stage _t_ that denotes the amount
of wealth the investor consumes at stage _t_ . Second, the objective function is







**x** 0 _,...,_ max **x** _T −_ 1 E
_C_ 0 _,...,CT −_ 1




_T_  - _−_ 1

_U_ ( _Ct_ ) + _B_ ( _WT_ )
_t_ =0



for some utility functions _U_ ( _C_ ) and _B_ ( _W_ ). Third, the new law of motion, or
inter-temporal budget constraint, is


_Wt_ +1 = ( _Wt −_ _Ct_ ) _· Rp,t_ +1 = ( _Wt −_ _Ct_ ) _·_ ( _Rf,t_ +1 + **r** [T] _t_ +1 **[x]** _[t]_ [)] _[,]_ _[t]_ [ = 0] _[, . . ., T]_ _[−]_ [1] _[.]_


To simplify our discussion we consider the case when there are no forecasting
variables **z** _t_ . In particular this implies that the returns on the risky assets are
independent across different time periods. At the final stage _T_ we have the
following value-to-go function


_JT_ ( _WT_ ) = _B_ ( _WT_ ) _._


For earlier stages, we have the Bellman equation


_Jt_ ( _Wt_ ) = max
_Ct,_ **x** _t_ [E] _[t]_ [ [] _[J][t]_ [+1][(] _[W][t]_ [+1][) +] _[ U]_ [(] _[C][t]_ [)]] _[ .]_


The first-order optimality conditions yield

                   -                    _U_ _[′]_ ( _Ct_ ) = E _t_ _Jt_ _[′]_ +1 [(] _[W][t]_ [+1][)] _[R][p,t]_ [+1]



and




  -  E _t_ _Jt_ _[′]_ +1 [(] _[W][t]_ [+1][)] **[r]** _[t]_ [+1] = **0** _._



The first one is obtained by differentiating with respect to _Ct_ and the second
one is obtained by differentiating with respect to **x** _t_ .
If we plug the optimal _Ct,_ **x** _t_ back into the Bellman equation and differentiate
with respect to the state variable _Wt_, we obtain the following _envelope condition_ :


_U_ _[′]_ ( _Ct_ ) = _Jt_ _[′]_ [(] _[W][t]_ [)] _[.]_


In the special case of a logarithmic utility of consumption and bequest _U_ ( _C_ ) =
log( _C_ ), _B_ ( _W_ ) = log( _W_ ), we can draw a more explicit conclusion about the
problem. In this case the Bellman equation yields the following expressions for
the value function and optimal consumption:

_Jt_ ( _Wt_ ) = _T_ [log(] _−_ _t_ _[W]_ + 1 _[t]_ [)] [+] _[ b][t]_


228 **Dynamic** **Programming** **Models:** **Multi-Period** **Optimization**


and

_Wt_
_Ct_ _[∗]_ [(] _[W][t]_ [) =]
_T_ _−_ _t_ + 1 _[.]_

The specific value _bt_ and the optimal portfolio **x** _[∗]_ _t_ [(] _[W][t]_ [)] [depend] [on] [the] [joint]
probability distribution of _Rf,t_ +1 and **r** _t_ +1. By contrast, the optimal consumption
_Ct_ _[∗]_ [(] _[W][t]_ [)] [only] [depends] [on] _[W][t]_ [.]


**14.3** **Dynamic** **Trading** **with** **Predictable** **Returns** **and**
**Transaction** **Costs**


We next discuss a recent model due to Gˆarleanu and Pedersen (2013) for dynamic
portfolio optimization when asset returns are predictable by signals and trading
is costly. This problem is quite timely and especially relevant for active investors.
The optimal trading policy should balance various tradeoffs. Fast trading generates more alpha and lower risk but also higher transaction costs. Slow trading
does the opposite. On the other hand, there may be fast signals that require
quick action and slow signals associated with longer-lasting alpha. The model
that we discuss next provides an insightful solution to this problem.
Consider a universe of assets, whose returns evolve according to the following
law of motion:


**r** _t_ +1 = **Bf** _t_ + **u** _t_ +1 _._


Here **f** _t_ is a vector of factor returns that predict asset returns, **B** is a matrix
of exposures or sensitivities of the asset returns to factor returns, and **u** _t_ is an
idiosyncratic zero-mean noise term with constant covariance matrix


var _t_ ( **u** _t_ +1) := Σ _._


The vector of factor returns **f** _t_ is known to the investor at time _t_ and evolves
according to


Δ **f** _t_ +1 = _−_ Φ **f** _t_ + _**ϵ**_ _t_ +1 _,_


where Δ **f** _t_ +1 = **f** _t_ +1 _−_ **f** _t_ .
Trading is costly. The transaction cost associated with trading the vector of
shares Δ **x** _t_ = **x** _t −_ **x** _t−_ 1 is


_TC_ (Δ **x** _t_ ) = [1] 2 [Δ] **[x]** _t_ [T][Λ Δ] **[x]** _[t]_


for some symmetric positive definite matrix Λ _._
The model objective is




   
_[γ]_ _t_ [Σ] **[x]** _[t]_ _−_ [(1] _[ −]_ _[ρ]_ [)] _[t]_

2 **[x]** [T] 2



Δ **x** [T] _t_ [Λ Δ] **[x]** _[t]_
2







max
**x** 0 _,_ **x** 1 _,..._ [E][0]





- _∞_




- _∞_

(1 _−_ _ρ_ ) _[t]_ [+1][ �] **r** [T] _t_ +1 **[x]** _[t]_ _[−]_ _[γ]_

2

_t_ =0



_._



Gˆarleanu and Pedersen (2013) apply a dynamic programming approach to
characterize the optimal trading strategy. We summarize the main results below.


**14.3** **Dynamic** **Trading** **with** **Predictable** **Returns** **and** **Costs** 229


The state at time _t_ is the pair ( **x** _t−_ 1 _,_ **f** _t_ ). The value-to-go function is




   
_[γ]_ _τ_ [Σ] **[x]** _[τ]_

2 **[x]** [T]



_V_ ( **x** _t−_ 1 _,_ **f** _t_ ) = max
**x** _t,_ **x** _t_ +1 _,..._ [E] _[t]_


Hence the Bellman equation is





- _∞_




- _∞_

(1 _−_ _ρ_ ) _[τ]_ [+1] _[−][t]_ [ �] **r** [T] _τ_ +1 **[x]** _[τ]_ _[−]_ _[γ]_

2

_τ_ = _t_




_−_ [(1] _[ −]_ _[ρ]_ [)] _[τ]_ _[−][t]_ Δ **x** [T] _τ_ [Λ Δ] **[x]** _[τ]_

2





_._





_−_ [1]




          - [�]

_[γ]_ _t_ [Σ] **[x]** _[t]_ [+][ E] _[t]_ [[] _[V]_ [ (] **[x]** _[t][,]_ **[ f]** _[t]_ [+1][)]] _._

2 **[x]** [T]



_V_ ( **x** _t−_ 1 _,_ **f** _t_ ) = max
**x** _t_



_t_ [Λ Δ] **[x]** _[t]_
2 [Δ] **[x]** [T]




    + (1 _−_ _ρ_ ) E _t_ ( **r** [T] _t_ +1 **[x]** _[t]_ [)] _[ −]_ _[γ]_



We make an educated guess and later verify (ansatz) the following quadratic
form for the value function:




[1] 2 **[x]** _t_ [T] **[A]** _[xx]_ **[x]** _[t]_ [+] **[ x]** [T] _t_ **[A]** _[xf]_ **[f]** _[t]_ [+1] [+] [1] 2



_V_ ( **x** _t,_ **f** _t_ +1) = _−_ [1]




[1] 2 **[f]** [ T] _t_ +1 **[A]** _[ff]_ **[f]** _[t]_ [+1] [+] _[ a]_ [0] _[.]_



Using this ansatz, it can be shown that the optimal trading policy is


**x** _t_ = **x** _t−_ 1 + Λ _[−]_ [1] **A** _xx_ (aim _t −_ **x** _t−_ 1)


where

aim _t_ = **A** _[−]_ _xx_ [1] **[A]** _[xf]_ **[f]** _[t][.]_


The Bellman equation also yields expressions for the matrices **A** _xx,_ **A** _xf_ _,_ **A** _ff_ .
See the exercises at the end of the chapter. In the special case Λ = _λ_ Σ we obtain




  **x** _t_ = 1 _−_ _[a]_

_λ_




**x** _t−_ 1 + _[a]_

_λ_ [aim] _[t][,]_



where




      _a_ = _[−]_ [(] _[γ]_ [(1] _[ −]_ _[ρ]_ [) +] _[ λρ]_ [) +] ( _γ_ (1 _−_ _ρ_ ) + _λρ_ ) [2] + 4 _γλ_ (1 _−_ _ρ_ ) [2] _._

2(1 _−_ _ρ_ )



Next, we get a more explicit expression of the aim portfolio. To that end, first
observe that the myopic solution in the absence of transaction costs is precisely
the solution to the static Markowitz model at time _t_ ; that is,


Markowitz _t_ = ( _γ_ Σ) _[−]_ [1] **Bf** _t._


Again we consider the special case Λ = _λ_ Σ. For _z_ := _γ/_ ( _γ_ + _a_ ) we get


aim _t_ = _z ·_ Markowitz _t_ + (1 _−_ _z_ )E _t_ (aim _t_ +1)



=




- _∞_

_z_ (1 _−_ _z_ ) _[τ]_ _[−][t]_ E _t_ (Markowitz _τ_ ) _._

_τ_ = _t_



Furthermore, the portfolio aim _t_ has a similar form to Markowitz _t_ provided the
forecasting signals are appropriately scaled down:

            -             - _−_ 1
aim _t_ = ( _γ_ Σ) _[−]_ [1] **B** **I** + _[a]_ **f** _t._

_γ_ [Φ]


230 **Dynamic** **Programming** **Models:** **Multi-Period** **Optimization**


The optimal strategy is characterized by two principles. First, aim in front of
the target. Second, trade partially towards the current aim. More precisely, the
optimal updated portfolio is a linear combination of the existing portfolio and an
_aim_ portfolio. The latter is a weighted average of the current Markowitz portfolio
(the moving target) and the expected Markowitz portfolios on all future dates
(where the target is moving).


**14.4** **Dynamic** **Portfolio** **Optimization** **with** **Taxes**


Taxes pose a significant friction to most investors in financial markets. There
are a variety of taxes that apply in different ways to income, dividends, and
capital gains. It is common to ignore taxes in traditional finance and portfolio
theory. This simplification is in part due to the difficulties involved in modeling
the effects of taxes.
Capital taxes introduce a peculiar type of challenge in portfolio management.
Since the sale of an appreciated asset triggers a capital gain tax liability, there is
a tradeoff between the benefits of diversification versus the tax costs triggered by
rebalancing the portfolio. In addition to the tradeoff between diversification and
taxes, many individual investors also have to deal with both a tax-deferred and
a taxable account. In this context an investor faces an _asset_ _location_ problem
in addition to the usual asset allocation problem. Asset location refers to the
problem of how the investor should locate her portfolio holdings across the taxdeferred and taxable accounts.


Basic Case: Tax Management Only


In the United States tax code, capital gains and losses are triggered when assets
are sold. This feature means that the investor could manage her assets in ways
that reduce her tax liabilities by choosing when to realize gains or losses. In this
section we describe some models for optimal tax trading.
One of the earliest and most basic models for optimal tax trading was introduced by Constantinides (1983). In this model it is assumed that the tax rate
on capital gains is independent of the length of the holding period. It is also
assumed that capital losses generate tax rebates. Finally, it is assumed that
there are no transaction costs, no capital loss restrictions, and no wash-sale
restrictions. A wash sale occurs when an asset is sold at a capital loss and the
same or substantially identical one is also purchased within 30 days before or after
the sale. Under these assumptions the optimal tax-trading strategy is relatively
simple: Realize losses as soon as they occur and defer gains indefinitely. By
realizing losses, the investor gets a tax rebate. If the investor did not realize the
loss as soon as it happened, the opportunity for a tax rebate could disappear.
Constantinides’s model can be extended to account for proportional transaction
costs. If there are proportional transaction costs, then the optimal tax-trading
strategy would still be to defer gains but to realize losses only beyond a certain
threshold. The exact size of the threshold depends on the size of the transaction


**14.4** **Dynamic** **Portfolio** **Optimization** **with** **Taxes** 231


In a more elaborate follow-up article Constantinides (1984) proposed a model
that considers a more realistic setting where the tax rate depends on the length
of the holding period. In this model the sale of assets with long-term status is
taxed at a rate lower than that of assets with short-term status. In this case the
optimal tax-trading strategy still calls for realizing losses as soon as they occur.
In addition and somewhat surprisingly, it is also sometimes optimal to sell (and
immediately repurchase) assets with an embedded long-term gain. The rationale
for this action is that there is a “re-start” option associated with resetting the
tax basis and having the opportunity to realize short-term losses. The value of
this re-start option depends on the asset volatility and the ratio of the short-term
1
and long-term capital tax rates. The following example provided by C. Spatt

illustrates this phenomenon.


**Example** **14.1** Consider an asset with current price _P_ 0 = $20 _._ Suppose that
at dates _t_ = 0 _,_ 1 we have

        _Pt_ + _k_ with probability 0 _._ 5
_Pt_ +1 = _Pt −_ _k_ with probability 0 _._ 5 _._


Assume an investor buys one share of this asset at date _t_ = 0. Our goal is
to determine the trading strategy (realize/not realize) at dates _t_ = 1 _,_ 2 that
minimizes expected taxes.


(a) First consider the following case. The short-term and long-term capital gain
tax rates are respectively _τs_ = 0 _._ 5, and _τℓ_ = 0 _._ 5 _y_, where 0 _< y_ _<_ 1. The sale
of shares held for one period can be treated as either short-term or long-term
depending on what is more advantageous to the investor. The sale of shares
held for two periods is treated as long-term. Assume there are no transaction
costs.
In this case at dates _t_ = 1 and _t_ = 2 it is optimal to realize losses.
At date _t_ = 1 it is optimal to realize a long-term gain if _y_ _<_ 0 _._ 5. See
Exercise 14.2.
(b) Now consider the case when the capital gain tax rate is _τ_ = 0 _._ 2 for both
long-term and short-term gains or losses. Assume a transaction cost of 0 _._ 5
per share traded.
In this case at date _t_ = 2 it is optimal to realize a loss if _k_ _>_ 1 _._ 25.
At date _t_ = 1 it is optimal to realize a loss if _k_ _>_ 5.
Since short-term and long-term rates are the same, it is optimal not to
realize gains at any date.


Portfolio Choice with Taxes


We now turn our attention to the problem of dynamic portfolio choice in the
presence of capital gains taxes. The model below is a simplified version of a
model proposed by Dammon et al. (2001).


1
Personal communication.


232 **Dynamic** **Programming** **Models:** **Multi-Period** **Optimization**



We consider an economy with a risky and a risk-free asset where investors
live for _T_ periods. We also assume that in this economy investors are endowed
with some initial capital and their goal is to maximize some expected utility of
consumption _Ct_ at dates _t_ = 0 _,_ 1 _, . . ., T_ and bequest _WT_ at date _T_ . The return of
the risk-free asset between date _t −_ 1 and date _t_ is _r_ . The price of the risky asset
is serially independent and follows a binomial process. Let _Pt_ denote the price of
the risky asset at date _t_ . Let _nt_ and _mt_ denote respectively the number of shares
of the risky and risk-free assets held right after trading at date _t_ . Throughout
the model we will assume no shorting, i.e., we will impose the constraints _nt_ _≥_ 0
and _mt_ _≥_ 0.
We assume that capital gains are taxed at a rate _τ_, and capital losses are
credited at the same rate. To compute the capital gain triggered by an asset
sale, we assume that the tax basis _Pt_ _[∗]_ [for] [the] [shares] [at] [date] _[t]_ [is] [the] [weighted]
average price of those shares. Therefore, the tax basis _Pt_ _[∗]_ [evolves] [according] [to]
the following law of motion:



_nt−_ 1 _· Pt_ _[∗]_ _−_ 1 [+ (] _[n][t]_ _[−]_ _[n][t][−]_ [1][)][+] _[·][ P][t]_ if _Pt_ _[∗]_ _−_ 1 _[< P][t]_
_nt−_ 1 + ( _nt −_ _nt−_ 1) [+]

_Pt_ if _Pt_ _[∗]_ _−_ 1 _[≥]_ _[P][t][.]_



_Pt_ _[∗]_ [=]



⎧
⎨


⎩



Right after trading at date _t_, the realized capital gain or loss _Gt_ is given by

      _Gt_ = ( _nnt−t−_ 11( _−Pt −nt_ ) _P_ + _t_ _[∗]_ _−_ ( _P_ 1 [)] _t −_ _P ∗t−_ 1 [)] ifif _P Ptt_ _[∗][∗]_ _−−_ 11 _[≤][≥]_ _[P][P][t][t][.]_



We have the following inter-temporal balance of wealth equation that relates the
portfolio holdings at dates _t−_ 1 to the portfolio holdings at dates _t_ = 1 _, . . ., T −_ 1:


_ntPt_ + _mt_ + _Ct_ = _nt−_ 1 _Pt_ + _mt−_ 1(1 + _r_ ) _−_ _τGt._


Similarly, at date _T_ we have


_WT_ = _nT −_ 1 _PT_ + _mT −_ 1(1 + _r_ ) _−_ _τGT ._


The portfolio choice problem can be stated as a dynamic programming problem
where the state variables at date _t_ are ( _Pt, Pt_ _[∗]_ _−_ 1 _[, n][t][−]_ [1] _[, m][t][−]_ [1][), the actions at time]
_t_ are ( _nt, mt, Ct_ ) and the objective is







max
_Ct,nt,mt_ [E]





- _T_



_U_ ( _Ct, t_ ) + _B_ ( _WT_ )
_t_ =0



_._



The following example illustrates the striking effect of taxes in portfolio choice.


**Example** **14.2** Assume that at date _t_ = 0 the holdings are _n−_ 1 _>_ 0 and
_m−_ 1 = 0. In other words, our entire portfolio is invested in the risky asset.
Assume _r_ = 0 _,_ _P_ 0 = 1, 0 _<_ 1 _−_ _k_ _< P−_ _[∗]_ 1 [= 1] _[ −]_ _[δ]_ _[<]_ [ 1,] [and]

         _P_ 0 + _k_ with prob 1 _/_ 2
_P_ 1 = _P_ 0 _−_ _k_ with prob 1 _/_ 2 _._


Assume _T_ = 1 and our goal is to determine the portfolio holdings at date _t_ = 0
so as to maximize some utility of final wealth E( _U_ ( _W_ 1)). Since there is no


**14.4** **Dynamic** **Portfolio** **Optimization** **with** **Taxes** 233


consumption at date _t_ = 0 we have


_n_ 0 _P_ 0 + _m_ 0 = _n−_ 1 _P_ 0 + _m−_ 1 _−_ _τ_ ( _n−_ 1 _−_ _n_ 0) [+] ( _P_ 0 _−_ _P−_ _[∗]_ 1 [)] _[.]_


Thus


_m_ 0 = ( _n−_ 1 _−_ _n_ 0)(1 _−_ _τδ_ ) _._


And so the only variable in our problem is _n_ 0 subject to the constraints 0 _≤_
_n_ 0 _≤_ _n_ 1.
Furthermore, the balance of wealth equation yields


_W_ 1 = _n_ 0 _P_ 1 + _m_ 0 + _τn_ 0( _P_ 0 _[∗]_ _[−]_ _[P]_ [1][)][+]

      = _n_ 0( _τδ_ + _k_ ) + _n−_ 1(1 _−_ _τδ_ ) with prob 1 _/_ 2
_n_ 0( _τk −_ _k_ ) + _n−_ 1(1 _−_ _τδ_ ) with prob 1 _/_ 2 _._


It is evident that in the absence of taxes ( _τ_ = 0), the optimal holding of the
risky asset is _n_ 0 = 0 for any positive level of risk aversion. However, it is easily
checked numerically that _n_ 0 may vary all the way between 0 and _n−_ 1 for positive
values of _τ_ . In particular, for _τ_ = 0 _._ 2, _δ_ = 0 _._ 1, _k_ = 0 _._ 2 we get _n_ 0 = 0 _._ 8352 for
the logarithmic utility function.


The numerical solution to the more general model in Dammon et al. (2001)
reveals the following interesting insights. As expected, it is optimal to realize
capital losses as soon as they occur. Since diversification is more valuable to
young investors, it is optimal for them to sell assets with large embedded capital
gains to rebalance their portfolios. On the other hand, elderly investors defer
most capital gains. Because in the US tax code there is a tax forgiveness at
death, it is optimal for elderly investors to increase their allocations to equity as
they approach their terminal age.
If in addition to some initial endowment an investor receives income, then
the following insights are again revealed by a numerical solution to the model.
Young investors hold more equity, very much in line with popular financial
planning advice. Because of capital gain taxes, it is optimal to use income to
adjust asset allocation instead of selling assets with embedded capital gains. In
years immediately prior to retirement it is optimal to reduce equity allocation,
again in line with popular financial planning advice. Finally, beyond retirement
it is optimal to have a gradual increase in equity holdings.


Asset Allocation and Asset Location


The availability of various kinds of tax-deferred retirements accounts such as
401K, 403(b), IRA, and Keough give investors the ability to shelter some of their
assets from taxes. Since assets may be held both in a tax-deferred as well as in
a taxable account, the _location_ decision has important implications on portfolio
choice. Dammon et al. (2004) developed a model to study this problem. Via
an arbitrage argument, they show that it is optimal to allocate assets to the
tax-deferred account in descending order of tax exposure until the limit of the


234 **Dynamic** **Programming** **Models:** **Multi-Period** **Optimization**


tax-deferred account is reached. In particular, the assets with the highest taxable
yields, such as taxable bonds, should go in the tax-deferred account. If the limit of
the tax-deferred account is reached, then assets with lower taxable yields should
be allocated to the taxable account.
The numerical solution to the model in Dammon et al. (2004) also shows
that, the larger the fraction of wealth in the tax-deferred account, the higher the
fraction of total wealth allocated to assets with higher taxable yield.


**14.5** **Exercises**


**Exercise** **14.1** Consider the optimal consumption and investment model discussed in Section 14.2.


(a) Prove the envelope condition by proceeding as follows. Let _Ct_ _[∗]_ [(] _[W][t]_ [)] [and]
**x** _[∗]_ _t_ [(] _[W][t]_ [)] [denote] [the] [optimal] [consumption] [and] [optimal] [portfolio] [at] [stage] _[t]_
respectively. Thus

                -                 -                 -                 _Jt_ ( _Wt_ ) = E _t_ _Jt_ +1 ( _Wt −_ _Ct_ _[∗]_ [(] _[W][t]_ [))] _[ ·]_ [ (1 +] **[ r]** _t_ [T] +1 **[x]** _t_ _[∗]_ [(] _[W][t]_ [))] + _U_ ( _Ct_ _[∗]_ [(] _[W][t]_ [))] _._


Use the chain rule to differentiate both sides above with respect to _Wt_ . Then
use the optimality conditions for the Bellman equation to show that the
expression for the derivative of the right-hand side simplifies to _U_ _[′]_ ( _Ct_ _[∗]_ [(] _[W][t]_ [)),]
thereby giving the envelope condition


_Jt_ _[′]_ [(] _[W][t]_ [) =] _[ U][ ′]_ [(] _[C]_ _t_ _[∗]_ [(] _[W][t]_ [))] _[.]_


(b) Consider the special case _U_ ( _C_ ) = log( _C_ ), _B_ ( _W_ ) = log( _W_ ). Use induction
to prove the following expressions for the value function and optimal consumption:



and



_Jt_ ( _Wt_ ) = _T_ [log(] _−_ _t_ _[W]_ + 1 _[t]_ [)] [+] _[ b][t]_


_Wt_
_Ct_ _[∗]_ [(] _[W][t]_ [) =]
_T_ _−_ _t_ + 1 _[,]_



where _bt_ depends on the joint distribution of _Rf,t_ +1 _,_ **r** _t_ +1 _._


**Exercise** **14.2** Consider the model for short-term versus long-term taxes
described in Example 14.1.


(a) Suppose the short-term and long-term capital gain tax rates are respectively
_τs_ = 0 _._ 5, and _τℓ_ = 0 _._ 5 _y_, where 0 _< y_ _<_ 1 _._


Prove that indeed at dates _t_ = 1 and _t_ = 2 it is optimal to realize losses,
and at date _t_ = 1 it is optimal to realize a long-term gain if _y_ _<_ 0 _._ 5 _._


**14.5** **Exercises** 235


(b) Suppose the capital gain tax rate is _τ_ = 0 _._ 2 for both long-term and shortterm gains or losses and there is a transaction cost of 0 _._ 5 per share traded.
Prove that at date _t_ = 2 it is optimal to realize a loss if _k_ _>_ 1 _._ 25, and at
date _t_ = 1 it is optimal to realize a loss if _k_ _>_ 5 _._ Prove that it is optimal not
to realize gains at any date.


**Exercise** **14.3** Consider the model for portfolio choice with taxes described in
Example 14.2.


(a) Prove that for _τ_ = 0 then the optimal holding of the risky asset at _t_ = 0 is
_n_ 0 = 0 for any risk-averse concave utility function _U_ ( _W_ ).
(b) Check numerically that for _τ_ = 0 _._ 2, _δ_ = 0 _._ 1, _k_ = 0 _._ 2 _,_ and logarithmic utility
function _U_ ( _W_ ) = log( _W_ ), the optimal holding at _t_ = 0 is _n_ 0 = 0 _._ 8352.


**Exercise** **14.4**


(a) Consider the following minimum-variance portfolio optimization problem
with risky assets, transaction costs, and no constraints:



min
**x**




1 [1]
2 **[x]** [T] **[Vx]** [ +] 2




       
[1] _._ (14.2)

2 [(] **[x]** _[ −]_ **[x]** [0][)][T] **[ R]** [(] **[x]** _[ −]_ **[x]** [0][)]



Here **x** 0 is some initial portfolio, **V** is the covariance matrix of asset returns,
and **R** is a symmetric positive definite matrix that models the transaction
cost incurred in changing the initial portfolio **x** 0 to the new portfolio **x** _._
Prove that the solution to (14.2) is


**x** _[∗]_ = ( **V** + **R** ) _[−]_ [1] **Rx** 0 _._


(b) Now consider a multi-period version of the previous problem. Assume the
investor starts with an initial portfolio **x** 0 and her objective is




- 1
_t_ **[Vx]** _[t]_ [+] [1] _._
2 **[x]** [T] 2 [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)][T] **[R]** [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)]



min
**x** 1 _,...,_ **x** _T_




- _T_


_t_ =1



Apply dynamic programming to solve this problem. Proceed as follows:

_•_ the stages are _t_ = 1 _, . . ., T_ ;

_•_ the state at stage _t_ is **x** _t−_ 1, that is, the portfolio previously set at stage
_t −_ 1;

_•_ the action at stage _t_ is the vector of holdings **x** _t_ ;

_•_ the cost at stage _t_ is the quadratic term
1 _t_ **[Vx]** _[t]_ [+] [1]
2 **[x]** [T] 2 [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)][T] **[R]** [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)] _[.]_

(i) Show that the optimal optimal decision rule **x** _[∗]_ _T_ [and] [the] [value-to-go]
function _JT_ ( **x** _T −_ 1) at the last stage _T_ are

**x** _[∗]_ _T_ [= (] **[V]** [ +] **[ R]** [)] _[−]_ [1] **[Rx]** _[T][ −]_ [1]


and

_JT_ ( **x** _T −_ 1) = [1] _T −_ 1 **[K]** _[T]_ **[x]** _[T][ −]_ [1] _[,]_

2 **[x]** [T]

where **K** _T_ = **R** _−_ **R** ( **V** + **R** ) _[−]_ [1] **R** _._


236 **Dynamic** **Programming** **Models:** **Multi-Period** **Optimization**


(ii) Use the Bellman equation and induction to prove that the optimal decision rule **x** _[∗]_ _t_ [and the value-to-go function] _[ J][t]_ [(] **[x]** _[t][−]_ [1][) at each stage] _[ t]_ [ =] _[ T][ −]_ [1] _[,]_
_T_ _−_ 2 _, . . .,_ 1 are of the form

**x** _[∗]_ _t_ [=] **[ L]** _[t]_ **[x]** _[t][−]_ [1]



and



_Jt_ ( **x** _t−_ 1) = [1] _t−_ 1 **[K]** _[t]_ **[x]** _[t][−]_ [1]

2 **[x]** [T]



for some suitable matrices **L** _t_ and **K** _t_ .
(c) Now consider an infinite horizon version of the previous problem. Assume
there is only one risky asset, the investor starts with an initial portfolio _x_ 0
and her objective is




_q_
2 _[x]_ _t_ [2] [+] 2 _[r]_ [(] _[x][t][ −]_ _[x][t][−]_ [1][)][2][�] _._



min
_x_ 1 _,x_ 2 _,..._




- _∞_


_t_ =1



Use the following educated guess (“ansatz”) for the optimal value function:

_V_ ( _xt−_ 1) = _[k]_ 2 _[x]_ _t_ [2] _−_ 1 (14.3)

for some constant _k_ _>_ 0. In other words, our educated guess is that the value
function starting at stage _t_ with state _xt−_ 1, namely




_q_
2 _[x]_ _τ_ [2] [+] 2 _[r]_ [(] _[x][τ]_ _[−]_ _[x][τ]_ _[−]_ [1][)][2][�] _,_



_V_ ( _xt−_ 1) := min
_xt,xt_ +1 _,..._




- _∞_


_τ_ = _t_



is of the form (14.3) for some constant _k_ _>_ 0.
Use the Bellman equation to verify this educated guess, determine the
optimal decision rule _x_ _[∗]_ _t_ [,] [and] [find] [the] [value] [of] _[k]_ [in] [terms] [of] _[q, r.]_
Give expressions for both _k_ and the optimal portfolio _x_ _[∗]_ _t_ [that are as explicit]
as possible.


**Exercise** **14.5**


(a) Consider the mean–variance portfolio optimization problem with risk-free
asset and no constraints:



max
**x**




_**μ**_ [T] **x** _−_ _[γ]_




   
_[γ]_ 2 **[x]** [T] **[Vx]** _._ (14.4)



Here _**μ**_ is the vector of excess returns, **V** is the covariance matrix, **x** is the
vector of holdings in risky assets, and _γ_ _>_ 0 is a risk-aversion constant.
Prove that the solution to (14.4) is

**x** _[∗]_ = [1]

_γ_ **[V]** _[−]_ [1] _**[μ]**_ _[.]_



(b) Now consider a variation of the previous problem that includes a quadratic
term for transaction costs:




       
_[λ]_ _._ (14.5)

2 [(] **[x]** _[ −]_ **[x]** [0][)][T] **[ V]** [(] **[x]** _[ −]_ **[x]** [0][)]



max
**x**




_**μ**_ [T] **x** _−_ _[γ]_




_[γ]_

2 **[x]** [T] **[Vx]** _[ −]_ _[λ]_ 2



Here **x** 0 is some initial portfolio and _λ >_ 0 is a transaction cost constant.


**14.5** **Exercises** 237


Prove that the solution to (14.5) is


1 _λ_
**x** _[∗]_ =
_γ_ + _λ_ **[V]** _[−]_ [1] _**[μ]**_ [ +] _γ_ + _λ_ **[x]** [0] _[.]_


(c) Now consider a multi-period version of the previous problem. Assume the
objective is




         - [�]

_[λ]_

2 [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)][T] **[ V]** [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)]



max
**x** 1 _,...,_ **x** _T_ [E]





- _T_


_t_ =1




_**μ**_ [T] _t_ **[x]** _[t]_ _[−]_ _[γ]_




_[γ]_ _t_ **[Vx]** _[t]_ _[−]_ _[λ]_

2 **[x]** [T] 2



_._



This assumes that the vector of expected returns may vary with time but not
the covariance matrix. Apply dynamic programming to solve this problem.
Proceed as follows:

_•_ the stages are _t_ = 1 _, . . ., T_ ;

_•_ the state at stage _t_ is ( **x** _t−_ 1 _,_ _**μ**_ _t_ );

_•_ the action at stage _t_ is the vector of holdings **x** _t_ ;

_•_ the reward at stage _t_ is the quadratic term



_**μ**_ [T] _t_ **[x]** _[t]_ _[−]_ _[γ]_




_[γ]_ _t_ **[Vx]** _[t]_ _[−]_ _[λ]_

2 **[x]** [T] 2



2 [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)][T] **[ V]** [(] **[x]** _[t][ −]_ **[x]** _[t][−]_ [1][)] _[.]_



(i) Show that the optimal decision rule **x** _[∗]_ _T_ [and] [the] [value-to-go] [function]
_JT_ ( **x** _T −_ 1 _,_ _**μ**_ _T_ ) at the last stage _T_ are

**x** _[∗]_ _T_ [=] _[ a]_ **[ V]** _[−]_ [1] _**[μ]**_ _T_ [+] _[ b]_ **[ x]** _[T][ −]_ [1] _[,]_


and



_JT_ ( **x** _T −_ 1 _,_ _**μ**_ _T_ ) = _[c]_



2 _[c]_ _**[μ]**_ _T_ [T] **[V]** _[−]_ [1] _**[μ]**_ _T_ [+] _[d]_ 2



2 **[x]** _T_ [T] _−_ 1 **[Vx]** _[T][ −]_ [1] [+] _[ e]_ _**[ μ]**_ [T] _T_ **[x]** _[T][ −]_ [1] _[,]_



for some constants _a, b, c, d, e._
(ii) *Assume _**μ**_ _t_ has the following (simple and somewhat unrealistic) law of
motion:

_**μ**_ _t_ +1 = _**μ**_ ¯ + _ρ_ ( _**μ**_ _t −_ _μ_ ¯) + _**ϵ**_ _t,_


where _μ, ρ_ ¯ are constants, _|ρ|_ _<_ 1, and _**ϵ**_ _t_ is a vector of independently
normally distributed random shocks each with mean 0 and variance 1.
Use the Bellman equation and induction to prove that the optimal decision rule **x** _[∗]_ _t_ [and] [the] [value-to-go] [function] _[J][t]_ [(] **[x]** _[t][−]_ [1] _[,]_ _**[ μ]**_ _t_ [)] [at] [each] [stage] _[t]_ [ =]
_T_ _−_ 1 _, T_ _−_ 2 _, . . .,_ 1 are


**x** _[∗]_ _t_ [=] _[ a][t]_ **[V]** _[−]_ [1] _**[μ]**_ _t_ [+] _[ b][t]_ **[x]** _[t][−]_ [1] _[,]_


and



_Jt_ ( **x** _t−_ 1 _,_ _**μ**_ _t_ ) = _[c][t]_




_[c][t]_ _[d][t]_

2 _**[μ]**_ _[t]_ **[V]** _[−]_ [1] _**[μ]**_ _[t]_ [ +] 2




_[t]_

_t−_ 1 **[Vx]** _[t][−]_ [1] [+] _[ e][t]_ _**[μ]**_ [T] _t_ **[x]** _[t][−]_ [1] [+] _[ f][t][,]_
2 **[x]** [T]



for some constants _at, bt, ct, dt, et, ft_ .


## 15 Dynamic Programming Models: the Binomial Pricing Model

One of the most common uses of dynamic programming in financial mathematics
is through lattice models. In particular, the _binomial_ _lattice_ _model_ of Cox et al.
(1979) has become an indispensable tool for pricing derivative securities. This
chapter describes this model and the underlying dynamic programming principles
for the pricing of European options and the pricing and optimal exercising of
American options.


**15.1** **Binomial** **Lattice** **Model**


The binomial lattice provides a model for the price movements of a risky asset.
It can be seen as a multi-period version of the single-period binomial model
discussed in Section 4.3. The binomial lattice model describes the price of a
risky asset at some discrete times 0 _,_ 1 _, . . ., N_ . A basic period length, such as a
week, day, or second, is assumed to elapse between any two consecutive times.
The model assumes that if the share price of the risky asset is _Sk_ at time _k_ then
the share price _Sk_ +1 at time _k_ +1 can take two values, namely _Sk_ +1 = _u_ _·_ _Sk_ and
_Sk_ +1 = _d · Sk_ where _u > d >_ 0 are multiplicative factors ( _u_ stands for “up” and
_d_ for “down” factors). The probabilities assigned to these two possible states are
_p_ and 1 _−_ _p_ respectively, where 0 _<_ _p_ _<_ 1. The multi-stage price structure can
be represented on a lattice as illustrated in Figure 15.1.
After _k_ time periods, the asset price can take _k_ +1 different values. If the price
at stage 0 is _S_ 0, then the price _Sk_ at stage _k_ is _u_ _[j]_      - _d_      - _[k][−][j]_ _S_ 0 if there are _j_ up moves
and _k −_ _j_ down moves. Observe that there are _kj_ possible paths to reach the
node corresponding to _j_ up moves and _t−j_ down moves after _t_ periods. Therefore

                                -                                 the probability that the price is _u_ _[j]_ _d_ _[k][−][j]_ _S_ 0 in stage _k_ is _kj_ _p_ _[j]_ (1 _−_ _p_ ) _[k][−][j]_ because
between two consecutive times the probability of an up move is _p_ whereas that
of a down move is 1 _−_ _p_ .


**15.2** **Option** **Pricing**


Using the above binomial lattice model for the price process of an underlying
risky asset, the value of an option on this asset can be computed by dynamic programming by using backward recursion, working from the maturity date (time _N_ )


**15.2** **Option** **Pricing** 239


u [3] S



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-251-0.png)







0 1 2 3 Time


**Figure** **15.1** Asset price in the binomial lattice model


back to time 0 (the current time). The approach fits within the stochastic setting
introduced in Section 13.7. More precisely, the stages of the dynamic program
are the discrete times _k_ = 0 _, . . ., N_ . The state at stage _k_ is the asset price _Sk_ .
Thus _Sk_ can take the _k_ + 1 possible values defined by the _k_ + 1 nodes in the _k_ th
layer of the lattice. The state _SN_ at the final stage _N_ is the _terminal_ _state_ . The
law of motion for the asset price is as follows:

           _Sk_ +1 = _uSdSkk_ withwith probabilityprobability _pq_ = 1 _−_ _p_


for _k_ = 0 _,_ 1 _, . . ., N._ However, the following adjustment of utmost importance
must be made: for option pricing purposes, we do not use these actual probabilities _p_ and _q_ = 1 _−_ _p_ but instead the risk-neutral probabilities _p_ ˜ and _q_ ˜ = 1 _−_ _p_ ˜
as explained below.


15.2.1 European Options


Consider a European option contract that matures at time _N_ with payoff _g_ ( _SN_ )
for some function _g_ ( _·_ ) of the underlying asset price _SN_ . For instance, if the
contract is a European call option maturing at time _N_ with strike price _K_, the
payoff at maturity is _g_ ( _SN_ ) = ( _SN −K_ ) [+] . Similarly, if the contract is a European
put option maturing at time _N_ with strike price _K_, the payoff at maturity is
_g_ ( _SN_ ) = ( _K −_ _SN_ ) [+] .
Let _Vk_ ( _Sk_ ) denote the value of the option at stage _k_ when the asset price is _Sk_ .
This is the value-to-go function in our dynamic program. The value of the option
at stage 0 is given by _V_ 0( _S_ 0). This is the quantity that we have to compute in
order to solve the option pricing problem. At the final time _N_ the value-to-go
function is given by the payoff of the option contract. That is,


_VN_ ( _SN_ ) = _g_ ( _SN_ ) _._


Since we are dealing with a European option, we can compute the value _Vk_ ( _·_ )


240 **Dynamic** **Programming** **Models:** **the** **Binomial** **Pricing** **Model**


in terms of _Vk_ +1( _·_ ). The single-period subproblem between stages _k_ and _k_ + 1 is
identical to the single-period binomial model discussed in Section 4.3. Therefore,
the value _Vk_ ( _Sk_ ) can be obtained via the _risk-neutral_ probabilities (4.4), namely




_[ r][ −]_ _[d]_

and _q_ ˜ = _[u][ −]_ [1] _[ −]_ _[r]_
_u −_ _d_ _u −_ _d_



_p_ ˜ = [1 +] _[ r][ −]_ _[d]_



_,_
_u −_ _d_



where _r_ is the one-period return on the risk-free asset between time _k_ and time _k_ +
1. Thus for European options the value-to-go functions _Vk_ ( _·_ ) can be recursively
computed as


1
_Vk_ ( _Sk_ ) = (15.1)
1 + _r_ [(˜] _[pV][k]_ [+1][(] _[uS][k]_ [) + ˜] _[qV][k]_ [+1][(] _[dS][k]_ [))] _[ .]_


**Example** **15.1** Consider a binomial lattice model with _N_ = 3 _, u_ = 2 _, d_ =
12 _[, r]_ [=] [0] _[.]_ [25] _[,]_ [and] _[S]_ [0] [=] [40] [as] [depicted] [in] [Figure] [15.2.] [Compute] [the] [price] [of] [a]
European call option with strike price _K_ = 50.


320



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-252-0.png)









0 1 2 3 Time


**Figure** **15.2** Binomial lattice with _u_ = 2 _, d_ = 0 _._ 5 _, S_ 0 = 40 _, N_ = 3


For these values of _u, d, r_ the risk-neutral probabilities are




_[.]_ [75] [1]

1 _._ 5 [=] 2



_p_ ˜ = _q_ ˜ = [0] _[.]_ [75]



2 _[.]_



The option value _V_ 3( _S_ 3) = ( _S_ 3 _−_ 50) [+] at the final stage 3 is as follows:


_V_ 3(5) = _V_ 3(20) = 0 _,_ _V_ 3(80) = 30 _,_ _V_ 3(320) = 270 _._


Next, applying (15.1) we get _V_ 2( _S_ 2):



1
_V_ 2(10) = 0 _,_ _V_ 2(40) = [30]
1 _._ 25 _[·]_ 2



1

_[V]_ [2][(160) =] [30 + 270]
2 [= 12] _[,]_ 1 _._ 25 _[·]_ 2



= 120 _._
2



Applying (15.1) again we get _V_ 1( _S_ 1):



1
_V_ 1(20) = [12]
1 _._ 25 _[·]_ 2



1

_[V]_ [1][(80) =] [120 + 12]
2 [= 4] _[.]_ [8] _[,]_ 1 _._ 25 _[·]_ 2



= 52 _._ 8 _._
2


**15.2** **Option** **Pricing** 241


Finally applying (15.1) one more time, we get the option value _V_ 0( _S_ 0):


1
_V_ 0(40) = [4] _[.]_ [8 + 52] _[.]_ [8] = 23 _._ 04 _._
1 _._ 25 _[·]_ 2

**Example** **15.2** Consider a binomial lattice model with _N_ = 3, _u_ = 2, _d_ = [1] 2 [,]

_r_ = 0 _._ 25, and _S_ 0 = 40. Compute the price of a European put option with strike
price _K_ = 60.


Again the risk-neutral probabilities are _p_ ˜ = _q_ ˜ = 12 [.] [We] [can] [proceed] [as] [in]
Example 15.1. The option value _V_ 3( _S_ 3) = (60 _−_ _S_ 3) [+] at the final stage 3 is


_V_ 3(5) = 55 _,_ _V_ 3(20) = 40 _,_ _V_ 3(80) = _V_ 3(320) = 0 _._


Next, applying (15.1) we get _V_ 2( _S_ 2):



1
_V_ 2(10) = [55 + 40]
1 _._ 25 _[·]_ 2



1
= 38 _,_ _V_ 2(40) = [40]
2 1 _._ 25 _[·]_ 2




_[V]_ [2][(160) = 0] _[.]_
2 [= 16] _[,]_



Applying (15.1) again we get _V_ 1( _S_ 1):



1
_V_ 1(20) = [38 + 16]
1 _._ 25 _[·]_ 2



1
= 21 _._ 6 _,_ _V_ 1(80) = [16]
2 1 _._ 25 _[·]_ 2



2 [= 6] _[.]_ [4] _[.]_



Finally applying (15.1) one more time, we get the option value _V_ 0( _S_ 0):


1
_V_ 0(40) = [21] _[.]_ [6 + 6] _[.]_ [4] = 11 _._ 2 _._
1 _._ 25 _[·]_ 2


15.2.2 American Options


Consider now an American option contract that can be exercised at any time
_k_ = 0 _,_ 1 _, . . ., N_ with payoff _g_ ( _Sk_ ) for some function _g_ ( _·_ ) of the underlying asset
price _Sk_ . The key difference between this type of _American_ _option_ contract and
the above type of _European_ _option_ contract is the possibility of early exercise.
Because of this additional feature in the contract, the pricing problem of an
American option needs to account for the optimal exercise timing of the option.
This is accomplished via an adjustment to the previous recursion in the calculation of the value function.
Once again, at the final time _N_ the value-to-go function is given by the payoff
of the option contract. That is,


_VN_ ( _SN_ ) = _g_ ( _SN_ ) _._


The computation of the value-to-go function _Vk_ ( _·_ ) in terms of _Vk_ +1( _·_ ) needs to
reflect the possibility of early exercise. To that end, the recursive formula (15.1)
needs to be amended as follows:

          -          1
_Vk_ ( _Sk_ ) = max _._ (15.2)
1 + _r_ [(˜] _[pV][k]_ [+1][(] _[uS][k]_ [) + ˜] _[qV][k]_ [+1][(] _[dS][k]_ [))] _[, g]_ [(] _[S][k]_ [)]


In words, the value of the option at stage _k_ is the maximum of the following two
quantities: the first one is the discounted value of the option at stage _k_ +1 or the


242 **Dynamic** **Programming** **Models:** **the** **Binomial** **Pricing** **Model**


payoff obtained if the option is exercised immediately. When the latter is larger,
it is optimal to exercise the option at stage _k_ .


**Example** **15.3** Consider a binomial lattice model with _N_ = 3, _u_ = 2, _d_ = [1] 2 [,]

_r_ = 0 _._ 25, and _S_ 0 = 40. Compute the price of an American call option with strike
price _K_ = 50.


Again the risk-neutral probabilities are _p_ ˜ = _q_ ˜ = [1] 2 _[.]_ [The] [option] [value] _[V]_ [3][(] _[S]_ [3][) =]

( _S_ 3 _−_ 50) [+] at the final stage 3 is


_V_ 3(5) = _V_ 3(20) = 0 _,_ _V_ 3(80) = 30 _,_ _V_ 3(320) = 270 _._



Next, applying (15.2) we get _V_ 2( _S_ 2):




        1
_V_ 2(10) = 0 _,_ _V_ 2(40) = max [30]
1 _._ 25 _[·]_ 2




     _,_ (160 _−_ 50) [+] = 120 _._
2




     1
_V_ 2(160) = max [30 + 270]
1 _._ 25 _[·]_ 2




    2 _[,]_ [ (40] _[ −]_ [50)][+] = 12 _,_



Observe that regardless of the value of _S_ 2, it is not optimal to exercise the option
at stage 2.
Applying (15.2) again we get _V_ 1( _S_ 1):




    2 _[,]_ [ (20] _[ −]_ [50)][+] = 4 _._ 8 _,_




    1
_V_ 1(20) = max [12]
1 _._ 25 _[·]_ 2




     _,_ (80 _−_ 50) [+] = 52 _._ 8 _._
2




    1
_V_ 1(80) = max [120 + 12]
1 _._ 25 _[·]_ 2



Observe that regardless of the value of _S_ 1, it is not optimal to exercise the option
at stage 1.
Finally applying (15.2) one more time, we get the option value _V_ 0( _S_ 0):




     
[8 + 4] _[.]_ [8]

_,_ (40 _−_ 50) [+] = 23 _._ 04 _._
2




    1
_V_ 0(40) = max [52] _[.]_ [8 + 4] _[.]_ [8]
1 _._ 25 _[·]_ 2



Observe that there is no difference in price and in exercise policy between the
American and the European call options.


**Example** **15.4** Consider a binomial lattice model with _N_ = 3, _u_ = 2, _d_ = [1] 2 [,]

_r_ = 0 _._ 25, and _S_ 0 = 40. Compute the price of an American put option with strike
price _K_ = 60.


Once again, the risk-neutral probabilities are _p_ ˜ = _q_ ˜ = [1] 2 _[.]_ [The] [option] [value]

_V_ 3( _S_ 3) = (60 _−_ _S_ 3) [+] at the final stage 3 is


_V_ 3(5) = 55 _,_ _V_ 3(20) = 40 _,_ _V_ 3(80) = _V_ 3(320) = 0 _._



Next, applying (15.2) we get _V_ 2( _S_ 2)




    1
_V_ 2(10) = max [55 + 40]
1 _._ 25 _[·]_ 2




    
= 20 _,_ _V_ 2(160) = 0 _._
2 _[,]_ [ (60] _[ −]_ [40)][+]




    1
_V_ 2(40) = max [40]
1 _._ 25 _[·]_ 2




     _,_ (60 _−_ 10) [+] = 50 _,_
2


**15.2** **Option** **Pricing** 243



Observe that it is optimal to exercise the option at stage 2 when _S_ 2 = 10 and
_S_ 2 = 40.
Applying (15.2) again we get _V_ 1( _S_ 1)




    1
_V_ 1(20) = max [50 + 20]
1 _._ 25 _[·]_ 2




    2 _[,]_ [ (60] _[ −]_ [80)][+] = 8 _._




    1
_V_ 1(80) = max [20]
1 _._ 25 _[·]_ 2




     _,_ (60 _−_ 20) [+] = 40 _,_
2



Observe that it is optimal to exercise the option at stage 1 when _S_ 1 = 20.
Finally applying (15.2) one more time, we get the option value _V_ 0( _S_ 0)




     _,_ (60 _−_ 40) [+] = 20 _._
2




     1
_V_ 0(40) = max [40 + 8]
1 _._ 25 _[·]_ 2



Observe that it is optimal to exercise the option at this stage.
Notice that the prices of the American and European calls in Example 15.1
and Example 15.3 are identical. This happens because there is nothing to gain by
early exercising of the American call. By contrast, there is a substantial difference
in the prices of the American and European puts in Example 15.2 and Example
15.4. This happens because sometimes it is advantageous to exercise an American
put early. The results of these examples illustrate the following far more general
property of American options.


**Theorem** **15.5** _Consider_ _the_ _binomial_ _lattice_ _model_ _described_ _in_ _Section_ _15.1,_
_and_ _an_ _American_ _option_ _contract_ _on_ _the_ _underlying_ _risky_ _asset_ _that_ _can_ _be_
_exercised_ _at_ _any_ _time_ _k_ = 0 _,_ 1 _, . . ., N_ _with_ _payoff_ _g_ ( _Sk_ ) _for_ _some_ _function_ _g_ ( _·_ ) _._
_If_ _r_ _≥_ 0 _and_ _the_ _function_ _g_ ( _·_ ) _is_ _convex_ _and_ _satisfies_ _g_ (0) = 0 _,_ _then_ _the_ _value_ _of_
_the_ _American_ _option_ _contract_ _is_ _the_ _same_ _as_ _that_ _of_ _a_ _European_ _option_ _contract_
_with_ _payoff_ _g_ ( _SN_ ) _that_ _can_ _only_ _be_ _exercised_ _at_ _stage_ _N_ _._ _In_ _other_ _words,_ _early_
_exercising_ _of_ _the_ _American_ _option_ _yields_ _no_ _advantage._


_Proof_ By (15.2), it suffices to show that the following equation and inequality
hold for _k_ = 0 _,_ 1 _, . . ., N_ _−_ 1:


1
_Vk_ ( _Sk_ ) = (15.3)
1 + _r_ [(˜] _[pV][k]_ [+1][(] _[uS][k]_ [) + ˜] _[qV][k]_ [+1][(] _[dS][k]_ [))] _[ ≥]_ _[g]_ [(] _[S][k]_ [)] _[.]_

First, observe that for _k_ = 0 _,_ 1 _, . . ., N_ _−_ 1


1
_Sk_ = (15.4)
1 + _r_ [(˜] _[puS][k]_ [ + ˜] _[qdS][k]_ [)] _[,]_


since _p,_ ˜ ˜ _q_ are the risk-neutral probabilities.
Next, we prove (15.3) by (backward) induction on _k_ . The assumptions on the
function _g_ ( _·_ ), equation (15.4), and _VN_ ( _SN_ ) = _g_ ( _SN_ ) imply that




    _r ·_ 0 + _puS_ ˜ _N_ _−_ 1 + ˜ _qdSN_ _−_ 1
_g_ ( _SN_ _−_ 1) = _g_
1 + _r_







_r_ 1
_≤_ 1 + _r_ _[·][ g]_ [(0) +] 1 + _r_ [(˜] _[pg]_ [(] _[uS][N]_ _[−]_ [1][) + ˜] _[qg]_ [(] _[dS][N]_ _[−]_ [1][))]

1
=
1 + _r_ [(˜] _[pV][N]_ [(] _[uS][N]_ _[−]_ [1][) + ˜] _[qV][N]_ [(] _[dS][N]_ _[−]_ [1][))] _[.]_


244 **Dynamic** **Programming** **Models:** **the** **Binomial** **Pricing** **Model**



Therefore (15.3) holds for _k_ = _N −_ 1. Suppose (15.3) holds for _k_ = _j_ +1 _≤_ _N −_ 1.
The assumptions on _g_ ( _·_ ), equation (15.4), and the induction hypothesis imply
that




   _r ·_ 0 + _puS_ ˜ _j_ + ˜ _qdSj_
_g_ ( _Sj_ ) = _g_
1 + _r_







_r_ 1
_≤_ 1 + _r_ _[·][ g]_ [(0) +] 1 + _r_ [(˜] _[pg]_ [(] _[uS][j]_ [) + ˜] _[qg]_ [(] _[dS][j]_ [))]

1
_≤_
1 + _r_ [(˜] _[pV][j]_ [+1][(] _[uS][j]_ [) + ˜] _[qV][j]_ [+1][(] _[dS][j]_ [))] _[.]_


Hence (15.3) holds for _k_ = _j_ as well.


**15.3** **Option** **Pricing** **in** **Continuous** **Time**


The binomial lattice model can be seen as a discrete version of a popular
continuous-time _geometric_ _Brownian_ _motion_ _model_ . We next sketch some of the
main ideas and results of this continuous model and its relation to the binomial
lattice model discussed above. A full treatment of this topic is beyond the scope
of this book. We refer the reader to Shreve (2000) for a detailed exposition of
this topic.
Suppose the continuous-time price _St_, with _t_ _∈_ [0 _, T_ ], of a risky asset evolves
according to the stochastic differential equation


_dSt_

= _μdt_ + _σdWt,_ (15.5)
_St_


where _μ_ and _σ_ are constants representing the instantaneous _drift_ and _volatility_
of the asset price _St_, and _Wt_ is a Brownian motion. The stochastic differential
equation (15.5) can be seen as a continuous-time analog of the one-period up or
down price movement in the binomial lattice model. The solution to (15.5) is the
continuous-time process

_St_ = _S_ 0 _e_ [(] _[μ][−][σ]_ [2] _[/]_ [2)] _[t]_ [+] _[σW][t]_ _,_ (15.6)



which can equivalently be written as




  
_[S][t]_ = _μ −_ _[σ]_ [2]

_S_ 0 2



log _[S][t]_



2





_t_ + _σWt._



Techniques from stochastic calculus have led to the development of pricing
models for a wide variety of options provided the underlying risky asset is
modeled via a suitable stochastic differential equation. In particular, in their
seminal and ground-breaking work Black and Scholes (1973) and Merton (1973)
derived a pricing formula for a European option on an underlying risky asset with
a price process modeled as a geometric Brownian motion. In particular, consider
a call option maturing at time _T_ _>_ 0 with payoff ( _ST_ _−_ _K_ ) [+] . Assume the price
of the underlying risky asset is as in (15.6) and the risk-free asset compounds
continuously at an instantaneous rate _r_ _≥_ 0; that is, the price _Bt_ of the risk-free


asset is



**15.4** **Specifying** **the** **Model** **Parameters** 245


_Bt_ = _B_ 0 _e_ _[rt]_ _._



The Black–Scholes–Merton model yields the following explicit formula for the
price _Vt_ ( _St_ ) at time _t ∈_ [0 _, T_ ] of a European call option with payoff ( _ST_ _−_ _K_ ) [+] :


_Vt_ ( _St_ ) = Φ( _d_ 1) _St −_ Φ( _d_ 2) _Ke_ _[−][r]_ [(] _[T][ −][t]_ [)] _,_ (15.7)



where




- ( _T_ _−_ _t_ ) _,_




- + _r_ + _[σ]_ [2]

2



Φ( _x_ ) = [1]




- _x_




- _St_
log
_K_



2 _π_



1
_e_ _[−][t]_ [2] _[/]_ [2] _dt,_ _d_ 1 = ~~_√_~~
_−∞_ _σ_ _T_



~~_√_~~
_d_ 2 = _d_ 1 _−_ _σ_



_T_ _−_ _t_



_T_ _−_ _t._



The Black–Scholes–Merton model also yields the following formula for the
price _Vt_ ( _St_ ) at time _t ∈_ [0 _, T_ ] of a European put option with payoff ( _K −_ _ST_ ) [+] :


_Vt_ ( _St_ ) = Φ( _−d_ 2) _Ke_ _[−][r]_ [(] _[T][ −][t]_ [)] _−_ Φ( _−d_ 1) _St,_


where Φ( _·_ ) _, d_ 1 _, d_ 2 are the same as above.
The binomial lattice model can be seen as a discrete approximation of the
geometric Brownian motion. The following section and Exercise 15.4 at the end
of the chapter elaborate on this approximation.


**15.4** **Specifying** **the** **Model** **Parameters**


To specify the binomial lattice model, one needs to choose values for _u_, _d_, and
_p_ . This is done by matching the mean and volatility of the asset price to the
mean and volatility of the above binomial distribution. Because the model is
multiplicative (the price _S_ of the asset being either _u · S_ or _d · S_ in the next
stage), it is convenient to work with log( _Sk_ +1 _/Sk_ ).
Let _Sk_ denote the asset price in stages _k_ = 0 _, . . ., N_ . Let _μ_ and _σ_ be the
mean and volatility of ln( _SN_ _/S_ 0). (We assume that this information about the
asset is known.) Let Δ = 1 _/N_ denote the length between consecutive stages.
Th ~~_√_~~ en for _k_ = 0 _,_ 1 _, . . ., N −_ 1 the mean and volatility of ln( _Sk_ +1 _/Sk_ ) are _μ_ Δ and
_σ_ Δ respectively. In the binomial lattice, a direct computation shows that for

_k_ = 0 _,_ 1 _, . . ., N −_ 1 the mean and variance of ln( _Sk_ +1 _/Sk_ ) are _p_ ln _u_ + (1 _−_ _p_ ) ln _d_
and _p_ (1 _−p_ )(ln _u−_ ln _d_ ) [2] respectively. Matching these values we get two equations:


_p_ ln _u_ + (1 _−_ _p_ ) ln _d_ = _μ_ Δ

_p_ (1 _−_ _p_ )(ln _u −_ ln _d_ ) [2] = _σ_ [2] Δ _._


Note that there are three parameters but only two equations, so we can set
_d_ = 1 _/u_ as in Cox et al. (1979). Then the equations simplify to


(2 _p −_ 1) ln _u_ = _μ_ Δ

4 _p_ (1 _−_ _p_ )(ln _u_ ) [2] = _σ_ [2] Δ _._


246 **Dynamic** **Programming** **Models:** **the** **Binomial** **Pricing** **Model**


Squaring the first and adding it to the second, we get (ln _u_ ) [2] = _σ_ [2] Δ + ( _μ_ Δ) [2] .
This yields



_√_
_u_ = _e_



_σ_ [2] Δ+( _μ_ Δ) [2]



_d_ = _e_ _[−][√]_



_σ_ [2] Δ+( _μ_ Δ) [2]











_p_ = [1]

2



1
1 + ~~�~~
1 + _σ_ [2] _/μ_ [2] Δ



_._



When Δ is small, these values can be approximated as



_√_
_u ≈_ _e_ _[σ]_



Δ



_√_
_d ≈_ _e_ _[−][σ]_



Δ



_p ≈_ [1]

2




1 + _[μ]_



_σ_



_√_ 
Δ _._



In other words, for small Δ



~~_√_~~
_−σ_



Δ with probability [1]

2

Δ with probability [1]




 Δ

 Δ _,_



_σ_



log _[S][k]_ [+1] _≈_

_Sk_



⎧
⎪⎨


⎪⎩



_√_
_σ_



Δ with probability [1]

2



_√_


_√_



2




1 + _[μ]_

_σ_

1 _−_ _[μ]_



_σ_



which is a discrete approximation of (15.5).
As an example, consider a binomial model with 52 periods of one week each.
Consider also a stock with current known price _S_ 0 and random price _S_ 52 a year
from today. We are given the mean _μ_ and volatility _σ_ of ln( _S_ 52 _/S_ 0), say _μ_ = 10%
and _σ_ = 30%. What are the parameters _u_, _d_, and _p_ of the binomial lattice? Since
Δ = 521 [is] [small,] [we] [can] [use] [the] [second] [set] [of] [formulas:]



_√_
_u ≈_ _e_ [0] _[.]_ [30] _[/]_ 52 = 1 _._ 0425



_√_
_d ≈_ _e_ _[−]_ [0] _[.]_ [30] _[/]_



52 = 0 _._ 9592



_p ≈_ [1]

2




0 _._ 10
1 + ~~_√_~~
0 _._ 30



52





= 0 _._ 523 _._



**15.5** **Exercises**


**Exercise** **15.1** Apply Theorem 15.5 to show that the price of a European call
option and an American call option with the same strike price and expiration
date are the same in the binomial lattice model. Why does Theorem 15.5 not
apply for put options?


**Exercise** **15.2** Compute the value of an American call option on a stock with
current price equal to $100, strike price equal to $102, and expiration date four
weeks from today. The yearly volatility of the logarithm of the stock return is
_σ_ = 0 _._ 30. The risk-free interest rate is 4%. Use a binomial lattice with _N_ = 4.


**15.5** **Exercises** 247


**Exercise** **15.3** Compute the value of an American put option on a stock with
current price equal to $100, strike price equal to $98, and expiration date five
weeks from today. The yearly volatility of the logarithm of the stock return is
_σ_ = 0 _._ 30. The risk-free interest rate is 4%. Use a binomial lattice with _N_ = 4.


**Exercise** **15.4** This is a computational exercise. Repeat Exercises 15.2 and
15.3 using a binomial lattice with _N_ = 10, _N_ = 100 _,_ and _N_ = 1000. Compare
the results obtained for the call option with those given by the Black–Scholes–
Merton formula (15.7).


## 16 Multi-Stage Stochastic Programming

_Stochastic_ _programming_ is a computational approach to stochastic optimization.
Stochastic programs have been studied for several decades (see, e.g., Birge and
Louveaux, 1997; Shapiro et al., 2009). Typically, the approach hinges on a
reformulation of the stochastic optimization problem as a deterministic one via
a _scenario_ _tree_ . Computational and algorithmic advances have made stochastic
programming techniques applicable to various classes of real-world problems.


**16.1** **Multi-Stage** **Stochastic** **Programming**


Multi-stage stochastic optimization can be seen as a generalization of the generic
class of stochastic optimization model discussed in Chapter 10. Let 0 _,_ 1 _, . . ., T_
index a set of stages where decisions are to be made. Assume that between two
consecutive stages _t −_ 1 and _t_ some random outcome _ωt_ is revealed. At each
stage _t_ = 0 _,_ 1 _, . . ., T_ we make a set of _non-anticipatory_ decisions **x** _t_ that can only
depend on the random information revealed up until that stage. Schematically,
the process can be seen as follows:


decision
_;_ [random] _;_ [decision] _;_ [random] _; · · · ;_ [random] _;_ [decision]
**x** 0 draw _ω_ 1 **x** 1 draw _ω_ 2 draw _ωT_ **x** _T_


A multi-stage stochastic minimization problem is the following kind of _multi-fold_
version of the two-stage stochastic model (10.2) discussed in Chapter 10:


min _g_ 0( **x** 0) + E[ _Q_ 1( **x** 0 _, ω_ 1)]
**x** 0 (16.1)

**x** 0 _∈X_ 0 _,_


where the recourse term _Q_ 1( **x** 0 _, ω_ 1) similarly depends on the decisions to be
made at later stages:


_Q_ 1( **x** 0 _, ω_ 1) := min _g_ 1( **x** 1 _, ω_ 1) + E[ _Q_ 2( **x** 1 _, ω_ 2)]
**x** 1

**x** 1 _∈X_ 1( **x** 0 _, ω_ 1) _,_


with


_Qt_ ( **x** _t−_ 1 _, ωt_ ) := min _gt_ ( **x** _t, ωt_ ) + E[ _Qt_ +1( **x** _t, ωt_ +1)]
**x** _t_

**x** _t_ _∈Xt_ ( **x** _t−_ 1 _, ωt_ ) _,_


**16.1** **Multi-Stage** **Stochastic** **Programming** 249


for _t_ = 2 _, . . ., T_ _−_ 1, and the last-stage recourse term _QT_ ( **x** _T −_ 1 _, ωT_ ) is of the
form
_QT_ ( **x** _T −_ 1 _, ωT_ ) := min _gT_ ( **x** _T, ωT_ )
**x** _T_

**x** _T_ _∈XT_ ( **x** _T −_ 1 _, ωT_ ) _._


The multi-stage optimization problem (16.1) can also be written as

       -       - ��

min min min _._
**x** 0 _∈X_ 0 _[g]_ [0][(] **[x]** [0][)+][E] **x** 1 _∈X_ 1( **x** 0 _,ω_ 1) _[g]_ [1][(] **[x]** [1] _[, ω]_ [1][) +] _[ · · ·]_ [ +][ E] **x** _T ∈XT_ ( **x** _T −_ 1 _,ωT_ ) _[g][T]_ [ (] **[x]** _[T][, ω][T]_ [ )]


Consider the special case of linear multi-stage stochastic optimization, where the
components are linear. More precisely, each _gt_ ( **x** _t, ωt_ ) = **c** [T] _t_ **[x]** _[t]_ [for] [some] [vector] **[c]** _[t]_
and each inter-temporal constraint **x** _t_ _∈Xt_ ( **x** _t−_ 1 _, ωt_ ) is of the form


**B** _t_ **x** _t−_ 1 + **A** _t_ **x** _t_ = **b** _t,_ **x** _t_ _≥_ 0 _,_


where _ωt_ = ( **c** _t,_ **A** _t,_ **B** _t,_ **b** _t_ ) is only revealed at stage _t_ . In this case we often write

         -         **x** 0 _,_ **x** min1 _,...,_ **x** _T_ E **c** [T] 0 **[x]** [0] + **c** [T] 1 **[x]** [1] + _· · ·_ + **c** [T] _T_ **[x]** _[T]_



s.t. **A** 0 **x** 0 = **b** 0
**B** 1 **x** 0 + **A** 1 **x** 1 = **b** 1
**B** 2 **x** 1 + **A** 2 **x** 2 = **b** 2
... ...
**B** _T_ **x** _T −_ 1 + **A** _T_ **x** _T_ = **b** _T_
**x** 0 _,_ **x** 1 _,_ _. . ._ **x** _T_ _≥_ 0 _._



(16.2)



**Example** **16.1** (Financial planning example) Assume an investor has initial
wealth _W_ 0 at _t_ = 0. At stage _t_ she can invest in two asset classes: bonds and
stocks. The (random) gross return on bonds from time _t −_ 1 to _t_ is _Rb,t_ and the
(random) gross return on stocks from _t_ _−_ 1 to _t_ is _Rs,t_ . Assume that the investor
needs to meet liabilities _Lt_ at times _t_ = 1 _, . . ., T_ . She wants to maximize her
expected wealth at time _T_ (after covering the liabilities). Assume no shorting is
allowed.


_Formulation_ _of_ _the_ _financial_ _planning_ _example_
**Variables:**
_xt_ : amount of money invested in bonds at stage _t_, for _t_ = 0 _, . . ., T −_ 1;
_yt_ : amount of money invested in stocks at stage _t_, for _t_ = 0 _, . . ., T −_ 1;
_WT_ : wealth at time _T_


max E( _WT_ )


s.t. _x_ 0 + _y_ 0 = _W_ 0
_Rb,txt−_ 1 + _Rs,tyt−_ 1 = _Lt_ + _xt_ + _yt,_ _t_ = 1 _, . . ., T_ _−_ 1
_Rb,T xT −_ 1 + _Rs,T yT −_ 1 = _LT_ + _WT_


_xt, yt_ _≥_ 0 _,_ _t_ = 0 _,_ 1 _, . . ., T_ _−_ 1
_WT_ _≥_ 0 _._


250 **Multi-Stage** **Stochastic** **Programming**


Notice that in this model the parameters _Rb,t_ and _Rs,t_ are unknown
prior to time _t_ .


**16.2** **Scenario** **Optimization**


As discussed in Chapter 10 for the two-stage case, a multi-stage optimization
model can be recast as a _deterministic_ _equivalent_ if each of the random outcomes has a discrete distribution. In this case for each stage _t_ = 1 _,_ 2 _, . . ., T_
there is a finite set of possible values or realizations _{ωt_ [1] _[, . . ., ω]_ _t_ _[S][}]_ [ for the random]
outcome _ωt_ . These sets of realizations can be described by an _event_ _tree_ as
depicted in Figure 16.1 for a problem with three stages. In this particular tree,
the random variables _ω_ 1 and _ω_ 2 have two- and five-valued discrete distributions
respectively. The tree structure is associated with the discrete filtration generated by the discrete-time random process _ω_ [ _t_ ] := ( _ω_ 1 _, ω_ 2 _, . . ., ωt_ ) _,_ _t_ = 1 _, . . ., T_ .
In particular, each possible value of _ω_ 2 has a unique _predecessor_ value of _ω_ 1. We
further elaborate on this tree structure below.


0 1 2 Stage


**Figure** **16.1** Event tree for a three-stage model


The set of scenarios described by the event tree in turn yield a deterministic
equivalent of a multi-stage stochastic optimization model. We next illustrate
this equivalence for the stochastic optimization model described in Example 16.1
in a particularly simple event tree. We subsequently describe the deterministic
equivalent for linear multi-stage stochastic programs in more general event trees.


**Example** **16.2** (Financial planning revisited) Consider the model described in
Example 16.1. Suppose _T_ = 2 and there are two equally likely outcomes (“ _H_ ”
and “ _T_ ”) for the joint returns ( _Rb,t, Rs,t_ ) over each period, say


( _Rb,t_ ( _H_ ) _, Rs,t_ ( _H_ )) = (1 _._ 14 _,_ 1 _._ 25) and ( _Rb,t_ ( _T_ ) _, Rs,t_ ( _T_ )) = (1 _._ 1 _,_ 1 _._ 06) _._


Figure 16.2 illustrates the corresponding scenario tree. In this event tree the
labels “ _H_ ” and “ _T_ ” on the edges indicate the specific outcome between two



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-262-0.png)
**16.2** **Scenario** **Optimization** 251


consecutive stages. Observe that each of the four scenarios _HH, HT, TH, TT_ in
the event tree occurs with probability 1 _/_ 4.



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-263-0.png)





0 1 2 Stage


**Figure** **16.2** Event tree for financial planning model


The scenario tree in turn yields a deterministic equivalent formulation for the
financial planning stochastic optimization model. In the deterministic equivalent
the stage 0 decisions are made at the root of the tree and thus may not depend
on any of the random outcomes. The stage 1 decisions may depend on the initial
path _H_ or _T_ realized up to stage 1 in the event tree. Finally, the stage 2 decisions
may depend on the path _HH_, _HT_, _TH_, or _TT_ realized up to stage 2 in the event
tree. The corresponding adaptiveness of the variables and constraints is explicitly
reflected in the following deterministic equivalent formulation.


_Scenario_ _optimization_ _model_
**Variables:**
_x_ 0 _, y_ 0: money in bonds and stocks at _t_ = 0;
_x_ 1( _H_ ) _, x_ 1( _T_ ) _, y_ 1( _H_ ) _, y_ 1( _T_ ): money in bonds and stocks at _t_ = 1;
_W_ 2( _HH_ ) _, W_ 2( _HT_ ) _, W_ 2( _TH_ ) _, W_ 2( _TT_ ): wealth at _t_ = 2


1
max 4 _[·]_ [ (] _[W]_ [2][(] _[HH]_ [) +] _[ W]_ [2][(] _[HT]_ [) +] _[ W]_ [2][(] _[TH]_ [) +] _[ W]_ [2][(] _[TT]_ [))]

s.t. _x_ 0 + _y_ 0 = _W_ 0 (stage 0)


1 _._ 14 _x_ 0 + 1 _._ 25 _y_ 0 = _L_ 1 + _x_ 1( _H_ ) + _y_ 1( _H_ ) (stage 1, path _H_ )
1 _._ 1 _x_ 0 + 1 _._ 06 _y_ 0 = _L_ 1 + _x_ 1( _T_ ) + _y_ 1( _T_ ) (stage 1, path _T_ )


1 _._ 14 _x_ 1( _H_ ) + 1 _._ 25 _y_ 1( _H_ ) = _L_ 2 + _W_ 2( _HH_ ) (stage 2, _HH_ )
1 _._ 1 _x_ 1( _H_ ) + 1 _._ 06 _y_ 1( _H_ ) = _L_ 2 + _W_ 2( _HT_ ) (stage 2, _HT_ )
1 _._ 14 _x_ 1( _T_ ) + 1 _._ 25 _y_ 1( _T_ ) = _L_ 2 + _W_ 2( _TH_ ) (stage 2, _TH_ )
1 _._ 1 _x_ 1( _T_ ) + 1 _._ 06 _y_ 1( _T_ ) = _L_ 2 + _W_ 2( _TT_ ) (stage 2, _TT_ )


_x_ 0 _, y_ 0 _, x_ 1( _H_ ) _, x_ 1( _T_ ) _, y_ 1( _H_ ) _, y_ 1( _T_ ) _≥_ 0
_W_ 2( _HH_ ) _, W_ 2( _HT_ ) _, W_ 2( _TH_ ) _, W_ 2( _TT_ ) _≥_ 0 _._


252 **Multi-Stage** **Stochastic** **Programming**


The above scenario optimization approach is quite flexible. In particular,
consider a variation of the above financial planning model where the objective
is max E ( _U_ ( _WT_ )) for some concave utility function _U_ ( _W_ ). The corresponding
deterministic equivalent has exactly the same variables and constraints as the
one above and the following objective:


max [1]

4 [(] _[U]_ [(] _[W]_ [2][(] _[HH]_ [)) +] _[ U]_ [(] _[W]_ [2][(] _[TH]_ [)) +] _[ U]_ [(] _[W]_ [2][(] _[HT]_ [)) +] _[ U]_ [(] _[W]_ [2][(] _[TT]_ [)))] _[ .]_


Furthermore, if _U_ ( _·_ ) is piecewise linear, then the problem can be recast as a
linear program. (See Exercise 16.1.)
Consider now the general multi-stage linear stochastic program (16.2). Suppose
each random vector _ωt_ = ( **c** _t,_ **A** _t,_ **B** _t,_ **b** _t_ ) has a discrete distribution and consider
their event tree representation. The description of the deterministic equivalent
relies on the following notation. Let


Ω _t_ := _{ωt_ _[k]_ [= (] **[c]** _t_ _[k][,]_ **[ A]** _t_ _[k][,]_ **[ B]** _t_ _[k][,]_ **[ b]** _t_ _[k]_ [) :] _[ k]_ [= 1] _[, . . ., S][t][}]_


be the set of possible realizations of the random variable _ωt_ for some integer _St_ _≥_
1 and for each stage _t_ = 1 _, . . ., T_ . Let _p_ _[k]_ _t_ [=] [P][(] _[ω][t]_ [=] _[ω]_ _t_ _[k]_ [),] [with] _[k]_ [=] [1] _[, . . ., S][t][,]_ _[t]_ [=]
1 _, . . ., T_ . The set Ω _t_ = _{ωt_ [1] _[, . . ., ω]_ _t_ _[S][t]_ _[}]_ [corresponds] [to] [the] [nodes] [in] [layer] _[t]_ [of] [the]
event tree, which can be conveniently denoted ( _t,_ 1) _, . . .,_ ( _t, St_ ) as illustrated in
Figure 16.3.



(2, 1)


(2, 2)


(2, 3)


(2, 4)


(2, 5)



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-264-0.png)





0 1 2 Stage


**Figure** **16.3** Event tree for a three-stage model with node labels


Observe that in the event tree there is always a single root node (0 _,_ 1) in layer 0.
Furthermore, for each _t_ = 1 _, . . ., T_ _−_ 1 each node ( _t, k_ ) has a _unique_ predecessor
( _t−_ 1 _,_ _k_ [ˆ] ) in the immediately preceding layer of the tree. For instance, in the event
tree depicted in Figure 16.3 the predecessors of each of the nodes in layer 2 is a
unique node in layer 1 as follows


ˆ1 = ˆ2 = 1 _,_ ˆ3 = ˆ4 = ˆ5 = 2 _._


Observe that the probability of a non-terminal node equals the combined probability of its direct descendants; that is, for _t_ = 1 _, . . ., T_ and for every node


( _t −_ 1 _, ℓ_ ) we have



**16.2** **Scenario** **Optimization** 253


  _p_ _[ℓ]_ _t−_ 1 [=] _p_ _[k]_ _t_ _[.]_

( _t,k_ ): _k_ [ˆ] = _ℓ_



Consider the multi-stage linear stochastic program (16.2) and assume the
random outcomes are described via a suitable event tree. We next detail the
variables, objective, and constraints of the corresponding deterministic linear
program equivalent.


**Variables:** Stage 0 variables: **x** 0.
Stage _t_ variables can be adapted to the _St_ possible paths up to stage
_t_ ; that is,


**x** _[k]_ _t_ _[,]_ _[k]_ [= 1] _[, . . ., S][t][.]_


**Objective:** The deterministic equivalent of the objective function








   -    min E **c** [T] 0 **[x]** [0] [+] **[ c]** [T] 1 **[x]** [1] [+] _[ · · ·]_ [ +] **[ c]** [T] _T_ **[x]** _[T]_ = min E







**c** [T] 0 **[x]** [0] [+]




- _T_

**c** [T] _t_ **[x]** _[t]_
_t_ =1



is




- _St_

_p_ _[k]_ _t_ [(] **[c]** _t_ _[k]_ [)][T] **[x]** _t_ _[k][.]_
_k_ =1



min **c** [T] 0 **[x]** [0] [+]




- _T_


_t_ =1



**Constraints:** The deterministic equivalent of each inter-temporal constraint


**B** _t_ **x** _t−_ 1 + **A** _t_ **x** _t_ = **b** _t,_ **x** _t_ _≥_ 0 _,_


is the set of constraints


**B** _[k]_ _t_ **[x]** _kt_ ˆ _−_ 1 [+] **[ A]** _t_ _[k]_ **[x]** _t_ _[k]_ [=] **[ b]** _[t][,]_ **[x]** _[k]_ _t_ _[≥]_ [0] _[,]_ [for] _[k]_ [= 1] _[, . . ., S][t][.]_


Observe that these constraints link the stage _t_ variables **x** _[k]_ _t_ [associated]
with the layer _t_ nodes ( _t, k_ ) with the variable associated with their
predecessor ( _t −_ 1 _,_ _k_ [ˆ] ).


Thus the complete deterministic equivalent of (16.2) is as follows:




- _ST_

_p_ _[k]_ _T_ [(] **[c]** _T_ _[k]_ [)][T] **[x]** _T_ _[k]_
_k_ =1



min _c_ [T] 0 **[x]** [0] [+]




- _S_ 1

_p_ _[k]_ 1 [(] **[c]** _[k]_ 1 [)][T] **[x]** _[k]_ 1 [+] _· · ·_ +
_k_ =1



(16.3)



s.t. **A** 0 **x** 0 = **b** 0
**B** _[k]_ 1 **[x]** [0] [+] **A** _[k]_ 1 **[x]** _[k]_ 1 = **b** _[k]_ 1 _[,]_ _[k]_ [= 1] _[, . . ., S]_ [1]
**B** _[k]_ 2 **[x]** 1 _[k]_ [ˆ] [+] **A** _[k]_ 2 **[x]** _[k]_ 2 = **b** 2 _,_ _k_ = 1 _, . . ., S_ 2
... ...
**B** _[k]_ _T_ **[x]** _T_ _[k]_ [ˆ] _−_ 1 [+] **A** _[k]_ _T_ **[x]** _T_ _[k]_ [=] **[ b]** _T_ _[k]_ _[,]_ _[k]_ [= 1] _[, . . ., S][T]_
**x** 0 _,_ **x** _[k]_ 1 _[,]_ _. . ._ **x** _[k]_ _T_ _[≥]_ [0] _[.]_


254 **Multi-Stage** **Stochastic** **Programming**


For example, if _T_ = 2 and the event tree is as depicted in Figure 16.3, then
the deterministic equivalent is


min **c** [T] 0 **[x]** 0 + _p_ [1] 1 [(] **[c]** [1] 1 [)][T] **[x]** [1] 1 + _p_ [2] 1 [(] **[c]** [2] 1 [)][T] **[x]** [2] 1 + _p_ [1] 2 [(] **[c]** [1] 2 [)][T] **[x]** [1] 2 + _p_ [2] 2 [(] **[c]** [2] 2 [)][T] **[x]** [2] 2 + _p_ [3] 2 [(] **[c]** [3] 2 [)][T] **[x]** [3] 2


+ _p_ [4] 2 [(] **[c]** [4] 2 [)][T] **[x]** [4] 2 + _p_ [5] 2 [(] **[c]** [5] 2 [)][T] **[x]** [5] 2


s.t. **A** 0 **x** 0 = **b** 0


**B** [1] 1 **[x]** 0 [+] **[A]** [1] 1 **[x]** [1] 1 = **b** [1] 1
**B** [2] 1 **[x]** 0 [+] **A** [2] 1 **[x]** [2] 1 = **b** [2] 1


**B** [1] 2 **[x]** [1] 1 + **A** [1] 2 **[x]** [1] 2 = **b** [1] 2
**B** [2] 2 **[x]** [1] 1 + **A** [2] 2 **[x]** [2] 2 = **b** [2] 2
**B** [3] 2 **[x]** [2] 1 [+] **A** [3] 2 **[x]** [3] 2 = **b** [3] 2
**B** [4] 2 **[x]** [2] 1 [+] **A** [4] 2 **[x]** [4] 2 = **b** [4] 2
**B** [5] 2 **[x]** [2] 1 [+] **A** [5] 2 **[x]** [5] 2 [=] **[ b]** 2 [5]


**x** 0 _,_ **x** [1] 1 _[,]_ **x** [2] 1 _[,]_ **x** [1] 2 _[,]_ **x** [2] 2 _[,]_ **x** [3] 2 _[,]_ **x** [4] 2 _[,]_ **x** [5] 2 _[≥]_ **[0]** _[.]_



Observe that the constraint matrix in the above model has the following
structure:
⎡ ⎤



⎤

⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦



⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣



**A** 0
**B** [1] 1 **A** [1] 1
**B** [2] 1 **A** [2] 1
**B** [1] 2 **A** [1] 2
**B** [2] 2 **A** [2] 2
**B** [3] 2 **A** [3] 2
**B** [4] 2 **A** [4] 2
**B** [5] 2 **A** [5] 2



_._



The constraint matrix for the general deterministic equivalent (16.3) has a similar
type of structure.
There are alternative ways of labeling the nodes and branches in the event
tree. In particular, the simple binary branching in Example 16.2 readily suggests
the natural edge labeling depicted in Figure 16.2. In that case the nodes in layer
_t_ can alternatively be labeled via the _t_ -long sequence of labels along the path
from the root node. This kind of edge labeling may appear more intuitive but
it could become cumbersome in other cases when there are different numbers of
branches at each non-terminal node.
Note that the size of the deterministic equivalent of a multi-stage stochastic
program increases rapidly with the number of stages. For example, for a problem
with 11 stages and a binary event tree, there are 2 [10] = 1024 scenarios and
therefore the linear program (16.3) may have several thousand constraints and
variables, depending on the number of variables and constraints at each node.
Modern commercial codes can handle such large linear programs, but a moderate
increase in the number of stages or in the number of branches at each stage could


**16.3** **Scenario** **Generation** 255


make (16.3) too large to solve by standard linear programming solvers. When
this happens, it is critical to exploit the special structure of (16.3) to solve the
model efficiently.
The Benders decomposition (or L-shaped method) introduced in Section 10.5
can also be used for multi-stage problems (16.3) in a straightforward way: The
stages are partitioned into a first set that gives rise to the “master problem”
and a second set that gives rise to the “recourse problems”. For example in a
six-stage problem, the variables of the first two stages could define the master
problem. When these variables are fixed, (16.3) decomposes into separate linear
programs each involving variables of the last four stages. The solutions of these
recourse linear programs provide optimality or feasibility cuts that can be added
to the master problem. As discussed in Section 10.5, upper and lower bounds
are computed at each iteration and the algorithm stops when the difference
drops below a given tolerance. Using this approach, Gondzio and Kouwenberg
(2001) were able to solve an asset liability management problem with over four
million scenarios, whose linear programming formulation (16.3) had 12 million
constraints and 24 million variables. This linear program was so large that storage
space on the computer became an issue. The scenario tree had six levels and
13 branches at each node. In order to apply Benders’ decomposition, Gondzio and
Kouwenberg divided the six-period problem into a first-stage problem containing
the first three periods and a second-stage problem containing periods four to six.
This resulted in 2197 recourse linear programs, each involving 2197 scenarios.
These recourse linear programs were solved by an interior-point algorithm. Note
that Benders’ decomposition is ideally suited for parallel computations since the
recourse linear programs can be solved simultaneously. When the solution of all
the recourse linear programs is completed (which takes the bulk of the time), the
master problem is then solved on one processor while the other processors remain
idle temporarily. Gondzio and Kouwenberg tested a parallel implementation on
a computer with 16 processors and they obtained an almost perfect speedup,
that is a speedup factor of almost _k_ when using _k_ processors.


**16.3** **Scenario** **Generation**


A key aspect of multi-stage stochastic programming is the generation of scenarios
so that the deterministic equivalent formulation (16.3) accurately represents the
underlying stochastic optimization problem.
There are two separate issues. First, one needs to model the correlation over
time among the random parameters. For a pension fund, such a model might
relate wage inflation (a random parameter that influences the liability side) to
interest rates and stock prices (random parameters that influence the asset side).
Below we discuss a simple autoregressive model that can be used for this purpose.
A second issue is the construction of a scenario tree from these inter-temporal
statistical models: A finite number of scenarios must reflect as accurately as


256 **Multi-Stage** **Stochastic** **Programming**


possible the random processes modeled in the previous step, suggesting the need
for a large number of scenarios. On the other hand, the linear program (16.3) can
only be solved if the size of the scenario tree is reasonable, suggesting a limited
number of scenarios. To reconcile these two conflicting objectives, it might be
crucial to use variance reduction techniques. We address these issues in this
section.


Autoregressive Model


In order to generate the random parameters underlying the stochastic program,
one needs to construct an economic model reflecting the correlation between the
parameters. Historical data may be available. The goal is to generate meaningful
time series for constructing the scenarios. One approach is to use an autoregressive model.
Specifically, if **r** _t_ denotes the random vector of parameters in period _t_, an
_autoregressive_ _model_ is defined by


**r** _t_ = **D** 0 + **D** 1 **r** _t−_ 1 + _· · ·_ + **D** _p_ **r** _t−p_ + _**ϵ**_ _t,_



where _p_ is the number of lags used in the regression, **D** 0 _,_ **D** 1 _, . . .,_ **D** _p_ are timeindependent constant matrices, which are estimated through statistical methods
such as maximum likelihood, and _**ϵ**_ _t_ is a vector of i.i.d. random disturbances
with mean zero.
To illustrate this, consider a problem where the vector **r** _t_ consists of three
random parameters: _st, bt_, and _mt_ are the rates of return of stocks, bonds, and
the money market, respectively, in year _t_ . An autoregressive model with _p_ = 1
has the form:
⎡ ⎤ ⎡ ⎤ ⎡ ⎤ ⎡ ⎤ ⎡ ⎤



⎡



⎡



⎡



_st−_ 1
⎣ _bt−_ 1
_mt−_ 1



⎦ +



⎡



⎤



⎤


⎦



⎤



⎤



_st_
⎣ _bt_
_mt_



⎤



⎦ =



_d_ 1
⎣ _d_ 2
_d_ 3



⎦ +



_d_ 11 _d_ 12 _d_ 13
⎣ _d_ 21 _d_ 22 _d_ 23
_d_ 31 _d_ 32 _d_ 33



_ϵ_ _[s]_ _t_
⎣ _ϵ_ _[b]_ _t_
_ϵ_ _[m]_ _t_



⎦ _,_ _t_ = 2 _, . . ., T._



Assuming independent error terms _ϵ_ _[s]_ _t_ [,] _[ϵ][b]_ _t_ [,] [and] _[ϵ][m]_ _t_ [,] [and] [using] [historical] [data,]
one can find the parameters _d_ 1, _d_ 11, _d_ 12, _d_ 13 in the first equation,


_st_ = _d_ 1 + _d_ 11 _st−_ 1 + _d_ 12 _bt−_ 1 + _d_ 13 _mt−_ 1 + _ϵ_ _[s]_ _t_ _[,]_


using standard linear regression tools that minimize the sum of squared errors
_ϵ_ _[s]_ _t_ [.] [Useful] [statistics,] [such] [as] [the] [standard] [error] _[σ][s]_ [of] [the] [estimates] _[s][t]_ [,] [can] [also]
be obtained. Similarly for _bt_ and _mt_ .


Constructing Scenario Trees


The random distributions relating the various parameters of a stochastic program must be discretized to generate a set of scenarios that is adequate for its
deterministic equivalent. Too few scenarios may lead to approximation errors.
On the other hand, too many scenarios will lead to an explosion in the size of


**16.3** **Scenario** **Generation** 257


the scenario tree, leading to an excessive computational burden. In this section,
we discuss a simple random sampling approach and two variance reduction techniques: adjusted random sampling and tree fitting. Unfortunately, scenario trees
constructed by these methods could contain spurious arbitrage opportunities.
We end this section with a procedure to test that this does not occur.


_Random_ _Sampling_
One can generate scenarios directly from the autoregressive model introduced in
the previous section:


**r** _t_ = **D** 0 + **D** 1 **r** _t−_ 1 + _· · ·_ + **D** _p_ **r** _t−p_ + _**ϵ**_ _t,_


where _ϵt_ _∼_ _N_ ( **0** _,_ Σ) are independently distributed multivariate normal distributions with mean 0 and covariance matrix Σ.
In our example with three random parameters _st_, _bt,_ and _mt_, and independent
error terms _ϵ_ _[s]_ _t_ [,] _[ϵ][b]_ _t_ [,] _[ϵ][m]_ _t_ [,] [the] [matrix] [Σ] [is] [a] [3] _[ ×]_ [ 3] [diagonal] [matrix,] [with] [diagonal]
entries _σs_, _σb_, _σm_ . Thirty branches or so may be needed to get a reasonable
approximation of the distribution of the rates of return in stage 1. For a problem
with three stages, 30 branches at each stage represent 27,000 scenarios. With
more stages, the size of the linear program (16.3) explodes. Kouwenberg (2001)
performed tests on scenario trees with fewer branches at each node (such as a
five-stage problem with branching structure 10–6–6–4–4, meaning ten branches
at the root, then six branches at each node in the next stage and so on) and
he concluded that random sampling on such trees leads to unstable investment
strategies. This occurs because the approximation error made by representing
parameter distributions by random samples can be significant in a small scenario tree. As a result the optimal solution of (16.3) is not optimal for the
actual parameter distributions. How can one construct a scenario tree that more
accurately represents these distributions, without blowing up the size of the
linear program (16.3)?


_Adjusted_ _Random_ _Sampling_
An easy way of improving upon random sampling is as follows. Assume that each
node of the scenario tree has an even number _K_ = 2 _k_ of branches. Instead of
generating 2 _k_ random samples from the autoregressive model, generate _k_ random
samples only and use the negative of their error terms to compute the values on
the remaining _k_ branches. This will fit all the odd moments of the distributions
correctly. In order to fit the variance of the distributions as well, one can scale
the sampled values. The sampled values are all scaled by a multiplicative factor
until their variance fits that of the corresponding parameter.


_Tree_ _Fitting_
How can one best approximate a continuous distribution by a discrete distribution with _K_ values? In other words, how should one choose values _vk_ and their
probabilities _pk_, for _k_ = 1 _, . . ., K_, in order to approximate the given distribution


258 **Multi-Stage** **Stochastic** **Programming**



as accurately as possible? A natural answer is to match as many of the moments
as possible. In the context of a scenario tree, the problem is somewhat more
complicated since there are several correlated parameters at each node and there
is interdependence between periods as well. Hoyland and Wallace (2001) propose
to formulate this fitting problem as a nonlinear program. The fitting problem
can be solved either at each node separately or on the overall tree. We explain
the fitting problem at a node. Let _Sl_ be the values of the statistical properties
of the distributions that one desires to fit, for _l_ = 1 _, . . ., s_ . These might be
the expected values of the distributions, the correlation matrix, the skewness,
and kurtosis. Let **v** _k_ and _pk_ denote the vector of values on branch _k_ and its
probability, respectively, for _k_ = 1 _, . . ., K_ . Let _fl_ ( **v** _,_ **p** ) be the mathematical
expression of property _l_ for the discrete distribution (for example, the mean
of the vectors **v** _k_, their correlation, skewness, and kurtosis). Each property has
a positive weight _wl_ indicating its importance in the desired fit. Hoyland and
Wallace formulate the fitting problem as







min
**v** _,_ **p**



_wl_ ( _fl_ ( **v** _,_ **p** ) _−_ _Sl_ ) [2]

_l_




 s.t.



_pk_ = 1

_k_



(16.4)



**p** _≥_ 0 _._


One might want some statistical properties to match exactly. As an example,
consider again the autoregressive model:


**r** _t_ = **D** 0 + **D** 1 **r** _t−_ 1 + _· · ·_ + **D** _p_ **r** _t−p_ + _**ϵ**_ _t,_


where _**ϵ**_ _t_ _∼_ _N_ ( **0** _,_ Σ) are independently distributed multivariate normal distributions with mean 0 and covariance matrix Σ. To simplify notation, let us write _**ϵ**_
instead of _**ϵ**_ _t_ . The random vector _**ϵ**_ has distribution _N_ ( **0** _,_ Σ) and we would like
to approximate this continuous distribution by a finite number of disturbance
vectors _**ϵ**_ _[k]_ occuring with probability _pk_, for _k_ = 1 _, . . ., K_ . Let _ϵ_ _[k]_ _q_ [denote] [the] _[q]_ [th]
component of vector _**ϵ**_ _[k]_ . One might want to fit the mean of _**ϵ**_ exactly and its
covariance matrix as well as possible. In this case, the fitting problem is



�2




- _l_


_r_ =1





 - _K_

_pkϵ_ _[k]_ _q_ _[ϵ][k]_ _r_ _[−]_ [Σ] _[qr]_
_k_ =1



min
_**ϵ**_ [1] _,...,_ _**ϵ**_ _[K]_ _,_ **p**


s.t.




- _l_


_q_ =1

- _K_



_pk_ _**ϵ**_ _[k]_ = **0**

_k_ =1







_pk_ = 1

_k_

**p** _≥_ 0 _._


_Arbitrage-Free_ _Scenario_ _Trees_
Approximating the continuous distributions of the uncertain parameters by a
finite number of scenarios in the linear program (16.3) typically creates modeling


**16.4** **Exercises** 259


errors. In fact, if the scenarios are not chosen properly or if their number is
too small, the supposed “linear programming equivalent” could be far from being
equivalent to the original stochastic optimization problem. One of the most
disturbing aspects of this phenomenon is the possibility of creating arbitrage
opportunities when constructing the scenario tree. When this occurs, model
(16.3) is flawed as it would be distorted by the arbitrage opportunities. Klaassen
(2002) was the first to address this issue. In particular, he shows how arbitrage
opportunities can be detected _ex_ _post_ in a scenario tree. See Exercise 16.3 for
details. When arbitrage opportunities exist, a simple solution is to discard the
scenario tree and to construct a new one with more branches. Klaassen also
discusses what constraints to add to the nonlinear program (16.4) in order to
preclude arbitrage opportunities _ex_ _ante_ . The additional constraints are nonlinear, thus increasing the difficulty of solving (16.4).


**16.4** **Exercises**


**Exercise** **16.1** Consider the following variation of the “financial planning”
problem discussed in Section 16.1:


_•_ Assume there are four stages, 0 through 3 (i.e., _T_ = 3).

_•_ Over each period we have two equally likely outcomes for joint returns of
bonds and stocks: (14%, 25%) and (10%, 6%).

_•_ Initial wealth _W_ 0 = 55. _L_ 1 = _L_ 2 = 0. Final liability _L_ 3 = 70.


(a) Use a multi-stage scenario optimization approach to determine the sequence
of investment decisions so that the liability is met at _T_ = 3, and the expected
value of the remaining wealth is maximized. Your investment decisions at
each stage must be non-anticipatory. That is, they can only depend on the
scenario path up to that stage.
(b) Modify your model to solve the following variation: Instead of the single
liability at stage 3, the following sequence of liabilities must be met at stages
1, 2, 3:


_L_ 1 = 20 _,_ _L_ 2 = 20 _,_ _L_ 3 = 25 _._


(c) Assume this time that _L_ 1 = _L_ 2 = 0 and that the final liability is _L_ 3 = 90.
Since this is too high, it is clear that, regardless of the investment decisions,
the final wealth _W_ 3 will be negative in some scenarios. Modify your model to
maximize instead E( _U_ ( _W_ 3)), where the utility function _U_ ( _W_ ) is as follows:

              _W_ if _W_ _≥_ 0
_U_ ( _W_ ) =
3 _W_ if _W_ _<_ 0 _._


It is preferable for your model to be a linear program for computational
purposes. For that purpose, you need to recast the objective


max E( _U_ ( _WT_ ))


260 **Multi-Stage** **Stochastic** **Programming**


so that the resulting model is a linear program. To do so, observe that
_U_ ( _W_ ) = min _{W,_ 3 _W_ _}_ and use a suitable set of new variables.


**Exercise** **16.2** Consider the following dynamic portfolio problem.


_•_ At time _t_ = 0 you have an initial endowment _W_ 0.

_•_ At time _t_ = 0 _,_ 1 _, . . ., T_ _−_ 1 you invest a fraction _xt_ of your wealth in a risky
asset and the remaining fraction 1 _−xt_ in a risk-free asset. The risk-free and
risky asset returns between _t_ and _t_ + 1 are _rf,t_ +1 and _rs,t_ +1 respectively.

_•_ At time _t_ = 1 _, . . ., T_ you receive an exogenous and deterministic income of _It_ .


Let _Wt_ denote your wealth at time _t_ = 0 _,_ 1 _, . . ., T_ . Your goal is to maximize
utility of final wealth E( _U_ ( _WT_ )).



(a) Write the law of motion for _Wt_ .
(b) Assume that between _t_ and _t_ + 1 there are two equally likely outcomes _H_
and _T_ . The risky return _rs,t_ +1 in each of these scenarios is as follows:

_•_ In outcome _H_ : _rs,t_ +1 = 0 _._ 5.

_•_ In outcome _T_ : _rs,t_ +1 = _−_ 0 _._ 4.
Assume a zero risk-free return, _rf,t_ +1 = 0, in both scenarios.
Suppose _T_ = 2. Write down the “law of motion” for _W_ 1 and _W_ 2 in each
relevant scenario using the above numerical values for _rf,t_ +1 _, rs,t_ +1.
(c) Assume _W_ 0 = 1 and _I_ 1 = _I_ 2 = 0 _._ 1. Use scenario optimization and Excel
Solver or MATLAB to solve the two-period portfolio optimization problem




_W_ 2 [1] _[−][γ]_
1 _−_ _γ_







max
_x_ 0 _,x_ 1 [E]



for _γ_ = 0 _._ 4 _,_ 0 _._ 7 _,_ 0 _._ 9.
(d) Repeat part (c) but this time assume _W_ 0 = 1 and _I_ 1 = _I_ 2 = 0.
(e) Repeat part (c) but this time assume _W_ 0 = 1 and _I_ 1 = _I_ 2 = 0 _._ 2.
(f) Can you infer anything from the numerical results in (c), (d), and (e) about
long-term investment when you know you will receive income along the
investment horizon?


**Exercise** **16.3** Recall from Section 4.2 in Chapter 4 that an arbitrage opportunity is an opportunity to make money without any cost and without any risk.
Consider a particular node at some stage _t −_ 1 _≥_ 0 in a scenario tree whose set
of immediate descendants in stage _t_ is _K_ . For each _k_ _∈_ _K_ let **r** _[k]_ _∈_ R _[n]_ denote the
vector of asset returns of a set of _n_ assets realized in branch _k_ between stages
_t −_ 1 and _t_ .


(a) Show that an arbitrage opportunity exists if there is an asset allocation

     -     **x** = _x_ 1 _· · ·_ _xn_ such that




- _n_

_xj_ _≤_ 0 _,_

_j_ =1




- _n_

( **r** _[k]_ ) [T] **x** _≥_ **0** _,_

_j_ =1



where at least one inequality is strict.


**16.4** **Exercises** 261


(b) Show that the condition in part (a) holds if and only if the following condition
does not hold: there exist _yk_ _>_ 0, for _k_ _∈_ _K_, such that

      
_yk_ **r** _[k]_ = **1** _._
_k∈K_


Hint: Apply the same kind of reasoning used in Section 4.2.
(c) Use part (a) and part (b) above to modify the nonlinear program (16.4) in
order to formulate a fitting problem at a node that does not contain any
arbitrage opportunities.


## 17 Stochastic Programming Models: Asset–Liability Management

**17.1** **Asset–Liability** **Management**


The financial health of any company, and in particular of financial institutions,
is reflected in the balance sheet of the company. Proper management of the
company requires attention to both sides of the balance sheet     - assets and
liabilities. _Asset–liability_ _management_ offers sophisticated mathematical tools
for an integrated management of assets and liabilities.
Asset–liability management recognizes that static, one-period investment planning models (such as mean–variance optimization) fail to incorporate the multiperiod nature of the liabilities faced by the company. A multi-period model that
emphasizes the need to meet liabilities in each period for a finite (or possibly
infinite) horizon is often required. Since liabilities and asset returns usually have
random components, their optimal management requires techniques to optimize
under uncertainty. In particular, stochastic programming approaches have been
effective for these kinds of problems.
The main components of the asset–liability management problem are the
stream of (random) liabilities faced by the firm, spread out over time, and the
(random) returns of the assets that the firm may use for investments. Positions
can be adjusted at each intermediate stage, adapting to the information revealed
up to that stage. This is closely related to the financial planning example presented in Example 16.1.
The model assumes a planning horizon of _T_ periods. Let _Ri,t_ denote the gross
return of asset _i_ between time _t −_ 1 and _t_, for _i_ = 1 _, . . ., n_ and _t_ = 1 _, . . ., T_ . Let
_Lt_ denote the liability at time _t_ = 1 _, . . ., T_ . Suppose we want to maximize the
expected wealth of the firm at time _T_ .


_Multi-stage_ _stochastic_ _programming_ _formulation_
**Variables:**
_xi,t_ : amount invested in asset _i_ at time _t_, for _i_ = 1 _, . . ., n_ and _t_ = 0 _,_ 1 _, . . ., T_ _−_ 1.


**Objective:**



**17.2** **The** **Case** **of** **an** **Insurance** **Company** 263


      


max E





- _n_



_Ri,T xi,T −_ 1 _−_ _LT_

_i_ =1




- _n_

_xi,t,_ for _t_ = 1 _, . . ., T_ _−_ 1

_i_ =1



s.t.




- _n_

_Ri,txi,t−_ 1 = _Lt_ +

_i_ =1



_xi,t_ _≥_ 0 _,_ for _i_ = 1 _, . . ., n,_ _t_ = 1 _, . . ., T_ _−_ 1 _._


The equality constraint in this formulation states that the surplus left after
liability _Lt_ is covered will be invested in the amounts _xi,t_ in asset _i_ for _i_ =
1 _, . . ., n_ .
The objective selected in the model above is to maximize the expected wealth
at the end of the planning horizon. In practice, one might have a different objective. For example, in some cases, minimizing value at risk (VaR) or conditional
value at risk (CVaR) might be more appropriate. Other priorities may dictate
other objective functions.
To address the issue of the most appropriate objective function, one must
understand the role of liabilities. Pension funds and insurance companies are
among the most typical arenas for the integrated management of assets and
liabilities.


**17.2** **The** **Case** **of** **an** **Insurance** **Company**


We consider the case of a Japanese insurance company, the Yasuda Fire and
Marine Insurance Co. Ltd., following the work of Cari˜no et al. (1994). In this case,
the liabilities are mainly savings-oriented policies issued by the company. Each
new policy sold represents a deposit, or inflow of funds. Interest is periodically
credited to the policy until maturity, typically three to five years, at which time
the principal amount plus credited interest is refunded to the policyholder. The
crediting rate is typically adjusted each year in relation to a market index like
the prime rate. Therefore, we cannot say with certainty what the future liabilities
will be. Insurance business regulations stipulate that interest credited to some
policies be earned from investment income, not capital gains. So, in addition
to ensuring that the maturity cash flows are met, the firm must seek to avoid
interim shortfalls in income earned versus interest credited. In fact, it is the risk
of not earning adequate income quarter by quarter that the decision makers view
as the primary component of risk at Yasuda.
The problem is to determine the optimal allocation of the deposited funds into
several asset categories: cash, fixed-rate and floating-rate loans, bonds, equities,
real estate, and other assets. Since we can revise the portfolio allocations over
time, the decision we make is not just among allocations today but among


264 **Stochastic** **Programming** **Models:** **Asset–Liability** **Management**


allocation strategies over time. A realistic dynamic asset–liability model must
also account for the payment of taxes. This is made possible by distinguishing
between interest income and price return.
A stochastic linear program is used to model the problem. The linear program
has uncertainty in many coefficients. This uncertainty is modeled through a finite
number of scenarios. In this fashion, the problem is transformed into a very
large-scale linear program of the form (16.3). The random elements include price
return and interest income for each asset class, as well as policy crediting rates.
We next describe the main components of the multi-stage stochastic programming model.


**Stages:** The stages of the model are indexed by _t_ = 0 _,_ 1 _, . . ., T_ .


**Variables:**


_xi,t_ = market value in asset _i_ at stage _t_ for _i_ = 1 _, . . ., n_ and _t_ = 0 _,_ 1 _, . . ., T_ .


_wt_ = interest income shortfall at stage for _t_ = 1 _, . . ., T_ .


_vt_ = interest income surplus at stage for _t_ = 1 _, . . ., T_ .


**Random** **parameters** **in** **the** **stochastic** **linear** **program:**


_RPi,t_ = price return of asset _i_ between stage _t_ _−_ 1 and stage _t_, for _i_ = 1 _, . . ., n_
and _t_ = 1 _, . . ., T._


_RIi,t_ = interest income of asset _i_ between stage _t −_ 1 and stage _t_, for _i_ =
1 _, . . ., n_ and _t_ = 1 _, . . ., T._


_Ft_ = deposit inflow between stage _t −_ 1 and stage _t_, for _t_ = 1 _, . . ., T._


_Pt_ = principal payout between stage _t −_ 1 and stage _t_, for _t_ = 1 _, . . ., T._


_It_ = interest payout between stage _t −_ 1 and stage _t_, for _t_ = 1 _, . . ., T._


_gt_ = rate at which interest is credited to policies between stage _t_ _−_ 1 and stage
_t_, for _t_ = 1 _, . . ., T._


_Lt_ = liability valuation at stage _t_ .


**Parameterized** **objective** **function** **components:**


_ct_ ( _·_ ) = piecewise linear convex penalty for shortfall at time _t_ .


The goal of the model is to allocate funds among available assets to maximize
expected wealth at the end of the planning horizon _T_ minus the expected penalized shortfall accumulated through the planning horizon. The problem can be


**17.3** **Option** **Pricing** **via** **Stochastic** **Programming** 265


formulated as the following multi-stage stochastic program:







max E





- _n_

_xi,T_ _−_

_i_ =1




- _T_

_ct_ ( _wt_ )

_t_ =1




- _n_




- _n_



s.t.



_xi,t −_ (1 + _RPi,t_ + _RIi,t_ ) _xi,t−_ 1 = _Ft −_ _Pt −_ _It_ for _t_ = 1 _, . . ., T_
_i_ =1 _i_ =1 asset accumulation

- _n_



_xi,t −_

_i_ =1



_RIi,txi,t−_ 1 + _wt −_ _vt_ = _gtLt−_ 1 for _t_ = 1 _, . . ., T_
_i_ =1 interest income shortfall
_Lt_ = (1 + _gt_ ) _Lt−_ 1 + _Ft −_ _Pt −_ _It_ for _t_ = 1 _, . . ., T_
liability accumulation
_xi,t_ _≥_ 0 _,_ _wt_ _≥_ 0 _,_ _vt_ _≥_ 0 _._ (17.1)



In the model discussed in Cari˜no et al. (1994), the stochastic linear program
(17.1) is converted into a large linear program using a finite number of scenarios
to deal with the random elements in the data. Creation of scenario inputs is
made in stages using a tree. The tree structure can be described by the number
of branches at each stage. For example, a 1–8–4–4–2–1 tree has 256 scenarios.
Stage _t_ = 0 is the initial stage. Stage _t_ = 1 may be chosen to be the end of
Quarter 1 and has eight different branches in this example. Stage _t_ = 2 may be
chosen to be the end of Year 1, with each of the previous eight branches giving rise
to four new branches, and so on. For the Yasuda Fire and Marine Insurance Co.
Ltd., a problem with seven asset classes and six stages gives rise to a stochastic
linear program (17.1) with 12 constraints (other than non-negativity) and 54
variables. Using 256 scenarios, this stochastic program is converted into a linear
program with several thousand constraints and over 10,000 variables. Solving
this model yielded extra income estimated to be about US $80 million per year
for the company.


**17.3** **Option** **Pricing** **via** **Stochastic** **Programming**


The option pricing problem discussed in Chapter 15 and modeled via the
binomial lattice can alternatively be formulated as a stochastic programming
problem. As should be expected, the two approaches are equivalent under the
assumptions made for the binomial lattice model. However, there is additional
flexibility in the stochastic programming approach that makes it applicable under
less restrictive assumptions. In particular, we will discuss how the stochastic
programming approach can easily model transaction costs. This is an important
practical issue that cannot be incorporated in the binomial lattice model.
We will work with the following similar setting to that in Chapter 15. Let _St_,
for _t_ = 0 _,_ 1 _, . . ., N,_ denote the share price of a risky asset at times _t_ = 0 _,_ 1 _, . . ., N_ .
Assume the economy also has a risk-free asset whose interest rate is _r_ in each
period [ _t −_ 1 _, t_ ] for _t_ = 1 _, . . ., N_ .


266 **Stochastic** **Programming** **Models:** **Asset–Liability** **Management**


European Options


Consider a European option contract that matures at time _N_ with payoff _g_ ( _SN_ )
for some function _g_ ( _·_ ) of the underlying asset price _SN_ . The following stochastic
program provides a model for the lowest-cost portfolio of the underlying asset
and the risk-free asset that can be constructed at time 0 and be subsequently
rebalanced to super-replicate the payoff _g_ ( _SN_ ) of the European option contract.


**Variables:**
_xt_ = amount of shares of the risky asset at time _t_ for _t_ = 0 _, . . ., N_ _−_ 1 _._
_yt_ = amount of money in the risk-free asset at time _t_ for _t_ = 0 _, . . ., N_ _−_ 1 _._


**Objective:**


min _S_ 0 _x_ 0 + _y_ 0
s.t. _SN_ _xN_ _−_ 1 + (1 + _r_ ) _yN_ _−_ 1 _≥_ _g_ ( _SN_ ) (17.2)
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _≥_ _Stxt_ + _yt,_ _t_ = 1 _, . . ., N_ _−_ 1 _._


Consider the following _binomial_ tree model for the risky prices. Assume that
there are exactly two possible random outcomes (“H” and “T”) between time
_t −_ 1 and _t_ for _t_ = 1 _, . . ., N_ . For the simplest case _N_ = 1, the binomial tree
model yields the following deterministic equivalent of (17.2):


min _S_ 0 _x_ 0 + _y_ 0
s.t. _S_ 1( _H_ ) _x_ 0 + (1 + _r_ ) _y_ 0 _≥_ _g_ ( _S_ 1( _H_ )) (17.3)
_S_ 1( _T_ ) _x_ 0 + (1 + _r_ ) _y_ 0 _≥_ _g_ ( _S_ 1( _T_ )) _._


Observe that the linear programming dual of (17.3) is



max _g_ ( _S_ 1( _H_ )) _v_ ( _H_ ) + _g_ ( _S_ 1( _T_ )) _v_ ( _T_ )
s.t. _S_ 1( _H_ ) _v_ ( _H_ ) + _S_ 1( _T_ ) _v_ ( _T_ ) = _S_ 0
(1 + _r_ ) _v_ ( _H_ ) + (1 + _r_ ) _v_ ( _T_ ) = 1
_v_ ( _H_ ) _, v_ ( _T_ ) _≥_ 0 _,_



(17.4)



which in turn can be rewritten via the change of variables _p_ ˜ := (1 + _r_ ) _v_ ( _H_ ) and
_q_ ˜ := (1 + _r_ ) _v_ ( _T_ ) as


1
max
1 + _r_ [(] _[g]_ [(] _[S]_ [1][(] _[H]_ [))˜] _[p]_ [ +] _[ g]_ [(] _[S]_ [1][(] _[T]_ [))˜] _[q]_ [)]



1
s.t.
1 + _r_ [(] _[S]_ [1][(] _[H]_ [)˜] _[p]_ [ +] _[ S]_ [1][(] _[T]_ [)˜] _[q]_ [) =] _[ S]_ [0]

_p_ ˜ + ˜ _q_ = 1
_p,_ ˜ ˜ _q_ _≥_ 0 _._



(17.5)



Without loss of generality assume _S_ 1( _H_ ) _≥_ _S_ 1( _T_ ). Furthermore, assume
_S_ 1( _H_ ) _>_ _S_ 1( _T_ ) as otherwise the pricing problem of the option contract is
trivial. It follows that (17.5) is feasible if and only if _S_ 1( _T_ ) _≤_ (1+ _r_ ) _S_ 0 _≤_ _S_ 1( _H_ ).
In this case the only feasible solution to (17.5) is



_p_ ˜ = [(1 +] _[ r]_ [)] _[S]_ [0] _[ −]_ _[S]_ [1][(] _[T]_ [)]




_[ r]_ [)] _[S]_ [0] _[ −]_ _[S]_ [1][(] _[T]_ [)]

_q_ ˜ = _[S]_ [1][(] _[H]_ [)] _[ −]_ [(1 +] _[ r]_ [)] _[S]_ [0]
_S_ 1( _H_ ) _−_ _S_ 1( _T_ ) _[,]_ _S_ 1( _H_ ) _−_ _S_ 1( _T_ )



_,_
_S_ 1( _H_ ) _−_ _S_ 1( _T_ )


**17.3** **Option** **Pricing** **via** **Stochastic** **Programming** 267


and thus the optimal value of (17.3) and (17.4) is


1
1 + _r_ [(˜] _[pg]_ [(] _[S]_ [1][(] _[H]_ [)) + ˜] _[qg]_ [(] _[S]_ [1][(] _[T]_ [)))] _[.]_


Observe that this price is exactly the same (as it should be) as the one obtained
via the one-period binomial model discussed in Section 4.3 when the singleperiod economy has no arbitrage. A similar duality argument shows that in the
absence of arbitrage the stochastic programming model (17.2) is equivalent to
the binomial lattice approach for the general multi-period case; that is, when
_N_ _>_ 1. The following example illustrates this equivalence.


**Example** **17.1** Suppose _n_ = 2 _,_ _r_ = [1] 4 _[,]_ [and] [the] [prices] _[S]_ [0] _[, S]_ [1] _[, S]_ [2] [of] [the] [risky]

asset are as indicated at the nodes of the binomial tree depicted in Figure 17.1.
Assume that the two branches emerging from each node are equally likely.
Determine the price of a European put option maturing at time _N_ = 2 with
strike price 50; that is, with payoff _g_ ( _S_ 2) = (50 _−_ _S_ 2) [+] _._
In this case the deterministic equivalent of (17.2) is


min 40 _x_ 0 + _y_ 0
s.t. 80 _x_ 0 + 1 _._ 25 _y_ 0 _≥_ 80 _x_ 1( _H_ ) + _y_ 1( _H_ )
20 _x_ 0 + 1 _._ 25 _y_ 0 _≥_ 20 _x_ 1( _T_ ) + _y_ 1( _T_ )
160 _x_ 1( _H_ ) + 1 _._ 25 _y_ 1( _H_ ) _≥_ (50 _−_ 160) [+] = 0
40 _x_ 1( _H_ ) + 1 _._ 25 _y_ 1( _H_ ) _≥_ (50 _−_ 40) [+] = 10
40 _x_ 1( _T_ ) + 1 _._ 25 _y_ 1( _T_ ) _≥_ (50 _−_ 40) [+] = 10
10 _x_ 1( _T_ ) + 1 _._ 25 _y_ 1( _T_ ) _≥_ (50 _−_ 10) [+] = 40 _._


The optimal solution to this linear program is


_x_ 1( _H_ ) = _−_ 0 _._ 0833 _,_ _y_ 1( _H_ ) = 10 _._ 6666 _,_ _x_ 1( _T_ ) = _−_ 1 _,_ _y_ 1( _T_ ) = 40 _,_ (17.6)

_x_ 0 = _−_ 0 _._ 2666 _,_ _y_ 0 = 20 _._ 2666


and thus its optimal value is 9 _._ 6.
On the other hand, the binomial lattice approach would yield the risk-neutral
probabilities _p_ ˜ = _q_ ˜ = [1] 2 [.] [Consequently,] [the] [value] _[V]_ [1][(] _[S]_ [1][)] [of] [the] [option] [at] [time] [1]

is



1
_V_ 1(80) = [0 + 10]
1 _._ 25 _[·]_ 2



1
= 4 _,_ _V_ 1(20) = [10 + 40]
2 1 _._ 25 _[·]_ 2



= 20;
2



and the value _V_ 0( _S_ 0) of the option at time 0 is


1
_V_ 0(40) = [4 + 20] = 9 _._ 6 _._
1 _._ 25 _[·]_ 2


The (super-)replicating portfolio (17.6) can also be recovered via delta-hedging.


American Options


Consider now an American option contract that can be exercised at any time _t_ =
0 _,_ 1 _, . . ., N_ with payoff _g_ ( _St_ ) for some function _g_ ( _·_ ) of the underlying asset price


268 **Stochastic** **Programming** **Models:** **Asset–Liability** **Management**



160


40


40


10





![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-280-0.png)



40





0 1 2 Stage


**Figure** **17.1** Binomial tree for option pricing example


_St_ . The stochastic program (17.2) has the following straightforward modification
for finding a lowest-cost portfolio of the underlying asset and the risk-free asset
that can be constructed at time 0 and be subsequently rebalanced to superreplicate the payoff of the American option contract:


min _S_ 0 _x_ 0 + _y_ 0
s.t. _SN_ _xN_ _−_ 1 + (1 + _r_ ) _yN_ _−_ 1 _≥_ _g_ ( _SN_ )
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _≥_ max _{Stxt_ + _yt, g_ ( _St_ ) _},_ _t_ = 1 _, . . ., N_ _−_ 1 _._


The latter problem in turn can be equivalently stated as follows:



min _S_ 0 _x_ 0 + _y_ 0
s.t. _SN_ _xN_ _−_ 1 + (1 + _r_ ) _yN_ _−_ 1 _≥_ _g_ ( _SN_ )
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _≥_ _Stxt_ + _yt,_ _t_ = 1 _, . . ., N_ _−_ 1
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _≥_ _g_ ( _St_ ) _,_ _t_ = 1 _, . . ., N_ _−_ 1 _._



(17.7)



Again for a binomial event tree model the above stochastic programming
approach is equivalent to the binomial lattice approach discussed in Chapter 15
in the absence of arbitrage.


Transaction Costs


The stochastic programming models (17.2) and (17.7) can be readily extended
to incorporate proportional transaction costs. Observe that in the absence of
transaction costs a transaction to sell _w_ shares of the risky asset when its price is
_S_ will generate a revenue equal to _wS_ . By contrast, if a proportional transaction
cost _θ_ applies to the sell transaction then the revenue would instead be (1 _−θ_ ) _wS_ .
Similarly, if a proportional transaction cost _θ_ applies to a buy transaction of _w_
shares, then the cost of the transaction would be (1 + _θ_ ) _wS._
The stochastic programming model (17.2) can be modified as follows to
account for a proportional transaction cost _θ_ applicable to each buy or sell


**17.3** **Option** **Pricing** **via** **Stochastic** **Programming** 269


transaction of the risky asset:


min _S_ 0 _x_ 0 + _θ|S_ 0 _x_ 0 _|_ + _y_ 0
s.t. _SN_ _xN_ _−_ 1 + (1 + _r_ ) _yN_ _−_ 1 _−_ _θ|SN_ _xN_ _−_ 1 _| ≥_ _g_ ( _SN_ )
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _−_ _θ|St_ ( _xt −_ _xt−_ 1) _| ≥_ _Stxt_ + _yt,_ _t_ = 1 _, . . ., N_ _−_ 1 _._
(17.8)

Similarly, the stochastic programming model (17.7) can also be modified to
account for the same kind of transaction costs as follows:


min _S_ 0 _x_ 0 + _θ|S_ 0 _x_ 0 _|_ + _y_ 0
s.t. _SN_ _xN_ _−_ 1 + (1 + _r_ ) _yN_ _−_ 1 _−_ _θ|SN_ _xN_ _−_ 1 _| ≥_ _g_ ( _SN_ )
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _−_ _θ|St_ ( _xt −_ _xt−_ 1) _| ≥_ _Stxt_ + _yt,_ _t_ = 1 _, . . ., N_ _−_ 1
_Stxt−_ 1 + (1 + _r_ ) _yt−_ 1 _−_ _θ|Stxt| ≥_ _g_ ( _St_ ) _,_ _t_ = 1 _, . . ., N_ _−_ 1 _._
(17.9)

Observe that the stochastic programs (17.9) and (17.8) include some term with
absolute values in the objective and constraints. The models can be recast as
linear stochastic programs by introducing some extra variables and constraints,
as the following example illustrates.


**Example** **17.2** Suppose _n_ = 2 _,_ _r_ = [1] 4 _[,]_ [and] [the] [prices] _[S]_ [0] _[, S]_ [1] _[, S]_ [2] [of] [the] [risky]

asset are as indicated at the nodes of the binomial tree depicted in Figure 17.1.
Assume that the two branches emerging from each node are equally likely.
Determine the price of a European put option maturing at time _N_ = 2 with
strike price 50; that is, with payoff _g_ ( _S_ 2) = (50 _−_ _S_ 2) [+] _._ Assume a proportional
transaction cost _θ_ applies to every buy or sell transaction.

In this case the deterministic equivalent of (17.8) is


min 40 _x_ 0 + _y_ 0 + 40 _θu_ 0
s.t. 80 _x_ 0 + 1 _._ 25 _y_ 0 _−_ 80 _θv_ 1( _H_ ) _≥_ 80 _x_ 1( _H_ ) + _y_ 1( _H_ )
20 _x_ 0 + 1 _._ 25 _y_ 0 _−_ 20 _θv_ 1( _T_ ) _≥_ 20 _x_ 1( _T_ ) + _y_ 1( _T_ )
160 _x_ 1( _H_ ) + 1 _._ 25 _y_ 1( _H_ ) _−_ 160 _θw_ 1( _H_ ) _≥_ (50 _−_ 160) [+] = 0
40 _x_ 1( _H_ ) + 1 _._ 25 _y_ 1( _H_ ) _−_ 40 _θw_ 1( _H_ ) _≥_ (50 _−_ 40) [+] = 10
40 _x_ 1( _T_ ) + 1 _._ 25 _y_ 1( _T_ ) _−_ 40 _θw_ 1( _T_ ) _≥_ (50 _−_ 40) [+] = 10
10 _x_ 1( _T_ ) + 1 _._ 25 _y_ 1( _T_ ) _−_ 10 _θw_ 1( _T_ ) _≥_ (50 _−_ 10) [+] = 40
_u_ 0 _≥_ _x_ 0 _,_ _u_ 0 _≥−x_ 0
_v_ 1( _H_ ) _≥_ _x_ 1( _H_ ) _−_ _x_ 0 _,_ _v_ 1( _T_ ) _≥−x_ 1( _T_ ) + _x_ 0
_w_ 1( _H_ ) _≥_ _x_ 1( _H_ ) _,_ _w_ 1( _H_ ) _≥−x_ 1( _H_ )
_w_ 1( _T_ ) _≥_ _x_ 1( _T_ ) _,_ _w_ 1( _T_ ) _≥−x_ 1( _T_ ) _._


Table 17.1 shows the optimal value and holdings _x_ 0 _, y_ 0 _, x_ 1( _H_ ) _, y_ 1( _H_ ) _, x_ 1( _T_ ) _, y_ 1( _T_ )
of the optimal super-replicating portfolio for various levels of transaction cost _θ_ .


270 **Stochastic** **Programming** **Models:** **Asset–Liability** **Management**


**Table** **17.1**


_θ_ Optimal value _x_ 0 _y_ 0 _x_ 1( _H_ ) _y_ 1( _H_ ) _x_ 1( _T_ ) _y_ 1( _T_ )


0 9.6 _−_ 0 _._ 26666 20.26666 _−_ 0 _._ 08333 10.66666 _−_ 1 40
0.01 9.93044 _−_ 0 _._ 26879 20.57443 _−_ 0 _._ 08251 10.66666 _−_ 0 _._ 9901 40
0.05 11.24337 _−_ 0 _._ 27546 21.71077 _−_ 0 _._ 07937 10.66666 _−_ 0 _._ 95238 40
0.1 12.84987 _−_ 0 _._ 28052 22.94857 _−_ 0 _._ 07576 10.66666 _−_ 0 _._ 90909 40


**17.4** **Synthetic** **Options**


An important issue in portfolio selection is the potential decline of the portfolio
value below some critical limit. How can we control the risk of downside losses? A
possible answer is to create a payoff structure similar to a European call option.
While a corporate investor may be able to construct a diversified portfolio,
there may be no option market available on this portfolio. One solution may be
to use index options. However, exchange-traded options with sufficient liquidity
are limited to maturities of about three months. This makes the cost of long-term
protection expensive, requiring the purchase of a series of highly priced shortterm options. For large institutional or corporate investors, a cheaper solution
is to artificially produce the desired payoff structure using available resources.
This is called a _synthetic_ _option_ _strategy_ . A model of this kind was proposed by
Zhao and Ziemba (2001) and can be described as follows.


**Problem** **parameters:**


_W_ 0 = investor’s initial wealth
_T_ = investor’s planning horizon
_R_ = gross return of a riskless asset for one period
_Ri,t_ = gross return for asset _i_ at time _t_
_θi,t_ = transaction cost for purchases and sales of asset _i_ at time _t_ .


The gross returns _Ri,t_ above are random, but their distributions are known.


**Variables:**


_xi,t_ = amount allocated to asset _i_ at time _t_
_Ai,t_ = amount of asset _i_ bought at time _t_
_Di,t_ = amount of asset _i_ sold at time _t_
_yt_ = amount allocated to riskless asset at time _t_ .


We formulate a stochastic program that produces the desired payoff at the
end of the planning horizon _T_, much in the flavor of the stochastic programs
developed in the previous section. Let us first discuss the constraints.
The initial portfolio must satisfy


_y_ 0 + _x_ 1 _,_ 0 + _. . ._ + _xn,_ 0 = _W_ 0 _._


**17.4** **Synthetic** **Options** 271


Similarly, the portfolio at time _t_ must satisfy



_xi,t_ = _Ri,txi,t−_ 1 + _Ai,t −_ _Di,t_ for _t_ = 1 _, . . ., T_




- _n_



_yt_ = _Ryt−_ 1 _−_




- _n_



(1 + _θi,t_ ) _Ai,t_ +

_i_ =1



(1 _−_ _θi,t_ ) _Di,t_ for _t_ = 1 _, . . ., T._

_i_ =1



One can also impose upper bounds on the proportion of any risky asset in the
portfolio:



⎛



⎞




- _n_

_xj,t_

_j_ =1



⎠ _,_



0 _≤_ _xi,t_ _≤_ _mt_



⎝ _yt_ +



where _mt_ is chosen by the investor.
The value of the portfolio at the end of the planning horizon is



_v_ = _RyT −_ 1 +




- _n_

(1 _−_ _θi,T_ ) _Ri,T xi,T −_ 1 _,_

_i_ =1



where the summation term is the value of the risky assets at time _T_ .
To construct the desired synthetic option, we split _v_ into the riskless value of
the portfolio _Z_ and a surplus _z_ _≥_ 0 which depends on random events. Using a
scenario approach to the stochastic program, _Z_ is the worst-case payoff over all
the scenarios. The surplus _z_ is a random variable that depends on the scenario.
Thus


_v_ = _Z_ + _z,_ _z_ _≥_ 0 _._


We consider _Z_ and _z_ as variables of the problem, and we optimize them
together with the asset allocations _x_ and other variables described earlier. The
objective function of the stochastic program is


max E( _z_ ) + _μZ,_


where _μ_ _≥_ 1 is the risk aversion of the investor. The risk aversion _μ_ is given
data. When _μ_ = 1, the objective is to maximize expected return. When _μ_ is very
large, the objective is to maximize “riskless profit”.


**Example** **17.3** Consider an investor with initial wealth _W_ 0 = 1 who wants to
construct a portfolio comprising one risky asset and one riskless asset using the
“synthetic option” model described above. We next describe the deterministic
equivalent of this model for a two-period planning horizon, i.e. _T_ = 2, and an
event tree with four scenarios. The construction is similar to that in Example
16.2. Suppose the return on the riskless asset is a non-random value _R_ per period
and there are two equally likely possible random outcomes (“ _H_ ” and “ _T_ ”) over
each time period. Let _Rt_ ( _H_ ) and _Rt_ ( _T_ ) denote the return of the risky asset
in the period [ _t −_ 1 _, t_ ] when the outcome is _H_ and _T_ respectively. Suppose the
transaction cost for purchases and sales of the risky asset is a non-random value _θ_ .


272 **Stochastic** **Programming** **Models:** **Asset–Liability** **Management**


The scenario tree in this case is identical to that depicted in Figure 16.1 for
Example 16.2. The deterministic equivalent of the multi-stage stochastic linear
program in this case is as follows:


max 14 [(] _[z]_ [(] _[HH]_ [) +] _[ z]_ [(] _[HT]_ [) +] _[ z]_ [(] _[TH]_ [) +] _[ z]_ [(] _[TT]_ [)) +] _[ μZ]_
s.t. _y_ 0 + _x_ 0 = 1
_x_ 1( _H_ ) = _R_ 1( _H_ ) _x_ 0 + _A_ 1( _H_ ) _−_ _D_ 1( _H_ )
_x_ 1( _T_ ) = _R_ 1( _T_ ) _x_ 0 + _A_ 1( _T_ ) _−_ _D_ 1( _T_ )
_y_ 1( _H_ ) = _Ry_ 0 _−_ (1 + _θ_ ) _A_ 1( _H_ ) + (1 _−_ _θ_ ) _D_ 1( _H_ )
_y_ 1( _T_ ) = _Ry_ 0 _−_ (1 + _θ_ ) _A_ 1( _T_ ) + (1 _−_ _θ_ ) _D_ 1( _T_ )
_z_ ( _HH_ ) + _Z_ = _Ry_ 1( _H_ ) + (1 _−_ _θ_ ) _R_ 2( _H_ ) _x_ 1( _H_ )
_z_ ( _HT_ ) + _Z_ = _Ry_ 1( _H_ ) + (1 _−_ _θ_ ) _R_ 2( _T_ ) _x_ 1( _H_ )
_z_ ( _TH_ ) + _Z_ = _Ry_ 1( _T_ ) + (1 _−_ _θ_ ) _R_ 2( _H_ ) _x_ 1( _T_ )
_z_ ( _TT_ ) + _Z_ = _Ry_ 1( _T_ ) + (1 _−_ _θ_ ) _R_ 2( _T_ ) _x_ 1( _T_ )
_x_ 0 _, y_ 0 _, x_ 1( _H_ ) _, x_ 1( _T_ ) _, y_ 1( _H_ ) _, y_ 1( _T_ ) _, A_ 1( _H_ ) _, D_ 1( _H_ ) _, A_ 1( _T_ ) _, A_ 2( _T_ ) _≥_ 0
_z_ ( _HH_ ) _, z_ ( _HT_ ) _, z_ ( _TH_ ) _, z_ ( _TT_ ) _≥_ 0
_Z_ free.


Zhao and Ziemba (2001) introduce and apply the above generic synthetic
option model to an example with three assets (cash, bonds, and stocks) and
four periods (a one-year horizon with quarterly portfolio reviews). The quarterly
return on cash is constant at _ρ_ = 0 _._ 0095. For stocks and bonds, the expected
logarithmic rates of returns are _s_ = 0 _._ 04 and _b_ = 0 _._ 019 respectively. Transaction
costs are assumed to be 0 _._ 5% for stocks and 0 _._ 1% for bonds. The scenarios needed
in the stochastic program are generated using an autoregression model which is
constructed based on historical data (quarterly returns from 1985 to 1998; the
Salomon Brothers bond index and S&P 500 index respectively). Specifically, the
autoregression model is


_st_ = 0 _._ 037 _−_ 0 _._ 193 _st−_ 1 + 0 _._ 418 _bt−_ 1 _−_ 0 _._ 172 _st−_ 2 + 0 _._ 517 _bt−_ 2 + _ϵt_
_bt_ = 0 _._ 007 _−_ 0 _._ 140 _st−_ 1 + 0 _._ 175 _bt−_ 1 _−_ 0 _._ 023 _st−_ 2 + 0 _._ 122 _bt−_ 2 + _ηt,_


where the pair ( _ϵt, ηt_ ) characterizes uncertainty. Zhao and Ziemba used a random
sampling approach to estimate the joint distribution of ( _ϵt, ηt_ ). From this joint
distribution of ( _ϵt, ηt_ ) a set of 20 pairs can be selected to estimate the empirical
distribution of ( _ϵt, ηt_ ). In this way, a scenario tree with 160,000 (= 20 _×_ 20 _×_
20 _×_ 20) paths describing possible outcomes of asset returns is generated for the
four periods.
The authors solved the resulting large deterministic linear program. We discuss
some of the results obtained when this linear program is solved for a risk aversion
of _μ_ = 2 _._ 5. The value of the terminal portfolio is always at least 4 _._ 6% more than
the initial portfolio wealth and the distribution of terminal portfolio values is
skewed to larger values because of dynamic downside risk control. The expected
return is 16 _._ 33% and the volatility is 7 _._ 2%. It is interesting to compare these
values with those obtained from a static Markowitz model. The expected return
is 15 _._ 4% for the same volatility but no minimum return is guaranteed. In fact,


**17.5** **Exercises** 273


in some scenarios, the value of the Markowitz portfolio is 5% _less_ at the end of
the one-year horizon than it was at the beginning.
It is also interesting to look at a typical portfolio (one of the 160,000 paths)
generated by the synthetic option model (the linear program was set up with an
upper bound of 70% placed on the fraction of stocks or bonds in the portfolio).


Portfolio value at

Quarter _t_ Cash Stocks Bonds the end of Quarter _t_

1 12% 18% 70% 103

2 41% 59% 107

3 70% 30% 112

4 30% 70% 114


**17.5** **Exercises**


**Exercise** **17.1** For a non-dividend paying stock, collect data on four or five
call options for the nearest maturity (but at least one month). Calculate the
_implied_ _volatility_ for each option; that is, the value of _σ_ that makes equation
(15.7) hold for the market prices of the call options. Solve the option pricing
problem (17.7) when the number of stages is seven using the implied volatility
of the at-the-money option to construct the tree.


**Exercise** **17.2** Repeat Exercise 17.1 allowing for transaction costs, with different values of _θ_, to see if the volatility smile can be explained by transaction
costs. Specifically, given a value for _σ_ and for _θ_, calculate option prices and see
how they match up to observed prices. Try _θ_ = 0 _._ 001, 0 _._ 005, 0 _._ 01, 0 _._ 02, 0 _._ 05.


**Exercise** **17.3** Develop a synthetic option model in the spirit of that used by
Zhao and Ziemba (2001), adapted to the size limitation of your linear programming solver. Compare with a static model.


## **Part IV** **Other Optimization** **Techniques**


## 18 Conic Programming: Theory and Algorithms

Conic programming refers to a class of convex optimization problems that generalizes linear and quadratic programming. The gist of conic programming is to
replace the non-negativity constraint with a _conic_ constraint.


**18.1** **Conic** **Programming**


A _conic_ _program_ in standard form is an optimization problem of the form


min **c** [T] **x**
**x**

s.t. **Ax** = **b** (18.1)
**Dx** _−_ **d** _∈K_


for some vectors and matrices **c** _∈_ R _[n]_, **b** _∈_ R _[m]_, **d** _∈_ R _[p]_, **A** _∈_ R _[m][×][n]_, **D** _∈_ R _[p][×][n]_

and some closed convex cone _K ⊆_ R _[p]_ .
When _K_ = R _[p]_ + [the] [problem] [(18.1)] [is] [a] [linear] [program.] [However,] [conic] [pro-]
gramming is far more general. We next discuss two particularly important classes
of conic programs, namely _second-order_ and _semidefinite_ programming.


18.1.1 Second-Order Programming



The _second-order_ cone, also known as the _Lorenz_ cone or the _ice-cream_ cone, is
defined as follows:





_._




  -  L _n_ = **x** = _x_ **x** ¯0




_∈_ R _[n]_ : _∥_ **x** ¯ _∥_ 2 _≤_ _x_ 0



See Figure 18.1.
A _second-order_ _program_ is a problem of the form (18.1) where _K_ is a direct
product of second-order cones; that is,


_K_ = L _n_ 1 _× · · · ×_ L _nr_


for some positive integers _n_ 1 _, . . ., nr_ .
We next illustrate the modeling power of second-order programming by showing that a convex quadratically constrained quadratic program can be recast
as a second-order program. In particular, second-order programming generalizes
both linear programming and convex quadratic programming.


278 **Conic** **Programming:** **Theory** **and** **Algorithms**


{( _x_ 1, _x_ 2, _x_ 3): _x_ 1 ≥ ||( _x_ 2, _x_ 3)||}


1


0.8


0.6


0.4


0.2


0
1



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-290-0.png)



1













−1



_x_ 3



_x_ 2


**Figure** **18.1** Second-order cone



−1



Consider a convex quadratically constrained quadratic program of the form



min **x** **c** [T] 0 **[x]** [ +] [1] 2

s.t. **c** [T] _i_ **[x]** [ +] [1] 2




[1]

2 **[x]** [T] **[Q]** [0] **[x]**



(18.2)

[1] 2 **[x]** [T] **[Q]** _[i]_ **[x]** _[ ≤]_ _[b][i][,]_ _[i]_ [ = 1] _[, . . ., m,]_



where **c** _i_ _∈_ R _[n]_, **Q** _i_ _∈_ S _[n]_ + [for] _[i]_ [ = 0] _[,]_ [ 1] _[, . . ., m]_ [and] _[b][i]_ _[∈]_ [R] [for] _[i]_ [ = 1] _[, . . ., m.]_ [Here] [S] _[n]_ +
denotes the family of _n × n_ positive semidefinite matrices.
Observe that (18.2) can be rewritten as


min _t_
**x** _,t_



s.t. **c** [T] 0 **[x]** [ +] [1] 2 **[x]** [T] **[Q]** [0] **[x]** _[ ≤]_ _[t]_



(18.3)



**c** [T] _i_ **[x]** [ +] [1] 2 **[x]** [T] **[Q]** _[i]_ **[x]** _[ ≤]_ _[b][i][,]_ _[i]_ [ = 1] _[, . . ., m.]_


The following step is key in the formulation of (18.2) as a second-order program:
given **Q** _∈_ S _[n]_ + [,] **[c]** _[ ∈]_ [R] _[n]_ [,] _[b][ ∈]_ [R] [the] [quadratic] [inequality]


**c** [T] **x** + [1] 2 **[x]** [T] **[Qx]** _[ ≤]_ _[b]_


can be formulated as a second-order cone constraint. To see that, observe that
because **Q** _∈_ S _[n]_ + [there] [exists] **[L]** _[∈]_ [R] _[n][×][p]_ [such] [that] **[Q]** [=] **[LL]** [T] [(in] [particular] [the]
Cholesky factorization satisfies this requirement). Therefore



⎡



⎤



_b −_ **c** [T] **x** + 1
⎣ _b −_ **c** [T] **x** _−_ 1
_√_



2 **L** [T] **x**



**c** [T] **x** + [1]




[1] 2 **[x]** [T] **[Qx]** _[ ≤]_ _[b]_ _⇔_ **c** [T] **x** + [1] 2




[1] 2 _[∥]_ **[L]** [T] **[x]** _[∥]_ [2] _[≤]_ _[b]_ _⇔_



⎦ _∈_ L _p_ +2 _._



It thus follows that (18.3) and in turn (18.2) can be rewritten as the following


second-order program:



min _t_
**x** _,t_



⎡



**18.1** **Conic** **Programming** 279


⎤


⎦ _∈_ L _p_ 0+2



s.t.



_t −_ **c** [T] 0 **[x]** [ + 1]
⎣ _t −√_ **c** [T] 0 **[x]** _[ −]_ [1]



2 **L** [T] 0 **[x]**



⎡



_bi −_ **c** [T] _i_ **[x]** [ + 1]
⎣ _bi −√_ **c** [T] _i_ **[x]** _[ −]_ [1]



⎤


⎦ _∈_ L _pi_ +2 _,_ _i_ = 1 _, . . ., m,_



2 **L** [T] _i_ **[x]**



where **L** _i_ _∈_ R _[n][×][p][i]_ such that **Q** _i_ = **L** _i_ **L** [T] _i_ [for] _[i]_ [ = 0] _[,]_ [ 1] _[, . . ., m.]_


Tracking Error and Volatility Constraints


In the context of quantitative asset management, portfolios are typically chosen
relative to some predetermined benchmark, as we discussed in Section 6.5. As a
consequence, it is common to use a constraint on the active risk (also known as
tracking error) instead of, or in addition to, the total risk.
More precisely, suppose **x** denotes the vector of percentage holdings in a
portfolio. Let **r** and _rB_ denote respectively the vector of asset returns and the
benchmark return. Recall that the active return is the difference **r** [T] **x** _−rB_ between
the portfolio return and the benchmark return. The active risk is the variance
of the active return. If **x** _[B]_ denotes the vector of percentage holdings in the
benchmark, then the active risk can be written as


var( **r** [T] ( **x** _−_ **x** _[B]_ )) = ( **x** _−_ **x** _[B]_ ) [T] **V** ( **x** _−_ **x** _[B]_ ) _,_


where **V** is the covariance matrix of asset returns.
A typical mean–variance model for benchmark-relative portfolio management
has the following form:



max _**α**_ [T] **x**
**x**

s.t. ( **x** _−_ **x** _[B]_ ) [T] **V** ( **x** _−_ **x** _[B]_ ) _≤_ _ψ_ [¯][2]

**Ax** = **b**
**Cx** _≤_ **d** _._



(18.4)



Note that this is not a quadratic program because it has a nonlinear constraint.
However, the problem (18.4) is a convex quadratically constrained quadratic
program of the form (18.2) discussed in Section 18.1.1. Therefore, it has a
straightforward formulation as a second-order conic program.
The above model can be readily extended to include multiple measures of
risk. For instance, the following model, which is an extension of the model discussed by Jorion (2003) that enforces upper bound constraints on both total risk
and tracking error, also has a straightforward second-order conic programming


280 **Conic** **Programming:** **Theory** **and** **Algorithms**


formulation:
max _**α**_ [T] **x**
**x**

s.t. ( **x** _−_ **x** _[B]_ ) [T] **V** ( **x** _−_ **x** _[B]_ ) _≤_ _ψ_ [¯][2]

**x** [T] **Vx** _≤_ _σ_ ¯ [2]

**Ax** = **b**
**Cx** _≤_ **d** _._


18.1.2 Semidefinite Programming



(18.5)



Some applications, such as the approximation of covariance matrices discussed
below, lead to conic optimization models involving the space of symmetric matrices and the cone of positive semidefinite matrices described next. Let S _[n]_ denote
the space of _n_ _×_ _n_ symmetric matrices. Although this space is equivalent to
R _[n]_ [(] _[n]_ [+1)] _[/]_ [2], it is more convenient and customary to treat it as a space of matrices.
A matrix **X** _∈_ S _[n]_ is _positive_ _semidefinite_ if


**u** [T] **Xu** _≥_ 0 for all **u** _∈_ R _[n]_ _._


It is a common convention to write **X** _⪰_ **0** to indicate that **X** _∈_ S _[n]_ is positive
semidefinite. The cone of positive semidefinite matrices S _[n]_ + [is] [defined] [as]

S _[n]_ + [:=] _[ {]_ **[X]** _[ ∈]_ [S] _[n]_ [:] **[ X]** _[ ⪰]_ **[0]** _[}][.]_


See Figure 18.2.


_X_ =[ _X_ 11 _X_ 12; _X_ 21 _X_ 22] positive semidefinite


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



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-292-0.png)



0



1

0

_X_ 11



_X_ 22



**Figure** **18.2** Cone of positive semidefinite matrices


A _semidefinite_ _program_ is a problem of the form (18.1) where _K_ is the cone of
positive semidefinite matrices.


**18.1** **Conic** **Programming** 281


Endow the space S _[n]_ of symmetric _n × n_ matrices with the following _Frobenius_
_inner_ _product_ . For **X** _,_ **S** _∈_ S _[n]_ let

       **X** _•_ **S** := trace( **XS** ) = _XijSij._


_i,j_


A semidefinite program is in _standard_ _form_ if it is written as


min **C** _•_ **X**
**X**

s.t. **AX** = **b**
**X** _⪰_ **0** _,_


where **C** _∈_ S _[n]_, **b** _∈_ R _[m]_ _,_ and **A** : S _[n]_ _→_ R _[m]_ is a linear mapping.


Approximating Covariance Matrices


We next illustrate the modeling power of semidefinite programming by showing
that a covariance estimation problem can be recast as a semidefinite program.
To that end, recall that any proper covariance matrix must be symmetric and
positive semidefinite. Suppose **V** [ˆ] _∈_ S _[n]_ is an estimate of a covariance matrix that
is not necessarily positive semidefinite and consider the problem of finding the
positive semidefinite matrix that is closest to **V** [ˆ] ; that is,


min _∥_ **X** _−_ **V** [ˆ] _∥_
**X** (18.6)

s.t. **X** _⪰_ **0** _._


This problem can be formulated as


min _t_
**X** _,t_

s.t. _∥_ **X** _−_ **V** [ˆ] _∥≤_ _t_
**X** _⪰_ **0** _._


If the norm _∥_ **X** _−_ **V** [ˆ] _∥_ is the Frobenius norm


         
~~�~~
_∥_ **X** _−_ **V** [ˆ] _∥F_ := ( _Xij_ _−_ _V_ [ˆ] _ij_ ) [2] _,_


_i,j_


then the constraint _∥_ **X** _−_ **V** [ˆ] _∥F_ _≤_ _t_ can be written as a second-order cone
constraint and it follows that the above covariance estimation problem (18.6)
can be written as a conic program over the Cartesian product of a second-order
cone and a semidefinite cone. As we detail in the exercises at the end of this
chapter, problem (18.6) can also be formulated as a conic program over a suitable
semidefinite cone for other choices of norms such as the operator norm or the
infinity norm.


282 **Conic** **Programming:** **Theory** **and** **Algorithms**


**18.2** **Numerical** **Conic** **Programming** **Solvers**


During the last three decades there have been major advancements in the theory,
algorithms, and software for conic programming. In particular, the software
packages SeDuMi and SDPT3 are MATLAB-based, freely available solvers for conic
programs. The commercial software vendors Gurobi and MOSEK also offer solvers
for conic programs. These solvers constitute the engine behind the MATLAB
modeling language CVX that we have discussed in previous chapters.
Both SeDuMi and SDPT3 as well as most other software packages are designed
to solve a conic program in the following _standard_ form:


min **c** [T] **x**
**x**

s.t. **Ax** = **b**
**x** _∈K,_


where the cone _K_ is a Cartesian product of the form R _[f]_ _×_ R _[ℓ]_ + _[×]_ [ L] _[n]_ 1 _[× · · · ×]_
L _nr ×_ S _[d]_ + [1] _[×· · ·×]_ [S] + _[d][k]_ [. In other words, the conic constraint] **[ x]** _[ ∈K]_ [models a vector]
**x** that has a block of _f_ free components, followed by a block of _ℓ_ non-negative
components, followed by _r_ blocks of second-order cone-constrained components,
and finally followed by _k_ blocks of semidefinite-constrained components. The
package SeDuMi uses the following syntax:


>> [x,y,info] = sedumi(A,b,c,K) ;


Here K is a MATLAB structure with fields K.f, K.l, K.q, K.s detailing the
dimensions of the above blocks. The matrix and vectors A, b, c should be of the
appropriate dimensions.
The package SDPT3 uses a similar syntax. It should be noted that although
the process of formatting a particular problem in the appropriate SeDuMi or
SDPT3 format is relatively routine, the particular details and steps could in some
cases introduce errors. The modeling environment provided by CVX performs that
formatting in an automated fashion.


**18.3** **Duality** **and** **Optimality** **Conditions**


As in linear and quadratic programming, there is a _dual_ conic program associated
with every _primal_ conic program. The construction of the dual conic program
relies on the following more fundamental construction. Let _K_ _⊆_ R _[p]_ be a closed
convex cone. The dual cone _K_ _[∗]_ _⊆_ R _[p]_ of _K_ is defined as


_K_ _[∗]_ := _{_ **s** _∈_ R _[p]_ : **s** [T] **x** _≥_ 0 for all **x** _∈K}._


It is easy to see that _K_ _[∗]_ _⊆_ R _[p]_ is also a closed convex cone.
Just as we did for linear and quadratic programming, the dual problem can
be derived via the following _Lagrangian_ _function_ associated with (18.1):


_L_ ( **x** _,_ **y** _,_ **s** ) := **c** [T] **x** + **y** [T] ( **b** _−_ **Ax** ) + **s** [T] ( **d** _−_ **Dx** ) _._


**18.3** **Duality** **and** **Optimality** **Conditions** 283


The constraints of (18.1) can be encoded via the Lagrangian function. For a
given vector **x**

        **c** T **x** if **Ax** = **b** and **Dx** _−_ **d** _∈K_
max **s** _∈K_ **y** _,_ **s** _[∗]_ _L_ ( **x** _,_ **y** _,_ **s** ) = + _∞_ otherwise.


Therefore the primal problem (18.1) can be written as


min **x** max **y** _,_ **s** _L_ ( **x** _,_ **y** _,_ **s** ) _._
**s** _∈K_ _[∗]_


The dual problem is obtained by flipping the order of the min and max operations:


max **s** _∈K_ **y** _,_ **s** _[∗]_ min **x** _[L]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ s]** [)] _[.]_


It is easy to see that the dual problem can be written as follows:


max **b** [T] **y** + **d** [T] **s**
**y** _,_ **s**



s.t. **A** [T] **y** + **D** [T] **s** = **c**
**s** _∈K_ _[∗]_ _._


In particular, when the primal problem is in the following _standard_ _form_,


min **c** [T] **x**
**x**

s.t. **Ax** = **b**
**x** _∈K,_


the dual problem is


max **b** [T] **y**
**y** _,_ **s**

s.t. **A** [T] **y** + **s** = **c**
**s** _∈K_ _[∗]_ _._



(18.7)



Observe that the dual problem of a conic program is again a conic program.
As in linear and quadratic programming, there is a deep connection between
the primal problem (18.1) and its dual (18.7). The following result follows by
construction.


**Theorem** **18.1** (Weak duality) _Assume_ **x** _is_ _a_ _feasible_ _point_ _for_ (18.1) _and_
( **y** _,_ **s** ) _is_ _a_ _feasible_ _point_ _for_ (18.7) _._ _Then_


**b** [T] **y** + **d** [T] **s** _≤_ **c** [T] **x** _._


_Proof_ If **x** and ( **y** _,_ **s** ) satisfy the above assumptions then


**b** [T] **y** + **d** [T] **s** _≤_ ( **Ax** ) [T] **y** + ( **Dx** ) [T] **s**

= ( **A** [T] **y** + **D** [T] **s** ) [T] **x**

= **c** [T] **x** _._


284 **Conic** **Programming:** **Theory** **and** **Algorithms**


In contrast to linear and quadratic programming, strong duality does not
always hold for conic programming. Fortunately, strong duality holds under a
mild regularity assumption. The conic program (18.1) satisfies the _Slater_ condition if there exists **x** _∈_ R _[n]_ such that


**Ax** = **b** _,_ **Dx** _−_ **d** _∈_ relint( _K_ ) _,_


where relint( _K_ ) denotes the relative interior of the set _K_ .
Similarly, the conic program (18.7) satisfies the _Slater_ condition if there exists
**y** _∈_ R _[m]_ and **s** _∈_ relint( _K_ _[∗]_ ) such that


**A** [T] **y** + **D** [T] **s** = **c** _._


**Theorem** **18.2** (Strong duality) _Suppose_ _the_ _problems_ (18.1) _and_ (18.7) _satisfy_
_the Slater condition. Then both problems have optimal solutions and their optimal_
_values_ _are_ _the_ _same._


We refer the reader to G¨uler (2010) or Renegar (2001) for a proof of Theorem
18.2. The following characterization of the solutions to both (18.1) and (18.7)
readily follows from Theorem 18.1 and Theorem 18.2.


**Theorem** **18.3** (Optimality conditions) _The_ _vectors_ **x** _∈_ R _[n]_ _and_ ( **y** _,_ **s** ) _∈_ R _[m]_ _×_
R _[n]_ _are_ _optimal_ _solutions_ _to_ (18.1) _and_ (18.7) _respectively_ _if_



**c** _−_ **A** [T] **y** _−_ **D** [T] **s** = **0**
**Ax** _−_ **b** = **0**
**Dx** _−_ **d** _∈K_
**s** _∈K_ _[∗]_

**s** [T] ( **Dx** _−_ **d** ) = 0 _._



(18.8)



_The_ _following_ _partial_ _converse_ _also_ _holds:_ _if_ (18.1) _and_ (18.7) _satisfy_ _the_ _Slater_
_condition_ _then_ _they_ _both_ _have_ _optimal_ _solutions_ **x** _and_ ( **y** _,_ **s** ) _that_ _satisfy_ (18.8) _._


For a conic program in standard form, the optimality conditions (18.8) can be
written as follows:
**A** [T] **y** + **s** = **c**
**Ax** = **b**
**x** _∈K_ (18.9)
**s** _∈K_ _[∗]_

**s** [T] **x** = 0 _._


**18.4** **Algorithms**


By relying on the structure of the cone _K_, the main algorithmic template of
interior-point methods, such as the one described in Chapter 2 and in Chapter
5, can be extended to a larger class of conic programs. The central idea is to
generate a sequence of points that converges to a solution to (18.9). We next


**18.4** **Algorithms** 285


sketch the gist of interior-point methods for semidefinite programming. For a
full and in-depth treatment of this interesting material we refer the reader to the
seminal articles by Nesterov and Todd (1997, 1998) and Schmieta and Alizadeh
(2001, 2003) and the textbooks by Nesterov (2004), Nesterov and Nemirovskii
(1994), and Renegar (2001).
For convenience of exposition, we consider a semidefinite program in standard
form:
min **C** _•_ **X**
**X**

s.t. **AX** = **b** (18.10)
**X** _⪰_ **0** _,_


where **C** _∈_ S _[n]_, **b** _∈_ R _[m]_ _,_ and **A** : S _[n]_ _→_ R _[m]_ is a linear mapping. As the exercises
at the end of this chapter detail, the dual of (18.10) is the semidefinite program


min **b** [T] **y**
**y** _,_ **S**



s.t. **A** _[∗]_ **y** + **S** = **C**
**S** _⪰_ **0** _,_



(18.11)



where **A** _[∗]_ : R _[m]_ _→_ S _[n]_ denotes the _adjoint_ of **A** ; that is, the unique linear mapping
satisfying


( **AX** ) [T] **y** = **X** _•_ **A** _[∗]_ **y**


for all **X** _∈_ S _[n]_ and all **y** _∈_ R _[m]_ .
We will rely on the following key property of positive semidefinite matrices:


**X** _,_ **S** _∈_ S _[n]_ + [and] **[X]** _[ •]_ **[ S]** [ = 0] _⇒_ **XS** = **0** _._ (18.12)


From Theorem 18.3 and (18.12) it follows that **X** and ( **y** _,_ **S** ) are optimal solutions
to (18.10) and (18.11) respectively if



**A** _[∗]_ **y** + **S** = **C**
**AX** = **b**
**XS** = **0**
**X** _,_ **S** _⪰_ **0** _._



(18.13)



As in the linear programming case, interior-point methods for semidefinite programming generate a sequence of iterates that satisfy **X** _,_ **S** _≻_ **0** . Each iteration of
the algorithm aims to make progress towards satisfying **A** _[∗]_ **y** + **S** = **C**, **AX** = **b**,
and **XS** = **0** _._
Given _μ >_ 0, let ( **X** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **S** ( _μ_ )) be the solution to the following perturbed
version of the above optimality conditions:
⎡ ⎤ ⎡ ⎤



⎤



⎡



⎤



**A** _[∗]_ **y** + **S** _−_ **C**
⎣ **AX** _−_ **b**
**XS**



⎦ =



**0**
⎣ **0**
_μ_ **I**



⎦ _,_ **X** _,_ **S** _≻_ **0** _._



The first condition above can be written as **r** _μ_ ( **X** _,_ **y** _,_ **S** ) = **0** for the _residual_


286 **Conic** **Programming:** **Theory** **and** **Algorithms**


_vector_ :



⎤


⎦ _._



**r** _μ_ ( **X** _,_ **y** _,_ **S** ) :=



⎡

**A** _[∗]_ **y** + **S** _−_ **C**
⎣ **AX** _−_ **b**
**XS** _−_ _μ_ **I**



The _central_ _path_ is the set _{_ ( **X** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **S** ( _μ_ )) : _μ_ _>_ 0 _}_ . It is intuitively clear
that ( **X** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **S** ( _μ_ )) converges to an optimal solution to both (18.10) and
(18.11). This suggests the following algorithmic strategy: suppose ( **X** _,_ **y** _,_ **S** ) is
“near” ( **X** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **S** ( _μ_ )) for some _μ_ _>_ 0. Use ( **X** _,_ **y** _,_ **S** ) to move to a better
point ( **X** [+] _,_ **y** [+] _,_ **S** [+] ) “near” ( **X** ( _μ_ [+] ) _,_ **y** ( _μ_ [+] ) _,_ **S** ( _μ_ [+] )) for some _μ_ [+] _< μ_ .
It can be shown that if a point ( **X** _,_ **y** _,_ **S** ) is on the central path, then the
corresponding value of _μ_ satisfies **X** _•_ **S** = _nμ._ Likewise, given **X** _,_ **S** _≻_ **0**, define


_μ_ ( **X** _,_ **S** ) := **[X]** _[ •]_ **[ S]** _._

_n_


To move from a current point ( **X** _,_ **y** _,_ **S** ) to a new point, we use a suitable _Newton_
_step_ ; that is, the solution to the following system of equations obtained as a
linearization of the system of nonlinear equations **r** _μ_ ( **X** _,_ **y** _,_ **S** ) = **0** :



⎡

**0** **A** _[∗]_ **I**
⎣ **A** **0** **0**
**F** **0** **G**



⎤


⎦



⎡ ⎤

Δ **X**
⎣ Δ **y** ⎦ =
Δ **S**



⎡

**C** _−_ **A** [T] **y** _−_ **S**
⎣ **b** _−_ **AX**
_μ_ **X** _[−]_ [1] _−_ **S**



⎤


⎦ (18.14)



for some suitably chosen mappings **F** _,_ **G** that depend on the current **X** _,_ **S** . The
details of these mappings are somewhat technical and related to nuances concerning the space of symmetric _n × n_ matrices. Further details can be found
in Renegar (2001) and in the exercises at the end of the chapter.
Algorithm 18.1 presents a template for an interior-point method for semidefinite programming.


**Algorithm** **18.1** Interior-point method for semidefnite programming

1: choose **X** [0] _,_ **S** [0] _≻_ 0

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve the Newton system (18.14) for ( **X** _,_ **y** _,_ **S** ) = ( **X** _[k]_ _,_ **y** _[k]_ _,_ **S** _[k]_ ) and _μ_ :=
0 _._ 1 _μ_ ( **X** _[k]_ _,_ **S** _[k]_ )

4: choose a step length _α ∈_ (0 _,_ 1] and set ( **X** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **S** _[k]_ [+1] ) =
( **X** _[k]_ _,_ **y** _[k]_ _,_ **S** _[k]_ ) + _α_ (Δ **X** _,_ Δ **y** _,_ Δ **S** )

5: **end** **for**


The step length _α_ in step 4 should be chosen so that **X** _[k]_ [+1] _,_ **S** _[k]_ [+1] _≻_ **0** and
the size of **r** _μ_ ( **X** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **S** _[k]_ [+1] ) is sufficiently smaller than **r** _μ_ ( **X** _[k]_ _,_ **y** _[k]_ _,_ **S** _[k]_ ). A
line-search procedure such as the one described in Algorithm 2.4 in Chapter 2
can be used for choosing the step length _α_ .


**18.6** **Exercises** 287


**18.5** **Notes**


The seminal works of Alizadeh (1991) and Nesterov and Nemirovskii (1994)
triggered a massive burst of research activity in optimization. This eventually
led to a mature theory and computational technology for solving important
classes of conic programs, notably second-order and semidefinite programming.
A particularly important development was the extension of primal–dual interiorpoint methods to conic programs over _symmetric_ _cones_ by Nesterov and Todd
(1997, 1998). Such cones include the non-negative orthant, the second-order
cone, the semidefinite cone, and Cartesian products of them. The textbook
by Renegar (2001) gives an excellent exposition of the main advances in conic
programming.
The software packages SeDuMi and SDPT3 were developed respectively by the
late Sturm (1999) and by Toh et al. (1999). These two packages are some of the
default engines used by the MATLAB-based modeling language CVX.


**18.6** **Exercises**


**Exercise** **18.1** Recall that the trace of a square matrix **M** _∈_ R _[n][×][n]_ is


        - _n_



trace( **M** ) =



_Mii._

_i_ =1



Suppose **A** _∈_ R _[m][×][n]_ _,_ **B** _∈_ R _[n][×][p]_ _,_ and **C** _∈_ R _[p][×][m]_ . Show that the trace satisfies
the following property:


trace( **ABC** ) = trace( **CAB** ) _._


**Exercise** **18.2**


(a) Suppose **X** _∈_ S _[n]_ + [.] [Show] [that]


trace( **X** ) = 0 _⇒_ **X** = **0** _._


(b) Suppose **L** _∈_ R _[n][×][m]_ . Show that **LL** [T] _∈_ S _[n]_ + [.] [The] [converse] [is] [true] [also] [but] [it]
is harder to show: if **X** _∈_ S _[n]_ + [then] [there] [exists] **[L]** _[∈]_ [R] _[n][×][m]_ [for] [some] _[m]_ [such]
that **X** = **LL** [T] _._
(c) Show an example of two matrices **X** _,_ **S** _∈_ S _[n]_ such that **XS** _̸∈_ S _[n]_ .

(d) Prove (18.12). That is, show that


**X** _,_ **S** _∈_ S _[n]_ + _[,]_ [trace(] **[XS]** [) = 0] _⇒_ **XS** = **0** _._


Hint: Observe that this is not immediate from part (a) because by part (c)
_a_ _priori_ we do not even know if **XS** _∈_ S _[n]_ . To get around this difficulty, use
part (b), Exercise 18.1, and part (a).


288 **Conic** **Programming:** **Theory** **and** **Algorithms**


**Exercise** **18.3** Show that the Lorenz cone and the semidefinite cone are “selfdual.” In other words, show that


(L _n_ ) _[∗]_ = L _n_


and

(S _[n]_ + [)] _[∗]_ [=][ S] _[n]_ + _[.]_


**Exercise** **18.4** This exercise shows that semidefinite programming includes as
special cases both linear and second-order programming.


(a) Suppose **x** _∈_ R _[n]_ and **X** = diag( **x** ) _∈_ S _[n]_ . Show that


**x** _≥_ **0** _⇔_ **X** _⪰_ **0** _._




_∈_ **S** _[n]_ . Show that




        (b) Suppose **x** = _x_ 0
**x** ¯




- _∈_ R _[n]_ and **X** = _x_ 0 **x** ¯ [T]

**x** ¯ _x_ 0 **I** _n−_ 1



**x** _∈_ L _n_ _⇔_ **X** _⪰_ **0** _._


(c) Use (a) and (b) to conclude that any linear program or second-order program
can be recast as a semidefinite program.


## 19 Robust Optimization

In many optimization models the inputs to the problem are either not known at
the time the problem must be solved, are computed inaccurately, or are otherwise
uncertain. Since the solutions obtained can be quite sensitive to these inputs, one
serious concern is that we are solving the wrong problem, and that the solution
we find is far from optimal for the correct problem. Robust optimization is an
approach to optimization problems with data uncertainty to obtain solutions
that are _good_ for _all_ or _most_ possible realizations of the uncertain parameters.


**19.1** **Uncertainty** **Sets**


In robust optimization, the description of the parameter uncertainty is formalized via _uncertainty_ _sets_ . Uncertainty sets can represent or may be formed by
difference of opinions on the possible values of problem parameters, alternative
estimates of parameters generated via statistical techniques from historical data,
Bayesian, or other estimation techniques. The size of the uncertainty set is
typically determined by the level of desired robustness.
Some of the most common types of uncertainty sets encountered in robust
optimization models include the following:


_•_ Uncertainty sets representing a finite number of scenarios generated for the
possible values of the parameters:


_U_ = _{_ **p** 1 _,_ **p** 2 _, . . .,_ **p** _k}._


_•_ Uncertainty sets representing the convex hull of a finite number of scenarios
generated for the possible values of the parameters (these are sometimes
called polytopic uncertainty sets):


_U_ = conv _{_ **p** 1 _,_ **p** 2 _, . . .,_ **p** _k}._


_•_ Uncertainty sets representing an interval description for each uncertain parameter:


_U_ = _{_ **p** : **l** _≤_ **p** _≤_ **u** _}._


Confidence intervals encountered frequently in statistics can be the source
of such uncertainty sets.


290 **Robust** **Optimization**


_•_ Ellipsoidal uncertainty sets:


_U_ = _{_ **p** : **p** = **p** 0 + **Mu** _, ∥_ **u** _∥≤_ 1 _}._


These uncertainty sets can also arise from statistical estimation in the form
of confidence regions; see Goldfarb and Iyengar (2003). In addition to their
mathematically compact description, ellipsoidal uncertainty sets have the
nice property that they smooth the optimal value function (Werner, 2010).


It is a non-trivial task to determine the uncertainty set that is appropriate for
a particular model as well as the type of uncertainty sets that lead to tractable
problems. As a general guideline, the shape of the uncertainty set will often
depend on the sources of uncertainty as well as the sensitivity of the solutions to
these uncertainties. The size of the uncertainty set, on the other hand, will often
be chosen based on the desired level of robustness. When uncertain parameters
reflect the “true” values of moments of random variables, as is the case in
mean–variance portfolio optimization, we simply have no way of knowing these
unobservable true values exactly. In such cases, after making some assumptions
about the stationarity of these random processes, we can generate estimates of
these true parameters using statistical procedures. Goldfarb and Iyengar (2003),
for example, show that if we use a linear factor model for the multivariate returns
of several assets and estimate the factor loading matrices via linear regression, the
confidence regions generated for these parameters are ellipsoidal sets and they
advocate their use in robust portfolio selection as uncertainty sets. To generate
interval-type uncertainty sets, T¨ut¨unc¨u and Koenig (2004) use bootstrapping
strategies as well as moving averages of returns from historical data. The shape
and the size of the uncertainty set can significantly affect the robust solutions
generated. However, with few guidelines backed by theoretical and empirical
studies, their choice remains a mix of art and science.


**19.2** **Different** **Flavors** **of** **Robustness**


As we next describe, different types of robustness arise depending on what
parameters of a problem are uncertain, and depending also on what exactly
constitutes a “good” robust solution.


Constraint Robustness


Constraint robustness refers to situations where the uncertainty is in the constraints and we seek solutions that remain feasible for all possible values of
the uncertain inputs. This type of solution is required in many engineering
applications. Typical instances include multi-stage problems where the uncertain
outcomes of earlier stages have an effect on the decisions of the later stages and
the decision variables must be chosen to satisfy constraints no matter what
happens with the uncertain parameters of the problem.


**19.2** **Different** **Flavors** **of** **Robustness** 291


Here is a precise mathematical model for finding constraint-robust solutions.
Consider an optimization problem of the form


min _f_ ( **x** )
**x** (19.1)

s.t. _G_ ( **x** _,_ **p** ) _∈_ _K._


In this problem **x** is the vector of decision variables, _f_ ( **x** ) is the (certain) objective
function, _G_ and _K_ are the structural elements of the constraints assumed to be
certain, and **p** is the vector of possibly uncertain parameters of the problem.
Consider an uncertainty set _U_ that contains all possible values of the uncertain
parameters **p** . Then, a constraint-robust optimal solution can be found by solving
the following problem:


min _f_ ( **x** )
**x** (19.2)

s.t. _G_ ( **x** _,_ **p** ) _∈_ _K,_ for all **p** _∈U_ _._


The feasible set in the robust optimization model (19.2) is the intersection of the
feasible sets:


_S_ ( **p** ) = _{_ **x** : _G_ ( **x** _,_ **p** ) _∈_ _K},_ **p** _∈U_ _._


We note that there are no uncertain parameters in the objective function of the
problem (19.1). However, this is not a restrictive assumption. An optimization
problem with uncertain parameters in both the objective function and constraints can be easily reformulated to fit the form in (19.1). Indeed, the problem


min _f_ ( **x** _,_ **p** )
**x**

s.t. _G_ ( **x** _,_ **p** ) _∈_ _K_


is equivalent to the problem


min _t_
**x** _,t_

s.t. _f_ ( **x** _,_ **p** ) _≤_ _t_
_G_ ( **x** _,_ **p** ) _∈_ _K._


This last problem has all its uncertainties in its constraints only.


Objective Robustness


Another important robustness concept is objective robustness. This refers to
solutions that will remain close to optimal for all possible realizations of the
uncertain problem parameters. Since such solutions may be difficult to obtain,
especially when uncertainty sets are relatively large, an alternative goal for
objective robustness is to find solutions whose worst-case behavior is optimized.
The worst-case behavior of a solution corresponds to the value of the objective
function for the worst possible realization of the uncertain data for that particular solution. We now develop a mathematical model that addresses objective


292 **Robust** **Optimization**


robustness. Consider an optimization problem of the form:


min
**x** _∈S_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[.]_


Here, _S_ is a (certain) feasible set and _f_ ( **x** _,_ **p** ) is the objective function that
depends on uncertain parameters **p** . As before, let _U_ denote the uncertainty set
that contains all possible values of the uncertain parameters **p** . Then an objective
robust solution can be obtained by solving the _saddle-point_ _problem_


min
**x** _∈S_ [max] **p** _∈U_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[.]_


As indicated at the end of the previous subsection, objective robustness can be
seen as a special case of constraint robustness via a suitable reformulation. However, it is important to distinguish between these two problem variants as their
“natural” robust formulations lead to two different classes of optimization formulations. Robust-constraint problems naturally lead to optimization problems
with infinitely many constraints whereas robust-objective problems naturally
lead to saddle-point problems. There are different methodologies available for
each of these two problem classes.


Relative Robustness


The focus of constraint and objective robustness models on an _absolute_ measure
of worst-case performance is not consistent with risk tolerances of many decision
makers. Instead, we may prefer to measure the worst case in a _relative_ manner,
relative to the best possible solution under each scenario. This leads us to the
notion of relative robustness. Consider the optimization problem


min (19.3)
**x** _∈S_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[,]_


where **p** is uncertain with uncertainty set _U_ . To simplify the description, we
restrict our attention to the case with objective uncertainty and assume that the
constraints are certain. Given a fixed **p** _∈U_, let _z_ _[∗]_ ( **p** ) denote the optimal value
function

_z_ _[∗]_ ( **p** ) := min
**x** _∈S_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[.]_


Furthermore, define the optimal solution map


**x** _[∗]_ ( **p** ) = arg min _f_ ( **x** _,_ **p** ) _._
**x** _∈S_


Note that _z_ _[∗]_ ( **p** ) can be extended-valued and **x** _[∗]_ ( **p** ) can be set-valued. To motivate
the notion of relative robustness we first define a measure of regret associated
with a decision after the uncertainty is resolved. If we choose **x** as our vector
and **p** is the realized value of the uncertain parameter, the _regret_ associated with
choosing **x** instead of an element of **x** _[∗]_ ( **p** ) is defined as


_r_ ( **x** _,_ **p** ) = _f_ ( **x** _,_ **p** ) _−_ _z_ _[∗]_ ( **p** ) = _f_ ( **x** _,_ **p** ) _−_ _f_ ( **x** _[∗]_ ( **p** ) _,_ **p** ) _._


**19.2** **Different** **Flavors** **of** **Robustness** 293


Note that the regret function is always non-negative and can also be regarded
as a measure of the “benefit of hindsight”. Now, for a given **x** _∈_ _S_ consider the
maximum regret function:


_R_ ( **x** ) := max
**p** _∈U_ _[r]_ [(] **[x]** _[,]_ **[ p]** [) = max] **p** _∈U_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[ −]_ _[z][∗]_ [(] **[p]** [)] _[.]_


A relative robust solution to problem (19.3) is a vector **x** that minimizes the
maximum regret:


min (19.4)
**x** _∈S_ [max] **p** _∈U_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[ −]_ _[z][∗]_ [(] **[p]** [)] _[.]_


While they are intuitively attractive, relative robust formulations can also be significantly more difficult than the standard absolute robust formulations. Indeed,
since _z_ _[∗]_ ( **p** ) is the optimal value function and involves an optimization problem
itself, the problem (19.4) is a three-level optimization problem as opposed to the
two-level problems in absolute robust formulations. Furthermore, the optimal
value function _z_ _[∗]_ ( **p** ) is rarely available in analytic form, is typically non-smooth,
and is often hard to analyze. Another difficulty is that if _f_ is linear in **p**, as is often
the case, then _z_ _[∗]_ ( **p** ) is a concave function. Therefore, the inner maximization
problem in (19.4) is a convex _maximization_ problem and is difficult for most _U_ .
A simpler variant of (19.4) can be constructed by deciding on the maximum
level of regret to be tolerated beforehand and by solving a feasibility problem
instead with this level imposed as a constraint. For example, if we decide to limit
the maximum regret to _R_, then the problem to solve becomes the following: find
an **x** satisfying **x** _∈_ _S_ such that


_f_ ( **x** _,_ **p** ) _−_ _z_ _[∗]_ ( **p** ) _≤_ _R,_ for all **p** _∈U_ _._


If desired, one can then perform a bisection search on _R_ to find its optimal
value. Another variant of relative robustness models arises when we measure the
regret in terms of the proximity of our chosen solution to the optimal solution
set rather than in terms of the optimal objective values. For this model, consider
the following distance function for a given **x** and **p** :


_d_ ( **x** _,_ **p** ) = inf
**x** _[∗]_ _∈_ **x** _[∗]_ ( **p** ) _[∥]_ **[x]** _[ −]_ **[x]** _[∗][∥][.]_


When the solution set is a singleton, there is no optimization involved in the
definition. As above, we then consider the maximum distance function


_D_ ( **x** ) = max inf
**p** _∈U_ _[d]_ [(] **[x]** _[,]_ **[ p]** [) = max] **p** _∈U_ **x** _[∗]_ _∈_ **x** _[∗]_ ( **p** ) _[∥]_ **[x]** _[ −]_ **[x]** _[∗][∥][.]_


For relative robustness in this new sense, we seek **x** that solves


min (19.5)
**x** _∈S_ [max] **p** _∈U_ _[d]_ [(] **[x]** _[,]_ **[ p]** [)] _[.]_


This variant is an attractive model for cases where we have time to revise our
decision variables **x**, perhaps only slightly, once **p** is revealed. In such cases, we


294 **Robust** **Optimization**


will want to choose an **x** that will not need much perturbation under any scenario,
i.e., we seek the solution to (19.5). This model can also be useful for multi-period
problems where revisions of decisions between periods can be costly. Portfolio
rebalancing problems with transaction costs are examples of such settings.


**19.3** **Techniques** **for** **Solving** **Robust** **Optimization** **Models**


In this section we review a few of the commonly used techniques for the solution
of robust optimization problems. The tools we discuss are essentially reformulation strategies for robust optimization problems so that they can be rewritten as a
deterministic optimization problem with no uncertainty. In these reformulations,
we look for economy, so that the new formulation is not much bigger than the
original, “uncertain” problem, and tractability, so that the new problem can be
solved efficiently using standard optimization methods.
The variety of the robustness models and the types of uncertainty sets rule out
a unified approach. However, there are some common threads and the material
in this section can be seen as a guide to the available tools which can be
combined or appended with other techniques to solve a given problem in the
robust optimization setting.


Sampling


One of the simplest strategies for achieving robustness under uncertainty is to
sample several scenarios for the uncertain parameters from a set that contains
possible values of these parameters. This sampling can be done with or without using distributional assumptions on the parameters and produces a robust
optimization formulation with a finite uncertainty set. If uncertain parameters
appear in the constraints, we create a copy of each such constraint corresponding
to each scenario. Uncertainty in the objective function can be handled in a similar
manner. Consider the generic uncertain optimization problem


min _f_ ( **x** _,_ **p** )
**x**

s.t. _G_ ( **x** _,_ **p** ) _∈_ _K,_ for all **p** _∈U_ _._


If the uncertainty set _U_ is a finite set, i.e., _U_ = _{_ **p** 1 _,_ **p** 2 _, . . .,_ **p** _k}_, the robust
formulation is obtained as follows:


min _t_
**x** _,t_

s.t. _f_ ( **x** _,_ **p** _i_ ) _≤_ _t,_ _i_ = 1 _, . . ., k_
_G_ ( **x** _,_ **p** _i_ ) _∈_ _K,_ _i_ = 1 _, . . ., k._


Note that no reformulation is necessary in this case and the duplicated
constraints preserve the structural properties (linearity, convexity, etc.) of the
original constraints. Consequently, when the uncertainty set is a finite set the
resulting robust optimization problem is larger but theoretically no more difficult


**19.3** **Techniques** **for** **Solving** **Robust** **Optimization** **Models** 295


than the non-robust version of the problem. The situation is somewhat similar
to stochastic programming formulations. Examples of robust optimization
formulations with finite uncertainty sets can be found, for example in Rustem
and Howe (2002).


Conic Optimization


Moving from finite uncertainty sets to continuous sets such as intervals or ellipsoids presents a theoretical challenge. The robust version of an uncertain constraint that has to be satisfied for all values of the uncertain parameters in a
continuous set results in a semi-infinite optimization formulation. These problems
are called semi-infinite since there are infinitely many constraints but only finitely
many variables.
Fortunately, for some types of uncertainty sets, it is possible to reformulate
their robust semi-infinite programming versions using a _finite_ set of conic constraints. To illustrate this, consider the following simple linear program:


max **r** [T] **x**
**x**

s.t. **1** [T] **x** = 1 (19.6)
**x** _≥_ **0** _._


What is the optimal solution to this linear program?
Now suppose the objective coefficients are uncertain with ellipsoidal uncertainty, e.g., suppose the objective coefficient vector **r** can be any element in the
uncertainty set










_,_



_U_ =



**r** : _∥_ **r** _−_ _**μ**_ _∥_ 2 _≤_ _δ_



where _**μ**_ is the “nominal” value of **r** . The robust version of (19.6) is


max min **r** [T] **x**
**x** **r** _∈U_

s.t. **1** [T] **x** = 1
**x** _≥_ **0** _._


Some simple calculations show that for a given **x**


min
**r** _∈U_ **[r]** [T] **[x]** [ =] _**[ μ]**_ [T] **[x]** _[ −]_ _[δ][ · ∥]_ **[x]** _[∥]_ [2] _[.]_


Thus the robust version of (19.6) is


max _**μ**_ [T] **x** _−_ _δ · ∥_ **x** _∥_ 2
**x**
s.t. **1** [T] **x** = 1
**x** _≥_ **0** _._


296 **Robust** **Optimization**


The latter problem can be rewritten as the following conic program:


max _**μ**_ [T] **x** _−_ _δ · t_
**x** _,t_

s.t. **1** [T] **x** = 1

                    -                     _t_
**x** _∈_ L _n_ +1

**x** _≥_ **0** _._


More generally, suppose **r** has the following _ellipsoidal_ uncertainty set:


_U_ = _{_ **r** : ( **r** _−_ _**μ**_ ) [T] Σ _[−]_ [1] ( **r** _−_ _**μ**_ ) _≤_ _δ_ [2] _}_


for some symmetric and positive definite matrix Σ. Then the robust version of
(19.6) is



_√_
max _**μ**_ [T] **x** _−_ _δ ·_
**x**

s.t. **1** [T] **x** = 1
**x** _≥_ 0 _,_



**x** [T] Σ **x**



which again can be formulated as a conic program. Observe the resemblance
between the latter model and Markowitz’s mean–variance model.
The machinery of robust optimization can be applied to mean–variance portfolio optimization to mitigate the effects of estimation errors in the expected
returns and/or in the covariance matrix (Ceria and Stubbs, 2006; Goldfarb and
Iyengar, 2003). The basic idea is to consider the mean–variance optimization
problem in one of its forms, e.g.,



max **x** _**μ**_ [T] **x** _−_ [1] 2




[1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**



s.t. **Ax** = **b** (19.7)
**Cx** _≤_ **d** _,_



and assume _**μ**_ belongs to some uncertainty set,


_U_ = _{_ _**μ**_ : ( _**μ**_ _−_ _**μ**_ ˆ ) [T] Σ _[−]_ [1] ( _**μ**_ _−_ _**μ**_ ˆ ) _≤_ _δ_ [2] _}._


Then the robust version of (19.7) is



~~_√_~~
max _**μ**_ ˆ [T] **x** _−_ _δ ·_
**x**



**x** [T] Σ **x** _−_ [1]




[1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**



s.t. **Ax** = **b** (19.8)
**Cx** _≤_ **d** _._



We next show that (19.8) is a conic program. To that end, it suffices to find
a conic representation of the objective function. Let **R** _∈_ R _[n][×][p]_ _,_ **L** _∈_ R _[n][×][q]_ be
such that Σ = **RR** [T] and **V** = **LL** [T] . Both **R** and **L** exist because Σ and **V** are
positive semidefinite. By introducing new variables _s, t,_ the problem (19.8) can


**19.4** **Some** **Robust** **Optimization** **Models** **in** **Finance** 297


be rewritten as the following conic program:



max **x** _,s,t_ _**μ**_ ˆ [T] **x** _−_ _δ · s −_ [1] 2



**x** _,s,t_ 
_s_
s.t.
**Rx**




_∈_ L _p_ +1




[1] 2 _[γ][ ·][ t]_



⎡ ⎤

_t_ + 1
⎣ _t −_ 1⎦ _∈_ L _q_ +2
2 **Lx**



**Ax** = **b**
**Cx** _≤_ **d** _._


Saddle-Point Characterizations


For the solution of problems arising from objective uncertainty, the robust solution can be characterized using saddle-point conditions when the original problem satisfies certain convexity assumptions. The benefit of this characterization is
that we can then use algorithms such as interior-point methods already developed
and available for saddle-point problems. As an example of this strategy, consider
the objective-robust formulation discussed in Section 19.2:


min (19.9)
**x** _∈S_ [max] **p** _∈U_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[.]_


We note that the dual of this robust optimization problem is obtained by changing the order of the minimization and maximization problems:


max (19.10)
**p** _∈U_ [min] **x** _∈S_ _[f]_ [(] **[x]** _[,]_ **[ p]** [)] _[.]_


Under mild assumptions on _f, S, U_, there exists a _saddle-point_ solution ( **x** _[∗]_ _,_ **p** _[∗]_ ) _∈_
_S × U_ such that


_f_ ( **x** _[∗]_ _,_ **p** ) _≤_ _f_ ( **x** _[∗]_ _,_ **p** _[∗]_ ) _≤_ _f_ ( **x** _,_ **p** _[∗]_ ) for all **x** _∈_ _S,_ **p** _∈U_ _._


This characterization is the basis of the robust optimization algorithms given
in T¨ut¨unc¨u and Koenig (2004).


**19.4** **Some** **Robust** **Optimization** **Models** **in** **Finance**


Since many financial optimization problems involve future values of security
prices, interest rates, exchange rates, etc., which are not known in advance
but can only be forecasted or estimated, such problems fit perfectly into the
framework of robust optimization. We next describe some examples of robust
optimization formulations for a variety of financial optimization problems.


298 **Robust** **Optimization**


Robust Profit Opportunities in Risky Portfolios


Consider an investment environment with _n_ financial securities whose future
price vector **r** _∈_ R _[n]_ is a random variable. Let **p** _∈_ R _[n]_ represent the current

                                        -                                         prices of these securities. If the investor chooses a portfolio **x** = _x_ 1 _· · ·_ _xn_

that satisfies

**p** [T] **x** _<_ 0


and the realization of the random variable **r** satisfies


**r** [T] **x** _≥_ 0 (19.11)


then there is an arbitrage opportunity: an investor could make money by
constructing the portfolio **x** with negative cash flow (pocketing money) and
subsequently collecting the non-negative cash flow **r** [T] **x** of the portfolio **x** .
Since arbitrage opportunities generally do not persist in financial markets, one
might be interested in the alternative and weaker profitability notion where the
non-negativity of the portfolio is only guaranteed to occur with high probability.
More precisely, consider the following relaxation of (19.11):


**P** ( **r** [T] **x** _≥_ 0) _≥_ 0 _._ 99 _._ (19.12)


Let _**μ**_ and **Q** represent the expected future price vector and covariance matrix

                 of the random vector **r** . Then E( **r** ) = _**μ**_ [T] **x** and stdev( **r** [T] **x** ) = **x** [T] **Qx** . If the
random vector **r** is Gaussian, then (19.12) is equivalent to

           _**μ**_ [T] **x** _−_ _θ ·_ **x** [T] **Qx** _≥_ 0 _,_


where _θ_ = Φ _[−]_ [1] (0 _._ 99) and Φ is the standard normal cumulative distribution.
Therefore, if we find an **x** satisfying

          _**μ**_ [T] **x** _−_ _θ ·_ **x** [T] **Qx** _≥_ 0 _,_ **p** [T] **x** _<_ 0 _,_


for a large enough positive value of _θ_, we have an approximation of an arbitrage
opportunity. Note that, by relaxing the constraint **p** [T] **x** _<_ 0 as **p** [T] **x** _≤_ 0 or as
**p** [T] **x** _≤−ε_, we obtain a conic feasibility system. Therefore, the resulting system
can be solved using the conic optimization approaches.
We next explore some portfolio selection models that incorporate the uncertainty of problem inputs.


Robust Portfolio Selection


This section is adapted from T¨ut¨unc¨u and Koenig (2004). Recall that Markowitz’s
mean–variance optimization problem can be stated in the following form, which
combines the reward and risk in the objective function:


max (19.13)
**x** _∈X_ _**[μ]**_ [T] **[x]** _[ −]_ _[γ]_ 2 _[·]_ **[ x]** [T] **[Qx]** _[.]_


Here _**μ**_ and **Q** are respectively estimates of the vector of expected values and
covariance of returns of a universe of securities, and _γ_ is a risk-aversion constant


**19.4** **Some** **Robust** **Optimization** **Models** **in** **Finance** 299


used to trade off the reward (expected return) and risk (portfolio variance). The
set _X_ is the set of feasible portfolios which may carry information on shortsale restrictions, sector distribution requirements, etc. Since such restrictions are
predetermined, we can assume that the set _X_ is known without any uncertainty
at the time the problem is solved.
Recall also that solving the problem above for different values of _γ_ we obtain
the _efficient frontier_ of the set of feasible portfolios. The optimal portfolio will be
different for individuals with different risk-taking tendencies, but it will always
be on the efficient frontier.
One of the limitations of this model is its need to accurately estimate the
expected returns and covariances. In Bawa et al. (1979), the authors argue that
using estimates of the unknown expected returns and covariances leads to an
_estimation_ _risk_ in portfolio choice, and that methods for optimal selection of
portfolios must take this risk into account. Furthermore, the optimal solution
is sensitive to perturbations in these input parameters - a small change in
the estimate of the return or the variance may lead to a large change in the
corresponding solution; see, for example, Michaud and Michaud (2008). This
attribute is unfavorable since the modeler may want to periodically rebalance
the portfolio based on new data and may incur significant transaction costs to
do so. Furthermore, using point estimates of the expected return and covariance
parameters does not fulfill the needs of a conservative investor. Such an investor
would not necessarily trust these estimates and would be more comfortable
choosing a portfolio that will perform well under a number of different scenarios.
Of course, such an investor cannot expect to get better performance on some of
the more likely scenarios, but will have insurance for more extreme cases. All
these arguments point to the need of a portfolio optimization formulation that
incorporates robustness and tries to find a solution that is relatively insensitive
to inaccuracies in the input data. Since all the uncertainty is in the objective function coefficients, we seek an objective robust portfolio, as outlined in
Section 19.2.
For _robust_ _portfolio_ _optimization_ we consider a model that allows return and
covariance matrix information to be given in the form of intervals. For example, this information may take the form “the expected return on security _j_ is
between 8% and 10%” rather than claiming that it is 9%. Mathematically, we
will represent this information as membership in the following set:


_U_ = _{_ ( _**μ**_ _,_ **Q** ) : _**μ**_ _[L]_ _≤_ _**μ**_ _≤_ _**μ**_ _[U]_ _,_ **Q** _[L]_ _≤_ **Q** _≤_ **Q** _[U]_ _,_ **Q** _⪰_ **0** _},_ (19.14)


where _**μ**_ _[L]_ _,_ _**μ**_ _[U]_ _,_ **Q** _[L]_ _,_ **Q** _[U]_ are the extreme values of the intervals we just mentioned.
The restriction **Q** _⪰_ **0** is necessary since **Q** is a covariance matrix and, therefore,
must be positive semidefinite. These intervals may be generated in different ways.
An extremely cautious modeler may want to use historical lows and highs of
certain input parameters as the range of their values. One may generate different
estimates using different scenarios on the general economy and then combine the
resulting estimates. Different analysts may produce different estimates for these
parameters and one may choose the extreme estimates as the endpoints of the


300 **Robust** **Optimization**


intervals. One may choose a confidence level and then generate estimates of
covariance and return parameters in the form of prediction intervals.
We want to find a portfolio that maximizes the objective function in (19.13) in
the worst-case realization of the input parameters _**μ**_ and **Q** from their uncertainty
set _U_ in (19.14). Given these considerations the robust optimization problem
takes the following form


max min (19.15)
**x** _∈X_ ( _**μ**_ _,_ **Q** ) _∈U_ _**[μ]**_ [T] **[x]** _[ −]_ _[γ]_ 2 _[·]_ **[ x]** [T] **[Qx]** _[.]_


This problem can be expressed as a _saddle-point_ _problem_ and be solved using
the technique outlined in Halld´orsson and T¨ut¨unc¨u (2003).


Relative Robustness in Portfolio Selection


We consider the following simple three-asset portfolio model from Ceria and
Stubbs (2006):



max _**μ**_ [T] **x**
s.t. _TE_ ( **x** ) _≤_ 0 _._ 1
**1** [T] **x** = 1
**x** _≥_ **0** _,_



(19.16)




      -       where **x** = _x_ 1 _x_ 2 _x_ 3 and



⎡



T ⎡



0 _._ 1764 0 _._ 09702 0
⎣0 _._ 9702 0 _._ 1089 0
0 0 0



⎤


⎦



⎡

_x_ 1 _−_ 0 _._ 5
⎣ _x_ 2 _−_ 0 _._ 5
_x_ 3



⎤


⎦ _._



⎤


⎦



_TE_ ( **x** ) =




~~�~~

~~�~~







_x_ 1 _−_ 0 _._ 5
⎣ _x_ 2 _−_ 0 _._ 5
_x_ 3



This is essentially a two-asset portfolio optimization problem where the third
asset represents the proportion of the funds that are not invested. The first two
assets have standard deviations of 42% and 33% respectively and a correlation
coefficient of 0.7. The “benchmark” is the portfolio that invests funds half-andhalf in the two assets. The function _TE_ ( **x** ) represents the tracking error of the
portfolio with respect to the half-and-half benchmark and the first constraint
indicates that this tracking error should not exceed 10%. The second constraint
is the budget constraint; the third enforces no shorting. We depict the projection
of the feasible set of this problem onto the space spanned by variables _x_ 1 and _x_ 2
in Figure 19.1.
We now build a relative robustness model for this portfolio problem. We
assume that the covariance matrix estimate is certain. We consider a very simple
uncertainty set for the expected return estimates consisting of three scenarios
represented with the three arrows in Figure 19.2. These three scenarios correspond to the following values for _**μ**_ : (6 _,_ 4 _,_ 0) _,_ (5 _,_ 5 _,_ 0) _,_ and (4 _,_ 6 _,_ 0) _._ When
_**μ**_ = (6 _,_ 4 _,_ 0) the optimal solution is (0 _._ 831 _,_ 0 _._ 169 _,_ 0) with objective value 5 _._ 662 _._
Similarly, when _**μ**_ = (4 _,_ 6 _,_ 0) the optimal solution is (0 _._ 169 _,_ 0 _._ 831 _,_ 0) with objective value 5 _._ 662 _._ When _**μ**_ = (5 _,_ 5 _,_ 0) all points between the previous two optimal


**19.4** **Some** **Robust** **Optimization** **Models** **in** **Finance** 301


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


**Figure** **19.1** The feasible set of the mean–variance model (19.16)


solutions are optimal with a shared objective value of 5.0. Therefore, the relative
robust formulation for this problem can be written as follows:


min _t_
**x** _,t_



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-313-0.png)

s.t. 5 _._ 662 _−_ (6 _x_ 1 + 4 _x_ 2) _≤_ _t_
5 _._ 662 _−_ (4 _x_ 1 + 6 _x_ 2) _≤_ _t_
5 _−_ (5 _x_ 1 + 5 _x_ 2) _≤_ _t_
_TE_ ( **x** ) _≤_ 0 _._ 1
**1** [T] **x** = 1
**x** _≥_ **0** _._



(19.17)



Instead of solving the problem where the optimal regret level is a variable ( _t_
in the formulation), an easier strategy is to choose a level of regret that can
be tolerated and find portfolios that do not exceed this level of regret in any
scenario. For example, choosing a maximum tolerable regret level of 0 _._ 75 we get
the following feasibility problem:


5 _._ 662 _−_ (6 _x_ 1 + 4 _x_ 2) _≤_ 0 _._ 75
5 _._ 662 _−_ (4 _x_ 1 + 6 _x_ 2) _≤_ 0 _._ 75
5 _−_ (5 _x_ 1 + 5 _x_ 2) _≤_ 0 _._ 75
_TE_ ( **x** ) _≤_ 0 _._ 1
**1** [T] **x** = 1
**x** _≥_ **0** _._


This problem and its feasible set of solutions is illustrated in Figure 19.2.


302 **Robust** **Optimization**


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



![](C:/AssetManager/data/quant_kb/Optimization_Methods_v2/Optimization Methods in Finance（second E）_assets/Optimization-Methods-in-Finance（second-E）.pdf-314-0.png)





0
0 0.2 0.4 0.6 0.8 1


**Figure** **19.2** Set of solutions with regret less than 0.75 for the mean–variance
model (19.16)


**19.5** **Notes**


Robust optimization was introduced by Ben-Tal and Nemirovski (1998, 2002)
and independently by El Ghaoui and Lebret (1997) and El Ghaoui et al. (1998).
The textbook by Ben-Tal et al. (2009) gives a thorough discussion on the subject,
including an extensive list of references.
Although robust optimization is widely popular in a variety of disciplines, it
is not as widespread in financial optimization yet. There are strong supporters
of its potential in finance (Ceria and Stubbs, 2006; Goldfarb and Iyengar, 2003;
T¨ut¨unc¨u and Koenig, 2004). There are also some skeptics (Scherer, 2007).


**19.6** **Exercises**


**Exercise** **19.1** Consider the optimization problem


max _**μ**_ [T] **x** _−_ [1] 2 _[γ][ ·]_ **[ x]** [T] **[Vx]**

(19.18)
**1** [T] **x** = 1 _,_


where **V** is a positive definite covariance matrix of asset returns, _**μ**_ is a vector
of expected returns, and _γ_ _>_ 0 is a risk-aversion constant. Assume **V** is certain
but _**μ**_ is uncertain.


(a) Let _z_ ( _**μ**_ ) denote the optimal value of (19.18). Show that _**μ**_ _�→_ _z_ ( _**μ**_ ) is a
quadratic convex function.
(b) Let _U_ denote the uncertainty set for _**μ**_ . Formulate both the absolute and
relative robust optimization versions of (19.18).


**19.6** **Exercises** 303


(c) Show that the absolute and relative robust optimization versions for the
uncertainty sets _U_ = _{_ _**μ**_ [1] _, . . .,_ _**μ**_ _[k]_ _}_ and _U_ = conv _{_ _**μ**_ [1] _, . . .,_ _**μ**_ _[k]_ _}_ are equivalent.


**Exercise** **19.2** (Robust least squares) Let **P** _∈_ R _[m][×][n]_, with **q** _∈_ R _[m]_, and
consider the least-squares problem


min (19.19)
**v** _[∥]_ **[Pv]** _[ −]_ **[q]** _[∥]_ [2] _[.]_


The purpose of this exercise is to compare the above usual least-squares problem
with a robust version.


(a) Suppose the matrix **P** can take any value in the ellipsoidal uncertainty set


_U_ = _{_ **P** : _∥_ **P** _−_ **P** [¯] _∥_ = _ρ},_


where _∥_ **P** _−_ **P** [¯] _∥_ is either the operator norm or the Frobenius norm of the
matrix **P** _−_ **P** [¯] .
Show that the robust version min [of] [(19.19)] [is] [equivalent]
**P** _∈U_ [min] **v** _[∥]_ **[Pv]** _[ −]_ **[q]** _[∥]_ [2]

to the problem


min (19.20)
**v** _[∥]_ **[Pv]** [¯] _[ −]_ **[q]** _[∥]_ [2][ +] _[ ρ][∥]_ **[v]** _[∥]_ [2] _[.]_


(b) Set **P** _,_ **q** as follows:

  - P = [1, 0 ; 1, 0.001 ; 10, -0.01] ;

  - q = [1 2 0]’ ;

Use the MATLAB command


  - v = P \ q


to find the solution **v** _[∗]_ to (19.19) for the above values of **P** _,_ **q** _._
What is the value of **v** _[∗]_ and the value of _∥_ **Pv** _[∗]_ _−_ **q** _∥_ 2 that you found?
(c) Now consider the matrix **Q** obtained by adding a small random perturbation
to **P**

  - Q = P + 0.05*randn(3,2)
What is the value of _∥_ **Qv** _[∗]_ _−_ **q** _∥_ 2 for the solution **v** found in (a)? Repeat
this a few (two or three) times. What do you observe?
(d) Now use the robust formulation (19.20) to find a robust solution **v** _[∗]_ to (19.19)
for _ρ_ = 0 _._ 1.
What is the value of **v** _[∗]_ and the value of _∥_ **Pv** _[∗]_ _−_ **q** _∥_ 2 that you found? How
different are they from the usual least-squares answers found in part (b)?

(e) Repeat part (c) for the robust solution **v** that you found in (d). How different
is the behavior now?


**Exercise** **19.3** Consider the convex quadratic inequality


**x** [T] ( **AA** [T] ) **x** _−_ 2 **b** [T] **x** + _γ_ _≤_ 0 _,_


304 **Robust** **Optimization**


where the parameters ( **A** _,_ **b** _, γ_ ) belong to the uncertainty set








        
- _k_

_uj_ ( **A** _[j]_ _,_ **b** _[j]_ _, γ_ _[j]_ ) : _∥_ **u** _∥_ 2 _≤_ 1

_j_ =1



_U_ =



( **A** _,_ **b** _, γ_ ) = ( **A** [0] _,_ **b** [0] _, γ_ [0] ) +



for some fixed ( **A** _[j]_ _,_ **b** _[j]_ _, γ_ _[j]_ ), for _j_ = 0 _,_ 1 _, . . ., k._
Show that the (infinite) robust quadratic constraint


**x** [T] ( **AA** [T] ) **x** _−_ 2 **b** [T] **x** + _γ_ _≤_ 0 for all ( **A** _,_ **b** _, γ_ ) _∈U_


holds if and only if there exist **z** _[j]_ _, y_ _[j]_, for _j_ = 1 _, . . ., k_, and _λ_ such that



**A** _[j]_ **x** = **z** _[j]_ _,_ _j_ = 0 _,_ 1 _, . . ., k_
( **b** _[j]_ ) [T] **x** = _y_ _[j]_ _,_ _j_ = 0 _,_ 1 _, . . ., k_
_λ ≥_ 0
⎡



_γ_ [0] + 2 _y_ [0] _−_ _λ_ ( **y** + [1] 2
⎣ [1]



⎤


⎦ _⪰_ **0** _,_



**y** + [1]




[1] 2 _[γ]_ [)][T] ( **z** [0] ) [T]




[1] 2 _[γ]_ _λ_ **I** **Z** [T]



**z** [0] **Z** **I**




      -       -       where **y** = _y_ [1] _· · ·_ _y_ _[k]_ [�][T], _γ_ = _γ_ [1] _· · ·_ _γ_ _[k]_ [�][T] _,_ and **Z** = **z** [1] _· · ·_ **z** _[k]_ [�] _._
Conclude that the robust version of the optimization problem


min **c** [T] **x**
**x**

s.t. **x** [T] ( **AA** [T] ) **x** _−_ 2 **b** [T] **x** + _γ_ _≤_ 0


for the above kind of uncertainty set _U_ can be written as a semidefinite program.


## 20 Nonlinear Programming: Theory and Algorithms

It is sometimes necessary to consider more general nonlinear programs than the
ones we have already studied: linear, quadratic, or conic programs. We give a
brief introduction to this vast topic, and we discuss an application to estimating
a volatility surface.


**20.1** **Nonlinear** **Programming**


Consider a very general optimization problem of the form


min _f_ ( **x** )
**x**

s.t. _gj_ ( **x** ) = _bj,_ for _j_ = 1 _, . . ., m_
_hi_ ( **x** ) _≤_ _di,_ for _i_ = 1 _, . . ., p,_


or the equivalent more concise form


min _f_ ( **x** )
**x**

s.t. **g** ( **x** ) = **b** (20.1)
**h** ( **x** ) _≤_ **d** _,_


where _f, gj, hi_ : R _[n]_ _→_ R. In the special case when all functions _f, gj, hi_ are
linear, problem (20.1) is a linear program as discussed in Chapter 2. When some
of the functions _f, gj, hi_ are nonlinear, problem (20.1) is a _nonlinear_ _program_ .
Many practical problems are naturally formulated as nonlinear programs. We
already saw quadratic programming and conic programming in earlier chapters.
However, the family of problems that can be formulated as nonlinear programs is
enormous, as many, if not most, imaginable kinds of constraints and objectives
can be cast in terms of nonlinear functions. (For some noteworthy examples,
see the exercises at the end of the chapter.) The immense modeling power
of nonlinear programming comes at a cost: unlike linear, quadratic, and conic
programming, which have a solid theory and are solvable via a few algorithmic
templates, both the theory and methods to solve general nonlinear programs
are far more complicated. Different types of nonlinear programs, determined by
structural properties of the objective and constraint functions, are amenable to
different types of algorithms. The subsequent sections sketch the main theory
and most popular algorithmic ideas. A comprehensive treatment of this vast


306 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


topic is beyond the scope of this textbook. We refer the reader to the excellent
references Bertsekas (1999), G¨uler (2010), and Nocedal and Wright (2006) for
more details.


**20.2** **Numerical** **Nonlinear** **Programming** **Solvers**


There are numerous software packages for solving nonlinear programs. The following are some popular ones. We list them according to the class of algorithms
(discussed in Section 20.4) that they are based on:


(1) CONOPT, GRG2, Excel SOLVER. These solvers are based on the _generalized_
_reduced-gradient_ _method_ .
(2) MATLAB optimization toolbox, SNOPT, NLPQL. These solvers are based on
sequential quadratic programming.
(3) MINOS, LANCELOT. These solvers are based on an _augmented_ _Lagrangian_
_approach._
(4) MOSEK, LOQO, IPOPT. These solvers are based on _interior-point_ _methods._


**20.3** **Optimality** **Conditions**


In this section we consider the class of nonlinear programs (20.1) where the
functions _f, gi, hj_ are once or twice continuously differentiable. The optimality
conditions for linear and convex quadratic programs extend to this more general
context, albeit some new technicalities arise. In particular, for a general nonlinear
program the theory described below applies to _local_ _minima._
Let _X_ := _{_ **x** _∈_ R _[n]_ : **g** ( **x** ) = **b** _,_ **h** ( **x** ) _≤_ **d** _}_ denote the feasible set of (20.1).
A point **x** _[∗]_ _∈X_ is a _local_ _minimum_ of (20.1) if there exists _r_ _>_ 0 such that
_f_ ( **x** _[∗]_ ) _≤_ _f_ ( **x** ) for all **x** _∈_ B _r_ ( **x** _[∗]_ ) _∩X_ _,_ where B _r_ ( **x** _[∗]_ ) denotes the ball of radius _r_
around **x** _[∗]_ ; that is,


B _r_ ( **x** _[∗]_ ) := _{_ **x** _∈_ R _[n]_ : _∥_ **x** _−_ **x** _[∗]_ _∥≤_ _r}._


A point **x** _[∗]_ _∈X_ is a _strict_ _local_ _minimum_ of (20.1) if there exists _r_ _>_ 0 such that
_f_ ( **x** _[∗]_ ) _< f_ ( **x** ) for all **x** _∈_ B _r_ ( **x** _[∗]_ ) _∩X_ _._


Unconstrained Case


For ease of exposition we first describe the optimality conditions for the simpler
case without constraints. Consider the unconstrained optimization problem


min (20.2)
**x** _∈_ R _[n][ f]_ [(] **[x]** [)] _[,]_


where _f_ : R _[n]_ _→_ R.


**20.3** **Optimality** **Conditions** 307


**Theorem** **20.1** (First-order necessary conditions) _Suppose_ _f_ _is_ _continuously_
_differentiable._ _If_ _a_ _point_ **x** _[∗]_ _∈_ R _[n]_ _is_ _a_ _local_ _minimum_ _of_ (20.2) _then_ _∇f_ ( **x** _[∗]_ ) = **0** _._


The above necessary conditions can be sharpened when the objective function
is twice differentiable.


**Theorem** **20.2** (Second-order necessary and sufficient conditions) _Suppose_ _f_ _is_
_twice_ _continuously_ _differentiable._


(a) _If_ _a_ _point_ **x** _[∗]_ _∈_ R _[n]_ _is_ _a_ _local_ _minimum_ _of_ (20.2) _then_ _∇f_ ( **x** _[∗]_ ) = **0** _and_
_∇_ [2] _f_ ( **x** _[∗]_ ) _⪰_ **0** _._
(b) _If_ **x** _[∗]_ _∈_ R _[n]_ _is_ _such_ _that_ _∇f_ ( **x** _[∗]_ ) = **0** _and_ _∇_ [2] _f_ ( **x** _[∗]_ ) _≻_ **0** _then_ **x** _[∗]_ _is_ _a_ _strict_
_local_ _minimum_ _of_ (20.2) _._


Constrained Case


Consider now the general constrained problem (20.1). The optimality conditions
for (20.1) rely on the following technical condition.


**Definition** **20.3** Let **x** _∈X_ . Define _I_ ( **x** ) := _{i_ : _hi_ ( **x** ) = _di}_ . The point **x**
satisfies the _linear_ _independence_ _constraint_ _qualification_ if the set of gradient
vectors


_{∇gj_ ( **x** ) : _j_ = 1 _, . . ., m} ∪{∇hi_ ( **x** ) : _i ∈_ _I_ ( **x** ) _}_


is linearly independent.


**Theorem** **20.4** (First-order necessary conditions) _Suppose_ _f, gi, hj_ _are_ _continu-_
_ously_ _differentiable._ _If_ _a_ _point_ **x** _[∗]_ _∈X_ _is_ _a_ _local_ _minimum_ _of_ (20.1) _and_ _satisfies_
_the_ _linear_ _independence_ _constraint_ _qualification,_ _then_ _there_ _exist_ _some_ _Lagrange_
_multipliers_ **y** _∈_ R _[m]_ _and_ **s** _∈_ R _[p]_ _such_ _that_

_∇f_ ( **x** _[∗]_ ) + [�] _[m]_ _j_ =1 _[y][j][∇][g][j]_ [(] **[x]** _[∗]_ [) +][ �] _j_ _[p]_ =1 **[s]** _[i][∇][h][i]_ [(] **[x]** _[∗]_ [) =] **[ 0]**
**s** _≥_ **0** (20.3)
_si_ ( _hi_ ( **x** _[∗]_ ) _−_ _di_ ) = 0 _,_ _for_ _i_ = 1 _, . . ., p._


Observe that the first block of equations in (20.3) can be written as


_∇_ **x** _L_ ( **x** _[∗]_ _,_ **y** _,_ **s** ) = _∇f_ ( **x** _[∗]_ ) + _∇_ **g** ( **x** _[∗]_ ) **y** + _∇_ **h** ( **x** _[∗]_ ) **s** = **0** _,_


where _L_ ( **x** _,_ **y** _,_ **s** ) is the following _Lagrangian_ _function_ for (20.1):


_L_ ( **x** _,_ **y** _,_ **s** ) := _f_ ( **x** ) + **y** [T] ( **g** ( **x** ) _−_ **b** ) + **s** [T] ( **h** ( **x** ) _−_ **d** ) _,_


and where

      -      -      -      _∇_ **g** ( **x** ) = _∇g_ 1( **x** ) _· · ·_ _∇gm_ ( **x** ) and _∇_ **h** ( **x** ) = _∇h_ 1( **x** ) _· · ·_ _∇hp_ ( **x** ) _._


Observe the nice analogy to the first-order conditions for the unconstrained case.
We next give second-order necessary and sufficient conditions. The precise


308 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


statements of the second-order conditions involve the following tangent subspace.
Let **x** _∈X_ . The _tangent_ _subspace_ _T_ ( **x** ) is defined as


_T_ ( **x** ) := _{_ **d** _∈_ R _[n]_ : _∇gj_ ( **x** ) [T] **d** = 0 _,_ _j_ = 1 _, . . ., m,_ and _∇hi_ ( **x** ) [T] **d** = 0 _,_ _i ∈_ _I_ ( **x** ) _}._


**Theorem** **20.5** (Second-order necessary conditions) _Suppose_ _f_ _is_ _twice_ _continu-_
_ously differentiable._ _If_ _a_ _point_ **x** _[∗]_ _∈_ R _[n]_ _is_ _a_ _local_ _minimum_ _of_ (20.2) _and_ _satisfies_
_the_ _linear_ _independence_ _constraint_ _qualification,_ _then_ _there_ _exist_ **y** _∈_ R _[m]_ _and_
**s** _∈_ R _[p]_ _such_ _that_ (20.3) _holds_ _and_


**d** [T] ( _∇_ [2] **x** _[L]_ [(] **[x]** _[∗][,]_ **[ y]** _[,]_ **[ s]** [))] **[d]** _[ ≥]_ [0]


_for_ _all_ **d** _∈_ _T_ ( **x** _[∗]_ ) _._


**Theorem** **20.6** (Second-order sufficient conditions) _Suppose_ _f_ _is_ _twice_ _contin-_
_uously_ _differentiable_ _and_ **x** _[∗]_ _∈_ R _[n]_ _satisfies_ _the_ _linear_ _independence_ _constraint_
_qualification._ _If_ _there_ _exist_ **y** _∈_ R _[m]_ _and_ **s** _∈_ R _[p]_ _such_ _that_ (20.3) _holds_ _as_ _well_ _as_
_hi_ ( **x** _[∗]_ ) = _di_ _⇒_ _si_ _>_ 0 _,_ _and_


**d** [T] ( _∇_ [2] **x** _[L]_ [(] **[x]** _[∗][,]_ _**[ λ]**_ _[,]_ _**[ μ]**_ [))] **[d]** _[ >]_ [ 0]


_for_ _all_ _non-zero_ **d** _∈_ _T_ ( **x** _[∗]_ ) _,_ _then_ **x** _[∗]_ _is_ _a_ _local_ _minimum_ _of_ (20.1) _._


Convex Case


As we detail next, the optimality conditions described above simplify and
strengthen substantially when the underlying problem is convex.


**Proposition** **20.7** _Assume_ _the_ _objective_ _function_ _f_ _in_ (20.2) _is_ _convex_ _and_
_differentiable. Then_ **x** _[∗]_ _is an optimal solution to_ (20.2) _if and only if ∇f_ ( **x** _[∗]_ ) = **0** _._


**Proposition** **20.8** _Assume_ _the_ _objective_ _function_ _f_ _in_ (20.1) _is_ _convex,_ _the_
_equality constraint functions gi_ _are linear, and the inequality constraint functions_
_hj_ _are_ _convex._ _Furthermore_ _assume_ _all_ _f, gi, hj_ _are_ _differentiable._ _Then_ **x** _[∗]_ _is_ _an_
_optimal_ _solution_ _to_ (20.1) _if_ _and_ _only_ _if_ _there_ _exist_ **y** _∈_ R _[m]_ _,_ **s** _∈_ R _[p]_ _such_ _that_


_∇_ **x** _L_ ( **x** _[∗]_ _,_ **y** _,_ **s** ) = **0** _,_ **g** ( **x** _[∗]_ ) = **b** _,_ **h** ( **x** _[∗]_ ) _≤_ **d** _,_ **s** _≥_ **0** _,_ **s** [T] ( **h** ( **x** _[∗]_ ) _−_ **d** ) = 0 _._


**20.4** **Algorithms**


Unconstrained Case


We next describe three main algorithmic approaches to solving an unconstrained
optimization problem of the form (20.2), namely the _gradient_ _descent_ _method_,
_Newton’s method,_ and the _subgradient method_ . These methods in turn provide the
foundation for the more elaborate methods for solving constrained optimization
problems.


**20.4** **Algorithms** 309


_Gradient_ _Descent_
Suppose the objective function _f_ in (20.2) is differentiable. In this case a simple
method for solving (20.2) is based on going downhill on the graph of the function
_f_ . The gradient gives the direction of fastest initial increase and thus its negative
is the direction of fastest initial decrease. This can also be motivated by the firstorder Taylor approximation of _f_ around a point **x** : for **p** small we have


_f_ ( **x** + **p** ) _≈_ _f_ ( **x** ) + _∇f_ ( **x** ) [T] **p** _._


Among all **p** of fixed norm, the one pointing in the direction _−∇f_ ( **x** ) minimizes
the right-hand side.
Algorithm 20.1 gives a formal description of the gradient descent method.


**Algorithm** **20.1** Gradient descent method

1: choose **x** [0] _∈_ R _[n]_

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: choose a step length _αk_ _>_ 0 and set **x** _[k]_ [+1] = **x** _[k]_ _−_ _αk∇f_ ( **x** _[k]_ )

4: **end** **for**


The choice of step length _α_ is a critical detail in the implementation of the
gradient descent algorithm. If _α_ is too large, the algorithm may fail to converge to
a solution because the objective value could even increase after one iteration. On
the other hand, if _α_ is too small, the algorithm will be too slow. This issue applies
not only to the gradient descent method but to any method that aims to move
along a direction **p** . Suppose **p** _∈_ R _[n]_ is a _descent_ _direction_ at the current point
**x** _[k]_ ; that is, _∇f_ ( **x** _[k]_ ) [T] **p** _<_ 0. A popular approach is to choose the step length large
enough and perform _backtracking_ ; that is, shrink _αk_ by a multiplicative constant
smaller than one until the following sufficient decrease condition holds for some
predetermined _μ ∈_ (0 _,_ 1):


_f_ ( **x** _[k]_ + _αk_ **p** ) _≤_ _f_ ( **x** _[k]_ ) + _αk · μ · ∇f_ ( **x** _[k]_ ) [T] **p** _._ (20.4)


The sufficient decrease requirement in (20.4) is called the _Armijo–Goldstein_
condition. The first-order Taylor approximation for _f_ around **x** ensures that
(20.4) holds for sufficiently small _αk_ provided _f_ is differentiable and **d** is a
descent direction. Algorithm 20.2 describes this kind of backtracking. This type
of backtracking is also often called _line_ _search._


**Algorithm** **20.2** Backtracking to select the step length _αk_

1: choose _αk_ _>_ 0 and _β, μ ∈_ (0 _,_ 1)

2: **while** (20.4) fails **do** _αk_ = _β · αk_
3: **end** **while**


310 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


_Newton’s_ _Method_
The gradient descent method uses only _first-order_ information to choose the
descent direction at each main iteration. There are several approaches to incorporate additional information and speed up convergence. Newton’s method yields
a substantially improved direction by incorporating _second-order_ information. In
its _pure_ form each step of Netwon’s method for (20.2) updates a trial point **x** to
the new point

**x** [+] = **x** _−∇_ [2] _f_ ( **x** ) _[−]_ [1] _∇f_ ( **x** ) _._


The latter update can be motivated by considering the second-order Taylor
approximation to _f_ around **x** :

_f_ ( **x** + **p** ) _≈_ _f_ ( **x** ) + _∇f_ ( **x** ) [T] **p** + [1]

2 **[p]** [T] _[∇]_ [2] _[f]_ [(] **[x]** [)] **[p]** _[.]_

Observe that when _∇_ [2] _f_ ( **x** ) _≻_ **0** the Newton step **p** := _−∇_ [2] _f_ ( **x** ) _[−]_ [1] _∇f_ ( **x** ) minimizes the right-hand side.
Newton’s method also applies to solving nonlinear equations. Consider the
system of nonlinear equations


_F_ ( **x** ) = **0** (20.5)


where _F_ : R _[n]_ _→_ R _[n]_ is a differentiable function. Let _F_ _[′]_ ( **x** ) denote the _Jacobian_
_matrix_ of _F_, that is, the _n × n_ matrix with ( _i, j_ ) component


_F_ _[′]_ ( **x** ) _ij_ = _[∂f][i]_ [(] **[x]** [)] _,_

_∂xj_


where _f_ 1( **x** ) _, . . ., fn_ ( **x** ) are the components of _F_ ( **x** ).
In its pure form, Newton’s method for (20.5) updates a trial point **x** to the
new point

**x** [+] = **x** _−_ _F_ _[′]_ ( **x** ) _[−]_ [1] _F_ ( **x** ) _._


The latter update can be motivated by considering the first-order Taylor approximation to _F_ around **x** :


_F_ ( **x** + **p** ) _≈_ _F_ ( **x** ) + _F_ _[′]_ ( **x** ) **p** _._


The Newton step **p** = _−F_ _[′]_ ( **x** ) _[−]_ [1] _F_ ( **x** ) makes the above right-hand side equal to
zero.
Observe that Newton’s method for the unconstrained optimization problem
(20.2) is exactly the same as Newton’s method for solving the system of nonlinear
equations _∇f_ ( **x** ) = **0** .
Newton’s method has a much faster rate of convergence than gradient descent
provided the initial iterate is sufficiently close to the solution. On the other
hand, when the initial iterate is far from the solution, the above pure form of
Newton’s method may fail to converge. The latter drawback can be rectified by
performing some backtracking along the Newton step direction as described in
Algorithm 20.3. The step length _αk_ can be chosen via the backtracking procedure


**20.4** **Algorithms** 311


described in Algorithm 20.2 to ensure the Armijo–Goldstein sufficient decrease
condition (20.4) holds. For the Newton direction **d** = _−∇_ [2] _f_ ( **x** _k_ ) _[−]_ [1] _∇f_ ( **x** _[k]_ ), a
natural and customary initial step length at each step is _αk_ = 1.


**Algorithm** **20.3** Newton’s method with backtracking

1: choose **x** [0] _∈_ R _[n]_

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: choose a step length _αk_ _∈_ (0 _,_ 1] via backtracking and set **x** _[k]_ [+1] = **x** _[k]_ _−_
_αk∇_ [2] _f_ ( **x** _[k]_ ) _[−]_ [1] _∇f_ ( **x** _[k]_ )

4: **end** **for**


_Subgradient_ _Method_
In the special case when the objective function _f_ is convex, the gradient descent
method can be extended to _non-smooth_ functions; that is, functions that are
not necessarily differentiable. Non-smooth functions arise often in optimization.
In particular, the Lagrangian relaxation heuristic for (8.9) described in Section
8.3.3 yields the minimization of a non-smooth convex function.
Let _f_ : R _[n]_ _→_ R be a convex function. A point **g** _∈_ R _[n]_ is a _subgradient_ of _f_ at
**x** _∈_ R _[n]_ if for all **y** _∈_ R _[n]_


_f_ ( **y** ) _−_ _f_ ( **x** ) _≥_ **g** [T] ( **y** _−_ **x** ) _._



The _subdifferential_ of _f_ at **x**, denoted _∂f_ ( **x** ), is the set of subgradients of _f_ at **x** .
The subdifferential of a convex function is non-empty at every point. The
following example illustrates the subdifferential of a simple non-smooth function.
Consider the convex function _f_ : R _→_ R defined by _f_ ( _x_ ) = _|x|_ . In this case we
have



1 if _x >_ 0

_−_ 1 if _x <_ 0

[ _−_ 1 _,_ 1] if _x_ = 0 _._



_∂f_ ( _x_ ) =



⎧
⎨


⎩



Algorithm 20.4 describes the subgradient method for (20.2) when _f_ is a convex
function. Observe that it is a natural extension of Algorithm 20.1.


**Algorithm** **20.4** Subgradient method

1: choose **x** [0] _∈_ R _[n]_

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: choose **g** _k_ _∈_ _∂f_ ( **x** _[k]_ ) and a step length _αk_ _>_ 0, and set **x** _[k]_ [+1] = **x** _[k]_ _−_
_αk_ **g** _k_
4: **end** **for**


For non-smooth functions, the choice of step length _αk_ for the subgradient
method cannot be chosen via a backtracking procedure as the Armijo–Goldstein
condition (20.4) cannot be guaranteed in the absence of differentiability. Various


312 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**



choices have been proposed in the literature. The following two generic types of
step lengths are particularly simple and popular. The first one is to choose _fixed_
sizes _αk_ = _α_ _>_ 0 for all _k_ . The second one is to choose slowly diminishing sizes
such that

    - _∞_     - _∞_



_αk_ [2] _[<][ ∞][,]_
_k_ =0




- _∞_



_αk_ = _∞._

_k_ =0



Constrained Case


_Generalized_ _Reduced_ _Gradient_
The main idea behind the _generalized_ _reduced_ _gradient_ method is to reduce a
constrained problem to a sequence of unconstrained problems in a space of
lower dimension. To illustrate this procedure, consider the special case when
the equality constraints are linear:


min _f_ ( **x** )
**x** (20.6)

s.t. **Ax** = **b**



for some **A** _∈_ R _[m][×][n]_ _._ Without loss of generality we may assume that **A** has
full row rank as otherwise either some constraints are redundant or the problem
is infeasible. Since **A** has full rank, we can partition both **A** and **x** as follows:




           **A** = - **A** _B_ **A** _N_ - and **x** = **xx** _NB_




for some subset _B_ _⊆{_ 1 _, . . ., n}_ such that **A** _B_



is non-singular. Therefore


**Ax** = **b** _⇔_ **A** _B_ **x** _B_ + **A** _N_ **x** _N_ = **b** _⇔_ **x** _B_ = **A** _[−]_ _B_ [1][(] **[b]** _[ −]_ **[A]** _[N]_ **[x]** _[N]_ [)] _[.]_


Consequently, problem (20.6) is equivalent to the following _reduced_ _space_ unconstrained minimization problem:


min _f_ ˆ( **x** _N_ )
**x** _N_


where
_f_ ˆ( **x** _N_ ) = _f_ ( **A** _[−]_ _B_ [1][(] **[b]** _[ −]_ **[A]** _[N]_ **[x]** _[N]_ [)] _[,]_ **[ x]** _[N]_ [)] _[.]_


Consider a more general program with nonlinear equality constraints:


min _f_ ( **x** )
**x** (20.7)

s.t. **g** ( **x** ) = **b** _._


We can extend the above approach by approximating the nonlinear equality
constraints with their first-order Taylor approximation. More precisely, suppose
the current point is **x** _[k]_ . Consider the modification of (20.7) obtained by replacing
**g** ( **x** ) = **b** with its first-order Taylor approximation


min _f_ ( **x** )
**x** (20.8)

s.t. **g** ( **x** _[k]_ ) + _∇_ **g** ( **x** _[k]_ ) [T] ( **x** _−_ **x** _[k]_ ) = **b** _._


**20.4** **Algorithms** 313


Observe that the latter problem is of the form (20.6) and is thus amenable to
the type of reduced space approach described above. Algorithm 20.5 describes a
template for a generalized reduced gradient approach to problem (20.7). The step
length _α_ at each iteration is typically chosen to balance both goals of objective
function reduction and constraint satisfaction.


**Algorithm** **20.5** Generalized reduced gradient

1: choose **x** [0]

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve the linearized constraints problem (20.8) to find a search direction
Δ **x** _[k]_

4: choose a step length _α >_ 0 and set **x** _[k]_ [+1] = **x** _[k]_ + _α_ Δ **x** _[k]_

5: **end** **for**


The generalized reduced gradient approach can be extended to deal with
inequality constraints as well via an _active-set_ _approach_ like that discussed in
Chapter 5. The basic idea is that the active inequalities can be treated as equality
constraints. The challenge of course is to determine the correct set of active
inequalities at the optimal solution.


_Sequential_ _Quadratic_ _Programming_
The central idea of _sequential_ _quadratic_ _programming_ is to capitalize on algorithms for quadratic programming to solve more general nonlinear programming
problems of the form (20.1). Given a current iterate **x** _[k]_, problem (20.1) can be
approximated with the following quadratic program:



min **x** _f_ ( **x** _[k]_ ) + _∇f_ ( **x** _[k]_ ) [T] ( **x** _−_ **x** _[k]_ ) + [1] 2




[1]

2 [(] **[x]** _[ −]_ **[x]** _[k]_ [)][T] **[B]** _[k]_ [(] **[x]** _[ −]_ **[x]** _[k]_ [)]



s.t. **g** ( **x** _[k]_ ) + _∇_ **g** ( **x** _[k]_ ) [T] ( **x** _−_ **x** _[k]_ ) = **b** (20.9)
**h** ( **x** _[k]_ ) + _∇_ **h** ( **x** _[k]_ ) [T] ( **x** _−_ **x** _[k]_ ) _≤_ **d** _,_



where

**B** _k_ = _∇_ [2] **xx** _[L]_ [(] **[x]** _[k][,]_ **[ y]** _[k][,]_ **[ s]** _[k]_ [)]


is the Hessian of the Lagrangian function with respect to the **x** variables and
( **y** _[k]_ _,_ **s** _[k]_ ) is the current estimate of the vector of Lagrange multipliers.
Algorithm 20.6 describes a template for a sequential quadratic programming
approach to problem (20.7). Once again, the step length _α_ at each iteration
is typically chosen to balance both goals of objective function reduction and
constraint satisfaction.


_Interior-Point_ _Methods_
Interior-point methods, formerly discussed in Chapters 2 and 5, can be extended
to general nonlinear programming under suitable differentiability conditions. The
gist of the method is to solve the optimality conditions (20.3).


314 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


**Algorithm** **20.6** Sequential quadratic programming

1: choose **x** [0] _,_ **y** [0] _,_ **s** [0]

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve the quadratic program (20.9) to find a search direction
(Δ **x** _[k]_ _,_ Δ **y** _[k]_ _,_ Δ **s** _[k]_ )

4: choose a step length _α >_ 0 and set ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) = ( **x** _[k]_ _,_ **y** _[k]_ _,_ **s** _[k]_ )+
_α_ (Δ **x** _[k]_ _,_ Δ **y** _[k]_ _,_ Δ **s** _[k]_ )

5: **end** **for**



Similar to the linear and quadratic programming cases, interior-point methods
generate a sequence of iterates that satisfy some inequalities strictly and each
iteration of the algorithm aims to make progress towards satisfying the optimality
conditions (20.3). The algorithm inevitably becomes a bit more elaborate for
nonlinear programs because of the nonlinearities in the constraints.
As before we use the following notational convention: given a vector **s** _∈_ R _[p]_,
let **S** _∈_ R _[p][×][p]_ denote the diagonal matrix defined by _Sii_ = _si_, for _i_ = 1 _, . . ., n_,
and let **1** _∈_ R _[p]_ denote the vector whose components are all 1s. The optimality
conditions (20.3) can be restated as
⎡ ⎤ ⎡ ⎤



⎤



⎡

⎢⎢⎣



⎤



_,_ **s** _,_ **z** _≥_ **0** _._
⎥⎥⎦



_∇f_ ( **x** ) + _∇_ **g** ( **x** ) **y** + _∇_ **h** ( **x** ) **s**
**g** ( **x** ) _−_ **b**
**h** ( **x** ) + **z** _−_ **d**
**SZ1**



⎢⎢⎣



=
⎥⎥⎦



**0**
**0**
**0**
**0**



Given _μ_ _>_ 0, let ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **z** ( _μ_ ) _,_ **s** ( _μ_ )) be the solution to the following
perturbed version of the above optimality conditions:
⎡ ⎤ ⎡ ⎤



⎤



⎡

⎢⎢⎣



⎤



_,_ **s** _,_ **z** _>_ **0** _._
⎥⎥⎦



_∇f_ ( **x** ) + _∇_ **g** ( **x** ) **y** + _∇_ **h** ( **x** ) **s**
**g** ( **x** ) _−_ **b**
**h** ( **x** ) + **z** _−_ **d**
**SZ1**



⎢⎢⎣



=
⎥⎥⎦



**0**
**0**
**0**
_μ_ **1**



The first condition above can be written as **r** _μ_ ( **x** _,_ **y** _,_ **z** _,_ **s** ) = **0** for the _residual_
_vector_ :



_∇f_ ( **x** ) + _∇_ **g** ( **x** ) **y** + _∇_ **h** ( **x** ) **s**
**g** ( **x** ) _−_ **b**
**h** ( **x** ) + **z** _−_ **d**
**SZ1** _−_ _μ_ **1**



_._
⎥⎥⎦



⎤



**r** _μ_ ( **x** _,_ **y** _,_ **z** _,_ **s** ) :=



⎡

⎢⎢⎣



The _central_ _path_ is the set _{_ ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **z** ( _μ_ ) _,_ **s** ( _μ_ )) : _μ_ _>_ 0 _}_ . Under suitable
assumptions ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **z** ( _μ_ ) _,_ **s** ( _μ_ )) converges to a local optimal solution to
(20.3). This suggests the following algorithmic strategy: Suppose ( **x** _,_ **y** _,_ **z** _,_ **s** ) is
“near” ( **x** ( _μ_ ) _,_ **y** ( _μ_ ) _,_ **z** ( _μ_ ) _,_ **s** ( _μ_ )) for some _μ >_ 0. Use ( **x** _,_ **y** _,_ **z** _,_ **s** ) to move to a better
point ( **x** [+] _,_ **y** [+] _,_ **z** [+] _,_ **s** [+] ) “near” ( **x** ( _μ_ [+] ) _,_ **y** ( _μ_ [+] ) _,_ **z** ( _μ_ [+] ) _,_ **s** ( _μ_ [+] )) for some _μ_ [+] _< μ_ .
It can be shown that if a point ( **x** _,_ **y** _,_ **z** _,_ **s** ) is on the central path, then the


**20.5** **Estimating** **a** **Volatility** **Surface** 315


corresponding value of _μ_ satisfies **z** [T] **s** = _pμ._ Likewise, given **z** _,_ **s** _>_ **0**, define


_μ_ ( **z** _,_ **s** ) := **[z]** [T] **[s]**

_p_ _[.]_


To move from a current point ( **x** _,_ **y** _,_ **z** _,_ **s** ) to a new point, we use the Newton
step for the nonlinear system of equations **r** _μ_ ( **x** _,_ **y** _,_ **z** _,_ **s** ) = **0** ; that is,


(Δ **x** _,_ Δ **y** _,_ Δ **z** _,_ Δ **s** ) = _−_ **r** _[′]_ _μ_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ z]** _[,]_ **[ s]** [)] _[−]_ [1] **[r]** _[μ]_ [(] **[x]** _[,]_ **[ y]** _[,]_ **[ z]** _[,]_ **[ s]** [)] _[.]_ (20.10)


Algorithm 20.7 presents a template for an interior-point method.


**Algorithm** **20.7** Interior-point method for nonlinear programming

1: choose **x** [0] _,_ **y** [0] and **z** [0] _,_ **s** [0] _>_ 0

2: **for** _k_ = 0 _,_ 1 _, . . ._ **do**

3: solve the Newton system (20.10) for ( **x** _,_ **y** _,_ **z** _,_ **s** ) = ( **x** _[k]_ _,_ **y** _[k]_ _,_ **z** _[k]_ _,_ **s** _[k]_ ) and _μ_ :=
0 _._ 1 _μ_ ( **z** _[k]_ _,_ **s** _[k]_ )

4: choose a step length _α ∈_ (0 _,_ 1] and set ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **z** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) =
( **x** _[k]_ _,_ **y** _[k]_ _,_ **z** _[k]_ _,_ **s** _[k]_ ) + _α_ (Δ **x** _,_ Δ **y** _,_ Δ **z** _,_ Δ **s** )

5: **end** **for**


The step length _α_ in step 4 should be chosen via a backtracking procedure
so that **z** _[k]_ [+1] _,_ **s** _[k]_ [+1] _>_ 0 and the size of **r** _μ_ ( **x** _[k]_ [+1] _,_ **y** _[k]_ [+1] _,_ **z** _[k]_ [+1] _,_ **s** _[k]_ [+1] ) is sufficiently
smaller than **r** _μ_ ( **x** _[k]_ _,_ **y** _[k]_ _,_ **z** _[k]_ _,_ **s** _[k]_ ).


**20.5** **Estimating** **a** **Volatility** **Surface**


We conclude this chapter with a description of nonlinear programming to estimate the volatility surface. The discussion in this section is based on Coleman
et al. (1999a,b).
The Black–Scholes–Merton (BSM) equation for pricing European options is
based on a geometric Brownian motion model for the movements of the underlying security. Namely, one assumes that the underlying security price _St_ at time
_t_ satisfies


_dSt_

= _μdt_ + _σdWt,_ (20.11)
_St_


where _μ_ is the _drift_, _σ_ is the (constant) volatility, and _Wt_ is the standard
Brownian motion. Using this equation and some standard assumptions about
the absence of frictions and arbitrage opportunities, one can derive the BSM
partial differential equation for the value of a European option on this underlying
security. Using the boundary conditions resulting from the payoff structure of the
particular option, one determines the value function for the option. For example,
for the European call and put options with strike _K_ and maturity _T_, we obtain


316 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


the following formulas:


_C_ ( _K, T_ ) = _S_ 0Φ( _d_ 1) _−_ _Ke_ _[−][rT]_ Φ( _d_ 2) _,_ (20.12)

_P_ ( _K, T_ ) = _Ke_ _[−][rT]_ Φ( _−d_ 2) _−_ _S_ 0Φ( _−d_ 1) _,_ (20.13)


where



_d_ 1 = [log(] _[S]_ [0] _[/K]_ [) + (] ~~_√_~~ _[r]_ [ +] _[ σ]_ [2] _[/]_ [2)] _[T]_



~~_√_~~
_d_ 2 = _d_ 1 _−_ _σ_



~~_√_~~
_σ_



_,_
_T_



_T,_



and Φ( _·_ ) is the cumulative distribution function for the standard normal distribution. In the formula _r_ represents the continuously compounded risk-free and
constant interest rate and _σ_ is the volatility of the underlying security that is
assumed to be constant.
The risk-free interest rate _r_, or a reasonably close approximation to it, is often
available, for example from Treasury bill prices in US markets. Therefore, all one
needs to determine the call or put price using these formulas is a reliable estimate
of the volatility parameter _σ_ . Conversely, given the market price for a particular
European call or put, one can uniquely determine the _implied_ _volatility_ of the
underlying security (implied by this option price) by solving the equations above
with the unknown _σ_ .
Empirical evidence against the appropriateness of (20.11) as a model for the
movements of most securities is abundant. Most such studies refute the assumption of a volatility that does not depend on time or underlying price level. Indeed,
studying the prices of options with the same maturity but different strikes,
researchers observed that the implied volatilities for such options exhibited a
“smile” structure, i.e., higher implied volatilities away from the money in both
directions, decreasing to a minimum level as one approaches the at-the-money
option from up or down. This is clearly in contrast with the constant (flat)
implied volatilities one would expect had (20.11) been an appropriate model for
the underlying price process.
There are quite a few models that try to capture the volatility smile, including
stochastic volatility models, jump diffusions, etc. Since these models introduce
non-traded sources of risk, perfect replication via dynamic hedging as in the BSM
approach becomes impossible and the pricing problem is more complicated. An
alternative that is explored in Coleman et al. (1999b) is the one-factor continuous
diffusion model:

_dSt_ = _μ_ ( _St, t_ ) _dt_ + _σ_ ( _St, t_ ) _dWt,_ _t ∈_ [0 _, T_ ] _,_ (20.14)

_St_


where the constant parameters _μ_ and _σ_ of (20.11) are replaced by continuous
and differentiable functions _μ_ ( _St, t_ ) and _σ_ ( _St, t_ ) of the underlying price _St_ and
time _t_ . Here _T_ denotes the end of the fixed time horizon. If the instantaneous
risk-free interest rate _r_ is assumed constant and the dividend rate is constant,


**20.5** **Estimating** **a** **Volatility** **Surface** 317


given a function _σ_ ( _S, t_ ), a European call option with maturity _T_ and strike _K_
has a unique price. Let us denote this price with _C_ ( _σ_ ( _S, t_ ) _, K, T_ ).
While an explicit solution for the price function _C_ ( _σ_ ( _S, t_ ) _, K, T_ ) as in (20.12)
is no longer possible, the resulting pricing problem can be solved efficiently via
numerical techniques. Since _μ_ ( _S, t_ ) does not appear in the generalized BSM
partial differential equation, all one needs is the specification of the function
_σ_ ( _S, t_ ) and a good numerical scheme to determine the option prices in this
generalized framework.
So, how does one specify the function _σ_ ( _S, t_ )? First of all, this function should
be consistent with the observed prices of currently or recently traded options on
the same underlying security. If we assume that we are given market prices of
_m_ call options with strikes _Kj_ and maturities _Tj_ in the form of bid–ask pairs
( _βj, αj_ ) for _j_ = 1 _, . . ., n_, it would be reasonable to require that the volatility
function _σ_ ( _S, t_ ) is chosen so that


_βj_ _≤_ _C_ ( _σ_ ( _S, t_ ) _, Kj, Tj_ ) _≤_ _αj,_ _j_ = 1 _, . . ., n._ (20.15)


To ensure that (20.15) is satisfied as closely as possible, one strategy is to
minimize the violations of the inequalities in (20.15):



min
_σ_ ( _S,t_ ) _∈H_




- _n_

[ _βj_ _−_ _C_ ( _σ_ ( _S, t_ ) _, Kj, Tj_ )] [+] + [ _C_ ( _σ_ ( _S, t_ ) _, Kj, Tj_ ) _−_ _αj_ ] [+] _._ (20.16)

_j_ =1



Above, _H_ denotes the space of measurable functions _σ_ ( _S, t_ ) with domain R+ _×_

[0 _, T_ ] and [ _u_ ] [+] = max _{u,_ 0 _}_ . Alternatively, using the closing prices _Cj_ for the
options under consideration, or choosing the mid-market prices _Cj_ = ( _βj_ + _αj_ ) _/_ 2,
we can solve the following nonlinear least-squares problem:



min
_σ_ ( _S,t_ ) _∈H_




- _n_

( _C_ ( _σ_ ( _S, t_ ) _, Kj, Tj_ ) _−_ _Cj_ ) [2] _._ (20.17)

_j_ =1



This is a nonlinear least-squares problem since the function _C_ ( _σ_ ( _S, t_ ) _, Kj, Tj_ )
depends nonlinearly on the variables, namely the local volatility function _σ_ ( _S, t_ ).
While the calibration of the local volatility function to the observed prices
using the objective functions in (20.16) and (20.17) is important and desirable,
there are additional properties that are desirable in the local volatility function.
The most common feature sought in existing models is regularity or smoothness.
For example, in Lagnado and Osher (1997) the authors try to achieve a smooth
volatility function by modifying the objective function in (20.17) as follows:



min
_σ_ ( _S,t_ ) _∈H_




- _n_

( _C_ ( _σ_ ( _S, t_ ) _, Kj, Tj_ ) _−_ _Cj_ ) [2] + _λ∥∇σ_ ( _S, t_ ) _∥_ 2 _._ (20.18)

_j_ =1



Here, _λ_ is a positive tradeoff parameter and _∥· ∥_ 2 represents the _L_ [2] -norm in _H_ .
Large deviations in the volatility function would result in a high value for the
norm of the gradient function, and by penalizing such occurences, the formulation
above encourages a smoother solution to the problem. The most appropriate


318 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


value for the tradeoff parameter _λ_ must be determined experimentally. To solve
the resulting problem numerically, one must discretize the volatility function on
the underlying price and time grid. Even for a relatively coarse discretization of
the _St_ and _t_ spaces, one can easily end up with an optimization problem with
many variables.
An alternative strategy is to build the smoothness into the volatility function
by modeling it with spline functions. The use of the spline functions not only
guarantees the smoothness of the resulting volatility function estimates but
also reduces the degrees of freedom in the problem. As a consequence, the
optimization problem to be solved has many fewer variables and is easier. This
strategy is proposed in Coleman et al. (1999b) and we review it below.
We start by assuming that _σ_ ( _S, t_ ) is a bi-cubic spline. While higher-order
splines can also be used, cubic splines often offer a good balance between flexibility and complexity. Next we choose a set of spline knots at points ( _S_ [¯] _i,_ _t_ [¯] _i_ )
for _i_ = 1 _, . . ., k_ . If the value of the volatility function at these points is given
by _σ_ ¯ _j_ := _σ_ ( _S_ [¯] _j,_ _t_ [¯] _j_ ), the interpolating cubic spline that goes through these knots
and satisfies a particular end condition (such as the natural spline end condition
of linearity at the boundary knots) is uniquely determined. In other words, to
completely determine the volatility function as a natural bi-cubic spline (and
therefore to determine the resulting call option prices) we have _k_ degrees of
freedom represented with the choices _σ_ ¯ = (¯ _σ_ 1 _, . . .,_ ¯ _σk_ ). Let Σ( _S, t,_ ¯ _σ_ ) be the
bi-cubic spline local volatility function obtained by setting _σ_ ( _S_ [¯] _j,_ _t_ [¯] _j_ ) := _σ_ ¯ _j_ . Let
_C_ (Σ( _S, t,_ ¯ _σ_ ) _, S, t_ ) denote the resulting call price function. Then the analog of the
objective function (20.17) is



min
_σ_ ¯ _∈_ R _[k]_




- _n_

( _C_ (Σ( _S, t,_ ¯ _σ_ ) _, Kj, Tj_ ) _−_ _Cj_ ) [2] _._ (20.19)

_j_ =1



One can introduce positive weights _wj_ for each of the terms in the objective
function above to address different accuracies or confidence in the call prices
_Cj_ . One can also introduce lower and upper bounds _li_ and _ui_ for the volatilities
at each knot to incorporate additional information that may be available from
historical data, etc. This way, we form the following nonlinear least-squares
problem with _k_ variables:



_σ_ ¯min _∈_ R _[k]_ _[f]_ [(] _[σ]_ [) :=]




- _n_

_wj_ ( _C_ (Σ( _S, t,_ ¯ _σ_ ) _, Kj, Tj_ ) _−_ _Cj_ ) [2] (20.20)

_j_ =1



s.t. _l ≤_ _σ_ ¯ _≤_ _u._


It should be noted that the formulation above will not be appropriate if there
are many more knots than prices, that is, if _k_ is much larger than _n_ . In this case,
the problem will be underdetermined and solutions may exhibit “overfitting”.
There should be fewer knots than available option prices.
The problem (20.20) is a standard nonlinear optimization problem except that
the objective function _f_ (¯ _σ_ ) and in particular the function _C_ (Σ( _S, t,_ ¯ _σ_ ) _, Kj, Tj_ )


**20.6** **Exercises** 319


depends on the decision variables _σ_ ¯ in a complicated and non-explicit manner.
Since most of the nonlinear optimization methods we discussed in the previous
section require at least the gradient of the objective function (and sometimes its
Hessian matrix as well), this may sound alarming. Without an explicit expression
for _f_, its gradient must be estimated either using a finite difference scheme or
using automatic differentiation. Coleman et al. (1999b) implement both alternatives and report that local volatility functions can be estimated very accurately
using these strategies. They also test the hedging accuracy of different deltahedging strategies, one using a constant volatility estimation and another using
the local volatility function produced by the strategy above. These tests indicate
that the hedges obtained from the local volatility function are significantly more
accurate.


**20.6** **Exercises**


**Exercise** **20.1** Suppose _f_ : R _[n]_ _→_ R is a differentiable function at the point
**x** _∈_ R _[n]_ . Consider the first-order Taylor approximation to _f_ around **x** :


_f_ ˆ( **p** ) := _f_ ( **x** ) + _∇f_ ( **x** ) [T] **p** _._


Show that if _∇f_ ( **x** ) _̸_ = **0** then the solution to the problem


min _f_ ˆ( **p** )
_∥_ **p** _∥≤_ 1


is

1
**p** _[∗]_ = _−_
_∥∇f_ ( **x** ) _∥_ _[∇][f]_ [(] **[x]** [)] _[.]_


In other words, it is the unitary vector in the direction of negative gradient.


**Exercise** **20.2**


(a) Let **A** _∈_ R _[m][×][n]_, **b** _∈_ R _[m]_, **c** _∈_ R _[n]_ . Show that the mixed binary program


min **c** [T] **x**
s.t. **Ax** _≤_ **b**
_xj_ _∈{_ 0 _,_ 1 _},_ _j_ _∈_ _J_


is equivalent to the nonlinear program


min **c** [T] **x**
s.t. **Ax** _≤_ **b**
_xj_ (1 _−_ _xj_ ) = 0 _,_ _j_ _∈_ _J._


(b) Let **A** _∈_ R _[m][×][n]_, **b** _∈_ R _[m]_, **c** _∈_ R _[n]_ . Show that the mixed integer program


min **c** [T] **x**
s.t. **Ax** _≤_ **b**
_xj_ _∈_ Z _,_ _j_ _∈_ _J_


320 **Nonlinear** **Programming:** **Theory** **and** **Algorithms**


is equivalent to the nonlinear program


min **c** [T] **x**
s.t. **Ax** _≤_ **b**
sin( _πxj_ ) = 0 _,_ _j_ _∈_ _J._


**Exercise** **20.3** Let _n_ be a positive integer. Show that for suitable differentiable
functions _f,_ **g** _,_ **h** the statement


“There exist _x, y, z_ _∈_ Z all different such that _x_ _[n]_ + _y_ _[n]_ = _z_ _[n]_ _._ ”


can be equivalently stated as


“The optimal value of


min _f_ ( **x** )
s.t. **g** ( **x** ) _≤_ **0**
**h** ( **x** ) = **0**


is zero.”


What does that suggest about the difficulty of solving generic nonlinear programming problems?


## **Appendices**


## Appendix Basic Mathematical Facts

**A.1** **Matrices** **and** **Vectors**


For two positive integers _m_ and _n_, let R _[m][×][n]_ denote the space of _m × n_ matrices
with real entries. The _transpose_ of an _m × n_ matrix



⎤

_a_ 11 _a_ 12 _. . ._ _a_ 1 _n_
_a_ 21 _a_ 22 _. . ._ _a_ 2 _n_

_∈_ R _m×n_

... ... ... ... ⎥⎥⎥⎦
_am_ 1 _am_ 2 _. . ._ _amn_



**A** =



⎡

⎢⎢⎢⎣



is the _n × m_ matrix


**A** [T] =



⎡

⎢⎢⎢⎣



⎤

_a_ 11 _a_ 21 _. . ._ _am_ 1
_a_ 12 _a_ 22 _. . ._ _am_ 2

_∈_ R _n×m._

... ... ... ... ⎥⎥⎥⎦
_a_ 1 _n_ _a_ 2 _n_ _. . ._ _amn_



A square matrix **A** _∈_ R _[n][×][n]_ is _symmetric_ if **A** [T] = **A** .
The product of two matrices **A** = ( _aik_ ) _∈_ R _[m][×][n]_ and **B** = ( _bkj_ ) _∈_ R _[n][×][p]_ is the
matrix **C** = **AB** = ( _cij_ ) _∈_ R _[m][×][p]_ defined componentwise as follows:


    - _n_



_cij_ =



_aikbkj,_ _i_ = 1 _, . . ., m,_ _j_ = 1 _, . . ., p._

_k_ =1



Observe that the matrix product **AB** is well defined if the number of columns
of **A** and the number of rows of **B** match.
The identity matrix **I** _∈_ R _[n][×][n]_ is the matrix with components equal to 1 on the
diagonal and all other components equal to 0. Observe that for all **A** _∈_ R _[m][×][n]_,
**B** _∈_ R _[n][×][p]_ we have **AI** = **A** and **IB** = **B** . If **A** _,_ **B** _∈_ R _[n][×][n]_ and **AB** = **BA** = **I**,
then we say that **B** is the _inverse_ of **A** and write **B** = **A** _[−]_ [1] .
The following kinds of matrix–vector products arise often. Suppose



⎤


_,_ **Q** :=
⎥⎥⎥⎦



⎡

⎢⎢⎢⎣



⎡

⎢⎢⎢⎣



_q_ 11 _q_ 12 _· · ·_ _q_ 1 _n_
_q_ 12 _q_ 22 _· · ·_ _q_ 2 _n_
... ... ... ...
_q_ 1 _n_ _q_ 2 _n_ _· · ·_ _qnn_



_x_ 1
_x_ 2
...
_xn_



⎤


_,_ **x** :=
⎥⎥⎥⎦



⎤


_._
⎥⎥⎥⎦



**c** :=



⎡

⎢⎢⎢⎣



_c_ 1
_c_ 2
...
_cn_


324 **Basic** **Mathematical** **Facts**


Then


                  -                   **c** [T] **x** = _c_ 1 _· · ·_ _cn_



⎡

_x_ 1

⎢⎣ ...

_xn_



⎤

⎥⎦ = _c_ 1 _x_ 1 + _· · ·_ + _cnxn_



and


So



_q_ 11 _· · ·_ _q_ 1 _n_
... ... ...
_q_ 1 _n_ _· · ·_ _qnn_



⎡

⎢⎣



⎡

⎢⎣



_x_ 1
...
_x_ 3



_q_ 11 _x_ 1 + _· · ·_ + _q_ 1 _nxn_
...
_q_ 1 _nx_ 1 + _· · ·_ + _qnnxn_



⎤

⎥⎦



⎤

⎥⎦ _._



⎤

⎥⎦ =



**Qx** =



⎡

⎢⎣



_q_ 11 _x_ 1 + _· · ·_ + _q_ 1 _nxn_
...
_q_ 1 _nx_ 1 + _· · ·_ + _qnnxn_



⎤

⎥⎦




     -      **x** [T] **Qx** = _x_ 1 _· · ·_ _xn_



⎡

⎢⎣




- _n_

_qijxixj_

_j_ =1



=




- _n_


_i_ =1



= _q_ 11 _x_ [2] 1 [+] _[ · · ·]_ [ +] _[ q][nn][x]_ _n_ [2] [+ 2] _[q]_ [12] _[x]_ [1] _[x]_ [2] [+ 2] _[q]_ [23] _[x]_ [2] _[x]_ [3] [+] _[ · · ·]_ [ + 2] _[q][n][−]_ [1] _[,n][x][n][−]_ [1] _[x][n][.]_


A symmetric matrix **M** _∈_ R _[n][×][n]_ is _positive_ _semidefinite_ if **x** [T] **Mx** _≥_ 0 for all
**x** _∈_ R _[n]_ and it is _positive_ _definite_ if it satisfies the stronger condition **x** [T] **Mx** _>_ 0
for all non-zero **x** _∈_ R _[n]_ .


**A.2** **Convex** **Sets** **and** **Convex** **Functions**


A set _S_ _⊆_ R _[n]_ is _convex_ if for all **x** _,_ **y** _∈_ _S_ the straight segment joining **x** and **y**
is contained in _S_ ; that is,


[ **x** _,_ **y** ] := _{λ_ **x** + (1 _−_ _λ_ ) **y** : _λ ∈_ [0 _,_ 1] _} ⊆_ _S._


The following are types of convex sets that appear often in optimization models.
It is easy to verify that they are indeed convex sets.


_Half-space_ : Given a non-zero **a** _∈_ R _[n]_ and _b ∈_ R the half-space


_{_ **x** _∈_ R _[n]_ : **a** [T] **x** _≤_ _b}_


is convex.


sets, _Intersections_ their intersection _of_ _convex_ [�] _setsi∈I_ : _[S][i]_ Given [is] [a] [convex] a collection [set.] _Si_ _⊆_ R _[n]_, for _i_ _∈_ _I_, of convex


**A.3** **Calculus** **of** **Variations:** **the** **Euler** **Equation** 325


_Affine_ _images_ _and_ _preimages_ : Given a convex set _S_ _⊆_ R _[n]_, matrices **A** _∈_ R _[m][×][n]_,
**B** _∈_ R _[n][×][p]_ and vectors **a** _∈_ R _[m]_, **b** _∈_ R _[n]_, the sets


**A** ( _S_ ) + **a** = _{_ **Ax** + **a** : **x** _∈_ _S} ⊆_ R _[m]_


and


**B** _[−]_ [1] ( _S_ + **b** ) := _{_ **v** _∈_ R _[p]_ : **Bv** _−_ **b** _∈_ _S} ⊆_ R _[p]_


are convex.


Suppose _S_ _⊆_ R _[n]_ is a convex set. A function _f_ : _S_ _→_ R is _convex_ if, for all
**x** _,_ **y** _∈_ _S_ and _λ ∈_ [0 _,_ 1],


_f_ ( _λ_ **x** + (1 _−_ _λ_ ) **y** ) _≤_ _λf_ ( **x** ) + (1 _−_ _λ_ ) _f_ ( **y** ) _._


A common way of dealing with the domain of a function is to consider _extended_
_valued_ functions; that is, functions defined on the whole space R _[n]_ and allowed to
take the value _∞._ The _domain_ of an extended valued function _f_ : R _[n]_ _→_ R _∪{∞}_
is the set

dom( _f_ ) := _{_ **x** _∈_ R _[n]_ : _f_ ( **x** ) _< ∞}._


An alternative and equivalent definition of convexity is the following. An
extended valued function _f_ : R _[n]_ _→_ R _∪{∞}_ is _convex_ if the set


epigraph( _f_ ) := _{_ ( **x** _, t_ ) _∈_ R _[n]_ [+1] : _f_ ( **x** ) _≤_ _t}_


is convex. Observe that if _f_ is convex, then its domain is a convex set. Furthermore, if _f_ is convex then for all _ℓ_ _∈_ R the _sublevel_ set _{_ **x** _∈_ R _[n]_ : _f_ ( **x** ) _≤_ _ℓ}_ is a
convex set.
The following relationship between differentiability and convexity is particularly useful to verify that functions are convex.


**Theorem** **A.1** _Suppose_ _f_ : _S_ _→_ R _is_ _twice_ _differentiable_ _on_ _the_ _open_ _set_
_S_ _⊆_ R _[n]_ _and_ _C_ _⊆_ _S_ _is_ _a_ _convex_ _set._ _Then_ _f_ _is_ _convex_ _on_ _C_ _if_ _and_ _only_ _if_ _∇_ [2] _f_ ( **x** )
_is_ _positive_ _semidefinite_ _for_ _all_ **x** _∈_ _C._


As an immediate consequence of Theorem A.1 it follows that every affine
function _f_ ( **x** ) = **c** [T] **x** + _b_ is convex. It also follows that a quadratic function

_f_ ( **x** ) = [1]

2 **[x]** [T] **[Qx]** [ +] **[ c]** [T] **[x]** [ +] _[ b]_


is convex if and only if **Q** is positive semidefinite.


**A.3** **Calculus** **of** **Variations:** **the** **Euler** **Equation**


The calculus of variations is the analog of calculus that works with functionals rather than functions. Functionals are often integrals of functions. Many
problems in the calculus of variations arose from the need to find a function


326 **Basic** **Mathematical** **Facts**


that optimizes a given functional. The _Euler_ _equation_ for the minimization of
a functional subject to boundary conditions is a kind of first-order optimality
condition for the problem

            - _T_



min
_x_



_L_ ( _t, x_ ( _t_ ) _,_ _x_ ˙ ( _t_ )) _dt,_ _x_ (0) = _x_ 0 _,_ _x_ ( _T_ ) = _xT ._
0



The optimal solution _x_ _[∗]_ ( _t_ ) must satisfy the differential equation

_Lx_ = _[d]_ (A.1)

_dt_ _[L][x]_ [ ˙] _[.]_


Equation (A.1) is called the _Euler_ _equation_ . For a derivation of this optimality
condition as well as a detailed discussion on the interesting subject of calculus
of variations, see Fleming and Rishel (1975).


### **References**

Alizadeh F. (1991). _Combinatorial Optimization with Interior Point Methods and_
_Semi-definite_ _Matrices_ . PhD thesis, University of Minnesota.
Almgren R. and N. Chriss (2000). Optimal execution of portfolio transactions.
_Journal_ _of_ _Risk_, 3:5–39.
Almgren R., C. Thum, E. Hauptmann, and H. Li (2005). Direct estimation of
equity market impact. _Risk_, 18:58-62.
Andersson F., H. Mausser, D. Rosen, and S. Uryasev (2001). Credit risk optimization with conditional value-at-risk criterion. _Mathematical_ _Programming_,
89:273-291.
Artzner P., F. Delbaen, J. Eber, and D. Heath (1999). Coherent measures of risk.
_Mathematical_ _Finance_, 9:203–228.
Back K. (2010). _Asset_ _Pricing_ _and_ _Portfolio_ _Choice_ _Theory_ . Oxford University
Press.
Basel Committee on Banking Supervision (2011). Basel III: A Global Regulatory
Framework for More Resilient Banks and Banking Systems. Technical Report,
Bank for International Settlements.
Bawa V.S., S.J. Brown, and R.W. Klein (1979). _Estimation_ _Risk_ _and_ _Optimal_
_Portfolio_ _Choice_ . North-Holland.
Bellman R. (1954). The theory of dynamic programming. _Bulletin_ _of_ _the_
_American_ _Mathematical_ _Society_, 60:503–515.
Bellman R. (1957). _Dynamic_ _Programming_ . Princeton University Press.
Ben-Tal A. and A. Nemirovski (1998). Robust convex optimization. _Mathematics_
_of_ _Operations_ _Research_, 23(4):769–805.
Ben-Tal A. and A. Nemirovski (2002). Robust optimization - methodology and
applications. _Mathematical_ _Programming_, 92(3):453–480.
Ben-Tal A., L. El Ghaoui, and A. Nemirovski (2009). _Robust_ _Optimization_ .
Princeton University Press.
Bertsekas D. (1999). _Nonlinear_ _Programming_ . Athena Scientific.
Bertsekas D. (2005). _Dynamic_ _Programming_ _and_ _Optimal_ _Control_ . Athena
Scientific.
Bertsimas D. and A. Lo (1998). Optimal control of execution costs. _Journal_ _of_
_Financial_ _Markets_, 1:1–50.
Bertsimas D. and J. Tsitsiklis (1997). _Introduction_ _to_ _Linear_ _Optimization_ .
Athena Scientific.


328 **References**


Bertsimas D., V. Gupta, and I.Ch. Paschalidis (2012). Inverse optimization: a
new perspective on the Black–Litterman model. _Operations_ _Research_, 1389–
1403.
Birge J. and F. Louveaux (1997). _Introduction_ _to_ _Stochastic_ _Programming_ .
Springer.
Black F. and R. Litterman (1992). Global portfolio optimization. _Financial_
_Analysts_ _Journal_, 48:28–43.
Black F. and M. Scholes (1973). The pricing of options and corporate liabilities.
_Journal_ _of_ _Political_ _Economy_, 81:637–659.
Blume M. (1975). Betas and the regression tendencies. _Journal_ _of_ _Finance_,
30:785–795.
Boyd S. and L. Vandenberghe (2004). _Convex_ _Optimization_ . Cambridge University Press.
Brinson G., B. Singer, and G. Beebower (1991). Determinants of portfolio
performance. _Financial_ _Analysts_ _Journal_, 47:40–48.
Broadie M. (1993). Computing efficient frontiers using estimated parameters.
_Annals_ _of_ _Operations_ _Research_, 45(1):21–58.
Campbell J., A. Lo, and A. MacKinlay (1997). _The_ _Econometrics_ _of_ _Financial_
_Markets_ . Princeton University Press.
Cari˜no D., T. Kent, D. Myers, C. Stacy, M. Sylvanus, A. Turner, K. Watanabe,
and W. Ziemba (1994). The Russell–Yasuda Kasai model: an asset/liability
model for a Japanese insurance company using multistage stochastic programming. _Interfaces_, 24(1):29–49.
Ceria S. and R. Stubbs (2006). Incorporating estimation errors into portfolio
selection: robust portfolio selection. _Journal_ _of_ _Asset_ _Management_, 7:109–127.
Choueifaty Y. and Y. Coignard (2008). Toward maximum diversification. _Journal_
_of_ _Portfolio_ _Management_, 40–51.
Chv´atal V. (1983). _Linear_ _Programming_ . W.H. Freeman.
Coleman T.F., Y. Kim, Y. Li, and A. Verma (1999a). Dynamic Hedging in a
Volatile Market. Technical Report, Cornell Theory Center.
Coleman T.F., Y. Kim, Y. Li, and A. Verma (1999b). Reconstructing the
unknown volatility function. _Journal_ _of_ _Computational_ _Finance_, 2:77–102.
Conforti M., G. Cornu´ejols, and G. Zambelli (2014). _Integer_ _Programming_ .
Springer.
Connor G. (1995). The three types of factor models: a comparison of their
explanatory power. _Financial_ _Analysts_ _Journal_, 51:42–46.
Constantinides G. (1983). Capital market equilibrium with personal tax. _Econo-_
_metrica_, 51:611–636.
Constantinides G. (1984). Optimal stock trading with personal taxes: implications for prices and the abnormal January returns. _Journal_ _of_ _Financial_
_Economics_, 13:65–89.
Cornu´ejols G., M. Fisher, and G. Nemhauser (1977). Location of bank accounts
to minimize float: an analytical study of exact and approximate algorithms.
_Management_ _Science_, 23:229–263.


**References** 329


Cox J., S. Ross, and M. Rubinstein (1979). Option pricing: a simplified approach.
_Journal_ _of_ _Financial_ _Economics_, 7:229–263.
Dammon R., C. Spatt, and H. Zhang (2001). Optimal consumption and
investment with capital gains taxes. _Review_ _of_ _Financial._ _Studies_, 14:583–616.
Dammon R., C. Spatt, and H. Zhang (2004). Optimal asset location and allocation with taxable and tax-deferred investing. _Journal of Finance_, 59:999–1038.
Dantzig G. (1963). _Linear_ _Programming_ _and_ _Extensions_ . Princeton University
Press.
Dantzig G. (1990). The diet problem. _Interfaces_, 20(4):43–47.
Dantzig G., R. Fulkerson, and S. Johnson (1954). Solution of a large-scale
traveling-salesman problem. _Operations_ _Research_, 2:393–410.
Davarnia D. and G. Cornu´ejols (2017). From estimation to optimization via
shrinkage. _Operations_ _Research_ _Letters_, 45:642–646.
De Vries S. and R. Vohra (2003). Combinatorial auctions: a survey. _INFORMS_
_Journal_ _on_ _Computing_, 15(3):284–309.
Duffie D. (2001). _Dynamic_ _Asset_ _Pricing_ _Theory_ . Princeton University Press.
Efron B. and C. Morris (1977). Stein’s paradox in statistics. _Scientific_ _American_,
236:119–127.
El Ghaoui L. and H. Lebret (1997). Robust solutions to least-squares problems
with uncertain data. _SIAM_ _Journal_ _on_ _Matrix_ _Analysis_ _and_ _Applications_,
18(4):1035–1064.
El Ghaoui L., F. Oustry, and H. Lebret (1998). Robust solutions to uncertain
semidefinite programs. _SIAM_ _Journal_ _on_ _Optimization_, 9(1):33–52.
Engle R. (1982). Autoregressive conditional heteroscedasticity with estimates of
the variance of United Kingdom inflation. _Econometrica,_ 50:987–1007.
Fabozzi F. (2004). _Bonds,_ _Markets,_ _Analysis_ _and_ _Strategies_, fifth edition.
Prentice-Hall.
Fabozzi F., P. Kolm, D. Pachamanova, and S. Focardi (2007). _Robust_ _Portfolio_
_Optimization_ _and_ _Management_ . Wiley.
Fama E. and K. French (1992). The cross-section of expected stock returns.
_Journal_ _of_ _Finance_, 67:427–465.
Fleming W. and R. Rishel (1975). _Deterministic and Stochastic Optimal Control_ .
Springer.
Friedman J., T. Hastie, and R. Tibshirani (2001). _The_ _Elements_ _of_ _Statistical_
_Learning_, volume 1. Springer.
Gˆarleanu N. and L. Pedersen (2013). Dynamic trading with predictable returns
and transaction costs. _Journal_ _of_ _Finance_, 68(6):2309–2340.
Goldfarb D. and G. Iyengar (2003). Robust portfolio selection problems.
_Mathematics_ _of_ _Operations_ _Research_, 28(1):1–38.
Gomory R.E. (1958). Outline of an algorithm for integer solutions to linear
programs. _Bulletin_ _of_ _the_ _American_ _Mathematical_ _Society_, 64:275–278.
Gomory R.E. (1960). An Algorithm for the Mixed Integer Problem. Technical
Report RM-2597, The Rand Corporation.


330 **References**


Gondzio J. and R. Kouwenberg (2001). High performance for asset liability
management. _Operations_ _Research_, 49:879–891.

Grinold R. and R. Kahn (1999). _Active_ _Portfolio_ _Management:_ _A_ _Quantitative_
_Approach for Producing Superior Returns and Controlling Risk_, second edition.
McGraw-Hill.

G¨uler O. (2010). _Foundations_ _of_ _Optimization_ . Springer.

Halld´orsson B. and R. T¨ut¨unc¨u (2003). An interior-point method for a class
of saddle-point problems. _Journal_ _of_ _Optimization_ _Theory_ _and_ _Applications_,
116(3):559–590.

Harrison J. and D. Kreps (1979). Martingales and arbitrage in multiperiod
security markets. _Journal_ _of_ _Economic_ _Theory_, 20:381–408.

Harrison J. and S. Pliska (1981). Martingales and stochastic integrals in the
theory of continuous trading. _Stochastic_ _Processes_ _and_ _their_ _Applications_,
11:215–260.

Heath D., R. Jarrow, and A. Morton (1992). Bond pricing and the term
structure of interest rates: a new methodology for contingent claims
valuation. _Econometrica_, 60:77–105.

Herzel S. (2005). Arbitrage opportunities on derivatives: a linear programming
approach. _Dynamics of Continuous, Discrete and Impulsive Systems. Series B:_
_Applications_ _and_ _Algorithms_, 12:589–606.

Hodges S. and S. Schaefer (1977). A model for bond portfolio improvement.
_Journal_ _of_ _Financial_ _and_ _Quantitative_ _Analysis_, 12:243–260.

Hoyland K. and S.W. Wallace (2001). Generating scenario trees for multistage
decision problems. _Management_ _Science_, 47:295–307.

Jorion P. (1986). Bayes–Stein estimation for portfolio analysis. _Journal_ _of_
_Financial_ _and_ _Quantitative_ _Analysis_, 21:279–292.

Jorion P. (1992). Portfolio optimization in practice. _Financial_ _Analysts_ _Journal_,
48:68–74.

Jorion P. (2003). Portfolio optimization with tracking-error constraints.
_Financial_ _Analysts_ _Journal_, 59:70–82.

Karmarkar N. (1984). A new polynomial time algorithm for linear programming.
_Combinatorica_, 4:373–395.

Kelly J.L. (1956). A new interpretation of information rate. _Bell_ _System_
_Technical_ _Journal_, 35:917–926.

Klaassen P. (2002). Comment on “Generating scenario trees for multistage
decision problems”. _Management_ _Science_, 48:1512–1516.

Kocuk B. and G. Cornu´ejols (2017). Incorporating Black–Litterman Views
in Portfolio Construction When Stock Returns Are a Mixture of Normals.
Technical Report, Carnegie–Mellon University, Pittsburgh.

Konno H. and H. Yamazaki (1991). Mean-absolute deviation portfolio optimization model and its applications to Tokyo stock market. _Management_ _Science_,
37(5):519–531.


**References** 331


Kouwenberg R. (2001). Scenario generation and stochastic programming models
for asset liability management. _European_ _Journal_ _of_ _Operational_ _Research_,
134:279–292.
Kritzman M. (2002). _Puzzles_ _of_ _Finance:_ _Six_ _Practical_ _Problems_ _and_ _their_
_Remarkable_ _Solutions_ . Wiley.
Lagnado R. and S. Osher (1997). Reconciling differences. _Risk_, 10:79–83.
Land A.H. and A.G. Doig (1960). An automatic method of solving discrete
programming problems. _Econometrica_, 28:497–520.
Ledoit O. and M. Wolf (2003). Improved estimation of the covariance matrix of
stock returns with an application to portfolio selection. _Journal_ _of_ _Empirical_
_Finance_, 10:602–621.
Ledoit O. and M. Wolf (2004). A well-conditioned estimator for large-dimensional
covariance matrices. _Journal_ _of_ _Multivariate_ _Analysis_, 88:365–411.
Lintner J. (1965). The valuation of risk assets and the selection of risky
investments in stock portfolios and capital budgets. _Review_ _of_ _Economics_ _and_
_Statistics_, 47:13–37.
Litterman B. (2003). _Modern_ _Investment_ _Management:_ _An_ _Equilibrium_
_Approach_ . Wiley.
Markowitz H. (1952). Portfolio selection. _Journal_ _of_ _Finance_, 7:77–91.
Merton R. (1973). Theory of rational option pricing. _Bell_ _Journal_ _of_ _Economics_
_and_ _Management_ _Science_, 4:141–183.
Meucci A. (2005). _Risk_ _and_ _Asset_ _Allocation_ . Springer.
Meucci A. (2010). Return calculations for leveraged securities and portfolios.
_GARP_ _Risk_ _Professional_, October:40–43.
Michaud R. and R. Michaud (2008). _Efficient_ _Asset_ _Management_ . Oxford
University Press.
Mossin J. (1966). Equilibrium in a capital asset market. _Econometrica_,
34:768–783.
Nesterov Y. (2004). _Introductory_ _Lectures_ _on_ _Convex_ _Optimization:_ _A_ _Basic_
_Course_ . Kluwer Academic.
Nesterov Y. and A. Nemirovskii (1994). _Interior-Point_ _Polynomial_ _Algorithms_
_in_ _Convex_ _Programming_ . SIAM.
Nesterov Y. and M. Todd (1997). Self-scaled barriers and interior-point methods
for convex programming. _Mathematics_ _of_ _Operations_ _Research_, 22:1–42.
Nesterov Y. and M. Todd (1998). Primal–dual interior-point methods for
self-scaled cones. _SIAM_ _Journal_ _on_ _Optimization_, 8:324–364.
Nocedal J. and S. Wright (2006). _Numerical_ _Optimization_ . Springer.
Padberg M. and G. Rinaldi (1987). Optimization of a 532-city symmetric traveling salesman problem by branch and cut. _Operations_ _Research_ _Letters_, 6:1–7.
P´erold A. (1988). The implementation shortfall: paper versus reality. _Journal_ _of_
_Portfolio_ _Management_, 14:4–9.
Pokutta S. and C. Schmaltz (2012). Optimal bank planning under Basel III
regulations. _Capco_ _Institute_ _Journal_ _of_ _Financial_ _Transformation_, 34:165–174.


332 **References**


Porteus E. (2002). _Foundations_ _of_ _Stochastic_ _Inventory_ _Theory_ . Stanford University Press.
Poundstone W. (2005). _Fortune’s_ _Formula:_ _The_ _Untold_ _Story_ _of_ _the_ _Scientific_
_Betting_ _System_ _that_ _Beat_ _the_ _Casinos_ _and_ _Wall_ _Street_ . Hill and Wang.
Ragsdale C. (2007). _Spreadsheet_ _Modeling_ _&_ _Decision_ _Analysis:_ _A_ _Practical_
_Introduction_ _to_ _Management_ _Science_, fifth edition. Thomson South-Western.
Renegar J. (2001). _A_ _Mathematical_ _View_ _of_ _Interior-Point_ _Methods_ _in_ _Convex_
_Optimization_ . SIAM.
Rockafellar T. and S. Uryasev (2000). Optimization of conditional value-at-risk.
_Journal_ _of_ _Risk_, 2:21–41.
Ronn E. I. (1987). A new linear programming approach to bond portfolio
management. _Journal_ _of_ _Financial_ _and_ _Quantitative_ _Analysis_, 22:439–466.
Roos C., T. Terlaky, and J.-Ph. Vial (2005). _Interior_ _Point_ _Methods_ _for_ _Linear_
_Optimization_, second edition. Springer.
Rosenberg B. (1974). Extra-market components of covariance in security returns.
_Journal_ _of_ _Financial_ _and_ _Quantitative_ _Analysis_, 9(2):263–274.
Ross S. (1976). The arbitrage theory of capital asset pricing. _Journal_ _of_
_Economic._ _Theory_, 13:341–360.
Rustem B. and M. Howe (2002). _Algorithms_ _for_ _Worst-Case_ _Design_ _and_
_Applications_ _to_ _Risk_ _Management_ . Princeton University Press.
Schaefer S.M. (1982). Tax induced clientele effects in the market for British
government securities. _Journal_ _of_ _Financial_ _Economics_, 10:121–159.
Scherer B. (2002). Portfolio resampling: review and critique. _Financial_ _Analysts_
_Journal_, 58:98–109.
Scherer B. (2007). Can robust portfolio optimization help to build better
portfolios? _Journal_ _of_ _Asset_ _Management_, 7:374–387.
Schmieta S. and F. Alizadeh (2001). Associative and Jordan algebras, and
polynomial time interior-point algorithms for symmetric cones. _Mathematics_
_of_ _Operations_ _Research_, 26(3):543–564.
Schmieta S. and F. Alizadeh (2003). Extension of primal–dual interior point
algorithms to symmetric cones. _Mathematical_ _Programming_, 96(3):409–438.
Shapiro A., D. Dentcheva, and A. Ruszczynski (2009). _Lectures_ _on_ _Stochastic_
_Programming:_ _Modeling_ _and_ _Theory_ . SIAM.
Sharpe W. (1964). Capital asset prices: a theory of market equilibrium under
conditions of risk. _Journal_ _of_ _Finance_, 19(3):425–442.
Sharpe W. (1992). Asset allocation: management style and performance measurement. _Journal_ _of_ _Portfolio_ _Management_, 18(2):7–19.
Shleifer A. (2000). _Inefficient_ _Markets_ . Oxford University Press.
Shreve S. (2000). _Stochastic_ _Calculus_ _for_ _Finance_, volumes I and II. Springer.
Sra S., S. Nowozin, and S. Wright (2012). _Optimization_ _for_ _Machine_ _Learning_ .
MIT Press.
Stein C. (1956). Inadmissibility of the usual estimator for the mean of multivariate normal distribution. In _Proceedings_ _of_ _the_ _Third_ _Berkeley_ _Symposium_ _on_
_Mathematical_ _Statistics_ _and_ _Probability_, pp. 197–206.


**References** 333


Sturm J. (1999). Using SeDuMi 1.02, a Matlab toolbox for optimization over
symmetric cones. _Optimization_ _Methods_ _and_ _Software_, 11:625–653.
Tibshirani R. (1996). Regression shrinkage and selection via the lasso. _Journal_
_of_ _the_ _Royal_ _Statistical_ _Society_, 58:267–288.
Tobin J. (1958). Liquidity preference as behavior towards risk. _Review_ _of_
_Economic_ _Studies_, 25(2):65–86.
Toh K., M. Todd, and R. T¨ut¨unc¨u (1999). SDPT3 - a MATLAB software
package for semidefinite programming. _Optimization_ _Methods_ _and_ _Software_,
11:545–581.
Tuckman B. (2002). _Fixed_ _Income_ _Securities:_ _Tools_ _for_ _Today’s_ _Markets_ . Wiley.
T¨ut¨unc¨u R. and M. Koenig (2004). Robust asset allocation. _Annals of Operations_
_Research_, 132:157–187.
Vapnik V. (2013). _The_ _Nature_ _of_ _Statistical_ _Learning_ _Theory_ . Springer.
Werner R. (2010). Costs and Benefits of Robust Optimization. Technical Report,
Technical University of M¨unchen.
Ye Y. (1997). _Interior-Point_ _Algorithms:_ _Theory_ _and_ _Analysis_ . Wiley.
Zhao Y. and W.T. Ziemba (2001). A stochastic programming model using an
endogenously determined worst case risk measure for dynamic asset allocation.
_Mathematical_ _Programming_, 89(2):293–309.


### **Index**

accrued interest, 42
active constraint, _see_ binding constraint
active return, 105
active risk, 105
active set, 313
active-set methods, 81
adaptive decision, 7
adjoint, 285
Almgren–Chriss model, 201
alpha
Jensen, 113
_t_ -statistic, 113
alpha of a security, 104
APT, 111
arbitrage, 55
arbitrage pricing theory, _see_ APT
Armijo–Goldstein condition, 309
asset allocation, 95
asset–liability management, 262
auction
combinatorial, 161
autoregressive model, 256


backtracking, 309
Basel III, 15
basic feasible solution, 25
basis, 25
optimal, 25
Bellman’s optimality principle, 215, 216, 221
Benders decomposition, 255
Benders decomposition method, 177
bequest, 227
beta
long–short threshold, 119
beta of a security, 104
bid, 161
bid–ask spread, 66
binary program, 140
binding constraint, 3
binomial lattice, 238
binomial lattice model, 238
binomial pricing model, 56
Black–Litterman model, 126
Black–Scholes–Merton equation, 245



Black–Scholes–Merton option pricing
formula, 316
blocking constraint, 82
bond
clean price, 42
coupon rate, 42
dirty price, 42
maturity date, 42
term to maturity, 42
yield, 42
bond allocation, 12
bond portfolio
dedicated, 35
boostrapping, 131
branch-and-bound method, 150, 151
branch-and-bound tree, 152
branch-and-cut method, 150
branching, 151
Brownian motion, 315
BSM formula, 316
bundle, 161


capital allocation line, 98
capital asset pricing model, _see_ CAPM
CAPM, 98, 108, 111, 112
captured value, 202
cash flow problems, 44
central path, 29, 83
clientele effects, 63
clustering, 142
combinatorial auction problem, 161
complementary slackness conditions, 24
conditional value at risk, _see_ CVaR
cone
second-order, 277
symmetric, 287
conic program, 277
dual, 282
primal, 282
constraint
turnover, 101
constraint set, 3
consumption, 174
contingent claim, 55


convex function, 325
convex optimization, 4
convex set, 324
cutting plane, 154
cutting-plane method, 150, 154
CVaR, 181, 184


decision variables, 3
descent direction, 309
deterministic model, 4
diffusion model, 316
dispersion measure, 181
diversification, 134
maximum, 135
drift, 244
dual cone, 282
dual problem, 21


efficient frontier, 93, 124
estimator
inadmissable, 129
James–Stein shrinkage, 129
risk, 129
Euler equation, 206
event tree, 250
excess return, 102


factor exposure, _see_ factor loading
factor loading, 107
factor model, 106
factor portfolio, 120
Farkas’s lemma, 21, 34
feasibility cut, 178
feasible point, 3
feasible region, 3
feasible solution, _see_ feasible point
Fisher–Weil convexity, 40
Fisher–Weil dollar convexity, 40
Fisher–Weil dollar duration, 39
Frobenius inner product, 281
fund allocation
linear programming model, 12
fundamental theorem of asset pricing, 56


geometric Brownian motion model, 244
Gomory mixed integer cut, 155
Gordan’s theorem, 22, 34
gradient descent method, 309


homogenization, 102
hyperplane separation theorem, 34


ice-cream cone, _see_ cone, second-order
immunization, 39
immunized portfolio, 39
implementation shortfall, _see_ total cost of
trading
implied volatility, 273
index fund, 165
infeasible problem, 3
information ratio, 105



**Index** 335


insurance company ALM problem, 263
interior-point method, 28
infeasibility, 30
nonlinear programming, 313
quadratic program, 83


Jacobian, 310
Jensen’s alpha, 112


Kelly criterion, 197


L-shaped method, 177
Lagrange multiplier, 75
Lagrangian dual, 147
Lagrangian function, 22, 77
lasso regression, 87
line search, 309
line-search procedure, 30
linear independence constraint qualification,
307
linear optimization model, _see_ linear
programming model
linear program, 11
linear programming, 5
linear programming model, 11
non-degenerate, 19
standard form, 13
linear–quadratic regulator, 216
lockbox problem, 163
Lorenz cone, _see_ cone, second-order
loss function, 193


MAD, 181
market completeness, 59
Markowitz mean–variance, 91
Markowitz mean–variance model, 8
master problem, 177
matrix
inverse, 323
positive semidefinite, 5, 280
mean absolute deviation, _see_ MAD
mean–variance, 71, 296
stochastic optimization, 175
mean–variance model
basic, 94
general, 100
mean–variance optimization model, 93
minimum position constraints, 168
mixed integer linear program, 140
mixed integer optimization, 4
mixed integer program, 140
mixed integer programming, 6
multi-period model, 4
multiple-factor risk model, 109


newsvendor problem, 173, 175, 177
Newton step, 29, 286
Newton’s method, 310
nonlinear program, 305
NP-hardness, 150


336 **Index**


objective function, 3
one-fund separation theorem, 97
optimal decision rule, 216
optimal policy, 216
optimal solution, 3
optimal value, 3
optimality conditions, 24
optimality cut, 178, 180
optimization
robust, 289
option
American, 241
European, 239
option pricing, 238


par, _see_ principal value
pension fund, 263
performance analysis, 112
portfolio
benchmark, 103
characteristic, 96
efficient, 93
equally weighted, 133
factor mimicking, 111
minimum risk, 95
risk-parity, 134
tangency, 97
value-weighted, 133
portfolio management, 8
portfolio optimization
dynamic, 198
positive linear pricing rule, 55
primal problem, 21
principal, _see_ principal value
principal value, 42
program
semidefinite, 280
pruning a node, 152
pure integer linear program, 140


quadratic program, 71
dual, 76
primal, 76
standard form, 71
quadratic programming, 5
sequential, 313
quadratic programming model, _see_ quadratic
program


random sampling, 257
adjusted, 257
recourse, 7
recourse problem, 177
reduced cost, 25
reduced gradient
generalized, 312
regret, 292
relaxation, 141, 145
linear programming, 145



resampled efficiency, 131
residual vector, 83
reward-to-risk ratio, _see_ Sharpe ratio
Ricatti equation, 220
ridge regression, 86
risk contribution, 134
marginal, 134
risk management, 9
risk measure, 6, 175, 181
coherent, 184
risk-neutral probability measure, 55
robust portfolio optimization, 299
robustness, 289
constraint, 290
objective, 291
relative, 292
sampling, 294


saddle-point problem, 292
scenario optimization, 176
scenario tree, 248
arbitrage-free, 258
scenario trees
construction, 256
second-order program, 277
security selection, 95, 103
selection return, 114
semidefinite program
standard form, 281
sensitivity, 18, 38, 75
separation theorem, _see_ hyperplane
sequential system, 214
shadow price, 17, 38
Sharpe ratio, 101, 116
shrinkage estimators, 129
shrinkage factor, 129
shrinkage procedure, 108
shrinkage target, 129
signal, 111
simplex method, 25
dual, 25, 27
single-factor risk model, 107
slack variable, 14
Slater condition, 284
static model, 4
Stein paradox, 129
Stiemke’s theorem, 22, 34
stochastic and dynamic optimization, 4
stochastic discount factor, 56
stochastic model, 4
stochastic optimization, 6, 173, 174
two-stage with recourse, 6
with recourse, 174
stochastic program
linear two-stage, 175
stochastic programming, 248
multi-stage, 248


stochastic sequential decision problem, 221
stochastic sequential system, 221
strong duality theorem, 21
style analysis, 113
subdifferential, 311
subgradient, 311
subgradient method, 311
support vector machine, 85
surplus variable, 14
synthetic option, 270
synthetic option strategy, 270


tangent subspace, 308
term structure, 39
implied, 38
total cost of trading, 203
tracking error, _see_ active risk
tractability, 4
trade list, 202
trading strategy
execution, 202
trading trajectory, 202
treasury yield curve, 42
tree fitting, 257



**Index** 337


two-fund separation theorem, 96
two-fund theorem, 115


unbounded problem, 4
uncertainty set, 289
ellipsoidal, 290
urgency, 206
utility, 173
logarithmic, 199
power, 199
quadratic, 93


value at risk, _see_ VaR
conditional, _see_ CVaR
value-to-go function, 215
VaR, 183
_α_, 183
volatility, 244
volatility smile, 316
volume-weighted average price (VWAP),
204


weak duality theorem, 21
winner selection problem, _see_ combinatorial
auction problem


