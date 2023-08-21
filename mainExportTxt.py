from main import df_semua_provinsi

# Ambil daftar kelurahan dari df_semua_provinsi
indonesia_kelurahan_list = df_semua_provinsi['kelurahan'].tolist()

# Buat query untuk setiap nama kelurahan dengan menyertakan nama provinsinya
indonesia_kelurahan_list = [kelurahan + ", " + provinsi + ", Indonesia" 
                           for kelurahan, provinsi in zip(indonesia_kelurahan_list, 
                                                           df_semua_provinsi['provinsi'])]

# Tentukan jalur berkas txt untuk mengekspor data
output_file_path = r'C:\OSMScience\KelurahanIndonesia\dataResult\daftar_kelurahan.txt'

# Buka berkas txt untuk menulis
with open(output_file_path, 'w') as file:
    # Tulis setiap elemen daftar kelurahan ke berkas txt
    for kelurahan in indonesia_kelurahan_list:
        file.write(kelurahan + '\n')

# Berhasil mengekspor data ke berkas txt
print("Data berhasil diekspor ke berkas daftar_kelurahan.txt")
