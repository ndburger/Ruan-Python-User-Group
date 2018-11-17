# IA06: Fuzzy String Matching
#### Due by Saturday, Oct. 8, 5 PM.

![Fuzzy String Matching](images/fuzzy_str.jpg)


Fuzzy string matching (aka approximate string matching) is fundamental to text processing and data mining. An application of this can be found within any spellchecker, whose algorithm must  identify the closest match for any text string not found in a dictionary. This idea applies not only to text matching, but also to any mapping of sequential data. In my research, for instance, it is often used to identify similar sequences of actions undertaken by a group of individuals while the enact their work. In fields such as molecular biology it used to support homology (similarity) searches on DNA sequences.

Much like Euclidean distance (we covered last week), fuzzy string matching also attempts to measure a "distance" between sets of data. In this IA we look at one approach to measuring distances in a non-Euclidean space -- that is, measuring the difference (or conversely, similarity) of words. Such approaches allow you to find the closest word, or phrase, to ones you are attempting to identify.

In this exercise, you will modify your work from IA05 to accept close matches a user gives against known university names. You will do this by adding to IA05 fuzzy string searching techniques that will search for a given university name based on how close the user given string is to the university names within the known list of universities that are contained within your IA05 database.

## Background

Levenshtein distance is named after the Russian scientist Vladimir Levenshtein, who devised the algorithm in 1965. It is an example of an "edit distance" (and some mistakenly use these synonymously), and similar to Euclidean distances, it is a measure of difference (or similarity) between data observations.

In the case of Levenshtein distance (LD), we are measuring the difference between two __strings__, which we will refer to as the source string (s) and the target string (t). The Levenshtein (or edit) distance is the number of deletions, insertions, or substitutions required to transform from string s into string t.

Let's look at two examples:

* s='test', t='test'
In this case LD(s,t) = 0, because no steps are necessary to transform s into t, as they are already identical.

* s='test', t='tent'
In this case LD(s,t) = 1, because it requires one substitution (change the third letter in 'test' to an "n") to transform s into t.

The greater the Levenshtein distance, the more different the strings are. The smaller the Levensthtein distance, the more similar the two strings are.

__NOTE1__: People often mistakenly use Levenshtein distance as synonymous with edit distance, but Levenshtein distance is a specific version of the more general concept of edit distance. For instance, the LCS (longest common sequence) distance is also an edit distance, but only allows insertions and deletions, while Levenschtein distances allow for substitutions as well.

# Task

Your task is to modify your I05.sqlite to use Levenshtein distance to account for a user mispelling a university name.

1. copy your ia05 code and data your IA06 directory.
2. rename ia05.sqlite to ia06.sqlite
3. Update your program to use Levenshtein distance to conduct a fuzzy string match between what the user entered, and the list of known universities found within the database. NOTE: The other functionality of the program will remain that same, that is, it will still print out the closest and further university based on Euclidean distance.

There are existing implementations of Levenschtein distances in Python available to use. In this IA you must search for, and use, any library available via pip (PyPI). Create an instructions.md file the provides both instructions on how to use your program, and which library you used to calculate the Levenshtein distance.

__NOTE2__: Instead of "hardcoding" a specific maximum Levenshtein distance, instead you must choose the (first) __closest__ match from the given string the user entered with that of the list of universities listed within the database.  
