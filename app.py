from faulthandler import disable
from pickle import READONLY_BUFFER
import urllib.parse
from urllib.request import urlopen
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import streamlit as st
import json
from streamlit_option_menu import option_menu
from PIL import Image


#Tittle ( Buat Cari Emoji ada disini https://www.webfx.com/tools/emoji-cheat-sheet/ )
st.set_page_config( page_title="Minang to Indonesia Translater", page_icon=":books:" )


#Header
with st.container():
    st.header("M i N A N G - T R A N S L A T E :books:")
    st.subheader(" BAHASA MINANGKABAU KE BAHASA INDONESIA ")

# Konten
#Navbar Option jadi 3
pilih = option_menu(
    menu_title=None,
    options=["Sejarah","Terjemahan","Tentang"],
    icons=["book","translate","info-circle-fill"],
    menu_icon=None,
    default_index=1,
    orientation="horizontal" )


#Navbar Sejarah
if pilih == "Sejarah":
    image1 = Image.open('minang1.png')
    st.image(image1)
    st.subheader("""
Berbicara tentang Minangkabau, maka kita akan dihadapkan pada sejarahnya yang begitu kompleks. Ini disebabkan karena beberapa hal yaitu:

Adanya perbedaan versi tentang sejarah Minangkabau itu sendiri
Masyarakat Minang zaman dulu tidak memiliki budaya tulis-menulis, sehingga kisah tentang Minangkabau selalu diturunkan melalui foktor. Upaya penulisan sejarah Minangkabau dalam bentuk Tambo (Hikayat, Babad) baru dimulai setelah Islam masuk pada kawasan tersebut
Berbagai Tambo tentang sejarah Minangkabau yang ditulis menggunakan abjad Arab sebagian besar masih tercampur dengan mitos, sehingga kebenarannya masih dipertanyakan para ahli.
Namun demikian, bukan berarti kita menjadi tutup mata dengan sejarah Minangkabau. Walau bagaimanapun, kawasan Minangkabau memiliki sejarah yang juga penting untuk diketahui. Melalui tulisan ini, kita akan mengkaji sedikit tentang sejarah Minangkabau yang tertuang dalam beberapa literatur.

Asal-usul Penamaan

Kata Minangkabau mengandung banyak pengertian. Kata tersebut tidak hanya merujuk pada nama desa yang terletak di kec. Sungayang kab. Tanah Datar, Sumatera Barat, tapi juga merujuk pada entitas suatu suku, bahasa dan budaya. Secara geografis, Minangkabau terdiri dari daratan Sumatera Barat, separuh daratan Riau, bagian barat Jambi, bagian utara Bengkulu, pantai barat Sumatera Utara, barat daya Aceh, dan Negeri Sembilan di Malaysia.

Nama Minangkabau sendiri berasal dari kata manang yang berarti menang dan kabau yang berarti kerbau. Nama itu diketahui dari sejarah yang ditulis di dalam Tambo. Kisahnya berawal pada saat kerajaan Pagaruyung yang dipimpin raja Adityawarman, akan ditaklukan oleh pasukan Majapahit.

Untuk mencegah pertempuran, penasehat raja mengusulkan adu kerbau sebagai pengganti peperangan. Jika kerbau dari pihak raja yang kalah, maka kerajaan akan diserahkan pada pasukan Majapahit. Sebaliknya, jika menang, pasukan Majapahit diminta untuk kembali ke Jawa. Akhirnya, usulan tersebut juga disetujui oleh pasukan Majapahit.

Singkat cerita, adu kerbau dimenangkan kerajaan Pagaruyung. Kemenangan tersebut pada akhirnya menginspirasikan masyarakat memakai nama Minangkabau, kata yang berasal dari ujaran “manangkabau” yang artinya kerbau yang menang.
Untuk mengenang kemenangan tersebut, masyarakat membuat sebuah rangkiang (Rumah Gadang) yang atapnya mengikuti bentuk tanduk kerbau. Kisah mengenai Minangkabau ini juga bisa ditemukan dalam Hikayat Raja-raja Pasai. Dalam hikayat itu tertulis bahwa kemenangan adu kerbau tersebut menjadikan kawasan yang sebelumnya bernama Pariangan menjadi Minangkabau.

Selain dari Tambo, nama Minangkabau juga bisa ditelusuri dari beberapa pendapat ahli sejarah, yaitu sebagai berikut:
NG. Poerbacaraka menyebut bahwa nama Minangkabau berasal dari kerajaan Minanga di Sumatra Barat. Hal ini didasarkan atas penemuan Prasasti Kedukan Bukit (683 Masehi) yang berada di Palembang. Dalam prasasti itu tertulis sepuluh baris kalimat yang diantaranya ada kata Minanga.
Ia mengatakan bahwa nama Minangkabau berasal dari kata “Menon Khabu” yang berarti Tanah Permai atau Tanah Pangkal.
Berbeda dengan Hussein Nainar, Vander Tuuk menganggap bahwa nama Minangkabau berasal dari kata “Pinang Khabu” yang berarti Tanah Asal.
Muhammad Zain berpendapat bahwa nama Minangkabau berasal dari kata “Binanga Kanvar” yang berarti Muara Kampar.
Nenek Moyang

Tidak hanya asal-usul nama Minangkabau, sejarah yang menyoal tentang nenek moyang masyarakat Minangkabau juga memiliki beragam versi, diantaranya ialah:

Menurut Tambo
Jika merujuk Pada Tambo, nenek moyang masyarakat Minangkabau berasal dari keturunan Iskandar Zulkarnain. Kisah di dalam Tambo ini juga terdapat pada hikayat Sulalatus Salatin. Dalam hikayat itu tertulis bahwa masyarakat Minangkabau pernah mengutus wakilnya untuk meminta Sang Sapurba (seorang keturunan Iskandar Zulkarnain) untuk menjadi raja mereka.
Kisah ini diragukan kebenarannya oleh para ahli karena terdapat kontradiksi. Maksudnya, kalaupun benar Sang Sapurba datang untuk menjadi raja, kenyataannya kawasan tersebut telah membentuk kelompok masyarakat yang sudah pasti memiliki nenek moyang.

Keterangan Beberapa Ahli
Beberapa ahli sejarah mengatakan bahwa nenek moyang masyarakat Minangkabau berasal dari bangsa Austronesia yang dulu bermukim di daerah Yunan, Cina Selatan. Mereka datang ke Nusantara ini dalam dua gelombang;

Gelombang pertama datang pada zaman Neolitikum ( Zaman Batu Baru) sekitar 2000 SM. Gelombang pertama ini oleh para ahli disebut bangsa Proto Melayu (Melayu Tua). Dari bangsa Melayu Tua ini berkembang menjadi suku Barak, Toraja, Dayak, Nias, Mentawai, Kubu dan lain-lain.
Gelombang kedua datang pada tahun 500 – 100 SM. Mereka yang datang pada gelombang kedua ini disebut Deutero Melayu (Melayu Muda). Dari bangsa Melayu Tua ini berkembang menjadi suku Minangkabau, Jawa, Makasar, Bugis dan lain-lain.

Agama
Saat ini, mayoratis agama masyarakat Minangkabau adalah Islam. Sebelum itu, mereka diyakini memeluk agama Budha karena pengaruh dari kerajaan Sriwijaya. Masuknya agama Islam ke kawasan tersebut diperkirakan melalui pesisir timur, bergerak dari daerah Inderagiri dan Arcat (Aru dan Rokan) yang saat itu telah menjadi pelabuhan Minangkabau ke arah pedalaman Minangkabau.
Dalam Sejarahnya, masyarakat Minang pernah mengalami perang saudara. Hal ini dipicu oleh konflik antara ulama dan pengikutnya yang bersikeras menerapkan hukum Islam dengan para kaum adat. Perang tersebut kemudian dikenal dengan Perang Padri. Perang Padri adalah perang saudara pertama di Asia Tenggara yang dipicu oleh konflik Agama.

Bahasa
Menurut sejarah yang  satu, masyarakat Minangkabau memiliki bahasa sendiri, bahkan bahasanya disebut-sebut termasuk ke dalam rumpun bahasa Austronesia. Sedangkan sejarah yang lain menyebut bahwa bahasa Minangkabau termasuk ke dalam bahasa Melayu, karena banyaknya kesamaan bentuk ujaran dan kosakata di dalamnya. Namun yang perlu diketahui, masyarakat penutur bahasa Minang itu sendiri juga telah memiliki berbagai macam dialek. Hal ini bergantung kepada daerahnya masing-masing.
Selain itu, bahasa lain seperti Sanskerta, Tamil, Arab dan Persia juga terserap ke dalam bahasa Minang. Ini bisa dilihat dari beberapa prasasti di Minangkabau yang ditulis menggunakan kosakata Sanskerta dan Tamil. Kemudian aksara Arab yang dahulu sering digunakan masyarakat Minang sebelum berganti menjadi Alfabet Latin.
""")

