i = 0
stack = 0
max_stack = 0
memoize_dic = {}

def memoize(dump_stats = True, freq = 1000000):
   
   def memoize_2(f):
      def memoize_wrapper(*args):
           global i
           global stack
           global max_stack
           global memoize_dic
           i += 1
           stack +=1

           args_frozen = []
           for arg in args:
               if type(arg) is dict:
                  args_frozen.append(frozenset(arg.items()))
               else:
                  args_frozen.append(arg)

           args_frozen = tuple(args_frozen)

           if stack > max_stack:
               max_stack= stack

           if dump_stats and (i % freq == 0):
               print(i)
               print(max_stack)
               print(len(memoize_dic))
               print("--")

           if args_frozen in memoize_dic:
               stack -= 1
               return memoize_dic[args_frozen]
               
           result = f(*args)
           memoize_dic[args_frozen] = result
           stack -= 1
           return result
       
      return memoize_wrapper
   return memoize_2
