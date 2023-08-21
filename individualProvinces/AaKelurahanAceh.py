import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_aceh():
    url_aceh_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Barat"
    df_aceh_barat = get_kelurahan_data(url_aceh_barat, 'Kabupaten Aceh Barat', 'Aceh')

    # Kabupaten Aceh Barat Daya
    url_aceh_barat_daya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Barat_Daya"
    df_aceh_barat_daya = get_kelurahan_data(url_aceh_barat_daya, 'Kabupaten Aceh Barat Daya', 'Aceh')

    # Kabupaten Aceh Besar
    url_aceh_besar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Besar"
    df_aceh_besar = get_kelurahan_data(url_aceh_besar, 'Kabupaten Aceh Besar', 'Aceh')

    # Kabupaten Aceh Jaya
    url_aceh_jaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Jaya"
    df_aceh_jaya = get_kelurahan_data(url_aceh_jaya, 'Kabupaten Aceh Jaya', 'Aceh')

    # Kabupaten Aceh Selatan
    url_aceh_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Selatan"
    df_aceh_selatan = get_kelurahan_data(url_aceh_selatan, 'Kabupaten Aceh Selatan', 'Aceh')

    # Kabupaten Aceh Singkil
    url_aceh_singkil = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Singkil"
    df_aceh_singkil = get_kelurahan_data(url_aceh_singkil, 'Kabupaten Aceh Singkil', 'Aceh')

    # Kabupaten Aceh Tamiang
    url_aceh_tamiang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Tamiang"
    df_aceh_tamiang = get_kelurahan_data(url_aceh_tamiang, 'Kabupaten Aceh Tamiang', 'Aceh')

    # Kabupaten Aceh Tengah
    url_aceh_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Tengah"
    df_aceh_tengah = get_kelurahan_data(url_aceh_tengah, 'Kabupaten Aceh Tengah', 'Aceh')

    # Kabupaten Aceh Tenggara
    url_aceh_tenggara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Tenggara"
    df_aceh_tenggara = get_kelurahan_data(url_aceh_tenggara, 'Kabupaten Aceh Tenggara', 'Aceh')

    # Kabupaten Aceh Timur
    url_aceh_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Timur"
    df_aceh_timur = get_kelurahan_data(url_aceh_timur, 'Kabupaten Aceh Timur', 'Aceh')

    # Kabupaten Aceh Utara
    url_aceh_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Aceh_Utara"
    df_aceh_utara = get_kelurahan_data(url_aceh_utara, 'Kabupaten Aceh Utara', 'Aceh')

    # Kabupaten Bener Meriah
    url_bener_meriah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bener_Meriah"
    df_bener_meriah = get_kelurahan_data(url_bener_meriah, 'Kabupaten Bener Meriah', 'Aceh')

    # Kabupaten Bireuen
    url_bireuen = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bireuen"
    df_bireuen = get_kelurahan_data(url_bireuen, 'Kabupaten Bireuen', 'Aceh')

    # Kabupaten Gayo Lues
    url_gayo_lues = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gayo_Lues"
    df_gayo_lues = get_kelurahan_data(url_gayo_lues, 'Kabupaten Gayo Lues', 'Aceh')

    # Kabupaten Nagan Raya
    url_nagan_raya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nagan_Raya"
    df_nagan_raya = get_kelurahan_data(url_nagan_raya, 'Kabupaten Nagan Raya', 'Aceh')

    # Kabupaten Pidie
    url_pidie = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pidie"
    df_pidie = get_kelurahan_data(url_pidie, 'Kabupaten Pidie', 'Aceh')

    # Kabupaten Pidie Jaya
    url_pidie_jaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pidie_Jaya"
    df_pidie_jaya = get_kelurahan_data(url_pidie_jaya, 'Kabupaten Pidie Jaya', 'Aceh')

    # Kabupaten Simeulue
    url_simeulue = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Simeulue"
    df_simeulue = get_kelurahan_data(url_simeulue, 'Kabupaten Simeulue', 'Aceh')

    # Kota Banda Aceh
    url_banda_aceh = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Banda_Aceh"
    df_banda_aceh = get_kelurahan_data(url_banda_aceh, 'Kota Banda Aceh', 'Aceh')

    # Kota Langsa
    url_langsa = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Langsa"
    df_langsa = get_kelurahan_data(url_langsa, 'Kota Langsa', 'Aceh')

    # Kota Lhokseumawe
    url_lhokseumawe = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Lhokseumawe"
    df_lhokseumawe = get_kelurahan_data(url_lhokseumawe, 'Kota Lhokseumawe', 'Aceh')

    # Kota Sabang
    url_sabang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Sabang"
    df_sabang = get_kelurahan_data(url_sabang, 'Kota Sabang', 'Aceh')

    # Kota Subulussalam
    url_subulussalam = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Subulussalam"
    df_subulussalam = get_kelurahan_data(url_subulussalam, 'Kota Subulussalam', 'Aceh')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_aceh = pd.concat([df_aceh_barat, df_aceh_barat_daya, df_aceh_besar, df_aceh_jaya, df_aceh_selatan,
                            df_aceh_singkil, df_aceh_tamiang, df_aceh_tengah, df_aceh_tenggara, df_aceh_timur,
                            df_aceh_utara, df_bener_meriah, df_bireuen, df_gayo_lues, df_nagan_raya, df_pidie,
                            df_pidie_jaya, df_simeulue, df_banda_aceh, df_langsa, df_lhokseumawe, df_sabang,
                            df_subulussalam], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_aceh = df_all_aceh.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_aceh = df_all_aceh[~df_all_aceh['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_aceh)

    # Ambil daftar kelurahan dari df_all_aceh
    aceh_kelurahan_list = df_all_aceh['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    aceh_kelurahan_list = [kelurahan + ", Aceh, Indonesia" for kelurahan in aceh_kelurahan_list]
    print(aceh_kelurahan_list)

    return df_all_aceh
