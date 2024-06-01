import DES
import str_work
print("Предложение:")
print(str_work.hex_string("ДВОРЯК"))
print("")
print("Ключ:")
print(str_work.hex_string("ДИАНА"))
print("-" * 128)
P = str_work.binary_string("ДВОРЯК")
print("Бинарный вид предложения:")
print(P)
P = "0" * (len(DES.STANDART_PERMUTATION) - len(P)) + P
print("Расширение предложения:")
print(P)
P = str_work.str_permutation(P, DES.STANDART_PERMUTATION)
print("Стандартная перестановка:")
print(P)
print("-" * 128)
print("Бинарный вид ключа:")
K = str_work.binary_string("ДИАНА")
print(K)
print("Расширение ключа:")
per = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
    ]
#K = "0" * (max(per) - len(K)) + K
K = "0" * (64 - len(K)) + K
print(K)
K = str_work.str_ex(K, per)
print("Стандартная изменение ключа:")
print(K)

