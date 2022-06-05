//
// Created by Administrator on 4/15/2022.
//


class Solution {
public:
    int strStr(string haystack, string needle) {
        int ans = -1;
        if(needle.size()==0){
            return 0;
        }
        for (int i = 0; i < haystack.length(); ++i) {
            if (haystack[i]==needle[0]){
                ans = i;
                for (int j = 0; j < needle.length(); ++j) {
                    if(haystack[i+j] == needle[j]){
                        continue;
                    }else{
                        ans = -1;
                        break;
                    }
                }
                if(ans != -1){
                    return ans;
                }
            }
        }
        return ans;
    }
};