#!/usr/bin/env python
import cobra.model.fv
import cobra.mit.access
import cobra.mit.session
from cobra.mit.request import ConfigRequest
from cobra.internal.codec.jsoncodec import toJSONStr
import creds
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


def commit(md, mo):
    """
    Helper function to commit changes to a mo
    :param md: MoDirectory instance
    :param mo: Cobra object to be committed
    :return: Response object
    """
    c = ConfigRequest()
    c.addMo(mo)
    return md.commit(c)

# Create a login session with APIC IP / credentials
ls = cobra.mit.session.LoginSession(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# Perform a class based lookup using Cobra
tenants = md.lookupByClass('fvTenant')

# Display some information about the returned objects
for t in tenants:
    print "Tenant Name: {} Description: {}".format(t.name, t.descr)

