class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if '0000' in deadends or target in deadends:
            return -1
        last_steps = set(self.neighbors(target)) - deadends
        if len(last_steps)==0:
            return -1
        
        direct_steps = self.dist(target)
        # direct transition is possible if there exists a last step closer than target
        for conf in last_steps:
            if self.dist(conf) < direct_steps:
                return direct_steps
            
        # direct transition is not possible
        return direct_steps + 2
        
    def neighbors(self, conf):
        res = []
        for i in range(4):
            temp = [c for c in conf]
            temp[i] = '0' if temp[i]=='9' else chr(ord(temp[i])+1)
            temp = ''.join(temp)
            res.append(temp)
                
            temp = [c for c in conf]
            temp[i] = '9' if temp[i]=='0' else chr(ord(temp[i])-1)
            temp = ''.join(temp)
            res.append(temp)
        return res
    
    def dist(self, conf):
        return sum([min(int(c), 10-int(c)) for c in conf])