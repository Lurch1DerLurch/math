# math 
###### a simple tool to evaluate python3-like math expressions from the command line

```
$ math 3x5+5
20
$ math 5xx3
125
$ math 5/2
2.5
```
Unfortunately, `'*'` is a special character. Replace any appearance of `'*'` with `'x'`.

## Installation
To make math available all over your system, you can create a symbolic link to `math.py` in your `/bin` directory. This can be done, for example, by executing
```
$ sudo ln -s $PWD/math.py /bin/math
```
Note that you'll have to be executing this command from the directory where `math.py` is stored.
