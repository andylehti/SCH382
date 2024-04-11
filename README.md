# SCH382
## Step by Step Process
SCH382 uses 62 digits with 64 character keys. This approximately ≈ **5.2×10^14 × a googol ( 10^100)**

### Process Overview

1. **Input Processing and Initial Conversion**
   - Receive an input string.
   - Calculate a new string by adding a fixed number to the input string's integer representation, raising the result to a power, dividing by another fixed number, and converting to a string.

2. **String Segmentation and Augmentation**
   - Split this string into segments, alternating between 3 and 1 characters in length.
   - Convert each segment into an integer and add a fixed number to each.

3. **Iterative Combination**
   - Combine these numbers through a sequence of multiplications and divisions, alternating operations based on the position in the sequence.

4. **Reverse and Base Conversion**
   - Reverse the digits of the final number and convert it into binary, ensuring it is a 256-character string.

5. **Expansion and Fibonacci Modification**
   - Expand this binary string to 512 characters by repeatedly:
     - Modifying it based on the remainder of division by a fixed number plus one.
     - Adding a sequence-derived number raised to a power plus one to the modification.
     - Reversing the digits of the new number at each step.

6. **Decoding and Re-Encoding**
   - Split the 512-character binary string into two equal parts.
   - Decode each part from binary to decimal.
   - Combine these decimals through addition, double the result, and re-encode into a base using a subset of printable characters.

7. **Final Encoding and Truncation**
   - Encode the entire 512-character binary string into a high base using another subset of printable characters, excluding the first character from the result.
   - Decode this string back to decimal, then re-encode into base-62, truncating to the last 64 characters.

### Gist

- Take an input string and apply mathematical transformations to it, obtaining a new string representation.
- This transformation involves:
  - Adding a predetermined number to the input's numerical value.
  - Raising the result to a specified power.
  - Dividing by another predetermined number.
  - Converting the final number to a string.
- Segment this new string into pieces, alternating between lengths of three and one characters.
- Adjust each segment by converting to an integer and adding a fixed value.
- Sequentially combine these adjusted values, alternating between multiplication and division, based on their sequence position.
- Reverse the digits of the final combined value and convert it to a binary string, adjusting its length to 256 characters by padding with zeros.
- Expand this binary representation to 512 characters by:
  - Determining a modification factor based on the remainder of division by 17 plus one.
  - Calculating a sequence-derived value, raising it to the modification factor, and incrementing by one.
  - Adjusting the binary number by this calculated value and a division operation, then incrementing.
  - Reversing the digits of the result after each iteration.
- Once the binary string reaches the desired length, split it into two halves.
- Convert each half from binary to decimal.
- Sum these decimal values, double the sum, and encode into a new base using a specific character set.
- Encode the entire 512-character binary string into a higher base, excluding the first character of the result.
- Decode this high-base string back to decimal and finally re-encode it into base-62, keeping only the last 64 characters of this encoding.

### Code

```python
import math
import string
import numpy as np

def s2b(s): return ''.join(bin(ord(c))[2:].zfill(8) for c in s)

def base(d, b):
    c, n, r = string.printable[:90], 1, d
    while r >= b ** n: r -= b ** n; n += 1
    s = ""
    while r > 0: s = c[r % b] + s; r //= b
    return s.zfill(n)

def inverse(c, b):
    chars = string.printable[:90]
    v, l = 0, len(c)
    for i, ch in enumerate(reversed(c)):
        v += chars.index(ch) * (b ** i)
    return v + sum(b ** i for i in range(1, l))

def cF(m):
    if m == 0: return 1
    a, b = 1, 2
    for _ in range(m - 1): a, b = b, a + b
    return b

def sDeterminer(s):
    r, i, p, s = [], 0, [], str((s+7)**8 // 3)
    while i < len(s):
        r.append(s[i:i + (3 if len(r) % 2 == 0 else 1)])
        i += 3 if len(r) % 2 == 0 else 1
    for x in r: p.append(int(x) + 5)
    f = p[0]
    for i in range(1, len(p)): f = f * p[i] if i % 2 == 0 else f / p[i]
    f = str(int(f))[::-1]
    return base(int(f), 2)

def SCH382(s):
    s, x = int(sDeterminer(s)[:256], 2), 5
    while len(bin(s)[2:]) < 512:
        x = s % 17 + 1
        c = cF(x) ** x + 1
        s += math.floor(s / x + c) + 1
        s = int(str(s)[::-1])
        # print(s, c, x)
    s = bin(s)[2:]
    s = s[:512]
    a, b = inverse(s[:256], 2), inverse(s[256:], 2)
    c = base((a + b) * 2, 9)
    y = base(int(s), 89)[1:]
    return base(inverse(y, 90), 62)[-64:]

for i in range(0, 10000):
    result = SCH382(i)
    print(result)

data = s2b('hello world!')
result = SCH382(inverse(data, 2))
result
```
