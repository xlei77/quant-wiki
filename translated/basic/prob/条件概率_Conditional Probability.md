---
{}
---

## What is Conditional Probability

Conditional probability is a fundamental concept in probability theory that deals with the probability of an event occurring given that another event has already occurred.

Conditional probability involves two or more interrelated events and poses the question: "If we know that event A has occurred, what is the probability that event B will occur?" The calculation of conditional probability is performed by multiplying the prior probability with the updated probability of the subsequent event (the conditional event).

### Key Points

- Conditional probability refers to the probability of an event (A) occurring given that another event (B) has already occurred.
- In probability notation, this is typically written as "A occurring given B": P(A|B), indicating that the probability of A depends on the probability of B occurring.
- Conditional probability contrasts with unconditional probability (or marginal probability).
- Probabilities can be categorized into conditional probability, marginal probability (base probability independent of other events), and joint probability (probability of two events occurring simultaneously).
- Bayes' theorem is a mathematical formula that can be used to calculate conditional probabilities related to uncertain events.

## Understanding Conditional Probability

Conditional probability measures the likelihood of a specific outcome (A) based on the occurrence of a prior event (B).

If the occurrence of one event does not affect the probability of another event occurring, these two events are called independent events. However, if the occurrence (or non-occurrence) of one event affects the likelihood of another event occurring, then these two events are related.

An example of related events is when a company's stock price rises following better-than-expected earnings reports.

If events are independent, then the probability of event B occurring is unrelated to whether event A occurs or not. For example, a rise in Apple's stock price has no relation to a fall in wheat prices.

Conditional probability is typically expressed as "A occurring given B" and is denoted as P(A|B).

- Conditional probability contrasts with unconditional probability, also known as marginal probability, which measures the probability of a single event occurring without dependence on any other events. In comparison, conditional probability determines the likelihood of one event given the occurrence of another event, thus linking them together.
- The probability of independent events lacks this interconnection and instead looks at the probability of an event in isolation, as it is considered independent.
- Joint probability is the probability of two events occurring simultaneously. From these concepts, we arrive at Bayes' theorem, which provides a mathematical way to reverse conditional probabilities. If you know the probability of event B occurring based on event A, you can calculate backwards to find the conditional probability of A given B.

Overall, while marginal and joint probabilities measure the likelihood of individual and paired events, conditional probability can measure the sequential and dependent relationships between events.

**Note:** Conditional probability is widely applied in insurance, economics, politics, and various mathematical fields.

## Conditional Probability Formula

$$ P(B|A) = P(A \text{ and } B) / P(A) $$

Or:

$$ P(B|A) = P(A∩B) / P(A) $$

Where the letters represent the following:

P = Probability

A = Event A

B = Event B

**Important:** Unconditional probability, also known as marginal probability, measures the likelihood of an event occurring without considering any prior or external event knowledge. Since this probability also ignores new information, it remains constant.

## Examples of Conditional Probability

Let's explain conditional probability using colored balls as an example, with the following steps:

Step 1: Understanding the Scenario

Initially, you have a bag containing six red balls, three blue balls, and one green ball. Therefore, there are 10 balls in total in the bag.

Step 2: Identifying Events

Define two events:

- Event A: Drawing a red ball from the bag
- Event B: Drawing a ball that is not green

Step 3: Calculate the probability of event B: P(B)

Event B is drawing a ball that is not green. Out of 10 balls, 9 are not green: 6 red balls and 3 blue balls.

$$ P(B) = (不是绿球的球数)/(总球数) = 9/10 $$

Step 4: Identify the intersection of events A and B: P(A∩B)

The intersection of events A and B involves drawing a ball that is both red and not green. Since all red balls are not green, the intersection is simply the event of drawing a red ball.

Step 5: Calculate the probability of the intersection of events A and B: P(A∩B)

$$ P(A∩B) = (红球数量)/(总球数) = 6/10 = 3/5 $$

Step 6: Calculate the conditional probability: P(A|B)

Using the conditional probability formula P(A|B), calculate the probability of drawing a red ball given that the drawn ball is not green.

