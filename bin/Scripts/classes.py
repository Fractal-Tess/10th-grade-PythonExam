class Train:
    def __init__(self, route):
        self.route = route.split(", ")
       # self.route_timing_v = [[int(n) for n in element.split(":")] for element in route_timings_v.split(", ")]


    def check_route(self, starting_station, ending_station, trip_time):
        if starting_station in self.route and ending_station in self.route:
            starting_station_index = self.route.index(starting_station)  # get integer value of starting station
            ending_station_index = self.route.index(ending_station)  # get integer value of end station
            if starting_station_index < ending_station_index: # if starting station is before ending station
                if trip_time[0] <= self.route_timing_v[starting_station_index][0] and trip_time[1] < \
                        self.route_timing_v[starting_station_index][1]:
                    return self
        return None

    def arrives_at(self, station):
        return self.route_timing_v[self.route.index(station)]
        # RETURNS A LIST OF 2 INTS EXAMPLE ; [20,10]


class Stations:
    def __init__(self, station_name, x, y, node, node_connection_list):
        self.station_name = station_name
        self.x = x
        self.y = y
        self.node = node
        self.node_connection_list = node_connection_list


class Ticket:
    def __init__(self, starting_station, end_station, date_and_hour_of_trip, passenger_name, ):
        self.starting_station = starting_station
        self.end_station = end_station
        self.date_and_hour_of_trip = date_and_hour_of_trip
        self.passenger_name = passenger_name
