import json
from main import df_semua_provinsi

# Ambil daftar kelurahan dari df_semua_provinsi
indonesia_kelurahan_list = df_semua_provinsi['kelurahan'].tolist()

# Buat query untuk setiap nama kelurahan dengan menyertakan nama provinsinya
indonesia_kelurahan_list = [kelurahan + ", " + provinsi + ", Indonesia" 
                           for kelurahan, provinsi in zip(indonesia_kelurahan_list, 
                                                           df_semua_provinsi['provinsi'])]

# Tentukan jalur berkas JSON untuk mengekspor data
output_file_path = r'C:\OSMScience\KelurahanIndonesia\dataResult\daftar_kelurahan.json'

# Buat dictionary untuk menyimpan data
data = {'indonesia_kelurahan_list': indonesia_kelurahan_list}

# Export data ke berkas JSON
with open(output_file_path, 'w') as file:
    json.dump(data, file)

# Berhasil mengekspor data ke berkas JSON
print("Data berhasil diekspor ke berkas daftar_kelurahan.json")
