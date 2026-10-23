def faktorial(n):
    if n < 0:
        raise ValueError("Bilangan tidak boleh negatif")

    if n <= 1:
        return 1

    return n * faktorial(n - 1)


print("Hasilnya", faktorial(5))