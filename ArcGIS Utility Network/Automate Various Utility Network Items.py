#Script to Create a Utility Network Diagram
import arcpy

def create_network_diagram(utility_network, output_diagram):
    arcpy.CreateUtilityNetworkDiagram_management(utility_network, output_diagram)

utility_network = "Electric_Network"
output_diagram = r"C:\Output\electric_diagram"
create_network_diagram(utility_network, output_diagram)

#Script to Perform a Trace on the Utility Network:
import arcpy

def perform_trace(utility_network, starting_points, trace_type):
    trace_result = arcpy.TraceGeometricNetwork_management(utility_network, trace_type, starting_points)
    return trace_result

utility_network = "Electric_Network"
starting_points = "Poles"  # Starting points for the trace
trace_type = "TRACE_DOWNSTREAM"
result = perform_trace(utility_network, starting_points, trace_type)
print("Trace Result:", result)

#Script to Calculate Subnetworks in the Utility Network:
import arcpy

def calculate_subnetworks(utility_network):
    arcpy.CalculateDefaultSubnetworks_management(utility_network)

utility_network = "Electric_Network"
calculate_subnetworks(utility_network)

#Script to Generate Reports for the Utility Network:
import arcpy

def generate_network_report(utility_network, output_report):
    arcpy.GenerateUtilityNetworkReport_management(utility_network, output_report)

utility_network = "Electric_Network"
output_report = r"C:\Output\electric_network_report.txt"
generate_network_report(utility_network, output_report)
