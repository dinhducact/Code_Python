# demo ="          vũ đình đức"
# print(demo)
# demo1=demo.strip()
# print(demo1)
# for i in demo1:
#     print(i)
# print(end='Mời bạn nhập 1 số:')
# a=input()
# print("số bạn vừa nhập = ",a)
 
# print('Mời bạn nhập 1 số',end=':')
# b=input()
# print('số bạn vừa nhập =',b)
# print('*'*20)
# a=input('nhap thông tin chuỗi a :')
# print(a    ,end=' kiểu của a là :')
# print(type(a))
# b=int(input('nhập thông tin số b :'))
# print('số vừa nhập ',b,end =("        kiểu của b là "))
# print(type(b))
# cắt số phần tử của chuỗi [khởi đầu : kết thúc -1: bước nhảy nếu có ]
# stra='vudinhduc'
# strb=stra[0:5]
# print(strb)
# strc=stra[None:5]
# print(strc)
# #lấy theo bước nhảy
# strd=stra[None:None:2]
# print(strd)
# #thay đổi kí tự chuỗi vd thay đổi phần tử thứ 1 
# stre=stra[None:1]+'U'+stra[2:None]
# print(stre)
#có thể căn lền 
# ten=input(str("Nhập Họ Và Tên :"))
# ngaysing=input(str("Nhập ngày sinh  :"))
# truong=input(str("Nhập Trường :"))
# doi='Thông Tin Sinh Viên  %20s'%(ten)
# print(doi)
# print('\n')
# ten1=f'Họ Và Tên  :{ten} \nNgày Sinh :{ngaysing} \nTheo học tại :{truong}'
# print(ten1)
# print('\n')
# #dùng format có thể đánh số thứ tự trong {}, căn lề :<>^n   trái , phải , giữa
# ten2='Họ Và Tên  :{:>50} \nNgày Sinh :{:>50} \nTheo học tại :{:>50}'.format(ten,ngaysing,truong)
# print(ten2)
# bai12=int(input("Nhập số phần tử của mảng :"))
# # khởi tạo mảng bai12a với bai12 giá trị , khởi tạo i , i trong phạm vi từ 0 đến bai12 thì sẽ có từ 0 đến bai12-1 giá trị
# bai12a=[i for i in range(0,bai12)]
# for i in range(0,bai12):
#     bai12a[i]=input(str("nhập thông tin :" ))
# for i in range(0,bai12):
#     print("phần tử thứ %d của mảng :"%(i)+bai12a[i])
# else:
#     print('da het')
# print(bai12a)
# rm = int(input('nhập phần tử muốn loại bỏ '))
# bai12a.remove(bai12a[rm])
# print(bai12a)
# bai12b=[[n,n*2,n*3] for n in range(0,bai12)]
# for i in range(0,bai12):
#     print()
#     print(bai12b[i])
#     for j in range(0,3):
#         print(bai12b[i][j] ,end ='   ')
# print()
# import array as arr
# a=arr.array('i',[1,2,2,3,4,54])
# print(a[2:4])
# bai16={value for value in range(8)}
# print(bai16)
# print(type(bai16))
# bai16_1=set((1,2,5,4,66,4,4,58,9,8,5,3,568,6,546,3))# có thể đưa vào một tuple nhưng khi đưa ra giá trị là set
# print(bai16_1)
# bai16_2=set('my nam is duc')
# print(bai16_2)
# print(4 in bai16_1)
# dic ={'nam':'dinhduc','number':22}
# print(dic)
# print(type(dic))
# #cách khởi tạo 2
# dic_1=dict(nam='dinhduc', number=22 )
# print(dic_1)
# print(type(dic_1))
# #cách khởi tạo 3
# key_2=('nam','number')
# dic_2=dict.fromkeys(key_2,'value default')
# print(dic_2)
# print(type(dic_2))
# #lấy giá trị từ dict
# print(dic_1['nam'])
# #thay đổi giá trị , thêm giá trị nếu chưa có 
# dic['nam']='vu dinh duc'
# dic['truong']='hoc vien ky thuat mat ma'
# print(dic)
# print(dic['nam'])
# #thêm giá trị thủ công 
# dic['nam']=dic['nam']+'----Vũ Đình Đức'
# print(dic)
# #bài18 các phương thức xử lý trong dict(dictionary = thư viện)
# dic_3=dic.copy()
# print(dic_3)
# dic_3.clear()
# print(dic_3)
# #phương thức get lấy ra value nếu ko có kye trả về noen hoặc một giá trị đặt sẵn
# value=dic.get('nam')
# print(value)
# value_1=dic.get('adsjdfsd','không có value phù hợp với key này')
# print(value_1)
# #phương thức keys lấy ra tất cả các keys có trong dict (danh sách keys)
# key_3=dic.keys()
# print(key_3)
# #phương thức values lấy ra tất cả các values có trong dict (danh sách values)
# value_2=dic.values()
# print(value_2)
# #phương thức items trả ra giá trị dưới dạng tuple với giá trị thứ nhất là ky giá trị thứ hai là value 
# value_3=dic.items()
# print(value_3)
# #để lấy giá trị với hàm items thì phải chuyển về list rồi lấy giá trị như list
# value_4=list(dic.items())
# print(value_4[0][1])
# #phương thức pop giống get nhưng pop sẽ loại bỏ cặp key - value trong dict
# value_5=dic.pop('number')
# print(value_5)
# print(dic)
# value_6=dic.pop('khonco','không có value phù hợp với key')
# print(value_6)
# #dic.popitem pop ra một cặp key value bất kỳ trong dict đồng thời loại bảo khỏi dict
# #phương thức setdefault trả ra value của key nếu ko có key đồng thời tự động thêm cặp key-value vào dict
# value_7=dic.setdefault('nam')
# print(value_7)
# value_8=dic.setdefault('class','AT15A')
# print(value_8)
# print(dic)
# #update của dic 
# dic.update(nam='Vũ Đình Đức',age =20)
# print(dic)

