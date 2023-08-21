import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_gorontalo():
    # KABUPATEN DAN KOTA DI GORONTALO
    # Kabupaten Boalemo
    url_boalemo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Boalemo"
    df_boalemo = get_kelurahan_data(url_boalemo, 'Kabupaten Boalemo', 'Gorontalo')

    # Kabupaten Bone Bolango
    url_bone_bolango = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bone_Bolango"
    df_bone_bolango = get_kelurahan_data(url_bone_bolango, 'Kabupaten Bone Bolango', 'Gorontalo')

    # Kabupaten Gorontalo
    url_gorontalo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gorontalo"
    df_gorontalo = get_kelurahan_data(url_gorontalo, 'Kabupaten Gorontalo', 'Gorontalo')

    # Kabupaten Gorontalo Utara
    url_gorontalo_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gorontalo_Utara"
    df_gorontalo_utara = get_kelurahan_data(url_gorontalo_utara, 'Kabupaten Gorontalo Utara', 'Gorontalo')

    # Kabupaten Pohuwato
    url_pohuwato = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pohuwato"
    df_pohuwato = get_kelurahan_data(url_pohuwato, 'Kabupaten Pohuwato', 'Gorontalo')

    # Kota Gorontalo
    url_gorontalo_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Gorontalo"
    df_gorontalo_kota = get_kelurahan_data(url_gorontalo_kota, 'Kota Gorontalo', 'Gorontalo')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_gorontalo = pd.concat([df_boalemo, df_bone_bolango, df_gorontalo, df_gorontalo_utara,
                                df_pohuwato, df_gorontalo_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_gorontalo = df_all_gorontalo.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_gorontalo = df_all_gorontalo[~df_all_gorontalo['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_gorontalo)

    # Ambil daftar kelurahan dari df_all_gorontalo
    gorontalo_kelurahan_list = df_all_gorontalo['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    gorontalo_kelurahan_list = [kelurahan + ", Gorontalo, Indonesia" for kelurahan in gorontalo_kelurahan_list]
    print(gorontalo_kelurahan_list)

    return df_all_gorontalo