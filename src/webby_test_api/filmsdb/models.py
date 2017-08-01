from django.db import models


class Film(models.Model):
    class Meta:
        verbose_name = u'Фильм'
        verbose_name_plural = u'Фильмы'

    def __str__(self):
        return self.title

    title = models.CharField(
        verbose_name=u'Название фильма',
        max_length=255,
        blank=False,
    )

    year = models.PositiveSmallIntegerField(
        verbose_name=u'Год выпуска',
        blank=False,
    )

    FORMAT_VHS = 'v'
    FORMAT_DVD = 'd'
    FORMAT_BLU = 'b'
    FORMAT_CHOICES = (
        (FORMAT_VHS, 'VHS'),
        (FORMAT_DVD, 'DVD'),
        (FORMAT_BLU, 'Blu-Ray'),
    )

    format = models.CharField(
        verbose_name=u'Формат',
        max_length=1,
        choices=FORMAT_CHOICES,
    )

    actors = models.ManyToManyField(
        'Actor',
        verbose_name=u'Актеры',
        blank=True,
    )


class Actor(models.Model):
    class Meta:
        verbose_name = u'Актер'
        verbose_name_plural = u'Актеры'

    def __str__(self):
        return self.name

    name = models.CharField(
        verbose_name=u'Имя',
        max_length=255,
        blank=False,
    )
