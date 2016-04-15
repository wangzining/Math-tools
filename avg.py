import re

num=re.compile('\$([0-9]{1,4})')    #num matching? min matching example?

fin=open('txt')
count=0
sum=0


for line in fin:
    l=line.split()
    for token in l:
        m=num.match(token)
        if m:

         print m.group(1)
         sum=sum+float(m.group(1))        #datatype?
         count=count+1
        #else:
         #   print token
'''
print 'count is',count

print 'sum is',sum

print  'average is',sum/count

'''

print float(37.25/57.25*(400+90+94)/6+20/(57.25)*76.5)+7

print [2*x for x in range(11)]

print 7//8.

a=5
a+1
print(a)