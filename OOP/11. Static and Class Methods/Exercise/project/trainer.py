class Trainer:
    ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.ID
        Trainer.ID += 1

    @staticmethod
    def get_next_id():
        return Trainer.ID

    def __str__(self):
        return 'Trainer <{}> {}'.format(self.id, self.name)

