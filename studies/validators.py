import re

from rest_framework import serializers


class LessonCustomValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = value.get('link_to_video')
        if link and not re.match(r'https?:\/\/(?:www\.)?youtube\.com\/.*', link):
            raise serializers.ValidationError("Ссылка должна быть на YouTube")
