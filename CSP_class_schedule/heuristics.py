from random import randint
from copy import copy

from structures import *


def run_mrv():
    return backtrack(mrv, init_domains(), Schedule([], [], []))


def run_lcv():
    return backtrack(lcv, init_domains(), Schedule([], [], []))


def run_degree():
    return backtrack(degree, init_domains(), Schedule([], [], []))


def run_forward_checking():
    return backtrack(forward_checking, init_domains(), Schedule([], [], []))


def init_domains():
    domain = {}
    buf = []
    buf_lecture = []
    for day in week_schedule.keys():
        for time_slot in time_schedule.keys():
            for room in classrooms:
                buf.append(DomainEl(day, time_slot, room))
                if room.is_big:
                    buf_lecture.append(DomainEl(day, time_slot, room))
    for i in range(len(lessons)):
        if lessons[i].is_lecture:
            domain[i] = copy(buf_lecture)
        else:
            domain[i] = copy(buf)
    return domain


def mrv(domain):
    min_len = len(week_schedule) * len(classrooms) * len(time_schedule) * 2
    ind = list(domain.keys())[0]
    for key, value in domain.items():
        if len(value) < min_len:
            min_len = len(value)
            ind = key
    return ind


def degree(domain):
    counts = {}
    for key in domain:
        counts[key] = 0 if lessons[key].is_lecture else 1
        for i in domain:
            if i == key:
                continue
            if lessons[key].teacher == lessons[i].teacher:
                counts[key] += 1
            counts[key] += len(
                set(map(str, lessons[key].group)) & set(map(str, lessons[i].group))
            )

    ind = list(counts.keys())[0]
    max = 0
    for key, value in counts.items():
        if value > max:
            max = value
            ind = key
    return ind


def lcv(domain):
    counts = {}
    for i in domain:
        counts[i] = 0
        for key in domain:
            if i == key:
                continue

            for d in domain[key]:
                if not (
                    d.day == domain[i][0].day
                    and d.time == domain[i][0].time
                    and d.room == domain[i][0].room
                ) and not (
                    d.day == domain[i][0].day
                    and d.time == domain[i][0].time
                    and (
                        lessons[key].teacher == lessons[i].teacher
                        or set(map(str, lessons[key].group))
                        & set(map(str, lessons[i].group))
                    )
                ):
                    counts[i] += 1

    ind = list(counts.keys())[0]
    max = 0
    for key, value in counts.items():
        if value > max:
            max = value
            ind = key
    return ind


def forward_checking(domain):
    return list(domain.keys())[0]


def backtrack(heuristic, domain, schedule):
    if not domain:
        return schedule
    ind = heuristic(domain)
    if ind == -1:
        return None
    for d in domain[ind]:
        sch_copy = copy(schedule)
        sch_copy.times.append(Time(d.day, d.time))
        sch_copy.classrooms.append(d.room)
        sch_copy.lessons.append(lessons[ind])

        dom_copy = copy(domain)
        dom_copy.pop(ind)
        dom_copy = update_domain(dom_copy, lessons[ind], d.day, d.time, d.room)

        res = backtrack(heuristic, dom_copy, sch_copy)
        if res:
            return res

    return None


def update_domain(domain, lesson, day, time, room):
    for key in domain:
        buf = []
        for d in domain[key]:
            if not (d.day == day and d.time == time and d.room == room) and not (
                d.day == day
                and d.time == time
                and (
                    lessons[key].teacher == lesson.teacher
                    or set(map(str, lessons[key].group)) & set(map(str, lesson.group))
                )
            ):
                buf.append(d)
        domain[key] = buf

    return domain