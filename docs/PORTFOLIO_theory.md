 Markowitz portfolios
In this section the portfolio selection approach proposed by Markowitz and the notation used in the chapters of Part III will be introduced. Given the scope of this book,
a more detailed derivation of the results is omitted and the reader is referred to such
works as Ingersoll (1987), Huang and Litzenberger (1988), Markowitz (1991), Elton
et al. (2007), and Scherer (2010).
The groundbreaking insight of Markowitz was that the risk/return profiles of single
assets should not be viewed separately but in their portfolio context. In this respect,
portfolios are considered to be efficient if they are either risk minimal for a given
return level or have the maximum return for a given level of risk. Even though both
views of efficient portfolios are equivalent, the kind of portfolio optimization does
differ for these two cases. The former is a quadratic optimization with linear constraints, whereas in the latter the objective function is linear and the constraints are
quadratic.
In the following it is assumed that there are N assets and that they are infinitely
divisible. The returns of these assets are jointly normally distributed. The portfolio
return r̄ is defined by the scalar product of the (N × 1) weight and return vectors 𝜔 and
𝜇. The portfolio risk is measured by the portfolio variance 𝜎2
W = 𝜔′
Σ𝜔, where Σ denotes the positive semi-definite variance-covariance matrix of the assets’ returns. For
the case of minimal variance portfolios for a given portfolio return,r̄, the optimization
problem can be stated as:
P = arg min 𝜔
𝜎2
W = 𝜔′
Σ𝜔,
𝜔′
𝜇 = r̄,
𝜔′
i = 1, (5.1)
where i is the (N × 1) vector of ones.
In the same year as Markowitz published his seminal paper, the function for determining efficient portfolios was derived by Roy (1952), although the paper by Merton
(1972) is cited in the literature more frequently. According to this function, the weight
vector for a minimal variance portfolio and a given target return is given by
𝜔∗ = r̄𝜔∗
0 + 𝜔∗
1, (5.2)
with
𝜔∗
0 = 1
d
(cΣ−1𝜇 − bΣ−1i),
𝜔∗
1 = −1
d
(bΣ−1𝜇 − aΣ−1i).
The portfolio standard deviation is given by
𝜎 =
√1
d
(cr̄2 − 2br̄ + a), (5.3)
48 MODERN PORTFOLIO THEORY
with a = 𝜇′
Σ−1𝜇, b = 𝜇′
Σ−1i, c = i
′
Σ−1i, and d = ac − b2. Equation (5.2) results
from a Lagrange optimization with the constraints for a given target return and
weights summing to one. A detailed exposition is contained in Merton (1972). It can
be concluded from this equation that the portfolio weights are a linear function of
the expected returns. Furthermore, it can be shown that each efficient portfolio can
be generated as a linear combination of two other efficient portfolios. In particular,
the risk/return profile of an efficient portfolio can be expressed in terms of a linear
combination between the global minimal variance (GMV) portfolio and any other
efficient portfolio. The covariance between these two portfolios equals the variance
of the minimum variance portfolio. Though it might not be evident at first glance,
it should be stressed that the only constraint with respect to the portfolio weights is
that their sum equals one. Hence, neither the existence of negative weights (short
positions) nor weights greater than one (leveraged positions) can be ruled out, per se.
Equation (5.3) describes a hyperbola for efficient mean-variance portfolios. The
hyperbola is enclosed by the asymptotes r̄ = b∕c ± √d∕c𝜎. The locus of the GMV
portfolio is the apex of the hyperbola with weights given by 𝜔∗
GMV = Σ−1i∕i
′
Σ−1i (see
Figure 5.1).
In contrast to the mean-variance portfolios, the weight vector of the global minimum variance portfolio does not depend on the expected returns of the assets. The
upper branch of the hyperbola is the geometric location of all efficient mean-variance
portfolios. The marginal risk contributions of the assets contained in these kinds of
portfolios are all the same and the weights correspond to the percentage risk contributions. Hence, these weights are Pareto-efficient. Intuitively this makes sense, because
in the case of differing marginal contributions to risk, an overall reduction in risk
would be feasible and this would violate the minimum variance characteristic for
02468
0.0
0.1
0.2
0.3
0.4
0.5
0.6
σ
μ
GMV
MSR
CML
Efficient frontier
Asymptotes
Utility
Figure 5.1 Global minimum variance and maximum Sharpe ratio portfolios.
MODERN PORTFOLIO THEORY 49
these kinds of portfolios. The risk/return points that are enclosed by the hyperbola
are referred to as the feasible portfolios, although these are sub-optimal. In other
words, portfolios exist that have either a higher return for a given level of risk or are
less risky for certain portfolio return. Both instances would yield a higher utility for
the investor.
So far, it has been assumed that the portfolio holdings of an investor are entirely
in risky assets. We will now depart from the Markowitz model in the strict sense
and allow the holding of a riskless asset with a return of rf . The question that now
arises is how high the optimal holding of this asset in a portfolio should be. This
depends on the risk aversion of the investor. A risk averse investor tries to maximize
his end-of-period wealth (his expected utility), whereby the decision as to the shape
of the portfolio has to be taken at the beginning of the period:1
maxE[U(Wt+1)], (5.4)
where E denotes the expectation operator. The utility function can be approximated
by a Taylor series expansion and it is further assumed that this function is twice differentiable. After a neutral expansion U(Wt+1) = U(Wt+1 + E[Wt+1] − E[Wt+1]), the
utility function to be maximized can be written as
E[U(Wt+1)] =U(E[Wt+1]) +
U′
(E[Wt+1])
1!
E[Wt+1 − E[Wt+1]]
+
U′′(E[Wt+1])
2!
E[Wt+1 − E[Wt+1]]2
+ ∑∞
i=3
U(i)
(E[Wt+1])
i!
E[Wt+1 − E[Wt+1]]i
. (5.5)
It is worth noting that so far no assumptions have been made about how wealth
is distributed. Therefore, (5.5) is defined for a broad class of distribution functions.
Further, utility is a function of the higher moments of the wealth distribution. If wealth
is assumed to be normally distributed, then the above expression simplifies to
E[U(Wt+1)] =U(E[Wt+1]) +
U′
(E[Wt+1])
1!
E[Wt+1 − E[Wt+1]]
+
U′′(E[Wt+1])
2!
E[Wt+1 − E[Wt+1]]2. (5.6)
Hence, the investor’s utility only depends on the first two moments. It should be
stressed that even in the case of non-normality, the above optimization approach can
be used for quadratic utility functions of the form U(W) = W − 𝜆
2 W2. Here the parameter 𝜆 is a measure of the risk aversion of an investor.
1 The following exposition draws on Huang and Litzenberger (1988).
50 MODERN PORTFOLIO THEORY
If one assumes quadratic utility, then the weight vector is given by 𝜔U =
(1∕𝜆)Σ−1𝜇. The greater the risk aversion is, the smaller the sum of the weights. The
expected total return R from the risky assets and the riskless asset is given by
E[R]=(1 − 𝛾)rf + 𝛾 ̄r
= rf + 𝛾(r̄ − rf), (5.7)
where 𝛾 = i
′
𝜔 is the share of risky assets compared to the total wealth. The standard
deviation for this portfolio is 𝜎(R) = 𝛾𝜎W. From this, the capital market line (CML)
can be derived—a linear relationship in the (𝜇, 𝜎) plane—as
E[R] = rf + r̄ − rf
𝜎W
𝜎(R). (5.8)
The optimal portfolio is located at the tangency point of this line and the upper
branch of the efficient frontier. This is given when the slope is greatest and hence the
Sharpe ratio is at its maximum. The portfolio that is characterized at this tangency
point is therefore also referred to as the maximum Sharpe ratio (MSR) portfolio.
In the case of the MSR portfolio the investor holds only risky assets. The marginal
contributions of the selected assets to the Sharpe ratio are all the same. The investment
grade of an investor is determined by the tangency point of his utility function and the
CML. This point lies southwest of the MSR portfolio, and the higher the risk aversion
is, the closer it will be located to the ordinate.
5.3 Empirical mean-variance portfolios
The theoretical portfolio concepts outlined in the previous section are unfortunately
not directly applicable in practice. So far the population moments have been employed in the analysis, but these entities are unknown. In empirical applications these
unknown parameters must be replaced by estimates. The locus of the set for the feasible portfolios is below the efficient frontier. At first glance, the sample mean and
the unbiased estimator of the variance-covariance matrix of the returns seem to be
appropriate candidates for replacing the population moments. In practice, however,
potential estimation errors exert a direct impact on the portfolio weights such that,
for instance, the desired properties of an efficient and/or a minimum variance portfolio are no longer valid, in general. Ultimately, estimation errors are mirrored by a
higher portfolio risk compared to the case of population moments. This is regardless
of whether the estimates have been generated from historic data or ex ante forecasts
for these parameters are employed. For portfolio optimizations that are based on estimators for the expected returns and the variance-covariance matrix, these should have
a greater effect compared to optimization approaches that only rest on estimates for
the return dispersion, ceteris paribus (see Chopra and Ziemba 1993; Merton 1980).
Hence, mean-variance portfolio optimizations should suffer more severely from estimation error than minimum variance ones. In empirical simulations and studies it was
found that the weights of the former kind of portfolio optimizations are characteri

