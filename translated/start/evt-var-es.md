---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# A Complete Guide to Understanding Tail Risk in Financial Markets: Application of Extreme Value Theory (EVT) in VaR and ES Calculations
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Extreme Value Theory (EVT): Tail Risk Modeling

In financial risk management, Extreme Value Theory (EVT) is an important tool used for analyzing and modeling the tail behavior of data distributions. Particularly in financial markets, extreme market fluctuations and risk events often lead to significant economic losses, and EVT helps us better understand and predict the probability and impact of these extreme events.

## Two Main Methods of Extreme Value Theory

The core idea of extreme value theory is to model the extreme values of data, and there are typically two popular parametric methods: **Block Maxima Method** and **Peak-Over-Threshold (POT) Method**.

### Block Maxima Method

The fundamental idea of the **Block Maxima** method is to divide historical data into multiple blocks (e.g., by month, quarter, or year), and then extract the maximum value from each block. These maximum values form the sample we use to model tail risk.

Assume we have some independent and identically distributed (iid) random variables with cumulative distribution function **F(x)** and **n** observations. We want to model the statistical behavior of **Mₙ = max(X₁, X₂, ..., Xₙ)**. Through the relationship of cumulative probability distribution, the distribution of maximum values can be expressed as:

$$
Pr(M_n \leq z) = Pr(X_1 \leq z, \ldots, X_n \leq z) = (F(z))^n
$$

However, we usually cannot obtain the true distribution function F(x). Fortunately, the **Fisher-Tippett-Gnedenko theorem** states that, with appropriate scaling, the distribution of maxima converges to one of three specific distributions: the **Gumbel distribution**, **Fréchet distribution**, and **Weibull distribution**. The combined form of these distributions is the Generalized Extreme Value (GEV) distribution:

$$
G(x) = \exp \left\{- \left[1 + \xi \left(\frac{x - \mu}{\sigma}\right)\right]^{-1/\xi}\right\}
$$

where **μ** is the location parameter, **σ** is the scale parameter, and **ξ** is the shape parameter. Different ξ values determine the tail behavior:

- When **ξ = 0**, we get the Gumbel distribution
- When **ξ < 0**, we get the Fréchet distribution
- When **ξ > 0**, we get the Weibull distribution

Using the `fExtremes` package in R, you can plot the density graphs of these distributions to help understand the tail behavior under different ξ values.


![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/02/15/1739614133652-5a5c0ac5-0c4f-4bb7-a076-75928efb3481.png)

#### Data Fitting: Block Maxima Method

How do we fit the Generalized Extreme Value (GEV) distribution to actual data? For example, in financial markets, we can use daily return data, divide it into monthly time blocks, and model the maximum loss for each month. This way, we can estimate the tail of the loss distribution.

```r
require(quantmod)
require(xts)
SPY_prices <- Ad(getSymbols('SPY', from = '2006-01-01', to = '2019-01-01', auto.assign = FALSE))
returns_xts <- diff(log(SPY_prices), k = 1)[-1] * 100  # 每日对数收益
```

#### Convert to Losses (Positive Values of Negative Returns) and Calculate Monthly Maximum Losses
```r
monthly_max_daily_loss <- do.call(rbind, lapply(split(x = -1 * returns_xts, 'months'), function(x) x[which.max(x)]))
```
Through the above code, we convert daily return data into monthly maximum losses, and then use Maximum Likelihood Estimation (MLE) to fit GEV distribution parameters.

Risk Estimation: VaR and ES
Using the fitted GEV distribution parameters, we can calculate risk metrics such as **VaR (Value at Risk) and ES (Expected Shortfall)**. For example, VaR can be calculated using the inverse cumulative distribution function:
```r
GEV_VAR <- function(params, alpha = .05){
    mu    <- rep(params[1], length(alpha))
    sigma <- rep(params[2], length(alpha))
    xi    <- rep(params[3], length(alpha))
    y <- -log(1 - alpha)
    result <- ifelse(abs(xi) < 0.0001, mu - sigma * log(-y), mu - sigma / xi * (1 - y ^ -xi))
    return(result)
}
```
By inputting the fitted parameters into the VaR function, we can calculate VaR values at different confidence levels.
```r
my_fit_vals <- my_gev_fit$par
GEV_VAR(my_fit_vals, alpha = c(.05, .025, .01))
```
----

### Peak-Over-Threshold Method

The **Peak-Over-Threshold (POT)** method differs from the Block Maxima method in that it focuses on all observations exceeding a specified threshold. The POT method typically captures tail risk more effectively, especially when multiple extreme values exist in the data.

In the POT method, we use the **Generalized Pareto Distribution (GPD)** to describe observations above the threshold. Through the **Pickands-Balkema-de Haan theorem**, we know that for sufficiently high thresholds, the conditional distribution of the data will approximate a Generalized Pareto Distribution:

