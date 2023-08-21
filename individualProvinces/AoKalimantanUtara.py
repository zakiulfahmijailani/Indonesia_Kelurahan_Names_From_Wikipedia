import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kalut():
    # KABUPATEN DAN KOTA DI KALIMANTAN UTARA
    # Kabupaten Bulungan
    url_bulungan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bulungan"
    df_bulungan = get_kelurahan_data(url_bulungan, 'Kabupaten Bulungan', 'kalimantan utara')

    # Kabupaten Malinau
    url_malinau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Malinau"
    df_malinau = get_kelurahan_data(url_malinau, 'Kabupaten Malinau', 'kalimantan utara')

    # Kabupaten Nunukan
    url_nunukan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nunukan"
    df_nunukan = get_kelurahan_data(url_nunukan, 'Kabupaten Nunukan', 'kalimantan utara')

    # Kabupaten Tana Tidung
    url_tana_tidung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tana_Tidung"
    df_tana_tidung = get_kelurahan_data(url_tana_tidung, 'Kabupaten Tana Tidung', 'kalimantan utara')

    # Kota Tarakan
    url_tarakan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tarakan"
    df_tarakan = get_kelurahan_data(url_tarakan, 'Kota Tarakan', 'kalimantan utara')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_kalimantan_utara = pd.concat([df_bulungan, df_malinau, df_nunukan, df_tana_tidung, df_tarakan], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_kalimantan_utara = df_all_kalimantan_utara.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_kalimantan_utara = df_all_kalimantan_utara[~df_all_kalimantan_utara['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_kalimantan_utara)

    # Ambil daftar kelurahan dari df_all_kalimantan_utara
    kalimantan_utara_kelurahan_list = df_all_kalimantan_utara['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    kalimantan_utara_kelurahan_list = [kelurahan + ", Kalimantan Utara, Indonesia" for kelurahan in kalimantan_utara_kelurahan_list]
    print(kalimantan_utara_kelurahan_list)

    return df_all_kalimantan_utara