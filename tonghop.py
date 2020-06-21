demo=input(str("Nhập Họ Và Tên "))
#loại bỏ khoảng trắng ở đầu và cuối xâu 
demo1=demo.strip()
print(demo1)
demo2=demo1.lower()
print(demo2)
demo3=demo1.upper()
print(demo3)
demo4=demo1.split(" ")
print(demo4)
for i in demo4:
    print(i)
demo5=demo1.partition("d") #vách ngăn khi tìm chữ cái  d đầu tiên tách thành lis
print(demo5)
# lấy thư viện decimal ( thư viện lấy số giá trị phần nguyên và phần thập phân )
from decimal import*
#lấy phần nguyên và phần thập phân tới 30 giá trị 
getcontext().prec=30
d= Decimal(10)/Decimal(3)
print(d)
print(type(d))
#lấy thư viện fractions ( thư viện phân số  )
from fractions import*
frac= Fraction(6,7)
print(frac)
print(type(frac))
#số phức(complex)
c=complex(2,5)
print(c)
print(c.real)
print(c.imag)
# cắt số phần tử của chuỗi [khởi đầu : kết thúc -1: bước nhảy nếu có ]
stra='vudinhduc'
strb=stra[0:5]
print(strb)
strc=stra[None:5]
print(strc)
#lấy theo bước nhảy
strd=stra[None:None:2]
print(strd)
#thay đổi kí tự chuỗi vd thay đổi phần tử thứ 1 
stre=stra[None:1]+'U'+stra[2:None]
print(stre)
ten=input(str("Nhập Họ Và Tên :"))
ngaysing=input(str("Nhập ngày sinh  :"))
truong=input(str("Nhập Trường :"))
#có thể căn lền 
doi='Thông Tin Sinh Viên  %20s'%(ten)
print(doi)
print('\n')
ten1=f'Họ Và Tên  :{ten} \nNgày Sinh :{ngaysing} \nTheo học tại :{truong}'
print(ten1)
print('\n')
#dùng format có thể đánh số thứ tự trong {}, căn lề :<>^n   trái , phải , giữa
ten2='Họ Và Tên  :{:>50} \nNgày Sinh :{:>50} \nTheo học tại :{:>50}'.format(ten,ngaysing,truong)
print(ten2)

bai10='vũ đình đức'
bai10a=bai10.capitalize()#viết hoa chữ cái đầu tiền của chuỗi
bai10b=bai10.title()#viết hoa chữ cái đầu mỗi chữ
print(bai10)
print(bai10a)
print(bai10b)
#list trong python giống chuỗi , các phần thử cách nhau bởi dấu phẩy
bai12=int(input("Nhập số phần tử của mảng :"))
# khởi tạo mảng bai12a với bai12 giá trị , khởi tạo i , i trong phạm vi từ 0 đến bai12 thì sẽ có từ 0 đến bai12-1 giá trị
bai12a=[i for i in range(0,bai12)]
for i in range(0,bai12):
    bai12a[i]=input(str("nhập thông tin :"))
for i in range(0,bai12):
    print("phần tử thứ %d của mảng :"%(i)+bai12a[i])
#  có thể để một công thức trong mảng (list)
bai12b=[[n,n*2,n*3] for n in range(0,bai12)]
for i in range(0,bai12):
    print(bai12b[i])
    for j in range(0,3):
        print(bai12b[i][j])
# sử  dụng thư viện numpy để tính toán các bài toán liên quan ma trận 
import numpy as np 
mt=np.array([5,4,3])
print(mt)
print(type(mt))
mtint=np.array([[5,6],[1,2],[7,8]])
mtfloat=np.array([[1.2,2.1,3.1,1.3],[1.2,2.1,3.1,1.3]])
print(mtint)
print(mtfloat)
mt0=np.zeros((2,3))#tất cả ma trận đều là zeros=0 với 2 hàng 3 cột
mt1=np.ones((3,2))#tất cả ma trận đề là 1 với 3 hàng 2 cột
print(mt0)
print(mt1)
#tạo một ma trận có 4 giá trị từ 0 đến 3
A = np.arange(4)
print('A =', A)
#tạo một ma trận có 12 giá trị tính từ 0 , gồm 2 hàng 6 cột
B = np.arange(12).reshape(6, 2)
print('B =', B)
#ma trận tích 
mttich=mtint.dot(mtfloat)
print("ma trận tích qua hàm .dot=",mttich)
#xuất cột của ma trận 
print("cột thứ hai của ma trận int ",mtint[:,1])
#chuyển vị của một ma trận transpose=đảo
print("ma trận số nguyên")
print(mtint)
print("chuển vị của ma trận số nguyên")
print(mtint.transpose())
#lát cắt của mảng giống như lát cắt trong list
bai13=[1,2,4]
print(bai13.count(2))# đếm
print(bai13.index(4))#tìm vị trí
bai13a=bai13.copy()
bai13a[1]='đình đức'
print(bai13)
print(bai13a)
#thêm phần tử
print(bai13)
# thêm vào cuối mảng một mảng con [1,0]
bai13.append([1,0])
print(bai13)
# thêm vào cuối mảng 2 phần tử 1 ,2
bai13.extend([1,2])
print(bai13)
#chèn vào vị trí a kí tự b .insert(a,b)
bai13.insert(0,'vu đình đức')
print(bai13)
#lấy ra phần tử thứ k pop(k)
bai13b=bai13.pop(0)
print(bai13)
print(bai13b)
#sắp xếp sort
bai13c=[1,5,2,6,7]
bai13c.sort()
print(bai13c)
bai13c.sort(reverse=True)
print(bai13c)
"""Tuple trong Python
 được giới hạn bởi cặp ngoặc()
 các phần thử của tuple được phân cách bằng dấu ,
 tuple có khả năng chứa mọi giá trị 
 tốc độ truy suất tuple nhanh hơn list
 dung lượng chiếm trong bộ nhớ nhỏ hơn list
 bảo vệ giữ liệu sẽ không bị thay đổi 
 có thể dùng làm key của dictionary"""
