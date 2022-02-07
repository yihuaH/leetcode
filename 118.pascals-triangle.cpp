#include "leetcode.h"
using namespace std;



class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> sub_ans;
        if(numRows == 1){
            sub_ans.push_back(1);
            ans.push_back(sub_ans);
            return ans;
        }else if(numRows == 2){
            sub_ans.push_back(1);
            ans.push_back(sub_ans);
            sub_ans.push_back(1);
            ans.push_back(sub_ans);
            return ans;
        }else{
            vector<vector<int>> temp = generate(numRows-1);
            sub_ans.push_back(1);
            for(int i = 0; i<numRows-2; i++){
                sub_ans.push_back(temp[numRows-2][i]+temp[numRows-2][i+1]);
            }
            sub_ans.push_back(1);
            temp.push_back(sub_ans);
            return temp;
        }
        return ans;

    }
};