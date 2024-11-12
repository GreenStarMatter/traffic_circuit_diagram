from traffic_circuit_diagram.road import Road
from traffic_circuit_diagram.traffic_light import TrafficLight
from traffic_circuit_diagram.traffic_light import LogicGateTrafficLight


def test_change_outcome_name():
    first_road = Road("Tested Using PyTest", False)
    first_road.set_road_name("Tested Using PyTest and Linter")
    assert first_road.road_name == "Tested Using PyTest and Linter"

def test_road_was_traversed():
    first_road = Road("Tested Using PyTest", False)
    assert first_road.get_if_road_was_traversed() == False

    first_road.set_road_traversel_status(True)
    assert first_road.get_if_road_was_traversed() == True

def test_set_incoming_light():
    first_road = Road("Tested Using PyTest", False)
    first_light = TrafficLight("First Outcome", "Completed")
    first_road.set_incoming_traffic_light(first_light)
    assert first_road.incoming_light == first_light
    

def test_set_outgoing_light():
    first_road = Road("Tested Using PyTest", False)
    second_light = TrafficLight("Second Outcome", "In Progress")
    first_road.set_outgoing_traffic_light(second_light)
    assert first_road.outgoing_light == second_light