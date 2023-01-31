from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """
        Attributes:
        -----------
        param event_title: Describes name of the event
        type event_title: str max length=20
        param start_date: Describes the date when the event will be started.
        type start_date: int (timestamp)
        param end_date: Describes the date when the event will be ended.
        type end_date: int (timestamp)
        param reservation_code: Describes exclusive for the person reservation_code of the event
        type reservation_code: str/int max length=20
    """

    event_title = models.CharField(blank=True, max_length=20)
    start_date = models.DateTimeField(editable=True)
    end_date = models.DateTimeField(editable=True)
    reservation_code = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            pass

    @staticmethod
    def get_by_reservation_code(reservation_code):
        try:
            user = User.objects.get(reservation_code=reservation_code)
            return user
        except User.DoesNotExist:
            pass

    @staticmethod
    def create(event_title=None, start_date=None, end_date=None, reservation_code=None):
        data = {}
        data['event_title'] = event_title if event_title else ''
        data['start_date'] = start_date if start_date else ''
        data['end_date'] = end_date if end_date else ''
        data['reservation_code'] = reservation_code
        user = User(**data)
        user.save()
        return user

    def update(self,
               event_title=None,
               start_date=None,
               end_date=None,
               reservation_code=None):

        if event_title:
            self.event_title = event_title
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date
        if reservation_code:
            self.reservation_code = reservation_code
        self.save()

    @staticmethod
    def get_all():
        all = User.objects.all()
        return all