# =======================================
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# =======================================

'''
1. Lengkapi kondisi agar menjadi ascending.
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
    
2. Jelaskan fungsi result.extend().
Menambahkan semua sisa elemen dari list left dam right mulai dari index i dan j ke dalam result.
'''
