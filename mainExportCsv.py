from main import df_semua_provinsi
import csv

# Ambil daftar kelurahan dari df_semua_provinsi
indonesia_kelurahan_list = df_semua_provinsi['kelurahan'].tolist()

# Buat query untuk setiap nama kelurahan dengan menyertakan nama provinsinya
indonesia_kelurahan_list = [kelurahan + ", " + provinsi + ", Indonesia" 
                           for kelurahan, provinsi in zip(indonesia_kelurahan_list, 
                                                           df_semua_provinsi['provinsi'])]

# Tentukan jalur berkas CSV untuk mengekspor data
output_file_path = r'C:\OSMScience\KelurahanIndonesia\dataResult\daftar_kelurahan.csv'

# Buka berkas CSV untuk menulis
with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
    # Buat objek penulis CSV
    csv_writer = csv.writer(file)
    
    # Tulis setiap elemen daftar kelurahan ke berkas CSV
    for kelurahan in indonesia_kelurahan_list:
        csv_writer.writerow([kelurahan])

# Berhasil mengekspor data ke berkas CSV
print("Data berhasil diekspor ke berkas daftar_kelurahan.csv")
