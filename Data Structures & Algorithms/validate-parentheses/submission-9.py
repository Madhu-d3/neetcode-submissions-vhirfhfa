class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = []
        brackets_map = {']':'[', ')':'(', '}':'{'}
        for c in s:
            if c in brackets_map:
                if brackets_stack and  brackets_stack[-1] == brackets_map[c]:
                    brackets_stack.pop()
                else:
                    return False
            else:
                brackets_stack.append(c)
        return len(brackets_stack) == 0

