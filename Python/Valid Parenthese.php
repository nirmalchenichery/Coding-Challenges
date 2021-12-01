<?php


echo "
        Valid Parentheses <br><br>


    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.<br><br>

	An input string is valid if:<br>
    Open brackets must be closed by the same type of brackets.<br>
	Open brackets must be closed in the correct order.<br><br>

	Example 1:<br><br>

	Input: s = '()'<br>
	Output: true<br><br>

	Example 2:<br><br>

	Input: s = '()[]{}'<br>
	Output: true<br><br>

	Example 3:<br><br>

	Input: s = '(]'<br>
	Output: false<br><br>

	Example 4:<br><br>

	Input: s = '([)]'<br>
	Output: false<br><br>

	Example 5:<br><br>

	Input: s = '{[]}'<br>
	Output: true<br><br>

";

class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
		$array_map_close_to_open = [")" => "(", "]" => "[", "}" => "{"];

	/*
		for( $i = 0; $i < 2); $i++)
		{
			var_dump($s.charAt(i));
		}
*/





    }
}

//$validate_input = "()";
//$validate_input ="()[]{}";
//$validate_input = "(]";
//$validate_input ="([)]";
$validate_input ="{[]}";

$cls = new Solution();

var_dump($cls->isValid($validate_input));





/*
class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        array_map_close_to_open = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in array_map_close_to_open:

                if stack and stack[-1] == array_map_close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False




p1 = Solution()
print(p1.isValid(validate_input))
*/

?>