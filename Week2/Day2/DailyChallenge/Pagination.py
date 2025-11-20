import math

class Pagination:
    # STEP 1: constructor
    def __init__(self, items=None, page_size=10):
        # STEP 2.1: if items is None, set it to an empty list
        if items is None:
            items = []

        # STEP 2.2: save instance attributes
        self.items = items          
        self.page_size = page_size  
        self.current_idx = 0        

        # STEP 2.3: calculate total pages using math.ceil
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # STEP 3: show visible items on the current page
    def get_visible_items(self):
        
        start = self.current_idx * self.page_size
       
        end = start + self.page_size

        return self.items[start:end]

    # STEP 4: go to specific page (user enters page starting from 1)
    def go_to_page(self, page_num):
        # STEP 4.1: convert input to int (in case user enters "3")
        page_num = int(page_num)

        # STEP 4.2: check valid range
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range!")

        # STEP 4.3: convert user page number (1-based) to index (0-based)
        self.current_idx = page_num - 1

        return self  # allow chaining

    # STEP 4: go to first page
    def first_page(self):
        self.current_idx = 0
        return self  # chaining

    # STEP 4: go to last page
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self  # chaining

    # STEP 4: next page
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self  # chaining

    # STEP 4: previous page
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self  # chaining

    # BONUS: STEP 5 — custom print
    def __str__(self):
       
        return "\n".join(self.get_visible_items())
#Step 6: Test Your Code
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']
