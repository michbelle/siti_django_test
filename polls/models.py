from django.db import models

# Create your models here.
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

class Sito(models.Model):
    ID = models.TextField
    Localita = models.TextField
    Indirizzo = models.TextField
    Provincia = models.TextField
    Posizione_GPS = models.TextField
    Link_scheda = models.TextField
    Link_foto = models.TextField
    Link_earth = models.TextField
    Serial_n = models.TextField
    Status = models.TextField

class Misure_PD(models.Model):
    ID_sito = models.ForeignKey(Sito, on_delete=models.CASCADE)
    Data_acquisizione = models.TextField
    Lunghezza_stendimento = models.TextField
    Note = models.TextField
    caratteristiche_sito = models.TextField
    vs30 = models.TextField
    vr40 = models.TextField
    spettro = models.TextField
    comment = models.TextField


class Contatti(models.Model):
    ID_sito = models.ForeignKey(Sito, on_delete=models.CASCADE)
    Nome = models.TextField
    Cognome = models.TextField
    Telefono = models.TextField
    Email = models.TextField
    Ruolo = models.TextField
    Priorita  = models.TextField

