import random
import sys

existid_codes = set()

def generate_kode_matkul_unique(prodi):
  if len(existid_codes) >= 792:
    raise Exception("Semua kombinasi kode sudah habis")

  while True:
    level = random.randint(1,8)
    nomor = random.randint(1, 99)
    kode = f"{prodi.upper()}{level}{nomor:02d}"

    if kode not in existid_codes:
      existid_codes.add(kode)
      return kode

mata_kuliah = [
    {
        "kode matkul" : generate_kode_matkul_unique("INF"),
        "mata kuliah" : "Algoritma pemrograman",
        "sks": 4
    },
]


def tampilkan_mata_kuliah():
  for index in range(len(mata_kuliah)):
    for key, value in mata_kuliah[index].items():
      print(f"{key} : {value}")
    print()

def tambah_mata_kuliah():
  try:
     nama_mata_kuliah = input("Masukkan nama mata kuliah: ")
     sks = int(input("Masukkan jumlah sks: "))
     print()
     mata_kuliah.append({
      "kode matkul": generate_kode_matkul_unique("INF"),
      "mata kuliah": nama_mata_kuliah,
      "sks": sks
  })
  except ValueError:
    print("input sks harus berupa angka coba lagi")
    tambah_mata_kuliah()

def update_mata_kuliah():
  for index, value in enumerate(mata_kuliah, start=1):
    print(f"{index}.{value["mata kuliah"]} : {value["kode matkul"]}")

  print()
  kode_matkul = input("masukkan code matkul : ").upper()

  for matkul in mata_kuliah:
    if kode_matkul in matkul["kode matkul"]:
      nama_mata_kuliah = input("Masukkan nama mata kuliah: ")
      sks = int(input("Masukkan jumlah sks: "))
      print()
      matkul.update({"mata kuliah": nama_mata_kuliah, "sks" : sks})
      return

  print()
  print("kode matkul tidak ada, coba lagi!!")
  print()
  return update_mata_kuliah()


def delete_mata_kuliah():
  for index, value in enumerate(mata_kuliah, start=1):
    print(f"{index}.{value["mata kuliah"]} : {value["kode matkul"]}")

  print()
  kode_matkul = input("Masukkan code matkul: ").upper()

  for matkul in mata_kuliah:
    if kode_matkul in matkul["kode matkul"]:
      del mata_kuliah[mata_kuliah.index(matkul)]
      return

  print()
  print("kode matkul tidak ada, coba lagi!!")
  print()
  return delete_mata_kuliah()


while True:
  print("Sistem Manajemen Mata Kuliah Sederhana \n".center(50))
  print("1.Tambah mata kuliah")
  print("2.Tampilkan mata kuliah")
  print("3.Update mata kuliah")
  print("4.Delete mata kuliah")
  print("x. keluar \n")

  pilih_menu = input("pilih menu : ")
  print()

  match pilih_menu:
    case "1":
      tambah_mata_kuliah()
    case "2":
      tampilkan_mata_kuliah()
    case "3":
      update_mata_kuliah()
    case "4":
      delete_mata_kuliah()
    case "x":
      sys.exit()

