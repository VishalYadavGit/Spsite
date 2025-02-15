from SP.models import Brand

for brand in Brand.objects.all():
    if not brand.brand_img:
        brand.brand_img = "motor.jpg"
        brand.save()