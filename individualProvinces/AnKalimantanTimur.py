import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kaltim():
    # KABUPATEN DAN KOTA DI KALIMANTAN TIMUR
    # Kabupaten Berau
    url_berau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Berau"
    df_berau = get_kelurahan_data(url_berau, 'Kabupaten Berau', 'kalimantan timur')

    # Kabupaten Kutai Barat
    url_kutai_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kutai_Barat"
    df_kutai_barat = get_kelurahan_data(url_kutai_barat, 'Kabupaten Kutai Barat', 'kalimantan timur')

    # Kabupaten Kutai Kartanegara
    url_kutai_kartanegara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kutai_Kartanegara"
    df_kutai_kartanegara = get_kelurahan_data(url_kutai_kartanegara, 'Kabupaten Kutai Kartanegara', 'kalimantan timur')

    # Kabupaten Kutai Timur
    url_kutai_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kutai_Timur"
    df_kutai_timur = get_kelurahan_data(url_kutai_timur, 'Kabupaten Kutai Timur', 'kalimantan timur')

    # Kabupaten Mahakam Ulu
    url_mahakam_ulu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mahakam_Ulu"
    df_mahakam_ulu = get_kelurahan_data(url_mahakam_ulu, 'Kabupaten Mahakam Ulu', 'kalimantan timur')

    # Kabupaten Paser
    url_paser = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Paser"
    df_paser = get_kelurahan_data(url_paser, 'Kabupaten Paser', 'kalimantan timur')

    # Kabupaten Penajam Paser Utara
    url_penajam_paser_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Penajam_Paser_Utara"
    df_penajam_paser_utara = get_kelurahan_data(url_penajam_paser_utara, 'Kabupaten Penajam Paser Utara', 'kalimantan timur')

    # Kota Balikpapan
    url_balikpapan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Balikpapan"
    df_balikpapan = get_kelurahan_data(url_balikpapan, 'Kota Balikpapan', 'kalimantan timur')

    # Kota Bontang
    url_bontang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bontang"
    df_bontang = get_kelurahan_data(url_bontang, 'Kota Bontang', 'kalimantan timur')

    # Kota Samarinda
    url_samarinda = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Samarinda"
    df_samarinda = get_kelurahan_data(url_samarinda, 'Kota Samarinda', 'kalimantan timur')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_kalimantan_timur = pd.concat([df_berau, df_kutai_barat, df_kutai_kartanegara, df_kutai_timur, df_mahakam_ulu,
                                        df_paser, df_penajam_paser_utara, df_balikpapan, df_bontang, df_samarinda], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_kalimantan_timur = df_all_kalimantan_timur.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_kalimantan_timur = df_all_kalimantan_timur[~df_all_kalimantan_timur['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_kalimantan_timur)

    # Ambil daftar kelurahan dari df_all_kalimantan_timur
    kalimantan_timur_kelurahan_list = df_all_kalimantan_timur['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    kalimantan_timur_kelurahan_list = [kelurahan + ", Kalimantan Timur, Indonesia" for kelurahan in kalimantan_timur_kelurahan_list]
    print(kalimantan_timur_kelurahan_list)

    return df_all_kalimantan_timur