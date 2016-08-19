def selectsort(lst):
 out=[] #the output list
 for i in range(len(lst)):
  m = min(lst)
  out = [m]+out #add at the end of the list
  lst.remove(m) #remove one occurrence of m
  #print(lst,"AND",out)
 return out
