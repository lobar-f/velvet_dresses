from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    category_name=models.CharField(max_length=255, verbose_name = "название")
    slug = models.SlugField(max_length=255, unique=True, null=True)


    def __str__(self):
        return self.category_name
    def get_absolute_url(self):
        return reverse('products:product_list_by_category',args=[self.slug])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


COLORS=[
 ('Красный', 'Красный'), 
  ('Чёрный', 'Чёрный'), 
  ('Белый', 'Белый'),
  ('Синий', 'Синий'),
   ('Золотой', 'Золотой'), 
  ('Серебряный', 'Серебряный'), 
  ('Розовый', 'Розовый'), 
  ('Бордовый', 'Бордовый'),
   ('Зелёный', 'Зелёный'), 
  ('Жёлтый', 'Жёлтый'),
  ('Фиолетовый', 'Фиолетовый'),
  ('Коричневый', 'Коричневый'),
   ('Оранжевый', 'Оранжевый')]


class Review(models.Model):
    image = ProcessedImageField(null=True, upload_to="media/review/%Y/%m/%d", 
                                           processors=[ResizeToFill(300, 660)],
                                           format='JPEG')
    text=models.CharField(max_length=255, verbose_name = "мнение")

class FAQ(models.Model):
    question=models.CharField(max_length=400, verbose_name = "Вопрос")
    answer=models.CharField(max_length=700, verbose_name = "ответ")


class MainImage(models.Model):
       image = ProcessedImageField(null=True, upload_to="media/products/%Y/%m/%d", 
                                           processors=[ResizeToFill(1200, 660)],
                                           format='JPEG')

class Size(models.Model):
    size=models.CharField(max_length=10,verbose_name = "Размер")
    def __str__(self):
        return self.size
class Product(models.Model):
    name= models.CharField(max_length=255, verbose_name = "название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Категория")
    slug = models.SlugField(max_length=255, unique=True,null=True)
    description = models.CharField(max_length=255, verbose_name = "описание")
    pub_date = models.DateField(default=timezone.now, verbose_name = "дата публикации")
    color=models.CharField(max_length=256, choices=COLORS, default='красный',  verbose_name = "Цвет")
    image=models.ImageField(upload_to='media/products/%Y/%m/%d')
    image2=models.ImageField(null=True, upload_to='media/products/%Y/%m/%d')
    image3=models.ImageField(null=True, upload_to='media/products/%Y/%m/%d')
    size=models.ManyToManyField(Size, verbose_name = "Размер")
    #material
    length=models.CharField(max_length=256, choices=[('длинная', 'длинная'), ('короткая', 'короткая'),('средний', 'средний')], default='длинная',  verbose_name = "длина")
    length_hand=models.CharField(max_length=256, choices=[('длинная', 'длинная'), ('короткая', 'короткая'),('средний', 'средний'),('нет', 'нет')], default='короткая',  verbose_name = "длина рукава")

    #fason
    favorite=models.BooleanField(default=0)
    image_thumbnail = ProcessedImageField(null=True, upload_to="media/products/%Y/%m/%d", 
                                           processors=[ResizeToFill(660, 1000)],
                                           format='JPEG')

   
 


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail',   args=[self.id, self.slug])
    class Meta:
        verbose_name_plural = "Одежда"
        ordering=("-pub_date",)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'media/images/')
 
    def __str__(self):
        return self.product.name
 