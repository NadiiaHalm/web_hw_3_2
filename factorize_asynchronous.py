import time
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
from typing import Iterable


def factorize(numbers: Iterable[int]) -> Iterable[list[int]]:
    results = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        results.append(factors)
    return results


def callback(result):
    print(f"Result in callback: {result}")


if __name__ == "__main__":
    start_time = time.time()
    with Pool(cpu_count()) as p:
        p.map_async(
            factorize,
            [(128, 255, 99999, 10651060)],
            callback=callback,
        )

        p.close()
        p.join()

    end_time = time.time()
    print("Синхронний час виконання:", end_time - start_time)


