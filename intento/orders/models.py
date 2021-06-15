from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse, reverse_lazy
from django_quill.fields import QuillField
from taggit.managers import TaggableManager
from institutes.models import Institute, Discipline, DisciplineMacroContent, DisciplineMicroContent
from conf.settings import AUTH_USER_MODEL as CustomUser


class QuestionOrder(models.Model):
    institute = models.ForeignKey(Institute, verbose_name="institute", on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name="discipline", on_delete=models.CASCADE)
    macro_content = models.ForeignKey(DisciplineMacroContent, verbose_name='macro_content', on_delete=models.CASCADE)
    micro_content = models.ForeignKey(DisciplineMicroContent, verbose_name='micro_content', on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, verbose_name="Teacher", on_delete=models.CASCADE)
    question_quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    order_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now=False)

    @staticmethod
    def get_absolute_url(self, **kwargs):
        return reverse('order-detail')

    @property
    def question_range(self):
        return range(self.question_quantity)

    @property
    def question_details(self, *args, **kwargs):
        order = dir(Question.objects.filter(question_order=self.pk))
        return order

    def __str__(self):
        order_info = f'{self.institute} | {self.discipline} | {self.macro_content} | {self.micro_content}'
        return f'Order {self.pk} - {order_info} | Professor {self.teacher}'


class Question(models.Model):
    question_order = models.ForeignKey(QuestionOrder, verbose_name="questionorder",
                                       related_name="questionorder", on_delete=models.CASCADE)

    id_by_order = models.IntegerField()

    INCOMPLETE_AFFIRMATION = 'IA'
    ASSERTION_REASON = 'AR'
    COLUMN_ASSOCIATION = 'CA'
    GAP = 'GP'
    COMPLEX_MULTICHOICE = 'CM'
    SIMPLE_MULTICHOICE = 'SM'
    SERIATION = 'SR'
    TRUTH_FALSE = 'TF'

    QUESTION_TYPE_CHOICES = [
        (INCOMPLETE_AFFIRMATION, 'Afirmação Incompleta'),
        (ASSERTION_REASON, 'Asserção-Razão'),
        (COLUMN_ASSOCIATION, 'Associação de Colunas'),
        (GAP, 'Lacuna'),
        (COMPLEX_MULTICHOICE, 'Múltipla Escolha Complexa'),
        (SIMPLE_MULTICHOICE, 'Múltipla Escolha Simples'),
        (SERIATION, 'Seriação'),
        (TRUTH_FALSE, 'Verdadeiro ou Falso')]

    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES)

    base_text_1 = QuillField()
    bibliographic_reference_1 = models.CharField(max_length=1000)
    base_text_2 = QuillField(blank=True, null=True)
    bibliographic_reference_2 = models.CharField(max_length=1000, blank=True, null=True)
    base_text_3 = QuillField(blank=True, null=True)
    bibliographic_reference_3 = models.CharField(max_length=1000, blank=True, null=True)
    question_statement = QuillField()
    answer_A = QuillField()
    answer_B = QuillField()
    answer_C = QuillField()
    answer_D = QuillField()
    answer_E = QuillField()

    EASY = 'EZ'
    INTERMEDIATE = 'IM'
    HARD = 'HD'

    DIFFICULTY_CHOICES = [(EASY, 'Fácil'), (INTERMEDIATE, 'Intermediário'), (HARD, 'Difícil')]

    difficulty = models.CharField(max_length=2, choices=DIFFICULTY_CHOICES, null=True)

    KNOWLEDGE = 'KW'
    COMPREENSION = 'CP'
    APPLICATION = 'AP'
    ANALYSIS = 'AN'
    SYNTHESIS = 'SY'
    AVALIATION = 'AV'

    BLOOM_CHOICES = [
        (KNOWLEDGE, 'Conhecimento'),
        (COMPREENSION, 'Compreensão'),
        (APPLICATION, 'Aplicação'),
        (ANALYSIS, 'Análise'),
        (SYNTHESIS, 'Síntese'),
        (AVALIATION, 'Avaliação')]

    bloom_taxonomy = models.CharField(max_length=2, choices=BLOOM_CHOICES, null=True)

    HAS_TABLE = 'HT'
    HAS_GRAPHICS = 'HG'
    HAS_IMAGES = 'HI'
    TEXT_ONLY = 'TO'

    INFO_CHOICES = [(HAS_TABLE, 'Contém Tabela'), (HAS_GRAPHICS, 'Contém Gráfico'),
                    (HAS_IMAGES, 'Contém Imagem'), (TEXT_ONLY, 'Somente Texto')]

    question_information = models.CharField(max_length=2, choices=INFO_CHOICES, null=True)

    ANSWER_A = 'A'
    ANSWER_B = 'B'
    ANSWER_C = 'C'
    ANSWER_D = 'D'
    ANSWER_E = 'E'

    ANSWER_CHOICES = [(ANSWER_A, 'Alternativa A'), (ANSWER_B, 'Alternativa B'),
                      (ANSWER_C, 'Alternativa C'), (ANSWER_D, 'Alternativa D'),
                      (ANSWER_E, 'Alternativa E')]

    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES, null=True)

    a_justification = QuillField(blank=True)
    b_justification = QuillField(blank=True)
    c_justification = QuillField(blank=True)
    d_justification = QuillField(blank=True)
    e_justification = QuillField(blank=True)
    general_justification = models.TextField(null=True, blank=True)

    revision_approval = models.BooleanField(default=False)

    tag = TaggableManager() # TODO: Implement Taggit autosuggestion

    def get_absolute_url(self):
        return reverse_lazy('question-detail', context={
            'order': self.question_order, 'id_by_order': self.id_by_order
        })

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Question._meta.fields]

    def __str__(self):
        return f'Order {self.question_order.id} - Question {self.id_by_order}'
