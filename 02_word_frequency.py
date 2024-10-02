#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import string
import re
def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies
    text = text.lower() # Lowercase
    words = text.split() # Split based on whitespace
    final = []
    for i in range(len(words)):
        # Iterating through all words to strip punctuations at their beginning and end
        words[i] = words[i].strip(string.punctuation)
        # Split those words that has -- in middle
        lst = words[i].split('-')
        for w in range(len(lst)):
            lst[w] = lst[w].strip(string.punctuation)
        # Add all words to a new list 
        final.extend(lst)
    for i in range(len(final)):
        # Iterating through the list of words
        if final[i] not in frequencies:
            # Add a new word in the dictionary
            frequencies[final[i]] = 0   
        # add 1 to the count of an already existing word 
        frequencies[final[i]] += 1    
    return frequencies

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)