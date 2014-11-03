# Generate reference values based on scipy.stats

from numpy import sqrt, nan, inf
from scipy.stats import *

lst = [
	(arcsine(), "Arcsine()"),
	(beta(2.0, 2.0), "Beta(2.0, 2.0)"),
	(beta(3.0, 4.0), "Beta(3.0, 4.0)"),
	(beta(17.0, 13.0), "Beta(17.0, 13.0)"),
	(betaprime(3.0, 3.0), "BetaPrime(3.0, 3.0)"),
	(betaprime(3.0, 5.0), "BetaPrime(3.0, 5.0)"),
	(betaprime(5.0, 3.0), "BetaPrime(5.0, 3.0)"),
	(cauchy(0.0, 1.0), "Cauchy(0.0, 1.0)"),
	(cauchy(10.0, 1.0), "Cauchy(10.0, 1.0)"),
	(cauchy(2.0, 10.0), "Cauchy(2.0, 10.0)"),
	(chi(1.0), "Chi(1)"),
	(chi(2.0), "Chi(2)"),
	(chi(3.0), "Chi(3)"),
	(chi(12.0), "Chi(12)"),
	(chi2(1.0), "Chisq(1)"),
	(chi2(8.0), "Chisq(8)"),
	(chi2(20.0), "Chisq(20)"),
	(erlang(1, scale=1.0), "Erlang(1, 1.0)"),
	(erlang(3, scale=1.0), "Erlang(3, 1.0)"),
	(erlang(5, scale=2.0), "Erlang(5, 2.0)"),
	(expon(scale=1.0), "Exponential(1.0)"),
	(expon(scale=6.5), "Exponential(6.5)"),
	(gamma(1.0, scale=1.0), "Gamma(1.0, 1.0)"),
	(gamma(3.0, scale=1.0), "Gamma(3.0, 1.0)"),
	(gamma(3.0, scale=2.0), "Gamma(3.0, 2.0)"),
	(gumbel_r(3.0, 5.0), "Gumbel(3.0, 5.0)"),
	(gumbel_r(5.0, 3.0), "Gumbel(5.0, 3.0)"),
	(invgamma(1.0, scale=1.0), "InverseGamma(1.0, 1.0)"),
	(invgamma(1.0, scale=2.0), "InverseGamma(1.0, 2.0)"),
	(invgamma(2.0, scale=1.0), "InverseGamma(2.0, 1.0)"),
	(invgamma(2.0, scale=3.0), "InverseGamma(2.0, 3.0)"),
	(invgauss(1.0), "InverseGaussian(1.0, 1.0)"),
	(laplace(0.0, 1.0), "Laplace(0.0, 1.0)"),
	(laplace(5.0, 1.0), "Laplace(5.0, 1.0)"),
	(laplace(5.0, 1.5), "Laplace(5.0, 1.5)"),
	(logistic(0.0, 1.0), "Logistic(0.0, 1.0)"),
	(logistic(5.0, 1.0), "Logistic(5.0, 1.0)"),
	(logistic(5.0, 1.5), "Logistic(5.0, 1.5)"),
	(lognorm(1.0), "LogNormal(0.0, 1.0)"), 
	(lognorm(2.0), "LogNormal(0.0, 2.0)"),
	(norm(0.0, 1.0), "Normal(0.0, 1.0)"),
	(norm(-3.0, 2.0), "Normal(-3.0, 2.0)"),
	(norm(1.0, 10.0), "Normal(1.0, 10.0)"),
	(norm(0.0, 1.0), "NormalCanon(0.0, 1.0)"),
	(norm(-0.4, sqrt(0.4)), "NormalCanon(-1.0, 2.5)"),
	(norm(2.5, sqrt(1.25)), "NormalCanon(2.0, 0.8)"),
	(pareto(1.0, scale=1.0), "Pareto(1.0, 1.0)"),
	(pareto(2.0, scale=1.0), "Pareto(2.0, 1.0)"),
	(pareto(3.0, scale=2.0), "Pareto(3.0, 2.0)"),
	(rayleigh(scale=1.0), "Rayleigh(1.0)"),
	(rayleigh(scale=3.0), "Rayleigh(3.0)"),
	(rayleigh(scale=8.0), "Rayleigh(8.0)"),
	(t(1.0), "TDist(1.0)"),
	(t(5.0), "TDist(5.0)"),
	(t(28.0), "TDist(28.0)"),
	(uniform(0.0, 1.0), "Uniform(0.0, 1.0)"),
	(uniform(3.0, 14.0), "Uniform(3.0, 17.0)"),
	(uniform(3.0, 0.1), "Uniform(3.0, 3.1)"),
	(weibull_min(0.5, scale=1.0), "Weibull(0.5, 1.0)"),
	(weibull_min(1.0, scale=1.0), "Weibull(1.0, 1.0)"),
	(weibull_min(5.0, scale=1.0), "Weibull(5.0, 1.0)"),
	(weibull_min(20.0, scale=1.0), "Weibull(20.0, 1.0)"),
	(weibull_min(1.0, scale=2.0), "Weibull(1.0, 2.0)"),
	(weibull_min(5.0, scale=2.0), "Weibull(5.0, 2.0)")
]

print "distr, mean, var, entropy, x25, x50, x75, p25, p50, p75"

for (d, e) in lst:
	m = d.mean()
	v = d.var()
	ent = d.entropy()

	x25 = d.ppf(0.25)
	x50 = d.ppf(0.50)
	x75 = d.ppf(0.75)

	lp25 = d.logpdf(x25)
	lp50 = d.logpdf(x50)
	lp75 = d.logpdf(x75)

	# workaround inconsistency of definitions
	if e.startswith("Geometric("):
		x25 -= 1
		x50 -= 1
		x75 -= 1
		m -= 1

	elif e == "TDist(1.0)":
		m = nan

	print '"%s", %.16e, %.16e, %.16e, %.16e, %.16e, %.16e, %.16e, %.16e, %.16e' % (e, m, v, ent, x25, x50, x75, lp25, lp50, lp75)
