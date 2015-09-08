#!/usr/bin/env python
import cobra.mit.session
import cobra.mit.access
import creds
from cobra.mit.request import ConfigRequest

ls = cobra.mit.session.LoginSession(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()
subnets = md.lookupByClass('fvSubnet')

template = "{0:70} {1:30} {2:40}"
print(template.format("Bridge Domain", "Subnet", "Description"))

for s in subnets:
    s.descr = 'this is new description'
    print template.format(s.parentDn, s.ip, s.descr)
    s.descr = 'this is new description'



