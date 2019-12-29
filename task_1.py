class Matrix:

    @staticmethod
    def __check_mtrx(mtrx, other_mtrx=None):
        if not isinstance(mtrx, list):
            raise Exception('Matrix should be of type list')
        for row in mtrx:
            if not isinstance(row, list):
                raise Exception('Rows of the matrix should be of type list')
        if len(set([len(row) for row in mtrx])) != 1:
            raise Exception('Rows of the matrix should have the same number of columns')
        if other_mtrx is not None:
            if len(mtrx) != len(other_mtrx):
                raise Exception('Two matrices should have the same number of rows')
            if set([len(row) for row in other_mtrx]) != set([len(row) for row in mtrx]):
                raise Exception("""Rows of the added matrix should have the same number of columns that the original matrix has""")

    def __init__(self, mtrx):
        Matrix.__check_mtrx(mtrx)
        self._mtrx = mtrx


    def __str__(self):
        return '\n'.join(['   '.join([str(col) for col in row]) for row in self._mtrx])

    def __add__(self, other):
        Matrix.__check_mtrx(self._mtrx, other._mtrx)
        row_list = []
        for row_idx, row in enumerate(self._mtrx):
            col_list = []
            for col_idx, col in enumerate(row):
                col_list.append(col + other[row_idx][col_idx])
            row_list.append(col_list)
        return Matrix(row_list)

    def __getitem__(self, index):
        return self._mtrx[index]


m = Matrix([
    [1,2,3],
    [4,5,6]
])

mm = Matrix([
    [7,8,9],
    [10,11,12]
])

print('====================')
print('Original matrix')
print(m)
print('====================')
print('Result of addition')
print(m + mm)