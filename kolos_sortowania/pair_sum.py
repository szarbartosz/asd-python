# Dana jest tablica zawierająca liczby naturalne. Proszę zaimplementować funkcję odpowiadającą na pytanie czy
# w tablicy jest para sumująca się do jakiejś liczby x. Funkcja powinna być jak najszybsza.


def find_pair(arr, n):
    dictionary = set(arr)
    for i in range(len(arr)):
        if n - arr[i] in dictionary:
            return True


print(find_pair([1,2,3,4,5], 6))
