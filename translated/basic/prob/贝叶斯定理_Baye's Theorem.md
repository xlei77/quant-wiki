---
{}
---

Bayes' Theorem, named after 18th-century British mathematician Thomas Bayes, is a mathematical formula used to determine conditional probabilities. Conditional probability refers to the likelihood of an outcome occurring under similar circumstances. Bayes' Theorem provides a method for revising existing predictions or theories (updating probabilities) when new evidence or additional information becomes available.

In finance, Bayes' Theorem can be used to evaluate the risk of lending to potential borrowers. The theorem, also known as Bayes' Rule or Bayes' Law, forms the foundation of Bayesian statistics.

### Key Points

- Bayes' Theorem allows you to update the predicted probability of events by incorporating new information.
- Bayes' Theorem is named after 18th-century mathematician Thomas Bayes.
- It is commonly used in finance to calculate or update risk assessments.
- Due to its requirement for extensive computational power, Bayes' Theorem remained unused for two centuries.

## Understanding Bayes' Theorem

Bayes' Theorem has wide-ranging applications beyond just the financial domain. For example, Bayes' Theorem can be used to evaluate the accuracy of medical test results by considering both the likelihood of a person having a disease and the general accuracy of the test. Bayes' Theorem relies on introducing prior probability distributions to generate posterior probabilities.

In Bayesian statistical inference, prior probability refers to the probability of an event occurring before new data is collected. In other words, it represents the best rational assessment of the probability of a specific outcome based on current knowledge before an experiment is conducted.

Posterior probability is the revised probability of an event occurring after considering new information. Posterior probability is calculated by updating the prior probability using Bayes' Theorem. From a statistical perspective, posterior probability is the probability of event A occurring, given that event B has already occurred.

## Special Considerations

Therefore, Bayes' theorem provides the probability of an event occurring based on new information related to that event. The formula can also be used to determine how assumed new information would affect the probability of an event occurring, provided that the assumed new information proves to be true.

For example, consider drawing a card from a complete deck of 52 playing cards.

There are four kings in the deck, so the probability of drawing a king is four divided by 52, which equals 1/13, or approximately 7.69%. Now, suppose it is revealed that the selected card is a face card. Given the condition that the face card is a king, the probability that the selected card is a king is four divided by 12, approximately 33.3%, because there are 12 face cards in the deck.

## Bayes' Theorem Formula

## Examples of Bayes' Theorem

Here are two examples of Bayes' Theorem. The first example demonstrates how to derive the formula using a stock investment example with Amazon.com Inc. (AMZN). The second example applies Bayes' Theorem to drug testing.

Bayes' Theorem simply comes from the axioms of conditional probability, which is the probability of one event occurring given that another event has occurred. For example, a simple probability question might be: "What is the probability that Amazon's stock price will fall?" Conditional probability further asks: "What is the probability that AMZN stock price will fall, given that the Dow Jones Industrial Average (DJIA) has previously fallen?"

The conditional probability of A, given that B has occurred, can be expressed as:

If A is: "AMZN price falls," then P(AMZN) is the probability of AMZN falling; B is: "Dow Jones has fallen," P(DJIA) is the probability of Dow Jones falling; then the conditional probability expression is "the probability of AMZN falling given DJIA has fallen equals the joint probability of AMZN price falling and DJIA falling divided by the probability of DJIA falling."

P(AMZN and DJIA) is the probability of both A and B occurring simultaneously. This equals the probability of A occurring multiplied by the probability of B occurring given that A has occurred, i.e., P(AMZN) x P(DJIA|AMZN). The fact that these two expressions are equal leads to the formation of Bayes' Theorem, expressed as:

P(AMZN) and P(DJIA) are the independent probabilities of Amazon and Dow Jones falling.

The formula explains the relationship between the probability of a hypothesis P(AMZN) before seeing evidence and the probability of the hypothesis P(AMZN|DJIA) after acquiring evidence, based on the Dow Jones proof.

As a numerical example, consider a drug test that is 98% accurate, meaning it shows correct positive results 98% of the time for users and correct negative results 98% of the time for non-users.

Next, assume that 0.5% of people use the drug. If a randomly selected person tests positive, the following calculation can be made to determine the probability that this person actually uses the drug, involving these terms:

- A = Probability of true positive test results
- B = Proportion of people who use the drug
- A x B = Probability of true positive test results
- (1 - A) x (1 - B) = Probability of true negative test results

The formula will show as follows:

Using these values, the calculation results in:

Bayes' Theorem shows that even in this case where a person tests positive, their probability of using the drug is only 19.76%, while the probability of not using the drug is 80.24%.

## What is the purpose of Bayes' Rule?

Bayes' Rule is used to update probabilities with new conditional variables. Investment analysts use it to predict probabilities in the stock market, but it has applications across many other industries.

## Why is Bayes' Theorem So Powerful?

Mathematically, it shows that two probabilities are equal. Whether in statistics, investing, or other industries, this enables you to examine conditional probabilities.

## How to Determine When to Use Bayes' Theorem?

If you need to determine the probability of an event occurring, given that there are other conditions that may influence the occurrence of that event, you can use Bayes' Theorem.

## Conclusion

In its simplest form, Bayes' theorem connects test results with their conditional probabilities under other related events. For high-probability false positives, the theorem provides a more reasonable likelihood of certain outcomes.