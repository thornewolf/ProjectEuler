import inflect

p = inflect.engine()
s = ''
for i in range(1,1001):
	s += p.number_to_words(i)

s = s.replace('-','').replace(' ','')

print(len(s))