class TrafficLight:
    def __init__(self,outcome_name: str, traffic_status: str):
        self.outcome_name = outcome_name
        self.traffic_status = traffic_status
        self.incoming_roads = {}
        self.outgoing_roads = {}

    def set_outcome_name(self, incoming_name: str) -> bool:
        self.outcome_name = incoming_name
        return True

    def set_traffic_status(self, incoming_status: str) -> bool:
        viable_status = False
        if incoming_status in ["Complete","In Progress","Roadblock","Not Started","Abandoned"]:
             self.traffic_status = incoming_status
             viable_status = True
        else:
             print("Nonviable Status, Retaining Old Status")
        return viable_status

    def get_traffic_status(self) -> str:
        return self.traffic_status

    def set_incoming_road(self, incoming_road) -> bool:
        self.incoming_roads[incoming_road] = incoming_road.road_name
        return True

    def set_outgoing_road(self, outgoing_road) -> bool:
        self.outgoing_roads[outgoing_road] = outgoing_road.road_name
        return True

    def _set_light_color(self) -> bool:
        return True

class LogicGateTrafficLight(TrafficLight):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gate_type = "MULTI"

    def set_gate_type(self, incoming_gate_type: str) -> bool:
        viable_gate = False
        if incoming_gate_type in ["MULTI","AND","OR","XOR"]:
            self.gate_type = incoming_gate_type
            viable_gate = True
        return viable_gate

    def get_gate_type(self) -> str:
        return self.gate_type

    def _set_gate_shape(self) -> bool:
        return True