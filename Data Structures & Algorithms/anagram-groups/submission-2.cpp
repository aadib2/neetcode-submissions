#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // dictionary-like data structure (hashmap)
        unordered_map<string, vector<string>> sorted_words;

        for (int j = 0; j < strs.size(); j++) {
            string curr = strs[j];
            sort(curr.begin(), curr.end()); // sorts in place

            if (sorted_words.find(curr) != sorted_words.end()) { // found
                sorted_words[curr].push_back(strs[j]); // add original string as found in list
            } else {
                sorted_words[curr] = vector<string>{strs[j]};
            }
        }
        // construct the output
        vector<vector<string>> anagram_sublists;
        for (const auto& [sorted, sublist] : sorted_words) {
            anagram_sublists.push_back(sublist);
        }
        
        return anagram_sublists;

    }
};
