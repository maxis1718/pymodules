pymodules
=========

* color - render strings

* ListCombination - python Combination in list type

* mathutil - often used math function

color
---

```python
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
```

ListCombination
---

similar to `itertools.combination`, but a list version

```python
# input 
pattern = [
	['I','They'],
	['love', 'loved', 'loves'],
	['You']
]

# output
  ['I', 'love', 'You']
  ['They', 'love', 'You']
  ['I', 'loved', 'You']
  ['They', 'loved', 'You']
  ['I', 'loves', 'You']
  ['They', 'loves', 'You']
```

mathutil
---

commonly used math functions: **entropy**, **variance**, **standard_deviation**, **geomatric_mean**...

e.g., 

```python
intput sequence: [1, 1, 1, 4, 10, 4, 1, 2, 1]
==================================================
normalized data is [0.04, 0.04, 0.04, 0.16, 0.4, 0.16, 0.04, 0.08, 0.04]
avg is 2.595
entropy is 2.595
variance is 7.95
standard_deviation is 2.819
geomatric_mean is 1.898
arithmetic_mean is 2.777
```



