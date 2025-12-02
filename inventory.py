# File: inventory.py

# 1. Khai báo biến danh sách toàn cục products = []
products = []

def add_product(name, price, quantity):
    """
    Hàm thêm sản phẩm vào danh sách products.
    Yêu cầu: Lưu dưới dạng Dictionary (ví dụ: {'name': 'Mi tom', 'price': 5000, 'qty': 100})
    """
    product = {
        "name": name,
        "price": price,
        "qty": quantity
    }
    products.append(product)
    print(f"Đã thêm thành công: {name}")

def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG (INVENTORY MANAGEMENT) ---")
        print("1. Thêm sản phẩm (Add product)")
        print("2. Hiển thị danh sách sản phẩm (List products)")
        print("3. Tìm kiếm sản phẩm (Search product)")
        print("0. Thoát (Exit)")
        
        choice = input("Mời bạn chọn chức năng: ")

        if choice == '1':
            # Nhập thông tin từ bàn phím
            name = input("Nhập tên sản phẩm: ")
            try:
                # Ép kiểu dữ liệu về số nguyên
                price = int(input("Nhập giá bán: "))
                quantity = int(input("Nhập số lượng tồn kho: "))
                
                # Gọi hàm xử lý
                add_product(name, price, quantity)
            except ValueError:
                print("Lỗi: Giá và Số lượng phải là số nguyên!")
                
        elif choice == '2':
            print("Chức năng Hiển thị danh sách sẽ được phát triển sau.")
        elif choice == '3':
            print("Chức năng Tìm kiếm sẽ được phát triển sau.")
        elif choice == '0':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if _name_ == "_main_":
    main()

thay nộ
