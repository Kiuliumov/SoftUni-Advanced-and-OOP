class Subscription:
    ID = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int) -> None:
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.ID
        Subscription.ID += 1

    @staticmethod
    def get_next_id() -> int:
        return Subscription.ID

    def __repr__(self) -> str:
        return 'Subscription <{}> on {}'.format(self.id, self.date)
