import sys
from itertools import product
input = sys.stdin.readline

def main():
    N = int(input())
    M = set(input())
    broken_buttons = set(map(int, input().split())) if M else set()
    print(Solution(broken_buttons).find_nearest_channel(N))

class Solution:
    def __init__(self, broken_buttons:set) -> None:
        self.buttons = {i for i in range(10) if not i in broken_buttons}
    
    def is_enable(self, number:int) -> bool:
        if set(map(int, str(number)))-self.buttons:
            return False
        return True
    
    def find_nearest_channel(self, goal_channel:int) -> int:
        ans = abs(goal_channel-100)
        for number in range(1000001):
            if self.is_enable(number):
                ans = min(ans, len(str(number))+abs(number-goal_channel))
        return ans

if __name__ == '__main__':
    main()