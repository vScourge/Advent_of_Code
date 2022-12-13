import regex as re
from ast import literal_eval

data = """
c0 c1 c2 c3 c4 c5
0   10 100.5 [1.5, 2]     [[10, 10.4], [c, 10, eee]]  [[a , bg], [5.5, ddd, edd]] 100.5
1   20 200.5 [2.5, 2]     [[20, 20.4], [d, 20, eee]]  [[a , bg], [7.5, udd, edd]] 200.5
"""

# regex definition
rx = re.compile(r'''
                (?(DEFINE)
                (?<item>[.\w]+)
                (?<list>\[(?:[^][\n]*|(?R))+\])
                )
                (?&list)|(?&item)
                ''', re.X)

# unquoted item
item_rx = re.compile(r"(?<!')\b([a-z][.\w]*)\b(?!')")

# afterwork party
def afterwork(match):
	match = item_rx.sub(r"'\1'", match)
	return literal_eval(match)

matrix = [
    [afterwork(item.group(0)) for item in rx.finditer(line)]
    for line in data.split("\n")
    if line
]

print(matrix)