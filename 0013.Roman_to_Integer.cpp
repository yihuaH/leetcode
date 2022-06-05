

class Solution {
public:
    int romanToInt(string s) {
        int value = 0;
        for (size_t i = 0; i < s.size(); i++)
        {
            switch (s[i])
            {
            case 'M':
                value += 1000;
                break;
            case 'D':
                value += 500;
                break;
            case 'C':
                value += 100;
                if(s[i+1]=='D'||s[i+1]=='M'){
                    i++;
                    if(s[i]=='D'){
                        value += 300;
                    }else{
                        value += 800;
                    }
                }
                break;
            case 'L':
                value += 50;
                break;
            case 'X':
                value += 10;
                if(s[i+1]=='L'||s[i+1]=='C'){
                    i++;
                    if(s[i]=='L'){
                        value += 30;
                    }else{
                        value += 80;
                    }
                }
                break;
            case 'V':
                value += 5;
                break;
            case 'I':
                value += 1;
                if(s[i+1]=='V'||s[i+1]=='X'){
                    i++;
                    if(s[i]=='V'){
                        value += 3;
                    }else{
                        value += 8;
                    }
                }
                break;
            default:
                break;
            }
        }
        return value;
    }
};