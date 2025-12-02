# File: inventory.py

# 1. Khai báo biến danh sách toàn cục products = []
products = []

def add_product(name, price, quantity):
    """
    Hàm thêm sản phẩm vào danh sách products.
    """
    product = {
        "name": name,
        "price": price,
        "qty": quantity
    }
    products.append(product)
    print(f"Đã thêm thành công: {name}")

def view_inventory():
    """
    Hàm hiển thị danh sách sản phẩm.
    Duyệt danh sách và in ra màn hình.
    """
    if not products:
        print("Kho hàng đang trống!")
    else:
        print("\n--- DANH SÁCH SẢN PHẨM ---")
        # In tiêu đề cột cho đẹp
        print(f"{'Tên SP':<20} {'Giá':<10} {'Số lượng':<10}")
        print("-" * 40)
        
        for p in products:
            # Lấy dữ liệu từ dictionary
            print(f"{p['name']:<20} {p['price']:<10} {p['qty']:<10}")
        print("-" * 40)

def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG (INVENTORY MANAGEMENT) ---")
        print("1. Thêm sản phẩm (Add product)")
        print("2. Hiển thị danh sách sản phẩm (List products)")
        print("3. Tìm kiếm sản phẩm (Search product)")
        print("0. Thoát (Exit)")
        
        choice = input("Mời bạn chọn chức năng: ")

        if choice == '1':
            name = input("Nhập tên sản phẩm: ")
            try:
                price = int(input("Nhập giá bán: "))
                quantity = int(input("Nhập số lượng tồn kho: "))
                add_product(name, price, quantity)
            except ValueError:
                print("Lỗi: Giá và Số lượng phải là số nguyên!")
                
        elif choice == '2':
            # Gọi hàm xem tồn kho vừa viết
            view_inventory()
            
        elif choice == '3':
            print("Chức năng Tìm kiếm sẽ được phát triển sau.")
        elif choice == '0':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if _name_ == "_main_":
    main()
