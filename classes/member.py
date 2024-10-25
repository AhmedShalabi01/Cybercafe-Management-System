import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)

from classes.user import user
import queries as QUERIES


class member(user):
    def __init__(self, **kwargs):
        self.__credit = kwargs.get("credit")
        super().__init__(**kwargs)

    def update_credit(self, value):
        self.__credit += value
        if self.__credit <= 0:
            print(
                "{} credit is {}, customer should recharge his credit".format(
                    self._user__user_name, self.__credit
                )
            )
        QUERIES.update_attribute(
            "databases/users.json", self._user__user_name, "credit", self.__credit
        )

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, credit):
        self.__credit = credit
        QUERIES.update_attribute(
            "databases/users.json",
            self._user__user_name,
            "credit",
            self.__credit,
        )
