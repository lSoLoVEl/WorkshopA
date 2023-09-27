def check_student_grade():
    num_students = int(input('โปรดป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ: '))

    for i in range(num_students):
        student_id = input(f'โปรดป้อนรหัสนักเรียนที่ {i+1}: ')
        student_name = input(f'โปรดป้อนชื่อนักเรียนที่ {i+1}: ')
        student_grade = float(input(f'โปรดป้อนเกรดเฉลี่ยของนักเรียนที่ {i+1}: '))

        if student_grade >= 2.00:
            print(f'นักเรียน {student_name} (รหัส {student_id}) ได้เกรดเฉลี่ย {student_grade} สอบผ่าน')
        else:
            print(f'นักเรียน {student_name} (รหัส {student_id}) ได้เกรดเฉลี่ย {student_grade} สอบไม่ผ่าน')

def main():
    print('**------------------------------------**')
    print('**------โปรแกรมตรวจสอบผลการเรียนของนักเรียน------**')
    print('**------------------------------------**')
    check_student_grade()
    print('**------------------------------------**')

if __name__ == "__main__":
    main()
