from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from . import serializers
from .models import Event, Registration
from .serializers import RegistrationSerializer

class EventRegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'regform/event_registration.html', {'event': event})

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'regform/event_registration.html', {'event': event})

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        print(request.data)  # Отладочное сообщение
        serializer = self.get_serializer(data=request.data)
        serializer.context['event'] = event  # Передаем событие в контекст сериализатора

        if serializer.is_valid():
            registration = serializer.save()  # Используем метод save для создания регистрации
            return Response({'message': 'Регистрация завершена!'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)