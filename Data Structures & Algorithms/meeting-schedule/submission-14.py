"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # print(len(intervals))
        # print(len(set(intervals)))
        # if len(set(intervals)) != len(intervals):
        #     return False
        for i in range(len(intervals) - 1):
            for j in range(i + 1, len(intervals)):
                # if (intervals[j].start >= intervals[i].start and intervals[j].start < intervals[i].end) or\
                #     (intervals[j].end >= intervals[i].start and intervals[j].end < intervals[i].end) or\
                #     (intervals[j].start == intervals[i].start and intervals[j].end == intervals[i].end):
                #     return False
                if intervals[i].start < intervals[j].end and \
                   intervals[j].start < intervals[i].end:
                   return False
        return True  