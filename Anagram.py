# Input the words
word1=input("Enter the first sentence or word :")
word2=input("Enter the sentence or word that is needed to be checked for anagram :")

#Ignore Capitalization
word_1= word1.lower()
word_2= word2.lower()

#Ignore Spaces
word_1= word_1.replace(" ", "")
word_2= word_2.replace(" ", "")

#Ignore Punctuation
punctuations = '''!()-[]/?@#$\,'"<>.`%^&*_~{};:'''
word1 = ""
for letter in word_1:
   if letter not in punctuations:
       word1 = word1 + letter

word2 = ""
for letter in word_2:
   if letter not in punctuations:
       word2 = word2 + letter

#Processing the input for Anagarm verification:
print(word1, word2)
#length check
length1=len(word1)
length2=len(word2)

if length1 == length2:
    for char in word1:
        if char in word2:
            word2= word2.replace(char, "")

    final_check=len(word2)
    
    if final_check == 0:
        print("The words are Anagrams")
    else:
        print("They both are not Anagrams")


else:
    print("They both are not Anagrams")

