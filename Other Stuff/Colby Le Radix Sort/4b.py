# -*- coding: utf-8 -*-

'''
Project 4b

Author: Colby Le
Writing Date: 10/9/18
Finished: ~10/9/18
'''

# import
import itertools
import nltk



strList = []

# get text and tokenize into words
page = open("booktext.txt", "rt")
for i in page:
  strList.extend(nltk.word_tokenize(i))

# create buckets
buckets = list(itertools.repeat([], 26))

# find max/analyze length/pad with zeros
max = ""
for i in range(0, len(strList)):
  if(len(strList[i]) >len(max)):
    max = strList[i]
    
# print("Length of max element: " + str(len(max)))
maxLength = len(max)

for i in range(0, len(strList)):
  strList[i] = strList[i].zfill(maxLength)
  
print(strList)

i = 0
while i < maxLength:
  # fill buckets
  for j in range(0, len(strList)):

    # get ASCII value of nth char in string, then subtract 97 and mod by 26 to find bucket
    if(i == 0):
      buckets[(ord(strList[j][-1 * (i + 1):])-97) % 26].append(strList[j])
    else:
      buckets[ord(strList[j][-1 * (i + 1):-1 * i])].append(strList[j])

  strList.clear()

  # empty buckets

  for j in range(0, 26):
    for k in range(0,len(buckets[j])):
      strList.append(buckets[j].pop(0))
  
  i += 1
print(strList)

print(ord("a"))

