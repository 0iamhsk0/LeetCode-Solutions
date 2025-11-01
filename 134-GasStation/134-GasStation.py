# Last updated: 11/1/2025, 9:34:37 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            # base case:
        if sum(gas) < sum(cost):
            return -1
        
        gas_tank = 0
        start = 0

        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            if gas_tank < 0:
                gas_tank = 0
                start = i + 1
            
        return start