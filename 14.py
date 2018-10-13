import sys
sys.setrecursionlimit(1000000)
def collatz(n):
	#print('starting {}'.format(n))
	cnt = 1
	while n != 1:
		if n%2 == 0:
			n = n//2
		else:
			n = n*3+1
		cnt += 1
	return cnt

print(collatz(13))

maxx = 0
i = 1
while i < 1000000:
	if i%10000==0:
		print(i)
	cnt = collatz(i)
	if cnt > maxx:
		print('New max @ {}: {}'.format(i,cnt))
		maxx = cnt
	i += 1
