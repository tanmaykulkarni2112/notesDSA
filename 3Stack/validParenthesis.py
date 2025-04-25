
class solution:
    def isValid(self, s: str) -> bool:
            stk = []
            for ch in s:
                if ch in "([{":
                    stk.append(ch)
                elif ch == ')':
                    if not stk or stk.pop() != '(':
                        return False
                elif ch == '}':
                    if not stk or stk.pop() != '{':
                        return False
                else:
                    if not stk or stk.pop() != '[':
                        return False
            if not stk:
                return True
            return False

sol = solution()
s1 = "{}(())"
print(sol.isValid(s1))
s2 = "({}})"
print(sol.isValid(s2))
s3 = "{[][][][][]}"
print(sol.isValid(s3))
s4 = "][]}"
print(sol.isValid(s4))