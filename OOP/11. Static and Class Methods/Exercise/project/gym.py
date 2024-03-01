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
        if equipment not in self.customers:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self,subscription_id):
        subscription_ids = [subscription.id for subscription in self.subscriptions]
        subscription = self.subscriptions[subscription_ids.index(subscription_id)]
        customer = next((cust for cust in self.customers if cust.customer_id == subscription.customer_id), None)
        trainer = next((trn for trn in self.trainers if trn.id == subscription_id), None)
        equipment = next((equip for equip in self.equipment if equip.id == subscription.exercise_id), None)
        plan = self.plans[0]

        string = ''
        string += subscription.__repr__() + '\n'
        string += customer.__repr__() + '\n'
        string += trainer.__repr__() + '\n'
        string += equipment.__repr__() + '\n'
        string += plan.__repr__()
        return string