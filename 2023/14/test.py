
pat = [69,63,65,68,64,69,65]

c = 360000
i = -1

while c <= 1000000000:
	c += 10000
	i += 1
	if i == len(pat):
		i = 0
		
	val = pat[i]

print(c, val)