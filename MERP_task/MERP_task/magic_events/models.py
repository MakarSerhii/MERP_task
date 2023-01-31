from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Events(AbstractBaseUser):
    """
        Attributes:
        -----------
        param event_title: Describes name of the event
        type event_title: str max length=20
        param start_date: Describes the date when the event will be started.
        type start_date: int (timestamp)
        param end_date: Describes the date when the event will be ended.
        type end_date: int (timestamp)
    """

    event_title = models.CharField(blank=True, max_length=20)
    start_date = models.DateTimeField(editable=True)
    end_date = models.DateTimeField(editable=True)

    def __str__(self):
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(event_id):
        try:
            event = Events.objects.get(id=event_id)
            return event
        except Events.DoesNotExist:
            pass

    @staticmethod
    def get_by_event_title(event_title):
        try:
            event = Events.objects.get(event_title=event_title)
            return event
        except Events.DoesNotExist:
            pass

    @staticmethod
    def create(event_title=None, start_date=None, end_date=None):
        data = {}
        data['event_title'] = event_title if event_title else ''
        data['start_date'] = start_date if start_date else ''
        data['end_date'] = end_date if end_date else ''
        event = Events(**data)
        event.save()
        return event

    def update(self,
               event_title=None,
               start_date=None,
               end_date=None):

        if event_title:
            self.event_title = event_title
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date
        self.save()
    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all events
        """
        all_events = Events.objects.all()
        return all_events

