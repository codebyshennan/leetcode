# Valid Parenthesis

[LC](https://leetcode.com/problems/valid-parentheses/description/)

```python
def isValid(self, s: str) -> bool:
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    # guard: immediate return if less than two char
    if len(s) < 2:
        return False

    for char in s:
        # push into stack if it's opening parenthesis
        if char not in mapping:
            stack.append(char)
        elif len(stack) != 0:
            # stop if closing bracket does not have opening bracket as top of stack
            if mapping[char] != stack[-1]:
                return False
            # if match, remove top of stack
            else:
                stack.pop()
        # catch other invalids
        else:
            return False

    if len(stack) != 0:
        return False

    return True

```

Better solution

```python
def isValid(self, s):
      """
      :type s: str
      :rtype: bool
      """
      d = {'(':')', '{':'}','[':']'}
      stack = []
      for i in s:
          if i in d:  # 1
              stack.append(i)
          elif len(stack) == 0 or d[stack.pop()] != i:  # 2
              return False
      return len(stack) == 0 # 3

# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket
```
