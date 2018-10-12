Google crash course for ML:
==============================================
**What is (supervised) machine learning?** ML systems learn how to combine input to produce useful predictions on never-before-seen data.

**Labels:** A label is the thing we're predicting—the y variable in simple linear regression. The label could be the future price of wheat, the kind of animal shown in a picture, the meaning of an audio clip, or just about anything.

**Features:** A feature is an input variable—the x variable in simple linear regression. A simple machine learning project might use a single feature, while a more sophisticated machine learning project could use millions of features, specified as: x1, x2,....,xn. <br>
  &nbsp;&nbsp;&nbsp;In the spam detector example, the features could include the following:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. words in the email text<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. sender's address<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. time of day the email was sent<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. email contains the phrase "one weird trick."<br>

**Examples:** An **example** is a particular instance of data, x. (We put x in boldface to indicate that it is a vector.) We break examples into two categories:<br>
&nbsp;&nbsp;&nbsp;1. labeled examples<br>
&nbsp;&nbsp;&nbsp;2. unlabeled examples<br>
&nbsp; A **labeled example** includes both feature(s) and the label. That is:  *labeled examples: {features, label}: (x, y)* <br>

Use labeled examples to train the model. In our spam detector example, the labeled examples would be individual emails that users have explicitly marked as "spam" or "not spam." <br>

For example, the following table shows 5 labeled examples from a data set containing information about housing prices in California:<br>
![Labled Example](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/Labled%20Example.PNG)

An **unlabeled example** contains features but not the label. That is: *unlabeled examples: {features, ?}: (x, ?)* <br>

Here are 3 unlabeled examples from the same housing dataset, which exclude *medianHouseValue*: <br>
![Unlabled Example](https://github.com/rajeshpp/ML-AI/blob/master/ML%20Images/Unlabled%20Example.PNG)

Once we've trained our model with labeled examples, we use that model to predict the label on unlabeled examples. In the spam detector, unlabeled examples are new emails that humans haven't yet labeled.

**Models:** A model defines the relationship between features and label. For example, a spam detection model might associate certain features strongly with "spam". Let's highlight two phases of a model's life: <br>
 * **Training** means *creating* or *learning* the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.<br>
 * **Inference** means applying the trained model to unlabeled examples. That is, you use the trained model to make useful predictions (y'). For example, during inference, you can predict medianHouseValue for new unlabeled examples. <br>
