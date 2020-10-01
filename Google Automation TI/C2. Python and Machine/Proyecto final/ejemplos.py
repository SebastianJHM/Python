import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
print(re.search(r"ticky: INFO: ([\w ]*) ", line))
print(re.search(r"ticky: INFO: ([\w ]*) ", line)[1])

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
print(re.search(r"ticky: ERROR: ([\w ]*) ", line))

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
print(sorted(fruit.items()))

import operator
print(sorted(fruit.items(), key=operator.itemgetter(0)))
print(sorted(fruit.items(), key=operator.itemgetter(1)))
print(sorted(fruit.items(), key = operator.itemgetter(1), reverse=True))

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
print(re.search(r"\((\w+)\)", line))
