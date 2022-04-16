#include "leetcode.h"
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> mystack;
        if(s.size()%2!=0){
            return false;
        }
        for (size_t i = 0; i < s.size(); i++)
        {
            switch (s[i])
            {
            case '(':
                mystack.push(s[i]);
                break;
            case '[':
                mystack.push(s[i]);
                break;
            case '{':
                mystack.push(s[i]);
                break;
            case ')':
                if(mystack.empty()){
                    return false;
                }
                if(mystack.top()=='('){
                    mystack.pop();
                }else{
                    return false;
                }
                break;
            case ']':
                if(mystack.empty()){
                    return false;
                }
                if(mystack.top()=='['){
                    mystack.pop();
                }else{
                    return false;
                }
                break;  
            case '}':
                if(mystack.empty()){
                    return false;
                }
                if(mystack.top()=='{'){
                    mystack.pop();
                }else{
                    return false;
                }
                break; 
            default:
                break;
            }
        }
        return mystack.empty()? true:false;
    }
};