import networkx as nx
import matplotlib.pyplot as plt

from traffic_circuit_diagram.traffic_container import TrafficContainer
from traffic_circuit_diagram.traffic_container import TrafficLight, LogicGateTrafficLight
class NetworkXTrafficEngine:
    def __init__(self, graph_position_algorithm = "default"):
        self.graph_position_algorithm = graph_position_algorithm
        self.traffic_circuit_diagram = self._set_up_graph()
        self.traffic_circuit_diagram_position = None

    def _set_up_graph(self):
        G = nx.Graph()
        return G

    def _set_up_graph_position(self, incoming_traffic_container):
        if self.graph_position_algorithm == "default":
            pos = nx.spring_layout(self.traffic_circuit_diagram)
        elif self.graph_position_algorithm == "Custom Algorithm 1":
            pos = incoming_traffic_container.traffic_lights_coordinates
        else:
            print("graph position algorithm not recognized, using default")
            pos = nx.spring_layout(self.traffic_circuit_diagram)
        return pos

    def upload_traffic_graph_to_engine(self, incoming_traffic_container):
        for traffic_light in incoming_traffic_container.traffic_lights:
            traffic_light_object = incoming_traffic_container.traffic_lights[traffic_light]
            color = self._get_node_color(traffic_light_object.traffic_status)
            shape = "o"
            if isinstance(traffic_light_object,LogicGateTrafficLight):
                if traffic_light_object.gate_type == "AND":
                    shape = "s"
                elif traffic_light_object.gate_type == "OR":
                    shape = "^"
            self.traffic_circuit_diagram.add_node(traffic_light_object.outcome_name, name=traffic_light_object.outcome_name, status=traffic_light_object.traffic_status, color = color, shape=shape)
        for road in incoming_traffic_container.roads:
            road_object = incoming_traffic_container.roads[road]
            width = 1
            print(road)
            if road_object.was_road_traversed:
                width = 2
            self.traffic_circuit_diagram.add_edge(road_object.incoming_light, road_object.outgoing_light, label=road, width=width)
        self.traffic_circuit_diagram_position = self._set_up_graph_position(incoming_traffic_container)

    def show_network_graph(self):
        for node, attributes in self.traffic_circuit_diagram.nodes(data=True):
            nx.draw_networkx_nodes(
                self.traffic_circuit_diagram, self.traffic_circuit_diagram_position,
                nodelist=[node],
                node_color=attributes["color"],
                node_shape=attributes["shape"],
                edgecolors="black",
                node_size=3000
            )
        nx.draw_networkx_edges(self.traffic_circuit_diagram, self.traffic_circuit_diagram_position)
        nx.draw_networkx_labels(self.traffic_circuit_diagram, self.traffic_circuit_diagram_position, font_weight="bold", font_size=8)
        plt.show()

    def _get_node_color(self, incoming_status) -> bool:
        color = "#FFFFFF"
        if incoming_status == "Complete":
            color = "#90EE90"
        elif incoming_status == "In Progress":
            color = "#ADD8E6"
        elif incoming_status == "Roadblock":
            color = "#FFFF00"
        elif incoming_status == "Not Started":
            color = "#FFFFFF"
        elif incoming_status == "Abandoned":
            color = "#FF0000"
        else:
            print("Color not recognized")

        return color