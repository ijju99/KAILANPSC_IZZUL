jenis_komponen = ("MPPF FORM","CONTROL HORN","PUSH ROD WIRE","BRUSHLESS MOTOR","LINKAGE STOPPER","ESC(SW50A)","RECEIVER(LA108 RX)","CARBON FIBER ROD 3 MM","SERVO 9 G","R1 LIPO PATTERY","PROPELLER","FLYSKY-16X REMOTE CONTROL")
harga_komponen = (23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,16)
jumlah =(0,1,2,3,4,5,6,7,8,9,10,11)

print("HARGA KOMPONEN MPFF FORM=RM23,CONTROL HORN=RM3,PUSH ROD WIRE=RM2,BRUSHLESS MOTOR=RM15.79,LINKAGE STOPPER=RM12,ESC(SW50A)=RM67,RECEIVER(LA108 RX)=RM61","CARBON FIBER ROD 3MM=RM25.30","SERVO 9 G=RM5.20","R1 LIPO PATTERY=RM57.56,PROPELLER=RM5.50,FLYSKY-16X REMOTE CONTROL=RM16")
a=int(input("Masukkan tempahan untuk MPPF FORM:"))
b=int(input("Masukkan tempahan untuk CONTROL HORN:"))
c=int(input("Masukkan tempahan untuk PUSH ROD WIRE:"))
d=int(input("Masukkan tempahan untuk BRUSHLESS MOTOR:"))
e=int(input("Masukkan tempahan untuk LINKAGE STOPPER:"))
f=int(input("Masukkan tempahan untuk ESC(SW50A):"))
g=int(input("Masukkan tempahan untuk RECEIVER(LA108 RX):"))
h=int(input("Masukkan tempahan untuk CARBON FIBER ROD 3MM:"))
i=int(input("Masukkan tempahan untuk SERVO 9 G:"))
j=int(input("Masukkan tempahan untuk R1 LIPO PATTERY:"))
k=int(input("Masukkan tempahan untuk PROPELLER:"))
l=int(input("Masukkan tempahan untuk FLYSKY-16X REMOTE CONTROL:"))

tempahan =(a,b,c,d,e,f,g,h,i,j,k,l)

def jumlah_harga():
    for i in range(4):
        jumlah[i] =  harga_komponen[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"komponen",jenis_komponen(0))
    print(b,"komponen",jenis_komponen(1))
    print(c,"komponen",jenis_komponen(2))
    print(d,"komponen",jenis_komponen(3))
    print(e,"komponen",jenis_komponen(4))
    print(f,"komponen",jenis_komponen(5))
    print(g,"komponen",jenis_komponen(6))
    print(h,"komponen",jenis_komponen(7))
    print(i,"komponen",jenis_komponen(8))
    print(j,"komponen",jenis_komponen(9))
    print(k,"komponen",jenis_komponen(10))
    print(l,"komponen",jenis_komponen(11))

    print("\nJumlah untuk harga tempahan ialah RM",sum(jumlah))
jumlah_harga()
cetak()