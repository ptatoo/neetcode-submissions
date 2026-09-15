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

        l = 0
        r = len(subArr) - 1
        while(l < r):
            m = (l + r + 1) // 2
            arr = subArr[m]
            if arr[0] == timestamp: return arr[1]
            if arr[0] > timestamp: r = m - 1
            else: l = m
        
        arr = subArr[l]
        if arr[0] <= timestamp: return arr[1]
        return ""

