---
{}
---

## What is Monte Carlo Simulation?

Monte Carlo simulation is a modeling method used to predict the probabilities of various outcomes in processes that are difficult to forecast due to random variable intervention. It is a technique used to understand the impact of risk and uncertainty. Monte Carlo simulation can be applied to various problems across multiple fields, including investments, business, physics, and engineering. This technique is also known as multiple probability simulation.

### Key Points

- Monte Carlo simulation is a model used to predict the probability of different outcomes in the presence of random variables.
- Monte Carlo simulation helps explain the impact of risk and uncertainty in prediction and forecasting models.
- Monte Carlo simulation requires assigning multiple values to an uncertain variable to obtain multiple outcomes, then averaging the results to arrive at an estimate.
- These simulations assume markets are perfectly efficient.
- Monte Carlo simulations are increasingly being used in combination with artificial intelligence.

## How Monte Carlo Simulation Evaluates Risk

When making predictions or estimates in the face of significant uncertainty, some methods replace uncertain variables with a single average. Monte Carlo simulation, however, uses multiple values and then averages the results.

Monte Carlo simulations have wide applications in fields affected by random variables, particularly in business and investment. They are used to estimate the probability of cost overruns in large projects and to predict the likelihood of asset prices moving in specific directions.

Telecommunications companies use Monte Carlo simulations to evaluate network performance under various scenarios to optimize network performance. Insurance companies use these simulations to quantify potential risks and set policy prices accordingly. Investment analysts use Monte Carlo simulations to assess the risk of an entity defaulting and analyze derivatives such as options. Financial planners can use these simulations to predict the probability of clients running out of funds during retirement.[1]

Monte Carlo simulations are also widely used in many fields beyond business and finance, such as meteorology, astronomy, and physics.

Today, Monte Carlo simulations are increasingly being combined with new artificial intelligence (AI) models. For example, according to IBM's 2024 report, many financial companies now run Monte Carlo simulations on high-performance computing systems, "as these simulations grow in number, covering an expanding range of financial assets and instruments, comprehensively interpreting this data becomes increasingly challenging." This is where AI comes in. IBM states, "Using AI to assist professionals in evaluating these simulations can improve accuracy and provide more timely insights. In a business environment where timeliness is a key differentiator, this has direct business value."[2]

## History of Monte Carlo Simulation

Monte Carlo simulation is named after Monaco's famous gambling destination because chance and random outcomes are at the core of this modeling technique, just like in roulette, dice, and slot machine games.

This technique was originally developed by mathematician Stanislaw Ulam, who worked on the Manhattan Project, the secret project to create the first atomic bomb. He shared his ideas with his Manhattan Project colleague John von Neumann, and together they refined the Monte Carlo simulation.[3]

## How Monte Carlo Simulation Works

Monte Carlo methods acknowledge the challenge faced by any simulation technique: due to the interference of random variables, it's impossible to precisely determine the probabilities of different outcomes. Therefore, Monte Carlo simulation focuses on repeatedly generating random samples.

Monte Carlo simulation assigns random values to uncertain variables. It then runs the model and provides results. This process is repeated over and over, assigning many different values to the relevant variables. Once the simulation is complete, the results are averaged to obtain an estimate.

## Four Steps of Monte Carlo Simulation

To perform a Monte Carlo simulation, there are four main steps. Using Microsoft Excel or similar programs as an example, you can create a Monte Carlo simulation to estimate price movements of stocks or other assets.

Asset price movements have two components: drift, which is its constant directional movement, and random input, representing market volatility.

By analyzing historical price data, you can determine a security's drift, standard deviation, variance, and average price movement. These are the basic building blocks of Monte Carlo simulation.

The four steps are as follows:

Step 1. Using the asset's historical price data, generate a series of periodic daily returns using natural logarithm (note that this formula differs from the common percentage change formula) to predict a possible price trajectory:

Step 2. Next, process the entire series of results using AVERAGE, STDEV.P, and VAR.P functions to obtain the average daily return, standard deviation, and variance inputs respectively. The drift equals:

Alternatively, drift can be set to 0; this choice reflects a theoretical orientation, but for short time frames, the difference won't be significant.

Step 3. Next, obtain the random input:

The price equation for the next day is:

