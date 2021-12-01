<?php
 
echo "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.<br>
    You may assume that each input would have exactly one solution, and you may not use the same element twice.<br>
    You can return the answer in any order.<br><br>

    Example 1:<br><br>

    Input: nums = [2,7,11,15], target = 9<br><br>
    Output: [0,1]<br><br>
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].<br>

    Example 2:<br><br>

    Input: nums = [3,2,4], target = 6<br><br>
    Output: [1,2]<br>
    Example 3:<br>

    Input: nums = [3,3], target = 6<br><br>
    Output: [0,1]<br>

";

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $resultarray[]=null;
        $temp_nums = $nums;
        for($i=0; $i<count($nums); $i++){
            for($j=$i+1; $j<count($temp_nums); $j++){
                if (($nums[$i] + $temp_nums[$j]) == $target){
                    $resultarray= [$i,$j];
                }
            }
        }
        return $resultarray;
    }    
}

$nums = [2,7,11,15];
$target = 9;

$cls = new Solution();

var_dump($cls->twosum($nums,$target));


?>