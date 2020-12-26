# Amazon Review Sentiment Analysis
This is my work on the Amazon review fashions dataset\
I have first created a dataframe known as dataset having only columns: reviewName, reviewText, overall\
Next, I have replaced the NAN values with space\
After ignoring the rating values of rating=3, I have split the ratings into 2 cases: (Refer the last part of this README file)\
Now the entire dataset is split into train and test, 75:25 Ratio and random state=17\
Then with the help of CountVectorizer all the words are tokenized, cleaned amd word2vector is done\
It is then applied on to the x_train of Reviews columns and then transformed on to the revieew column of the x_test\
Using the Logistic Regression I have fit the training files to the model\
It then provides the accuracy\
# To Find The Gloabal Promoter 
For this I converted the Name and Output columns to lists\
with the help of counter function i found out the name that is most common\
after knowing the most common user I checked if they have the maximum positive reviews and if so the result is being printed\
# Output:
# Case 1: If Ratings are split only into Positive and Negative Sentiments
       rating>3 - Output=+1
       rating<3 - Output=-1
       Accuracy = 88.89%
       The Global Promoter is: Amazon Customer With highest number of positive reviews = 63514
       Code Execution Time is: 494.9836037158966 seconds (8 Minutes 25 Seconds)
# Case 2: If Ratings are split into Positive,Negative and Neutral Sentiments
       rating>3 - Output=+1
       rating=3 - Output= 0
       rating<3 - Output=-1
       Accuracy = 83.52%
       The Global Promoter is: Amazon Customer With highest number of positive reviews = 63514
       Code Execution Time is: 985.1667013168335 seconds (16 Minutes 41 Seconds)
The Global Promoter will be same with the same number of positive reviews, as in both the cases only neutal and negative sentiments are varied but the positive sentiments remain the same       
