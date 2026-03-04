# =======================================
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# =======================================
# merge sort ascending
# =======================================

def merge_sort(data):

    if len(data) <= 1:
        return data

    # membagi datta jadi 2 bagian
    mid = len(data) // 2
    left = data[:mid]  # slicing
    right = data[mid:]

    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result


angka = [13, 7, 28, 5, 19, 36, 4]
print("hasil sorting: ", merge_sort(angka))
