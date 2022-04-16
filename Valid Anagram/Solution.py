class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dic = {}
        t_dic = {}

        if len(s) != len(t):
            return False

        for x in range(len(s)):
            if s[x] not in s_dic:
                s_dic[s[x]] = 1
            else:
                s_dic[s[x]] += 1
            if t[x] not in t_dic:
                t_dic[t[x]] = 1
            else:
                t_dic[t[x]] += 1

        return s_dic == t_dic
