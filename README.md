# math 
###### a simple tool to evaluate python3 math expressions from the command line

```
$ math 3x5+5
20
$ math 5xx3
125
$ math 5/2
2.5
```
Unfortunately, `'*'` is a special character. To make math work, you have to replace any appearance of `'*'` with `'x'`.

## Installation
To make math available all over your system, you can create a symbolic link to `math.py` in your `/bin` directory. This can be done with the following command.
`$ sudo ln -s $PWD/math.py /bin/math`