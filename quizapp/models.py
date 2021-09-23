from django.db import models

# Create your models here.
from django.utils import timezone


class Questions(models.Model):
    """Модель для вопросов"""
    user = models.CharField("Автор", max_length=30)
    question = models.CharField("Вопрос", max_length=250, blank=False)
    linkOfPicture = models.ImageField("Картинка к вопросу", upload_to='question_foto', blank=True, null=True)
    rightAnswer = models.CharField("Ответ", max_length=70, blank=False)
    wrongAnswerOne = models.CharField("Первый неправильный ответ", max_length=50, blank=False)
    wrongAnswerTwo = models.CharField("Первый неправильный ответ", max_length=50, blank=False)
    wrongAnswerThree = models.CharField("Первый неправильный ответ", max_length=50, blank=False)
    commentForJudge = models.CharField("Комментарий к вопросу", max_length=400, blank=False)
    aboutQuestion = models.CharField("Описание вопроса", max_length=2000, blank=False)
    themeOfQuestion = models.CharField("Тема", max_length=150, blank=True, null=True)
    link = models.CharField("Источник информации", max_length=50, blank=False)
    sectionOfQuestion = models.CharField("Раздел", max_length=55, blank=False)
    complexityOfQuestion = models.IntegerField("Сложность по десятибальной шкале", blank=False, null=True, default=0)
    approve = models.IntegerField("Статус одобрения", blank=False, default=0)
    date_ques_sub = models.DateField("Дата подачи вопроса", blank=False)
    base_date = models.DateField("Дата добавления в базу", blank=False, null=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.date_ques_sub = timezone.now()
        return super(Questions, self).save(*args, **kwargs)


class QuestionsReviewer(models.Model):
    question = models.OneToOneField(Questions, on_delete=models.CASCADE, primary_key=True)
    reviewer = models.CharField("Рецензент", max_length=30, blank=True, null=True)
    reviewer_date = models.DateField("Дата рецензии", blank=True)


# class QuestionsThemes(models.Model):
#     """Модель тем для вопросов"""
#     # question = models.ForeignKey(Questions, on_delete=models.CASCADE, primary_key=True)
#     question = models.ManyToManyField(Questions)



class QuestionsThemesCategory(models.Model):
    """Модель категорий для тем"""
    # themeOfQuestion = models.ForeignKey(QuestionsThemes, on_delete=models.CASCADE, blank=True, null=True)
    questionCategory = models.CharField("Категория", max_length=120)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=True, null=True)


