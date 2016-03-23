d_2 = { 5 : 10, 10 : 5, 20 : 30, 100:10, 200: 4, 50: 1}

goal_2 = 1735

@memoize()
def next_2(goal, state):
    
    results = []

    for key in state:
        if key == goal:
            return (1, [(state, goal, key)])
        else:
            state2 = state.copy()
            state2[key] -= 1
            if(state2[key] == 0):
                del state2[key]
            
            (c, histo) = next_2(goal - key, state2)
            
            results.append( (c,key, histo) )

    min_ = 9999999
    val = -1
    histo = []
    
    for (c, key, histo_i) in results:
        if c < min_:
            min_ = c
            val = key
            histo = histo_i

    if min_ == 9999999:
        min_ -=1

    histo2 = histo.copy()
    histo2.append( (state, goal, val) )
    return (min_+1, histo2)
    


aa = next_2(goal_2, d_2)


print(aa[0])

for i in aa[1]:
   print(i)





