class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.id
        Trainer.id += 1

    @staticmethod
    def get_next_id():
        return Trainer.id

    def __repr__(self):
        return 'Trainer <{}> {}'.format(self.id, self.name)


