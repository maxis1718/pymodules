# -*- coding: utf-8 -*-
from pprint import pprint


def read(raw_deps, delimiter=None, auto_detect=False, return_type=list):
	deps = []
	if not delimiter or auto_detect:
		delimiter = '\n' if raw_deps.count('\n') > raw_deps.count('), ') else '), '

	for dep in map(lambda x:x.strip(), raw_deps.strip().split(delimiter)):

		if ')' not in dep.split('-')[-1]: # put ")" back
			dep = dep + ')'

		lpb = [i for (i,x) in enumerate(dep) if x == '(']
		rpb = [i for (i,x) in enumerate(dep) if x == ')']
		if not lpb or not rpb: continue

		dl = min(lpb)
		dr = max(rpb)

		rel = dep[:dl]
		body = dep[dl+1:dr]

		parts = body.split(', ')

		left, right = map(lambda x: ( '-'.join(x.split('-')[:-1]), int( x.split('-')[-1].replace("'",'') ) ), parts)

		if return_type == dict:
			deps.append( {'rel':rel, 'ltoken': left[0], 'lidx': left[1], 'rtoken': right[0], 'ridx': right[1]} )
		else:
			deps.append((rel , left, right))

	return deps

if __name__ == '__main__':
	raw_deps = '''nsubj((Acqui---red--2, AIDS-1)
	dep(called-14, (Acquired-2)
	nn(-6, Immune-3)
	nn(-6, Deficiency-4)
	nn(-6, Syndrome)-5)
	nsubj(condition-9, -6)
	cop(condition-9, is-7)
	det(condition-9, a-8)
	ccomp((Acquired-2, condition-9)
	partmod(condition-9, caused-10)
	det(virus-13, a-12)
	agent(caused-10, virus-13)
	nn(Virus)-19, HIV-15)
	nn(Virus)-19, (Human-16)
	nn(Virus)-19, Immuno-17)
	nn(Virus)-19, Deficiency-18)
	nsubj(called-14, Virus)-19)'''

	raw_deps = '''root(ROOT-0, <center>-1), dep(see-19, <img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00818.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-2), nsubj(fucked-4, my-3), ccomp(see-19, fucked-4), prt(fucked-4, up-5), num(<img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00822.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-9, <lj-cut\xc2\xa0text="car">-6), amod(<img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00822.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-9, <lj-cut>-7), amod(<img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00822.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-9, <img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00821.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-8), dobj(fucked-4, <img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00822.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-9), advmod(fence-14, here-11), cop(fence-14, \'s-12), det(fence-14, the-13), conj_and(fucked-4, fence-14), dobj(took-16, fence-14), ccomp(see-19, fence-14), nsubj(took-16, I-15), rcmod(fence-14, took-16), prt(took-16, out-17), acomp(<center>-1, see-19), det(ditch-22, the-20), amod(ditch-22, big-21), dobj(see-19, ditch-22), prep_in_front_of(see-19, it-26), dep(missed-29, that-27), nsubj(missed-29, I-28), dep(see-19, missed-29), prep(missed-29, by-30), pcomp(by-30, like-31), num(feet-33, five-32), prep_like(by-30, feet-33), num(</lj-cut>-39, <img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00824.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-35), amod(</lj-cut>-39, <img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00826.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-36), amod(</lj-cut>-39, <img\xc2\xa0src="http://www.pyxz.com/users/1061083943//dsc00827.jpg"\xc2\xa0alt=".",height"500"width"300"\xc2\xa0/>-37), amod(</lj-cut>-39, </center>-38), nsubj(<center>-1, </lj-cut>-39)'''

	from pprint import pprint
	deps = read(raw_deps, delimiter='), ', auto_detect=False, return_type=dict)
	pprint(deps)

