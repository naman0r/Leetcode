# neetcode roadmap, stack

# https://leetcode.com/problems/valid-parentheses/description/

'''
time complexity: o(n)
space complexity: o(n)

best possible solution to this problem. 


this problem introduced me to to stacks and deques. Fun problem. 
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        from collections import deque # recomended use of stacks.



        # each opening parenthesis should have a closing one. 

        # most recent opening -> demands next closing. 

        opening = "({["
        closing = ")}]"


        # key = opening, value = closing. 
        parenthesis = { ")":"(", 
                        "}":"{",
                        "]":"["}

        mystack = deque()

        for candidate in s: 
            if candidate in opening: # same thing as .contains in java....
                mystack.append(candidate)
            
            # else means that it is a closing bracket....
            else: 
                if not mystack or parenthesis[candidate] != mystack[-1]: 
                    return False
                else: 
                    # pop the topmost element in the stack.....
                    mystack.pop()

            
        # mistake: was returning true. this returns true if mystack is empty. 
        return not mystack

        
