/*
Jan 13, 2021 -Given an array nums.
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
*/

#include<iostream>
#include<vector>

using namespace std;

class Solution {
    public:
        vector<int> runningSum(vector<int>& nums)
        {
            vector<int> ret;
            int sum = 0;
            for(auto i=nums.begin();i!=nums.end();i++)
            {
                ret.push_back(sum+*i);
                sum += *i;
            }
            return ret;
        }
};

int main()
{
    Solution sol;
    vector<int> ans;
    vector<int> test = {3, 1, 2, 10, 1};
    ans = sol.runningSum(test);
    for(auto i=ans.begin();i!=ans.end();i++)
    {
        cout << *i << " ";
    }
    return 0;
}