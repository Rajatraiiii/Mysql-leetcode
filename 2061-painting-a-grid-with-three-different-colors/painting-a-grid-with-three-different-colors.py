class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        from itertools import product

        # Generate all valid rows (represented as tuples of colors)
        def generate_valid_rows(m):
            colors = [0, 1, 2]  # 0=red, 1=green, 2=blue
            valid_rows = []
            for row in product(colors, repeat=m):
                if all(row[i] != row[i+1] for i in range(m-1)):
                    valid_rows.append(row)
            return valid_rows

        valid_rows = generate_valid_rows(m)

        # Precompute which rows can follow which
        def can_follow(row1, row2):
            return all(row1[i] != row2[i] for i in range(m))

        adjacency = {}
        for row1 in valid_rows:
            adjacency[row1] = []
            for row2 in valid_rows:
                if can_follow(row1, row2):
                    adjacency[row1].append(row2)

        memo = {}

        def dp(col, prev_row):
            key = (col, prev_row)
            if key in memo:
                return memo[key]
            if col == n:
                return 1
            total = 0
            for next_row in adjacency[prev_row]:
                total = (total + dp(col+1, next_row)) % MOD
            memo[key] = total
            return total

        result = 0
        for row in valid_rows:
            result = (result + dp(1, row)) % MOD

        return result
