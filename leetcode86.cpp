#include <iostream>
#include <string>
#include <map>

using namespace std;

bool isScramble(string s1, string s2) {
    if(s1 == s2)
        return true;
    map<char, int> cnt;
    for(int i =0; i != s1.size(); ++i)
    {
        ++cnt[s1[i]];
        --cnt[s2[i]];
    }
    for(auto s:cnt)
        if(s.second != 0)
            return false;
    int l = s1.size();
    for(int i =1; i != s1.size(); ++i)
    {
        if(isScramble(s1.substr(0,i),s2.substr(0,i)) && isScramble(s1.substr(i),s2.substr(i)))
            return true;
        if(isScramble(s1.substr(0,i),s2.substr(l - i)) && isScramble(s1.substr(i),s2.substr(0,l-i)))
            return true;
    }
    return false;
}

int main()
{
    string s1 = "great";
    string s2 = "rgtae";
    cout << isScramble(s1,s2) << endl;
}
