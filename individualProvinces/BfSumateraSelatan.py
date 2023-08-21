import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_sumatera_selatan():
    # KABUPATEN DAN KOTA DI SUMATERA SELATAN
    # Kabupaten Banyuasin
    url_banyuasin = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banyuasin"
    df_banyuasin = get_kelurahan_data(url_banyuasin, 'Kabupaten Banyuasin', 'sumatera selatan')

    # Kabupaten Empat Lawang
    url_empat_lawang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Empat_Lawang"
    df_empat_lawang = get_kelurahan_data(url_empat_lawang, 'Kabupaten Empat Lawang', 'sumatera selatan')

    # Kabupaten Lahat
    url_lahat = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lahat"
    df_lahat = get_kelurahan_data(url_lahat, 'Kabupaten Lahat', 'sumatera selatan')

    # Kabupaten Muara Enim
    url_muara_enim = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Muara_Enim"
    df_muara_enim = get_kelurahan_data(url_muara_enim, 'Kabupaten Muara Enim', 'sumatera selatan')

    # Kabupaten Musi Banyuasin
    url_musi_banyuasin = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Musi_Banyuasin"
    df_musi_banyuasin = get_kelurahan_data(url_musi_banyuasin, 'Kabupaten Musi Banyuasin', 'sumatera selatan')

    # Kabupaten Musi Rawas
    url_musi_rawas = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Musi_Rawas"
    df_musi_rawas = get_kelurahan_data(url_musi_rawas, 'Kabupaten Musi Rawas', 'sumatera selatan')

    # Kabupaten Musi Rawas Utara
    url_musi_rawas_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Musi_Rawas_Utara"
    df_musi_rawas_utara = get_kelurahan_data(url_musi_rawas_utara, 'Kabupaten Musi Rawas Utara', 'sumatera selatan')

    # Kabupaten Ogan Ilir
    url_ogan_ilir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ogan_Ilir"
    df_ogan_ilir = get_kelurahan_data(url_ogan_ilir, 'Kabupaten Ogan Ilir', 'sumatera selatan')

    # Kabupaten Ogan Komering Ilir
    url_ogan_komering_ilir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ogan_Komering_Ilir"
    df_ogan_komering_ilir = get_kelurahan_data(url_ogan_komering_ilir, 'Kabupaten Ogan Komering Ilir', 'sumatera selatan')

    # Kabupaten Ogan Komering Ulu
    url_ogan_komering_ulu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ogan_Komering_Ulu"
    df_ogan_komering_ulu = get_kelurahan_data(url_ogan_komering_ulu, 'Kabupaten Ogan Komering Ulu', 'sumatera selatan')

    # Kabupaten Ogan Komering Ulu Selatan
    url_ogan_komering_ulu_selatan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ogan_Komering_Ulu_Selatan"
    df_ogan_komering_ulu_selatan = get_kelurahan_data(url_ogan_komering_ulu_selatan, 'Kabupaten Ogan Komering Ulu Selatan', 'sumatera selatan')

    # Kabupaten Ogan Komering Ulu Timur
    url_ogan_komering_ulu_timur = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ogan_Komering_Ulu_Timur"
    df_ogan_komering_ulu_timur = get_kelurahan_data(url_ogan_komering_ulu_timur, 'Kabupaten Ogan Komering Ulu Timur', 'sumatera selatan')

    # Kabupaten Penukal Abab Lematang Ilir
    url_penukal_abab_lematang_ilir = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Penukal_Abab_Lematang_Ilir"
    df_penukal_abab_lematang_ilir = get_kelurahan_data(url_penukal_abab_lematang_ilir, 'Kabupaten Penukal Abab Lematang Ilir', 'sumatera selatan')

    # Kota Lubuklinggau
    url_lubuklinggau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Lubuklinggau"
    df_lubuklinggau = get_kelurahan_data(url_lubuklinggau, 'Kota Lubuklinggau', 'sumatera selatan')

    # Kota Pagar Alam
    url_pagar_alam = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pagar_Alam"
    df_pagar_alam = get_kelurahan_data(url_pagar_alam, 'Kota Pagar Alam', 'sumatera selatan')

    # Kota Palembang
    url_palembang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Palembang"
    df_palembang = get_kelurahan_data(url_palembang, 'Kota Palembang', 'sumatera selatan')

    # Kota Prabumulih
    url_prabumulih = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Prabumulih"
    df_prabumulih = get_kelurahan_data(url_prabumulih, 'Kota Prabumulih', 'sumatera selatan')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_sumatera_selatan = pd.concat([df_banyuasin, df_empat_lawang, df_lahat, df_muara_enim, df_musi_banyuasin,
                                        df_musi_rawas, df_musi_rawas_utara, df_ogan_ilir, df_ogan_komering_ilir,
                                        df_ogan_komering_ulu, df_ogan_komering_ulu_selatan, df_ogan_komering_ulu_timur,
                                        df_penukal_abab_lematang_ilir, df_lubuklinggau, df_pagar_alam, df_palembang,
                                        df_prabumulih], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_sumatera_selatan = df_all_sumatera_selatan.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_sumatera_selatan = df_all_sumatera_selatan[~df_all_sumatera_selatan['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_sumatera_selatan)

    # Ambil daftar kelurahan dari df_all_sumatera_selatan
    sumatera_selatan_kelurahan_list = df_all_sumatera_selatan['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    sumatera_selatan_kelurahan_list = [kelurahan + ", Sumatera Selatan, Indonesia" for kelurahan in sumatera_selatan_kelurahan_list]
    print(sumatera_selatan_kelurahan_list)

    return df_all_sumatera_selatan