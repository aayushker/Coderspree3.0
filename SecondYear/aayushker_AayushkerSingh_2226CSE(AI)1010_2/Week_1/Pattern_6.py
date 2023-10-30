#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N + 1):
            for j in range(N, i, -1):
                print(" ", end="")
            for k in range(1, 2 * i):
                print("*", end="")
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends