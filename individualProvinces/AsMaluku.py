import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_maluku():
    # KABUPATEN DAN KOTA DI MALUKU
    # Kabupaten Buru
    url_buru = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Buru"
    df_buru = get_kelurahan_data(url_buru, 'Kabupaten Buru', 'maluku')

    # Kabupaten Buru Selatan
    url_buru_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Buru_Selatan"
    df_buru_selatan = get_kelurahan_data(url_buru_selatan, 'Kabupaten Buru Selatan', 'maluku')

    # Kabupaten Kepulauan Aru
    url_kepulauan_aru = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Aru"
    df_kepulauan_aru = get_kelurahan_data(url_kepulauan_aru, 'Kabupaten Kepulauan Aru', 'maluku')

    # Kabupaten Maluku Barat Daya
    url_maluku_barat_daya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Maluku_Barat_Daya"
    df_maluku_barat_daya = get_kelurahan_data(url_maluku_barat_daya, 'Kabupaten Maluku Barat Daya', 'maluku')

    # Kabupaten Maluku Tengah
    url_maluku_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Maluku_Tengah"
    df_maluku_tengah = get_kelurahan_data(url_maluku_tengah, 'Kabupaten Maluku Tengah', 'maluku')

    # Kabupaten Maluku Tenggara
    url_maluku_tenggara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Maluku_Tenggara"
    df_maluku_tenggara = get_kelurahan_data(url_maluku_tenggara, 'Kabupaten Maluku Tenggara', 'maluku')

    # Kabupaten Maluku Tenggara Barat
    url_maluku_tenggara_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Maluku_Tenggara_Barat"
    df_maluku_tenggara_barat = get_kelurahan_data(url_maluku_tenggara_barat, 'Kabupaten Maluku Tenggara Barat', 'maluku')

    # Kabupaten Seram Bagian Barat
    url_seram_bagian_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Seram_Bagian_Barat"
    df_seram_bagian_barat = get_kelurahan_data(url_seram_bagian_barat, 'Kabupaten Seram Bagian Barat', 'maluku')

    # Kabupaten Seram Bagian Timur
    url_seram_bagian_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Seram_Bagian_Timur"
    df_seram_bagian_timur = get_kelurahan_data(url_seram_bagian_timur, 'Kabupaten Seram Bagian Timur', 'maluku')

    # Kota Ambon
    url_ambon = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Ambon"
    df_ambon = get_kelurahan_data(url_ambon, 'Kota Ambon', 'maluku')

    # Kota Tual
    url_tual = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tual"
    df_tual = get_kelurahan_data(url_tual, 'Kota Tual', 'maluku')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_maluku = pd.concat([df_buru, df_buru_selatan, df_kepulauan_aru, df_maluku_barat_daya,
                            df_maluku_tengah, df_maluku_tenggara, df_maluku_tenggara_barat,
                            df_seram_bagian_barat, df_seram_bagian_timur, df_ambon, df_tual], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_maluku = df_all_maluku.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_maluku = df_all_maluku[~df_all_maluku['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_maluku)

    # Ambil daftar kelurahan dari df_all_maluku
    maluku_kelurahan_list = df_all_maluku['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    maluku_kelurahan_list = [kelurahan + ", Maluku, Indonesia" for kelurahan in maluku_kelurahan_list]
    print(maluku_kelurahan_list)

    return df_all_maluku