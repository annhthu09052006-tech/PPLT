# Hàm thêm liên hệ
def add_contact(danh_ba):
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    contact = ten + " - " + sdt
    danh_ba.append(contact)
    print("Đã thêm liên hệ thành công!")

# Hàm hiển thị danh bạ
def show_contacts(danh_ba):
    if len(danh_ba) == 0:
        print("Chưa có liên hệ nào.")
    else:
        print("Danh bạ:")
        for i in range(len(danh_ba)):
            print(f"{i+1}. {danh_ba[i]}")

# Hàm tìm kiếm
def search_contact(danh_ba):
    ten_can_tim = input("Nhập tên cần tìm: ")
    found = False
    for contact in danh_ba:
        if ten_can_tim.lower() in contact.lower():
            print("Tìm thấy:", contact)
            found = True
    if not found:
        print("Không tìm thấy.")

# Hàm main
def main():
    danh_ba = []

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ DANH BẠ ===")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị danh bạ")
        print("3. Tìm kiếm liên hệ")
        print("4. Thoát")

        choice = input("Nhập lựa chọn (1-4): ")

        if choice == "1":
            add_contact(danh_ba)
        elif choice == "2":
            show_contacts(danh_ba)
        elif choice == "3":
            search_contact(danh_ba)
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình
main()