# Khai báo biến danh sách toàn cục products = []
products = [] # Biến này sẽ chứa danh sách các sản phẩm trong kho

def add_product():
    # Nhập tên, giá, số lượng -> append vào products
    print("--- 1. Nhập hàng mới ---")
    pass 

def view_inventory():
    # Duyệt list products và in ra
    pass 

def check_low_stock():
    # Duyệt list, kiểm tra nếu qty < 5 thì in ra cảnh báo hết hàng
    pass 

def main():
    while True:
        print("\n=== QUẢN LÝ KHO HÀNG ===")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            check_low_stock()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()