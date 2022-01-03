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
    #id = models.TextField(default=None)
    localita = models.CharField(max_length=100,default=None)
    indirizzo = models.TextField(default=None)
    provincia = models.TextField(default=None)
    posizione_GPS = models.TextField(default=None)
    link_scheda = models.TextField(default=None)
    link_foto = models.TextField(default=None)
    link_earth = models.TextField(default=None)
    serial_n = models.TextField(default=None)
    status = models.TextField(default=None)
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.localita, self.indirizzo, self.provincia, self.posizione_GPS, self.link_scheda, self.link_foto, self.link_earth, self.serial_n, self.status)


class Misure_PD(models.Model):
    #id_sito = models.ForeignKey(Sito, on_delete=models.CASCADE)
    data_acquisizione = models.TextField(default=None)
    lunghezza_stendimento = models.TextField(default=None)
    note = models.TextField(default=None)
    caratteristiche_sito = models.TextField(default=None)
    vs30 = models.TextField(default=None)
    vr40 = models.TextField(default=None)
    spettro = models.TextField(default=None)
    comment = models.TextField(default=None)


class Contatti(models.Model):
    #id_sito = models.ForeignKey(Sito, on_delete=models.CASCADE)
    nome = models.TextField(default=None)
    cognome = models.TextField(default=None)
    telefono = models.TextField(default=None)
    email = models.TextField(default=None)
    ruolo = models.TextField(default=None)
    priorita  = models.TextField(default=None)

