# py-ping

> [!NOTE]
> **Academic & Development Status**
> `py-ping` is a project developed by @doccy-dev as part of undergraduate studies at UniSQ. It serves as a practical application of Python-based networking, focusing on **Strict Confinement** and secure system interfacing within the Ubuntu ecosystem.

**py-ping** is a modern, high-performance network diagnostic suite. Unlike traditional ping tools, `py-ping` is designed to run in a fully sandboxed environment, demonstrating that robust networking utilities can be both powerful and secure.

## Key Features

* **Low-Level Probing**: Native ICMP implementation using raw sockets.
* **Snap-First Design**: Built for **Strict Confinement**, ensuring the tool only accesses the network and nothing else.
* **Structured Diagnostics**: Export network health data in `.json` for integration with monitoring pipelines.
* **Rich Visualization**: Terminal-based HUD for real-time latency and packet loss tracking.

## Installation (Snap)

Since `py-ping` uses raw sockets for ICMP packets, it requires specific interface connections after installation:

```bash
sudo snap install py-ping --edge
sudo snap connect py-ping:network-observe
sudo snap connect py-ping:network-bind
```

## help

im still learning if you see something that could look better let me know!

### thank you for reading 
