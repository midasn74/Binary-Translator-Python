# Python binary translator

This is a really simple binary translator made with python.

  - Translate binary to text.
  - Translate text to binary.
  <p>&nbsp;</p>

## import
``
from BinaryTranslator import *
``
<p>&nbsp;</p>

## Example's

##### Text to binary:

```
input:
print(textToBinary("Hello, World"))

output:
> 1001000 1100101 1101100 1101100 1101111 101100 
  100000 1010111 1101111 1110010 1101100 1100100
```

##### Binary to text:

```
input:
print(binaryToText("1001000 1100101 1101100 1101100 1101111 101100 
                    100000 1010111 1101111 1110010 1101100 1100100"))

output:
> Hello, World 
```
<p>&nbsp;</p>

##### You can also change the seperator (seperator is one space a default).

```
input:
print(textToBinary("Hello, World", sep='-'))

output:
> 1001000-1100101-1101100-1101100-1101111-101100- 
  100000-1010111-1101111-1110010-1101100-1100100
```

```
input:
print(binaryToText("1001000-1100101-1101100-1101100-1101111-101100- 
                    100000-1010111-1101111-1110010-1101100-1100100", sep='-'))
output:
> Hello, World 
```
<p>&nbsp;</p>

##### Or write it to external files.
_code_
```
text = textToBinary("1001000 1100101 1101100 1101100 1101111 101100 
                     100000 1010111 1101111 1110010 1101100 1100100")

f = open("example.txt", "w")
f.write(text)
f.close()
```

_example.txt_
```text
1001000 1100101 1101100 1101100 1101111 101100 100000 1010111 1101111 1110010 1101100 1100100
```
<p>&nbsp;</p>

##### Or read from external files.
_example.txt_
```text
1001000 1100101 1101100 1101100 1101111 101100 100000 1010111 1101111 1110010 1101100 1100100
```
_code_
```
input:
f = open("example.txt", "r")
text = f.read()
f.close()

print(binaryToText(text))
```
```
output:
> Hello, World
```

