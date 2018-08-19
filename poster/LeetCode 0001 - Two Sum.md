## Desicription

Given an array of **integers**, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the same element twice.

```c++
class Solution{
    public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        unordered_map<int, int>mp;
        for(int i = 0; i < numbers.size(); i++){
            int need = target - numbers[i];
            if(mp.find(need) != mp.end()){
                vector<int>res;
                res.push_back(i);
                res.push_back(mp[need]);
                return res;
            }
            mp[numbers[i]] = i;
        }
    }
};
```
