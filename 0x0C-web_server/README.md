# 0x0C. Web server
* What is the main role of a web server?
A web server's main role is to serve web content (web pages, files, etc.) to clients (typically web browsers) over the internet. It processes requests from clients and responds with the appropriate content, which may include HTML pages, images, CSS, JavaScript, or other resources.

* What is a child process?
In computing, a child process is a process created by another process, known as the parent process. The child process inherits various attributes (like file handles and memory) from its parent but operates independently.

* Why do web servers usually have a parent process and child processes?
Web servers often have a parent process and child processes to handle incoming client requests efficiently. The parent process listens for incoming requests and creates child processes to handle these requests. This allows the server to handle multiple requests concurrently, improving performance and responsiveness.

* What are the main HTTP requests?
What are the main HTTP requests?
The main HTTP requests are:

GET: Retrieve data from the server.
POST: Submit data to be processed to a specified resource.
PUT: Update a current resource with new data.
DELETE: Remove a resource from the server.
HEAD: Retrieve headers of a resource without the body.
OPTIONS: Describe the communication options for the target resource.
PATCH: Apply partial modifications to a resource.
DNS (Domain Name System)
What does DNS stand for?
DNS stands for Domain Name System.

* What is DNS's main role?
The main role of DNS is to translate human-readable domain names (like example.com) into IP addresses (e.g., 192.168.1.1) that are used by computers to communicate over a network.

* DNS Record Types:
A (Address) Record:
Associates a domain name with an IPv4 address.

* CNAME (Canonical Name) Record:
Maps an alias (alternate) domain name to the canonical (primary) domain name.

* TXT (Text) Record:
Used to associate arbitrary text with a domain, often used for human-readable information.

* MX (Mail Exchange) Record:
Specifies the mail server responsible for receiving and handling email messages for a domain.
