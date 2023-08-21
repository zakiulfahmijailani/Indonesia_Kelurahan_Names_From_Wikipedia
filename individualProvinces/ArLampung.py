import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_lampung():
    # KABUPATEN DAN KOTA DI LAMPUNG
    # Kabupaten Lampung Barat
    url_lampung_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lampung_Barat"
    df_lampung_barat = get_kelurahan_data(url_lampung_barat, 'Kabupaten Lampung Barat', 'lampung')

    # Kabupaten Lampung Selatan
    url_lampung_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lampung_Selatan"
    df_lampung_selatan = get_kelurahan_data(url_lampung_selatan, 'Kabupaten Lampung Selatan', 'lampung')

    # Kabupaten Lampung Tengah
    url_lampung_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lampung_Tengah"
    df_lampung_tengah = get_kelurahan_data(url_lampung_tengah, 'Kabupaten Lampung Tengah', 'lampung')

    # Kabupaten Lampung Timur
    url_lampung_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lampung_Timur"
    df_lampung_timur = get_kelurahan_data(url_lampung_timur, 'Kabupaten Lampung Timur', 'lampung')

    # Kabupaten Lampung Utara
    url_lampung_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lampung_Utara"
    df_lampung_utara = get_kelurahan_data(url_lampung_utara, 'Kabupaten Lampung Utara', 'lampung')

    # Kabupaten Lampung Way Kanan
    url_way_kanan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Way_Kanan"
    df_way_kanan = get_kelurahan_data(url_way_kanan, 'Kabupaten Lampung Way Kanan', 'lampung')

    # Kota Bandar Lampung
    url_bandar_lampung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bandar_Lampung"
    df_bandar_lampung = get_kelurahan_data(url_bandar_lampung, 'Kota Bandar Lampung', 'lampung')

    # Kota Metro
    url_metro = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Metro"
    df_metro = get_kelurahan_data(url_metro, 'Kota Metro', 'lampung')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_lampung = pd.concat([df_lampung_barat, df_lampung_selatan, df_lampung_tengah, df_lampung_timur,
                            df_lampung_utara, df_way_kanan, df_bandar_lampung, df_metro], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_lampung = df_all_lampung.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_lampung = df_all_lampung[~df_all_lampung['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_lampung)

    # Ambil daftar kelurahan dari df_all_lampung
    lampung_kelurahan_list = df_all_lampung['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    lampung_kelurahan_list = [kelurahan + ", Lampung, Indonesia" for kelurahan in lampung_kelurahan_list]
    print(lampung_kelurahan_list)

    return df_all_lampung