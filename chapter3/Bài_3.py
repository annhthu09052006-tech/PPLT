# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(so_nguyen):
    # Số nhỏ hơn 2 không phải số nguyên tố
    if so_nguyen < 2:
        return False

    # Kiểm tra từ 2 đến n-1
    for uoc in range(2, so_nguyen):
        if so_nguyen % uoc == 0:
            return False

    return True


# In các số nguyên tố từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100:")
for gia_tri in range(1, 101):
    if la_so_nguyen_to(gia_tri):
        print(gia_tri, end=" ")