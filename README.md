SDN Static Routing using Mininet & POX

Problem Statement:
Implement static routing in a Software Defined Network (SDN) using POX controller and Mininet.
Verify packet forwarding behavior and ensure routing consistency after network restart.

Tools Used:
Mininet
POX Controller
Open vSwitch
Ubuntu / WSL

Topology:
Linear topology with 2 switches:-
h1 ---- s1 ---- s2 ---- h2

Setup & Execution Steps:
Step 1: Start Controller
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 --port=6633 static_routing

Step 2: Run Mininet
sudo mn --topo linear,2 --controller=remote,ip=127.0.0.1,port=6633

Step 3: Test Connectivity
pingall
Expected:
0% packet loss

Step 4: Check Flow Tables
sudo ovs-ofctl dump-flows s1
sudo ovs-ofctl dump-flows s2

Regression Test:
exit
sudo mn -c
sudo mn --topo linear,2 --controller=remote
pingall

Same result observed -> proves static routing consistency

Failure Case (Optional):
Stop controller and test:-
pingall
Expected:
100% packet loss

Expected Output:
Successful communication between hosts
Flow rules installed in switches
Same routing behavior after restart

Proof of Execution:
Ping Results

(Add screenshot)

Flow Tables

(Add screenshots of s1 and s2)

Regression Test

(Add screenshot)

Conclusion:
Static routing was successfully implemented using POX controller.
Flow tables verified correct forwarding behavior and consistent routing was observed after restart.

References:
Mininet Documentation
POX Controller Documentation
Open vSwitch Documentation