from libraries import *
from main import get_kelurahan_data

'''
BANTEN
'''

# BANTEN
# Kabupaten/Kota yang ada di Banten
# Ganti link URL berikut dengan sumber data yang sesuai untuk Kabupaten/Kota di Banten

# Kabupaten Lebak
url_lebak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lebak"
df_lebak = get_kelurahan_data(url_lebak, 'Kabupaten Lebak')

# Kabupaten Pandeglang
url_pandeglang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pandeglang"
df_pandeglang = get_kelurahan_data(url_pandeglang, 'Kabupaten Pandeglang')

# Kabupaten Serang
url_serang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Serang"
df_serang = get_kelurahan_data(url_serang, 'Kabupaten Serang')

# Kabupaten Tangerang
url_tangerang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tangerang"
df_tangerang = get_kelurahan_data(url_tangerang, 'Kabupaten Tangerang')

# Kota Cilegon
url_cilegon = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Cilegon"
df_cilegon = get_kelurahan_data(url_cilegon, 'Kota Cilegon')

# Kota Serang
url_kota_serang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Serang"
df_kota_serang = get_kelurahan_data(url_kota_serang, 'Kota Serang')

# Kota Tangerang
url_kota_tangerang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tangerang"
df_kota_tangerang = get_kelurahan_data(url_kota_tangerang, 'Kota Tangerang')

# Kota Tangerang Selatan
url_tangerang_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tangerang_Selatan"
df_tangerang_selatan = get_kelurahan_data(url_tangerang_selatan, 'Kota Tangerang Selatan')

# Gabungkan semua DataFrame menjadi satu DataFrame tunggal
df_all_Banten = pd.concat([df_lebak, df_pandeglang, df_serang, df_tangerang, df_cilegon, df_kota_serang, df_kota_tangerang, df_tangerang_selatan], ignore_index=True)

# Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai ke huruf kecil
df_all_Banten = df_all_Banten.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# List of values to remove
values_to_remove = ['bendungan', 'bojongjuruh', 'cibaturkeusik', 'cidahu', 'cilegong ilir']

# Remove rows where the 'kelurahan' column matches any of the specified values
df_all_Banten = df_all_Banten[~df_all_Banten['kelurahan'].isin(values_to_remove)]

# Cetak DataFrame untuk memastikan perubahan telah dilakukan
print(df_all_Banten)

# Ambil daftar kelurahan dari df_all_Banten
Banten_kelurahan_list = df_all_Banten['kelurahan'].tolist()

# Buat query untuk setiap nama kelurahan
Banten_kelurahan_list = [kelurahan + ", Banten, Indonesia" for kelurahan in Banten_kelurahan_list]
print(Banten_kelurahan_list)