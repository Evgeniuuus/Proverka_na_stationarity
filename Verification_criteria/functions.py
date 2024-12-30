import numpy as numpy


# --------------------------------------Критерий инверсий--------------------------------------
def Criterion_of_inversions(values):
    inv = 0
    for i in range(len(values) - 1):
        for j in range(i, len(values)):
            if values[i] > values[j] and i < j:
                inv += 1

    n = len(values)
    m = n * (n - 1) / 4

    d = n * (n - 1) * (2 * n + 5) / 72
    z = (inv - m) / numpy.sqrt(d)
    q1 = numpy.quantile(numpy.random.normal(0, 1, 100000), 1 - 0.05 / 2)
    q2 = numpy.quantile(numpy.random.normal(0, 1, 100000), 0.05 / 2)

    if q2 < z < q1:
        return 'Процесс стационарен'
    else:
        return 'Процесс нестационарен'


# ---------------------------------------Критерий серий---------------------------------------
def Criterion_of_series(values):
    median = numpy.median(values)
    plusminus = ['+' if values[i] > median else '-' for i in range(len(values))]
    cur_sign = plusminus[0]
    series = 1
    for i in range(1, len(values)):
        if plusminus[i] != cur_sign:
            series += 1
            cur_sign = plusminus[i]

    mu = len(values) / 2
    std = numpy.sqrt((mu - 1) * (mu - 2) / (len(values) - 1))
    quantile1 = numpy.quantile(numpy.random.normal(mu, std, 100000), 1 - 0.05 / 2)
    quantile2 = numpy.quantile(numpy.random.normal(mu, std, 100000), 0.05 / 2)

    if quantile2 < series < quantile1:
        return 'Процесс стационарен'
    else:
        return 'Процесс нестационарен'


# Далее функцию помог написать Анатолий
def Approximate_abbe(n):
    return (-1.1424 * pow(10, -7) * n ** 4 + 1.8834 * pow(10, -5) * n ** 3
            - 1.1798 * pow(10, -3) * n ** 2 + 3.637 * pow(10, -2) * n + 0.2641)


'''Критерий Аббе — это способ последовательных разностей, который применяется для 
обнаружения изменяющейся во времени систематической погрешности'''


# ------------------------------Критерий последовательных разностей--------------------------------
def Criterion_of_consecutive_differences(values):
    length = len(values)
    k = sum(values) / length
    d1 = 1 / (length - 1) * sum([(i - k) ** 2 for i in values])
    d2 = 1 / (2 * (length - 1)) * sum([(values[i + 1] - values[i]) ** 2 for i in range(len(values) - 1)])
    theta = d2 / d1

    if theta > Approximate_abbe(len(values)):
        return 'Процесс стационарен'
    else:
        return 'Процесс нестационарен'

