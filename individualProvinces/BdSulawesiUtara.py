import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sulawesi_utara():
    # KABUPATEN DAN KOTA DI SULAWESI UTARA
    # Kabupaten Bolaang Mongondow
    url_bolaang_mongondow = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bolaang_Mongondow"
    df_bolaang_mongondow = get_kelurahan_data(url_bolaang_mongondow, 'Kabupaten Bolaang Mongondow', 'sulawesi utara')

    # Kabupaten Bolaang Mongondow Utara
    url_bolaang_mongondow_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bolaang_Mongondow_Utara"
    df_bolaang_mongondow_utara = get_kelurahan_data(url_bolaang_mongondow_utara, 'Kabupaten Bolaang Mongondow Utara', 'sulawesi utara')

    # Kabupaten Bolaang Mongondow Selatan
    url_bolaang_mongondow_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bolaang_Mongondow_Selatan"
    df_bolaang_mongondow_selatan = get_kelurahan_data(url_bolaang_mongondow_selatan, 'Kabupaten Bolaang Mongondow Selatan', 'sulawesi utara')

    # Kabupaten Bolaang Mongondow Timur
    url_bolaang_mongondow_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bolaang_Mongondow_Timur"
    df_bolaang_mongondow_timur = get_kelurahan_data(url_bolaang_mongondow_timur, 'Kabupaten Bolaang Mongondow Timur', 'sulawesi utara')

    # Kabupaten Kepulauan Sangihe
    url_kepulauan_sangihe = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Sangihe"
    df_kepulauan_sangihe = get_kelurahan_data(url_kepulauan_sangihe, 'Kabupaten Kepulauan Sangihe', 'sulawesi utara')

    # Kabupaten Kepulauan Siau Tagulandang Biaro
    url_kepulauan_siau_tagulandang_biaro = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Siau_Tagulandang_Biaro"
    df_kepulauan_siau_tagulandang_biaro = get_kelurahan_data(url_kepulauan_siau_tagulandang_biaro, 'Kabupaten Kepulauan Siau Tagulandang Biaro', 'sulawesi utara')

    # Kabupaten Kepulauan Talaud
    url_kepulauan_talaud = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Talaud"
    df_kepulauan_talaud = get_kelurahan_data(url_kepulauan_talaud, 'Kabupaten Kepulauan Talaud', 'sulawesi utara')

    # Kabupaten Minahasa
    url_minahasa = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Minahasa"
    df_minahasa = get_kelurahan_data(url_minahasa, 'Kabupaten Minahasa', 'sulawesi utara')

    # Kabupaten Minahasa Selatan
    url_minahasa_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Minahasa_Selatan"
    df_minahasa_selatan = get_kelurahan_data(url_minahasa_selatan, 'Kabupaten Minahasa Selatan', 'sulawesi utara')

    # Kabupaten Minahasa Utara
    url_minahasa_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Minahasa_Utara"
    df_minahasa_utara = get_kelurahan_data(url_minahasa_utara, 'Kabupaten Minahasa Utara', 'sulawesi utara')

    # Kabupaten Minahasa Tenggara
    url_minahasa_tenggara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Minahasa_Tenggara"
    df_minahasa_tenggara = get_kelurahan_data(url_minahasa_tenggara, 'Kabupaten Minahasa Tenggara', 'sulawesi utara')

    # Kota Bitung
    url_bitung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bitung"
    df_bitung = get_kelurahan_data(url_bitung, 'Kota Bitung', 'sulawesi utara')

    # Kota Kotamobagu
    url_kotamobagu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Kotamobagu"
    df_kotamobagu = get_kelurahan_data(url_kotamobagu, 'Kota Kotamobagu', 'sulawesi utara')

    # Kota Manado
    url_manado = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Manado"
    df_manado = get_kelurahan_data(url_manado, 'Kota Manado', 'sulawesi utara')

    # Kota Tomohon
    url_tomohon = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tomohon"
    df_tomohon = get_kelurahan_data(url_tomohon, 'Kota Tomohon', 'sulawesi utara')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sulawesi_utara = pd.concat([df_bolaang_mongondow, df_bolaang_mongondow_utara, df_bolaang_mongondow_selatan,
                                    df_bolaang_mongondow_timur, df_kepulauan_sangihe, df_kepulauan_siau_tagulandang_biaro,
                                    df_kepulauan_talaud, df_minahasa, df_minahasa_selatan, df_minahasa_utara,
                                    df_minahasa_tenggara, df_bitung, df_kotamobagu, df_manado, df_tomohon], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sulawesi_utara = df_all_sulawesi_utara.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sulawesi_utara = df_all_sulawesi_utara[~df_all_sulawesi_utara['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sulawesi_utara)

    # Ambil daftar kelurahan dari df_all_sulawesi_utara
    sulawesi_utara_kelurahan_list = df_all_sulawesi_utara['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sulawesi_utara_kelurahan_list = [kelurahan + ", Sulawesi Utara, Indonesia" for kelurahan in sulawesi_utara_kelurahan_list]
    print(sulawesi_utara_kelurahan_list)

    return df_all_sulawesi_utara