Springer Finance


Editorial Board
M. Avellaneda
G. Barone-Adesi
M. Broadie
M.H.A. Davis
E. Derman
C. Kliippelberg
E. Kopp
W. Schachermayer


Springer Finance


Springer Finance is a programme of books aimed at students, academics, and

practitioners working on increasingly technical approaches to the analysis of

financial markets. It to cover a variety of topics, not only mathematical
aims

finance but foreign exchanges, term structure, risk m gement, portfolio

theory, equity derivatives, and financial economics.



A nn, Credit Risk Valuation: Methods, Models, and Applications (2001)
M mma



Barucci. Financial Markets Theory: Equilibrium, Efficiency and Information (2003)
E.

Bingham R. Kiesel. Risk-Neutral Valuation: Pricing and Hedging of Financial
N.H and



Derivatives, 2nd Edition (2004)



T.R. Bielecki and Rutkowski. Credit Risk: Modeling, Valuation and Hedging (2001)
M



T.R. Bielecki and Rutkowski.

Brigo amd Mercurio, Interest Rate Models: Theory and Pracbce (200
D. F. I)



R. Buff, Uncertain Volatility Models- Theory and Application (2002)



R.-A. Dana and Jeanblanc, Financial Markets in Continuous Time (2003)
M



Deboeck and Kohonen (Editors), Visual Explorations in Finance with Self­
G. T.



Organizing Maps (1998)



R.J. Elliott and P.E. Kopp. Mathematics of Financial Markets (19)

Gemon, Madan, S.R. Pliska Vorst (Editors), Mathematical Finance­
H. D. and T.

Bachelier Congress 20 (2001)



Gundlach Lehrba (Editors), CreditRlsk+ in the Banking Industry (2004)
M. and F.



Kwok, Mathematical Models of Financial Derivatives (1998)
Y.-K.



Kii/pmonn, Itional Exuberance Reconsidered: The Cross Section of Stock Returns,
M.



2nd Edition (2004)



A. Pelsser. Efficient Methods for Valuing Interest Rate Derivatives (20)


J.-L Prigent, Weak Convergence of Financial Markets (2003)

B. Schmid. Credit Risk Pricing Models: Theory and Practice, 2nd Edition (2004)



S.E. Shreve, Stochastic Calculus for Finance The Binomial Asset Pricing Model (2004)
1:



S.E. Shreve, Stochastic Calculus for Finance II: Continuous-Time Models (2004)



Yor, Exponential Funcbonals of Brownian Motion and Related Processes (2001)
M.



R. gst,lnterest-Rate Management (2002)
Za



Zhu and Chern, Derivative Securities and Difference Methods (2004)
Y.-1. 1-L



A. Ziegler, Incomplete lnfonnabon and Heterogeneous Beliefs in Continuous-Time



Finance (2003)

A. Ziegler, A Game Theory Analysis of Options: Corporate Finance and Financial

Intermediation in Conbnuous Time, 2nd Edition (2004)


Steven E. Shreve

###### Stochastic Calcu I us for Finance II

Continuous-Time Models


With 28 Figures

###### �Springer


Steven Shreve
E.

Department of Mathematical Sciences



Carnegie Mellon University



Pittsburgh, PA
15213



USA



shreve@cmu.edu



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-3-0.png)







Mathematics Subject Classification (20 ): 60-01, 60HIO, 60165, 91B28


Library of Congress Cataloging-in-Publication Data



Shreve, Steven E.



Stochastic calculus for finance Steven E. Shreve.
I



p. em. - (Springer finance series)



Includes bibliographical references and index.



Contents v. 2. Continuous-time models.



ISBN 0-387-40101-6 paper)
(alk.



I. Finance-Mathematical models-Textbooks. 2. Stochastic analysis­



Textbooks. I. Title. II. Spnnger finance.

HGI06.S57 2003

332'.01'51922-{lc22 2003063342


ISBN 0-387-40101-6 P ted on acid-free paper.


2004 Spnnger Science+ Business Media, Inc.
©

All nghts reserved This work may not be translated or copied in whole or in part without

the wntten permission of the publisher (Springer Science+Business Media, Inc, 233

Spring Street, New York, NY 10013, USA), except for bnef excerpts in connection with

revtews or scholarly analysis. Use in connection with any form of information storage and

retrieval, electronic adaptation, computer software, or by similar or dissimilar

methodology now known or hereafter developed is forbidden

The use in this publication of trade names, trademarks, service marks and similar terms,

even if they are not identified as such, is not to be taken as an expression of opinion as to

whether or not they are subject to propnetary nghts.


Printed in the United States of America.


9 8 7 6 5 4 3 2


springeronline com


To my students


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-5-0.png)
Preface


Origin of This Text


This text has evolved from mathematics courses in the Master of Science in
Computational Finance (MSCF) program at Carnegie Mellon University. The
content of this book has been used successfully with students whose math­
ematics background consists of calculus and calculus-based probability. The
text gives precise statements of results, plausibility arguments, and even some
proofs, but more importantly, intuitive explanations developed and refined
through cla room experience with this material are provided. Exercises con­
clude every chapter. Some of these extend the theory and others are drawn
from practical problems in quantitative finance.
The first three chapters of Volume I have been used in a half-semester
course in the MSCF program. The full Volume I has been used in a full­
semester course in the Carnegie Mellon Bachelor's program in Computational
Finance. Volume II was developed to support three half-semester courses in
the MSCF program.


Dedication


Since its inception in 1994, the Carnegie Mellon Master's program in Compu­
tational Finance has graduated hundreds of students. These people, who have
come from a variety of educational and professional backgrounds, have been
a joy to teach. They have been eager to learn, asking questions that stimu­
lated thinking, working hard to understand the material both theoretically
and practically, and often requesting the inclusion of additional topics. Many
came from the finance industry, and were gracious in sharing their knowledge
in ways that enhanced the cla room experience for all.
This text and my own store of knowledge have benefited greatly from
interactions with the MSCF students, and I continue to learn from the MSCF


VIII Preface

alumni. I take this opportunity to express gratitude to these students and
former students by dedicating this work to them.


Acknowledgments


Conversations with several people, including my colleagues David Heath and
Dmitry Kramkov, have influenced this text. Lukasz Kruk read much of the
manuscript and provided numerous comments and corrections. Other students
and faculty have pointed out errors in and suggested improvements of earlier
drafts of this work. Some of these are Jonathan Anderson, Nathaniel Carter,
Bogdan Doytchinov, David German, Steven Gillispie, Karel Janecek, Sean
Jones, Anatoli Karolik, David Korpi, Andrzej Krause, Rael Limbitco, Petr
Luksan, Sergey Myagchilov, Nicki Rasmussen, Isaac Sonin, Ma imo Ta an­
Solet, David Whitaker and Uwe Wystup. In some cases, users of these earlier
drafts have suggested exercises or examples, and their contributions are ac­
knowledged at appropriate points in the text. To all those who aided in the
development of this text, I am most grateful.
During the creation of this text, the author was partially supported by the
National Science Foundation under grants DMS-9802464, DMS-0103814, and
DMS-0139911. Any opinions, findings, and conclusions or recommendations
expressed in this material are those of the author and do not necessarily reflect
the views of the National Science Foundation.


Pittsburgh, Pennsylvania, USA Steven E. Shreve
April 2004


Contents


1 General Probability Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1 Infinite Probability Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Random Variables and Distributions . . . . . . . . . . . . . . . . . . . . . . . 7

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Expectations . 13
1.4 Convergence of Integrals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
1.5 Computation of Expectations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
1.6 Change of Measure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
1. 7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
1.8 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
1. 9 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

2 Information and Conditioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
2.1 Information and u-algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
2.2 Independence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
2.3 General Conditional Expectations . . . . . . . . . . . . . . . . . . . . . . . . . 66
2.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
2.5 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6 Exercises 77

3 Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.1 Introduction . . . . . . : . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.2 Scaled Random Walks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.2.1 Symmetric Random Walk . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.2.2 Increments of the Symmetric Random Walk . . . . . . . . . . 84
3.2.3 Martingale Property for the Symmetric
Random Walk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.2.4 Quadratic Variation of the Symmetric
Random Walk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.2.5 Scaled Symmetric Random Walk . . . . . . . . . . . . . . . . . . . . 86
3.2.6 Limiting Distribution of the Scaled Random Walk . . . . . 88


X Contents

3.2.7 Log-Normal Distribution as the Limit of the
Binomial Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
3.3 Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
3.3.1 Definition of Brownian Motion . . . . . . . . . . . . . . . . . . . . . . 93
3.3.2 Distribution of Brownian Motion . . . . . . . . . . . . . . . . . . . . 95
3.3.3 Filtration for Brownian Motion . . . . . . . . . . . . . . . . . . . . . 97
3.3.4 Martingale Property for Brownian Motion . . . . . . . . . . . . 98
3.4 Quadratic Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.4.1 First-Order Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.4.2 Quadratic Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.4.3 Volatility of Geometric Brownian Motion . . . . . . . . . . . . . 106
3.5 Markov Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
3.6 First Pa age Time Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.7 Reflection Principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.7.1 Reflection Equality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.7.2 First Pa age Time Distribution . . . . . . . . . . . . . . . . . . . . . 112
3.7.3 Distribution of Brownian Motion and Its Maximum . . . . 113
3.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.9 Notes 116
3.10 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

Stochastic Calculus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
4
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
4.2 Ito's Integral for Simple Integrands . . . . . . . . . . . . . . . . . . . . . . . . 125
4.2.1 Construction of the Integral . . . . . . . . . . . . . . . . . . . . . . . . 126
4.2.2 Properties of the Integral . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
4.3 Ito's Integral for General Integrands . . . . . . . . . . . . . . . . . . . . . . . 132
4.4 ltO-Doeblin Formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
4.4.1 Formula for Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . 137
4.4.2 Formula for Ito Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
4.4.3 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
4.5 Black-Scholes-Merton Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
4.5.1 Evolution of Portfolio Value . . . . . . . . . . . . . . . . . . . . . . . . 154
4.5.2 Evolution of Option Value . . . . . . . . . . . . . . . . . . . . . . . . . . 155
4.5.3 Equating the Evolutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
4.5.4 Solution to the Black-Scholes-Merton Equation . . . . . . . . 158
4.5.5 The Greeks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
4.5.6 Put-Call Parity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
4.6 Multivariable Stochastic Calculus . . . . . . . . . . . . . . . . . . . . . . . . . . 164
4.6.1 Multiple Brownian Motions . . . . . . . . . . . . . . . . . . . . . . . . . 164
4.6.2 ItO-Doeblin Formula for Multiple Processes . . . . . . . . . . . 165
4.6.3 Recognizing a Brownian Motion . . . . . . . . . . . . . . . . . . . . . 168
4. 7 Brownian Bridge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
4. 7.1 Gaussian Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
4. 7.2 Brownian Bridge as a Gaussian Process . . . . . . . . . . . . . . 175


Contents XI


. . . . . . .
4. 7.3 Brownian Bridge as a Scaled Stochastic Integral 176
4.7.4 Multidimensional Distribution of the
Brownian Bridge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
4.7.5 Brownian Bridge as a Conditioned Brownian Motion . . . 182
4.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9 Notes 187
4.10 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189

Risk-Neutral Pricing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
5
5.1 Introduction . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
5.2 Risk-Neutral Measure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
5.2.1 Girsanov's Theorem for a Single Brownian Motion . . . . . 210
5.2.2 Stock Under the Risk-Neutral Measure . . . . . . . . . . . . . . . 214
5.2.3 Value of Portfolio Process Under the
Risk-Neutral Measure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
5.2.4 Pricing Under the Risk-Neutral Measure . . . . . . . . . . . . . 218
5.2.5 Deriving the Black-Scholes-Merton Formula . . . . . . . . . . . 218

. . . . . . . . . . . . . . . . . . . . . . .
5.3 Martingale Representation Theorem 221
5.3.1 Martingale Representation with One
Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
5.3.2 Hedging with One Stock . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
5.4 Fundamental Theorems of Asset Pricing . . . . . . . . . . . . . . . . . . . . 224
5.4.1 Girsanov and Martingale Representation Theorems . . . . 224
5.4.2 Multidimensional Market Model . . . . . . . . . . . . . . . . . . . . . 226
5.4.3 Existence of the Risk-Neutral Measure . . . . . . . . . . . . . . . 228
5.4.4 Uniqueness of the Risk-Neutral Measure . . . . . . . . . . . . . . 231
5.5 Dividend-Paying Stocks . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . 234
5.5.1 Continuously Paying Dividend . . . . . . . . . . . . . . . . . . . . . . 235
5.5.2 Continuously Paying Dividend with
Constant Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
5.5.3 Lump Payments of Dividends . . . . . . . . . . . . . . . . . . . . . . . 238
5.5.4 Lump Payments of Dividends with
Constant Coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
5.6 Forwards and Futures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
5.6.1 Forward Contracts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
5.6.2 Futures Contracts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
5.6.3 Forward-Futures Spread . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
5.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
5.8 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
5.9 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251

6 Connections with Partial Differential Equations . . . . . . . . . . . 263
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
6.2 Stochastic Differential Equations . . . . . . . . . . . . . . . . . . . . . . . . . . 263
6.3 The Markov Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266


XII Contents


. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4 Partial Differential Equations 268

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5 Interest Rate Models 272

. . . . . . . . . . . . . . . . . .
6.6 Multidimensional Feynman-Kac Theorems 277

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6. 7 Summary 280

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.8 Notes 281

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.9 Exercises 282

7 Exotic Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1 Introduction 295

. . . . . . . . . . . . . . . . . .
295

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Knock-out Barrier Options 299

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3.1 Up-and-Out Call 300

. . . . . . . . . . . . . . . . . . . . .
7.3.2 Black-Scholes-Merton Equation 300

. . . . .
7.3.3 Computation of the Price of the Up-and-Out Call 304

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4 Lookback Options 308

. . . . . . . . . . . . . . . . . . . .
7.4.1 Floating Strike Lookback Option 308

. . . . . . . . . . . . . . . . . . . . .
7.4.2 Black-Scholes-Merton Equation 309
7.4.3 Reduction of Dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312

. . . . .
7.4.4 Computation of the Price of the Lookback Option 314

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5 Asian Options 320

. . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5.1 Fixed-Strike Asian Call 320

. . . . . . . . . . . . . . . . . . . . . . . . . .
7.5.2 Augmentation of the State 321

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5.3 Change of Numeraire 323

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6 Summary 331

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.7 Notes . 331

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8 Exercises 332

8 American Derivative Securities . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.1 Introduction . 339

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2 Stopping Times 340

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.3 Perpetual American Put 345

. . . . . . . . . . . . . . . . . . . . .
8.3.1 Price Under Arbitrary Exercise 346

. . . . . . . . . . . . . . . . . . . . . . .
8.3.2 Price Under Optimal Exercise 349

. . . . . . . . . .
8.3.3 Analytical Characterization of the Put Price 351

. . . . . . . .
8.3.4 Probabilistic Characterization of the Put Price 353

. . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4 Finite-Expiration American Put 356

. . . . . . . . . .
8.4.1 Analytical Characterization of the Put Price 357

. . . . . . . .
8.4.2 Probabilistic Characterization of the Put Price 359

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.5 American Call 361

. . . . . . . . . . . . . . . . .
8.5.1 Underlying Asset Pays No Dividends 361

. . . . . . . . . . . . . . . . . . . .
8.5.2 Underlying Asset Pays Dividends 363

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.6 Summary . . 368
8.7 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.8 Exercises . 370

7.2 Maximum of Brownian Motion with Drift


Contents XIII

9 Change of N umeraire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.1 Introduction . . 375

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.2 Numeraire 376

. . . . . . . . . . . . . . .
9.3 Foreign and Domestic Risk-Neutral Measures 381

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3.1 The Basic Processes 381

. . . . . . . . . . . . . . . . . . . . .
9.3.2 Domestic Risk-Neutral Measure 383

. . . . . . . . . . . . . . . . . . . . . . .
9.3.3 Foreign Risk-Neutral Measure 385

. . . . . . . . . . . . . . . . . . . . .
9.3.4 Siegel's Exchange Rate Paradox 387

. . . . . . . . . . . . . . . . . . . . . . . . . . .
9.3.5 Forward Exchange Rates 388

. . . . . . . . . . . . . . . . . . . . . . . .
9.3.6 Garman-Kohlhagen Formula 390

. . . . . . . . . . . . . . . . . . . .
9.3.7 Exchange Rate Put-Call Duality 390

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4 Forward Measures 392

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.4.1 Forward Price 392

. . . . . . . . . . . . . . . . . . . .
9.4.2 Zero-Coupon Bond as Numeraire 392

. . . . . . . . .
9.4.3 Option Pricing with a Random Interest Rate 394

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.5 Summary 397

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.6 Notes 398

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9. 7 Exercises 398

10 Term-Structure �odels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.1 Introduction 403

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10.2 Affine-Yield Models 405

. . . . . . . . . . . . . . . . . . . . . . . . .
10.2.1 Two-Factor Vasicek Model . 406
10.2.2 Two-Factor CIR Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420
10.2.3 Mixed Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
10.3 Heath-Jarrow-Morton Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
10.3.1 Forward Rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
10.3.2 Dynamics of Forward Rates and Bond Prices . . . . . . . . . 425
10.3.3 No-Arbitrage Condition . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
10.3.4 HJM Under Risk-Neutral Measure . . . . . . . . . . . . . . . . . . . 429
10.3.5 Relation to Affine-Yield Models . . . . . . . . . . . . . . . . . . . . . 430
10.3.6 Implementation of HJM . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432
10.4 Forward LIBOR Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
10.4.1 The Problem with Forward Rates . . . . . . . . . . . . . . . . . . . 435
10.4.2 LIBOR and Forward LIBOR . . . . . . . . . . . . . . . . . . . . . . . . 436
10.4.3 Pricing a Backset LIBOR Contract . . . . . . . . . . . . . . . . . . 437
10.4.4 Black Caplet Formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438
10.4.5 Forward LIBOR and Zero-Coupon Bond Volatilities . . . 440
10.4.6 A Forward LIBOR Term-Structure Model . . . . . . . . . . . . 442
10.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44 7
10.6 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 450
10.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451


XIV Contents


11 Introduction to Jump Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . 461
11.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461
11.2 Poisson Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 462
11.2.1 Exponential Random Variables . . . . . . . . . . . . . . . . . . . . . . 462
11.2.2 Construction of a Poisson Proce . . . . . . . . . . . . . . . . . . . 463
11.2.3 Distribution of Poisson Process Increments . . . . . . . . . . . 463
11.2.4 Mean and Variance of Poisson Increments . . . . . . . . . . . . 466
11.2.5 Martingale Property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
11.3 Compound Poisson Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
11.3.1 Construction of a Compound Poisson Process . . . . . . . . . 468
11.3.2 Moment-Generating Function . . . . . . . . . . . . . . . . . . . . . . . 470
11.4 Jump Processes and Their Integrals . . . . . . . . . . . . . . . . . . . . . . . . 473
11.4.1 Jump Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
11.4.2 Quadratic Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479
11.5 Stochastic Calculus for Jump Processes . . . . . . . . . . . . . . . . . . . . 483
11.5.1 ItO-Doeblin Formula for One Jump Process . . . . . . . . . . . 483
11.5.2 ItO-Doeblin Formula for Multiple Jump Processes . . . . . 489
11.6 Change of Measure . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492
11.6.1 Change of Measure for a Poisson Process . . . . . . . . . . . . . 493
11.6.2 Change of Measure for a Compound Poisson Process . . . 495
11.6.3 Change of Measure for a Compound Poisson Process
and a Brownian Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
11.7 Pricing a European Call in a Jump Model . . . . . . . . . . . . . . . . . . 505
11.7.1 Asset Driven by a Poisson Process . . . . . . . . . . . . . . . . . . . 505
11.7.2 Asset Driven by a Brownian Motion and a Compound
Poisson Process . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
11.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 523
11.9 Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525
11.10Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525

A Advanced Topics in Probability Theory . . . . . . . . . . . . . . . . . . . . 527
A.1 Countable Additivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 527
A.2 Generating u-algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 530
A.3 Random Variable with Neither Density nor Probability Ma
Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531

B Existence of Conditional Expectations . . . . . . . . . . . . . . . . . . . . . 533


C Completion of the Proof of the Second Fundamental
Theorem of Asset Pricing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 535

References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 537

Index [.] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 545


Introduction


Background


By awarding Harry Markowitz, William Sharpe, and Merton Miller the 1990
Nobel Prize in Economics, the Nobel Prize Committee brought to worldwide
attention the fact that the previous forty years had seen the emergence of
a new scientific discipline, the "theory of finance." This theory attempts to
understand how financial markets work, how to make them more efficient, and
how they should be regulated. It explains and enhances the important role
these markets play in capital allocation and risk reduction to facilitate eco­
nomic activity. Without losing its application to practical aspects of trading
and regulation, the theory of finance has become increasingly mathematical,
to the point that problems in finance are now driving research in mathematics.
Harry Markowitz's 1952 Ph.D. thesis Portfolio Selection laid the ground­
work for the mathematical theory of finance. Markowitz developed a notion
of mean return and covariances for common stocks that allowed him to quan­
tify the concept of "diversification" in a market. He showed how to compute
the mean return and variance for a given portfolio and argued that investors
should hold only those portfolios whose variance is minimal among all portfo­
lios with a given mean return. Although the language of finance now involves
stochastic (Ito) calculus, management of risk in a quantifiable manner is the
underlying theme of the modern theory and practice of quantitative finance.
1969, Robert Merton introduced stochastic calculus into the study of
In
finance. Merton was motivated by the desire to understand how prices are
set in financial markets, which is the cla ical economics question of "equi­
librium," and in later papers he used the machinery of stochastic calculus to
begin investigation of this issue.
At the same time as Merton's work and with Merton's a istance, Fis­
cher Black and Myron Scholes were developing their celebrated option pricing
formula. This work won the 1997 Nobel Prize in Economics. It provided a
price for a European call option (i.e., the right to buy one share of a given
satisfying solution to an important practical problem, that of finding a fair


XVI Introduction


stock at a specified price and time). In the period 1979-1983, Harrison, Kreps,
and Pliska used the general theory of continuous-time stochastic processes to
put the Black-Scholes option-pricing formula on a solid theoretical basis, and,
as a result, showed how to price numerous other "derivative" securities.
Many of the theoretical developments in finance have found immediate
application in financial markets. To understand how they are applied, we
digress for a moment on the role of financial institutions. A principal function
of a nation's financial institutions is to act as a risk-reducing intermediary
among customers engaged in production. For example, the insurance industry
pools premiums of many customers and must pay off only the few who actually
incur losses. But risk arises in situations for which pooled-premium insurance
is unavailable. For instance, as a hedge against higher fuel costs, an airline
may want to buy a security whose value will rise if oil prices rise. But who
wants to sell such a security? The role of a financial institution is to design
such a security, determine a "fair" price for it, and sell it to airlines. The
security thus sold is usually "derivative" (i.e., its value is based on the value
of other, identified securities). "Fair" in this context means that the financial
institution earns just enough from selling the security to enable it to trade
in other securities whose relation with oil prices is such that, if oil prices do
indeed rise, the firm can pay off its increased obligation to the airlines. An
"efficient" market is one in which risk-hedging securities are widely available
at "fair" prices.
The Black-Scholes option pricing formula provided, for the first time, a
theoretical method of fairly pricing a risk-hedging security. If an investment
bank offers a derivative security at a price that is higher than "fair," it may be
underbid. If it offers the security at less than the "fair" price, it runs the risk of
substantial loss. This makes the bank reluctant to offer many of the derivative
securities that would contribute to market efficiency. In particular, the bank
only wants to offer derivative securities whose "fair" price can be determined
in advance. Furthermore, if the bank sells such a security, it must then address
the hedging problem: how should it manage the risk a ociated with its new
position? The mathematical theory growing out of the Black-Scholes option
pricing formula provides solutions for both the pricing and hedging problems.
It thus has enabled the creation of a host of specialized derivative securities.
This theory is the subject of this text.


Relationship between Volumes I and II


Volume II treats the continuous-time theory of stochastic calculus within the
context of finance applications. The presentation of this theory is the raison
d'etre of this work. Volume II includes a self-contained treatment of the prob­
ability theory needed for stochastic calculus, including Brownian motion and
its properties.


Introduction XVII


Volume I presents many of the same finance applications, but within the
simpler context of the discrete-time binomial model. It prepares the reader
for Volume II by treating several fundamental concepts, including martin­
gales, Markov processes, change of measure and risk-neutral pricing in this
less technical setting. However, Volume II has a self-contained treatment of
these topics, and strictly speaking, it is not necessary to read Volume I before
reading Volume II. It is helpful in that the difficult concepts of Volume II are
first seen in a simpler context in Volume I.
In the Carnegie Mellon Master's program in Computational Finance, the
course based on Volume I is a prerequisite for the courses based on Volume
II. However, graduate students in computer science, finance, mathematics,
physics and statistics frequently take the courses based on Volume II without
first taking the course based on Volume I.
The reader who begins with Volume II may use Volume I as a reference. As
several concepts are presented in Volume II, reference is made to the analogous
concepts in Volume I. The reader can at that point choose to read only Volume
II or to refer to Volume I for a discussion of the concept at hand in a more
transparent setting.


Summary of Volume I


Volume I presents the binomial a et pricing model. Although this model is
interesting in its own right, and is often the paradigm of practice, here it is
used primarily as a vehicle for introducing in a simple setting the concepts
needed for the continuous-time theory of Volume II.
Chapter 1, The Binomial No-Arbitrage Pricing Model, presents the no­
arbitrage method of option pricing in a binomial model. The mathematics is
simple, but the profound concept of risk-neutral pricing introduced here is
not. Chapter 2, Probability Theory on Coin Toss Space, formalizes the results
of Chapter 1, using the notions of martingales and Markov processes. This
chapter culminates with the risk-neutral pricing formula for European deriva­
tive securities. The tools used to derive this formula are not really required for
the derivation in the binomial model, but we need these concepts in Volume II
and therefore develop them in the simpler discrete-time setting of Volume I.
Chapter 3, State Prices, discusses the change of measure a ociated with risk­
neutral pricing of European derivative securities, again as a warm-up exercise
for change of measure in continuous-time models. An interesting application
developed here is to solve the problem of optimal (in the sense of expected
utility maximization) investment in a binomial model. The ideas of Chapters
1 to 3 are essential to understanding the methodology of modern quantitative
finance. They are developed again in Chapters 4 and 5 of Volume II.
The remaining three chapters of Volume I treat more specialized con­
cepts. Chapter 4, American Derivative Securities, considers derivative secu­
rities whose owner can choose the exercise time. This topic is revisited in


XVIII Introduction


a continuous-time context in Chapter 8 of Volume II. Chapter 5, Random

Walk, explains the reflection principle for random walk. The analogous reflec­
tion principle for Brownian motion plays a prominent role in the derivation of
pricing formulas for exotic options in Chapter 7 of Volume II. Finally, Chap­
ter 6, Interest-Rate-Dependent Assets, considers models with random interest
rates, examining the difference between forward and futures prices and intro­
ducing the concept of a forward measure. Forward and futures prices reappear
at the end of Chapter 5 of Volume II. Forward measures for continuous-time
models are developed in Chapter 9 of Volume II and used to create forward
LIBOR models for interest rate movements in Chapter 10 of Volume II.


Summary of Volume II



Chapter 1, General Probability Theory, and Chapter 2, Information and Con­

ditioning, of Volume II lay the measure-theoretic foundation for probability
theory required for a treatment of continuous-time models. Chapter 1 presents
probability spaces, Lebesgue integrals, and change of measure. Independence,
conditional expectations, and properties of conditional expectations are intro­
duced in Chapter 2. These chapters are used extensively throughout the text,
but some readers, especially those with exposure to probability theory, may
choose to skip this material at the outset, referring to it as needed.
Chapter 3, Brownian Motion, introduces Brownian motion and its proper­
ties. The most important of these for stochastic calculus is quadratic variation,
presented in Section 3.4. All of this material is needed in order to proceed,
except Sections 3.6 and 3.7, which are used only in Chapter 7, Exotic Options
and Chapter 8, Early Exercise.
The core of Volume II is Chapter 4, Stochastic Calculus. Here the Ito
integral is constructed and Ito's formula (called the It6-Doeblin formula in
this text) is developed. Several consequences of the It6-Doeblin formula are
worked out. One of these is the characterization of Brownian motion in terms
of its quadratic variation (Levy's theorem) and another is the Black-Scholes
equation for a European call price (called the Black-Scholes-Merton equation
in this text). The only material which the reader may omit is Section 4.7,

Brownian Bridge. This topic is included because of its importance in Monte
Carlo simulation, but it is not used elsewhere in the text.
Chapter 5, Risk-Neutral Pricing, states and proves Girsanov's Theorem,
which underlies change of measure. This permits a systematic treatment of
risk-neutral pricing and the FUndamental Theorems of Asset Pricing (Section
5.4). Section 5.5, Dividend-Paying Stocks, is not used elsewhere in the text.
Section 5.6, Forwards and Futures, appears later in Section 9.4 and in some
exercises.
Chapter 6, Connections with Partial Differential Equations, develops the
connection between stochastic calculus and partial differential equations. This
is used frequently in later chapters.


Introduction XIX

With the exceptions noted above, the material in Chapters is fun­
1--6
damental for quantitative finance is essential for reading the later chapters.
Chapter 6, the reader choices.
After has
Chapter 7, Exotic Options, not in subsequent chapters, nor is Chap­
is used
ter 8, Early Exercise. Chapter 9, Change of Numeraire, plays an important
role in Section Forward LIBOR model, but is not otherwise used. Chapter
10.4,
Term Structure Models, and Chapter Introduction to Jump Processes,
10, 11,
are not used elsewhere in the text.


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-19-0.png)
1


General Probability Theory


1 . 1 Infinite Probability Spaces


An infinite probability space is used to model a situation in which a random
experiment with infinitely many possible outcomes is conducted. For purposes
of the following discussion, there are two such experiments to keep in mind:

{i) choose a number from the unit interval [0,1), and
{ii) toss a coin infinitely many times.
In each case, we need a sample space of possible outcomes. For {i), our
sample space will be simply the unit interval [0, 1]. A generic element of [0, 1]
will be denoted by w, rather than the more natural choice x, because these
elements are the possible outcomes of a random experiment.
For case {ii), we define

il00 = the set of infinite sequences of H s and Ts. {1.1.1)


. .                                                                           A generic element of il00 will be denoted w = w1w2, where Wn indicates
the result of the nth coin toss.
The samples spaces listed above are not only infinite but are uncountably
infinite (i.e., it is not possible to list their elements in a sequence) . The first
problem we face with an uncountably infinite sample space is that, for most
interesting experiments, the probability of any particular outcome is zero.
Consequently, we cannot determine the probability of a subset A of the sample
space, a so-called event, by summing up the probabilities of the elements in
(2.1.5) 2
as we did in equation of Chapter of Volume I. We must instead
A,
define the probabilities of events directly. But in infinite sample spaces there
are infinitely many events. Even though we may understand well what random
experiment we want to model, some of the events may have such complicated
descriptions that it is not obvious what their probabilities should be. It would
be hopeless to try to give a formula that determines the probability for every
subset of an uncountably infinite sample space. We instead give a formula for


2 1 General Probability Theory


the probability of certain simple events and then appeal to the properties of
probability measures to determine the probability of more complicated events.
This prompts the following definitions, after which we describe the process of
setting up the uniform probability measure on (0, 1).

Definition 1.1.1. Let il be a nonempty set, and let .r be a collection of sub­
sets of il. We say that .r is a u-algebra (called a u-field by some authors}
provided that:
(i} the empty set 0 belongs to .r,
(ii} whenever a set A belongs to .r, its complement Ac also belongs to .r, and
(iii} whenever a sequence of sets A1, A2, . . . belongs to .r, their union U �=1An
also belongs to .r.
If we have a u-algebra of sets, then all the operations we might want to
do to the sets will give us other sets in the u-algebra. If we have two sets A
and B in a u-algebra, then by considering the sequence A, B, 0, 0, . . ., we
0,
can conclude from (i) and (iii) that A U B must also be in the u-algebra. The
same argument shows that if A1, A2, . . ., AN are finitely many sets in a u­
algebra, then their union must also be in the u-algebra. Finally, if A1, A2, . . .
is a sequence of sets in a u-algebra, then because



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-21-0.png)

properties (ii) and (iii) applied to the right-hand side show that n�=1An is
also in the u-algebra. Similarly, the intersection of a finite number of sets in
a u-algebra results in a set in the u-algebra. Of course, if .r is a u-algebra,
then the whole space n must be one of the sets in .r because n = 0c.

Definition 1.1.2. Let n be a nonempty set, and let .r be a u-algebra of sub­
sets of n. A probability measure n» is a function that, to every set A E .r,
assigns a number in (0, 1), called the probability of A and written P(A). We
require:
(i) P(il) = 1, and
(ii} (countable additivity) whenever A1, A2, . . . is a sequence of disjoint sets
in .r, then

The triple (il, .r, P) is called a P (Qprobability space. 1 An) = � P(An)· (1.1.2)
If n is a finite set and .r is the collection of all subsets of n, then .r is a
u-algebra and Definition 1.1.2 boils down to Definition 2.1.1 of Chapter 2 of
Volume I. In the context of infinite probability spaces, we must take care that
the definition of probability measure just given is consistent with our intuition.
The countable additivity condition (ii) in Definition 1.1.2 is designed to take


1.1 Infinite Probability Spaces 3



care [of this. For example, we should be sure that ] 0 [) ][= ][0. That follows from ]
###### JP [(]
taking
A1 = A2 = A3 = · · · = 0
in (1.1.2), for then this equation becomes JP(0) = L =11P(0). The only number
in (0, 1] that (0) could be is
###### JP JP(0) = 0. ( 1.1.3)

We also still want (2.1.7) of Chapter 2 of Volume I to hold: if and B are
###### A
disjoint sets in :F, we want to have
###### JP(A U B) = JP(A) + JP(B). (1.1.4)

Not only does Definition 1.1.2(ii) guarantee this, it guarantees the finite ad­
ditivity condition that if A1, are finitely many disjoint sets in :F,
###### A2, ...,AN
then
(1.1.5)
###### lP (Ql An) [= ] t.JP(An)·



To see this, apply (1.1.2) with
= = = . . . = 0.
###### AN+ [l ] AN+2 AN+3



In the special case that N = 2 and A1 = A, A2 = B, we get (1.1.4). From
part (i) of Definition 1.1.2 and (1.1.4) with B we get
= N,
###### JP(Ac) = 1 -JP(A). (1.1.6)

In suary, from Definition 1.1.2, we conclude that a probability measure
must satisfy (1.1.3)-(1.1.6).
We now describe by example the process of construction of probability
measures on uncountable sample spaces. We do this here for the spaces (0, 1]
and fl00 with which we began this section.
Example 1.1.3 (Uniform (Lebesgue} measure on [0, 1]). We construct a math­
ematical model for choosing a number at random from the unit interval (0, 1]

so that the probability is distributed uniformly over the interval. We define
the probability of closed intervals [a, b] by the formula
###### JP(a, b] = b - a, 0 � a � b � 1, (1.1. 7)

(i.e., the probability that the number chosen is between a and b is b - a).
(This particular probability measure on (0, 1] is called Lebesgue measure and
in this text is sometimes denoted The Lebesgue measure of a subset of
£. JR.
is its "length.") If b = a, then [a, b] is the set containing only the number a,
and (1.1.7) says that the probability of this set is zero (i.e., the probability is
zero that the number we choose is exactly equal to a). Because single points
have zero probability, the probability of an open interval (a, b) is the same as
the probability of the closed interval [a, b); we have


IP'( a, b) = b - a, 0 � a � b � 1. (1.1.8)


00
1 1
###### (a, b) = [ + ;;,, b - ;;,, I a ]
l:J

[


:Fo = {0, fl}. (1.1.9)


1 See Appendix A, Section A.l for the construction of the Cantor set, which gives
some indication of how complicated sets in 8[0, 1] can be.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-23-0.png)
1.1 Infinite Probability Spaces 5

by setting IP'(AH) = p, IP'(Ar) = q. We have now defined IP' for 2 [(21) ] = 4 sets,
and these four sets form a a-algebra; since Ali = Ar we do not need to add
anything else in order to have a a-algebra. We call this a-algebra
:Fi:



:F1 = {0, !l, AH, Ar}.

We next define IP' for the four sets

AH H = The set of all sequences beginning with H H
= {w;w1 = H,w2 = H},
AHr = The set of all sequences beginning with HT
= {w;w1 = H,w2 = T},
ArH = The set of all sequences beginning with TH
= {w;w1 = T,w2 = H},
Arr = The set of all sequences beginning with TT
= {w;w1 = T,w2 = T}

by setting

IP'(AHH) = p [2], IP'(AHr) = pq, IP'(ArH) = pq, IP'(Arr) = q [2]   


(1.1.10)


(1.1.11)



Because of (1.1.6), this determines the probability of the complements AIIH,
AHT• ArH' Arr· Using (1. 1.5), we see that the probabilities of the unions
AHHUArH, AHH U Arr, AHr U ArH, and AHr U Arr are also determined.
We have already defined the probabilities of the two other pairwise unions
AHH U AHr = AH and ArH U Arr = Ar. We have already noted that the
probability of the triple unions is determined since these are complements of
the sets in (1.1.11), e.g.,



AHH u AHr [u ] ArH = Arr·



At this point, we have determined the probability of 2 [(22) ] = 16 sets, and these
sets form a a-algebra, which we call :F2:



sets form a a-algebra, which we call :F2:


                                                              AHH U ArH, AHH U Arr, AHr U ArH, AHr U Arr
(1.1.12)
We next define the probability of every set that can be described in terms
of the outcome of the first three coin tosses. Counting the sets we already
have, this will give us 2 [(] 2 [3) ] = 256 sets, and these will form a a-algebra, which
we call :F3.
By continuing this process, we can define the probability of every set that
can be described in terms of finitely many tosses. Once the probabilities of
all these sets are specified, there are other sets, not describable in terms of
finitely many coin tosses, whose probabilities are determined. For example,
0, !l, AH, Ar, AHH, AHr, ArH, Arr, AIIH, AHr, ArH, Arr'
;2 =
###### { }


6 1 General Probability Theory

the set containing only the single sequence H H H H . . . cannot be described
in terms of finitely many coin tosses, but it is a subset of AH, AH H, AH H H,
etc. Furthermore,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-25-0.png)











This set is in :Fn, and once n and m are known, its probability is defined by
the process outlined above. By the definition of limit, a coin-toss sequence
w = w1w2 . . . satisfies (1.1.13) if and only if for every positive integer m there
exists a positive integer such that for all n we have In other
N          - N wE An,m·
words, the set of w for which (1.1.13) holds is
00 00 00
A =
An,m·
n U n
m=l N=l n=N


1.2 Random Variables and Distributions 7


The set A is in :F00 because it is described in terms of unions and intersections
of sequences of sets that are in :F 00• This does not immediately tell us how to
compute IP'(A), but it tells [us ] that IP'(A) is somehow determined. As it turns
out, the Strong Law of Large Numbers a erts that IP'(A) = 1 if p = ! and
IP'(A) = 0 if p =I=!·
Every subset of il00 we shall encounter will be in :F00• Indeed, it is extremely difficult to produce a set not in :F00, although such sets exist. 0

The observation in Example 1.1.4 that every individual sequence has prob­
ability zero highlights a paradox in uncountable probability spaces. We would
like to say that something that has probability zero cannot happen. In par­
ticular, we would like to say that if we toss a coin infinitely many times, it
cannot happen that we get a head on every toss (we are a uming here that
the probability for head on each toss is p > 0 and q = 1 - p > 0). It would
be satisfying if events that have probability zero are sure not to happen and
events that have probability one are sure to happen. In particular, we would
like to say that we are sure to get at least one tail. However, because the
sequence that is all heads is in our sample space, and is no less likely to hap­
pen than any other particular sequence (every single sequence has probability
zero), mathematicians have created a terminology that equivocates. We say
that we will get at least one tail almost surely. Whenever an event is said to be
almost sure, we mean it has probability one, even though it may not include
every possible outcome. The outcome or set of outcomes not included, taken
together, has probability zero.
a

Definition 1.1.5. Let (il, :F, IP') be a probability space. If a set A E :F satisfies
IP'(A) = 1, we say that the event A occurs almost surely.


1 .2 Random Variables and Distributions


Definition 1.2.1. Let (il, :F, IP') be a probability space. A random variable is
a real-valued function X defined on {l with the property that for every Borel
subset B of JR., the subset of il given by

{X E B} = {w E il; X(w) E B} (1.2.1)

is in the a-algebm :F. (We sometimes also permit a mndom variable to take
the values +oo and -oo.)

To get the Borel subsets of JR., one begins with the closed intervals [a, b] C JR.
and a s all other sets that are necessary in order to have a a-algebra. This
means that unions of sequences of closed intervals are Borel sets. In particular,
every open interval is a Borel set, because an open interval can be written

as the union of a sequence of closed intervals. Furthermore, every open set
(whether or not an interval) is a Borel set because every open set is the union


8 1 General Probability Theory



of a sequence of open intervals. Every closed set is a Borel set because it is
the complement of an open set. We denote the collection of Borel subsets of
lR
by and call it the Borel u-algebm ofR Every subset of we encounter
B(IR) lR
in this text is in this a-algebra.
A random variable X is a numerical quantity whose value is determined
by the random experiment of choosing w E il. We shall be interested in the
probability that X takes various values. It is often the case that the probability
that X takes a particular value is zero, and hence we shall mostly talk about
the probability that X takes a value in some set rather than the probability
that X takes a particular value. In other words, we will want to speak of
Definition 1.2.1 requires that be in :F for all
JP{X E B}. {X E B} BE B(IR),
so that we are sure the probability of this set is defined.
Example 1.2.2 (Stock prices). Recall the independent, infinite coin-toss space
( il00, :F 00, JP) of Example 1.1.4. Let us define stock prices by the formulas



and, in general,



So(w) = 4 for all wE il00,
###### SI(w) = [{] [8] 2If WI = [ �][fwi =H, ] T,

16 if H,
WI = W2 =
4 if
S2(w) = WI =/-w2,
### { 1 if T,
WI = W2 =
S ( ) n+I w - [_ ][{ ][2Sn(w) ][if ] "f [Wn+l = ][H, ]

2 IS ( ) n W [1 ] Wn+I .



"f

2 IS ( ) n W [1 ] Wn+I .
All of these are random variables. They a ign a numerical value to each pos­
sible sequence of coin tosses. FUrthermore, we can compute the probabilities
that these random variables take various values. For example, in the notation
of Example 1.1.4,



0



In the previous example, the random variables etc., have dis­
So, S1, S2,
tributions. Indeed, So = 4 with probability one, so we can regard this random
variable as putting a unit of ma on the number 4. On the other hand,
JP{S2 = 16} = p [2], JP{S2 = 4} = 2pq, and JP{S2 = 1} = q [2] - We can think of
the distribution of this random variable as three lumps of ma, one of size
p [2 ]
located at the number 16, another of size 2pq located at the number 4, and a
third of size q [2 ] located at the number 1. We need to allow for the possibility
that the random variables we consider don't a ign any lumps of ma but
rather spread a unit of ma "continuously" over the real line. To do this, we
should think of the distribution of a random variable as telling us how much
ma is in a set rather than how much ma is at a point. In other words, the
distribution of a random variable is itself a probability measure, but it is a
measure on subsets of rather than subsets of
lR il.


1.2 Random Variables and Distributions 9


Fig. 1.2.1. Distribution measure of X.


Definition 1.2.3. Let X be a mndom variable on a probability space (il, .r, IP').
The distribution measure of X is the probability measure J.Lx that assigns to
each Borel subset B ofiR the mass J.Lx(B) = IP'{X E B} (see Figure 1.2. 1}.

In this definition, the set B could contain a single number. For example,

=
if B = {4}, then in Example 1.2.2 we would have J.Ls2(B) = 2pq. If B

[2, 5], we still have J.Ls2 (B) = 2pq, because the only ma that S2 puts in the
interval [2, 5] is the lump of ma placed at the number 4. Definition 1.2.3
for the distribution measure of a random variable makes sense for discrete
random variables as well as for random variables that spread a unit of ma
"continuously" over the real line.
Random variables have distributions, but distributions and random vari­
ables are different concepts. Two different random variables can have the same
distribution. A single random variable can have two different distributions.
Consider the following example.
Example 1.2.4. Let lP' be the uniform measure on [0, 1] described in Exam­
ple 1.1.3. Define X(w) = w and Y(w) = 1 - w for all w E [0, 1]. Then the
distribution measure of X is uniform, i.e.,

J.Lx[a, b] = IP'{w; a � X(w) � b} = IP'[a, b] = b - a, 0 �a � b � 1,

by the definition of IP'. Although the random variable Y is different from the
random variable X (if X takes the value l, Y takes the value �), Y has the
same distribution as X:


Now suppose we define another probability measure P on [0, 1] by specify­
ing

      - 2 2
IP'[a, b] = 2wdw = b - a, O �a �b �l. (1.2.2)
jb a

J.Ly[a, b] = IP'{w; a � Y(w) � b} = IP'{w; a � 1 - w � b} = IP'[1 - b, 1 - a]
= (1 - a) - (1 - b) = b - a = J.Lx[a, b], 0 �a � b � 1.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-28-0.png)
10 1 General Probability Theory

Equation (1.2.2) and the properties of probability measures determine JP(B)
for every Borel subset B of R Note that JP[O, 1) = 1, so J is in fact a prob­
ability measure. Under J, the random variable X no longer has the uniform
distribution. Denoting the distribution measure of X under lP by iix, we have


=
iix[a, b] = P{w; a � X(w) � b} = JP[a, b) b [2 ]   - a [2], 0 �a � b � 1.

Under J, the distribution of Y no longer agrees with the distribution of X.
We have


= (1 - a) [2 ]           - (1 - b) [2], 0 �a � b � 1. 0


There are other ways to record the distribution of a random variable rather
than specifying the distribution measure J.Lx. We can describe the distribution
of a random variable in terms of its cumulative distribution function ( cdf)

F(x) = lP{X �x}, x E R (1.2.3)

If we know the distribution measure J.Lx, then we know the cdf F because
F(x) = J.Lx( -oo, x] . On the other hand, if we know the cdf F, then we can
compute J.Lx(x, y] = F(y) - F(x) for x < y. For a � b, we have

jiy[a, b] = JP{w; a � Y(w) � b} = JP{w; a � 1 - w � b} = JP[1 - b, 1 - a]



and so we can compute [2 ]



00

[a, b] = n (a - �, b] '
n=l



J.Lx[a, b] = n-too lim J.Lx (a - l., n b] = F(b) - n-too lim F(a - 1.). n (1.2.4)



Once the distribution measure J.Lx [a, b] is known for every interval [a, b] C JR., it
is determined for every Borel subset of R Therefore, in principle, knowing the
cdf F for a random variable is the same as knowing its distribution measure
/LX ·
In two special cases, the distribution of a random variable can be recorded
in more detail. The first of these is when there is a density function f(x), a
nonnegative function defined for x E JR. such that



=
J.Lx[a, b] JP{a �X � b} = f(x) dx, -oo < a � b < oo. (1.2.5)
### 1 [b ]

[3 ]



In particular, because the closed intervals [-n, n] have union JR., we must have [3 ]



2 See Appendix A, Theorem A.l.1(ii) for more detail.
See Appendix A, Theorem A.l.1(i) for more detail.
3


1.2 Random Variables and Distributions 1 1
f(x) dx = limn-too f [�] n f(x) dx = [lim] n [-too ] IP'{ [-n ] ::; X ::; [n] }
f�oo = IP'{ X E lR} = IP'( !2) = 1. ( 1 .2.6)



(For purposes of this discussion, we are not considering random variables that
can take the value ±oo. [) ]
The second special case is that of a probability mass function, in which
case there is either a finite sequence of numbers x1, x2, ...,x N or an infinite
sequence x1, x2, . . . such that with probability one the random variable X
takes one of the values in the sequence. We then define Each
Pi = IP'{X =xi}·



takes one of the values in the sequence. We then define Each

Pi is nonnegative, and Li Pi = 1. The mass a igned to a Borel set B C lR by
the distribution measure of X is
JLx(B) = L Pi, {i;x;EB} B E B(JR). (1.2.7)



The distribution of some random variables can be described via a density,



as in (1.2.5). For other random variables, the distribution must be described in
terms of a probability ma function, as in (1.2.7). There are random variables
whose distribution is given by a mixture of a density and a probability ma
function, and there are random variables whose distribution has no lumps of
ma but neither does it have a density.4 Random variables of this last type
have applications in finance but only at a level more advanced than this part
of the text.
Example 1.2.5. (Another mndom variable uniformly distributed on {0,1].} We
construct a uniformly distributed random variable taking values in [0, 1] and
defined on infinite coin-toss space !200• Suppose in the independent coin-toss
space of Example 1.1.4 that the probability for head on each toss is p = .

                                      For n = 1, 2, . . ., we define


(1.2.8)


We set

also happens with probability �, then � ::; X ::; 1. If = Y1 = 0 and Y2 = 0, which
happens with probability .!, then 0 ::; X ::; �. If Y1 0 and Y2 = 1, which also
happens with probability then ::; X ::; . This pattern continues; indeed
�,            -            

4 See Appendix A, Section A.3.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-30-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-30-1.png)
12 1 General Probability Theory


Taking unions of intervals of this form and using the finite additivity of
probability measures, we see that whenever k, m, and n are integers and
0 � k � m � 2 [n], we have


1.2.9


function


The function N(x) is strictly increasing, mapping JR. onto (0, 1), and so has a
strictly increasing inverse function N [-1] (y). In other words, N(N [-1] (y)) = y
for all y E (0, 1) . Now let Y be a uniformly distributed random variable,
defined on some probability space (.!?, F, IP') (two possibilities for (.!?, F, IP')
and Y are presented in Examples 1.2.4 and 1.2.5, and set X N [-1] (Y).
) =
Whenever < a � b < we have
-oo oo,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-31-0.png)

fLx[a, b] = IP'{w E .!?; a � X(w) � b}
= IP'{w E .!?; a � N [-1] (Y(w)) � b}
= IP'{w E .!?; N(a) � N(N [-1] (Y(w))) � N(b)}
= IP'{w E .!?; N(a) � Y(w) � N(b)}
= N(b) - N(a)



= cp(x) dx.
1b



The measure on given by this formula is called the standard normal
/LX JR.
distnbution. Any random variable that has this distribution, regardless of the
probability space ( .!t, F, IP') on which it is defined, is called a standard normal
random variable. The method used here for generating a standard normal
random variable from a uniformly distributed random variable is called the
probability integral transform and is widely used in Monte Carlo simulation.
Another way to construct a standard normal random variable is to take
.!t = JR., F = B(IR.), take IP' to be the probability measure on JR. that satisfies


1.3 Expectations 13

IP'[a, b] = cp(x) dx whenever          - oo < a � b < oo,
1b

and take X(w) = w for all w E JR D

The second construction of a standard normal random variable in Example
1.2.6 is economical, and this method can be used to construct a random vari­
able with any desired distribution. However, it is not useful when we want to
have multiple random variables, each with a specified distribution and with
certain dependencies among the random variables. For such cases, we con­
struct (or at least a ume there exists) a single probability space (.a, .r, IP') on
which all the random variables of interest are defined. This point of view may
seem overly abstract at the outset, but in the end it pays off handsomely in
conceptual simplicity.


1.3 Expectations

Let X be a random variable defined on a probability space (.a, .r, IP'). We would
like to compute an "average value" of X, where we take the probabilities into
a ount when doing the averaging. If .a is finite, we simply define this average
value by
lEX = L X(w)IP'(w).

wEn
If .a is countably infinite, its elements can be listed in a sequence WI, w2, w3, . . .,
and we can define lEX as an infinite sum:

00
lEX = L X(wk)IP'(wk)·
k=I
Diculty arises, however, if .a is uncountably infinite. Uncountable sums can­
not be defined. Instead, we must think in terms of integrals.
To see how to go about this, we first review the Riemann integral. If f(x) is

a continuous function defined for all x in the closed interval [a, b], we define the
Riemann integral J: f(x)dx as follows. First partition [a, b] into subintervals

[xo, XI], [x1, x2], . . ., [xn-I, Xn], where a = xo < XI < · · · < Xn = b. We denote
by II = {xo, XI, . . ., Xn} the set of partition points and by


the length of the longest subinterval in the partition. For each subinterval

n
RSjj (f) = L Mk(Xk - Xk-I),
k=I

[xk-I, xk], we set Mk = ma k_1::;x::;xk f(x) and mk = minxk_1::;x::;xk f(x).
The upper Riemann sum is


14 1 General Probability Theory


and the lower Riemann sum (see Figure 1.3.1) is

n
RS]j(f) = L mk (xk - Xk-d·
k=l

As 111 1 converges to zero (i.e., as we put in more and more partition points,
and the subintervals in the partition become shorter and shorter), the upper
Riemann sum RSjj(!) and the lower Riemann sum RS]j(f) converge to the
same limit, which we call J: f(x)dx. This is the Riemann integral.


y



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-33-0.png)





We define the lower Lebesgue sum to be (see Figure 1.3.2)
00
LS]j(X) = LYklP(Ak)·
k=l


1.3 Expectations 15

This lower sum converges as III I, the maximal distance between the Yk par­
tition points, approaches zero, and we define this limit to be the Lebesgue
integral In X(w) dlP(w), or simply In X diP. The Lebesgue integral might be

oo, because we have not made any a umptions about how large the values of
can be.
X
We a umed a moment ago that 0 � X(w) < oo for every w E il. If the
set of w that violates this condition has zero probability, there is no effect on
the integral we just defined. lf !P'{w; X(w) ; 0} = 1 but IP'{w; X(w) = oo} - 0,
then we define In X(w)dlP(w) = oo.


Fig. 1.3.2. Lower Lebesgue sum.


Finally, we need to consider random variables X that can take both pos­
itive and negative values. For such a random variable, we define the positive
negative parts of X by
and



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-34-0.png)

x [+] (w) = max{X(w), O}, x [-] (w) = max{-X(w), O}. (1.3.1)

Both x+ and x- are nonnegative random variables, X = x+ - x-, and
lXI = x [+ ] + x [-] . Both In x [+] (w) dlP(w) and In x [- ] (w) dlP(w) are defined by
the procedure described above, and provided they are not both oo, we can
define
X(w) dlP(w) = x [+] (w) dlP(w) x [- ] (w) dlP(w). (1.3.2)
###### -l
l l

- [f ] In X [+] (w) dlP(w) and In X [-] (w) dlP(w) are both finite, we say that X is
tntegrable, and In X(w) dlP(w) is also finite. If In x+(w) dlP(w) = 00 and


16 1 General Probability Theory

In X [- ] (w) diP'(w) is finite, then In X(w) diP'(w) = oo. If In X [+] (w) diP'(w)
is finite and In x [-] (w) d!P'(w) = oo, then In X(w) d!P'(w) = -00. If both
In X [+] (w) diP'(w) = oo and In X [-] (w) diP'(w) = oo, then an ["] oo - oo [" ] situa­
tion arises in (1.3.2), and In X(w) d!P'(w) is not defined.
The Lebesgue integral has the following basic properties.

Theorem 1.3.1. Let X be a random variable on a probability space (il, .1', JP).
{i) If X takes only finitely many values Yo, Yt. Y2, . . ., Yn, then



(ii} (Integrability) The random variable X is integrable if and only if

iX(w)i d!P'(w) <
oo.
fn



Now let Y be another random variable on (il,.1', 1P).
{iii} (Comparison) If X :S Y almost surely (i.e., JP{X :S Y} = 1}, and if
In X(w) d!P'(w) and In Y(w) d!P'(w) are defined, then

X(w) d!P'(w) Y(w) d!P'(w).
:S
###### l l



In particular, if X = Y almost surely and one of the integrals is defined,
then they are both defined and

X(w) d!P'(w) = Y(w) d!P'(w).
###### l l



{iv} (Linearity) If a and {3 are real constants and X and Y are integrable, or
if a and {3 are nonnegative constants and X and Y are nonnegative, then

(aX(w) + {JY(w)) d!P'(w) X(w) d!P'(w) + {J Y(w) d!P'(w).
###### l =a l l

PARTIAL PROOF:
For (i), we consider only the case when X is almost surely
nonnegative. If zero is not among the YkS, we may add Yo = 0 to the list and
then relabel the YkS if necessary so that 0 = Yo < Y1 < Y2 < · · · < Yn· Using
these as our partition points, we have Ak = {Yk :S X < Yk+l} = {X = Yk}
and the lower Lebesgue sum is
n
LSJ7(X) = L YklP{X = Yk}·
k=O
If we put in more partition points, the lower Lebesgue sum does not change,
and hence this is the Lebesgue integral.
also


1.3 Expectations 17

We next consider part (iii). If X � Y almost surely, then x [+ ]  - y [+ ] and
x- - y [-] almost surely. Because x [+ ] - y [+ ] almost surely, for every partition
II, the lower Lebesgue sums satisfy LS.U(X [+] ) � LS.U(Y [+] ), so
x [+] (w) dlP'(w) � y [+] (w) dlP'(w). (1.3.3)
###### l l

Because x [-] - y [-] almost surely, we also have
x [-] (w) dlP'(w) [� ] y [-] (w) dlP'(w). (1.3.4)
###### l l

Subtracting (1.3.4) from (1.3.3) and recalling the definition (1.3.2), we obtain
the comparison property (iii).
The linearity property (iv) requires a more detailed analysis of the con­
struction of Lebesgue integrals. We do not provide that here.
We can use the comparison property (iii) and the linearity property (iv)
to prove (ii) as follows. Because lXI = x [+ ] + x [-], we have x [+ ] - lXI and
x- - lXI. If In IX(w)l dlP'(w) < oo, then the comparison property implies
In X [+] (w) dlP'(w) < oo and In X [- ] (w) dlP'(w) < oo, and X is integrable by
definition. On the other hand, if X is integrable, then In x [+] (w) dlP'(w) < 00
and In x [-] (w) dlP'(w) < oo. Adding these two quantities and using (iv), we see
that In IX(w)l dlP'(w) < oo. D



Remark 1.3.2. We often want to integrate a random variable X over a subset
A of {l rather than over all of il. For this reason, we define

X(w) dlP'(w) = HA(w)X(w) dlP'(w) for all A E F,
###### l
i



Where HA is the indicator junction {random variable} given by


###### n A w ( ) = [{ ][1 ][if w ][E A, ]

0 if w ¢ A.



If A and B are disjoint sets in F, then nA + nB = nAuB and the linearity
property (iv) of Theorem 1.3.1 implies that

X(w) dlP'(w) = X(w) dlP'(w) + X(w) dlP'(w).


Definition 1.3.3. Let X be a random variable on a probability space ( {l, F, IP).



Definition 1.3.3. Let X be a random variable on a probability space ( {l, F, IP).
The expectation (or expected value) of X is defined to be



lEX = X(w) dlP'(w).
###### l



definition makes sense if X is integrable, i.e.; if
This


18 1 General Probability Theory

lEIXI = IX(w)i dlP(w) < oo
In

or if X � 0 almost surely. In the latter case, lEX might be oo.

We have thus managed to define lEX when X is a random variable on an
abstract probability space (n,.r, P). We restate in terms of expected values
the basic properties of Theorem 1.3.1 and add an additional one.

Theorem 1.3.4. Let X be a random variable on a probability space (n, .r, P).
{i} If X takes only finitely many values xo, Xt. . . ., Xn, then

n
lEX = L XkP{X = xk}.
k=O
In particular, if n is finite, then

lEX = L X(w)P(w).

wen
{ii} (Integrability) The random variable X is integrable if and only if
JEIXI < oo.
Now let Y be another random variable on (n, .r, P).
{iii} (Comparison) If X � Y almost surely and X and Y are integrable or
almost surely nonnegative, then
lEX � lEY.

In particular, if X = Y almost surely and one of the random variables is
integrable or almost surely nonnegative, then they are both integrable or
almost surely nonnegative, respectively, and
lEX = lEY.

{iv) (Linearity) If a and {3 are real constants and X and Y are integrable or
if a and {3 are nonnegative constants and X and Y are nonnegative, then

E( aX + {3Y) = alEX + {3JEY.

(v) (Jensen's inequality) If r.p is a convex, real-valued function defined on
JR., and if lEI XI < oo, then
r.p(JEX) � JEr.p(X).


PROOF:
The only new claim is Jensen's inequality, and the proof of that is
the same as the proof given for Theorem 2.2.5 of Chapter 2 of Volume I. D


1 . 3 Expectations 19

Example 1.3.5. Consider the infinite independent coin-toss space floc of Ex­
ample 1.1.4 with the probability measure IP' that corresponds to probability

                                          for head on each toss. Let


Yn(w) =
{ 0 If Wn = [1 ][�][f Wn = H, ] T.

Even though the probability space floc is uncountable, this random variable
takes only two values, and we can compute its expectation using Theorem
1.3.4(i):
1
lEYn = 1 · 1P'{Yn = 1} + 0 · IP'{Yn = 0} =
2"

Example 1.3. 6. Let fl = [0, 1], and let IP' be the Lebesgue measure on [0, 1]
(see Example 1.1.3). Consider the random variable


X(w) =
{ 0 If w [1 ][�][f w ] IS [�][s irr�tional, ] rational.

Again the random variable takes only two values, and we can compute its
expectation using Theorem 1.3.4(i):

lEX = 1 · IP'{w E [0, 1]; w is irrational} + 0 · IP'{w E [0, 1]; w is rational}.

There are only countably many rational numbers in [0, 1] (i.e., they can all

.
be listed in a sequence XI> x2, x3, . . ). Each number in the sequence has
probability zero, and because of the countable additivity property (ii) of
Definition 1.1.2, the whole sequence must have probability zero. Therefore,
IP'{w E [0, 1]; w is rational} = 0. Since IP'[O, 1] = 1, the probability of the set of
irrational numbers in [0, 1] must be 1. We conclude that lEX = 1.
The idea behind this example is that if we choose a number from [0, 1]
a ording to the uniform distribution, then with probability one the number
chosen will be irrational. Therefore, the random variable X is almost surely
equal to 1, and hence its expected value equals 1. As a practical matter,
of course, almost any algorithm we devise for generating a random number

[0, 1] will generate a rational number. The uniform distribution is often
in
a reasonable idealization of the output of algorithms that generate random
numbers in [0, 1], but if we push the model too far it can depart from reality.
If we had been working with Riemann rather than Lebesgue integrals, we
would have gotten a different result. To make the notation more familiar, we
write x rather than w and f(x) rather than X(w), thus defining


f(x) = (1.3.5)
{ 0 If [1 ][�][f ] X IS [x ][�][s irr�tional, ] ratiOnal.

We have just seen that the Lebesgue integral of this function over the interval

[ [0], 1] is 1.


20 1 General Probability Theory


To construct the Riemann integral, we choose partition points 0 = xo <
x1 < x2 < · · · < Xn = 1. We define


0


lR


5 This concept is discussed in more detail in Appendix A, Section A.2.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-39-0.png)
1.3 Expectations 21


Definition 1.3.7 is similar to Definition 1.1.2, except that now some sets
have [measure greater than 1. The Lebesgue measure of every interval is its ]
length, so that [JR. ] [and half-lines ] [a, [oo] ) [and ] ( [-oo, ][b] ] [have infinite Lebesgue ]
measure, single points have Lebesgue measure zero, and the Lebesgue measure
the [empty set is zero. Lebesgue measure has the finite additivity property ]
of
(see (1.1.5))


Because of the a umption that f is Borel measurable, even though these
sets Bk can be quite complicated, they are Borel subsets of JR. and so their
Lebesgue measures are defined. We define the lower Lebesgue sum

00
LS[i(f) = L Yk [.C.(B] k).
k=l

As 111 1 converges to zero, these lower Lebesgue sums will converge to a limit,
which we define to be f(x) d.C.(x). It is possible that this integral gives the
fiR
value
oo.
We a umed a moment ago that 0 � f(x) < for every x E R If the set
oo
of x where the condition is violated has zero Lebesgue measure, the integral
of f is not affected. If .C.{x E JR.; f(x) < 0} = 0 and .C.{x E JR.; f(x) = oo} > 0,
we define fiR f(x)d.C.(x) = oo.
We next consider the possibility that f(x) takes both positive and negative
In this case, we define
values.

j [+] (x) = max{!(x), O}, f [-] (x) = max{-f(x), O}.

Because J [+ ] and f- are nonnegative, fiR J [+] (x) d.C.(x) and fiR f-(x) d.C.(x) are
defined by the procedure described above. We then define
f(x) d.C.(x) = J [+] (x) d.C.(x) r(x) d.C.(x),
1 1 -1



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-40-0.png)
22 1 General Probability Theory



provided this is not oo - oo . In the case where both IR J [+] (x) d.C(x) and
IR J-(x) d.C(x) are infinite, IR J(x) d.C(x) is not defined. If IR J [+] (x) d.C(x)
and IR f [-] ( x) d.C( x) are finite, we say that f is integmble. This is equivalent to
the condition IIR 1/(x)l d.C(x) < oo. The Lebesgue integral just constructed has
the comparison and linearity properties described in Theorem 1.3.1. Moreover,
if f takes only finitely many values Yo, YI. Y2, . . ., Yn• then

R
k=O
###### 1 [f(x) d.C(x) ][= ] [t][ yk .C{x ][E ][IR; f(x) ][= ][Y][k}][, ]

provided the computation of the right-hand side does not require that
oo - oo
be a igned a value.
Finally, sometimes we have a function f(x) defined for every x E but
lR
want to compute its Lebesgue integral over only part of IR, say over some set
B E B(IR). We do this by multiplying f(x) by the indicator function of B:
###### li ( ) B X = [{ ][1 if ][X ][E B, ]

0 if X                       - B.



The product f(x)liB(x) agrees with f(x) when x E B and is zero when x � B.
We define
f(x) d.C(x) = liB(x)f(x) d.C(x).
L l

The following theorem, whose proof is beyond the scope of this book,
relates Riemann and Lebesgue integrals on
JR.

Theorem 1.3.8. (Comparison of Riemann and Lebesgue integrals).
Let f be a bounded function defined on IR, and let a b be numbers.
<
(i) The Riemann integml I: f(x)dx is defined (i.e., the lower and upper Rie­
mann sums converge to the same limit) if and only if the set of points x
in [a, b] where f(x) is not continuous has Lebesgue measure zero.
(ii} If the Riemann integml I: f(x)dx is defined, then f is Borel measumble
(so the Lebesgue integml I[a,b) f(x) d.C(x) is also defined}, and the Rie­
mann and Lebesgue integmls agr .

A single point in has Lebesgue measure zero, and so any finite set of
lR
points has Lebesgue measure zero. Theorem 1.3.8 guarantees that if we have a
real-valued function f on lR that is continuous except at finitely many points,
then there will be no difference between Riemann and Lebesgue integrals of
this function.

Definition 1.3.9. If the set of numbers in lR that fail to have some property
is a set with Lebesgue measure zero, we say that the property holds almost
everywhere.

1.3.8(i)
Theorem may be restated as:


1.4 Convergence of Integrals 23


The Riemann integral f(x)dx exists if and only if f(x) is almost
I:
everywhere continuous on [a, b].
Because the Riemann and Lebesgue integrals agree whenever the Riemann
integral is defined, we shall use the more familiar notation f(x) dx to denote
I:
the Lebesgue integral rather than f(x) d£(x). If the set B over which we
wish to integrate is not an interval, we shall write I[a,b) f(x) dx. When we are
I8
developing theory, we shall understand f(x) dx to be a Lebesgue integral;
I8
when we need to compute, we will use techniques learned in calculus for
computing Riemann integrals.


1.4 Convergence of Integrals


There are several w.ays a sequence of random variables can converge. In this
section, we consider the case of convergence almost surely, defined as follows.

Definition 1.4.1. Let XI, x2, X3, 0 0 0 be a sequence of random variables, all
defined on the same probability space ( il, .1", IP'). Let X be another random
variable defined on this space. We say that X I, X 2, X 3, . . . converges to X
almost surely and write

lim Xn = X almost surely
n-+oo

. .
if the set ofw E il for which the sequence of numbers XI(w), X2(w), X3(w), .
has limit X(w) is a set with probability one. Equivalently, the set ofw E il for
which the sequence of numbers XI(w), X2(w), X3(w), . . . does not converge to
X(w) is a set with probability zero.

Example 1.4.2 {Strong Law of Large Numbers). An intuitively appealing case
of almost sure convergence is the Strong Law of Large Numbers. On the infi­
nite independent coin-toss space .!200, with the probability measure chosen to
correspond to probability p = � of head on each toss, we define

Yk(w) =
{ 0 [1 ] I [�] f [f ][Wk ] Wk = [= ] T, [H, ]

and


k=I
so that Hn is the number of heads obtained in the first n tosses. The Strong
of Large Numbers is a theorem that a erts that
Law

1
Hn
lim - =         - almost surely.
n-+oo n 2


24 1 General Probability Theory


In other words, the ratio of the number of heads to the number of tosses
approaches almost surely. The "almost surely" in this a ertion acknowl­

       edges the fact that there are sequences of tosses, such as the sequence of all
heads, for which the ratio does not converge to We shall ultimately see
�.
that there are in fact uncountably many such sequences. However, under our
a umptions that the probability of head on each toss is and the tosses are

                                independent, the probability of all these sequences taken together is zero. 0

Definition 1.4.3. Let h, /2, fa, . . . be a sequence of real-valued, Borel-measur­
able functions defined on JR. Let f be another real-valued, Borel-measurable
function defined on R We say that h, /2, fa, . . . converges to f almost every­
where and write
lim f n = f almost everywhere
n-+oo
if the set of x E for which the sequence of numbers !I (x), h(x), fa(x), . . .
lR
does not have limit f(x) is a set with Lebesgue measure zero.

It is clear from these definitions that convergence almost surely and con­
vergence almost everywhere are really the same concept in different notation.
Example 1.4.4. Consider a sequence of normal densities, each with mean zero
and the nth having variance � (see Figure 1.4.1):



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-43-0.png)



Therefore, the sequence /I, /2, fa, . . . converges everywhere to the function



fa,
###### f [*] (x) = [{][ O �f x -:/: 0, ]

00 If X = 0,



and converges almost everywhere to the identically zero function f(x) = 0 for
all x E The set of x where the convergence to f(x) does not take place
R
contains only the number 0, and this set has zero Lebesgue measure. 0
Often when random variables converge almost surely, their expected values
converge to the expected value of the limiting random variable. Likewise,
when functions converge almost everywhere, it is often the case that their
Lebesgue integrals converge to the Lebesgue integral of the limiting function.
This is not always the case, however. In Example 1.4.4, we have a sequence
of normal densities for which �oo fn(x)dx = 1 for every n but the almost
f
everywhere limit function f is identically zero. It would not help matters to
use the everywhere limit function f [*] (x) because any two functions that differ
only on a set of zero Lebesgue measure must have the same Lebesgue integral.


1.4 Convergence of Integrals 25



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-44-0.png)





to





the left-hand side is 1 and the right-hand side is 0.
Incidentally, matters are even worse with the Riemann integral, which is
not defined for f*; upper Riemann sums for f* are infinite, and lower Riemann
sums are zero.
To get the integrals of a sequence of functions to converge to the integral of
the limiting function, we need to impose some condition. One condition that
guarantees this is that all the functions are nonnegative and they converge to
their limit from below. If we think of an integral as the area under a curve, the
aumption is that as we go farther out in the sequence of functions, we keep
a ing area and never taking it away. If we do this, then the area under the


26 1 General Probability Theory


limiting function is the limit of the areas under the functions in the sequence.
The precise statement of this result is given in the following theorem.

Theorem 1.4.5 (Monotone convergence). Let X�, X2, X a, . . . be a se­
quence of mndom variables converging almost surely to another mndom vari­
able X. If
0 $ XI $ X2 $ Xa $ . . . almost surely,
then
lim IEXn = lEX.
n-+oo
Let /I, /2, fa, . . . be a sequence of Borel-measumble functions on JR. converging
almost everywhere to a function f. If



0 $ /I $ /2 $ fa $ . . . almost everywhere,
then



n [�] - [�-: ][fn(x) ][dx ][=]
### I [: ][f][(x) ][dx. ]



The following corollary to the Monotone Convergence Theorem extends
Theorem 1.3.4(i).

Corollary 1.4.6. Suppose the nonnegative mndom variable X takes countably
many values xo, x�, x2, . . . . Then

00
lEX = �kiP{ X = Xk}· (1.4.1)
k=O

PROOF: Let Ak = {X = xk}, so that X can be written as

00
X = L: xkliAk ·
k=O
Define Xn = E�=O XkliAk . Then 0 $ X I $ x2 $ X a $ . . . and limn-+oo Xn =
X almost surely ("surely," actually). Theorem 1.3.4(i) implies that
n
IEXn = L XkiP{X = Xk}·
k=O
Taking the limit on both sides as n - and using the Monotone Convergence
oo
Theorem to justify the first equality below, we obtain
n oo
lEX = lim IEXn = lim n-+oo n-+oo k=O = xk} = k=O = Xk}· 0
Remark 1 7. If X can take negative as well as positive values, we can apply
Corollary 1.4.6 to x [+ ] and x- separately and then subtract the resulting
equations to again get formula (1.4.1), provided the subtraction does not
create "oo - situation.
an oo [" ]


1.5 Computation of Expectations 27


Example 1.4.8 (St. Petersburg paradox). On the infinite independent coin­
toss space il00 with the probability of a head on each toss equal to, define
!
a random variable X by


X(w) =


This defines X(w) for every sequence of coin tosses except the sequence that
is all tails. For this sequence, we define X(TTT . . . ) = oo. The probability
that X = oo is then the probability of this sequence, which is zero. Therefore,
X is finite almost surely. According to Corollary 1.4.6,

lEX = 2 · IP'{X = 2} + 4 · IP'{X = 4} + 8 · IP'{X = 8} + . . .
1 1 1
= 2 · - + 4 · - + 8 · - + . . .
2 4 8
= 1 + 1 + 1 + [. ][. . ] = oo.

The point is that lEX can be infinite, even though X is finite almost surely.
0

The following theorem provides another common situation in which we are
a ured that the limit of the integrals of a sequence of functions is the integral
the limiting function.
of

Theorem 1.4.9 (Dominated convergence). Let XI, x2, . . . be a sequence
of random variables converging almost surely to a random variable X. If there
is another random variable Y such that lEY < oo and IXnl : Y almost surely
for every n, then
lim EXn = EX.
n-+oo
Let /I, h, . . . be a sequence of Borel-measurable functions on JR. converging
almost everywhere to a function f. If there is another function g such that
f�oo g( x) dx < oo and Ifn I : g almost everywhere for every n, then


Computation of Expectations
1 .5

Let X be a random variable on some probability space (il, :F, IP'). We have
defined the expectation of X to be the Lebesgue integral

fn(x) dx = f(x) dx.
###### nl��/_ /_:
:



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-46-0.png)
28 1 General Probability Theory



lEX = X (w) dlP'(w ),
l



the idea being to average the values of X(w) over fl, taking the probabilities
into account. This level of abstraction is sometimes helpful. For example, the
equality
JE(X + Y) = lEX + lEY
follows directly from the linearity of integrals. By contrast, if we were to
derive this fact using a joint density for X and Y, it would be a tedious,
unenlightening computation.
On the other hand, the abstract space fl is not a pleasant environment in
which to actually compute integrals. For computations, we often need to rely
on densities of the random variables under consideration, and we integrate
these over the real numbers rather than over fl. In this section, we develop
the relationship between integrals over fl and integrals over
R
Recall that the distribution measure of X is the probability measure J-Lx
defined on JR. by



J-Lx(B) = JP{X E B} for every Borel subset B of R (1.5.1)



Because J-Lx is a probability measure on JR., we can use it to integrate functions
over JR We have the following fundamental theorem relating integrals over JR.
to integrals over fl.

Theorem 1.5.1. Let X be a mndom variable on a probability space (fl, F, JP)
and let g be a Borel-measumble function on R. Then


lEig(X)I = lg(x)l dJ-Lx(x), (1.5.2)

          
and if this quantity is finite, then


lEg(X) = g(x) dJ-Lx(x). (1.5.3)

          
PROOF:
The proof proceeds by several steps, which collectively are called the
standard machine.

Step 1. Indicator functions. Suppose the function g(x) = H8(x) is the indicator
of a Borel subset of Since this function is nonnegative, (1.5.2) and (1.5.3)
R
reduce to the same equation, namely



lEHB(X) = HB(x) dJ-Lx(x). (1.5.4)
l



Since the random variable HB(X) takes only the two values one and zero, its
expectation is


1.5 Computation of Expectations 29
lEHB(X) = 1 · 1P'{X E B} + 0 · IP'{X fj. B} = IP'{X E B}.



Similarly, the function HB(x) of the dummy (not random!) variable x takes only
the two values one and zero, so according to Theorem 1.3.1 (i) with fl = IR,
X = nB, and IP' = J.Lx, its integral is

HB(x) dJ.Lx(x) = 1 · J.Lx{x; HB(x) = 1} + 0 · J.Lx{x; HB(x) = 0} = J.Lx(B).
l

In light of (1.5.1), we have gotten the same result in both cases, and (1.5.4)
is proved.


Step 2. Nonnegative simple functions. A simple function is a finite sum of
indicator functions times constants. In this step, we a ume that
n



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-48-0.png)








30 1 General Probability Theory


At the next stage n + 1, the partition points include all those at stage n and
new partition points at the midpoints between the old ones. Because of this
fact, the simple functions



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-49-0.png)







and we can subtract these two equations because this is not an situ­
ation. The result of this subtraction is (1.5.3).
0

Theorem 1.5.1 tells us that in order to compute the Lebesgue integral
lEX = J: X(w) dlP(w) over the abstract space fl, it suffices to compute the
integral [J] Rg(x) dJLx(x) over the set of real numbers. This is still a Lebesgue
integral, and the integrator is the distribution measure JLx rather than the
Lebesgue measure. To actually perform a computation, we need to reduce
this to something more familiar. Depending on the nature of the random
variable X, the distribution measure on the right-hand side of (1.5.3) can
/-LX


1.5 Computation of Expectations 31

have different forms. In the simplest case, X takes only finitely many values

x [0 ], XI > x2, . . . [, X] n [, ] and then J-Lx places a ma of size Pk = IP'{X = xk} at each
number Xk · In this case, formula (1.5.3) becomes



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-50-0.png)

The most common case for continuous-time models in finance is when
X has a density. This means that there is a nonnegative, Borel-measurable
function f defined on lR such that



J-Lx(B) = f(x) dx for every Borel subset B of R (1.5.5)
l



This density allows us to compute the measure J-Lx of a set B by computing
an integral over B.· In most cases, the density function f is bounded and
continuous or almost everywhere continuous, so that the integral on the right­
hand side of (1.5.5) can be computed as a Riemann integral.
If X has a density, we can use this density to compute expectations, as
shown by the following theorem.

Theorem 1.5.2. Let X be a random variable on a probability space (n, .1", IP'),
and let g be a Borel-measurable function on JR. Suppose that X has a density
f {i.e., f is a function satisfying {1.5.5}}. Then



lEig(X)I = lg(x)lf(x) dx. (1.5.6)
###### /_:



If this quantity is finite, then



lEg(X) = g(x)f(x) dx. (1.5. 7)
###### /_:



PROOF: The proof proceeds again by the standard machine.



Step 1. Indicator functions. If g(x) = HB(x), then because g is nonnegative,
equations (1.5.6) and (1.5.7) are the same and reduce to



lEHB(X) = f(x) dx.
l



The left-hand side is IP'{X E B} = J-Lx(B), and (1.5.5) shows that the two
sides are equal.



Step 2. Simple functions. If g(x) = L�=l akHBk(x), then


32 1 General Probability Theory



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-51-0.png)





0



because division by zero is undefined. We could rewrite this equation as

Z(w )IP'(w) = JP(w ), (1.6.2)

and now we have a meaningful equation, with both sides equal to zero, but the
equation tells us nothing about the relationship among IP', JP, and Z. Because


1.6 Change of Measure 33



IP'(w) = [P] (w) = 0, the value of Z(w) could be anything and (1.6.2) would still
hold.
However, (1.6.2) does capture the spirit of what we would like to accom­
plish. To change from lP to iP, we need to rea ign probabilities in {l using Z to
tell us where in {l we should revise the probability upward (where Z > 1) and
where we should revise the probability downward (where Z < 1). However,

we should do this set-by-set, rather than w-by-w. The process is described by
the following theorem.

Theorem 1.6.1. Let (il, :F, IP) be a probability space and let Z be an almost
surely nonnegative random variable with IEZ = 1. For A E :F, define



P(A) = Z(w) dlP(w). (1.6.3)
L



Then lP is a probability measure. Furthermore, if X is a nonnegative random
variable, then
EX = IE[X Z]. (1.6.4)
If Z is almost surely strictly positive, we also have



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-52-0.png)

(1.6.5)


fn







=
and limn-+oo IIBn II Boo, we may use the Monotone Convergence Theorem,
Theorem 1.4.5, to write


34 1 General Probability Theory



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-53-0.png)

Putting these two equations together, we obtain the countable additivity prop­
erty

Now suppose JX is a nonnegative random variable. If Ak) = nl��� J(Ak) = �J(Ak)· X is an indicator
function X A then (Q1



Now suppose X is a nonnegative random variable. If X is an indicator
function X A ' then
###### = n



lEX = HA(w) [Z] (w) dlP'(w) lE [HAZ] lE [ [XZ] ],
###### J(A) = l = =



which is (1.6.4). We finish the proof of (1.6.4) using the standard machine
developed in Theorem 1.5.1. When Z > 0 almost surely, is defined and we

                        may replace X in (1.6.4) by to obtain (1.6.5).

            - 0

Definition 1.6.3. Let fl be a nonemyty set and :F a a-algebra of subsets of
fl. Two probability measures lP' and lP' on (fl, :F) are said to be equivalent if
they agr which sets in :F have probability zero.

Under the a umptions of Theorem 1.6.1, including the a umption that
Z - 0 almost surely, lP' and J are equivalent. Suppose A E :F is given and
###### IP'(A) 0. Then the random variable HAZ is lP' almost surely zero, which
implies =
llA(w)Z(w) dlP'(w) 0.
###### J(A) = l =



On the other hand, suppose B E :F satisfies 0. Then 0 almost
###### J(B) surely under so = �nB = J, iE[�nBJ =o.



Equation (1.6.5) implies IP'(B) EHB 0. This shows that lP' and J agree
###### which sets have probability zero. Because the sets with probability one are = =
complements of the sets with prol?._ability zero, lP' and J agree which sets have
probability one as well. Because lP' and lP' are equivalent, we do not need to
specify which measure we have in mind when we say an event occurs almost
surely.
In financial models, we will first set up a sample space which one

[l,
can regard as the set of possible scenarios for the future. We imagine this


1 .6 Change of Measure 35



set of possible scenarios has an actual probability measure JP>. However, for
purposes of pricing derivative securities, we will use a risk-neutral measure [JP] .
We will insist that these two measures are equivalent. They must agree on
what is possible and what is impossible; they may disagree on how probable
the possibilities are. This is the same situation we had in the binomial model;
lP
and [JP ] a igned different probabilities to the stock price paths, but they agreed
which stock paths were possible. In the continuous-time model, after we
have and we shall determine prices of derivative securities that allow us to
lP
set up hedges that work with [JP] -probability one. These hedges then also work
with JP>-probability one. Although we have used the risk-neutral probability to
compute prices, we will have obtained hedges that work with probability one
under the actual (and the risk-neutral) probability measure.
It is common to refer to computations done under the actual measure
as computations in the real world and computations done under the risk­
neutral measure as computations in the risk-neutral world. This unfortunate
terminology raises the question whether prices computed in the "risk-neutral
world" are appropriate for the "real world" in which we live and have our
profits and losses. Our answer to this question is that there is only one world
in the models. There is a single sample space {l representing all possible future
states of the financial markets, and there is a single set of a et prices, modeled
by random variables (i.e., functions of these future states of the market). We
sometimes work in this world a uming that probabilities are given by an
empirically estimated actual probability measure and sometimes a uming
that they are given by risk-neutral probabilities, but we do not change our
view of the world of possibilities. A hedge that works almost surely under one
a umption of probabilities works almost surely under the other a umption
as well, since the probability measures agree which events have probability
one.
The change of measure discussed in Section 3.1 of Volume I is the spe­
cial case of Theorem 1.6.1 for finite probability spaces, and Example 3.1.2 of
Chapter 3 of Volume I provides a case with explicit formulas for JP>, [JP], and Z
when the expectations are sums. We give here two examples on uncountable
probability spaces.
Example 1.6.4. Recall Example 1.2.4 in which {l = [0, 1], lP is the uniform
(i.e., Lebesgue) measure, and



JP[a, b] = 2w dw = b [2 ] - a [2], 0 : a : b : 1. (1.2.2)
### 1 [b ] dw to rewrite (1.2.2) as



We may use the fact that JP>(dw) = dw to rewrite (1.2.2) as



JP[a, b] = 2w dlP(w). (1.2.2)'


Because B[O, 1] is the a-algebra generated by the closed intervals (i.e., begin
with the closed intervals and put in all other sets necessary in order to have a


36 1 General Probability Theory



a-algebra), the validity of (1.2.2)' for all closed intervals [a, b] C [0, 1] implies
its validity for all Borel subsets of [0, 1]:
J(B) = 2w dlP'(w) for every Borel set B c R
L



This is (1.6.3) with Z(w) = 2w.
Note that Z(w) = 2w is strictly positive almost surely (JP{O} = 0), and



fEz = 2w dw = 1.
### 1 [1 ]



According to (1.6.4), for every nonnegative random variable X(w), we have
the equation

[(w) ][= ]
### This suggests the notation 1 [1 ][X(w) dJ] 11 [X(w) ][· ] [2w dw. ]



This suggests the notation



dJ(w) = 2w dw = 2w dlP'(w). (1.6.6)

0



In general, when JP, JP, and Z are related as in Theorem 1.6.1, we may
rewrite the two equations (1.6.4) and (1.6.5) as

X(w) dJ(w) [= ] dlP' [(w)],


Example 1. 6. 6 (Change of measure for a normal random variable). Let X be a
standard normal random variable defined on some probability space (n, .1', JP).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-55-0.png)
1.6 Change of Measure 37



Two ways of constructing X and (!l,F,IP') were described in Example 1.2.6.
For purposes of this example, we do not need to know the details about
the probability space ( !l, F, IP'), except we note that the set !l is necessarily
uncountably infinite and IP'(w) 0 for every w E !l.
When we say X is a standard normal random variable, we mean that
=



J.Lx(B) IP'{X E B} cp(x) dx for every Borel subset B of JR., (1.6.7)
= = L



where
1 .,2
cp(x) -- e - 2
= V2
is the standard normal density. If we take B ( -oo, b], this reduces to the
more familiar condition
=



IP'{X : cp(x)dx for every b E JR (1.6.8)
b} =[boo



In fact, (1.6.8) is equivalent to the apparently stronger statement (1.6.7). Note
that lEX 0 and variance Var(X) lE(X - JEX) [2 ] 1.
Let () = be a constant and define Y = X + (), so that under = IP', the random
variable Y is normal with lEY () and variance Var(Y) JE(Y - JEY) [2 ] 1.
=
Although it is not required by the formulas, we will a ume () is posit2ve for
= = =
the discussion below. We want to change to a new probability measure lP' on !l
under which Y is a standard normal random variable. In other words, we want
EY 0 and Var(Y) 1. We want to do this not by subtracting
() away from Y, but rather by a igning less probability to those w for which
= = E(Y-EY)2 =
Y(w) is sufficiently positive and more probability to those w for which Y(w)
is negative. We want to change the distribution of Y without changing the
random variable Y. In finance, the change from the actual to the risk-neutral
probability measure changes the distribution of a et prices without changing
the a et prices themselves, and this example is a step in understanding that
procedure.
We first define the random variable
exp { -OX (w) - �()2} for all w E !l.
Z(w) =

This random variable has two important properties that allow it to serve as a
Radon-Nikodym derivative for obtaining a probability measure lP equivalent
to IP':
(i) Z(w) > 0 for all w E !l (Z > 0 almost surely would be good enough), and
(ii) lEZ 1.
Property = (i) is obvious because Z is defined as an exponential. Property (ii)
follows from the integration


38 1 General Probability Theory



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-57-0.png)





<










1. 7 Summary 39


We conclude that

which shows th�t Y is a standard normal random variable under the proba­
bility measure IP'.
0

Following Corollary 2.4.6 of Chapter 2 of Volume I, we discussed how
the existence of a risk-neutral measure guarantees that a financial model is
free of arbitrage, the so-called First Fundamental Theorem of Asset Pricing.
The same argument applies in continuous-time models and in fact underlies
the Heath-Jarrow-Morton no-arbitrage condition for term-structure models.
Consequently, we are interested in the existence of risk-neutral measures. As
discussed earlier in this section, these must be equivalent to the actual proba­
bility measure. How can such probability measures iP arise? In Theorem 1.6.1,
we began with the probability measure IP' and an almost surely po�tive ran­
dom variable Z and constructed the equivalent probability IP'. It turns
out that this is the only way to obtain a probability measure IP' equivalent to
IP'. The proof of the following profound theorem is beyond the scope of this
text.

Theorem 1.6. 7 (Radon-Nikodym). Let IP' and iP be equivalent probabil­
ity measures defined on (!?,:F). Then there exists an almost surely positive
random variable Z such that JEZ = 1 and

P(A) = Z(w) dlP'(w) for every A E :F.
l


Summary
1 .7

Probability theory begins with a probability space (!?, :F, IP') (Definition 1.1.2).
Here !? is the set of all possible outcomes of a random experiment, :F is the
collection of subsets of n whose probability is defined, and IP' is a function
mapping :F to [0, 1]. The two axioms of probability spaces are IP'(!?) = 1 and
countable additivity: the probability of a union of disjoint sets is the sum of
the probabilities of the individual sets.
The collection of sets :F in the preceding paragraph is a a-algebra, which
means that belongs to :F, the complement of every set in :F is also in :F, and
0
the union of any sequence of sets in :F is also in :F. The Borel a-algebra in R,
denoted B(R), is the smallest a-algebra that contains all the closed interval



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-58-0.png)
40 1 General Probability Theory

[a, b] in JR. Every set encountered in practice is a Borel set (i.e., belongs to
B(IR) ) .
A random variable X is a mapping from J! to lR (Definition 1.2.1). By def­
inition, it has the property that, for every B E B(IR), the set {w E J!; X(w) E
B} is in the a-algebra F. A random variable X together with the probability
measure lP on J! determines a distribution on JR. This distribution is not the
random variable. Different random variables can have the same distribution,
and the same random variable can have different distributions. We describe
the distribution as a measure J.Lx that a igns to each Borel subset B of lR the
ma J.Lx(B) = JP{X E B} (Definition 1.2.3). If X has a density f(x), then
J.Lx (B) = f(x) dx. If X is a discrete random variable, which means that it
J8
takes one of countably many values x1, x2, . . ., then we define Pi = JP{X = xi}
and have J.Lx(B) = L:{i;x;EB} Pi·
the right-hand side is a Lebesgue integral over The expectation of a random variable X is fl. lEX = Lebesgue integrals are dis­fn X(w) dlP(w), where
cussed in Section 1.3. They differ from Riemann integrals, which form approx­
imating sums to the integral by partitioning the "x" (horizontal)-axis, because
Lebesgue integrals form approximating sums to the integral by partitioning
the ["] y [" ] (vertical)-axis. Lebesgue integrals have the properties one would ex­
pect (Theorem 1.3.4):
Comparison. If X : Y almost surely, then lEX : lEY;
Linearity. lE(aX +,BY) = alEX +,BlEY.
In addition, if cp is a convex function, we have Jensen's inequality: cp(JEX) :
JEep( X).
If the random variable X has a density f ( x), then lEX = x f ( x) dx and,
f�oo
more generally, variable is discrete with lEg(X) = Pi = f�oo lP{X = xg(x)f(x) dx i }, then (Theorem lEg(X) = 1.5.2). L:i g(xi)Pi· If the random
Suppose we have a sequence of random variables X�, X2, X3, . . . converg­
ing almost surely to a random variable X. It is not always true that

lEX = lim lEXn. (1.7.1
n-t )
oo

However, if 0 : X1 : X2 : X3 : . . . almost surely, then (1.7.1) holds
(Monotone Convergence Theorem, Theorem 1.4.5) . Alternatively, if there ex­
ists a random variable Y such that lEY < oo and IXnl ::=; Y almost surely for
every n, then again (1.7.1 ) holds (Dominated Convergence Theorem, Theorem
1.4.9).
We may start with a probability space (J!, F, JP) and change to a different
measure J. Our motivation for considering two measures is that in finance
there is both an actual probability measure and a risk-neutral probability
measure. If lP is a probability measure and Z is a nonnegative random variable
satisfying lEZ = 1, then J defined by
P(A) = Z(w) dlP(w) for all A E F
l


1.9 Exercises 41


also a probability measure (Theorem 1.6.1). If Z is strictly positive almost
is
,surely, the two measures are equivalent: they agree about which sets have
probabili!,y zero. For a random variable X, we have the change-of-expectation
formula JE[X) = lE[X Z]. If Z is strictly positive almost surely, there is a
change-of-expectation formula in the other direction. Namely, if Y is a random
variable, then lEY = i [ � J .


1.8 Notes


Probability theory is usually learned in two stages. In the first stage, one
learns that a discrete random variable has a probability ma function and

a continuous random variable has a density. These can be used to compute
expectations and variances, and even conditional expectations, which are dis­
cussed in Chapter 2. Furthermore, one learns how transformations of contin­
uous random variables change densities. A well-written book that contains all
these things is DeGroot [48).
The second stage of probability theory, which is treated in this chapter,
is measure-theoretic. In this stage, one views a random variable as a function
from a sample space il to the set of real numbers JR. Certain subsets of il
are called events, and the collection of all events forms a a-algebra :F. Each
set A in :F has a probability IP'(A). This point of view handles both discrete
and continuous random variables within the same unifying framework. It is
necessary to adopt this point of view in order to understand the change from
the actual to the risk-neutral measure in finance.
The measure-theoretic view of probability theory was begun by Kol­
mogorov [104). A comprehensive book on measure-theoretic probability is
Billingsley [10). A succinct book on measure-theoretic probability and mar­
tingales is Williams [161). A more detailed book is Chung [35). All of these
are at the level of a Ph.D. course in mathematics.


Exercises
1. 9

Exercise 1.1. Using the properties of Definition 1.1.2 for a probability mea­
sure IP', show the following.
(i) If A E :F, B E :F, and A c B, then IP'(A) � IP'(B).
(ii) If A E :F and { An};:o=l is a sequence of sets in :F with limn-too IP'(An) = 0
and A C An for every n, then IP'(A) = 0. (This property was used implicitly
in Example 1.1.4 when we argued that the sequence of all heads, and
indeed any particular sequence, must have probability zero.)

Exercise 1.2. The infinite coin-toss space il00 of Example 1.1.4 is uncount­
ably infinite. In other words, we cannot list all its elements in a sequence.


42 1 General Probability Theory


To see that this is impossible, suppose there were such a sequential list of all
elements of il00:


                                                                      -                                                                       w [(l) ] [= ] w� [1)] w� [1)] w� [1)] w [�1) ][•],

0 0 0
1 2 3 4 '
W( [3] ) [= ] w1 2 3 [(3)] w [(3)] w [(3)] w4 [(3) ] 0 0 0 '


(i) Show that A is uncountably infinite.
=
(ii) Show that, when 0 < p < 1, we have IP'(A) 0.
Uncountably infinite sets can have any probability between zero and one,
including zero and one. The uncountability of the set does not help determine
its probability.

the formula that IP'(A) Exercise 1.3. Consider the set function = 0 if A is a finite set and IP'(A) lP' defined for every subset of [0, 1) by = oo if A is an infinite
set. Show that lP' satisfies (1.1.3)-(1.1.5), but lP' does not have the countable
additivity property (1.1.2). We see then that the finite additivity property
(1.1.5) does not imply the countable additivity property (1.1.2).

Exercise 1.4. (i) Construct a standard normal random variable Z on the
probability space (il00, :F00, IP') of Example 1.1.4 under the a umption
=
that the probability for head is p �- (Hint: Consider Examples 1.2.5
and 1.2.6.)
(ii) Define a sequence of random variables {Zn}�=1 on il00 such that


=
lim Zn(w) Z(w) for every w E il00
n-+oo

and, for each n, Zn depends only on the first n coin tosses. (This gives
us a procedure for approximating a standard normal random variable by
random variables generated by a finite number of coin tosses, a useful
algorithm for Monte Carlo simulation.)

Exercise 1.5. When dealing with double Lebesgue integrals, just as with
double Riemann integrals, the order of integration can be reversed. The only

=
W(2) w(2)w(2)w(2)w(2)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-61-0.png)
1 .9 Exercises 43



aumption required is that the function being integrated be either nonnega­
tive or integrable. Here is an application of this fact.
Let X be a nonnegative random variable with cumulative distribution
function F(x) = IP'{X - x}. Show that



lEX = (1 - F(x)) dx
### 100



showing that
by
H[o,X(w))(x) dx diP'(w)

is equal to both lEX and J1100 (1 - F(x)) dx.
t



is equal to both lEX and J (1 - F(x)) dx.
t



Exercise 1.6. Let u be a fixed number in JR., and define the convex function
rp [(] x) = eu [x ] for all x E R Let X be a normal random variable with mean
p, = lEX and standard deviation a = [IE( X - [p,)2] ][2] 1 [, ] i.e., with density



i Veri that
( ) fy



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-62-0.png)

(i) What is the function f(x) = limn-+oo fn(x)?
(i) Note that


Explain why this does not violate the Monotone Convergence Theorem,
Theorem 1.4.5.

Exercise 1.8 (Moment-generating function). Let X be a nonnegative
random variable, and a ume that

rp(t) = lEe [tX ]

(ii) What is limn-+oo f�oo fn(x) dx?
fn(x) dx # f(x) dx.
nl�� /_: /_:


44 1 General Probability Theory

is finite for every t E R Assume further that IE [X etX] < oo for every t E
JR The purpose of this exercise is to show that cp' ( t) = IE [X etX] and, in
particular, cp' ( 0) = lEX.
We recall the definition of derivative:


tiable function, then for any two numbers s and t, there is a number () between
s and t such that
f(t) - f(s) = f'(O)(t - s).
If we fix w E {l and define f(t) = etX( [w] ), then this becomes

e [tX(w) ] [_ ] e [sX(w) ] = (t _ s)X(w)e8(w)X(w), (1.9.1)

where O(w) is a number depending on w (i.e., a random variable lying between
t and s).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-63-0.png)

(i) Use the Dominated Convergence Theorem (Theorem 1.4.9) and equation
(1.9.1) to show that



lim IEYn = IE lim Yn = IE (X e [tx] ] .
n-too n-too

[ ]
This establishes the desired formula cp'(t) = IE [Xet [x] ] .



(1.9.2)



(ii) Suppose the random variable X can take both positive and negative values
and IEet [x ] < oo and E [!X!etX] < oo for every t E R Show that once again



cp [' ] ( t) = E (X et [x] ] . (Hint: Use the notation ( 1.3.1) to write X = x [+] -x-.)



Exercise 1.9. Suppose X is a random variable on some probability space
(il, .1', IP'), A is a set in .1', and for every Borel subset B of JR., we have
l!B(X(w)) diP'(w) = IP'(A) · IP'{X E B}. (1.9.3)
i


1.9 Exercises 45



Then we say that X is independent of the event A.
Show that if X is independent of an event A, then

g(X(w)) dlP'(w) = JP>(A) · lEg(X)
i

for every nonnegative, Borel-measurable function g.



Exercise 1.10. Let JP> be the uniform (Lebesgue) measure on fl = [0, 1). De­
fine
###### Z(w) = [{][ 0 ][�][f] [�] [::; ][w ][< ] [�' ]

2 If 2 ::; w ::; l.



For A E B[O, 1), define



JPi(A) = Z(w) dlP'(w).
i



(i) Show that JPi is a probability measure.
(ii) Show that if JP>(A) = 0, then JPi(A) = 0. We say that JP> is absolutely
continuous with respect to JP>.
(i) Show t!_:at there is a set A for which JPi(A) = 0 but JP>(A) - 0. In other
words, JP> and JP> are not equivalent.

Exercise 1.11. In Example 1.6.6, we began with a standard normal random
variable X under a measure JP>. According to Exercise 1.6, this random variable
has the moment-generating function

lEeu [X ] = e!u [2 ] for all u E R

The moment-generating function of a random variable determines its distribu­
tion. In particular, any random variable that has moment-generating function
du [2 ] must be standard normal.
In Example 1.6.6, we also defined Y = X + 0, where 0 is a constant, we
set Z = e-8 [X-] !8 [2], and we defined JPi by the formula (1.6.9):



JPi(A) = Z(w) dlP'(w) for all A E :F.
i



We showed by considering its cumulative distribution function that Y is a
standard normal random variable under JPi. Give another proof that Y is stan­
dard normal under JPi by verifying the moment-generating function formula



Exercise 1.12. In Example 1.6.6, we began with a standard normal random
variable X on a probability space (fl, F, JP>) and defined the random variable
Y = X + 0, where 0 is a constant. We also defined Z = e [-] 8 [X-] !8 [2 ] and used Z

as the Radon-Nikodym derivative to construct the probability measure JPi by
the formula (1.6.9):


46 1 General Probability Theory



JP(A) = Z(w) dP(w) for all A E :F.
L



Under J, the random variable Y was shown to be standard normal.
We now have a standard normal random variable Y on the probability
space (il, :F, [JP] ), and X is related to Y by X = Y - 6. By what we have
just stated, with X replaced by Y and 6 replaced by -6, we could define
z = e9 [Y-] �9 [2 ] and then use [Z ] as a Radon-Nikodym derivative to construct a
probability measure iP by the formula



P(A) = Z(w) dlP(w) for all A E :F,
L



so that, under iP, the random variable X is standard normal. Show that [Z ] = !
and iP = JP.

Exercise 1.13 (Change of measure for a normal random variable). A
nonrigorous but informative derivation of the formula for the Radon-Nikodym
derivative Z(w) in Example 1.6.6 is provided by this exercise. As in that
example, let X be a standard normal random variable on some probability
space ( n, :F, JP), and let Y = X + 6. Our goal is to define a strictly positive
random variable Z(w) so that when we set



JP(A) = Z(w) dP(w) for all A E :F, (1.9.4)
L



the random variable Y under lP is standard normal. If we fix w E n and choose
a set A that contains w and is "small," then (1.9.4) gives
JP(A) � Z(w)JP(A),

where the symbol - means "is approximately equal to." Dividing by JP(A),
we see that
JP(A)

              JP(A)                  - Z(w)

for "small" sets A containing w. We use this observation to identify Z(w).
With w fixed, let x = X(w). For f > 0, we define B(x, f) = [x   - �, x + �]
to be the closed interval centered at x and having length f. Let y = x + 6 and
B(y, f) = [y - �, y + �] .
(i) Show that


(ii) In order for Y to be a standard normal random variable under [JP], show
that we must have
1 - 1 Y [2] (w)
--JP{Y f E B(y, f)} [�] -� exp -{ 2 } .

JP{X E B(x, exp .
{
        - f)} �



for "small" sets A containing w. We use this observation to identify Z(w).
With w fixed, let x = X(w). For f > 0, we define B(x, f) = [x   - �, x + �]
to be the closed interval centered at x and having length f. Let y = x + 6 and
B(y, f) = [y - �, y + �] .
(i) Show that
JP{X E B(x, exp .
{
        - f)} �


1 . 9 Exercises 4 7

(iii) Show that {X E B(x, €)} and {Y E B(y, €) } are the same set, which we
call A(w, €) . This set contains w and is "small" when €   - 0 is small.
(iv) Show that
--iPW(A) (A)                              - exp { -OX(w) - -0 2 1 2} .

The right-hand side is the value we obtained for Z(w) in Example 1.6.6.
Exercise 1.14 (Change of measure for an exponential random vari­
able). Let X be a nonnegative random variable defined on a probability space
(fl, :F, P) with the exponential distribution, which is
W{X :S a} = 1 - e [-] >- [a], a 2 0,
where >. is a positive constant. Let A be another positive constant, and define


                 -                  Z -- e (X .>.)X .

            - [A ]



Define W by



P(A) = Z diP for all A E :F.
i



(i) Show that iP(n) = 1.
(ii) Compute the cumulative distribution function
P{X ::; a} for a 2 0



for the random variable X under the probability measure W.
Exercise 1.15 (Provided by Alexander Ng). Let X be a random variable
on a probability space (n, :F, W), and a ume X has a density function f(x)
that is positive for every x E JR. Let g be a strictly increasing, differentiable
function satisfying
lim g(y) = -oo, lim g(y) = oo,
y-+ [- oo ] y-+ [oo ]
and define the random variable Y = g(X).
Let h(y) be an arbitrary nonnegative function satisfying f h(y) dy = 1.
�oo
We want to change the probability measure so that h(y) is the density function
for the random variable Y. To do this, we define
h(g(X))g'(X)
z [= ] .
f(X)

(i) Show that Z is nonnegative and lEZ = 1.
Now define iP by
P(A) = Z diP for all A E :F.
i

(ii) Show that Y has density h under iP.


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-67-0.png)
2


Information and Conditioning


Information and u-algebras
2.1

The no-arbitrage theory of derivative security pricing is based on contingency
plans. In order to price a derivative security, we determine the initial wealth
we would need to set up a hedge of a short position in the derivative security.
The hedge must speci what position we will take in the underlying security
fy
at each future time contingent on how the uncertainty between the present
time and that future time is resolved. In order to make these contingency
plans, we need a way to mathematically model the information on which our
future decisions can be based. In the binomial model, that information was
knowledge of the coin tosses between the initial time and the future time. For
the continuous-time model, we need to develop somewhat more sophisticated
machinery to capture this concept of information.
We imagine as always that some random experiment is performed, and the
outcome is a particular w in the set of all possible outcomes fl. We might then
be given some information-not enough to know the precise value of w but
enough to narrow down the possibilities. For example, the true w might be
the result of three coin tosses, and we are told only the first one. Or perhaps
we are told the stock price at time two without being told any of the coin
tosses. In such a situation, although we do not know the true w precisely, we

can make a list of sets that are sure to contain it and other sets that are sure
not to contain it. These are the sets that are resolved by the information.
Indeed, suppose fl is the set of eight possible outcomes of three coin tosses.
we are told the outcome of the first coin toss only, the sets
If

AH = {HHH, HHT, HTH, HTT}, Ar = {THH,THT, TTH, TTT}
(2.1.1)
are resolved. For each of these sets, once we are told the first coin toss, we
know if the true w is a member. The empty set and the whole space fl are
0
always resolved, even without any information; the true w does not belong to
and does belong to fl. The four sets that are resolved by the first coin toss
0


50 2 Information and Conditioning


form the a-algebra
:Fi = {0, .!1, AH, AT}·
We shall think of this a-algebra as containing the information learned by
observing the first coin toss. More precisely, if instead of being told the first
coin toss, we are told, for each set in :Fi, whether or not the true w belongs
to the set, we know the outcome of the first coin toss and nothing more.
If we are told the first two coin tosses, we obtain a finer resolution. In
particular, the four sets

AHH = {HHH, HHT}, AHT = {HTH, HTT}, (2.1.2)
ATH = {THH, THT}, ATT = {TTH, TTT},

are resolved. Of course, the sets in :F1 are still resolved. Whenever a set is
resolved, so is its complement, which means that Al:rH, Al:rT, ArH' and ArT
are resolved. Whenever two sets are resolved, so is their union, which means
that AHH UATH, AHH UATT, AHTUATH, and AHTUATT are resolved. We
have already noted that the two other pairwise unions, AH = AH H U AHT
and AT = ATH U ATT, are resolved. The triple unions are also resolved, and
these are the complements already mentioned, e.g.,



In all, we have 16 resolved sets that together form a a-algebra we call :F2; i.e.,



:F2



16 resolved sets that together form a a-algebra we call


                                                                                                                                
AHH U ATH, AHH U ATT, AHT U ATH, AHT U ATT
_
0, .n, AH, AT, AHH, AHT, ATH, ATT, Al:rH, Al:rT, ArH' ArT'
###### { }



AHH U ATH, AHH U ATT, AHT U ATH, AHT U ATT     
(2.1.3)
We shall think of this a-algebra as containing the information learned by
observing the first two coin tosses.
If we are told all three coin tosses, we know the true w and every subset
of .!1 is resolved. There are 256 subsets of .!1 and, taken all together, they
constitute the a-algebra Fa:

:Fa = The set of all subsets of .!1.

If we are told nothing about the coin tosses, the only resolved sets are 0
and .!1. We form the so-called trivial a-field :Fo with these two sets:

:Fo = {0, .!1}.

We have then four a-algebras, :Fo, :F1, :F2, and Fa, indexed by time. As
time moves forward, we obtain finer resolution. In other words, if n m, then
<
:Fm contains every set in :Fn and even more. This means that :Fm contains
more information than :Fn. The collection of a-algebras :Fo, :Fll :F2, :Fa is

example of filtmtion. We give the continuous-time formulation of this
an a
situation in the following definition.


2. 1 Information and a algebras 51

Definition 2.1.1. Let [} be a nonempty set. Let T be a fixed positive number,
and assume that for each t E [0, T] there is a a-algebm :F(t). Assume further
that if s : t, then every set in :F(s) is also in :F(t). Then we call the collection
of a -algebms :F( t), 0 : t : T, a filtration.
A filtration tells us the information we will have at future times. More
precisely, when we get to time t, we will know for each set in :F(t) whether
the true w lies in that set.
Example 2. 1.2. Suppose our sample space is [} = Co[O, T], the set of continu­
ous functions defined on [0, T] taking the value zero at time zero. Suppose one
of these functions w is chosen at random and we get to observe it up to time

t, where 0 : t : T. That is to say, we know the value of w(s) for 0 : s : t,
but we do not know the value of w( s) for t < s : T. Certain subsets of [} are
resolved. For example, the set { w E n; maxo�s::;t w( s) : 1} is resolved. We
would put this in the a-algebra :F(t). Other subsets of [} are not resolved by
time t. For example, if t < T, the set {w E n; w(T) - 0} is not resolved by
time t. Indeed, the sets that are resolved by time t are just those sets that
can be described in terms of the path of w up to time t. [1 ] Every reasonable [2 ]
subset of [} = Co[O, T] is resolved by time T. By contrast, at time zero we see
only the value of w(O), which is equal to zero by the definition of n. We learn
nothing about the outcome of the random experiment of choosing w by ob­
serving this. The only sets resolved at time zero are 0 and [}, and consequently
:F(o) = {0, n} . Example 2.1.2 provides the simplest setting in which we may construct a
Brownian motion. It remains only to a ign probability to the sets in :F =
:F(T), and then the paths w E C0[0, T] will be the paths of the Brownian
motion.
The discussion preceding Definition 2.1.1 suggests that the a-algebras in
a filtration can be built by taking unions and complements of certain funda­
mental sets in the way F2 was constructed from the four sets AHH, AHr,
ArH, and Arr· If this were the case, it would be enough to work with these
so-called atoms (indivisible sets in the a-algebra) and not consider all the
other sets. In uncountable sample spaces, however, there are sets that cannot
be constructed as countable unions of atoms (and uncountable unions are for­
bidden because we cannot add up probabilities of such unions). For example,
let us fix t E (0, T) in Example 2.1.2. Now choose a continuous function f(u),
defined only for 0 : : t and satisfying f(O) = 0. The set of continuous
u
functions w E C0[0, T] that agree with f on [0, t] and that are free to take any
values on (t, T] form an atom in :Ft. In symbols, this atom is
1 For technical reasons, we would not include in .F(t) sets such as {w E

il; maxo�s::;t w(s) E B} if B is a subset of lR that is not Borel measurable. This
technical issue can safely be ignored.
2
Once again, there are pathological sets such as {w E n; w(T) E B}, where B is
a subset of lR that is not Borel measurable. These are not included in .F(T), but
that shall not concern us.


52 2 Information and Conditioning

{w E Co[O, T]; w(u) = f(u) for all u E [0, t]}.

Each time we choose a new function f(u), defined for 0 � u � t, we get a new
atom. However, there is no way to obtain the important set {w E il;w(t) > 0}
by taking countable unions of these atoms. Moreover, it is usually the case
that the atoms have zero probability. Consequently, in what follows we work
with all the sets of :F(t), especially those with positive probability, not with
just the atoms.
Besides observing the evolution of an economy over time, which is the idea
behind Example 2.1.2, there is a second way we might acquire information
about the value of w. Let X be a random variable. We a ume throughout
that there is a "formula" for X, and we know this formula even before the
random experiment is performed. Because we already know this formula, we
are waiting only to learn the value of w to substitute into the formula so we
can evaluate X(w). But suppose that rather than being told the value of w
we are told only the value of X(w). This resolves certain sets. For example,
if we know the value of X(w), then we know if w is in the set {X � 1} (yes
if X(w) 1 and no if X(w) - 1). Indeed, every set of the form {X E B},

     where B is a subset of IR, is resolved. Again, for technical reasons, we restrict
attention to subsets B that are Borel measurable.
Definition 2.1.3. Let X be a random variable defined on a nonempty sample
space il. The a-algebra generated by X, denoted a(X), is the collection of all
subsets of il of the form {X E B}, [3 ] where B ranges over the Borel subsets of
JR.
Example 2.1.4. We return to the three-period model of Example 1.2.1 of Chap­
ter 1. In that model, il is the set of eight possible outcomes of three coin tosses,
and
S2(HHH) = S2(HHT) = 16,
S2(HTH) = S2(HTT) = S2(THH) = S2(THT) = 4,
S2(TTH) = S2(TTT) = 1.

In Example 1.2.2 of Chapter 1, we wrote 82 as a function of the first two coin
tosses alone, but now we include the irrelevant third toss in the argument to
get the full picture. If we take B to be the set containing the single number 16,
then {S2 E B} = {HHH, HHT} = AHH, where we are using the notation
of (2.1.2). It follows that AHH belongs to the a-algebra a(S2). Similarly, we
can take B to contain the single number 4 and conclude that AHr U ArH
belongs to a(S2), and we can take B to contain the single number 1 to see
that Arr belongs to a(S2) . Taking B = 0, we obtain 0. Taking B = IR, we
obtain n. Taking B = [4, 16], we obtain the set AHH u AHT u ArH· In short,
as B ranges over the Borel subsets of IR, we will obtain the list of sets
We recall that {X E B} is shorthand notation for the subset {w E !t; X(w) E B}
3 of n.


2.2 Independence 53


and all unions and complements of these. This is the a-algebra a(82).
Every set in a(82) is in the a-algebra F2 of (2.1.3), the information con­
tained in the first two coin tosses. On the other hand, AHr and ArH appear
separately in F2 and only their union appears in a(82). This is because seeing
the first two coin tosses allows us to distinguish an initial head followed by

a tail from an initial tail followed by a head, but knowing only the value of
82 does not permit this. There is enough information in F2 to determine the
value of 82 and even more. We say that 82 is F2-measumble. D

Definition 2.1.5. Let X be a mndom variable defined on a nonempty sample
space n. Let g be a a-algebm of subsets of n. If every set in a( X) is also in
g, we say that X is g-measurable.

A random variable X is g-measurable if and only if the information in g
is sufficient to determine the value of X. If X is g-measurable, then f(X) is
also g-measurable for any Borel-measurable function f; if the information in
g is sufficient to determine the value of X, it will also determine the value of
f(X). If X and Y are g-measurable, then f(X, Y) is g-measurable for any
Borel-measurable function f(x, y) of two variables. In particular, X + Y and
XY are g-measurable.
A portfolio position Ll(t) taken at time t must be F(t)-measurable (i.e.,
must depend only on information available to the investor at time t). We
revisit a concept first encountered in Definition 2.4.1 of Chapter 2 of Volume
I.

Definition 2.1.6. Let [} be a nonempty sample space equipped with a filtm­
tion F(t), 0 : t : T. Let X(t) be a collection of mndom variables indexed by
t E [0, T]. We say this collection of mndom variables is an adapted stochastic
process if, for each t, the mndom variable X(t) is F(t)-measumble.
In the continuous-time models of this text, a et prices, portfolio processes
(i.e., positions), and wealth processes (i.e., values of portfolio processes) will
a be adapted to a filtration that we regard as a model of the flow of public
information.


Independence
2.2

When a random variable is measurable with respect to a a-algebra g, the
information contained in g is sufficient to determine the value of the random
variable. The other extreme is when a random variable is independent of a
u-algebra. In this case, the information contained in the a-algebra gives no
clue about the value of the random variable. Independence is the subject of
the present section. In the more common case, when we have a a-algebra g
and a random variable X that is neither measurable with respect to g nor


54 2 Information and Conditioning


independent of g, the information in g is not sufficient to evaluate X, but we
can estimate X based on the information in g. We take up this case in the
next section.
In contrast to the concept of measurability, we need a probability mea­
sure in order to talk about independence. Consequently, independence can be
affected by changes of probability measure; measurability is not.
Let (il, .1', JP) be a probability space. We say that two sets A and B in .1'
are independent if
JP(A n B) = JP(A) · lP(B).
For example, in il = { H H, HT, T H, TT} with 0 � p � 1, q = 1 - p, and

JP(HH) = p [2], JP(HT) = pq, JP(TH) = pq, JP(TT) = q [2],

the sets
A = {head on first toss} = { H H, HT}
and
B = {head on the second toss} = { H H, T H}
are independent. Indeed,

JP(A n B) = JP(HH) = p [2 ] and JP(A)JP(B) = (p [2 ] + pq)(p [2 ] + pq) [= ] p [2. ]

Independence of sets A and B means that knowing that the outcome w of a
random experiment is in A does not change our estimation of the probability
that it is in B. If we know the first toss results in head, we still have probability
p for a head on the second toss.
In a similar way, we want to define independence of two random variables
X and Y to mean that if w occurs and we know the value of X(w) (without
actually knowing w), then our estimation of the distribution of Y is the same
as when we did not know the value of X(w). The formal definitions are the
following.
Definition 2.2.1. Let (il, .1', JP) be a probability space, and let g and 1i be
sub-u-algebras of .1' {i.e., the sets in g and the sets in 1i are also in .1' ). We
say these two a-algebras are independent if
JP(A n B) = JP(A) · lP(B) for all A E Q, B E 11..
Let X and Y be random variables on (il, .1', JP). We say these two random
variables are independent if the a-algebras they generate, a(X) and a(Y),
are independent. We say that the random variable X is independent of the
a-algebra g if a( X) and g are independent.
Recall that a( X) is the collection of all sets of the form {X E C}, where C
ranges over the Borel subsets of JR Similarly, every set in a(Y) is of the form
{Y E D}. Definition 2.2.1 says that X and Y are independent if and only if
JP{X E C and Y E D} = lP{X E C} · lP{Y E D}
for all Borel subsets C and D of R


2.2 Independence 55

Example 2.2.2. Recall the space {l of three independent coin tosses on which
the stock price random variables of Figure 1.2.2 of Chapter 1 are constructed.
Let the probability measure IP' be given by
IP'(HHH) = p [3], IP'(HHT) = p [2] q, IP'(HTH) = p [2] q, IP'(HTT) = pq [2],
IP'(THH) = p [2] q, IP'(THT) = pq [2], IP'(TTH) = pq [2], IP'(TTT) = q [3] .

Intuitively, the random variables s2 and s3 are not independent because if we
know that s2 takes the value 16, then we know that s3 is either 8 or 32 and
is not 2 or .50. To formalize this, we consider the sets {S3 = 32} = {HHH}
and {S2 = 16} = {HHH, HHT}, whose probabilities are IP'{S3 = 32} = p [3 ]
and IP'{ S2 = 16} = p [2] . In order to have independence, we must have

IP'{S2 = 16 and S3 = 32} = IP'{S2 = 16} · IP'{S3 = 32} = p [5] .

But IP'{ S2 = 16 and S3 = 32} = IP'{ H H H} = p [3], so independence requires

p = 1 or p = 0. Indeed, if p = 1, then after learning that S2 = 16, we do not
revise our estimate of the distribution of S3; we already knew it would be 32.
If p = 0, then S2 cannot be 16, and we do not have to worry about revising
our estimate of the distribution of S3 if this occurs because it will not occur.
As the previous discussion shows, in the interesting cases of 0 < p < 1,
the random variables S2 and S3 are not independent. However, the random
variables S2 and are independent. Intuitively, this is because S2 depends
t
on the first two tosses, and depends on the third toss only. The a-algebra
t
generated by s2 comprises 0, n3, the atoms (fundamental sets)

{S2 = 16} = {HHH, HHT},
{S2 = 4} = {HTH, HTT, THH, THT},
{S2 = 1} = {TTH, TTT},

and their unions. The a-algebra generated by comprises 0, il3, and the
t
atoms


= 2 = {HHH, HTH, THH, TTH},
}
s3 1
= {HHT, HTT,THT, TTT}.
###### { S2 [= ] [2" ] }

To verify independence, we can conduct a series of checks of the form


IP' S2 = 16 and = 2 = IP'{S2 = 16} · IP' = 2 .
} { }
###### {

The left-hand side of this equality is

IP' S2 = 16 and = 2} = IP'{HHH} = p [3],
{


56 2 Information and Conditioning


and the right-hand side is





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-75-0.png)







Note that gk is different from Fk in Example 1.1.4 of Chapter 1, the a-algebra
a ociated with the first k tosses. Under the probability measure constructed
in Example 1.1.4 of Chapter 1, the full sequence of a-algebras g1, g2, g3, . . .
is independent. Now recall the sequence of the random variables of (1.2.8) of
Chapter 1:
Yk(w) =
{ 0 lf Wk = [1 ][�][f wk = ] T. [H, ]
The full sequence of random variables Y1, Y2, Y3, . . . is likewise independent.
0


2.2 Independence 57


The definition of independence of random variables, which was given in
terms of independence of a-algebras that they generate, is a strong condition
that is conceptually useful but difficult to check in practice. We illustrate the
first point with the following theorem and thereafter give a second theorem
that simplifies the verification that two random variables are independent.
Although this and the next section treat only the case of a pair of random
variables, there are analogues of these results for n random variables.

Theorem 2.2.5. Let X andY be independent mndom variables, and let f and
g be Borel-measumble functions on JR Then f(X) and g(Y) are independent
mndom variables.

PROOF: Let A be in the a-algebra generated by f(X). This a-algebra is a
sub-a-algebra of a(X). To see this, recall that, by definition, every set A in
a(f(X)) is of the form {w E fl; f(X(w)) E C}, where C is a Borel subset of
R We define D = {x E JR.; f(x) E C} and then have

A = {w E fl; f(X(w)) E C} = {w E fl, X(w) E D}. (2.2.1)

The set on the right-hand side of (2.2.1) is in a(X), so A E a(X).
Let B be in the a-algebra generated by g(Y). This a-algebra is a sub­
a-algebra of a(Y), so B E a(Y). Since X and Y are independent, we have
IP'(A n B) = IP'(A) · IP'(B). 0

Definition 2.2.6. Let X and Y be mndom variables. The pair of mndom
variables (X, Y) takes values in the plane IR. [2], and the joint distribution mea­
sure of (X, Y) is given by4

t-tx,y(C) = IP'{(X, Y) E C} for all Borel sets C [C ] [IR.2]     - (2.2.2)
This is a probability measure (i.e., a way of assigning measure between 0 and
1 to subsets of IR. [2 ] so that /-tX,Y (IR. [2] ) = and the countable additivity property
is satisfied}. The joint cumulative distribution function of 1 (X, Y) is

(2.2.3)
We say that a nonnegative, Borel-measumble function fx,y(x, y) is a joint
density for the pair of mndom variables (X, Y) if
Fx,y(a, b) = t-tx,y ((-oo, a] x (-oo, bl) = IP'{X �a, Y � b}, a E IR., b E JR



t-tx,Y(C) = Hc(x, y)fx,y(x, y) dydx for all Borel sets C [c ] JR. [2] .
(2.2.4)
I:
### I: [2 ]



4 One way to generate the u-algebra of Borel subsets of R [2 ] is to start with the
collection of closed rectangles (ar, br] x (a2, b2] and then add all other sets necessary
in order to have a u-algebra. Any set in this resulting u-algebra is called a Borel
subset of R [2]  - All subsets of R [2 ] normally encountered belong to this u-algebra.


58 2 Information and Conditioning



Condition (2.2.4) holds if and only if



Fx,Y(a, b) = (2.2.5)
oo [fx,v(x, y) dydx ][for all ][a E ][JR, ][b E ][JR. ]
###### /_� /_ [b]



The distribution measures (generally called the marginal distribution mea­
sures in this context) of X and Y are



J.Lx(A) = JP{X E A} J.Lx,v(A x JR) for all Borel subsets A C JR,
J.Ly(B) = lP{Y E B} J.Lx,v(JR x B) for all Borel subsets B C R

The {marginal) cumulative distribution functions are

Fx(a) = J.Lx(-oo, a] JP{X �a} for all a E JR,
Fy(b) = J.Ly(-oo, b] JP{Y � b} for all b E JR.



If the joint density fx,Y exists, then the marginal densities exist and are given
by
fx(x) = fx,v(x, y) dy and fy(y) = fx,v(x, y) dx.
###### /_: /_:

The marginal densities, if they exist, are nonnegative, Borel-measurable func­
tions that satisfy



J.Lx(A) = fx(x) dx for all Borel subsets A C JR,
i



J.LY (B) = Jy (y) dy for all Borel subsets B c JR.
L



These last conditions hold if and only if



Fx(a) = fx(x) dx for all a E JR,
###### /_�



Fy(b) =
oo [Jy(y) dy ][for all ][b E ][JR. ]
###### /_ [b]



(2.2.6)


(2.2.7)



Theorem 2.2. 7. Let X and Y be random variables. The following conditions
are equivalent.
{i} X and Y are independent.
{ii} The joint distribution measure factors:

J.Lx,v(A x B) = J.Lx(A) · J.Lv(B) for all Borel subsets A C JR, B C R
(2.2.8)
{iii} The joint cumulative distribution function factors:

Fx,v(a, b) = Fx(a) · Fv(b) for all a E JR, b E JR. (2.2.9)


2.2 Independence 59
(iv) The joint moment-generating function factors:



IEeu [X +vY ] [= ] IEeu [X . ] lEe [vY ]



(2.2.10)



for all u E IR, v E lR for which the expectations are finite.



If there is a joint density, each of the conditions above is equivalent to the
following.
(v) The joint density factors:

=
fx,y(x, y) fx(x) · Jy(y) for almost every x E IR, y E JR. (2.2.11)
The conditions above imply but are not equivalent to the following.



(2.2.11)



{vi} The expectation factors:


=
IE[XY] lEX · lEY,
provided IEIXYI < oo.



(2.2.12)



OUTLINE OF PROOF: We sketch the various steps that constitute the proof
of this theorem.
(i)=?(ii) Assume that X and Y are independent. Then

JLx,y(A x B) = IP'{X E A and Y E B}
= IP'({X E A} n {Y E B})
= IP'{X E A} · IP'{Y E B}
= JLx(A) · JLy(B).

(ii)=?(i) A typical set in a(X) is of the form {X E A}, and a typical set in
a(Y) is of the form {Y E B}. Assume (ii). Then

IP'({X E A} n {Y E B}) = IP'{X E A and Y E B}
= JLX,Y(A X B)
= JLx(A) · JLy(B)
= IP'{X E A} · IP'{Y E B}.

This shows that every set in a(X) is independent of every set in a(Y).
(ii)=?(iii) Assume (2.2.8). Then

Fx,y(a, b) = JLx,Y ((-oo, a] x (-oo, bl)
= JLx(-oo, a] · JLy(-oo, b]
= Fx(a) · Fy(b).

(iii)=?(ii) Equation (2.2.9) implies that (2.2.8) holds whenever A is of the
=
form A = ( -oo, a] and B is of the form B ( -oo, b]. This is enough to


60 2 Information and Conditioning



establish (2.2.8) for all Borel sets and B, but the details of this are beyond
A
the scope of the text.
(iii)=?(v) If there is a joint density, then (iii) implies


Differentiating first with respect to a and then with respect to b, we obtain

Jx,y(x, y) dydx fx(x) dx Jy(y) dy.
### = /_� · �� /_�/_boo



Differentiating first with respect to a and then with respect to b, we obtain



!x,y(a, b) !x(a) Jy(b),
### with different dummy variables. = ·



which is just (2.2.11) with different dummy variables.
(v)=?(iii) Assume there is a joint density. If we also a ume (2.2.11), we can
integrate both sides to get



Fx,y(a, b) Jx,y(x, y) dydx
### =/_�/_ [b] oo fx(x) Jy(y) dydx =/_�/_ [b] ·
fx(x) dx oo Jy(y) dy
Fx(a) Fy(b).
### = /_� ·/_ [b] oo = ·



(i)=?(iv) We first use the "standard machine" as in the proof of Theorem
1.5.1 of Chapter 1, starting with the case when h is the indicator function of
a Borel subset of JR. [2], to show that, for every real-valued, Borel-measurable
function h(x, y) on IR. [2], we have



lEih(X, Y)l ih(x, y)i dJ.Lx,y(x, y),
and if this quantity is finite, then =



(2.2.13)


X and Y, whether or not they

lEh(X, Y) h(x, y) dJ.Lx,y(x, y).
### =



This is true for any pair of random variables X and Y, whether or not they
are independent. If X and Y are independent, then the joint distribution J.Lx, y
is a product of marginal distributions, and this permits us to rewrite (2.2.13)
as
lEh(X, Y) h(x, y) dJ.Ly(y) dJ.Lx(x). (2.2.14)
###### /_:

We now fix numbers and = and take /_: h(x, y) eu [x] +vy. Equation (2.2.14)



We now numbers and and take h(x, y) eu [x] +vy. Equation 2.2.14)
fix u v (
reduces to
### =


2.2 Independence 61



eu [x ] dJ-Lx(x) · e [vy ] dJ-Ly(y)
###### /_: /_:
### = IEeu [X . ] lEe [vY] '

where we have used Theorem 1.5.1 of Chapter 1 for the last step. The proof
### =
(iv)=?(i) is beyond the scope of this text.
(i)=?(vi) In the special case when h(x, y) xy, (2.2.14) reduces to
### IE[XY] xdJ-Lx(x) · = ydJ-Ly(y) = lEX · lEY,

where again we have used Theorem = /_: 1.5.1 /_: of Chapter 1 for the last step.
0
Example 2.2.8 {Independent normal random variables). Random variables X
and Y are independent and standard normal if they have the joint density

lEeuX+vY eux+vy dJ-Ly(y) dJ-Lx(x)
### = /_: i:



IE[XY] xdJ-Lx(x) · ydJ-Ly(y) = lEX · lEY,
### = /_: 1.5.1 /_: of Chapter 1



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-80-0.png)



(2.2.15)



for the standard normal cumulative distribution function. The joint cumula­
tive distribution function for (X, Y) factors:



Fx,y(a, b) fx(x)Jy(y) dydx
### =/_�/_ [b]
fx(x) dx oo Jy(y) dy
###### /_�
N(a) · N(b).
### = ·/_ [b] oo

J-Lx is the probability measure on JR
### =



The joint distribution J-Lx is the probability measure on JR [2 ] that a igns a
measure to each Borel set C C JR [2 ] equal to the integral of Jx,y(x, y) over C.
If C = A x B, where A E B(IR) and B E B(IR), then J-Lx,Y factors:



J-Lx,y(A x B) fx(x)Jy(y) dydx
i l
### = fx(x) dx · Jy(y) dy = J-Lx(A) i · J-Ly(B). l 0 =


62 2 Information and Conditioning


We give an example to show that property (vi) of Theorem 2.2.7 does not
imply independence. We precede this with a definition.

Definition 2.2.9. Let X be a random variable whose expected value is defined.
The variance of X, denoted Var(X), is


=
Var(X) lE [(X - JEX) [2] ) .


expectations shows that


= =
If p(X, Y) 0 (or equivalently, Cov(X, Y) 0}, we say that X and Y are
uncorrelated.

Property (vi) of Theorem 2.2.7 implies that independent random variables
are uncorrelated. The converse is not true, even for normal random variables,
although it is true of jointly normal random variables (see Definition 2.2.11
below).
Example 2.2. 10 (Uncorrelated, dependent normal random variables). Let X
be a standard normal random variable and let Z be independent of X and
satisfy [5 ]

5 To construct such random variables, we can choose {} = {(w1, w2); 0 :S w1 :S
1, 0 :S w2 1} to be the unit square and choose to be the two-dimensional
:S JP>
Lebesgue measure according to which is equal to the area of for every
JP>(A) A
Borel subset of G. We then set X(w1, w2) = N-1 (wt ), which is a standard normal
random variable under see Example 1.2.6 for a discussion of this probability
JP> (
integral transform . We set Z(w1, w2) to be  - 1 if 0 w2 :S and to be 1 if
) :S                  
  - < W2 :S 1.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-81-0.png)
2.2 Independence 63
1 1
IP'{Z = 1} =           - and IP'{Z = -1} = -. (2.2.16}
2 2

Define Y = ZX. We show below that, like X, the random variable Y is
standard normal. FUrthermore, X and Y are uncorrelated, but they are not
independent. The pair (X, Y) does not have a joint density.
Let us first determine the distribution of Y. We compute

Fy(b) = IP'{Y :S b}
= IP'{Y : b and Z = 1} + IP'{Y ::; b and Z = -1}
= IP'{X ::; b and Z = 1} + IP'{ -X :S b and Z = -1}.

Because X and Z are independent, we have

IP'{X : b and Z = 1} + IP'{ -X : b and Z = -1}
= IP'{Z = 1} · IP'{X :S b} + IP'{Z = -1} · IP'{ -X :S b}
1 1
=       - IP'{X :S b} +       - IP'{ -X ::; b}.
2 2

Because X is a standard normal random variable, so is -X. Therefore, IP'{X :
b} = IP'{ -X : b} = N(b). It follows that Fy(b) = N(b); in other words, Y is
a standard normal random variable.
Since lEX = lEY = 0, the covariance of X and Y is

Cov(X, Y) = JE[XY] = lE ZX [2] ] .
(

Because Z and X are independent, so are Z and X [2], and we may use Theorem
2.2.7(vi) to write


Therefore, X and Y are uncorrelated.
The random variables X and Y cannot be independent for if they were,
then lXI and IYI would also be independent (Theorem 2.2.5). But lXI = IYI·
In particular,

IP'{IXI : 1, IYI : 1} = IP'{IXI : 1} = N(1) - N( -1),

and
IP'{IXI : 1} · IP'{IYI : 1} = (N(1) - N(-1)) [2] .
These two expressions are not equal, as they would be for independent random
variables.
Finally, we want to examine the joint distribution measure of (X, Y).
/LX,Y
Since lXI = IYI, the pair (X, Y) takes values only in the set

C [= ] {(x, y); x = ±y}.


64 2 Information and Conditioning


In other words, J-Lx,Y(C) = 1 and J-Lx.Y(Cc) = 0. But C has zero area. It
follows that for any nonnegative function f, we must have


One way of thinking about this is to observe that if we want to integrate a
function ITc(x, y)f(x, y) over the plane JR. [2], we could first fix x and integrate
out the y-variable, but since f(x, y)ITc(x, y) is zero except when y = x and
y = -x, we will get zero. When we next integrate out the x-variable, we will
be integrating the zero function, and the end result will be zero. There cannot
be a joint density for Y) because with this choice of the set C, the left­
(X,
hand side of (2.2.4) is one but the right-hand side is zero. Of course, and
X
Y have marginal densities because they are both standard normal. Moreover,
the joint cumulative distribution function exists (as it always does). In this
case, it is

ITc(x, y)f(x, y) dy dx = 0.
###### /_: i:



Fx, y (a, b)



= IP'{X ::; a and Y ::; b}



= IP'{X ::; a, X ::; b, and Z = 1} + IP'{X ::; a, -X ::; b, and Z = -1}



= IP'{ Z = 1} · IP'{ X ::; min( a, b)} + IP'{ Z = -1} · IP'{ -b ::; X ::; a}
1 . 1
= 2N(mm(a, b)) + 2 max{N(a) - N(-b), O}.



There is no joint density fx, y (x, y) that permits us to write this function in
the form (2.2.5).
0

Definition 2.2.11. Two mndom variables X and Y are said to be jointly
normal if they have the joint density



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-83-0.png)



. .                                                 In equation {2.2.18}, x = (x17, Xn) is a row vector of dummy variables,
J-L = (J-LI, . . ., J-tn) is the row vector of expectations, and C is the positive definite
matrix of covariances.


2.2 Independence 65



In the case of (2.2.17), X is normal with expectation J.L1 and variance 17f,
Y is normal with expectation f2 and variance 17�, and the correlation between
X and Y is p. The density factors (equivalently, X and Y are independent)
if and only if p = 0. In the case (2.2.18), the density factors into the product
of normal densities (equivalently, the components of are independent) if
n X
and only if C is a diagonal matrix (all the covariances are zero).
Linear combinations of jointly normal random variables (i.e., sums of con­
stants times the random variables) are jointly normal. Since independent nor­
mal random variables are jointly normal, a general method for creating jointly
normal random variables is to begin with a set of independent normal random
variables and take linear combinations. Conversely, any set of jointly normal
random variables can be reduced to linear combinations of independent nor­
mal random variables. We do this reduction for a pair of correlated normal
random variables in Example 2.2.12 below.
Since the distribution of jointly normal random variables is characterized in
terms of means and covariances, and joint normality is preserved under linear
combinations, it is not necessary to deal directly with the density when making
linear changes of variables. The following example illustrates this point.
Example 2.2.12. Let (X, Y) be jointly normal with the density (2.2.17). Define
W = Y - £X. Then X and W are independent. To verify this, it suffices to
show that,., X and W have covariance zero since they are jointly normal. We
compute
Cov(X, W) = lE[(X - lEX)(W - JEW)]



=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-84-0.png)

175 = lE[(W - JEW) [2] ]



= (1 - p [2] )17�.



of a pair of independent normal random variables X and W. D


66 2 Information and Conditioning


2.3 General Conditional Expectations


We consider a random variable X defined on a probability space (il, F, IP')
and a sub-a-algebra g of F. If X is g-measurable, then the information in g
is sufficient to determine the value of X. If X is independent of g, then the
information in g provides no help in determining the value of X. In the inter­
mediate case, we can use the information in g to estimate but not precisely
evaluate X. The conditional expectation of X given g is such an estimate.
We have already discussed conditional expectations in the binomial model.
Let il be the set of all possible outcomes of N coin tosses, and a ume these
coin tosses are independent with probability p for head and probability q =
1 - p for tail on each toss. Let IP'(w) denote the probability of a sequence of
coin tosses under these a umptions. Let n be an integer, 1 � n � N - 1, and
let X be a random variable. Then the conditional expectation of X under IP',
based on the information at time n, is (see Definition 2.3.1 of Chapter 2)



lEn [X)(w1 . . . [W] n)

p# [H] (wn+I···wN)q#T(wn+l···wN)X(w 1       - . . W n n+ lW       - . . W N) .
Wn+l···WN

In the special cases n = 0 and n = N, we define

lEoX = L P [#H(wo ... wN)] q [#T(wo ... wN)] X [(wo ] . . . wN) = lEX,
wo ... wN



(2.3.1)


(2.3.2)



(2.3.3)
In (2.3.2), we have the estimate of X based on no information, and in (2.3.3)
we have the estimate based on full information.
We need to generalize (2.3.1)-(2.3.3) in a way suitable for a continuous­
time model. Toward that end, we examine (2.3.1) within the context of a
three-period example. Consider the general three-period model of Figure 2.3.1.
We a ume the probability of head on each toss is p and the probability of
tail is q = 1 - p, and we compute



lE2[S3)(HH) = pS3(HHH) + qS3(HHT),
lE2[S3](HT) = pS3(HTH) + qS3(HTT),
lE2[S3)(TH) = pS3(THH) + qS3(THT),
lE2[S3)(TT) = pS3(TTH) + qS3(TTT).



(2.3.4)
(2.3.5)
(2.3.6)
(2.3.7)



Recall the a-algebra F2 of (2.1.3), which is built up from the four fundamental
sets (we call them atoms because they are indivisible within the a-algebra)
AHH, AHr, ArH, and Arr of (2.1.2) . We multiply (2.3.4) by IP'(AHH) = p [2],
multiply (2.3.5) by IP'(AHr) = pq, multiply (2.3.6) by IP'(ArH) = pq, and
multiply (2.3.7) by IP'(Arr) = q [2] . The resulting equations may be written as


2.3 General Conditional Expectations 67
Ss(HHH) = u3So


(2.3.8)


(2.3.10)


E2[S3](TT)IP'(Arr) = L S3(w)IP'(w). (2.3.11)

wEATT

We could divide each of these equations by the probability of the atom appear­
ing as the second factor on the left-hand sides and thereby recover the formulas
{2.3.4)-(2.3. 7) for the conditional expectations. However, in the continuous­
time model, atoms typically have probability zero, and such a step cannot be
performed. We therefore take an alternate route here to lay the groundwork
for the continuous-time model.
On each of the atoms of :F2, the conditional expectation IE2[S3] is con­
stant because the conditional expectation does not depend on the third
toss and the atom is created by holding the first two tosses fixed. It fol­
lows that the left-hand sides of (2.3.8)-(2.3.11) may be written as integrals
of the integrand IE2[S3] over the atom. For this purpose, we shall write
lE2[S3](w) = IE2[S3)(w1w2w3), including the third toss in the argument, even
though it is irrelevant. The right-hand sides of these equations are sums, which
are Lebesgue integrals on a finite probability space. Using Lebesgue integral
notation, we rewrite (2.3.8)-(2.3.11) as



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-86-0.png)
68 2 Information and Conditioning



(2.3.12)


(2.3.13)


(2.3.14)


(2.3.15)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-87-0.png)

(2.3.16)


for every set A E :F2, except possibly for A = 0. However, if A = 0, equa­
tion (2.3.16) still holds, with both sides equal to zero. We call (2.3.16) the
partial-avemging property of conditional expectations because it says that the
conditional expectation and the random variable being estimated give the
same value when averaged over "parts" of Jl (those "parts" that are sets in
the conditioning a-algebra :F2).
We take (2.3.16) as the defining property of conditional expectations. The
precise definition is the following.

Definition 2.3.1. Let (il, :F, IP') be a probability space, let g be a sub-a-algebm
of :F, and let X be a mndom variable that is either nonnegative or integmble.
The conditional expectation of X given 9, denoted JE[XI9), is any mndom
variable that satisfies
{i) (Measurability) JE[XI9] is 9-measumble, and
{ii) (Partial averaging)

lE[XjQ](w) dlP'(w) = X(w) dlP'(w) for all A E Q. (2.3.17)
i i

If g is the a-algebm genemted by some other mndom variable W (i.e., g =
a(W)), we genemlly write JE[XIW] mther than JE[Xja(W)].


2.3 General Conditional Expectations 69



Property (i) in Definition 2.3.1 guarantees that, although the estimate of
based on the information in g is itself a random variable, the value of the
X
estimate JE[XIg] can be determined from the information in g. Property (i)
captures the fact that the estimate lE[XIg] of X is based on the information in
g. Note in (2.3.4)-(2.3. 7) that the conditional expectation lE2[S3] is constant
on the atoms of F2; this is property (i) for this case.
The second property ensures that JE[XIg] is indeed an estimate of X. It
gives the same averages as X over all the sets in g. If g has many sets,
which provide a fine resolution of the uncertainty inherent in w, then this
partial-averaging property over the "small" sets in g says that lE[XIg] is a
good estimator of X. If g has only a few sets, this partial-averaging property
guarantees only that JE[XIg] is a crude estimate of X.
Definition 2.3.1 raises two immediate questions. First, does there always
exist a random variable lE[XIg] satisfying properties (i) and (ii)? Second, if
there is a random variable satisfying these properties, is it unique? The answer
to the first question is yes, and the proof of the existence of JE[XIg] is based on
the Radon-Nikodym Theorem, Theorem 1.6.7 (see Appendix B). The answer
to the second question is a qualified yes, as we now explain. Suppose Y and
Z both satisfy conditions (i) and (ii) of Definition 2.3.1. Because both Y
and Z are g-measurable, their difference Y - Z is as well, and thus the set
A = {Y - Z > 0} is in g. From (2.3.17), we have

Y(w) dlP(w) = X(w) dlP(w) = Z(w) dlP(w),
L L L



and thus
(Y(w) - Z(w)) dlP(w) = 0.
L



The integrand is strictly positive on the set A, so the only way this equation
can hold is for A to have probability zero (i.e., Y Z almost surely). We
:
can reverse the roles of Y and Z in this argument and conclude that Z Y
:
almost surely. Hence Y = Z almost surely. This means that although differ­
ent procedures might result in different random variables when determining
E[XIg], these different random variables will agree almost surely. The set of

w for which the random variables are different has zero probability.
In this more general context, conditional expectations still have the five
fundamental properties developed in Theorem 2.3.2 of Chapter 2 of Volume
I. We restate them in the present context.

Theorem 2.3.2. Let (il, F, IP) be a probability space and let g be a sub-a­
algebra of F.
{i) (Linearity of conditional expectations) If X and Y are integrable
random variables and c1 and c2 are constants, then

(2.3.18)


70 2 Information and Conditioning


This equation also holds if we assume that X and Y are nonnegative
(mther than integmble) and c1 and c2 are positive, although both sides
may be +oo.
{ii} (Taking out what is known) If X and Y are integmble mndom vari­
ables, Y and XY are integmble, and X is g-measumble, then

IE[XYig] = XIE[Yigj. (2.3.19)

This equation also holds if we assume that X is positive and Y is nonneg­
ative (mther than integmble}, although both sides may be +oo.
(iii} (Iterated conditioning) If 1l is a sub-a algebm of g (1£ contains less
information than g) and X is an integmble mndom variable, then

IE[IE[XIgJI1l] = IE[XI1l) . (2.3.20)

This equation also holds if we assume that X is nonnegative {mther than
integmble}, although both sides may be +oo.
(iv) (Independence) If X is integmble and independent of g, then

IE[XIg] = lEX. (2.3.21)

This equation also holds if we assume that X is nonnegative (mther than
integmble}, although both sides may be +oo.
{v} (Conditional Jensen's inequality) If cp(x) is a convex function of a
dummy variable x and X is integmble, then

IE[cp(X)Ig) 2 cp(E[XIgl). (2.3.22)

DISCUSSION AND SKETCH OF PROOF: We take each of these properties in
turn.
(i) Linearity allows us to separate the estimation of random variables into
estimation of separate pieces and then add the estimates of the pieces to
estimate the whole. To verify that IE[c1X + c2Yigj is given by the right­
hand side of (2.3.18), we observe that the right-hand side is g-measurable
because IE[XIg] and IE[Yig] are g-measurable and then must check the partial­
averaging property (ii) of Definition 2.3.1. Using the fact that E[XIg] and
E[Yig] themselves satisfy the partial-averaging property, we have for every
A E g that

(cl!E[XIg](w) + c21E[Yigj(w)} dlP'(w)
i



= c1 IE[XIg](w) dlP'(w) + c2 IE[Yig](w) dlP'(w)
i i



= c1 X(w) dlP'(w) + c2 Y(w) dlP'(w)
i i



= (c1X(w) + c2Y(w)) dlP'(w),
i


2.3 General Conditional Expectations 71



which shows that c1lE(XIg] + c2lE[Yjg] satisfies the partial-averaging property
that characterizes JE(c1X + c2Yig] and hence is JE[c1X + c2Yig].
(ii) Taking out what is known permits us to remove X from the estimation
problem if its value can be determined from the information in g. To estimate
XY, it suffices to estimate Y alone and then multiply the estimate by X. To
prove (2.3.19), we observe first that XlE(Yigj is g-measurable because both X
and JE(Yig] are g-measurable. We must check the partial-averaging property.
Let us first consider the case when X is a g-measurable indicator random
variable (i.e., X = HB, where B is a set in g). Using the fact that JE(Yjg] itself
satisfies the partial-averaging property, we have for every set A E g that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-90-0.png)



= X(w)Y(w) dlP'(w). (2.3.23)



Having proved (2.3.23) for g-measurable indicator random variables X, we
may use the standard machine developed in the proof of Theorem 1.5.1 of
Chapter 1 to obtain this equation for all g-measurable random variables X
for which XY is integrable. This shows that XlE[Yjg] satisfies the partial­
averaging condition that characterizes lE[XYjg], and hence XJE(Yjg] is the
conditional expectation lE[XYjg].
(iii) If we estimate X based on the information in g and then estimate the
estimate based on the smaller amount of information in H., we obtain the
random variable we would have gotten by estimating X directly based on
the smaller amount of information in H To prove this, we observe first that
lE(Xj'H.] is H.-measurable by definition. The partial-averaging property that
characterizes lE lE(Xjg] H. is

[ j )
lE [lE[Xjg] jH.] (w) dlP'(w) = JE(Xjg](w) IP'(w) for all A E H
i i

In order to prove (2.3.20), we must show that we can replace lE [lE[Xjg] jH.) on
the left-hand side of this equation by JE[XI'H.]. But when A E H., it is also in
and the partial-averaging properties for JE(Xj'H.] and JE[Xjg] imply
g,
lE[Xj'H.](w) dlP'(w) = X(w) dlP'(w) = JE[Xjg](w) dlP'(w).
i i i

This shows that lE(XI'H.] satisfies the partial-averaging property that charac­
terizes lE lE(Xjg] 'H., and hence JE[Xj'H.] is lE lE(Xjg] H. .

[ j ) [ j )
(iv) If X is independent of the information in g, then the best estimate we can
give of X is its expected value. This is also the estimate we would give based
on no information. To prove this, we observe first that lEX is g-measurable.


72 2 Information and Conditioning


Indeed, lEX is not random and so is measurable with respect to every a­
algebra. We need to verify that lEX satisfies the partial-averaging property
that characterizes IE[XIQ]; i.e.,

lEX dlP(w) = X(w) dlP(w) for all A E Q. (2.3.24)
i i

Let us consider first the case when X is an indicator random variable indepen­
dent of Q (i.e., X = where the set B is independent of Q). For all A E Q,
HB,
we have then

X(w) dlP(w) = JP>(A n B) = JP>(A) · JP>(B) = JP>(A)IEX = lEX dlP(w),
i i

and (2.3.24) holds. We complete the proof using the standard machine devel­
oped in the proof of Theorem 1.5.1 of Chapter 1.
(v) Using the linearity of conditional expectations, we can repeat the proof
of Theorem 2.2.5 of Chapter 2 to prove the conditional Jensen's inequality.
0

We note that IE[XIQ] is an unbiased estimator of X:


IE(IE[XIQ]) = lEX. (2.3.25)

This equality is just the partial-averaging property ( 2.3.17) with A = il.

Example 2. 3. 3. Let X and Y be a pair of jointly normal random variables
with joint density (2.2.17). As in Example 2.2.12, define W = Y - £<Tt X so
that X and W are independent and (2.2.19) holds:

(2.2.19)

In Example 2.2.12, we saw that W is normal with mean J.LJ = J.L2 - - <Tt
and variance a� = (1 - p [2] )a�. Let us take the conditioning a-algebra to be
g = a(X). (When g is generated by a random variable X, it is customary to
write IE[· · · IX] rather than IE[· · · la(X)].) We estimate Y, based on X, using
(2.2.19) above and properties (i) (Linearity) and (iv) (Independence) from
Theorem 2.3.2 to get the linear regre ion equation
p [a] 2 p [a] 2
IE[YIX] = -X + lEW = -(X -a1 a1 J.LI) + J.L2· (2.3.26)

Note that the right-hand side of (2.3.26) is random but is a(X)-measurable
(i.e., if we know the information in a(X), which is the same as knowing the
value of X, then we can evaluate IE[YIX]). Subtracting (2.3.26) from (2.2.19),
we see that the error made by the estimator is


=
Y - IE[YIX] W - lEW


2.3 General Conditional Expectations 73



The error is random, with expected value zero (the estimator is unbiased), and
is independent of the estimate IE[YIX] (because IE[YIX] is a(X)-measurable
and W is independent of a(X)). The independence between the error and the
conditioning random variable X is a consequence of the joint normality in
the example. In general, the error and the conditioning random variable are
uncorrelated, but not nece arily independent; see Exercise 2.8.
0
The Independence Lemma, Lemma 2.5.3 of Chapter 2 of Volume I, now
takes the following more general form.
Lemma 2.3.4 (Independence). Let (!l, :F, IP') be a probability space, and
let g be a sub-a-algebra of :F. Suppose the random variables X1, . . ., XK are
Q-measurable and the random variables Y�, . . ., YL are independent of g. Let
f(x�, . . ., XK, y�, . . ., YL) be a function of the dummy variables x1, . . ., XK and


(2.3.27)
Then

(2.3.28)

0 0 0
xb


Y 7;
g(x1, .           - ., xK ) = 1Ef(x1, •           -           -, xK, Y�, . . ., YL).

. . ., YL, and define
Yl l



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-92-0.png)






74 2 Information and Conditioning


Then
lE[f(X, Y) !XJ = 9(X).
Our final answer is random but a(X)-measurable, as it should be.
0

We have all the tools required to introduce martingales and Markov pro­
cesses in a continuous-time framework. The definitions are provided below.
Examples will be given after we construct Brownian motion and Ito integrals
in the next chapters.

Definition 2.3.5. Let ( Jl, F, IP') be a probability space, let T be a fixed positive
number, and let F(t), 0 : t : T, be a filtration of sub-a-algebras of F.
Consider an adapted stochastic process M ( t), 0 : t : T.
(i} If
JE[M(t)IF(s)] = M(s) for all 0 : s : t : T,
we say this process is a martingale. It has no tendency to rise or fall.
(ii} If
JE[M(t)IF(s)] 2: M(s) for all 0 : s : t : T,
we say this process is a submartingale. It has no tendency to fall; it may
have a tendency to rise.
(iii} If
JE[M(t)IF(s)] : M(s) for all 0 : s : t : T,
we say this process is a supermartingale. It has no tendency to rise; it
may have a tendency to fall.

Definition 2.3.6. Let (Jl, F, IP') be a probability space, let T be a fixed positive
number, and let F(t), 0 : t : T, be a filtration of sub-a-algebras of F.
Consider an adapted stochastic process X(t), 0 : t : T. Assume that for all
0 : s : t : T and for every nonnegative, Borel-measurable function f, there
is another Borel-measurable function 9 such that

lE[f(X(t))IF(s)] = 9(X(s)). (2.3.29)

Then we say that the X is a Markov process.
Remark 2.3. 7. In Definition 2.3.6, the function f is permitted to depend on
t, and the function g will depend on s. These dependencies are not indicated
in (2.3.29) because we wish there to emphasize how the dependence on the
sample point w works (i.e., the right-hand side depends on w only through
the random variable X ( s)). If we indicate the dependence on time by writing
f(t, x) rather than f(x), we can write f(s, x) rather than 9(x) (we do not need
different symbols f and 9 because the time variables t and s indicate we are
dealing with different functions of x at the different times) and can rewrite
(2.3.29) as


2.4 Summary 75


lE[f(t, X(t))IF(s)] = f(s, X(s)), 0 � s � t � T. (2.3.30)

Ultimately, we shall see that when we regard f(t, x) as a function of two
variables this way, (2.3.30) implies that it satisfies a partial differential equa­
tion. This partial differential equation gives us a way to determine f(s, x) if
we know f(t, x). The Black-Scholes-Merton partial differential equation is a
special case of this. 0


2.4 Summary


In measure-theoretic probability, information is modeled using a-algebras. The
information a ociated with a a-algebra g can be thought of as follows. A
random experiment is performed and an outcome w is determined, but the
value of w is not revealed. Instead, for each set in the a-algebra g, we are told
whether w is in the set. The more sets there are on g, the more information this
provides. If g is the trivial a-algebra containing only 0 and n, this provides
no information.
A random variable X is g-measurable if and only if the set {X E B} =
{w E fl; X(w) E B} is in g for every Borel subset of R In this case, the
information in g is enough to determine the value of the random variable
X(w), even though it may not be enough to determine the value w of the
outcome of the random experiment.
At the other extreme, the information in a a-algebra g may be irrelevant
to the determination of the value of X. In this case, we say that g and X are
independent. This idea is captured mathematically by Definition 2.2.3, which
says that X and g are independent if, for every set A E g and every Borel
subset B of IR, we have

JP{w E fl;w E A and X(w) E B} = lP(A) · lP{w E fl; X(w) E B}.

Two random variables X and Y are independent if and only if the a algebra
generated by X, defined to be the collection of sets of the form {X E B}, is
independent of the a-algebra generated by Y. In other words, X and Y are
independent if and only if

lP{X E B and Y E C} = JP{X E B} · lP{X E C} for all B E B(IR), C E B(IR),

where B(IR) denotes the a-algebra of Borel subsets of R There are several
equivalent ways to describe independence between two random variables hav­
ing to do with factoring the joint cumulative distribution function, factoring
the joint moment-generating function, and factoring the joint density (if there
is a joint density). These are set out in Theorem 2.2.7. Independence implies
uncorrelatedness, but uncorrelated random variables do not need to be in­
dependent. Jointly normally distributed random variables (Definition 2.2.11)
are uncorrelated if and only if tl>ey are independent, but normally distributed
random variables do not need to be jointly normal.


76 2 Information and Conditioning


Often we find ourselves between the two extremes of random variables X
that are g-measurable and random variables X that are independent of g. In
such a case, the information in g is relevant to the determination of the value
of X but is not sufficient to completely determine it. We then want to use the
information in g to estimate X. We denote our estimate by JE[XIg] and call
this the conditional expectation of X given g. This is itself a random variable,
but one that is g-measurable (i.e., one that we can evaluate using only the
information in g). To be sure this is a good estimate of X, we require that it
satisfy the partial-averaging property (see Definition 2.3.1(ii)):

lE[XIg](w) dlP'(w) = X(w) dlP'(w) for every A E g.
L L

Conditional expectations behave in many ways like expectations, except that
expectations do not depend on w and conditional expectations do. The princi­
pal properties of conditional expectations are provided in Theorem 2.3.2, and
these are reported briefly here.
Linearity: JE[c1X + c2Yigl = c1lE[XIg] + c2lE[Yig].
Taking out what is known: lE[XYig] = XJE[Yig] if X is g-measurable.
Iterated conditioning: lE lE[XIgJ 1l] = JE[XI1l] if 1l is a sub-a-algebra of

[ I
g.
Independence: JE[XIg] = lEX if X is independent of g.
Jensen's inequality: JE[cp(X)Ig] ; cp(lE[XIg]) if cp is convex.
In continuous-time finance, we work within the framework of a probabil­
ity space (!l, :F, IP'). We normally have a fixed final time T and then have a
filtration, which is a collection of a-algebras {:F(t); 0 � t � T} indexed by the
time variable t. We interpret :F(t) as the information available at time t. For
0 � s � t � T, every set in :F(s) is also in :F(t). In other words, information
increases over time. Within this context, an adapted stochastic process is a
collection of random variables {X ( t); 0 � t � T} also indexed by time such
that, for every t, X(t) is :F(t)-measurable; the information at time t is suffi­
cient to evaluate the random variable X(t). We think of X(t) as the price of
some a et at time t and :F(t) as the information obtained by watching all the
prices in the market up to time t.
Two important cla es of adapted stochastic processes are martingales and
Markov processes. These are defined in Definitions 2.3.5 and 2.3.6, respectively.
A martingale has the property that

JE[M(t)I:F(s)] = M(s) for all 0 � s � t � T.

If JE[M(t) I:F(s)] ; M(s) when 0 � s � t � T, we have a submartingale. If the
inequality is reversed, we have a supermartingale. A Markov process has the
property that whenever 0 � s � t � T and we are given a function f, there is
another function g such that

lE[f(X(t))I:F(s)] = g(X(s)).


:.!.o t;xerc1ses 77

The i [mportant feature here is that the estimate of ][f][(][X][(][t][)) ][made at time ] [s ]
dep [ends only on the process value X(s) at time s and not on the path of the ]
process before time s.
A useful tool for establishing that a process is Markov is the Independence
Lemma, Lemma 2.3.4. The simplest version of this says that if X is a Q­
measurable random variable and Y is independent of Q, then

lE[f(X, Y)IQ] = g(X),

where g(x) = lEf(x, Y).


Notes
2.5

In the measure-theoretic view of probability theory, a conditional expectation
is itself a random variable, measurable with respect to the conditioning a­
algebra. This point of view is indispensable for treating the rather complicated
conditional expectations that arise in martingale theory. It was invented by
Kolmogorov [104]. The term martingale was apparently first used by Ville

[158], who a igned the name to a betting strategy. The concept dates back to
1934 work of Levy. The first systematic treatment of martingales was provided
by Doob [53].


Exercises
2.6

Exercise 2.1. Let ( !l, F, IP') be a general probability space, and suppose a
random variable X on this space is measurable with respect to the trivial
a-algebra Fo = {0, !l}. Show that X is not random (i.e., there is a constant c
such that X (w) = c for all w E !l). Such a random variable is called degenemte.

Exercise 2.2. Independence of random variables can be affected by changes
of measure. To illustrate this point, consider the space of two coin tosses
!!2 = { H H, HT, T H, TT}, and let stock prices be given by

So = 4, S1(H) = 8, S1(T) = 2,
S2(HH) = 16, S2(HT) = S2(TH) = 4, S2(TT) = 1.

Consider two probability measures given by



JP(HH) = i, lP(HT) = i, lP(TH) = i, lP(TT) = i [, ]
IP'(HH) = IP'(HT) = IP'(TH) = IP'(TT) = �·
�' �. �'



Define the random variable


###### X = [{ ][1 if ][82 = ][4, ]

0 if 82 -1- 4.


78 2 Information and Conditioning


(i) List all the sets in a(X).
(ii) List all the sets in a(SI).
(iii) how that a( X) and a(S1) are independent under the probability measure

  IP'.
(iv) Show that a(X) and a(SI) are not independent under the probability
measure IP'.
(v) Under IP', we have IP'{S1 = 8} = and IP'{S1 = 2} = - Explain intuitively
                  -                   why, if you are told that X = 1, you would want to revise your estimate
of the distribution of sl.

Exercise 2.3 (Rotating the axes). Let X and Y be independent standard
normal random variables. Let () be a constant, and define random variables

V = X cos() + Y sin() and W = -X sin() + Y cos().

Show that V and W are independent standard normal random variables.

Exercise 2.4. In Example 2.2.8, X is a standard normal random variable and
Z is an independent random variable satisfying

1
IP'{Z = 1} = IP'{Z = -1} = -2 '
We defined Y = X Z and showed that Y is standard normal. We established
that although X and Y are uncorrelated, they are not independent. In this
exercise, we use moment-generating functions to show that Y is standard
normal and and Y are not independent.
X
(i) Establish the joint moment-generating function formula


not independent.


function


Show that X and Y are standard normal random variables and that they are
uncorrelated but not independent.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-97-0.png)
2.6 Exercises 79


Exercise 2.6. Consider a probability space fl with four elements, which we
call a, b, c, and d (i.e., fl = {a, b, c, d} ). The a-algebra :F is the collection of
all subsets of fl; i.e., the sets in :F are


n, {a, b, c}, {a, b, d}, {a, c, d}, {b, c, d},
{a, b}, {a, c}, {a, d}, {b, c}, {b, d}, {c, d},
{a}, {b}, {c}, {d}, 0.

We define a probability measure lP' by specifying that

1 1 1 1
IP'{a} = 6' IP'{b} = 3' IP'{c} = 4' IP'{d} = 4'

and, as usual, the probability of every other set in :F is the sum of the prob­
abilities of the elements in the set, e.g., IP'{ a, b, c} = IP'{ a} + IP'{b} + IP'{ c} =
�.
We next define two random variables, and Y, by the formulas
X

X(a) = 1, X(b) = 1, X(c) = -1, X(d) = -1,
Y(a) = 1, Y(b) = -1, Y(c) = 1, Y(d) = -1.

We then define Z = X + Y.
(i) List the sets in a(X).
(ii) Determine IE[YIX] (i.e., specify the values of this random variable for a,
b, c, and d). Verify that the partial-averaging property is satisfied.
(iii) Determine IE[ZIX]. Again, verify the partial-averaging property.
(iv) Compute IE[ZIX] - IE[YIX]. Citing the appropriate properties of condi­
tional expectation from Theorem 2.3.2, explain why you get X.

Exercise 2.7. Let Y be an integrable random variable on a probability space
(fl, :F, IP') and let g be a sub-a-algebra of F. Based on the information in Q,
we can form the estimate IE[YIQ] of Y and define the error of the estimation
Err = Y - IE[YIQ]. This is a random variable with expectation zero and some
variance Var(Err). Let X be some other Q-measurable random variable, which
we can regard as another estimate of Y. Show that

Var(Err) � Var(Y - X).

other words, the estimate IE[YIQ] minimizes the variance of the error among
In
a estimates based on the information in Q. (Hint: Let = IE(Y -X). Compute
the variance of Y - X as
J.L



IE [(Y - X - = IE [ ((Y - IE[YIQ]) + (IE[YIQ] - X J.L)2) J.L))2] .



Multiply out the right-hand side and use iterated conditioning to show the
cross-term is zero.)


80 2 Information and Conditioning


Exercise 2.8. Let X and Y be integrable random variables on a probability
space (n, :F, IP'). Then Y = Y1 + Y2, where Y1 = IE[YIX] is a(X)-measurable
and Y2 = Y - E[YIX]. Show that Y2 and X are uncorrelated. More generally,
show that Y2 is uncorrelated with every a(X)-measurable random variable.

Exercise 2.9. Let X be a random variable.
(i) Give an example of a probability space (n, :F, IP'), a random variable X
defined on this probability space, and a function f so that the a-algebra
generated by f(X) is not the trivial a-algebra {0, n} but is strictly smaller
than the a-algebra generated by X.
(ii) Can the a-algebra generated by f(X) ever be strictly larger than the
a-algebra generated by X?



Exercise 2.10. Let X and Y be random variables (on some unspecified prob­
ability space (n, :F, IP')), a ume they have a joint density Jx,y(x, y), and as­
sume IEIYI oo. In particular, for every Borel subset C of IR. [2], we have
<



IP'{ (X, Y) E C} = fx,y(x, y) dx dy.
fc



In elementary probability, one learns to compute IE[YIX = x], which is a
nonrandom function of the dummy variable x, by the formula



IE[YIX = x] = YfYIX(Yix)dy,
1:



(2.6.1)



is the conditional density defined by



In measure-theoretic probability, conditional expectation is a random vari­
able IE[YIX]. This exercise is to show that when there is a joint density for
(X, Y), this random variable can be obtained by substituting the random vari­
able X in place of the dummy variable x in the function g(x). In other words,
this exercise is to show that

IE[YIX] = g(X) .

(We introduced the symbol g(x) in order to avoid the mathematically confus­
ing expression E[YIX = X].)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-99-0.png)
2.6 Exercises 81



Since g(X) is obviously a(X)-measurable, to verify that IE[YIX] = g(X),



we need only check that the partial-averaging property is satisfied. For every
Borel-measurable function h mapping to and satisfying 1Eih(X)I oo, we
lR lR <
have
IEh(X) = h(x)fx(x)dx. (2.6.2)
###### /_:

This is Theorem 1.5.2 in Chapter 1. Similarly, if h is a function of both x and

y, then
lEh(X, Y) = h(x, y)Jx,y (x, y)dxdy (2.6.3)
###### /_: /_:

whenever (X, Y) has a joint density Jx,y(x, y). You may use both (2.6.2) and
(2.6.3) in your solution to this problem.
Let A be a set in a(X). By the definition of a( X), there is a Borel subset
of such that A = {w E n; X(w) E B} or, more simply, A = {X E B}.
B lR
Show the partial-averaging property
y [diP'. ]

Exercise 2.11. (i) Let X be a random variable on a probability space i [g(X)diP' ][= ] i



Exercise 2.11. (i) Let X be a random variable on a probability space
(n, :F, IP'), and let W be a nonnegative a(X)-measurable random variable.
Show there exists a function g such that W = g(X). (Hint: Recall that
every set in a(X) is of the form {X E B} for some Borel set B C R Sup­
pose first that W is the indicator of such a set, and then use the standard
machine.)
(ii) Let X be a random variable on a probability space (il, :F, IP'), and let Y be
a nonnegative random variable on this space. We do not a ume that X
and Y have a joint density. Nonetheless, show there is a function g such
that IE[YIX] = g(X).


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-101-0.png)
3


Brownian Motion


3.1 Introduction


In this chapter, we define Brownian motion and develop its basic properties.
The definition of Brownian motion is provided in Section 3.3. Section 3.2
precedes it to give some intuition. For us, the most important properties of
Brownian motion are that it is a martingale (Theorem 3.3.4) and that it
accumulates quadratic variation at rate one per unit time (Theorem 3.4.3).
The notion of quadratic variation is profound. It makes stochastic calculus
different from ordinary calculus. For this reason, we begin already in Section
3.2 to talk about it.
Sections 3.5-3. 7 develop properties of Brownian motion we shall need later
but not in the development of stochastic calculus in Chapter 4. Therefore,
the reader can go to Chapter 4 after completing Section 3.4. The Markov
property is the concept used to relate stochastic calculus to partial differential
equations. For Brownian motion, this property is presented in Section 3.5. The
first pa age time of Brownian motion to a level is presented in Section 3.6
and used in Chapter 8 to analyze a perpetual American put on a geometric
Brownian motion. This is in the spirit of the perpetual American put analysis
for the binomial model, which is given in Section 5.4 of Volume I. The reflection
principle for Brownian motion developed in Section 3. 7 is used in Chapter 7
to price exotic options.


3.2 Scaled Random Walks


3.2.1 Symmetric Random Walk


To create a Brownian motion, we begin with a symmetric random walk, one
path of which is shown in Figure 3.2.1. To construct a symmetric random
walk, we repeatedly toss a fair coin (p, the probability of H on each toss, and
q = 1 - p, the probability of T on each toss, are both equal to We denote
�).


84 3 Brownian Motion



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-103-0.png)









(3.2.1)


(3.2.2)



are independent. Each of these random variables,
ki+l
Mki+l            - Mk, = L Xj, (3.2.3)
j=k;+l

is called an increment of the random walk. It is the change in the position of
the random walk between times ki and ki+l· Increments over nonoverlapping
time intervals are independent because they depend on different coin tosses.


3.2 Scaled Random Walks 85

Moreover, each increment Mki+t - Mk, has expected value 0 and variance
ki+t - ki. It is easy to see that the expected value is zero because the expected
value of each Xj appearing on the right-hand side of (3.2.3) is zero. We also
have Var(Xj) = lEXJ = 1, and since the different Xj are independent, we
have from (3.2.3) that
ki+l ki+l
Var(Mk,+t   - Mk.) = L Var(Xj) = L 1 = ki+l   - ki. (3.2.4)


The variance of the symmetric random walk accumulates at rate one per unit
time, so that the variance of the increment over any time interval k to for
f
nonnegative integers k is k.
< f f             

3.2.3 Martingale Property for the Symmetric Random Walk


To see that the symmetric random walk is a martingale, we choose nonnegative
integers k and compute
< f

lE[MeiFk] = lE[(Mt - Mk) + MkiFk]
= lE[Me - MkiFk] + lE[MkiFk]
= lE[Me - MkiFk] + Mk
= lE[Me - Mk] + Mk = Mk. (3.2.5)

Here we have used the notation lE[· · · I.Fk] of Chapter 2 to denote the con­
ditional expectation based on the information at time k, which in this case
is knowledge of the first k coin tosses. The second equality is a result of the
linearity of conditional expectations (Theorem 2.3.2(i)). The third equality
is because Mk depends only on the first k coin tosses (it is .1"k-measurable,
where, in the language of Definition 2.1.5, Fk is the a-algebra of information
corresponding to the first k coin tosses). The fourth equality follows from
independence (Theorem 2.3.2(iv)).


3.2.4 Quadratic Variation of the Symmetric Random Walk


Finally, we consider the quadratic variation of the symmetric random walk.
The quadratic variation up to time k is defined to be
k

[M, M]k = L (MJ - Mj_t)2 = k. (3.2.6)
j=l

Note that this is computed path-by-path. The quadratic variation up to time
k along a path is computed by taking all the one-step increments Mj - Mj-l
along that path (these are equal to Xj, which is either 1 or -1, depending on


86 3 Brownian Motion


the path), squaring these increments, and then summing them. Since (Mj ­
Mj_1) [2 ] = 1, regardless of whether Mj - Mj-1 is 1 or -1, the sum in (3.2.6)
is equal to E7=1 1 = k, as reported in that equation.
We note that [M, M]k is the same as Var(Mk) (set ki+l = k and ki = 0
in (3.2.4)), but the computations of these two quantities are quite different.
Var(Mk) is computed by taking an average over all paths, taking their prob­
abilities into account. If the random walk were not symmetric (i.e., if p were
different from q), this would affect Var(Mk)· By contrast, [M, M]k is com­
puted along a single path, and the probabilities of up and down steps do not
enter the computation. One can compute the variance of a random walk only
theoretically because it requires an average over all paths, realized and unre­
alized. However, from tick-by-tick price data, one can compute the quadratic
variation along the realized path rather explicitly. For a random walk, there is
the somewhat unusual feature that [M, M]k does not depend on the particular
path chosen, but we shall see later that the quadratic variation for a random
process generally does depend on the path along which it is computed.


3.2.5 Scaled Symmetric Random Walk

To approximate a Brownian motion, we speed up time and scale down the step
size of a symmetric random walk. More precisely, we fix a positive integer n
and define the scaled symmetric random walk





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-105-0.png)



are independent. These random variables depend on different coin tosses. For
example, w< [100] ) (0.20) - w< [100] ) (0) depends on the first 20 coin tosses and
w< [100] l(0.70) - w< [100] l(0.20) depends on the next 50 tosses. Furthermore, if
0 s :S t are such that ns and nt are integers, then
:S
IE(w< [n] >(t) - w< [n] >(s)) = 0, Var(w< [n] l(t) - w< [n] l(s)) = t - s. (3.2.8)

This is because w< [n] l(t) - w< [n] l(s) is the sum of n(t - s) independent
random variables, each with expected value zero and variance For ex­
�.
ample, w< [100] l(0.70) - w< [1] 00l(0.20) is the sum of 50 independent random


3.2 Scaled Random Walks 87


1



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-106-0.png)

H






88 3 Brownian Motion


In general, for t 2 0 such that nt is an integer,


(3.2.10)


paths.


between -25 and 25, the scaled random walk w< [100) ] (0.25) can take any of
the values

-2.5, -2.3, -2.1, . . ., -0.3, -0.1, 0.1, 0.3, . . ., 2.1, 2.3, 2.5.

In order for w< [100] l (0.25) to take the value 0.1, we must get 13 heads and 12
tails in the 25 tosses. The probability of this is

25
P{W (100) (0.25) -- 0.1 } -- � � 13! 12! 2 ( )      - 0.1555. - (3.2.11)

We plot this information in Figure 3.2.3 by drawing a histogram bar centered
at 0.1 with area 0.1555. Since this bar has width 0.2, its height must be
0. 7775. Figure 3.2.3 shows similar histogram bars for all possible
values of w<= [100] - (0.25) between -1.5 and 1.5.
The random variable w< [100] l (0.25) has expected value zero and variance
0.25. Superimposed on the histogram in Figure 3.2.3 is the normal density



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-107-0.png)
3.2 Scaled Random Walks 89



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-108-0.png)





with mean zero and variance t, the moment-generating function is


90 3 Brownian Motion



cp(u) eux f(x) dx





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-109-0.png)









If we were to substitute x 0 into the expression on the right-hand side,
g,
derivative of the numerator with respect to x is


3.2 Scaled Random Walks 91



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-110-0.png)










92 3 Brownian Motion

The stock price at time t is determined by the initial stock price 8(0) and
the result of the first nt coin tosses. The sum of the number of heads Hnt and
number of tails Tnt in the first nt coin tosses is nt, a fact that we write as

nt = Hnt + Tnt·

The random walk Mnt is the number of heads minus the number of tails in
these nt coin tosses:

=
Mnt Hnt - Tnt·
Adding these two equations and dividing by 2, we see that
1
Hnt = 2(nt + Mnt)·

Subtracting them and dividing by 2, we see further that


is


to the distribution of
###### � }



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-111-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-111-1.png)

1og 8n(t)



n t





converges to the distribution of


3.3 Brownian Motion 93
1
=
log S(t) log S(O) + aW(t) - 2a [2] t,

where W(t) is a normal random variable with mean zero and variance t. To do
this, we need the Taylor series expansion of f(x) = log(1 + x). We compute
f'(x) (1 + x)- [1 ] and f"(x) = -(1 + x) [-][2 ] and evaluate them to obtain
###### f'(O) [= ] = 1 and f"(O) [= ] -1. According to Taylor's Theorem,


bution of a normal random variable with mean zero and variance t, a random
variable we call W(t). However, in one of its appearances, w< [n] l(t) is multiplied
by a term that has n in the denominator, and this will have limit zero. The
term 0 ( n [-!] also has limit zero as n --+ oo. We conclude that as n --+ oo the
)
distribution of log S(t) approaches the distribution of log S(O) - �a [2] t+aW(t),
which is what we set out to prove.
0


3.3 Brownian Motion


3.3.1 Definition of Brownian Motion

We obtain Brownian motion as the limit of the scaled random walks w< [n] l(t)
of (3.2.7) as n --+ oo. The Brownian motion inherits properties from these
random walks. This leads to the following definition.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-112-0.png)
94 3 Brownian Motion


Definition 3.3.1. Let (il, F, IP') be a probability space. For each w E il, sup­
pose there is a continuous function W(t) of t - 0 that satisfies W(O) 0
and that depends on w. Then W(t), t 0, is a Brownian motion if for all =

                    0 to < t1 < - · · < tm the increments
###### =
W(ti) W(h) - W(to), W(t2) - W(ti), . . ., W(tm) - W(tm-d (3.3.1)
###### =
are independent and each of these increments is normally distributed with
IE[W(ti+I) - W(ti)] = 0, (3.3.2)
Var[W(ti+I) - W(ti)] ti+I - ti. (3.3.3)
###### =

One difference between Brownian motion W(t) and a scaled random walk,
say w< [100] )(t), is that the scaled random walk has a natural time step and
is linear between these time steps, whereas the Brownian motion has no linear
pieces. The other difference is that, while the scaled random walk w< [100] )(t)
is only approximately normal for each t (see Figure 3.2.3), the Brownian
motion is exactly normal. This is a consequence of the Central Limit Theorem,
Theorem 3.2.1. Not only is W(t) W(t) -W(O) normally distributed for each
t, but the increments W(t) - W(s) = are normally distributed for all 0 ::; s < t.
There are two ways to think of w in Definition 3.3.1. One is to think of
w as the Brownian motion path. A random experiment is performed, and its
outcome is the path of the Brownian motion. Then W(t) is the value of this
path at time t, and this value of course depends on which path resulted from
the random experiment. Alternatively, one can think of w as something more
primitive than the path itself, akin to the outcome of a sequence of coin tosses,
although now the coin is being tossed "infinitely fast." Once the sequence of
coin tosses has been performed and the result w obtained, then the path of the
Brownian motion can be drawn. If the tossing is done again and a different w
is obtained, then a different path will be drawn.
In either case, the sample space il is the set of all possible outcomes of
a random experiment, .r is the a-algebra of subsets of il whose probabilities
are defined, and IP' is a probability measure. For each A E .r, the probability
of A is a number IP'(A) between zero and one. The distributional statements
about Brownian motion pertain to IP'.
For example, we might wish to determine the probability of the set A
containing all w E il that result in a Brownian motion path satisfying 0 ::;
W(0.25) ::; 0.2. Let us first consider this matter for the scaled random walk
w( [loo] ). If we were asked to determine the set {w : 0 ::; W( [I00] )(0.25) ::; 0.2},
we would note that in order for the scaled random walk w< [100] ) to fall between
0 and 0.2 at time 0.25, the unsealed random walk M25 10W< [100] )(0.25) must
fall between 0 and 2 after 25 tosses. Since M25 can only be an odd number, =
it falls between 0 and 2 if and only if it is equal to 1 or, equivalently, if and
only if w< [100] )(0.25) = 0.1. To achieve this, the coin tossing must result in 13
heads and 12 tails in the first 25 tosses. Therefore, A is the set of all infinite
sequences of coin tosses with the property that in the first 25 tosses there


3.3 Brownian Motion 95



are 13 heads and 12 tails. The probability that one of these sequences occurs,
given by (3.2.11), is IP(A) 0.1555.
For the Brownian motion = W, there is also a set of outcomes w to the
random experiment that results in a Brownian motion path satisfying 0 W(0.25) � 0.2. We choose not to describe this set as concretely as we just did
for the scaled random walk [w<100). ] Nonetheless, there is such a set of w E
Jl,
and the probability of this set is





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-114-0.png)





Because the increments


###### =




###### =



JE(W [2] (t1)] JE(W(ti)W(t2)] · ·   lE(W(t2)W(h)] lE(W [2] (t2)]  -  - ·


(3.3.4)

The moment-generating function of this random vector can be computed

lE(W(tm)W(ti)] lE[W(tm)W(t2)] · · ·



(3.3.4)



The moment-generating function of this random vector can be computed
using the moment-generating function (3.2.13) for a zero-mean normal random
variable with variance t and the independence of the increments in (3.3.1). To
a ist in this computation, we note first that


96 3 Brownian Motion

u3W(t3) + u2W(t2) + u1W(h)
u3(W(t3) - W(t2)) + (u2 + u3)(W(t2) - W(tl))
###### =
+(u1 + u2 + u3)W(h)

and more generally


0 0 [0 ]
UrnW(trn) + Urn-1 W(trn-d + Urn-2W(trn-2) + + u1W(t1)
Urn(W(trn) - W(trn-d) + (urn-1 + Urn)(W(trn-1) - W(trn-2))
###### =
+(urn-2 + Urn-1 + Urn) (W(trn-2) - W(trn-3)) + . . .
. . . + (u1 + u2 + . . . + urn)W(h).

We use these facts to compute the moment-generating function of the random
vector (W(t1), W(t2), . . ., W(trn)):

cp(ub u2, . . ., Urn)
lEexp {urnW(trn) + Urn-1 W(trn-1) + · · · + U1 W(ti)}
###### =

= lE exp {Urn (W(trn) - W(trn-1)) }
·lEexp {(urn-1 + urn) (W(trn-1) - [W(t] rn-2 [)) } ]
. . · lE exp { (u1 + u2 + . . . + urn)W(t1)}
exp �u;.(trn - trn-1)} · exp { � (urn-1 + urn) [2] (trn-1 - trn-2)}
###### = {

. . . exp { � ( U1 + u2 + . . . + Urn) [2] t1} .

In conclusion, the moment-genemting function for Brownian motion (i.e., for
the m-dimensional random vector (W(tl), W(t2), . . ., W(trn))) is


The distribution of the Brownian increments in (3.3.1) can be specified
by specifying the joint density or the joint moment-generating function of
the random variables W(t1), W(t2), . . ., W(trn)· This leads to the following
theorem.


Theorem 3.3.2 (Alternative characterizations of Brownian motion).
Let (f.?, .1", lP) be a probability space. For each w E f.?, suppose there is a

lEexp {urn(W(trn) - W(trn-1)) + (urn-1 + urn)(W(trn-1) - W(trn-2))+
###### =
. . . + (u1 + u2 + . . · + Urn)W(t1)}



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-115-0.png)
3.3 Brownian Motion 97

continuous function W(t) of t 2: 0 that satisfies W(O) = 0 and that depends
on w. The following thr properties are equivalent.
(i} For all 0 = to t1 tm, the increments
< <          - · · <

W(h) = W(h) - W(to), W(t2) - W(t1), . . ., W(tm) - W(tm-d
are independent and each of these increments is normally distributed with
mean and variance given by (3.3.2} and (3.3.3).
(ii} For all 0 = to < t1 < - · · < tm, the mndom variables W(t1), W(t2), . . .,
W(tm) are jointly normally distributed with means equal to zero and co­
variance matrix (3.3.4).
(iii} For all 0 = to < h < - · · < tm, the mndom variables W(h), W(t2), . . .,
W(tm) have the joint moment-genemting function (3.3.5}.
If any of (i}, (ii}, or (iii} holds (and hence they all hold}, then W(t), t 2: 0,
is a Brownian motion.


3.3.3 Filtration for Brownian Motion


In addition to the Brownian motion itself, we will need some notation for the
amount of information available at each time. We do that with a filtration.

Definition 3.3.3. Let ( !l, F, IP') be a probability space on which is defined a
Brownian motion W(t), t 2: 0. A filtration for the Brownian motion is a
collection of a-algebms F(t), t 2: 0, satisfying:
(i} (Information accumulates) For 0 � s < t, every set in F(s) is also in
F(t). In other words, there is at least as much information available at
the later time F ( t) as there is at the earlier time F ( s).
(ii} (Adaptivity) For each t 2: 0, the Brownian motion W(t) at time t is
F(t)-measumble. In other words, the information available at time t is
sufficient to evaluate the Brownian motion W(t) at that time.
(iii} (Independence of future increments) For 0 � t < u, the increment
W(u) - W(t) is independent of F(t). In other words, any increment of the
Brownian motion after time t is independent of the information available
at time t.
Let Ll(t), t 2: 0, be a stochastic process. We say that Ll(t) is adapted to the
filtmtion F(t) if for each t 2: 0 the mndom variable Ll(t) is F(t)-measumble. [1 ]

Properties (i) and (ii) in the definition above guarantee that the infor­
mation available at each time t is at least as much as one would learn from
observing the Brownian motion up to time t. Property (iii) says that this

1 The adapted processes we encounter will serve as integrands, and for this one
needs them to be jointly measurable in t and w so that their integrals are defined
and are themselves adapted processes. This is a technical requirement that we
shall ignore in this text.


98 3 Brownian Motion


information is of no use in predicting future movements of the Brownian mo­
tion. In the a et-pricing models we build, property (iii) leads to the efficient
market hypothesis.
There are two possibilities for the filtration :F(t) for a Brownian motion.
One is to let :F(t) contain only the information obtained by observing the
Brownian motion itself up to time t. The other is to include in :F(t) information
obtained by observing the Brownian motion and one or more other processes.
However, if the information in :F(t) includes observations of processes other
than the Brownian motion W, this additional information is not allowed to
give clues about the future increments of W because of property (iii).


3.3.4 Martingale Property for Brownian Motion



Theorem 3.3.4. Brownian motion is a martingale.
PROOF: Let 0 : s : t be given. Then
IE[W(t)i:F(s)) = IE[(W(t) - W(s)) W(s)i:F(s)]
+



= IE(W(t) - W(s)i:F(s)) + IE(W [(s] )i [:F(s)] )



= IE(W(t) - W(s)] W(s)
+



= W(s).
The justifications for the steps in this equality are the same as the justifications
for (3.2.5). 0



3.4 Quadratic Variation

We computed the quadratic variation of the scaled random walk W( [n] ) up
to time in (3.2.10), and this quadratic variation turned out to be This
T T.
was computed by taking each of the steps of the scaled random walk between
times 0 and squaring them, and summing them.
T,
For Brownian motion, there is no natural step size. If we are given   - 0,
T
we could simply choose a step size, say � for some large and compute the
n,
quadratic variation up to time with this step size. In other words, we could
T
compute
(3.4.1)
                - ] [2 ]
###### [w ((j [+] nl [)T] ) w

We are interested in this quantity for small step sizes, and so as a last step we �
could evaluate the limit as - oo. If we do this, we will get the same final
n T,
answer as for the scaled random walk in (3.2.10). This is proved in Theorem
3.4.3 below.
The paths of Brownian motion are unusual in that their quadratic variation
is not zero. This makes stochastic calculus different from ordinary calculus
and is the source of the volatility term in the Black-Scholes-Merton partial
differential equation. These matters will be discussed in the next chapter.


3.4 Quadratic Variation 99


3.4.1 First-Order Variation


Before proving that Brownian motion accumulates T units of quadratic varia­
tion between times 0 and T, we digress slightly to discuss first-order variation
(as opposed to quadratic variation, which is second-order variation). Consider
the function f(t) in Figure 3.4.1. We wish to compute the amount of up and
down oscillation undergone by this function between times 0 and T, with the
down moves adding to rather than subtracting from the up moves. We call
this the first-order variation FV r(f). For the function f shown, it is



FVr [(f) ][= ] [ [f(t] t [)] - [f(] O [)] ) - [ [f(t] 2 [)] - [f(] h [)] ) [+ ] [ [f(] T [)] [-] j [(t2)] )





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-118-0.png)





f [(t) ]


Fig. 3.4.1. Computing the first-order variation.


In general, to compute the first-order variation of a function up to time T,
we first choose a partition II = { t0, t1 1 • - -, tn} of [0, T], which is a set of times

0 = t0 < h <              - · · < tn = T.


100 3 Brownian Motion


These will serve to determine the step size. We do not require the parti­
tion points to = 0, h, t2, . . ., tn = T to be equally spaced, although they
are allowed to be. The maximum step size of the partition will be denoted

n-1
111 1 [-+] 0 j=O

The limit in (3.4.3) is taken as the number n of partition points goes to infinity
and the length of the longest subinterval ti+l - ti goes to zero.
Our first task is to verify that the definition (3.4.3) is consistent with the
formula (3.4.2) for the function shown in Figure 3.4.1. To do this, we use
the Mean Value Theorem, which applies to any function f(t) whose deriva­
tive f'(t) is defined everywhere. The Mean Value Theorem says that in each
subinterval [tj, ti+Il there is a point tj such that


3.4.2).


f(t)


Fig. 3.4.2. Mean Value Theorem.


Multiplying (3.4.4) by ti+l - ti, we obtain
f(tj+I) - f(tj) = f'(tj)(tj+l - tj)·

The sum on the right-hand side of (3.4.3) may thus be written as

IIJIII = maxj=O, ...,n-l(tj+l - tj)· We then define
FVr(J) = lim L lf(ti+I) - f(tj)l. (3.4.3)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-119-0.png)
3.4 Quadratic Variation 101
n-1
'E if'<t;)i(tj+l - tj),
i=O

which is a Riemann sum for the integral of the function 1/'(t)j. Therefore,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-120-0.png)



and thus









leads to a 0 oo situation, which can be anything betw n 0 and oo . 0
### ·


102 3 Brownian Motion


Most functions have continuous derivatives, and hence their quadratic vari­
ations are zero. For this reason, one never considers quadratic variation in
ordinary calculus. The paths of Brownian motion, on the other hand, can­
not be differentiated with respect to the time variable. For functions that do
not have derivatives, the Mean Value Theorem can fail and Remark 3.4.2 no
longer applies. Consider, for example, the absolute value function f(t) = ltl in
Figure 3.4.3. The chord connecting (t1, J(ti)) and (t2, j(t2)) has slope, but
nowhere between h and t2 does the derivative of f(t) = ltl equal - Indeed, !
!
this derivative is always -1 for t 0, is always 1 for t > 0, and is undefined
<
at t = 0, where the the graph of the function f(t) = ltl has a "point." Figure
3.2.2 suggests correctly that the paths of Brownian motion are very "pointy."
Indeed, for a Brownian motion path W(t), there is no value of t for which
W ( t) is defined.
ft


Fig. 3.4.3. Absolute value function.


Theorem 3.4.3. Let W be a Brownian motion. Then [W, W](T) = T for all
T 2: 0 almost surely.
We recall that the terminology almost surely means that there can be some
paths of the Brownian motion for which the a ertion [W, W] (T) = T is not
true. However, the set of all such paths has zero probability. The set of paths
for which the a ertion of the theorem is true has probability one.


PROOF OF THEOREM 3.4.3: Let II = {to, t1, . . ., tn} be a partition of [0, T).
Define the sampled quadratic variation corresponding to this partition to be
n-1
Qrr = L (W(ti+I) - W(ti)) [2]          
j= [O ]
We must show that this sampled quadratic variation, which is a random vari­
able i.e., it depends on the path of the Brownian motion along which it is
(



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-121-0.png)
3.4 Quadratic Variation 103

computed) converges to T as **I** J I - 0. We shall show that it has expected
value T, and its variance converges to zero. Hence, it converges to its expected
value T, regardless of the path along which we are doing the computation. [2 ]
The sampled quadratic variation is the sum of independent random vari­
ables. Therefore, its mean and variance are the sums of the means and vari­
ances of these random variables. We have
IE [ (W(ti+I)-W(ti)) [2] ] = Var [W(ti+I)-W(ti)] = ti+l -ti, (3.4.6)

which implies
n-1 n-1
IEQrr = LIE [(w(tj+I)-W(ti)) [2] ] = L(ti+I -ti) = T,
j=O j=O

as desired. Moreover,

Var [ (W(tj+I)-W(tj)) [2] ]

=IE [ (W(tj+I)-W(ti))4] -2(ti+I -ti)IE [ (W(ti+I)-W(ti)) [2] ]
+(tj+1 -tj
)
The fourth moment of a normal random variable with zero mean is three times 2•
its variance squared (see Exercise 3.3). Therefore,
IE [ (W(tJ+1)-W(tj))4] = 3(ti+l -ti) [2],
=IE (W(tj+I)-W(ti))2-(ti+l -ti)r
###### [ ( ]



Var [ (W(ti+I)-W(ti)) [2] ] = 3(ti+l -ti) [2 ] -2(tj+l -ti) [2 ] + (ti+l -ti) [2 ]

= 2(tj+l-tj)2, (3.4.7)
and
n-1 n-1
Var(Qrr) = var [(w(tj+1)-W(ti)) [2] ] 2(tj+l -tj)2
L: L:
j=O j=O
n-1
: L 2 **I** 1 I(tj+1 -tj) = 2 **I** 1 IT.
j=O

In particular, limiiii-tO Var(Qrr) = 0, and we conclude that limiii i-tO Qrr =
IEQrr = T. 0
2 The convergence we prove is actually convergence in mean square, also called
L [2] -convergence. When this convergence takes place, there is a subsequence along
which the convergence is almost sure (i.e., the convergence takes place for all
paths except for a set of paths having probability zero). We shall not dwell on
subtle differences among types of convergence of random variables.


104 3 Brownian Motion


Remark 3.4.4. In the proof above, we derived the equations (3.4.6) and (3.4. 7):


and


(3.4.8)


(3.4.9)


W(tj)) [2 ] converges to T. Each of the terms (W(ti+1) -W(t1)) [2 ] in this sum
can be quite different from its mean t1+1 -t1 = �' but when we sum many
terms like this, the differences average out to zero.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-123-0.png)
3.4 Quadratic Variation 105


We write informally
dW(t) dW(t) = dt, (3.4.10)
but this should not be interpreted to mean either (3.4.8) or (3.4.9). It is only
when we sum both sides of (3.4.9) and call upon the Law of Large Numbers
to cancel errors that we get a correct statement. The statement is that on an
interval [0, T], Brownian motion accumulates T units of quadratic variation.
If we compute the quadratic variation of Brownian motion over the time
interval [0, TI), we get [W, W] (T1) = T1. If we compute the quadratic variation
over where 0 we get Therefore, if we

[0, T2], < T1 < T2, [W, W](T2) = T2.
partition the interval square the increments of Brownian motion for

[T11 T2],
each of the subintervals in the partition, sum the squared increments, and
take the limit as the maximal step size approaches zero, we will get the limit
Brownian motion accumulates

[W, W](T2) - [W, W](TI) = T2 -T1. T2 -T1
units of quadratic variation over the interval Since this is true for

[T1, T2].
every interval of time, we conclude that
Brownian motion accumulates quadratic variation at rate one per unit
time.
We write (3.4.10) to record this fact. In particular, the dt on the right-hand
side of (3.4.10) is multiplied by an understood 1.
As mentioned earlier, the quadratic variation of Brownian motion is the
source of volatility in a et prices driven by Brownian motion. We shall even­
tually scale Brownian motion, sometimes in time- and path-dependent ways,
in order to vary the rate at which volatility enters these a et prices.
0
Remark 3.4.5. Let II = {to,t1, ...,tn} be a partition of [O,T) (i.e., 0 = to <
t1 < < tn = T). In addition to computing the quadratic variation of

       - · ·
Brownian motion



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-124-0.png)










106 3 Brownian Motion


and so



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-125-0.png)





0









= a2 (W(ti+I)-W(ti))2 + �a2) (ti+l -ti)2



+2a a2 W(tj+I) -W(tj))(ti+1 -ti)· (3.4.15)
)
###### (a- Y: ]=0 [(]
     

3.5 Markov Property 107

When the maximum step size lll l maxj=O, ...,m-l(tj+l - tj) is small,
then the first term on the right-hand side of (3.4.15) is approximately equal to =
its limit, which is a [2 ] times the amount of quadratic variation accumulated by
Brownian motion on the interval [T11 T2], which is T2 - T1. The second term
on the right-hand side of (3.4.15) is (a - !a [2] ) [2 ] times the quadratic variation
of t, which was shown in Remark 3.4.5 to be zero. The third term on the
right-hand side of (3.4.1'5) is 2a a - !a [2] ) times the cross variation of W(t)
(
and t, which was also shown in Remark 3.4.5 to be zero. We conclude that
when the maximum step size lll l is small, the right-hand side of (3.4.15) is
approximately equal to a [2] (T2 - Tl), and hence


(3.4.16)


If the a et price S(t) really is a geometric Brownian motion with constant
volatility a, then a can be identified from price observations by computing the
left-hand side of (3.4.16) and taking the square root. In theory, we can make
this approximation as accurate as we like by decreasing the step size. In prac­
tice, there is a limit to how small the step size can be. Between trades, there
is no information about prices, and when a trade takes place, it is sometimes
at the bid price and sometimes at the ask price. On small time intervals, the
difference in prices due to the bid-ask spread can be as large as the difference
due to price fluctuations during the time interval.


3.5 Markov Property


this section, we show that Brownian motion is a Markov process and discuss
In
its transition density.

Theorem 3.5.1. Let W(t), t � 0, be a Brownian motion and let :F(t), t � 0,
be a filtration for this Brownian motion (see Definition 3.3.3). Then W(t),
t � 0, is a Markov process.

PROOF: According to Definition 2.3.6, we must show that whenever 0 � s �
t and f is a Borel-measurable function, there is another Borel-measurable
function g such that
lE[f(W(t))j:F(s)] g(W(s)). (3.5.1)
###### =

To do this, we write
lE[f(W(t)) j:F(s)] lE[/((W(t)-W(s)) + W(s)) j:F(s)]. (3.5.2)
###### =

The random variable W(t) - W(s) is independent of :F(s), and the random
variable W(s) is :F(s)-measurable. This permits us to apply the Independence



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-126-0.png)
108 3 Brownian Motion


Lemma, Lemma 2.3.4. In order to compute the expectation on the right-hand
side of (3.5.2), we replace W(s) by a dummy variable x to hold it constant
and then take the unconditional expectation of the remaining random variable
(i.e., we define g(x) = lEf(W(t) - W(s) + x)). But W(t) - W(s) is normally
distributed with mean zero and variance t - s. Therefore,


obtain



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-127-0.png)

so that we may further rewrite (3.5.3) as



and (3.5.1) as



IE[f(W(t)) j.F(s)] = f(y)p(r, W(s), y) dy.
I:



g(x) = f(y)p(r, x, y) dy
I:



(3.5.4)


(3.5.5)



This equation has the following interpretation. Conditioned on the informa­
tion in .F(s) (which contains all the information obtained by observing the
Brownian motion up to and including time s), the conditional density of W(t)
is p(r, W(s), y). This is a density in the variable y. This density is normal with
mean W(s) and variance T = t - s. In particular, the only information from
F(s) that is relevant is the value of W(s). The fact that only W(s) is relevant
is the essence of the Markov property.



3.6 First Passage Time Distribution


In Chapter 5 of Volume I, we studied the first pa age time for a random walk,
first using the optional sampling theorem for martingales to obtain the distri­
bution in Section 5.2 and then rederiving the distribution using the reflection


3.6 First Pa age Time Distribution 109


principle in Section 5.3. Here we develop the first approach; the second is pre­
sented in the next section. In Sections 5.2 and 5.3 of Volume I, we observed
after deriving the distribution of the first pa age time for the symmetric
random walk that our answer could easily be modified to obtain the first pas­
sage distribution for an asymmetric random walk. In this section, we work
only with Brownian motion, the continuous-time counterpart of the symmet­
ric random walk. The case of Brownian motion with drift, the continuous-time
counterpart of an asymmetric random walk, is treated in Exercise 3.7. We re­
visit this problem in Chapter 7, where it is solved using Girsanov's Theorem.
The resulting formulas often provide explicit pricing and hedging formulas for
exotic options. Examples of the application of these formulas to such options
are given in Chapter 7.
Just as we began in Section 5.2 of Volume I with a martingale that had
the random walk in the exponential function, we must begin here with a
martingale containing Brownian motion in the exponential function. We fix a
constant The so-called exponential martingale corresponding to which is
u. u,

=
Z(t) exp (3.6.1)
{ uW(t)- �u [2] t},



plays a key role in much of the remainder of this text.



Theorem 3.6.1 (Exponential martingale). Let W(t), t ; be a Brow­
0,
nian motion with a filtmtion :F( t), t ; 0, and let u be a constant. The process
Z(t), t of {3.6.1} is a martingale.
2: 0,
PROOF: For : s : t, we have
0
lE[Z(t)I:F(s)]



lE exp :F(s)
= { uW(t)- �u [2] t} I
### [ ]



lE exp { u(W(t)-W(s))} · exp :F(s)
= { uW(s)- �u [2] t} I
### [ ]

u(W(t)-W(s)) }I :F(s)],

[2]



exp ·lE [ exp { u(W(t)-W(s)) }I :F(s)], (3.6.2)
= { uW(s)- �u [2] t}



where we have used "taking out what is known" (Theorem 2.3.2(ii)) for the
last step. We next use "independence" (Theorem 2.3.2(iv)) to write
lE [exp{u(W(t)-W(s))}I:F(s)] [= ] lE [exp{u(W(t) -W(s))}] .

Because W(t) - W(s) is normally distributed with mean zero and variance
t-s, this expected value is exp { �u2(t-s)} (see (3.2.13)) . Substituting this
into (3.6.2), we obtain the martingale property

lE[Z(t) i:F(s)] exp s Z(s).
= u [2] = D
###### }
{ uW(s)- �


1 10 3 Brownian Motion

Let m be a real number, and define the first passage time to level m

Tm = min{t ;; 0; W(t) = m}. (3.6.3)

This is the first time the Brownian motion W reaches the level m. If the
Brownian motion never reaches the level m, we set Tm = oo. A martingale
that is stopped ("frozen" would be a more apt description) at a stopping
time is still a martingale and thus must have constant expectation. (The text
following Theorem 4.3.2 of Volume I discusses this in more detail.) Because
of this fact,



=
1 = Z(O) IEZ(t 1\ Tm) = IE exp uW(t 1\ Tm) - �u [2] (t 1\ Tm)}], (3.6.4)
###### [ {



where the notation t 1\ Tm denotes the minimum oft and Tm.
For the next step, we a ume that u  - 0 and m  - 0. In this case, the
Brownian motion is always at or below level m for t � T m and so

(3.6.5)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-129-0.png)











3 The interchange of limit and expectation implicit in this step is justified by the
Dominated Convergence Theorem, Theorem 1 .4.9.


3.7 Reflection Principle 1 1 1



IE [n{rm<oo} exp (3.6.6)
{
-�u2rrn}] =e-a [rn] .



Equation (3.6.6) holds when m and are positive. We may not substitute
into this equation, but since it holds for every positive we may take
0 u
u = the limit on both sides as 0. This yields4 1E [n{rm<oo}] 1 or, equivalently, u,
u..!. < oo} 1. = (3.6.7)
Because is finite with probability one P{rrn (= we say is finite almost surely),
we may drop the indicator of this event in (3.6.6) to obtain
Trn Trn
exp (3.6.8)
{ }
###### [
IE -�0'2Trn = e-a [rn] .

We have done the hard work in the proof of the following theorem. ]



We have done the hard work in the proof of the following theorem.
Theorem 3.6.2. For m E IR, the first passage time of Brownian motion to
level m is finite almost surely, and the Laplace transform of its distribution is
given by
(3.6.9)

Trn Tlrnl

Letting a 0, we obtain oo so long as m =F 0.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-130-0.png)

3. 7 Reflection Principle


3. 7.1 Reflection Equality

this section, we repeat for Brownian motion the reflection principle argu­
In
ment of Section 5.3 of Volume I for the random walk. The reader may wish
to review that section before reading this one.
We fix a positive level m and a positive time t. We wish to "count" the
Brownian motion paths that reach level m at or before time t (i.e., those paths
for which the first pa age time to level m is less than or equal to t). There
are two types of such paths: those that reach level m prior to t but at time t
Trn
are at some level w below m, and those that exceed level m at time t. There
are also Brownian motion paths that are exactly at level m at time t, but
unlike the case of the random walk in Section 5.3 of Volume I, the probability
of this for Brownian motion is zero. We may thus ignore this possibility.

4 Here we use the Monotone Convergence Theorem, Theorem 1 .4.5.


112 3 Brownian Motion


Fig. 3.7.1. Brownian path and reflected path.


As Figure 3.7.1 illustrates, for each Brownian motion path that reaches
level m prior to time t but is at a level w below m at time t, there is a
"reflected path" that is at level 2m - w at time t. This reflected path is
constructed by switching the up and down moves of the Brownian motion
from time T onward. Of course, the probability that a Brownian motion
m
path ends at exactly w or at exactly 2m - w is zero. In order to have nonzero
probabilities, we consider the paths that reach level m prior to time t and are
at or below level w at time t, and we consider their reflections, which are at
or above 2m - w at time t. This leads to the key reflection equality
lP{Tm � t, W(t) � w} = lP{W(t) �2m - w}, w � m, m > 0. (3.7.1)


3.7.2 First Passage Time Distribution

We draw two conclusions from (3.7.1). The first is the distribution for the
random variable T
m .

Theorem 3.7.1. For all m f. 0, the random variable Tm has cumulative dis­
tribution function



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-131-0.png)
and density



3.7 Reflection Principle 1 13


(3.7.3)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-132-0.png)

other words,

for Tm:


distribution, and (3.7.2) provides the cumulative distribution function of the
latter. Finally, (3.7.3) is obtained by differentiating (3.7.2) with respect to t.
0
Remark 3. 7.2. From (3.7.3), we see that
jmj m [2 ]
lEe [-<XTm ] = e [-] a [m ] frm (t) dt =
100 0 100 0 t../2
(3. 7.4)
Theorem 3.6.2 provides the apparently different Laplace transform formula
(3.6.9). These two formulas are in fact the same, and the steps needed to
verify this are provided in Exercise 3.9. 0


3. 7.3 Distribution of Brownian Motion and Its Maximum


We define the maximum to date for Brownian motion to be

M(t) = max W(s). (3.7.5)
O�s�t

This stochastic process is used in pricing barrier options. For the value of t in
Figure 3.7.1, the random variable M(t) is indicated. For positive m, we have

-e-am-2t dt for all (): > 0.


1 14 3 Brownian Motion

M(t) � m if and only if Tm : t. This observation permits us to rewrite the
reflection equality (3.7.1) as

JP{M(t) � m, W(t) : w} = JP{W(t) �2m - w}, w : m, m > 0. (3.7.6)

From this, we can obtain the joint distribution of W(t) and M(t).

Theorem 3.7.3. For t > 0, the joint density of (M(t), W(t)) is





PROOF: Because



(3.7.7)


D



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-133-0.png)

and



and




###### l [w ]

-oo





This is (3.7.7).



is


3.8 Summary 115



PROOF: The conditional density is the joint density divided by the marginal
density of the conditioning random variable. The conditional density we seek
here is



_





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-134-0.png)



This is the density in the variable y for the random variable W ( s + T) given
that W(s) = x.
A profound property of Brownian motion is that it accumulates quadratic
variation at rate one per unit time (Theorem 3.4.3). If we choose a time
interval [T1, T2], choose partition points T1 = to < h < · · · < tm = T2,
and compute E';,:� [1 ] (W(tj+l) - W(ti)) [2], we get an answer that depends
on the path along which the computation is done. However, if we let the
number of partition points approach infinity and the length of the longest
subinterval ti+l -ti approach zero, this quantity has limit T2 -T1, the length
the interval over which the quadratic variation is being computed. We
of
write dW(t) dW(t) = dt to symbolize the fact that the amount of quadratic


1 16 3 Brownian Motion


variation Brownian motion accumulates in an interval is equal to the length
of the interval, regardless of the path along which we do the computation.

and pa to the limit, we get zero (Remark 3.4.5). We symbolize this by writing
dW(t) dt = dt dt = 0.
The first pa age time of Brownian motion,
Tm = min{t 0; W(t) = m},
;

is the first time the Brownian motion reaches the level m. For m "1- 0, we
have IP'{rm < oo} = 1 (equation (3.6.7)) (i.e., the Brownian motion eventually
reaches every nonzero level), but IErm = oo (Remark 3.6.3). The random
variable Tm is a stopping time, has density (Theorem 3.7.1)


3.9 Notes


In 1828, Robert Brown observed irregular movement of pollen suspended in
water. This motion is now known to be caused by the buffeting of the pollen
by water molecules, as explained by Einstein [62]. Bachelier [6] used Brown­
ian motion (not geometric Brownian motion) as a model of stock prices, even
though Brownian motion can take negative values. Levy [107], [108] discovered
many of the nonintuitive properties of Brownian motion. The first mathemat­
ically rigorous construction of Brownian motion is credited to Wiener [159],

[160], and Brownian motion is sometimes called the Wiener process.
Brownian motion and its properties are presented in numerous texts, in­
cluding Billingsley [10]. The development in these notes is a summary of that
found in Karatzas and Shreve [101]. The properties of Brownian motion and
many formulas useful for pricing exotic options are developed in Borodin and
Salminen [18].
Convergence of discrete-time and/or discrete-state models to continuous­
time models, a topic touched upon in Section 3.2.7, is treated by Amin and
Khanna [3], Cox, Ross and Rubinstein [42], Duffie and Protter [60], and Will­
inger and Taqqu [162], among others.

If we compute L.;'=-�/ (W(ti+I) - W(tj))(ti+l - tj) or L.;'=-;_1(tj+l - tj)2


, w � m, m > 0.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-135-0.png)
3.10 Exercises 117


3. 10 Exercises

Exercise 3.1. According to Definition 3.3.3(iii), for 0 : t < u, the Brownian
motion increment W(u) - W(t) is independent of the a-algebra :F(t). Use this
property and property (i) of that definition to show that, for 0 : t < u1 < u2,
the increment W(u2) - W(ui) is also independent of :F(t).

Exercise 3.2. Let W(t), t ; 0, be a Brownian motion, and let :F(t), t ; 0,
be a filtration for this Brownian motion. Show that W [2] (t) - t is a martingale.
(Hint: For 0 ::=; s ::=; t, write W [2] (t) as (W(t) - W(s)) [2 ][+ ] 2W(t)W(s) - W [2] (s).)

Exercise 3.3 (Normal kurtosis). The kurtosis of a random variable is de­
fined to be the ratio of its fourth central moment to the square of its variance.
For a normal random variable, the kurtosis is 3. This fact was used to obtain
(3.4. 7). This exercise verifies this fact.
Let X be a normal random variable with mean JL, so that X - JL has
mean zero. Let the variance of X, which is also the variance of X - JL, be
a2. In (3.2.13), we computed the moment-generating function of X- JL to be
cp(u) = IE [eu] (X-JL [) ] = d [u2cr2], where u is a real variable. Differentiating this
function with respect to u, we obtain


and, in particular, cp'(O) = IE(X - JL) = 0. Differentiating again, we obtain


and, in particular, cp"(O) = IE [(X - JL) [2] ] = a2. Differentiate two more times
and obtain the normal kurtosis formula IE [(X - JL )4] = 3a4.

Exercise 3.4 (Other variations of Brownian motion). Theorem 3.4.3
a erts that if T is a positive number and we choose a partition II with points
0 = to < t1 < t2 < · · · < tn = T, then as the number n of partition points
approaches infinity and the length of the longest subinterval III I approaches
zero, the sample quadratic variation

n-1
L (W(tj+I) - W(tj)) [2 ]
j=O

approaches T for almost every path of the Brownian motion W. In Re­
mark 3.4.5, we further showed that I:;:� (W(tJ+I) - W(t3))(tJ+1 - t3) and
.L:7:�(tJ+1 - t3) [2 ] have limit zero. We summarize these facts by the multipli­
cation rules

dW(t) dW(t) = dt, dW(t) dt = 0, dt dt = 0. (3.10.1 )

cp"(u) = IE [(X- JL)2eu(X-JL)] = (a2 + a4u2) e�cr2u2

cp'(u) = IE [(X- JL)eu(X-JL)] = a2ue!cr2u2


1 18 3 Brownian Motion

(i) Show that as the number m of partition points approaches infinity and
the length of the longest subinterval approaches zero, the sample first
variation
n-1
L IW(tj+I) - W(tj)i
j=O
approaches oo for almost every path of the Brownian motion W. (Hint:
n-1
L (W(tj+1) - W(tj)} [2 ]
j=O



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-137-0.png)


Exercise 3.6. Let W(t) be a Brownian motion and let :F(t), t � 0, be an
a ociated filtration.


3.10 Exercises 1 19

(i) For J.L E JR., consider the Brownian motion with drift J.L:
X(t) = J.Lt + W(t).

Show that for any Borel-measurable function f(y), and for any 0 : s < t,
the function


and

v



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-138-0.png)





Show that for any Borel-measurable function f(y) and for any 0 : s < t
the function g(x) = J000 h(y)p(T,x,y)dy satisfies lE[f(S(t))IF(s)] =
g(S(s)) and hence S has the Markov property and p(T,x,y) is its transi­
tion density.



Exercise 3.7. Theorem provides the Laplace transform of the density
3.6.2
of the first pa age time for Brownian motion. This problem derives the anal­
ogous formula for Brownian motions with drift. Let W be a Brownian motion.
Fix m > 0 and J.L E JR For 0 : t < oo, define
X(t) = J.Lt + W(t),
Tm = min{t � O;X(t) = m} .

As usual, we set Tm = oo if X(t) never reaches the level m. Let a be a positive
number and set
Z(t) = exp aX(t)- ( aJ.L + �a2) t}.
###### {



(i) Show that Z(t), t � 0, is a martingale.
(ii) Use (i) to conclude that
lE [exp{aX(tATm)- (aJ.L+�a2) (ti\Tm)}] = 1, t �O.


120 3 Brownian Motion

(i) Now suppose J.L 2: 0. Show that, for a > 0,


The stock price at time t in this binomial model, which is the result of nt
steps from the initial time, is given by (see (3.2.15) for a similar equation)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-139-0.png)
3.10 Exercises 121





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-140-0.png)

























1 rux2 1
= 1 + 2u2x2 + 7 - 2ux2u + O(x4).



= 1 + 2u2x2 + 7 - 2ux2u + O(x4). (3.10.2)

The notation O(x [i] ) is used to represent terms of the order xi.


122 3 Brownian Motion



(iv) Use the Taylor series expansion log(1 + x) = x + O(x [2] ) to compute
limx.(.O log <p ( u) . Now explain how you know that the limiting distribution for is normal with mean (r - �a [2] )t and variance a [2] t.

Exercise 3.9 (Laplace transform of first passage density). The so­
lution to this problem is long and technical. It is included for the sake of
completeness, but the reader may safely skip it.
Let m > 0 be given, and define
m
###### { [m2][} ]

According to (3.7.3) in Theorem 3.7.1, f(t, m) is the density in the variable t
of the first pa age time T m = min { t 2': 0; W ( t) = m}, where W is a Brownian
motion without drift. Let

J(t, = exp -- .
m) 2



g(a, m) = e-a.t f(t, m) dt, a: > 0,
### 100 f(t,

m).



be the Laplace transform of the density f(t, m). This problem verifies that
g(a, m) = [e] - [m] v'2a, which is the formula derived in Theorem 3.6.2.
(i) For k 1, define
2':



ak [(] m [) ] = c [k/2 ] exp o:t [-] } dt,
###### { [-]

Show that 100



so g(o:, m) = maa(m). Show that



9m(o:, m) [= ] aa(m) - m [2] as(m),
9mm(o:, m) [= ] -3mas(m) + m3a7(m).



(ii) Use integration by parts to show that


2o:
m [2 ]
as(m) = -3aa(m) + 3a7(m).

(i) Use (i) and (ii) to show that g satisfies the second-order ordinary differ­
ential equation
9mm(o:, m) = 2o:g(o:, m).
(iv) The general solution to a second-order ordinary differential equation of
the form
ay"(m) + by'(m) + cy(m) = 0
is

where ..X1 and ..X2 are roots of the characteristic equation
y(m) = AleA'm + A2eA2m,


3. 10 Exercises 123



a..\ [2 ] + b,\ + c = 0.



Here we are a uming that these roots are distinct. Find the general so­
lution of the equation in (iii) when a > 0. This solution has two undeter­
mined parameters A1 and A2, and these may depend on a.
(v) Derive the bound



g(a, m) :S --m - c [3] 1 [2 ] exp - -m [2] dt + --1 e-at dt
###### y'2 0 1 [m ] t { 2t } .,f 1m [oo ] R



t                   - -2t -y'2 0 .,f m
and use it to show that, for every a > 0,



m-too lim g(a, m) = 0.

Use this fact to determine one of the parameters in the general solution
to the equation (iii).
in
(vi) Using first the change of variable s = tjm [2 ] and then the change of variable
y = 1/JS, show that
m.(.O lim g(a, m) = 1.
Use this fact to determine the other parameter in the general solution to
the equation in (iii).


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-143-0.png)
4


Stochastic Calculus


4.1 Introduction


This chapter defines Ito integrals and develops their properties. These are
used to model the value of a portfolio that results from trading a ets in
continuous time. The calculus used to manipulate these integrals is based
on the lt6-Doeblin formula of Section 4.4 and differs from ordinary calcu­
lus. This difference can be traced to the fact that Brownian motion has a
nonzero quadratic variation and is the source of the volatility term in the
Black-Scholes-Merton partial differential equation. The Black-Scholes-Merton
equation is presented in Section 4.5. This is in the spirit of Sections 1.1 and
1.2 of Volume I in which we priced options by determining the portfolio that
would hedge a short position. In particular, there is no discussion of risk­
neutral pricing in this chapter. That topic is taken up in Chapter 5.
Section 4.6 extends stochastic calculus to multiple processes. Section 4. 7
discusses the Brownian bridge, which plays a useful role in Monte Carlo meth­
ods for pricing. We do not treat Monte Carlo methods in this text; we include
the Brownian bridge only because it is a natural application of the stochastic
calculus developed in the earlier sections.


4.2 Ito's Integral for Simple Integrands


We fix a positive number T and seek to make sense of

(4.2.1)
1 [T ][Ll(t) dW(t). ]

The basic ingredients here are a Brownian motion W(t), t 2: 0, together with
a filtration :F(t), t � 0, for this Brownian motion. We will let the integrand
Ll(t) be an adapted stochastic process. Our reason for doing this is that Ll(t)
will eventually be the position we take in an asset at time t, and this typically


126 4 Stochastic Calculus


depends on the price path of the a et up to time t. Anything that depends on
the path of a random process is itself random. Requiring Ll(t) to be adapted
means that we require Ll(t) to be F(t)-measurable for each t ; 0. In other
words, the information available at time t is sufficient to evaluate Ll(t) at
that time. When we are standing at time 0 and t is strictly positive, Ll(t)
is unknown to us. It is a random variable. When we get to time t, we have
sufficient information to evaluate Ll(t); its randomness has been resolved.
Recall that increments of the Brownian motion after time t are indepen­
dent of F(t), and since Ll(t) is F(t)-measurable, it must also be independent
of these future Brownian increments. Positions we take in a ets may depend
on the price history of those a ets, but they must be independent of the
future increments of the Brownian motion that drives those prices.
The problem we face when trying to a ign meaning to the Ito integral
(4.2.1) is that Brownian motion paths cannot be differentiated with respect
to time. If g(t) is a differentiable function, then we can define

Ll(t) dg(t) = Ll(t)g'(t) dt,
1 [T ] 1 [T ]

where the right-hand side is an ordinary (Lebesgue) integral with respect to
time. This will not work for Brownian motion.


4.2.1 Construction of the Integral


To define the integral (4.2.1), Ito devised the following way around the nondif­
ferentiability of the Brownian paths. We first define the Ito integral for simple
integrands Ll(t) and then extend it to nonsimple integrands as a limit of the
integral of simple integrands. We describe this procedure.
Let II = {t0, t1, . . ., tn} be a partition of [0, T]; i.e.,


Assume that Ll(t) is constant in t on each subinterval [t3, t3+I)· Such a process
Ll(t) is a simple process.
Figure 4.2.1 shows a single path of a simple process Ll(t). We shall always
choose these simple processes, as shown in this figure, to take a value at a
partition time t3 and then hold it up to but not including the next partition
time tJ+l· Although it is not apparent from Figure 4.2.1, the path shown
depends on the same w on which the path of the Brownian motion W(t) (not
shown) depends. If one were to choose a different w, there would be a different
path of the Brownian motion and possibly a different path of Ll(t). However,
the value of Ll(t) can depend only on the information available at time t.
Since there is no information at time 0, the value of Ll(O) must be the same
for all paths, and hence the first piece of Ll(t), for 0 � t < h, does not really
depend on w. The value of Ll(t) on the second interval, [h, t2), can depend on
observations made during the first time interval [0, h ) .


![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-146-0.png)



4.2 Ito's Integral for Simple Integrands 127


Fig. 4.2.1. A path of a simple process.



We shall think of the interplay between the simple process Ll(t) and the
Brownian motion W(t) in (4.2.1) in the following way. Regard W(t) as the
price per share of an a et at time t. (Since Brownian motion can take negative
as well as positive values, it is not a good model of the price of a limited­
liability a et such as a stock. For the sake of this illustration, we ignore that
issue.) Think of t0, t1, . . ., tn_1 as the trading dates in the a et, and think
of Ll(t0), Ll(t1), . . ., Ll(tn-1) as the position (number of shares) taken in the
a et at each trading date and held to the next trading date. The gain from
trading at each time t is given by

l(t) = Ll(t0)[W(t) - W(t0)] = Ll(O)W(t), 0 � t � t�,
l(t) = Ll(O)W(t1) + Ll(t1)[W(t) - W(t1)], t1 � t � t2,
I(t) = Ll(O)W(h) + Ll(h)[W(t2) - W(t1)] + Ll(t2)[W(t) - W(t2)],
t2 � t � t3,

and so on. In general, if tk � t � tk+b then
k-1
l(t) = L Ll(tj)[W(tj+l) - W(tj)] + Ll(tk)[W(t) - W(tk)]. (4.2.2)
j=O

The process l(t) in (4.2.2) is the Ito integral of the simple process Ll(t), a fact
that we write as


128 4 Stochastic Calculus



I(t) = Ll(u) dW(u).
###### lo [t ]



In particular, we can take t = tn = T, and (4.2.2) provides a definition for
the Ito integral (4.2.1). We have managed to define this integral not only for
the upper limit of integration T but also for every upper limit of integration
t between 0 and T.



4.2.2 Properties of the Integral


The ItO integral (4.2.2) is defined as the gain from trading in the martingale
W ( t). A martingale has no tendency to rise or fall, and hence it is to be
expected that J(t), thought of as a process in its upper limit of integration t,
also has no tendency to rise or fall. We formalize this observation by the next
theorem and proof.

Theorem 4.2.1. The Ito integml defined by (4.2.2} is a martingale.

PROOF: Let 0 - s - t - T be given. We shall a ume that s and t are in
different subintervals of the partition II (i.e., there are partition points te and
tk such that te < tk, s E [te, te+I), and t E [tk, tk+I)). If s and t are in the same
subinterval, the following proof simplifies. Equation (4.2.2) may be rewritten
as
l-1
I(t) = L Ll(tj) [W(ti+1) - W(ti)] + Ll(te) [W(te+d - W(te)]
j=O
k-1
+ L Ll(tj) [W(tj+l) - W(tj)] + Ll(tk) [W(t) - W(tk)] . (4.2.3)
j=l+1

We must show that IE[J(t)IF(s)] = I(s). We take the conditional expecta­
tion of each of the four terms on the right-hand side of (4.2.3). Every random
variable in the first sum E ;:�Ll(tj) [W(tj+l) - W(tj)] is F(s)-measurable
because the latest time appearing in this sum is � te and te � s. Therefore,
l-1 l-1
IE Ll(ti) [W(ti+1) - W(ti)] F(s) = Ll(ti) [W(ti+I) � W(ti)] .
### [ l
?; ?;

(4.2.4)
For the second term on the right-hand side of (4.2.3), we "take out what is
known" (Theorem 2.3.2(ii)) and use the martingale property of W to write

IE[Ll(te)(W(te+d - W(te)) iF(s)] = Ll(te)(lE[W(te+I)iF(s)]  - W(te))
= Ll(te)(W(s) - W(te)).

Adding (4.2.4) and (4.2.5), we obtain I(s).

(4.2.5)


4.2 Ito's Integral for Simple Integrands 129



It remains to show that the conditional expectations of the third and
fourth terms on the right-hand side of ( 4.2.3) are zero. We will then have
IE[I(t)iF(s)] = I(s).
The summands in the third term are of the form Ll(tj) [W(ti+I) - W(tj)],
where ti 2 tt+1 > s. This permits us to use the following iterated conditioning
trick, which is based on properties (iii) (iterated conditioning) and (ii) (taking
out what is known) of Theorem 2.3.2:



IE Ll(ti) (W(ti+l) - W(tj)) F(s)
###### { I }



= IE IE[Ll(tj) (W(tj+l) - W(tj)) IF(tj)] .r(s)
###### { l }



= IE Ll(ti)(IE[W(ti+l)IF(tj)) - W(ti)) .r(s)
###### { l }
= IE Ll(tj) (W(tj) - W(tj)) .r(s) =
o.
###### { l }



At the end, we have used the fact that W is a martingale. Because the condi­
tional expectation of each of the summands in the third term on the right-hand
side of (4.2.3) is zero, the conditional expectation of the whole term is zero:



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-148-0.png)

The fourth term on the right-hand side of (4.2.3) is treated like the summands
in the third term, with the result that



IE Ll(tk) (W(t) - W(tk)) F(s)
###### { I }



= IE IE[Ll(tk) (W(t) - W(tk)) IF(tk)) .r(s)
###### { l }



= IE Ll(tk) (IE[W(t)IF(tk)) - W(tk)) F(s)
###### { I }



= IE Ll(tk)(W(tk) - W(tk)) F(s) = 0.
###### { I }



This concludes the proof. 0


Because I(t) is a martingale and J(O) = 0, we have IEJ(t) = 0 for all t 2 0.
It follows that Var J(t) = IEJ [2] (t), a quantity that can be evaluated by the
formula in the next theorem.

Theorem 4.2.2 (Ito isometry). The Ito integml defined by (4.2.2} satisfies


IEJ [2] (t) = IE Ll [2] (u) du. (4.2.6)
1t


130 4 Stochastic Calculus

PROOF: To simplify the notation, we set Di = W(tj+t) - W(tj) for j =
0, . . ., k - 1 and Dk = W(t) - W(tk) so that (4.2.2) may be written as I(t) =
E�=O Ll(tj)Dj and

k
I [2] (t) = L Ll [2] (tj)DJ + 2 L Ll(ti)Ll(ti)Di [D] i [. ]
j=O O$i<j$k

We first show that the expected value of each of the cross terms is zero. For i <
j, the random variable Ll(ti)Ll(tj)Di is F(tj)-measurable, while the Brownian
increment Dj is independent of F(tj)· Furthermore, lEDj = 0. Therefore,


Finally, we turn to the quadratic variation of the Ito integral I(t) thought
of as a process in its upper limit of integration t. Brownian motion accumulates
quadratic variation at rate one per unit time. However, Brownian motion is
scaled in a time- and path-dependent way by the integrand Ll(u) as it enters
the Ito integral I(t) = I� Ll(u) dB(u). Because increments are squared in
the computation of quadratic variation, the quadratic variation of Brownian
motion will be scaled by Ll [2] (u) as it enters the Ito integral. The following
theorem gives the precise statement.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-149-0.png)
4.2 Ito's Integral for Simple Integrands 131


Theorem 4.2.3. The quadmtic variation accumulated up to time t by the Ito
integml (4.2.2} is

[I, I](t) = Ll [2] (u) du. (4.2.8)
###### lo [t ]

PROOF: We first compute the quadratic variation accumulated by the Ito
integral on one of the subintervals (tj, ti+Il on which Ll(u) is constant. For
this, we choose partition points


and consider

(4.2.9)


where again we have used the fact that Ll(u) is constant for ti - u < ti+l·
Analogously, the quadratic variation accumulated by the Ito integral between
times tk and t is ft [t] k Ll [2] (u) du. Adding up all these pieces, we obtain (4.2.8).
0

In Theorems 4.2.2 and 4.2.3, we finally see how the quadratic variation
and the variance of a process can differ. The quadratic variation is computed
path-by-path, and the result can depend on the path. If along one path of the
Brownian motion we choose large positions Ll(u), the Ito integral will have
a large quadratic variation. Along a different path, we could choose small
positions Ll(u) and the Ito integral would have a small quadratic variation.
The quadratic variation can be regarded as a measure of risk, and it depends
on the size of the positions we take. The variance of I(t) is an average over
all possible paths of the quadratic variation. Because it is the expectation of
something, it cannot be random. As an average over all possible paths, real­
ized and unrealized, it is a more theoretical concept than quadratic variation.
We emphasize here that what we are calling variance is not the empirical vari­
ance. Empirical (or sample) variance is computed from a realized path and



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-150-0.png)
132 4 Stochastic Calculus



is an estimator of the theoretical variance we are discussing. The empirical
variance is sometimes carelessly called variance, which creates the possibility
of confusion.
Finally, we recall the equation (3.4.10), dW(t) dW(t) = dt, of Remark
3.4.4. We interpret this equation as the statement that Brownian motion ac­
cumulates quadratic variation at rate one per unit time. It is another way of
writing (W, W](t) = t, t 2 0. The Ito integral formula J(t) = J� Ll(u) dW(u)
can be written in differential form as dl(t) = Ll(t) dW(t), and we can then
use (3.4.10) to square dl(t):
dl(t) dl(t) = ..1 [2] (t) dW(t) dW(t) = ..1 [2] (t) dt. (4.2.10)

This equation says that the Ito integral J(t) accumulates quadratic variation
at rate ..1 [2] (t) per unit time. The rate of accumulation is typically both time­
and path-dependent. Equation (4.2.10) is another way of reporting the result
of Theorem 4.2.3.
Remark 4.2.4 (on notation). The notations



I(t) = Ll(u) dW(u) (4.2.11)
1 [t ]



and
dl(t) = Ll(t) dW(t) (4.2.12)
mean almost the same thing, although the second is probably more intuitive.
Equation (4.2.11) has the precise meaning given by (4.2.2) . Equation (4.2.12)
has the imprecise meaning that when we move forward a little bit in time
from time t, the change in the Ito integral I is Ll(t) times the change in the
Brownian motion W. It also has a precise meaning, which one obtains by
integrating both sides, remembering to put in a constant of integration J(O):



I(t) = 1(0) + Ll(u) dW(u). (4.2.13)
1 [t ]



We say that (4.2.12) is the differential form of (4.2.13) and that (4.2.13) is the
integral form of (4.2.12). These two equations mean exactly the same thing.
The only difference between (4.2.11) and (4.2.13), and hence the only dif­
ference between (4.2.11 ) and (4.2.12), is that (4.2.11 ) specifies the initial con­
dition J(O) = 0, whereas (4.2.12) and (4.2.13) permit J(O) to be any arbitrary
constant. D



4.3 Ito's Integral for General Integrands

In this section, we define the Ito integral J0 [T ] Ll(t) dW(t) for integrands Ll(t)
that are allowed to vary continuously with time and also to jump. In partic­
ular, we no longer a ume that Ll(t) is a simple process shown in Figure
as


4.3 Ito's Integral for General Integrands 133



4.2.1. We do a ume that Ll(t), t ; 0, is adapted to the filtration :F(t), t 2: 0.
We also a ume the square-integrability condition



IE Ll [2] (t) dt < 00. (4.3.1)
###### lo [T ]



In order to define J0 [T ] Ll(t) dW(t), we approximate Ll(t) by simple pro­
cesses. Figure 4.3.1 suggests how this can be done. In that figure, the continu­
ously varying Ll(t) is shown as a solid line and the approximating simple inte­
grand is dashed. Notice that Ll(t) is allowed to jump. The approximating sim­
ple integrand is constructed by choosing a partition 0 = to < t1 < t2 < t3 < t4,
setting the approximating simple process equal to Ll( ti) at each ti, and then
holding the simple process constant over the subinterval [tj, tH1). As the max­
imal step size of the partition approaches zero, the approximating integrand
will become a better and better approximation of the continuously varying
one.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-152-0.png)


134 4 Stochastic Calculus

For each Lln(t), the Ito integral Lln(u) dW(u) has already been defined for
0 - t � T. We define the Ito integral for the continuously varying integrand
### Ll(t) by the formula [1 ] J�



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-153-0.png)











nition,





1 For each t, the limit in 4.3.3 exists because In(t) = J; Lln(u) dW(u) is a Cauchy
sequence in F, IP'). ( This is because of Ito's isometry ) Theorem 4.2.2, which
yields IE(In(t) - Im(t) L2(il, = IE J; ILln(u) - Llm(u) du. As a consequence of ( ) 4.3.2,
the right-hand side has limit zero as ) [2 ] n and m approach infinity. 1 [2 ] ( )


4.3 Ito's Integral for General Integrands 135



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-154-0.png)
136 4 Stochastic Calculus


From (4.3.5), we conclude that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-155-0.png)







(4.3.6)



(





(4.3.7)



then we would not have gotten this term see Exercise 4.4). The integral ob­
(
tained by making this replacement is called the Stratonovich integral, and the
ordinary rules of calculus apply to it. However, it is inappropriate for finance.
In finance, the integrand represents a position in an a et and the integrator
represents the price of that a et. We cannot decide at 1:00 p.m. which po­
sition we took at 9:00 a.m. We must decide the position at the beginning of
each time interval, and the Ito integral is the limit of the gain achieved by
that kind of trading as the time between trades approaches zero.
For functions g(t) that have a derivative, integrals such as J� g(t) dg(t)
are not sensitive to this distinction i.e., the Ito integral and Stratonovich
(
integral approximations have the same limit, which is �g (T . For functions
that have a nonzero quadratic variation, integrals are sensitive to where in
### the subintervals the approximating integrands are evaluated. 2 ))


4.4 ltODoeblin Formula 137

The upper limit of integration T in ( 4.3.6) is arbitrary and can be replaced
by any t ; 0. In other words,

t : 0. (4.3.8)


which could be written in differential notation as

df(W(t)) = J'(W(t)) W'(t) dt = J'(W(t)) dW(t).

Because W has nonzero quadratic variation, the correct formula has an extra
term, namely,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-156-0.png)

df(W(t)) = J'(W(t)) dW(t) + f"(W(t)) dt. (4.4.1 )

             


This is the lto-Doeblin formula in differential form. Integrating this, we obtain
the lto-Doeblin formula in integral form:



f(W(t)) - f(W(O)) = J'(W(u)) dW(u) + J"(W(u)) du. (4.4.2)

                  ### The mathematically meaningful form of the lt61t 1t Doeblin formula is the



The mathematically meaningful form of the lt6Doeblin formula is the
integral form (4.4.2) . This is because we have precise definitions for both
terms appearing on the right-hand side. The first, J; J'(W(u)) dW(u), is an
Ito integral, defined in the previous section. The second, J; f"(W(u)) du, is
an ordinary (Lebesgue) integral with respect to the time variable.


138 4 Stochastic Calculus



For pencil and paper computations, the more convenient form of the ltO­
Doeblin formula is the differential form (4.4.1). There is an intuitive meaning
but no precise definition for the terms df(W(t)), dW(t), and dt appearing in
this formula. The intuitive meaning is that df(W(t)) is the change in f(W(t))
when t changes a "little bit" dt, dW(t) is the change in the Brownian motion
when t changes a "little bit" dt, and the whole formula is exact only when
the "little bit" is "infinitesimally small." Because there is no precise definition
for "little bit" and "infinitesimally small," we rely on (4.4.2) to give precise
meaning to (4.4.1).
The relationship between (4.4.1) and (4.4.2) is similar to that developed
in ordinary calculus to a ist in changing variables in an integral. If asked
to compute the indefinite integral J f(u)f'(u) du, we might make the change
of variable v = f(u) and write dv = f'(u) du, so that the indefinite integral
becomes Jvdv, which is !v [2 ] + C = !J [2] (u) + C, where C is a constant of
integration. The final formula
f(u)f'(u) du = f [2] (u) + C
###### �
J

is correct, as can be verified by differentiating !P(u)+C to get f(u)f'(u). We
do not attempt to give precise definitions to the terms dv and du appearing
in the equation dv = f'(u) du used in deriving it.
We formalize the preceding discussion with a theorem that provides a
formula slightly more general than ( 4.4.2) in that it allows f to be a function
of both t and x.

Theorem 4.4.1 (ItO-Doeblin formula for Brownian motion). Let
f(t, x) be a function for which the partial derivatives ft(t, x), fx(t, x), and
fxx(t, x) are defined and continuous, and let W(t) be a Brownian motion.
Then, for every T 2 0,



T
f(T, W(T)) = f(O, W(O)) + ft(t, W(t)) dt



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-157-0.png)



( 4.4.4)

In this case, Taylor's formula to second order is exact (there is no remainder
term) because !'" and all higher derivatives of f are zero. We return to this
matter later.


4.4 ItO-Doeblin Formula

Fix T > 0, and let II = {t0, h, . . ., tn} be a partition of [O,T] (i.e., 0 =
to < t1 < · · · < tn = T). We are interested in the difference between f(W(O))
and f(W(T)). This change in f(W(t)) between times t = 0 and t = T can
be written as the sum of the changes in f(W(t)) over each of the subintervals

[t;, tJ+1]. We do this and then use Taylor's formula (4.4.4) with Xj = W(t;)
and Xj+I = W(tJ+d to obtain
n-1
f(W(T)) - f(W(O)) = L [f(W(tj+I)) - f(W(t;))]
j=O
n-1
= L f'(W(t3)) [W(tJ+I) - W(t3)]
j=O n-1
+ L j"(W(t3)) [W(tJ+I) - W(t3)t (4.4.5)
###### � j=O

For the function f(x) = !x [2], the right-hand side of (4.4.5) is
n-1 n-1
L [W(t] 3 [)] [ [W(t] 3+ [1) - W(t] 3 [)] ] [+ ] L [ [W(tJ] +I [) - W(t3)t ] (4.4.6)
###### j=O � j=O

If we let II I I - 0, the left-hand side of (4.4.5) is unaffected and the terms on
the right-hand side converge to an Ito integral and one-half of the quadratic
variation of Brownian motion, respectively:
f(W(T)) - f(W(O))

139



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-158-0.png)



= f' (W(t)) dW(t) + f" (W(t)) dt. (4.4.7)



This is the ItO-Doeblin formula in integral form for the function f(x) = !x [2] If instead of the quadratic function f(x) = !x [2 ] we had a general func­
tion f(x), then in (4.4.5) we would have also gotten a sum of terms con­
taining [W(tJ+1) - W(t3)t But according to Exercise 3.4 of Chapter 3,
L:;,:-� iW(tj+I) - W(t3)i [3 ] has limit zero as III I - 0. Therefore, this term
would make no contribution to the final answer.

If we take a function f(t,x) of both the time variable t and the variable
x, then Taylor's Theorem says that


140 4 Stochastic Calculus



f(tj+I, Xj+I) - f(tj, Xj)
=
ft(tj, Xj)(tj+1 - tj) + fx(tj,Xj)(Xj+1 - Xj)
1
+2fxx(tj,Xj)(Xj+1 - Xj) + ftx(tj, Xj)(tj+l - tj)(Xj+1 - Xj) 2



+ ftt(t3, x3)(t3+l - t3)2 + higher-order terms. (4.4.8)

 


We replace x3 by W(t3), replace Xj+l by W(tj+l), and sum:
f(T, W(T)) - f(O, W(O))
n-1
= L [f(tj+l, W(tj+1)) - f(tj, W(tj))]
j=O
n-1 n-1
= L ft(tj, W(tj))(tj+l - tj) + L fx(tj, W(tj)) (W(tj+I) - W(tj))
j=O j=O



1 n-1
2
+2 L fxx(tj, W(tj)) (W(tj+1) - W(tj))
j=O
n-1
+ L ftx(tj, W(tj))(tj+l - tj)(W(tj+1) - W(tj))
j=O n-1
( 4.4.9)
j=O
+ L !tt(ti, W(t3))(ti+1 - t3)2 + higher-order terms.

 


When we take the limit as lll l - 0, the left-hand side of (4.4.9) is unaf­
fected. The first term on the right-hand side of (4.4.9) contributes the ordinary
(Lebesgue) integral



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-159-0.png)

to the final answer. As 111711 - 0, the second term contributes the Ito in­
tegral Io [T ] fx(t, W(t)) dW(t). The third term contributes another ordinary
(Lebesgue) integral, �I: fxx(t, W(t)) dt, similar to the way we obtained
this integral in (4.4.7). In other words, in the third term we can replace
(W(ti+I) - W(t3)) [2 ] by ti+1 - t3. This is not an exact substitution, but when
we sum the terms this substitution gives the correct limit as 111711 - 0. See
Remark 3.4.4 for more discussion of this point. With this substitution, the
third term on the right-hand side of (4.4.9) contributes �I: fxx(t, W(t)) dt.
These limits of the first three terms appear on the right-hand side of (4.4.3).
The fourth and fifth terms contribute zero. Indeed, for the fourth term, we
observe that


4.4 ItO-Doeblin Formula 141

(4.4. 10)


n-1
111 1--+0 j=O -2
-2


The higher-order terms likewise contribute zero to the final answer. 0
Remark 4.4.2. The fact that the sum (4.4. 10) of terms containing the product
(tj+I - t1)(W(tJ+1) - W(t1)) has limit zero can be informally recorded by
the formula dt dW ( t) = 0. Similarly, the sum ( 4.4.11) of terms containing
( tj+l - t1 ) [2 ] also has limit zero, and this can be recorded by the formula
dt dt = 0. We can write these terms if we like in the ltO-Doeblin formula, so
that in differential form it becomes
df(t, W(t))
1
= ft(t, W(t)) dt + fx(t, W(t)) dW(t) + 2fxx(t, W(t)) dW(t) dW(t)
1
+ ftx(t, W(t)) dt dW(t) + 2Jxx (t, W(t)) dt dt,

but
dW(t) dW(t) = dt, dt dW(t) = dW(t) dt = 0, dt dt = 0, (4.4. )
12
and the ItO-Doeblin formula in differential form simplifies to

1
df(t, W(t)) = !t(t, W(t)) dt+ fx(t, W(t)) dW(t)+ 2!xx(t, W(t)) dt. (4.4.13)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-160-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-160-1.png)
142 4 Stochastic Calculus


In Figure 4.4.1, we illustrate the Taylor series approximation of the differ­
ence f(W(ti+d) - f(W(tj)) for a function f(x) that does not depend on t.
The first-order approximation, which is f'(W(tj)) (W(tj+l) - W(tj)), has an
error due to the convexity of the function f(x). Most of this error is removed
by adding in the second-order term �f"(W(tj)) (W(tj+1) - W(tj)) [2], which
captures the curvature of the function f(x) at x = W(tj)·


Fig. 4.4.1. Taylor approximation to f(W(t;H))      - f(W(t;)).


In other words,
f(W(t3+I)) - f(W(tj)) = f'(W(tj)) (W(tj+l) - W(ti)) + small error,
(4.4.14)


and

f(W(ti+I)) - f(W(ti)) = f'(W(ti)) (W(ti+I) - W(ti))
+ f"(W(ti)) (W(ti+I) - W(ti)) [2 ]

+ smaller error. i (4.4.15)

In both (4.4.14) and (4.4.15), as lll l - 0, the errors approach zero. However,
before we let lll l - 0, we must first sum these equations over j, and the
smaller we make lll l, the more terms there are in the sum. When we sum
both sides of (4.4.14), the errors accumulate, and although the error in each
summand approaches zero as lll l - 0, the sum of the errors does not. When
we use the more accurate approximation (4.4.15), this does not happen; the
limit of the sum of the smaller errors is zero. We need the extra accuracy
of (4.4.15) because the paths of Brownian motion are so volatile (i.e., they



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-161-0.png)
4.4 ltO-Doeblin Formula

have nonzero quadratic variation) . This extra term makes stochastic calculus
different from ordinary calculus.
The ItO-Doeblin formula often simplifies the computation of Ito integrals.
For example, with f(x) !x [2], this formula says that
=

     - W [2] (T) = f(W(T)) - f(W(O))


Rearranging terms, we have formula ( 4.3.6) and have obtained it without
going through the approximation of the integrand by simple processes as we
did in Example 4.3.2.


4.4. 2 Formula for Ito Processes


We extend the ItO-Doeblin formula to stochastic processes more general than
Brownian motion. The processes for which we develop stochastic calculus are
the Ito processes defined below. Almost all stochastic processes, except those
that have jumps, are ItO processes.

Definition 4.4.3. Let W(t), t 2 0, be a Brownian motion, and let :F(t),
t 2 0, be an associated filtration. An Ito process is a stochastic process of the
form
X(t) X(O) lo [t ] Ll(u) dW(u) lo [t ] 8(u) du, (4.4.16)
= + +

where X(O) is nonrandom and Ll(u) and 8(u) are adapted stochastic pro­
cesses. [2 ]

order to understand the volatility a ociated with Ito processes, we must
In
determine the rate at which they accumulate quadratic variation.

Lemma 4.4.4. The quadratic variation of the ItO process (4.4.16} is

[X, X)(t) lo [t ] Ll [2] (u) du. (4.4.17)
=

PROOF: We introduce the notation I(t) = J; Ll(u) dW(u), R(t) = J; 8(u) du.
Both these processes are continuous in their upper limit of integration t. To
2 We athe integrals on the right-hand side of (4.4.16) are defined and the Ito integral ume that lEI� Ll [2 ] (u) du and I� IB(u) i du are finite for every t - 0 so that
is a martingale. We shall always make such integrability a umptions, but we do
not always explicitly state them.

143



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-162-0.png)
144 4 Stochastic Calculus

determine the quadratic variation of X on [0, t], we choose a partition II =
{to, h, . . ., tn} of [O, t] (i.e., 0 = to < t1 < · · · < tn = t) and we write the
sampled quadratic variation
n-1 n-1 n-1
L [ [X(t] j+I) - [X(t] j [)] ] [2 = ] L [ [I(t] i+I [) - I(t] j [)] ] [2 ][+ ] L [ [R(t] j+I [) - R(t] j [)] ] [2 ]
j=O j=O j=O
n-1
+2
L [I(tj+I) - I(tj)] [R(tj+1) - R(tj)] .

As IIIIII --+ 0, the first term on the right-hand side, I:j,:-g [I(tj+I) - I(tj)] [2],
converges to the quadratic variation of I on [0, t], which according to Theorem
4.3.1 (vi) is [I, I](t) = J; Ll [2] (u) du. The absolute value of the second term is
bounded above by
n-1
max IR(tk+1) - R(tk)l · L IR(ti+I) - R(tj)l
O�k�n-1
j=O

j=O



t;+I

- e(u) du
o<'
-· IR(t,.,) - R(t,)i ·
### � lfH l



t;+I
:5 IB(u)l du
olf!t;_1 IR(tk+I) - R(tk)l ·





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-163-0.png)

O<k<n-1

        -        


t
:5 2 IB(u)l du,
0�V(t;_1 II(tk+I) - I(tk)i ·
fo



and this has limit 0· J; jB(uW du = 0 as III I --+ 0 because I(t) is continuous.
We conclude that (X, X)(t) = [I, I](t) = J; Ll [2] (u) du. 0


The conclusion of Lemma 4.4.4 is most easily remembered by first writing
( 4.4.16) in the differential notation
dX(t) = Ll(t) dW(t) + B(t) dt (4.4.18)

and then using the differential multiplication table (4.4.12) to compute


4.4 ItO-Doeblin Formula 145
dX(t) dX(t) = Ll [2] (t) dW(t) dW(t) + 2Ll(t)8(t) dW(t) dt + 8 [2] (t) dt dt
= Ll [2] (t) dt. (4.4.19)

This says that, at each time t, the process X is accumulating quadratic
variation at rate Ll [2] (t) per unit time, and hence the total quadratic varia­
tion accumulated on the time interval (O, t] is (X, X](t) = J� Ll [2] (u) du. This
quadratic variation is solely due to the quadratic variation of the Ito inte­
gral I(t) = f� Ll(u) dW(u). The ordinary integral R(t) = f� 8(u) du has zero
quadratic variation and thus contributes nothing to the quadratic variation
of X.
Notice in this connection that having zero quadratic variation does not
necessarily mean that R(t) is nonrandom. Because 8(u) can be random, R(t)
can also be random. However, R(t) is not as volatile as I(t). At each time t,
we have a good estimate of the next increment of R(t). For small time steps

 - 0,
h
R(t + h) � R(t) + 8(t)h,
and we know both R(t) and 8(t) at time t. This is like investing in a money
market account at a variable interest rate. At each time, we have a good
estimate of the return over the near future because we know today's interest
rate. Nonetheless, the return is random because the interest rate ( e in this
analogy) can change. In contrast, I is more volatile. At time t, one estimate
of I(t + h) is
I(t + h) � I(t) + Ll(t)(W(t + h) - W(t)),
but we do not know W(t + h) - W(t) at time t. In fact, W(t + h) - W(t) is
independent of the information available at time t. This is like investing in a
stock.
So far we have discussed integrals with respect to time, such as R(t) =
J� 8( u) du appearing in ( 4.4.16) and Ito integrals (integrals with respect to
Brownian motion) such as I(t) = J� Ll(u) dW(u), also appearing in (4.4.16).
In addition, we shall need integrals with respect to Ito processes (i.e., integrals
of the form J� r(u) dX(u), where r is some adapted process). We define such
an integral by separating dX(t) into a dW(t) term and a dt term as in (4.4.18).

Definition 4.4.5. Let X(t), t � 0, be an Ito process as described in Definition
4-4.3, and let r(t), t � 0, be an adapted process. We define the integral with
respect to an Ito process [3 ]
lo [t ] T(u) dX(u) = lo [t ] T(u)Ll(u) dW(u) + lo [t ] T(u)8(u) du. 4.4.20
( )

We again work through the sketch of the proof of Theorem 4.4.1, but with
the Ito process X(t) replacing the Brownian motion W(t). In place of (4.4.9),
we now have

3 We a ume that E J; r [2] (u)Ll [2 ] (u) du and jr(u)8(u)i du are finite for every
t   - 0 so that the integrals on the right-hand side of J; ( 4.4.20) are defined.


146 4 Stochastic Calculus



f(T, X(T)) - f(O, X(O))
n-1 n-1

j=O j=O
n-1
+ L fxx(tj, X(tj)} (X(tj+I) - X(tj)} [2 ]
###### � j=O
n-1
+ L ftx(ti, X(ti))(ti+1 - ti)(X(ti+1) - X(ti))
j=O
n-1
+ ftt(tj, X(tj))(ti+l - ti) [2 ] + higher-order terms. (4.4.21)
###### �
t,;
=
L ft(ti, X(ti))(ti+1 - ti) + L fx(ti, X(ti)} (X(ti+I) - X(tj))



The last two sums on the right-hand side have zero limits as lll l - 0 for the
same reasons the analogous terms have zero limits in the sketch of the proof
of Theorem 4.4.1 (see (4.4.10) and (4.4.11)). The higher-order terms likewise
have limit zero. The limit of the first term on the right-hand side of (4.4.21)
is J0 [T ] ft(t, X(t))dt. The limit of the second term is
T T T
fx(t, X(t)) dX(t) = fx(t, X(t)}Ll(t)dW(t) + fx(t, X(t))8(t)dt.
### Finally, the limit of the third term on the right-hand side of 1 1 1 (4.4.19) is



Finally, the limit of the third term on the right-hand side of (4.4.19) is
T T
fxx(t, X(t)) d[X, X](t) = fxx(t, X(t))Ll2(t) dt
###### � �

because the Ito process 1 X(t) accumulates quadratic variation at rate 1



because the Ito process X(t) accumulates quadratic variation at rate Ll [2] (t)
per unit time (Lemma 4.4.4). These considerations lead to the following gen­
eralization of Theorem 4.4.1.

Theorem 4.4.6 {ItO-Doeblin formula for Ito process). Let X(t),
an
t 2 0, be an Ito process as described in Definition 4.4.3, and let f(t, x) be a
function for which the partial derivatives ft(t,x), fx(t,x), and fxx(t,x) are
defined and continuous. Then, for every T 2 0,
f(T, X(T))



T T
= f(O, X(O)} + ft(t, X(t)) dt + fx(t, X(t)) dX(t)

T
1
### 1 1



T
1
fxx(t, X(t)) d[X, X](t)
0
+2
### 1

[T ]



0

= f(O, X(O)) + ft(t, X(t)) dt + fx(t, X(t))Ll(t) dW(t)
T 1 T
+ 0 fx(t,X(t))8(t) dt + -1 [T ] 2 0 1fxx(t, X(t))Ll [T ] [2] (t) dt. (4.4.22)
### 1 1


4.4 ItO-Doeblin Formula 147

Remark 4.4. 7 (Summary of stochastic calculus). Theorem 4.4.6 is stated in
mathematically precise language. Every term on the right-hand side has a solid
definition, and in the end the right-hand side reduces to a sum of a nonrandom
quantity X(O)), three ordinary (Lebesgue) integrals with respect to time,
and an Ito integral.
/(0,
However, it is easier to remember and use the result of this theorem if we
recast it in differential notation. We may rewrite ( 4.4.22) as


1
df(t, X(t)) = ft(t, X(t)) dt + f (t, X(t)) dX(t) + (t, X(t)) dX(t) dX(t).
x 2/xx (4.4.23)


The guiding principle here is that we write out the Taylor series expansion of
f(t, X(t)) with respect to all its arguments, which in this case are t and X(t).
We take this Taylor series expansion out to first order for every argument that
has zero quadratic variation, which in this case is t, and we take the expansion
out to second order for every argument that has nonzero quadratic variation,
which in this case is X(t).
We may reduce (4.4.23) to an expression that involves only dt and dW(t)
by using the differential form (4.4.18) of the Ito process (i.e., dX(t) =
Ll(t) dW(t) + B(t) dt) and the formula (4.4.19) for the rate at which X(t)
a umulates quadratic variation (i.e., dX(t) dX(t) = Ll2(t) dt). This is ob­
tained by squaring the formula for dX(t) and using the multiplication table
(4.4.12). Making these substitutions in (4.4.23), we obtain
df(t, X(t)) = It (t, X(t)) dt + f (t, X(t))Ll(t) dW(t)
1
+ f (t, X(t) )B(t) dt x + (t, X(t))Ll2(t) dt. (4.4.24)
x 2/xx

Ito calculus is little more than repeated use of this formula in a variety of
situations. 0


4.4.3 Examples


We conclude this section with three examples illustrating Remark 4.4. 7. Many
more examples are developed in subsequent sections and in the exercises.
Example 4.4.8 (Generalized geometric Brownian motion). Let W(t), t � 0,
be a Brownian motion, let :F(t), t � 0, be an a ociated filtration, and let a(t)
and u(t) be adapted processes. Define the Ito process



and u(t)


X(t) u(s) dW(s) +
= 0
###### 1 [t ] 1

Then



t
1
X(t) u(s) dW(s) + ( a(s) - u2(s) )ds.
= 0 0
###### 1 1 2



(4.4.25)



dX(t) = u(t) dW(t) + ( a(t) - �u2(t)) dt,


148 4 Stochastic Calculus



and
dX(t) dX(t) = a2(t) dW(t) dW(t) = a2(t) dt.
Consider an a et price process given by

S(t) = S(O)eX [(] t [) ] = S(O) exp { a(s) dW(s) + ( a(s) - �a2(s) )ds},
###### lo [t ] lo [t ]
(4.4.26)
where S(O) is nonrandom and positive. We may write S(t) = f(X(t)), where
f(x) = S(O)ex, f' (x) = S(O)e [x], and f" (x) = S(O)e [x] . According to the It6Doeblin formula
dS(t) = df(X(t))
= f' (X(t)) dX(t) + �f" (X(t)) dX(t) dX(t)
= S(O)eX [(t) ] dX(t) + [�] S(O)e [x(t) ] dX(t) dX(t)
2
= S(t) dX(t) + �S(t) dX(t) dX(t)
= a(t)S(t) dt + a(t)S(t) dW(t). (4.4.27)

The a et price S(t) has instantaneous mean rate of return a(t) and volatil­
ity Both the instantaneous mean rate of return and the volatility are
a(t).
allowed to be time-varying and random.
This example includes all possible models of an asset price process that is
always positive, has no jumps, and is driven by a single Brownian motion.
Although the model is driven by a Brownian motion, the distribution of S(t)
does not need to be log-normal because a(t) and a(t) are allowed to be time­
varying and random. If a and a are constant, we have the usual geometric
Brownian motion model, and the distribution of S(t) is log-normal.
In the case of constant a and a, ( 4.4.26) becomes



S(t) = S(O) exp { aW(t) + (a - �a2) t (4.4.28)
###### }·



One can incorrectly argue from this formula that since Brownian motion is a
martingale (i.e., it has no overall tendency to rise or fall), the mean rate of
return for S(t) must be a - The error in this argument is that although
!a2.
W(t) is a martingale, S(O)euW( [t) ] is not. The convexity of the function eux
imparts an upward drift to S(O)euW( [t] ). In order to correct for this, one must
subtract in the exponential; the process S(O) exp { is a
!a2t aW(t)- !a2t}
martingale (see Theorem 3.6.1). If we now add at in the exponential, we get
S(t), a process with mean rate of return a.
The lt6-Doeblin formula automatically keeps track of these effects, even
when a and a are time-varying and random. If a = 0, then ( 4.4.27) yields
dS(t) = a(t)S(t) dW(t).


4.4 ItO-Doeblin Formula 149


Integration of both sides yields


8(t) 8(0) + a(s)8(s) dW(s).
###### = lo [t ]



The right-hand side is the nonrandom constant 8(0) plus an Ito integral,
which is a martingale, and hence (in the case a= 0)


(4.4.29)


is a martingale. In other words, the term a(t)8(t) dW(t) on the right-hand
side of (4.4.27) contributes no drift, just pure volatility, to the a et price.
When a(t) is a nonzero random process, (4.4.27) shows that it plays the
role of the mean rate of return. In the case of time-varying and random a(t),
we will call this the instantaneous mean rate of return since it depends on the
time (and the sample path) where it is evaluated. 0

The preceding example supplies the heart of the proof of the following
theorem.

Theorem 4.4.9 (Ito integral of a deterministic integrand). Let W(s),
s 2: 0, be a Brownian motion, and let Ll( s) be a nonrandom function of time.
Define 1(t) = J� Ll(s) dW(s). For each t 2: 0, the random variable 1(t) is
normally distributed with expected value zero and variance J� Ll [2] (s) ds.

PROOF: The mean and variance of 1(t) are easy to determine. Since 1(t) is
a martingale and 1(0) = 0, we must have IE1(t) = 1(0) = 0. Ito's isometry
(Theorem 4.3.1(v)) implies that



Var1(t) = IE12(t) = Ll [2] (s) ds.
###### lo [t ]



We do not need to take the expected value of J� Ll [2] (s) ds on the right-hand
side of this formula because Ll( s) is not random.
The challenge is to show that 1(t) is normally distributed. We shall do
this by establishing that 1(t) has the moment-generating function of a nor­
mal random variable with mean zero and variance J� Ll (s) ds, which is (see
(3.2.13))
2
IEeuJ( [t] ) = exp { Ll (s) ds for all E JR (4.4.30)
###### �u2 lo [t ] 2 } u



(4.4.30)



Because Ll( s) is not random, ( 4.4.30) is equivalent to



!Eexp { Ll (s) ds = 1,
###### lo [t ] }
u1(t) - �u2 2


150 4 Stochastic Calculus


which may be rewritten as

!Eexp {lo [t ] uLl(s) dW(s) - �lo [t ] ( uLl(s) ) [2 ] ds} = 1.


But the process

exp {lo [t ] uLl(s) dW(s) - �lo [t ] (uLl(s)) [2 ] ds}



(4.4.31)



is a martingale. Indeed, it is a generalized geometric Brownian motion with
mean rate of return a = 0; see (4.4.29) with u(s) = uLl(s). Furthermore, this
process takes the value 1 at t = 0, and hence its expectation is always 1. This
gives us (4.4.31).
0

Note that (4.4.31) always holds, regardless of whether Ll(s) is random.
However, we need to a ume that Ll(s) is nonrandom in order to obtain the
moment-generating function formula (4.4.30) from (4.4.31). When Ll(s) is
random, there is no reason that the distribution of J; Ll(s) dW(s) should be
normal.
Example 4.4.10 (Vasicek interest rate model). Let W(t), t � 0, be a Brownian
motion. The Vasicek model for the interest rate process R(t) is



dR(t) = (a - {3R(t)) dt + u dW(t), (4.4.32)

where a, {3, and u are positive constants. Equation (4.4.32) is an example of a
stochastic differential equation. It defines a random process, R(t) in this case,
by giving a formula for its differential, and the formula involves the random
process itself and the differential of a Brownian motion.
The solution to the stochastic differential equation ( 4.4.32) can be deter­
mined in closed form and is
a
R(t) = e-f3t R(O) + - (1 [-] e-f3t) + ue-f3t t ef3 [s ] dW(s ), (4.4.33)
###### 1

a claim that we now verify. In particular, we compute the differential of the
right-hand side of (4.4.33). To do this, we use the ItO-Doeblin formula with


and X(t) = J; ef3 [s ] dW(s). Then the right-hand side of (4.4.33) is f(t, X(t)).
The technique we are using is to separate the right-hand side into two parts: an
ordinary function of two variables t and x, which has no randomness in it, and
an Ito process X(t), which contains all the randomness. For the It6-Doeblin
formula, we shall need the following partial derivatives of f(t, x) :

f(t, x) = e-f3t R(O) + (1 - e-f3t) + ue-f3tx

              
{3 0


4.4 ItO-Doeblin Formula 151

ft(t, x) = -{3e [-] f3 [t ] R(O) + ae [-] f3 [t ]      - a{3e [-] f3 [t] x = a - {3f(t, x),
fx(t, x) = ae [-] f3 [t],
fxx(t,x) = 0.

We shall also need the differential of X(t), which is dX(t) = ef3 [t ] dW(t). We
shall not need dX ( t) dX ( t) = e [2] f3 [t ] dt because f xx ( t, x) = 0. The ItO-Doeblin
formula states that



df(t, X(t))
1
= ft(t, X(t)) dt + fx(t, X(t)) dX(t) + 2fxx(t,X(t)) dX(t) dX(t)



= a - f3f(t, X(t)) dt + adW(t).
( )



This shows that f(t, X(t)) satisfies the stochastic differential equation (4.4.32)
that defines R(t). Moreover, f(O, X(O)) = R(O). Because f(t,X(t)) satisfies
the equation defining R(t) and has the same initial condition as R(t), it must
be the case that f(t, X(t)) = R(t) for all t � 0.
Theorem 4.4.9 implies that the random variable ef3 [s ] dW(s) appearing
on the right-hand side of (4.4.33) is normally distributed with mean zero and J�
variance
e [2] f3 [s ] ds = [_.!:._ ] ( e [2] f3 [t ]                - 1).
2{3
0
1 [t ]
Therefore, R(t) is normally distributed with mean e [-] f3 [t ] R(O) + � (1-e [-] f3 [t] ) and
variance e [-2] f3 [t] ). In particular, no matter how the parameters a > 0,
{3 > 0, and a > 0 are chosen, there is positive probability that R(t) is negative,
an undesirable property for an interest rate model.
The Vasicek model has the desirable property that the interest rate is
mean-reverting. When R(t) = -, the drift term (the dt term) in (4.4.32) is
zero. When R(t) > �, this term is negative, which pushes R(t) back toward
l When R(t) < �, this term is positive, which again pushes R(t) back
toward �- If R(O) = �, then lER(t) = � for all t - 0. If R(O) =/= �' then
limt00 lER(t) = 0
�·

Example 4.4.11 (Cox-Ingersoll-Ross (CIR) interest rate model}. Let W(t),
t � 0, be a Brownian motion. The Cox-Ingersoll-Ross model for the interest
rate process R( t) is

dR(t) = (a - {3R(t)) dt + aJR[i} dW(t), (4.4.34)

where a, {3, and a are positive constants. Unlike the Vasicek equation (4.4.32),
the CIR equation (4.4.34) does not have a closed-form solution. The advantage
of (4.4.34) over the Vasicek model is that the interest rate in the CIR model
does not become negative. If R(t) reaches zero, the term multiplying dW(t)


152 4 Stochastic Calculus

vanishes and the positive drift term a dt in equation ( 4.4.34) drives the interest
rate back into positive territory. Like the Vasicek model, the CIR model is
mean-reverting.
Although one cannot derive a closed-form solution for (4.4.34), the dis­
tribution of R(t) for each positive t can be determined. That computation
would take us too far afield. We instead content ourselves with the derivation
of the expected value and variance of R(t). To do this, we use the function
f(t,x) = ef3tx and the ItO-Doeblin formula to compute
d( ef3t R(t))
= df(t,R(t)}
1
= It (t, R(t)} dt + fx(t, R(t)} dR(t) + ?Jxx (t, R(t)} dR(t) dR(t)
= {3ef3t R(t) dt + ef3t (a - {3R(t)) dt + ef3taJR[iJ dW(t)
= aef3t dt + ae!3tJR[iJ dW(t). (4.4.35)

Integration of both sides of (4.4.35) yields



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-171-0.png)



(4.4.36
)



This is the same expectation as in the Vasicek model.



To compute the variance of R(t), we set X(t) = ef3t R(t), for which we have
already computed
dX ( t) = aef3t dt + aef3t JR(iJ dW ( t) = aef3t dt + ae '¥ v'x(t) dW ( t)

and lEX(t) = R(O) + �(ef3t - 1). According to the ltO-Doeblin formula (with
f(x) = x [2], f'(x) = 2x, and f"(x) = 2),
d(X [2] (t)) = 2X(t) dX(t) + dX(t) dX(t)
= 2aef3t X(t) dt + 2ae'¥ x! (t) dW(t) + a [2] ef3t X(t) dt. (4.4.37)



Integration of ( 4.4.37) yields


405 Black-Scholes-Merton Equation 153



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-172-0.png)























In


Black-Scholes-Merton Equation
4.5

The addition of Merton's name to what has traditionally been called the
Black-Scholes equation is explained in the Notes, Section 4o9o


154 4 Stochastic Calculus


In this section, we derive the Black-Scholes-Merton partial differential
equation for the price of an option on an a et modeled as a geometric Brow­
nian motion. The idea behind this derivation is the same as in the binomial
model of Chapter 1 of Volume I, which is to determine the initial capital
required to perfectly hedge a short position in the option.


4.5.1 Evolution of Portfolio Value

Consider an agent who at each time t has a portfolio valued at X(t). This
portfolio invests in a money market account paying a constant rate of interest
r and in a stock modeled by the geometric Brownian motion
dS(t) = o:S(t) dt + uS(t) dW(t). (4.5.1)

Suppose at each time t, the investor holds L\(t) shares of stock. The position
L\(t) can be random but must be adapted to the filtration a ociated with
the Brownian motion W(t), t - 0. The remainder of the portfolio value,
X(t) - L\(t)S(t), is invested in the money market account.
The differential dX(t) for the investor's portfolio value at each time t is
due to two factors, the capital gain L\(t) dS(t) on the stock position and the
interest earnings r(X(t) - L\(t)S(t)) dt on the cash position. In other words,

dX(t) = L\(t) dS(t) + r(X(t) - L\(t)S(t)) dt
= L\(t) (o:S(t) dt + uS(t) dW(t)) + r(X(t) - L\(t)S(t)) dt
= rX(t) dt + L\(t)(o: - r)S(t) dt + L\(t)uS(t) dW(t). (4.5.2)

The three terms appearing in the last line of (4.5.2) can be understood as
follows:

(i) an average underlying rate of return r on the portfolio, which is reflected
by the term r X ( t) dt,
(ii) a risk premium o: - r for investing in the stock, which is reflected by the
term L\(t)(o: - r)S(t) dt, and
(i) a volatility term proportional to the size of the stock investment, which
is the term L\(t)uS(t) dW(t).
The discrete-time analogue of equation (4.5.2) appears in Chapter 1 of
Volume I as (1.2.12):
Xn+l = L\nSn+l + (1 + r)(Xn - L\nSn)·

We may rearrange terms in this equation to obtain


(4.5.3)


which is analogous to the first line of (4.5.2), except in (4.5.3) time steps for­
ward one unit at a time, whereas in (4.5.2) time moves forward continuously.


4.5 Black-Scholes-Merton Equation 155

See Exercise 4.10 for additional discussion of the rationale for equation ( 4.5.2)
in option pricing.
We shall often consider the discounted stock price e-rts(t) and the dis­
counted portfolio value of an agent, e-rt X(t). According to the ItO-Doeblin
formula with f(t, x) = e-rtx, the differential of the discounted stock price is
d(e [-] rts(t))
= df(t,S(t))
1
= ft (t, S(t)) dt + fx(t, S(t)) dS(t) + ?Jxx (t, S(t)) dS(t) dS(t)
= -re [-] rt S(t) dt + e-rt dS(t)
= (a - r)e [-] rts(t) dt + ae [-] rts(t) dW(t), (4.5.4)

and the differential of the discounted portfolio value is
d(e [-] rtx(t))
= df(t,X(t))

1
= ft (t, X(t)) dt + fx(t, X(t)) dX(t) + ?Jxx (t, X(t)) dX(t) dX(t)
= -re [-] rt X(t) dt + e [-rt ] dX(t)
= Ll(t)(a - r)e [-] rt S(t) dt + Ll(t)ae [-] rt S(t) dW(t)
(4.5.5)
= Ll(t)d(e [-] rts(t)).

Discounting the stock price reduces the mean rate of return from a, the term
multiplying S(t) dt in (4.5.1), to a - r, the term multiplying e-rtS(t) dt in
(4.5.4) . Discounting the portfolio value removes the underlying rate of return
r; compare the last line of (4.5.2) to the next-to-last line of (4.5.5). The last
line of (4.5.5) shows that change in the discounted portfolio value is solely due
to change in the discounted stock price.


4.5.2 Evolution of Option Value

Consider a European call option that pays (S(T)- Kt at time T. The strike
price is some nonnegative constant. Black, Scholes, and Merton argued that
K
the value of this call at any time should depend on the time (more precisely,
on the time to expiration) and on the value of the stock price at that time,
and of course it should also depend on the model parameters r and a and the
contractual strike price Only two of these quantities, time and stock price,
K.
are variable. Following this reasoning, we let c( t, x) denote the value of the call
at time t if the stock price at that time is S(t) = x. There is nothing random
about the function c(t, x). However, the value of the option is random; it is
the stochastic process c(t,S(t)) obtained by replacing the dummy variable x
by the random stock price S(t) in this function. At the initial time, we do not


156 4 Stochastic Calculus



know the future stock prices S(t) and hence do not know the future option
values c(t,S(t)). Our goal is to determine the function c(t,x) so we at least
have a formula for the future option values in terms of the future stock prices.
We begin by computing the differential of c ( t, S ( t)). According to the ltO­
Doeblin formula, it is
dc(t,S(t))
= Ct (t, S(t)) dt + Cx (t, S(t)) dS(t) + 2Cxx(t, S(t)) dS(t) dS(t) 1
= Ct (t, S(t)) dt + cx(t, S(t)) (aS(t) dt + uS(t) dW(t))
+2Cxx (t, S(t) )u1 [2 ] S [2] (t) dt
= ct(t,S(t)) + aS(t)cx(t,S(t)) + �u [2] S [2] (t)cxx(t,S(t))] dt
(4.5.6)
### [ +uS(t)cx(t, S(t)) dW(t).

We next compute the differential of the discounted option price e-rtc( t, S( t)).
Let f(t, x) = e-rtx. According to the ltO-Doeblin formula,
d(e [-] rtc(t, S(t)))
= df(t, c(t, S(t)))
= ft (t, c(t, S(t))) dt + fx (t, c(t, S(t))) dc(t, S(t))
+2fxx ( t, c(t, S(t))) dc(t, S(t)) dc(t, S(t)) 1
= -re [-] rtc(t, S(t)) dt + e [-] rt dc(t, S(t))


(4.5.7)
+�u [2] S [2] (t)cxx(t, S(t))] dt + e [-] rtuS(t)cx(t, S(t))dW(t).


4.5.3 Equating the Evolutions

A (short option) hedging portfolio starts with some initial capital X(O) and
invests in the stock and money market account so that the portfolio value
X(t) at each time t E [0, T] agrees with c(t, S(t)). This happens if and only if
e-rt X(t) = e-rtc(t, S(t)) for all t. One way to ensure this equality is to make
sure that
d(e [-] rt X(t)) = d(e [-] rtc(t, S(t))) for all t E [0, T) (4.5.8)
and X(O) = c(O, S(O)). Integration of (4.5.8) from 0 to t then yields
e-rt X(t) - X(O) = e-rtc(t, S(t)) - c(O, S(O)) for all t E [0, T). (4.5.9)
If X(O) = c(O, S(O)), then we can cancel this term in (4.5.9) and get the
desired equality.

= e-rt -rc(t, S(t)) + Ct(t, S(t)) + aS(t)cx(t, S(t))
###### [


4.5 Black-Scholes-Merton Equation 157


Comparing (4.5.5) and (4.5.7), we see that (4.5.8) holds if and only if
Ll(t)(a - r)S(t) dt + Ll(t)aS(t) dW(t)

= [ -rc(t, S(t)) + Ct(t, S(t)) + aS(t)cx(t, S(t)) + a [2] S [2] (t)cxx(t, S(t))] dt
###### �
(4.5.10)
+aS(t)cx(t, S(t)) dW(t).

We examine what is required in order for ( 4.5.10) to hold.
We first equate the dW(t) terms in (4.5.10), which gives
Ll(t) = cx(t, S(t)) for all t E [0, T). (4.5.11)

This is called the delta-hedging rule. At each time t prior to expiration, the
number of shares held by the hedge of the short option position is the partial
derivative with respect to the stock price of the option value at that time.
This quantity, cx(t, S(t)), is called the delta of the option.
We next equate the dt terms in (4.5.10), using (4.5.11), to obtain
(a - r)S(t)cx(t, S(t))
1
= -rc(t, S(t)) + Ct(t, S( t)) + aS(t)cx(t, S(t)) + 2a [2 ] S [2] (t)cxx(t, S(t))
for all t E [O, T) . (4.5.12)

The term aS(t)cx(t, S(t)) appears on both sides of (4.5.12), and after canceling
it, we obtain


1
rc(t, S(t)) = Ct(t, S(t)) + rS(t)cx(t, S(t)) + 2a [2] S [2] (t)cxx(t, S(t))
for all t E [0, T). (4.5.13)

In conclusion, we should seek a continuous function c( t, x) that is a solution
to the Black-Scholes-Merton partial differential equation


1
Ct(t, x) + rxcx(t, x) + 2a [2] x [2] cxx(t, x) = rc(t, x) for all t E [0, T), x 2 0,
4.5.14)
(
and that satisfies the terminal condition
c(T, x) = (x - K) [+] . (4.5.15)

Suppose we have found this function. If an investor starts with initial capital
X(O) = c(O, S(O)) and uses the hedge Ll(t) = cx(t, S(t)), then (4.5.10) will
hold for all t E [0, T). Indeed, the dW(t) terms on the left and right sides
of (4.5.10) agree because Ll(t) = cx(t, S(t)), and the dt terms agree because
(4.5.14) guarantees (4.5.13). Equality in (4.5.10) gives us (4.5.9) . Canceling
X(O) = c(O,S(O)) and e [-] rt in this equation, we see that X(t) = c(t,S(t)) for
all t E [0, T). Taking the limit as t t T and using the fact that both X(t) and


158 4 Stochastic Calculus
c(t, S(t)) are continuous, we conclude that X(T) = c(T, S(T)) = (S(T)-Kt.
This means that the short position has been successfully hedged. No matter
which of its possible paths the stock price follows, when the option expires,
the agent hedging the short position has a portfolio whose value agrees with
the option payoff.


4.5.4 Solution to the Black-Scholes-Merton Equation


The Black-Scholes-Merton equation (4.5.14) does not involve probability. It is
a partial differential equation, and the arguments t and x are dummy variables,
not random variables. One can solve it by partial differential equation meth­
ods. In this section, however, rather than showing how to solve the equation,
we shall simply present the solution and check that it works. In Subsection
5.2.5, we present a derivation of this solution based on probability theory.
We want the Black-Scholes-Merton equation to hold for all x 0 and
2:
t E [0, T) so that (4.5.14) will hold regardless of which of its possible paths
the stock price follows. If the initial stock price is positive, then the stock price
is always positive, and it can take any positive value. If the initial stock price
is zero, then subsequent stock prices are all zero. We cover both of these cases
by asking (4.5.14) to hold for all x 0. We do not need (4.5.14) to hold at
2:
t = T, although we need the function c(t, x) to be continuous at t = T. If the
hedge works at all times strictly prior to T, it also works at time T because
of continuity.
Equation (4.5.14) is a partial differential equation of the type called back­
ward parabolic. For such an equation, in addition to the terminal condition
(4.5.15), one needs boundary conditions at x = 0 and x = oo in order to
determine the solution. The boundary condition at x = 0 is obtained by sub­
stituting x = 0 into (4.5.14), which then becomes
Ct(t, 0) = rc(t, 0). (4.5.16)

This is an ordinary differential equation for the function c(t, 0) of t, and the
solution is
0) = 0).
c(t, ertc(O,
Substituting t = T into this equation and using the fact that c(T, 0) = (0 K) [+ ] = 0, we see that c(O, 0) = 0 and hence
c(t, 0) = 0 for all t E [0, T]. (4.5.17)

This is the boundary condition at x = 0.
As x - oo, the function c( t, x) grows without boq.nd. In such a case, we
give the boundary condition at x = oo by specifying the rate of growth. One
way to specify a boundary condition at x = oo for the European call is

(4.5.18)
X-+00
lim [c(t, x) - (x - e-r(T-t)K)] = 0 for all t E [O, T].


4.5 Black-Scholes-Merton Equation 159



In particular, c(t, x) grows at the same rate as x as x - oo . Recall that c(t, x)
is the value at time t of a call on a stock whose price at time t is x. For large x,
this call is deep in the money and very likely to end in the money. In this case,
the price of the call is almost as much as the price of the forward contract
discussed in Subsection 4.5.6 below (see (4.5.26)). This is the a ertion of
(4.5.18).
The solution to the Black-Scholes-Merton equation (4.5.14) with terminal
condition (4.5.15) and boundary conditions (4.5.17) and (4.5.18) is

c(t, x) = xN(d+(T - t, x)} - Ke [-] r [(] T [-t)] N(d-(T - t, x)}, 0 ::; t < T, x > 0,
(4.5.19)
where



(4.5.20)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-178-0.png)





N(y) =



(4.5.21)





(4.5.22)





4.9.



4.5.5


delta, which is


Because both N and N' are always positive, delta is always positive and theta
is always negative. Another of the Greeks is gamma, which is


160 4 Stochastic Calculus

(4.5.25)

must be

market account.

difference,


is zero at the moment t when we set up these positions.
If the stock price were to instantaneously fall to x0 as shown in Figure 4.5.1
and we do not change our positions in the stock or money market account,
then the value of the option we hold would fall to c(t, x0) and the liability
due to our short position in stock would decrease to xocx(t, xi)· Our total
portfolio value, including M in the money market account, would be
c(t,xo) - xocx(t,xl) + M = c(t,xo) - cx(t, xl)(xo   - xi) - c(t,xl).

This is the difference at xo between the curve y = c(t, x) and the straight
line y = cx (t, xl)(x - xi) + c(t, xi) in Figure 4.5.1. Because this difference is
positive, our portfolio benefits from an instantaneous drop in the stock price.
On the other hand, if the stock price were to instantaneously rise to x2
and we do not change our positions in the stock or money market account,
then the value of the option would rise to c(t, x2 ) and the liability due to our



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-179-0.png)
4.5 Black-Scholes-Merton Equation 161

short position in stock would increase to x2cx(t, xi ). Our total portfolio value,
including M in the money market account, would be



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-180-0.png)

Fig. 4.5.1. Delta-neutral position.





The portfolio we have set up is said to be delta-neutral and long gamma.
The portfolio is long gamma because it benefits from the convexity of c(t, x)
as described above. If there is an instantaneous rise or an instantaneous fall in
the stock price, the value of the portfolio increases. A long gamma portfolio
is profitable in times of high stock volatility.
"Delta-neutral" refers to the fact that the line in Figure 4.5.1 is tangent
to the curve y = c(t, x). Therefore, when the stock price makes a small move,
the change of portfolio value due to the corresponding change in option price
is nearly offset by the change in the value of our short position in the stock.
The straight line is a good approximation to the option price for small stock
price moves. If the straight line were steeper than the option price curve at the
starting point x1, then we would be short delta; an upward move in the stock
price would hurt the portfolio because the liability from the short position
in stock would rise faster than the value of the option. On the other hand, a
downward move would increase the portfolio value because the option price
would fall more slowly than the rate of decrease in the liability from the short
stock position. Unless a trader has a view on the market, he tries to set up
portfolios that are delta-neutral. If he expects high volatility, he would at the
same time try to choose the portfolio to be long gamma.
The portfolio described above may at first appear to offer an arbitrage
opportunity. When we let time move forward, not only does the long gamma
position offer an opportunity for profit, but the positive investment in the


162 4 Stochastic Calculus


money market account enhances this opportunity. The drawback is that theta,
the derivative of c( t, x) with respect to time, is negative. As we move forward
in time, the curve y = c( t, x) is shifting downward. Figure 4.5.1 is misleading
because it is drawn with t fixed. In principle, the portfolio can lose money
because the curve c(t, x) shifts downward more rapidly than the money market
investment and the long gamma position generate income. The essence of the
hedging argument in Subsection 4.5.3 is that if the stock really is a geometric
Brownian motion and we have determined the right value of the volatility
u, then so long as we continuously rebalance our portfolio, all these effects
exactly cancel!
Of course, a ets are not really geometric Brownian motions with constant
volatility, but the argument above gives a good first approximation to reality.
It also highlights volatility as the key parameter. In fact, the mean rate of
return a of the stock does not appear in the Black-Scholes-Merton equation
(4.5.14). From the point of view of no-arbitrage pricing, it is irrelevant how
likely the stock is to go up or down because a delta-neutral position is a
hedge against both possibilities. What matters is how much volatility the
stock has, for we need to know the amount of profit that can be made from
the long gamma position. The more volatile stocks offer more opportunity for
profit from the portfolio that hedges a long call position with a short stock
position, and hence the call is more expensive. The derivative of the option
price with respect to the volatility u is called vega, and it is positive. As
volatility increases, so do option prices in the Black-Scholes-Merton model.


4.5.6 Put-Call Parity

A forward contract with delivery price obligates its holder to buy one share
K
of the stock at expiration time T in exchange for payment At expiration,
K.
the value of the forward contract is S(T) - Let f(t, x) denote the value of
K.
the forward contract at earlier times t E [0, T] if the stock price at time t is
S(t) = X.
We argue that the value of a forward contract is given by

f(t, x) = x - e [-] r [(T-] t [) ] K. (4.5.26)

If an agent sells this forward contract at time zero for f(t, S(O)) = S(O) e-rT K, he can set up a static hedge, a hedge that does not trade except
at the initial time, in order to protect himself. Specifically, the agent should
purchase one share of stock. Since he has initial capital S(O) - e-rT K from
the sale of the forward contract, this requires that he borrow e-rT K from the
money market account. The agent makes no further trades. At expiration of
the forward contract, he owns one share of stock and his debt to the money
market account has grown to so his portfolio value is S(T) - exactly the
K, K,
value of the forward contract. Because the agent has been able to replicate the
payoff of the forward contract with a portfolio whose value at each time t is


4.5 Black-Scholes-Merton Equation 163

e-r(T-t) K, this must be the value at each time of the forward contract.
S(t) This is f(t, S(t)), where f(t, x) is defined by (4.5.26).
The forward price of a stock at time t is defined to be the value of K that
causes the forward contract at time t to have value zero (i.e., it is the value
of K that satisfies the equation S(t) - e [-] r [(T-] t) K = 0). Hence, we see that in
a model with a constant interest rate, the forward price at time t is

For t = er [(T-] t)S(t). (4.5.27)
( )

Note that the forward price is not the price (or value) of a forward contract.
For 0 � t � T, the forward price at time t is the price one can lock in at time
t for the purchase of one share of stock at time T, paying the price (settling)
at time T. No money changes hands at the time the price is locked in.
Let us consider this situation at time t = 0. At that time, one can lock
in a price For(O) = errs(O) for purchase of the stock at time T. Let us do
this, which means we set K = erTS(O) in (4.5.26). The value of this forward
contract is zero at time t = 0, but as soon as time begins to move forward,
the value of the forward contract changes. Indeed, its value at time t is
f(t, S(t)) = S(t) - ert 8(0).

Finally, let us consider a European put, which pays off (K - S(T)) [+ ] at
time T. We observe that for any number x, the equation
x - K = (x - K) [+ ]           - (K - x) [+ ] (4.5.28)

holds. Indeed, if x ; K, then (x - K) [+ ] = x - K and (K - x) [+ ] = 0. On the
other hand, if x � K, then (x-K) [+ ] = 0 and -(K -x) [+ ] = -(K -x) = x-K.
either case, the right-hand side of 4.5.28 equals the left-hand side. We
In ( )
denote by p(t, x) the value of the European put at time t if the time-t stock
price is S(t) = x. Similarly, we denote by c(t, x) the value of the European
call expiring at time T with strike price K and by f(t, x) the value of the
forward contract for the purchase of one share of stock at time T in exchange
for payment K. Equation (4.5.28) implies

f(T, S(T)) = c(T, S(T)) - p(T, S(T));

the payoff of the forward contract agrees with the payoff of a portfolio that
is long one call and short one put. Since the value at time T of the forward
contract agrees with the value of the portfolio that is long one call and short
one put, these values must agree at all previous times:
f(t,x) = c(t, x) - p(t, x), x ; O, O         - t         - T. (4.5.29)

If this were not the case, one could at some time t either sell or buy the
portfolio that is long the forward, short the call, and long the put, realizing
an instant profit, and have no liability upon expiration of the contracts. The
relationship ( 4.5.29) is called put-call parity.


164 4 Stochastic Calculus


Note that we have derived the put-call parity formula (4.5.29) without ap­
pealing to the Black-Scholes-Merton model of a geometric Brownian motion
for the stock price and a constant interest rate. Indeed, without any a ump­
tions on the prices except sufficient liquidity that permits one to form the
portfolio that is long one call and short one put, we have put-call parity. If
we make the a umption of a constant interest rate r, then f(t, x) is given by
(4.5.26). If we make the additional a umption that the stock is a geometric
Brownian motion with constant volatility a > 0, then we have also the Black­
Scholes-Merton call formula (4.5.19). We can then solve (4.5.29) to obtain the
Black-Scholes-Merton put formula

p(t, x) = x(N(d+(T - t, x)) - 1) - Ke [-] r [(T-t) ] (N(d-(T - t, x)) - 1)


where d±(T - t, x) is given by (4.5.20).


4.6 Multivariable Stochastic Calculus


4.6.1 Multiple Brownian Motions


Definition 4.6.1. A d-dimensional Brownian motion is a process

W(t) = (WI (t), . . ., Wd(t))

with the following properties.
{i} Each Wi(t) is a one-dimensional Brownian motion.
{ii} If i f. j, then the processes Wi(t) and Wj(t) are independent.
Associated with a d-dimensional Brownian motion, we have a filtration :F(t),
t 0, such that the following holds.

 {iii} (Information accumulates) For 0 � s < t, every set in :F(s) is also in
:F(t).
{iv} (Adaptivity) For each t 0, the random vector W(t) is :F(t)-measurable.

               (v) (Independence of future increments) For 0 - t u, the vector of
<
increments W(u) - W(t) is independent of :F(t).

Although we have defined a multidimensional Brownian motion to be a
vector of independent one-dimensional Brownian motions, we shall see in Ex­
ample 4.6.6 how to build correlated Brownian motions from this.
Because each component Wi of a d-dimensional Brownian motion is a
one-dimensional Brownian motion, we have the quadratic variation formula

[Wi, Wi](t) = t, which we write informally as

= Ke-r(T-t) N( -d_ (T - t, x)) - xN( -d+(T - t, x)), (4.5.30)


4.6 Multivariable Stochastic Calculus 165

However, if i f. j, we shall see that independence of Wi and Wi implies

[Wi, Wi](t) = 0, which we write informally as


All the increments appearing in the sum of cross-terms are independent of
one another and all have mean zero. Therefore,
n-1
Var(Crr) = IECfr = IE L [Wi(tk+I) - Wi(tk)] [2 ] [Wi(tk+I) - Wj(tk)t
k=O

But [Wi(tk+1) - Wi(tk)] [2 ] and [Wi(tk+I) - Wj(tk)] [2 ] are independent of one
another, and each has expectation (tk+1 - tk)· It follows that
n-1 n-1
Var(Crr) = L(tk+l - tk) [2 ]    - **I** I I · L(tk+1 - tk) = **I** I I · [T] .
k=O k=O

As **I** II II --+ 0, we have Var( Crr) --+ 0, so Crr converges to the constant IECrr =
0.


4.6.2 ltO-Doeblin Formula for Multiple Processes

To keep the notation as simple as possible, we write the Ito formula for two
processes driven by a two-dimensional Brownian motion. In the obvious way,
the formula generalizes to any number of processes driven by a Brownian
motion of any number (not necessarily the same number) of dimensions.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-184-0.png)
166 4 Stochastic Calculus



Let X(t) and Y(t) be Ito processes, which means they are processes of the
form
X(t) X(O) + 81(u)du+ uu(u)dW1(u) + 0'12(u)dW2(u),
###### =
1 [t ] 1 [t ] 1 [t ]



Y(t) Y(O) + 82(u) du + 0'21(u) dW1(u) + 0'22(u) dW2(u).
###### =
1 [t ] 1 [t ] 1 [t ]



The integrands 8i(u) and O'i;(u) are a umed to be adapted processes. In
differential notation, we write
dX(t) 81 (t) dt + uu (t) dW1 (t) + u12(t) dW2(t), (4.6.1)
###### =
dY(t) 82(t) dt + u21 (t) dW1 {t) + u22(t) dW2(t). {4.6.2)
###### =

The Ito integral J� u11 ( u) dW1 ( u) a umulates quadratic variation at rate
u�1(t) per unit time, and the Ito integral J� u12(u)dW2(u) accumulates
quadratic variation at rate u�2(t) per unit time. Because both of these in­
tegrals appear in X(t), the process X(t) accumulates quadratic variation at
rate u�1 (t) + u�2{t) per unit time:

[X,X]{t) = (u�1(u) +u�2(u)) du.
1 [t ]

We may write this equation in differential form as



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-185-0.png)

In a similar way, we may derive the differential formulas
dY(t) dY(t) (u�1 {t) + u�2{t)) dt,
###### =
dX(t) dY(t) (uu(t)u21(t) + 0'12(t)u22(t)) dt.
###### =



{4.6.4)
(4.6.5)



Equation {4.6.5) says that, for every T � 0,




[X, Y](T) (uu(t)u21(t) + 0'12(t)u22(t)) dt.
###### =
1T



{4.6.6)



=
The term [X, Y](T) on the left-hand side is defined as follows. Let II
{to, t1, . . .,tn} be a partition of [0, T) (i.e., 0 to < t1 < - · · < tn T)
###### and set up the sampled cross variation = =
n-1
L [X(tk+l) - X(tk)] [Y(tk+I) - Y(tk)]. (4.6.7)
k=O


4.6 Multivariable Stochastic Calculus 167


Now let the number of partition points n go to infinity as the length of the
longest subinterval 111711 = maxo<k<n-I (tk+1 - tk) goes to zero. The limit of
the sum in (4.6.7) is [X, Y] (T). [T] h [i] s limit is given by the right-hand side of
(4.6.6). The proof of this a ertion is similar to the proof of Lemma 4.4.4,
with the additional feature that we must use the fact that [WI, W2](t) = 0.
We omit the details.
The following theorem generalizes the It6-Doeblin formula of Theorem
4.4.6. The justification, which we omit, is similar to that of Theorem 4.4.6.

Theorem 4.6.2 (Two-dimensional ItO-Doeblin formula). Let l(t, x, y)
be a function whose partial derivatives ft, lx, ly, lxx, lxy1 lyx1 and IYY are
defined and are continuous. Let X(t) and Y(t) be Ito processes as discussed
above. The two-dimensional lt6-Doeblin formula in differential form is

dl(t, X(t), Y(t))
=ft(t, X(t), Y(t)) dt + lx(t, X(t), Y(t)) dX(t) + ly(t, X(t), Y(t)) dY(t)
1
+2lxx (t, X(t), Y(t)} dX(t) dX(t) + lxy (t, X(t), Y(t)} dX(t) dY(t)
1
(4.6.8)


Before discussing formula (4.6.8), we rewrite it, leaving out t wherever
possible, to obtain the same formula in the more compact notation

dl(t, X, Y) = It dt + lx dX + ly dY
1 1
+2,lxx dX dX + lxy dX dY + 2,IYY [dY dY. ] (4.6.9)

The right-hand side of (4.6.9) is the Taylor series expansion of I out to sec­
ond order. The full expansion would have the additional second-order terms
Itt dt dt, ltx dt dX, [and ] - lty dt dY, [but ] dt dt, dt dX, [and ] dt dY [are zero. The ]
!
Taylor series expansion actually has two mixed partial terms, �lxy dX dY and

- [ly] x [dY dX. ][For functions ] I [whose second partial derivatives exist and are ]
continuous, lxy = lyx, and so we have combined these terms into the single
term lxy dX dY in (4.6.9).
The differentials dX, dY, dX dX, dX dY, and dY dY appearing in (4.6.9)
are given by (4.6.1)-(4.6.5). Making these substitutions and then integrating
(4.6.9), we obtain the It6-Doeblin formula in integral form:

l(t, X(t), Y(t)) - I(O, X(O), Y(O))
= [au (u)lx(u, X(u), Y( u)) + <121 (u)ly(u, X(u), Y(u)) J dW1 (u)
###### lo [t ]

+ 1 [t ] [a12(u)lx (u, X(u), Y(u)) + <T22(u)ly(u, X(u), Y(u))] dW2(u)

+"21yy(t, X(t), Y(t)) dY(t) dY(t).


168 4 Stochastic Calculus



+ !t(u, X(u), Y(u))

[
###### lo [t ]
+6 (u)fx(u, X(u), Y(u)) + 6l2(u)jy(u, X(u), Y(u))
1 2 2

1 2 2
(4.6.10)
]
+(uu(u)u21(u) + D"12(u)u22(u))/xy(u, X(u), Y(u))
+2(u21(u) + u22(u))/yy(u, X(u), Y(u)) du.
+2(uu (u) + u12(u))fxx(u, X( u), Y(u))



The right-hand side of this equation has one ordinary (Lebesgue) integral with
respect to du and two Ito integrals, one with respect to dW1(u) and the other
with respect to dW2(u). All terms have precise mathematical meanings. This
equation demonstrates why it is preferable to work with differential notation,
such as in (4.6.9).

Corollary 4.6.3 (Ito product rule). Let X(t) and Y(t) be Ito processes.
Then
d(X(t)Y(t)) X(t) dY(t) + Y(t) dX(t) + dX(t) dY(t).
=

PROOF: In (4.6.9), take f(t, x, y) = xy, so that ft = 0, fx = y, /y = x,
fxx = 0, fxy = 1, and /yy = 0. 0



Corollary 4.6.3 (Ito product rule). Let X(t) and Y(t) be Ito processes.
Then
d(X(t)Y(t)) X(t) dY(t) + Y(t) dX(t) + dX(t) dY(t).
=



4.6.3 Recognizing a Brownian Motion


A Brownian motion W(t) is a martingale with continuous paths whose
quadratic variation is [W, W](t) t. It turns out that these conditions char­
=
acterize Brownian motion in the sense of the following theorem.

Theorem 4.6.4 (Levy, one dimension). Let M(t), t 0, be a martin­
;
gale relative to a filtration :F(t), t 2 0. Assume that M(O) 0, M(t) has
=
continuous paths, and [M, M](t) t for all t ; 0. Then M(t) is a Brownian
=
motion.

IDEA OF THE PROOF: A Brownian motion is a martingale whose increments
are normally distributed. The surprising feature of Levy's Theorem is that
the a umptions do not say anything about normality, and yet implicit in the
conclusion is the a ertion that M(t) is normally distributed.
The method used to establish normality is to first check that in the deriva­
tion of the ltO-Doeblin formula, Theorem 4.4.1, for Brownian motion, the only
properties of Brownian motion that were used are a umed in this theorem: a
continuous process with quadratic variation [M, M](t) t. Therefore, the ltO­
=
Doeblin formula may be applied to M with the result that, for any function
f(t, x) whose derivatives exist and are continuous,
df(t, M(t)) = ft(t, M(t)) dt + fx(t, M(t)) dM(t) + 2fxx(t, M(t)) dt. (41 .6. 11 )


4.6 Multivariable Stochastic Calculus 169



The last term uses the fact that dM(t) dM(t) = dt. In integrated form, (4.6.11)
is



f(t, M(t)) = f(O, M(O)) + 1



t

[ft (s, M(s)) + �fxx(s, M(s))] ds



+
1



t
fx(s, M(s)) dM(s). (4.6.12)



Because M ( t) is a martingale, the stochastic integral J� f x ( s, M ( s)) dM ( s) is
also. (See Exercise 4.1 for the case of a simple integrand; the general case
follows from this exercise upon pa age to the limit.) At t = 0, this stochastic
integral takes the value zero, and so its expectation is always zero. Taking
expectations in (4.6.12), we obtain



1
JEf(t, M(t)) = f(O, M(O)) + IE [ft (s, M(s)) + 2fxx(s, M(s))] ds. (4.6.13)



We fix a number u and define



f(t, x) exp ux - u [2] t
=    - }·
###### {



Then ft(t, x) = -�u [2] f(t, x), fx(t, x) = uf(t, x), and fxx(t, x) = u [2] f(t, x). In
particular,
1
ft(t, x) + 2fxx(t, x) = 0.

For this function f(t, x), the second term on the right-hand side of (4.6.13) is
zero, and that equation becomes

JEexp { uM(t) - �u [2] t} = 1.

In other words, we have the moment-generating function formula

JEeuM(t) e�u [2] t.
=

This is the moment-generating function for the normal distribution with mean
zero and variance t (see (3.2.13)). Hence, that is the distribution that M(t)
must have.
0

The idea used to justify Theorem 4.6.4 can be combined with the two­
dimensional It6-Doeblin formula used to show independence. In particular,
we have the following two-dimensional version of Levy's Theorem.

Theorem 4.6.5 (Levy, two dimensions). Let M1(t) and M2(t), t - 0,
be martingales relative to a filtration F(t), t � 0. Assume that for i = 1, 2,
we have Mi(O) = 0, Mi(t) has continuous paths, and [Mi, Mi](t) = t for all
t � 0. If, in addition, [M1, M2](t) = 0 for all t � 0, then M1 (t) and M2(t) are
independent Brownian motions.


170 4 Stochastic Calculus


IDEA OF THE PROOF: The one-dimensional Levy Theorem, Theorem 4.6.4,
implies that M1 and M2 are Brownian motions. To show independence, we
examine the joint moment-generating function.
Let f(t, x, y) be a function whose derivatives are defined and continuous.
The two-dimensional ItO-Doeblin formula implies that
df(t, M1, M2) = ft dt + fx dM1 + /y dM2
1
+?Jxx dM1 dM1 + /xy dM1 dM2 + /yy dM2 dM2
1 1
= ft dt + fx dM1 + /y dM2 + ?Jxx dt + ?.IYY dt,

where we have used the a umptions [MI> MI](t) = t, [M2, M2](t) = t, and

[MI> M2](t) = in their equivalent form dM1(t) dM1(t) = dt, dM2(t) dM2(t) =
dt, and dM1(t) dM2(t) = 0. We integrate both sides to obtain
J(t, M1(t), M2(t))



= f(O, M1 (0), M2(0)) + !t(s, M1 (s), M2(s)) + �fxx(s, M1(s), M2(s))
###### 1 [t ] [



+�/yy(s, M1(s), M2(s)) ds
###### ]



+ fx(s, M1(s), M2(s)) dM1(s) + /y(x, M1(s), M2(s)) dM2(s).
###### 1 [t ] 1 [t ]



The last two terms on the right-hand side are martingales, starting at zero at
time zero, and hence having expectation zero. Therefore,



'Ef(t, M1(t), M2(t))



= /(0, M1(0), M2(0)) + 'E tt(s, M1(s), M2(s)) + �fxx(s, M1(s), M2(s))
###### 1 [t ] [



+�/yy(s, M1(s), M2(s)) ds. (4.6.14)
###### ]



We now fix numbers u1 and u2 and define



f ( t, X, y) = exp { U1X + U2Y - � ( U� + un t .
###### }




We conclude that
u2f(t, x, y). fxx(t, x, y) = uU(t, x, y), and /yy(t, x, y) = u�f(t, x, y). For this
function f(t, x, y), the second term on the right-hand side of (4.6.14) is zero.
Then ft(t, x, y) = - H u� + uDJ(t, x, y), fx(t, x, y) = ud(t, x, y), /y(t, x, y) =



'Eexp {u1M1(t) + u2M2(t) - � (u� + u�)t = 1,
}



which gives us the moment-generating function formula


4.6 Multivariable Stochastic Calculus 171



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-190-0.png)

define


we see that S2(t) is a geometric Brownian motion with mean rate of return
a2 and volatility 0"2.
The Brownian motions W1(t) and W3(t) are correlated. According to Ito's
product rule (Corollary 4.6.3),
d(W1(t)W3(t)) = W1(t) dW3(t) + W3(t) dW1(t) + dW1(t) dW3(t)
= W1(t) dW3(t) + W3(t) dW1(t) + pdt.
Integrating, we obtain



W1(t)W3(t) = W1(s) dW3(s) + W3(s) dW1(s) + pt.
###### 1 [t ] 1 [t ]



The Ito integrals on the right-hand side have expectation zero, so the covari­
ance of W1(t) and W3(t) is
1E[W1(t)W3(t)] = pt.



Because both W1(t) and W3(t) have standard deviation v'f the number p is
the correlation between W1 ( t) and W3 ( t). The case of non constant correlation

4.17. 0
p is presented in Exercise


172 4 Stochastic Calculus


4. 7 Brownian Bridge


We conclude this chapter with a the discussion of the Brownian bridge. This
is a stochastic process that is like a Brownian motion except that with prob­
ability one it reaches a specified point at a specified positive time. We first
discuss Gaussian processes in general, the cla to which the Brownian bridge
belongs, and we then define the Brownian bridge and present its properties.
The primary use for the Brownian bridge in finance is as an aid to Monte
Carlo simulation. We make no use of it in this text.


4.7.1 Gaussian Processes


Definition 4.7.1. A Gaussian process X(t), t 0, is a stochastic process

                       that has the property that, for arbitrary times 0 < h < t2 < - · · < tn, the
random variables X(t1), X(t2), . . . X(tn) are jointly normally distributed.

The joint normal distribution of a set of vectors is determined by their
means and covariances. Therefore, for a Gaussian process, the joint distribu­

                             -                              - .
tion of X (h), X ( t2),, X ( tn) is determined by the means and covariances of
these random variables. We denote the mean of X(t) by m(t), and, for s � 0,
t � 0, we denote the covariance of X(s) and X(t) by c(s, t); i.e.,

m(t) = JEX(t), c(s, t) = lE [( [X(s) - m(s)][) ] ( [X(t) -] m [(t)] }] [. ]

Example 4. 7.2 (Brownian motion). Brownian motion W(t) is a Gaussian pro­
cess. For 0 < h < t2 < - · · < tn, the increments

h = W(h), !2 = W(t2) - W(h), . . ., In = W(tn) - W(tn-d

are independent and normally distributed. Writing
2 n
W(h) = h, W(t2) = Llj, . . ., W(tn) = L lj,
j=l j=l

we see that the random variables W ( t 1 ), W ( t2), . . ., W ( tn) are jointly normally
distributed. These random variables are not independent. It is the increments
of Brownian motion that are independent. Of course, the mean function for
Brownian motion is
m(t) = JEW(t) = 0.
We may compute the covariance by letting 0 � s � t be given and noting that

c(s, t) = lE[W(s)W(t)]
lE [W(s) (W(t) - W(s) + W(s)}]
###### =
= lE [W(s) (W(t) - W(s)}] + lE [W [2] (s)] .


4. 7 Brownian Bridge 173



Because W ( s) and W ( t) - W ( s) are independent and both have mean zero,

we see that IE[W(s)(W(t) - W(s))] 0. The other term, IE[W [2] (s)], is the
variance of W(s), which is s. We conclude that = c(s, t) s when 0 � s � t.
###### Reversing the roles of s and t, we conclude that c(s, t) = t when 0 � t � s. In
general, the covariance function for Brownian motion is then =



Because W ( s) and W ( t) - W ( s) are independent and both have mean zero,



c(s, t) s l\ t,
###### =



where s 1\ t denotes the minimum of s and t. 0
Example 4. 7.3 (Ito integml of a deterministic integmnd). Let Ll(t) be a non­
random function of time, and define



I(t) Ll(s) dW(s),
###### = 1 [t ]



where W(t) is a Brownian motion. Then J(t) is a Gaussian process, as we now
show.
In the proof of Theorem 4.4.9, we showed that, for fixed u E JR., the process



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-192-0.png)



(4.7.1)



The right-hand side is the moment generating function for a normal random
variable with mean zero and variance J� Ll [2 ] ( s) ds. Therefore, this is the dis­
tribution of I(t).
Although we have shown that J(t) is normally distributed, verification
that the process is Gaussian requires more. We must verify that, for 0 < h <
t2 < - · · < tn, the random variables J(ti), I(t2), . . ., I(tn) are jointly normally
distributed. It turns out that the increments



I(t!) - 1(0) I( h), I(t2) - I( h), . . ., I(tn) - I(tn-l)
###### =



are normally distributed and independent, and from this the joint normality
of I( h), I(t2), . . ., I(tn) follows by the same argument as used in Example
4.7.2 for Brownian motion.
We show that, for 0 < t1 < t2, the two random increments J(ti) - 1(0)
I(tt) and J(t2) - I(h) are normally distributed and independent. The ar­=
gument we provide can be iterated to prove this result for any number of
increments. For fixed u2 E JR., the martingale property of Mu2 implies that


174 4 Stochastic Calculus



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-193-0.png)







The right-hand side is the product of the moment-generating function for
a normal random variable with mean zero and variance J� [1 ] ..1 [2] (s) ds and the
moment-generating function for a normal random variable with mean zero and
variance ft [t] 12 ..1 [2] (s) ds. It follows that I(t1) and I(t2) - I(t1) must have these
distributions, and because their joint moment-generating function factors into
this product of moment-generating functions, they must be independent.
The covariance of I(t1) and I(t2) can be computed using the same trick
as in Example 4. 7.2 for the covariance of Brownian motion. We have


4. 7 Brownian Bridge 175



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-194-0.png)





In



are jointly normal because W(h), . . ., W(tn), W(T) are jointly normal. Hence,
the Brownian bridge from 0 to 0 is a Gaussian process. Its mean function is
easily seen to be



m(t) JEX(t) lE[W(t) - W(T) 0.
= = =
          - ]



For s, t E (0, T), we compute the covariance function


176 4 Stochastic Calculus



c(s, t)
= lE w(s) - W(T) w(t) - W(T)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-195-0.png)







increases for 0 : t : and then decreases for t : T. In Example 4.7.3,

          -          - :
the variance of I(t) = J; Ll(u) dW(u) is J; Ll [2] (u) du, which is nondecreasing
in t. However, we can obtain a process with the same distribution as the
Brownian bridge from 0 to 0 as a scaled stochastic integral. In particular,
consider



consider

1
Y(t) = (T - t)         - dW(u), 0 : t < T.
1t 0 T - u
The integral
1
I(t) =              - dW(u)
1t o T - u



(4.7.4)


4. 7 Brownian Bridge 177



is a Gaussian process of the type discussed in Example 4.7.3, provided t T
<
so the integrand is defined. For 0 < h < t2 < - · · < tn < T, the random
variables
Y(tt) = (T - tt)I(tt), Y(t2) = (T - t2)I(t2), . . ., Y(tn) = (T - tn)I(tn)
are jointly normal because I(tt), I(t2), . . ., I(tn) are jointly normal. In partic­
ular, Y is a Gaussian process.
The mean and covariance functions of I are
m1(t) = 0,





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-196-0.png)

<
that



Then









In general,


[O,T).


Note that, as t T, this variance converges to 0. In other words, as t t
t
T, the random process Y(t), which always has mean zero, has a variance
that converges to zero. We did not initially define Y(T), but this observation
suggests that it makes sense to define Y(T) = 0. If we do that, then Y(t)
is continuous at t = T. We summarize this discussion with the following
theorem.

(4.7.5)


178 4 Stochastic Calculus


Theorem 4. 7 .6. Define the process


variance functions


of Y(t), which is

-1
1o [t ] T - u

T


and covariance function

When s ::; t, we may write this as

          - t



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-197-0.png)
4o 7 Brownian Bridge 179



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-198-0.png)

















= Oo


180 4 Stochastic Calculus


We conclude that the normal random variables Z1, . . ., Zn are independent,
and we can write down their joint density, which is





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-199-0.png)
















4.7 Brownian Bridge 181



Now



Tj-1 - Tj = (T - tj-d - (T - tj) [= ] tj - tj-1,
and so this last expression is equal to



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-200-0.png)






### }









whose determinant is I1j=1 -!:;· Multiplying /z(t,), ...,Z(t,.)(Zt, . . .,Zn) by this
determinant and using the change of variables worked out above, we obtain
the density for xa--+b(tt), . . . 'xa--+b(tn),


182 4 Stochastic Calculus



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-201-0.png)

is the transition density for Brownian motion.


4. 7.5 Brownian Bridge as a Conditioned Brownian Motion

The joint density (4.7.6) for xa-+b(h), . . .,xa-+b(tn) permits us to give one
more interpretation for the Brownian bridge from a to b on [0, T]. It is a
Brownian motion W(t) on this time interval, starting at W(O) = a and
conditioned to arrive at b at time T (i.e., conditioned on W(T) = b).
Let 0 = t0 < t1 < t2 < - · · < tn < T be given. The joint density of
W(h), . . .,W(tn), W(T) is
n
fw(t.), ...,W(tn),W(T) (x�, . . .,Xn, b) = p(T- tn, Xn, b) II p(tj - tj-11 Xj-11 Xj ),
j=1
(4.7.7)
where W(O) = xo = a. This is because p(t1 - to, xo, xi) = p(t1, a, xi) is the
density for the Brownian motion going from W(O) = a to W(tl) = x1 in the
time between t = 0 and t = t1• Similarly, p(t2 - t1,x1,x2) is the density for
going from W(tl) = x1 to W(t2) = x2 between time t = t1 and t = t2. The
joint density for W(ti) and W(t2) is then the product
p(t1,a,xl)p(t2 - t1,x1,x2).

Continuing in this way, we obtain the joint density (4.7.7). The marginal
density of W(T) is p(T, a, b). The density of W(h), . . .,W(tn) conditioned on
W(T) = b is thus the quotient


4.8 Summary 183


t.

(4.8.2)

t

(4.8.3)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-202-0.png)
184 4 Stochastic Calculus


These a ertions appear in Theorem 4.3.1. Note that the quadratic variation
(4.8.3) is computed path-by-path and the result may depend on the path,
whereas the variance (4.8.2) is an average over all paths. In differential nota­
tion, we write (4.8.1) as
dl(t) = Ll(t) dW(t)
and ( 4.8.3) as

dl(t) dl(t) = Ll [2] (t) dW(t) dW(t) = Ll [2] (t) dt.



An Ito process (Definition 4.4.3) is a process of the form



X(t) = X(O) + Ll(u) dW(u) + e(u) du, (4.8.4)
###### 1 [t ] 1 [t ]



where X(O) is nonrandom and Ll(u) and e(u) are adapted stochastic pr<r
cesses. According to Lemma 4.4.4, the quadratic variation accumulated by X
up to time t is
(X, X](t) = Ll [2] (u) du. (4.8.5)
###### 1 [t ]



In differential notation, we write (4.8.4) as



dX(t) = Ll(t) dW(t) + e(t) dt



and ( 4.8.5) as



dX(t) dX(t) = (Ll(t) dW(t) + e(t) dt) [2 ]



= Ll [2] (t) dW(t) dW(t) + 2Ll(t) e(t) dW(t) dt + e [2] (t) dt dt
= Ll [2] (t) dt,



where we have used the multiplication table

dW(t) dW(t) = dt, dW(t) dt = dtdW(t) = 0, dtdt = 0.

Suppose X and Y are Ito processes with differentials

dX(t) = e1 (t) dt + uu(t) dWt (t) + u12(t) dW2(t),
dY(t) = e2(t) dt + u21(t) dWt(t) + u22(t) dW2(t),

where WI and w2 are independent Brownian motions. Then

dX(t) dX(t) = (u�1(t) + u�2(t)) dt,
dX(t) dY(t) = (uu(t)u2t(t) + O't2(t)u22(t)) dt,
dY(t) dY(t) = (u�1(t) + u�2(t)) dt.



(4.8.6)
(4.8.7)


(4.8.8)
(4.8.9)
(4.8.10)



Equations (4.8.8)-(4.8.10) can be obtained by multiplying the equations
(4.8.6) and (4.8.7) for dX(t) and dY(t) and using the multiplication table


and



4.8 Summary 185


dW;(t) dW;(t) dt, dWi(t) dt dtdW;(t) 0, dtdt 0,
###### = = = =



(4.8.11)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-204-0.png)

for a constant p E [- 1, 1], then p would be the correlation between W1(t) and
W2(t) i.e., IE[W1(t)W2(t)] pt).
(
Now suppose f(t, x, y is a function of the time variable = t and two dummy
)
variables x and y. The multidimensional ItO-Doeblin formula Theorem 4.6.2)
(
says

df t, X(t), Y(t))
(
ft t, X(t), Y(t)) dt + fx t, X(t), Y(t)) dX(t) + /y(t, X(t), Y(t)) dY(t)
( (
###### =
t, X(t), Y(t)) dX(t) dX(t) + /xy t, X(t), Y(t)) dX(t) dY(t)
( (
�fxx 1
(4.8.12)


Replacing all the differentials on the right-hand side of ( 4.8.12) by their formu­
las (4.8.6)-(4.8.10) and integrating, one obtains a formula for the stochastic
process f(t, X(t), Y(t)) as the sum of /(0, X(O), Y(O)), an ordinary integral
with respect to time, an Ito integral with respect to dW1, and an Ito integral
with respect to dW2.
There are two important special cases of (4.8.12). If the second process
is not present, (4.8.12) reduces to the ItO-Doeblin formula for one process
Y
(Theorem 4.4.6):

+"2/yy(t, X(t), Y(t)) dY(t) dY(t).



1
df(t, X(t)) ft(t, X(t)) dt + fx(t, X(t)) dX(t) + 2/xx(t, X(t)) dX(t) dX(t).
###### =



If both X and Y are present and (t, x, y) xy, then (4.8.12) gives us Ito ['] s
###### product rule Corollary 4.6.3): =
( f



Corollary 4.6.3):

d(X(t)Y(t)) X(t) dY(t) + Y(t) dX(t) + dX(t) dY(t).
###### =



Using the ItO-Doeblin formula, we can derive the Black-Scholes-Merton
partial differential equation. This was done in Section 4.5, and that section is
summarized here. Let the stock price S(t) be a geometric Brownian motion:



S(t)

dS(t) aS(t) dt + aS(t) dW(t).
###### =



Let c(t, S(t)) be the price at time t E [0, T] of a European call paying S T ­
( ( )
K) [+ ] at expiration time T. Suppose we sell this call for X(O) c(O, S O at
( ))
time zero and, starting with initial capital X(O), invest in a stock and a money =


186 4 Stochastic Calculus

market a ount paying a constant rate of interest r. If Ll(t) is the number of
shares of stock held by the portfolio at time t, then

dX(t) = Ll(t) dS(t) + r(X(t)         - Ll(t)S(t)) dt.

We compute the differential of the discounted portfolio value e-rt X(t), the
differential of the discounted call price e-rtc(t, S(t)), and set these two equal.
This results in the delta-hedging rule (4.5.11),



Ll(t) = Cx(t, S(t)),

and the Black-Scholes-Merton partial differential equation (4.5.14),
1 2 2
Ct(t, x) + rxcx(t, x) + X Cxx(t, x) = rc(t, x).
20'



(4.8.13)



In addition to satisfying this partial differential equation, the function c( t, x)
must satisfy the boundary conditions


X-+00

The function satisfying these conditions is (see (4.5.19))

c(T, x) = (x - K)+, c(t, O) = O, lim [c(t, x) - (x - e-r(T-t)K)] = 0.



c(t, x) = xN(d+(T - t, x)) - Ke [-] r [(T-t) ] N(d-(T - t, x)), (4.8.14)



where
d±(T, x) = log + (r± T .
###### [ ; ]



Using the function given by (4.8.14), if one starts with initial capital
X(O) = c(O, S(O)) and uses the delta-hedging rule (4.8.13), then at every
time t, X(t) = c(t, S(t)). In particular, at the final time, the value of the
hedging portfolio is X(T) = c(T, S(T)) = (S(T) - K) [+ ] almost surely. The
short position in the European call has been hedged.
Levy's Theorem, Theorem 4.6.4, says that if M(t) is a continuous mar­
tingale starting at M(O) = 0 and if [M, M](t) = t (i.e., dM(t) dM(t) = dt),
then M(t) is a Brownian motion. If M1(t) and M2(t) are two such processes
and [M1, M2](t) = 0 (i.e., dM1(t) dM2(t) = 0), then M1(t) and M2(t) are
independent Brownian motions (Theorem 4.6.5). One can use this theorem to
construct independent Brownian motions from correlated Brownian motions
and vice versa (see Exercise 4.13).
A Gaussian process X(t) is one for which X(tt), X(t2), . . . X(tn) are jointly
normally distributed whenever 0 < t1 < t2 < - · · < tn (Definition 4.7.1).
Because the joint distribution of jointly normal random variables is deter­
mined by means, variances, and covariances, the distribution of a Gaussian
process is determined by its mean function m(t) = JEX(t) and covariance
function c(s, t) = Cov(X(s), X(t)). Brownian motion is a Gaussian process


4.9 Notes 187

with m(t) = 0 and c(s, t) = s 1\ t (Example 4.7.2). If Ll(u) is nonran­
dom, then I(t) [= ] [J; ] Ll(u) dW(u) is a Gaussian process with m(t) [= ] 0 [and ]

10.7.5).


Notes
4.9


(4.3.1)


The integral can be defined under the weaker condition


but then is not guaranteed to be a martingale. It is still a local martingale, a
topic discussed in advanced books on stochastic calculus (e.g., [101]). In this
text, we do not consider local martingales. We work only under the condition
(4.3.1), and every Ito integral we encounter is a martingale.
Brownian motion was introduced to finance by Bachelier [6]. Samuelson

[143], [145] presents the argument that geometric Brownian motion is a good
model for stock prices. The application of stochastic calculus to finance began

r
Ll2(t) < oo almost surely
fo



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-206-0.png)
188 4 Stochastic Calculus


with the work of Merton [121]. (The paper [121] and many other papers by
Merton that use stochastic calculus in finance are collected in Merton [124].)
The Black-Scholes-Merton formula is based on the geometric Brownian motion
model for stock prices. However, no-arbitrage pricing theory has now moved
far beyond this a umption. As seen in this and subsequent chapters, this
theory and the accompanying risk-neutral pricing formula can be applied in
the presence of a time-varying random volatility, a time-varying random mean
rate of return, and a time-varying random interest rate.
Many finance books, including (in order of increasing mathematical diffi­
culty) Hull [87], Dothan [54], and Duffie [56], include sections on Ito's integral
and the lt6-Doeblin formula. Some other books on dynamic models in finance
are Cox and Rubinstein [43], Huang and Litzenberger [86], Ingersoll [91], and
Jarrow [97]. A comprehensive text is Wilmott [164]. Some good references for
practitioners are Baxter and Rennie [8] (reviewed in [134]), Bjork [11] (re­
viewed in [135]), and Musiela and Rutkowski [126] (reviewed in [134]). More
mathematical texts on stochastic calculus with applications to finance are
Lamberton and Lapeyre [105] (reviewed in [134]) and Steele [150] (reviewed
in [136]). Other texts on stochastic calculus are Chung and Williams [36],
Karatzas and Shreve [101], 0ksendal [129], and Protter [133]. Karatzas and
Shreve [102] is a sequel to [101] that focuses on finance. Protter [133] is the
easiest place to learn about stochastic calculus for processes with jumps, and
this is not at all easy. We introduce this topic in Chapter 11.
No-arbitrage pricing theory and the accompanying risk-neutral pricing for­
mula is predicated on the a umption that there is no arbitrage in the market.
An arbitrage is defined to be a trading strategy which begins with zero capi­
tal and at a later time has positive capital with positive probability without
having any risk of loss. Absence of arbitrage is similar to but different from
the efficient market hypothesis, which asserts that technical analysis of stock
prices is of no value. This hypothesis a erts that patterns in stock prices may
be useful to estimate the parameters of the distribution of future returns,
but they do not provide clues to whether the next price movement will be
up or down. In particular, technical analysis does not permit one to outper­
form the market. This hypothesis could be violated in a way which permits
one to outperform the market with high probability without actually admit­
ting arbitrage because there is still a nonzero probability of underperforming
the market. This is sometimes called statistical arbitmge. An empirical study
supporting the efficient market hypothesis is Fama [64], which also discusses
distributions that fit stock prices better than geometric Brownian motion. A
criticism of the efficient market hypothesis is provided by LeRoy [106], and a
recent paper that finds long-range dependence (but not much) in stock price
data is Willinger, Taqqu, and Teverovsky [163]. A provocative article on the
source of stock price movements is Black [14].
Geometric fractional Brownian motion has been proposed as an alternative
model for stock prices because it has fatter tails than geometric Brownian
motion. One can assume such a model and compute the prices of derivative


4.10 Exercises 189


sec [urities as their expected discounted payoffs, but the model is inconsistent ]
with the usual delta-hedging formula. Indeed, geometric fractional Brownian
motion violates the efficient market hypothesis so strongly that it admits
arbitrage (not just "statistical arbitrage" but actual arbitrage). An example of
this is provided by Rogers [138]. Further examples of arbitrage and a market­
trading restriction that prevents arbitrage in such markets are provided by
Cheridito [33].
The Vasicek model of Example 4.4.10 is taken from [154]. The Cox­
Ingersoll-Ross model of Example 4.4.11 is due to [41], where the distribution
of the interest rate process in the model is provided.
The derivation of the Black-Scholes-Merton formula in Section 4.5 is sim­
ilar to that originally given by Black and Scholes [17] but also relies heavily
on the no-arbitrage idea appearing in Merton [122]. It is well-documented
that the three men cooperated on development of the option-pricing formula,
and in recognition of this the 1997 Nobel Prize in Economics was awarded
to Scholes and Merton. (Black died in 1995, and the prize is not awarded
posthumously). In this text, the role of all three men is acknowledged by the
terminology Black-Scholes-Merton option-pricing formula. Even though ge­
ometric Brownian motion is a less than perfect model for stock prices, the
Black-Scholes-Merton pricing formula for vanilla options (i.e., European calls
and puts) seems not to be terribly sensitive to deficiencies in the model.
The pa age from discrete to continuous time in the model of evolution of
the portfolio value, which is touched upon in Subsection 4.5.1, is given a more
detailed treatment by Duffie and Protter [60]; see also Exercise 4.10.


4. 10 Exercises


Exercise 4.1. Suppose M(t), 0 � t � T, is a martingale with respect to some
filtration :F(t), 0 � t � T. Let Ll(t), 0 � t � T, be a simple process adapted to
:F(t) (i.e., there is a partition II = {to, t1, . . ., tn} of [0, T] such that, for every
j, Ll(tj) is :F(t3)-measurable and Ll(t) is constant in t on each subinterval

[tj, tJ+1)). For t E [tk, tk+I), define the stochastic integral
k-1
I(t) = L Ll(tj)[M(tj+I) - M(tj)] + Ll(tk)[M(t) - M(tk)].
j=O

We think of M(t) as the price of an a et at time t and Ll(t3) as the number
of shares of the a et held by an investor between times t3 and tj+I· Then I(t)
is the capital gains that accrue to the investor between times 0 and t. Show
that I(t), 0 � t � T, is a martingale.

Exercise 4.2. Let W(t), 0 � t - T, be a Brownian motion, and let :F(t),
0 t � T, be an a ociated filtration. Let Ll(t), 0 � t � T, be a nonmndom

 simple process (i.e., there is a partition II = { t0, t1, . . ., tn} of [0, T] such that


190 4 Stochastic Calculus



for every j, Ll(tj) is a nonrandom quantity and Ll(t) = Ll(tj) is constant in t
on the subinterval [tj, ti+I)). For t E [tk, tk+l], define the stochastic integral
k-1
I(t) = L ..1(tj)[W(tj+1) - W(tj)] + Ll(tk)[W(t) - W(tk)].
j=O

(i) Show that whenever 0 : s < t : T, the increment I(t) - I(s) is inde­
pendent of :F(s). (Simplification: If s is between two partition points, we
can always insert s as an extra partition point. Then we can relabel the
partition points so that they are still called to, t1, . . .,tn, but with a larger
value of n and now with s = tk for some value of k. Of course, we must set
Ll(s) = ..1(tk_1) so that ..1 takes the same value on the interval [s, tk+1)
as on the interval [tk_1, s). Similarly, we can insert t as an extra parti­
tion point if it is not already one. Consequently, to show that I(t) - I(s)
is independent of :F( s) for all 0 : s < t : T, it suffices to show that
I(tk) -I(tt) is independent of :F(tt) whenever tk and tt are two partition
points with tt < tk. This is all you need to do.)
(ii) Show that whenever 0 ::=; s < t ::=; T, the increment I(t) -I(s) is a normally
distributed random variable with mean zero and variance J: ..1 [2] (u) du.
(iii) Use (i) and (ii) to show that I(t), 0 : t : T, is a martingale.
(iv) Show that I [2] (t) - J� ..1 [2] (u) du, 0 ::=; t ::=; T, is a martingale.

Exercise 4.3. We now consider a case in which Ll(t) in Exercise 4.2 is simple
but random. In particular, let to = 0, t1 = s, and t2 = t, and let ..1(0)
be nonrandom and Ll(s) = W(s). Which of the following a ertions is true?
Justify your answers.
(i) I(t) - I(s) is independent of :F(s).
(ii) I(t) - I(s) is normally distributed. (Hint: Check if the fourth moment is
three times the square of the variance; see Exercise 3.3 of Chapter 3.)
(i) IE[I(t)I:F(s)] = I(s).
(iv) IE [I [2] (t) - J� ..1 [2] (u)du :F(s)] = I [2] (s) - J; ..1 [2] (u)du.
j

Exercise 4.4 (Stratonovich integral). Let W(t), t � 0, be a Brownian
motion. Let T be a fixed positive number and let II = {t0,t1, . . .,tn} be a
partition of [0, T] (i.e., 0 = t0 < t1 < - · · < tn = T). For each j, define
tj = to be the midpoint of the interval [tj, ti+1l·
(i) Define the half-sample quadratic variation corresponding to II to be
n-1
QII/2 [= ] L (W(tj) - W(tj)t
j=O

Show that Qn; has limit �T as III I --+ 0. (Hint: It suffices to show that
2
lEQn;2 = �T and limiii -+O Var(Qn;2) = 0.)


4.10 Exercises 191


(ii) Define the Stratonovich integral of W(t) with respect to W(t) to be

T n-1
W(t) o dW(t) = lim L W(tj) (W(t3+d       - W(tj)). (4.10.1)
111 1 [-+] 0 i=O

In contrast to the Ito integral J0 [T ] W(t) dW(t) = � W [2] (T) - �T of (4.3.4),
which evaluates the integrand at the left endpoint of each subinterval

[tj, ti+1], here we evaluate the integrand at the midpoint tj. Show that


(Hint: Write the approximating sum in (4.10.1) as the sum of an approx­
imating sum for the Ito integral J0 [T ] W(t) dW(t) and Q11;2• The approxi­
mating sum for the Ito integral is the one corresponding to the partition
0 = to < t0 < t1 < ti <   - · · < t�_1 < tn = T, not the partition II.)

Exercise 4.5 Solving the generalized geometric Brownian motion
(
equation) . Let S(t) be a positive stochastic process that satisfies the gener­
alized geometric Brownian motion differential equation (see Example 4.4.8)

dS(t) = a(t)S(t) dt + a(t)S(t) dW(t), (4.10.2)

where a(t) and a(t) are processes adapted to the filtration :F(t), t 2 0, a o­
ciated with the Brownian motion W(t), t 2 0. In this exercise, we show that
S(t) must be given by formula (4.4.26) (i.e., that formula provides the only
solution to the stochastic differential equation (4.10.2)). In the process, we
provide a method for solving this equation.
(i) Using (4.10.2) and the ltO-Doeblin formula, compute dlog S(t). Simplify
so that you have a formula for dlog S(t) that does not involve S(t).
(ii) Integrate the formula you obtained in (i), and then exponentiate the answer to obtain (4.4.26).

Exercise 4.6. Let S(t) = S(O) exp aW(t) + a - �a [2] t} be a geometric
Brownian motion. Let p be a positive constant. Compute d ( SP ( t)), the differ­{ ( )
ential of S(t) raised to the power p.

Exercise 4.7. (i) Compute dW4(t) and then write W4(T) as the sum of an
ordinary (Lebesgue) integral with respect to time and an Ito integral.
(ii) Take expectations on both sides of the formula you obtained in (i), use
the fact that IEW [2] (t) = t, and derive the formula IEW4(T) = 3T [2]   (i) Use the method of (i) and (ii) to derive a formula for IEW6(T).

Exercise 4.8 (Solving the Vasicek equation) . The Vasicek interest rate
stochastic differential equation ( 4.4.32) is


192 4 Stochastic Calculus
dR(t) = (a -,BR(t)) dt + u dW(t),

where a,,B, and u are positive constants. The solution to this equation is
given in Example 4.4.10. This exercise shows how to derive this solution.
(i) Use (4.4.32) and the Ito-Doeblin formula to compute . Simplify
d(e.B [t ] R(t) )
it so that you have a formula for that does not involve
d(e.B [t ] R(t)) R(t).
(ii) Integrate the equation you obtained in (i) and solve for to obtain
R(t)
(4.4.33).


Exercise 4.9. For a European call expiring at time with strike price
T K,
the Black-Scholes-Merton price at time if the time-t stock price is is
t, x,
c(t, x) = xN(d+(T- t, x)) -Ke-r [(] T- [t) ] N(d-(T- t, x)),



where



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-211-0.png)

N(y)



The purpose of this exercise is to show that the function satisfies the Black­
c
Scholes-Merton partial differential equation
1
+ + 2 2 0 :     - 0, (4.10.3)
Ct(t, x) rxcx(t, x) 2 [17 ] x Cxx(t, x) = rc(t, x), t < T, x



the
terminal condition

                       limc(t,x) = (x -K) [+], x O,x =/: K,
t [t] T
and the
boundary conditions



(4.10.4)



limc(t,x) = O, lim [c(t,x) - (x-e-r [(] T- [t)] K)] = O, O :S t < T. (4.10.5)
x.j.O x-+oo



Equation ( 4.10.4) and the first part of ( 4.10.5) are usually written more simply
but less precisely as

                       - 0
c(T,x) = (x- K) [+], x
and
0) 0, 0 :
c(t, = t : T.
For this exercise, we abbreviate simply and
c(t, x) as c d±(T - t, x) as
simply d±.


(i) Verify first the equation



4.10 Exercises 193


(4.10.6)



(ii) Show that Cx This is the delta of the option. (Be careful! Re­
= N(d+)·
member that is a function of
d+ x.)
(iii) Show that





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-212-0.png)



limit is



(4.10.7)


194 4 Stochastic Calculus


This formula can be rearranged to become

(4.10.8)


(4.10.10)


(4.10.11)


tion
(4.10.12)

it is

dition
(4.10.13)
The first term is the cost of rebalancing in the stock, and the second is the
cost of rebalancing in the money market account. If the sum of these two
terms is not zero, then money must either be put into the position or can
be taken out as a by-product of rebalancing. The point is that when the two
processes Llk and n are used to describe the evolution of the portfolio value



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-213-0.png)
4.10 Exercises 195


xk, then two equations, (4.10.12) and (4.10.13), are required rather than the
single equation (4.10.8) when only the process Llk is used.
Finally, we note that we may rewrite the discrete-time self-financing con­
dition ( 4.10.13) as

Sk(Llk+l - Llk) + (Sk+t - Sk)(Llk+l - Llk)
+Mk(rk+I - rk) + (Mk+l - Mk)(rk+l - rk) = o. (4.10.14)

This is suggestive of the continuous-time self-financing condition

S(t) dLl(t) + dS(t) dLl(t) + M(t) dF(t) + dM(t) dT(t) = 0, (4.10.15)

which we derive below.

(i) In continuous time, let M(t) = ert be the price of a share of the money
market account _at time t, let Ll(t) denote the number of shares of stock
held at time t, and let F(t) denote the number of shares of the money
market account held at time t, so that the total portfolio value at time t
is
X(t) = Ll(t)S(t) + F(t)M(t). (4.10.16)
Using (4.10.16) and (4.10.9), derive the continuous-time self-financing con­
dition (4.10.15).
A common argument used to derive the Black-Scholes-Merton partial dif­
ferential equation and delta-hedging formula goes like this. Let c(t, x) be the
price of a call at some time t if the stock price at that time is S(t) = x. Form
a portfolio that is long the call and short Ll(t) shares of stock, so that the
value of the portfolio at time t is N(t) = c(t, S(t)} - Ll(t)S(t). We want to
choose Ll(t) so this is "instantaneously riskless," in which case its value would
have to grow at the interest rate. Otherwise, according to this argument, we
could arbitrage this portfolio against the money market account. This means
we should have dN(t) = rN(t) dt. We compute the differential of N(t) and
get

dN(t) = Ct(t, S(t)) dt + cx(t, S(t)) dS(t)
1
+2cxx(t, S(t)) dS(t) dS(t) - Ll(t) dS(t)



= [cx(t, S(t)) - Ll(t)] dS(t)



+ ct (t, S(t)} + �a2S2(t)cxx(t, S(t)) dt. (4.10.17)
###### [ ]



In order for this to be instantaneously riskless, we must cancel out the dS(t)
term, which contains the risk. This gives us the delta-hedging formula Ll(t) =
Cx ( t, S ( t)} . Having chosen Ll ( t) this way, we recall that we expect to have
dN(t) = rN(t) dt, and this yields


196 4 Stochastic Calculus


But



(4.10.18)


(4.10.19)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-215-0.png)

(ii) Now replace (4.10.17) by its corrected version (4.10.21) and use the
continuous-time self-financing condition you derived in part (i) to derive
(4.10.18).

Exercise 4.11. Let

c(t, x) = xN(d+ ( [T]        - t, x) )        - Ke-r(T-t)N(d- (T        - t, x))


4.10 Exercises 197


denote the price for a European call, expiring at time T with strike price K,
where



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-216-0.png)
198 4 Stochastic Calculus

where p is a stochastic process taking values strictly between -1 and 1. Define
processes W1(t) and W2(t) such that
B1(t) = W1(t),


n-1
j=O

appearing in (4.4.5). Indeed,


that
n-1
j=O
is approximately equal to
n-1
j=O


explanation for the equation

111 1--. [o ]
i=O



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-217-0.png)
4.10 Exercises



Define



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-218-0.png)

so that



:E



{4.10.23)







define









(i) Show that, for each i, Bi is a Brownian motion.


200 4 Stochastic Calculus

(ii) Show that dBi(t) dBk(t) = Pik(t), where


(
nian motions with


matrix

m



which means that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-219-0.png)

m m
aii(t)aik(t) = aii(t)aik(t) = 8ik, (4.10.26)
L L
i=l j=l


4.10 Exercises 201


where we define
if i = k,
0ik = 0 1 if i k,
{ -1
to be [the so-called ] [Kronecker delta. ] [Show that there exist ] [m ] [independent ]
Brownian motions W1(t), . . ., Wm(t) such that





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-220-0.png)



has means, variances, and covariance

Mi(f) = IE [Xi(to + f) - Xi(to)l :F(to)] = 6lif for i = 1, 2, (4.10.28)
l/i(f) = IE (Xi(to + f) - Xi(to)) [2] :F(to)     - M'f(f)
]

= u?f [ for i = 1, 2, 1 (4.10.29)
C(f) = IE [ (xl (to + f) - xl (to)) (X2(to + f) - X2(to)) :F(to)]
I
-Ml(f)M2(f) = PD"ID"2f· (4.10.30)


202 4 Stochastic Calculus


In particular, conditioned on :F(to), the correlation between the incre­
ments X1(to + f) - X1(to) and X2(to + f) - X2(to) is





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-221-0.png)





(4.10.31)

(4.10.32)





(4.10.33)


(4.10.34)




(4.10.35)

where we set Pu(t) = P22(t) = 1 and P12(t) = p21(t) = p(t). (Hint: You
should define the martingales


4.10 Exercises 203



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-222-0.png)









sion is



f
€.).0


has variances and covariance

f) = + f) -       - Ml{f)
###### Vi( IE [ (Xi(to Xi(to)) [2] jF(to)]
= a-r(to)f + O(f) for i = 1, 2, (4.10.38)
C(f) IE [ + f) - + f) = (X1(to XI(to)) (X2(to X2(to)) IF(to)]
-M1(f)M2(f) (4.10.39)
(to)a2(to)f +
= p(to)al o( f) .


204 4 Stochastic Calculus


(vi) Show that
(4.10.40)



In other words, for small values of € - 0, conditioned on :F( to), the corre­
lation between the increments X1 (to + €) - X1 (to) and X2(to + €) - X2(to)
is approximately equal to p(to), and this approximation becomes exact as



0.
€ t



Exercise 4.18. Let a stock price be a geometric Brownian motion
dS(t) = aS(t) dt + aS(t) dW(t),



and let r denote the interest rate. We define the market price of risk to be
a - r
0=
-­(1



(1
and the state price density process to be
((t) = exp OW(t) - r + �o [2] t }·
{ - ( )



(i) Show that
d( t = -O( t dW t r((t) dt.
( ) ( ) ( ) (ii) Let X denote the value of an investor's portfolio when he uses a portfolio
process Ll(t). From (4.5.2), we have
dX(t) = r X(t) dt + Ll(t)(a       - r)S(t) dt + Ll(t)aS(t) dW(t).



Show that ( t X t is a martingale. (Hint: Show that the differential
( ) ( )
d ( t X t has no dt term.)
( ( ) ( ))
(iii) Let T - 0 be a fixed terminal time. Show that if an investor wants to
begin with some initial capital X O and invest in order to have portfolio
( )
value V(T) at time T, where V(T) is a given :F(T)-measurable random
variable, then he must begin with initial capital
X(O) = IE[((T)V(T)].



In other words, the present value at time zero of the random payment
V(T) at time T is IE[((T)V(T)]. This justifies calling ( t the state price
( )
density process.



Exercise 4.19. Let W t be a Brownian motion, and define
( )



where



B t sign(W(s)) dW s,
( ) ( )
###### =lo [t ]

1 if 0,
Sign X �
. ( ) { X = -1 if X < 0.


4.10 Exercises 205

(i) Show that B(t) is a Brownian motion.
( [ii) ][Use Ito's product rule to compute ] d[B(t)W(t)] . Integrate both sides of
the resulting equation and take expectations. Show that lE[B(t)W(t)] 0
=
(i.e., B(t) and W(t) are uncorrelated).
( [i][) ] Verify that
dW [2] (t) 2W(t) dW(t) + dt.
=
(iv) Use Ito's product rule to compute d[B(t)W [2] (t)] . Integrate both sides of
the resulting equation and take expectations to conclude that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-224-0.png)



In





The usual statement of this formula a umes that the function !" ( x) is defined
for every x E and is a continuous function of x. In fact, the formula still
lR
holds if there are finitely many points x where f"(x) is undefined, provided
that f'(x) is defined for every x E lR and is a continuous function of x (and
provided that lf"(x)l is bounded so that the integral J0 [T ] f"(W(t)) dt is de­
fined). However, if f'(x) is not defined at some point, naive application of the
ItO-Doeblin formula can give wrong answers, as this problem demonstrates.
(i) Let K be a positive constant, and define f(x) (x - K) [+] . Compute f'(x)
=
and f"(x). Note that there is a point x where f'(x) is not defined, and
note also that f"(x) is zero everywhere except at this point, where f"(x)
is also undefined.
(ii) Substitute the function f(x) = (x-K) [+ ] into (4.10.42), replacing the term

  - J: f"(W(t)) dt by zero since !" is zero everywhere except at one point,
where it is not defined. Show that the two sides of this equation cannot
be equal by computing their expected values.
(iii) To get some idea of what is going on here, define a sequence of functions
{! n} ;= 1 by the formula
0 if x < K -- .2n' 1.
f n (x) = !!(x -2 K) [2 ] + .!(x - K) + .2 8n 1. if K - .2n -1. < x < K + .- 2n ' 1.
### { - K if � K +
X X


206 4 Stochastic Calculus



Show that
l�(x) =



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-225-0.png)

I� (

(iv) Show that



lR














4. 10 Exercises 207


Let us define the to be
local time of the Brownian motion at K


where 6 K is the so-called "Dirac delta function" at K.) For a fixed n, the
expression J:[ ll(K _ .12 [n ] ' K + .12 [n ] ) ( W ( t)) dt measures how much time between time
and time T the Brownian motion spends in the band of length centered at
0 K. As n --+ oo, this has limit zero because the width of the band is approaching
zero. However, before taking the limit, we multiply by n, and now it is not
clear whether the limit will be zero, +oo, or something in between. The limit
will, of course, be random; it depends on the path of the Brownian motion.

Show that if the path of the Brownian motion stays strictly below on
(v) K
the time interval [0, T], we have LK(T) 0.
=
(vi) We may solve (4.10.44) for LK (T), using the fact that W(O) = 0 and

    - 0, to obtain
K


LK (T) (W(T) -    - ll( [K],oo) dW(t). (4.10.45)
= K) [+ ] 1 [T ] (W(t))

From this, we see that LK (T) is never +oo. Show that we cannot have
LK (T) 0 almost surely. In other words, for some paths of the Brownian
=
motion, we must have LK (T) > 0. (It turns out that the paths that reach
level are those for which LK (T) > 0.)
K

Exercise 4.21 (Stop-loss start-gain paradox). Let S(t) be a geometric
Brownian motion with mean rate of return zero. In other words,


dS(t) aS(t) dW(t),
=

where the volatility a is constant. We a ume the interest rate is 0.
r =
Suppose we want to hedge a short position in a European call with strike
price and expiration date T. We a ume that the call is initially out of the
K
money (i.e., S(O) Starting with zero capital (X(O) 0), we could try
< K). =
the following portfolio strategy: own one share of the stock whenever its price
strictly exceeds and own zero shares whenever its price is or less. In
K, K
other words, we use the hedging portfolio process
Ll(t) = ll(K,oo) (S(t)) .

The value of this hedge follows the stochastic differential equation



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-226-0.png)
208 4 Stochastic Calculus

dX(t) = Ll(t) dS(t) + r(X(t) - Ll(t)X(t)) dt,

and since r = 0 and X(O) = 0, we have

X(T) = a 1 [T ] H(K,oo)(S(t))S(t) dW(t). (4.10.46)


Executing this hedge requires us to borrow from the money market to
buy a share of stock whenever the stock price rises across level K and sell
the share, repaying the money market debt, when it falls back across level
K. Recall that we have taken the interest rate to be zero. The situation
(
we are describing can also occur with a nonzero interest rate, but it is more
complicated to set up.) At expiration, if the stock price S(T) is below K,
there would appear to have been an even number of crossings of the level
K, half in the up direction and half in the down direction, so that we would
have bought and sold the stock repeatedly, each time at the same price K,
and at the final time have no stock and zero debt to the money market. In
other words, if S(T) < K, then X(T) = 0. On the other hand, if at the final
time S(T) is above K, we have bought the stock one more time than we sold
it, so that we end with one share of stock and a debt of K to the money
market. Hence, if S(T) > K, we have X(T) = S(T) - K. If at the final time
S(T) = K, then we either own a share of stock valued at K and have a money
market debt K or we have sold the stock and have zero money market debt.
In either case, X(T) = 0. According to this argument, regardless of the final
stock price, we have X(T) = (S(T) - K) [+] . This kind of hedging is called a
stop-loss start-gain strategy.

(i) Discuss the practical aspects of implementing the stop-loss start-gain
strategy described above. Can it be done?
ii Apart from the practical aspects, does the mathematics of continuous­
( )
time stochastic calculus suggest that the stop-loss start-gain strategy can
be implemented? In other words, with X(T) defined by (4.10.46), is it
really true that X(T) = (S(T) - K) [+] ?


5


Risk-Neutral Pricing


5. 1 Introduction


In the binomial a et pricing model of Chapter 1 of Volume we showed
I,
how to price a derivative security by determining the initial capital required
to hedge a short position in the derivative security. a two-period model,
In
this method led to the six equations (1.2.2), (1.2.3), and (1.2.5)-(1.2.8) in six
unknowns in Volume Three of these unknowns were the position the hedge
I.
should take in the underlying a et at time zero, the position taken by the
hedge at time one if the first coin toss results in H, and the position taken
by the hedge at time one if the first coin toss results in T. The three other
u owns were the value of the derivative security at time zero, the value of
the derivative security at time one if the first coin toss results in H, and the
value of the derivative security at time one if the first coin toss results in T.
The solution to these six equations provides both the value of the derivative
security at all times and the hedge for the short position at all times, regardless
of the outcome of the first coin toss.
In Theorem 1.2.2 of Volume I, we discovered a clever way to solve these six
equations in six unknowns by first solving for the derivative security values
using the risk-neutral probabilities and in (1.2.16) and then computing
Vn p ij
the hedge positions from (1.2.17). Equation (1.2.16) says that under the risk­
neutral probabilities, the discounted derivative security value is a martingale.
In Section 4.5 of this volume, we repeated the first part of this program. To
determine the value of a European call, we determined the initial capital re­
quired to set up a portfolio that with probability one hedges a short position
in the derivative security. Subsection 4.5.3, in which we equated the evolu­
tion of the discounted portfolio value with the evolution of the discounted
option value, provides the continuous-time analogue of solving the six equa­
tions (1.2.2), (1.2.3), and (1.2.5)-(1.2.8) of Volume I. From that process, we
obtained the delta-hedging rule (4.5.11) and we obtained the Black-Scholes­
Merton partial differential equation (4.5.14) for the value of the call.


210 5 Risk-Neutral Pricing


Now we execute the second part of the program. In this chapter, we dis­
cover a clever way to solve the partial differential equation (4.5.14) using
a risk-neutral probability measure. After solving this equation, we can then
compute the short option hedge using ( 4.5.11).
To accomplish this second part of the program, we show in Section 5.2
how to construct the risk-neutral measure in a model with a single underlying
security. This step relies on Girsanov's Theorem, which is presented in Sec­
tion 5.2. Risk-neutral pricing is a powerful method for computing prices of
derivative securities, but it is fully justified only when it is accompanied by a
hedge for a short position in the security being priced. In Section 5.3, we pro­
vide the conditions under which such a hedge exists in a model with a single
underlying security. Section 5.4 generalizes the ideas of Sections 5.2 and 5.3 to
models with multiple underlying securities. Furthermore, Section 5.4 provides
conditions that guarantee that such a model does not admit arbitrage and
that every derivative security in the model can be hedged.


5.2 Risk-Neutral Measure


5.2.1 Girsanov's Theorem for a Single Brownian Motion

In Theorem 1.6.1, we began with a probability space (il, :F, IP') and a nonnega­
tive random variable Z satisfying IEZ = 1. We then defined a new probability
measure lP by the formula



JP(A) = Z(w) dP(w) for all A E :F. (5.2. 1)
l



Any random variable X now has two expectations, one under the original
probability measure_!, which we denot� lEX, and the other under the new
probability measure IP', which we denote lEX. These are related by the formula
EX = IE[XZ]. (5.2.2)

If IP'{Z > 0} = 1, then IP' and lP agree which sets have probability zero and
(5.2.2) has the companion formula

(5.2.3)


This is supposed to remind us that Z is like a ratio of these two probability
measures. The reader may wish to review Section of Volume I, where
3.1



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-229-0.png)
5.2 Risk-Neutral Measure 211


this concept is discussed in a finite probability model. In the case of a finite
probability model, we actually have

JP(w)
Z(w) = JP(w) " (5.2.4)

If we multiply both sides of (5.2.4) by JP(w) and then sum over w in a set A,
we obtain
JP(A) = L Z(w)P(w) for all A c n. (5.2.5)

wE A

In a general probability model, we cannot write (5.2.4) because JP(w) is typi­
cally zero for each individual w, but we can write an analogue of (5.2.5). This
is (5.2.1).
Example 1.6.6 shows how we can use this change-of-measure idea to move
the mean of a normal random variable. In particular, if X is a standard normal
random variable on a probability space ( n, F, JP), () is a constant, and we define



wE A



Z = exp {-OX ###### �()2},



then under the probability measure lP given_by (5.2.1), the random variable
Y = X +0 is standard normal. In par..ticular, lEY = 0, whereas lEY = lEX +0 =
0. By changing the probability measure, we have changed the expectation of
Y.
In this section, we perform a similar change of measure in order to change
a mean, but this time for a whole process rather than for a single random
variable. To set the stage, suppose we have a probability space (n,F,JP) and
a filtration F(t), defined for 0 � t � T, where T is a fixed final time. Suppose
further that Z is an almost surely positive random variable satisfying IEZ = 1,
and we define lP by (5.2.1). We can then define the Radon-Nikodym derivative
process
Z(t) = IE[ZIF(t)], 0 � t � T. (5.2.6)
This process in discrete time is discussed in Section 3.2 of Volume I. The
Radon-Nikodym derivative process (5.2.6) is a martingale because of iterated
conditioning (Theorem 2.3.2(iii)): for 0 � s � t � T,

IE[Z(t)IF(s)] = IE[IE[ZIF(t)JIF(s)] = IE[ZIF(s)] = Z(s). (5.2.7)

Furthermore, it has the properties presented in the following two lemmas,
which are continuous-time analogues of Lemmas 3.2.5 and 3.2.6 of Volume I.

Lemma 5.2.1. Let t satisfying 0 - t - T be given and let Y be an F(t)­
measurable random variable. Then
lEY = IE[YZ(t)]. (5.2.8)


212 5 Risk-Neutral Pricing



PROOF: We use (5.2.2), the unbiasedness of conditional expectations (2.3.25),
the property "taking out what is known" (Theorem 2.3.2(ii)), and the defini­
tion of Z(t) to write
fEy = IE[YZ] = IE[IE[YZj.F(t)l] = IE [YIE[ZIF(t)l] = IE[YZ(t)]. D

Lemma 5.2.2. Let s and t satisfying 0 � s � t � T be given and let Y be an
F(t)-measurable random variable. Then



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-231-0.png)










###### }



(5.2.11)


(5.2.12)




and assume that [1 ]



5.2 Risk-Neutral Measure 213


(5.2.13)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-232-0.png)

= f' (X(t)) dX(t) + f" (X(t)) dX(t) dX(t)

              
= e [X] { [t) ]       - 6l(t) dW(t) - �6l [2] (t) dt + �e [X{t)] 6J [2] (t) dt
( )
= -6l(t)Z(t) dW(t).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-232-1.png)



Z(t) = Z(O) - 6l(u)Z(u) dW(u). (5.2.14)
###### 1 [t ]



Z(t) = lE[Z(T)IF(t)] = IE[ZIF(t)], 0 : t : T.


and is a martingale. This is ( 4.3.1) imposed in the construction of Ito integrals.


214 5 Risk-Neutral Pricing


tingale under IP'.


This shows that W(t) is a martingale under JP>. The proof is complete. 0

The probability measures IP' and IP' in Girsanov's Theorem are equivalent
(i.e., they agree about which sets have probability zero and hence about which
sets have probability one) . This is because IP'{ Z > 0} = 1; see Definition 1.6.3
and the discussion following it. In the remainder of this section, we set_ up
an a et price model in which IP' is the actual probability measure and IP' is
the risk-neutral measure. We want these probabilities to agree about what is
possible and what is impossible, and they do. In the discrete-time binomial
model of Volume I, the actual and risk-neutral probability measures agree
about which moves are possible (i.e., they both give positive probability to
an up move, positive probability to a down move, and the sizes (but not the
probabilities) of the up and down moves are the same whether we are working
under the actual probability measure or the risk-neutral probability measure) .
The set of possible asset price paths is a tree in the binomial model, and both
the actual probability measure and the risk-neutral probability measure are
based on the same tree. In the continuous-time model, there are infinitely
many possible paths, and this agreement about what is possible and what is
not possible is the equivalence of Definition 1.6.3.


5.2.2 Stock Under the Risk-Neutral Measure

Let W(t), 0 : t : T, be a Brownian motion on a probability space (il, F, IP'),
and let F(t), 0 : t : T, be a filtration for this Brownian motion. Here T is a
fixed final time. Consider a stock price process whose differential is
dS(t) = a(t)S(t) dt + a(t)S(t) dW(t), 0 : t : T. (5.2.15)

The mean rate of return a( t) and the volatility a( t) are allowed to be adapted
processes. We a ume that, for all t E [0, T], a(t) is almost surely not zero.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-233-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-233-1.png)
5.2 Risk-Neutral Measure 215



This stock price is a generalized geometric Brownian motion (see Example
4.4.8, in particular, (4.4.27)), and an equivalent way of writing (5.2.15) is (see
( 4.4.26))



S(t) = S(O) exp a(s) dW(s) + ( a(s) - �a2(s) ds . (5.2.16)
###### {1 [t ] 1 [t ] ) }



In addition, suppose we have an adapted interest rate process R( t). We
define the discount process



D(t) = e [-J� ][R(s)ds ]
and note that

dD(t) = -R(t)D(t) dt.



(5.2.18)



(5.2.17)



To obtain (5.2.18) from (5.2.17), we can define I(t) J; R(s) ds so that
dl(t) = R(t) dt and dl(t) dl(t) = 0. We introduce the function f(x) = e [-][x],

       for which f'(x) = f(x), f"(x) = f(x), and then use the Ito-Doeblin formula
to write
dD(t) = df(I(t))
= f' ( I(t)) dl(t) + � f" ( I(t)) dl(t) dl(t)

         = f(I(t))R(t) dt
= -R(t)D(t) dt.

Observe that although D(t) is random, it has zero quadratic variation. This
is because it is "smooth." It has a derivative, namely D'(t) = -R(t)D(t), and
one does not need stochastic calculus to do this computation. The stock price
S(t) is random and has nonzero quadratic variation. It is "more random"
than D(t). If we invest in the stock, we have no way of knowing whether the
next move of the driving Brownian motion will be up or down, and this move
directly affects the stock price. Hence, we face a high degree of uncertainty.
On the other hand, consider a money market account with variable interest
rate R(t), where money is rolled over at this interest rate. If the price of
a share of this money market account at time zero is 1, then the price of
a share of this money market account at time t is ef [� ][R(s) ds ] = If we
invest in this account, we know the interest rate at the time of the investment
and hence have a high degree of certainty about what the return will be
over a short period of time. Over longer periods, we are less certain because
the interest rate is variable, and at the time of investment, we do not know
the future interest rates that will be applied. However, the randomness in
the model affects the money market account only indirectly by affecting the
interest rate. Changes in the interest rate do not affect the money market
account instantaneously but only when they act over time. (Warning: The
money market account is not a bond. For a bond, a change in the interest


216 5 Risk-Neutral Pricing



rate can have an instantaneous effect on price.) Unlike the price of the money
market account, the stock price is susceptible to instantaneous unpredictable
changes and is, in this sense, "more random" than D(t). Our mathematical
model captures this effect because 8(t) has nonzero quadratic variation, while
D(t) has zero quadratic variation.
The discounted stock price process is

D(t)8(t) 8(0) exp a(s)dW(s) + a(s) - R(s) - a [2] (s) ds,
= {lot 1t      ###### }
( ) (5.2.19)
and its differential is
d(D(t)8(t)) (a(t) - R(t))D(t)8(t) dt + a(t)D(t)8(t) dW(t)
=
a(t)D(t)8(t) [B(t) dt + dW(t)], (5.2.20)
=

where we define the market price of risk to be


as


a martingale.

=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-235-0.png)
5.2 Risk-Neutral Measure 217


(5.2.24)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-236-0.png)

Our agent has two investment options: (1) a money market account with
rate of return R(t), and (2) a stock with mean rate of return R(t) under J.
Regardless of how the agent invests, the mean rate of return for his portfolio
will be R(t) under J, and hence the discounted value of his portfolio, D(t)X(t),
will be a martingale. This is the content of (5.2.27).


218 5 Risk-Neutral Pricing


5.2.4 Pricing Under the Risk-Neutral Measure



In Section 4.5, we derived the Black-Scholes-Merton equation for the value
of a European call by asking what initial capital X(O) and portfolio process
Ll(t) an agent would need in order to hedge a short position in the call (i.e.,
in order to have X(T) (S(T) almost surely). In this section, we
=           - K)+
generalize the question. Let V(T) be an .F(T)-measurable random variable.
This represents the payoff at time T of a derivative security. We allow this
payoff to be path-dependent (i.e., to depend on anything that occurs between
times 0 and T), which is what .F(T)-measurability means. We wish to know
what initial capital X(O) and portfolio process Ll(t), 0 - t - T, an agent
would need in order to hedge a short position in this derivative security, i.e.,
in order to have
X(T) = V(T) almost surely. (5.2.28)
In Section 4.5, the mean rate of return, volatility, and interest rate were con­
stant. In this section, we do not a ume a constant mean rate of return,
volatility, and interest rate.
Our agent wishes to choose initial capital X(O) and portfolio strategy Ll(t),
0 � t � T, such that (5.2.28) holds. We shall see in the next section that this
can be_done. Once it has been done, the fact that D(t)X(t) is a martingale
under lP' implies



D(t)X(t) fE [D(T)X(T)iF(t)] fE [D(T)V(T)IF(t)] . (5.2.29)
= =



The value X(t) of the hedging portfolio in (5.2.29) is the capital needed at
time t in order to successfully complete the hedge of the short position in the
derivative security with payoff V(T). Hence, we can call this the price V(t) of
the derivative security at time t, and (5.2.29) becomes



D(t)V(t) fE [D(T)V(T)IF(t)], 0 � t � T. (5.2.30)
=



This is the continuous-time analogue of the risk-neutral pricing formula
(2.4.10) in the binomial model of Volume I. Dividing (5.2.30) by D(t), which
is F(t)-measurable and hence can be moved inside the conditional expectation
on the right-hand side of (5.2.30), and recalling the definition of D(t), we may
write (5.2.30) as



V(t) = fE e- It R [(] u [) d] uV(T) F(t) []], 0 � t � T. (5.2.31)
###### [ I



This is the continuous-time analogue of (2.4.11) of Volume I. We shall re­
fer to both (5.2.30) and (5.2.31) as the risk-neutral pricing formula for the
continuous-time model.



5.2.5 Deriving the Black-Scholes-Merton Formula

The addition of Merton's name to what has traditionally been called the
Black-Scholes formula is explained in the Notes to Chapter 4, Section 4.9.


5.2 Risk-Neutral Measure 219


To obtain the Black-Scholes-Merton price of a European call, we a ume a
constant volatility u, constant interest rate r, and take the derivative security
payoff to be V(T) (S(T) - The right-hand side of (5.2.31) becomes
= K)+.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-238-0.png)



















The integrand


220 5 Risk-Neutral Pricing



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-239-0.png)













For future reference, we introduce the notation



(5.2.35)
where Y is a standard normal random variable under J. We have just shown
that

BSM(T, x; K, r, a) = xN (d+(T, x))    - e [-r-r ] KN (d- (T, x)) . (5.2.36)

In Section 4.5, we derived the Black-Scholes-Merton partial differential
equation (4.5.14) and then provided the solution in equation (4.5.19) without
explaining how one obtains this solution (although one can verify after the fact
that (4.5.19) does indeed solve (4.5.14); see Exercise 4.9 of Chapter 4). Here
we have derived the solution by the device of switching to the risk-neutral
measure.

+

           BSM(r, x; K, r, u) E e-n x exp { -u,/i'Y + r - �u' K,
### [ ( ( ) 7}- ) ]



BSM(T, x; K, r, a) = xN (d+(T, x)) - e [-r-r ] KN (d- (T, x)) . (5.2.36)


5.3 Martingale Representation Theorem 221


Martingale Representation Theorem
5.3

The risk-neutral pricing formula for the price (value) at time t of a derivative
security paying V(T) at time T, equation (5.2.31), was derived under the
a umption that if an agent begins with the correct initial capital, there is
a portfolio process L\(t), 0 - t - T, such that the agent's portfolio value
at the final time T will be V(T) almost surely. Under this a umption, we
determined the "correct initial capital" to be (set t = 0 in (5.2.31))

V(O) = fE[D(T)V(T)],

and the value of the hedging portfolio at every time t, 0 � t � T, to be V(t)
given by (5.2.31). In this section, in the model with one stock driven by one
Brownian motion, we verify the a umption on which the risk--neutral pricing
formula (5.2.31) is based. We take up the case of multiple Brownian motions
and multiple stocks in Section 5.4.


5.3.1 Martingale Representation with One Brownian Motion


The existence of a hedging portfolio in the model with one stock and one
Brownian motion depends on the following theorem, which we state without
proof.

Theorem 5.3.1 (Martingale representation, one dimension) . Let W(t),
0 - t - T, be a Brownian motion on a probability space ( n, F, IP'), and let
F(t), 0 - t - T, be the filtration generated by this Brownian motion. Let
M ( t), 0 � t � T, be a martingale with respect to this filtration (i.e., for every
t, M(t) is F(t)-measurable and for 0 � s - t � T, IE[M(t)j.F(s)] = M(s)}.
Then there is an adapted process r(u), 0 � u � T, such that

M(t) = M(O) + 1 [t ] r(u) dW(u), 0 � t � T. (5.3.1)

The Martingale Representation Theorem a erts that when the filtration
is the one generated by a Brownian motion (i.e., the only information in .F(t)
that gained from observing the Brownian motion up to time t), then every
is
martingale with respect to this filtration is an initial condition plus an Ito in­
tegral with respect to the Brownian motion. The relevance to hedging of this
is that the only source of uncertainty in the model is the Brownian motion
appearing in Theorem 5.3.1, and hence there is only one source of uncertainty
to be removed by hedging. This a umption implies that the martingale can­
not have jumps because Ito integrals are continuous. If we want to have a
martingale with jumps, we will need to build a model that includes sources
of uncertainty different from (or in addition to) Brownian motion.
The a umption that the filtration in Theorem 5.3.1 is the one generated
by the Brownian motion is more restrictive than the assumption of Girsanov's


222 5 Risk-Neutral Pricing


Theorem, Theorem 5.2.3, in which the filtration can be larger than the one
generated by the Brownian motion. If we include this extra restriction in Gir­
sanov's Theorem, then we obtain the following corollary. The first paragraph
of this corollary is just a repeat of Girsanov's Theorem; the second part con­
tains the new a ertion.

Corollary 5.3.2. Let W(t), 0 : t : T, be a Brownian motion on a probability
space (il,F,IP'), and let F(t), 0 : t : T, be the filtration generated by this
Brownian motion. Let B(t), 0 : t : T, be an adapted process, define



Z(t) = exp { -1t B(u) dW(u) - � 1t 82(u) du,
###### }



W(t) = W(t) + 1 [t ] B(u) du,



and assume that IE - J0 T 8 [2] (u)Z [2] (u) du < oo. Set Z = Z(T). Then IEZ = 1, and
under the probability measure lP given by {5.2.1}, the process W(t), 0 : t : T,
is a Brownian motion.
Now let M ( t), 0 : t : T, be a martingale under lP. Then there is an
adapted process T(u), 0 : u : T, such that

M(t) = M(O) + 1 [t ] T(u) dW(u), 0 : t : T. (5.3.2)

Corollary 5.3.2 is not a trivial consequence of the Martingale Representa­
tion Theorem, Theorem 5.3.1, with W(t) replacing W(t) because the filtration
F(t) in this corollary is generated by the process W(t), not the [JP] -Brownian
motion W(t). However, the proof is not difficult and is left to the reader as
Exercise 5.5.


5.3.2 Hedging with One Stock


We now return to the hedging problem. We begin with the model of Subsection
5.2.2, which has the stock price process (5.2.15) and an interest rate process
R(t) that generates the discount process (5.2.17). Recall the a umption that,
for all t E [0, T), the volatility a(t) is almost surely not zero. We make the
additional a umption that the filtration F(t), 0 : t : T, is generated by the
Brownian motion W(t), 0 : t : T.
Let V(T) be an F(T)-measurable random variable and, for 0 : t : T,
define V(t) by the risk-neutral pricing formula (5.2.31). Then, according to
(5.2.30),
D(t)V(t) = E[D(T)V(T)iF(t)] .

This is a [JP] -martingale; indeed, iterated conditioning implies that, for 0 : s :
t : T,


5.3 Martingale Representation Theorem 223




[D(T)V(T) i.F(s)]
= [E]
D(s)V(s). (5.3.3)
=

V(O))
=

t
D(t)V(t) = V(O) + F(u) dW(u), 0 � t � T. (5.3.4)
###### lo

iE [D(t)V(t) IF(s)] iE[iE[D(T) V(T)I.F(t)J I.F(s)]
=



Therefore, D(t)V(t) has a representation as (recall that D(O)V(O) V(O))
=



On the other hand, for any portfolio process Ll(t), the differential of the
discounted portfolio value is given by (5.2.27), and hence



D(t)X(t) = X(O) +
###### lo
t
Ll(u)u(u)D(u)S(u) dW(u), 0 � t � T.



(5.3.5)


(5.3.6)


(5.3.7)


(5.3.8)



In order to have X(t) V(t) for all t, we should choose
=



and choose Ll ( t) to satisfy



X(O) V(O)
=



Ll(t)u(t)D(t)S(t) F(t), 0 � t � T,
=

which is equivalent to

f{t)

         <
Ll(t) - u(t)D(t)S(t) ' O � t - T.



With these choices, we have a hedge for a short position in the derivative
security with payoff V(T) at time T.
There are two key a umptions that make the hedge possible. The first is
that the volatility u(t) is not zero, so equation (5.3.7) can be solved for Ll(t). If
the volatility vanishes, then the randomness of the Brownian motion does not
enter the stock, although it may still enter the payoff V(T) of the derivative
security. In this case, the stock is no longer an effective hedging instrument.
The other key a umption is that .F(t) is generated by the underlying Brown­
motion (i.e., there is no randomness in the derivative security apart from
ian
the Brownian motion randomness, which can be hedged by trading the stock).
Under these two a umptions, every .F(T)-measurable derivative security can
be hedged. Such a model is said to be complete.
The Martingale Representation Theorem argument of this section justifies
the risk-neutral pricing formulas (5.2.30) and (5.2.31), but it does not provide

a practical method of finding the hedging portfolio Ll(t). The final formula
(5.3.8) for Ll(t) involves the integrand F(t) in the martingale representation
(5.3.4) of the discounted derivative security price. While the Martingale Rep­
resentation Theorem guarantees that such a process f exists and hence a
hedge Ll(t) exists, it does not provide a method for finding f(t). We return
to this point in Chapter 6.


224 5 Risk-Neutral Pricing


5.4 Fundamental Theorems of Asset Pricing


In this section, we extend the discussions of Sections 5.2 and 5.3 to the case
of multiple stocks driven by multiple Brownian motions. In the process, we
develop and illustrate the two fundamental theorems of a et pricing. In ad­
dition to providing these theorems, in this section we give precise definitions
of some of the basic concepts of derivative security pricing in continuous-time
models


5.4.1 Girsanov and Martingale Representation Theorems


The two theorems on which this section is based are the multidimensional
Girsanov Theorem and the multidimensional Martingale Representation The­
orem. We state them here.
Throughout this section,

W(t) = {W1(t), . . ., Wd(t))

is a multidimensional Brownian motion on a probability space ( .n, F, IP'). We
interpret IP' to be the actual probability measure, the one that would be ob­
serveed from empirical studies of price data. Associated with this Brownian
motion, we have a filtration F(t) (see Definition 3.3.3). We shall have a fixed
final time T, and we shall a ume that F = F(T) . We do not always a ume
that the filtration is the one generated by the Brownian motion. When that
is a umed, we say so explicitly.



Theorem 5.4.1 (Girsanov, multiple dimensions) . Let T be a fixed pos­
itive time, and let e(t) = ( el (t), 0 0 0 ' ed(t)) be a d-dimensional adapted pro­
cess. Define



Z(t) = exp { -1 [t ] 8(u) · dW(u) - � 1 [t ] ll8(u)ll [2] du,
###### }



(5.4.1)


(5.4.2)


(5.4.3)



W(t) = W(t) + 8(u) du,
1 [t ]



and assume that



Set Z = Z(T) . Then lEZ = 1, and under the probability measure J given by



P(A) = Z(w) diP'(w) for all A E F,
L



the process W(t) is a d-dimensional Brownian motion.


5.4 Fundamental Theorems of Asset Pricing 225


The Ito integral in (5.4.1) is



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-244-0.png)








226 5 Risk-Neutral Pricing


5.4.2 Multidimensional Market Model


We a ume there are m stocks, each with stochastic differential
d
dSi(t) = ai(t)Si(t) dt + Si(t) L CTij(t) dWj(t), i = 1, . . ., m. (5.4.6)
j=l

We a ume that the mean rate of return vector (ai(t))i=l, ...,m and the volatil­



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-245-0.png)






5.4 Fundamental Theorems of Asset Pricing 227


Taking expectations and using the fact that the expectation of an Ito integral
is zero, we obtain the covariance formula


(5.4.12)


(5.4.13)


The volatility processes ai(t) and ak(t) are the respective instantaneous stan­
dard deviations of the relative changes in si and sk at time t, and the process
Pik(t) is the instantaneous correlation between these relative changes.
Mean rates of return are affected by the change to a risk-neutral measure
in the next subsection. Instantaneous standard deviations and correlations are
unaffected (Exercise 5.12(ii) and (iii)). If the instantaneous standard devia­
tions and correlations are not random, then ( noninstantaneous) standard de­
viations and correlations are unaffected by the change of measure (see Exercise
5.12(iv) for the case of correlations) . However, (noninstantaneous) standard
deviations and correlations can be affected by a change of measure when the
instantaneous standard deviations and correlations are random (see Exercises
5.12(v) and 5.13 for the case of correlations) .
We define a discount process

D(t) = e [-] f� [R(u)du] . (5.4.14)

We a ume that the interest rate process R(t) is adapted. In addition to stock
prices, we shall often work with discounted stock prices. Their differentials
are



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-246-0.png)
228 5 Risk-Neutral Pricing
d(D(t)Si(t)) = D(t) [dSi(t) - R(t)Si(t) dt]
d
= D(t)Si(t) (ai(t) - R(t)) dt + L:Uij(t) dWi(t)
j=l

[ ]
= D(t)Si(t) [(ai(t) - R(t)} dt + ai(t) dBi(t)], i = 1, . . ., m.
(5.4.15)


5.4.3 Existence of the Risk-Neutral Measure

Definition 5.4.3. A probability measure iP is said to be risk-neutral if
(i} iP and lP are equivalent (i.e., for every A E :F, JP(A) = 0 if and only if
P(A) = 0}, and
(ii}under iP, the discounted stock price D(t)Si(t) is a martingale for every
1, . . ., m.
i =
In order to make discounted stock prices be martingales, we would like to
rewrite (5.4.15) as
d
d(D(t)Si(t)) = D(t)Si(t) LO"ij(t) [6lj(t) dt + dWj(t)] . (5.4.16)
j=l

If we can find the market price of risk processes 6lj(t) that make (5.4.16)
hold, with one such process for each source of uncertainty Wj(t), we can
then use the multidimensional Girsanov Theorem to construct an equivalent
probability measure iP under which W(t) given by (5.4.2) is a d-dimensional
Brownian motion. This permits us to reduce (5.4.16) to
d
d(D(t)Si(t)) = D(t)Si(t) L O"ij(t) dWj(t), (5.4.17)
j=l

and hence D(t)Si(t) is a martingale under iP. The problem of finding a risk­
neutral measure is simply one of finding processes 6lj(t) that make (5.4.15)
and (5.4.16) agree. Since these equations have the same coefficient multiplying
each dWi ( t), they agree if and only if the coefficient multiplying dt is the same
in both cases, which means that
d
ai(t) - R(t) = L O"ij(t)6lj(t), i = 1, [. . ., m. ] (5.4.18)
j=l

We call these the market price of risk equations. These are m equations in the

0 0 0
d unknown processes el (t), ed(t) .
'
If one cannot solve the market price of risk equations, then there is an
arbitrage lurking in the model; the model is bad and should not be used for
pricing. We do not give the detailed proof of this fact. Instead, we give a
simple example to illustrate it.


5.4 Fundamental Theorems of Asset Pricing 229



Example 5.4.4- Suppose there are two stocks (m = 2) and one Brownian mo­
tion ( d 1), and suppose further that all coefficient processes are constant.
=
Then, the market price of risk equations are
01 - r = a10, (5.4.19)
02 - r = a20. (5.4.20)



(5.4.19)
(5.4.20)



These equations have a solution if and only if
(}



this equation does not hold, then one can arbitrage one stock against the
If
other. Suppose, for example, that

01 - r                - 02 - r
-- -( (12



and define

JL = --01 -( r - --02 -(12 r               - 0.
Suppose that at each time an agent holds Ll1(t) = shares of stock one
and Ll2 ( t) = - 82 shares of stock two, borrowing or investing as necessary
at the interest rate to set up and maintain this portfolio. The initial capital
r
required to take the stock positions is .lfl - ., but if this is positive we borrow
from the money market account, and if it is negative we invest in the money lT2
market account, so the initial capital required to set up the whole portfolio,
including the money market position, is X(O) = 0. The differential of the
portfolio value X ( t) is

dX(t)
= Ll1(t) dS1(t) + Ll2(t) dS2(t) + r(X(t) - Ll1(t)S1(t) - Ll2(t)S2(t)) dt
= --01 -( r dt + dW(t) - --o2 -(12 r dt - dW(t) + rX(t) dt
= JLdt + rX(t) dt.

The differential of the discounted portfolio value is
d(D(t)X(t)) D(t)(dX(t) - rX(t) dt) = JLD(t) dt.
=

The right-hand side JLD(t) is strictly positive and nonrandom. Therefore, this
portfolio will make money for sure and do so faster than the interest rate
r
because the discounted portfolio value has a nonrandom positive derivative.
We have managed to synthesize a second money market account with rate of
return higher than r, and now the arbitrage opportunities are limitless. D


230 5 Risk-Neutral Pricing



When there is no solution to the market price of risk equations, the ar­
bitrage in the model may not be as obvious as in Example 5.4.4, but it does
exist. If there is a solution to the market price of risk equations, then there
is no arbitrage. To show this, we need to introduce some notation and ter­
minology. In the market with stock prices Si(t) given by (5.4.6) and interest
rate process R(t), an agent can begin with initial capital X(O) and choose
adapted portfolio processes L\i(t), one for each stock Si(t). The differential of
the agent's portfolio value will then be



dX(t) = L\i(t) dSi(t) + R(t) X(t) - L\i(t)Si(t) dt
###### t t
m
### ( )
= R(t)X(t) dt + L L\i(t) (dSi(t) - R(t)Si(t) dt)
i=l
m
L\ (t)
= R(t)X(t) dt + d(D(t)Si(t)). (5.4.21)

     


The differential of the discounted portfolio value is



d(D(t)X(t)) = D(t)(dX(t) - R(t)X(t) dt)
m
= L L\i(t) d(D(t)Si(t)). (5.4.22)
i=l

lfJP is a risk-neutral measure, then under JP the processes D(t)Si(t) are martin­
gales, and hence the process D(t)X(t) must also be a martingale. Put another
way, under lP each of the stocks has mean rate of return R(t), the same as the
rate of return of the money market account. Hence, no matte!:_ how an agent
invests, the mean rate of return of his portfolio value under lP' must also be
R(t), and the discounted portfolio value must then be a martingale. We have
proved the following result.

Lemma 5.4.5. Let JP be a risk-neutml measure, and let X(t) be the value of
a portfolio. Under P, the discounted portfolio value D(t)X(t) is a martingale.

Definition 5.4.6. An arbitrage is a portfolio value process X(t) satisfying
X(O) = 0 and also satisfying for some time T > 0

IP'{X(T) � 0} = 1, IP'{X(T) > 0} > 0. (5.4.23)

An arbitrage is a way of trading so that one starts with zero capital and
at some later time T is sure not to have lost money and furthermore has a
positive probability of having made money. Such an opportunity exists if and
only if there is a way to start with positive capital X(O) and to beat the
money market account. In other words, there exists an arbitrage if and only if


5.4 Fundamental Theorems of Asset Pricing 231


there is a way to start with X(O) and at a later time T have a portfolio value
satisfying
X(O) X(O)
###### lP' { X(T) ; D(T) } = 1, lP' [{ ] X(T) > D(T) } > 0 (5.4.24)

(see Exercise 5.7).

Theorem 5.4.7 (First fundamental theorem of asset pricing). If a
market model has a risk-neutml probability measure, then it does not admit
arbitmge.

PROOF: If a market model has a risk-neutral probability measure [JP], then every
discounted portfolio value process is a martingale under [JP] . In particular, every
portfolio value process satisfies [E] [D(T)X(T)] = X(O). Let X(t) be a portfolio
value process with X(O) = 0. Then we have

E [D(T)X(T)] = 0. (5.4.25)

Suppose X(T) satisfies the first part of (5.4.23) (i.e., IP'{X(T) < 0} = 0).
Since lP is equivalent to IP', we have also [JP] {X(T) < 0} = 0. This, cou­
pled with (5.4.25), implies [JP] {X(T) - 0} = 0, for otherwise we would have
P{D(T)X(T) - 0} - 0, which would imply E [D(T)X(T)] - 0. Because lP'
and lP are equivalent, we have also IP'{X(T) > 0} = 0. Hence, X(t) is not an
arbitrage. In fact, there cannot exist an arbitrage since every portfolio value
process X(t) satisfying X(O) = 0 cannot be an arbitrage. 0

One should never offer prices derived from a model that admits arbitrage,
and the First Fundamental Theorem provides a simple condition one can apply
to check that the model one is using does not have this fatal flaw. In our model
with d Brownian motions and stocks, this amounts to producing a solution
m
to the market price of risk equations (5.4.18). In models of the term structure
of interest rates (i.e., models that provide prices for bonds of every maturity),
there are many instruments available for trading, and possible arbitrages in
the model prices are a real concern. An application of the First Fundamental
Theorem of Asset Pricing in such a model leads directly to the Heath-Jarrow­
Morton condition for no arbitrage in term-structure models.


5.4.4 Uniqueness of the Risk-Neutral Measure


Definition 5.4.8. A market model is complete if every derivative security
can be hedged.

Let us suppose we have a market model with a filtration generated by

a d-dimensional Brownian motion and with a risk-neutral measure lP (i.e.,
we have solved the market price of risk equations (5.4.18), used the resulting


232 5 Risk-Neutral Pricing



market prices of risk 81 (t), . . ., 8d(t) to define the Radon-Nikodym derivative
process Z(t), and have changed to the measure iP under which W(t) defined
by (5.4.2) is a d-dimensional Brownian motion). Suppose further that we are
given an F(T)-measurable random variable V(T), which is the payoff of some
derivative security.
We would like to be sure we can hedge a short position in the derivative
security whose payoff at time T is V(T). We can define V(t) by (5.2.31), so
that D(t)V(t) satisfies (5.2.30), and just as in (5.3.3), we see that D(t)V(t) is
a martingale under iP. According to the Martingale Representation Theorem
5.4.2, there are processes h(u), . . ., rd(u) such that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-251-0.png)



or, equivalently,

=



(5.4.27)


(5.4.28)



(5.4.29)


.
are satisfied. These are d equations in m unknown processes Ll1(t), . . ., Llm(t)

Theorem 5.4.9 (Second fundamental theorem of asset pricing). Con­
sider a market model that has a risk-neutral probability measure. The model
is complete if and only if the risk-neutral probability measure is unique.

SKETCH OF PROOF: We first a ume that the model is complete. We wish to
show that there can be only one risk-neutral measure. Suppose the model has
two risk-neutral measures, P1 and P2. Let A be a set in :F, which we a umed
at the beginning of this section is the same as F(T). Consider the derivative


5.4 Fundamental Theorems of Asset Pricing 233



measures are really the same.



(5.4.30)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-252-0.png)





(5.4.31)



el(t)
e2(t)
X = .
'
ed(t)
and b is the m-dimensional column vector
a1(t) - R(t)
a2(t) - R(t)
b = . .
# [ am(t) - R(t) l


234 5 Risk-Neutral Pricing


Our a umption that there is only one risk-neutral measure means that the
system of equations (5.4.30) has a unique solution x.
In order to be a ured that every derivative security can be hedged, we


(5.4.32)


vector

,

c



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-253-0.png)





y'"',

could then conclude that a short position in an arbitrary derivative security
can be hedged.
The uniqueness of the solution x to (5.4.30) implies the existence of a so­
lution to (5.4.32). We give a proof of this fact in Appendix C. Consequently,
y
uniqueness of the risk-neutral measure implies that the market model is com­
plete. []


5.5 Dividend-Paying Stocks


According to Definition 5.4.3, discounted stock prices are martingales under
the risk-neutral measure. This is the case provided the stock pays no dividend.
The key feature of a risk-neutral measure is that it causes discounted portfolio
values to be martingales (see Lemma 5.4.5), and that ensures the absence of
arbitrage (First Fundamental Theorem of Asset Pricing, Theorem 5.4.7). In
order for the discounted value of a portfolio that invests in a dividend-paying


5.5 Dividend-Paying Stocks 235


stock to be a martingale, the discounted value of the stock with the dividends
reinvested must be a martingale, but the discounted stock price itself is not a
martingale. This section works out the details of this situation. We consider a
single stock price driven by a single Brownian motion, although the results we
obtain here also apply when there are multiple t5tocks and multiple Brownian
motions.


5.5.1 Continuously Paying Dividend

Consider a stock, modeled as a generalized geometric Brownian motion, that
pays dividends continuously over time at a rate A(t) per unit time. Here A(t),
0 - t � T, is a nonnegative adapted process. A continuously paid dividend
is not a bad model for a mutual fund, which collects lump sum dividends at
a variety of times on a variety of stocks. In the case of a single stock, it is
more reasonable to a ume there are periodic lump sum dividend payments.
We consider that case in Subsections 5.5.3 and 5.5.4.
Dividends paid by a stock reduce its value, and so we shall take as our
model of the stock price

dS(t) = o(t)S(t) dt + a(t) S(t) dW(t) - A(t)S(t) dt. (5.5.1)

H the stock were to withhold dividends, its mean rate of return would be o(t).
Equivalently, if an agent holding the stock were to reinvest the dividends, the
mean rate of return on his investment would be o(t). The mean rate of return
o(t), the volatility a(t), and the interest rate R(t) appearing in (5.5.2) below
are all a umed to be adapted processes.
An agent who holds the stock receives both the capital gain or loss due to
stock price movements and the continuously paying dividend. Thus, if Ll(t) is
the number of shares held at time t, then the portfolio value X(t) satisfies



dX(t) = Ll(t) dS(t) + Ll(t)A(t)S(t) dt + R(t) [X(t) - Ll(t)S(t)) dt



= R(t)X(t) dt + (o(t) - R(t))Ll(t)S(t) dt + a(t)Ll(t)S(t) dW(t)



= R(t)X(t) dt + Ll(t)S(t)a(t) [8(t) dt + dW(t)], (5.5.2)



where



e(t) = [o(t) - R(t) ] (5.5.3)
a(t)



is the usual market price of risk.
We define
t
W(t) = W(t) + 8(u) du (5.5.4)
###### lo

and use Girsanov's Theorem to change to a measure iP under which W is a
Brownian motion, so we may rewrite (5.5.2) as



dX(t) R(t)X(t) dt + Ll(t)S(t)a(t) dW(t).
###### =


236 5 Risk-Neutral Pricing


The discounted portfolio value satisfies

=


process.

we must have

=


=


as in the no-dividend case; see Section 5.3.

and the definition of W(t), we see that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-255-0.png)

= +



Under the risk-neutral measure, the stock does not have mean rate of return
R(t), and consequently the discounted stock price is not a martingale. Indeed,


S(t) S(O) exp a(u) dW(u) R(u) - A(u) - a [2] (u) du .
= {lo [t ] +lo [t ]    - ]
###### }

[ (5.5.7)
The process



ef; A [(] u [) ] D(t)S(t) = exp {lo [t ] a(u) dW(u) - �lo [t ] a [2] (u) du
###### }



is a martingale. This is the interest-rate-discounted value at time t of ac­
an
count that initially purchases one share of the stock and continuously reinvests
the dividends in the stock.


5.5 Dividend-Paying Stocks 237



5.5.2 Continuously Paying Dividend with Constant Coefficients



In the event that the volatility a, the interest rate r, and the dividend rate a
are constant, the stock price at time t, given by (5.5.7), is





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-256-0.png)
















238 5 Risk-Neutral Pricing

We make the change of variable z = y + a .jT in the integral, which leads us
to the formula


We a ume that each a3 is an F(t3)-measurable random variable taking values
in [0, 1] . If a3 = 0, no dividend is paid at time t 3. If a3 = 1, the full value of the
stock is paid as a dividend at time t3, and the stock value is zero thereafter. To
simplify the notation, we set to = 0 and tn+l = T. However, neither t0 = 0 nor
tn+l = T is a dividend payment date (i.e., ao = 0 and an+l = 0). We a ume
that, between dividend payment dates, the stock price follows a generalized
geometric Brownian motion:

dS(t) = a(t)S(t) dt+a(t)S(t) dW(t), t3 ::; t < tJ+l> j = 0, 1, . . ., n. (5.5.14)

Equations (5.5.13) and (5.5.14) fully determine the evolution of the stock
price.
Between dividend payment dates, the differential of the portfolio value
corresponding to a portfolio process Ll(t), 0 ::; t ::; T, is

dX(t) = Ll(t) dS(t) + R(t) [X(t) - Ll(t)S(t) dt
)
= R(t)X(t) dt + a(t) - R(t) Ll(t)S(t) dt + a(t)Ll(t)S(t) dW(t)
( )
= R(t)X(t) dt + Ll(t)a(t)S(t) [B(t) dt + dW(t)],

where the market price of risk B(t) is again defined by (5.5.3) . At the div­
idend payment dates, the value of the portfolio stock holdings drops by
a3Ll(t1)S(t1-), but the portfolio collects the dividend a3Ll(t1)S(t1-), and
so the portfolio value does not jump. It follows that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-257-0.png)
5.5 Dividend-Paying Stocks 239

dX(t) = R(t)X(t) dt + Ll(t)a(t)S(t) [B(t) dt + dW(t)] (5.5.15)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-258-0.png)


###### }

(                         - )



(5.5.16)




###### }

(                         - )




###### }

(                          - )








###### }

(                  - )


###### ( � ) }



This is the same formula we would have for the price at time T of a geo­
metric Brownian motion not paying dividends if the initial stock price were


240 5 Risk-Neutral Pricing


S(O) ai+I) rather than S(O). Therefore, the price at time zero of
Ilj,:-�(1    a European call on this dividend-paying a et, a call that expires at time
T with strike price K, is obtained by replacing the initial stock price by
S(O) aj+l) in the cla ical Black-Scholes-Merton formula. This re­
Ilj,:;-�(1 sults in the call price

n-1
S(O) aj+l)N(d+) IT (1 - e-rT KN(d-),
j=O

where

###### 1

This pricing formula guarantees that no arbitrage can be found by trading in
these bonds because any such portfolio, when discounted, will be a martingale
under the risk-neutral measure. The details of this argument in the binomial
model are presented in Theorem 6.2.6 and Remark 6.2. 7 of Volume I.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-259-0.png)
5.6 Forwards and Futures 241


Definition 5.6.1. A forward contract is an agreement to pay a specified de­
livery price K at a delivery date T, where 0 : T for the asset whose
: T,
price at time t is S(t). The T-forward price Fors (t, T) of this asset at time t,
where 0 : t : T : T, is the value of K that makes the forward contract have
no-arbitrage price zero at time t.

Theorem 5.6.2. Assume that zero-coupon bonds of all maturities can be
traded. Then


to be



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-260-0.png)





= S(t) - K B(t, T).



In order for this to be zero, K must be given by (5.6.2).


5.6.2 Futures Contracts

Consider a time interval [0, T], which we divide into subintervals using the
partition points 0 = t0 < t1 < t2 < - · · < tn = T. We shall refer to each
subinterval [tk, tk+l) as a "day."


242 5 Risk-Neutral Pricing



Suppose the interest rate is constant within each day. Then the discount
process is given by D(O) 1 and, for k 0, 1, . . ., n - 1,





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-261-0.png)



( )


r
###### =




5.6 Forwards and Futures 243



=

v. n-1,n S( ) S( tn - tn-1 ) B(tm T) ·



=
n-1,n tn - tn-1 = _

S( ) S( ) B(tm T) S(T) S(tn-d .




                                                                        B( tn-1' T) B( tn-1,T )
There are two problems with this. First of all, the purchaser of the for­
ward contract was presumably motivated by a desire to hedge against a price
increase in the underlying a et. It is not clear the extent to which receiving
this cash flow provides such a hedge. Second, this daily buying and selling of
forward contracts requires that there be a liquid market each day for forward
contracts initiated that day and forward contracts initiated one day before.
This is too much to expect.
A better idea than daily repurchase of forward contracts is to create a
futures price Futs(t, T), and use it as described below. If an agent holds a
long futures position between times tk and tk+I, then at time tk+I he receives
a payment
Futs(tk+1, T) - Futs(tk, T).
This is called marking to margin. The stochastic process Futs(t, T) is con­
structed so that Futs(t, T) is F(t)-measurable for every t and

=
Futs(T, T) S(T).
Therefore, the sum of payments received by an agent who purchases a futures
contract at time zero and holds it until delivery date T is
(Futs(h, T) - Futs(to, T)) + (Futs(t2, T) - Futs(t1, T)) + . . .



=

- · · + (Futs(tn, T) - Futs(tn-1, T) Futs(T, T) - Futs(O, T)



=
S(T) - Futs(O, T).
If the agent takes delivery of the a et at time T, paying market price S(T)
for it, his total income from the futures contract and the delivery payment
is -Futs(O, T). Ignoring the time value of money, he has effectively paid the
price Futs(O, T) for the a et, a price that was locked in at time zero.
In contrast to the case of a forward contract, the payment from holding a
futures contract is distributed over the life of the contract rather than coming
solely at the end. The mechanism for these payments is the margin account,
which the owner of the futures contract must open at the time of purchase of
the contract and to which he must contribute or from which he may withdraw
money, depending on the trajectory of the futures price. Whereas the owner
of a forward contract is exposed to counterparty default risk, the owner of a
futures contract is exposed to the risk that some of the intermediate payments
(margin calls) will force him to close out his position prematurely.
=
In a ition to satisfying Futs(T, T) S(T), the futures price process is
chosen so that at each time tk the value of the payment to be received at time

                   tk+I, and indeed at all future times t1 tk, is zero. This means that at any
time one may enter or close out a position in the contract without incurring
any cost other than payments already made. The condition that the value at
time tk of the payment to be received at time tk+I be zero may be written as


244 5 Risk-Neutral Pricing



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-263-0.png)









These considerations lead us to make the following definition for the fully
continuous case (i.e., the case when R(t) is a umed only to be an adapted
stochastic process, not necessarily constant on time intervals of the form

[tk, tk+1)).

Definition 5.6.4. The futures price of an asset whose value at time T is S(T)
is given by the formula
Futs(t, T) = JE[S(T)IF(t)], 0 ::; t ::; T. (5.6.6)

A long position in the futures contract is an agreement to receive as a cash
flow the changes in the futures price (which may be negative as well as positive}
during the time the position is held. A short position in the futures contmct
receives the opposite cash flow.


5.6 Forwards and Futures 245


Theorem 5.6.5. The futures price is a martingale under the risk-neutml
measure P, it satisfies Futs(T, T) = S(T), and the value of a long (or a
short) futures position to be held over an interval of time is always zero.


OUTLINE OF PROOF:
The usual iterated conditioning argument shows that
Futs(t, T) given by (5.6.6) is a P-martingale satisfying the terminal condi­
tion Futs(T, T) = S(T). In fact, this is the only P-martingale satisfying this
terminal condition.
If the filtration :F(t), 0 � t � T, is generated by a Brownian motion W(t),
0 - t - T, then Corollary 5.3.2 of the Martingale Representation Theorem
implies that


and thus


(5.6.7)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-264-0.png)

JE[D(t1 )X






246 5 Risk-Neutral Pricing
this is zero. The value of owning a long futures position over the interval to
to t1 is obtained by setting Ll(u) = 1 for all u; the value of holding a short
position is obtained by setting Ll(u) = -1 for all u. In both cases, we see that
this value is zero.
If the filtration :F(t), 0 $ t $ T, is not generated by a Brownian motion,
so that we cannot use Corollary 5.3.2, then we must write (5.6.7) as

(5.6.9)
D(t1)X(ti) = l. [t] l D(u)Ll(u) dFuts(u, T).
to

This integral can be defined and it will be a martingale. We will again have
E[D(tt)X(h)I:F(to)] = 0. D

Remark 5.6.6 (Risk-neutral valuation of a cash flow). Suppose an a et gen­
erates a cash flow so that between times 0 and u a total of C(u) is paid,
where C(u) is :F(u)-measurable. Then a portfolio that begins with one share
of this a et at time t and holds this a et between times t and T, investing
or borrowing at the interest rate r as necessary, satisfies
+
dX(u) = dC(u) R(u)X(u) du,
or equivalently
d(D(u)X(u)) = D(u) dC(u).
Suppose X(t) = 0. Then integration shows that
D(T)X(T) = D(u) dC(u).

[T

The risk-neutral value at time t of X(T), which is the risk-neutral value at
time t of the cash flow received between times t and T, is thus



D(u)dC(u) :F(t), O $ t $ T.
### I ]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-265-0.png)

(5.6.10)
Formula (5.6.10) generalizes the risk-neutral pricing formula (5.2.30) to allow
for a cash flow rather than payment at the single time T. In (5.6.10), the

                                                                                                  - .                                                                                                   process C( u) can represent a succession of lump sum payments A1, A2,, An
at times t1 < h < - · · < tn, where each Ai is an :F(ti)-measurable random
variable. The formula for this is



n
C(u) = L Aill[o,uJ(ti)·
i=l
In this case,


5.6 Forwards and Futures 247

t i=l
Only payments made strictly later than time t appear in this sum. Equation
(5.6.10} says that the value at time t of the string of payments to be made
strictly later than time t is


0

=
1T D(u) dC(u) tD(ti)AiH(t,TJ(ti)·



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-266-0.png)


is





risk-neutral measure. If the interest rate is nonrandom, this covariance is zero
and the futures price agrees with the forward price.


248 5 Risk-Neutral Pricing
One can explain this last formula as follows. If D(T) and S(T) are pos­
itively correlated, then higher a et prices tend to correspond to higher dis­
count levels, which tend to correspond to lower interest rates. But when the
a et goes up, the long position in the futures contract receives a payment
(because the futures price is positively correlated with the underlying a et
price). The long position in the futures contract thus receives money when the
interest rate for investing is unfavorable (low) and conversely must pay money
when the interest rate at which money can be borrowed is also unfavorable
(high). The owner of the futures contract would have rather owned the for­
ward contract, in which all payments are postponed until the end. Therefore,
to make the futures contract attractive, the futures price must be lower than
the forward price. (Recall that this price is what the investor ultimately pays
for the a et.) This creates a positive forward-futures spread when the dis­
count factor D(T) and the a et price S(T) are positively correlated. Note
that all correlations in this argument are computed under the risk-neutral
measure, not the actual probability measure. In a Brownian-motion-driven
model, in which the multidimensional Girsanov Theorem, Theorem 5.4.1, is
used to change to the risk-neutral measure, instantaneous a et correlations
are the same under both measures (s Exercise 5.12). However, correlations
between random variables (as opposed to instantaneous correlations between
stochastic processes) can be affected by changes of measure (see Exercise 5.13).


5.7 Summary

This chapter treats the application to finance of two major theorems, Girsanov
(Theorem 5.4.1) and Martingale Representation (Theorem 5.4.2). These lead
to the two Fundamental Theorems of Asset Pricing, Theorem 5.4. 7 and The­
orem 5.4.9. Both of these are stated for models with multiple a ets whose
prices are driven by multiple Brownian motions.
According to the Fundamental Theorems of Asset Pricing, there are three
possible situations when we build a mathematical model of a multia et mar­
ket.
Case 1.
There is no risk-neutral measure (i.e., the market price of risk
equations (5.4.18) cannot be solved for 81 (t), . . ., 8d(t)). This is a bad model.
There must be some way to form an arbitrage by trading at the prices given
by this model. Do not use this model.
Case 2.
There are multiple risk-neutral measures (i.e., the market price
of risk equations (5.4.18) have more than one solution). The different risk­
neutral measures lead to different prices for derivative securities in the model.
Any derivative security that has more than one price cannot be synthesized
by trading in the model (i.e., a position in this derivative security cannot be
hedged). (If the derivative security could be hedged, this would determine a
unique price; see the proof of Theorem 5.4.9.) It may still be possible to cali­
brate the model (i.e., determine its parameters by getting it to match market


5. 7 Summary 249
prices, and the model might then give reasonable prices for nontraded instru­
ments). However, it cannot be used to fully hedge the exposure a ociated
with derivative positions.
At the present time, credit derivative models fall into Case 2. They are
used for pricing, but are incomplete because the derivatives in question pay
off contingent upon the default of some party and it is impossible to perfectly
hedge default risk by trading in primary a ets. These models have multiple
risk-neutral measures, all of which can be consistent with market prices of the
primary a ets but give different prices for derivatives. In practical applica­
tions, one of these risk-neutral measures is singled out and used for pricing.
Which of the risk-neutral measures is chosen for this purpose depends on the
way the model is specified and calibrated.
Case 3. There is one and only one set of processes 81 (t), . . .,Bd(t) that
solve the market price of risk equations (5.4.18). There is a unique risk-neutral
measure, and risk-neutral pricing is justified. In other words,the price (value)
at time t of any security that pays V(T) at time T is

=

face value 1:



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-268-0.png)
250 5 Risk-Neutral Pricing
The futures price of an a et is an adapted stochastic process Futs(t, T)
with two properties.
(i) The futures price agrees with the a et price on the delivery date (i.e.,
Futs(T, T) = S(T)).
(ii) The value of holding the futures contract over a period of time and re­
ceiving the cash flows a ociated with this position is zero:


see Karatzas and Shreve [101], page 198. The multidimensional version of both
Girsanov's Theorem and the Martingale Representation Theorem (Theorems
5.4.1 and 5.4.2) can be found in Karatzas and Shreve [101] as Theorems 5.1 and
4.15 of Chapter 3. A mathematically rigorous application of these theorems
to Brownian-motion-driven models in finance is provided by Karatzas and
Shreve [102].



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-269-0.png)
5.9 Exercises 251
The application of the Girsanov Theorem to risk-neutral pricing is due to
Harrison and Pliska [78]. This methodology frees the Brownian-motion-driven
model from the a umption of a constant interest rate and volatility. When
both of these are stochastic, the Brownian-motion-driven model is mathe­
matically the most general possible for continuous stock prices that do not
admit arbitrage. In particular, the log-normal model for asset prices is just
one special case of the Brownian-motion-driven model.
The Fundamental Theorems of Asset Pricing, Theorems 5.4. 7 and 5.4.9,
can be found in Harrison and Pliska [78], [79]. It is tempting to believe the
converse of Theorem 5.4.7 (i.e., that the absence of arbitrage implies the
existence of a risk-neutral measure). This is true in discrete-time models (see
Dalang, Morton, and Willinger [45]), but in continuous-time models a slightly
stronger condition is needed to guarantee existence of a risk-neutral measure.
See Delbaen and Schachermayer [49] for a summary of relevant results.
The distinction between forward contracts and futures was pointed out by
Margrabe [118] and Black [13]. No-arbitrage pricing of futures in a discrete­
time model was developed by Cox, Ingersoll, and Ross [40] and Jarrow and
Oldfield [98].


5. 9 Exercises

Exercise 5.1. Consider the discounted stock price D(t)S(t) of (5.2.19). In
this problem, we derive the formula (5.2.20) for d(D(t)S(t)) by two methods.
(i) Define f(x) = S(O)e [x ] and set

X(t) = 1 [t ] a(s) dW(s) + 1 [t ] o:(s) - R(s) - �a [2] (s) ds
( )
so that D(t)S(t) = f(X(t)). Use the It6-Doeblin formula to compute
df(X(t)).
(ii) According to Ito's product rule,

d(D(t)S(t)) = S(t) dD(t) + D(t) dS(t) + dD(t) dS(t).
Use (5.2.15) and (5.2.18) to work out the right-hand side of this equation.

Exercise 5.2 (State price density process).
Show that the risk-neutral
pricing formula (5.2.30) may be rewritten as

D(t)Z(t)V(t) lE[D(T)Z(T)V(T)iF(t)] .
= (5.9.1)
Here Z(t) is the Radon-Nikodym derivative process (5.2.11) when the market
price of risk process 8(t) is given by (5.2.21) and the conditional expectation
on the right-hand side of (5.9.1) is taken under the actual probability measure


252 5 Risk-Neutral Pricing



IP', not the risk-neutral measure JP>. In particular, if for some A E :F(T) a deriva­
tive security pays off [A (i.e., pays 1 if A occurs and 0 if A does not occur),
then the value of this derivative security at time zero is JE[D(T)Z(T)KA]· The
process D(t)Z(t) appearing in (5.9.1) is called the state price density process.

Exercise 5.3.
According to the Black-Scholes-Merton formula, the value at
time zero of a European call on a stock whose initial price is S(O) = x is given
by
c(O,x) = xN(d+(T,x)) -Ke-r [T] N(d-(T,x)),
where


( )
formula for Cx(O,x).

                       
is a Brownian motion under P.

+



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-271-0.png)
5.9 Exercises 253
(iii) Rewrite S(T) in terms of W(T), and then show that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-272-0.png)

(ii) Let


###### )




254 5 Risk-Neutral Pricing

Exercise 5.6. Use the two-dimensional Levy Theorem, Theorem 4.6.5, to
prove the two-dimensional Girsanov Theorem (i.e., Theorem 5.4.1 with d = 2).

Exercise 5.7.
(i) Suppose a multidimensional market model as described in
Section 5.4.2 has an arbitrage. In other words, suppose there is a portfolio
value process satisfying X1(0) = 0 and

lP{X1(T) � 0} = 1, lP{X1(T) > 0} > 0, (5.4.23)
for some positive T. Show that if X2(0) is positive, then there exists a
portfolio value process X2(t) starting at X2(0) and satisfying


(5.4.24)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-273-0.png)
5.9 Exercises 255

(ii) Show that, for each t E [0, T], the price of the derivative security V(t) at
time t is almost surely positive.
(iii) Conclude from (i) and (ii) that there exists an adapted process a(t), 0 �
t � T, such that


Let S(t) be the


equations

                                CKK(O,T,x,K) = e [-] r [T] p(O,T,x,K).

The second of these equations provides a formula for the risk-neutral distri­
bution of S(T) in terms of call prices:
p(O,T,x,K) = erTCKK(O,T,x,K) for all K > 0.
In practice, we do not have this many prices. We have the prices of calls at some
2
strikes, and we can infer the prices of calls at other strikes by knowing the prices
of puts and using put-call parity. We must create prices for the calls of other
strikes by interpolation of the prices we do have.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-274-0.png)
256 5 Risk-Neutral Pricing


Exercise 5.10 (Chooser option).
Consider a model with a unique risk­
neutral measure iP and constant interest rate r. According to the risk-neutral
pricing formula, for 0 $ t $ T, the price at time t of a European call expiring
at time T is
C(t) = E [ e [-r(] T [-t) ] (S(T) F [(t)] ] [, ]
-K) +I
where S(T) is the underlying a et price at time T and is the strike price
of the call. Similarly, the price at time t of a European put expiring at time K
T is



Finally, because e-rts(t) is a martingale under iP, the price at time t of a
forward contract for delivery of one share of stock at time T in exchange for
a payment of at time T is
K



Because



= S(t) - e-r [(] T [-] t [) ]
K.
F(t) = E [ e-r(T-t) (S(T) F(t)]
-K) I
= ertjE [ e-rTS(T)j J="(t)]    - e-r(T-t)
K



Because

(S(T) - S(T) = S(T) K)+ - (K- )+ K,
we have the put-call parity relationship



C( t) - P( t) = iE [ e-r(T-t) S(T) - e-r(T-t) - S(T)) J="(t)]
( -Kt ( K +I



Now consider a date to between 0 and T, and consider a chooser option,
which gives the right at time to to choose to own either the call or the put.
(i) Show that at time to the value of the chooser option is


(ii) Show that the value of the chooser option at time 0 is the sum of the
value of a call expiring at time T with strike price and the value of a
put expiring at time to with strike price e-r [(] T-t [o) ] K
K.
C(to) + max{O, -F(to)} = C(to) + e-r(T-to) S(to)
( K- ) +.

= iE [ e-r(T-t) (S(T) J="(t)] = F(t).
-K) I



Exercise 5.11 (Hedging a cash flow). Let W(t), 0 $ t $ T, be a Brownian
motion on a probability space (il,J=",lP), and let J="(t), 0 $ t $ T, be the
filtration generated by this Brownian motion. Let the mean rate of return
a(t), the interest rate R(t), and the volatility u(t) be adapted processes, and
a ume that u(t) is never zero. Consider a stock price process whose differential
is given by (5.2.15):


5.9 Exercises 257
dS(t) = a(t)S(t) dt + a(t)S(t) dW(t), 0 � t � T.
Suppose an agent must pay a cash flow at rate C(t) at each time t, where
C(t), 0 � t � T, is an adapted process. If the agent holds Ll(t) shares of stock
at each time t, then the differential of her portfolio value will be
dX(t) = Ll(t) dS(t) + R(t) (X(t) - Ll(t)S(t)) dt - C(t) dt. (5.9.4)
Show that there is a nonrandom value of X(O) and a portfolio process Ll(t),
0 � t � T, such that X(T) = 0 almost surely. (Hint: Define the risk-neutral
measure and apply Corollary 5.3.2 of the Martingale Representation Theorem
to the process





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-276-0.png)




.
(iii) We saw in (5.4.9) that dBi(t) dBk(t) = Pik(t) This is the instantaneous
correlation between Bi(t) and Bk(t) . Because (5.4.9) makes no reference
to the probability measure, Exercise 4.17 of Chapter 4 implies that under
both lP' and iP', the correlation between the pair of increments B1 (to + f) B1 (to) and B2(to + f) - B2(to) is approximately Pik(to). Show that


258 5 Risk-Neutral Pricing


Show that


Exercise 5.13. In part (v) of Exercise 5.12, we saw that when we change
measures and change Brownian motions, correlations can change if the in­
stantaneous correlations are random. This exercise shows that a change of
measure without a change of Brownian motions can change correlations if the
market prices of risk are random.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-277-0.png)
Let W1(t) and W (t) be independent Brownian motions under a prob­
5.9 Exercises 259



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-278-0.png)
260 5 Risk-Neutral Pricing
Verify that, for 0 � t � T,
=



satisfies (5.9.7).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-279-0.png)

writing




[ds ]





and then simplifying the right-hand side of this equation.
(iv) The process IE[S(T)IF(t)] is the futures price process for the commodity
(i.e., Futs(t, T) = E[S(T)IF(t)]). This must be a martingale under P. To
check the formula you obtained in (iii), differentiate it and verify that
E[S(T)jF(t)] is a martingale under P.
(v) Let 0 � t � T be given. Consider a forward contract entered at time t to
purchase one unit of the commodity at time T for price K paid at time
T. The value of this contract at time t when it is entered is
(5.9.10)
The forward price Fors(t, T) is the value of K that makes the contract
value (5.9.10) equal to zero. Show that Fors(t, T) = Futs(t, T).
(vi) Consider an agent who takes a short position in a forward contract at time
zero. This costs nothing and generates no income at time zero. The agent
hedges this position by borrowing S(O) from the money market account
and purchasing one unit of the commodity, which she holds until time T.
At time T, the agent delivers the commodity under the forward contract
and receives the forward price Fors(O, T) set at time zero. Show that this
is exactly what the agent needs to cover her debt to the money market
account, which has two parts. First of all, at time zero, the agent borrows
S(O) from the money market account in order to purchase the unit of the
commodity. Second, between times zero and T, the agent pays the cost
of carry a per unit time, borrowing from the money market account to
finance this. (Hint: The value of the agent's portfolio of commodity and
money market account begins at X(O) = 0 (one unit of the commodity
and a money market position of -S(O)) and is governed by (5.9.6) with
Ll(t) = 1. Write this equation, determine d(e-r [t] x(t)), integrate both
E[e-r(T-t) (S(T) - K) iF(t)].


5.9 Exercie 261

sides from zero to T, and solve for X(T). You wiH need the fact; that
e-rt(dS(t) - rS(t)dt) ""' d(e-rtS(t)). You should !et X(T) = S(T) ­
Fors(O, T).)


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-281-0.png)
6


Connections with Partial Differential Equations


6. 1 Introduction


There are two ways to compute a derivative security price: (1) use Monte
Carlo simulation to generate paths of the underlying security or securities un­
der the risk-neutral measure and use these paths to estimate the risk-neutral
expected discounted payoff; or (2) numerically solve a partial differential equa­
tion. This chapter addresses the second of these methods by showing how to
connect the risk-neutral pricing problem to partial differential equations. Sec­
tion 6.2 explains the concept of stochastic differential equations, which is used
to model a et prices. Solutions to stochastic differential equations have the
Markov property, as is discussed in Section 6.3. Because of this, related to
each stochastic differential equation there are two partial differential equa­
tions, one that includes discounting and one that does not. These partial dif­
ferential equations and their derivations are the subject of Section 6.4. Section
6.5 shows how these ideas can be applied to interest rate models to compute
bond prices and the prices of derivatives on bonds. The discussion of Sections
6.2-6.5 concerns one-dimensional processes. The multidimensional theory is
outlined in Section 6.6, and a representative example that uses this theory,
pricing and hedging an Asian option, is presented in that section.


6.2 Stochastic Differential Equations


A stochastic differential equation is an equation of the form

dX(u) = f3(u, X(u)) du + -y(u, X(u)) dW(u) . (6.2.1)

Here /3( u, x) and -y( u, x) are given functions, called the drift and diffusion,
respectively. In addition to this equation, an initial condition of the form

=
X ( t) x, where t 2 0 and x E IR, is specified. The problem is then to find a
stochastic process X(T), defined for T 2 t, such that


264 6 Connections with Partial Differential Equations
X(t) = x,
X(T) = X(t) + i [T ] {3(u, X(u)) du + i [T ] f'(u, X(u)) dW(u).



(6.2.2)

(6.2.3)



Under mild conditions on the functions and there exists a
{3(u, x) f'(u, x),
unique process X(T), T 2 t, satisfying (6.2.2) and (6.2.3). However, this
proce can be difficult to determine explicitly because it appears on both the
left- and right-hand sides of equation (6.2.3).
The solution X(T) at time T will be F(T)-measurable (i.e., X(T) only
depends on the path of the Brownian motion up to time T.) In fact, since the
initial condition X ( t) = x is specified, all that is really needed to determine
X(T) is the path of the Brownian motion between times t and T.
Although stochastic differential equations are, in general, difficult to solve,
a one-dimensional linear stochastic differential equation can be solved explic­
itly. This is a stochastic differential equation of the form
dX(u) = (a(u) + b(u)X(u)) du + ('y(u) + a(u)X(u)) dW(u), (6.2.4)

where a(u), b(u), a(u), and f'(u) are nonrandom functions of time. Indeed,
this equation can even be solved when and are adapted
a(u), b(u), f'(u), a(u)
random processes (see Exercise 6.1), although it is then no longer of the form
(6.2.1). In order to guarantee that the solution to (6.2.1) has the Markov
property discussed in Section 6.3 below, the only randomness we permit on
the right-hand side of (6.2.1) is the randomness inherent in the solution X(u)
and in the driving Brownian motions There cannot be additional ran­
W(u).
domness such as would occur if any of the processes and
a(u), b(u), l'(u),
a(u) appearing in (6.2.4) were themselves random. The next two examples
are special cases of (6.2.4) in which a(u), b(u), l'(u), and a(u) are nonrandom.
Example 6.2.1 (Geometric Brownian motion). The stochastic differential equa­
tion for geometric Brownian motion is
dS(u) = aS(u) du + aS(u) dW(u).

In the notation of (6.2.1), {3(u, x) = ax and l'(u, x) = ax. We know the formula
for the solution to this stochastic differential equation when the initial time
is zero and the initial position is namely
S(O),
S(t) = S(O) exp { aW(t) + (a- �a [2] t
) }·



Similarly, for T 2 t,
S(T) = S(O) exp aW(T) + (a- a [2] ) T }·
{              


Dividing by we obtain
S(T) S(t),


6.2 Stochastic Differential Equations 265
                  - ) }·
{ (



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-284-0.png)



(                   - )
}·



this case, we use the dummy variable r rather than x, and {3(u, r) = a(u) ­
b(u)r, -y(u, r) = u(u). Let us take the initial condition R(t) = r. We can solve
the stochastic differential equation by first using the stochastic differential
equation to compute



d( eiou b(v)dv R(u)) = eiou b(v)dv (b(u)R(u) du + dR(u))

= eiou b(v)dv (a(u) du + u(u) dW(u)).



Integrating both sides from t to T and using the initial condition R(t) = r,
we obtain the formula


eJ:J' b(v)dvR(T) = rei; b(v)dv+ eiou b(v)dva(u) du+ eiou b(v)dvu(u) dW(u),
### 1T 1T



which we can solve for R(T):



R(T) = re- It [b] (v) [d] v + e- I:; [b] (v) [d] va(u) du + e- I:; [b] (v) [d] vu(u) dW(u).
### 1T 1T



This is an explicit formula for the solution R(T). The right-hand side of the
final equation does not involve the interest rate process R(u) apart from the
initial condition R(t) = r; it contains only this initial condition, an integral
with respect to time, and an Ito integral of given functions. Note also that
the Brownian motion path between times t and T only enters this formula.
Recall from Theorem 4.4.9 that the Ito integral

of the nonrandom integrand e- I:; [b] (v) [d] vu(u) is normally distributed with mean
zero and variance e-2I:; b(v)dvu2(u) du. The other terms appearing in the
It


266 6 Connections with Partial Differential Equations



formula above for R(T) are nonrandom. Therefore, under the risk-neutral
measure IP, R(T) is normally distributed with mean



re- [ftb(v)dv ] + [[T ] e [- f:; b(v)dv] o:(u) du



and variance
e- [2] J [:; b] (v) [d] vu [2] (u) du.
lT



In particular, there is a positive probability that R(T) is negative. This is one
of the principal objections to the Hull-White model. D
Example 6.2.3 {Cox-Ingersoll-Ross interest rate model}. In the Cox-Ingersoll­
Ross (CIR) model, the interest rate is given by the stochastic differential
equation
dR(u) = (a - bR(u)) du + u.J dW(u), (6.2.5)
where a, b, and u are positive constants. Suppose an initial condition R(t) = r
is given. Although there is no formula for R(T), there is one and only one
solution to this differential equation starting from the given initial condition.
This solution can be approximated by Monte Carlo simulation, and many
of its properties can be determined, even though we do not have an explicit
formula for it. For instance, in Example 4.4.11, the mean and variance of R(T)
were computed when the initial time is t = 0 and the initial interest rate is
R(O).
Unlike the interest rate in the Hull-White model, the interest rate in the
Cox-Ingersoll-Ross model cannot take negative values. When the interest rate
approaches zero, the term u.J dW(u) also approaches zero. With the
volatility disappearing, the behavior of the interest rate near zero depends on
the drift term a - bR(u), and this is a > 0 when R(u) = 0. The positive drift
prevents the interest rate from crossing zero into negative territory.
More information about the solution to (6.2.5) is provided in Exercise 6.6
and Remark 6.9.1 following that exercise. D



6.3 The Markov Property


Consider the stochastic differential equation (6.2.1). Let 0 � t � T be given,
and let h(y) be a Borel-measurable function. Denote by

g(t, x) = IE1• [x] h(X(T)) (6.3.1)

the expectation of h(X(T)), where X(T) is the solution to (6.2.1) with initial
condition X(t) = x. (We a ume that IE1• [x] lh(X(T))I < oo.) Note that there is
nothing random about g(t, x); it is an ordinary (actually, Borel-measurable)
function of the two dummy variables t and x.


6.3 The Markov Property 267


If we do not have an explicit formula for the distribution of X(T), we could
compute g(t, x) numerically by beginning at X(t) = x and simulating the
stochastic differential equation. One way to do this would be to use the Euler
method, a particular type of Monte Carlo method: choose a small positive step
size and then set
8,
X(t + = x + f3(t, x)8 + -y(t, x)v'o t:1,
8)

where t:1 is a standard normal random variable. Then set
X(t + = X(t + + /3(t + X(t + + -y(t + X(t + t:2,
28) 8) 8, 8))8 8, 8))vto

where t:2 is a standard normal random variable independent of f l . By this
device, one eventually determines a value for X(T) assuming is chosen so
( 8
that is an integer) . This gives one realization of X(T) (corresponding
to one w) . Now repeat this process many times and compute the average of
h(X(T)) over all these simulations to get an approximate value for g(t, x) .
Note that if one were to begin with a different time t and initial value x, one
would get a different answer (i.e., the answer is a function of t and x). This
dependence on t and x is emphasized by the notation in (6.3.1).

Theorem 6.3.1. Let X(u), u 2 0, be a solution to the stochastic differential Et, [x ]
equation {6.2.1) with initial condition given at time 0. Then, for 0 � t � T,
lE[h(X(T))iF(t)] = g(t, X(t)). (6.3. )
2

While the details of the proof of Theorem 6.3.1 are quite technical and will
not be given, the intuitive content is clear. Suppose the process X(u) begins
at time zero, being generated by the stochastic differential equation (6. .1),
2
and one watches it up to time t. Suppose now that one is asked, based on
this information, to compute the conditional expectation of h(X(T)), where
T ; t. Then one should pretend that the process is starting at time t at its
current position, generate the solution to the stochastic differential equation
corresponding to this initial condition, and compute the expected value of
h(X(T)) generated in this way. In other words, replace X(t) by a dummy x in
order to hold it constant, compute g(t, x) = lEt, [x] h(X(T)), and after computing
this function put the random variable X(t) back in place of the dummy x.
This is the procedure set forth in the Independence Lemma, Lemma 2.3.4, and
it is applicable here because the value of X (T) is determined by the value of
X(t), which is F(t)-measurable, and the increments of the Brownian motion
between times t and T, which are independent of F(t).
Notice in the discussion above that although one watches the stochastic
process X(u) for 0 - u - t, the only relevant piece of information when
computing IE[h(X(T))IF(t)] is the value of X(t). This means that X(t) is a
Markov process see Definition .3.6). We highlight this fact as a corollary.
( 2

Corollary 6.3.2. Solutions to stochastzc differential equations are Markov
processes.


268 6 Connections with Partial Differential Equations


6.4 Partial Differential Equations


The Feynman-Kac Theorem below relates stochastic differential equations and
partial differential equations. When this partial differential equation is solved
(usually numerically), it produces the function g ( t, x) of ( 6.3.1). The Euler
method described in the previous section for determining this function con­
verges slowly and gives the function value for only one pair (t, x). Numerical
algorithms for solving equation (6.4.1) below converge quickly in the case of
one-dimensional x being considered here and give the function g(t, x) for all
values of (t, x) simultaneously. The relationship between geometric Brownian
motion and the Black-Scholes-Merton partial differential equation is a special
case of the relationship between stochastic differential equations and partial
differential equations developed in the following theorems.

Theorem 6.4.1 (Feynman-Kac). Consider the stochastic differential equa­
tion
dX(u) = (J(u, X(u)) du + 'Y(u, X(u)) dW(u). (6.2.1)
Let h(y) be a Borel-measurable function. Fix T > 0, and let t E [0, T] be given.
Define the function
g(t, x) = lE [t,x] h(X(T)). (6.3.1)
{We assume that lEt [,x] ih(X(T))i < oo for all t and x.} Then g(t, x) satisfies
the partial differential equation

gt(t, x) + (J(t, x)gx(t, x) + �'Y [2] (t, x)gxx(t, x) = 0 (6.4.1)

and the terminal condition


g(T, x) = h(x) for all x. (6.4.2)



The proof of the Feynman-Kac Theorem depends on the following lemma.



Lemma 6.4.2. Let X(u) a solution to the stochastic differential equation
be
{6.2.1} with initial condition given at time 0. Let h(y) be a Borel-measurable
function, fix T - 0, and let g(t, x) be given by {6.3.1}. Then the stochastic
process



g(t, X(t)), 0 :; t :; T,
is a martingale.



PROOF: Let 0 :; s :; t :; T be given. Theorem 6.3.1 implies

lE[h(X(T))iF(s)] = g(s, X(s)),

lE[h(X(T))iF(t)] = g(t, X(t)).
Take conditional expectations of the second equation, using iterated condi­
tioning and the first equation, to obtain


6.4 Partial Differential Equations 269


E[ [g(t, X(t))] i [F(s)] ] [= ] E[E [[h(X(T))] i [F(t)] IF(s)] ]
= E[h(X(T))iF(s)]
= g(s, X(s)). D

OUTLINE OF PROOF OF THEOREM 6.4.1: Let X(t) be the solution to the
stochastic differential equation (6.2.1) starting at time zero. Since g(t, X(t))
is a martingale, the net dt term in the differential dg(t, X(t)) must be zero.
If it were positive at any time, then g(t, X(t)) would have a tendency to rise
at that time; if it were negative, g(t, X(t)) would have a tendency to fall.
Omitting the argument (t, X(t)) in several places below, we compute

1
dg(t, X(t)) = 9t dt + 9x dX + 29xx dX dX
1 2
= 9t dt + f3gx dt + 'Y9x dW + 2'Y 9xx dt

= [9t + f3gx + �'Y [2] 9xx] dt + 'Y9x dW

Setting the dt term to zero and putting back the argument (t, X(t)), we obtain

1
9t(t, X(t)) + (3(t, X(t))gx(t, X(t)) + 2'Y [2] (t, X(t))9xx(t, X(t)) = 0

along every path of X. Therefore,

1 2
9t(t,x) + (3(t,x)gx(t, x) + 2'Y (t, x)gxx(t, x) = 0

at every point (t,x) that can be reached by (t, X(t)). For example, if X(t) is
a geometric Brownian motion, then (6.4.1) must hold for every t E [0, T) and
every x > 0. On the other hand, if X(t) is a Hull-White interest rate process,
which can take any positive or negative value, then (6.4.1) must hold for every
t E [O, T) and every x E R D

The general principle behind the proof of the Feynman-Kac theorem is:
1. find the martingale,
2. take the differential, and
3. set the dt term equal to zero.
This gives a partial differential equation, which can then be solved numer­
ically. We illustrate this three-step procedure in the following theorem and
subsequent examples.

Theorem 6.4.3 (Discounted Feynman-Kac). Consider the stochastic
differential equation

dX(u) = (3(u, X(u)) du + 7(u, X(u)) dW(u). (6.2.1)


270 6 Connections with Partial Differential Equations

Let h(y) be a Borel-measumble function and let r be constant. Fix T > 0, and
let t E [0, T] be given. Define the function

f(t, x) lE [t], [x ] [e [-r(T-t)] h(X(T))] . (6.4.3)
=

(We assume that lEt, [x] ih(X(T)) i < oo for all t and x.) Then f(t, x) satisfies
the partial differential equation

ft(t, x) + (3(t, x)fx(t, x) + �-y [2] (t, x)fxx(t, x) = r f(t, x) (6.4.4)

and the terminal condition
f(T, x) h(x) for all x. (6.4.5)
=

OuTLINE OF PROOF: Let X(t) be the solution to the stochastic differential
equation (6.2.1 ) starting at time zero. Then



f(t, X(t)) lE[e [-r(T-t)] h(X(T))iF(t)] .
=



However, it is not the case that f(t, X(t)) is a martingale. Indeed, if 0 � s �
t � T, then



lE[f(t, X(t))IF(s)] lE[lE[e [-r(T-t)] h(X(T))iF(t)] IF(s)]
=

lE[e-r(T-t)h(X(T))iF(s)],
=



which is not the same as



f(s, X(s)) = lE[e [-r(T-] s [)] h(X(T))iF(s)]

because of the differing discount terms. The difficulty here is that in order to
get the martingale property from iterated conditioning, we need the random
variable being estimated not to depend on t, the time of the conditioning. To
achieve this, we "complete the discounting," observing that
e-rtf(t, X(t)) lE[e-r [T] h(X(T))iF(t)] .
=

We may now apply iterated conditioning to show that e-rt f(t, X(t)) is a
martingale. The differential of this martingale is



d(e [-] r [t] f(t, X(t))) = e [-rt] [ - rfdt + ft dt + fx dX + �fxx dX dX]

= e [-] r [t ] [        - r f + ft + f3fx + �'"Y [2 ] fxx] dt + e [-rt] '"Yfx dW



Setting the dt term equal to zero, we obtain (6.4.4). D
Example 6.4.4 {Options on a geometric Brownian motion). Let h(S(T)) be
the payoff at time T of a derivative security whose underlying a et is the
geometric Brownian motion


6.4 Partial Differential Equations 271

dS(u) = aS(u) du + aS(u) dW(u). (6.4.6)

We may rewrite this as

dS(u) = rS(u) du + aS(u) dW(u), (6.4.7)

where W(u) is a Brownian motion under the risk-neutral probability measure
P. Here we a ume that a and the interest rate r are constant. According to
the risk-neutral pricing formula (5.2.31), the price of the derivative security
at time t is
(6.4.8)
Because the stock price is Markov and the payoff is a function of the stock
price alone, there is a function v(t,x) such that V(t) = v(t, S(t)). Moreover,
the function v( t, x) must satisfy the discounted partial differential equation
(6.4.4). This is the Black-Scholes-Merton equation

1 2 2
Vt (t, x) + rxvx(t,x) + 20' x Vxx (t,x) = rv(t,x). (6.4.9)

When the underlying a et is a geometric Brownian motion, this is the right
pricing equation for a European call, a European put, a forward contract, and
any other option that pays off some function of S(T) at time T.
Note that to derive (6.4.9) we use the discounted partial differential equa­
tion (6.4.4) when the stochastic differential equation for the underlying process
is (6.4.7) rather than (6.4.6) (i.e., we have rxvx(t, x) in (6.4.9) rather than
axvx (t,x)). This is because we are computing the conditional expectation in
(6.4.8) under the risk-neutral measure P and hence must use the differential

- [uation that represents S(u) in terms of W(u), the Brownian motion under ]
IP'. In other words, we are using the Discounted Feynman-Kac Theorem with
W ( u) replacing W ( u) and P replacing lP'. D

In the previous example, if a were a function of time and stock price (i.e.,
a ( t, x)), then the stock price would no longer be a geometric Brownian motion
and the Black-Scholes-Merton formula would no longer apply. However, one
can still solve for the option price by solving the partial differential equation
( 6.4. 9), where now the constant a [2 ] is replaced by a [2 ] ( t, x):

1 2
Vt (t,x) + rxvx(t,x) + 20' (t,x x Vxx) [2 ] (t,x) = rv(t,x). (6.4.10)

This equation is not difficult to solve numerically.
It has been observed in markets that if one a umes a constant volatility,
the parameter a that makes the theoretical option price given by (6.4.9) agree
with the market price, the so-called implied volatility, is different for options
having different strikes. In fact, this implied volatility is generally a convex
function of the strike price. One refers to this phenomenon as the volatility
smile.

V(t) = E[e-r(T-t)h(S(T))iF(t)] .


272 6 Connections with Partial Differential Equations


One simple model with nonconstant volatility is the constant elasticity of
variance (CEV) model, in which u(t,x) = ux6- [1 ] depends on x but not t. The
parameter 8 E (0, 1) is chosen so that the model gives a good fit to option
prices across different strikes at a single expiration date. For this model, the
stock price is governed by the stochastic differential equation

dS(t) = rS(t) dt + uS6(t) dW(t).

The volatility uS6- [1] (t) is a decreasing function of the stock price.
When one wishes to a ount for different volatilities implied by options
expiring at different dates as well as different strikes, one needs to allow u to
depend on t as well as x. This function u(t, x) is called the volatility surface
(see Exercise 6.10).


6.5 Interest Rate Models


The simplest models for fixed income markets begin with a stochastic differ­
ential equation for the interest rate, e.g.,

dR(t) = {3(t, R(t)) dt + -y(t, R(t)) dW(t), (6.5.1)

where W(t) is a Brownian motion under a risk-neutral probability measure iP.
In these models, one begins with a risk-neutral measure iP and uses the risk­
neutral pricing formula to price all a ets. This guarantees that discounted
a et prices are martingales under the risk-neutral measure, and hence there is
no arbitrage. The issue of calibration of these models (i.e., choosing the model
and the model parameters so that they give a good fit to market prices) is
not discussed in this text.
Models for the interest rate R(t) are sometimes called short-rate models
because R(t) is the interest rate for short-term borrowing. When the interest
rate is determined by only one stochastic differential equation, as is the case
in this section, the model is said to have one factor. The primary shortcoming
of one-factor models is that they cannot capture complicated yield curve be­
havior; they tend to produce parallel shifts in the yield curve but not changes
in its slope or curvature.
The discount process is as given in (5.2.17),

D(t) = e [- J; ][R(s)ds],


= .
ef; R(s)ds
D(t)

This is the value at time t of one unit of currency invested in the money market
account at time zero and continuously rolled over at the short-term interest

and we denote the money market account price process to be


6.5 Interest Rate Models 273



rate R(s), s 2: 0. As discussed following (5.2.18), we have the differential
formulas
1 R(t)
dD(t) = -R(t)D(t) dt, d D(t) = D(t) dt. ( )

A zero-coupon bond is a contract promising to pay a certain "face" amount,
which we take to be 1, at a fixed maturity date T. Prior to that, the bond
makes no payments. The risk-neutral pricing formula (5.2.30) says that the
discounted price of this bond should be a martingale under the risk-neutral
measure. In other words, for 0 : t : T, the price of the bond B(t, T) should
satisfy
D(t)B(t, T) = [IE] [D(T)i.F(t)] . (6.5.2)
(Note that B(T, T) = 1.) This gives us the zero-coupon bond pricing formula
B(t, T) = R(s)ds .F(t), (6.5.3)
JE

[e-ft I ]



which we take as a definition. Once zero-coupon bond prices have been com­
puted, we can define the yield between times t and T to be
1
Y(t, T) = -T _ t [log ][B(t, T) ]



_ t [log ][B(t, T) ]



or, equivalently,
B(t,T) = e [-Y(t,T)(T-t)] _
The yield Y(t, T) is the constant rate of continuously compounding interest
between times t and T that is consistent with the bond price B(t, T). The 30year rate at time t is Y(t, 30+t); this is an example of a long rate. Notice that
once we adopt a model (6.5. 1) for the short rate, the long rate is determined
by the formulas above; we may not model the long rate separately.
Since R is given by a stochastic differential equation, it is a Markov process
and we must have
B(t, T) = f(t, R(t))
for some function f(t, r) of the dummy variables t and r. This is a slight step
beyond the way we have used the Markov property previously because the
random variable It R( [s] ) [ds ] being estimated in (6.5.3) depends on the path
segment R(s), t : s : T, not just on R(T). However, the only relevant part
eof the path of R before time t is its value at time t, and so the bond price
B(t, T) must be a function of time t and R(t).
To find the partial differential equation for the unknown function f ( t, r),
we find a martingale, take its differential, and set the dt term equal to zero.
The martingale in this case is D(t)B(t, T) = D(t)f(t, R(t)). Its differential is
d(D(t)f(t, R(t)))=J(t, R(t)) dD(t) + D(t) df(t, R(t))



=D(t) [ -Rf dt + ft dt + frdR + frr dRdR
###### � ]



=D(t) [ -RJ + ft + /3/r + 7 [2 ] /rr dt + D(t)'Yfr dW.
###### � ]


274 6 Connections with Partial Differential Equations


Setting the dt term equal to zero, we obtain the partial differential equation
ft(t, r) + {J(t, r)fr(t, r) + fY 1 2 (t, r)frr(t, r) = r f(t, r). (6.5.4)

We also have the terminal condition



f(T,r) = 1 for all r

because the value of the bond at maturity is its face value 1.



(6.5.5)



Example 6.5.1 (Hull-White interest rate model}. In the Hull-White model,
the evolution of the interest rate is given by


models.
Furthermore,


( - C'(t, T) + b(t)C(t, T) - 1)r

[

-A'(t, T) - a(t)C(t, T) + T) f(t, r) = 0. (6.5.7
�a2(t)C2(t, )
###### ]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-293-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-293-1.png)
6.5 Interest Rate Models 275


Because this equation must hold for all r, the term that multiplies r in this
equation must be zero. Otherwise, changing the value of r would change the
value of the left-hand side of (6.5.7), and hence it could not always be equal
to zero. This gives us an ordinary differential equation in t:
=               - 1. (6.5.8)
C'(t,T) b(t)C(t,T)

Setting this term equal to zero in (6.5.7), we now see that

= -a(t)C(t, + (6.5.9
A'(t, T) T) �a2(t)C2(t, T). )

The terminal condition (6.5.5) must hold for all r, and this implies that
C(T, T) = A(T, T) = 0. Equations (6.5.8) and (6.5.9) and these terminal con­
ditions provide enough information to determine the functions and
A(t, T)
C(t, for 0 � t � They are
T) T.
= [1][T ] e [-][ J,• ][b(v)dv] ds, 6.5.10
C(t, T) ( )
= [1][T ] a(s)C(s, ds. 6.5.11
A(t, T) T) - �a2(s)C2(s, T)) ( )
###### (

It is clear that these formulas give functions that satisfy = =
C(T, T) A(T, T)
0. The verification that these formulas provide the unique solutions to (6.5.8)
and (6.5.9) is Exercise 6.3.
conclusion, we have derived an explicit formula for the price of a zero­
In
coupon bond as a function of the interest rate in the Hull-White model. It
is
B(t, T) = [e-R(t)C(t,T)-A(t,T)], 0 [� ] t [� ] T,
where C(t, and are given by 6.5.10 and (6.5.11).
T) A(t, T) ( ) 0
Example 6.5.2 (Cox-Ingersoll-Ross interest rate model). In the CIR model,
the evolution of the interest rate is given by

dR(t) = a - R t dt + dW(t),
( b ( )) ay'R{i)

where a, and are positive constants. The partial differential equation
b, a
(6.5.4) for the bond price becomes
1
ft(t, r) + (a - br)fr(t, r) + 2a 2 r frr(t, r) = r f(t, r). (6.5.12)

Again, we initially guess and subsequently verify that the solution has the
form

The Cox-Ingersoll-Ross model is another example of an affine yield model.
Substitution into the differential equation (6.5.12) gives
f(t, r) = e-rC(t,T)-A(t,T).



(6.5.10)

(6.5.11)



dR(t) = a - R t dt + dW(t),
( b ( )) ay'R{i)


276 6 Connections with Partial Differential Equations


-A'(t, T) - aC(t, T)] f(t, r) = 0. (6.5.13)

We can again conclude that the term multiplying r must be zero and then
conclude that the other term must also be zero, thereby obtaining two ordinary
differential equations in t:

[( - C'(t, T) + bC(t, T) + T) - 1)r
�a2C2 (t,



C'(t, T) = bC(t, T) + T) - 1,
�a [2] C [2] (t,
A'(t, T) = -aC(t, T).



(6.5.14)

(6.5.15)



The solutions to these equations satisfying the terminal conditions C(T, T) =
A(T, T) = 0 are







![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-295-0.png)













is a martingale. The differential of the discounted call price is


6.6 Multidimensional Feynman-Kac Theorems 277



d(D(t)c(t, R(t))) = c(t, R(t)) dD(t) + D(t) dc(t, R(t))



=

= D [ -Rcdt + Ct dt + Cr dR + Crr dRdR
###### � ]



= D [ -Rc + Ct + f3cr + ')' [2] Crr dt + D')'Cr dW.
###### � ]



Setting the dt term to zero, we obtain the partial differential equation



1
Ct t, r) ( + {3(t, r) cr(t, r) + 2, 2 (t, r)crr(t, r) = rc(t,r).

This is the same partial differential equation that governs f(t, r). However,
c(t, r) and f(t, r) have different terminal conditions. The terminal condition
for c(t, r) is
c(T1,r) = (f(TI.r) - K) [+ ] for all r.
One can use these conditions to numerically determine the call price function
c(t,r).

[]


6.6 Multidimensional Feynman-Kac Theorems


The Feynman-Kac and Discounted Feynman-Kac Theorems, Theorems 6.4.1
and 6.4.3, have multidimensional versions. The number of differential equa­
tions and the number of Brownian motions entering those differential equa­
tions can both be larger than one and do not need to be the same. We illustrate
the general situation by working out the details for two stochastic differential
equations driven by two Brownian motions.
Let W(t) = (W1(t), W2(t)) be a two-dimensional Brownian motion (i.e., a
vector of two independent, one-dimensional Brownian motions) . Consider two
stochastic differential equations
dX1 (u) = fJ1 (u, X1 (u), X2(u)) du +I'll (u, X1 (u), X2(u)) dW1 (u)

=
dX2(u) fJ2(u, X1 (u), X2(u)) du + /'21 (u, X1 (u), X2(u)) dW1 (u)


The solution to this pair of stochastic differential equations, starting at
X1(t) = x1 and X2(t) = x2, depends on the specified initial time t and the
initial positions x1 and x2. Regardless of the initial condition, the solution is
a Markov process.
Let a Borel-measurable function h(y1, Y2) be given. Corresponding to the
initial condition t, x1, x2, where 0 � t � T, we define
g(t,x1,x2) = 1Et [,x] 1, [x] 2h(X1(T),X2(T)), (6.6.1)
f(t,x1,x2) = 1Et, [x] ., [x] 2 [e -r [(T] -t [)] h(X1(T),X2(T))] . (6.6.2)

+1'12(u, X1 (u), X2(u)) dW2(u),
+1'22(u, X1 (u), X2(u)) dW2(u).


278 6 Connections with Partial Differential Equations


Then

9t + f319xl + f329x2
1 2 2 1 2 2
+2(1'11 + 'Y12)9x1x1 + h'n/'21 + /'121'22)9xlx2 + 2h'21 + 1'22 9x2x2 ) = 0,
(6.6.3)
ft + f3dxl + f32/x2
1 2 2 2 2
) 1 ( ) = r f.
+2 h'n + 'Y12)fx1x1 + h'n /'21 + /'12/'22 fx1x2 + 2 1'21 + 1'22 fx2x2
(6.6.4)

Of course, these functions also satisfy the terminal conditions

g(T, XI, X2) = f(T, XI, X2) = h(xb X2) for all X1 and X2.

Equations (6.6.3) and (6.6.4) are derived by starting the pair of pro­
cesses X1, X2 at time zero, observing that the processes g(t, X1(t), X2(t))
and e-rtf(t, X1(t), X2(t)) are martingales, taking their differentials, and set­
ting the dt terms equal to zero. When taking the differentials, one uses the
fact that W1 and W2 are independent. We leave the details to the reader in
Exercise 6.5. This exercise also provides the counterparts of (6.6.3) and (6.6.4)
when W1 and W2 are correlated Brownian motions.
Example 6.6.1 (Asian option). We show by example how the Discounted
Feynman-Kac Theorem can be used to find prices and hedges, even for path­
dependent options. The option we choose for this example is an Asian option.
A more detailed discussion of this option is presented in Section 7.5. The
payoff we consider is



V(T) � S(u) du - K
### (� [ f



where S(u) is a geometric Brownian motion, the expiration time T is fixed
and and K is a positive strike pric� In terms of the Brownian mo­
tion W(u) under the risk-neutral measure IP', we may write the stochastic
differential equation for S ( u) as

dS(u) = rS(u) du + aS(u) dW(u). (6.6.5)

Because the payoff depends on the whole path of the stock price via its
integral, at each time t prior to expiration it is not enough to know just the
stock price in order to determine the value of the option. We must also know
the integral of the stock price,


Y(t) = S(u) du,
1t


6.6 Multidimensional Feynman-Kac Theorems


up to the current time t. Similarly, it is not enough to know just the integral
Y(t). We must also know the current stock price S(t). Indeed, for the same
value of Y(t), the Asian option is worth more for high values of S(t) than for
low values because the high values of S(t) make it more likely that the option
will have a high payoff.
For the process Y(u), we have the stochastic differential equation

dY(u) = S(u) du. (6.6.6)

Because the pair of processes (S(u), Y(u)) is given by the pair of stochastic
differential equations (6.6.5) and (6.6.6), the pair of processes (S(u), Y(u)) is
a two-dimensional Markov process.
Note that Y(u) alone is not a Markov process because its stochastic dif­
ferential equation involves the process S(u). However, the pair (S(u), Y(u))
is Markov because the pair of stochastic differential equations for these pro­

                             
279



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-298-0.png)

Because the pair of processes (S(u), Y(u)) is Markov, this can be written as
some function of the time variable t and the values at time t of these processes.
In other words, there is a function v(t, x, y) such that



v(t, S(t), Y(t)) = V(t) = e-r [(T] -t) Y(T) - K F(t) .
E [
###### (� ) [+]
### I ]



Note that this function must satisfy the terminal condition



v(T, x, y) = K for all x and y. (6.6.7)
(�- ) [+]



Using iterated conditioning, it is easy to see that the discounted option
value e-rtv(t, S(t), Y(t)) is martingale. Its differential is



= e [-] r [t ] rv dt + dt + dS + dY + dS dS + dS dY

[- Vt Vx Vy �Vxx Vxy

+ vyy dY dY

      ###### ]

d(e-rtv(t, S(t), Y(t)))


280 6 Connections with Partial Differential Equations


###### ]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-299-0.png)



equation
(6.6.11)
If we sell the Asian option at time zero for v(O, 8(0), 0) and use this as the
initial capital for a hedging portfolio (i.e., take X(O) = v(O, 8(0), 0)), and at
each time t use the portfolio process Ll(t) = vx(t, S(t), Y(t)), then we will
have
d(e [-rt ] X(t)) [= ] d(e [-rt] v(t, S(t), Y(t)))
for all times t, and hence



X(T) = v(T, S(T), Y(T)) = �Y(T) ( K) +.



This procedure hedges a short position in the Asian option. We have obtained
the usual formula that the number of shares held to hedge a short position
in the option is the derivative of the option value with respect to the under­
lying stock price. However, the Asian option price is the solution to a partial
differential equation that contains a term xvy(t, x, y) that does not appear in
the partial differential equation for the price of a European option. 0



6.7 Summary


When the underlying price of an a et is given by a stochastic differential
equation, the a et price is Markov and the price of any non-path-dependent
derivative security based on that a et is given by a partial differential equa­
tion. In order to price path-dependent securities, one first seeks to determine


6.8 Notes 281


the variables on which the path-dependent payoff depends and then intro­
duce one or more additional stochastic differential equations in order to have
a system of such equations that describes the relevant variables. If this can
be done, then again the price of the derivative security is given by a partial
differential equation.
This leads to the following four-step procedure for finding the pricing dif­
ferential equation and for constructing a hedge for a derivative security.
1. Determine the variables on which the derivative security price depends. In
addition to time t, these are the underlying a et price S(t) and possibly
other stochastic processes. We call these stochastic processes the state
processes. One must be able to represent the derivative security payoff in
terms of these state processes.
2. Write down a system of stochastic differential equations for the state pro­
cesses. Be sure that, except for the driving Brownian motions, the only
random processes appearing on the right-hand sides of these equations
are the state processes themselves. This ensures that the vector of state
processes is Markov.
3. The Markov property guarantees that the derivative security price at each
time is a function of time and the state processes at that time. The dis­
counted option price is a martingale under the risk-neutral measure. Com­
pute the differential of the discounted option price, set the dt term equal
to zero, and obtain thereby a partial differential equation.
4. The terms multiplying the Brownian motion differentials in the discounted
derivative security price differential must be matched by the terms multi­
plying the Brownian motion differentials in the evolution of the hedging
portfolio value; see (5.4.27). Matching these terms determines the hedge
for a short position in the derivative security.


6.8 Notes


Conditions for the existence and uniqueness of solutions to stochastic differen­
tial equations are provided by Karatzas and Shreve [101], Chapter 5, Section
2, who also show in Chapter 5, Section 4, that solutions to stochastic differ­
ential equations have the Markov property. This is based on work of Stroock
and Varadhan [151]. The ideas behind the Feynman-Kac Theorem, although
not the presentation we give here, trace back to Feynman [65] and Kac [99].
Hull and White presented their interest rate model in [88], in which they
generalized a model of Vasicek [154] to allow time-varying coefficients. The
origin of the Cox-Ingersoll-Ross model is [41], where one can find a closed­
form formula for the distribution of the interest rate in the model. These are
examples of affine-yield models, a cla identified by Duffie and Kan [58]. They
are sometimes called multifactor CIR models.
Example 6.6.1 obtains a partial differential equation for the price of an
Asian option but does not address computational issues. In the form given


282 6 Connections with Partial Differential Equations


here, the equation is difficult to handle numerically. Veeer [156] and Rogers and
Shi [139] present transformations of this equation that are numerically more
stable. See also Andreasen [4] for an application of the change-of-numeraire
idea of Chapter 9 to discretely sampled Asian options. The transformation of
Veeer and its use for both continuously sampled and discretely sampled Asian
options is presented in Section 7.5.
The Heston stochastic volatility model of Exercise 6. 7 is taken from Heston

[84]. Exercise 6.10 on implying the volatility surface comes from Dupire [61].
The same idea for binomial trees was worked out by Derman et al. [50], [51].


6.9 Exercises


Exercise 6.1. Consider the stochastic differential equation

dX(u) = (a(u) + b(u)X(u)) du + ('Y(u) + u(u)X(u)) dW(u), (6.2.4)

where W(u) is a Brownian motion relative to a filtration F(u), u � 0, and we
allow a(u), b(u), "Y(u), and u(u) to be processes adapted to this filtration. Fix
an initial time t � 0 and an initial position x E Define
:R



Z(u) = exp u(v) dW(v) + b(v) - u [2] (v) dv,
                    - }
###### {lu lu ( )



v .



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-301-0.png)




Show that X(u) = Y(u)Z(u) solves the stochastic differential equation
(6.2.4) and satisfies the initial condition X(t) = x.

Exercise 6.2 (No-arbitrage derivation of bond-pricing equation). In
Section 6.5, we began with the stochastic differential equation (6.5.1) for the
interest rate under the risk-neutral measure JP, used the risk-neutral pricing
formula (6.5.3) to consider a zero-coupon bond maturing at time T whose
price B(t, T) at time t before maturity is a function f(t, R(t)) of the time
and the interest rate, and derived the partial differential equation (6.5.4) for
the function f(t, r) . In this exercise, we show how to derive this partial dif­
ferential equation from no-arbitrage considerations rather than by using the
risk-neutral pricing formula.


6.9 Exercises 283


Suppose the interest rate is given by a stochastic differential equation

dR(t) = a(t, R(t)) dt + 7(t, R(t)) dW(t), (6.9.1)

where W(t) is a Brownian motion under a probability measure lP' not a umed
to be risk-neutral. Assume further that, for each T, the T-maturity zero­
coupon bond price is a function f(t, R(t), T) of the current time t, the current
interest rate R(t), and the maturity of the bond T. We do not a ume that
this bond price is given by the risk-neutral pricing formula (6.5.3).
Assume for the moment that fr(t, r, T) =/:- 0 for all values of r and 0 : t :
T, so we can define
1 1 2
f3(t, r, [T] ) [= ]  - fr(t, r, T) [ - [r f(t, r], [T] ) + ft [(t, r, ][T] ) + 2'Y [(t, r)f] rr [(t, r], [T] ) ] [, ]

(6.9.2)

and then have
1 2
ft(t, r, T) + {J(t, r, T)fr(t, r, T) + 2'Y (t, r)frr(t, r, T) = r f(t, r, T) . (6.9.3)

Equation (6.9.3) will reduce to (6.5.4) for the function f(t, r, T) if we can show
that {J(t, r, T) does not depend on T.

(i) Consider two maturities 0 < T1 < T2, and consider a portfolio that at each
time t : T1 holds Ll1(t) bonds maturing at time T1 and Ll2(t) bonds ma­
turing at time T2, financing this by investing or borrowing at the interest
rate R(t). Show that the value of this portfolio satisfies



d(D(t)X(t))



= Ll1(t)D(t) R(t)f(t, R(t), TI ) + ft(t, R(t), T1 )
###### [1 2
+a(t, R(t))fr(t, R(t), T1 ) + 2'Y (t, R(t))frr(t, R(t), Tt ) ] dt



+Ll2(t)D(t) R(t)f(t, R(t), T2) + ft(t, R(t), T2)
###### [


1 2
+a(t, R(t))fr(t, R(t), T2) + 2'Y (t, R(t))frr(t, R(t), T2) dt ]



+D(t)'Y(t, R(t)) [Llt(t)fr(t, R(t), Tt) + Ll2(t)fr(t, R(t), T2)) dW(t)
= Llt(t)D(t) [a(t, R(t)) - {J(t, R(t), TI)]fr(t, R(t), Tt ) dt
+Ll2(t)D(t) [ a(t, R(t)) - {J(t, R(t), T2)) fr(t, R(t), T2) dt
+D(t)'Y(t, R(t)) [Llt(t)fr(t, R(t), TI ) + Ll2(t)fr(t, R(t), T2)) dW(t).
(6.9.4)


284 6 Connections with Partial Differential Equations


(ii) Denote

1 if X                           - 0,
sign(x) = 0 if x = 0,
### { -1 if X < 0,

and

S(t) = sign { [.B(t, R(t), T2) -,B(t, R(t), TI)] fr(t, R(t), TI)fr(t, R(t), T2)} .

Show that the portfolio processes Ll1(t) = S(t)fr(t, R(t), T2) and Ll2(t) =
-S(t)fr(t, R(t), T1) result in arbitrage unless,B(t, R( t), TI) =,B(t, R(t), T2).
Since T1 and T2 are arbitrary, we conclude that,B(t, r, T) does not depend
on T.
(iii) Now let a maturity T - 0 be given and consider a portfolio Ll(t) that
invests only in the bond of maturity T, financing this by investing or
borrowing at the interest rate R(t). Show that the value of this portfolio
satisfies
d(D(t)X(t))
= Ll(t)D(t) [ - R(t)f(t, R(t), T) + ft(t, R(t), T)

+a(t, R(t))fr(t, R(t), T) + �-l(t, R(t))frr(t, R(t), T)] dt
+D(t)Ll(t)'y(t, R(t))fr(t, R(t), T) dW(t). (6.9.5)

Show that if fr(t, r, T) = 0, then there is an arbitrage unless
1 2
ft(t, r, T) + 2'�' (t, r)frr(t, r, T) = r f(t, r, T). (6.9.6)

In other words, if fr(t, r, T) = 0, then (6.9.3) must hold no matter how
we choose,B(t, r, T).

In conclusion, we have shown that if trading in the zero-coupon bonds presents
no arbitrage opportunity, then for all t, r, and T such that fr(t, r, T) =/= 0, we
can define,B(t, r) by (6.9.2) because the right-hand side of (6.9.2) does not
depend on T. We then have
1 2
ft(t, r, T) +,B(t, r)fr(t, r, T) + 2'�' (t, r)frr(t, r, T) = r f(t, r, T), (6.9.7)

which is (6.5.4) for the T-maturity bond. If fr(t, r, T) = 0, then (6.9.6) holds,
so (6.9.7) must still hold, no matter how,B(t, r) is defined. If we now change
to a measure JPi under which

1
W(t) = W(t) + 'Y(u, R(u)) [a(u, R(u)) -,B(u, R(u))] du

is a Brow�ian motion, then (6.9.1) can be rewritten as (6.5.1). The probability
measure is risk-neutral.
lP'


6.9 Exercises 285



Exercise 6.3 (Solution of Hull-White model). This exercise solves the
ordinary differential equations (6.5.8) and (6.5.9) to produce the solutions
T) and T) given in (6.5.10) and (6.5.1 1).
C(t, A(t,

i Use equation (6.5.8) with s replacing to show that
( ) t



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-304-0.png)



Show that





(6.9.8)


(6.9.9)


(6.9. 10)









(6.9. 1 1)




286 6 Connections with Partial Differential Equations



(iv) Show that
cp '(t) = c1 e -( [!.] 2 b [+')'] )(T-t) - c2e -( [!.] 2 b- [')'] )(T-t) (

                                                                                                     Use the fact that C(T, T) = 0 to show that c1 = c2.
(v) Show that



(6.9. 12)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-305-0.png)





(6.9.13)


(6.9.14)


Exercise 6.6 (Moment-generating function for Cox-Ingersoll-Ross
process).
(i) Let W1, . . ., Wd be independent Brownian motions and let a and a be pos­
itive constants. For = 1, . . ., d, let X3(t) be the solution of the Ornstein­
j
Uhlenbeck stochastic differential equation


![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-306-0.png)



6.9 Exercises 287


(6.9.15)


(6.9.16)





(
ii Define
( )

]



(6.9.17)


(6.9.18)


(6.9.19)


(6.9.20)









iv Part iii shows that R(t) given by (6.9.18) is the sum of squares of in­
( ) ( )
dependent, identically distributed, normal random variables and hence
has a noncentral x [2 ] distribution, the term "noncentral" referring to the


288 6 Connections with Partial Differential Equations



fact that J.L(t) = [lE] Xj (t) is not zero. To compute the moment-generating
function of R(t), first compute the moment-generating function



R(t), first compute the moment-generating function





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-307-0.png)












6.9 Exercises 289



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-308-0.png)

correlated Brownian motions under ff with

it is a two-dimensional Markov process.

(6.9.23).





equation


the boundary conditions

(



s-+oo S    - K [= ][1 ]
v-+oo



(6.9.27)
(6.9.28)
(6.9.29)

(6.9.30)

(6.9.31)



(6.9.30)



to obtain (6.9.26).


###### ( )



(6.9.32)


(6.9.33)



( )


290 6 Connections with Partial Differential Equations


in the region 0 t < T, -oo < x < oo, and v 0. Show that if we define
::; ;

c(t, s, v) = sf(t, log s, v) - e-r [(T]        - [t] ) Kg(t, log s, v), (6.9.34)

then c(t, s, v) satisfies the partial differential equation (6.9.26).
(i) Suppose a pair of processes (X(t), V(t)) is governed by the stochastic
differential equations


dX(t) = r + V(t) dt + [JV{i)] dW1(t), (6.9.35)
(              - )

dV(t) = a       - bV(t) + paV(t)) dt + a dW2(t), (6.9.36)
( JV{t)

where W1 (t) and W2(t) are Brownian motions under some probability
measure lP with dW1(t) dW2(t) = pdt. Define

J(t, x, v) = IE [t], [x], [v] n{X(T)�Iog K} · (6.9.37)

Show that f(t, x, v satisfies the partial differential equation (6.9.32) and
)
the boundary condition

f(T, x, v) = H{x�Iog K} for all X E IR., v 2: 0. (6.9.38)

iv Suppose a pair of processes (X(t), V(t)) is governed by the stochastic
( )
differential equations



dV(t) = a - bV(t)) dt + a dW2(t),
( JV{t)

dX(t) = r - V(t) dt + JV{i)dW1(t),
(     - )



(6.9.39)


(6.9.40)



where W1 (t) and W2(t) are Brownian motions under some probability
measure lP with dW1 (t) dW2(t) = pdt. Define

g(t, x, v) = IE [t], [x], [v] n{X(T)�Iog K} · (6.9.41)

Show that g(t, x, v) satisfies the partial differential equation (6.9.33) and
the boundary condition

g(T, x, v) = H{x�Iog K} for all X E JR., V 2: 0. (6.9.42)

v Show that with f(t, x, v) and g(t,x, v) as in iii and iv, the function
( ) ( ) ( )
c(t, x, v) of (6.9.34) satisfies the boundary condition (6.9.27).

Remark 6.9.2. In fact, with f(t, x,v) and g(t, x, v) as in iii and iv, the
( ) ( )
function c(t, x, v) of (6.9.34) satisfies all the boundary conditions (6.9.27)­
(6.9.31) and is the function appearing on the left-hand side of (6.9.25).


6.9 Exercises 291


Exercise 6.8 (Kolmogorov backward equation). Consider the stochas­
tic differential equation

dX(u) = f3(u, X(u)) du + -y(u, X(u)) dW(u).

We a ume that, just as with a geometric Brownian motion, if we begin a
process at an arbitrary initial positive value X(t) = x at an arbitrary initial
time t and evolve it forward using this equation, its value at each time T > t
could be any positive number but cannot be less than or equal to zero. For
0 ::; t < T, let p(t, T, x, y) be the transition density for the solution to this
equation (i.e., if we solve the equation with the initial condition X(t) = x,
then the random variable X(T) has density p(t, T, x, y) in the y variable). We
are a uming that p(t, T, x, y) = 0 for 0 ::; t < T and y ::; 0.
Show that p(t, T; x, y) satisfies the Kolmogorov backward equation



1 2
-pt(t, T, x, y) = {3(t, x)px(t, T, x, y) + (t, X)Pxx(t, T, x, y). (6.9.43)
2'Y



(Hint: We know from the Feynman-Kac Theorem, Theorem 6.4.1, that, for
any function h(y), the function



g(t, x) = lE [t], [x] h(X(T)) =
100 h(y)p(t,T,x,y)dy

satisfies the partial differential equation
1 2
gt(t, x) + {3(t, x)gx(t, x) + 2'Y (t, x)gxx(t, x) = 0.



(6.9.44)


(6.9.45)



Use (6.9.44) to compute gt, gx, and gxx, and then argue that the only way
(6.9.45) can hold regardless of the choice of the function h(y) is for p(t, T, x, y)
to satisfy the Kolmogorov backward equation.)

Exercise 6.9 (Kolmogorov forward equation). (Also called the Fokker­
Planck equation). We begin with the same stochastic differential equation,

dX(u) = f3(u, X(u)) du + -y(u, X(u)) dW(u), (6.9.46)

as in Exercise 6.8, use the same notation p(t, T, x, y) for the transition density,
and again a ume that p(t, T, x, y) = 0 for 0 ::; t < T and y ::; 0. In this
problem, we show that p(t, T, x, y) satisfies the Kolmogorov forward equation

{) {) 1 {) [2 ] 2

[-]
{)T [p(t][,][ T][,][ x][, y][) ][=] ay [(f3(t][, y][)p(t][,] [T][,][ x][, y][)) + ] 2 0Y [2 ] [('Y (T, y)p(t, T, x, y)) . ]
(6.9.47)
In contrast to the Kolmogorov backward equation, in which T and y were
held constant and the variables were t and x, here t and x are held constant
and the variables are y and T. The variables t and x are sometimes called the
backward variables, and T and y are called the forward vanables.


292 6 Connections with Partial Differential Equations



(i) Let b be a positive constant and let hb(Y) be a function with continuous
first and second derivatives such that hb(x) = 0 for all x ::; 0, h/,(x) = 0
for all x ; b, and hb(b) = h/,(b) = 0. Let X(u) be the solution to the
stochastic differential equation with initial condition X(t) = x E (0, b),
and use Ito's formula to compute dhb(X(u)).
(ii) Let 0 t < T be given, and integrate the equation you obtained in (i)
::;
from t to T. Take expectations and use the fact that X(u) has density
p(t, u, x, y) in the y-variable to obtain
fo [b ] hb(y)p(t,T, x, y)dy = hb(x) + i [T ] fo [b ] f3(u, y)p(t, u, x, y)h [/,] (y)dydu



T
+ b ''?{u, y)p(t, u, x, y)h�(y)dy.
�i fo



(6.9.48)



(iii) Integrate the integrals J; dy on the right-hand side of (6.9.48) by parts

                                  - · ·
to obtain
fo [b ] hb(y)p(t, T, x, y)dy



= hb(x) - i [T ] fo [b] - [f3(u, y)p(t, u, x, y)] hb(y)dydu





(6.9.49)


(6.9.50)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-311-0.png)










6.9 Exercises 293


This is as much as you need to do for this problem. It is now obvious that if



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-312-0.png)

(6.9.51)















(6.9.54)


(6.9.55)


(6.9.56)






= a [2] (T, K)K [2] p(O, T, [x], K).


294 6 Connections with Partial Differential Equations


You may a ume that



8
y-+oo lim (y - K) 8Y (a2(T,y)y2p(O,T,x,y)) = 0,
lim a [2] (T, y)y [2] p(O, T, x, y) = 0.
y [-+oo ]



(6.9.57)
(6.9.58)



(i) Now use (6.9.53), (6.9.52), (6.9.51), (6.9.54), (6.9.56), and Exercise 5.9 of
Chapter 5 in that order to obtain the equation
CT(O, T, x, K)



= e-rTrK p(O,T,x,y)dy+ �e-rTa2(T,K)K2p(O,T,x,K)
1:



= -rKcK(O,T,x,K) + 1 2 (T,K)K 2 CKK(O,T,x,K). (6.9.59)
2a



This is the end of the problem. Note that under the a umption that
CKK(O, T, x, K) =f. 0, (6.9.59) can be solved for the volatility term a [2] (T, K)
in terms of the quantities cT(O, T, x, K), cK(O, T, x, K), and CKK(O, T, x, K),
which can be inferred from market prices.


This Brownian motion W(t) has drift a under JPi. We further define



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-314-0.png)
296 7 Exotic Options

=
M(T) o:max **:** t::;T W(t). (7.2.2)

Because W(O) 0, we have M(T) ; **:** 0. We also have W(T) < M(T).
Therefore, the pair of random variables (M(t), W(T)) takes values in the
set {(m,w); w � m, m ; **:** 0} shown in Figure 7.2.1.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-315-0.png)


and is zero for other values of m and w.



(7.2.3)



PROOF:
We define the exponential martingale


= =
Z(t) e-<>W(t)-!a2t e-<>W(t)+!a2t, 0 � t � T,



and use Z(T) to define a new probability measure fiD by



=
P(A) Z(T) dP for all A E F.
L



According to Girsanov's Theorem, Theorem5.2.3, W(t) is a Brownian
mo­
tion (with zero drift) under fiD. Theorem 3.7.3 gives us the joint density of
(M(T), W(T)) under fiD, which is


7.2 Maximum of Brownian Motion with Drift 297


   - _



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-316-0.png)


















298 7 Exotic Options



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-317-0.png)
7.3 Knock-out Barrier Options 299



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-318-0.png)















we obtain (7.2.7).
0





7.3 Knock-out Barrier Options


There are several types of barrier options. Some "knock out" when the un­
derlying a et price crosses a barrier (i.e., they become worthless . If the un­
)
derlying a et price begins below the barrier and must cross above it to cause
the knock-out, the option is said to be up-and-out. A down-and-out option
has the barrier below the initial a et price and knocks out if the a et price
fa s below the barrier. Other options "knock in" at a barrier (i.e., they pay off
zero unless they cross a barrier . Knock-in options also fall into two cla es,
)
up-and-in and down-and-in. The payoff at expiration for barrier options is
typically either that of a put or a call. More complex barrier options require
the a et price to not only cross a barrier but spend a certain amount of time
across the barrier in order to knock in or knock out.
In this section, we treat an up-and-out call on a geometric Brownian mo­
tion. The methodology we develop works equally well for up-and-in, down­
and-out, and down-and-in puts and calls.


300 7 Exotic Options


7.3.1 Up-and-Out Call

Our underlying risky a et is geometric Brownian motion


K



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-319-0.png)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-319-1.png)



option pays off





(7.3.2)


(7.3.3}



where







7.3.2 Black-Scholes-Merton Equation

The price of an up-and-out call satisfies a Black-Scholes-Merton equation that
has been modified to account for the barrier. This equation can be used to
solve for the price. In this particular case, we do not need to find the price this
way because it can be computed analytically (see Subsection 7.3.3}. However,
we provide the equation and its derivation because this methodology works
in situations where analytical solutions cannot be obtained.


7.3 Knock-out Barrier Options 301


Theorem 7.3.1. Let v(t, x) denote the price at time t of the up-and-out call
under the assumption that the call has not knocked out prior to time t and
S(t) = x. Then v(t, x) satisfies the Black-Scholes-Merton partial differential
equation
1 2 2
Vt(t, x ) + rxvx(t, x) + 20" x Vxx(t, x) = rv(t, x) (7.3.4)
in the rectangle { ( t, x); 0 ::; t < T, 0 ::; x ::; B} and satisfies the boundary
conditions



v(t, 0) = 0, 0 ::; t ::; T,
v( t, B) = 0, 0 ::; t < T,
v(T, x) = (x - K) [+], 0 ::; x ::; B.



(7.3.5)
(7.3.6)
(7.3.7)



The lower boundary condition (7.3.5) follows as in the usual Black-Scholes­
Merton framework: If the a et price begins at zero, it stays there and the
option expires out of the money. The upper boundary condition follows from
the fact that when the geometric Brownian S(t) hits the level B, it immedi­
ately rises above B. In fact, because it has nonzero quadratic variation, the
a et price S(t) oscillates, rising and falling across the level B infinitely many
times immediately after hitting it. The option price is zero when the a et
price hits B because the option is on the verge of knocking out. The only
exception to this is if the level B is first reached at the expiration time T,
for then there is no time left for the knock-out. In this case, the option price
is given by the terminal condition (7.3.7). In particular, the function v(t, x)
is not continuous at the corner of its domain where t = T and x = B. It is
continuous everywhere else in the rectangle {(t, x); O ::; t ::; T, O ::; x ::; B}.
Exercise 7.8 outlines the steps to verify the Black-Scholes-Merton equation
by direct computation, starting with the analytical formula (7.3.20) obtained
in Subsection 7.3.3. Here we derive this partial differential equation (7.3.4) by
the simpler but more generally applicable argument used previously: (1) find
the martingale, (2) take the differential, and (3) set the dt term equal to zero.
Let us begin with an initial a et price S(O) E (0, B). We then define
the option payoff V(T) by (7.3.2). The price of the option at time t between
initiation and expiration is given by the risk-neutral pricing formula



V(t) = E [ e [-] r [(] T [-t)] V(T) F(t)], [0 ::; t ::; T. ] (7.3.8)
I



The usual iterated conditioning argument (e.g., (5.3.3)) shows that



(7.3.9)

is a martingale. We would like to use the Markov property as we did in Exam­
ple 6.4.4 to say that V(t) = v(t, S(t)), where v(t, x) is the function in Theorem
7.3.1. However, this equation does not hold for all values of t along all paths.
Recall that v ( t, S( t)) is the value of the option under the a umption that it


302 7 Exotic Options


has not knocked out prior to t, whereas V(t) is the value of the option with­
out any a umption. In particular, if the underlying a et price rises above the
barrier B and then returns below the barrier by time t, then V(t) will be zero
because the option has knocked out, but v t, S(t) will be strictly positive
( )
because v(t, x) given by (7.3.20) is strictly positive for all values of 0 : t < T
and 0 < x < B. The process V ( t) is path-dependent and remembers that the
option has knocked out. The process v(t, S(t)) is not path-dependent, and
when S(t) < B, it gives the price of the option under the a umption that it
has not knocked out, even if that assumption is incorrect.
We resolve this annoyance by defining p to be the first time t at which
the a et price reaches the barrier B. In other words, p is chosen in a path­
dependent way so that S ( t) < B for 0 : t � p and S (p) = B. Since the a et
price almost surely exceeds the barrier immediately after reaching it, we may
regard p as the time of knock-out. If the a et price does not reach the barrier
before expiration, we set p = oo. If the a et price first reaches the barrier at
time T, then p = T but knock-out does not occur because there is no time
left for the a et price to exceed the barrier. However, the probability that
the a et price first reaches the barrier at time T is zero, so this anomaly does
not matter.
The random variable p is a stopping time because it chooses its value based
on the path of the a et price up to time p. Stopping times in the binomial
model were defined in Definition 4.3.1 of Volume I. The Optional Sampling
Theorem, Theorem 4.3.2 of Volume I, a erts that a martingale stopped at a
stopping time is still a martingale. The same is true in continuous time. In
particular, the process


e 1\ p (7.3.10)
e-rpV(p) if p t : T,
<

is a [JP] -martingale. Before t gets to p, this is just the martingale e [-rt] v(t).
Once t gets to p, although the time parameter t can march on, the value of
the process is frozen at e [-r] PV(p). A process that does not move is trivially
a martingale. The only way the martingale property could be ruined would
be if p "looked ahead" when deciding to stop the process. If p stopped at a
time because the process was about to go up and let the process continue if it
was about to go down, the stopped process would have a downward tendency.
So long as p makes the decision to stop at the current time based only on
the path up to and perhaps including the current time, the act of stopping a
martingale at time p preserves the martingale property.

Lemma 7.3.2. We have

V(t) = v t, S(t), 0 : t : p [. ] (7.3.11)
( )

In particular, e [-rt] v t, S t is a IP'-martingale up to time p, or, put another
( ( ))
way, the stopped process

e-rtv(t) if 0 : t : p,
-r(t/\p)V(t ) =
###### {


7.3 Knock-out Barrier Options 303

e [-] r(tA [p)] v(t 1\ p, S(t 1\ p)), 0 � t � T, (7.3.12)

is a martingale under iP.

SKETCH OF PR F:
Because v(t, S(t)) is the value of the up-and-out call
under the a umption that it has not knocked out before time t, and for
t � p this a umption is correct, we have (7.3.11) for t � p. From (7.3.11), we
conclude that the process in (7.3.12) is the i-martingale (7.3.10). D



PROOF OF THEOREM
7.3.1: We compute the differential



d( e [-] rtv(t, S(t))) = e [-] rt rv(t, S(t)) dt + Vt (t, S(t)) dt + Vx (t, S(t)) dS(t)
###### [


+�vxx(t, S(t)) dS(t) dS(t)
]



= e-rt - rv(t, S(t)) + vt(t, S(t)) + rS(t)vx(t, S(t))
###### [



+�u [2] S [2] (t)vxx(t, S(t)) dt
]





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-322-0.png)

obtain


At least theoretically, if an agent begins with a short position in the up-and-out
call and with initial capital X(O) = v(O, S(O)), then the usual delta-hedging
formula
L\(t) = vx(t, S(t)) (7.3.15)
will cause her portfolio value X(t) to track the option value v(t, S(t)) up to
the time p of knock-out or up to expiration T, whichever comes first.
In practice, the delta hedge is impossible to implement if the option has
not knocked out and the underlying a et price approaches the barrier near


304 7 Exotic Options

expiration of the option. The function v(T,x) is discontinuous at x = B,
jumping from B - [K ] to 0 at that point. For t near T and x just below
B, the function v( t, x) is approaching a discontinuity and has large negative
delta vx(t, x) and large negative gamma Vxx (t, x) values. Near expiration near
the barrier, the delta-hedging formula (7.3.15) requires the agent to take a
large short position in the underlying a et and to make large adjustments
in the position (because of the large negative gamma) whenever the a et
price moves. The Black-Scholes-Merton model a umes the bid-ask spread is
zero, and here that a umption is a poor model of reality. The delta-hedging
formula calls for such a large amount of trading that the bid-ask spread
becomes significant. The common industry practice is to price and hedge the
up-and-out call as if the barrier were at a level slightly higher than B. In this
way, the large delta and gamma values of the option occur in the region above
the contractual barrier B, and the hedging position will be closed out upon
knock-out at the contractual barrier before the a et price reaches this region.
0


7.3.3 Computation of the Price of the Up-and-Out Call


The risk-neutral price at time zero of the up-and-out call with payoff V(T)
given by (7.3.2) is V(O) = E[ [e-rT] V(T)] . We use the density formula (7.2.3)
to compute this. If k - 0, we must integrate over the region {(m, w); k w - m - b}. On the other hand, if k < 0, we integrate over the region
{(m, w); k � w � m, 0 � m � b}. In both cases, the region can be described
as {(m,w); k � w � b, w [+ ] - m � b}; see Figure 7.3.1. We a ume here that
S(O) � B so that b - 0. Otherwise, the region over which we integrate has
zero area, and the time-zero value of the call is zero rather than the integral
computed below. We also a ume S(O) > 0 so that b and k are finite.
When 0 < S(O) � B, the time-zero value of the up-and-out call is





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-323-0.png)

dw











where


7.3 Knock-out Barrier Options 305



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-324-0.png)









=                           continue, writing


306 7 Exotic Options



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-325-0.png)















Set


7.3 Knock-out Barrier Options 307



Therefore,





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-326-0.png)









t T, . .

Formula 7.3.2 was derived under the a umption that T > (i.e., t < T)
and < x :( B. 0) For : t T and x - B, we have v(t, x) 0 = because
###### the option knocks out when the a0 0 : et price exceeds the barrier B. 0 Indeed, if
the a et price reaches the barrier before expiration, then it will immediately
exceed the barrier almost surely, and so v(t, B) = for t < T. However,
###### v(T, B) = B-K. We also have v(t, = because geometric Brownian motion 0 0: starting at stays at zero, and hence the call expires out of the money. Finally, 0) 0
if the option does not knock out prior to expiration, then its payoff is that 0
of a European call (i.e., v(T, x) = (x - In summary, v(t, x) satisfies
###### K)+).


308 7 Exotic Options


the boundary conditions (7.3.5)-(7.3.7). Formula (7.3.6) can be obtained by
substitution of x = B in (7.3.20), but for x - B, the right-hand side of
(7.3.20) is not (t, x) = 0. Formula (7.3.20) was derived under the a umption
v
0 < x � B, and it is incorrect if x > B. Formulas (7.3.5) and (7.3.7) cannot
be obtained by substitution of x = 0 and t = T (r = 0) into (7.3.20) because
this leads to zeroes in denominators, but it can be shown that (7.3.20) gives
these formulas as limits as x -I- 0 and T -I- 0; see Exercise 7.2.


7.4 Look back Options


An option whose payoff is based on the maximum that the underlying a et
price attains over some interval of time prior to expiration is called a lookback
option. In this section we price a floating strike lookback option. The payoff
of this option is the difference betw n the maximum a et price over the
time betw n initiation and expiration and the a et price at expiration. The
discussion of this option introduces a new type of differential, a differential
that is neither dt nor dW(t) .


7.4.1 Floating Strike Lookback Option


We begin with a geometric Brownian motion a et price, which may be written
as in (7.3.1) as
S(t) = S(O)eu [W(t)], (7.4.1)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-327-0.png)

With
M(t) = max W(u), 0 � t � T,
O�u::;t
we may write the maximum of the a et price up to time t as

Y(t) = max S(u) = S(O)eu [M(t)] .
O�u::;t

The lookback option considered in this section pays off

V(T) = Y(T) - S(T)



(7.4.2)


(7.4.3)


(7.4.4)



at expiration time T. This payoff is nonnegative because Y(T) � S(T).
Let t E [0, T] be given. At time t, the risk-neutral price of the lookback
option is
V(t) = IE e [-] r [(T] -t [) ] Y(T) - S(T)) F( [t)]

[ ( ] [. ]
I
(7.4.5)


7.4 Lookback Options 309

Because the pair of processes (S(t), Y(t)) has the Markov property [(] see Ex­
ercise 7.3), there must exist a function v(t, x, y) such that

V(t) = v(t, S(t), Y(t)).

In Subsection 7.4.2, we characterize this function by the Black-Scholes-Merton
equation. In Subsection 7.4.3, we compute it explicitly.


7.4.2 Black-Scholes-Merton Equation


Theorem 7.4.1. Let v(t, x, y) denote the price at time t of the floating strike
lookback option under the assumption that S(t) = x and Y(t) = y. Then
v(t, x, y) satisfies the Black-Scholes-Merton partial differential equation

Vt(t, x, y ) + rxvx(t, x, y ) + 20" 1 2 2 X Vxx(t, x, y) = rv(t, x, y) (7.4.6)

in the region {(t, x, y); 0 - t < T, 0 - x - y} and satisfies the boundary
conditions



v(t, 0, y) = e [-] r [(T-t)] y, 0 � t � T, y 0,
:2:
Vy(t, y, y) = 0, 0 � t � T, y > 0,
v(T, x, y) = y - x, 0 � x � y.



(7.4. 7)
(7.4.8)
(7.4.9)



Iterated conditioning implies that e [-] rtv(t) = e-rtv (t, S(t), Y(t)), where
V(t) is given by (7.4.5), is a martingale under P. We compute its differential
and set the dt term equal to zero to obtain (7.4.6). However, when we do this,
the term dY(t) appears. This is different from the term dS(t), because S(t)
has nonzero quadratic variation, whereas Y(t) has zero quadratic variation.
This is because Y(t) is continuous and nondecreasing in t. Let 0 = to < t1 <


 - · ·
< tm = T be a partition of [0, 11· Then
m
L (Y(tj) - Y(tj-1)) [2 ]
j=l
m

      - . max (Y(ti) - Y(ti_t)) L (Y(tj) - Y(ti-d)
J [=l, ...,m ] . ]=l
(7.4.10)
J [=l,. ..,m ]

and maxi=l, ...,m (Y(tj) - Y(ti-d) has limit zero as maxi=l, ...,m(ti - ti-d
goes to zero because Y(t) is continuous. We conclude that Y(t) accumulates
zero quadratic variation on [0, T], a fact we record by writing
dY(t) dY(t) = 0. (7.4.11)

= . max (Y(ti) - Y(ti_t)) · (Y(T) - Y(O)),


310 7 Exotic Options

This argument works because Y(tJ) - Y(tJ -l ) is nonnegative, and hence we
do not need to take the absolute value of these terms in (7.4.10). This ar­
gument shows that on any interval in which a function is continuous and
nondecreasing, it will accumulate zero quadratic variation.
On the other hand, dY(t) is not a dt term: there is no process 8(t) such
that dY(t) = 8(t) dt. In other words, we cannot write Y(t) as

Y(t) = Y(O) + 1 [t ] 8(u) du. (7.4.12)

If we could, then 8(u) would be zero whenever u is in a "flat spot" of Y(t),
which occurs whenever S(t) drops below its maximum to date (see Figure
7.4.1). Figure 7.4.1 suggests that there are time intervals in which Y(t) is
strictly increasing, but in fact no such interval exists. Such an interval can
occur only if S ( t) is strictly increasing on the interval, and if there were such an
interval, then S(t) would accumulate zero quadratic variation on the interval
(see the argument in the previous paragraph). This is not the case because
dS(t) dS(t) = aS [2] (t) dt is positive for all t. Thus, despite the suggestion of
Figure 7.4.1, the lengths of the "flat spots" of Y(t) on any time interval [0, T)
sum to T. Therefore, if (7.4.12) were to hold, we would need to have 8(u) = 0
for Lebesgue almost every u in [0, T). This would result in Y(t) = Y(O) for
0 ::; t ::; T. But in fact Y(t) - Y(O) for all t - 0. We conclude that Y(t)
cannot be represented in the form (7.4.12); dY(t) is not a dt term.
The paths of Y(t) increase over time, but they do so on a set of times
having zero Lebesgue measure. Each time interval [0, T) contains a sequence
of subintervals whose lengths sum to T, and on each of these subintervals, Y(t)
is constant. The particular subintervals depend on the path, but regardless
of the path, the lengths of these subintervals sum to T. A similar situation
is described in Appendix A, Section A.3. In the case discussed there, T = 1
and the subintervals are explicitly exhibited. Their union is the Cantor set.
It is verified that although the lengths of these subintervals sum to 1, there
are uncountably many points not contained in these intervals. The function
F(x) described in Section A.3 increases, but only on the complement of the
Cantor set. Furthermore, F(x) is continuous. Functions of this kind are said
to be singularly continuous.
Fortunately, we can work with the differential of Y(t). We have already
argued that dY(t) dY(t) = 0. Similarly, we have

dY(t) dS(t) = 0 (7.4.13)

(see Exercise 7.4). We now provide the proof of Theorem 7.4.1.


PROOF OF THEOREM
7.4. 1: We use the lt6-Doeblin formula and (7.4.11) and
(7.4.13) to differentiate the martingale e [-][r] t v (t, S(t), Y(t)) to obtain


![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-330-0.png)



7.4 Lookback Options 311


Y(t)




+e [-rt] vy(t, S(t), Y(t)) dY(t). (7.4.14)

order to have a martingale, the dt term must be zero, and this gives us
In
the Black-Scholes-Merton equation (7.4.6) . The new feature is that the term


312 7 Exotic Options

e-rtvy(t, S(t), Y(t)) dY(t) must also be zero. It cannot be canceled by the dt
term nor by the dW(t) term because it is fundamentally different from both
of these terms. The dY(t) term is naturally zero on the "flat spots" of Y(t)
(i.e., when S(t) < Y(t)). However, at the times when Y(t) increases, which
are the times when S(t) = Y(t), the term e-rtvy ( t, S(t), Y(t)} must be zero
because dY(t) is "positive." This gives us the boundary condition (7.4.8).
The boundary condition (7.4.9) is the payoff of the option. If at any time
t we have S(t) = 0, then we will have S(T) = 0. FUrthermore, Y will be
constant on [t, T]; if Y(t) = y, then Y(T) = y and the price of the option at
time t is this value discounted from T back to t. This gives us the boundary
condition (7.4.7). 0
Remark 1.4.2. The proof of Theorem 7.4.1 shows that


formula



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-331-0.png)



(7.4.17)


###### (


###### (


7.4 Lookback Options 313


Substitution into the Black-Scholes-Merton equation (7.4.6) yields



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-332-0.png)

0 = -rv(t, x, y) + Vt (t, x, y) + rxvx(t, x, y) + 1 2 2 Vxx(t, x, y)
20' X



= y ru t, + Ut t, + r Uz t,
###### [- �) �) (�) �) ( ( (


###### . +�a [2 ] (�r Uzz (t,�) ] ·



Canceling y and making the change of variable z =, we see that u(t, z)
:
satisfies the Black-Scholes-Merton equation

Ut(t, z) + rzuz(t, z) + 1 2 2 z Uzz(t, z) = ru(t, z), 0 ::; t < T, 0 < z < 1.
20'
(7.4.18)
Boundary conditions for u(t, z) can be obtained from the boundary conditions
(7.4.7)-(7.4.9) for v(t, x, y). In particular,

e-r(T-t)y = v(t, 0, y) = yu (t, 0)



implies


Furthermore,


implies


Finally,



u(t, 0) = e [-] r [(T-t)], 0 ::; t ::; T.

0 = vy (t, y, y) = u(t, 1) - Uz(t, 1)

u(t, 1) = Uz (t, 1), 0 ::; t < T.


y - x [= ] v(T, x, y) [= ] yu r,
###### �) (



(7.4.19)


(7.4.20)



implies



u(T, z) = 1 - z, 0 ::; z ::; 1.



u(T, z) = 1 - z, 0 ::; z ::; 1. (7.4.21)

Equation (7.4.18) and the boundary conditions (7.4.19)-(7.4.21) uniquely de­
termine the function u(t, z). As a consequence, we see that the Black-Scholes­
Merton equation and boundary conditions in Theorem 7.4.1 uniquely deter­
mine the function v (t, x, y).


314 7 Exotic Options


7 .4 .4 Computation of the Price of the Look back Option


In this subsection, we compute the function v(t, x, y) of Theorem 7.4.1. We
do this for 0 � t < T and 0 < x - y. Because Y(t) S(t) for all t, we do
2:
not need to compute values of v(t, x, y) for x - y. The reader is invited in
Exercise 7.5 to compute the partial derivatives of v(t, x, y) and verify that the
Black-Scholes-Merton equation and boundary conditions in Theorem 7.4.1 are
satisfied.
For 0 � t < T and r = T - t, we observe that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-333-0.png)
















7.4 Lookback Options 315



Because Y(t) and S(t) are .F(t)-measurable and maxt�u�T u ( [W] (u) - [W] (t))
is independent of F(t), we can use the Independence Lemma, Lemma 2.3.4,
to write the conditional expectation in (7.4.24) as g(S(t), Y(t)), where



+
g(x, y) = [E] exp max u ( [W] (u) - [W] (t)) - log [�] . (7.4.25)

[t�u�T ]
### { X }



Note that the expectation in (7.4.25) is no longer conditioned on F(t). Putting
this all together, we have

V(t) = e [-] r'"Y(t)g(S(t), Y(t))          - S(t)

or, equivalently,
v(t, x, y) = [e-] r [ry] g(x, y) - x. (7.4.26)
It remains to compute the function g(x, y). Because


t�u�T t�u�T

and maxt�u�T( [W] (u) - [W] (t)) has the same unconditional distribution under
as maxo�u�,- ( [W] (u)  - [W] (O)) = M(T), the function g(x, y) of (7.4.25) can
also be written as J

max u(W(u)      - W(t)) = u max (W(u)      - W(t)),



g(x, y) = IEexp [uM(T) - log
{
###### �r}



=



(7.4.27)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-334-0.png)



are


316 7 Exotic Options



where O±(T, s) is defined by (7.3.18). The term e [2] "' [m ] appearing on the right­
hand side of (7.2.6) becomes

2a



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-335-0.png)






[



(7.4.29)
= 








log becomes

- 



7.4 Lookback Options 317



With this change of variable in the integral on the right-hand side of (7.4.30),
we obtain the following formula for the first term on the right-hand side of
(7.4.29):



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-336-0.png)













(7.4.32)



Fig. 7.4.2. Reversal of integration in (7.4.32).


318 7 Exotic Options



2 U 2 -ar
1 [-e,;:F-ocr ] log 11. e 1" !L [� ] 2 d m = [-] 2r e " 2 1m=.l.log 11. [m=-f!]

_ �
1.!:m.



2 U 2

e 1" !L [� ] 2 d m = [-] 2r e " 2 1
_ �
1.!:m.



a log 11. z 2r m=.l.log 11. a z
.l.



But



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-337-0.png)



and



and










7.4 Lookback Options 319



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-338-0.png)


























320 7 Exotic Options



Making the change of variable z we obtain
= �,


###### (



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-339-0.png)



(7.4.36)



7.5 Asian Options



An Asian option is one whose payoff includes a time average of the underlying
a et price. The average may be over the entire time period between initiation
and expiration or may be over some period of time that begins later than the
initiation of the option and ends with the option's expiration. The average
may be from continuous sampling,





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-339-1.png)



where 0 < lt < t2 · · · < tm = T. The primary reason to base an option payoff
on an average a et price is to make it more difficult for anyone to significantly
affect the payoff by manipulation of the underlying a et price.
The price of Asian options is not known in closed form. Therefore, in this
section we discuss two ways to derive partial differential equations for Asian
option prices. The first of these was briefly presented in Example 6.6.1. The
other method for computing Asian option prices is Monte Carlo simulation.


7.5.1 Fixed-Strike Asian Call


Once again, we begin with a geometric Brownian motion S(t) given by


dS(t) rS(t) dt + aS(t) dW(t), (7.5.1)
=

- [here W(t), ][0 ][� ][t ][� T, is a Brownian motion under the risk-neutral measure ]
IP'. Consider a fixed-strike Asian call whose payoff at time T is


                V(T) S(t) dt - K (7.5.2)
###### ( [

           ### f


7.5 Asian Options 321



where the strike price K is a nonnegative constant. The price at times t prior
to the expiration time T of this call is given by the risk-neutral pricing formula



V(t) E [ e- [r(T] - [t)] V(T) F(t), 0 � t � T. (7.5.3)
=
I ]



The usual iterated conditioning argument shows that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-340-0.png)

( )

process





This implies that there must exist some function v( t, x, y) such that the Asian
call price (7.5.3) is given as



v(t, S(t), Y(t)) [= ] iE e-r [(T] - [t) ] Y(T) - K F(t)
###### [ ( ) [+]

         ### = iE I ]



(7.5. 7)
= iE e-r(T-t)V(T) F(t) .

[ I )



The function v(t, x, y) satisfies a partial differential equation. This equation
and three boundary conditions are provided in the next theorem. However,


322 7 Exotic Options


in order to numerically solve this equation, it would normally be necessary
to also specify the behavior of v(t, x,y) as x approaches oo and y approaches
either oo or -oo. This can be avoided by the method discussed in Subsection
7.5.3; see Remark 7.5.4 below.

Theorem 7.5.1. The Asian call price function v(t, x, y) of (7.5.7} satisfies
the partial differential equation
1 2 2
Vt(t, x, y) + rxvx(t, x, y) + xvy(t, x, y) + x Vxx(t, x, y) = rv(t, x, y),
0 � t < T, x � 0, y 20" E (7.5.8)
:R.,
and the boundary conditions


v(t, O, y) = e [-r(] T [-t]          -          - K, O �t < T, y E R, (7.5.9)
(� ) [+ ]
lim v(t, x, y) = 0, 0 � t < T, x � 0, (7.5.10)
y.j.-oo
v(T, x,y) = (�       - K) [+ ], x � 0, y E R. (7.5.11)

PROOF: Using the stochastic differential equations (7.5.1) and (7.5.5) and
noting that dS(t) dY(t) = dY(t) dY(t) = 0, we take the differential of the
P-martingale e-rtv(t) = e-rtv(t, S(t), Y(t) ). This differential is



d (e-rtv(t, S(t), Y(t)))



= e [-rt ] [ -rvdt + vt dt + vx dS + Vy dY + �Vxx dS dS
###### ]



= e-r [t ] [ -rv + Vt + rSvx + Svy + �a [2] S [2] vxx dt
###### ]



+e- [rt] aSvx dW(t). (7.5.12)



In order for this to be a martingale, the dt term must be zero, which implies

vt (t, S(t), Y(t)) + rS(t)vx(t, S(t), Y(t)) + S(t)vy (t, S(t), Y(t))
1
+2a [2] S [2] (t)vxx(t, S(t), Y(t)) = rv(t, S(t), Y(t)).

Replacing S(t) by the dummy variable x and Y(t) by the dummy variable y,
we obtain (7.5.8).
We note that S(t) must always be nonnegative, and so (7.5.8) holds for
x � 0. If S(t) 0 and Y(t) y for some value of t, then S(u) 0 for all
= = =
u E [t, T), and so Y(u) is constant on [t, T). Therefore, Y(T) y, and the
=

              value of the Asian call at time t is ( K) [+], discounted from T back to t.
lf
This gives us the boundary condition (7.5.9).

=
In contrast, it is not the case that if Y(t) 0 for some time t, then
Y(u) = 0 for all u � 0. Therefore, we cannot easily determine the value of


7.5 Asian Options 323


v(t, x, 0), and we do not provide a condition on the boundary y = 0. Indeed,
at least mathematically there is no problem with allowing y to be negative. If
at time t we set Y(t) = y, then Y(T) is defined by (7.5.5). In integrated form,
this formula is
Y(T) [= ] y [+] S(u) du. (7.5.13)
i [T ]

Even if y is negative, this makes sense, and in this case we could still have
Y(T) > 0 or even �Y(T)-K > 0, so that the call expires in the money. When
using the differential equations (7.5.1) and (7.5.5) to describe the "state"
processes S(t) and Y(t), there is no reason to require that Y(t) be nonnegative.

=
(We still require that S(t) be nonnegative because x 0 is a natural boundary
for S(t).) For this reason, we do not restrict the values of y in the partial
differential equation (7.5.8). The natural boundary for y is y = -oo. If Y(t) =
y, S(t) = x, and holding x fixed we let y - -oo, then Y(T) approaches -oo
(see (7.5.13)), the probability that the call expires in the money approaches
zero, and the option price approaches zero. The natural boundary for y is
y = -oo, and the boundary condition there is (7.5.10).
The boundary condition (7.5.11) is just the payoff of the call. 0
Remark 7.5.2. After we set the dt term in (7.5.12) equal to zero, we see that

d (e [-] r [t] v(t, S(t), Y(t))) = e [-] r [t] aS(t)vx(t, S(t), Y(t)) dW(t). (7.5.14)

The discounted value of a portfolio that at each time t holds Ll(t) shares of
the underlying a et is given by (see (5.2.27))

(7.5.15)


In



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-342-0.png)





(7.5.16)


324 7 Exotic Options


where c is a constant satisfying 0 < c : T and K is a nonnegative constant.
If c = T, this is the Asian call (7.5.2) considered in Subsection 7.5.2. Here
we also admit the possibility that the averaging is over less than the full time
between initiation and expiration of the call.
To price this call, we create a portfolio process whose value at time T is
1

              X(T) = S(u) du - K.
C 1 [T ]
T-c
We begin with a nonrandom function of time -y(t), 0 : t : T, which will be
the number of shares of the risky a et held by our portfolio. There will be no
Brownian motion term in -y(t), and because of this it will satisfy d-y(t) d-y(t) =
d-y(t) dS(t) = 0. This implies that
d('Y(t)S(t)) = -y(t) dS(t) + S(t) d-y(t), (7.5.17)

which further implies



d(er(T-t)-y(t)S(t)) = er(T-t)d(-y(t)S(t)) - rer(T-t)-y(t)S(t) dt



= er(T-t)-y(t) dS(t) + er(T-t) S(t) d-y(t)



-rer [(T-t)] -y(t)S(t) dt. (7.5.18)



Rearranging terms in (7.5.18), we obtain

er [(T-t)] -y(t)(dS(t) - rS(t) dt) = d(er [(T-t)] -y(t)S(t)) - e [r(T-t)] S(t) d-y(t).
(7.5.19)
An agent who holds -y(t) shares of the risky a et at each time t and finances
this by investing or borrowing at the interest rate r will have a portfolio whose
value evolves according to the equation



dX(t) = -y(t) dS(t) + r(X(t) - -y(t)S(t) )dt
= r X(t) dt + -y(t) (dS(t) - rS(t) dt).

Using this equation and (7.5.19), we obtain



7.5.20
( )



d(er [(T-t) ] X(t)} = -rer [(T-t) ] X(t) dt + er [(T-t) ] dX(t)



= er(T-t)-y(t)(S(t) - rS(t) dt)



7.5.21
= d( er(T-t)-y(t)S(t)} - er(T-t) S(t) d-y(t). ( )



To study the Asian call with payoff (7.5.16), we take -y(t) to be

      - 1 - e [-], 0 : t : T - c,
-y(t) = rc
rc
and we take the initial capital to be
1 ( rc}
## {
1 - e-r(T-t)), T - c : t : T,
_!_ (



7.5.22
( )


7.5 Asian Options 325

X(O) = [_.!:._ ] (1 - e-r [e] )S(O) - e-rT K. (7.5.23)
rc



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-344-0.png)



(7.5.24)


(7.5.25)





















7.5.27
( )









7.5.29
( )


326 7 Exotic Options


The calculation of the right-hand side of (7.5.29) uses a change-of-numeraire
argument, which we now exlain. Let us define


Therefore,



d

[ ( e-rt S(t)) [-] 1]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-345-0.png)

=



=



=





dt







= d
dY(t)



=





and then have


7.5 Asian Options 327





other words,
In



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-346-0.png)





(7.5.34)





L





Markov (see Corollary 6.3.2) .
write (7.5.29) as








[+]

iE
### [ ]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-346-1.png)





where E8[· · · I:F(t)) denotes conditional expectation under the probability
measure P8. Because Y is Markov under P8, there must be some function
g(t,y) such that
g(t, Y(t)) = E8 [Y [+] (T)i :F(t)] . (7.5.36)
From (7.5.36), we see that

g(T, Y(T)) = E8 [Y [+] (T)i :F(T)] = y [+] (T). (7.5.37)


328 7 Exotic Options


We note that Y(T) = can take any value since the numerator X(T),
given by (7.5.27), can be either positive or negative, and the denominator
S(T) can be any positive number. Therefore, (7.5.37) leads to the boundary
condition
g(T, y) = y [+], y E JR. (7.5.38)
The usual iterated conditioning argument shows that the right-hand side
of (7.5.36) is a martingale under P8, and so the differential of g(t, Y(t)) should
have only a dW8(t) term. This differential is

dg(t, Y(t)) = gt(t, Y(t)) dt + gy(t, Y(t)) dY(t)
1
+2gyy(t, Y(t)) dY(t) dY(t)

= [Yt(t, Y(t)) + �u [2] ('Y(t) - Y(t)) [2] gyy(t, Y(t))] dt

+u('Y(t) - Y(t))gy(t, Y(t)) d [W] 8(t).

We conclude that g(t, y) satisfies the partial differential equation

gt(t, y) + �u [2] ('Y(t) - y) [2] gyy(t, y) = 0, 0 � t < T, y E JR. (7.5.39)

We summarize this discussion with the following theorem.

Theorem 7.5.3 (Vecef). For 0 - t - T, the price V(t) at time t of the
continuously averaged Asian call with payoff {7.5.16} at time T is



V(t) = S(t) g t, (7.5.40)
###### (



where g(t, y) satisfies {7.5.99} and X(t) is given by (7.5.24} and {7.5.26}. The
boundary conditions for g(t, y) are {7.5.98} and

lim g(t, y) = 0, lim [g(t, y) - y] = 0, 0 � t T. 7.5.41
y--+-oo y--+oo :5 ( )

Remark 7.5.4 (Boundary conditions). Let 0 - t - T be given. The first
boundary condition in (7.5.41) can be derived from the fact that when Y(t)
is very negative, the probability that Y(T) also is negative is near one and
therefore the probability that Y [+] (T) = 0 is near one. This causes g(t, Y(t))
in (7.5.36) to be near zero. The second boundary condition in (7.5.41) is a
consequence of that fact that when Y(t) is large, then the probability that
Y(T) > 0 is near one. Therefore, g(t, Y(t)) given by (7.5.36) is approximately
equal to fE.8 [Y(T)iF(t)], and because Y(T) is a martingale under J8, this
conditional expectation is Y(t).
It is easier to derive these boundary conditions at y = ±oo for g(t, y) than
it is to derive the boundary conditions for v(t, x, y) in Theorem 7.5.1 because


7.5 Asian Options 329

v(t, x, y) has two variables, x and y, that can become large. For example, it is
not at all clear how v(t, x, y) behaves as x --+ oo and y --+ -oo. The reduction
of the Asian option pricing problem provided by Theorem 7.5.3 reduces the
dimensionality of the problem and simplifies the boundary conditions. It also
removes a so-called "degeneracy" in equation (7.5.8) created by the absence
of the Vyy(t, x, y) term. This degeneracy complicates the numerical solution
of (7.5.8). 0

In the remainder of this subsection, we adapt the arguments just given to
treat a discretely sampled Asian call. = Assume we are given times 0 = t0 <
t1 < t2 · · · < tm T and the Asian call payoff is



=
T and the Asian call payoff is



V(T) S(t;) ### � (! t. K) [+ ]



We wish to create a portfolio process so that



1 [m ]
X(T) =           - L S(ti) - K.
m j=1

In place of (7.5.22), we define

1 [m ]
-y(tj) =           - L e [-] r(T [-] t [;)], j = 0, 1, . . ., m.
m .'=J .



(7.5.42)


(7.5.43
)



Then

1
-y(tj) = -y(tj_1) - -e [-] r(T [-] ti-d, j = 1, . . ., m, 7.5.44
m ( )
and -y(T) = -y(tm) = -;k. We complete the definition of -y(t) by setting

7.5.45
( )

This defines -y(t) for all t E [0, T] . In this situation, (7.5.21) still holds, but
now d-y(t) = 0 in each subinterval (tj_1, tj)· Integrating (7.5.21) from tj_1 to
ti and using (7.5.44) and the fact that -y(t) = -y(tj) for t E (tj_1, tj], we obtain



er(T-t [3] )X(tj)



_

er(T-t [3] )X(tj) er(T-ti-dX(tj-d

= -y(tj) [er(T [-] ti [)] S(tj) - er(T [-] ti-dS(tj_I)]



= -y(tj)er(T-tilS(tj) - -y(tj-d - e-r(T-ti-d er(T-ti-dS(tj-d
###### ( � )



= -y(tj)er(T-tilS(tj) - -y(ti_l)er(T-ti-dS(ti_I) + [__!_] S(ti_I).
m
Summing this equation from j = 1 to j = k, we see that


330 7 Exotic Options



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-349-0.png)

In particular,
1 [m ]
X(T) = X(tm) =         - LS(ti) - [K ]
m i=l
as desired.



(7.5.47)



To determine X(t) for tk :5 t :5 tk+l• we integrate (7.5.21) from tk to t to
obtain
er(T-t)X(t) = er(T-t,.)X(tk) + 'Y(tk+t) [er(T-t)S(t) - er(T-t,.)S(tk)]



= -y(tk)er(T [-] t,. [) ] S(tk) + [..!_] S(ti) - K + -y(tk+l)er [(] T [-t) ] S(t)
m i=l
I:



k
= -y(tk+t)er(T [-] t)S(t) + [..!_ ] L S(ti) - K.
m i=l

  - -y(tk) - e-r(T-t,.) er(T-t,.)S(tk)
###### ( )
      


Therefore,

1 [k ]
m i=l
(7.5.48)
We now proceed with the change of numeraire as before. This leads again
to Theorem 7.5.3 for the discretely sampled Asian call with payoff (7.5.42).
X(t) = -y(tk+t)S(t) + e-r(T-t)- L S(ti) - e-r(T-t) K, tk :5 t :5 tk+l·


7.7 Notes 331

The price at time t is given by (7.5.40), where g(t,x) satisfies (7.5.39) with
boundar [y conditions ] (7.5.38) [and ] (7.5.41). [The only difference is that now ]
the [nonrandom function ][7] (t) [appearing in ] (7.5.39) [is given by ] (7.5.43) [and ]
(7.5.45) and the process X(t) in (7.5.40) is given by (7.5.48).


Summary
7.6

Three specific exotic options on a geometric Brownian motion have been con­
sidered: an up-and-out barrier call, a lookback call, and an Asian call. In
each case, the discounted option price is a martingale under the risk-neutral
measure, and this leads to a partial differential equation of the Black-Scholes­
Merton type. However, the look back call and the Asian call equations have
a itional state variable in this equation.
an
For the barrier call and the lookback call, the option price was computed
explicitly. The Asian option pricing problem was transformed by a change of
numeraire to an equation with a single state variable. This transformation

was done both for the continuously sampled and the discretely sampled Asian
options.


Notes
7.7

There are scores of different exotic options, and the search for explicit pricing
formulas can lead to complex computations. Analysis of many exotic options
provided by Zhang [167] and Haug [80]. Papers by a variety of authors who
is
treat exotic options, including some of those cited below, have been collected
by Lipton [110]. Exotic options are prevalent in foreign exchange markets.
Analysis of several instruments appearing in these markets is provided by
Hakala and Wystup [76]. Many exotic pricing formulas can be derived from
the formulas for distributions related to Brownian motion collected by Borodin
and Salminen [18].
The analysis of barrier options presented here follows Rubinstein and
Reiner [142]. Monte Carlo simulation of barrier options normally obtains the
price for the case when barrier crossing is checked only at discrete times.
Broadie, Gla erman and Kou [22] provide a correction term to adjust this
result to obtain the price for an option in which the barrier is monitored con­
tinuously. The problem of large delta and gamma values for barrier options
near expiration near the barrier can be ameliorated by placing an a priori
constraint on the hedging strategy and pricing this constraint into the option;

s Schmock, Shreve, and Wystup [148].
The change-of-numeraire approach to Asian options, explained in Subsec­
tion 7.5.3, is due to Vecef [155], [156]. This methodology was extended to
jump processes by Vecef and Xl' [157]. Other partial differential equations for


7 Exotic Options


pricing Asian options are provided by Andreasen [4], Lipton [109], and Rogers
and Shi [139] .
Geman and Yor [71] obtain a closed-form formula for a Laplace transform
of the Asian option price. Fu, Madan, and Wang [67] compare Monte Carlo
and Laplace transform methods for Asian option pricing.


7.8 Exercises


Exercise (Black-Scholes-Merton equation for the up-and-out call).
7.1
This exercise shows by direct calculation that the function x) of (7.3.20)
v(t,
satisfies the Black-Scholes-Merton equation 7.3.4 .
( )

332



7.8. 1
( )



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-351-0.png)







(7.8.2)


(7.8.3)


(7.8.4)


(7.8.5)


(7.8.6)




7.8 Exercises 333



(v i) Use (i) to compute and (7.8.3)-(7.8.5) to simplify it, obtaining
Vt(t, x)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-352-0.png)













(xi) Now verify that v(t, x) satisfies the Black-Scholes-Merton equation (7.3.4).


334 7 Exotic Options



Exercise 7.2 (Boundary conditions for the up-and-out call). In this
exercise, it is verified that the up-and-out call price v(t, x) given by (7.3.20)
satisfies the boundary condition (7.3.6). Furthermore, the limit as x 0 sat­
.j.
isfies (7.3.5) and the limit as t T satisfies (7.3.7).
t
(i) Verify by direct substitution into (7.3.20) that (7.3.6) is satisfied.
(ii) Show that, for any positive constant c,



limo± x.j_O (T, �C = -oo, limO± x.j_O (T, !:X = oo. (7.8.11)
) )



Use this to show that for any p E JR. and positive constants c1 and c2, we
have



(7.8.12)


(7.8.13)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-353-0.png)

If p ; 0, (7.8.12) and (7.8.13) are immediate consequences of (7.8.11).
However, if p < 0, one should first use L'Hopital's rule and then show
that



P [exp ] P [exp ]
###### �i [x] { [-] � [o] ! ( [T, ] �)} [= ] o, �i [x] { [-] � [o] ! ( [T, ] } [= ] o.
;)



(7.8.14)
To establish (7.8.14), you may wish to prove and use the inequality



1
2a2-b2 ::; (a+ b)2 for all a, bE JR



(7.8.15)


(7.8.16)



Conclude that limx.J-0 v(t, x) = 0 for 0 $ t < T.
(iii) Show that, for any positive c,
-oo if 0 < c < 1,
limo±(T, c) = 0 if c = 1,
### r [.j_O ] { 00 if C > 1.



Use this to show that limr.J-0 v(t, x) = (x - K) [+ ] for 0 < x < B.



Exercise 7.3 (Markov property for geometric Brownian motion and
its maximum to date). Recall the geometric Brownian motion S(t) of
(7.4.1) and its maximum-to-date process Y(t) of (7.4.3). According to Defini­
tion 2.3.6, in order to show that the pair of processes (S(t), Y(t)) is Markov,
we must show that whenever 0 ::; t ::; T and f(x, y) is a function, there exists
another function g(x, y) such that
lE[f(S(T), Y(T)) IF(t)] g(S(t), Y(t)). (7.8.17)
=

Use the Independence Lemma, Lemma 2.3.4, to show that such a function
g(x, y) exists.


7.8 Exercises 335



Exercise 7.4 (Cross variation of geometric Brownian motion and its
maximum to date). Let S(t) be the geometric Brownian motion (7.4.1)
and let Y(t) be the maximum-to-date process (7.4.3). Let T be fixed and let
0 = to < t1 < . .. tm = T be a partition of [0, T]. Show that as the number of
partition points m approaches infinity and the length of the longest subinterval
ma.xj=1, . .,m ti - tj-1 approaches zero, the sum

m
L (Y(tj) - Y(tj-d)(S(tj) - S(tj-d)
j=1

has limit zero.


Exercise 7.5 (Black-Scholes-Merton equation for lookback option).
We wish to verify by direct computation that the function v(t, x, y) of (7.4.35)
satisfies the Black-Scholes-Merton equation (7.4.6). As we saw in Subsection
7.4.3, this is equivalent to showing that the function u defined by (7.4.36)
satisfies the Black-Scholes-Merton equation (7.4.18). We verify that u(t, z)
satisfies (7.4. 18) in the following steps. Let 0 : t < T be given, and define

T T - t.
=
(i) Use (7.8.1) to compute Ut(t, z), and use (7.8.3) and (7.8.4) to simplify the
result, thereby showing that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-354-0.png)



(7.8.20)
(iv) Verify that u(t, z) satisfies the Black-Scholes-Merton equation (7.4.18).
(v) Verify that u(t, z) satisfies the boundary condition (7.4.20).

Exercise 7.6 (Boundary conditions for lookback option) . The look­
back option price v(t, x, y) of (7.4.35) must satisfy the boundary conditions

2
###### (


336 7 Exotic Options
(7.4.7)-(7.4.9). As we saw in Subsection 7.4.3, this is equivalent to the function
u(t, z) of (7.4.16) given by (7.4.36),
###### (

satisfying the boundary conditions (7.4.19)-(7.4.21). This function was shown
to satisfy boundary condition (7.4.20) in Exercise 7.5(v). Here we verify by
direct computation that the limit of u(t, z) as z .j. 0 satisfies (7.4.19) and the
limit of u(t, z) as t t T (T 0) satisfies (7.4.21).
.j.
(i) If you have not worked Exercise 7.2, then verify (7.8.11), the second equal­
ity in (7.8.14) and (7.8.16).
(ii) Use (7.8.11) and the second part of (7.8.14) to show that limz.(.O u(t, z) =
e-r,- for 0 '5. t < T.
=
(iii) Use (7.8.16) to show that lim,-.J_o u(t, z) 1-z for 0 < z '5. 1.

Exercise 7. 7 (Zero-strike Asian call). Consider a zero-strike Asian ca
whose payoff at time T is


it is not random.
=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-355-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-355-1.png)
7.8 Exercises 337

Exercise 7.8. Consider the continuously sampled Asian option of Subsection
7.5.3, but a ume now that the interest rate is r = 0. Find an initial capital
X(O) and a nonrandom function 7(t) to replace (7.5.22) so that

1
X(T) =          - S(u) du - K (7.5.27)
C 1 [T ]
T- c
still holds. Give the formula for the resulting process X(t), 0 � t � T, tore­
place (7.5.24) and (7.5.26). With this function 7(t) and process X(t), Theorem
7.5.3 still holds.

Exercise 7.9. Let g(t, y) be the function in Theorem 7.5.3. Then the value of
the Asian option at timet is V(t) = v(t, S(t), X(t)), where v(t, s, x) = sg(t, y)

and y = �- The process S(t) is given by (7.5.1). For the sake of specificity,
we consider the case of continuous sampling with r i 0, so 7(t) is given by
(7.5.22) and X(t) is given by (7.5.24) and (7.5.26) .
(i) Verify the derivative formulas

Vt(t, S, x) = S9t(t, y),
V8(t, s, x) = g(t, y) - ygy(t, y),
Vx (t, s, x) = gy(t, y),
y [2 ]
V8s(t, S, x) = -gyy(t, ys ),
y
Vsx (t, S, x) = --gyy(t, y), s
1
Vxx (t, S, x) = -gyy(t, ys ).
(ii) Show that e-rtv(t, S(t), X(t)) is a martingale under JPi by computing its
differential, writing the differential in terms of dt and dW, and verifying
that the dt term is zero. (Hint: Use the fact that g(t, y) satisfies (7.5.39).)
(iii) Suppose we begin with initial capital v(O, S(O), X(O)) and at each time t
take a position Ll(t) in the risky a et, investing or borrowing at the inter­
est rate r in order to finance this. We want to do this so that the portfolio
value at the final time is S(u) du - . Give a formula for Ll(t)

         - f c K) [+]
in terms of the function ( v and the processes S(t) and X(t). (Warning:
The process X(t) appearing in Theorem 7.5.3 and in this problem is not
the value of the hedging portfolio. For example, X(O) is given by (7.5.23),
and this is different from v(O, S(O) X(O)), the initial value of the hedging
portfolio.)
,


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-357-0.png)
8


American Derivative Securities


8. 1 Introduction
European option contracts specify an expiration date, and if the option is
to be exercised at all, the exercise must occur on the expiration date. An
option whose owner can choose to exercise at any time up to and including the
expiration date is called American. Because of this early exercise feature, such
an option is at least as valuable as its European counterpart. Sometimes the
difference in value is negligible or even zero, and then American and European
options are close or exact substitutes. We shall see in this chapter that the
early exercise feature for a call on a stock paying no dividends is worthless;
American and European calls on such a stock have the same price. In other
cases, most notably put options, the value of this early exercise feature, the
so-called early exercise premium, can be substantial. An intermediate option
between American and European is Bermudan, an option that permits early
exercise but only on a contractually specified finite set of dates.
Because an American option can be exercised at any time prior to its ex­
piration, it can never be worth less than the payoff a ociated with immediate
exercise. This is called the intrinsic value of the option.
In contrast to the case for a European option, whose discounted price
process is a martingale under the risk-neutral measure, the discounted price
process of an American option is a supermartingale under this measure. The
holder of this option may fail to exercise at the optimal exercise date, and
in this case the discounted option price has a tendency to fall; hence, the
supermartingale property. During any period of time in which it is not optimal
to exercise, however, the discounted price process behaves as a martingale.
To price an American option, just as with a European option, we could
imagine selling the option in exchange for some initial capital and then con­
sider how to use this capital to hedge the short position in the option. In this
case, we would need to be ready to pay off the option at all times prior to the
expiration date because we do not know when it will be exercised. We could
determine when, from our point of view, is the worst time for the owner to


340 8 American Derivative Securities
exercise the option. From the owner's point of view, this would be the optimal
exercise time, and we shall call it that. We could then compute the initial
capital we need in order to be hedged against exercise at the optimal exercise
time. Finally, we could show how to invest this capital so that we are hedged
even if the owner exercises at a nonoptimal time. In the subsequent sections,
we do all these things but begin the analysis at a different point than for Eu­
ropean options. We define the price of American options using a risk-neutral
pricing formula and then show that this price is the smallest initial capital
that permits construction of the hedge just described.
For the binomial model, the program described above was carried out in
Chapter 4 of Volume I. Here we revisit these matters in a continuous-time
setting. We treat first the perpetual American put (Section 8.3), which is not
actually traded. The analysis of this option provides lessons that we apply
in the subsequent sections. In Section 8.4, we discuss the finite-expiration
American put, an option that is traded. Section 8.5 treats the American call.
In the case of a non-dividend-paying stock, we show that the American and
European calls have the same price. However, if the stock pays dividends,
these prices can differ. We show how to compute the American call price in
this latter case.


8.2 Stopping Times
Throughout this chapter, we need the concept of stopping times. These were
defined and discussed in the binomial model in Section 4.3 of Volume I. A
stopping time is a random variable T that takes values in [0, oo]. The stopping
times we shall encounter are the times at which an American option is exer­
cised. The decision of an agent to exercise this option may depend on all the
information available at that time but may not depend on future information.
We provide a mathematical formulation of this property in Definition 8.2.1
below. Before stating this definition, we seek to motivate it.
In theN-period model of Volume I, where the filtration is generated by coin
tossing and there are only finitely many dates, we defined a stopping time to
be a random variable T taking values 0, 1, ...,Nor oo and having the property
that if T(wl . . . WnWn+l · .. wN) = n, then T(w1 . . . WnW�+l · .. w�) = n for all
w�+l ... w�. This condition guarantees that the decision to stop at time n
does not depend on the coin tosses that come after time n.
One way to try to capture this same idea in continuous time is to require
that for each nonrandom t 0, the set { T = t} = { w E n; T( w) = t} should
;
be in :F(t) (i.e., the agent stops (exercises the option) at time t based on the
information available at time t). However, we shall be interested in sets of ws
of the form {w E n; T1 - T(w) � T2}, and these cannot be gotten by taking
countable unions of sets of the form {w E n; T(w) = t}. Therefore, we impose
the slightly stronger condition of Definition 8.2.1 below.


8.2 Stopping Times 341

Definition 8.2.1. A stopping time T is a mndom variable taking values in

[0, oo] and satisfying
{T : t} E :F(t) for all t 2 0. (8.2.1)

Remark 8.2.2. Let t 2 0 be given. Note that (8.2.1) and the properties of a­
algebras imply that { T > t { T : t }c E :F ( t for all positive

              - �} =              - �              - �)
integers n. Since every set in :F (t - is also in :F(t), we conclude that
�)
T > t - is in :F(t) for every n, and hence
{ �}

{T t} {T :S t} n T > t = = {
### �})
is also in :F(t). In other words, by Definition c�l 8.2.1, a stopping time T has the
property that the decision to stop at time t must be based on information
available at timet.
Example 8.2.3 {First passage time for a continuous process). Let X(t) be an
adapted process with continuous paths, let m be a number, and set
Tm min{t 2 0; X(t) m} . (8.2.2)
= =
This is the first time the process X(t) reaches the level m. If X(t) never
reaches the level m, then we interpret Tm to be oo. Intuitively, Tm must be
a stopping time because the value of Tm is determined by the path of X(t)
up to time T m. An agent can exercise an option the first time the underlying
a et price reaches a level; this exercise strategy does not require information
about the underlying price movements after the exercise time.
We use Definition 8.2.1 and the properties of a-algebras to show mathe­
matically that T m is a stopping time. Let t 2 0 be given. We need to show
that {T : t} is in :F(t).
If t 0, then { T :S t} { T 0} is either fl or 0, depending On whether
= = =
X(O) m or X(O) =f. m. In either case, {T : 0} E :F(O).
=
We consider the case t > 0. Suppose w E n satisfies T(w) : t. Then there
is some numbers : t such that X(s, w) = m, where we indicate explicitly the
dependence of X on w. For each positive integer n, there is an open interval
of time containing s for which the process X is in ( m - �, m + �). In this
interval, there is a rational number q : s : t. Therefore, w is in the set

00 1
A = n O�q9,q u rational m - n < X(q) < m + n .
### } We have shown that n= [l ] { T : t} C A.

On the other hand, if w E A, then for every positive integer n there is a
rational number : t such that
### Qn
1
###### {


342 8 American Derivative Securities
m - -n 1 < X ( Qn, w) < m + -. n 1
The infinite sequence {qn}�=l must have an accumulation point s in the
closed, bounded interval [0, t]. In other words, there must exist a number
s E [0, t] and a subsequence { Qnk }k=l such that limk--+oo Qnk = s. But

1 1
m - -nk < X ( Qnk, w) < m + -nk for all k = 1, 2, . . . .
Letting k -+ oo in these inequalities and using the fact that X has continuous
paths, we see that X s,w = It fo **l** ows that r w - t. We have shown that
( ) m. ( )
A C {r � t}. Therefore A = {r � t}.
Because X is adapted to the filtration, for each positive integer n and
rational q E [0, t], the set
{ m            - < X (q) < [m ] +
is in F(q) and hence in the larger a-algebra � F(t). Because there are only count­�}
ably many rational numbers q in [0, t], they can be arranged in a sequence,
and the union

Bn = U . { [m ] < X ( q) < [m ] +
O:$q:,q rational
### -� �}
is really a union of a sequence of sets in F(t). The set Bn must therefore also
be in F(t). Because Bn is in F(t) for every positive integer n, the intersection
n�=1Bn = A is also in F(t). We have already shown that A = {r � t}. We
conclude that { T � t} E F(t). D
Suppose now that we have an adapted process X(t) and a stopping time
T. We define the stopped process X(t 1\ r), where 1\ denotes the minimum of
two quantities (i.e., t 1\ T = min{t, T} ). The stopped process X(t 1\ r) agrees
with X(t) up to time T, and thereafter it is frozen at the value of X(r). See
Figure 8.2.1.

Theorem 8.2.4 (Optional sampling). A martingale stopped at a stop­
ping time is a martingale. A supermartingale {or submartingale) stopped at a
stopping time is a supermartingale (or submartingale, respectively).
While the proof of Theorem 8.2.4 is technical and will not be given here,
the intuition is clear. If M(t) is a martingale, then the stopped process M(tl\r)
agrees with M(t) before time T and thus is also a martingale. After time T,
the stopped process is frozen (i.e., it no longer changes with time), and this
is a trivial martingale. A martingale goes neither up nor down "on average."
After being frozen, a process goes neither up nor down, path-by-path. The
only way the martingale property could be violated is if the stopping decision


1



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-362-0.png)



8.2 Stopping Times 343



Fig. 8.2.1. A stopped process.

looked ahead. Suppose that a martingale is stopped (frozen) if it will go up
in the near future but is allowed to continue if it will go down. Then stopping
introduces a downward bias by removing the upward possibility. Figure 8.2.2
shows a martingale in a discrete-time model under the a umption that the
probability of H (an up move) is jj - and the probability ofT (a down
=
move) is ij = �- Figures 8.2.2-8.2.4 are taken from Section 4.3 of Volume I,
where the martingale in Figure 8.2.2 is a discounted stock price under a risk­
neutral measure. Figure 8.2.3 shows a random time that is not a stopping
p
time; this random time p causes stopping at time 0 if there is an H on the
first toss (an up move) but lets the process continue if there is a T on the first
toss. Similarly, if there is a T on the first toss and an H on the second toss, p
stops the martingale at time 1 but lets it continue to time 2 if there is a T on
the first toss and an H on the second toss. The stopped martingale is shown
in Figure 8.2.4, and it is not a martingale. For example,

lEM2/\p - = 4 1 ( 4 + 4 + 1.60 + 0.64) = 2.56 < M0 = 4,
whereas the expectation of a martingale does not change over time. Our def­
inition of stopping time rules out this kind of stopping.
Similar intuition applies to supermartingales. A stopped supermartingale
is a supermartingale before being frozen, and after being frozen it is a mar­
tingale, which is a special case of a supermartingale. The situation with sub­
martingales is analogous. Again, the stopping must be done at a stopping time.


344 8 American Derivative Securities



M2(HH) = 10.24
/

M1(H) = 6.40
/
Mo = 4    - M2(HT) = M2(TH) = 2.56

  - = 1.60
M1(T)
/
M2(TT) = 0.64

      

Fig. 8.2.2. Martingale under p = =
ij �

Mo = 4

p(HH) = p(HT) = 0

    - M1(T) = 1.60
p(TH) = 1
M2(TT) = 0.64
p(TT) = 2

    
Fig. 8.2.3. Non-stopping time p.


MoAT = 4


Fig. 8.2.4. Martingale stopped at the non-stopping time p.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-363-0.png)
8.3 Perpetual American Put 345
Looking ahead to make the stopping decision can ruin the supermartingale
(respectively, submartingale) property.


8.3 Perpetual American Put
The simplest interesting American option is the perpetual American put. It is
interesting because the optimal exercise policy is not obvious, and it is simple
because this policy can be determined explicitly. Although this is not a traded
option, we begin our discussion with it in order to present in a simple context
the ideas behind the subsequent analysis of more realistic options.
The underlying a et in most of this chapter (except in Subsection 8.5.2,
where the a et pays dividends) has the price process S(t) given by

dS(t) = rS(t) dt + uS(t) dW(t), (8.3.1)
where the interest rate r and the volatility u are strictly positive constants
and W(t) is a Brownian motion under the risk-neutral probability measure J.
The perpetual American put pays K - S(t) if it is exercised at time t. This
is its intrinsic value.

Definition 8.3.1. Let be the set of all stopping times. The price of the
T
perpetual American put is defined to be

v. x maxlE [ [e-rr] (8.3.2)
( ) = r [ET ] ( [K - S(r)}), ]

where x S(O) in {8.3.2} is the initial stock price. In the event that T oo,
= =
we interpret e-rr(K - S(r)) to be zero.
The idea behind Definition 8.3.1 is that the owner of the perpetual Amer­
ican put can choose an exercise timeT, subject only to the condition that she
may not look ahead to determine when to exercise. The mathematical formu­
lation of this "not look ahead" restriction is that T must be a stopping time.
The price of the option at time zero is the risk-neutral expected payoff of the
option, discounted from the exercise time back to time zero. If the option is
never exercised, its payoff is zero. This explains the term under the expecta­
tion on the right-hand side of (8.3.2). The owner of the option should choose
the exercise strategy that maximizes this expected payoff, discounted back to
time zero, and thus we define the price of the option to be the maximum over
T E of the discounted expected payoffs.
T
This risk-neutral pricing definition of the perpetual American put price
appears to differ from the construction of the price of a European call in
Section 4.5. There we took the price to be the initial capital required by an
agent holding a short position in the option in order for this agent to hedge the
short position (i.e., invest in the stock and money market account in such a
way that at expiration of the option the resulting portfolio value is the payoff


346 8 American Derivative Securities
of the option). It turns out that v*(x) defined above is the initial capital
required for an agent to hedge a short position in the American put regardless
of the exercise strategy T used by the owner of the put; see Corollaries 8.3.6
and 8.3.7.
The owner of the perpetual American put can exercise at any time. In
particular, there is no expiration date after which the put can no longer be
exercised. This makes every date like every other date; the time remaining to
expiration is always the same (i.e., infinity). Because every date is like every
other date, it is reasonable to expect that the optimal exercise policy depends
only on the value of S(t) and not on the time variable t. The owner of the put
should exercise as soon as S(t) falls "far enough" below K. In other words, it
is reasonable to expect that the optimal exercise policy is of the form
"Exercise the put as soon as S(t) falls to the level L*."
We have two questions to answer:
(i) What is the value of L* and how do we know it corresponds to optimal
exercise?
(ii) What is the value of the put?
For the perpetual American put, we can base the answers to these questions
on explicit computations.


8.3.1 Price Under Arbitrary Exercise


(8.3.3)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-365-0.png)







= .
.A


8.3 Perpetual American Put 347
Then


gale



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-366-0.png)





(8.3.4)



and







(8.3.5)





have





(8.3.6)


(8.3.7)

0







=

This is (8.3.3) when we interpret e->, to be zero if Tm oo .
iE



=
oo .


348 8 American Derivative Securities

Remark 8.3.3. We used the strict positivity of A to derive (8.3.7), but now that
we have it, we can take the limit as A .j 0. The random variables e-A [rm ] n{ rm <oo}
are nonnegative and increase to as A 0, and the Monotone Conver­
H{rm<oo} .j
gence Theorem allows us to conclude that

m
e-2The solution to [m] lttl (8.3.1) is



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-367-0.png)
8.3 Perpetual American Put 349



reaches the level L. But S(t) = L if and only if




 - 1 1 1 X
-W(t) - - t = - log -.
###### r--u 2 2 L u u
### ( )



We now apply Theorem 8.3.2 with X(t) in that theorem replaced by -W(t)­

- (r-�u2) t (the processes W(t) and -W(t) are both Brownian motions
under P), with replaced by with replaced by and with
###### A r, J.L -� (r-�u2),



m replaced by - log f, which is positive. With these replacements, T m m
Theorem 8.3.2 is T£ and



= �
###### J.L2 + 2A r2 -ru2 + �u44 + 2r u2
### ( )



4

= �
###### r2 +ru2 + �u44 u2
### ( )
###### [2 ]



Therefore,



= �
###### r+ �u2 u2 2
### ( ) [2 ]



1 1 1 1
=      - = -. 2r
###### -J.L + J.L2 + 2A r--u2 +- r + -u2 u 2 u 2 u
### ( ) ( )



Equation (8.3.3) implies
1 x x                      JE_.,- L = exp -{              - log L · � 2r = (L )              - ·
### }



0



The second line in (8.3.11) follows.



8.3.2 Price Under Optimal Exercise

Figure 8.3.1 shows the function L (x) for three different values of L. The
v
function V£, (x) in that figure actually lies below the intrinsic value K - x for

x
between L1 and L2. If the initial stock price is between L1 and L2, then the
strategy of exercising the first time the stock price falls to L1 is obviously a
poor one; it would be better to exercise at time zero and receive the intrinsic
value. The function V£2 (x) agrees with the intrinsic value for 0 � x � L2 and
follows the indicated curve for x L2. The function L. ( x agrees with the
; v )
intrinsic value for 0 � x - L. and follows the indicated curve for x L
;                        - .
For x L., the function L. ( x is strictly larger than the function L2 ( x,
; v ) v )
and hence the strategy of exercising the first time the stock price falls to L.
is better than exercising the first time the stock price falls to L2.
As Figure 8.3.1 suggests, for any value of L smaller than L., the function
vL (x) agrees with the intrinsic value for 0 � x - L, lies below the intrinsic


350 8 American Derivative Securities





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-369-0.png)








                          
Setting this equal to zero, we solve for


8.3 Perpetual American Put 351



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-370-0.png)



8.3.3







so that





If




   








=

  - l,


352 8 American Derivative Securities



which agrees with the left-hand derivative v�. (L*-) = -1 provided by the
first line in (8.3.14). The derivative of VL. (x) is continuous at x = L*. This is
known as smooth pasting. The two parts of the definition of V£. (x) fit together


0. (8.3.16)


On the other hand, for 0 � x < L*,
1
rvL. (x) - rxv�. (x) - 2a [2] x [2] vZ. (x) = r(K - x) + rx = rK. (8.3.17)

In particular, we see that V£. (x) satisfies the so-called linear complementarity
conditions
v(x) (K - x)+ for all x 0, (8.3.18)
2: 2:
1
rv(x) - rxv'(x) - 2a [2] x [2] v"(x) 2: 0 for all x 2: 0, and (8.3.19)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-371-0.png)

v(x) (K - x)+ for all x 0, (8.3.18)
2: 2:
1
rv(x) - rxv'(x) - 2a [2] x [2] v"(x) 2: 0 for all x 2: 0, and (8.3.19)

for each x 0, equality holds in either (8.3.18) or (8.3.19). (8.3.20)
2:

The point L* is slightly problematical in (8.3.19) since vZ. (L*) is undefined.
However, if we replace vZ. (L*) in (8.3.19) by either vZ. (L*-) or vZ. (L*+),
the inequality holds.
The linear complementarity conditions (8.3.18)-(8.3.20) determine the
function VL.(x). More precisely, the function VL.(x) given by (8.3.13) is the
only bounded continuous function having a continuous derivative that satisfies
these conditions; see Exercise 8.3.



for each x 0, equality holds in either (8.3.18) or (8.3.19).
2:


8.3 Perpetual American Put 353


8.3.4 Probabilistic Characterization of the Put Price

Theorem 8.3.5. Let S(t) be the stock price given by {8.3.1} and let T£. be
given by {8.3.9} with L = L Then e-rtvL. (S(t)) is a supermartingale under

                   - .
P, and the stopped process e-r(t/\n [. ] >vL. (S(t 1\ T£.)) is a martingale.

PROOF: Fortunately, the ltO-Doeblin formula applies to functions whose sec­
ond derivatives have jumps, provided the first derivative is continuous (see
Exercise 4.20 for a discussion related to this). We may thus compute



d[e [-] r [t] VL. (S(t)))



= e [-] r [t ] [ -rvL. (S(t)) dt + vL (S(t)) dS(t) + �v�. (S(t)) [dS(t) dS(t)] ]



= e [-] r [t ] [ -rvL. (S(t)) + rS(t)v�. (S(t)) + �a [2] S [2] (t)v�. ( [S(t))] ] [dt ]



Ito integrals are martingales, and hence the Ito integral above stopped at the
stopping time n. is a martingale. 0

Corollary 8.3.6. Recall that is the set of all stopping times, not just those
T
of the form (8.3.9}. We have


                VL. (x) = max [i ] [e [-r][r] (K S(r))],
r [ET ]
where x = S(O) is the initial stock price. In other words, vL. (x) is the perpetual
American put price of Definition 8.3.1.

PROOF: Because e-rtvL. (S(t)) is a supermartingale under P, we have from
Theorem 8.2.4 (optional sampling) that, for every stopping time T E T,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-372-0.png)
354 8 American Derivative Securities


(8.3.22)

Because VL. S(t 1\ r)) is bounded, we may let t - oo in (8.3.22), using the
(
Dominated Convergence Theorem, Theorem 1.4.9, to conclude that
VL. (x) ;:=: lE [e-rrVL. (S(r)}) ;:=: lE [e [-] rr(K - S(r)}),
where we have gotten the last inequality from (8.3.18). Because this inequality
holds for every T E we have
T,
VL.(x) ;:=: max7 lE [e-rr(K - S(r)}) .
r [E ]
On the other hand, if we replace T by T£., we obtain equality in (8.3.22)
because e-r(tML [.] >v(S(t 1\ TL.)) is a martingale under P. Letting t - oo and
using the Dominated Convergence Theorem, we obtain
VL.(x) = lE [e-rrL [.] VL. (S(TL.))] .
Since
e-rrL [. ] VL. (S(TL.)) = e-rrL [. ] VL. (L.) = e [-] rrL [. ] (K- L.) = [e-] rrL [. ] (K-S(TL.))

if T£. < oo (and is interpreted to be zero if T£. = oo), we see that
VL. (x) = lE [e-rrL [. ] (K - S(rL.))] . (8.3.23)

It follows that
VL.(x) �max iE [e-rr(K - S(r)}) . 0
r [ET ]

Discounted European option prices are martingales under the risk-neutral
probability measure. Discounted American option prices are martingales up
to the time they should be exercised. If they are not exercised when they
should be, they tend downward. Since a martingale is a special case of a
supermartingale, and processes that tend downward are supermartingales,
discounted American option prices are supermartingales. An agent who is
short an American option can hedge that short position in the usual way
during the time the discounted option price is a martingale. If the option
is not exercised when it should be, then the agent can continue the hedge
and take money off the table. The following corollary illustrates this for the
perpetual American put of this section.

Corollary 8.3.7. Consider an agent with initial capital X(O) = VL.(S(O)),
the initial perpetual American put price. Suppose this agent uses the portfolio
process Ll(t) = vL (S(t)) and consumes cash at rate C(t) = rKH{s(t)<L•}
{i.e., consumes cash at rate rK whenever S(t) < L [* ] ). Then the value X(t) of
the agent ['] s portfolio agr s with the option price VL. (S(t)) for all times t until
the option is exercised. In particular, X(t) ;:=: (K - S(t)) [+ ] for all t until the
option is exercised, so the agent can pay off a short option position regardless
of when the option is exercised.


8.3 Perpetual American Put 355


PROOF:
The differential of the agent's portfolio value process is

dX(t) = Ll(t) dS(t) + r(X(t) - Ll(t)S(t)) dt - C(t) dt,

so the differential of the discounted portfolio value process is

d ( e -r [t ] X ( t)) = e -r [t ] ( - r X ( t) dt + dX ( t))
= e-rt (Ll(t) dS(t) - rLl(t)S(t) dt - C(t) dt)

= e-rt (Ll(t)aS(t) dW(t) - C(t) dt). (8.3.24)

Substituting Ll(t) = vL (S(t)) and C(t) = rKH{s(t)<L*} into (8.3.24) and
comparing it to (8.3.21), we see that d(e-rtx(t)) = d[e-rtvL.(S(t))]. In­
tegrating both sides of this equation and using the initial equality X(O) =
vL. (S(O)), we obtain X(t) = VL. (S(t)) for all t prior to exercise. 0
Remark 8.3.8. During any period in which S(t) < L*, the agent in Corollary
8.3.7 has stock position Ll(t) = v�. (S(t)) = -1 (i.e., is short one share of
stock) and has a total portfolio value X(t) = VL. (S(t)) = K - S(t). There­
fore, the agent has K invested in the money market. If the owner of the put
exercises, the agent in Corollary 8.3. 7 receives a share of stock, which covers
his short position, and pays out K from his money market account. If the
owner of the put does not exercise, the agent holds his position and consumes
the interest from the money market investment (i.e., consumes cash at rate
rK per unit time). 0

The argument in Corollary 8.3. 7 applies generally. In a complete market,
whenever some discounted price process is a supermartingale, it is possible to
construct a hedging portfolio whose value tracks the price process. This port­
folio may sometimes consume. In the case of the perpetual American put, the
supermartingale property for the discounted put price follows from (8.3.19).
If, in addition, the price process dominates some intrinsic value (see (8.3.18)
for the perpetual American put), then a short position in the American op­
tion with that intrinsic value can be hedged. There are always two conditions
on the price of any American option, corresponding to (8.3.18) and (8.3.19).
These conditions guarantee that the price is sufficient to satisfy the seller of
the put.
However, conditions (8.3.18) and (8.3.19) alone are not enough to deter­
mine the price of the perpetual American put. There can be functions that
satisfy these conditions but are strictly greater than the price VL. (x) we con­
structed in (8.3.13) (see Exercise 8.2). There must be some additional con­
dition that guarantees that the price is satisfactory for the purchaser of the
put. One version of this condition for the perpetual American put is (8.3.20).
Condition (8.3.20) guarantees that there exists an exercise strategy that per­
mits the owner of the put to capture the full value of the put. It says that if
we divide the half-line [0, oo) into two sets, the stopping set


356 8 American Derivative Securities



(8.3.25)


(8.3.26)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-375-0.png)

These three conditions determine the value of V(O).


8.4 Finite-Expiration American Put


In this section, we consider an American put on a stock whose price is the
geometric Brownian motion (8.3.1), but now the put has a finite expiration
time T.

Definition 8.4.1. Let 0 : t : T and x 2 0 be given. Assume S(t) = x.
Let :F� [t)], t : u : T, denote the a-algebm genemted by the process S(v) as v
mnges over [t, u], and let Tt,r denote the set of stopping times for the filtmtion
:F� [t)], t : u : T, taking values in [t, T] or taking the value oo. In other words,
{T : u} E :F� [t) ] for every u E [t, T]; a stopping time in Tt,r makes the decision
to stop at a time u E [t, T] based only on the path of the stock price between


8.4 Finite-Expiration American Put 357



times t and u. The price at time t of the American put expiring at time T is
defined to be [1 ]



v t, x) max e [-r] (K - S(T)) S(t) x . (8.4.1)
( = rETt,T ( [r-][t] ) =
iE [ I ]



In the event that T = oo, we interpret e [-rr] (K - S(T)) to be zero. This is the
case when the put expires unexercised.

In Subsection 8.4.1 we present without proof the primary analytical prop­
erties of the finite-expiration American put price v(t, x) . These are time­
dependent versions of the properties developed in Section 8.3 for the perpetual
American put. In Subsection 8.4.2, we show that the only function possessing
the analytical properties presented in Subsection 8.4.1 is v(t, x) defined by
(8.4.1).


8.4.1 Analytical Characterization of the Put Price

The finite-expiration American put price function v( t, x) satisfies the linear
complementarity conditions (cf. (8.3.18)-(8.3.20))

v(t, x) ; (K - x) [+ ] for all t E [0, T], x ; 0, (8.4.2)
rv(t, x) - Vt (t, x) - rxvx (t, x) - �a [2] x [2] Vxx (t, x) ; 0
for all t E [0, T), x 0, and (8.4.3)
;
for each t E [0, T) and x ; 0, equality holds in either (8.4.2) or (8.4.3).
(8.4.4)

As with the perpetual American put, the owner of the finite-expiration Amer­
ican put should wait until the stock price falls to a certain level at or below K
before exercising, but now this level L(T t) depends on the time to expiration

              T-t. The level L. of (8.3.12) for the perpetual American put is limr-+oo L(T).
At the other extreme, L(O) = K; at expiration, one should exercise the put if
the stock price is below K, one should not exercise if the stock price is above
K, and one is indifferent between exercising and not exercising if the stock
price is equal to K. No formula is known for the function L(T - t), but this
function can be determined numerically from the analytic characterization of
the put price provided in the next subsection. It is known that L(T) decreases
wtih increasing T, as shown in Figure 8.4.1. The set { ( t, x); 0 � t � T, x ; 0}
can be divided into two regions, the stopping set

S = {(t, x); v(t, x) = (K - x) [+] } (8.4.5)

and the continuation set
1 Here we use v(t, x) rather than v. (x) as in Section 8.3 to denote the put price
because in this section we do not consider functions of t and x other than the put
price itself.


358 8 American Derivative Securities


C {(t, v(t,            - (K - (8.4.6)
= x); x) x)+}.

The graph of the function L(T - t) forms the boundary between C and
x =
S and belongs to S. Because of (8.4.4), equality holds in (8.4.3) for (t, x) in
C, t =f. T. For (t, in S, strict inequality holds in (8.4.3) except on the curve
x)
x = L(T - t), where equality holds in (8.4.3). Because v(t, x) = (K - x)+ =
K - for 0 : : L(T - t), we have see Figure 8.4.1)
x x (

rv(t, x) - Vt(t, x) - rxvx(t, x - 2u x ) [1 ] 2 2 Vxx(t, x) = rK for x E C.


Fig. 8.4.1. Finite-expiration American put.


Because v(t, K - for 0 : : L(T - t), we also have the left­
x) = x x
hand derivative Vx(t, x-) -1 on the curve L(T - t). The put price
= x =
v(t, satisfies the smooth-pasting condition that vx(t, is continuous, even
x) x)
at L(T - t). In other words,
x =

Vx(t, x+) = Vx(t, x-) = -1 for X = L(T - t), 0 $; t < T. (8.4. 7)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-377-0.png)

The smooth-pasting condition does not hold at t = T. Indeed,



L(O) K and (K - (8.4.8)
= v(T,x) = x)+,



so vx(T,x-) = -1, whereas vx(T, x+) = 0 for x = L(O). Also, Vt(t, x) and
Vxx(t, x) are not continuous along the curve L(T - t).
x =
The equations



rv(t, x)- Vt(t, x)- rxvx(t, x)- �u2x2vxx(t, x) = 0, x � L(T - t),
v(t,x) = K - x, 0 : x [·] : L(T - t),


8.4 Finite-Expiration American Put 359


tog [ether with the smooth-pasting condition ] [(8.4.7), ] [the terminal condition ]
(8. [4.8), ][and the asymptotic condition ]

x-+oo lim v(t, x) = 0, (8.4.9)

determine the function v(t,x). Using these equations, one can set up a finite­
dierence scheme to simultaneously compute v(t, x) and L(T - t).


8.4.2 Probabilistic Characterization of the Put Price

Theorem 8.4.2. Let S(u), t ::; u ::; T, be the stock price of (8.3.1} starting
at S(t) = x and with the stopping set S defined by (8.4.5}. Let

r. = min{u E [t, T]; (u, S(u)) [E ] S}, (8.4.10)
where we interpret r. to be oo if (u, S(u)) doesn ['] t enter S for any u E [t, T].

    Then e ruv(u, S(u)), t ::; u ::; T, is a supermartingale under J, and the
stopped process e -r [(] uM,)v(u, S(u 1\ r.)), t ::; u ::; T, is a martingale.

PROOF: The It6-Doeblin formula applies to e -ruv(u, S(u)), even though
Vu(u,x) and Vxx(u,x) are not continuous along the curve x = L(T - u) be­
cause the process S(u) spends zero time on this curve. All that is needed for
the It6-Doeblin formula to apply is that vx(u, x) be continuous (see Exercise
4.20 for a discussion related to this), and this follows from the smooth-pasting
condition (8.4.7). We may thus compute
d[e-ruv(u, S(u))]

= e-ru [- rv(u, S(u)) du + vu(u, S(u)) du + vx(u, S(u)) dS(u)

+ Vxx ( u, S(u)) dS(u) dS(u)

      - ]



1
+2u [2] S [2] (u)vxx(u, S(u)) du + e [-r] uuS(u)vx(u, S(u)) dW(u). ###### ]
= e-ru [ -rv(u, S(u)) + vu(u, S(u)) + rS(u)vx(u, S(u))



(8.4.11)



According to Figure 8.4.1, the du term in (8.4.11) is -e-rurKH{s(u)<L(T-u)}·
This is nonpositive, and so e-ruv(u, S(u)) is a supermartingale under J. In
fact, starting from u = t and up until time r., we have S(u) > L(T-u), so the
term is zero. Therefore, the stopped process e-r(uM,)v(u 1\ r., S(u 1\ r.)),
du
u ::; T, is a martingale. 0
t ::;

Corollary 8.4.3. Consider an agent with initial capital X(O) = v(O, S(O)),
the initial finite-expiration put price. Suppose this agent uses the portfolio pro­
cess Ll(u) = vx(u, S(u)) and consumes cash at rate C(u) = rKH{s(u)<L(T-u)}


360 8 American Derivative Securities

per unit time. Then X(u) = v(u, S(u)) for all times u between u = 0 and the
time the option is exercised or expires. In particular, S(u) � (K - S(u)) [+ ] for
all times u until the option is exercised or expires, so the agent can pay off a
short option position regardless of when the option is exercised.


PROOF:
The differential of the agent's discounted portfolio value is given by
(8.3.24). Substituting for Ll(u) and C(u) in this equation and comparing it
to (8.4.11), we see that d(e-ru X(u)) = d[e-ruv(u, S(u))]. Integrating this
equation and using X(O) = v(O, S(O)), we obtain X(t) = v(t, S(t)) for all
times t prior to exercise or expiration. 0
Remark 8.4.4. The proofs of Theorem 8.4.2 and Corollary 8.4.3 use the ana­
lytic characterization of the American put price captured in Figure 8.4.1 plus
the smooth-pasting condition that guarantees that vx(t, x) is continuous even
on the curve x = L(T-t) so that the lt6-Doeblin formula can be applied. Here
we show that the only function v( t, x) satisfying these conditions is the func­
tion v(t,x) defined by (8.4.1). To do this, we first fix t with 0 : t : T. The
supermartingale property for e-rtv(t, S(t)) of Theorem 8.4.2 and Theorem
8.2.4 (optional sampling) implies that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-379-0.png)







Because S(t) is a Markov process, the right-hand side of (8.4.14) is a function
of t and S(t). In particular, if we denote the value of S(t) by x, we may rewrite
(8.4.14) as
e [-] r [t] v(t, x) = [e [-] rr (K - S(r)) I S(t) = x] . (8.4.15)
Since (8.4.15) holds for any T E iE 7t,r, we conclude that

v(t, x) � max fE [e [-] r [(] r [-t) ] (K - S(r)) S(t) = x . (8.4.16)
r [ETt.T ]
i ]


8.5 American Call 361


For the reverse inequality, we recall from Theorem 8.4.2 that the stopped
process e [-r(tM' ] >v(t l\r., S(t l\ r.)) is a martingale, where r. defined by (8.4.10)
is such that v(r., S(r.)) = K - S(r.) if r. < [oo] . Replacing T by r. in (8.4.12),

we make the first inequality into an equality. If r [* ] = oo, we have (T, S(T)) E C
(i.e., S(T) > K), so v(T, S(T))H{r.=oo} = 0. This makes the second inequality
in (8.4.12) into an equality. Finally, because v(r, S(r)) = K -S(r) on n{r<oo}'
the inequality in (8.4.13) is an equality, and hence (8.4.15) becomes

(8.4.17)


0


(8.5.2)

See Figure 8.5.1 for the case of a call payoff, h(x) = (x - K) [+] .
Taking x1 = 0, x2 = x, and using the fact that h(O) = 0, we obtain from
(8.5.2) that
h(Ax) $ Ah(x) for all x : 0, 0 $ A $ 1. (8.5.3)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-380-0.png)
362 8 American Derivative Securities



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-381-0.png)





























This is the submartingale property for e-rth(S(t)).





D



Theorem 8.5.2. Let h(x) be a nonnegative, convex function of x 0 satis­
2:
fying h(O) [= ] 0. Then the price of the American derivative security expiring
at time T and having intrinsic value h(S(t)), 0 $ t $ T, is the same as the
price of the European derivative security paying h(S(T)) at expiration T.



PROOF: Replacing t by T in (8.5.7), we obtain


8.5 American Call 363


outflow.


(8.5.9)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-382-0.png)
8 American Derivative Securities


We a ume that each a3, j = 1, . . ., n, is a number between 0 and 1. We set
t0 = 0, but this is not a dividend payment date. We also a ume that T is not
a dividend payment date, although it is not difficult to modify the analysis
given below to handle the case when T is a dividend payment date.
We shall see that it is not optimal to exercise an American call on this
a et except possibly immediately before a dividend payment. The price of
the call will be seen to satisfy the Black-Scholes-Merton partial differential
equation between dividend payment dates. At dividend payment dates, the
price of the call is the maximum of the call's intrinsic value and the price
of the call after the dividend is paid and the stock price is reduced by the
amount of the payment. These observations lead to a recursive algorithm for
determining the price, and that is developed in this subsection.
The a et price process in this section was considered in Subsection 5.5.4.
For t3 � t < t3+1, we have


(8.5.10)


(8.5.11)


(8.5.13)

364



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-383-0.png)
8.5 American Call 365

is greater than the intrinsic value of the American call, ( S ( t) - K) [+] . Conse­
quentl [y, the early exercise feature of the American call is worthless, and the ]
p [rices at time ] [t ][of the European and American calls agree for ][tn � t � T. ]
price is given by the Black-Scholes-Merton formula
This

en(t, x) = xN(d+(T - t, x)) - Ke [-] r [(T-t) ] N(d-(T - t, x)), (8.5.14)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-384-0.png)













is



convex in x. It follows that
is


366 8 American Derivative Securities



Cn(tn, (1 - A)XI + AX2)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-385-0.png)











This shows that cn(t, (1 - an)x) is a convex function of x. The maximum of
two convex functions is convex (see Exercise 8.7), and therefore hn(x) defined
by (8.5.20) is convex.
Starting from time t, where tn-I � t < tn, the owner of the American call
can exercise at any time u E [t, tn), and if she does, she receives S(u) - K.
If she does not exercise prior to tn, then at time tn, immediately before the
dividend payment, she owns a call whose value we have just determined to be
hn(S(tn-)). Therefore, for tn-I :S t < tn, the American call expiring at time
T has the same price as the American call expiring immediately before the
dividend payment at date tn and paying hn(S(tn-)) upon expiration.


8.5 American Call 367


Because the underlying a et evolves as a geometric Brownian motion after
the dividend is paid at time tn-1 until the dividend is paid at time tn, Lemma
8.5.1 implies that e-rthn(S(t)) is a submartingale for tn-1 � t < tn. In
particular,


(8.5.21)


(8.5.23)


(8.5.25)


tn-1                        - t < tn, X ; 0, (8.5.26)

and the terminal condition



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-386-0.png)
368 8 American Derivative Securities



(8.5.27)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-387-0.png)

(8.5.29)


(8.5.30)

For t3_1 � t < t3, if S(t) = x, then c3_1(t, x) is the American call price.
Within each interval [t3_�, t3 ), the American call price is actually the price of
a European call expiring at t3• The optimal exercise time is immediately prior
to the dividend payment at the smallest time t3 for which S(t3-) - K exceeds
c3(t3, (1 - a3)S(t3- )) . If there is no t3 for which this condition is satisfied,
then optimal exercise takes place at time T if S(T) - K, and otherwise the
option should be allowed to expire unexercised.


8.6 Summary


This chaper discusses American puts and calls. To do this, we introduce the
notions of stopping times and optional sampling in Section 8.2. The value of
an American option can then be defined as the maximum over all stopping
times of the discounted, risk-neutral payoff of the option evaluated at the
stopping time. We do this for the perpetual American put in Section 8.3 and
for the finite-horizon American put in Section 8.4. This definition of option
value gives the no-arbitrage price. Starting with initial capital given by this
definition, a person holding a short position in the option can hedge in such
a way that, regardless of when the option is exercised, he will be able to pay
off the short position. Furthermore, this definition of American option price
is the smallest initial capital that permits such hedging. In particular, there


8.7 Notes 369


is an optimal stopping time, and if the option owner exercises at this time,
she captures the full value of the option.
The American put has an analytical characterization, which we present as
linear complementarity conditions in Subsections 8.3.3 and 8.4.1. According
to this characterization, there are two regions in the space of time and stock
prices (t, x), one in which it is optimal to exercise the put (the stopping set)
and another in which it is optimal not to exercise (the continuation set) .
The put price v(t, x) and its first derivative vx(t, x) are continuous across the
boundary between these two regions (smooth pasting), and this fact tells us
that vx(t, x) = -1 on this boundary. Using this smooth-pasting condition,
one can solve numerically for the American put price.
The American call on a stock that pays no dividends has the same price as
the corresponding European call; see Section 8.5.1. If the stock pays dividends,
the American call can be more valuable than the European call. In Section
8.5.2, we work out an algorithm for the American call price when dividends
are paid at discrete dates.


8.7 Notes


The use of stopping times with martingales was pioneered by Doob [53), who
provided Theorem 8.2.4. A modern treatment can be found in many texts,
including Chung [35] and Williams [161] in discrete time and Karatzas and
Shreve [101] in continuous time.
The perpetual American put problem was first solved by McKean [119),
who also wrote down the analytic characterization of the finite-horizon Amer­
ican put price. The fact that this analytic characterization determines the
finite-horizon American put price follows from the optimal-stopping theory
developed by van Moerbeke [153]. For the particular case of the American
put, a simpler derivation of this fact is provided by Jacka [93], and this is
presented in Section 2. 7 of Karatzas and Shreve [102]. Although the price of
the American put cannot be computed explicitly, it is possible to give a vari­
ety of characterizations of the early exercise premium, the difference between
the American put price and the corresponding European put price; see Carr,
Jarrow, and Myneni [27), Jacka [93), and Kim [103].
The probabilistic characterization of the American put price is due to
Bensoussan [9] and Karatzas [100]. This is also reported in Section 2.5 of
Karatzas and Shreve [102]. A survey of all these things, and a wealth of
other references, are provided by Myneni [127]. Merton [122] observed that
an American call on a stock paying no dividends has the same value as a
European call.
There are two principal ways to compute option prices numerically: finite­
difference schemes and Monte Carlo simulation. finite-difference scheme
A
for the American put is described in Wilmott, Howison, and Dewynne [165].


370 8 American Derivative Securities


Monte Carlo methods are more difficult to develop because one must simulta­
neously determine the price of the put and determine the boundary between
the stopping and continuation sets. A novel method to deal with this was
recently provided by Longstaff and Schwartz [112) and Tsitsiklis and Van Roy

[152) . Results on convergence of a modification of the Longstaff-Schwartz algo­
rithm can be found in Clement, Lamberton, and Protter [37) and Gla erman
and Yu [75). Papers that use binomial trees and analytic approximations are
listed in Section 2.8 of Karatzas and Shreve [102).


8.8 Exercises


Exercise 8.1 (Determination of L,. by smooth pasting). Consider the
function VL(x) in (8.3.11). The first line in formula (8.3.11) implies that the
left-hand derivative of VL(x) at x = L is vL(L-) = -1. Use the second line
in formula (8.3.11) to compute the right-hand derivative vL(L+). Show that
the smooth-pasting condition

v�. (L,.-) = v (L,.+)
L

is satisfied only by L,. given by (8.3.12).

Exercise 8.2. Consider two perpetual American puts on the geometric Brow­
nian motion (8.3.1). Suppose the puts have different strike prices, K1 and K2,
where 0 < K1 < K2. Let v1 (x) and v2 (x) denote their respective prices,
as determined in Section 8.3.2. Show that v2 (x) satisfies the first two linear
complementarity conditions,



v2(x) � (K1 - x) [+ ] for all x � 0,
1
rv2(x) - rxv;(x) - 2u [2] x [2] v�(x) � 0 for all x � 0,



(8.8.1)

(8.8.2)



for the perpetual American put price with strike K1 but that v2 (x) does not
satisfy the third linear complementarity condition:

for each x � 0, equality holds in either (8.8.1) or (8.8.2) or both. (8.8.3)

Exercise 8.3 (Solving the linear complementarity conditions). Sup­
pose v(x) is a bounded continuous function having a continuous derivative
and satisfying the linear complementarity conditions (8.3.18)-(8.3.20). This
exercise shows that v(x) must be the function VL. (x) given by (8.3.13) with
L,. given by (8.3.12). We a ume that K is strictly positive.
(i) First consider an interval of x-values in which v(x) satisfies (8.3.19) with
equality, i.e., where


(8.8.4)


8.8 Exercises 371


Equation (8.8.4) is a linear, second-order ordinary differential equation,
and it has two solutions of the form xP, the solutions differing because
of different values of p. Substitute xP into (8.8.4) and show that the only
values of p that cause xP to satisfy (8.8.4) are p = - and p = 1.

(ii) The functions x [-] -2r and x are said to be linearly independent solutions
of (8.8.4), and every function that satisfies (8.8.4) on an interval must be
of the form
f(x) = Ax [-] -2r + Bx
for some constants A and B. Use this fact and the fact that both v ( x)
and v'(x) are continuous to show that there cannot be an interval [x1, x2],
where 0 < x1 < x2 < oo, such that v(x) satisfies (8.3.19) with equality
on [x�, x2] and satisfies (8.3.18) with equality for x at and immediately to
the left of x1 and for x at and immediately to the right of x2 unless v(x)
is identically zero on [ x�, x2].
(iii) Use the fact that v(O) must equal K to show that there cannot be a
number x2 > 0 such that v(x) satisfies (8.3.19) with equality on [O, x2].
(iv) Explain why v(x) cannot satisfy (8.3.19) with equality for all x 0.
2
(v) Explain why v(x) cannot satisfy (8.3.18) with equality for all x 2 0.
(vi) From (iv) and (v) and (8.3.20), we see that v(x) sometimes satisfies
(8.3.18) with equality and sometimes does not satisfy (8.3.18) with equal­
ity, in which case it must satisfy (8.3.19) with equality. From (ii) and (iii)
we see that the region in which v(x) does not satisfy (8.3.18) with equal­
ity and satisfies (8.3.19) with equality is not an interval [x�, x2], where
0   - x1 < x2 < oo, nor can this region be a union of disjoint intervals
of this form. Therefore, it must be a half-line [x�, oo), where x1 > 0. In
the region [O, xi], v(x) satisfies (8.3.18) with equality. Show that X1 must
equal L* given by (8.3.12) and v(x) must be VL. (x) given by (8.3.13).

Exercise 8.4. It was a erted at the end of Subsection 8.3.3 and established
in Exercise 8.3 that VL. (x) given by (8.3.13) is the only bounded continuous
function having a continuous derivative and satisfying the linear complemen­
tarity conditions (8.3.18)-(8.3.20). There are, however, unbounded functions
that satisfy these conditions. Let 0 L K be given, and a ume that
< <
2r
(8.8.5)
2 [K > L. ]
2 r + u

(i) Show that, for any constants A and B, the function

f(x) = Ax [-] -2r + Bx (8.8.6)

satisfies the differential equation

1
rf(x) - rxf'(x) - 2u [2] x [2 ] J"(x) = 0 for all x 2 0. (8.8.7)


372 8 American Derivative Securities



(ii) Show that the constants A and B can be chosen so that
f(L) = K - L, f'(L) = -1. (8.8.8)



(iii) With the constants A and B you chose in (ii), show that f(x) � (K - x) [+ ]
for all x L.

       (iv) Define
v(x) =
{ f [K -] (x), x [ x, ][0 � ]                 - [x ] L. [� L, ]
Show that v(x) satisfies the linear complementarity conditions (8.3.18)­
(8.3.20), but v(x) is not the function VL. (x) given by (8.3.13).
(v) Every solution of the differential equation (8.8.7) is of the form (8.8.6).


where W(t) is a Brownian motion under a risk-neutral measure JPi. (Equation
(8.8.9) can be obtained by computing the differential in (5.5.8).)
(i) Suppose we adopt the strategy of exercising the put the first time the
a et price is at or below L. What is the risk-neutral expected discounted
payoff of this strategy? Write this as a function vL(x) of the initial a et
price x. (Hint: Define the positive constant



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-391-0.png)

I' = � - a - [�] u [2] + [� ] - - a - [�] u [2] + 2r
###### u [2 ] ( [r ] 2 ) u u [2 ] ( [r ] 2 ) [2 ]



and write vL(x) using I'·)
(ii) Determine L., the value of L that maximizes the risk-neutral expected
discounted payoff computed in (i).
(iii) Show that, for any initial a et price S(O) = x, the process e-rtvL. (S(t)) is
a supermartingale under JPi. Show that if S(O) = x > L. and e-rtvL. (S(t))
is stopped the first time the a et price reaches L., then the stopped
supermartingale is a martingale. (Hint: Show that
1
r + (r             - a)/' - 2u [2] ')'(/' + 1) = 0. ) (8.8.10)



(iv) Show that, for any initial a et price S(O) = x,

VL. (x) = maxfE TEl [e [-] r,.(K - S(r))] .
(8.8.11 )


8.8 Exercises 373


Exercise 8.6. There is a second part to Theorem 8.2.4 (optional sampling),
which says the following.

Theorem 8.8.1 (Optional sampling - Part II). Let X(t), t 2 0, be a
submartingale, and let r be a stopping time. Then IEX(tl\r) : IEX(t). If X(t)
is a supermartingale, then IEX(t 1\ r) 2 IEX(t). If X(t) is a martingale, then
IEX(t A r) = IEX(t).

The proof is technical and is omitted. The idea behind the statement about
submartingales is the following. Submartingales tend to go up. Since tAr : t,
we would expect this upward trend to result in the inequality lEX ( t A r)
::=;
IEX(t). When r is a stopping time, this intuition is correct. Once we have
Theorem 8.8.1 for submartingales, we easily obtain it for supermartingales by
using the fact that the negative of a supermartingale is a submartingale. Since

a martingale is both a submartingale and a supermartingale, we obtain the
equality IEX(t A r) = IEX(t) for martingales.
Use Theorem 8.8.1 and Lemma 8.5.1 to show in the context of Subsection
8.5.1 that


(8.8.12)


holds. Suppose f(x) and g(x) are convex functions defined for x 2 0. Show
that
h(x) = max{!(x), g(x)}

is also convex.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-392-0.png)
This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-393-0.png)
9


Change of N umeraire


9 . 1 Introduction


A numeraire is the unit of a ount in which other a ets are denominated. One
usually takes the numeraire to be the currency of a country. One might change
the numeraire by changing to the currency of another country. As this example
suggests, in some applications one must change the numeraire in which one
works because of finance considerations. We shall see that sometimes it is
convenient to change the numeraire because of modeling considerations as
well. A model can be complicated or simple, depending on the choice of the
numeraire for the model.
In this chapter, we will work within the multidimensional market model
of Section 5.4. In particular, our model will be driven by a d-dimensional
Brownian motion W(t) = (W1(t), . . ., Wd(t)), 0 � t � T, defined on a prob­
ability space (!?, .1', IP'). In particular, W1, . . ., Wd are independent Brownian
motions. The filtration F(t), 0 � t � T, is the one generated by this vector of
Brownian motions. There is an adapted interest rate process R(t), 0 � t � T.
This can be used to create a money market a ount whose price per share at
time t is
M(t) = e [f; R(u)du] .
This is the capital an agent would have if the agent invested one unit of
currency in the money market a ount at time zero and continuously rolled
over the capital at the short-term interest rate. We also define the discount
process
D(t) = [e-][ J; ][R(u)du ] =
M(t)
There are m primary a ets in the model of this chapter, and their prices
satisfy equation (5.4.6), which we repeat here:
d
dSi (t) = ai(t)Si(t) dt + Si(t) L aij(t) dWj(t), i = 1, . . ., m. (9.1.1)
1= [1 ]


376 9 Change of Numeraire

We a ume there is a unique risk-neutral measure lP (i.e., there is a unique
d-dimensional process B(t) = (81(t), . . ., 8d(t)) satisfying the market price
of risk equations (5.4.18)). The risk-neutral measu�e is constructed using the
multidimensional Girsanov Theorem 5.4.1. Under IP', the Brownian motions


are independent of one another. According to the Second Fundamental Theo­
rem of Asset Pricing, Theorem 5.4.9, the market is complete; every derivative
security can be hedged by trading in the primary a ets and the money market
a ount.
Under JP, the discounted a et prices D(t)Si(t) are martingales, and so
the discounted val_ue of every portfolio process is also a martingale. The risk­
neutral measure lP' is thus a ociated with the money market a ount price
M(t) in the following way. If we were to denominate the ith a et in terms
of the money market a ount, its price would be Si(t)/M(t) = D(t)Si(t). In
other words, at time t, the ith a et is worth D(t)Si(t) shares of the money
market a ount. This process, the value of the ith a et denominated in shares
of the money market a ount, is a martingale under JP. We say the measure lP
is risk-neutral for the money market account numeraire.
When we change the numeraire, denominating the ith a et in some other
unit of a ount, it is no longer a martingale under JP. When we change the
numeraire, we need to also change the risk-neutral measure in order to main­
tain risk neutrality. The details and some applications of this idea are devel­
oped in this chapter.


9.2 Numeraire


In principle, we can take any positively priced a et as a numeraire and de­
nominate all other a ets in terms of the chosen numeraire. Associated with
each numeraire, we shall have a risk-neutral measure. When making this as­
sociation, we shall take only non-dividend-paying a ets as numeraires. In
particular, we regard lP as the risk-neutral measure a ociated with the do­
mestic money market account, not the domestic currency. Currency pays a
dividend because it can be invested in the money market. In contrast, in our
model, a share of the money market a ount increases in value without paying
a dividend.
The numeraires we consider in this chapter are:

- Domestic m£ney market a ount. We denote the a ociated risk-neutral
measure by IP'. It is the one discussed in Section 9.1.

- Foreign money market a ount. We denote the a ociated risk-neutral mea­
sure by jpf. It is constructed in Section 9.3 below.


9.2 Numeraire 377

- A zero-coupon bond maturing at time T. We denote the a ociated risk­
neutral measure by jp> [T] . It is called the T -forward measure and is used in
Section 9.4.
The a et we take as numeraire could be one of the primary a ets given
by (9.1.1) or it could be a derivative a et. Regardless of which a et we take,
it has the stochastic representation provided by the following theorem.

Theorem 9.2.1 (Stochastic representation of assets). Let be a
N
strictly positive price process for a non-dividend-paying asset, either primary
or derivative, in the multidimensional market model of Section 9.1. Then there
exists a vector volatility process
v(t) = (v1(t), ...,vd(t))

such that
dN(t) = R(t)N(t) dt + N(t)v(t) · dW(t). (9.2.1)
This equation is equivalent to each of the equations

d(D(t)N(t)) = D(t)N(t)v(t) · dW(t), (9.2.2)


(9.2.4)


have no effect on return).


PROOF:
D(t)N(t)

d

j=l



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-396-0.png)
378 9 Change of Numeraire



Then
d (D(t)N(t)) = D(t)N(t)v(t) · dW(t),
which is (9.2.2).
The solution to (9.2.2) is (9.2.3), as we now show. Define



so that



d
1 [d ]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-397-0.png)

1 [d ]



Then


=





(9.2.5)








9.2 Numeraire 379



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-398-2.png)



(9.2.7)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-398-0.png)









(9.2.8)



=





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-398-1.png)

(9.2.9)


380 9 Change of N umeraire



We are not saying that volatilities subtract when we change the numeraire.
We are saying that volatility vectors subtract. The process N(t) in Theo­
rem 9.2.2 has the stochastic differential representation (9.2.1), which we may
rewrite as



dN(t) [= ] R(t)N(t) dt + llv(t)IIN(t)dB [N ] (t),
where



(9.2.10)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-399-0.png)

=



See Exercise 9.1.




###### }


###### }



and hence



(lla(u)ll [2 ]                    - llv(u)ll2) du .
###### }
=


9.3 Foreign and Domestic Risk-Neutral Measures 381


To apply the ItO-Doeblin formula to this, we first define



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-400-0.png)

so that



















Since w<Nl(t) is a d-dimensional Brownian motion under p(N), the process
s<Nl(t) is a martingale under this measure. D


9.3 Foreign and Domestic Risk-Neutral Measures


9.3.1 The Basic Processes


We now apply the ideas of the previous section to a market with two curren­
cies, which we call foreign and domestic. This model is driven by


382 9 Change of Numeraire


=
W(t) (W1(t), W2(t)),

a two-dimensional Brownian motion on some ( n, .r, IP). In particular, we are
a uming that W1 and W2 are independent under IP. We begin with a stock
whose price in domestic currency, S(t), satisfies

dS(t) [= ] o(t)S(t) dt + o-1 (t)S(t) dW1 (t). (9.3.1)

There is a domestic interest rate R(t), which leads to a domestic money market
account price and domestic discount process


There is also a foreign interest rate Rf (t), which leads to a foreign money
market account price and foreign discount process


We define


(9.3.3)


=

M(t) = ef� R(u)du, D(t) = e- J� R(u)du.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-401-0.png)





the process p(t) is the instantaneous correlation between relative changes in
S(t) and Q(t).


9.3 Foreign and Domestic Risk-Neutral Measures 383


9.3.2 Domestic Risk-Neutral Measure

There are three a ets that can be traded: the domestic money market account,
the stock, and the foreign money market account. We shall price each of these
in domestic currency and discount at the domestic interest rate. The result
is the price of each of them in units of the domestic money market account.
Under the domestic risk-neutral measure, all three a ets priced in units of the
domestic money market account must be martingales. We use this observation
to find the domestic risk-neutral measure.
We note that the first a et, the domestic money market account, when
priced in units of the domestic money market, has constant price 1. This is
always a martingale, regardless of the measure being used.
The second a et, the stock, in units of the domestic money market account
has price D(t)S(t), and this satisfies the stochastic differential equation
d(D(t)S(t)) = D(t)S(t) [ ( a(t) - R(t)) dt + u1 (t) dW1 (t)) . (9.3.5)

We would like to construct a process


)


=


=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-402-0.png)
384 9 Change of N umeraire

and then using Ito's product rule again on D(t) · Mf (t)Q(t) to obtain (9.3.8).
The mean rate of change of Q(t) is -y(t). When we inflate this at the foreign
interest rate and discount it at the domestic interest rate, (9.3.8) shows that
the mean rate of return changes to Rf (t) - R(t) + -y(t). The volatility terms
are unchanged. _
In addition to the process W1 ( t), we would like to construct a process


(9.3.12)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-403-0.png)
9.3 Foreign and Domestic Risk-Neutral Measures 385


All these price proce�es have mean rate of return R(t) under the domestic
risk-neutral measure JP>. We constructed the domestic risk-neutral measure so
this is the case.
We may multiply Mf(t)Q(t) by Df(t) and use Ito's product rule again to
obtain

dQ(t) [= ] Q(t) [(R(t) - Rf (t)} dt + a2(t)p(t) dW1 (t) + p [2] (t) dW2(t)]


=
Q(t) ( ( R(t) - Rf (t)} dt + a2(t) dW3(t)). (9.3.16)

Under the domestic risk-neutral measure, the mean rate of change of the
exchange rate is the difference between the domestic and foreign interest rates
R(t) - Rf (t). In particular, it is not R(t), as would be the case for an a et. If
one regards the exchange rate as an a et (i.e., hold a unit of foreign currency
whose value is always Q(t)), then it is a dividend-paying a et. The unit of
foreign currency can and should be invested in the foreign money market, and
this pays out a continuous dividend at rate Rf (t). If this dividend is reinvested
in the foreign money market, then we get the a et in (9.3. 15), which has mean
rate of return R(t); if the dividend is not reinvested, then the rate of return
is reduced by Rf(t) and we have (9.3.16) (cf. (5.5.6)).
It is important to note that (9.3.16) tells us about the mean rate of change
of the exchange rate under the domestic risk-neutral measure. Under the ac­
tual probability measure JP>, the mean rate of change of the exchange rate can
be anything. There are no restrictions on the process 'Y(t) in (9.3.2).


9.3.3 Foreign Risk-Neutral Measure


In this model, we have three a ets: the domestic money market account, the
stock, and the foreign money market account. We list these a ets across the
top of Figure 9.3.1, and down the side of the figure we list the four ways of
denominating them.
ln_the previous subsection, we constructed the domestic risk-neutral mea­
sure JP> under which the three entries in the second line of Figure 9.3.1 are
martingales. In this subsection, we construct the foreign risk-neutral measure
under which the entries in the fourth line are martingales. (We cannot make
all the entries in the first line be martingales because every path of the pro­
cess M(t) is increasing, and thus this process is not a martingale under any
measure. The same applies to the entries in the third line, which contains the
increasing process M f ( t).)
We observe that the fourth line in Figure 9.3.1 is obtained by dividing
each entry of the second line by D(t)Mf(t)Q(t). In other words, to find the
foreign risk-neutral measure, we take the foreign money market a ount as the
numeraire. Its value at time t, denominated in units of the domestic money
market account, is D(t)Mf (t)Q(t), and denominated in units of domestic
currency, it is Mf(t)Q(t). The differential of Mf(t)Q(t) is given in (9.3.15),
and from that formula we see that its volatility vector is


386 9 Change of N umeraire



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-405-0.png)

(9.3.17)














9.3 Foreign and Domestic Risk-Neutral Measures 387


=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-406-0.png)
388 9 Change of N umeraire





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-407-0.png)







= �







(9.3.25)



b



(9.3.26)

(9.3.27)



Both Q and have the same volatility. (A change of sign in the volatility
b
does not affect volatility because Brownian motion is symmetric. ) However,
the mean rates of change of Q and are not negatives of one another.
b


9.3.5 Forward Exchange Rates

We assume in this subsection that the domestic and foreign interest rates are
constant and denote these constants by r and rf, respectively. Recall that
Q is units of domestic currency per unit of foreign currency. The exchange
rate from the domestic viewpoint is governed by the stochastic differential
equation (9.3.16)


9.3 Foreign and Domestic Risk-Neutral Measures 389



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-408-0.png)












390 9 Change of Numeraire


9.3.6 Garman-Kohlhagen Formula



In this section, we a ume the domestic and foreign interest rates r and rf
and the volatility a2 are constant. Consider a call on a unit of foreign currency
whose payoff in domestic currency is ( Q(T) - K) [+] . At time zero, the value of
this is
Ee-rT(Q(T) - K)+.
In this case, (9.3.16) becomes





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-409-0.png)











+
### ]·





(9.3.28)


and N is the cumulative standard normal distribution function. Equation
(9.3.28) is called the Garman-Kohlhagen formula.


9.3. 7 Exchange Rate Put-Call Duality

In this subsection, we develop a relationship between a call on domestic cur­
rency, denominated in foreign currency, and a put on a foreign currency, de­
nominated in the domestic currency.
Recall the numeraire Mf (t)Q(t), which is the domestic price of the foreign
money market account. The Radon-Nikodym derivative of the foreign risk­
neutral measure with respect to the domestic risk-neutral measure is (see
(9.3.17))


9.3 Foreign and Domestic Risk-Neutral Measures 391





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-410-0.png)





IE! Df (T)





+
### ]








currency is





The call we began with has a value K times this amount. When we denominate
both the call and the put this way in foreign currency, we can then understand
the final result. Indeed, we have seen that the option to exchange K units of
foreign currency for one unit of domestic currency (the call) is the same as
K options to exchange units of domestic currency for one unit of foreign
f<
currency (the put). Stated in this way, the result is almost obvious.


9 Change of N umeraire


9.4 Forward Measures


Although there may be multiple Brownian motions driving the model of this
section, in order to simplify the notation, we a ume in this section that there
is only one. It is not difficult to rederive the results presented here under the
a umption that there are d Brownian motions.


9.4.1 Forward Price


We recall the discussion of Section 5.6.1. Consider a zero-coupon bond that
pays 1 unit of currency (all currency is domestic in this section) at maturity
T. According to the risk-neutral pricing formula, the value of this bond at
time t (0, T) is
E
1 B(t, T) = D(t)lE [D(T) iF(t)] . (9.4.1)

In particular, B(T, T) = 1.
Consider now an a et whose price denominated in currency is S(t).
A
forward contract that delivers one share of this a et at time T in exchange
for K has a time-T payoff of S(T) - K. According to the risk-neutral pricing
formula, the value of this contract at earlier times t is


1 

The T -forward price Fors(t, T) at time t (0, T) of an a et is the value of K
E
that causes the value of the forward contract in (9.4.2) to be zero:

392



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-411-0.png)

S(t)
Fors(t, T) = B(t, T) .


9.4.2 Zero-Coupon Bond as Numeraire



(9.4.3)



A zero-coupon bond is an a et, and therefore the discounted bond price
D(t)B(t, T) must be a martingale under the risk-neutral measure JP. According
to Theorem 9.2.1, there is a volatility process u*(t, T) for the bond (a process
in t; T is fixed) such that

d D(t)B(t, T) = -u*(t, T)D(t)B(t, T) dW(t).
( )

In (9.4.4), we write -u*(t, T) rather than u*(t, T) in order to be consistent
with the notation used in our discussion of the Heath-Jarrow-Morton model

(9.4.4)


9.4 Forward Measures 393



in [Chapter ][10. ][This has no effect on the distribution of the bond price process ]
since we could ust as well write (9.4.4) as
j



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-412-1.png)

j



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-412-0.png)

measure Jr by

      


a

(


( )

I ]

This gives us the simple formula
V(t) B(t,T) [ET ] [V(T)iF(t)] . (9.4.7)
=

If we can find a simple model for the evolution of a ets under the T-forward
measure, we can use (9.4.7), in which we only need to estimate V T, instead
( )
of using (9.4.6), which requires us to estimate D T V T . give an example
( ) ( ) We
of the power of this approach in the next subsection.


394 9 Change of Numeraire


9.4.3 Option Pricing with a Random Interest Rate


The classical Black-Scholes-Merton option-pricing formula assumes a constant
interest rate. For options on bonds and other interest-rate-dependent instru­
ments, movements in the interest rate are critical. For these "fixed income"
derivatives, the a umption of a constant interest rate is inappropriate.
In this section, we present a generalized Black-Scholes-Merton option­
pricing formula that permits the interest rate to be random. The cla ical
Black-Scholes-Merton a umption that the volatility of the underlying a et
is constant is here replaced by the a umption that the volatility of the for­


(9.4.10)


=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-413-0.png)
9.4 Forward Measures 395



1.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-414-0.png)













(9.4.12)




###### a.





At time zero, the value of a European call expiring at time T, according
to the risk-neutral pricing formula, is


396 9 Change of Numeraire

V(O) = iE [D(T)(S(T) - K) [+] ]
= iE [ D(T)S(T)H{S(T)>K}] - KE [ D(T)H{S(T)>K}]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-415-0.png)



J!D -8








### }







(9.4.14)


9.5 Summary 397


This gives us the option price denominated in zero-coupon bonds. Suppose

we hedge a short position in the option by holding N(d+(t)) shares of the
a et and shorting KN(d_(t)) zero-coupon bonds at each time t. The value of
this portfolio, denominated in units of zero-coupon bond, agrees with (9.4.14).
be sure this short option hedge works, however, we must verify that the
To
portfolio just described is self-financing. In other words, we must be sure we
do not need to infuse cash in order to maintain the positions just described. (A
discussion related to this, pa ing from discrete to continuous time, is provided
Exercise 4.10 of Chapter 4.) The capital gains differential a ociated with
in
this portfolio, again denominated in units of zero-coupon bond, is
N(d+(t)) dFors(t, T).

(When measuring wealth in units of zero-coupon bond, there is no capital gain
from movements in the bond price.) The differential of the portfolio, according
to Ito's formula, is
V(t)
d B(t, ( T) ) = N(d+(t)) dFors(t, T) + Fors(t, T) dN(d+(t))

+dFors(t, T) dN(d+(t)) - K dN(d_(t)). (9.4.15)

In order for the portfolio to be self-financing, we must have

Fors(t, T) dN(d+(t)) + dFors(t, T) dN(d+(t)) - K dN(d_(t)) 0, (9.4.16)
=

so that the change of value in the portfolio is entirely due to capital gains.
The verification of (9.4.16) is Exercise 9.6. 0


9.5 Summary


This chapter discusses the fact that when we change the units of account, the
so-called numemire, we must change the risk-neutral measure. Fortunately,
the Radon-Nikodym derivative process needed to effect this change of measure
is simple; it is the numeraire itself, discounted in order to be a martingale and
normalized by its initial condition in order to have expected value 1. This is
the content of Theorem 9.2.2.
In this chapter, we apply the change-of-numeraire idea in two cases: foreign
exchange models and option pricing in the presence of a random interest rate.
It was also used in the discussion of Asian options in Section 7.5.
In the context of foreign exchange models, we show that the mean rate of
change of the exchange rate is the difference betw n the interest rates in the
two economies under the risk-neutml measure for the economy in which the
exchange rote is being considered. We show that one can derive other expected
symmetries (e.g., the forward exchange rate in one currency is the reciprocal
of the foreign exchange rate in the other currency), provided one is careful to
use the appropriate risk-neutral measures.


398 9 Change of Numeraire


When the interest rate is random, the cla ical Black-Scholes-Merton
option-pricing formula does not apply. However, if one is willing to a ume
that the T-forward price of the underlying a et has constant volatility, then
the price of a call expiring at time T has a simple formula and a simple hedg­
ing strategy (Theorem 9.4.2). This fact is exploited to build LIBOR models
in Section 10.4.


9.6 Notes


The model of foreign and domestic markets presented in this chapter is a
simplification of one in Musiela and Rutkowski [126). The model in [126),
drawn from Amin and Jarrow [2), permits foreign and domestic interest rates
to be random. The Garman-Kohlhagen formula of Subsection 9.3.6 is taken
from Garman and Kohlhagen [68) . The option to exchange one risky a et for
another, of which Subsection 9.3. 7 is a special case, was studied by Margrabe

[117).
Theorem 9.4.2, option pricing with a random interest rate, is taken from
Geman, El Karoui, and Rochet [70). It traces back at least to Geman [69) and
Jamshidian [94), who observed that the forward price of an a et is its price
when denominated in the numeraire of the zero-coupon bond maturing at the
delivery date. Even earlier, Merton [122) proposed hedging European options
by using a bond maturing on the option expiration date.


9. 7 Exercises


Exercise 9.1. This exercise provides an alternate proof of the main a ertion
of Theorem 9.2.2.

(i) Use Lemma 5.2.2 to prove Remark 9.2.5.
(ii) Let S(t) and N(t) be prices of two a ets, denominated in a common
currency, and a ume N(t) is always strictly positive. Let JPi be the risk­
neutral measure under which the discounted a et prices D(t)S(t) and


Exercise 9.2 (Portfolios under change of numeraire). Consider two
a ets with prices S(t) and N(t) given by


S(t) = S(O) exp { aW(t) a t,
+ (r- � 2) }

N(t) = N(O) exp vW(t) + (r- �v2) t,
###### }
{

D(t)N(t) are martingales. Apply Remark 9.2.5 to show that S(Nl(t)
###### is a martingale under jpi(N) defined by (9.2.6). =


9. 7 Exercises 399


where W(t) is a one-dimensional Brownian motion under the risk-neutral
measure J and the volatilities u > 0 and v > 0 are constant, as is the interest
rate r. We define a third a et, the money market account, whose price per
share at time t is M(t) [= ] e [rt] .
Let us now denominate prices in terms of the numeraire N, so that the
redenominated first a et price is


vt.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-418-0.png)



is



We define



r( t )



so that (dividing (9.7.2) by N(t)) we have

X(t) [= ] Ll(t)S(t) + F(t) [M] (t).



(9.7.1)


(9.7.2)


(9.7.3)


(9. 7.4)


400 9 Change of N umeraire


(iii) Use stochastic calculus to show that

dX(t) = Ll(t) dS(t) + r(t) d [M] (t).

This equation is the counterpart in the new numeraire of equation (9.7.1)
and says that the change in X (t) is solely due to changes in the prices
of the a ets held by the portfolio. (Hint: Start from equation (9.7.3) and
use (9.7.1) and (9.7.4) along the way.)



Exercise 9.3 (Change in volatility caused by change of numeraire).
Let S(t) and N(t) be the prices of two a ets, denominated in a common cur­
rency, and let u and v denote their volatilities, which we a ume are constant.
We a ume also that the interest rate r is constant. Then



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-419-0.png)







Show that



Exercise 9.4. From the differential formulas (9.3.14) and (9.3.15) for the
stock and discounted exchange rate in terms of the Brownian motions under
the domestic risk-neutral measure, derive the differential formulas (9.3.22) and
(9.3.23) for the redenominated money market account and stock discounted at
the foreign interest rate and written in terms of the Brownian motions under
the foreign risk-neutral measure.


9. 7 Exercises 401


Exercise 9.5 (Quanto option). A quanto option pays off in one currency
the [price in another currency of an underlying a] [et without taking the cur­]
rency conversion into account. For example, a quanto call on a British a et
struck at $25 would pay $5 if the price of the a et upon expiration of the
option is £30. To compute the payoff of the option, the price 30 is treated as
it were dollars, even though it is pounds sterling.
if
In this problem we consider a quanto option in the foreign exchange model
of Section 9.3. We take the domestic and foreign interest rates to be constants

r and rf, respectively, and we a ume that a1 - 0, a2 - 0, and p E ( -1, 1)
are likewise constant.



(i) From (9.3.14), show that





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-420-0.png)


###### )



(i) Show that



where


and









number of units of domestic currency. ) Show that if at time t E [0, T] we
have = x, then the price of the quanto call at this time is



q(t, x) = xe [-ar ] N(d+(T,x)) - e [-rr ] KN(d_(T, x)),


402 9 Change of Numeraire



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-421-0.png)





















(x) Now prove (9.4.16).


On the other hand, if one is given the price of a coupon-paying bond of

.                               - .
each maturity T1, T2,, Tn, then using (10.1.1) one can solve recursively for
B(O, T1), . . ., B(O, Tn) by first observing that B(O, Tt) is the price of the T1maturity bond divided by the payment it will make at Tt, then using this
value of B(O, T1) and the price of the T2-maturity bond to solve for B(O, T2),
and continuing in this manner. This method of determining zero-coupon bond
prices from coupon-paying bond prices is called bootstrapping.
In any event, from market data one can ultimately determine prices of zero­
coupon bonds for a number of different maturity dates. Each of these bonds
has a yield specific to its maturity, where yield is defined to be the constant
continuously compounding interest rate over the lifetime of the bond that is
consistent with its price:

The face value of a zero-coupon bond is the amount it promises to pay upon
maturity. The formula above implies that capital equal to the price of the
=
price of zero-coupon bond face value X e -yield x time to maturity .



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-422-0.png)
404 10 Term-Structure Models


bond, invested at a continuously compounded interest rate equal to the yield,
would, over the lifetime of the bond, result in a final payment of the face
value. In this chapter, we shall normalize zero-coupon bonds by taking the
face value to be 1.
In summary, instead of having a single interest rate, real markets have a
yield curve, which one can regard either as a function of finitely many yields
plotted versus their corresponding maturities or more often as a function of
a nonnegative real variable (time) obtained by interpolation from the finitely
many maturity-yield pairs provided by the market. The interest rate (some­
times called the short mte) is an idealization corresponding to the shortest­
maturity yield or perhaps the overnight rate offered by the government, de­
pending on the particular application.
We a ume throughout this chapter that the bonds have no risk of default.
One generally regards U.S. government bonds to be nondefaultable.
Models for interest rates have already appeared in this text, most notably
in Section 6.5, where the partial differential equation satisfied by zero-coupon
bonds in a one-factor short-rate model was developed and the Hull-White
and Cox-Ingersoll-Ross models were given as examples. In Section 10.2 of this
chapter, we extend these models to permit finitely many factors. These are
Markov models in which the state of the model at each time is a multidimen­
sional vector.
Unlike the models for equities considered heretofore and the Heath-Jarrow­
Morton model considered later, the multifactor models in Section 10.2 do not
immediately provide a mechanism for evolution of the prices of tradeable as­
sets. In the earlier models, we a ume an evolution of the price of a primary
a et or the prices of multiple primary a ets under the actual measure and
then determine the market prices of risk that enable us to switch to a risk­
neutral measure. In the multifactor models of Section 10.2, we begin with the
evolution of abstract "factors," and from these the interest rate is obtained.
But the interest rate is not the price of an a et, and we cannot infer a market
price of risk from the interest rate alone. If we also had prices of some primary
a ets, say zero-coupon bonds, we could determine market prices of risk. How­
ever, in the models of Section 10.2, the only way to get prices of zero-coupon
bonds is to use the risk-neutral pricing formula, and this cannot be done until
we have a risk-neutral measure. Therefore, we build these models under the
risk-neutral measure from the outset. Zero-coupon bond prices are given by
the risk-neutral pricing formula, which implies that discounted zero-coupon
bond prices are martingales under the risk-neutral measure. This implies in
turn that no arbitrage can be achieved by trading in the zero-coupon bonds
and the money market. After these models are built, they are calibrated to
market prices for zero-coupon bonds and probably also some fixed income
derivatives. The actual probability measure and the market prices of risk
never enter the picture.
In contrast to the models of Section 10.2, the Heath-Jarrow-Morton (HJM)
model takes its state at each time to be the forward curve at that time. The


10.2 Affine-Yield Models 405


forward rate f(t, T), which is the state of the HJM model, is the instantaneous
rate that can be locked in at time t for borrowing at time T � t. For fixed t,
one calls the function T t-+ f(t, T), defined for T � t, the forward rate curve.
The HJM model provides a mechanism for evolving this curve (a "curve" in
the variable T) forward in time (the variable t). The forward rate curve can be
deduced from the zero-coupon bond prices, and the zero-coupon bond prices
can be deduced from the forward rate curve. Because zero-coupon bond prices
are given directly by the HJM model rather than indirectly by the risk-neutral
pricing formula, one needs to be careful that the model does not generate
prices that admit arbitrage. Hence, HJM is more than a model because it
provides a necessary and sufficient condition for a model driven by Brownian
motion to be free of arbitrage. Every Brownian-motion-driven model must
satisfy the HJM no-arbitrage condition, and to illustrate that point we provide
Exercise 10.10 to verify that the Hull-White and Cox-Ingersoll-Ross models
satisfy this condition.
For practical applications, it would be convenient to build a model where
the forward rate had a log-normal distribution. Unfortunately, this is not pos­
sible. However, if one instead models the simple interest rate L(t, T) that one
can lock in at time t for borrowing over the interval T to T +8, where 8 is a pos­
itive constant, this problem can be overcome. We call L(t, T) forward LIBOR
(London interbank offered rate). The constant 8 is typically 0.25 (thr -month
LIBOR) or 0.50 (six-month LIBOR). The model that takes forward LIBOR
as its state is often called the forward LIBOR model, the market model, or the
Brace-Gatarek-Musiela (BGM) model. It is presented in Section 10.4.


10.2 Affine-Yield Models


The one-factor Cox-Ingersoll-Ross (CIR) and Hull-White models appearing
in Section 6.5 are called affine-yield models because in these models the yield
for zero-coupon bond prices is an affine (linear plus constant) function of the
interest rate. In this section, we develop the two-factor, constant-coefficient
versions of these models. (The constant-coefficient version of the Hull-White
model is the Vasicek model.) Models with three or more factors can be devel­
oped along the lines of the two-factor models of this section.
It turns out that there are essentially three different two-factor affine-yield
models, one in which both factors have constant diffusion terms (and hence
are Gaussian processes, taking negative values with positive probability), one
in which both factors appear under the square root in diffusion terms (and
hence must be nonnegative at all times), and one in which only one factor
appears under the square root in the diffusion terms (and only this factor is
nonnegative at all times, whereas the other factor can become negative). We
shall call these the two-factor Vasicek, the two-factor CIR, and the two-factor
mixed term-structure models, respectively. For each of these types of models,
there is a canonical model (i.e., a simplest way of writing the model).


406 10 Term-Structure Models


Two-factor ane yield-models appearing in the literature, which often
seem to be more complicated than the canonical models of this section, can
always be obtained from one of the three canonical models by changing vari­
ables. It is desirable when calibrating a model to first change the variables
to put the model into a form having the minimum number of parameters;
otherwise, the calibration can be confounded by the fact that multiple sets of
parameters yield the same result. The canonical models presented here have
the minimmu number of parameters.


10.2.1 Two-Factor Vasicek Model

For the two-factor Vasicek model, we let the factors X1(t) and X2(t) be given
by the system of stochastic differential equations
dX1(t) (a1 - bnX1(t) - b12X2(t)) dt 171 dB1(t), (10.2.1)
= +
dX1 (t) (a2 - b21X1 (t) - b22X2(t)) dt 172 dB2(t), (10.2.2)
= +

where the processes B1(t) and B2(t) are Brownian motions under a risk­
neutral measure lP with constant correlation v E ( -1, 1) (i.e., dB1 (t) dB2(t) =
vdt). The constants 171 and 172 are a umed to be strictly positive. We further
a ume that the matrix
B
= [��� ���]

has strictly positive eigenvalues ..\1 and ..\2. The positivity of these eigenvalues
causes the factors X1(t) and X2(t), as well as the canonical factors Y1(t) and
Y2(t) defined below, to be mean-reverting. Finally, we a ume the interest rate
is an affine function of the factors,

(10.2.3)


model.


Canonical Form



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-425-0.png)

R(t) 8 81Y1(t) 82Y2(t),
=          - + +

where W1 ( t) and W2 ( t) are independent Brownian motions.



(10.2.4)
(10.2.5)
(10.2.6)


10.2 Affine-Yield Models 407


The canonical two-factor Vasicek model has six parameters:
A1           - 0, A2 > 0, A21 8o, 8�, 82.



The parameters are used to calibrate the model. In practice, one often permits
some of these parameters to be time-varying but nonrandom in order to make
the model fit the initial yield curve; see Exercise 10.3.
To achieve this reduction, we first transform B to its Jordan canonical
form by choosing a nonsingular matrix



Pu P12
p =
###### [P21 P22 ]



such that



K = PBP [-1 ] =
###### [� �J.



If A1 =f. A2, then the columns of p- [1 ] are eigenvectors of B and K = 0 (i.e., K
is diagonal). If A1 = A2, then K might be zero, but it can also happen that



K =f. 0, in which case we may choose P so that K = 1. Using the notation



X2(t) [' ] a2 ' 0 u2 [' ] B2(t) [' ]
X1(t) a1 0 1(t)
X(t) = A = E = B(t) = ### [ ] [ ] [u1 ] [ ]



we may rewrite (10.2.1) and (10.2.2) in vector notation:



dX(t) = A dt - BX(t) dt + E dB(t).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-426-0.png)



(10.2.7)


(10.2.8)







(10.2.10)


408 10 Term-Structure Models


PROOF: Because E - 1, the matrix
###### v ( 1),



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-427-0.png)















motions. Furthermore,


10.2 Affine-Yield Models 409



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-428-0.png)














410 10 Term-Structure Models

We may thus rewrite (10.2.13) and (10.2.14) as



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-429-0.png)
10.2 Affine-Yield Models 411


We solve (10.2.15) for X(t):

X(t) = p [-1 ] (r [-1] Y(t) - V).

Therefore,



R(t) = Eo + h E2)X(t)
= Eo + [E1 E2)P- [1 ] r- [1] Y(t) - [E1 f2)P- [1] V
= 8o + [81 82]Y(t),



where

8o = fo h f2)P [-1 ] v, [81 82) = [€1 f2)P [-1 ] r [-1] .
###### We have obtained (10.2.6).



where



Bond Prices



We derive the formula for zero-coupon bond prices in the canonical two-factor
Vasicek model. According to the risk-neutral pricing formula, the price at time
t of a zero-coupon bond paying 1 at a later time T is



B(t, T) = E [ e [-] It [R] ( [u)du] F(t)], 0 ::; t ::; T.
l



Because R(t) given by (10.2.6) is a function of the factors Y1(t) and Y2(t),
the solution of the system of stochastic differential equations (10.2.4) and
and
{10.2.5) is Markov, there must be some function f(t, YI. Y2) such that

B(t, T) = f(t, Y1(t), Y2(t)). (10.2.16)

The discount factor D(t) = e [-][ f� ] R [(u)du ] satisfies dD(t) -R(t)D(t) dt
(see (5.2.18)). Iterated conditioning implies that the discounted bond price
D(t)B(t, T) is a martingale under JP. Therefore, the differential of D(t)B(t, T)
has dt term zero. We compute this differential:



d(D(t)B(t, T))



=

=
d D(t)f(t, Y1(t), Y2(t))
( )



=
-R(t)D(t)f(t, Y1(t), Y2(t)) dt + D(t) df(t, Y1(t), Y2(t))
= D Rf dt + ft dt + /y1 dY1 + /y2 dY2
###### [

###### 1 1 ]

+2Jy1y1 dY1 dY1 + /y1y2 dY1 dY2 + 2/y2y2 dY2 dY2 .



(10.2.17)



We use equations (10.2.4)-(10.2.6) to take the next step:


412 10 Term-Structure Models



d (D(t)B(t, T))



(D(t)B(t, T))


1 1              -              ###### ]

[ ]
= D (8o 81Y1 82Y2)f ft - >1Ydy, - >21Ydy2
###### [- + + +

->2Y2/y2 2/y1y1 2/y2y2 dt D /y, dW1 /y2 dW2 .
###### + + + +



Setting the dt term equal to zero, we obtain the partial differential equation



-(8o 81Y1 82y2)J(t, Y1> Y2) ft(t, Y1, Y2)
###### ->+ 1Ydy, (t, Y1, Y2) - A21YdY2 (t, Yb Y2) - A2Y2/y2 (t, Y1, Y2) + +

1 1 =
/y, Y> (t, Yb Y2) 2/y2y2 (t, Yb Y2) 0 (10.2.18)
###### +2 +



for all t E [0, T) and all Y1 E IR, Y2 E lR. We have also the terminal condition



(10.2.19)


(10.2.20)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-431-0.png)

for some functions C1(r), C2(r), and A(r). Here we define T = T - t to be
the relative maturity (i.e., the time until maturity). So long as the model
parameters do not depend on t, zero-coupon bond prices will depend on t and
T only through T. The terminal condition (10.2.19) implies that



C1 (0) = C2(0) = = 0. (10.2.21)
###### A(O)



We compute derivatives, where ' denotes differentiation with respect to T. We
use the fact ftCi(r) = C:(r) · ftr = -C:(r), i = 1, 2, and the similar equation
ftA(r) = - '(r) to obtain
###### A



ft = [y1 C� y2C� A']J, /y, = -Cd, fY2 = -C2/,
###### �� [=] �h + + �n [=] ��h �n [=] �f

Equation (10.2.18) becomes

>1C1 >21 [C] 2 [- 8] I [)y] l         - >2 [C] 2 [- 8] 2 [)] Y2
###### [(c� + + + [(C] +

                           - 8o f [= ] (10.2 [.22) ]
J o.
###### + (A'+ �c; + �ci )



Because (10.2.22) must hold for all Y1 and Y2, the term C� >C1 >21 C2 ###### 81 multiplying y1 must be zero. If it were not, and (10.2.22) held for one + +
value of y1, then a change in the value of y1 would cause the equation to be
violated. Similarly, the term C2 + >2C2 - 82 multiplying Y2 must be zero, and
consequently the remaining term A' + !Cr + !C�-80 must also be zero. This
gives us a system of three ordinary differential equations:


10.2 Affine-Yield Models 413



C�(r) -AICI(r) - A2IC2(r)
= + (h,
C�(r) = -A2C2(r) + 82,

1 2 2
A I (r) = - 2CI (r) - 2C2 (r) 1 + Oo.



(10.2.23)
(10.2.24)

(10.2.25)



The solution of (10.2.24) satisfying the initial condition C2(0) = 0 (see



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-432-0.png)



















and this can be obtained in closed form by a lengthy but straightforward
computation.


Short Rate and Long Rate

We fix a positive relative maturity 'f (say, thirty years) and call the yield
at time t on the zero-coupon bond with relative maturity 'f (i.e., the bond
maturing at date t +'f) the long rate L(t). Once we have a model for evolution
of the short rate R(t) under the risk-neutral measure, then for each t 0 the
;
price of the (t + 'f)-maturity zero-coupon bond is determined by the risk­
neutral pricing formula, and hence the short-rate model alone determines the
long rate. We cannot therefore write down an arbitrary stochastic differential
equation for the long rate. Nonetheless, in any affine-yield model, the long


414 10 Term-Structure Models


rate satisfies some stochastic differential equation, and we can work out this
equation.
Consider the canonical two-factor Vasicek model. As we have seen in the
previous discussion, zero-coupon bond prices in this model are of the form


where 1 (r), 2(r), and A(r) are given by (10.2.26)-(10.2.29). Thus, the long
C C
rate at time t is

=
B(t, T) e-Y.(t}C,(T-t)-Y2(t)C2(T-t)-A(T-t),



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-433-0.png)
















10.2 Affine-Yield Models 415



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-434-0.png)
416 10 Term-Structure Models



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-435-0.png)







where


10.2 Affine-Yield Models 417


(10.2.35)


(10.2.36)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-436-0.png)



(10.2.37)










418 10 Term-Structure Models

which is (10.2.39) with n replaced by n + 1. Having thus established (10.2.39)
for all values of n, we have



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-437-0.png)

















t


10.2 Affine-Yield Models 419


0



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-438-0.png)





(10.2.42)






















420 10 Term-Structure Models


Being nonrandom quantities plus Ito integrals of nonrandom integrands, the
processes Y1 (t) and Y2(t) are Gaussian, and so R(t) = 8o + 81 Y1(t) +82Y2(t) is
normally distributed. The statistics of Y1 (t) and Y2(t) are provided in Exercise
10.1.


10.2.2 Two-Factor CIR Model


In the two-factor Vasicek model, the canonical factors Y1(t) and Y2(t) are
jointly normally distributed. Because these factors are driven by independent
Brownian motions, they are not perfectly correlated and hence, for all t > 0,

(10.2.47)


(10.2.48)


(10.2.51)


a umed to be independent. We do not need this a umption to guarantee
nonnegativity of Y1(t) and Y2(t) but rather to obtain the affine-yield result
below; see Remark 10.2.4.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-439-0.png)
10.2 Affine-Yield Models 421


Bond Prices


We derive the formula for zero-coupon bond prices in the canonical two-factor
CIR model. As in the two-factor Vasicek model, the price at time t of a zero­
coupon bond maturing at a later time T must be of the form

B(t, T) [= ] f(t, Y1(t), Y2(t))

for some function f(t, y�, Y2)· The discounted bond price has differential



d(D(t)B(t,T [)) ]



=

=
d D(t)f(t, Y1(t), Y2(t))
( )



=
-R(t)D(t)f(t, Y1(t), Y2(t)) dt + D(t) df(t, Y1(t), Y2(t))



=
D - Rf dt + ft dt + jy1 dY1 + fy2 dY2

[ 1 1
+2fy1y1 dY1 dY1 + fy1y2 dY1 dY2 + 2fy2y2 dY2 dY2 ]



1 1
###### ]
=
D (8o + 81Y1 + 82Y2)f + ft + (J-LI - .AuY1 - .A12Y2)fy1
###### [
+(J-L2 - A2lyl - A22Y2)!Y2 + 2YdY1Y1 + 2Y2fY2Y2 dt





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-440-0.png)


(10.2.53)


=
for some functions C1(r), C2(r), and A(r), where T T - t. The terminal
condition

= =
f(T, Y1(T), Y2(T)) B(T, T) 1
implies

=
C1 (0) [= ] C2(0) [= ] A(O) 0. (10.2.54)

=
With ' denoting differentiation with respect to T, we have ftCi(r) -C:(r),

=
=
i 1, 2, ftA(r) -A'(r), and (10.2.52) becomes

=


422 10 Term-Structure Models

[ ( o� + .Xu01 + .X2102 + 81) Y1
###### �o�1
I
###### ( 2 )

f [= ] (10.2.55)
+(A'-J.L101 -J.L202-8o)] o.

Because (10.2.55) must hold for all 0 and 0, the term
Y1 ; Y2 ; 0� +An 01 +
multiplying must be zero. Similarly, the term
..\21 02+ to� -81 y1 0�+..\1201 +
multiplying must be zero, and consequently the remaining
.X2202 + 20i-82 Y2
term must also be zero. This gives us a system of three
A'-J.L1 02 -J.L202 -8o
ordinary differential equations:


(10.2.56)

0�(7) [= ] -.XnOI(7)-.X2102(7)- �0�(7) + 81,

(10.2.57)
(10.2.58)

+ 02 + .x1201 + .x2202 + 2o2 -82 Y2



(10.2.56)


(10.2.57)
(10.2.58)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-441-0.png)



10.2.3 Mixed Model



become negative.


(10.2.59)


=

(10.2.60)


motions and are independent. We a ume ; 0, and w [e ]
W1(t) W2(t) Y1(0)
have ; 0 for all t 0 almost surely. On the other hand, even if
Y1 ( t) ; Y2 ( t) [is ]



(10.2.59)



(10.2.60)


10.3 Heath-Jarrow-Morton Model 423


positive, Y2(t) can take negative values for t > 0. The interest rate is defined
by
R(t) [= ] 8o + 81Y1(t) + 82Y2(t). (10.2.61)
In this model, zero-coupon bond prices have the ane-yield form



=
B(t, T) e [-][Yl(t)Ct (T-t)-Y2(t)C2(T-t)-A(T-t)] .



(10.2.62)



Just as in the two-factor Vasicek model and the two-factor CIR model, the
functions C1(T), C2(T), and A(T) must satisfy the terminal condition

(10.2.63)


model.


10.3.1 Forward Rates


violate it.


B(t, T).


B(t, T).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-442-0.png)
424 10 Term-Structure Models


The net cost of setting up this portfolio at time t is zero. At the later time
T, holding this portfolio requires that we pay to cover the short position in
1
the T-maturity bond. At the still later time T + 8, we receive from
the long position in the T+8-maturity bond. In other words, we have invested
at time T and received more than at time T + 8. The yield that explains
1 1
the surplus received at time T + 8 is


1
)

1
( )



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-443-0.png)



time t.





(10.3.3)


From bond prices, we can determine forward rates from From
(10.3.2).
forward rates, we can determine bond prices from Therefore, at least
(10.3.3).
theoretically, it does not appear to matter whether we build a model for
forward rates or for bond prices. In fact, the no-arbitrage condition works out


10.3 Heath-Jarrow-Morton Model 425



to have a simple form when we model forward rates. From a practical point
of view, forward rates are a more difficult object to determine from market
data because the differentiation in (10.3.2) is sensitive to small changes in the
bond prices. On the other hand, once we have forward rates, bond prices are
easy to determine because the integration in (10.3.3) is not sensitive to small
changes in the forward rates.
The interest rate at time t is
R(t) f(t, t). (10.3.4)

This is the instantaneous rate we can lock in at time t for borrowing at time
### =


10.3.2 Dynamics of Forward Rates and Bond Prices

Assume that /(0, T), 0 � T � is known at time 0. We call this the initial
T,
forward rate curve. In the HJM model, the forward rate at later times t for
investing at still later times T is given by

t.



f(t, T) f(O, T) + 1 [t ] a(u, T) du + 1 [t ] a(u, T) dW(u). (10.3.5)
### =



We may write this in differential form as
df(t, T) a(t, T) dt + a(t, T) dW(t), 0 � t � T. ( 10.3.6)

Here and elsewhere in this section, d indicates the differential with respect to
### =



Here and elsewhere in this section, d indicates the differential with respect to
the variable t; the variable T is being held constant in ( 10.3.6) .
Here the process W(u) is a Brownian motion under the actual measure
JP. In particular, o(t, T) is the drift of f(t, T) under the actual measure. The
processes o(t, T) and a(t, T) may be random. For each fixed T, they are
adapted processes in the t variable. To simplify the notation, we a ume that
the forward rate is driven by a single Brownian motion. The case when the
forward rate is driven by multiple Brownian motions is a ressed in Exercise
10.9.
From ( 10.3.6), we can work out the dynamics of the bond prices given by
(10.3.3). Note first that because - Jt f(t, v) dv has a t-variable in two places,
its differential has two terms. Indeed,



d - f(t, v) dv f(t, t) dt - df(t, v) dv.
### ( [T ) = [T



The first term on the right-hand side is the result of taking the differential
with respect to the lower limit of integration t. The fact that this is the lower
limit produces a minus sign, which cancels the minus sign on the left-hand
side. The other term is the result of taking the differential with respect to the
t under the integral sign. Using (10.3.4) and ( 10.3.6), we see that


426 10 Term-Structure Models
d f(t, v) dv = R(t) dt- [a(t, v) dt + a(t, v) dW(t)] dv.
### ( -1T ) [T



We next reverse the order of the integration (see Exercise 10.8), writing

(10.3.7)
a(t,v)dtdv = a(t,v)dvdt = a*(t,T)dt,
### 1T 1T

(10.3.8)
a(t, v) dW(t) dv = a(t, v) dv dW(t) = a*(t, T) dW(t),
### where [T 1T



where
at(t, T) = a(t, v) dv, a*(t, T) = a(t, v) dv.
### In conclusion, we have 1T 1T



(10.3.9)



In conclusion, we have



(10.3.10)
d f(t, v) dv = R(t) dt-a*(t, T) dt-a*(t, T) dW(t).
### (-[T )



Let so that and According to (10.3.3,
g(x) =ex, g'(x) =ex g"(x) =ex. )
B(t,T) =g f(t,v)dv .
### ( -1T )



The ltO-Doeblin formula implies
dB(t,T) =g' f(t,v)dv d f(t,v)dv
### ( -1T ) ( -1T )
+�g"        - f(t,v)dv f(t,v)d•
### ( [ ) [[] { [ )] [' ]

= B(t, T) [R(t) dt-a*(t, T) dt-a*(t, T) dW(t)]



= B(t, T) [R(t) dt-a*(t, T) dt-a*(t, T) dW(t)]
+�B(t, T)(a*(t, T) ) [2 ] dt
=B(t,T) [R(t) -a*(t,T)+�(a*(t,T)) [2] ] dt
-a*(t, T)B(t, T) dW(t). (10.3.11)



10.3.3 No-Arbitrage Condition


The HJM model has a zero-coupon bond with maturity for every E [0,
T T T].
We need to make sure there is no opportunity for arbitrage by trading in these
bonds. The First Fundamental Theorem of Asset Pricing, Theorem 5.4.7, says


10.3 Heath-Jarrow-Morton Model 427



that, in order to guarantee this, we should seek a probability measure lP under
which each discounted bond price



D(t)B(t, T) [= ] exp R(u) du B(t, T), 0 : t : T,
{ -1 [t ]
###### }



=
is a martingale. Because dD(t) -R(t)D(t) dt, we have the differential



d(D(t)B(t, T))



=
-R(t)D(t)B(t, T) dt + D(t) dB(t, T)



=
-R(t)D(t)B(t, T) dt + D(t) dB(t, T)

= D(t)B(t, T) -a*(t, T) + (a*(t, T)) [2] dt - a*(t, T) dW(t) . (10.3.12)
###### [ ( � ) ]



We want to write the term in square brackets as



-a*(t, T)[6l(t) dt + dW(t)],

and we can then us� Girsanov's Theorem, Theorem 5.2.3, to change to a
probability measure lP' under which

W(t) [= ] 6l(u) du + W(t) (10.3.13)
1 [t ]

is a Brownian motion. Using this Brownian motion, we may rewrite (10.3.12)

as
d(D(t)B(t, T)) [= ] -D(t)B(t, T)a*(t, T) dW(t). (10.3.14)

It would then follow that D(t)B(t, T) is a martingale under lP (i.e., lP would
be risk-neutral).
For the program above to work, we must solve the equation
-a*(t, T) + (a*(t, T)) [2] dt - a*(t, T) dW(t)
###### [ ( ) ]

           - =

-a*(t, T) [6l(t) dt + dW(t)]

for 6l(t). In other words, we must find a process 6l(t) satisfying



-a*(t, T) + (a*(t, T)) [2 ]

     


=
-a*(t, T)6l(t). (10.3.15)



Actually, (10.3.15) represents infinitely many equations, one for each maturity
T E (0, These are the market price of risk equations, and we have one such
TJ.
equation for each bond (maturity). However, there is only one process 6l(t).
This process is the market price of risk, and we have as many such processes

as there are sources of uncertainty. In this case, there is only one Brownian
motion driving the model.
To solve (10.3.15), we reca from (10.3.9) that


428 10 Term-Structure Models


v :



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-447-0.png)



0


(10.3.17)



This shows that 8(t) is unique, and hence the risk-neutral measure is unique.
In this case, the Second FUndamental Theorem of Asset Pricing, Theorem
5.4.9, guarantees that the model is complete (i.e., all interest rate derivatives
can be hedged by trading in zero-coupon bonds).


10.3 Heath-Jarrow-Morton Model 429


10.3.4 HJM Under Risk-Neutral Measure

We began with the formula (10.3.5) for the evolution of the forward rate, and
the driving process W(u) appearing in (10.3.5) is a Brownian motion under
the actual measure IP. Assuming the model satisfies the HJM no-arbitrage
condition (10.3.16), we may rewrite (10.3.5) as
df(t, T) = a(t, T) dt + u(t, T) dW(t)



= a(t, T) dt + u(t, T) dW(t)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-448-1.png)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-448-0.png)






                          




Jt
bond prices satisfy


430 10 Term-Structure Models
where D(t) = e [-] is the discount process. The solution to the stochas­
f� [R(u)du ]
tic differential equation ( 10.3.19) is
B(t, T)



t t T
= B(O, T) exp lo R(u)du - lo u*(u, T) dW(u) - �lo (u*(u, T))2 du
### { t T }



t T
### { }



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-449-0.png)

dR(t) = f3(t, R(t)) dt + 'Y (t, R(t)) dW(t),


J. In the case of the Hull-White model,



{J(t, r) = a(t) - b(t)r, 'Y(t, r) [= ] u(t),



for some nonrandom positive functions a(t), b(t), and u(t). For the CIR model,



{J(t, r) = a - br, 'Y(t, r) = u.Ji, (10.3.22)



for some positive constants b, and The zero-coupon bond prices are of
a, u.
the form
(10.3.23)
where C(t, T) and A(t, T) are nonrandom functions. In the case of the Hull­
White model, C(t, T) and A(t, T) are given by (6.5.10) and (6.5.11), which
we repeat here:
B(t, T) = e-R(t)C(t,T)-A(t,T),



C(t, T) = e [-][ J," ][b(v)dv ] ds,
i [T ]

A(t, T) = i [T ] a(s)C(s, T) - �u2(s)C2(s, T) ds.
( )



(10.3.24)


(10.3.25)


10.3 Heath-Jarrow-Morton Model 431


In the case of the CIR model, and t are given by (6.5.16) and
C(t, T) A(, T)
(6.5.17). According to (10.3.2), the forward rates are



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-450-0.png)







reduce to



and hence




432 10 Term-Structure Models



Therefore,

and
a(t, T) = ae-b(T-t),



a*(t, T) = l [T ] a(t, u) du = a l [T ] e [-b(] T [-u) ] du = [� ] ( 1 - [e-b(T-t)] ) .



It follows that
!c(t, T)/3(t, R(t)) + R(t) T) + !A'(t, T)



= e-b(T-t)(a - bR(t)) + R(t)be-b(T-t) + - a e-b(T-t)
( )



(}"2



_
-e-2b(t-t)
b

= a(t, T)a*(t, T),
_
= e-b(T-t) e-2b(T-t)
( )



as expected.


10.3.6 Implementation of HJM

To implement an HJM model, we need to know a(t, T) for 0 � t � T � T.
We can use historical data to estimate this because the same diffusion process
a(t, T) appears in both the stochastic differential equation (10.3.6) driven by
the Brownian motion W(t) under the actual probability measure lP' and in
the stochastic differential equation (10.3.18) driven by the Brownian motion
W(t) under the risk-neutral measure [JP] . Once we have a(t, T), we can compute
a*(t, T) = Jt a(t, v) dv. This plus the initial forward curve f(O, T), 0 � T �
T, permits us to determine all the terms appearing in the formulas in Theorem
10.3.2. In particular, we use the initial forward curve to compute


R(t) = f(t, t) = f(O, t) + a(u, t)a*(u, t) du + a(u, t) dW(u). (10.3.28)
lo [t ] lo [t ]

Since all expectations required for pricing interest rate derivatives are com­
puted under [JP], we need only the formulas in Theorem 10.3.2; the market
price of risk 8(t) and the drift of the forward rate o:(t, T) in (10.3.6) are irrel­
evant to derivative pricing. They are relevant, however, if we want to estimate
nondiffusion terms from historical data (e.g., the probability of credit class
migration for defaultable bonds) or we want to compute a quantity such as
Value-at-Risk that requires use of the actual measure.
Assume for the moment that a(t, T) is of the form
a(t, T) = a(T - t) min{M, f(t, T)} (10.3.29)


10.3 Heath-Jarrow-Morton Model 433



for some nonrandom function 0:(7), 7 � 0, and some positive constant M. In
(10.3.29), we need to have the capped forward rate min{M, f(t, T)} on the
right-hand side rather than the forward rate f(t, T) itself to prevent explosion
of the forward rate. This is discussed in more detail in Subsection 10.4.1.
One consequence of this fact is that forward rates (recall we are working
here with continuously compounding forward rates; see (10.3.2)) cannot be
log-normal. This is a statement about forward rates, not about the HJM
model. Section 10.4 discusses how to overcome this feature of continuously
compounding forward rates by building a model for simple forward rates.
We choose a(T - t) to match historical data. The forward rate evolves
according to the continuous-time model
df(t, T) = a(t, T) dt + a(T - t) min{ M, f(t, T)} dW(t).

Suppose we have observed this forward rate at times t1 < t2 < - · · < tJ < 0
in the past, and the forward rate we observed at those times was for the
relative maturities 71 < 72 < - · · < 7K (i.e., we have observed f(ti, ti +7k) for
j = 1, . . ., J and k = 1, . . ., K). Suppose further that for some small positive
8 we have also observed f(tj + 8, ti + 7k)· We a ume that 8 is sufficiently
small that ti + 8 < ti+l for j = 1, . . ., J - 1 and tJ + 8 ::; 0. According to our
model,
/(tj + 8, tj + 7k) - f(tj, tj + 7k)

  - [8a(t] j [, t] j [+ ] 7k [) + a(] 7k [) ][min][{][M, ][f(t] j [, t] j [+ 7k)}(W(tj + 8) - W(tj)). ]



We identify by defining
a





(10.3.30)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-452-0.png)









(10.3.32)

Observe that not only are X1, . . ., XJ standard normal random variables
but are also independent of one another. The approximation (10.3.32) per­
mits us to regard Dlk, D2k, . . ., DJk as independent observations taken at




434 10 Term-Structure Models

times t1. t2, . . . tJ on forward rates, all with the same relative maturity Tk. We
compute the empirical covariance


(10.3.33)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-453-0.png)




has






10.4 Forward LIBOR Model 435


However, this cannot be done exactly. The best approximation is


To get a better approximation to C, we can introduce more Brownian
motions into the equation driving the forward rates (see Exercise 10.9). Each
of these has its own a vector, and these can be chosen to be VJ;2 e2, .fJ\3 eg,
etc.
So far we have used only historical data. In the final step of the calibration,
we introduce a nonrandom function s(t) into the forward rate evolution under
the risk-neutral measure, writing
df(t, T) = u(t, T)u'*(t, T) dt + s(t)a(T - t) min{M, f(t, T)} dW(t). (10.3.34)

This is our final model. We use the values ofa(T-t) estimated from historical
data under the a umption s(t) 1. We then a ow the possibility that s(t) is
=
different from 1. We have u(t, T) = s(t)a(T - t) min{M, f(t, T)}. Therefore,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-454-0.png)

u*(t, T) = u(t, v) dv = s(t) a(v - t) min{M, f(t, v)} dv. (10.3.35)
### 1T 1T 10.3.34 and evolve the forward rate. Even



We substitute this function into (10.3.34) and evolve the forward rate. Even
with this last-minute introduction of s(t) into the model, the model is free
of arbitrage when u*(t, T) in (10.3.34) is defined by (10.3.35). Typically, one
a umes that s(t) is piecewise constant, and the values of these constants are
free parameters that can be used to get the model to agree with market prices.
Recalibrations of the model affect s(t) only.



10.4 Forward LIBOR Model


In this section, we present the forward LIBOR model, which leads to the Black
caplet formula. This requires us to build a model for LIBOR (London inter­
bank offered rate) and use the forward measures introduced in Section 9.4.
We begin by explaining why the continuously compounding forward rates of
Section 10.3 are inadequate for the purposes of this section.


10.4.1 The Problem with Forward Rates


We have seen in Theorem 10.3.2 that in an arbitrage-free term-structure
model, forward rates must evolve according to (10.3.18),

df(t, T) = u(t, T)u*(t, T) dt + u(t, T) dW(t), (10.3.18)


436 10 Term-Structure Models



where W is a Brownian motion under a risk-neutral measure JPi. In order to
adapt the Black-Scholes formula for equity options to fixed income markets,
and thereby obtain the Black caplet formula (see Theorem 10.4.2 below), it
would be desirable to build a model in which forward rates are log-normal
under a risk-neutral measure. To do that, we should set a( t, T) = a f ( t, T) in
(10.3.18), where a is a positive constant. However, we would then have



a*(T, t) = a(t, v) dv = a f(t,v) dv,
### lT lT



and the dt term in (10.3.18) would be



a [2 ] f(t, T) f(t, v) dv. (10.4.1)
### lT



Heath, Jarrow, and Morton [83) show that this drift term causes forward
rates to explode. For T near t, the dt term (10.4.1) is approximately equal
to a [2] (T - t)j [2] (t, T), and the square of the forward rate creates the problem.
With the drift term (10.4.1), equation (10.3.18) is similar to the deterministic
ordinary differential equation



(10.4.2)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-455-0.png)
10.4 Forward LIBOR Model 437

of 1 at time T to cover the short position, and it "repays" at time
T + 8. The continuously compounding interest rate that would explain this
repayment on the investment of 1 over the time interval [T, T + 8] is given by
(10.3.1). In this section, we study the simple interest rate that would explain
this repayment, and this interest rate L(t, T) is determined by the equation



investment x (1 + duration of investment x interest rate = repayment,
)



or in symbols:



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-456-0.png)



(10.4.3)


(10.4.4)



When 0 � t < T, we call L(t, T) forward LIBOR. When t = T, we call it spot
LIBOR, or simply LIBOR, set at time T. The positive number 8 is called the
tenor of the LIBOR, and it is usually either 0.25 years or 0.50 years.



10.4.3 Pricing a Backset LIBOR Contract

An interest rate swap is an agreement between two parties A and B that A
will make fixed interest rate payments on some "notional amount" to B at
regularly spaced dates and B will make variable interest rate payments on the
same notional amount on these same dates. The variable rate is often backset
LIBOR, defined on one payment date to be the LIBOR set on the previous
payment date. The no-arbitrage price of a payment of backset LIBOR on a
notional amount of 1 is given by the following theorem.

Theorem 10.4.1 (Price of backset LIBOR) . Let 0 � t � T and 8 > 0
be given. The no-arbitrage price at time t of a contract that pays L(T, T) at
time T + 8 is

(10.4.5)

PROOF: There are two cases to consider. In the first case, T � t � T + 8,
LIBOR has been set at L(T, T) and is known at time t. The value at time t
of a contract that pays 1 at time T + 8 is B(t, T + 8), so the value at time t
of a contract that pays L(T, T) at time T + 8 is B(t, T + 8)L(T, T).
In the second case, 0 � t � T, we note from (10.4.4) that
1
B(t, T + 8)L(t, T) = [B(t, T) - B(t, T + 8)].
J

We must show that the right-hand side is the value at time t of the backset
LIBOR contract. To do this, suppose at time t we have � [B(t, T)-B(t, T+8)],
and we use this capital to set up a portfolio that is:

B(t, T + 8)L(T, T), T � t � T + 8.
B(t, T + 8)L(t, T), 0 � t � T,
S(t) =
{


438 10 Term-Structure Models

 - long short � bonds maturing at T;




 - short ! bonds maturing at T + o.
!
in (T + o)-maturity bonds. At time T + o, this portfolio pays


L(T, T).


T + o.

                                   

(10.4.6)


Recalling Definition 5.6.1 and Theorem 5.6.2, at least for 0 � t � T, we see
that forward LIBOR L(t, T) is the (T+o)-forward price of the contract paying
backset LIBOR L(T, T) at time T + o.
If we build a term-structure model driven by a single Brownian motion un­
der the actual probability measure and satisfying the Heath-Jarrow-Morton
JP>



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-457-0.png)

=
L(T, T).



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-457-1.png)
10.4 Forward LIBOR Model 439



no-arbitrage condition of Theorem 10.3.1, then there is a Brownian motion
W(t) under a risk-neutral probability measure lP such that forward rates are
given by (10.3.18) and bond prices by (10.3.19). Theorem 9.2.2 implies that
the risk-neutral measure corresponding to numeraire B(t, T + 8) is given by



and





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-458-0.png)

(10.4.8)



where


### l



(10.4.10)


(10.4.11)



PROOF: According to the risk-neutral pricing formula, the price of the caplet
at time zero is the discounted risk-neutral (under P) expected value of the
payoff, which is


440 10 Term-Structure Models



E n(T + 8) (L(T, T) - K) [+]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-459-0.png)







and
+





can rewrite as



D(t)B(t, T)



D(t)B(t, T + 8)




10.4 Forward LIBOR Model 441



This implies
1
L(t, T) + 8



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-460-1.png)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-460-0.png)




Therefore,
dL(t, T) = 1 (1 + 8L(t, T)) [a*(t, T + 8) - a*(t, T)]dW -T [+ ]  - (t). (10.4.14)
8

Comparing this with (10.4.9), we conclude that the forward LIBOR volatil­
ity 7(t, T) of (10.4.9) and the (T + 8)- and T-maturity zero-coupon bond
volatilities a* ( t, T + 8) and a* ( t, T) are related by the formula


442 10 Term-Structure Models



(10.4.15)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-461-0.png)















of j. Before we use (10.4.9) to evolve forward LIBORs, we must determine
the relationship among these different equations.


10.4 Forward LIBOR Model 443


Construction of Forward LIBOR Processes


Observe from (10.4.8) that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-462-0.png)









0 � t � Tj, j = 1, 10.4.19
. . ., n. ( )



Now we have a single Brownian motion driving all n equations. Thus, to
construct the forward LIBOR model, we choose a Brownian motion, which


444 10 Term-Structure Models

we call W [Tn+t ] (t), 0 � t � Tn+I. under a probability measure we call [jj][Tn+t ] .


Tj-1 � t <

(10.4.20)


formula in (10.3.9).


determined.)


and since u [*] (t, T2) has been determined for 0 � t < T2, the function u(t, T3)
is determined by this equation for 0 � t < T2. For T2 � t < T3, u(t, T3)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-463-0.png)
10.4 Forward LIBOR Model 445

has already been chosen. Therefore, a*(t, T3) is determined for 0 - t < T3•
Continuing in this way, we determine a( t, Tj) for all j = 1, . . ., n + 1 and
0 � t < Tj.
Using the bond volatilities a*(t, T) and (10.4.8), we may write the zero­
coupon bond price formula (10.3.19) of Theorem 10.3.2 as

dB(t, Tj) = R(t)B(t, Tj) dt - a*(t, Tj)B(t, Tj) dW(t)

= R(t)B(t, Tj) dt + a*(t, Tj)a*(t, Tn+I)B(t, Tj) dt


)
)



D(Tj) = D(Tj)B(Tj, Tj)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-464-0.png)

T3
= B(O,Tj) exp 1
### {




- 1 [T3 ] [� (a*(u, Tj) ) [2 ] - a*(u, Tj )a* [( u, T] n+1 [)] ] [du]

(10.4.24) } [ . ]



(10.4.24)



In the special case when j = n + 1, we obtain


446 10 Term-Structure Models



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-465-0.png)














is a Brownian motion under a measure iP defined by
Z(Tn+l) dlPTn+l for all E F,
P(A) [= ] A
i


10.5 Summary 447


where


0


where 80, 81> and 82 are either constants (as in the text) or nonrandom func­
tions of time (as in Exercise 10.3), and Y1(t) and Y2(t) are the factor pro­
cesses. When regarded as a two-dimensional process, (Y1 (t), Y2(t)) is Markov,
and hence bond prices and the prices of interest rate derivatives are func­
tions of these processes. These functions can be determined by solving partial
differential equations with boundary conditions depending on the particular
instrument being priced. For the boundary condition a ociated with zero­
coupon bonds, the partial differential equations reduce to a system of ordinary
differential equations, which permits rapid calibration of the models.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-466-0.png)
448 10 Term-Structure Models

For the two-factor affine-yield models, the price at time t of a zero-coupon
bond maturing at a later time and paying 1 upon maturity is of the form
T
(10.5.1)

The nonrandom functions CI (t, C2(t, and A(t, are given by a system
T), T), T)
of ordinary differential equations in the t variable and the boundary condition

=
CI(, C2(, = = 0.
T T) T T) A(T, T)

When the model coefficients, both Oo, oi, and 82 in (10.2.6) and the coefficients
in the differential equations satisfied by the factor processes, are constant, the
functions CI (t, T), C2(t, T), and A(t, T) depend on t and T only through their
difference T = t.
T The affine-yield models are calibrated by choosing the coefficients in
(10.2.6) and/or in the stochastic differential equations for the factor processes.
To introduce more variables for the calibration, it is customary to take the
coefficients to be nonrandom, often piecewise constant, functions of time. It
is helpful before beginning the calibration to make sure that the models are
written in their most parsimonious form so that one cannot obtain the same
model statistics from two different sets of parameter choices. The canonical
forms presented here are "most parsimonious" in this sense.
There are three canonical two-factor affine-yield models, which we call the
two-factor Vasicek model, the two-factor Cox-Ingersoll-Ross model, and the
two-factor mixed model. In the first of these, both factors can become negative.
In the second, both factors are guaranteed to be nonnegative. In the third, one
factor is guaranteed to be nonnegative and the other can become ne�tive.
All three of these models are driven by independent Brownian motions WI(t),
W2(t) under a risk-neutral measure JPl.
The canonical two-factor Vasicek model is


where JLI 2: 0, JL2 2: 0, Au - 0, A22 > 0, AI2 : 0, and A21 : 0. The system
of ordinary differential equations (10.2.56)-(10.2.58) determines the functions

B(t, = e-Y, (t)C, (t,T)-Y2(t)C2(t,T)-A(t,T).
T)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-467-0.png)
10.5 Summary 449
C1(T -t), C2(T-t), and (T-t) in (10.5.1). The canonical two-factor mixed
A
model is


making the similar replacement for

on T and that satisfies


where a*(t, T) = Jt a(t, v) dv; see Theorem 10.3.2. A calibration procedure
for the HJM model is provided in Subsection 10.3.6.
In contrast to the continuously compounding forward rate f(t, T), which
is the basis of the HJM model, forward LIBOR L(t, T) is the simple interest



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-468-0.png)
450 10 Term-Structure Models

rate that can be locked in at time t for borrowing at a later time T over the
interval [T, T + 8] . Here 8 is a positive constant, and although not indicated
by the notation, L(t, T) depends on the choice of this constant.
Section 10.4 introduces a model for forward LIBOR. One can build this
model so that forward LIBOR L(t, T) is log-normal under the forward measure
pT+O, and this permits a mathematically rigorous derivation of the Black
caplet formula. This formula is similar to the Black-Scholes-Merton formula
for equities but used in fixed income markets in which the essence of the
market is that the interest rate is random, in contrast to the Black-Scholes­
Merton a umption.


10.6 Notes


The Vasicek model appears in [154] and the Cox-Ingersoll-Ross model in [41].
Hull and White generalized the Vasicek model in [88]. The general concept
of multifactor affine-yield models is developed in Duffie and Kan [57], [58].
The reduction of affine-yield models to canonical versions is due to Dai and
Singleton [44]. A sampling of other articles related to ane-yield models in­
cludes Ait-Sahalia [1], Balduzzi, Das, Foresi, and Sundaram [7], Chen [29],
Chen and Scott [30], [31], [32], Collin-Dufresne and Goldstein [38], [39], Duf­
fee [55], and Piazzesi [132]. Maghsoodi [116] provides a detailed study of the
one-dimensional CIR equation when the parameters are time-varying.
Although affine-yield models have simple bond price formulas, the prices
for fixed income derivatives are more complicated. However, numerical so­
lution of partial differential equations can be avoided by Fourier transform
analysis; see, Duffie, Pan, and Singleton [59].
Some other common short rate models are those of Black, Derman, and
Toy [15], Black and Karasinski [16], and Longstaff and Schwartz [111]. An
empirical comparison of various short rate models is provided by Chan et al.

[28].
Ho and Lee [85] developed a discrete-time model for the evolution of the
yield curve. The continuous-time limit of the Ho-Lee model is a constant­
diffusion forward rate. In particular, the interest rate behaves like that in a
Vasicek model and can become negative.
An arbitrage-free framework for the evolution of the yield curve in contin­
uous time was developed by Heath, Jarrow, and Morton [83]. Related papers
are [81] and [82]. The HJM framework presented in this chapter is general,
but it can be specialized to obtain a Markov implementation; see Brace and
Musiela [20], Cheyette [34], and Hunt, Kennedy, and Pelsser [90]. Filipovic [66]
examines the issue of making the yield curves generated by the HJM model
consistent with the scheme used to generate the initial yield curve. Jara [96]
considers an HJM-type model but for interest rate futures rather than forward
rates. The advantage is that the drift term causing the explosion discussed in
Subsection 10.4.1 does not appear in such a model.


10.7 Exercises 451


The switch from continuously compounding forward rates to simple for­
ward rates in order to remove the explosion problem described in Section
10.4.1 was proposed by Sandmann and Sondermann [146], [147]. The use of
a log-normal simple interest rate to price caps and floors was worked out by
Miltersen, Sandmann, and Sondermann [125]. This idea was embedded in a
full forward LIBOR term-structure model by Brace, G�tarek, and Musiela

[19]. This was the first full term-structure model consistent with the heuristic
formula provided by Black [13] in 1976 and in common use since then.
Recently, a variation on forward LIBOR models has been developed for
swaps markets; see Jamshidian [95] and the three books cited below. Term­
structure models with jumps have been studied by Bjork, Kabanov, and Rung­
galdier [12], Das [46], Das and Foresi [47], Gla erman and Kou [73], Gla er­
man and Merener [74], and Shirakawa [149].
Three recent books by authors with practical experience in term-structure
modeling are Pelsser [131], Brigo and Mercurio [21], and Rebonato [137].
Pelsser's text [131] is succinct but comprehensive, Brigo and Mercurio's text

[21] contains considerably more detail, and Rebonato's book [137] is devoted
to forward LIBOR models.


10.7 Exercises

Exercise 10.1 (Statistics in the two-factor Vasicek model) . Accord­
ing to Example 4.7.3, Y1(t) and Y2(t) in (10.2.43)-(10.2.46) are Gaussian
proce es.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-470-0.png)








452 10 Term-Structure Models



where the Ito integrals





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-471-0.png)




JP.









1E(J3(t)J4(t)) = 0.



(iii) Some derivative securities involve time spread (i.e., they depend on the
interest rate at two different times). In such cases, we are interested in
the joint statistics of the factor processes at different times. These are
still jointly normal and depend on the statistics of the Ito integrals Ii at


10.7 Exercises 453



different times. Compute E[I1(8)h(t)], where 0 � 8 < t. (Hint: Fix 8 2 0
and define


tions

(10. 7.4)
(10.7.5)
(10.7.6)


(10.7.7)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-472-0.png)



(10.7.8)



Holding T fixed, derive a system of ordinary differential equations for
ftCI (t, T), ftC2(t, T), and ftA(t, T).


454 10 Term-Structure Models

(ii) Using the terminal conditions Ct(T, T) = C2(T, T) = 0, solve the equa­
tions in (i) for Ct(t, T) and C2(t, T). (As in Subsection 10.2.1, the func­
tions Ct and c2 depend on t and T only through the difference T = T-t;
however, the function A discussed in part (iii) below depends on t and T
separately.
)
iii Using the terminal condition A(T, T) 0, write a formula for A(t, T) as
( ) =
an integral involving Ct(u,T), C2(u,T), and oo(u). You do not need to
evaluate this integral.
(iv) Assume that the model parameters At > 0 A2 > 0, A2t, Ot, and 82 and the
initial conditions Yt (0) and Y2(0) are given. We wish to choose a function
o0 so that the zero-coupon bond prices given by the model match the
bond prices given by the market at the initial time zero. In other words,
we want to choose a function o(T), T 2 0, so that

f(O, T, Yt(O), Y2(0)) = B(O, T), T 2 0.


(10. 7.9)

a fact that you will need.
)

Exercise 10.4. Hull and White [89] propose the two-factor model



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-473-0.png)

dU(t) = -AtU(t) dt + at dB2(t),
dR(t) = [O(t) + U(t) - A2R(t)] dt + a2 dBt(t),



10.7.10
( )
(10.7.11)



where At, A2, at, and a2 are positive constants, O(t) is a nonrandom function,
and Bt (t) and B2(t) are correlated Brownian motions with dBt (t) dB2(t) =
pdt for some p E ( -1, 1 . In this exercise, we discuss how to reduce this to the
)
two-factor Vasicek model of Subsection 10.2.1, except that, instead of ( 10.2.6,
)
the interest rate is given by (10.7.7), in which o0(t) is a nonrandom function
of time.


10.7 Exercises 455



i Define
( )



U(t) 0 a1
) K =, E =
###### [ ] [.X1 ] [ OJ
X(t =
R(t)
## '
-1 .X2 0 a2



8(t) =, B(t) =

     - t)]
###### [ �
�:�:�
### [ l,

R(t) -1 .X2



so that 10.7.10 and 10.7.11 can be written in vector notation as
( ) ( )



dX(t) = 8(t) dt - KX(t) dt + Ed [B] (t). 10.7.12
( )



Now set



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-474-0.png)

Show that

ii With
( )







( )

where


nian motion. In this model, the price at time t E [0, T] of the zero-coupon
bond maturing at time T is


456 10 Term-Structure Models
B(t, T) = e-C(t,T)R(t)-A(t,T),



where C(t, T) and A(t, T) are given by (6.5.10) and (6.5.11):

T) =
C(t,
### 1

T

T
e- I: bdv ds = (1 - e-b(T-t) ),

            


_ _

T
A(t, T) = a (, T) - T) ds
C s �a2C2(s,



e e
4b3
+
b3



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-475-0.png)

1
L(t) = -= log B(t, t + 7).
T


dR(t) = (a - bR(t)) dt + dWt(t). (10.7.16)


dR(t) = (a - bR(t)) dt + a dB(t) . (10.7.17)


10.7 Exercises 457



Exercise 10.7 (Forward measure in the two-factor Vasicek model).
Fix a maturity T > 0. In the two-factor Vasicek model of Subsection 10.2.1,
consider the T-forward measure [j] T of Definition 9.4.1:



jT (A) = [for all ][A ][E ] [F. ]

[T) ][i ][D(T) ][d]



(i) Show that the two-dimensional [jp>] T_Brownian motions W{(t), W!(t) of
(9.2.5) are



WT(t) = lot Ct (T - u) du + Wj (t), j = 1, 2, (10.7.18)



where Ct(r) and C2(r) are given by (10.2.26)-(10.2.28).
(ii) Consider a call option on a bond maturing at time T > T. The call expires
at time T and has strike price K. Show that at time zero the risk-neutral
price of this option is


###### B(O, T)fET e [-CdT-T)Y• (T)-C2(T-T)Y2(T)-A(T-T) ] [_ ] K [) ][+] ] [. ] (10.7.19)

[ [( ]



(iii) Show that, under the T-forward measure Jr, the term
X = -Ct(T - T)Yt(T) - C2(T - T)Yt(T) - A(T - T)
appearing in the exponent in (10.7.19) is normally distributed.
(iv) It is a straightforward but lengthy computation, like the computations in
Exercise 10.1, to determine the mean and variance of the term X. Let us
call its variance a [2 ] and its mean IL   - �a [2], so that we can write X as



X = �a2 [2 ] -aZ '



where Z is a standard normal random variable under Jr. Show that the
call option price in (10.7.19) is
B(O, T) (elL N(d+) - KN(d- )),
where
d± =          - log K ±
�a [2] .
###### � (IL )



Exercise 10.8 (Reversal of order of integration in forward rates).
The forward rate formula (10.3.5) with v replacing T states that



f(t, v) = f(O, v) + lo [t ] a(u, v) du + lo [t ] a(u, v) dW(u) .



Therefore,

 - i [T ] f(t,v) dv = - i [T] [f(o, v) + 1 [t] a(u, v) du + 1 [t] a(u, v) dW(u)] dv.
(10.7.20)


458 10 Term-Structure Models



(i) Define



= =
a(u, t,T) a(u, v) dv, u(u, t,T) a(u,v) dv.
### 1T 1T



Show that if we reverse the order of integration in (10.7.20), we obtain
the equation

J(t, v) dv
### -1T



f(O, v) dv a(u, t, T) du u(u, t, T) dW(u).
= -lo [t ] -lo [t ]
(10.7.21)
### -1T



(In one case, this is a reversal of the order of two Riemann integrals, a
step that uses only the theory of ordinary calculus. In the other case, the
order of a Riemann and an Ito integral are being reversed. This step is
justified in the appendix of [83]. You may a ume without proof that this
step is legitimate.)
(ii) Take the differential with respect to t in (10.7.21), remembering to get two
terms from each of the integrals J; a(u, t, T) du and J; u(u, t, T) dW(u)
because one must differentiate with respect to each of the two ts appearing
in these integrals.
(iii) Check that your formula in (ii) agrees with (10.3.10).

Exercise 10.9 (Multifactor HJM model). Suppose the Heath-Jarrow­
Morton model is driven by a d-dimensional Brownian motion, so that a( t, T)
is also a d-dimensional vector and the forward rate dynamics are given by
d
df(t, T) a(t, T) dt + ai(t, T) dWj(t).
= L
j=l

(i) Show that (10.3.16) becomes
d
a(t, T) L ai(t, T) [aj(t, T) + ei(t)] .
=
j=l



(ii) Suppose there is an adapted, d-dimensional process



e(t) (e1(t), . . ., ed(t))
=



satisfying this equation for all 0 : t : T : Show that if there are ma­
T.
turities T1, . . ., Td such that the d x d matrix (ai(t, Ti)) . . is nonsingular,

                                                                 -,J
then e(t) is unique.


10.7 Exercises 459

Exercise 10.10. (i) Use the ordinary differential equations (6.5.8) and (6.5.9)
satisfied by the functions A(t, T) and C(t, T) in the one-factor Hull-White
model to show that this model satisfies the HJM no-arbitrage condition
(10.3.27).
(ii) Use the ordinary differential equations (6.5.14) and (6.5.15) satisfied by
the functions A(t, T) and C(t, T) in the one-factor Cox-Ingersoll-Ross
model to show that this model satisfies the HJM no-arbitrage condition
(10.3.27).

Exercise 10.11. Let o > 0 be given. Consider an interest rate swap paying a
fixed interest rate K and receiving backset LIBOR L(Tj-1, Tj-1) on a princi­
pal of 1 at each of the payment dates Tj = oj, j = 1, 2, . . ., n + 1. Show that
the value of the swap is
n+1 n+1
oK .L: B(o, Tj) - o L B(o, Tj )L(O, Tj-1 ). (10.7.22)
j=1 j=1

Remark 10. 7. 1. The swap rote is defined to be the value of K that makes the
initial value of the swap equal to zero. Thus, the swap rate is


(10.7.23)



Use the definitions



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-478-0.png)

B(O, T + o) = lE [D(T + o)],



and the properties of conditional expectations to show that


=
lE [D(T + o)L(T, T)] B(O, T + o)L(O, T).


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-479-0.png)
1 1


Introduction to Jump Processes


1 1 . 1 Introduction


This chapter studies jump-diffusion processes. The "diffusion" part of the
nomenclature refers to the fact that these processes can have a Brownian
motion component or, more generally, an integral with respect to Brownian
motion. In addition, the paths of these processes may have jumps. We consider
in this chapter the special case when there are only finitely many jumps in
each finite time interval.
One can also construct processes in which there are infinitely many jumps
in a finite time interval, although for such processes it is necessarily the case
that, for each positive threshold, only finitely many jumps can have a size
exceeding the threshold in any finite time interval. The number exceeding the
threshold can depend on the threshold and become arbitrarily large as the
threshold approaches zero. Such processes are not considered here, although
the theory provided here gives some idea of how such processes can be ana­
lyzed.
The fundamental pure jump process is the Poisson process, and this is
presented in Section 11.2. All jumps of a Poisson process are of size one. A
compound Poisson process is like a Poisson process, except that the jumps are
of random size. Compound Poisson processes are the subject of Section 11.3.
In Section 11.4, we define a jump process to be the sum of a nonrandom
initial condition, an Ito integral with respect to a Brownian motion dW(t), a
Riemann integral with respect to dt, and a pure jump process. A pure jump
process begins at zero, has finitely many jumps in each finite time interval,
and is constant between jumps. Section 11.4 defines stochastic integrals with
respect to jump processes. These stochastic integrals are themselves jump
processes. Section 11.4 also examines the quadratic variation of jump processes
and their stochastic integrals.
In Section 11.5, we present the stochastic calculus for jump processes. The
key result is the extension of the ItO-Doeblin formula to cover these processes.


462 1 1 Introduction to Jump Processes


In Section 11.6, we take up the matter of changing measures for Poisson
processes and for compound Poisson processes. We conclude with a discussion
of how to simultaneously change the measure for a Brownian motion and a
compound Poisson process. The effect of this change is to adjust the drift of
the Brownian motion and to adjust the intensity (average rate of jump arrival)
and the distribution of the jump sizes for the compound Poisson process.
In Section 11.7, we apply this theory to the problem of pricing and partially
hedging a European call in a jump-diffusion model.


1 1 . 2 Poisson Process


In the way that Brownian motion is the basic building block for continuous­
path processes, the Poisson process serves as the starting point for jump pro­
cesses. In this section, we construct the Poisson process and develop its basic
properties.


Exponential Random Variables
11.2.1

Let T be a random variable with density
###### f(t) = [{ ][Ae->.t, t ][� ][0, ] (11.2.1)

0, t 0,
<

where A is a positive constant. We say that T has the exponential distribution
or simply that T is an exponential mndom variable.
The expected value of T can be computed by an integration by parts:




          - t [=O ]
= 0 - e->.t =             ± l t [t=oo ][=O ] t
For the cumulative distribution function, we have
+ e-,\t dt
t=oo
lET = J.00 tf(t) dt = A te-,\t dt = -te-,\tl



1o [t ] �u [u-t ][=O ]
F(t) = IP'{r $ t} = Ae->.u du = -e->.u - = 1 - e->.t,



t � 0,



and hence
IP'{r > t} = e [-] >- [t], t � 0.



IP'{r > t} = e [-] >- [t], t � 0. (11.2.2)

Suppose we are waiting for an event, such as default of a bond, and we
know that the distribution of the time of this event is exponential with mean
t
(i.e., it has the density (11.2.1)). Suppose we have already waited s time units,
and we are interested in the probability that we will have to wait an additional
t time units (conditioned on knowing that the event has not occurred during
the time interval [0, s]). This probability is


1 1 .2 Poisson Process 463


                                                                                            - .                                                                                             t.


(11.2.4)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-482-0.png)





Note that at the jump times N(t) is defined so that it is right-continuous (i.e.,
N(t) = lims.j.t N(s)). We denote by :F(t) the a-algebra of information acquired
by observing N(s) for 0 :S s :S t.
Because the expected time between jumps is the jumps are arriving
±,
at an average rate of A per unit time. We say the Poisson process N(t) has
intensity A. Figure 11.2.1 shows one path of a Poisson process.


11.2.3 Distribution of Poisson Process Increments


In order to determine the distribution of the increments of a Poisson process,

0 0 0 0
we must first determine the distribution of the jump times 81' 82,


464



1 1 Introduction to Jump Processes



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-483-0.png)
















1 1.2 Poisson Process 465


PROOF: For k 1, we have N(t) ; k if and only if there are at least k jumps
;
by time t (i.e., if and only if sk, the time of the kth jump, is less than or equal
to t). Therefore,


Similarly,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-484-0.png)









For k = 0, we have from (11.2.2)



IP'{N(t) = 0} = IP'{S1 > t} = IP'{T1 > t} = e->. [t],



which is (11.2.6) with k = 0. 0

Suppose we observe the Poisson process up to time s and then want to
know the distribution of N(t + s) - N(s), conditioned on knowing what has
happened up to and including time s. It turns out that the information about
what has happened up to and including time s is irrelevant. This is a conse­
quence of the memorylessness of exponential random variables (see (11.2.3)).
Because N(t+s)-N(s) is the number of jumps in the time interval (s, t+s], in
order to compute the distribution of N(t + s) - N(s), we are interested in the
time of the next jump after s. At time s, we know the time since the last jump,
but the time between s and the next jump does not depend on this. Indeed,
the time between s and the first jump after s has an exponential distribution
with mean, independent of everything that has happened up to time s. The
!
time between that jump and the one after it is also exponentially distributed
with mean, independent of everything that has happened up to time s.
!
The same applies for all subsequent jumps. Consequently, N(t + s) - N(s) is
independent of :F(s). Furthermore, the distribution of N(t + s) - N(s) is the
same as the distribution of N(t). In both cases, one is simply counting the
number of jumps that occur in a time interval of length t, and the jumps are


466 1 1 Introduction to Jump Processes


independent and exponentially distributed with mean When a process has
t                         the property that the distribution of the increment depends only on the dif­
ference between the two time points, the increments are said to be stationary.
Both the Poisson process and Brownian motion have stationary independent
increments.

Theorem 11.2.3. Let N(t) be a Poisson process with intensity .A - 0, and
let 0 = to < h < - · · < tn be given. Then the increments

N(ti) - N(to), N(t2) - N(ti), . . ., N(tn) - N(tn-d

are stationary and independent, and


=
k 0, 1, . . . .
(11.2. 7)


=

0


(11.2.8)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-485-0.png)












as we would expect. We next compute the expected increment


11.2 Poisson Process 467



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-486-0.png)

k=O













k=1
= ) [2] (t - 8) [2 ] + .>.(t - 8) .



This implies

Var(N(t) - N(8)] = lE((N(t) - N(8)} [2] ] - (lE(N(t) - N(8)]} [2 ]

= .>. [2] (t - 8) [2 ] + .>.(t - 8) - .>. [2] (t - 8) [2 ]
= .>.(t - 8); (11.2.10)

the variance is the same as the mean.


11.2.5 Martingale Property


Theorem 11.2.4. Let N(t) be a Poisson process with intensity .> We define
the compensated Poisson process (see Figure 11.2.2}

M(t) = N(t) - .>.t.
Then M(t) is a martingale.


468 11 Introduction to Jump Processes

PROOF: Let 0 : s < t be given. Because N(t) - N(s) is independent of :F(s)
and has expected value .X(t - s), we have

lE[M(t)IF(s)] [= ] lE[M(t) - M(s)i:F(s)] + lE[M(s)i:F(s)]


=
lE[N(t) - N(s) - .X(t - s)i:F(s)] + M(s)





=
lE[N(t) - N(s)] - .X(t - s) + M(s)


=
M(s). D


Fig. 1 1 .2.2. One path of a compensated Poisson process.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-487-0.png)

Compound Poisson Process
11.3

When a Poisson process or a compensated Poisson process jumps, it jumps
up one unit. For models of financial markets, we need to allow the jump size
to be random. We introduce random jump sizes in this section.


11.3.1 Construction of a Compound Poisson Process


Let N(t) be a Poisson process with intensity .X, and let Y1, Y2, . . . be a se­

=
quence of identically distributed random variables with mean (3 lEYi . We
a ume the random variables Y1, Y2, . . . are independent of one another and
also independent of the Poisson process N ( t). We define the compound Poisson
process
N(t)
Q(t) [= ] L Yi, t (11.3.1)
2: o.
i=l

The jumps in Q(t) occur at the same times as the jumps in N(t), but whereas
the jumps in N(t) are always of size 1, the jumps in Q(t) are of random size.
The first jump is of size Y1, the second of size Y2, etc. Figure 11.3.1 shows one
path of a compound Poisson process.


11.3 Compound Poisson Process 469



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-488-0.png)











On average, there are ..\t jumps in the time interval [0, t], the average jump
size is /3, and the number of jumps is independent of the size of the jumps.
Hence, IEQ(t) is the product {3..\t.


470 11 Introduction to Jump Processes


Theorem 11.3.1. Let Q(t) the compound Poisson process defined above.
be
Then the compensated compound Poisson process
Q(t) - (3>.t
is a martingale.
PROOF: Let 0 : s < t be given. Because the increment Q(t) - Q(s) is inde­
pendent of F(s) and has mean (3>.(t - s), we have
lE Q(t) - (3>.t F(s) = lE Q(t) - Q(s) F(s) + Q(s) - (3>.t

[ i ] [ I ]
= (3>.(t - s) + Q(s) - (3>.t
= Q(s) - (3>.s.

[


Just like a Poisson process, a compound Poisson process has stationary
independent increments. We give the precise statement below.

Theorem 11.3.2. Let Q(t) be a compound Poisson process and let 0 = to
<
h < [· · · ] < tn be given. The increments


are independent and stationary. In particular, the distribution of Q(tj) Q(tj-t) is the same as the distribution ofQ(tj - t1-d·


11.3.2 Moment-Generating Function

In Theorem 11.3.2, we did not write an explicit formula for the distribution
of Q(ti - tj-l) because the formula for the density or probability ma func­
tion of this random variable is quite complicated. However, the formula for its
moment-generating function is simple. For this reason, we use moment gen­
erating functions rather than densities or probability ma functions in much
of what follows.
Let Q(t) be the compound Poisson process defined by (11.3.1). Denote the
moment-generating function of the random variable Yi by

cpy(u) = lEeu [Y],_

This does not depend on the index i because Yll Y2, . . . all have the same dis­
tribution. The moment generating function for the compound Poisson process
Q(t) is

'PQ(t)(u) = lE [euQ(t) ]
N(t)
= lEexp {u L Yi}
i= l

k
00
= JP>{N(t) = 0} lEexp u Yi N(t) = k JP>{N(t) = k}
+ L L i }
k=l i=l
{


11.3 Compound Poisson Process 471



00 k



= =
IP'{N(t) 0} + L IEexp { u L Yi }IP'{N(t) [= ] k}
k=l i=l





(.At)

k!



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-490-0.png)

=



(11.3.3)


=
is thus






               


ing intensity .Ap(ym). Define


472 1 1 Introduction to Jump Processes
M
L


M

m=l
= [JEe]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-491-0.png)

![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-491-2.png)




- •



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-491-1.png)

the distribution of the whole path of the process Q appearing on the left-hand
side of (11.3.5).
Recall that the process Q appearing on the left-hand side of (11.3.5) is the
compound Poisson process defined by (11.3.1). For this process N(t), the total
number of jumps by time t is Poisson with intensity .A, and the sizes of the
jumps, Y1, Y2, • . -, are identically distributed random variables, independent
of one another and independent of N(t), and with lP{Yi = Ym} = p(ym) for


11.4 Jump Processes and Their Integrals 473


m = 1, . . ., M. Because the processes Q and Q have the same distribution,
these statements must also be true for the total number of jumps and the sizes
of the jumps of the process Q of (11.3.6), which is what the theorem a erts.
0

The substance of Theorem 11.3.3 is that there are two equivalent ways of
regarding a compound Poisson process that has only finitely many possible
jump sizes. It can be thought of as a single Poisson process in which the
size-one jumps are replaced by jumps of random size. Alternatively, it can be
regarded as a sum of independent Poisson processes in each of which the size­
one jumps are replaced by jumps of a fixed size. We restate Theorem 11.3.3
in a way designed to make this more clear.

Corollary 11.3.4. Let Y1, . . ., YM be a finite set of nonzero numbers, and

              - .               let p(y1),,p(yM) be positive numbers that sum to 1. Let Y1, Y2, . . . be a
sequence of independent, identically distributed random variables with IP'{Yi =
Ym} = p(ym), m = 1, [.] . ., M. Let N(t) be a Poisson process and define the
compound Poisson process
N(t)
Q(t) = L }i.
i=l
For m = 1, . . ., M, let Nm(t) denote the number of jumps in Q of size Ym up
to and including time t. Then
M M
N(t) = L Nm(t) and Q(t) = L YmNm(t).
m=l m=l
The processes N1, . . ., N M defined this way are independent Poisson processes,
and each Nm has intensity .>p(ym)·


11.4 Jump Processes and Their Integrals


In this section, we introduce the stochastic integral when the integrator is a
process with jumps, and we develop properties of this integral. We shall have
a Brownian motion and Poisson and compound Poisson processes. There will
always be a single filtratoin a ociated with all of them, in the sense of the
following definition.

Definition 11.4.1. Let (!I, F, IP') be a probability space, and let F(t), t 2 0,
be a filtration on this space. We say that a Brownian motion W is a Brownian
motion relative to this filtration if W(t) is F(t)-measurable for every t and
for every u > t the increment W(u) - W(t) is independent of F(t). Similarly,
we say that a Poisson process N is a Poisson process relative to this filtration
if N(t) is F(t)-measurable for every t and for every u - t the increment


474 1 1 Introduction to Jump Proce


N(u) - N(t) is independent of J="(t). Finally, we say that a compound Poisson
process Q is a compound Poisson process relaative to this filtration if Q(t) is
J="(t)-measumble for every t and for every u > t the increment Q(u) - Q(t) is
independent of J="(t).


11.4.1 Jump Processes


We wish to define the stochastic integral

!P(s) dX(s),
lo [t ]

where the integrator X can have jumps. Let ( n, J=", P) be a probability space
on which is given a filtration J="(t), t - 0. All processes will be adapted to
this filtration. Furthermore, the integrators we consider in this section will be
right-continuous and of the form

X(t) X(O) I(t) R(t) J(t). (11.4.1)
= + + +

In (11.4.1), X(O) is a nonrandom initial condition. The process


I(t) F(s) dW(s) {11.4.2)
=lo [t ]

is an Ito integml of an adapted process F(s) with respect to a Brownian
motion relative to the filtration. We shall call I(t) the ItO integml part of X.
The process R(t) in (11.4.1) is a Riemann integml [1 ]

R(t) = 1 [t ] e(s) ds (11.4.3)

for some adapted process e(t). We shall call R(t) the Riemann integml part
of X. The continuous part of X(t) is defined to be


xc(t) X(O) I(t) R(t) X(O) F(s) dW(s) e(s) ds.
= + + = + 1 [t ] +lo [t ]

The quadratic variation of this process is


an equation that we write in differential form as

1 One usually takes this to be a Lebesgue integral with respect to dt, but for all the
cases we consider, the Riemann integral is defined and agrees with the Lebesgue
integral.


1 1 .4 Jump Processes and Their Integrals 475


Finally, in (11.4.1), J(t) is an adapted, right-continuous pure jump process
with J(O) = 0. By right-continuous, we mean that J(t) = lims.j.t J(s) for all
t ; 0. The left-continuous version of such a process will be denoted J(t-). In
other words, if J has a jump at time t, then J(t) is the value of J immediately
after the jump, and J(t-) is its value immediately before the jump. We a ume
that J does not jump at time zero, has only finitely many jumps on each finite
time interval (0, T], and is constant between jumps. The constancy between
jumps is what justifies calling J(t) a pure jump process. A Poisson process
and a compound Poisson process have this property. A compensated Poisson
process does not because it decreases between jumps. We shall call J(t) the
pure jump part of X.

Definition 11.4.2. A process X(t) of the form {11.4.1}, with Ito integral part
I(t), Riemann integral part R(t), and pure jump part J(t) as described above,
will be called a jump process. The continuous part of this process is xc(t) =
X(O) + I(t) + R(t).

A jump process in this book is not the most general possible because
we permit only finitely many jumps in finite time. For many applications,
these processes are sufficient. Furthermore, the stochastic calculus for these
processes gives a good indication of how the stochastic calculus works for the
more general case.
A jump process X(t) is right-continuous and adapted. Because both I(t)
and R(t) are continuous, the left-continuous version of X(t) is

X(t-) = X(O) + I(t) + R(t) + J(t-).

The jump size of X at time t is denoted

LlX(t) = X(t) - X(t-).

If X is continuous at t, then LlX(t) = 0. If X has a jump at time t, then
LlX(t) is the size of this jump, which is also LlJ(t) = J(t) - J(t-), the size
of the jump in J. Whenever X(O-) appears in the formulas below, we mean
it to be X(O). In particular, LlX(O) = 0; there is no jump at time zero.

Definition 11.4.3. Let X(t) be a jump process of the form {11.4.1}-{11.4.3}
and let s) be an adapted process. The stochastic integral of with respect
q';( q;
to X is defined to be
t t t
1 q'j(s) dX(s) = 1 q'j(s)F(s) dW(s) + 1 q'j(s)8(s) ds + L q'j(s)LlJ(s).
0 0 0 O<s:<t
(11.4.4)
In differential notation,


476 1 1 Introduction to Jump Processes


tP(t)dX(t) tl>(t) dl(t) tl>(t) dR(t) tl>(t) dJ(t)
= + +
tf>(t) dXc(t) tf>(t) dJ(t),
= +

where


tl>(t) dl(t) tl>(t)F(t) dW(t), tl>(t) dR(t) tl>(t)8(t) dt,
= =
tl>(t) dXc(t) tl>(t)F(t) dW(t) tl>(t)8(t) dt.
= +

Example 11.4.4. Let X(t) M(t) N(t)->t, where N(t) is a Poisson process
= =
with intensity > so that M(t) is the compensated Poisson process of Theorem
11.2.4. In the terminology of Definition 11.4.2, I(t) 0, xc(t) R(t) ->t,
= = =
and J(t) N(t). Let tl>(s) LlN(s) (i.e., tl>(s) is 1 if N has a jump at time
= =
s, and tf>( s) is zero otherwise). For s E (0, t], tf>( s) is zero except for finitely
many values of s, and thus



However,

tl>(s) dN(s) L (.6.N(s)) [2 ] N(t).
= =
0
1 [t ]
O<s�t
Therefore,


tl>(s) dM(s) tl>(s) ds tl>(s) dN(s) N(t).
lo [t ] = ->.lo [t ] + lo [t ] =


For Brownian motion W(t), we defined the stochastic integral


I(t) F(s) dW(s)
= lo [t ]



(11.4.5)

0



in a way that caused I(t) to be a martingale. To define the stochastic integral,
we approximated the integrand F(s) by simple integrands Fn(s), wrote down
a formula for
ln(t) Fn(s) dW(s),
= lo [t ]

and verified that, for each n, In(t) is a martingale. We defined I(t) as the limit
of In(t) as n -+ oo and, because it is the limit of martingales, I(t) also is a
martingale. The only conditions we needed on F(s) for this construction were
that it be adapted and that it satisfy the technical condition lE J; F [2 ] ( s) ds <
oo for every t > 0.
This construction makes sense for finance because we ultimately replace
F(s) by a position in an a et and replace W(s) by the price of that a et.
If the a et price is a martingale (i.e., it is pure volatility with no underlying


1 1 .4 Jump Processes and Their Integrals 477
trend), then the gain we make from investing in the a et should also be a
martingale. The stochastic integral is this gain.
In the context of processes that can jump, we still want the stochastic
integral with respect to a martingale to be a martingale. However, we see
in Example 11.4.4 that this is not always the case. The integrator M(t) in
that example is a martingale (see Theorem 11.2.4), but the integral N(t) in
(11.4.5) is not because it goes up but cannot go down.
An agent who invests in the compensated Poisson process M ( t) by choos­
ing his position according to the formula 4>(s) = <1N(s) has created an arbi­
trage. To do this, he is holding a zero position at all times except the jump
times of N(s), which are also the jump times of M(s), at which times he holds
a position one. Because the jumps in M(s) are always up and our investor
holds a long position at exactly the jump times, he will reap the upside gain
from all these jumps and have no possibility of loss.
In reality, the portfolio process 4>(s) = <1N(s) cannot be implemented
because investors must take positions before jumps occur. No one without
insider information can arrange consistently to take a position exactly at the
jump times. However, 4>( s) depends only on the path of the underlying process
M up to and including at time s and does not depend on the future of the
path. That is the definition of adapted we used when constructing stochastic
integrals with respect to Brownian motion. Here we see that it is not enough
to require the integrand to be adapted. A mathematically convenient way
of formulating the extra condition is to insist that our integrands be left­
continuous. That rules out 4'( s) = <1N ( s). In the time interval between jumps,
this process is zero, and a left-continuous process that is zero between jumps
must also be zero at the jump times.
We give the following theorem without proof.

Theorem 11.4.5. Assume that the jump process X(s) of {11.4.1}-{11.4.3} is
a martingale, the integrand 4>(s) is left-continuous and adapted, and


Then the stochastic integral J� 4>(s) dX(s) is also a martingale.
The mathematical literature on integration with respect to jump processes
gives a slightly more general version of Theorem 11.4.5 in which the integrand
is required only to be predictable. Roughly speaking, such processes are those
that can be gotten as the limit of left-continuous processes. We shall not need
this more general concept.
Note that although we require the integrand 4>( s) to be left-continuous in
Theorem 11.4.5, the integrator X(t) is always taken to be right-continuous,
and so the integral J� 4>( s) dX ( s) will be right-continuous in the upper limit of
integration t. The integral jumps whenever X jumps and 4> is simultaneously
not zero. The value of the integral at time t includes the jump at time t if
there is a jump; see (ll.4.4).

lE 1t F2(s)4>2(s) ds < 00 for all t 2 0.


478 1 1 Introduction to Jump Processes
Example 11.4.6. Let N(t) be a Poisson process with intensity A, let M(t) =
N(t) - At be the compensated Poisson process, and let


It follows that, when S1 > s,



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-497-0.png)
1 1 .4 Jump Processes and Their Integrals 4 79
AlE[t A S1IF(s)] = AlE[t A S1IS1 > s]



= A [2] (t A
u)e->.(u-s) du
1 [00 ]



= A [2] + A [2] [1][oo ][t]
ue->.(u-s)du e->.(u-s)du
1 [t ]



= + A
-Aue->.<u-s) l [u=t ] 1 [t ] e->.(u- [s] >du-Ate->.<u-s) [lu=oo ]
u [=] s 8 u=t



8
u

= As +
-Ate->.(t-s) -e->.(u-s) Ate->.(t-s)
1:::



= As - e->.(t-s) + 1. (11.4.9)
Subtracting (11.4.9) from (11.4.8), we obtain in the case 81 > s that



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-498-0.png)

According to (11.4.9) with s = 0,
lE[- A(t A SI)] = 1,
e->.t which is strictly decreasing in t. Consequently, the integral (11.4.10) obtained
from the right-continuous integrand n[o,st) (t) is not a martingale. 0


11.4.2 Quadratic Variation
In order to write down the It6-Doeblin formula for processes with jumps, we
need to discuss quadratic variation. Let X(t) be a jump process. To compute
the quadratic variation of X on [0, T], we choose 0 = to < h < t2 < - · · <
tn = T, denote the set of these times by II = {to, h, . . .,tn}, denote the
length of the longest subinterval by III I = maxj(tj+l - tj), and define
n-1
Qrr(X) = L (X(tj+I) - X(tj)t
j=O
The quadratic variation of X on [0, T] is defined to be

[X, X](T) = lim Qrr(X),
IIITII--+0


480 1 1 Introduction to Jump Procees
where of course as II Jill -+ 0 the number of points in li must approach infinity.
In general, [X, X](T) can be random (i.e., can depend on the path of X).
However, in the case of Brownian motion, we know that [W, W](T) = T does
not depend on the path. In the case of an Ito integral I(T) = JT r(s)dW(s)
0
with respect to Brownian motion, [J, I](T) = J: T [2] (s)ds can depend on the
path because r( s) can depend on the path.
We will also need the concept of cross variation. Let XI(t) and X2(t) be
jump processes. We define
n-I
Cn(XI, X2) = L (XI(tj+l) - XI(ti)) (X2(ti+1) - X2(ti))

j=O
and



Theorem 11.4.7. Let XI(t) = XI(O) + h (t) + RI (t) + JI(t) be a jump pro­
cess, where II(t) = f� n(s) dW(s), RI(t) = f� BI(s) ds, and JI(t) is a right­
continuous pure jump process. Then Xl(t) = XI (0) + h (t) + RI (t) and




[XI> XI)(T) = [Xf, Xf)(T) + [Jl> JI](T) =
1



T

[XI> XI)(T) = [Xf, Xf)(T) + [Jl> JI](T) = rf(s) ds + L (LlJI(s)) [2] .
10 0<s:$T

(11.4.11)
Let X2(t) = X2(0) + l2(t) + R2(t) + J2(t) be another jump process, where
h(t) = f� T2(s) dW(s), R2(t) = f� 82(s) ds, and J2(t) is a right-continuous
pure jump process. Then Xi(t) = X2(0) + l2(t) + R2(t), and




[XI, X2)(T) = [Xf, Xil(T) + [JI, J2](T)



=
1



0 O<s:$T
n(s)r2(s) ds + L LlJI(s)Llh(s). (11.4.12)
T



PROOF:
We only need to prove (11.4.12) since (11.4.11) is the special case of
(11.4.12) in which x2 = XI. We have
n-I
Cn(XI, X2) = L (XI(tjH) - XI(ti)) (X2(ti+1) - X2(ti))



j=O
n-I
= L (Xf(tj+l) - xc(tj ) + JI(tj+I) - JI(tj ))



j=O



X (XHtj+l) - Xi{tj) + h(tj+l) - h [(t] j [)) ]


1 1 .4 Jump Processes and Their Integrals 481



n-1



=
(Xf(tj+l) - Xf(tj)) (Xi(tj+l) - Xi(tj))
j=O E
n-1
+ E (Xf(tj+I) - Xf(tj)) (J2(tj+l) - J2(tj))
j=O
n-1
+ j=O E (J1(tj+1) - J1(tj)) (Xi(tj+l) - Xi(tj))
n-1

j=O
We know from the theory of continuous processes that
n-1

=
lim (Xf(ti+d - Xf(tj)) (Xi{tj+l) - Xi(tj)) [XL Xi] (T)
III I-+0 L
j=O


=
1T n(s)H(s) ds.
We shall show that the second and third terms appearing on the right­
hand side of (11.4.13) have limit zero as lll l -+ 0, and the fourth term has
limit

[J1, J2](T) [= ] L1J1(s)L1J2(s).
L
O<s�T
We consider the second term on the right-hand side of (11.4.13):
n-1
(Xf(tj+l) - Xf(tj)) (J2(tj+l) - J2(tj))
j=O E
n-1

+ E (J1(ti+d - J1(tj)) (J2(tj+1) - h(tj)). (11.4.13)



O�J�n-1 J= . 0
::; �ax IXf(tj+l) - Xf(tj)l · L ih(tj+l) - J2(tj)l



::; O<J<n-1 �ax IXf(tj+l) - Xf(tj)l · L IL1J2( [s] ) [l] .
O<s�T
As lll l -+ 0, the factor maxo�j�n-1 IXf(tj+l) - Xf(tj)l has limit zero,
whereas Eo<s<T IL1J2(s)l is a finite number not depending on ll. Hence, the
second term on the right-hand side of (11.4.13) has limit zero as lll l -+ 0.
Similarly, the third term on the right-hand side of (11.4.13) has limit zero.
Let us fix an arbitrary w E fl, which fixes the paths of these processes, and
choose the time points in ll so close together that there is at most one jump of
J1 in each interval (ti, ti+l], at most one jump of J2 in each interval (tj, ti+1],
and if J1 and J2 have a jump in the same interval, then these jumps are
simultaneous. Let A1 denote the set of indices j for which (tj, t3+1] contains a

       -       

482 1 1 Introduction to Jump Processes
jump of J1, and let A2 denote the set of indices j for which (tj, ti+Il contains
a jump of J2. The fourth term on the right-hand side of (11.4.13) is
n-1
L (Jl(tj+l) - Jl(tj)) (h(tj+I) - h(tj))

[=]
j O


then


In particular,
dXf(t) dJ2(t) = dX2(t) dJ1 (t) = 0;
the cross variation between a continuous process and a pure jump process is
zero. It follows that the cross variation between a Brownian motion and a
Poisson process is zero.
More generally, the cross variation between two processes is zero if one of
them is continuous and the other has no Ito integral part. In order to get a
nonzero cross variation, both processes must have a dW term or the processes
must have simultaneous jumps. This means that the cross variation between
a Brownian motion and a compensated Poisson process is also zero. We state
this last fact as a corollary. 0

Corollary 11.4.9. Let W(t) be a Brownian motion and M(t) = N(t) - )t be
a compensated Poisson process relative to the same filtration :F(t) {Definition
11.4.1}. Then

[W, M](t) = 0, t 2 0.
PROOF: In Theorem 11.4.7, take h(t) = W(t), R1(t) = J1(t) = 0 and take
/2(t) [= ] 0, R2(t) [= ] ->-.t, and h(t) [= ] N(t). 0
We shall see in Corollary 11.5.3 that the equation [W, M](t) = 0 implies
that W and M are independent, and hence W and N are independent. A
Brownian motion and a Poisson process relative to the same filtration must
be independent.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-501-0.png)
11.5 Stochastic Calculus for Jump Processes

Corollary 11.4.10. For i = 1, 2, let Xi(t) be an adapted, right-continuous
jump process. In other words, Xi(t) = Xi(O) + Ii(t) + Ri(t) + Ji(t), where
Ii(t) = J; ri(s) dW(s), �(t) = J; Bi(s) ds, and Ji(t) is a pure jump process.
Let Xi(O) be a constant, let <Pi(s) be an adapted process, and set


where

483



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-502-0.png)









then


(11.5.1)
where r(s) and B(s) are adapted processes. In differential notation, we write


484 1 1 Introduction to Jump Processes



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-503-0.png)







We now add a right-continuous pure jump term J into (11.5.1), setting



X(t) [= ] X(O) + I(t) + R(t) + J(t),

= =
where I(t) J� r(s) dW(s) and R(t) J� 8(s) ds. As usual, we denote by
=
xc(t) X(O) + I(t) + R(t) the continuous part of X(t). Between jumps of J,
the analogue of (11.5.2) holds:



df(X(s)) [= ] !' (X(s)) dX(s) + �!" (X(s)) dX(s) dX(s)



=
!' (X(s))r(s) dW(s) + !' (X(s) )e(s) ds
1
+2!" (X(s))r [2] (s) ds



=
f'(X(s)) dXc(s) + �f"(X(s)) dXc(s) dXc(s). (11.5.3)
When there is a jump in X from X(s-) to X(s), there is typically also a
jump in f (X) from f (X ( s-)} to f (X ( s)}. When we integrate both sides of
(11.5.3) from 0 to t, we must add in all the jumps that occur between these
two times. This leads to the following theorem.

Theorem 11.5.1 (ItO-Doeblin formula for one jump process). Let
X(t) be a jump process and f(x) a function for which f'(x) and f"(x) are
defined and continuous. Then

t t
f(X(t)) [= ] f(X(O)) + f'(X(s)) dXc(s) + � f" (X(s)) dXc(s) dXc(s)
1 1
+ L [f(X(s)) - f(X(s-))] . (11.5.4)
O<s::;t


11.5 Stochastic Calculus for Jump Processes 485

PROOF: Fix w E J!, which fixes the path of X, and let 0 < r1 < T2 < - · · <
Tn-1 < t be the jump times in [0, t) of this path of the process X. We set
To [= ] 0, which is not a jump time, and Tn = t, which may or may not be a
jump time. Whenever u < v are both in the same interval (Tj, Tj+I), there
is no jump between times u and v, and the ltO-Doeblin formula (11.5.3) for
continuous processes applies. We thus have



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-504-0.png)

















+ L [f(X(TJ+d) - f(X(Tj+I-))],
j=O


486 1 1 Introduction to Jump Processes
which is (11.5.4). Note in this connection that if there is no jump at Tn = t,
then the last term in the sum on the right-hand side, f(X(rn)) -f(X(Tn-)),
is zero. 0
It is not always possible to rewrite (11.5.4) in differential form because it
is not always possible to find a differential form for the sum of jumps. We
provide one case in which this can be done in the next example.
Example 11. 5. 2 (Geometric Poisson process). Consider the geometric Poisson
process
S(t) = S(O) exp {N(t) log( a+ 1) - >at} = S(O)e-.Xut(a + 1) [N] (t), (11.5.6)
where a > -1 is a constant. If a > 0, this process jumps up and moves down
between jumps; if -1 < a < 0, it jumps down and moves up between jumps.
We show that the process is a martingale.
We may write S(t) = S(O)f(X(t)), where f(x) =e [x ] and

X(t) = N(t) log( a+ 1) - >at
has continuous part xc(t) = ->at and pure jump part J(t) = N(t) log( a+ 1).
According to the It6-Doeblin formula for jump processes,
S(t) = f(X(t))
= f(X(O)) - >a !' (X(u)) du + L [f(X(u)) - f(X(u-)}]
0
1t 0<u$t
(11.5.7)
0 O<u�t

If there is a jump at time u, then S(u) = (a+ 1)S(u-). Therefore,
S(u) - S(u-) = aS(u-) (11.5.8)
whenever there is a jump at time u, and of course S(u) -S(u-) = 0 if there
is no jump at time u. In either case, we have
S(u) -S(u-) = aS(u-)LlN(u).
This observation permits us to rewrite the sum on the right-hand side of
(11.5. 7) as

= S(O) - >a 1t S(u) du + L [S(u) - S(u-)] .



O<u�t O<u�t 0
L L

[S(u) - S(u-)] = aS(u-)LlN(u) =a 1tS(u-)dN(u).



It does not matter whether we write the Riemann integral on the right­
hand side of ( 11.5. 7) as J; S( u) du or as J; S( u-) du. The integrands in these


1 1 .5 Stochastic Calculus for Jump Processes 487
two integrals differ at only finitely many times, and when we integrate with
respect to du, these differences do not matter. Therefore, we may rewrite
(11.5. 7) as


S(t) = S(O) - S(u-) du + u S(u-) dN(u)
..\u 1 [t ] 1 [t ]

= S(O) + u S(u-) dM(u),
1 [t ]
where M is the compensated Poisson process M(u) = N(u) - ..\u, which is a
martingale. Because the integrand S( u-) is left-continuous, Theorem 11.4.5
guarantees that S(t) is a martingale.
In this case, the ltO-Doeblin formula (11.5.7) has a differential form,
namely,

dS(t) = uS(t-) dM(t) = -..\uS(t) dt + uS(t-) dN(t). (11.5.9)
We were able to obtain this differential form because in (11.5.8) we were able
to write the jump in /(X) (i.e., the jump in S) at time u in terms of f (X(u-))
(i.e., in terms of S(u-)). 0

Corollary 11.5.3. Let W(t) be a Brownian motion and let N(t) be a Pois­
son process with intensity ..\ > 0, both defined on the same probability space
(!2, :F, IP') and relative to the same filtration :F(t), t 0. Then the processes
;
W ( t) and N ( t) are independent.

KEY STEP IN PROOF: Let u1 and u2 be fixed real numbers and define

Y(t) = exp { u1 W(t) + u2N(t) - �u�t - ..\(eu [2 ]       - 1)t }·
We use the ltO-Doeblin formula to show that Y is a martingale.
To do this, we define
1
X(s) = u1 W(s) + u2N(s) - 2u�s - ..\(e [u2 ]        - 1)s
and f(x) = e [x], so that Y(s) = f (X(s)) . The process X(s) has Ito integral
part I(s) = u1 W(s), Riemann integral part R(s) = -!u�s - ..\(eu [2 ] - l)s, and
pure jump part J(s) = u2N(s). In particular,

1
dXc (s) = u1 dW(s) - 2u� ds - ..\(eu [2 ]  - 1) ds, dXc(s) dXc(s) = u� ds.
We next observe that if Y has a jump at time s, then


Therefore,


488 1 1 Introduction to Jump Processes
Y(s) -Y(s-) = (eu2 - 1)Y(s-)LlN(s).
According to the ItO-Doeblin formula for jump processes,
Y(t) = J(X(t))

+ L [J(X(s)) - f(X(s-))]
t
= f(X(O)) + f'(X(s)) dXc(s) +    - t J"(X(s)) dXc(s) dXc(s)
###### lo lo





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-507-0.png)





This is the product of the moment-generating function IEeu' [W] (t [) ] = exp { �urt}
for W(t) (see Exercise 1.6(i)) and the moment-generating function 1Eeu2 [N(t) ] =
exp { )t ( eu2 - 1) } for N ( t) (see ( 11.3.4)). Since the joint moment-generating
function factors into the product of moment-generating functions, the random
variables W(t) and N(t) are independent.
The corollary a erts more than the independence between N ( and W
t) ( t)
processes
for fixed t, saying that the N and W are independent (i.e., anything
depending only on the path of W is independent of anything depending only


1 1 .5 Stochastic Calculus for Jump Processes
on the path of N). For example, the corollary a erts that maxo<s<t W(s)
is independent of J; N ( s) ds. The first step in the proof of this st te ent is
;                        the one just given, which shows that the random variables W(t) and N(t) are
independent of each fixed t. The next step, which we omit, is to show that for
any finite set of times 0 : t1 < t2 < - · · < tn, the vector of random variables
.                      - .
(W(h), W(t2),, W(tn)) is independent of the vector of random variables
(N(h), N(h), . . ., N(tn)). The a ertion of the corollary follows from this. 0


11.5.2 ItO-Doeblin Formula for Multiple Jump Processes
There is a multidimensional version of the ItO-Doeblin formula for jump pro­
cesses. We give the two-dimensional version. The formula for higher dimen­
sions follows the same pattern.
Theorem 11.5.4 (Two-dimensional ItO-Doeblin formula for processes
with jumps). Let X1 (t) and X2(t) be jump processes, and let f(t, X1, x2) be
a function whose first and second partial derivatives appearing in the following
formula are defined and are continuous. Then
f(t, X1(t), X2(t))

t

=
f(O, X1(0), X2(0)) + lo ft(s, X1(s), X2(s)) ds

489



t t
+ lo fx, (s, X1 (s), X2(s)) dXf(s) + lo fx2 (s, X1 (s), X2(s)) dX2(s)



t
+ fx,,x, (s, X1 (s), X2(s)) dXf(s) dXf(s)
�lo



t
+ lo fx,,x2 (s, Xl(s), X2(s)) dXf(s) dX2(s)



t
+�lo fx2,x2 (s, X1 (s ), X2(s)) dX2(s) dX2(s)



+ L [f(s, X1(s), X2(s)) - f(s, X1(s-), X2(s-))] .
0<s$t
Corollary 11.5.5 (Ito's product rule for jump processes). Let X1(t)
and X2(t) be jump processes. Then

t t

=
X1(t)X2(t) X1(0)X2(0) + X2(s) dXf(s) + X1(s) dX2(s)
lo lo

+ (Xf, X2] (t) + L [X [1] (s)X2(s) - X1(s-)X2(s-)]

t t
=
X1(0)X2(0) + X2(s-) dX1(s) + X1(s-) dX2(s)
lo lo
+[X [1], X2](t). (11.5.11)


490 1 1 Introduction to Jump Processes


(11.5.12)


=

L
+ [X2(s-)LlX1(s) + X1(s-)LlX2(s) + LlX1(s)LlX2(s)].
0<s$t
(11.5.13)
We have also used the fact that the jumps in Xi(t) are the same as the jumps
in Ji(t). It remains to show that this last sum is the same as the sum

L

[X1(s)X2(s) -X1(s-)X2(s-)]
O<s::;t
in the second line of (11.5.11). We expand the typical term in the sum in the
second line of (11.5.11):



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-509-0.png)
1 1 .5 Stochastic Calculus for Jump Processes 491


X1(s)X2(s) - X1(s-)X2(s-)
= (X1(s-) + LlX1(s)) (X2(s-) + LlX2(s)) - X1 (s-)X2(s-)
= X1 (s-)X2(s-) + X1 (s-)LlX2(s) + LlX1 (s)X2(s-) + LlX1 (s)LlX2(s)
-X1(s-)X2(s-)
= X1(s-)LlX2(s) + LlX1(s)X2(s-) + LlX1(s)LlX2(s).
This is the typical term in the sum appearing at the end of (11.5.13). 0
For stochastic calculus without jumps, Girsanov's Theorem tells us how
to change the measure using the Radon-Nikodym derivative process

t t
Z(t) = exp { - 1 F(s) dW(s) - � 1 F [2] (s) ds }·
This process satisfies the stochastic differential equation
dZ(t) = -F(t)Z(t) dW(t) = Z(t) dXc(t),
where xc(t) = - I� r(s) dW(s) and [xc, xc](t) = I� F [2] (s) ds. We may
rewrite Z(t) as
(11.5.14)


Therefore,


(11.5.16)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-510-0.png)
492 1 1 Introduction to Jump Processes

PROOF: We may write X(t) as X(t) = Xc(t) + J(t), where


(11.5.17)

is the continuous part of X and J(t) is the pure jump part. We define

t t t
Y(t) [= ] exp {1 r(s) dW(s) + 1 8(s) ds - � 1 T2(s) ds}

(11.5.18)

From the It6-Doeblin formula for continuous processes, we know that
dY(t) [= ] Y(t) dXc(t) [= ] Y(t-) dXc(t). (11.5.19)

=
We next define K(t) 1 for t between 0 and the time of the first jump of
X, and we set

=
K(t) IJ (1 + LlX(s)) (11.5.20)

for t greater than or equal to the first jump time of X. The process K(t) is a
=
pure jump process, and z [x ] (t) Y(t)K(t). If X has a jump at time t, then
=
K(t) K(t-)(1 + LlX(t)). Therefore,
LlK(t) [= ] K(t) - K(t-) [= ] K(t-)LlX(t). 11.5.21
( )

=
Because Y(t) is continuous and K(t) is a pure jump process, [Y, K](t) 0.
We now use Ito's product rule for jump processes to obtain

t t
r(s) dW(s) + 8(s) ds
1
=
xc(t)
1


=
exp { xc(t) - [xc, xc](t) .
              - }



z [x ] (t) = Y(t)K(t)



t t

=
Y(O) + K(s-) dY(s) + Y(s-) dK(s)
1 1



t

=
1 + Y(s-)K(s-) dXc(s) + L Y(s-)K(s-)LlX(s)
10 0<s$t



t

=
1 + Y(s-)K(s-) dX(s)
1



t

=
1 + 1 z [X ] (s-) dX(s). (11.5.22)
This is (11.5.16). 0



11.6 Change of Measure
Just as we can use Girsanov's Theorem to change the measure so that a
Brownian motion with drift becomes a Brownian motion without drift, we


1 1.6 Change of Measure 493
can change the measure for Poisson processes and compound Poisson pro­
cesses. For a Poisson process, the change of measure affects the intensity. For
a compound Poisson process, the change of measure can affect both the in­
tensity and the distribution of the jump sizes. We treat these two situations
in the next two subsections, and in the third subsection we also include a
Brownian motion component in the process under consideration.


11.6.1 Change of Measure for a Poisson Process
Let N(t) be a Poisson process on a probability space (!I, :F, IP') relative to a
filtration :F(t), t ?: 0. We denote the intensity of N(t) by A, a positive constant
= =
(i.e., JEN(t) At). The compensated Poisson process M(t) N(t) - At is a
martingale under lP' (Theorem 11.2.4). Let .X be a positive number. We define


(11.6.1)


=


.X
1 + L\X(t) = �Therefore, the process in (11.6.1) may be written as

Z(t) = exp {Xc(t) - �[Xc,xc](t)} IT (1 + L\X(s)).
O<s::;t
We see from this formula that Z(t) is the Doleans-Dade exponential zx (t) of
Corollary 11.5.6. In particular,

Z(t) = 1 Z(s-) dX(s).
+lo [t ]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-512-0.png)
494 1 1 Introduction to Jump Processes
Since X is a martingale and Z(s-) is left-continuous, Z(t) is a martingale.
Because Z(t) is a martingale and Z(O) = 1, we know that JEZ(t) 1 for all
###### t � 0. = 0

We may now fix a positive time T and use Z(T) to change the measure.
We define
P(A) = Z(T) dlP for all A E F. (11.6.3)
i

Theorem 11.6.2 (Change of Poisson intensity). Under the probability
measure P, the process N(t), 0 : t : T, is Poisson with intensity .X.

KEY STEP I N PROOF: We compute the moment-generating function of N(t)
under P. For 0 : t : T, we can change the iE expectation of euN [(] t) to the lE
expectation by using Z(t) as the Radon-Nikodym derivative rather than Z(T)
(see Lemma 5.2.1). Using the formula for Z(t) and the moment-generating
function formula (11.3.4), we obtain



N(t)
lE [euN(t) Z(t) = e<A-5.)t lE euN(t)
(�)
]
### [ l



= e<A-5.)t )t eu+log(5./ A) - 1

= e<A-5.)t lE exp u + log N(t)

          ### [ { ( ) }]



= e<A-5.)t exp )t eu+log(5./ A) - 1
{ ( )}



= exp { .Xt(eu - 1)
},
which is the moment generating function for a Poisson process with intensity
.X (see again (11.3.4)). 0
Example 11.6.3. Consider a stock modeled as a geometric Poisson process

where a > -1, a =f. 0, and N(t) is a Poisson process with intensity ) under
the actual probability measure IP'. We saw in Example 11.5.2 that e [-] ats(t) is
a martingale under IP', and hence S(t) has mean rate of return a. Indeed, in
place of (11.5.9), we now have

dS(t) = aS(t) dt + aS(t-) dM(t), (11.6.4)
where M(t) is the compensated Poisson process M(t) N(t) - .>.t. We would
like to change to a probability measure P under which =
dS(t) = rS(t) dt + aS(t-) dM(t), (11.6.5)
where r is the interest rate, N(t) is a Poisson process with intensity .X under

=
P, and M(t) N(t) - .Xt is a compensated Poisson process under P. Then,

S(t) = S(O) exp {at + N(t) log( a + 1) - .>.at} = S(O)e<a-Au)t(a + 1)N(t),


1 1 .6 Change of Measure 495
under IP', the geometric Poisson process would have mean rate of return equal
to the interest rate, and iP would be the risk-neutral measure.
To accomplish this, we note that the "dt" term in (11.6.4) is



(a               - Aa)S(t) dt
(recall that dM(t) = dN(t) - Adt) and the "dt" term in (11.6.5) is



(11.6.6)



(r                  - 5.a)S(t) dt. (11.6.7)

(Here again we are using the fact that S(t-) dt and S(t) dt have the same
integrals, and we can thus use them interchangeably.) We set (11.6.6) and
(11.6.7) equal and solve for

                    - a - r
A = A - -- .
CT
We then change to the risk-neutral measure by formula (11.6.3) with Z(T)
defined by (11.6.1).
to [To make the change of measure, we must have ] a - r [>. ][> 0, ][which is equivalent ]

A > --. (11.6.8)
CT
If condition (11.6.8) does not hold, then there is no risk-neutral measure and
hence there must be an arbitrage. Indeed, if a > 0 and (11.6.8) fails, then


r
and borrowing at the interest rate to invest in the stock is an arbitrage.
If -1 < a < 0, the inequalities are reversed and the arbitrage consists of
D
shorting the stock to invest in the money market account.


11.6.2 Change of Measure for a Compound Poisson Process
Let N(t) be a Poisson process with intensity A, and let Y1, Y2, . . . be a se­
quence of identically distributed random variables defined on a probability
space (!l, F, IP'). We a ume the random variables Y1, Y2, . . . are independent
of one another and also independent of the Poisson process N(t). We define
the compound Poisson process
N(t)
Q(t) = L }i. (11.6.9)
i=l
Note for future reference that if N jumps at time t, then Q jumps at time t
and
LlQ(t) = YN(t)· (11.6.10)


496 1 1 Introduction to Jump Processes
Our goal is to change the measure so that the intensity of N(t) and the
distribution of the jump sizes Y1, Y2, . . . both change. We first consider the
case when the jump-size random variables have a discrete distribution (i.e.,
each Yi takes one of finitely many possible nonzero values Y1, Y2, . . ., YM ). Let
p(ym) denote the probability that a jump is of size Ym=

P(Ym) = IP'{Yi = Ym}, m [= 1], . . ., M.
This does not depend on i since Y1, Y2, . . . are identicall� distributed. We
a ume that p(ym) > 0 for every m and, of course, that Lm=l P(Ym) = 1.
Let Nm(t) denote the number of jumps in Q(t) of size Ym up to and
including time t, so that
M M
N(t) = L Nm(t) and Q(t) = L YmNm(t).
m=l m=l

.                                                 -                                                 According to Corollary 11.3.4, N1,, N M are independent Poisson processes
and each Nm has intensity Am = Ap(ym)·
Let 5.1, . . ., >.M be given positive numbers, and set



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-515-0.png)
11.6 Change of Measure 497
Once again, the integrators are martingales and the integrands are left­
continuous. Therefore, Z1Z2Z3 is a martingale. Continuing this process, we
eventually conclude that Z(t) = Z1(t)Z2(t) · · · Zm(t) is a martingale. 0
Fix T > 0. Because Z(T) > 0 almost surely and JEZ(T) = 1, we can use
Z(T) to change the measure, defining



P(A) = Z(T) dP for all Z E F.
L



Theorem 11.6.5 (Change of compound Poisson intensity and jump
distribution for finitely many jump sizes). UnderP, Q(t) is a compound
Poisson process with intensity >. = E!:=l >.m, and Yi, Y2, . . . are independent,
identically distributed random variables with



( 6 4)
11. .1



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-516-0.png)

KEY STEP



lE



Nm(<)









According to (11.3.5), this is the moment-generating function for a compound
Poisson process with intensity >. and jump-size distribution (11.6.14). 0


498 1 1 Introduction to Jump Processes
The Radon-Nikodym derivative process Z(t) of (11.6.11) may be written
as



M          - _ Nm(t) N(t) [-] _
M
### {



=




derivative process

=

11.6.7 below.


JEZ(t) [= ] 1 for all t 2 0.

=



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-517-0.png)



(recall (11.6.10))
### Q,



and hence
### Q.



(11.6.17)


(11.6.18)







for which


1 1 .6 Change of Measure 499



(11.6.19)



Because





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-518-0.png)

orem 11.3.1 with {3 = �). We may rewrite (11.6.17) as
LlJ(t) = J(t-)LlH(t) - J(t-)LlN(t), (11.6.20)
and because all these terms are zero if there is no jump at t, this equation
holds at all times t, not just at the jump times of Q. Because J, H, and N
are all pure jump processes, we may also write (11.6.20) as

dJ(t) = J(t-) dH(t) - J(t-) dN(t).
Because J(t) is a pure jump process and e<>.- [5.] )t is continuous, the cross
variation between these two processes is zero. Therefore, Ito's product rule
for jump processes (Corollary 11.5.5) implies that Z(t) = e<>.- [5.] )tJ(t) may be
written as
Z(t) = Z(O) + t J(s-)(>. - 5.)e<>.-5.)s ds + t e<>.-5.)s dJ(s)
1 1



=
1 + t e<>.-5.)s J(s-)(>. - 5.) ds + t e<>.-5.)s J(s-) dH(s)
1 1




- e< [>.-5.)] s J(s-) dN(s)
lo [t ]



= 1 + t e<>.-5.)sJ(s-) d(H(s) - :Xs) - t e<>.-5.)sJ(s-) d(N(s) - >.s)
1 1



= 1 [+ ] Z(s-) d(H(s) - :Xs) - Z(s-) d(N(s) - >.s). (11.6.21)
1 [t ] lo [t ]



Theorem 11.4.5 implies that Z(t) is a martingale. Since Z(t) is a martingale
and Z(O) = 1, we have IEZ(t) = 1 for all t. 0
For future reference, we rewrite (11.6.21) in the differential form
dZ(t) = Z(t-)d(H(t) - 5.t) - Z(t-)d(N(t) - >.t).
This equation implies
LlZ(t) = Z(t-)LlH(t) - Z(t-)LlN(t). (11.6.22)


500 1 1 Introduction to Jump Proce es
Fix a positive T and define



P(A) = Z(T) diP' for all A E :F. (11.6.23)
i



Theorem 11.6.7 (Change of compound Poisson intensity and jump
distribution for a continuum of jump sizes). Under the probability
measure P, the process Q(t), 0 ::; t � T, of {11.6.9} is a compound Poisson
process with intensity 5 Furthermore, the jumps in Q(t) are independent and
identically distributed with density J(y).

KEY STEP IN PROOF: We need to show that, under P, the process Q(t)
has the moment-generating function corresponding to a compound Poisson
process with intensity 5. and jump density J(y). In other words, we must
show that (see (11.3.2))

(11.6.24)
where
(11.6.25)
We define

and hence

(11.6.26)

fEeuQ(t) = exp >.t(cPy(u) - 1) },
{



(11.6.26)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-519-0.png)



Because










1 1 .6 Change of Measure 501
where H(t), defined by (11.6.18), satisfies (11.6.19) at jump times of Q.
Because X(t) and Z(t) have no Ito integral components, (11.6.26), (11.6.22),
and (11.6.27) imply



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-520-0.png)


       - L X(s-)Z(s-)(eu<lQ [(s) ]       - 1) . (11.6.28)
0<s$t
We have omitted LlN(s) in the last term because it is always either 1 or 0,
and when it is zero, eu<lQ( [s) ] - 1 is also zero. In other words,
( [eu] <lQ [(s) ]               - [1] )LlN(s) [= ] ( [eu] <lQ [(s) ]               - 1) .
We use Ito's product rule for jump processes to write
X(t)Z(t) = 1 + X(s-)dZ(s) + Z(s-)dX(s) + [X,Z](t).
###### 1 [t ] 1 [t ]
We show that the right-hand side is a martingale under JP. The integral
J� X(s-) dZ(s) is a martingale because the integrand is left-continuous and Z
is a martingale. We examine the two other terms, using (11.6.26) and (11.6.28):
Z(s-) dX(s) + [X, Z](t)
###### 1 [t ]



= 0 t Z(s-)dXc(s) + 0<s$t L Z(s-)LlX(s) + [X,Zj(t)
###### 1



0 O<s$t
+ L X(s-)Z(s-)LlV(s) - L X(s-)Z(s-)LlH(s)
0<s$t 0<s$t

  - L X(s-)Z(s-)(eu<lQ [(s) ]  - 1)
0<s$t
= -5.(cP'y(u) - 1 t X(s-)Z(s-)ds + L X s- Z s- eu<lQ(s) - 1
) ( ) ( )( )
###### 1



= X(s-)Z(s-)d(V(s) - 5.scP'y(u)ds) - X(s-)Z(s-)d(H(s) - 5.s) .
###### lo [t ]
1t
This is a martingale because the processes V(t) - 5.tcpy(u) and H(t) - >.t are
martingales and the integrands are left-continuous.


502 1 1 Introduction to Jump Processes
We can now prove (11.6.24). Using Lemma 5.2.1, we may write

=
E[eu [Q] (t)) IE[eu [Q] (t) Z(t)] . (11.6.29)
But the martingale X(t)Z(t) has constant expectation 1, which implies



1 [= ] IE[X(t)Z(t))


=
exp { - 5.t(cP'y(u) - 1) } · IE[eu [Q] ( [t) ] Z(t)] .
Combining (11.6.29) and (11.6.30), we obtain (11.6.24).



(11.6.30)

D



11.6.3 Change of Measure for a Compound Poisson Process and a
Brownian Motion
Suppose now that we have a probability space (!l, F, JP) on which is defined
a Brownian motion W(t). Suppose that on this same probability space there
is defined a compound Poisson process
N(t)
Q(t) [=] Yi
I:
i=l
as in (11.3.1) with intensity A and jumps having density function f(y). We
a ume there is a single filtration F(t), t 0, for both the Brownian motion
2:
and the compound Poisson process. In this case, the Brownian motion and
compound Poisson process must be independent. (See Corollary 11.4.9 for the
case of a Brownian motion and a Poisson process. The case of a Brownian
motion and a compound Poisson process is Exercise 11.6.)
Let 5. be a positive number, let J(y) be another density function with
= =
the property that J(y) 0 whenever f(y) 0, and let 6l(t) be an adapted
process. We define



Z1 (t) [= ] exp { - 6l(u) dW(u) - � 6l [2] (u) du,
###### 1 [t ] 1 [t ] }

        N(t [) ]         z 2 (t) [= ] e [<.X] - [X)t ] IT [AJ(Yi) ]
i=l [Af(Yi) ' ]
Z(t) [= ] Z1 (t)Z2(t).



(11.6.31)


(11.6.32)


(11.6.33)



Lemma 11.6.8. The process Z(t) of {11.6.33} is a martingale. In particular,
=
IEZ(t) 1 for all t 0.
2:
PROOF: We know from stochastic calculus for continuous processes that Z1(t)
is a martingale and from Lemma 11.6.6 that Z2(t) is a martingale. Since Z1(t)
is continuous and Z2(t) has no Ito integral part, [Z1, Z2](t) [= ] 0. Ito's product
rule for jump processes thus implies


11.6 Change of Measure 503


and (11.6 30) implies
.

lE [ [eu2Q(t) ] Z2(t)] [= ] exp { 5.t(cpy [( ][u] 2 [) ]

                       - [1] )}.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-522-0.png)
504 1 1 Introduction to Jump Processes
Equation (11.6.35) follows.
The surprising fact is that (11.6.35) and hence the conclusion of Theorem
11.6.9 hold even if 8(t) is allowed to depend on Q(t). Indeed, we could have
8(t) equal to Q(t). We give the proof of this fact.

PROOF OF (11.6.35): We define

martingales under IP'.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-523-0.png)



=



=



=





follows that



this gives us (11.6.35). 0


11.7 Pricing a European Call in a Jump Model 505
Suppose a compound Poisson process Q( t) has jumps Y1, Y2, . . . that take
so that p(ym) - 0 and L:�=l Pm 1. Let 5. be a positive constant and let
=
p(yi), [.] . .,p(yM) be positive numbers that sum to 1. In place of (11.6.32), we
now define _
N(t) Z2(t) e< [A]              - [X)] t
= IT [Ap(Yi) ]
i=l [Ap(Yi) ]
and then define Z(t) by (11.6.33). Lemma 11.6.8 still applies and permits us
to define the probability measure iP' by the formula P(A) = fA Z(T) diP' for all
Z E F. A straightforward modification of the proof of Theorem 11.6.9 gives
the following result.

Theorem 11.6.10. Under the probability measure iP', the process

W(t) W(t) + 6l(s) ds
=
###### 1 [t ]

is a Brownian motion, Q(t) is a compound Poisson process with intensity >.

=
and independent, identically distributed jump sizes satisfying P{Yi Ym}
=
p(ym) for all [i ] and [m ] [= ] [1], . . ., M, and the processes W(t) and Q(t) are
independent.


1 1 . 7 Pricing a European Call in a Jump Model

In this section, we consider the problem of pricing a European call when the
underlying a et is a jump process. We work out the details for two cases:
(1) the underlying a et is driven by a single Poisson process, and (2) the
underlying a et is driven by a Brownian motion and a compound Poisson
process. The market is complete in the first case and incomplete in the second.
We discuss the nature of the incompleteness in the second case.

only finitely many nonzero values Y1, Y2, . . ., YM, with P(Ym) IP'{Yi Ym}
= =



11.7.1 Asset Driven by a Poisson Process
We return to Example 11.6.3, in which the underlying a et price is given by
S(t) [= ] S(O) exp {at + N(t) log( a + 1) - -\at}

(11.7.1)

for which the differential is
dS(t) aS(t) dt + aS(t-) dM(t).
=

In this model, N(t) is a Poisson process with intensity,\ > 0 on a probability
space (fl, :F, IP'), and M(t) N(t) - At is the compensated Poisson process.
=

= S(O)e<a-M)t(a + 1)N(t) '


506 1 1 Introduction to Jump Processes
We fix a positive time T and wish to price a European call whose payoff at
time T is
=
V(T) (S(T) -K) [+] .



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-525-0.png)







We have
S(T) = S(O)e [(] r- [>.] u [)] t(a + 1) [N] (t) . e<r->.u)(T-t)(a + 1)N(T)-N(t)
= S(t) . e<r->.u [)] (T-t)(a + 1)N(T)-N(t).
It follows that

_
= +
iE[e-r(T-t) ( S(t)e(r->.u)(T-t)(a 1)N(T)-N(t) K) +'F(t) .
]
=
V(t) E[e-r(T-t) (S(T) - KtiF(t)]


1 1.7 Pricing a European Call in a Jump Model 507


The random variable S(t) is .F(t)-measurable, whereas
e [<] r- [5.u)(] T- [t)] (a + 1) [N(] T [)]             - [N(t) ]

is independent of F(t). According to the Independence Lemma, Lemma 2.3.4,

V(t) = c t, S(t),
( )



where



+
c(t, = jE (a + _ K
x) e-r(T-t) xe<r-5.u)(T-t) 1)N(T)-N(t)





![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-526-0.png)



(11.7.3)



condition



is a martingale under JP. Therefore, we compute d c(t, S(t)) and set the
(e-rt )
"dt" term equal to zero. The stochastic differential equation (11.7.2) may be
rewritten as
dS(t) = (r          - Xa)S(t) dt + aS(t-) dN(t), (11.7.5)
which shows that the continuous part of the stock price satisfies

dSc(t) = (r             - Xa)S(t) dt.

On the other hand, if the stock price jumps at time t, then

LlS(t) = S(t) - S(t-) = aS(t-), S(t) = (a + 1)S(t-).

The ItO-Doeblin formula implies


508 1 1 Introduction to Jump Processes
e-r [t] c(t, S(t))



= c(O, S(O)) + e [-] ru [ - rc(u, S(u)) du + Ct(u, S(u)) du
###### 1 [t ]
+cx(u, S(u)) dSc(u)]
+ L e [-] ru [c(u, S(u)) - c(u, S(u-))]
0<u$t



= c(O, S(O)) + e [-] ru [- rc(u, S(u)) + Ct(u, S(u))
###### 1 [t ]
+(r- >:a)S(u)cx(u, S(u))] du
+ 1t e [-] ru [c(u, (a+ 1)S(u-)) -c(u, S(u-))] dN(u)



= c(O, S(O)) + e-ru [-rc(u, S(u)) + Ct(u, S(u))
###### 1 [t ]
+(r->:a)S(u)cx(u, S(u))] du
+ e [-] ru [c(u, (a+ 1)S(u-)) -c(u, S(u-))]>: du
###### 1 [t ]
+ e [-] ru[c(u,(a+ 1)S(u-)) - c(u,S(u-))] dM(u).
###### 1 [t ]



However, the integral
e [-] ru [c(u, (a+ 1)S(u-)) - c(u, S(u-))] ); du
###### 1 [t ]



is the same as the integral
e [-] ru [c(u, (a+ 1)S(u)) - c(u, S(u))]); du.
###### 1 [t ]



We have shown that
e-r [t] c(t, S(t))



= c(O, S(O))

+>:(c(u, (a+ 1)S(u)) -c(u, S(u)))] du
+ e [-] ru [c(u, (a+ 1)S(u-)) -c(u, S(u-))] dM(u). (11.7.6)
###### 1 [t ]
+ t e-ru [-rc(u, S(u)) + Ct(u, S(u)) + (r- >:a)S(u)cx(u, S(u))
###### 1



The last integral is a martingale because the integrator is a martin­
M(u)
gale and the integrand is left-continuous. Because left-hand side of
(11.7.6),
is also a martingale we can then solve for
e-rtc(t, S(t)),


11. 7 Pricing a European Call in a Jump Model 509



c(O, S(O)) + e-ru [ - rc(u, S(u)) + Ct(u, S(u)) + (r - �u)S(u)cx(u, S(u))
###### lo [t ]



+�(c(u, (u + 1)S(u)) - c(u, S(u)))] du



and see that it is the difference of two martingales and hence is itself a mar­
tingale. This can only happen if the integrand is zero:

-rc(t, S(t)) + Ct(t, S(t)) + (r - �u)S(t)cx(t, S(t))
+�(c(t, (u + 1)S(t)) - c(t, S(t))) 0. (11.7.7)
=

The way we have in the past argued for (11.7.7) using (11.7.6) (see the dis­
cussion preceding Theorem 6.4.3) is by first taking the differential in (11.7.6)
to obtain

d(e-rtc(t, S(t)))
= e-rt [ - rc(t, S(t)) + Ct(t, S(t)) + (r - �u)S(t)cx(t, S(t))
+�(c(t, (u + 1)S(t)) - c(t, S(t)))] dt
+e-r [t ] [c(t, (u + 1)S(t-)) - c(t, S(t-))) dM(t)

and then setting the dt term equal to zero. This still works, provided we make
sure the non-dt term has a martingale integrator, and if this integrator has
jumps, then the integrand for this martingale is left-continuous. In particular,
we also have

d(e-rtc(t, S(t)))
= e-rt [ - rc(t, S(t)) + ct(t, S(t)) + (r - �u)S(t)cx(t, S(t))] dt
+e-r [t ] [c(t, (u + 1)S(t-)) - c(t, S(t-))) dN(t), (11.7.8)

but setting the "dt" term

e-rt [ - rc(t, S(t)) + Ct(t, S(t)) + (r - �u)S(t)cx(t, S(t))] dt

in this expression equal to zero gives an incorrect result because the non-dt
term has integrator dN(t) and N(t) is not a martingale.
We conclude by replacing the stock price process S(t) in (11.7.7) by a
dummy variable x. This gives the equation

-rc(t, x)+ct(t, x)+(r-�u)xcx(t, x)+�(c(t, (u+1)x) -c(t, x)) = 0, (11.7.9)

which must hold for 0 - t < T and x ; 0. This is sometimes called a
differential-difference equation because it involves c at two different values
of the stock price, namely x and (u + 1)x. The function c(t, x) defined by
(11.7.3) satisfies this equation because, by its construction, e-rtc(t, S(t)) is a
martingale under JP>.


510 11 Introduction to Jump Processes


Returning to (11.7.6) and using equation (11.7.9), we see that for 0 : t :
T,

e-rtc(t, S(t))

= c(O, S(O)) + e-ru [c(u, (a + 1)S(u-)) - c(u, S(u-))] dM(u). (11.7.10)
###### lo [t ]

In particular,



e-r [T] (S(T) - K) [+ ]



e [-] r [T] c(T, S(T))
=



c(O, S(O)) + e [-] ru[c(u, (a + 1)S(u-)) - c(u, S(u-))] dM(u). (11.7.11)
=
###### lo [T ]



We use this observation to construct the hedge for a short position in the call.
Suppose we sell the call at time zero in exchange for initial capital X(O)
=
c(O, S(O)). We want to invest in the stock and money market account so that
X(t) c(t, S(t)) for all t or, equivalently,
=



e-rtx(t) e-rtc(t, S(t)) for all t E [O,T].
=



To accomplish this, we match differentials. From (11.7.10), we see that the
differential of e-rtc(t, S(t)) is

d(e [-] r [t] c(t, S(t))) e [-] r [t ] [c(t, (a + 1)S(t-)) - c(t, S(t-))] dM(t). (11.7.12)
=

The differential of the value X(t) of a portfolio that at each time t holds r(t)
shares of stock (we use r(t) rather than L\(t) to denote the number of shares
of stock held in the hedging portfolio to avoid confusion with the use of L\ as
the size of the jump in a process) is


=
dX(t) r(t-) dS(t) + r[X(t) - r(t)S(t)] dt.

Therefore,

d( e [-] r [t ] X(t)) e [-] r [t] [-r X(t) dt + dX(t)]
=
e [-] r [t] [r(t-) dS(t) - rr(t)S(t) dt]



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-529-0.png)
1 1.7 Pricing a European Call in a Jump Model 511


This is the hedging position we should hold at all times, whether they are
jump times or not. More specifically, if we define



t
aS(t)

then (11.7.14) will also hold and integration of (11.7.13) yields

a t E,,
r( ) = c(t, (a + 1)S(t)) - c(t, S(t)) II [O T]



(11.7.15)



e-rt X(t)



= X(O) + e-ru [c(u, (a + 1)S(u-)) - c(u, S(u-))] dM(u). (11.7.16)
###### 1 [t ]



Comparison of (11.7.10) with (11.7.16) shows that X(t) = c(t, S(t)) for all t.
In particular, (11.7.11) shows that X(T) = (S(T) - Kt; the short position
in the European call has been hedged.
Remark 11. 7. 1 {Sanity check). To convince ourselves that the hedge (11.7.15)
really works, we consider separately the cases when the stock jumps at time
t and when the stock does not jump at time t. In the event of a jump, the
change in the option price is c(t, (a + 1)S(t-)) - c(t, S(t-)). The change in
the hedging portfolio value is

r(t-) (S(t) - S(t-)} = r(t-)aS(t-) = c(t, (a + 1)S(t-)) - c(t, S(t-)),

which agrees with the change in the option price.
On the other hand, if the stock price does not jump at time t, then the
stock price follows equation (11.7.5) without the dN(t) term at time t:

dS(t) = (r - 5;a)S(t) dt.

At this time, (11.7.8) shows that the discounted option price has the differen­
tial

d(e [-] r [t] c(t, S(t))}
= e [-] r [t ] [ - rc(t, S(t)) + Ct (t, S(t)) + (r - 5;a)S(t)cx(t, S(t))] dt


where we have used the differential-difference equation (11.7.9) to obtain the
second equality. The differential of the discounted portfolio value at this time
is (from (11.7.13) without the dN(t) term implicit in dM(t))

d(e [-rt ] X(t)} = e -r [t] ar(t)S(t)( _); dt)

= -e [-] r [t] .>;[c(t, (a + 1)S(t)) - c(t, S(t))] dt.

Once again, the discounted portfolio value tracks the discounted option price.
0

= -e-rt); [c(t, (a + 1)S(t)) - c(t, S(t))] dt,


512 11 Introduction to Jump Processes


Remark 11.7.2 (Completeness). In this subsection, we have constructed the
price and hedge for a European call on a stock driven by a single Poisson
process. It is clear from the analysis that this same argument would work
for an arbitrary European derivative security with payoff h(S(T)) at time T
written on a stock modeled this way. One could simply replace the call payoff
by the function h in equation (11.7.3). The differential-difference equation
(11.7.9) would still apply, although now with terminal condition c(T, x) = h(x)
replacing (11.7.4), and the hedging formula (11.7.15) would still be correct.
The model is complete and the risk-neutral measure is unique if and only
if every derivative security can be hedged (Second Fundamental Theorem of
Asset Pricing, Theorem 5.4.9). "Every" derivative security means also those
derivative securities that are path-dependent. We have not considered path­
dependent derivative securities in this subsection, but one can show that they
also can be hedged, and thus the model is complete.


11.7.2 Asset Driven by a Brownian Motion and a Compound
Poisson Process


Let ( n, .1", IP') be a probability space on which is defined a Brownian motion
W(t), 0 - t - T, and M independent Poisson processes N1 (t), . . ., N M(t),
0 � t � T. Let F(t), 0 � t � T, be the filtration generated by the Brownian
motion and the M Poisson processes.
Let Am > 0 be the intensity of the mth Poisson process and let -1 < Y1 <

     
- · < YM be nonzero numbers. Set
M M
N(t) = L Nm(t), Q(t) [= ] L YmNm(t).
m=l m=l

Then N is a Poisson process with intensity A = L!:=l Am and Q is a com­
pound Poisson process. Let Yi denote the size of the ith jump of Q. Then
the Yi random variables take values in the set {y1, . . ., YM }, and Q(t) can be
written as
N(t)
Q(t) = 2 }'i.
i=l
Define
Am
P Ym) ( [= ] T"
The random variables Y1, Y2, . . . are independent and identically distributed,
with IP'{Yi = Ym} = p(ym)· These a ertions all follow from Theorem 11.3.3.
Set
M
1 [M ]
f3 [= ] lE}'i [= ] L YmP(Ym) [= ]             - L AmYm· (11.7.17)
m=l m=l
According to Theorem 11.3.1,


11.7 Pricing a European Call in a Jump Model 513
M
Q(t) - {3>t = Q(t) - t L: AmYm
m=l
is a martingale.
In this subsection, the stock price will be modeled by the stochastic dif­
ferential equation

dS(t) = o:S(t) dt + aS(t) dW(t) + S(t-)d(Q(t) - {3>t)
= (a: - {3>)S(t) dt + aS(t) dW(t) + S(t-) dQ(t). (11.7.18)

Under the original probability measure IP', the mean rate of return on the stock
is a:. The a umption that Yi > -1 for i = 1, . . ., M guarantees that although
the stock price can jump down, it cannot jump from a positive to a negative
value or to zero. We begin with a positive initial stock price S(O), and the
stock price is positive at all subsequent times; see (11.7.19) below. If S(O) = 0,
then S(t) = 0 for all t.

Theorem 11.7.3. The solution to {11. 7.18} is

N(t)
1
S(t) [= ] S(O) exp aW(t) + (3> t (Yi + 1). (11.7.19)
{ a: -          - 2a [2] } II
i=l
( )

PROOF:
We show that S(t) defined by the right-hand side of (11.7.19) satis­
fies the stochastic differential equation (11.7.18). Toward this end, define the
continuous stochastic process


and the pure jump process

N(t)
J(t) = II (Yi + 1).
i=l

Then S(t) = X(t)J(t). We show that S(t) = X(t)J(t) is a solution to the
stochastic differential equation ( 11.7.18).
The ltO-Doeblin formula for a continuous process says that

dX(t) = (a: - (3>)X(t) dt + aX(t) dW(t). (11.7.20)

At the time of the ith jump, J(t) = J(t-)(Yi + 1) and hence

LlJ(t) = J(t) - J(t-) = J(t-)Yi = J(t-)LlQ(t).

The equation LlJ(t) = J(t-)LlQ(t) also holds at nonjump times, with both
sides equal to zero. Therefore,


514 11 Introduction to Jump Processes

dJ(t) = J(t-) dQ(t). (11.7.21)

Ito's product rule for jump processes implies that

S(t) = X(t)J(t) = S(O) + 1 [t ] X(s-) dJ(s) + 1 [t ] J(s) dX(s) + [X, J](t).
(11.7.22)

=
Since J is a pure jump process and X is continuous, [X, J](t) 0. Substituting
(11.7.20) and (11.7.21) into (11.7.22), we obtain



S(t) [= ] X(t)J(t)



= S(O) + 1 [t ] X(s-)J(s-) dQ(s) + (a - (JA) 1 [t ] J(s)X(s) ds



+u J(s)X(s) dW(s),
1 [t ]



which in differential form is



dS(t) = d(X(t)J(t))
= X(t-)J(t-) dQ(t) + (a - (JA)J(t)X(t) dt + uJ(t)X(t) dW(t)
= S(t-) dQ(t) + (a - (JA)S(t) dt + uS(t) dW(t).

This is (11.7.18). 0

We now undertake to construct a risk-neutral measure. Let () be a constant

     -      and let A1, . . ., AM be positive constants. Define 2



Zo(t) = exp - OW(t) - �() [2] t
{      - },



Zo(t) = exp - OW(t) - �() [2] t

               Nm(t)
Z m (t) _ - e(Am - [Xm] )t [A][m ], m - 1 [-], . . ., M
### ( A )m '
M
Z(t) = Zo(t) IT Zm(t),
m=l
P(A) = Z(T) diP for all A E F.
i



The following a erti<!.ns follow f�m Theorem 11.6.10 and Corollary 11.3.4.
Independence under lP' between W and each of the Poisson processes Nm,
a erted (iii) below, follows from Corollary 11.5.3. Under the probability

    measure IP',



2 One could create more risk-neutral measures than we consider here by letting ()
and . be adapted stochastic processes.
>.1,, >.M
### ..


11.7 Pricing a European Call in a Jump Model 515



(i) the process

Define



(11.7.23)



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-534-0.png)

This is equivalent to the equation

a - (3A = r + a(} - {3X, (11.7.25)

which is the market price of risk equation for this model. Recalling the defini­
tions of (3 and {3, we may rewrite the market price of risk equation (11.7.25)
as

a - r = aO + (3A - {3X
M
= aO + L (Am - Am)Ym· (11. 7.26)
m=l

Because there is one equation and M + 1 unknowns, 0, A1, . . ., AM, there are
multiple risk-neutral measures.
Extra stocks would help determine a unique risk-neutral measure. We il­
lustrate this point by taking M = 2 in the following example.
Example 11. 1.4 (Three stocks and two Poisson processes). With one Brownian
motion W and two independent Poisson processes N1 and N2, define three
compound Poisson processes


516 11 Introduction to Jump Processes



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-535-0.png)








0


we have


i=1

Indeed, it is a straightforward matter to use (11.7.25) to verify that (11.7.19)
and (11.7.28) are in fact the same equation. We have not changed the stock
price process; we have changed only its distribution.
We compute the risk-neutral price of a call on the stock with price process
given by (11.7.28). Because 0 does not appear explicitly in (11.7.28), it will
not appear in our pricing formula. However,
M

[3-X [= ] XmYm
L
m=1


1 1.7 Pricing a European Call in a Jump Model 517


will appear in this formula, and we can choose the risk-neutral intensities
:X1, . . ., :XM to be any positive constants and subsequently choose () so that
the market price of risk equation (11.7.25) is satisfied. We a ume for the
remainder of this section that some choice has been made. Our pricing for­
mula will depend on the choice. It is common to use these free parameters to
calibrate the model to market data.
For the next step, we need some notation. Define



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-536-0.png)











i=N{t)+l
(11. 7.31 )
The term S(t) is F(t)-measurable, and the other term appearing on the right­
hand side of (11.7.31 ) is independent of F(t). Therefore, the Independence
Lemma, Lemma 2.3.4, implies that


518 11 Introduction to Jump Processes



V(t) = E[e [-] r'"(S(T) - KtiF(t)] = c(t, S(t)),
where
c(t, x)




### [ (



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-537-0.png)






### [ [ (








E E
### [ [ (



where








  





### [ (



N(T)


i=N(t)+l
### ( N(T)





N(T)

i=N(t)+l



N(T)

i=N(t)+l
### )


11.7 Pricing a European Call in a Jump Model 519


It follows that
N(T)


tribution as nf=l (Yi + 1). Furthermore,


Remark 11. 7.6 (Continuous jump distribution). Suppose the jump sizes Yi
have a density f(y) rather than a probability ma function p(yt), . . .,p(ym),
and this density is strictly positive on a set B C ( -1, oo) and zero elsewhere.
In this case, we replace ( 11.7 .17) by the formula


For the risk-neutral measure, we can choose 6, >. - 0 and any density J(y)
that is strictly positive on B and zero elsewhere so that the market price of
risk equation (see (11.7.26))

a - r = u6 + /3A - /3>.

is satisfied, where now


Under these conditions, Theorem 11.7.5 still holds.
0

We return to the model with discrete jump sizes. The following theorem
provides the differential-difference equation satisfied by the call price.

Theorem 11.7.7. The call price c(t, x) of {11.7.30} satisfies the equation
-- 1
2 2 Cxx(t,x)
-rc(t, x) + Ct(t,x) + (r - /3A)Xcx(t, x) + 2q X

M

m=l
and the terminal condition

c(T, x) [= ] (x - K)+, x � 0.

+X 2: P(Ym)c(t, (Ym + 1)x) - c(t, x) = 0, 0 � t < T, x ; 0, (11.7.33)

[ ]

/3 = EYi = yf(y) dy.

f3 = lEYi = yf(y) dy.



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-538-0.png)
520 1 1 Introduction to Jump Processes



formula implies
e-rtc(t, S(t)) - c(O, S(O))



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-539-1.png)
###### 1 [t ] [






![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-539-0.png)

0<u$t
M


###### [



=



M

d( e-rtc(t, S(t)))





1 2 2
{



M
m=l



M
+ L e-rt [c(t, (Ym + 1)S(t-)) - c(t, S(t-))] d(Nm(t) - 5mt). (11.7.35)
m=l


11.7 Pricing a European Call in a Jump Model 521



The integrators N m ( t) ->m t in the last term are martingales under JPl, and the
integrands e-rt[c(t, ))] are left-continuous. There­
###### (Ym + 1)S(t- ) -c(t, S(tfore, the integral of this term is a martingale. Likewise, the integral of the
next-to-last term e-rtcx(t, is a martingale. Since the discounted
###### S(t)) dW(t)
option price appearing on the left-hand side of is also a martingale,
###### (11.7.35)
the remaining term in is a martingale as well. Because the remaining
###### (11.7.35)
term is a term, it must be zero. Replacing the price process by the
###### dt S(t)
dummy variable in the integrand of this term, we obtain
###### x (11.7.33). 0



Corollary 11.7.8. The call price c(t, {11. 7.30} satisfies
###### x) of
d(e-rtc(t, S(t)))



= e-rtaS(t)cx(t, S(t)) dW(t)



M
L e-rt
###### + [c(t, (Ym + 1)S(t-))-c(t, S(t-))) d(Nm(t)-5mt) m=l



= e-rtaS(t)cx(t, S(t)) dW(t)
+e-r [t ]
###### [c(t, S(t))-c(t, S(t-))) dN(t)



-e-r [t] j.
###### [t/(Ym)c(t,(y+1)S(t-)) -c(t,S(t-))] dt. (11.7.36)



PROOF: We use to cancel the term in and obtain the first
###### (11.7.33) dt (11.7.35) equality in - M (11.7.36). - -For the second equality, recall that - - N(t) = E:':=l Nm(t), 0

Remark 11. 7.9 (Continuous jump distribution). There are modifications of
Theorem and Corollary for the case when the jump sizes Yi
###### 11.7.7 11.7.8 have a density M J(y) under the risk-neutral measure would be replaced by J_1 oo JPl. In (11.7.33), -the term In Em=l p(ym)c(t, (Ym + 1)x) c(t, (y + 1)x)f(y) dy.

we would use the second formula for d e-rtc t, which is writ­
###### (11.7.36), ( ( S(t))),
ten in terms of the total number of jumps (i.e., in terms of the Poisson process
###### N(t) = E�=l Nm(t)) rather than in terms of the individual Poisson processes

and replace by
###### Nm, E:': p(ym)c(t, (Ym + 1)S(t-)) J� c(t, y+ 1)S(t-))J(y) dy
0
###### A = Em=l Am, and Ap(ym) = Am·



Finally, we think about hedging a short position in the European call
whose discounted price satisfies Suppose we begin with a short call
###### (11.7.36).
position and a hedging portfolio whose initial capital is X(O) = c(O, S(O)). We
compare the differential of the discounted call price with the differential of
the discounted value of the hedging portfolio. If shares of stock are held
###### F(t)
by the hedging portfolio at each time t, then
= +
###### dX(t) F(t-) dS(t) r[X(t)-F(t)S(t)] dt

and


522 1 1 Introduction to Jump Processes

d e [-] r [t] x(t) = e [-] r [t ] [ - rX(t) dt + dX(t)]
( )
= e-r [t ] [r(t-) dS(t) - rF(t)S(t) dt]


M

m=l



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-541-0.png)
11.8 Summary 523



"On average," the delta-hedging formula hedges the option, where the average
is computed under the risk-neutral measure we have chosen. This provides
some justification for choosing Xm [=] Am, so that, at least as far as the jumps
are concerned, the average under the risk-neutral measure we are using is also
the average under the actual probability measure.
Remark 11. 7. 10 (Continuous jump distribution}. When the risk-neutral dis­
tribution of the jumps Yi has density J(y), (11.7.38) becomes
d[e-rtc(t, S(t)) - e-rtx(t)]



= e-rt [c(t, S(t)) - c(t, S(t-)) - (S(t) - S(t-))cx(t, S(t-))] dN(t)



-e-rt X [c(t, (y + 1)S(t-)) - c(t, S(t-))
17



-yS(t-)cx(t, S(t-))] f(y) dy dt. (11.7.40)



Equation (11.7.40) can be interpreted just as (11.7.38) was. Because

c(t, (y + 1)S(t-)) - c(t, S(t-)) - yS(t-)cx(t, S(t-)) > 0

for all y > -1, y =/:- 0, between jumps

d[e-rtc(t, S(t)) - e-rt X(t)] < 0,

the hedging portfolio outperforms the option. At jump times, the option out­
performs the hedging portfolio because

c(t, S(t)) - c(t, S(t-)) - (S(t) - S(t-))cx(t, S(t-)) > 0.

On "average," where the average is computed under the risk-neutral measure
we have chosen, these two effects cancel one another.


1 1 .8 Summary


The fundamental pure jump process is the Poisson process. Like Brownian
motion, the Poisson process is Markov, but unlike Brownian motion, it is not
a martingale. The Possion process only jumps up, and between jumps it is
constant. To obtain a martingale, one must subtract away the mean of the
Poisson process to obtain a compensated Poisson process (Theorem 11.2.4).
All jumps of a Poisson process are of size one. A compound Poisson process
is like a Poisson process, except that the jumps are of random size. Like the
Poisson process, a compound Poisson process is Markov (Exercise 11. 7), and
although it is generally not a martingale, one can obtain a martingale by
subtracting away its mean (Theorem 11.3.1). A compound Poisson process
that has only finitely many, say M, possible jump sizes can be decomposed


1 1 Introduction to Jump Processes

into a sum of M independent scaled Poisson processes (Theorem 11.3.3 and
Corollary 11 .3.4).
A jump process has four components: an initial condition, an Ito integral, a
Riemann integral, and a pure jump process. The sum of the first three consti­
tute the continuous part of the jump process. Stochastic integrals and stochas­
tic calculus for the continuous part of a jump process were treated in Chapter

4. In this chapter, the pure jump part is a right-continuous process that has
finitely many jumps in each finite time interval and is constant between jumps.
Stochastic integrals with respect to such processes are straightforward. The
quadratic variation of such a process over a time interval is the sum of the
squares of the jumps within that time interval, and the quadratic variation
of a (non pure) jump process is the quadratic variation of the continuous part
plus the quadratic variation of the pure jump part. These observations lead
to a version of the ItO-Doeblin formula for jump processes (Theorems 11.5.1
and 11.5.4). One of the consequences of these theorems is that a Brownian
motion and a Poisson process relative to the same filtration must be indepen­
dent (Corollary 11.5.3) and that two Poisson processes are independent if and
only if they have no simultaneous jumps (Exercises 1 1 .4 and 11.5).
If we integrate an adapted process with respect to a jump process that
is a martingale, the resulting stochastic integral can fail to be a martingale.
However, if the integrand is left-continuous, then the stochastic integral will
be a martingale.
For compound Poisson processes, one can change the measure in order to
obtain an arbitrary positive intensity (average rate of jump arrival) and an
arbitrary distribution of jump sizes, subject to the condition that every jump
size that was impossible before the change of measure is still impossible after
the change of measure. This provides a great deal of freedom when construct­
ing risk-neutral measures. In particular, if there are M possible jump sizes,
there are M - 1 degrees of freedom in the a ignment of probabilities to these
jump sizes (the probabilities must sum to one, and thus there are not M de­
grees of freedom). In order to have a complete market, there must be a money
market account and as many nonredundant securities as there are sources of
uncertainty. Each possible jump size counts as a source of uncertainty. If there
is no Brownian motion and only one possible jump size, a single security in
addition to the money market account will make the model complete (Section
11.7.1). If there are two possible jump sizes and an additional source of un­
certainty due to a Brownian motion, three securities in addition to the money
market account are required (Example 11.7.4). If there are infinitely many
possible jump sizes, infinitely many securities would be required to make the
model complete.
As the discussion above suggests, jump-diffusion models are generally in­
complete and there are typically multiple risk-neutral measures in such mod­
els. The practice is to consider a parametrized cla of such measures and then
calibrate the model to market prices to determine values for the parameters.
One can then apply the risk-neutral pricing formula to price derivative secu
524


1 1 . 10 Exercises 525


rities, but this formula can no longer be justified by a hedging argument. It
is instead an elaborate interpolation procedure by which prices of nontraded
securities are computed based on prices of traded ones. One can use this for­
mula to examine the effectiveness of various hedging techniques. This is done
for the delta-hedging rule in Subsection 11.7.2 following Remark 11.7.9.


1 1 .9 Notes


A text on Poisson and compound Possion processes, but that does not include
the ideas of change of measure, is Ross [141]. The easiest place to read about
stochastic calculus for processes with jumps is Protter [133].
In Section 11.7, we consider a European call in two models, one in which
the driving process for the underlying a et is a single Poisson process and
the other in which the underlying a et is driven by a Brownian motion and
multiple Poisson processes. In both these models, there are only finitely many
jump sizes, but the analogous results for models with a continuous jump
distribution are presented in Remarks 11.7.6, 11.7.9, and 11.7.10. Such a model
was first treated by Merton [123], who considered the case in which one plus
the jump size has a log-normal distribution. Some of the more recent works
on option pricing in models with jumps are Brockhaus et al. [23], Elliott and
Kopp [63], Madan, Carr, and Chang [113], Madan and Milne [114], Madan and
Seneta [115], Mercurio and Runggaldier [120], and Overhaus et al [130]. Term­
structure models with jumps are treated by Bjork, Kabanov and Runggaldier

[12], Das [46], Das and Foresi [47], Gla erman and Kou [73], and Gla erman
and Merener [74].


1 1 . 10 Exercises


Exercise 11.1. Let M ( t) be the compensated Poisson process of Theorem
11.2.4.
(i) Show that M [2] (t) is a submartingale.
(ii) Show that M [2] (t) - >t is a martingale.

Exercise 11.2. Suppose we have observed a Poisson process up to time s,
have seen that N(s) = k, and are interested in the value of N(s + t) for small
positive t. Show that

IP'{ N(s + t) = kjN(s) = k} = 1 - >t + O(t [2] ),
IP'{N(s + t) = k + 1IN(s) = k} = >t + O(t [2] ),
IP'{ N(s + t) ; k + 2IN(s) = k} = O(t2),

where O(t2) is used to denote terms involving t2 and higher powers of t.


526 1 1 Introduction to Jump Processes


Exercise 11.3 (Geometric Poisson process). Let N(t) be a Poisson pro­
cess with intensity A - 0, and let S(O) - 0 and a - -1 be given. Using
Theorem 11.2.3 rather than the ItO-Doeblin formula for jump processes, show
that


is a martingale.

Exercise 11.4. Suppose N1 (t) and N2(t) are Poisson processes with inten­
sities .X1 and .X2, respectively, both defined on the same probability space
(il, F, P) and relative to the same filtration F(t), t 2: 0. Show that almost
surely N1 (t) and N2(t) can have no simultaneous jump. (Hint: Define the
compensated Poisson processes M1(t) = N1(t) - .X1t and M2(t) = N2(t) - .X2t,
which like N1 and N2 are independent. Use Ito's product rule for jump pro­
cesses to compute M1 (t)M2(t) and take expectations.)

Exercise 11.5. Suppose N1 (t) and N2(t) are Poisson processes defined on the
same probability space (il,F, IP') relative to the same filtration F(t), t 2: 0.
Assume that almost surely N1 (t) and N2(t) have no simultaneous jump. Show
that, for each fixed t, the random variables N1 (t) and N2(t) are independent.
(Hint: Adapt the proof of Corollary 11.5.3.) (In fact, the whole path of N1
is independent of the whole path of N2, although you are not being asked to
prove this stronger statement.)

Exercise 11.6. Let W(t) be a Brownian motion and let Q(t) be a compound
Poisson process, both defined on the same probability space (il,F, IP') and
relative to the same filtration F(t), t 2: 0. Show that, for each t, the random
variables W(t) and Q(t) are independent. (In fact, the whole path of W is
independent of the whole path of Q, although you are not being asked to
prove this stronger statement.)

Exercise 11. 7. Use Theorem 11.3.2 to prove that a compound Poisson pro­
cess is Markov. In other words, show that, whenever we are given two times
0 � t � T and a function h(x), there is another function g(t, x) such that

lE[h(Q(T))iF(t)] = g(t, Q(t)).

S(t) = exp {N(t) log( a + 1) - .Xat} = (a + 1)N(t)e->.ut


A


Because of this fact, there is no way to get condition (1.1.2) from condition
(1.1.5), and so we build the stronger condition (1.1.2) into the definition of
probability space.
In fact, condition (1.1.2) is so strong that it is not possible to define P(A)
for every subset A of an uncountably infinite sample space so that (1.1.2)
n
holds. Because of this, we content ourselves with defining P(A) for every set
A in a a-algebra :F that contains all the sets we will need for our analysis
but omits some of the pathological sets that a determined mathematician can
construct.
There are two other consequences of (1.1.2) that we often use implicitly,
and these are provided by the next theorem.


Theorem A.l.l. Let (fl, :F, P) be a probability space and let A1. A2, A3, • - be a sequence of sets in :F.
{i) If A1 c A2 c A3 c . . ., then



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-546-0.png)
528 A Advanced Topics in Probability Theory



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-547-0.png)

= lim lP(Uk=l Bk) = lim lP(An ).
n-+oo n-+oo





This concludes the proof of (i).

                                                             -                                                              -                                                              -                                                              Let us now a ume A1 : A2 : A3 : We define Ck = A�, so that
C1 c C2 c C3 c . . . and n�1Ak = (uk=lCk)c. Then (1.1.6) and (i) imply

JP(n�1Ak) = 1 - 1P(U�1Ck) = 1 - lim lP(Cn)
n-+oo
= lim (1 - JP(Cn)) = lim lP(An) ·
n-+oo n-+oo

Thus we have (ii).
0



JP(n�1Ak) = 1 - 1P(U�1Ck) = 1 - lim lP(Cn)
n-+oo
= lim (1 - JP(Cn)) = lim lP(An) ·
n-+oo n-+oo



Property (i) of Theorem A.1.1 was used in (1.2.6) at the step

lim lP{ -n X n} lP{X E IR}.
:5 :5 =
n-+oo

Property (ii) of this theorem was used in (1.2.4). Property (ii) can also be
used in the following example.

Example A.1.2. We continue Example 1.1.3, the uniform measure on [0, 1].
Recall the u-algebra 8[0, 1] of Borel subsets of [0, 1], obtained by beginning
with the closed intervals and adding all other sets necessary in order to have a
u-algebra. A complicated but instructive example of a set in 8[0, 1] is the Can­

tor set, which we now construct. We also compute its probability, where the
probability measure we use is the uniform measure, a igning a probability
lP
to each interval [a, b] c [0, 1] equal to its length b - a.


A.1 Countable Additivity 529


From the interval [0, 1], remove the middle third (i.e., the open interval



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-548-0.png)





















which are the endpoints of the intervals appearing at the successive stages,
because these are never removed. This is a countably infinite set of points. In
fact, the Cantor set has uncountably many points. To see this, assume that all

                                                                                            - .                                                                                            -                                                                                            the points in the Cantor set can be listed in a sequence Let
x1, x2, x3, K1
denote the piece of C1, either [ 0, or [ 1], that does not contain Let
�] i, x1.
be a piece of that does not contain X2· For example, if =
K2 Kt nc2 Kt [o, �]


530 A Advanced Topics in Probability Theory


and E [� �], we take K [0, �] . If =f. Kt, it does not matter whether
x2, 2 = x2
we take K [0, �] or [�, �] . Next let K3 be a piece of K n that
2 = K2 = 2 C3
does not contain Continue this process. Then
x3.
(A.1.2)
and x1 ¢ K1, x2 ¢ K2, x3 ¢ K3, . . . . In particular, n�=1Kn does not contain
. .                                                          -                                                          any point in the sequence But the intersection of a sequence
x1,x2,x3,
of nonempty closed intervals that are "nested" as described by (A.1.2) must
contain something, and so there is a point y satisfying y E n�=l Kn· But
n�=tKn c C, and so the point y is in the Cantor set but not on the list
. . . . This shows that the list cannot include every point in the Can­
x1, x2, x3,
tor set. The set of all points in the Cantor set cannot be listed in a sequence,
which means that the Cantor set is uncountably infinite.
0


A.2 Generating u-algebras


We often have some collection C of subsets of a sample space fl and want to put
in all other sets necessary in order to have a a-algebra. We did this in Example
1.1.3 when we constructed the a-algebra 8[0, 1] and again in Example 1.1.4
when we constructed F 00 • In the former case, C was the collection of all closed
intervals [a, b] C [0, 1]; in the latter case, C was the collection of all subsets of
fl00 that could be described in terms of finitely many coin tosses.
In general, when we begin with a collection C of subsets of fl and put in
all other sets necessary in order to have a a-algebra, the resulting a-algebra
is called the a-algebra generated by C and is denoted by a( C). The description
just given of a(C) is not mathematically precise because it is difficult to de­
termine how and whether the process of "putting in all other sets necessary
in order to have a a-algebra" terminates. We provide a precise mathematical
definition at the end of this discussion.
The precise definition of a(C) works from the outside in rather than the
inside out. In particular, we define a(C) to be the "smallest" a-algebra con­
taining all the sets in C in the following sense. Put in a(C) every set that is
in every a-algebra that is "bigger" than C (i.e., that contains all the sets in
C). There is at least one a-algebra containing all the sets in C, the a-algebra
of all subsets of fl. If this is the only a-algebra bigger than C, then we put
every subset of fl into a(C) and we are done. If there are other a-algebras
bigger than C, then we put into a(C) only those sets that are in every such
a-algebra. We note the following items.
(i) The empty set 0 is in a( C) because it is in every a-algebra bigger than C.
(ii) If A E a(C), then A is in every a-algebra bigger than C. Therefore, is
N
in every such a-algebra, which implies that Ac is in a(C).

                          - . .
(i) If A1, A2, A3, is a sequence of sets in a( C), then this sequence is in
every a-algebra bigger than C, and so the union U�=l An is also in every
such a-algebra. This shows that the union is in a(C).


A.3 Random Variable with Neither Density nor Probability Ma Function 531

(iv) By definition, every set in C is in every a-algebra bigger than C and so is
in a(C).
(v) Suppose g is a a-algebra bigger than C. By definition, every set in a(C)
is also in g.
Properties (i)-(iii) show that a(C) is a a-algebra. Property (iv) shows that
a(C) contains all the sets in C. Property (v) shows that a(C) is the "smallest"
a-algebra containing all the sets in C.


Definition A.2.1 Let C be a collection of subsets of a nonempty set il. The
a-algebra generated by C, denoted a( C), is the collection of sets that belong to
all a -algebras bigger than C (i.e., all a -algebras containing all the sets in C).


A.3 Random Variable with Neither Density nor

Probability Mass Function


Using the notation of Example 1.2.5, let us define


      


![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-550-0.png)
532 A Advanced Topics in Probability Theory


and



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-551-0.png)









9 9



3 3 9



9



Fig. A.3.1. A singularly continuous function.


the comment following Definition 1.6.3).
The probabilities IP(A) and JP(A) are defined for every subset A of {l that is
in F. We define two equivalent probability measures on the smaller a-algebra
Q. The first is simply IP restricted to g (i.e., we define Q(A) = IP(A) for every



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-552-0.png)
534 B Existence of Conditional Expectations



A E Q, and we leave Q(A) undefined for A ¢ Q). The second is P restricted to
g (i.e., we define Q(A) = P(A) for every A E Q, and we leave Q(A) undefined
for A ¢ Q). We now have two probability spaces, (il, Q, Q) and (il, Q, Q),
�hich differ only by their probability measures Q and ij. Moreover, Q and
Q are equivalent. The Radon-Nikodym Theorem, Theorem 1.6.7, implies the
existence of a random variable Z such that



Q(A) = Z(w) dQ(w) for every A E Q.
L



However, since we are now working on probability spaces with a-algebra Q,
the random variable Z whose existence is guaranteed by the Radon-Nikodym
Theorem will be Q-measurable rather than .1"-measurable. (Recall from Def­
inition 1.2.1 that every random variable is measurable with respect to the
a-algebra in the space on which it is defined.)
Since ij and Q agree with P and P on g, we may rewrite the formula above
as
P(A) = Z(w) dlP(w) for every A E g
L



or, equivalently,

dlP(w) = Z(w) dlP(w) for every A E Q.
L L



Multiplication by JE[X 1] 1eads to the equation
###### +
X(w) dlP(w) + 1 dlP(w) = JE[X + 1]Z(w) dlP(w) for every A E Q.
L L L



We conclude that
X(w) dlP(w) = (JE[X + 1]Z(w) - 1) dlP(w) for every A E g.
L L



and JE[X Taking Y+ (w) 1] is constant, = JE[X + 1]Z(w) - 1, Y is also Q-measurable. we have (B.1) . Because Z is Q-measurable 0


c


Completion of the Proof of the Second

Fundamental Theorem of Asset Pricing


This appendix provides a lemma that is the last step in the proof of the Second
FUndamental Theorem of Asset Pricing, Theorem 5.4.9 of Chapter 5.


Lemma C.l Let A be an m x d-dimensional matrix, b an m-dimensional
vector, and c a d-dimensional vector. If the equation
Ax = b (C.l)
has a unique solution x0, a d-dimensional vector, then the equation
Atry = C (C.2)



(C.l)



Atry = C (C.2)

has at least one solution y0, an m-dimensional vector. (Here, Atr denotes the
tmnspose of the matrix A.)

PROOF: We regard A as a mapping from JR.d to �R_ [m ] and define the kernel of
A to be
K(A) = {x E IR.d : Ax = 0}.
If x0 solves (C.l) and x E K(A), then x0 + x also solves (C.l). Thus, the
a umption of a unique solution to (C.l) implies that K(A) contains only the
d-dimensional zero vector.
The rank of A is defined to be the number of linearly independent columns
of A. Because K(A) contains only the d-dimensional zero vector, the rank
must be d. Otherwise, we could find a linear combination of these columns
that would be the m-dimensional zero vector, and the coefficients in this lin.:lar
combination would give us a non-zero vector in K(A). But any matrix and its
transpose have the same rank, and so the rank of A tr is d as well. The rank
of a matrix is also the dimension of its range space. The range space of Atr is

Because the dimension of this space is d and it is a subspace of JR.d, it must in
fact be equal to JR.d. In other words, for every z E JR.d, there is some y E IR. [m ]
such that z = Atry. Hence, (C.2) has a solution y0 E R [m] . 0
R(Atr) = {z E IR.d : z = Atry for some y E IR.m}.


This page intentionally left blank



![](C:/AssetManager/data/quant_kb/Stochastic_Calculus_II/Steven E. Shreve Stochastic Calculus for Finance II- Continuous-Time Models (Springer Finance) (v. 2)_assets/Steven-E.-Shreve-Stochastic-Calculus-for-Finance-II--Continuous-Time-Models-(Springer-Finance)-(v.-2).pdf-555-0.png)
References


1. AIT-SAHALIA, Y. (1996) Testing continuous-time models of the spot interest
rate, Rev. Fin. Stud. 9, 385-426.
2. AMIN, K. AND JARROW, R. (1991) Pricing foreign currency options under
stochastic interest rates, J. Int. Money Fin. 10, 31Q-329.
3. AMIN, K. AND KHANNA, A. (1994) Convergence of American option values
from discrete- to continuous-time financial models, Math. Fin. 4, 289-304.
4. ANDREASEN, J. (1998) The pricing of discretely sampled Asian and lookback
options: a change of numeraire approach, J. Comput. Fin. 2, 5-30.
5. ARROW, K. AND DEBREU, G. (1954) Existence of equilibrium for a competitive
economy, Econometrica 22, 265-290.
6. BACHELlER, L. (1900) Theorie de la speculation, Ann. Sci. Ecole Norm. Sup.

17, 21-86.
7. BALDUZZI, P., DAS, S., FORESI, S., AND SUNDARAM, R. (1996) A simple
approach to three-factor term structure models, J. Fixed Income 6, 43-53.
8. BAXTER, M. W. AND RENNIE, A. (1996) Financial Calculus: An Introduction

to Derivative Pricing, Cambridge University Press, Cambridge, UK.
9. BENSOUSSAN, A. (1984) On the theory of option pricing, Acta Appl. Math. 2,
139-158.
10. BILLINGSLEY, P. (1986) Probability and Measure, 2nd ed., Wiley, New York.
11. BJORK, T. (1998) Arbitrage Theory in Continuous Time, Oxford University
Press, Oxford, UK.
12. BJORK, T., KABANOV, Y., AND RUNGGALDIER, W. (1997) Bond market struc­
ture in the presence of marked point processes, Math. Fin. 7, 21 1-239.
13. BLACK, F. (1976) The pricing of commodity contracts, J. Fin. Econ. 3, 167179.
14. BLACK, F. (1986) Noise, J. Fin. 41, 529-543.
15. BLACK, F., DERMAN, E., AND TOY, W. (1990) A one-factor model of interest
rates and its applications to treasury bond options, Fin. Anal. J. 46(1), 33-39.
16. BLACK, F. AND KARASINSKI, P. (1991) Bond and option pricing when short
rates are lognormal, Fin. Anal. J. 47(4), 52-59.
17. BLACK, F. AND SCHOLES, M. (1973) The pricing of options and corporate
liabilities, J. Polit. Econ. 81, 637-659.
18. BORODIN, A. AND SALMINEN, P. (1996) Handbook of Brownian Motion - Facts

and Formulae, Birkhii.user, Boston.


538 References


19. BRACE, A., G4TAREK, D., AND MUSIELA, M. (1997) The market model of
interest rate dynamics, Math. Fin. 4, 127-155.
20. BRACE, A. AND MUSIELA, M. (1994) A multifactor Gauss-Markov implemen­
tation of Heath, Jarrow and Morton, Math. Fin. 2, 259--283.
21. BRIGO, D. AND MERCURIO, F. (2001) Interest Rate Models: Theory and Prac­

tice, Springer-Verlag, Berlin.
22. BROADIE, M., GLASSERMAN, P., AND Kou, S. (1999) Connecting discrete and
continuous path-dependent options, Fin. Stochastics 3, 55-82.
23. BROCKHAUS, 0., FARKAS, M., FERRARIS, A., LONG, D., AND 0VERHAUS, M.
(2000) Equity Derivatives and Market Risk Models, Risk Books, London.
24. BRU, B. (2000) Un hiver en campagne, C. R. Ser. I 331, 1037-1058.
25. BRU, B. AND YOR, M. (2002) Comments on the life and mathematical legacy
of Wolfgang Doeblin, Fin. Stochastics 6, 3-47.
26. CAMERON, R. H. AND MARTIN, W. T. (1944) Transformation of Wiener inte­
grals under translations, Ann. Math. 45, 386-396.
27. CARR, P., JARROW, R., AND MYNENI, R. (1992) Alternative characterizations
of American put options, Math. Fin. 2(2), 87-106.
28. CHAN, K., KAROLY, A., LONGSTAFF, F., AND SANDERS, A. (1992) An empir­
ical comparison of alternative models of the short-term interest rate, J. Fin.
47, 1209-1227.
29. CHEN, L. (1996) Stochastic Mean and Stochastic Volatility - A Thr -Factor

Model of the Term Structure of Interest Rates and Its Application to the Pncing

of Interest Rate Derivatives, Blackwell, Oxford and Cambridge.
30. CHEN, R. AND SCOTT, L. (1992) Pricing interest rate options in a two-factor
Cox-Ingersoll-Ross model of the term structure, Rev. Fin. Stud. 5, 613-636.
31. CHEN, R. AND ScoTT, L. (1993) Maximum likelihood estimation for a multi­
factor equilibrium model of the term structure of interest rates, J. Fixed Income

3, 14-31.
32. CHEN, R. AND SCOTT, L. (1995) Interest rate options in multifactor Cox­
Ingersoll-Ross models of the term structure, J. Derivatives 3, 53-72.
33. CHERIDITO, P. (2003) Arbitrage in fractional Brownian motion models, Fin.

Stochastics 7, 533-553.
34. CHEYETTE, 0. (1996) Markov representation of the Heath-Jarrow-Morton
model, BARRA, Berkeley, CA.
35. CHUNG, K. L. (1968) A Course in Probability Theory, Academic Press, Or­
lando.
36. CHUNG, K. L. AND WILLIAMS, R. J. (1983) Introduction to Stochastic Inte­

gration, Birkhiiuser, Boston.
37. CLEMENT, E., LAMBERTON, D., AND PROTTER, P. (2002) An analysis of a
least squares regression algorithm for American option pricing, Fin. Stochastics

6, 449--471.
38. COLLIN-DUFRESNE, P. AND GOLDSTEIN, R. (2002) Pricing swaptions in the
affine framework, J. Derivatives 10, 926.
39. COLLIN-DUFRESNE, P. AND GOLDSTEIN, R. (2001) Generalizing the affine
framework to HJM and random fields, Graduate School of Industrial Admin­
istration, Carnegie Mellon University.
40. Cox, J. C., INGERSOLL, J. E., AND Ross, S. (1981) The relation between
forward prices and futures prices, J. Fin. Econ. 9, 321-346.
41. Cox, J. C., INGERSOLL, J. E., AND Ross, S. (1985) A theory of the term
structure of interest rates, Econometrica 53, 373-384.


References 539


42. Cox, J. C., Ross, S. A ., AND RUBINSTEIN, M. (1979) Option pricing: a sim­
plified approach, J. Fin. Econ. 7, 229-263.
43. Cox, J. C. AND RUBINSTEIN, M. (1985) Options Markets, Prentice-Ha, En­
glewood Cliffs, NJ.
44. DAI, Q. AND SINGLETON, K. (2000) Specification analysis of affine term struc­
ture models, J. Fin. 55, 1943-1978.
45. DALANG, R. C., MORTON, A., AND WILLINGER, W. (1990) Equivalent martin­
gale measures and no-arbitrage in stochastic security market models, Stochas­

tics 29, 185-201.
46. DAs, S. (1999) A discrete-time approach to Poisson-Gaussian bond option
pricing in the Heath-Jarrow-Morton model, J. Econ. Dynam. Control 23, 333369.
47. DAS, S. AND FORESI, S. (1996) Exact solutions for bond and option prices
with systematic jump risk, Rev. Derivatives Res. 1, 7-24.
48. DEGROOT, M. (1986) Probability and Statistics, 2nd ed., Addison-Wesley,
Reading, MA.
49. DELBAEN, F. AND SCHACHERMAYER, W. (1997) Non-arbitrage and the funda­
mental theorem of a et pricing: summary of main results, Proceedings of Sym­

posia in Applied Mathematics, American Mathematical Society, Providence,
Rl.
50. DERMAN, E. AND KANI, I. (1994) Riding on a smile, Risk 7 (2), 98-101.
51. DERMAN, E., KANI, 1., AND CHRISS, N. (1996) Implied binomial trees of the
volatility smile, J. Derivatives 3, 7-22.
52. DOEBLIN, W. (1940) Sur l'equation de Kolmogoroff, C. R. Ser. I 331, 10591 102.
53. DooB, J. (1942) Stochastic Processes, Wiley, New York.
54. DOTHAN, M. U. (1990) Prices in Financial Markets, Oxford University Press,
New York.
55. DUFFEE, G. (2002) Term premia and interest rate forecasts in affine models,
J. Fin. 57, 405-444.
56. DUFFIE, D. (1992) Dynamic Asset Pricing Theory, Princeton University Press,
Princeton, NJ.
57. DUFFIE, D. AND KAN, R. (1994) Multi-factor term structure models, Philos.

Trans. R. Soc. London, Ser. A 347, 577-586.
58. DUFFIE, D. AND KAN, R. (1994) A yield-factor model of interest rates, Math.

Fin. 6, 379-406.
59. DUFFIE, D., PAN, J., AND SINGLETON, K. (2000) Transform analysis and
option pricing for affine jump-diffusions, Econometnca 68, 1343-1376.
60. DUFFIE, D. AND PROTTER, P. (1992) From discrete- to continuous-time fi­
nance; weak convergence of the financial gain process, Math. Fin. 2, 1-15.
61. DUPIRE, 8. (1994) Pricing with a smile, Risk 9 (3), 18-20.
62. EINSTEIN, A. (1905) On the movement of small particles suspended in a sta­
tionary liquid demanded by the molecular-kinetic theory of heat, Ann. Phys.

17.
63. ELLIOTT, R. AND KOPP, P. (1990) Option pricing and hedge portfolios for
Poisson processes, Stochastic Anal. Appl. 9, 429-444.
64. FAMA, E. (1965) The behavior of stock-market prices, J. Business 38, 34-104.
65. FEYNMAN, R. (1948) Space-time approach to nonrelativistic quantum mechan­
ics, Rev. Mod. Phys. 20, 367-387.


540 References


66. FILIPOVIC, D. (2001) Consistency Problems for Heath-Jarrow-Morton Interest
Rate Models, Springer, Berlin.
67. Fu, M., MADAN, D., AND WANG, T. (1998/1999) Pricing continuous Asian op­
tions: a comparison of Monte Carlo and Laplace transform inversion methods,
J. Comput. Fin., 2(2), 49-74.
68. GARMAN, M . AND KOHLHAGEN, S. (1983) Foreign currency option values, J.
Int. Money Fin. 2, 231-237.
69. GEMAN, H. (1989) The importance of the forward neutral probability in a
stochastic approach of interest rates, Working paper, ESSEC.
70. GEMAN, H., EL KAROUI, N., AND ROCHET, J. (1995) Changes of numeraire,
change of probability measure and option pricing, J. Appl. Prob. 32, 443-458.
71. GEMAN, H. AND YOR, M. (1993) Bessel processes, Asian options, and perpe­
tuities, Math. Fin. 3, 349-375.
72. GIRSANOV, I. V. (1960) On transforming a certain cla of stochastic processes
by absolutely continuous substitution of measures, Theory Prob. Appl. 5, 285301.
73. GLASSERMAN, P. AND Kou, S. (2003) The term structure of simple forward
rates with jump risk, Math. Fin. 13, 383-410.
74. GLASSERMAN, P. AND MERENER, N. (2003) Numerical solution of jump diffu­
sion LIBOR market models, Fin. Stochastics 7, 1-27.
75. GLASSERMAN, P. AND Yu, B. Number of paths versus number of basis func­
tions in American option pricing, Fin. Stochastics to appear.
76. HAKALA, J. AND WYSTUP, U. (2002) Foreign Exchange Risk, Risk Books,
London.
77. HARRISON, J. M. AND KREPS, D. M. (1979) Martingales and arbitrage in
multiperiod security markets, J. Econ. Theory 20, 381-408.
78. HARRISON, J. M. AND PLISKA, S. R. (1981) Martingales and stochastic in­
tegrals in the theory of continuous trading, Stochastic Processes Appl. 11,
215-260.
79. HARRISON, J. M. AND PLISKA, S. R. (1983) A stochastic calculus model of
continuous trading: complete markets, Stochastic Processes Appl. 15, 313-316.
80. HAUG, E. (1998) The Complete Guide to Option Pricing Formulas, McGraw­
Hill, New York.
81. HEATH, D., JARROW, R., AND MORTON, A. (1990) Bond pricing and the term
structure of interest rates: A discrete time approximation, J. Fin. Quant. Anal.

25, 419-440.
82. HEATH, D., JARROW, R., AND MORTON, A. (1990) Contingent claim valuation
with a random evolution of interest rates, Rev. Futures Markets 9, 54-76.
83. HEATH, D., JARROW, R., AND MORTON, A. (1992) Bond pricing and the term
structure of interest rates: a new methodology, Econometrica 60, 77-105.
84. HESTON, S. (1993) A closed-form solution for options with stochastic volatility
and applications to bond and currency options, Rev. Fin. Stud. 6, 327-343.
85. Ho, T. AND LEE, S. (1986) Term structure movements and pricing interest
rate contingent claims, J. Fin. 41, 101 1-1029.
86. HUANG, C.-F. AND LITZENBERGER, R. (1988) Foundations for Financial Eco­
nomics, North Holland, Amsterdam.
87. HULL, J. (2002) Options, Futures, and other Derivative Secunties, 5th ed.,
Prentice-Hall, Englewood Cliffs, NJ.
88. HULL, J. AND WHITE, A. (1990) Pricing interest rate derivative securities,
Rev. Fin. Stud. 3, 573-592.


References 541


89. HULL, J. AND WHITE, A. (1994) Numerical procedures for implementing term
structure models II: two-factor models, J. Derivatives 2, 37-47.
90. HUNT, P., KENNEDY, J., AND PELSSER, A. (2000) Markov-functional interest
rate models, Fin. Stochastics 4, 391-408.
91. INGERSOLL, J. E. (1987) Theory of Financial Decision Making, Rowman and
Littlefield, Savage, MD.
92. IT<), K. (1944) Stochastic integral, Proc. Jmperwl Acad. Tokyo 20, 519-524.
93. JACKA, S. (1991) Optimal stopping and the American put, Math. Fin. 1(2),
1-14.
94. JAMSHIDIAN, F. (1989) An exact bond option formula, J. Fin. 44, 205-209.
95. JAMSHIDIAN, F. (1990) LIBOR and swap market models and measures, Fin.
Stochastics 1, 293-330.
96. JARA, D. (2000) An extension of Levy's theorem and applications to financial
models based on futures prices, Ph.D. dissertation, Dept. of Mathematical
Sciences, Carnegie Mellon University.
97. JARROW, R. (1988) Finance Theory, Prentice-Hall, Englewood Cliffs, NJ.
98. JARROW, R. A. AND OLDFIELD, G. S. (1981) Forward contracts and futures
contracts, J. Fin. Econ. 9, 373-382.
99. KAC, M. (1951) On some connections between probability theory and dif­
ferential and integral equations, Proceedings of the 2nd Berkeley Symposium
on Mathematical Statistics and Probability, 189-215, University of California
Press, Berkeley
100. KARATZAS, I. (1988) On the pricing of American options, Appl. Math. Optim.

17, 37--60.
101. KARATZAS, I. AND SHREVE, S. E. (1991) Brownian Motion and Stochastic
Calculus, Springer-Verlag, New York.
102. KARATZAS, I. AND SHREVE, S. (1998) Methods of Mathematical Finance,
Springer-Verlag, New York.
103. KIM, I. J. (1990) The analytic valuation of American options, Rev. Fin. Stud.

3, 547-572.
104. KOLMOGOROV, A. N. (1933) Grundbegriffe der Wahrscheinlichkeitsrechnung,
Ergeb. Math. 2, No. 3. Reprinted by Chelsea Publishing Company, New York,
1946. English translation: Foundations of Probability Theory, Chelsea Publish­
ing Co., New York, 1950.
105. LAMBERTON, D. AND LAPEYRE, B. (1996) Introduction to Stochastic Calculus
Applied to Finance, Chapman and Hall, London.
106. LEROY, S. F. (1989) Efficient capital markets and martingales, J. Econ. Lit.

27, 1583-1621.
107. LEVY, P . (1939) Sur certains processus stochastiques homogenes, Composition
Math. 7, 283-339.
108. LEVY, P. (1948) Processus Stochastiques et Mouvement Brownian, Gauthier­
Villars, Paris.
109. LIPTON, A. (1999) Similarities via self-similarities, Risk 1 2(9), 101-105.
1 10. LIPTON, A. (2003) Exotic Options: Technical Papers Published in Risk 1 9992003, Risk Books, London.
1 1 1 . LONGSTAFF, F. AND SCHWARTZ, E. (1992) Interest rate volatility and the term
structure: a two-factor general equilibrium model, J. Fin. 47, 1259-1282.
1 12. LONGSTAFF, F. AND SCHWARTZ, E. (2001) Valuing American options by sim­
ulation: a simple least-squares approach, Rev. Fin. Stud. 14, 1 13-147.


542 References


113. MADAN, D., CARR, P., AND CHANG, E. (1998) The variance gamma process
and option pricing, Eur. Fin. Rev. 2, 79-105.
114. MADAN, D. AND MILNE, F. (1991) Option pricing with V.G. martingale com­
ponents, Math. Fin. 1 (4), 39-56.
115. MADAN, D. AND SENETA, E. (1990) The V.G. model for share returns, J.
Business 63, 51 1-524.
116. MAGHSOODI, Y. (1996) Solution of the extended CIR term structure and bond
option valuation, Math. Fin. 6, 89-109.
117. MARGRABE, W. (1978) The value of an option to exchange one a et for an­
other, J. Fin. 33, 177-186.
118. MARGRABE, W. (1978) A theory of forward and futures prices, preprint, Whar­
ton School, University of Pennsylvania.
1 19. McKEAN, H. (1965) A free-boundary problem for the heat equation arising
from a problem in mathematical economics, Ind. Manage. Rev. 6, 32-39. Ap­
pendix to [144].
120. MERCURIO, F. AND RUNGGALDIER, W. (1993) Option pricing for jump diffu­
sions: approximations and their interpretation, Math. Fin. 3, 191-200.
121. MERTON, R. C. (1969) Lifetime portfolio selection under uncertainty: the
continuous-time case, Rev. Econ. Stat. 51, 247-257.
122. MERTON, R. C. (1973) Theory of rational option pricing, Bell J. Econ. Man­
age. Sci. 4, 141-183.
123. MERTON, R. C. (1976) Option pricing when underlying stock returns are dis­
continuous, J. Fin. Econ. 3, 125-144.
124. MERTON, R. C. (1990) Continuous- Time Finance, Basil Blackwell, Oxford and
Cambridge.
125. MILTERSEN, K., SANDMANN, S., AND SONDERMANN, D. (1997) Closed form
solutions for term structure derivatives with log-normal interest rates, J. Fin.
52, 409-430.
126. MUSIELA, M . AND RUTKOWSKI, M. (1997) Martingale Methods in Financial
Modelling, Springer-Verlag, New York.
127. MYNENI, R. (1992) The pricing of the American option, Ann. Appl. Prob. 2,
1-23.
128. NOVIKOV, A. A. (1971) On moment inequalities for stochastic integrals, Theory
Prob. Appl. 17, 717-720.
129. 0KSENDAL, B. (1995) Stochastic Differential Equations, 4th ed., Springer­
Verlag, New York.
130. OVERHAUS, M., FERRARIS, A., KNUDSEN, T., MILWARD, R., NGUYEN-NGOC,
L., AND SCHINDLMAYR, G. (2002) Equity Derivatives: Theory and Applications,
Wiley, New York.
131 . PELSSER, A. (2000) Efficient Methods for Valuing Interest Rate Derwatives,
Springer, Berlin.
132. PIAZZESI, M. (2003) Affine term structure models. In Handbook of Financial
Econometrics (Y. Ait-Sahalia and L. P. Hansen, eds.), North Holland, Ams­
terdam.
133. PROTTER, P. (2004) Stochastic Integration and Differential Equations, 2nd ed.,
Springer-Verlag, New York.
134. PROTTER, P. (1999) Featured review: recent books on mathematical finance,
SIAM Rev. 41, 167-173.
135. PROTTER, P. (2000) Arbitrage Theory in Continuous Time by T. Bjork, J.
Fin. 55, 518.


Refere [nces ] 543


136. PROTTER, P. {2001), Stochastic Calculus and Financial Applicatio [ns, SIAM ]

Rev. 43, 731-733.
137. REBONATO, R. {2002) Modern Pricing of Interest-Rate Derivatives: The LI­

BOR Market Model and Beyond, Princeton University Pre, Princeton, NJ.
138. RoGERS, L. C. G. {1997) Arbitrage with fractional Brownian motion, Math.

Fin. 7 {1), 95-105.
139. ROGERS, L. C . G. AND SHI, Z. {1995) The value of an Asian option, J. Appl.

Prob. 32, 1077-1088.
140. Ross, S. {1976) The arbitrage theory of capital a et pricing, J. Econ. Theory

13, 341-360.
141 . Ross, S. M. {1983) Stochastic Processes, Wiley, New York.
142. RUBINSTEIN, M. AND REINER, E. {1991) Breaking down barriers, Risk 4{9),
28-35.
143. SAMUELSON, P. A. {1965) Proof that properly anticipated prices fluctuate
randomly, Ind. Manage. Rev. 6, 41-50.
144. SAMUELSON, P. A. {1965) Rational theory of warrant pricing, Ind. Manage.

Rev. 6, 13-31.
145. SAMUELSON, P. A. (1973) Mathematics of speculative prices, SIAM Rev. 15,
1-42.
146. SANDMANN, K. AND SONDERMANN, D. {1993) A term structure model and the
pricing of interest rate derivatives, Rev. Futures Markets 12, 391-423.
147. SANDMANN, K. AND SONDERMANN, D. {1997) A note on the stability of log­
normal interest rate models and the pricing of Eurodollar futures, Math. Fin.

7, 119-128.
148. SCHMOCK, U., SHREVE, S., AND WYSTUP, U. {2002) Valuation of exotic op­
tions under shortselling constraints, Fin. Stochastics 6, 143-172.
149. SHIRAKAWA, H. {1991) Interest rate option pricing with Poisson-Gaussian for­
ward rate curve processes, Math. Fin. 1, 77-94.
150. STEELE, J. M. {2001) Stochastic Calculus and Financial Applications,
Springer-Verlag, New York.
151 . STROOCK, D. AND VARADHAN, S. R. S. {1969) Diffusion processes with con­
tinuous coefficients, I and II, Communications Pure Appl. Math. 22, 245-400
and 479-530.
152. TSITSIKLIS, J. AND VAN RoY, B. {2001) Regression methods for pricing com­
plex American-style options, IEEE Trans. Neural Networks 12, 694-703.
153. VAN MOERBEKE, P. {1979) On optimal stopping and free boundary problems,

Arch. Rational Mech. Anal. 60, 101-148.
154. VASICEK, 0 . {1977) An equilibrium characterization of the term structure, J.

Fin. Econ. 5, 177-188.
155. VECER, J. {2001) A new POE approach for pricing arithmetic average Asian
options, J. Comput. Fin. 4{4), 105-1 13.
156. VECER, J. {2002) Unified Asian pricing, Risk 15{6), 113-116.
157. VECER, J. AND Xu, M. {2004) Pricing Asian options in a semimartingale
model, Quant. Fin. 4, 17Q-175.
158. VILLE, J. {1939) Etude Critique de la Notion du Collectif, Gauthier-Villars,
Paris.
159. WIENER, N. {1923) Differential spaces, J. Math. Phys. 2, 131-174.
160. WIENER, N. {1924) Un probleme de probabilites denombrables, Bull. Soc.

Math. Prance 52, 569-578.


544 References


161. WILLIAMS, D. (1991) Probability with Martingales, Cambridge University
Press, Cambridge, UK.
162. WILLINGER, W. AND TAQQU, M . (1991) Towards a convergence theory for
continuous stochastic securities market models, Math. Fin. 1, 55-99.
163. WILLINGER, W., TAQQU, M., AND TEVEROVSKY, V. (1999) Stock market
prices and long-range dependence, Fin. Stochastics 3, 1-14.
164. WILMOTT, P. (1998) Derivatives, Wiley, New York.
165. WILMOTT, P ., HOWISON, S., AND DEWYNNE, J. (1995) The Mathematics of
Financial Derivatives: A Student Introduction, Cambridge University Press,
Cambridge, UK.
166. YoR, M. (2000) Presentation du pli cachete, C. R. Ser. I 331, 1033-1036.
167. ZHANG, P . (1997) Exotic Options, World Scientific, Singapore.


Index


Absolute continuity of probability
measures 45
adapted stochastic process 53, 97
additivity
countable 2
finite 3
affine yield 27 4, 405
almost everywhere 22
convergence 24
almost surely 7, 23
convergence 23
American options 339
perpetual put 345
arbitrage 230
statistical 188
arrival times 463
Asian option 278, 320
discretely sampled 329
zero-strike call 336
atom 51
augmentation of state 321


Backward equation (Kolmogorov) 291
barrier options 299
Bermudan option 339
BGM model (see Brace-Gatarek-Musiela
model)
Black caplet formula 439
Black-Scholes-Merton
boundary conditions 158
formula 118
for time-varying nonrandom
interest rate 253
function 159, 220



partial differential equation 157
put formula 164
bootstrapping 403
Borel
measurable function 21
set 4, 7
a algebra 4, 8, 20, 57, 528
Brace-Gatarek-Musiela model (see
forward LIBOR model) 405
Brownian bridge
as conditioned Brownian motion 182
from a to b 176
from 0 to 0 175
maximum of 183
multidimensional distribution 178
Brownian motion 94
correlated 197, 199, 200
covariance 95
filtration for 97
fractional 188
Markov property 107
martingale property 98
maximum to date 113
with drift 295
moment-generating function 96
multidimensional 164
other variations 117
quadratic variation 102
reflection principle 111
relative to a filtration 4 73
transition density 108
transition density with drift 119
uncorrelated dependent 204


546 Index


Calibration 272
call option
European 155
Cantor set 528
cap (see interest rate cap)
caplet (see interest rate caplet)
Central Limit Theorem 89
change of measure 32
for Brownian motion 212, 224
for compound Poisson process 500
for compound Poisson process and
Brownian motion 503
for exponential random variable 4 7
for normal random variable 36, 46
for Poisson process 494
change of numeraire
change in volatility caused by 400
portfolio under 398
to price Asian option 326
chooser option 256
CIR model (see Cox-Ingersoll-Ross
model)
coin-toss space 4
complete model 223, 231
compound Poisson process 468
compensated 470
decomposition 471
moment-generating function 4 70
relative to a filtration 474
conditional density 80
conditional expectation 69
existence 533
independence 70
iterated conditioning 70
linearity 69
taking out what is known 70
constant elasticity of variance 272
continuation set 357
convergence almost everywhere 24
convergence almost surely 23
correlated Brownian motions 197, 199,
200
correlated stock prices 171
correlation 62
instantaneous 201, 227
under change of measure 257
cost of carry 259
countable additivity 2, 527
covariance 62



for Brownian motion 95
Cox-Ingersoll-Ross interest rate model
151, 266, 275
hitting zero 288
moment generating function for 286
solution of 285
two-factor 422
cumulative distribution function ( cdf)
10
cumulative normal distribution 12


Delta 159, 193
hedging rule 157
neutral 161
of an option 157
short 161
density function 10
conditional 80
joint 57
marginal 58, 80
differential-difference equation 509
diffusion 263
discount process 227, 272
differential 215
distribution
joint 57
marginal 58
measure 9
dividend-paying stocks 234
risk-neutral pricing formula for 236
Doleans-Dade t>xponential 491
domestic risk-neutral measure 383
Dominated Convergence Theorem 27
drift 263


Early exercise premium 339
efficient market hypothesis 188
equivalent probability measures 34
Euler method 267
European call 155
European put 163
event 1
exchange rate 382
as dividend-paying a et 385
forward 388
paradox 387
put-call duality 390
exotic option 295
expectation (expected value) 17


computation of 27, 31
exponential martingale 109
exponential random variable 462
memorylessness for 463


Feynman-Kac Theorems 268, 269
two-dimensional 286
filtration 51
for Brownian motion
finite additivity 3
first-order variation 99
first pa age time 1 10
as a stopping time 341
distribution 112
Laplace transform for Brownian
motion 1 19, 122
Laplace transform for Brownian
motion with drift 346
Fokker-Planck equation 291
foreign exchange model 381
foreign risk-neutral measure 386
forward
contract 162, 241
exchange rate 388
LIBOR 437
LIBOR models 405
measure 393
price 163, 241, 392
rate 405, 424
forward equation Kolmogorov 291
( )
forward-futures spread 247
fractional Brownian motion 188
Fundamental Theorems of Asset Pricing
First 231
Second 232
futures price 244


Gamma 159
gamma density 464
long 161
Garman-Kohlhagen formula 390
Gaussian process 172
generalized geometric Brownian motion
147, 191
geometric Brownian motion 106
generalized 148, 191
limit of binomial model 120
maximum to date 334, 335
transition density 119



Index 547


geometric Poisson process 486
Girsanov's Theorem
multi-dimensional 224
one-dimensional 212
Greeks 159


Heath-Jarrow-Morton model 404
calibration of 432
multifactor 458
no-arbitrage condition 428
under risk-neutral measure 429
hedging a cash flow 256
hedging equations 232
Heston stochastic volatility model 288
HJM model see Heath-Jarrow-Morton
(
model
)
Hull-White interest rate model 265, 274
solution of 285


Implied volatility 271
independence
among sequence of random variables
56
among sequence of a algebras 56
between normal random variables 61
between random variable and
a algebra 54
between random variables 54
between set and random variable 45
between sets 54
between a algebras 54
Independence Lemma 73
indicator function 17, 22
indicator random variable 17
instantaneous correlation 201, 227
instantaneous standard deviation 227
integrability 16, 18
integral with respect to Ito process 145
intensity of Poisson process 463
interarrival times 463
interest rate cap 438
interest rate caplet 438
interest rate models 272
affine yield 274, 405
canonical 405
two-factor mixed 422
Brace-Gatarek-Musiela see forward
(
LIBOR 405
)
Cox-Ingersoll-Ross 151, 266, 275


548 Index


solution of 285
two-factor 420
forward LIBOR 405
calibration of 442
Heath-Jarrow-Morton model 404
calibration of 432
multi-factor 458
no-arbitrage condition 428
under risk-neutral measure 429
Hull-White 265, 274
solution of 285
market 405
one-factor 272
Vasicek 151, 405, 431
forward measure in 457
statistics for 451
two-factor 406
interest rate swap 459
intrinsic value 339
iterated conditioning 70
It6-Doeblin formula
for Brownian motion 138
for Ito process 143, 146
for jump processes 484, 489
in differential form 137
in integral form 137
two-dimensional 167
Ito integral
of deterministic integrand 149, 173
of general process 134
of Ito process 145
of simple process 127
Ito process 143
integral with respect to 145
quadratic variation 143
Ito's product rule 168, 489


Jensen's inequality 18
conditional 70
joint density 57
joint distribution 57
jump process 475
continuous part 475
cross variation 480
It6-Doeblin formula 484, 489
Ito integral part 474
Ito's product rule 489
pure jump part 475
quadratic variation 479



Riemann integral part 474
stochastic integral with respect to 475


Knock-in options 299
Knock-out options 299
Kolmogorov backward equation 291
Kolmogorov forward equation 291
Kronecker delta 201
kurtosis 1 17


Lebesgue integral 15
comparison property for 16, 18
comparison with Riemann integral 22
linearity 16, 18
over R
Lebesgue measure 3, 20
Levy's theorem
one-dimensional 168
two-dimensional 170
LIBOR (London interbank offered rate)
405
backset 437
tenor of 437
linear complementarity 352, 357
local martingale 188
local time 205
of Brownian motion 207
log-normal distribution 92
long rate 273, 413
lookback option 308, 335


Market model 405
market price of risk 204, 216, 228
in Heath-Jarrow-Morton model 427
in jump-diffusion model 515
marking to market 243
Markov process 74
martingale 7 4
exponential 109
local 188
Martingale Representation Theorem
multi-dimensional 225
one-dimensional 221
measurability of a random variable 53
measure
distribution 9
Lebesgue 3, 20
probability 2
uniform 3


mean reversion in Vasicek model 151
Mean Value Theorem 44, 100
memorylessness 463
moment-generating function 43
for Brownian motion 96
of standard normal random variable
45
Monotone Convergence Theorem 26
money market account 272


No-arbitrage derivation of bond price
282
normal random variable(s)
jointly 64
kurtosis 117
moment generating function 45
uncorrelated and dependent 62
numeraire 375


Optimal exercise time 340
option
American 339
perpetual put 345
Asian option 278, 320
discretely sampled 329
zero-strike call 336
barrier 299
Bermudan option 339
chooser 256
European call 155
European put 163
exotic 295
knock-out 299
knock-in 299
lookback 308, 335
on a bond 276
path-dependent 295
quanto 401
up-and-out call 307, 332
vanilla 295
Option pricing with random interest
rate 394
Optional sampling 302, 342, 373
Ornstein-Uhlenbeck process 286


Partial averaging 68
path-dependent option 295
perpetual American put 345
Poisson process 463



Index 549


compensated 467
compound 468
expected value 467
geometric 486
intensity 463

moment generating function 471
relative to a filtration 473
variance 467
portfolio value process 154
predictable 477
principal components analysis 434
probability integral transform 12
probability measure 2
probability space 2
coin toss 4
pure jump process 475
put-call parity 164
put option
European 163


Quadratic variation 101
for Brownian motion 102
for Ito process 143
for jump process 4 79
quanto option 401


Radon-Nikodym
derivative 36, 210
derivative process 211
theorem 39
random variable 7
degenerate 77
exponential 462
indicator 17
standard normal 12
random walk (see symmetric random
walk)
reflection principle 1 1 1
relative maturity 412
Riemann integral 14
comparison with Lebesgue integral 22
not defined 20
Riemann sum
lower 13
upper 13
risk-neutral measure 216, 228
domestic 383
existence 231
foreign 386


550 Index


implying from option prices 255
uniqueness 232
risk-neutral pricing formula 218
for a cash flow 246


St. Petersburg paradox 27
sample space 1
self-financing trading 193, 397
sets resolved by information 49
short rate models see interest rate
(
models
)
Siegel's exchange rate paradox 387
a-algebra a-field 1
( )
Borel 4, 8, 20
generated by a collection of sets 531
generated by a random variable 52
a X 52
( )
trivial 50
simple process 126
singularly continuous function 310
standard deviation 62
instantaneous 227
standard normal 12
density 12
distribution 12
random variable 12
state price density 204, 252
state processes 281
augmentation of 321
static hedge 162
stationary increments 466
statistical arbitrage 188
stochastic differential equation 263
one-dimensional linear 264
stop-loss start-gain paradox 207
stopped process 342
stopping set 355, 357
stopping time 302, 341
Stratonovich integral 136, 190
Strong Law of Large Numbers 7, 23
submartingale 74
supermartingale 7 4



swap see interest rate swap 459
( )
swap rate 459
symmetric random walk 84
independent increments 84
martingale property 85
quadratic variation 85
scaled 86


Tenor 437
theta 159, 193
time spread 452


U ncorrelated dependent Brownian
motions 204
uncorrelated random variables 62
dependent normal random variables
62
uncountably infinite set 1, 41
uniform measure distribution 3, 19
( )
up-and-out call price 307, 332


Van ilia option 295
variance 62
Vasicek equation 191
Vasicek interest rate model 151, 405,
431
forward measure in 457
mean reversion in 151
statistics for 451
two-factor 406
vega 162
volatility 106
implied 271
smile 271
surface 293
vector 377


Yield 273, 403
affine 274
curve 404


Zero-coupon bond 240, 273


