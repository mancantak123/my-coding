<h1 align="center"> Selamat Datang di CodeBase-centra </h1>
<p align="center">
  Platform ini merupakan repositori pusat yang didedikasikan sebagai wadah integrasi bagi seluruh dokumentasi skrip dan karya digital yang telah dikembangkan secara personal oleh <b>Nikco</b>.
</p>
<p align="center">
  <i>"Sebuah laboratorium digital yang dinamis untuk memvalidasi efisiensi kode serta mengasah ketajaman pemecahan masalah dalam berbagai skenario komputasi yang kompleks."</i>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Focus-Competitive%20Programming-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-red?style=flat-square">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Topic-Data%20Structures-orange?style=flat-square&logo=databricks&logoColor=white">
</p>
<p align="justify">
  Platform ini merupakan sebuah <b>repositori pusat</b> yang didedikasikan sebagai wadah integrasi bagi seluruh dokumentasi skrip dan karya digital yang telah dikembangkan secara personal oleh <b>Nikco</b>. Arsip ini merangkum evolusi teknis yang komprehensif, mulai dari implementasi sintaks <b>fundamental</b> dan logika dasar pemrograman hingga pengembangan <b>algoritma tingkat tinggi</b> yang dirancang khusus untuk memenuhi kebutuhan <b>competitive programming</b>. Lebih dari sekadar tempat penyimpanan data, platform ini berfungsi sebagai <b>laboratorium digital</b> yang dinamis untuk melakukan berbagai ujicoba program dan eksperimen teknis, guna memvalidasi efisiensi kode serta mengasah ketajaman pemecahan masalah dalam berbagai skenario komputasi yang kompleks.
</p>


### Bahasa Pemrograman dan Lingkungan

<table>
  <tr>
    <td width="100"><b>C++</b></td>
    <td>
      <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" align="center">
      &nbsp; Fokus pada implementasi algoritma berperforma tinggi dan penyelesaian tantangan kompetitif.
    </td>
  </tr>
  <tr>
    <td><b>Python</b></td>
    <td>
      <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" align="center">
      &nbsp; Digunakan untuk logika prototyping, analisis data, dan pengembangan skrip otomasi.
    </td>
  </tr>
</table>

### Spesifikasi Teknis

* **Antarmuka:** Berbasis **CLI (Command Line Interface)** untuk menjamin efisiensi eksekusi maksimal.
* **Compiler dan Alat:**
  * **C++:** Menggunakan compiler `g++ (MinGW/GCC)` atau **Dev-C++**.
  * **Python:** Menggunakan interpreter `Python 3.x` dengan **VS Code**.
### 📥 Cara Mengunduh Repositori
Anda dapat menduplikasi seluruh isi repositori ini ke perangkat lokal Anda dengan langkah-langkah berikut:

