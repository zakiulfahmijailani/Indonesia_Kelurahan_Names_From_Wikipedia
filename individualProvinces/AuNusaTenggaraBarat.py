import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_ntb():
    # KABUPATEN DAN KOTA DI NUSA TENGGARA BARAT
    # Kabupaten Bima
    url_bima = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bima"
    df_bima = get_kelurahan_data(url_bima, 'Kabupaten Bima', 'nusa tenggara barat')

    # Kabupaten Dompu
    url_dompu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Dompu"
    df_dompu = get_kelurahan_data(url_dompu, 'Kabupaten Dompu', 'nusa tenggara barat')

    # Kabupaten Lombok Barat
    url_lombok_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lombok_Barat"
    df_lombok_barat = get_kelurahan_data(url_lombok_barat, 'Kabupaten Lombok Barat', 'nusa tenggara barat')

    # Kabupaten Lombok Tengah
    url_lombok_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lombok_Tengah"
    df_lombok_tengah = get_kelurahan_data(url_lombok_tengah, 'Kabupaten Lombok Tengah', 'nusa tenggara barat')

    # Kabupaten Lombok Timur
    url_lombok_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lombok_Timur"
    df_lombok_timur = get_kelurahan_data(url_lombok_timur, 'Kabupaten Lombok Timur', 'nusa tenggara barat')

    # Kabupaten Sumbawa
    url_sumbawa = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumbawa"
    df_sumbawa = get_kelurahan_data(url_sumbawa, 'Kabupaten Sumbawa', 'nusa tenggara barat')

    # Kabupaten Sumbawa Barat
    url_sumbawa_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumbawa_Barat"
    df_sumbawa_barat = get_kelurahan_data(url_sumbawa_barat, 'Kabupaten Sumbawa Barat', 'nusa tenggara barat')

    # Kota Bima
    url_bima_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bima"
    df_bima_kota = get_kelurahan_data(url_bima_kota, 'Kota Bima', 'nusa tenggara barat')

    # Kota Mataram
    url_mataram = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Mataram"
    df_mataram = get_kelurahan_data(url_mataram, 'Kota Mataram', 'nusa tenggara barat')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_ntb = pd.concat([df_bima, df_dompu, df_lombok_barat, df_lombok_tengah, df_lombok_timur,
                            df_sumbawa, df_sumbawa_barat, df_bima_kota, df_mataram], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_ntb = df_all_ntb.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_ntb = df_all_ntb[~df_all_ntb['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_ntb)

    # Ambil daftar kelurahan dari df_all_ntb
    ntb_kelurahan_list = df_all_ntb['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    ntb_kelurahan_list = [kelurahan + ", Nusa Tenggara Barat, Indonesia" for kelurahan in ntb_kelurahan_list]
    print(ntb_kelurahan_list)

    return df_all_ntb