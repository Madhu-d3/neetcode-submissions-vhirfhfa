class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        brackets_stack = []
        brackets_map = {'[':']', '(':')', '{':'}'}
        if s[0] not in opening or len(s) <= 1:
            return False
        for c in s:
            if c in opening:
                brackets_stack.append(c)
            if c in closing :
                if len(brackets_stack) > 0 and c != brackets_map[brackets_stack[-1]]:
                    return False
                if len(brackets_stack):
                    brackets_stack.pop()
                else:
                    return False
        return len(brackets_stack) == 0

