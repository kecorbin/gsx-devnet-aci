#!/usr/bin/env python
import acitoolkit.acitoolkit as aci
import creds

session = aci.Session(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
session.login()

tenant = aci.Tenant('devnet2')

print 'Posting tenant {} to {}'.format(tenant.get_json(), session.api + tenant.get_url())

session.push_to_apic(tenant.get_url(), tenant.get_json())
