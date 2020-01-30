# p.633
# 2020-01-30
# 짝이 맞지 않는 괄호 문제
# (), {}, [] 괄호 찾기 교차하면 안됨.


def wellMatched(formula):
  stack = []
  for c in formula:
    if c in "({[":
      stack.append(c)
    else:
      if len(stack) == 0:
        return False
      if "({[".find(stack.pop()) != ")}]".find(c):
        return False
  return len(stack) == 0


print("Must be true")
print(wellMatched("()()"))
print(wellMatched("({}[]())"))

print("\nMust be false")
print(wellMatched("]"))
print(wellMatched("({[}])"))