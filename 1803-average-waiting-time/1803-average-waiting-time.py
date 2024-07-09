class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        time_waiting = customers[0][1]
        finished_prev = customers[0][0] + customers[0][1]

        for customer_ind in range(1, n, 1):
            times = customers[customer_ind]
            arrive = times[0]

            start_cook = max(arrive, finished_prev)
            end_time = start_cook + times[1]
            finished_prev = end_time
            time_waiting += end_time - arrive

        return time_waiting / n