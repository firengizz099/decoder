import json

# Veri dosyasını yükle
with open("text.json", "r") as file:
    data = json.load(file)

# Örnek bir word_to_number sözlüğü
word_to_number = data["word_to_number"]

# Decoder işlemi
def decode(encoded_input, data):
    responses = data["responses"]
    
    response = responses.get(encoded_input, "Üzgünüm, bu soruya cevap veremem.")
    return response

def get_response(user_input, data):
    encoded_input = data["word_to_number"].get(user_input, user_input)
    return decode(str(encoded_input), data)

while True:
    user_input = input("Kullanıcı: ")
    
    response = get_response(user_input, data)
    print("Chat Bot: ", response)
