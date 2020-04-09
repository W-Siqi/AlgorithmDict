# 这题可能的陷阱，就是这个环不一定是第一个数字，可能是中间的某一个。所以visited要存所有的，而不是开始
class Solution:
    def isHappy(self, n: int) -> bool:
        def checkHappy(number, visited):
            if number == 1:
                return True
            if number in visited:
                return False
            
            visited.add(number)
            nextNumber = 0
            while number > 0:
                nextNumber += pow(number%10,2)
                number = number//10
            
            return checkHappy(nextNumber,visited)
        return checkHappy(n,set())