# Static Routing using SDN Controller

# This controller (POX) installs static flow rules on switches when they connect
# It defines a fixed forwarding path between hosts in a linear topology:
# h1 ---- s1 ---- s2 ---- h2

# The controller listens for switch connection events and installs
# flow rules based on switch ID (DPID)

from pox.core import core
import pox.openflow.libopenflow_01 as of

# Logger for printing controller messages
log = core.getLogger()


# This function is triggered whenever a switch connects to the controller
def _handle_ConnectionUp(event):
    # Get the switch ID (DPID)
    dpid = event.connection.dpid

    # Log switch connection
    log.info("Switch %s has connected", dpid)

    # Rules for Switch 1 (s1)
    if dpid == 1:
        # Rule 1: Forward packets coming from h1 (port 1) to s2 (port 2)
        msg = of.ofp_flow_mod()
        msg.match.in_port = 1
        msg.actions.append(of.ofp_action_output(port=2))
        event.connection.send(msg)

        # Rule 2: Forward packets coming from s2 (port 2) back to h1 (port 1)
        msg = of.ofp_flow_mod()
        msg.match.in_port = 2
        msg.actions.append(of.ofp_action_output(port=1))
        event.connection.send(msg)

    # Rules for Switch 2 (s2)
    elif dpid == 2:
        # Rule 1: Forward packets coming from s1 (port 1) to h2 (port 2)
        msg = of.ofp_flow_mod()
        msg.match.in_port = 1
        msg.actions.append(of.ofp_action_output(port=2))
        event.connection.send(msg)
        
        # Rule 2: Forward packets coming from h2 (port 2) back to s1 (port 1)
        msg = of.ofp_flow_mod()
        msg.match.in_port = 2
        msg.actions.append(of.ofp_action_output(port=1))
        event.connection.send(msg)


# Launch function - called when POX starts this module
def launch():
    # Register the ConnectionUp event handler
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)