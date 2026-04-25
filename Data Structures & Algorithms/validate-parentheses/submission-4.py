class Solution:
    def isValid(self, s: str) -> bool:
        
        lastBrackets = []
        for char in s:

            if char in "({[":
                lastBrackets.append(char)

            if char == ')':
                if not lastBrackets or lastBrackets.pop() != '(':
                    return False

            if char == '}':
                if not lastBrackets or lastBrackets.pop() != '{':
                    return False
                    
            if char == ']':
                if not lastBrackets or lastBrackets.pop() != '[':
                    return False

        if len(lastBrackets) > 0:
            return False
        else:
            return True

