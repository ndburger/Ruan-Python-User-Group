
# EX1: PigLatin translator
# Due September 11, by 1 PM.
# Submit this assignment via git to your individual private repo (MIS407-cid00xx) under the directory IA02.

You will write a program that will take up to 100 command line given English words, and translate each of these words into Pig Latin.

The Pig Latin system used here works as follows:
* Words that start with a vowel (A, E, I, O, U) simply have "WAY" appended to the end of the word.
* Words that start with a consonant have all consonant letters up to the first vowel moved to the end of the word (as opposed to just the first consonant letter), and "AY" is appended.
  * ('Y' is counted as a vowel in this context)

### Example usage:
```
$ python pigl.py Our liberties we prize and our rights we will maintain
Ourway ibertieslay eway izepray andway ourway ightsray eway illway aintainmay
```

# EX2: Create a package called translator. Include in this package one module called piglatin. This module will contain two functions. The first will accept a string up to 100 words, and return the translation of those words into pigLatin. The second function simply returns the language rules. Rewright your pigl.py program from EX1 to recreate this functionality using your new package.

The two package functions should be callable using the following fully qualified forms:
piglatin.rules() # return string of text representing the rules of pigLatin
piglatin.english_to_piglatin() # input a single string of English words, and output a string of each of these words translated into pigLatin.

Example Usage:
```
from translator import piglatin
print(piglatin.rules())
print(piglatin.english_to_piglatin("Hello There"))
```
