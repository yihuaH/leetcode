/*
 * @lc app=leetcode id=1931 lang=cpp
 *
 * [1931] Painting a Grid With Three Different Colors
 */

// @lc code=start
#include <vector>
#include <cmath>
using namespace std;

class Solution
{
public:
    const int mode = 1e9 + 7;
    bool judg(int x, int m)
    {
        int pre = -1;
        while (m-- > 0)
        {
            if (pre == x % 3) return false;
            else pre = x % 3;
            x /= 3;
        }
        return true;
    }
    bool judg(int x, int y, int m)
    {
        while (m-- > 0)
        {
            if (y % 3 == x % 3) return false;
            x /= 3;
            y /= 3;
        }
        return true;
    }
    int colorTheGrid(int m, int n) {
        int size = pow(3, m);
        vector<int> v(size, 0);
        for (int i = 0; i < size; ++i)
        {
            if (judg(i, m)) v[i] = 1;
        }
        for (int i = 1; i < n; ++i)
        {
            vector<int> v_tmp(size, 0);
            for (int j = 0; j < size; ++j)
            {
                if (v[j] != 0)
                {
                    for (int k = 0; k < size; ++k)
                    {
                        if (judg(k, m) && judg(j, k, m))
                        {
                            v_tmp[k] += v[j];
                            v_tmp[k] %= mode;
                        }
                    }
                }
            }
            v = v_tmp;
        }
        int ans = 0;
        for (int i : v)
        {
            ans += i;
            ans %= mode;
        }
        return ans;
    }
};
// @lc code=end
