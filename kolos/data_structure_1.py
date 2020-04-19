# Zaprojektuj strukturę danych przechowującą liczby naturalne, udostępniającą następujący Interfejs:
# insert(num) - umieszcza w strukturze liczbę naturalną.
# delete(num) - usuwa ze struktury liczbę
# find(num) - sprawdza czy liczba jest w strukturze.
# getRandom() - zwraca losową liczbę ze struktury. Do tej funkcji możesz wykorzystać funkcję randInt(N), która
# w czasie O(1) zwraca losową liczbę naturalną z zakresu od 0 do N-1.
# Wszystkie powyższe funkcje powinny działać w czasie O(1) zawsze!!!
import random


class RandomHashSet():
    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val):
        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1

    def find(self, val):
        return val in self.dict

    def __delete__(self, val):
        index = self.dict[val]
        last = self.arr[len(self.arr) - 1]
        self.arr[index] = last
        del self.dict[val]
        self.arr.pop()

    def get_random(self):
        return self.arr[random.randint(len(self.arr))]