tup = (i for i in range(100) if i %3 ==0 and i %2==0)
#tuple ko giống list. demo không giống list
print(tup)
# thông qua một bước gán trung gian chứ ko thể dùng trực tiếp như list 
bai14=tuple(tup)
print(bai14)
# tuple ko không cho phép bạn thay thế nội dung còn list thì có 
'''Set trong Python
được giới hạn bởi dấu {}
các phần tử của set được phân cách bằng dấu  , 
set không chứa nhiều hơn một phần tử trùng lặp 
set có thể chứa hashable object nhưng không phải là một hashable object
vì vậy set ko thể chứa một set'''
bai16={value for value in range(8)}
print(bai16)
print(type(bai16))
bai16_1=set((1,2,5,4,66,4,4,58,9,8,5,3,568,6,546,3))# có thể đưa vào một tuple nhưng khi đưa ra giá trị là set
print(bai16_1)
bai16_2=set('my nam is duc')
print(bai16_2)
print(4 in bai16_1)
print({1,2,23,4,5,6,3}-{3,4,5,6})
print({1,2,3,5} & {3 ,4,5}) # lấy phần thử thuộc cả 2 bên 
print({1,2,3,5} | {3 ,4,5}) #lấy hết các phần tử 2 bên có 
print({1,2,3,5} ^ {3 ,4,5}) #lấy hết các phần tử loại bỏ phần tử trùng
bai16_1.pop()# lấy ra phần tử đầu tiên , khác so với list có thể lấy phần tử bất kỳ 
print(bai16_1)
bai16_3={1,2,5,6,4,8,}
bai16_3.remove(5) #lấy phần tử có giá trị 5, nếu ko có phần tử đó sẽ báo lỗi 
print(bai16_3)
bai16_3.discard(55) #giống remove nhưng nếu không có phần tử đó không báo lỗi 
print(bai16_3)
'''Dict trong Python
được giới hạn bởi cặp dâu {}, các phần tử phân cách bởi dấu  ,
các phần tử của dict phải là một cặp key-value
cặp key - value được phân cách bởi dấu :
các key thuộc phải là hột hash object'''
dic ={'nam':'dinhduc','number':22}
print(dic)
print(type(dic))
#cách khởi tạo 2
dic_1=dict(nam='dinhduc', number=22 )
print(dic_1)
print(type(dic_1))
#cách khởi tạo 3
key_2=('nam','number')
dic_2=dict.fromkeys(key_2,'value default')
print(dic_2)
print(type(dic_2))
#lấy giá trị từ dict
print(dic_1['nam'])
#thay đổi giá trị , thêm giá trị nếu chưa có 
dic['nam']='vu dinh duc'
dic['truong']='hoc vien ky thuat mat ma'
print(dic)
print(dic['nam'])
#thêm giá trị thủ công 
dic['nam']=dic['nam']+'----Vũ Đình Đức'
print(dic)
#bài18 các phương thức xử lý trong dict(dictionary = thư viện)
dic_3=dic.copy()
print(dic_3)
dic_3.clear()
print(dic_3)
#phương thức get lấy ra value nếu ko có kye trả về noen hoặc một giá trị đặt sẵn
value=dic.get('nam')
print(value)
value_1=dic.get('adsjdfsd','không có value phù hợp với key này')
print(value_1)
#phương thức keys lấy ra tất cả các keys có trong dict (danh sách keys)
key_3=dic.keys()
print(key_3)
#phương thức values lấy ra tất cả các values có trong dict (danh sách values)
value_2=dic.values()
print(value_2)
#phương thức items trả ra giá trị dưới dạng tuple với giá trị thứ nhất là ky giá trị thứ hai là value 
value_3=dic.items()
print(value_3)
#để lấy giá trị với hàm items thì phải chuyển về list rồi lấy giá trị như list
value_4=list(dic.items())
print(value_4[0][1])
#phương thức pop giống get nhưng pop sẽ loại bỏ cặp key - value trong dict
value_5=dic.pop('number')
print(value_5)
print(dic)
value_6=dic.pop('khonco','không có value phù hợp với key')
print(value_6)
#dic.popitem pop ra một cặp key value bất kỳ trong dict đồng thời loại bảo khỏi dict
#phương thức setdefault trả ra value của key nếu ko có key đồng thời tự động thêm cặp key-value vào dict
value_7=dic.setdefault('nam')
print(value_7)
value_8=dic.setdefault('class','AT15A')
print(value_8)
print(dic)
#update của dic 
dic.update(nam='Vũ Đình Đức',age =20)
print(dic)
