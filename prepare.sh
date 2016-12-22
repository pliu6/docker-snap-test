#!/bin/sh
iw dev vphy0.067d del
iw phy phy0 interface add vphy0.067d type __ap
ip link set dev vphy0.067d address 02:da:02:52:25:a5
ip addr flush dev vphy0.067d
ip addr add 192.168.128.1/255.255.255.0 dev vphy0.067d
ip link set dev vphy0.067d up

iptables --wait 5 --table filter --new zone_vphy0.067d_input
iptables --wait 5 --table filter --new zone_vphy0.067d_output
iptables --wait 5 --table filter --new zone_vphy0.067d_forward
iptables --wait 5 --table nat --new zone_vphy0.067d_prerouting
iptables --wait 5 --table nat --new zone_vphy0.067d_postrouting
iptables --wait 5 --table filter --append delegate_input --in-interface vphy0.067d --jump zone_vphy0.067d_input
iptables --wait 5 --table filter --append input_rule --in-interface vphy0.067d --match state --state ESTABLISHED,RELATED --match comment --comment zone  --jump ACCEPT
iptables --wait 5 --table filter --append input_rule --in-interface vphy0.067d --match comment --comment zone --jump REJECT
iptables --wait 5 --table filter --append delegate_output --out-interface vphy0.067d --jump zone_vphy0.067d_output
iptables --wait 5 --table filter --append output_rule --out-interface vphy0.067d --match comment --comment zone --jump ACCEPT
iptables --wait 5 --table filter --append delegate_forward --out-interface vphy0.067d --jump zone_vphy0.067d_forward
iptables --wait 5 --table filter --append forward_rule --out-interface vphy0.067d --match comment --comment zone --jump ACCEPT
iptables --wait 5 --table nat --append delegate_prerouting --in-interface vphy0.067d --jump zone_vphy0.067d_prerouting
iptables --wait 5 --table nat --append delegate_postrouting --out-interface vphy0.067d --jump zone_vphy0.067d_postrouting

