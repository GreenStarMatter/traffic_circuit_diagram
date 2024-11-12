from traffic_circuit_diagram.traffic_light import TrafficLight
from traffic_circuit_diagram.traffic_light import LogicGateTrafficLight
from traffic_circuit_diagram.road import Road

def test_change_outcome_name():
    first_light = TrafficLight("First Outcome", "In Progress")
    first_light.set_outcome_name("New First Outcome")
    assert first_light.outcome_name == "New First Outcome"

def test_set_traffic_status():
    first_light = TrafficLight("First Outcome", "In Progress")
    first_light.set_traffic_status("Complete")
    assert first_light.get_traffic_status() == "Complete"

def test_set_outgoing_road():
    first_light = TrafficLight("First Outcome", "In Progress")
    first_road = Road("Tested Using PyTest", False)
    first_light.set_outgoing_road(first_road)
    assert first_light.outgoing_roads[first_road] == first_road.road_name

def test_set_incoming_road():
    second_light = TrafficLight("SecondOutcome", "In Progress")
    first_road = Road("Tested Using PyTest", True)
    second_light.set_incoming_road(first_road)
    assert second_light.incoming_roads[first_road] == first_road.road_name

def test_set_gate_type():
    first_logic_light = LogicGateTrafficLight("SecondOutcome", "In Progress")
    first_logic_light.set_gate_type("AND")
    assert first_logic_light.get_gate_type() == "AND"

