class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        index = 0
        while index < len(nums):
            if nums[index] not in dic:
                if index == len(nums) - 1:
                    return False
                else:
                    dic[nums[index]] = 1

            else:
                return True

            index += 1

def test_letter(puzz_list, letter_list):

    letter_count = 0
    final_list = {}
    for puzz in puzz_list:
        for c in puzz:
            if c in letter_list:
                if c not in final_list:
                    final_list[c] = 1
                else:
                    final_list[c] += 1

    return final_list

def max_vowel(dict):
    return max(dict['A'], dict['I'], dict['O'], dict['U'])
"""
Method append_dict:
Input -> Entire letter dictionary
Output -> Entire vowel dictionary, entire constantentn dictionary
"""
def append_dict(letter_list):
    vowel_dict = {}
    c_list= {}
    for key, value in letter_list:
        if key == 'A' or key == 'I' or key == 'O' or key == 'U':
            vowel_dict[key] = value
        else:
            c_list[key] = value

    return vowel_dict, c_list

def get_max(letter_list):
    return max(letter_list, key=letter_list.get())