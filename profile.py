"""This topology has one host.

To use this topology, follow the instructions at: [Hello Linux](https://teaching-on-testbeds.github.io/hello-linux/)

"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as rspec
# Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal context, needed to defined parameters
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Set up first host - romeo
node_romeo = request.RawPC("romeo")

node_romeo.startVNC()

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
