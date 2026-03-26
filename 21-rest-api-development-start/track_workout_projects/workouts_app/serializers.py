# this will contain all serialization logic.
# think of the amazon box analogy.
from rest_framework import serializers

# I'm going to need the model of exercise
# to validate the types.
from .models import Exercise


class ExerciseSerializer(serializers.Serializer):
    # a mapping to the model fields explicitly

    # on the id it is readonly because the database/ORM
    # takes care of it for us.
    id = serializers.IntegerField(read_only=True)

    # let's add the fields that we created
    name = serializers.CharField(max_length=100)
    exercise_type = serializers.ChoiceField(
        choices=Exercise.EXERCISE_TYPES,
    )
