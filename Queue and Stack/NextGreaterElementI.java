class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack <Integer> stack = new Stack<>();
        for(int val : nums1) {
            stack.push(val);
        }
        Stack <Integer> helper = new Stack<>();
        HashMap <Integer, Integer> map = new HashMap<>();
        for(int num : nums2) {
            // when the stack is not empty and the top element of is lesser than arrays[i], pop and map
            while(!helper.isEmpty() && helper.peek() < num ) { // This will map the greater number
                map.put(helper.pop(), num); 
            }
            helper.push(num);
        }
        // assign other values with -1
        while(!helper.isEmpty()) {
            map.put(helper.pop(), -1);
        }
        int[] result = new int[nums1.length];
        for(int i = 0; i < nums1.length; i++) {
            result[i] = map.get(nums1[i]);
        }
        return result;
    }
}