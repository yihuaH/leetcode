#include "leetcode.h"
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr&&list2==nullptr){
            return nullptr;
        }
        if(list1 == nullptr){
            return list2;
        }
        if(list2 == nullptr){
            return list1;
        }

        ListNode* ans;
        while (list1->next!=nullptr && list2->next!=nullptr)
        {
            if(list1->val <= list2->val){
                ans->val = list1->val;
                list1 = list1->next;
            }else{
                ans->val = list2->val;
                list1 = list2->next;
            }
        }
        return ans;
    }
};