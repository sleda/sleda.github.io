import requests
import json
import tkinter as tk

# Instagram API istekleri için gerekli olan erişim anahtarını girin
access_token = "EAAWGHf9DVswBAEBiycF6Fc3les0TQZBjtIYBkH3Gm5GZB140ZC3cPXa57xn9kM8dVO1YoyHkSjjRoxyFLnsxm4aJRcVO4ilggZCLyJWOxcAl65AsKnPdNJXYioZCryGZBglb2PlGzp56vCNCshkbD5EGl3nU0ApLPbraixaZBIETdOjhTizLPxSkGYCXtOeJ96ilOxYgRVzaznFNv1YQoM2n5Kb6Jlu6tsZD"

# Tkinter penceresi oluşturun
window = tk.Tk()
window.title("Instagram Etkileşim Oranı Hesaplayıcı")

# Kullanıcı adını ve Instagram hesap bilgisini almak için etiketler ve girdi kutuları oluşturun
username_label = tk.Label(window, text="Kullanıcı Adı:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Etkileşim oranını hesaplamak için işlev oluşturun
def calculate_engagement_rate():
    # Kullanıcının takipçi sayısını ve gönderi sayısını alın
    response = requests.get(f"https://api.instagram.com/v1/users/self/?access_token={access_token}")
    data = json.loads(response.content.decode("utf-8"))
    follower_count = int(data["data"]["counts"]["followed_by"])
    media_count = int(data["data"]["counts"]["media"])

    # Kullanıcının son 12 gönderisini alın ve her gönderinin etkileşim sayısını hesaplayın
    response = requests.get(f"https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}")
    data = json.loads(response.content.decode("utf-8"))
    interactions = 0
    for post in data["data"][:12]:
        like_count = int(post["likes"]["count"])
        comment_count = int(post["comments"]["count"])
        interactions += like_count + comment_count

    # Etkileşim oranını hesaplayın ve kullanıcıya gösterin
    engagement_rate = interactions / (follower_count * media_count) * 100
    engagement_rate_label.configure(text=f"Etkileşim Oranı: {engagement_rate:.2f}%")

# Etkileşim oranını hesaplamak için bir düğme oluşturun
calculate_button = tk.Button(window, text="Etkileşim Oranını Hesapla", command=calculate_engagement_rate)
calculate_button.pack()

# Etkileşim oranını göstermek için bir etiket oluşturun
engagement_rate_label = tk.Label(window, text="")
engagement_rate_label.pack()

# Tkinter penceresini açın
window.mainloop()
