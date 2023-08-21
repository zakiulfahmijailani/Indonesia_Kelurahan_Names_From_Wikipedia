
import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_banten():
    # KABUPATEN DAN KOTA DI BANTEN
    # Kabupaten Lebak
    url_lebak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lebak"
    df_lebak = get_kelurahan_data(url_lebak, 'Kabupaten Lebak', 'Banten')

    # Kabupaten Pandeglang
    url_pandeglang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pandeglang"
    df_pandeglang = get_kelurahan_data(url_pandeglang, 'Kabupaten Pandeglang', 'Banten')

    # Kabupaten Serang
    url_serang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Serang"
    df_serang = get_kelurahan_data(url_serang, 'Kabupaten Serang', 'Banten')

    # Kabupaten Tangerang
    url_tangerang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tangerang"
    df_tangerang = get_kelurahan_data(url_tangerang, 'Kabupaten Tangerang', 'Banten')

    # Kota Cilegon
    url_cilegon = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Cilegon"
    df_cilegon = get_kelurahan_data(url_cilegon, 'Kota Cilegon', 'Banten')

    # Kota Serang
    url_kota_serang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Serang"
    df_kota_serang = get_kelurahan_data(url_kota_serang, 'Kota Serang', 'Banten')

    # Kota Tangerang
    url_kota_tangerang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tangerang"
    df_kota_tangerang = get_kelurahan_data(url_kota_tangerang, 'Kota Tangerang', 'Banten')

    # Kota Tangerang Selatan
    url_tangerang_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tangerang_Selatan"
    df_tangerang_selatan = get_kelurahan_data(url_tangerang_selatan, 'Kota Tangerang Selatan', 'Banten')
    
    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_banten = pd.concat([df_lebak, df_pandeglang, df_serang, df_tangerang,
                            df_cilegon, df_kota_serang, df_kota_tangerang, df_tangerang_selatan],
                            ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_banten = df_all_banten.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_banten = df_all_banten[~df_all_banten['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_banten)

    # Ambil daftar kelurahan dari df_all_banten
    banten_kelurahan_list = df_all_banten['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    banten_kelurahan_list = [kelurahan + ", Banten, Indonesia" for kelurahan in banten_kelurahan_list]
    print(banten_kelurahan_list)

    return df_all_banten