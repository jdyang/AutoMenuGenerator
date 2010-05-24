def lcs(long, short):
   if short in long:
      return short
   s1 = lcs(long, short[:-1])
   s2 = lcs(long, short[1:])
   if len(s1) > len(s2):
      return s1
   else:
      return s2

def rangeLen(s, t):
    if len(s) < len(t):
        return (t, s)
    else:
        return (s, t)

if __name__ == '__main__':
    max = 'abc'
    min = 'abcd'
    (max, min) = rangeLen(max, min)
    print max
    print lcs('abc', 'bcd')