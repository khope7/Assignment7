#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
#    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


#Creating code for ProductReviewAnalysisTask2


#Copying list from ProductReviewAnalysisTask1  
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
        ]

#Introducing tally variables
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

#Concantenating list into str so words can be found
review_full = ""

for iteration in reviews:
    review_full += iteration + " "

#Creating positive count variable
positive_count = 0

#Checking each iteration in positive words to see if it is a word found in the the reviews list str and printing the number of times a positive word is found
for iteration2 in positive_words:
#Using .lower() function to catch for capitalization in review str
    if iteration2 in review_full.lower():
        positive_count += 1

#Created additional if elif statements to catch for 0 and 1 for grammar
if positive_count > 1:
        print(f"There are {positive_count} positive words in the reviews list.")
elif positive_count == 1:
        print(f"There is {positive_count} positive word in the reviews list.")
else:
        print(f"Unfortunately there are {positive_count} positive words in the reviews list.")

#Creating negative count variable
negative_count = 0

#Checking each iteration in negative words to see if it is a word found in the the reviews list str and printing the number of times a negative word is found
for iteration3 in negative_words:
#Using .lower() function to catch for capitalization in review str
    if iteration3 in review_full.lower():
        negative_count += 1

#Created additional if elif statements to catch for 0 and 1 for grammar
if negative_count > 1:
        print(f"There are {negative_count} negative words in the reviews list.")
elif negative_count == 1:
        print(f"There is {negative_count} negative word in the reviews list.")
else:
        print(f"Fortunately there are {negative_count} negative words in the reviews list.")