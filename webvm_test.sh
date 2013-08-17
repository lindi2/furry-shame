#!/bin/bash

websockify 2001 localhost:2000 > /dev/null 2> /dev/null < /dev/null &
websockify_pid=$!

SPICE_DEBUG_ALLOW_MC=1 kvm -drive file=debian_wheezy_amd64_desktop.qcow2,cache=none,index=0,if=virtio -snapshot -net nic,model=virtio -net user -m 2048 -cpu host -spice port=2000,password=w > /dev/null 2> /dev/null < /dev/null &
#SPICE_DEBUG_ALLOW_MC=1 kvm -drive file=digabi-livecd-v1.0.iso,cache=none,index=0,media=cdrom -snapshot -net nic -net user -m 2048 -cpu host -spice port=2000,password=w > /dev/null 2> /dev/null < /dev/null &
kvm_pid=$!

ssh -N -R2001:localhost:2001 nm.0xff.fi > /dev/null 2> /dev/null < /dev/null &
ssh_pid=$!

echo $websockify_pid
echo $kvm_pid
echo $ssh_pid