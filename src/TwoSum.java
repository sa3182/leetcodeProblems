import java.util.HashMap;
import java.util.Map;

public class TwoSum {

        public int[] twoSum(int[] nums, int target) {

            Map<Integer, Integer> twoSum = new HashMap<>();
            for(int i=0;i<nums.length;i++){
                int temp = target-nums[i];
                if(twoSum.containsKey(temp)){
                    return new int[]{twoSum.get(temp), i};
                }
                twoSum.put(nums[i],i);
            }
            return new int[]{};
        }
}
