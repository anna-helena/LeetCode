from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''if amount == 0:
            return 0
        q = deque()
        seen = set()
        q.append((0,amount))
        seen.add(amount)
        while q:
            nr_tries,old_val = q.popleft()
            for coin in coins:
                new_val = old_val-coin
                if new_val == 0:
                    return nr_tries + 1
                if new_val > 0:
                    new_try = (nr_tries + 1,new_val)
                    if new_val not in seen:
                        q.append(new_try)
                        seen.add(new_val)
        return -1
        '''
        #####try dp solution
        @lru_cache(None)
        def get_dp(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            min_steps = float('inf')
            for coin in coins:
                res = get_dp(amount-coin)
                if res >= 0:
                    min_steps = min(min_steps,get_dp(amount-coin))
            return min_steps + 1 if min_steps != float('inf') else -1
        return get_dp(amount)
                