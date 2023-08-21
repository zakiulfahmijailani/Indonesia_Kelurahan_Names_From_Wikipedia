import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kepulauan_bangka_belitung():
    # KABUPATEN DAN KOTA DI KEPULAUAN BANGKA BELITUNG
    # Kabupaten Bangka
    url_bangka = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bangka"
    df_bangka = get_kelurahan_data(url_bangka, 'Kabupaten Bangka', 'kepulauan bangka belitung')

    # Kabupaten Bangka Barat
    url_bangka_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bangka_Barat"
    df_bangka_barat = get_kelurahan_data(url_bangka_barat, 'Kabupaten Bangka Barat', 'kepulauan bangka belitung')

    # Kabupaten Bangka Selatan
    url_bangka_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bangka_Selatan"
    df_bangka_selatan = get_kelurahan_data(url_bangka_selatan, 'Kabupaten Bangka Selatan', 'kepulauan bangka belitung')

    # Kabupaten Bangka Tengah
    url_bangka_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bangka_Tengah"
    df_bangka_tengah = get_kelurahan_data(url_bangka_tengah, 'Kabupaten Bangka Tengah', 'kepulauan bangka belitung')

    # Kabupaten Belitung
    url_belitung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Belitung"
    df_belitung = get_kelurahan_data(url_belitung, 'Kabupaten Belitung', 'kepulauan bangka belitung')

    # Kabupaten Belitung Timur
    url_belitung_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Belitung_Timur"
    df_belitung_timur = get_kelurahan_data(url_belitung_timur, 'Kabupaten Belitung Timur', 'kepulauan bangka belitung')

    # Kota Pangkal Pinang
    url_pangkal_pinang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pangkal_Pinang"
    df_pangkal_pinang = get_kelurahan_data(url_pangkal_pinang, 'Kota Pangkal Pinang', 'kepulauan bangka belitung')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_bangka_belitung = pd.concat([df_bangka, df_bangka_barat, df_bangka_selatan, df_bangka_tengah,
                                    df_belitung, df_belitung_timur, df_pangkal_pinang], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_bangka_belitung = df_all_bangka_belitung.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_bangka_belitung = df_all_bangka_belitung[~df_all_bangka_belitung['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_bangka_belitung)

    # Ambil daftar kelurahan dari df_all_bangka_belitung
    bangka_belitung_kelurahan_list = df_all_bangka_belitung['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    bangka_belitung_kelurahan_list = [kelurahan + ", Kepulauan Bangka Belitung, Indonesia" for kelurahan in bangka_belitung_kelurahan_list]
    print(bangka_belitung_kelurahan_list)

    return df_all_bangka_belitung