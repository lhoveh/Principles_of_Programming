import re
from collections import Counter

s1 = (input('Enter submission text 1: '))
s2 = (input('Enter submission text 2: '))

# To avoid case sensitive issues, we turn both statements into lower case.

s1 = s1.lower()
s2 = s2.lower()

# We turn them into lists, so words become items.

list1 = s1.split()
list2 = s2.split()

# Creating a list to keep the similar words.

similar = []

# below the conditional to add every similar word in both statements to the "similar" list

for i in list1:
    if i in list2:
        similar.append(i)

# from the similar lists we create a similar_unique, with counter.
# it means each similar word will be counted only once.
# for example, the statements "me, myself and Irene", "him, himself and "Irene" will have:
# "and, and, Irene, Irene" as a list of similar words, but counter list will group these:
# counter = "and:2, Irene:2", so it will have two items (and the amount of occurrences).
# we are going to use the items from counter list (in this case "and" and "Irene" as the number of similar words.


similar_unique = Counter(similar)

common_btw = len(similar_unique)

print('Common words between the two submissions: ', common_btw)

# now we create a list with both statements together, so we can find the unique words in both statements.
# same process, we separate the list, per categories, using counter, so we find how many unique words in both sentences.

lists = list1 + list2

unique_both = Counter(lists)
unique_both_count = len(unique_both)

print('Total of unique words in both submissions: ', unique_both_count)

# similarity will be "(the amount of unique similar words between then) / (amount of unique words between then)"

similarity = common_btw / unique_both_count

# percentage = "{:.0%}".format(similarity)

print("The similarity between the two statements is {:2.2%}".format(similarity))
