class EntertainmentDevice:
    def connect_to_device(self, cable):
        cable_types: dict = {}

        if cable not in cable_types:
            raise Exception('Cable type not supported')

        cable = cable_types.get(cable)
        ...


    def connect_device_to_power_outlet(self, device): pass


class Television(EntertainmentDevice):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device('hdmi')

    def connect_to_game_console(self, game_console):
        self.connect_to_device('hdmi')

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
