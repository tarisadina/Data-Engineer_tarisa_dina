import uuid

expenses = []


def add_expense():
    name = input("Masukkan nama pengeluaran: ")
    amount = float(input("Masukkan jumlah pengeluaran: "))
    expense = {"id": str(uuid.uuid4()), "name": name, "amount": amount}
    expenses.append(expense)
    print("Pengeluaran berhasil ditambahkan.")


def view_expenses():
    total_expenses = sum(expense["amount"] for expense in expenses)
    print("Data Pengeluaran:")
    for expense in expenses:
        print(
            f"ID: {expense['id']}, Nama: {expense['name']}, Jumlah: {expense['amount']}")
    print(f"Total Pengeluaran: {total_expenses}")


def update_expense():
    expense_id = input("Masukkan ID pengeluaran yang ingin diubah: ")
    for expense in expenses:
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


def delete_expense():
    expense_id = input("Masukkan ID pengeluaran yang ingin dihapus: ")
    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
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
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Menu tidak valid, silakan pilih menu yang tersedia.")


if __name__ == "__main__":
    main()
