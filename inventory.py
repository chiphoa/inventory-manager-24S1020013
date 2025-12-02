def check_low_stock():
    """
    Hàm kiểm tra tồn kho.
    Duyệt danh sách sản phẩm và in ra những sản phẩm nào có số lượng dưới 5.
    """
    print("\n=== 3. CẢNH BÁO HẾT HÀNG ===")
    
    # Lọc ra các sản phẩm có số lượng (qty) dưới 5
    low_stock_items = [product for product in products if product['qty'] < 5] 

    if not low_stock_items:
        print("Không có sản phẩm nào cần nhập thêm (Tồn kho > 5).")
        return

    print("CÁC SẢN PHẨM CẦN NHẬP THÊM (Tồn kho < 5):")
    print(f"{'TÊN SẢN PHẨM':<30}{'TỒN KHO':<10}")
    print("-" * 40)
    for item in low_stock_items:
        print(f"{item['name']:<30}{item['qty']:<10}")
