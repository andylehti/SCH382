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
print(result)

data = s2b('Hello world!')
result = SCH382(inverse(data, 2))
print(result)

data = s2b('Hello World!')
result = SCH382(inverse(data, 2))
print(result)

data = s2b('hello World!')
result = SCH382(inverse(data, 2))
print(result)

for i in range(2 ** 108, 2 ** 108 + 10):
    result = SCH382(i)
    print(result)
