import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kepri():
    # KABUPATEN DAN KOTA DI KEPULAUAN RIAU
    # Kabupaten Bintan
    url_bintan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bintan"
    df_bintan = get_kelurahan_data(url_bintan, 'Kabupaten Bintan', 'kepulauan riau')

    # Kabupaten Karimun
    url_karimun = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Karimun"
    df_karimun = get_kelurahan_data(url_karimun, 'Kabupaten Karimun', 'kepulauan riau')

    # Kabupaten Lingga
    url_lingga = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lingga"
    df_lingga = get_kelurahan_data(url_lingga, 'Kabupaten Lingga', 'kepulauan riau')

    # Kabupaten Natuna
    url_natuna = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Natuna"
    df_natuna = get_kelurahan_data(url_natuna, 'Kabupaten Natuna', 'kepulauan riau')

    # Kota Batam
    url_batam = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Batam"
    df_batam = get_kelurahan_data(url_batam, 'Kota Batam', 'kepulauan riau')

    # Kota Tanjungpinang
    url_tanjungpinang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tanjungpinang"
    df_tanjungpinang = get_kelurahan_data(url_tanjungpinang, 'Kota Tanjungpinang', 'kepulauan riau')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_kepulauan_riau = pd.concat([df_bintan, df_karimun, df_lingga, df_natuna,
                                    df_batam, df_tanjungpinang], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_kepulauan_riau = df_all_kepulauan_riau.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_kepulauan_riau = df_all_kepulauan_riau[~df_all_kepulauan_riau['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_kepulauan_riau)

    # Ambil daftar kelurahan dari df_all_kepulauan_riau
    kepulauan_riau_kelurahan_list = df_all_kepulauan_riau['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    kepulauan_riau_kelurahan_list = [kelurahan + ", Kepulauan Riau, Indonesia" for kelurahan in kepulauan_riau_kelurahan_list]
    print(kepulauan_riau_kelurahan_list)

    return df_all_kepulauan_riau