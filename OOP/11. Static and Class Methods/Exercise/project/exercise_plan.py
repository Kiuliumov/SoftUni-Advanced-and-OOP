class ExercisePlan:
    ID = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.ID
        ExercisePlan.ID += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id() -> int:
        return ExercisePlan.ID

    def __str__(self) -> str:
        return 'Plan <{}> with duration {} minutes'.format(self.id, self.duration)
