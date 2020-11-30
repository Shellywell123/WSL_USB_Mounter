import os

usb_drives     = ['D','E','F','G','H']
mounted_drives = []

for usb_drive in usb_drives:

    mount_dir  = usb_drive+'_USB'
    mount_point = '/media/'+mount_dir

    if not os.path.exists(mount_point):
        os.system('sudo mkdir {}'.format(mount_point))

    os_str = "sudo mount -t drvfs {}: {}".format(usb_drive.lower(),mount_point)

    try:
        os.system(os_str)
        mounted_drives.append(usb_drive)
    except:
        pass

print('mounted {} in /media'.format(mounted_drives))