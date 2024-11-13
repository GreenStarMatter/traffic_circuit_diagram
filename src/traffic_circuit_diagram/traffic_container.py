from traffic_circuit_diagram.traffic_light import TrafficLight
from traffic_circuit_diagram.traffic_light import LogicGateTrafficLight
from traffic_circuit_diagram.road import Road

class TrafficContainer:
    def __init__(self):
        self.traffic_lights = {}
        self.roads = {}
        self.connection_map = {}
        self.traffic_lights_coordinates = {}
        self.root_traffic_light = None

    def add_traffic_light(self, incoming_traffic_light_command):
        if len(incoming_traffic_light_command) == 3:
            new_traffic_light = TrafficLight(incoming_traffic_light_command[1], incoming_traffic_light_command[2])
        elif len(incoming_traffic_light_command) == 4:
            new_traffic_light = LogicGateTrafficLight(incoming_traffic_light_command[1], incoming_traffic_light_command[2])
            new_traffic_light.set_gate_type(incoming_traffic_light_command[3])
        self.traffic_lights[new_traffic_light.outcome_name] = new_traffic_light
        if new_traffic_light.outcome_name == "Project Start":
            self.root_traffic_light = new_traffic_light.outcome_name
        return True

    def add_road(self, incoming_road_command):
        new_road = Road(incoming_road_command[1], incoming_road_command[2])
        new_road.set_incoming_traffic_light(incoming_road_command[3])
        new_road.set_outgoing_traffic_light(incoming_road_command[4])
        self.roads[new_road.road_name] = new_road
        return True

    def connect_roads_to_traffic_lights(self):
        for road in self.roads:
            road_object = self.roads[road]
            if road_object.incoming_light not in self.traffic_lights.keys():
                print(road_object.incoming_light+ " not in traffic_lights, added automatically")
                new_traffic_light = TrafficLight(road_object.incoming_light, "Not Started")
                self.traffic_lights[new_traffic_light.outcome_name] = new_traffic_light
            if road_object.outgoing_light not in self.traffic_lights.keys():
                print(road_object.outgoing_light + " not in traffic_lights, added automatically")
                new_traffic_light = TrafficLight(road_object.outgoing_light, "Not Started")
                self.traffic_lights[road_object.outgoing_light] = new_traffic_light
            self.traffic_lights[road_object.incoming_light].outgoing_roads[road_object.road_name] = road_object
            self.traffic_lights[road_object.outgoing_light].incoming_roads[road_object.road_name] = road_object
            self.connection_map[road] = [road_object.incoming_light, road_object.outgoing_light]
        #print(self.connection_map)
        self._calculate_discrete_cartesian_coordinates_of_traffic_lights()
        #print(self.traffic_lights_coordinates)
        return True

    def _calculate_discrete_cartesian_coordinates_of_traffic_lights(self):
        in_process_nodes = [self.root_traffic_light]
        while len(in_process_nodes)> 0:
            current_traffic_light = in_process_nodes.pop(0)
            current_traffic_light_object = self.traffic_lights[current_traffic_light]
            for road in current_traffic_light_object.outgoing_roads:
                outgoing_road_object = self.roads[road]
                outgoing_traffic_light = self.roads[road].outgoing_light
                outgoing_node = self.roads[road]
                #This is wrong, this pulls in a road object, but needs to pull in the string associated with it instead
                if (outgoing_traffic_light not in self.traffic_lights_coordinates) and (outgoing_traffic_light not in in_process_nodes):
                    in_process_nodes.append(outgoing_traffic_light)
            all_incoming_lights_accounted_for = True
            incoming_max_x = -1
            incoming_max_y = -1
            for road in self.traffic_lights[current_traffic_light].incoming_roads:
                if self.roads[road].incoming_light not in self.traffic_lights_coordinates:
                    if self.roads[road].incoming_light not in in_process_nodes:
                        in_process_nodes.insert(0, self.roads[road].incoming_light)
                    all_incoming_lights_accounted_for = False
                    break
                incoming_max_x = max(incoming_max_x, self.traffic_lights_coordinates[self.roads[road].incoming_light][0])
                incoming_max_y = max(incoming_max_y, self.traffic_lights_coordinates[self.roads[road].incoming_light][1])
            if all_incoming_lights_accounted_for:
                self.traffic_lights_coordinates[current_traffic_light] = [incoming_max_x + 1, incoming_max_y + 1]
            else:
                in_process_nodes.append(current_traffic_light)
        self._calculate_y_coordinate_from_overlaps()
        self._handle_for_overlapping_edges()

    def _calculate_y_coordinate_from_overlaps(self):
        x_position_dict = {}
        for traffic_light in self.traffic_lights_coordinates:
            if self.traffic_lights_coordinates[traffic_light][0] not in x_position_dict:
                x_position_dict[self.traffic_lights_coordinates[traffic_light][0]] = []
            x_position_dict[self.traffic_lights_coordinates[traffic_light][0]].append(traffic_light)

        for x_position in x_position_dict:
            height_counter = 0
            for traffic_light in x_position_dict[x_position]:
                self.traffic_lights_coordinates[traffic_light][1] = height_counter
                height_counter += 1

    def _handle_for_overlapping_edges(self):
        road_cartesian_info = {}
        for road in self.roads:
            starting_coordinates = self.traffic_lights_coordinates[self.roads[road].incoming_light]
            ending_coordinates = self.traffic_lights_coordinates[self.roads[road].outgoing_light]
            x_start = starting_coordinates[0]
            x_end = ending_coordinates[0]
            slope = self._calc_slope_from_coordinates(x_start, x_end, starting_coordinates[1], ending_coordinates[1])
            road_cartesian_info[road] = [x_start, x_end, slope]
        
        list_of_roads_to_verify = list(road_cartesian_info.keys())
        searched_index = 1
        max_y = 0
        for road in list_of_roads_to_verify:
            max_y = max(max_y, self.traffic_lights_coordinates[self.roads[road].outgoing_light][1], self.traffic_lights_coordinates[self.roads[road].incoming_light][1])
        for road in list_of_roads_to_verify:
            leftmost_road_interval = [self.traffic_lights_coordinates[self.roads[road].incoming_light][0], self.traffic_lights_coordinates[self.roads[road].outgoing_light][0]]
            for further_road in list_of_roads_to_verify[searched_index:]:
                comparing_road_interval = [self.traffic_lights_coordinates[self.roads[further_road].incoming_light][0], self.traffic_lights_coordinates[self.roads[further_road].outgoing_light][0]]
                intersection_detected = self._calc_coordinates_intersection(leftmost_road_interval, comparing_road_interval)
                if (road_cartesian_info[road][2] == road_cartesian_info[further_road][2]) and intersection_detected:
                    max_y += 1
                    self.traffic_lights_coordinates[self.roads[further_road].outgoing_light][1] = max_y
                    further_road_starting_coordinates = self.traffic_lights_coordinates[self.roads[further_road].incoming_light]
                    further_road_ending_coordinates = self.traffic_lights_coordinates[self.roads[further_road].outgoing_light]
                    new_slope = self._calc_slope_from_coordinates(further_road_starting_coordinates[0], further_road_ending_coordinates[0], further_road_starting_coordinates[1], max_y)
                    road_cartesian_info[further_road][2] = new_slope
            searched_index += 1

    def _calc_slope_from_coordinates(self, x_start, x_end, y_start, y_end):
        return (y_end - y_start)/(x_end - x_start)

    def _calc_coordinates_intersection(self, interval_1, interval_2):
        return ((interval_1[0] <= interval_2[1]) and (interval_2[0] <= interval_1[1]))
        
        

