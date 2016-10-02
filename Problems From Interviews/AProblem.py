#Unsolved

#input -> list/array
# discard_count -> number of time You can discard
def  largest_mono_subsequence(input, discard_count):
    lst = []
    if input == None:
        return lst
    if len(input) == 1:
        return input
    
    for i in range(len(input)):
        sub = [input[i]]
        count = discard_count
        index = 0
        for j in range(i+1,len(input)):
            if input[j] > sub[index]:
                sub.append(input[j])
                index += 1
            else:
                if count <= 0:
                    break
                count -= 1
        lst.append(sub)
        
    maxLen = 0
    maxLst = None
    for l in lst:
        if len(l) > maxLen:
            maxLen = len(l)
            maxLst = l
        elif maxLen == len(l):
            s1 = sum(l)
            s2 = sum(maxLst)
            if s1 > s2:
                maxLen = len(l)
                maxLst = l
                
    return maxLst