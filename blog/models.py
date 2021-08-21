# blog/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
      return reverse('post_detail', args=[str(self.id)])
"""
В верхней части мы импортируем класс models а затем создаем подкласс models.Model с 
именем Post. Используя функционал подкласса, мы автоматически имеем доступ ко всему 
в django.db.models.Models и можем добавлять дополнительные поля и методы по 
своему желанию.
Для title мы ограничиваем длину до 200 символов, а для body мы используем текстовое 
поле, которое будет автоматически расширяться по мере необходимости, чтобы 
соответствовать тексту пользователя. В Django доступно много типов полей; вы можете 
увидеть полный список здесь. 
Для поля author мы используем ForeignKey это предоставляет связь многие-к-одному .
Это означает, что данный пользователь может быть автором многих различных постов в 
блоге, но не наоборот. Ссылка на встроенную модель User которой Django обеспечивает 
аутентификацию. Для всех связей многие-к-одному таких как ForeignKey нам также 
необходимо указать параметр on_delete .

python manage.py makemigrations blog
python manage.py migrate blog
"""
