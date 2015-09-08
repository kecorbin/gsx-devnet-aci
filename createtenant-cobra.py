#!/usr/bin/env python
import cobra.model.fv
import cobra.mit.access
import cobra.mit.session
from cobra.mit.request import ConfigRequest
import creds

# Create a login session with APIC IP / credentials
ls = cobra.mit.session.LoginSession(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# Create MO object for root of the object tree
root = md.lookupByDn('uni')

# Create a tenant
cobratenant = cobra.model.fv.Tenant(root, 'cobratenant')

# Create a
c = ConfigRequest()
c.addMo(root)

# Get the URL to POST to
print 'Posting {} to {}'.format(c.data, c.getUrl(ls))

md.commit(c)