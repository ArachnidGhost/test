from rest_framework import serializers
from django.core.mail import send_mail
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True)
    user_email = serializers.EmailField(required=True)  # Добавлено поле user_email
    available_time = serializers.DateTimeField(required=True)

    class Meta:
        model = Registration
        fields = ['user_name', 'user_email', 'available_time']

    def create(self, validated_data):
        event = self.context['event']
        validated_data['event'] = event

        registration = super().create(validated_data)

        user_email = registration.user_email
        user_name = registration.user_name
        available_time = registration.available_time
        event_title = registration.event.name

        try:
            send_mail(
                'Регистрация на мероприятие',
                f'Вы успешно зарегистрировались на мероприятие: {event_title}\n'
                f'Ваше имя: {user_name}\n'
                f'Ваш email: {user_email}\n'
                f'Выбранное время: {available_time}',
                '8vtaradina@gmail.com',
                [user_email],
                fail_silently=False,
            )

            send_mail(
                'Новая регистрация на мероприятие',
                f'Пользователь с email {user_email} зарегистрировался на мероприятие: {event_title}\n'
                f'Имя: {user_name}\n'
                f'Выбранное время: {available_time}',
                '8vtaradina@gmail.com',
                ['8vtaradina@gmail.com'],
                fail_silently=False,
            )

            return registration
        except Exception as e:
            raise serializers.ValidationError(f'Ошибка отправки почты: {str(e)}')