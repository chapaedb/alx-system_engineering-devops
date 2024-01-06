Web Infrastructure Design

The architecture consists of two servers, one web server (Nginx), one application server, one load-balancer (HAproxy), one set of application files (your code base), and one database (MySQL).

Why we are adding each element:

Two servers: We need two servers to ensure high availability and redundancy. If one server fails, the other server can take over the workload.
One web server (Nginx): Nginx is a high-performance web server that can handle a large number of concurrent connections. It is also used as a reverse proxy to distribute traffic to the application servers.
One application server: The application server is responsible for running the application code and generating dynamic content.
One load-balancer (HAproxy): HAproxy is a load balancer that distributes traffic evenly across multiple servers. It uses a round-robin algorithm to distribute requests.
One set of application files (your code base): The application files contain the code that runs the website.
One database (MySQL): MySQL is a popular open-source relational database management system. It is used to store and manage the website’s data.
Distribution algorithm and Active-Active vs Active-Passive setup:

HAproxy is configured with a round-robin algorithm to distribute requests evenly across the two application servers. The load-balancer is configured with an Active-Active setup, which means that both application servers are active and serving traffic at all times. This setup provides better performance and availability than an Active-Passive setup, where one server is active and the other is passive.

How a database Primary-Replica (Master-Slave) cluster works:

In a Primary-Replica (Master-Slave) cluster, the primary node is the main database server that handles all write operations. The replica node is a backup server that receives a copy of all write operations from the primary node. The replica node can be used to handle read operations, which reduces the load on the primary node.

Difference between the Primary node and the Replica node in regard to the application:

The primary node is responsible for handling all write operations, while the replica node is used to handle read operations. This means that the primary node is more critical to the application’s performance and availability than the replica node.

Issues with this infrastructure:

Single point of failure (SPOF): The load balancer is a single point of failure. If it fails, the entire infrastructure will be unavailable.
Security issues: The infrastructure does not have a firewall or HTTPS enabled, which makes it vulnerable to attacks.
No monitoring: The infrastructure does not have any monitoring in place, which makes it difficult to detect and troubleshoot issues.
