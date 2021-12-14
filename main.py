from solutions.day1 import solve_day1
from solutions.day10 import solve_day10
from solutions.day11 import solve_day11
from solutions.day12 import solve_day12
from solutions.day13 import solve_day13
from solutions.day14 import solve_day14
from solutions.day2 import solve_day2
from solutions.day3 import solve_day3
from solutions.day4 import solve_day4
from solutions.day5 import solve_day5
from solutions.day6 import solve_day6
from solutions.day7 import solve_day7
from solutions.day8 import solve_day8
from solutions.day9 import solve_day9


def main():
    print('\n--------------------------------------------------\n')
    for i in range(1, 15):
        globals()['solve_day%d' % i]()
        print('\n--------------------------------------------------\n')


if __name__ == '__main__':
    main()
