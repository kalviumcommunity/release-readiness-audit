# Approved sizing brief (synthetic)
Keep 3 nodes, same region us-central1, USD, 730 hours/node/month, SQL HA and service scope.
Peak aggregate app/background requests: 1.5 vCPU / 3 GiB.
Illustrative system allowance per node: 0.5 vCPU / 2 GiB (not official allocatable formula).
One node may fail. Two candidate survivors offer 3 vCPU / 12 GiB after allowance.
Boot footprint=35 GiB/node; 50 GiB leaves 15 GiB headroom.
Only candidates: node profile 4 vCPU/16 GiB -> 2 vCPU/8 GiB, and disk 100 -> 50 GiB.
Use fixed prices in costs.json. Excluded: network, taxes, observability, backup use.
Validate real allocatable resources, placement, representative latency/load, failover and disk performance.
Disk reduction requires replacement/migration; existing Persistent Disk cannot shrink in place.
