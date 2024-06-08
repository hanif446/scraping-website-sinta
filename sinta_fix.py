from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

app = Flask(__name__)

# Fungsi untuk login menggunakan Selenium
def login_sinta(driver, username, password):
    login_url = 'https://sinta.kemdikbud.go.id/logins'
    driver.get(login_url)

    username_elem = driver.find_element(By.NAME, "username")
    password_elem = driver.find_element(By.NAME, "password")

    username_elem.send_keys(username)
    password_elem.send_keys(password)
    password_elem.submit()
    time.sleep(5)


# Fungsi untuk mendapatkan total halaman profile
def get_total_pages_profile(driver, profile_url):
    datas = []
    try:
        driver.get(profile_url)

        # Gunakan page_source dari driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Temukan elemen yang berisi total halaman
        nav_element = soup.find('div', class_='text-center pagination-text')

        if nav_element:
            # Ambil teks dari elemen total halaman
            total_page_text = nav_element.text.strip()

            # Gunakan regex untuk ekstraksi nilai total records
            total_records_match = re.search(r'Page \d+ of (\d+)', total_page_text)
            if total_records_match:
                total_records = int(total_records_match.group(1))
                return total_records
            else:
                return None  # Atur nilai default jika tidak ditemukan informasi total halaman
        else:
            return None  # Atur nilai default jika tidak ditemukan elemen navigasi
    except Exception as e:
        print(f"An error occurred while getting total pages: {e}")
        return None  # Atur nilai default jika terjadi kesalahan

# Fungsi untuk mendapatkan total halaman scopus
def get_total_pages_scopus(driver, article_url):
    datas = []
    try:
        article_page_url = f"{article_url}?view=scopus"
        driver.get(article_page_url)

        # Gunakan page_source dari driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Temukan elemen yang berisi total halaman
        nav_element = soup.find('div', class_='text-center pagination-text')

        if nav_element:
            # Ambil teks dari elemen total halaman
            total_page_text = nav_element.text.strip()

            # Gunakan regex untuk ekstraksi nilai total records
            total_records_match = re.search(r'Page \d+ of (\d+)', total_page_text)
            if total_records_match:
                total_records = int(total_records_match.group(1))
                return total_records
            else:
                return None  # Atur nilai default jika tidak ditemukan informasi total halaman
        else:
            return None  # Atur nilai default jika tidak ditemukan elemen navigasi
    except Exception as e:
        print(f"An error occurred while getting total pages: {e}")
        return None  # Atur nilai default jika terjadi kesalahan
    
# Fungsi untuk mendapatkan total halaman wos
def get_total_pages_wos(driver, article_url):
    try:
        article_page_url = f"{article_url}?view=wos"  # Menambahkan parameter view=wos
        driver.get(article_page_url)  # Navigasi menggunakan Selenium

        # Gunakan page_source dari driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Temukan elemen yang berisi total halaman
        nav_element = soup.find('div', class_='text-center pagination-text')

        if nav_element:
            # Ambil teks dari elemen total halaman
            total_page_text = nav_element.text.strip()

            # Gunakan regex untuk ekstraksi nilai total records
            total_records_match = re.search(r'Page \d+ of (\d+)', total_page_text)
            if total_records_match:
                total_records = int(total_records_match.group(1))
                return total_records
            else:
                return None  # Atur nilai default jika tidak ditemukan informasi total halaman
        else:
            return None  # Atur nilai default jika tidak ditemukan elemen navigasi
    except Exception as e:
        print(f"An error occurred while getting total pages: {e}")
        return None  # Atur nilai default jika terjadi kesalahan

