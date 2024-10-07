class Flight:
    def __init__(self, flight_id, aircraft_id):
        self.__flight_id = flight_id
        self.__aircraft_id = aircraft_id
        self.status = "Scheduled"

    @property
    def flight_id(self):
        return self.__flight_id

    @property
    def aircraft_id(self):
        return self.__aircraft_id

    def display_info(self):
        print(f"Flight {self.flight_id} on aircraft {self.aircraft_id} is {self.status}.")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Flight {self.flight_id} status updated to {self.status}.")

    @staticmethod
    def is_active(status):
        return status.lower() in ['scheduled', 'in air']

class InternationalFlight(Flight):
    def __init__(self, flight_id, aircraft_id, destination_country):
        super().__init__(flight_id, aircraft_id)
        self.destination_country = destination_country

    def display_info(self):
        super().display_info()
        print(f"Destination country: {self.destination_country}")

class ShortDistanceFlight:
    def __init__(self, max_flight_time):
        self.max_flight_time = max_flight_time

    def display_flight_time(self):
        print(f"Maximum flight time: {self.max_flight_time} hours.")

class DomesticFlight(Flight, ShortDistanceFlight):
    def __init__(self, flight_id, aircraft_id, max_flight_time, departure_city):
        Flight.__init__(self, flight_id, aircraft_id)
        ShortDistanceFlight.__init__(self, max_flight_time)
        self.departure_city = departure_city

    def display_info(self):
        super().display_info()
        print(f"Departure city: {self.departure_city}")
        self.display_flight_time()

flight1 = InternationalFlight("AI202", "Boeing 747", "Germany")
flight1.display_info()
flight1.update_status("In Air")

flight2 = DomesticFlight("UA345", "Airbus A320", 2.5, "Kyiv")
flight2.display_info()
