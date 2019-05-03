import os
import random
import string
from time import perf_counter
from typing import List, Dict, Union


def random_text(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))


class StopWatch:

    _start_time: float
    _wrap_times: List[float]
    _wrap_comments: List[str]

    def start(self):
        self._start_time = perf_counter()
        self._wrap_comments = ['']
        self._wrap_times = [0.0]

    def wrap(self, comment: str = ''):
        wrap_time = perf_counter() - self._start_time
        self._wrap_times.append(wrap_time)
        self._wrap_comments.append(comment)

    def get_report(self) -> List[Dict[str, Union[str, float]]]:
        max_comment_length = max([len(c) for c in self._wrap_comments])
        return [{
            'comment': c.ljust(max_comment_length),
            'time': t-self._wrap_times[i-1]
        } for i, (t, c) in enumerate(zip(self._wrap_times, self._wrap_comments)) if i > 0]

    def describe(self, report: List[Dict[str, Union[str, float]]] = None):
        if report is None:
            report = self.get_report()
        message = os.linesep.join([
            '[{0}] {1} : {2}[s]'.format(i, r['comment'], round(r['time'], 3)) for i, r in enumerate(report)
        ])
        print(message)