# Fungsi untuk mendapatkan total halaman garuda
def get_total_pages_garuda(driver, article_url):
    try:
        article_page_url = f"{article_url}?view=garuda"  # Menambahkan parameter view=garuda
        driver.get(article_page_url)  # Navigasi menggunakan Selenium

        # Gunakan page_source dari driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Temukan elemen yang berisi total halaman
        nav_element = soup.find('div', class_='text-center pagination-text')

        if nav_element:
            # Ambil teks dari elemen total halaman
            total_page_text = nav_element.text.strip()

            # Gunakan regex untuk ekstraksi nilai total records
            total_records_match = re.search(r'Page \d+ of (\d+)', total_page_text)
            if total_records_match:
                total_records = int(total_records_match.group(1))
                return total_records
            else:
                return None  # Atur nilai default jika tidak ditemukan informasi total halaman
        else:
            return None  # Atur nilai default jika tidak ditemukan elemen navigasi
    except Exception as e:
        print(f"An error occurred while getting total pages: {e}")
        return None  # Atur nilai default jika terjadi kesalahan

# Fungsi untuk mendapatkan total halaman google_scholar
def get_total_pages_google_scholar(driver, article_url):
    try:
        article_page_url = f"{article_url}?view=googlescholar" # Menambahkan parameter view=google schoolar
        driver.get(article_page_url)

        # Gunakan page_source dari driver
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Temukan elemen yang berisi total halaman
        nav_element = soup.find('div', class_='text-center pagination-text')

        if nav_element:
            # Ambil teks dari elemen total halaman
            total_page_text = nav_element.text.strip()

            # Gunakan regex untuk ekstraksi nilai total records
            total_records_match = re.search(r'Page \d+ of (\d+)', total_page_text)
            if total_records_match:
                total_records = int(total_records_match.group(1))
                return total_records
            else:
                return None  # Atur nilai default jika tidak ditemukan informasi total halaman
        else:
            return None  # Atur nilai default jika tidak ditemukan elemen navigasi
    except Exception as e:
        print(f"An error occurred while getting total pages: {e}")
        return None  # Atur nilai default jika terjadi kesalahan
    

