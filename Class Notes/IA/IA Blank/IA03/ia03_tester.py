"""Functions that generate a subset of common predictive patterns."""
import predictive_models as pm

# Use lm to create a linear model with a slope of 2, and an intercept of 10 and
# name the returned function lm1
lm1 = pm.lm(i=10, m=2)
print(lm1(1))  # prints the result of 10 + 2*(1)
print(lm1(0))  # prints the result from 10 + 2*(0)
print(lm1(-1.1))  # 10 + 2*(-1.1)

# Use lm to create a linear model with a slope of -2.2, and an intercept of
# 1001.23 and name the returned function lm2
lm2 = pm.lm(i=1001.23, m=-2.2)
print(lm2(1))  # print the result of 1001.23 + 1*(-2.2)
print(lm2(0))  # print the result of 1001.23 + 0*(-2.2)
print(lm2(-3.9))  # print the result of 1001.23 + (-3.9)*(-2.2)

# create a linear module using lm()
lm1 = pm.lm(i=10, m=2)
# create an exp tranform of lm
pm1 = pm.lm_p(l=lm1, p=2)
# use our new model to generate various output
print(pm1(2))  # 10+2(2**2)
print(pm1(10))  # 10+2(10**2)
print(pm1(127))  # 10+2(127**2)

# create an exp tranform of lm to the power of 3.5
pm2 = pm.lm_p(l=lm1, p=3.5)
# use our new model to generate various output
print(pm2(2))  # 10+2(2**3.5)
print(pm2(10))  # 10+2(10**3.5)
print(pm2(127))  # 10+2(127**3.5)

print(help(pm))


# Sample output
# $ python ia03_tester.py
# 12
# 10
# 7.8
# 999.03
# 1001.23
# 1009.8100000000001
# 18
# 210
# 32268
# 32.62741699796952
# 6334.555320336759
# 46168218.116213605
# Help on module predictive_models:

# NAME
#     predictive_models - Functions that generate a subset of common moduling patterns.

# FUNCTIONS
#     lm(i, m)
#         "Return a linear predictive model defined by intercept and slope.

#         ex: given lm1=lm(10,2), lm1(10)=210

#     lm_p(l, p)
#         Power transform lm (l) using given power (p).

#         ex: given lm -> f(x)=10+2x, then lm_p(lm,2.5) -> 10+2(x**2.5)

# FILE
#     e:\dropbox\___iastate\mis407\sandbox\individual_assignments\ia03\predictive_models.py


# None
