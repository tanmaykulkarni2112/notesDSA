class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(')', '(');
        map.put(']', '[');
        Stack<Character> stk = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (map.containsKey(curr)) {
                char pop = stk.size() != 0 ? stk.pop() : '#';
                if (pop != map.get(curr))
                    return false;
            } else {
                stk.push(curr);
            }
        }
        return stk.isEmpty();
    }
}