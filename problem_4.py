"""
Problem Statement
Given Problem is to design a special stack data structure such that it supports following operations in constant O(1) time complexity.

Operation 1: top(): which will get the top element of the stack.
Operation 2: getMin(): returns the minimum elements of the stack (Currently present, deleted ones are not taken into account).
Operation 3: push(element): pushes an element "element" in the stack.
Operation 4: pop(): removes the element present at the top from the stack.
Input
First line of the input contains an integer T, number of test cases. T test cases are provided afterwards.
Each test case starts with a integer Q, number of operations. Next Q lines describes the operations. Operations can be of 4 types:

1: top()
2: getMin()
3 ele: push(ele)
4: pop()
Output
For each of the top() and getMin() operations print expected output.

Constraints 
1 ≤ T ≤ 100
1 ≤ Q ≤ 10000 
1 ≤ ele ≤ 10000
"""