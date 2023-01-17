# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
def encode(s):

    encoding = "" # сохраняет выходную строку

    i = 0
    while i < len(s):
        count = 1

    while i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
        i += 1

# добавляет к результату текущий символ и его количество
    encoding += str(count) + s[i]
    i += 1

    return encoding


    if __name__ == '__main__':

        s = 'ABBCCCD'
print(encode(s))