import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_bali():
    # KABUPATEN DAN KOTA DI BALI
    # Kabupaten Badung
    url_badung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Badung"
    df_badung = get_kelurahan_data(url_badung, 'Kabupaten Badung', 'Bali')

    # Kabupaten Bangli
    url_bangli = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bangli"
    df_bangli = get_kelurahan_data(url_bangli, 'Kabupaten Bangli', 'Bali')

    # Kabupaten Buleleng
    url_buleleng = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Buleleng"
    df_buleleng = get_kelurahan_data(url_buleleng, 'Kabupaten Buleleng', 'Bali')

    # Kabupaten Gianyar
    url_gianyar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gianyar"
    df_gianyar = get_kelurahan_data(url_gianyar, 'Kabupaten Gianyar', 'Bali')

    # Kabupaten Jembrana
    url_jembrana = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jembrana"
    df_jembrana = get_kelurahan_data(url_jembrana, 'Kabupaten Jembrana', 'Bali')

    # Kabupaten Karangasem
    url_karangasem = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Karangasem"
    df_karangasem = get_kelurahan_data(url_karangasem, 'Kabupaten Karangasem', 'Bali')

    # Kabupaten Klungkung
    url_klungkung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Klungkung"
    df_klungkung = get_kelurahan_data(url_klungkung, 'Kabupaten Klungkung', 'Bali')

    # Kabupaten Tabanan
    url_tabanan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tabanan"
    df_tabanan = get_kelurahan_data(url_tabanan, 'Kabupaten Tabanan', 'Bali')

    # Kota Denpasar
    url_denpasar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Denpasar"
    df_denpasar = get_kelurahan_data(url_denpasar, 'Kota Denpasar', 'Bali')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_bali = pd.concat([df_badung, df_bangli, df_buleleng, df_gianyar, df_jembrana,
                            df_karangasem, df_klungkung, df_tabanan, df_denpasar], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_bali = df_all_bali.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_bali = df_all_bali[~df_all_bali['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_bali)

    # Ambil daftar kelurahan dari df_all_bali
    bali_kelurahan_list = df_all_bali['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    bali_kelurahan_list = [kelurahan + ", Bali, Indonesia" for kelurahan in bali_kelurahan_list]
    print(bali_kelurahan_list)

    return df_all_bali