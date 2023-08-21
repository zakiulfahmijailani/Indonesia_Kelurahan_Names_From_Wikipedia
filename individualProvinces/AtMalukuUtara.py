import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_maluku_utara():
    # KABUPATEN DAN KOTA DI MALUKU UTARA
    # Kabupaten Halmahera Barat
    url_halmahera_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Halmahera_Barat"
    df_halmahera_barat = get_kelurahan_data(url_halmahera_barat, 'Kabupaten Halmahera Barat', 'maluku utara')

    # Kabupaten Halmahera Tengah
    url_halmahera_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Halmahera_Tengah"
    df_halmahera_tengah = get_kelurahan_data(url_halmahera_tengah, 'Kabupaten Halmahera Tengah', 'maluku utara')

    # Kabupaten Halmahera Timur
    url_halmahera_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Halmahera_Timur"
    df_halmahera_timur = get_kelurahan_data(url_halmahera_timur, 'Kabupaten Halmahera Timur', 'maluku utara')

    # Kabupaten Halmahera Selatan
    url_halmahera_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Halmahera_Selatan"
    df_halmahera_selatan = get_kelurahan_data(url_halmahera_selatan, 'Kabupaten Halmahera Selatan', 'maluku utara')

    # Kabupaten Halmahera Utara
    url_halmahera_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Halmahera_Utara"
    df_halmahera_utara = get_kelurahan_data(url_halmahera_utara, 'Kabupaten Halmahera Utara', 'maluku utara')

    # Kabupaten Morotai
    url_morotai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Morotai"
    df_morotai = get_kelurahan_data(url_morotai, 'Kabupaten Morotai', 'maluku utara')

    # Kabupaten Pulau Taliabu
    url_taliabu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pulau_Taliabu"
    df_taliabu = get_kelurahan_data(url_taliabu, 'Kabupaten Pulau Taliabu', 'maluku utara')

    # Kota Ternate
    url_ternate = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Ternate"
    df_ternate = get_kelurahan_data(url_ternate, 'Kota Ternate', 'maluku utara')

    # Kota Tidore Kepulauan
    url_tidore_kepulauan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tidore_Kepulauan"
    df_tidore_kepulauan = get_kelurahan_data(url_tidore_kepulauan, 'Kota Tidore Kepulauan', 'maluku utara')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_maluku_utara = pd.concat([df_halmahera_barat, df_halmahera_tengah, df_halmahera_timur,
                                    df_halmahera_selatan, df_halmahera_utara, df_morotai,
                                    df_taliabu, df_ternate, df_tidore_kepulauan], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_maluku_utara = df_all_maluku_utara.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_maluku_utara = df_all_maluku_utara[~df_all_maluku_utara['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_maluku_utara)

    # Ambil daftar kelurahan dari df_all_maluku_utara
    maluku_utara_kelurahan_list = df_all_maluku_utara['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    maluku_utara_kelurahan_list = [kelurahan + ", Maluku Utara, Indonesia" for kelurahan in maluku_utara_kelurahan_list]
    print(maluku_utara_kelurahan_list)

    return df_all_maluku_utara