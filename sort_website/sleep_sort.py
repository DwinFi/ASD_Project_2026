import time
import threading

def sleep_sort(values, unit=0.1):
    data = list(values)
    if not data:
        return []
    if any(value < 0 for value in data):
        return "Ошибка: Sleep Sort не поддерживает отрицательные числа."

    result = []
    lock = threading.Lock()
    start = threading.Event()
    start_at = 0.0

    def worker(value):
        start.wait()
        target = start_at + value * unit
        while (remaining := target - time.monotonic()) > 0:
            time.sleep(remaining)
        with lock:
            result.append(value)

    threads = [
        threading.Thread(target=worker, args=(value,), daemon=True)
        for value in data
    ]
    
    for thread in threads:
        thread.start()

    start_at = time.monotonic()
    start.set()
    
    for thread in threads:
        thread.join()
        
    return result