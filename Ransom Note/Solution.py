from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dic = Counter(ransomNote)
        mag_dic = Counter(magazine)

        def helpder(note_dic, mag_dic):
            for key in note_dic:
                if key not in mag_dic:
                    return False
                elif note_dic[key] > mag_dic[key]:
                    return False
            return True

        return helpder(note_dic, mag_dic)