import uuid

pengeluaran = []


def tambahPengeluaran():
    name = input("Masukkan nama pengeluaran: ")
    amount = float(input("Masukkan jumlah pengeluaran: "))
    expense = {"id": str(uuid.uuid4()), "name": name, "amount": amount}
    pengeluaran.append(expense)
    print("Pengeluaran berhasil ditambahkan.")


def lihatPengeluaran():
    total_pengeluaran = sum(expense["amount"] for expense in pengeluaran)
    print("Data Pengeluaran:")
    for expense in pengeluaran:
        print(
            f"ID: {expense['id']}, Nama: {expense['name']}, Jumlah: {expense['amount']}")
    print(f"Total Pengeluaran: {total_pengeluaran}")


def ubahPengeluaran():
    expense_id = input("Masukkan ID pengeluaran yang ingin diubah: ")
    for expense in pengeluaran:
        if expense['id'] == expense_id:
            name = input(
                "Masukkan nama pengeluaran baru (kosongkan jika tidak ingin diubah): ")
            amount = input(
                "Masukkan jumlah pengeluaran baru (kosongkan jika tidak ingin diubah): ")
            if name:
                expense['name'] = name
            if amount:
                expense['amount'] = float(amount)
            print("Pengeluaran berhasil diubah.")
            return
    print("ID pengeluaran tidak ditemukan.")


def hapusPengeluaran():
    expense_id = input("Masukkan ID pengeluaran yang ingin dihapus: ")
    for expense in pengeluaran:
        if expense['id'] == expense_id:
            pengeluaran.remove(expense)
            print("Pengeluaran berhasil dihapus.")
            return
    print("ID pengeluaran tidak ditemukan.")


def main():
    while True:
        print("\nMenu:")
        print("1. Tambahkan Data Pengeluaran")
        print("2. Lihat Data Pengeluaran")
        print("3. Ubah Data Pengeluaran")
        print("4. Hapus Data Pengeluaran")
        print("5. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            tambahPengeluaran()
        elif choice == '2':
            lihatPengeluaran()
        elif choice == '3':
            ubahPengeluaran()
        elif choice == '4':
            hapusPengeluaran()
        elif choice == '5':
            print("Terima kasih! bye...")
            break
        else:
            print("Menu tidak valid, silakan pilih menu yang tersedia.")


if __name__ == "__main__":
    main()
