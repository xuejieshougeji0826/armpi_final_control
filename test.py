 
import serial  
import time  
# 打开串口  
ser = serial.Serial('/dev/ttyAMA0', 115200)  


if ser.isOpen == False:
    ser.open()
    print("chuankouyidakai")# 打开串口
ag=1500;bg=1500;cg=1400;dg=1500;runningtime=2000;
single=str("{G0000#001P"+str(ag)+"T"+str(runningtime)+"!#002P"+str(bg)+str(runningtime)
                   +"!#003P"+str(cg)+str(runningtime)+"!#004P"+str(dg)+str(runningtime)+"!}")
ser.write(single.encode())
print(single)

ser.write("{G0000#001P1500T2000!#002P1500T2000!#003P1500T2000!#004P1500T2000!}".encode())
time.sleep(3)
ser.write("{G0000#001P1263T2000!#002P1582T2000!#003P1040T2000!#004P0715T2000!}".encode())
#ser.write(b"{G0000#006P1800T1000!}")
