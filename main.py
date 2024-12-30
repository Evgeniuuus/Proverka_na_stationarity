from Verification_criteria.functions import *

size = 500
noise = numpy.random.normal(0, 0.5, size)
time_series = [0 for i in range(size)]

for i in range(1, size):
    time_series[i] = 0.8 * time_series[i - 1] + float(noise[i])

spacing = 20
block_size = int(len(time_series) / spacing)
time_series = [float(numpy.mean(time_series[i:i + block_size])) for i in range(0, len(time_series), block_size)]

print(f'Критерий Инверсий говорит: {Criterion_of_inversions(time_series)}')
print(f'Критерий Серий говорит: {Criterion_of_series(time_series)}')
print(f'Критерий Последовательных разностей говорит: {Criterion_of_consecutive_differences(time_series)}')



