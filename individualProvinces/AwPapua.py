import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_papua():
    # KABUPATEN DAN KOTA DI PAPUA
    # Kabupaten Asmat
    url_asmat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Asmat"
    df_asmat = get_kelurahan_data(url_asmat, 'Kabupaten Asmat', 'papua')

    # Kabupaten Biak Numfor
    url_biak_numfor = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Biak_Numfor"
    df_biak_numfor = get_kelurahan_data(url_biak_numfor, 'Kabupaten Biak Numfor', 'papua')

    # Kabupaten Boven Digoel
    url_boven_digoel = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Boven_Digoel"
    df_boven_digoel = get_kelurahan_data(url_boven_digoel, 'Kabupaten Boven Digoel', 'papua')

    # Kabupaten Deiyai
    url_deiyai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Deiyai"
    df_deiyai = get_kelurahan_data(url_deiyai, 'Kabupaten Deiyai', 'papua')

    # Kabupaten Dogiyai
    url_dogiyai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Dogiyai"
    df_dogiyai = get_kelurahan_data(url_dogiyai, 'Kabupaten Dogiyai', 'papua')

    # Kabupaten Intan Jaya
    url_intan_jaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Intan_Jaya"
    df_intan_jaya = get_kelurahan_data(url_intan_jaya, 'Kabupaten Intan Jaya', 'papua')

    # Kabupaten Jayapura
    url_jayapura = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jayapura"
    df_jayapura = get_kelurahan_data(url_jayapura, 'Kabupaten Jayapura', 'papua')

    # Kabupaten Jayawijaya
    url_jayawijaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jayawijaya"
    df_jayawijaya = get_kelurahan_data(url_jayawijaya, 'Kabupaten Jayawijaya', 'papua')

    # Kabupaten Keerom
    url_keerom = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Keerom"
    df_keerom = get_kelurahan_data(url_keerom, 'Kabupaten Keerom', 'papua')

    # Kabupaten Kepulauan Yapen
    url_kepulauan_yapen = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Yapen"
    df_kepulauan_yapen = get_kelurahan_data(url_kepulauan_yapen, 'Kabupaten Kepulauan Yapen', 'papua')

    # Kabupaten Lanny Jaya
    url_lanny_jaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lanny_Jaya"
    df_lanny_jaya = get_kelurahan_data(url_lanny_jaya, 'Kabupaten Lanny Jaya', 'papua')

    # Kabupaten Mamberamo Raya
    url_mamberamo_raya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mamberamo_Raya"
    df_mamberamo_raya = get_kelurahan_data(url_mamberamo_raya, 'Kabupaten Mamberamo Raya', 'papua')

    # Kabupaten Mamberamo Tengah
    url_mamberamo_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mamberamo_Tengah"
    df_mamberamo_tengah = get_kelurahan_data(url_mamberamo_tengah, 'Kabupaten Mamberamo Tengah', 'papua')

    # Kabupaten Mappi
    url_mappi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mappi"
    df_mappi = get_kelurahan_data(url_mappi, 'Kabupaten Mappi', 'papua')

    # Kabupaten Merauke
    url_merauke = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Merauke"
    df_merauke = get_kelurahan_data(url_merauke, 'Kabupaten Merauke', 'papua')

    # Kabupaten Mimika
    url_mimika = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mimika"
    df_mimika = get_kelurahan_data(url_mimika, 'Kabupaten Mimika', 'papua')

    # Kabupaten Nabire
    url_nabire = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nabire"
    df_nabire = get_kelurahan_data(url_nabire, 'Kabupaten Nabire', 'papua')

    # Kabupaten Nduga
    url_nduga = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nduga"
    df_nduga = get_kelurahan_data(url_nduga, 'Kabupaten Nduga', 'papua')

    # Kabupaten Paniai
    url_paniai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Paniai"
    df_paniai = get_kelurahan_data(url_paniai, 'Kabupaten Paniai', 'papua')

    # Kabupaten Pegunungan Bintang
    url_peg_bintang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pegunungan_Bintang"
    df_peg_bintang = get_kelurahan_data(url_peg_bintang, 'Kabupaten Pegunungan Bintang', 'papua')

    # Kabupaten Puncak
    url_puncak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Puncak"
    df_puncak = get_kelurahan_data(url_puncak, 'Kabupaten Puncak', 'papua')

    # Kabupaten Puncak Jaya
    url_puncak_jaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Puncak_Jaya"
    df_puncak_jaya = get_kelurahan_data(url_puncak_jaya, 'Kabupaten Puncak Jaya', 'papua')

    # Kabupaten Sarmi
    url_sarmi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sarmi"
    df_sarmi = get_kelurahan_data(url_sarmi, 'Kabupaten Sarmi', 'papua')

    # Kabupaten Supiori
    url_supiori = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Supiori"
    df_supiori = get_kelurahan_data(url_supiori, 'Kabupaten Supiori', 'papua')

    # Kabupaten Tolikara
    url_tolikara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tolikara"
    df_tolikara = get_kelurahan_data(url_tolikara, 'Kabupaten Tolikara', 'papua')

    # Kabupaten Waropen
    url_waropen = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Waropen"
    df_waropen = get_kelurahan_data(url_waropen, 'Kabupaten Waropen', 'papua')

    # Kabupaten Yahukimo
    url_yahukimo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Yahukimo"
    df_yahukimo = get_kelurahan_data(url_yahukimo, 'Kabupaten Yahukimo', 'papua')

    # Kabupaten Yalimo
    url_yalimo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Yalimo"
    df_yalimo = get_kelurahan_data(url_yalimo, 'Kabupaten Yalimo', 'papua')

    # Kota Jayapura
    url_jayapura_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Jayapura"
    df_jayapura_kota = get_kelurahan_data(url_jayapura_kota, 'Kota Jayapura', 'papua')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_papua = pd.concat([df_asmat, df_biak_numfor, df_boven_digoel, df_deiyai, df_dogiyai,
                            df_intan_jaya, df_jayapura, df_jayawijaya, df_keerom, df_kepulauan_yapen,
                            df_lanny_jaya, df_mamberamo_raya, df_mamberamo_tengah, df_mappi,
                            df_merauke, df_mimika, df_nabire, df_nduga, df_paniai, df_peg_bintang,
                            df_puncak, df_puncak_jaya, df_sarmi, df_supiori, df_tolikara, df_waropen,
                            df_yahukimo, df_yalimo, df_jayapura_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_papua = df_all_papua.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_papua = df_all_papua[~df_all_papua['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_papua)

    # Ambil daftar kelurahan dari df_all_papua
    papua_kelurahan_list = df_all_papua['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    papua_kelurahan_list = [kelurahan + ", Papua, Indonesia" for kelurahan in papua_kelurahan_list]
    print(papua_kelurahan_list)

    return df_all_papua