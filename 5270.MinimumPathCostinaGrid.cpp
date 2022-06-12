#include <vector>
#include <cmath>
using namespace std;
class Solution {
public:
    int minPathCost(vector<vector<int>>& grid, vector<vector<int>>& moveCost) {
        float a = pow(grid[0].size(),grid.size());
        int b = (int)a;
        int costarray[b];
        int m = grid.size();
        int n = grid[0].size();
        
            for (int i = 0; i < n; i++)
            {
                for (int j = i*(b/n); j < (i+1)*(b/n); j++)
                {
                    costarray[j] += grid[0][i];
                }
                
                
                
            }
            
        
        
    }
};