class Train:
    def __init__(self, train_id, trip_duration, starting_station, end_station, route,
                 ticket_price, departure_time, arrival_time, route_timings_v,):

        self.train_id = int(train_id)
        self.trip_duration = trip_duration.strip().split(":")
        self.starting_station = starting_station
        self.end_station = end_station
        self.route = route.split(", ")
        self.ticket_price = ticket_price              # keeping as a string
        self.departure_time = departure_time.split(":")
        self.arrival_time = arrival_time.split(":")
        self.route_timing_v = [[int(n) for n in element.split(":")] for element in route_timings_v.split(", ")]

    def check_route(self, starting_station, ending_station, trip_time):
        if starting_station in self.route and ending_station in self.route:
            starting_station_index = self.route.index(starting_station) # get index of SS
            ending_station_index = self.route.index(ending_station)     # get index of ES
            if starting_station_index < ending_station_index:        # if SS < ES = If ticket_route in route (in-order):
                if trip_time[0] <= self.route_timing_v[starting_station_index][0] and trip_time[1] <\
                        self.route_timing_v[starting_station_index][1]:
                    return self

    def arrives_at(self, station):
        return self.route_timing_v[self.route.index(station)]
        # RETURNS A LIST OF 2 INTS EXAMPLE ; [20,10]

class Ticket:
    def __init__(self, starting_station, end_station, date_and_hour_of_trip, passenger_name,):

        self.starting_station = starting_station
        self.end_station = end_station
        self.date_and_hour_of_trip = date_and_hour_of_trip
        self.passenger_name = passenger_name


