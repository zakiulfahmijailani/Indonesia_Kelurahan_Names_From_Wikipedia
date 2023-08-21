import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data


def get_df_all_jakarta():
    # KABUPATEN DAN KOTA DI DKI JAKARTA
    # Kota Administrasi Jakarta Barat
    url_jakarta_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Barat"
    df_jakarta_barat = get_kelurahan_data(url_jakarta_barat, 'Kota Administrasi Jakarta Barat', 'DKI Jakarta')

    # Kota Administrasi Jakarta Pusat
    url_jakarta_pusat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Pusat"
    df_jakarta_pusat = get_kelurahan_data(url_jakarta_pusat, 'Kota Administrasi Jakarta Pusat', 'DKI Jakarta')

    # Kota Administrasi Jakarta Selatan
    url_jakarta_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Selatan"
    df_jakarta_selatan = get_kelurahan_data(url_jakarta_selatan, 'Kota Administrasi Jakarta Selatan', 'DKI Jakarta')

    # Kota Administrasi Jakarta Timur
    url_jakarta_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Timur"
    df_jakarta_timur = get_kelurahan_data(url_jakarta_timur, 'Kota Administrasi Jakarta Timur', 'DKI Jakarta')

    # Kota Administrasi Jakarta Utara
    url_jakarta_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Administrasi_Jakarta_Utara"
    df_jakarta_utara = get_kelurahan_data(url_jakarta_utara, 'Kota Administrasi Jakarta Utara', 'DKI Jakarta')

    #GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_dki_jakarta = pd.concat([df_jakarta_barat, df_jakarta_pusat, df_jakarta_selatan,
    df_jakarta_timur, df_jakarta_utara], ignore_index=True)

    #Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_dki_jakarta = df_all_dki_jakarta.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    #Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_dki_jakarta = df_all_dki_jakarta[~df_all_dki_jakarta['kelurahan'].isin(values_to_remove)]

    #Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_dki_jakarta)

    # Ambil daftar kelurahan dari df_all_dki_jakarta
    dki_jakarta_kelurahan_list = df_all_dki_jakarta['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    dki_jakarta_kelurahan_list = [kelurahan + ", DKI Jakarta, Indonesia" for kelurahan in dki_jakarta_kelurahan_list]
    print(dki_jakarta_kelurahan_list)

    return df_all_dki_jakarta