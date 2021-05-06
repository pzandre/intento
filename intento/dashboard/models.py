from django.db import models

# Create your models here.
class Question(models.Model):
    
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
    
    base_text = models.TextField()
    bibliographic_reference = models.CharField(max_length=1000)
    question_statement = models.TextField()
    answer_A = models.TextField()
    answer_B = models.TextField()
    answer_C = models.TextField()
    answer_D = models.TextField()
    answer_E = models.TextField()
    

class Answer(models.Model):
    
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    EASY = 'EZ'
    INTERMEDIATE = 'IM'
    HARD = 'HD'
    
    DIFFICULTY_CHOICES = [(EASY, 'Fácil'), (INTERMEDIATE, 'Intermediário'), (HARD, 'Difícil')]
    
    difficulty = models.CharField(max_length=2, choices=DIFFICULTY_CHOICES)

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

    bloom_taxonomy = models.CharField(max_length=2, choices=BLOOM_CHOICES)
    
    HAS_TABLE = 'HT'
    HAS_GRAPHICS = 'HG'
    HAS_IMAGES = 'HI'
    TEXT_ONLY = 'TO'

    INFO_CHOICES = [(HAS_TABLE, 'Contém Tabela'), (HAS_GRAPHICS, 'Contém Gráfico'),
                    (HAS_IMAGES, 'Contém Imagem'), (TEXT_ONLY, 'Somente Texto')]

    question_information = models.CharField(max_length=2, choices=INFO_CHOICES)

    ANSWER_A = 'A'
    ANSWER_B = 'B'
    ANSWER_C = 'C'
    ANSWER_D = 'D'
    ANSWER_E = 'E'

    ANSWER_CHOICES = [(ANSWER_A, 'Alternativa A'), (ANSWER_B, 'Alternativa B'),
                      (ANSWER_C, 'Alternativa C'), (ANSWER_D, 'Alternativa D'), 
                      (ANSWER_E, 'Alternativa E')]

    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

    a_justification = models.TextField()
    b_justification = models.TextField()
    c_justification = models.TextField()
    d_justification = models.TextField()
    e_justification = models.TextField()