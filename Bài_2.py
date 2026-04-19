gi# Nhập số nguyên dương n
so_n = int(input("Nhập số nguyên dương n: "))

# Khởi tạo biến tổng
tong_tat_ca = 0
tong_so_chan = 0

# Duyệt từ 1 đến n
for gia_tri in range(1, so_n + 1):
    tong_tat_ca += gia_tri  # cộng dồn tổng

    # Kiểm tra số chẵn
    if gia_tri % 2 == 0:
        tong_so_chan += gia_tri

# In kết quả
print("Tổng từ 1 đến n:", tong_tat_ca)
print("Tổng các số chẵn:", tong_so_chan)