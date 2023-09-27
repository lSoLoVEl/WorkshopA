#2. จงเขียนโปรแกรมPython ของโปรแกรมค านวณหาค่าเฉลี ยของคะแนนจากการสอบ 3 ครั้ง 
#โดยรับค่า รหัสนักเรียน ชื อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ แล้วแสดงผลค่าเฉลี ยที ค านวณได้ทางหน้าจอ

#1.รับค่าข้อมูลของนักเรียนทางแป้นพิมพ์ 2.คำนวณหาค่าเฉลี่ยของคะแนนสอบ 3.แสดงผลค่าเฉลี่ยทางหน้าจอ  4.แสดงชื่อโปรอแกรมทางหน้าจอ

def inputData( ) :
    name = input('โปรอป้อนชื่อของคุณ : ')
    idstuden = input('โปรดป้อนรหัสนักศึกษาของคุณ : ')
    grade1 = float(input('โปรดป้อนคะแนนสอบครั้งแรกของคุณ : '))
    grade2 = float(input('โปรดป้อนคะแนนสอบครั้งที่สองของคุณ : '))
    grade3 = float(input('โปรดป้อนคะแนนสอบครั้งที่สามของคุณ : '))
    return name,idstuden,grade1,grade2,grade3
def calaverageGrade (grade1,grade2,grade3) :
    averageGrade = (grade1+grade2+grade3)/3
    return averageGrade
def showCalAverageGrade( ) :
    print(f'ชื่อของคุณคือ {name} ')
    print(f'รหัสนักศึกษาของคุณคือ {idstuden} ')
    print(f'คะแนนสอบเฉลี่ยของคุณ {averageGrade:.2f} ')
def ShowProgramName( ) :
    print('--**โปรแกรมตำนวณค่าเฉลี่ยคะแนนสอบทั้ง3ครั้ง--**')

print('----------------------------')
ShowProgramName( )
print('----------------------------')
name,idstuden,grade1,grade2,grade3=inputData( )
print('----------------------------')
averageGrade=calaverageGrade(grade1,grade2,grade3)
showCalAverageGrade( )
print('----------------------------')
