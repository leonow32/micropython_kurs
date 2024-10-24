import os
import machine
import free_mem

def init():
    global sd
    sd = machine.SDCard(slot=3, width=1, cs=13, miso=2, mosi=15, sck=14, freq=20000000)
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/sd")    # znak / nie ma żadnego znaczenia i może być dowolny inny

def check_if_folder(path):
    atrib = os.stat(path)[0]
    if atrib & 0x4000:
        print(f"check_if_folder({path}) = True")
        return True
    else:
        print(f"check_if_folder({path}) = False")
        return False
    
def print_tree(path):
    print(f"print_tree({path})")
        
    items = os.listdir(path)
        
    #print(items)
    for item in items:
        is_folder = check_if_folder(path + item)
        print(f"{item} {is_folder}")
        
        if is_folder:
            print_tree(path + item + "/")
        
if __name__ == "__main__":
    free_mem.ram_free()
    init()
    print(os.listdir(""))
    print(os.listdir("sd"))
    #print(os.listdir("sd/katalog1"))
    #print(os.listdir("sd/katalog2"))
    #print_tree("/")
    free_mem.ram_free()
