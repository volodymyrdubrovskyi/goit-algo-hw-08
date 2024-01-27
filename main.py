import heapq

def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]

cable_lenth = [8,12,18,7,6,4,9]
print("Заданий набір довжин кабелів: ", cable_lenth)
print("Порядок об'єднання, який мінімізує загальні витрати, наступний:")
arr = heap_sort(cable_lenth)
combination_price = 0
step = 1
while len(arr)>1:
    r = arr[0] + arr[1]
    combination_price += r
    print(f"Крок {step}: об'єднуємо кабелі довжинами {arr[0]} та {arr[1]},")
    arr = arr[2:]
    arr.append(r)
    print(f"        набір довжин кабелів після з'єднання: {arr}, поточні витрати на з'єднання: {combination_price}")
    arr = heap_sort(arr)
    step += 1