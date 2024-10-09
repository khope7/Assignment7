#Task 3: Review Summary

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

#Copying list from ProductReviewAnalysisTask1  
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
        ]

#Creating summary that appends "..."

#Concantenating list into str to slice intro for first 30 characters
review_full = ""

for iteration in reviews:
    review_full += iteration + " "

#Slicing first 30 characters
review_summary = review_full[0:32]

#Creating new list to appened convereted str back into list to appened "..."
working_summary = []

#Appending converted str into new list
working_summary.append(review_summary)

#Appending "..." into new list
working_summary.append("...")

#Joining both list variables together and printing to form summary
final_summary = "".join(working_summary)

print(final_summary)