from django.db import models
# from round.models import Round
from player.models import Player

from django.core import serializers

# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)

    # step    = models.IntegerField()
    # turn    = models.IntegerField()
    # total   = models.IntegerField()
    status  = models.IntegerField()

    players = models.ManyToManyField(Player, related_name='game')
    # rounds  = models.ForeignKey(Round, null=True, blank=True, default = None)
    # questions = models.ManyToManyField(Question, related_name='game')
    # game_round = models.ForeignKey(Round)

    def json(self):

        # questions = []
        #
        # for q in self.questions.all():
        #
        #     questions.append({
        #         'question': q.question,
        #         'answer1': q.answer1,
        #         'answer2': q.answer2,
        #         'answer3': q.answer3,
        #         'answer4': q.answer4,
        #         'id': str(q.id),
        #     })

        players = []
        for player in self.players.all():
            players.append(player.json())

        rounds = []
        current_round = None
        for r in self.rounds.all():
            rounds.append(r.json())
            if r.current == 1:
                current_round = r.json()

        return {
            'id': str(self.id),
            'status': str(self.status),
            'players': players,
            'rounds': rounds,
            'current_round': current_round
            # 'step': str(self.step),
            # 'turn': str(self.turn),
            # 'questions': questions,
        }

# class IngameResults(models.Model):
#     id = models.AutoField(primary_key=True)
#
#     question_id = models.IntegerField()
#     answer_id = models.IntegerField()
#     player_id = models.IntegerField()
#
#     game = models.ForeignKey(Game)






