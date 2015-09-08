#!/usr/bin/env python
import cobra.model.fv
import cobra.mit.access
import cobra.mit.session
from cobra.mit.request import ConfigRequest
from cobra.internal.codec.jsoncodec import toJSONStr
import creds



# Create a login session with APIC IP / credentials
ls = cobra.mit.session.LoginSession(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# Perform a class based lookup using Cobra
endpoints = md.lookupByClass('fvCEp')

# Display some information about the returned objects
print 'Endpoints'
template = "{0:70} {1:30} {2:15} {3:20}"
print(template.format("EPG", "MAC", "IP Address ", "Encap"))
print(template.format("=" * 60, "=" * 15, "=" * 15, "=" * 10 ))

for ep in endpoints:
    print template.format(ep.parentDn, ep.mac, ep.ip, ep.encap)
