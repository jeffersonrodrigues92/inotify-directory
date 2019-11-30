import inotify.adapters

def _main():
    
    notifier = inotify.adapters.Inotify()
    notifier.add_watch('/home/jefferson/inotify')   

    for event in notifier.event_gen():
        if event is not None:
            if 'IN_MOVED_TO' in event[1]:
                filename = event[3]
                with open('/home/jefferson/inotify/' + filename, 'rb') as data:
                    print(filename)

if __name__ == '__main__':
    _main()