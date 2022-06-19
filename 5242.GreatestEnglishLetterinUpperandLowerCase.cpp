#include <string>
#include <vector>
using namespace std;


class Solution {
public:
    string greatestLetter(string s) {
        char ans = 0;
        string answer = "";
        string::size_type idx;
        for (int i = 0; i < s.length(); i++)
        {
            if(s[i]>64 && s[i]<=90){
                idx = s.find(s[i]+32);
                if (idx!=string::npos)
                {
                    if (s[i] > ans)
                    {
                        ans = s[i];
                    }
                    
                }
                
            }else if(s[i]>96 && s[i]<=122){
                idx = s.find(s[i]-32);
                if (idx!=string::npos)
                {
                    if (s[i]-32 > ans)
                    {
                        ans = s[i]-32;
                    }
                    
                }
            }
        }
        if (ans != 0)
        {
            answer+=ans;
        }
        
        return answer;
    }
};