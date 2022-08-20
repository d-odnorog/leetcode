# https://leetcode.com/problems/minimum-number-of-refueling-stops/
import heapq
from typing import List


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        stations.append([target, 0])  # regard target as a station
        fuel = startFuel
        cnt, prev = 0, 0
        miss = []

        for pos, gas in stations:
            dis, prev = pos - prev, pos  # calculate the distance between two stations

            if fuel < dis:  # we are running out of fuel

                while (
                    miss and fuel < dis
                ):  # use Time machine to get some fuel we missed~
                    fuel += -heapq.heappop(miss)
                    cnt += 1  # cnt is how many times we travel back to get gas

                if fuel < dis:
                    # we have used all the gas, but still cannot get to the next station
                    return -1

            fuel -= dis
            heapq.heappush(
                miss, -gas
            )  # we don't need the gas until we run out of all fuel

        return cnt


if __name__ == '__main__':
    s = Solution()

    assert s.minRefuelStops(1, 1, []) == 0
    assert s.minRefuelStops(100, 1, [[10, 100]]) == -1
    assert s.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2
