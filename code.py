__author__ = 'wl'

class delect_duplicate:
    def method_set(self,mlist):
        print("method_set is called")
        print("before process mlist is", mlist)
        l2 = set(mlist)
        print("after processed by method_xunhuan, the mlist is",l2)
    def method_xunhuan(self,mlist):
        print("method_xunhuan is called")
        print("before process mlist is", mlist)
        if mlist:
            mlist.sort()
            last = mlist[-1]
            for i in range(len(mlist) - 2, -1, -1):
                if last == mlist[i]:
                    del mlist[i]
                else:
                    last = mlist[i]
        print("after processed by method_xunhuan, the mlist is",mlist)
    def method3(self,mlist):
        print("method3 is called")
        print("before process mlist is", mlist)
        temp = []
        [temp.append(i) for i in mlist if not i in temp]
        print("after processed by method3, the result is",temp)

if __name__ == '__main__':
    A = [1, 5, 4, 8, 9, 2, 4, 5, 1]
    B = [1, 5, 4, 8, 9, 2, 4, 5, 1]
    C = [1, 5, 4, 8, 9, 2, 4, 5, 1]
    s = delect_duplicate()
    s.method_set(A)
    s.method_xunhuan(B)
    s.method3(C)


