import math


class Pagination:
    def __init__(self, items=(), page_size=10):
        self._items = list(items)
        self._page_size = page_size
        self._total_pages = math.ceil(len(items) / page_size)
        self._current_page = 1

    @property
    def page_size(self):
        return self._page_size

    @property
    def total_pages(self):
        return self._total_pages

    @property
    def current_page(self):
        return self._current_page
    
    def prev_page(self):
        self._current_page = max(1, self.current_page - 1)
        return self

    def next_page(self):
        self._current_page = min(self.total_pages, self.current_page + 1)
        return self

    def first_page(self):
        self._current_page = 1
        return self
 
    def last_page(self):
        self._current_page = self.total_pages
        return self
    
    def go_to_page(self, page):
        self._current_page = max(1, min(self.total_pages, page))
        return self
 
    def get_visible_items(self):
        start = (self.current_page - 1) * self.page_size
        stop = min(self.current_page * self.page_size, len(self._items))
        return self._items[start:stop]