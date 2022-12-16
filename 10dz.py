class MinStat:

    def __init__(self):
        self.list_number = []

    def add_number(self, number:float):
        self.list_number.append(number)

    def result(self):
        return min(self.list_number)

class MaxStat:

    def __init__(self):
        self.list_number = []


    def add_number(self, number:float):
        self.list_number.append(number)

    def result(self):
        return max(self.list_number)

class AverageStat:

    def __init__(self):
        self.list_number = []


    def add_number(self, number:float):
        self.list_number.append(number)

    def result(self):
        return sum(self.list_number) / len(self.list_number)

min_stat = MinStat()
max_stat = MaxStat()
average = AverageStat()
values = [23.77, 33.13, 4, 0, -104.33]

for i in values:
    min_stat.add_number(i)
    max_stat.add_number(i)
    average.add_number(i)

print(f'Минимальное число = {min_stat.result()}\n\
Максимальное число = {max_stat.result()}\n\
Среднее арифметическое = {round(average.result(), 2)}')