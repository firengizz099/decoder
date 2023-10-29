# Decoder
**Decoder, özellikle dil işleme ve yapay zeka alanlarında kullanılan bir terimdir. Decoder, kodlanmış veriyi veya bilgiyi anlamlı bir forma çevirmek için kullanılan bir bileşendir. Encoder ile kodlanmış veriyi, orijinal veya anlamlı bir formata dönüştürmek amacıyla kullanılır.**

**Decoder terimi, özellikle dil modelleri ve yapay zeka alanında sıkça kullanılır. Örneğin, bir dil modeli (örneğin, bir metin oluşturan veya anlam çıkaran bir model) bir giriş metni alır, bu girişi kodlar (embeds) ve ardından bu kodu daha anlamlı bir metin olarak çevirmek için bir decoder kullanır.**


1)**import json ile JSON** işlemleri için gerekli olan json modülünü içe aktarıyoruz.

with open("text.json", "r") as file: ile "text.json" adlı JSON dosyasını okuma modunda açıyoruz ve bu dosyayı file adlı bir değişkene atıyoruz.

data = json.load(file) ile JSON dosyasındaki verileri data adlı bir sözlüğe yüklüyoruz. Bu sözlük, "word_to_number" ve "responses" adlı iki anahtar ile iki alt sözlüğü içerir.

2)**word_to_number = data["word_to_number"]** ile "word_to_number" adlı alt sözlüğü alıyoruz. Bu alt sözlüğü, kullanıcı girişlerini kodlamak için kullanacağız.

3)**def decode(encoded_input, data):** ile decode adlı bir fonksiyon tanımlıyoruz. Bu fonksiyon, kodlanmış girişi kullanarak yanıtları almak için kullanılacak. Veritabanındaki "responses" alt sözlüğünden yanıtları döndürür.

4)**def get_response(user_input, data):** ile get_response adlı bir fonksiyon tanımlıyoruz. Bu fonksiyon, kullanıcı girişini alır, eğer giriş veritabanındaki metinlerle eşleşirse kodlar ve yanıtı döndürür. Aksi takdirde, girişi doğrudan yanıt olarak döndürür.

5)**while True:** ile sonsuz bir döngü başlatıyoruz. Kullanıcı her seferinde bir giriş yapar.

user_input = input("Kullanıcı: ") ile kullanıcıdan bir giriş alıyoruz.

response = get_response(user_input, data) ile kullanıcının girişini get_response fonksiyonuna veriyoruz ve geri dönen yanıtı alıyoruz.

print("Chat Bot: ", response) ile Chat Bot'un yanıtını ekrana yazdırıyoruz.

**Bu kod, kullanıcı girişlerini kodlamak ve bu kodları kullanarak yanıtlar almak için bir veritabanını kullanır. JSON dosyasındaki veriler, kullanıcı girişlerini tanımlamak ve bu girişlere karşılık gelen yanıtları içerir. Kullanıcı girişi veritabanındaki metinlerle eşleşirse, ilgili yanıt döndürülür; aksi takdirde, kullanıcı girişi doğrudan yanıt olarak döndürülür.**
