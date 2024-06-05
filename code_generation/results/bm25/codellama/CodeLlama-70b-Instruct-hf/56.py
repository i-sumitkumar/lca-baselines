


```python
import seed_emulator

# Create an emulation with three autonomous systems (AS150, AS151, AS152)
emulator = seed_emulator.makeEmulatorBaseWith10StubASAndHosts(
    as_count=3,
    as_numbers=[150, 151, 152],
    shouldMerge=False,
    merge_as_number=None,
    merge_as_count=None,
    merge_as_routers_count=None,
    merge_as_networks_count=None,
    merge_as_hosts_count=None,
    merge_as_stubs_count=None,
    merge_as_transit_count=None,
    merge_as_ix_count=None,
    merge_as_host_count=None,
    merge_as_host_network_count=None,
    merge_as_host_network_prefix_count=None,
    merge_as_host_network_prefix_length=None,
    merge_as_host_network_prefix_length_min=None,
    merge_as_host_network_prefix_length_max=None,
    merge_as_host_network_prefix_length_step=None,
    merge_as_host_network_prefix_length_mode=None,
    merge_as_host_network_prefix_length_mode_min=None,
    merge_as_host_network_prefix_length_mode_max=None,
    merge_as_host_network_prefix_length_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_max=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_step=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode=None,
    merge_as_host_network_prefix_length_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_mode_min=None,
    merge_as_host_network_prefix_length_