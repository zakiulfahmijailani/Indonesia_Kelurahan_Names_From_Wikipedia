from libraries import *
from main import get_kelurahan_data

'''
JAKARTA
'''

# J.PUSAT
url_pusat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Pusat"
df_pusat = get_kelurahan_data(url_pusat, 'Kota Administrasi Jakarta Pusat')

# J. SEL
url_sel = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Selatan"
df_sel = get_kelurahan_data(url_sel, 'Kota Administrasi Jakarta Selatan')

# J. UTARA
url_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Utara"
df_utara = get_kelurahan_data(url_utara, 'Kota Administrasi Jakarta Utara')

# J.TIMUR
url_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Timur"
df_timur = get_kelurahan_data(url_timur, 'Kota Administrasi Jakarta Timur')

# J.BARAT
url_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Barat"
df_barat = get_kelurahan_data(url_barat, 'Kota Administrasi Jakarta Barat')

# ALL JAKARTA
# Combine all DataFrames into a single DataFrame
df_all_Jakarta = pd.concat([df_pusat, df_sel, df_utara, df_timur, df_barat], ignore_index=True)

# Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai ke huruf kecil
df_all_Jakarta = df_all_Jakarta.applymap(lambda x: x.lower() if isinstance(x, str) else x)

values_to_remove = ['Gunung', 'Balekambang']

# Remove rows where the 'kelurahan' column matches any of the specified values
df_all_Jakarta = df_all_Jakarta[~df_all_Jakarta['kelurahan'].isin(values_to_remove)]

# Cetak DataFrame untuk memastikan perubahan telah dilakukan
print(df_all_Jakarta)

# Ambil daftar kelurahan dari df_all_Jakarta
Jakarta_kelurahan_list = df_all_Jakarta['kelurahan'].tolist()

# Buat query untuk setiap nama kelurahan
Jakarta_kelurahan_list = [kelurahan + ", Jakarta, Indonesia" for kelurahan in Jakarta_kelurahan_list]
print(Jakarta_kelurahan_list)