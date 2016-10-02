from __future__ import division
def s(X):
    # write your code in Python 2.7
    y = str(X)
    y = list(y)
    lst = []
    for i in xrange(1,len(y)):
        n1 = eval(y[i-1])
        n2 = eval(y[i])
        avg = int(round((n1+n2)/2))
        print avg
        a = str(avg)
        str1 = "".join(y[:i-1])
        str2 = "".join(y[i+1:])
        f = str1 + a + str2
        lst.append(eval(f))
    return max(lst)