#Navbar Translate
if pilih == "Terjemahan":
    st.title(f"")    
    col1, col2, col3= st.columns(3)
    col4, col5, col6 = st.columns([3,2,3])



    with col1:
        minang = st.text_area('Kalimat','',max_chars=1000)

    with col2:
        with col4:
            st.write("")

        with col5:
            button3 = st.button('Hapus Jawaban')
            button = st.button('Minang - Indonesia')
            button2 = st.button('Indonesia - Minang')
            
        with col6:
            st.write("")

    with col3:
        #Translate Minang Ke indonesia
        if button:
            query = urllib.parse.quote_plus(str(minang))
            url = "https://bade.kopas.id/translator?versi=2&mode=1&bahasa=padang_minang&text="+query
            response = urlopen(url)
            data_json = json.loads(response.read())
            indo=data_json['response']['indonesia']
            indohasil=""
            for key in indo :
                indohasil=indohasil+str(key['k'])+" "
            hasil = st.text_area('Bahasa Indonesia',indohasil,disabled=True,max_chars=1000)

        if button2:
            #Translate Indonesia Ke Minang
            query = urllib.parse.quote_plus(str(minang))
            url = "https://bade.kopas.id/translator?versi=2&mode=2&bahasa=padang_minang&text="+query
            response = urlopen(url)
            data_json = json.loads(response.read())
            daerah=data_json['response']['daerah']
            daerahhasil=""
            for key in daerah :
                daerahhasil=daerahhasil+str(key['k'])+" "
            hasil = st.text_area('Bahasa Minang',daerahhasil,disabled=True,max_chars=1000)

        if button3:
            minang = st.text_area(" ",disabled=True)
      

