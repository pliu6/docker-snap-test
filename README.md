# Steps to reproduce the problem

1. Build the dockertest snap with snapcraft (On development machine Ubuntu 16.04 LTS)

2. Test the snap on the machine with all-snap image (16.04 amd64). The machine must have a Wi-Fi device and must be reboot before the test.
```
#snap list
Name             Version     Rev  Developer  Notes
core             16.04.1     714  canonical  -
docker           1.11.2-9    56   canonical  devmode
dockertest       0.0.1       x12             devmode
pc               16.04-0.8   9    canonical  -
pc-kernel        4.4.0-53-2  51   canonical  -
```
Test steps
```
#install docker snap
snap install docker --devmode

#install the test snap
snap install dockertest_0.0.1_amd64.snap --devmode

#pull the nginx image
sudo docker pull nginx:latest

#run the script to setup virtual Wi-Fi network interface
sudo sh ./prepare.sh

#Run the test snap
sudo dockertest
```

#################################
```
Kernel panic

[  504.783341] BUG: unable to handle kernel paging request at fffffffffffffff3
[  504.867186] IP: [<ffffffff813fe6c0>] strlen+0x0/0x20
[  504.926879] PGD 1e0d067 PUD 1e0f067 PMD 0 
[  504.976588] Oops: 0000 [#1] SMP 
[  505.015690] Modules linked in: veth xt_addrtype br_netfilter ipt_REJECT nf_reject_ipv4 ipt_MASQUERADE nf_nat_masquerade_ipv4 xt_comment xt_conntrack iptable_nat nf_conntrack_ipv4 nf_defrag_ipv4 nf_nat_ipv4 nf_nat nf_conntrack bridge stp llc overlay aufs arc4 ath9k ath9k_common ath9k_hw ath mac80211 cfg80211 kvm_amd uas kvm irqbypass k10temp r8169 mii sp5100_tco mac_hid i2c_piix4 shpchp iptable_filter ip_tables ip6table_filter ip6_tables x_tables autofs4 mmc_block sdhci_acpi sdhci_pci sdhci virtio_scsi nls_iso8859_1 usb_storage ahci libahci
[  505.599099] CPU: 1 PID: 2414 Comm: snap-confine Not tainted 4.4.0-53-generic #74-Ubuntu
[  505.694977] Hardware name: PC Engines APU, BIOS SageBios_PCEngines_APU-45 04/05/2014
[  505.787738] task: ffff880037637080 ti: ffff880061a70000 task.ti: ffff880061a70000
[  505.877382] RIP: 0010:[<ffffffff813fe6c0>]  [<ffffffff813fe6c0>] strlen+0x0/0x20
[  505.966192] RSP: 0018:ffff880061a73a20  EFLAGS: 00010246
[  506.029835] RAX: ffff880061a73b20 RBX: fffffffffffffff3 RCX: 0000000000000000
[  506.115320] RDX: 000000000000014e RSI: fffffffffffffff3 RDI: fffffffffffffff3
[  506.200802] RBP: ffff880061a73a38 R08: ffff88005c835138 R09: ffff880061a73a94
[  506.286283] R10: 000000000000000e R11: ffff88005c835131 R12: ffff88007aff0480
[  506.371767] R13: ffff880037637080 R14: ffffffff81399fc0 R15: 00000000fffffff3
[  506.457251] FS:  00007fa9f36aa740(0000) GS:ffff88007df00000(0000) knlGS:0000000000000000
[  506.554170] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  506.623014] CR2: fffffffffffffff3 CR3: 000000007853e000 CR4: 00000000000006e0
[  506.708497] Stack:
[  506.732624]  ffffffff81122a1a ffff88007aff0480 ffff880061a73b00 ffff880061a73a60
[  506.822056]  ffffffff8139a028 ffff88007aff0480 ffff880061a73b00 ffff880037637080
[  506.911490]  ffff880061a73ad8 ffffffff8136f088 ffffffff812285c0 ffff880061a73af0
[  507.000926] Call Trace:
[  507.030263]  [<ffffffff81122a1a>] ? audit_log_untrustedstring+0x1a/0x30
[  507.109502]  [<ffffffff8139a028>] audit_cb+0x68/0x3f0
[  507.170027]  [<ffffffff8136f088>] common_lsm_audit+0x1b8/0x740
[  507.239910]  [<ffffffff812285c0>] ? alloc_inode+0x50/0x90
[  507.304593]  [<ffffffff812265b6>] ? prepend_path+0xc6/0x2a0
[  507.371358]  [<ffffffff8138161f>] aa_audit+0x5f/0x170
[  507.431880]  [<ffffffff81399fb2>] audit_mount+0x152/0x160
[  507.496567]  [<ffffffff8139a67d>] match_mnt_path_str+0x1dd/0x490
[  507.568529]  [<ffffffff812278b8>] ? dentry_path+0x18/0x70
[  507.633213]  [<ffffffff8139aa0a>] match_mnt+0xda/0x150
[  507.694776]  [<ffffffff8139b280>] aa_bind_mount+0x100/0x180
[  507.761540]  [<ffffffff813903e0>] wrap_apparmor_sb_mount+0x1c0/0x270
[  507.837664]  [<ffffffff81345db7>] security_sb_mount+0x57/0x80
[  507.906506]  [<ffffffff8123029b>] do_mount+0xab/0xde0
[  507.967032]  [<ffffffff811efd74>] ? __kmalloc_track_caller+0x1b4/0x250
[  508.045236]  [<ffffffff810ef581>] ? hrtimer_try_to_cancel+0xd1/0x130
[  508.121361]  [<ffffffff811acc72>] ? memdup_user+0x42/0x70
[  508.186042]  [<ffffffff812312ff>] SyS_mount+0x9f/0x100
[  508.247607]  [<ffffffff81836072>] entry_SYSCALL_64_fastpath+0x16/0x71
[  508.324765] Code: 89 f8 48 89 e5 f6 82 a0 05 a5 81 20 74 10 48 83 c0 01 0f b6 10 f6 82 a0 05 a5 81 20 75 f0 5d c3 90 66 2e 0f 1f 84 00 00 00 00 00 <80> 3f 00 55 48 89 e5 74 11 48 89 f8 48 83 c0 01 80 38 00 75 f7 
[  508.564156] RIP  [<ffffffff813fe6c0>] strlen+0x0/0x20
[  508.624889]  RSP <ffff880061a73a20>
[  508.666696] CR2: fffffffffffffff3
[  508.706425] ---[ end trace 9a8196367a1a3630 ]---
```
