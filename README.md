# Amazon_review_sentiment_analysis
This is my work on the Amazon review fashions dataset
I have first created a dataframe known as dataset having only columns: reviewName, reviewText, overall
Next, I have replaced the NAN values with space
After ignoring the rating values of rating=3, I have split the ratings into 2 cases: (Refer the last part of this README file)
Now the entire dataset is split into train and test, 75:25 Ratio and random state=17
Then with the help of CountVectorizer all the words are tokenized, cleaned amd word2vector is done 
It is then applied on to the x_train of Reviews columns and then transformed on to the revieew column of the x_test
Using the Logistic Regression I have fit the training files to the model
It then provides the accuracy 
# --------------------------------------------
# The next step is to find the Gloabal Promoter 
# For this i converted the Name and Output columns to lists
# with the help of counter function i found out the name that is most common
# after knowing the most common user I checked if they have the maximum positive reviews and if so the result is being printed
# --------------------------------------------
# Two Cases:
# Case 1:
#       rating>3 - Output=+1
#       rating<3 - Output=-1
#       Accuracy = 88.89%
#       The Global Promoter is: Amazon Customer With highest number of positive reviews = 63514
# Case 2:
#       rating>3 - Output=+1
#       rating=3 - Output=0
#       rating<3 - Output=-1
#       Accuracy = 83.52%
#       The Global Promoter is: Amazon Customer With highest number of positive reviews = 63514
