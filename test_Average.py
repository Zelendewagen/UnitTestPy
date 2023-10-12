from Average import Average


def test_average_arrays():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    avg = Average(a, b)
    assert avg.average_arrays() == "Второй список имеет большее среднее значение"

    a = [6, 7, 8, 9, 10]
    b = [1, 2, 3, 4, 5]
    avg = Average(a, b)
    assert avg.average_arrays() == "Первый список имеет большее среднее значение"

    a = b
    avg = Average(a, b)
    assert avg.average_arrays() == "Средние значения равны"
