class Road:
    def __init__(self,road_name: str, was_road_traversed: bool):
        self.road_name = road_name
        self.was_road_traversed = was_road_traversed
        self.incoming_light = None
        self.outgoing_light = None

    def set_road_name(self, incoming_name: str) -> bool:
        self.road_name = incoming_name
        return True

    def set_road_traversel_status(self, incoming_traversal_status: bool) -> bool:
        self.was_road_traversed = incoming_traversal_status
        return True

    def get_if_road_was_traversed(self) -> bool:
        return self.was_road_traversed

    def set_incoming_traffic_light(self, incoming_traffic_light) -> bool:
        self.incoming_light = incoming_traffic_light
        return True

    def set_outgoing_traffic_light(self, outgoing_traffic_light) -> bool:
        self.outgoing_light = outgoing_traffic_light
        return True

    def _set_line_thickness(self) -> bool:
        return True