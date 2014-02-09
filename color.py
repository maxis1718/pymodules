# -*- coding: utf-8 -*-

# python string color rendering v1.0

# [function]
## render a string with pre-specified color
#
# [usage]
## import color
## color.render('your msg', '<some color name>')

# by Maxis / Jan 28, 2013

_R = '\033[0;32;31m'
_G = '\033[0;32;32m'
_B = '\033[0;32;34m'
_Y = '\033[1;33m'
_N = '\033[m'
_LP = '\033[1;35m'
_LC = '\033[1;36m'
_W = '\033[1;37m'

_ColorMap = {
        'red':_R,
        'green':_G,
        'blue':_B,
        'yellow':_Y,
        'none':_N,
        'lightpurple':_LP,
        'lightcyron':_LC,
        'white':_W
}

_Alias = {
        'r':'red',
        'g':'green',
        'b':'blue',
        'y':'yellow',
        'n':'none',
        'lp':'lightpurple',
        'lc':'lightcyron',
        'w':'white'
}

def render(text, c):
        c = c.lower()
        if c in _Alias: c = _Alias[c]
        c = _ColorMap['none'] if c not in _ColorMap else _ColorMap[c]
        return c+text+_ColorMap['none']


if __name__ == '__main__':

        print render('Hello','Green'), render('World','lp'), render('!!','rEd')