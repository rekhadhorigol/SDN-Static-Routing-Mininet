# SDN Static Routing using Mininet & POX
### Rekha Dhorigol, PES1UG24CS370
### Section G

## Problem Statement
Implement static routing in a Software Defined Network (SDN) using POX controller and Mininet.

Verify packet forwarding behavior and ensure routing consistency after network restart.

## Tools Used
- Mininet
- POX Controller
- Open vSwitch
- Ubuntu / WSL

## Topology
Linear topology with 2 switches:
```bash
h1 ---- s1 ---- s2 ---- h2
```
## Setup & Execution Steps
Make sure to install Mininet, Open vSwitch, POX etc.

Also create **static_routing.py** and paste the code provided in the repo or your own code.

We'll need 3 terminals for execution.
### 1) Initial Cleanup & Setup
Terminal 1:
```bash
sudo mn -c
sudo killall pox.py
sudo service openvswitch-switch restart
```
### 2) Start Controller
Terminal 1:
```bash
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 --port=6633 static_routing
```
### 3) Run Mininet
Terminal 2:
```bash
sudo mn --topo linear,2 --controller=remote,ip=127.0.0.1,port=6633
pingall
```
***Expected Output:***
```bash
0% packet loss
```
### 4) Check Flow Tables
Terminal 3:
```bash
sudo ovs-ofctl dump-flows s1
sudo ovs-ofctl dump-flows s2
```
### 5) Regression Test (Restart Consistency)
Terminal 2:
```bash
exit
sudo mn -c
sudo mn --topo linear,2 --controller=remote
pingall
```
***Expected Output:***
(Same result)
```bash
0% packet loss
```
Same result observed -> proves static routing consistency
### 6) Confirms static routing consistency
**Failure Case (Controller Down):-**

Terminal 1: Stop Controller
```bash
Ctrl + C
```
Terminal 3: Clear Flow Tables
```bash
sudo ovs-ofctl del-flows s1
sudo ovs-ofctl del-flows s2
```
Terminal 2: Test Connectivity
```bash
pingall
```
***Expected Output:***
```bash
100% packet loss
```

## Additional Setup Commands (Development Phase)
Terminal 2:
```bash
sudo mn
```
Terminal 1:
```bash
sudo ovs-vsctl show
cd ~/pox
./pox.py log.level --DEBUG forwarding.l2_learning
```

## Edit your script (for controller)
```bash
nano ~/pox/static_routing.py
```

## Expected Output
- Successful communication between hosts
- Flow rules installed in switches
- Same routing behavior after restart

## Proof of Execution
(Refer to the screenshots provided in the repo!)

## Conclusion
Static routing was successfully implemented using POX controller.

Flow tables verified correct forwarding behavior and consistent routing was observed after restart.

## References
- Mininet Documentation
- POX Controller Documentation
- Open vSwitch Documentation

## Note
- Mininet, Open vSwitch and POX were installed using apt and Git
- POX is an SDN controller. SDN is the architecture and POX is one implementation used to control the network
