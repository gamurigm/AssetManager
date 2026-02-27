![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-0-full.png)
##### Steven Shreve: Stochastic Calculus and Finance



PRASAD CHALASANI
Carnegie Mellon University
chal@cs.cmu.edu



SOMESH JHA
Carnegie Mellon University
sjha@cs.cmu.edu




- c Copyright; Steven E. Shreve, 1996


July 25, 1997


# **Contents**

**1** **Introduction to Probability Theory** **11**

1.1 The Binomial Asset Pricing Model . . . . . . . . . . . . . . . . . . . . . . . . . . 11

1.2 Finite Probability Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

1.3 Lebesgue Measure and the Lebesgue Integral . . . . . . . . . . . . . . . . . . . . 22

1.4 General Probability Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

1.5 Independence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

1.5.1 Independence of sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

1.5.2 Independence of      - -algebras . . . . . . . . . . . . . . . . . . . . . . . . . 41

1.5.3 Independence of random variables . . . . . . . . . . . . . . . . . . . . . . 42

1.5.4 Correlation and independence . . . . . . . . . . . . . . . . . . . . . . . . 44

1.5.5 Independence and conditional expectation. . . . . . . . . . . . . . . . . . 45

1.5.6 Law of Large Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

1.5.7 Central Limit Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47


**2** **Conditional Expectation** **49**

2.1 A Binomial Model for Stock Price Dynamics . . . . . . . . . . . . . . . . . . . . 49

2.2 Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

2.3 Conditional Expectation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

2.3.1 An example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

2.3.2 Definition of Conditional Expectation . . . . . . . . . . . . . . . . . . . . 53

2.3.3 Further discussion of Partial Averaging . . . . . . . . . . . . . . . . . . . 54

2.3.4 Properties of Conditional Expectation . . . . . . . . . . . . . . . . . . . . 55

2.3.5 Examples from the Binomial Model . . . . . . . . . . . . . . . . . . . . . 57

2.4 Martingales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58


1


2


**3** **Arbitrage Pricing** **59**

3.1 Binomial Pricing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

3.2 General one-step APT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

3.3 Risk-Neutral Probability Measure . . . . . . . . . . . . . . . . . . . . . . . . . . 61

3.3.1 Portfolio Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

3.3.2 Self-financing Value of a Portfolio Process      - . . . . . . . . . . . . . . . . 62

3.4 Simple European Derivative Securities . . . . . . . . . . . . . . . . . . . . . . . . 63

3.5 The Binomial Model is Complete . . . . . . . . . . . . . . . . . . . . . . . . . . . 64


**4** **The Markov Property** **67**

4.1 Binomial Model Pricing and Hedging . . . . . . . . . . . . . . . . . . . . . . . . 67

4.2 Computational Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

4.3 Markov Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70

4.3.1 Different ways to write the Markov property . . . . . . . . . . . . . . . . 70

4.4 Showing that a process is Markov . . . . . . . . . . . . . . . . . . . . . . . . . . 73

4.5 Application to Exotic Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74


**5** **Stopping Times and American Options** **77**

5.1 American Pricing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

5.2 Value of Portfolio Hedging an American Option . . . . . . . . . . . . . . . . . . . 79

5.3 Information up to a Stopping Time . . . . . . . . . . . . . . . . . . . . . . . . . . 81


**6** **Properties of American Derivative Securities** **85**

6.1 The properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

6.2 Proofs of the Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

6.3 Compound European Derivative Securities . . . . . . . . . . . . . . . . . . . . . . 88

6.4 Optimal Exercise of American Derivative Security . . . . . . . . . . . . . . . . . . 89


**7** **Jensen’s Inequality** **91**

7.1 Jensen’s Inequality for Conditional Expectations . . . . . . . . . . . . . . . . . . . 91

7.2 Optimal Exercise of an American Call . . . . . . . . . . . . . . . . . . . . . . . . 92

7.3 Stopped Martingales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94


**8** **Random Walks** **97**

8.1 First Passage Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97


3


8.2   - is almost surely finite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97

8.3 The moment generating function for   - . . . . . . . . . . . . . . . . . . . . . . . . 99

8.4 Expectation of   - . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

8.5 The Strong Markov Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

8.6 General First Passage Times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

8.7 Example: Perpetual American Put . . . . . . . . . . . . . . . . . . . . . . . . . . 102

8.8 Difference Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

8.9 Distribution of First Passage Times . . . . . . . . . . . . . . . . . . . . . . . . . . 107

8.10 The Reflection Principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109


**9** **Pricing in terms of Market Probabilities: The Radon-Nikodym Theorem.** **111**

9.1 Radon-Nikodym Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

9.2 Radon-Nikodym Martingales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112

9.3 The State Price Density Process . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

9.4 Stochastic Volatility Binomial Model . . . . . . . . . . . . . . . . . . . . . . . . . 116

9.5 Another Applicaton of the Radon-Nikodym Theorem . . . . . . . . . . . . . . . . 118


**10** **Capital Asset Pricing** **119**

10.1 An Optimization Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119


**11** **General Random Variables** **123**

11.1 Law of a Random Variable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

11.2 Density of a Random Variable . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

11.3 Expectation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124

11.4 Two random variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

11.5 Marginal Density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

11.6 Conditional Expectation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

11.7 Conditional Density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127

11.8 Multivariate Normal Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

11.9 Bivariate normal distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

11.10MGF of jointly normal random variables . . . . . . . . . . . . . . . . . . . . . . . 130


**12** **Semi-Continuous Models** **131**

12.1 Discrete-time Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . 131


4


12.2 The Stock Price Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

12.3 Remainder of the Market . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133

12.4 Risk-Neutral Measure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133

12.5 Risk-Neutral Pricing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

12.6 Arbitrage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

12.7 Stalking the Risk-Neutral Measure . . . . . . . . . . . . . . . . . . . . . . . . . . 135

12.8 Pricing a European Call . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138


**13** **Brownian Motion** **139**

13.1 Symmetric Random Walk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

13.2 The Law of Large Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

13.3 Central Limit Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

13.4 Brownian Motion as a Limit of Random Walks . . . . . . . . . . . . . . . . . . . 141

13.5 Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

13.6 Covariance of Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . 143

13.7 Finite-Dimensional Distributions of Brownian Motion . . . . . . . . . . . . . . . . 144

13.8 Filtration generated by a Brownian Motion . . . . . . . . . . . . . . . . . . . . . . 144

13.9 Martingale Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145

13.10The Limit of a Binomial Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145

13.11Starting at Points Other Than 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

13.12Markov Property for Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . 147

13.13Transition Density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149

13.14First Passage Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149


**14** **The Itˆo Integral** **153**

14.1 Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153

14.2 First Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153

14.3 Quadratic Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155

14.4 Quadratic Variation as Absolute Volatility . . . . . . . . . . . . . . . . . . . . . . 157

14.5 Construction of the Itˆo Integral . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

14.6 Itˆo integral of an elementary integrand . . . . . . . . . . . . . . . . . . . . . . . . 158

14.7 Properties of the Itˆo integral of an elementary process . . . . . . . . . . . . . . . . 159

14.8 Itˆo integral of a general integrand . . . . . . . . . . . . . . . . . . . . . . . . . . . 162


5


14.9 Properties of the (general) Itˆo integral . . . . . . . . . . . . . . . . . . . . . . . . 163

14.10Quadratic variation of an Itˆo integral . . . . . . . . . . . . . . . . . . . . . . . . . 165


**15** **Itˆo’s Formula** **167**

15.1 Itˆo’s formula for one Brownian motion . . . . . . . . . . . . . . . . . . . . . . . . 167

15.2 Derivation of Itˆo’s formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168

15.3 Geometric Brownian motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169

15.4 Quadratic variation of geometric Brownian motion . . . . . . . . . . . . . . . . . 170

15.5 Volatility of Geometric Brownian motion . . . . . . . . . . . . . . . . . . . . . . 170

15.6 First derivation of the Black-Scholes formula . . . . . . . . . . . . . . . . . . . . 170

15.7 Mean and variance of the Cox-Ingersoll-Ross process . . . . . . . . . . . . . . . . 172

15.8 Multidimensional Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . 173

15.9 Cross-variations of Brownian motions . . . . . . . . . . . . . . . . . . . . . . . . 174

15.10Multi-dimensional Itˆo formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175


**16** **Markov processes and the Kolmogorov equations** **177**

16.1 Stochastic Differential Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . 177

16.2 Markov Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178

16.3 Transition density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179

16.4 The Kolmogorov Backward Equation . . . . . . . . . . . . . . . . . . . . . . . . 180

16.5 Connection between stochastic calculus and KBE . . . . . . . . . . . . . . . . . . 181

16.6 Black-Scholes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183

16.7 Black-Scholes with price-dependent volatility . . . . . . . . . . . . . . . . . . . . 186


**17** **Girsanov’s theorem and the risk-neutral measure** **189**



17.1 Conditional expectations under



IP . . . . . . . . . . . . . . . . . . . . . . . . . . 191



.

f



17.2 Risk-neutral measure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193



**18** **Martingale Representation Theorem** **197**

18.1 Martingale Representation Theorem . . . . . . . . . . . . . . . . . . . . . . . . . 197

18.2 A hedging application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

18.3 d -dimensional Girsanov Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . 199

18.4 d -dimensional Martingale Representation Theorem . . . . . . . . . . . . . . . . . 200

18.5 Multi-dimensional market model . . . . . . . . . . . . . . . . . . . . . . . . . . . 200


6


**19** **A two-dimensional market model** **203**

19.1 Hedging when <  - < . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204

       
19.2 Hedging when  - = . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205


**20** **Pricing Exotic Options** **209**

20.1 Reflection principle for Brownian motion . . . . . . . . . . . . . . . . . . . . . . 209

20.2 Up and out European call. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212

20.3 A practical issue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218


**21** **Asian Options** **219**

21.1 Feynman-Kac Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

21.2 Constructing the hedge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

21.3 Partial average payoff Asian option . . . . . . . . . . . . . . . . . . . . . . . . . . 221


**22** **Summary of Arbitrage Pricing Theory** **223**

22.1 Binomial model, Hedging Portfolio . . . . . . . . . . . . . . . . . . . . . . . . . 223

22.2 Setting up the continuous model . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

22.3 Risk-neutral pricing and hedging . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

22.4 Implementation of risk-neutral pricing and hedging . . . . . . . . . . . . . . . . . 229


**23** **Recognizing a Brownian Motion** **233**

23.1 Identifying volatility and correlation . . . . . . . . . . . . . . . . . . . . . . . . . 235

23.2 Reversing the process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236


**24** **An outside barrier option** **239**

24.1 Computing the option value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242

24.2 The PDE for the outside barrier option . . . . . . . . . . . . . . . . . . . . . . . . 243

24.3 The hedge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245


**25** **American Options** **247**

25.1 Preview of perpetual American put . . . . . . . . . . . . . . . . . . . . . . . . . . 247

25.2 First passage times for Brownian motion: first method . . . . . . . . . . . . . . . . 247

25.3 Drift adjustment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249

25.4 Drift-adjusted Laplace transform . . . . . . . . . . . . . . . . . . . . . . . . . . . 250

25.5 First passage times: Second method . . . . . . . . . . . . . . . . . . . . . . . . . 251


7


25.6 Perpetual American put . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252

25.7 Value of the perpetual American put . . . . . . . . . . . . . . . . . . . . . . . . . 256

25.8 Hedging the put . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257

25.9 Perpetual American contingent claim . . . . . . . . . . . . . . . . . . . . . . . . . 259

25.10Perpetual American call . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259

25.11Put with expiration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

25.12American contingent claim with expiration . . . . . . . . . . . . . . . . . . . . . 261


**26** **Options on dividend-paying stocks** **263**

26.1 American option with convex payoff function . . . . . . . . . . . . . . . . . . . . 263

26.2 Dividend paying stock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264



26.3 Hedging at time t



. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266



**27** **Bonds, forward contracts and futures** **267**

27.1 Forward contracts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269

27.2 Hedging a forward contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269

27.3 Future contracts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270

27.4 Cash flow from a future contract . . . . . . . . . . . . . . . . . . . . . . . . . . . 272

27.5 Forward-future spread . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272

27.6 Backwardation and contango . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273


**28** **Term-structure models** **275**

28.1 Computing arbitrage-free bond prices: first method . . . . . . . . . . . . . . . . . 276

28.2 Some interest-rate dependent assets . . . . . . . . . . . . . . . . . . . . . . . . . 276

28.3 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277

28.4 Forward rate agreement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277

28.5 Recovering the interest r (t) from the forward rate . . . . . . . . . . . . . . . . . . 278

28.6 Computing arbitrage-free bond prices: Heath-Jarrow-Morton method . . . . . . . . 279

28.7 Checking for absence of arbitrage . . . . . . . . . . . . . . . . . . . . . . . . . . 280

28.8 Implementation of the Heath-Jarrow-Morton model . . . . . . . . . . . . . . . . . 281


**29** **Gaussian processes** **285**

29.1 An example: Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286


**30** **Hull and White model** **293**


8


30.1 Fiddling with the formulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295

30.2 Dynamics of the bond price . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296

30.3 Calibration of the Hull & White model . . . . . . . . . . . . . . . . . . . . . . . . 297

30.4 Option on a bond . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299


**31** **Cox-Ingersoll-Ross model** **303**

31.1 Equilibrium distribution of r (t) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306

31.2 Kolmogorov forward equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306

31.3 Cox-Ingersoll-Ross equilibrium density . . . . . . . . . . . . . . . . . . . . . . . 309

31.4 Bond prices in the CIR model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310

31.5 Option on a bond . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313

31.6 Deterministic time change of CIR model . . . . . . . . . . . . . . . . . . . . . . . 313

31.7 Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315



0 (0) in the time change of the CIR model . . . . . . . . . . . . . 316



31.8 Tracking down '0



0



**32** **A two-factor model (Duffie & Kan)** **319**

32.1 Non-negativity of Y . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320

32.2 Zero-coupon bond prices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321

32.3 Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 323


**33** **Change of num´eraire** **325**

33.1 Bond price as num´eraire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327

33.2 Stock price as num´eraire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328

33.3 Merton option pricing formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329


**34** **Brace-Gatarek-Musiela model** **335**

34.1 Review of HJM under risk-neutral IP . . . . . . . . . . . . . . . . . . . . . . . . . 335

34.2 Brace-Gatarek-Musiela model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336

34.3 LIBOR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337

34.4 Forward LIBOR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338

34.5 The dynamics of L(t;  - ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338

34.6 Implementation of BGM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340

34.7 Bond prices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342

34.8 Forward LIBOR under more forward measure . . . . . . . . . . . . . . . . . . . . 343


9


34.9 Pricing an interest rate caplet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343

34.10Pricing an interest rate cap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345

34.11Calibration of BGM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345

34.12Long rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346

34.13Pricing a swap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346


10


### **Chapter 1**

# **Introduction to Probability Theory**

**1.1** **The Binomial Asset Pricing Model**


The _binomial asset pricing model_ provides a powerful tool to understand arbitrage pricing theory
and probability theory. In this course, we shall use it for both these purposes.

In the binomial asset pricing model, we model stock prices in discrete time, assuming that at each
step, the stock price will change to one of two possible values. Let us begin with an initial positive
stock price S0 [.] [There are two positive numbers,] d and u, with


0 < d < u; (1.1)



such that at the next period, the stock price will be either dS0 [or] uS0 [.] [Typically, we] [take] d and u

to satisfy 0 < d < < u, so change of the stock price from S0 [to] dS0 [represents] [a] _[downward]_



such that at the next period, the stock price will be either dS



0 [or] uS



0 [to] dS



to satisfy 0 < d < < u, so change of the stock price from S0 [to] dS0 [represents] [a] _[downward]_

movement, and change of the stock price from S0 [to] uS0 [represents] [an] _[upward]_ [movement.] [It] [is]



movement, and change of the stock price from S0 [to] uS0 [represents] [an] _[upward]_ [movement.] [It] [is]

common to also have d = [, and this will be the case in many of our examples.] [However, strictly]



0 [to] uS



common to also have d = u [, and this will be the case in many of our examples.] [However, strictly]

speaking, for what we are about to do we need to assume only (1.1) and (1.2) below.

Of course, stock price movements are much more complicated than indicated by the binomial asset
pricing model. We consider this simple model for three reasons. First of all, within this model the
concept of arbitrage pricing and its relation to risk-neutral pricing is clearly illuminated. Secondly,
the model is used in practice because with a sufficient number of steps, it provides a good, computationally tractable approximation to continuous-time models. Thirdly, within the binomial model
we can develop the theory of conditional expectations and martingales which lies at the heart of
continuous-time models.

With this third motivation in mind, we develop notation for the binomial model which is a bit
different from that normally found in practice. Let us imagine that we are tossing a coin, and when
we get a “Head,” the stock price moves up, but when we get a “Tail,” the price moves down. We
denote the price at time by S (H ) = uS0 [if the toss results in head (H), and by] S (T ) = dS0 [if it]



0 [if the toss results in head (H), and by] S



0 [if it]



(H ) = uS



(T ) = dS



11


12



_S (HH) = 16_

_2_



_S (H) = 8_

_1_



_S (HT) = 4_

_2_



_S = 4_
_0_



_S (TH) = 4_

_2_



_S (T) = 2_

_1_



_S (TT) = 1_

_2_



Figure 1.1: _Binomial tree of stock prices with_ S



0



= _,_ u = =d = _._



results in tail (T). After the second toss, the price will be one of:



(H ) = u



(T ) = udS0



S0



(H ) = duS0



(T ) = d



S


S



(H H ) = uS


(T H ) = uS



; S



; S



(H T ) = dS


(T T ) = dS



;



S0 :



After three tosses, there are eight possible coin sequences, although not all of them result in different
stock prices at time .

For the moment, let us assume that the third toss is the last one and denote by


     - = fH H H ; H H T ; H T H ; H T T ; T H H ; T H T ; T T H ; T T T g

the set of all possible outcomes of the three tosses. The set - of all possible outcomes of a random experiment is called the _sample space_ for the experiment, and the elements ! of - are called
_sample points_ . In this case, each sample point ! is a sequence of length three. We denote the k -th
component of ! by !k [.] [For example, when] ! = H T H, we have ! = H, ! = T and ! = H .

The stock price Sk [at time] k depends on the coin tosses. To emphasize this, we often write Sk (! ) .

Actually, this notation does not quite tell the whole story, for while S [depends] [on] [all] [of] !, S



k [.] [For example, when] ! = H T H, we have !



= H, !



= T and !



= H .



The stock price S



k [at time] k depends on the coin tosses. To emphasize this, we often write S



k



depends on only the first two components of !, S




[depends on only the first component of] !, and




[depends] [on] [all] [of] !, S



S0 [does not depend on] ! at all. Sometimes we will use notation such S (! ; ! ) just to record more

explicitly how S [depends on] ! = (! ; ! ; ! ) .



0 [does not depend on] ! at all. Sometimes we will use notation such S



S




[depends on] ! = (!



(!



; !



; !



; !



) .



**Example 1.1** Set S



**Example 1.1** Set S0 =, u = and d = [.] [We] [have] [then the binomial “tree”] [of possible stock]

prices shown in Fig. 1.1. Each sample point ! = (! ; ! ; ! ) represents a path through the tree.



0



=, u = and d =



prices shown in Fig. 1.1. Each sample point ! = (! ; ! ; ! ) represents a path through the tree.

Thus, we can think of the sample space - as either the set of all possible outcomes from three coin
tosses or as the set of all possible paths through the tree.



; !



; !



To complete our binomial asset pricing model, we introduce a _money market_ with _interest rate_ r ;
$1 invested in the money market becomes $( + r ) in the next period. We take r to be the interest


CHAPTER 1.Introduction to Probability Theory 13


rate for both _borrowing_ and _lending_ . (This is not as ridiculous as it first seems, because in a many
applications of the model, an agent is either borrowing or lending (not both) and knows in advance
which she will be doing; in such an application, she should take r to be the rate of interest for her
activity.) We assume that


d < + r < u: (1.2)


The model would not make sense if we did not have this condition. For example, if + r u, then

                       the rate of return on the money market is always at least as great as and sometimes greater than the
return on the stock, and no one would invest in the stock. The inequality d + r cannot happen

                    unless either r is negative (which never happens, except maybe once upon a time in Switzerland) or

d . In the latter case, the stock does not really go “down” if we get a tail; it just goes up less

 than if we had gotten a head. One should borrow money at interest rate r and invest in the stock,
since even in the worst case, the stock price rises at least as fast as the debt used to buy it.

With the stock as the underlying asset, let us consider a _European_ _call_ _option_ with strike price

K - 0 and expiration time . This option confers the right to buy the stock at time for K dollars,
and so is worth S K at time if S K is positive and is otherwise worth zero. We denote by



K at time if S




K is positive and is otherwise worth zero. We denote by




(! ) - K ; 0g



=� maxfS



(! ) - K )+



V



(! ) = (S



the value (payoff) of this option at expiration. Of course, V (! ) actually depends only on ! [, and]

we can and do sometimes write V (! ) rather than V (! ) . Our first task is to compute the _arbitrage_



the value (payoff) of this option at expiration. Of course, V



(! ) actually depends only on !



we can and do sometimes write V (! ) rather than V (! ) . Our first task is to compute the _arbitrage_

_price_ of this option at time zero.



(!



) rather than V



Suppose at time zero you sell the call for V



0 [dollars, where] V



Suppose at time zero you sell the call for V0 [dollars, where] V0 [is still to be determined.] [You now]

have an obligation to pay off (uS0 K )+ if ! = H and to pay off (dS0 K )+ if ! = T . At



= H and to pay off (dS



have an obligation to pay off (uS0 K )+ if ! = H and to pay off (dS0 K )+ if ! = T . At

          -          
the time you sell the option, you don’t yet know which value ! [will take.] [You] _[hedge]_ [ your short]



0




- K )



0



0

+ if !




- K )



+ if !



the time you sell the option, you don’t yet know which value ! [will take.] [You] _[hedge]_ [ your short]

position in the option by buying �0 [shares of stock, where] �0 [is still to be determined. You can use]



position in the option by buying �0 [shares of stock, where] �0 [is still to be determined. You can use]

the proceeds V0 [of the sale] [of the option for this purpose, and then borrow if] [necessary at interest]



0 [shares of stock, where] 


the proceeds V0 [of the sale] [of the option for this purpose, and then borrow if] [necessary at interest]

rate r to complete the purchase. If V0 [is] [more] [than necessary] [to] [buy the] �0 [shares] [of] [stock,] [you]



rate r to complete the purchase. If V0 [is] [more] [than necessary] [to] [buy the] �0 [shares] [of] [stock,] [you]

invest the residual money at interest rate r . In either case, you will have V0 �0 S0 [dollars invested]



0 [is] [more] [than necessary] [to] [buy the] 


invest the residual money at interest rate r . In either case, you will have V0 �0 S0 [dollars invested]

                    
in the money market, where this quantity might be negative. You will also own �0 [shares of stock.]



0




- 


0



S



0 [shares of stock.]



If the stock goes up, the value of your portfolio (excluding the short position in the option) is



�0 S



(H ) + ( + r )(V0



�0




S0



);



and you need to have V



(H ) . Thus, you want to choose V



0 [and] 


0 [so that]



�0




S0



): (1.3)



V



(H ) = �0



S



(H ) + ( + r )(V0



If the stock goes down, the value of your portfolio is



�0 S



(T ) + ( + r )(V0



�0




S0



);



and you need to have V



(T ) . Thus, you want to choose V



0 [and] 


0 [to also have]



S0



): (1.4)



V



(T ) = �0



S



(T ) + ( + r )(V0



�0



14


These are two equations in two unknowns, and we solve them below

Subtracting (1.4) from (1.3), we obtain



(T ) = �0



(S



(H ) - S



(T )); (1.5)



V



(H ) - V


�0



so that



(T )

(T )



(H ) - V

(H ) - S



=



V

S



: (1.6)



This is a discrete-time version of the famous “delta-hedging” formula for derivative securities, according to which the number of shares of an underlying asset a hedge should hold is the derivative
(in the sense of calculus) of the value of the derivative security with respect to the price of the
underlying asset. This formula is so pervasive the when a practitioner says “delta”, she means the
derivative (in the sense of calculus) just described. Note, however, that my _definition_ of �0 [is the]



derivative (in the sense of calculus) just described. Note, however, that my _definition_ of �0 [is the]

number of shares of stock one holds at time zero, and (1.6) is a consequence of this definition, not
the definition of �0 [itself.] [Depending] [on] [how] [uncertainty] [enters] [the] [model,] [there] [can] [be] [cases]



the definition of �0 [itself.] [Depending] [on] [how] [uncertainty] [enters] [the] [model,] [there] [can] [be] [cases]

in which the number of shares of stock a hedge should hold is not the (calculus) derivative of the
derivative security with respect to the price of the underlying asset.

To complete the solution of (1.3) and (1.4), we substitute (1.6) into either (1.3) or (1.4) and solve
for V0 [. After some simplification, this leads to the formula]



To complete the solution of (1.3) and (1.4), we substitute (1.6) into either (1.3) or (1.4) and solve
for V0 [. After some simplification, this leads to the formula]



+ r - d



u - d



+ r



u - ( + r )



u - d



V0



=



(H ) +



(T )

  


: (1.7)







V



V



This is the _arbitrage price_ for the European call option with payoff V [at time] . To simplify this

formula, we define



This is the _arbitrage price_ for the European call option with payoff V



+ r - d

u - d



; q~



=�



u - ( + r )

u  - d



= p~; (1.8)

 


p~



=�







so that (1.7) becomes



+ r



(H ) + q~V



(T )]: (1.9)



V0



=




[p~V



Because we have taken d < u, both p~ and q~ are defined,i.e., the denominator in (1.8) is not zero.
Because of (1.2), both p~ and q~ are in the interval (0; ), and because they sum to, we can regard
them as probabilities of H and T, respectively. They are the _risk-neutral_ probabilites. They appeared when we solved the two equations (1.3) and (1.4), and have nothing to do with the actual
probabilities of getting H or T on the coin tosses. In fact, at this point, they are nothing more than
a convenient tool for writing (1.7) as (1.9).

We now consider a European call which pays off K dollars at time . At expiration, the payoff of
this option is V =� (S K )+, where V [and] S [depend on] ! [and] ! [, the first] [and second coin]



this option is V =� (S K )+, where V [and] S [depend on] ! [and] ! [, the first] [and second coin]

       
tosses. We want to determine the arbitrage price for this option at time zero. Suppose an agent sells
the option at time zero for V0 [dollars, where] V0 [is still to be determined.] [She then buys] �0 [shares]




[depend on] !




[and] !







= (S




- K )



+, where V




[and] S



0 [dollars, where] V



0 [is still to be determined.] [She then buys] 


0 [shares]


CHAPTER 1.Introduction to Probability Theory 15



of stock, investing V



of stock, investing V0 �0 S0 [dollars in the money market to finance this. At time], the agent has

      
a portfolio (excluding the short position in the option) valued at



0




- 


0



S



S



�0




S0



): (1.10)



X



= 






0



+ ( + r )(V0



Although we do not indicate it in the notation, S




[and therefore] X



Although we do not indicate it in the notation, S [and therefore] X [depend on] ! [, the outcome of]

the first coin toss. Thus, there are really two equations implicit in (1.10):




[depend on] !



X (H )


X (T )



=� 






=� 


0



�0




S0


S0



);



(H ) + ( + r )(V0


(T ) + ( + r )(V0



�0




0







S


S



):



After the first coin toss, the agent has X [dollars and can readjust her hedge. Suppose she decides to]

now hold - [shares of stock, where] - [is allowed to depend on] ! [because the agent knows what]



After the first coin toss, the agent has X



now hold - [shares of stock, where] - [is allowed to depend on] ! [because the agent knows what]

value ! [has taken.] [She invests the remainder of her wealth,] X - S [in the money market.] [In]




[shares of stock, where]  



[is allowed to depend on] !



value ! [has taken.] [She invests the remainder of her wealth,] X - S [in the money market.] [In]

                 
the next period, her wealth will be given by the right-hand side of the following equation, and she
wants it to be V [. Therefore, she wants to have]




[has taken.] [She invests the remainder of her wealth,] X




- 


S




[. Therefore, she wants to have]




- 


V



= 


S



+ ( + r )(X



S



): (1.11)



Although we do not indicate it in the notation, S




[and] V




[depend on] !



Although we do not indicate it in the notation, S [and] V [depend on] ! [and] ! [, the outcomes of the]

first two coin tosses. Considering all four possible outcomes, we can write (1.11) as four equations:




[and] !



(H )S


(H )S


(T )S


(T )S



(H H ) + ( + r )(X


(H T ) + ( + r )(X


(T H ) + ( + r )(X



(T T ) + ( + r )(X



(H ) - 


(H )S


(H )S



(H ));


(H ));



V


V


V


V



(H H ) = 

(H T ) = 

(T H ) = 

(T T ) = 


(H ) - 


(T )S


(T )S



(T ));


(T )):



(T ) - 
(T ) - 


We now have six equations, the two represented by (1.10) and the four represented by (1.11), in the
six unknowns V0 [,] �0 [,] - (H ), - (T ), X (H ), and X (T ) .

To solve these equations, and thereby determine the arbitrage price V0 [at time zero of the option and]

the hedging portfolio �0 [,] - (H ) and - (T ), we begin with the last two



0 [,] 


0 [,] 


(H ), 


(T ), X



(H ), and X



(T ) .



To solve these equations, and thereby determine the arbitrage price V



0 [,] 


(H ) and 


(T ), we begin with the last two



(T )S


(T )S



(T H ) + ( + r )(X


(T T ) + ( + r )(X



(T ) - 
(T ) - 


(T )S


(T )S



(T ));


(T )):



V


V



(T H ) = 

(T T ) = 


Subtracting one of these from the other and solving for - (T ), we obtain the “delta-hedging for
mula”



(T T )

(T T )



(T H ) - V

(T H ) - S







(T ) =



V

S



; (1.12)



and substituting this into either equation, we can solve for




[pV~

+ r



(T H ) + q~V



(T T )]: (1.13)



X



(T ) =


16



Equation (1.13), gives the value the hedging portfolio should have at time if the stock goes down
between times 0 and . We define this quantity to be the _arbitrage value of the option at time_ _if_



(T ) . We have just shown that



!



= T, and we denote it by V



+ r







(T H ) + q~V



(T T )]: (1.14)



V



(T )



=�




[p~V



= T agrees with V



The hedger should choose her portfolio so that her wealth X



(T ) if !



X (T ) ! = T V (T )

defined by (1.14). This formula is analgous to formula (1.9), but postponed by one step. The first
two equations implicit in (1.11) lead in a similar way to the formulas



(H T )

(1.15)
(H T )



(H H ) - V

(H H ) - S







(H ) =



V

S



and X



(H )



(H ) is the value of the option at time if !



=�



= H, defined by



(H ) = V



(H ), where V


V








[pV~

+ r



(H H ) + q~V



(H T )]: (1.16)



This is again analgous to formula (1.9), postponed by one step. Finally, we plug the values X



V (H ) and X (T ) = V (T ) into the two equations implicit in (1.10). The solution of these equa
tions for �0 [and] V0 [is] [the] [same] [as] [the] [solution of] [(1.3)] [and] [(1.4),] [and] [results] [again] [in] [(1.6)] [and]



(H ) =



V



(H ) and X



0 [and] V



(T ) = V



tions for �0 [and] V0 [is] [the] [same] [as] [the] [solution of] [(1.3)] [and] [(1.4),] [and] [results] [again] [in] [(1.6)] [and]

(1.9).



The pattern emerging here persists, regardless of the number of periods. If V



k [,] [then at time]



The pattern emerging here persists, regardless of the number of periods. If Vk [denotes the value at]

time k of a derivative security, and this depends on the first k coin tosses ! ; : : : ; !k [,] [then at time]



k, after the first k tosses !

 - 


k, after the first k tosses ! ; : : : ; !k [are] [known, the] [portfolio to hedge a] [short position]

 - - 
should hold �k (! ; : : : ; !k ) shares of stock, where



; : : : ; !



; : : : ; !



(!



k 


) shares of stock, where



k 


; : : : ; !



k 
k 


; : : : ; !k 
; : : : ; !k 


; H ) - V

; H ) - S



; T )

; (1.17)

; T )



k


k



(!

(!



�k - (!



Vk (!

Sk (!



; : : : ; !

; : : : ; !



; : : : ; !



k - ) =



and the value at time k of the derivative security, when the first k coin tosses result in the

      -       outcomes ! ; : : : ; !k [, is given by]



k [, is given by]

 


; : : : ; !



Vk - (!



+ r



; : : : ; !k 


(!



; : : : ; !k 


; : : : ; !



k - ) =



; H ) + q~Vk



; : : : ; !



; T )]
(1.18)




[pV~ k (!



**1.2** **Finite Probability Spaces**


Let - be a set with finitely many elements. An example to keep in mind is


     - = H H H ; H H T ; H T H ; H T T ; T H H ; T H T ; T T H ; T T T (2.1)
f g

of all possible outcomes of three coin tosses. Let be the set of all subsets of - . Some sets in
F F
are, H H H ; H H T ; H T H ; H T T, T T T, and - itself. How many sets are there in ?
; f g f g F


CHAPTER 1.Introduction to Probability Theory 17


**Definition 1.1** A _probability_ _measure_ IP is a function mapping into [0; ] with the following
F
properties:


**(i)** IP (�) =,



**(ii)** If A



; A



; : : : is a sequence of disjoint sets in, then
F



Ak

!



k =

X



IP (Ak ):



IP



k =

[



=



Probability measures have the following interpretation. Let A be a subset of . Imagine that - is
F
the set of all possible outcomes of some random experiment. There is a certain probability, between

0 and, that when that experiment is performed, the outcome will lie in the set A . We think of

IP (A) as this probability.



**Example 1.2** Suppose a coin has probability

- in (2.1), define




[for] H and




[for] T . For the individual elements of


















- 
- 






;


;


;



IP fH H H g =

IP fH T H g =













- 


; IP fH H T g =
















:







IP fT H H g =

IP fT T H g =

For A, we define
F


For example,
















; IP fH T T g =

; IP fT H T g =

; IP fT T T g =





 
 


IP (A) =



! A

X



! A

X



IP ! : (2.2)
f g



















+

 






IP fH H H ; H H T ; H T H ; H T T g =







+







=



;



which is another way of saying that the probability of H on the first toss is




- 
[.]



As in the above example, it is generally the case that we specify a probability measure on only some
of the subsets of - and then use property (ii) of Definition 1.1 to determine IP (A) for the remaining
sets A . In the above example, we specified the probability measure only for the sets containing
F
a single element, and then used Definition 1.1(ii) in the form (2.2) (see Problem 1.4(ii)) to determine

IP for all the other sets in .
F

**Definition 1.2** Let - be a nonempty set. A - -algebra is a collection of subsets of - with the
G
following three properties:


**(i)**,
; G


18



**(ii)** If A, then its complement A
G



c



,
G



**(iii)** If A



; A



; A



; : : : is a sequence of sets in, then
G [



k =



Ak [is also in] .

G



Here are some important - -algebras of subsets of the set - in Example 1.2:



0

F


F


F


F



=


=


=



= = The set of all subsets of �:
F



(;; �);

(;; �; fH H H ; H H T ; H T H ; H T T g; fT H H ; T H T ; T T H ; T T T g



(;; �; fH H H ; H H T g; fH T H ; H T T g; fT H H ; T H T g; fT T H ; T T T g;



;

)



and all sets which can be built by taking unions of these



;



)



To simplify notation a bit, let us define



=� H H H ; H H T ; H T H ; H T T = H on the first toss ;
f g f g







=� H H H ; H H T = H H on the first two tosses ;
f g f g



=� T H H ; T H T ; T T H ; T T T = T on the first toss ;
f g f g







so that


and let us define


so that



AH


AT


A



F



= ; �; AH
f;



; AT ;

g



H H







=� H T H ; H T T = H T on the first two tosses ;
f g f g







AH T


AT H


AT T



=� T H H ; T H T = T H on the first two tosses ;
f g f g







=� T T H ; T T T = T T on the first two tosses ;
f g f g







F



= f;; �; A



A


A



; AT T



;



H H



; AH T ; AT H



c

T T



AT H

[



; A



; A



; AH H



T H



AT T ; AH T

[



; AH T



AT T

[



;



H



T



; AH H



c

H H



c

H T




[ A



c



T H



g:



; A



; A



We interpret - -algebras as a record of information. Suppose the coin is tossed three times, and you
are not told the outcome, but you are told, for every set in [whether or not the outcome is in that]
F



are not told the outcome, but you are told, for every set in [whether or not the outcome is in that]
F

set. For example, you would be told that the outcome is not in and is in - . Moreover, you might
;
be told that the outcome is not in AH [but is in] AT [.] [In effect, you have been told that the first toss]



be told that the outcome is not in AH [but is in] AT [.] [In effect, you have been told that the first toss]

was a T, and nothing more. The - -algebra [is said to contain the “information of the first toss”,]
F



H [but is in] A



was a T, and nothing more. The - -algebra [is said to contain the “information of the first toss”,]
F

which is usually called the “information up to time ”. Similarly, [contains the “information of]
F




[contains the “information of]


CHAPTER 1.Introduction to Probability Theory 19



the first two tosses,” which is the “information up to time .” The - -algebra
F



the first two tosses,” which is the “information up to time .” The - -algebra = contains “full
F F

information” about the outcome of all three tosses. The so-called “trivial” - -algebra 0 [contains no]
F



information” about the outcome of all three tosses. The so-called “trivial” - -algebra 0 [contains no]
F

information. Knowing whether the outcome ! of the three tosses is in (it is not) and whether it is
;
in - (it is) tells you nothing about !



**Definition 1.3** Let - be a nonempty finite set. A _filtration_ is a sequence of - -algebras
F



; F



; : : : ; F



0 n

such that each - -algebra in the sequence contains all the sets contained by the previous - -algebra.



0



; F



**Definition 1.4** Let - be a nonempty finite set and let be the - -algebra of all subsets of - . A
F
random variable is a function mapping - into IR .



**Example 1.3** Let - be given by (2.1) and consider the binomial asset pricing Example 1.1, where




[.] [Then] S



0 [,] S




[,] S




[and] S




[are] [all] [random] [variables.] [For] [example,]



S0



=, u = and d =



0 [is really not random, since] S



0



0



S



(H H T ) = u



S



= . The “random variable” S



(! ) = for all



! - . Nonetheless, it is a function mapping - into IR, and thus technically a random variable,
albeit a degenerate one.



A random variable maps - into IR, and we can look at the preimage under the random variable of
sets in IR . Consider, for example, the random variable S [of Example 1.1.] [We have]



(H T T ) = S


(T T T ) = :



(H H T ) = ;



S


S


S



(H H H ) = S


(H T H ) = S


(T T H ) = S



(T H H ) = S



(T H T ) = ;



Let us consider the interval [; ] . The preimage under S [of this interval is defined to be]



f! �; S



(! ) [; ]g = f! �; - S



= AcT T

- g



:



The complete list of subsets of - we can get as preimages of sets in IR is:



; �; AH H ; AH T
;



AT H

[



; AT T



;



and sets which can be built by taking unions of these. This collection of sets is a - -algebra, called
the - _-algebra_ _generated_ _by_ _the_ _random_ _variable_ S [,] [and] [is] [denoted] [by] - (S ) . The information



the - _-algebra_ _generated_ _by_ _the_ _random_ _variable_ S [,] [and] [is] [denoted] [by] - (S ) . The information

content of this - -algebra is exactly the information learned by observing S [.] [More] [specifically,]




[,] [and] [is] [denoted] [by]   - (S



content of this - -algebra is exactly the information learned by observing S [.] [More] [specifically,]

suppose the coin is tossed three times and you do not know the outcome !, but someone is willing
to tell you, for each set in - (S ), whether ! is in the set. You might be told, for example, that ! is



to tell you, for each set in - (S ), whether ! is in the set. You might be told, for example, that ! is

not in AH H [, is in] AH T AT H [, and is not in] AT T [.] [Then you know that in the first two tosses, there]



not in AH H [, is in] AH T AT H [, and is not in] AT T [.] [Then you know that in the first two tosses, there]

[

was a head and a tail, and you know nothing more. This information is the same you would have
gotten by being told that the value of S (! ) is .

Note that [defined earlier] [contains all the] [sets which are] [in] - (S ), and even more. This means
F

that the information in the first two tosses is greater than the information in S [. In particular, if you]



H H [, is in] A



H T




[ A



T H [, and is not in] A



(! ) is .



Note that
F




[defined earlier] [contains all the] [sets which are] [in]  - (S



that the information in the first two tosses is greater than the information in S [. In particular, if you]

see the first two tosses, you can distinguish AH T [from] AT H [, but you cannot make this distinction]



see the first two tosses, you can distinguish AH T [from] AT H [, but you cannot make this distinction]

from knowing the value of S [alone.]




[alone.]



H T [from] A


20


**Definition 1.5** Let - be a nonemtpy finite set and let be the - -algebra of all subsets of - . Let X
F
be a random variable on (�; ) . The - _-algebra_ - (X ) _generated by_ X is defined to be the collection
F
of all sets of the form ! �; X (! ) A, where A is a subset of IR . Let be a sub- - -algebra of
f g G

. We say that X _is_ _-measurable_ if every set in  - (X ) is also in .
F G G

Note: We normally write simply X A rather than ! �; X (! ) A .
f g f g

**Definition 1.6** Let - be a nonempty, finite set, let be the - -algebra of all subsets of -, let IP be
F
a probabilty measure on (�; ), and let X be a random variable on - . Given any set A IR, we
F         define the _induced measure_ of A to be



X

L



(A)



=� IP fX Ag:



In other words, the induced measure of a set A tells us the probability that X takes a value in A . In
the case of S [above with the probability measure of Example 1.2, some sets in] IR and their induced

measures are:



S

L

S

L

S

L


S

L



(;) = IP (;) = 0;

(IR) = IP (�) = ;


[0; ) = IP (�) = ;




[0; ] = IP fS







= = IP (AT T ) =
g







:



In fact, the induced measure of S [places a mass of size]











=




[at the number], a mass of size




[at] [the] [number], and a mass of size = [at the] [number] . A common way to record this

information is to give the _cumulative distribution function_ - - FS (x) of S [, defined by]




[at] [the] [number], and a mass of size











S



=




[, defined by]



(x) of S



0; if x < ;



; if x < ;

  



- x) =



=� IP (S










>>



>>

<





<



>>>



>>>



FS



(x)



(2.3)



>>>

:





:



; if x:

   


; if x < ;

  


By the _distribution_ of a random variable X, we mean any of the several ways of characterizing

X [.] [If] X is discrete, as in the case of S [above, we can] [either tell where the masses are] [and how]

L

large they are, or tell what the cumulative distribution function is. (Later we will consider random
variables X which have densities, in which case the induced measure of a set A IR is the integral

                     of the density over the set A .)



X [.] [If] X is discrete, as in the case of S



L



**Important** **Note.** In order to work through the concept of a risk-neutral measure, we set up the
definitions to make a clear distinction between random variables and their distributions.

A _random variable_ is a mapping from - to IR, nothing more. It has an existence quite apart from
discussion of probabilities. For example, in the discussion above, S (T T H ) = S (T T T ) =,



discussion of probabilities. For example, in the discussion above, S (T T H ) = S (T T T ) =,

regardless of whether the probability for H is [or] [.]




[or]




[.]



(T T H ) = S


CHAPTER 1.Introduction to Probability Theory 21



The _distribution_ of a random variable is a measure
L



The _distribution_ of a random variable is a measure X [on] IR, i.e., a way of assigning probabilities
L

to sets in IR . It depends on the random variable X and the probability measure IP we use in - . If we
set the probability of H to be [, then] S [assigns mass] [to the number] . If we set the probability



set the probability of H to be [, then] S [assigns mass] [to the number] . If we set the probability

L

of H to be [, then] S [assigns mass] [to the number] . The distribution of S [has changed, but]




[assigns mass]



of H to be [, then] S [assigns mass] [to the number] . The distribution of S [has changed, but]

L

the random variable has not. It is still defined by




[, then]
L




[assigns mass]




[to the number] . The distribution of S



S



S




[, then]
L



(H H T ) = ;



S


S


S



(H H H ) = S


(H T H ) = S


(T T H ) = S



(H T T ) = S


(T T T ) = :



(T H H ) = S



(T H T ) = ;



Thus, a random variable can have more than one distribution (a “market” or “objective” distribution,
and a “risk-neutral” distribution).

In a similar vein, two _different_ _random variables_ can have the _same_ _distribution_ . Suppose in the
binomial model of Example 1.1, the probability of H and the probability of T is [.] [Consider] [a]



binomial model of Example 1.1, the probability of H and the probability of T is [.] [Consider] [a]

European call with strike price expiring at time . The payoff of the call at time is the random
variable (S )+, which takes the value if ! = H H H or ! = H H T, and takes the value 0 in



variable (S )+, which takes the value if ! = H H H or ! = H H T, and takes the value 0 in

    
every other case. The probability the payoff is is [, and the probability it is zero is] [. Consider also]




- )




[, and the probability it is zero is]



every other case. The probability the payoff is is [, and the probability it is zero is] [. Consider also]

a European put with strike price expiring at time . The payoff of the put at time is ( S )+,

                        


)



a European put with strike price expiring at time . The payoff of the put at time is ( S )+,

                        
which takes the value if ! = T T H or ! = T T T . Like the payoff of the call, the payoff of the
put is with probability [and] 0 with probability [. The payoffs of the call and the put are different]



put is with probability [and] 0 with probability [. The payoffs of the call and the put are different]

random variables having the same distribution.


**Definition 1.7** Let - be a nonempty, finite set, let be the - -algebra of all subsets of -, let IP be
F
a probabilty measure on (�; ), and let X be a random variable on - . The _expected value_ of X is
F
defined to be




[and] 0 with probability



X (! )IP ! : (2.4)
f g



! 
X



IE X



=�



Notice that the expected value in (2.4) is defined to be a sum _over the sample space_ - . Since - is a
finite set, X can take only finitely many values, which we label x ; : : : ; xn [. We can partition] - into



finite set, X can take only finitely many values, which we label x ; : : : ; xn [. We can partition] - into

the subsets X = x ; : : : ; Xn = xn, and then rewrite (2.4) as
f g f g



; : : : ; x



= x



g; : : : ; fX



n



, and then rewrite (2.4) as
g



= x



n



! 
X



xk

k =

X



X

L



xk
f



IE X



=�


=


=


=


=



X (! )IP f! g



! 
n


k =

X



n



g



k =



! fX



Xk

X



k



=x



k



X (! )IP f! g



n



k =

X



k g



xk



Xk =

X



k =



! fX



k



=x



IP f! g



n



k =

X



= xk


g:



g



xk



IP Xk
f



k =



n


22


Thus, although the expected value is defined as a sum over the sample space -, we can also write it
as a sum over IR .

To make the above set of equations absolutely clear, we consider S [with the distribution given by]

(2.3). The definition of IE S [is]



To make the above set of equations absolutely clear, we consider S




[is]



(H H H )IP fH H H g + S



(H H T )IP fH H T g



IE S



= S



+S


+S


+S



(H T H )IP fH T H g + S

(T H H )IP fT H H g + S



(T T H )IP fT T H g + S



(H T T )IP fH T T g

(T H T )IP fT H T g



(T T T )IP fT T T g



= - IP (A

= - IP fS



= g + - IP fS



) + - IP (A




[ A



H H



H T



T H



) + - IP (A



T T



)



= g + - IP fS



= g



= - L



S



f g + - L



S



f g + - L



S



f g



= 


+ 


+ 


=



:



**Definition 1.8** Let - be a nonempty, finite set, let be the - -algebra of all subsets of -, let IP be a
F
probabilty measure on (�; ), and let X be a random variable on - . The _variance_ of X is defined
F
to be the expected value of (X IE X ), i.e.,

        


Var (X )



IP ! : (2.5)
f g



=�



(X (! )  - IE X )

! 
X



One again, we can rewrite (2.5) as a sum over IR rather than over - . Indeed, if X takes the values



x



; : : : ; x



n [, then]



n



Var (X ) =



n


k =

X



(xk




- IE X )



IP X = xk =
f g



k =

X



k =



(xk




- IE X )



X (xk

L



):



**1.3** **Lebesgue Measure and the Lebesgue Integral**


In this section, we consider the set of real numbers IR, which is uncountably infinite. We define the
_Lebesgue measure_ of intervals in IR to be their length. This definition and the properties of measure
determine the Lebesgue measure of many, but not all, subsets of IR . The collection of subsets of

IR we consider, and for which Lebesgue measure is defined, is the collection of _Borel sets_ defined
below.

We use Lebesgue measure to construct the _Lebesgue_ _integral_, a generalization of the Riemann
integral. We need this integral because, unlike the Riemann integral, it can be defined on abstract
spaces, such as the space of infinite sequences of coin tosses or the space of paths of Brownian
motion. This section concerns the Lebesgue integral on the space IR only; the generalization to
other spaces will be given later.


CHAPTER 1.Introduction to Probability Theory 23


**Definition 1.9** The _Borel_ - _-algebra_, denoted (IR), is the smallest - -algebra containing all open
B
intervals in IR . The sets in (IR) are called _Borel sets_ .
B

Every set which can be written down and just about every set imaginable is in (IR) . The following
B
discussion of this fact uses the - -algebra properties developed in Problem 1.3.

By definition, every open interval (a; b) is in (IR), where a and b are real numbers. Since (IR) is
B B
a - -algebra, every union of open intervals is also in (IR) . For example, for every real number a,
B
the _open half-line_



n=

[



(a; a + n)



(a - n; a):



is a Borel set, as is


For real numbers a and b, the union



(a; ) =


(�; a) =



n=

[



n=



(�; a) [ (b; )

is Borel. Since (IR) is a - -algebra, every complement of a Borel set is Borel, so (IR) contains
B B








[a; b] =







(�; a) [ (b; )



c



:



This shows that every closed interval is Borel. In addition, the _closed half-lines_




[a; ) =



n=



n=

[




[a; a + n]



and



(�; a] =



n=



n=

[




[a - n; a]



are Borel. Half-open and half-closed intervals are also Borel, since they can be written as intersections of open half-lines and closed half-lines. For example,



(a; b] = (�; b] \ (a; ):


Every set which contains only one real number is Borel. Indeed, if a is a real number, then



a 



fag =



n=

\



n



n



; a +



:




This means that every set containing finitely many real numbers is Borel; if A = a ; a ; : : : ; an,
f g

then



This means that every set containing finitely many real numbers is Borel; if A = a
f



; a



; : : : ; a



n



n



A =



k =

[



k =

[



ak
f



g:


24


In fact, every set containing countably infinitely many numbers is Borel; if A = a
f

n



; a



; : : :, then
g



A =



k =

[



ak
f



k =



g:



This means that the set of rational numbers is Borel, as is its complement, the set of irrational
numbers.

There are, however, sets which are not Borel. We have just seen that any non-Borel set must have
uncountably many points.


**Example 1.4** (The Cantor set.) _This example gives a hint of how complicated a Borel set can be._
_We use it later when we discuss the sample space for an infinite sequence of coin tosses._

_Consider the unit interval_ [0; ] _, and remove the middle half, i.e., remove the open interval_



;


[







=�







0;



















_The remaining set_



:


;







C



A


=



_has two pieces. From each of these pieces, remove the middle half, i.e., remove the open set_




[











=�








[



;







;



:




_The remaining set_




[




[



k _[has]_



















A


0;



C



=



;







;







;







:



_has four pieces._ _Continue this process, so at stage_ k _, the set_ Ck _[has]_ k _pieces, and each piece has_

_length_ k _[. The]_ [ Cantor set]



_has four pieces._ _Continue this process, so at stage_ k _, the set_ C



k _[. The]_ [ Cantor set]



k =

\



Ck



C



=�



k =



_is defined to be the set of points not removed at any stage of this nonterminating process._



_Note that the length of_ A _[, the first set removed, is]_ _[.]_ _[The “length” of]_ A _[, the second set removed,]_

_is_ + = _[.]_ _[The “length” of the next set removed is]_ = _[, and in general, the length of the]_




_[, the first set removed, is]_



_Note that the length of_ A




_[.]_ _[The “length” of]_ A



+



=




_[.]_ _[The “length” of the next set removed is]_ k    


=




_[, and in general, the length of the]_



k _-th set removed is_



�k _. Thus, the total length removed is_



k =

X



k



= ;



k =



_and so the Cantor set, the set of points not removed, has zero “length.”_



_Despite the fact that the Cantor set has no “length,” there are lots of points in this set. In particular,_
_none of the endpoints of the pieces of the sets_ C ; C ; : : : _is ever removed. Thus, the points_



; C



; : : : _is ever removed. Thus, the points_



0;



;



; ;



;



;



;



;



; : : :



_are_ _all in_ C _._ _This is a countably infinite set of points._ _We shall see_ _eventually that the Cantor set_
_has uncountably many points._ 

CHAPTER 1.Introduction to Probability Theory 25


**Definition 1.10** Let (IR) be the - -algebra of Borel subsets of IR . A _measure on_ (IR; (IR)) is a
B B
function - mapping into [0; ] with the following properties:
B

**(i)** �( ) = 0,
;



**(ii)** If A



; A



; : : : is a sequence of disjoint sets in (IR), then
B



!



k =

X



k =

X



�(Ak



):







k =

[



k =

[



Ak



=



_Lebesgue measure_ is defined to be the measure on (IR; (IR)) which assigns the measure of each
B
interval to be its length. Following Williams’s book, we denote Lebesgue measure by �0 [.]



A measure has all the properties of a probability measure given in Problem 1.4, except that the total
measure of the space is not necessarily (in fact, �0 (IR) = ), one no longer has the equation



(IR) = ), one no longer has the equation



0



�(Ac ) = - �(A)



in Problem 1.4(iii), and property (v) in Problem 1.4 needs to be modified to say:



**(v)** If A




- A



) <, then




- - - - _and_ �(A



; A



; : : : is a sequence of sets in (IR) with A
B



= lim

n!



!



�(An



):



= lim




             

To see that the additional requirment �(A



k =

\



k =

\



) < is needed in (v), consider



Ak



= [; ); A



= [; ); : : : :



A



= [; ); A



Then
\



) = .



=, so ;



0



) = 0, but lim



n!



�0 (An



k =



Ak



Ak



(\



k =



We specify that the Lebesgue measure of each interval is its length, and that determines the Lebesgue
measure of all other Borel sets. For example, the Lebesgue measure of the Cantor set in Example
1.4 must be zero, because of the “length” computation given at the end of that example.



The Lebesgue measure of a set containing only one point must be zero. In fact, since







fag               
for every positive integer n, we must have



a 



; a +

n



n






n



0 �0

 


a �0
f g 


a  



=



n



n



; a +



:



Letting n, we obtain
!



�0 a = 0:

f g


26



The Lebesgue measure of a set containing countably many points must also be zero. Indeed, if



A = fa



; a



; : : :, then
g



�0 (A) =



k =

X



�0



g =



k =

X



k =



0 = 0:



k =



ak
f



The Lebesgue measure of a set containing uncountably many points can be either zero, positive and
finite, or infinite. We may not compute the Lebesgue measure of an uncountable set by adding up
the Lebesgue measure of its individual members, because there is no way to add up uncountably
many numbers. The integral was invented to get around this problem.



In order to think about Lebesgue integrals, we must first consider the functions to be integrated.



**Definition 1.11** Let f be a function from IR to IR . We say that f is _Borel-measurable_ if the set

x IR; f (x) A is in (IR) whenever A (IR) . In the language of Section 2, we want the
f g B B

- _-algebra generated by_ f to be contained in (IR) .
B

Definition 3.4 is purely technical and has nothing to do with keeping track of information. It is
difficult to conceive of a function which is not Borel-measurable, and we shall pretend such functions don’t exist. Hencefore, “function mapping IR to IR ” will mean “Borel-measurable function
mapping IR to IR ” and “subset of IR ” will mean “Borel subset of IR ”.


**Definition 1.12** An _indicator function_ g from IR to IR is a function which takes only the values 0
and . We call



A







= fx IR; g (x) = g



the set _indicated_ by g . We define the _Lebesgue integral_ of g to be



IR

Z



(A):



g d�0



=� 






0



A _simple function_ h from IR to IR is a linear combination of indicators, i.e., a function of the form


n



h(x) =



k =

X



ck



gk



(x);



where each gk [is of the form]



;

;



; if x A

0; if x = A



; if x A



(



k


k



gk



(x) =



and each c



k [is a real number. We define the] _[ Lebesgue integral]_ [ of] h to be



R

Z



n



IR

Z



k =

X



ck



n


k =

X



ck



):



h d�0



=�







gk



d�0



=



�0



(Ak



Let f be a nonnegative function defined on IR, possibly taking the value at some points. We
define the _Lebesgue integral_ of f to be



IR

Z







IR

�Z



h d�0 ; h is simple and h(x) f (x) for every x IR

        


f d�0



=� sup



:


CHAPTER 1.Introduction to Probability Theory 27


It is possible that this integral is infinite. If it is finite, we say that f _is integrable_ .

Finally, let f be a function defined on IR, possibly taking the value at some points and the value

at other points. We define the _positive_ and _negative parts_ of f to be
�







+







= maxff (x); 0g; f



(x)







= maxf�f (x); 0g;



f



(x)



respectively, and we define the _Lebesgue integral_ of f to be



Z



d�0



Z



d�0



d�



I

Z



IR



f d�0



=�



IR



f +




- 


f







d�



;



IR



provided the right-hand side is not of the form . If both

             


provided the right-hand side is not of the form . If both IR f + d�0 [and] IR f - d�0 [are finite]

(or equivalently, IR jf j d�0 <, since jf j = f + �+ f - ), we say that R f is _integrable_ R .

Let f be a function defined on R IR, possibly taking the value at some points and the value at
�
other points. Let A be a subset of IR . We define



R



R



IR



d�



0 [and]



+







f



f



IR



d�



R



jf j d�



+ f




- ), we say that f is _integrable_ .



IR



+



0



<, since f = f
j j



IR

Z



lIA



f d�0



f d�



f d�0



=�







;



where


is the _indicator function of_ A .



A

Z



; if x A;

0; if x = A;



(



lIA (x)



=�



The Lebesgue integral just defined is related to the Riemann integral in one very important way: if

b

the Riemann integral f (x)dx is defined, then the Lebesgue integral f d�0 [agrees] [with the]



b

Riemann integral.the Riemann integralThe Lebesgue integral has two important advantages over the Riemann integral. a f (x)dx is defined, then the Lebesgue integral [a;b] f d�0 [agrees] [with the]

R R

The first is that the Lebesgue integral is defined for more functions, as we show in the following
examples.



R




[a;b]



b

a



R



f (x)dx is defined, then the Lebesgue integral



f d�



**Example 1.5** Let Q be the set of rational numbers in [0; ], and consider f



**Example 1.5** Let Q be the set of rational numbers in [0; ], and consider f =� lIQ [. Being a countable]

set, Q has Lebesgue measure zero, and so the Lebesgue integral of f over [0; ] is







= lI




[0;]

Z



f d�0



= 0:



To compute the Riemann integral



;

R



0



k [, where] f (q



< x



f (x)dx, we choose partition points 0 = x



xn = and divide the interval [0; ] into subintervals [x0 ; x ]; [x ; x ]; : : : ; [xn� ; xn ] . In each

subinterval [xk ; xk ] there is a rational point qk [, where] f (qk ) =, and there is also an irrational



0



0



x



]; [x



; x



]; : : : ; [x



n�



; x



n



= and divide the interval [0; ] into subintervals [x



n



< - - - <



subinterval [xk - ; xk ] there is a rational point qk [, where] f (qk ) =, and there is also an irrational

point rk [, where] f (rk ) = 0 . We approximate the Riemann integral from above by the _upper sum_



; x



k



; x



] there is a rational point q



) = 0 . We approximate the Riemann integral from above by the _upper sum_



k 


k


k



k [, where] f (r



n



n



k =

X



f (qk )(xk




- xk - ) =



k =

X



k =




- xk 


) = ;


) = 0:



k =



(xk




and we also approximate it from below by the _lower sum_



n


k =

X



f (rk )(xk




- xk - ) =



n

0 (xk

    
k =

X




- xk 

28


No matter how fine we take the partition of [0; ], the upper sum is always and the lower sum is
always 0 . Since these two do not converge to a common value as the partition becomes finer, the
Riemann integral is not defined.

                                       
**Example 1.6** Consider the function



; if x = 0;

0; if x = 0:



=�







(



f (x)



This is not a simple function because simple function cannot take the value . Every simple
function which lies between 0 and f is of the form



y ; if x = 0;

0; if x = 0;



(



h(x)



=�



for some y [0; ), and thus has Lebesgue integral



IR

Z



f0g = 0:



h d�0



= y �0



= y 


It follows that



IR

Z







�Z



= 0:



f d�0



= sup



IR



h d�0 ; h is simple and h(x) f (x) for every x IR

        


Now consider the Riemann integral



Now consider the Riemann integral f (x) dx, which for this function f is the same as the

�

Riemann integral f (x) dx . When we partition R [ ; ] into subintervals,one of these will contain



R



�



Riemann integral f (x) dx . When we partition [ ; ] into subintervals,one of these will contain

       -       
the point 0, and when R we compute the upper approximating sum for f (x) dx, this point will



R











R



the point 0, and when we compute the upper approximating sum for f (x) dx, this point will

                         
contribute times the length of the subinterval containing it. Thus the upper approximating sum is

R

. On the other hand, the lower approximating sum is 0, and again the Riemann integral does not
exist.

                                       
The Lebesgue integral has all _linearity_ and _comparison_ properties one would expect of an integral.
In particular, for any two functions f and g and any real constant c,



IR

Z



IR

Z



(f + g ) d�0



=



Z



IR



IR

Z



g d�0



+



;



f d�0



IR

Z



f d�0



cf d�0



= c



;



and whenever f (x) g (x) for all x IR, we have

     


IR

Z

Finally, if A and B are disjoint sets, then



IR

Z



f d�0



f d�







g d d�0:



A B

Z [



A

Z



f d�0



f d�0



f d�0



f d�



=



+



B

Z



f d�



:


CHAPTER 1.Introduction to Probability Theory 29



There are three _convergence_ _theorems_ satisfied by the Lebesgue integral. In each of these the situation is that there is a sequence of functions fn ; n = ; ; : : : converging _pointwise_ to a limiting



uation is that there is a sequence of functions fn ; n = ; ; : : : converging _pointwise_ to a limiting

function f . _Pointwise convergence_ just means that



n



fn (x) = f (x) for every x IR:



lim

n!



There are no such theorems for the Riemann integral, because the Riemann integral of the limiting function f is too often not defined. Before we state the theorems, we given two examples of
pointwise convergence which arise in probability theory.


**Example 1.7** Consider a sequence of normal densities, each with variance and the n -th having
mean n :



p 


(x n)

e� 


fn (x)



=�



:



These converge pointwise to the function


f (x) = 0 for every x IR:



We have



R



IR



R



IR



R



IR



0



=, but



= 0 .

        


fn



d�



fn



d�0



d�



f d�0



= for every n, so lim



n!



**Example 1.8** Consider a sequence of normal densities, each with mean 0 and the n -th having variance [:]



n [:]



n

 


r



x

e� n



=�



fn


These converge pointwise to the function


f (x)



(x)



=�



:



; if x = 0;

0; if x = 0:







(



n!



IR



We have again IR fn d�0 = for every n, so lim n! IR fn d�0 =, but IR f d�0 = 0 . The

function f is not the Dirac delta; the Lebesgue integral of this function was already seen in Example

R R R

1.6 to be zero.

                                       


We have again



R



IR



R



IR



0



0



d�



I

R



d�



0



f



n



f d�



f



n



= for every n, so lim



=, but



**Theorem 3.1** (Fatou’s Lemma) _Let_ f



**Theorem 3.1** (Fatou’s Lemma) _Let_ fn ; n = ; ; : : : _be a sequence of nonnegative functions con-_

_verging pointwise to a function_ f _._ _Then_



n



IR

Z



Z



f d�0



lim inf

- n

!



IR



d�0



:



fn



If lim n!



IR

R



Z



fn



d�0 [is defined, then Fatou’s Lemma has the simpler conclusion]



IR

Z



fn



d�0



:



IR



f d�0



lim

- n

!



lim

- n



This is the case in Examples 1.7 and 1.8, where



lim

n!



lim



IR

Z



fn



d�0



= ;


30



while



IR



0



while IR f d�0 = 0 . We could modify either Example 1.7 or 1.8 by setting gn = fn [if] n is even,

but gn = fn [if] n is odd. Now gn d�0 = if n is even, but gn d�0 = if n is odd. The

R



R



R



g



= 0 . We could modify either Example 1.7 or 1.8 by setting g



= f



f d�



n [if] n is odd. Now



but gn = fn [if] n is odd. Now IR gn d�0 = if n is even, but IR gn d�0 = if n is odd. The

sequence f IR gn d�0 gn= [has] [two] R [cluster] [points,] and . By definition, R the smaller one,, is

lim inf n!R IR gn d�0 [and the larger one,], is lim sup n! IR gn d�0 [. Fatou’s Lemma guarantees]

that even the smaller cluster point will be greater than or equal to the integral of the limiting function.

R R



R



IR



IR



n



n



= f



g



d�



0



d�



0



n



g



n



= if n is even, but



d�



0



g



0 [and the larger one,], is lim sup



IR



n

g



n= [has] [two] [cluster] [points,] and . By definition, the smaller one,, is



IR



lim inf



IR



n!



R



d�



n!



R



d�



R



g



n



n



The key assumption in Fatou’s Lemma is that all the functions take only nonnegative values. Fatou’s
Lemma does not assume much but it is is not very satisfying because it does not conclude that



IR

Z



Z



f d�0



= lim

n!



IR



fn



d�0



d�



:



There are two sets of assumptions which permit this stronger conclusion.



**Theorem 3.2** (Monotone Convergence Theorem) _Let_ f



**Theorem 3.2** (Monotone Convergence Theorem) _Let_ fn ; n = ; ; : : : _be a sequence of functions_

_converging pointwise to a function_ f _._ _Assume that_



n



0 - f



(x) - f



(x) - f



(x) - - - - _for every_ x IR:



_Then_



Z



Z



= lim

n!



IR



fn



d�0



d�



;



IR



f d�0



_where both sides are allowed to be_ _._



**Theorem 3.3** (Dominated Convergence Theorem) _Let_ f



**Theorem 3.3** (Dominated Convergence Theorem) _Let_ fn ; n = ; ; : : : _be a sequence of functions,_

_which_ _may_ _take_ _either positive or_ _negative_ _values,_ _converging pointwise to_ _a_ _function_ f _._ _Assume_
_that there is a nonnegative integrable function_ g _(i.e.,_ g d�0 < _) such that_



n



IR



g d�



0



< _) such that_



(x)j - g (x) _for every_ x IR _for every_ n:



fn
j



R



_Then_


_and both sides will be finite._



IR

Z



Z



f d�0



= lim

n!



IR



fn



d�0



d�



;



**1.4** **General Probability Spaces**


**Definition 1.13** A _probability space_ (�; ; IP ) consists of three objects:
F

**(i)** -, a nonempty set, called the _sample_ _space_, which contains all possible outcomes of some
random experiment;


**(ii)**, a - -algebra of subsets of - ;
F

**(iii)** IP, a probability measure on (�; ), i.e., a function which assigns to each set A a number
F F

IP (A) [0; ], which represents the probability that the outcome of the random experiment
lies in the set A .


CHAPTER 1.Introduction to Probability Theory 31


**Remark 1.1** We recall from Homework Problem 1.4 that a probabilitymeasure IP has the following
properties:



**(a)** IP ( ) = 0 .
;

**(b)** (Countable additivity) If A



; A



; : : : is a sequence of disjoint sets in, then
F



k =

X



k =

X



IP (Ak



):



IP



k =

[



=

[



Ak



!



=



**(c)** (Finite additivity) If n is a positive integer and A



; : : : ; An [are disjoint sets in], then

F



IP (A



An ) = IP (A

[ - - - [



) + + IP (An

   -    -    


):



**(d)** If A and B are sets in and A B, then
F        


In particular,


**(d)** (Continuity from below.) If A


**(d)** (Continuity from above.) If A



IP (B ) = IP (A) + IP (B n A):


IP (B )    - IP (A):



, then

- - - 

, then

- - - 


; A



; : : : is a sequence of sets in with A
F



= lim

n!



Ak

!



IP (An



):



IP



k =

[



= lim




- A


- A



; A



; : : : is a sequence of sets in with A
F



= lim

n!



Ak

!



IP (An



):



IP



k =

\



= lim



We have already seen some examples of finite probability spaces. We repeat these and give some
examples of infinite probability spaces as well.


**Example 1.9** Finite coin toss space.
Toss a coin n times, so that - is the set of all sequences of H and T which have n components.
We will use this space quite a bit, and so give it a name: �n [.] [Let] be the collection of all subsets



We will use this space quite a bit, and so give it a name: �n [.] [Let] be the collection of all subsets

F
of �n [.] [Suppose the probability of] H on each toss is p, a number between zero and one. Then the



of �n [.] [Suppose the probability of] H on each toss is p, a number between zero and one. Then the

probability of T is q =� p . For each ! = (! ; ! ; : : : ; !n ) in �n [, we define]



=� p . For each ! = (!

 






; !



; : : : ; !



n



) in 


n [, we define]




- q N umber of T in !



:



N umber of H in !



IP f! g

For each A, we define
F



=� p







! A

X



IP (A)



=�



! A



IP ! : (4.1)
f g



We can define IP (A) this way because A has only finitely many elements, and so only finitely many
terms appear in the sum on the right-hand side of (4.1).

                                       

32


**Example 1.10** Infinite coin toss space.
Toss a coin repeatedly without stopping, so that - is the set of all nonterminating sequences of H
and T . We call this space - [.] [This is an uncountably infinite space, and we need to exercise some]

care in the construction of the - -algebra we will use here.



For each positive integer n, we define
F



For each positive integer n, we define n [to be the] - -algebra determined by the first n tosses. For
F

example, [contains four basic sets,]
F




[contains four basic sets,]



; !



= H ; !



= H g



AH H


AH T


AT H


AT T







= f! = (!



= f! = (!



; !



; : : : ); !



= The set of all sequences which begin with H H ;







; !



= f! = (!



= H ; !



= T g



; !



; : : : ); !



= The set of all sequences which begin with H T ;







; !



= f! = (!



= T ; !



= H g



; !



; : : : ); !



= The set of all sequences which begin with T H ;







; !



= T ; !



= T g



; !



; : : : ); !



= The set of all sequences which begin with T T :



Because [is] [a] - -algebra, we must also put into it the sets, -, and all unions of the four basic
F ;

sets.



In the - -algebra, we put every set in every - -algebra n [,] [where] n ranges over the positive
F F

integers. We also put in every other set which is required to make be a - -algebra. For example,
F
the set containing the single sequence


H H H H H = H on every toss
f             -             -             - g f g



is not in any of the
F



is not in any of the n - -algebras, because it depends on all the components of the sequence and
F

not just the first n components. However, for each positive integer n, the set



n



H on the first n tosses
f g



is in
F



n [and hence in] . Therefore,
F

H on every toss =
f g



n=

\



n=



H on the first n tosses
f g



is also in .
F



We next construct the probability measure IP on (�



; ) which corresponds to probability p
F




[0; ] for H and probability q = p for T . Let A be given. If there is a positive integer n

         - F
such that A n [, then the description of] A depends on only the first n tosses, and it is clear how to
F



such that A n [, then the description of] A depends on only the first n tosses, and it is clear how to
F

define IP (A) . For example, suppose A = AH H AT H [, where these sets were defined earlier. Then]




[ A



) = q p, and then we have



T H [, where these sets were defined earlier. Then]



T H



A is in
F




[.] [We set] IP (A



H H



) = p



H H



and IP (A



IP (A) = IP (AH H



AT H ) = p

[



+ q p = (p + q )p = p:



In other words, the probability of a H on the second toss is p .


CHAPTER 1.Introduction to Probability Theory 33


Let us now consider a set A for which there is no positive integer n such that A . Such
F F
is the case for the set H on every toss . To determine the probability of these sets, we write them
f g
in terms of sets which are in n [for] [positive integers] n, and then use the properties of probability
F

measures listed in Remark 1.1. For example,



H on the first toss H on the first two tosses
f g - f g



H on the first three tosses

- f g




- - - - ;



and



n=

\



n=



H on the first n tosses = H on every toss :
f g f g



According to Remark 1.1(d) (continuity from above),



IP H on every toss = lim
f g n

!



IP H on the first n tosses = lim
f g n

!



pn



:



If p =, then IP H on every toss = ; otherwise, IP H on every toss = 0 .
f g f g



A similar argument shows that if 0 < p < so that 0 < q <, then every set in 


A similar argument shows that if 0 < p < so that 0 < q <, then every set in - [which contains]

only one element (nonterminating sequence of H and T ) has probability zero, and hence very set
which contains countably many elements also has probabiliy zero. We are in a case very similar to
Lebesgue measure: every point has measure zero, but sets can have positive measure. Of course,
the only sets which can have positive probabilty in - [are those which contain uncountably many]



the only sets which can have positive probabilty in - [are those which contain uncountably many]

elements.



In the infinite coin toss space, we define a sequence of random variables Y



; Y



; : : : by



if !k

0 if !k



(



= H ;

= T ;



=�



Yk



(! )



and we also define the random variable



X (! ) =



n


k =

X



Yk (! )

k



:



Since each Y



k [is either zero or one,] X takes values in the interval [0; ] . Indeed, X (T T T T ) = 0,

                                                      -                                                       -                                                       


X (H H H H ) = and the other values of X lie in between. We define a “dyadic rational
number” to be - - - a number of the form mk [,] [where] k and m are integers. For example, [is a] [dyadic]



number” to be a number of the form mk [,] [where] k and m are integers. For example, [is a] [dyadic]

rational. Every dyadic rational in (0,1) corresponds to two sequences ! - [. For example,]



k [,] [where] k and m are integers. For example,



m




[. For example,]



X (H H T T T T T - - - ) = X (H T H H H H H - - - ) =



:



The numbers in (0,1) which are not dyadic rationals correspond to a single ! - [; these numbers]

have a unique binary expansion.


34



Whenever we place a probability measure IP on (�; ), we have a corresponding induced measure
F



X [on] [0; ] . For example, if we set p = q =




[in the construction of this example, then we have]



L



X

L


X

L


X

L


X

L


X

L


X

L












0;



;


0;


;


;


;













= IP First toss is T =
f g

= IP First toss is H =
f g



= IP First two tosses are T T =
f g

= IP First two tosses are T H =
f g

= IP First two tosses are H T =
f g

= IP First two tosses are H H =
f g



;


;



;








;


;


:



Continuing this process, we can verify that for any positive integers k and m satisfying



<


m

;

k



0 


m

k






- ;



we have



m 
k


m 
k



X

L







=



k



:



In other words, the X [-measure of all intervals in] [0; ] whose endpoints are dyadic rationals is the
L

same as the Lebesgue measure of these intervals. The only way this can be is for X [to be Lebesgue]
L



In other words, the
L



same as the Lebesgue measure of these intervals. The only way this can be is for X [to be Lebesgue]
L

measure.



It is interesing to consider what
L



It is interesing to consider what X [would look like if we take a value of] p other than [when we]
L

construct the probability measure IP on - .

We conclude this example with another look at the Cantor set of Example 3.2. Let �pair s [be] [the]

subset of - in which every even-numbered toss is the same as the odd-numbered toss immediately
preceding it. For example, H H T T T T H H is the beginning of a sequence in �pair s [, but] H T is not.



X [would look like if we take a value of] p other than



We conclude this example with another look at the Cantor set of Example 3.2. Let 


preceding it. For example, H H T T T T H H is the beginning of a sequence in �pair s [, but] H T is not.

Consider now the set of real numbers



C 0



=� X (! ); ! �pair s
f



g:



The numbers between (



;



) can be written as X (! ), but the sequence ! must begin with either



0 . Similarly, the numbers between (



T H or H T . Therefore, none of these numbers is in C



T H H T C 0 ( ; )

can be written as X (! ), but the sequence ! must begin with T T T H or T T H T, so none of these
numbers is in C 0 . Continuing this process, we see that C 0 will not contain any of the numbers which



;



numbers is in C 0 . Continuing this process, we see that C 0 will not contain any of the numbers which

were removed in the construction of the Cantor set C in Example 3.2. In other words, C 0 C .



0 . Continuing this process, we see that C 0



were removed in the construction of the Cantor set C in Example 3.2. In other words, C 0 - C .

With a bit more work, one can convince onself that in fact C 0 = C, i.e., by requiring consecutive



0



With a bit more work, one can convince onself that in fact C 0 = C, i.e., by requiring consecutive

coin tosses to be paired, we are removing exactly those points in [0; ] which were removed in the
Cantor set construction of Example 3.2.

                                       


0


CHAPTER 1.Introduction to Probability Theory 35


In addition to tossing a coin, another common random experiment is to pick a number, perhaps
using a random number generator. Here are some probability spaces which correspond to different
ways of picking a number at random.



**Example 1.11**
Suppose we choose a number from IR in such a way that we are sure to get either, or .
Furthermore, we construct the experiment so that the probability of getting is [, the probability of]



Furthermore, we construct the experiment so that the probability of getting is [, the probability of]

getting is [and the probability of getting] is [.] [We describe this random experiment by taking]




[and the probability of getting] is




[.] [We describe this random experiment by taking]




- to be IR, to be (IR), and setting up the probability measure so that
F B



IP f g =



; IP f g =



; IP f g =



:



This determines IP (A) for every set A (IR) . For example, the probability of the interval (0; ]
B
is [, because this interval contains the numbers] and, but not the number .



The probability measure described in this example is
L




[, the measure] [induced by the stock price]



S [, when the initial stock price] S0 = and the probabilityof H is [. This distributionwas discussed]

immediately following Definition 2.8.

                                       



[, when the initial stock price] S



0



S



S



= and the probabilityof H is



**Example 1.12** Uniform distribution on [0; ] .
Let - = [0; ] and let = ([0; ]), the collection of all Borel subsets containined in [0; ] . For
F B
each Borel set A [0; ], we define IP (A) = �0 (A) to be the Lebesgue measure of the set. Because

     


(A) to be the Lebesgue measure of the set. Because



0







0




[0; ] =, this gives us a probability measure.



This probability space corresponds to the random experiment of choosing a number from [0; ] so
that every number is “equally likely” to be chosen. Since there are infinitely mean numbers in [0; ],
this requires that every number have probabilty zero of being chosen. Nonetheless, we can speak of
the probability that the number chosen lies in a particular set, and if the set has uncountably many
points, then this probability can be positive.

                                       
I know of no way to design a physical experiment which corresponds to choosing a number at
random from [0; ] so that each number is equally likely to be chosen, just as I know of no way to
toss a coin infinitely many times. Nonetheless, both Examples 1.10 and 1.12 provide probability
spaces which are often useful approximations to reality.


**Example 1.13** Standard normal distribution.
Define the standard normal density



:



p 


x

 
e



'(x)



=�



Let - = IR, = (IR) and for every Borel set A IR, define
F B    


A

Z



' d�0



IP (A)



=�



: (4.2)


36


If A in (4.2) is an interval [a; b], then we can write (4.2) as the less mysterious Riemann integral:



x



dx:



b


a

Z



p 



 
e



IP [a; b]



=�



This corresponds to choosing a point at random on the real line, and every single point has probability zero of being chosen, but if a set A is given, then the probability the point is in that set is given
by (4.2).

                                       
The construction of the integral in a general probability space follows the same steps as the construction of Lebesgue integral. We repeat this construction below.


**Definition 1.14** Let (�; ; IP ) be a probability space, and let X be a random variable on this space,
F
i.e., a mapping from - to IR, possibly also taking the values .
�

If X is an _indicator_, i.e,

  


if ! A;



X (! ) = lIA



(



0 if ! A



c



;



for some set A, we define
F


If X is a _simple function_, i.e,




(! ) =


X dIP


n




 
Z



=� IP (A):



X (! ) =



k =

X



ck



lIAk (! );



k =



where each c



k [is a real number and each] A



k [is a set in], we define
F



Z



n



ck



n


k =

X



ck IP (Ak



):



X dIP




=�







k =

X




 
Z



lIAk



dIP =



If X is _nonnegative_ but otherwise general, we define





 
Z



X dIP



Y dIP ; Y is simple and Y (! ) X (! ) for every ! 
        
                


=� sup




 
�Z



:



In fact, we can always construct a sequence of simple functions Y



n



; n = ; ; : : : such that



0 - Y



(! ) - Y



(! ) - Y



(! ) : : : for every ! �;

 


and Y (! ) = lim



n!



(! ) for every ! - . With this sequence, we can define



Yn



X dIP


 
Z







= lim



n!




 
Z



Yn



dIP :


CHAPTER 1.Introduction to Probability Theory 37



If X is _integrable_, i.e,



where




 
Z



+



X




 
Z







X



dIP < ;



dIP < ;



(! ) =� maxf�X (! ); 0g;







=� maxfX (! ); 0g; X







X



+ (! )



then we define




 
Z




 
Z




 
Z



X



X dIP



=�



X



+



dIP - 






dIP :



If A is a set in and X is a random variable, we define
F



Z



Z



lIA



X dIP



=�








- X dIP :



A







The _expectation_ of a random variable X is defined to be



X dIP :


 
Z



IE X



=�



The above integral has all the linearity and comparison properties one would expect. In particular,
if X and Y are random variables and c is a real constant, then




 
Z



Z



Z



X dIP +


X dP ;



(X + Y ) dIP =



Z



Y dIP ;


 
Z







cX dIP = c











If X (! ) Y (! ) for every ! -, then

   


Z



Z







Y dIP :







X dIP 


In fact, we don’t need to have X (! ) Y (! ) for _every_ ! - in order to reach this conclusion; it is

          enough if the set of ! for which X (! ) Y (! ) has probability one. When a condition holds with

           probability one, we say it holds _almost surely_ . Finally, if A and B are disjoint subsets of - and X
is a random variable, then



A B

Z [



X dIP =



A

Z



X dIP +



B

Z



X dIP :



We restate the Lebesgue integral convergence theorem in this more general context. We acknowledge in these statements that conditions don’t need to hold for every ! ; almost surely is enough.



**Theorem 4.4** (Fatou’s Lemma) _Let_ X



**Theorem 4.4** (Fatou’s Lemma) _Let_ Xn ; n = ; ; : : : _be a sequence of almost surely nonnegative_

_random variables converging almost surely to a random variable_ X _. Then_



n



X dIP lim inf

  - n

!



X dIP lim inf

  - n




 
Z



Xn dIP ;



_or equivalently,_




 
Z



IE X lim inf

  - n

!



IE Xn :


38



**Theorem 4.5** (Monotone Convergence Theorem) _Let_ X



**Theorem 4.5** (Monotone Convergence Theorem) _Let_ Xn ; n = ; ; : : : _be_ _a_ _sequence of random_

_variables converging almost surely to a random variable_ X _. Assume that_



n




- X




- X




- - - - _almost surely_ :



_Then_


_or equivalently,_



0 - X

Z



X dIP = lim

n!



X dIP = lim




 
Z



Xn



dIP ;







IE X = lim

n!



IE X = lim



IE Xn



:



**Theorem 4.6** (Dominated Convergence Theorem) _Let_ X



**Theorem 4.6** (Dominated Convergence Theorem) _Let_ Xn ; n = ; ; : : : _be a sequence of random_

_variables, converging_ _almost_ _surely to_ _a_ _random_ _variable_ X _._ _Assume_ _that_ _there_ _exists_ _a_ _random_
_variable_ Y _such that_



n



_Then_


_or equivalently,_



Xn Y _almost surely for every_ n:
j j 



 
Z



X dIP = lim

n!



X dIP = lim




 
Z



Xn



dIP ;



IE X = lim

n!



IE X = lim



IE Xn



:



In Example 1.13, we constructed a probability measure on (IR; (IR)) by integrating the standard
B
normal density. In fact, whenever ' is a nonnegative function defined on R satisfying ' d�0 =,



normal density. In fact, whenever ' is a nonnegative function defined on R satisfying IR ' d�0 =,

we call ' a _density_ and we can define an associated probability measure by

R



R



IR



' d�



0



Z



IP (A)



=�



A



' d�0 [for every] A (IR): (4.3)

B



We shall often have a situation in which two measure are related by an equation like (4.3). In fact,
the market measure and the risk-neutral measures in financial markets are related this way. We say
that ' in (4.3) is the _Radon-Nikodym derivative_ of dIP with respect to �0 [, and we write]



0 [, and we write]



' =



dIP

d�0



: (4.4)



The probability measure IP weights different parts of the real line according to the density ' . Now
suppose f is a function on (R; (IR); IP ) . Definition 1.14 gives us a value for the abstract integral
B



f dIP :



We can also evaluate



Z



IR

Z



;



IR



f ' d�0



which is an integral with respec to Lebesgue measure over the real line. We want to show that



IR

Z



f dIP =



IR

Z



f ' d�0



; (4.5)


CHAPTER 1.Introduction to Probability Theory 39



an equation which is suggested by the notation introduced in (4.4) (substitute



dIP

d�



an equation which is suggested by the notation introduced in (4.4) (substitute d�dIP0 [for] ' in (4.5) and

“cancel” the d�0 [).] [We] [include a] [proof] [of] [this because] [it allows us to] [illustrate the] [concept of] [the]



0
“cancel” the d�0 [).] [We] [include a] [proof] [of] [this because] [it allows us to] [illustrate the] [concept of] [the]

_standard machine_ explained in Williams’s book in Section 5.12, page 5.



The standard machine argument proceeds in four steps.



**Step 1.** Assume that f is an _indicator function_, i.e., f (x) = lI



Assume that f is an _indicator function_, i.e., f (x) = lIA (x) for some Borel set A IR . In

                      that case, (4.5) becomes



A



IP (A) =



Z



' d�0



:



A



This is true because it is the definition of IP (A) .



**Step 2.** Now that we know that (4.5) holds when f is an indicator function, assume that f is a
_simple function_, i.e., a linear combination of indicator functions. In other words,


n



k =

X



f (x) =



ck



hk



(x);



where each c



k [is a real number and each] hk [is an indicator function. Then]



n



IR

Z



f dIP =


=


=


=


=



IR

Z

n


k =

X



k =

X


IR

Z


IR

Z



"



f ' d�0



k =

X



ck



hk

#



dIP



k =



dIP


' d�0



ck



k =



n



k =

X



ck



hk


hk



"



IR

Z


IR

Z

n



k =

X



ck



hk

#


:



' d�0



k =



**Step 3.** Now that we know that (4.5) holds when f is a simple function, we consider a general
nonnegative function f . We can always construct a sequence of nonnegative simple functions



fn



; n = ; ; : : : such that



0 - f



(x) - f



(x) - f



(x) : : : for every x IR;

 


and f (x) = lim



n!



(x) for every x IR . We have already proved that



fn



Z



Z



dIP =



IR



IR



fn



fn ' d�0 [for every] n:



We let n and use the Monotone Convergence Theorem on both sides of this equality to
!
get



IR

Z



f dIP =



IR

Z



f ' d�0 :


40


**Step 4.** In the last step, we consider an _integrable_ function f, which can take both positive and
negative values. By _integrable_, we mean that



dIP < :



f +



dIP < ;



f



IR

Z







¿From Step 3, we have



IR

Z



Z

Z



Z

Z



IR


IR



+





dIP =


dIP =



' d�0



' d�0



;


:



IR


IR



f


f



f


f



+





Subtracting these two equations, we obtain the desired result:



IR

Z



f dIP =


=


=



f


IR







dIP 

' d�0







Z

Z

Z



Z



IR

Z



+


+






f



dIP



IR



f


f



' d�0



IR



:



R



f ' d�0



**1.5** **Independence**


In this section, we define and discuss the notion of independence in a general probability space

(�; ; IP ), although most of the examples we give will be for coin toss space.
F


**1.5.1** **Independence of sets**


**Definition 1.15** We say that two sets A and B are _independent_ if
F F

IP (A \ B ) = IP (A)IP (B ):

Suppose a random experiment is conducted, and ! is the outcome. The probability that ! A is

IP (A) . Suppose you are not told !, but you are told that ! B . Conditional on this information,
the probability that ! A is



IP (A \ B )

IP (B )



IP (AjB )



=�



:



The sets A and B are independent if and only if this conditional probability is the uncondidtional
probability IP (A), i.e., knowing that ! B does not change the probability you assign to A . This
discussion is symmetric with respect to A and B ; if A and B are independent and you know that

! A, the conditional probability you assign to B is still the unconditional probability IP (B ) .

Whether two sets are independent depends on the probability measure IP . For example, suppose we
toss a coin twice, with probability p for H and probability q = p for T on each toss. To avoid

                 trivialities, we assume that 0 < p < . Then



IP fH H g = p



; IP fH T g = IP fT H g = pq ; IP fT T g = q



: (5.1)


CHAPTER 1.Introduction to Probability Theory 41


Let A = H H ; H T and B = H T ; T H . In words, A is the set “ H on the first toss” and B is the
f g f g
set “one H and one T .” Then A B = H T . We compute
\ f g



IP (A) = p



+ pq = p;



IP (B ) = pq ;


IP (A)IP (B ) = p

IP (A \ B ) = pq :



q ;



These sets are independent if and only if p



q = pq, which is the case if and only if p =




[.]



If p = [,] [then] IP (B ), the probability of one head and one tail, is [.] [If] [you] [are] [told that the] [coin]

tosses resulted in a head on the first toss, the probability of B, which is now the probability of a T
on the second toss, is still [.]



If p =




[,] [then] IP (B ), the probability of one head and one tail, is




[.]



Suppose however that p = 0:0 . By far the most likely outcome of the two coin tosses is T T, and
the probability of one head and one tail is quite small; in fact, IP (B ) = 0:0  . However, if you
are told that the first toss resulted in H, it becomes very likely that the two tosses result in one head
and one tail. In fact, conditioned on getting a H on the first toss, the probability of one H and one

T is the probability of a T on the second toss, which is 0: .


         **1.5.2** **Independence of** **-algebras**


**Definition 1.16** Let and be sub- - -algebras of . We say that and are _independent_ if every
G H F G H
set in is independent of every set in, i.e,
G H

IP (A B ) = IP (A)IP (B ) for every A ; B :
\ H G

**Example 1.14** Toss a coin twice, and let IP be given by (5.1). Let = [be] [the] - -algebra
G F

determined by the first toss: contains the sets
G

;; �; fH H ; H T g; fT H ; T T g:

Let be the - -albegra determined by the second toss: contains the sets
H H

;; �; fH H ; T H g; fH T ; T T g:

These two - -algebras are independent. For example, if we choose the set H H ; H T from and
f g G
the set H H ; T H from, then we have
f g H



IP fH H ; H T gIP fH H ; T H g = (p



+ pq )(p



+ pq ) = p



;







= IP fH H g = p



IP







fH H ; H T g \ fH H ; T H g



:



No matter which set we choose in and which set we choose in, we will find that the product of
G H
the probabilties is the probability of the intersection.


42


Example 1.14 illustrates the general principle that when the probability for a sequence of tosses is
defined to be the product of the probabilities for the individual tosses of the sequence, then every
set depending on a particular toss will be independent of every set depending on a different toss.
We say that the different tosses are independent when we construct probabilities this way. It is also
possible to construct probabilities such that the different tosses are not independent, as shown by
the following example.


**Example 1.15** Define IP for the individual elements of - = H H ; H T ; T H ; T T to be
f g



IP fH H g =



; IP fH T g =



; IP fT H g =



; IP fT T g =



;



and for every set A -, define IP (A) to be the sum of the probabilities of the elements in A . Then

     
IP (�) =, so IP is a probability measure. Note that the sets H on first toss = H H ; H T and
f g f g



H on second toss = H H ; T H have probabilities IP H H ; H T =
f g f g f g



IP H H ; T H =

[and]
f g




[,] [so] [the] [product] [of] [the] [probabilities] [is] [.] [On] [the] [other] [hand,] [the] [intersection] [of] H H ; H T

f g
and H H ; T H contains the single element H H, which has probability [.] [These] [sets] [are] [not]
f g f g




[,] [so] [the] [product] [of] [the] [probabilities] [is]



and H H ; T H contains the single element H H, which has probability [.] [These] [sets] [are] [not]
f g f g

independent.



**1.5.3** **Independence of random variables**


**Definition 1.17** We say that two random variables X and Y are _independent_ if the - -algebras they
generate - (X ) and - (Y ) are independent.



In the probability space of three independent coin tosses, the price S



In the probability space of three independent coin tosses, the price S [of] [the] [stock] [at] [time] is

independent of S [.] [This] [is] [because] S [depends] [on] [only] [the] [first] [two] [coin] [tosses,] [whereas] S [is]



independent of SS [.] [This] [is] [because] S [depends] [on] [only] [the] [first] [two] [coin] [tosses,] [whereas] SS [is]

either u or d, depending on whether the _third_ coin toss is H or T .

Definition 1.17 says that for independent random variables X and Y, every set defined in terms of




[.] [This] [is] [because] S




[depends] [on] [only] [the] [first] [two] [coin] [tosses,] [whereas]



S

S



S

S



X is independent of every set defined in terms of Y . In the case of S




[and]



S

S




[just considered, for ex-]



ample, the sets S
f



n







S = udS0 = H T H ; H T T S = u = H H H ; H T H ; T H H ; T T H
f g f g f g

are indepedent sets. n 
Suppose X and Y are independent random variables. We defined earlier the measure induced by X
on IR to be



= udS



0



= H T H ; H T T and
g f g



S

S



= u



L



=� IP fX Ag; A - IR:



X



(A)



Similarly, the measure induced by Y is



L







= IP fY B g; B - IR:



Y



(B )



Now the pair (X ; Y ) takes values in the plane IR



Now the pair (X ; Y ) takes values in the plane IR, and we can define the measure induced by the

pair



L



X ;Y



(C ) = IP f(X ; Y ) C g; C - IR



:



The set C in this last equation is a subset of the plane IR



The set C in this last equation is a subset of the plane IR . In particular, C could be a “rectangle”,

i.e, a set of the form A B, where A IR and B IR . In this case,

      -       -       


f(X ; Y ) A - B g = fX Ag \ fY B g;


CHAPTER 1.Introduction to Probability Theory 43


and X and Y are independent if and only if







X ;Y

L



(A - B ) = IP



= IP X A IP Y B (5.2)
f g f g







fX Ag \ fY B g



= L



(A)L



X



Y



(B ):



In other words, for independent random variables X and Y, the _joint distribution_ represented by the
measure X ;Y [factors] [into] [the] [product] [of] [the] _[marginal distributions]_ [ represented] [by] [the] [measures]
L



X [and]
L



Y [.]



X ;Y [factors] [into] [the] [product] [of] [the] _[marginal distributions]_ [ represented] [by] [the] [measures]



L



A _joint density_ for (X ; Y ) is a nonnegative function f



X ;Y



(x; y ) such that


(x; y ) dx dy :



X ;Y

L



(A - B ) =



Z



A



B

Z



fX ;Y



Not every pair of random variables (X ; Y ) has a joint density, but if a pair does, then the random
variables X and Y have _marginal densities_ defined by



Z�



fX ;Y



Z�



fX ;Y



(x; - ) d� ; fY (y )



(� ; y ) d� :



fX



(x) =



These have the properties



X (A) =

L


Y (B ) =

L



Z

Z



B



fX



A



fY



(x) dx; A - IR;

(y ) dy ; B - IR:



Suppose X and Y have a joint density. Then X and Y are independent variables if and only if
the joint density is the product of the marginal densities. This follows from the fact that (5.2) is
equivalent to independence of X and Y . Take A = ( ; x] and B = ( ; y ], write (5.1) in terms
� �
of densities, and differentiate with respect to both x and y .


**Theorem 5.7** _Suppose_ X _and_ Y _are independent random variables. Let_ g _and_ h _be functions from_

IR _to_ IR _._ _Then_ g (X ) _and_ h(Y ) _are also independent random variables._


PROOF: Let us denote W = g (X ) and Z = h(Y ) . We must consider sets in - (W ) and - (Z ) . But
a typical set in - (W ) is of the form


f! ; W (! ) Ag = f! : g (X (! )) Ag;

which is defined in terms of the random variable X . Therefore, this set is in - (X ) . (In general,
we have that every set in - (W ) is also in - (X ), which means that X contains at least as much
information as W . In fact, X can contain strictly more information than W, which means that - (X )
will contain all the sets in - (W ) and others besides; this is the case, for example, if W = X .)

In the same way that we just argued that every set in - (W ) is also in - (X ), we can show that
every set in - (Z ) is also in - (Y ) . Since every set in - (X ) is independent of every set in - (Y ), we
conclude that every set in - (W ) is independent of every set in - (Z ) .

                                       

44



**Definition 1.18** Let X



**Definition 1.18** Let X ; X ; : : : be a sequence of random variables. We say that these random

variables are _independent_ if for every sequence of sets A - (X ); A - (X ); : : : and for every



; X



variables are _independent_ if for every sequence of sets A - (X ); A - (X ); : : : and for every

positive integer n,




- (X



); A




- (X



IP (A



\ A



An ) = IP (A
\ - - 


)IP (A



) IP (An

  -  -  


):



**1.5.4** **Correlation and independence**


**Theorem 5.8** _If two random variables_ X _and_ Y _are independent, and if_ g _and_ h _are functions from_

IR _to_ IR _, then_

IE [g (X )h(Y )] = IE g (X )              - IE h(Y );

_provided all the expectations are defined._



PROOF: Let g (x) = lIA (x) and h(y ) = lIB (y ) be indicator functions. Then the equation we are

trying to prove becomes



PROOF: Let g (x) = lI



A



(x) and h(y ) = lI



B











= IP fX AgIP fY B g;



IP



fX Ag \ fY B g



which is true because X and Y are independent. Now use the standard machine to get the result for
general functions g and h .

                                       


The _variance_ of a random variable X is defined to be



Var (X )



=� IE [X - IE X ]



:



The covariance of two random variables X and Y is defined to be



Cov (X ; Y )



=� IE







h



(X - IE X )(Y - IE Y )



= IE [X Y ] - IE X - IE Y :



i



According to Theorem 5.8, for independent random variables, the covariance is zero. If X and Y
both have positive variances, we define their _correlation coefficient_



�(X ; Y )



=� Cov (X ; Y )







p Var (X ) Var (Y )



:



For independent random variables, the correlation coefficient is zero.



Unfortunately, two random variables can have zero correlation and still not be independent. Consider the following example.



**Example 1.16** Let X be a standard normal random variable, let Z be independent of X and have
the distribution IP Z = = IP Z = = 0 . Define Y = X Z . We show that Y is also a
f g f        - g
standard normal random variable, X and Y are uncorrelated, but X and Y are not independent.



, but in fact,



The last claim is easy to see. If X and Y were independent, so would be X



and Y



almost surely.



X



= Y


CHAPTER 1.Introduction to Probability Theory 45


We next check that Y is standard normal. For y IR, we have



IP Y y = IP Y y and Z = + IP Y y and Z =
f  - g f  - g f  -  - g

= IP X y and Z = + IP X y and Z =
f         - g f�         -         - g

= IP fX    - y gIP fZ = g + IP f�X    - y gIP fZ =    - g



=



IP fX - y g +



IP f�X - y g:



Since X is standard normal, IP X y = IP X y, and we have IP Y y = IP X y,
f             - g f             -             - g f             - g f             - g
which shows that Y is also standard normal.

Being standard normal, both X and Y have expected value zero. Therefore,



Cov (X ; Y ) = IE [X Y ] = IE [X



Z ] = IE X




- IE Z = - 0 = 0:



does the measure
L



Where in IR



X ;Y [put its mass, i.e., what is the distribution of] (X ; Y ) ?



We conclude this section with the observation that for independent random variables, the variance
of their sum is the sum of their variances. Indeed, if X and Y are independent and Z = X + Y,
then



Var (Z )



=� IE


= IE


= IE



(Z - IE Z )



h


h



(X - IE X )



i



X + Y - IE X - IE Y )



i



+ (X - IE X )(Y - IE Y ) + (Y - IE Y )



i



= Var (X ) + IE [X IE X ]IE [Y IE Y ] + Var (Y )

      -       


= Var (X ) + Var (Y ):



This argument extends to any finite number of random variables. If we are given independent
random variables X ; X ; : : : ; Xn [, then]



; X



; : : : ; X



n [, then]



) + Var (X



) + + Var (X

   -    -    


n



): (5.3)



Var (X



+ X



+ + Xn ) = Var (X

  -   -   


**1.5.5** **Independence and conditional expectation.**


We now return to property (k) for conditional expectations, presented in the lecture dated October
19, 1995. The property as stated there is taken from Williams’s book, page 88; we shall need only
the second assertion of the property:


**(k)** If a random variable X is independent of a - -algebra, then
H

IE [X jH] = IE X :


The point of this statement is that if X is independent of, then the best estimate of X based on
H
the information in is IE X, the same as the best estimate of X based on no information.
H


46


To show this equality, we observe first that IE X is -measurable, since it is not random. We must
H
also check the partial averaging property



Z



IE X dIP =



Z



A



A



X dIP for every A :
H



If X is an indicator of some set B, which by assumption must be independent of, then the partial
H
averaging equation we must check is



Z



IP (B ) dIP =



Z



dIP :



A



A



lIB



The left-hand side of this equation is IP (A)IP (B ), and the right hand side is



Z



Z



lIA



lIB



dIP =



dIP = IP (A \ B ):











lIA\B



The partial averaging equation holds because A and B are independent. The partial averaging
equation for general X independent of follows by the standard machine.
H



**1.5.6** **Law of Large Numbers**


There are two fundamental theorems about sequences of independent random variables. Here is the
first one.



**Theorem 5.9** **(Law of Large Numbers)** _Let_ X



**Theorem 5.9** **(Law of Large Numbers)** _Let_ X ; X ; : : : _be a sequence of independent, identically_

_distributed random variables, each with expected value_ - _and variance_ - _._ _Define the sequence of_



; X



_distributed random variables, each with expected value_ - _and variance_ - _._ _Define the sequence of_

_averages_



+ - - - + X

n



+ - - - + X



n



+ X



; n = ; ; : : : :



=�



X



Yn







_Then_ Y



n _[converges to]_ - _almost surely as_ n ! _._



We are not going to give the proof of this theorem, but here is an argument which makes it plausible.
We will use this argument later when developing stochastic calculus. The argument proceeds in two
steps. We first check that IE Yn = - for every n . We next check that Var (Yn ) 0 as n 0 . In



steps. We first check that IE Yn = - for every n . We next check that Var (Yn ) 0 as n 0 . In

! !
other words, the random variables Yn [are increasingly tightly distributed around] - as n .



n



n



= - for every n . We next check that Var (Y



n [are increasingly tightly distributed around] - as n .
!



For the first step, we simply compute



n



+ IE X



+ + IE Xn

  -   -   


] =



n



= �:



IE Yn



=




[IE X




[� + - + - - - + �]

| n times {z }



n times



For the second step, we first recall from (5.3) that the variance of the sum of independent random
variables is the sum of their variances. Therefore,



=




Xk

n



n


k =

X





n



Var (Y



n



n







Var
k =

X



k =

X



=





n



) =



:



As n, we have Var (Y
!



n



) 0 .
!


CHAPTER 1.Introduction to Probability Theory 47


**1.5.7** **Central Limit Theorem**



The Law of Large Numbers is a bit boring because the limit is nonrandom. This is because the
denominator in the definition of Yn [is so large that the variance of] Yn [converges to zero. If we want]



denominator in the definition of Yn [is so large that the variance of] Yn [converges to zero. If we want]

to prevent this, we should divide by pn rather than n . In particular, if we again have a sequence of



n [is so large that the variance of] Y



p



to prevent this, we should divide by n rather than n . In particular, if we again have a sequence of

independent, identically distributed random variables, each with expected value - and variance -,



independent, identically distributed random variables, each with expected value - and variance -,

but now we set




- �) + (X




- �) + - - - + (X



p



n



;


:




- �)



(X



n



Zn



=�



then each Z



n [has expected value zero and]







X



Var (Z



n



n








- 


k



Var

k =

X



k =

X



p



n



n


k =

X





n



= 


) =



=



As n, the distributions of all the random variables Zn [have the same degree] [of tightness, as]
!

measured by their variance, around their expected value 0 . The Central Limit Theorem asserts that
as n, the distribution of Zn [approaches that of a normal random variable with mean (expected]
!



As n, the distributions of all the random variables Z
!



as n, the distribution of Zn [approaches that of a normal random variable with mean (expected]
!

value) zero and variance - . In other words, for every set A IR,



. In other words, for every set A IR,

         


dx:



x

 


A

Z



e�



lim

n!



IP Zn
f



Ag =







p 


p


48


### **Chapter 2**

# **Conditional Expectation**

Please see Hull’s book (Section 9.6.)


**2.1** **A Binomial Model for Stock Price Dynamics**


Stock prices are assumed to follow this simple binomial model: The initial stock price during the
period under study is denoted S0 [.] [At each time step, the stock price either goes up by a factor of] u

or down by a factor of d . It will be useful to visualize tossing a coin at each time step, and say that



the stock price moves up by a factor of u if the coin comes out heads ( H ), and

  
down by a factor of d if it comes out tails ( T ).

  
Note that we are not specifying the probability of heads here.

Consider a sequence of 3 tosses of the coin (See Fig. 2.1) The collection of all possible outcomes
(i.e. sequences of tosses of length 3) is


    - = fH H H ; H H T ; H T H ; H T T ; T H H ; T H H; T H T ; T T H ; T T T g:

A typical sequence of - will be denoted !, and ! k [will denote the] k th element in the sequence ! .

We write Sk (! ) to denote the stock price at “time” k (i.e. after k tosses) under the outcome ! . Note



A typical sequence of - will be denoted !, and !



We write Sk (! ) to denote the stock price at “time” k (i.e. after k tosses) under the outcome ! . Note

that Sk (! ) depends only on ! ; ! ; : : : ; ! k [.] [Thus in the 3-coin-toss example we write for instance,]



k



(! ) depends only on !



; : : : ; !



k [.] [Thus in the 3-coin-toss example we write for instance,]



k



; !



= S



(!



= S



(!



);



S



(! )



; !



; !



)



= S



(!



= S



(!



S



(! )



; !



; !



)



; !



):



Each S



k [is a] _[random variable]_ [ defined on] [the set] - . More precisely, let = (�) . Then is a
F P F




- -algebra and (�; ) is a measurable space. Each S
F



k [is an] -measurable function - IR, that is,
F !



k [is in fact]



S



k� is a function where is the Borel - -algebra on IR. We will see later that S
B !F B







49


50



_3_

_S3 (HHH) = u_ _S0_


_2_
_S3_ _(HHT) = u_ _d_ _S0_



ω = Η

_3_



ω = Τ

_3_



ω = Η

_2_



ω = Τ

_3_



_2_

_S3_ _(HTH) = u_ _d_ _S0_

_2_

_S3_ _(THH) = u_ _d_ _S0_



ω = Τ

_2_



_S_ _(HH) = u_ _[2]_
_2_ _S0_


_S2_ _(HT) = ud S0_

_S2_ _(TH) = ud S0_



ω = Η

_3_



_S0_



_S (H) = uS1_ _0_


ω = Η
_1_


ω = Τ

_1_


_S (T) = dS_
_1_ _0_



_2_

_(HTT) = d_ _u_ _S0_

_2_

_(THT) = d_ _u_ _S0_



ω = Η

_2_



_S3_



_2_

_u_ _S0_



ω = Τ



ω = Η



_S3_


_S3_



_(TTH) = d_



_2_ _3_



_2_
_S_ _(TT) = d_
_2_ _S0_



ω = Τ

_3_



_3_
_S3_ _(TTT) = d_ _S0_



Figure 2.1: _A three coin period binomial model._


measurable under a sub- - -algebra of . Recall that the Borel - -algebra is the - -algebra generated
F B
by the open intervals of IR. In this course we will always deal with subsets of IR that belong to .
B

For any random variable X defined on a sample space - and any y IR, we will use the notation:



fX - y g



= f! �; X (!) - y g:



The sets X < y ; X y ; X = y ; etc, are defined similarly. Similarly for any subset B of IR,
f g f    - g f g
we define



fX B g



= f! �; X (!) B g:



**Assumption 2.1** u - d - 0 .


**2.2** **Information**



**Definition 2.1 (Sets determined by the first** k **tosses.)** We say that a set A - is _determined by_

                    _the first_ k _coin tosses_ if, knowing only the outcome of the first k tosses, we can decide whether the
outcome of _all_ tosses is in A . In general we denote the collection of sets determined by the first k
tosses by k [.] [It is easy to check that] k [is a] - -algebra.
F F



k [.] [It is easy to check that]
F



k [is a] - -algebra.



Note that the random variable Sk [is]

F



k [-measurable, for each] k = ; ; : : : ; n .



**Example 2.1** In the 3 coin-toss example, the collection [of sets determined by the first toss consists of:]
F


CHAPTER 2.Conditional Expectation 51



1. A

2. A



T



H



= H H H ; H H T ; H T H ; H T T,
f g



2. AT = fT H H ; T H T ; T T H ; T T T g,

3. -,
4. - .



The collection [of sets determined by the first two tosses consists of:]
F



1. A

2. A

3. A

4. A



T T



H H


H T


T H



= H H H ; H H T,
f g



= H T H ; H T T,
f g

= T H H ; T H T,
f g



4. AT T = fT T H ; T T T g,

5. The complements of the above sets,



6. Any union of the above sets (including the complements),
7. - and - .



**Definition 2.2 (Information carried by a random variable.)** Let X be a random variable - IR .
!
We say that a set A - is _determined by the random variable_ X if, knowing only the value X (! )

     of the random variable, we can decide whether or not ! A . Another way of saying this is that for
every y IR, either X - (y ) A or X - (y ) A = - . The collection of susbets of - determined



every y IR, either X - (y ) - A or X - (y ) \ A = - . The collection of susbets of - determined

by X is a - -algebra, which we call the - -algebra generated by X, and denote by - (X ) .







(y ) A or X

 






If the random variable X takes finitely many different values, then - (X ) is generated by the collection of sets



(X (! ))j! �g;



fX







these sets are called the _atoms_ of the - -algebra - (X ) .



In general, if X is a random variable - IR, then - (X ) is given by
!



(B ); B B g:




- (X ) = fX








[consists of the following sets:]



**Example 2.2 (Sets determined by** S




**[)]** [The]   - -algebra generated by S



1. A



1. AH H = fH H H ; H H T g = f! �; S (! ) = u S0 g,

2. AT T = T T H ; T T T = S = d S0 ;



H H


T T


H T



(! ) = u



S



0



= fH H H ; H H T g = f! �; S




[ A



T H



AT T = fT T H ; T T T g = fS = d S0 g;

3. AH T AT H = S = udS0 ;



= fT T H ; T T T g = fS



= d



S



0



= udS



= fS



0



g;



4. Complements of the above sets,
5. Any union of the above sets,
6. - = S (! ) -,
f g



6. - = S (! ) -,
f g

7. - = S (! ) IR
f



(! ) IR .
g


52


**2.3** **Conditional Expectation**


In order to talk about conditional expectation, we need to introduce a probability measure on our
coin-toss sample space - . Let us define



p (0; ) is the probability of H,





- q



= ( p) is the probability of T,

  


the coin tosses are _independent,_ so that, e.g., IP (H H T ) = p




q ; etc.




- IP (A)



=



P



! A



IP (! ), A - .

   


**Definition 2.3 (Expectation.)**



!X�



X



X (! )IP (! ):



IE X



=



If A - then

  

and


We can think of IE (I



A



X ) as a _partial average_ of X over the set A .



if ! A

0 if ! A



IA (! )



=



(



! A



IE (IA



X ) =



A

Z



X dIP =



! A

X



X (! )IP (! ):



**2.3.1** **An example**



Let us estimate S




[,] [given] S




[.] [Denote] [the] [estimate] [by] IE (S



jS



) . From elementary probability,



IE (S



jS



) is a random variable Y whose value at ! is defined by



Y (! ) = IE (S



jS



= y );



where y = S



(! ) . Properties of IE (S



jS



) :




- IE (S



jS



) should depend on !, i.e., it is a _random variable_ .




[is known, then the value of] IE (S



If the value of S




jS



) should also be known. In particular,




**–** If ! = H H H or ! = H H T, then S



If ! = H H H or ! = H H T, then S (! ) = u S0 [.] [If we know that] S (! ) = u S0 [, then]

even without knowing !, we know that S (! ) = uS0 [.] [We define]



(! ) = u



0 [.] [If we know that] S



S



0 [.] [We define]



(! ) = u



S



(! ) = uS



IE (S



jS



)(H H H ) = IE (S



jS



)(H H T ) = uS0



:




**–** If ! = T T T or ! = T T H, then S



If ! = T T T or ! = T T H, then S (! ) = d S0 [.] [If we know that] S (! ) = d S0 [, then]

even without knowing !, we know that S (! ) = dS0 [.] [We define]



(! ) = d



0 [.] [If we know that] S



S



0 [.] [We define]



(! ) = d



S



(! ) = dS



IE (S



jS



)(T T T ) = IE (S



jS



)(T T H ) = dS0



:


CHAPTER 2.Conditional Expectation 53




**–** If ! A = H T H ; H T T ; T H H; T H T, then S
f g



= dS



(! ) =



udS0 [, then we do not know whether] S = uS0 [or] S = dS0 [.] [We then take a weighted]

average:



0 [, then we do not know whether] S



0 [or] S



(! ) = udS



0 [.] [If we know] S



udS



= uS



q + pq



+ p



q + pq



= pq :



Furthermore,



A

Z



= pq (u + d)S0



uS0



q dS0



dS0



S



IP (A) = p


dIP = p



q uS0 + pq



+ p



+ pq



For ! A we define


Then


In conclusion, we can write


where



IP (A)


)dIP =



dIP



=



:



S



IE (S



jS )(! ) =



R



A



IE (S

A

Z



jS



A

Z



S



(u + d)S0


dIP :



IE (S



jS



)(! ) = g (S



(! ));



0 if x = udS



S



uS



0 if x = u



g (x) =





<





<



(u + d)S



S0



0


0




_[.]_ [ We also write]



dS



0 if x = d



In other words, IE (S



jS



) is random _only through dependence on_ S



>:



>:



IE (S


where g is the function defined above.



jS



= x) = g (x);



The random variable IE (S



jS



) has two fundamental properties:



) -measurable.




- IE (S



jS



) is - (S



For every set A  - (S




),



A

Z



IE (S



S



jS



)dIP =



A

Z



dIP :



**2.3.2** **Definition of Conditional Expectation**


Please see Williams, p.83.

Let (�; ; IP ) be a probability space, and let be a sub- - -algebra of . Let X be a random variable
F G F
on (�; ; IP ) . Then IE (X ) is defined to be any random variable Y that satisfies:
F jG

**(a)** Y is -measurable,
G


54


**(b)** For every set A, we have the “partial averaging property”
G



A

Z



Y dIP =



A

Z



X dIP :



**Existence.** There is always a random variable Y satisfying the above properties (provided that



IE X < ), i.e., conditional expectations always exist.
j j



**Uniqueness.** There can be more than one random variable Y satisfying the above properties, but if



0 almost surely, i.e., IP f! �; Y (! ) = Y



0 (! )g = :



Y



0 is another one, then Y = Y



**Notation 2.1** For random variables X ; Y, it is standard notation to write



IE (X jY )



= IE (X j�(Y )):



Here are some useful ways to think about IE (X ) :
jG

A random experiment is performed, i.e., an element ! of  - is selected. The value of ! is

  partially but not fully revealed to us, and thus we cannot compute the exact value of X (! ) .
Based on what we know about !, we compute an estimate of X (! ) . Because this estimate
depends on the partial information we have about !, it depends on !, i.e., IE [X Y ](! ) is a
j
function of !, although the dependence on ! is often not shown explicitly.



If the  - -algebra contains finitely many sets, there will be a “smallest” set A in containing

- G G



!, which is the intersection of all sets in containing ! . The way ! is partially revealed to us
G
is that we are told it is in A, but not told which element of A it is. We then define IE [X Y ](! )
j
to be the average (with respect to IP ) value of X over this set A . Thus, for all ! in this set A,



IE [X Y ](! ) will be the same.
j



**2.3.3** **Further discussion of Partial Averaging**


The partial averaging property is



A

Z



IE (X jG)dIP =



A

Z



X dIP ; A : (3.1)
G



We can rewrite this as



IE [IA



:IE (X )] = IE [IA
jG



:X ]: (3.2)



Note that I



A [is a] -measurable random variable. In fact the following holds:
G



**Lemma 3.10** _If_ V _is any_ _-measurable random variable, then provided_ IE V :IE (X ) < _,_
G j jG j

IE [V :IE (X )] = IE [V :X ]: (3.3)
jG


CHAPTER 2.Conditional Expectation 55



**Proof:** To see this, first use (3.2) and linearity of expectations to prove (3.3) when V is a _simple_



-measurable random variable, i.e., V is of the form V =
G



-measurable random variable, i.e., V is of the form V = nk = ck IAK [, where each] Ak [is in] and
G G

each ck [is constant.] [Next consider the case that] V is a nonnegative -measurable random variable,

P



P



n



I



K [, where each] A



A



k =



c



k



each ck [is constant.] [Next consider the case that] V is a nonnegative -measurable random variable,

G
but is not necessarily simple. Such a V can be written as the limit of an increasing sequence
of simple random variables Vn [;] [we] [write] [(3.3)] [for] [each] Vn [and] [then] [pass] [to] [the] [limit,] [using] [the]



of simple random variables Vn [;] [we] [write] [(3.3)] [for] [each] Vn [and] [then] [pass] [to] [the] [limit,] [using] [the]

Monotone Convergence Theorem (See Williams), to obtain (3.3) for V . Finally, the general G
measurable random variable V can be written as the difference of two nonnegative random-variables

V = V + - V -, and since (3.3) holds for V + and V - it must hold for V as well. Williams calls

this argument the “standard machine” (p. 56).



n [;] [we] [write] [(3.3)] [for] [each] V



+ and V



V = V




-, and since (3.3) holds for V



+




- V



Based on this lemma, we can replace the second condition in the definition of a conditional expectation (Section 2.3.2) by:


**(b’)** For every -measurable random-variable V, we have
G

IE [V :IE (X )] = IE [V :X ]: (3.4)
jG


**2.3.4** **Properties of Conditional Expectation**


Please see Willams p. 88. Proof sketches of some of the properties are provided below.


**(a)** IE (IE (X )) = IE (X ):
jG
Proof: Just take A in the partial averaging property to be    - .

The conditional expectation of X is thus an unbiased estimator of the random variable X .



**(b)** If X is -measurable, then
G



IE (X jG ) = X :



Proof: The partial averaging property holds trivially when Y is replaced by X . And since X
is -measurable, X satisfies the requirement (a) of a conditional expectation as well.
G

If the information content of is sufficient to determine X, then the best estimate of X based
G
on is X itself.
G



**(c)** (Linearity)



IE (a



IE (X



jG ) + a



IE (X



jG ):



X



+ a



X



jG ) = a



**(d)** (Positivity) If X 0 almost surely, then

      


IE (X jG ) - 0:



Proof: Take A = ! �; IE (X )(! ) < 0 . This set is in since IE (X ) is -measurable.
f jG g G jG G
Partial averaging implies IE (X )dIP = X dIP . The right-hand side is greater than



Partial averaging implies A IE (X )dIP = A X dIP . The right-hand side is greater than

jG

or equal to zero, and the left-hand side is strictly negative, unless IP (A) = 0 . Therefore,

R R



R



A



IE (X jG )dIP =



A



IP (A) = 0 .



R


56


**(h)** (Jensen’s Inequality) If - : R R is convex and IE �(X ) <, then
! j j

IE (�(X )jG )                 - �(IE (X jG)):

Recall the usual Jensen’s Inequality: IE �(X ) �(IE (X )):

              
**(i)** (Tower Property) If is a sub- - -algebra of, then
H G

IE (IE (X jG )jH) = IE (X jH):

is a sub-     - -algebra of means that contains more information than . If we estimate X
H G G H
based on the information in, and then estimate the estimator based on the smaller amount
G
of information in, then we get the same result as if we had estimated X directly based on
H
the information in .
H

**(j)** (Taking out what is known) If Z is -measurable, then
G

IE (Z X jG ) = Z :IE (X jG):

When conditioning on, the -measurable random variable Z acts like a constant.
G G

Proof: Let Z be a -measurable random variable. A random variable Y is IE (Z X ) if and
G jG
only if



(a) Y is -measurable;
G
(b) Y dIP = Z X



R



R



A



A



Y dIP =



Z X dIP ; A .
G



Take Y = Z :IE (X ) . Then Y satisfies (a) (a product of -measurable random variables is
jG G



-measurable). Y also satisfies property (b), as we can check below:
G



A

Z



= IE [IA

= IE [IA



Z IE (X jG )]

Z :X ] ((b’) with V = I



Z IE (X jG )]



Y dIP = IE (IA :Y )



A



Z



=



A

Z



Z X dIP :



**(k)** (Role of Independence) If is independent of - (� (X ); ), then
H G

IE (X j�(G ; H)) = IE (X jG ):

In particular, if X is independent of, then
H

IE (X jH) = IE (X ):

If is independent of X and, then nothing is gained by including the information content
H G
of in the estimation of X .
H


CHAPTER 2.Conditional Expectation 57


**2.3.5** **Examples from the Binomial Model**



Recall that
F



= f�; A



jF



H [and] A



T [.]



) must be constant on A



; - . Notice that IE (S
g



H



; AT



Now since IE (S



jF



) must satisfy the partial averaging property,



jF


jF



)dIP =


)dIP =



AH

Z



AT

Z



dIP ;


dIP :



S


S



We compute


On the other hand,


Therefore,


We can also write


Similarly,



IE (S

AH

Z


IE (S

AT

Z



AH

Z



:



IE (S



jF



)dIP = IP (AH


= pIE (S



):IE (S



jF



jF



)(! )



)(! ); ! AH



AH

Z



S



dIP = p



u



S0 + pq udS0



:



IE (S



jF



)(! ) = pu



S0



+ q udS0 ; ! AH



:



IE (S



jF



)(! ) = pu S0



= (pu + q d)uS0



+ q udS0



= (pu + q d)S



(! ); ! AH



IE (S

Thus in both cases we have


IE (S



jF


jF



)(! ) = (pu + q d)S


)(! ) = (pu + q d)S



(! ); ! AT


(! ); ! �:



:



A similar argument one time step later shows that



IE (S



jF



)(! ) = (pu + q d)S



(! ):



We leave the verification of this equality as an exercise. We can verify the Tower Property, for
instance, from the previous equations we have



IE [IE (S


This final expression is IE (S



jF


jF



)jF


) .



] = IE [(pu + q d)S


= (pu + q d)IE (S



jF

jF



]

) (linearity)



= (pu + q d)



S



:


58


**2.4** **Martingales**


The ingredients are:



A probability space (�; ; IP ) .

- F



A sequence of  - -algebras

- F



; F



; : : : ; F



n [, with the property that]
F



: : : n

- - F







0




- F



. Such a sequence of  - -algebras is called a _filtration_ .
F



0



A sequence of random variables M




0 ; M



; : : : ; M



n [. This is called a] _[ stochastic process]_ [.]



Conditions for a martingale:



k [-measurable.] [If you know the information in]
F



k



k [, then you know the value of]



k



1. Each M



k [is]
F



k [.] [We say that the process] M
f



M



is _adapted_ to the filtration
g fF



.
g



2. For each k, IE (M



) = M



k [. Martingales tend to go neither up nor down.]



k +



k

jF



A _supermartingale_ tends to go _down_, i.e. the second conditionabove is replaced by IE (M



k +

jF



k )

 


k [; a] _[ submartingale]_ [ tends to go] _[ up]_ [, i.e.] IE (M



M



k +



jF



k



) - M



k [.]



**Example 2.3 (Example from the binomial model.)** For k = ; we already showed that



IE (Sk +



jF



) = (pu + q d)Sk



k



:



For k = 0, we set
F



0



= �; -, the “trivial - -algebra”. This - -algebra contains no information, and any
f g



F 0 [-measurable random variable must be constant (nonrandom).] [Therefore, by definition,] IE (S jF 0 ) is that

constant which satisfies the averaging property



jF



0



F



0 [-measurable random variable must be constant (nonrandom).] [Therefore, by definition,] IE (S




 
Z



IE (S



jF



0




 
Z



S



dIP :



)dIP =



The right hand side is IE S


In conclusion,



= (pu + q d)S0 [, and so we have]



IE (S



jF



:



0 ) = (pu + q d)S0



If (pu + q d) = then S

- f

If (pu + q d) then S

- - f

If (pu + q d) then S

- - f



k ; F

k ; F

k ; F



k


k


k



; k = 0; ; ; is a martingale.
g



; k = 0; ; ; is a supermartingale.
g



; k = 0; ; ; is a submartingale.
g


### **Chapter 3**

# **Arbitrage Pricing**

**3.1** **Binomial Pricing**


Return to the binomial pricing model

Please see:


Cox, Ross and Rubinstein, _J. Financial Economics_, **7** (1979), 229–263, and

  
Cox and Rubinstein (1985), **Options Markets**, Prentice-Hall.

  


**Example 3.1 (Pricing a Call Option)** Suppose u = ; d = 0: ; r = % (interest rate), S



**Example 3.1 (Pricing a Call Option)** Suppose u = ; d = 0: ; r = % (interest rate), S0 = 0 . (In this

and all examples, the interest rate quoted is per unit time, and the stock prices S0 ; S ; : : : are indexed by the



0



same time periods). We know thatand all examples, the interest rate quoted is per unit time, and the stock prices S0 ; S ; : : : are indexed by the



0



; S



00 if !

if !



S



(! ) =







= H

= T



Find the value _at time zero_ of a call option to buy one share of stock at time 1 for $50 (i.e. the _strike price_ is
$50).

The value of the call at time 1 is



0 if !

0 if !



V



(! ) = (S



(! ) - 0)+



=







= H

= T



Suppose the option sells for $20 at time 0. Let us construct a portfolio:


1. Sell 3 options for $20 each. Cash outlay is $0:

             
2. Buy 2 shares of stock for $50 each. Cash outlay is $100.

3. Borrow $40. Cash outlay is $0:

         
59


60


This portfolio thus requires no initial investment. For this portfolio, the cash outlay at time 1 is:



! = H ! = T

Pay off option $0 $0
Sell stock $00 $0

      -       Pay off debt $0 $0



!



= H !




- - - - - - - - - 
$0 $0



The _arbitrage pricing theory (APT)_ value of the option at time 0 is V


Assumptions underlying APT:



0



= 0 .



Unlimited short selling of stock.




Unlimited borrowing.




No transaction costs.




Agent is a “small investor”, i.e., his/her trading does not move the market.




**Important Observation:** The APT value of the option does not depend on the probabilities of H
and T .


**3.2** **General one-step APT**



Suppose a derivative security pays off the amount V



Suppose a derivative security pays off the amount V [at] [time] [1,] [where] V [is] [an] [-measurable]

F

random variable. (This measurability condition is important; this is why it does not make sense
to use some stock unrelated to the derivative security in valuing it, at least in the straightforward
method described below).




[at] [time] [1,] [where] V




[is] [an]
F



Sell the security for V




0 [at time 0. (] [V]



0 [is to be determined later).]



0 [is also to be determined later)]



Buy  



0 [shares of stock at time 0. (] [�]



Invest V




Invest V0 �0 S0 [in] [the] [money] [market,] [at] [risk-free] [interest] [rate] r . ( V0 �0 S0 [might] [be]

   -   
negative).



0



0




- 


0



S



0 [in] [the] [money] [market,] [at] [risk-free] [interest] [rate] r . ( V




- 


0



S



Then wealth at time 1 is




+ ( + r )(V0




- 


0



= �0 S



= ( + r )V0


0 [so that]


X



)



S0



+ 


= V



0




- ( + r )S



0



(S



):



We want to choose V




X


0 [and] 


_regardless of whether the stock goes up or down._


CHAPTER 3.Arbitrage Pricing 61


The last condition above can be expressed by _two_ equations (which is fortunate since there are _two_
unknowns):



( + r )V0



+ �0 (S



(H ) ( + r )S0

  


(H ) (2.1)


(T ) (2.2)



( + r )V0



+ 


0



(S



) = V


) = V



(T ) ( + r )S0

  


Note that this is where we use the fact that the derivative security value V



k [is] [a] [function] [of] S



Note that this is where we use the fact that the derivative security value Vk [is] [a] [function] [of] Sk [,]

i.e., when Sk [is] [known for] [a] [given] !, Vk [is] [known (and] [therefore] [non-random) at] [that] ! as well.



i.e., when Sk [is] [known for] [a] [given] !, Vk [is] [known (and] [therefore] [non-random) at] [that] ! as well.

Subtracting the second equation above from the first gives



k [is] [known for] [a] [given] !, V



(T )

(T )



(H ) - V

(H ) - S



(H ) - V



V

S



: (2.3)



Plug the formula (2.3) for 


�0 =


0 [into (2.1):]



( + r )V0



= V


= V



(H ) - 


(H ) 


0



(S



(H ) - ( + r )S



0



)



(H ) - V

(u - d)S



(T )



V



0



(u r )S0

 -  


=


=



+ r - d



u - d




[(u - d)V



(H ) - (V



(H ) - V



(T ))(u - - r )]



u - d



u - - r

u  - d



u - - r



(H ) +



V



(T ):



V



We have already assumed u - d - 0 . We now also assume d + r u (otherwise there would

                -                 be an arbitrage opportunity). Define



p~



=



+ r - d



u - d



u - - r



u - d



; q~ =



:



Then p~ - 0 and q~ - 0 . Since p~ + q~ =, we have 0 < p~ < and q~ = p~ . Thus, p;~ q~ are like

                    probabilities. We will return to this later. Thus the price of the call at time 0 is given by




[p~V

+ r



(H ) + q~V



(T )]: (2.4)



V0



=



**3.3** **Risk-Neutral Probability Measure**



Let - be the set of possible outcomes from n coin tosses. Construct a probability measure



Let - be the set of possible outcomes from n coin tosses. Construct a probability measure IP on 
by the formula



f



=H g



#fj ;!



IP (!



# j ;!

= p~ f



#fj ;!



; : : : ; !



n



)



# j ;!

q~ f



j



=T g



j



; !



IP is called the _risk-neutral probability measure_ . We denote by



IP is called the _risk-neutral probability measure_ . We denote by IE the expectation under IP . Equa
tion 2.4 says



f



f



f



V0



IE the expectation under



IE

f



+ r



=











:



f



V


62


**Theorem 3.11** _Under_


**Proof:**



IP _, the discounted stock price process_ f( + r )

f



IP _, the discounted stock price process_ f( + r )



�k



Sk



n

gk =0 _[is a martingale.]_



; F



k



n

k =0 _[is a martingale.]_



k



IE [( + r )



Sk +



]



f



�(k +)



�(k +)


�(k +)


�(k +)


�(k +)



jF



u - d



= ( + r )



(pu~ + q~d)S



k



Sk




u - d



= ( + r )


= ( + r )


= ( + r )


= ( + r )


**3.3.1** **Portfolio Process**







u( + r - d)



d(u - - r )



u - d



+



u + ur - ud + du - d - dr



Sk



u - d



(u - d)( + r )



Sk



�k



Sk



:



The portfolio process is - = (�



; 


; : : : ; �n� ), where



0



k [is the number of shares of stock held between times] k and k + .




- 


Each  



k [is]
F



k [-measurable. (No insider trading).]




             **3.3.2** **Self-financing Value of a Portfolio Process**



Start with nonrandom initial wealth X0 [, which need not be 0.]


Define recursively




+ ( + r )(Xk



k



Xk +



= �k Sk +



Sk ) (3.1)



+ 


k




- 



- ( + r )S



): (3.2)



(Sk +



k



Then each Xk [is]

- F



= ( + r )Xk


k [-measurable.]



**Theorem 3.12** _Under_



IP _, the discounted self-financingportfolioprocess value_ f( + r )



k



; F



k



g



n



f



�k



X



k k k =0

_is a martingale._



**Proof:** We have



+ �k



( + r )








Sk +



( + r )�(k +) Xk +



= ( + r )�k Xk



�(k +)




- ( + r )�k



Sk







:


CHAPTER 3.Arbitrage Pricing 63


Therefore,



IE [( + r )



Xk +



]


]



�k



f



+




�(k +)



IE [( + r )



=



IE [( + r )



f



Xk



k


k



IE

f



IE [( + r )



�k



Sk +



jF

jF



k ]



�k



X



�(k +)



�k Sk



jF



k



]



jF



r

f



IE [( + r )



�k



k (requirement (b) of conditional exp.)



= ( + r )



jF



+�



r

f

�k



Sk +



k ] (taking out what is known)



k



�(k +)



�k



�( + r )



k (Theorem 3.11)



�k



k (property (b))



S



= ( + r )



X



**3.4** **Simple European Derivative Securities**



**Definition 3.1 ()** A _simpleEuropean derivative security_ with expiration time m is an
F



**Definition 3.1 ()** A _simpleEuropean derivative security_ with expiration time m is an m [-measurable]
F

random variable Vm [.] [(Here,] m is less than or equal to n, the number of periods/coin-tosses in the



random variable Vm [.] [(Here,] m is less than or equal to n, the number of periods/coin-tosses in the

model).



**Definition 3.2 ()** A simple European derivative security V



**Definition 3.2 ()** A simple European derivative security Vm [is said to be] _[ hedgeable]_ [ if] [there exists]

a constant X0 [and] [a] [portfolio] [process] - = (�0 ; : : : ; �m ) such that the self-financing value



a constant X0 [and] [a] [portfolio] [process] - = (�0 ; : : : ; �m ) such that the self-financing value

                     
process X0 ; X ; : : : ; Xm [given by (3.2) satisfies]



0 [and] [a] [portfolio] [process] - = (�



m�



0



; : : : ; 


; : : : ; X



m [given by (3.2) satisfies]



0



; X



(! ) = Vm



m _[.]_



Xm



In this case, for k = 0; ; : : : ; m, we call X



k [the] _[ APT value at time]_ k _of_ V



(! ); ! �:



**Theorem 4.13 (Corollary to Theorem 3.12)** _If a simple European security_ V



**Theorem 4.13 (Corollary to Theorem 3.12)** _If a simple European security_ Vm _[is hedgeable, then]_

_for each_ k = 0; ; : : : ; m _, the APT value at time_ k _of_ Vm _[is]_



m _[is]_



jF



Vm



Vk



= ( + r )k



IE [( + r )



k



]: (4.1)



�m



**Proof:** We first observe that if M
f



; F



**Proof:** We first observe that if Mk ; k ; k = 0; ; : : : ; m is a martingale, i.e., satisfies the
f F g

martingale property



fk



k



k



IE [M



jF



k + k k

for each k = 0; ; : : : ; m, then we also have

       - f



k



] = M



f



k +



IE [M



jF



] = Mk



k



; k = 0; ; : : : ; m : (4.2)

     


f



m



When k = m, the equation (4.2) follows directly from the martingale property. For k = m,

    -    we use the tower property to write



IE [M

f



IE [M



jF



] =


=



= M



IE [



IE

f



IE [M



M

f



jF

jF



]jF



m



m�



m�



]



IE [M



m



m�



m�



]



M

f



m�



m�



:


64


We can continue by induction to obtain (4.2).



If the simple European security V



m [satisfies] X



If the simple European security Vm [is] [hedgeable,] [then] [there] [is] [a] [portfolio] [process] [whose] [self-]

financing value process X0 ; X ; : : : ; Xm [satisfies] Xm = Vm [.] [By definition,] Xk [is the APT value]



financing value process X0 ; X ; : : : ; Xm [satisfies] Xm = Vm [.] [By definition,] Xk [is the APT value]

at time k of Vm [. Theorem 3.12 says that]



; X



m



= V



m [.] [By definition,] X



0



; : : : ; X



m [. Theorem 3.12 says that]



; ( + r )�



X0



X



; : : : ; ( + r )�m Xm



is a martingale, and so for each k,



( + r )�k Xk



IE [( + r )

f



=



�m



Xm



] =



IE [( + r )�m

f



Vm

jF



k



jF



k



]:



Therefore,



jF



�m



Vm



]:



k



Xk



= ( + r )k



IE [( + r )

f



**3.5** **The Binomial Model is Complete**


Can a simple European derivative security always be hedged? It depends on the model. If the answer
is “yes”, the model is said to be _complete._ If the answer is “no”, the model is called _incomplete._


**Theorem 5.14** _The binomial model is complete. In particular, let_ Vm _[be a simple European deriva-]_

_tive security, and set_



�m



Vm



jF



k



](!



; : : : ; !k



Vk



(!



; : : : ; !



) = ( + r )k



k



); (5.1)



IE [( + r )

f



(!

(!



; : : : ; !k



; : : : ; !k



; : : : ; !



�k



(!



Vk + (!

Sk + (!



; : : : ; !k



; : : : ; !



; : : : ; !k



; : : : ; !



; : : : ; !



k ) =



; H ) - V

; H ) - S



k +


k +



; : : : ; !



; T )

; T )



: (5.2)



_Starting with initial wealth_ V



0



m _[.]_



IE [( + r )



V

f



m



] _, the self-financing value of the portfolio process_



�m



V



=



�0



; 


; : : : ; 


m _[is the process]_ V

 


0



; V



; : : : ; V



**Proof:** Let V



0



**Proof:** Let V0 ; : : : ; Vm [and] �0 ; : : : ; �m [be] [defined] [by] [(5.1)] [and] [(5.2).] [Set] X0 = V0 [and]

         -         
define the self-financing value of the portfolio process �0 ; : : : ; �m [by the recursive formula 3.2:]



0



; : : : ; V



0



; : : : ; 


m [and] 
 


m [be] [defined] [by] [(5.1)] [and] [(5.2).] [Set] X

 


= V



0



; : : : ; 


m [by the recursive formula 3.2:]

 


Sk +



�k Sk




):



Xk +



= �k



+ ( + r )(Xk



We need to show that



; k 0; ; : : : ; m : (5.3)
f g



Xk



= Vk



We proceed by induction. For k = 0, (5.3) holds by definition of X0 [.] [Assume that (5.3) holds for]

some value of k, i.e., for each fixed (! ; : : : ; !k ), we have



We proceed by induction. For k = 0, (5.3) holds by definition of X



; : : : ; !



), we have



k



Xk (!



; : : : ; !k



; : : : ; !k



) = Vk (!



; : : : ; !



):


CHAPTER 3.Arbitrage Pricing 65


We need to show that



Xk + (!



; H ) = Vk +



; : : : ; !k



; : : : ; !k



; : : : ; !



; : : : ; !k



(!



; T ) = Vk +



Xk +



; : : : ; !k



(!


(!



; H );


; T ):



We prove the first equality; the second can be shown similarly. Note first that



�(k +)



jF



k



k



IE [( + r )

f



] =


=



= ( + r )



IE [



IE

f



IE [( + r )



(

f



IE [( + r )




[(

f



Vm



]jF



k ]



Vk +



k +



�k



jF



�m


Vm



jF



]



�m



Vk



In other words, ( + r )
f



�k



n

k =0 [is a martingale under]

g



Vk



n

k =0 [is a martingale under]



IP . In particular,



k



jF



k



k



IE [( + r )



f



+ r



Vk +



](!



Vk



(!



; : : : ; !



) =


=



)



f;



; : : : ; !







; : : : ; !k



; H ) + q~Vk +



(!



; T )) :



(p~Vk + (!



; : : : ; !k



; : : : ; !



Since (!



Since (! ; : : : ; !k ) will be fixed for the rest of the proof, we simplify notation by suppressing these

symbols. For example, we write the last equation as



; : : : ; !



k



+ r



(pV~ k +



(T )) :



Vk



=



(H ) + q~Vk +



We compute



Xk +



(H )



= �k

= �k



(Sk +



(H ) + ( + r )(Xk



k



k



Sk



Sk +



)



) + ( + r )V




- 


k



(T )

(T )



(H ) ( + r )Sk

  


(H ) - ( + r )S



k +


k +



=


=



Vk +

Sk +



(H ) - V

(H ) - S



(H ) - V



uS



(Sk +



)



+pV~



(H ) + q~V



(T )



k +



k +



(T )



( + r )Sk




Vk +



k +



(uSk



)



k +



k




- dS



k



+pV~



(H ) + q~V



(T )



k +



+ pV~ k +



(H ) + q~Vk +



u - - r



u - d



= (Vk +


= (Vk +



(H ) Vk +

 


(H ) - V



k +



(T ))







(T )







(T )) q~ + p~V



k +



(H ) + q~V



k +



(T )



= Vk +



(H ):


66


### **Chapter 4**

# **The Markov Property**

**4.1** **Binomial Model Pricing and Hedging**


Recall that Vm [is] [the] [given] [simple] [European] [derivative] [security,] [and] [the] [value] [and] [portfolio pro-]

cesses are given by:



Vm



jF



]; k = 0; ; : : : ; m - :



Vk



= ( + r )k



IE [( + r )



k



k


k



�m



f: :



(!

(!



; : : : ; !k



(!

(!



; : : : ; !

; : : : ; !



; H ) - V

; H ) - S



; : : : ; !



k +


k +



; : : : ; !k



; : : : ; !



�k



(!



k



Vk +

Sk +



; : : : ; !



) =



; T )

; T )



; k = 0; ; : : : ; m - :



**Example 4.1 (Lookback Option)** u = ; d = 0: ; r = 0: ; S



u = ; d = 0: ; r = 0: ; S0 = ; p~ = +u��d = 0: ; q~ =             - p~ = 0: :

Consider a simple European derivative security with expiration 2, with payoff given by (See Fig. 4.1):



= ; p~ =



+r �d



u�d



0



V



= max



0�k 



- )+



(S



:



k



Notice that



V



(H H ) = ; V



(H T ) = = V



(T H ) = 0; V



(T T ) = 0:



The payoff is thus “path dependent”. Working backward in time, we have:



V



(H ) =



+ r



(H H ) + q~V



(H T )] =




[0: - + 0: - ] = :0;




[pV~



V


V0



(T ) =




[0: - 0 + 0: - 0] = 0;



=




[0: - :0 + 0: - 0] = : :



Using these values, we can now compute:


�0



(H ) - V (T )

(H ) - S (T )



(H H ) - V

(H H ) - S

67



=



V

S


V


S



= 0: ;



(H T )

(H T )



= 0: ;







(H ) =


68



_S (HH) = 16_

_2_



_S (H) = 8_

_1_



_S (HT) = 4_

_2_



_S = 4_
_0_



_S (TH) = 4_

_2_



_S (T) = 2_

_1_



_S (TT) = 1_

_2_



Figure 4.1: _Stock price underlying the lookback option._



(T H ) - V

(T H ) - S



(T T )

(T T )



V

S



= 0:







(T ) =



Working forward in time, we can check that



X



(H ) = �0



S



(H ) + ( + r )(X0




- �0



S0



(H ) = :0;



) = : ; V



(H )S



(T ) = �0



S



(T ) + ( + r )(X0




- �0



S0



(T ) = 0;



) = 0:0; V



X



X


(H H ) = 


(H H ) + ( + r )(X



(H ) - 


(H )S



(H )) = :0; V



(H H ) = ;



etc.



**Example 4.2 (European Call)** Let u = ; d =



**Example 4.2 (European Call)** Let u = ; d = ; r = ; S0 = ; p~ = q~ = [, and consider a European call]

with expiration time 2 and payoff function



; r =



; S



0



= ; p~ = q~ =



V



= (S




- )+ :



Note that



V



(H H ) = ; V



(H T ) = V



(T H ) = 0; V



(T T ) = 0;



V


0



(H ) =




[



: +



(T ) =




[




[



:0 +



V



V


=



:0] = :0


:0] = 0


- 0] = : :




- :0 +



Define v



k



k



(x) to be the value of the call at time k when S



= x . Then



v


v (x) =


v0 (x) =



(x) = (x - )+



(x) +


(x) +



v


v



(x=)];


(x=)]:




[


[



v


v


CHAPTER 4.The Markov Property 69


In particular,



v


v



() = ; v



v


=



() = 0; v



() = 0;



v


0



() =




[



: +




[



:0] = :0;


:0] = 0;


- 0] = : :



() =




[



:0 +




- :0 +



Let 


k



= x . Then



(x) be the number of shares in the hedging portfolio at time k when Sk



k +



(x=)

; k = 0; :



�k (x) =



vk +



(x) - v



x - x=



**4.2** **Computational Issues**


For a model with n periods (coin tosses), - has

equations of the form



n elements. For period k, we must solve



k



; : : : ; !k



+ r



; H ) + q~Vk + (!



; : : : ; !k



; : : : ; !



; T )]:



Vk



(!



) =




[pV~ k + (!



; : : : ; !k



For example, a three-month option has 66 trading days. If each day is taken to be one period, then



n = and




- - 0



.



There are three possible ways to deal with this problem:



1. Simulation. We have, for example, that



f



V0



= ( + r )�n



IE V



;



n



and so we could compute V



and so we could compute V0 [by] [simulation.] [More] [specifically,] [we] [could] [simulate] n coin

tosses ! = (! ; : : : ; !n ) under the risk-neutral probability measure. We could store the



tosses ! = (! ; : : : ; !n ) under the risk-neutral probability measure. We could store the

value of Vn (! ) . We could repeat this several times and take the average value of Vn [as] [an]



; : : : ; !



n



value of Vn (! ) . We could repeat this several times and take the average value of Vn [as] [an]

approximation to IE Vn [.]



(! ) . We could repeat this several times and take the average value of V



n



IE V



f



n [.]



2. Approximate a many-period model by a continuous-time model. Then we can use calculus
and partial differential equations. We’ll get to that.

3. Look for Markov structure. Example 4.2 has this. In period 2, the option in Example 4.2 has
three possiblevalues v (); v (); v (), rather than four possiblevalues V (H H ); V (H T );



three possiblevalues v (); v (); v (), rather than four possiblevalues V (H H ); V (H T ); V (T H ); V (T T ) .

If there were 66 periods, then in period 66 there would be 67 possible stock price values (since
the final price depends only on the _number_ of up-ticks of the stock price – i.e., heads – so far)
and hence only 67 possible option values, rather than 0 .



(); v



(); v



(), rather than four possiblevalues V



(H H ); V



(H T ); V



(T H ); V




- - 0



.


70


**4.3** **Markov Processes**


**Technical condition always present:** We consider only functions on IR and subsets of IR which are
Borel-measurable, i.e., we only consider subsets A of IR that are in and functions g : IR IR such
B !
that g - is a function B !B .



**Definition 4.1 ()** Let (�; ; P) be a probability space. Let

n F fF



g



k



nk =0 [be] [a] [filtration under] . Let

F



n



fX



k



g



nk =0 [be a stochastic process on] (�; ; P) . This process is said to be _Markov_ if:

F



n



The stochastic process X

- f



is adapted to the filtration
g fF



, and
g



k



k



_(The Markov Property)._ For each k = 0; ; : : : ; n, the distribution of X

- 


_(The Markov Property)._ For each k = 0; ; : : : ; n, the distribution of Xk + [conditioned]

              
on k [is the same as the distribution of] Xk + [conditioned on] Xk [.]
F



k [is the same as the distribution of] X



k + [conditioned on] X



k [.]



**4.3.1** **Different ways to write the Markov property**



**(a)** (Agreement of distributions). For every A
B



= (IR), we have
B



IP (Xk +



AjF



k ) = IE [IA

= IE [IA



(Xk +

(Xk +



k


k



]


]



= IP [Xk +



)jF

)jX

AjX



]:



k



**(b)** (Agreement of expectations of all functions). For every (Borel-measurable) function h : IR IR
!
for which IE h(Xk + ) <, we have
j j



k +



) <, we have
j



IE [h(Xk +



)jF



] = IE [h(Xk +



]:



k



) Xk
j



**(c)** (Agreement of Laplace transforms.) For every u IR for which IE euXk +



<, we have



































F



X



e




uXk +



IE



e




uXk +











= IE



:



k



k



(If we fix u and define h(x) = eux, then the equations in (b) and (c) are the same. However in

(b) we have a condition which holds for _every_ function h, and in (c) we assume this condition
only for functions h of the form h(x) = eux . A main result in the theory of Laplace transforms



(If we fix u and define h(x) = e



only for functions h of the form h(x) = eux . A main result in the theory of Laplace transforms

is that if the equation holds for every h of this special form, then it holds for every h, i.e., (c)
implies (b).)



**(d)** (Agreement of characteristic functions) For every u IR, we have



k



i



h



eiuXk +



Xk
j



h



= cos x + sin x we don’t need to assume that IE e
j j j - j



eiuXk +



jF



i



= IE



;



IE


. (Since eiux

- j



where i =

.)



p



iux



j <


CHAPTER 4.The Markov Property 71



**Remark 4.1** In every case of the Markov properties where IE [: : : X
j



**Remark 4.1** In every case of the Markov properties where IE [: : : Xk ] appears, we could just as
j

well write g (Xk ) for some function g . For example, form (a) of the Markov property can be restated



k



well write g (Xk ) for some function g . For example, form (a) of the Markov property can be restated

as:



k



For every A, we have
B



IP (Xk +



AjF



) = g (Xk



k



);



where g is a function that depends on the set A .


Conditions (a)-(d) are equivalent. The Markov property as stated in (a)-(d) involves the process at
a “current” time k and one future time k + . Conditions (a)-(d) are also equivalent to conditions
involving the process at time k and multiple future times. We write these apparently stronger but
actually equivalent conditions below.

**Consequences of the Markov property.** Let j be a positive integer.



**(A)** For every Ak +


IP [Xk +



Ak +



jF



IR; : : : ; k +j

- A



k


k



Ak +



; : : : ; Xk +j



]:



; : : : ; X



k +j



Ak +j


]:



Xk
j



IR,



Ak +j



] = IP [Xk +



] = IP [(Xk +



; : : : ; Xk +j



; : : : ; X



**(A’)** For every A IR



j,



IP [(Xk +



; : : : ; X



k +j ) A

jF



; : : : ; X



) A Xk
j



**(B)** For every function h : IR



j



IR for which IE h(Xk +
! j



; : : : ; Xk +j



; : : : ; X



) <, we have
j



IE [h(Xk +



k +j



; : : : ; X



) Xk
j



)jF



k



] = IE [h(Xk +



; : : : ; Xk +j



; : : : ; X



**(C)** For every u = (u



k +



+:::+uk +j



Xk +j



]:


<, we have
j



; : : : ; u



k +j



) IRj for which IE e

j



uk +



Xk +



IE [euk +



Xk +



+:::+uk +j Xk +j



jF



k



+:::+uk +j



Xk +j



Xk ]:
j



] = IE [euk + Xk +



**(D)** For every u = (u



k +



; : : : ; u



k +j



) IRj we have



IE [ei(uk +



Xk +



+:::+uk +j Xk +j



+:::+uk +j



Xk +j



)



jF



k



Xk
j



]:



] = IE [ei(uk +



Xk +



)



Once again, every expression of the form IE (: : : Xk ) can also be written as g (Xk ), where the
j

function g depends on the random variable represented by : : : in this expression.



Once again, every expression of the form IE (: : : X
j



k



) can also be written as g (X



k



**Remark.** All these Markov properties have analogues for vector-valued processes.


72


**Proof** **that** **(b)** = **(A)** . (with j = in (A)) Assume (b). Then (a) also holds (take h = IA [).]
)

Consider



IP [Xk +

= IE [I



k +



k ]



)jF



Ak + ; Xk +



Ak +



A



k +



jF



k



]



(X



A



(Xk +



k +



)I



(Definition of conditional probability)



k +



]jF



k ]



(Xk +



= IE [IE [I



k +



)jF



A



(Xk +



)I



(Tower property)



Ak +



= IE [I



k +



A



k +



k +



]


]



] k
jF


] k
jF



A



(Xk +



):IE [I



(Xk +



(Taking out what is known)



)jF



A



k +



= IE [I



k +



A



(Xk +



(Xk +



):IE [I



(Markov property, form (a).)



) Xk +
j



= IE [I



k +



k +)

jF



)jF



k



A



(Xk +



):g (X



(Remark 4.1)



= IE [I



k +



k +



)jX



]


]



A



(Xk +



k



):g (X



(Markov property, form (b).)



Now take conditional expectation on both sides of the above equation, conditioned on - (Xk ), and

use the tower property on the left, to obtain



Now take conditional expectation on both sides of the above equation, conditioned on - (X



k



IP [Xk +



Ak +



(Xk +



):g (X



k +) X

j



)jX



k



; X



k +



] = IE [I

Ak +



Ak +



Xk
j



]: (3.1)



Since both


and



IP [Xk +


IP [Xk +



Ak + ; Xk +



Ak + ; Xk +



Ak +



jF



k



Ak +



jX



k



]


]



are equal to the RHS of (3.1)), they are equal to each other, and this is property (A) with j = .



**Example 4.3** It is intuitively clear that the stock price process in the binomial model is a Markov process.
We will formally prove this later. If we want to estimate the distribution of Sk + [based on the information in]



k + [based on the information in]



F



k [, the only relevant piece of information is the value of] S



k [.] [For example,]



IE [S



jF



= ( + r )Sk (3.2)



k



] = (pu~ + q~d)Sk



k +



is a function of Sk [.] [Note however] [that form (b) of the Markov property is] [stronger then (3.2);] [the Markov]

property requires that for _any_ function h,



is a function of S



e



IE [h(S



)jF



]



k



k +



is a function of S



k [.] [Equation (3.2) is the case of] h(x) = x .



e



Consider a model with 66 periods and a simple European derivative security whose payoff at time 66 is



V



=



+ S



+ S



):



(S


CHAPTER 4.The Markov Property 73


The value of this security at time 50 is



V



IE [( + r )



I

e



V0



= ( + r )0



jF



0



]











IE [V



e



= ( + r )



jS0 ];



because the stock price process is Markov. (We are using form (B) of the Markov property here). In other
words, the F0 [-measurable random variable] V0 [can be written as]



0 [-measurable random variable] V



0 [can be written as]



V0



(!



; : : : ; !



0



) = g (S0



(!



; : : : ; !



0



))



for some function g, which we can determine with a bit of work.


**4.4** **Showing that a process is Markov**


**Definition 4.2 (Independence)** Let (�; ; P) be a probability space, and let and be sub- - F G H
algebras of . We say that and are _independent_ if for every A and B, we have
F G H G H

IP (A \ B ) = IP (A)IP (B ):

We say that a random variable X is independent of a - -algebra if - (X ), the - -algebra generated
G
by X, is independent of .
G

**Example 4.4** Consider the two-period binomial model. Recall that [is the] - -algebra of sets determined
F

by the first toss, i.e., [contains the four sets]
F



**Example 4.4** Consider the two-period binomial model. Recall that
F




[contains the four sets]



AH



= fH H ; H T g; AT



= fT H ; T T g; �; �:



Let be the - -algebra of sets determined by the second toss, i.e., contains the four sets
H H

fH H ; T H g; fH T ; T T g; �; �:



Then
F



Then [and] are independent. For example, if we take A = H H ; H T from [and] B = H H ; T H
F H f g F f g

from, then IP (A B ) = IP (H H ) = p and
H \




[and] are independent. For example, if we take A = H H ; H T from
H f g F



and



IP (A)IP (B ) = (p



+ pq )(p



+ pq ) = p



(p + q )



= p



:



Note that
F




[and] S




[are not independent (unless] p = or p = 0 ). For example, one of the sets in  - (S



) is



), then



f! ; S



(! ) = u



S0



= H H . If we take A = H H ; H T from
g f g f g F



, but




[and] B = H H from  - (S
f g



IP (A \ B ) = IP (H H ) = p



IP (A)IP (B ) = (p



+ pq )p



= p



(p + q ) = p



:



The following lemma will be very useful in showing that a process is Markov:


**Lemma 4.15 (Independence** **Lemma)** _Let_ X _and_ Y _be_ _random variables on a_ _probability space_

(�; F ; P) _. Let_ G _be a sub-_ - _-algebra of_ F _._ _Assume_


74




- X _is independent of_ G _;_

- Y _is_ G _-measurable._



_Let_ f (x; y ) _be a function of two variables, and define_



g (y )



= IE f (X ; y ):



_Then_



IE [f (X ; Y )jG ] = g (Y ):

**Remark.** In this lemma and the following discussion, capital letters denote random variables and
lower case letters denote nonrandom variables.


**Example 4.5 (Showing the stock price process is Markov)** Consider an n -period binomial model. Fix a



+

and
k G



time k and define X



= F



k [.] [Then] X = u if !



k +



k +



=



S



k +



S



= H and X = d if !



= T . Since X



depends only on the (k + ) st toss, X is independent of . Define Y
G



= Sk [, so that] Y is -measurable. Let h

G



be any function and set f (x; y )



= h(xy ) . Then



g (y )



= IE f (X ; y ) = IE h(X y ) = ph(uy ) + q h(dy ):



The Independence Lemma asserts that



:Sk



IE [h(Sk +



Sk +



Sk







jF



k



)jF



] = IE [h



]



k







= IE [f (X ; Y )jG ]



= g (Y )



= ph(uSk



) + q h(dSk ):



This shows the stock price is Markov. Indeed, if we condition both sides of the above equation on - (S



This shows the stock price is Markov. Indeed, if we condition both sides of the above equation on - (Sk ) and

use the tower property on the left and the fact that the right hand side is - (Sk ) -measurable, we obtain



) -measurable, we obtain



k



k



IE [h(Sk +



):



k



] = ph(uSk ) + q h(dSk



Thus IE [h(S



k +



)jF



)jX



)jS



k



] and IE [h(S



k +



k



] are equal and form (b) of the Markov property is proved.



Not only have we shown that the stock price process is Markov, but we have also obtained a formula for



k [.] [This is a special case of Remark 4.1.]



IE [h(Sk +



)jF



] as a function of S



k



**4.5** **Application to Exotic Options**


Consider an n -period binomial model. Define the _running maximum_ of the stock price to be



Sj



Mk



= max



�j �k



:



Consider a simple European derivative security with payoff at time n of v



; Mn



) .



n



(Sn



**Examples:**


CHAPTER 4.The Markov Property 75



vn


vn




(Sn


(Sn



; Mn


; Mn




- K )



+
(Lookback option);



) = (Mn


) = IMn



�B



K )+ (Knock-in Barrier option).




(Sn



**Lemma 5.16** _The two-dimensional process_ (S
f



**Lemma 5.16** _The two-dimensional process_ f(Sk ; Mk )gnk =0 _[is Markov. (Here we are working under]_

_the risk-neutral measure IP, although that does not matter)._



; M



k



k



)g



n



**Proof:** Fix k . We have



Mk + = Mk



Sk +
_



;



+

k [, so]



where indicates the maximum of two quantities. Let Z
_



S



=



k +



S



IP (Z = u) = p;~



IP (Z = d) = q~;



f



and Z is independent of
F


Define



k [. Let] h(x; y ) be a function of two variables. We have



fh



h(Sk +



) = h(Sk +



; Mk +



; Mk



k + )



= h(Z Sk ; Mk



_ (Z S



_ S



k



)):



g (x; y )



=



IE h(Z x; y _ (Z x))



ph~

f



= ph~ (ux; y _ (ux)) + q~h(dx; y _ (dx)):



The Independence Lemma implies



IE [h(S



] = g (Sk



) = ph~ (uSk



; Mk



)jF



(uSk
_



)) + q~h(dSk



; Mk



);



k +



k



; Mk



f



k +



; M



the second equality being a consequence of the fact that Mk dSk = Mk [.] [Since] [the] [RHS] [is] [a]

^

function of (Sk ; Mk ), we have proved the Markov property (form (b)) for this two-dimensional



the second equality being a consequence of the fact that M



k



^ dS



k



= M



function of (Sk ; Mk ), we have proved the Markov property (form (b)) for this two-dimensional

process.



k



k



; M



Continuing with the exotic option of the previous Lemma... Let Vk [denote the value of the derivative]

security at time k . Since ( + r )�k Vk [is a martingale under] IP, we have



Continuing with the exotic option of the previous Lemma... Let V



IP, we have



f



�k



k [is a martingale under]



V



+ r



]; k = 0; ; : : : ; n - :



Vk


At the final time, we have



=



k

jF



IE [V

f



IE [V



k +



; Mn



):



Vn

Stepping back one step, we can compute



= vn



(Sn



+ r


+ r



IE [v




[pv~



(Sn



; Mn



)jF



]



Vn�



=


=



f



n�



n



n



(uSn�



; uSn�



(dSn�



; Mn�



)] :



_ Mn�



) + q~vn


76


This leads us to define


so that



=



+ r



(dx; y )]



vn�



(x; y )




[pv~ n



(ux; ux y ) + q~vn
_



; Mn�



= vn�



(Sn�



):



The general algorithm is



Vn�



vk (x; y ) =



+ r



(dx; y )



;








pv~ k +



(ux; ux y ) + q~vk +
_



and the value of the option at time k is vk (Sk ; Mk ) . Since this is a simple European option, the

hedging portfolio is given by the usual formula, which in this case is



and the value of the option at time k is v



k



(S



k



; M



k



) _ M



k



) - v



(uSk



; (uSk



)



k + (dSk



; Mk



�k



=



vk +



(u - d)S



k


### **Chapter 5**

# **Stopping Times and American Options**

**5.1** **American Pricing**



Let us first review the **European** **pricing** **formula** **in** **a** **Markov** **model** . Consider the Binomial
model with n periods. Let Vn = g (Sn ) be the payoff of a derivative security. Define by backward



model with n periods. Let Vn = g (Sn ) be the payoff of a derivative security. Define by backward

recursion:



n



= g (S



n



vn (x) = g (x)



vk (x) =



+ r




[p~vk +



(dx)]:



(ux) + q~vk +



Then v



k



) is the value of the option at time k, and the hedging portfolio is given by



(Sk



k +



)

; k = 0; ; ; : : : ; n  - :



(uSk



) - v



(dSk



�k



=



vk +



(u - d)S



k



Now consider an American option. Again a function g is specified. In any period k, the holder
of the derivative security can “exercise” and receive payment g (Sk ) . Thus, the hedging portfolio



of the derivative security can “exercise” and receive payment g (Sk ) . Thus, the hedging portfolio

should create a wealth process which satisfies



k



Xk



g (Sk ); k ; almost surely.




This is because the value of the derivative security at time k is at least g (S



This is because the value of the derivative security at time k is at least g (Sk ), and the wealth process

value at that time must equal the value of the derivative security.



k



**American algorithm.**



(x) = g (x)


(x) = max



+ r



(pv~ k +



vn



(dx)); g (x)

    


vk







(ux) + q~vk +



Then v



k



) is the value of the option at time k .


77



(Sk


78



_v (16) = 0_
_2_



_S (HH) = 16_

_2_



_S (HH) = 16_



_S (H) = 8_

_1_



_S (HT) = 42_



_S = 4_
_0_



_S (TH) = 4_

_2_



_S (T) = 2_

_1_



_S (TT) = 1_

_2_



_v (4) = 1_

_2_


_v (1) = 4_

_2_



Figure 5.1: _Stock price and final value of an American put option with strike price 5._



**Example 5.1** See Fig. 5.1. S



**Example 5.1** See Fig. 5.1. S0 = ; u = ; d = ; r = ; p~ = q~ = ; n = . Set v (x) = g (x) = ( x)+ .

                           
Then



(x) = g (x) = ( - x)



; r =



; p~ = q~ =



; n = . Set v



0



= ; u = ; d =









v


v


v0



: 

: 


; ( - )+



; ( - )+



() = max


= max


= 0:0


() = max













 
; 0







:0 +



: +



= maxf ; g



= :00











:(:0)

   


; ( - )+



() = max







:(0:) +



= maxf : ; g



= :



Let us now construct the hedging portfolio for this option. Begin with initial wealth X



0



= : . Compute



0 [as follows:]







0:0 = v


= S



(S



(H )�0



(H ))



+ ( + r )(X0




- �0



S0



)



= �0


= �0



+



(: - �0 )



= �0:



:00 = v


= S



(S



(T )�0



+ :0 =) �0

(T ))



)



+ ( + r )(X0




- �0 S0



= �0



+



(: - �0 )



= ��0 + :0 =) �0



= �0:


CHAPTER 5.Stopping Times and American Options 79



Using �0



= 0: results in

 


X



(H ) = v



(S



(T ) = v



(S (T )) = :00



Now let us compute 



[(Recall that] S



(H )) = 0:0; X


(T ) = ):



= v ()


= S (T H )�



(T ) + ( + r )(X



(T ) - 


(T ))


(T ))



( - �



(T ))



= �



(T ) +



= :�



(T ) + : =) 


(T ) = - :



= v


= S


= 


()


(T T )�


(T ) +



( - �



(T ) + ( + r )(X



(T ) - 


(T )S


(T )S



(T ))



= - :�



(T ) + : =) 


(T ) = �0:



We get different answers for 


(T ) ! If we had X



(T ) =, the value of the _European_ put, we would have



= :�


= - :�



(T ) + : =) 
(T ) + : =) 


(T ) = - ;

(T ) = - ;



**5.2** **Value of Portfolio Hedging an American Option**



Sk +



k



Xk +



= �k



+ ( + r )(Xk



)




- 


k Sk



= ( + r )Xk



+ �k



(Sk +




- C




- ( + r )S



k



) ( + r )Ck

 


Here, Ck [is the amount “consumed” at time] k .



The discounted value of the portfolio is a _supermartingale_ .




The value satisfies X




k




- g (S



k



); k = 0; ; : : : ; n .



The value process is the smallest process with these properties.




When do you consume? If



�(k +)



)jF



] < ( + r )�k



);



vk +



(Sk +



(Sk



k



vk



or, equivalently,



IE (( + r )

f



IE (

f



) k
jF



] < vk



(Sk



)



+ r vk +



(Sk +


80



and the holder of the American option does not exercise, then the seller of the option can consume
to close the gap. By doing this, he can ensure that Xk = vk (Sk ) for all k, where vk [is] [the] [value]



to close the gap. By doing this, he can ensure that Xk = vk (Sk ) for all k, where vk [is] [the] [value]

defined by the American algorithm in Section 5.1.



k



= v



k



(S



k



) for all k, where v



In the previous example, v



(S


IE [

f



(T )) = ; v



(S



(T H )) = and v



(S



(T T )) = . Therefore,


:

i



)jF


(S



](T ) =

h

=

      
= ;


(T )) = ;



v

+ r



(S


v



: +

 


so there is a gap of size 1. If the owner of the option does not exercise it at time one in the state



!



= T, then the seller can consume 1 at time 1. Thereafter, he uses the usual hedging portfolio



k +



(dSk



)



) - v



�k



=



vk +



(uSk



(u - d)S



k



In the example, we have v (S (T )) = g (S (T )) . It is optimal for the owner of the American option

to exercise whenever its value vk (Sk ) agrees with its intrinsic value g (Sk ) .



In the example, we have v



(S



(T )) = g (S



k



(S



k



) agrees with its intrinsic value g (S



k



) .



**Definition 5.1 (Stopping Time)** Let (�; ; P) be a probability space and let
F fF



**Definition 5.1 (Stopping Time)** Let (�; ; P) be a probability space and let k nk =0 [be] [a filtra-]
F fF g

tion. A _stopping time_ is a random variable - : - 0; ; ; : : : ; n with the property that:
!f g [ fg



k



g



n



f! �; - (! ) = k g F



k ; k = 0; ; : : : ; n; :



**Example 5.2** Consider the binomial model with n = ; S




[.] [Let]



; r =




[, so] p~ = q~ =



0



= ; u = ; d =



v0 ; v



; v




[be the value functions defined for the American put with strike price 5.] [Define]



g:




- (! ) = minfk ; vk



(Sk



) = ( - Sk



)+



The stopping time - corresponds to “stopping the first time the value of the option agrees with its intrinsic
value”. It is an optimal exercise time. We note that



if ! AT

if ! AH




                  - (! ) =


We verify that - is indeed a stopping time:







f! ; - (!) = 0g = - F



f! ; - (!) = g = A

f! ; - (!) = g = A



T


H



0


F

F



**Example 5.3 (A random time which is not a stopping time)** In the same binomial model as in the previous
example, define



�(! ) = minfk ; Sk (! ) = m



(! )g;


CHAPTER 5.Stopping Times and American Options 81



random variable is given bywhere m = min0�j - Sj [.] [In other words,] - stops when the stock price reaches its minimum value. This



where m



0�j 


= min



S



0 if ! A



H



;



�(! ) =


We verify that - is _not_ a stopping time:



<

:



if ! = T H ;



if ! = T T



f! ; �(! ) = 0g = A



H



F



0



f! ; �(! ) = g = fT H g F

f! ; �(! ) = g = fT T g F



**5.3** **Information up to a Stopping Time**


**Definition 5.2** Let - be a stopping time. We say that a set A - is _determined by time_ - provided

                that



A \ f! ; - (! ) = k g F



; k :



k



The collection of sets determined by - is a - -algebra, which we denote by
F




- [.]



**Example 5.4** In the binomial model considered earlier, let




- = minfk ; vk



(Sk



) = ( - Sk



)+ g;



i.e.,



if ! AT

if ! AH




- (! ) =







The set H T is determined by time -, but the set T H is not. Indeed,
f g f g



fH T g \ f! ; - (! ) = 0g = - F

fH T g \ f! ; - (! ) = g = - F



0



fH T g \ f! ; - (! ) = g = fH T g F



but


The atoms of
F



fH T g; fH H g; AT



:




- [are]



fT H g \ f! ; - (! ) = g = fT H g F



= fT H ; T T g:



**Notation 5.1 (Value of Stochastic Process at a Stopping Time)** If (�; ; P) is a probabilityspace,

n n F



k nk =0 [is a filtration under], Xk nk =0 [is a stochastic process adapted to this filtration, and]  - is

fF g F f g

a stopping time with respect to the same filtration, then X� [is an] - [-measurable] [random variable]



k



fF




- [is an]
F



k



g



nk =0 [is a filtration under], X

F f



n



g



n



a stopping time with respect to the same filtration, then X� [is an] - [-measurable] [random variable]

F

whose value at ! is given by



X� (! )



= X� (! ) (! ):


82



**Theorem 3.17 (Optional Sampling)** _Suppose that_ Y
f



; F



**Theorem 3.17 (Optional Sampling)** _Suppose that_ fYk ; F k gk =0 _[(or]_ fYk ; F k gnk =0 _[) is a submartin-]_

_gale. Let_ - _and_ - _be_ bounded _stopping times, i.e., there is a nonrandom number_ n _such that_



; F



k



k



g



k =0 _[(or]_ fY



k



k



g



n




- - n; - - n; _almost surely._



_If_ - - - _almost surely, then_



Y�



):




- IE (Y







jF







_Taking expectations, we obtain_ IE Y








- IE Y




 - _[, and in particular,]_ Y



; F



k



g




                    -                     - 0 0                     - k k k =0

_is a supermartingale, then_ - - _implies_ Y� IE (Y� - ) _._

        -        - jF



= IE Y



0




- IE Y




- _[. If]_ fY



k



_is a supermartingale, then_ - - _implies_ Y� IE (Y� - ) _._

        -        - jF

_If_ fYk ; F k gk =0 _[is a martingale, then]_ - - - _implies_ Y� = I



0



jF







= IE (Y




 



 







 



- IE (Y



jF



) _._



k



; F



k



g



k =0 _[is a martingale, then]_ - - - _implies_ Y




 


**Example 5.5** In the example 5.4 considered earlier, we define - (! ) = for all ! - . Under the risk-neutral
probability measure, the discounted stock price process ( )�k Sk [is a martingale. We compute]



�k



k [is a martingale. We compute]



)



S








 



 



 



 


IE







S



F



#



:



"




 


The atoms of
F




- [are] H H ; H T ; and A
f g f g



T [.] [Therefore,]



e



"









 







IE

e



IE












 



 



 


F



F



(H H );


(H T );



(H H ) =




 


S


S











"













S


S



#

#



(H T ) =







and for ! A



T [,]



IE

e



(! ) =


=




 
 











 



 



 
 


F



(T H ) +


 - 0:







S



(T T )



IE

e



"�







S








- : +



S





#



= :0



In every case we have gotten (see Fig. 5.2)







(! ) =

  



 



 - (! )




IE

e



"

 


S




 



 



 


F



#



S� (! )



(! ):




 

CHAPTER 5.Stopping Times and American Options 83



_S (HH) = 10.24_

_2_



_S (HH) = 10.24_



_(16/25)_


_(16/25)_


_(16/25)_



_S (HT) = 2.56_

_2_



_S (HT) = 2.56_



_S = 4_
_0_



_(4/5)_ _S (H) = 6.40_

_1_


_(4/5)_ _S (T) = 1.60_
_1_



_S (TH) = 2.56_

_2_



_S (TH) = 2.56_



_(16/25)_



_S (TT) = 0.64_

_2_



_S (TT) = 0.64_



Figure 5.2: _Illustrating the optional sampling theorem._


84


### **Chapter 6**

# **Properties of American Derivative** **Securities**

**6.1** **The properties**



**Definition 6.1** An _American_ _derivative_ _security_ is a sequence of non-negative random variables

Gk nk =0 [such that each] Gk [is] k [-measurable.] [The owner of an American derivative security can]
f g F

exercise at any time k, and if he does, he receives the payment Gk [.]



k [.]



k [is]
F



fG



k



g



nk =0 [such that each] G



n



**(a)** The value V



k [of the security at time] k is



IE [( + r )



f



G�



( + r )k



Vk



= max

   


jF



k



];



��



where the maximum is over all stopping times - satisfying - k almost surely.

                


**(b)** The discounted value process ( + r )
f



�k Vk



g



n

k =0 [is the smallest supermartingale which satisfies]



n



Vk


**(c)** Any stopping time - which satisfies



Gk ; k ; almost surely.




IE [( + r )��

f



G� ]



V0



=



is an optimal exercise time. In particular



= Gk

g







= min k ; Vk
f



is an optimal exercise time.

**(d)** The hedging portfolio is given by



; : : : ; !k



; : : : ; !k



; k = 0; ; : : : ; n - :



(!

(!



; : : : ; !k



; : : : ; !



(!

(!



; : : : ; !k



�k



(!



Vk +

Sk +



; : : : ; !



; : : : ; !



k



) =



; H ) - V

; H ) - S



k +


k +



; T )

; T )



85


86



**(e)** Suppose for some k and !, we have V



Suppose for some k and !, we have Vk (! ) = Gk (! ) . Then the owner of the derivative security

should exercise it. If he does not, then the seller of the security can immediately consume



(! ) = G



k



k



IE [V

f



IE [V



jF



](! )



Vk



(! ) 


+ r



k



k +



and still maintain the hedge.


**6.2** **Proofs of the Properties**



Let G
f



Let Gk nk =0 [be a sequence of non-negative random variables such that each] Gk [is] k [-measurable.]
f g F

Define Tk [to be the set of all stopping times] - satisfying k - n almost surely. Define also



k [is]
F



k



g



k [to be the set of all stopping times] - satisfying k - n almost surely. Define also

             -              


nk =0 [be a sequence of non-negative random variables such that each] G



n



max




- T



jF



��



G�



] :



Vk



= ( + r )k



k



k



IE [( + r )

f



**Lemma 2.18** Vk




- Gk _[for every]_ k _._



**Proof:** Take - Tk [to be the constant] k .



**Lemma 2.19** _The process_ ( + r )
f



�k



n

gk =0 _[is a supermartingale.]_



Vk



n

k =0 _[is a supermartingale.]_




- attain the maximum in the definition of V



**Proof:** Let 


k + [, i.e.,]



Vk +



=



IE

f



( + r )

h



��



G�



jF



]jF




 






i



:


k +



k +



Because - - is also in T



( + r )�(k +)


k [, we have]



��







IE [( + r )�(k +)

f



jF

G



k ] =


=



IE

IfE



IE [( + r )



�f



h



G�



Vk +



jF



IE [( + r )



jF

]

jF



i







k



k



��


G�







f




 

k





max

- - Tk



IE [( + r )



]



Vk



��




- T



�k



k



fr )



= ( + r )



:



**Lemma 2.20** _If_ Yk
f



n

gk =0 _[is another process satisfying]_



Yk



Gk ; k = 0; ; : : : ; n; _a.s.,_




_and_ f( + r )



�k



n

gk =0 _[is a supermartingale, then]_



Yk



n

k =0 _[is a supermartingale, then]_



Yk



Vk ; k = 0; ; : : : ; n; _a.s._



CHAPTER 6.Properties of American Derivative Securities 87



**Proof:** The optional sampling theorem for the supermartingale ( + r )
f



�k



n

k =0 [implies]

g



Yk



n

k =0 [implies]



; - Tk



] - ( + r )�k



Y�



k



:



Yk



Therefore,


**Lemma 2.21** _Define_



IE [( + r )��

f



jF



IE [( + r )



jF



k



G�



]



Vk



= ( + r )k



max

- Tk


max

- Tk



k



��



k




- ( + r )k



IfE



jF



IE [( + r )



Y�



]



k



��



k



�k



fr




- ( + r )



( + r )



Yk



= Y



k



:







+ r



IE [V



jF



IE [( + r )

f



Ck



= Vk



k



k +



�k



n



f



= ( + r )k



( + r )



Vk



]

 


]





�(k +)



Vk +



jF



k



:



_Since_ f( + r )



�k



gnk =0 _[is a supermartingale,]_ C



Vk



nk =0 _[is a supermartingale,]_ C



k _[must be non-negative almost surely. Define]_



(!

(!



; : : : ; !k



:


= Vk [for] [some]



; : : : ; !k



; : : : ; !



�k



(!



k



Vk + (!

Sk + (!



; : : : ; !k



; : : : ; !



; : : : ; !k



; : : : ; !



; : : : ; !



) =



; H ) - V

; H ) - S



k +


k +



; : : : ; !



; T )

; T )



_Set_ X


_Then_



0



= V0 _[and define recursively]_



= �k



�k




Sk



Xk +



Sk +



+ ( + r )(Xk



Ck




):



Xk = Vk



k :



**Proof:** We proceed by induction on k . The induction hypothesis is that X



k 0; ; : : : ; n, i.e., for each fixed (!
f   - g



k



; : : : ; !k



; : : : ; !



) we have



(!



; : : : ; !k



; : : : ; !k



; : : : ; !



) = Vk



(!



; : : : ; !



):



We need to show that



Xk


(!



; : : : ; !k



Xk +



; : : : ; !k



; : : : ; !



; H ) = Vk +


; T ) = Vk +



; : : : ; !k



; : : : ; !



Xk + (!



; : : : ; !k



(!


(!



; : : : ; !



; H );


; T ):



We prove the first equality; the proof of the second is similar. Note first that



Vk (!


=


=



; : : : ; !k ) Ck

   


+ r


+ r



(pV~



(!



; : : : ; !k



; : : : ; !



)



IE [V



](!



)



k



; : : : ; !k



; : : : ; !



f



k +



k +



jF


(!



; : : : ; !k



; H ) + q~Vk +



(!



; T )) :



; : : : ; !k



; : : : ; !


88



Since (!



Since (! ; : : : ; !k ) will be fixed for the rest of the proof, we will suppress these symbols. For

example, the last equation can be written simply as



; : : : ; !



k



Vk Ck

 


=



+ r



(T )) :



(pV~ k +



(H ) + q~Vk +



We compute



(H ) = �k



�k




Sk



)



Xk +



Sk +



(H ) + ( + r )(Xk




- C



(T )

(T )



Ck




(H ) ( + r )Sk

  


k +


k +



=


=



Vk +

Sk +



(H ) - V

(H ) - S



(H ) Vk

  
(u - d)S



(Sk +



)



+( + r )(V



)



k



k



(T )



( + r )Sk




Vk +



k +



(uSk



)



k



+pV~



(T )



k +



(H ) + q~V



k +



= (Vk +



k +



(T ))q~ + pV~ k +



(T )



(H ) + q~Vk +



= Vk +



(H ):



(H ) - V



**6.3** **Compound European Derivative Securities**


In order to derive the optimal stopping time for an American derivative security, it will be useful to
study compound European derivative securities, which are also interesting in their own right.

A compound European derivative security consists of n + different simple European derivative
securities (with the same underlying stock) expiring at times 0; ; : : : ; n ; the security that expires
at time j has payoff Cj [.] [Thus a compound European derivative security is specified by the process]



j [.] [Thus a compound European derivative security is specified by the process]



j [-measurable,] [i.e.,] [the] [process] C
f



fC

fF



g

g



j


k



nj =0 [,] [where] [each] C



n



n

k =0 [.]



g



nj =0 [is] [adapted] [to] [the] [filtration]



n



j [is]
F



j



n



**Hedging** **a short** **position (one payment)** . Here is how we can hedge a short position in the j ’th
European derivative security. The value of European derivative security j at time k is given by



Vk(j )



f



= ( + r )k



IE [( + r )



Cj



k ]; k = 0; : : : ; j;



jF



�j



and the hedging portfolio for that security is given by



; : : : ; !k


; : : : ; !k



(!


(!



; : : : ; !k



(!


(!



; : : : ; !k



; : : : ; !



(j )

k +

(j )

k +



; : : : ; !k



; : : : ; !



(kj ) (!







k



V


S



(j )

k +

(j )

k +



; : : : ; !



) =



; H ) - V

; H ) - S



; : : : ; !



; T )


; T )



; k = 0; : : : ; j - :



Thus, starting with wealth V0(j ), and using the portfolio (�0(j ) ; : : : ; �j(j�) ), we can ensure that at

time j we have wealth Cj [.]



Thus, starting with wealth V



0



(j )



(j )



; : : : ; 


(j )



j 


j [.]



0(j ), and using the portfolio (�



**Hedging** **a** **short position (all payments).** Superpose the hedges for the individual payments. In
other words, start with wealth V0 = nj V (j ) . At each time k 0; ; : : : ; n, first make the



other words, start with wealth V0 = nj =0 V0(j ) . At each time k 0; ; : : : ; n, first make the

f                           - g
payment Ck [and then use the portfolio]

P



(j )



P



n



j =0



V



0



=



k [and then use the portfolio]



+ �k (k +)



+ : : : + �k (n)



�k



= �k (k +)


CHAPTER 6.Properties of American Derivative Securities 89


corresponding to all future payments. At the final time n, after making the final payment Cn [,] [we]

will have exactly zero wealth.



Suppose you own a compound European derivative security C
f



nj =0 [.] [Compute]

g



j



nj =0 [.] [Compute]



n



=



(j )



j =0

X



0



IE

f



V0



=



V



n


j =0

X



( + r )�j Cj



and the hedging portfolio is �k kn=0� [. You can borrow] V0 [and consume it immediately. This leaves]
f g

you with wealth X0 = V0 [.] [In each] [period] k, _receive_ the payment Ck [and then use the portfolio]



and the hedging portfolio is f



g



k



kn=0� [. You can borrow] V



n�



k [and then use the portfolio]



0



= �V



0 [.] [In each] [period] k, _receive_ the payment C



�k [. At the final time] n, after receiving the last payment Cn [, your wealth will reach zero, i.e., you]


will no longer have a debt.



k [. At the final time] n, after receiving the last payment C



��



**6.4** **Optimal Exercise of American Derivative Security**



In this section we derive the optimal exercise time for the owner of an American derivative security.
Let Gk nk =0 [be] [an] [American] [derivative] [security.] [Let] - be the stopping time the owner plans to
f g



Let Gk nk =0 [be] [an] [American] [derivative] [security.] [Let] - be the stopping time the owner plans to
f g

use. (We assume that each Gk [is non-negative, so we may assume without loss of generality that the]



k



g



n



use. (We assume that each Gk [is non-negative, so we may assume without loss of generality that the]

owner stops at expiration – time n - if not before). Using the stopping time -, in period j the owner
will receive the payment



Gj



Cj



= I



f� =j g



:



In other words, once he chooses a stopping time, the owner has effectively converted the American
derivative security into a compound European derivative security, whose value is



V0(� )



=


=


=



IE

f



n



IE [( + r )



f

IE

f



��



( + r )�j



Cj



If� =j g Gj



IE



j =0

X

n


j =0

X



( + r )�j



G�



]:



The owner of the American derivative security can borrow this amount of money immediately, if
he chooses, and invest in the market so as to exaclty pay off his debt as the payments Cj nj =0 [are]
f g



j



g



n

j =0 [are]



n



received. Thus, his optimal behavior is to use a stopping time - which maximizes V



0(� ) .



(� )



**Lemma 4.22** V



0(� ) _is maximized by the stopping time_




- 


= min k ; Vk = Gk
f



g:



**Proof:** Recall the definition



��



G�



] = max



(� )



V0



= max




- T




 - T



V



0



IE [( + r )

f



0



0


90



0



Let 


0 be a stoppingtime which maximizes V



0(� ), i.e., V



: Because ( + r )
f



k



(� )



IE

f



h



( + r )



��



0 G







g



n



0



0 0                       - 0 k k =0

is a supermartingale, we have from the optional sampling theorem and the inequality Vk Gk [, the]



=



0



i



�k



V



is a supermartingale, we have from the optional sampling theorem and the inequality Vk Gk [, the]

                       
following:



k




- G



i



IE

IfE



V�



V0





=



( + r )



0

jF



0



0



V�



0


0



( + r )







IE

IfE



IE


V0

f



:



0


0


0



G�



0

i



0

i



( + r )



�� 0


�� 0


�� 0



= V



h

h

h



0



Therefore,


and



IE

f



IE

f



i



0

i



( + r )

h



��



0 G�



V0



=



( + r )

h



��



V�



0



0



0



;



=



0



= G�



V� 0



; a.s.



0



0 attains the maximum in the formula



We have just shown that if 

then


But we have defined



] ; (4.1)



��



G�



V0



= max




 - T



IE [( + r )

f



0



0 = G�



V�



0 ; a.s.




 






= min fk ; V



k



= Gk



g;



and so we must have 







- - 0



n almost surely. The optional sampling theorem implies




( + r )��



G�



V� 
�� 0


�� 0



G�



0












 


= ( + r )��







:




            
=


Taking expectations on both sides, we obtain



h

h



V�



0



IE

IfE



( + r )



0

jF



0

jF



i








 


0


0



IE

f



( + r )



i




 



 


G�



f



G�



h



( + r )



��



i



0

i




 






0



h



( + r )



��



0







IE



= V0 :



It follows that - - also attains the maximum in (4.1), and is therefore an optimal exercise time for

the American derivative security.



It follows that 


IE

f


### **Chapter 7**

# **Jensen’s Inequality**

**7.1** **Jensen’s Inequality for Conditional Expectations**


**Lemma 1.23** _If_ ' : IR IR _is convex and_ IE '(X ) < _, then_
! j j

IE ['(X )jG]                - '(IE [X jG]):



_For instance, if_ G = f�; �g; '(x) = x _:_



IE X




- (IE X )



:



**Proof:** Since ' is convex we can express it as follows (See Fig. 7.1):



'(x) = max

h '

     
h is linear



h(x):



Now let h(x) = ax + b lie below ' . Then,



IE ['(X )jG] - IE [aX + bjG ]



= aIE [X jG ] + b



= h(IE [X jG ])



This implies



IE ['(X ) ] max
jG     - h '



h '

 



  
h is linear



h(IE [X jG ])



= '(IE [X jG]):


91


92



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-93-0.png)



Figure 7.1: _Expressing a convex function as a max over linear functions._



**Theorem 1.24** _If_ Y
f

**Proof:**



k



gnk =0 _[is a martingale and]_ - _is convex then_ f'(Y



k



)gnk =0 _[is a submartingale.]_



IE ['(Yk + )

jF



= '(Y



])



k



] - '(IE [Y



k +



k



jF



k



):



**7.2** **Optimal Exercise of an American Call**


This follows from Jensen’s inequality.



**Corollary 2.25** _Given_ _a_ _convex_ _function_ g : [0; ) IR _where_ g (0) = 0 _._ _For_ _instance,_ g (x) =
!



(x - K )+ _is the payoff function for an American call._ _Assume that_ r - 0 _._ _Consider the American_

_derivative security with payoff_ g (Sk ) _in period_ k _._ _The value of this security is the same as the value_



(x - K )



k



_derivative security with payoff_ g (Sk ) _in period_ k _._ _The value of this security is the same as the value_

_of the simple European derivative security with final payoff_ g (Sn ) _, i.e.,_



) _, i.e.,_



n



g (Sn



IE [( + r )



)] = max

    


IE [( + r )



f



g (S�



)] ;



f



�n



��



_where the LHS is the European value and the RHS is the American value._ _In particular_ - = n _is an_
_optimal exercise time._



**Proof:** Because g is convex, for all - [0; ] we have (see Fig. 7.2):



g (�x) = g (�x + ( - �):0)




- �g (x) + ( - �):g (0)



= �g (x):


CHAPTER 7.Jensen’s Inequality 93



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-94-0.png)







_(_ λ _x, g(_ λ _x))_


Figure 7.2: _Proof of Cor. 2.25_



Therefore,


and



g

 


g (Sk +



Sk +







+ r



+ r







)


+ r





 


IE

f

IE

f



i



) k
jF







IE

f



h( + r )�(k +)



g (Sk +



)jF




- ( + r )�k

- ( + r )�k

= ( + r )�k



IE

fk )



g



g (Sk +



k



= ( + r )�k








k











k

jF



k

jF



Sk +


Sk +







��



g



+ r


+ r



g (S



);



So ( + r )�k g (Sk ) nk =0 [is a submartingale.] [Let] - be a stopping time satisfying 0 - n . The
f g  -  
optional sampling theorem implies



So ( + r )
f



�k



g (S



k



)g



n



( + r )��

Taking expectations, we obtain



)jF



g (S� )

  


IE [( + r )

f



�n



g (Sn







] :



�n



IE [( + r )��

f



) jF



g (S�



)] 
=



IE

IfE



IE [( + r )



f



]

 


IE [( + r )



�n g (Sn



g (Sn



)] :







f



Therefore, the value of the American derivative security is



)] 


max

  


IE [( + r )



f



g (S�



IE [( + r )



f



g (Sn



)] ;



��



�n



and this last expression is the value of the European derivative security. Of course, the LHS cannot
be strictly less than the RHS above, since stopping at time n is always allowed, and we conclude
that



max

  


IE [( + r )��

f



g (S� )] =



IE [( + r )

f



�n



g (Sn



)] :


94



_S (HH) = 16_

_2_



_S (H) = 8_

_1_



_S (HT) = 4_

_2_



_S = 4_
_0_



_S (TH) = 4_

_2_



_S (T) = 2_

_1_



_S (TT) = 1_

_2_



Figure 7.3: _A three period binomial model._


**7.3** **Stopped Martingales**



Let Yk nk =0 [be] [a] [stochastic] [process] [and] [let] - be a stopping time. We denote by Yk - nk =0 [the]
f g f ^ g

_stopped process_



Let Y
f



k ^�



k



g



nk =0 [be] [a] [stochastic] [process] [and] [let] - be a stopping time. We denote by Y

f



n



g



n



Yk ^� (! ) (! ); k = 0; ; : : : ; n:



**Example 7.1 (Stopped Process)** Figure 7.3 shows our familiar 3-period binomial example.



Define



if !

if !




- (! ) =







= T ;



! = H :

Then



S ^� (! )



(! ) =



>>



>>

<





<










>:



>:



S

S

S

S



(H H ) = if ! = H H ;

(H T ) = if ! = H T ;

(T ) = if ! = T H ;

(T ) = if ! = T T :



**Theorem 3.26** _A stopped martingale (or submartingale, or supermartingale) is still a_ _martingale_
_(or submartingale, or supermartingale respectively)._



**Proof:** Let Y
f



**Proof:** Let Yk nk =0 [be a martingale, and] - be a stopping time. Choose some k 0; ; : : : ; n .

The set - f k g is in k [, so the set] - k + = - k c is also in k [.] [We compute] f g
f    - g F f    - g f    - g F



k



g



n



k [.] [We compute]



= I


= I


= Y



f� �k g

f� �k g



c is also in
F



k [, so the set] - k + = - k
f      - g f      - g



i



= IE



h



If� �k g



IE



h



Y



(k +)^�



Y� + If� �k +g



Yk +



jF



i



k

jF



IE [Yk +

Yk



jF



k


]



+ If� �k +g

+ If� �k +g



Y�


Y�



k



k ^�



:


CHAPTER 7.Jensen’s Inequality 95


96


### **Chapter 8**

# **Random Walks**

**8.1** **First Passage Time**



Toss a coin infinitely many times. Then the sample space - is the set of all infinite sequences

! = (! ; ! ; : : : ) of H and T . Assume the tosses are independent, and on each toss, the probability

of H is [, as is the probability of] T . Define



! = (!




[, as is the probability of] T . Define



; !



if !

if !




if !



= H ;

= T ;



(



j


j



Yj



(! ) =



M0


Mk



= 0;


k



=



j =

X



Yj



; k = ; ; : : :



j =



The process Mk k =0 [is a] _[ symmetric random walk]_ [ (see Fig. 8.1) Its analogue in continuous time is]
f g

_Brownian motion_ .



The process M
f



k



g



Define



= g:



k



If Mk [never] [gets to 1 (e.g.,] ! = (T T T T : : : ) ), then - = . The random variable - is called the

_first passage time to 1_ . It is the first time the number of heads exceeds by one the number of tails.



If M




- = min fk - 0; M



**8.2** - **is almost surely finite**


It is shown in a Homework Problem that Mk
f



k =0 [and] N

g f



k =0 [where]

g



+ e��



!)




 - Mk

(




- k log



k


e�



Nk



= exp



= e� Mk







e�



+ e��


97



�k


98





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-99-0.png)



Figure 8.1: _The random walk process_ Mk



θ

|Col1|e + e θ −θ|
|---|---|
||_e + e_<br>_2_<br>θ<br>−θ<br>1|
|||


|Col1|2<br>θ −θ<br>e + e<br>1|
|---|---|
|||



Figure 8.2: _Illustrating two functions of_      



###### θ



are martingales. (Take M



are martingales. (Take Mk = Sk [in part (i) of the Homework Problem and take] - = - in part

        -         
(v).) Since N0 = and a stopped martingale is a martingale, we have



k



= �S



0



= and a stopped martingale is a martingale, we have







#



= IE Nk ^�



= IE



e� Mk ^�

"



e�



+ e��



�k ^�



(2.1)



for every fixed - IR (See Fig. 8.2 for an illustration of the various functions involved). We want
to let k in (2.1), but we have to worry a bit that for some sequences ! -, - (! ) = .
!

We consider fixed - - 0, so



e�



+ e��







< :



As k,
!


Furthermore, M



k ^�







�0



e�





 








 if    - < ;



+e



(



0 if - =



e







+ e��



�k ^�



!



, because we stop this martingale when it reaches 1, so




0 - e� Mk ^�




- e�


CHAPTER 8.Random Walks 99



and


In addition,







0 - e� Mk ^�



+ e��



e�



�k ^�




- e�



:



0 if - = :







e







k ^�

+ e��

  


+ e��



e�



IE




 




if    - < ;



+e







lim

k !



e� Mk ^�



=



(



e�



Recall Equation (2.1):



e� Mk ^�

"



e�




=

#



�k ^�



Letting k, and using the Bounded Convergence Theorem, we obtain
!







e�




e�




IE



+ e��



= : (2.2)


- e;



��



If� <g


 


For all - (0; ], we have



0 - e�







e�



+ e��







If� <g



so we can let - 0 in (2.2), using the Bounded Convergence Theorem again, to conclude
#



IE



i



= ;



i.e.,



I

f� < g

h



IP f� < g = :



We know there are paths of the symmetric random walk M
f



We know there are paths of the symmetric random walk Mk k =0 [which never] [reach] [level 1.] [We]
f g

have just shown that these paths _collectively_ have no probability. (In our infinite sample space -,
each path _individually_ has zero probability). We therefore do not need the indicator I [in]



g



k



each path _individually_ has zero probability). We therefore do not need the indicator I

                                        - < [in]
f g
(2.2), and we rewrite that equation as



= e��



: (2.3)



��







IE



e�



+ e��



��







**8.3** **The moment generating function for** 

Let - (0; ) be given. We want to find - - 0 so that




- =







e� + e��



:




Solution:



�e�


�(e��



+ �e��




- = 0



)




- e��



+ - = 0


100


We want - - 0, so we must have e��



e��



=



p


  



- 


:



< . Now 0 < - <, so



0 < ( - �)



< ( - �) < - 


;




- - <




- 


;



pp



p












p




- 


< �;


<


 
- :




- 


We take the negative square root:


Recall Equation (2.3):


IE



e��



=



p


  


��



+ e��


=



��











= e��



; - - 0:



With - (0; ) and - - 0 related by



e�


��



p


 

+ e




- 


;


;



e




- =



e�




��







this becomes



IE ��



=



p


  



- 


; 0 < - < : (3.1)



We have computed the _moment generating function_ for the first passage time to 1.


**8.4** **Expectation of** 


Recall that


so



IE ��



=



p


  



- 


; 0 < - < ;



d IE ��

d�



= IE (� �� 


)

p


 


!







=


=



d

d�












- 


p




- 

:




 - 
- 


p


CHAPTER 8.Random Walks 101



Using the Monotone Convergence Theorem, we can let - in the equation
"




 - 
- 


;



p



IE (� �� - ) =











p



to obtain


Thus in summary:



IE - = :



= g;







= min k ; Mk
f



IP f� < g = ;


IE                    - = :


**8.5** **The Strong Markov Property**



The random walk process Mk
f



k =0 [is a Markov process, i.e.,]

g



IE [ random variable depending only on M



k +



]



; Mk +



; : : : j F



k



= IE [ same random variable M
j



] :



k



In discrete time, this Markov property implies the _Strong Markov property_ :



IE [ random variable depending only on M



; M� + ;




- +



; : : : j F







]



= IE [ same random variable M�
j


for any almost surely finite stopping time - .


**8.6** **General First Passage Times**


Define



] :



= mg; m = ; ; : : :



�m



= min k 0; Mk
f   


Then - - [is the number of periods between the first arrival at level 1 and the first arrival at level]

  
2. The distribution of - - [is the same as the distribution of] - [(see Fig. 8.3), i.e.,]



Then 



- 



- 



[is the same as the distribution of]  



[(see Fig. 8.3), i.e.,]



p


 



- 


IE ��



��



=







; - (0; ):


102


For - (0; ),



IE [�



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-103-0.png)











Figure 8.3: _General first passage times._




 










jF







��



��



IE [�



IE [��




 


] = IE

= ��


= ��


= ��







��

��



jF



jF



]�



]�



(taking out what is known)



IE [��



��



jM







]



(strong Markov property)



��



]



(M�


= ��







= ; not random )



p




 




!




- 


:



Take expectations of both sides to get


IE ��


In general,



!



= IE ��



:

p


 


p


 


!


; - (0; ):




- 



- 


=







p


 



- 


!m



IE ��m



=







**8.7** **Example:** **Perpetual American Put**



Consider the binomial model, with u = ; d = ; r = [, and payoff function] ( Sk )+ . The risk

                     
neutral probabilities are p~ = [,] q~ = [, and thus]



Consider the binomial model, with u = ; d =




[, and payoff function] ( S

       


k



)



q~ =

[,]




[, and thus]



; r =



Sk



= S0



uMk



;


CHAPTER 8.Random Walks 103



where M



k [is] [a] [symmetric] [random] [walk] [under] [the] [risk-neutral measure,] [denoted] [by]



IP . Suppose

f



S0



= . Here are some possible exercise rules:



**Rule 0:** Stop immediately. �0



(�0



= 0; V



)



= .



**Rule 1:** Stop as soon as stock price falls to 2, i.e., at time



�� = min fk ; Mk



= - g:


= - g:



**Rule 2:** Stop as soon as stock price falls to 1, i.e., at time



�� = min fk ; Mk



Because the random walk is symmetric under



Because the random walk is symmetric under IP, - m [has] [the] [same] [distribution under] IP as the

                  
stopping time �m [in the previous section.] [This observation leads to the following computations of]



IP, 


f



f



m [has] [the] [same] [distribution under]




stopping time �m [in the previous section.] [This observation leads to the following computations of]

f f

value. **Value of Rule 1:**



IE



IE



=



(

f



)+







IE







( + r )���





 


( - S



+



h







= ( - )



)


)







(



i



q




- (



= :







:


= ( - )



IE

f



**Value of Rule 2:**



V (�� )


V (�



=


)




i



+



(

h




 
) 


= :(


= :



)



This suggests that the optimal rule is Rule 1, i.e., stop (exercise the put) as soon as the stock price
falls to 2, and the value of the put is [if] S0 = .

Suppose instead we start with S0 =, and stop the first time the price falls to 2. This requires 2

down steps, so the value of this rule with this initial stock price is



S

[if]



0



= .



Suppose instead we start with S



0



i



= :(



( - )+



h




 
) 


)



=



(



:



In general, if S0 = j for some j, and we stop when the stock price falls to 2, then j down

         -          steps will be required and the value of the option is



In general, if S



0



IE

f



=



)��(j �)

i



( - )+



)j - :



IE



(

h



= :(



We define



IE

f



v (j )



= :(



)j - ; j = ; ; ; : : :


104



If S0 = j for some j, then the initial price is at or below 2. In this case, we exercise

       immediately, and the value of the put is



If S



0



=



v (j



j



)



= 


j ; j = ; 0; - ; - ; : : :



**Proposed exercise rule:** Exercise the put whenever the stock price is at or below 2. The value of
this rule is given by v (j ) as we just defined it. Since the put is perpetual, the initial time is no



this rule is given by v (j ) as we just defined it. Since the put is perpetual, the initial time is no

different from any other time. This leads us to make the following:



j



**Conjecture 1** _The value of the perpetual put at time_ k _is_ v (S



) _._



k



How do we recognize the value of an American derivative security when we see it?

There are three parts to the proof of the conjecture. We must show:



**(a)** v (S



k ;



k



) ( Sk )+

 - 


**(b)**



n







(



)k v (Sk



)



k =0 [is a supermartingale,]



**(c)** v (S
f



k )

g



k =0 [is the smallest process with properties (a) and (b).]



**Note:** To simplify matters, we shall only consider initial stock prices of the form S0 = j, so Sk [is]

always of the form j, with a possibly different j .



**Note:** To simplify matters, we shall only consider initial stock prices of the form S



j, so S



=



j, with a possibly different j .



0



**Proof:** **(a).** Just check that


This is straightforward.



v (j



)



j


)



+ for j ;

   


= :(



)j - - ( 


)



v (j



)



= 

) 
=




- ( 


+ for j :

   


j



IE


:

f



j



**Proof:** **(b).** We must show that


v (Sk



h



k



k



Sk


):



i

v (



i



v (Sk + )

jF



:



v (S



):



) +



By assumption, Sk



=



j for some j . We must show that



:


v (



j 


v (j + ) +



If j, then v (j

 


) 


) = :(



v (j

)j - and



v (j +



)j



v (j - )



+



=



) +


: :(



: :(



= :


= :







:(







(



)



)j 

j 


:



+


)j 


= v (j ):


CHAPTER 8.Random Walks 105



If j =, then v (



) = v () = and



j



v (j + ) +



v (j - )



=


=



v () +



: :



v ()


:



+



= = + =



< v () =


v (j - )



There is a gap of size




[.]



( 


If j 0, then v (

 


) = 


j



j and


v (


=



=


j + ) +



( 


j + ) +



j 


j 


)



= 
= 


( + )



j



< v (j ) = 


j :



There is a gap of size 1. This concludes the proof of (b).



**Proof:** **(c).** Suppose Y
f



n

k =0 [is some other process satisfying:]

g



k



n

k =0 [is some other process satisfying:]



**(a’)** Yk

**(b’)** (
f



( Sk )+

- 


k ;



)k



Yk



k =0 [is a supermartingale.]

g



We must show that



Yk



v (Sk ) k : (7.1)




Actually, since the put is perpetual, every time k is like every other time, so it will suffice to show



Y0



v (S0 ); (7.2)




provided we let S0 [in (7.2) be any number of the form] j . With appropriate (but messy) conditioning

on k [, the proof we give of (7.2) can be modified to prove (7.1).]
F



0 [in (7.2) be any number of the form]



provided we let S



k [, the proof we give of (7.2) can be modified to prove (7.1).]



For j,

  


v (j



;



= v (S



) = 


= ( 


j


0



so if S0



=



j for some j, then (a’) implies

    


j


j



)+



)+


):



Y0




- ( 


Suppose now that S



0



j for some j, i.e., S

    


0



=



. Let





- = min fk ; S



k



= g



= min fk ; M



k



= j - g:


106


Then


Because (
f



) = v (j



v (S0



) = :(



)j 


)+



)�



( S�

 


i



)k



= IE


k =0 [is a supermartingale]

g



Yk



:


= v (S0):



i




- IE



( S�

 


)+



(

h


(

h



)�



i



(

h



)� Y�



Y0




- IE



**Comment** **on** **the** **proof** **of** **(c):** If the candidate value process is the actual value of a particular
exercise rule, then (c) will be automatically satisfied. In this case, we constructed v so that v (Sk ) is



exercise rule, then (c) will be automatically satisfied. In this case, we constructed v so that v (Sk ) is

the value of the put at time k if the stock price at time k is Sk [and] _[ if we exercise the put the first time]_



k



the value of the put at time k if the stock price at time k is Sk [and] _[ if we exercise the put the first time]_

_(_ k _, or later) that the stock price is 2 or less._ In such a situation, we need only verify properties (a)
and (b).



**8.8** **Difference Equation**


If we imagine stock prices which can fall at any point in (0; ), not just at points of the form j for

integers j, then we can imagine the function v (x), defined for all x - 0, which gives the value of
the perpetual American put when the stock price is x . This function should satisfy the conditions:



**(a)** v (x) (K x)+

   -   


; x,



**(b)** v (x)

   


+r




[pv~ (ux) + q~v (dx)] ; x;



**(c)** At each x, either (a) or (b) holds with equality.


In the example we worked out, we have



For j : v (

  


j



) = :(



j



)j 


=



;



) = 


:



j



This suggests the formula


We then have (see Fig. 8.4):



For j : v (j

  


; x - ;

- x; 0 < x - :



v (x) =



(



x



**(a)** v (x) ( x)

   -   


+ ; x;



**(b)** v (x)

   


h



)i for every x except for < x < .



v (x) +



v (



x


CHAPTER 8.Random Walks 107

###### 5



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-108-0.png)







Figure 8.4: _Graph of_ v (x) _._


Check of condition (c):


If 0 < x, then (a) holds with equality.

  -  
If x, then (b) holds with equality:

  -  






v (x) +



v (



x

)

 


=







x



x



x



+







=



:



If < x < or < x <, then both (a) and (b) are strict. This is an artifact of the

  discreteness of the binomial model. This artifact will disappear in the continuous model, in
which an analogue of (a) or (b) holds with equality at every point.


**8.9** **Distribution of First Passage Times**



Let M
f



k



k =0 [be a symetric random walk under a probability measure] IP, with M

g



0



= 0 . Defining




- = min k 0; Mk
f    


= g;



we recall that



p


 



- 


IE ��



=







; 0 < - < :



We will use this moment generating function to obtain the distribution of - . We first obtain the
Taylor series expasion of IE �� as follows:


108




- x; f (0) = 0



f (x) = 


p



0



; f


; f


; f



( - x)�

( - x)�

( - x)�




- - : : : - (j - )

j



0



( - x)�



f



(x) =


(x) =


(x) =


: : :


(x) =



(0) =



(0) =



00



00



f



(0) =



000



000



f



;



(j )



(j )

 


f


f



(0) =


=


=



(j )








- - : : : - (j - )

j

- - : : : - (j - )

j




- - : : : - (j - )

j

- - : : : - (j - )

j




- - : : : - (j - )



:




- - : : : - (j - )



j 


(j - )!




- j 


(j - )!

(j - )!



(j - )!



The Taylor series expansion of f (x) is given by



f (x) = - p




- x



j =0

X


j =

X



f



(j ) (0)xj



j !





- j 


j  


(j - )!

j !(j - )!

j 


xj



x

!



+







j =

X



j =

X








- 


j 
j



j :



So we have


But also,



IE ��



=


=


=


=


=


=



x


 
 


+





p


 


f (�



)



:

!



(j  - )


j  










(j - )



j = 
X



j 
j



IP f� = j - g:




- j 


IE ��



=



j =

X


CHAPTER 8.Random Walks 109


Figure 8.5: _Reflection principle._


Figure 8.6: _Example with_ j = _._


Therefore,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-110-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-110-1.png)

IP f� = g =

IP f� = j - g =



;





- j 


(j - )



; j = ; ; : : :

!



j 
j



**8.10** **The Reflection Principle**



To count how many paths reach level 1 by time j, count all those for which M

              


To count how many paths reach level 1 by time j -, count all those for which M j - = and

double count all those for which M j . (See Figures 8.5, 8.6.)



j 


j 


. (See Figures 8.5, 8.6.)



110


In other words,



IP f� - j - g = IP fM



j 
j 


= g + IP fM



= g + IP fM




- g



= IP fM



j 



- g + IP fM



j 



- - g



= - IP fM



j 


j 


= - g:



For j,

  


IP f� = j - g = IP f� - j - g - IP f� - j - g



= [ - IP fM



= - g] - [ - IP fM



= IP fM



j 


j 


= - g]



j 


(j - )!



= - g



j  


j 


= - g - IP fM











j 


(j - )







(j - )!

j !(j - )!



=


=


=


=


=











j











j 

j 

j 

j 


(j - )!(j - )!



(j - )!

j !(j - )!

(j - )!

j !(j - )!

(j - )!

j !(j - )!




[ j (j - ) - (j - )(j - )]


[ j (j - ) - (j - )(j - )]



:

!



j 

### **Chapter 9**

# **Pricing in terms of Market Probabilities:** **The Radon-Nikodym Theorem.**

**9.1** **Radon-Nikodym Theorem**



**Theorem 1.27 (Radon-Nikodym)** _Let_ _IP_ _and_



)

f



IP (A) = 0 _._ _Then_ _we_ _say that_



**Theorem 1.27 (Radon-Nikodym)** _Let_ _IP_ _and_ IP _be_ _two_ _probability measures on_ _a_ _space_ (�; ) _._

F
_Assume that for every_ A F _satisfying_ IP (A)f= 0 _,_ _we_ _also have_ IP (A) = 0 _._ _Then_ _we_ _say that_

IP _is_ absolutely continuous _with respect to IP. Under this assumption, there is a nonegative random_

f

_variable_ Z _such that_



f



f



IP (A) =



A

Z



Z dIP ; A ; (1.1)
F



f



IP _with respect to IP._



_and_ Z _is called the_ Radon-Nikodym derivative _of_



f



**Remark 9.1** Equation (1.1) implies the apparently stronger condition



IE X = IE [X Z ]



f



for every random variable X for which IE X Z < .
j j



**Remark 9.2** If IP is absolutely continuous with respect to IP, and IP is absolutely continuous with

respect to IP, we say that IP and IP are _equivalent._ IP and IP are equivalent if and only if



**Remark 9.2** If



f



IP (A) = 0 exactly when



IP, we say that IP and



IP are _equivalent._ IP and



=f



IP are equivalent if and only if



f)



f



IP (A) = 0; A F :



f



If IP and



If IP and IP are equivalent and Z is the Radon-Nikodym derivative of IP w.r.t. IP, then Z [is] [the]

Radon-Nikodym derivative of IP w.r.t. IP, i.e.,



IP are equivalent and Z is the Radon-Nikodym derivative of



f



IP w.r.t. IP, then



f



fIE



IE X = IE [X Z ] X ; (1.2)



IP, i.e.,



f



IE Y =



IE [Y :



Xf



Z



] Y : (1.3)



(Let X and Y be related by the equation Y = X Z to see that (1.2) and (1.3) are the same.)



111


112



**Example 9.1 (Radon-Nikodym Theorem)** Let - = H H ; H T ; T H ; T T, the set of coin toss sequences
f g
of length 2. Let P correspond to probability [for] H and [for] T, and let IP correspond to probability [for]




[for] H and




[for] T, and let



IP correspond to probability



e




[for]



H and




[for] T . Then Z (! ) =



IP (! )



IP (! )

IP (! ) [, so]



IP

e



Z (H H ) =



; Z (H T ) =



; Z (T H ) =



; Z (T T ) =



:



**9.2** **Radon-Nikodym Martingales**



Let - be the set of all sequences of n coin tosses. Let IP be the market probability measure and let



IP be the risk-neutral probability measure. Assume



f



IP (! ) - 0;



IP (! ) - 0; ! �;



f



IP with respect to IP is

f



so that IP and



IP are equivalent. The Radon-Nikodym derivative of



f



Z (! ) =



IP (! )



IP

f



IP (! )



:



Define the IP-martingale



k ]; k = 0; ; : : : ; n:



Zk



= IE [Z jF



We can check that Z



k [is indeed a martingale:]



IE [Zk +



jF



] = IE [IE [Z jF



= IE [Z jF



]



k



k +



]jF



k



k



]



= Z



:



k



**Lemma 2.28** _If_ X _is_ k _[-measurable, then]_
F

**Proof:**



k ] _._



IE X = IE [X Z

f



IE X = IE [X Z ]



f



= IE [IE [X Z jF

= IE [X :IE [Z jF



k ]]



]]



k



= IE [X Z



]:



k



Note that Lemma 2.28 implies that if X is k [-measurable, then for any] A
F F



k [,]



IE [I



X ] = IE [Zk IA



A



or equivalently,



f



Z



A

Z



X d



X Zk



X ];


dIP :



A



IP =

f


CHAPTER 9.Pricing in terms of Market Probabilities 113


_Z (HH) = 9/4_

_2_



_Z (HT) = 9/82_


_Z (TH) = 9/8_

_2_


_Z (TT) = 9/16_

_2_



_Z (H) = 3/2_

_1_



_1/3_


2/3



_Z = 1_

_0_



_Z = 1_



_Z (T) = 3/4_

_1_



1/3


2/3


1/3


2/3



Figure 9.1: _Showing the_ Z



Figure 9.1: _Showing the_ Zk _[values in the 2-period binomialmodel example. The probabilitiesshown]_

_are for IP, not_ IP _._



IP _._

f



**Lemma 2.29** _If_ X _is_
F



k _[-measurable and]_ 0 - j - k _, then_



IE [X jF



] =



Zj



]:



j



IE [X Zk

jF



j



**Proof:** Note first that



Zj



j [-measurable. So for any] A
F



j [, we have]



IE [X Zk



j



] is
F



f


j

jF



A

Z



IP (Lemma 2.28)

f



j



]d



IE [X Zk



jF



]dIP (Lemma 2.28)



IP =



f



=


=



X Zk



Zj



IE [X Zk

jF



j



A

Z


A

Z


A

Z



dIP (Partial averaging)



X d



**Example 9.2 (Radon-Nikodym Theorem, continued)** We show in Fig. 9.1 the values of the martingale Z



**Example 9.2 (Radon-Nikodym Theorem, continued)** We show in Fig. 9.1 the values of the martingale Zk [.]

We always have Z0 =, since



0



=, since



Z0



= IE Z =




 
Z



Z dIP =



IPe (�) = :



**9.3** **The State Price Density Process**


In order to express the value of a derivative security in terms of the market probabilities, it will be
useful to introduce the following _state price density process_ :



�k



= ( + r )�k



Zk



; k = 0; : : : ; n:


114


We then have the following pricing formulas: For a **Simple** **European** **derivative security** with
payoff Ck [at time] k,



k



i (Lemma 2.28)



i

C



i



IE

IfE



Ck



V0



=



h

h



( + r )



�k



= IE



( + r )�k



Zk



= IE [�



Ck



k



]:



More generally for 0 j k,

      -      


�k



jF



Ck



i



Vj



= ( + r )



j



h



( + r )



�k



j



j



h



Ck



=


=



( + r )



�j



IE


j

f



Zk



i (Lemma 2.29)



( + r )



jF



j



IE



jF



]



j



Zj


IE [�k



Ck



**Remark 9.3** f



k

j =0 [is a martingale under IP, as we can check below:]

g



j



Vj



IE [�j +



jF



] = IE [IE [�k Ck



= IE [�k



Ck



jF



j +



j ]



Vj +



j



j



jF

]



= �j



Vj :



jF



Now for an **American derivative security** G
f



n

k =0 [:]

g



k



n

k =0 [:]



IE [( + r )



V0



= sup




 - T



]


G�



��



��



0



G�


Z�



= sup



IfE



IE [( + r )



]




 - T



0



= sup



IE [��



G� ]:




 - T0



More generally for 0 j n,

      -      


f

Zj



IE [( + r )��



jF



Z�



G�



G�



Vj



= ( + r )j


= ( + r )j



sup

- Tj


sup

- Tj



IE [( + r )



j



]jF


]



��



]



j

jF



=



�j



jF



j ]:



sup

- Tj



IE [��



G�



**Remark 9.4** Note that



**(a)** �j
f



Vj nj =0 [is a supermartingale under IP,]

g



**(b)** 


j Vj



�j




Gj



j;


CHAPTER 9.Pricing in terms of Market Probabilities 115



ζ (ΗΗ) = 1.44



_2_



_S (HH) = 16_



_2_



ζ (ΤΤ) = 0.36



_2_



ζ (Η) = 1.20



_1_



_S (H) = 8_



_1_



ζ (ΗΤ) = 0.72



_S (TH) = 42_



_2_



_S (HT) = 4_



_2_



_S = 4_
_0_

ζ  = 1.00

0



1/3


2/3



_S (T) = 2_

_1_



ζ (ΤΗ) = 0.72

_2_



ζ (Τ) = 0.6

_1_



1/3


2/3


1/3


2/3



_S (TT) = 1_



_2_



Figure 9.2: _Showing the state price values_ �k _[. The probabilities shown are for IP, not]_



IP _._

f



**(c)** f



n

j =0 [is the smallest process having properties (a) and (b).]



j



Vj



n

j =0 [is the smallest process having properties (a) and (b).]

g



We interpret 


k [by observing that] 


k



We interpret �k [by observing that] �k (! )IP (! ) is the value at time zero of a contract which pays $1

at time k if ! occurs.


**Example 9.3 (Radon-NikodymTheorem, continued)** We illustrate the use of the valuation formulas for
European and American derivative securities in terms of market probabilities. Recall that p = [,] q = [.] [The]



European and American derivative securities in terms of market probabilities. Recall that p = [,] q = [.] [The]

state price values �k [are shown in Fig. 9.2.]



k [are shown in Fig. 9.2.]




[,] q =



For a **European Call** with strike price 5, expiration time 2, we have



V



(H H ) = ; 


(H H )V



(H H ) = : - = : :



(H T ) = V



(T H ) = V



(T T ) = 0:



V0



=








- : = : :








V


(H H )

V

(H H )




- = :0 - = :0



(H H ) =



:

:0



V



(H ) =




- :0 = :0



Compare with the risk-neutral pricing formulas:



V



(H ) =


V



(T ) =



V



(H H ) +



V



(H T ) =




- = :0;



V



(T H ) +



V



(T T ) = 0;



V0



(H ) +



V



(T ) =




- :0 = : :



=



V



Now consider an **American** **put** with strike price 5 and expiration time 2. Fig. 9.3 shows the values of



�k



( - Sk )



+ . We compute the value of the put under various stopping times - :



**(0)** Stop immediately: value is 1.

**(1)** If - (H H ) = - (H T ) = ; - (T H ) = - (T T ) =, the value is




- :0 = : :








- 0: +


116



_+_
_(5 - S_ _(HH))_ _= 0_
_2_
_+_
_(HH)_ _(5 - S_ _(HH))_ _= 0_
ζ2 _2_



_(5 - S1(H))_ _[+]_ _= 0_



1/3



_(5 - S1(H))_ _[+]_ _= 0_ _+_
_(5 - S_ _(HT))_
_2_



_+_

_(TH)_ _(5 - S_ _(TH))_

ζ2 _2_



_(TH)_ _(5 - S_ _(TH))_



_(HT))_



_= 1_



_= 0.72_



_+_

_(HT)_ _(5 - S_ _(HT))_

ζ2 _2_



_+_
_(5 - S_ _(TT))_ _= 4_
_2_
_+_

_(TT)_ _(5 - S_ _(TT))_

ζ2 _2_



_(HT)_ _(5 - S_ _(HT))_



_(TT))_



_(5-S0)_ _[+]_ _=1_

ζ0 _(5-S0)_ _[+]_ _=1_



ζ1 _(H)_


1/3


2/3



_+_
_(5 - S_ _(TH))_
_2_



_(TH))_



_= 1_



_= 0.72_



2/3


1/3


2/3



ζ1 _(T)_



_+_
_(5 - S1(T))_

_+_
_(5 - S1(T))_



_= 3_

_= 1.80_



_= 4_



_(TT)_ _(5 - S_ _(TT))_



_= 1.44_



Figure 9.3: _Showing the values_ �k ( Sk )+ _for an American put._ _The probabilities shown are for_

          
_IP, not_ IP _._



Figure 9.3: _Showing the values_ 


( - S



)



k



IP _._

f



k



**(2)** If we stop at time 2, the value is
















- 0: +




- 0: +




- : = 0:



We see that (1) is optimal stopping rule.


**9.4** **Stochastic Volatility Binomial Model**



Let - be the set of sequences of n tosses, and let 0 < d



k



k k k k k k

are k [-measurable.] [Also let]
F



< + r



k



< u



k [, where for each] k, d



; u



k



; r



k [-measurable.] [Also let]



k




- d



k



; q~k



)



:



k



p~k



=



+ rk



uk



=



uk




- ( + r



u



k



; q~k




- d



k




- d



k



Let



IP be the risk-neutral probability measure:



f



IP f!



fIP



= H = p~0
g



;



= H = p~0
g

= T = q~0
g



= T g = q~



;



and for k n,

   -   


IP [!



IP

f



IP f!



f



] = p~k



= H jF



k +



IP [!



k


k



] = p~k


] = q~k



] = q~k



;


:



= T jF



f



k +



Let IP be the market probability measure, and assume IP ! - 0 ! - . Then IP and IP are
f g

equivalent. Define



Let IP be the market probability measure, and assume IP ! - 0 ! - . Then IP and
f g



f



Z (! ) =



IP (! )



IP

f



IP (! )



! �;


CHAPTER 9.Pricing in terms of Market Probabilities 117



= IE [Z jF



]; k = 0; ; : : : ; n:



Zk



k



We define the _money market price process_ as follows:



M0 = ;



; k = ; : : : ; n:



Mk



= ( + rk 


)Mk 


Note that M



k [is] F



k [-measurable.]

 


We then define the _state price process_ to be



Mk



Zk



�k



=



; k = 0; : : : ; n:



As before the portfolio process is f



As before the portfolio process is �k nk =0� [.] [The] [self-financing] [value] [process] [(wealth] [process)]
f g

consists of X0 [, the non-random initial wealth, and]



g



k



n�



0 [, the non-random initial wealth, and]



+ ( + rk



�k




Sk



); k = 0; : : : ; n - :



Xk +



= �k



Sk +



)(Xk



Then the following processes are martingales under



IP :



f



Xk











Sk



n

and
k =0



Mk



n


k =0



;



Mk











and the following processes are martingales under IP:



�k
f



nk =0 and  
g f



Sk



k



Xk



n

k =0



:



g



We thus have the following pricing formulas:


**Simple European derivative security** with payoff Ck [at time] k :



F



Ck




 
 



 
 


IE

f







Mk





]



Vj



= Mj



k



j



j



Ck



=



�j



jF




 



 


IE [�



**American derivative security** G
f



n

k =0 [:]

g



k















sup

 - Tj







M�






] :



Vj



= Mj



G�



F



j


j



=



�j



IE [�



IE

f



G�







jF



sup

- Tj







The usual hedging portfolio formulas still work.


118


**9.5** **Another Applicaton of the Radon-Nikodym Theorem**



Let (�; ; Q) be a probability space. Let be a sub- - -algebra of, and let X be a non-negative
F G F
random variable with X dQ = . We construct the conditional expectation (under Q ) of X



random variable with X dQ = . We construct the conditional expectation (under Q ) of X

       
given . On, define two probability measures
G G R



R







IP (A) = Q(A) A G ;



IP (A) =



Z



A X dQ A G :



f



Whenever Y is a -measurable random variable, we have
G




 
Z



Y dIP =




 
Z



Y dQ;



if Y =



if Y = A [for some] A, this is just the definition of IP, and the rest follows from the “standard

G
machine”. If A and IP (A) = 0, then Q(A) = 0, so IP (A) = 0 . In other words, the measure IP
G



IP (A) = 0 . In other words, the measure



f



A G IP (A) = 0 Q(A) = 0 IP (A) = 0 IP

is absolutely continuous with respect to the measure IP . The Radon-Nikodym theorem implies that



is absolutely continuous with respect to the measure IP . The Radon-Nikodym theorem implies that

f f

there exists a -measurable random variable Z such that
G f



f



f



=



A Z dIP A G ;

Z



i.e.,



Z



IP (A)

f



X dQ =



Z dIP A G :



A



Z



A



This shows that Z has the “partial averaging” property, and since Z is -measurable, it is the conG
ditional expectation (under the probability measure Q ) of X given . The existence of conditional
G
expectations is a consequence of the Radon-Nikodym theorem.


### **Chapter 10**

# **Capital Asset Pricing**

**10.1** **An Optimization Problem**


Consider an agent who has initial wealth X0 [and wants to invest in the stock and money markets so]

as to maximize



IE log Xn :



**Remark 10.1** Regardless of the portfolio used by the agent, f



k =0 [is a martingale under IP, so]

g

(B C )



k



Xk



IE �n



Xn



= X0



Here, (BC) stands for “Budget Constraint”.


**Remark 10.2** If - is any random variable satisfying (BC), i.e.,



IE �n - = X0



;



then there is a portfolio which starts with initial wealth X0 [and produces] Xn = - at time n . To see

this, just regard - as a simple European derivative security paying off at time n . Then X0 [is its value]



then there is a portfolio which starts with initial wealth X



0 [and produces] X



n



this, just regard - as a simple European derivative security paying off at time n . Then X0 [is its value]

at time 0, and starting from this value, there is a hedging portfolio which produces Xn = - .



n



= - .



Remarks 10.1 and 10.2 show that the optimal Xn [for] [the] [capital] [asset] [pricing] [problem] [can] [be]

obtained by solving the following

**Constrained Optimization Problem:**
Find a random variable - which solves:


Maximize IE log                 


Subject to IE 


n - = X0



:



Equivalently, we wish to
Maximize



!X�



(log - (! )) IP (! )



119


120


There are



n sequences ! in - . Call them !



Subject to



X



�n



= 0:



! 


(! )� (! )IP (! ) X0

    


; !



; : : : ; !



n . Adopt the notation



); x



= - (!


n



); : : : ; x



x



= - (!



):



n



= - (!



n



We can thus restate the problem as:



Maximize


n



k =

X



(log xk )IP (!



k



)



Subject to


In order to solve this problem we use:



k =

X



k =

X



(!



)xk



k



) Xo

 


= 0:



�n



k



IP (!



**Theorem 1.30 (Lagrange Multiplier)** _If_ (x




 






m



) _solve the problem_



; : : : ; x



_Maxmize_ f (x



; : : : ; xm



; : : : ; x



)



_Subject to_ g (x


_then there is a number_ - _such that_



; : : : ; xm



; : : : ; x



) = 0;



@

@ xk



f (x� ;



�m




 


@

@ xk







m



); k = ; : : : ; m; (1.1)



g (x�



; : : : ; x



) = 


; : : : ; x



_and_



g (x�


For our problem, (1.1) and (1.2) become







) = 0: (1.2)



; : : : ; x



m



k



) = ��n


n



)IP (! k



); k = ; : : : ;



n ; (: 0



)



(!



k



�k



IP (!



x



k =

X



)x�k



IP (! k



) = X0 : (: 0



)



�n



(! k



k =



Equation (1.1’) implies



x�k



=



��n (!



k



:

)



Plugging this into (1.2’) we get



n



) = X0



=)











k =

X



IP (!



k



= X0



:


CHAPTER 10. Capital Asset Pricing 121



Therefore,


Thus we have shown that if 

then



)



�k



�k



�n



X0

(!



n :



x



=



k



; k = ; : : : ;




- solves the problem



Maximize IE log Subject to IE (� n - )



0




- ) = X



(1.3)
;



n




- 


X0



=



�n



: (1.4)



**Theorem 1.31** _If_ 



- _is given by (1.4), then_ - - _solves the problem (1.3)._



**Proof:** Fix Z - 0 and define


We maximize f over x - 0 :



f (x) = log x - xZ :



0



0 (x) =



Z = 0 x =

x - ()



Z



f



;



(x) =

  - x

Z [, i.e.,]



< 0; x IR:



f



00



The function f is maximized at x�



=



log x           - xZ           - f (x� ) = log

Let - be any random variable satisfying



Z



; x   - 0; Z   - 0: (1.5)




IE (�n - ) = X0



and let


From (1.5) we have


Taking expectations, we have


and so




- 


X0



=



�n



:







�n

X0

 


X0

�n



log  -  -  

IE log - 







- log








- :




- ;



IE (�n







X0




- ) - IE log 


IE log - - IE log 






:


122


In summary, capital asset pricing works as follows: Consider an agent who has initial wealth X0

and wants to invest in the stock and money market so as to maximize



IE log Xn :



The optimal X



n [is] X



n



�n Xn



X




0

n [, i.e.,]



=



0



= X0 :



Since f


so



n

k =0 [is a martingale under IP, we have]

g



k



Xk



jF



�k



Xk



= IE [�n



Xn



k



] = X0 ; k = 0; : : : ; n;



=



X0

�k







�k +



k



;T )



and the optimal portfolio is given by



Xk


X



(!

(!



X



(!



; : : : ; !



0



k



; : : : ; !



; : : : ; !k



0



;


;H )



�k



(!



Sk + (!



�k +



; : : : ; !k



; : : : ; !



; : : : ; !



k



) =



:



; H ) Sk +

  


; : : : ; !



; T )


### **Chapter 11**

# **General Random Variables**

**11.1** **Law of a Random Variable**


Thus far we have considered only random variables whose domain and range are discrete. We now
consider a general random variable X : - IR defined on the probability space (�; ; P) . Recall
! F
that:


is a      - -algebra of subsets of      - .

  - F

IP is a probability measure on, i.e., IP (A) is defined for every A .

  - F F

A function X : - IR is a random variable if and only if for every B (IR) (the - -algebra of
! B
Borel subsets of IR), the set



fX B g



= X







(B )



= f! ; X (!) B g F ;



i.e., X : �!IR is a random variable if and only if X - is a function from B (IR) to F (See Fig.

11.1)



i.e., X : - IR is a random variable if and only if X
!



Thus any random variable X induces a measure �X [on the] [measurable] [space] (IR; (IR)) defined

B
by



(B ) . F











B B (IR);



�X



(B ) = IP



X



(B )



where the probabiliy on the right is defined since X - (B ) F . �X [is often called the] _[ Law of]_ X 
in Williams’ book this is denoted by X [.]
L



where the probabiliy on the right is defined since X








X [.]



**11.2** **Density of a Random Variable**



The _density of_ X (if it exists) is a function fX



: IR [0; ) such that
!


(x) dx B B (IR):


123



B

Z



fX



�X



(B ) =


124



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-125-0.png)





_X_


Figure 11.1: _Illustrating a real-valued random variable_ X _._



We then write



d�X



(x) = fX (x)dx;



where the integral is with respect to the Lebesgue measure on IR. f



where the integral is with respect to the Lebesgue measure on IR. fX [is the Radon-Nikodym deriva-]

tive of �X [with] [respect] [to] [the] [Lebesgue] [measure.] [Thus] X has a density if and only if �X [is]



tive of �X [with] [respect] [to] [the] [Lebesgue] [measure.] [Thus] X has a density if and only if �X [is]

absolutely continuous with respect to Lebesgue measure, which means that whenever B (IR)
B
has Lebesgue measure zero, then



X [with] [respect] [to] [the] [Lebesgue] [measure.] [Thus] X has a density if and only if 


IP fX B g = 0:


**11.3** **Expectation**


**Theorem 3.32 (Expectation of a function of** X **)** _Let_ h : IR IR _be given. Then_
!



IE h(X )



=


=


=




 
Z


IR

Z


IR

Z



h(X (! )) dIP (! )



h(x)fX (x) dx:



h(x) d�X (x)



**Proof:** (Sketch). If h(x) =



B



(x) for some B IR, then these equations are

    


= P fX B g



IE



B (X )



= 


(B )



X



=



fX

B

Z



(x) dx;



which are true by definition. Now use the “standard machine” to get the equations for general h .


CHAPTER 11. General Random Variables 125



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-126-0.png)





Figure 11.2: _Two real-valued random variables_ X ; Y _._


**11.4** **Two random variables**


Let X ; Y be two random variables - IR defined on the space (�; ; P) . Then X ; Y induce a
! F
measure on (IR ) (see Fig. 11.2) called the _joint law of_ (X ; Y ), defined by
B



= IP f(X ; Y ) C g C B (IR



):



�X ;Y



(C )



The _joint density of_ (X ; Y ) is a function


fX ;Y


that satisfies



: IR



! [0; )



ZCZ



fX ;Y (x; y ) dxdy C (IR

B



):



�X ;Y



(C ) =



fX ;Y [is the Radon-Nikodym derivative of] 


X ;Y [with respect to the Lebesgue measure (area) on] IR



.



We compute the expectation of a function of X ; Y in a manner analogous to the univariate case:



IE k (X ; Y )



=


=


=



Z



IZRZ







k (x; y )fX ;Y



k (X (! ); Y (! )) dIP (! )



Z Z



k (x; y ) d�X ;Y



(x; y )



IR



(x; y ) dxdy


126


**11.5** **Marginal Density**


Suppose (X ; Y ) has joint density f



X ;Y [. Let] B IR be given. Then

   


�Y



(B ) = IP fY B g



= IP f(X ; Y ) IR - B g



= 


X ;Y



(IR - B )



Z

Z



Z



(x; y ) dxdy



B


B



Z



IR



fX ;Y



fY



(y ) dy ;



where


Therefore, f



Y



Z



fY



=


=


(y )



=



IR



(x; y ) dx:



fX ;Y



(y ) is the (marginal) density for Y .



**11.6** **Conditional Expectation**



Suppose (X ; Y ) has joint density f



X ;Y [.] [Let] h : IR IR be given. Recall that IE [h(X ) Y ]
! j



=



IE [h(X ) �(Y )] depends on ! through Y, i.e., there is a function g (y ) ( g depending on h ) such that
j



IE [h(X )jY ](! ) = g (Y (! )):

How do we determine g ?

We can characterize g using _partial averaging:_ Recall that A - (Y ) A = Y B for some
() f g

B (IR) . Then the following are equivalent characterizations of g :
B



A

Z



g (Y ) dIP =



A

Z



h(X ) dIP A - (Y ); (6.1)




 
Z



(y )h(x) d�X ;Y




 
Z


B



B (Y )h(X ) dIP B (IR); (6.2)

B



B



(Y )g (Y ) dIP =



IR

Z


Z



(dy ) =



IZRZ



(y )h(x) d�



(x; y ) B (IR); (6.3)
B



B



(y )g (y )�Y



IR

Z



(y ) dy =



B

Z



h(x)fX ;Y



(x; y ) dxdy B (IR): (6.4)
B



B



g (y )fY


CHAPTER 11. General Random Variables 127


**11.7** **Conditional Density**



A function fX jY (xjy ) : IR ![0; ) is called a _conditional density_ for X given Y provided that for

any function h : IR IR :
!



A function f



X jY



(xjy ) : IR



g (y ) =



IR

Z



h(x)fX jY (xjy ) dx: (7.1)



(Here g is the function satisfying



IE [h(X )jY ] = g (Y );

X Y [does not.)]
j



and g depends on h, but f



IE [h(X )jY ] = g (Y );



**Theorem 7.33** _If_ (X ; Y ) _has a joint density_ fX ;Y _[, then]_



(x; y )

: (7.2)

(y )



fX ;Y

fY



fX jY



(xjy ) =



**Proof:** Just verify that g defined by (7.1) satisfies (6.4): For B (IR);
B



B

Z



Z



g (y )

| {z }



IR

Z



(xjy ) dx



B

Z



h(x)fX ;Y



(x; y ) dxdy :



(y ) dy =



IR



h(x)fX jY



fY



g (y )



**Notation 11.1** Let g be the function satisfying



The function g is often written as


and (7.1) becomes



IE [h(X )jY ] = g (Y ):


g (y ) = IE [h(X )jY = y ];



IE [h(X )jY = y ] =



IR

Z



h(x)fX jY



(xjy ) dx:



In conclusion, to determine IE [h(X ) Y ] (a function of ! ), first compute
j



g (y ) =



IR

Z



h(x)fX jY (xjy ) dx;



and then replace the dummy variable y by the random variable Y :


IE [h(X )jY ](! ) = g (Y (! )):

**Example 11.1 (Jointly normal random variables)** Given parameters: 
(X ; Y ) have the joint density




- 0; 



- 0; < - < . Let

  



- ( 
  


y




��



fX;Y



(x; y ) =




 - 


)



y




:







p




- 


exp

 


x

 



x

  
- 


+


128


The exponent is







y




y

 
- 


y








( - 

= 

= 


)



x

 




- 


+



x



x




x 



��

 






( - 


y




( - 

( - 


"





)


)







+



y

 






y

 

��

 


:



We can compute the _Marginal density of_ Y as follows



)

#


dx:e











x 



y



fY



(y ) =


=


=




 - 

 - 


p - 


)�







Z



p


�




- 


u

e�



�

Z


du:e



(��

e�


y

  



using the substitution u =



p �� 





y



y 



-, du =



x  



:



y




e�



Thus Y is normal with mean 0 and variance - [.]

**Conditional density.** From the expressions



y

 

dx

p ��


;


:



e�


��

 


y

 

y

 


x�

 

;



��

 

��

 


(x; y ) =


(xjy ) =


=



p - 


fY



(x; y )

(y )



(��



)




 - 






p




- 



 
e






y




fY (y ) =



p - 


e�



we have


In the x -variable, f



X jY



fX;Y


fX jY



(x y ) is a normal density with mean
j



fX;Y



x 



p




- 


) 


��

 


)�



(��

e�



y and variance ( 
     



[.] [Therefore,]



�

Z



IE [X jY = y ] =



xfX jY



(xjy ) dx =



��

 


y ;



















y

 


IE



" X 
 


��

 


Y = y



y

 


#



fX jY



(xjy ) dx



=



Z



�



x 



��




= ( - 


)�



:


CHAPTER 11. General Random Variables 129


From the above two formulas we have the formulas



IE [X jY ] =



��

 


Y ; (7.3)







IE



" X 
 


��

 


Y











Y



= ( - 


)�



: (7.4)



#



Taking expectations in (7.3) and (7.4) yields


IE X =






��

 






IE Y = 0; (7.5)



"







IE



X 



��




Y



#



= ( - 


)�



: (7.6)



Based on Y, the best estimator of X is



Based on Y, the best estimator of X is ��� Y . This estimator is unbiased (has expected error zero) and the

expected square error is ( - )� [.] [No other estimator based on] Y can have a smaller expected square error

       


��




expected square error is ( - )� [.] [No other estimator based on] Y can have a smaller expected square error

       
(Homework problem 2.1).



)�



**11.8** **Multivariate Normal Distribution**


Please see Oksendal Appendix A.



Let X denote the column vector of random variables (X ; X ; : : : ; Xn )T, and x the corresponding

column vector of values (x ; x ; : : : ; xn )T . X has a multivariate normal distribution if and only if



Let X denote the column vector of random variables (X



; X



; : : : ; X



n



)



column vector of values (x ; x ; : : : ; xn )T . X has a multivariate normal distribution if and only if

the random variables have the joint density



; x



; : : : ; x



n



)




 
n



:A:(X - �)

    


; : : : ; �n



pdet A

( - )n=



)



exp



T

(X - - )



(x) =


= (�



:



Here,



fX





= IE X



= (IE X



; : : : ; IE Xn



T



)T



;



and A is an n - n nonsingular matrix. A� is the covariance matrix



j



A�



;



= IE



(X - �):(X - �)



T



i



i.e. the (i; j ) thelement of A



i.e. the (i; j ) thelement of A� IE (Xi - �i )(Xj - �j ) . The random variables in X are independent

if and only if A� is diagonal, i.e.,




- is IE (Xi



)(X




- 


�i




h


i



j




- is diagonal, i.e.,



i



A�



= diag (�



; 


; : : : ; �n



; : : : ; 


);



where 


j



�j




) is the variance of Xj [.]



= IE (Xj


130


**11.9** **Bivariate normal distribution**


Take n = in the above definitions, and let




- 
 


)(X - 


��  


;

#



)

:



IE (X







=



Thus,



"




 
��



p








- 




(��



)



;






)


 










A =



A�


 


=


 

 


(���



(���



)







(��









(��



pdet A =







)


;



and we have the formula from Example 11.1, adjusted to account for the possibly non-zero expectations:



)








- 
 


)(x





- 


)



+




- 



)



#)



:




 - 






( - 


�(x



(x



fX



;X



) =



(x



; x



)



" (x




- 



exp



(�



p




- 


**11.10** **MGF of jointly normal random variables**



Let u = (u ; u ; : : : ; un )T denote a column vector with components in IR, and let X have a

multivariate normal distribution with covariance matrix A� and mean vector - . Then the moment



Let u = (u



; u



; : : : ; u



n



)



multivariate normal distribution with covariance matrix A� and mean vector - . Then the moment

generating function is given by







euT



f

X







IE euT



:X



=



: : :



Z



; X



; : : : ; xn



; : : : ; x



) dx



: : : dx



n



:X



; : : : ; Xn



; : : : ; X



(x



; x



u + uT



�



Z

T



�







= exp



n



u



A



:



If any n random variables X



If any n random variables X ; X ; : : : ; Xn [have] [this] [moment] [generating] [function,] [then] [they] [are]

jointly normal, and we can read out the means and covariances. The random variables are jointly
normal _and independent_ if and only if for any real column vector u = (u ; : : : ; un )T



; X



; : : : ; X



; : : : ; u



)



n



T



n



<

:



<



n



IE euT



:X



= IE exp



<

:



<



j =

X



uj



Xj



j =

X




[



�j




- j



uj



+ uj



]



=

;



:



=

;



= exp


### **Chapter 12**

# **Semi-Continuous Models**

**12.1** **Discrete-time Brownian Motion**



Let Y
f



Let Yj nj = [be a collection of independent, standard normal random variables defined on] (�; ; P),

where IP is the f g _market measure_ . As before we denote the column vector (Y ; : : : ; Yn )T by YF . We



j



g



n



=
where IP is the _market measure_ . As before we denote the column vector (Y ; : : : ; Yn )T by Y . We

therefore have for any real colum vector u = (u ; : : : ; un )T,



)



; : : : ; Y



n



; : : : ; u



)



n



T,



;



n



IE euT Y



= IE exp



<



n


j =

X



uj



<



j =

X



uj



=

;



Yj



=



= exp



:



:



j =



Define the _discrete-time Brownian motion_ (See Fig. 12.1):



:



B0


Bk



= 0;


k



=



j =

X



Yj



; k = ; : : : ; n:



j =



If we know Y



If we know Y ; Y ; : : : ; Yk [, then we know] B ; B ; : : : ; Bk [. Conversely, if we know] B ; B ; : : : ; Bk [,]

then we know Y = B ; Y = B B ; : : : ; Yk = Bk Bk [.] [Define the filtration]



; Y



; : : : ; Y



k [, then we know] B



; B



; : : : ; B



k [. Conversely, if we know] B



k [.] [Define the filtration]

 


; : : : ; B



; B



= B




- B



k



; Y



= B



; : : : ; Y



= B



k




- B



F

F



F



= - (Y



; Y



0


k



= f�; �g;



; : : : ; Y



k



) = - (B



; : : : ; Bk



; : : : ; B



); k = ; : : : ; n:



; B



**Theorem 1.34** Bk
f

**Proof:**



n

gk =0 _[is a martingale (under IP).]_



IE [Bk +



jF



k ] = IE [Yk +



= IE Yk +



+ Bk



k



]



+ Bk



jF



= Bk


131



:


132


**Theorem 1.35** B
f

**Proof:** Note that














|Bk|Col2|
|---|---|
|_Y_<br>_Y_<br>_Y_<br>_1_<br>_2_<br>_3_<br>_k_|_Y_<br>_4_|
|_k_<br>_0_<br>_1_<br>_2_<br>_3_<br>_4_|_k_<br>_0_<br>_1_<br>_2_<br>_3_<br>_4_|



k



Figure 12.1: _Discrete-time Brownian motion._


n

gk =0 _[is a Markov process.]_



IE [h(Bk +

Use the Independence Lemma. Define


g (b) = IE h(Yk +



)jF



k ] = IE [h(Yk +



+ Bk



)jF



k



]:



dy :




 


y



+ b) =



p



h(y + b)e�

Z�



Then


which is a function of Bk [alone.]



IE [h(Yk +



+ Bk



)jF



k



);



] = g (Bk



**12.2** **The Stock Price Process**


Given parameters:




 - IR, the _mean rate of return._





 -  - 0, the _volatility._




S0





- 0, the initial stock price.



The _stock price process_ is then given by



; k = 0; : : : ; n:



exp




 - Bk

n



+ (� 


)k







Sk



= S0







Note that



exp




 - Yk +

n



+ (� 


Sk +



= Sk







) ;

 

CHAPTER 12. Semi-Continuous Models 133



k




 


IE [Sk +

jF



] = Sk



]:e��



k



IE [e� Yk +







jF



= Sk

= e�



e






:




 
e 


Sk



Thus


and



]



= log IE

    


F



















Sk +

Sk




- = log



IE [Sk +



Sk



jF



k




 


;



k



= 






Sk +

Sk



= var - Yk +

   


var



log




+ (� 


)

 






:



**12.3** **Remainder of the Market**


The other processes in the market are defined as follows.

Money market process:



= er k ; k = 0; ; : : : ; n:



= �k

= �k



Sk +



Portfolio process:




- 


; : : : ; 


k [is]
F



;



0



; 


Each  



k [-measurable.]



n�



Wealth process:


X0 [given, nonrandom.]

  
  


Mk


k +



k



Sk



Sk



+ er (Xk



)



) + e



(Sk +




- e



r



Xk




- 


r



Each X




k [is]
F



X


k [-measurable.]



Discounted wealth process:







M



Xk +

Mk +



= �k







Mk +



Sk +



S



k

k



X

M



k

k







+



:



**12.4** **Risk-Neutral Measure**



**Definition 12.1** Let



IP be a probability measure on (�; ), equivalent to the market measure IP. If
F



f







n



k =0 [is a martingale under]



IP, we say that



f



n



Sk

Mk



IP is a _risk-neutral measure._



f


134


**Theorem 4.36** _If_



f







n

k =0 _[is]_



Xk

Mk



IP _is a risk-neutral measure, then every_ _discounted wealth process_



n



_a martingale under_



IP _, regardless of the portfolio process used to generate it._



f



**Proof:**








 
 



 
 



 


















F



F



+























F



X



IE

f











M



S



k

k






k

k



X

M




k

k



IE

f



IE



Xk +

Mk +



�k







=



= 


k



k



k









 


Sk

Mk



+



Sk +

Mk +

Sk +

Mk +




 


IE







M



k





:



IE

f



=


**12.5** **Risk-Neutral Pricing**



X

M



k

k



Let V



n [be the payoff at time] n, and say it is
F



n [-measurable. Note that] V



n [may be path-dependent.]



Hedging a short position:



Sell the simple European derivative security V




n [.]



Receive X




0 [at time 0.]



Construct a portfolio process  



0 [and ends with] Xn



= Vn [.]



0



n [which starts with] X

 


If there is a risk-neutral measure




; : : : ; 
IP, then



f



0



IE

f



X

M



n



IE

f



n



X



n



V

M



n



=



=



:



**Remark 12.1** Hedging in this “semi-continuous” model is usually not possible because there are
not enough trading dates. This difficulty will disappear when we go to the fully continuous model.



**12.6** **Arbitrage**


**Definition 12.2** An _arbitrage_ is a portfolio which starts with X0



= 0 and ends with X



n [satisfying]



IP (Xn



0) = ; IP (Xn





- 0) - 0:



(IP here is the market measure).


**Theorem 6.37 (Fundamental Theorem of Asset Pricing:** **Easy part)** _If there is a risk-neutralmea-_
_sure, then there is no arbitrage._


CHAPTER 12. Semi-Continuous Models 135



**Proof:** Let



f



X

M



IP be a risk-neutral measure, let X



**Proof:** Let IP be a risk-neutral measure, let X0 = 0, and let Xn [be the final wealth corresponding]

to any portfolio process. Since Xk n [is a martingale under] IP,



n



= 0, and let X



0



IP,

f



k

k







n



k =0 [is a martingale under]



=



IE



IE

f



M



X



0

0



IE



X



n

n



= 0: (6.1)



M



Suppose IP (Xn



0) = . We have




IE

f



IP (Xn



0) = = IP (Xn

- )



< 0) = 0 =)



IP (X

f



IP (X



n



IfP (Xn




- 0) = :
(6.2)



< 0) = 0 =)



(6.1) and (6.2) imply



IP (X



= 0) = . We have



n



IP (X



= 0) = =)



IP (X

f



IP (X



n




- 0) = 0 = IP (Xn - 0) = 0:
)



f



f



n



This is not an arbitrage.



**12.7** **Stalking the Risk-Neutral Measure**


Recall that




- Y



; Y



; : : : ; Y



(�; ; P) .
F



n [are independent, standard normal random variables on some probability space]



Sk





= S0



exp




 - B

n



n



k



+ (� 


)k - .








- (Bk




- Yk +



+ Yk + ) + (�

    


Sk +



= S0



exp


exp







)(k + )

   


:


 


= Sk



n

n



+ (� 






)

 


)



;




Therefore,



Sk +

Mk +



=


=


=



: exp



S



M



k



k

k


k

k



+ (� - r 


M



k




 - Yk +

n







S















k

 


S



IE







Mk +



Sk +



g



] : expf� - r 






F



:IE [exp - Yk +
f



g jF



k



M



g: expf� - r 






g



: expf







= e��r



Sk

M



:



k

k



:



If - = r, the market measure is risk neutral. If - = r, we must seek further.


136


where


The quantity



��� r is denoted - and is called the _market price of risk_ .



Sk +

Mk +



=


=


=



Sk

M

Sk

M

Sk

M



k



k



+ (� - r 


)

 



k




- Yk +









k



��� r )

  


k




- (Yk +



+



k



~






:



k +



;








: exp


: exp


: exp



n

n

n







Y



Y~k +



= Yk +



+



��� r



We want a probability measure



IP under which



f



We want a probability measure IP under which Y~ ; : : : ; Y~n [are] [independent, standard normal ran-]

dom variables. Then we would have



; : : : ;



Y~



Y



~




 



 



 



 


=


=


=



S



F







gjF



k

 


M



S



k

k


k

k


k

k



~



i




IE

f







Sk +

Mk +



h



expf�



Y



k +



g



k



: expf�

g







:



M



M



g: expf�



: expf



IE

f



S



:



**Cameron-Martin-Girsanov’s Idea:** Define the random variable


n



Z = exp



(   - Yj

 
j =

X











)



:



Properties of Z :


Z 0 .

  -  
  

Define







n

 


n







IE Z = IE exp



<



j



)



=



;



: exp




 



(�� Y







j =







j =

X







:�



= exp



n







n







: exp



= :




IP (A) =



A

Z



Z dIP A F :



Then



IP (A) 0 for all A and

  - F



f



f



IP (�) = IE Z = :



In other words,



IP is a probability measure.



f



f


CHAPTER 12. Semi-Continuous Models 137



We show that



IP is a risk-neutral measure. For this, it suffices to show that



f



Y~



= Y



Y



+ - ; : : : ;



~



n



= Yn + 


are independent, standard normal under

**Verification:**



IP .

f




- Y



; Y



; : : : ; Yn [: Independent, standard normal under IP, and]



IE exp



n


j =

X



uj Yj



n


j =

X



uj



= exp



+ - ; : : : ;



= Yn







Y~ = Y



Y~n



+ - :



Z - 0 almost surely.




j

h

P



( - Yj

 



- Z = exp



n

j =











)

i



;



IP (A) =

f



A

Z



Z dIP A F ;



IE X = IE (X Z ) for every random variable X .



f



Compute the moment generating function of (




:


IP :

f



Y~



~



) under


n



; : : : ;



Y~



n



n



IE exp

f



n

uj

j =

X



~



j =

X

n


j =

X



(Yj



+ - ) +



(   - Yj

 
j =

X

n







Y







)



j



= IE exp


= IE exp


n



uj



(uj




 - )Yj




: exp



j =

X



(uj 
  


j =



= exp


= exp


= exp



j =

X

n


j =

X

n


j =

X



(



uj



(uj




- - )



: exp



n


j =

X



(uj 
  





 



- )


)


)

 


uj uj

 

:




- +







) + (uj 
   

138


**12.8** **Pricing a European Call**


Stock price at time n is




 - B

n



Sn


Payoff at time n is (S



= S0



n



exp


exp


exp


exp



)n

 


+ (� 






n


n



= S0



<



;



(Yj



Yj



+ (� 






)n



=



j =

X



j =

X







n



= S0



:

<









+



��� r



) - (� - r )n + (� 


)n



=

;



=



j =

X



j =



n



= S0



:

<







Y



~



j



)n



=

;



:



+ (r 






j =

X



:




- K )



+
. Price at time zero is



+




- K )



=


=



+



n



0



@



S0



~



IE

f

Z



�r n




- b + (r 



- K



IE

f



(Sn



e�r n



<







j =

X



Y



j



)n



=



+ (r 






e



M



n







:



+

;







Y



b

n


IP .

f



db



0



A




- K



+



)n







p




 - n



e



S



exp


exp



:







�

since



�



P



n



j =







n



~



j [is normal with mean 0, variance] n, under



This is the _Black-Scholes_ price. It does not depend on - .


### **Chapter 13**

# **Brownian Motion**

**13.1** **Symmetric Random Walk**


Toss a fair coin infinitely many times. Define



= H ;


= T :



if !

( if !

 


j


j



Xj



(! ) =



Set



M0


Mk



= 0


k



=



j =

X



Xj



; k - :



**13.2** **The Law of Large Numbers**


We will use the method of moment generating functions to derive the Law of Large Numbers:


**Theorem 2.38 (Law of Large Numbers:)**



! 0 _almost surely, as_ k !:


139



k



Mk


140


**Proof:**


which implies,







u

k



'k



(u) = IE exp


= IE exp


k





<



Mk



k



u

k



=



= (Def. of M

;



k : )



j [’s)]



j =

X



Xj








- (Independence of the X



:



=


=



j =

Y







IE exp



u

k



Xj



+





;



u

e k



�k



e�



u

k



+



e�ux 


u

k






+



(u) = k log



u

k



e�



e



Let x =



log 'k


k [. Then]







eux



lim

k !



log 'k



(u) = lim

x 0
!



log



u



eux

eux



�ux



(L’Hˆopital’s Rule)
�ux





+



e



u



x

e



= lim

x 0
!



= ;



Therefore,



lim



'k



= 0:


(u) = e0



k !



which is the m.g.f. for the constant 0.



**13.3** **Central Limit Theorem**


We use the method of moment generating functions to prove the Central Limit Theorem.

**Theorem 3.39 (Central Limit Theorem)**



pk



Mk


'



! _Standard normal, as_ k ! :



**Proof:**



Mk



u



p



k



(u) = IE exp











;



+







k



u

pk



=







k


e







e



u

pk


CHAPTER 13. Brownian Motion 141


so that,



+







:



u

pk



u

e pk



e�



log 'k



(u) = k log







Let x =




[Then]

pk [.]



eux +


x



e�ux 


lim

k !



log 'k



(u) = lim

x 0
!



log

  


u



eux



e�ux







(L’Hˆopital’s Rule)

- u ux u ux



u



= lim

x 0
!



ux



e�ux



e



+



�ux



u



ux







e



u



= lim

x 0
!



x

 

eux



e



: lim

x 0
!



e�ux

u e�ux



x



eux



x




+




= lim

x 0
!



u


u



eux



e�ux



u



(L’Hˆopital’s Rule)



= lim



=



x 0
!



u



:



Therefore,



;



lim

k !



u



'k



(u) = e



which is the m.g.f. for a standard normal random variable.


**13.4** **Brownian Motion as a Limit of Random Walks**



Let n be a positive integer. If t 0 is of the form

        


k

n [, then set]



(n)



Mtn

n



p



Mk

pn



B



(t) =



=



:



If t 0 is not of the form

 


nk [, then define] B



(n) (t) by linear interpolation (See Fig. 13.1).



Here are some properties of B



(00)



(t) :


142



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-143-0.png)
### _k/n (k+1)/n_



Figure 13.1: _Linear Interpolation to define_ B



(n)



(t) _._



Properties of B



(00)



() :



B (00)


IE B (00)



() =


() =



0


0



IE Xj



00


j =

X

00


j =

X



Xj (Approximately normal)



= 0:



(00)



var(B



()) =



00



) =



00


j =

X



var(Xj



Properties of B



(00)



() :



B (00)


IE B (00)



() = 0:



() =



0



00


j =

X



Xj (Approximately normal)



(00)



var(B



()) = :



Also note that:



() - B




- B

- B



(00) () are independent.



(00)


(00)



() and B



(t) is a continuous function of t .



(00)



To get Brownian motion, let n in B (n)
!


**13.5** **Brownian Motion**


(Please refer to Oksendal, Chapter 2.)



(t); t 0 .

  

CHAPTER 13. Brownian Motion 143

|B(t) = B(t,ω)<br>ω<br>t|Col2|
|---|---|
|ω|ω|
|ω|_t_|


##### (Ω, F,P)


Figure 13.2: _Continuous-time Brownian Motion._


A random variable B (t) (see Fig. 13.2) is called a Brownian Motion if it satisfies the following
properties:


1. B (0) = 0,

2. B (t) is a continuous function of t ;

3. B has independent, normally distributed increments: If





0 = t0



< t



< t



< : : : < tn



and


then



) B (t0

 


); Y



= B (t



) - B (t



); : : : Yn



= B (tn



) - B (tn�



);



Y



= B (t




- Y



; Y



; : : : ; Yn [are independent,]




- IE Y



j



= 0 j;




- var(Y



j



) = t



j



tj




j 


j:



**13.6** **Covariance of Brownian Motion**


Let 0 s t be given. Then B (s) and B (t) B (s) are independent, so B (s) and B (t) =

  -   -   
(B (t) B (s)) + B (s) are jointly normal. Moreover,

  
IE B (s) = 0; var(B (s)) = s;


IE B (t) = 0; var(B (t)) = t;



IE B (s)B (t) = IE B (s)[(B (t) - B (s)) + B (s)]



= IE B (s)(B (t) - B (s))



+ IE B



(s)



0

s:| {z }



s

| {z }



0



= s:


144


Thus for any s 0, t 0 (not necessarily s t ), we have

    -     -     
IE B (s)B (t) = s ^ t:


**13.7** **Finite-Dimensional Distributions of Brownian Motion**


Let



0 < t



< t



< : : : < tn



be given. Then

(B (t

is jointly normal with covariance matrix



); B (t



); : : : ; B (tn ))



) IE B (t



)B (t



) : : : IE B (t



)B (tn

)B (tn



)

)



(t



)B (t



) IE B



(t



) : : : IE B (t



C =


=



IE B

IE B (t



: : : : : : : : : : : : : : :



: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :



IE B (tn



)B (t



) IE B (tn )B (t



) : : : IE B



(tn



)



t

t



t

t



: : : t

: : : t



t



t



: : : tn



**13.8** **Filtration generated by a Brownian Motion**


fF (t)gt�0

Required properties:



For each t, B (t) is (t) -measurable,

- F



n [, the Brownian motion increments]



For each t and for t < t




< t



< - - - < t



B (t



) - B (t) ; B (t



) - B (t



); : : : ; B (tn



) - B (tn� )



are _independent of_ (t) _._
F

Here is one way to construct (t) . First fix t . Let s [0; t] and C (IR) be given. Put the set
F B

fB (s) C g = f! : B (s; ! ) C g

in (t) . Do this for all possible numbers s [0; t] and C (IR) . Then put in every other set
F B
required by the - -algebra properties.

This (t) contains exactly the information learned by observing the Brownian motion upto time t .
F



t 0 [is called the] _[ filtration generated by the Brownian motion.]_




fF (t)g


CHAPTER 13. Brownian Motion 145


**13.9** **Martingale Property**


**Theorem 9.40** _Brownian motion is a martingale._


**Proof:** Let 0 s t be given. Then

    -    


IE [B (t)jF (s)] = IE [(B (t) - B (s)) + B (s)jF (s)]



= IE [B (t) - B (s)] + B (s)



= B (s):



**Theorem 9.41** _Let_ - IR _be given. Then_


Z (t) = exp


_is a martingale._


**Proof:** Let 0 s t be given. Then

    -    


�� B (t) 
n







t

 


F (s)



IE [Z (t)jF (s)] = IE


= IE








exp f�� (B (t) - B (s) + B (s)) 


Z (s) expf�� (B (t) - B (s)) 






((t - s) + s)g























F (s)

  


(t - s)g



(t - s)g




 



 



 
 










n



(�� )







= Z (s)IE



h



expf�� (B (t) - B (s)) 



 





 
 


= Z (s) exp



var(B (t) - B (s)) 


(t - s)



i



= Z (s):



**13.10** **The Limit of a Binomial Model**


Consider the n ’th Binomial model with the following parameters:



un




= +







n



: “Up” factor. ( - - 0 ).

: “Down” factor.




- d







n



= 


p

 
p



n



r = 0 .




p~n




un

[.]



�d




- =

 - =



p

p



n

n



=




[.]



=



n



�d



n


n



q~n




=


=


146



Let ]



k



(H ) denote the number of H in the first k tosses, and let ]



Let ]k (H ) denote the number of H in the first k tosses, and let ]k (T ) denote the number of T in the

first k tosses. Then



k



]k


]k



(T ) = k ;


(T ) = Mk



;



which implies,



(H ) + ]k

(H ) ]k

  


]k (H ) =

]k (T ) =



nk [for some] k, and let



In the n ’th model, take n steps per unit time. Set S0(n)



(k + Mk )

(k Mk ):

 
= . Let t =







:











(nt+Mnt



)



(nt�Mnt



)



(t) =







n







+



p



p







S



(n)







n



Under



IP, the price process S



f



(n)
is a martingale.



**Theorem 10.42** _As_ n _, the distribution of_ S
!



(t) _converges to the distribution of_



(n)



expf� B (t) 






tg;



_where_ B _is_ _a_ _Brownian motion._ _Note_ _that_ _the_ _correction_ - - t _is_ _necessary_ _in_ _order_ _to_ _have_ _a_

_martingale._



_where_ B _is_ _a_ _Brownian motion._ _Note_ _that_ _the_ _correction_ 






**Proof:** Recall that from the Taylor series we have



x



+ O (x );



so



log( + x) = x 


) +



(nt + Mnt



) log( +



log S



(n) (t) =



p







n



) log( 


p







(nt Mnt

 


n







= nt







log( +



p







n



log ( 


p







n



) +



)







) 


+ Mnt



log( +



p







n



log ( 


p







n



)

 






+ O (n� =



)

!



= nt


+ M



p







p







p



n



+ O (n� =



n







n








 
n







)

!







nt



p



n






 
n





n


+



= 


)







t + O (n



0

| !{z }



+


Mnt





n


)



+ 






p



n



Mnt







n



+











O (n�







Bt

| !{z }



Bt
!



t



0
!



As n, the distribution of log S
!



(t) approaches the distribution of - B (t)

           


(n)



)


t .


CHAPTER 13. Brownian Motion 147

|B(t) = B(t,ω)<br>x<br>ω<br>t|Col2|
|---|---|
|ω|ω|
|ω|_t_|



(Ω, _F, P_ _[x]_ _)_


Figure 13.3: _Continuous-time Brownian Motion, starting at_ x = 0 _._


**13.11** **Starting at Points Other Than 0**


(The remaining sections in this chapter were taught Dec 7.)

For a Brownian motion B (t) that starts at 0, we have:


IP (B (0) = 0) = :



For a Brownian motion B (t) that starts at x, denote the corresponding probability measure by IP

(See Fig. 13.3), and for such a Brownian motion we have:



x



(B (0) = x) = :



IP



x



Note that:



If x = 0, then IP




x puts all its probability on a completely different set from IP.



x is the same as the distribution of x + B (t) under IP.



The distribution of B (t) under IP




**13.12** **Markov Property for Brownian Motion**


We prove that


**Theorem 12.43** _Brownian motion has the Markov property._


**Proof:**

Let s 0; t 0 be given (See Fig. 13.4).

  -  


F (s)

  






h( B (s + t) - B (s)

Independentof F (s)
| {z }



)















F (s)



+ B (s)

F (s) -measurable

| {z }



IE



h(B (s + t))
















= IE






148


##### _B(s)_

|Col1|Col2|
|---|---|
|||
|_s_<br>_s+t_|_s_<br>_s+t_|


##### _restart_

Figure 13.4: _Markov Property of Brownian Motion._


Use the Independence Lemma. Define


g (x) = IE [h( B (s + t)           - B (s) + x )]



= IE


= IE



)



x



h( x + B (t)

same distribution as B (s + t)      - B (s)

h(B (t)): | {z }



Then



= E



= g (B (s))



IE



h (B (s + t) )
















F (s)











B (s)h(B (t)):



In fact Brownian motion has the _strong Markov property._


**Example 13.1 (Strong Markov Property)** See Fig. 13.5. Fix x - 0 and define


                  - = min ft                  - 0; B (t) = xg :

Then we have:



F (� )

  


h(B (t)):



IE



h( B (� + t) )


















x



= g (B (� )) = IE






CHAPTER 13. Brownian Motion 149

##### _x_



|Col1|Col2|
|---|---|
|||
|τ +_t_<br>τ|τ +_t_<br>τ|

##### _restart_





Figure 13.5: _Strong Markov Property of Brownian Motion._


**13.13** **Transition Density**


Let p(t; x; y ) be the probability that the Brownian motion changes value from x to y in time t, and
let - be defined as in the previous section.



e�



(y x)
�t



p(t; x; y ) =



p - t



p



h(B (t)) =



g (x) = IE



x



Z

�



h(y )p(t; x; y ) dy :



= g (B (s)) =

Z

�



h(y )p(t; B (s); y ) dy :



IE


IE



h(B (s + t))








h(B (� + t))











F (s)












 



 



 



 










F (� )



=



Z

�



h(y )p(t; x; y ) dy :



**13.14** **First Passage Time**


Fix x - 0 . Define



Fix - - 0 . Then


is a martingale, and




- = min ft - 0; B (t) = xg :



exp




 - B (t ^  - )  
n







(t ^ - )

   


IE exp




 - B (t ^ - ) 
n







(t ^ - )

   


= :


150


We have




- if - < ;











<



lim

t!



exp




 
n



n



e



(14.1)
0 if - = ;







(t ^ - )

   


=



:



0 - expf� B (t ^ - ) 



 
:







(t ^ - )g - e




- x



Let t in (14.1), using the Bounded Convergence Theorem, to get
!



exp f� x 
h








 - g f� <g

i



= :



Let - 0 to get IE
#



f� <g



IE


=, so



IP f� < g = ;



IE expf�



: (14.2)








 - g = e



�� x



Let - =







. We have the m.g.f.:



IE e���


Differentiation of (14.3) w.r.t. - yields



= e�xp




 


; - - 0: (14.3)



e�xp




 






:



�IE



�� e���



= 


p



x




 


Letting - 0, we obtain
#



IE                    - = : (14.4)


**Conclusion.** Brownian motion reaches level x with probability 1. The expected time to reach level

x is infinite.

We use the Reflection Principle below (see Fig. 13.6).



IP f� - t; B (t) < xg = IP fB (t) - xg



IP f� - tg = IP f� - t; B (t) < xg + IP f� - t; B (t) - xg



= IP fB (t) - xg + IP fB (t) - xg



= IP fB (t) - xg



Zx



y

e� t



=



p - t



dy


CHAPTER 13. Brownian Motion 151

###### _x_


|Col1|shado|
|---|---|
|||
|||


###### τ




###### _Brownian motion_

Figure 13.6: _Reflection Principle in Brownian Motion._



Using the substitution z =



y

p



t



dy



p



t [we get]



; dz =



Zx

pt



z

e�



IP f� - tg =



p 


dz :



Density:



IP f� - tg =


b



x


 - t



x

e� t



@

@ t



p



f�



(t) =



which follows from the fact that if


then


Laplace transform formula:


IE e���



F (t) =



aZ(t)



g (z ) dz ;



@ F

@ t



= 


@ a

@ t



;


:



g (a(t)):


(t)dt = e



=



Z0



e��t



f�



�xp




 

152


### **Chapter 14**

# **The Itˆo Integral**

The following chapters deal with _Stochastic Differential Equations in Finance_ . References:


1. B. Oksendal, _Stochastic Differential Equations_, Springer-Verlag,1995

2. J. Hull, _Options, Futures and other Derivative Securities,_ Prentice Hall, 1993.


**14.1** **Brownian Motion**


(See Fig. 13.3.) (�; ; P) is given, always in the background, even when not explicitly mentioned.
F
**Brownian motion**, B (t; ! ) : [0; ) - IR, has the following properties:

          - !


1. B (0) = 0; Technically, IP ! ; B (0; !) = 0 =,
f g

2. B (t) is a continuous function of t,



3. If 0 = t



0



: : : tn [, then the increments]

- 



- t



B (t


are _independent,normal,_ and



) B (t0 ); : : : ; B (tn

 


) - B (tn�



)



IE [B (tk +



k



)] = 0;



IE [B (tk +



) - B (t



) - B (t



)]



= tk +



tk




k



:



**14.2** **First Variation**


Quadratic variation is a measure of volatility. First we will consider _first variation_, F V (f ), of a
function f (t) .


153


154









_**t**_



_**t**_


|Col1|f(t)|Col3|Col4|
|---|---|---|---|
||**_t_**<br>**_2_**|**_t_**<br>**_2_**||
||**_t_**<br>**_1_**|**_T_**|**_T_**|



Figure 14.1: _Example function_ f (t) _._


For the function pictured in Fig. 14.1, the first variation over the interval [0; T ] is given by:



) - f (0)] - [f (t

t



) - f (t



)] + [f (T ) - f (t

T



)]



F V




[0;T ](f ) = [f (t


t



Z0


T



f 0


jf



0 (t)j dt:



tZ



tZ



=


=



(t) dt +



tZ



(�f



0



0 (t)) dt +



f



0 (t) dt:



Z0



Thus, first variation measures the total amount of up and down motion of the path.

The general definition of first variation is as follows:



**Definition 14.1 (First Variation)** Let - = t
f



; t



; : : : ; tn



be a _partition_ of [0; T ], i.e.,
g


= T :



0



0 = t0


The _mesh_ of the partition is defined to be




- t



: : : tn

- 



 - = max
jj jj k =0;::: ;n

      



 - = max
jj jj k =0;::: ;n



(tk +



tk ):




We then define



n�


k =0

X



f (tk +
j



) f (tk

 


)j:



F V



(f ) = lim

jj�jj!0



(f ) = lim




[0;T ]



Suppose f is differentiable. Then the Mean Value Theorem implies that in each subinterval [t



Suppose f is differentiable. Then the Mean Value Theorem implies that in each subinterval [tk ; tk + ],

there is a point t� [such that]



k



; t



k +



�k [such that]



�k



�k



�k



)(tk +



f (tk +



) f (tk ) = f

 


0



(t



tk




):


CHAPTER 14. The Itˆo Integral 155



Then


and



n�


k =0

X



�k



�k



f (tk +
j



) f (tk

 


)j =



n�


k =0

X



k =0



jf



0



(t



) (tk +
j



tk );




�k



n�


k =0

X



jf



0



(t



) (tk +
j



tk




)



F V




[0;T ]



(f ) = lim

jj�jj!0



(f ) = lim



k =0



=



T

Z0



jf



0



0 (t)j dt:



**14.3** **Quadratic Variation**



**Definition 14.2 (Quadratic Variation)** The _quadraticvariation_ of a function f on an interval [0; T ]
is



:



f (T ) = lim
h i - 0

jj jj!



f (T ) = lim
h i 


n�



k =0



k =0

X



f (tk +
j



)j



) f (tk

 


**Remark 14.1 (Quadratic Variation of Differentiable Functions)** If f is differentiable, then f (T ) =
h i

0, because



n�



n�



) f (tk

 


�k



�k



(tk +



k =0

X



(t



)j


jf



tk




)



)j



=



n�


k =0

X



k =0



jf



0



k =0



f (tk +
j



0



0 (t



�k



k =0

X



)j



(tk +



tk )





- jj�jj:



k =0



and


**Theorem 3.44**


_or more precisely,_



�k



)j



f (T ) lim
h i - - 0

jj jj!




 - : lim
jj jj - 0

jj jj!




 - : lim
jj jj 


n�


k =0

X



jf



0



(t



(tk +



tk




)



T



= lim

jj�jj! 0

= 0:



jj�jj



Z0



jf



0



(t)j



dt



hB i(T ) = T ;



IP f! �; hB (:; !)i(T ) = T g = :

_In particular, the paths of Brownian motion are not differentiable._


156



**Proof:** (Outline) Let - = t
f



; t



; : : : ; t



n



be a partition of [0; T ] . To simplify notation, set D
g



=



0



k



B (t



k +



) - B (t



k



) . Define the _sample quadratic variation_



Dk



Q�



=



n�


k =0

X



:



k =0



Then


We want to show that



n�

[Dk

k =0

X



(tk +




tk




)]:



Q�




- T =



lim



(Q




- T ) = 0:







Consider an individual summand



jj�jj!0



tk




) = [B (tk +



) B (tk

 


)]



(tk +




tk




):



Dk



(tk +




This has expectation 0, so


IE (Q�




- T ) = IE



n�


k =0

X



(tk +




tk




)] = 0:




[Dk



k =0



For j = k, the terms


are independent, so



k (tk +

 


(tj +




) and D



tk




)



Dj



tj




tk




)]



var(Q�


Thus we have




- T ) =


=


=


=



n�


k =0

X



k =0

X



var[Dk



(t



k +



k =0

n�


k =0

X



(tk +




tk )Dk




+ (tk +



tk )




]


tk




k =0

n�


k =0

X



IE [Dk (tk +

  


) = 



[(tk +



)



(tk +




tk )




+ (tk +



)



]



k =0



tk




(if X is normal with mean 0 and variance 


, then IE (X



)



n�



tk )




k =0




- jj�jj



n�


k =0

X



k =0



(t



k +



tk )




= jj�jj T :



IE (Q�




- T ) = 0;

- T ) - jj�jj:T :



var(Q�


CHAPTER 14. The Itˆo Integral 157



As - 0, var(Q
jj jj!







T ) 0, so

- !



lim



(Q




- T ) = 0:



jj�jj!0







**Remark 14.2 (Differential Representation)** We know that



IE [(B (tk +



) B (tk

 


))



(tk +




tk )] = 0:




We showed above that


var[(B (tk +



) - B (t



))




- (t



k +




- t



k




- t



k )] = (tk +



k



)



:



When (t



k +



tk




) is small, (tk +



)



is _very_ small, and we have the approximate equation



tk




(B (tk +


which we can write informally as



) B (tk

 


))



tk +
'



tk




;



dB (t) dB (t) = dt:


**14.4** **Quadratic Variation as Absolute Volatility**



On any time interval [T



; T



], we can sample the Brownian motion at times




- t



: : : tn = T

- 


T



= t0



and compute the _squared sample absolute volatility_



) B (tk ))

 


n�


k =0

X



(B (tk +



:



T




- T



k =0



This is approximately equal to




- T

- T



) - hB i(T



T

)] =

T



= :




[hB i(T



T




- T



As we increase the number of sample points, this approximation becomes exact. In other words,
Brownian motion has _absolute volatility 1._



Furthermore, consider the equation


hB i(T ) = T =



T

Z0



dt; T - 0:



This says that quadratic variation for Brownian motion accumulates at rate 1 _at_ _all_ _times_ _along_
_almost every path_ .


158


**14.5** **Construction of the Itˆo Integral**


The **integrator** is Brownian motion B (t); t 0, with associated filtration (t); t 0, and the

            - F             following properties:



1. s t= every set in (s) is also in (t),

  - ) F F



2. B (t) is (t) -measurable, t,
F



) - B (t); B (t



n



3. For t t

   



- : : : - t



n [, the increments] B (t



t   - t   - : : :   - tn B (t )   - B (t); B (t )   - B (t ); : : : ; B (tn )   - B (tn� )

are independent of (t) .
F



) - B (t



); : : : ; B (t



) - B (t



n�



The **integrand** is - (t); t 0, where

       
1.  - (t) is (t) -measurable t (i.e.,  - is adapted)
F

2.  - is square-integrable:

T



IE







(t) dt < ; T :



We want to define the **Itˆo Integral:**


I (t) =



Z0



Z0


t




- (u) dB (u); t - 0:



**Remark 14.3 (Integral w.r.t.** **a differentiable function)** If f (t) is a differentiable function, then
we can define



t



Z0



0 (u) du:




- (u) df (u) =



Z



t


0




- (u)f



This won’t work when the integrator is Brownian motion, because the paths of Brownian motion
are not differentiable.


**14.6** **Itˆo integral of an elementary integrand**



Let - = t
f



; : : : ; t



n



be a partition of [0; T ], i.e.,
g



0



; t



0 = t0




- t



: : : tn

- 


= T :



Assume that - (t) is constant on each subinterval [t



Assume that - (t) is constant on each subinterval [tk ; tk + ] (see Fig. 14.2). We call such a - an

_elementary process_ .



k



; t



k +



The functions B (t) and - (tk



) can be interpreted as follows:



Think of B (t) as the _price per unit share_ of an asset at time t .



CHAPTER 14. The Itˆo Integral 159



δ( _**t**_ )



_**=**_ δ( _**t**_ )



_**=**_ δ( _**t**_ )



δ( _**t**_ )
δ( _**t**_ ) _**=**_ δ( _**t**_ )




###### **_t t t_**



δ( _**t**_ )



_**=**_ δ( _**t**_ )
_**2**_



Think of t




Figure 14.2: _An elementary function_     - _._


; : : : ; tn [as the] _[ trading dates]_ [ for the asset.]



0



; t



Think of  - (t




Think of - (tk ) as the _number of shares of the asset acquired_ at trading date tk [and held until]

trading date tk + [.]



) as the _number of shares of the asset acquired_ at trading date t



k + [.]



k



Then the Itˆo integral I (t) can be interpreted as the _gain from trading_ at time t ; this gain is given by:




- (t0



)[B (t) - B (t



0



)



]; 0 - t - t



=B (0)=0



I (t) =



>>



>>






>>



>>

<





<




- (t0

- (t0



) - B (t

) - B (t



B (0)=0

|B {z(t0 }



0



)] + - (t


)] + - (t



)[B (t) - B (t



)[B (t



)]; t



:








)[B (t


)[B (t



0





>>



0



>>






>:



) - B (t



)] + - (t



)[B (t) - B (t



)]; t




- t - t

- t - t



>:



In general, if t



k



t tk + [,]

- 


I (t) =



k 

j =0

X




- (tj



)[B (tj +



) B (tj

 


)] + - (tk )[B (t) B (tk

    


)]:



j =0



**14.7** **Properties of the Itˆo integral of an elementary process**


**Adaptedness** For each t; I (t) is (t) -measurable.
F

**Linearity** If



t



t



I (t) =



Z0




- (u) dB (u); J (t) =



Z0




- (u) dB (u)



then



t



I (t) - J (t) =



0

Z



(� (u) - - (u)) dB (u)


160



_**s**_ _**t**_

_**tl**_ _**t**_ _**l+1**_ _**. . . . .**_ _**tk**_ _**tk+1**_



Figure 14.3: _Showing_ s _and_ t _in different partitions._



and


**Martingale** I (t) is a martingale.



cI (t) =



t


0

Z



c� (u)dB (u):



We prove the martingale property for the elementary process case.


**Theorem 7.45 (Martingale Property)**



I (t) =


_is a martingale._



k 

j =0

X




- (tj



)[B (tj +



) B (tj )] + - (tk

 


)[B (t) B (tk )]; tk

  


t tk +

- 


**Proof:** Let 0 s t be given. We treat the more difficult case that s and t are in different

    -     subintervals, i.e., there are partition points t` [and] tk [such that] s [t` ; t`+ ] and t [tk ; tk + ] (See



subintervals, i.e., there are partition points t` [and] tk [such that] s [t` ; t`+ ] and t [tk ; tk + ] (See

Fig. 14.3).



` [and] t



k [such that] s [t



`



; t



`+



] and t [t



k



; t



k +



Write



`�


j =0

X



I (t) =




- (tj



)[B (tj +



) B (tj

 


)] + - (t`



)[B (t`+



) B (t`

 


)]



j =0



+



k 

j =`+

X




- (tj



)[B (tj + ) B (tj

   


)] + - (tk



)[B (t) B (tk

  


)]



We compute conditional expectations:



) B (tj

 


))











F (s)



=



`�


j =0

X



j =0




- (tj



)(B (tj + ) B (tj

   


)):



IE



`�


j =0

X




 - (tj



)(B (tj +



j =0



= - (t` )[B (s) B (t`

    


) B (t`

 


))












 



 



 



 


F (s)

  


) (s)] B (t` ))
jF 


IE








- (t`



)(B (t`+



= - (t` ) (IE [B (t`+



)]


CHAPTER 14. The Itˆo Integral 161


These first two terms add up to I (s) . We show that the third and fourth terms are zero.



)(B (tj +



) B (tj

 


))




 



 
 



 
 



 


F (s)



=


=



j =`+



k 

=`

X

k 

=`

X



))





















F (t



)













F (s)

  


IE



k 

=`

X




 - (tj




- (tj




 - (tj




)(B (tj +



) B (tj

 



- 
 






j



j =`+



IE


IE



IE




) (IE [B (tj +



)jF (t



j



)] - B (t



))















F (s)



j



j =`+



=0

| {z }



=0







=0

| {z }



=0



















F (s)

  



- (tk



) (IE [B (t)jF (t



k



)] - B (t



F (s)



IE




 - (tk




)(B (t) B (tk

  


))



k



))



















= IE



**Theorem 7.46 (Itˆo Isometry)**



t



0

Z



(u) du:



IE I



(t) = IE




 


**Proof:** To simplify notation, assume t = tk [, so]


k



j =0

X



j



I (t) =




- (tj



)[B (tj +



) - B (t



j



)]



)]



D



Each D



j [has expectation 0, and different] Dj



j [are independent.]



Dj

| {z }



k



0




  

j =0

X



j =0

X



(tj )Dj



I



(t) =


=



@k




 - (tj



)Dj



i<j

X




- (ti



)� (tj



j =0



k



A

+



)Di



Dj



:



Since the cross terms have expectation zero,


k



j =0

X



j =0

X



j =0

X



IE [�



(tj


(t



)Dj



]



IE I



(t) =


=


=



j =0



k



j =0

X



) B (tj

 


))



















(tj
F



)

��



IE



j



)IE



(B (tj +

 


j =0




 



k



tj




)



IE 


)(tj +



t



(tj


tj +



= IE


= IE



k


j =0

X



0

Z



tZ







(u) du



t



j



t







(u) du


162





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-163-0.png)

Figure 14.4: _Approximating a general process by an elementary process_    

**14.8** **Itˆo integral of a general integrand**


Fix T - 0 . Let - be a process (not necessarily an elementary process) such that


   - (t) is (t) -measurable, t [0; T ],

  - F




_[, over]_ [0; T ] _._




- IE



R



T


0







(t) dt < :



**Theorem 8.47** _There is a sequence of elementary processes_ f



n



gn= _[such that]_



(t) - - (t)j


T



T


0



lim

n!



dt = 0:



IE



Z



�n
j



**Proof:** Fig. 14.4 shows the main idea.


In the last section we have defined


In


for every n . We now define



(T ) =



Z



�n



(t) dB (t)



0



T


0

Z




- (t) dB (t) = lim

n!



T


0

Z



�n



(t) dB (t):


CHAPTER 14. The Itˆo Integral 163


The only difficulty with this approach is that we need to make sure the above limit exists. Suppose

n and m are large positive integers. Then



T



(t)] dB (t)

!



var(In



(T ) Im

  


(T )) = IE



0

Z

T


0

T


0

T


0

Z




[�n (t) �m

  


T



(Itˆo Isometry:) = IE


= IE



Z

Z




[ �n
j



(t) - (t) + - (t) �m

 - j j  



[�n



(t) �m

 


(t)]



dt



(t)j ]



((a + b)




- a



+ b



:) - IE



�n (t) - (t)
j - j



dt + IE



T


0

Z



�m
j



dt


(t) - - (t)j



dt;



which is small. This guarantees that the sequence I
f



n



(T ) n= [has a limit.]
g



**14.9** **Properties of the (general) Itˆo integral**



I (t) =



Z



t


0




- (u) dB (u):



Here - is any adapted, square-integrable process.



**Adaptedness.** For each t, I (t) is (t) -measurable.
F



**Linearity.** If



t



t



I (t) =



Z0




- (u) dB (u); J (t) =



Z0




- (u) dB (u)



then


and



t



I (t) - J (t) =



0

Z



(� (u) - - (u)) dB (u)


t

c� (u)dB (u):



cI (t) =



Z



0



**Martingale.** I (t) is a martingale.

**Continuity.** I (t) is a continuous function of the upper limit of integration t .



**Itˆo Isometry.** IE I



R



(t) = IE



t


0







(u) du .



**Example 14.1 ()** Consider the Itˆo integral



Z



T



B (u) dB (u):



0



We approximate the integrand as shown in Fig. 14.5


164


By definition,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-165-0.png)

Figure 14.5: _Approximating the integrand_ B (u) _with_ - _[, over]_ [0; T ] _._



B (0) = 0 if 0 u < T =n;

      


�n (u) =










>>



>>






><



><



B (T =n) if T =n u < T =n;

       


: : :



>>



>>




(n�T)T if

   



- u < T :





>>



B







(n�)T

n



>>

:





:



B

- 


k T

n




��



0

Z



T



(k + )T

n




 - B




B (u) dB (u) = lim

n!



n�


k =0

X



B







k T

n



:



To simplify notation, we denote


so










;



Bk = B



k T

n




B (u) dB (u) = lim

n!



n�


k =0

X



Bk



(Bk +




- Bk



):



We compute



T


0

Z



n�


k =0

X



(Bk +




- Bk







Bk +



)



=


=


=


=



n�


k =0

X



Bn



+


+





Bk +



n�

Bk

k =0

X

n�



Bk



+



n�


k =0

X



Bn







n�


j =0

X



Bj



k =0

X



Bk



n�


k =0

X



k =0



Bk



+



j =0



n�



Bn



k =0

X



Bk



n�


k =0

X



k =0

X



B



Bk +


k +



Bk



k =0



n�






(B



k +



k =0

X



k =0

X



Bk




- Bk ):


CHAPTER 14. The Itˆo Integral 165


Therefore,




- 


k

T



Bk (Bk +




- Bk



) =



Bn


=



n�

(Bk +


k =0

X




- Bk )



or equivalently



n�


k =0

X



n�


k =0

X



(k + )T

n





 - B




k T

n




��






B



n�







;


(k + )T

n



B

- 


��



B




B







k T

n



k =0

X


T :



:



Let n and use the definition of quadratic variation to get
!



T


0

Z



B (u) dB (u) =



B



(T ) 

(T ) 


**Remark 14.4 (Reason for the**



T **term)** If f is differentiable with f (0) = 0, then



�:



:




0

Z



Z



T



f (u) df (u) =


=


=







T



Z



T


0


f


f



(T ):



f (u)f



0



0 (u) du







(u)



0



In contrast, for Brownian motion, we have



T


0

Z



B (u)dB (u) =



B



(T ) 


T :



The extra term



The extra term T comes from the nonzero quadratic variation of Brownian motion. It has to be

there, because



B (u) dB (u) = 0 (Itˆo integral is a martingale)



T



IE



Z



0



but



IE



B



(T ) =



T :



**14.10** **Quadratic variation of an Itˆo integral**


**Theorem 10.48 (Quadratic variation of Itˆo integral)** _Let_



I (t) =



t


0

Z




- (u) dB (u):



_Then_



hI i(t) =



Z



t


0







(u) du:


166


This holds even if - is not an elementary process. The quadratic variation formula says that at each
time u, the _instantaneous absolute_ _volatility_ of I is - (u) . This is the absolute volatility of the

Brownian motion scaled by the size of the position (i.e. - (t) ) in the Brownian motion. Informally,
we can write the quadratic variation formula in differential form as follows:



dI (t) dI (t) = 


(t) dt:



Compare this with



dB (t) dB (t) = dt:



**Proof:** (For an elementary process - ). Let - = t
f



; : : : ; t



n [.] [We have]



be the partition for -, i.e., - (t) =
g



k



0



; t



n




- (t



k



) for t




- t - t



k + [. To simplify notation, assume] t = t



n�


k =0

X



hI i(t) =



)] :



k =0




[ I (tk +
h i



) I (tk

 - h i



Let us compute I (t
h i


Then


so


It follows that



) . Let - = s
f



= s0



; : : : ; sm



; : : : ; s



be a partition
g



k +



) I (tk

 - h i

tk



0



; s




- s



: : : sm

- 

sj +



= tk +



:



I (sj +



) I (sj

 


) =



sZj



s




- (tk ) dB (u)



j



= - (tk



) [B (sj +



) B (sj

 


)] ;



I (tk +
h i



) I (tk ) =

 - h i



m�


j =0

X




[I (sj + ) I (sj

   


)]



= 


(tk



)



m�



j =0

X



)]



j =0




[B (sj + ) B (sj

   


jj�jj!0

�����!



)(tk +



tk ):








(tk



hI i(t) =


=



n�


k =0

X



k =0


n�


k =0

X



)(tk +



tk )





- (tk


tk +



k =0



t



tZ



k






t


0

Z



(u) du


t



jj�jj!0

������!







(u) du:


### **Chapter 15**

# **Itˆo’s Formula**

**15.1** **Itˆo’s formula for one Brownian motion**


We want a rule to “differentiate” expressions of the form f (B (t)), where f (x) is a differentiable
function. If B (t) were also differentiable, then the ordinary _chain rule_ would give



d

f (B (t)) = f

dt



0



0



0 (B (t))B 0



0 (t);



which could be written in differential notation as



0



df (B (t)) = f


= f



0

0



0 (B (t))B 0



0 (B (t))dB (t)



0 (t) dt



However, B (t) is not differentiable, and in particular has nonzero quadratic variation, so the correct
formula has an extra term, namely,



df (B (t)) = f



0 (B (t)) dB (t) +



f



00 (B (t)) dt



:



t)

|{z}



dB (t) dB (t)



This is _Itˆo’s formula in differential form._ Integrating this, we obtain _Itˆo’s formula in integral form:_



t



t


0

Z



f (B (t)) - f (B (0))



=



0

Z



f



0 (B (u)) dB (u) +



f



00 (B (u)) du:



f (0)

| {z }



f (0)



**Remark 15.1 (Differential vs. Integral Forms)** The mathematically meaningful form of Itˆo’s formula is Itˆo’s formula in integral form:



t



t


0

Z



f (B (t)) - f (B (0)) =



0

Z



f



0 (B (u)) dB (u) +


167



f



00 (B (u)) du:


168


This is because we have solid definitions for both integrals appearing on the right-hand side. The
first,



t


0



Z



0



f



(B (u)) dB (u)



is an _Itˆo integral_, defined in the previous chapter. The second,



t


0



Z



f



00



(B (u)) du;



is a _Riemann integral_, the type used in freshman calculus.

For paper and pencil computations, the more convenient form of Itˆo’s rule is _Itˆo’s formula in differ-_
_ential form:_



0



df (B (t)) = f



0 (B (t)) dB (t) +



00



f



(B (t)) dt:



There is an intuitive meaning but no solid definition for the terms df (B (t)); dB (t) and dt appearing
in this formula. This formula becomes mathematically respectable only after we integrate it.


**15.2** **Derivation of Itˆo’s formula**



Consider f (x) =



x, so that



f 0



00



(x) = x; f



(x) = :



Let x



k



; xk + [be numbers. Taylor’s formula implies]



(xk



f (xk + ) f (xk

   


) = (xk +



xk




)f



0 (xk



) +



(xk +



xk




)



):



f



00



In this case, Taylor’s formula to second order is _exact_ because f is a _quadratic function_ .



In the general case, the above equation is only approximate, and the error is of the order of (x



k +







xk



)



. The total error will have limit zero in the last step of the following argument.



Fix T - 0 and let - = t
f



0 ; t



; : : : ; t



n be a partition of [0; T ] . Using Taylor’s formula, we write:

g



f (B (T )) - f (B (0))



=



B



(T ) 


B



(0)



=


=


=



n�


k =0

X



k =0

n�


k =0

X




[f (B (tk +



B (tk ) [B (tk +



))]



k =0

n�


k =0

X



)) f (B (tk

 


(B (tk



)] f



0



(B (tk



)) +




[B (tk +



) B (tk

 


)]



))



f



00




[B (tk + ) B (tk

   


n�


k =0

X



) B (tk )] +

 


n�


k =0

X




[B (tk + ) B (tk

   


)]



:



k =0


CHAPTER 15. Itˆo’s Formula 169



We let - 0 to obtain
jj jj!

f (B (T ))       - f (B (0)) =


=



0

Z


0

Z



T


T



0



B (u) dB (u) +



hB i(T )

T

T

| {z }



00



T



T



Z



(B (u))



du:



f



(B (u)) dB (u) +



f



0



| {z }



This is Itˆo’s formula in integral form for the special case



f (x) =


**15.3** **Geometric Brownian motion**



x



:



**Definition 15.1 (Geometric Brownian Motion)** Geometric Brownian motion is



S (t) = S (0) exp          - B (t) +

n

where - and - - 0 are constant.


Define




 - 







;




 - 




 

t

 










;



so


Then



f (t; x) = S (0) exp - x +

n


S (t) = f (t; B (t)):




 - 



= 


t

 

f :



ft



=







f ; fx




= - f ; fxx



According to Itˆo’s formula,



dS (t) = df (t; B (t))



= ft



dt + fx dB +



fxx



dB dB


dt

|dB{z+}



dt



= (� 






)f dt + - f dB +







f dt



= �S (t)dt + - S (t) dB (t)



Thus, _Geometric Brownian motion in differential form_ is


dS (t) = �S (t)dt +         - S (t) dB (t);


and _Geometric Brownian motion in integral form_ is



�S (u) du +

0

Z



t



S (t) = S (0) +



t


0

Z




- S (u) dB (u):


170


**15.4** **Quadratic variation of geometric Brownian motion**


In the integral form of Geometric Brownian motion,



S (t) = S (0) +



t


0

Z



�S (u) du +



t


0

Z




- S (u) dB (u);



the Riemann integral


is differentiable with F 0



t



F (t) =



Z



�S (u) du



0



(t) = �S (t) . This term has zero quadratic variation. The Itˆo integral



G(t) =



t


0

Z



is not differentiable. It has quadratic variation


hGi(t) =



Z



0




- S (u) dB (u)


t







S



(u) du:



Thus the quadratic variation of S is given by the quadratic variation of G . In differential notation,
we write



dS (t) dS (t) = (�S (t)dt + - S (t)dB (t))



= 


S



(t) dt



**15.5** **Volatility of Geometric Brownian motion**



Fix 0 T T [.] [Let] - = t0 ; : : : ; tn be a partition of [T ; T ] . The _squared absolute sample_

  -  - f g

_volatility_ of S on [T ; T ] is



Fix 0 T

  



- T




[.] [Let]   - = t
f



; T



n



be a partition of [T
g



; T



; : : : ; t



0



] is



) S (tk )]

 


'



T



S



(u) du



n�


k =0

X




[S (tk +







T




- T




- T



' 


T

TZ


)



S



(T



As T T [,] [the] [above] [approximation becomes] [exact.] [In] [other] [words,] [the] _[ instantaneous relative]_

#

_volatility_ of S is - . This is usually called simply the _volatility_ of S .



As T



# T



. This is usually called simply the _volatility_ of S .



**15.6** **First derivation of the Black-Scholes formula**


**Wealth** **of** **an investor.** An investor begins with nonrandom initial wealth X0 [and] [at] [each] [time] t,

holds �(t) shares of stock. Stock is modelled by a geometric Brownian motion:


dS (t) = �S (t)dt +            - S (t)dB (t):


CHAPTER 15. Itˆo’s Formula 171


�(t) can be random, but must be adapted. The investor finances his investing by borrowing or
lending at interest rate r .

Let X (t) denote the wealth of the investor at time t . Then



dX (t) = �(t)dS (t) + r [X (t) - �(t)S (t)] dt



= �(t) [�S (t)dt + - S (t)dB (t)] + r [X (t) - �(t)S (t)] dt



= r X (t)dt + �(t)S (t) (� - r )



dt + �(t)S (t)�dB (t):



Risk premium | {z }



**Value of an option.** Consider an European option which pays g (S (T )) at time T . Let v (t; x) denote
the value of this option at time t if the stock price is S (t) = x . In other words, the value of the
option at each time t [0; T ] is



v (t; S (t)):



The differential of this value is


dv (t; S (t)) = vt



dt + vx


dt + vx



dS +



vxx dS dS



= vt




[�S dt + - S dB ] +



vxx







S


dB



dt



=



h



vt



+



+ �S vx







S



vxx



i



dt + - S vx



A hedging portfolio starts with some initial wealth X



A hedging portfolio starts with some initial wealth X0 [and invests so that the wealth] X (t) at each

time tracks v (t; S (t)) . We saw above that



dX (t) = [r X + �(� - r )S ] dt + - S �dB :



To ensure that X (t) = v (t; S (t)) for all t, we equate coefficients in their differentials. Equating the



dB coefficients, we obtain the - _-hedging rule_ :



�(t) = vx (t; S (t)):



Equating the dt coefficients, we obtain:



vt + �S vx



+







S



vxx



= r X + �(� - r )S:



But we have set - = v



But we have set - = vx [, and we are seeking to cause] X to agree with v . Making these substitutions,

we obtain



+



vt



+ �S vx







S



vxx



= r v + vx



(where v = v (t; S (t)) and S = S (t) ) which simplifies to



(� - r )S;



+



vt



+ r S vx







S



vxx = r v :



In conclusion, we should let v be the solution to the _Black-Scholes partial differential equation_



vt



(t; x) + r xvx (t; x) +







x



vxx (t; x) = r v (t; x)



satisfying the terminal condition



v (T ; x) = g (x):



If an investor starts with X



(t; S (t)), then he will have



0



= v (0; S (0)) and uses the hedge �(t) = v



X (t) = v (t; S (t)) for all t, and in particular, X (T ) = g (S (T )) .



x


172


**15.7** **Mean and variance of the Cox-Ingersoll-Ross process**


The _Cox-Ingersoll-Ross_ model for interest rates is



q



dr (t) = a(b - cr (t))dt + 


r (t) dB (t);



where a; b; c; - and r (0) are positive constants. In integral form, this equation is



t


0

Z



q



r (t) = r (0) + a



Z



t

0 (b - cr (u)) du + 


r (u) dB (u):



We apply Itˆo’s formula to compute dr



(t) . This is df (r (t)), where f (x) = x



. We obtain



dr



(t) = df (r (t))



f 00



= f



0 (r (t)) dr (t) +



(r (t)) dr (t) dr (t)



r (t) dB (t)

q 


r (t) dB (t)

     


a(b - cr (t)) dt + 



= r (t)



a(b - cr (t)) dt + 



+



= abr (t) dt - acr



(t) dt + - r



q



(t) dB (t) + 


r (t) dt



= (ab + 


)r (t) dt - acr



(t) dt + - r



(t) dB (t)



**The mean of** r (t) **.** The integral form of the CIR equation is



Z



0



q



t



r (t) = r (0) + a



Z



t

0 (b - cr (u)) du + 


r (u) dB (u):



Taking expectations and remembering that the expectation of an Itˆo integral is zero, we obtain



t



IE r (t) = r (0) + a



0

Z



Z



(b - cIE r (u)) du:



Differentiation yields


which implies that


d

dt

Integration yields


We solve for IE r (t) :



d

dt


eact



IE r (t)

i



= eact



IE r (t) = a(b - cIE r (t)) = ab - acIE r (t);



IE r (t)

   


d

dt



h


e



IE r (t) - r (0) = ab



acIE r (t) +




= eact ab:



eacu



t



act



0

Z



Z



du =



b

c




- ):



(eact







r (0) 


IE r (t) =



b

c



+ e�act



b

c







:



If r (0) =



cb [, then] IE r (t) =



bc [for every] t . If r (0) =



cb [, then] r (t) exhibits _mean reversion_ :



b



lim

t!



IE r (t) =



b

c



:


CHAPTER 15. Itˆo’s Formula 173



**Variance of** r (t) . The integral form of the equation derived earlier for dr



(t) is



t



t



(0) + (ab + 


)



0

Z



Z



r (u) du - ac



0

Z



Z



r



(t) = r



r



t

(u) du + 
0

Z



r



(u) dB (u):



Taking expectations, we obtain



t



t



(0) + (ab + 


)



0

Z



Z



IE r (u) du - ac



0

Z



Z



IE r



(t) = r



IE r



(u) du:



Differentiation yields


which implies that



d

IE r

dt



(t) = (ab + 


)IE r (t) - acIE r



(t);



d

dt



(t)

 


)IE r (t):



e act



IE r



(t) +



d

IE r

dt



(t) = e act



acIE r


(ab + 


= e act



Using the formula already derived for IE r (t) and integrating the last equation, after considerable
algebra we obtain



b

c



b

c









ac



b�

ac



+



b

c



+



r (0)  







+



!



e�act



IE r



(t) =





ac



b

c





- r (0)

  


+ r (0) 
 


b

c

 


e� act





ac



b

c




e� act



:



var r (t) = IE r



(t) - (IE r (t))




- r (0) e� act

  



- e�act

ac







r (0) 


b

c







+



+



ac



=



b�

ac



+



:



**15.8** **Multidimensional Brownian Motion**


**Definition 15.2 (** d **-dimensional Brownian Motion)** A d _-dimensional Brownian_ _Motion_ is a process



B (t) = (B



(t); : : : ; Bd



(t); : : : ; B



(t))



with the following properties:



Each B




k



(t) is a one-dimensional Brownian motion;



If i = j, then the processes Bi




(t) are independent.



i



(t) and B



j



Associated with a d -dimensional Brownian motion, we have a filtration (t) such that
fF g



For each t, the random vector B (t) is (t) -measurable;

- F



For each t t

- 



- : : : - t



n [, the vector increments]



B (t



) B (t); : : : ; B (tn

 


) - B (tn�



)



are independent of (t) .
F


174


**15.9** **Cross-variations of Brownian motions**



Because each component B


However, we have:


**Theorem 9.49** _If_ i = j _,_



i [is a one-dimensional Brownian motion, we have the informal equation]



dBi


dBi



i



(t) dBi



(t) dBj



(t) = dt:



(t) = 0



**Proof:** Let - = t0 ; : : : ; tn be a partition of [0; T ] . For i = j, define the _sample cross variation_
f g

of Bi [and] Bj [on] [0; T ] to be



**Proof:** Let - = t
f



; : : : ; t



n



i [and] B



j [on] [0; T ] to be



0



) Bi

 


(tk



)] [Bj



(tk +



) Bj

 


(tk



)] :



n�


k =0

X




[Bi



(tk +



C�



=



k =0



The increments appearing on the right-hand side of the above equation are all independent of one
another and all have mean zero. Therefore,



IE C�



= 0:



We compute var(C�



) . First note that



Bj

 


i (tk



)

 


(tk +



) Bj

 


(tk



)

 


n�


k =0

X



Bi




(tk +



C�



=



) Bi

 


+



k =0

n�


`<k

X




[Bi



(t`+



) Bi

 


(t`



)] [Bj



(t`+



) Bj

 


(t`



)] : [Bi



i (tk +



) Bi

 


(tk



)] [Bj



(tk +



) Bj

 


(tk



)]



`<k



All the increments appearing in the sum of cross terms are independent of one another and have
mean zero. Therefore,



var(C� ) = IE C�



= IE



n�


k =0

X




[Bi



(tk +



) Bi

 


(tk



)]




[Bj (tk +



) Bj

 


(tk



)]



:



k =0



But [Bi (tk + ) Bi (tk )] and [Bj (tk + ) Bj (tk )] are independent of one another, and each has

    -     
expectation (tk + tk ) . It follows that



But [Bi



(t



k



)]



) . It follows that



j



i



k +



) Bi

 


i



(t



k



and [B



(t



k +



j



(t



k



)]



) - B



k +




- t



var(C�



) =



n�


k =0

X



(tk +



tk )





- jj�jj



n�



k =0

X



k =0



(t



k +



) = jj�jj:T :



tk




k =0



As - 0, we have var(C
jj jj!



) 0, so C
!












- [converges to the constant] IE C



= 0 .


CHAPTER 15. Itˆo’s Formula 175


**15.10** **Multi-dimensional Itˆo formula**


To keep the notation as simple as possible, we write the Itˆo formula for _two_ processes driven by a
_two_ -dimensional Brownian motion. The formula generalizes to _any number_ of processes driven by
a Brownian motion of _any number_ (not necessarily the same number) of dimensions.

Let X and Y be processes of the form



�(u) du +


- (u) du +



0

t



Z

Z









t



X (t) = X (0) +


Y (t) = Y (0) +



t


0

t



Z



Z



t


0

t



(u) +


(u) +



Z

Z



(u);


(u):



(u) dB


(u) dB



(u) dB


(u) dB









0



0



0



Such processes, consisting of a nonrandom initial condition, plus a Riemann integral, plus one or
more Itˆo integrals, are called _semimartingales_ . The integrands �(u); - (u); and �ij (u) can be any



more Itˆo integrals, are called _semimartingales_ . The integrands �(u); - (u); and �ij (u) can be any

adapted processes. The adaptedness of the integrands guarantees that X and Y are also adapted. In
differential notation, we write



ij



dX = - dt + 

d Y = - dt + 


dB


dB



+ 

+ 


dB


dB



;


:



Given these two semimartingales X and Y, the quadratic and cross variations are:



dX dX = (� dt + 


+�



dB



+ 


= 

= (�



dt

|+ �{z ) }



+ 


dB



dB



dB



+�







dB


dB



) ;


dB



dB



dt

| {z }



dt



)



dt;



0

| {z }



d Y d Y = (� dt + 


+ 

+ 

) dt



dB


dB



)


)(� dt + 


dB



= (�



+ 


)



dB


dt;


dB


 


dX d Y = (� dt + 


+ 


dB



)



= (�







+ 


Let f (t; x; y ) be a function of three variables, and let X (t) and Y (t) be semimartingales. Then we
have the corresponding Itˆo formula:



df (t; x; y ) = ft



dt + fx



dX + fy d Y +




[fxx



dX dX + fxy



dX d Y + fy y



d Y d Y ] :



In integral form, with X and Y as decribed earlier and with all the variables filled in, this equation
is



f (t; X (t); Y (t)) - f (0; X (0); Y (0))



t



Z




[�



=



0

Z

+



+ �fx



+ - fy



+



(�



+ 


)fxx



+ (�



+



(�



+ 


)fy y



] du



+ 

] dB






;



)fxy



0




[ft


t


0



fx



fy ] dB



+



Z



t


0




[�



fx






fy



+ 


+ 


where f = f (u; X (u); Y (u), for i; j ;, f g



= Bi



(u), and Bi



(u) .



ij



= �ij


176


### **Chapter 16**

# **Markov processes and the Kolmogorov** **equations**

**16.1** **Stochastic Differential Equations**


Consider the _stochastic differential equation_ :


dX (t) = a(t; X (t)) dt +         - (t; X (t)) dB (t): (SDE)


Here a(t; x) and - (t; x) are given functions, usually assumed to be continuous in (t; x) and Lipschitz continuous in x,i.e., there is a constant L such that



for all t; x; y .



ja(t; x) - a(t; y )j - Ljx - y j; j� (t; x) - - (t; y )j - Ljx - y j



0



Let (t



0



; x) be given. A _solution_ to (SDE) with the _initial condition_ (t



; x) is a process X (t)
f g



t�t



satisfying 0 0 0



X (t0



) = x;



t



t



tZ



X (t) = X (t0 ) +



a(s; X (s)) ds +



tZ



t




- (s; X (s)) dB (s); t t0

       


0



t



0



The solution process X (t) t t0 [will be adapted to the filtration] (t) t 0 [generated by the Brow-]
f g         - fF g         
nian motion. If you know the path of the Brownian motion up to time t, then you can evaluate



The solution process X (t)
f g



0 [will be adapted to the filtration] (t)
fF g



t�t



X (t) .



**Example 16.1 (Drifted Brownian motion)** Let a be a constant and - =, so


dX (t) = a dt + dB (t):



If (t



0



; x) is given and we start with the initial condition



X (t0



) = x;



177


178


then



X (t) = x + a(t - t0



) + (B (t) - B (t0



)); t - t0



:



To compute the differential w.r.t. t, treat t



0 [and] B (t



0



) as constants:



dX (t) = a dt + dB (t):


**Example 16.2 (Geometric Brownian motion)** Let r and - be constants. Consider


dX (t) = r X (t) dt +           - X (t) dB (t):


Given the initial condition



X (t0



) = x;



the solution is



0 [and] B (t



)(t - t0



)

 


:



X (t) = x exp



�t




 - (B (t) - B (t0



)) + (r 






Again, to compute the differential w.r.t. t, treat t



0 ) as constants:



dX (t) = (r 






)X (t) dt + - X (t) dB (t) +







X (t) dt



= r X (t) dt + - X (t) dB (t):



**16.2** **Markov Property**



Let 0 t

  


0



< t [be given and let] h(y ) be a function. Denote by



IE t0



;x h(X (t



))



the expectation of h(X (t )), given that X (t0 ) = x . Now let - IR be given, and start with initial

condition



the expectation of h(X (t



)), given that X (t



0



X (0) = - :



We have the _Markov property_



















h(X (t




))



;X (t0



) h(X (t



)):



F (t



= IE t0



IE



0;�



0 )

 


In other words, if you observe the path of the driving Brownian motion from time 0 to time t



In other words, if you observe the path of the driving Brownian motion from time 0 to time t0 [, and]

based on this information, you want to estimate h(X (t )), the only relevant information is the value



based on this information, you want to estimate h(X (t )), the only relevant information is the value

of X (t0 ) . You imagine starting the (S D E ) at time t0 [at] [value] X (t0 ), and compute the expected



of X (t0 ) . You imagine starting the (S D E ) at time t0 [at] [value] X (t0 ), and compute the expected

value of h(X (t )) .



0



0



) . You imagine starting the (S D E ) at time t



)) .



0 [at] [value] X (t


CHAPTER 16. Markov processes and the Kolmogorov equations 179


**16.3** **Transition density**


Denote by



p(t0 ; t



; x; y )



the density (in the y variable) of X (t



), conditioned on X (t



0



t0



h(X (t



)) =

IR

Z



h(y )p(t0 ; t



) = x . In other words,


; x; y ) dy :



IE



;x



The Markov property says that for 0 t0

          


t [and for every]   -,




















IE 0;�



h(X (t




))



(t0
F



=



IR

Z



h(y )p(t0



; X (t0 ); y ) dy :



; t



)

 


**Example 16.3 (Drifted Brownian motion)** Consider the SDE



dX (t) = a dt + dB (t):



Conditioned on X (t



) is normal with mean x + a(t




- t0



) and variance



) = x, the random variable X (t



0



(t




- t0



), i.e.,




- t







:



p(t0 ; t



; x; y ) =



p




 - (t




 



(y - (x + a(t



(t



0 )))




- t



0




- t



0



)



exp



)



Note that p depends on t



Note that p depends on t0 [and] t [only through their difference] t t0 [.] [This is always the case when] a(t; x)

                 
and - (t; x) don’t depend on t .



0 [and] t




[only through their difference] t




- t



**Example 16.4 (Geometric Brownian motion)** Recall that the solution to the SDE


dX (t) = r X (t) dt +           - X (t) dB (t);



with initial condition X (t



0 ) = x, is Geometric Brownian motion:



X (t



) = x exp








- (B (t



) - B (t0 )) + (r 






)(t


(t



)

 


)



:



The random variable B (t



) - B (t0



) has density



IP fB (t



) - B (t0



) dbg =




  - (t

p




- t0



)



exp







db;




 



and we are making the change of variable


y = x exp


or equivalently,




 - b + (r 




 





- t0


b

- t0


:



)(t


)(t




- t0




- t0



)

 



- (r 


y

x



:


dy

- y



b =







)

i



log

h



The derivative is



dy

db



= - y ; or equivalently, db =


180


Therefore,



p(t0



; t



; x; y ) dy = IP fX (t



) dy g




- (r 










)(t




- t0



)



i



y

x



=




- y











(t



dy :




- t



0



)�



h



log



p




 - (t




- t



0



)



exp



Using the transition density and a fair amount of calculus, one can compute the expected payoff from a
European call:



t;x



=



IE



(X (T ) - K )+



0

Z



(y - K )+ p(t; T ; x; y ) dy



+ r (T - t) +



x

K



= er (T �t)







xN







p







(T - t)







x

K



T - t



log







pT - t



+ r (T - t) 


h



i




- K N







(T - t)



(T - t)

��



i







p



h



log



where


Therefore,



dx =



dx:



x



x



N (� ) =



p 


p 


p



Z




 

�



e�



��

Z


+



e�







e




�r (T �t)



(X (T ) - K )+

















t;X (t)



F (t)

  


IE



0;�



(X (T ) - K )



= e�r (T �t)



= X (t)N



IE



pT - t



+ r (T - t) +






 










X (t)

K



log




- e�r (T �t) K N












(T - t)

��



p



T - t



X (t)

log

K




+ r (T - t) 






**16.4** **The Kolmogorov Backward Equation**


Consider

dX (t) = a(t; X (t)) dt +         - (t; X (t)) dB (t);



and let p(t



; t


@



; x; y ) be the transition density. Then the Kolmogorov Backward Equation is:



p(t0



0







; x)



@

@ x



p(t0



@

@ x



p(t0 ; t



; x; y ):
(KBE)



; x; y ) = a(t0



; t



; x; y ) +







(t0



; x)



@ t0



; t



The variables t0 [and] x in (K B E ) are called the _backward variables_ .



In the case that a and - are functions of x alone, p(t



In the case that a and - are functions of x alone, p(t0 ; t ; x; y ) depends on t0 [and] t [only through]

their difference - = t t0 [.] [We] [then] [write] p(� ; x; y ) rather than p(t0 ; t ; x; y ), and (K B E )



0



; t



; x; y ) depends on t



their difference - = t t0 [.] [We] [then] [write] p(� ; x; y ) rather than p(t0 ; t ; x; y ), and (K B E )

       
becomes



0 [.] [We] [then] [write] p(� ; x; y ) rather than p(t



0



0 [and] t




- t



; t



@

@ 


@

@ x



p(� ; x; y ) = a(x)



p(� ; x; y ) +



@

@ x



p(� ; x; y ): (KBE’)







(x)


CHAPTER 16. Markov processes and the Kolmogorov equations 181


**Example 16.5 (Drifted Brownian motion)**


dX (t) = a dt + dB (t)











p(� ; x; y ) =



p - 






exp







(y - (x + a� ))

    


(y - (x + a� ))



:



(y - x - a� )

    


(y - x - a� )



@


@ 

@

@ x







@

@ 

+




 


p = p�







(y - x - a� )



p




@

@ x




@

@ 




p - 


p



y - x - a�

   


exp



p +




 


(y - x - a� )




 


a(y - x - a� )

    


(y - x - a� )








p








 - 










exp










+












 


p:



p = px



=


=


=


=



y - x - a�




 


p:







p = pxx



y x a�

 - - px

   


(y - x - a� )







(y - x - a� )

   


=

 - 


p +



Therefore,



@


@ x


apx



p


 










)�



+



pxx



=







a(y - x - a� )

   


a(y - x - a� )




 


p:


+



= p







:



This is the Kolmogorov backward equation.


**Example 16.6 (Geometric Brownian motion)**


dX (t) = r X (t) dt +           - X (t) dB (t):




- (r 


y

x







p(� ; x; y ) =




- y p



i



:




 - 











 -  


exp



It is true but very tedious to verify that p satisfies the KBE



log

h



p�



= r xpx



x



pxx :



+







**16.5** **Connection between stochastic calculus and KBE**


Consider


dX (t) = a(X (t)) dt +         - (X (t)) dB (t): (5.1)


Let h(y ) be a function, and define



t;x



v (t; x) = IE



h(X (T ));


182


where 0 t T . Then

   -   


v (t; x) =



Z



h(y ) p(T - t; x; y ) dy ;



vt (t; x) =

   


Z



h(y ) p�



(T - t; x; y ) dy ;



(t; x) =


(t; x) =



Z

Z



h(y ) px



h(y ) pxx (T t; x; y ) dy :

    


(T - t; x; y ) dy ;



vx



vxx



Therefore, the Kolmogorov backward equation implies



vt



(t; x) + a(x)vx (t; x) +







(x)vxx (t; x) =



Z



�p

h



h



(T - t; x; y )

i



dy = 0



h(y )







(T t; x; y ) + a(x)px (T t; x; y ) +

 -  



- (x)pxx



Let (0; - ) be an initial condition for the SDE (5.1). We simplify notation by writing IE rather than



0;�
.



IE



**Theorem 5.50** _Starting at_ X (0) = - _, the process_ v (t; X (t)) _satisfies the martingale property:_





















= v (s; X (s)); 0 - s - t - T :



IE







v (t; X (t))



F (s)







**Proof:** According to the Markov property,







IE h(X (T ))

 


F (t)



= IE t;X (t)h(X (T )) = v (t; X (t));







so






















IE

 






















F (s)

  


IE [v (t; X (t))jF (s)] = IE


= IE


= IE



h(X (T ))



F (t)















h(X (T ))



F (s)







�)







s;X (s)



h(X (T )) (Markov property)











= v (s; X (s)):







Itˆo’s formula implies



dv (t; X (t)) = vt dt + vx



dX +



vxx



dX dX



= vt



dt + avx



dt + - vx



dB +







vxx dt:


CHAPTER 16. Markov processes and the Kolmogorov equations 183


In integral form, we have


v (t; X (t)) = v (0; X (0))



+


+



Z

Z




- (X (u))vx(u; X (u)) dB (u):



(u; X (u))

i



(u; X (u)) + a(X (u))vx



(u; X (u)) +







(X (u))vxx



du



0



t


t



vt

h



0



We know that v (t; X (t)) is a martingale, so the integral



t

We know that v (t; X (t)) is a martingale, so the integral 0 vt + avx + - vxx du must be zero

for all t . This implies that the integrand is zero; hence R h i



R



t


0



t



h



v



v



xx



+ av



x



+







i



+



vt



+ avx







vxx



= 0:



Thus by two different arguments, one based on the Kolmogorov backward equation, and the other
based on Itˆo’s formula, we have come to the same conclusion.


**Theorem 5.51 (Feynman-Kac)** _Define_



v (t; x) = IE



t;x h(X (T )); 0 - t - T ;



_where_


_Then_


_and_



dX (t) = a(X (t)) dt + - (X (t)) dB (t):



vt (t; x) + a(x)vx (t; x) +



(t; x) = 0 (FK)







(x)vxx



v (T ; x) = h(x):


The Black-Scholes equation is a special case of this theorem, as we show in the next section.


**Remark 16.1 (Derivation of KBE)** We plunked down the Kolmogorov backward equation without any justification. In fact, one can use Itˆo’s formula to prove the Feynman-Kac Theorem, and use
the Feynman-Kac Theorem to derive the Kolmogorov backward equation.


**16.6** **Black-Scholes**


Consider the SDE

dS (t) = r S (t) dt +            - S (t) dB (t):

With initial condition

S (t) = x;

the solution is



S (u) = x exp - (B (u) - B (t)) + (r 
n







)(u - t)

   


; u - t:


184


Define



t;x



v (t; x) = IE



h(S (T ))



= IE h







x exp



n




- (B (T ) - B (t)) + (r 






)(T - t)

o�



;



where h is a function to be specified later.



Recall the _Independence Lemma_ : If is a - -field, X is -measurable, and Y is independent of,
G G G
then



G

 


IE



h(X ; Y )





 



 



 


= - (X );



where




 



         - (x) = IE h(x; Y ):


With geometric Brownian motion, for 0 t T, we have

           -           


exp







S (t) = S (0) exp


S (T ) = S (0) exp


= S (t)



n

n




- B (t) + (r 


)t



)T







;








- B (T ) + (r 





 



- (B (T ) - B (t)) + (r 


)(T - t)







n



We thus have


where


Now



F (t) -measurable

| {z }


S (T ) = X Y ;


X = S (t)



independentof F (t)
| {z }



Y = exp




 - (B (T ) - B (t)) + (r 
n







)(T - t)

   


:



IE h(xY ) = v (t; x):


The independence lemma implies



= IE [h(X Y )jF (t)]

= v (t; X )


= v (t; S (t)):



IE



h(S (T ))












F (t)














CHAPTER 16. Markov processes and the Kolmogorov equations 185


We have shown that



v (t; S (t)) = IE



h(S (T ))





 



 



 


F (t)



; 0 - t - T :




 






Note that the random variable h(S (T )) whose conditional expectation is being computed does not
depend on t . Because of this, the tower property implies that v (t; S (t)); 0 t T, is a martingale:

                   -                    For 0 s t T,

  -  -  


















= IE


= IE




 
 



 


h(S (T ))



F (s)















F (s)

  


IE







v (t; S (t))



F (s)







h(S (T ))



F (t)



IE












- 
  










�)







= v (s; S (s)):




 



 



 


This is a special case of Theorem 5.51.

Because v (t; S (t)) is a martingale, the sum of the dt terms in dv (t; S (t)) must be 0. By Itˆo’s
formula,



h



x



dv (t; S (t)) =



vt



(t; S (t)) dt + r S (t)vx



(t; S (t))

i



(t; S (t)) +







S



(t)vxx



dt



+ - S (t)v



(t; S (t)) dB (t):



This leads us to the equation



(t; x) +



vt



(t; x) + r xvx







x



vxx (t; x) = 0; 0 t < T ; x 0:

      -      


This is a special case of Theorem 5.51 (Feynman-Kac).

Along with the above partial differential equation, we have the _terminal condition_


v (T ; x) = h(x); x               - 0:

Furthermore, if S (t) = 0 for some t [0; T ], then also S (T ) = 0 . This gives us the _boundary_
_condition_

v (t; 0) = h(0); 0               - t               - T :

Finally, we shall eventually see that the value at time t of a contingent claim paying h(S (T )) is



u(t; x) = e�r (T �t)

= e�r (T �t)



IE t;x



h(S (T ))



v (t; x)



at time t if S (t) = x . Therefore,


v (t; x) = er (T �t)



u(t; x);



ut



(t; x) = �r e



u(t; x) + er (T �t)



vt


vx



r (T �t)



(t; x);



r (T �t)



ux (t; x);



(t; x) = e



vxx (t; x) = er (T �t)



uxx (t; x):


186


Plugging these formulas into the partial differential equation for v and cancelling the er (T �t) ap
pearing in every term, we obtain the _Black-Scholes partial differential equation_ :



r u(t; x) + ut




(t; x) + r xux



(t; x) +







x



uxx (t; x) = 0; 0 t < T ; x 0:

      -      (BS)



Compare this with the earlier derivation of the Black-Scholes PDE in Section 15.6.

In terms of the transition density




- (T t)�

  



- (r 


)



y

x



p(t; T ; x; y ) =

      - y



p




 - (T - t)



log




)(T - t)

    


exp

(







for geometric Brownian motion (See Example 16.4), we have the “stochastic representation”



u(t; x) = e�r (T �t)


= e�r (T �t)



IE


0

Z



t;x



h(S (T )) (SR)


h(y )p(t; T ; x; y ) dy :



In the case of a call,


and



h(y ) = (y - K )+



+ r (T - t) +



log


 - e



x

K



�r (T �t)



u(t; x) = x N











(T - t)



pT - t







pT - t



��

x



��



log




K



K N











p



(T - t)

��



+ r (T - t) 






Even if h(y ) is some other function (e.g., h(y ) = (K y )+, a put), u(t; x) is still given by and

               
satisfies the Black-Scholes PDE (BS) derived above.


**16.7** **Black-Scholes with price-dependent volatility**


dS (t) = r S (t) dt +            - (S (t)) dB (t);



v (t; x) = e�r (T �t) IE


The Feynman-Kac Theorem now implies that



t;x (S (T ) - K )+



:



r v (t; x) + vt (t; x) + r xv




x (t; x) +







(x)vxx (t; x) = 0; 0 t < T ; x - 0:

       


v also satisfies the _terminal condition_


v (T ; x) = (x              - K )+ ; x              - 0;


CHAPTER 16. Markov processes and the Kolmogorov equations 187


and the _boundary condition_

v (t; 0) = 0; 0               - t               - T :

An example of such a process is the following from J.C. Cox, _Notes on options pricing I: Constant_
_elasticity of variance diffusions,_ Working Paper, Stanford University, 1975:



(t) dB (t);



dS (t) = r S (t) dt + - S







where 0 - - < . The “volatility” - S - - (t) decreases with increasing stock price. The corre
sponding Black-Scholes equation is



where 0 - < . The “volatility” - S

   



- 


vxx



r v + vt




+ r xv



x



v (t; 0) = 0; 0 - t - T



x 


= 0; 0 - t < T x - 0;



+







+



; x - 0:



v (T ; x) = (x - K )


188


### **Chapter 17**

# **Girsanov’s theorem and the risk-neutral** **measure**

(Please see Oksendal, 4th ed., pp 145–151.)


**Theorem 0.52 (Girsanov, One-dimensional)** _Let_ B (t); 0 t T _,_ _be_ _a_ _Brownian_ _motion_ _on_

                -                _a_ _probability_ _space_ (�; F ; P) _._ _Let_ F (t); 0 - t - T _,_ _be_ _the_ _accompanying_ _filtration,_ _and_ _let_

- (t); 0 - t - T _, be a process adapted to this filtration. For_ 0 - t - T _, define_



t



B (t) =



0

Z



Z




- (u) du + B (t);



e







t



Z (t) = exp



t

 - 0

- Z




- (u) dB (u) 


0

Z



(u) du

  


;



_and define a new probability measure by_



IP (A) =



Z (T ) dIP ; A F :



A

Z



_Under_



IP _, the process_



f



B (t); 0 - t - T _, is a Brownian motion._



e



f



**Caveat:** This theorem requires a technical condition on the size of - . If



IE exp

(



T


0

Z




 




(u) du

)



(t)Z (t) dB (t) dB (t) 


< ;







everything is OK.

We make the following remarks:


Z (t) **is a matingale.** In fact,


dZ (t) = �� (t)Z (t) dB (t) +

= �� (t)Z (t) dB (t):



(t)Z (t) dt



189


190



IP **is a probability measure.** Since Z (0) =, we have IE Z (t) = for every t 0 . In particular

                     


f



IP (�) =



Z



Z (T ) dIP = IE Z (T ) = ;







so



IP is a probability measure.



f



f



IP . If X is a random variable, then




[Z

f



IE **in terms of** IE **.** Let



IE denote expectation under



f



f



=

f



IE Z = IE [Z (T )X ] :



A [, where] A . We have
F



To see this, consider first the case X =



IE X =



IP (A) =



f



Z



Z (T ) dIP =



Z



Z (T ) A



Z (T )



dIP = IE [Z (T )X ] :



f



A







Now use Williams’ “standard machine”.



IP **and** IP **.** The intuition behind the formula



f



IP (A) =



Z (T ) dIP A F



is that we want to have



IP (A) =

f



A

Z



IP (! ) = Z (T ; !)IP (! );



but since IP (! ) = 0 and IP (! ) = 0, this doesn’t really tell us anything useful about IP . Thus,

we consider subsets of -, rather than individual elements of - .



but since IP (! ) = 0 and



IP (! ) = 0, this doesn’t really tell us anything useful about



f



f



0

f



**Distribution of**



B (T ) **.** If - is constant, then



e



Z (T ) = exp



�� B (T ) 






T

 


B (T ) = - T + B (T ):



e



n



Under IP, B (T ) is normal with mean 0 and variance T, so B (T ) is normal with mean - T and

variance T :



Under IP, B (T ) is normal with mean 0 and variance T, so



e



)



(



IP (



B (T ) d



p - T



exp







(



~



b - - T )



T



~



b) =



IP removes the drift from



d~b:



B (T ) **.** The change of measure from IP to IP removes the drift from B (T ) .

To see this, we compute



e



**Removal of Drift from**



B (T ) **.** The change of measure from IP to



e



e



B (T ) = IE [Z (T )(� T + B (T ))]



f



IE

f



IE



e



n



(� T + B (T ))

i



(�



= IE



h



exp



�� B (T ) 






T

 


)



Z

Z

Z



�


�


�



(



b

T



=


=


(y = - T + b) =



p - T


p - T


p - T



(� T + b) expf�� b 


y exp







T g exp



db



(�



)



(� T + b) exp



(b + - T )

T



db



)



dy (Substitute y = - T + b )







y



= 0:


CHAPTER 17. Girsanov’s theorem and the risk-neutral measure 191



We can also see that



IE

f



B (T ) = 0 by arguing directly from the density formula



e



~b



d~b:


T g



)





e



=







p - T



exp



(







(



T



~



b - - T )



IP



n



B (t) d



Because


we have



Z (T ) = expf�� B (T ) 






T g



= expf�� (



B (T ) - - T ) 


(

e



= expf��



B (T ) +



e



T g;







e



= IP

n



T



B (T ) d









(



��



~b +



IP

f



IP



n



B (T ) d



exp







T

 
 


~b



=


=



exp


exp



~



b



n




- �~b +



e



p


p




 - T


 - T



(

(









T



~



b - - T )



)



d~b:



T



~b



)



d~b:



Under



Under IP, B (T ) is normal with _mean zero_ and variance T . Under IP, B (T ) is normal with

_mean_ - T and variance T .



IP,

T

f



B (T ) is normal with _mean zero_ and variance T . Under IP,



e



e



**Means change, variances don’t.** When we use the Girsanov Theorem to change the probability
measure, means change but variances do not. Martingales may be destroyed or created.
Volatilities, quadratic variations and cross variations are unaffected. Check:



= dB :dB = dt:



d



B d



e



B = (� (t) dt + dB (t))



e



**17.1** **Conditional expectations under**



f



IP



**Lemma 1.53** _Let_ 0 t T _._ _If_ X _is_ (t) _-measurable, then_

      -      - F



**Proof:**



IE X = IE [X :Z (t)]:

f



IE X = IE [X :Z (T )] = IE [ IE [X :Z (T )jF (t)] ]



f



= IE [X IE [Z (T )jF (t)] ]



= IE [X :Z (t)]



because Z (t); 0 t T, is a martingale under IP .

     -     

192


**Lemma 1.54 (Baye’s Rule)** _If_ X _is_ (t) _-measurable and_ 0 s t T _, then_
F           -           -           


IE [X jF (s)] =



IE [X Z (t) (s)]: (1.1)

Z (s) jF



**Proof:** It is clear that



Z (s)



f



**Proof:** It is clear that Z (s) IE [X Z (t) (s)] is (s) -measurable. We check the partial averaging

jF F
property. For A (s), we have
F



IE [X Z (t) (s)]] (Lemma 1.53)
jF







A

Z



IE

IfE







A IE [X Z (t) (s)]

Z (s) jF



= IE [



Z (s)



IE [X Z (t)jF (s)] d



IP =



f



A



= IE [IE [



X Z (t) (s)]] (Taking in what is known)
jF



A



= IE [ A



X Z (t)]



=


=



IE [



f



Z



X ] (Lemma 1.53 again)



A



X d



A



IP :

f



Although we have proved Lemmas 1.53 and 1.54, we have not proved Girsanov’s Theorem. We
will not prove it completely, but here is the beginning of the proof.


**Lemma 1.55** _Using the notation of Girsanov’s Theorem, we have the martingale property_



IE [



B (t)jF (s)] =



e



e



B (s); 0 - s - t - T :



**Proof:** We first check that


Therefore,



f



B (t)Z (t) is a martingale under IP . Recall



e



e



B (t) = - (t) dt + dB (t);



d



dZ (t) = �� (t)Z (t) dB (t):



d(



B Z ) =



B dZ + Z d



�e



e



= 


B - Z dB + Z - dt + Z dB - - Z dt



e



B + d



B dZ



e



e



= (�



B - Z + Z ) dB :



e



Next we use Bayes’ Rule. For 0 s t T,

         -         -         


IE [

f



IE [



B (t)jF (s)] =



e



IE [



=


=



e



B (t)Z (t)jF (s)]



Z (s)


Z (s)


B (s):

e



B (s):



B (s)Z (s)



e


CHAPTER 17. Girsanov’s theorem and the risk-neutral measure 193


**Definition 17.1 (Equivalent measures)** Two measures on the same probability space which have
the same measure-zero sets are said to be _equivalent._



The probability measures IP and



IP of the Girsanov Theorem are equivalent. Recall that



f



The probability measures IP and IP of the Girsanov Theorem are equivalent. Recall that IP is

defined by



f



IP (A) =



Z



Z (T ) dIP ; A F :



If IP (A) = 0, then A Z (T ) dIP = 0: Because Z (T ) - 0 for every !, we can invert the definition

of IP to obtain

R



If IP (A) = 0, then



R



A



f



IP to obtain



f



Z (T )



d



IP ; A F :

f



If



IP (A) = 0, then

f



A

R



Z (T )



IP (A) =

A

Z


dIP = 0:



**17.2** **Risk-neutral measure**


As usual we are given the **Brownian motion:** B (t); 0 t T, with filtration (t); 0 t T,
defined on a probability space (�; ; P) . We can then define the following. - - F - F

**Stock price:**


dS (t) = �(t)S (t) dt +           - (t)S (t) dB (t):


The processes �(t) and - (t) are adapted to the filtration. The stock price model is completely
general, subject only to the condition that the paths of the process are continuous.

**Interest rate:** r (t); 0 t T . The process r (t) is adapted.

      -      
**Wealth** **of** **an** **agent,** starting with X (0) = x . We can write the wealth process differential in
several ways:



dX (t) = �(t) dS (t)



+ r (t)[X (t) - �(t)S (t)] dt



Capital gains from Stock

r (t)|X (t{z) dt +} �(



Interest earnings

dS| (t) r S ({zt) dt] }



= r (t)X (t) dt + �(t)[dS (t) - r S (t) dt]



= r (t)X (t) dt + �(t) (�(t) - r (t))



S (t) dt + �(t)� (t)S (t) dB (t)



| Risk premium {z }



= r (t)X (t) dt + �(t)� (t)S (t)



�(t) - r (t)

  - (t)



dt + dB (t)



Market price of risk= | {z } - (t)


194


**Discounted processes:**







R


0

R



r (u) du [�r (t)S (t) dt + dS (t)]

r (u) du [�r (t)X (t) dt + dX (t)]



t



r (u) du








= e�



d



e







R



0



S (t)







X (t)



t


0



r (u) du



t


0


t


0



= e�



d



e







R



S (t)

  


R



t


0



r (u) du



:



= �(t)d



e








**Notation:**



r (u) du ;



t


0



;




- (t) = e

R



t



r (u) du




- (t)



= e�



0







R



d� (t) = r (t)� (t) dt; d


The discounted formulas are




 - (t)




= 


r (t)

- (t)



dt:



=


=


=







�(t)

- (t)




[ r (t)S (t) dt + dS (t)]

- (t) 

[(�(t) r (t))S (t) dt +   - (t)S (t) dB (t)]

- (t) 

  - (t)S (t) [� (t) dt + dB (t)] ;

- (t)



d



S (t)

- (t)













S (t)

- (t)

  


d



X (t)

- (t)



= �(t) d







=


**Changing the measure.** Define


Then


d




- (t)S (t) [� (t) dt + dB (t)]:



B (t) =

e



t


0

Z




- (u) du + B (t):














- (t)

�(t)

- (t)




- (t)S (t) d




- (t)S (t) d



B (t):



B (t);



e



e



d



S (t)

- (t)

X (t)

- (t)



=


=



Under



IP,



f



S (t)

- (t) [and]



X (t)

 - (t) [are martingales.]



**Definition 17.2 (Risk-neutral measure)** A _risk-neutral_ _measure_ (sometimes called a _martingale_
_measure_ ) is any probability measure, equivalent to the market measure IP, which makes all discounted asset prices martingales.


CHAPTER 17. Girsanov’s theorem and the risk-neutral measure 195


For the market model considered here,



A Z (T ) dIP ; A F ;

Z



where



IP (A) =

f



t


0



Z (t) = exp




 



Z




- (u) dB (u) 


t


0

Z







(u) du

  


;



is the unique risk-neutral measure. Note that because - (t) =

0 .



; we must assume that - (t) =



�(t)�r (t)

 - (t)



�(t)�r (t)



**Risk-neutral valuation.** Consider a contingent claim paying an (T ) -measurable random variable
F

V at time T .


**Example 17.1**



+



V = (S (T ) - K )

V = (K - S (T ))



; European call

; European put



+



V =



T



!+



; Asian call



Z



T


0



S (u) du - K



S (t); Look back



V = max

0�t�T



If there is a hedging portfolio, i.e., a process �(t); 0 t T, whose corresponding wealth process

              -              satisfies X (T ) = V, then



V

:

- (T )

   


X (0) =



IE

f







This is because



X (t)

- (t) [is a martingale under]



IP, so







f



X (T )

- (T )







X (0) =



X (0)

- (0)



=



IE

f



IE

f







=







V

- (T )



:


196


### **Chapter 18**

# **Martingale Representation Theorem**

**18.1** **Martingale Representation Theorem**


See Oksendal, 4th ed., Theorem 4.11, p.50.


**Theorem 1.56** _Let_ B (t) ; 0 t T ; _be a Brownian motion on_ (�; ; P) _._ _Let_ (t); 0 t T _, be_

       -        - F F        -        _the filtration_ generated by this Brownian motion. _Let_ X (t); 0 t T _, be a martingale (under_ IP _)_

                -                 _relative to this filtration. Then there is an adapted process_ - (t); 0 - t - T _, such that_



t



X (t) = X (0) +



Z



0




- (u) dB (u); 0 - t - T :



_In particular, the paths of_ X _are continuous._



**Remark 18.1** We already know that if X (t) is a process satisfying


dX (t) =            - (t) dB (t);


then X (t) is a martingale. Now we see that if X (t) is a martingale adapted to the filtration generated
by the Brownian motion B (t), i.e, the Brownian motion is the only source of randomness in X, then


dX (t) =            - (t) dB (t)


for some - (t) .


**18.2** **A hedging application**



**Homework Problem 4.5.** In the context of Girsanov’s Theorem, suppse that (t); 0 t T ; is
F                      -                      the filtration generated by the Brownian motion B (under IP ). Suppose that Y is a IP -martingale.



the filtration generated by the Brownian motion B (under IP ). Suppose that Y is a IP -martingale.

Then there is an adapted process - (t); 0 t T, such that

           -           - f



e



f



Y (t) = Y (0) +



t


0

Z




- (u) d



B (u); 0 - t - T :



197


198


Then



dS (t) = �(t)S (t) dt + - (t)S (t) dB (t);



t




- (t) = exp







Z



r (u) du



;



0








 - (t) =



�(t) - r (t)




- (t)



;



B (t) =



t


0

Z




- (u) du + B (t);



e







t



Z (t) = exp




 



0

Z




- (u) dB (u) 


t


0

Z



(u) du

  


;



IP (A) =

f



A

Z



Z (T ) dIP ; A F :



e











S (t)

- (t)




- (t) d



B (t):



d



S (t)

- (t)



=



Let �(t); 0 t T ; be a portfolio process. The corresponding wealth process X (t) satisfies

   -    


S (t)

= �(t)� (t)

     - (t)



Z



B (t);

e



d

 


X (t)

- (t)

  

X (t)

 - (t)



B (t);



d



i.e.,



B (u); 0 - t - T :



e



S (u)

- (u)



= X (0) +



t


0



�(u)� (u)



d



Let V be an (T ) -measurable random variable, representing the payoff of a contingent claim at
F
time T . We want to choose X (0) and �(t); 0 t T, so that

            -             


X (T ) = V :



Define the



IP -martingale

f



Y (t) =



IE

f



















V

 - (T )




F (t)

  


; 0 - t - T :



According to Homework Problem 4.5, there is an adapted process - (t); 0 t T, such that

                   -                    


Y (t) = Y (0) +

0

Z



t



e




- (u) d



B (u); 0 - t - T :



Set X (0) = Y (0) =



IE

f



i and choose �(u) so that



V

 - (T )

h



�(u)�(u)



S (u)

- (u)



= - (u):


CHAPTER 18. Martingale Representation Theorem 199


With this choice of �(u); 0 u T, we have

        -        


IE

f



F (t)

  



 



 



 



 


= Y (t) =



IE

f




 


IE



V

- (T )



; 0 - t - T :



In particular,


so



X (t)

 - (t)


X (T )

 - (T )



F (T )

   


V

- (T )



















=




 


V

;

- (T )



IE



=



X (T ) = V :


The Martingale Representation Theorem guarantees the existence of a hedging portfolio, although
it does not tell us how to compute it. It also justifies the risk-neutral pricing formula














)�



)




F (t)



X (t) = - (t)




 


V

- (T )











Z (T )

- (T )




- (t)

Z (t)



IE

- (t)


Z (t)

- (t)



IE

f



IE



V



F (t)




 
































F (t)



; 0 - t - T ;








 - (T )V











where



=


=


- (t) =



t


0

Z



Z



t


0



(r (u) +



= exp




 




- (u) dB (u) 






(u)) du

   


**18.3** d **-dimensional Girsanov Theorem**



**Theorem 3.57 (** d **-dimensional Girsanov)** B (t) = (B

                   


d **-dimensional Girsanov)** B (t) = (B (t); : : : ; Bd (t)); 0 t T _,_ _a_ d _-_

_dimensional Brownian motion on_ (�; F ; P� ) _;_ - 


(t); : : : ; B



d




- F (t); 0 - t - T ; _the accompanying filtration, perhaps larger than the one generated by_ B _;_




- - (t) = (�



(t); : : : ; 


d



(t)); 0 - t - T _,_ d _-dimensional adapted process._



_For_ 0 - t - T ; _define_



t



0

Z



Z



�j (u) du + Bj



(t); j = ; : : : ; d;



B



j



(t) =



e



;



t



Z (t) = exp




 - 0

- Z




- (u): dB (u) 


t


0

Z



jj� (u)jj



du

 


IP (A) =

f



A

Z



Z (T ) dIP :


200


_Then, under_



IP _, the process_



f



B (t) = (



e



d



(t); : : : ;



B



(t)); 0 - t - T ;



B



e



_is a_ d _-dimensional Brownian motion._



B

e



**18.4** d **-dimensional Martingale Representation Theorem**



**Theorem 4.58** B (t) = (B

        


B (t) = (B (t); : : : ; Bd (t)); 0 t T ; _a_ d _-dimensional Brownian motion_

      -      -      
_on_ (�; F ; P) _;_



(t); : : : ; B



d



(t); 0 t T ; _the filtration_ generated by the Brownian motion B _._

- F - 


_If_ X (t); 0 - t - T _,_ _is_ _a_ _martingale_ _(under_ IP _)_ _relative_ _to_ F (t); 0 - t - T _,_ _then_ _there_ _is_ _a_



d _-dimensional adpated process_ - (t) = (�



d



(t); : : : ; 


(t)) _, such that_



Z



X (t) = X (0) +



t


0




- (u): dB (u); 0 - t - T :



**Corollary 4.59** _If we have a_ d _-dimensionaladapted process_ - (t) = (�



**Corollary 4.59** _If we have a_ d _-dimensionaladapted process_ - (t) = (� (t); : : : ; �d (t)); _then we can_

_define_ B ; Z _and_ IP _as in Girsanov’s Theorem. If_ Y (t); 0 t T _, is a martingale under_ IP _relative_



(t); : : : ; 


_define_ B ; Z _and_ IP _as in Girsanov’s Theorem. If_ Y (t); 0 - t - T _, is a martingale under_ IP _relative_

_to_ (t); 0 t T _, then there is a_ d _-dimensional adpated process_ - (t) = (� (t); : : : ; �d (t)) _such_
F e - �f f



B ; Z _and_



IP _as in Girsanov’s Theorem. If_ Y (t); 0 - t - T _, is a martingale under_



f



d



d (

f



d



;

e



_to_ (t); 0 t T _, then there is a_ d _-dimensional adpated process_ - (t) = (� (t); : : : ; �d (t)) _such_
F - 
_that_



(t); : : : ; 


t



Y (t) = Y (0) +



Z




- (u): d



0



B (u); 0 - t - T :



e



**18.5** **Multi-dimensional market model**



Let B (t) = (B



(t); : : : ; B



d



(t)); 0 t T, be a d -dimensional Brownian motion on some

   -   


(�; ; P), and let (t); 0 t T, be the _filtration generated_ _by_ B . Then we can define the
F F  -  following:



**Stocks**



dSi (t) = �i (t)Si


**Accumulation factor**



(t) dt + Si



(t)



d


j =

X



(t); i = ; : : : ; m







ij



(t) dBj



r (u) du

   


t




- (t) = exp



0

�Z



:



Here, �i



(t); �ij



i



(t) and r (t) are adpated processes.


CHAPTER 18. Martingale Representation Theorem 201


**Discounted stock prices**







= (�i



i (t) r (t))

 


dt +



d


j =

X







(t)



(t)



d

 


Si



Si



Si (t)

- (t)



(t)



ij



(t) dBj




- (t)




- (t)



j =

X



d







d



=?



Risk Premium


d

|Si (t) {z }



Si




- (t)



i



(t)



(5.1)



ij



(t) [�



j



(t) + dBj (t)]



j =



j



(t)



For 5.1 to be satisfied, we need to choose 


dBj (t)

| {z }



;Be�j



d



(t); : : : ; 


(t), so that



d


j =

X



(t) = �i (t) r (t); i = ; : : : ; m: (MPR)

   



- ij



(t)�j



**Market** **price** **of** **risk.** The market price of risk is an adapted process - (t) = (�




                                - (t) = (� (t); : : : ; �d (t))

satisfying the system of equations (MPR) above. There are three cases to consider:



(t); : : : ; 


d



**Case I:** (Unique Solution). For Lebesgue-almost every t and IP -almost every !, (MPR) has a
_unique solution_    - (t) . Using    - (t) in the d -dimensional Girsanov Theorem, we define a _unique_
_risk-neutral probability measure_ IP _._ Under IP, every discounted stock price is a martingale.



_risk-neutral probability measure_ IP _._ Under IP, every discounted stock price is a martingale.

Consequently, the discounted wealth process corresponding to any portfolio process is a IP 


IP _._ Under



f



f



f



Consequently, the discounted wealth process corresponding to any portfolio process is a IP 
f f

martingale, and this implies that the market admits no arbitrage. Finally, the Martingale

f

Representation Theorem can be used to show that every contingent claim can be hedged; the
market is said to be _complete_ .



**Case II:** (No solution.) If (MPR) has no solution, then there is _no risk-neutral probability measure_
and the market admits _arbitrage_ .


**Case III:** (Multiple solutions). If (MPR) has multiple solutions, then there are _multiple risk-neutral_
_probability measures_ . The market admits _no arbitrage_, but there are contingent claims which
cannot be hedged; the market is said to be _incomplete._


**Theorem 5.60 (Fundamental Theorem of Asset Pricing)** **Part** **I.** _(Harrison and_ _Pliska,_ _Martin-_
_gales and Stochasticintegrals in the theory of continuous trading,_ Stochastic Proc. and Applications
11 _(1981), pp 215-260.):_
_If a market has a risk-neutral probability measure, then it admits no arbitrage._

**Part II.** _(Harrisonand Pliska, A stochasticcalculus model of continuoustrading: complete markets,_
Stochastic Proc. and Applications _15 (1983), pp 313-316):_
_The risk-neutral measure is unique if and only if every contingent claim can be hedged._


202


### **Chapter 19**

# **A two-dimensional market model**



Let B (t) = (B



(t); B



(t)); 0 t T ; be a two-dimensional Brownian motion on (�; ; P) . Let

  -   - F



(t); 0 t T ; be the filtration generated by B .
F - 


In what follows, all processes can depend on t and !, but are adapted to (t); 0 t T . To
F                      -                      simplify notation, we omit the arguments whenever there is no ambiguity.



**Stocks:**


We assume 



- 0; 

dS


dS


dS




[�


 



dt + 

dt + ��



dS


dS



= S


= S



dB



dB



] ;



q


dt;




- 






dB



:




+


S




- 0; - : Note that

  -  -  


dS


dS


dS



= S


= S


= 

= S








S





S



dB



dB



= 


( - 






S







dB



dB


dB



+ S


dB



= ��



dB



dB



dt;



��



)�


S



dt:



In other words,




[,]

[,]









dS

S


dS

S


dS

S




           
[has instantaneous variance]

           
[has instantaneous variance]




[and]



dS ��

S [have instantaneous covariance]




- [.]



**Accumulation factor:**



�Z



r du

  



             - (t) = exp


The market price of risk equations are



t


0



:




- r

(MPR)

- r









= 

= 


203



q




- 








��







+


204


The solution to these equations is


              

              


=


=



(�




- r










 - r








;




- r ) - ��



(�



r )

- ;







p




- 


provided < - < .

   


Suppose < - < . Then (MPR) has a unique solution (�

   


; 


) ; we define



dB



t



t

 


Z (t) = exp



0

Z



Z



t


0



(�



+ 


) du

  






0

Z







dB







;




 



IP (A) =



A

Z



Z (T ) dIP ; A F :



f



IP is the _unique_ risk-neutral measure. Define



f



B



t


t



Z

Z



Z



0


0



du + B (t);


du + B (t):



(t) =


(t) =









B



Then



e

B

e



;


+



q







h




r dt + 


r dt + ��



dS


dS



= S


= S



d



B




- 


i



de



B

e



d



B



e







:



We have changed the mean rates of return of the stock prices, but not the variances and covariances.




      **19.1** **Hedging when** < - <



dX = 


dS



+ 


dS



+ r (X - 


S




 - 

- r S



S



) dt







=


=


=











(dX - r X dt)









d



X

 



(dS




- r S



dt) +







(dS



dt)



��




d



B




 






S



q




- 


S







d



B



e



e



dB

e







:



+



+







Let V be (T ) -measurable. Define the
F



IP -martingale



f













V











Y (t) =



IE

f








- (T )



F (t)

  


; 0 - t - T :


CHAPTER 19. A two-dimensional market model 205


The Martingale Representation Corollary implies







Z






+



Y (t) = Y (0) +



t


0



d



B



e







dB

e



:



Z







We have


We solve the equations







X







+












 



+


S



d







=



t


0









d



B



S



S



q



d



;



e



d Y = 


B

e



d



B



e



B

e



+ 


d



S - +


 - S

 




q








- 



- 

:


��











S







��


 

= 

= 


for the hedging portfolio (�



; 


) . With this choice of (�



; 


) and setting



X (0) = Y (0) =


we have X (t) = Y (t); 0 t T ; and in particular,

       -       


IE

f



V

;

- (T )



X (T ) = V :


Every (T ) -measurable random variable can be hedged; the market is _complete_ .
F


**19.2** **Hedging when** - =


The case - = is analogous. Assume that - = . Then

    



[�


[�



dt + 

dt + 


dS


dS


The stocks are perfectly correlated.

The market price of risk equations are



= S


= S


 

 


dB


dB



]


]




- r (MPR)

- r









= 

= 


The process 



[is free.] [There are two cases:]


206




 - �r =  - �r : There is no solution to (MPR), and consequently, there is no risk-neutral

  -  
measure. This market admits arbitrage. Indeed



**Case I:**











�r



=








 


�r







=


=









(dS




- r S



dt) +











(dS




- r S



d


Suppose


Then







X











- r ) dt + 












S




[(�



dB



] +



dt)


[(�


:




- r ) dt + 


dB



S


S




 


�r



�r




 














: Set







=







= 


S



; 











 - r


 - r





- r




- r







d

 


X




=


=









r

 - dt + dB































dt + dB












- r




 






dt



**Case II:**











�r



�r



| Positive {z }







=







: The market price of risk equations




- r

- r















= 

= 


have the solution




 - r




=








- r



;








 - r








=




- [is free; there are infinitely many risk-neutral measures. Let]

**Hedging:**



IP be one of them.

f







=


=


=















- r ) dt + 


dt + dB




[(�




- r ) dt + 


d







X





[(�



dB



] +



dB



]


]









S


S



dt + dB



S 


] +




 



]




[�





+




 - S



- [�



dB

e




 

S




 







S


:







Notice that



e




[does not appear.]



B



Let V be an (T ) -measurable random variable. If V depends on B
F



Let V be an (T ) -measurable random variable. If V depends on B [, then it can probably not]
F

be hedged. For example, if



V = h(S



(T ); S



(T ));



and 



[or]  



[depend on] B




[, then there is trouble.]


CHAPTER 19. A two-dimensional market model 207



More precisely, we define the



IP -martingale



f



IE

f



F (t)

  



 



 



 



 


Y (t) =







V

- (T )



; 0 - t - T :



We can write


so



dB

e



t



Y (t) = Y (0) +



t


0

Z


+ 


0

Z







dB

e



+







dB

e



;



:



To get d







X




d Y =        

- to match d Y, we must have



dB

e







= 0:


208


### **Chapter 20**

# **Pricing Exotic Options**

**20.1** **Reflection principle for Brownian motion**


**Without drift.**

Define



M (T ) = max B (t):

0�t�T



Then we have:


IP fM (T )     - m; B (T ) < bg


So the joint density is



= IP fB (T ) - m - bg



)



exp

m b

Z 


p - T



(



exp



dm db



=



p - T


@







x

T



dx; m - 0; b < m



dx

!



)



m b

Z 


IP fM (T ) dm; B (T ) dbg = 

=         


(�



x

T



@ m @ b



dm db;

)!



@

@ m



p - T



exp



(�



(m - b)

T



(m - b)



)



=



(m - b)



T



( 


(m - b)

T



dm db; m - 0; b < m:



exp



p




 - T



**With drift.** Let



B (t) = - t + B (t) ;



e



209


210



_b_



_Brownian motion_



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-211-0.png)

Figure 20.1: _Reflection Principle for Brownian motion without drift_



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-211-1.png)



_b_


Figure 20.2: _Possible values of_ B (T ); M (T ) _._


CHAPTER 20. Pricing Exotic Options 211


where B (t); 0 t T, is a Brownian motion (without drift) on (�; ; P) . Define

    -     - F



Z (T ) = exp f�� B (T ) 










T g



= exp f�� (B (T ) + - T ) +



T g



= exp f��



B (t) +



T g;







Z



Z (T ) dIP ; A F :



A



e



Set



0�t�T



IP (A) =

f



M (T ) = max

f



M (T ) = max



B (T ):

e



Under



IP ;

f



B is a Brownian motion (without drift), so



e



exp



(



)



dm~ d



~



b; m~ - 0;



~b)



~



IP f



B (T ) d



e



(m~ 


T



p







(m~ 
T



(m~ 


~b)



~b < m:~



f



M (T ) dm~ ;



f



~



~b) be a function of two variables. Then



~



bg =




 - T



Let h(m;~



)

e



B (T ))



IE h(M (T );

f



B (T )) =



e



h(



Z (T )



M (T );



=


=



f



~b=m~



~



IE

IfE


m~

f



Z



h



h(



M (T );



B (T )) expf�



e



T g

i



~b) expf�



~



B (T ) 






m~ =



~b=

f



~



~b=�



~



b 


e







IP f

f



IP f



M (T ) dm;~

f



B (T ) d



e



T g



~



bg:



m~ =0



Z



h(m~ ;


h(m~ ;



But also,



m~ =



~b=m~



~b) IP f



~



~



~



~b=�



M (T ) dm~ ;

f



M (T ) dm~ ;



IE h(M (T );

f



B (T )) =

e



Z



B (T ) d



e



~



bg:



m~ =0



Z



Since h is arbitrary, we conclude that



(MPR)



IP f



M (T ) dm;~



~



B (T ) d



eg



f



b 


IP f



f



~



bg







= exp f�



B (T ) d



e



T g



M (T ) dm~ ;



m~

f



T



~b 


~



bg



)



: expf�



~



~



b)



exp



(



~b)




 


=



(m~ 


T







(m~ 


~b < m:~



T gdm~ d



~



b; m~ - 0;



p




 - T


212


**20.2** **Up and out European call.**


Let 0 < K < L be given. The payoff at time T is



(T )<Lg







;



where



(S (T ) - K )+



fS







0�t�T



S



(T ) = max



S (t):



To simplify notation, assume that IP is already the risk-neutral measure, so the value at time zero of
the option is



v (0; S (0)) = e�r T IE



h



(S (T ) - K )







+



fS



(T )<Lg



:



i



Because IP is the risk-neutral measure,



dS (t) = r S (t) dt + - S (t) dB (t)



S (t) = S0


= S0


= S0



expf� B (t) + (r 


expf�



>�

:



B (t)g;

e



B (t)g;



)tg










>>







t



>>

<














>>



>>

;











<



exp







r











>>



>>

=





=







B (t) +










>>



>>�

:





;




 



   
| {z }



where







r





- =








- 


;



B (t) = - t + B (t):



e





Consequently,



expf�



M (t)g;

f



M (t)g;



S



(t) = S0



where,



M (t) = max



B (u):

e



B (u):



f



0�u�t



We compute,







Be(T )>







v (0; S (0)) = e�r T







fS



IE


IE


IE



h




(S (T ) - K )

S (0) expf�




S (0) expf�




+



B (T )g - K



(T )<Lg



i





e



= e�r T







B (T )g - K



+



fS (0) expf�



M (T )g < Lg



e







K

;

S (0)



e



= e�r T



"



Me (T )<







~b

| {z }



#







L

S (0)



m~

| {z }



log



log



~b


CHAPTER 20. Pricing Exotic Options 213



_y_





~~_~_~~

_m_







_x_

_~_

_B(T)_


|M(T) ~|x=y|
|---|---|
||_x=y_|
||_(B(T),_<br>|
|_b_<br>_~_|_b_<br>_~_|



Figure 20.3: _Possible values of_



B (T );

e



M (T ) _._

f



M (T ) _._



B (T );



We consider only the case



S (0) K < L; so 0

  -  


~b < m~ :



~



The other case, K < S (0) L leads to

       


~b < 0 m~ and the analysis is similar.

  


We compute



R



~b



m~



m~



: : : dy dx :



R



x



dy dx


dx



m~


x



(



+ - x 


m~



(y - x)



v (0; S (0)) = e�r T



Z



T



p







(y - x)

T



(y - x)



T



)



exp








 - T



~b



(S (0) expf� xg - K )



















+ - x 


Z

m~



= �e�r T



Z



~b



p - T



exp



(�



(y - x)

T



(y - x)







T



)



y =m~


y =x



(S (0) expf� xg - K )



+ - x 


m~



= e�r T



Z



(



p - T



exp

"







x

T







T



)



~b



(S (0) expf� xg - K )




- exp (�



(m~ - x)

T



+ - x 






T



)#



+ - x 


Z



m~



=



p - T e�r T



S (0)



(� x 


x

T



dx


 
)



dx



~b



(



x

T



+ - x 


m~



Z



e�r T








+



p - T


p - T


p - T



e�r T



K







T



T

)


dx



~b



exp


exp


m~







+ - x 


e�r T



S (0)



exp



( - x 


(m~ - x)

T







T

)



dx



~b



+ - x 


Z

m~



Z



(







(m~ - x)

T



(m~ - x)



K



exp







T

)



dx:



~b



The standard method for all these integrals is to complete the square in the exponent and then
recognize a cumulative normal distribution. We carry out the details for the first integral and just


214


give the result for the other three. The exponent in the first integrand is



x

T




- x 
= 

= 


+ - x 






T



(x - - T - - T )



+




T + - - T



T


T



x 







+ r T :



r T

 - 



- T



In the first integral we make the change of variable


y = (x           - r T =�           -           - T =)=

to obtain



pT ; dy = dx=



p



p



T ;



�r T



(� x 


exp







+ - x 

r

x  


exp f�



e



m~



p



S (0)



~b



x

T



)



dx








 - T



Z



m~



(



T






- T



dx



b

Z



~b



=


=



p - T


p - T



S (0)



S (0):



exp







r T

 

y



~b



m~

pT















r



T







T


pT



g dy



r



p



p


Z



T















pT




- N



:







r



pT









pT



!



!#



= S (0)



N

"



p



m~



T



p



~b



T







pT






r



p



T











)





pT

 


Putting all four integrals together, we have




- N



r



!







T



pT



+



!#





p







r



v (0; S (0)) = S (0)



N

"



p



m~



T



pT

 


pT







p



~b



T



p













r




 

T


+



T




- N




 

T



p



T



!#




- e�r T


- S (0)



T



r





p




 

T



!

p



p



~b



T







K



N

"



p



m~



+







pT






r



p


 

r











p



!




- N



N

"



m~



+



T !#



p



(m~ 


T



r







p



T


+



+



p



pT




p

p





:



T



~b)









T



! 


+ exp


N



�r T + m~




(m~ 


p



T











�� 


p



m~











+




 

K



N

!



T



p



T



T



;




~b)



r



S (0)







; m~ =



p



where



~b =



~



+


 



 

log







log



r


L



S (0)


CHAPTER 20. Pricing Exotic Options 215


_L_





_+_


|Col1|v(t,L) = 0<br>v(T,|Col3|
|---|---|---|
||||
||_v(t,0) = 0_|_T_|



Figure 20.4: _Initial and boundary conditions._



If we let L we obtain the classical Black-Scholes formula
!



!#

p



r



"



T





p



p







v (0; S (0)) = S (0)




- N



p



~



b



T



p



pT



p












+



r



T



T



!#




 - e�r T


= S (0)N


 - e�r T



p



~



b



T







K



"




- N







!



T



pT



+


+








- pT



S (0)

K



log



r



r pT

 









+



p



T



!



:



S (0)

K







K N




- pT



log



If we replace T by T t and replace S (0) by x in the formula for v (0; S (0)), we obtain a formula

      for v (t; x), the value of the option at the time t if S (t) = x . We have actually derived the formula
under the assumption x K L, but a similar albeit longer formula can also be derived for

       -       
K < x L . We consider the function

  


h



e�r (T �t)



(S (T ) - K )+



fS







v (t; x) = IE



t;x



(T )<Lg

i



; 0 - t - T ; 0 - x - L:



This function satisfies the _terminal condition_



v (T ; x) = (x - K )+



; 0 - x < L



and the _boundary conditions_



v (t; 0) = 0; 0 - t - T ;

v (t; L) = 0; 0 - t - T :



We show that v satisfies the Black-Scholes equation



r v + vt




+ r xvx



+







x



vxx



; 0 - t < T ; 0 - x - L:


216


Let S (0) - 0 be given and define the _stopping time_


                - = minft                 - 0; S (t) = Lg:

**Theorem 2.61** _The process_



e�r (t^� ) v (t ^ - ; S (t ^ - )); 0 - t - T ;



_is a martingale._


**Proof:** First note that







S



(T ) < L () - - T :



Let ! - be given, and choose t [0; T ] . If - (! ) t, then

              


e




fS







IE



�r T



(S (T ) - K )+



(T )<Lg



F (t)

  


(! ) = 0:



















But when - (! ) t, we have

    


v (t ^ - (! ); S (t ^ - (! ); !)) = v (t ^ - (! ); L) = 0;



so we may write



IE



e�r T




(S (T ) - K )+



fS







(T )<Lg



F (t)

  


















r (t       - (!))

(! ) = e� ^ v (t ^ - (! ); S (t ^ - (! ); !)) :



On the other hand, if - (! ) - t, then the Markov property implies



e




i



(S (T ) - K )+



fS 


IE



�r T



(T )<Lg



















F (t)

   






(! )



(T )<Lg



t;S (t;! )



e



�r T



(S (T ) - K )+



fS



= IE



= e�r t



h



v (t; S (t; !))



r (t    - (! ))

= e� ^ v (t ^ - ; S (t ^ - (! ); ! )) :



In both cases, we have



e�r (t^� ) v (t ^ - ; S (t ^ - )) = IE



e




�r T (S (T ) - K )+



fS



(T )<Lg



F (t)

  


:

























Suppose 0 u t T . Then

   -    -    







F (u)



IE



e




�r (t^� )



v (t ^ - ; S (t ^ - ))



fS











e








F (u)

   


= IE


= IE



e�r T



(S (T ) - K )+


















 



 



 



 


IE



�r T



(S (T ) - K )



+















u�



F (t)



(T )<Lg











fS 


(T )<Lg







F (u)



�r (u^� )



= e



v (u ^ - ; S (u ^ - )) :














CHAPTER 20. Pricing Exotic Options 217


For 0 t T, we compute the differential

  -  







- S vx



= e�r t



( r v + vt

 


+ r S vx



+




 

+



d



e



�r t



v (t; S (t))



S





vxx ) dt + e�r t



S



dB :



Integrate from 0 to t - :
^







e�r (t^� )



v (t ^ - ; S (t ^ - )) = v (0; S (0))



e�r u ( r v + vt

  


Z



t^�



+ r S vx


+



+



Z



vxx ) du



0



e�r u



t^�




- S vx



dB :



0



Because e



v (t - ; S (t - )) is also a martingale, the Riemann integral
^ ^



�r (t^� )



A stopped martingale is still a martingale | {z }



e�r u ( r v + vt

  


+ r S vx







0

Z



Z



t^�



(u)vxx (u; S (u)) = 0; 0 u t - :

       -        - ^



S



vxx ) du



is a martingale. Therefore,



r v (u; S (u)) + vt


The PDE



(u; S (u)) + r S (u)vx (u; S (u)) +







+


S



+ r xvx



+







x



vxx



= 0; 0 - t - T ; 0 - x - L;



then follows.

**The Hedge**



r v + vt









- S (t)vx (t; S (t)) dB (t); 0 t - :

        -        


= e�r t



d







e



�r t



v (t; S (t))



Let X (t) be the wealth process corresponding to some portfolio �(t) . Then



d(e�r t X (t)) = e�r t



�(t)� S (t) dB (t):



We should take


and


Then



X (0) = v (0; S (0))


�(t) = vx (t; S (t)); 0 t T - :

       -       - ^



X (T ^ - ) = v (T ^ - ; S (T ^ - ))



+ if - - T



=



(



v (T ; S (T )) = (S (T ) - K )



v (� ; L) = 0 if - T .

          

218



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-219-0.png)









_0_ _K_ _L_ _x_


Figure 20.5: _Practial issue._


**20.3** **A practical issue**


For t < T but t near T, v (t; x) has the form shown in the bottom part of Fig. 20.5.

In particular, the hedging portfolio



�(t) = vx



(t; S (t))



can become very negative near the knockout boundary. The hedger is in an unstable situation. He
should take a large short position in the stock. If the stock does not cross the barrier L, he covers
this short position with funds from the money market, pays off the option, and is left with zero. If
the stock moves across the barrier, he is now in a region of �(t) = vx (t; S (t)) near zero. He should



the stock moves across the barrier, he is now in a region of �(t) = vx (t; S (t)) near zero. He should

cover his short position with the money market. This is more expensive than before, because the
stock price has risen, and consequently he is left with no money. However, the option has “knocked
out”, so no money is needed to pay it off.

Because a large short position is being taken, a small error in hedging can create a significant effect.
Here is a possible resolution.

Rather than using the boundary condition


v (t; L) = 0; 0                - t                - T ;

solve the PDE with the boundary condition



x



v (t; L) + �Lvx



(t; L) = 0; 0 - t - T ;



where - is a “tolerance parameter”, say %. At the boundary, Lv



where - is a “tolerance parameter”, say %. At the boundary, Lvx (t; L) is the dollar size of the

short position. The new boundary condition guarantees:



x



1. Lv



x



(t; L) remains bounded;



2. The value of the portfolio is always sufficient to cover a hedging error of - times the dollar
size of the short position.


### **Chapter 21**

# **Asian Options**

Stock:


dS (t) = r S (t) dt +            - S (t) dB (t):


Payoff:



S (t) dt

!



T


0

Z



:



V = h



Z



T


0


h



Value of the payoff at time zero:


X (0) = IE



e�r T

"



S (t) dt

!#



Introduce an _auxiliary process_ Y (t) by specifying


d Y (t) = S (t) dt:


With the initial conditions


S (t) = x; Y (t) = y ;


we have the solutions



nT



S (T ) = x exp




- (B (T ) - B (t)) + (r 






)(T - t)

   


;



T



Y (T ) = y +



Z



S (u) du:



t



Define the undiscounted expected payoff



u(t; x; y ) = IE t;x;y



h(Y (T )); 0 - t - T ; x - 0; y IR:


219


220


**21.1** **Feynman-Kac Theorem**


The function u satisfies the PDE



+



= 0; 0 - t - T ; x - 0; y IR;



ut



+ r xux







x



uxx



+ xuy



the terminal condition


and the boundary condition



u(T ; x; y ) = h(y ); x - 0; y IR;



u(t; 0; y ) = h(y ); 0               - t               - T ; y IR:

One can solve this equation. Then



S (u) du

   


0

Z



Z



t



v



t; S (t);




is the option value at time t, where



v (t; x; y ) = e�r (T �t)



u(t; x; y ):



The PDE for v is



r v + vt




+ r xvx



+ r xv



v (T ; x; y ) = h(y );



+



= 0; (1.1)







x



vxx + xvy



v (t; 0; y ) = e�r (T �t) h(y ):



One can solve this equation rather than the equation for u .


**21.2** **Constructing the hedge**


Start with the stock price S (0) . The differential of the value X (t) of a portfolio �(t) is



dX = - dS + r (X - �S ) dt



= �S (r dt + - dB ) + r X dt - r �S dt



= �� S dB + r X dt:



We want to have


so that



X (t) = v


X (T ) = v


= h



0

Z



Z



t



t; S (t);




T


0

Z



0

Z



Z



S (u) du

   

T

S (u) du



;


!



T ; S (0);



;



S (u) du

!



:


CHAPTER 21. Asian Options 221


The differential of the value of the option is



S (u) du

   


0

Z



t



= (vt



+ r S vx







dS + vy



S dt +



vxx



dv



t; S (t);




= vt



dt + vx



dS dS



+ S vy



+



S



vxx ) dt + - S vx



dB



= r v (t; S (t)) dt + vx (t; S (t)) - S (t) dB (t): (From Eq. 1.1)



Compare this with



Take �(t) = v



x



dX (t) = r X (t) dt + �(t)   - S (t) dB (t):


(t; S (t)): If X (0) = v (0; S (0); 0), then











t



X (t) = v



t; S (t);



; 0 - t - T ;



Z



S (u) du



0



because both these processes satisfy the same stochastic differential equation, starting from the same
initial condition.



**21.3** **Partial average payoff Asian option**


Now suppose the payoff is



S (t) dt

!



V = h



T


 
Z



;



where 0 < - < T . We compute


v (� ; x; y ) = IE



e�r (T �� )




 - ;x;y



h(Y (T ))



just as before. For 0 t -, we compute next the value of a derivative security which pays off

      -      
v (� ; S (� ); 0)

at time - . This value is



t;x



v (� ; S (� ); 0):



w (t; x) = IE



e�r (� �t)



The function w satisfies the Black-Scholes PDE



r w + wt

     
with terminal condition


and boundary condition


The hedge is given by



+ r xwx



+







x



wxx = 0; 0 t - ; x 0;

    -     -     


w (� ; x) = v (� ; x; 0); x - 0;



w (t; 0) = e�r (T �t)



h(0); 0 - t - T :



(t; S (t)); 0 - t - - ;



�(t) =



<



w



v



R



S (u) du











t



; - < t - T :







t; S (t);



:



x


x


222



**Remark 21.1** While no closed-form for the Asian option price is known, the Laplace transform (in

     
the variable (T t) ) has been computed. See H. Geman and M. Yor, _Bessel_ _processes, Asian_




     
the variable (T t) ) has been computed. See H. Geman and M. Yor, _Bessel_ _processes, Asian_

     _options, and perpetuities,_ Math. Finance 3 (1993), 349–375.






### **Chapter 22**

# **Summary of Arbitrage Pricing Theory**

A _simple European derivative security_ makes a random payment at a time fixed in advance. The
_value at time_ t of such a security is the amount of wealth needed at time t in order to replicate the
security by trading in the market. The _hedging portfolio_ is a specification of how to do this trading.


**22.1** **Binomial model, Hedging Portfolio**


Let - be the set of all possible sequences of n coin-tosses. We have _no probabilities_ at this point.
Let r 0; u - r + ; d = =u be given. (See Fig. 2.1)

  
Evolution of the value of a portfolio:



Sk +



�k




Sk



Xk +



= �k



+ ( + r )(Xk



):



Given a simple European derivative security V (!



Given a simple European derivative security V (! ; ! ), we want to start with a nonrandom X0 [and]

use a portfolio processes



; !



), we want to start with a nonrandom X



�0



; 


(H ); 


so that



X



(!



; !



) = V (!



; !



) !



; !



(T )


: (four equations)



There are four unknowns: X



0 ; �0



; 


(H ); 


(T ) . Solving the equations, we obtain:


223


224



V (!



;H )



V (! ;T )

| {z }



V (!



;T )



; H )



+



u - ( + r )

u  - d



u - ( + r )



X (!



; T )



X





(!


X


(!



) =



) =



(!



;



+ r - d

u - d



+ r - d



X



V (! ;H )

| {z u}



+ r - d



u - d



u - d



+ r


+ r



u - ( + r )



(T )







;



0



=



(!

(!



X



(H ) +



X



; H ) - X



; H ) - S



; T )

; T )



(!

(!



(H ) - X

(H ) - S







(T )



;



(T )



�0



=



X

S

X

S



:



The probabilities of the stock price paths are irrelevant, because we have a hedge which works on
_every_ _path._ From a practical point of view, what matters is that the paths in the model include all
the possibilities. We want to find a description of the paths in the model. They all have the property







(log Sk +



log Sk )




=



log




Sk +



Sk



= (� log u)



= (log u)



:



Let - = log u - 0 . Then



(log Sk +



log Sk )




= 


n:



k =0



per unit time.



The paths of log S



k [accumulate quadratic variation at rate] 


n�


k =0

X



If we change u, then we change -, and the pricing and hedging formulas on the previous page will
give different results.

We reiterate that the probabilities are only introduced as an aid to understanding and computation.
Recall:



= �k



Sk + + ( + r )(Xk



�k




):



Define


Then


i.e.,



Xk +


X



�k +


Xk +

�k +



= ( + r )k :



�k



Sk

�k



k +



= �k Sk +

�k +



+



Xk

�k



�k




Sk


;







Sk +

�k +







Xk



�k







Sk

�k



:




= �k



In continuous time, we will have the analogous equation



d

 


X (t)

- (t)







S (t)

- (t)







= �(t) d







:


CHAPTER 22. Summary of Arbitrage Pricing Theory 225



k [martingale, then]

k [is a]



If we introduce a probability measure IP under which S�kk [is a] [martingale, then] X�kk [will also be] [a]

martingale, regardless of the portfolio used. Indeed,



X

 


If we introduce a probability measure



IP under which



f



k



S

 


k



















IE

fX



X







Xk +

�k +



�k




 
k











Sk

�k



F



Xk

�k



+ 


IE

f







F



=


=



k











:



k



k


k



k




 



 



 



 


















S








k







Sk +

�k +

Sk +

�k +



=0



F







IE

f








+ 


k



Suppose we want to have X



Suppose we want to have X = V, where V is some [-measurable] [random variable.] [Then] [we]

F

must have



= V, where V is some
F



=0

| {z }





















f




 
 



 
 



 



 


IE

f



X




=



=



;








X

 






=



V



:

 


:



F



IE



+ r



X


X




 

=



F




X0



X




V








IE

f



�0



IE

f







k



0



=



=



To find the risk-neutral probability measure



IP under which



f



S




 


k [a] [martingale,] [we] [denote] p~ =

k [is]



IP f!

f



IP f!

f



IE

f



IE







k



= H, q~ =
g



k



= T, and compute
g























Sk



Sk



Sk +

�k +



F



= pu~



�k +



=



+ q~d



�k +



k



+ r



Sk




[pu~ + q~d]



�k



:



We need to choose p~ and q~ so that


The solution of these equations is


p~ =



+ r d

 - ; q~ =

u - d



pu~ + q~d = + r;


p~ + q~ = :



u - ( + r )

u  - d



u - ( + r )



:



**22.2** **Setting up the continuous model**



Now the stock price S (t); 0 t T, is a continuous function of t . We would like to hedge

        -         along every possible path of S (t), but that is impossible. Using the binomial model as a guide, we
choose - - 0 and try to hedge along every path S (t) for which the quadratic variation of log S (t)
accumulates at rate - per unit time. These are the paths with volatility - .

To generate these paths, we use Brownian motion, rather than coin-tossing. To introduce Brownian
motion, we need a probability measure. However, the only thing about this probability measure
which ultimately matters is the set of paths to which it assigns probability zero.



per unit time. These are the paths with volatility 


.


226


Let B (t) ; 0 t T, be a Brownian motion defined on a probability space (�; ; P) . For any

    -    - F

- IR, the paths of

�t +                     - B (t)



accumulate quadratic variation at rate - per unit time. We want to define



so that the paths of



S (t) = S (0) expf�t + - B (t)g;


log S (t) = log S (0) + �t + - B (t)



accumulate quadratic variation at rate - per unit time. Surprisingly, the choice of - in this definition

is irrelevant. Roughly, the reason for this is the following: Choose ! - . Then, for - IR,



accumulate quadratic variation at rate 



- . Then, for 


IR,



); 0 - t - T ;







t + - B (t; !



is a continuous function of t . If we replace - [by] - [, then] - t + - B (t; ! ) is a different function.

However, there is an ! - such that



is a continuous function of t . If we replace 



[by]  



[, then] 



- such that



t + - B (t; !



) = 


t + - B (t; !



); 0 - t - T :







t + - B (t; !



In other words, regardless of whether we use 


In other words, regardless of whether we use - [or] - [in the definition of] S (t), we will see the same

paths. The mathematically precise statement is the following:




[or]  


If a set of stock price paths has a positive probability when S (t) is defined by



S (t) = S (0) expf�



t + - B (t)g;



then this set of paths has positive probability when S (t) is defined by



S (t) = S (0) expf�



t + - B (t)g:



Since we are interested in hedging along every path, except possibly for a set of paths
which has probability zero, the choice of    - is irrelevant.


The most _convenient_ choice of - is







;



so


and




- = r 


S (t) = S (0) expfr t + - B (t) 


tg;


tg



e�r t



S (t) = S (0) expf� B (t) 








is a martingale under IP . With this choice of -,



dS (t) = r S (t) dt + - S (t) dB (t)


CHAPTER 22. Summary of Arbitrage Pricing Theory 227


and IP is the risk-neutral measure. If a different choice of - is made, we have



S (t) = S (0) expf�t + - B (t)g;



dS (t) = (� +







)



S (t) dt + - S (t) dB (t):




   
|r S (t{z) dt +}



h



:







d



B (t)



= r S (t) dt + 


��� r



��r



dt + dB (t)



dB (t)

| {z }



i







B has the same paths as B . We can change to the risk-neutral measure



B has the same paths as B . We can change to the risk-neutral measure IP, under which B is a

Brownian motion, and then proceed as if - had been chosen to be equal to r - .

e f� e



IP, under which



f



.



e



e



e



**22.3** **Risk-neutral pricing and hedging**



Let



IP denote the risk-neutral measure. Then



f



dS (t) = r S (t) dt + - S (t) d



B (t);



where


Then



B is a Brownian motion under

e


d



IP . Set







d



B (t);



e



f




- (t) = er t :



S (t)

= 
  - (t)



B (t);

e



S (t)

- (t)

  


so



S (t)

- (t) [is a martingale under]



IP .

f



S (t)



Evolution of the value of a portfolio:



dX (t) = �(t)dS (t) + r (X (t) �(t)S (t)) dt; (3.1)

         


which is equivalent to



= �(t)d


= �(t)�







S (t)

- (t)



X (t)

- (t)

  


S (t)

- (t)



B (t):



d








- (3.2)



e



d



Regardless of the portfolio used,



X (t)

- (t) [is a martingale under]



IP .



f



X (t)



Now suppose V is a given (T ) -measurable random variable, the payoff of a simple European
F
derivative security. We want to find the portfolio process �(T ); 0 t T, and initial portfolio
value X (0) so that X (T ) = V . Because X (t) [must be a martingale, we must have] - 


X (t)

- (t) [must be a martingale, we must have]



X (t)



X (t)

 - (t)



















F (t)



=



IE

f



; 0 t T : (3.3)

  -  






V

- (T )







This is the _risk-neutral pricing formula._ We have the following sequence:


228


1. V is given,

2. Define X (t); 0 t T, by (3.3) (not by (3.1) or (3.2), because we do not yet have �(t) ).

      -      
3. Construct �(t) so that (3.2) (or equivalently, (3.1)) is satisfied by the X (t); 0 t T,

                       -                        defined in step 2.



To carry out step 3, we first use the tower property to show that



X (t)

- (t) [defined by (3.3) is a martingale]



X (t)



under IP . We next use the corollary to the Martingale Representation Theorem (Homework Problem

4.5) to show that



under



f



d

 


X (t)

- (t)







e



B (t) (3.4)



= - (t) d



for some proecss - . Comparing (3.4), which we know, and (3.2), which we want, we decide to
define




- (t)� (t)

 - S (t)



�(t) =



: (3.5)



Then (3.4) implies (3.2), which implies (3.1), which implies that X (t); 0 t T, is the value of

                    -                    the portfolio process �(t); 0 t T .

        -        
From (3.3), the definition of X, we see that the hedging portfolio must begin with value







X (0) =



IE

f







V

- (T )



;



and it will end with value


X (T ) =      - (T )



F (T )

   


V

- (T )



















V

= - (T )

   - (T )



IE

f







= V :



**Remark 22.1** Although we have taken r and - to be constant, the risk-neutral pricing formula is
still “valid” when r and - are processes adapted to the filtration generated by B . If they depend on
either B or on S, they are adapted to the filtration generated by B . The “validity” of the risk-neutral



either B or on S, they are adapted to the filtration generated by B . The “validity” of the risk-neutral

pricing formula means:



e



1. If you start with







X (0) =



IE

f







V

- (T )



;



then there is a hedging portfolio �(t); 0 t T, such that X (T ) = V ;

           -           


2. At each time t, the value X (t) of the hedging portfolio in 1 satisfies



X (t)

 - (t)



IE

f















F (t)

  


=



V

 - (T )








:



**Remark 22.2** In general, when there are multiple assets and/or multiple Brownian motions, the
risk-neutral pricing formula is valid provided there is a _unique risk-neutral measure._ A probability
measure is said to be risk-neutral provided


CHAPTER 22. Summary of Arbitrage Pricing Theory 229


it has the same probability-zero sets as the original measure;

  
it makes all the discounted asset prices be martingales.

  


To see if the risk-neutral measure is unique, compute the differential of all discounted asset prices
and check if there is more than one way to define B so that all these differentials have only dB



B so that all these differentials have only d



e



B dB

terms.



e



**22.4** **Implementation of risk-neutral pricing and hedging**


To get a computable result from the general risk-neutral pricing formula



X (t)

- (t)



IE

f





















F (t)



=







V

- (T )



;







one uses the Markov property. We need to identify some _state variables,_ the stock price and possibly
other variables, so that



F (t)



V

- (T )



















X (t) = - (t)











is a function of these variables.



IE

f



**Example 22.1** Assume r and - are constant, and V = h(S (T )) . We can take the stock price to be the state
variable. Define



e



�r (T �t)



i



IE



t;x



h



h(S (T ))



:



Then



v (t; x) =


X (t) = e



IE

e



r t



IE

e



h(S (T ))



















e



�r T



F (t)

  

:



= v (t; S (t));







and



X (t)

 - (t)



= e�r t



v (t; S (t)) is a martingale under



IP .

e



IP .



**Example 22.2** Assume r and - are constant.


V = h



T


0

Z



S (u) du

!



Take S (t) and Y (t) =


where



t


0

R



S (u) du to be the state variables. Define



v (t; x; y ) =



�r (T �t)



h(Y (T ))

i



;



IE

e



IE



t;x;y



e

h



h



Y (T ) = y +

t

Z



T



S (u) du:


230


Then


and


is a martingale under



IP .



e



X (t) = er t



eS



h(S (T ))







IE







e



�r T



F (t)

  


= v (t; S (t); Y (t))















X (t)

 - (t)



= e�r t v (t; S (t); Y (t))



**Example 22.3** (Homework problem 4.2)



dS (t) = r (t; Y (t)) S (t)dt + - (t; Y (t))S (t) d



B (t);



;

e



d Y (t) = �(t; Y (t)) dt +             - (t; Y (t)) d


V = h(S (T )):

Take S (t) and Y (t) to be the state variables. Define



B (t);



e



r (u; Y (u)) du

)



T



v (t; x; y ) =



IE

e



t;x;y



exp




       - (t)

       - (T )

| {z }



(� t

Z



h(S (T ))



Then


and


is a martingale under



IP .



e



)



F (t)



X (t) = - (t)



IE











h(S (T ))

 - (T )



(



Z




















 



 
 



 
 


r�(



T


t



"



e



h(S (T ))



:


#



=



IE

ve(



exp







r (u; Y (u)) du



F (t)



= v (t; S (t); Y (t));



r (u; Y (u)) du

    


t



X (t)

- (t)




 



0



= exp



Z



v (t; S (t); Y (t))



In every case, we get an expression involving v to be a martingale. We take the differential and
set the dt term to zero. This gives us a partial differential equation for v, and this equation must
hold wherever the state processes can be. The dB term in the differential of the equation is the



hold wherever the state processes can be. The dB term in the differential of the equation is the

differential of a martingale, and since the martingale is



e



X (t)

- (t)



0



e



t



= X (0) +



Z



�(u)�



S (u)

- (u)



B (u)



d



we can solve for �(t) . This is the argument which uses (3.4) to obtain (3.5).


CHAPTER 22. Summary of Arbitrage Pricing Theory 231


**Example 22.4 (Continuation of Example 22.3)**







Z



t



X (t)

- (t)







v (t; S (t); Y (t))



= exp







0



r (u; Y (u)) du



=� (t)



is a martingale under



IP . We have



e



=� (t)

| {z }



+ vt



dt + vx







d







X (t)

- (t)



=









�r (t; Y (t))v (t; S (t); Y (t)) dt



(�r v + vt



dS + vy



d Y


dS d Y +



vy y



d Y d Y




 


+



vxx



dS dS + vxy



S



vxx



+ - - S vxy



+


= 0



vy y



) dt











xy



=




- (t)


- (t)



+ r S v



x



+ �vy



v



+


xx



+ (� S vx



+ - v



y



) d



B

e



The partial differential equation satisfied by v is



�r v + vt



+ r xvx + �vy






x



+ - - xv



vy y



+











+



where it should be noted that v = v (t; x; y ), and all other variables are functions of (t; y ) . We have












- (t)



d



X (t)

 - (t)



=



+ - vy



] d



B (t);



e




[� S vx



where - = - (t; Y (t)), - = - (t; Y (t)), v = v (t; S (t); Y (t)), and S = S (t) . We want to choose �(t) so that
(see (3.2))











S (t)

= �(t)� (t; Y (t))

       - (t)



d



X (t)

 - (t)



d



Therefore, we should take �(t) to be



Be (t):


(t; S (t); Y (t)):



�(t) = vx



(t; S (t); Y (t)) +




 - (t; Y (t))

- (t; Y (t)) S (t)



vy


232


### **Chapter 23**

# **Recognizing a Brownian Motion**

**Theorem 0.62 (Levy)** _Let_ B (t) ; 0 t T ; _be_ _a_ _process_ _on_ (�; ; P) _,_ _adapted_ _to_ _a_ _filtration_

          -          - F

F (t); 0 - t - T _, such that:_


_1._ _the paths of_ B (t) _are continuous,_


_2._ B _is a martingale,_

_3._ hB i(t) = t; 0  - t  - T _, (i.e., informally_ dB (t) dB (t) = dt _)._


_Then_ B _is a Brownian motion._


**Proof:** (Idea) Let 0 s < t T be given. We need to show that B (t) B (s) is normal, with

      -      -      mean zero and variance t s, and B (t) B (s) is independent of (s) . We shall show that the

       -        - F
_conditional moment generating function_ of B (t) B (s) is

             




















(t�s)



:



F (s)

  


u



IE



e




u(B (t)�B (s))



= e



Since the moment generating function characterizes the distribution, this shows that B (t) B (s)

                        is normal with mean 0 and variance t s, and conditioning on (s) does not affect this, i.e.,

           - F



B (t) B (s) is independent of (s) .

  - F



We compute (this uses the continuity condition (1) of the theorem)



= ueuB (t)



= euB (s)



dB (t) +



dB (t) dB (t);



u



u



euB (t)



so



deuB (t)


euB (t)



euB (v )



t

ueuB (v )


233



t



+



dv :

uses cond. 3 |{z}



s

Z



dB (v ) +



s

Z


234


Now



R



t


0



dB (v ) is a martingale (by condition 2), and so



ueuB (v )



t



Z



t


0

�Z







s


0




 


F (s)



IE







Z



ueuB (v )



dB (v )







s
















 



 


v�



F (s)

  


= 
= 0:



ueuB (v )



dB (v ) + IE



ueuB (v ) dB (v )



It follows that


We define


so that


and



'(s) = euB (s)


'(t) = euB (s)




 



 



 



 


F (s)

  


t



F (s)

   


+



s

Z



IE



e




uB (v )



IE



euB (t)
















dv :



= euB (s)



u







e




















F (s)

   


'(v ) = IE



uB (v )



;



+



t



u



s

Z



'(v ) dv ;



'0



(t) =



u



'(t);



t :



s =) k = euB (s)�



'(t) = k e



Plugging in s, we get


Therefore,



s



:



euB (s)



= k e



u


u



F (s)


F (s)



u



(t�s)



u


;



= '(t) = euB (s)+



IE



euB (t)






































(t�s)



:



u



IE



e




u(B (t)�B (s))



= e







CHAPTER 23. Recognizing a Brownian Motion 235


**23.1** **Identifying volatility and correlation**



Let B




[and] B [be independent Brownian motions and]



=


=



= r dt + 

= r dt + 


:



;


;



dB



Define


Define processes W




[and] W [by]


dW


dW



dS

S

dS

S


 

 






q

q�



dB


dB


;


;











+ 

+ 


+ 
 

+ 
 
+ 
 






+ 

+ 

:


dB


dB




- =







=


=




 

dB


dB









Then W




[and] W




[have continuous paths, are martingales, and]









dB


+ 


dW


dW



=


=



= dt;


= dt:



+ 

dB



dB


dB


)


dB



(�


(�



dB


dB



)



and similarly


Therefore, W [and] W




[are Brownian motions. The stock prices have the representation]



dW


dW



dS

S

dS

S



= r dt + 

= r dt + 


dW


dW



;


:



The Brownian motions W




[and] W




[are correlated. Indeed,]









dW



dW



=


=



+ 

+ 






dB



)(�



dB



+ 


dB



)









(�


(�



dB





) dt



= - dt:


236


**23.2** **Reversing the process**


Suppose we are given that


dS

S

dS

S



= r dt + 

= r dt + 


dW


dW



;


;



where W


so that




[and] W




[are Brownian motions with correlation coefficient]  - . We want to find



+ 
+ 







- =




 
"�



#




 
 




 











 




��0



=


=


=



"

"

"










��



# "


+ 
+ 

��

 


#














A simple (but not unique) solution is (see Chapter 19)



= 


; 


#


#


 
 

= 0;




- 

;


dB



q



= ��




 

= ��



dB



; 


=







:



This corresponds to



= dW










 

dW


dW



= 


dB



=) dB



+







; (� = �)




- - dW




- 


=) dB



=



dW



q

p




- 


If - =, then there is no B

  



[and] dW



= - dB



= - dW



:


dW



+ 


dW



Continuing in the case - =, we have

       


dB


dB



dB


dB



= dW



=


=



dW



= dt;




- 

- 


dt - 


dW




- - dW



dW












dW



dt + 


dt

 


= dt;


CHAPTER 23. Recognizing a Brownian Motion 237



so both B




[and] B




[are Brownian motions. Furthermore,]



p

p




- 

- 


(� dt - - dt) = 0:



dB



dB



=


=




- �dW



dW



)



(dW



dW



We can now apply an **Extension** **of** **Levy’s** **Theorem** that says that Brownian motions with zero
cross-variation are independent, to conclude that B ; B [are independent Brownians.]




[are independent Brownians.]



; B


238


### **Chapter 24**

# **An outside barrier option**

Barrier process:



d Y (t)

Y (t)



= - dt + 


dB



(t):



Stock process:



dS (t)

S (t)



= - dt + ��



q




- 


dB



(t) +







dB



(t);



where 



[are independent Brownian motions on some]




- 0; 



- 0; < - <, and B

  


(�; ; P) . The option pays off:
F




[and] B



(S (T ) - K )+



fY







(T )<Lg



at time T, where



0 < S (0) < K ; 0 < Y (0) < L;



Y (t):



Y







(T ) = max

0�t�T



(T ) = max



**Remark 24.1** The option payoff depends on both the Y and S processes. In order to hedge it, we
will need the money market and two other assets, which we take to be Y and S . The risk-neutral
measure must make the discounted value of every traded asset be a martingale, which in this case
means the discounted Y and S processes.



We want to find 



[and]  



[and define]



dt + dB



; dB

e

239



dt + dB



dB

e



= 


= 


;


240


so that


We must have


We solve to get



d Y

Y


dS

S



= r dt + ��


= r dt + ��



= r dt + 

= r dt + 


B

e



d







dt + 


dB



;



q



d



B



B







+



d



dt




- 
- 









 


e



e



q



dt +




- 


q



+ ��



dB




 

+



dB



:




- = r + 



 


; (0.1)




- = r + ��







+

q




- 










: (0.2)




- r

 - ;

 



- - r - ��



p




- 












=


=







:



We shall see that the formulas for 


We shall see that the formulas for - [and] - [do] [not] [matter.] [What] [matters] [is] [that] [(0.1)] [and] [(0.2)]

uniquely determine - [and] - [. This implies the existence and uniqueness of the risk-neutral measure.]



uniquely determine - [and] - [. This implies the existence and uniqueness of the risk-neutral measure.]

We define




[and]  



[and]  


Z (T ) = exp



n



��



(�



+ 


)T







B



(T ) - 


B



(T ) 


;



IP (A) =



A

Z



Z (T ) dIP ; A F :



Under IP, B [and] B [are] [independent Brownian motions (Girsanov’s Theorem).] IP is the unique

risk-neutral measure.



Under



IP,

f



B

e




[and]



B

e



f




[are] [independent Brownian motions (Girsanov’s Theorem).]



f



**Remark 24.2** Under both IP and



IP, Y has volatility 



[and]



f



d Y dS

Y S



= ��








[,] S has volatility    

dt;



i.e., the correlation between



d Y

Y [and]



dSS [is] - .



The value of the option at time zero is


v (0; S (0); Y (0)) =



IE

f



h



(S (T ) - K )+



fY







e



�r T



i



:



(T )<Lg



We need to work out a density which permits us to compute the right-hand side.


CHAPTER 24. An outside barrier option 241


Recall that the _barrier process_ is



d Y

Y



= r dt + 


dB

e



;



so


Set


Then


The joint density of


_The stock process._



Y (t) = Y (0) exp



B

e



t :

 


(t) 



- = r =�




- 


r t + 
n


= ;



B (t) =




- t +



b



B

e



(t);



(

b



)

b



0�t�T



M (T ) = max



B (t):



c



b



Y (t) = Y (0) expf�



B (t)g;



M

b



M (T )g:



c



Y







(T ) = Y (0) expf�



B (T ) and



cd



Pb



M (T ), appearing in Chapter 20, is



IP f



f



B (T ) d



^b;



(







(m^ 
T



(m^ 


+





b



exp



M (T ) dm^ g



c



^b)



^b)



=



b



(m^ 


T



^



b 




b






T




B

e



)



d



^



b dm;^



p




 - T



^b < m:^



^



m^ - 0;



dS

S



= r dt + ��



dB

e



+

q




- 






dB ;

e


 - 


T +



B



so



S (T ) = S (0) expfr T + ��



( - 

(T )g



)�



T g



B



(T ) 


(T ) 



- 


B

e



q



q




- 





q



= S (0) expfr T 






Te



T + ��



(T ) +



(e



(T )g



From the above paragraph we have



B (T );

b



B (T );



(T ) = 



- T +

b



so



B

e



S (T ) = S (0) expfr T + ��



B (T ) 
b




- T +

b




- 






T - ��







B

e


242


**24.1** **Computing the option value**



fY



v (0; S (0); Y (0)) =



IE

f



h



e



�r T



IE

f



(S (T ) - K )+




- (T )<Lg



i







�r T



S (0) exp

- 


= e




- )T + ��

b



B (T ) +

b



B (T ) +



q




- 


�+







(r 







- ��







B

e



(T )

 



- K



:



fY (0) exp[�



M (T )]<Lg



M (T )) . The density of



We know the joint density of (



B (T );



c



b



~



bg =



p - T



B



(T ) is



d~b;



)



e



~b

T



~b IR:



IP f



exp



(�



b



f



B



e



(T ) d



Furthermore, the pair of random variables (



B

e



B

;

e




[and]



M (T )) is _independent_ of



c




[are independent under]



f



B (T );



(T ) because



B

e



B IP (B (T ); B (T ); M (T ))

is



b



B

is

e



IP . Therefore, the joint density of the random vector (



B (T );



b



(T );



c



b



c



IP f

f



IP f



IP f



B (T ) d



M (T ) dm;^ g =



B

e



B (T ) d



b



M (T ) dm^ g

c



M (T ) dm^ g



(T ) d



~b;



(T ) d



~



bg:



f



B

e



^b;



IP f

f



IP f



^b;



The option value at time zero is



v (0; S (0); Y (0))



m^







log



L

Y (0)



Z







�+



+







T



�



S (0) exp








q




- 



- K



= e�r T



Z



^b +




- )T + ��

b








- ��







~b







(r 


�



~b



p - T



Z0


exp



(



:


:



T

~



)



exp



+



(m^ 


^b)



^b)



(�



(m^ 
T



(m^ 




b



^



b 




b



T

)



p



^



b dm:^




 - T



:d



b d



The answer depends on T ; S (0) and Y (0) . It also depends on 


The answer depends on T ; S (0) and Y (0) . It also depends on - ; - ; �; r; K and L . It does not

r                                            
depend on �; �; - ; nor - [. The parameter] - appearing in the answer is - = :



:



; nor 



[. The parameter]




- appearing in the answer is



b



; 










r








- =



b



**Remark 24.3** If we had not regarded Y as a traded asset, then we would not have tried to set its
mean return equal to r . We would have had only one equation (see Eqs (0.1),(0.2))




- = r + ��



q




- 






+











(1.1)



to determine - [and] - [.] [The] [nonuniqueness of] [the] [solution alerts] [us] [that some] [options cannot] [be]

hedged. Indeed, any option whose payoff depends on Y cannot be hedged when we are allowed to
trade only in the stock.




[and]  


to determine 

CHAPTER 24. An outside barrier option 243


If we have an option whose payoff depends only on S, then Y is superfluous. Returning to the
original equation for S,



dS

S



= - dt + ��



q




- 


dB



+



dB



;



we should set



dW = - dB



+



q




- 


dB






;



so W is a Brownian motion under IP (Levy’s theorem), and



dS

S



= - dt + - dW:



Now we have only Brownian motion, there will be only one -, namely,




- =




- - r

 


;



so with d



W = - dt + dW; we have

f



W = - dt + dW; we have



dS

S



= r dt + 


dW ;

f



and we are on our way.



**24.2** **The PDE for the outside barrier option**


Returning to the case of the option with payoff



(S (T ) - K )+



fY



(T )<Lg




 


;



we obtain a formula for


v (t; x; y ) = e�r (T �t)



IE

f



maxt u T
f - 


t;x;y



(S (T ) - K )+



h



i



Y (u) < Lg



;



by replacing T, S (0) and Y (0) by T t, x and y respectively in the formula for v (0; S (0); Y (0)) .

          Now start at time 0 at S (0) and Y (0) . Using the Markov property, we can show that the stochastic
process



e�r t v (t; S (t); Y (t))



is a martingale under



IP . We compute



f;



�r t



d



h



e



�r t



v (t; S (t); Y (t))



�r v + v








i



t



+



= e







S



vxx



+ ��



S Y vxy



+







Y



vy y







dt



+ r S v



x



+ r Y vy







+ ��



S vx



q




- 


Y vy



d



B

e



B



+







S vx



dB

e



+ 


d



B

e




 


244





_L_



|Col1|y|
|---|---|
||_v(t, x, L) = 0, x >= 0_|
|||
|||


_v(t, 0, 0) = 0_



_x_



Figure 24.1: _Boundary conditions for barrier option. Note that_ t [0; T ] _is fixed._


Setting the dt term equal to 0, we obtain the PDE



r v + vt




+ r xv



x



+



+ ��







x



vxx



+ r y vy







xy vxy



+







y



vy y



= 0;

0 - t < T ; x - 0; 0 - y - L:



The terminal condition is


v (T ; x; y ) = (x            - K )+


and the boundary conditions are



; x - 0; 0 - y < L;



v (t; 0; 0) = 0; 0   - t   - T ;

v (t; x; L) = 0; 0 - t - T ; x - 0:


CHAPTER 24. An outside barrier option 245


x = 0 y = 0



r v + vt




+ r y vy



+



+



vy y



= 0 r v + vt

    


+ r xvx



+ r xv







vxx



= 0







y



x



This is the usual Black-Scholes formula
in y .



This is the usual Black-Scholes formula
in x .



The boundary conditions are The boundary condition is



�r (T �t)



v (t; 0; L) = 0; v (t; 0; 0) = 0; v (t; 0; 0) = e



v (t; 0; L) = 0; v (t; 0; 0) = 0; v (t; 0; 0) = e� ( - ) (0 - K )+ = 0;

the terminal condition is the terminal condition is



(0 - K )



+



v (T ; 0; y ) = (0 - K )+



= 0; y - 0: v (T ; x; 0) = (x - K )+



; x - 0:



On the x = 0 boundary, the option value
is v (t; 0; y ) = 0; 0 y L:

      -       

**24.3** **The hedge**



On the y = 0 boundary, the barrier is irrelevant, and the option value is given by
the usual Black-Scholes formula for a European call.



After setting the dt term to 0, we have the equation



�r t



q




- 


d



h



e



�r t



v (t; S (t); Y (t))



��




S vx



= e



Y vy



d



B

e



i

+







S vx



d



B



e



B

e







;



+ 


d



where vx = vx (t; S (t); Y (t)), vy = vy (t; S (t); Y (t)), and B ; B ; S; Y are functions of t . Note

that



where v



x



e



B

e



= v



x



(t; S (t); Y (t)), v



y



= v



y



(t; S (t); Y (t)), and



B



;



S (t)

i



S (t) d



B




[�r S (t) dt + dS (t)]



d


d



e

h



h



�r t



�r t



e



q




- 


(t)

 


S (t) dB

e



:



(t) +







e

h



h



Y (t)

i



= e�r t


= e�r t


= e�r t


= e�r t



��









[�r Y (t) dt + d Y (t)]



Y (t) dB

e



Therefore,


d



h



e



�r t



i



= vx



d[e�r t



S ] + vy



(t):


d[e�r t



Y ]:



v (t; S (t); Y (t))



Let 


Let - (t) denote the number of shares of stock held at time t, and let - (t) denote the number of

“shares” of the barrier process Y . The value X (t) of the portfolio has the differential



(t) denote the number of shares of stock held at time t, and let 


dX = 


dS + 


d Y + r [X - 


S - 


Y ] dt:


246


This is equivalent to



d[e�r t



X (t)] = 


(t)d[e�r t



S (t)] + 


(t)d[e�r t



Y (t)]:



To get X (t) = v (t; S (t); Y (t)) for all t, we must have


X (0) = v (0; S (0); Y (0))


and









(t) = vx


(t) = vy



(t; S (t); Y (t));


(t; S (t); Y (t)):


### **Chapter 25**

# **American Options**

This and the following chapters form part of the course _Stochastic_ _Differential Equations for_ _Fi-_
_nance II._


**25.1** **Preview of perpetual American put**


dS = r S dt +              - S dB



Intrinsic value at time t : (K S (t))

        


+ :



Let L [0; K ] be given. Suppose we exercise the first time the stock price is L or lower. We define



�L



= min ft - 0; S (t) - Lg;



vL



(x) = IE e



�r 


L



(K - S (�



L



))



+



�r 


=



(



K x if x L,

 -  


(K - L)IE e



L if x - L:



The plan is to comute vL (x) and then maximize over L to find the optimal exercise price. We need

to know the distribution of �L [.]



The plan is to comute v



L



L [.]



**25.2** **First passage times for Brownian motion: first method**


(Based on the reflection principle)

Let B be a Brownian motion under IP, let x - 0 be given, and define


                - = min ft                 - 0; B (t) = xg:

- is called the _first passage time to_ x _._ We compute the distribution of - .


247


248


Define








|c value|Col2|Col3|
|---|---|---|
|_Intrinsi_|||
||||



_x_



Figure 25.1: _Intrinsic value of perpetual American put_



M (t) = max

0�u�t

From the first section of Chapter 20 we have



B (u):



(�



)



IP fM (t) dm; B (t) dbg =


Therefore,


IP fM (t)         - xg =


=


=



(m - b)



x

Z


x

Z


x

Z



p



p - t


p - t









m

t



(m - b)

t



dm db; m - 0; b < m:



exp



t




 - t



)



Z�m



(m - b)



p



(�



(m - b)

t



(m - b)



exp



db dm



t




 - t



















b=m


b=�



)



exp

(


exp

(



(m - b)

t



(m - b)



dm



)



We make the change of variable z =



pmt [in the integral to get]



)



dm:


dz :



=



x=pt p 
Z



exp



z

(�



Now




- - t() M (t) - x;


CHAPTER 25. American Options 249


so



IP f� dtg =


=


=



@

IP  - t dt

@ t f - g

@

IP M (t) x dt

@ t f - g



@

" @ t



pt



pt



x=

Z



#



dz

)



exp (�



p 


dt



@

@ t



z





x



t



p 


= 


(�



( 


:



p







dt



x

t


x

t



)

)



exp


exp



=



t



p



x



dt:




 - t



We also have the Laplace transform formula



IE e���



IP f� dtg



=



Z



e��t



0



p



; - - 0: (See Homework)



�x




 


= e



Reference: Karatzas and Shreve, Brownian Motion and Stochastic Calculus, pp 95-96.


**25.3** **Drift adjustment**


Reference: Karatzas/Shreve, _Brownian motion and Stochastic Calculus_, pp 196–197.

For 0 t <, define

  


B (t) = - t + B (t);



e



Z (t) = exp f�� B (t) 


tg;

tg;



= exp f��



B (t) +









Define



B (t) +

e



�~ = min ft - 0;



B (t) = xg:



e



We fix a finite time T and change the probability measure “only up to T ”. More specifically, with



T fixed, define



IP (A) =



Z



Z (T ) dP ; A F (T ):



A



Under



IP, the process



f



B (t); 0 t T, is a (nondrifted) Brownian motion, so

  -   


e



IP f�~ dtg = IP f� dtg



f



f



=



)



t



p



x



x

t



dt; 0 < t - T :



exp



(�




 - t


250


For 0 < t T we have

   

IP f�~          - tg = IE



f�~�tg

i







t



IE



IfE

IfE

IfE

IfE


t

f











F (�~ ^ t)







T g


 

 


i

T g



i



IE



Z (T )

expf�



B (T ) 


B (T ) 






e



e







expf�



B (�~ ^ t) 


xe



IE







i



��



IE



IE

f



expf�



(�~ ^ t)g



IE







�~g



i



f�~�tg


f�~�tg


f�~�tg


f�~�tg


f�~�tg



expf� x 


Z



h


h


h

th



t



t


t



sg



f



IP f�~ dsg







0



exp f� x 


x



ds

)



0

Z


0

Z



x



p



x

s





(

(




- x 






(x - - s)

s



(x - - s)



s 


exp


exp



s


s




 - s




 - s


exp



)



p



(x - - t)

t



ds:



Therefore,



=


=


=


=


=


=


=


=


IP f�~ dtg =



)



dt; 0 < t - T :



x



p



(�




 - t



Since T is arbitrary, this must in fact be the correct formula for all t - 0 .


**25.4** **Drift-adjusted Laplace transform**


Recall the Laplace transform formula for


                - = minft                 - 0; B (t) = xg

for nondrifted Brownian motion:



)



x



IE e���



; - - 0; x - 0:



=



0

Z



t



p



x

�t

(� - t



dt = e�xp




 


exp




 - t



For



�~ = min ft - 0; - t + B (t) = xg;


CHAPTER 25. American Options 251


the Laplace transform is



dt




x

t



)



x



IE e���~



=


=



��t 

��t 


x

t



0

Z


0

Z



t


t



p



p



(x - - t)

t



t

)

)




 - t




 - t



+ x� 


x



exp


exp



(

(



p



x



= ex�



Z



( �(� +



dt


dt



)t 


exp








 - t



0



t



p



= ex� �x



�+�



; - - 0; x - 0;



where in the last step we have used the formula for IE e��� with - replaced by - +







.



If �~(! ) <, then


��~(! )

if �~(! ) =, then e�


Therefore,



��~(! )

e�



lim

- 0
#



= 0 for every - - 0, so



��~(! )

e�



lim

- 0
#



lim



lim

- 0
#



��~(! )

e�



=



= ;


= 0:


�~< :



Letting - 0 and using the Monotone Convergence Theorem in the Laplace transform formula
#



IE e���~



= ex� �xp



we obtain


If - 0, then

 

If - < 0, then


(Recall that x - 0 ).



IP f�~ < g = ex� �xp



�+�


= e




 


;


x� �xj� j



:



IP f�~ < g = :



IP f�~ < g = e x�



< :



**25.5** **First passage times:** **Second method**


(Based on martingales)

Let - - 0 be given. Then



Y (t) = exp f� B (t) 






tg


252


is a martingale, so Y (t - ) is also a martingale. We have
^



= Y (0 ^ - )



= IE Y (t ^ - )







= IE expf� B (t ^ - ) 






(t ^ - )g:



= lim



IE expf� B (t ^ - ) 


(t ^ - )g:



t!



We want to take the limit inside the expectation. Since



0 - exp f� B (t ^ - ) 






(t ^ - )g - e



x



;



this is justified by the Bounded Convergence Theorem. Therefore,



= IE lim



expf� B (t ^ - ) 


(t ^ - )g:



t!







There are two possibilities. For those ! for which - (! ) <,









:







tg = 0:



lim




     - x

(t ^ - )g = e 


t!



expf� B (t ^ - ) 






For those ! for which - (! ) =,



exp f� B (t ^ - ) 


exp f� x 






(t - ) lim
^ g  - t

!



Therefore,



lim

t!



= IE lim



exp f� B (t ^ - ) 


(t ^ - )g



t!








- <

  


= IE








- x�



e



= IE e� x�








- 

 
;




- to be zero if - = .







where we understand e




- x�



p




 - . We have again derived the Laplace transform formula



Let - =







, so - =



e�xp 


= IE e���



; - - 0; x - 0;



for the first passage time for nondrifted Brownian motion.


**25.6** **Perpetual American put**


dS = r S dt +           - S dB


S (0) = x



S (t) = x expf(r 


)t + - B (t)g






 









>>



>>

<



t + B (t)



:










>>



>>

;





;






r






<



= x exp


















>>



>>

=





=


















>>



>>

:





:




   
| {z }


CHAPTER 25. American Options 253



Intrinsic value of the put at time t : (K S (t))+ .

          
Let L [0; K ] be given. Define for x L,

          


�L = min t 0; S (t) = L

f     - g

= minft  - 0;  - t + B (t) =



log




L

x



g

x

L



g



= minft - 0; �� t - B (t) =






 

:



x

L



p r + 


p



Define



= (K - L)IE e

= (K - L) exp











vL



�r 


L












 














x

L



log


log



log







p



r +�



x

L

 






= (K       - L)


We compute the exponent










v








- - =

  

- r + 


r




= 

= 

= 

= 

= 

= 


r



r



r



r


r


r

























+


+


+


+


+


:

















r




=



p r + 


s

s

s

s




r +


r +





r




r




+ r + 


=







r




+ - =

  


+ - =



Therefore,



<



(K - x); 0 - x - L;



(K - L)



; x - L:



L



(x) =








- r =�



x

L








- r =�



; are all of the form C x



:



The curves (K L)

    






.



x

L








- r =�



We want to choose the largest possible constant. The constant is



r =�

C = (K - L)L



;


254











|ue|Col2|Col3|
|---|---|---|
|_val_|_-2_<br>_K - x_<br>_(K - L) (x/L)_|_-2_<br>_K - x_<br>_(K - L) (x/L)_|
||||


_x_



Figure 25.2: _Value of perpetual American put_


_-2r/_ σ [2]
_C3_ _x_

_-2r/_ σ [2]
_C2_ _x_

_-2r/_ σ [2]
_C1_ _x_

_Stock price_ _x_


Figure 25.3: _Curves._


CHAPTER 25. American Options 255


and



@ C

@ L



= �L



r




r



r

+ (K L)L

 -  


r




r







L






:



r




r




- +



r




(K - L)




 










r




r












:



r




K

L



+



r




+



We solve


to get


Since 0 < r < 


+ r; we have



K

L



= L


= L


= 0



r


 










+



+



r




L =







r K

+ r



0 < L < K :

Solution to the perpetual American put pricing problem (see Fig. 25.4):







;



v (x) =



<



(K - x); 0 - x - L



(K - L



; x - L







;








- r =�







)



L�



x







where


Note that


We have



:



L� =







r K

:

+ r







0



(x) =



(




- ; 0 - x < L







r







;



v



x




- r =�















r =�







(L



)



; x - L



:



(K - L)




 

0 (x):







r



r



r




L�



lim



0



(K - L�



)



x#L



v



K 







0 (x) = 

=  

=  


r K

+ r




- + r

r K











+ r - r







+ r

r





!



+ r



= 


= lim



0



x"L



v






256









_-2r/_ σ [2]

|ue|Col2|Col3|
|---|---|---|
|_val_|_K - x_<br>_(K - L )(x/L )_<br>_*_<br>_*_|_K - x_<br>_(K - L )(x/L )_<br>_*_<br>_*_|
||||



_x_



Figure 25.4: _Solution to perpetual American put._


**25.7** **Value of the perpetual American put**



Set


If 0 x < L

 

where


If 0 x < L

 



- =



r

; L�




=



r K

- + r



=




 
- +



K :




-, then v (x) = K - x . If L







x <, then








)�



�� (7.1)



v (x) = (K - L



)(L�



x



C

I|E x e�{zr - (K }







C



; (7.2)



x



h



e



�r 


(K - L



= IE



)+



f� <g



i



S (0) = x (7.3)



: (7.4)
g




-, then




- = min ft - 0; S (t) = L�



0



(x) +







x



v



00



(x) = �r (K - x) + r x(�) = �r K :



If L







�r v (x) + r xv 0



�r v (x) + r xv 0

x <, then




0



�r v (x) + r xv 0



�� 






(x) +







x



v



00



(x)



��




- r x� x







= C [�r x







]



x




- (�� - )x



�� 


��



= C x




[�r - r - 



- (�� - )]




 


= C (�� - )x��

= 0:



r 










r







��



In other words, v solves the _linear complementarity problem:_ (See Fig. 25.5).


CHAPTER 25. American Options 257



K



**@**



v



**@**



@@



@@



@

@



@



@



@@







@@



L K




   
x


Figure 25.5: _Linear complementarity_



For all x IR, x = L




-,



r v - r xv 0







0; (a)




v - (K - x)



+







x



v 00



; (b)



One of the inequalities (a) or (b) is an equality. (c)



The half-line [0; ) is divided into two regions:



+



C = fx; v (x) - (K - x)



0








- 0g;



S = fx; r v - r xv 0







x



g;



v



00



and L� is the boundary between them. If the stock price is in C, the owner of the put should not

exercise (should “continue”). If the stock price is in S or at L�, the owner of the put should exercise



and L



exercise (should “continue”). If the stock price is in S or at L�, the owner of the put should exercise

(should “stop”).



**25.8** **Hedging the put**


Let S (0) be given. Sell the put at time zero for v (S (0)) . Invest the money, holding �(t) shares of
stock and consuming at rate C (t) at time t . The value X (t) of this portfolio is governed by


dX (t) = �(t) dS (t) + r (X (t)       - �(t)S (t)) dt       - C (t) dt;


or equivalently,



d(e�r t X (t)) = �e�r t



C (t) dt + e�r t �(t)� S (t) dB (t):


258


The discounted value of the put satisfies



e




+ e



�r t




- S (t)v



0



(S (t)) dB (t)



v (S (t))

   






= e�r t



hr t



�r v (S (t)) + r S (t)v



0



(S (t))

i



00



(S (t)) +



d



�r t







S



(t)v



dt



= �r K e�r t



0



fS (t)<L�



fS (t)<L



g



dt + e�r t




- S (t)v



(S (t)) dB (t):



We should set



C (t) = r K



fS (t)<L�



;

g



0



�(t) = v



(S (t)):



**Remark 25.1** If S (t) < L�, then



0



v (S (t)) = K - S (t); �(t) = v



(S (t)) = - :



To hedge the put when S (t) < L�, short one share of stock and hold K in the money market. As

long as the owner does not exercise, you can consume the interest from the money market position,
i.e.,



C (t) = r K



fS (t)<L�



fS (t)<L



g



:



Properties of e



�r t v (S (t)) :



1. e


2. e

3. e



�r t


�r t


�r t



v (S (t)) is a supermartingale (see its differential above).



�r t



(K - S (t))



+, 0 t < ;

  


v (S (t)) - e



v (S (t)) is the smallest process with properties 1 and 2.



**Explanation of property 3.** Let Y be a supermartingale satisfying



Y (t) - e�r t



(K - S (t))+



(K - S (t))



; 0 t < : (8.1)

  


Then property 3 says that



Y (t)            - e�r t v (S (t)); 0            - t < : (8.2)

We use (8.1) to prove (8.2) for t = 0, i.e.,


Y (0) v (S (0)): (8.3)

            
If t is not zero, we can take t to be the initial time and S (t) to be the initial stock price, and then
adapt the argument below to prove property (8.2).

**Proof of (8.3), assuming** Y **is a supermartingale satisfying (8.1)** :



**Case I:** S (0) - L�



: We have



= v (S (0)):



Y (0) 


(K - S (0))



+



(: )

|{z}



(: )


CHAPTER 25. American Options 259



**Case II:** S (0) - L




- : For T - 0, we have



Y (0) IE Y (� T ) (Stopped supermartingale is a supermartingale)

  - ^




     - IE

Now let T to get
!



h



Y (� ^ T ) f� <g



Y (� ^ T )



i



: (Since Y 0 )

    


i (Fatou’s Lemma)



i



Y (0) lim

  - T



h



Y (� ^ T ) f� <g



T !



IE




- IE



h



Y (� )



f� <g



(K - S (� )



f� <g




- IE



e�r 


L�

| {z }



)



+



(by 8.1)



L







= v (S (0)): (See eq. 7.2)



**25.9** **Perpetual American contingent claim**


Intinsic value: h(S (t)) .

Value of the American contingent claim:



e�r 


h(S (� ))�



;



v (x) = sup

      


v (x) = sup



x



IE







where the supremum is over all stopping times.



Optimal exercise rule: Any stopping time - which attains the supremum.

**Characterization of** v **:**



1. e


2. e


3. e



�r t


�r t


�r t



v (S (t)) - e�r t h(S (t)); 0 < t < ;

v (S (t)) is the smallest process with properties 1 and 2.



v (S (t)) is a supermartingale;



**25.10** **Perpetual American call**



(S (� ) - K )+



e�r 






v (x) = sup

      


x



IE







**Theorem 10.63**



v (x) = x x - 0:


260


**Proof:** For every t,



K :


�r t



x


x


x



e�r t


e�r t

�r t



�r t



S (t)



K



v (x) - IE

  - IE

= IE



h

h

h



e



(S (t) - K )+



(S (t) - K )



i



it



�r t



= x - e




 - e

i



Let t to get v (x) x .
!  
Now start with S (0) = x and define


Then:



Y (t) = e



S (t):



1. Y is a supermartingale (in fact, Y is a martingale);



2. Y (t) e

   


�r t



(S (t) - K )+



; 0 t < .

  


Therefore, Y (0) v (S (0)), i.e.,

     
x                - v (x):


**Remark 25.2** No matter what - we choose,







e�r 


(S (� ) - K )+







S (� )�




- x = v (x):



< IE x



e�r 


IE



x



There is no optimal exercise time.







**25.11** **Put with expiration**


Expiration time: T - 0 .



+
.



Intrinsic value: (K S (t))

     
Value of the put:



Intrinsic value: (K S (t))

     


v (t; x) = (value of the put at time t if S (t) = x )



(K - S (� ))+



= sup



IE



x e�r (� �t)



:



t�� �T

| {z }




- : stopping time



See Fig. 25.6. It can be shown that v ; vt; vx [are] [continuous across the] [boundary, while] vxx [has] [a]

jump.



See Fig. 25.6. It can be shown that v ; v



; v



t



x [are] [continuous across the] [boundary, while] v



Let S (0) be given. Then


CHAPTER 25. American Options 261


x



v - K - x



�r v + v



x



= 0


= �r K



t



+ r xv



x



+







K



v (T ; x) = 0; x - K


v (T ; x) = K - x; 0 - x - K



t



L�



v = K - x



= - ; v



x







vxx


vxx



v



t



= 0; v



xx



= 0



r v + vt




+ r xv



x



x



+



T



Figure 25.6: _Value of put with expiration_



1. e


2. e


3. e



�r t


�r t


�r t



v (t; S (t)); 0 t T ; is a supermartingale;

    -     


v (t; S (t)) is the smallest process with properties 1 and 2.



v (t; S (t)) - e�r t



(K - S (t))+



(K - S (t))



; 0 t T ;

  -  


**25.12** **American contingent claim with expiration**


Expiration time: T - 0 .

Intrinsic value: h(S (t)) .

Value of the contingent claim:



h(S (� )):



v (t; x) = sup

t�� �T



IE



x



e�r (� �t)



Then



r v - v



x



vxx



0; (a)




t




- r xv



x











v h(x); (b)

                   At every point (t; x) [0; T ] [0; ), either (a) or (b) is an equality. (c)

        


**Characterization of** v **:** Let S (0) be given. Then


262


1. e


2. e


3. e



�r t


�r t


�r t



v (t; S (t)) - e�r t h(S (t)) ;

v (t; S (t)) is the smallest process with properties 1 and 2.



v (t; S (t)); 0 t T ; is a supermartingale;

    -    


The optimal exercise time is


              - = min ft              - 0; v (t; S (t)) = h(S (t))g

If - (! ) =, then there is no optimal exercise time along the particular path ! .


### **Chapter 26**

# **Options on dividend-paying stocks**

**26.1** **American option with convex payoff function**


**Theorem 1.64** _Consider the stock price process_


dS (t) = r (t)S (t) dt +           - (t)S (t) dB (t);

_Letwhere_ h(xr) _andbe_ _a_ - _convexare_ _processesfunctionandof_ xr (�t) 0� _,_ _and_ 0; _assume_ 0 - th(0)� T=; _a.s._ 0 _._ _(E.g.,This_ _stock_ h(x) = _pays_ (x _no_ - K _dividends._ )+ _)._ _An_

_American_ _contingent_ _claim_ _paying_ h(S (t)) _if_ _exercised_ _at_ _time_ t _does_ _not_ _need_ _to_ _be_ _exercised_
_before expiration, i.e., waiting until expiration to decide whether to exercise entails no loss of value._


**Proof:** For 0 - and x 0, we have

    -    -    


h(�x) = h(( - �)0 + �x)




- ( - �)h(0) + �h(x)



= �h(x):



Let T be the time of expiration of the contingent claim. For 0 t T,

                -                 


t

Z



r (u) du

)



T




- (t)

- (T )







= exp



(�







and S (T ) 0, so

   


0 

h



S (T )

  







- (t)

- (T )




- (t)

- (T )



h(S (T )): (*)



Consider a European contingent claim paying h(S (T )) at time T . The value of this claim at time

t [0; T ] is




- (T )


263







X (t) = - (t) IE







h(S (T ))



:











F (t)










264


Therefore,















(x; h(x))



�r

[.]



r

**.** **[.........................................................]** [.]



r



















�h(x)


h(�x)




          
         
�r

        
        
       - (x; h

       
      
**....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** . . **...** . **....** . **....** . **....** . **....** .   - **.** r

     
     
    
**....** **....** **....** **....** **....** **....** **....** **....** **....** **....**   - **....** **....**   - **....** **....** . . **...** . **....** . **....** . **....** . **....** . **.** r h

   
  
  
 
**.....** - **[.........................................................................................................................................]** - **.** **[...................]** [.] **[..]** [..] **[....]** [.] **[....]** [.] **[....]** [.] **[.]** [.] **.** **[.........................................................]** [.] 


**....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** . . **...** . **....** . **....** . **....** . **....** . **.** [.] r







**.** r


**.** r

**.** **[...................]** [.] **[..]** [..] **[....]** [.] **[....]** [.] **[....]** [.] **[.]** [.]



r




- **.** r

**[.]** [.]











r







**....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** **....** . . **...** . **....** . **....** . **....** . **....** . [..] **.** r



h




- **....**




- **....** **....**




























- x



Figure 26.1: _Convex payoff function_



X (t)

- (t)



=






=


=







F (t)




- (t)


- (t)


- (t)


- (t)


- (t)



h(S (t)):



h




 - (t)

- (T )



h(S (T ))



IE


IE








































(t) (by (*))
F

  







 - (t)

- (T )



S (T )



�� (Jensen’s inequality)



















S







S (T )

- (T )

- (



F (t)



h


h









- (t) IE




- (t)







S (t)

- (t)




- [is a martingale)]



This shows that the value X (t) of the European contingent claim dominates the intrinsic value

h(S (t)) of the American claim. In fact, except in degenerate cases, the inequality


X (t)         - h(S (t)); 0         - t         - T ;

is strict, i.e., the American claim should not be exercised prior to expiration.


**26.2** **Dividend paying stock**


Let r and - be constant, let - be a “dividend coefficient” satisfying


0 <                  - < :


CHAPTER 26. Options on dividend paying stocks 265


Let T - 0 be an expiration time, and let t (0; T ) be the time of dividend payment. The stock

price is given by



( - - )S (t







)t + - B (t)g; 0 - t - t



;



S (t) =



(



S (0) expf(r 






) + - (B (t) - B (t



))g; t



< t - T :



) expf(r 


)(t - t



Consider an American call on this stock. At times t (t ; T ), it is not optimal to exercise, so the

value of the call is given by the usual Black-Scholes formula



(T - t; x)) - K e�r (T �t)



v (t; x) = xN (d+



N (d

  


(T - t; x)); t



where


At time t


At time t


where



+ (T - t)(r - 


< t - T ;


:







p



x

K



=)







d

 


(T - t; x) =







log



T - t




[, immediately] _[ after]_ [ payment of the dividend, the value of the call is]



v (t



; ( - - )S (t



)):




[, immediately] _[ before]_ [ payment of the dividend, the value of the call is]



w (t ; S (t ));



; v (t



:



w (t


**Theorem 2.65** _For_ 0 t t

      -      


; x) = max







(x - K )



+



; ( - - )x








_[, the value of the American call is]_ w (t; S (t)) _, where_



e



�r (t



�t) w (t



w (t; x) = IE



t;x



h



)) :

i



; S (t



_This function satisfies the usual Black-Scholes equation_



r w + wt




+ r xwx



+



; x - 0;







x



wxx = 0; 0 t t

    -     


_(where_ w = w (t; x) _) with terminal condition_



w (t


_and boundary condition_


_The hedging portfolio is_



; x) = max �(x - K )+



; v (t



; ( - - )x)� ; x - 0;



w (t; 0) = 0; 0 - t - T :



�(t) =

(



vx



wx



;



< t - T :



(t; S (t)); 0 - t - t



(t; S (t)); t



**Proof:** We only need to show that an American contingent claim with payoff w (t



)) at time




[need not be exercised before time] t



; S (t



t




[. According to Theorem 1.64, it suffices to prove]



1. w (t



; 0) = 0,


266


2. w (t ; x) is convex in x .


Since v (t ; 0) = 0, we have immediately that



; v (t



w (t



; 0) = max







(0 - K )



+



; ( - - )0)



= 0:



To prove that w (t



; x) is convex in x, we need to show that v (t



; ( - )x) is convex is x . Obviously,

 






(x K )+ is convex in x, and the maximum of two convex functions is convex. The proof of the

 
convexity of v (t ; ( - )x) in x is left as a homework problem.



(x - K )



; ( - )x) in x is left as a homework problem.

 


**26.3** **Hedging at time** t



Let x = S (t



) .



**Case I:** v (t ; ( - )x) (x K )+ .

    -     -     
The option need not be exercised at time t



**Case I:** v (t



; ( - - )x) - (x - K )



The option need not be exercised at time t [(should not be exercised if the inequality is strict).] [We]

have



w (t



; x) = v (t



; ( - - )x);



�(t



) = wx



(t



; x) = ( - - )v



x



(t



; ( - - )x) = ( - - )�(t



+);



where



�(t



+) = lim



t#t



�(t)



is the number of shares of stock held by the hedge immediately after payment of the dividend. The
post-dividend position can be achieved by reinvesting in stock the dividends received on the stock
held in the hedge. Indeed,



�(t



+) =




- 


) = �(t



) +


)





�(t )

- 


�(t



)S (t



= �(t



) +




- �(t



( - - )S (t



)



dividends received
= # of shares held when dividend is paid +
price per share when dividend is reinvested



**Case II:** v (t ; ( - )x) < (x K )+ .

     -     
The owner of the option should exercise before the dividend payment at time t



**Case II:** v (t



; ( - - )x) < (x - K )



The owner of the option should exercise before the dividend payment at time t [and receive] (x K ) .

                        The hedge has been constructed so the seller of the option has x K before the dividend payment

                 at time t [. If the option is not exercised, its value drops from] x K to v (t ; ( - )x), and the seller



at time t [. If the option is not exercised, its value drops from] x K to v (t ; ( - )x), and the seller

                -                 
of the option can pocket the difference and continue the hedge.




[. If the option is not exercised, its value drops from] x K to v (t

              

### **Chapter 27**

# **Bonds, forward contracts and futures**

Let W (t); (t); 0 t T be a Brownian motion (Wiener process) on some (�; ; P) . Conf F  -  - g F
sider an asset, which we call a stock, whose price satisfies


dS (t) = r (t)S (t) dt +           - (t)S (t) dW (t):


Here, r and - are adapted processes, and we have already switched to the risk-neutral measure,
which we call IP . Assume that every martingale under IP can be represented as an integral with
respect to W .

Define the accumulation factor



r (u) du

   


�Z




- (t) = exp



t


0



:



A zero-coupon bond, maturing at time T, pays 1 at time T and nothing before time T . According
to the risk-neutral pricing formula, its value at time t [0; T ] is







B (t; T ) = - (t) IE




- (T )





















F (t)

  


F (t)



(




 
 


r (u) du

)



= IE


= IE





"




- (t)

- (T )



exp




 
 



 


















F (t)#



T




 



 






t

Z



:



Given B (t; T ) dollars at time t, one can construct a portfolio of investment in the stock and money


267


268


market so that the portfolio value at time T is 1 almost surely. Indeed, for some process -,



B (t; T ) = - (t) IE








- (T )



















F (t)
















 


Z



t



= - (t)


= - (t)



| martingale {z }








B (0; T ) +



IE




- (T )



+



0




- (u) dW (u)

      






t


0



Z



Z




- (u) dW (u)



;







t



dB (t; T ) = r (t)� (t)



B (0; T ) +




- (u) dW (u)



dt + - (t)� (t) dW (t)



0



= r (t)B (t; T ) dt + - (t)� (t) dW (t):



The value of a portfolio satisfies


dX (t) = �(t) dS (t) + r (t)[X (t)        - �(t)S (t)]dt

= r (t)X (t) dt + �(t)� (t)S (t) dW (t):


We set



(*)



�(t) =




- (t)� (t)

:

- (t)S (t)



If, at any time t, X (t) = B (t; T ) and we use the portfolio �(u); t u T, then we will have

                  -                  

X (T ) = B (T ; T ) = :


If r (t) is nonrandom for all t, then



B (t; T ) = exp (�



t

Z



r (u) du

)



T



;



dB (t; T ) = r (t)B (t; T ) dt;


i.e., - = 0 . Then - given above is zero. If, at time t, you are given B (t; T ) dollars and you always
invest only in the money market, then at time T you will have



( t

Z



T



r (u) du

)



B (t; T ) exp



= :



If r (t) is random for all t, then - is not zero. One generally has three different instruments: the
stock, the money market, and the zero coupon bond. Any two of them are sufficient for hedging,
and the two which are most convenient can depend on the instrument being hedged.


CHAPTER 27. Bonds, forward contracts and futures 269


**27.1** **Forward contracts**


We continue with the set-up for zero-coupon bonds. The T _-forward_ _price_ of the stock at time

t [0; T ] is the (t) -measurable price, agreed upon at time t, for purchase of a share of stock at
F
time T, chosen so the forward contract has value zero at time t . In other words,





















F (t)

  


IE








- (T )



(S (T ) - F (t))



= 0; 0 - t - T :



We solve for F (t) :


This implies that



=


F (t) =



0 = IE


= IE









- (T )

S (T )

- (T )



F (t)



(S (T ) - F (t))



















F (t)




 







 


















F (t)

  



- (t)

- (T )




 






F (t)

- (t)




 


I�



B (t; T ):



IE











F (t)

- (t)



S (t)

- (t)



S (t)

B (t; T )



:



**Remark 27.1 (Value vs. Forward price)** The T -forward price F (t) is _not_ the value at time t of
the forward contract. The value of the contract at time t is zero. F (t) is the price agreed upon at
time t which will be paid for the stock at time T .


**27.2** **Hedging a forward contract**



Enter a forward contract at time 0, i.e., agree to pay F (0) = BS(0(0);T ) [for a share of stock at time] T .

At time zero, this contract has value 0. At later times, however, it does not. In fact, its value at time



Enter a forward contract at time 0, i.e., agree to pay F (0) =



S (0)



t [0; T ] is







V (t) = - (t) IE


=  - (t) IE









- (T )

S (T )

- (T )



F (t)



(S (T ) - F (0))





















F (t)











F (t)

  

















- (t)

- (T )


















- F (0) IE











S (t)

- (t)




- F (0)B (t; T )



= - (t)



= S (t) - F (0)B (t; T ):



This suggests the following hedge of a short position in the forward contract. At time 0, short F (0)



T -maturity zero-coupon bonds. This generates income



F (0)B (0; T ) =



S (0)

B (0; T )



B (0; T ) = S (0):


270


Buy one share of stock. This portfolio requires no initial investment. Maintain this position until
time T, when the portfolio is worth


S (T )          - F (0)B (T ; T ) = S (T )          - F (0):

Deliver the share of stock and receive payment F (0) .

A short position in the forward could also be hedged using the stock and money market, but the
implementation of this hedge would require a term-structure model.


**27.3** **Future contracts**


Future contracts are designed to remove the risk of default inherent in forward contracts. Through
the device of _marking to market_, the value of the future contract is maintained at zero at all times.
Thus, either party can close out his/her position at any time.

Let us first consider the situation with discrete trading dates



< t



< : : : < tn



= T :



On each [t



j



0 = t0


), r is constant, so



; tj +



r (u) du

   


tk +




- (tk +



) = exp


= exp





<

:



<



0

Z



j =0

X



r (tj )(tj +



k



tj




)



=

;



=



is (t
F



k [, taking the long position, when the future price is] �(t



k



) -measurable.



k



Enter a future contract at time t



) . At time



tk + [, when the future price is] �(tk + ), you receive a payment �(tk + ) �(tk ) . (If the price has

                   
fallen, you make the payment (�(tk + ) �(tk )) . ) The mechanism for receiving and making

        -         


k + [, when the future price is] �(t



), you receive a payment �(t



) - �(t



t



k +



k +



k



fallen, you make the payment (�(tk + ) �(tk )) . ) The mechanism for receiving and making

        -         
these payments is the _margin account_ held by the broker.



k +



) - �(t



k



By time T = tn [, you have received the sequence of payments]



�(tk +



) �(tk

 


); �(tk +



) �(tk + ); : : : ; �(tn

 


) - �(tn�



)



at times t



k +



; t



n [.] [The value at time] t = t0 [of this sequence is]



k +



; : : : ; t




- (t) IE



n�


j =k

X




- (tj +



))



















F (t)



:



)



(�(tj +



) �(tj

 


j =k



Because it costs nothing to enter the future contract at time t, this expression must be zero almost
surely.


CHAPTER 27. Bonds, forward contracts and futures 271


The continuous-time version of this condition is



T




- (t) IE



"



t

Z



Z




- (u)



F (t)



= 0; 0 - t - T :



d�(u)



















#



j



Note that - (tj + ) appearing in the discrete-time version is (tj ) -measurable, as it should be when

F

approximating a stochastic integral.



Note that - (t



j +



) appearing in the discrete-time version is (t
F



**Definition 27.1** The T _-future price_ of the stock is any (t) -adapted stochastic process
F

f�(t); 0                  - t                  - T g ;

satisfying


�(T ) = S (T ) a.s., and (a)



F (t)



= 0; 0 t T : (b)

   -   


IE



T

" t

Z




- (u)



d�(u)



















#



**Theorem 3.66** _The unique process satisfying (a) and (b) is_



�(t) = IE



S (T )

















F (t)



; 0 - t - T :












**Proof:** We first show that (b) holds if and only if - is a martingale. If - is a martingale, then



t


0




- (u)



R



d�(u) is also a martingale, so



= IE


= 0:



















t


 - (u)




- 0

Z



t



0

�Z



d�(u)



F (t)



IE



T

" t

Z




- (u)



d�(u)











F (t)











d�(u)



#








- (u)



On the other hand, if (b) holds, then the martingale



T



M (t) = IE



T


0




- (u)



F (t)



d�(u)



















#



satisfies


this implies



M (t) =


=


dM (t) =



"

Z


t



0

Z


0

Z




- (t)



d�(u) + IE

" t

Z



d�(u); 0 - t - T :




- (u)



d�(u)











F (t)











#



t




- (u)


- (u)



d�(t);



d�(t) = - (t) dM (t);


272


and so - is a martingale (its differential has no dt term).



Now define




 



 



 
 



 
 


�(t) = IE







S (T )



F (t)



; 0 - t - T :







Clearly (a) is satisfied. By the tower property, - is a martingale, so (b) is also satisfied. Indeed, this




- is the only martingale satisfying (a).



**27.4** **Cash flow from a future contract**


With a forward contract, entered at time 0, the buyer agrees to pay F (0) for an asset valued at S (T ) .
The only payment is at time T .

With a future contract, entered at time 0, the buyer receives a cash flow (which may at times be
negative) between times 0 and T . If he still holds the contract at time T, then he pays S (T ) at time

T for an asset valued at S (T ) . The cash flow received between times 0 and T sums to



Z



T


0



d�(u) = �(T ) - �(0) = S (T ) - �(0):



Thus, if the future contract holder takes delivery at time T, he has paid a total of


(�(0)               - S (T )) + S (T ) = �(0)

for an asset valued at S (T ) .


**27.5** **Forward-future spread**



Future price: �(t) = IE


Forward price:


Forward-future spread:



S (T )












F (t)












- .



=

 - (t)IE


S (0)







F (t) =



S (t)

B (t; T )



S (t)



:




- (T )



















F (t)







�(0) - F (0) = IE [S (T )] 



- (T )



i







IE (S (T )) - IE



h




- (T )







S (T )

- (T )

��



=















IE


IE



:



IE




- (T )







If




- (T ) [and] S (T ) are uncorrelated,



�(0) = F (0):


CHAPTER 27. Bonds, forward contracts and futures 273



If




- (T ) [and] S (T ) are positively correlated, then


�(0)                - F (0):



This is the case that a rise in stock price tends to occur with a fall in the interest rate. The owner
of the future tends to receive income when the stock price rises, but invests it at a declining interest
rate. If the stock price falls, the owner usually must make payments on the future contract. He
withdraws from the money market to do this just as the interest rate rises. In short, the long position
in the future is hurt by positive correlation between - (T ) [and] S (T ) . The buyer of the future is

compensated by a reduction of the future price below the forward price.


**27.6** **Backwardation and contango**


Suppose

dS (t) = �S (t) dt +            - S (t) dW (t):



Define - =



��r

 


;



W (t) = - t + W (t),



f



Z (T ) = expf�� W (T ) 






T g



IP (A) =



Z



A



Z (T ) dIP ; A F (T ):



Then



W is a Brownian motion under



f



f



IP, and



f



dS (t) = r S (t) dt + - S (t) d



W (t):

f



W (t):



We have


Because




- (T )




- (t) = er t

S (t) = S (0) expf(� 


)t + 


)t + - W (t)g



= S (0) expf(r 








W (t)g



f




- (T ) [are uncorrelated under]



IP . Therefore,

f



= e



�r T is nonrandom, S (T ) and



�(t) =



IE [S (T )



Ff(







F (t)]



= F (t)















=



S (t)

B (t; T )



= er (T �t)



S (t):



The expected future spot price of the stock under IP is




 
n



IE S (T ) = S (0)e�T



IE



exp

h







T + - W (T )

oi



= e�T S (0):


274


The future price at time 0 is



�(0) = er T



S (0):



If - - r, then �(0) < IE S (T ): This situation is called _normal backwardation_ (see Hull). If - < r,
then �(0) - IE S (T ) . This is called _contango._


### **Chapter 28**

# **Term-structure models**



Throughout this discussion, W (t); 0 t T
f            -            


is a Brownian motion on some probability space
g



(�; ; P), and F (t); 0 t T
F f  -  



 










is the filtration generated by W .
g



Suppose we are given an adapted _interest rate process_ fr (t); 0 - t - T - g . We define the accumu
lation factor



Suppose we are given an adapted _interest rate process_ r (t); 0 t T
f                      -                      






t




- (t) = exp







0

Z



r (u) du



; 0 - t - T







:



In a term-structure model, we take the zero-coupon bonds (“zeroes”) of various maturities to be the
primitive assets. We assume these bonds are default-free and pay $1 at maturity. For 0 t T

                       -                       -                       


B (t; T ) = price at time t of the zero-coupon bond paying $1 at time T .



T




-, let



**Theorem 0.67 (Fundamental Theorem of Asset Pricing)** _A_ _term structure model is free of arbi-_
_trage if and only if there is a probability measure_ IP _on_ - _(a risk-neutral measure) with the same_



_trage if and only if there is a probability measure_ IP _on_ - _(a risk-neutral measure) with the same_

_probability-zero sets as_ IP _(i.e.,_ equivalent _to_ IP _), such that for each_ T (0; T - ] _, the process_



f







] _, the process_



B (t; T )

 - (t)



; 0 - t - T ;



_is a martingale under_



IP _._



f



**Remark 28.1** We shall always have



dB (t; T ) = �(t; T )B (t; T ) dt + �(t; T )B (t; T ) dW (t); 0     - t     - T ;

for some functions �(t; T ) and �(t; T ) . Therefore







B (t; T )

 - (t)








- (t)




- (t)



d







= B (t; T ) d







+



dB (t; T )



dt + �(t; T )



= [�(t; T ) - r (t)]



B (t; T )




 - (t)


275



B (t; T )

 - (t)



dW (t);


276



so IP is a risk-neutral measure if and only if �(t; T ), the mean rate of return of B (t; T ) under IP, is
the interest rate r (t) . If the mean rate of return of B (t; T ) under IP is not r (t) at each time t and for
each maturity T, we should change to a measure IP under which the mean rate of return is r (t) . If



each maturity T, we should change to a measure IP under which the mean rate of return is r (t) . If

such a measure does not exist, then the model admits an arbitrage by trading in zero-coupon bonds.



f



**28.1** **Computing arbitrage-free bond prices: first method**


Begin with a stochastic differential equation (SDE)


dX (t) = a(t; X (t)) dt + b(t; X (t)) dW (t):


The solution X (t) is the _factor._ If we want to have n -factors, we let W be an n -dimensional
Brownian motion and let X be an n -dimensional process. We let the interest rate r (t) be a function
of X (t) . In the usual one-factor models, we take r (t) to be X (t) (e.g., Cox-Ingersoll-Ross, HullWhite).



Now that we have an interest rate process r (t); 0 t T
f                  -                  


Now that we have an interest rate process fr (t); 0 - t - T - g, we define the zero-coupon bond

prices to be







)



B (t; T ) = - (t) IE




- (T )







F (t)

   


r (u) du



"







(



















F (t)#



T







T




T




= IE



exp







t

Z



:



; 0 - t - T - T




 


We showed in Chapter 27 that



dB (t; T ) = r (t)B (t; T ) dt +         - (t)� (t) dW (t)


for some process - . Since B (t; T ) has mean rate of return r (t) under IP, IP is a risk-neutral measure
and there is no arbitrage.


**28.2** **Some interest-rate dependent assets**



**Coupon-paying bond:** Payments P



; P



; : : : ; Pn [at times] T



n [at times] T



; : : : ; Tn [. Price at time] t is



k :t<T
f X



B (t; Tk



B (t; T



; T


):



Pk



k g



**Call option on a zero-coupon bond:** Bond matures at time T . Option expires at time T < T .

Price at time t is




- (t) IE

    




















F (t)

  


; T ) - K )+



:




- (T



)



(B (T



; 0 - t - T


CHAPTER 28. Term-structure models 277


**28.3** **Terminology**


**Definition 28.1 (Term-structure** **model)** Any mathematical model which determines, at least theoretically, the stochastic processes


B (t; T ); 0           - t           - T ;



for all T (0; T



�] .



**Definition 28.2 (Yield to maturity)** For 0 t T T

            -            -            
(t) -measurable random-variable satisfying
F




-, the _yield_ _to_ _maturity_ Y (t; T ) is the



B (t; T ) exp f(T - t)Y (t; T )g = ;



or equivalently,


Determining


is equivalent to determining



B (t; T ); 0 - t - T - T


Y (t; T ); 0 - t - T - T



Y (t; T ) = 


T - t



log B (t; T ):




- ;


- :



**28.4** **Forward rate agreement**



Let 0 - t - T < T + - - T - be given. Suppose you want to borrow $1 at time T with repayment

(plus interest) at time T + -, at an interest rate agreed upon at time t . To synthesize a _forward-rate_
_agreement_ to do this, at time t buy a T -maturity zero and short B (t;T ) (T + �) -maturity zeroes.



Let 0 t T < T + - T

  -  -  


_agreement_ to do this, at time t buy a T -maturity zero and short BB(t;T(t;T+)�) (T + �) -maturity zeroes.

The value of this portfolio at time t is



B (t;T )



B (t;T +�)



B (t; T ) 


B (t; T )

B (t; T + �) = 0:

B (t; T + �)



At time T, you receive $1 from the T -maturity zero. At time T + -, you pay $



At time T, you receive $1 from the T -maturity zero. At time T + -, you pay $ BB(t;T(t;T+)�) [.] [The]

effective interest rate on the dollar you receive at time T is R(t; T ; T + �) given by



B (t;T )



B (t; T )

B (t; T + �)



= expf� R(t; T ; T + �)g;



or equivalently,


The _forward rate_ is



R(t; T ; T + �) = 


log B (t; T + �) - log B (t; T )

        


:



f (t; T ) = lim

       - 0
#



R(t; T ; T + �) = 


@

@ T



log B (t; T ): (4.1)


278


This is the instantaneous interest rate, agreed upon at time t, for money borrowed at time T .

Integrating the above equation, we obtain



T


t

Z



T


t

Z








f (t; u) du = 


@

log B (t; u) du

@ u








= - log B (t; u)



u=T


u=t



�;



;




= - log B (t; T );



so



(�



T



f (t; u) du

)



B (t; T ) = exp



t

Z



:



You can agree at time t to receive interest rate f (t; u) at each time u [t; T ] . If you invest $ B (t; T )
at time t and receive interest rate f (t; u) at each time u between t and T, this will grow to



( t

Z



f (t; u) du

)



T



B (t; T ) exp



=



at time T .


**28.5** **Recovering the interest** r (t) **from the forward rate**



(�



t

Z



















F (t)# ;



T



r (u) du

)



exp

"



"�r (T ) exp



r (u) du



)



(�



t

Z



F (t)#



@

@ T



B (t; T ) = IE


B (t; T ) = IE



T















;



@

@ T


On the other hand,


@

@ T







T =t























F (t)

  






B (t; T )



�r (t)
















= IE







= �r (t):



T =t



t

Z



T



f (t; u) du

)



B (t; T ) = exp



( 


;



t

Z



f (t; u) du ;

)



@

@ T



B (t; T ) = �f (t; T ) exp



T



(







B (t; T )



= �f (t; t):



Conclusion: r (t) = f (t; t) .














CHAPTER 28. Term-structure models 279


**28.6** **Computing** **arbitrage-free** **bond** **prices:** **Heath-Jarrow-Morton**
**method**



For each T (0; T �], let the forward rate be given by



0



Z



t



f (t; T ) = f (0; T ) +



t


0



�(u; T ) du +



Z




- (u; T ) dW (u); 0 - t - T :



Here �(u; T ); 0 u T and - (u; T ); 0 u T are adapted processes.
f   -   - g f   -   - g



In other words,



df (t; T ) = �(t; T ) dt + - (t; T ) dW (t):



Recall that


Now



(�



f (t; u) du

)



T



B (t; T ) = exp



t

Z



:



t

Z

T



t

Z



f (t; u) du

)



T



T



df (t; u) du



d



(�



= f (t; t) dt 


Z

"



= r (t) dt 

= r (t) dt 


t

Z




[�(t; u) dt + - (t; u) dW (t)] du



dt 


t



T



�(t; u) du

#



T




- (t; u) du

#



" t

Z



dW (t)



�� (t;T )

�| - (t; T ){zdt - �}




  -   - (t;T )

dW| (t): {z }







(t;T )








 






(t;T )











(t; T ) dt - 


(t; T ) dW (t):



Let


Then


and



B (t; T ) = g


dB (t; T ) = dg



= r (t) dt - 


g (x) = ex



0



(x) = ex



; g


;



; g



00 (x) = ex



:



T



f (t; u) du

!











t

Z



t

Z



T



f (t; u) du

!


f (t; u) du

!



(r dt - ��



t

Z



T



= g



0




 

+



00







f (t; u) du

!







t

Z



T



(�



)



dt - - 

dt



g



dW )


dt



= B (t; T )



r (t) - 



 


(t; T ) +



(�







(t; T ))



i







h




- 


(t; T )B (t; T ) dW (t):


280


**28.7** **Checking for absence of arbitrage**


IP is a risk-neutral measure if and only if



�� (t; T ) =







(�



(t; T ))



; 0 - t - T - T




- ;



i.e.,



T


t

Z




- (t; u) du

!



�(t; u) du =



t

Z



; 0 - t - T - T







: (7.1)



Differentiating this w.r.t. T, we obtain


�(t; T ) =           - (t; T )



t

Z



T


T




- : (7.2)



t




- (t; u) du; 0 - t - T - T



Not only does (7.1) imply (7.2), (7.2) also implies (7.1). This will be a homework problem.



Suppose (7.1) does not hold. Then IP is not a risk-neutral measure, but there might still be a riskneutral measure. Let f� (t); 0 - t - T - g be an adapted process, and define



be an adapted process, and define
g







t



W (t) =



0

Z



Z




- (u) du + W (t);



f




 


0

Z



t



Z (t) = exp




 




- (u) dW (u) 


Z



t


0



(u) du

  


):


(�


(�



) dIP A F (T







(t; T ))


(t; T ))



A

Z



Z (T




 


Then



IP (A) =

f



W (t); 0 - t - T :



rf(



dB (t; T ) = B (t; T )







(t; T ) +



i



+ 


dt



;


- (t; T )� (t)i



r (t) - 



- 






(t; T )B (t; T ) dW (t)









= B (t; T )



r (t) - 






(t; T ) +



dt



h

h




- 






(t; T )B (t; T ) d



In order for B (t; T ) to have mean rate of return r (t) under



IP, we must have



;f



�� (t; T ) =







(t; T )� (t); 0 - t - T - T







(�



(t; T ))



+ - 


: (7.3)



Differentiation w.r.t. T yields the equivalent condition



(t; T ) + - (t; T )� (t); 0 - t - T - T




 


�(t; T ) = - (t; T )�







: (7.4)



**Theorem 7.68 (Heath-Jarrow-Morton)** _For_ _each_ T (0; T



] _,_ _let_ �(u; T ); 0 - u - T ; _and_








- (u; T ); 0 - u - T _,_ _be_ _adapted_ _processes,_ _and_ _assume_ - (u; T ) - 0 _for_ _all_ u _and_ T _._ _Let_



f (0; T ); 0 - t - T




- _, be a deterministic function, and define_



0

Z



t



f (t; T ) = f (0; T ) +



Z



t


0



�(u; T ) du +




- (u; T ) dW (u):


CHAPTER 28. Term-structure models 281



_Then_ f (t; T ); 0 - t - T - T



_Then_ f (t; T ); 0 - t - T - T - _is a family of forward rate_ _processes for a term-structure model_

_without arbitrage if and only if there is an adapted process_ - (t); 0 - t - T - _, satisfying (7.3), or_



_without arbitrage if and only if there is an adapted process_ - (t); 0 - t - T - _, satisfying (7.3), or_

_equivalently, satisfying (7.4)._



**Remark 28.2** Under IP, the zero-coupon bond with maturity T has mean rate of return



r (t) - ��



(t; T ) +



(�







(t; T ))



and volatility 






(t; T ) . The excess mean rate of return, above the interest rate, is



���



(t; T ) +



(�







(t; T ))



;



and when normalized by the volatility, this becomes the _market price of risk_



���







(t; T ) +



(�







(t; T ))



:







(t; T )



The no-arbitrage condition is that this market price of risk at time t does not depend on the maturity

T of the bond. We can then set




- 


(t; T )




- (t) = - "



���



(t; T ) +



(� 


(t; T ))



#



;



and (7.3) is satisfied.

(The remainder of this chapter was taught Mar 21)

Suppose the market price of risk does not depend on the maturity T, so we can solve (7.3) for - .
Plugging this into the stochastic differential equation for B (t; T ), we obtain for every maturity T :



dB (t; T ) = r (t)B (t; T ) dt - - 


f



(t; T )B (t; T ) d



W (t):



Because (7.4) is equivalent to (7.3), we may plug (7.4) into the stochastic differential equation for



f (t; T ) to obtain, for every maturity T :



df (t; T ) = [� (t; T )� 


(t; T ) + - (t; T )� (t)] dt + - (t; T ) dW (t)



= - (t; T )�� (t; T ) dt + - (t; T ) dW (t):

f



**28.8** **Implementation of the Heath-Jarrow-Morton model**


Choose




- 


(t; T ); 0 - t - T - T




- ;




 



- (t); 0 - t - T



:


282


These may be stochastic processes, but are usually taken to be deterministic functions. Define







�(t; T ) = - (t; T )�



(t; T ) + - (t; T )� (t);



t



W (t) =



0

Z



Z




- (u) du + W (t);



f







t


0

Z



Z (t) = exp




- (u) dW (u) 


(u) du

  


;




 




 


t


0

Z

):



IP (A) =



A

Z



Z (T







) dIP A F (T



f



; be determined by the market; recall from equation (4.1):



Let f (0; T ); 0 T T

    -     






@

f (0; T ) =

   - @ T



log B (0; T ); 0 - T - T







:



Then f (t; T ) for 0 t T is determined by the equation

     -      


df (t; T ) =             - (t; T )��


this determines the interest rate process



W (t); (8.1)

f



(t; T ) dt + - (t; T ) d







r (t) = f (t; t); 0 - t - T



; (8.2)



and then the zero-coupon bond prices are determined by the initial conditions B (0; T ); 0 T

                        -                         


T




-, gotten from the market, combined with the stochastic differential equation



W (t): (8.3)



f



dB (t; T ) = r (t)B (t; T ) dt - 






(t; T )B (t; T ) d



Because all pricing of interest rate dependent assets will be done under the risk-neutral measure IP,

under which W is a Brownian motion, we have written (8.1) and (8.3) in terms of W rather than



Because all pricing of interest rate dependent assets will be done under the risk-neutral measure



f



W is a Brownian motion, we have written (8.1) and (8.3) in terms of



W rather than



f



f




-, and the process



W . Written this way, it is apparent that neither - (t) nor �(t; T ) will enter subsequent computations.

f f

The only process which matters is - (t; T ); 0 - t - T - T -, and the process




- (t; u) du; 0 - t - T - T 


T



(t; T ) =

t

Z



; (8.4)











obtained from - (t; T ) .



From (8.3) we see that 


(t; T ) is the volatility at time t of the zero coupon bond maturing at time







T . Equation (8.4) implies








 


: (8.5)







(T ; T ) = 0; 0 - T - T



This is because B (T ; T ) = and so as t approaches T (from below), the volatility in B (t; T ) must
vanish.

In conclusion, to implement the HJM model, it suffices to have the initial market data B (0; T ); 0

                         


; and the volatilities







T - T















(t; T ); 0 - t - T - T



:


CHAPTER 28. Term-structure models 283



We require that 






(t; T ) be differentiable in T and satisfy (8.5). We can then define




- (t; T ) =



@

@ T











(t; T );



and (8.4) will be satisfied because



@

@ u







T



(t; T ) - 










(t; t) =



t

Z











(t; T ) = 






(t; u) du:



We then let



W be a Brownian motion under a probability measure



f



IP, and we let B (t; T ); 0 t

       -        


T

f



T - T -, be given by (8.3), f where r (t) is given by (8.2) and f (t; Tf) by (8.1). In (8.1) we use the

initial conditions



T - T



f (0; T ) = 


@







@ T



log B (0; T ); 0 - T - T



:



**Remark 28.3** It is customary in the literature to write W rather than W and IP rather than IP,

so that IP is the symbol used for the risk-neutral measure and no reference is ever made to the

f f

market measure. The only parameter which must be estimated from the market is the bond volatility



**Remark 28.3** It is customary in the literature to write W rather than



W and IP rather than



f



f



(t; T ), and volatility is unaffected by the change of measure.










284


### **Chapter 29**

# **Gaussian processes**



**Definition 29.1 (Gaussian Process)** A _Gaussian process_ X (t), t 0, is a stochastic process with

                  the property that for every set of times 0 t t : : : tn [, the set of random variables]

           -           -           -           



- t




- : : : - t



n [, the set of random variables]



X (t



); X (t



); : : : ; X (tn



)



is jointly normally distributed.


**Remark 29.1** If X is a Gaussian process, then its distribution is determined by its _mean function_


m(t) = IE X (t)

and its _covariance function_



�(s; t) = IE [(X (s) - m(s)) - (X (t) - m(t))]:



Indeed, the joint density of X (t



); : : : ; X (tn



) is



IP fX (t



) dx



; : : : ; X (tn



) dxn



g



T

- (x - m(t))







=



(� )n= pdet 


exp



(x - m(t)) - ��



dx



: : : dxn



;


); m(t



); : : : ; m(tn



where - is the covariance matrix


        - =




 
n


�(t

�(t



: : : : : : : : : : : :



; tn )

; tn )



; t

; t



) �(t

) �(t



; t

; t



) : : : �(t

) : : : �(t



�(tn ; t



) �(tn ; t



) : : : �(tn



; tn



)



x is the row vector [x



)] .



; x



; : : : ; x



n



], t is the row vector [t



; : : : ; tn



], and m(t) = [m(t



; t



The moment generating function is



(



n







= exp



T

u - m(t)

n



+



T

u - - - u



k =

X



X (tk



uk



)

)



;



k =



where u = [u



; u



IE exp


; : : : ; u



n



] .



285


286


**29.1** **An example: Brownian Motion**


Brownian motion W is a Gaussian process with m(t) = 0 and �(s; t) = s t . Indeed, if 0 s t,
^                       -                       then



�(s; t) = IE [W (s)W (t)] = IE



h



W (s) (W (t) - W (s)) + W



(s)

i



= IE W (s):IE (W (t) - W (s)) + IE W



(s)



= IE W

= s ^ t:



(s)



To prove that a process is Gaussian, one must show that X (t



To prove that a process is Gaussian, one must show that X (t ); : : : ; X (tn ) has either a density or a

moment generating function of the appropriate form. We shall use the m.g.f., and shall cheat a bit
by considering only two times, which we usually call s and t . We will want to show that



n



); : : : ; X (t



#)



u

# "u



IE exp fu



X (s) + u



X (t)g = exp



u

(




[u




 
"�








m



+ u



m



+



u



]



:



**Theorem 1.69 (Integral w.r.t.** **a Brownian)** _Let_ W (t) _be_ _a_ _Brownian motion and_ - (t) _a_ _nonran-_
_dom function. Then_



t



X (t) =


_is a Gaussian process with_ m(t) = 0 _and_



0

Z




- (u) dW (u)



�(s; t) =



s^t


0

Z







(u) du:



**Proof:** (Sketch.) We have


Therefore,



dX = - dW:



deuX (s)


euX (s)



= ueuX (s) - (s) dW (s) +



= euX (0)



(s) ds;



u



euX (s) 


+



u







+ u



Z



s


0



euX (v )




- (v ) dW (v )



s


0

Z



euX (v )



(v ) dv ;



s



=


= e



dv ;



= +



u



Z



Martingale

s

| {zuX (v ) }







(v )IE e



uX (v )



0



d

ds



IE euX (s)


IE euX (s)


IE euX (s)



u







(s)IE euX (s)



;







uX (0)



exp







(v ) dv



s


0

Z







(v ) dv



:



u






- (1.1)



s



= exp







u



Z



0



This shows that X (s) is normal with mean 0 and variance



R



s


0







(v ) dv .


CHAPTER 29. Gaussian processes 287



Now let 0 s < t be given. Just as before,

   


uX (t)



= ue



uX (t)



u



(t) dt:




- (t) dW (t) +



euX (t)



de






t



Integrate from s to t to get



dW (v ) +



t

 - (v )euX (v )



euX (t) = euX (s)



+ u



Z



u



Z




 


(v )euX (v )



dv :



s



s



Take IE [: : : (s)] conditional expectations and use the martingale property
jF



dW (v )




- (v )euX (v )


IE









- 0

Z



= IE


= 0



0

�Z



t







t











s

 - (v )euX (v )

















F (s)








F (s)




- (v )euX (v )



dW (v )



IE



s

�Z



dW (v )











to get




 



 


F (s)


F (s)



F (s)

  


t



uX (v )



= euX (s) +




 
 



 
 



 



 



 



 


s

Z







(v )IE



e




 
 



 
 



 


u



dv




 


d

IE

dt








e


e



uX (t)


uX (t)




 



 



 



 


F (s)







euX (t)



; t - s:




 






(t)IE



=



u













The solution to this ordinary differential equation with initial time s is



e

 



 




















t



F (s)

  


exp







IE



uX (t)



s

Z




 


(v ) dv ; t s: (1.2)

    
  


= euX (s)



u



We now compute the m.g.f. for (X (s); X (t)), where 0 s t :

               -               






( 1.2 = ) e(u +u



t

 


��















F (s)

  






F (s)



)X (s)



IE



eu




X (s)+u X (t)



u



= eu



X (s)



IE



u



s



(v ) dv



;



e












X (t)


exp





















Z







= IE


= IE



IE




X (t)

i



X (s)+u



X (t)



F (s)



e




u



IE



eu

h



X (s)+u



u



s



t















(u



)X (s)







: exp



Z




 


(v ) dv







(1.1)



e

n







+ u


+ u







t



Z



s


0



= exp



(v ) dv +


(v ) dv +



Z



(v ) dv



(v ) dv














t

 


+u


(u


(u


[u




 

s



R



= exp


= exp





(



R



0

t


0



0






s


0

t



0



#)



u


u


:



s

Z



)


u


s


0

s


0



Z



u

# "u



"



R



R



u



]



)











This shows that (X (s); X (t)) is jointly normal with IE X (s) = IE X (t) = 0,



0

Z



Z



s


0



(t) =



Z



t


0



IE X



(s) =







(v ) dv ; IE X







(v ) dv ;



s



IE [X (s)X (t)] =







(v ) dv :


288


**Remark 29.2** The hard part of the above argument, and the reason we use moment generating
functions, is to prove the normality. The computation of means and variances does not require the
use of moment generating functions. Indeed,



X (t) =



t


0

Z




- (u) dW (u)



is a martingale and X (0) = 0, so


For fixed s 0,

   


IE X



m(t) = IE X (t) = 0 t - 0:



s


0

Z



(s) =







(v ) dv



by the Itˆo isometry. For 0 s t,

       -        
IE [X (s)(X (t)       - X (s))] = IE


= IE


= 0:


Therefore,



IE




















F (s)

��



X (s)(X (t) - X (s))



































0



X (s)




- X (s)



IE



X (t)



F (s)







0

| {z }



IE [X (s)X (t)] = IE [X (s)(X (t) - X (s)) + X



(s)]



s



= IE X



(s) =







(v ) dv :



0



If - were a stochastic proess, the Itˆo isometry says



Z



s



Z



IE X



(s) =



IE 


(v ) dv



0



and the same argument used above shows that for 0 s t,

              -              


s



IE [X (s)X (t)] = IE X



(s) =



Z



IE - (v ) dv :



0



However, when - is stochastic, X is not necessarily a Gaussian process, so its distribution is not
determined from its mean and covariance functions.



**Remark 29.3** When - is nonrandom,


X (t) =



Z



t


0




- (u) dW (u)



is also Markov. We proved this before, but note again that the Markov property follows immediately
from (1.2). The equation (1.2) says that conditioned on (s), the distribution of X (t) depends only
F t
on X (s) ; in fact, X (t) is normal with mean X (s) and variance - (v ) dv .



t

s



R







(v ) dv .


CHAPTER 29. Gaussian processes 289



_z_


_s_



_z_


_s_


_y_

_(b)_
_(a)_


_z_


_s_

_v_



_v_





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-290-0.png)

_y_


|Col1|Col2|
|---|---|
|||



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-290-1.png)

_(c)_


Figure 29.1: _Range of values of_ y ; z ; v _for the integrals in the proof of Theorem 1.70._


**Theorem 1.70** _Let_ W (t) _be_ _a_ _Brownian_ _motion,_ _and_ _let_ - (t) _and_ h(t) _be_ _nonrandom_ _functions._
_Define_



t



0

Z



X (t) =




- (u) dW (u); Y (t) =



t


0

Z



h(u)X (u) du:



_Then_ Y _is a Gaussian process with mean function_ m



Y



(t) = 0 _and covariance function_







v

- �Z



h(y ) dy

   


dv : (1.3)



s



t



s^t



0

Z



Z



v

�Z



h(y ) dy



�Y



(s; t) =



(v )



**Proof:** (Partial) Computation of �Y (s; t) : Let 0 s t be given. It is shown in a homework

              -              problem that (Y (s); Y (t)) is a jointly normal pair of random variables. Here we observe that



**Proof:** (Partial) Computation of 


Y



h(u) IE X (u) du = 0;



mY



(t) = IE Y (t) =



t


0

Z



and we verify that (1.3) holds.


290


We have



�Y



(s; t) = IE [Y (s)Y (t)]







s



t



= IE


= IE



Z



h(y )X (y ) dy :



h(y )h(z )X (y )X (z ) dy dz



h(z )X (z ) dz



0



s



0

Z



Z



t



Z

t



Z



s



0




 
Z



s



=


=


=


=


=


=


=


=


=


=



Z

Z

Z



Z

Z

Z



h(y )h(z )IE [X (y )X (z )] dy dz



0



s



0

Z

Z

Z



0


0


z

Z



t


t



z

 


(v ) dv dy dz



0

Z



y ^z




 


0

s


0



h(y )h(z )


h(y )h(z )



�Z



(v ) dv







dy dz



0



y

Z



0

Z








s



h(y )h(z )


t

h(y ) dy

z



y


0



Z



dz dy (See Fig. 29.1(a))



(v ) dv



0




 

z


0




- 






Z



+


s



Z



y


0



h(z )



(v ) dv







dz



0


+



s


0



�Z




- 






s



�Z







h(y )



�Z







h(z ) dz



(v ) dv







dy



y



Z



Z



t











0

Z



Z



s



z



s



h(z )�



(v )



h(y ) dy



dv dz



z



0

Z







s



y



h(z ) dz



+



h(y )�



(v )



dv dy



y



s


0

Z



Z



0

Z



v

Z



t



�Z



�Z











0

s



s


0



h(z )�



(v )



�Z







h(y ) dy



dz dv



z



v

Z







s



s



h(y )�



(v )



h(z ) dz



dy dv (See Fig. 29.1(b))



y



s



s







Z



+


s



Z



t


v

t




- 
- 


�Z







h(y )h(z ) dy dz







(v )


s

 

0



dv



0


+


s



v



y

Z



s







(v )



h(y )h(z ) dz dy



dv



z

Z








s









Z

Z

Z



h(y )h(z ) dy dz



dv (See Fig. 29.1(c))



(v )


(v )


(v )



Z


Z



v



0



v



s


0

s











s


s



h(z ) dz


h(y ) dy







dv


dv



Z

Z



v



h(y ) dy


h(y ) dy



v



t


t



v



0



v



**Remark 29.4** Unlike the process X (t) =



R



0



t


0

R



t



X (u) du is




- (u) dW (u), the process Y (t) =


CHAPTER 29. Gaussian processes 291


neither Markov nor a martingale. For 0 s < t,

           










s



t



IE [Y (t)jF (s)] =



0

Z



h(u)X (u) du + IE







Z

 


s



h(u)X (u) du



F (s)

  


h(u)IE [X (u)


h(u)X (s) du




 



 



 


= Y (s) +


= Y (s) +



Z

Z



F (s)] du











s



t


t



s



t



= Y (s) + X (s)



s

Z



h(u) du;



where we have used the fact that X is a martingale. The conditional expectation IE [Y (t) (s)] is
jF
not equal to Y (s), nor is it a function of Y (s) alone.


292


### **Chapter 30**

# **Hull and White model**

Consider

dr (t) = (�(t)            -            - (t)r (t)) dt +            - (t) dW (t);

where �(t), - (t) and - (t) are nonrandom functions of t .

We can solve the stochastic differential equation. Set



K (t) =



t


0

Z




- (u) du:



Then


Integrating, we get


eK (t)


so



r (0) +




r (t)

  


= eK (t)




 - (t)r (t) dt + dr (t)




(�(t) dt + - (t) dW (t)) :



d



eK (t)




= eK (t)







�(u) du +




- (u) dW (u);



r (t) = r (0) +



t


0

Z



eK (u)



Z



t


0



eK (u)



t


0

Z



r (t) = e�K (t)



eK (u) �(u) du +



t


0

Z



eK (u)




- (u) dW (u)

      


:



From Theorem 1.69 in Chapter 29, we see that r (t) is a Gaussian process with mean function



e K (u)



eK (u) �(u) du� (0.1)



r (0) +




mr



(t) = e�K (t)



and covariance function



t


0

Z


s^t



0

Z







�r



(s; t) = e�K (s)�K (t)



(u) du: (0.2)



The process r (t) is also Markov.



293


294


We want to study


Then


Z



T



r (t) dt . To do this, we define



R



0

Z



Z



0



t



X (t) =



eK (u)




- (u) dW (u); Y (T ) =



T


0

Z



e�K (t) X (t) dt:











t



r (t) = e�K (t)



+ e�K (t)



X (t);



r (0) +



Z



t


0



eK (u)



T


0



e�K (t)







�(u) du

    


T



r (t) dt =



0

Z



Z



r (0) +



0

Z



eK (u)



�(u) du



dt + Y (T ):



According to Theorem 1.70 in Chapter 29,



T


0

R



r (t) dt is normal. Its mean is



r (0) +








T



�(u) du

    


Z



t


0



0

Z



Z



eK (u)



T


0

Z



e�K (t)



IE


and its variance is


var



0

Z



Z



r (t) dt =



r (t) dt



!



T



= IE Y







dt; (0.3)


dv :



(T )


e K (v )



=



T


0

Z



T


v

Z



e�K (y )



(v )



dy



!



The price at time 0 of a zero-coupon bond paying $1 at time T is



(�



T



r (t) dt

)


T

r (t) dt +

0



B (0; T ) = IE exp



0

Z



Z



(



Z



r (t) dt

!)



var



T


0

Z



= exp


= exp



(�)IE



Z



(�)



e�K (t)



0

Z



�r (0)




T



t



dt 


T


0

Z



e�K (t)+K (u)



�(u) du dt



0



dv

 






dy

!



+



T


0

Z



e K (v )



T


v

Z



e�K (y )



(v )



= exp f�r (0)C (0; T ) - A(0; T )g;



where


C (0; T ) =


A(0; T ) =



T


0

Z

T


0

Z



t


0



e�K (t)+K (u)



�(u) du dt 


Z



e�K (t)



dt;



e�K (y )



T







T


0

Z



e K (v )



v

Z



(v )



dy



!



dv :


CHAPTER 30. Hull and White model 295

## _t_ _T_ _u_


Figure 30.1: _Range of values of_ u; t _for the integral._


**30.1** **Fiddling with the formulas**


Note that (see Fig 30.1)



T


0



Z



T


u

Z



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-296-0.png)

e�K (t)+K (u) �(u) dt du



Z



t


0

T



e�K (t)+K (u) �(u) du dt



=


(y = t; v = u) =


Therefore,


A(0; T ) =


C (0; T ) =



Z

Z


Z

Z



0

T


0


T


0


T


0



eK (v )


e�K (y )



e�K (y )



T



eK (v )



�(v )



dy



v

Z



!



dv :



e�K (y )



T



dy

!







(v )



�(v )


dy ;



T


v

Z



e�K (y )



e K (v ) 


v

Z



dy



!



dv ;



B (0; T ) = exp f�r (0)C (0; T ) - A(0; T )g :



Consider the price at time t [0; T ] of the zero-coupon bond:



( 


t

Z



















F (t)#



r (u) du

)



T



B (t; T ) = IE



exp

"



:



Because r is a Markov process, this should be random only through a dependence on r (t) . In fact,



B (t; T ) = exp f�r (t)C (t; T ) - A(t; T )g ;


296


where


A(t; T ) =



t

Z



e�K (y )



eK (v ) �(v )



T



T



!



(v )



dy



T


v

Z



e�K (y )



v

Z



e K (v ) 


dy







!



dv ;



e�K (y )



C (t; T ) = eK (t)

t

Z



T



dy :



The reason for these changes is the following. We are now taking the initial time to be t rather than

T T

zero, so it is plausible that : : : dv should be replaced by : : : dv : Recall that



t

R



t



T



: : : dv should be replaced by



T



: : : dv : Recall that



R



0



K (v ) =



Z



v


0




- (u) du;



and this should be replaced by



K (v ) - K (t) =



v


t

Z




- (u) du:



Similarly, K (y ) should be replaced by K (y ) K (t) . Making these replacements in A(0; T ), we

            see that the K (t) terms cancel. In C (0; T ), however, the K (t) term does not cancel.


**30.2** **Dynamics of the bond price**



Let C



t



(t; T ) denote the partial derivatives with respect to t . From the formula



(t; T ) and At



B (t; T ) = exp f�r (t)C (t; T ) - A(t; T )g ;

we have



h



dB (t; T ) = B (t; T )


= B (t; T )



�C (t; T ) dr (t) 



- C (t; T ) (�(t) - - (t)r (t)) dt



(t; T ) dt At

   


(t; T ) dt

i



C



(t; T ) dr (t) dr (t) r (t)Ct

     



 



- C (t; T )� (t) dW (t) 


:




(t) dt



C



(t; T )�



r (t)Ct




(t; T ) dt At

   


(t; T ) dt



Because we have used the risk-neutral pricing formula



exp (�



T


t

Z




 


F (t)#



r (u) du

)




 


B (t; T ) = IE



"



to obtain the bond price, its differential must be of the form




 



 


dB (t; T ) = r (t)B (t; T ) dt + (: : : ) dW (t):


CHAPTER 30. Hull and White model 297


Therefore, we must have



�C (t; T ) (�(t) - - (t)r (t)) 


(t) r (t)Ct

 


(t; T ) At

  


(t; T ) = r (t):



C



(t; T )�



We leave the verification of this equation to the homework. After this verification, we have the
formula

dB (t; T ) = r (t)B (t; T ) dt       -       - (t)C (t; T )B (t; T ) dW (t):

In particular, the volatility of the bond price is - (t)C (t; T ) .


**30.3** **Calibration of the Hull & White model**


Recall:



dr (t) = (�(t) - - (t)r (t)) dt + - (t) dB (t);



t



K (t) =


A(t; T ) =



Z



T


t

Z




- (u) du;



0



e�K (y )



e�K (y )



T



T



eK (v )



�(v )



dy

!







dy



(v )



v

Z



Z



e K (v ) 


v

Z



!



dv ;



e�K (y )



T



C (t; T ) = eK (t)



Z



dy ;



t



B (t; T ) = exp f�r (t)C (t; T ) - A(t; T )g :



Suppose we obtain B (0; T ) for all T [0; T - ] from market data (with some interpolation). Can we

determine the functions �(t), - (t), and - (t) for all t [0; T �] ? Not quite. Here is what we can do.



Suppose we obtain B (0; T ) for all T [0; T







] ? Not quite. Here is what we can do.







We take the following input data for the calibration:



1. B (0; T ); 0 T T

    -     
2. r (0) ;


3. �(0) ;




- ;



4. - (t); 0 - t - T - (usually assumed to be constant);



5. - (0)C (0; T ); 0 T T

     -      



-, i.e., the volatility at time zero of bonds of all maturities.



**Step 1.** From 4 and 5 we solve for



C (0; T ) =



T


0

Z



e�K (y )



dy :


298


We can then compute



@ C (0; T ) = e�K (T )

@ T



=) K (T ) = - log



C (0; T );



@

K (T ) =

@ T



@

@ T



Z



0



@

@ T

T




- (u) du = - (T ):



We now have - (T ) for all T [0; T �] .

**Step 2.** From the formula



B (0; T ) = expf�r (0)C (0; T ) - A(0; T )g;



we can solve for A(0; T ) for all T [0; T



] . Recall that



�]



dv :


T

e�K (y )

v

Z



e�K (y )



T



v

Z



!



(v )



dy

!



A(0; T ) =



T


0

Z



eK (v ) �(v )



e K (v ) 


T


v

Z



e�K (y )



dy







We can use this formula to determine �(T ); 0 - T - T - as follows:



e

"


e

"




- e K (v )







T


0

Z

T


0

Z



K (v )


K (v )



�(v )e�K (T )



�(v ) - e K (v )



!#



(v )e�K (T )



dy



e�K (y )



@

@ T


@

@ T



A(0; T ) =


A(0; T ) =



v



T



!#



dv ;



(v )


(v ) e






Z



dy








A(0; T )


A(0; T )







eK (T )


K (T )



Z



T


0



e K (v )







= eK (T ) �(T ) 


= e K (T )�(T ) 


@



�K (T )



(T ); 0 - T - T








T


0



(v ) dv ;



@

@ T

@

@ T



e


e



K (T )



@ T

@

@ T



Z



e K (v ) 


dv ;


K (T ) 


@

@ T







��



eK (T )


K (T )



@

@ T



A(0; T )



(T )e K (T )



+ �(T )� (T )e K (T )




- e



dv ;


:



= �0







e



@ T



@







eK (T )



This gives us an ordinary differential equation for -, i.e.,



�0 (t)e K (t)



+ �(t)� (t)e K (t)




- e



K (t)







(t) = known function of t:



From assumption 4 and step 1, we know all the coefficients in this equation. From assumption 3,
we have the initial condition �(0) . We can solve the equation numerically to determine the function




- .



�(t); 0 - t - T



**Remark 30.1** The derivation of the ordinary differential equation for �(t) requires three differentiations. Differentiation is an unstable procedure, i.e., functions which are close can have very
different derivatives. Consider, for example,



f (x) = 0 x IR;



x IR:



g (x) =



sin (000x)



00


CHAPTER 30. Hull and White model 299


Then



jf (x) - g (x)j 


00



x IR;



but because


we have


for many values of x .



0



(x) = 0 cos(000x);



g



0



jf



0



0 (x) - g



(x)j = 0



Assumption 5 for the calibration was that we know the volatility at time zero of bonds of all maturities. These volatilities can be implied by the prices of options on bonds. We consider now how the
model prices options.


**30.4** **Option on a bond**



Consider a European call option on a zero-coupon bond with strike price K and expiration time T [.]

The bond matures at time T - T [.] [The price of the option at time 0 is]



Consider a European call option on a zero-coupon bond with strike price K and expiration time T




[.] [The price of the option at time 0 is]




- T



R



R

Z



T



r (u) du



(B (T



; T



IE



e�




) - K )+



+







0



r (u) du



= IE e�



T



; T



:



)C (T ; T



) - A(T



+



)g - K )



+



0



(expf�r (T



�







expf�y C (T



)g - K







f (x; y ) dx dy ;



=



Z�



e�x



; T



) - A(T ; T



where f (x; y ) is the joint density of







R



T


0



T



r (u) du; r (T



)




- .



We observed at the beginning of this Chapter (equation (0.3)) that



R



0



r (u) du is normal with



r (u) du

#


r (u) du

#



=


=


=



r (0)e



e K (v )



"



"



0

Z



0

Z



T


0

Z

T


0

Z

T


0

Z



IE r (u) du




 




= IE


= var







eK (u)



v



�K (v )



+ e�K (v )



0

Z



dv ;



T


T



�(u) du

    

dv :



e�K (y )



T



dy

!



Z



(v )



v



We also observed (equation (0.1)) that r (T



) is normal with



eK (u) �(u) du;



T



+ e�K (T



)


0

Z



) = r (0)e�K (T







= IE r (T



(u) du:



Z



)


T


0



e K (u) 


)) = e� K (T



)







= var (r (T


300


In fact,



R



0







T



r (u) du; r (T



)� is jointly normal, and the covariance is



T



) - IE r (T



))

#



0

Z



Z



(r (u) - IE r (u)) du: (r (T



��







= IE



"


T


T



=


=



Z

Z



�r (u; T



) - IE r (T



))] du



0



IE [(r (u) - IE r (u)) (r (T



) du;



0



where 


(u; T



) is defined in Equation 0.2.



r



The option on the bond has price at time zero of



Z



Z�



exp f�y C (T




)g - K



�+



) - A(T ; T



�



e�x




- ( 
  


+



#)



(



)



�xy







y




dx dy : (4.1)




 



 - 






"



x




+



)g - K )+



exp



; T


p




- 


The price of the option at time t [0; T



r (u) du



t

R



e




T



(B (T



; T



] is


F (t)



IE



e








) - K )+



t



; T







t

R



r (u) du







T



(exp f�r (T































(t) (4.2)
F

  


= IE







)C (T




 

; T



) - A(T



t



Because of the Markov property, this is random only through a dependence on r (t) . To compute

T

this option price, we need the joint distribution of r (u) du; r (T ) conditioned on r (t) . This







T



r (u) du; r (T



t

R



)




- conditioned on r (t) . This



t


CHAPTER 30. Hull and White model 301


pair of random variables has a jointly normal conditional distribution, and



T







F (t)#



r (u) du



(t) = IE



= e� K (T


(t) = IE

" t

Z



"

Z



r (u) du - 


+ e�K (v )



dv ;



t



eK (u) �(u) du

      

dv ;















T


T





r (t)e




v



t

Z



=



t

Z



Z



�K (v )+K (t)



















(t) = IE



T


t

Z



r (u) du - 


(t)

!



F (t)



!



�K (y )



(v )



T



=



t

Z



e K (v ) 


Z



e



dy



v



(t) = IE



r (T



)















r (t)



)+K (t) + e�K (T



)




 


t



eK (u)



T



�K (T



�(u) du;



t

Z



= r (t)e







(t) = IE (r (T

    


) - 



 



 


F (t)

  


(t))


K (u)



T



)


t

Z

T



e




 


��







(u) du;



�(t)�




 

 

 

 

(t)�



(t) (r (T

!



) - 


(t))











F (t)#



e�K (u)�K (T



T



u



t

Z



e K (v )















=



Z



)



(v ) dv du:



t



t



The variances and covariances are not random. The means are random through a dependence on



r (t) .



Advantages of the Hull & White model:


1. Leads to closed-form pricing formulas.

2. Allows calibration to fit initial yield curve exactly.


Short-comings of the Hull & White model:


1. One-factor, so only allows parallel shifts of the yield curve, i.e.,


B (t; T ) = exp f�r (t)C (t; T )         - A(t; T )g ;

so bond prices of all maturities are perfectly correlated.

2. Interest rate is normally distributed, and hence can take negative values. Consequently, the
bond price



(



t

Z



















F (t)#



T



r (u) du

)



B (t; T ) = IE



exp

"







can exceed 1.


302


### **Chapter 31**

# **Cox-Ingersoll-Ross model**

In the Hull & White model, r (t) is a Gaussian process. Since, for each t, r (t) is normally distributed,
there is a positiveprobabilitythat r (t) < 0 . The Cox-Ingersoll-Ross model is the simplest one which
avoids negative interest rates.



We begin with a d -dimensional Brownian motion (W



We begin with a d -dimensional Brownian motion (W ; W ; : : : ; Wd ) . Let - - 0 and - - 0 be

constants. For j = ; : : : ; d, let Xj (0) IR be given so that



; W



; : : : ; W



(0) IR be given so that



d



j



(0) + : : : + Xd



(0) - 0;



X



(0) + X



and let X



j [be the solution to the stochastic differential equation]




- dWj




- Xj (t) dt +



(t):



dX



j (t) =

  



- dW



Xj [is called the] _[ Orstein-Uhlenbeck]_ [ process. It always has a drift toward the origin. The solution to]

this stochastic differential equation is



Z




- t



Xj (0) +








dWj



dW



Xj



(t) = e�



t


0



e




- u



(u)

  


:



This solution is a Gaussian process with mean function




- t



Xj



(t) = e�



and covariance function


Define


If d =, we have r (t) = X



(t) and for each t, IP r (t) - 0 =, but (see Fig. 31.1)
f g



mj


�(s; t) =



(0)


s^t




- (s+t)



Z



e� u



du:


(t):







e�



0



r (t) = X



(t) + X



(t) + : : : + Xd







IP




- There are infinitely many values of t - 0 for which r (t) = 0


303



=


304


If d, (see Fig. 31.1)

 




![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_I/Steven E. Shreve Stochastic Calculus for Finance I The Binomial Asset Pricing Model  2005_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-I-The-Binomial-Asset-Pricing-Model--2005.pdf-305-0.png)

_t_


_( X (t),  X (t) )_
_1_ _2_



_x_

_1_


|Col1|x 2|
|---|---|
||_2_|
|||



Figure 31.1: r (t) _can be zero._



IP There is at least one value of t - 0 for which r (t) = 0 = 0:
f g



Let f (x



+ x


fxi


d



+ : : : + xd [. Then]



; fxi


d



; x



; : : : ; x



d



) = x



= xi



xj



if i = j ;

0 if i = j:



=



(



Itˆo’s formula implies


dr (t) =


=



i=

X



i



i=

X



dXi



i



+


i


 - Xi



i=

X



fxi



xi



dXi dXi



i=



d




 

dWi



d



fxi


Xi



i



(t)

 


d


i=

X


(t)



dWi


(t):



dWi




 



i



dt +




- dWi



+



i=

X



= �� r (t) dt + 


d�


d



Xi



dWi



+



i=



q




- - r (t)



!



i=

X



dt


Xi



pr (t)



d


i=

X



d�



t


0

Z



dt + 


r (t)



Define



=


W (t) =



pr (u)



Xi (u)



dWi



dW



(u):


CHAPTER 31. Cox-Ingersoll-Ross model 305


Then W is a martingale,



d



dWi



dt = dt;



Xi



dW =


dW dW =



i=

X



i=

X



r



;



i=



p



d



X



i

r


i



so W is a Brownian motion. We have




- - r (t)!



dt + 


dr (t) =



d�



r (t) dW (t):

q



The _Cox-Ingersoll-Ross (CIR) process_ is given by


dr (t) = (�            -            - r (t)) dt +            


r (t) dW (t);

q



We define



d =




 




- 0:



If d happens to be an integer, then we have the representation


d



r (t) =



i=

X



Xi



(t);



but we do not require d to be an integer. If d < (i.e., - <







), then



IP There are infinitely many values of t       - 0 for which r (t) = 0 = :
f g

This is not a good parameter choice.



If d (i.e., 
 -  






), then



IP There is at least one value of t - 0 for which r (t) = 0 = 0:
f g



With the CIR process, one can derive formulas under the assumption that d = �� [is] [a] [positive]

integer, and they are still correct even when d is not an integer.



With the CIR process, one can derive formulas under the assumption that d =








 


For example, here is the distribution of r (t) for fixed t - 0 . Let r (0) 0 be given. Take

                  


(0) = 0; : : : ; Xd�



(0) = 0; Xd



(0) =



q



r (0):



X



(0) = 0; X



For i = ; ; : : : ; d, Xi

     


(t) is normal with mean zero and variance



( - e�� t



�(t; t) =





 


):


306



Xd



(t) is normal with mean



md (t) = e�




- t



r (0)

q



q



and variance �(t; t) . Then


r (t) = �(t; t)



d�


i=

X



Xi (t)



!



(t)



(0.1)



+ Xd



i=



p



�(t; t)




       -        
d     - = ��

| {z }



degrees of



Chi-square with d - =




 - 
 


Normal squared and independent of the other

term

| {z }



freedom







Thus r (t) has a _non-central chi-square distribution._


**31.1** **Equilibrium distribution of** r (t)



As t, m
!



d



(t) 0 . We have
!



d

r (t) = �(t; t)

i=

X



p



Xi (t)



!







�(t; t)



:




           -           
As t, we have �(t; t) = - [,] [and so] [the limiting distribution of] r (t) is - [times a] [chi-square]

with !d = - [degrees of freedom.] [The chi-square density with] - [degrees of freedom is]



As t, we have �(t; t) =
!





 - [,] [and so] [the limiting distribution of] r (t) is




 











 







[degrees of freedom.] [The chi-square density with]




[degrees of freedom is]



e�y = :



f (y ) =



�=�




 - 
 







 - 
��







y








 




 


We make the change of variable r =





 - y . The limiting density for r (t) is




 



p(r ) =


=




 
:









  -  
- ��



e�



r




 - 
 



 



r



�=�




















 




   
e� 



 








 







:



r



r




 - 
��












 



We computed the mean and variance of r (t) in Section 15.7.



**31.2** **Kolmogorov forward equation**


Consider a Markov process governed by the stochastic differential equation


dX (t) = b(X (t)) dt +         - (X (t)) dW (t):


CHAPTER 31. Cox-Ingersoll-Ross model 307


h



0





y



Figure 31.2: _The function_ h(y )



Because we are going to apply the following analysis to the case X (t) = r (t), we assume that



X (t) 0 for all t .

  


We start at X (0) = x 0 at time 0. Then X (t) is random with density p(0; t; x; y ) (in the y

       variable). Since 0 and x will not change during the following, we omit them and write p(t; y ) rather
than p(0; t; x; y ) . We have



IE h(X (t)) =



0

Z



h(y )p(t; y ) dy



for any function h .

The Kolmogorov forward equation (KFE) is a partial differential equation in the “forward” variables

t and y . We derive it below.

Let h(y ) be a smooth function of y 0 which vanishes near y = 0 and for all large values of y (see

         Fig. 31.2). Itˆo’s formula implies



dh(X (t)) =



hh0



0



(X (t))b(X (t)) +



h00



(X (t))�



(X (t))

i



dt + h0 (X (t))�(X (t)) dW (t);



so



hh0



h



h(X (t)) = h(X (0)) +



Z



t


0



0



(X (s))b(X (s)) +



h00



(X (s))�



(X (s))

i



ds +



h0 (X (s))�(X (s)) dW (s);



0

Z



t



Z



hh0



h



IE h(X (t)) = h(X (0)) + IE



t


0



0



(X (s))b(X (s)) dt +



h00



(X (s))�



(X (s))

i



ds;


308


or equivalently,



0

Z


h



0

Z



Z



t


0



(y )�



h(y )p(t; y ) dy = h(X (0)) +



t


0



h0



(y )b(y )p(s; y ) dy ds +



0



Z

Z



00



(y )p(s; y ) dy ds:



Differentiate with respect to t to get



0

Z



(b(y )p(t; y )) dy ;



h(y )pt



(t; y ) dy =



0

Z



h0



(y )b(y )p(t; y ) dy +



0

Z


h(y )



h00


@

@ y



(y )�



(y )p(t; y ) dy :



Integration by parts yields



Z


0

Z



=0

@

| {z }



h0











y =



0

Z



(y )b(y )p(t; y ) dy = h(y )b(y )p(t; y )



y =











0



y =0



=0












- 0

Z



h0



(y )



dy




 



(y )p(t; y )

    


h00 (y )�



=0

y =

| {z }



0



@

@ y



(y )p(t; y ) dy = h



0 (y )�



(y )p(t; y )







y =0







=0











+

0

Z




 
 

@

@ y



y =


y =0




 



(y )p(t; y )

    


@

@ y



= �h(y )



@




 



 



 
 


(y )p(t; y )



h(y )



dy :



@ y











=0




 
 


Therefore,



=0

| {z }



@

h(y )

@ y



0

Z



(y )p(t; y )

    


h(y )pt



(t; y ) dy = - 0

Z



(b(y )p(t; y )) dy +



0

Z



h(y )



dy ;



or equivalently,


0

Z



(b(y )p(t; y )) 



 



#




h(y )



pt

"



(t; y ) +



@

@ y



@

@ y



(y )p(t; y )



#



dy = 0:



This last equation holds for every function h of the form in Figure 31.2. It implies that



((b(y )p(t; y )) 



 



(y )p(t; y )

    


= 0: (KFE)



@

@ y



@

@ y



pt



(t; y ) +



If there were a place where (KFE) did not hold, then we could take h(y ) - 0 at that and nearby
points, but take h to be zero elsewhere, and we would obtain



@

@ y



0

Z



@

(bp)

@ y 


(�



p)

#



dy = 0:



h



pt

"



+


CHAPTER 31. Cox-Ingersoll-Ross model 309


If the process X (t) has an equilibrium density, it will be



p(y ) = lim



p(t; y ):


(t; y ):



In order for this limit to exist, we must have



t!



0 = lim



t!



pt



Letting t in (KFE), we obtain the equilibrium Kolmogorov forward equation
!



@

@ y



(b(y )p(y )) 






@

@ y



= 0:







(y )p(y )







When an equilibrium density exists, it is the unique solution to this equation satisfying



p(y ) - 0 y - 0;



0

Z



p(y ) dy = :



**31.3** **Cox-Ingersoll-Ross equilibrium density**


We computed this to be



e�


 



 








 



r

;



p(r ) = C r




 - 
��



where


C =


We compute








 








 








 


:



p(r )

:

r







p0


p00



(r ) = 


(r ) =


=




 - - 
 







 
p(r )





- - r

  


p(r );






r





- 











 - 



p(r ) +









- - r








- - r

  


p0



(r )



(  - )p(r ) +

r 






r








- 






=







(�

r 






p(r )




- - r ) - - +








- - r )



r




r







(�

r 






We want to verify the equilibrium Kolmogorov forward equation for the CIR process:



@

@ r



((� - - r )p(r )) 


@

@ r



(�



r p(r )) = 0: (EKFE)


310


Now



@

@ r



((� - - r )p(r )) = �� p(r ) + (� - - r )p0 (r );



@

@ r



(�


p0



(�



r p(r )) =



@

@ r



p(r ) + 


r p0 (r ))



=        

The LHS of (EKFE) becomes



(r ) + 


r p00 (r ):



0



(�

r 


�� p(r ) + (� - - r )p



(r ) 






r p00 (r )







0 (r ) - 


= p(r )


= p(r )


= 0;



�� + (� - - r - 


)



p0










- - r )



+



r








- - r ) + - 







- - r )



(� 






(�

r 






(� 



(�

r 



 - r )

- 


(�

r 







- - r )






+



r










 







- - r )




 

)








- - r ) 






F (t)#




- - r )



(� 






r



(� 


as expected.


**31.4** **Bond prices in the CIR model**


The interest rate process r (t) is given by


dr (t) = (�            -            - r (t)) dt +            
q

where r (0) is given. The bond price process is



r (t) dW (t);



(



t

Z



















F (t)#



r (u) du

)



T



B (t; T ) = IE



exp

"







:



Because



T


0

Z



r (u) du B (t; T ) = IE

   



 


0

Z



"exp (�



t



exp




 



r (u) du




 



 



 


;



the tower property implies that this is a martingale. The Markov property implies that B (t; T ) is
random only through a dependence on r (t) . Thus, there is a function B (r; t; T ) of the three dummy
variables r; t; T such that the _process_ B (t; T ) is the _function_ B (r; t; T ) evaluated at r (t); t; T, i.e.,



B (t; T ) = B (r (t); t; T ):


CHAPTER 31. Cox-Ingersoll-Ross model 311



Because exp



n







t

Because exp 0 r (u) du B (r (t); t; T ) is a martingale, its differential has no dt term. We com
    
pute n 
R







R



t


0



r (u) du












t



0

t



r (u) du



B (r (t); t; T )



d



exp









- 






= exp







Z

Z



0



r (u) du



r (t)B (r (t); t; T ) dt + Br




(r (t); t; T ) dr (t) +



Br r (r (t); t; T ) dr (t) dr (t) + Bt



(r (t); t; T ) dt :

      


The expression in [: : : ] equals



= �r B dt + B



r



(� - - r ) dt + B



r







pr dW



p



+



r r



B



r dt + B



t







dt:



Setting the dt term to zero, we obtain the partial differential equation



r B (r; t; T ) + Bt




(r; t; T ) + (� - r )Br

    


(r; t; T ) +







r Br r (r; t; T ) = 0;

0 t < T ; r 0: (4.1)

    -    


The terminal condition is



B (r; T ; T ) = ; r           - 0:

Surprisingly, this equation has a closed form solution. Using the Hull & White model as a guide,
we look for a solution of the form


B (r; t; T ) = e�r C (t;T )�A(t;T );


where C (T ; T ) = 0; A(T ; T ) = 0 . Then we have



Bt


Br



= (�r C



= �C B ; B



r r



t



At




t



)B ;



= C



B ;



and the partial differential equation becomes



0 = �r B + (�r C







r C



B



t




- A



t



)B - (� - - r )C B +







= r B ( Ct

  -   


C



) B (At

 


t



t



+ - C +



+ �C )



We first solve the ordinary differential equation



Ct

- 


C (u; T ) du;







C


T



(t; T ) = 0; C (T ; T ) = 0;



and then set



(t; T ) + - C (t; T ) +


A(t; T ) =     


t

Z


312


so A(T ; T ) = 0 and



(t; T ) = ��C (t; T ):



At



It is tedious but straightforward to check that the solutions are given by



C (t; T ) =




- cosh (� (T - t)) +



sinh (� (T - t))



;




- sinh (� (T - t))




- cosh(� (T - t)) +




- (T �t)



A(t; T ) = 



 
log





- e




- sinh (� (T - t))



where



e�u

- ; cosh u =



eu



+ e�u



;


:




- =



q



; sinh u =



eu







+ 


Thus in the CIR model, we have



(



t

Z



Z



r (u) du

)




 



 


T




 
 



 
 


F (t)



= B (r (t); t; T );



IE



exp

"







#



where



B (r; t; T ) = exp f�r C (t; T )     - A(t; T )g ; 0     - t < T ; r     - 0;

and C (t; T ) and A(t; T ) are given by the formulas above. Because the coefficients in



q



dr (t) = (� - - r (t)) dt + 


r (t) dW (t)



do not depend on t, the function B (r; t; T ) depends on t and T only through their difference - =

T t . Similarly, C (t; T ) and A(t; T ) are functions of - = T t . We write B (r; - ) instead of

 - 


B (r; t; T ), and we have



B (r; - ) = exp f�r C (� ) - A(� )g ; - - 0; r - 0;



where


We have



B (r (0); T ) = IE exp

(



C (� ) =




- cosh(� - ) +



sinh (� - )




- sinh (� - )



;




    
A(� ) =

   -   


log




    - e     -     

- cosh (� - ) + - sinh (� - )



;




- =




 
q



+ 


:



r (u) du

)







Z



T


0



:



Now r (u) - 0 for each u, almost surely, so B (r (0); T ) is strictly decreasing in T . Moreover,



B (r (0); 0) = ;


CHAPTER 31. Cox-Ingersoll-Ross model 313



r (u) du

   


B (r (0); T ) = IE exp




 - 0

- Z



= 0:



But also,


so


and



lim

T !



B (r (0); T ) = exp f�r (0)C (T ) - A(T )g ;


r (0)C (0) + A(0) = 0;



lim

T !




[r (0)C (T ) + A(T )] = ;


r (0)C (T ) + A(T )



is strictly inreasing in T .


**31.5** **Option on a bond**


The value at time t of an option on a bond in the CIR model is



Z







r (u) du (B (T

)



T



F (t)#



v (t; r (t)) = IE



exp

" (







t



; T



) - K )+















;



where T




[is the expiration time of the option,] T







t

T [.] [As usual,] exp 0 r (u) du v (t; r (t)) is a martingale, and this leads to the partial differential

     
equation n 
R




[.] [As usual,] exp



n








[is the maturity time of the bond, and] 0 t T

           -           






R



t


0



r (u) du



T



�r v + v



+ (� - - r )v



; r - 0:



r vr r



= 0; 0 - t < T



t



r



+







(where v = v (t; r ) .) The terminal condition is



v (T



; r ) = (B (r; T ; T



) - K )+ ; r - 0:



Other European derivative securities on the bond are priced using the same partial differential equation with the terminal condition appropriate for the particular security.


**31.6** **Deterministic time change of CIR model**


_Process time scale:_ In this time scale, the interest rate r (t) is given by the constant coefficient CIR
equation



dr (t) = (� - - r (t)) dt + 


q



r (t) dW (t):



_Real time scale:_ In this time scale, the interest rate r^(



t^) is given by a time-dependent CIR equation



t^



t^):



t^



t^



t^) 


t^



�^(



t^)r^(



t^



t^)) d



t^



t^ + �^ (



t^



t^)



t^)



r^(

q



q



t^) d



t^



W^ (



^



dr^(



t^) = (�^ (


t : Process time



314







t^)



t^



t = '(



**.** **[.......]** [.] **[....]** [.] **[....]** [.] **[...]** [.] **[........]**



**.** **[.......]** [.] **[....]** [.] **[....]** [.] **[....]** [.] **[....]** [.] **[...]** [.] **[...]** [.] **[....................................]** [.]



t^ : Real time




- A period of high interest rate volatility



Figure 31.3: _Time change function._



There is a strictly increasing time change function t = '(t^) which relates the two time scales (See

Fig. 31.3).



There is a strictly increasing time change function t = '(



t^



Let



t^ of a bond with maturity T^ when the interest rate at time



^



T^ ) denote the price at real time



^



B (r;^



^t;



t^ is r^ . We want to set things up so



t^



B^ (r;^



�r C (t;T )�A(t;T )



;



^t;



T^ ) = B (r; t; T ) = e



^



where t = '(



t^



T^ ), and C (t; T ) and A(t; T ) are as defined previously.



t^); T = '(



^



We need to determine the relationship between r^ and r . We have



T



r (t) dt

)



B (r (0); 0; T ) = IE exp



;


:



t^) d



t^



T^ ) = IE exp



0

Z


0

Z



T^



r^(



t^



)



B (r^(0); 0;



(�

(�



With T = '(



T^ ), make the change of variable t = '(



t^), dt = '0



t^), dt = '



t^) d



t^



t^ in the first integral to get



(



0

Z



T^



t^))'



t^



0(



t^) d



t^



t^



)



;



B (r (0); 0; T ) = IE exp



(







r ('(



and this will be B (r^(0); 0;



T^ ) if we set


r^(



t^)) '0



t^) = r ('(



t^



0



(



t^):


CHAPTER 31. Cox-Ingersoll-Ross model 315


**31.7** **Calibration**



; '(



B^ (r^(



^



t^);



t^



'0



r^(



t^)



t^)

(t^



t^)



t^)



!



^t;



^t;



T^ ) = B



^



^



T )



t^



t); '(




- A('(



t^); '(



t^



T^ ))



^



'0



t^); '(



t^



(



T^ ))

)



= exp


= exp



(



�r^(

n



�r^(



t^)



t^



t^)



C^ (



C ('(



t^)



t^



^



t^;



t^



^



t;^



t^)



T^ ) 


A^(



t;^



T^ )



;




where



T^ ))



^



^



t;^



C ('(



'0



t^); '(



(



C (



T^ ) =



^



t^)



^



t;^



t^); '(



T^ ))



^



A(



T^ ) = A('(



^



do _not_ depend on ^t and T^ only through T^ t^, since, in the real time scale, the model coefficients

           
are time dependent.



do _not_ depend on



^t and



T^ only through



T 


^



t^



^t



^



Suppose we know r^(0) and



B^ (r^(0); 0;



^



T^ ) for all



T^ [0;



^



T^



^



�] . We calibrate by writing the equation



B^ (r^(0); 0;



T^ ) = exp



^



�r^(0)

n



C^ (0;



^



T^ ) 


^



A^(0;



T^ )



^







;



or equivalently,



T^ )):



^



B^ (r^(0); 0;



'0



r^(0)



(0)




- log



T^ ) =



^



C ('(0); '(



T^ )) + A('(0); '(



^



Take �; - and - so the equilibrium distribution of r (t) seems reasonable. These values determine
the functions C ; A . Take '0 (0) = (we justify this in the next section). For each T^, solve the



the functions C ; A . Take '0 (0) = (we justify this in the next section). For each T^, solve the

equation for '(T^ ) :



^



T^ ) :



0



0 (0) = (we justify this in the next section). For each



^



B^ (r^(0); 0;



T^ ) = r^(0)C (0; '(



^



T^ )) + A(0; '(



^



T^ )): (*)




- log



^



The right-hand side of this equation is increasing in the '(



The right-hand side of this equation is increasing in the '(T^ ) variable, starting at 0 at time 0 and

having limit at, i.e.,



^



r^(0)C (0; 0) + A(0; 0) = 0;



lim

T !




[r^(0)C (0; T ) + A(0; T )] = :



Since 0 log

  -   


Since 0 log B^ (r^(0); 0; T^ ) < ; (*) has a unique solution for each T^ . For T^ = 0, this solution

  -   
is '(0) = 0 . If T^ < T^ [, then]



T^ . For



^



^



^



^



B (r^(0); 0;



^



<



T^ ) < ; (*) has a unique solution for each



T



T^




[, then]



T^



^



) < - log



T^



^



);




- log



B^ (r (0); 0;



^



B^ (r (0); 0;



so '(



T^



^



) < '(



T^



^



) . Thus ' is a strictly increasing time-change-function with the right properties.


316


**31.8** **Tracking down** '0



(0) **in the time change of the CIR model**



0



Result for general term structure models:





















T =0







@

@ T



log B (0; T )



= r (0):



Justification:



(



Z



r (u) du

)



B (0; T ) = IE exp







T


0



:







r (u) du

)




- log B (0; T ) = - log IE exp







Z



T


0



(


T


0



r (u) du



r (u) du







r (T )e



IE



0



IE e�







@

@ T



log B (0; T ) =



R






T



















T =0







@

@ T



log B (0; T )



R



= r (0):



In the real time scale associated with the calibration of CIR by time change, we write the bond price
as



B^ (r^(0); 0;



T^ );



thereby indicating explicitly the initial interest rate. The above says that



@



















T^



B^ (r^(0); 0;



T^ )



= r^(0):



log







T^ =0



@



^



The calibration of CIR by time change requires that we find a strictly increasing function ' with



'(0) = 0 such that



T^ ) =



^



'0



(0)



^



T ));




- log



B^ (r^(0); 0;



^



T^ 0; (cal)

 


r^(0)C ('(



T )) + A('(



^



where B^ (r^(0); 0; T^ ), determined by market data, is strictly increasing in T^, starts at 1 when T^ = 0,

and goes to zero as T^ . Therefore, log B^ (r^(0); 0; T^ ) is as shown in Fig. 31.4.



T^, starts at 1 when



where



^



^



^



B (r^(0); 0;



T^ ), determined by market data, is strictly increasing in



^



T^ . Therefore, log
! 


^



^



B (r^(0); 0;



T^ ) is as shown in Fig. 31.4.



^



Consider the function



Here C (T ) and A(T ) are given by



r^(0)C (T ) + A(T );


sinh (� T )



C (T ) =




- cosh(� T ) +



;




- sinh (� T )




    
A(T ) =

   -   



- T


 - sinh (� T )



log




    - e

- cosh (� T ) +



;




- =




 
q



+ 


:


CHAPTER 31. Cox-Ingersoll-Ross model 317



B^ (r^(0); 0;




- log



T^ )



^



Strictly increasing


    


Goes to


T^



B^ (r^(0); 0;



T^ )



Figure 31.4: _Bond price in CIR model_


r^(0)C (T ) + A(T )


**....** **....** **....** . **....** . **....** . **....** . **....** . **....** . **...** . **...** . **....**


         
**.** **[.......................]** [.] **[....]** [.] **[....]** [.] **[....]** [.] **[....]** [.] **[....]** [.] T




- log



^



'(T^ )


Figure 31.5: _Calibration_



The function r^(0)C (T ) + A(T ) is zero at T = 0, is strictly increasing in T, and goes to as

T . This is because the interest rate is positive in the CIR model (see last paragraph of Section
!
31.4).

To solve (cal), let us first consider the related equation



^



T )) + A('(



^



T^ )): (cal’)



^




- log



B^ (r^(0); 0;



T^ ) = r^(0)C ('(



T^ ) to be the unique T for which (see Fig. 31.5)



Fix



T^ and define '(




- log B^ (r^(0); 0;



T^ ) = r^(0)C (T ) + A(T )



If T^ = 0, then '(T^ ) = 0 . If T^ < T^ [, then] '(T^ ) < '(T^ ) . As T^, '(T^ ) . We have thus

! !

defined a time-change function ' which has all the right properties, except it satisfies (cal’) rather
than (cal).



If



T^ = 0, then '(



T^, '(
!



^



T^ ) = 0 . If



^



T^



<



T^



) < '(



T^



) . As



^



^



T^




[, then] '(


318


We conclude by showing that '0



0 (0) = so ' also satisfies (cal). From (cal’) we compute



0



T^ )



^











�0



r^(0) = 


@



T^



^



log



B^ (r^(0); 0;



T^=0



@



0



(0):



0

0



0



0



0



0 ('(0))'0(0)



= r^(0)C


= r^(0)C



('(0))'



(0) + A



(0)'



0 (0)'0(0) + A0



0




We show in a moment that C 0



0 (0) =, A0



0



(0) = 0, so we have



r^(0) = r^(0)'0(0):


Note that r^(0) is the initial interest rate, observed in the market, and is striclty positive. Dividing by

r^(0), we obtain



'0 (0) = :



Computation of C



0 (0) :



0




- sinh (� - )

    


0



0 (� ) =







C




- sinh (� - )




 - cosh(� - )





 - cosh (� - ) +









- cosh(� - ) +




- sinh (� - )




- - )

i








 



sinh (� - ) +




- - cosh(� - )




 



C 0



= :



(0) =







h




- (� + 0) - 0(0 +



Computation of A0



0 (0) :



0




- sinh (� - )




- cosh(� - ) +







A0 (� ) = 

A0 (0) = 

=  

= 0:




 


 


 



"



#




- e




- - =




- sinh (� - )

    











- cosh(� - ) +




- 



- - =







e� - =




- sinh (� - )




 



sinh (� - ) +




- - e

- + 0

 


(� + 0)




- - cosh(� - )








 - cosh(� - ) +








 






;

��

- - )







(� + 0) - - (0 +




- 







- 



- 

#



"


### **Chapter 32**

# **A two-factor model (Duffie & Kan)**

Let us define:



X



(t) = Interest rate at time t



0



X



(t) = Yield at time t on a bond maturing at time t + 


Let X



Let X (0) - 0, X (0) - 0 be given, and let X (t) and X (t) be given by the coupled stochastic

differential equations



(0) - 0, X



(0) - 0 be given, and let X



(t) and X



) dt + 

) dt + 


q

q



(t); (SDE1)



dX


dX



(t) = (a


(t) = (a



X


X



(t) + a


(t) + a



X


X



(t) + b


(t) + b











(t) + 

(t) + 


X


X



(t) + - dW



(t) + - (� dW



(t) +



q




- 


dW (t));

(SDE2)



X


X




[are independent Brownian motions. To simplify notation, we define]



where W




[and] W



Y (t)



= 


X



(t) + 


X



(t) + �;



= �W



(t) +



q




- 


W



(t)



W



(t):



Then W


and




[is a Brownian motion with]



(t) = - dt;



(t) dW



dX



dW


Y dt; dX



dX



dX



= 


= 

319



Y dt; dX



dX



= ��







Y dt:


320


**32.1** **Non-negativity of** Y



d Y = 

= (�


= [(�



+ 

+ (�



a





+ 


+ 


dX



X


+



+ - a



X



+ 


b



) dt + (�



a



X



+ 


a



X





+ 


b



) dt



pY (�



b



��


+ 


dW


a



q




- 


dW



+ (�



+ 


+ 


dW



Y (t) dW

q


(t)



] dt + (�



b


)




 

)X



+ 






a



+ 

(t)



)


) dt


= - 


)X


)


W



��







+ 

 - 
+ 



 

 




where



)W



+ 


(t) + 






(�



dX


a


a


 


q



W



(t) =







��





��



�p



is a Brownian motion. We shall choose the parameters so that:



**Assumption 1:** For some -, 


a



+ 


a



= - - ; 


+ - a


+ - 


pY dW



:



Then



d Y = [� 


+ 


X



+ - 


X



+ �� ] dt + (� b



b




- �� ) dt



+ (�


= - Y dt + (�



p



+ 







 

b



+ 


+ 


b







��







+ 






)





Y dW



:




- �� ) dt + (�



��



a





From our discussion of the CIR process, we recall that Y will stay strictly positive provided that:



**Assumption 2:** Y (0) = 


X



(0) + 


X



(0) + - - 0;



and
**Assumption 3:**      

Under Assumptions 1,2, and 3,



(�



b



+ 


b




- - - 






+ 






��







+ 






):



Y (t)           - 0; 0 t < ; almost surely,

            
and (SDE1) and (SDE2) make sense. These can be rewritten as



X (t) + b


X (t) + b



) dt + 

) dt + 


q

q



Y (t) dW



Y (t) dW



dX


dX



(t) = (a


(t) = (a



X


X



(t) + a


(t) + a



(t); (SDE1’)


(t): (SDE2’)


CHAPTER 32. A two-factor model (Duffie & Kan) 321


**32.2** **Zero-coupon bond prices**


The value at time t T of a zero-coupon bond paying $1 at time T is

     


"



















F (t)#



T



B (t; T ) = IE



exp



(�



t

Z



X



(u) du

)



:



Since the pair (X



; X



) of processes is Markov, this is random only through a dependence on



X (t); X (t) . Since the coefficients in (SDE1) and (SDE2) do not depend on time, the bond price

depends on t and T only through their difference - = T t . Thus, there is a function B (x ; x ; - )

               


X



(t); X



t T        - = T        - t B (x ; x ;        - )

of the dummy variables x ; x [and] -, so that




[and]  -, so that



; x



; x



(�





















F (t)#



T



X (u) du

)



B (X



(t); X



(t); T - t) = IE



"



exp



t

Z



:



The usual tower property argument shows that




 



t



exp



0

Z



Z



(t); T - t)



X



(u) du B (X

  


(t); X



is a martingale. We compute its stochastic differential and set the dt term equal to zero.








t



0



B (X



(t); X



(t); T - t)

   


d



exp












(u) du



(u) du �X

  - ��







X



X


X


+


X



= exp


= exp









Z

Z



0

Z



Z



(u) du



�X



B dt + Bx



+ Bx



dX



dX



B�




dt



0




- 


Bx



Bx



x



dX



x



+



x



dX







dX



dX


dX



dX







+ Bx


B + (a



t


t



+ b



)Bx



+ (a



)Bx



B�




+ a



+ a



+ b



+ �)Bx



dt


 

x



+


+ 






Y Bx



x



Y Bx



x



Y Bx



x



+ �)Bx



X


(�



+ ��







X


+


dW





 





+



p



x



Y B



+ 


dW



The partial differential equation for B (x



; x



pY Bx


; - ) is



x



)Bx



(� ) - A(� )g ;




- x



B B�

 


+ (a



+ ��







)Bx



+ (a


+ �)B



x


x



X


x



x



+ a



x



x



+ a



+ b



+ 


x



x



+ 


x


x



x


 


x



(�



+ 


+



= 0: (PDE)



We seek a solution of the form



B (x


valid for all - 0 and all x

    


; - ) = exp f�x

[satisfying]



C


x



+ b


(�


C



; x


; x



(� ) - x



+ - - 0: (*)







x



+ 

322


We must have



B (x



; 0) = ; x



; x



; x



satisfying (*) ;



because - = 0 corresponds to t = T . This implies the initial conditions



(0) = A(0) = 0: (IC)



C



(0) = C



We want to find C



(� ); A(� ) for - - 0 . We have



(� ); C



(� ) - A



0



; - ) =



; - ) = C


; - ) = C


; - ) = C



�x



(� )B (x


(� )B (x



0



; x


; x



0



B (x



B�



; x


; x


; x


; x


; x


; x




 


C



(� ) - x



C



; x



; - );



; x



(� )�



Bx


Bx



; - ) = �C

; - ) = �C



; - );


; - );



(� )B (x



(� )B (x ; x



Bx



x


x


x



; - );



(x


(x


(x


(x


(x


(x



(� )B (x



; x ; - );



Bx


Bx

(PDE) becomes


0 = B (x ; x



; - )



�x


x



(� )C



; - ):



C


x



(� ) - (a



+ x


+ a



0



+ b



(� ) + x



0



)C



(� )


(� )



C



(� ) + A0



x



+ a



x



+ b




- (a



)C



(� )



+



+ �)C


+ �)C



(� ) + ��


(� )

  


x


C


C



(� )C







+ - x


+ - x







(�



x



+ 


+ �)C


(� )

  

(� )

  


B (x







(�


(�



x


x



= x



B (x



+


; x


+ x



; - )

  



- + C



0



(� ) - a



C


 


(� ) - a



C



C



(� )



+



(� ) +







C



C



(� ) + ��







(� )C








 

; x


 


; - ) C

  


0 (� ) - a



C



(� ) - a



C



(� )



+


+ B (x


+


We get three equations:







(� ) + ��







(� ) - b



C



(� )C



C













(� ) + ��



0



0 (� ) - b










C



; x


 


; - )


�C



A0




(� ) +


(� )



(� ) +



�C



(� )C







�C



(� )

  


(� ) = a


(0) = 0;


(� ) = b



(� ) 


C


C


C


C



0


0



(� ) = + a


(0) = 0;



C



(� ) + a



C



(� ) 










C



(� ) - ��











C



(� )C







(� ); (2)



C



(� );
(1)



(� ) 



 

�C



C



(� ) + a



C



(� ) 










C



(� ) - �� 






C



(� )C







(� ); (3)






C



A0



(� ) 


C



(� ) + b



C



(� ) 






�C



(� ) - ��







�C



(� )C







A(0) = 0;


CHAPTER 32. A two-factor model (Duffie & Kan) 323


We first solve (1) and (2) simultaneously numerically, and then integrate (3) to obtain the function

A(� ) .


**32.3** **Calibration**



Let 


0




- 0 be given. The value at time t of a bond maturing at time t + �0 [is]



B (X


and the yield is



(t); X



(t); �0 ) = exp X

f�



(t)C



(�0 ) X

 


(t)C



(�0 ) A(�0

 


)g



(t); X



(t); �0 ) =



�0



(t)C



(�0 ) + X



(t)C



(�0 ) + A(�0



)] :







�0



log B (X




[X



But we have set up the model so that X (t) is the yield at time t of a bond maturing at time t + �0 [.]

Thus



But we have set up the model so that X



(t) is the yield at time t of a bond maturing at time t + 


�0



(t)C



(�0



) + X



(t)C



(�0



) + A(�0 )] :



X



(t) =




[X



This equation must hold for every value of X



(t) and X



; a



; a



(�0


; b



) = �0



; 


; 


(t), which implies that


; A(� ) = 0:



C


We must choose the parameters



) = 0; C



a



; a



(�0


; b



; �; 


; �; 


;



so that these three equations are satisfied.


324


### **Chapter 33**

# **Change of num´eraire**

Consider a Brownian motion driven market model with time horizon T - . For now, we will have

one asset, which we call a “stock” even though in applications it will usually be an interest rate
dependent claim. The price of the stock is modeled by


dS (t) = r (t) S (t) dt +           - (t)S (t) dW (t); (0.1)



where the interest rate process r (t) and the volatility process - (t) are adapted to some filtration



. W is a Brownian motion relative to this filtration, but (t); 0 t T
g fF - 






fF (t); 0 - t - T



fF (t); 0 - t - T - g W fF (t); 0 - t - T - g

may be larger than the filtration generated by W .

This is _not_ a geometric Brownian motion model. We are particularly interested in the case that the
interest rate is stochastic, given by a term structure model we have not yet specified.

We shall work only under the risk-neutral measure, which is reflected by the fact that the mean rate
of return for the stock is r (t) .

We define the _accumulation factor_








- (t) = exp



t


0

�Z



r (u) du

   


;



so that the discounted stock price



S (t)

- (t) [is a martingale. Indeed,]







S (t)

- (t)



S (t)

- (t)




- (t) dW (t):



d







=



The zero-coupon bond prices are given by


B (t; T ) = IE

"


= IE

                     

325



t

Z



F (t)#



r (u) du

)


;







T



exp



(�




- (t)

- (T )





















F (t)


















326


so



B (t; T )

 - (t)







= IE








- (T )



F (t)

  


is also a martingale (tower property).















The T _-forward price_ F (t; T ) of the stock is the price set at time t for delivery of one share of stock
at time T with payment at time T . The value of the forward contract at time t is zero, so



(S (T ) - F (t; T ))




 


0 = IE








- (t)

- (T )



















F (t)







F t

 


F (t)

  







 



 



 



 


= - (t)IE



S (T )

- (T )








- (t)

- (T )




- F (t; T )IE







S (t)

- (t)




- F (t; T )B (t; T )




 



 



 


= - (t)



= S (t) - F (t; T )B (t; T )



Therefore,



F (t; T ) =



S (t)

B (t; T )



:



**Definition 33.1 (Num´eraire)** Any asset in the model whose price is always strictly positive can be
taken as the num´eraire. We then denominate all other assets in units of this num´eraire.



**Example 33.1 (Money market as num´eraire)** The money market could be the num´eraire. At time t, the
stock is worth S (t) [units of money market and the] T -maturity bond is worth B (t;T ) units of money market.



S� ((tt)) [units of money market and the] T -maturity bond is worth



�(t;T(t) ) units of money market.



S (t)



B (t;T )



**Example 33.2 (Bond as num´eraire)** The T -maturity bond could be the num´eraire. At time t T, the stock

                         is worth F (t; T ) units of T -maturity bond and the T -maturity bond is worth 1 unit.



We will say that a probability measure IPN [is] _[ risk-neutral for the num´eraire]_ N if every asset price,

divided by N, is a martingale under IPN [. The original probability measure] IP is risk-neutral for the



We will say that a probability measure IP



divided by N, is a martingale under IPN [. The original probability measure] IP is risk-neutral for the

num´eraire - (Example 33.1).



**Theorem 0.71** _Let_ N _be a num´eraire, i.e., the price process for some asset whose price is always_
_strictly positive. Then_ IPN _[defined by]_



)



)



dIP ; A F (T



N (T

- (T







N (0)







);



IPN



(A) =



A

Z







_is risk-neutral for_ N _._


CHAPTER 33. Change of num´eraire 327



_Note:_ IP and IPN [are equivalent, i.e., have the same probability zero sets, and]



)

)



; A F (T




- (T

N (T








IP (A) = N (0)



A

Z



dIPN



):







**Proof:** Because N is the price process for some asset, N =� is a martingale under IP . Therefore,



)

 


N (T

- (T



N (T

- (T



�)







IPN (�) =


=


=



N (0)


N (0)


N (0)




 
Z


:IE



N (0)

- (0)







)



)







dIP

 


and we see that IP



= ;


N [is a probability measure.]



Let Y be an asset price. Under IP, Y =� is a martingale. We must show that under IPN [,] Y =N is

a martingale. For this, we need to recall how to combine conditional expectations with change of
measure (Lemma 1.54). If 0 - t - T - T - and X is F (T ) -measurable, then



Let Y be an asset price. Under IP, Y =� is a martingale. We must show that under IP




- and X is F (T ) -measurable, then























N (T )

N (0)� (T )







=


=


=


=


=



Y (t)



N (0)� (t)

IE

N (t)




 - (t)

N (t)


 - (t)

N (t)

 - (t)

N (t)

Y (t)

N (t)



IEN



X

 


F (t)















F (t)







Y (T )

N (T )















X


:















N (T )

- (T )


N (T )

- (T )



X



F (t)







Therefore,





















F (t)





















F (t)

  


Y (T )

N (T )



IE


IE



IEN














 - (t)


;



which is the martingale property for Y =N under IPN [.]


**33.1** **Bond price as num´eraire**



Fix T (0; T




- ] and let B (t; T ) be the num´eraire. The risk-neutral measure for this num´eraire is



B (T ; T )

 - (T )



B (0; T )


B (0; T )



IPT



(A) =


=



A

Z


A

Z




- (T )



dIP



dIP A F (T ):


328



Because this bond is not defined after time T, we change the measure only “up to time T ”, i.e.,
using B (0;T ) B�((TT;T) ) [and only for] A (T ) .

F

IPT [is called] [the] T _-forward measure._ Denominated in units of T -maturity bond, the value of the

stock is



B (T ;T )



B (0;T )



�((TT;T) ) [and only for] A (T ) .
F



IP



F (t; T ) =



S (t)

; 0 t T :

B (t; T ) - 


This is a martingale under IPT [, and so has a differential of the form]



dF (t; T ) = 


(t; T )F (t; T ) dWT



(t; T )F (t; T ) dW



(t); 0 t T ; (1.1)

  -   


F



i.e., a differential without a dt term. The process W
f



; 0 t T is a Brownian motion under

 -  - g

(t; T ) 0 .

  


T [.] [We may assume without loss of generality that] 


IP



T


F



We write F (t) rather than F (t; T ) from now on.


**33.2** **Stock price as num´eraire**



Let S (t) be the num´eraire. In terms of this num´eraire, the stock price is identically 1. The riskneutral measure under this num´eraire is




- )

- )



dIP ; A F (T



S (T

- (T



IPS (A) =



S (0)







):



A

Z



Denominated in shares of stock, the value of the T -maturity bond is



B (t; T )

S (t)



=



F (t)



:



This is a martingale under IPS [, and so has a differential of the form]











F (t)








dWS



d



F (t)



(t); (2.1)



= - (t; T )



where W
f



where fWS (t); 0 - t - T - g is a Brownian motion under IPS [.] [We] [may] [assume] [without loss of]

generality that - (t; T ) 0 .

      


is a Brownian motion under IP
g



S



(t); 0 - t - T







**Theorem 2.72** _The_ _volatility_ - (t; T ) _in_ _(2.1)_ _is_ _equal to_ _the_ _volatility_ 


**Theorem 2.72** _The_ _volatility_ - (t; T ) _in_ _(2.1)_ _is_ _equal to_ _the_ _volatility_ - F (t; T ) _in_ _(1.1)._ _In_ _other_

_words, (2.1) can be rewritten as_



F















F (t)



d



F (t)



(t); (2.1’)



= - F



(t; T )







dWS


CHAPTER 33. Change of num´eraire 329



**Proof:** Let g (x) = =x, so g 0



0



. Then



0 (x) = - =x



00



; g



(x) = =x



0



F (t)

  


d







= dg (F (t))



= g



(F (t)) dF (t) +



00



g



(F (t)) dF (t) dF (t)



=

 - F



(t) +



F



(t; T ) dt



(t; T )F (t; T ) dWT



(t; T )F (t; T ) dW



(t; T )F



(t)







F




- F



(t)







=



F (t)



(t; T ) dWT



(t; T ) dW



(t) + 


F



(t; T ) dt

i



h



��



F







(t) + - F



(t; T ) dt]:



= 


(t; T )



F (t)



F




[ dWT




Under IP



Under IPT ; WT [is a Brownian motion. Under this measure,] F (t) [has volatility] - F (t; T ) and mean

   
rate of return - (t; T ) . The change of measure from IPT [to] IPS [makes] [a] [martingale,] [i.e.,] [it]



T




       F (t) [has volatility]



; �W



T [is a Brownian motion. Under this measure,]



F



rate of return - F (t; T ) . The change of measure from IPT [to] IPS [makes] F (t) [a] [martingale,] [i.e.,] [it]

changes the mean return to zero, but the change of measure does not affect the volatility. Therefore,



S [makes]



F



(t; T ) . The change of measure from IP



T [to] IP




- (t; T ) in (2.1) must be 


(t; T ) and W



F



S [must be]



Z



t


0



WS



W



(t) = WT

  


(t) +







F (u; T ) du:



**33.3** **Merton option pricing formula**


The price at time zero of a European call is



V (0) = IE

     

= IE

     


(S (T ) - K )+




- (T )

S (T )

- (T )







fS (T )>K g

    



 - (T )




fS (T )>K g








- K IE



S (T )



= S (0)



S (T )>K

Zf g



S (0)� (T )



S (T )>K

Zf g



B (0; T )� (T )



dIP - K B (0; T )



dIP



= S (0)IPS

= S (0)IPS


= S (0)IPS



fS (T ) - K g - K B (0; T )IP

fF (T ) - K g - K B (0; T )IP







F (T )



fS (T ) - K g

fF (T ) - K g



fS (T ) - K g



T



T



K



<







K B (0; T )IPT F (T ) - K :

- f g


330



This is a completely general formula which permits computation as soon as we specify 


F



This is a completely general formula which permits computation as soon as we specify - F (t; T ) . If

we assume that - F (t; T ) is a constant - F [, we have the following:]



F



(t; T ) is a constant 


F [, we have the following:]




 
n



B (0; T )

S (0)



exp



F



T







;



WS (T )

  



- F



F (T )



=



W



=



F








p



T



K B (0; T )



S (0)



WS



F



IPS







F (T )



K

 

 


= IPS


= IPS







F



T < log



(T ) 






<



(T )



S



S (0)

K B (0; T )



F



+













pT

 


<



F



pT



log


+



= N (�



);



where


Similarly,


where







;



log




S (0)

K B (0; T )




- F



T






T



:



pT








 
n



F (T ) =



S (0)

B (0; T )



exp



F



WT (T )

  



- F



F



T









p



T



K B (0; T )



S (0)



IPT



F (T ) - K = IPT
f g


= IPT


= IPT







F



WT







F



T - log



(T ) 





 


W



(T )



K B (0; T )

S (0)



T



p



F



log




��



T


T







pT



p



+



�W




 

<







S (0)

K B (0; T )



(T )



log




T



��







F



pT







F



= N (�



);



:


;



;




log




S (0)

K B (0; T )




- F







=



T







pT











F



If r is constant, then B (0; T ) = e�r T,



+ (r +


+ (r 


S (0)

K

S (0)

K




- F


- F



pT









=


=



)T


)T



pT



log

 

log

 








F


F



and we have the usual Black-Scholes formula. When r is not constant, we still have the explicit
formula



V (0) = S (0)N (�



) - K B (0; T )N (�



):


CHAPTER 33. Change of num´eraire 331


As this formula suggests, if - F [is constant, then for] 0 t T, the value of a European call expiring

              -               at time T is



V (t) = S (t)N (�



(t)) - K B (t; T )N (�



(t));



where



+






- F


- F



p



F (t)

K

F (t)

K



F


F









(t) =


(t) =



(T - t)

    


(T - t)



pT - t



T - t



;


:








log


log









This formula also suggests a hedge: at each time t, hold N (�



(t)) shares of stock and short







K N (�



(t)) bonds.



We want to verify that this hedge is _self-financing._ Suppose we begin with $ V (0) and at each time



t hold N (�



t hold N (� (t)) shares of stock. We short bonds as necessary to finance this. Will the position in

the bond always be K N (� (t)) ? If so, the value of the portfolio will always be

     


(t)) ? If so, the value of the portfolio will always be



S (t)N (�



(t)) - K B (t; T )N (�



(t)) = V (t);



and we will have a hedge.



Mathematically, this question takes the following form. Let



�(t) = N (�



(t)):



At time t, hold �(t) shares of stock. If X (t) is the value of the portfolio at time t, then X (t)

X t t                         


�(t)S (t) will be invested in the bond, so the number of bonds owned is



�( portfolio value evolves according to t)S (t) will be invested in the bond, so the number of bonds owned is X (Bt)(�t;T�() t) S (t) and the



B (t;T )



X (t)��(t)



dX (t) = �(t) dS (t) +


The value of the option evolves according to



X (t) - �(t)

B (t; T )



X (t) - �(t)



S (t) dB (t; T ): (3.1)



dV (t) = N (�



(t)) dS (t) + S (t) dN (�



(t)) + dS (t) dN (�



(t))

(t)) - K B (t; T ) dN (�




- K N (�



(t)) dB (t; T ) - K dB (t; T ) dN (�



(t)): (3.2)



If X (0) = V (0), will X (t) = V (t) for 0 t T ?

           -            


Formulas (3.1) and (3.2) are difficult to compare, so we simplify them by a change of num´eraire.
This change is justified by the following theorem.



**Theorem 3.73** _Changes of num´eraire affect portfolio values in the way you would expect._



**Proof:** Suppose we have a model with k assets with prices S



; S



; : : : ; S



k [.] [At each] [time] t, hold



�i (t) shares of asset i, i = ; ; : : : ; k, and invest the remaining wealth in asset k . Begin with

           a nonrandom initial wealth X (0), and let X (t) be the value of the portfolio at time t . The number
of shares of asset k held at time t is



�i



i



P



S



k



�i (t)Si



(t)

;

 


�k



(t) = X (t) 
   


ki=�



k 


(t)


332


and X evolves according to the equation



k 

i=

X



dX =


=



�i



dSi



�i



dSi



k 

i=

X



!



X 


�i



Si



dSk

Sk



i=



i=



k



i=

X



:



+


k



Note that


and we only get to specify 


Xk (t) =



i=

X



�i



(t)Si



(t);



i=



; : : : ; 


k [, in advance.]



Let N be a num´eraire, and define



k [, not] 
 


X (t)

N (t)



; i = ; ; : : : ; k :



X (t) =



Si



N (t)



(t)



;



Sci



i



(t) =



Then


Now


Therefore,



X (t) =

b



i=

X





k







�i



Si



N







d



X =



b



=


=


=


=


=


=



dX + X d


k



i=

X


�i



N



+ dX d



N








N



N




N


N


k



X 
b



X 


i

P



�i dSi






+



!



k


i=

X



�i



dSi






d



d







N






d



+







��



i=

X



+ Si







dSi



d



N



+ dSi




i=



k



i

P



S



k



d



Si



i



:



ci



Si







�k



�i

i=

X


X 



ki=�



k 


�i



X=N 



k



i



!



ki=�



k 


Si



PSk



�i



=N






�i



S



=N



Sci



i



S



ck



ki=�



k 


�i



:



k



ci



ck



k


Sk

c



k


k



k

�i

i=

X



X 
b



k 

i=

X



d



X =

b



d



Si



i



d



S



+



S



i=



Sci


CHAPTER 33. Change of num´eraire 333



This is the formula for the evolution of a portfolio which holds �i [shares of asset] i, i = ; ; : : : ; k

                          
, and all assets and the portfolio are denominated in units of N .



We return to the European call hedging problem (comparison of (3.1) and (3.2)), but we now use
the zero-coupon bond as num´eraire. We still hold �(t) = N (� (t)) shares of stock at each time t .

In terms of the new num´eraire, the asset values are



Stock:


Bond:


The portfolio value evolves according to



S (t)

B (t; T )

B (t; T )

B (t; T )



= F (t);


= :



= �(t) dF (t): (3.1’)



X (t) = �(t) dF (t) + (



b



d()



d



b



X (t) - �(t))



In the new num´eraire, the option value formula



V (t) = N (�



(t))S (t) - K B (t; T )N (�



(t))



becomes


and



V (t) =

b



V (t)

B (t; T )



= N (�



(t))F (t) - K N (�



(t));



(t)) dF (t) + F (t) dN (�



(t)) + dN (�



(t)) dF (t) - K dN (�



(t)):
(3.2’)



d



V = N (�

b



To show that the hedge works, we must show that



F (t) dN (�


This is a homework problem.



(t)) + dN (�



(t)) dF (t) - K dN (�



(t)) = 0:


334


### **Chapter 34**

# **Brace-Gatarek-Musiela model**

**34.1** **Review of HJM under risk-neutral** IP


f (t; T ) = Forward rate at time t for borrowing at time T :



df (t; T ) = - (t; T )�� (t; T ) dt + - (t; T ) dW (t);



where



T



t

Z



















F (t)#


B (t; T ) dW (t):








- (t; T ) =



t




- (t; u) du


T

r (u) du

t )



The interest rate is r (t) = f (t; t) . The bond prices



Z



B (t; T ) = IE



exp

"



(�



(



t

Z



T



f (t; u) du

)



= exp







satisfy



dB (t; T ) = r (t) B (t; T ) dt - 






(t; T )



To implement HJM, you specify a function



volatility of | T{z -maturity bond. }




              - (t; T ); 0              - t              - T :

A simple choice we would like to use is


              - (t; T ) =               - f (t; T )

where - - 0 is the constant “volatility of the forward rate”. This is not possible because it leads to



T




- 


(t; T ) = 


t

Z



f (t; u) du;



f (t; u) du

!


335



df (t; T ) = 


f (t; T )



T


t

Z



dt + - f (t; T ) dW (t);


336


and Heath, Jarrow and Morton show that solutions to this equation explode before T .

The problem with the above equation is that the dt term grows like the square of the forward rate.
To see what problem this causes, consider the similar deterministic ordinary differential equation



f



0 (t) = f



(t);



where f (0) = c - 0 . We have


        


0



= ;


= ;



f

f

d



(t)

(t)



dt



f (t)


f (0)



=



t


0

Z



du = t







f (t)



+




         

This solution explodes at t = =c .



ct 
c



f (t)



= t 


f (0)



= t - =c =



;



f (t) =



c

:

- ct



**34.2** **Brace-Gatarek-Musiela model**


New variables:


Current time t

Time to maturity                 - = T t:

                
Forward rates:


r (t;            - ) = f (t; t +            - ); r (t; 0) = f (t; t) = r (t); (2.1)



@

@ 


r (t; - ) =



@

@ T



f (t; t + - ) (2.2)



Bond prices:



D (t; - ) = B (t; t + - ) (2.3)







t+�





= exp


(u = v - t; du = dv ) : = exp


= exp











Z

Z

Z




 

0



f (t; v ) dv







t


0



f (t; t + u) du


r (t; u) du

   








B (t; t + - ) = r (t; - )D (t; - ): (2.4)

    


@

@ 


D (t; - ) =



@

@ T


CHAPTER 34. Brace-Gatarek-Musiela model 337


We will now write - (t; - ) = - (t; T t) rather than - (t; T ) . In this notation, the HJM model is

          


df (t; T ) = - (t; - )�




- (t; - ) dt + - (t; - ) dW (t); (2.5)




 


dB (t; T ) = r (t)B (t; T ) dt - 


(t; - )B (t; T ) dW (t); (2.6)



where




- (t; u) du; (2.7)







0

Z



Z









(t; - ) =



(t; - ) = - (t; - ): (2.8)



@

@ 








We now derive the differentials of r (t; - ) and D (t; - ), analogous to (2.5) and (2.6) We have



dr (t; - ) = df (t; t + - )



+



@

@ T



f (t; t + - ) dt



differential applies only to first argument | {z }



(2.5),(2.2)







= - (t; - )�



(t; - ) dt + - (t; - ) dW (t) +



@

@ 


r (t; - ) dt



(2.8)

=



@

@ 


(�







r (t; - ) +

h



dt + - (t; - ) dW (t): (2.9)



(t; - ))



i



Also,



dD (t; - ) = dB (t; t + - )



+



@

@ T



B (t; t + - ) dt



differential applies only to first argument | {z }



(2.6),(2.4)




 


= r (t) B (t; t + - ) dt - 


(t; - )B (t; t + - ) dW (t) - r (t; - )D (t; - ) dt



(2.1)



= [r (t; 0) - r (t; - )] D (t; - ) dt - 






(t; - )D (t; - ) dW (t): (2.10)



**34.3** **LIBOR**


Fix - - 0 (say, - = [year).] [$] D (t; - ) invested at time t in a (t + - ) -maturity bond grows to $ 1 at

time t + - . L(t; 0) is defined to be the corresponding rate of simple interest:


D (t;         - )( +         - L(t; 0)) = ;



@

r (t; u) du

0 )

Z



+ - L(t; 0) =



D (t; - )



(



= exp



;



r (t; u) du

  -  


@


0

n

R







:



L(t; 0) =



exp


338


**34.4** **Forward LIBOR**


- - 0 is still fixed. At time t, agree to invest $



DD(t;�(t;�+)� ) at time t + -, with payback of $1 at time



t + - + - . Can do this at time t by shorting



t + - + - . Can do this at time t by shorting DD(t;�(t;�+)� ) bonds maturing at time t + - and going long

one bond maturing at time t + - + - . The value of this portfolio at time t is



D (t;� +� )







D (t; - + - )

D (t; - )



D (t; - ) + D (t; - + - ) = 0:



The _forward LIBOR_ L(t; - ) is defined to be the simple (forward) interest rate for this investment:



D (t; - + - )

D (t; - )



( + - L(t; - )) = ;



r (t; u) dug




 

0



+      - L(t;      - ) =


Connection with forward rates:



D (t; - )

D (t; - + - )



=



exp



exp f�



r (t; u) du







r (t; u) du



;



�R




 
R




 - +�



0




- +�



)



= exp



r (t; u) du

 -  






n

(

n






 
Z

 
 
R




 - +�







: (4.1)



L(t; - ) =



exp




 
Z



Z




















 



 


r (t; u) du

)



r (t; u) du

)




 



 


@

@ 



- =0




 - +�




- +�



exp



(



= r (t; - + - ) exp


= r (t; - );



( 
Z




- =0



so



r (t; u) du

 -  






n



R




 - +�







f (t; t + - ) = r (t; - ) = lim



exp







r (t; u) du


 



- 0
#







; - - 0 fixed :
(4.2)



n



R




 - +�







L(t; - ) =



exp



r (t; - ) is the continuously compounded rate. L(t; - ) is the simple rate over a period of duration - .

We cannot have a log-normal model for r (t; - ) because solutions explode as we saw in Section 34.1.
For fixed positive -, we _can_ have a log-normal model for L(t; - ) .


**34.5** **The dynamics of** L(t; - )


We want to choose - (t; - ); t 0; - 0, appearing in (2.5) so that

        -        
dL(t;             - ) = (: : : ) dt + L(t;             - )             - (t;             - ) dW (t)


CHAPTER 34. Brace-Gatarek-Musiela model 339


for some - (t; - ); t 0; - 0 . This is the BGM model, and is a subclass of HJM models,

      -      corresponding to particular choices of - (t; - ) .

Recall (2.9):



r (t; u) +

h



(t; u))



i



dt + - (t; u) dW (t):



dr (t; - ) =



@

@ u



(�







Therefore,



(: )

= d



r (t; u) du

!


dL(t;  - )



@

@ u



h




- +�




 - +�


 - +�



+ [�




 


(t; - + - ) - 



 
Z



Z

Z

h



r (t; - + - ) - r (t; - ) +



dr (t; u) du (5.1)



d



Z







=


=


=




- +�



r (t; u) +



(�







(t; u))



i



du dt +




 
Z




- (t; u) du dW (t)







(�











(t; - + - ))







(�







(t; - ))



i



dt


!



(t; - )] dW (t)



and



r (t; u) du






d



n

R




- +�




r (t; u) du


 






exp



exp




 
Z




- +�



r (t; u) du

)




- +�



=







(

Z


+



exp






 


( 
Z




 
Z



Z




- +�



r (t; u) du

)




- +�



d



r (t; u) du



(4.1), (5.1)

=




[ +  - L(t;  - )] (5.2)

- 






+ [�




 







[r (t; - + - ) - r (t; - ) +



(� 


(t; - + - ))







(� 


(t; - ))



] dt







(t; - + - ) - 


(t; - )] dW (t)







+




[�







(t; - + - ) - 


(t; - )]



dt

 


=








[r (t; - + - ) - r (t; - )] dt




[ + - L(t; - )]








 


(t; - + - ) - 


+ 






(t; - + - )[�







(t; - )] dt



:




= +[� 


(t; - + - ) - - 


(t; - )] dW (t)


340


But


Therefore,



=


dL(t; - ) =








  - +�

  
nR



r (t; u) du


 






@

L(t;  - ) =

@ 


@

@ 


exp




- +�

r (t; u) du

)



= exp



( 
Z



:[r (t; - + - ) - r (t; - )]



@

@ 


L(t; - ) dt +








[ + - L(t; - )][r (t; - + - ) - r (t; - )]:



(t; - + - ) - 















- (t; - )]:[�



(t; - + - ) dt + dW (t)]:




[ + - L(t; - )][�



Take - (t; - ) to be given by


        - (t;        - )L(t;        - ) =

                 
Then




 



 



[ + - L(t; - )][�



(t; - + - ) - 


(t; - )]: (5.3)



L(t; - ) + - (t; - )L(t; - )�� (t; - + - )] dt + - (t; - )L(t; - ) dW (t):

(5.4)



dL(t; - ) = [



@

@ 


Note that (5.3) is equivalent to











(t; - ) +




- L(t; - )� (t; - )

+  - L(t;  - )



: (5.3’)







(t; - + - ) = 


Plugging this into (5.4) yields



(t; - )



#



dt



(t; - )�



dL(t; - ) =



"



@

@ 


L(t; - ) + - (t; - )L(t; - )��



(t; - ) +




- L



+ - L(t; - )



+                  - (t;                  - )L(t;                  - ) dW (t): (5.4’)


**34.6** **Implementation of BGM**


Obtain the initial _forward LIBOR curve_


L(0;                  - );                  -                  - 0;

from market data. Choose a _forward LIBOR volatility function_ (usually nonrandom)


              - (t;               - ); t               - 0;               -               - 0:


CHAPTER 34. Brace-Gatarek-Musiela model 341


Because LIBOR gives no rate information on time periods smaller than -, we must also choose a
_partial bond volatility function_








- (t; - ); t - 0; 0 - - < 


for maturities less than - from the current time variable t .

With these functions, we can for each - [0; - ) solve (5.4’) to obtain


L(t;                 - ); t                 - 0; 0                 -                 - < �:



Plugging the solution into (5.3’), we obtain 






(t; - ) for - - < - . We then solve (5.4’) to obtain

   


L(t; - ); t - 0; - - - < �;



and we continue recursively.



**Remark 34.1** BGM is a special case of HJM with HJM’s 






**Remark 34.1** BGM is a special case of HJM with HJM’s - - (t; - ) generated recursively by (5.3’).

In BGM, - (t; - ) is usually taken to be nonrandom; the resulting - - (t; - ) is random.







(t; - ) is random.



**Remark 34.2** (5.4) (equivalently, (5.4’)) is a stochastic _partial_ differential equation because of the

@@� L(t; - ) term. This is not as terrible as it first appears. Returning to the HJM variables t and T,

set



@



@ 


Then



K (t; T ) = L(t; T - t):



dK (t; T ) = dL(t; T        - t)        
and (5.4) and (5.4’) become



@

L(t; T t) dt

@ - 






dK (t; T ) = - (t; T - t)K (t; T ) [�



(t; T - t + - ) dt + dW (t)]



dt + dW (t)

     






:
(6.1)



(t; T - t) dt +



=     - (t; T     - t)K (t; T )


**Remark 34.3** From (5.3) we have








- K (t; T )� (t; T - t)



+ - K (t; T )







(t; - + - ) - 
    






(t; - )



:








- (t; - )L(t; - ) = [ + - L(t; - )]







If we let - 0, then
#


and so








- =0
















- (t; - )L(t; - )!



@

@ 



- 


(t; - + - )



= - (t; - );




- (t; T - t)K (t; T )!� (t; T - t):



We saw before (eq. 4.2) that as - 0,
#



L(t; - )!r (t; - ) = f (t; t + - );


342


so

K (t; T )!f (t; T ):

Therefore, the limit as - 0 of (6.1) is given by equation (2.5):
#







df (t; T ) = - (t; T - t) [�



(t; T - t) dt + dW (t)] :



**Remark 34.4** Although the dt term in (6.1) has the term



**Remark 34.4** to this equation do not explode becauseAlthough the dt term in (6.1) has the term - - (t;T+K�t()t;TK )(t;T ) involving K, solutions




- 


(t;T �t)K



t;T+K�t()t;TK )(t;T ) involving K



(t;T )



(t; T )







(t; T )




            -            

**34.7** **Bond prices**



(t; T - t)K



(t; T - t)K

  - K (t; T )




- 


+ - K (t; T )



(t; T - t)K (t; T ):



Let - (t) = exp



t


0

n

R



r (u) du

   



     -      

: From (2.6) we have




- (t)








[�r (t)B (t; T ) dt + dB (t; T )]



d







B (t; T )

 - (t)



=



= 


B (t; T )

 - (t)




 






(t; T - t) dW (t):



The solution



B (t;T )

 - (t) [to this stochastic differential equation is given by]







B (t; T )

- (t)B (0; T )



= exp 
  


0

Z



t



(u; T - u))



Z



t

(�

0







du

 






(u; T - u) dW (u) 


:



This is a martingale, and we can use it to switch to the _forward measure_



IPT (A) =


=



A

Z




- (T )B (0; T )



B (0; T )



Z



A




- (T )



B (T ; T )



dIP


dIP A F (T ):



Girsanov’s Theorem implies that



t



(u; T - u) du; 0 - t - T ;



0

Z



WT



(t) = W (t) +











is a Brownian motion under IPT [.]


CHAPTER 34. Brace-Gatarek-Musiela model 343


**34.8** **Forward LIBOR under more forward measure**


From (6.1) we have



(t; T - t + - ) dt + dW (t)]



dK (t; T ) = - (t; T - t)K (t; T ) [�







= - (t; T - t)K (t; T ) dW



(t);



T +�



so


and



K (t; T ) = K (0; T ) exp


K (T ; T ) = K (0; T ) exp



�Z




 

T



t


0




- (u; T u) dWT +�

  



- (u; T - u) dW




- (u; T u) dWT +�

  



- (u; T - u) dW



(u) 


Z



t


0



(u; T - u) du

    


( 0

Z



T



(8.1)



(u) 


0

Z



(u; T - u) du)

(u; T - u) du)



:



= K (t; T ) exp

(



t

Z



Z









T




- (u; T u) dWT +�

  



- (u; T - u) dW



(u) 


T


t

Z



We assume that - is nonrandom. Then



T



T



X (t) =


is normal with variance



t

Z




- (u; T u) dWT +�

  


(u) 


t

Z







(u; T u) du (8.2)

  


T



Z







(t) =







(u; T - u) du



t



and mean

   






(t) .



**34.9** **Pricing an interest rate caplet**



Consider a floating rate interest payment settled in arrears. At time T + -, the floating rate interest
payment due is - L(T ; 0) = - K (T ; T ); the LIBOR at time T . A caplet protects its owner by
requiring him to pay only the cap - c if - K (T ; T ) - - c . Thus, the value of the caplet at time T + is - (K (T ; T ) c)+ . We determine its value at times 0 t T + - .

    -    -    


+ . We determine its value at times 0 t T + - .

          -          


**Case I:** T t T + - .

   -    



- (K (T ; T ) - c)+




 



 - (t)

- (T + - )



(t) = IE



CT +�







(t) (9.1)
F

  


F (t)

  



 - (t)

- (T + - )




 



 



 



 


= - (K (T ; T ) - c)+

= - (K (T ; T ) - c)+



IE







B (t; T + - ):




 



 



 

344


**Case II:** 0 t T .

   -    Recall that



A

Z



Z (T + - ) dIP ; A F (T + - );



IPT +�


where



(A) =



Z (t) =


We have



B (t; T + - )

:

- (t)B (0; T + - )




 



 



 


F (t)




 - (t)

- (T + - )








- (K (T ; T ) - c)+



CT +�



(t) = IE








 


+



















F (t)



= - B (t; T + - )




- (t)B (0; T + - )

B (t; T + - )


Z (t)

| {z }



IE



B (T + �; T + - )

- (T + - )B (0; T + - )


Z (T +� )

| {z }



(K (T ; T ) - c)+



Z (t)



Z (T +� )















F (t)



= - B (t; T + - )IE







T +�







(K (T ; T ) - c)







From (8.1) and (8.2) we have



K (T ; T ) = K (t; T ) expfX (t)g;



T

where X (t) is normal under IPT +� [with variance] - (t) = t - (u; T u) du and mean - (t) .

                   -                   
Furthermore, X (t) is independent of (t) .
F R



where X (t) is normal under IP



T +� [with variance] 






(t) =



R



T



t



(u; T u) du and mean

  -  


























F (t)

  


CT +� (t) = - B (t; T + - )IET +�



(K (t; T ) expfX (t)g - c)+



+



:





Set


Then



:



g (y ) = IET +�



+



(y expfX (t)g - c)



i



= y N







h



�(t)



y

c



+



�(t)

  



- c N



�(t)




log



y

c 


�(t)



log



CT +� (t) = - B (t; T + - ) g (K (t; T )); 0 t T �: (9.2)

            -            -            


In the case of constant -, we have

�(t) =                    
and (9.2) is called the _Black caplet formula._



pT - t;


CHAPTER 34. Brace-Gatarek-Musiela model 345


**34.10** **Pricing an interest rate cap**


Let



= �; T



= �; : : : ; Tn



= n�:



T0

A cap is a series of payments



= 0; T




- (K (Tk



k



; T



) - c)



+ at time T



k +



; k = 0; ; : : : ; n - :



The value at time t of the cap is the value of all remaining caplets, i.e.,



C (t) =


**34.11** **Calibration of BGM**



k :t Tk

X�



CTk



(t):



The interest rate caplet c on L(0; T ) at time T + - has time-zero value



CT +�



(0) = - B (0; T + - ) g (K (0; T ));



where g (defined in the last section) depends on



T


0

Z







(u; T - u) du:



Let us suppose - is a deterministic function of its second argument, i.e.,


                - (t;                 - ) =                 - (� ):


Then g depends on



T


0

Z



T


0

Z



(v ) dv :







(T - u) du =







If we know the caplet price C



T

If we know the caplet priceknow caplet prices CT +� (0), we can “back out” the squared volatility 0 - (v ) dv . If we

R



R



T


0



T +�



(0), we can “back out” the squared volatility







+�



n



+�



CT0



(0); CT



(0); C



+�



(0); : : : ; CT



(0); : : : ; C



(0);



where T0



< T



< : : : < T



n [, we can “back out”]



Z



T0



T



Z



T


0

Z



T0


0

Z







(v ) dv ;







(v ) dv =







(v ) dv 






(v ) dv ;



0



T



0



Tn

  
Tn

 


: : : ;


In this case, we may assume that - is constant on each of the intervals



Z



(v ) dv : (11.1)



(0; T0); (T0 ; T



); : : : ; (Tn�



; Tn



);


346


and choose these constants to make the above integrals have the values implied by the caplet prices.



If we know caplet prices C



(0) for all T 0, we can “back out”

    


T

If we know caplet prices CT +� (0) for all T 0, we can “back out” 0 - (v ) dv and then differen
            
tiate to discover - (� ) and - (� ) = - (� ) for all - 0 .

R



R



T +�



(� ) and - (� ) =



p�



T


0











(� ) for all - 0 .

    


To implement BGM, we need both - (� ); - 0, and

            







- (t; - ); t - 0; 0 - - < �:



Now 


Now - - (t; - ) is the volatility at time t of a zero coupon bond maturing at time t + - (see (2.6)).

Since - is small (say [year), and] 0 - < -, it is reasonable to set








[year), and] 0  - <  -, it is reasonable to set

    







- (t; - ) = 0; t - 0; 0 - - < �:



We can now solve (or simulate) to get


L(t;                  - ); t                  - 0;                  -                  - 0;

or equivalently,

K (t; T ); t         - 0; T         - 0;

using the recursive procedure outlined at the start of Section 34.6.


**34.12** **Long rates**


The long rate is determined by long maturity bond prices. Let n be a large fixed positive integer, so
that n� is 20 or 30 years. Then



r (t; u) du

)



n�

( 0

Z



D (t; n� )



= exp


n



r (t; u) du

)



(

Z



=


=



k =

Y

n


k =

Y



exp




[ + - L(t; (k - )� )];



k 

(k �)�



k =



n



k =



where the last equality follows from (4.1). The long rate is


n



=

D (t; n� )



n�



n�



log



k =

X



log [ + - L(t; (k - )� )]:



**34.13** **Pricing a swap**



Let T



0



0 be given, and set




+ �; T



= T0



+ �; : : : ; Tn



= T0



+ n�:



T



= T0


CHAPTER 34. Brace-Gatarek-Musiela model 347


The swap is the series of payments



; k = 0; ; : : : ; n - :




- (L(Tk



k +



For 0 t T

  -  

Now



0 [, the value of the swap is]



; 0) c) at time T

 


n�


k =0

X




- (t)





















F (t)



IE






)




- (Tk +



)



:




- (L(Tk



; 0) - c)







k =0



+  - L(Tk


so


L(Tk


We compute



; 0) =


; 0) =


IE








- (Tk +



)



B (Tk



k +



; T



)



;



:




k +











B (Tk



; T








- (t)















F (t)




- (L(Tk



; 0) - c)



)























F (t)

  



 

 



- (t)



= IE


= IE


= IE




- (Tk +



)




- (Tk +



)







B (Tk



k +




- - - c

   


; T








- (t)








- (Tk )



)



( +  - c)B (t; Tk +









 



 



 



 


F (t)




- (Tk +



)



)




- (Tk



)B (Tk



; Tk +



)







(Tk
F



IE



B (T



;T















k



k +



)




- (t)



B (Tk ;Tk + )

| {z }



)



k +



















F (t)

  



- ( + - c)B (t; T



k +



= B (t; T



) - ( + - c)B (t; T



):



k



The value of the swap at time t is



n�


k =0

X




 - (t)

- (Tk +



















F (t)



IE



)




- (L(Tk



; 0) - c)



)]







k =0







=



n�


k =0

X




[B (t; T



k



) - ( + - c)B (t; T



k +



k =0



= B (t; T



) + B (t; T



) - ( + - c)B (t; T



) + : : : + B (t; T



)



) ( + - c)B (t; Tn

 


0



) - ( + - c)B (t; T



= B (t; T0



) - - cB (t; T



) - - cB (t; T



) - : : : - - cB (t; T



) - B (t; T



n�



n



n



):



The forward swap rate w



The forward swap rate wT0 (t) at time t for maturity T0 [is] [the] [value] [of] c which makes the time- t

value of the swap equal to zero:



T



0



(t) at time t for maturity T



) - B (t; T



n



)



wT0 (t) =




- [B (t; T



B (t; T0



B (t; T



) + : : : + B (t; T



n



:

)]



In contrast to the cap formula, which depends on the term structure model and requires estimation
of -, the swap formula is generic.