1. Buka Terminal atau Command Prompt.
2. Jalankan perintah *clone* berikut:
   ```bash
   git clone https://github.com/mancantak123/my-coding.git

<h2 align="center">Panduan competitve programing</h2>

<p align="justify">
  <b>Gulir dan pilih penjelasan atau panduan folder yang anda cari</b> , di bawah ini untuk melihat panduan teknis . Sebagian besar materi pemrograman kompetitif dalam repositori ini diambil langsung dari soal-soal latihan pada platform TLX (https://tlx.toki.id/courses).
</p>

<hr />

<details style="margin-bottom: 20px; border: 1px solid #333; border-radius: 8px; background: #1a1a1a;">
  <summary style="padding: 15px; cursor: pointer; font-weight: bold; color: #fff; background: #2d2d2d; border-radius: 8px;">
    📂 Paduan Competitive programing 1&2 
  </summary>
  <br>
  <p><i><b>Competitive programing</b></i> adalah program pengenalan dan contoh program competitive , dimana anda mengenal nama batasan waktu dan batasan memory untuk program , selain itu anda dapat menemukan batasan tipe Data yang digunakan oleh program</p>
  
  <h3>Deskripsi</h3>
<p>
  Diberikan <i>N</i> buah bilangan bulat: <i>A</i><sub>1</sub> hingga <i>A</i><sub><i>N</i></sub>. 
  Anda ingin mengetahui, untuk setiap 1 &le; <i>i</i> &le; <i>N</i>, berapakah jumlah dari 
  keseluruhan bilangan bulat tersebut kecuali <i>A<sub>i</sub></i>.
</p>
<h3>Masukan</h3>
<p>Masukan diberikan dalam format berikut:</p>

<div style="background-color: #0d1117; color: white; padding: 15px; border-radius: 8px; font-family: monospace;">
   <blockquote>
    N<br>
    A<sub>1</sub><br>
    :<br>
    A<sub>N</sub>
   </blockquote>
</div>

<h3>Keluaran</h3>
<p>
    Keluarkan <i>N</i> buah baris. Baris ke-<i>i</i> berisi jumlah dari keseluruhan bilangan bulat tersebut kecuali <i>A<sub>i</sub></i>.
</p>
<h3>Contoh Masukan</h3>

<div>
  <blockquote style="background-color:#0d1117">
    8<br>
    100<br>
    281923<br>
    7<br>
    1000000<br>
    777777<br>
    123456<br>
    9999999<br>
    7239
  </blockquote>
</div>
</details>
<details style="margin-bottom: 20px; border: 1px solid #333; border-radius: 8px;">
  <summary style="padding: 15px; cursor: pointer; font-weight: bold; color: #fff;border-radius: 8px;">
    📂 cek Bilangan Prima
  </summary>
  <br>
  <p align="justify">Didalam folder cek Bilangan prima adalah sebuah program yang <i><b>berkhusus untuk mengecek bilangan n prima</b></i>. dengan cara mencari nilai batas atas dari akar kuadrat dari p($$\sqrt{p}$$) , lalu n prima dibagi mulai dari bilangan bulat 2 hingga nilai batas akar kuadrat p($$\sqrt{p}$$). Jika tidak ada bilangan yang tidak bisa dibagi diantara 2 sampai akar kuadrat dari p , maka n adalah bilangan prima , sebalik dia ada bilangan bisa dibagi maka , dia bukan bilangan prima.</p>
<div>
  <h3>Batasan</h3>
  <blockqueto>
    <ul>
      <li>1 &le; <i>Q</i> &le; 1000</li>
      <li>1 &le; <i>N<sub>i</sub></i> &le; 1 000 000</li>
    </ul>
  </blockqueto>
</div>
<h3>Masukan</h3>
<p>Masukan diberikan dalam format berikut:</p>

<div>
    <blockquate>
      <pre style="margin: 0;">
<i>Q</i>
<i>N</i><sub>1</sub>
<i>N</i><sub>2</sub>
&#8942;
<i>N</i><sub><i>Q</i></sub></pre>
    </blockquate>
</div>
<div>
  <h3>keluaran</h3>
  <p>Untuk setiap bilangan, keluarkan sebuah baris berisi <b><i>YA</i></b> apabila bilangan tersebut prima, atau <b><i>BUKAN</i></b> jika bukan prima.</p>
</div>
  <div style="background-color: #0d1117; color: white; padding: 15px; border-radius: 8px; font-family: monospace;">
   <h3>contoh masukan</h3>
    <blockquote>
4<br>
1<br>
2<br>
3<br>
4
   </blockquote>
</div>
<div>
  <h3>contoh keluaran</h3>
  <blockquate>
BUKAN<br>
YA<br>
YA<br>
BUKAN
    </blockquate>
</div>
</details>
<details style="margin-bottom: 20px; border: 1px solid #333; border-radius: 8px; background: #1a1a1a;">
  <summary style="padding: 15px; cursor: pointer; font-weight: bold; color: #fff; background: #2d2d2d; border-radius: 8px;">
    📂 Statiska sederhana
  </summary>
  <div style="padding: 20px; color: #fff;">
    <br>
    <p>Didalam folder Statiska sederhana adalah sebuah program yang <i><b> mencari data terbesar dan terkecil yang mulai index data 0</b></i>.</p>
  </div>
  <h3>Batasan</h3>
  <blockqueto>
  <ul>
  <li>1 &le; <i>N</i> &le; 100</li>
  <li>-100 000 &le; <i>A<sub>i</sub></i> &le; 100 000</li>
</ul>
  </blockqueto>
</div>

<p>Masukan diberikan dalam format berikut:</p>

<div style="background-color: #0d1117; color: white; padding: 15px; border-radius: 8px; font-family: monospace;">
   <blockquote>
    <b>N</b><br>
    <b>A</b><sub>1</sub> <b>A</b><sub>2</sub> ... <b>A</b><sub>N</sub>
   </blockquote>
</div>
  <h3>keluaran</h3>
  <p>coming soon</p>
  <p>.</p>
</details>

<details style="margin-bottom: 20px; border: 1px solid #333; border-radius: 8px; background: #1a1a1a;">
  <summary style="padding: 15px; cursor: pointer; font-weight: bold; color: #fff; background: #2d2d2d; border-radius: 8px;">
    📂 SEARCH: /coming soon
  </summary>
  <div style="padding: 20px; color: #fff;">
    <p align="center"><i>Konten panduan folder coming soon.</i></p>
  </div>
</details>
<hr />

