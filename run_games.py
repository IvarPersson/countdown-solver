"""
Run module for the games
"""
import argparse
import ast

from solvers.countdown import CountdownCalculator
from solvers.word_game import WordGameCalculator


def main():
    """
    Main method to control the two games
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numbers", help="The numbers used in the numbers round")
    parser.add_argument("-t", "--target", help="Target in the numbers round")
    parser.add_argument(
        "-l",
        "--letters",
        help="Letters for the word round, cannot be used at same time as --numbers or --target",
    )
    grp = parser.add_mutually_exclusive_group()
    grp.add_argument(
        "-dn", "--demo-nbr", "-Provides a demo of the numbers game", action="store_true"
    )
    grp.add_argument(
        "-dw", "--demo-wrd", "-Provides a demo of the word game.", action="store_true"
    )
    args = parser.parse_args()

    numbers = args.numbers
    target = args.target
    letters = args.letters
    demo_nbr = args.demo_nbr
    demo_wrd = args.demo_wrd
    if not (demo_nbr or demo_wrd):
        assert (numbers is None and target is None) or (
            numbers is not None and target is not None
        ), "Both numbers and target must be set for numbers game. None can be set for words game"
        if numbers is not None:
            assert letters is None, "You must provide letters in the word game"
            try:
                numbers = ast.literal_eval(numbers)
            except ValueError as _:
                print("The numbers must be ints in a list")
                return
            try:
                target = int(target)
            except ValueError as _:
                print("Target must be an int")
                return
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
        else:
            solution = cd_calc.find_solution(numbers, target)
            if solution == [0]:
                print("No solution exists")
            else:
                sol_tick = solution[2]
                solution = cd_calc.stack_to_string(solution[1])
                print(f"Solution: {solution}")
                print(f"Can be solved in {sol_tick} ways.")
                print("_____________________")

    # Word game
    if demo_wrd or letters is not None:
        word_calc = WordGameCalculator()
        if demo_wrd:
            print("Demo of the word game, generating problem and solution")
            tmp, tmp2 = word_calc.generate_example_problem()
            all_true_words = tmp
            letters = tmp2
        else:
            all_true_words = word_calc.generate_true_words(letters)
        print(f"Letter given: {letters}")
        break_flag = 0
        for nbr_letters in range(9, 2, -1):
            true_words = all_true_words[f"{str(nbr_letters)}"]
            if len(true_words) == 0:
                print(f"There are no words of length {nbr_letters}")
            else:
                print(f"There are {len(true_words)} word(s) of length {nbr_letters}:")
                for t_w in true_words:
                    print(t_w)
                if break_flag:
                    break
                if len(true_words):
                    break_flag = 1
            print("----------")


if __name__ == "__main__":
    main()
