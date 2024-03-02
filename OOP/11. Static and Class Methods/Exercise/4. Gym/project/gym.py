class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment.id not in [e.id for e in self.equipment]:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self._get_subscription_by_id(subscription_id)
        customer = self._get_customer_by_id(subscription_id)
        trainer = self._get_trainer_by_id(subscription_id)
        equipment = self._get_equipment_by_id(subscription_id)
        plan = self._get_plan_by_id(subscription_id)

        string = ''
        string += subscription.__repr__() + '\n'
        string += customer.__repr__() + '\n'
        string += trainer.__repr__() + '\n'
        string += equipment.__repr__() + '\n'
        string += plan.__repr__() + '\n'
        return string

    # helper methods
    def _get_subscription_by_id(self, subscription_id):
        subscription = [subscription for subscription in self.subscriptions if subscription.id == subscription_id]
        return subscription[0] if subscription else None

    def _get_trainer_by_id(self, trainer_id):
        trainer = [trainer for trainer in self.trainers if trainer.id == trainer_id]
        return trainer[0] if trainer else None

    def _get_customer_by_id(self, customer_id):
        customer = [customer for customer in self.customers if customer.id == customer_id]
        return customer[0] if customer else None

    def _get_equipment_by_id(self, equipment_id):
        equipment = [equipment for equipment in self.equipment if equipment.id == equipment_id]
        return equipment[0] if equipment else None

    def _get_plan_by_id(self, plan_id):
        plan = [plan for plan in self.plans if plan.id == plan_id]
        return plan[0] if plan else None