# a ='vu dinh duc'
# print(a)
# print(type(a))
# print(id(a))
# import pygame 
# ''' không được đặt tên trùng với tên thư viện vì khi run time thì compiler sẽ tìm tới tên chương trình chạy chứ 
# không tìm đến tên thư viện , hoặc trong cùng một package '''
# pygame.init()
# screen = pygame.display.set_mode((600,600))
# GREY=(150,150,150)
# WHITE=(255,255,255)
# running=True
# while running:
#     screen.fill(GREY)
#     pygame.draw.rect(screen,WHITE,(50,50,500,500))
#     for event in pygame.event.get():

#         if event.type==pygame.QUIT:
#             running=False
       
#     pygame.display.flip()
    
# pygame.quit()
# x=range(11,22,2)
# print(type(x))
# print(x)
# print(list(x))
# bai12=int(input("Nhập số phần tử của mảng :"))
# bai12a=[i for i in range(0,bai12)]
# for i in range(0,bai12):
#     bai12a[i]=input(str("nhập thông tin :"))
# print(bai12a)
# """tạo một hàm mới trong python"""
# from typing import type_check_only


# def xuat():
#     print('hello world')
# """gọi hàm xuat ()  """
# xuat()
# def so4(a) :
#     return a

# so=so4(7)
# print(so)
# print('ket qua la',so4(9))
# """sử dụng đưa vào nhiều giá trị dùng với * """
# def tong(*x):
#     tong=0
#     for item in x:
#         tong =tong+item
#     return tong
# tonggt=tong(5,5,5,5,5,5,5)
# print(tonggt)
# def tong2(*data):
    
#     kq=[]
#     for item in data:
#         tong2a=0
#         for n in item:
#             tong2a=tong2a+n
#         kq.append(tong2a)
#     return kq
# tong2b=tong2([5,5,5,5],[6,6,6,6],[76,5])
# print(tong2b)



# def dienthoai(**data):
#     tong=0
#     for name,price in data.items():
#         row ="{:<20}{:<10}".format(name,price)
#         print(row)
#         tong+=price
#     return tong
# tongtien= dienthoai(iphone=30000, samsung=8888)
# print("-"*30)
# row="{:<20}{:<10}".format("tong tien",tongtien)
# print(row)

# def tongbai30 (n1, n2 , n3 , *data, ** dict):
#     t1=t2=t3=0
#     t1=n1+n2+n3
#     for i in data:
#         t2+=i
#     for k, v in dict.items():
#         t3+=v
#     t=[t1,t2,t3]
#     return t
# tong30= tongbai30(11,22,33,44,55,66,77,duc=22, vinh =28)
# print( tong30)
# tup = (i for i in range(100) if i %3 ==0 and i %2==0)
# #tuple ko giống list. demo không giống list
# print(tup)
# # thông qua một bước gán trung gian chứ ko thể dùng trực tiếp như list 
# bai14=tuple(tup)
# print(bai14)

