import docker

class DockerMonitor:
    def __init__(self):
        self.client = docker.from_env()

    def get_container_stats(self):
        container_stats = {}
        for container in self.client.containers.list():
            stats = container.stats(stream=False)
            container_stats[container.name] = {
                'cpu_usage': stats['cpu_stats']['cpu_usage']['total_usage'],
                'memory_usage': stats['memory_stats']['usage'],
                'network_rx_bytes': stats['networks']['eth0']['rx_bytes'],
                'network_tx_bytes': stats['networks']['eth0']['tx_bytes']
            }
        return container_stats

if __name__ == "__main__":
    monitor = DockerMonitor()
    stats = monitor.get_container_stats()
    for name, stat in stats.items():
        print(f"Container: {name}")
        print(f"CPU Usage: {stat['cpu_usage']}")
        print(f"Memory Usage: {stat['memory_usage']}")
        print(f"Network RX: {stat['network_rx_bytes']} bytes")
        print(f"Network TX: {stat['network_tx_bytes']} bytes")
        print("-" * 40)
