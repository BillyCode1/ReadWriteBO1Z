from ReadWriteMemory import ReadWriteMemory
import keyboard

rwm = ReadWriteMemory()
enableMod = "F1"
viewStats = "F2"
process = rwm.get_process_by_name("BlackOps.exe")
process.open()
##
cashAddr = process.get_pointer(0x01C0a6C8)
healthAddr = process.get_pointer(0x01A7987C)
wep1Addr = 0x01C08F10
wep2Addr = 0x01C08F00
grenadeAddr = 0x01C08F08
kills = 0x01C0A6CC
headshots = 0x01C0A6EC
userName = 0x01C0A678
##

print("Press F1 for All-in-One Mods (Godmode, Inf Ammo, Inf Cash")

def Mods():
  while 1:
      process.write(healthAddr, 2000000000), # Health
      process.write(cashAddr, 2000000000), # Cash
      process.write(wep1Addr, 1500), # Inf Ammo Gun.1
      process.write(wep2Addr, 1500), # Inf Ammo Gun.2
      process.write(GrenadeAddr, 10), # Inf Grenades
        
   ## Read Current Set Stats ##
# if keyboard.is_pressed("F2"):
#     Hvalue = process.read(healthAddr)
#     Cvalue = process.read(cashAddr)
#     print(f"Health: {Hvalue} \n Cash: {Cvalue}")
        
while True:
  if keyboard.is_pressed("F1"):
    print(f"Modded values have been set! \n enjoy ;)")
    Mods()
