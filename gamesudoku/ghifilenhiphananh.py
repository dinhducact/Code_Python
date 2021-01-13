try:
    rf=open("C:/Users/DELL/OneDrive/Máy tính/cThaops3.png","rb")
    wf=open("C:/Users/DELL/OneDrive/Máy tính/ghifilecthao2.png","wb")
    buffersize=250000
    buff=rf.read(buffersize)
    i=0
    while(len(buff)):
        i+=1
        wf.write(buff)
        print(i, "  {} byte".format(len(buff))) 
        buff=rf.read(buffersize)
finally:
    rf.close()
    wf.close()
"""đọc file thông thường có thể dùng with mặc định sẽ đóng luôn file """
with open ("C:/Users/DELL/OneDrive/Máy tính/cThaops3.png","r",encoding= 'utf-8') as f :
    pass