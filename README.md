<h1>What I've learnt!</h1>
<h3>How to write Markdown</h3>

[Mark Down Usage(KR version)](https://gist.github.com/ihoneymon/652be052a0727ad59601)

<h3>How to convert list to string</h3>
```
  >> l = ["a", "b", "c"]
  >> s = ''.join(l)
  >> print(s)
  "abc"
```

<h3>How to convert list to string if element is not a string type</h3>
<h4>A. if you try to convert int list to string, you get TypeError, because join() method only takes string type as its parameter</h4>
```buildoutcfg
  >> l = [1, 2, 3]
  >> s = ''.join(l)
  Traceback (most recent call last):
    File "<pyshell#1>", line 1, in <module>
      ''.join(l)
  TypeError: sequence item 0: expected str instance, int found
```

<h4>B. So before using join() method, you should convert an element type from int to string, first</h4>
```buildoutcfg
# Using list comprehension
  >> l = [1, 2, 3]
  >> ''.join([str(_) for _ in l])
  '123' 
# Using map()
  >> l = [1, 2, 3]
  >> ''.join(map(str, l))
 '123'
```