/*
33. Feb 3, 2021 - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/
#include<iostream>
#include<vector>

using namespace std;

class Solution
{
    public:
    vector<int> twoSum(vector<int>& nums, int target){
        vector<int> vect;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i] == nums[j]){
                    vect.push_back(i);
                    vect.push_back(j);
                }
            }
        }
        return vect;
    }
};

int main(){
    Solution soln;
    vector<int> testCase{2, 7, 11, 15};
    int target = 9;
    vector<int> ans = soln.twoSum(testCase, target);
    for(int i=0;i<ans.size();i++){
        cout << ans[i];
    }
    return 0;
}