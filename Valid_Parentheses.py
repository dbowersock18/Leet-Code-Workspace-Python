# NOT SOLVED!!!!


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


USED HINTS
Hint 1
Use a stack of characters.
Hint 2
When you encounter an opening bracket, push it to the top of the stack.
Hint 3
When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.
"""


# class Solution:
def isValid(s: str) -> bool:

    # an odd number String, is gaurenteed to be false
    if (len(s) % 2) != 0:
        return False
    
    if ( (s.count("(") != s.count(")")) or (s.count("{") != s.count("}"))) or (s.count("[") != s.count("]") ):
        return False
    
    stack = []
    for x in s: 
        if x in ("{", "(", "["):
            stack.append(x)
            continue
        if x in ("}", "]", ")"):
            if not stack:
                return False
            test = stack[-1] + x
            if test in ("{}", "()", "[]"):
                stack.pop()
                continue
            else:
                return False
    return True

       

def test_isvalid():
    #assert isValid("()") is True
    assert isValid("()[]{}") is True
    assert isValid("()[{()}]{}") is True  
    assert isValid("(((((())))))") is True    

def test_isvalid2():
    assert isValid("(])") is not True
    assert isValid("((()") is not True  
    assert isValid("([)]") is not True
    assert isValid("({)}[]") is not True
    assert isValid("(){}}{") is not True

test_isvalid()
test_isvalid2()

# python -m pytest Valid_Parentheses.py works!!

