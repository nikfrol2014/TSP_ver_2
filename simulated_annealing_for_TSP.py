import random
import math

# Константа бесконечности
INF = float('inf')

# Заданная матрица стоимости
costMatrix = [
    [INF, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
    [2451, INF, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
    [713, 1745, INF, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
    [1018, 1524, 355, INF, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
    [1631, 831, 920, 700, INF, 663, 1021, 1769, 949, 796, 879, 586, 371],
    [1374, 1240, 803, 862, 663, INF, 1681, 1551, 1765, 547, 225, 887, 999],
    [2408, 959, 1737, 1395, 1021, 1681, INF, 2493, 678, 1724, 1891, 1114, 701],
    [213, 2596, 851, 1123, 1769, 1551, 2493, INF, 2699, 1038, 1605, 2300, 2099],
    [2571, 403, 1858, 1584, 949, 1765, 678, 2699, INF, 1744, 1645, 653, 600],
    [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, INF, 679, 1272, 1162],
    [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, INF, 1017, 1200],
    [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, INF, 504],
    [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, INF]
]

N = 13  # Количество городов


def route_length(route):
    """Вычисляет длину маршрута."""
    length = 0
    for i in range(len(route)):
        length += costMatrix[route[i]][route[(i + 1) % N]]
    return length


def simulated_annealing(initial_temp, cooling_rate, min_temp, iterations):
    """Алгоритм имитации отжига для TSP."""
    # Инициализация начального маршрута
    current_route = list(range(N))
    random.shuffle(current_route)
    current_length = route_length(current_route)

    best_route = current_route[:]
    best_length = current_length
    temp = initial_temp

    for _ in range(iterations): # Используем цикл for с заданным числом итераций
        # Генерация соседнего маршрута (обмен двух городов)
        new_route = current_route[:]
        i, j = random.sample(range(N), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_length = route_length(new_route)

        # Принятие решения с вероятностью, зависящей от температуры
        delta_e = new_length - current_length
        if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
            current_route = new_route
            current_length = new_length
            if current_length < best_length:
                best_route = current_route[:]
                best_length = current_length

        temp *= cooling_rate # Охлаждение
        if temp <= min_temp:
            break

    return best_route, best_length


# Параметры для алгоритма
initial_temp = 1000
cooling_rate = 0.99
min_temp = 1e-8
iterations = 500000 # Увеличить число итераций для большей точности

# Запуск алгоритма и вывод результатов
best_route, best_length = simulated_annealing(initial_temp, cooling_rate, min_temp, iterations)
print("Лучший маршрут:", best_route)
print("Длина лучшего маршрута:", best_length)