# print( range(4))
# """ range không tực tiếp trả giá trị về , phải thông qua for để đưa ra giá trị """
# def myrange( start , lenght , step):
#     i=start
#     while(i<lenght):
#         print(i)
#         i+=step
# myrange(2,6,2)
# l=[1,2,3,4,5,3,2,4,2,43,33]
# print(len(l))
# i=iter(l)
# print(type(i))
# for k in range(len(l)):
#     # __next__ truy suất tới từng phần tử của list 
#     print(i.__next__())
# def generator_test():
#     listgener=[1,23,4,34,543,343,64]
#     # print(len(listgener))
#     i=iter(listgener)
#     for k in range(len(listgener)):
#         yield i.__next__()
# gener=tuple(generator_test())
# print(gener)

# gener2 =generator_test()
# for i in gener2:
#     print(i)


# # bài 1   tạo một hàm truyền vào tham số tùy ý , đếm xem có bao nhiêu chữ giống nhau , trả về dạng dict\
# def countchar(* data):
#     dic={}
#     for i in data:
#         for item in i:
#             item = item.upper()
#             if item in dic:
#                 dic[item]+=1
#             else :
#                 dic[item]=1
#     return dic
# countchar1=countchar("vu dinh duc ", "vu dinh vinh ","vu dinh kiem ")
# print(countchar1)
##bài 2 tạo hàm range
# def rangetest(*data):
#     start=lenght=step=0
#     if len(data)==3 :
#         start=data[0]
#         lenght=data[1]
#         step=data[2]
#     elif len(data)==2:
#         sstart=data[0]
#         lenght=data[1]
#         step=1
#     elif len(data)==1:
#         start=0
#         lenght=data[1]
#         step=data[2]
#     i=start 
#     while (i<lenght):
#         yield i
#         i+=step
# check=tuple(rangetest(5,45,3))
# print(check)
# class st :
#     def __init__(self,name):
#         print ("day là hàm koong có tham số ")
#         self.name=name
#     def show(self ):
#         print ("hello ",self.name)
# student=st("duc")
# student.show()
# class myClass(object):
#     def __init__(self):
#         self.x = 10
#         self .__y = 5  # khai báo thuộc tính riêng của lớp ( private) 
 
# class Class1(myClass):
#     def __init__(self):
#         super().__init__()
#         self.z = 20
 
# ob1 = Class1()
# print( ob1.x)
# print(ob1.__y) # thuộc tính riêng không thể truy cập tới 
# def sum(a, b):
#     return a / b
# try:
#     sum(6,0)
# except Exception :
#     print(" co loi xay ra ")
# try:
#     rf=open("C:/Users/DELL/OneDrive/Máy tính/cThaops3.png","rb")
#     wf=open("C:/Users/DELL/OneDrive/Máy tính/ghifilecthao2.png","wb")
#     buffersize=250000
#     buff=rf.read(buffersize)
#     i=0
#     while(len(buff)):
#         i+=1
#         wf.write(buff)
#         print(i, "  {} byte".format(len(buff))) 
#         buff=rf.read(buffersize)

# finally:
#     rf.close()
#     wf.close()
# from colorama import Fore,Back,Style
# import time
# import os
# from colorama import init,AnsiToWin32
# import sys
# stream= AnsiToWin32(sys.stderr).stream
# print(Fore.BLUE,'\n'.join(
# 		[' '.join(
# 		[
# 		(
# 		'duc'[(x-y) % len('duc')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
# 		else ' '
# 		)
# 		for x in range(-50, 30,1)
# 		]
# 		)
# 		for y in range(50, -30, -1)
# 		]
# 		)
# 	,file=stream)
# # time.sleep(5)
# # os.system("cls")
# import calendar
# print ("Thang hien tai la:")
# cal = calendar.month(2000, 6)
# print (cal)
# from colorama import Fore,init,ansitowin32
# print(Fore.RED,"toi ten duc")
# node_template = "System Info node {node_number} # Count: {issue_count} issues"\
#                 "=> {warning_count} warning; {major_count} marjor;"\
#                 "{cirtical_count} critical; {fatal_count} fatal;"
# print( node_template)
# print ( "vu dinh duc ", end="dddddddđ  ")
# print("aaaaaaaaaaaaa")
#1
# def xuat():
#     print('hello world')
# """gọi hàm xuat ()  """
# xuat()
# try:
#     a=100
#     b=10 
#     x=( a*b )+ (1000 *a )/(a/b)
#     print(x)
#     f=open("file.txt","r")
#     f.write("hihih")

# except Exception as aaa:
#     print(" lỗi  :", aaa)
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

