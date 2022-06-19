#include <string>
#include <vector>
using namespace std;


class Solution {
public:
   int minimumNumbers(int num, int k) {
        int ans = -1;
        if(num == 0){
            return 0;
        }
        if (num < k)
        {
            return -1;
        }
        
        for (int i = 1; i <= 10; i++)
        {
            if (num%10 == ((k*i)%10))
            {
                ans = i;
                break;
            }
            
        }
        if (ans == -1)
        {
            return ans;
        }
        if (num < k*ans)
        {
            ans = -1;
        }
        

        return ans;
        
        
    }
};
