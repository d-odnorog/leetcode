# https://leetcode.com/problems/my-calendar-i/


class MyCalendar(object):
    def __init__(self):
        self.booking = []

    def book(self, start, end):
        for i, j in self.booking:
            if i < end and start < j:
                return False
        self.booking.append((start, end))

        return True


if __name__ == '__main__':
    obj = MyCalendar()

    assert obj.book(10, 20)
    assert not obj.book(15, 25)
    assert obj.book(20, 30)
