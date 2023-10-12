class Average:
    def __init__(self, a: list[int], b: list[int]):
        self.a = a
        self.b = b

    def average_arrays(self):
        summ_a = 0
        summ_b = 0
        for i in self.a:
            summ_a += i
        avg_a = summ_a / len(self.a)

        for i in self.b:
            summ_b += i
        avg_b = summ_b / len(self.b)

        if avg_a > avg_b:
            return "Первый список имеет большее среднее значение"
        elif avg_a == avg_b:
            return "Средние значения равны"
        else:
            return "Второй список имеет большее среднее значение"
