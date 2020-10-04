import psutil


def get_memory_usage():
    memory = psutil.virtual_memory()
    # Divide from Bytes -> KB -> MB
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    # return str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'
    return 'Memory: ' + str(memory.percent) + '% '


def get_cpu_usage():
    return 'CPU: ' + str(psutil.cpu_percent()) + '% '


def get_disk_usage():
    disk = psutil.disk_usage('/')
    # Divide from Bytes -> KB -> MB -> GB
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    # return str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
    return 'Disk: ' + str(disk.percent) + '% '

def display_system_info(color,speed):

    # get readings
    memory = get_memory_usage()
    cpu = get_cpu_usage()
    disk = get_disk_usage()
    # build display string
    displayMessage = memory + cpu + disk
    # display information
    sense.show_message(displayMessage, text_colour=color, scroll_speed=speed)
