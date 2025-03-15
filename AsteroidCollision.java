class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int num : asteroids) {
            if (num > 0) { // positive always printed
                stack.push(num);
            } else {
                // negative number
                while (!stack.isEmpty() && stack.peek() > 0 && stack.peek() < Math.abs(num)) {
                    stack.pop();
                }
                if(stack.isEmpty() || stack.peek() < 0) {
                    stack.push(num);
                }
                if(stack.peek() == -num) {
                    stack.pop();
                }
            }
        }
        int i = stack.size() - 1;
        int[] result = new int[stack.size()];
        while(!stack.isEmpty()) {
            result[i--] = stack.pop();
        }
        return result;
    }
}