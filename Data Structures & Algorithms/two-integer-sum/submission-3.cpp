#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // hashmap / dictionary creation
        std::unordered_map<int, int> visited;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            if (visited.find(diff) != visited.end()) { // found
                vector<int> answer = {visited[diff], i};
                return answer;
            } else {
                visited[nums[i]] = i;
            }
        }
    }
};