$$
P(X \leq x | X > u) \approx \left\{
\begin{array}{ll}
1 - \left( 1 + \xi \frac{x}{\tau} \right)^{-1/\xi} & \text{当} \xi \neq 0 \\
1 - \exp \left( -\frac{x}{\tau} \right) & \text{当} \xi = 0
\end{array}
\right.
$$

Here, the parameters **ξ** and **τ** are similar to those in the GEV distribution and are used to fit the data exceeding the threshold.

#### Data Fitting: POT Method

When using the POT (Peaks Over Threshold) method, we first set a threshold **u**, then filter out all observations exceeding this threshold. Next, we fit these exceedances, typically modeling them using the **Generalized Pareto Distribution (GPD)**.

Below is a code example of fitting the POT model in R, first loading the data and setting the threshold:

```r
require(quantmod)
require(xts)

SPY_prices <- Ad(getSymbols('SPY', from = '2006-01-01', to = '2019-01-01', auto.assign = FALSE))
returns_xts <- -1 * diff(log(SPY_prices), k = 1)[-1] * 100  # 每日对数收益
names(returns_xts) <- 'SPY_Returns'

# 设置阈值
my_threshold <- 0.85

# 筛选出超过阈值的数据
my_data <- returns_xts[returns_xts > my_threshold]
```
Next, we can use the log-likelihood function for parameter estimation:
```r
gdp_loglik <- function(params, threshold, data){
    xi <- params[1]; tau <- params[2]
    data <- data - threshold  # y = x - u
    data <- coredata(data[data > 0])  # 只保留超过阈值的数据
    m <- nrow(data)
    if((tau <= 0) | (xi <= -1)) return(1e6)  # 参数约束
    term1 <- -m * log(tau)
    if(abs(xi) < 0.0001){
        result <- term1 - 1 / tau * sum(data)
    } else {
        if(any(1 + xi * data / tau <= 0)) return(1e6)
        result <- term1 - (1 + 1 / xi) * sum(log(1 + xi * data / tau))
    }
    return(-result)
}
```
By maximizing the log-likelihood function, we can obtain estimates for ξ and τ
```r
my_gpd_fit <- optim(par = c(0.5, 0.5), fn = gdp_loglik, method = "Nelder-Mead", threshold = my_threshold, data = returns_xts)
my_gpd_fit
```

### Risk Calculation: VaR and ES

Using the fitted GEV distribution parameters, we can calculate risk metrics such as **VaR (Value at Risk)** and **ES (Expected Shortfall)**. For example, VaR can be calculated using the inverse cumulative distribution function:

#### VaR (Value at Risk) Calculation

VaR is a quantile value at a certain confidence level. To calculate VaR, we need to use the inverse function of the cumulative distribution function. The specific formula is as follows:

$$
\hat{z}_p = \left\{
\begin{array}{ll}
\mu - \frac{\sigma}{\hat{\xi}} \left[ 1 - y_p^{-\xi} \right] & \text{当} \hat{\xi} \neq 0 \\
\hat{\mu} - \hat{\sigma} \log (-y_p) & \text{当} \hat{\xi} = 0
\end{array}
\right.
$$

Where $y_p = -\log(1 - p)$, $p$ is the confidence level (for example, 0.05 represents a 95% confidence interval).

Below is the R code implementation for calculating VaR:

```r
GEV_VAR <- function(params, alpha = .05){
    # 将参数展开为向量
    mu    <- rep(params[1], length(alpha))
    sigma <- rep(params[2], length(alpha))
    xi    <- rep(params[3], length(alpha))
    
    y <- -log(1 - alpha)
    result <- ifelse(abs(xi) < 0.0001, mu - sigma * log(-y), mu - sigma / xi * (1 - y ^ -xi))
    return(result)
}
使用上述函数，可以计算不同置信度下的VaR值：
```r
my_fit_vals <- my_gev_fit$par
GEV_VAR(my_fit_vals, alpha = c(.05, .025, .01))
```
#### ES（预期损失）计算

**ES**（即条件VaR）表示在发生极端损失时，平均损失的大小。它反映了在损失超过VaR时，风险的严重程度。计算ES的公式如下：

$$
\mathrm{ES}_{\alpha} = \frac{1}{1 - \alpha} \int_{\alpha}^{1} q_x(F) \, \mathrm{d}x = \frac{VAR_{\alpha}}{1 - \xi} + \frac{\tilde{\sigma} - \xi u}{1 - \xi}
$$

其中，$\hat{z}_p$为VaR值，$\alpha$为风险水平（例如，0.01代表1%风险水平）。

在R语言中，计算ES的实现如下：

```r
GEV_ES <- function(params, alpha = .05){
    # 定义一个函数来计算VAR值
    my_fun <- function(x) {GEV_VAR(x, params = params)}
    
    # 数值积分，计算ES
    result <- 1 / alpha * integrate(my_fun, lower = .00001, upper = alpha, stop.on.error = FALSE)$value
    return(result)
}
```
通过上述代码，我们可以计算在特定置信度下的ES值。例如，对于1%的风险水平，我们可以运行：
```r
GEV_ES(my_fit_vals, alpha = .01)
```
This calculation result tells us the average size of losses during extreme loss events. If we know the VaR is 8.66%, the ES result would likely be larger because ES considers more extreme loss scenarios.

Through using ES, financial institutions and investors can better evaluate risks and prepare for larger potential losses during extreme market fluctuations.

## Summary

Extreme Value Theory (EVT) provides powerful tools for tail risk management in financial markets, particularly when facing extreme market volatility, helping decision-makers develop more rational risk control strategies. Through **Block Maxima** and **Peak-Over-Threshold** methods, we can effectively estimate tail risks and conduct fitting and risk assessment using the **Generalized Extreme Value (GEV) distribution** and **Generalized Pareto Distribution (GPD)**.

In practical applications, by calculating risk metrics such as **VaR (Value at Risk)** and **ES (Expected Shortfall)**, investors and financial institutions can quantify the impact of extreme events and implement appropriate risk control measures. VaR provides a boundary for potential losses at a specific confidence level, while ES further considers the average magnitude of extreme losses, helping us better understand tail risks.

If you would like to learn more about how to apply these methods in practice, welcome to join our knowledge community to unlock more professional techniques and code examples, helping you take more solid steps in financial risk management.