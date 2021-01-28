from django.db.models import Q
from django.shortcuts import redirect, reverse
from django.views.generic import DeleteView
from users import models as user_models
from . import models


def go_conversation(request, a_pk, b_pk):
    user_one = user_models.User.objects.get_or_none(pk=a_pk)
    user_two = user_models.User.objects.get_or_none(pk=b_pk)

    if user_one is not None and user_two is not None:
        # conversation = models.Conversation.objects.filter(participants=user_one).filter(participants=user_two)
        try:
            conversation = models.Conversation.objects.get_or_none(
                Q(participants=user_one) & Q(participants=user_two)
            )
        except models.Conversation.DoesNotExist:
            conversation = models.Conversation.objects.create()
            conversation.participants.add(user_one, user_two)
        return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))


class ConversationDetailView(DeleteView):
    model = models.Conversation
