import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sumatera_barat():
    # KABUPATEN DAN KOTA DI SUMATERA BARAT
    # Kabupaten Agam
    url_agam = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Agam"
    df_agam = get_kelurahan_data(url_agam, 'Kabupaten Agam', 'sumatera barat')

    # Kabupaten Dharmasraya
    url_dharmasraya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Dharmasraya"
    df_dharmasraya = get_kelurahan_data(url_dharmasraya, 'Kabupaten Dharmasraya', 'sumatera barat')

    # Kabupaten Kepulauan Mentawai
    url_kepulauan_mentawai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kepulauan_Mentawai"
    df_kepulauan_mentawai = get_kelurahan_data(url_kepulauan_mentawai, 'Kabupaten Kepulauan Mentawai', 'sumatera barat')

    # Kabupaten Lima Puluh Kota
    url_lima_puluh_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lima_Puluh_Kota"
    df_lima_puluh_kota = get_kelurahan_data(url_lima_puluh_kota, 'Kabupaten Lima Puluh Kota', 'sumatera barat')

    # Kabupaten Padang Pariaman
    url_padang_pariaman = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Padang_Pariaman"
    df_padang_pariaman = get_kelurahan_data(url_padang_pariaman, 'Kabupaten Padang Pariaman', 'sumatera barat')

    # Kabupaten Pasaman
    url_pasaman = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pasaman"
    df_pasaman = get_kelurahan_data(url_pasaman, 'Kabupaten Pasaman', 'sumatera barat')

    # Kabupaten Pasaman Barat
    url_pasaman_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pasaman_Barat"
    df_pasaman_barat = get_kelurahan_data(url_pasaman_barat, 'Kabupaten Pasaman Barat', 'sumatera barat')

    # Kabupaten Pesisir Selatan
    url_pesisir_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pesisir_Selatan"
    df_pesisir_selatan = get_kelurahan_data(url_pesisir_selatan, 'Kabupaten Pesisir Selatan', 'sumatera barat')

    # Kabupaten Sijunjung
    url_sijunjung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sijunjung"
    df_sijunjung = get_kelurahan_data(url_sijunjung, 'Kabupaten Sijunjung', 'sumatera barat')

    # Kabupaten Solok
    url_solok = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Solok"
    df_solok = get_kelurahan_data(url_solok, 'Kabupaten Solok', 'sumatera barat')

    # Kabupaten Solok Selatan
    url_solok_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Solok_Selatan"
    df_solok_selatan = get_kelurahan_data(url_solok_selatan, 'Kabupaten Solok Selatan', 'sumatera barat')

    # Kabupaten Tanah Datar
    url_tanah_datar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tanah_Datar"
    df_tanah_datar = get_kelurahan_data(url_tanah_datar, 'Kabupaten Tanah Datar', 'sumatera barat')

    # Kota Bukittinggi
    url_bukittinggi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Bukittinggi"
    df_bukittinggi = get_kelurahan_data(url_bukittinggi, 'Kota Bukittinggi', 'sumatera barat')

    # Kota Padang
    url_padang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Padang"
    df_padang = get_kelurahan_data(url_padang, 'Kota Padang', 'sumatera barat')

    # Kota Padangpanjang
    url_padangpanjang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Padangpanjang"
    df_padangpanjang = get_kelurahan_data(url_padangpanjang, 'Kota Padangpanjang', 'sumatera barat')

    # Kota Pariaman
    url_pariaman = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pariaman"
    df_pariaman = get_kelurahan_data(url_pariaman, 'Kota Pariaman', 'sumatera barat')

    # Kota Payakumbuh
    url_payakumbuh = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Payakumbuh"
    df_payakumbuh = get_kelurahan_data(url_payakumbuh, 'Kota Payakumbuh', 'sumatera barat')

    # Kota Sawahlunto
    url_sawahlunto = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Sawahlunto"
    df_sawahlunto = get_kelurahan_data(url_sawahlunto, 'Kota Sawahlunto', 'sumatera barat')

    # Kota Solok
    url_kota_solok = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Solok"
    df_kota_solok = get_kelurahan_data(url_kota_solok, 'Kota Solok', 'sumatera barat')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sumatera_barat = pd.concat([df_agam, df_dharmasraya, df_kepulauan_mentawai, df_lima_puluh_kota, df_padang_pariaman,
                                    df_pasaman, df_pasaman_barat, df_pesisir_selatan, df_sijunjung, df_solok,
                                    df_solok_selatan, df_tanah_datar, df_bukittinggi, df_padang, df_padangpanjang,
                                    df_pariaman, df_payakumbuh, df_sawahlunto, df_kota_solok], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sumatera_barat = df_all_sumatera_barat.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sumatera_barat = df_all_sumatera_barat[~df_all_sumatera_barat['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sumatera_barat)

    # Ambil daftar kelurahan dari df_all_sumatera_barat
    sumatera_barat_kelurahan_list = df_all_sumatera_barat['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sumatera_barat_kelurahan_list = [kelurahan + ", Sumatera Barat, Indonesia" for kelurahan in sumatera_barat_kelurahan_list]
    print(sumatera_barat_kelurahan_list)

    return df_all_sumatera_barat