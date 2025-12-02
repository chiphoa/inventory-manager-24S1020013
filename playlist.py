# Biến lưu trữ dữ liệu. Mỗi bài hát là một dict {'title': '...', 'artist': '...', 'duration': 0}
songs = []

def add_song():
    # Nhập tên bài, ca sĩ, thời lượng -> append vào songs
    print("--- Thêm bài hát vào playlist ---")
    pass # Sẽ triển khai ở Feature 1

def view_playlist():
    # Duyệt list songs và in ra
    # Ví dụ: 1. Lạc Trôi - Sơn Tùng MTP (240s)
    pass # Sẽ triển khai ở Feature 2

def search_by_artist(artist_name):
    # Nhập tên ca sĩ, duyệt list, so sánh artist, in ra bài hát
    pass # Sẽ triển khai ở Feature 3

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            artist = input("Nhập tên ca sĩ cần tìm: ")
            search_by_artist(artist)
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()