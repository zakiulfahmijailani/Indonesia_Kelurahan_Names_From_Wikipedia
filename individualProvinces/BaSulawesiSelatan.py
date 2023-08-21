import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sulawesi_selatan():
    # KABUPATEN DAN KOTA DI SULAWESI SELATAN
    # Kabupaten Bantaeng
    url_bantaeng = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bantaeng"
    df_bantaeng = get_kelurahan_data(url_bantaeng, 'Kabupaten Bantaeng', 'sulawesi selatan')

    # Kabupaten Barru
    url_barru = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Barru"
    df_barru = get_kelurahan_data(url_barru, 'Kabupaten Barru', 'sulawesi selatan')

    # Kabupaten Bone
    url_bone = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bone"
    df_bone = get_kelurahan_data(url_bone, 'Kabupaten Bone', 'sulawesi selatan')

    # Kabupaten Bulukumba
    url_bulukumba = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bulukumba"
    df_bulukumba = get_kelurahan_data(url_bulukumba, 'Kabupaten Bulukumba', 'sulawesi selatan')

    # Kabupaten Enrekang
    url_enrekang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Enrekang"
    df_enrekang = get_kelurahan_data(url_enrekang, 'Kabupaten Enrekang', 'sulawesi selatan')

    # Kabupaten Gowa
    url_gowa = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gowa"
    df_gowa = get_kelurahan_data(url_gowa, 'Kabupaten Gowa', 'sulawesi selatan')

    # Kabupaten Jeneponto
    url_jeneponto = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jeneponto"
    df_jeneponto = get_kelurahan_data(url_jeneponto, 'Kabupaten Jeneponto', 'sulawesi selatan')

    # Kabupaten Kepulauan Selayar
    url_selayar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Selayar"
    df_selayar = get_kelurahan_data(url_selayar, 'Kabupaten Kepulauan Selayar', 'sulawesi selatan')

    # Kabupaten Luwu
    url_luwu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Luwu"
    df_luwu = get_kelurahan_data(url_luwu, 'Kabupaten Luwu', 'sulawesi selatan')

    # Kabupaten Luwu Timur
    url_luwu_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Luwu_Timur"
    df_luwu_timur = get_kelurahan_data(url_luwu_timur, 'Kabupaten Luwu Timur', 'sulawesi selatan')

    # Kabupaten Luwu Utara
    url_luwu_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Luwu_Utara"
    df_luwu_utara = get_kelurahan_data(url_luwu_utara, 'Kabupaten Luwu Utara', 'sulawesi selatan')

    # Kabupaten Maros
    url_maros = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Maros"
    df_maros = get_kelurahan_data(url_maros, 'Kabupaten Maros', 'sulawesi selatan')

    # Kabupaten Pangkajene Dan Kepulauan
    url_pangkep = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pangkajene_Dan_Kepulauan"
    df_pangkep = get_kelurahan_data(url_pangkep, 'Kabupaten Pangkajene Dan Kepulauan', 'sulawesi selatan')

    # Kabupaten Pinrang
    url_pinrang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pinrang"
    df_pinrang = get_kelurahan_data(url_pinrang, 'Kabupaten Pinrang', 'sulawesi selatan')

    # Kabupaten Sidenreng Rappang
    url_sidenreng_rappang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sidenreng_Rappang"
    df_sidenreng_rappang = get_kelurahan_data(url_sidenreng_rappang, 'Kabupaten Sidenreng Rappang', 'sulawesi selatan')

    # Kabupaten Sinjai
    url_sinjai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sinjai"
    df_sinjai = get_kelurahan_data(url_sinjai, 'Kabupaten Sinjai', 'sulawesi selatan')

    # Kabupaten Soppeng
    url_soppeng = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Soppeng"
    df_soppeng = get_kelurahan_data(url_soppeng, 'Kabupaten Soppeng', 'sulawesi selatan')

    # Kabupaten Takalar
    url_takalar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Takalar"
    df_takalar = get_kelurahan_data(url_takalar, 'Kabupaten Takalar', 'sulawesi selatan')

    # Kabupaten Tana Toraja
    url_tana_toraja = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tana_Toraja"
    df_tana_toraja = get_kelurahan_data(url_tana_toraja, 'Kabupaten Tana Toraja', 'sulawesi selatan')

    # Kabupaten Toraja Utara
    url_toraja_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Toraja_Utara"
    df_toraja_utara = get_kelurahan_data(url_toraja_utara, 'Kabupaten Toraja Utara', 'sulawesi selatan')

    # Kabupaten Wajo
    url_wajo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Wajo"
    df_wajo = get_kelurahan_data(url_wajo, 'Kabupaten Wajo', 'sulawesi selatan')

    # Kota Makassar
    url_makassar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Makassar"
    df_makassar = get_kelurahan_data(url_makassar, 'Kota Makassar', 'sulawesi selatan')

    # Kota Palopo
    url_palopo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Palopo"
    df_palopo = get_kelurahan_data(url_palopo, 'Kota Palopo', 'sulawesi selatan')

    # Kota Parepare
    url_parepare = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Parepare"
    df_parepare = get_kelurahan_data(url_parepare, 'Kota Parepare', 'sulawesi selatan')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sulawesi_selatan = pd.concat([df_bantaeng, df_barru, df_bone, df_bulukumba, df_enrekang, df_gowa, df_jeneponto,
                                        df_selayar, df_luwu, df_luwu_timur, df_luwu_utara, df_maros, df_pangkep,
                                        df_pinrang, df_sidenreng_rappang, df_sinjai, df_soppeng, df_takalar,
                                        df_tana_toraja, df_toraja_utara, df_wajo, df_makassar, df_palopo,
                                        df_parepare], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sulawesi_selatan = df_all_sulawesi_selatan.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sulawesi_selatan = df_all_sulawesi_selatan[~df_all_sulawesi_selatan['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sulawesi_selatan)

    # Ambil daftar kelurahan dari df_all_sulawesi_selatan
    sulawesi_selatan_kelurahan_list = df_all_sulawesi_selatan['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sulawesi_selatan_kelurahan_list = [kelurahan + ", Sulawesi Selatan, Indonesia" for kelurahan in sulawesi_selatan_kelurahan_list]
    print(sulawesi_selatan_kelurahan_list)

    return df_all_sulawesi_selatan