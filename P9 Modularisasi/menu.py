menu_list = [] #modulini berfungsi untuk mengelola data menu (user defined) 

def tambah_menu(makanan, minuman): #code ini untuk user memilih menu makanan dan minuman yang dipilih
    menu = {
        "makanan": makanan,
        "minuman": minuman,
    }
    menu_list.append(menu) #menambahkan menu ke dalamn menu_list

def tampilkan_menu(): #code ini menampilkan menu yang dipilih user
    if len(menu_list) == 0: #jika menu tidak dipilih/kosong maka tidak akan menampilkan menu yang dipilih
        print("Belum ada menu Anda!")
    else:
        for menu in menu_list: #jika menu di dalam menu_list maka akan menampilkan menu makanan dan minuman yang dipilih
            print(f"Makanan: {menu["makanan"]}, Minuman: {menu["minuman"]}")

def hapus_menu(): #code ini jika ingin menghapus menu yang dipilih
    menu_list.clear()

def selesai(): #code ini jika sudah selesai untuk memilih menu
    for menu in menu_list:
        print(f"Hasil belanja Anda: {menu["makanan"]} dan {menu["minuman"]}, Terima Kasih!")