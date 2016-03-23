sss = "asdkjfbdkjfbjdkreeeteeerldfnknk"

@memoize(dump_stats = True, freq = 100)
def longest_pal(word):

   def is_pal(word):
      if len(word) <= 1:
         return True

      for i1 in range(0, len(word)):
         if word[i1] != word[len(word)-1-i1]:
            return False
      return True

   if( is_pal(word)):
      return (len(word), [word])

   (l1, w1) = longest_pal(word[1:])
   (l2, w2) = longest_pal(word[:-1])

   if l1 > l2:
      w = w1.copy()
      w.append(word)
      return (l1, w)
   else:
      w = w2.copy()
      w.append(word)
      return (l2, w)

aa = longest_pal(sss)

print(aa)
