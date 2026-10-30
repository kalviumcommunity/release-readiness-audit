from support import load, require, main, ROOT


def audit():
    policy = load('ops/policy.json')
    require(policy['bindings'] == [{'role':'roles/logging.viewer','members':['user:reviewer@example.invalid']}],
            'Preserve existing least-privilege IAM binding.')
    require(policy['auditConfigs'] == [{'service':'storage.googleapis.com',
            'auditLogConfigs':[{'logType':'DATA_READ'},{'logType':'DATA_WRITE'}]}],
            'Storage audit block requires DATA_READ and DATA_WRITE; retain IAM bindings.')
    print('Storage DATA_READ/DATA_WRITE configured; existing IAM binding unchanged.')
    print('OFFLINE configuration check only: no cloud policy applied or audit event generated.')


def cost():
    data=load('fixtures/costs.json')
    totals={}
    for name in ('baseline','candidate'):
        x=data[name]
        total=x['nodes']*x['node_monthly']+x['nodes']*x['disk_gib_per_node']*x['disk_gib_monthly']+x['sql_monthly']+x['storage_monthly']
        totals[name]=total
        print(f'{name}: nodes={x["nodes"]} node_cost={x["nodes"]*x["node_monthly"]:.2f} disk_cost={x["nodes"]*x["disk_gib_per_node"]*x["disk_gib_monthly"]:.2f} SQL={x["sql_monthly"]:.2f} Storage={x["storage_monthly"]:.2f} total=USD {total:.2f}')
    saving=totals['baseline']-totals['candidate']
    print(f'Illustrative saving=USD {saving:.2f}/month ({100*saving/totals["baseline"]:.2f}% of baseline)')
    print('Candidate survivors: 3 vCPU/12 GiB after allowance, peak needs 1.5 vCPU/3 GiB.')
    print('50 GiB disks leave 15 GiB per node. Proposal requires real load/failover and disk checks.')
    print('Cost-review reasoning is manually graded; no production savings are measured.')


def review():
    print((ROOT/'fixtures/evidence-index.md').read_text())
    print('Verdict and owner/date/retest action require manual review, not a keyword PASS.')


if __name__=='__main__':
    raise SystemExit(main(dict(audit=audit,cost=cost,review=review)))
