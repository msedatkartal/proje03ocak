from django.db import models

class Category(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    image = models.ImageField(("Kategori Resmi"), upload_to="category", max_length=200)
    
    def __str__(self):
        return self.title

class Card(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"))
    image = models.ImageField(("Kart Resmi"), upload_to="category", max_length=200)
    price = models.FloatField(("Fiyat"))
    isactive = models.BooleanField(("Aktif Kart"))
    date_now = models.DateField(("Tarih"), auto_now_add=False)
    new = models.BooleanField(("Yeni Ürün"),default=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    card = models.ForeignKey(Card, verbose_name=("Kart"), on_delete=models.CASCADE,null=True)
    fname = models.CharField(("İsim Soyisim"), max_length=50)
    text = models.TextField(("Yorum"))
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
    
    
    def __str__(self):
        return self.fname