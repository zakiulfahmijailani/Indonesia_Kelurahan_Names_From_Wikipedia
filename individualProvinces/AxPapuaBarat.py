import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_papua_barat():
    # KABUPATEN DAN KOTA DI PAPUA BARAT
    # Kabupaten Fakfak
    url_fakfak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Fakfak"
    df_fakfak = get_kelurahan_data(url_fakfak, 'Kabupaten Fakfak', 'papua barat')

    # Kabupaten Kaimana
    url_kaimana = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kaimana"
    df_kaimana = get_kelurahan_data(url_kaimana, 'Kabupaten Kaimana', 'papua barat')

    # Kabupaten Manokwari
    url_manokwari = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Manokwari"
    df_manokwari = get_kelurahan_data(url_manokwari, 'Kabupaten Manokwari', 'papua barat')

    # Kabupaten Manokwari Selatan
    url_manokwari_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Manokwari_Selatan"
    df_manokwari_selatan = get_kelurahan_data(url_manokwari_selatan, 'Kabupaten Manokwari Selatan', 'papua barat')

    # Kabupaten Maybrat
    url_maybrat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Maybrat"
    df_maybrat = get_kelurahan_data(url_maybrat, 'Kabupaten Maybrat', 'papua barat')

    # Kabupaten Pegunungan Arfak
    url_peg_arfak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pegunungan_Arfak"
    df_peg_arfak = get_kelurahan_data(url_peg_arfak, 'Kabupaten Pegunungan Arfak', 'papua barat')

    # Kabupaten Raja Ampat
    url_raja_ampat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Raja_Ampat"
    df_raja_ampat = get_kelurahan_data(url_raja_ampat, 'Kabupaten Raja Ampat', 'papua barat')

    # Kabupaten Sorong
    url_sorong = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sorong"
    df_sorong = get_kelurahan_data(url_sorong, 'Kabupaten Sorong', 'papua barat')

    # Kabupaten Sorong Selatan
    url_sorong_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sorong_Selatan"
    df_sorong_selatan = get_kelurahan_data(url_sorong_selatan, 'Kabupaten Sorong Selatan', 'papua barat')

    # Kabupaten Tambrauw
    url_tambrauw = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tambrauw"
    df_tambrauw = get_kelurahan_data(url_tambrauw, 'Kabupaten Tambrauw', 'papua barat')

    # Kabupaten Teluk Bintuni
    url_teluk_bintuni = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Teluk_Bintuni"
    df_teluk_bintuni = get_kelurahan_data(url_teluk_bintuni, 'Kabupaten Teluk Bintuni', 'papua barat')

    # Kabupaten Teluk Wondama
    url_teluk_wondama = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Teluk_Wondama"
    df_teluk_wondama = get_kelurahan_data(url_teluk_wondama, 'Kabupaten Teluk Wondama', 'papua barat')

    # Kota Sorong
    url_sorong_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Sorong"
    df_sorong_kota = get_kelurahan_data(url_sorong_kota, 'Kota Sorong', 'papua barat')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_papua_barat = pd.concat([df_fakfak, df_kaimana, df_manokwari, df_manokwari_selatan, df_maybrat,
                                df_peg_arfak, df_raja_ampat, df_sorong, df_sorong_selatan, df_tambrauw,
                                df_teluk_bintuni, df_teluk_wondama, df_sorong_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_papua_barat = df_all_papua_barat.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_papua_barat = df_all_papua_barat[~df_all_papua_barat['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_papua_barat)

    # Ambil daftar kelurahan dari df_all_papua_barat
    papua_barat_kelurahan_list = df_all_papua_barat['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    papua_barat_kelurahan_list = [kelurahan + ", Papua Barat, Indonesia" for kelurahan in papua_barat_kelurahan_list]
    print(papua_barat_kelurahan_list)

    return df_all_papua_barat