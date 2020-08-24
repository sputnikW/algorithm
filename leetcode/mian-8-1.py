class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        from collections import deque
        dp_state = deque([1,2,4])
        for i in range(4, n+1):
            dp_i_1 = dp_state.pop() # dp(i-1)
            dp_i_2 = dp_state.pop() # dp(i-2)
            dp_i_3 = dp_state.pop() # dp(i-3)
            dp_state.extend([
                dp_i_2,
                dp_i_1,
                (dp_i_1 + dp_i_2 + dp_i_3) % 1000000007
            ])
        
        return dp_state.pop()