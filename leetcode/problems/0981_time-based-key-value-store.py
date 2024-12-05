from bisect import bisect_right


class TimeMap:

    def __init__(self):
        self.time_dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = list()

        # Because set's timestamps are increasing, just append to have an ascending array
        self.time_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""

        # Binary search the timestamp in previous timestamps
        # Use ASCII 127 to make sure the target pair is larger than the previous
        idx = bisect_right(self.time_dict[key], (timestamp, chr(127)))
        if idx == 0:
            return ""
        return self.time_dict[key][idx - 1][1]
