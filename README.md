# py-ping

**py-ping** is a modern, high-performance network diagnostic suite. Unlike traditional ping tools, `py-ping` is designed to run in a fully sandboxed environment, demonstrating that robust networking utilities can be both powerful and secure.

## Key Features

* **Low-Level Probing**: Native ICMP implementation using raw sockets.
* **Snap-First Design**: Built for **Strict Confinement**, ensuring the tool only accesses the network and nothing else.
* **Structured Diagnostics**: Export network health data in `.json` for integration with monitoring pipelines.
* **Rich Visualization**: Terminal-based HUD for real-time latency and packet loss tracking.

## Project Structure
_Mostly placeholders still!_

```
py-ping
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│   ROADMAP.md
│   setup.py
│   snapcraft.yaml
│   
└───src
    │   config.py
    │   hud.py
    │   logger.py
    │   main.py
    │   
    └───os
            apple.py
            linux.py
            windows.py
```

## Installation (Snap)

```text
    __   __      __________      __________      __________
   |  |_|  |    |          |    |          |    |          |
   |_______|    |  COMING  |    |  ALMOST  |    |  STAY    |
  /_______/     |   SOON   |    |  THERE   |    |  TUNED   |
 [oo----oo]     [oo----oo]      [oo----oo]      [oo----oo]
############################################################
```

## help

im still learning if you see something that could look better let me know!

### thank you for reading 
