#Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average".
# We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
#   reviews = [
#        "This product is really good. I'm impressed with its quality.",
#        "The performance of this product is excellent. Highly recommended!",
#        "I had a bad experience with this product. It didn't meet my expectations.",
#        "Poor quality product. Wouldn't recommend it to anyone.",
#        "The product was average. Nothing extraordinary about it."
#    ]
#So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

#Writing code for Task1


#Introducing string for indexing
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
        ]

#Creating for loop with if elif statements to catch for keywords, then replaces keywords with capitalization and prints full review line
for word in reviews:
    if "good" in word:
        good_emphasis = word.replace("good", "GOOD")
        print(good_emphasis)
    elif "excellent" in word:
        excellent_emphasis = word.replace("excellent", "EXCELLENT")
        print(excellent_emphasis)
    elif "bad" in word:
        bad_emphasis = word.replace("bad", "BAD")
        print(bad_emphasis)
    elif "poor" in word:
        poor_emphasis = word.replace("poor", "POOR")
        print(poor_emphasis)
    elif "average" in word:
        average_emphasis = word.replace("average", "AVERAGE")
        print(average_emphasis)