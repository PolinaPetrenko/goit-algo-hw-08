import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # перетворюємо список кабелів у купу

    total_cost = 0
    while len(cables) > 1:
        # вилучаємо два найкоротші кабелі
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        
        # об'єднуємо їх і додаємо новий кабель з їхньою сумарною довжиною назад до купи
        combined_length = shortest1 + shortest2
        total_cost += combined_length
        heapq.heappush(cables, combined_length)

    return total_cost

# Приклад використання:
cables = [8, 4, 6, 12]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)
