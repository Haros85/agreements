from django.db import models


# Таблица наименование организации/ФОИВ
class Foiv(models.Model):
    title = models.CharField(max_length=250, verbose_name=u"Полное название ФОИВ")
    short = models.CharField(max_length=20, verbose_name=u"Краткое название ФОИВ")

    class Meta:
        verbose_name = u"ФОИВ"
        verbose_name_plural = u"ФОИВы"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Подразделения
class Department(models.Model):
    title = models.CharField(max_length=30, verbose_name=u"Ответственные подразделения")

    class Meta:
        verbose_name = u"Подразделение"
        verbose_name_plural = u"Подразделения"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Соглашения
class Agreements(models.Model):
    foiv_id = models.ForeignKey(Foiv, on_delete=models.CASCADE, verbose_name=u"ФОИВ")
    title = models.CharField(max_length=250, verbose_name=u"Название соглашения")
    number = models.CharField(max_length=20, verbose_name=u"Регистрационный номер")
    reg_date = models.DateField(verbose_name=u"Дата заключения соглашения")
    inv_number = models.CharField(max_length=20, verbose_name=u"Инвентарный номер", blank=True, null=True)
    subject = models.TextField(verbose_name=u"Предмет соглашения")
    departments = models.ManyToManyField(
        Department,
        verbose_name=u"Уполномоченные подразделения", blank=True
    )
    note = models.TextField(verbose_name=u"Примечание", blank=True, null=True)
    file = models.FileField(upload_to='agreements/', verbose_name=u"Соглашение(PDF-формат)", blank=True, null=True)

    @property
    def display_dept(self):
        return ", ".join([departments.title for departments in self.departments.all()])

    class Meta:
        verbose_name = u"Соглашение"
        verbose_name_plural = u"Соглашения"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Дополнительные соглашения
class Additional(models.Model):
    agr_id = models.ForeignKey(Agreements, on_delete=models.CASCADE, verbose_name=u"Соглашение")
    title = models.CharField(max_length=250, verbose_name=u"Название доп.соглашения")
    number = models.CharField(max_length=20, verbose_name=u"Регистрационный номер")
    reg_date = models.DateField(verbose_name=u"Дата заключения доп.соглашения")
    inv_number = models.CharField(max_length=20, verbose_name=u"Инвентарный номер", blank=True, null=True)
    subject = models.TextField(verbose_name=u"Предмет доп.соглашения", blank=True, null=True)
    departments = models.ManyToManyField(
        Department,
        verbose_name=u"Уполномоченные подразделения", blank=True
    )
    note = models.TextField(verbose_name=u"Примечание", blank=True, null=True)
    file = models.FileField(upload_to='additional/', verbose_name=u"Доп.соглашение(PDF-формат)", blank=True, null=True)

    @property
    def display_dept(self):
        return ", ".join([departments.title for departments in self.departments.all()])

    class Meta:
        verbose_name = u"Доп. соглашение"
        verbose_name_plural = u"Доп. соглашения"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# Таблица Типы протоколов
class Type(models.Model):
    type_protocol = models.CharField(max_length=50, verbose_name=u"Тип протокола")
    short_name = models.CharField(max_length=20, verbose_name=u"Аббревиатура", blank=True, null=True)

    class Meta:
        verbose_name = u"Тип протокол"
        verbose_name_plural = u"Типы протоколов"

    def __unicode__(self):
        return self.type_protocol

    def __str__(self):
        return self.type_protocol


# Таблица Протоколы
class Protocol(models.Model):
    agr_id = models.ForeignKey(Agreements, on_delete=models.CASCADE, verbose_name=u"Соглашение")
    title = models.CharField(max_length=250, verbose_name=u"Название протокола")
    number = models.CharField(max_length=20, verbose_name=u"Регистрационный номер")
    reg_date = models.DateField(verbose_name=u"Дата регистрации протокола")
    inv_number = models.CharField(max_length=20, verbose_name=u"Инвентарный номер", blank=True, null=True)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=u"Тип протокола")
    from_mvd = models.TextField(verbose_name=u"Данные от МВД", blank=True, null=True)  # Перечень сведений от МВД
    for_mvd = models.TextField(verbose_name=u"Данные для МВД", blank=True, null=True)  # Перечень сведений для МВД
    note = models.TextField(verbose_name=u"Примечание", blank=True, null=True)
    file = models.FileField(upload_to='protocol/', verbose_name=u"Протокол (PDF-формат)", blank=True, null=True)

    class Meta:
        verbose_name = u"Протокол"
        verbose_name_plural = u"Протоколы"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
