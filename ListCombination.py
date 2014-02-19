# -*- coding: UTF-8 -*-

def ListCombination(list_of_list):
	if len(list_of_list) == 0: return False
	L, anchor = [], list_of_list.pop(0)
	for ele in anchor:
		L.append([ele])
	while len(list_of_list) > 0:
		anchor = list_of_list.pop(0)
		update = []
		for ele in anchor:
			for exist in L:
				update.append(exist + [ele])
		L = update
	return L

if __name__ == '__main__':
	# origin: person like bridge
	pattern = [['PERSON', 'BODY', 'COMMUNICATION'], ['like'], ['ARTIFACT', 'RELATION', 'BODY', 'ACT']]
	for single_pat in ListCombination(pattern):
		print single_pat
