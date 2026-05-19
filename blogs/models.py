from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'blogs'
        ordering = ['date_added']

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'
        ordering = ['-date_added']


    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(str(self.text)) > 50:
            return f"{str(self.text)[:50]}..."
        return str(self.text)
