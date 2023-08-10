"""
Calculator for the numbers-game in the british TV-show Countdown
"""

import random
from math import inf, isinf

operations = [
    (lambda a, b: a + b, "+"),
    (lambda a, b: a - b, "-"),
    (lambda a, b: a * b, "*"),
    (lambda a, b: a / b if a % b == 0 else inf, "/"),
]


class CountdownCalculator:
    """
    Countdown calculator. Finds the correct way to get the answer or the closest to the
    correct value
    """

    def __init__(self):
        self.big_values = [25, 50, 75, 100]
        self.small_values = list(range(1, 11))
        self.small_values = self.small_values + self.small_values.copy()

    def _pick_from_the_top(self, nbr: int):
        """
        Picks the large ones in the stack
        """
        assert nbr > -1, "Number of big ones cannot be negative"
        assert nbr < 5, "Number of big ones must be max 4"
        values = []
        big_val = self.big_values.copy()
        for _ in range(nbr):
            val = random.choice(big_val)
            big_val.remove(val)
            values.append(val)
        return values

    def _pick_from_the_others(self, nbr: int):
        """
        Picks the small ones in the stack
        """
        assert nbr > -1, "Number of small ones cannot be negative"
        assert nbr < 7, "Number of small ones must be max 6"
        values = []
        small_val = self.small_values.copy()
        for _ in range(nbr):
            val = random.choice(small_val)
            small_val.remove(val)
            values.append(val)
        return values

    def _evaluate(self, stack):
        """
        Evaluates the value of the given stack
        """
        total = 0
        operand = operations[0][0]
        for item in stack:
            if isinstance(item, int):
                total = operand(total, item)
                if isinf(total):
                    return 0, 1e10
            else:
                operand = item[0]
        return int(total), len(stack)

    def _solve(self, target, numbers) -> list:
        solutions = {}

        def part_solve(stack, nums):
            for idx, val in enumerate(nums):
                if isinf(val):
                    continue
                if stack != []:
                    if (stack[-1][1] == "*" or stack[-1][1] == "/") and val == 1:
                        # Multiplying or dividing by 1 is unnecessary
                        continue
                stack.append(val)
                remaining = nums[:idx] + nums[idx + 1 :]
                res, length = self._evaluate(stack)
                if abs(res - target) <= 10:
                    if f"{res}" in solutions:
                        solutions[f"{res}"][2] = solutions[f"{res}"][2] + 1
                        if solutions[f"{res}"][0] > length:
                            solutions[f"{res}"] = [
                                length,
                                stack.copy(),
                                solutions[f"{res}"][2],
                            ]
                    else:
                        solutions[f"{res}"] = [length, stack.copy(), 1]
                if len(remaining) > 0:
                    for oper in operations:
                        stack.append(oper)
                        stack = part_solve(stack, remaining)
                        stack = stack[:-1]
                stack = stack[:-1]
            return stack

        part_solve([], numbers)

        if f"{target}" in solutions:
            return solutions[f"{target}"]
        # TODO: choose best solution and return its sum
        return [0]

    def stack_to_string(self, stack: list):
        """
        Takes in a stack representation and gives a string
        """
        reps = [str(item) if isinstance(item, int) else item[1] for item in stack]
        return " ".join(reps)

    def find_solution(self, numbers: list, target: int) -> list:
        """
        Finds the correct solution given the inputs.
        """
        assert target > 100, "Target must be bigger than 100."
        assert target < 1000, "Target must be smaller than 1000."
        assert len(numbers) == 6, "6 numbers must be given"
        print(f"Solving for target: {target} and numbers: {numbers}")
        return self._solve(target, numbers)

    def make_random_solution(self):
        """
        Generates a random problem and finds the soluton
        """
        target = random.randint(100, 1000)
        nbr_top = random.randint(0, 4)
        numbers = self._pick_from_the_top(nbr_top) + self._pick_from_the_others(
            6 - nbr_top
        )
        solution = self.find_solution(numbers, target)
        return numbers, target, solution
