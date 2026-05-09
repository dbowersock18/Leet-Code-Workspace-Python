""" 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty."""

# populate string file
strs = ["terminal","terminus","a"]

commonPrefix = []
loopBreak = False
for i in range(len(min(strs, key=len))):
    testArray = []
    for x in strs:
        placeHolder= x[i]
        #list of characters to check that each i is the same
        testArray.append(x[i])
        # loop to validate unique, or only 1 value, in testArray. If false breaks
        if (len(set(testArray)) != 1):
            loopBreak = True
            break
    if loopBreak == True:
            break
    commonPrefix.append(placeHolder)

output = "".join(commonPrefix)
# print(output)
