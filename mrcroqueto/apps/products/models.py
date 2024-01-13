from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField

# Create your models here.


class CategoryProduct(models.Model):
    description = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description


class Products(models.Model):
    choices = [
        ("breakfast", "BREAKFAST"),
        ("lunch", "LUNCH"),
        ("dinner", "DINNER"),
        ("happy_hour", "HAPPY_HOUR"),
        ("all_day", "ALL_DAY"),
    ]
    name = models.CharField(max_length=50, unique=True)
    state = models.BooleanField(default=True)
    description = RichTextField()
    category_product = models.ManyToManyField(
        CategoryProduct, blank=True, related_name="category"
    )
    image = models.ImageField(upload_to="products/", default="menu_1.jpg")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    menu = models.CharField(max_length=50, choices=choices, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Redimensionar la imagen a 300x300 pixeles
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        super().save(*args, **kwargs)
