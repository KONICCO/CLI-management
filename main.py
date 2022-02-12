import json,datetime,os #modul

today = datetime.date.today().strftime("%d-%m-%y") #tanggal hari ini
filename = "tes.json"#mengvariabelkan file

def setup():
    if os.path.isfile(filename): #melihat apakah sudah ada file json
        while True:#perulangn
            menu() #menu
            pilih = input("\npilih menu: ")
            print("\n")
            if   pilih == "1":
                view_data() #manggil function
            elif pilih == "2":
                add_data() #manggil function
            elif pilih == "3":
                delete_data() #manggil function
            elif pilih == "4":
                edit_data() #manggil function
            elif pilih == "5":
                search_data()
            elif pilih == "6":
                break #berhenti
            else:
                print ("salah masukan") #slah masukan
                
    else:
        news()#penambahan baru
def search_data():
    with open (filename, "r") as f: #membuka dan membaca
        temp = json.load(f)#mengambil path/memuat JSON file kedalam variabel 
    print('='*60)
    print("{:>30}".format('Program search barang'))
    print('='*60)
    # x= input('Masukan yang ingin dicari: ')
    # x=1
    search_option =  input('Masukan yang ingin dicari: ')
    print("no\ttanggal\t\ttempat\t\tnama barang\t jumlah barang\ttotal harga")
    print("="*85)
    i=1
    for x in temp:
        if search_option== x["nama barang"]:
                tanggal = x["tgl"]#membuat variabel untuk value
                tempat  = x["tempat"]
                nama    = x["nama barang"]
                jumlah  = x["jumlah barang"]
                harga   = x["total harga" ]
                print("{:<8}{:<15}{:<18}{:<18}{:<18}{:<10}".format(i,tanggal,tempat,nama,jumlah,harga)) #formatting string
                i+=1
        else:
            print('data tidak ada')
            search_data()
    print()
    
def news():
    baru= []
    i =dict()
    i["tgl"]            = today
    i["tempat"]         = input('tempat beli: ')
    i["nama barang"]    = input('nama barang: ')
    i["jumlah barang"]  = int(input('jumlah barang: '))
    i["total harga"]    = int(input('total harga: '))
    baru.append(i)
    with open (filename, "w") as f:
        json.dump(baru,f,indent=4) #menyimpan array dictionary kedalam file 
    setup()
def add_data():
    print('='*60)
    print("{:>30}".format('add data'))
    print('='*60)
    item_data = {} #dict
    with open (filename, "r") as f:
        temp = json.load(f)#mengambil path/memuat JSON file kedalam variabel 
    item_data["tgl"]                = today #menginput value
    item_data["tempat"]             = input("nama tempat: ")#menginput value
    item_data["nama barang"]        = input("nama barang: ")#menginput value
    item_data["jumlah barang"]      = int(input("jumlah barang: "))#menginput value
    item_data["total harga"]        = int(input("total harga: "))#menginput value
    temp.append(item_data)#menambah item data ke array
    with open (filename, "w") as f: #membuka dan menulis
        json.dump(temp, f, indent=4)#menyimpan array dictionary kedalam file , 
    print()

def delete_data():
    view_data()
    new_data = []#array
    with open(filename,"r") as f: #membuka dan membaca
        temp=json.load(f)#mengambil path/memuat JSON file kedalam variabel 
        length=len(temp) #menghitung byk data
    print("Hapus berdasarkan nomor")
    delete_option = input(f"Pilih nomor [1-{length}]: ")#input
    i=1
    for entry in temp:
        if i == int(delete_option):#jika sama
            pass#tidak melakukan apa2 maka listnya kosong dan akan menghapus
            i+=1# i adalah nomor
        else:
            new_data.append(entry)#menambah ke list
            i+=1
    with open(filename,"w") as f: #membuka dan menulis
        json.dump(new_data,f,indent=4)#menyimpan array dictionary kedalam file ,  inden
    print()

def edit_data():
    view_data()#melihat
    new_data = []#array
    with open (filename, "r") as f:#membuka dan membaca
        temp = json.load(f)#mengambil path/memuat JSON file kedalam variabel 
        data_length = len(temp)#menghitung byk data
    print("pilih nomor untuk mengganti data")
    edit_option = input(f"pilih nomor 1-{data_length}: ") #input nomor
    i=1
    Check_True= True
    for x in temp:
        if int(edit_option) > data_length:
            if Check_True == True:
                print("salah masukan")
                Check_True=False
        else:
            try:
                if i == int(edit_option): #jika sama dengan input
                    tanggal = x["tgl"] #membuat variabel pada value
                    tempat  = x["tempat"]#membuat variabel pada value
                    nama    = x["nama barang"]#membuat variabel pada value
                    jumlah  = x["jumlah barang"]
                    harga   = x["total harga" ]#membuat variabel pada value
                    print(f"tanggal sebelumnya: {tanggal}")#menampilkan data yang akan dirubah
                    tanggal = tanggal#input perubah
                    print()
                    print(f"tempat sebelumnya: {tempat}")#menampilkan data yang akan dirubah
                    tempat  =input("masukan tempat ganti: ")#input perubah
                    print()
                    print(f"barang sebelumnya : {nama}")#menampilkan data yang akan dirubah
                    nama    =nama#input perubah
                    print()
                    print(f"jumlah sebelumnya : {jumlah}")#menampilkan data yang akan dirubah
                    jumlah  =jumlah#input perubah
                    print()
                    print(f"total sebelumnya : {harga}")#menampilkan data yang akan dirubah
                    harga   =int(input("masukan total harga ganti: "))#input perubah
                    print()
                    new_data.append({ "tgl": tanggal, "tempat": tempat, "nama barang": nama, "jumlah barang": jumlah, "total harga": harga}) #menambahkan yang dirubah
                    i=i+1
                else:
                    new_data.append(x)#menambah
                    i=i+1
                with open (filename, "w") as f: #membuka dan menulis
                    json.dump(new_data, f, indent=4)#menyimpan array dictionary kedalam file ,  inden
            except ValueError:
                if Check_True == True:
                        print("hanya angka")
                        Check_True=False
def menu(): #menu
    print ("transaksi pembelian")
    print ("Data Management System")
    print ("[1] View Data")
    print ("[2] Add Data")
    print ("[3] Delete Data")
    print ("[4] Edit Data")
    print ("[5] Search data")
    print ("[6] Exit")

def view_data():
    with open (filename, "r") as f: #membuka dan membaca
        temp = json.load(f)#mengambil path/memuat JSON file kedalam variabel 
        i = 1
        print("no\ttanggal\t\ttempat\t\tnama barang\t jumlah barang\ttotal harga")
        print("="*85)
        for x in temp:
            tanggal = x["tgl"]#membuat variabel untuk value
            tempat  = x["tempat"]
            nama    = x["nama barang"]
            jumlah  = x["jumlah barang"]
            harga   = x["total harga" ]
            print("{:<8}{:<15}{:<18}{:<18}{:<18}{:<10}".format(i,tanggal,tempat,nama,jumlah,harga)) #formatting string
            i=i+1
    print()


if __name__ == '__main__': #main blok
    setup()
