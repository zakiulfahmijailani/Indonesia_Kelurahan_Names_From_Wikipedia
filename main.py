from libraries import *
from function_custom import *
from individualProvinces.AaKelurahanAceh import get_df_all_aceh
from individualProvinces.AbBali import get_df_all_bali
from individualProvinces.AcBanten import get_df_all_banten
from individualProvinces.AdBengkulu import get_df_all_bengkulu
from individualProvinces.AeGorontalo import get_df_all_gorontalo
from individualProvinces.AfDkiJakarta import get_df_all_jakarta
from individualProvinces.AgJambi import get_df_all_jambi
from individualProvinces.AhJawaBarat import get_df_all_jabar
from individualProvinces.AiJawaTengah import get_df_all_jateng
from individualProvinces.AjJawaTimur import get_df_all_jatim
from individualProvinces.AkKalimantanBarat import get_df_all_kalbar
from individualProvinces.AlKalimantanSelatan import get_df_all_kalsel
from individualProvinces.AmKalimantanTengah import get_df_all_kalteng
from individualProvinces.AnKalimantanTimur import get_df_all_kaltim
from individualProvinces.AoKalimantanUtara import get_df_all_kalut
from individualProvinces.ApKepulauanBangkaBelitung import get_df_all_kepulauan_bangka_belitung
from individualProvinces.AqKepulauanRiau import get_df_all_kepri
from individualProvinces.ArLampung import get_df_all_lampung
from individualProvinces.AsMaluku import get_df_all_maluku
from individualProvinces.AtMalukuUtara import get_df_all_maluku_utara
from individualProvinces.AuNusaTenggaraBarat import get_df_all_ntb
from individualProvinces.AvNusaTenggaraTimur import get_df_all_ntt
from individualProvinces.AwPapua import get_df_all_papua
from individualProvinces.AxPapuaBarat import get_df_all_papua_barat
from individualProvinces.AyRiau import get_df_all_riau
from individualProvinces.AzSulawesiBarat import get_df_all_sulawesi_barat
from individualProvinces.BaSulawesiSelatan import get_df_all_sulawesi_selatan
from individualProvinces.BbSulawesiTengah import get_df_all_sulawesi_tengah
from individualProvinces.BcSulawesiTenggara import get_df_all_sulawesi_tenggara
from individualProvinces.BdSulawesiUtara import get_df_all_sulawesi_utara
from individualProvinces.BeSumateraBarat import get_df_all_sumatera_barat
from individualProvinces.BfSumateraSelatan import get_df_all_sumatera_selatan
from individualProvinces.BgSumateraUtara import get_df_all_sumatera_utara
from individualProvinces.BhYogyakarta import get_df_all_Yogyakarta

df_all_aceh = get_df_all_aceh()
df_all_bali= get_df_all_bali()
df_all_banten = get_df_all_banten()
df_all_bengkulu = get_df_all_bengkulu()
df_all_gorontalo = get_df_all_gorontalo()
df_all_jakarta = get_df_all_jakarta()
df_all_jambi = get_df_all_jambi()
df_all_jabar = get_df_all_jabar()
df_all_jateng = get_df_all_jateng()
df_all_jatim = get_df_all_jatim()
df_all_kalbar = get_df_all_kalbar()
df_all_kalsel = get_df_all_kalsel()
df_all_kalteng = get_df_all_kalteng()
df_all_kaltim = get_df_all_kaltim()
df_all_kalut = get_df_all_kalut()
df_all_kepulauan_bangka_belitung = get_df_all_kepulauan_bangka_belitung()
df_all_kepri = get_df_all_kepri()
df_all_lampung = get_df_all_lampung()
df_all_maluku = get_df_all_maluku()
df_all_maluku_utara = get_df_all_maluku_utara()
df_all_papua = get_df_all_papua()
df_all_papua_barat = get_df_all_papua_barat()
df_all_ntb = get_df_all_ntb()
df_all_ntt = get_df_all_ntt()
df_all_riau = get_df_all_riau()
df_all_sulawesi_barat = get_df_all_sulawesi_barat()
df_all_sulawesi_selatan = get_df_all_sulawesi_selatan()
df_all_sulawesi_tengah = get_df_all_sulawesi_tengah()
df_all_sulawesi_tenggara = get_df_all_sulawesi_tenggara()
df_all_sulawesi_utara = get_df_all_sulawesi_utara()
df_all_sumatera_barat = get_df_all_sumatera_barat()
df_all_sumatera_selatan = get_df_all_sumatera_selatan()
df_all_sumatera_utara = get_df_all_sumatera_utara()
df_all_Yogyakarta = get_df_all_Yogyakarta()


# List dataframes dari semua provinsi
list_dataframes = [df_all_aceh, df_all_bali, df_all_banten, df_all_bengkulu, df_all_gorontalo, df_all_jakarta,
                   df_all_jambi, df_all_jabar, df_all_jateng, df_all_jatim, df_all_kalbar,
                   df_all_kalsel, df_all_kalteng, df_all_kaltim, df_all_kalut,
                   df_all_kepulauan_bangka_belitung, df_all_riau, df_all_lampung, df_all_maluku, df_all_maluku_utara,
                   df_all_ntb, df_all_ntt, df_all_papua, df_all_papua_barat, df_all_riau,
                   df_all_sulawesi_barat, df_all_sulawesi_selatan, df_all_sulawesi_tengah, df_all_sulawesi_tenggara,
                   df_all_sulawesi_utara, df_all_sumatera_barat, df_all_sumatera_selatan, df_all_sumatera_utara,
                   df_all_Yogyakarta]

# Menggabungkan semua dataframes menjadi satu dataframe
df_semua_provinsi = pd.concat(list_dataframes, ignore_index=True)

# Lowercase
df_semua_provinsi = df_semua_provinsi.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Mengganti setiap nilai di DataFrame dengan nilai yang telah dihapus karakter non-latin
df_semua_provinsi = df_semua_provinsi.applymap(hapus_karakter_non_latin)

values_to_remove = ['lbskecamatan']

# Hapus baris yang sesuai dengan nilai yang ditentukan dalam variabel values_to_remove
df_semua_provinsi = df_semua_provinsi[~df_semua_provinsi['kelurahan'].isin(values_to_remove)]

# Cetak DataFrame hasil
print(df_semua_provinsi)
