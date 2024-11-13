import networkx as nx
import matplotlib.pyplot as plt
from traffic_circuit_diagram.traffic_container import TrafficContainer
from traffic_circuit_diagram.networkx_engine import NetworkXTrafficEngine

class EnvironmentSetter:
    def __init__(self, save_file_location:str, graphics_engine:str = "networkx"):
        self.save_file_location = save_file_location
        self.command_list = []
        self.traffic_circuit_diagram_container = TrafficContainer()
        self.graphics_engine = graphics_engine

    def set_save_file_location(self, incoming_save_file_location:str) -> bool:
        self.save_file_location = incoming_save_file_location
        return True

    def read_save_file(self) -> bool:
        with open(self.save_file_location, 'r') as save_file:
            self.command_list = [line.strip() for line in save_file.readlines() ]
        return True

    def set_up_graph_using_engine(self):
        if self.graphics_engine == "networkx":
            self.graphics_engine = NetworkXTrafficEngine("Custom Algorithm 1")
        else:
            print("Engine Unrecognized")

    def upload_stored_graph_to_engine(self):
        #
        self.graphics_engine.upload_traffic_graph_to_engine(self.traffic_circuit_diagram_container)

    def show_network_graph(self):
        self.graphics_engine.show_network_graph()

    def execute_command_list(self) -> bool:
        for command in self.command_list:
            split_commands = command.split("|")
            if split_commands[0] == "Traffic Light":
                self._create_traffic_light(split_commands)
            elif split_commands[0] == "Traffic Light Gate":
                self._create_traffic_light(split_commands)
            elif split_commands[0] == "Road":
                self._create_road(split_commands)
            else:
                print("Command not recognized: " + split_commands[0])
        self.traffic_circuit_diagram_container.connect_roads_to_traffic_lights()
        return True

    def _create_traffic_light(self, incoming_traffic_command: list) -> bool:
        self.traffic_circuit_diagram_container.add_traffic_light(incoming_traffic_command)
        return True

    def _create_road(self, incoming_road_command: list) -> bool:
        self.traffic_circuit_diagram_container.add_road(incoming_road_command)
        return True