$$ P(A|B) = P(A∩B)/P(B) = (3/5)/(9/10) = 2/3 $$

Result: The conditional probability of drawing a red ball, given that the drawn ball is not green, is 2/3.

Another example involves using a fair six-sided die. The steps are as follows:

Step 1: Understanding the Scenario

You have a fair six-sided die. You want to determine the probability of rolling an even number given that the number rolled is greater than 4.

Step 2: Identifying Events

For a six-sided die, the possible outcomes (sample space) are numbers 1 through 6. From this, two events can be defined:

- Event A: Rolling an even number. Event A means rolling {2, 4, 6}.
- Event B: Rolling a number greater than 4. Event B means rolling {5, 6}.

Step 3: Calculate the Probability of Each Event

The probability of each event can be calculated by dividing the number of favorable outcomes (the outcomes you're looking for) by the total number of outcomes in the sample space.

P(A) is the probability of rolling an even number. Out of six possible outcomes, there are three even numbers {2, 4, 6}. Therefore, P(A) = 3/6 = 1/2.

P(B) is the probability of rolling a number greater than 4. Out of six possible outcomes, only two numbers are greater than 4 {5, 6}. Therefore, P(B) = 2/6 = 1/3.

Step 4: Identify the Intersection of Events A and B

The intersection of events A and B includes outcomes that satisfy both conditions. In this case, there is only one outcome that is both even and greater than 4, which is rolling a 6.

Step 5: Calculate the Probability of the Intersection of Events A and B

Even though the previous content is simple, we should still explain in detail: P(A∩B) is the probability of rolling a 6, as 6 is the only number that is both even and greater than 4. Out of six possibilities, there is only one such outcome. So P(A∩B) = 1/6.

Step 6: Calculate the Conditional Probability: P(B|A)

The formula for conditional probability is:

$$ P(B|A) = P(A∩B) / P(A) $$

Plugging in the values, we get:

$$ P(B|A) = (1/6)/(1/2) = 1/3 $$

Result: This means that given the number rolled is even, the probability that it is greater than 4 is 1/3.

Another scenario involves a student applying for university admission while hoping to receive tuition and living expense subsidies. The steps to determine the conditional probabilities of receiving subsidies and scholarships are as follows:

Step 1: Understanding the Scenario

The student wants to understand the possibility of being admitted to the university. If admitted, the student hopes to receive an academic scholarship. And if possible, hopes to receive book, meal, and housing subsidies after receiving the scholarship.

Step 2: Identifying Events

There are three events:

- Event A: Being admitted to the university.
- Event B: Receiving a scholarship after admission.
- Event C: Receiving book, meal, and housing subsidies after getting the scholarship.

Step 3: Calculate the Probability of Admission (Event A)

The university admits 100 people out of every 1000 applications. Therefore, the probability of a student being admitted is P(A) = 100/1000 = 0.10 or 10%.

Step 4: Determine the Probability of Receiving a Scholarship Given Admission: P(B|A)

It is known that among admitted students, 10 out of every 500 receive scholarships. Therefore, the probability of receiving a scholarship after being admitted is:

$$ P(B|A) = 10/500 = 0.02 = 2\% $$

Step 5: Calculate the Probability of Being Admitted and Receiving a Scholarship

To calculate the probability of being admitted and receiving a scholarship, multiply the probability of admission by the conditional probability of receiving a scholarship given admission.

$$ P(A∩B) = P(A)×P(B|A) = 0.1×0.02 = 0.002 = 0.2\% $$

Step 6: Determine the Probability of Receiving Subsidies Given Scholarship: P(C|B)

It is known that 50% of students who receive scholarships get book, meal, and housing subsidies. Therefore, P(C|B) = 0.5 = 50%.

Step 7: Calculate the Probability of Being Admitted, Receiving a Scholarship, and Getting Subsidies

To calculate the probability of a student being admitted, receiving a scholarship, and further receiving subsidies, multiply the probabilities of these events.

$$ P(A∩B∩C) = P(A)×P(B|A)×P(C|B) = 0.1×0.02×0.5 = 0.001 = 0.1\% $$

This step-by-step analysis demonstrates how to use basic probability formulas and conditional probability to calculate probabilities for each scenario.

## Comparison of Conditional Probability, Joint Probability, and Marginal Probability

Let's distinguish between conditional probability and other types of probability calculations.

This time, we'll use a standard deck of playing cards as an example. Define two events:

- Event A: Drawing a four.
- Event B: Drawing a red card.

A standard deck has 52 cards, divided into four suits (Hearts, Diamonds, Clubs, and Spades). Hearts and Diamonds are red, while Clubs and Spades are black. Each suit has 13 cards: from Ace to 10, plus face cards J, Q, and K.

The deck contains 26 red cards, consisting of 13 Hearts and 13 Diamonds. Therefore, the probability of drawing a red card is P(B) = 26/52 = 1/2.

Among the red cards, there is one Four of Hearts and one Four of Diamonds. Thus, if we need to draw a red card, we must consider only the subset of these 26 red cards.

The probability of drawing a four, given that we've drawn a red card, is calculated as follows:

$$ P(B|A) = P(A∩B) / P(A) $$0

The marginal probability P(A) refers to the probability of event A occurring independently. It doesn't consider the occurrence of any other events.

Since event A is drawing a four, P(A) is calculated by dividing the number of fours by the total number of cards.

$$ P(B|A) = P(A∩B) / P(A) $$1

Joint probability is the likelihood of two or more events occurring simultaneously. This is typically denoted as P(A∩B), representing the probability of both events A and B occurring together.

Keeping the previous events unchanged, where event A is drawing a four and event B is drawing a red card, we can find the joint probability of drawing both a four and a red card.

There are two cards that satisfy both conditions: the Four of Hearts and the Four of Diamonds. Therefore, the joint probability of drawing a four that is also a red card is calculated as:

$$ P(B|A) = P(A∩B) / P(A) $$2

## Bayes' Theorem and Conditional Probability

Bayes' Theorem is used to calculate conditional probabilities when dealing with uncertain events. In investing, this can be used to update probability estimates of market outcomes after receiving new relevant data.

For example, suppose you want to know the probability that the S&P 500 will return a positive percentage this year, given initial Gross Domestic Product (GDP) data. In this case, you would first use Bayes' Theorem, considering the index's historical returns, to obtain a preliminary expectation of economic expansion.

You would then modify this preliminary probability based on the latest GDP forecasts. This provides a more refined probability assessment that integrates all evidence as the year progresses.

Although mathematically somewhat complex, Bayes' Theorem is quite logical. If investors discover new economic information relevant to potential market returns, it makes sense to integrate this data to obtain more precise calculations.

This statistical technique, developed by 18th-century English clergyman Thomas Bayes, remains central to financial modeling and other fields requiring predictions under uncertain conditions.

**Note:** Bayes' Theorem is particularly well-suited for machine learning and is widely used in that field.

## What is a Conditional Probability Calculator?

A conditional probability calculator is an online tool that can calculate conditional probabilities. It provides the probabilities of first and second events occurring, thus saving users the trouble of performing mathematical calculations manually.

## What is the difference between probability and conditional probability?

Probability focuses on the likelihood of an event occurring. Conditional probability focuses on the relationship between two events occurring, more specifically, conditional probability is the probability of the second event occurring given that the first event has occurred.

## What is Prior Probability?

Prior probability is the probability of an event occurring before collecting any data. It is determined by prior beliefs. In Bayesian statistical inference, prior probability is one component, as you can revise these beliefs and mathematically derive the posterior probability.

## What is Compound Probability?

Compound probability aims to determine the likelihood of two independent events occurring. Compound probability multiplies the probability of the first event by the probability of the second event. The most common example is flipping a coin twice and finding out whether the second result matches the first one.

## Conclusion

Conditional probability examines the likelihood of an event occurring based on the probability of a prior event. The second event is dependent on the occurrence of the first event.

For example, we might want to know the probability that a stock will rise given that its industry index has increased. Conditional probability calculations consider both the likelihood of the first event (stock price increase) and the overlap between these two events.