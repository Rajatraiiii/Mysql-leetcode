import bisect

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            available = workers[-k:]  # strongest k workers
            available.sort()
            pills_left = pills

            for i in reversed(range(k)):  # hardest to easiest
                task_strength = tasks[i]

                # If strongest worker can do it
                if available[-1] >= task_strength:
                    available.pop()
                else:
                    if pills_left == 0:
                        return False
                    # Find leftmost worker who can be boosted to meet task
                    idx = bisect.bisect_left(available, task_strength - strength)
                    if idx == len(available):
                        return False
                    # Remove that worker and use pill
                    del available[idx]
                    pills_left -= 1
            return True

        left, right = 0, min(len(tasks), len(workers))
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
