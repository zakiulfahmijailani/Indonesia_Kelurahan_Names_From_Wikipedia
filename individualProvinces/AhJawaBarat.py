import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_jabar():
    # KABUPATEN DAN KOTA DI JAWA BARAT
    # Kabupaten Bandung
    url_bandung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bandung"
    df_bandung = get_kelurahan_data(url_bandung, 'Kabupaten Bandung', 'jawa barat')

    # Kabupaten Bandung Barat
    url_bandung_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bandung_Barat"
    df_bandung_barat = get_kelurahan_data(url_bandung_barat, 'Kabupaten Bandung Barat', 'jawa barat')

    # Kabupaten Bekasi
    url_bekasi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bekasi"
    df_bekasi = get_kelurahan_data(url_bekasi, 'Kabupaten Bekasi', 'jawa barat')

    # Kabupaten Bogor
    url_bogor = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bogor"
    df_bogor = get_kelurahan_data(url_bogor, 'Kabupaten Bogor', 'jawa barat')

    # Kabupaten Ciamis
    url_ciamis = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ciamis"
    df_ciamis = get_kelurahan_data(url_ciamis, 'Kabupaten Ciamis', 'jawa barat')

    # Kabupaten Cianjur
    url_cianjur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Cianjur"
    df_cianjur = get_kelurahan_data(url_cianjur, 'Kabupaten Cianjur', 'jawa barat')

    # Kabupaten Cirebon
    url_cirebon = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Cirebon"
    df_cirebon = get_kelurahan_data(url_cirebon, 'Kabupaten Cirebon', 'jawa barat')

    # Kabupaten Garut
    url_garut = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Garut"
    df_garut = get_kelurahan_data(url_garut, 'Kabupaten Garut', 'jawa barat')

    # Kabupaten Indramayu
    url_indramayu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Indramayu"
    df_indramayu = get_kelurahan_data(url_indramayu, 'Kabupaten Indramayu', 'jawa barat')

    # Kabupaten Karawang
    url_karawang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Karawang"
    df_karawang = get_kelurahan_data(url_karawang, 'Kabupaten Karawang', 'jawa barat')

    # Kabupaten Kuningan
    url_kuningan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kuningan"
    df_kuningan = get_kelurahan_data(url_kuningan, 'Kabupaten Kuningan', 'jawa barat')

    # Kabupaten Majalengka
    url_majalengka = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Majalengka"
    df_majalengka = get_kelurahan_data(url_majalengka, 'Kabupaten Majalengka', 'jawa barat')

    # Kabupaten Pangandaran
    url_pangandaran = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pangandaran"
    df_pangandaran = get_kelurahan_data(url_pangandaran, 'Kabupaten Pangandaran', 'jawa barat')

    # Kabupaten Purwakarta
    url_purwakarta = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Purwakarta"
    df_purwakarta = get_kelurahan_data(url_purwakarta, 'Kabupaten Purwakarta', 'jawa barat')

    # Kabupaten Subang
    url_subang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Subang"
    df_subang = get_kelurahan_data(url_subang, 'Kabupaten Subang', 'jawa barat')

    # Kabupaten Sukabumi
    url_sukabumi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sukabumi"
    df_sukabumi = get_kelurahan_data(url_sukabumi, 'Kabupaten Sukabumi', 'jawa barat')

    # Kabupaten Sumedang
    url_sumedang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumedang"
    df_sumedang = get_kelurahan_data(url_sumedang, 'Kabupaten Sumedang', 'jawa barat')

    # Kabupaten Tasikmalaya
    url_tasikmalaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tasikmalaya"
    df_tasikmalaya = get_kelurahan_data(url_tasikmalaya, 'Kabupaten Tasikmalaya', 'jawa barat')

    # Kota Bandung
    url_bandung_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bandung"
    df_bandung_kota = get_kelurahan_data(url_bandung_kota, 'Kota Bandung', 'jawa barat')

    # Kota Banjar
    url_banjar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Banjar"
    df_banjar = get_kelurahan_data(url_banjar, 'Kota Banjar', 'jawa barat')

    # Kota Bekasi
    url_bekasi_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bekasi"
    df_bekasi_kota = get_kelurahan_data(url_bekasi_kota, 'Kota Bekasi', 'jawa barat')

    # Kota Bogor
    url_bogor_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bogor"
    df_bogor_kota = get_kelurahan_data(url_bogor_kota, 'Kota Bogor', 'jawa barat')

    # Kota Cimahi
    url_cimahi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Cimahi"
    df_cimahi = get_kelurahan_data(url_cimahi, 'Kota Cimahi', 'jawa barat')

    # Kota Cirebon
    url_cirebon_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Cirebon"
    df_cirebon_kota = get_kelurahan_data(url_cirebon_kota, 'Kota Cirebon', 'jawa barat')

    # Kota Depok
    url_depok = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Depok"
    df_depok = get_kelurahan_data(url_depok, 'Kota Depok', 'jawa barat')

    # Kota Sukabumi
    url_sukabumi_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Sukabumi"
    df_sukabumi_kota = get_kelurahan_data(url_sukabumi_kota, 'Kota Sukabumi', 'jawa barat')

    # Kota Tasikmalaya
    url_tasikmalaya_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tasikmalaya"
    df_tasikmalaya_kota = get_kelurahan_data(url_tasikmalaya_kota, 'Kota Tasikmalaya', 'jawa barat')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_jawa_barat = pd.concat([df_bandung, df_bandung_barat, df_bekasi, df_bogor, df_ciamis,
                                df_cianjur, df_cirebon, df_garut, df_indramayu, df_karawang,
                                df_kuningan, df_majalengka, df_pangandaran, df_purwakarta,
                                df_subang, df_sukabumi, df_sumedang, df_tasikmalaya,
                                df_bandung_kota, df_banjar, df_bekasi_kota, df_bogor_kota,
                                df_cimahi, df_cirebon_kota, df_depok, df_sukabumi_kota,
                                df_tasikmalaya_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_jawa_barat = df_all_jawa_barat.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_jawa_barat = df_all_jawa_barat[~df_all_jawa_barat['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_jawa_barat)

    # Ambil daftar kelurahan dari df_all_jawa_barat
    jawa_barat_kelurahan_list = df_all_jawa_barat['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    jawa_barat_kelurahan_list = [kelurahan + ", Jawa Barat, Indonesia" for kelurahan in jawa_barat_kelurahan_list]
    print(jawa_barat_kelurahan_list)

    return df_all_jawa_barat