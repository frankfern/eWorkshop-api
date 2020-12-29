from eworkshop.utils.models import BasicInfoModel


class Customer(BasicInfoModel):
    """
    Customer Model
    """

    def __str__(self):
        return self.first_name
