from typing import Type
from TAScheduler.models import User as UserModel, PublicInfo, PrivateInfo
from typing import Dict


def create_account(data: Dict[str, any]):
    if __has_required_fields(data):
        new_user = UserModel.objects.create()
        new_user.email = data.get('email')
        new_user.password = data.get('password')
        new_user.account_type = data.get('account_type')

        public_info = PublicInfo.objects.create()
        public_info.user_id = new_user.pk
        public_info.first_name = data.get('first_name')
        public_info.last_name = data.get('last_name')

        private_info = PrivateInfo.objects.create()
        private_info.user_id = new_user.pk
        return new_user
    else:
        return None


def __has_required_fields(self, data: Dict[str, str]) -> bool:
    required_fields = {"email", "password", "account_type", "first_name", "last_name"}
    return required_fields.issubset(data.keys())


def valid_login(email_attempt: str, password_attempt: str):
    user = __get_account(email_attempt)
    if user is not None and user.password == password_attempt:
        return True
    else:
        return False


def __get_account(email_attempt):
    try:
        user = UserModel.objects.get(email=email_attempt)
        return user
    except UserModel.DoesNotExist:
        return None


class Account:
    def __int__(self, user_model: Type[UserModel]):
        self.user_model = user_model
        self.public_info_model = PublicInfo.objects.get(user_id=user_model.pk)
        self.private_info_model = PrivateInfo.objects.get(user_id=user_model.pk)

    def get_email(self):
        return self.user_model.email

    def get_office_hours(self):
        return self.public_info_model.office_hours

    def set_office_hours(self, new_office_hours):
        self.public_info_model.office_hours = new_office_hours
        self.public_info_model.save()

    def get_first_name(self):
        return self.public_info_model.first_name

    def set_first_name(self, new_first_name):
        self.public_info_model.first_name = new_first_name
        self.public_info_model.save()

    def get_last_name(self):
        return self.public_info_model.last_name

    def set_last_name(self, new_last_name):
        self.public_info_model.last_name = new_last_name
        self.public_info_model.save()

    def get_address(self):
        return self.private_info_model.address

    def set_address(self, new_address):
        self.private_info_model.address = new_address
        self.private_info_model.save()

    def get_phone_number(self):
        return self.private_info_model.phone_number

    def set_phone_number(self, new_phone_number):
        self.private_info_model.phone_number = new_phone_number
        self.private_info_model.save()