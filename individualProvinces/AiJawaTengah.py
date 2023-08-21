import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_jateng():
    # KABUPATEN DAN KOTA DI JAWA TENGAH
    # Kabupaten Banjarnegara
    url_banjarnegara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banjarnegara"
    df_banjarnegara = get_kelurahan_data(url_banjarnegara, 'Kabupaten Banjarnegara', 'jawa tengah')

    # Kabupaten Banyumas
    url_banyumas = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banyumas"
    df_banyumas = get_kelurahan_data(url_banyumas, 'Kabupaten Banyumas', 'jawa tengah')

    # Kabupaten Batang
    url_batang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Batang"
    df_batang = get_kelurahan_data(url_batang, 'Kabupaten Batang', 'jawa tengah')

    # Kabupaten Blora
    url_blora = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Blora"
    df_blora = get_kelurahan_data(url_blora, 'Kabupaten Blora', 'jawa tengah')

    # Kabupaten Boyolali
    url_boyolali = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Boyolali"
    df_boyolali = get_kelurahan_data(url_boyolali, 'Kabupaten Boyolali', 'jawa tengah')

    # Kabupaten Brebes
    url_brebes = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Brebes"
    df_brebes = get_kelurahan_data(url_brebes, 'Kabupaten Brebes', 'jawa tengah')

    # Kabupaten Cilacap
    url_cilacap = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Cilacap"
    df_cilacap = get_kelurahan_data(url_cilacap, 'Kabupaten Cilacap', 'jawa tengah')

    # Kabupaten Demak
    url_demak = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Demak"
    df_demak = get_kelurahan_data(url_demak, 'Kabupaten Demak', 'jawa tengah')

    # Kabupaten Grobogan
    url_grobogan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Grobogan"
    df_grobogan = get_kelurahan_data(url_grobogan, 'Kabupaten Grobogan', 'jawa tengah')

    # Kabupaten Jepara
    url_jepara = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jepara"
    df_jepara = get_kelurahan_data(url_jepara, 'Kabupaten Jepara', 'jawa tengah')

    # Kabupaten Karanganyar
    url_karanganyar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Karanganyar"
    df_karanganyar = get_kelurahan_data(url_karanganyar, 'Kabupaten Karanganyar', 'jawa tengah')

    # Kabupaten Kebumen
    url_kebumen = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kebumen"
    df_kebumen = get_kelurahan_data(url_kebumen, 'Kabupaten Kebumen', 'jawa tengah')

    # Kabupaten Kendal
    url_kendal = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kendal"
    df_kendal = get_kelurahan_data(url_kendal, 'Kabupaten Kendal', 'jawa tengah')

    # Kabupaten Klaten
    url_klaten = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Klaten"
    df_klaten = get_kelurahan_data(url_klaten, 'Kabupaten Klaten', 'jawa tengah')

    # Kabupaten Kudus
    url_kudus = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kudus"
    df_kudus = get_kelurahan_data(url_kudus, 'Kabupaten Kudus', 'jawa tengah')

    # Kabupaten Magelang
    url_magelang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Magelang"
    df_magelang = get_kelurahan_data(url_magelang, 'Kabupaten Magelang', 'jawa tengah')

    # Kabupaten Pati
    url_pati = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pati"
    df_pati = get_kelurahan_data(url_pati, 'Kabupaten Pati', 'jawa tengah')

    # Kabupaten Pekalongan
    url_pekalongan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pekalongan"
    df_pekalongan = get_kelurahan_data(url_pekalongan, 'Kabupaten Pekalongan', 'jawa tengah')

    # Kabupaten Pemalang
    url_pemalang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pemalang"
    df_pemalang = get_kelurahan_data(url_pemalang, 'Kabupaten Pemalang', 'jawa tengah')

    # Kabupaten Purbalingga
    url_purbalingga = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Purbalingga"
    df_purbalingga = get_kelurahan_data(url_purbalingga, 'Kabupaten Purbalingga', 'jawa tengah')

    # Kabupaten Purworejo
    url_purworejo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Purworejo"
    df_purworejo = get_kelurahan_data(url_purworejo, 'Kabupaten Purworejo', 'jawa tengah')

    # Kabupaten Rembang
    url_rembang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Rembang"
    df_rembang = get_kelurahan_data(url_rembang, 'Kabupaten Rembang', 'jawa tengah')

    # Kabupaten Semarang
    url_semarang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Semarang"
    df_semarang = get_kelurahan_data(url_semarang, 'Kabupaten Semarang', 'jawa tengah')

    # Kabupaten Sragen
    url_sragen = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sragen"
    df_sragen = get_kelurahan_data(url_sragen, 'Kabupaten Sragen', 'jawa tengah')

    # Kabupaten Sukoharjo
    url_sukoharjo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sukoharjo"
    df_sukoharjo = get_kelurahan_data(url_sukoharjo, 'Kabupaten Sukoharjo', 'jawa tengah')

    # Kabupaten Tegal
    url_tegal = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tegal"
    df_tegal = get_kelurahan_data(url_tegal, 'Kabupaten Tegal', 'jawa tengah')

    # Kabupaten Temanggung
    url_temanggung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Temanggung"
    df_temanggung = get_kelurahan_data(url_temanggung, 'Kabupaten Temanggung', 'jawa tengah')

    # Kabupaten Wonogiri
    url_wonogiri = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Wonogiri"
    df_wonogiri = get_kelurahan_data(url_wonogiri, 'Kabupaten Wonogiri', 'jawa tengah')

    # Kabupaten Wonosobo
    url_wonosobo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Wonosobo"
    df_wonosobo = get_kelurahan_data(url_wonosobo, 'Kabupaten Wonosobo', 'jawa tengah')

    # Kota Magelang
    url_magelang_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Magelang"
    df_magelang_kota = get_kelurahan_data(url_magelang_kota, 'Kota Magelang', 'jawa tengah')

    # Kota Pekalongan
    url_pekalongan_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pekalongan"
    df_pekalongan_kota = get_kelurahan_data(url_pekalongan_kota, 'Kota Pekalongan', 'jawa tengah')

    # Kota Salatiga
    url_salatiga = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Salatiga"
    df_salatiga = get_kelurahan_data(url_salatiga, 'Kota Salatiga', 'jawa tengah')

    # Kota Semarang
    url_semarang_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Semarang"
    df_semarang_kota = get_kelurahan_data(url_semarang_kota, 'Kota Semarang', 'jawa tengah')

    # Kota Surakarta
    url_surakarta = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Surakarta"
    df_surakarta = get_kelurahan_data(url_surakarta, 'Kota Surakarta', 'jawa tengah')

    # Kota Tegal
    url_tegal_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tegal"
    df_tegal_kota = get_kelurahan_data(url_tegal_kota, 'Kota Tegal', 'jawa tengah')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_jawa_tengah = pd.concat([df_banjarnegara, df_banyumas, df_batang, df_blora, df_boyolali,
                                df_brebes, df_cilacap, df_demak, df_grobogan, df_jepara,
                                df_karanganyar, df_kebumen, df_kendal, df_klaten, df_kudus,
                                df_magelang, df_pati, df_pekalongan, df_pemalang, df_purbalingga,
                                df_purworejo, df_rembang, df_semarang, df_sragen, df_sukoharjo,
                                df_tegal, df_temanggung, df_wonogiri, df_wonosobo, df_magelang_kota,
                                df_pekalongan_kota, df_salatiga, df_semarang_kota, df_surakarta,
                                df_tegal_kota], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_jawa_tengah = df_all_jawa_tengah.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_jawa_tengah = df_all_jawa_tengah[~df_all_jawa_tengah['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_jawa_tengah)

    # Ambil daftar kelurahan dari df_all_jawa_tengah
    jawa_tengah_kelurahan_list = df_all_jawa_tengah['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    jawa_tengah_kelurahan_list = [kelurahan + ", Jawa Tengah, Indonesia" for kelurahan in jawa_tengah_kelurahan_list]
    print(jawa_tengah_kelurahan_list)

    return df_all_jawa_tengah