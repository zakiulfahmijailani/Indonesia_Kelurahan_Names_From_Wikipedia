import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kalteng():
    # KABUPATEN DAN KOTA DI KALIMANTAN TENGAH
    # Kabupaten Barito Selatan
    url_barito_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Barito_Selatan"
    df_barito_selatan = get_kelurahan_data(url_barito_selatan, 'Kabupaten Barito Selatan', 'kalimantan tengah')

    # Kabupaten Barito Timur
    url_barito_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Barito_Timur"
    df_barito_timur = get_kelurahan_data(url_barito_timur, 'Kabupaten Barito Timur', 'kalimantan tengah')

    # Kabupaten Barito Utara
    url_barito_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Barito_Utara"
    df_barito_utara = get_kelurahan_data(url_barito_utara, 'Kabupaten Barito Utara', 'kalimantan tengah')

    # Kabupaten Gunung Mas
    url_gunung_mas = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gunung_Mas"
    df_gunung_mas = get_kelurahan_data(url_gunung_mas, 'Kabupaten Gunung Mas', 'kalimantan tengah')

    # Kabupaten Kapuas
    url_kapuas = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kapuas"
    df_kapuas = get_kelurahan_data(url_kapuas, 'Kabupaten Kapuas', 'kalimantan tengah')

    # Kabupaten Katingan
    url_katingan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Katingan"
    df_katingan = get_kelurahan_data(url_katingan, 'Kabupaten Katingan', 'kalimantan tengah')

    # Kabupaten Kotawaringin Barat
    url_kotawaringin_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kotawaringin_Barat"
    df_kotawaringin_barat = get_kelurahan_data(url_kotawaringin_barat, 'Kabupaten Kotawaringin Barat', 'kalimantan tengah')

    # Kabupaten Kotawaringin Timur
    url_kotawaringin_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kotawaringin_Timur"
    df_kotawaringin_timur = get_kelurahan_data(url_kotawaringin_timur, 'Kabupaten Kotawaringin Timur', 'kalimantan tengah')

    # Kabupaten Lamandau
    url_lamandau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lamandau"
    df_lamandau = get_kelurahan_data(url_lamandau, 'Kabupaten Lamandau', 'kalimantan tengah')

    # Kabupaten Murung Raya
    url_murung_raya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Murung_Raya"
    df_murung_raya = get_kelurahan_data(url_murung_raya, 'Kabupaten Murung Raya', 'kalimantan tengah')

    # Kabupaten Pulang Pisau
    url_pulang_pisau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pulang_Pisau"
    df_pulang_pisau = get_kelurahan_data(url_pulang_pisau, 'Kabupaten Pulang Pisau', 'kalimantan tengah')

    # Kabupaten Seruyan
    url_seruyan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Seruyan"
    df_seruyan = get_kelurahan_data(url_seruyan, 'Kabupaten Seruyan', 'kalimantan tengah')

    # Kota Palangka Raya
    url_palangka_raya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Palangka_Raya"
    df_palangka_raya = get_kelurahan_data(url_palangka_raya, 'Kota Palangka Raya', 'kalimantan tengah')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_kalimantan_tengah = pd.concat([df_barito_selatan, df_barito_timur, df_barito_utara, df_gunung_mas, df_kapuas,
                                        df_katingan, df_kotawaringin_barat, df_kotawaringin_timur, df_lamandau,
                                        df_murung_raya, df_pulang_pisau, df_seruyan, df_palangka_raya], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_kalimantan_tengah = df_all_kalimantan_tengah.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_kalimantan_tengah = df_all_kalimantan_tengah[~df_all_kalimantan_tengah['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_kalimantan_tengah)

    # Ambil daftar kelurahan dari df_all_kalimantan_tengah
    kalimantan_tengah_kelurahan_list = df_all_kalimantan_tengah['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    kalimantan_tengah_kelurahan_list = [kelurahan + ", Kalimantan Tengah, Indonesia" for kelurahan in kalimantan_tengah_kelurahan_list]
    print(kalimantan_tengah_kelurahan_list)

    return df_all_kalimantan_tengah