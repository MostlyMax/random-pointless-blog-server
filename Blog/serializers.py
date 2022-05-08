from rest_framework import routers, serializers, viewsets
from .models import Entry, Feature


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'title', 'body', 'submitted_date']


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'entry', 'title', 'body', 'featured_date']
