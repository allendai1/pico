
def main():
    import sys
    shouldRun = str(input('Run? (y/n): ')).lower()
    if shouldRun != 'y':
        sys.exit(1)
    del sys # make space in memory

    # read settings.json
    from lib.at_client import io_util
    ssid, password, atSign = io_util.read_settings()
    del io_util # make space in memory

    # connect to wifi
    from lib import wifi
    print('Connecting to WiFi %s...' % ssid)
    wifi.init_wlan(ssid, password)
    del ssid, password, wifi # make space in memory

    # connect and pkam authenticate into secondary
    from lib.at_client import at_client
    atClient = at_client.AtClient(atSign, writeKeys=True)
    atClient.pkam_authenticate(verbose=True)
    del at_client

    import time
    value = 0
    import random
    namespace = "group5"
    for i in range(100):
        time.sleep(3)
        num = random.randint(1,10)
        
        # emit the data
        time.sleep(2)
        data = atClient.put_public('test', str(num), namespace=namespace) # update:public:led@soccer0 0
        time.sleep(2)

        print('response: data:%s' %data)
        
if __name__ == '__main__':
    main()