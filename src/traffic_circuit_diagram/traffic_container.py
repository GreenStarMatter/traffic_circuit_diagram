from traffic_circuit_diagram.traffic_light import TrafficLight
from traffic_circuit_diagram.traffic_light import LogicGateTrafficLight
from traffic_circuit_diagram.road import Road

class TrafficContainer:
    def __init__(self):
        self.traffic_lights = {}
        self.roads = {}
        self.connection_map = {}

    def add_traffic_light(self, incoming_traffic_light_command):
        if len(incoming_traffic_light_command) == 3:
            new_traffic_light = TrafficLight(incoming_traffic_light_command[1], incoming_traffic_light_command[2])
        elif len(incoming_traffic_light_command) == 4:
            new_traffic_light = LogicGateTrafficLight(incoming_traffic_light_command[1], incoming_traffic_light_command[2])
            new_traffic_light.set_gate_type(incoming_traffic_light_command[3])
        self.traffic_lights[new_traffic_light.outcome_name] = new_traffic_light
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
            self.connection_map[road] = [road_object.incoming_light, road_object.outgoing_light]
        return True