Step 4. In Excel, to raise e to a given power x, use the EXP function: EXP(x). Repeat this calculation as many times as needed. (Each repetition represents one day.) The result is a simulation of the asset's future price movements.

By generating any number of simulations, you can evaluate the probability of a security's price following specific trajectories.

## Interpreting Monte Carlo Simulation Results

The frequency of different outcomes generated by the simulation will form a normal distribution, also known as a bell curve. The most likely returns are located in the middle of the curve, meaning there are equal chances of actual returns being higher or lower than this value.

There is a 68% probability that actual returns will fall within one standard deviation of the most likely ("expected") return. The probability is 95% within two standard deviations, and 99.7% within three standard deviations.

However, there is no guarantee that the most expected outcome will occur, or that actual movements won't exceed even the wildest predictions.

Crucially, Monte Carlo simulation ignores all factors not incorporated into price volatility, such as macro trends, company leadership, market hype, and cyclical factors.

In other words, it assumes the market is perfectly efficient.

## Advantages and Disadvantages of Monte Carlo Simulation

Monte Carlo simulation was created to overcome perceived limitations of other methods for estimating possible outcomes.

The difference lies in that Monte Carlo methods test multiple random variables and then average them, rather than starting from a single average value.

Like any financial simulation, Monte Carlo methods rely on historical price data as a basis for predicting future price data. It then disrupts this pattern by introducing random variables, which are represented numerically. Finally, it averages these numbers to estimate the risk of the pattern being disrupted in real life.

Of course, no simulation can accurately predict inevitable outcomes. The Monte Carlo method aims to provide more scientific probability estimates to predict how an outcome might differ from expectations.

## Monte Carlo Simulation Applications in Finance

Monte Carlo simulation is used to estimate the probability of certain outcomes, and is therefore widely used by investors and financial analysts to evaluate the potential success rate of their considered investments. Common applications include:

- Stock Option Pricing: Tracking potential price movements of the underlying asset under each possible variable. The results are then averaged and discounted to the asset's current price. This aims to indicate the potential returns of the option.
- Portfolio Valuation: Monte Carlo simulation can be used to test multiple alternative portfolios to derive measurements of their relative risks.
- Fixed Income Investments: Short-term interest rates are the random variables here. The simulation is used to calculate the potential impact that short-term interest rate fluctuations may have on fixed income investments (such as bonds).

## Which Industries Use Monte Carlo Simulation?

Although Monte Carlo simulation is best known for its financial applications, this method is used in almost all professions that need to measure and prepare for risks.

For example, a telecommunications company might build its network to support the needs of all users. To achieve this goal, it must consider all possible variations in service demand. It needs to determine whether the system can withstand the pressure during peak hours and peak seasons.

Monte Carlo simulation can help companies decide whether their services can handle the pressure of Super Bowl Sunday, as well as the pressure of a regular Sunday in August.

## Factors Evaluated in Monte Carlo Simulation

Monte Carlo simulation in investment is based on historical price data of the evaluated assets.

The basic building blocks of the simulation are derived from historical data, namely drift, standard deviation, variance, and average price fluctuation.

## Conclusion

Monte Carlo simulation demonstrates the spectrum of possible outcomes under uncertain scenarios. This technique assigns multiple values to uncertain variables, obtains multiple results, and then averages these results to arrive at an estimate.

From investment to engineering, Monte Carlo methods are used in many fields to measure risk, including estimating the probability of investment gains or losses, or the likelihood of a project exceeding its budget.

## References

[1] T. Rowe Price. "[How a Monte Carlo Analysis Could Help Improve Your Retirement Plan](https://www.troweprice.com/personal-investing/resources/insights/how-monte-carlo-analysis-could-improve-your-retirement-plan.html)."

[2] IBM. "[Working Together, AI & HPC Can Solve Large, Complex Problems](https://community.ibm.com/community/user/cloud/blogs/john-easton/2024/03/25/working-together-ai-hpc-can-solve-large-complex-ch?CommunityKey=74d589b7-7276-4d70-acf5-0fc26430c6c0)."

[3] Virginia Polytechnic Institute, via Internet Archive Wayback Machine. "[Monte Carlo Simulation](https://web.archive.org/web/20201025115012/https://sites.google.com/a/vt.edu/monte-carlo-simulation/history)."