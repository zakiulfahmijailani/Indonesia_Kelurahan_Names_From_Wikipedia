from libraries import *

# Fungsi untuk mendapatkan data kelurahan dari halaman Wikipedia
def get_kelurahan_data(url, city_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='wikitable')
    kelurahan_list = []
    if table:
        rows = table.find_all('tr')
        header_row = rows[0]  # Ambil baris header
        header_columns = header_row.find_all('th')
        kelurahan_column_index = None
        for i, header_column in enumerate(header_columns):
            if 'Daftar Desa' in header_column.text or 'Daftar Desa/Kelurahan' in header_column.text or 'Daftar Kelurahan' in header_column.text:
                kelurahan_column_index = i
                break
        if kelurahan_column_index is not None:
            for row in rows[1:]:  # Lewati baris header
                columns = row.find_all('td')
                if len(columns) > kelurahan_column_index:
                    kelurahan_name = columns[kelurahan_column_index].text.strip()
                    kelurahan_list.append(kelurahan_name)
    kelurahan_list = [element.replace('\n', ', ').replace("'", "") for element in kelurahan_list]
    kelurahan_list = [item for element in kelurahan_list for item in element.split(', ')]
    data = {'kelurahan': kelurahan_list, 'kota': city_name}
    return pd.DataFrame(data)
