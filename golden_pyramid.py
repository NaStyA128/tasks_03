class Pyramid:


    def __init__(self):
        a =self.__go__([[7],
                        [2, 3],
                        [3, 3, 1],
                        [3, 1, 5, 4],
                        [3, 1, 3, 1, 3],
                        [2, 2, 2, 2, 2, 2],
                        [5, 6, 4, 5, 6, 4, 3]])
        b = self.__go__([[1],
                         [2, 1],
                         [1, 2, 1],
                         [1, 2, 1, 1],
                         [1, 2, 1, 1, 1],
                         [1, 2, 1, 1, 1, 1],
                         [1, 2, 1, 1, 1, 9, 1]])
        print('a = ' + repr(a))
        print('b = ' + repr(b))

    def __go__(self, triangle, x=0, y=0, max_sum=0):
        if x == len(triangle) - 1:
            return max_sum + triangle[x][y]
        return max(self.__go__(triangle, x + 1, y, max_sum + triangle[x][y]),
                   self.__go__(triangle, x + 1, y + 1, max_sum + triangle[x][y]))


def main():
    Pyramid()

if __name__ == '__main__':
    main()

