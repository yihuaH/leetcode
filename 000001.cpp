bool checkXMatrix(vector<vector<int>>& grid) {
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (i == j||(j == grid.size()-i-1))
                {
                    if (grid[i][j]==0)
                    {
                        return false;
                    }
                    
                }else{
                    if (grid[i][j]!=0)
                    {
                        return false;
                    }
                    
                }
                
            }
            
            
            
        }
        return true;
        
    }

int countHousePlacements(int n) {
    /*if (n == 0)
    {
        return 0;
    }else if (n == 1)
    {
        return 4;
    }else if (n == 2)
    {
        return 9;
    }else{
        
    }*/
    int ans = 1;
    for (int i = 1; i < n/2; i++)
    {
        ans += pow(fact(n)/(fact(i)*fact(n-i)),2);
    }
    return ans;
        
}

long fact(int a){
    if (a == 1)
    {
        return 1;
    }else{
        return a * fact(a-1);
    }
    
}
