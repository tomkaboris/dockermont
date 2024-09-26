import docker
import os
import subprocess

class DockerMonitor:
    def __init__(self):
        self.client = docker.from_env()

    def get_container_stats(self):
        container_stats = {}
        for container in self.client.containers.list():
            stats = container.stats(stream=False)
            # Get disk usage through 'docker exec' by inspecting the filesystem within the container
            disk_usage = self.get_container_disk_usage(container)

            container_stats[container.name] = {
                'cpu_usage': stats['cpu_stats']['cpu_usage']['total_usage'],
                'memory_usage': stats['memory_stats']['usage'],
                'network_rx_bytes': stats['networks']['eth0']['rx_bytes'],
                'network_tx_bytes': stats['networks']['eth0']['tx_bytes'],
                'disk_usage': disk_usage
            }
        return container_stats

    def get_container_disk_usage(self, container):
        # Running 'df -h' inside the container to get disk usage
        try:
            # Execute 'df' inside the container
            exec_command = container.exec_run("df -h /")
            output = exec_command.output.decode("utf-8").strip().splitlines()
            # Parse the output to get disk usage percentage (e.g. '50%')
            disk_usage = output[1].split()[4]
            return disk_usage
        except docker.errors.APIError as e:
            return f"Error fetching disk usage: {e}"

if __name__ == "__main__":
    monitor = DockerMonitor()
    stats = monitor.get_container_stats()
    for name, stat in stats.items():
        print(f"Container: {name}")
        print(f"CPU Usage: {stat['cpu_usage']}")
        print(f"Memory Usage: {stat['memory_usage']}")
        print(f"Network RX: {stat['network_rx_bytes']} bytes")
        print(f"Network TX: {stat['network_tx_bytes']} bytes")
        print(f"Disk Usage: {stat['disk_usage']}")
        print("-" * 40)
