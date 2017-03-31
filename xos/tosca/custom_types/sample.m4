tosca_definitions_version: tosca_simple_yaml_1_0

# compile this with "m4 sample.m4 > sample.yaml"

# include macros
include(macros.m4)

node_types:
    tosca.nodes.SampleService:
        derived_from: tosca.nodes.Root
        description: >
            Sample Service
        capabilities:
            xos_base_service_caps
        properties:
            xos_base_props
            xos_base_service_props