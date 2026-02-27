class Solution(object):
    def romanToInt(self, s):
        r_map = {
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        sum = 0
                
        for i in range(len(s)):
            if i + 1 < len(s) and r_map[s[i]] < r_map[s[i+1]]:
                sum -= r_map[s[i]]
            else:
                sum += r_map[s[i]]
        return sum