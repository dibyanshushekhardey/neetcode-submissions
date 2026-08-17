class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_a = []
        my_dict = {}
        for i in strs:
            my_dict["".join(sorted(i))] = []
        for i in strs:
            if "".join(sorted(i)) in my_dict:
                my_dict["".join(sorted(i))].append(i) 
        values_list = list(my_dict.values())
        return values_list