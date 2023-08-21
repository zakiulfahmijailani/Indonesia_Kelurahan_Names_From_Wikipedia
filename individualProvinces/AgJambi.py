import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_jambi():
    # KABUPATEN DAN KOTA DI JAMBI
    # Kabupaten Batanghari
    url_batanghari = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Batanghari"
    df_batanghari = get_kelurahan_data(url_batanghari, 'Kabupaten Batanghari', 'Jambi')

    # Kabupaten Bungo
    url_bungo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bungo"
    df_bungo = get_kelurahan_data(url_bungo, 'Kabupaten Bungo', 'Jambi')

    # Kabupaten Kerinci
    url_kerinci = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kerinci"
    df_kerinci = get_kelurahan_data(url_kerinci, 'Kabupaten Kerinci', 'Jambi')

    # Kabupaten Merangin
    url_merangin = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Merangin"
    df_merangin = get_kelurahan_data(url_merangin, 'Kabupaten Merangin', 'Jambi')

    # Kabupaten Muaro Jambi
    url_muaro_jambi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Muaro_Jambi"
    df_muaro_jambi = get_kelurahan_data(url_muaro_jambi, 'Kabupaten Muaro Jambi', 'Jambi')

    # Kabupaten Sarolangun
    url_sarolangun = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sarolangun"
    df_sarolangun = get_kelurahan_data(url_sarolangun, 'Kabupaten Sarolangun', 'Jambi')

    # Kabupaten Tanjung Jabung Barat
    url_tanjung_jabung_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tanjung_Jabung_Barat"
    df_tanjung_jabung_barat = get_kelurahan_data(url_tanjung_jabung_barat, 'Kabupaten Tanjung Jabung Barat', 'Jambi')

    # Kabupaten Tanjung Jabung Timur
    url_tanjung_jabung_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tanjung_Jabung_Timur"
    df_tanjung_jabung_timur = get_kelurahan_data(url_tanjung_jabung_timur, 'Kabupaten Tanjung Jabung Timur', 'Jambi')

    # Kota Jambi
    url_jambi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Jambi"
    df_jambi = get_kelurahan_data(url_jambi, 'Kota Jambi', 'Jambi')

    # Kota Sungai Penuh
    url_sungai_penuh = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Sungai_Penuh"
    df_sungai_penuh = get_kelurahan_data(url_sungai_penuh, 'Kota Sungai Penuh', 'Jambi')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_jambi = pd.concat([df_batanghari, df_bungo, df_kerinci, df_merangin, df_muaro_jambi,
                            df_sarolangun, df_tanjung_jabung_barat, df_tanjung_jabung_timur,
                            df_jambi, df_sungai_penuh], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_jambi = df_all_jambi.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_jambi = df_all_jambi[~df_all_jambi['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_jambi)

    # Ambil daftar kelurahan dari df_all_jambi
    jambi_kelurahan_list = df_all_jambi['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    jambi_kelurahan_list = [kelurahan + ", Jambi, Indonesia" for kelurahan in jambi_kelurahan_list]
    print(jambi_kelurahan_list)

    return df_all_jambi