def s(S):
    # write your code in Python 2.7
    s = S.split("/n")
    lst = []
    path = []
    for word in s:
        #word = word.strip()
        w = word.split(".")
        #print w
        if len(w) == 2:
            if  w[-1] not in ["jpeg","png","gif"]:
                continue
            else:
                s = "/"
                #print lst
                for item in lst:
                    s += item
                s += "/"
                #print s
                path.append(len(s))
                continue
        #print "coming"
        count = 0
        #print word
        for char in word:
            #print char
            if char == " ":
                count += 1
            else:
                break
              
        #print count
        #print word
        print "lst = ",lst
        print "count =",count
        print word
        if len(lst) == count:
            lst.append(word.strip())
        else:
            lst[count] = word.strip()
            lst = lst[:count+1]
        print "lst2 = ",lst
        #print lst
    print
    print 
    print path
    return max(path)
