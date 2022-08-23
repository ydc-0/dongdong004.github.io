# PVE

- Proxmox Virtual Environment:
  - https://www.proxmox.com/en/

## Create new VM

- login: https://xxxx:8006
- local -> ISO Images -> Upload / Dowload
- <Node> -> Create VM

### Create VM - Cloud Init

- Ref: https://pve.proxmox.com/wiki/Cloud-Init_Support
- open node shell
  - `wget http://cloud-images.ubuntu.com/releases/22.04/release-20220712/ubuntu-22.04-server-cloudimg-amd64.vmdk`
  - `qm importdisk 10001 ubuntu-22.04-server-cloudimg-amd64.vmdk local-zfs`
- VM hardware
  - Add disk
  - Add cloud-init
- VM Cloud Init
  - Set user, password, ssh-key, ipconfig
- Start VM

## Create CT

### Add USB devices to CT

- CT config: nesting=1, unprivileged
- Node Shell:
  - ```sh
    $ ls /dev/ttyUSB* -al
    crw-rw-rw- 1 root dialout 188, 0 Aug 23 19:35 /dev/ttyUSB0
    ```
- `/etc/pve/lxc/65902.conf`
  - ```sh
    ...
    lxc.cgroup2.devices.allow: c 188:* rwm
    lxc.mount.entry: /dev/ttyUSB1 dev/ttyUSB1 none bind,optional,create=file
    ```
- `/etc/udev/rules.d/49-usb-serial.rules`
  - ```sh
    KERNEL=="ttyUSB*", SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", OWNER="root", GROUP="dialout", MODE="0666"
    ```

