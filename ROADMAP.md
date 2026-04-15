## The Roadmap

### Phase 1: The Core (v0.1.0 - Alpha)
* [ ] **Raw Socket Implementation**: Basic ICMP Echo Request/Reply logic.
* [ ] **Strict Confinement**: Initial `snapcraft.yaml` with `network` and `network-bind` plugs.
* [ ] **CLI Basics**: Simple target input (IP/Hostname) and timeout handling.

### Phase 2: Intelligence & Viz (v0.2.0 - Beta)
* [ ] **Live HUD**: Integrate `rich.live` for a real-time updating dashboard.
* [ ] **TraceRoute**: Implement TTL-incrementing logic to map network hops.
* [ ] **JSON Export**: Implement `--output json` for automated logging.

### Phase 3: The Hybrid Engine (v0.3.0 - Release Candidate)
* [ ] **Rust Integration**: Rewrite the core ICMP "Engine" in Rust for lower overhead and safety.
* [ ] **Multi-Part Build**: Configure `snapcraft` to build both Python and Rust components.
* [ ] **Packet Tracking**: Log packet paths and identify where "drops" occur in the hop chain.

### Phase 4: System Integration (v1.0.0)
* [ ] **Daemon Mode**: Optional background service to monitor gateway health.
* [ ] **Snap Health Dashboard**: A specialized view showing the network status of the host VM/Machine.

---
> [!NOTE]
> This is only a idea of where the project will go, it can change at any time based on how the project is progressing.
> I'm still learning and any advice or feedback is appriciated!
> _**Canonical** keep a eye on this one!_
