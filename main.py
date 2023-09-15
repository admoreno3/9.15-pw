#Adelynn moreno , maritza

##################################### String Methods#################################
# String Methods Practice #1
# Print the following text in uppercase, using the specific string method:
text = "Especially in electronic communications, writing in all caps is equivalent to yelling."
result = text.upper()
print(result)
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple","is","better","than","complex."]
word_list2= " " .join(word_list)
print(word_list2)
# String Methods Practice #3
# Replace in the following sentence:
text = "If the implementation is hard to explain, it might be a bad idea."
x = text.replace("hard" , "easy").replace("bad" , "good")
print(x)
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.

#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
word="repetition "
print(word*15)
# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
haiku = "Whitecaps on the bay: \n A broken signboard banging \nIn the April wind.\n— Richard Wright,\n collected in Haiku: This Other World, 1998"
presence_beach='beach' in haiku.lower()
print(presence_beach)

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the
word = "electroencephalographist"
print(len(word))


