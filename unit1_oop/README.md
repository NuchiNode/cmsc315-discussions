# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.
For this assignment, I created a program based on my system administration work with Defense Information Systems Agency (DISA) 
Security Technical Implementation Guide (STIG) compliance. A STIG (Security Technical Implementation Guide) is a security hardening 
checklist published by DISA, and each requirement that is not met on a system is tracked as an open finding under a vulnerability ID 
(for example, V-257778). I implemented this with a Server parent class and a StigServer child class, so the program used inheritance 
similar to a real infrastructure is organized. Every server shares basic attributes, and STIG-tracked servers add compliance data on top.

## Class Design
I created a parent class named "Server" to store information every server has. A "hostname" and an "ip_address" as instance variables, plus
a "network" class variable shared by all Server objects. Its "display_info()" method printed the basic information for a server.

I then created the StigServer child class, which inherited from Server. It added an authority class variable ("DISA"), two new instance 
variables (baseline and a findings list), and two new methods: add_finding() and remediate_findings(). Each StigServer object owned its own 
findings list, which started empty and grew one entry at a time as findings were logged. All changes to the list went through the class's 
methods rather than outside code editing it directly.

## Inheritance and Method Overriding
The StigServer constructor called super().__init__(hostname, ip_address) so the parent class initialized the inherited attributes instead of 
repeating that code. I also overrode display_info(): the child version reused the parent's method through super().display_info() and then printed 
the STIG baseline and open findings. I joined the findings with ", ".join(...) so the output showed clean IDs instead of list brackets and quotes.

## Namespaces
The namespace demonstration created two StigServer objects (a RHEL 9 server and a Windows Server 2022 server) and showed that the authority class 
variable could be read through the class itself or through an object, because Python checks the instance namespace first and then the class namespace.
I added a poam_due attribute (a POA&M due date) to only one object after it was created. Printing each object's __dict__ showed that the new attribute 
existed only in that one object's instance namespace, while printing the class __dict__ keys showed that the class variable and the methods were stored 
once in the class namespace rather than in every object.

## Shallow and Deep Copying

The copy demonstration created a StigServer with one open finding, then made a shallow copy with copy() and a deep copy with deepcopy(). After I added a 
second finding to the original, the shallow copy showed the new finding too, because the shallow copy was a new object whose findings attribute still 
referenced the same nested list. The deep copy did not change, because it received its own independently allocated copy of the list.

## Edge Cases
1. add_finding() rejected an empty finding ID and rejected a finding that was already open on the server, returning False in both cases. The append only ran after both checks passed.
2. remediate_findings() returned False when asked to close a finding that was not open; main() demonstrated this with V-357779, and the output displayed it was not an open finding.
3. display_info() handled an empty findings list by printing "Open Findings: None", which appeared in the output after the last finding was remediated.

## Extension
My created extension was the remediate_findings() method, which closed a finding after a fix was applied. If the finding was open, it was removed from the list and the method returned 
True; otherwise the method returned False.

## Real-World Use
This mirrors how compliance tracking works in system administration. Many servers share common inventory data, while STIG-tracked systems have a baseline and a working list of open 
findings that grows after scans and shrinks as items are remediated. The same design could be used for patch tracking or configuration management.