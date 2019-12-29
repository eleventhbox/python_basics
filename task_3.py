class Cell():
    def __init__(self, part_num):
        self.__part_num = part_num

    @property
    def part_num(self):
        return self.__part_num

    def __add__(self, other):
        return Cell(self.part_num + other.part_num)

    def __sub__(self, other):
        res = self.part_num - other.part_num
        if res > 0:
            return Cell(res)
        else:
            raise Exception("Result of subtraction should be greater then 0 ")

    def __mul__(self, other):
        return Cell(self.part_num * other.part_num)

    def __truediv__(self, other):
        return Cell(self.part_num // other.part_num)

    def make_order(self, parts_per_row):
        row_num, remainder = self.part_num // parts_per_row, self.part_num % parts_per_row
        row_lst = ['*' * parts_per_row for j in [i for i in range(row_num)]]
        if remainder > 0:
            row_lst.append('*' * remainder)
        return '\n'.join(row_lst)


c1 = Cell(10)
c2 = Cell(4)
print((c1 + c2).make_order(5))
print('=======')
print((c1 - c2).make_order(5))
print('=======')
print((c1 * c2).make_order(5))
print('=======')
print((c1 / c2).make_order(5))


