"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Server:
    # Class variable shared by all Server objects.
    network = "Enterprise Network"

    def __init__(self, hostname, ip_address):
        # Instance variable stor information unique to each server object.
        self.hostname = hostname
        self.ip_address = ip_address

    def display_info(self):
        # Display the basic information stored in this Server object
        print (f"Hostname: {self.hostname}")
        print(f"IP Address: {self.ip_address}")

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class StigServer(Server):
    """STIG is an acronym for Security Technical Implementation Guide"""
    """DISA is an acronym for Defense Information Systems Agency (DoD)"""

    # Class variable shared by all StigServer objects.
    authority = "DISA"

    def __init__(self, hostname, ip_address, baseline):
        # super() calls the Server constructor to initialize inherited data.
        super().__init__(hostname, ip_address)

        # These instance variables are specific to StigServer objects
        self.baseline = baseline
        self.findings = []

    def add_finding(self, finding):
        # Add a new STIG finding to this server's findings list
        if not finding:
            return False

        # Edge case: check for findings that are already open on the server.
        if finding in self.findings:
            return False

        self.findings.append(finding)
        return True

    # Created Extension
    def remediate_findings(self, finding):
        # Remove the finding only if it is currently open on the server.
        if finding in self.findings:
            self.findings.remove(finding)
            return True

        # Return False when the requested finding is not in the list
        return False

    # This method overrides Server.display_info().
    def display_info(self):
        # Resue the parent method displaying STIG-specific information
        super().display_info()
        print(f"STIG Baseline: {self.baseline}")

        # Join the findings for a clean output.
        if self.findings:
            print("Open Findings: " + ", ".join(self.findings))
        else:
            print("Open Findings: None")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Each object get its own instance variables and instance namespace.
    server1 = StigServer("rhel01", "192.168.1.1","RHEL 9 STIG")
    server2 = StigServer("win02", "192.168.1.2","Windows Server 2022 STIG")

    # A class variable through can be accessed through the class or an object.
    print("Class variable through class:", StigServer.authority)
    print("Class variable through object:", server1.authority)

    # Added an attribute to server1 after the object has been created.
    server1.poam_due = "September 30, 2026"

    # __dict__ shows the instance namespace for each object
    print("\nserver1 namespace:")
    print(server1.__dict__)
    print("\nserver2 namespace:")
    print(server2.__dict__)

    # The class __dict__ shows names stored in the class namespace
    print("\nStigServer class namespace:")
    print(StigServer.__dict__.keys())


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # The findings list is mutable data stored inside the StigServer object.
    original = StigServer("rhel02", "192.168.1.3", "RHEL 9 STIG")
    original.add_finding("V-257777")

    # copy() creates a shallow copy
    shallow = copy(original)

    # deepcopy() creates an independent copy of the objected nested data.
    deep = deepcopy(original)

    original.add_finding("V-257778")

    """The original and shallow copy both show the new finding because
    they share the same nested findings list. The deep copy has its
    own independent list, so it remains unchanged."""
    print("\nOriginal findings:", original.findings) # Show new finding
    original.display_info()
    print("\nShallow copy findings:", shallow.findings) # Show new finding
    shallow.display_info()
    print("\nDeep copy findings:", deep.findings) # Show unchanged finding
    deep.display_info()


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    server = Server("files01","192.168.1.1")
    server.display_info()

    print("\n=== Child Object ===")
    # Created a StigServer object and added one open STIG finding.
    stig_server = StigServer("rhel01", "192.168.1.2","RHEL 9 STIG")
    stig_server.add_finding("V-257778")

    # Calls the overriden display_info() method from StigServer
    stig_server.display_info()

    print("\n=== Extension ===")
    if stig_server.remediate_findings("V-257778"):
        print("V-257778 was remediated.")

    stig_server.display_info()

    # Edge case: attempt to remediate a finding that is not open
    print("\n=== Edge Case ===")
    if not stig_server.remediate_findings("V-357779"):
        print("V-357779 was not an open finding.")

    demonstrate_namespaces()
    demonstrate_copying()

if __name__ == "__main__":
    main()