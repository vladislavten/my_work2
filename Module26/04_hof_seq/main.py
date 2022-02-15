class QHofstadter:
    def __init__(self, item) -> None:
        self.item = item[:]

    def __next__(self) -> list:
        try:
            QHof = self.item[-self.item[-1]] + self.item[-self.item[-2]]
            self.item.append(QHof)
            return QHof
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self) -> list:
        return self.item


QHof = QHofstadter([1, 1])
resolve = [next(QHof) for _ in range(10)]
print(resolve)
