#!/usr/bin/env python
import acitoolkit.acitoolkit as aci
import creds

session = aci.Session(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
session.login()

epgs = aci.EPG.get(session)

for epg in epgs:
    print "EPG Name: {} EPG Description: {}".format(epg.name, epg.descr)