# Fungsi untuk melakukan scraping dan mengembalikan data pada profile 
def scrape_data_profile(driver, profile_urls):
    datas = []

    for profile_url in profile_urls:
        # Get total pages
        total_pages_profile = get_total_pages_profile(driver, profile_url)

        if total_pages_profile is None:
            continue
        
        for page in range(1, total_pages_profile + 1):
            profile_page_url = f"{profile_url}?page={page}"
            driver.get(profile_page_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            author = soup.findAll('div', 'au-item mt-3 mb-3 pb-5 pt-3')
            for auth in author:
                img = auth.find('img', 'img-thumbnail avatar')
                img_src = img.get('src')
                name_get = auth.find('div', 'profile-name').text
                name = name_get.title()
                sinta_id_element = soup.find('div', 'profile-id')
                sinta_id = sinta_id_element.get_text().replace('ID :', '').strip()
                datas.append([name, sinta_id, img_src])
    return datas

# Fungsi untuk melakukan scraping dan mengembalikan data pada artikel (scopus)
def scrape_data_article_scopus(driver, article_urls):
    datas = []

    for article_url in article_urls:
        # Get total pages
        total_pages_scopus = get_total_pages_scopus(driver, article_url)

        # datas.append([total_pages_scopus])

        if total_pages_scopus is None:
            continue

        for page in range(1, total_pages_scopus + 1):
            article_page_url = f"{article_url}?page={page}&view=scopus"
            driver.get(article_page_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            article = soup.findAll('div', 'ar-list-item mb-5')

            for art in article:
                try:
                    title_div = art.find('div', 'ar-title')
                    title = title_div.a.text.strip()
                    link_article = title_div.a['href']
                    index = art.find('a', 'ar-quartile').text.strip()
                    jurnal = art.find('a', 'ar-pub').text.strip()
                    link_jurnal = art.find('a', 'ar-pub')['href']
                    creator_element = art.select('div.ar-meta a:nth-of-type(3)')
                    creator = creator_element[0].get_text()
                    year = art.find('a', 'ar-year').text.strip()
                    cited = art.find('a', 'ar-cited').text.strip()

                    datas.append([title, link_article, index, jurnal, link_jurnal, creator, year, cited])
                except Exception as e:
                    print(f"An error occurred while scraping article: {e}")

    return datas

# # Fungsi untuk melakukan scraping dan mengembalikan data pada artikel (wos)
def scrape_data_article_wos(driver, article_urls):
    datas = []

    for article_url in article_urls:
        # Get total pages
        total_pages_wos = get_total_pages_wos(driver, article_url)

        if total_pages_wos is None:
            continue

        for page in range(1, total_pages_wos + 1):
            article_page_url = f"{article_url}?page={page}&view=wos"
            driver.get(article_page_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            article = soup.findAll('div', 'ar-list-item mb-5')

            for art in article:
                try:
                    title_div = art.find('div', 'ar-title')
                    title = title_div.a.text.strip() 
                    link_article = title_div.a['href']
                    index = art.find('a', 'ar-quartile mr-3').text.strip()
                    jurnal = art.find('a', 'ar-pub').text.strip()
                    pub_element = art.select('div.ar-meta a:nth-of-type(4)')
                    publikasi = pub_element[0].get_text().strip()
                    pub_link = pub_element[0]['href']
                    author_element = art.select('div.ar-meta a:nth-of-type(5)')
                    author = author_element[0].get_text().strip()

                    # Menggunakan regex untuk mengekstrak tahun dari string
                    year_match = re.search(r'\b\d{4}\b', art.find('a', 'ar-year').text.strip())
                    if year_match:
                        year = year_match.group()
                    else:
                        # Jika tidak ada tahun, kita dapat menangani kasus ini sesuai kebutuhan
                        year = ''

                    cited  = art.find('a', 'ar-cited').text.strip()
                    accred = art.find('span', 'num-stat scopus-indexed ml-3').text.strip()
                    try : doi = art.find('a', 'ar-sinta')['href']
                    except : doi = ''

                    datas.append([title, link_article, index, jurnal, publikasi, pub_link, author, year, cited, accred, doi])
                 
                except Exception as e:
                    print(f"An error occurred while scraping article: {e}")

    return datas

# Fungsi untuk melakukan scraping dan mengembalikan data pada artikel (garuda)
def scrape_data_article_garuda(driver, article_urls):
    datas = []

    for article_url in article_urls:
        # Get total pages
        total_pages_garuda = get_total_pages_garuda(driver, article_url)

        # datas.append([total_pages_garuda])

        if total_pages_garuda is None:
            continue

        for page in range(1, total_pages_garuda + 1):
            article_page_url = f"{article_url}?page={page}&view=garuda"
            driver.get(article_page_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            article = soup.findAll('div', 'ar-list-item mb-5')

            for art in article:
                try: 
                    title_div = art.find('div', 'ar-title')
                    title = title_div.a.text.strip() 
                    link_article = title_div.a['href']
                    index_element = art.select('div.ar-meta a:nth-of-type(1)')
                    index = index_element[0].get_text().strip()
                    jurnal = art.find('a', 'ar-pub').text.strip()
                    link_jurnal = art.find('a', 'ar-pub')['href']
                    year = art.find('a', 'ar-year').text.strip()
                    doi  = art.find('a', 'ar-cited').text.strip()
                    accred = art.find('a', 'ar-quartile').text.strip()

                    datas.append([title, link_article, index, jurnal, link_jurnal, year, doi, accred])
                except Exception as e:
                    print(f"An error occurred while scraping article: {e}")

    return datas

# Fungsi untuk melakukan scraping dan mengembalikan data pada artikel (google scholar)
def scrape_data_article_google_scholar(driver, article_urls):
    datas = []

    for article_url in article_urls:
        # Get total pages
        total_pages_google_scholar = get_total_pages_google_scholar(driver, article_url)

        # datas.append([total_pages_google_scholar])

        if total_pages_google_scholar is None:
            continue

        for page in range(1, total_pages_google_scholar + 1):
            article_page_url = f"{article_url}?page={page}&view=googlescholar"
            driver.get(article_page_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            article = soup.findAll('div', 'ar-list-item mb-5')

            for art in article:
                try:
                    title_div = art.find('div', 'ar-title')
                    title = title_div.a.text.strip()
                    link_article = title_div.a['href']
                    author_element = art.select('div.ar-meta a:nth-of-type(1)')
                    author = author_element[0].get_text().strip()
                    jurnal = art.find('a', 'ar-pub').text.strip()
                    year = art.find('a', 'ar-year').text.strip()
                    cited  = art.find('a', 'ar-cited').text.strip()
                    
                    datas.append([title, link_article, author, jurnal, year, cited])
                except Exception as e:
                    print(f"An error occurred while scraping article: {e}")
    
    return datas

profile_urls = [
    'https://sinta.kemdikbud.go.id/departments/authors/520/8B47E80A-3A42-4412-BDF2-7E5F853A0717/2DC09F85-E112-44C9-9ED2-471434CC1446',
    'https://sinta.kemdikbud.go.id/departments/authors/520/8B47E80A-3A42-4412-BDF2-7E5F853A0717/5BA41BB8-A2AF-4BBD-9019-2369D643AA34'
]

article_urls = [
    'https://sinta.kemdikbud.go.id/departments/profile/520/8B47E80A-3A42-4412-BDF2-7E5F853A0717/2DC09F85-E112-44C9-9ED2-471434CC1446',
    'https://sinta.kemdikbud.go.id/departments/profile/520/8B47E80A-3A42-4412-BDF2-7E5F853A0717/5BA41BB8-A2AF-4BBD-9019-2369D643AA34'
]

@app.route('/profile')
def get_profile_data():
    # Inisialisasi driver Gecko (Firefox)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Login ke Sinta
    login_sinta(driver, "USERNAME", "PASSWORD")

    # Lakukan scraping dan dapatkan data
    scraped_data_profile = scrape_data_profile(driver, profile_urls)

    # Tutup browser Selenium setelah selesai
    driver.quit()

    return jsonify(scraped_data_profile)

@app.route('/article_scopus')
def get_article_scopus_data():
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    login_sinta(driver, "USERNAME", "PASSWORD")

    scraped_data_article_scopus = scrape_data_article_scopus(driver, article_urls)

    driver.quit()

    return jsonify(scraped_data_article_scopus)
    

@app.route('/article_wos')
def get_article_wos_data():
    # Inisialisasi driver Gecko (Firefox)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Login ke Sinta
    login_sinta(driver, "USERNAME", "PASSWORD")

    # Lakukan scraping dan dapatkan data
    scraped_data_article_wos = scrape_data_article_wos(driver, article_urls)

    # Tutup browser Selenium setelah selesai
    driver.quit()

    return jsonify(scraped_data_article_wos)

@app.route('/article_garuda')
def get_article_garuda_data():
    # Inisialisasi driver Gecko (Firefox)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Login ke Sinta
    login_sinta(driver, "USERNAME", "PASSWORD")

    # Lakukan scraping dan dapatkan data
    scraped_data_article_garuda = scrape_data_article_garuda(driver, article_urls)

    # Tutup browser Selenium setelah selesai
    driver.quit()

    return jsonify(scraped_data_article_garuda)

@app.route('/article_google_scholar')
def get_article_google_scholar_data():
    # Inisialisasi driver Gecko (Firefox)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Login ke Sinta
    login_sinta(driver, "USERNAME", "PASSWORD")

    # Lakukan scraping dan dapatkan data
    scraped_data_article_google_scholar = scrape_data_article_google_scholar(driver, article_urls)

    # Tutup browser Selenium setelah selesai
    driver.quit()

    return jsonify(scraped_data_article_google_scholar)

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Menggunakan ChromeDriverManager untuk mengelola versi ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Inisialisasi driver Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)

    app.run(host='0.0.0.0', port=5000)
