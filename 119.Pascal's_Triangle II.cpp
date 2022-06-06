

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> answer;
        if(rowIndex == 0){
            answer.push_back(1);
            return answer;
        }else if(rowIndex == 1){
            answer.push_back(1);
            answer.push_back(1);
            return answer;
        }else{
            answer.push_back(1);
            vector<int> temp = getRow(rowIndex-1);
            for(int i = 0; i<rowIndex-1; i++){
                answer.push_back(temp[i]+temp[i+1]);
            }
            answer.push_back(1);
            return answer;
        }
        return answer;
    }
};