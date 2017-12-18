# Given n and e, decrypt the cipher

import sys,math
from binascii import unhexlify

cipher = [121560831698874219453267613174219141247779625979263684086055365282206190849386529369540754333346196170380400323865047328204751135058776179967797282368990382515924294891518016686180279409054094397243792496242298466435824664626111902]
#125675338953457551017,
#524099092120785248852,
#772538252438953530955,
#547462544172248492882,
#28215860448757441963,
#543018082275730030658,
#585936545563088067075,
#131807465077304821584]
n = 1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413
e = 65537
p = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489 #http://www.numberempire.com/numberfactorizer.php
q = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917 #http://www.numberempire.com/numberfactorizer.php

def bezout(a, b):
	if a == 0 and b == 0: 
		return (0, 0, 0)
	if b == 0: 
		return (a/abs(a), 0, abs(a))
	(u, v, p) = bezout(b, a%b)
	return (v, (u - v*(a/b)), p)
	
def inv_modulo(x, m):
	(u, _, p) = bezout(x, m)
	if p == 1: 
		return u%abs(m)
	else:
		raise Exception("%s e %s nao sao primos entre si" % (x, m))

if __name__ == "__main__":
	phi = (p-1)*(q-1)
	d = inv_modulo(e,phi)
	print d
	m = ''.join([unhexlify(hex(pow(i,d,n))[2:-1]) for i in cipher])
	print m
	
	
