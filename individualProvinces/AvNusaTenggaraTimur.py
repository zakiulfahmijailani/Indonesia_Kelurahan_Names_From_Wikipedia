import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_ntt():
    # KABUPATEN DAN KOTA DI NUSA TENGGARA TIMUR
    # Kabupaten Alor
    url_alor = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Alor"
    df_alor = get_kelurahan_data(url_alor, 'Kabupaten Alor', 'nusa tenggara timur')

    # Kabupaten Belu
    url_belu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Belu"
    df_belu = get_kelurahan_data(url_belu, 'Kabupaten Belu', 'nusa tenggara timur')

    # Kabupaten Ende
    url_ende = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ende"
    df_ende = get_kelurahan_data(url_ende, 'Kabupaten Ende', 'nusa tenggara timur')

    # Kabupaten Flores Timur
    url_flores_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Flores_Timur"
    df_flores_timur = get_kelurahan_data(url_flores_timur, 'Kabupaten Flores Timur', 'nusa tenggara timur')

    # Kabupaten Kupang
    url_kupang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kupang"
    df_kupang = get_kelurahan_data(url_kupang, 'Kabupaten Kupang', 'nusa tenggara timur')

    # Kabupaten Lembata
    url_lembata = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lembata"
    df_lembata = get_kelurahan_data(url_lembata, 'Kabupaten Lembata', 'nusa tenggara timur')

    # Kabupaten Malaka
    url_malaka = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Malaka"
    df_malaka = get_kelurahan_data(url_malaka, 'Kabupaten Malaka', 'nusa tenggara timur')

    # Kabupaten Manggarai
    url_manggarai = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Manggarai"
    df_manggarai = get_kelurahan_data(url_manggarai, 'Kabupaten Manggarai', 'nusa tenggara timur')

    # Kabupaten Manggarai Barat
    url_manggarai_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Manggarai_Barat"
    df_manggarai_barat = get_kelurahan_data(url_manggarai_barat, 'Kabupaten Manggarai Barat', 'nusa tenggara timur')

    # Kabupaten Manggarai Timur
    url_manggarai_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Manggarai_Timur"
    df_manggarai_timur = get_kelurahan_data(url_manggarai_timur, 'Kabupaten Manggarai Timur', 'nusa tenggara timur')

    # Kabupaten Nagekeo
    url_nagekeo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nagekeo"
    df_nagekeo = get_kelurahan_data(url_nagekeo, 'Kabupaten Nagekeo', 'nusa tenggara timur')

    # Kabupaten Ngada
    url_ngada = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ngada"
    df_ngada = get_kelurahan_data(url_ngada, 'Kabupaten Ngada', 'nusa tenggara timur')

    # Kabupaten Rote Ndao
    url_rote_ndao = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Rote_Ndao"
    df_rote_ndao = get_kelurahan_data(url_rote_ndao, 'Kabupaten Rote Ndao', 'nusa tenggara timur')

    # Kabupaten Sabu Raijua
    url_sabu_raijua = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sabu_Raijua"
    df_sabu_raijua = get_kelurahan_data(url_sabu_raijua, 'Kabupaten Sabu Raijua', 'nusa tenggara timur')

    # Kabupaten Sikka
    url_sikka = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sikka"
    df_sikka = get_kelurahan_data(url_sikka, 'Kabupaten Sikka', 'nusa tenggara timur')

    # Kabupaten Sumba Barat
    url_sumba_barat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumba_Barat"
    df_sumba_barat = get_kelurahan_data(url_sumba_barat, 'Kabupaten Sumba Barat', 'nusa tenggara timur')

    # Kabupaten Sumba Barat Daya
    url_sumba_barat_daya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumba_Barat_Daya"
    df_sumba_barat_daya = get_kelurahan_data(url_sumba_barat_daya, 'Kabupaten Sumba Barat Daya', 'nusa tenggara timur')

    # Kabupaten Sumba Tengah
    url_sumba_tengah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumba_Tengah"
    df_sumba_tengah = get_kelurahan_data(url_sumba_tengah, 'Kabupaten Sumba Tengah', 'nusa tenggara timur')

    # Kabupaten Sumba Timur
    url_sumba_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumba_Timur"
    df_sumba_timur = get_kelurahan_data(url_sumba_timur, 'Kabupaten Sumba Timur', 'nusa tenggara timur')

    # Kabupaten Timor Tengah Selatan
    url_timor_tengah_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Timor_Tengah_Selatan"
    df_timor_tengah_selatan = get_kelurahan_data(url_timor_tengah_selatan, 'Kabupaten Timor Tengah Selatan', 'nusa tenggara timur')

    # Kabupaten Timor Tengah Utara
    url_timor_tengah_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Timor_Tengah_Utara"
    df_timor_tengah_utara = get_kelurahan_data(url_timor_tengah_utara, 'Kabupaten Timor Tengah Utara', 'nusa tenggara timur')

    # Kota Kupang
    url_kupang_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Kupang"
    df_kupang_kota = get_kelurahan_data(url_kupang_kota, 'Kota Kupang', 'nusa tenggara timur')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_ntt = pd.concat([df_alor, df_belu, df_ende, df_flores_timur, df_kupang, df_lembata,
                            df_malaka, df_manggarai, df_manggarai_barat, df_manggarai_timur,
                            df_nagekeo, df_ngada, df_rote_ndao, df_sabu_raijua, df_sikka,
                            df_sumba_barat, df_sumba_barat_daya, df_sumba_tengah, df_sumba_timur,
                            df_timor_tengah_selatan, df_timor_tengah_utara, df_kupang_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_ntt = df_all_ntt.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_ntt = df_all_ntt[~df_all_ntt['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_ntt)

    # Ambil daftar kelurahan dari df_all_ntt
    ntt_kelurahan_list = df_all_ntt['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    ntt_kelurahan_list = [kelurahan + ", Nusa Tenggara Timur, Indonesia" for kelurahan in ntt_kelurahan_list]
    print(ntt_kelurahan_list)

    return df_all_ntt