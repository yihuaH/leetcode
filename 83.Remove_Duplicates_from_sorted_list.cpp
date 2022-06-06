
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp = new ListNode;
        temp = head;
        if(head == nullptr)
            return nullptr;
        while (temp->next != nullptr)
        {
            if (temp->val==temp->next->val)
            {
                if (temp->next->next!= nullptr)
                {
                    temp -> next = temp->next->next;
                }else{
                    temp->next = nullptr;
                    break;
                }
                continue;
            }
            temp = temp->next;
        }
        return head;
        
    }
};