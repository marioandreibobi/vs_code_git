
matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

crestere = True

nume = {"ANA", "ION", "MARIA"}

# printăm numele
for i in nume:
    print(i)

# definim funcția Fibonacci la nivel global
def fib(n):
    """
    Construiește și scrie șirul lui Fibonacci până la n și întoarce lista ca rezultat
    I: n - limita superioară
    E: lista termenilor calculați
    """
    result = []
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        result.append(a)
        a, b = b, a + b
    print("<== gata")
    return result

print('Al doilea text')

# rulăm funcția doar dacă scriptul e executat direct
if __name__ == '__main__':
    a = fib(50)
    print('Lista generata:')
    print(a)