from operator import itemgetter
from unittest.util import sorted_list_difference


def char_count(str):

  ocurrences = {}
  result = []
  # count repetitions with dictionary
  for i in str:
    if i.isalnum():
      ocurrences[i] = ocurrences.get(i,0)+1
  # sort the dictionary by keys so we maintain this primary order in the list
  sortedx = sorted(ocurrences)
  # now we build the list with the first alphabetical order
  
  for x in sortedx:
    result.append([x,ocurrences.get(x)])
  # and after we have this order we sort by value in reverse order to get higher first, and since python maintains order in dictionaries we make sure key alphabetical is the secondary sorting 
  res = sorted(result,key=itemgetter(1),reverse=True)
   
  return res

  
  # def sorting(a,b):
  #   if a[1] > b[1]: return 1
  #   if b[1] > a[1]: return -1
  #   if a[1] == b[1]: 
  #     if a < b:
  #       return 1
  #     if b > a:
  #       return -1
  #     if a == b:
  #       return 0