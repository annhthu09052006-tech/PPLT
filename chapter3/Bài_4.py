# Hàm tìm giá trị lớn nhất
def tim_gia_tri_lon_nhat(danh_sach_so):
    gia_tri_lon_nhat = danh_sach_so[0]

    for phan_tu in danh_sach_so:
        if phan_tu > gia_tri_lon_nhat:
            gia_tri_lon_nhat = phan_tu

    return gia_tri_lon_nhat


# Hàm tìm giá trị nhỏ nhất
def tim_gia_tri_nho_nhat(danh_sach_so):
    gia_tri_nho_nhat = danh_sach_so[0]

    for phan_tu in danh_sach_so:
        if phan_tu < gia_tri_nho_nhat:
            gia_tri_nho_nhat = phan_tu

    return gia_tri_nho_nhat


# Danh sách điểm mẫu
danh_sach_diem = [6.5, 8.0, 4.5, 9.5, 7.0]

print("Giá trị lớn nhất:", tim_gia_tri_lon_nhat(danh_sach_diem))
print("Giá trị nhỏ nhất:", tim_gia_tri_nho_nhat(danh_sach_diem))
