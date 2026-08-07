The generalized hyperbolic distribution
The GHD was introduced into the literature by Barndorff-Nielsen (1977). The application of this distribution to the increments of financial market price processes
Financial Risk Modelling and Portfolio Optimization with R, Second Edition. Bernhard Pfaff.
© 2016 John Wiley & Sons, Ltd. Published 2016 by John Wiley & Sons, Ltd.
Companion Website: www.pfaffikus.de
58 SUITABLE DISTRIBUTIONS FOR RETURNS
was probably first proposed by Eberlein and Keller (1995). Further contributions followed in which this distribution class was applied to financial market data. The work
of Prause (1997), Barndorff-Nielsen (1997), Barndorff-Nielsen (1998), Eberlein and
Prause (1998), and Prause (1999) paved the way for this distribution class to become
more widely known in the financial community. The generalized hyperbolic distribution owes its name to the fact that the logarithm of the density function is of hyperbolic
shape, whereas the logarithmic values of the normal distribution are parabolic.
The density of the GHD is given by
gh(x; 𝜆, 𝛼, 𝛽, 𝛿, 𝜇) = a(𝜆, 𝛼, 𝛽, 𝛿)(𝛿2 + (x − 𝜇)
2)
(𝜆−1
2 )∕2
× K𝜆− 1
2
(𝛼
√
𝛿2 + (x − 𝜇)2) exp (𝛽(x − 𝜇)), (6.1)
where a(𝜆, 𝛼, 𝛽, 𝛿) is defined as
a(𝜆, 𝛼, 𝛽, 𝛿) = (𝛼2 − 𝛽2)
𝜆∕2
√
2𝜋𝛼𝜆−1∕2𝛿𝜆K𝜆(𝛿
√𝛼2 − 𝛽2)
(6.2)
and K𝜈 denotes a modified third-order Bessel function with index value 𝜈. The density
is defined for x ∈ ℝ and encompasses five parameters: 𝜆, 𝛼, 𝛽, 𝛿, 𝜇. The allowable
parameter space is defined as 𝜆, 𝜇 ∈ ℝ, 𝛿 > 0, 𝛿 > 0, and 0 ≤ |𝛽| < 𝛼. The parameter
𝜆 can be interpreted as a class-defining parameter, whereas 𝜇 and 𝛿 are location and
scale parameters.
Three reparameterizations of the GHD can also be found in the literature:
𝜁 = 𝛿
√
𝛼2 − 𝛽2, 𝜌 = 𝛽∕𝛼,
𝜉 = (1 + 𝜁)
−1∕2, 𝜒 = 𝜉∕𝜌,
𝛼̄ = 𝛼𝛿, 𝛽̄ = 𝛽𝛿. (6.3)
These reparameterizations have in common a lack of location and scale parameters.
Put differently, these parameterizations do not change for affine transformations of the
random variable x. Figure 6.1 shows the densities for different parameter constellations. As is evident from this graph, it is possible to capture not only semi-strong tails
(i.e., with a kurtosis greater than 3), but also skewed distributions. From an intuitive
point of view it should be reasonable to expect that the following continuous distributions can be derived from the GHD: the hyperbolic, hyperboloid, normal inverse
Gaussian, normal reciprocal inverse Gaussian, normal, variance gamma, Student’s t,
Cauchy, generalized inverse Gaussian (GIG), and skewed Laplace distributions.
The HYP is a special case of the GHD. If the parameter 𝜆 = 1, then the following
density results:
hyp(x; 𝛼, 𝛽, 𝛿, 𝜇) =
√𝛼2 − 𝛽2
2𝛿𝛼K1(𝛿
√𝛼2 − 𝛽2
exp (−𝛼
√
𝛿2 + (x − 𝜇)2 + 𝛽(x − 𝜇)), (6.4)
where x, 𝜇 ∈ ℝ, 0 ≤ 𝛿, and |𝛽| < 𝛼.

![alt text](image.png)

As mentioned above, 𝜆 can be interpreted as a class-selecting parameter. Analogously to the reparameterization of the GHD, the parameters of the HYP can be
expressed in these specifications. Here, the reparameterization in the form of (𝜉,𝜒)
is of particular interest, since the defined range is given by 0 ≤ |𝜒| <𝜉< 1. This
relation describes a triangle, the so-called shape triangle. Asymptotically, the parameters reflect the third and fourth moments of the distribution (skewness and kurtosis).
The HYP can itself be viewed as a general class of distributions which encompasses
the following distributions at the limit: for 𝜉 → 0 a normal distribution results; for
𝜉 → 1 one obtains symmetric and asymmetric Laplace distributions; for 𝜒 → ±𝜉 the
HYP converges to a generalized inverse Gaussian distribution; and for |𝜒| → 1 an
exponential distribution results. The shape triangle can therefore be used as a graphical means of assessing whether a return process can be approximated by one these
distributions.
The NIG distribution can be derived from the GHD if the class-selecting parameter
is set to 𝜆 = −1∕2. The density of the NIG is given by
nig(x; 𝛼, 𝛽, 𝛿, 𝜇) = 𝛼𝛿
𝜋 exp (𝛿
√
𝛼2 − 𝛽2 + 𝛽(x − 𝜇))
K1(𝛼
√𝛿2 + (x − 𝜇)2)
√𝛿2 + (x − 𝜇)2
, (6.5)
where the parameter space is defined as x, 𝜇 ∈ ℝ, 0 ≤ 𝛿, and 0 ≤ |𝛽| ≤ 𝛼. For instance, this distribution was employed by Barndorff-Nielsen (1998) to model financial market time series.
60 SUITABLE DISTRIBUTIONS FOR RETURNS
The unknown parameters can be estimated by the maximum likelihood (ML) principle for a given sample. However, closed-form estimators cannot be derived and
hence the negative log-likelihood has to be minimized numerically.
6.3 The generalized lambda distribution
The GLD is an extension of the family of lambda distributions proposed by Tukey
(see Tukey 1962). The latter family is defined by the quantile function Q(u) with
u ∈ [0, 1], that is, the inverse of the distribution function:
Q(u) = {u𝜆−(1−u)
𝜆
𝜆 𝜆 ≠ 0, log u
1−u 𝜆 = 0. (6.6)
The parameter 𝜆 is referred to as a shape parameter and Q(u) is symmetric. It should
be noted that this quantile function does not have a simple closed form for any parameter values 𝜆, except for 𝜆 = 0, and hence the values of the density and distribution
function have to be computed numerically. Incidentally, the density function can be
expressed parametrically for all values of 𝜆 in terms of the quantile function, as in the
equation above, and the reciprocal of the quantile density function, that is, the first
derivative of (6.6). Tukey’s lambda distribution is termed a family of distributions,
because many other statistical distributions can be approximated by it. For instance,
if 𝜆 = −1 then Q(u) behaves approximately as a Cauchy distribution, and if 𝜆 = 1 a
uniform [−1, 1] distribution results. Indeed, an approximate distribution for a given
data series can be discerned by plotting the probability plot correlation coefficient.
By splitting the parameter 𝜆 in (6.6) into distinct parameters, one obtains the
GLD. Here, different parameterizations have been proposed in the literature. A
four-parameter extension of the quantile function is due to Ramberg and Schmeiser
(1974):
Q(u)RS = 𝜆1 + u𝜆3 − (1 − u)
𝜆4
𝜆2
. (6.7)
Tukey’s lambda distribution is recovered from this specification when 𝜆1 = 0 and
𝜆2 = 𝜆3 = 𝜆4 = 𝜆. The four parameters represent the location (𝜆1), the scale (𝜆2),
and the shape characteristics (𝜆3 and 𝜆4) of a distribution. A symmetric distribution
is given for 𝜆3 = 𝜆4. The characteristics of this specification have been extensively
investigated by Ramberg and Schmeiser (1974), Ramberg et al. (1979), King and
MacGillivray (1999), and Karian and Dudewicz (2000), among others. As it turns
out, not all parameter combinations yield a valid density/distribution function. The
probability density function of the GLD at the point x = Q(u) is given by
f(x) = f(Q(u)) =
𝜆2
𝜆3u𝜆3−1 + 𝜆4(1 − u)𝜆4−1 . (6.8)
Valid parameter combinations for 𝛌 must yield the following, such that (6.8) qualifies as a density function:
f(x) ≥ 0 (6.9)
SUITABLE DISTRIBUTIONS FOR RETURNS 61
and
∫ f(x)dx = 1. (6.10)
Originally, only four regions of valid parameter constellations for 𝜆3 and 𝜆4 were
identified by Ramberg and Schmeiser (1974). In Karian et al. (1996) this scheme
was amended by additional regions which are labeled “5” and “6” in Figure 6.2.
The distributions pertinent to these regions share the same boundaries as for adjacent
regions. The parameter constellations for the four/six regions and the implied support
boundaries of the GLD are replicated in Table 6.1.
![alt text](image-1.png)
![alt text](image-2.png)


62 SUITABLE DISTRIBUTIONS FOR RETURNS
Two observations can be made from Table 6.1. First, the support of the GLD distribution can change quite abruptly for slightly different parameter constellations.
Second, parameter constellations that fall in the third quadrant imply skewed and
heavy-tailed distributions. These characteristics are part of the stylized facts about
financial return series that were stated earlier. Recalling that the market risk measures VaR and ES are quantile values, the GLD seems to be an ideal candidate for
computing these measures. This will be shown further below.
In order to avoid the problem that the GLD is confined to certain parameter constellations for 𝜆3 and 𝜆4, Freimer et al. (1988) proposed a different specification:
Q(u)FMKL = 𝜆1 +
u𝜆3−1
𝜆3
− (1−u)
𝜆4
𝜆4
𝜆2
. (6.11)
This specification yields valid density functions over the entire (𝜆3, 𝜆4) plane. The distribution given by this specification will have finite kth-order moment if min(𝜆3, 𝜆4) >
−1∕k.
Recently, Chalabi et al. (2010, 2011) proposed a respecification of the GLD. This
proposed approach is a combination of using robust estimators for location, scale,
skewness, and kurtosis, and expressing the tail exponents 𝜆3 and 𝜆4 by more intuitive
steepness and asymmetric parameters 𝜉 and 𝜒. The new parameterization takes the
following form:
𝜇̂ = u0.5, (6.12)
𝜎̂ = u0.75 − u0.25, (6.13)
𝜒 = 𝜆3 − 𝜆4
√1 + (𝜆3 − 𝜆4)2
, (6.14)
𝜉 = 1
2 − 𝜆3 + 𝜆4
2 ×
√1 + (𝜆3 + 𝜆4)2
. (6.15)
Here, the bounds for 𝜒 and 𝜉 are −1 <𝜒< 1 and 0 ≤ 𝜉 < 1, respectively. The quantile function of the GLD can then be written as
Q(u|𝜇, ̂ ̂ 𝜎,𝜒, 𝜉) = 𝜇̂ + 𝜎̂ Ŝ(u|𝜒,𝜉) − Ŝ(0.5|𝜒,𝜉)
Ŝ(0.75|𝜒,𝜉) − Ŝ(0.25|𝜒,𝜉)
. (6.16)
The function Ŝ(u|𝜒,𝜉) is defined for the following cases:
Ŝ(u|𝜒,𝜉)
⎧
⎪
⎪
⎨
⎪
⎪
⎩
log(u) − log(1 − u) 𝜒 = 0, 𝜉 = 0.5,
log(u) − (1−u)
2𝛼−1
2𝛼 𝜒 = 2𝜉 − 1,
u2𝛼−1
2𝛼 − log(1 − u) 𝜒 = 1 − 2𝜉,
u𝛼+𝛽−1
𝛼+𝛽 − (1−u)
𝛼−𝛽−1
𝛼−𝛽 otherwise,
![alt text](image-3.png)

where
𝛼 = 1
2
0.5 − 𝜉
√𝜉(1 − 𝜉)
, (6.18)
𝛽 = 1
2
𝜒
√1 − 𝜒2
. (6.19)
In this parameterization the GLD has infinite support if the condition (|𝜒| + 1)∕2 ≤
𝜉 is met. Akin to the shape triangle of the HYP, one can now construct a triangle which
starts at 𝜒 = 0 and has as corners (𝜉 = 1, 𝜒 = −1) and (𝜉 = 1, 𝜒 = 1). All parameter
combinations of 𝜒 and 𝜉 would thus give a distribution with infinite support. The
GLD shape plot is shown in Figure 6.3.
As already hinted, the computation of VaR and ES can easily be achieved when a
return series has been fitted to the GLD. Here, the formulas are expressed in terms of
returns and not for the losses, which are expressed as positive numbers. The VaR for
a given probability of error is given by
VaR𝛼 = Q(u|𝛌)
= 𝜆1 + 𝛼𝜆3 − (1 − 𝛼)
𝜆4
𝜆2
, (6.20)
and the formula for computing the ES for a given probability of error can be expressed
as
ES𝛼 = ∫
VaR
−∞
xf(x|𝛌)dx = ∫
𝛼
−∞
Q(u|𝛌)du
= 𝜆1 +
1
𝜆2(𝜆3 + 1)
𝛼𝜆3+1 +
1
𝜆2(𝜆4 + 1)
[
(1 − 𝛼)
𝜆4+1 − 1
]
. (6.21)
64 SUITABLE DISTRIBUTIONS FOR RETURNS
Various estimation methods for finding optimal values for the parameter vector 𝛌
have been proposed in the literature. Among these are
• the moment-matching approach
• the percentile-based approach
• the histogram-based approach
• the goodness-of-fit approach
• maximum likelihood and maximum product spacing.
The method of moment matching was suggested in the seminal papers of Ramberg
and Schmeiser (1974) and Ramberg et al. (1979). The first four moments are matched
to the distribution parameters 𝜆1, ··· , 𝜆4. For 𝜆1 = 0, the kth moment of the GLD is
defined as
𝔼(Xk
) = 𝜆−k
2
∑
k
i=0
(k
i
)
(−1)
i
𝛽(𝛼, 𝛾), (6.22)
where 𝛽(𝛼, 𝛾) denotes the beta function evaluated at 𝛼 = 𝜆3(k − i) + 1 and 𝛾 = 𝜆4i
+ 1. A nonlinear system of four equations in four unknowns results, and has to be
solved. Incidentally, this can be accomplished sequentially, by first determining estimates for 𝜆3 and 𝜆4 and then solving for the two remaining parameters (see Ramberg
and Schmeiser 1974, Section 3). This approach is only valid in the parameter regions
for which these moments exist (region 4), and the condition min(𝜆3, 𝜆4) < −1∕4 must
be met. As an aside, because the estimates for the skewness and the kurtosis of a data
set are very sensitive to outliers, the resulting parameter vector 𝛌 is affected likewise.
In order to achieve robust estimation results with respect to outlier sensitivity, Chalabi
et al. (2010) suggested replacing the moment estimators by their robust counterparts.
The robust moments for location, scale, skewness, and kurtosis are defined as (see,
for instance, Kim and White 2004):
𝜇r = 𝜋1∕2, (6.23)
𝜎r = 𝜋3∕4 − 𝜋1∕4, (6.24)
sr = 𝜋3∕4 + 𝜋1∕4 − 2𝜋1∕2
𝜋3∕4 − 𝜋1∕4
, (6.25)
kr = 𝜋7∕8 − 𝜋5∕8 + 𝜋3∕8 − 𝜋1∕8
𝜋6∕8 − 𝜋2∕8
. (6.26)
These statistics can be estimated by inserting the empirical quantiles pq. It is shown
in Chalabi et al. (2010) that the higher robust skewness and kurtosis moments only
depend on 𝜆3 and 𝜆4. Hence, a nonlinear system of two equations in two unknowns
results, which has to be solved. The robust estimation of the GLD parameters has
the further advantage of deriving a standardized distribution characterized by a zero
median, a unit interquartile range, and the two shape parameters 𝜆1 and 𝜆2:
SUITABLE DISTRIBUTIONS FOR RETURNS 65
Q(u|𝜆3, 𝜆4) = Q(u|𝜆∗
1, 𝜆∗
2, 𝜆3, 𝜆4),
𝜆∗
2 = S𝜆3,𝜆4
(3∕4) − S𝜆3,𝜆4
(1∕4),
𝜆∗
1 = −S𝜆3,𝜆4
(1∕2)∕𝜆∗
2, (6.27)
where S𝜆3,𝜆4
(u) is equal to the numerator in (6.7).
Karian and Dudewicz (1999) proposed an estimation approach based on the empirical percentiles of the data. From the order statistics 𝜋̂p of the data the following
four percentiles are defined, where u ∈ (0, 0.25):
p̂1 = 𝜋̂0.5, (6.28)
p̂ 2 = 𝜋̂1−u − 𝜋̂u, (6.29)
p̂ 3 = 𝜋̂0.5 − 𝜋̂u
𝜋̂1−u − 𝜋̂0.5
, (6.30)
p̂ 4 = 𝜋̂0.75 − 𝜋̂0.25
p̂2
. (6.31)
For u = 0.1 these percentiles refer to the sample median (p̂ 1), the interdecile range
(p̂ 2), the left–right tail weight ratio (p̂ 3), and a measure of relative tail weights of the
left tail to the right tail (p̂4). These quantiles correspond to the following quantiles of
the GLD:
p1 = Q(0.5) = 𝜆1 +
0.5𝜆3 − 0.5𝜆4
𝜆2
, (6.32)
p2 = Q(1 − u) − Q(u) = (1 − u)
𝜆3 − u𝜆4 + (1 − u)
𝜆4 − u𝜆3
𝜆2
, (6.33)
p3 = Q(0.5) − Q(u)
Q(1 − u) − Q(0.5) = (1 − u)
𝜆4 − u𝜆3 + 0.5𝜆3 − 0.5𝜆4
(1 − u)𝜆3 − u𝜆4 + 0.5𝜆4 − 0.5𝜆3
, (6.34)
p4 = Q(0.75) − Q(0.25)
p2
= 0.75𝜆3 − 0.25𝜆4 + 0.75𝜆4 − 0.25𝜆3
(1 − u)𝜆3 − u𝜆4 + (1 − u)𝜆4 − u𝜆3
. (6.35)
This nonlinear system of four equations in four unknowns has to be solved. Similar to the moment-matching method, a sequential approach by first solving only the
subsystem consisting of p̂ 3 = p3 and p̂ 4 = p4 for 𝜆3 and 𝜆4 can be applied.
Deriving estimates for 𝛌 from histograms was proposed by Su (2005, 2007). Within
this approach the empirical probabilities are binned in a histogram and the resulting
midpoint probabilities are fitted to the true GLD density. A drawback of this method
is that the resultant estimates are dependent on the chosen number of bins.
The fourth kind of estimation method is based on goodness-of-fit statistics, such as
the Kolmogorov–Smirnov, Cramér–von Mises, or Anderson–Darling statistics. These
statistics measure the discrepancy between the hypothetical GLD and the empirical
distribution, which is derived from the order statistics of the data in question. Parameter estimates can be employed when these statistics are minimized with respect to the
parameters of the GLD. The determination of the parameter values can be achieved

with the starship method as proposed by Owen (1988) and adapted to the fitting of
the GLD by King and MacGillivray (1999). It consists of the following four steps:
1. Compute the pseudo-uniform variables of the data set.
2. Specify a valid range of values for 𝜆1,…, 𝜆4 and generate a four-dimensional
grid of values that obey these bounds.
3. Calculate the goodness-of-fit statistics compared to the uniform (0, 1) distribution.
4. Choose the grid point (𝜆1, 𝜆2, 𝜆3, 𝜆4) that minimizes the goodness-of-fit statistic as the estimate for 𝛌.
Finally, the GLD parameters could also be estimated by the ML principle and/or
the method of maximum product spacing. The latter method was proposed separately
by Cheng and Amin (1983) and Ranneby (1984). This method is also based on the
order statistics {x(1), x(2),…, x(N)} of the sample {x1, x2,…, xN} of size N. Next, the
spacings between adjacent points are defined as D(x(i)|𝛌) = F(x(i)|𝛌) − F(x(i−1)|𝛌) for
i = 2,…,N. The objective is the maximization of the sum of the logarithmic spacings. Compared to the ML method, the maximum product spacing method has the
advantage of not breaking down when the support of the distribution is not warranted
for a given parameter combination.
6.4 Synopsis of R packages for GHD
6.4.1 The package fBasics
The package fBasics is part of the Rmetrics suite of packages (see Würtz et al. 2014).
The primary purpose of this package is to provide basic tools for the statistical analysis of financial market data. Within the package S4 classes and methods are utilized.
The package is considered a core package in the CRAN “Finance” Task View and
is also listed in the “Distributions” Task View. The package has dependencies on
other packages contained in the Rmetrics suite. With respect to the modelling, fitting,
and inferences drawn from the GHD, quite a few functions have been directly ported
and/or included from the package GeneralizedHyperbolic to this package. The latter
package will be presented in the next subsection.
With respect to the topic of this chapter, the following distributions are addressed
in this package: the generalized hyperbolic, the generalized hyperbolic Student’s t,
the hyperbolic, and the normal inverse Gaussian, as well as the standardized versions of the GHD and NIG distributions. For each of these distributions, functions
for calculating the value of the density, the probabilities, the quantiles, and the generation of random numbers are available. The R naming convention for the density
(prefix d), distribution (prefix p), quantile function (prefix q), and the generation of
random numbers (prefix r) is followed. In addition, routines for fitting and for calculation of the mode and moments are included in the package. In particular, the
mean, variance, skewness, and kurtosis are implemented for all distributions. It is
SUITABLE DISTRIBUTIONS FOR RETURNS 67
further possible to return their robust counterparts, namely, the median, the interquartile range, and skewness or kurtosis measures that are derived from these quartiles.
The shape of the density for the GHD, HYP, and NIG can be plotted interactively for
various parameter combinations through a tcl/Tk interface. These functions are
termed ghSlider(), hypSlider(), and nigSlider(), respectively, and are
intended primarily for illustrative purposes.
The functions that relate to the GHD have gh in their names, while those for
the generalized hyperbolic Student’s t have ght, those for the HYP have hyp, and
those for the NIG have nig. Thus, the routines for fitting these distributions to
financial market return data are termed fooFit() where foo is replaced by one
of these abbreviations. Similarly, the mode is returned by the function fooMode()
and the routines for the moments are fooMean(), fooVar(), fooSkew(),
and fooKurt() for the mean, the variance, the skewness, and the kurtosis, respectively. Analogously, the functions fooMED(), fooIQR(), fooSKEW(), and
fooKURT() relate to the robust counterparts, namely the median, the interquartile
range, and the robust definitions of the skewness and the kurtosis.
By default, the unknown parameters of the distributions are estimated by applying
the ML principle. Here, the negative log-likelihood is minimized with the function
nlminb(). It should be noted that the ellipsis argument in the function fooFit()
is passed down to the plotting of the fitted distribution, hence the user cannot pass
arguments directly to the optimization routine. With respect to fitting the NIG, in
addition to the ML principle, the parameters can be estimated by the generalized
methods of moments, maximum product spacing, or minimum variance product spacing. It is also possible to produce a shape triangle for fitted objects with the routine
nigShapeTriangle(). All fit() methods return an object of formal class
fDISTFIT, for which a show() method is defined.
6.4.2 The package GeneralizedHyperbolic
This package offers functions not only for the GHD, but also for the derived distributions HYP, GIG, and skew Laplace (see Scott 2015). The package is written purely
in R. A NAMESPACE file is included in the package’s source that contains the export
directives for the functions and S3 methods pertinent to the above-mentioned distributions. Some of the routines contained in this package have been ported to fBasics.
Routines for fitting the hyperbolic, normal inverse Gaussian, and generalized inverse
Gaussian distributions to data have been implemented. Six data sets from the fields
of geology, engineering, and finance are provided. The package is contained in the
CRAN Task View “Distributions.”
The functions that relate to the generalized hyperbolic have the acronym ghyp in
their names. Routines for the density, the distribution, the quantile function, and the
generation of random numbers are implemented, and the dpqr naming convention
as introduced in Section 6.4.1 is followed. Furthermore, the first derivative of the
density function has been implemented as function ddghyp(). Quantile–quantile
and percentile–percentile plots for a given set of parameters and an observed
time series have been implemented as functions qqghyp() and ppghyp(),
68 SUITABLE DISTRIBUTIONS FOR RETURNS
respectively. It is further possible to return the ranges on the real line where the
probability mass is small for a given parameter set (ghypCalcRange()). Whether
certain parameters are in the allowable set of values can be checked with the function
ghypCheckPars(). Furthermore, with the routine ghypChangePars() the
user can calculate the parameters for the alternative specifications of the GHD. The
moments and mode of the GHD distribution can be computed with the functions
ghyperbMean(), ghyperbVar(), ghyperbSkew(), ghyperbKurt(),
and ghyperbMode() for the mean, variance, skewness, kurtosis, and mode,
respectively. The moments of the GHD can also be computed with the function
ghypMom().
The chosen acronym for the hyperbolic distribution in this package is hyperb.
The dpqr naming convention is followed as in the case of the generalized hyperbolic
distribution, and the first derivative of the density function has been implemented
as function ddhyperb(). The two-sided Hessian matrix for a given data vector
and parameter set can be calculated by calling hyperbHessian(). The points
on the real line for which the probability mass for a given set of parameters
is negligibly small can be determined by means of the routine hyperbCalcRange(). Conversion from one HYP parameterization to another is accomplished
by invoking hyperbChangePars(). A similar group of functions to the case
of the GHYP for recovering the moments is also made available, now prefixed
by hyperb instead of ghyp. The fitting of the HYP distribution is achieved
with the function hyperbFit(). Suitable starting parameters can be determined
with the function hyperbFitStart(). The user has the option to choose
between six different numerical optimization algorithms, namely Nelder–Mead,
BFGS (Broyden–Fletcher–Goldfarb–Shanno), and L-BFGS-B (all implemented in
optim(), nonlinear minimization (nlm()), or constrained optimization (constrOptim()). Arguments to control the behavior of the optimizer can be specified
in the call to hyperbFit(). This function returns an object with class attributes
hyperbFit, distFit. For objects of this kind, print(), summary(), and
plot() methods have been defined. In addition, there are coef() and vcov()
methods for retrieving the estimated parameters and their variance-covariance matrix.
The fit can be assessed in the form of a quantile–quantile (QQ) plot (qqhyperb())
or probability–probability (PP) plot (pphyperb()). Furthermore, a Cramér–von
Mises goodness-of-fit test is implemented as function hyperbCvMTest(). This
function returns an object with class attribute hyperbCvMTest for which a
print() method has been defined. Finally, a linear model with hyperbolic errors
can be fitted by utilizing hyperblm().
Basically, the same set of functions that have been defined for the HYP are made
available for the generalized inverse Gaussian (acronym gig). In addition, the moments and raw moments for a given parameter specification are computed by the
functions gigMom() and gigRawMom(), respectively. The moments of its special cases, namely the gamma and inverse gamma distributions, can be invoked by
gammaRawMom(). Similarly, the same set of functions that have been defined for
the GHD are made available for the GIG. In addition, QQ and PP plot routines are
included in the package for this distribution.
SUITABLE DISTRIBUTIONS FOR RETURNS 69
In addition, the functions that directly relate to the skew Laplace distribution
(acronym skewlap) are available: the density, the distribution, the quantile
function, and the generation of random numbers, as well as methods for producing
QQ and PP plots.    

 The package ghyp
In contrast to the previous package, ghyp provides functions for fitting not only the
univariate HYP, but also the GHD, NIG, VG, Student’s t, and Gaussian distributions
for the univariate and multivariate cases (see Luethi and Breymann 2013). The package utilizes S4 classes and methods and is shipped with a NAMESPACE file. It is
contained in the CRAN “Distributions” and “Finance” Task Views. In addition to the
package’s help files, a vignette is available.
The functions that relate to the GHD or the GIG are the density, quantile, probability, and random variates routines. The dpqr naming convention is followed and
the chosen acronyms are ghyp and gig for the GHD and the GIG, respectively.
A feature of this package is the inclusion of routines for calculating the expected
shortfall for these distributions. The functions are named ESghyp() and ESgig().
Furthermore, the package offers a function for portfolio optimization (portfolio.optimize()). The user can choose the risk measure employed, namely the
standard deviation, the VaR, or the ES, and whether the portfolio should be a minimum risk, a tangency, or a target return portfolio. These portfolios are derived from
a multivariate GHD.
To estimate the unknown coefficients of the GHD and its special cases, the ML
principle is employed. The function names are made up of the prefix fit. followed
by the acronym of the desired distribution, followed by either uv or mv for fitting
univariate or multivariate data. The objects returned are of formal class mle.ghyp.
For objects of this kind, show() and summary() methods are defined as well
as methods for extracting the Akaike information criterion (AIC) and the value of
the log-likelihood. Furthermore, a routine for model selection using the AIC is implemented as function stepAIC.ghyp(). In addition, a function for discriminating between models in the form of a likelihood ratio test is implemented (see routine lik.ratio.test()). The estimated parameters can be extracted with the
coef() method. The moments of objects that inherit from the class ghyp can be
computed with the function mean() for the mean, with the function vcov() for
the variance in the univariate and the variance-covariance matrix in the multivariate
case, and with the functions ghyp.skewness() and ghyp.kurtosis() for the
skewness and kurtosis, respectively. In general, central and non-central moments can
be computed with the function ghyp.moment(). By default, the skewness and the
kurtosis are returned.
For plotting purposes, a QQ plot, a histogram view, and a pairs plot for the graphical
display of multivariate QQ plots, as well as plotting the density or superimposing the
density on existing plot devices, are available. The functions are termed qqghyp(),
hist(), pairs(), plot(), and lines(), in that order.
70 SUITABLE DISTRIBUTIONS FOR RETURNS
The package comes with two data sets. The first, indices, contains monthly
returns for five asset classes between August 1999 and October 2008. The second
data set (smi.stocks) contains daily return data for the Swiss equity market and
equity returns of selected Swiss companies from 5 January 2000 to 10 January 2007.
6.4.4 The package QRM
Most of the examples contained in McNeil et al. (2005) can be replicated with the
functions contained in the package QRM (see Pfaff and McNeil 2016). These were
originally written in the S-PLUS language by A. McNeil and distributed as package QRMlib. An initial R port was accomplished by S. Ulman and is still available
from the CRAN archive (see McNeil and Ulman 2011). The package QRM is based
on this initial R port. It has dependencies on the CRAN packages gsl, mvtnorm,
numDeriv, and timeSeries. Within QRM partial use of S3 classes and methods is
made. The more burdensome computations are interfaced from C routines. In addition, 14 financial data sets are available.
With respect to the GHD, functions for fitting data to its special cases, namely the
NIG and HYP, are included in this package. These are termed fit.NH() for univariate and fit.mNH() for multivariate data. The case argument of these functions
controls whether the negative log-likelihood of the NIG or HYP is minimized. Both
routines return a list object without a class attribute. Hence, no further methods are
available.
In addition, the moment and log moment of the GIG can be computed with the
functions EGIG() and ElogGIG(), respectively. Random variates of this distribution can be generated with the function rGIG() that interfaces to a routine written
in C.
6.4.5 The package SkewHyperbolic
The package SkewHyperbolic is dedicated solely to the modelling and fitting of the
skew hyperbolic Student’s t distribution (see Scott and Grimson 2015). The package
is written purely in R, and S3 classes and methods are used. It is shipped with a
NAMESPACE file, and some underlying utility functions are imported from the packages GeneralizedHyperbolic and DistributionUtils. As well as the functions that
primarily deal with the skew hyperbolic distribution, three data sets are included in
the package.
With respect to the distribution itself, routines for its density, distribution, and
quantile functions as well as for the generation of random variates are included. The
dpqr naming convention is followed, and the chosen acronym for this distribution
is skewhyp. In addition to these functions there is a routine for returning the first
derivative of the density function (ddskewhyp()). Similar to the package GeneralizedHyperbolic, a function for determining ranges for which the probability mass
is small is available (skewhypCalcRange()). The coherence of a parameter set
can be checked with the function skewhypCheckPars().
The included routines skewhypMean(), skewhypVar(), skewhypSkew(),
and skewhypKurt() are used for calculating the mean, variance, skewness, and
SUITABLE DISTRIBUTIONS FOR RETURNS 71
kurtosis, respectively. The mode of the distribution for a given parameter set can be
computed with skewhypMode(). Similarly to the package GeneralizedHyperbolic, the central and non-central moments of any order can be calculated with the
routine skewhypMom().
The fitting of data to the skew hyperbolic Student’s t distribution is accomplished
by the function skewhypFit(). Suitable starting values can be determined with
the routine skewhypFitStart(). The parameters are determined numerically
by applying the ML principle. The negative log-likelihood is minimized by employing either the general purpose optimizer optim() or the function nlm(). For the
former the user can use either the BFGS or Nelder–Mead algorithm. The function
skewhypFit() returns an object of informal class skewhypFit. For objects of
this kind, print(), plot(), and summary() methods are available. Goodness of
fit can be inspected graphically by means of a QQ and/or PP plot. The relevant functions are termed qqskewhyp() and ppskewhyp(), respectively. In addition, a
function for producing a tail plot line (skewhypTailPlotLine()) for a given
data set and parameter specification is provided.
6.4.6 The package VarianceGamma
The package VarianceGamma can be considered as a twin package to the SkewHyperbolic package discussed in the previous subsection, but its focus is on the
variance gamma distribution (see Scott and Dong 2015). As its twin, the package is
contained in the CRAN “Distributions” Task View. Within the package S3 classes
and methods are employed and the package is shipped with a NAMESPACE file in
which import directives for the utility functions contained in the packages GeneralizedHyperbolic and DistributionUtils are included. Basically, all functionalities
contained in the package SkewHyperbolic have been mirrored in this package, and
the dpqr naming convention is followed. The acronym vg is used for the variance
gamma distribution. Hence, the discussion of the functions, methods, and classes in
Section 6.4.5 carries over to these instances, too.
6.5 Synopsis of R packages for GLD
6.5.1 The package Davies
Even though the focus of the package Davies is an implementation of the Davies
quantile function (see Hankin and Lee 2006), R routines that address the GLD distribution are also included. The package is listed in the CRAN “Distributions” Task
View. The package is shipped with a NAMESPACE file, but neither S3 nor S4 classes/
methods are employed. Hence, in addition to two data sets, the package offers a collection of functions for dealing with these two kinds of distributions—no more and
no less.
With respect to the GLD, the functions are based on the Ramberg–Schmeiser (RS)
specification. The density, distribution, and quantile functions of the GLD have been
implemented, as well as a function for generating random variates, and the dpqr

naming convention is followed for naming these routines, ( e.g., dgld()). Furthermore, the routine dgld.p() is an implementation of the density function expressed
in terms of the quantile.
The expected value of the GLD for a given parameterization can be retrieved either
as an exact value with the routine expected.gld() or as an approximation with
expected.gld.approx(). Within both functions the values are determined as
the sum of a constant (𝜆1) and two Davies quantile functions.
6.5.2 The package fBasics
A general description of the package fBasics has already been provided in Section
6.4.1. Hence, in the following description the focus will be on the R routines for
handling the GLD.
The density, distribution, and quantile functions and a routine for obtaining random
variates have been implemented as R routines, and the dpqr naming convention is
followed ( e.g., dgld()). These functions are wrappers for the bodies of the functions of the routines with the same name contained in the package gld by King et al.
(2016)—see Section 6.5.3 for a discussion of this package. However, these wrapper
functions are limited to the RS specification, and only parameter values for 𝜆1,…, 𝜆4
pertinent to region 4 of the parameter space can be supplied as arguments to these
functions, otherwise an error is returned.
The fitting of data to the GLD is provided by the function gldFit(). Similar
to the above functions, the GLD is expressed in the RS specification and the
optimization is carried out for the parameter space pertinent to region 4. Apart
from the data argument x and the initial parameter values lambda1[234], the
function has an argument method by which the estimation method can be set. The
available estimation procedures are: maximization of the log-likelihood ("mle"),
the method of maximum product spacing ("mps"), robust moment matching
("rob"), goodness of fit ("gof"), and histogram binning ("hist"). If one of the
latter two methods is chosen, the user can set the type of goodness-of-fit statistic
or the binning method via the function’s argument type. This argument is passed
as an ellipsis argument to either of the user-hidden functions .gldFit.gof()
or .gldFit.hist(), respectively. For estimation methods based on goodness
of fit this can be the Anderson–Darling ("ad"), Cramér–von Mises ("cvm"), or
Kolmogorov–Smirnov ("ks") statistic. If the histogram approach is chosen, the
count of bins can be determined by the Freedman–Diaconis binning ("fd"), Scott’s
histogram binning ("scott"), or Sturges binning approach ("sturges"). The
function returns an S4 object fDISTFIT. The estimates, the value of the objective,
and the convergence code of the nlminb() optimizer are returned as a list in
the slot fit of objects of this kind. By default, a plot of the estimated density is
produced, which can be suppressed by setting doplot = FALSE.
The mode of the GLD can be computed for given parameter values of 𝜆1,…, 𝜆4
with the function gldMode(). Robust estimates for location, dispersion, skewness, and kurtosis can be computed for given parameter values with the functions
gldMED(), gldIQR(), gldSKEW(), and gldKURT(), respectively.
SUITABLE DISTRIBUTIONS FOR RETURNS 73
6.5.3 The package gld
The package gld is, to the author’s knowledge, the only one that implements all three
GLD specifications: RS, FMKL, and FM5 (see King et al. 2016). The latter is an
extension of the FMKL version in which a fifth parameter is included in order to
explicitly capture the skewness of the data. The FM5 specification is derived from
the modification of the RS specification by Gilchrist (2000).
The package is included in CRAN “Distributions” Task View. S3 classes and methods have been utilized, and the package contains a NAMESPACE file. The distribution
functions of the GLD specifications are interfaced from routines written in the C language.
The density, quantile density, distribution, and quantile distribution functions are
implemented as R routines dgl(), dqgl(), pgl(), and qdgl(), respectively.
Random variates of the GLD can be generated with the function rgl(). With
respect to parameter estimation, the starship method has been implemented as
function starship(). Here, the initial values are determined according to an
adaptive grid search (starship.adaptivegrid()) and then used in the call
to optim(). The objective function itself is included in the package as function
starship.obj(). The function starship() returns an object of informal
class starship for which plot(), print(), and summary() methods are
made available. The validity of the estimated 𝜆 parameters can be checked with
the function gl.check.lambda(). As a means of assessing the goodness of fit
graphically, the function qqgl() produces a QQ plot. Finally, the density of the
GLD can be depicted with the function plotgl().
6.5.4 The package lmomco
Estimation methods based on L-moments for various distributions are implemented
in the package lmomco (see Asquith 2016). Here we will concentrate on those tools
that directly address the GLD. The package is considered to be a core package in
the CRAN “Distributions” Task View. It is written purely in R and is shipped with a
NAMESPACE file with export directives for all relevant user functions. The package
is quite huge, judged by the size of its manual, which runs to more than 500 pages.
It is worth mentioning that, in addition to estimation methods based on L-moments
and their extensions, probability-weighted moment (PWM) estimators are available.
In order to estimate the parameters of the GLD, the L-moments for univariate
sample data must be determined first. This can be achieved with the function
lmom.ub() for unbiased L-moment estimates, with the function TLmoms() for
trimmed L-moments, or with the function pwm.ub() for unbiased sample PWMs.
If the latter route is chosen, these PWM estimates can be converted to L-moment
estimates with the function pwm2lmom(). Having estimated the L-moments,
the resulting object can be used in the call to the functions pargld() and/or
parTLgld() to estimate the parameters of the GLD by L-moments or trimmed
L-moments, respectively. The package offers routines for checking the validity
of the estimated parameters and/or L-moments (functions are.par.valid(),
74 SUITABLE DISTRIBUTIONS FOR RETURNS
are.pargld.valid(), and are.lmom.valid()) as well as means of
converting between parameter estimates and the associated L-moments for a
given distribution (functions vec2par(), lmom2par(), par2lmom(), and
lmomgld()).
The R functions that directly relate to the GLD are cdfgld() for the cumulative
distribution function, quagld() for the quantile function, and pdfgld() for the
density function. Random variates for a given parameterization of the GLD can
be generated with the function rlmomco(). The correctness of an empirically
determined probability or density function can be assessed with the functions
check.fs() and check.pdf(), respectively.
6.6 Applications of the GHD to risk modelling
6.6.1 Fitting stock returns to the GHD
In this subsection the daily returns of Hewlett Packard (HWP) stock are fitted to the
GHD and its special cases, the HYP and NIG. The R code is shown in Listing 6.1.
The sample runs from 31 December 1990 to 2 January 2001 and consists of 2529 observations. The following analysis has been conducted with the functions contained
in the package ghyp. In the listing this package is loaded into the workspace first.
The package fBasics contains the data set DowJones30, which includes the HWP
stock price. This series is converted into a timeSeries object and the continuous
percentage returns are then computed. For comparison of the fitted distributions, the
empirical distribution (EDF) is first retrieved from the data with the function ef().
Then the returns are fitted to GHD, HYP, and NIG distributions. In each case, possible
asymmetries in the data are allowed (i.e., non-zero skewness). In the next chunk of
code the shapes of the estimated densities are computed, along with a Gaussian distribution which serves as the benchmark. A plot of the empirical and fitted densities
is then produced (see Figure 6.4).
The rather poor description of the empirical return distribution for the Gaussian
case is immediately evident from this plot. The normal distribution falls short of
capturing the excess kurtosis of 4.811. Matters are different for the class of generalized hyperbolic distributions. In these instances the empirical distribution function
is tracked rather well. The fitted HYP and NIG models almost coincide, and from
this plot these two distributions cannot be discerned. The fitted GHD seems to mirror
the returns slightly better. In particular, the values of the density are closer to their
empirical counterparts around the median of the EDF. Ceteris paribus, this implies
higher probability masses in the tails of the distribution compared to the 𝜆-restricted
HYP and NIG distributions.
As a second means of graphically comparing the fitted distributions, QQ plots are
produced in the ensuing code lines of Listing 6.1. These are shown in Figure 6.5. For
clarity the marks of the fitted normal distribution have been omitted from the plot.
The reader is encouraged to adopt the plot accordingly. What has already been concluded from the density becomes even more evident when the QQ plot is examined.

i b r a r y ( ghyp ) 1
library (timeSeries ) 2
library ( fBasics ) 3
## Return calculation 4
data ( DowJones30 ) 5
y <− t i m e S e r i e s ( DowJones30 [ , "HWP" ] , c h a r v e c = 6
as . cha racte r ( DowJones30 [ , 1]) ) 7
yret <− na . omit ( di f f ( log (y ) ) ∗ 100) 8
## Fitting 9
e f <− density ( yret ) 10
ghdfit <− f i t . ghypuv ( y r e t , s ymm et ri c = FALSE , 11
control = li st ( maxit = 1000) ) 12
hypfit <− f i t . hypuv ( y r e t , s ymm et ri c = FALSE , 13
control = li st ( maxit = 1000) ) 14
nigfit <− f i t . NIGuv ( y r e t , s ymm et ri c = FALSE , 15
control = li st ( maxit = 1000) ) 16
## Densities 17
ghddens <− dghyp ( e f $x , g h d f i t ) 18
hypdens <− dghyp ( e f $x , h y p f i t ) 19
nigdens <− dghyp ( e f $x , n i g f i t ) 20
nordens <− dnorm ( e f $x , mean = mean ( y r et ) , sd = 21
sd (c ( yret [ , 1]) ) ) 22
col . def <− c ( " black " , " red " , " blue " , " green " , "orange" ) 23
plot ( ef , xlab = "" , ylab = expression ( f (x) ) , ylim = c (0 , 0.25) ) 24
l i n e s ( e f $x , ghddens , c ol = " red " ) 25
l i n e s ( e f $x , hypdens , c ol = " bl ue " ) 26
l i n e s ( e f $x , nigdens , c ol = " g reen " ) 27
l i n e s ( e f $x , nordens , c ol = " o range " ) 28
legend (" topleft " , 29
l e g e n d = c ( " e m p i r i c a l " , "GHD" , "HYP" , "NIG" , "NORM" ) , 30
col = col . def , lty = 1) 31
## QQ−Plots 32
qqghyp ( g h d f i t , l i n e = TRUE, ghyp . col = " red " , 33
p l o t . l e g e n d = FALSE , g a u s s i a n = FALSE , 34
main = " " , cex = 0.8 ) 35
qqghyp ( h y p f i t , add = TRUE, ghyp . pch = 2 , ghyp . col = " blue " , 36
g a u s s i a n = FALSE , l i n e = FALSE , ce x = 0 . 8 ) 37
qqghyp ( n i g f i t , add = TRUE, ghyp . pch = 3 , ghyp . c o l = " g r e e n " , 38
g a u s s i a n = FALSE , l i n e = FALSE , ce x = 0 . 8 ) 39
l e g e n d ( " t o p l e f t " , l e g e n d = c ( "GHD" , "HYP" , "NIG" ) , 40
col = col . def[−c (1 ,5) ] , pch = 1:3) 41
## Diagnostics 42
AIC <− ste pA IC . ghyp ( y r et , d i s t = c ( " ghyp " , " hyp " , "NIG" ) , 43
s ymm et ri c = FALSE , 44
control = li st ( maxit = 1000) ) 45
LRghdnig <− lik . ratio . test ( ghdfit , nigfit ) 46
LRghdhyp <− lik . ratio . test ( ghdfit , hypfit )

![alt text](image-4.png)

The daily returns can be tracked better with the GHD than with the HYP and NIG
distributions, especially in the tails. Furthermore—this conclusion was less clear from
the density plot—the returns can be slightly better explained by the NIG than by the
HYP distribution.
In the last three lines of the listing, diagnostic measures for the three models are
produced. First, the function stepAIC.ghyp() is utilized to determine with which
distribution the data can be explained best in terms of the AIC. This function returns a

![alt text](image-5.png)

list object with three elements: best.model, all.models, and fit.table.
The latter is of most interest because it not only provides information about the AICs
and the values of the log-likelihood (LLH), but also returns the estimates of the distribution parameters, whether a symmetric distribution has been fitted or not, whether
the optimizer achieved convergence, and the number of iterations required. An excerpt from these results is provided in Table 6.2.
The conclusions drawn from the graphical inspection of the results are mirrored
by their quantitative counterparts. Clearly, a GHD-based model is favored over
the NIG and HYP distributions according to the AIC. However, the differences
between the AIC and/or the log-likelihood of the GHD and NIG are rather small.
A cross-comparison to the values of the HYP model would yield a preference for
the NIG, if one had to choose between the restricted distributions. The reason for
this is primarily that the unrestricted estimate of 𝜆̂ is −2.27 closer to the parameter
restriction for 𝜆 of the NIG than that of the HYP. Whether the differences in the
values for the log-likelihoods are significantly different from zero can be tested by
means of a likelihood ratio test. These tests are carried out in the last two lines of the
R code listing. First, it is checked whether the GHD can be replaced by the NIG. The
value of the test statistic is 0.007 and the p-value is 0.002. Hence, the null hypothesis
that the explanatory power of the two distributions is equal must be rejected at a
confidence level of 95%. The corresponding value of the test statistic for comparing
the GHD with the HYP is 0 and the implied p-value is 0. Here, the null hypothesis
must be rejected even more clearly, which is plausible given the ordering of the three
log-likelihood values.
6.6.2 Risk assessment with the GHD
In this subsection the behavior of the VaR and ES risk measures according to each
of the models is investigated. In particular, the two risks measures are derived from
the fitted GHD, HYP, and NIG distributions for the HWP returns from the previous subsection. These measures are calculated over a span from the 95.0% to the
99.9% levels. The resulting trajectories of the VaR and ES are then compared to their
empirical counterparts. For the ES the mean of the lower quintile values is used.
The relevant code is provided in Listing 6.2. First, the sequence of probabilities is
created for which the VaR and ES are to be computed. Because we are dealing with
returns instead of losses, these are defined for the left tail of the distribution. In the
next lines the VaR for these levels is computed by utilizing the quantile function for
the GHD. By convention, losses are expressed as positive numbers, and hence the
78 SUITABLE DISTRIBUTIONS FOR RETURNS
R code 6.2 VaR and ES derived from the GHD, HYP, and NIG.
## Probabilities 1
p <− seq (0.001 , 0.05 , 0.001) 2
## VaR 3
ghd . VaR <− abs ( qghyp (p , ghd fit ) ) 4
hyp . VaR <− abs ( qghyp (p , hyp fit ) ) 5
ni g . VaR <− abs ( qghyp (p , ni g fit ) ) 6
n o r . VaR <− abs ( qnorm ( p , mean = mean ( y r et ) , 7
sd = sd (c ( yret [ , 1]) ) ) ) 8
emp . VaR <− abs ( quantile (x = yret , probs = p) ) 9
# Pl ot of VaR 10
p l o t ( emp . VaR , t y p e = " l " , xl a b = " " , yl a b = "VaR" , 11
a x e s = FALSE , ylim = r a n g e ( c ( hyp . VaR , ni g . VaR , ghd . VaR , 12
n o r . VaR , emp . VaR ) ) ) 13
box ( ) 14
a x i s ( 1 , a t = s e q ( al o n g = p ) , l a b e l s = names ( emp . VaR ) , 15
t i c k = FALSE ) 16
a x i s ( 2 , a t = p r e t t y ( r a n g e ( emp . VaR , ghd . VaR , hyp . VaR , 17
ni g . VaR , n o r . VaR ) ) ) 18
l i n e s ( s e q ( al o n g = p ) , ghd . VaR , c o l = " r e d " ) 19
l i n e s ( s e q ( al o n g = p ) , hyp . VaR , c o l = " bl u e " ) 20
l i n e s ( s e q ( al o n g = p ) , ni g . VaR , c o l = " g r e e n " ) 21
l i n e s ( s e q ( al o n g = p ) , n o r . VaR , c o l = " o r a n g e " ) 22
legend (" topright " , 23
l e g e n d = c ( " E m p i r i c a l " , "GHD" , "HYP" , "NIG " , " Normal " ) , 24
col = col . def , lty = 1) 25
## ES 26
ghd . ES <− abs ( ESghyp ( p , g h d fit ) ) 27
hyp . ES <− abs ( ESghyp ( p , h y p fit ) ) 28
ni g . ES <− abs ( ESghyp ( p , n i g f i t ) ) 29
n o r . ES <− abs ( mean ( y r et ) − sd (c ( yret [ , 1]) ) ∗ 30
dnorm ( qnorm (1 − p) ) / p) 31
obs . p <− ceiling (p ∗ length ( yret ) ) 32
emp . ES <− sapply ( obs . p , f u n cti o n ( x ) abs ( mean ( s o rt ( c ( y r et ) ) 33
[1:x]) ) ) 34
## Pl ot of ES 35
p l o t ( emp . ES , t y p e = " l " , xl a b = " " , yl a b = "ES " , a x e s = FALSE , 36
ylim = r a n g e ( c ( hyp . ES , ni g . ES , ghd . ES , n o r . ES , emp . ES ) ) ) 37
box ( ) 38
a x i s ( 1 , a t = 1 : l e n g t h ( p ) , l a b e l s = names ( emp . VaR ) , 39
t i c k = FALSE ) 40
a x i s ( 2 , a t = p r e t t y ( r a n g e ( emp . ES , ghd . ES , hyp . ES , ni g . ES , 41
n o r . ES ) ) ) 42
l i n e s ( 1 : l e n g t h ( p ) , ghd . ES , c ol = " r e d " ) 43
l i n e s ( 1 : l e n g t h ( p ) , hyp . ES , c ol = " bl u e " ) 44
l i n e s ( 1 : l e n g t h ( p ) , ni g . ES , c ol = " g r e e n " ) 45
l i n e s ( 1 : l e n g t h ( p ) , n o r . ES , c ol = " o r a n g e " ) 46
legend (" topright " , 47
l e g e n d = c ( " E m p i r i c a l " , "GHD" , "HYP" , "NIG " , " Normal " ) , 48
col = col . def , lty = 1)

![alt text](image-6.png)

absolute values of the quantiles returned by the function are used. The VaR based on
the normal distribution can be computed by providing the necessary estimates for the
location and scale. The VaR values thus determined are compared to their empirical
counterparts, which are determined by the quantile() function.
The development of these risk measures is plotted in Figure 6.6. The quantiles derived from the GHD and its special cases track the associated empirical loss levels
fairly closely. Only in the extreme confidence region of 99.0% or greater is the risk
slightly underestimated by these models. The ordering of the goodness of fit for the
three distributions can also be concluded from this graph: the fitted GHD tracks the
data in that region very well, whereas the risk is underestimated by the NIG and HYP
models. Two conclusions can be drawn from the VaR based on the normal distribution. First, as expected, the normal distribution falls short of capturing extreme risk
events ( i.e., above the 97.5% level). Second, the riskiness of holding a position in the
HWP stock is overestimated for the confidence region between 95.0% and 97.5%.
Put differently, for these levels the VaR derived from the normal distribution is consistently too conservative and hence an investor could be disadvantaged by not being
allowed to take a larger position in that stock.
Next in Listing 6.2, the ES is calculated for the fitted model objects. As mentioned
in Section 6.4.3, this risk measure can be computed with the function ESghyp().
The expected shortfall for the normal distribution is determined by (4.5) in Section
4.2. Similarly to the VaR, the trajectory of the ES for alternative confidence levels is
compared to its empirical counterpart. Here, the mean of the values smaller than the
quantile is employed. The risk measures thus determined are shown in Figure 6.7.
In contrast to the VaR, now the risk measures derived from all models consistently
underestimate the expected loss in the case of such an event. However, this underestimation is less severe for the GHD-based models and for the less conservative levels.
The ES derived from the normal distribution fares worst. Overall, the reason why

![alt text](image-7.png)

the risk is consistently underestimated, regardless of the model chosen, is primarily
that all distributions underestimate the probability of extreme losses and hence these
errors accumulate when the ES is calculated.

 Stylized facts revisited
In this subsection the stylized facts of financial returns are reconsidered by employing the shape triangle of the HYP distribution. Ordinarily, the empirical distribution
of financial market returns is characterized by excess kurtosis and negative skewness. These characteristics are most pronounced for higher-frequency returns ( i.e.,
intra-daily or daily). Therefore, the need arises to utilize models/distributions which
acknowledge these stylized facts. One might also be interested in whether these more
complicated (compared to the normal distribution) models are indeed necessary if
the focus is shifted to lower-frequency return processes ( i.e., weekly, monthly, or bimonthly). As discussed in Section 6.2, the exponential, Laplace, left- or right-skewed
hyperbolic, and normal distributions are contained within the HYP distribution as
limit cases. Whether the HYP can be approximated by one of these distributions can
be graphically inspected by the shape triangle. This tool can also be employed to
assess whether the stylized facts are still applicable for lower-frequency return processes. This kind of analysis is conducted in the R code in Listing 6.3.
The first line of the listing defines the return days used. These correspond to daily,
weekly, biweekly, monthly, and bimonthly returns. The next line computes the returns for these frequencies. This can be achieved most easily with the lapply()
function. The resulting list object is then converted to a matrix and NA values
are omitted. The package ghd does not provide a function for parameterizing the
HYP in the (𝜉,𝜒) space. Hence, in the subsequent lines the function xichi() is
specified for this purpose. Then the unknown parameters of the HYP distribution
are estimated by means of the function fit.hypuv() for each of the columns in
SUITABLE DISTRIBUTIONS FOR RETURNS 81
R code 6.3 Shape triangle for HYP distribution.
r d <− c (1 , 5, 10, 20, 40) 1
yrets <− na . omit ( matrix ( u nli st ( lapply ( rd , 2
function (x) diff (log (y) , lag = x) ) ) , 3
ncol = 5) ) 4
## Function for xi / chi coefficients 5
xichi <− function (x){ 6
param <− coef (x, type = "alpha . delta " ) 7
rho <− param [ [ " beta " ] ] / param [ [ " alpha " ] ] 8
zeta <− param [ [ " delta " ] ] ∗ sq rt ( param [ [ " alpha " ]]^2 − 9
param [ [ " beta " ] ]^2 ) 10
x i <− 1 / sqrt (1 + zeta ) 11
chi <− x i ∗ rho 12
result <− c ( chi , xi ) 13
names ( r e s ult ) <− c("chi" , "xi" ) 14
return ( result ) 15
} 16
## HYP F i t t i n g 17
hypfits <− a p pl y ( y r e t s , 2 , f i t . hypuv , s ymm et ri c = FALSE ) 18
points <− matrix ( unlist ( lapply ( hypfits , xichi ) ) , 19
n c ol = 2 , byrow = TRUE ) 20
## Shape tri angle 21
col . def <− c ( " black " , " blue " , " red " , " green " , "orange" ) 22
leg . def <− paste ( rd , rep ( "day retu rn " , 5) ) 23
plot ( points , ylim = c ( −0.2 , 1.2) , xlim = c ( −1.2, 1.2) , 24
col = col . def , pch = 16 , ylab = expression ( xi ) , 25
xlab = expression ( chi ) ) 26
lines (x = c(0 , −1) , y = c (0 , 1) ) 27
lines (x = c (0 , 1) , y = c (0 , 1) ) 28
lines (x = c( −1, 1) , y = c (1 , 1) ) 29
legend ( " bottomright " , legend = leg . def , col = col . def , pch = 16) 30
text (x = 0.0 , y = 1.05 , label = "Laplace " , srt = 0) 31
text (x = −1.0, y = 1.05 , label = " Exponential " , s rt = 0) 32
text (x = 1.0 , y = 1.05 , label = "Exponential " , srt = 0) 33
text (x = 0.0 , y = −0.1 , label = "Normal" , s rt = 0) 34
text (x = −0.6, y = 0.5 , label = " Hyperbolic , l e ft skewed" , 35
s rt = 302) 36
text (x = 0.6 , y = 0.5 , label = " Hyperbolic , right skewed" , 37
s rt = 57) 38
yrets by employing the function apply(). The returned list object hypfits,
which contains the fitted distributions, is then submitted to lapply() in order to
extract the (̂
𝜉, ̂𝜒) pairs. These points are plotted in the final lines of the listing and the
resulting shape triangle is provided in Figure 6.8.
A clear pattern can be detected from this shape triangle: the lower the frequency of
the return, the more it approaches the south of the triangle, hence the HYP distribution
could in principle be approximated by a normal distribution for these lower-frequency

![alt text](image-8.png)

returns. Overall, however, the point cloud remains fairly close to the center of the
triangle, so this approximation may not work well. Furthermore, a comparison of the
(̂
𝜉, ̂𝜒) pairs indicates that the bimonthly returns show the greatest negative skewness
in absolute terms. Surprisingly, even the 

 Applications of the GLD to risk modelling
and data analysis
6.7.1 VaR for a single stock
In the first application of the GLD a back-test is conducted for the 99% VaR of the
weekly losses of the QCOM stock contained in the S&P 500 Index. The data is provided in the R package FRAPO. The sample covers the period from 2003 to 2008 and
comprises 265 observations. The back-test is expressed in terms of the unconditional
VaR implied by the GLD and the normal distribution. The R code for conducting the
back-test is exhibited in Listing 6.4.
First, the necessary packages are loaded into memory. The fitting of the loss series
to the GLD is accomplished with the functions of the package lmomco and, as stated
above, the data set is contained in the package FRAPO. The data.frame object
SUITABLE DISTRIBUTIONS FOR RETURNS 83
R code 6.4 VaR of QCOM stock: comparison of GLD and normal distribution.
## Loading of packages 1
l i b r a r y (lmomco ) 2
l i b r a r y (FRAPO ) 3
## Data loading 4
data ( SP500 ) 5
Idx <− SP500 [ , "QCOM" ] 6
L <− −1 ∗ r e t u r n s e r i e s ( Idx , method = " d i s c r e t e " , t r i m = TRUE ) 7
## Computing VaR ( Normal & GLD ) 99%, moving window 8
ep <− 104: length (L) 9
s p <− 1: length ( ep ) 10
level <− 0.99 11
VaR <− m a t r i x (NA, n c ol = 2 , nrow = l e n g t h ( ep ) ) 12
for ( i in 1: length ( sp ) ) { 13
x <− L[ sp [ i ]: ep [ i ] ] 14
lmom <− lmom . ub ( x ) 15
fit <− p a r gl d (lmom ) 16
VaRGld <− quagld ( level , fit ) 17
VaRNor <− qnorm ( le vel , mean ( x ) , sd ( x ) ) 18
VaR [ i , ] <− c ( VaRGld , VaRNor ) 19
p r i n t ( p a st e ( " R e s ult f o r " , ep [ i ] , " : " , VaRGld , " and " , VaRNor ) ) 20
} 21
## Summarising results 22
Res <− c bi n d ( L [ 1 0 5 : l e n g t h ( L ) ] , VaR[−nrow ( VaR ) , ] ) 23
colnames (Res ) <− c ( " Loss " , "VaRGld " , "VaRNor" ) 24
## Plot of backtest results 25
pl ot ( Res [ , " Loss " ] , type = "p" , xlab = "Time Index " , 26
ylab = " Losses in percent " , pch = 19 , cex = 0.5 , 27
ylim = c( −15 , max ( Res ) ) ) 28
abline (h = 0, col = "grey" ) 29
l i n e s ( Res [ , "VaRGld" ] , c ol = " blue " , lwd = 2 ) 30
l i n e s ( Res [ , "VaRNor" ] , c ol = " re d " , lwd = 2 ) 31
l e g e n d ( " b o t t o m r i g h t " , l e g e n d = c ( " L o s s e s " , "VaR GLD" , 32
"VaR Normal " ) , 33
col = c(" black " , " blue " , " red" ) , 34
l t y = c (NA, 1 , 1 ) , pch = c ( 1 9 , NA, NA) , bt y = " n " ) 35
SP500 is loaded next and the weekly percentage losses of QCOM are stored in the
object L. Then, the shape of the back-test is defined. A moving window approach with
a window size of 104 observations, equivalent to a time span of two years, has been
chosen. The objects ep and sp define the relevant end and start points, respectively.
The 99% confident level is assigned to the object level. At line 12 a matrix
object is initialized with row dimension equal to the number of back-testing periods
and two columns in which the VaR of the GLD and the normal distributions will be
written. One might argue that a for loop is not R-like, but to correct a common
prejudice, as long as the proper memory slot of the object VaR is allotted before the

![alt text](image-9.png)


loop is executed, one is not penalized by a worse execution time. Within the loop,
the relevant data window is extracted and fitted to the GLD, and the VaR measures
are calculated for the two distributions and stored in the ith row of VaR. The last line
in the loop informs the user about the progress of the loop execution by printing the
time index and the values of the VaRs. The results are then aggregated into the object
Res, which has the losses as the first column and the VaR measures lagged by one
week in the next two columns. The trajectory of the two unconditional VaR measures
is then plotted together with losses as points in the ensuing block of plot statements.
The plot is shown in Figure 6.9. The VaR trajectory according to the GLD model
is more volatile than for the normal distribution. Notice the sharp drop of the GLD
VaR toward the end of the back-test period, which goes hand in hand with a lower
loss volatility, but also reflects the sensitivity of moment estimates with respect to
outliers. During this episode, the VaR measures according to the normal distribution
are too conservative. Both models violate the actual losses only once and hence the
size of the risk measure at the 99% confidence level is not violated—that is, given
160 back-test observations one would expect at most two violations.
6.7.2 Shape triangle for FTSE 100 constituents
In the second example, the characteristics of FTSE 100 stocks are analyzed by means
of a shape triangle for the standardized GLD as in (6.23)–(6.27). This kind of shape
triangle was proposed in Chalabi et al. (2010) and applied to the constituent stocks of
the NASDAQ 100. The shape triangle is depicted in the 𝛿 = 𝜆4 − 𝜆3 and 𝛽 = 𝜆3 + 𝜆4
plane. The R code is shown in Listing 6.5.
The robust estimation of the GLD parameters is covered in the package fBasics and
the weekly price data of the FTSE 100 constituents is part of the package FRAPO,
SUITABLE DISTRIBUTIONS FOR RETURNS 85
R code 6.5 FTSE 100 stocks: shape triangle of standardized GLD.
l i b r a r y (FRAPO ) 1
library ( fBasics ) 2
## Loading of data 3
d a t a ( INDTRACK3 ) 4
P <− INDTRACK3 [ , −1] 5
R <− r e t u r n s e r i e s ( P , method = " d i s c r e t " , t r i m = TRUE ) 6
## Fitti n g and calc ul ati ng beta and lambda 7
Fit <− a p pl y (R , 2 , g l d F i t , method = " r o b " , d o p l o t = FALSE , 8
t r a c e = FALSE ) 9
DeltaBetaParam <− matrix ( unlist ( lapply ( Fit , function (x) { 10
l <− x@fit$estimate [c (3 , 4) ] 11
res <− c(l [2] − l [1] , l [1] + l [2]) 12
res } ) ) , n c ol = 2 , byrow = TRUE ) 13
## Shape tri angle 14
plot ( DeltaBetaParam , xlim = c( −2, 2) , ylim = c( −2, 0) , 15
xl a b = e x p r e s si o n ( d e l t a == lambda [ 4 ] − lambda [3 ] ) , 16
yl a b = e x p r e s si o n ( b et a == lambda [ 3 ] + lambda [ 4 ] ) , 17
pch = 19 , cex = 0.5) 18
segments ( x0 = −2, y0 = −2, x1 = 0 , y1 = 0 , 19
col = " grey " , lwd = 0.8 , lt y = 2) 20
segments ( x0 = 2 , y0 = −2, x1 = 0 , y1 = 0 , 21
col = " grey " , lwd = 0.8 , lt y = 2) 22
segments ( x0 = 0 , y0 = −2, x1 = 0 , y1 = 0 , col = " blue " , 23
lwd = 0.8 , lt y = 2) 24
segments ( x0 = −0.5 , y0 = −0.5 , x1 = 0.5 , y1 = −0.5, 25
col = " red " , lwd = 0.8 , lt y = 2) 26
segments ( x0 = −1.0 , y0 = −1.0 , x1 = 1.0 , y1 = −1.0, 27
col = " red " , lwd = 0.8 , lt y = 2) 28
hence these two packages are loaded into the workspace first. Next, the data object
INDTRACK3 is loaded and its first column—representing the FTSE 100 index—is
omitted from further analysis. The percentage returns of the stocks are assigned to the
object R, which is then used to fit each of its columns to the GLD with the function
gldFit(). This task is swiftly accomplished by utilizing the apply() function.
The object Fit is a list with the returned objects of gldFit. In lines 10–13 a small
function is defined that returns the (𝛿, 𝛽) parameter pairs, which are then plotted in
the shape triangle. The output is shown in Figure 6.10.
The x-axis represents the difference between the right- and left-tail shape parameters, and the y-axis their sum. There are a total of six regions discernible in this
triangle. The light gray dashed line discriminates between stocks that are characterized by either a left-skewed or a right-skewed distribution. Points on that line refer
to a symmetric distribution. As can easily be seen, the majority of stock returns are
characterized by being skewed to the left, thus confirming a stylized fact of financial
returns. Points in the top part of the triangle represent return distributions with finite
variance and kurtosis, and points in the middle region, between the −0.5 and −1.0
![alt text](image-10.png)
dark gray dashed lines, refer to return distributions with infinite kurtosis but finite
variance. The (𝛿, 𝛽) pairs below the −1 line represent return processes where these
moments are infinite, which is the case for one of the FTSE 100 constituents stocks.