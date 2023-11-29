from collections import namedtuple

week_schedule = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
time_schedule = {
    1: "8:40-10:15",
    2: "10:35-12:10",
    3: "12:20-13:55",
}

#  Main data classes
Classroom = namedtuple("Classroom", "room is_big")
Time = namedtuple("Time", "weekday time")
Teacher = namedtuple("Teacher", "name")
Subject = namedtuple("Subject", "name")
Group = namedtuple("Group", "name")
Lesson = namedtuple("Lesson", "teacher subject group is_lecture per_week")
Schedule = namedtuple("Schedule", "lessons classrooms times")
DomainEl = namedtuple("DomainEl", "day time room")

Classroom.__repr__ = lambda c: f"{c.room} ({'big' if c.is_big else 'small'})"
Teacher.__repr__ = lambda t: f"{t.name.split()[1]}"
Subject.__repr__ = lambda s: f"{s.name.split()[1]}"
Group.__repr__ = lambda g: f"{g.name}"
Lesson.__repr__ = (
    lambda l: f"{l.teacher} | {l.subject} | {l.group} | "
    f"{'Lecture' if l.is_lecture else 'Seminar'} {l.per_week}/week"
)


def gen_repr(g: Schedule):
    output = ""
    for i in range(len(g.lessons)):
        output += f"{g.lessons[i]},   {g.classrooms[i]},   {g.times[i]}\n"
    return output


Schedule.__repr__ = lambda g: gen_repr(g)

#  Sample data for schedule
classrooms = [
    Classroom(43, True),
    Classroom(42, True),
    Classroom(41, True),
    Classroom(228, False),
    Classroom(217, False),
    Classroom(206, False),
    #  Classroom(205, False),
]

schedule = [
    Time(w, n)
    for w in range(1, len(week_schedule.keys()) + 1)
    for n in range(1, len(week_schedule.keys()) + 1)
]

teachers = [
    Teacher(name)
    for name in (
        "0 T1",
        "1 T2",
        "2 T3",
        "3 T4",
        "4 T5",
        "5 T6",
        "6 T7",
        "7 T8",
        "8 T9",
        "9 T10",
        "10 T11",
        "11 T12",
        "12 T13",
        "13 T14",
        "14 T15",
        "15 T16",
        "16 T17",
        "17 T18",
        "18 T19",
    )
]

subjects = [
    Subject(name)
    for name in (
        "0 S1",
        "1 S2",
        "2 S3",
        "3 S4",
        "4 S5",
        "5 S6",
        "6 S7",
        "7 S8",
        "8 S9",
        "9 S10",
        "10 S11",
        "11 S12",
        "12 S13",
        "13 S14",
        "14 S15",
        "15 S16",
        "16 S17",
        "17 S18",
    )
]

groups = [
    Group(name)
    for name in (
        "G1",
        "G2",
        "G3",
        "G4",
        "G5",
    )
]

lessons = [
    Lesson(teachers[0], subjects[0], groups[0], False, 1),
    Lesson(teachers[1], subjects[1], groups[0:5], True, 1),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[3], subjects[12], groups[0], True, 1),
    Lesson(teachers[4], subjects[4], groups[0:5], True, 1),
    Lesson(teachers[5], subjects[4], groups[0], False, 1),
    Lesson(teachers[5], subjects[15], groups[0], True, 1),
    Lesson(teachers[9], subjects[6], groups[0:5], True, 1),
    Lesson(teachers[13], subjects[4], groups[0], False, 1),
    Lesson(teachers[13], subjects[16], groups[0], True, 2),
    Lesson(teachers[13], subjects[16], groups[0], True, 2),
    Lesson(teachers[5], subjects[4], groups[1], False, 1),
    Lesson(teachers[5], subjects[4], groups[2], False, 1),
    Lesson(teachers[6], subjects[4], groups[1], False, 1),
    Lesson(teachers[7], subjects[4], groups[2], False, 1),
    Lesson(teachers[8], subjects[3], groups[1:3], True, 1),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[18], subjects[10], groups[1:3], True, 1),
    Lesson(teachers[5], subjects[4], groups[3], False, 1),
    Lesson(teachers[5], subjects[4], groups[4], False, 1),
    Lesson(teachers[6], subjects[4], groups[3], False, 1),
    Lesson(teachers[6], subjects[4], groups[4], False, 1),
    Lesson(teachers[14], subjects[12], groups[3:5], True, 2),
    Lesson(teachers[14], subjects[12], groups[3:5], True, 2),
    Lesson(teachers[15], subjects[13], groups[3:5], False, 1),
    Lesson(teachers[16], subjects[11], groups[3:5], True, 2),
    Lesson(teachers[16], subjects[11], groups[3:5], True, 2),
    Lesson(teachers[17], subjects[14], groups[3:5], True, 1),
    Lesson(teachers[17], subjects[17], groups[3:5], True, 1),
]