by wide spans and erratic behavior over time (see, for example, DeMiguel et al. 2007;
Frahm 2008; Jagannathan and Ma 2003; Kempf and Memmel 2006; Ledoit and Wolf
2003). From a normative point of view both characteristics are undesired. The effect
of “haphazardly” behaving weights is ameliorated for minimum variance portfolios,
and hence this portfolio design is to be preferred with respect to the potential impact of estimation errors. The sensitivity of the optimal solutions for mean-variance
portfolios with respect to the utilized expected returns is per se not a flaw of the approach proposed by Markowitz, but rather an artifact of the quadratic optimization
for deriving the portfolio weights.
The errors of the estimates for the expected returns and the variance-covariance
matrix could be quantified heuristically beforehand by means of Monte Carlo simulations. This portfolio resampling was proposed by Michaud (1998), and a detailed
description with a critique is given in Scherer (2002) and Scherer (2010, Chapter 4).
In a first step, the estimates 𝜇̂0 and Σ̂ 0 for the theoretical moments 𝜇 and Σ for given
sample size T are calculated and m points on the empirical efficient frontier are computed. Next, K random samples of dimension (T × N) are generated and from these
the sample moments are determined, giving in total K pairs(𝜇̂i, Σ̂ i), i = 1,…,K. Each
of these pairs is then used to compute m points on the respective efficient frontiers.
The locus of these simulated efficient frontiers is below the efficient frontier for 𝜇̂0
and Σ̂ 0. To assess the impact of the estimation error with respect to the mean, the
above procedure is repeated, but now the random pairs(𝜇̂i, Σ̂
0), i = 1,…,K, are used.
That is, the estimation error is confined to the expected returns. Likewise, the impact
of the estimation error for the return dispersion can be evaluated by generating random pairs (𝜇̂0, Σ̂ i
), i = 1,…,K. To conclude the exposition of portfolio resampling,
it should be noted that randomized efficient portfolios can be retrieved by averaging
the weights over m and K. This approach should not be viewed as a panacea for coping with estimation errors. The main critique against this approach is the propagation
of errors. The initial values (𝜇̂0, Σ̂
0) from which the random samples are generated
are estimates themselves and are hence contaminated by estimation errors. Therefore,
the initial errors are replicated and mirrored by applying the Monte Carlo analysis.
Furthermore, for the case of constrained portfolio optimizations the above procedure
can yield unintuitive results (see Scherer 2010, Chapter 4).
Further, recall from Chapter 3 that asset returns are in general not multivariate
normally distributed. This implies that, in addition to estimation errors, a model error often exists. A non-stationary return process would be modelled according to a
distribution for stationary processes. Hence, there is a trade-off between using a distribution assumption for stationary processes on the one hand, thereby committing a
model error, and using a longer sample span by which the stationarity assumption is
more likely to be violated but the estimation error diminishes.
The above-stated consequences of estimation errors could in principle be ameliorated beforehand by imposing restrictions on the weights. The following example
elucidates the effect of placing constraints on the portfolio weights. Consider two
independent investment opportunities A and B with an expected return of 3% and a
volatility of 10%. A return-maximizing agent would be indifferent to all linear combinations between these two assets. However, an estimation error as high as one basis
52 MODERN PORTFOLIO THEORY
point would result in a very different outcome. Suppose that the estimates for the
expected returns are 𝜇̂A = 3.01 and 𝜇̂B = 2.99, respectively. This would imply an
infinitely high long position in asset A that is financed by an equal-sized short position in asset B. Matters are rather different if long-only and/or bound constraints
are included in the optimization. It was found that these kinds of restrictions yield a
favorable out-of-sample performance (see, for instance, Frost and Savarino 1988) or
are associated with a reduced portfolio risk (see, for instance, Gupta and Eichhorn
1998; Jagannathan and Ma 2003). Both of these empirical findings can be traced
back to a smaller implied estimation error if restrictions are imposed on the weights.
It is worth mentioning that the locus of portfolios in the (𝜇, 𝜎) plane are inferior to
efficient portfolios to a greater degree as the restrictions become more binding. However, in general an investor is eager to achieve a portfolio allocation that comes as
close as possible to the efficient frontier. But the implementation of long-only constraints is undesirable for other reasons. For instance, the implementation of most of
the hedge-fund type strategies requires short positioning to be allowed. In summary,
the imposition of constraints is not a panacea for all kinds of portfolio strategies and
optimizations. Part III of this book will address these issues in more detail and also
offer examples of how these more recent advances in portfolio construction can be
explored with R