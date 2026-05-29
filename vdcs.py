try:
    num_forms = input("Nhập số lượng phiếu đăng ký cần xử lý:")
    num_forms_int = int(num_forms)

    if num_forms_int <= 0:
        print("Số lượng phiếu đăng ký không hợp lệ")
        print("Chương trình kết thúc.")
    else:
        for i in range(1, num_forms_int + 1):
            print(f"\nPhiếu {i}")
            raw_data = input("Định dạng (Họ tên | Tên khóa học | Mã học viên | Email): ")

            parts = raw_data.split("|")
            if len(parts) != 4:
                print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
                continue

            raw_name = parts[0].strip()
            raw_course = parts[1].strip()
            raw_student_id = parts[2].strip()
            raw_email = parts[3].strip()

            if '@' not in raw_email:
                print("Email không hợp lệ. Bỏ qua phiếu này")
                continue

            if len(raw_student_id) < 5:
                print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
                continue

            clean_name = " ".join(raw_name.split()).title()
            clean_course = " ".join(raw_course.split()).title()
            clean_student_id = raw_student_id.upper()
            clean_email = raw_email.lower()

            course_upper_slug = "-".join(raw_course.split()).upper()
            confirmation_code = f"{clean_student_id}_{course_upper_slug}"

            print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
            print(f"Học viên: {clean_name}")
            print(f"Khóa học: {clean_course}")
            print(f"Mã học viên: {clean_student_id}")
            print(f"Email: {clean_email}")
            print(f"Mã xác nhận: {confirmation_code}")
except ValueError:
    print("Số lượng phiếu đăng ký không hợp lệ")
    print("Chương trình kết thúc.")