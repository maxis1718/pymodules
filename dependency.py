# -*- coding: utf-8 -*-

def read(raw_deps, return_type=list):
	deps = []
	for dep in map(lambda x:x.strip(), raw_deps.strip().split('\n')):

		lpb = [i for (i,x) in enumerate(dep) if x == '(']
		rpb = [i for (i,x) in enumerate(dep) if x == ')']
		if not lpb or not rpb: continue

		dl = min(lpb)
		dr = max(rpb)

		rel = dep[:dl]
		body = dep[dl+1:dr]

		parts = body.split(', ')
		left, right = map(lambda x:( '-'.join(x.split('-')[:-1]), int(x.split('-')[-1].replace("'",'')) ), parts)

		if return_type == dict:
			deps.append( {'rel':rel, 'ltoken': left[0], 'lidx': left[1], 'rtoken': right[0], 'ridx': right[1]} )
		else:
			deps.append((rel , left, right))

	return deps

if __name__ == '__main__':
	raw_deps = '''nsubj((Acquired-2, AIDS-1)
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

	from pprint import pprint
	deps = read(raw_deps, return_type=dict)
	pprint(deps)

