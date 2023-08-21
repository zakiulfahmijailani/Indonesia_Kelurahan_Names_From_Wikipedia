import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sulawesi_tenggara():
    # KABUPATEN DAN KOTA DI SULAWESI TENGGARA
    # Kabupaten Bombana
    url_bombana = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bombana"
    df_bombana = get_kelurahan_data(url_bombana, 'Kabupaten Bombana', 'sulawesi tenggara')

    # Kabupaten Buton
    url_buton = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Buton"
    df_buton = get_kelurahan_data(url_buton, 'Kabupaten Buton', 'sulawesi tenggara')

    # Kabupaten Buton Utara
    url_buton_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Buton_Utara"
    df_buton_utara = get_kelurahan_data(url_buton_utara, 'Kabupaten Buton Utara', 'sulawesi tenggara')

    # Kabupaten Kolaka
    url_kolaka = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kolaka"
    df_kolaka = get_kelurahan_data(url_kolaka, 'Kabupaten Kolaka', 'sulawesi tenggara')

    # Kabupaten Kolaka Timur
    url_kolaka_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kolaka_Timur"
    df_kolaka_timur = get_kelurahan_data(url_kolaka_timur, 'Kabupaten Kolaka Timur', 'sulawesi tenggara')

    # Kabupaten Kolaka Utara
    url_kolaka_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kolaka_Utara"
    df_kolaka_utara = get_kelurahan_data(url_kolaka_utara, 'Kabupaten Kolaka Utara', 'sulawesi tenggara')

    # Kabupaten Konawe
    url_konawe = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Konawe"
    df_konawe = get_kelurahan_data(url_konawe, 'Kabupaten Konawe', 'sulawesi tenggara')

    # Kabupaten Konawe Selatan
    url_konawe_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Konawe_Selatan"
    df_konawe_selatan = get_kelurahan_data(url_konawe_selatan, 'Kabupaten Konawe Selatan', 'sulawesi tenggara')

    # Kabupaten Konawe Utara
    url_konawe_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Konawe_Utara"
    df_konawe_utara = get_kelurahan_data(url_konawe_utara, 'Kabupaten Konawe Utara', 'sulawesi tenggara')

    # Kabupaten Muna
    url_muna = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Muna"
    df_muna = get_kelurahan_data(url_muna, 'Kabupaten Muna', 'sulawesi tenggara')

    # Kabupaten Muna Barat
    url_muna_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Muna_Barat"
    df_muna_barat = get_kelurahan_data(url_muna_barat, 'Kabupaten Muna Barat', 'sulawesi tenggara')

    # Kabupaten Wakatobi
    url_wakatobi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Wakatobi"
    df_wakatobi = get_kelurahan_data(url_wakatobi, 'Kabupaten Wakatobi', 'sulawesi tenggara')

    # Kota Bau-Bau
    url_bau_bau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bau-Bau"
    df_bau_bau = get_kelurahan_data(url_bau_bau, 'Kota Bau-Bau', 'sulawesi tenggara')

    # Kota Kendari
    url_kendari = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Kendari"
    df_kendari = get_kelurahan_data(url_kendari, 'Kota Kendari', 'sulawesi tenggara')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sulawesi_tenggara = pd.concat([df_bombana, df_buton, df_buton_utara, df_kolaka, df_kolaka_timur, df_kolaka_utara,
                                        df_konawe, df_konawe_selatan, df_konawe_utara, df_muna, df_muna_barat,
                                        df_wakatobi, df_bau_bau, df_kendari], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sulawesi_tenggara = df_all_sulawesi_tenggara.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sulawesi_tenggara = df_all_sulawesi_tenggara[~df_all_sulawesi_tenggara['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sulawesi_tenggara)

    # Ambil daftar kelurahan dari df_all_sulawesi_tenggara
    sulawesi_tenggara_kelurahan_list = df_all_sulawesi_tenggara['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sulawesi_tenggara_kelurahan_list = [kelurahan + ", Sulawesi Tenggara, Indonesia" for kelurahan in sulawesi_tenggara_kelurahan_list]
    print(sulawesi_tenggara_kelurahan_list)

    return df_all_sulawesi_tenggara