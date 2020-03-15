from collections import namedtuple
n = int(input())
Sheet = namedtuple('Sheet',input().split()) 
marks = [int(Sheet(*input().split()).MARKS) for _ in range(n) ]
print(sum(marks)/n)
