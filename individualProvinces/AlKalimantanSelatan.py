import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kalsel():
    # KABUPATEN DAN KOTA DI KALIMANTAN SELATAN
    # Kabupaten Banjar
    url_banjar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banjar"
    df_banjar = get_kelurahan_data(url_banjar, 'Kabupaten Banjar', 'kalimantan selatan')

    # Kabupaten Barito Kuala
    url_barito_kuala = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Barito_Kuala"
    df_barito_kuala = get_kelurahan_data(url_barito_kuala, 'Kabupaten Barito Kuala', 'kalimantan selatan')

    # Kabupaten Hulu Sungai Selatan
    url_hulu_sungai_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Hulu_Sungai_Selatan"
    df_hulu_sungai_selatan = get_kelurahan_data(url_hulu_sungai_selatan, 'Kabupaten Hulu Sungai Selatan', 'kalimantan selatan')

    # Kabupaten Hulu Sungai Tengah
    url_hulu_sungai_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Hulu_Sungai_Tengah"
    df_hulu_sungai_tengah = get_kelurahan_data(url_hulu_sungai_tengah, 'Kabupaten Hulu Sungai Tengah', 'kalimantan selatan')

    # Kabupaten Hulu Sungai Utara
    url_hulu_sungai_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Hulu_Sungai_Utara"
    df_hulu_sungai_utara = get_kelurahan_data(url_hulu_sungai_utara, 'Kabupaten Hulu Sungai Utara', 'kalimantan selatan')

    # Kabupaten Kotabaru
    url_kotabaru = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kotabaru"
    df_kotabaru = get_kelurahan_data(url_kotabaru, 'Kabupaten Kotabaru', 'kalimantan selatan')

    # Kabupaten Tabalong
    url_tabalong = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tabalong"
    df_tabalong = get_kelurahan_data(url_tabalong, 'Kabupaten Tabalong', 'kalimantan selatan')

    # Kabupaten Tanah Bumbu
    url_tanah_bumbu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tanah_Bumbu"
    df_tanah_bumbu = get_kelurahan_data(url_tanah_bumbu, 'Kabupaten Tanah Bumbu', 'kalimantan selatan')

    # Kabupaten Tanah Laut
    url_tanah_laut = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tanah_Laut"
    df_tanah_laut = get_kelurahan_data(url_tanah_laut, 'Kabupaten Tanah Laut', 'kalimantan selatan')

    # Kabupaten Tapin
    url_tapin = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tapin"
    df_tapin = get_kelurahan_data(url_tapin, 'Kabupaten Tapin', 'kalimantan selatan')

    # Kota Banjarmasin
    url_banjarmasin = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Banjarmasin"
    df_banjarmasin = get_kelurahan_data(url_banjarmasin, 'Kota Banjarmasin', 'kalimantan selatan')

    # Kota Banjarbaru
    url_banjarbaru = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Banjarbaru"
    df_banjarbaru = get_kelurahan_data(url_banjarbaru, 'Kota Banjarbaru', 'kalimantan selatan')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_kalimantan_selatan = pd.concat([df_banjar, df_barito_kuala, df_hulu_sungai_selatan, df_hulu_sungai_tengah, df_hulu_sungai_utara,
                                        df_kotabaru, df_tabalong, df_tanah_bumbu, df_tanah_laut, df_tapin, df_banjarmasin,
                                        df_banjarbaru], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_kalimantan_selatan = df_all_kalimantan_selatan.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_kalimantan_selatan = df_all_kalimantan_selatan[~df_all_kalimantan_selatan['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_kalimantan_selatan)

    # Ambil daftar kelurahan dari df_all_kalimantan_selatan
    kalimantan_selatan_kelurahan_list = df_all_kalimantan_selatan['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    kalimantan_selatan_kelurahan_list = [kelurahan + ", Kalimantan Selatan, Indonesia" for kelurahan in kalimantan_selatan_kelurahan_list]
    print(kalimantan_selatan_kelurahan_list)

    return df_all_kalimantan_selatan