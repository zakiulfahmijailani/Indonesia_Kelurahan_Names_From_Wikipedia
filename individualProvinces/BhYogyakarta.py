import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_Yogyakarta():
    # KABUPATEN DAN KOTA DI YOGYAKARTA
    # Kota Yogyakarta
    url_yogyakarta = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Yogyakarta"
    df_yogyakarta = get_kelurahan_data(url_yogyakarta, 'Kota Yogyakarta', 'yogyakarta')

    # Kabupaten Bantul
    url_bantul = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bantul"
    df_bantul = get_kelurahan_data(url_bantul, 'Kabupaten Bantul', 'yogyakarta')

    # Kabupaten Gunung Kidul
    url_gunung_kidul = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gunung_Kidul"
    df_gunung_kidul = get_kelurahan_data(url_gunung_kidul, 'Kabupaten Gunung Kidul', 'yogyakarta')

    # Kabupaten Kulon Progo
    url_kulon_progo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kulon_Progo"
    df_kulon_progo = get_kelurahan_data(url_kulon_progo, 'Kabupaten Kulon Progo', 'yogyakarta')

    # Kabupaten Sleman
    url_sleman = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sleman"
    df_sleman = get_kelurahan_data(url_sleman, 'Kabupaten Sleman', 'yogyakarta')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_yogyakarta = pd.concat([df_yogyakarta, df_bantul, df_gunung_kidul, df_kulon_progo, df_sleman], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_yogyakarta = df_all_yogyakarta.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_yogyakarta = df_all_yogyakarta[~df_all_yogyakarta['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_yogyakarta)

    # Ambil daftar kelurahan dari df_all_yogyakarta
    yogyakarta_kelurahan_list = df_all_yogyakarta['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    yogyakarta_kelurahan_list = [kelurahan + ", Yogyakarta, Indonesia" for kelurahan in yogyakarta_kelurahan_list]
    print(yogyakarta_kelurahan_list)

    return df_all_yogyakarta