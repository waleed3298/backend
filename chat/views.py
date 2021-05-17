from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import ChatMessage, Chat
from .serializers import ChatMessageSerializer, ChatSerializer
from .permissions import HasChatPermissions
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.authentication import TokenAuthentication


### Chat Views
class ChatMessageListView(ListAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    def get_queryset(self):
        return ChatMessage.objects.filter(chat__uuid=self.kwargs['chat_uuid']).order_by('-date_sent')


class ChatListCreateView(ListCreateAPIView):
    serializer_class = ChatSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Chat.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))


class ChatDestroyView(DestroyAPIView):
    permission_classes = [HasChatPermissions]
    serializer_class = ChatSerializer
    authentication_classes = [TokenAuthentication]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'chat_uuid'

    def get_queryset(self):
        return Chat.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
