from collections import deque

jobs = list(map(int, input().split(',')))
job_index = int(input())


job = jobs[job_index]
clock_cycle = 0

jobs.sort()
jobs = deque(job for job in jobs)
JOB_DONE = False

while not JOB_DONE:
    cycle = jobs.popleft()
    clock_cycle += cycle
    if cycle == job:
        while job in jobs:
            clock_cycle += cycle
            jobs.popleft()
        JOB_DONE = True
        break

print(clock_cycle)





