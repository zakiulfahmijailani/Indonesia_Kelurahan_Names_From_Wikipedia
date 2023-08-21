import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sulawesi_tengah():
    # KABUPATEN DAN KOTA DI SULAWESI TENGAH
    # Kabupaten Banggai
    url_banggai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banggai"
    df_banggai = get_kelurahan_data(url_banggai, 'Kabupaten Banggai', 'sulawesi tengah')

    # Kabupaten Banggai Kepulauan
    url_banggai_kepulauan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banggai_Kepulauan"
    df_banggai_kepulauan = get_kelurahan_data(url_banggai_kepulauan, 'Kabupaten Banggai Kepulauan', 'sulawesi tengah')

    # Kabupaten Banggai Laut
    url_banggai_laut = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banggai_Laut"
    df_banggai_laut = get_kelurahan_data(url_banggai_laut, 'Kabupaten Banggai Laut', 'sulawesi tengah')

    # Kabupaten Buol
    url_buol = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Buol"
    df_buol = get_kelurahan_data(url_buol, 'Kabupaten Buol', 'sulawesi tengah')

    # Kabupaten Donggala
    url_donggala = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Donggala"
    df_donggala = get_kelurahan_data(url_donggala, 'Kabupaten Donggala', 'sulawesi tengah')

    # Kabupaten Morowali
    url_morowali = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Morowali"
    df_morowali = get_kelurahan_data(url_morowali, 'Kabupaten Morowali', 'sulawesi tengah')

    # Kabupaten Morowali Utara
    url_morowali_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Morowali_Utara"
    df_morowali_utara = get_kelurahan_data(url_morowali_utara, 'Kabupaten Morowali Utara', 'sulawesi tengah')

    # Kabupaten Parigi Moutong
    url_parigi_moutong = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Parigi_Moutong"
    df_parigi_moutong = get_kelurahan_data(url_parigi_moutong, 'Kabupaten Parigi Moutong', 'sulawesi tengah')

    # Kabupaten Poso
    url_poso = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Poso"
    df_poso = get_kelurahan_data(url_poso, 'Kabupaten Poso', 'sulawesi tengah')

    # Kabupaten Sigi
    url_sigi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sigi"
    df_sigi = get_kelurahan_data(url_sigi, 'Kabupaten Sigi', 'sulawesi tengah')

    # Kabupaten Tojo Una-Una
    url_tojo_una_una = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tojo_Una-Una"
    df_tojo_una_una = get_kelurahan_data(url_tojo_una_una, 'Kabupaten Tojo Una-Una', 'sulawesi tengah')

    # Kabupaten Toli-Toli
    url_toli_toli = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Toli-Toli"
    df_toli_toli = get_kelurahan_data(url_toli_toli, 'Kabupaten Toli-Toli', 'sulawesi tengah')

    # Kota Palu
    url_palu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Palu"
    df_palu = get_kelurahan_data(url_palu, 'Kota Palu', 'sulawesi tengah')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sulawesi_tengah = pd.concat([df_banggai, df_banggai_kepulauan, df_banggai_laut, df_buol, df_donggala, df_morowali,
                                    df_morowali_utara, df_parigi_moutong, df_poso, df_sigi, df_tojo_una_una,
                                    df_toli_toli, df_palu], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sulawesi_tengah = df_all_sulawesi_tengah.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sulawesi_tengah = df_all_sulawesi_tengah[~df_all_sulawesi_tengah['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sulawesi_tengah)

    # Ambil daftar kelurahan dari df_all_sulawesi_tengah
    sulawesi_tengah_kelurahan_list = df_all_sulawesi_tengah['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sulawesi_tengah_kelurahan_list = [kelurahan + ", Sulawesi Tengah, Indonesia" for kelurahan in sulawesi_tengah_kelurahan_list]
    print(sulawesi_tengah_kelurahan_list)

    return df_all_sulawesi_tengah