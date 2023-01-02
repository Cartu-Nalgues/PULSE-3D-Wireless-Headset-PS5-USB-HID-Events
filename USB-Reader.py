# -*- coding: utf-8 -*-
from msvcrt import kbhit
#O BIBLIOTECA SACRA
import pywinusb.hid as hid
import keyboard

def sample_handler(data):
    print("DATA RAW", data,"\n")

    if(data[0] == 176 and data[4] == 239 and data[5] == 89):
        print("CONNECTION")
        time.sleep(0.2)
    elif(data[0] == 176 and data[4] == 227 and data[5] == 91):
        print("DISCONNECTION")
    elif(data[0] == 176 and data[5] == 17):
        print("SOUND VOLUME UP")
    elif (data[0] == 176 and data[5] == 18):
        print("SOUND VOLUME DOWN")
    elif (data[0] == 176 and data[4] == 237 and data[5] == 21):
        print("MIC ACT")
    elif (data[0] == 176 and data[4] == 239 and data[5] == 21):
        print("MIC DEA")
    elif (data[0] == 176 and data[4] == 239 and data[5] == 19):
        print("INCREASE GAME SOUND VOLUME")
    elif (data[0] == 176 and data[4] == 239 and data[5] == 20):
        print("LOWER GAME SOUND VOLUME")


def raw_test():
    # simple test
    # browse devices...
    all_hids = hid.find_all_hid_devices()
    if all_hids:
        while True:
            print("Choose a device to monitor raw input reports:\n")
            print("0 => Exit")
            for index, device in enumerate(all_hids):
                device_name = unicode("{0.vendor_name} {0.product_name}" \
                        "(vID=0x{1:04x}, pID=0x{2:04x})"\
                        "".format(device, device.vendor_id, device.product_id))
                print("{0} => {1}".format(index+1, device_name))
            print("\n\tDevice ('0' to '%d', '0' to exit?) " \
                    "[press enter after number]:" % len(all_hids))
            index_option = raw_input()
            if index_option.isdigit() and int(index_option) <= len(all_hids):
                # invalid
                break;
        int_option = int(index_option)
        if int_option:
            device = all_hids[int_option-1]
            try:
                device.open()

                #set custom raw data handler
                device.set_raw_data_handler(sample_handler)

                print("\nWaiting for data...\nPress any (system keyboard) key to stop...")
                while not kbhit() and device.is_plugged():
                    #just keep the device opened to receive events
                    sleep(0.5)
                return
            finally:
                device.close()
    else:
        print("There's not any non system HID class device available")
#
if __name__ == '__main__':
    # first be kind with local encodings
    import sys
    if sys.version_info >= (3,):
        # as is, don't handle unicodes
        unicode = str
        raw_input = input
        print("input",input,"raw",raw_input)
    else:
        # allow to show encoded strings
        import codecs
        sys.stdout = codecs.getwriter('mbcs')(sys.stdout)
    raw_test()
