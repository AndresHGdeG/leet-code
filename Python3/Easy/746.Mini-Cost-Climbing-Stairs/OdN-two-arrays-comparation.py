

class Solution:

    def __init__(self):
        self.list_size = 0


    def minCostClimbingStairs(self, cost: list[int]) -> int:
        index = 0
        min_cost = 0
        self.list_size = len(cost)
        print('list_size', self.list_size)
        while index < self.list_size - 1:
            print(cost[index])
            first_step_cost = self.getFirstStepCost(cost, index)
            second_step_cost = self.getSecondStepCost(cost, index)
            if first_step_cost < second_step_cost:
                min_cost += first_step_cost
                index += 2
            else:
                min_cost += second_step_cost
                index += 3
            print('min_cost', min_cost)
        return min_cost
    
    def validateIndex(self, index: int) -> bool:
        if index+1 == self.list_size:
            return False
        return True

    def getFirstStepCost(self, cost: list[int], index : int) -> int:
        first_step_cost = cost[index] + cost[index+2]
        return first_step_cost
    
    def getSecondStepCost(self, cost: list[int], index : int) -> int:
        second_step_cost = cost[index+1] + cost[index+3]
        return second_step_cost
    
test = Solution()
cost = [10, 15, 20, 100]
result = test.minCostClimbingStairs(cost)
print('min cost: ', result)