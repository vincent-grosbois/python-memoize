d = "kitten"
goal = "sitting"


@memoize()
def next(goal, d):

    if min(len(goal), len(d)) == 0:
        return (max(len(goal), len(d)), [goal+d])
    
    (len1, list1) = next(goal[0:-1], d)
    (len2, list2) = next(goal, d[0:-1])
    (len3, list3) = next(goal[0:-1], d[0:-1])

    len1 +=1
    len2 +=1
    if goal[-1] != d[-1]:
        len3 +=1

    
    if len1 < min(len2, len3):
        list_ = list1
        list_.append(goal+"/."+ d)
        val_ = len1
    elif len2 < min(len1, len3):
        list_ = list2
        list_.append(goal+"./"+ d)
        val_ = len2
    else:
        list_ = list3
        if goal[-1] != d[-1]:
            list_.append(goal+"./."+ d)
        else:
            list_.append(goal+"/"+ d)
        val_ = len3


    return (val_, list_)


aa = next(goal, d)

print(i)
print(max_stack)
print(aa)
