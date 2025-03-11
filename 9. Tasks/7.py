class Pagination:
    def __init__(self, random_list, quantity_elements):
        self._data, self.qe = random_list, quantity_elements
        self.len_data = len(self._data)
        self.cur_page = 0

    def get_visible_items(self):
        if self.cur_page > 0:
            return self._data[self.cur_page:self.cur_page + self.qe]
        else:
            return self._data[self.cur_page:]

    def prev_page(self):
        self.cur_page -= self.qe

    def next_page(self):
        self.cur_page += self.qe
        return self

    def first_page(self):
        self.cur_page = 0

    def last_page(self):
        self.cur_page = -(self.len_data % self.qe)

    def go_to_page(self, page_number):
        if page_number < 0:
            self.cur_page = 0
        else:
            self.cur_page = page_number


alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.next_page().next_page()
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)
