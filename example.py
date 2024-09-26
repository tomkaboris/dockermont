from dockermont.monitor import DockerMonitor

# Initialize Docker Monitor
monitor = DockerMonitor()

# Fetch the container stats
stats = monitor.get_container_stats()

# Display the stats for each container
for name, stat in stats.items():
    print(f"Container: {name}")
    print(f"CPU Usage: {stat['cpu_usage']} nanoseconds")
    print(f"Memory Usage: {stat['memory_usage']} bytes")
    print(f"Network RX: {stat['network_rx_bytes']} bytes")
    print(f"Network TX: {stat['network_tx_bytes']} bytes")
    print("-" * 40)