#Navbar Tentang
if pilih == "Tentang":
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("-", "TR")
    col2.metric("T", "AN")
    col3.metric("I", "SL")
    col4.metric("M", "AT")
    col5.metric("-", "OR")

    #Robin
    coq1, coq2, coq3, coq4 = st.columns(4)
    coq1.metric("Robin Richard P.N","Leibniz","10418114")
    coq2.metric(" "," "," ")
    coq3.metric(" "," ")
    coq4.metric(" "," ")
    #Farhan
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(" "," ")
    col2.metric("Muhamad Farhan","amAIzing","10418192")
    col3.metric(" "," ")
    col4.metric(" "," ")
    #Dika
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(" "," ")
    col2.metric(" "," "," ")
    col3.metric("Dika Dwiyanti","amAIzing","1051904")
    col4.metric(" "," ")
    #Dafani
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(" "," ")
    col2.metric("Dafani Alifia Rasyada","Leibniz","B2A019038")
    col3.metric(" "," "," ")
    col4.metric(" "," ")
    #Niko
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Niko Taufiqurrokhman","Artemis","10418074")
    col2.metric(" "," "," ")
    col3.metric(" "," "," ")
    col4.metric(" "," ")


#Menghilangkan Bekas Streamlit
#Catatan ( Kalau visibility: hidden = Hilang ) - ( Kalau visibility: visible = Muncul )
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden}
            footer {visibility: hidden;}
            header {visibility: visible;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



#Koneksi Css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)