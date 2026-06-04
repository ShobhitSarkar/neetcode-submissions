/**
Possible Approach: 
- Loop through every char in the array 
    - Push only these characters {, (, [ onto the stack whenver encountered 
    - Now when we have any of the characters }, ), ] : 
        - Peek and see the top most element and pop it it is a match 
    - then use .empty() to give the output of the function 
**/
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (current == '{' || current == '(' || current == '[') {
                stack.push(current);
            } else if (current == '}') {
                if (stack.isEmpty() || stack.peek() != '{') {
                    return false;
                }
                stack.pop();
            } else if (current == ')') {
                if (stack.isEmpty() || stack.peek() != '(') {
                    return false;
                }
                stack.pop();
            } else if (current == ']') {
                if (stack.isEmpty() || stack.peek() != '[') {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}