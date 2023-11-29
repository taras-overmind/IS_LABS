from time import time
from heuristics import *
from structures import *


def print_schedule(
    solution: Schedule,
):
    for day in week_schedule:
        print("\n" + "=" * 100)
        print(f"{week_schedule[day].upper()}")
        for time in time_schedule:
            print("\n\n" + time_schedule[time])
            for c in classrooms:
                print(f"\n{c}", end="\t\t")
                for i in range(len(solution.lessons)):
                    if (
                        solution.times[i].weekday == day
                        and solution.times[i].time == time
                        and solution.classrooms[i].room == c.room
                    ):
                        print(solution.lessons[i], end="")


def main():

    solution = run_mrv()
    print_schedule(solution)

    #  Minimum Remaining Values
    start_time = time()
    run_mrv()
    print(f"MRV: {time() - start_time}")

    #  Least Constraining Value
    start_time = time()
    run_lcv()
    print(f"LCV: {time() - start_time}")

    #  Degree heuristic
    start_time = time()
    run_degree()
    print(f"Degree: {time() - start_time}")

    #  Forward checking
    start_time = time()
    run_forward_checking()
    print(f"Forward checking: {time() - start_time}")


if __name__ == "__main__":
    main()