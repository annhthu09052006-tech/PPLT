# Hàm cộng
def cong_hai_so(so_a, so_b):
    return so_a + so_b


# Hàm trừ
def tru_hai_so(so_a, so_b):
    return so_a - so_b


# Hàm nhân
def nhan_hai_so(so_a, so_b):
    return so_a * so_b


# Hàm chia (có kiểm tra chia cho 0)
def chia_hai_so(so_a, so_b):
    if so_b == 0:
        return "Lỗi: Không thể chia cho 0"
    return so_a / so_b


# Hiển thị menu
def hien_thi_menu():
    print("\n===== MENU =====")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")


# Chương trình chính
while True:
    hien_thi_menu()

    lua_chon = int(input("Nhập lựa chọn: "))

    # Thoát chương trình
    if lua_chon == 5:
        print("Kết thúc chương trình.")
        break

    # Nhập 2 số
    so_a = float(input("Nhập số a: "))
    so_b = float(input("Nhập số b: "))

    # Xử lý theo lựa chọn
    if lua_chon == 1:
        print("Kết quả:", cong_hai_so(so_a, so_b))
    elif lua_chon == 2:
        print("Kết quả:", tru_hai_so(so_a, so_b))
    elif lua_chon == 3:
        print("Kết quả:", nhan_hai_so(so_a, so_b))
    elif lua_chon == 4:
        print("Kết quả:", chia_hai_so(so_a, so_b))
    else:
        print("Lựa chọn không hợp lệ!")
