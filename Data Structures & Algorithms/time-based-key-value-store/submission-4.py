class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append([timestamp, value])
        else:
            self.hashMap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if not (key in self.hashMap): return ""
        subArr = self.hashMap[key]
        res = ""

        l = 0
        r = len(subArr) - 1
        while(l <= r):
            m = (l + r + 1) // 2
            if subArr[m][0] <= timestamp:
                res = subArr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

