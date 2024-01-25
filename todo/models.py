from django.db import models



class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    completed = models.BooleanField(default=False, verbose_name="Выполнено")

    def __str__(self):
        return self.title
