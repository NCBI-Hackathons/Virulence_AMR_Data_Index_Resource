import sys 
from collections import Counter

print(Counter(open(sys.argv[1]).read()))
