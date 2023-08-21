import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_riau():
    # KABUPATEN DAN KOTA DI RIAU
    # Kabupaten Bengkalis
    url_bengkalis = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bengkalis"
    df_bengkalis = get_kelurahan_data(url_bengkalis, 'Kabupaten Bengkalis', 'riau')

    # Kabupaten Indragiri Hilir
    url_indragiri_hilir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Indragiri_Hilir"
    df_indragiri_hilir = get_kelurahan_data(url_indragiri_hilir, 'Kabupaten Indragiri Hilir', 'riau')

    # Kabupaten Indragiri Hulu
    url_indragiri_hulu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Indragiri_Hulu"
    df_indragiri_hulu = get_kelurahan_data(url_indragiri_hulu, 'Kabupaten Indragiri Hulu', 'riau')

    # Kabupaten Kampar
    url_kampar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kampar"
    df_kampar = get_kelurahan_data(url_kampar, 'Kabupaten Kampar', 'riau')

    # Kabupaten Kepulauan Meranti
    url_kepulauan_meranti = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Meranti"
    df_kepulauan_meranti = get_kelurahan_data(url_kepulauan_meranti, 'Kabupaten Kepulauan Meranti', 'riau')

    # Kabupaten Kuantan Singingi
    url_kuantan_singingi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kuantan_Singingi"
    df_kuantan_singingi = get_kelurahan_data(url_kuantan_singingi, 'Kabupaten Kuantan Singingi', 'riau')

    # Kabupaten Pelalawan
    url_pelalawan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pelalawan"
    df_pelalawan = get_kelurahan_data(url_pelalawan, 'Kabupaten Pelalawan', 'riau')

    # Kabupaten Rokan Hilir
    url_rokan_hilir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Rokan_Hilir"
    df_rokan_hilir = get_kelurahan_data(url_rokan_hilir, 'Kabupaten Rokan Hilir', 'riau')

    # Kabupaten Rokan Hulu
    url_rokan_hulu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Rokan_Hulu"
    df_rokan_hulu = get_kelurahan_data(url_rokan_hulu, 'Kabupaten Rokan Hulu', 'riau')

    # Kabupaten Siak
    url_siak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Siak"
    df_siak = get_kelurahan_data(url_siak, 'Kabupaten Siak', 'riau')

    # Kota Dumai
    url_dumai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Dumai"
    df_dumai = get_kelurahan_data(url_dumai, 'Kota Dumai', 'riau')

    # Kota Pekanbaru
    url_pekanbaru = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pekanbaru"
    df_pekanbaru = get_kelurahan_data(url_pekanbaru, 'Kota Pekanbaru', 'riau')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_riau = pd.concat([df_bengkalis, df_indragiri_hilir, df_indragiri_hulu, df_kampar, df_kepulauan_meranti,
                            df_kuantan_singingi, df_pelalawan, df_rokan_hilir, df_rokan_hulu, df_siak, df_dumai,
                            df_pekanbaru], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_riau = df_all_riau.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_riau = df_all_riau[~df_all_riau['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_riau)

    # Ambil daftar kelurahan dari df_all_riau
    riau_kelurahan_list = df_all_riau['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    riau_kelurahan_list = [kelurahan + ", Riau, Indonesia" for kelurahan in riau_kelurahan_list]
    print(riau_kelurahan_list)

    return df_all_riau