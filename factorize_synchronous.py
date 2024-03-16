import time


def factorize(numbers):
    results = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        results.append(factors)
    return results


if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()
    results = factorize(numbers)
    end_time = time.time()
    print("Синхронний час виконання:", end_time - start_time)
    print("Результати:", results)