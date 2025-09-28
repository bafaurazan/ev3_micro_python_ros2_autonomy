#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist  # zakładam, że /cmd/vel_nav to Twist, zmień jeśli inny typ
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

PORT = 8083
CMD = "0.0"  # przechowuje np. prędkość liniową z Twist

linear_x = "0.0"
angular_z = "0.0"

class CmdSubscriber(Node):
    def __init__(self):
        super().__init__('cmd_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel_nav',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        global CMD
        global linear_x
        global angular_z

        linear_x = msg.linear.x
        angular_z = msg.angular.z
        
        # przykładowo bierzemy tylko prędkość liniową w osi x
        CMD = f"{linear_x} {angular_z}"

        self.get_logger().info(f"Odebrano CMD: {CMD}")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/command":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(CMD.encode())
        else:
            self.send_response(404)
            self.end_headers()


def ros_spin(node):
    rclpy.spin(node)


def main():
    rclpy.init()
    node = CmdSubscriber()

    # ROS w osobnym wątku
    t = threading.Thread(target=ros_spin, args=(node,), daemon=True)
    t.start()

    # HTTP server
    with HTTPServer(("", PORT), Handler) as server:
        print("Serwer gotowy na porcie", PORT)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# from http.server import BaseHTTPRequestHandler, HTTPServer 

# PORT = 8083 
# CMD = "40" 

# class Handler(BaseHTTPRequestHandler): 
#     def do_GET(self): 
#         if self.path == "/command": 
#             self.send_response(200) 
#             self.send_header("Content-type", "text/plain") 
#             self.end_headers() 
#             self.wfile.write(CMD.encode()) 
#         else: 
#             self.send_response(404) 
#             self.end_headers() 

# with HTTPServer(("", PORT), Handler) as server: 
#     print("Serwer gotowy na porcie", PORT) 
#     server.serve_forever()