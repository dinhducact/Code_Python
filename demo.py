# number= int(input("nhap vao so nguyen:"))
# if number<2:
#     print("so phải nhập lớn hơn 2")
#     exit()

# kiemtra = True
# for i in range(2,int(number /2 )+1):
#     if number %i==0:
#         kiemtra = False
#         break
# if kiemtra:
#     print("so " , number,"là số nguyên tố ")
# else:
#     print("so " , number," không là số nguyên tố ")
# a="hello"
# for i in range(0,len(a)):
#     print(a[i])
# number=str(input("nhập vào chuỗi: "))
# for i in range(0,len(number)):
#     print(number[i])
# hello = """ help \n mình là đình đức"""
# print(hello)
# ten=input(str("Nhập Họ và Tên :"))
# for i in range(0,len(ten)):
#     if ten[i]=='c':
#         print(i)
#     else:
#         continue
# A = [[1, 4, 5, 12], 
#  [-5, 8, 9, 0],
#  [-6, 7, 11, 19]]
# print("A =", A) 
# print("A[1] =", A[1]) # Hàng thứ 2 của ma trân
# print("A[1][2] =", A[1][2]) # Phần tử thứ 3 của hàng thứ 2
# print("A[0][-1] =", A[0][-1]) # Phần tử cuối cùng của hàng 1
# column = []; 
# for row in A:#truy cập tới từng phần thử trong mảng A
#  column.append(row[2]) #append chắm thêm các phần thử trong mảng con row của mảng A
#  print(row[2])
# print("Cột thứ 3 =", column)
# import numpy as np 
# mt=np.array([5,4,3])
# print(mt)
# print(type(mt))
# mtint=np.array([[5,6],[1,2],[7,8]])
# mtfloat=np.array([[1.2,2.1,3.1,1.3],[1.2,2.1,3.1,1.3]])
# print(mtint)
# print(mtfloat)
# A = np.array([[3, 6, 7], [5, -3, 0]])
# B = np.array([[1, 1], [2, 1], [3, -3]])
# C = A.dot(B)
# print(C)
# nhap = input(str("nhập họ và tên "))
# print(nhap)
# nhap1 = str(input("nhập họ và tên "))
# print(nhap1)
# nhap2 = int(input("nhập số tự nhiên "))
# print(nhap2)
# nhap3=input(int("nhập số tự nhiên"))
# print(nhap3)
# bai13=[1,2,4]
# print(bai13.count(2))# đếm
# print(bai13.index(4))#tìm vị trí
# bai13a=bai13.copy()
# bai13a[1]='đình đức'
# print(bai13)
# print(bai13a)
# #thêm phần tử
# print(bai13)
# bai13.append([1,0])
# print(bai13)
# bai13.extend([1,2])
# print(bai13)
# a=list('dinhduc')
# print(a)
# b=tuple('dinhduc')
# print(b)
# ket_qua=int(input("Nam nhập kết quả"))
# dap_an=43
# if dap_an==ket_qua:
#     print("Hạnh rất giỏi")
# else:
#     print("thế đáp án là gì ?"

ten=input(str("Nhập Họ Và Tên :"))
ngaysing=input(str("Nhập ngày sinh  :"))
truong=input(str("Nhập Trường :"))
#có thể căn lền phải
doi='Thông Tin Sinh Viên  %20s'%(ten)
print(doi)

ten1=f'Họ Và Tên  :{ten} \nNgày Sinh :{ngaysing} \nTheo học tại :{truong}'
print(ten1)

#dùng format có thể đánh số thứ tự trong {}, căn lề :<>^n   trái , phải , giữa
ten2='Họ Và Tên  :{:>50} \nNgày Sinh :{:>50} \nTheo học tại :{:}'.format(ten,ngaysing,truong)
print(ten2)