/*
 * @lc app=leetcode id=399 lang=cpp
 *
 * [399] Evaluate Division
 */

// @lc code=start
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> ans(queries.size());
        for (int i = 0; i < queries.size(); i++)
        {
            vector<vector<int>> pos_a = check_pos(equations,values,queries[i][0]);
            vector<vector<int>> pos_b = check_pos(equations,values,queries[i][1]);
            if ((!pos_a.empty())&&(!pos_b.empty()))
            {
                if (queries[i][0].compare(queries[i][1])==0)
                {
                    ans[i] = 1.0;
                    continue;
                }
                
                //[a,b][b,a]
                for (int j = 0; j < pos_a.size(); j++)
                {
                    for (int k = 0; k < pos_b.size(); k++)
                    {
                        if (pos_a[j][0]==pos_b[k][0])
                        {
                            if (queries[i][0].compare(equations[j][0])==0)
                            {
                                ans[i] = values[j];
                            }else{
                                ans[i] = 1.0/values[j];
                            }
                            continue;
                        }
                        
                    }
                    
                }

                string a = queries[i][0];
                string b = queries[i][1];
                ans[i] = 1.0;
                vector<int> ans_chain = chain(equations,values,a,b);
                for (int j = 0; j < ans_chain.size(); j++)
                {
                    if (equations[ans_chain[j]][0].compare(a)==0)
                    {
                        a = equations[ans_chain[j]][1];
                        ans[i] *= values[ans_chain[j]];
                    }else{
                        a = equations[ans_chain[j]][0];
                        ans[i] *= (1.0 / values[ans_chain[j]]);
                    }
                    
                }
                
            }else{
                ans[i] = -1.0;
            }
            
        }
        return ans;
        
    }
    vector<vector<int>> check_pos(vector<vector<string>>& equations, vector<double>& values, string a){
        vector<vector<int>> pos_vector;
        for (int i = 0; i < equations.size(); i++)
        {
            for (int j = 0; j < equations[0].size(); j++)
            {
                if (equations[i][j].compare(a)==0)
                {
                    vector<int> temp;
                    temp.push_back(i);
                    temp.push_back(j);
                    pos_vector.push_back(temp);
                }
                
            }
            
        }
        return pos_vector;
        
    }
    vector<int> chain(vector<vector<string>>& equations, vector<double>& values, string a, string b){
        vector<int> answer;
        vector<vector<int>> pos_a = check_pos(equations,values,a);
        vector<vector<int>> pos_b = check_pos(equations,values,b);
        for (int j = 0; j < pos_a.size(); j++)
        {
            for (int k = 0; k < pos_b.size(); k++)
            {
                if (pos_a[j][0]==pos_b[k][0])
                {
                    answer.push_back(pos_a[j][0]);
                    return answer;
                }
                
            }
            
        }
        for (int j = 0; j < pos_a.size(); j++)
        {
            string temp;
            temp = equations[pos_a[j][0]][abs(pos_a[j][1]-1)];
            answer.push_back(pos_a[j][0]);
            vector<int> temp_ans = chain(equations,values,temp,b);
            answer.insert(answer.end(),temp_ans.begin(),temp_ans.end());
        }
        return answer;
    }
};
// @lc code=end

