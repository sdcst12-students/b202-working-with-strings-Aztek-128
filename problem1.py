"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split 
function.
Have the user enter a sentence or paragraph and gives a word count.
"""

paragraph = input("enter your paragraph: ")

count = paragraph.split(" ")
num = len(count)
print(f"your word count is {num}")