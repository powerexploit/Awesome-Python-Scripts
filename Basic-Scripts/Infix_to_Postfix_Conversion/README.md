### Infix to Postfix

> • In Infix expression operator is in between every pair of operands.<br>
> • In Postfix expression, the operator is followed for every pair of operands. 

> Infix expression is converted to postfix conversion using Stack.
> Postfix expression is evaluated using Stack in Left to Right order.

##### If the scanned character is operand, show it as output. Else, If precedence of scanned operator is greater than the precedence of the operator in the stack,push it.

> Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator.

•  If the scanned input is '(', push it into stack<br>
• If the scanned input is ')' ,pop the stack and the output it until '(' comes.<br>
• Repeat above steps. Continue Pop and output from stack until it becomes empty.

##### It makes the code more efficient and even reduces the time complexity.
### Constraints
"""
 Input:
 Enter infix expression: A+C*(B^D-E)^(G+H*K)-K
 Output:
 Postfix expression:     ACBD^E-GHK*+^*+K-

 Time Complexity : O(n)
 Space Complexity: Θ(n)
"""
