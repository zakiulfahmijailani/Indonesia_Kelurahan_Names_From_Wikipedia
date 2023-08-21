import sys
sys.path.append('C:/OSMScience/KelurahanIndonesia/')

from libraries import *
from function_custom import get_kelurahan_data

def get_df_all_jatim():
    # KABUPATEN DAN KOTA DI JAWA TIMUR
    # Kabupaten Bangkalan
    url_bangkalan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bangkalan"
    df_bangkalan = get_kelurahan_data(url_bangkalan, 'Kabupaten Bangkalan', 'jawa timur')

    # Kabupaten Banyuwangi
    url_banyuwangi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banyuwangi"
    df_banyuwangi = get_kelurahan_data(url_banyuwangi, 'Kabupaten Banyuwangi', 'jawa timur')

    # Kabupaten Blitar
    url_blitar = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Blitar"
    df_blitar = get_kelurahan_data(url_blitar, 'Kabupaten Blitar', 'jawa timur')

    # Kabupaten Bojonegoro
    url_bojonegoro = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bojonegoro"
    df_bojonegoro = get_kelurahan_data(url_bojonegoro, 'Kabupaten Bojonegoro', 'jawa timur')

    # Kabupaten Bondowoso
    url_bondowoso = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Bondowoso"
    df_bondowoso = get_kelurahan_data(url_bondowoso, 'Kabupaten Bondowoso', 'jawa timur')

    # Kabupaten Gresik
    url_gresik = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Gresik"
    df_gresik = get_kelurahan_data(url_gresik, 'Kabupaten Gresik', 'jawa timur')

    # Kabupaten Jember
    url_jember = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jember"
    df_jember = get_kelurahan_data(url_jember, 'Kabupaten Jember', 'jawa timur')

    # Kabupaten Jombang
    url_jombang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Jombang"
    df_jombang = get_kelurahan_data(url_jombang, 'Kabupaten Jombang', 'jawa timur')

    # Kabupaten Kediri
    url_kediri = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Kediri"
    df_kediri = get_kelurahan_data(url_kediri, 'Kabupaten Kediri', 'jawa timur')

    # Kabupaten Lamongan
    url_lamongan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lamongan"
    df_lamongan = get_kelurahan_data(url_lamongan, 'Kabupaten Lamongan', 'jawa timur')

    # Kabupaten Lumajang
    url_lumajang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Lumajang"
    df_lumajang = get_kelurahan_data(url_lumajang, 'Kabupaten Lumajang', 'jawa timur')

    # Kabupaten Madiun
    url_madiun = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Madiun"
    df_madiun = get_kelurahan_data(url_madiun, 'Kabupaten Madiun', 'jawa timur')

    # Kabupaten Magetan
    url_magetan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Magetan"
    df_magetan = get_kelurahan_data(url_magetan, 'Kabupaten Magetan', 'jawa timur')

    # Kabupaten Malang
    url_malang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Malang"
    df_malang = get_kelurahan_data(url_malang, 'Kabupaten Malang', 'jawa timur')

    # Kabupaten Mojokerto
    url_mojokerto = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Mojokerto"
    df_mojokerto = get_kelurahan_data(url_mojokerto, 'Kabupaten Mojokerto', 'jawa timur')

    # Kabupaten Nganjuk
    url_nganjuk = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Nganjuk"
    df_nganjuk = get_kelurahan_data(url_nganjuk, 'Kabupaten Nganjuk', 'jawa timur')

    # Kabupaten Ngawi
    url_ngawi = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ngawi"
    df_ngawi = get_kelurahan_data(url_ngawi, 'Kabupaten Ngawi', 'jawa timur')

    # Kabupaten Pacitan
    url_pacitan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pacitan"
    df_pacitan = get_kelurahan_data(url_pacitan, 'Kabupaten Pacitan', 'jawa timur')

    # Kabupaten Pamekasan
    url_pamekasan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pamekasan"
    df_pamekasan = get_kelurahan_data(url_pamekasan, 'Kabupaten Pamekasan', 'jawa timur')

    # Kabupaten Pasuruan
    url_pasuruan = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Pasuruan"
    df_pasuruan = get_kelurahan_data(url_pasuruan, 'Kabupaten Pasuruan', 'jawa timur')

    # Kabupaten Ponorogo
    url_ponorogo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Ponorogo"
    df_ponorogo = get_kelurahan_data(url_ponorogo, 'Kabupaten Ponorogo', 'jawa timur')

    # Kabupaten Probolinggo
    url_probolinggo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Probolinggo"
    df_probolinggo = get_kelurahan_data(url_probolinggo, 'Kabupaten Probolinggo', 'jawa timur')

    # Kabupaten Sampang
    url_sampang = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sampang"
    df_sampang = get_kelurahan_data(url_sampang, 'Kabupaten Sampang', 'jawa timur')

    # Kabupaten Sidoarjo
    url_sidoarjo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sidoarjo"
    df_sidoarjo = get_kelurahan_data(url_sidoarjo, 'Kabupaten Sidoarjo', 'jawa timur')

    # Kabupaten Situbondo
    url_situbondo = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Situbondo"
    df_situbondo = get_kelurahan_data(url_situbondo, 'Kabupaten Situbondo', 'jawa timur')

    # Kabupaten Sumenep
    url_sumenep = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Sumenep"
    df_sumenep = get_kelurahan_data(url_sumenep, 'Kabupaten Sumenep', 'jawa timur')

    # Kabupaten Trenggalek
    url_trenggalek = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Trenggalek"
    df_trenggalek = get_kelurahan_data(url_trenggalek, 'Kabupaten Trenggalek', 'jawa timur')

    # Kabupaten Tuban
    url_tuban = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tuban"
    df_tuban = get_kelurahan_data(url_tuban, 'Kabupaten Tuban', 'jawa timur')

    # Kabupaten Tulungagung
    url_tulungagung = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Tulungagung"
    df_tulungagung = get_kelurahan_data(url_tulungagung, 'Kabupaten Tulungagung', 'jawa timur')

    # Kota Batu
    url_batu = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Batu"
    df_batu = get_kelurahan_data(url_batu, 'Kota Batu', 'jawa timur')

    # Kota Blitar
    url_blitar_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Blitar"
    df_blitar_kota = get_kelurahan_data(url_blitar_kota, 'Kota Blitar', 'jawa timur')

    # Kota Kediri
    url_kediri_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Kediri"
    df_kediri_kota = get_kelurahan_data(url_kediri_kota, 'Kota Kediri', 'jawa timur')

    # Kota Madiun
    url_madiun_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Madiun"
    df_madiun_kota = get_kelurahan_data(url_madiun_kota, 'Kota Madiun', 'jawa timur')

    # Kota Malang
    url_malang_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Malang"
    df_malang_kota = get_kelurahan_data(url_malang_kota, 'Kota Malang', 'jawa timur')

    # Kota Mojokerto
    url_mojokerto_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Mojokerto"
    df_mojokerto_kota = get_kelurahan_data(url_mojokerto_kota, 'Kota Mojokerto', 'jawa timur')

    # Kota Pasuruan
    url_pasuruan_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Pasuruan"
    df_pasuruan_kota = get_kelurahan_data(url_pasuruan_kota, 'Kota Pasuruan', 'jawa timur')

    # Kota Probolinggo
    url_probolinggo_kota = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Probolinggo"
    df_probolinggo_kota = get_kelurahan_data(url_probolinggo_kota, 'Kota Probolinggo', 'jawa timur')

    # Kota Surabaya
    url_surabaya = "https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Surabaya"
    df_surabaya = get_kelurahan_data(url_surabaya, 'Kota Surabaya', 'jawa timur')

    # GABUNGKAN SEMUA DATAFRAME KE DALAM SATU DATAFRAME
    df_all_jawa_timur = pd.concat([df_bangkalan, df_banyuwangi, df_blitar, df_bojonegoro, df_bondowoso,
                                df_gresik, df_jember, df_jombang, df_kediri, df_lamongan, df_lumajang,
                                df_madiun, df_magetan, df_malang, df_mojokerto, df_nganjuk, df_ngawi,
                                df_pacitan, df_pamekasan, df_pasuruan, df_ponorogo, df_probolinggo,
                                df_sampang, df_sidoarjo, df_situbondo, df_sumenep, df_trenggalek,
                                df_tuban, df_tulungagung, df_batu, df_blitar_kota, df_kediri_kota,
                                df_madiun_kota, df_malang_kota, df_mojokerto_kota, df_pasuruan_kota,
                                df_probolinggo_kota, df_surabaya], ignore_index=True)

    # Gunakan metode applymap dengan fungsi str.lower() untuk mengubah semua nilai menjadi huruf kecil
    df_all_jawa_timur = df_all_jawa_timur.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    values_to_remove = ['Gunung', 'Balekambang']

    # Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
    df_all_jawa_timur = df_all_jawa_timur[~df_all_jawa_timur['kelurahan'].isin(values_to_remove)]

    # Cetak DataFrame untuk memastikan perubahan telah dilakukan
    print(df_all_jawa_timur)

    # Ambil daftar kelurahan dari df_all_jawa_timur
    jawa_timur_kelurahan_list = df_all_jawa_timur['kelurahan'].tolist()

    # Buat query untuk setiap nama kelurahan
    jawa_timur_kelurahan_list = [kelurahan + ", Jawa Timur, Indonesia" for kelurahan in jawa_timur_kelurahan_list]
    print(jawa_timur_kelurahan_list)

    return df_all_jawa_timur