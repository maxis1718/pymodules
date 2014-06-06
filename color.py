# -*- coding: utf-8 -*-

# python string color rendering v2.0

# [function]
## render a string with pre-specified color
#
# [usage]
## import color
## color.render('your msg', [color code / EnglishName / Eng abbr.], [light=True/False])

# by Maxis / Jun 6, 2014

import re

ColorMap = {
	'red': 		31,
	'green': 	32,
	'yellow': 	33,
	'blue': 	34,
	'purple': 	35,
	'cyan': 	36,
	'white':	37
}

def render(string, this_color, light=False):
	this_color = str(this_color).lower()
	if re.match(r'^[a-z]+$', this_color):
		if this_color.startswith('l') and len(this_color) == 2: # lg
			light = True
			this_color = this_color[1:]

		if this_color.startswith('light'):
			light = True
			this_color = this_color.replace('light','')

		if this_color in ColorMap: 
			code = str(ColorMap[this_color])
		else:
			abbr = [ColorMap[c] for c in ColorMap if c.startswith(this_color[0])]
			if abbr:
				code = str(abbr[0])
			else:
				code = False
	elif re.match(r'[0-9]+;?', this_color):
		if this_color.startswith('1;'):
			light = True
			this_color = this_color.replace('1;','')
		code = this_color
	else:
		code = False
	if not code: return string
	else: 
		code = '1;'+code if light else code
		colorized = "\033[" + code + "m" + string + "\033[0m"

	return colorized

def show():
	for i in range(30, 38):
		c = str(i)
		print('This is %s' % render('color ' + c, c))
		print('This is %s' % render('color ' + c, c, light=True))

	print '--'*8

	for i in range(256):
		c = '38;05;%d' % i
		print( render('color '+c, c) )	

def highlight(string): return render(string, 'yellow')

if __name__ == '__main__':
	
	# highlight text
	print highlight('Hello World')

	# render color on text using English color name
	print render('Hello World', 'green')

	# light color support
	print render('Hello World', 'green', light=True)

	# also can use abbreviation: r for red, g for green, ... etc.
	print render('Hello World', 'g')

	# auto detec light color (a color name starting with "light")
	print render('Hello World', 'lightgreen')

	# also abbr.
	print render('Hello World', 'lg')

	# more geeky, use ANSI code directly
	print render('Hello World', '1;30')



