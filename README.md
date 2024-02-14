# otopark-sayac-sistemi
Kullanılan Teknolojiler: Python, OpenCV, Tkinter, numpy, pickle kütüphaneleri.
![1](https://github.com/enesyondes/otopark-sayac-sistemi/assets/91937666/a2182966-14e5-41d2-94e7-ff52cc816a80)

Bu resimde gözüktüğü gibi otoparktaki boş alanları sayıyor ve bir çıktı üretiyor.

Program 3 kod sayfasından oluşuyor. 
1- Parking space picker sayfası. Bu kısımda elimizle park alanlarını işaretliyoruz ve bunları bir dosyaya kaydediyoruz CarParkSpace adındaki dosyaya kaydediyoruz.
2- Parking space counter sayfası. Bu kısımda ise CarParkSpace dosyasından çektiğimiz alanlara göre görüntü işleme teknikleri ile dikdörtgenlerin içindeki pikselleri sayarak bir eşik değer belirliyoruz. Dolu ya da boş şeklinde sınıflandırıyoruz.
3- main sayfası. Burada ise artık Tkinter kütüphanesi ile basit bir arayüz tasarlıyoruz ve diğer sayfalardaki kodları bu kısımda çağırıyoruz. 

Son olarak giriş bilgilerini bir .txt dosyasına kaydettim geliştirmek isteyen veritabanına çekerek programı geliştirebilir.
