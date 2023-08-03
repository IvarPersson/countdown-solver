import argparse

from countdown import CountdownCalculator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numbers", help="The numbers used in the numbers round")
    parser.add_argument("-t", "--target", help="Target in the numbers round")
    parser.add_argument(
        "-l",
        "--letters",
        help="Letters for the word round, cannot be used at same time as --numbers or --target",
    )
    g = parser.add_mutually_exclusive_group()
    g.add_argument(
        "-dn", "--demo-nbr", "-Provides a demo of the numbers game", action="store_true"
    )
    g.add_argument(
        "-dw", "--demo-wrd", "-Provides a demo of the word game.", action="store_true"
    )
    args = parser.parse_args()

    numbers = args.numbers
    target = args.target
    letters = args.letters
    demo_nbr = True  # args.demo_nbr
    demo_wrd = args.demo_wrd
    if not (demo_nbr or demo_wrd):
        assert (numbers is None and target is None) or (
            numbers is not None and target is not None
        ), "Both numbers and target must be set for numbers game. None can be set for words game"
        if numbers is not None:
            assert letters is None, "You must provide letters in the word game"
        else:
            assert letters is not None, "You must provide letters in the word game"
            assert len(letters) == 9, "The number of letters must be 9."

    # Numbers game
    if demo_nbr or numbers is not None:
        cd_calc = CountdownCalculator()
        if demo_nbr:
            print("Demo of the numbers game, generating problem and solution")
            numbers, target, solution = cd_calc.make_random_solution()
            sol_tick = solution[2]
            solution = cd_calc.stack_to_string(solution[1])
            print(f"Target: {target}\nNumbers: {numbers}\nSolution: {solution}")
            print(f"Can be solved in {sol_tick} ways.")
            print("_____________________")

    # Word game


if __name__ == "__main__":
    main()

# stack = solutions[f"{target}"][1]
# tick = solutions[f"{target}"][2]
# print(f"It can be solved in {tick} ways, shortest solution:")
# print(self._stack_to_string(stack))
