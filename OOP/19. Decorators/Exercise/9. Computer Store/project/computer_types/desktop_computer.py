from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}
    MAX_RAM = 128

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):

        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(
                '{} is not compatible with desktop computer {} {}!'.format(processor, self.manufacturer, self.model))

        if ram not in [2 ** x for x in range(8)] or ram > self.MAX_RAM:
            raise ValueError(
                '{}GB RAM is not compatible with desktop computer {} {}!'.format(ram, self.manufacturer, self.model))

        ram_price = [2 ** x for x in range(8)].index(ram) * 100
        processor_price = self.AVAILABLE_PROCESSORS[processor]
        self.processor = processor
        self.ram = ram
        self.price = ram_price + processor_price

        return 'Created {} {} with {} and {}GB RAM for {}$.'.format(self.manufacturer, self.model, self.processor,
                                                                    self.ram, self.price)
