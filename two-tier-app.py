#!/usr/bin/env python
import cobra.mit.session
import cobra.mit.access
import cobra.mit.request
import cobra.model.pol
import cobra.model.fv
import cobra.model.vz
import creds
import json
from cobra.internal.codec.jsoncodec import toJSONStr

ls = cobra.mit.session.LoginSession(creds.APIC_URL, creds.APIC_USER, creds.APIC_PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

tenant = 'devnet-full'
app = 'devnet-app'
gateway = '1.1.1.1/24'

# lookup the top level object on which operations will be made
topMo = md.lookupByDn('uni')

# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(topMo, name=tenant)

# Create various Filters needed for contract subjects
vzFilter = cobra.model.vz.Filter(fvTenant, name='http')
vzEntry = cobra.model.vz.Entry(vzFilter, etherT='ip', prot='6', dFromPort='80', name='e1', dToPort='80')
vzFilter2 = cobra.model.vz.Filter(fvTenant, name='https')
vzEntry2 = cobra.model.vz.Entry(vzFilter2, etherT='ip', prot='6', dFromPort='443', name='e1', dToPort='443')
vzFilter3 = cobra.model.vz.Filter(fvTenant, name='mysql')
vzEntry3 = cobra.model.vz.Entry(vzFilter3,  etherT='ip', prot='6', dFromPort='3306', name='e1', dToPort='3306')
# Create a contract, w
vzBrCP = cobra.model.vz.BrCP(fvTenant, name='web-contract')
vzSubj = cobra.model.vz.Subj(vzBrCP, name='http')
vzRsSubjFiltAtt = cobra.model.vz.RsSubjFiltAtt(vzSubj, tnVzFilterName='http')
vzRsSubjFiltAtt2 = cobra.model.vz.RsSubjFiltAtt(vzSubj, tnVzFilterName='https')
vzBrCP3 = cobra.model.vz.BrCP(fvTenant, name='db-contract')
vzSubj3 = cobra.model.vz.Subj(vzBrCP3, name='mysql')
vzRsSubjFiltAtt4 = cobra.model.vz.RsSubjFiltAtt(vzSubj3, tnVzFilterName='mysql')
fvCtx = cobra.model.fv.Ctx(fvTenant, name=tenant+'-ctx1')
fvBD = cobra.model.fv.BD(fvTenant, name=tenant+'-bd1')
fvBD2 = cobra.model.fv.BD(fvTenant, name=tenant+'-inside', unkMacUcastAct='flood',arpFlood='true',unicastRoute='false')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName=tenant+'-ctx1')
fvRsCtx2 = cobra.model.fv.RsCtx(fvBD2, tnFvCtxName=tenant+'-ctx1')

fvSubnet = cobra.model.fv.Subnet(fvBD, ip=gateway)
fvAp = cobra.model.fv.Ap(fvTenant, name=app)

fvAEPg = cobra.model.fv.AEPg(fvAp, name='web-epg')
fvRsProv = cobra.model.fv.RsProv(fvAEPg, tnVzBrCPName='web-contract')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=tenant+'-bd1')
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName='db-contract')
fvAEPg3 = cobra.model.fv.AEPg(fvAp, name='db-epg')
fvRsProv3 = cobra.model.fv.RsProv(fvAEPg3, tnVzBrCPName='db-contract')
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, tnFvBDName=tenant+'-bd1')
c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)

print toJSONStr(fvTenant, prettyPrint=True)