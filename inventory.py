# inventory.py

products = []  # danh sách lưu sản phẩm
def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "qty": quantity
    }
    products.append(product)
    print(">>> Đã thêm sản phẩm thành công!")

def main():
    while True:
        print("\n=== MENU QUẢN LÝ KHO ===")
        print("1. Nhập hàng (add product)")
        print("2. Xem tồn kho (view inventory)")
        print("3. Cảnh báo hết hàng (low stock)")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "0":
            print("Tạm biệt!")
            break
