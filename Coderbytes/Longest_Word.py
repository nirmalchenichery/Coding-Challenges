'''
----------------------------
Longest Word
----------------------------

Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

Examples

Input: "fun&!! time"
Output: time

Input: "I love dogs"
Output: love

'''

import string

def LongestWord(sen):

  word = sen.translate(str.maketrans('', '', string.punctuation)).split()
  # word = re.sub('[^A-Za-z]+', ' ', sen).split()
  max_length = 0
  longestWord = ""

  for i in word:
      if len(i) > max_length:
          longestWord = i
          max_length = len(i)

  return longestWord

# keep this function call here
# word = "I love dogs"
# word = "fun&!! time"
word = "123456789 98765432"

print(LongestWord(word))