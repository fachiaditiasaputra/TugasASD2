class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TokoIkanHias:
    def __init__(self):
        self.head = None
        self.counter = 0

    def tambah_ikan_hias(self, nama, jenis, makanan, jenis_kelamin, harga, stok):
        self.counter += 1
        new_ikan = {
            'id': self.counter,
            'nama': nama,
            'jenis': jenis,
            'makanan': makanan,
            'jenis_kelamin': jenis_kelamin,
            'harga': harga,
            'stok': stok,
        }
        if not self.head:
            self.head = Node(new_ikan)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(new_ikan)
        print("===============================")
        print("Ikan hias berhasil ditambahkan")
        print("===============================")

    def lihat_ikan_hias(self):
        if not self.head:
            print("=====================")
            print("Ikan tidak ditemukan")
            print("=====================")
            return
        current = self.head
        print("==================")
        print("Daftar ikan hias")
        print("==================")
        while current:
            ikan = current.data
            print(f"ID: {ikan['id']}, Nama: {ikan['nama']}, Jenis: {ikan['jenis']}, Makanan: {ikan['makanan']}, Jenis_kelamin: {ikan['jenis_kelamin']}, Harga: {ikan['harga']}, Stok: {ikan['stok']}")
            current = current.next


    def ubah_ikan_hias(self, id_ikan, field, ikan_baru):
        current = self.head
        while current:
            if current.data['id'] == id_ikan:
                current.data[field] = ikan_baru
                print("=====================")
                print("Ikan Berhasil Diubah")
                print("=====================")
                return
            current = current.next
        print("=====================")
        print("Ikan Tidak Ditemukan")
        print("=====================")

    def hapus_ikan_hias(self, id_ikan):
        if not self.head:
            print("=====================")
            print("Ikan tidak ditemukan")
            print("=====================")
            return

        if self.head.data['id'] == id_ikan:
            self.head = self.head.next
            print("===========================")
            print("Ikan Hias Berhasil Dihapus")
            print("===========================")
            return

        prev = None
        current = self.head
        while current:
            if current.data['id'] == id_ikan:
                prev.next = current.next
                print("===========================")
                print("Ikan Hias Berhasil Dihapus")
                print("===========================")
                return
            prev = current
            current = current.next
        print("=====================")
        print("Ikan Tidak Ditemukan")
        print("=====================")

def main():
    toko = TokoIkanHias()

    while True:
        print("-------------------------")
        print("Pilihan Menu Ikan Hias ")
        print("-------------------------")
        print("1. Tambah ikan hias")
        print("2. Lihat ikan hias")
        print("3. Ubah ikan hias")
        print("4. Hapus ikan hias")
        print("5. Keluar Program")
        print("-------------------------")

        pilihan = input("Masukkan Pilihan Anda:")

        if pilihan == '1':
            nama = input("Masukkan Nama Ikan Hias:")
            jenis = input("Masukkan Jenis Ikan Hias:")
            makanan = input("Masukkan Jenis Makanan Ikan Hias:")
            jenis_kelamin = input("Masukkan Jenis Kelamin Ikan Hias:")
            harga = float(input("Masukkan Harga Ikan Hias:"))
            stok = int(input("Masukkan Stok Ikan Hias:"))
            toko.tambah_ikan_hias(nama, jenis, makanan, jenis_kelamin, harga, stok)

        elif pilihan == '2':
            toko.lihat_ikan_hias()

        elif pilihan == '3':
            id_ikan = int(input("Masukkan ID Ikan Hias Yang Ingin Diubah:"))
            field = input("Masukkan Nama field Yang Ingin Diubah (nama/jenis/makanan/jenis_kelamin/harga/stok):")
            ikan_baru = input("Masukkan Ikan Hias Baru:")
            toko.ubah_ikan_hias(id_ikan, field, ikan_baru)

        elif pilihan == '4':
            id_ikan = int(input("Masukkan ID Ikan Hias Yang Ingin Dihapus:"))
            toko.hapus_ikan_hias(id_ikan)

        elif pilihan == '5':
            print("Keluar Dari Program")
            break

        else:
            print("Pilihan Tidak Valid. Silahkan Masukkan Pilihan Yang Benar")

if __name__ == "__main__":
    main()
