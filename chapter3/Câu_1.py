# Nhập số km khách đã đi
so_km = float(input("Nhập số km đã đi: "))

# Khởi tạo biến tiền cước
tien_cuoc = 0

# Tính tiền theo từng mức
if so_km <= 1:
    tien_cuoc = 15000
elif so_km <= 20:
    tien_cuoc = 15000 + (so_km - 1) * 12000
else:
    tien_cuoc = 15000 + 19 * 12000 + (so_km - 20) * 10000

# In kết quả
print("Số tiền phải trả:", tien_cuoc, "VND")