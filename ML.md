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
&nbsp;&nbsp;&nbsp;labeled examples<br>
&nbsp;&nbsp;&nbsp;unlabeled examples<br>
&nbsp; A **labeled example** includes both feature(s) and the label. That is:  *labeled examples: {features, label}: (x, y)* <br>

Use labeled examples to train the model. In our spam detector example, the labeled examples would be individual emails that users have explicitly marked as "spam" or "not spam." <br>

For example, the following table shows 5 labeled examples from a data set containing information about housing prices in California:<br>


An **unlabeled example** contains features but not the label. That is: *unlabeled examples: {features, ?}: (x, ?)* <br>

Here are 3 unlabeled examples from the same housing dataset, which exclude *medianHouseValue*: <br>

