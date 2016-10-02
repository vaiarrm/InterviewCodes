def qs(lst,start,end):
              if start < end:
                            pivot = partition(lst,start,end)
                            qs(lst,start,pivot-1)
                            qs(lst,pivot+1,end)
              return lst

def swap(lst,i,j):
              temp = lst[i]
              lst[i] = j
              lst[j] = temp
              
def partition(lst,start,end):
              pivot = lst[end]
              i = start - 1
              for j in range(start,end):
                            if lst[j] <= pivot:
                                          i +=1 
                                          swap(lst,i,j)
              i+=1
              swap(lst,i,end)
              return i


def ms(lst):
              if lst == None:
                            return lst
              if len(lst) == 0 or len(lst) == 1:
                            return lst
              msH(lst,0,len(lst)-1)
              
def msH(lst,lo,hi):
              if lo < hi:
                            mid = (lo+hi)/2
                            msH(lst,lo,mid)
                            msH(lst,mid+1,hi)
                            merge(lst,lo,mid,hi)
                            
def merge(lst,lo,mid,hi):
              print lst , lo,mid,hi
              if len(lst) == 0:
                            return lst
              tempLst = [0] * len(lst)
              l1 = lst[lo:mid+1]
              l2 = lst[mid+1:hi+1]
              print l1, l2
              i = 0
              j = 0
              k = 0
              while i < len(l1) and j < len(l2):
                            if l1[i] <= l2[j]:
                                          tempLst[k] = l1[i]
                                          i += 1
                                          k += 1
                            else:
                                          tempLst[k] = l2[j]
                                          j += 1
                                          k += 1

              while i < len(l1):
                            tempLst[k] = l1[i]
                            i += 1
                            k += 1
              while j < len(l2):
                            tempLst[k] = l2[j]
                            j += 1
                            k += 1
              i = 0
              k = lo
              for k in range(lo,hi+1):
                            lst[k] = tempLst[i]
                            #k+=1
                            i+=1
                            
