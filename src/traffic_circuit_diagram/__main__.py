import sys
import os
import importlib.resources
from traffic_circuit_diagram.environment_setter import EnvironmentSetter

def main():
    print("Main Loop Run")
    if  "--local_test" in sys.argv:
        print("Run Local Tests")
        run_from_local_test_file()

def run_from_local_test_file():
    data_folder = os.path.join(os.path.dirname(__file__), 'data')
    data_file = os.path.join(data_folder, "test_graph_file.txt")
    test_environment = EnvironmentSetter(data_file)
    test_environment.read_save_file()
    test_environment.execute_command_list()
    test_environment.set_up_graph_using_engine()
    test_environment.upload_stored_graph_to_engine()
    test_environment.show_network_graph()



if __name__ =="__main__":
    main()