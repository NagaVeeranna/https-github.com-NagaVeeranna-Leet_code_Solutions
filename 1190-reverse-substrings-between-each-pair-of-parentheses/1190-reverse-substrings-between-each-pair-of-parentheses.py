class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for ch in s:
            if ch == "(":
                stack.append("")
            elif ch == ")":
                current = stack.pop()[::-1]
                stack[-1] += current
            else:
                stack[-1] += ch

        return stack[0]