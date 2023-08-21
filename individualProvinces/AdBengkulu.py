import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_bengkulu():
        # KABUPATEN DAN KOTA DI BENGKULU
    # Kabupaten Bengkulu Selatan
    url_bengkulu_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bengkulu_Selatan"
    df_bengkulu_selatan = get_kelurahan_data(url_bengkulu_selatan, 'Kabupaten Bengkulu Selatan', 'Bengkulu')

    # Kabupaten Bengkulu Tengah
    url_bengkulu_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bengkulu_Tengah"
    df_bengkulu_tengah = get_kelurahan_data(url_bengkulu_tengah, 'Kabupaten Bengkulu Tengah', 'Bengkulu')

    # Kabupaten Bengkulu Utara
    url_bengkulu_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bengkulu_Utara"
    df_bengkulu_utara = get_kelurahan_data(url_bengkulu_utara, 'Kabupaten Bengkulu Utara', 'Bengkulu')

    # Kabupaten Kaur
    url_kaur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kaur"
    df_kaur = get_kelurahan_data(url_kaur, 'Kabupaten Kaur', 'Bengkulu')

    # Kabupaten Kepahiang
    url_kepahiang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepahiang"
    df_kepahiang = get_kelurahan_data(url_kepahiang, 'Kabupaten Kepahiang', 'Bengkulu')

    # Kabupaten Lebong
    url_lebong = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lebong"
    df_lebong = get_kelurahan_data(url_lebong, 'Kabupaten Lebong', 'Bengkulu')

    # Kabupaten Mukomuko
    url_mukomuko = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mukomuko"
    df_mukomuko = get_kelurahan_data(url_mukomuko, 'Kabupaten Mukomuko', 'Bengkulu')

    # Kabupaten Rejang Lebong
    url_rejang_lebong = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Rejang_Lebong"
    df_rejang_lebong = get_kelurahan_data(url_rejang_lebong, 'Kabupaten Rejang Lebong', 'Bengkulu')

    # Kabupaten Seluma
    url_seluma = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Seluma"
    df_seluma = get_kelurahan_data(url_seluma, 'Kabupaten Seluma', 'Bengkulu')

    # Kota Bengkulu
    url_bengkulu_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bengkulu"
    df_bengkulu_kota = get_kelurahan_data(url_bengkulu_kota, 'Kota Bengkulu', 'Bengkulu')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_bengkulu = pd.concat([df_bengkulu_selatan, df_bengkulu_tengah, df_bengkulu_utara,
                                df_kaur, df_kepahiang, df_lebong, df_mukomuko, df_rejang_lebong,
                                df_seluma, df_bengkulu_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_bengkulu = df_all_bengkulu.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_bengkulu = df_all_bengkulu[~df_all_bengkulu['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_bengkulu)

    # Ambil daftar kelurahan dari df_all_bengkulu
    bengkulu_kelurahan_list = df_all_bengkulu['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    bengkulu_kelurahan_list = [kelurahan + ", Bengkulu, Indonesia" for kelurahan in bengkulu_kelurahan_list]
    print(bengkulu_kelurahan_list)

    return df_all_bengkulu