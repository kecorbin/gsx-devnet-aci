#!/usr/bin/env python
import cobra.model.fv
import cobra.mit.access
import cobra.mit.session
from cobra.mit.request import ConfigRequest
from cobra.internal.codec.jsoncodec import toJSONStr
import creds


def commit(md, mo):
    """
    Helper function to commit changes to a mo
    :param md: MoDirectory instance
    :param mo: Cobra object to be committed
    :return:
    """
    c = ConfigRequest()
    c.addMo(mo)
    return md.commit(c)

# Create a login session with APIC IP / credentials
ls = cobra.mit.session.LoginSession(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# Perform a DN based lookup using Cobra
cust1 = md.lookupByDn('uni/tn-Customer1')

# View an attribute
print cust1.name
