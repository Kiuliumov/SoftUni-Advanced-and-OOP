def genrange(start, end):

   while start <= end:
       i = start
       start += 1
       yield i

print(list(genrange(1,10)))