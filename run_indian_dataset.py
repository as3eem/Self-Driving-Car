class MagicList :
    def __init__(self):
        self.data = [0]
    
    def findMin(self):
        M = self.data
        smallest= min(M)
        return(smallest)
        
    def insert(self, E):
        M = self.data
        M.append(E)
        l=len(M)
        i= l-1
        while (i//2 >= 1 and M[i//2] > M[i]):
                    M[i],M[i//2] = M[i//2],M[i]
                    i=i//2  
        return(M)
    
    def deleteMin(self):
        M = self.data
        E1= min(M)
        E2= M[len(M)-1]
        i=0
        
        while(E2<M[2*i] and E2<M[2*i+1]):
            if M[2*i]< M[2*i+1]:
                s=M[2*i]
            else:
                s=M[2*i+1]
            b=E2
            E2=s
            s=b     
                
def K_sum(L, K):
    w = MagicList()
    aseem = w.data
    for i in L:
        w.insert(i)
    ans = 0 
    for i in range(1,K+1):
        ans+=aseem[i]
    return ans



if __name__ == "__main__" :
    '''Here are a few test cases'''
    
    '''insert and findMin'''
    M = MagicList()
    M.insert(4)
    M.insert(3)
    M.insert(5)
    x = M.findMin()
    if x == 3 :
        print("testcase 1 : Passed")
    else :
        print("testcase 1 : Failed")
        
    '''deleteMin and findMin'''
    M.deleteMin()
    x = M.findMin()
    if x == 4 :
        print("testcase 2 : Passed")
    else :
        print("testcase 2 : Failed")
        
    '''k-sum'''
    L = [2,5,8,3,6,1,0,9,4]
    K = 4
    x = K_sum(L,K)
    if x == 6 :
        print("testcase 3 : Passed")
    else :
        print("testcase 3 : Failed")
