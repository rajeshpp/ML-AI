Google crash course for ML:
==============================================

Day 1: Supervised Machine learning
----------------------------------------------------------

**What is [(supervised) machine learning](https://developers.google.com/machine-learning/glossary/#supervised_machine_learning)?** ML systems learn how to combine input to produce useful predictions on never-before-seen data.

**Labels:** A [label](https://developers.google.com/machine-learning/glossary#label) is the thing we're predicting—the y variable in simple linear regression. The label could be the future price of wheat, the kind of animal shown in a picture, the meaning of an audio clip, or just about anything.

**Features:** A [feature](https://developers.google.com/machine-learning/glossary#feature) is an input variable—the x variable in simple linear regression. A simple machine learning project might use a single feature, while a more sophisticated machine learning project could use millions of features, specified as: x1, x2,....,xn. <br>
  &nbsp;&nbsp;&nbsp;In the spam detector example, the features could include the following:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. words in the email text<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. sender's address<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. time of day the email was sent<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. email contains the phrase "one weird trick."<br>

**Examples:** An **[example](https://developers.google.com/machine-learning/glossary#example)** is a particular instance of data, x. (We put x in boldface to indicate that it is a vector.) We break examples into two categories:<br>
&nbsp;&nbsp;&nbsp;1. labeled examples<br>
&nbsp;&nbsp;&nbsp;2. unlabeled examples<br>
&nbsp; A **labeled example** includes both feature(s) and the label. That is:  *labeled examples: <pre>{features, label}: (x, y)* </pre>

Use labeled examples to train the model. In our spam detector example, the labeled examples would be individual emails that users have explicitly marked as "spam" or "not spam." <br>

For example, the following table shows 5 labeled examples from a data set containing information about housing prices in California:<br>
![Labled Example](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/Labled%20Example.PNG)

An **unlabeled example** contains features but not the label. That is: *unlabeled examples: <pre>{features, ?}: (x, ?)* </pre>

Here are 3 unlabeled examples from the same housing dataset, which exclude *medianHouseValue*: <br>
![Unlabled Example](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/Unlabled%20Example.PNG)

Once we've trained our model with labeled examples, we use that model to predict the label on unlabeled examples. In the spam detector, unlabeled examples are new emails that humans haven't yet labeled.

**Models:** A [model](https://developers.google.com/machine-learning/glossary#model) defines the relationship between features and label. For example, a spam detection model might associate certain features strongly with "spam". Let's highlight two phases of a model's life: <br>
 * **[Training](https://developers.google.com/machine-learning/glossary#training)** means *creating* or *learning* the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.<br>
 * **[Inference](https://developers.google.com/machine-learning/glossary#inference)** means applying the trained model to unlabeled examples. That is, you use the trained model to make useful predictions (y'). For example, during inference, you can predict medianHouseValue for new unlabeled examples. <br>


**Regression vs. classification** <br>
A **[regression model](https://developers.google.com/machine-learning/glossary#regression_model)** predicts continuous values. For example, regression models make predictions that answer questions like the following:<br>
* What is the value of a house in California? <br>
* What is the probability that a user will click on this ad? <br>

A **classification** model predicts discrete values. For example, [classification models](https://developers.google.com/machine-learning/glossary#classification_model) make predictions that answer questions like the following: <br>
* Is a given email message spam or not spam?
* Is this an image of a dog, a cat, or a hamster?

Day 2: Linear regression
----------------------------------------------

**[Linear regression](https://developers.google.com/machine-learning/glossary#linear_regression)** is a method for finding the straight line or hyperplane that best fits a set of points. This module explores linear regression intuitively before laying the groundwork for a machine learning approach to linear regression.

**Figure 1. Chirps per Minute vs. Temperature in Celsius.**
![Unlabled Example](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/Linear%20Regression%20Example.PNG)

True, the line doesn't pass through every dot, but the line does clearly show the relationship between chirps and temperature. Using the equation for a line, you could write down this relationship as follows:<br>
<pre>                                              y = mx + b                     </pre>
**where:**
 * ***y*** is the temperature in Celsius—the value we're trying to predict.
 * ***m*** is the slope of the line.
 * ***x*** is the number of chirps per minute—the value of our input feature.
 * ***b*** is the y-intercept.

By convention in machine learning, you'll write the equation for a model slightly differently:<br>
<pre>                                              y' = b + w1x1                     </pre>

**where:**
 * ***y'*** is the predicted [label](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology#labels) (a desired output).
 * ***b*** is the [bias](https://developers.google.com/machine-learning/glossary#bias) (the y-intercept), sometimes referred to as .
 * ***w1*** is the [weight](https://developers.google.com/machine-learning/glossary#weight) of feature 1. Weight is the same concept as the "slope"  in the traditional equation of a line.
 * ***x1*** is a [feature](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology#features) (a known input).


To **[infer](https://developers.google.com/machine-learning/glossary#inference)** (predict) the temperature y′ for a new chirps-per-minute value x1, just substitute the x1 value into this model. <br>

Although this model uses only one feature, a more sophisticated model might rely on multiple features, each having a separate weight (w1, w2, etc.). For example, a model that relies on three features might look as follows: <br>

<pre>                                              y′=b+w1x1+w2x2+w3x3                     </pre>

Day 3: Training and Loss
-----------------------------------------------------
[Training](https://developers.google.com/machine-learning/glossary#training) a model simply means learning (determining) good values for all the weights and the bias from labeled examples. In supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called [empirical risk minimization](https://developers.google.com/machine-learning/glossary#ERM). <br>

Loss is the penalty for a bad prediction. That is, [loss](https://developers.google.com/machine-learning/glossary#loss) is a number indicating how bad the model's prediction was on a single example. If the model's prediction is perfect, the loss is zero; otherwise, the loss is greater. The goal of training a model is to find a set of weights and biases that have low loss, on average, across all examples. <br>
* The red arrow represents loss.
* The blue line represents predictions.
![LossSideBySide](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/LossSideBySide.png)
**High loss in the left model; low loss in the right model.**

We can create a mathematical function—a loss function—that would aggregate the individual losses in a meaningful fashion.<br>

**[Squared loss](https://developers.google.com/machine-learning/glossary#squared_loss): a popular loss function** <br>
The **[linear regression](https://developers.google.com/machine-learning/glossary#linear_regression)** models we'll examine here use a loss function called [squared loss](https://developers.google.com/machine-learning/glossary#squared_loss) (also known as L2 loss). The squared loss for a single example is as follows:
<pre>
  = the square of the difference between the label and the prediction
  = (observation - prediction(x))2
  = (y - y')2
</pre>

[Mean square error (MSE)](https://developers.google.com/machine-learning/glossary#MSE) is the average squared loss per example over the whole dataset. To calculate MSE, sum up all the squared losses for individual examples and then divide by the number of examples: <br>
![MeanSquareError](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/MeanSquareError.PNG)
where:
* (x,y) is an example in which
  * x is the set of features (for example, chirps/minute, age, gender) that the model uses to make predictions.
  * y is the example's label (for example, temperature).
* prediction(x) is a function of the weights and bias in combination with the set of features x.
* D is a data set containing many labeled examples, which are (x,y) pairs.
* N is the number of examples in D. <br>

Although [MSE](https://developers.google.com/machine-learning/glossary#MSE) is commonly-used in machine learning, it is neither the only practical loss function nor the best loss function for all circumstances.
