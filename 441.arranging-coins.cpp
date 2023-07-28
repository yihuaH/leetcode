/*
 * @lc app=leetcode id=441 lang=cpp
 *
 * [441] Arranging Coins
 */

// @lc code=start
class Solution {
public:
    int arrangeCoins(int n) {
        long i = 1 ;
        int ans = i;
        while (i <= n){
            ans = ans + 1;
            i += ans;
        }
        return ans-1;
    }
};
// @lc code=end

