import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sulawesi_barat():
    # KABUPATEN DAN KOTA DI SULAWESI BARAT
    # Kabupaten Majene
    url_majene = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Majene"
    df_majene = get_kelurahan_data(url_majene, 'Kabupaten Majene', 'sulawesi barat')

    # Kabupaten Mamasa
    url_mamasa = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mamasa"
    df_mamasa = get_kelurahan_data(url_mamasa, 'Kabupaten Mamasa', 'sulawesi barat')

    # Kabupaten Mamuju
    url_mamuju = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mamuju"
    df_mamuju = get_kelurahan_data(url_mamuju, 'Kabupaten Mamuju', 'sulawesi barat')

    # Kabupaten Mamuju Tengah
    url_mamuju_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mamuju_Tengah"
    df_mamuju_tengah = get_kelurahan_data(url_mamuju_tengah, 'Kabupaten Mamuju Tengah', 'sulawesi barat')

    # Kabupaten Polewali Mandar
    url_polewali_mandar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Polewali_Mandar"
    df_polewali_mandar = get_kelurahan_data(url_polewali_mandar, 'Kabupaten Polewali Mandar', 'sulawesi barat')

    # Kota Mamuju
    url_mamuju_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Mamuju"
    df_mamuju_kota = get_kelurahan_data(url_mamuju_kota, 'Kota Mamuju', 'sulawesi barat')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sulawesi_barat = pd.concat([df_majene, df_mamasa, df_mamuju, df_mamuju_tengah, df_polewali_mandar,
                                    df_mamuju_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sulawesi_barat = df_all_sulawesi_barat.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sulawesi_barat = df_all_sulawesi_barat[~df_all_sulawesi_barat['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sulawesi_barat)

    # Ambil daftar kelurahan dari df_all_sulawesi_barat
    sulawesi_barat_kelurahan_list = df_all_sulawesi_barat['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sulawesi_barat_kelurahan_list = [kelurahan + ", Sulawesi Barat, Indonesia" for kelurahan in sulawesi_barat_kelurahan_list]
    print(sulawesi_barat_kelurahan_list)

    return df_all_sulawesi_barat