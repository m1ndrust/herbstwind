#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.



def duplicate_count(text):

  duplicate = []
  dup_count = 0
  text_lower = text.lower()

  for char in text_lower:
      index = text_lower.index(char)
      if char in text_lower[index+1:] and char not in duplicate:
          duplicate.append(char)

  print len(duplicate)
  return len(duplicate)


duplicate_count("wownicedoggo")
