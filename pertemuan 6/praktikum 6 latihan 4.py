# =======================================
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# =======================================

'''def merge_sort(data):
    if len(data) <= 1:
       return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

'''

'''
1. Apa yang dimaksud dengan base case?
Base case adalah kondisi berhenti dalam rekursi.
Pada kode di atas, base case adalah:
if len(data) <= 1:
    return data

2. Mengapa fungsi memanggil dirinya sendiri?
Karena merge_sort menggunakan rekursi dengan konsep Divide and Conquer.

3. Apa tujuan fungsi merge()?
Menggabungkan dua list yang sudah terurut menjadi satu list yang tetap terurut.
'''