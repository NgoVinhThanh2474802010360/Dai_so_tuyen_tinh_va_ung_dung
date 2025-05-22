print("BÀI TẬP CHƯƠNG 1")
print("Bài tập 1: Giải phương trình với Sympy" )
from sympy import Symbol, solve

x = Symbol('x')

# Ví dụ 1: x + 3 - 5 = 0 -> x - 2 = 0
bieuthuc = x + 3 - 5
print(solve(bieuthuc))
# Kết quả: [2]

# Ví dụ 2: x**2 + 3 - 5 = 0 -> x**2 - 2 = 0
bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print(nghiemx)
# Kết quả: [-sqrt(2), sqrt(2)] (hoặc dạng tương tự)

print(nghiemx[0])
# Kết quả: -sqrt(2)

print(nghiemx[1])
# Kết quả: sqrt(2)


print(" Bài tập 2: Giải phương trình bậc 2" )
from sympy import Symbol, solve

x = Symbol('x')

# Bài 1: phương trình x^2 + 9x + 8 = 0
ptb2_1 = x**2 + 9*x + 8
nghiem1 = solve(ptb2_1, dict=True)
print(nghiem1)
# Kết quả sẽ là: [{x: -1}, {x: -8}]

# Bài 2: phương trình x^2 + x + 10 = 0 (có nghiệm phức)
ptb2_2 = x**2 + 1*x + 10
nghiem2 = solve(ptb2_2, dict=True)
print(nghiem2)
# Kết quả sẽ là: [{x: -1/2 - 3*I/2}, {x: -1/2 + 3*I/2}]


print("Bài tập 3: Giải phương trình 1 biến biểu diễn đại số các biến còn lại")
from sympy import Symbol, solve, sqrt

# Định nghĩa các biến symbol
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

# Phương trình bậc 2 tổng quát: a*x^2 + b*x + c = 0
ptb2 = a*x**2 + b*x + c

# Giải phương trình theo biến x, kết quả trả về dưới dạng dict
nghiem = solve(ptb2, x, dict=True)

print(nghiem)

print("Bài tập 4: Giải hệ phương trình ")
from sympy import Symbol, solve

# Khai báo các biến
x = Symbol('x')
y = Symbol('y')

# Định nghĩa phương trình
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

# Giải hệ phương trình
nghiem = solve((pt1, pt2), dict=True)
print(nghiem)
# Kết quả: [{x: 3, y: 2}]

# Kiểm tra nghiệm bằng cách thay vào từng phương trình
nghiem0 = nghiem[0]
print(pt1.subs({x: nghiem0[x], y: nghiem0[y]}))  # Kết quả: 0
print(pt2.subs({x: nghiem0[x], y: nghiem0[y]}))  # Kết quả: 0


print("Bài tập 5: Thể hiện ma trận bằng numpy")
import numpy as np

# Khai báo ma trận 2x2
M1 = np.array([[9, 12],
               [23, 30]])
print(M1)

# Khai báo vector cột (dạng 1 chiều)
u = np.array([2, 1])

# Tích ma trận M1 nhân với vector u
tichM1u = M1.dot(u)
print(tichM1u)

# Giải thích: M1.dot(u) thực hiện phép nhân ma trận 2x2 với vector 2x1 -> ra vector 2x1

# Tích vector u nhân với ma trận M1
tichuM1 = u.dot(M1)
print(tichuM1)

# Giải thích: u.dot(M1) thực hiện phép nhân vector 1x2 với ma trận 2x2 -> ra vector 1x2

print("Sinh viên thực hành và cho biết kết quả các lệnh sau: ")
import numpy as np

# Lệnh 1
mat1 = np.zeros([5, 5])
print("mat1 =\n", mat1)
# mat1 là ma trận 5x5 toàn số 0

# Lệnh 2
mat2 = np.ones([5, 5])
print("mat2 =\n", mat2)
# mat2 là ma trận 5x5 toàn số 1

# Lệnh 3
mat3 = mat1 + 2 * mat2
print("mat3 =\n", mat3)
# mat3 = ma trận toàn số 2 (vì mat1 = 0, mat2 = 1, nên 0 + 2*1 = 2)

# Lệnh 4
mat4 = mat3
mat3[3][2] = 10
print("mat3 =\n", mat3)
print("mat4 =\n", mat4)
# mat3 thay đổi thì mat4 cũng thay đổi theo vì mat4 chỉ là tham chiếu (alias) của mat3

# Lệnh 5
mat5 = np.copy(mat3)
mat3[3][2] = 10
print("mat3 =\n", mat3)
print("mat4 =\n", mat4)
print("mat5 =\n", mat5)
# mat4 vẫn thay đổi khi mat3 thay đổi (vì alias),
# mat5 không thay đổi vì đây là bản sao độc lập của mat3 lúc tạo

# Lệnh 6
mat6 = np.empty([4, 5])
print("mat6 =\n", mat6)
# mat6 là ma trận 4x5, chứa các giá trị rác (không được khởi tạo rõ)

