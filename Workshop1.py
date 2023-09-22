#1. จงเขียนโปรแกรมPython ค านวณหาราคาขายสินค้า โดยรับชื อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์ 
#แล้วคำนวณหาราคาขายของสินค้า โดยราคาขายสินค้าจะคิดเพิ มจากราคาสินค้า (ต้นทุน) ร้อยละ 10 
#สูตร ราคาขายสินค้า  =  ราคาสินค้า(ต้นทุน)  + (ราคาสินค้า(ต้นทุน) * 10 / 100)

#1.รับค่าข้อมูลของสินค้า 2.คำนวณหาราคาขายของสินค้า 3.แสดงชื่อโปรแกรม 4.แสดงผลราคาขายสิค้า

def showProgramName () :
    print('**--โปรแกรมคำรวณราคาขายสินค้า--**')

def showSellprice(name,price,sellprice ) :
    print(f'ชื่อของสินค้าคือ {name} ราคาต้นทุน {price:.2f} บาท ราคาขาย {Sellprice:.2f} บาท ')


def inputData( ) :
    name = input('โปรดป้อนชื่อของสินค้า : ')

    price = float(input('โปรดป้อนราคา(ต้นทุน)ของสินค้า : '))
    return name,price
def calSellprice (price ) :
    Sellprice = price + (price*10/100)    
    return  Sellprice
print('---------------------------')
showProgramName( )
print('---------------------------')
name,price = inputData( )
print('---------------------------')
Sellprice=calSellprice( price)
showSellprice (name,price,Sellprice)
print('---------------------------')