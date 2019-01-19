class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # store all operands
        vals = []
        for token in tokens:
            if token=='+':
                b = vals.pop()
                a = vals.pop()
                vals.append(a+b)
            elif token=='-':
                b = vals.pop()
                a = vals.pop()
                vals.append(a-b)
            elif token=='*':
                b = vals.pop()
                a = vals.pop()
                vals.append(a*b)
            elif token=='/':
                b = vals.pop()
                a = vals.pop()
                vals.append(int(a*1.0/b))
            else:
                vals.append(int(token))
        return vals[0]