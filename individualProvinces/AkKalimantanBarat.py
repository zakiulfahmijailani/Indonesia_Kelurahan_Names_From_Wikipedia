import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_kalbar():
    # KABUPATEN DAN KOTA DI KALIMANTAN BARAT
    # Kabupaten Bengkayang
    url_bengkayang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bengkayang"
    df_bengkayang = get_kelurahan_data(url_bengkayang, 'Kabupaten Bengkayang', 'kalimantan barat')

    # Kabupaten Kapuas Hulu
    url_kapuas_hulu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kapuas_Hulu"
    df_kapuas_hulu = get_kelurahan_data(url_kapuas_hulu, 'Kabupaten Kapuas Hulu', 'kalimantan barat')

    # Kabupaten Kayong Utara
    url_kayong_utara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kayong_Utara"
    df_kayong_utara = get_kelurahan_data(url_kayong_utara, 'Kabupaten Kayong Utara', 'kalimantan barat')

    # Kabupaten Ketapang
    url_ketapang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ketapang"
    df_ketapang = get_kelurahan_data(url_ketapang, 'Kabupaten Ketapang', 'kalimantan barat')

    # Kabupaten Kubu Raya
    url_kubu_raya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kubu_Raya"
    df_kubu_raya = get_kelurahan_data(url_kubu_raya, 'Kabupaten Kubu Raya', 'kalimantan barat')

    # Kabupaten Landak
    url_landak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Landak"
    df_landak = get_kelurahan_data(url_landak, 'Kabupaten Landak', 'kalimantan barat')

    # Kabupaten Melawi
    url_melawi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Melawi"
    df_melawi = get_kelurahan_data(url_melawi, 'Kabupaten Melawi', 'kalimantan barat')

    # Kabupaten Mempawah
    url_mempawah = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mempawah"
    df_mempawah = get_kelurahan_data(url_mempawah, 'Kabupaten Mempawah', 'kalimantan barat')

    # Kabupaten Sambas
    url_sambas = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sambas"
    df_sambas = get_kelurahan_data(url_sambas, 'Kabupaten Sambas', 'kalimantan barat')

    # Kabupaten Sanggau
    url_sanggau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sanggau"
    df_sanggau = get_kelurahan_data(url_sanggau, 'Kabupaten Sanggau', 'kalimantan barat')

    # Kabupaten Sekadau
    url_sekadau = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sekadau"
    df_sekadau = get_kelurahan_data(url_sekadau, 'Kabupaten Sekadau', 'kalimantan barat')

    # Kabupaten Sintang
    url_sintang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sintang"
    df_sintang = get_kelurahan_data(url_sintang, 'Kabupaten Sintang', 'kalimantan barat')

    # Kota Pontianak
    url_pontianak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pontianak"
    df_pontianak = get_kelurahan_data(url_pontianak, 'Kota Pontianak', 'kalimantan barat')

    # Kota Singkawang
    url_singkawang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Singkawang"
    df_singkawang = get_kelurahan_data(url_singkawang, 'Kota Singkawang', 'kalimantan barat')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_kalimantan_barat = pd.concat([df_bengkayang, df_kapuas_hulu, df_kayong_utara, df_ketapang, df_kubu_raya,
                                        df_landak, df_melawi, df_mempawah, df_sambas, df_sanggau, df_sekadau,
                                        df_sintang, df_pontianak, df_singkawang], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_kalimantan_barat = df_all_kalimantan_barat.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_kalimantan_barat = df_all_kalimantan_barat[~df_all_kalimantan_barat['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_kalimantan_barat)

    # Ambil daftar kelurahan dari df_all_kalimantan_barat
    kalimantan_barat_kelurahan_list = df_all_kalimantan_barat['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    kalimantan_barat_kelurahan_list = [kelurahan + ", Kalimantan Barat, Indonesia" for kelurahan in kalimantan_barat_kelurahan_list]
    print(kalimantan_barat_kelurahan_list)

    return df_all_kalimantan_barat