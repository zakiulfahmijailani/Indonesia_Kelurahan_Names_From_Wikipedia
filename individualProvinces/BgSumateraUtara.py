import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sumatera_utara():
    # KABUPATEN DAN KOTA DI SUMATERA UTARA
    # Kabupaten Asahan
    url_asahan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Asahan"
    df_asahan = get_kelurahan_data(url_asahan, 'Kabupaten Asahan', 'sumatera utara')

    # Kabupaten Batubara
    url_batubara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Batubara"
    df_batubara = get_kelurahan_data(url_batubara, 'Kabupaten Batubara', 'sumatera utara')

    # Kabupaten Dairi
    url_dairi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Dairi"
    df_dairi = get_kelurahan_data(url_dairi, 'Kabupaten Dairi', 'sumatera utara')

    # Kabupaten Deli Serdang
    url_deli_serdang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Deli_Serdang"
    df_deli_serdang = get_kelurahan_data(url_deli_serdang, 'Kabupaten Deli Serdang', 'sumatera utara')

    # Kabupaten Humbang Hasundutan
    url_humbang_hasundutan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Humbang_Hasundutan"
    df_humbang_hasundutan = get_kelurahan_data(url_humbang_hasundutan, 'Kabupaten Humbang Hasundutan', 'sumatera utara')

    # Kabupaten Karo
    url_karo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Karo"
    df_karo = get_kelurahan_data(url_karo, 'Kabupaten Karo', 'sumatera utara')

    # Kabupaten Labuhanbatu
    url_labuhanbatu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Labuhanbatu"
    df_labuhanbatu = get_kelurahan_data(url_labuhanbatu, 'Kabupaten Labuhanbatu', 'sumatera utara')

    # Kabupaten Labuhanbatu Selatan
    url_labuhanbatu_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Labuhanbatu_Selatan"
    df_labuhanbatu_selatan = get_kelurahan_data(url_labuhanbatu_selatan, 'Kabupaten Labuhanbatu Selatan', 'sumatera utara')

    # Kabupaten Labuhanbatu Utara
    url_labuhanbatu_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Labuhanbatu_Utara"
    df_labuhanbatu_utara = get_kelurahan_data(url_labuhanbatu_utara, 'Kabupaten Labuhanbatu Utara', 'sumatera utara')

    # Kabupaten Langkat
    url_langkat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Langkat"
    df_langkat = get_kelurahan_data(url_langkat, 'Kabupaten Langkat', 'sumatera utara')

    # Kabupaten Mandailing Natal
    url_mandailing_natal = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mandailing_Natal"
    df_mandailing_natal = get_kelurahan_data(url_mandailing_natal, 'Kabupaten Mandailing Natal', 'sumatera utara')

    # Kabupaten Nias
    url_nias = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nias"
    df_nias = get_kelurahan_data(url_nias, 'Kabupaten Nias', 'sumatera utara')

    # Kabupaten Nias Barat
    url_nias_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nias_Barat"
    df_nias_barat = get_kelurahan_data(url_nias_barat, 'Kabupaten Nias Barat', 'sumatera utara')

    # Kabupaten Nias Selatan
    url_nias_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nias_Selatan"
    df_nias_selatan = get_kelurahan_data(url_nias_selatan, 'Kabupaten Nias Selatan', 'sumatera utara')

    # Kabupaten Nias Utara
    url_nias_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nias_Utara"
    df_nias_utara = get_kelurahan_data(url_nias_utara, 'Kabupaten Nias Utara', 'sumatera utara')

    # Kabupaten Padang Lawas
    url_padang_lawas = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Padang_Lawas"
    df_padang_lawas = get_kelurahan_data(url_padang_lawas, 'Kabupaten Padang Lawas', 'sumatera utara')

    # Kabupaten Padang Lawas Utara
    url_padang_lawas_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Padang_Lawas_Utara"
    df_padang_lawas_utara = get_kelurahan_data(url_padang_lawas_utara, 'Kabupaten Padang Lawas Utara', 'sumatera utara')

    # Kabupaten Pakpak Bharat
    url_pakpak_bharat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pakpak_Bharat"
    df_pakpak_bharat = get_kelurahan_data(url_pakpak_bharat, 'Kabupaten Pakpak Bharat', 'sumatera utara')

    # Kabupaten Samosir
    url_samosir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Samosir"
    df_samosir = get_kelurahan_data(url_samosir, 'Kabupaten Samosir', 'sumatera utara')

    # Kabupaten Serdang Bedagai
    url_serdang_bedagai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Serdang_Bedagai"
    df_serdang_bedagai = get_kelurahan_data(url_serdang_bedagai, 'Kabupaten Serdang Bedagai', 'sumatera utara')

    # Kabupaten Simalungun
    url_simalungun = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Simalungun"
    df_simalungun = get_kelurahan_data(url_simalungun, 'Kabupaten Simalungun', 'sumatera utara')

    # Kabupaten Tapanuli Selatan
    url_tapanuli_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tapanuli_Selatan"
    df_tapanuli_selatan = get_kelurahan_data(url_tapanuli_selatan, 'Kabupaten Tapanuli Selatan', 'sumatera utara')

    # Kabupaten Tapanuli Tengah
    url_tapanuli_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tapanuli_Tengah"
    df_tapanuli_tengah = get_kelurahan_data(url_tapanuli_tengah, 'Kabupaten Tapanuli Tengah', 'sumatera utara')

    # Kabupaten Tapanuli Utara
    url_tapanuli_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tapanuli_Utara"
    df_tapanuli_utara = get_kelurahan_data(url_tapanuli_utara, 'Kabupaten Tapanuli Utara', 'sumatera utara')

    # Kabupaten Toba Samosir
    url_toba_samosir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Toba_Samosir"
    df_toba_samosir = get_kelurahan_data(url_toba_samosir, 'Kabupaten Toba Samosir', 'sumatera utara')

    # Kota Binjai
    url_binjai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Binjai"
    df_binjai = get_kelurahan_data(url_binjai, 'Kota Binjai', 'sumatera utara')

    # Kota Gunungsitoli
    url_gunungsitoli = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Gunungsitoli"
    df_gunungsitoli = get_kelurahan_data(url_gunungsitoli, 'Kota Gunungsitoli', 'sumatera utara')

    # Kota Medan
    url_medan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Medan"
    df_medan = get_kelurahan_data(url_medan, 'Kota Medan', 'sumatera utara')

    # Kota Padang Sidempuan
    url_padang_sidempuan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Padang_Sidempuan"
    df_padang_sidempuan = get_kelurahan_data(url_padang_sidempuan, 'Kota Padang Sidempuan', 'sumatera utara')

    # Kota Pematangsiantar
    url_pematangsiantar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pematangsiantar"
    df_pematangsiantar = get_kelurahan_data(url_pematangsiantar, 'Kota Pematangsiantar', 'sumatera utara')

    # Kota Sibolga
    url_sibolga = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Sibolga"
    df_sibolga = get_kelurahan_data(url_sibolga, 'Kota Sibolga', 'sumatera utara')

    # Kota Tanjung Balai
    url_tanjung_balai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tanjung_Balai"
    df_tanjung_balai = get_kelurahan_data(url_tanjung_balai, 'Kota Tanjung Balai', 'sumatera utara')

    # Kota Tebing Tinggi
    url_tebing_tinggi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tebing_Tinggi"
    df_tebing_tinggi = get_kelurahan_data(url_tebing_tinggi, 'Kota Tebing Tinggi', 'sumatera utara')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sumut = pd.concat([df_asahan, df_batubara, df_dairi, df_deli_serdang, df_humbang_hasundutan, df_karo,
                            df_labuhanbatu, df_labuhanbatu_selatan, df_labuhanbatu_utara, df_langkat, df_mandailing_natal,
                            df_nias, df_nias_barat, df_nias_selatan, df_nias_utara, df_padang_lawas, df_padang_lawas_utara,
                            df_pakpak_bharat, df_samosir, df_serdang_bedagai, df_simalungun, df_tapanuli_selatan,
                            df_tapanuli_tengah, df_tapanuli_utara, df_toba_samosir, df_binjai, df_gunungsitoli, df_medan,
                            df_padang_sidempuan, df_pematangsiantar, df_sibolga, df_tanjung_balai, df_tebing_tinggi],
                            ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sumut = df_all_sumut.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sumut = df_all_sumut[~df_all_sumut['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sumut)

    # Ambil daftar kelurahan dari df_all_sumut
    sumut_kelurahan_list = df_all_sumut['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sumut_kelurahan_list = [kelurahan + ", Sumatera Utara, Indonesia" for kelurahan in sumut_kelurahan_list]
    print(sumut_kelurahan_list)

    return df_all_sumut