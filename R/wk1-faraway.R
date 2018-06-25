# install faraway package
install.packages("lme4")
install.packages("faraway")

# import coagulation data
data(package = 'faraway')
data(coagulation, package='faraway')
summary(coagulation)

plot(coag ~ diet, coagulation)
coagulation$diet
coagulation$coag

coag_model = lm(coag ~ diet - 1, data = coagulation)
summary(coag_model)

# import rats package
data(rats, package='faraway')
plot(time ~ poison, rats)
plot(time ~ treat, rats)

# plot histogram with smooth density line
data <- c(78, 49, 91, 44, 84, 45, 30, 84, 53, 38, 12, 64, 54, 78, 31, 45, 32, 88, 93, 64, 69)
hist(data, col = "yellow", freq = F)
lines(density(data), col = "red")

# plot scatterplot
set.seed(2016)
scores1=round(rnorm(50, 78, 10))
scores2=round(rnorm(50, 78, 10))
plot(scores2~scores1, col='red')

# plot co2 with linear model
help(co2)
plot(co2)
co2_model = lm(co2 ~ time(co2))
plot(co2)
abline(co2_model)
summary(co2_model)
coef(co2_model)

# Quiz
x=c(1,2,3,4);
y=c(5, 7, 12, 13);
m=lm(y~x)
plot(x, y)
abline(m)
coef(m)

# Compute residuals
co2_resid  <- resid(co2_model)
co2_resid_norm = rnorm(length(co2_resid), mean = mean(co2_resid), sd = sd(co2_resid))
par(mfrow = c(1,4))
hist(co2_resid)
lines(density(co2_resid_norm), col = 'red')

qqnorm(co2_resid)
qqline(co2_resid)
plot(co2_resid)
plot(co2_resid ~ time(co2), xlim = c(1960, 1963))

# sleeping aides data 
attach(sleep)
plot(extra ~ group)
t.test(extra[group == 1], extra[group == 2], paired = T, alternative = 'two.sided')

help(t.test)
