
## IA02 Sample Solution

The following is one way we could write this program:

```Python
import sys

if len(sys.argv) > 101:
    print("Sorry, the limit is 100 words")
else:
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', "E", "I", "O", "U", "Y")
    for i in range(1, len(sys.argv)):
        if sys.argv[i][0] in vowels:
            print(sys.argv[i][:len(sys.argv[i])] + "way ", end="")
        else:
            wrd = ""
            for j in range(0, len(sys.argv[i])):
                if sys.argv[i][j] not in vowels:
                    wrd = wrd + sys.argv[i][j]
                else:
                    out = sys.argv[i][j:] + wrd.lower() + "ay "
                    if sys.argv[i][0].isupper():
                        print(out.title(), end="")
                    else:
                        print(out, end="")
                    break
```

However the code is written though, the output it produces must match the
following examples (notice the handling of capitalization):

```
$ python pigl_ex1.py Iowa State University is located in Ames Iowa
Iowaway Atestay Universityway isway ocatedlay inway Amesway Iowaway
$ python pigl_ex1.py The Gerdin building houses the Business School
Ethay Erdingay uildingbay ouseshay ethay Usinessbay Oolschay
```
