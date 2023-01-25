import numpy as np

def random_predict(number:int = np.random.randint(1, 1001)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-1000.

    Returns:
        int: Число попыток
    """
    count = 0 
    lower = 1 #Нижняя граница диапазона
    upper = 1001 #Верхняя граница диапазона
    print("загаданное число ", number)
    while True:
        count += 1
        predict_number = int((lower+upper)/2) #Делим диапазон пополам
        if number == predict_number:
            break #Выход из цикла
        elif predict_number<number:
            lower = predict_number
        else:
          upper = predict_number
    return count    
print(f'Количество попыток:', random_predict())