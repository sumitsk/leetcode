class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        char_stack = []
        i = 0
        while i<len(s):
            # if ch is an integer, keep reading all integers
            if 0<=ord(s[i])-ord('0')<=9:
                int_ch = []
                while i<len(s) and 0<=ord(s[i])-ord('0')<=9:
                    int_ch.append(s[i])
                    i += 1
                count_stack.append(int(''.join(int_ch)))
            
            elif s[i] ==']':
                char_ch = []
                # pop char_stack till you exhaust or get an [
                while len(char_stack)>0:
                    ch = char_stack.pop()
                    if ch=='[':
                        break
                    else:
                        char_ch.append(ch)
                char_ch = list(reversed(char_ch))
                times = count_stack.pop()
                if len(char_ch)>0:
                    new_str = char_ch*times
                    char_stack += list(new_str)
                i += 1 
            else:
                char_stack.append(s[i])
                i += 1 

        return ''.join(char_stack)  

sol = Solution()
string = "3[a]2[bc]"
ans = sol.decodeString(string)
print(ans)