# Lệnh 7
mat7 = np.identity(4)
print("mat7 =\n", mat7)
# mat7 là ma trận đơn vị kích thước 4x4

# Lệnh 8
try:
    mat8 = np.rand([4,5])  # Lệnh này sẽ lỗi vì numpy không có hàm rand()
except AttributeError:
    mat8 = np.random.random([4,5])
print("mat8 =\n", mat8)
# mat8 là ma trận 4x5 với các số ngẫu nhiên trong khoảng [0,1)


print("Bài tập 6: Tìm chỗ đóng quân")

import numpy as np

# Bảng điểm cho từng nguy cơ theo cấp độ (index cấp độ): Không(0), Thấp(1), Trung bình(2), Cao(3), Rất cao(4)
diem_chay_rung =    np.array([0, 1, 2, 3, 5])
diem_lu_quet =       np.array([0, 1, 2, 4, 8])
diem_sat_lo_nui =    np.array([0, 1, 3, 5, 9])
diem_benh_dich =     np.array([0, 1, 3, 5, 7])
diem_lo_bi_mat =     np.array([0, 5, 10, 15, 20])

# Ma trận cấp độ (4x5) từng loại nguy cơ, theo đề bài:
A_chay_rung = np.array([
    [0, 1, 1, 3, 1],
    [0, 0, 1, 0, 1],
    [1, 5, 2, 2, 0],
    [0, 1, 2, 1, 2]
])

B_lu_quet = np.array([
    [1, 1, 2, 2, 2],
    [2, 1, 2, 0, 0],
    [1, 4, 2, 4, 2],
    [1, 2, 2, 2, 2]
])

C_sat_lo = np.array([
    [0, 5, 0, 1, 1],
    [1, 1, 1, 1, 3],
    [1, 3, 0, 1, 3],
    [3, 3, 0, 2, 2]
])

D_benh_dich = np.array([
    [1, 3, 1, 5, 0],
    [1, 0, 3, 7, 7],
    [0, 5, 0, 3, 0],
    [5, 0, 0, 2, 2]
])

E_lo_bi_mat = np.array([
    [0, 0, 0, 0, 0],
    [10, 0, 15, 0, 0],
    [0, 20, 15, 5, 0],
    [5, 0, 0, 2, 0]
])

# Chuẩn hóa cấp độ: giới hạn max cấp độ là 4
def chuan_hoa_cap_do(ma_tran):
    return np.where(ma_tran > 4, 4, ma_tran)

A_chay_rung = chuan_hoa_cap_do(A_chay_rung)
B_lu_quet = chuan_hoa_cap_do(B_lu_quet)
C_sat_lo = chuan_hoa_cap_do(C_sat_lo)
D_benh_dich = chuan_hoa_cap_do(D_benh_dich)
E_lo_bi_mat = chuan_hoa_cap_do(E_lo_bi_mat)

# Hàm chuyển cấp độ sang điểm theo bảng điểm
def chuyen_cap_do_sang_diem(cap_do_ma_tran, bang_diem):
    return bang_diem[cap_do_ma_tran]

# Tính điểm nguy cơ từng loại
diemA = chuyen_cap_do_sang_diem(A_chay_rung, diem_chay_rung)
diemB = chuyen_cap_do_sang_diem(B_lu_quet, diem_lu_quet)
diemC = chuyen_cap_do_sang_diem(C_sat_lo, diem_sat_lo_nui)
diemD = chuyen_cap_do_sang_diem(D_benh_dich, diem_benh_dich)
diemE = chuyen_cap_do_sang_diem(E_lo_bi_mat, diem_lo_bi_mat)

# Ngưỡng an toàn
nguong_an_toan = 5

# a. An toàn chiến dịch ngắn hạn 1-2 ngày (chỉ xét lộ bí mật)
tong_diem_a = diemE
an_toan_a = tong_diem_a <= nguong_an_toan
print("An toàn chiến dịch ngắn hạn (1-2 ngày):\n", an_toan_a)

# b. An toàn tập luyện thời bình (không xét lộ bí mật và bệnh dịch)
tong_diem_b = diemA + diemB + diemC
an_toan_b = tong_diem_b <= nguong_an_toan
print("An toàn tập luyện thời bình:\n", an_toan_b)

# c. An toàn theo mùa khô (có cháy rừng và bệnh dịch, không có lũ và sạt lở)
tong_diem_c = diemA + diemD
an_toan_c = tong_diem_c <= nguong_an_toan
print("An toàn mùa khô:\n", an_toan_c)

# d. An toàn mùa mưa (có lũ, sạt lở, bệnh dịch, không có cháy rừng)
tong_diem_d = diemB + diemC + diemD
an_toan_d = tong_diem_d <= nguong_an_toan
print("An toàn mùa mưa:\n", an_toan_d)

# e. An toàn trong 8 tháng (có đủ các mùa và yếu tố tránh lộ bí mật)
tong_diem_e = diemA + diemB + diemC + diemD + diemE
an_toan_e = tong_diem_e <= nguong_an_toan
print("An toàn trong 8 tháng:\n", an_toan_e)
