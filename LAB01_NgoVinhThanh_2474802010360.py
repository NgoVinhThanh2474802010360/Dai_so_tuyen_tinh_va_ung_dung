# 1.2.1. Các phép xử lý với danh sách 
danhsach1 = [1. , 3.]
danhsach2 = [5. , 7.]
danhsach = danhsach1 + danhsach2
# Kết quả: [1.0, 3.0, 5.0, 7.0]
print("1.2.1. CÁC PHÉP XỬ LÍ VỚI DANH SÁCH ")
print(danhsach)
danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)

tich = danhsach * 2
print(tich)

danhsach_chia2 = [x / 2 for x in danhsach]
print(danhsach_chia2)
 
#2.1. Định nghĩa Symbol và các phép toán hình thức (symbolic)
print("2.1 ĐỊNH NGHĨA SYMBOL VÀ CÁC PHÉP TOÁN HÌNH THỨC (SYMBOLIC)")
x = 1
x + x + x + 2 
from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)

from sympy import Symbol

# Tạo các biểu tượng
a = Symbol('Noi')
b = Symbol('Chim')

# Biểu thức đại số
bieuthuc = 3 * b + 7 * a
print("Biểu thức:", bieuthuc)

# Truy tên các biểu tượng
print("Tên của a là:", a.name)
print("Tên của b là:", b.name)

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print("Kết quả là: ",s)

p = x*(x+2*x)
print("Kết quả là: ",p ) 

from sympy import symbols

# Khai báo các biến
x, y = symbols('x y')

# Biểu thức ban đầu
p = (x + 2)*(y + 3)
print("Biểu thức p:", p)

# Biểu thức phức tạp hơn
p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
print("Biểu thức p mới:", p)

# Biểu thức đơn giản tự động
p = x * (-x + 2*x - x)
print("Biểu thức p đơn giản tự động:", p)

# Sử dụng expand() để triển khai
p = (x + 2)*(y + 3)
print("Triển khai p:", p.expand())


#2.2.1. Đặt nhân tử chung và khai triển biểu thức
print("2.2.1. ĐẶT NHÂN TỬ CHUNG VÀ KHAI TRIỂN BIỂU THỨC")
from sympy import symbols, factor, expand

# Khai báo biến
x, y = symbols('x y')

# Phân tích đa thức thành nhân tử
bieuthuc1 = x**3 - y**3
print("Phân tích x^3 - y^3:", factor(bieuthuc1))

# Khai triển biểu thức
bieuthuc2 = (x - y)*(x**2 + x*y + y**2)
print("Khai triển (x - y)(x^2 + x*y + y^2):", expand(bieuthuc2))


#2.2.3. Thay thế giá trị
print("THAY THẾ GIÁ TRỊ")
from sympy import Symbol

# Khai báo biến
x = Symbol('x')
y = Symbol('y')

# Tạo biểu thức
bieuthuc = x*x - x*y + y*y
print("Biểu thức:", bieuthuc)

# Thay thế x = 3, y = 2
giatri = bieuthuc.subs({x: 3, y: 2})
print("Giá trị khi x = 3, y = 2:", giatri)

# Kiểm tra giá trị ban đầu của x và y vẫn không đổi
print("Giá trị x sau khi thay:", x)
print("Giá trị y sau khi thay:", y)


# Thực hành: Sinh viên thực hành 3 tình huống sau:
print("THỰC HÀNH 3 TÌNH HUỐNG SAU") 
print("Tình huống 1: Xác định theo thứ tự x=3 và y = x")
giatri = bieuthuc.subs({x:3, y:x})
print(giatri)
print("Tình huống 2: Xác định theo thứ tự: x=y và y = 3" )
giatri = bieuthuc.subs({x:y, y:3})
print(giatri)
print("Tình huống 3: Xác định y=x và sau đó tính x = 3 ")
giatri = bieuthuc.subs({y:x}).subs({x:3})
print(giatri) 

from sympy import Symbol, simplify, sin, cos

# Khai báo biến
x = Symbol('x')
y = Symbol('y')

# Biểu thức ban đầu
bieuthuc = x*x - x*y + y*y
print("Biểu thức ban đầu:", bieuthuc)

# Thay x bằng (1 - y)
bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print("Biểu thức sau khi thay x = 1 - y:", bieuthuc_moi)

# Đơn giản hóa biểu thức
dongian = simplify(bieuthuc_moi)
print("Biểu thức đơn giản:", dongian)

# Biểu thức lượng giác
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print("Biểu thức lượng giác đơn giản:", bt_moi)

#3.1. Một số lệnh cơ bản numpy xử lý vector
print("3.1. MỘT SỐ LỆNH CƠ BẢN NUMPY XỬ LÝ VECTOR")
import numpy as np

vec1 = np.array([1., 3., 5.])
print(vec1 * 2)            
print(vec1 * vec1)        
print(vec1 / 2)          
print(vec1 + vec1)        

vec2 = np.array([2., 4., 6.])  
print(vec1 + vec2)        

vec3 = np.array([2., 4., 6.])
print(vec1 + vec3)        
print(vec1 / vec3)        
print(vec1 * vec3)        
print(2 * vec1 + 5 * vec3) 

