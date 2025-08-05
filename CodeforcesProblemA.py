def mex(arr):
    present = set(arr)
    mex_val = 0
    while mex_val in present:
        mex_val += 1
    return mex_val


def solve_case(S):
    n = len(S)
    if n <= 20:
        memo = {}

        def dp(remaining_indices):
            key = tuple(sorted(remaining_indices))
            if key in memo:
                return memo[key]

            if not remaining_indices:
                return 0

            max_score = 0
            for mask in range(1, 1 << len(remaining_indices)):
                subset_indices = []
                for i in range(len(remaining_indices)):
                    if mask & (1 << i):
                        subset_indices.append(remaining_indices[i])

                subset = [S[i] for i in subset_indices]
                score = max(sum(subset), mex(subset))

                new_remaining = [idx for idx in remaining_indices if idx not in subset_indices]

                total_score = score + dp(new_remaining)
                max_score = max(max_score, total_score)

            memo[key] = max_score
            return max_score

        return dp(list(range(n)))

    else:
        total = 0
        for x in S:
            total += max(x, mex([x]))
        return total


t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    print(solve_case(S))