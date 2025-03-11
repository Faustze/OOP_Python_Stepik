import heapq


class HighScoreTable:
    def __init__(self, max_records):
        self.max_records = max_records
        self._data = []

    @property
    def scores(self):
        return sorted(self._data, reverse=True)
    
    def update(self, record):
        if len(self._data) < self.max_records:
            heapq.heappush(self._data, record)  
        else:
            heapq.heappushpop(self._data, record)
                    
    def reset(self):
        self._data.clear()