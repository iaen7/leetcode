#include <iostream>

using namespace std;

struct ListNode
{
    ListNode *next;
    int val;
    ListNode(int x):val(x), next(NULL) {};
};

//Two pointer:
//One to point the head of elements less than x, the other to point the head of elements equal or greater than x.
ListNode* partition(ListNode* head, int x) {
    if (head == NULL)
        return NULL;
    ListNode *lp = NULL, *gp = NULL, *p = head, *newhead = NULL, *ghead = NULL;
    while (p != NULL)
    {
        if (p -> val < x)
        {
            if (newhead == NULL)
                newhead = p;
            else
                lp -> next = p;
            lp = p;
        }
        else
        {
            if (ghead == NULL)
                ghead = p;
            else
                gp -> next = p;
            gp = p;
        }
        p = p-> next;
    }
    if(gp != NULL)
         gp -> next = NULL;
    if (newhead == NULL)
        newhead = ghead;
    else
        lp -> next = ghead;
    return newhead;
}

int main()
{
    ListNode p1(1),p2(4),p3(3),p4(2),p5(5),p6(2);
    p1.next = &p2;
    p2.next = &p3;
    p3.next = &p4;
    p4.next = &p5;
    p5.next = &p6;
    ListNode *p = partition(&p1,3);
    while(p!=NULL)
    {
        cout << p->val<<endl;
        p = p-> next;
    }
}
