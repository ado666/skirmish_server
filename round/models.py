from django.db import models

from theme.models import  Theme
from question.models import Question
from game.models import Game
from player.models import Player

# Create your models here.


class Round(models.Model):
    id          = models.AutoField(primary_key=True)

    step        = models.IntegerField(null=True, blank=True)
    turn        = models.ForeignKey(Player)
    owner       = models.ForeignKey(Player, related_name='round_owner')

    theme       = models.ForeignKey(Theme, null=True, blank=True)
    game        = models.ForeignKey(Game, related_name='rounds', null=True, blank=True)
    questions   = models.ManyToManyField(Question, related_name='round')

    current     = models.IntegerField(null=False, default=0)

    def json(self):

        questions = []
        themes = []

        for theme in Theme.objects.all():
            themes.append(theme.json())

        theme = None
        if self.theme:
            theme = self.theme.json()

        for q in self.questions.all():

            questions.append({
                'question': q.question,
                'answer1': q.answer1,
                'answer2': q.answer2,
                'answer3': q.answer3,
                'answer4': q.answer4,
                'id': str(q.id),
            })

        return {
            'id': str(self.id),
            'step': str(self.step),
            'questions': questions,
            'owner': self.owner.json(),
            'theme': theme,
            'step': self.step,
            'themes': themes,
        }