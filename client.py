import customtkinter as ctk
from PIL import Image, ImageTk
import os
import threading
import datetime
import time
from bson.objectid import ObjectId
from pymongo import MongoClient, UpdateOne
import sys

is_touching = False

MaterMixDoorBlinking = False
GreenMaterMixDoor = False
RedMaterMixDoor = False
TbletHoprDoor0Blinking = False
GreenTbletHoprDoor0 = False
RedTbletHoprDoor0 = False
RedManBTbletHoprDoor0 = False
TbletHoprDoor1Blinking = False
GreenTbletHoprDoor1 = False
RedTbletHoprDoor1 = False
RedToRotaryCnvyr0 = False
GreenToRotaryCnvyr0 = False
RedToRotaryCnvyr1 = False
GreenToRotaryCnvyr1 = False
RedToRotaryCnvyr2 = False
GreenToRotaryCnvyr2 = False
RedToRotaryCnvyr3 = False
GreenToRotaryCnvyr3 = False
RedToRotaryCnvyr4 = False
GreenToRotaryCnvyr4 = False
GreenToHopperCnvyr0 = False
GreenToHopperCnvyr1 = False
GreenToHopperCnvyr2 = False
GreenToHopperCnvyr3 = False
MaterMixRotorBlinking = False
MateriVbratorBlinking = False
MatScrewCnvyrBlinking = False
RtaryUnitHop0Blinking = False
RtaryUnitHop1Blinking = False
RtaryUnitHop2Blinking = False
RtaryUnitHop3Blinking = False
RtaryUnitHop4Blinking = False
TabletVaryHop0Blinking = False
TabletVaryHop1Blinking = False
TabletVaryHop2Blinking = False
TabletVaryHop3Blinking = False
RncenMachHop0Blinking = False
RncenMachHop1Blinking = False
ToRotaryCnvyrBlinking = False
FrmRtaryCnvyrBlinking = False
TbletHoprDoorBlinking = False
UpLadderCnvyrBlinking = False
ToHopperCnvyrBlinking = False
ToRncenCnvyrBlinking = False
ManBTbletHoprDoor0Blinking = False
ManBTbletHoprDoor1Blinking = False
FrmBManRtaryCnvyrBlinking = False
FeederBPutihBlinking = False
FeederBWarna1Blinking = False
FeederBWarna2Blinking = False
FeederBWarna3Blinking = False
HopperBPutihBlinking = False
HopperBWarnaBlinking = False

# LINE C
GreenCManMaterMixDoor = False
RedCManMaterMixDoor = False
RedCManTbletHoprDoor0 = False
GreenCManTbletHoprDoor0 = False
RedCManTbletHoprDoor1 = False
GreenCManTbletHoprDoor1 = False
RedCManTbletHoprDoor2 = False
GreenCManTbletHoprDoor2 = False
RedCManTbletHoprDoor3 = False
GreenCManTbletHoprDoor3 = False
RedCManTbletHoprDoor4 = False
GreenCManTbletHoprDoor4 = False
CManMaterMixRotorBlinking =  False
CManMaterMixDoorBlinking =  False
CManMateriVbratorBlinking = False
CManMotorMatScrewCnvyrBlinking = False
CManMotorToRotaryCnvyrBlinking = False
CManMotorFrmRtaryCnvyrBlinking = False
CManMotorUpladderCnvyrBlinking = False
CManMotorToHopperCnvyrBlinking = False
CManPneumMaterMixDoorBlinking = False
CManPneumTbletHoprDoor0Blinking = False
CManPneumTbletHoprDoor1Blinking = False
CManPneumTbletHoprDoor2Blinking = False
CManPneumTbletHoprDoor3Blinking = False
CManPneumTbletHoprDoor4Blinking = False
CManRtaryUnitHop0Blinking = False
CManRtaryUnitHop1Blinking = False
CManRtaryUnitHop2Blinking = False
CManTabletVaryHop0Blinking = False
CManTabletVaryHop1Blinking = False
CManTabletVaryHop2Blinking = False
CManTabletVaryHop3Blinking = False
CManTabletVaryHop4Blinking = False
CManRncenMachHop0Blinking = False
CManRncenMachHop1Blinking = False
CManRncenMachHop2Blinking = False
CManRncenMachHop3Blinking = False
CManRncenMachHop4Blinking = False
FeederCPutihBlinking = False
FeederCWarna1Blinking = False
FeederCWarna2Blinking = False
FeederCWarna3Blinking = False
FeederCWarna4Blinking = False
HopperCPutihBlinking = False
HopperCWarna1Blinking = False
HopperCWarna2Blinking = False
HopperCWarna3Blinking = False
HopperCWarna4Blinking = False

# LINE Z
ZManPneumFeed3Door0Blinking = False
ZManPneumFeed3Door1Blinking = False
RedZManPneumFeed3Door = False
YellowZManPneumFeed3Door = False
GreenZManPneumFeed3Door = False
DumpMixerBBlinking = False
DumpMixerCBlinking = False
FillMixerBBlinking = False
FillMixerCBlinking = False

loopAllButtonFalse = True
idFalse = ""

holdbtnRedZManFeedThreeDoor = False
holdbtnYellowZManFeedThreeDoor = False
holdbtnGreenZManFeedThreeDoor = False
holdBManMaterMixRotorSwitch = False
holdRedBManMaterMixDoor = False
holdGreenBManMaterMixDoor = False
holdGreenBManToRotaryCnvyr0 = False
holdGreenBManToRotaryCnvyr1 = False
holdGreenBManToRotaryCnvyr2 = False
holdGreenBManToRotaryCnvyr3 = False
holdGreenBManToRotaryCnvyr4 = False
holdGreenBManToHopperCnvyr0 = False
holdGreenBManToHopperCnvyr1 = False
holdGreenBManToHopperCnvyr2 = False
holdGreenBManToHopperCnvyr3 = False
holdRedManBTbletHoprDoor0 = False
holdGreenManBTbletHoprDoor0 = False
holdRedManBTbletHoprDoor1 = False
holdGreenManBTbletHoprDoor1 = False
holdGreenBManToRncenCnvyr = False
holdRedCManMaterMixDoor = False
holdGreenCManMaterMixDoor = False
holdGreenCManToRotaryCnvyr0 = False
holdGreenCManToRotaryCnvyr1 = False
holdGreenCManToRotaryCnvyr2 = False
holdGreenCManToHopperCnvyr0 = False
holdGreenCManToHopperCnvyr1 = False
holdGreenCManToHopperCnvyr2 = False
holdGreenCManToHopperCnvyr3 = False
holdGreenCManToHopperCnvyr4 = False
holdRedManCTbletHoprDoor0 = False
holdGreenManCTbletHoprDoor0 = False
holdRedManCTbletHoprDoor1 = False
holdGreenManCTbletHoprDoor1 = False
holdRedManCTbletHoprDoor2 = False
holdGreenManCTbletHoprDoor2 = False
holdRedManCTbletHoprDoor3 = False
holdGreenManCTbletHoprDoor3 = False
holdRedManCTbletHoprDoor4 = False
holdGreenManCTbletHoprDoor4 = False


for i in range(100):
    globals()[f'I000{str(i).zfill(2)}'] = False
for i in range(100, 257):
    globals()[f'I00{str(i).zfill(3)}'] = False

for i in range(100):
    globals()[f'J000{str(i).zfill(2)}'] = False
for i in range(100, 578):
    globals()[f'J00{str(i).zfill(3)}'] = False

for i in range(100):
    globals()[f'V00{str(i).zfill(2)}'] = 0
for i in range(100, 60):
    globals()[f'V0{str(i).zfill(3)}'] = 0

globals()['V0144'] = 0
globals()['V0145'] = 0
globals()['V0146'] = 0
globals()['V0147'] = 0
globals()['V0148'] = 0
globals()['V0149'] = 0


hold_time = 100

client = MongoClient('mongodb://192.168.18.149:27017/')
# client = MongoClient('mongodb://localhost:27017/')

db_mongo = client['unitamaDB']
collection = db_mongo['napthalMachine']
objID = '68366b8cde0dc02539587580'

def unpack_inputs(packed_inputs: dict):
    # Unpack 8 bits per byte to Ixxxxx keys
    for j in range(16):
        qi_key = f"qi{str(j).zfill(4)}glovar"
        if qi_key not in packed_inputs.keys():
            continue
        qi_val = packed_inputs[qi_key]
        if not isinstance(qi_val, int):
            continue
        for bit_position in range(8):
            input_idx = j * 8 + bit_position
            old_val = globals().get(f'I{input_idx:05d}')
            bit_val = (qi_val >> bit_position) & 1

            if old_val != bool(bit_val):
                globals()[f'I{input_idx:05d}'] = bit_val == 1

def unpack_processes(packed_processes: dict):
    # Unpack 8 bits per byte to Jxxxxx keys
    for j in range(16, 72):
        qj_key = f"qj{str(j).zfill(4)}latchv"
        if qj_key not in packed_processes.keys():
            continue
        qj_val = packed_processes[qj_key]
        if not isinstance(qj_val, int):
            continue
        for bit_position in range(8):
            process_idx = j * 8 + bit_position
            old_val = globals().get(f'J{process_idx:05d}')
            bit_val = (qj_val >> bit_position) & 1

            if old_val != bool(bit_val):
                globals()[f'J{process_idx:05d}'] = bit_val == 1

def JQueue():
    return (
        [globals()[f"J{8 * group + offset:05d}"] for offset in range(8)]
        for group in range(16)
    )

previous_jqueues = [jqueue[:] for jqueue in JQueue()]

def processQueue():
    updated_queue = []
    updated_var_names = []

    for jqueue_index, current_jqueue in enumerate(JQueue()):
        prev_jqueue = previous_jqueues[jqueue_index]
        for bit_index, (prev_val, curr_val) in enumerate(zip(prev_jqueue, current_jqueue)):
            if prev_val != curr_val:
                updated_queue.append((jqueue_index, bit_index))

                global_index = 8 * jqueue_index + bit_index
                var_name = f"J{global_index:05d}"
                updated_var_names.append(var_name)

                previous_jqueues[jqueue_index][bit_index] = curr_val

    return updated_queue, updated_var_names

def updateProcess(updated_queue: list):
    if not updated_queue:
        return

    # Group changes by their queue index
    changed_groups = set()
    for group_idx, _ in updated_queue:
        changed_groups.add(group_idx)

    # Build dictionary of full byte values for changed groups
    packed_list = {}
    current_queues = list(JQueue())  # Get current state of all groups
    
    for group_idx in changed_groups:
        # Calculate the full byte value (0-255) for this group
        byte_value = 0
        for bit_idx, bit_val in enumerate(current_queues[group_idx]):
            if bit_val:
                byte_value |= (1 << bit_idx)  # Set bit if True
                
        # Key format: "qj{GROUP_NUMBER:04d}latchv" (GROUP_NUMBER = group_idx)
        qi_key = f"qj{group_idx:04d}latchv"
        packed_list[qi_key] = byte_value

    # Update database
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': packed_list}
    )
# -------------------------------------------
# START SET PAGES VARIABLES
# -------------------------------------------

# Set B
V0000 = 0
V0001 = 0
V0002 = 0
V0016 = 0
V0017 = 0
V0018 = 0
V0019 = 0
V0020 = 0
V0021 = 0
V0022 = 0
V0023 = 0
V0024 = 0
V0025 = 0
V0026 = 0

# Set C
V0032 = 0
V0033 = 0
V0034 = 0
V0035 = 0
V0036 = 0
V0037 = 0
V0048 = 0
V0049 = 0
V0050 = 0
V0051 = 0
V0052 = 0
V0053 = 0
V0054 = 0
V0055 = 0
V0056 = 0
V0057 = 0
V0058 = 0
V0059 = 0
V0060 = 0

# Set Z
V0064 = 0
V0065 = 0

V0011 = 10 # Timer B
V0043 = 11 # Timer C

timerBrunning = False
timerCrunning = False
startTimeB = None
startTimeC = None
elapsedTimeB = 0
elapsedTimeC = 0

custom_variables2 = {
    "V0000" : 0,
    "V0001" : 0,
    "V0002" : 0,
    "V0016" : 0,
    "V0017" : 0,
    "V0018" : 0,
    "V0019" : 0,
    "V0020" : 0,
    "V0021" : 0,
    "V0022" : 0,
    "V0023" : 0,
    "V0024" : 0,
    "V0025" : 0,
    "V0026" : 0,
    "V0032" : 0,
    "V0033" : 0,
    "V0034" : 0,
    "V0035" : 0,
    "V0036" : 0,
    "V0037" : 0,
    "V0048" : 0,
    "V0049" : 0,
    "V0050" : 0,
    "V0051" : 0,
    "V0052" : 0,
    "V0053" : 0,
    "V0054" : 0,
    "V0055" : 0,
    "V0056" : 0,
    "V0057" : 0,
    "V0058" : 0,
    "V0059" : 0,
    "V0060" : 0,
    "V0064" : 0,
    "V0065" : 0,
    "V0011" : 88,
    "V0043" : 99
}

custom_variables = {}

current_box_value = {"Box 1": 0, "Box 2": 0}
current_value = 0
current_box = None
previous_values = {}
# Dictionary untuk memetakan widget ke variabel
widget_variable_map = {}

document = collection.find_one({"_id": ObjectId(objID)})
if document:
    for i in range(578):
        # var_name = f'J{i:05}'
        # if var_name in document:
        #     # Setel nilai variabel global dengan nilai dari MongoDB
        #     globals()[var_name] = document[var_name]

        var_nameV = f'V{i:04}'
        if var_nameV in document:
            # Setel nilai variabel global dengan nilai dari MongoDB
            globals()[var_nameV] = document[var_nameV]
        
        var_nameI = f'I{i:05}'
        if var_nameI in document:
            # Setel nilai variabel global dengan nilai dari MongoDB
            globals()[var_nameI] = document[var_nameI]

    TARGET_QI_KEYS_0_TO_15 = {f"qi{str(j).zfill(4)}glovar" for j in range(16)}
    TARGET_QJ_KEYS_0_TO_71 = {f"qj{str(j).zfill(4)}latchv" for j in range(72)}

    if TARGET_QI_KEYS_0_TO_15 & document.keys():
        unpack_inputs(document)

    if TARGET_QJ_KEYS_0_TO_71 & document.keys():
        unpack_processes(document)

# time.sleep(1)


up_image = ctk.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'img', 'atas.png')), size=(70, 40))
down_image = ctk.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'img', 'bawah.png')), size=(70, 40))

# -------------------------------------------
# END SET PAGES VARIABLES
# -------------------------------------------

# ----------------------------------
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("1024x768")
app.resizable(width=False, height=False)
app.wm_attributes("-fullscreen",True)

# ------------------------------------------------------------------------------------------------------------------------
btnSize = 45
lampWidth = 75
lampHeight = 50
swicthImgWidth = 231  # Gambar asli 330
switchImgHeight = 105  # Gambar asli 150

btnRedGreenSize = 95

stateBtnFeederBPutih = "normal"
stateBtnFeederBWarna1 = "normal"
stateBtnFeederBWarna2 = "normal"
stateBtnFeederBWarna3 = "normal"
stateBtnHopperBPutih = "normal"
stateBtnHopperBWarna = "normal"

switchUp = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'atasN.png')).resize(
    (swicthImgWidth, switchImgHeight))
switchLeft = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'kiriN.png')).resize(
    (swicthImgWidth, switchImgHeight))
switchRight = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'kananN.png')).resize(
    (swicthImgWidth, switchImgHeight))

btnLeft = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'DoRev.png'))
btnRight = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'DoFwd.png'))
btnLeftTrans = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'DoRevTrans.png'))
btnRightTrans = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'DoFwdTrans.png'))


image_height = switchUp.height
image_width = switchUp.width

# ================================================================================
# TOUCH SCREEN FUNCTION - .touchscreen
# ================================================================================
def on_touch(event):
    global is_touching
    is_touching = True
    print("Layar sedang disentuh")

# ini fungsi untuk update status ketika sedang dilepas
def on_release(event):
    global is_touching
    is_touching = False
    print("Layar tidak disentuh")
    resetButton()

# Fungsi untuk mengecek status sentuhan (bisa dipanggil di manapun ketika mau cek statusnya)
def check_touch_status():
    if not is_touching:
        resetButton()
    app.after(200, check_touch_status) 

def resetButton():
    globals()['holdbtnRedZManFeedThreeDoor'] = False
    globals()['holdbtnYellowZManFeedThreeDoor'] = False
    globals()['holdbtnGreenZManFeedThreeDoor'] = False
    globals()['holdBManMaterMixRotorSwitch'] = False
    globals()['holdRedBManMaterMixDoor'] = False
    globals()['holdGreenBManMaterMixDoor'] = False
    globals()['holdGreenBManToRotaryCnvyr0'] = False
    globals()['holdGreenBManToRotaryCnvyr1'] = False
    globals()['holdGreenBManToRotaryCnvyr2'] = False
    globals()['holdGreenBManToRotaryCnvyr3'] = False
    globals()['holdGreenBManToRotaryCnvyr4'] = False
    globals()['holdGreenBManToHopperCnvyr0'] = False
    globals()['holdGreenBManToHopperCnvyr1'] = False
    globals()['holdGreenBManToHopperCnvyr2'] = False
    globals()['holdGreenBManToHopperCnvyr3'] = False
    globals()['holdRedManBTbletHoprDoor0'] = False
    globals()['holdGreenManBTbletHoprDoor0'] = False
    globals()['holdRedManBTbletHoprDoor1'] = False
    globals()['holdGreenManBTbletHoprDoor1'] = False
    globals()['holdGreenBManToRncenCnvyr'] = False
    globals()['holdRedCManMaterMixDoor'] = False
    globals()['holdGreenCManMaterMixDoor'] = False
    globals()['holdGreenCManToRotaryCnvyr0'] = False
    globals()['holdGreenCManToRotaryCnvyr1'] = False
    globals()['holdGreenCManToRotaryCnvyr2'] = False
    globals()['holdGreenCManToHopperCnvyr0'] = False
    globals()['holdGreenCManToHopperCnvyr1'] = False
    globals()['holdGreenCManToHopperCnvyr2'] = False
    globals()['holdGreenCManToHopperCnvyr3'] = False
    globals()['holdGreenCManToHopperCnvyr4'] = False
    globals()['holdRedManCTbletHoprDoor0'] = False
    globals()['holdGreenManCTbletHoprDoor0'] = False
    globals()['holdRedManCTbletHoprDoor1'] = False
    globals()['holdGreenManCTbletHoprDoor1'] = False
    globals()['holdRedManCTbletHoprDoor2'] = False
    globals()['holdGreenManCTbletHoprDoor2'] = False
    globals()['holdRedManCTbletHoprDoor3'] = False
    globals()['holdGreenManCTbletHoprDoor3'] = False
    globals()['holdRedManCTbletHoprDoor4'] = False
    globals()['holdGreenManCTbletHoprDoor4'] = False

    globals()['J00046'] = False
    globals()['J00047'] = False
    globals()['J00048'] = False
    globals()['J00057'] = False
    globals()['J00037'] = False
    globals()['J00058'] = False
    globals()['J00038'] = False
    # LINE B
    globals()['J00000'] = False
    globals()['J00001'] = False
    globals()['J00002'] = False
    globals()['J00003'] = False
    globals()['J00004'] = False
    globals()['J00016'] = False
    globals()['J00017'] = False
    globals()['J00005'] = False
    globals()['J00032'] = False
    globals()['J00033'] = False
    globals()['J00018'] = False
    globals()['J00031'] = False
    globals()['J00034'] = False
    globals()['J00006'] = False
    globals()['J00007'] = False
    globals()['J00008'] = False
    globals()['J00009'] = False
    globals()['J00010'] = False
    globals()['J00011'] = False
    globals()['J00012'] = False
    globals()['J00013'] = False
    globals()['J00014'] = False
    globals()['J00015'] = False
    globals()['J00019'] = False
    globals()['J00020'] = False
    globals()['J00021'] = False
    globals()['J00022'] = False
    globals()['J00023'] = False
    globals()['J00024'] = False
    globals()['J00025'] = False
    globals()['J00026'] = False
    globals()['J00027'] = False
    globals()['J00028'] = False
    globals()['J00029'] = False
    globals()['J00030'] = False
    globals()['J00035'] = False
    globals()['J00036'] = False
    # LINE C
    globals()['J00059'] = False
    globals()['J00060'] = False
    globals()['J00061'] = False
    globals()['J00062'] = False
    globals()['J00063'] = False
    globals()['J00065'] = False
    globals()['J00067'] = False
    globals()['J00069'] = False
    globals()['J00070'] = False
    globals()['J00071'] = False
    globals()['J00072'] = False
    globals()['J00073'] = False
    globals()['J00074'] = False
    globals()['J00075'] = False
    globals()['J00076'] = False
    globals()['J00077'] = False
    globals()['J00078'] = False
    globals()['J00079'] = False
    globals()['J00080'] = False
    globals()['J00081'] = False
    globals()['J00082'] = False
    globals()['J00083'] = False
    globals()['J00084'] = False
    globals()['J00085'] = False
    globals()['J00087'] = False
    globals()['J00089'] = False
    globals()['J00091'] = False
    globals()['J00093'] = False
    globals()['J00095'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         # LINE Z
    #         'J00046': False,
    #         'J00047': False,
    #         'J00048': False,
    #         'J00057': False,
    #         'J00037': False,
    #         'J00058': False,
    #         'J00038': False,
    #         # LINE B
    #         'J00000': False,
    #         'J00001': False,
    #         'J00002': False,
    #         'J00003': False,
    #         'J00004': False,
    #         'J00016': False,
    #         'J00017': False,
    #         'J00005': False,
    #         'J00032': False,
    #         'J00033': False,
    #         'J00018': False,
    #         'J00031': False,
    #         'J00034': False,
    #         'J00006': False,
    #         'J00007': False,
    #         'J00008': False,
    #         'J00009': False,
    #         'J00010': False,
    #         'J00011': False,
    #         'J00012': False,
    #         'J00013': False,
    #         'J00014': False,
    #         'J00015': False,
    #         'J00019': False,
    #         'J00020': False,
    #         'J00021': False,
    #         'J00022': False,
    #         'J00023': False,
    #         'J00024': False,
    #         'J00025': False,
    #         'J00026': False,
    #         'J00027': False,
    #         'J00028': False,
    #         'J00029': False,
    #         'J00030': False,
    #         'J00035': False,
    #         'J00036': False,
    #         # LINE C
    #         'J00059': False,
    #         'J00060': False,
    #         'J00061': False,
    #         'J00062': False,
    #         'J00063': False,
    #         'J00065': False,
    #         'J00067': False,
    #         'J00069': False,
    #         'J00070': False,
    #         'J00071': False,
    #         'J00072': False,
    #         'J00073': False,
    #         'J00074': False,
    #         'J00075': False,
    #         'J00076': False,
    #         'J00077': False,
    #         'J00078': False,
    #         'J00079': False,
    #         'J00080': False,
    #         'J00081': False,
    #         'J00082': False,
    #         'J00083': False,
    #         'J00084': False,
    #         'J00085': False,
    #         'J00087': False,
    #         'J00089': False,
    #         'J00091': False,
    #         'J00093': False,
    #         'J00095': False
    #     }})
# ================================================================================
# END TOUCH SCREEN FUNCTION
# ================================================================================

# ================================================================================
# GENERAL FUNCTION - .gfunc
# ================================================================================
def keluarProgram():
    sys.exit()

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def resetAll():
    global loopAllButtonFalse
    loopAllButtonFalse = True

# .nav
def showCommonMan():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0149': 0
        }})
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualBesar1.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualCommon.pack(fill="both", expand=True)

def showCommonManwithReset():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0149': 0
        }})
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualBesar1.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualCommon.pack(fill="both", expand=True)

def showCommonMan2():
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualBesar1.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabManualCommon2.pack(fill="both", expand=True)
    
def showCommonAuto():
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualBesar1.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabCommonZAuto.pack(fill="both", expand=True)

def showCommonAuto2():
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualBesar1.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabCommonZAuto2.pack(fill="both", expand=True)

def showBesarA():
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualBesar1.pack(fill="both", expand=True)

def showBesarB():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualBesar2.pack(fill="both", expand=True)

def showBesarC():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualBesar3.pack(fill="both", expand=True)

def showBolaA():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualBola1.pack(fill="both", expand=True)

def showBolaB():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualBola2.pack(fill="both", expand=True)

def showBolaC():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabManualBola3.pack(fill="both", expand=True)

def showAutoBesarB1():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabBesarBAuto.pack(fill="both", expand=True)

def showAutoBesarB2():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabAutoLineB22.pack(fill="both", expand=True)

def showAutoBesarC1():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabBesarCAuto.pack(fill="both", expand=True)

def showAutoBesarC2():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_tabAutoLineC22.pack(fill="both", expand=True)

def showAutoSetZ():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_SetAutoZ.pack(fill="both", expand=True)

def showAutoSetB():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoC.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_SetAutoB.pack(fill="both", expand=True)

def showAutoSetC():
    frame_tabManualBesar1.pack_forget()
    frame_tabManualBesar2.pack_forget()
    frame_tabManualBesar3.pack_forget()
    frame_tabManualBola1.pack_forget()
    frame_tabManualBola2.pack_forget()
    frame_tabManualBola3.pack_forget()
    frame_tabAutoLineB22.pack_forget()
    frame_tabAutoLineC22.pack_forget()
    frame_tabBesarCAuto.pack_forget()
    frame_tabBesarBAuto.pack_forget()
    frame_tabManualCommon.pack_forget()
    frame_tabCommonZAuto.pack_forget()
    # frame_tabAutoLineZ.pack_forget()
    frame_SetAutoB.pack_forget()
    frame_SetAutoZ.pack_forget()
    frame_tabCommonZAuto2.pack_forget()
    frame_tabManualCommon2.pack_forget()
    frame_SetAutoC.pack(fill="both", expand=True)

def listenMongo():
    pipeline = [{'$match': {'documentKey._id': ObjectId(objID)}}]
    updated_queue = []
    with collection.watch(pipeline) as stream:
        print("Listening for changes...")

        for change in stream:

            if change['operationType'] == 'update':
                try:
                    updated_fields = change['updateDescription']['updatedFields']
                    print(f"updated_fields = {updated_fields}")

                    TARGET_QI_KEYS_0_TO_15 = {f"qi{str(j).zfill(4)}glovar" for j in range(16)}

                    TARGET_QJ_KEYS_0_TO_71 = {f"qj{str(j).zfill(4)}latchv" for j in range(72)}

                    for key, value in updated_fields.items():
                        if key not in TARGET_QI_KEYS_0_TO_15 and key not in TARGET_QJ_KEYS_0_TO_71:
                            if key in globals():
                                globals()[key] = value
                            else:
                                print(f"Warning: {key} not found in globals.")

                    if TARGET_QI_KEYS_0_TO_15 & updated_fields.keys():
                        unpack_inputs(updated_fields)

                    if TARGET_QJ_KEYS_0_TO_71 & updated_fields.keys():
                        unpack_processes(updated_fields)
                except KeyError as e:
                    print(f"Error accessing updated fields: {e}")

def refreshGUI():
    global MaterMixDoorBlinking, GreenMaterMixDoor, RedMaterMixDoor, TbletHoprDoor0Blinking, GreenTbletHoprDoor0, RedTbletHoprDoor0, TbletHoprDoor1Blinking, GreenTbletHoprDoor1, RedTbletHoprDoor1
    global MaterMixRotorBlinking, MatScrewCnvyrBlinking, RtaryUnitHop0Blinking, RtaryUnitHop1Blinking, RtaryUnitHop2Blinking, RtaryUnitHop3Blinking, RtaryUnitHop4Blinking, FrmRtaryCnvyrBlinking
    global TabletVaryHop0Blinking, TabletVaryHop1Blinking, TabletVaryHop2Blinking, TabletVaryHop3Blinking, RncenMachHop0Blinking, RncenMachHop1Blinking, MateriVbratorBlinking, ToRotaryCnvyrBlinking
    global TbletHoprDoorBlinking, UpLadderCnvyrBlinking, ToHopperCnvyrBlinking, ToRncenCnvyrBlinking, ManBTbletHoprDoor0Blinking, ManBTbletHoprDoor1Blinking, FrmBManRtaryCnvyrBlinking
    global GreenToRotaryCnvyr0, RedToRotaryCnvyr0, GreenToRotaryCnvyr1, RedToRotaryCnvyr1, GreenToRotaryCnvyr2, RedToRotaryCnvyr2, GreenToRotaryCnvyr3, RedToRotaryCnvyr3, GreenToRotaryCnvyr4, RedToRotaryCnvyr4
    global GreenToHopperCnvyr0, GreenToHopperCnvyr1, GreenToHopperCnvyr2, GreenToHopperCnvyr3, RedManBTbletHoprDoor0, RedManCTbletHoprDoor0, GreenManCTbletHoprDoor0, GreenCManMaterMixDoor, RedCManMaterMixDoor
    global J00262, J00263, J00264, J00265, J00266, J00267, J00268, J00269, J00270, J00271, J00275, J00276, J00277, J00278, J00279, J00280, J00281, J00282, J00291, J00292, loopAllButtonFalse
    global V0148, V0144, V0140, V0145, V0141
    global stateBtnFeederBPutih, stateBtnFeederBWarna1, stateBtnFeederBWarna2, stateBtnFeederBWarna3, stateBtnHopperBPutih, stateBtnHopperBWarna
    global J00128, J00129, J00130, J00131, J00132, J00133, J00135, J00136, J00137, J00138, J00139, J00140, J00141, J00142, J00143, J00144, J00145, J00260, J00263, J00265, J00265, J00267, J00272, J00273
    global J00274, J00276, J00278, J00280, J00282, J00287, J00288, J00289, J00290, J00292, J00357, J00369, J00512, J00513, J00514, J00515, J00517, J00518, J00519, J00520, J00521, J00522, J00523

    # print('start refresh')
    lightOrange_rgb = (247, 223, 192)  # RGB untuk oranye
    lightOrange = rgb_to_hex(lightOrange_rgb)

    updated_queue, _ = processQueue()
    updateProcess(updated_queue)

# LINE COMMON
    # DumpMixerB
    if globals()['J00245'] and not globals()['J00244'] :
        btnDumpB.configure(fg_color="red", text_color="black", state="normal")
    elif not globals()['J00244'] and not globals()['J00245']:
        btnDumpB.configure(fg_color="pink", text_color="white", state="normal")
    elif globals()['J00244']:
        if globals()['DumpMixerBBlinking']:
            btnDumpB.configure(fg_color="Red", text_color="black", state="normal")
        else:
            btnDumpB.configure(fg_color="pink", text_color="white", state="normal")
        globals()['DumpMixerBBlinking'] = not globals()['DumpMixerBBlinking']
    
    # DumpMixerC
    if globals()['J00251'] and not globals()['J00250'] :
        btnDumpC.configure(fg_color="red", text_color="black", state="normal")
    elif not globals()['J00250'] and not globals()['J00251']:
        btnDumpC.configure(fg_color="pink", text_color="white", state="normal")
    elif globals()['J00250']:
        if globals()['DumpMixerCBlinking']:
            btnDumpC.configure(fg_color="Red", text_color="black", state="normal")
        else:
            btnDumpC.configure(fg_color="pink", text_color="white", state="normal")
        globals()['DumpMixerCBlinking'] = not globals()['DumpMixerCBlinking']

    # FillMixerB
    if not bool(globals()['J00243'] or globals()['I00144']) and bool(bool(globals()['V0149']) and not globals()['J00245']):
        btnFillB.configure(fg_color="lime", text_color="black", state="normal")
    elif not (bool(globals()['V0149']) and not globals()['J00245']):
        btnFillB.configure(fg_color="light green", text_color="white", state="normal")
    elif bool(globals()['J00243'] or globals()['I00144']) and bool(bool(globals()['V0149']) and not globals()['J00245']):
        if globals()['FillMixerBBlinking']:
            btnFillB.configure(fg_color="lime", text_color="black", state="normal")
        else:
            btnFillB.configure(fg_color="light green", text_color="white", state="normal")
        globals()['FillMixerBBlinking'] = not globals()['FillMixerBBlinking']

    # FillMixerC
    if not bool(globals()['J00249'] or globals()['I00208']) and bool(bool(globals()['V0149']) and not globals()['J00251']):
        btnFillC.configure(fg_color="lime", text_color="black", state="normal")
    elif not (bool(globals()['V0149']) and not globals()['J00251']):
        btnFillC.configure(fg_color="light green", text_color="white", state="normal")
    elif bool(globals()['J00249'] or globals()['I00208']) and bool(bool(globals()['V0149']) and not globals()['J00251']):
        if globals()['FillMixerCBlinking']:
            btnFillC.configure(fg_color="lime", text_color="black", state="normal")
        else:
            btnFillC.configure(fg_color="light green", text_color="white", state="normal")
        globals()['FillMixerCBlinking'] = not globals()['FillMixerCBlinking']

    # FaultDoorZ0
    if not globals()['J00558'] and globals()['J00526']:
        frmZManFeedThreeDoor0Lbl.configure(fg_color="orange")
        btnZAutoPneumFeedThreeDoorIsFault0.configure(fg_color="orange", text_color="black")
    elif globals()['J00558'] and globals()['J00526']:
        if globals()['ZManPneumFeed3Door0Blinking']:
            frmZManFeedThreeDoor0Lbl.configure(fg_color="orange")
            btnZAutoPneumFeedThreeDoorIsFault0.configure(fg_color="orange", text_color="black")
        else:
            frmZManFeedThreeDoor0Lbl.configure(fg_color=lightOrange)
            btnZAutoPneumFeedThreeDoorIsFault0.configure(fg_color=lightOrange, text_color="white")
        globals()['ZManPneumFeed3Door0Blinking'] = not globals()['ZManPneumFeed3Door0Blinking']
    else:
        frmZManFeedThreeDoor0Lbl.configure(fg_color=lightOrange)
        btnZAutoPneumFeedThreeDoorIsFault0.configure(fg_color=lightOrange, text_color="white")

    # FaultDoorZ1
    if not globals()['J00559'] and globals()['J00527']:
        frmZManFeedThreeDoor1Lbl.configure(fg_color="orange")
        btnZAutoPneumFeedThreeDoorIsFault1.configure(fg_color="orange", text_color="black")
    elif globals()['J00559'] and globals()['J00527']:
        if globals()['ZManPneumFeed3Door1Blinking']:
            frmZManFeedThreeDoor1Lbl.configure(fg_color="orange")
            btnZAutoPneumFeedThreeDoorIsFault1.configure(fg_color="orange", text_color="black")
        else:
            frmZManFeedThreeDoor1Lbl.configure(fg_color=lightOrange)
            btnZAutoPneumFeedThreeDoorIsFault1.configure(fg_color=lightOrange, text_color="white")
        globals()['ZManPneumFeed3Door1Blinking'] = not globals()['ZManPneumFeed3Door1Blinking']
    else:
        frmZManFeedThreeDoor1Lbl.configure(fg_color=lightOrange)
        btnZAutoPneumFeedThreeDoorIsFault1.configure(fg_color=lightOrange, text_color="white")

    if globals()['J00176']:
        btnYellowZManFeedThreeDoor.configure(fg_color="yellow")
        btnZAutoPneumFeedThreeDoorIsLineA.configure(fg_color="yellow", text_color="black")
    elif not globals()['J00176'] and not globals()['J00302']:
        btnYellowZManFeedThreeDoor.configure(fg_color="light yellow")
        btnZAutoPneumFeedThreeDoorIsLineA.configure(fg_color="light yellow", text_color="white")
    elif not globals()['J00176'] and globals()['J00302']:
        if globals()['YellowZManPneumFeed3Door']:
            btnYellowZManFeedThreeDoor.configure(fg_color="yellow")
            btnZAutoPneumFeedThreeDoorIsLineA.configure(fg_color="yellow", text_color="black")
        else:
            btnYellowZManFeedThreeDoor.configure(fg_color="light yellow")
            btnZAutoPneumFeedThreeDoorIsLineA.configure(fg_color="light yellow", text_color="white")
        globals()['YellowZManPneumFeed3Door'] = not globals()['YellowZManPneumFeed3Door']
    
    if globals()['J00175']:
        btnRedZManFeedThreeDoor.configure(fg_color="red")
        btnZAutoPneumFeedThreeDoorIsLineB.configure(fg_color="red", text_color="black")
    elif not globals()['J00175'] and not globals()['J00304']:
        btnRedZManFeedThreeDoor.configure(fg_color="pink")
        btnZAutoPneumFeedThreeDoorIsLineB.configure(fg_color="pink", text_color="white")
    elif not globals()['J00175'] and globals()['J00304']:
        if globals()['RedZManPneumFeed3Door']:
            btnRedZManFeedThreeDoor.configure(fg_color="red")
            btnZAutoPneumFeedThreeDoorIsLineB.configure(fg_color="red", text_color="black")
        else:
            btnRedZManFeedThreeDoor.configure(fg_color="pink")
            btnZAutoPneumFeedThreeDoorIsLineB.configure(fg_color="pink", text_color="white")
        globals()['RedZManPneumFeed3Door'] = not globals()['RedZManPneumFeed3Door']
    
    if globals()['J00174']:
        btnGreenZManFeedThreeDoor.configure(fg_color="lime")
        btnZAutoPneumFeedThreeDoorIsLineC.configure(fg_color="lime", text_color="black")
    elif not globals()['J00174'] and not globals()['J00303']:
        btnGreenZManFeedThreeDoor.configure(fg_color="light green")
        btnZAutoPneumFeedThreeDoorIsLineC.configure(fg_color="light green", text_color="white")
    elif not globals()['J00174'] and globals()['J00303']:
        if globals()['RedZManPneumFeed3Door']:
            btnGreenZManFeedThreeDoor.configure(fg_color="lime")
            btnZAutoPneumFeedThreeDoorIsLineC.configure(fg_color="lime", text_color="black")
        else:
            btnGreenZManFeedThreeDoor.configure(fg_color="light green")
            btnZAutoPneumFeedThreeDoorIsLineC.configure(fg_color="light green", text_color="white")
        globals()['RedZManPneumFeed3Door'] = not globals()['RedZManPneumFeed3Door']
   
    # btnPneumFeedDoor Auto Common Page 2
    if not globals()['J00558'] and globals()['J00526']:
        btnPneumFeedDoor.configure(fg_color="orange", text="Fault 0")
    elif globals()['J00558'] and globals()['J00526']:
        if globals()['ZManPneumFeed3Door0Blinking']:
            btnPneumFeedDoor.configure(fg_color="orange", text="Fault 0")
        else:
            btnPneumFeedDoor.configure(fg_color=lightOrange, text="Fault 0")
    elif not globals()['J00559'] and globals()['J00527']:
        btnPneumFeedDoor.configure(fg_color="orange", text="Fault 1")
    elif globals()['J00559'] and globals()['J00527']:
        if globals()['ZManPneumFeed3Door1Blinking']:
            btnPneumFeedDoor.configure(fg_color="orange", text="Fault 1")
        else:
            btnPneumFeedDoor.configure(fg_color=lightOrange, text="Fault 1")
    elif globals()['J00176']:
        btnPneumFeedDoor.configure(fg_color="yellow", text="Line A", text_color="black")
    elif not globals()['J00176'] and globals()['J00302']:
        if globals()['YellowZManPneumFeed3Door']:
            btnPneumFeedDoor.configure(fg_color="yellow", text="Line A", text_color="black")
        else:
            btnPneumFeedDoor.configure(fg_color="light yellow", text="Line A", text_color="white")
    elif globals()['J00175']:
        btnPneumFeedDoor.configure(fg_color="red", text="Line B", text_color="black")
    elif not globals()['J00175'] and globals()['J00304']:
        if globals()['RedZManPneumFeed3Door']:
            btnPneumFeedDoor.configure(fg_color="red", text="Line B", text_color="black")
        else:
            btnPneumFeedDoor.configure(fg_color="pink", text="Line B", text_color="white")
    elif globals()['J00174']:
        btnPneumFeedDoor.configure(fg_color="lime", text="Line C", text_color="black")
    elif not globals()['J00174'] and globals()['J00303']:
        if globals()['RedZManPneumFeed3Door']:
            btnPneumFeedDoor.configure(fg_color="lime", text="Line C", text_color="black")
        else:
            btnPneumFeedDoor.configure(fg_color="light green", text="Line C", text_color="white")
    else:
        btnPneumFeedDoor.configure(fg_color=lightOrange, text="Fault 2", text_color="white")


# .TIMERB MIXING B
    if globals()['I00144'] and bool(globals()['V0149']) and not globals()['timerBrunning']:
        lbl_Num.configure(text=f"00.00")
        lbl_NumMixingB.configure(text=f"00.00")
        globals()['startTimeB'] = time.time()
        globals()['timerBrunning'] = True
        
    if not bool(globals()['V0149']) or globals()['J00243']:
        globals()['timerBrunning'] = False
        globals()['startTimeB'] = 0
        globals()['elapsedTimeB'] = 0
        

    if globals()['timerBrunning'] and globals()['elapsedTimeB'] <= globals()['V0011']:
        globals()['elapsedTimeB'] = time.time() - globals()['startTimeB']
        seconds = int(globals()['elapsedTimeB'])
        milliseconds = int((globals()['elapsedTimeB'] - seconds) * 100)
        lbl_NumMixingB.configure(text=f"{seconds:02}.{milliseconds:02}")
        lbl_Num.configure(text=f"{seconds:02}.{milliseconds:02}")
    else:
        globals()['timerBrunning'] = False
        globals()['startTimeB'] = 0
        globals()['elapsedTimeB'] = 0

# TIMER MIXING C
    if globals()['I00208'] and bool(globals()['V0149']) and not globals()['timerCrunning']:
        lbl_NumC.configure(text=f"00.00")
        lbl_NumMixingC.configure(text=f"00.00")
        globals()['startTimeC'] = time.time()
        globals()['timerCrunning'] = True
        
    if not bool(globals()['V0149']) or globals()['J00249']:
        globals()['timerCrunning'] = False
        globals()['startTimeC'] = 0
        globals()['elapsedTimeC'] = 0

    if globals()['timerCrunning'] and globals()['elapsedTimeC'] <= globals()['V0043']:
        globals()['elapsedTimeC'] = time.time() - globals()['startTimeC']
        seconds = int(globals()['elapsedTimeC'])
        milliseconds = int((globals()['elapsedTimeC'] - seconds) * 100)
        lbl_NumMixingC.configure(text=f"{seconds:02}.{milliseconds:02}")
        lbl_NumC.configure(text=f"{seconds:02}.{milliseconds:02}")
    else:
        globals()['timerCrunning'] = False
        globals()['startTimeC'] = 0
        globals()['elapsedTimeC'] = 0

# LINE B
    # BUTTON FEEDER B
    # Putih
    if ((globals()['V0148'] & 32768) != 32768) and globals()['V0144'] != 32768:
        btnAutoFeedPutih.configure(fg_color="light green", text_color="white", state="normal")
    elif ((globals()['V0148'] & 32768) == 32768) and globals()['V0140'] != 32768 and globals()['V0144'] != 32768:
        btnAutoFeedPutih.configure(fg_color="lime", text_color="black", state="normal")
    elif ((globals()['V0148'] & 32768) == 32768) and globals()['V0140'] == 32768 and globals()['V0144'] != 32768:
        # print("BUTTON FEEDER B", globals()['V0148'], globals()['V0140'], globals()['V0144'])
        if globals()['FeederBPutihBlinking']:
            btnAutoFeedPutih.configure(fg_color="light green", text_color="white", state="normal")
        else:
            btnAutoFeedPutih.configure(fg_color="lime", text_color="black", state="normal")
        globals()['FeederBPutihBlinking'] = not globals()['FeederBPutihBlinking']
    elif globals()['V0144'] == 32768:
        btnAutoFeedPutih.configure(fg_color="lime", text_color="black", state="normal")
    
    # Warna1
    if ((globals()['V0148'] & 16384) != 16384) and globals()['V0144'] != 16384:
        btnAutoFeedWarna1.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 16384) == 16384) and globals()['V0140'] != 16384 and globals()['V0144'] != 16384:
        btnAutoFeedWarna1.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 16384) == 16384) and globals()['V0140'] == 16384 and globals()['V0144'] != 16384:
        if globals()['FeederBWarna1Blinking']:
            btnAutoFeedWarna1.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna1.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederBWarna1Blinking'] = not globals()['FeederBWarna1Blinking']
    elif globals()['V0144'] == 16384:
        btnAutoFeedWarna1.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna2
    if ((globals()['V0148'] & 8192) != 8192) and globals()['V0144'] != 8192:
        btnAutoFeedWarna2.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 8192) == 8192) and globals()['V0140'] != 8192 and globals()['V0144'] != 8192:
        btnAutoFeedWarna2.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 8192) == 8192) and globals()['V0140'] == 8192 and globals()['V0144'] != 8192:
        if globals()['FeederBWarna2Blinking']:
            btnAutoFeedWarna2.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna2.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederBWarna2Blinking'] = not globals()['FeederBWarna2Blinking']
    elif globals()['V0144'] == 8192:
        btnAutoFeedWarna2.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna3
    if ((globals()['V0148'] & 4096) != 4096) and globals()['V0144'] != 4096:
        btnAutoFeedWarna3.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 4096) == 4096) and globals()['V0140'] != 4096 and globals()['V0144'] != 4096:
        btnAutoFeedWarna3.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 4096) == 4096) and globals()['V0140'] == 4096 and globals()['V0144'] != 4096:
        if globals()['FeederBWarna3Blinking']:
            btnAutoFeedWarna3.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna3.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederBWarna3Blinking'] = not globals()['FeederBWarna3Blinking']
    elif globals()['V0144'] == 4096:
        btnAutoFeedWarna3.configure(fg_color="red", text_color="black", state="normal")
    
    # Hopper Putih
    if ((globals()['V0148'] & 2048) != 2048) and globals()['V0145'] != 2048:
        btnAutoHopperPutih.configure(fg_color="light green", text_color="white", state="normal")
    elif ((globals()['V0148'] & 2048) == 2048) and globals()['V0141'] != 2048 and globals()['V0145'] != 2048:
        btnAutoHopperPutih.configure(fg_color="lime", text_color="black", state="normal")
    elif ((globals()['V0148'] & 2048) == 2048) and globals()['V0141'] == 2048 and globals()['V0145'] != 2048:
        # print("Hopper Putih", globals()['V0148'], globals()['V0141'], globals()['V0145'])
        if globals()['HopperBPutihBlinking']:
            btnAutoHopperPutih.configure(fg_color="light green", text_color="white", state="normal")
        else:
            btnAutoHopperPutih.configure(fg_color="lime", text_color="black", state="normal")
        globals()['HopperBPutihBlinking'] = not globals()['HopperBPutihBlinking']
    elif globals()['V0145'] == 2048:
        btnAutoHopperPutih.configure(fg_color="lime", text_color="black", state="normal")
    
    # Hopper Warna
    if ((globals()['V0148'] & 1024) != 1024) and globals()['V0145'] != 1024:
        btnAutoHopperWarna1.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 1024) == 1024) and globals()['V0141'] != 1024 and globals()['V0145'] != 1024:
        btnAutoHopperWarna1.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 1024) == 1024) and globals()['V0141'] == 1024 and globals()['V0145'] != 1024:
        if globals()['HopperBWarnaBlinking']:
            btnAutoHopperWarna1.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoHopperWarna1.configure(fg_color="red", text_color="black", state="normal")
        globals()['HopperBWarnaBlinking'] = not globals()['HopperBWarnaBlinking']
    elif globals()['V0145'] == 1024:
        btnAutoHopperWarna1.configure(fg_color="red", text_color="black", state="normal")

    mode = MaterialModeSelectorFeederB()

    if mode.putih():
        globals()['V0144'] = 32768
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0144': globals()['V0144']
            }})
    elif mode.warna1():
        globals()['V0144'] = 16384
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0144': globals()['V0144']
            }})
    elif mode.warna2():
        globals()['V0144'] = 8192
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0144': globals()['V0144']
            }})
    elif mode.warna3():
        globals()['V0144'] = 4096
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0144': globals()['V0144']
            }})
    elif mode.reset():
        globals()['V0144'] = 0
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0144': globals()['V0144']
            }})


    mode = ProductModeSelectorHopperB()

    if mode.putih():
        globals()['V0145'] = 2048
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0145': globals()['V0145']
            }})

    elif mode.warna():
        globals()['V0145'] = 1024
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0145': globals()['V0145']
            }})
    elif mode.reset():
        globals()['V0145'] = 0
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0145': globals()['V0145']
            }})


    # ERROR
    if not globals()['J00544'] and globals()['J00512']:
        frmBManMaterMixDoorLbl.configure(fg_color="orange")
        btnBAutoPneumMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00544'] and globals()['J00512']:
        if MaterMixDoorBlinking:
            frmBManMaterMixDoorLbl.configure(fg_color="orange")
            btnBAutoPneumMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManMaterMixDoorLbl.configure(fg_color=lightOrange)
            btnBAutoPneumMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
        MaterMixDoorBlinking = not MaterMixDoorBlinking
    else:
        frmBManMaterMixDoorLbl.configure(fg_color=lightOrange)
        btnBAutoPneumMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
    # ANIMASI BUTTON
    if globals()['I00001']:
        btnRedBManMaterMixDoor.configure(fg_color="Red")
        btnBAutoPneumMaterMixDoorIsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00001'] and not globals()['I00128']:
        btnRedBManMaterMixDoor.configure(fg_color="pink")
        btnBAutoPneumMaterMixDoorIsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00001'] and globals()['I00128']:
        if RedMaterMixDoor:
            btnRedBManMaterMixDoor.configure(fg_color="Red")
            btnBAutoPneumMaterMixDoorIsOpen.configure(fg_color="Red", text_color="black")
        else:
            btnRedBManMaterMixDoor.configure(fg_color="pink")
            btnBAutoPneumMaterMixDoorIsOpen.configure(fg_color="pink", text_color="white")
        RedMaterMixDoor = not RedMaterMixDoor

    if globals()['I00002']:
        btnGreenBManMaterMixDoor.configure(fg_color="lime")
        btnBAutoPneumMaterMixDoorIsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00002'] and not globals()['I00129']:
        btnGreenBManMaterMixDoor.configure(fg_color="light green")
        btnBAutoPneumMaterMixDoorIsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00002'] and globals()['I00129']:
        if GreenMaterMixDoor:
            btnGreenBManMaterMixDoor.configure(fg_color="lime")
            btnBAutoPneumMaterMixDoorIsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenBManMaterMixDoor.configure(fg_color="light green")
            btnBAutoPneumMaterMixDoorIsClose.configure(fg_color="light green", text_color="white")
        GreenMaterMixDoor = not GreenMaterMixDoor

    # btnMatermix Auto Common Page 2
    if not globals()['J00544'] and globals()['J00512']:
        btnMatermix.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00544'] and globals()['J00512']:
        if MaterMixDoorBlinking:
            btnMatermix.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMatermix.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00001']:
        btnMatermix.configure(text="Open",fg_color="Red", text_color="black")
    elif not globals()['I00001'] and globals()['I00128']:
        if RedMaterMixDoor:
            btnMatermix.configure(text="Open",fg_color="Red", text_color="black")
        else:
            btnMatermix.configure(text="Open",fg_color="pink", text_color="white")
    elif globals()['I00002']:
        btnMatermix.configure(text="Close",fg_color="lime", text_color="black")
    elif not globals()['I00002'] and globals()['I00129']:
        if GreenMaterMixDoor:
            btnMatermix.configure(text="Close",fg_color="lime", text_color="black")
        else:
            btnMatermix.configure(text="Close",fg_color="light green", text_color="white")
    else:
        btnMatermix.configure(fg_color=lightOrange, text="Fault", text_color="white")
    


    # ERROR
    if not globals()['J00545'] and globals()['J00513']:
        frmManBTbletHoprDoor0Lbl.configure(fg_color="orange")
        btnBAutoPneumTbletHoprDoor0IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00545'] and globals()['J00513']:
        if ManBTbletHoprDoor0Blinking:
            frmManBTbletHoprDoor0Lbl.configure(fg_color="orange")
            btnBAutoPneumTbletHoprDoor0IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManBTbletHoprDoor0Lbl.configure(fg_color=lightOrange)
            btnBAutoPneumTbletHoprDoor0IsFault.configure(fg_color=lightOrange, text_color="white")
        ManBTbletHoprDoor0Blinking = not ManBTbletHoprDoor0Blinking
    else:
        frmManBTbletHoprDoor0Lbl.configure(fg_color=lightOrange)
        btnBAutoPneumTbletHoprDoor0IsFault.configure(fg_color=lightOrange, text_color="white")
    # ANIMASI BUTTON
    if globals()['I00020']:
        btnRedManBTbletHoprDoor0.configure(fg_color="Red")
        btnBAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00020'] and not globals()['I00164']:
        btnRedManBTbletHoprDoor0.configure(fg_color="pink")
        btnBAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00020'] and globals()['I00164']:
        if RedManBTbletHoprDoor0:
            btnRedManBTbletHoprDoor0.configure(fg_color="Red")
            btnBAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="Red", text_color="black")
        else:
            btnRedManBTbletHoprDoor0.configure(fg_color="pink")
            btnBAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="pink", text_color="white")
        RedManBTbletHoprDoor0 = not RedManBTbletHoprDoor0

    if globals()['I00021']:
        btnGreenManBTbletHoprDoor0.configure(fg_color="lime")
        btnBAutoPneumTbletHoprDoor0IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00021'] and not globals()['I00165']:
        btnGreenManBTbletHoprDoor0.configure(fg_color="light green")
        btnBAutoPneumTbletHoprDoor0IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00021'] and globals()['I00165']:
        if GreenTbletHoprDoor0:
            btnGreenManBTbletHoprDoor0.configure(fg_color="lime")
            btnBAutoPneumTbletHoprDoor0IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManBTbletHoprDoor0.configure(fg_color="light green")
            btnBAutoPneumTbletHoprDoor0IsClose.configure(fg_color="light green", text_color="white")
        GreenTbletHoprDoor0 = not GreenTbletHoprDoor0
    
    # .btnBolaC1C32 Auto Common Page 2
    if not globals()['J00545'] and globals()['J00513']:
        btnBolaC1C32.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00545'] and globals()['J00513']:
        if ManBTbletHoprDoor0Blinking:
            btnBolaC1C32.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnBolaC1C32.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00020']:
        btnBolaC1C32.configure(text="Open",fg_color="Red", text_color="black")
    elif not globals()['I00020'] and globals()['I00164']:
        if RedManBTbletHoprDoor0:
            btnBolaC1C32.configure(text="Open",fg_color="Red", text_color="black")
        else:
            btnBolaC1C32.configure(text="Open",fg_color="pink", text_color="white")
    elif globals()['I00021']:
        btnBolaC1C32.configure(text="Close",fg_color="lime", text_color="black")
    elif not globals()['I00021'] and globals()['I00165']:
        if GreenTbletHoprDoor0:
            btnBolaC1C32.configure(text="Close",fg_color="lime", text_color="black")
        else:
            btnBolaC1C32.configure(text="Close",fg_color="light green", text_color="white")
    else:
        btnBolaC1C32.configure(fg_color=lightOrange, text="Fault", text_color="white")

    # ERROR
    if not globals()['J00546'] and globals()['J00514']:
        frmManBTbletHoprDoor1Lbl.configure(fg_color="orange")
        btnBAutoPneumTbletHoprDoor1IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00546'] and globals()['J00514']:
        if TbletHoprDoor1Blinking:
            frmManBTbletHoprDoor1Lbl.configure(fg_color="orange")
            btnBAutoPneumTbletHoprDoor1IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManBTbletHoprDoor1Lbl.configure(fg_color=lightOrange)
            btnBAutoPneumTbletHoprDoor1IsFault.configure(fg_color=lightOrange, text_color="white")
        TbletHoprDoor1Blinking = not TbletHoprDoor1Blinking
    else:
        frmManBTbletHoprDoor1Lbl.configure(fg_color=lightOrange)
        btnBAutoPneumTbletHoprDoor1IsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00022']:
        btnRedManBTbletHoprDoor1.configure(fg_color="Red")
        btnBAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00022'] and not globals()['I00166']:
        btnRedManBTbletHoprDoor1.configure(fg_color="pink")
        btnBAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00022'] and globals()['I00166']:
        if RedTbletHoprDoor1:
            btnRedManBTbletHoprDoor1.configure(fg_color="Red")
            btnBAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="Red", text_color="black")
        else:
            btnRedManBTbletHoprDoor1.configure(fg_color="pink")
            btnBAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="pink", text_color="white")
        RedTbletHoprDoor1 = not RedTbletHoprDoor1

    if globals()['I00023']:
        btnGreenManBTbletHoprDoor1.configure(fg_color="lime")
        btnBAutoPneumTbletHoprDoor1IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00023'] and not globals()['I00167']:
        btnGreenManBTbletHoprDoor1.configure(fg_color="light green")
        btnBAutoPneumTbletHoprDoor1IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00023'] and globals()['I00167']:
        if GreenTbletHoprDoor1:
            btnGreenManBTbletHoprDoor1.configure(fg_color="lime")
            btnBAutoPneumTbletHoprDoor1IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManBTbletHoprDoor1.configure(fg_color="light green")
            btnBAutoPneumTbletHoprDoor1IsClose.configure(fg_color="light green", text_color="white")
        GreenTbletHoprDoor1 = not GreenTbletHoprDoor1

    # .btnBolaC1C33 Auto Common Page 2
    if not globals()['J00546'] and globals()['J00514']:
        btnBolaC1C33.configure(text="Fault",fg_color="orange", text_color="black")
    elif globals()['J00546'] and globals()['J00514']:
        if TbletHoprDoor1Blinking:
            btnBolaC1C33.configure(text="Fault",fg_color="orange", text_color="black")
        else:
            btnBolaC1C33.configure(text="Fault",fg_color=lightOrange,  text_color="white")
    elif globals()['I00022']:
        btnBolaC1C33.configure(text="Open",fg_color="Red", text_color="black")
    elif not globals()['I00022'] and globals()['I00166']:
        if RedTbletHoprDoor1:
            btnBolaC1C33.configure(text="Open",fg_color="Red", text_color="black")
        else:
            btnBolaC1C33.configure(text="Open",fg_color="pink", text_color="white")
    elif globals()['I00023']:
        btnBolaC1C33.configure(text="Close",fg_color="lime", text_color="black")
    elif not globals()['I00023'] and globals()['I00167']:
        if GreenTbletHoprDoor1:
            btnBolaC1C33.configure(text="Close",fg_color="lime", text_color="black")
        else:
            btnBolaC1C33.configure(text="Close",fg_color="light green", text_color="white")
    else:
        btnBolaC1C33.configure(text="Fault",fg_color=lightOrange,  text_color="white") 

    # btnMatermixRotor Line Z
    if not globals()['J00548'] and globals()['J00516']:
        frmBManMaterMixRotorLbl.configure(fg_color="orange")
        btnBAutoMotorMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
        btnMatermixRotor.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00548'] and globals()['J00516']:
        if MaterMixRotorBlinking:
            frmBManMaterMixRotorLbl.configure(fg_color="orange")
            btnBAutoMotorMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
            btnMatermixRotor.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            frmBManMaterMixRotorLbl.configure(fg_color=lightOrange)
            btnBAutoMotorMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
            btnMatermixRotor.configure(text="Fault", fg_color=lightOrange, text_color="white")
        MaterMixRotorBlinking = not MaterMixRotorBlinking
    else:
        frmBManMaterMixRotorLbl.configure(fg_color=lightOrange)
        btnBAutoMotorMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
    
    # Auto B Motor Rev Fwd
    if globals()['I00146']:
        btnBAutoMotorMaterMixDoorDoRev.configure(fg_color="red", text_color="black")
        btnMatermixRotor.configure(text="Rev", fg_color="red", text_color="black")
    else:
        btnBAutoMotorMaterMixDoorDoRev.configure(fg_color="pink", text_color="white")
        btnMatermixRotor.configure(text="Rev", fg_color="pink", text_color="white")
    
    if globals()['I00144']:
        btnBAutoMotorMaterMixDoorDoFwd.configure(fg_color="lime", text_color="black")
        btnMatermixRotor.configure(text="Fwd", fg_color="lime", text_color="black")
    else:
        btnBAutoMotorMaterMixDoorDoFwd.configure(fg_color="light green", text_color="white")
        btnMatermixRotor.configure(text="Fwd", fg_color="light green", text_color="white")

    if (not globals()['I00146'] and not globals()['I00144'] and not globals()['J00548'] and not globals()['J00516']):
        btnMatermixRotor.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # .btnMatermixRotor Auto Common Page 2
    if not globals()['J00548'] and globals()['J00516']:
        btnMatermixRotor.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00548'] and globals()['J00516']:
        if MaterMixRotorBlinking:
            btnMatermixRotor.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnMatermixRotor.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00146']:
        btnMatermixRotor.configure(text="Rev", fg_color="red", text_color="black")
    elif globals()['I00144']:
        btnMatermixRotor.configure(text="Fwd", fg_color="lime", text_color="black")
    else:
        btnMatermixRotor.configure(text="Fault", fg_color=lightOrange, text_color="white")



    # ERROR MotorMaterMixRotorC0 Common Page 2 Line C
    if not globals()['J00566'] and globals()['J00534']:
        frmCManMaterMixRotorLbl.configure(fg_color="orange")
        btnCAutoMotorMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00566'] and globals()['J00534']:
        if globals()['CManMaterMixRotorBlinking']:
            frmCManMaterMixRotorLbl.configure(fg_color="orange")
            btnCAutoMotorMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManMaterMixRotorLbl.configure(fg_color=lightOrange)
            btnCAutoMotorMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMaterMixRotorBlinking'] = not globals()['CManMaterMixRotorBlinking']
    else:
        frmCManMaterMixRotorLbl.configure(fg_color=lightOrange)
        btnCAutoMotorMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
    
    # Auto C Motor Rev Fwd
    if globals()['I00210']:
        btnCAutoMotorMaterMixDoorDoRev.configure(fg_color="red", text_color="black")
    else:
        btnCAutoMotorMaterMixDoorDoRev.configure(fg_color="pink", text_color="white")
    
    if globals()['I00208']:
        btnCAutoMotorMaterMixDoorDoFwd.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorMaterMixDoorDoFwd.configure(fg_color="light green", text_color="white")
    
    # .btnMatermixRotorC Auto Common Page 2
    if not globals()['J00566'] and globals()['J00534']:
        btnMatermixRotorC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00566'] and globals()['J00534']:
        if globals()['CManMaterMixRotorBlinking']:
            btnMatermixRotorC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMatermixRotorC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00210']:
        btnMatermixRotorC.configure(text="Rev", fg_color="red", text_color="black")
    elif globals()['I00208']:
        btnMatermixRotorC.configure(text="Fwd", fg_color="lime", text_color="black")
    else:
        btnMatermixRotorC.configure(text="Fault", fg_color=lightOrange, text_color="white")

    
    # ERROR PneumMaterMixDoorC0
    if not globals()['J00560'] and globals()['J00528']:
        frmCManMaterMixDoorLbl.configure(fg_color="orange")
        btnCAutoPneumMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00560'] and globals()['J00528']:
        if globals()['CManPneumMaterMixDoorBlinking']:
            frmCManMaterMixDoorLbl.configure(fg_color="orange")
            btnCAutoPneumMaterMixDoorIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManMaterMixDoorLbl.configure(fg_color=lightOrange)
            btnCAutoPneumMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManPneumMaterMixDoorBlinking'] = not globals()['CManPneumMaterMixDoorBlinking']
    else:
        frmCManMaterMixDoorLbl.configure(fg_color=lightOrange)
        btnCAutoPneumMaterMixDoorIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00065']:   
        btnRedCManMaterMixDoor.configure(fg_color="Red")
        btnCAutoPneumMaterMixDoorIsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00065'] and not globals()['I00192']:
        btnRedCManMaterMixDoor.configure(fg_color="pink")
        btnCAutoPneumMaterMixDoorIsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00065'] and globals()['I00192']:
        if globals()['RedCManMaterMixDoor']:
            btnRedCManMaterMixDoor.configure(fg_color="pink")
            btnCAutoPneumMaterMixDoorIsOpen.configure(fg_color="pink", text_color="white")
        else:
            btnRedCManMaterMixDoor.configure(fg_color="red")
            btnCAutoPneumMaterMixDoorIsOpen.configure(fg_color="Red", text_color="black")
        globals()['RedCManMaterMixDoor'] = not globals()['RedCManMaterMixDoor']

    if globals()['I00066']:
        btnGreenCManMaterMixDoor.configure(fg_color="lime")
        btnCAutoPneumMaterMixDoorIsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00066'] and not globals()['I00193']:
        btnGreenCManMaterMixDoor.configure(fg_color="light green")
        btnCAutoPneumMaterMixDoorIsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00066'] and globals()['I00193']:
        if GreenCManMaterMixDoor:
            btnGreenCManMaterMixDoor.configure(fg_color="lime")
            btnCAutoPneumMaterMixDoorIsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenCManMaterMixDoor.configure(fg_color="light green")
            btnCAutoPneumMaterMixDoorIsClose.configure(fg_color="light green", text_color="white")
        GreenCManMaterMixDoor = not GreenCManMaterMixDoor
    
    # .btnMatermixC Mixer Door Auto Common Z Page 2
    if not globals()['J00560'] and globals()['J00528']:
        btnMatermixC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00560'] and globals()['J00528']:
        if globals()['CManPneumMaterMixDoorBlinking']:
            btnMatermixC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMatermixC.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00065']:   
        btnMatermixC.configure(fg_color="Red", text="Open", text_color="black")
    elif not globals()['I00065'] and globals()['I00192']:
        if globals()['RedCManMaterMixDoor']:
            btnMatermixC.configure(fg_color="pink", text="Open", text_color="white")
        else:
            btnMatermixC.configure(fg_color="Red", text="Open", text_color="black")
    elif globals()['I00066']:
        btnMatermixC.configure(fg_color="lime", text="Close", text_color="black")
    elif not globals()['I00066'] and globals()['I00193']:
        if GreenCManMaterMixDoor:
            btnMatermixC.configure(fg_color="lime", text="Close", text_color="black")
        else:
            btnMatermixC.configure(fg_color="light green", text="Close", text_color="white")
    else:
        btnMatermixC.configure(fg_color=lightOrange, text="Fault", text_color="white")




    if globals()['I00135']:
        btnGreenBManToRotaryCnvyr0.configure(fg_color="lime")
        btnBAutoPneumToRotaryCnvyr0DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr0.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToRotaryCnvyr0.configure(fg_color="light green")
        btnBAutoPneumToRotaryCnvyr0DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr0.configure(fg_color="light green", text_color="white")

    if globals()['I00137']:
        btnGreenBManToRotaryCnvyr1.configure(fg_color="lime")
        btnBAutoPneumToRotaryCnvyr1DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr1.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToRotaryCnvyr1.configure(fg_color="light green")
        btnBAutoPneumToRotaryCnvyr1DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr1.configure(fg_color="light green", text_color="white")

    if globals()['I00139']:
        btnGreenBManToRotaryCnvyr2.configure(fg_color="lime")
        btnBAutoPneumToRotaryCnvyr2DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr2.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToRotaryCnvyr2.configure(fg_color="light green")
        btnBAutoPneumToRotaryCnvyr2DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr2.configure(fg_color="light green", text_color="white")

    if globals()['I00141']:
        btnGreenBManToRotaryCnvyr3.configure(fg_color="lime")
        btnBAutoPneumToRotaryCnvyr3DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr3.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToRotaryCnvyr3.configure(fg_color="light green")
        btnBAutoPneumToRotaryCnvyr3DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr3.configure(fg_color="light green", text_color="white")

    if globals()['I00143']:
        btnGreenBManToRotaryCnvyr4.configure(fg_color="lime")
        btnBAutoPneumToRotaryCnvyr4DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr4.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToRotaryCnvyr4.configure(fg_color="light green")
        btnBAutoPneumToRotaryCnvyr4DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr4.configure(fg_color="light green", text_color="white")

    if globals()['I00153']:
        btnGreenBManToHopperCnvyr0.configure(fg_color="lime")
        btnBAutoPneumToHopperCnvyr0DoClose.configure(fg_color="lime", text_color="black")
        btnTbltHoprDoor0.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToHopperCnvyr0.configure(fg_color="Light Green")
        btnBAutoPneumToHopperCnvyr0DoClose.configure(fg_color="light green", text_color="white")
        btnTbltHoprDoor0.configure(fg_color="light green", text_color="white")

    if globals()['I00155']:
        btnGreenBManToHopperCnvyr1.configure(fg_color="lime")
        btnBAutoPneumToHopperCnvyr1DoClose.configure(fg_color="lime", text_color="black")
        btnTbltHoprDoor1.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToHopperCnvyr1.configure(fg_color="Light Green")
        btnBAutoPneumToHopperCnvyr1DoClose.configure(fg_color="Light Green", text_color="white")
        btnTbltHoprDoor1.configure(fg_color="Light Green", text_color="white")

    if globals()['I00157']:
        btnGreenBManToHopperCnvyr2.configure(fg_color="lime")
        btnBAutoPneumToHopperCnvyr2DoClose.configure(fg_color="lime", text_color="black")
        btnTbltHoprDoor2.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToHopperCnvyr2.configure(fg_color="Light Green")
        btnBAutoPneumToHopperCnvyr2DoClose.configure(fg_color="Light Green", text_color="white")
        btnTbltHoprDoor2.configure(fg_color="Light Green", text_color="white")

    if globals()['I00159']:
        btnGreenBManToHopperCnvyr3.configure(fg_color="lime")
        btnBAutoPneumToHopperCnvyr3DoClose.configure(fg_color="lime", text_color="black")
        btnTbltHoprDoor3.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToHopperCnvyr3.configure(fg_color="Light Green")
        btnBAutoPneumToHopperCnvyr3DoClose.configure(fg_color="Light Green", text_color="white")
        btnTbltHoprDoor3.configure(fg_color="Light Green", text_color="white")

    if globals()['I00173']:
        btnGreenBManToRncenCnvyr.configure(fg_color="lime")
        btnBAutoPneumToRncenCnvyrDoClose.configure(fg_color="lime", text_color="black")
        btnMotorToRncenCnvyr.configure(fg_color="lime", text_color="black")
    else:
        btnGreenBManToRncenCnvyr.configure(fg_color="Light Green")
        btnBAutoPneumToRncenCnvyrDoClose.configure(fg_color="light green", text_color="white")
        btnMotorToRncenCnvyr.configure(fg_color="light green", text_color="white")

    if globals()['I00006']:
        if not globals()['J00135']:
            if RtaryUnitHop0Blinking:
                frmnBManRtaryUnitHop0.configure(fg_color="yellow")
                btnBAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop0.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManRtaryUnitHop0.configure(fg_color="light yellow")
                btnBAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop0.configure(fg_color="light yellow", text_color="white")
            RtaryUnitHop0Blinking = not RtaryUnitHop0Blinking
        elif globals()['J00135']:
            frmnBManRtaryUnitHop0.configure(fg_color="yellow")
            btnBAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop0.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManRtaryUnitHop0.configure(fg_color="light yellow")
        btnBAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop0.configure(fg_color="light yellow", text_color="white")

    if globals()['I00007']:
        if not globals()['J00136']:
            if RtaryUnitHop1Blinking:
                frmnBManRtaryUnitHop1.configure(fg_color="yellow")
                btnBAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop1.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManRtaryUnitHop1.configure(fg_color="light yellow")
                btnBAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop1.configure(fg_color="light yellow", text_color="white")
            RtaryUnitHop1Blinking = not RtaryUnitHop1Blinking
        elif globals()['J00136']:
            frmnBManRtaryUnitHop1.configure(fg_color="yellow")
            btnBAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop1.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManRtaryUnitHop1.configure(fg_color="light yellow")
        btnBAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop1.configure(fg_color="light yellow", text_color="white")

    if globals()['I00008']:
        if not globals()['J00137']:
            if RtaryUnitHop2Blinking:
                frmnBManRtaryUnitHop2.configure(fg_color="yellow")
                btnBAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop2.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManRtaryUnitHop2.configure(fg_color="light yellow")
                btnBAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop2.configure(fg_color="light yellow", text_color="white")
            RtaryUnitHop2Blinking = not RtaryUnitHop2Blinking
        elif globals()['J00137']:
            frmnBManRtaryUnitHop2.configure(fg_color="yellow")
            btnBAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop2.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManRtaryUnitHop2.configure(fg_color="light yellow")
        btnBAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop2.configure(fg_color="light yellow", text_color="white")

    if globals()['I00009']:
        if not globals()['J00138']:
            if RtaryUnitHop3Blinking:
                frmnBManRtaryUnitHop3.configure(fg_color="yellow")
                btnBAutoPneumSensorRtaryUnitHop3IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop3.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManRtaryUnitHop3.configure(fg_color="light yellow")
                btnBAutoPneumSensorRtaryUnitHop3IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop3.configure(fg_color="light yellow", text_color="white")
            RtaryUnitHop3Blinking = not RtaryUnitHop3Blinking
        elif globals()['J00138']:
            frmnBManRtaryUnitHop3.configure(fg_color="yellow")
            btnBAutoPneumSensorRtaryUnitHop3IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop3.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManRtaryUnitHop3.configure(fg_color="light yellow")
        btnBAutoPneumSensorRtaryUnitHop3IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop3.configure(fg_color="light yellow", text_color="white")

    if globals()['I00010']:
        if not globals()['J00139']:
            if RtaryUnitHop4Blinking:
                frmnBManRtaryUnitHop4.configure(fg_color="yellow")
                btnBAutoPneumSensorRtaryUnitHop4IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop4.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManRtaryUnitHop4.configure(fg_color="light yellow")
                btnBAutoPneumSensorRtaryUnitHop4IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop4.configure(fg_color="light yellow", text_color="white")
            RtaryUnitHop4Blinking = not RtaryUnitHop4Blinking
        elif globals()['J00139']:
            frmnBManRtaryUnitHop4.configure(fg_color="yellow")
            btnBAutoPneumSensorRtaryUnitHop4IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop4.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManRtaryUnitHop4.configure(fg_color="light yellow")
        btnBAutoPneumSensorRtaryUnitHop4IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop4.configure(fg_color="light yellow", text_color="white")

    if globals()['I00016']:
        if not globals()['J00140']:
            if TabletVaryHop0Blinking:
                frmnBManTabletVaryHop0.configure(fg_color="yellow")
                btnBAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop0.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManTabletVaryHop0.configure(fg_color="light yellow")
                btnBAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop0.configure(fg_color="light yellow", text_color="white")
            TabletVaryHop0Blinking = not TabletVaryHop0Blinking
        elif globals()['J00140']:
            frmnBManTabletVaryHop0.configure(fg_color="yellow")
            btnBAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop0.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManTabletVaryHop0.configure(fg_color="light yellow")
        btnBAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop0.configure(fg_color="light yellow", text_color="white")

    if globals()['I00017']:
        if not globals()['J00141']:
            if TabletVaryHop1Blinking:
                frmnBManTabletVaryHop1.configure(fg_color="yellow")
                btnBAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop1.configure(fg_color="yellow", text_color="black")
            else:
                frmnBManTabletVaryHop1.configure(fg_color="light yellow")
                btnBAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop1.configure(fg_color="light yellow", text_color="white")
            TabletVaryHop1Blinking = not TabletVaryHop1Blinking
        elif globals()['J00141']:
            frmnBManTabletVaryHop1.configure(fg_color="yellow")
            btnBAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop1.configure(fg_color="yellow", text_color="black")
    else:
        frmnBManTabletVaryHop1.configure(fg_color="light yellow")
        btnBAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop1.configure(fg_color="light yellow", text_color="white")

    if globals()['I00018']:
        if not globals()['J00142']:
            if TabletVaryHop2Blinking:
                frmnManBTabletVaryHop2.configure(fg_color="yellow")
                btnBAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop2.configure(fg_color="yellow", text_color="black")
            else:
                frmnManBTabletVaryHop2.configure(fg_color="light yellow")
                btnBAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop2.configure(fg_color="light yellow", text_color="white")
            TabletVaryHop2Blinking = not TabletVaryHop2Blinking
        elif globals()['J00142']:
            frmnManBTabletVaryHop2.configure(fg_color="yellow")
            btnBAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop2.configure(fg_color="yellow", text_color="black")
    else:
        frmnManBTabletVaryHop2.configure(fg_color="light yellow")
        btnBAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop2.configure(fg_color="light yellow", text_color="white")

    if globals()['I00019']:
        if not globals()['J00143']:
            if TabletVaryHop3Blinking:
                frmnManBTabletVaryHop3.configure(fg_color="yellow")
                btnBAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop3.configure(fg_color="yellow", text_color="black")
            else:
                frmnManBTabletVaryHop3.configure(fg_color="light yellow")
                btnBAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop3.configure(fg_color="light yellow", text_color="white")
            TabletVaryHop3Blinking = not TabletVaryHop3Blinking
        elif globals()['J00143']:
            frmnManBTabletVaryHop3.configure(fg_color="yellow")
            btnBAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop3.configure(fg_color="yellow", text_color="black")
    else:
        frmnManBTabletVaryHop3.configure(fg_color="light yellow")
        btnBAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop3.configure(fg_color="light yellow", text_color="white")

    if globals()['I00014']:
        if not globals()['J00144']:
            if RncenMachHop0Blinking:
                frmnRncenMachHop0.configure(fg_color="yellow")
                btnBAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="yellow", text_color="black")
                btnRncenMachHop0.configure(fg_color="yellow", text_color="black")
            else:
                frmnRncenMachHop0.configure(fg_color="light yellow")
                btnBAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="light yellow", text_color="white")
                btnRncenMachHop0.configure(fg_color="light yellow", text_color="white")
            RncenMachHop0Blinking = not RncenMachHop0Blinking
        elif globals()['J00144']:
            frmnRncenMachHop0.configure(fg_color="yellow")
            btnBAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="yellow", text_color="black")
            btnRncenMachHop0.configure(fg_color="yellow", text_color="black")
    else:
        frmnRncenMachHop0.configure(fg_color="light yellow")
        btnBAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="light yellow", text_color="white")
        btnRncenMachHop0.configure(fg_color="light yellow", text_color="white")

    if globals()['I00015']:
        if not globals()['J00145']:
            if RncenMachHop1Blinking:
                frmnRncenMachHop1.configure(fg_color="yellow")
                btnBAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="yellow", text_color="black")
                btnRncenMachHop1.configure(fg_color="yellow", text_color="black")
            else:
                frmnRncenMachHop1.configure(fg_color="light yellow")
                btnBAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="light yellow", text_color="white")
                btnRncenMachHop1.configure(fg_color="light yellow", text_color="white")
            RncenMachHop1Blinking = not RncenMachHop1Blinking
        elif globals()['J00145']:
            frmnRncenMachHop1.configure(fg_color="yellow")
            btnBAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="yellow", text_color="black")
            btnRncenMachHop1.configure(fg_color="yellow", text_color="black")
    else:
        frmnRncenMachHop1.configure(fg_color="light yellow")
        btnBAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="light yellow", text_color="white")
        btnRncenMachHop1.configure(fg_color="light yellow", text_color="white")

    if not globals()['J00547'] and globals()['J00515']:
        frmManBTbletHoprDoorLbl.configure(fg_color="orange")
        btnBAutoMotorTbletHoprDoorIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00547'] and globals()['J00515']:
        if TbletHoprDoorBlinking:
            frmManBTbletHoprDoorLbl.configure(fg_color="orange")
            btnBAutoMotorTbletHoprDoorIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManBTbletHoprDoorLbl.configure(fg_color=lightOrange)
            btnBAutoMotorTbletHoprDoorIsFault.configure(fg_color=lightOrange, text_color="white")
        TbletHoprDoorBlinking = not TbletHoprDoorBlinking
    else:
        frmManBTbletHoprDoorLbl.configure(fg_color=lightOrange)
        btnBAutoMotorTbletHoprDoorIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00168']:
        btnBAutoMotorTbletHoprDoorDoStart.configure(fg_color="lime")
    else:
        btnBAutoMotorTbletHoprDoorDoStart.configure(fg_color="Light Green", text_color="white")

    # .btnTbltHoprDoor Auto Besar B Page 2
    if not globals()['J00547'] and globals()['J00515']:
        btnTbltHoprDoor.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00547'] and globals()['J00515']:
        if TbletHoprDoorBlinking:
            btnTbltHoprDoor.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnTbltHoprDoor.configure(fg_color=lightOrange, text="Fault", text_color="black")
    elif globals()['I00168']:
        btnTbltHoprDoor.configure(fg_color="lime", text="Start", text_color="black")
    else:
        btnTbltHoprDoor.configure(fg_color=lightOrange, text="Fault", text_color="white")


    if not globals()['J00549'] and globals()['J00517']:
        frmBManMateriVbratorLbl.configure(fg_color="orange")
        btnBAutoMotorMateriVbratorIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00549'] and globals()['J00517']:
        if MateriVbratorBlinking:
            frmBManMateriVbratorLbl.configure(fg_color="orange")
            btnBAutoMotorMateriVbratorIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManMateriVbratorLbl.configure(fg_color=lightOrange)
            btnBAutoMotorMateriVbratorIsFault.configure(fg_color=lightOrange, text_color="white")
        MateriVbratorBlinking = not MateriVbratorBlinking
    else:
        frmBManMateriVbratorLbl.configure(fg_color=lightOrange)
        btnBAutoMotorMateriVbratorIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00130']:
        btnBAutoMotorMateriVbratorDoStart.configure(fg_color="lime")
    else:
        btnBAutoMotorMateriVbratorDoStart.configure(fg_color="Light Green", text_color="white")
    
    # .btnMateriVbrator Auto Besar B Page 2
    if not globals()['J00549'] and globals()['J00517']:
        btnMateriVbrator.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00549'] and globals()['J00517']:
        if MateriVbratorBlinking:
            btnMateriVbrator.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMateriVbrator.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00130']:
        btnMateriVbrator.configure(fg_color="lime", text="Start", text_color="black")
    else:
        btnMateriVbrator.configure(fg_color=lightOrange, text="Fault", text_color="white")

    # btnMotorMatScrewCnvyr Motor Screw Auto Line B
    if not globals()['J00550'] and globals()['J00518']:
        frmBManMatScrewCnvyrLbl.configure(fg_color="orange")
        btnBAutoMotorMatScrewCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00550'] and globals()['J00518']:
        if MatScrewCnvyrBlinking:
            frmBManMatScrewCnvyrLbl.configure(fg_color="orange")
            btnBAutoMotorMatScrewCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManMatScrewCnvyrLbl.configure(fg_color=lightOrange)
            btnBAutoMotorMatScrewCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        MatScrewCnvyrBlinking = not MatScrewCnvyrBlinking
    else:
        frmBManMatScrewCnvyrLbl.configure(fg_color=lightOrange)
        btnBAutoMotorMatScrewCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00149']:
        btnBAutoMotorMatScrewCnvyrDoRev.configure(fg_color="red", text_color="black")
    else:
        btnBAutoMotorMatScrewCnvyrDoRev.configure(fg_color="pink", text_color="white")
    
    if globals()['I00147']:
        btnBAutoMotorMatScrewCnvyrDoFwd.configure(fg_color="lime", text_color="black")
    else:
        btnBAutoMotorMatScrewCnvyrDoFwd.configure(fg_color="light green", text_color="white")
    
    # .btnMotorMatScrewCnvyr Auto Besar B Page 2
    if not globals()['J00550'] and globals()['J00518']:
        btnMotorMatScrewCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00550'] and globals()['J00518']:
        if MatScrewCnvyrBlinking:
            btnMotorMatScrewCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnMotorMatScrewCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00149']:
        btnMotorMatScrewCnvyr.configure(text="Rev", fg_color="red", text_color="black")
    elif globals()['I00147']:
        btnMotorMatScrewCnvyr.configure(text="Fwd", fg_color="lime", text_color="black")
    else:
        btnMotorMatScrewCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # btnMotorToRotaryCnvyr Line B Auto
    if not globals()['J00551'] and globals()['J00519']:
        frmBManToRotaryCnvyrLbl.configure(fg_color="orange")
        btnBAutoMotorToRotaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00551'] and globals()['J00519']:
        if ToRotaryCnvyrBlinking:
            frmBManToRotaryCnvyrLbl.configure(fg_color="orange")
            btnBAutoMotorToRotaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManToRotaryCnvyrLbl.configure(fg_color=lightOrange)
            btnBAutoMotorToRotaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        ToRotaryCnvyrBlinking = not ToRotaryCnvyrBlinking
    else:
        frmBManToRotaryCnvyrLbl.configure(fg_color=lightOrange)
        btnBAutoMotorToRotaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00132']:
        btnBAutoMotorToRotaryCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnBAutoMotorToRotaryCnvyrDoStart.configure(fg_color="Light Green", text_color="white")
    
    # .btnMotorToRotaryCnvyr Auto Besar B Page 2
    if not globals()['J00551'] and globals()['J00519']:
        btnMotorToRotaryCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00551'] and globals()['J00519']:
        if ToRotaryCnvyrBlinking:
            btnMotorToRotaryCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnMotorToRotaryCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00132']:
        btnMotorToRotaryCnvyr.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnMotorToRotaryCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # btnFrmRtaryCnvyr Auto Besar Line B
    if not globals()['J00552'] and globals()['J00520']:
        frmBManRtaryCnvyrLbl.configure(fg_color="orange")
        btnBAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00552'] and globals()['J00520']:
        if FrmBManRtaryCnvyrBlinking:
            frmBManRtaryCnvyrLbl.configure(fg_color="orange")
            btnBAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManRtaryCnvyrLbl.configure(fg_color=lightOrange)
            btnBAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        FrmBManRtaryCnvyrBlinking = not FrmBManRtaryCnvyrBlinking
    else:
        frmBManRtaryCnvyrLbl.configure(fg_color=lightOrange)
        btnBAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00160']:
        btnBAutoMotorFrmRtaryCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnBAutoMotorFrmRtaryCnvyrDoStart.configure(fg_color="Light Green", text_color="white")

    # .btnFrmRtaryCnvyr Auto Besar B Page 2
    if not globals()['J00552'] and globals()['J00520']:
        btnFrmRtaryCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00552'] and globals()['J00520']:
        if FrmBManRtaryCnvyrBlinking:
            btnFrmRtaryCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnFrmRtaryCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00160']:
        btnFrmRtaryCnvyr.configure(text="Start",fg_color="lime", text_color="black")
    else:
        btnFrmRtaryCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # btnUpLadderCnvyr Auto Besar B page 2
    if not globals()['J00553'] and globals()['J00521']:
        frmBManUpLadderCnvyrLbl.configure(fg_color="orange")
        btnBAutoMotorUpladderCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00553'] and globals()['J00521']:
        if UpLadderCnvyrBlinking:
            frmBManUpLadderCnvyrLbl.configure(fg_color="orange")
            btnBAutoMotorUpladderCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManUpLadderCnvyrLbl.configure(fg_color=lightOrange)
            btnBAutoMotorUpladderCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        UpLadderCnvyrBlinking = not UpLadderCnvyrBlinking
    else:
        frmBManUpLadderCnvyrLbl.configure(fg_color=lightOrange)
        btnBAutoMotorUpladderCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00162']:
        btnBAutoMotorUpladderCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnBAutoMotorUpladderCnvyrDoStart.configure(fg_color="Light Green", text_color="white")
    
    # .btnUpLadderCnvyr Auto Besar B Page 2
    if not globals()['J00553'] and globals()['J00521']:
        btnUpLadderCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00553'] and globals()['J00521']:
        if UpLadderCnvyrBlinking:
            btnUpLadderCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnUpLadderCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00162']:
        btnUpLadderCnvyr.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnUpLadderCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # Conveyor To Silo Line B Auto page 2
    if not globals()['J00554'] and globals()['J00522']:
        frmBManToHopperCnvyrLbl.configure(fg_color="orange")
        btnBAutoMotorToHopperCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00554'] and globals()['J00522']:
        if ToHopperCnvyrBlinking:
            frmBManToHopperCnvyrLbl.configure(fg_color="orange")
            btnBAutoMotorToHopperCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmBManToHopperCnvyrLbl.configure(fg_color=lightOrange)
            btnBAutoMotorToHopperCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        ToHopperCnvyrBlinking = not ToHopperCnvyrBlinking
    else:
        frmBManToHopperCnvyrLbl.configure(fg_color=lightOrange)
        btnBAutoMotorToHopperCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00150']:
        btnBAutoMotorToHopperCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnBAutoMotorToHopperCnvyrDoStart.configure(fg_color="Light Green", text_color="white")
    
    # .btnUpLadderCnvyr Auto Besar B Page 2
    if not globals()['J00554'] and globals()['J00522']:
        btnToHopperCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00554'] and globals()['J00522']:
        if ToHopperCnvyrBlinking:
            btnToHopperCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnToHopperCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00150']:
        btnToHopperCnvyr.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnToHopperCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # Modular Conveyor / To Renceng Conveyor Line B Auto Page 2
    if not globals()['J00555'] and globals()['J00523']:
        frmManBToRncenCnvyrLbl.configure(fg_color="orange")
        btnBAutoMotorToRncenCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00555'] and globals()['J00523']:
        if ToRncenCnvyrBlinking:
            frmManBToRncenCnvyrLbl.configure(fg_color="orange")
            btnBAutoMotorToRncenCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManBToRncenCnvyrLbl.configure(fg_color=lightOrange)
            btnBAutoMotorToRncenCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        ToRncenCnvyrBlinking = not ToRncenCnvyrBlinking
    else:
        frmManBToRncenCnvyrLbl.configure(fg_color=lightOrange)
        btnBAutoMotorToRncenCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00170']:
        btnBAutoMotorToRncenCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnBAutoMotorToRncenCnvyrDoStart.configure(fg_color="Light Green", text_color="white")

    # .btnPneumToRncenCnvyr Auto Besar B Page 2
    if not globals()['J00555'] and globals()['J00523']:
        btnPneumToRncenCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
    elif globals()['J00555'] and globals()['J00523']:
        if ToRncenCnvyrBlinking:
            btnPneumToRncenCnvyr.configure(text="Fault", fg_color="orange", text_color="black")
        else:
            btnPneumToRncenCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")
    elif globals()['I00170']:
        btnPneumToRncenCnvyr.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnPneumToRncenCnvyr.configure(text="Fault", fg_color=lightOrange, text_color="white")


# LINE C
    # BUTTON FEEDER C
    # Putih
    if ((globals()['V0148'] & 512) != 512) and globals()['V0146'] != 512:
        btnAutoFeedPutihC.configure(fg_color="light green", text_color="white", state="normal")
    elif ((globals()['V0148'] & 512) == 512) and globals()['V0142'] != 512 and globals()['V0146'] != 512:
        btnAutoFeedPutihC.configure(fg_color="lime", text_color="black", state="normal")
    elif ((globals()['V0148'] & 512) == 512) and globals()['V0142'] == 512 and globals()['V0146'] != 512:
        if globals()['FeederCPutihBlinking']:
            btnAutoFeedPutihC.configure(fg_color="light green", text_color="white", state="normal")
        else:
            btnAutoFeedPutihC.configure(fg_color="lime", text_color="black", state="normal")
        globals()['FeederCPutihBlinking'] = not globals()['FeederCPutihBlinking']
    elif globals()['V0146'] == 512:
        btnAutoFeedPutihC.configure(fg_color="lime", text_color="black", state="normal")
    
    # Warna1
    if ((globals()['V0148'] & 256) != 256) and globals()['V0146'] != 256:
        btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 256) == 256) and globals()['V0142'] != 256 and globals()['V0146'] != 256:
        btnAutoFeedWarna1C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 256) == 256) and globals()['V0142'] == 256 and globals()['V0146'] != 256:
        if globals()['FeederCWarna1Blinking']:
            btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna1C.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederCWarna1Blinking'] = not globals()['FeederCWarna1Blinking']
    elif globals()['V0146'] == 256:
        btnAutoFeedWarna1C.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna2
    if ((globals()['V0148'] & 128) != 128) and globals()['V0146'] != 128:
        btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 128) == 128) and globals()['V0142'] != 128 and globals()['V0146'] != 128:
        btnAutoFeedWarna2C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 128) == 128) and globals()['V0142'] == 128 and globals()['V0146'] != 128:
        if globals()['FeederCWarna2Blinking']:
            btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna2C.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederCWarna2Blinking'] = not globals()['FeederCWarna2Blinking']
    elif globals()['V0146'] == 128:
        btnAutoFeedWarna2C.configure(fg_color="red", text_color="black", state="normal")

    # Warna3
    if ((globals()['V0148'] & 64) != 64) and globals()['V0146'] != 64:
        btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 64) == 64) and globals()['V0142'] != 64 and globals()['V0146'] != 64:
        btnAutoFeedWarna3C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 64) == 64) and globals()['V0142'] == 64 and globals()['V0146'] != 64:
        if globals()['FeederCWarna3Blinking']:
            btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna3C.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederCWarna3Blinking'] = not globals()['FeederCWarna3Blinking']
    elif globals()['V0146'] == 64:
        btnAutoFeedWarna3C.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna4
    if ((globals()['V0148'] & 32) != 32) and globals()['V0146'] != 32:
        btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 32) == 32) and globals()['V0142'] != 32 and globals()['V0146'] != 32:
        btnAutoFeedWarna4C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 32) == 32) and globals()['V0142'] == 32 and globals()['V0146'] != 32:
        if globals()['FeederCWarna4Blinking']:
            btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoFeedWarna4C.configure(fg_color="red", text_color="black", state="normal")
        globals()['FeederCWarna4Blinking'] = not globals()['FeederCWarna4Blinking']
    elif globals()['V0146'] == 32:
        btnAutoFeedWarna4C.configure(fg_color="red", text_color="black", state="normal")
    
    # BUTTON HOPPER C
    # Putih
    if ((globals()['V0148'] & 16) != 16) and globals()['V0147'] != 16:
        btnAutoHopperPutihC.configure(fg_color="light green", text_color="white", state="normal")
    elif ((globals()['V0148'] & 16) == 16) and globals()['V0143'] != 16 and globals()['V0147'] != 16:
        btnAutoHopperPutihC.configure(fg_color="lime", text_color="black", state="normal")
    elif ((globals()['V0148'] & 16) == 16) and globals()['V0143'] == 16 and globals()['V0147'] != 16:
        if globals()['HopperCPutihBlinking']:
            btnAutoHopperPutihC.configure(fg_color="light green", text_color="white", state="normal")
        else:
            btnAutoHopperPutihC.configure(fg_color="lime", text_color="black", state="normal")
        globals()['HopperCPutihBlinking'] = not globals()['HopperCPutihBlinking']
    elif globals()['V0147'] == 16:
        btnAutoHopperPutihC.configure(fg_color="lime", text_color="black", state="normal")
    
    # Warna1
    if ((globals()['V0148'] & 8) != 8) and globals()['V0147'] != 8:
        btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 8) == 8) and globals()['V0143'] != 8 and globals()['V0147'] != 8:
        btnAutoHopperWarna1C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 8) == 8) and globals()['V0143'] == 8 and globals()['V0147'] != 8:
        if globals()['HopperCWarna1Blinking']:
            btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoHopperWarna1C.configure(fg_color="red", text_color="black", state="normal")
        globals()['HopperCWarna1Blinking'] = not globals()['HopperCWarna1Blinking']
    elif globals()['V0147'] == 8:
        btnAutoHopperWarna1C.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna2
    if ((globals()['V0148'] & 4) != 4) and globals()['V0147'] != 4:
        btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 4) == 4) and globals()['V0143'] != 4 and globals()['V0147'] != 4:
        btnAutoHopperWarna2C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 4) == 4) and globals()['V0143'] == 4 and globals()['V0147'] != 4:
        if globals()['HopperCWarna2Blinking']:
            btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoHopperWarna2C.configure(fg_color="red", text_color="black", state="normal")
        globals()['HopperCWarna2Blinking'] = not globals()['HopperCWarna2Blinking']
    elif globals()['V0147'] == 4:
        btnAutoHopperWarna2C.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna3
    if ((globals()['V0148'] & 2) != 2) and globals()['V0147'] != 2:
        btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 2) == 2) and globals()['V0143'] != 2 and globals()['V0147'] != 2:
        btnAutoHopperWarna3C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 2) == 2) and globals()['V0143'] == 2 and globals()['V0147'] != 2:
        if globals()['HopperCWarna3Blinking']:
            btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoHopperWarna3C.configure(fg_color="red", text_color="black", state="normal")
        globals()['HopperCWarna3Blinking'] = not globals()['HopperCWarna3Blinking']
    elif globals()['V0147'] == 2:
        btnAutoHopperWarna3C.configure(fg_color="red", text_color="black", state="normal")
    
    # Warna4
    if ((globals()['V0148'] & 1) != 1) and globals()['V0147'] != 1:
        btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white", state="normal")
    elif ((globals()['V0148'] & 1) == 1) and globals()['V0143'] != 1 and globals()['V0147'] != 1:
        btnAutoHopperWarna4C.configure(fg_color="red", text_color="black", state="normal")
    elif ((globals()['V0148'] & 1) == 1) and globals()['V0143'] == 1 and globals()['V0147'] != 1:
        if globals()['HopperCWarna4Blinking']:
            btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white", state="normal")
        else:
            btnAutoHopperWarna4C.configure(fg_color="red", text_color="black", state="normal")
        globals()['HopperCWarna4Blinking'] = not globals()['HopperCWarna4Blinking']
    elif globals()['V0147'] == 1:
        btnAutoHopperWarna4C.configure(fg_color="red", text_color="black", state="normal")



    # ERROR MotorMatScrewCnvyrC0
    if not globals()['J00568'] and globals()['J00536']:
        frmCManMatScrewCnvyrLbl.configure(fg_color="orange")
        btnCAutoMotorMatScrewCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00568'] and globals()['J00536']:
        if globals()['CManMotorMatScrewCnvyrBlinking']:
            frmCManMatScrewCnvyrLbl.configure(fg_color="orange")
            btnCAutoMotorMatScrewCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManMatScrewCnvyrLbl.configure(fg_color=lightOrange)
            btnCAutoMotorMatScrewCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMotorMatScrewCnvyrBlinking'] = not globals()['CManMotorMatScrewCnvyrBlinking']
    else:
        frmCManMatScrewCnvyrLbl.configure(fg_color=lightOrange)
        btnCAutoMotorMatScrewCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")

    # Auto C MotorMatscrew Rev Fwd
    if globals()['I00213']:
        btnCAutoMotorMatScrewCnvyrDoRev.configure(fg_color="red", text_color="black")
    else:
        btnCAutoMotorMatScrewCnvyrDoRev.configure(fg_color="pink", text_color="white")
    
    if globals()['I00211']:
        btnCAutoMotorMatScrewCnvyrDoFwd.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorMatScrewCnvyrDoFwd.configure(fg_color="light green", text_color="white")

    # .btnMotorMatScrewCnvyrC Auto Besar C Page 2
    if not globals()['J00568'] and globals()['J00536']:
        btnMotorMatScrewCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00568'] and globals()['J00536']:
        if globals()['CManMotorMatScrewCnvyrBlinking']:
            btnMotorMatScrewCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMotorMatScrewCnvyrC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00213']:
        btnMotorMatScrewCnvyrC.configure(text="Rev", fg_color="red", text_color="black")
    elif globals()['I00211']:
        btnMotorMatScrewCnvyrC.configure(text="Fwd", fg_color="lime", text_color="black")
    else:
        btnMotorMatScrewCnvyrC.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # ERROR MateriVbratorC0
    if not globals()['J00567'] and globals()['J00535']:
        frmCManMateriVbratorLbl.configure(fg_color="orange")
        btnCAutoMotorMateriVbratorIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00567'] and globals()['J00535']:
        if globals()['CManMateriVbratorBlinking']:
            frmCManMateriVbratorLbl.configure(fg_color="orange")
            btnCAutoMotorMateriVbratorIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManMateriVbratorLbl.configure(fg_color=lightOrange)
            btnCAutoMotorMateriVbratorIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMateriVbratorBlinking'] = not globals()['CManMateriVbratorBlinking']
    else:
        frmCManMateriVbratorLbl.configure(fg_color=lightOrange)
        btnCAutoMotorMateriVbratorIsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00194']:
        btnCAutoMotorMateriVbratorDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorMateriVbratorDoStart.configure(fg_color="light green", text_color="white")
    
    # .btnMateriVbratorC / motor Osciliating Auto Besar C Page 2
    if not globals()['J00567'] and globals()['J00535']:
        btnMateriVbratorC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00567'] and globals()['J00535']:
        if globals()['CManMateriVbratorBlinking']:
            btnMateriVbratorC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMateriVbratorC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00194']:
        btnMateriVbratorC.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnMateriVbratorC.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # ERROR MotorToRotaryCnvyrC0
    if not globals()['J00569'] and globals()['J00537']:
        frmCManToRotaryCnvyrLbl.configure(fg_color="orange")
        btnCAutoMotorToRotaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00569'] and globals()['J00537']:
        if globals()['CManMotorToRotaryCnvyrBlinking']:
            frmCManToRotaryCnvyrLbl.configure(fg_color="orange")
            btnCAutoMotorToRotaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManToRotaryCnvyrLbl.configure(fg_color=lightOrange)
            btnCAutoMotorToRotaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMotorToRotaryCnvyrBlinking'] = not globals()['CManMotorToRotaryCnvyrBlinking']
    else:
        frmCManToRotaryCnvyrLbl.configure(fg_color=lightOrange)
        btnCAutoMotorToRotaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00228']:
        btnCAutoMotorToRotaryCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorToRotaryCnvyrDoStart.configure(fg_color="light green", text_color="white")
    
    # .btnMotorToRotaryCnvyrC  Auto Besar C Page 2
    if not globals()['J00569'] and globals()['J00537']:
        btnMotorToRotaryCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00569'] and globals()['J00537']:
        if globals()['CManMotorToRotaryCnvyrBlinking']:
            btnMotorToRotaryCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnMotorToRotaryCnvyrC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00228']:
        btnMotorToRotaryCnvyrC.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnMotorToRotaryCnvyrC.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # ERROR MotorFrmRtaryCnvyrC0
    if not globals()['J00570'] and globals()['J00538']:
        frmCManRtaryCnvyrLbl.configure(fg_color="orange")
        btnCAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00570'] and globals()['J00538']:
        if globals()['CManMotorFrmRtaryCnvyrBlinking']:
            frmCManRtaryCnvyrLbl.configure(fg_color="orange")
            btnCAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManRtaryCnvyrLbl.configure(fg_color=lightOrange)
            btnCAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMotorFrmRtaryCnvyrBlinking'] = not globals()['CManMotorFrmRtaryCnvyrBlinking']
    else:
        frmCManRtaryCnvyrLbl.configure(fg_color=lightOrange)
        btnCAutoMotorFrmRtaryCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00224']:
        btnCAutoMotorFrmRtaryCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorFrmRtaryCnvyrDoStart.configure(fg_color="light green", text_color="white")
    
    # .btnFrmRtaryCnvyrC  Auto Besar C Page 2
    if not globals()['J00570'] and globals()['J00538']:
        btnFrmRtaryCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00570'] and globals()['J00538']:
        if globals()['CManMotorFrmRtaryCnvyrBlinking']:
            btnFrmRtaryCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnFrmRtaryCnvyrC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00224']:
        btnFrmRtaryCnvyrC.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnFrmRtaryCnvyrC.configure(text="Fault", fg_color=lightOrange, text_color="white")

    # ERROR MotorUpLadderCnvyrC0
    if not globals()['J00571'] and globals()['J00539']:
        frmCManUpLadderCnvyrLbl.configure(fg_color="orange")
        btnCAutoMotorUpladderCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00571'] and globals()['J00539']:
        if globals()['CManMotorUpladderCnvyrBlinking']:
            frmCManUpLadderCnvyrLbl.configure(fg_color="orange")
            btnCAutoMotorUpladderCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManUpLadderCnvyrLbl.configure(fg_color=lightOrange)
            btnCAutoMotorUpladderCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMotorUpladderCnvyrBlinking'] = not globals()['CManMotorUpladderCnvyrBlinking']
    else:
        frmCManUpLadderCnvyrLbl.configure(fg_color=lightOrange)
        btnCAutoMotorUpladderCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00226']:
        btnCAutoMotorUpladderCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorUpladderCnvyrDoStart.configure(fg_color="light green", text_color="white")
    
    # .btnUpLadderCnvyrC / Incline Conveyor  Auto Besar C Page 2
    if not globals()['J00571'] and globals()['J00539']:
        btnUpLadderCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00571'] and globals()['J00539']:
        if globals()['CManMotorUpladderCnvyrBlinking']:
            btnUpLadderCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnUpLadderCnvyrC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00226']:
        btnUpLadderCnvyrC.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnUpLadderCnvyrC.configure(text="Fault", fg_color=lightOrange, text_color="white")
    
    # ERROR MotorToHopperCnvyrC0
    if not globals()['J00572'] and globals()['J00540']:
        frmCManToHopperCnvyrLbl.configure(fg_color="orange")
        btnCAutoMotorToHopperCnvyrIsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00572'] and globals()['J00540']:
        if globals()['CManMotorToHopperCnvyrBlinking']:
            frmCManToHopperCnvyrLbl.configure(fg_color="orange")
            btnCAutoMotorToHopperCnvyrIsFault.configure(fg_color="orange", text_color="black")
        else:
            frmCManToHopperCnvyrLbl.configure(fg_color=lightOrange)
            btnCAutoMotorToHopperCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManMotorToHopperCnvyrBlinking'] = not globals()['CManMotorToHopperCnvyrBlinking']
    else:
        frmCManToHopperCnvyrLbl.configure(fg_color=lightOrange)
        btnCAutoMotorToHopperCnvyrIsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00196']:
        btnCAutoMotorToHopperCnvyrDoStart.configure(fg_color="lime", text_color="black")
    else:
        btnCAutoMotorToHopperCnvyrDoStart.configure(fg_color="light green", text_color="white")
    
    # .btnToHopperCnvyrC / Convetor To Silo  Auto Besar C Page 2
    if not globals()['J00572'] and globals()['J00540']:
        btnToHopperCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00572'] and globals()['J00540']:
        if globals()['CManMotorToHopperCnvyrBlinking']:
            btnToHopperCnvyrC.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnToHopperCnvyrC.configure(fg_color=lightOrange, text="Fault")
    elif globals()['I00196']:
        btnToHopperCnvyrC.configure(text="Start", fg_color="lime", text_color="black")
    else:
        btnToHopperCnvyrC.configure(text="Fault", fg_color=lightOrange, text_color="white")
    
    
    
    # ERROR PneumTbletHoprDoorC0
    if not globals()['J00561'] and globals()['J00529']:
        frmManCTbletHoprDoor0Lbl.configure(fg_color="orange")
        btnCAutoPneumTbletHoprDoor0IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00561'] and globals()['J00529']:
        if globals()['CManPneumTbletHoprDoor0Blinking']:
            frmManCTbletHoprDoor0Lbl.configure(fg_color="orange")
            btnCAutoPneumTbletHoprDoor0IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManCTbletHoprDoor0Lbl.configure(fg_color=lightOrange)
            btnCAutoPneumTbletHoprDoor0IsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManPneumTbletHoprDoor0Blinking'] = not globals()['CManPneumTbletHoprDoor0Blinking']
    else:
        frmManCTbletHoprDoor0Lbl.configure(fg_color=lightOrange)
        btnCAutoPneumTbletHoprDoor0IsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00070']:   
        btnRedManCTbletHoprDoor0.configure(fg_color="Red")
        btnCAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00070'] and not globals()['I00214']:
        btnRedManCTbletHoprDoor0.configure(fg_color="pink")
        btnCAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00070'] and globals()['I00214']:
        if globals()['RedCManTbletHoprDoor0']:
            btnRedManCTbletHoprDoor0.configure(fg_color="pink")
            btnCAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="pink", text_color="white")
        else:
            btnRedManCTbletHoprDoor0.configure(fg_color="red")
            btnCAutoPneumTbletHoprDoor0IsOpen.configure(fg_color="Red", text_color="black")
        globals()['RedCManTbletHoprDoor0'] = not globals()['RedCManTbletHoprDoor0']

    if globals()['I00071']:
        btnGreenManCTbletHoprDoor0.configure(fg_color="lime")
        btnCAutoPneumTbletHoprDoor0IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00071'] and not globals()['I00215']:
        btnGreenManCTbletHoprDoor0.configure(fg_color="light green")
        btnCAutoPneumTbletHoprDoor0IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00071'] and globals()['I00215']:
        if globals()['GreenCManTbletHoprDoor0']:
            btnGreenManCTbletHoprDoor0.configure(fg_color="lime")
            btnCAutoPneumTbletHoprDoor0IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManCTbletHoprDoor0.configure(fg_color="light green")
            btnCAutoPneumTbletHoprDoor0IsClose.configure(fg_color="light green", text_color="white")
        globals()['GreenCManTbletHoprDoor0'] = not globals()['GreenCManTbletHoprDoor0']
    
    
    # .btnTbltHoprDoor0C / Door Silo 1  Auto Besar C Page 2
    if not globals()['J00561'] and globals()['J00529']:
        btnTbltHoprDoor0C.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00561'] and globals()['J00529']:
        if globals()['CManPneumTbletHoprDoor0Blinking']:
            btnTbltHoprDoor0C.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnTbltHoprDoor0C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00070']:   
        btnTbltHoprDoor0C.configure(fg_color="Red", text="Open", text_color="black")
    elif not globals()['I00070'] and globals()['I00214']:
        if globals()['RedCManTbletHoprDoor0']:
            btnTbltHoprDoor0C.configure(fg_color="pink", text="Open", text_color="white")
        else:
            btnTbltHoprDoor0C.configure(fg_color="Red", text="Open", text_color="black")
    elif globals()['I00071']:
        btnTbltHoprDoor0C.configure(fg_color="lime", text="Close", text_color="black")
    elif not globals()['I00071'] and globals()['I00215']:
        if globals()['GreenCManTbletHoprDoor0']:
            btnTbltHoprDoor0C.configure(fg_color="lime", text="Close", text_color="black")
        else:
            btnTbltHoprDoor0C.configure(fg_color="light green", text="Close", text_color="white")
    else:
        btnTbltHoprDoor0C.configure(fg_color=lightOrange, text="Fault", text_color="white")
 

    # ERROR PneumTbletHoprDoorC1
    if not globals()['J00562'] and globals()['J00530']:
        frmManCTbletHoprDoor1Lbl.configure(fg_color="orange")
        btnCAutoPneumTbletHoprDoor1IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00562'] and globals()['J00530']:
        if globals()['CManPneumTbletHoprDoor1Blinking']:
            frmManCTbletHoprDoor1Lbl.configure(fg_color="orange")
            btnCAutoPneumTbletHoprDoor1IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManCTbletHoprDoor1Lbl.configure(fg_color=lightOrange)
            btnCAutoPneumTbletHoprDoor1IsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManPneumTbletHoprDoor1Blinking'] = not globals()['CManPneumTbletHoprDoor1Blinking']
    else:
        frmManCTbletHoprDoor1Lbl.configure(fg_color=lightOrange)
        btnCAutoPneumTbletHoprDoor1IsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00072']:   
        btnRedManCTbletHoprDoor1.configure(fg_color="Red")
        btnCAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00072'] and not globals()['I00216']:
        btnRedManCTbletHoprDoor1.configure(fg_color="pink")
        btnCAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00072'] and globals()['I00216']:
        if globals()['RedCManTbletHoprDoor1']:
            btnRedManCTbletHoprDoor1.configure(fg_color="pink")
            btnCAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="pink", text_color="white")
        else:
            btnRedManCTbletHoprDoor1.configure(fg_color="red")
            btnCAutoPneumTbletHoprDoor1IsOpen.configure(fg_color="Red", text_color="black")
        globals()['RedCManTbletHoprDoor1'] = not globals()['RedCManTbletHoprDoor1']

    if globals()['I00073']:
        btnGreenManCTbletHoprDoor1.configure(fg_color="lime")
        btnCAutoPneumTbletHoprDoor1IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00073'] and not globals()['I00217']:
        btnGreenManCTbletHoprDoor1.configure(fg_color="light green")
        btnCAutoPneumTbletHoprDoor1IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00073'] and globals()['I00217']:
        if globals()['GreenCManTbletHoprDoor1']:
            btnGreenManCTbletHoprDoor1.configure(fg_color="lime")
            btnCAutoPneumTbletHoprDoor1IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManCTbletHoprDoor1.configure(fg_color="light green")
            btnCAutoPneumTbletHoprDoor1IsClose.configure(fg_color="light green", text_color="white")
        globals()['GreenCManTbletHoprDoor1'] = not globals()['GreenCManTbletHoprDoor1']

    # .btnTbltHoprDoor1C / Door Silo 2  Auto Besar C Page 2
    if not globals()['J00562'] and globals()['J00530']:
        btnTbltHoprDoor1C.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00562'] and globals()['J00530']:
        if globals()['CManPneumTbletHoprDoor1Blinking']:
            btnTbltHoprDoor1C.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnTbltHoprDoor1C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00072']:   
        btnTbltHoprDoor1C.configure(fg_color="Red", text="Open", text_color="black")
    elif not globals()['I00072'] and globals()['I00216']:
        if globals()['RedCManTbletHoprDoor1']:
            btnTbltHoprDoor1C.configure(fg_color="pink", text="Open", text_color="white")
        else:
            btnTbltHoprDoor1C.configure(fg_color="Red", text="Open", text_color="black")
    elif globals()['I00073']:
        btnTbltHoprDoor1C.configure(fg_color="lime", text="Close", text_color="black")
    elif not globals()['I00073'] and globals()['I00217']:
        if globals()['GreenCManTbletHoprDoor1']:
            btnTbltHoprDoor1C.configure(fg_color="lime", text="Close", text_color="black")
        else:
            btnTbltHoprDoor1C.configure(fg_color="light green", text="Close", text_color="white")
    else:
        btnTbltHoprDoor1C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    
    
    # ERROR PneumTbletHoprDoorC2
    if not globals()['J00563'] and globals()['J00531']:
        frmManCTbletHoprDoor2Lbl.configure(fg_color="orange")
        btnCAutoPneumTbletHoprDoor2IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00563'] and globals()['J00531']:
        if globals()['CManPneumTbletHoprDoor2Blinking']:
            frmManCTbletHoprDoor2Lbl.configure(fg_color="orange")
            btnCAutoPneumTbletHoprDoor2IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManCTbletHoprDoor2Lbl.configure(fg_color=lightOrange)
            btnCAutoPneumTbletHoprDoor2IsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManPneumTbletHoprDoor2Blinking'] = not globals()['CManPneumTbletHoprDoor2Blinking']
    else:
        frmManCTbletHoprDoor2Lbl.configure(fg_color=lightOrange)
        btnCAutoPneumTbletHoprDoor2IsFault.configure(fg_color=lightOrange, text_color="white")
    
    if globals()['I00074']:   
        btnRedManCTbletHoprDoor2.configure(fg_color="Red")
        btnCAutoPneumTbletHoprDoor2IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00074'] and not globals()['I00218']:
        btnRedManCTbletHoprDoor2.configure(fg_color="pink")
        btnCAutoPneumTbletHoprDoor2IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00074'] and globals()['I00218']:
        if globals()['RedCManTbletHoprDoor2']:
            btnRedManCTbletHoprDoor2.configure(fg_color="pink")
            btnCAutoPneumTbletHoprDoor2IsOpen.configure(fg_color="pink", text_color="white")
        else:
            btnRedManCTbletHoprDoor2.configure(fg_color="red")
            btnCAutoPneumTbletHoprDoor2IsOpen.configure(fg_color="Red", text_color="black")
        globals()['RedCManTbletHoprDoor2'] = not globals()['RedCManTbletHoprDoor2']

    if globals()['I00075']:
        btnGreenManCTbletHoprDoor2.configure(fg_color="lime")
        btnCAutoPneumTbletHoprDoor2IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00075'] and not globals()['I00219']:
        btnGreenManCTbletHoprDoor2.configure(fg_color="light green")
        btnCAutoPneumTbletHoprDoor2IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00075'] and globals()['I00219']:
        if globals()['GreenCManTbletHoprDoor2']:
            btnGreenManCTbletHoprDoor2.configure(fg_color="lime")
            btnCAutoPneumTbletHoprDoor2IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManCTbletHoprDoor2.configure(fg_color="light green")
            btnCAutoPneumTbletHoprDoor2IsClose.configure(fg_color="light green", text_color="white")
        globals()['GreenCManTbletHoprDoor2'] = not globals()['GreenCManTbletHoprDoor2']
    
    # .btnTbltHoprDoor2C / Door Silo 3  Auto Besar C Page 2
    if not globals()['J00563'] and globals()['J00531']:
        btnTbltHoprDoor2C.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00563'] and globals()['J00531']:
        if globals()['CManPneumTbletHoprDoor2Blinking']:
            btnTbltHoprDoor2C.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnTbltHoprDoor2C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00074']:   
        btnTbltHoprDoor2C.configure(fg_color="Red", text="Open", text_color="black")
    elif not globals()['I00074'] and globals()['I00218']:
        if globals()['RedCManTbletHoprDoor2']:
            btnTbltHoprDoor2C.configure(fg_color="pink", text="Open", text_color="white")
        else:
            btnTbltHoprDoor2C.configure(fg_color="Red", text="Open", text_color="black")
    elif globals()['I00075']:
        btnTbltHoprDoor2C.configure(fg_color="lime", text="Close", text_color="black")
    elif not globals()['I00075'] and globals()['I00219']:
        if globals()['GreenCManTbletHoprDoor2']:
            btnTbltHoprDoor2C.configure(fg_color="lime", text="Close", text_color="black")
        else:
            btnTbltHoprDoor2C.configure(fg_color="light green", text="Close", text_color="white")
    else:
        btnTbltHoprDoor2C.configure(fg_color=lightOrange, text="Fault", text_color="white")  
    

    # ERROR PneumTbletHoprDoorC3
    if not globals()['J00564'] and globals()['J00532']:
        frmManCTbletHoprDoor3Lbl.configure(fg_color="orange")
        btnCAutoPneumTbletHoprDoor3IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00564'] and globals()['J00532']:
        if globals()['CManPneumTbletHoprDoor3Blinking']:
            frmManCTbletHoprDoor3Lbl.configure(fg_color="orange")
            btnCAutoPneumTbletHoprDoor3IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManCTbletHoprDoor3Lbl.configure(fg_color=lightOrange)
            btnCAutoPneumTbletHoprDoor3IsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManPneumTbletHoprDoor3Blinking'] = not globals()['CManPneumTbletHoprDoor3Blinking']
    else:
        frmManCTbletHoprDoor3Lbl.configure(fg_color=lightOrange)
        btnCAutoPneumTbletHoprDoor3IsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00076']:   
        btnRedManCTbletHoprDoor3.configure(fg_color="Red")
        btnCAutoPneumTbletHoprDoor3IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00076'] and not globals()['I00220']:
        btnRedManCTbletHoprDoor3.configure(fg_color="pink")
        btnCAutoPneumTbletHoprDoor3IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00076'] and globals()['I00220']:
        if globals()['RedCManTbletHoprDoor3']:
            btnRedManCTbletHoprDoor3.configure(fg_color="pink")
            btnCAutoPneumTbletHoprDoor3IsOpen.configure(fg_color="pink", text_color="white")
        else:
            btnRedManCTbletHoprDoor3.configure(fg_color="red")
            btnCAutoPneumTbletHoprDoor3IsOpen.configure(fg_color="Red", text_color="black")
        globals()['RedCManTbletHoprDoor3'] = not globals()['RedCManTbletHoprDoor3']

    if globals()['I00077']:
        btnGreenManCTbletHoprDoor3.configure(fg_color="lime")
        btnCAutoPneumTbletHoprDoor3IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00077'] and not globals()['I00221']:
        btnGreenManCTbletHoprDoor3.configure(fg_color="light green")
        btnCAutoPneumTbletHoprDoor3IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00077'] and globals()['I00221']:
        if globals()['GreenCManTbletHoprDoor3']:
            btnGreenManCTbletHoprDoor3.configure(fg_color="lime")
            btnCAutoPneumTbletHoprDoor3IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManCTbletHoprDoor3.configure(fg_color="light green")
            btnCAutoPneumTbletHoprDoor3IsClose.configure(fg_color="light green", text_color="white")
        globals()['GreenCManTbletHoprDoor3'] = not globals()['GreenCManTbletHoprDoor3']
    
    # .btnTbltHoprDoor3C / Door Silo 4  Auto Besar C Page 2
    if not globals()['J00564'] and globals()['J00532']:
        btnTbltHoprDoor3C.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00564'] and globals()['J00532']:
        if globals()['CManPneumTbletHoprDoor3Blinking']:
            btnTbltHoprDoor3C.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnTbltHoprDoor3C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00076']:   
        btnTbltHoprDoor3C.configure(fg_color="Red", text="Open", text_color="black")
    elif not globals()['I00076'] and globals()['I00220']:
        if globals()['RedCManTbletHoprDoor3']:
            btnTbltHoprDoor3C.configure(fg_color="pink", text="Open", text_color="white")
        else:
            btnTbltHoprDoor3C.configure(fg_color="Red", text="Open", text_color="black")
    elif globals()['I00077']:
        btnTbltHoprDoor3C.configure(fg_color="lime", text="Close", text_color="black")
    elif not globals()['I00077'] and globals()['I00221']:
        if globals()['GreenCManTbletHoprDoor3']:
            btnTbltHoprDoor3C.configure(fg_color="lime", text="Close", text_color="black")
        else:
            btnTbltHoprDoor3C.configure(fg_color="light green", text="Close", text_color="white")
    else:
        btnTbltHoprDoor3C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    
    
    # ERROR PneumTbletHoprDoorC4
    if not globals()['J00565'] and globals()['J00533']:
        frmManCTbletHoprDoor4Lbl.configure(fg_color="orange")
        btnCAutoPneumTbletHoprDoor4IsFault.configure(fg_color="orange", text_color="black")
    elif globals()['J00565'] and globals()['J00533']:
        if globals()['CManPneumTbletHoprDoor4Blinking']:
            frmManCTbletHoprDoor4Lbl.configure(fg_color="orange")
            btnCAutoPneumTbletHoprDoor4IsFault.configure(fg_color="orange", text_color="black")
        else:
            frmManCTbletHoprDoor4Lbl.configure(fg_color=lightOrange)
            btnCAutoPneumTbletHoprDoor4IsFault.configure(fg_color=lightOrange, text_color="white")
        globals()['CManPneumTbletHoprDoor4Blinking'] = not globals()['CManPneumTbletHoprDoor4Blinking']
    else:
        frmManCTbletHoprDoor4Lbl.configure(fg_color=lightOrange)
        btnCAutoPneumTbletHoprDoor4IsFault.configure(fg_color=lightOrange, text_color="white")

    if globals()['I00078']:   
        btnRedManCTbletHoprDoor4.configure(fg_color="Red")
        btnCAutoPneumTbletHoprDoor4IsOpen.configure(fg_color="Red", text_color="black")
    elif not globals()['I00078'] and not globals()['I00222']:
        btnRedManCTbletHoprDoor4.configure(fg_color="pink")
        btnCAutoPneumTbletHoprDoor4IsOpen.configure(fg_color="pink", text_color="white")
    elif not globals()['I00078'] and globals()['I00222']:
        if globals()['RedCManTbletHoprDoor4']:
            btnRedManCTbletHoprDoor4.configure(fg_color="pink")
            btnCAutoPneumTbletHoprDoor4IsOpen.configure(fg_color="pink", text_color="white")
        else:
            btnRedManCTbletHoprDoor4.configure(fg_color="red")
            btnCAutoPneumTbletHoprDoor4IsOpen.configure(fg_color="Red", text_color="black")
        globals()['RedCManTbletHoprDoor4'] = not globals()['RedCManTbletHoprDoor4']

    if globals()['I00079']:
        btnGreenManCTbletHoprDoor4.configure(fg_color="lime")
        btnCAutoPneumTbletHoprDoor4IsClose.configure(fg_color="lime", text_color="black")
    elif not globals()['I00079'] and not globals()['I00223']:
        btnGreenManCTbletHoprDoor4.configure(fg_color="light green")
        btnCAutoPneumTbletHoprDoor4IsClose.configure(fg_color="light green", text_color="white")
    elif not globals()['I00079'] and globals()['I00223']:
        if globals()['GreenCManTbletHoprDoor4']:
            btnGreenManCTbletHoprDoor4.configure(fg_color="lime")
            btnCAutoPneumTbletHoprDoor4IsClose.configure(fg_color="lime", text_color="black")
        else:
            btnGreenManCTbletHoprDoor4.configure(fg_color="light green")
            btnCAutoPneumTbletHoprDoor4IsClose.configure(fg_color="light green", text_color="white")
        globals()['GreenCManTbletHoprDoor4'] = not globals()['GreenCManTbletHoprDoor4']
    
    # .btnTbltHoprDoor4C / Door Silo 5  Auto Besar C Page 2
    if not globals()['J00565'] and globals()['J00533']:
        btnTbltHoprDoor4C.configure(fg_color="orange", text="Fault", text_color="black")
    elif globals()['J00565'] and globals()['J00533']:
        if globals()['CManPneumTbletHoprDoor4Blinking']:
            btnTbltHoprDoor4C.configure(fg_color="orange", text="Fault", text_color="black")
        else:
            btnTbltHoprDoor4C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    elif globals()['I00078']:   
        btnTbltHoprDoor4C.configure(fg_color="Red", text="Open", text_color="black")
    elif not globals()['I00078'] and globals()['I00222']:
        if globals()['RedCManTbletHoprDoor4']:
            btnTbltHoprDoor4C.configure(fg_color="pink", text="Open", text_color="white")
        else:
            btnTbltHoprDoor4C.configure(fg_color="Red", text="Open", text_color="black")
    elif globals()['I00079']:
        btnTbltHoprDoor4C.configure(fg_color="lime", text="Close", text_color="black")
    elif not globals()['I00079'] and globals()['I00223']:
        if globals()['GreenCManTbletHoprDoor4']:
            btnTbltHoprDoor4C.configure(fg_color="lime", text="Close", text_color="black")
        else:
            btnTbltHoprDoor4C.configure(fg_color="light green", text="Close", text_color="white")
    else:
        btnTbltHoprDoor4C.configure(fg_color=lightOrange, text="Fault", text_color="white")
    

    # SENSOR RtaryUnitHop0  .herea
    if globals()['I00080']:
        if not globals()['J00208']:
            if globals()['CManRtaryUnitHop0Blinking']:
                frmnCManRtaryUnitHop0.configure(fg_color="yellow")
                btnCAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop0C.configure(fg_color="yellow", text_color="black")
            else:
                frmnCManRtaryUnitHop0.configure(fg_color="light yellow")
                btnCAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop0C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRtaryUnitHop0Blinking'] = not globals()['CManRtaryUnitHop0Blinking']
        elif globals()['J00208']:
            frmnCManRtaryUnitHop0.configure(fg_color="yellow")
            btnCAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop0C.configure(fg_color="yellow", text_color="black")
    else:
        frmnCManRtaryUnitHop0.configure(fg_color="light yellow")
        btnCAutoPneumSensorRtaryUnitHop0IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop0C.configure(fg_color="light yellow", text_color="white")
    
    
    # SENSOR RtaryUnitHop1
    if globals()['I00081']:
        if not globals()['J00209']:
            if globals()['CManRtaryUnitHop1Blinking']:
                frmnCManRtaryUnitHop1.configure(fg_color="yellow")
                btnCAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop1C.configure(fg_color="yellow", text_color="black")
            else:
                frmnCManRtaryUnitHop1.configure(fg_color="light yellow")
                btnCAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop1C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRtaryUnitHop1Blinking'] = not globals()['CManRtaryUnitHop1Blinking']
        elif globals()['J00209']:
            frmnCManRtaryUnitHop1.configure(fg_color="yellow")
            btnCAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop1C.configure(fg_color="yellow", text_color="black")
    else:
        frmnCManRtaryUnitHop1.configure(fg_color="light yellow")
        btnCAutoPneumSensorRtaryUnitHop1IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop1C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR RtaryUnitHop2
    if globals()['I00082']:
        if not globals()['J00210']:
            if globals()['CManRtaryUnitHop2Blinking']:
                frmnCManRtaryUnitHop2.configure(fg_color="yellow")
                btnCAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="yellow", text_color="black")
                btnRtaryUnitHop3C.configure(fg_color="yellow", text_color="black")
            else:
                frmnCManRtaryUnitHop2.configure(fg_color="light yellow")
                btnCAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="light yellow", text_color="white")
                btnRtaryUnitHop3C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRtaryUnitHop2Blinking'] = not globals()['CManRtaryUnitHop2Blinking']
        elif globals()['J00210']:
            frmnCManRtaryUnitHop2.configure(fg_color="yellow")
            btnCAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="yellow", text_color="black")
            btnRtaryUnitHop3C.configure(fg_color="yellow", text_color="black")
    else:
        frmnCManRtaryUnitHop2.configure(fg_color="light yellow")
        btnCAutoPneumSensorRtaryUnitHop2IsOn.configure(fg_color="light yellow", text_color="white")
        btnRtaryUnitHop3C.configure(fg_color="light yellow", text_color="white")

    # SENSOR TabletVaryHop0
    if globals()['I00086']:
        if not globals()['J00203']:
            if globals()['CManTabletVaryHop0Blinking']:
                frmnCManTabletVaryHop0.configure(fg_color="yellow")
                btnCAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="yellow", text_color="black")
                btnTabletVaryHop0C.configure(fg_color="yellow", text_color="black")
            else:
                frmnCManTabletVaryHop0.configure(fg_color="light yellow")
                btnCAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="light yellow", text_color="white")
                btnTabletVaryHop0C.configure(fg_color="light yellow", text_color="white")
            globals()['CManTabletVaryHop0Blinking'] = not globals()['CManTabletVaryHop0Blinking']
        elif globals()['J00203']:
            frmnCManTabletVaryHop0.configure(fg_color="yellow")
            btnCAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="yellow", text_color="black")
            btnTabletVaryHop0C.configure(fg_color="yellow", text_color="black")
    else:
        frmnCManTabletVaryHop0.configure(fg_color="light yellow")
        btnCAutoPneumSensorTabletVaryHop0IsOn.configure(fg_color="light yellow", text_color="white")
        btnTabletVaryHop0C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR TabletVaryHop1
    if globals()['I00087']:
        if not globals()['J00204']:
            if globals()['CManTabletVaryHop1Blinking']:
                frmnCManTabletVaryHop1.configure(fg_color="yellow")
                btnCAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="yellow", text_color="black")
                btnTabletVaryHop1C.configure(fg_color="yellow", text_color="black")
            else:
                frmnCManTabletVaryHop1.configure(fg_color="light yellow")
                btnCAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="light yellow", text_color="white")
                btnTabletVaryHop1C.configure(fg_color="light yellow", text_color="white")
            globals()['CManTabletVaryHop1Blinking'] = not globals()['CManTabletVaryHop1Blinking']
        elif globals()['J00204']:
            frmnCManTabletVaryHop1.configure(fg_color="yellow")
            btnCAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="yellow", text_color="black")
            btnTabletVaryHop1C.configure(fg_color="yellow", text_color="black")
    else:
        frmnCManTabletVaryHop1.configure(fg_color="light yellow")
        btnCAutoPneumSensorTabletVaryHop1IsOn.configure(fg_color="light yellow", text_color="white")
        btnTabletVaryHop1C.configure(fg_color="light yellow", text_color="white")

    # SENSOR TabletVaryHop2
    if globals()['I00088']:
        if not globals()['J00205']:
            if globals()['CManTabletVaryHop2Blinking']:
                frmnManCTabletVaryHop2.configure(fg_color="yellow")
                btnCAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="yellow", text_color="black")
                btnTabletVaryHop2C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCTabletVaryHop2.configure(fg_color="light yellow")
                btnCAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="light yellow", text_color="white")
                btnTabletVaryHop2C.configure(fg_color="light yellow", text_color="white")
            globals()['CManTabletVaryHop2Blinking'] = not globals()['CManTabletVaryHop2Blinking']
        elif globals()['J00205']:
            frmnManCTabletVaryHop2.configure(fg_color="yellow")
            btnCAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="yellow", text_color="black")
            btnTabletVaryHop2C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCTabletVaryHop2.configure(fg_color="light yellow")
        btnCAutoPneumSensorTabletVaryHop2IsOn.configure(fg_color="light yellow", text_color="white")
        btnTabletVaryHop2C.configure(fg_color="light yellow", text_color="white")

    # SENSOR TabletVaryHop3
    if globals()['I00089']:
        if not globals()['J00206']:
            if globals()['CManTabletVaryHop3Blinking']:
                frmnManCTabletVaryHop3.configure(fg_color="yellow")
                btnCAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="yellow", text_color="black")
                btnTabletVaryHop3C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCTabletVaryHop3.configure(fg_color="light yellow")
                btnCAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="light yellow", text_color="white")
                btnTabletVaryHop3C.configure(fg_color="light yellow", text_color="white")
            globals()['CManTabletVaryHop3Blinking'] = not globals()['CManTabletVaryHop3Blinking']
        elif globals()['J00206']:
            frmnManCTabletVaryHop3.configure(fg_color="yellow")
            btnCAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="yellow", text_color="black")
            btnTabletVaryHop3C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCTabletVaryHop3.configure(fg_color="light yellow")
        btnCAutoPneumSensorTabletVaryHop3IsOn.configure(fg_color="light yellow", text_color="white")
        btnTabletVaryHop3C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR TabletVaryHop4
    if globals()['I00090']:
        if not globals()['J00207']:
            if globals()['CManTabletVaryHop4Blinking']:
                frmnManCTabletVaryHop4.configure(fg_color="yellow")
                btnCAutoPneumSensorTabletVaryHop4IsOn.configure(fg_color="yellow", text_color="black")
                btnTabletVaryHop4C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCTabletVaryHop4.configure(fg_color="light yellow")
                btnCAutoPneumSensorTabletVaryHop4IsOn.configure(fg_color="light yellow", text_color="white")
                btnTabletVaryHop4C.configure(fg_color="light yellow", text_color="white")
            globals()['CManTabletVaryHop4Blinking'] = not globals()['CManTabletVaryHop4Blinking']
        elif globals()['J00207']:
            frmnManCTabletVaryHop4.configure(fg_color="yellow")
            btnCAutoPneumSensorTabletVaryHop4IsOn.configure(fg_color="yellow", text_color="black")
            btnTabletVaryHop4C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCTabletVaryHop4.configure(fg_color="light yellow")
        btnCAutoPneumSensorTabletVaryHop4IsOn.configure(fg_color="light yellow", text_color="white")
        btnTabletVaryHop4C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR RncenMachHop0
    if globals()['I00091']:
        if not globals()['J00198']:
            if globals()['CManRncenMachHop0Blinking']:
                frmnManCRncenMachHop0.configure(fg_color="yellow")
                btnCAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop0C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCRncenMachHop0.configure(fg_color="light yellow")
                btnCAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop0C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRncenMachHop0Blinking'] = not globals()['CManRncenMachHop0Blinking']
        elif globals()['J00198']:
            frmnManCRncenMachHop0.configure(fg_color="yellow")
            btnCAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop0C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCRncenMachHop0.configure(fg_color="light yellow")
        btnCAutoPneumSensorRncenMachHop0IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop0C.configure(fg_color="light yellow", text_color="white")

    # SENSOR RncenMachHop1
    if globals()['I00092']:
        if not globals()['J00199']:
            if globals()['CManRncenMachHop1Blinking']:
                frmnManCRncenMachHop1.configure(fg_color="yellow")
                btnCAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop1C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCRncenMachHop1.configure(fg_color="light yellow")
                btnCAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop1C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRncenMachHop1Blinking'] = not globals()['CManRncenMachHop1Blinking']
        elif globals()['J00199']:
            frmnManCRncenMachHop1.configure(fg_color="yellow")
            btnCAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop1C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCRncenMachHop1.configure(fg_color="light yellow")
        btnCAutoPneumSensorRncenMachHop1IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop1C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR RncenMachHop2
    if globals()['I00093']:
        if not globals()['J00200']:
            if globals()['CManRncenMachHop2Blinking']:
                frmnManCRncenMachHop2.configure(fg_color="yellow")
                btnCAutoPneumSensorRncenMachHop2IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop2C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCRncenMachHop2.configure(fg_color="light yellow")
                btnCAutoPneumSensorRncenMachHop2IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop2C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRncenMachHop2Blinking'] = not globals()['CManRncenMachHop2Blinking']
        elif globals()['J00200']:
            frmnManCRncenMachHop2.configure(fg_color="yellow")
            btnCAutoPneumSensorRncenMachHop2IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop2C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCRncenMachHop2.configure(fg_color="light yellow")
        btnCAutoPneumSensorRncenMachHop2IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop2C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR RncenMachHop3
    if globals()['I00094']:
        if not globals()['J00201']:
            if globals()['CManRncenMachHop3Blinking']:
                frmnManCRncenMachHop3.configure(fg_color="yellow")
                btnCAutoPneumSensorRncenMachHop3IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop3C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCRncenMachHop3.configure(fg_color="light yellow")
                btnCAutoPneumSensorRncenMachHop3IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop3C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRncenMachHop3Blinking'] = not globals()['CManRncenMachHop3Blinking']
        elif globals()['J00201']:
            frmnManCRncenMachHop3.configure(fg_color="yellow")
            btnCAutoPneumSensorRncenMachHop3IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop3C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCRncenMachHop3.configure(fg_color="light yellow")
        btnCAutoPneumSensorRncenMachHop3IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop3C.configure(fg_color="light yellow", text_color="white")
    
    # SENSOR RncenMachHop4
    if globals()['I00095']:
        if not globals()['J00202']:
            if globals()['CManRncenMachHop4Blinking']:
                frmnManCRncenMachHop4.configure(fg_color="yellow")
                btnCAutoPneumSensorRncenMachHop4IsOn.configure(fg_color="yellow", text_color="black")
                btnTbltVaryHop4C.configure(fg_color="yellow", text_color="black")
            else:
                frmnManCRncenMachHop4.configure(fg_color="light yellow")
                btnCAutoPneumSensorRncenMachHop4IsOn.configure(fg_color="light yellow", text_color="white")
                btnTbltVaryHop4C.configure(fg_color="light yellow", text_color="white")
            globals()['CManRncenMachHop4Blinking'] = not globals()['CManRncenMachHop4Blinking']
        elif globals()['J00202']:
            frmnManCRncenMachHop4.configure(fg_color="yellow")
            btnCAutoPneumSensorRncenMachHop4IsOn.configure(fg_color="yellow", text_color="black")
            btnTbltVaryHop4C.configure(fg_color="yellow", text_color="black")
    else:
        frmnManCRncenMachHop4.configure(fg_color="light yellow")
        btnCAutoPneumSensorRncenMachHop4IsOn.configure(fg_color="light yellow", text_color="white")
        btnTbltVaryHop4C.configure(fg_color="light yellow", text_color="white")


    if globals()['I00231']:
        btnGreenCManToRotaryCnvyr0.configure(fg_color="lime")
        btnCAutoPneumToRotaryCnvyr0DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr0C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToRotaryCnvyr0.configure(fg_color="light green")
        btnCAutoPneumToRotaryCnvyr0DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr0C.configure(fg_color="light green", text_color="white")
    
    if globals()['I00233']:
        btnGreenCManToRotaryCnvyr1.configure(fg_color="lime")
        btnCAutoPneumToRotaryCnvyr1DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr1C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToRotaryCnvyr1.configure(fg_color="light green")
        btnCAutoPneumToRotaryCnvyr1DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr1C.configure(fg_color="light green", text_color="white")
    
    if globals()['I00235']:
        btnGreenCManToRotaryCnvyr2.configure(fg_color="lime")
        btnCAutoPneumToRotaryCnvyr2DoClose.configure(fg_color="lime", text_color="black")
        btnToRotaryCnvyr2C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToRotaryCnvyr2.configure(fg_color="light green")
        btnCAutoPneumToRotaryCnvyr2DoClose.configure(fg_color="light green", text_color="white")
        btnToRotaryCnvyr2C.configure(fg_color="light green", text_color="white")

    if globals()['I00199']:
        btnGreenCManToHopperCnvyr0.configure(fg_color="lime")
        btnCAutoPneumToHopperCnvyr0DoClose.configure(fg_color="lime", text_color="black")
        btnToHopperCnvyr0C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToHopperCnvyr0.configure(fg_color="light green")
        btnCAutoPneumToHopperCnvyr0DoClose.configure(fg_color="light green", text_color="white")
        btnToHopperCnvyr0C.configure(fg_color="light green", text_color="white")
    
    if globals()['I00201']:
        btnGreenCManToHopperCnvyr1.configure(fg_color="lime")
        btnCAutoPneumToHopperCnvyr1DoClose.configure(fg_color="lime", text_color="black")
        btnToHopperCnvyr1C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToHopperCnvyr1.configure(fg_color="light green")
        btnCAutoPneumToHopperCnvyr1DoClose.configure(fg_color="light green", text_color="white")
        btnToHopperCnvyr1C.configure(fg_color="light green", text_color="white")

    if globals()['I00203']:
        btnGreenCManToHopperCnvyr2.configure(fg_color="lime")
        btnCAutoPneumToHopperCnvyr2DoClose.configure(fg_color="lime", text_color="black")
        btnToHopperCnvyr2C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToHopperCnvyr2.configure(fg_color="light green")
        btnCAutoPneumToHopperCnvyr2DoClose.configure(fg_color="light green", text_color="white")
        btnToHopperCnvyr2C.configure(fg_color="light green", text_color="white")
    
    if globals()['I00205']:
        btnGreenCManToHopperCnvyr3.configure(fg_color="lime")
        btnCAutoPneumToHopperCnvyr3DoClose.configure(fg_color="lime", text_color="black")
        btnToHopperCnvyr3C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToHopperCnvyr3.configure(fg_color="light green")
        btnCAutoPneumToHopperCnvyr3DoClose.configure(fg_color="light green", text_color="white")
        btnToHopperCnvyr3C.configure(fg_color="light green", text_color="white")
    
    if globals()['I00207']:
        btnGreenCManToHopperCnvyr4.configure(fg_color="lime")
        btnCAutoPneumToHopperCnvyr4DoClose.configure(fg_color="lime", text_color="black")
        btnToHopperCnvyr4C.configure(fg_color="lime", text_color="black")
    else:
        btnGreenCManToHopperCnvyr4.configure(fg_color="light green")
        btnCAutoPneumToHopperCnvyr4DoClose.configure(fg_color="light green", text_color="white")
        btnToHopperCnvyr4C.configure(fg_color="light green", text_color="white")


    
    # if loopAllButtonFalse:

    #     btnRedCManMixerLineB.configure(fg_color="red")
    #     btnGreenCManMixerLineB.configure(fg_color="lime")


    #     collection.update_one(
    #         {'_id': ObjectId(objID)},
    #         {'$set': {
    #             # LINE Z
    #             'J00046': False,
    #             'J00047': False,
    #             'J00048': False,
    #             'J00057': False,
    #             'J00037': False,
    #             'J00058': False,
    #             'J00038': False,
    #             # LINE B
    #             'J00000': False,
    #             'J00001': False,
    #             'J00002': False,
    #             'J00003': False,
    #             'J00004': False,
    #             'J00016': False,
    #             'J00017': False,
    #             'J00005': False,
    #             'J00032': False,
    #             'J00033': False,
    #             'J00018': False,
    #             'J00031': False,
    #             'J00034': False,
    #             'J00006': False,
    #             'J00007': False,
    #             'J00008': False,
    #             'J00009': False,
    #             'J00010': False,
    #             'J00011': False,
    #             'J00012': False,
    #             'J00013': False,
    #             'J00014': False,
    #             'J00015': False,
    #             'J00019': False,
    #             'J00020': False,
    #             'J00021': False,
    #             'J00022': False,
    #             'J00023': False,
    #             'J00024': False,
    #             'J00025': False,
    #             'J00026': False,
    #             'J00027': False,
    #             'J00028': False,
    #             'J00029': False,
    #             'J00030': False,
    #             'J00035': False,
    #             'J00036': False,
    #             # LINE C
    #             'J00059': False,
    #             'J00060': False,
    #             'J00061': False,
    #             'J00062': False,
    #             'J00063': False,
    #             'J00065': False,
    #             'J00067': False,
    #             'J00069': False,
    #             'J00070': False,
    #             'J00071': False,
    #             'J00072': False,
    #             'J00073': False,
    #             'J00074': False,
    #             'J00075': False,
    #             'J00076': False,
    #             'J00077': False,
    #             'J00078': False,
    #             'J00079': False,
    #             'J00080': False,
    #             'J00081': False,
    #             'J00082': False,
    #             'J00083': False,
    #             'J00084': False,
    #             'J00085': False,
    #             'J00087': False,
    #             'J00089': False,
    #             'J00091': False,
    #             'J00093': False,
    #             'J00095': False
    #         }})

    # print('End refresh')

    app.after(200, refreshGUI)

# ================================================================================
# END GENERAL FUNCTION
# ================================================================================


# ================================================================================
# SET FUNCTION - .setfunc
# ================================================================================
def on_click(button):
    if button.cget("fg_color") == "lightblue":
        button.configure(fg_color="darkblue")
        button.configure(text_color="white")
    else:
        button.configure(fg_color="lightblue")
        button.configure(text_color="black")

    # Fungsi untuk menangani naik dan turun angka

def saveAllSetNumber():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            # 'V0000' : globals['V0000'],
            # 'V0001' : globals['V0001'],
            # 'V0002' : globals['V0002'],
            # 'V0016' : globals['V0016'],
            # 'V0017' : globals['V0017'],
            # 'V0018' : globals['V0018'],
            # 'V0019' : globals['V0019'],
            # 'V0020' : globals['V0020'],
            # 'V0021' : globals['V0021'],
            # 'V0022' : globals['V0022'],
            # 'V0023' : globals['V0023'],
            # 'V0024' : globals['V0024'],
            # 'V0025' : globals['V0025'],
            # 'V0026' : globals['V0026'],
            # 'V0032' : globals['V0032'],
            # 'V0033' : globals['V0033'],
            # 'V0034' : globals['V0034'],
            # 'V0035' : globals['V0035'],
            # 'V0036' : globals['V0036'],
            # 'V0037' : globals['V0037'],
            # 'V0048' : globals['V0048'],
            # 'V0049' : globals['V0049'],
            # 'V0050' : globals['V0050'],
            # 'V0051' : globals['V0051'],
            # 'V0052' : globals['V0052'],
            # 'V0053' : globals['V0053'],
            # 'V0054' : globals['V0054'],
            # 'V0055' : globals['V0055'],
            # 'V0056' : globals['V0056'],
            # 'V0057' : globals['V0057'],
            # 'V0058' : globals['V0058'],
            # 'V0059' : globals['V0059'],
            # 'V0060' : globals['V0060'],
            # 'V0064' : globals['V0064'],
            # 'V0065' : globals['V0065'],
            # 'V0011' : globals['V0011'],
            # 'V0043' : globals['V0043']
            'V0000': globals().get('V0000', 0),
            'V0001': globals().get('V0001', 0),
            'V0002': globals().get('V0002', 0),
            'V0016': globals().get('V0016', 0),
            'V0017': globals().get('V0017', 0),
            'V0018': globals().get('V0018', 0),
            'V0019': globals().get('V0019', 0),
            'V0020': globals().get('V0020', 0),
            'V0021': globals().get('V0021', 0),
            'V0022': globals().get('V0022', 0),
            'V0023': globals().get('V0023', 0),
            'V0024': globals().get('V0024', 0),
            'V0025': globals().get('V0025', 0),
            'V0026': globals().get('V0026', 0),
            'V0032': globals().get('V0032', 0),
            'V0033': globals().get('V0033', 0),
            'V0034': globals().get('V0034', 0),
            'V0035': globals().get('V0035', 0),
            'V0036': globals().get('V0036', 0),
            'V0037': globals().get('V0037', 0),
            'V0048': globals().get('V0048', 0),
            'V0049': globals().get('V0049', 0),
            'V0050': globals().get('V0050', 0),
            'V0051': globals().get('V0051', 0),
            'V0052': globals().get('V0052', 0),
            'V0053': globals().get('V0053', 0),
            'V0054': globals().get('V0054', 0),
            'V0055': globals().get('V0055', 0),
            'V0056': globals().get('V0056', 0),
            'V0057': globals().get('V0057', 0),
            'V0058': globals().get('V0058', 0),
            'V0059': globals().get('V0059', 0),
            'V0060': globals().get('V0060', 0),
            'V0064': globals().get('V0064', 0),
            'V0065': globals().get('V0065', 0),
            'V0011': globals().get('V0011', 0),
            'V0043': globals().get('V0043', 0)
        }})

def increase_number(label, nama):
    global current_value, current_box
    current_value = int(label.cget("text"))
    current_value += 1

    # Batasi nilai maksimum menjadi 99
    if current_value > 99:
        current_value = 99

    var_name = widget_variable_map.get(current_box, "Unknown Variable")

    label.configure(text=f"{current_value:02d}")  # Format angka menjadi dua digit

    print(f"User ada di: {var_name}")  # Tampilkan nama variabel

    # Perbarui nilai pada custom_variables
    if var_name in custom_variables:
        custom_variables2[var_name] = current_value
        globals()[var_name] = current_value

    print(custom_variables2)
    saveAllSetNumber()

def increase_number2(label, number):
    current_value = int(label.cget("text"))
    current_value += number

    # Batasi nilai maksimum menjadi 99
    if current_value > 99:
        current_value = 99

    label.configure(text=f"{current_value:02d}")  # Format angka menjadi dua digit
    saveAllSetNumber()

def decrease_number(label, nama):
    global current_value, current_box
    current_value = int(label.cget("text"))

    if current_value > 0:  # Mencegah angka turun di bawah 0
        current_value -= 1

    var_name = widget_variable_map.get(current_box, "Unknown Variable")

    label.configure(text=f"{current_value:02d}")  # Format angka menjadi dua digit

    print(f"User ada di: {var_name}")  # Tampilkan nama variabel

    # Perbarui nilai pada custom_variables
    if var_name in custom_variables:
        custom_variables2[var_name] = current_value
        globals()[var_name] = current_value

    print(custom_variables2)
    saveAllSetNumber()

def save_current_box(label):
    global current_box
    current_box = label.winfo_name()  # Mengambil nama label sebagai posisi
    print(f"User ada di: {current_box}")  # Tampilkan di mana user berada

def on_area_click(area_box):
    global current_box, current_value, previous_values
    # Jika kotak sebelumnya ada, simpan nilainya
    if current_box is not None and current_box != area_box:
        previous_values[current_box] = current_value
    elif current_box is not None and current_box == area_box:
        previous_values[current_box] = current_value

    # Update current_box dengan kotak baru
    current_box = area_box

    # Ambil nama variabel dari widget_variable_map
    var_name = widget_variable_map.get(current_box, "Unknown Variable")

    # Jika nilai sebelumnya ada, pulihkan, jika tidak reset ke 0
    if current_box in previous_values:
        current_value = previous_values[current_box]
    else:
        current_value = 0

    current_box.configure(text=f"{current_value:02d}")

    print(f"User ada di: {var_name}")  # Tampilkan nama variabel

# Fungsi untuk menangani klik tombol kalkulator
def oldon_calculator_button_click(button_text):
    global current_value, current_box
    print(f"Tombol {button_text} ditekan di kotak: {current_box}")
    if current_box:
        if button_text in ["+", "-", "←"]:
            # Handle increasing or decreasing the number
            if button_text == "+":
                increase_number(current_box)  # Increase the value in current_box
                # Update teks current_box dengan current_value
                update_label(current_box)
            elif button_text == "-":
                decrease_number(current_box)  # Decrease the value in current_box
                # Update teks current_box dengan current_value
                update_label(current_box)
            elif button_text == "←":
                current_value_str = str(current_value)

                # Menghapus digit terakhir dari current_value_str
                if len(current_value_str) > 0:  # Pastikan ada digit untuk dihapus
                    current_value_str = current_value_str[:-1]  # Hapus digit terakhir
                else:
                    current_value_str = "0"  # Jika tidak ada, set ke "0"

                # Jika current_value_str kosong, atur ke "0"
                if not current_value_str:
                    current_value_str = "0"

                # Mengubah kembali ke integer, pastikan tidak negatif
                current_value = int(current_value_str) if current_value_str else 0

                current_box.configure(text=f"{current_value:02d}")

                var_name = widget_variable_map.get(current_box, "Unknown Variable")

                print(f"User ada di: {var_name}")  # Tampilkan nama variabel

                # Perbarui nilai pada custom_variables
                if var_name in custom_variables:
                    custom_variables2[var_name] = current_value

                print(custom_variables2)
        elif button_text.isdigit():  # Check if button_text is a digit
            # Simpan angka saat ini sebagai string untuk manipulasi angka
            current_value_str = str(current_value)

            # Tambahkan digit baru ke current_value_str
            current_value_str += button_text

            # Konversi kembali ke integer untuk pengecekan batas
            current_value = int(current_value_str)

            # Jika current_value melebihi 99, set jadi 99
            if current_value > 99:
                current_value = 99

            # Update teks current_box dengan current_value
            current_box.configure(text=f"{current_value:02d}")

            # Update teks current_box dengan current_value
            update_label(current_box)

            var_name = widget_variable_map.get(current_box, "Unknown Variable")

            print(f"User ada di: {var_name}")  # Tampilkan nama variabel

            # Perbarui nilai pada custom_variables
            if var_name in custom_variables:
                custom_variables2[var_name] = current_value

            print(custom_variables2)

        else:
            if button_text == "↵":
                previous_values[current_box] = current_value
                current_box.configure(text=f"{current_value:02d}")
                # Update teks current_box dengan current_value
                update_label(current_box)
            else:
                current_value += button_text  # Append button text to current value

            # Update the current_box's text with the new current_value
            current_box.configure(text=f"{current_value:02d}")

def on_calculator_button_click(button_text):
    global current_value, current_box
    print(f"Tombol {button_text} ditekan di kotak: {current_box}")
    if current_box:
        var_name = widget_variable_map.get(current_box, "Unknown Variable")
        
        # Pastikan var_name valid dan ada di globals
        if var_name not in globals():
            print(f"Error: {var_name} tidak ditemukan di variabel global.")
            return

        if button_text in ["+", "-", "←"]:
            # Handle increasing or decreasing the number
            if button_text == "+":
                increase_number(current_box)  # Increase the value in current_box
                update_label(current_box)  # Update teks current_box dengan current_value
                globals()[var_name] = current_value  # Perbarui nilai di globals
            elif button_text == "-":
                decrease_number(current_box)  # Decrease the value in current_box
                update_label(current_box)  # Update teks current_box dengan current_value
                globals()[var_name] = current_value  # Perbarui nilai di globals
            elif button_text == "←":
                current_value_str = str(current_value)

                # Menghapus digit terakhir dari current_value_str
                if len(current_value_str) > 0:  # Pastikan ada digit untuk dihapus
                    current_value_str = current_value_str[:-1]  # Hapus digit terakhir
                else:
                    current_value_str = "0"  # Jika tidak ada, set ke "0"

                # Jika current_value_str kosong, atur ke "0"
                if not current_value_str:
                    current_value_str = "0"

                # Mengubah kembali ke integer, pastikan tidak negatif
                current_value = int(current_value_str) if current_value_str else 0

                current_box.configure(text=f"{current_value:02d}")

                globals()[var_name] = current_value  # Perbarui nilai di globals

        elif button_text.isdigit():  # Check if button_text is a digit
            # Simpan angka saat ini sebagai string untuk manipulasi angka
            current_value_str = str(current_value)

            # Tambahkan digit baru ke current_value_str
            current_value_str += button_text

            # Konversi kembali ke integer untuk pengecekan batas
            current_value = int(current_value_str)

            # Jika current_value melebihi 99, set jadi 99
            if current_value > 99:
                current_value = 99

            current_box.configure(text=f"{current_value:02d}")
            update_label(current_box)  # Update teks current_box dengan current_value
            globals()[var_name] = current_value  # Perbarui nilai di globals

        elif button_text == "↵":
            # Menyimpan nilai ke globals
            globals()[var_name] = current_value
            previous_values[current_box] = current_value
            current_box.configure(text=f"{current_value:02d}")
            update_label(current_box)  # Update teks current_box dengan current_value

        print(f"Nilai global {var_name}: {globals()[var_name]}")
    saveAllSetNumber()

def update_label(var_name):
    for widget, name in widget_variable_map.items():
        if name == var_name:
            widget.configure(text=f"{custom_variables[var_name]:02d}")

def create_area_frame(parent, title, var_name):
    global custom_variables

    # Frame untuk area baru
    top_left_frame = ctk.CTkFrame(parent, width=100, height=90, fg_color="transparent")
    top_left_frame.pack(side="left", anchor="nw", padx=13, pady=0)  # Ditempatkan secara horizontal (kiri ke kanan)

    # Frame untuk border di sekitar judul (dengan border hitam)
    title_border_frame = ctk.CTkFrame(top_left_frame, border_width=1, border_color="black", fg_color="transparent",
                                      width=140, height=23)
    title_border_frame.pack_propagate(False)  # Agar ukuran frame tidak berubah sesuai konten
    title_border_frame.pack(side="top", padx=0, pady=0)

    # Persegi panjang di atas untuk judul
    title_label = ctk.CTkLabel(title_border_frame, text=title, width=130, height=20, fg_color="transparent",  font=("Arial", 10))
    title_label.pack(expand=True)

    # Frame untuk memberi border hitam pada sec_label
    sec_border_frame = ctk.CTkFrame(top_left_frame, border_width=2, border_color="gray", fg_color="transparent",
                                    width=38, height=26)
    sec_border_frame.pack_propagate(False)  # Agar ukuran frame tidak menyesuaikan konten di dalamnya
    sec_border_frame.pack(side="top", pady=(0, 0), padx=(0, 100))

    # Kotak kecil "sec" di atas kotak angka
    sec_label = ctk.CTkLabel(sec_border_frame, text="sec", width=30, height=20, fg_color="transparent")
    sec_label.pack(expand=True)  # Pastikan label mengisi frame

    # Frame untuk membungkus number_label dengan border hitam
    number_border_frame = ctk.CTkFrame(top_left_frame, border_width=2, border_color="black", fg_color="transparent",
                                       width=58, height=58)
    number_border_frame.pack_propagate(False)  # Agar ukuran frame tidak berubah sesuai konten
    number_border_frame.pack(side="left", pady=(0,0))

    # Kotak angka di sebelah kiri tombol panah ke atas
    number_label = ctk.CTkLabel(number_border_frame, text="00", width=50, height=50, fg_color="transparent",
                                text_color="black", font=("Arial", 24))
    number_label.pack(expand=True)

    # Simpan mapping antara widget dan variabel
    # widget_variable_map[number_label] = var_name
    custom_variables[var_name] = globals().get(var_name, 0)  # Inisialisasi variabel di dictionary
    widget_variable_map[number_label] = var_name  # Simpan number_label sesuai dengan var_name

    # Tampilkan nilai awal dari variabel pada label
    number_label.configure(text=str(custom_variables[var_name]))

    # Tombol panah ke atas
    up_button = ctk.CTkButton(top_left_frame,  image=up_image, command=lambda: (on_area_click(number_label), increase_number(number_label, var_name)), width=50, height=10, fg_color="transparent", text_color="black", text="")
    up_button.pack(side="top", pady=(0, 0))

    # Tombol panah ke bawah
    down_button = ctk.CTkButton(top_left_frame, image=down_image, command=lambda: (on_area_click(number_label), decrease_number(number_label, var_name)), width=50, height=10, fg_color="transparent", text_color="black", text="")
    down_button.pack(side="top", pady=(0, 0))

    number_label.bind("<Button-1>", lambda e: on_area_click(number_label))
# ================================================================================
# END SET FUNCTION
# ================================================================================

# ================================================================================
# LINE Z FUNCTION - .zfunc
# ================================================================================
def cmdBtnZLineA():
    # globals()['J00048'] = True
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            # 'J00048' : globals()['J00048'],
            'V0149': 16777216
        }})
    # btnZManLineA.configure(fg_color="lime", text_color="black")
    # btnZManLineB.configure(fg_color="pink", text_color="white")
    # btnZManLineC.configure(fg_color="pink", text_color="white")
    # showCommonAuto()

def cmdBtnZLineB():
    # globals()['J00047'] = True
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            # 'J00047' : globals()['J00047'],
            'V0149': 8388608
        }})
    # btnZManLineB.configure(fg_color="lime", text_color="black")
    # btnZManLineA.configure(fg_color="pink", text_color="white")
    # btnZManLineC.configure(fg_color="pink", text_color="white")
    # showCommonAuto()

def cmdBtnZLineC():
    # globals()['J00046'] = True
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            # 'J00046' : globals()['J00046'],
            'V0149': 4194304
        }})
    # btnZManLineC.configure(fg_color="lime", text_color="black")
    # btnZManLineB.configure(fg_color="pink", text_color="white")
    # btnZManLineA.configure(fg_color="pink", text_color="white")
    # showCommonAuto()

def cmdBtnFillC():
    globals()['J00057'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00057': True
    #     }})

def cmdBtnDumpC():
    globals()['J00058'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00058': True
    #     }})


def cmdBtnFillB():
    globals()['J00037'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00037': True
    #     }})

def cmdBtnDumpB():
    globals()['J00038'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00038': True
    #     }})




globals()['holdbtnRedZManFeedThreeDoor'] = False

def btnRedZManFeedThreeDoorClick():
    global holdbtnRedZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnRedZManFeedThreeDoor'] = False
    btnRedZManFeedThreeDoor.after(hold_time, checkbtnRedZManFeedThreeDoorhold)
    print("btnbtnRedZManFeedThreeDoorClick clicked")
    
def checkbtnRedZManFeedThreeDoorhold():
    global holdbtnRedZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedZManFeedThreeDoor.winfo_containing(btnRedZManFeedThreeDoor.winfo_pointerx(),
                                               btnRedZManFeedThreeDoor.winfo_pointery()):
        holdbtnRedZManFeedThreeDoor = True
        globals()['J00047'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00047': True
        #     }})

def btnRedZManFeedThreeDoorClickReset():
    global holdbtnRedZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnRedZManFeedThreeDoor'] = False
    print("btnRedZManFeedThreeDoorClick Released")



globals()['holdbtnYellowZManFeedThreeDoor'] = False

def btnYellowZManFeedThreeDoorClick():
    global holdbtnYellowZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnYellowZManFeedThreeDoor'] = False
    btnYellowZManFeedThreeDoor.after(hold_time, checkbtnYellowZManFeedThreeDoorhold)
    print("btnbtnYellowZManFeedThreeDoorClick clicked")
    
def checkbtnYellowZManFeedThreeDoorhold():
    global holdbtnYellowZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnYellowZManFeedThreeDoor.winfo_containing(btnYellowZManFeedThreeDoor.winfo_pointerx(),
                                               btnYellowZManFeedThreeDoor.winfo_pointery()):
        holdbtnYellowZManFeedThreeDoor = True
        globals()['J00048'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00048': True
        #     }})

def btnYellowZManFeedThreeDoorClickReset():
    global holdbtnYellowZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnYellowZManFeedThreeDoor'] = False
    print("btnYellowZManFeedThreeDoorClick Released")

globals()['holdbtnGreenZManFeedThreeDoor'] = False

def btnGreenZManFeedThreeDoorClick():
    global holdbtnGreenZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnGreenZManFeedThreeDoor'] = False
    btnGreenZManFeedThreeDoor.after(hold_time, checkbtnGreenZManFeedThreeDoorhold)
    print("btnbtnGreenZManFeedThreeDoorClick clicked")
    
def checkbtnGreenZManFeedThreeDoorhold():
    global holdbtnGreenZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenZManFeedThreeDoor.winfo_containing(btnGreenZManFeedThreeDoor.winfo_pointerx(),
                                               btnGreenZManFeedThreeDoor.winfo_pointery()):
        holdbtnGreenZManFeedThreeDoor = True
        globals()['J00046'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00046': True
        #     }})

def btnGreenZManFeedThreeDoorClickReset():
    global holdbtnGreenZManFeedThreeDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnGreenZManFeedThreeDoor'] = False
    print("btnGreenZManFeedThreeDoorClick Released")



# ================================================================================
# LINE B FUNCTION - .bfunc
# ================================================================================

class MaterialModeSelectorFeederB:
    def __init__(self):
        self.not_full_sensor = not bool(globals()['J00135'] and globals()['J00136'] and globals()['J00137'] and globals()['J00138'] and globals()['J00139'])

    def putih(self):
        return bool(self.not_full_sensor and not globals()['J00140'] and globals()['V0140'] == 32768 and (globals()['I00021'] and not globals()['I00020']))

    def warna1(self):
        return bool(self.not_full_sensor and not globals()['J00141'] and globals()['V0140'] == 16384 and (globals()['I00023'] and not globals()['I00022']))

    def warna2(self):
        return bool(self.not_full_sensor and not globals()['J00142'] and globals()['V0140'] == 8192 and (globals()['I00023'] and not globals()['I00022']))

    def warna3(self):
        return bool(self.not_full_sensor and not globals()['J00143'] and globals()['V0140'] == 4096 and (globals()['I00023'] and not globals()['I00022']))

    def reset(self):
        return not bool(self.putih or self.warna1 or self.warna2 or self.warna3)

class ProductModeSelectorHopperB:
    def __init__(self):
        self.not_full_sensor = not bool(globals()['J00144'] and globals()['J00145'])

    def putih(self):
        return bool(self.not_full_sensor and globals()['V0141'] == 2048)

    def warna(self):
        return bool(self.not_full_sensor and globals()['V0141'] == 1024)

    def reset(self):
        return not bool(self.putih or self.warna)

def cmdBtnFeederBPutih():
    globals()['V0140'] = 32768
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0140': globals()['V0140']
        }})
    # btnAutoFeedPutih.configure(fg_color="lime", text_color="black")
    # btnAutoFeedWarna1.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3.configure(fg_color="pink", text_color="white")
    showAutoBesarB2()

def cmdBtnFeederBWarna1():
    globals()['V0140'] = 16384
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0140': globals()['V0140']
        }})
    # btnAutoFeedPutih.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1.configure(fg_color="red", text_color="black")
    # btnAutoFeedWarna2.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3.configure(fg_color="pink", text_color="white")
    showAutoBesarB2()

def cmdBtnFeederBWarna2():
    globals()['V0140'] = 8192
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0140': globals()['V0140']
        }})
    # btnAutoFeedPutih.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2.configure(fg_color="red", text_color="black")
    # btnAutoFeedWarna3.configure(fg_color="pink", text_color="white")
    showAutoBesarB2()

def cmdBtnFeederBWarna3():
    globals()['V0140'] = 4096
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0140': globals()['V0140']
        }})
    # btnAutoFeedPutih.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3.configure(fg_color="red", text_color="black")
    showAutoBesarB2()

def cmdBtnFeederManual():
    globals()['V0140'] = 0
    globals()['V0141'] = 0
    globals()['V0144'] = 0
    globals()['V0145'] = 0
    globals()['V0146'] = 0
    globals()['V0147'] = 0
    globals()['V0149'] = 0
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0140': 0,
            'V0141': 0,
            'V0144': 0,
            'V0145': 0,
            'V0146': 0,
            'V0147': 0,
            'V0149': 0
        }})
    btnAutoFeedPutih.configure(fg_color="light green", text_color="white")
    btnAutoFeedWarna1.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna2.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna3.configure(fg_color="pink", text_color="white")
    btnAutoHopperPutih.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1.configure(fg_color="pink", text_color="white")
    btnAutoFeedPutihC.configure(fg_color="light green", text_color="white")
    btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white")
    btnAutoHopperPutihC.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white")
    showBesarA()


# ----------------------------------
def cmdBtnHopperBPutih():
    globals()['V0141'] = 2048
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0141': globals()['V0141']
        }})
    # btnAutoHopperPutih.configure(fg_color="lime", text_color="black")
    # btnAutoHopperWarna1.configure(fg_color="pink", text_color="white")
    showAutoBesarB2()

def cmdBtnHopperBWarna():
    globals()['V0141'] = 1024
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0141': globals()['V0141']
        }})
    # btnAutoHopperPutih.configure(fg_color="light green", text_color="white")
    # btnAutoHopperWarna1.configure(fg_color="red", text_color="black")
    showAutoBesarB2()

def cmdBtnHopperBManual():
    globals()['V0145'] = 0
    globals()['V0141'] = 0
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0145': 0,
            'V0141': 0
        }})

# ----------------------------------
globals()['holdbtnKiriBManMaterMixRotor'] = False

def btnKiriBManMaterMixRotorClick():
    global holdbtnKiriBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKiriBManMaterMixRotor'] = False
    btnKiriBManMaterMixRotor.after(hold_time, checkbtnKiriBManMaterMixRotorhold)
    btnKiriBManMaterMixRotor.configure(image=imgBManMaterMixRotorLeft)

def checkbtnKiriBManMaterMixRotorhold():
    global holdbtnKiriBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKiriBManMaterMixRotor.winfo_containing(btnKiriBManMaterMixRotor.winfo_pointerx(),
                                               btnKiriBManMaterMixRotor.winfo_pointery()):
        holdbtnKiriBManMaterMixRotor = True
        globals()['J00001'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00001': True
        #     }})

def btnKiriBManMaterMixRotorClickReset():
    global holdbtnKiriBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKiriBManMaterMixRotor'] = False
    btnKiriBManMaterMixRotor.configure(image=imgBManMaterMixRotorLeftTrans)

# ----------------------------------
globals()['holdbtnKananBManMaterMixRotor'] = False

def btnKananBManMaterMixRotorClick():
    global holdbtnKananBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManMaterMixRotor'] = False
    btnKananBManMaterMixRotor.after(hold_time, checkbtnKananBManMaterMixRotorhold)
    btnKananBManMaterMixRotor.configure(image=imgBManMaterMixRotorRight)

def checkbtnKananBManMaterMixRotorhold():
    global holdbtnKananBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManMaterMixRotor.winfo_containing(btnKananBManMaterMixRotor.winfo_pointerx(),
                                               btnKananBManMaterMixRotor.winfo_pointery()):
        holdbtnKananBManMaterMixRotor = True
        globals()['J00000'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00000': True
        #     }})

def btnKananBManMaterMixRotorClickReset():
    global holdbtnKananBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManMaterMixRotor'] = False
    btnKananBManMaterMixRotor.configure(image=imgBManMaterMixRotorRightTrans)

# ----------------------------------
globals()['holdRedBManMaterMixDoor'] = False


def btnRedBManMaterMixDoorClick():
    global holdRedBManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedBManMaterMixDoor'] = False
    btnRedBManMaterMixDoor.after(hold_time, checkRedBManMaterMixDoorhold)
    print("btnRedBManMaterMixDoorClick clicked")
    


def checkRedBManMaterMixDoorhold():
    global holdRedBManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedBManMaterMixDoor.winfo_containing(btnRedBManMaterMixDoor.winfo_pointerx(), btnRedBManMaterMixDoor.winfo_pointery()):
        holdRedBManMaterMixDoor = True
        globals()['J00002'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00002': True
        #     }})
        


def btnRedBManMaterMixDoorClickReset():
    global holdRedBManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedBManMaterMixDoor'] = False
    print("btnRedBManMaterMixDoorClick Release")


# ----------------------------------
globals()['holdGreenBManMaterMixDoor'] = False

def btnGreenBManMaterMixDoorClick():
    global holdGreenBManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManMaterMixDoor'] = False
    btnGreenBManMaterMixDoor.after(hold_time, checkGreenBManMaterMixDoorhold)
    print("btnGreenBManMaterMixDoorClick clicked")
    


def checkGreenBManMaterMixDoorhold():
    global holdGreenBManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManMaterMixDoor.winfo_containing(btnGreenBManMaterMixDoor.winfo_pointerx(),
                                             btnGreenBManMaterMixDoor.winfo_pointery()):
        holdGreenBManMaterMixDoor = True
        globals()['J00003'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00003': True
        #     }})
        


def btnGreenBManMaterMixDoorClickReset():
    global holdGreenBManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManMaterMixDoor'] = False
    print("btnGreenBManMaterMixDoorClick Released")
# ----------------------------------
# holdManBMateriVbratorSwitch = False

# def changeBManMateriVbratorSwitch(direction):
#     global stateBManMateriVbrator, imgBManMateriVbrator, imgBManMateriVbratorLeft, imgBManMateriVbratorRight, loopAllButtonFalse, holdManBMateriVbratorSwitch
#     loopAllButtonFalse = False
#     holdManBMateriVbratorSwitch = False
#     canvasBManMateriVbrator.after(hold_time, checkBManMateriVbratorSwitchhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasBManMateriVbrator.itemconfig(imgBManMateriVbrator, image=imgBManMateriVbratorLeft)
#         stateBManMateriVbrator = "left"
#     elif direction == "right":
#         canvasBManMateriVbrator.itemconfig(imgBManMateriVbrator, image=imgBManMateriVbratorRight)
#         stateBManMateriVbrator = "right"


# def checkBManMateriVbratorSwitchhold(direction):
#     global stateBManMateriVbrator, imgBManMateriVbrator, imgBManMateriVbratorLeft, imgBManMateriVbratorRight, holdBManMateriVbratorSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasBManMateriVbrator.winfo_containing(canvasBManMateriVbrator.winfo_pointerx(), canvasBManMateriVbrator.winfo_pointery()):
#         holdBManMateriVbratorSwitch = True
#     if direction == "left":
#         canvasBManMateriVbrator.itemconfig(imgBManMateriVbrator, image=imgBManMateriVbratorLeft)
#         stateBManMateriVbrator = "left"

#     elif direction == "right":
#         canvasBManMateriVbrator.itemconfig(imgBManMateriVbrator, image=imgBManMateriVbratorRight)
#         stateBManMateriVbrator = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00004': True
#             }})


# def resetBManMateriVbratorSwicth(event):
#     global stateBManMateriVbrator, imgBManMateriVbratorUp, loopAllButtonFalse, holdManBMateriVbratorSwitch
#     loopAllButtonFalse = True
#     holdManBMateriVbratorSwitch = False
#     print("Arrow reset")
#     canvasBManMateriVbrator.itemconfig(imgBManMateriVbrator, image=imgBManMateriVbratorUp)
#     stateBManMateriVbrator = "up"

globals()['holdbtnKananBManMateriVbrator'] = False

def btnKananBManMateriVbratorClick():
    global holdbtnKananBManMateriVbrator, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManMateriVbrator'] = False
    btnKananBManMateriVbrator.after(hold_time, checkbtnKananBManMateriVbratorhold)
    btnKananBManMateriVbrator.configure(image=imgBManMateriVbratorRight)

def checkbtnKananBManMateriVbratorhold():
    global holdbtnKananBManMateriVbrator, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManMateriVbrator.winfo_containing(btnKananBManMateriVbrator.winfo_pointerx(),
                                               btnKananBManMateriVbrator.winfo_pointery()):
        holdbtnKananBManMateriVbrator = True
        globals()['J00004'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00004': True
        #     }})

def btnKananBManMateriVbratorClickReset():
    global holdbtnKananBManMateriVbrator, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManMateriVbrator'] = False
    btnKananBManMateriVbrator.configure(image=imgBManMateriVbratorRightTrans)

# ----------------------------------
globals()['holdbtnKananBManMaterMixRotor'] = False

def btnKananBManMaterMixRotorClick():
    global holdbtnKananBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManMaterMixRotor'] = False
    btnKananBManMaterMixRotor.after(hold_time, checkbtnKananBManMaterMixRotorhold)
    btnKananBManMaterMixRotor.configure(image=imgBManMaterMixRotorRight)

def btnKananBManMaterMixRotorClickReset():
    global holdbtnKananBManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManMaterMixRotor'] = False
    btnKananBManMaterMixRotor.configure(image=imgBManMaterMixRotorRightTrans)

# ---------------------------------- here.
globals()['holdbtnKiriBManMatScrewCnvyr'] = False

def btnKiriBManMatScrewCnvyrClick():
    global holdbtnKiriBManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKiriBManMatScrewCnvyr'] = False
    btnKiriBManMatScrewCnvyr.after(hold_time, checkbtnKiriBManMatScrewCnvyrhold)
    btnKiriBManMatScrewCnvyr.configure(image=imgBManMatScrewCnvyrLeft)

def checkbtnKiriBManMatScrewCnvyrhold():
    global holdbtnKiriBManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKiriBManMatScrewCnvyr.winfo_containing(btnKiriBManMatScrewCnvyr.winfo_pointerx(),
                                               btnKiriBManMatScrewCnvyr.winfo_pointery()):
        holdbtnKiriBManMatScrewCnvyr = True
        globals()['J00017'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00017': True
        #     }})

def btnKiriBManMatScrewCnvyrClickReset():
    global holdbtnKiriBManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKiriBManMatScrewCnvyr'] = False
    btnKiriBManMatScrewCnvyr.configure(image=imgBManMatScrewCnvyrLeftTrans)

# ----------------------------------
globals()['holdbtnKananBManMatScrewCnvyr'] = False

def btnKananBManMatScrewCnvyrClick():
    global holdbtnKananBManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManMatScrewCnvyr'] = False
    btnKananBManMatScrewCnvyr.after(hold_time, checkbtnKananBManMatScrewCnvyrhold)
    btnKananBManMatScrewCnvyr.configure(image=imgBManMatScrewCnvyrRight)

def checkbtnKananBManMatScrewCnvyrhold():
    global holdbtnKananBManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManMatScrewCnvyr.winfo_containing(btnKananBManMatScrewCnvyr.winfo_pointerx(),
                                               btnKananBManMatScrewCnvyr.winfo_pointery()):
        holdbtnKananBManMatScrewCnvyr = True
        globals()['J00016'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00016': True
        #     }})

def btnKananBManMatScrewCnvyrClickReset():
    global holdbtnKananBManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManMatScrewCnvyr'] = False
    btnKananBManMatScrewCnvyr.configure(image=imgBManMatScrewCnvyrRightTrans)



# holdBManMatScrewCnvyrSwitch = False

# def changeBManMatScrewCnvyrSwitch(direction):
#     global stateBManMatScrewCnvyr, imgBManMatScrewCnvyr, imgBManMatScrewCnvyrLeft, imgBManMatScrewCnvyrRight, loopAllButtonFalse, holdBManMatScrewCnvyrSwitch
#     holdBManMatScrewCnvyrSwitch = False
#     loopAllButtonFalse = False
#     canvasBManMatScrewCnvyr.after(hold_time, checkBManMatScrewCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasBManMatScrewCnvyr.itemconfig(imgBManMatScrewCnvyr, image=imgBManMatScrewCnvyrLeft)
#         stateBManMatScrewCnvyr = "left"

#     elif direction == "right":
#         canvasBManMatScrewCnvyr.itemconfig(imgBManMatScrewCnvyr, image=imgBManMatScrewCnvyrRight)
#         stateBManMatScrewCnvyr = "right"


# def checkBManMatScrewCnvyrhold(direction):
#     global stateBManMatScrewCnvyr, imgBManMatScrewCnvyr, imgBManMatScrewCnvyrLeft, imgBManMatScrewCnvyrRight, holdBManMatScrewCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasBManMatScrewCnvyr.winfo_containing(canvasBManMatScrewCnvyr.winfo_pointerx(), canvasBManMatScrewCnvyr.winfo_pointery()):
#         holdBManMatScrewCnvyrSwitch = True
#     if direction == "left":
#         canvasBManMatScrewCnvyr.itemconfig(imgBManMatScrewCnvyr, image=imgBManMatScrewCnvyrLeft)
#         stateBManMatScrewCnvyr = "left"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00017': True,
#                 'J00016': False
#             }})
#     elif direction == "right":
#         canvasBManMatScrewCnvyr.itemconfig(imgBManMatScrewCnvyr, image=imgBManMatScrewCnvyrRight)
#         stateBManMatScrewCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00016': True,
#                 'J00017': False
#             }})


# def resetBManMatScrewCnvyrSwicth(event):
#     global stateBManMatScrewCnvyr, imgBManMatScrewCnvyrUp, loopAllButtonFalse, holdBManMatScrewCnvyrSwitch
#     loopAllButtonFalse = True
#     holdBManMatScrewCnvyrSwitch = False
#     print("Arrow reset")
#     canvasBManMatScrewCnvyr.itemconfig(imgBManMatScrewCnvyr, image=imgBManMatScrewCnvyrUp)
#     stateBManMatScrewCnvyr = "up"

# ---------------------------------- here.
globals()['holdbtnKananBManToRotaryCnvyr'] = False

def btnKananBManToRotaryCnvyrClick():
    global holdbtnKananBManToRotaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManToRotaryCnvyr'] = False
    btnKananBManToRotaryCnvyr.after(hold_time, checkbtnKananBManToRotaryCnvyrhold)
    btnKananBManToRotaryCnvyr.configure(image=imgBManToRotaryCnvyrRight)

def checkbtnKananBManToRotaryCnvyrhold():
    global holdbtnKananBManToRotaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManToRotaryCnvyr.winfo_containing(btnKananBManToRotaryCnvyr.winfo_pointerx(),
                                               btnKananBManToRotaryCnvyr.winfo_pointery()):
        holdbtnKananBManToRotaryCnvyr = True
        globals()['J00005'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00005': True
        #     }})

def btnKananBManToRotaryCnvyrClickReset():
    global holdbtnKananBManToRotaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManToRotaryCnvyr'] = False
    btnKananBManToRotaryCnvyr.configure(image=imgBManToRotaryCnvyrRightTrans)

# holdBManToRotaryCnvyrSwitch = False

# def changeBManToRotaryCnvyrSwitch(direction):
#     global stateBManToRotaryCnvyr, imgBManToRotaryCnvyr, imgBManToRotaryCnvyrLeft, imgBManToRotaryCnvyrRight, loopAllButtonFalse, holdBManToRotaryCnvyrSwitch
#     loopAllButtonFalse = False
#     holdBManToRotaryCnvyrSwitch = False
#     canvasBManToRotaryCnvyr.after(hold_time, checkoRotaryCnvyrBhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasBManToRotaryCnvyr.itemconfig(imgBManToRotaryCnvyr, image=imgBManToRotaryCnvyrLeft)
#         stateBManToRotaryCnvyr = "left"
#     elif direction == "right":
#         canvasBManToRotaryCnvyr.itemconfig(imgBManToRotaryCnvyr, image=imgBManToRotaryCnvyrRight)
#         stateBManToRotaryCnvyr = "right"


# def checkoRotaryCnvyrBhold(direction):
#     global stateBManToRotaryCnvyr, imgBManToRotaryCnvyr, imgBManToRotaryCnvyrLeft, imgBManToRotaryCnvyrRight, holdBManToRotaryCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasBManToRotaryCnvyr.winfo_containing(canvasBManToRotaryCnvyr.winfo_pointerx(), canvasBManToRotaryCnvyr.winfo_pointery()):
#         holdBManToRotaryCnvyrSwitch = True
#     if direction == "left":
#         canvasBManToRotaryCnvyr.itemconfig(imgBManToRotaryCnvyr, image=imgBManToRotaryCnvyrLeft)
#         stateBManToRotaryCnvyr = "left"
#     elif direction == "right":
#         canvasBManToRotaryCnvyr.itemconfig(imgBManToRotaryCnvyr, image=imgBManToRotaryCnvyrRight)
#         stateBManToRotaryCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00005': True
#             }})


# def resetBManToRotaryCnvyrSwicth(event):
#     global stateBManToRotaryCnvyr, imgBManToRotaryCnvyrUp, loopAllButtonFalse, holdBManToRotaryCnvyrSwitch
#     loopAllButtonFalse = True
#     holdBManToRotaryCnvyrSwitch = False
#     print("Arrow reset")
#     canvasBManToRotaryCnvyr.itemconfig(imgBManToRotaryCnvyr, image=imgBManToRotaryCnvyrUp)
#     stateBManToRotaryCnvyr = "up"
# ----------------------------------
globals()['holdGreenBManToRotaryCnvyr0'] = False


def btnGreenBManToRotaryCnvyr0Click():
    global holdGreenBManToRotaryCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToRotaryCnvyr0'] = False
    btnGreenBManToRotaryCnvyr0.after(hold_time, checkGreenBManToRotaryCnvyr0hold)
    print("btnGreenBManToRotaryCnvyr0Click clicked")
    

def checkGreenBManToRotaryCnvyr0hold():
    global holdGreenBManToRotaryCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToRotaryCnvyr0.winfo_containing(btnGreenBManToRotaryCnvyr0.winfo_pointerx(),
                                               btnGreenBManToRotaryCnvyr0.winfo_pointery()):
        holdGreenBManToRotaryCnvyr0 = True
        globals()['J00007'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00007': True
        #     }})


def btnGreenBManToRotaryCnvyr0ClickReset():
    global holdGreenBManToRotaryCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToRotaryCnvyr0'] = False
    print("btnGreenBManToRotaryCnvyr0Click Released")
# ----------------------------------
globals()['holdGreenBManToRotaryCnvyr1'] = False


def btnGreenBManToRotaryCnvyr1Click():
    global holdGreenBManToRotaryCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToRotaryCnvyr1'] = False
    btnGreenBManToRotaryCnvyr1.after(hold_time, checkGreenBManToRotaryCnvyr1hold)
    print("btnGreenBManToRotaryCnvyr1Click clicked")
    

def checkGreenBManToRotaryCnvyr1hold():
    global holdGreenBManToRotaryCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToRotaryCnvyr1.winfo_containing(btnGreenBManToRotaryCnvyr1.winfo_pointerx(),
                                               btnGreenBManToRotaryCnvyr1.winfo_pointery()):
        holdGreenBManToRotaryCnvyr1 = True
        globals()['J00009'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00009': True
        #     }})


def btnGreenBManToRotaryCnvyr1ClickReset():
    global holdGreenBManToRotaryCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToRotaryCnvyr1'] = False
    print("btnGreenBManToRotaryCnvyr1Click Released")
# ----------------------------------
globals()['holdGreenBManToRotaryCnvyr2'] = False


def btnGreenBManToRotaryCnvyr2Click():
    global holdGreenBManToRotaryCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToRotaryCnvyr2'] = False
    btnGreenBManToRotaryCnvyr2.after(hold_time, checkGreenBManToRotaryCnvyr2hold)
    print("btnGreenBManToRotaryCnvyr2Click clicked")
    

def checkGreenBManToRotaryCnvyr2hold():
    global holdGreenBManToRotaryCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToRotaryCnvyr2.winfo_containing(btnGreenBManToRotaryCnvyr2.winfo_pointerx(),
                                               btnGreenBManToRotaryCnvyr2.winfo_pointery()):
        holdGreenBManToRotaryCnvyr2 = True
        globals()['J00011'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00011': True
        #     }})


def btnGreenBManToRotaryCnvyr2ClickReset():
    global holdGreenBManToRotaryCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToRotaryCnvyr2'] = False
    print("btnGreenBManToRotaryCnvyr2Click Released")

# ----------------------------------
globals()['holdGreenBManToRotaryCnvyr3'] = False


def btnGreenBManToRotaryCnvyr3Click():
    global holdGreenBManToRotaryCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToRotaryCnvyr3'] = False
    btnGreenBManToRotaryCnvyr3.after(hold_time, checkGreenBManToRotaryCnvyr3hold)
    print("btnGreenBManToRotaryCnvyr3Click clicked")
    

def checkGreenBManToRotaryCnvyr3hold():
    global holdGreenBManToRotaryCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToRotaryCnvyr3.winfo_containing(btnGreenBManToRotaryCnvyr3.winfo_pointerx(),
                                               btnGreenBManToRotaryCnvyr3.winfo_pointery()):
        holdGreenBManToRotaryCnvyr3 = True
        globals()['J00013'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00013': True
        #     }})


def btnGreenBManToRotaryCnvyr3ClickReset():
    global holdGreenBManToRotaryCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToRotaryCnvyr3'] = False
    print("btnGreenBManToRotaryCnvyr3Click Released")
# ----------------------------------
globals()['holdGreenBManToRotaryCnvyr4'] = False


def btnGreenBManToRotaryCnvyr4Click():
    global holdGreenBManToRotaryCnvyr4, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToRotaryCnvyr4'] = False
    btnGreenBManToRotaryCnvyr4.after(hold_time, checkGreenBManToRotaryCnvyr4hold)
    print("btnGreenBManToRotaryCnvyr4Click clicked")
    

def checkGreenBManToRotaryCnvyr4hold():
    global holdGreenBManToRotaryCnvyr4, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToRotaryCnvyr4.winfo_containing(btnGreenBManToRotaryCnvyr4.winfo_pointerx(),
                                               btnGreenBManToRotaryCnvyr4.winfo_pointery()):
        holdGreenBManToRotaryCnvyr4 = True
        globals()['J00015'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00015': True
        #     }})


def btnGreenBManToRotaryCnvyr4ClickReset():
    global holdGreenBManToRotaryCnvyr4, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToRotaryCnvyr4'] = False
    print("btnGreenBManToRotaryCnvyr4Click Released")

# ----------------------------------
globals()['holdbtnKananBManFrmRtaryCnvyr'] = False

def btnKananBManFrmRtaryCnvyrClick():
    global holdbtnKananBManFrmRtaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManFrmRtaryCnvyr'] = False
    btnKananBManFrmRtaryCnvyr.after(hold_time, checkbtnKananBManFrmRtaryCnvyrhold)
    btnKananBManFrmRtaryCnvyr.configure(image=imgBManFrmRtaryCnvyrRight)

def checkbtnKananBManFrmRtaryCnvyrhold():
    global holdbtnKananBManFrmRtaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManFrmRtaryCnvyr.winfo_containing(btnKananBManFrmRtaryCnvyr.winfo_pointerx(),
                                               btnKananBManFrmRtaryCnvyr.winfo_pointery()):
        holdbtnKananBManFrmRtaryCnvyr = True
        globals()['J00032'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00032': True
        #     }})

def btnKananBManFrmRtaryCnvyrClickReset():
    global holdbtnKananBManFrmRtaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManFrmRtaryCnvyr'] = False
    btnKananBManFrmRtaryCnvyr.configure(image=imgBManFrmRtaryCnvyrRightTrans)

# holdBManFrmRtaryCnvyrSwitch = False


# def changeBManFrmRtaryCnvyrSwitch(direction):
#     global stateBManFrmRtaryCnvyr, imgBManFrmRtaryCnvyr, imgBManFrmRtaryCnvyrLeft, imgBManFrmRtaryCnvyrRight, loopAllButtonFalse, holdBManFrmRtaryCnvyrSwitch
#     holdBManFrmRtaryCnvyrSwitch = False
#     loopAllButtonFalse = False
#     canvasBManFrmRtaryCnvyr.after(hold_time, checkBManFrmRtaryCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasBManFrmRtaryCnvyr.itemconfig(imgBManFrmRtaryCnvyr, image=imgBManFrmRtaryCnvyrLeft)
#         stateBManFrmRtaryCnvyr = "left"
#     elif direction == "right":
#         canvasBManFrmRtaryCnvyr.itemconfig(imgBManFrmRtaryCnvyr, image=imgBManFrmRtaryCnvyrRight)
#         stateBManFrmRtaryCnvyr = "right"


# def checkBManFrmRtaryCnvyrhold(direction):
#     global stateBManFrmRtaryCnvyr, imgBManFrmRtaryCnvyr, imgBManFrmRtaryCnvyrLeft, imgBManFrmRtaryCnvyrRight, holdBManFrmRtaryCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasBManFrmRtaryCnvyr.winfo_containing(canvasBManFrmRtaryCnvyr.winfo_pointerx(), canvasBManFrmRtaryCnvyr.winfo_pointery()):
#         holdBManFrmRtaryCnvyrSwitch = True
#     if direction == "left":
#         canvasBManFrmRtaryCnvyr.itemconfig(imgBManFrmRtaryCnvyr, image=imgBManFrmRtaryCnvyrLeft)
#         stateBManFrmRtaryCnvyr = "left"
#     elif direction == "right":
#         canvasBManFrmRtaryCnvyr.itemconfig(imgBManFrmRtaryCnvyr, image=imgBManFrmRtaryCnvyrRight)
#         stateBManFrmRtaryCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00032': True
#             }})


# def resetBManFrmRtaryCnvyrSwicth(event):
#     global stateBManFrmRtaryCnvyr, imgBManFrmRtaryCnvyrUp, loopAllButtonFalse, holdBManFrmRtaryCnvyrSwitch
#     holdBManFrmRtaryCnvyrSwitch = False
#     loopAllButtonFalse = True
#     print("Arrow reset")
#     canvasBManFrmRtaryCnvyr.itemconfig(imgBManFrmRtaryCnvyr, image=imgBManFrmRtaryCnvyrUp)
#     stateBManFrmRtaryCnvyr = "up"

# ----------------------------------
globals()['holdbtnKananBManUpLadderCnvyr'] = False

def btnKananBManUpLadderCnvyrClick():
    global holdbtnKananBManUpLadderCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManUpLadderCnvyr'] = False
    btnKananBManUpLadderCnvyr.after(hold_time, checkbtnKananBManUpLadderCnvyrhold)
    btnKananBManUpLadderCnvyr.configure(image=imgBManUpLadderCnvyrRight)

def checkbtnKananBManUpLadderCnvyrhold():
    global holdbtnKananBManUpLadderCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManUpLadderCnvyr.winfo_containing(btnKananBManUpLadderCnvyr.winfo_pointerx(),
                                               btnKananBManUpLadderCnvyr.winfo_pointery()):
        holdbtnKananBManUpLadderCnvyr = True
        globals()['J00033'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00033': True
        #     }})

def btnKananBManUpLadderCnvyrClickReset():
    global holdbtnKananBManUpLadderCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManUpLadderCnvyr'] = False
    btnKananBManUpLadderCnvyr.configure(image=imgBManUpLadderCnvyrRightTrans)

# holdBManUpLadderCnvyrSwitch = False

# def changeBManUpLadderCnvyrSwitch(direction):
#     global stateBManUpLadderCnvyr, imgBManUpLadderCnvyr, imgBManUpLadderCnvyrLeft, imgBManUpLadderCnvyrRight, loopAllButtonFalse, holdBManUpLadderCnvyrSwitch
#     loopAllButtonFalse = False
#     holdBManUpLadderCnvyrSwitch = False
#     canvasBManUpLadderCnvyr.after(hold_time, checkBManUpLadderCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasBManUpLadderCnvyr.itemconfig(imgBManUpLadderCnvyr, image=imgBManUpLadderCnvyrLeft)
#         stateBManUpLadderCnvyr = "left"
#     elif direction == "right":
#         canvasBManUpLadderCnvyr.itemconfig(imgBManUpLadderCnvyr, image=imgBManUpLadderCnvyrRight)
#         stateBManUpLadderCnvyr = "right"


# def checkBManUpLadderCnvyrhold(direction):
#     global stateBManUpLadderCnvyr, imgBManUpLadderCnvyr, imgBManUpLadderCnvyrLeft, imgBManUpLadderCnvyrRight, holdBManUpLadderCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasBManUpLadderCnvyr.winfo_containing(canvasBManUpLadderCnvyr.winfo_pointerx(), canvasBManUpLadderCnvyr.winfo_pointery()):
#         holdBManUpLadderCnvyrSwitch = True
#     if direction == "right":
#         canvasBManUpLadderCnvyr.itemconfig(imgBManUpLadderCnvyr, image=imgBManUpLadderCnvyrRight)
#         stateBManUpLadderCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00033': True
#             }})


# def resetBManUpLadderCnvyrSwicth(event):
#     global stateBManUpLadderCnvyr, imgBManUpLadderCnvyrUp, loopAllButtonFalse, holdBManUpLadderCnvyrSwitch
#     holdBManUpLadderCnvyrSwitch = False
#     loopAllButtonFalse = True
#     print("Arrow reset")
#     canvasBManUpLadderCnvyr.itemconfig(imgBManUpLadderCnvyr, image=imgBManUpLadderCnvyrUp)
#     stateBManUpLadderCnvyr = "up"

# ----------------------------------
globals()['holdGreenBManToHopperCnvyr0'] = False


def btnGreenBManToHopperCnvyr0Click():
    global holdGreenBManToHopperCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToHopperCnvyr0'] = False
    btnGreenBManToHopperCnvyr0.after(hold_time, checkGreenBManToHopperCnvyr0hold)
    print("btnGreenBManToHopperCnvyr0Click clicked")
    

def checkGreenBManToHopperCnvyr0hold():
    global holdGreenBManToHopperCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToHopperCnvyr0.winfo_containing(btnGreenBManToHopperCnvyr0.winfo_pointerx(),
                                               btnGreenBManToHopperCnvyr0.winfo_pointery()):
        holdGreenBManToHopperCnvyr0 = True
        globals()['J00020'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00020': True
        #     }})


def btnGreenBManToHopperCnvyr0ClickReset():
    global holdGreenBManToHopperCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToHopperCnvyr0'] = False
    print("btnGreenToRotaryCnvyr0Click Released")

# ----------------------------------
globals()['holdGreenBManToHopperCnvyr1'] = False


def btnGreenBManToHopperCnvyr1Click():
    global holdGreenBManToHopperCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToHopperCnvyr1'] = False
    btnGreenBManToHopperCnvyr1.after(hold_time, checkGreenBManToHopperCnvyr1hold)
    print("btnGreenBManToHopperCnvyr1Click clicked")
    

def checkGreenBManToHopperCnvyr1hold():
    global holdGreenBManToHopperCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToHopperCnvyr1.winfo_containing(btnGreenBManToHopperCnvyr1.winfo_pointerx(),
                                               btnGreenBManToHopperCnvyr1.winfo_pointery()):
        holdGreenBManToHopperCnvyr1 = True
        globals()['J00022'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00022': True
        #     }})


def btnGreenBManToHopperCnvyr1ClickReset():
    global holdGreenBManToHopperCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToHopperCnvyr1'] = False
    print("btnGreenToRotaryCnvyr1Click Released")

# ----------------------------------
globals()['holdGreenBManToHopperCnvyr2'] = False


def btnGreenBManToHopperCnvyr2Click():
    global holdGreenBManToHopperCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToHopperCnvyr2'] = False
    btnGreenBManToHopperCnvyr2.after(hold_time, checkGreenBManToHopperCnvyr2hold)
    print("btnGreenBManToHopperCnvyr2Click clicked")
    

def checkGreenBManToHopperCnvyr2hold():
    global holdGreenBManToHopperCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToHopperCnvyr2.winfo_containing(btnGreenBManToHopperCnvyr2.winfo_pointerx(),
                                               btnGreenBManToHopperCnvyr2.winfo_pointery()):
        holdGreenBManToHopperCnvyr2 = True
        globals()['J00024'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00024': True
        #     }})


def btnGreenBManToHopperCnvyr2ClickReset():
    global holdGreenBManToHopperCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToHopperCnvyr2'] = False
    print("btnGreenToRotaryCnvyr2Click Released")
# ----------------------------------
globals()['holdGreenBManToHopperCnvyr3'] = False


def btnGreenBManToHopperCnvyr3Click():
    global holdGreenBManToHopperCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToHopperCnvyr3'] = False
    btnGreenBManToHopperCnvyr3.after(hold_time, checkGreenBManToHopperCnvyr3hold)
    print("btnGreenBManToHopperCnvyr3Click clicked")
    

def checkGreenBManToHopperCnvyr3hold():
    global holdGreenBManToHopperCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToHopperCnvyr3.winfo_containing(btnGreenBManToHopperCnvyr3.winfo_pointerx(),
                                               btnGreenBManToHopperCnvyr3.winfo_pointery()):
        holdGreenBManToHopperCnvyr3 = True
        globals()['J00026'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00026': True
        #     }})


def btnGreenBManToHopperCnvyr3ClickReset():
    global holdGreenBManToHopperCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToHopperCnvyr3'] = False
    print("btnGreenToRotaryCnvyr3Click Released")

# ----------------------------------
globals()['holdbtnKananBManToHopperCnvyr'] = False

def btnKananBManToHopperCnvyrClick():
    global holdbtnKananBManToHopperCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManToHopperCnvyr'] = False
    btnKananBManToHopperCnvyr.after(hold_time, checkbtnKananBManToHopperCnvyrhold)
    btnKananBManToHopperCnvyr.configure(image=imgBManToHopperCnvyrRight)

def checkbtnKananBManToHopperCnvyrhold():
    global holdbtnKananBManToHopperCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManToHopperCnvyr.winfo_containing(btnKananBManToHopperCnvyr.winfo_pointerx(),
                                               btnKananBManToHopperCnvyr.winfo_pointery()):
        holdbtnKananBManToHopperCnvyr = True
        globals()['J00018'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00018': True
        #     }})

def btnKananBManToHopperCnvyrClickReset():
    global holdbtnKananBManToHopperCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManToHopperCnvyr'] = False
    btnKananBManToHopperCnvyr.configure(image=imgBManToHopperCnvyrRightTrans)

# holdBManToHopperCnvyrSwitch = False


# def changeBManToHopperCnvyrSwitch(direction):
#     global stateBManToHopperCnvyr, imgBManToHopperCnvyr, imgBManToHopperCnvyrLeft, imgBManToHopperCnvyrRight, loopAllButtonFalse, holdBManToHopperCnvyrSwitch
#     loopAllButtonFalse = False
#     holdBManToHopperCnvyrSwitch = False
#     canvasBManToHopperCnvyr.after(hold_time, checkBManToHopperCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasBManToHopperCnvyr.itemconfig(imgBManToHopperCnvyr, image=imgBManToHopperCnvyrLeft)
#         stateBManToHopperCnvyr = "left"
#     elif direction == "right":
#         canvasBManToHopperCnvyr.itemconfig(imgBManToHopperCnvyr, image=imgBManToHopperCnvyrRight)
#         stateBManToHopperCnvyr = "right"


# def checkBManToHopperCnvyrhold(direction):
#     global stateBManToHopperCnvyr, imgBManToHopperCnvyr, imgBManToHopperCnvyrLeft, imgBManToHopperCnvyrRight, holdBManToHopperCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasBManToHopperCnvyr.winfo_containing(canvasBManToHopperCnvyr.winfo_pointerx(), canvasBManToHopperCnvyr.winfo_pointery()):
#         holdBManToHopperCnvyrSwitch = True
#     if direction == "left":
#         canvasBManToHopperCnvyr.itemconfig(imgBManToHopperCnvyr, image=imgBManToHopperCnvyrLeft)
#         stateBManToHopperCnvyr = "left"
#     elif direction == "right":
#         canvasBManToHopperCnvyr.itemconfig(imgBManToHopperCnvyr, image=imgBManToHopperCnvyrRight)
#         stateBManToHopperCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00018': True
#             }})


# def resetBManToHopperCnvyrSwicth(event):
#     global stateBManToHopperCnvyr, imgBManToHopperCnvyrUp, loopAllButtonFalse, holdBManToHopperCnvyrSwitch
#     holdBManToHopperCnvyrSwitch = False
#     loopAllButtonFalse = True
#     print("Arrow reset")
#     canvasBManToHopperCnvyr.itemconfig(imgBManToHopperCnvyr, image=imgBManToHopperCnvyrUp)
#     stateBManToHopperCnvyr = "up"

# ------------
globals()['holdRedManBTbletHoprDoor0'] = False


def btnRedManBTbletHoprDoor0Click():
    global holdRedManBTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManBTbletHoprDoor0'] = False
    btnRedManBTbletHoprDoor0.after(hold_time, checkRedManBTbletHoprDoor0hold)
    print("btnRedManBTbletHoprDoor0Click clicked")
    

def checkRedManBTbletHoprDoor0hold():
    global holdRedManBTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManBTbletHoprDoor0.winfo_containing(btnRedManBTbletHoprDoor0.winfo_pointerx(),
                                             btnRedManBTbletHoprDoor0.winfo_pointery()):
        holdRedManBTbletHoprDoor0 = True
        globals()['J00027'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00027': True
        #     }})
        

def btnRedManBTbletHoprDoor0ClickReset():
    global holdRedManBTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManBTbletHoprDoor0'] = False
    print("btnRedManBTbletHoprDoor0Click Released")


# ------------
globals()['holdGreenManBTbletHoprDoor0'] = False


def btnGreenManBTbletHoprDoor0Click():
    global holdGreenManBTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManBTbletHoprDoor0Click clicked")
    globals()['holdGreenManBTbletHoprDoor0'] = False
    btnGreenManBTbletHoprDoor0.after(hold_time, checkGreenManBTbletHoprDoor0hold)


def checkGreenManBTbletHoprDoor0hold():
    global holdGreenManBTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManBTbletHoprDoor0.winfo_containing(btnGreenManBTbletHoprDoor0.winfo_pointerx(),
                                               btnGreenManBTbletHoprDoor0.winfo_pointery()):
        holdGreenManBTbletHoprDoor0 = True
        globals()['J00028'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00028': True
        #     }})
        

def btnGreenManBTbletHoprDoor0ClickReset():
    global holdGreenManBTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManBTbletHoprDoor0'] = False
    print("btnGreenManBTbletHoprDoor0Click Released")


# ------------
globals()['holdRedManBTbletHoprDoor1'] = False


def btnRedManBTbletHoprDoor1Click():
    global holdRedManBTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManBTbletHoprDoor1'] = False
    btnRedManBTbletHoprDoor1.after(hold_time, checkRedManBTbletHoprDoor1hold)
    print("btnRedManBTbletHoprDoor1Click clicked")
    

def checkRedManBTbletHoprDoor1hold():
    global holdRedManBTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManBTbletHoprDoor1.winfo_containing(btnRedManBTbletHoprDoor1.winfo_pointerx(),
                                             btnRedManBTbletHoprDoor1.winfo_pointery()):
        holdRedManBTbletHoprDoor1 = True
        globals()['J00029'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00029': True
        #     }})
        

def btnRedManBTbletHoprDoor1ClickReset():
    global holdRedManBTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManBTbletHoprDoor1'] = False
    print("btnRedManBTbletHoprDoor1Click Released")


globals()['holdGreenManBTbletHoprDoor1'] = False


def btnGreenManBTbletHoprDoor1Click():
    global holdGreenManBTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManBTbletHoprDoor1Click clicked")
    globals()['holdGreenManBTbletHoprDoor1'] = False
    btnGreenManBTbletHoprDoor1.after(hold_time, checkGreenManBTbletHoprDoor1hold)
    

def checkGreenManBTbletHoprDoor1hold():
    global holdGreenManBTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManBTbletHoprDoor1.winfo_containing(btnGreenManBTbletHoprDoor1.winfo_pointerx(),
                                               btnGreenManBTbletHoprDoor1.winfo_pointery()):
        holdGreenManBTbletHoprDoor1 = True
        globals()['J00030'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00030': True
        #     }})
        

def btnGreenManBTbletHoprDoor1ClickReset():
    global holdGreenManBTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManBTbletHoprDoor1'] = False
    print("btnGreenManBTbletHoprDoor1Click Released")

# ------------
globals()['holdbtnKananBManTbletHoprDoor'] = False

def btnKananBManTbletHoprDoorClick():
    global holdbtnKananBManTbletHoprDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManTbletHoprDoor'] = False
    btnKananBManTbletHoprDoor.after(hold_time, checkbtnKananBManTbletHoprDoorhold)
    btnKananBManTbletHoprDoor.configure(image=imgBManTbletHoprDoorRight)

def checkbtnKananBManTbletHoprDoorhold():
    global holdbtnKananBManTbletHoprDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManTbletHoprDoor.winfo_containing(btnKananBManTbletHoprDoor.winfo_pointerx(),
                                               btnKananBManTbletHoprDoor.winfo_pointery()):
        holdbtnKananBManTbletHoprDoor = True
        globals()['J00031'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00031': True
        #     }})

def btnKananBManTbletHoprDoorClickReset():
    global holdbtnKananBManTbletHoprDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManTbletHoprDoor'] = False
    btnKananBManTbletHoprDoor.configure(image=imgBManTbletHoprDoorRightTrans)

# holdManBTbletHoprDoorSwitch = False


# def changeManBTbletHoprDoorSwitch(direction):
#     global stateManBTbletHoprDoor, imgManBTbletHoprDoor, imgManBTbletHoprDoorLeft, imgManBTbletHoprDoorRight, loopAllButtonFalse, holdManBTbletHoprDoorSwitch
#     loopAllButtonFalse = False
#     holdManBTbletHoprDoorSwitch = False
#     canvasManBTbletHoprDoor.after(hold_time, checkManBTbletHoprDoorhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasManBTbletHoprDoor.itemconfig(imgManBTbletHoprDoor, image=imgManBTbletHoprDoorLeft)
#         stateManBTbletHoprDoor = "left"
#     elif direction == "right":
#         canvasManBTbletHoprDoor.itemconfig(imgManBTbletHoprDoor, image=imgManBTbletHoprDoorRight)
#         stateManBTbletHoprDoor = "right"


# def checkManBTbletHoprDoorhold(direction):
#     global stateManBTbletHoprDoor, imgManBTbletHoprDoor, imgManBTbletHoprDoorLeft, imgManBTbletHoprDoorRight, holdManBTbletHoprDoorSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasManBTbletHoprDoor.winfo_containing(canvasManBTbletHoprDoor.winfo_pointerx(), canvasManBTbletHoprDoor.winfo_pointery()):
#         holdManBTbletHoprDoorSwitch = True
#     if direction == "left":
#         canvasManBTbletHoprDoor.itemconfig(imgManBTbletHoprDoor, image=imgManBTbletHoprDoorLeft)
#         stateManBTbletHoprDoor = "left"
#     elif direction == "right":
#         canvasManBTbletHoprDoor.itemconfig(imgManBTbletHoprDoor, image=imgManBTbletHoprDoorRight)
#         stateManBTbletHoprDoor = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00031': True
#             }})


# def resetManBTbletHoprDoorSwicth(event):
#     global stateManBTbletHoprDoor, imgManBTbletHoprDoorUp, loopAllButtonFalse, holdManBTbletHoprDoorSwitch
#     loopAllButtonFalse = True
#     holdManBTbletHoprDoorSwitch = False
#     print("Arrow reset")
#     canvasManBTbletHoprDoor.itemconfig(imgManBTbletHoprDoor, image=imgManBTbletHoprDoorUp)
#     stateManBTbletHoprDoor = "up"

# ----------------------------------
globals()['holdbtnKananBManToRncenCnvyr'] = False

def btnKananBManToRncenCnvyrClick():
    global holdbtnKananBManToRncenCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananBManToRncenCnvyr'] = False
    btnKananBManToRncenCnvyr.after(hold_time, checkbtnKananBManToRncenCnvyrhold)
    btnKananBManToRncenCnvyr.configure(image=imgBManToRncenCnvyrRight)

def checkbtnKananBManToRncenCnvyrhold():
    global holdbtnKananBManToRncenCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananBManToRncenCnvyr.winfo_containing(btnKananBManToRncenCnvyr.winfo_pointerx(),
                                               btnKananBManToRncenCnvyr.winfo_pointery()):
        holdbtnKananBManToRncenCnvyr = True
        globals()['J00034'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00034': True
        #     }})

def btnKananBManToRncenCnvyrClickReset():
    global holdbtnKananBManToRncenCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananBManToRncenCnvyr'] = False
    btnKananBManToRncenCnvyr.configure(image=imgBManToRncenCnvyrRightTrans)

# holdManBToRncenCnvyrSwitch = False


# def changeManBToRncenCnvyrSwitch(direction):
#     global stateManBToRncenCnvyr, imgManBToRncenCnvyr, imgManBToRncenCnvyrLeft, imgManBToRncenCnvyrRight, loopAllButtonFalse, holdManBToRncenCnvyrSwitch
#     loopAllButtonFalse = False
#     holdManBToRncenCnvyrSwitch = False
#     canvasManBToRncenCnvyr.after(hold_time, checkManBToRncenCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasManBToRncenCnvyr.itemconfig(imgManBToRncenCnvyr, image=imgManBToRncenCnvyrLeft)
#         stateManBToRncenCnvyr = "left"
#     elif direction == "right":
#         canvasManBToRncenCnvyr.itemconfig(imgManBToRncenCnvyr, image=imgManBToRncenCnvyrRight)
#         stateManBToRncenCnvyr = "right"


# def checkManBToRncenCnvyrhold(direction):
#     global stateManBToRncenCnvyr, imgManBToRncenCnvyr, imgManBToRncenCnvyrLeft, imgManBToRncenCnvyrRight, holdManBToRncenCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasManBToRncenCnvyr.winfo_containing(canvasManBToRncenCnvyr.winfo_pointerx(), canvasManBToRncenCnvyr.winfo_pointery()):
#         holdManBToRncenCnvyrSwitch = True
#     if direction == "left":
#         canvasManBToRncenCnvyr.itemconfig(imgManBToRncenCnvyr, image=imgManBToRncenCnvyrLeft)
#         stateManBToRncenCnvyr = "left"
#     elif direction == "right":
#         canvasManBToRncenCnvyr.itemconfig(imgManBToRncenCnvyr, image=imgManBToRncenCnvyrRight)
#         stateManBToRncenCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00034': True
#             }})


# def resetManBToRncenCnvyrSwicth(event):
#     global stateManBToRncenCnvyr, imgManBToRncenCnvyrUp, loopAllButtonFalse, holdManBToRncenCnvyrSwitch
#     loopAllButtonFalse = True
#     holdManBToRncenCnvyrSwitch = False
#     print("Arrow reset")
#     canvasManBToRncenCnvyr.itemconfig(imgManBToRncenCnvyr, image=imgManBToRncenCnvyrUp)
#     stateManBToRncenCnvyr = "up"


# ----------------------------------
globals()['holdGreenBManToRncenCnvyr'] = False


def btnGreenBManToRncenCnvyrClick():
    global holdGreenBManToRncenCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenBManToRncenCnvyr'] = False
    btnGreenBManToRncenCnvyr.after(hold_time, checkGreenBManToRncenCnvyrhold)
    print("btnGreenBManToRncenCnvyrClick clicked")
    

def checkGreenBManToRncenCnvyrhold():
    global holdGreenBManToRncenCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenBManToRncenCnvyr.winfo_containing(btnGreenBManToRncenCnvyr.winfo_pointerx(),
                                             btnGreenBManToRncenCnvyr.winfo_pointery()):
        holdGreenBManToRncenCnvyr = True
        globals()['J00036'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00036': True
        #     }})


def btnGreenBManToRncenCnvyrClickReset():
    global holdGreenBManToRncenCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenBManToRncenCnvyr'] = False
    print("btnGreenToRotaryCnvyr0Click Released")

# ================================================================================
# END LINE B FUNCTION
# ================================================================================















# ================================================================================
# START LINE C FUNCTION - .cfunc
# ================================================================================
def cmdBtnFeederCPutih():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0146': 512
        }})
    # btnAutoFeedPutihC.configure(fg_color="lime", text_color="black")
    # btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnFeederCWarna1():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0146': 256
        }})
    # btnAutoFeedPutihC.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1C.configure(fg_color="red", text_color="black")
    # btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnFeederCWarna2():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0146': 128
        }})
    # btnAutoFeedPutihC.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2C.configure(fg_color="red", text_color="black")
    # btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnFeederCWarna3():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0146': 64
        }})
    # btnAutoFeedPutihC.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3C.configure(fg_color="red", text_color="black")
    # btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnFeederCWarna4():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0146': 32
        }})
    # btnAutoFeedPutihC.configure(fg_color="light green", text_color="white")
    # btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white")
    # btnAutoFeedWarna4C.configure(fg_color="red", text_color="black")
    showAutoBesarC2()

def cmdBtnFeederCManual():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0144': 0,
            'V0145': 0,
            'V0146': 0,
            'V0147': 0
        }})
    btnAutoFeedPutih.configure(fg_color="light green", text_color="white")
    btnAutoFeedWarna1.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna2.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna3.configure(fg_color="pink", text_color="white")
    btnAutoHopperPutih.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1.configure(fg_color="pink", text_color="white")
    btnAutoFeedPutihC.configure(fg_color="light green", text_color="white")
    btnAutoFeedWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoFeedWarna4C.configure(fg_color="pink", text_color="white")
    btnAutoHopperPutihC.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white")
    showBolaA()

def cmdBtnHopperCPutih():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0147': 16
        }})
    btnAutoHopperPutihC.configure(fg_color="lime", text_color="black")
    btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnHopperCWarna1():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0147': 8
        }})
    btnAutoHopperPutihC.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1C.configure(fg_color="red", text_color="black")
    btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnHopperCWarna2():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0147': 4
        }})
    btnAutoHopperPutihC.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna2C.configure(fg_color="red", text_color="black")
    btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnHopperCWarna3():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0147': 2
        }})
    btnAutoHopperPutihC.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna3C.configure(fg_color="red", text_color="black")
    btnAutoHopperWarna4C.configure(fg_color="pink", text_color="white")
    showAutoBesarC2()

def cmdBtnHopperCWarna4():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0147': 1
        }})
    btnAutoHopperPutihC.configure(fg_color="light green", text_color="white")
    btnAutoHopperWarna1C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna2C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna3C.configure(fg_color="pink", text_color="white")
    btnAutoHopperWarna4C.configure(fg_color="red", text_color="black")
    showAutoBesarC2()


# ----------------------------------
holdbtnKiriCManMaterMixRotor = False

def btnKiriCManMaterMixRotorClick():
    global holdbtnKiriCManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKiriCManMaterMixRotor'] = False
    btnKiriCManMaterMixRotor.after(hold_time, checkbtnKiriCManMaterMixRotorhold)
    btnKiriCManMaterMixRotor.configure(image=imgCManMaterMixRotorLeft)

def checkbtnKiriCManMaterMixRotorhold():
    global holdbtnKiriCManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKiriCManMaterMixRotor.winfo_containing(btnKiriCManMaterMixRotor.winfo_pointerx(),
                                               btnKiriCManMaterMixRotor.winfo_pointery()):
        holdbtnKiriCManMaterMixRotor = True
        globals()['J00060'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00060': True
        #     }})

def btnKiriCManMaterMixRotorClickReset():
    global holdbtnKiriCManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKiriCManMaterMixRotor'] = False
    btnKiriCManMaterMixRotor.configure(image=imgCManMaterMixRotorLeftTrans)

# ----------------------------------
globals()['holdbtnKananCManMaterMixRotor'] = False

def btnKananCManMaterMixRotorClick():
    global holdbtnKananCManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManMaterMixRotor'] = False
    btnKananCManMaterMixRotor.after(hold_time, checkbtnKananCManMaterMixRotorhold)
    btnKananCManMaterMixRotor.configure(image=imgCManMaterMixRotorRight)

def checkbtnKananCManMaterMixRotorhold():
    global holdbtnKananCManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManMaterMixRotor.winfo_containing(btnKananCManMaterMixRotor.winfo_pointerx(),
                                               btnKananCManMaterMixRotor.winfo_pointery()):
        holdbtnKananCManMaterMixRotor = True
        globals()['J00059'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00059': True
        #     }})

def btnKananCManMaterMixRotorClickReset():
    global holdbtnKananCManMaterMixRotor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManMaterMixRotor'] = False
    btnKananCManMaterMixRotor.configure(image=imgCManMaterMixRotorRightTrans)



# holdCManMaterMixRotorSwitch = False
# def changeCManMaterMixRotorSwitch(direction):
#     global stateCManMaterMixRotor, imgCManMaterMixRotor, imgCManMaterMixRotorLeft, imgCManMaterMixRotorRight, loopAllButtonFalse, holdCManMaterMixRotorSwitch
#     loopAllButtonFalse = False
#     holdCManMaterMixRotorSwitch = False
#     canvasCManMaterMixRotor.after(hold_time, checkCManMaterMixRotorSwitchhold(direction))
#     if direction == "left":
#         canvasCManMaterMixRotor.itemconfig(imgCManMaterMixRotor, image=imgCManMaterMixRotorLeft)
#         stateCManMaterMixRotor = "left"
#     elif direction == "right":
#         canvasCManMaterMixRotor.itemconfig(imgCManMaterMixRotor, image=imgCManMaterMixRotorRight)
#         stateCManMaterMixRotor = "right"


# def checkCManMaterMixRotorSwitchhold(direction):
#     global stateCManMaterMixRotor, imgCManMaterMixRotor, imgCManMaterMixRotorLeft, imgCManMaterMixRotorRight, holdCManMaterMixRotorSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManMaterMixRotor.winfo_containing(canvasCManMaterMixRotor.winfo_pointerx(), canvasCManMaterMixRotor.winfo_pointery()):
#         holdCManMaterMixRotorSwitch = True
#     if direction == "left":
#         canvasCManMaterMixRotor.itemconfig(imgCManMaterMixRotor, image=imgCManMaterMixRotorLeft)
#         stateCManMaterMixRotor = "left"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00059': False,
#                 'J00060': True
#             }})

#     elif direction == "right":
#         canvasCManMaterMixRotor.itemconfig(imgCManMaterMixRotor, image=imgCManMaterMixRotorRight)
#         stateCManMaterMixRotor = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00059': True,
#                 'J00060': False

#             }})


# def resetCManMaterMixRotorSwicth(event):
#     global stateCManMaterMixRotor, imgCManMaterMixRotorUp, loopAllButtonFalse, holdCManMaterMixRotorSwitch
#     loopAllButtonFalse = True
#     holdCManMaterMixRotorSwitch = False
#     canvasCManMaterMixRotor.itemconfig(imgCManMaterMixRotor, image=imgCManMaterMixRotorUp)
#     stateCManMaterMixRotor = "up"

# ----------------------------------
globals()['holdRedCManMaterMixDoor'] = False


def btnRedCManMaterMixDoorClick():
    global holdRedCManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedCManMaterMixDoor'] = False
    btnRedCManMaterMixDoor.after(hold_time, checkRedCManMaterMixDoorhold)
    print("btnRedCManMaterMixDoorClick clicked")
    

def checkRedCManMaterMixDoorhold():
    global holdRedCManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedCManMaterMixDoor.winfo_containing(btnRedCManMaterMixDoor.winfo_pointerx(), btnRedCManMaterMixDoor.winfo_pointery()):
        holdRedCManMaterMixDoor = True
        globals()['J00061'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00061': True
        #     }})
        


def btnRedCManMaterMixDoorClickReset():
    global holdRedCManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedCManMaterMixDoor'] = False
    print("btnRedCManMaterMixDoorClick Release")


# ----------------------------------
globals()['holdGreenCManMaterMixDoor'] = False

def btnGreenCManMaterMixDoorClick():
    global holdGreenCManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManMaterMixDoor'] = False
    btnGreenCManMaterMixDoor.after(hold_time, checkGreenCManMaterMixDoorhold)
    print("btnGreenCManMaterMixDoorClick clicked")
    

def checkGreenCManMaterMixDoorhold():
    global holdGreenCManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManMaterMixDoor.winfo_containing(btnGreenCManMaterMixDoor.winfo_pointerx(),
                                             btnGreenCManMaterMixDoor.winfo_pointery()):
        holdGreenCManMaterMixDoor = True
        globals()['J00062'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00062': True
        #     }})

def btnGreenCManMaterMixDoorClickReset():
    global holdGreenCManMaterMixDoor, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManMaterMixDoor'] = False
    print("btnGreenCManMaterMixDoorClick Released")

# ----------------------------------
globals()['holdbtnKananCManMateriVbrator'] = False

def btnKananCManMateriVbratorClick():
    global holdbtnKananCManMateriVbrator, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManMateriVbrator'] = False
    btnKananCManMateriVbrator.after(hold_time, checkbtnKananCManMateriVbratorhold)
    btnKananCManMateriVbrator.configure(image=imgCManMateriVbratorRight)

def checkbtnKananCManMateriVbratorhold():
    global holdbtnKananCManMateriVbrator, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManMateriVbrator.winfo_containing(btnKananCManMateriVbrator.winfo_pointerx(),
                                               btnKananCManMateriVbrator.winfo_pointery()):
        holdbtnKananCManMateriVbrator = True
        globals()['J00080'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00080': True
        #     }})

def btnKananCManMateriVbratorClickReset():
    global holdbtnKananCManMateriVbrator, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManMateriVbrator'] = False
    btnKananCManMateriVbrator.configure(image=imgCManMateriVbratorRightTrans)

# holdCManMateriVbratorSwitch = False

# def changeCManMateriVbratorSwitch(direction):
#     global stateCManMateriVbrator, imgCManMateriVbrator, imgCManMateriVbratorLeft, imgCManMateriVbratorRight, loopAllButtonFalse, holdCManMateriVbratorSwitch
#     loopAllButtonFalse = False
#     holdCManMateriVbratorSwitch = False
#     canvasCManMateriVbrator.after(hold_time, checkCManMateriVbratorSwitchhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasCManMateriVbrator.itemconfig(imgCManMateriVbrator, image=imgCManMateriVbratorLeft)
#         stateCManMateriVbrator = "left"
#     elif direction == "right":
#         canvasCManMateriVbrator.itemconfig(imgCManMateriVbrator, image=imgCManMateriVbratorRight)
#         stateCManMateriVbrator = "right"


# def checkCManMateriVbratorSwitchhold(direction):
#     global stateCManMateriVbrator, imgCManMateriVbrator, imgCManMateriVbratorLeft, imgCManMateriVbratorRight, holdCManMateriVbratorSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManMateriVbrator.winfo_containing(canvasCManMateriVbrator.winfo_pointerx(), canvasCManMateriVbrator.winfo_pointery()):
#         holdCManMateriVbratorSwitch = True
#     if direction == "left":
#         canvasCManMateriVbrator.itemconfig(imgCManMateriVbrator, image=imgCManMateriVbratorLeft)
#         stateCManMateriVbrator = "left"

#     elif direction == "right":
#         canvasCManMateriVbrator.itemconfig(imgCManMateriVbrator, image=imgCManMateriVbratorRight)
#         stateCManMateriVbrator = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00080': True
#             }})


# def resetCManMateriVbratorSwicth(event):
#     global stateCManMateriVbrator, imgCManMateriVbratorUp, loopAllButtonFalse, holdCManMateriVbratorSwitch
#     loopAllButtonFalse = True
#     holdCManMateriVbratorSwitch = False
#     print("Arrow reset")
#     canvasCManMateriVbrator.itemconfig(imgCManMateriVbrator, image=imgCManMateriVbratorUp)
#     stateCManMateriVbrator = "up"

# ----------------------------------
globals()['holdbtnKiriCManMatScrewCnvyr'] = False

def btnKiriCManMatScrewCnvyrClick():
    global holdbtnKiriCManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKiriCManMatScrewCnvyr'] = False
    btnKiriCManMatScrewCnvyr.after(hold_time, checkbtnKiriCManMatScrewCnvyrhold)
    btnKiriCManMatScrewCnvyr.configure(image=imgCManMatScrewCnvyrLeft)

def checkbtnKiriCManMatScrewCnvyrhold():
    global holdbtnKiriCManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKiriCManMatScrewCnvyr.winfo_containing(btnKiriCManMatScrewCnvyr.winfo_pointerx(),
                                               btnKiriCManMatScrewCnvyr.winfo_pointery()):
        holdbtnKiriCManMatScrewCnvyr = True
        globals()['J00082'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00082': True
        #     }})

def btnKiriCManMatScrewCnvyrClickReset():
    global holdbtnKiriCManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKiriCManMatScrewCnvyr'] = False
    btnKiriCManMatScrewCnvyr.configure(image=imgCManMatScrewCnvyrLeftTrans)
# ----------------------------------
globals()['holdbtnKananCManMatScrewCnvyr'] = False

def btnKananCManMatScrewCnvyrClick():
    global holdbtnKananCManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManMatScrewCnvyr'] = False
    btnKananCManMatScrewCnvyr.after(hold_time, checkbtnKananCManMatScrewCnvyrhold)
    btnKananCManMatScrewCnvyr.configure(image=imgCManMatScrewCnvyrRight)

def checkbtnKananCManMatScrewCnvyrhold():
    global holdbtnKananCManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManMatScrewCnvyr.winfo_containing(btnKananCManMatScrewCnvyr.winfo_pointerx(),
                                               btnKananCManMatScrewCnvyr.winfo_pointery()):
        holdbtnKananCManMatScrewCnvyr = True
        globals()['J00081'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00081': True
        #     }})

def btnKananCManMatScrewCnvyrClickReset():
    global holdbtnKananCManMatScrewCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManMatScrewCnvyr'] = False
    btnKananCManMatScrewCnvyr.configure(image=imgCManMatScrewCnvyrRightTrans)

# holdCManMatScrewCnvyrSwitch = False

# def changeCManMatScrewCnvyrSwitch(direction):
#     global stateCManMatScrewCnvyr, imgCManMatScrewCnvyr, imgCManMatScrewCnvyrLeft, imgCManMatScrewCnvyrRight, loopAllButtonFalse, holdCManMatScrewCnvyrSwitch
#     holdCManMatScrewCnvyrSwitch = False
#     loopAllButtonFalse = False
#     canvasCManMatScrewCnvyr.after(hold_time, checkCManMatScrewCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasCManMatScrewCnvyr.itemconfig(imgCManMatScrewCnvyr, image=imgCManMatScrewCnvyrLeft)
#         stateCManMatScrewCnvyr = "left"

#     elif direction == "right":
#         canvasCManMatScrewCnvyr.itemconfig(imgCManMatScrewCnvyr, image=imgCManMatScrewCnvyrRight)
#         stateCManMatScrewCnvyr = "right"


# def checkCManMatScrewCnvyrhold(direction):
#     global stateCManMatScrewCnvyr, imgCManMatScrewCnvyr, imgCManMatScrewCnvyrLeft, imgCManMatScrewCnvyrRight, holdCManMatScrewCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManMatScrewCnvyr.winfo_containing(canvasCManMatScrewCnvyr.winfo_pointerx(), canvasCManMatScrewCnvyr.winfo_pointery()):
#         holdCManMatScrewCnvyrSwitch = True
#     if direction == "left":
#         canvasCManMatScrewCnvyr.itemconfig(imgCManMatScrewCnvyr, image=imgCManMatScrewCnvyrLeft)
#         stateCManMatScrewCnvyr = "left"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00082': True,
#                 'J00081': False
#             }})
#     elif direction == "right":
#         canvasCManMatScrewCnvyr.itemconfig(imgCManMatScrewCnvyr, image=imgCManMatScrewCnvyrRight)
#         stateCManMatScrewCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00081': True,
#                 'J00082': False
#             }})


# def resetCManMatScrewCnvyrSwicth(event):
#     global stateCManMatScrewCnvyr, imgCManMatScrewCnvyrUp, loopAllButtonFalse, holdCManMatScrewCnvyrSwitch
#     loopAllButtonFalse = True
#     holdCManMatScrewCnvyrSwitch = False
#     print("Arrow reset")
#     canvasCManMatScrewCnvyr.itemconfig(imgCManMatScrewCnvyr, image=imgCManMatScrewCnvyrUp)
#     stateCManMatScrewCnvyr = "up"

# ----------------------------------
globals()['holdbtnKananCManToRotaryCnvyr'] = False

def btnKananCManToRotaryCnvyrClick():
    global holdbtnKananCManToRotaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManToRotaryCnvyr'] = False
    btnKananCManToRotaryCnvyr.after(hold_time, checkbtnKananCManToRotaryCnvyrhold)
    btnKananCManToRotaryCnvyr.configure(image=imgCManToRotaryCnvyrRight)

def checkbtnKananCManToRotaryCnvyrhold():
    global holdbtnKananCManToRotaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManToRotaryCnvyr.winfo_containing(btnKananCManToRotaryCnvyr.winfo_pointerx(),
                                               btnKananCManToRotaryCnvyr.winfo_pointery()):
        holdbtnKananCManToRotaryCnvyr = True
        globals()['J00063'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00063': True
        #     }})

def btnKananCManToRotaryCnvyrClickReset():
    global holdbtnKananCManToRotaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManToRotaryCnvyr'] = False
    btnKananCManToRotaryCnvyr.configure(image=imgCManToRotaryCnvyrRightTrans)

# holdCManToRotaryCnvyrSwitch = False

# def changeCManToRotaryCnvyrSwitch(direction):
#     global stateCManToRotaryCnvyr, imgCManToRotaryCnvyr, imgCManToRotaryCnvyrLeft, imgCManToRotaryCnvyrRight, loopAllButtonFalse, holdCManToRotaryCnvyrSwitch
#     loopAllButtonFalse = False
#     holdCManToRotaryCnvyrSwitch = False
#     canvasCManToRotaryCnvyr.after(hold_time, checkoRotaryCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasCManToRotaryCnvyr.itemconfig(imgCManToRotaryCnvyr, image=imgCManToRotaryCnvyrLeft)
#         stateCManToRotaryCnvyr = "left"
#     elif direction == "right":
#         canvasCManToRotaryCnvyr.itemconfig(imgCManToRotaryCnvyr, image=imgCManToRotaryCnvyrRight)
#         stateCManToRotaryCnvyr = "right"


# def checkoRotaryCnvyrhold(direction):
#     global stateCManToRotaryCnvyr, imgCManToRotaryCnvyr, imgCManToRotaryCnvyrLeft, imgCManToRotaryCnvyrRight, holdCManToRotaryCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManToRotaryCnvyr.winfo_containing(canvasCManToRotaryCnvyr.winfo_pointerx(), canvasCManToRotaryCnvyr.winfo_pointery()):
#         holdCManToRotaryCnvyrSwitch = True
#     if direction == "left":
#         canvasCManToRotaryCnvyr.itemconfig(imgCManToRotaryCnvyr, image=imgCManToRotaryCnvyrLeft)
#         stateCManToRotaryCnvyr = "left"
#     elif direction == "right":
#         canvasCManToRotaryCnvyr.itemconfig(imgCManToRotaryCnvyr, image=imgCManToRotaryCnvyrRight)
#         stateCManToRotaryCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00063': True
#             }})


# def resetCManToRotaryCnvyrSwicth(event):
#     global stateCManToRotaryCnvyr, imgCManToRotaryCnvyrUp, loopAllButtonFalse, holdCManToRotaryCnvyrSwitch
#     loopAllButtonFalse = True
#     holdCManToRotaryCnvyrSwitch = False
#     print("Arrow reset")
#     canvasCManToRotaryCnvyr.itemconfig(imgCManToRotaryCnvyr, image=imgCManToRotaryCnvyrUp)
#     stateCManToRotaryCnvyr = "up"

# ----------------------------------
globals()['holdGreenCManToRotaryCnvyr0'] = False


def btnGreenCManToRotaryCnvyr0Click():
    global holdGreenCManToRotaryCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToRotaryCnvyr0'] = False
    btnGreenCManToRotaryCnvyr0.after(hold_time, checkGreenCManToRotaryCnvyr0hold)
    print("btnGreenCManToRotaryCnvyr0Click clicked")
    

def checkGreenCManToRotaryCnvyr0hold():
    global holdGreenCManToRotaryCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToRotaryCnvyr0.winfo_containing(btnGreenCManToRotaryCnvyr0.winfo_pointerx(),
                                               btnGreenCManToRotaryCnvyr0.winfo_pointery()):
        holdGreenCManToRotaryCnvyr0 = True
        globals()['J00065'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00065': True
        #     }})


def btnGreenCManToRotaryCnvyr0ClickReset():
    global holdGreenCManToRotaryCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToRotaryCnvyr0'] = False
    print("btnGreenCManToRotaryCnvyr0Click Released")
# ----------------------------------
globals()['holdGreenCManToRotaryCnvyr1'] = False


def btnGreenCManToRotaryCnvyr1Click():
    global holdGreenCManToRotaryCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToRotaryCnvyr1'] = False
    btnGreenCManToRotaryCnvyr1.after(hold_time, checkGreenCManToRotaryCnvyr1hold)
    print("btnGreenCManToRotaryCnvyr1Click clicked")
    

def checkGreenCManToRotaryCnvyr1hold():
    global holdGreenCManToRotaryCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToRotaryCnvyr1.winfo_containing(btnGreenCManToRotaryCnvyr1.winfo_pointerx(),
                                               btnGreenCManToRotaryCnvyr1.winfo_pointery()):
        holdGreenCManToRotaryCnvyr1 = True
        globals()['J00067'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00067': True
        #     }})


def btnGreenCManToRotaryCnvyr1ClickReset():
    global holdGreenCManToRotaryCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToRotaryCnvyr1'] = False
    print("btnGreenCManToRotaryCnvyr1Click Released")
# ----------------------------------
globals()['holdGreenCManToRotaryCnvyr2'] = False


def btnGreenCManToRotaryCnvyr2Click():
    global holdGreenCManToRotaryCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToRotaryCnvyr2'] = False
    btnGreenCManToRotaryCnvyr2.after(hold_time, checkGreenCManToRotaryCnvyr2hold)
    print("btnGreenCManToRotaryCnvyr2Click clicked")
    

def checkGreenCManToRotaryCnvyr2hold():
    global holdGreenCManToRotaryCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToRotaryCnvyr2.winfo_containing(btnGreenCManToRotaryCnvyr2.winfo_pointerx(),
                                               btnGreenCManToRotaryCnvyr2.winfo_pointery()):
        holdGreenCManToRotaryCnvyr2 = True
        globals()['J00069'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00069': True
        #     }})


def btnGreenCManToRotaryCnvyr2ClickReset():
    global holdGreenCManToRotaryCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToRotaryCnvyr2'] = False
    print("btnGreenCManToRotaryCnvyr2Click Released")

# ----------------------------------
globals()['holdbtnKananCManFrmRtaryCnvyr'] = False

def btnKananCManFrmRtaryCnvyrClick():
    global holdbtnKananCManFrmRtaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManFrmRtaryCnvyr'] = False
    btnKananCManFrmRtaryCnvyr.after(hold_time, checkbtnKananCManFrmRtaryCnvyrhold)
    btnKananCManFrmRtaryCnvyr.configure(image=imgCManFrmRtaryCnvyrRight)

def checkbtnKananCManFrmRtaryCnvyrhold():
    global holdbtnKananCManFrmRtaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManFrmRtaryCnvyr.winfo_containing(btnKananCManFrmRtaryCnvyr.winfo_pointerx(),
                                               btnKananCManFrmRtaryCnvyr.winfo_pointery()):
        holdbtnKananCManFrmRtaryCnvyr = True
        globals()['J00083'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00083': True
        #     }})

def btnKananCManFrmRtaryCnvyrClickReset():
    global holdbtnKananCManFrmRtaryCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManFrmRtaryCnvyr'] = False
    btnKananCManFrmRtaryCnvyr.configure(image=imgCManFrmRtaryCnvyrRightTrans)

# holdCManFrmRtaryCnvyrSwitch = False


# def changeCManFrmRtaryCnvyrSwitch(direction):
#     global stateCManFrmRtaryCnvyr, imgCManFrmRtaryCnvyr, imgCManFrmRtaryCnvyrLeft, imgCManFrmRtaryCnvyrRight, loopAllButtonFalse, holdCManFrmRtaryCnvyrSwitch
#     holdCManFrmRtaryCnvyrSwitch = False
#     loopAllButtonFalse = False
#     canvasCManFrmRtaryCnvyr.after(hold_time, checkCManFrmRtaryCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasCManFrmRtaryCnvyr.itemconfig(imgCManFrmRtaryCnvyr, image=imgCManFrmRtaryCnvyrLeft)
#         stateCManFrmRtaryCnvyr = "left"
#     elif direction == "right":
#         canvasCManFrmRtaryCnvyr.itemconfig(imgCManFrmRtaryCnvyr, image=imgCManFrmRtaryCnvyrRight)
#         stateCManFrmRtaryCnvyr = "right"


# def checkCManFrmRtaryCnvyrhold(direction):
#     global stateCManFrmRtaryCnvyr, imgCManFrmRtaryCnvyr, imgCManFrmRtaryCnvyrLeft, imgCManFrmRtaryCnvyrRight, holdCManFrmRtaryCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManFrmRtaryCnvyr.winfo_containing(canvasCManFrmRtaryCnvyr.winfo_pointerx(), canvasCManFrmRtaryCnvyr.winfo_pointery()):
#         holdCManFrmRtaryCnvyrSwitch = True
#     if direction == "left":
#         canvasCManFrmRtaryCnvyr.itemconfig(imgCManFrmRtaryCnvyr, image=imgCManFrmRtaryCnvyrLeft)
#         stateCManFrmRtaryCnvyr = "left"
#     elif direction == "right":
#         canvasCManFrmRtaryCnvyr.itemconfig(imgCManFrmRtaryCnvyr, image=imgCManFrmRtaryCnvyrRight)
#         stateCManFrmRtaryCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00083': True
#             }})


# def resetCManFrmRtaryCnvyrSwicth(event):
#     global stateCManFrmRtaryCnvyr, imgCManFrmRtaryCnvyrUp, loopAllButtonFalse, holdCManFrmRtaryCnvyrSwitch
#     holdCManFrmRtaryCnvyrSwitch = False
#     loopAllButtonFalse = True
#     print("Arrow reset")
#     canvasCManFrmRtaryCnvyr.itemconfig(imgCManFrmRtaryCnvyr, image=imgCManFrmRtaryCnvyrUp)
#     stateCManFrmRtaryCnvyr = "up"

# ----------------------------------
globals()['holdbtnKananCManUpLadderCnvyr'] = False

def btnKananCManUpLadderCnvyrClick():
    global holdbtnKananCManUpLadderCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManUpLadderCnvyr'] = False
    btnKananCManUpLadderCnvyr.after(hold_time, checkbtnKananCManUpLadderCnvyrhold)
    btnKananCManUpLadderCnvyr.configure(image=imgCManUpLadderCnvyrRight)

def checkbtnKananCManUpLadderCnvyrhold():
    global holdbtnKananCManUpLadderCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManUpLadderCnvyr.winfo_containing(btnKananCManUpLadderCnvyr.winfo_pointerx(),
                                               btnKananCManUpLadderCnvyr.winfo_pointery()):
        holdbtnKananCManUpLadderCnvyr = True
        globals()['J00084'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00084': True
        #     }})

def btnKananCManUpLadderCnvyrClickReset():
    global holdbtnKananCManUpLadderCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManUpLadderCnvyr'] = False
    btnKananCManUpLadderCnvyr.configure(image=imgCManUpLadderCnvyrRightTrans)

# holdCManUpLadderCnvyrSwitch = False

# def changeCManUpLadderCnvyrSwitch(direction):
#     global stateCManUpLadderCnvyr, imgCManUpLadderCnvyr, imgCManUpLadderCnvyrLeft, imgCManUpLadderCnvyrRight, loopAllButtonFalse, holdCManUpLadderCnvyrSwitch
#     loopAllButtonFalse = False
#     holdCManUpLadderCnvyrSwitch = False
#     canvasCManUpLadderCnvyr.after(hold_time, checkCManUpLadderCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasCManUpLadderCnvyr.itemconfig(imgCManUpLadderCnvyr, image=imgCManUpLadderCnvyrLeft)
#         stateCManUpLadderCnvyr = "left"
#     elif direction == "right":
#         canvasCManUpLadderCnvyr.itemconfig(imgCManUpLadderCnvyr, image=imgCManUpLadderCnvyrRight)
#         stateCManUpLadderCnvyr = "right"


# def checkCManUpLadderCnvyrhold(direction):
#     global stateCManUpLadderCnvyr, imgCManUpLadderCnvyr, imgCManUpLadderCnvyrLeft, imgCManUpLadderCnvyrRight, holdCManUpLadderCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManUpLadderCnvyr.winfo_containing(canvasCManUpLadderCnvyr.winfo_pointerx(), canvasCManUpLadderCnvyr.winfo_pointery()):
#         holdCManUpLadderCnvyrSwitch = True
#     if direction == "right":
#         canvasCManUpLadderCnvyr.itemconfig(imgCManUpLadderCnvyr, image=imgCManUpLadderCnvyrRight)
#         stateCManUpLadderCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00084': True
#             }})


# def resetCManUpLadderCnvyrSwicth(event):
#     global stateCManUpLadderCnvyr, imgCManUpLadderCnvyrUp, loopAllButtonFalse, holdCManUpLadderCnvyrSwitch
#     holdCManUpLadderCnvyrSwitch = False
#     loopAllButtonFalse = True
#     print("Arrow reset")
#     canvasCManUpLadderCnvyr.itemconfig(imgCManUpLadderCnvyr, image=imgCManUpLadderCnvyrUp)
#     stateCManUpLadderCnvyr = "up"

# ----------------------------------
globals()['holdbtnKananCManToHopperCnvyr'] = False

def btnKananCManToHopperCnvyrClick():
    global holdbtnKananCManToHopperCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdbtnKananCManToHopperCnvyr'] = False
    btnKananCManToHopperCnvyr.after(hold_time, checkbtnKananCManToHopperCnvyrhold)
    btnKananCManToHopperCnvyr.configure(image=imgCManToHopperCnvyrRight)

def checkbtnKananCManToHopperCnvyrhold():
    global holdbtnKananCManToHopperCnvyr, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnKananCManToHopperCnvyr.winfo_containing(btnKananCManToHopperCnvyr.winfo_pointerx(),
                                               btnKananCManToHopperCnvyr.winfo_pointery()):
        holdbtnKananCManToHopperCnvyr = True
        globals()['J00085'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00085': True
        #     }})

def btnKananCManToHopperCnvyrClickReset():
    global holdbtnKananCManToHopperCnvyr, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdbtnKananCManToHopperCnvyr'] = False
    btnKananCManToHopperCnvyr.configure(image=imgCManToHopperCnvyrRightTrans)

# holdCManToHopperCnvyrSwitch = False


# def changeCManToHopperCnvyrSwitch(direction):
#     global stateCManToHopperCnvyr, imgCManToHopperCnvyr, imgCManToHopperCnvyrLeft, imgCManToHopperCnvyrRight, loopAllButtonFalse, holdCManToHopperCnvyrSwitch
#     loopAllButtonFalse = False
#     holdCManToHopperCnvyrSwitch = False
#     canvasCManToHopperCnvyr.after(hold_time, checkCManToHopperCnvyrhold(direction))
#     # Gambar panah
#     if direction == "left":
#         canvasCManToHopperCnvyr.itemconfig(imgCManToHopperCnvyr, image=imgCManToHopperCnvyrLeft)
#         stateCManToHopperCnvyr = "left"
#     elif direction == "right":
#         canvasCManToHopperCnvyr.itemconfig(imgCManToHopperCnvyr, image=imgCManToHopperCnvyrRight)
#         stateCManToHopperCnvyr = "right"


# def checkCManToHopperCnvyrhold(direction):
#     global stateCManToHopperCnvyr, imgCManToHopperCnvyr, imgCManToHopperCnvyrLeft, imgCManToHopperCnvyrRight, holdCManToHopperCnvyrSwitch, loopAllButtonFalse
#     loopAllButtonFalse = False
#     if canvasCManToHopperCnvyr.winfo_containing(canvasCManToHopperCnvyr.winfo_pointerx(), canvasCManToHopperCnvyr.winfo_pointery()):
#         holdCManToHopperCnvyrSwitch = True
#     if direction == "left":
#         canvasCManToHopperCnvyr.itemconfig(imgCManToHopperCnvyr, image=imgCManToHopperCnvyrLeft)
#         stateCManToHopperCnvyr = "left"
#     elif direction == "right":
#         canvasCManToHopperCnvyr.itemconfig(imgCManToHopperCnvyr, image=imgCManToHopperCnvyrRight)
#         stateCManToHopperCnvyr = "right"
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00085': True
#             }})


# def resetCManToHopperCnvyrSwicth(event):
#     global stateCManToHopperCnvyr, imgCManToHopperCnvyrUp, loopAllButtonFalse, holdCManToHopperCnvyrSwitch
#     holdCManToHopperCnvyrSwitch = False
#     loopAllButtonFalse = True
#     print("Arrow reset")
#     canvasCManToHopperCnvyr.itemconfig(imgCManToHopperCnvyr, image=imgCManToHopperCnvyrUp)
#     stateCManToHopperCnvyr = "up"

# ----------------------------------
globals()['holdGreenCManToHopperCnvyr0'] = False


def btnGreenCManToHopperCnvyr0Click():
    global holdGreenCManToHopperCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToHopperCnvyr0'] = False
    btnGreenCManToHopperCnvyr0.after(hold_time, checkGreenCManToHopperCnvyr0hold)
    print("btnGreenCManToHopperCnvyr0Click clicked")
    

def checkGreenCManToHopperCnvyr0hold():
    global holdGreenCManToHopperCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToHopperCnvyr0.winfo_containing(btnGreenCManToHopperCnvyr0.winfo_pointerx(),
                                               btnGreenCManToHopperCnvyr0.winfo_pointery()):
        holdGreenCManToHopperCnvyr0 = True
        globals()['J00087'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00087': True
        #     }})


def btnGreenCManToHopperCnvyr0ClickReset():
    global holdGreenCManToHopperCnvyr0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToHopperCnvyr0'] = False
    print("btnGreenToRotaryCnvyr0Click Released")

# ----------------------------------
globals()['holdGreenCManToHopperCnvyr1'] = False


def btnGreenCManToHopperCnvyr1Click():
    global holdGreenCManToHopperCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToHopperCnvyr1'] = False
    btnGreenCManToHopperCnvyr1.after(hold_time, checkGreenCManToHopperCnvyr1hold)
    print("btnGreenCManToHopperCnvyr1Click clicked")
    

def checkGreenCManToHopperCnvyr1hold():
    global holdGreenCManToHopperCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToHopperCnvyr1.winfo_containing(btnGreenCManToHopperCnvyr1.winfo_pointerx(),
                                               btnGreenCManToHopperCnvyr1.winfo_pointery()):
        holdGreenCManToHopperCnvyr1 = True
        globals()['J00089'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00089': True
        #     }})


def btnGreenCManToHopperCnvyr1ClickReset():
    global holdGreenCManToHopperCnvyr1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToHopperCnvyr1'] = False
    print("btnGreenToRotaryCnvyr1Click Released")

# ----------------------------------
globals()['holdGreenCManToHopperCnvyr2'] = False


def btnGreenCManToHopperCnvyr2Click():
    global holdGreenCManToHopperCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToHopperCnvyr2'] = False
    btnGreenCManToHopperCnvyr2.after(hold_time, checkGreenCManToHopperCnvyr2hold)
    print("btnGreenCManToHopperCnvyr2Click clicked")
    

def checkGreenCManToHopperCnvyr2hold():
    global holdGreenCManToHopperCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToHopperCnvyr2.winfo_containing(btnGreenCManToHopperCnvyr2.winfo_pointerx(),
                                               btnGreenCManToHopperCnvyr2.winfo_pointery()):
        holdGreenCManToHopperCnvyr2 = True
        globals()['J00091'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00091': True
        #     }})


def btnGreenCManToHopperCnvyr2ClickReset():
    global holdGreenCManToHopperCnvyr2, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToHopperCnvyr2'] = False
    print("btnGreenToRotaryCnvyr2Click Released")
# ----------------------------------
globals()['holdGreenCManToHopperCnvyr3'] = False


def btnGreenCManToHopperCnvyr3Click():
    global holdGreenCManToHopperCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToHopperCnvyr3'] = False
    btnGreenCManToHopperCnvyr3.after(hold_time, checkGreenCManToHopperCnvyr3hold)
    print("btnGreenCManToHopperCnvyr3Click clicked")
    


def checkGreenCManToHopperCnvyr3hold():
    global holdGreenCManToHopperCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToHopperCnvyr3.winfo_containing(btnGreenCManToHopperCnvyr3.winfo_pointerx(),
                                               btnGreenCManToHopperCnvyr3.winfo_pointery()):
        globals()['J00093'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00093': True
        #     }})
        holdGreenCManToHopperCnvyr3 = True


def btnGreenCManToHopperCnvyr3ClickReset():
    global holdGreenCManToHopperCnvyr3, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToHopperCnvyr3'] = False
    print("btnGreenToRotaryCnvyr3Click Released")

# ----------------------------------
globals()['holdGreenCManToHopperCnvyr4'] = False


def btnGreenCManToHopperCnvyr4Click():
    global holdGreenCManToHopperCnvyr4, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdGreenCManToHopperCnvyr4'] = False
    btnGreenCManToHopperCnvyr4.after(hold_time, checkGreenCManToHopperCnvyr4hold)
    print("btnGreenCManToHopperCnvyr4Click clicked")
    

def checkGreenCManToHopperCnvyr4hold():
    global holdGreenCManToHopperCnvyr4, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenCManToHopperCnvyr4.winfo_containing(btnGreenCManToHopperCnvyr4.winfo_pointerx(),
                                               btnGreenCManToHopperCnvyr4.winfo_pointery()):
        holdGreenCManToHopperCnvyr4 = True
        globals()['J00095'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00095': True
        #     }})


def btnGreenCManToHopperCnvyr4ClickReset():
    global holdGreenCManToHopperCnvyr4, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenCManToHopperCnvyr4'] = False
    print("btnGreenToRotaryCnvyr4Click Released")

# ------------
globals()['holdRedManCTbletHoprDoor0'] = False


def btnRedManCTbletHoprDoor0Click():
    global holdRedManCTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManCTbletHoprDoor0'] = False
    btnRedManCTbletHoprDoor0.after(hold_time, checkRedManCTbletHoprDoor0hold)
    print("btnRedManCTbletHoprDoor0Click clicked")
    

def checkRedManCTbletHoprDoor0hold():
    global holdRedManCTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManCTbletHoprDoor0.winfo_containing(btnRedManCTbletHoprDoor0.winfo_pointerx(),
                                             btnRedManCTbletHoprDoor0.winfo_pointery()):
        holdRedManCTbletHoprDoor0 = True
        globals()['J00070'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00070': True
        #     }})
        

def btnRedManCTbletHoprDoor0ClickReset():
    global holdRedManCTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManCTbletHoprDoor0'] = False
    print("btnRedManCTbletHoprDoor0Click Released")


# ------------
globals()['holdGreenManCTbletHoprDoor0'] = False


def btnGreenManCTbletHoprDoor0Click():
    global holdGreenManCTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManCTbletHoprDoor0Click clicked")
    globals()['holdGreenManCTbletHoprDoor0'] = False
    btnGreenManCTbletHoprDoor0.after(hold_time, checkGreenManCTbletHoprDoor0hold)


def checkGreenManCTbletHoprDoor0hold():
    global holdGreenManCTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManCTbletHoprDoor0.winfo_containing(btnGreenManCTbletHoprDoor0.winfo_pointerx(),
                                               btnGreenManCTbletHoprDoor0.winfo_pointery()):
        holdGreenManCTbletHoprDoor0 = True
        globals()['J00071'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00071': True
        #     }})
        

def btnGreenManCTbletHoprDoor0ClickReset():
    global holdGreenManCTbletHoprDoor0, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManCTbletHoprDoor0'] = False
    print("btnGreenManCTbletHoprDoor0Click Released")


# ------------
globals()['holdRedManCTbletHoprDoor1'] = False


def btnRedManCTbletHoprDoor1Click():
    global holdRedManCTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManCTbletHoprDoor1'] = False
    btnRedManCTbletHoprDoor1.after(hold_time, checkRedManCTbletHoprDoor1hold)
    print("btnRedManCTbletHoprDoor1Click clicked")
    

def checkRedManCTbletHoprDoor1hold():
    global holdRedManCTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManCTbletHoprDoor1.winfo_containing(btnRedManCTbletHoprDoor1.winfo_pointerx(),
                                             btnRedManCTbletHoprDoor1.winfo_pointery()):
        holdRedManCTbletHoprDoor1 = True
        globals()['J00072'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00072': True
        #     }})
        

def btnRedManCTbletHoprDoor1ClickReset():
    global holdRedManCTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManCTbletHoprDoor1'] = False
    print("btnRedManCTbletHoprDoor1Click Released")

# ------------
globals()['holdGreenManCTbletHoprDoor1'] = False


def btnGreenManCTbletHoprDoor1Click():
    global holdGreenManCTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManCTbletHoprDoor1Click clicked")
    globals()['holdGreenManCTbletHoprDoor1'] = False
    btnGreenManCTbletHoprDoor1.after(hold_time, checkGreenManCTbletHoprDoor1hold)
    

def checkGreenManCTbletHoprDoor1hold():
    global holdGreenManCTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManCTbletHoprDoor1.winfo_containing(btnGreenManCTbletHoprDoor1.winfo_pointerx(),
                                               btnGreenManCTbletHoprDoor1.winfo_pointery()):
        holdGreenManCTbletHoprDoor1 = True
        globals()['J00073'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00073': True
        #     }})
        

def btnGreenManCTbletHoprDoor1ClickReset():
    global holdGreenManCTbletHoprDoor1, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManCTbletHoprDoor1'] = False
    print("btnGreenManCTbletHoprDoor1Click Released")

# ------------
globals()['holdRedManCTbletHoprDoor2'] = False


def btnRedManCTbletHoprDoor2Click():
    global holdRedManCTbletHoprDoor2, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManCTbletHoprDoor2'] = False
    btnRedManCTbletHoprDoor2.after(hold_time, checkRedManCTbletHoprDoor2hold)
    print("btnRedManCTbletHoprDoor2Click clicked")
    

def checkRedManCTbletHoprDoor2hold():
    global holdRedManCTbletHoprDoor2, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManCTbletHoprDoor2.winfo_containing(btnRedManCTbletHoprDoor2.winfo_pointerx(),
                                             btnRedManCTbletHoprDoor2.winfo_pointery()):
        holdRedManCTbletHoprDoor2 = True
        globals()['J00074'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00074': True
        #     }})
        

def btnRedManCTbletHoprDoor2ClickReset():
    global holdRedManCTbletHoprDoor2, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManCTbletHoprDoor2'] = False
    print("btnRedManCTbletHoprDoor2Click Released")

# ------------
globals()['holdGreenManCTbletHoprDoor2'] = False


def btnGreenManCTbletHoprDoor2Click():
    global holdGreenManCTbletHoprDoor2, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManCTbletHoprDoor2Click clicked")
    globals()['holdGreenManCTbletHoprDoor2'] = False
    btnGreenManCTbletHoprDoor2.after(hold_time, checkGreenManCTbletHoprDoor2hold)
    

def checkGreenManCTbletHoprDoor2hold():
    global holdGreenManCTbletHoprDoor2, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManCTbletHoprDoor2.winfo_containing(btnGreenManCTbletHoprDoor2.winfo_pointerx(),
                                               btnGreenManCTbletHoprDoor2.winfo_pointery()):
        holdGreenManCTbletHoprDoor2 = True
        globals()['J00075'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00075': True
        #     }})
        

def btnGreenManCTbletHoprDoor2ClickReset():
    global holdGreenManCTbletHoprDoor2, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManCTbletHoprDoor2'] = False
    print("btnGreenManCTbletHoprDoor2Click Released")

# ------------
globals()['holdRedManCTbletHoprDoor3'] = False


def btnRedManCTbletHoprDoor3Click():
    global holdRedManCTbletHoprDoor3, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManCTbletHoprDoor3'] = False
    btnRedManCTbletHoprDoor3.after(hold_time, checkRedManCTbletHoprDoor3hold)
    print("btnRedManCTbletHoprDoor3Click clicked")
    

def checkRedManCTbletHoprDoor3hold():
    global holdRedManCTbletHoprDoor3, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManCTbletHoprDoor3.winfo_containing(btnRedManCTbletHoprDoor3.winfo_pointerx(),
                                             btnRedManCTbletHoprDoor3.winfo_pointery()):
        holdRedManCTbletHoprDoor3 = True
        globals()['J00076'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00076': True
        #     }})
        

def btnRedManCTbletHoprDoor3ClickReset():
    global holdRedManCTbletHoprDoor3, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManCTbletHoprDoor3'] = False
    print("btnRedManCTbletHoprDoor3Click Released")

# ------------
globals()['holdGreenManCTbletHoprDoor3'] = False


def btnGreenManCTbletHoprDoor3Click():
    global holdGreenManCTbletHoprDoor3, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManCTbletHoprDoor3Click clicked")
    globals()['holdGreenManCTbletHoprDoor3'] = False
    btnGreenManCTbletHoprDoor3.after(hold_time, checkGreenManCTbletHoprDoor3hold)
    

def checkGreenManCTbletHoprDoor3hold():
    global holdGreenManCTbletHoprDoor3, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManCTbletHoprDoor3.winfo_containing(btnGreenManCTbletHoprDoor3.winfo_pointerx(),
                                               btnGreenManCTbletHoprDoor3.winfo_pointery()):
        holdGreenManCTbletHoprDoor3 = True
        globals()['J00077'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00077': True
        #     }})
        

def btnGreenManCTbletHoprDoor3ClickReset():
    global holdGreenManCTbletHoprDoor3, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManCTbletHoprDoor3'] = False
    print("btnGreenManCTbletHoprDoor3Click Released")

# ------------
globals()['holdRedManCTbletHoprDoor4'] = False


def btnRedManCTbletHoprDoor4Click():
    global holdRedManCTbletHoprDoor4, loopAllButtonFalse
    loopAllButtonFalse = False
    globals()['holdRedManCTbletHoprDoor4'] = False
    btnRedManCTbletHoprDoor4.after(hold_time, checkRedManCTbletHoprDoor4hold)
    print("btnRedManCTbletHoprDoor4Click clicked")
    

def checkRedManCTbletHoprDoor4hold():
    global holdRedManCTbletHoprDoor4, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnRedManCTbletHoprDoor4.winfo_containing(btnRedManCTbletHoprDoor4.winfo_pointerx(),
                                             btnRedManCTbletHoprDoor4.winfo_pointery()):
        holdRedManCTbletHoprDoor4 = True
        globals()['J00078'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00078': True
        #     }})
        

def btnRedManCTbletHoprDoor4ClickReset():
    global holdRedManCTbletHoprDoor4, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdRedManCTbletHoprDoor4'] = False
    print("btnRedManCTbletHoprDoor4Click Released")

# ------------
globals()['holdGreenManCTbletHoprDoor4'] = False


def btnGreenManCTbletHoprDoor4Click():
    global holdGreenManCTbletHoprDoor4, loopAllButtonFalse
    loopAllButtonFalse = False
    print("btnGreenManCTbletHoprDoor4Click clicked")
    globals()['holdGreenManCTbletHoprDoor4'] = False
    btnGreenManCTbletHoprDoor4.after(hold_time, checkGreenManCTbletHoprDoor4hold)
    

def checkGreenManCTbletHoprDoor4hold():
    global holdGreenManCTbletHoprDoor4, loopAllButtonFalse
    loopAllButtonFalse = False
    if btnGreenManCTbletHoprDoor4.winfo_containing(btnGreenManCTbletHoprDoor4.winfo_pointerx(),
                                               btnGreenManCTbletHoprDoor4.winfo_pointery()):
        holdGreenManCTbletHoprDoor4 = True
        globals()['J00079'] = True
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00079': True
        #     }})
        

def btnGreenManCTbletHoprDoor4ClickReset():
    global holdGreenManCTbletHoprDoor4, loopAllButtonFalse
    loopAllButtonFalse = True
    globals()['holdGreenManCTbletHoprDoor4'] = False
    print("btnGreenManCTbletHoprDoor4Click Released")


# DEBUG CODE .debug
# def startMixingTimerB():
#     globals()['startTimeB'] = time.time()
#     globals()['timerBrunning'] = True
#     print(f"globals()['startTimeB'] : {globals()['startTimeB']} - globals()['timerBrunning'] : {globals()['timerBrunning']}")

def startMixingTimerC():
    globals()['startTimeC'] = time.time()
    globals()['timerCrunning'] = True
    print(f"globals()['startTimeC'] : {globals()['startTimeC']} - globals()['timerCrunning'] : {globals()['timerCrunning']}")

# ================================================================================
# END LINE C FUNCTION
# ================================================================================

lightOrange_rgb = (247, 223, 192)  # RGB untuk oranye
lightOrange = rgb_to_hex(lightOrange_rgb)

# # ================================================================================
# # LINE A - UI UX - MANUAL - .aman
# # ================================================================================
# frame_tabManualMixer = ctk.CTkFrame(app, fg_color="white")
# frame_tabManualMixer.pack(fill="both", expand=True)


# ================================================================================
# LINE Z - UI UX - AUTO - .zauto1
# ================================================================================
frame_tabCommonZAuto2 = ctk.CTkFrame(app, fg_color="white")
frame_tabCommonZAuto2.pack(fill="both", expand=True)

# START FeederDoor
frm_FeederDoor = ctk.CTkFrame(frame_tabCommonZAuto2, fg_color="white")
frm_FeederDoor.grid(row=0, column=0, padx=1, pady=1)

lbl_MatCol = ctk.CTkLabel(frm_FeederDoor, text="Feeder Door (Material Z)", font=('Helvetica', 16))
lbl_MatCol.grid(row=0, column=0, columnspan=5, pady=1)

frm_BtnWarna = ctk.CTkFrame(frm_FeederDoor)
frm_BtnWarna.grid(row=1, column=0, pady=1)

btnZManLineA = ctk.CTkButton(frm_BtnWarna, text="Line A (Kecil)", text_color="black", fg_color="light green", border_color="black", border_width=5,
                                 command=cmdBtnZLineA, height=btnSize)
btnZManLineA.grid(row=1, column=0, padx=5, pady=(10, 10))

btnZManLineB = ctk.CTkButton(frm_BtnWarna, text="Line B (Besar)", text_color="black", fg_color="pink", border_color="black", border_width=5,
                                  command=cmdBtnZLineB, height=btnSize)
btnZManLineB.grid(row=1, column=1, padx=5, pady=(10, 10))

btnZManLineC = ctk.CTkButton(frm_BtnWarna, text="Line C (Bola)", text_color="black", fg_color="pink", border_color="black", border_width=5,
                                  command=cmdBtnZLineC, height=btnSize)
btnZManLineC.grid(row=1, column=2, padx=5, pady=(10, 10))

btnZManManual = ctk.CTkButton(frm_FeederDoor, text="Manual", fg_color="red", border_color="black", border_width=5,
                                 command=showCommonManwithReset, height=btnSize)
btnZManManual.grid(row=1, column=5, padx=20, pady=(10, 10))
# END FeederDoor





# Membuka gambar dan mengubah ukurannya
img = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'Common.png'))  # Ganti dengan path gambar yang ingin kamu gunakan
resized_img = img.resize((650, 500))  # Atur ukuran sesuai kebutuhan

# Konversi gambar agar bisa digunakan dalam tkinter
ctk_imageAutoZ = ctk.CTkImage(resized_img, size=(650, 500))

# frame_tabAutoLineZ = ctk.CTkFrame(app, fg_color="white")
# frame_tabAutoLineZ.pack(fill="both", expand=True)


frm_BesarC3LineBawah = ctk.CTkFrame(frame_tabCommonZAuto2, fg_color="white")
frm_BesarC3LineBawah.grid(row=3, column=0, padx=(0,180), pady=1)

label_with_image = ctk.CTkLabel(frm_BesarC3LineBawah, image=ctk_imageAutoZ, text="")  # Kosongkan teks agar hanya gambar yang tampil
label_with_image.pack(pady=(1,0))



# Membuat frame untuk border
frame_with_border00 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border00.grid(row=0, column=0, padx=(0,300), pady=(0,50))

lbl_ToRotaryCnvyr1 = ctk.CTkLabel(frame_with_border00, text="Conveyor Slitting", font=('Helvetica', 7))
lbl_ToRotaryCnvyr1.grid(row=0, column=0, padx=3, pady=2)

btnMotorToRotaryCnvyrZ = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorToRotaryCnvyrZ.grid(row=0, column=0, padx=(0,300), pady=(20,1))


frame_with_border312 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border312.grid(row=0, column=0,padx=(240,0), pady=(0,50))

lbl_MatScrewCnvyr1 = ctk.CTkLabel(frame_with_border312, text="Bag Slitter Cuter", font=('Helvetica', 7))
lbl_MatScrewCnvyr1.grid(row=0, column=0,padx=3, pady=2)

btnMotorMatScrewCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorMatScrewCnvyr.grid(row=0, column=0, padx=(240,0), pady=(20,1))


frame_with_border314 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border314.grid(row=0, column=0,padx=(240,0), pady=(140,50))

lbl_MatScrewCnvyr1 = ctk.CTkLabel(frame_with_border314, text="Bag Holder", font=('Helvetica', 7))
lbl_MatScrewCnvyr1.grid(row=0, column=0,padx=3, pady=2)

btnMotorMatScrewCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorMatScrewCnvyr.grid(row=0, column=0, padx=(240,0), pady=(160,1))


frame_with_border313 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border313.grid(row=0, column=0,padx=(480,0), pady=(0,50))

lbl_MatScrewCnvyr2 = ctk.CTkLabel(frame_with_border313, text="Pneum\nFeedThreeDoor", font=('Helvetica', 7))
lbl_MatScrewCnvyr2.grid(row=0, column=0,padx=3, pady=2)
# btnMotorMatScrewCnvyr2
btnPneumFeedDoor = ctk.CTkButton(label_with_image, text="Line A", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnPneumFeedDoor.grid(row=0, column=0, padx=(480,0), pady=(20,1))



frm_MixerC = ctk.CTkFrame(label_with_image, fg_color="white")
frm_MixerC.grid(row=0, column=0, padx=(750,0), pady=(0,380))

frame_with_border3p = ctk.CTkFrame(frm_MixerC, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border3p.grid(row=0, column=0,padx=1, pady=(0,1))

lbl_Matermixdoor = ctk.CTkLabel(frame_with_border3p, text="Pintu Mixer Line C", font=('Helvetica', 7))
lbl_Matermixdoor.grid(row=0, column=0,padx=3, pady=2)

btnMatermixC = ctk.CTkButton(frm_MixerC, text="Open", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMatermixC.grid(row=1, column=0, padx=1, pady=(0,1))

frame_with_border5pC = ctk.CTkFrame(frm_MixerC, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border5pC.grid(row=2, column=0,padx=(0,1), pady=(0,1))

lbl_MaterMixRotorC = ctk.CTkLabel(frame_with_border5pC, text="Motor Mixer\nLine C", font=('Helvetica', 7))
lbl_MaterMixRotorC.grid(row=3, column=0,padx=1, pady=2)

btnMatermixRotorC = ctk.CTkButton(frm_MixerC, text="Rev", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMatermixRotorC.grid(row=4, column=0, padx=(0,1), pady=(1,1))

frame_with_border6pC = ctk.CTkFrame(frm_MixerC, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border6pC.grid(row=0, column=1, columnspan=2, padx=(0,1), pady=(1,1))
lbl_MixingC = ctk.CTkLabel(frame_with_border6pC, text="Mixing Line C", font=('Helvetica', 7), width=60, height=15)
lbl_MixingC.grid(row=0, column=0,padx=3, pady=2)

frame_with_NumC = ctk.CTkFrame(frm_MixerC, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_NumC.grid(row=1, column=1,padx=(0,1), pady=(1,1))
lbl_NumC = ctk.CTkLabel(frame_with_NumC, text="00.00", font=('Helvetica', 12), width=60, height=15)
lbl_NumC.grid(row=0, column=0,padx=3, pady=2)

frame_with_SecC = ctk.CTkFrame(frm_MixerC, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_SecC.grid(row=1, column=2,padx=(0,0), pady=(1,1), sticky="w")
lbl_SecC = ctk.CTkLabel(frame_with_SecC, text="Sec", font=('Helvetica', 7), width=20, height=15)
lbl_SecC.grid(row=0, column=0,padx=3, pady=2)

btnFillC = ctk.CTkButton(frm_MixerC, text="Fill", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=80, height=80, state="normal", command=cmdBtnFillC)
btnFillC.grid(row=2, rowspan = 3, column=1, padx=1, pady=(0,1))

btnDumpC = ctk.CTkButton(frm_MixerC, text="Dump", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=80, height=80, state="normal", command=cmdBtnDumpC)
btnDumpC.grid(row=2, rowspan = 3, column=2, padx=1, pady=(0,1))


frm_MixerB = ctk.CTkFrame(label_with_image, fg_color="white")
frm_MixerB.grid(row=0, column=0, padx=(780,0), pady=(0,3))

frame_with_border3p = ctk.CTkFrame(frm_MixerB, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border3p.grid(row=0, column=0,padx=1, pady=(0,1))

lbl_Matermixdoor = ctk.CTkLabel(frame_with_border3p, text="Pintu Mixer Line B", font=('Helvetica', 7))
lbl_Matermixdoor.grid(row=0, column=0,padx=3, pady=2)

btnMatermix = ctk.CTkButton(frm_MixerB, text="Open", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMatermix.grid(row=1, column=0, padx=1, pady=(0,1))

frame_with_border5p = ctk.CTkFrame(frm_MixerB, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border5p.grid(row=2, column=0,padx=(0,1), pady=(0,1))

lbl_MaterMixRotor = ctk.CTkLabel(frame_with_border5p, text="Motor Mixer\nLine B", font=('Helvetica', 7))
lbl_MaterMixRotor.grid(row=3, column=0,padx=1, pady=2)

btnMatermixRotor = ctk.CTkButton(frm_MixerB, text="Rev", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMatermixRotor.grid(row=4, column=0, padx=(0,1), pady=(1,1))

frame_with_border6p = ctk.CTkFrame(frm_MixerB, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border6p.grid(row=0, column=1, columnspan=2, padx=(0,1), pady=(1,1))
lbl_Mixing = ctk.CTkLabel(frame_with_border6p, text="Mixing Line B", font=('Helvetica', 7), width=60, height=15)
lbl_Mixing.grid(row=0, column=0,padx=3, pady=2)

frame_with_Num = ctk.CTkFrame(frm_MixerB, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_Num.grid(row=1, column=1,padx=(0,1), pady=(1,1))
lbl_Num = ctk.CTkLabel(frame_with_Num, text="00.00", font=('Helvetica', 12), width=60, height=15)
lbl_Num.grid(row=0, column=0,padx=3, pady=2)

frame_with_Sec = ctk.CTkFrame(frm_MixerB, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_Sec.grid(row=1, column=2,padx=(0,0), pady=(1,1), sticky="w")
lbl_Sec = ctk.CTkLabel(frame_with_Sec, text="Sec", font=('Helvetica', 7), width=20, height=15)
lbl_Sec.grid(row=0, column=0,padx=3, pady=2)

btnFillB = ctk.CTkButton(frm_MixerB, text="Fill", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=80, height=80, state="normal", command=cmdBtnFillB)
btnFillB.grid(row=2, rowspan = 3, column=1, padx=1, pady=(0,1))

btnDumpB = ctk.CTkButton(frm_MixerB, text="Dump", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=80, height=80, state="normal", command=cmdBtnDumpB)
btnDumpB.grid(row=2, rowspan = 3, column=2, padx=1, pady=(0,1))


frm_MixerA = ctk.CTkFrame(label_with_image, fg_color="white")
frm_MixerA.grid(row=0, column=0, padx=(750,0), pady=(380,0))

frame_with_border3pA = ctk.CTkFrame(frm_MixerA, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border3pA.grid(row=0, column=0,padx=1, pady=(0,1))

lbl_MatermixdoorA = ctk.CTkLabel(frame_with_border3pA, text="Pintu Mixer Line A", font=('Helvetica', 7))
lbl_MatermixdoorA.grid(row=0, column=0,padx=3, pady=2)

btnMatermixA = ctk.CTkButton(frm_MixerA, text="Open", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMatermixA.grid(row=1, column=0, padx=1, pady=(0,1))

frame_with_border5pA = ctk.CTkFrame(frm_MixerA, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border5pA.grid(row=2, column=0,padx=(0,1), pady=(0,1))

lbl_MaterMixRotorA = ctk.CTkLabel(frame_with_border5pA, text="Motor Mixer\nLine A", font=('Helvetica', 7))
lbl_MaterMixRotorA.grid(row=3, column=0,padx=1, pady=2)

btnMatermixRotorA = ctk.CTkButton(frm_MixerA, text="Rev", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMatermixRotorA.grid(row=4, column=0, padx=(0,1), pady=(1,1))

frame_with_border6pA = ctk.CTkFrame(frm_MixerA, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border6pA.grid(row=0, column=1, columnspan=2, padx=(0,1), pady=(1,1))
lbl_MixingA = ctk.CTkLabel(frame_with_border6pA, text="Mixing Line A", font=('Helvetica', 7), width=60, height=15)
lbl_MixingA.grid(row=0, column=0,padx=3, pady=2)

frame_with_NumA = ctk.CTkFrame(frm_MixerA, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_NumA.grid(row=1, column=1,padx=(0,1), pady=(1,1))
lbl_NumA = ctk.CTkLabel(frame_with_NumA, text="00.00", font=('Helvetica', 12), width=60, height=15)
lbl_NumA.grid(row=0, column=0,padx=3, pady=2)

frame_with_SecA = ctk.CTkFrame(frm_MixerA, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_SecA.grid(row=1, column=2,padx=(0,0), pady=(1,1), sticky="w")
lbl_SecA = ctk.CTkLabel(frame_with_SecA, text="Sec", font=('Helvetica', 7), width=20, height=15)
lbl_SecA.grid(row=0, column=0,padx=3, pady=2)

btnFillA = ctk.CTkButton(frm_MixerA, text="Fill", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=80, height=80, state="normal")
btnFillA.grid(row=2, rowspan = 3, column=1, padx=1, pady=(0,1))

btnDumpA = ctk.CTkButton(frm_MixerA, text="Dump", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=80, height=80, state="normal")
btnDumpA.grid(row=2, rowspan = 3, column=2, padx=1, pady=(0,1))




# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabCommonZAuto2, fg_color="transparent")
frm_MenuBawah.grid(row=8, column=0, padx=(0,1), pady=(80,0), sticky="ew")

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="blue", text_color="white",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2, state="normal")
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU






# ================================================================================
# LINE Z - UI UX - AUTO - .zauto2
# ================================================================================
frame_tabCommonZAuto = ctk.CTkFrame(app, fg_color="white")
frame_tabCommonZAuto.pack(fill="both", expand=True)

frm_CommonAuto2LineAtas = ctk.CTkFrame(frame_tabCommonZAuto, fg_color="white")
frm_CommonAuto2LineAtas.grid(row=0, column=0, padx=10, pady=1, sticky="w")

# ------------

frmZAuto2 = ctk.CTkFrame(frm_CommonAuto2LineAtas, fg_color="white")
frmZAuto2.grid(row=0, column=0, padx=(1,1), pady=1, sticky="w")

frmZAutoPneumFeedThreeDoor = ctk.CTkFrame(frmZAuto2, fg_color="white")
frmZAutoPneumFeedThreeDoor.grid(row=0, column=2, padx=1, pady=1, sticky="w")

imageZAutoPneumFeedThreeDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PneumFeedThreeDoor.png'))
imageZAutoPneumFeedThreeDoor = ctk.CTkImage(light_image=imageZAutoPneumFeedThreeDoor, size=(400, 20)) 
ZAutoPneumFeedThreeDoorLbl = ctk.CTkLabel(frmZAutoPneumFeedThreeDoor, image=imageZAutoPneumFeedThreeDoor, text="")
ZAutoPneumFeedThreeDoorLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1, sticky="w")
btnZAutoPneumFeedThreeDoorIsLineA = ctk.CTkButton(frmZAutoPneumFeedThreeDoor, text="Line A", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoPneumFeedThreeDoorIsLineA.grid(row=1, column=0, padx=1, pady=1)
btnZAutoPneumFeedThreeDoorIsLineB = ctk.CTkButton(frmZAutoPneumFeedThreeDoor, text="Line B", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoPneumFeedThreeDoorIsLineB.grid(row=1, column=1, padx=1, pady=1)
btnZAutoPneumFeedThreeDoorIsLineC = ctk.CTkButton(frmZAutoPneumFeedThreeDoor, text="Line C", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoPneumFeedThreeDoorIsLineC.grid(row=1, column=2, padx=1, pady=1)
btnZAutoPneumFeedThreeDoorIsFault0 = ctk.CTkButton(frmZAutoPneumFeedThreeDoor, text="Fault 1", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoPneumFeedThreeDoorIsFault0.grid(row=1, column=3, padx=1, pady=1)
btnZAutoPneumFeedThreeDoorIsFault1 = ctk.CTkButton(frmZAutoPneumFeedThreeDoor, text="Fault 2", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoPneumFeedThreeDoorIsFault1.grid(row=1, column=4, padx=1, pady=1)

frm_CommonAuto2LineAtas2 = ctk.CTkFrame(frame_tabCommonZAuto, fg_color="white")
frm_CommonAuto2LineAtas2.grid(row=1, column=0, padx=10, pady=1, sticky="w")

frmAAutoMotorMaterMixDoor = ctk.CTkFrame(frm_CommonAuto2LineAtas2, fg_color="white")
frmAAutoMotorMaterMixDoor.grid(row=0, column=0, padx=1, pady=1)

imageAAutoMotorMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMaterMixRotorA.png'))
imageAAutoMotorMaterMixDoor = ctk.CTkImage(light_image=imageAAutoMotorMaterMixDoor, size=(240, 20))
AAutoMotorMaterMixDoorLbl = ctk.CTkLabel(frmAAutoMotorMaterMixDoor, image=imageAAutoMotorMaterMixDoor, text="")
AAutoMotorMaterMixDoorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnAAutoMotorMaterMixDoorDoRev = ctk.CTkButton(frmAAutoMotorMaterMixDoor, text="Rev", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnAAutoMotorMaterMixDoorDoRev.grid(row=1, column=0, padx=1, pady=1)
btnAAutoMotorMaterMixDoorDoFwd = ctk.CTkButton(frmAAutoMotorMaterMixDoor, text="Fwd", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnAAutoMotorMaterMixDoorDoFwd.grid(row=1, column=1, padx=1, pady=1)
btnAAutoMotorMaterMixDoorIsFault = ctk.CTkButton(frmAAutoMotorMaterMixDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnAAutoMotorMaterMixDoorIsFault.grid(row=1, column=2, padx=1, pady=1)


frmAAutoPneumMaterMixDoor = ctk.CTkFrame(frm_CommonAuto2LineAtas2, fg_color="white")
frmAAutoPneumMaterMixDoor.grid(row=0, column=1, padx=1, pady=1)

imageAAutoPneumMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PintuMixerA.png'))
imageAAutoPneumMaterMixDoor = ctk.CTkImage(light_image=imageAAutoPneumMaterMixDoor, size=(240, 20)) 
AAutoPneumMaterMixDoorLbl = ctk.CTkLabel(frmAAutoPneumMaterMixDoor, image=imageAAutoPneumMaterMixDoor, text="")
AAutoPneumMaterMixDoorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnAAutoPneumMaterMixDoorIsOpen = ctk.CTkButton(frmAAutoPneumMaterMixDoor, text="Open", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnAAutoPneumMaterMixDoorIsOpen.grid(row=1, column=0, padx=1, pady=1)
btnAAutoPneumMaterMixDoorIsClose = ctk.CTkButton(frmAAutoPneumMaterMixDoor, text="Close", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnAAutoPneumMaterMixDoorIsClose.grid(row=1, column=1, padx=1, pady=1)
btnAAutoPneumMaterMixDoorIsFault = ctk.CTkButton(frmAAutoPneumMaterMixDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnAAutoPneumMaterMixDoorIsFault.grid(row=1, column=2, padx=1, pady=1)


frmAAutoMixing = ctk.CTkFrame(frm_CommonAuto2LineAtas2, fg_color="white")
frmAAutoMixing.grid(row=0, column=3, padx=(50,1), pady=1)

imageAAutoMixing = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MixingA.png'))
imageAAutoMixing = ctk.CTkImage(light_image=imageAAutoMixing, size=(120, 20)) 
AAutoMixingLbl = ctk.CTkLabel(frmAAutoMixing, image=imageAAutoMixing, text="")
AAutoMixingLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
frmMixingNumA = ctk.CTkFrame(frmAAutoMixing, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frmMixingNumA.grid(row=1, column=0, padx=0, pady=1)
lbl_NumMixingB = ctk.CTkLabel(frmMixingNumA, text="00.00", font=('Helvetica', 25), width=lampWidth, height=lampHeight)
lbl_NumMixingB.grid(row=0, column=0,padx=2, pady=2)
frmMixingSecA = ctk.CTkFrame(frmAAutoMixing, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frmMixingSecA.grid(row=1, column=1, padx=0, pady=1)
lbl_secMixingA = ctk.CTkLabel(frmMixingSecA, text="SEC", font=('Helvetica', 12), width=lampWidth/2, height=lampHeight)
lbl_secMixingA.grid(row=0, column=0,padx=2, pady=2)


frm_CommonAuto2LineAtas3 = ctk.CTkFrame(frame_tabCommonZAuto, fg_color="white")
frm_CommonAuto2LineAtas3.grid(row=2, column=0, padx=10, pady=1, sticky="w")

frmBAutoMotorMaterMixDoor = ctk.CTkFrame(frm_CommonAuto2LineAtas3, fg_color="white")
frmBAutoMotorMaterMixDoor.grid(row=0, column=0, padx=1, pady=1)

imageBAutoMotorMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMaterMixRotorB.png'))
imageBAutoMotorMaterMixDoor = ctk.CTkImage(light_image=imageBAutoMotorMaterMixDoor, size=(240, 20))
BAutoMotorMaterMixDoorLbl = ctk.CTkLabel(frmBAutoMotorMaterMixDoor, image=imageBAutoMotorMaterMixDoor, text="")
BAutoMotorMaterMixDoorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnBAutoMotorMaterMixDoorDoRev = ctk.CTkButton(frmBAutoMotorMaterMixDoor, text="Rev", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMaterMixDoorDoRev.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorMaterMixDoorDoFwd = ctk.CTkButton(frmBAutoMotorMaterMixDoor, text="Fwd", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMaterMixDoorDoFwd.grid(row=1, column=1, padx=1, pady=1)
btnBAutoMotorMaterMixDoorIsFault = ctk.CTkButton(frmBAutoMotorMaterMixDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMaterMixDoorIsFault.grid(row=1, column=2, padx=1, pady=1)


frmBAutoPneumMaterMixDoor = ctk.CTkFrame(frm_CommonAuto2LineAtas3, fg_color="white")
frmBAutoPneumMaterMixDoor.grid(row=0, column=1, padx=1, pady=1)

imageBAutoPneumMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PintuMixerB.png'))
imageBAutoPneumMaterMixDoor = ctk.CTkImage(light_image=imageBAutoPneumMaterMixDoor, size=(240, 20)) 
BAutoPneumMaterMixDoorLbl = ctk.CTkLabel(frmBAutoPneumMaterMixDoor, image=imageBAutoPneumMaterMixDoor, text="")
BAutoPneumMaterMixDoorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnBAutoPneumMaterMixDoorIsOpen = ctk.CTkButton(frmBAutoPneumMaterMixDoor, text="Open", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumMaterMixDoorIsOpen.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumMaterMixDoorIsClose = ctk.CTkButton(frmBAutoPneumMaterMixDoor, text="Close", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumMaterMixDoorIsClose.grid(row=1, column=1, padx=1, pady=1)
btnBAutoPneumMaterMixDoorIsFault = ctk.CTkButton(frmBAutoPneumMaterMixDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumMaterMixDoorIsFault.grid(row=1, column=2, padx=1, pady=1)


frmBAutoMixing = ctk.CTkFrame(frm_CommonAuto2LineAtas3, fg_color="white")
frmBAutoMixing.grid(row=0, column=3, padx=(50,1), pady=1)

imageBAutoMixing = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MixingB.png'))
imageBAutoMixing = ctk.CTkImage(light_image=imageBAutoMixing, size=(120, 20)) 
BAutoMixingLbl = ctk.CTkLabel(frmBAutoMixing, image=imageBAutoMixing, text="")
BAutoMixingLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
frmMixingNumB = ctk.CTkFrame(frmBAutoMixing, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frmMixingNumB.grid(row=1, column=0, padx=0, pady=1)
lbl_NumMixingB = ctk.CTkLabel(frmMixingNumB, text="00.00", font=('Helvetica', 25), width=lampWidth, height=lampHeight)
lbl_NumMixingB.grid(row=0, column=0,padx=2, pady=2)
frmMixingSecB = ctk.CTkFrame(frmBAutoMixing, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frmMixingSecB.grid(row=1, column=1, padx=0, pady=1)
lbl_secMixingB = ctk.CTkLabel(frmMixingSecB, text="SEC", font=('Helvetica', 12), width=lampWidth/2, height=lampHeight)
lbl_secMixingB.grid(row=0, column=0,padx=2, pady=2)

frm_CommonAuto2LineTengah = ctk.CTkFrame(frame_tabCommonZAuto, fg_color="white")
frm_CommonAuto2LineTengah.grid(row=3, column=0, padx=10, pady=1, sticky="w")
# ------------
frmCAutoMotorMaterMixDoor = ctk.CTkFrame(frm_CommonAuto2LineTengah, fg_color="white")
frmCAutoMotorMaterMixDoor.grid(row=0, column=0, padx=1, pady=1)

imageCAutoMotorMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMaterMixRotorC.png'))
imageCAutoMotorMaterMixDoor = ctk.CTkImage(light_image=imageCAutoMotorMaterMixDoor, size=(240, 20))
CAutoMotorMaterMixDoorLbl = ctk.CTkLabel(frmCAutoMotorMaterMixDoor, image=imageCAutoMotorMaterMixDoor, text="")
CAutoMotorMaterMixDoorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnCAutoMotorMaterMixDoorDoRev = ctk.CTkButton(frmCAutoMotorMaterMixDoor, text="Rev", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMaterMixDoorDoRev.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorMaterMixDoorDoFwd = ctk.CTkButton(frmCAutoMotorMaterMixDoor, text="Fwd", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMaterMixDoorDoFwd.grid(row=1, column=1, padx=1, pady=1)
btnCAutoMotorMaterMixDoorIsFault = ctk.CTkButton(frmCAutoMotorMaterMixDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMaterMixDoorIsFault.grid(row=1, column=2, padx=1, pady=1)


frmBAutoPneumMaterMixDoor = ctk.CTkFrame(frm_CommonAuto2LineTengah, fg_color="white")
frmBAutoPneumMaterMixDoor.grid(row=0, column=1, padx=1, pady=1)

imageCAutoPneumMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PintuMixerC.png'))
imageCAutoPneumMaterMixDoor = ctk.CTkImage(light_image=imageCAutoPneumMaterMixDoor, size=(240, 20)) 
CAutoPneumMaterMixDoorLbl = ctk.CTkLabel(frmBAutoPneumMaterMixDoor, image=imageCAutoPneumMaterMixDoor, text="")
CAutoPneumMaterMixDoorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnCAutoPneumMaterMixDoorIsOpen = ctk.CTkButton(frmBAutoPneumMaterMixDoor, text="Open", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumMaterMixDoorIsOpen.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumMaterMixDoorIsClose = ctk.CTkButton(frmBAutoPneumMaterMixDoor, text="Close", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumMaterMixDoorIsClose.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumMaterMixDoorIsFault = ctk.CTkButton(frmBAutoPneumMaterMixDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumMaterMixDoorIsFault.grid(row=1, column=2, padx=1, pady=1)

frmCAutoMixing = ctk.CTkFrame(frm_CommonAuto2LineTengah, fg_color="white")
frmCAutoMixing.grid(row=0, column=3, padx=(50,1), pady=1)

imageCAutoMixing = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MixingC.png'))
imageCAutoMixing = ctk.CTkImage(light_image=imageCAutoMixing, size=(120, 20)) 
CAutoMixingLbl = ctk.CTkLabel(frmCAutoMixing, image=imageCAutoMixing, text="")
CAutoMixingLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
frmMixingNumC = ctk.CTkFrame(frmCAutoMixing, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frmMixingNumC.grid(row=1, column=0, padx=0, pady=1)
lbl_NumMixingC = ctk.CTkLabel(frmMixingNumC, text="00.00", font=('Helvetica', 25), width=lampWidth, height=lampHeight)
lbl_NumMixingC.grid(row=0, column=0,padx=2, pady=2)
frmMixingSecC = ctk.CTkFrame(frmCAutoMixing, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frmMixingSecC.grid(row=1, column=1, padx=0, pady=1)
lbl_secMixingC = ctk.CTkLabel(frmMixingSecC, text="SEC", font=('Helvetica', 12), width=lampWidth/2, height=lampHeight)
lbl_secMixingC.grid(row=0, column=0,padx=2, pady=2)

frmZAuto1 = ctk.CTkFrame(frame_tabCommonZAuto, fg_color="white")
frmZAuto1.grid(row=5, column=0, padx=(10,1), pady=1, sticky="w")

frmZAutoMotorMaterialCnvyr = ctk.CTkFrame(frmZAuto1, fg_color="white")
frmZAutoMotorMaterialCnvyr.grid(row=0, column=0, padx=1, pady=1)

imageZAutoMotorMaterialCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMaterialCnvyr.png'))
imageZAutoMotorMaterialCnvyr = ctk.CTkImage(light_image=imageZAutoMotorMaterialCnvyr, size=(160, 20)) 
ZAutoMotorMaterialCnvyrLbl = ctk.CTkLabel(frmZAutoMotorMaterialCnvyr, image=imageZAutoMotorMaterialCnvyr, text="")
ZAutoMotorMaterialCnvyrLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnZAutoMotorMaterialCnvyrDoStart = ctk.CTkButton(frmZAutoMotorMaterialCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoMotorMaterialCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnZAutoMotorMaterialCnvyrIsFault = ctk.CTkButton(frmZAutoMotorMaterialCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoMotorMaterialCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

frmZAutoMotorBagSlitrCnvyr = ctk.CTkFrame(frmZAuto1, fg_color="white")
frmZAutoMotorBagSlitrCnvyr.grid(row=0, column=1, padx=1, pady=1)

imageZAutoMotorBagSlitrCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorBagSlitrCnvyr.png'))
imageZAutoMotorBagSlitrCnvyr = ctk.CTkImage(light_image=imageZAutoMotorBagSlitrCnvyr, size=(160, 20)) 
ZAutoMotorBagSlitrCnvyrLbl = ctk.CTkLabel(frmZAutoMotorBagSlitrCnvyr, image=imageZAutoMotorBagSlitrCnvyr, text="")
ZAutoMotorBagSlitrCnvyrLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnZAutoMotorBagSlitrCnvyrDoStart = ctk.CTkButton(frmZAutoMotorBagSlitrCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoMotorBagSlitrCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnZAutoMotorBagSlitrCnvyrIsFault = ctk.CTkButton(frmZAutoMotorBagSlitrCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoMotorBagSlitrCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

frmZAutoMotorBagSlitrCuter = ctk.CTkFrame(frmZAuto1, fg_color="white")
frmZAutoMotorBagSlitrCuter.grid(row=0, column=2, padx=1, pady=1)

imageZAutoMotorBagSlitrCuter = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorBagSlitrCuter.png'))
imageZAutoMotorBagSlitrCuter = ctk.CTkImage(light_image=imageZAutoMotorBagSlitrCuter, size=(160, 20)) 
ZAutoMotorBagSlitrCuterLbl = ctk.CTkLabel(frmZAutoMotorBagSlitrCuter, image=imageZAutoMotorBagSlitrCuter, text="")
ZAutoMotorBagSlitrCuterLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnZAutoMotorBagSlitrCuterDoStart = ctk.CTkButton(frmZAutoMotorBagSlitrCuter, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoMotorBagSlitrCuterDoStart.grid(row=1, column=0, padx=1, pady=1)
btnZAutoMotorBagSlitrCuterIsFault = ctk.CTkButton(frmZAutoMotorBagSlitrCuter, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnZAutoMotorBagSlitrCuterIsFault.grid(row=1, column=1, padx=1, pady=1)



# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabCommonZAuto, fg_color="transparent")
frm_MenuBawah.grid(row=8, column=0, padx=(0,1), pady=(262,0), sticky="ew")

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="blue", text_color="white",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto, state="normal")
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU













# ================================================================================
# LINE COMMON - UI UX - MANUAL 1 - .zman1
# ================================================================================

frame_tabManualCommon = ctk.CTkFrame(app, fg_color="white")
frame_tabManualCommon.pack(fill="both", expand=True)

# START FeederDoor
frm_FeederDoor = ctk.CTkFrame(frame_tabManualCommon, fg_color="white")
frm_FeederDoor.grid(row=0, column=0, padx=1, pady=1)

lbl_MatCol = ctk.CTkLabel(frm_FeederDoor, text="Feeder Door", font=('Helvetica', 16))
lbl_MatCol.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarna = ctk.CTkFrame(frm_FeederDoor)
frm_BtnWarna.grid(row=1, column=0, columnspan=5, pady=1)

btnZManLineA = ctk.CTkButton(frm_BtnWarna, text="LineA (Kecil)", text_color="black", fg_color="light green", border_color="black", border_width=5,
                                 command=cmdBtnZLineA, height=btnSize)
btnZManLineA.grid(row=1, column=0, padx=5, pady=(10, 10))

btnZManLineB = ctk.CTkButton(frm_BtnWarna, text="LineB (Besar)", text_color="black", fg_color="pink", border_color="black", border_width=5,
                                  command=cmdBtnZLineB, height=btnSize)
btnZManLineB.grid(row=1, column=1, padx=5, pady=(10, 10))

btnZManLineC = ctk.CTkButton(frm_BtnWarna, text="LineC (Bola)", text_color="black", fg_color="pink", border_color="black", border_width=5,
                                  command=cmdBtnZLineC, height=btnSize)
btnZManLineC.grid(row=1, column=2, padx=5, pady=(10, 10))

btnZManManual = ctk.CTkButton(frm_FeederDoor, text="Auto", fg_color="red", text_color="black", border_color="black", border_width=5,
                                 command=showCommonAuto2, height=btnSize)
btnZManManual.grid(row=1, column=5, padx=20, pady=(10, 10))
# END FeederDoor

frm_CommonManLineAtas = ctk.CTkFrame(frame_tabManualCommon, fg_color="white")
frm_CommonManLineAtas.grid(row=1, column=0, padx=10, pady=1, sticky="w")


frmZManFeedThreeDoor = ctk.CTkFrame(frm_CommonManLineAtas, fg_color="white")
frmZManFeedThreeDoor.grid(row=0, column=0, padx=(20,0), pady=(0, 5))

frmZManFeedThreeDoor0Lbl = ctk.CTkFrame(frmZManFeedThreeDoor, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                  border_width=5)
frmZManFeedThreeDoor0Lbl.grid(row=0, column=0, padx=(5,1), pady=10,  sticky="n")

lblSwitchZManFeedThreeDoor0 = ctk.CTkLabel(frmZManFeedThreeDoor0Lbl, text="Pneum\nFeedThreeDoor 0", width=150)
lblSwitchZManFeedThreeDoor0.grid(row=1, column=0, padx=10, pady=5)

frmZManFeedThreeDoor1Lbl = ctk.CTkFrame(frmZManFeedThreeDoor, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                  border_width=5)
frmZManFeedThreeDoor1Lbl.grid(row=0, column=1, padx=(1,5), pady=10, sticky="n")

lblSwitchZManFeedThreeDoor1 = ctk.CTkLabel(frmZManFeedThreeDoor1Lbl, text="Pneum\nFeedThreeDoor 1", width=150)
lblSwitchZManFeedThreeDoor1.grid(row=1, column=1, padx=10, pady=5)

frmBtnZManFeedThreeDoor = ctk.CTkFrame(frmZManFeedThreeDoor, fg_color="transparent")
frmBtnZManFeedThreeDoor.grid(row=2, column=0, padx=1, pady=1, columnspan=2)

btnRedZManFeedThreeDoor = ctk.CTkFrame(frmBtnZManFeedThreeDoor, width=btnRedGreenSize, height=btnRedGreenSize, corner_radius=100,
                                  fg_color='red', border_color="black", border_width=5)
btnRedZManFeedThreeDoor.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedZManFeedThreeDoor.bind("<Button-1>", lambda event: btnRedZManFeedThreeDoorClick())
btnRedZManFeedThreeDoor.bind("<ButtonRelease-1>", lambda event: btnRedZManFeedThreeDoorClickReset())

btnYellowZManFeedThreeDoor = ctk.CTkFrame(frmBtnZManFeedThreeDoor, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='Yellow', border_color="black", border_width=5)
btnYellowZManFeedThreeDoor.grid(row=0, column=1, padx=(5, 1), pady=1)
btnYellowZManFeedThreeDoor.bind("<Button-1>", lambda event: btnYellowZManFeedThreeDoorClick())
btnYellowZManFeedThreeDoor.bind("<ButtonRelease-1>", lambda event: btnYellowZManFeedThreeDoorClickReset())

btnGreenZManFeedThreeDoor = ctk.CTkFrame(frmBtnZManFeedThreeDoor, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenZManFeedThreeDoor.grid(row=0, column=2, padx=(5, 1), pady=1)
btnGreenZManFeedThreeDoor.bind("<Button-1>", lambda event: btnGreenZManFeedThreeDoorClick())
btnGreenZManFeedThreeDoor.bind("<ButtonRelease-1>", lambda event: btnGreenZManFeedThreeDoorClickReset())

frmSwitchZManFeedThreeDoorbawah = ctk.CTkFrame(frmBtnZManFeedThreeDoor, fg_color="transparent")
frmSwitchZManFeedThreeDoorbawah.grid(row=2, column=0, columnspan=3)
imageZManFeedThreeDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'PneumFeedThreeDoor.png'))
imageZManFeedThreeDoor = ctk.CTkImage(light_image=imageZManFeedThreeDoor, size=(240, 50))
ZManFeedThreeDoorLbl = ctk.CTkLabel(frmSwitchZManFeedThreeDoorbawah, image=imageZManFeedThreeDoor, text="")
ZManFeedThreeDoorLbl.pack(padx=1, pady=1)

# ------------
# stateAManMaterMixRotor = "up"

frmAManMaterMixRotor = ctk.CTkFrame(frm_CommonManLineAtas, fg_color="white")
frmAManMaterMixRotor.grid(row=0, column=1, padx=10, pady=(0, 5))

frmAManMaterMixRotorLbl = ctk.CTkFrame(frmAManMaterMixRotor, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                   border_width=5)
frmAManMaterMixRotorLbl.grid(row=1, column=0, padx=5, pady=(10,0))

lblSwitchAManMaterMixRotor = ctk.CTkLabel(frmAManMaterMixRotorLbl, text="Motor Mixer LineA", width=150)
lblSwitchAManMaterMixRotor.grid(row=0, column=0, padx=10, pady=5)

frmBtnAManMaterMixRotor = ctk.CTkFrame(frmAManMaterMixRotor, fg_color="transparent")
frmBtnAManMaterMixRotor.grid(row=2, column=0, padx=1, pady=1)

# imgAManMaterMixRotorUp = ImageTk.PhotoImage(switchUp)
# imgAManMaterMixRotorLeft = ImageTk.PhotoImage(switchLeft)
# imgAManMaterMixRotorRight = ImageTk.PhotoImage(switchRight)

# canvasAManMaterMixRotor = ctk.CTkCanvas(frmBtnAManMaterMixRotor, width=image_width, height=image_height, highlightthickness=0)
# canvasAManMaterMixRotor.pack()
# imgAManMaterMixRotor = canvasAManMaterMixRotor.create_image(0, 0, anchor='nw', image=imgAManMaterMixRotorUp)

# btnKiriAManMaterMixRotor = canvasAManMaterMixRotor.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananAManMaterMixRotor = canvasAManMaterMixRotor.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

imgAManMaterMixRotorLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgAManMaterMixRotorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))


btnKiriAManMaterMixRotor = ctk.CTkButton(frmBtnAManMaterMixRotor,  image=imgAManMaterMixRotorLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriAManMaterMixRotor.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))

btnkananAManMaterMixRotor = ctk.CTkButton(frmBtnAManMaterMixRotor, image=imgAManMaterMixRotorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnkananAManMaterMixRotor.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))

# canvasAManMaterMixRotor.tag_bind(btnKiriAManMaterMixRotor, "<ButtonPress-1>", lambda event: changeAManMaterMixRotorSwitch("left"))
# canvasAManMaterMixRotor.tag_bind(btnKiriAManMaterMixRotor, "<ButtonRelease-1>", resetAManMaterMixRotorSwicth)

# canvasAManMaterMixRotor.tag_bind(btnKananAManMaterMixRotor, "<ButtonPress-1>", lambda event: changeAManMaterMixRotorSwitch("right"))
# canvasAManMaterMixRotor.tag_bind(btnKananAManMaterMixRotor, "<ButtonRelease-1>", resetAManMaterMixRotorSwicth)

frmAManMaterMixRotorBawah = ctk.CTkFrame(frmBtnAManMaterMixRotor, fg_color="transparent", width=150)
frmAManMaterMixRotorBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchAManMaterMixRotorbawah = ctk.CTkFrame(frmAManMaterMixRotorBawah, fg_color="transparent")
frmSwitchAManMaterMixRotorbawah.grid(row=2, column=0, columnspan=2)
imageAManMaterMixRotorbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MaterMixRotorLineA.png'))
imageAManMaterMixRotorbawah = ctk.CTkImage(light_image=imageAManMaterMixRotorbawah, size=(180, 50))
AManMaterMixRotorbawahLbl = ctk.CTkLabel(frmSwitchAManMaterMixRotorbawah, image=imageAManMaterMixRotorbawah, text="")
AManMaterMixRotorbawahLbl.pack(padx=1, pady=1)

# ------------
frmAManMaterMixDoor = ctk.CTkFrame(frm_CommonManLineAtas, fg_color="white")
frmAManMaterMixDoor.grid(row=0, column=2, padx=(20,0), pady=(0, 5))

frmAManMaterMixDoorLbl = ctk.CTkFrame(frmAManMaterMixDoor, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                  border_width=5)
frmAManMaterMixDoorLbl.grid(row=0, column=0, padx=5, pady=10)

lblSwitchAManMaterMixDoor = ctk.CTkLabel(frmAManMaterMixDoorLbl, text="Pintu Mixer LineA", width=150)
lblSwitchAManMaterMixDoor.grid(row=1, column=0, padx=10, pady=5)

frmBtnAManMaterMixDoor = ctk.CTkFrame(frmAManMaterMixDoor, fg_color="transparent")
frmBtnAManMaterMixDoor.grid(row=2, column=0, padx=1, pady=1)

btnRedAManMaterMixDoor = ctk.CTkFrame(frmBtnAManMaterMixDoor, width=btnRedGreenSize, height=btnRedGreenSize, corner_radius=100,
                                  fg_color='red', border_color="black", border_width=5)
btnRedAManMaterMixDoor.grid(row=0, column=0, padx=(1, 5), pady=1)
# btnRedAManMaterMixDoor.bind("<Button-1>", lambda event: btnRedAManMaterMixDoorClick())
# btnRedAManMaterMixDoor.bind("<ButtonRelease-1>", lambda event: btnRedAManMaterMixDoorClickReset())

btnGreenAManMaterMixDoor = ctk.CTkFrame(frmBtnAManMaterMixDoor, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenAManMaterMixDoor.grid(row=0, column=1, padx=(5, 1), pady=1)
# btnGreenAManMaterMixDoor.bind("<Button-1>", lambda event: btnGreenAManMaterMixDoorClick())
# btnGreenAManMaterMixDoor.bind("<ButtonRelease-1>", lambda event: btnGreenAManMaterMixDoorClickReset())

frmSwitchAManMaterMixDoorbawah = ctk.CTkFrame(frmBtnAManMaterMixDoor, fg_color="transparent")
frmSwitchAManMaterMixDoorbawah.grid(row=2, column=0, columnspan=2)
imageAManMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'PintuMixerLineA.png'))
imageAManMaterMixDoor = ctk.CTkImage(light_image=imageAManMaterMixDoor, size=(190, 50))
AManMaterMixDoorLbl = ctk.CTkLabel(frmSwitchAManMaterMixDoorbawah, image=imageAManMaterMixDoor, text="")
AManMaterMixDoorLbl.pack(padx=1, pady=1)





frm_CommonManLineBawah = ctk.CTkFrame(frame_tabManualCommon, fg_color="white")
frm_CommonManLineBawah.grid(row=3, column=0, padx=10, pady=1, sticky="w")

# ------------
# stateBManMaterMixRotor = "up"

frmBManMaterMixRotor = ctk.CTkFrame(frm_CommonManLineBawah, fg_color="white")
frmBManMaterMixRotor.grid(row=0, column=0, padx=10, pady=(0, 5))

frmBManMaterMixRotorLbl = ctk.CTkFrame(frmBManMaterMixRotor, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManMaterMixRotorLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManMaterMixRotor = ctk.CTkLabel(frmBManMaterMixRotorLbl, text="Motor Mixer LineB", width=150)
lblSwitchBManMaterMixRotor.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManMaterMixRotor = ctk.CTkFrame(frmBManMaterMixRotor, fg_color="transparent")
frmBtnBManMaterMixRotor.grid(row=2, column=0, padx=1, pady=1)

# imgBManMaterMixRotorUp = ImageTk.PhotoImage(switchUp)
# imgBManMaterMixRotorLeft = ImageTk.PhotoImage(switchLeft)
# imgBManMaterMixRotorRight = ImageTk.PhotoImage(switchRight)

# canvasBManMaterMixRotor = ctk.CTkCanvas(frmBtnBManMaterMixRotor, width=image_width, height=image_height, highlightthickness=0)
# canvasBManMaterMixRotor.pack()
# imgBManMaterMixRotor = canvasBManMaterMixRotor.create_image(0, 0, anchor='nw', image=imgBManMaterMixRotorUp)

# btnKiriBManMaterMixRotor = canvasBManMaterMixRotor.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManMaterMixRotor = canvasBManMaterMixRotor.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasBManMaterMixRotor.tag_bind(btnKiriBManMaterMixRotor, "<ButtonPress-1>", lambda event: changeBManMaterMixRotorSwitch("left"))
# canvasBManMaterMixRotor.tag_bind(btnKiriBManMaterMixRotor, "<ButtonRelease-1>", resetBManMaterMixRotorSwicth)

# canvasBManMaterMixRotor.tag_bind(btnKananBManMaterMixRotor, "<ButtonPress-1>", lambda event: changeBManMaterMixRotorSwitch("right"))
# canvasBManMaterMixRotor.tag_bind(btnKananBManMaterMixRotor, "<ButtonRelease-1>", resetBManMaterMixRotorSwicth)

imgBManMaterMixRotorLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMaterMixRotorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMaterMixRotorLeft = ctk.CTkImage(btnLeft, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMaterMixRotorRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriBManMaterMixRotor = ctk.CTkButton(frmBtnBManMaterMixRotor,  image=imgBManMaterMixRotorLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriBManMaterMixRotor.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))
btnKiriBManMaterMixRotor.bind("<Button-1>", lambda event: btnKiriBManMaterMixRotorClick())
btnKiriBManMaterMixRotor.bind("<ButtonRelease-1>", lambda event: btnKiriBManMaterMixRotorClickReset())

btnKananBManMaterMixRotor = ctk.CTkButton(frmBtnBManMaterMixRotor, image=imgBManMaterMixRotorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManMaterMixRotor.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManMaterMixRotor.bind("<Button-1>", lambda event: btnKananBManMaterMixRotorClick())
btnKananBManMaterMixRotor.bind("<ButtonRelease-1>", lambda event: btnKananBManMaterMixRotorClickReset())

frmBManMaterMixRotorBawah = ctk.CTkFrame(frmBtnBManMaterMixRotor, fg_color="transparent", width=150)
frmBManMaterMixRotorBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchBManMaterMixRotorbawah = ctk.CTkFrame(frmBManMaterMixRotorBawah, fg_color="transparent")
frmSwitchBManMaterMixRotorbawah.grid(row=2, column=0, columnspan=2)
imageBManMaterMixRotorbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MaterMixRotorLineB.png'))
imageBManMaterMixRotorbawah = ctk.CTkImage(light_image=imageBManMaterMixRotorbawah, size=(180, 50))
BManMaterMixRotorbawahLbl = ctk.CTkLabel(frmSwitchBManMaterMixRotorbawah, image=imageBManMaterMixRotorbawah, text="")
BManMaterMixRotorbawahLbl.pack(padx=1, pady=1)
# ------------
frmBManMaterMixDoor = ctk.CTkFrame(frm_CommonManLineBawah, fg_color="white")
frmBManMaterMixDoor.grid(row=0, column=1, padx=(20,0), pady=(0, 5))

frmBManMaterMixDoorLbl = ctk.CTkFrame(frmBManMaterMixDoor, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmBManMaterMixDoorLbl.grid(row=0, column=0, padx=5, pady=10)

lblSwitchBManMaterMixDoor = ctk.CTkLabel(frmBManMaterMixDoorLbl, text="Pintu Mixer LineB", width=150)
lblSwitchBManMaterMixDoor.grid(row=1, column=0, padx=10, pady=5)

frmBtnBManMaterMixDoor = ctk.CTkFrame(frmBManMaterMixDoor, fg_color="transparent")
frmBtnBManMaterMixDoor.grid(row=2, column=0, padx=1, pady=1)

btnRedBManMaterMixDoor = ctk.CTkFrame(frmBtnBManMaterMixDoor, width=btnRedGreenSize, height=btnRedGreenSize, corner_radius=100,
                                  fg_color='red', border_color="black", border_width=5)
btnRedBManMaterMixDoor.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedBManMaterMixDoor.bind("<Button-1>", lambda event: btnRedBManMaterMixDoorClick())
btnRedBManMaterMixDoor.bind("<ButtonRelease-1>", lambda event: btnRedBManMaterMixDoorClickReset())

btnGreenBManMaterMixDoor = ctk.CTkFrame(frmBtnBManMaterMixDoor, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManMaterMixDoor.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenBManMaterMixDoor.bind("<Button-1>", lambda event: btnGreenBManMaterMixDoorClick())
btnGreenBManMaterMixDoor.bind("<ButtonRelease-1>", lambda event: btnGreenBManMaterMixDoorClickReset())

frmSwitchBManMaterMixDoorbawah = ctk.CTkFrame(frmBtnBManMaterMixDoor, fg_color="transparent")
frmSwitchBManMaterMixDoorbawah.grid(row=2, column=0, columnspan=2)
imageBManMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'PintuMixerLineB.png'))
imageBManMaterMixDoor = ctk.CTkImage(light_image=imageBManMaterMixDoor, size=(190, 50))
BManMaterMixDoorLbl = ctk.CTkLabel(frmSwitchBManMaterMixDoorbawah, image=imageBManMaterMixDoor, text="")
BManMaterMixDoorLbl.pack(padx=1, pady=1)

# ------------
stateCManMaterMixRotor = "up"

frmCManMaterMixRotor = ctk.CTkFrame(frm_CommonManLineBawah, fg_color="white")
frmCManMaterMixRotor.grid(row=0, column=2, padx=10, pady=(0, 5))

frmCManMaterMixRotorLbl = ctk.CTkFrame(frmCManMaterMixRotor, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManMaterMixRotorLbl.grid(row=1, column=0, padx=1, pady=10)

lblSwitchCManMaterMixRotor = ctk.CTkLabel(frmCManMaterMixRotorLbl, text="Motor Mixer LineC", width=150)
lblSwitchCManMaterMixRotor.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManMaterMixRotor = ctk.CTkFrame(frmCManMaterMixRotor, fg_color="transparent")
frmBtnCManMaterMixRotor.grid(row=2, column=0, padx=1, pady=1)

# imgCManMaterMixRotorUp = ImageTk.PhotoImage(switchUp)
# imgCManMaterMixRotorLeft = ImageTk.PhotoImage(switchLeft)
# imgCManMaterMixRotorRight = ImageTk.PhotoImage(switchRight)

# canvasCManMaterMixRotor = ctk.CTkCanvas(frmBtnCManMaterMixRotor, width=image_width, height=image_height, highlightthickness=0)
# canvasCManMaterMixRotor.pack()
# imgCManMaterMixRotor = canvasCManMaterMixRotor.create_image(0, 0, anchor='nw', image=imgCManMaterMixRotorUp)

# btnKiriCManMaterMixRotor = canvasCManMaterMixRotor.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManMaterMixRotor = canvasCManMaterMixRotor.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasCManMaterMixRotor.tag_bind(btnKiriCManMaterMixRotor, "<ButtonPress-1>", lambda event: changeCManMaterMixRotorSwitch("left"))
# canvasCManMaterMixRotor.tag_bind(btnKiriCManMaterMixRotor, "<ButtonRelease-1>", resetCManMaterMixRotorSwicth)

# canvasCManMaterMixRotor.tag_bind(btnKananCManMaterMixRotor, "<ButtonPress-1>", lambda event: changeCManMaterMixRotorSwitch("right"))
# canvasCManMaterMixRotor.tag_bind(btnKananCManMaterMixRotor, "<ButtonRelease-1>", resetCManMaterMixRotorSwicth)

imgCManMaterMixRotorLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMaterMixRotorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMaterMixRotorLeft = ctk.CTkImage(btnLeft, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMaterMixRotorRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriCManMaterMixRotor = ctk.CTkButton(frmBtnCManMaterMixRotor,  image=imgCManMaterMixRotorLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriCManMaterMixRotor.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))
btnKiriCManMaterMixRotor.bind("<Button-1>", lambda event: btnKiriCManMaterMixRotorClick())
btnKiriCManMaterMixRotor.bind("<ButtonRelease-1>", lambda event: btnKiriCManMaterMixRotorClickReset())

btnKananCManMaterMixRotor = ctk.CTkButton(frmBtnCManMaterMixRotor, image=imgCManMaterMixRotorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManMaterMixRotor.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManMaterMixRotor.bind("<Button-1>", lambda event: btnKananCManMaterMixRotorClick())
btnKananCManMaterMixRotor.bind("<ButtonRelease-1>", lambda event: btnKananCManMaterMixRotorClickReset())

frmCManMaterMixRotorBawah = ctk.CTkFrame(frmBtnCManMaterMixRotor, fg_color="transparent", width=150)
frmCManMaterMixRotorBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManMaterMixRotorbawah = ctk.CTkFrame(frmCManMaterMixRotorBawah, fg_color="transparent")
frmSwitchCManMaterMixRotorbawah.grid(row=2, column=0, columnspan=2)
imageCManMaterMixRotorbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MaterMixRotorLineC.png'))
imageCManMaterMixRotorbawah = ctk.CTkImage(light_image=imageCManMaterMixRotorbawah, size=(180, 50))
CManMaterMixRotorbawahLbl = ctk.CTkLabel(frmSwitchCManMaterMixRotorbawah, image=imageCManMaterMixRotorbawah, text="")
CManMaterMixRotorbawahLbl.pack(padx=1, pady=1)
# ------------
frmCManMaterMixDoor = ctk.CTkFrame(frm_CommonManLineBawah, fg_color="white")
frmCManMaterMixDoor.grid(row=0, column=3, padx=10, pady=(0, 5))

frmCManMaterMixDoorLbl = ctk.CTkFrame(frmCManMaterMixDoor, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmCManMaterMixDoorLbl.grid(row=0, column=0, padx=5, pady=10)

lblSwitchCManMaterMixDoor = ctk.CTkLabel(frmCManMaterMixDoorLbl, text="Pintu Mixer LineC", width=150)
lblSwitchCManMaterMixDoor.grid(row=1, column=0, padx=10, pady=5)

frmBtnCManMaterMixDoor = ctk.CTkFrame(frmCManMaterMixDoor, fg_color="transparent")
frmBtnCManMaterMixDoor.grid(row=2, column=0, padx=1, pady=1)

btnRedCManMaterMixDoor = ctk.CTkFrame(frmBtnCManMaterMixDoor, width=btnRedGreenSize, height=btnRedGreenSize, corner_radius=100,
                                  fg_color='pink', border_color="black", border_width=5)
btnRedCManMaterMixDoor.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedCManMaterMixDoor.bind("<Button-1>", lambda event: btnRedCManMaterMixDoorClick())
btnRedCManMaterMixDoor.bind("<ButtonRelease-1>", lambda event: btnRedCManMaterMixDoorClickReset())

btnGreenCManMaterMixDoor = ctk.CTkFrame(frmBtnCManMaterMixDoor, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='light green', border_color="black", border_width=5)
btnGreenCManMaterMixDoor.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenCManMaterMixDoor.bind("<Button-1>", lambda event: btnGreenCManMaterMixDoorClick())
btnGreenCManMaterMixDoor.bind("<ButtonRelease-1>", lambda event: btnGreenCManMaterMixDoorClickReset())

frmSwitchCManMaterMixDoorbawah = ctk.CTkFrame(frmBtnCManMaterMixDoor, fg_color="transparent")
frmSwitchCManMaterMixDoorbawah.grid(row=2, column=0, columnspan=2)
imageCManMaterMixDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'PintuMixerLineC.png'))
imageCManMaterMixDoor = ctk.CTkImage(light_image=imageCManMaterMixDoor, size=(190, 50))
CManMaterMixDoorLbl = ctk.CTkLabel(frmSwitchCManMaterMixDoorbawah, image=imageCManMaterMixDoor, text="")
CManMaterMixDoorLbl.pack(padx=1, pady=1)


# # ------------
# frm_CommonManLineBawah2 = ctk.CTkFrame(frame_tabManualCommon, fg_color="white")
# frm_CommonManLineBawah2.grid(row=4, column=0, padx=10, pady=1, sticky="w")

# btnRedCManMixerLineB = ctk.CTkFrame(frm_CommonManLineBawah2, width=btnRedGreenSize, height=btnRedGreenSize, corner_radius=100,
#                                   fg_color='red', border_color="black", border_width=5)
# btnRedCManMixerLineB.grid(row=0, column=0, padx=(1, 5), pady=1)
# btnRedCManMixerLineB.bind("<Button-1>", lambda event: pressRed())
# btnRedCManMixerLineB.bind("<ButtonRelease-1>", lambda event: resetBManMaterMixRotorSwicthTest())

# btnGreenCManMixerLineB = ctk.CTkFrame(frm_CommonManLineBawah2, width=btnRedGreenSize, height=btnRedGreenSize,
#                                     corner_radius=100, fg_color='lime', border_color="black", border_width=5)
# btnGreenCManMixerLineB.grid(row=0, column=1, padx=(5, 1), pady=1)
# btnGreenCManMixerLineB.bind("<Button-1>", lambda event: pressGreen())
# btnGreenCManMixerLineB.bind("<ButtonRelease-1>", lambda event: resetBManMaterMixRotorSwicthTest())


# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualCommon, fg_color="transparent")
frm_MenuBawah.grid(row=4, column=0, padx=1, pady=(138,1))

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="blue", text_color="white",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan, state="normal")
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU






# ================================================================================
# LINE COMMON - UI UX - MANUAL 2 - .zman2
# ================================================================================

frame_tabManualCommon2 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualCommon2.pack(fill="both", expand=True)

# START FeederDoor
# frm_FeederDoor = ctk.CTkFrame(frame_tabManualCommon2, fg_color="white")
# frm_FeederDoor.grid(row=0, column=0, padx=1, pady=1)

# lbl_MatCol = ctk.CTkLabel(frm_FeederDoor, text="Feeder Door", font=('Helvetica', 16))
# lbl_MatCol.grid(row=0, column=0, columnspan=6, pady=1)

# frm_BtnWarna = ctk.CTkFrame(frm_FeederDoor)
# frm_BtnWarna.grid(row=1, column=0, columnspan=5, pady=1)

# btnZManLineA = ctk.CTkButton(frm_BtnWarna, text="Line A (Kecil)", text_color="black", fg_color="light green", border_color="black", border_width=5,
#                                  command=cmdBtnZLineA, height=btnSize)
# btnZManLineA.grid(row=1, column=0, padx=5, pady=(10, 10))

# btnZManLineB = ctk.CTkButton(frm_BtnWarna, text="Line B (Besar)", text_color="black", fg_color="pink", border_color="black", border_width=5,
#                                   command=cmdBtnZLineB, height=btnSize)
# btnZManLineB.grid(row=1, column=1, padx=5, pady=(10, 10))

# btnZManLineC = ctk.CTkButton(frm_BtnWarna, text="Line C (Bola)", text_color="black", fg_color="pink", border_color="black", border_width=5,
#                                   command=cmdBtnZLineC, height=btnSize)
# btnZManLineC.grid(row=1, column=2, padx=5, pady=(10, 10))

# btnZManManual = ctk.CTkButton(frm_FeederDoor, text="Auto", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                  command=showCommonAuto, height=btnSize)
# btnZManManual.grid(row=1, column=5, padx=20, pady=(10, 10))
# # END FeederDoor

frm_CommonManLineAtas = ctk.CTkFrame(frame_tabManualCommon2, fg_color="white")
frm_CommonManLineAtas.grid(row=1, column=0, padx=10, pady=1, sticky="w")

# ------------
stateZManMotorMaterialConvyr = "up"

frmZManMotorMaterialConvyr = ctk.CTkFrame(frm_CommonManLineAtas, fg_color="white")
frmZManMotorMaterialConvyr.grid(row=0, column=0, padx=20, pady=(0, 5))

frmZManMotorMaterialConvyrLbl = ctk.CTkFrame(frmZManMotorMaterialConvyr, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                   border_width=5)
frmZManMotorMaterialConvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchZManMotorMaterialConvyr = ctk.CTkLabel(frmZManMotorMaterialConvyrLbl, text="Motor\nMotorMaterialConvyr", width=150)
lblSwitchZManMotorMaterialConvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnZManMotorMaterialConvyr = ctk.CTkFrame(frmZManMotorMaterialConvyr, fg_color="transparent")
frmBtnZManMotorMaterialConvyr.grid(row=2, column=0, padx=1, pady=1)

# imgZManMotorMaterialConvyrUp = ImageTk.PhotoImage(switchUp)
# imgZManMotorMaterialConvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgZManMotorMaterialConvyrRight = ImageTk.PhotoImage(switchRight)

# canvasZManMotorMaterialConvyr = ctk.CTkCanvas(frmBtnZManMotorMaterialConvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasZManMotorMaterialConvyr.pack()
# imgZManMotorMaterialConvyr = canvasZManMotorMaterialConvyr.create_image(0, 0, anchor='nw', image=imgZManMotorMaterialConvyrUp)

# btnKiriZManMotorMaterialConvyr = canvasZManMotorMaterialConvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananZManMotorMaterialConvyr = canvasZManMotorMaterialConvyr.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvasZManMotorMaterialConvyr.tag_bind(btnKananZManMotorMaterialConvyr, "<ButtonPress-1>", lambda event: changeZManMotorMaterialConvyrSwitch("right"))
# canvasZManMotorMaterialConvyr.tag_bind(btnKananZManMotorMaterialConvyr, "<ButtonRelease-1>", resetZManMotorMaterialConvyrSwicth)

imgZManMaterMixRotorLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgZManMaterMixRotorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriZManMaterMixRotor = ctk.CTkButton(frmBtnZManMotorMaterialConvyr,  image=imgZManMaterMixRotorLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriZManMaterMixRotor.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))

btnKananZManMaterMixRotor = ctk.CTkButton(frmBtnZManMotorMaterialConvyr, image=imgZManMaterMixRotorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananZManMaterMixRotor.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))


frmZManMotorMaterialConvyrBawah = ctk.CTkFrame(frmBtnZManMotorMaterialConvyr, fg_color="transparent", width=150)
frmZManMotorMaterialConvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchZManMotorMaterialConvyrbawah = ctk.CTkFrame(frmZManMotorMaterialConvyrBawah, fg_color="transparent")
frmSwitchZManMotorMaterialConvyrbawah.grid(row=2, column=0, columnspan=2)
imageZManMotorMaterialConvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MotorMaterialCnvyr.png'))
imageZManMotorMaterialConvyrbawah = ctk.CTkImage(light_image=imageZManMotorMaterialConvyrbawah, size=(180, 50))
ZManMotorMaterialConvyrbawahLbl = ctk.CTkLabel(frmSwitchZManMotorMaterialConvyrbawah, image=imageZManMotorMaterialConvyrbawah, text="")
ZManMotorMaterialConvyrbawahLbl.pack(padx=1, pady=1)
# ------------
statBagSlitrConvyr = "up"

frmZBagSlitrConvyr = ctk.CTkFrame(frm_CommonManLineAtas, fg_color="white")
frmZBagSlitrConvyr.grid(row=0, column=1, padx=20, pady=(0, 5))

frmZBagSlitrConvyrLbl = ctk.CTkFrame(frmZBagSlitrConvyr, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                   border_width=5)
frmZBagSlitrConvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSBagSlitrConvyr = ctk.CTkLabel(frmZBagSlitrConvyrLbl, text="Motor\nMotBagSlitrConvyr", width=150)
lblSBagSlitrConvyr.grid(row=0, column=0, padx=10, pady=5)

frmBBagSlitrConvyr = ctk.CTkFrame(frmZBagSlitrConvyr, fg_color="transparent")
frmBBagSlitrConvyr.grid(row=2, column=0, padx=1, pady=1)

# imgZBagSlitrConvyrUp = ImageTk.PhotoImage(switchUp)
# imgZBagSlitrConvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgZBagSlitrConvyrRight = ImageTk.PhotoImage(switchRight)

# canvBagSlitrConvyr = ctk.CTkCanvas(frmBBagSlitrConvyr, width=image_width, height=image_height, highlightthickness=0)
# canvBagSlitrConvyr.pack()
# imgZBagSlitrConvyr = canvBagSlitrConvyr.create_image(0, 0, anchor='nw', image=imgZBagSlitrConvyrUp)

# btnKBagSlitrConvyr = canvBagSlitrConvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKBagSlitrConvyr = canvBagSlitrConvyr.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvBagSlitrConvyr.tag_bind(btnKBagSlitrConvyr, "<ButtonPress-1>", lambda event: chanBagSlitrConvyrSwitch("right"))
# canvBagSlitrConvyr.tag_bind(btnKBagSlitrConvyr, "<ButtonRelease-1>", reseBagSlitrConvyrSwicth)

imgZBagSlitrConvyrLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgZBagSlitrConvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriZBagSlitrConvyr = ctk.CTkButton(frmBBagSlitrConvyr,  image=imgZBagSlitrConvyrLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriZBagSlitrConvyr.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))

btnKananZBagSlitrConvyr = ctk.CTkButton(frmBBagSlitrConvyr, image=imgZBagSlitrConvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananZBagSlitrConvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))

frmZBagSlitrConvyrBawah = ctk.CTkFrame(frmBBagSlitrConvyr, fg_color="transparent", width=150)
frmZBagSlitrConvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSBagSlitrConvyrbawah = ctk.CTkFrame(frmZBagSlitrConvyrBawah, fg_color="transparent")
frmSBagSlitrConvyrbawah.grid(row=2, column=0, columnspan=2)
imagBagSlitrConvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MotorBagSlitrCnvyr.png'))
imagBagSlitrConvyrbawah = ctk.CTkImage(light_image=imagBagSlitrConvyrbawah, size=(180, 50))
ZManBagSlitrConvyrbawahLbl = ctk.CTkLabel(frmSBagSlitrConvyrbawah, image=imagBagSlitrConvyrbawah, text="")
ZManBagSlitrConvyrbawahLbl.pack(padx=1, pady=1)
# ------------
statBagSlitrCuter = "up"

frmZBagSlitrCuter = ctk.CTkFrame(frm_CommonManLineAtas, fg_color="white")
frmZBagSlitrCuter.grid(row=0, column=2, padx=20, pady=(0, 5))

frmZBagSlitrCuterLbl = ctk.CTkFrame(frmZBagSlitrCuter, fg_color=lightOrange, corner_radius=0, border_color="light grey",
                                   border_width=5)
frmZBagSlitrCuterLbl.grid(row=1, column=0, padx=5, pady=10)

lblSBagSlitrCuter = ctk.CTkLabel(frmZBagSlitrCuterLbl, text="Motor\nMotBagSlitrCuter", width=150)
lblSBagSlitrCuter.grid(row=0, column=0, padx=10, pady=5)

frmBBagSlitrCuter = ctk.CTkFrame(frmZBagSlitrCuter, fg_color="transparent")
frmBBagSlitrCuter.grid(row=2, column=0, padx=1, pady=1)

# imgZBagSlitrCuterUp = ImageTk.PhotoImage(switchUp)
# imgZBagSlitrCuterLeft = ImageTk.PhotoImage(switchLeft)
# imgZBagSlitrCuterRight = ImageTk.PhotoImage(switchRight)

# canvBagSlitrCuter = ctk.CTkCanvas(frmBBagSlitrCuter, width=image_width, height=image_height, highlightthickness=0)
# canvBagSlitrCuter.pack()
# imgZBagSlitrCuter = canvBagSlitrCuter.create_image(0, 0, anchor='nw', image=imgZBagSlitrCuterUp)

# btnKBagSlitrCuter = canvBagSlitrCuter.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKBagSlitrCuter = canvBagSlitrCuter.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvBagSlitrCuter.tag_bind(btnKBagSlitrCuter, "<ButtonPress-1>", lambda event: chanBagSlitrCuterSwitch("right"))
# canvBagSlitrCuter.tag_bind(btnKBagSlitrCuter, "<ButtonRelease-1>", reseBagSlitrCuterSwicth)

imgZBagSlitrCuterLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgZBagSlitrCuterRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriZBagSlitrCuter = ctk.CTkButton(frmBBagSlitrCuter,  image=imgZBagSlitrCuterLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriZBagSlitrCuter.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))

btnKananZBagSlitrCuter = ctk.CTkButton(frmBBagSlitrCuter, image=imgZBagSlitrCuterRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananZBagSlitrCuter.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))

frmZBagSlitrCuterBawah = ctk.CTkFrame(frmBBagSlitrCuter, fg_color="transparent", width=150)
frmZBagSlitrCuterBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSBagSlitrCuterbawah = ctk.CTkFrame(frmZBagSlitrCuterBawah, fg_color="transparent")
frmSBagSlitrCuterbawah.grid(row=2, column=0, columnspan=2)
imagBagSlitrCuterbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MotorBagSlitrCuter.png'))
imagBagSlitrCuterbawah = ctk.CTkImage(light_image=imagBagSlitrCuterbawah, size=(180, 50))
ZManBagSlitrCuterbawahLbl = ctk.CTkLabel(frmSBagSlitrCuterbawah, image=imagBagSlitrCuterbawah, text="")
ZManBagSlitrCuterbawahLbl.pack(padx=1, pady=1)
# -----------------

# frm_CommonManLineTengah = ctk.CTkFrame(frame_tabManualCommon2, fg_color="white")
# frm_CommonManLineTengah.grid(row=2, column=0, padx=10, pady=1, sticky="w")



# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualCommon2, fg_color="transparent")
frm_MenuBawah.grid(row=4, column=0, padx=1, pady=(470,1))

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="blue", text_color="white",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2, state="normal")
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU








# ================================================================================
# LINE Z - UI UX - SET Z - .zset
# ================================================================================

frame_SetAutoZ = ctk.CTkFrame(app, fg_color="white")
frame_SetAutoZ.pack(fill="both", expand=True)

main_frame = ctk.CTkFrame(frame_SetAutoZ, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=10, pady=0)

# Frame container untuk area di sebelah kiri
area_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
area_frame.pack(side="left", anchor="nw", padx=10, pady=0)

# Membuat frame container untuk area baris pertama (judul 1-4)
row1_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row1_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris pertama secara horizontal

# Membuat area frame untuk judul 1-4 di baris pertama
create_area_frame(row1_frame, "Pneum FeedThreeDoor 0", "V0064")
create_area_frame(row1_frame, "Pneum FeedThreeDoor 1", "V0065")



# Frame untuk kalkulator di sebelah kanan
calculator_frame = ctk.CTkFrame(main_frame, width=330, height=410, corner_radius=10, fg_color="gray")
calculator_frame.pack(side="right", anchor="ne", padx=10, pady=120)

# Baris pertama: /, *, -, <-
row1_buttons = ["/", "*", "-", "←"]
for i, text in enumerate(row1_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=0, column=i, padx=7.5, pady=7.5, sticky="nsew")  # Menggunakan grid untuk penempatan

# Baris kedua: 7, 8, 9, +
row2_buttons = ["7", "8", "9"]
for i, text in enumerate(row2_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=1, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Tombol + yang menggabungkan baris kedua dan ketiga
button_plus = ctk.CTkButton(calculator_frame, text="+", command=lambda: on_calculator_button_click("+"), width=60, height=125, fg_color="white", text_color="black", font=("Helvetica", 24))
button_plus.grid(row=1, column=3, rowspan=2, padx=7.5, pady=7.5, sticky="nsew")

# Baris ketiga: 4, 5, 6
row3_buttons = ["4", "5", "6"]
for i, text in enumerate(row3_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=2, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Baris keempat: 1, 2, 3
row4_buttons = ["1", "2", "3"]
for i, text in enumerate(row4_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=3, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Menggabungkan tombol Backspace ke baris keempat dan kelima
button_backspace = ctk.CTkButton(calculator_frame, text="↵", command=lambda: on_calculator_button_click("↵"), width=60, height=125, fg_color="white", text_color="black", font=("Helvetica", 24))
button_backspace.grid(row=3, column=3, rowspan=2, padx=7.5, pady=7.5, sticky="nsew")

# Baris kelima: 0, .
button_zero = ctk.CTkButton(calculator_frame, text="0", command=lambda: on_calculator_button_click("0"), width=125, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
button_zero.grid(row=4, column=0, columnspan=2, padx=7.5, pady=7.5, sticky="nsew")

button_dot = ctk.CTkButton(calculator_frame, text=".", command=lambda: on_calculator_button_click("."), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 44))
button_dot.grid(row=4, column=2, padx=7.5, pady=7.5, sticky="nsew")


# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_SetAutoZ, fg_color="transparent")
frm_MenuBawah.pack(side="bottom", anchor="s", fill="x", pady=0)

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ, state="normal")
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU









# ================================================================================
# LINE B - UI UX - MANUAL 1/3 - .bman1
# ================================================================================

frame_tabManualBesar1 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualBesar1.pack(fill="both", expand=True)

# START MatCol
frm_MatCol = ctk.CTkFrame(frame_tabManualBesar1, fg_color="white")
frm_MatCol.grid(row=0, column=0, padx=1, pady=1)

lbl_MatCol = ctk.CTkLabel(frm_MatCol, text="Material Color", font=('Helvetica', 16))
lbl_MatCol.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarna = ctk.CTkFrame(frm_MatCol)
frm_BtnWarna.grid(row=1, column=0, columnspan=5, pady=1)

btnAutoFeedPutih = ctk.CTkButton(frm_BtnWarna, text="Putih", fg_color="light green", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnFeederBPutih, height=btnSize)
btnAutoFeedPutih.grid(row=1, column=0, padx=5, pady=(10, 10))

btnAutoFeedWarna1 = ctk.CTkButton(frm_BtnWarna, text="Warna 1", fg_color="pink",text_color="white", border_color="black", border_width=5,
                                     command=cmdBtnFeederBWarna1, height=btnSize)
btnAutoFeedWarna1.grid(row=1, column=1, padx=5, pady=(10, 10))

btnAutoFeedWarna2 = ctk.CTkButton(frm_BtnWarna, text="Warna 2", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnFeederBWarna2, height=btnSize)
btnAutoFeedWarna2.grid(row=1, column=2, padx=5, pady=(10, 10))

btnAutoFeedWarna3 = ctk.CTkButton(frm_BtnWarna, text="Warna 3", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                  command=cmdBtnFeederBWarna3, height=btnSize)
btnAutoFeedWarna3.grid(row=1, column=3, padx=5, pady=(10, 10))

btnManFeedAuto = ctk.CTkButton(frm_MatCol, text="Auto", fg_color="red", text_color="black", border_color="black", border_width=5,
                                 command=showAutoBesarB2, height=btnSize)
btnManFeedAuto.grid(row=1, column=5, padx=20, pady=(10, 10))
# END MatCol
# START ProdType
frm_ProdType = ctk.CTkFrame(frame_tabManualBesar1, fg_color="white")
frm_ProdType.grid(row=1, column=0, padx=1, pady=1)

lbl_ProdType = ctk.CTkLabel(frm_ProdType, text="Product Type", font=('Helvetica', 16))
lbl_ProdType.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarna = ctk.CTkFrame(frm_ProdType)
frm_BtnWarna.grid(row=1, column=0, columnspan=5, pady=1)

btnAutoHopperPutih = ctk.CTkButton(frm_BtnWarna, text="Putih", fg_color="light green", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnHopperBPutih, height=btnSize)
btnAutoHopperPutih.grid(row=1, column=0, padx=5, pady=(10, 10))

btnAutoHopperWarna1 = ctk.CTkButton(frm_BtnWarna, text="Warna", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                        command=cmdBtnHopperBWarna, height=btnSize)
btnAutoHopperWarna1.grid(row=1, column=1, padx=5, pady=(10, 10))

btnManHopperAuto = ctk.CTkButton(frm_ProdType, text="Auto", fg_color="red", text_color="black", border_color="black", border_width=5,
                                command=showAutoBesarB2, height=btnSize)
btnManHopperAuto.grid(row=1, column=5, padx=20, pady=(10, 10))
# END ProdType
# START frm_BesarB1LineTengah
frm_BesarB1LineTengah = ctk.CTkFrame(frame_tabManualBesar1, fg_color="white")
frm_BesarB1LineTengah.grid(row=2, column=0, padx=10, pady=1, sticky="w")

# # ------------
stateBManMateriVbrator = "up"

frmBManMateriVbrator = ctk.CTkFrame(frm_BesarB1LineTengah, fg_color="white")
frmBManMateriVbrator.grid(row=0, column=0, padx=20, pady=(0, 5))

frmBManMateriVbratorLbl = ctk.CTkFrame(frmBManMateriVbrator, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManMateriVbratorLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManMateriVbrator = ctk.CTkLabel(frmBManMateriVbratorLbl, text="Motor\nOsciliating", width=150)
lblSwitchBManMateriVbrator.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManMateriVbrator = ctk.CTkFrame(frmBManMateriVbrator, fg_color="transparent")
frmBtnBManMateriVbrator.grid(row=2, column=0, padx=1, pady=1)

# imgBManMateriVbratorUp = ImageTk.PhotoImage(switchUp)
# imgBManMateriVbratorLeft = ImageTk.PhotoImage(switchLeft)
# imgBManMateriVbratorRight = ImageTk.PhotoImage(switchRight)

# canvasBManMateriVbrator = ctk.CTkCanvas(frmBtnBManMateriVbrator, width=image_width, height=image_height, highlightthickness=0)
# canvasBManMateriVbrator.pack()
# imgBManMateriVbrator = canvasBManMateriVbrator.create_image(0, 0, anchor='nw', image=imgBManMateriVbratorUp)

# btnKiriBManMateriVbrator = canvasBManMateriVbrator.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManMateriVbrator = canvasBManMateriVbrator.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvasBManMateriVbrator.tag_bind(btnKananBManMateriVbrator, "<ButtonPress-1>", lambda event: changeBManMateriVbratorSwitch("right"))
# canvasBManMateriVbrator.tag_bind(btnKananBManMateriVbrator, "<ButtonRelease-1>", resetBManMateriVbratorSwicth)

imgBManMateriVbratorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMateriVbratorRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

# btnKiriBManMateriVbrator = ctk.CTkButton(frmBtnBManMateriVbrator,  image=imgBManMateriVbratorLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
# btnKiriBManMateriVbrator.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))
# btnKiriBManMateriVbrator.bind("<Button-1>", lambda event: btnKiriBManMateriVbratorClick())
# btnKiriBManMateriVbrator.bind("<ButtonRelease-1>", lambda event: btnKiriBManMateriVbratorClickReset())

btnKananBManMateriVbrator = ctk.CTkButton(frmBtnBManMateriVbrator, image=imgBManMateriVbratorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManMateriVbrator.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManMateriVbrator.bind("<Button-1>", lambda event: btnKananBManMateriVbratorClick())
btnKananBManMateriVbrator.bind("<ButtonRelease-1>", lambda event: btnKananBManMateriVbratorClickReset())

frmBManMateriVbratorBawah = ctk.CTkFrame(frmBtnBManMateriVbrator, fg_color="transparent", width=150)
frmBManMateriVbratorBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchBManMateriVbratorbawah = ctk.CTkFrame(frmBManMateriVbratorBawah, fg_color="transparent")
frmSwitchBManMateriVbratorbawah.grid(row=2, column=0, columnspan=2)
imageBManMateriVbratorbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MateriVbrator.png'))
imageBManMateriVbratorbawah = ctk.CTkImage(light_image=imageBManMateriVbratorbawah, size=(180, 50))
BManMateriVbratorbawahLbl = ctk.CTkLabel(frmSwitchBManMateriVbratorbawah, image=imageBManMateriVbratorbawah, text="")
BManMateriVbratorbawahLbl.pack(padx=1, pady=1)
# ------------
stateBManMatScrewCnvyr = "up"

frmBManMatScrewCnvyr = ctk.CTkFrame(frm_BesarB1LineTengah, fg_color="white")
frmBManMatScrewCnvyr.grid(row=0, column=1, padx=10, pady=(0, 5))

frmBManMatScrewCnvyrLbl = ctk.CTkFrame(frmBManMatScrewCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManMatScrewCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManMatScrewCnvyr = ctk.CTkLabel(frmBManMatScrewCnvyrLbl, text="Motor\nScrew", width=150)
lblSwitchBManMatScrewCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManMatScrewCnvyr = ctk.CTkFrame(frmBManMatScrewCnvyr, fg_color="transparent")
frmBtnBManMatScrewCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgBManMatScrewCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgBManMatScrewCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgBManMatScrewCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasBManMatScrewCnvyr = ctk.CTkCanvas(frmBtnBManMatScrewCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasBManMatScrewCnvyr.pack()
# imgBManMatScrewCnvyr = canvasBManMatScrewCnvyr.create_image(0, 0, anchor='nw', image=imgBManMatScrewCnvyrUp)

# btnKiriBManMatScrewCnvyr = canvasBManMatScrewCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManMatScrewCnvyr = canvasBManMatScrewCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# # Bind click events to transparent rectangles
# canvasBManMatScrewCnvyr.tag_bind(btnKiriBManMatScrewCnvyr, "<ButtonPress-1>", lambda event: changeBManMatScrewCnvyrSwitch("left"))
# canvasBManMatScrewCnvyr.tag_bind(btnKiriBManMatScrewCnvyr, "<ButtonRelease-1>", resetBManMatScrewCnvyrSwicth)

# canvasBManMatScrewCnvyr.tag_bind(btnKananBManMatScrewCnvyr, "<ButtonPress-1>", lambda event: changeBManMatScrewCnvyrSwitch("right"))
# canvasBManMatScrewCnvyr.tag_bind(btnKananBManMatScrewCnvyr, "<ButtonRelease-1>", resetBManMatScrewCnvyrSwicth)

imgBManMatScrewCnvyrLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMatScrewCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMatScrewCnvyrLeft = ctk.CTkImage(btnLeft, size=(btnRedGreenSize, btnRedGreenSize))
imgBManMatScrewCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriBManMatScrewCnvyr = ctk.CTkButton(frmBtnBManMatScrewCnvyr,  image=imgBManMatScrewCnvyrLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriBManMatScrewCnvyr.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))
btnKiriBManMatScrewCnvyr.bind("<Button-1>", lambda event: btnKiriBManMatScrewCnvyrClick())
btnKiriBManMatScrewCnvyr.bind("<ButtonRelease-1>", lambda event: btnKiriBManMatScrewCnvyrClickReset())

btnKananBManMatScrewCnvyr = ctk.CTkButton(frmBtnBManMatScrewCnvyr, image=imgBManMatScrewCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManMatScrewCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManMatScrewCnvyr.bind("<Button-1>", lambda event: btnKananBManMatScrewCnvyrClick())
btnKananBManMatScrewCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananBManMatScrewCnvyrClickReset())

frmBManMatScrewCnvyrBawah = ctk.CTkFrame(frmBtnBManMatScrewCnvyr, fg_color="transparent", width=150)
frmBManMatScrewCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)


frmSwitchBManMatScrewCnvyrbawah = ctk.CTkFrame(frmBManMatScrewCnvyrBawah, fg_color="transparent")
frmSwitchBManMatScrewCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageBManMatScrewCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MatScrewCnvyr.png'))
imageBManMatScrewCnvyrbawah = ctk.CTkImage(light_image=imageBManMatScrewCnvyrbawah, size=(180, 50))
BManMatScrewCnvyrbawahLbl = ctk.CTkLabel(frmSwitchBManMatScrewCnvyrbawah, image=imageBManMatScrewCnvyrbawah, text="")
BManMatScrewCnvyrbawahLbl.pack(padx=1, pady=(15, 0))
# ------------
stateBManToRotaryCnvyr = "up"

frmBManToRotaryCnvyr = ctk.CTkFrame(frm_BesarB1LineTengah, fg_color="white")
frmBManToRotaryCnvyr.grid(row=0, column=2, padx=10, pady=(0, 5))

frmBManToRotaryCnvyrLbl = ctk.CTkFrame(frmBManToRotaryCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManToRotaryCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManToRotaryCnvyr = ctk.CTkLabel(frmBManToRotaryCnvyrLbl, text="Conveyor\nto Rotary", width=150)
lblSwitchBManToRotaryCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManToRotaryCnvyr = ctk.CTkFrame(frmBManToRotaryCnvyr, fg_color="transparent")
frmBtnBManToRotaryCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgBManToRotaryCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgBManToRotaryCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgBManToRotaryCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasBManToRotaryCnvyr = ctk.CTkCanvas(frmBtnBManToRotaryCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasBManToRotaryCnvyr.pack()
# imgBManToRotaryCnvyr = canvasBManToRotaryCnvyr.create_image(0, 0, anchor='nw', image=imgBManToRotaryCnvyrUp)

# btnKiriBManToRotaryCnvyr = canvasBManToRotaryCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManToRotaryCnvyr = canvasBManToRotaryCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')
                                                                                             
# canvasBManToRotaryCnvyr.tag_bind(btnKananBManToRotaryCnvyr, "<ButtonPress-1>", lambda event: changeBManToRotaryCnvyrSwitch("right"))
# canvasBManToRotaryCnvyr.tag_bind(btnKananBManToRotaryCnvyr, "<ButtonRelease-1>", resetBManToRotaryCnvyrSwicth)

imgBManToRotaryCnvyrLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManToRotaryCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManToRotaryCnvyrLeft = ctk.CTkImage(btnLeft, size=(btnRedGreenSize, btnRedGreenSize))
imgBManToRotaryCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))


btnKananBManToRotaryCnvyr = ctk.CTkButton(frmBtnBManToRotaryCnvyr, image=imgBManToRotaryCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManToRotaryCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManToRotaryCnvyr.bind("<Button-1>", lambda event: btnKananBManToRotaryCnvyrClick())
btnKananBManToRotaryCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananBManToRotaryCnvyrClickReset())

frmBManToRotaryCnvyrBawah = ctk.CTkFrame(frmBtnBManToRotaryCnvyr, fg_color="transparent", width=150)
frmBManToRotaryCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchBManToRotaryCnvyrbawah = ctk.CTkFrame(frmBManToRotaryCnvyrBawah, fg_color="transparent")
frmSwitchBManToRotaryCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageBManToRotaryCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr.png'))
imageBManToRotaryCnvyrbawah = ctk.CTkImage(light_image=imageBManToRotaryCnvyrbawah, size=(180, 50))
BManToRotaryCnvyrbawahLbl = ctk.CTkLabel(frmSwitchBManToRotaryCnvyrbawah, image=imageBManToRotaryCnvyrbawah, text="")
BManToRotaryCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToRotaryCnvyr0 = ctk.CTkFrame(frm_BesarB1LineTengah, fg_color="white")
frmBManToRotaryCnvyr0.grid(row=0, column=3, padx=(20, 20), pady=1)

frmnBManRtaryUnitHop0 = ctk.CTkFrame(frmBManToRotaryCnvyr0, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManRtaryUnitHop0.grid(row=0, column=0, padx=(10,0), pady=(5, 5))

lblSensornRtaryUnitHop0 = ctk.CTkLabel(frmnBManRtaryUnitHop0, text="Hopper Rotary 5", width=150)
lblSensornRtaryUnitHop0.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToRotaryCnvyr0 = ctk.CTkFrame(frmBManToRotaryCnvyr0, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToRotaryCnvyr0.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToRotaryCnvyr0.bind("<ButtonPress-1>", lambda event: btnGreenBManToRotaryCnvyr0Click())
btnGreenBManToRotaryCnvyr0.bind("<ButtonRelease-1>", lambda event: btnGreenBManToRotaryCnvyr0ClickReset())

frmSwitchBManToRotaryCnvyr0bawah = ctk.CTkFrame(frmBManToRotaryCnvyr0, fg_color="transparent")
frmSwitchBManToRotaryCnvyr0bawah.grid(row=2, column=0, columnspan=2)
imageBManToRotaryCnvyr0bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr0.png'))
imageBManToRotaryCnvyr0bawah = ctk.CTkImage(light_image=imageBManToRotaryCnvyr0bawah, size=(180, 50))
BManToRotaryCnvyr0bawahLbl = ctk.CTkLabel(frmSwitchBManToRotaryCnvyr0bawah, image=imageBManToRotaryCnvyr0bawah, text="")
BManToRotaryCnvyr0bawahLbl.pack(padx=1, pady=1)
# END frm_BesarB1LineTengah
# START frm_BesarB1LineBawah
frm_BesarB1LineBawah = ctk.CTkFrame(frame_tabManualBesar1, fg_color="white")
frm_BesarB1LineBawah.grid(row=3, column=0, padx=10, pady=15, sticky="w")

# ------------
frmBManToRotaryCnvyr1 = ctk.CTkFrame(frm_BesarB1LineBawah, fg_color="white")
frmBManToRotaryCnvyr1.grid(row=0, column=0, padx=50, pady=1)

frmnBManRtaryUnitHop1 = ctk.CTkFrame(frmBManToRotaryCnvyr1, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManRtaryUnitHop1.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop1 = ctk.CTkLabel(frmnBManRtaryUnitHop1, text="Hopper Rotary 4", width=150)
lblSensornRtaryUnitHop1.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToRotaryCnvyr1 = ctk.CTkFrame(frmBManToRotaryCnvyr1, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToRotaryCnvyr1.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToRotaryCnvyr1.bind("<ButtonPress-1>", lambda event: btnGreenBManToRotaryCnvyr1Click())
btnGreenBManToRotaryCnvyr1.bind("<ButtonRelease-1>", lambda event: btnGreenBManToRotaryCnvyr1ClickReset())

frmSwitchBManToRotaryCnvyr1bawah = ctk.CTkFrame(frmBManToRotaryCnvyr1, fg_color="transparent")
frmSwitchBManToRotaryCnvyr1bawah.grid(row=2, column=0, columnspan=2)
imageBManToRotaryCnvyr1bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr1.png'))
imageBManToRotaryCnvyr1bawah = ctk.CTkImage(light_image=imageBManToRotaryCnvyr1bawah, size=(180, 50))
BManToRotaryCnvyr1bawahLbl = ctk.CTkLabel(frmSwitchBManToRotaryCnvyr1bawah, image=imageBManToRotaryCnvyr1bawah, text="")
BManToRotaryCnvyr1bawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToRotaryCnvyr2 = ctk.CTkFrame(frm_BesarB1LineBawah, fg_color="white")
frmBManToRotaryCnvyr2.grid(row=0, column=1, padx=(20, 20), pady=1)

frmnBManRtaryUnitHop2 = ctk.CTkFrame(frmBManToRotaryCnvyr2, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManRtaryUnitHop2.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop2 = ctk.CTkLabel(frmnBManRtaryUnitHop2, text="Hopper Rotary 3", width=150)
lblSensornRtaryUnitHop2.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToRotaryCnvyr2 = ctk.CTkFrame(frmBManToRotaryCnvyr2, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToRotaryCnvyr2.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToRotaryCnvyr2.bind("<ButtonPress-1>", lambda event: btnGreenBManToRotaryCnvyr2Click())
btnGreenBManToRotaryCnvyr2.bind("<ButtonRelease-1>", lambda event: btnGreenBManToRotaryCnvyr2ClickReset())

frmSwitchBManToRotaryCnvyr2bawah = ctk.CTkFrame(frmBManToRotaryCnvyr2, fg_color="transparent")
frmSwitchBManToRotaryCnvyr2bawah.grid(row=2, column=0, columnspan=2)
imageBManToRotaryCnvyr2bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr2.png'))
imageBManToRotaryCnvyr2bawah = ctk.CTkImage(light_image=imageBManToRotaryCnvyr2bawah, size=(180, 50))
BManToRotaryCnvyr2bawahLbl = ctk.CTkLabel(frmSwitchBManToRotaryCnvyr2bawah, image=imageBManToRotaryCnvyr2bawah, text="")
BManToRotaryCnvyr2bawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToRotaryCnvyr3 = ctk.CTkFrame(frm_BesarB1LineBawah, fg_color="white")
frmBManToRotaryCnvyr3.grid(row=0, column=2, padx=(20, 10), pady=1)

frmnBManRtaryUnitHop3 = ctk.CTkFrame(frmBManToRotaryCnvyr3, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManRtaryUnitHop3.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop3 = ctk.CTkLabel(frmnBManRtaryUnitHop3, text="Hopper Rotary 2", width=150)
lblSensornRtaryUnitHop3.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToRotaryCnvyr3 = ctk.CTkFrame(frmBManToRotaryCnvyr3, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToRotaryCnvyr3.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToRotaryCnvyr3.bind("<ButtonPress-1>", lambda event: btnGreenBManToRotaryCnvyr3Click())
btnGreenBManToRotaryCnvyr3.bind("<ButtonRelease-1>", lambda event: btnGreenBManToRotaryCnvyr3ClickReset())

frmSwitchBManToRotaryCnvyr3bawah = ctk.CTkFrame(frmBManToRotaryCnvyr3, fg_color="transparent")
frmSwitchBManToRotaryCnvyr3bawah.grid(row=2, column=0, columnspan=2)
imageBManToRotaryCnvyr3bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr3.png'))
imageBManToRotaryCnvyr3bawah = ctk.CTkImage(light_image=imageBManToRotaryCnvyr3bawah, size=(180, 50))
BManToRotaryCnvyr3bawahLbl = ctk.CTkLabel(frmSwitchBManToRotaryCnvyr3bawah, image=imageBManToRotaryCnvyr3bawah, text="")
BManToRotaryCnvyr3bawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToRotaryCnvyr4 = ctk.CTkFrame(frm_BesarB1LineBawah, fg_color="white")
frmBManToRotaryCnvyr4.grid(row=0, column=3, padx=(50, 15), pady=1)

frmnBManRtaryUnitHop4 = ctk.CTkFrame(frmBManToRotaryCnvyr4, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManRtaryUnitHop4.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop4 = ctk.CTkLabel(frmnBManRtaryUnitHop4, text="Hopper Rotary 1", width=150)
lblSensornRtaryUnitHop4.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToRotaryCnvyr4 = ctk.CTkFrame(frmBManToRotaryCnvyr4, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToRotaryCnvyr4.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToRotaryCnvyr4.bind("<ButtonPress-1>", lambda event: btnGreenBManToRotaryCnvyr4Click())
btnGreenBManToRotaryCnvyr4.bind("<ButtonRelease-1>", lambda event: btnGreenBManToRotaryCnvyr4ClickReset())

frmSwitchBManToRotaryCnvyr4bawah = ctk.CTkFrame(frmBManToRotaryCnvyr4, fg_color="transparent")
frmSwitchBManToRotaryCnvyr4bawah.grid(row=2, column=0, columnspan=2)
imageBManToRotaryCnvyr4bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr4.png'))
imageBManToRotaryCnvyr4bawah = ctk.CTkImage(light_image=imageBManToRotaryCnvyr4bawah, size=(180, 50))
BManToRotaryCnvyr4bawahLbl = ctk.CTkLabel(frmSwitchBManToRotaryCnvyr4bawah, image=imageBManToRotaryCnvyr4bawah, text="")
BManToRotaryCnvyr4bawahLbl.pack(padx=1, pady=1)

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualBesar1, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=1, pady=(40,0))

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="blue", text_color="white",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA, state="normal")
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU
























# ================================================================================
# LINE B - UI UX - MANUAL 2/3 - .bman2
# ================================================================================

# -------------------------------------------------------------------------------------------------------------------------
frame_tabManualBesar2 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualBesar2.pack(fill="both", expand=True)
# START frm_BesarB2LineAtas
frm_BesarB2LineAtas = ctk.CTkFrame(frame_tabManualBesar2, fg_color="white")
frm_BesarB2LineAtas.grid(row=0, column=0, padx=10, pady=1, sticky="w")



# ------------
# stateBManFrmRtaryCnvyr = "up"

frmBManRtaryCnvyr = ctk.CTkFrame(frm_BesarB2LineAtas, fg_color="white")
frmBManRtaryCnvyr.grid(row=0, column=0, padx=(30, 30), pady=(0, 5))

frmBManRtaryCnvyrLbl = ctk.CTkFrame(frmBManRtaryCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManRtaryCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManFrmRtaryCnvyr = ctk.CTkLabel(frmBManRtaryCnvyrLbl, text="Conveyor\nfrom Rtary", width=150)
lblSwitchBManFrmRtaryCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManFrmRtaryCnvyr = ctk.CTkFrame(frmBManRtaryCnvyr, fg_color="transparent")
frmBtnBManFrmRtaryCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgBManFrmRtaryCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgBManFrmRtaryCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgBManFrmRtaryCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasBManFrmRtaryCnvyr = ctk.CTkCanvas(frmBtnBManFrmRtaryCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasBManFrmRtaryCnvyr.pack()
# imgBManFrmRtaryCnvyr = canvasBManFrmRtaryCnvyr.create_image(0, 0, anchor='nw', image=imgBManFrmRtaryCnvyrUp)

# btnKiriBManFrmRtaryCnvyr = canvasBManFrmRtaryCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManFrmRtaryCnvyr = canvasBManFrmRtaryCnvyr.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvasBManFrmRtaryCnvyr.tag_bind(btnKananBManFrmRtaryCnvyr, "<ButtonPress-1>", lambda event: changeBManFrmRtaryCnvyrSwitch("right"))
# canvasBManFrmRtaryCnvyr.tag_bind(btnKananBManFrmRtaryCnvyr, "<ButtonRelease-1>", resetBManFrmRtaryCnvyrSwicth)

imgBManFrmRtaryCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManFrmRtaryCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananBManFrmRtaryCnvyr = ctk.CTkButton(frmBtnBManFrmRtaryCnvyr, image=imgBManFrmRtaryCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManFrmRtaryCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManFrmRtaryCnvyr.bind("<Button-1>", lambda event: btnKananBManFrmRtaryCnvyrClick())
btnKananBManFrmRtaryCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananBManFrmRtaryCnvyrClickReset())


frmBManFrmRtaryCnvyrBawah = ctk.CTkFrame(frmBtnBManFrmRtaryCnvyr, fg_color="transparent", width=150)
frmBManFrmRtaryCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchBManFrmRtaryCnvyrbawah = ctk.CTkFrame(frmBManFrmRtaryCnvyrBawah, fg_color="transparent")
frmSwitchBManFrmRtaryCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageBManFrmRtaryCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'FrmRtaryCnvyr.png'))
imageBManFrmRtaryCnvyrbawah = ctk.CTkImage(light_image=imageBManFrmRtaryCnvyrbawah, size=(180, 50))
BManFrmRtaryCnvyrbawahLbl = ctk.CTkLabel(frmSwitchBManFrmRtaryCnvyrbawah, image=imageBManFrmRtaryCnvyrbawah, text="")
BManFrmRtaryCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
# stateBManUpLadderCnvyr = "up"

frmBManUpLadderCnvyr = ctk.CTkFrame(frm_BesarB2LineAtas, fg_color="white")
frmBManUpLadderCnvyr.grid(row=0, column=1, padx=1, pady=10)

frmBManUpLadderCnvyrLbl = ctk.CTkFrame(frmBManUpLadderCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManUpLadderCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManUpLadderCnvyr = ctk.CTkLabel(frmBManUpLadderCnvyrLbl, text="Incline Conveyor", width=150)
lblSwitchBManUpLadderCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManUpLadderCnvyr = ctk.CTkFrame(frmBManUpLadderCnvyr, fg_color="transparent")
frmBtnBManUpLadderCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgBManUpLadderCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgBManUpLadderCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgBManUpLadderCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasBManUpLadderCnvyr = ctk.CTkCanvas(frmBtnBManUpLadderCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasBManUpLadderCnvyr.pack()
# imgBManUpLadderCnvyr = canvasBManUpLadderCnvyr.create_image(0, 0, anchor='nw', image=imgBManUpLadderCnvyrUp)

# btnKiriBManUpLadderCnvyr = canvasBManUpLadderCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManUpLadderCnvyr = canvasBManUpLadderCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasBManUpLadderCnvyr.tag_bind(btnKananBManUpLadderCnvyr, "<ButtonPress-1>", lambda event: changeBManUpLadderCnvyrSwitch("right"))
# canvasBManUpLadderCnvyr.tag_bind(btnKananBManUpLadderCnvyr, "<ButtonRelease-1>", resetBManUpLadderCnvyrSwicth)

imgBManUpLadderCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManUpLadderCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananBManUpLadderCnvyr = ctk.CTkButton(frmBtnBManUpLadderCnvyr, image=imgBManUpLadderCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManUpLadderCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManUpLadderCnvyr.bind("<Button-1>", lambda event: btnKananBManUpLadderCnvyrClick())
btnKananBManUpLadderCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananBManUpLadderCnvyrClickReset())

frmBManUpLadderCnvyrBawah = ctk.CTkFrame(frmBtnBManUpLadderCnvyr, fg_color="transparent", width=150)
frmBManUpLadderCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchBManUpLadderCnvyrbawah = ctk.CTkFrame(frmBManUpLadderCnvyrBawah, fg_color="transparent")
frmSwitchBManUpLadderCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageBManUpLadderCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'UpLadderCnvyr.png'))
imageBManUpLadderCnvyrbawah = ctk.CTkImage(light_image=imageBManUpLadderCnvyrbawah, size=(180, 50))
BManUpLadderCnvyrbawahLbl = ctk.CTkLabel(frmSwitchBManUpLadderCnvyrbawah, image=imageBManUpLadderCnvyrbawah, text="")
BManUpLadderCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
# stateBManToHopperCnvyr = "up"

frmBManToHopperCnvyr = ctk.CTkFrame(frm_BesarB2LineAtas, fg_color="white")
frmBManToHopperCnvyr.grid(row=0, column=2, padx=20, pady=5)

frmBManToHopperCnvyrLbl = ctk.CTkFrame(frmBManToHopperCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmBManToHopperCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchBManToHopperCnvyr = ctk.CTkLabel(frmBManToHopperCnvyrLbl, text="Conveyor to Silo", width=150)
lblSwitchBManToHopperCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnBManToHopperCnvyr = ctk.CTkFrame(frmBManToHopperCnvyr, fg_color="transparent")
frmBtnBManToHopperCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgBManToHopperCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgBManToHopperCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgBManToHopperCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasBManToHopperCnvyr = ctk.CTkCanvas(frmBtnBManToHopperCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasBManToHopperCnvyr.pack()
# imgBManToHopperCnvyr = canvasBManToHopperCnvyr.create_image(0, 0, anchor='nw', image=imgBManToHopperCnvyrUp)

# btnKiriBManToHopperCnvyr = canvasBManToHopperCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananBManToHopperCnvyr = canvasBManToHopperCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasBManToHopperCnvyr.tag_bind(btnKananBManToHopperCnvyr, "<ButtonPress-1>", lambda event: changeBManToHopperCnvyrSwitch("right"))
# canvasBManToHopperCnvyr.tag_bind(btnKananBManToHopperCnvyr, "<ButtonRelease-1>", resetBManToHopperCnvyrSwicth)

imgBManToHopperCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManToHopperCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananBManToHopperCnvyr = ctk.CTkButton(frmBtnBManToHopperCnvyr, image=imgBManToHopperCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManToHopperCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManToHopperCnvyr.bind("<Button-1>", lambda event: btnKananBManToHopperCnvyrClick())
btnKananBManToHopperCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananBManToHopperCnvyrClickReset())

frmBManToHopperCnvyrBawah = ctk.CTkFrame(frmBtnBManToHopperCnvyr, fg_color="transparent", width=150)
frmBManToHopperCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchBManToHopperCnvyrbawah = ctk.CTkFrame(frmBManToHopperCnvyrBawah, fg_color="transparent")
frmSwitchBManToHopperCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageBManToHopperCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr.png'))
imageBManToHopperCnvyrbawah = ctk.CTkImage(light_image=imageBManToHopperCnvyrbawah, size=(180, 50))
BManToHopperCnvyrbawahLbl = ctk.CTkLabel(frmSwitchBManToHopperCnvyrbawah, image=imageBManToHopperCnvyrbawah, text="")
BManToHopperCnvyrbawahLbl.pack(padx=1, pady=1)
# END frm_BesarB2LineAtas
# START frm_BesarB2LineTengah
frm_BesarB2LineTengah = ctk.CTkFrame(frame_tabManualBesar2, fg_color="white")
frm_BesarB2LineTengah.grid(row=1, column=0, padx=10, pady=1, sticky="w")

# ------------
frmBManToHopperCnvyr0 = ctk.CTkFrame(frm_BesarB2LineTengah, fg_color="white")
frmBManToHopperCnvyr0.grid(row=0, column=0, padx=(30, 15), pady=1)

frmnBManTabletVaryHop0 = ctk.CTkFrame(frmBManToHopperCnvyr0, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManTabletVaryHop0.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornBManTabletVaryHop0 = ctk.CTkLabel(frmnBManTabletVaryHop0, text="Sensor Silo 4", width=150)
lblSensornBManTabletVaryHop0.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToHopperCnvyr0 = ctk.CTkFrame(frmBManToHopperCnvyr0, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToHopperCnvyr0.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToHopperCnvyr0.bind("<ButtonPress-1>", lambda event: btnGreenBManToHopperCnvyr0Click())
btnGreenBManToHopperCnvyr0.bind("<ButtonRelease-1>", lambda event: btnGreenBManToHopperCnvyr0ClickReset())

frmSwitchBManToHopperCnvyr0bawah = ctk.CTkFrame(frmBManToHopperCnvyr0, fg_color="transparent")
frmSwitchBManToHopperCnvyr0bawah.grid(row=2, column=0, columnspan=2)
imageBManToHopperCnvyr0bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr0.png'))
imageBManToHopperCnvyr0bawah = ctk.CTkImage(light_image=imageBManToHopperCnvyr0bawah, size=(180, 50))
BManToHopperCnvyr0bawahLbl = ctk.CTkLabel(frmSwitchBManToHopperCnvyr0bawah, image=imageBManToHopperCnvyr0bawah, text="")
BManToHopperCnvyr0bawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToHopperCnvyr1 = ctk.CTkFrame(frm_BesarB2LineTengah, fg_color="white")
frmBManToHopperCnvyr1.grid(row=0, column=1, padx=(65, 20), pady=1)

frmnBManTabletVaryHop1 = ctk.CTkFrame(frmBManToHopperCnvyr1, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnBManTabletVaryHop1.grid(row=0, column=0, padx=15, pady=(5, 5))

lblSensornBManTabletVaryHop1 = ctk.CTkLabel(frmnBManTabletVaryHop1, text="Sensor Silo 3", width=150)
lblSensornBManTabletVaryHop1.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToHopperCnvyr1 = ctk.CTkFrame(frmBManToHopperCnvyr1, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToHopperCnvyr1.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToHopperCnvyr1.bind("<ButtonPress-1>", lambda event: btnGreenBManToHopperCnvyr1Click())
btnGreenBManToHopperCnvyr1.bind("<ButtonRelease-1>", lambda event: btnGreenBManToHopperCnvyr1ClickReset())

frmSwitchBManToHopperCnvyr1bawah = ctk.CTkFrame(frmBManToHopperCnvyr1, fg_color="transparent")
frmSwitchBManToHopperCnvyr1bawah.grid(row=2, column=0, columnspan=2)
imageBManToHopperCnvyr1bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr1.png'))
imageBManToHopperCnvyr1bawah = ctk.CTkImage(light_image=imageBManToHopperCnvyr1bawah, size=(180, 50))
BManToHopperCnvyr1bawahLbl = ctk.CTkLabel(frmSwitchBManToHopperCnvyr1bawah, image=imageBManToHopperCnvyr1bawah, text="")
BManToHopperCnvyr1bawahLbl.pack(padx=1, pady=1)
# END frm_BesarB2LineTengah
# START frm_BesarB2LineBawah
frm_BesarB2LineBawah = ctk.CTkFrame(frame_tabManualBesar2, fg_color="white")
frm_BesarB2LineBawah.grid(row=2, column=0, padx=10, pady=1, sticky="w")
# ------------
frmBManToHopperCnvyr2 = ctk.CTkFrame(frm_BesarB2LineBawah, fg_color="white")
frmBManToHopperCnvyr2.grid(row=0, column=0, padx=(30, 15), pady=12)

frmnManBTabletVaryHop2 = ctk.CTkFrame(frmBManToHopperCnvyr2, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManBTabletVaryHop2.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornManBTabletVaryHop2 = ctk.CTkLabel(frmnManBTabletVaryHop2, text="Sensor Silo 2", width=150)
lblSensornManBTabletVaryHop2.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToHopperCnvyr2 = ctk.CTkFrame(frmBManToHopperCnvyr2, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToHopperCnvyr2.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToHopperCnvyr2.bind("<ButtonPress-1>", lambda event: btnGreenBManToHopperCnvyr2Click())
btnGreenBManToHopperCnvyr2.bind("<ButtonRelease-1>", lambda event: btnGreenBManToHopperCnvyr2ClickReset())

frmSwitchBManToHopperCnvyr2bawah = ctk.CTkFrame(frmBManToHopperCnvyr2, fg_color="transparent")
frmSwitchBManToHopperCnvyr2bawah.grid(row=2, column=0, columnspan=2)
imageBManToHopperCnvyr2bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr2.png'))
imageBManToHopperCnvyr2bawah = ctk.CTkImage(light_image=imageBManToHopperCnvyr2bawah, size=(180, 50))
BManToHopperCnvyr2bawahLbl = ctk.CTkLabel(frmSwitchBManToHopperCnvyr2bawah, image=imageBManToHopperCnvyr2bawah, text="")
BManToHopperCnvyr2bawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToHopperCnvyr3 = ctk.CTkFrame(frm_BesarB2LineBawah, fg_color="white")
frmBManToHopperCnvyr3.grid(row=0, column=1, padx=(75, 20), pady=1)

frmnManBTabletVaryHop3 = ctk.CTkFrame(frmBManToHopperCnvyr3, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManBTabletVaryHop3.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornManBTabletVaryHop3 = ctk.CTkLabel(frmnManBTabletVaryHop3, text="Sensor Silo 1", width=150)
lblSensornManBTabletVaryHop3.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToHopperCnvyr3 = ctk.CTkFrame(frmBManToHopperCnvyr3, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToHopperCnvyr3.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToHopperCnvyr3.bind("<ButtonPress-1>", lambda event: btnGreenBManToHopperCnvyr3Click())
btnGreenBManToHopperCnvyr3.bind("<ButtonRelease-1>", lambda event: btnGreenBManToHopperCnvyr3ClickReset())

frmSwitchBManToHopperCnvyr3bawah = ctk.CTkFrame(frmBManToHopperCnvyr3, fg_color="transparent")
frmSwitchBManToHopperCnvyr3bawah.grid(row=2, column=0, columnspan=2)
imageBManToHopperCnvyr3bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr3.png'))
imageBManToHopperCnvyr3bawah = ctk.CTkImage(light_image=imageBManToHopperCnvyr3bawah, size=(180, 50))
BManToHopperCnvyr3bawahLbl = ctk.CTkLabel(frmSwitchBManToHopperCnvyr3bawah, image=imageBManToHopperCnvyr3bawah, text="")
BManToHopperCnvyr3bawahLbl.pack(padx=1, pady=1)

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualBesar2, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=1, pady=(48,0))

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="blue", text_color="white",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB, state="normal")
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU















# ================================================================================
# LINE B - UI UX - MANUAL 3/3 - .bman3
# ================================================================================

# -------------------------------------------------------------------------------------------------------------------------
frame_tabManualBesar3 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualBesar3.pack(fill="both", expand=True)
# START frm_BesarB3LineAtas
frm_BesarB3LineAtas = ctk.CTkFrame(frame_tabManualBesar3, fg_color="white")
frm_BesarB3LineAtas.grid(row=0, column=0, padx=10, pady=1, sticky="w")
# ------------
frmManBTbletHoprDoor0 = ctk.CTkFrame(frm_BesarB3LineAtas, fg_color="white")
frmManBTbletHoprDoor0.grid(row=0, column=0, padx=1, pady=(20, 5))

frmManBTbletHoprDoor0Lbl = ctk.CTkFrame(frmManBTbletHoprDoor0, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManBTbletHoprDoor0Lbl.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSwitchManBTbletHoprDoor0 = ctk.CTkLabel(frmManBTbletHoprDoor0Lbl, text="Silo Door 2", width=150)
lblSwitchManBTbletHoprDoor0.grid(row=1, column=0, padx=10, pady=5)

frmBtnManBTbletHoprDoor0 = ctk.CTkFrame(frmManBTbletHoprDoor0, fg_color="transparent")
frmBtnManBTbletHoprDoor0.grid(row=2, column=0, padx=1, pady=1)

btnRedManBTbletHoprDoor0 = ctk.CTkFrame(frmBtnManBTbletHoprDoor0, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='red', border_color="black", border_width=5)
btnRedManBTbletHoprDoor0.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManBTbletHoprDoor0.bind("<Button-1>", lambda event: btnRedManBTbletHoprDoor0Click())
btnRedManBTbletHoprDoor0.bind("<ButtonRelease-1>", lambda event: btnRedManBTbletHoprDoor0ClickReset())

btnGreenManBTbletHoprDoor0 = ctk.CTkFrame(frmBtnManBTbletHoprDoor0, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenManBTbletHoprDoor0.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManBTbletHoprDoor0.bind("<Button-1>", lambda event: btnGreenManBTbletHoprDoor0Click())
btnGreenManBTbletHoprDoor0.bind("<ButtonRelease-1>", lambda event: btnGreenManBTbletHoprDoor0ClickReset())

frmSwitchManBTbletHoprDoor0bawah = ctk.CTkFrame(frmBtnManBTbletHoprDoor0, fg_color="transparent")
frmSwitchManBTbletHoprDoor0bawah.grid(row=2, column=0, columnspan=2)
imageManBTbletHoprDoor0bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'TbletHoprDoor0.png'))
imageManBTbletHoprDoor0bawah = ctk.CTkImage(light_image=imageManBTbletHoprDoor0bawah, size=(160, 50))
ManBTbletHoprDoor0bawahLbl = ctk.CTkLabel(frmSwitchManBTbletHoprDoor0bawah, image=imageManBTbletHoprDoor0bawah, text="")
ManBTbletHoprDoor0bawahLbl.pack(padx=1, pady=1)
# ------------
frmManBTbletHoprDoor1 = ctk.CTkFrame(frm_BesarB3LineAtas, fg_color="white")
frmManBTbletHoprDoor1.grid(row=0, column=1, padx=(50, 1), pady=(20, 5))

frmManBTbletHoprDoor1Lbl = ctk.CTkFrame(frmManBTbletHoprDoor1, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManBTbletHoprDoor1Lbl.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSwitchManBTbletHoprDoor1 = ctk.CTkLabel(frmManBTbletHoprDoor1Lbl, text="Silo Door 1", width=150)
lblSwitchManBTbletHoprDoor1.grid(row=1, column=0, padx=10, pady=5)

frmBtnManBTbletHoprDoor1 = ctk.CTkFrame(frmManBTbletHoprDoor1, fg_color="transparent")
frmBtnManBTbletHoprDoor1.grid(row=2, column=0, padx=1, pady=1)

btnRedManBTbletHoprDoor1 = ctk.CTkFrame(frmBtnManBTbletHoprDoor1, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='red', border_color="black", border_width=5)
btnRedManBTbletHoprDoor1.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManBTbletHoprDoor1.bind("<Button-1>", lambda event: btnRedManBTbletHoprDoor1Click())
btnRedManBTbletHoprDoor1.bind("<ButtonRelease-1>", lambda event: btnRedManBTbletHoprDoor1ClickReset())

btnGreenManBTbletHoprDoor1 = ctk.CTkFrame(frmBtnManBTbletHoprDoor1, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenManBTbletHoprDoor1.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManBTbletHoprDoor1.bind("<Button-1>", lambda event: btnGreenManBTbletHoprDoor1Click())
btnGreenManBTbletHoprDoor1.bind("<ButtonRelease-1>", lambda event: btnGreenManBTbletHoprDoor1ClickReset())

frmSwitchManBTbletHoprDoor1bawah = ctk.CTkFrame(frmBtnManBTbletHoprDoor1, fg_color="transparent")
frmSwitchManBTbletHoprDoor1bawah.grid(row=2, column=0, columnspan=2)
imageManBTbletHoprDoor1bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'TbletHoprDoor1.png'))
imageManBTbletHoprDoor1bawah = ctk.CTkImage(light_image=imageManBTbletHoprDoor1bawah, size=(160, 50))
ManBTbletHoprDoor1bawahLbl = ctk.CTkLabel(frmSwitchManBTbletHoprDoor1bawah, image=imageManBTbletHoprDoor1bawah, text="")
ManBTbletHoprDoor1bawahLbl.pack(padx=1, pady=1)
# ------------
# stateManBTbletHoprDoor = "up"

frmManBTbletHoprDoor = ctk.CTkFrame(frm_BesarB3LineAtas, fg_color="white")
frmManBTbletHoprDoor.grid(row=0, column=2, padx=(50, 1), pady=20, sticky="n")

frmManBTbletHoprDoorLbl = ctk.CTkFrame(frmManBTbletHoprDoor, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmManBTbletHoprDoorLbl.grid(row=1, column=0, padx=5, pady=(15, 5))

lblSwitchManBTbletHoprDoor = ctk.CTkLabel(frmManBTbletHoprDoorLbl, text="Tablet Silo Door", width=150)
lblSwitchManBTbletHoprDoor.grid(row=0, column=0, padx=10, pady=5)

frmBtnManBTbletHoprDoor = ctk.CTkFrame(frmManBTbletHoprDoor, fg_color="transparent")
frmBtnManBTbletHoprDoor.grid(row=2, column=0, padx=1, pady=1)

# imgManBTbletHoprDoorUp = ImageTk.PhotoImage(switchUp)
# imgManBTbletHoprDoorLeft = ImageTk.PhotoImage(switchLeft)
# imgManBTbletHoprDoorRight = ImageTk.PhotoImage(switchRight)

# canvasManBTbletHoprDoor = ctk.CTkCanvas(frmBtnManBTbletHoprDoor, width=image_width, height=image_height, highlightthickness=0)
# canvasManBTbletHoprDoor.pack()
# imgManBTbletHoprDoor = canvasManBTbletHoprDoor.create_image(0, 0, anchor='nw', image=imgManBTbletHoprDoorUp)

# btnKiriManBTbletHoprDoor = canvasManBTbletHoprDoor.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananManBTbletHoprDoor = canvasManBTbletHoprDoor.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasManBTbletHoprDoor.tag_bind(btnKananManBTbletHoprDoor, "<ButtonPress-1>", lambda event: changeManBTbletHoprDoorSwitch("right"))
# canvasManBTbletHoprDoor.tag_bind(btnKananManBTbletHoprDoor, "<ButtonRelease-1>", resetManBTbletHoprDoorSwicth)

imgBManTbletHoprDoorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManTbletHoprDoorRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananBManTbletHoprDoor = ctk.CTkButton(frmBtnManBTbletHoprDoor, image=imgBManTbletHoprDoorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManTbletHoprDoor.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManTbletHoprDoor.bind("<Button-1>", lambda event: btnKananBManTbletHoprDoorClick())
btnKananBManTbletHoprDoor.bind("<ButtonRelease-1>", lambda event: btnKananBManTbletHoprDoorClickReset())

frmManBTbletHoprDoorBawah = ctk.CTkFrame(frmBtnManBTbletHoprDoor, fg_color="transparent", width=150)
frmManBTbletHoprDoorBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchManBTbletHoprDoorbawah = ctk.CTkFrame(frmManBTbletHoprDoorBawah, fg_color="transparent")
frmSwitchManBTbletHoprDoorbawah.grid(row=2, column=0, columnspan=2)
imageManBTbletHoprDoorbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'TbletHoprDoor.png'))
imageManBTbletHoprDoorbawah = ctk.CTkImage(light_image=imageManBTbletHoprDoorbawah, size=(180, 50))
ManBTbletHoprDoorbawahLbl = ctk.CTkLabel(frmSwitchManBTbletHoprDoorbawah, image=imageManBTbletHoprDoorbawah, text="")
ManBTbletHoprDoorbawahLbl.pack(padx=1, pady=1)
# ------------
stateManBToRncenCnvyr = "up"

frmManBToRncenCnvyr = ctk.CTkFrame(frm_BesarB3LineAtas, fg_color="white")
frmManBToRncenCnvyr.grid(row=0, column=3, padx=(50, 1), pady=20, sticky="n")

frmManBToRncenCnvyrLbl = ctk.CTkFrame(frmManBToRncenCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmManBToRncenCnvyrLbl.grid(row=1, column=0, padx=5, pady=(15, 5))

lblSwitchManBToRncenCnvyr = ctk.CTkLabel(frmManBToRncenCnvyrLbl, text="Modular Conveyor", width=150)
lblSwitchManBToRncenCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnManBToRncenCnvyr = ctk.CTkFrame(frmManBToRncenCnvyr, fg_color="transparent")
frmBtnManBToRncenCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgManBToRncenCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgManBToRncenCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgManBToRncenCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasManBToRncenCnvyr = ctk.CTkCanvas(frmBtnManBToRncenCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasManBToRncenCnvyr.pack()
# imgManBToRncenCnvyr = canvasManBToRncenCnvyr.create_image(0, 0, anchor='nw', image=imgManBToRncenCnvyrUp)

# btnKiriManBToRncenCnvyr = canvasManBToRncenCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananManBToRncenCnvyr = canvasManBToRncenCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                            image_height, outline='', fill='')

# canvasManBToRncenCnvyr.tag_bind(btnKananManBToRncenCnvyr, "<ButtonPress-1>", lambda event: changeManBToRncenCnvyrSwitch("right"))
# canvasManBToRncenCnvyr.tag_bind(btnKananManBToRncenCnvyr, "<ButtonRelease-1>", resetManBToRncenCnvyrSwicth)

imgBManToRncenCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgBManToRncenCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananBManToRncenCnvyr = ctk.CTkButton(frmBtnManBToRncenCnvyr, image=imgBManToRncenCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananBManToRncenCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananBManToRncenCnvyr.bind("<Button-1>", lambda event: btnKananBManToRncenCnvyrClick())
btnKananBManToRncenCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananBManToRncenCnvyrClickReset())

frmManBToRncenCnvyrBawah = ctk.CTkFrame(frmBtnManBToRncenCnvyr, fg_color="transparent", width=150)
frmManBToRncenCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchManBToRncenCnvyrbawah = ctk.CTkFrame(frmManBToRncenCnvyrBawah, fg_color="transparent")
frmSwitchManBToRncenCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageManBToRncenCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRncenCnvyrSw.png'))
imageManBToRncenCnvyrbawah = ctk.CTkImage(light_image=imageManBToRncenCnvyrbawah, size=(180, 50))
ManBToRncenCnvyrbawahLbl = ctk.CTkLabel(frmSwitchManBToRncenCnvyrbawah, image=imageManBToRncenCnvyrbawah, text="")
ManBToRncenCnvyrbawahLbl.pack(padx=1, pady=1)
# END frm_BesarB3LineAtas
# START frm_BesarB3LineTengah
frm_BesarB3LineTengah = ctk.CTkFrame(frame_tabManualBesar3, fg_color="white")
frm_BesarB3LineTengah.grid(row=1, column=0, padx=10, pady=30, sticky="w")
# ------------
frmBManToRncenCnvyr = ctk.CTkFrame(frm_BesarB3LineTengah, fg_color="white")
frmBManToRncenCnvyr.grid(row=0, column=0, padx=(20, 20), pady=1)

frmnRncenMachHop0 = ctk.CTkFrame(frmBManToRncenCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnRncenMachHop0.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop0 = ctk.CTkLabel(frmnRncenMachHop0, text="Sensor\nRncenMachHop 0", width=150)
lblSensornRncenMachHop0.grid(row=0, column=0, padx=10, pady=5)

btnGreenBManToRncenCnvyr = ctk.CTkFrame(frmBManToRncenCnvyr, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenBManToRncenCnvyr.grid(row=1, column=0, padx=1, pady=1)
btnGreenBManToRncenCnvyr.bind("<ButtonPress-1>", lambda event: btnGreenBManToRncenCnvyrClick())
btnGreenBManToRncenCnvyr.bind("<ButtonRelease-1>", lambda event: btnGreenBManToRncenCnvyrClickReset())

frmSwitchBManToRncenCnvyrbawah = ctk.CTkFrame(frmBManToRncenCnvyr, fg_color="transparent")
frmSwitchBManToRncenCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageBManToRncenCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRncenCnvyr.png'))
imageBManToRncenCnvyrbawah = ctk.CTkImage(light_image=imageBManToRncenCnvyrbawah, size=(180, 50))
BManToRncenCnvyrbawahLbl = ctk.CTkLabel(frmSwitchBManToRncenCnvyrbawah, image=imageBManToRncenCnvyrbawah, text="")
BManToRncenCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
frmBManToRncenCnvyrz = ctk.CTkFrame(frm_BesarB3LineTengah, fg_color="white")
frmBManToRncenCnvyrz.grid(row=0, column=1, padx=(45, 20), pady=1, sticky="n")

frmnRncenMachHop1 = ctk.CTkFrame(frmBManToRncenCnvyrz, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnRncenMachHop1.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop0 = ctk.CTkLabel(frmnRncenMachHop1, text="Sensor\nRncenMachHop 1", width=150)
lblSensornRncenMachHop0.grid(row=0, column=0, padx=10, pady=5)

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualBesar3, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=1, pady=(179,0), sticky="w")

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="blue", text_color="white",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC, state="normal")
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU




# ================================================================================
# LINE B - UI UX - AUTO 1/2 - .bauto1
# ================================================================================
frame_tabBesarBAuto = ctk.CTkFrame(app, fg_color="white")
frame_tabBesarBAuto.pack(fill="both", expand=True)


frmBAuto1 = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="white")
# frmBAuto1.pack(padx=5, pady=(1, 1))
frmBAuto1.grid(row=0, column=0, padx=10, pady=1, sticky="w")


frmBAutoMotorMateriVbrator = ctk.CTkFrame(frmBAuto1, fg_color="white")
frmBAutoMotorMateriVbrator.grid(row=0, column=0, padx=1, pady=1)

imageBAutoMotorMateriVbrator = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMateriVbrator.png'))
imageBAutoMotorMateriVbrator = ctk.CTkImage(light_image=imageBAutoMotorMateriVbrator, size=(160, 20)) 
BAutoMotorMateriVbratorLbl = ctk.CTkLabel(frmBAutoMotorMateriVbrator, image=imageBAutoMotorMateriVbrator, text="")
BAutoMotorMateriVbratorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnBAutoMotorMateriVbratorDoStart = ctk.CTkButton(frmBAutoMotorMateriVbrator, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMateriVbratorDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorMateriVbratorIsFault = ctk.CTkButton(frmBAutoMotorMateriVbrator, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMateriVbratorIsFault.grid(row=1, column=1, padx=1, pady=1)

# ------------
frmBAutoMotorMatScrewCnvyr = ctk.CTkFrame(frmBAuto1, fg_color="white")
frmBAutoMotorMatScrewCnvyr.grid(row=0, column=1, padx=1, pady=1)

imageBAutoMotorMatScrewCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMatScrewCnvyr.png'))
imageBAutoMotorMatScrewCnvyr = ctk.CTkImage(light_image=imageBAutoMotorMatScrewCnvyr, size=(240, 20)) 
BAutoMotorMatScrewCnvyrLbl = ctk.CTkLabel(frmBAutoMotorMatScrewCnvyr, image=imageBAutoMotorMatScrewCnvyr, text="")
BAutoMotorMatScrewCnvyrLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnBAutoMotorMatScrewCnvyrDoRev = ctk.CTkButton(frmBAutoMotorMatScrewCnvyr, text="Rev", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMatScrewCnvyrDoRev.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorMatScrewCnvyrDoFwd = ctk.CTkButton(frmBAutoMotorMatScrewCnvyr, text="Fwd", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMatScrewCnvyrDoFwd.grid(row=1, column=1, padx=1, pady=1)
btnBAutoMotorMatScrewCnvyrIsFault = ctk.CTkButton(frmBAutoMotorMatScrewCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorMatScrewCnvyrIsFault.grid(row=1, column=2, padx=1, pady=1)

frmBAutoMotorToRotaryCnvyr = ctk.CTkFrame(frmBAuto1, fg_color="white")
frmBAutoMotorToRotaryCnvyr.grid(row=0, column=2, padx=1, pady=1)

imageBAutoMotorToRotaryCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorToRotaryCnvyr.png'))
imageBAutoMotorToRotaryCnvyr = ctk.CTkImage(light_image=imageBAutoMotorToRotaryCnvyr, size=(160, 20)) 
BAutoMotorToRotaryCnvyrLbl = ctk.CTkLabel(frmBAutoMotorToRotaryCnvyr, image=imageBAutoMotorToRotaryCnvyr, text="")
BAutoMotorToRotaryCnvyrLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnBAutoMotorToRotaryCnvyrDoStart = ctk.CTkButton(frmBAutoMotorToRotaryCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorToRotaryCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorToRotaryCnvyrIsFault = ctk.CTkButton(frmBAutoMotorToRotaryCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorToRotaryCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

# btnBAutoMixingDoStart = ctk.CTkButton(frmBAutoMixing, text="DoStart", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
# btnBAutoMixingDoStart.grid(row=1, column=0, padx=1, pady=1)
# btnBAutoMixingIsFault = ctk.CTkButton(frmBAutoMixing, text="IsFault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
# btnBAutoMixingIsFault.grid(row=1, column=1, padx=1, pady=1)

# frame_with_Num = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
# frame_with_Num.grid(row=0, column=0,padx=(0,770), pady=(450,1))
# lbl_Num = ctk.CTkLabel(frame_with_Num, text="00.00", font=('Helvetica', 12), width=60, height=15)
# lbl_Num.grid(row=0, column=0,padx=3, pady=2)

# frame_with_Sec = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
# frame_with_Sec.grid(row=0, column=0,padx=(0,680), pady=(450,1))
# lbl_Sec = ctk.CTkLabel(frame_with_Sec, text="Sec", font=('Helvetica', 7), width=20, height=15)
# lbl_Sec.grid(row=0, column=0,padx=3, pady=2)

# ------------

frmBAuto2 = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="white")
# frmBAuto2.pack(padx=5, pady=(1, 1))
frmBAuto2.grid(row=1, column=0, padx=10, pady=1, sticky="w")


frmBAutoPneumToRotaryCnvyr = ctk.CTkFrame(frmBAuto2, fg_color="white")
frmBAutoPneumToRotaryCnvyr.grid(row=0, column=0, padx=1, pady=1)

imageBAutoPneumToRotaryCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PneumToRotaryCnvyr5Col.png'))
imageBAutoPneumToRotaryCnvyr = ctk.CTkImage(light_image=imageBAutoPneumToRotaryCnvyr, size=(400, 20)) 
BAutoPneumToRotaryCnvyrLbl = ctk.CTkLabel(frmBAutoPneumToRotaryCnvyr, image=imageBAutoPneumToRotaryCnvyr, text="")
BAutoPneumToRotaryCnvyrLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
btnBAutoPneumToRotaryCnvyr0DoClose = ctk.CTkButton(frmBAutoPneumToRotaryCnvyr, text="Close 5", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToRotaryCnvyr0DoClose.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumToRotaryCnvyr1DoClose = ctk.CTkButton(frmBAutoPneumToRotaryCnvyr, text="Close 4", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToRotaryCnvyr1DoClose.grid(row=1, column=1, padx=1, pady=1)
btnBAutoPneumToRotaryCnvyr2DoClose = ctk.CTkButton(frmBAutoPneumToRotaryCnvyr, text="Close 3", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToRotaryCnvyr2DoClose.grid(row=1, column=2, padx=1, pady=1)
btnBAutoPneumToRotaryCnvyr3DoClose = ctk.CTkButton(frmBAutoPneumToRotaryCnvyr, text="Close 2", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToRotaryCnvyr3DoClose.grid(row=1, column=3, padx=1, pady=1)
btnBAutoPneumToRotaryCnvyr4DoClose = ctk.CTkButton(frmBAutoPneumToRotaryCnvyr, text="Close 1", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToRotaryCnvyr4DoClose.grid(row=1, column=4, padx=1, pady=1)

frmBAutoSensorRtaryUnitHop = ctk.CTkFrame(frmBAuto2, fg_color="white")
frmBAutoSensorRtaryUnitHop.grid(row=0, column=1, padx=1, pady=1)

imageBAutoSensorRtaryUnitHop = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SensorRtaryUnitHop.png'))
imageBAutoSensorRtaryUnitHop = ctk.CTkImage(light_image=imageBAutoSensorRtaryUnitHop, size=(400, 20)) 
BAutoSensorRtaryUnitHopLbl = ctk.CTkLabel(frmBAutoSensorRtaryUnitHop, image=imageBAutoSensorRtaryUnitHop, text="")
BAutoSensorRtaryUnitHopLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
btnBAutoPneumSensorRtaryUnitHop0IsOn = ctk.CTkButton(frmBAutoSensorRtaryUnitHop, text="Sensor 5", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRtaryUnitHop0IsOn.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumSensorRtaryUnitHop1IsOn = ctk.CTkButton(frmBAutoSensorRtaryUnitHop, text="Sensor 4", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRtaryUnitHop1IsOn.grid(row=1, column=1, padx=1, pady=1)
btnBAutoPneumSensorRtaryUnitHop2IsOn = ctk.CTkButton(frmBAutoSensorRtaryUnitHop, text="Sensor 3", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRtaryUnitHop2IsOn.grid(row=1, column=2, padx=1, pady=1)
btnBAutoPneumSensorRtaryUnitHop3IsOn = ctk.CTkButton(frmBAutoSensorRtaryUnitHop, text="Sensor 2", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRtaryUnitHop3IsOn.grid(row=1, column=3, padx=1, pady=1)
btnBAutoPneumSensorRtaryUnitHop4IsOn = ctk.CTkButton(frmBAutoSensorRtaryUnitHop, text="Sensor 1", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRtaryUnitHop4IsOn.grid(row=1, column=4, padx=1, pady=1)
# ------------

frmBAuto3 = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="white")
# frmBAuto3.pack(padx=5, pady=(1, 1))
frmBAuto3.grid(row=2, column=0, padx=10, pady=1, sticky="w")
# ------------


frmBAutoMotorFrmRtaryCnvyr = ctk.CTkFrame(frmBAuto3, fg_color="white")
frmBAutoMotorFrmRtaryCnvyr.grid(row=0, column=1, padx=1, pady=1)

imageBAutoMotorFrmRtaryCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorFrmRtaryCnvyr.png'))
imageBAutoMotorFrmRtaryCnvyr = ctk.CTkImage(light_image=imageBAutoMotorFrmRtaryCnvyr, size=(160, 20)) 
BAutoMotorFrmRtaryCnvyrLbl = ctk.CTkLabel(frmBAutoMotorFrmRtaryCnvyr, image=imageBAutoMotorFrmRtaryCnvyr, text="")
BAutoMotorFrmRtaryCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnBAutoMotorFrmRtaryCnvyrDoStart = ctk.CTkButton(frmBAutoMotorFrmRtaryCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorFrmRtaryCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorFrmRtaryCnvyrIsFault = ctk.CTkButton(frmBAutoMotorFrmRtaryCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorFrmRtaryCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

frmBAutoMotorUpladderCnvyr = ctk.CTkFrame(frmBAuto3, fg_color="white")
frmBAutoMotorUpladderCnvyr.grid(row=0, column=2, padx=1, pady=1)

imageBAutoMotorUpladderCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorUpladderCnvyr.png'))
imageBAutoMotorUpladderCnvyr = ctk.CTkImage(light_image=imageBAutoMotorUpladderCnvyr, size=(160, 20)) 
BAutoMotorUpladderCnvyrLbl = ctk.CTkLabel(frmBAutoMotorUpladderCnvyr, image=imageBAutoMotorUpladderCnvyr, text="")
BAutoMotorUpladderCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnBAutoMotorUpladderCnvyrDoStart = ctk.CTkButton(frmBAutoMotorUpladderCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorUpladderCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorUpladderCnvyrIsFault = ctk.CTkButton(frmBAutoMotorUpladderCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorUpladderCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

frmBAutoMotorToHopperCnvyr = ctk.CTkFrame(frmBAuto3, fg_color="white")
frmBAutoMotorToHopperCnvyr.grid(row=0, column=3, padx=1, pady=1)

imageBAutoMotorToHopperCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorToHopperCnvyr.png'))
imageBAutoMotorToHopperCnvyr = ctk.CTkImage(light_image=imageBAutoMotorToHopperCnvyr, size=(160, 20)) 
BAutoMotorToHopperCnvyrLbl = ctk.CTkLabel(frmBAutoMotorToHopperCnvyr, image=imageBAutoMotorToHopperCnvyr, text="")
BAutoMotorToHopperCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnBAutoMotorToHopperCnvyrDoStart = ctk.CTkButton(frmBAutoMotorToHopperCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorToHopperCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorToHopperCnvyrIsFault = ctk.CTkButton(frmBAutoMotorToHopperCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorToHopperCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

# ------------

frmBAuto4 = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="white")
# frmBAuto4.pack(padx=5, pady=(1, 1))
frmBAuto4.grid(row=3, column=0, padx=10, pady=1, sticky="w")
# ------------


frmBAutoPneumToHopperCnvyr = ctk.CTkFrame(frmBAuto4, fg_color="white")
frmBAutoPneumToHopperCnvyr.grid(row=0, column=1, padx=1, pady=1)

imageBAutoPneumToHopperCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PneumToHopperCnvyr5Col.png'))
imageBAutoPneumToHopperCnvyr = ctk.CTkImage(light_image=imageBAutoPneumToHopperCnvyr, size=(320, 20)) 
BAutoPneumToHopperCnvyrLbl = ctk.CTkLabel(frmBAutoPneumToHopperCnvyr, image=imageBAutoPneumToHopperCnvyr, text="")
BAutoPneumToHopperCnvyrLbl.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
btnBAutoPneumToHopperCnvyr0DoClose = ctk.CTkButton(frmBAutoPneumToHopperCnvyr, text="Close 0", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToHopperCnvyr0DoClose.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumToHopperCnvyr1DoClose = ctk.CTkButton(frmBAutoPneumToHopperCnvyr, text="Close 1", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToHopperCnvyr1DoClose.grid(row=1, column=1, padx=1, pady=1)
btnBAutoPneumToHopperCnvyr2DoClose = ctk.CTkButton(frmBAutoPneumToHopperCnvyr, text="Close 2", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToHopperCnvyr2DoClose.grid(row=1, column=2, padx=1, pady=1)
btnBAutoPneumToHopperCnvyr3DoClose = ctk.CTkButton(frmBAutoPneumToHopperCnvyr, text="Close 3", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToHopperCnvyr3DoClose.grid(row=1, column=3, padx=1, pady=1)

frmBAutoSensorTabletVaryHop = ctk.CTkFrame(frmBAuto4, fg_color="white")
frmBAutoSensorTabletVaryHop.grid(row=0, column=2, padx=1, pady=1)

imageBAutoSensorTabletVaryHop = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SensorTabletVaryHop.png'))
imageBAutoSensorTabletVaryHop = ctk.CTkImage(light_image=imageBAutoSensorTabletVaryHop, size=(320, 20)) 
BAutoSensorTabletVaryHopLbl = ctk.CTkLabel(frmBAutoSensorTabletVaryHop, image=imageBAutoSensorTabletVaryHop, text="")
BAutoSensorTabletVaryHopLbl.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
btnBAutoPneumSensorTabletVaryHop0IsOn = ctk.CTkButton(frmBAutoSensorTabletVaryHop, text="Sensor 0", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorTabletVaryHop0IsOn.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumSensorTabletVaryHop1IsOn = ctk.CTkButton(frmBAutoSensorTabletVaryHop, text="Sensor 1", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorTabletVaryHop1IsOn.grid(row=1, column=1, padx=1, pady=1)
btnBAutoPneumSensorTabletVaryHop2IsOn = ctk.CTkButton(frmBAutoSensorTabletVaryHop, text="Sensor 2", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorTabletVaryHop2IsOn.grid(row=1, column=2, padx=1, pady=1)
btnBAutoPneumSensorTabletVaryHop3IsOn = ctk.CTkButton(frmBAutoSensorTabletVaryHop, text="Sensor 3", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorTabletVaryHop3IsOn.grid(row=1, column=3, padx=1, pady=1)
# ------------
frmBAuto5 = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="white")
# frmBAuto5.pack(padx=5, pady=(1, 1))
frmBAuto5.grid(row=5, column=0, padx=10, pady=1, sticky="w")
# ------------
frmBAutoPneumTbletHoprDoor = ctk.CTkFrame(frmBAuto5, fg_color="white")
frmBAutoPneumTbletHoprDoor.grid(row=0, column=0, padx=1, pady=1)

imageBAutoPneumTbletHoprDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PneumTbletHoprDoor.png'))
imageBAutoPneumTbletHoprDoor = ctk.CTkImage(light_image=imageBAutoPneumTbletHoprDoor, size=(480, 20)) 
BAutoPneumTbletHoprDoorLbl = ctk.CTkLabel(frmBAutoPneumTbletHoprDoor, image=imageBAutoPneumTbletHoprDoor, text="")
BAutoPneumTbletHoprDoorLbl.grid(row=0, column=0, columnspan=6, padx=1, pady=1)
btnBAutoPneumTbletHoprDoor0IsOpen = ctk.CTkButton(frmBAutoPneumTbletHoprDoor, text="Open 0", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumTbletHoprDoor0IsOpen.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumTbletHoprDoor0IsClose = ctk.CTkButton(frmBAutoPneumTbletHoprDoor, text="Close 0", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumTbletHoprDoor0IsClose.grid(row=1, column=1, padx=1, pady=1)
btnBAutoPneumTbletHoprDoor0IsFault = ctk.CTkButton(frmBAutoPneumTbletHoprDoor, text="Fault 0", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumTbletHoprDoor0IsFault.grid(row=1, column=2, padx=1, pady=1)
btnBAutoPneumTbletHoprDoor1IsOpen = ctk.CTkButton(frmBAutoPneumTbletHoprDoor, text="Open 1", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumTbletHoprDoor1IsOpen.grid(row=1, column=3, padx=1, pady=1)
btnBAutoPneumTbletHoprDoor1IsClose = ctk.CTkButton(frmBAutoPneumTbletHoprDoor, text="Close 1", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumTbletHoprDoor1IsClose.grid(row=1, column=4, padx=1, pady=1)
btnBAutoPneumTbletHoprDoor1IsFault = ctk.CTkButton(frmBAutoPneumTbletHoprDoor, text="Fault 1", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumTbletHoprDoor1IsFault.grid(row=1, column=5, padx=1, pady=1)

frmBAutoMotorTbletHoprDoor = ctk.CTkFrame(frmBAuto5, fg_color="white")
frmBAutoMotorTbletHoprDoor.grid(row=0, column=1, padx=1, pady=1)

imageBAutoMotorTbletHoprDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorTbletHoprDoor.png'))
imageBAutoMotorTbletHoprDoor = ctk.CTkImage(light_image=imageBAutoMotorTbletHoprDoor, size=(160, 20)) 
BAutoMotorTbletHoprDoorLbl = ctk.CTkLabel(frmBAutoMotorTbletHoprDoor, image=imageBAutoMotorTbletHoprDoor, text="")
BAutoMotorTbletHoprDoorLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnBAutoMotorTbletHoprDoorDoStart = ctk.CTkButton(frmBAutoMotorTbletHoprDoor, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorTbletHoprDoorDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorTbletHoprDoorIsFault = ctk.CTkButton(frmBAutoMotorTbletHoprDoor, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorTbletHoprDoorIsFault.grid(row=1, column=1, padx=1, pady=1)

frmBAutoMotorToRncenCnvyr = ctk.CTkFrame(frmBAuto5, fg_color="white")
frmBAutoMotorToRncenCnvyr.grid(row=0, column=2, padx=1, pady=1)

imageBAutoMotorToRncenCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorToRncenCnvyr.png'))
imageBAutoMotorToRncenCnvyr = ctk.CTkImage(light_image=imageBAutoMotorToRncenCnvyr, size=(160, 20)) 
BAutoMotorToRncenCnvyrLbl = ctk.CTkLabel(frmBAutoMotorToRncenCnvyr, image=imageBAutoMotorToRncenCnvyr, text="")
BAutoMotorToRncenCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnBAutoMotorToRncenCnvyrDoStart = ctk.CTkButton(frmBAutoMotorToRncenCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorToRncenCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnBAutoMotorToRncenCnvyrIsFault = ctk.CTkButton(frmBAutoMotorToRncenCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoMotorToRncenCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)
# ------------
frmBAuto6 = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="white")
# frmBAuto6.pack(padx=5, pady=(1, 1))
frmBAuto6.grid(row=7, column=0, padx=10, pady=1, sticky="w")
# ------------
frmBAutoPneumToRncenCnvyr = ctk.CTkFrame(frmBAuto6, fg_color="white")
frmBAutoPneumToRncenCnvyr.grid(row=0, column=0, padx=1, pady=1)

imageBAutoPneumToRncenCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','PneumToRncenCnvyr.png'))
imageBAutoPneumToRncenCnvyr = ctk.CTkImage(light_image=imageBAutoPneumToRncenCnvyr, size=(160, 20)) 
BAutoPneumToRncenCnvyrLbl = ctk.CTkLabel(frmBAutoPneumToRncenCnvyr, image=imageBAutoPneumToRncenCnvyr, text="")
BAutoPneumToRncenCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
# btnBAutoPneumToRncenCnvyrDoOpen = ctk.CTkButton(frmBAutoPneumToRncenCnvyr, text="DoOpen", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
# btnBAutoPneumToRncenCnvyrDoOpen.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumToRncenCnvyrDoClose = ctk.CTkButton(frmBAutoPneumToRncenCnvyr, text="Close", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumToRncenCnvyrDoClose.grid(row=1, column=1, padx=1, pady=1)

frmBAutoSensorRncenMachHop = ctk.CTkFrame(frmBAuto6, fg_color="white")
frmBAutoSensorRncenMachHop.grid(row=0, column=1, padx=1, pady=1)

imageBAutoSensorRncenMachHop = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SensorRncenMachHop.png'))
imageBAutoSensorRncenMachHop = ctk.CTkImage(light_image=imageBAutoSensorRncenMachHop, size=(160, 20)) 
BAutoSensorRncenMachHopLbl = ctk.CTkLabel(frmBAutoSensorRncenMachHop, image=imageBAutoSensorRncenMachHop, text="")
BAutoSensorRncenMachHopLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnBAutoPneumSensorRncenMachHop0IsOn = ctk.CTkButton(frmBAutoSensorRncenMachHop, text="Sensor 0", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRncenMachHop0IsOn.grid(row=1, column=0, padx=1, pady=1)
btnBAutoPneumSensorRncenMachHop1IsOn = ctk.CTkButton(frmBAutoSensorRncenMachHop, text="Sensor 1", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnBAutoPneumSensorRncenMachHop1IsOn.grid(row=1, column=1, padx=1, pady=1)

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabBesarBAuto, fg_color="transparent")
frm_MenuBawah.grid(row=8, column=0, padx=(0,1), pady=(193,0), sticky="ew")

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="blue", text_color="white",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1, state="normal")
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                        border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU





# ================================================================================
# LINE B - UI UX - AUTO 2/2 - .bauto2
# ================================================================================

img = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'AutoB22.png'))  # Ganti dengan path gambar yang ingin kamu gunakan
resized_img = img.resize((1000, 320))  # Atur ukuran sesuai kebutuhan

# Konversi gambar agar bisa digunakan dalam tkinter
ctk_imageAutoB = ctk.CTkImage(resized_img, size=(1000, 320))

frame_tabAutoLineB22 = ctk.CTkFrame(app, fg_color="white")
frame_tabAutoLineB22.pack(fill="both", expand=True)

# START MatCol
frm_MatCol = ctk.CTkFrame(frame_tabAutoLineB22, fg_color="white")
frm_MatCol.grid(row=0, column=0, padx=1, pady=1)

lbl_MatCol = ctk.CTkLabel(frm_MatCol, text="Material Color", font=('Helvetica', 16))
lbl_MatCol.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarna = ctk.CTkFrame(frm_MatCol)
frm_BtnWarna.grid(row=1, column=0, columnspan=5, pady=1)

btnAutoFeedPutih = ctk.CTkButton(frm_BtnWarna, text="Putih", fg_color="lime", text_color="black", border_color="black", border_width=5,
                                    command=cmdBtnFeederBPutih, height=btnSize)
btnAutoFeedPutih.grid(row=1, column=0, padx=5, pady=(10, 10))
# if globals()['V0144'] == 32768:
# else:
    # btnAutoFeedPutih = ctk.CTkButton(frm_BtnWarna, text="Putih", fg_color="light green", text_color="white", border_color="black", border_width=5,
    #                                 command=cmdBtnFeederBPutih, height=btnSize)
    # btnAutoFeedPutih.grid(row=1, column=0, padx=5, pady=(10, 10))

btnAutoFeedWarna1 = ctk.CTkButton(frm_BtnWarna, text="Warna 1", fg_color="red", text_color="black", border_color="black", border_width=5,
                                    command=cmdBtnFeederBWarna1, height=btnSize)
btnAutoFeedWarna1.grid(row=1, column=1, padx=5, pady=(10, 10))
# if globals()['V0144'] == 16384:
# else:
#     btnAutoFeedWarna1 = ctk.CTkButton(frm_BtnWarna, text="Warna 1", fg_color="pink",text_color="white", border_color="black", border_width=5,
#                                      command=cmdBtnFeederBWarna1, height=btnSize)
#     btnAutoFeedWarna1.grid(row=1, column=1, padx=5, pady=(10, 10))

btnAutoFeedWarna2 = ctk.CTkButton(frm_BtnWarna, text="Warna 2", fg_color="red", text_color="black", border_color="black", border_width=5,
                                    command=cmdBtnFeederBWarna2, height=btnSize)
btnAutoFeedWarna2.grid(row=1, column=2, padx=5, pady=(10, 10))
# if globals()['V0144'] == 8192:
# else:
#     btnAutoFeedWarna2 = ctk.CTkButton(frm_BtnWarna, text="Warna 2", fg_color="pink", text_color="white", border_color="black", border_width=5,
#                                     command=cmdBtnFeederBWarna2, height=btnSize)
#     btnAutoFeedWarna2.grid(row=1, column=2, padx=5, pady=(10, 10))

btnAutoFeedWarna3 = ctk.CTkButton(frm_BtnWarna, text="Warna 3", fg_color="red", text_color="black", border_color="black", border_width=5,
                                    command=cmdBtnFeederBWarna3, height=btnSize)
btnAutoFeedWarna3.grid(row=1, column=3, padx=5, pady=(10, 10))
# if globals()['V0144'] == 4096:
# else:
#     btnAutoFeedWarna3 = ctk.CTkButton(frm_BtnWarna, text="Warna 3", fg_color="pink", text_color="white", border_color="black", border_width=5,
#                                   command=cmdBtnFeederBWarna3, height=btnSize)
#     btnAutoFeedWarna3.grid(row=1, column=3, padx=5, pady=(10, 10))


btnManFeedManual = ctk.CTkButton(frm_MatCol, text="Manual", fg_color="red", text_color="black", border_color="black", border_width=5,
                                 command=cmdBtnFeederManual, height=btnSize)
btnManFeedManual.grid(row=1, column=5, padx=20, pady=(10, 10))
# END MatCol
# START ProdType
frm_ProdType = ctk.CTkFrame(frame_tabAutoLineB22, fg_color="white")
frm_ProdType.grid(row=1, column=0, padx=1, pady=1)

lbl_ProdType = ctk.CTkLabel(frm_ProdType, text="Product Type", font=('Helvetica', 16))
lbl_ProdType.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarna = ctk.CTkFrame(frm_ProdType)
frm_BtnWarna.grid(row=1, column=0, columnspan=5, pady=1)


btnAutoHopperPutih = ctk.CTkButton(frm_BtnWarna, text="Putih", fg_color="lime", text_color="black", border_color="black", border_width=5,
                                   command=cmdBtnHopperBPutih, height=btnSize)
btnAutoHopperPutih.grid(row=1, column=0, padx=5, pady=(10, 10))
# if globals()['V0145'] == 2048:
# else:
#     btnAutoHopperPutih = ctk.CTkButton(frm_BtnWarna, text="Putih", fg_color="light green", text_color="white", border_color="black", border_width=5,
#                                     command=cmdBtnHopperBPutih, height=btnSize)
#     btnAutoHopperPutih.grid(row=1, column=0, padx=5, pady=(10, 10))

btnAutoHopperWarna1 = ctk.CTkButton(frm_BtnWarna, text="Warna", fg_color="red", text_color="black", border_color="black", border_width=5,
                                       command=cmdBtnHopperBWarna, height=btnSize)
btnAutoHopperWarna1.grid(row=1, column=1, padx=5, pady=(10, 10))
# if globals()['V0145'] == 1024:
# else:
#     btnAutoHopperWarna1 = ctk.CTkButton(frm_BtnWarna, text="Warna", fg_color="pink", text_color="white", border_color="black", border_width=5,
#                                         command=cmdBtnHopperBWarna, height=btnSize)
#     btnAutoHopperWarna1.grid(row=1, column=1, padx=5, pady=(10, 10))

btnManHopperManual = ctk.CTkButton(frm_ProdType, text="Manual", fg_color="red", text_color="black", border_color="black", border_width=5,
                                command=cmdBtnFeederManual, height=btnSize)
btnManHopperManual.grid(row=1, column=5, padx=20, pady=(10, 10))
# END ProdType

frm_BesarC3LineBawah = ctk.CTkFrame(frame_tabAutoLineB22, fg_color="white")
frm_BesarC3LineBawah.grid(row=2, column=0, padx=10, pady=1)

label_with_image = ctk.CTkLabel(frm_BesarC3LineBawah, image=ctk_imageAutoB, text="")  # Kosongkan teks agar hanya gambar yang tampil
label_with_image.pack(pady=5)


# Membuat frame untuk border
frame_with_border22 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border22.grid(row=0, column=0, columnspan=6, padx=(940,0), pady=(1, 420))

lbl_ProdType = ctk.CTkLabel(frame_with_border22, text="Silo Door 2", font=('Inter', 7))
lbl_ProdType.grid(row=0, column=0, padx=2, pady=2)

frame_with_border223 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border223.grid(row=0, column=0,columnspan=6, padx=(800,0), pady=(1, 420))

lbl_ProdTypez = ctk.CTkLabel(frame_with_border223, text="Silo Door 1", font=('Inter', 7))
lbl_ProdTypez.grid(row=0, column=0, padx=2, pady=2)
# kanan
btnBolaC1C32 = ctk.CTkButton(label_with_image, text="Open", fg_color="red", text_color="black",
                          border_color="grey", border_width=5, width=40, height=15)
btnBolaC1C32.grid(row=0, column=0, padx=(940,0), pady=(1, 340))
# kiri
btnBolaC1C33 = ctk.CTkButton(label_with_image, text="Open", fg_color="red", text_color="black",
                          border_color="grey", border_width=5, width=40, height=15)
btnBolaC1C33.grid(row=0, column=0, padx=(800,0), pady=(1, 340))

frame_with_border222 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border222.grid(row=0, column=0, padx=(860,0), pady=(1, 80))

lbl_ToHopperCnvyr = ctk.CTkLabel(frame_with_border222, text="Conveyor ToSilo", font=('Helvetica', 7))
lbl_ToHopperCnvyr.grid(row=0, column=0, padx=2, pady=2)

frame_with_border2234 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border2234.grid(row=0, column=0, padx=(860,0), pady=(1, 210))

lbl_TbltHoprDoor = ctk.CTkLabel(frame_with_border2234, text="Tablet Silo Door", font=('Helvetica', 7))
lbl_TbltHoprDoor.grid(row=0, column=0,padx=2, pady=2)

frame_with_border21 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border21.grid(row=0, column=0, padx=(640,0), pady=(1, 380))

lbl_ToHopperCnvyr0 = ctk.CTkLabel(frame_with_border21, text="Door Silo 4", font=('Helvetica', 7))
lbl_ToHopperCnvyr0.grid(row=0, column=0, padx=2, pady=2)

frame_with_border20 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border20.grid(row=0, column=0, padx=(510,0), pady=(1, 380))

lbl_TbltHoprCnvyr1 = ctk.CTkLabel(frame_with_border20, text="Door Silo 3", font=('Helvetica', 7))
lbl_TbltHoprCnvyr1.grid(row=0, column=0,padx=2, pady=2)

frame_with_border19 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border19.grid(row=0, column=0, padx=(380,0), pady=(1, 380))

lbl_ToHopperCnvyr2 = ctk.CTkLabel(frame_with_border19, text="Door Silo 2", font=('Helvetica', 7))
lbl_ToHopperCnvyr2.grid(row=0, column=0, padx=2, pady=2)

frame_with_border18 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border18.grid(row=0, column=0, padx=(250,0), pady=(1, 380))

lbl_TbltHoprCnvyr3 = ctk.CTkLabel(frame_with_border18, text="Door Silo 1", font=('Helvetica', 7))
lbl_TbltHoprCnvyr3.grid(row=0, column=0,padx=2, pady=2)

btnTbltHoprDoor0 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor0.grid(row=0, column=0, padx=(640,0), pady=(1, 310))

btnTbltHoprDoor1 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor1.grid(row=0, column=0, padx=(510,0), pady=(1, 310))

btnTbltHoprDoor2 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor2.grid(row=0, column=0, padx=(380,0), pady=(1, 310))

btnTbltHoprDoor3 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor3.grid(row=0, column=0, padx=(250,0), pady=(1, 310))

frame_with_border17 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border17.grid(row=0, column=0, padx=(640,0), pady=(1, 240))

lbl_TbltVaryHop0 = ctk.CTkLabel(frame_with_border17, text="Sensor\nSilo 4", font=('Helvetica', 7))
lbl_TbltVaryHop0.grid(row=0, column=0, padx=3, pady=2)

frame_with_border16 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border16.grid(row=0, column=0, padx=(510,0), pady=(1, 240))

lbl_TbltVaryHop1 = ctk.CTkLabel(frame_with_border16, text="Sensor\nSilo 3", font=('Helvetica', 7))
lbl_TbltVaryHop1.grid(row=0, column=0,padx=3, pady=2)

frame_with_border15 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border15.grid(row=0, column=0, padx=(380,0), pady=(1, 240))

lbl_TbltVaryHop2 = ctk.CTkLabel(frame_with_border15, text="Sensor\nSilo 2", font=('Helvetica', 7))
lbl_TbltVaryHop2.grid(row=0, column=0, padx=3, pady=2)

frame_with_border14 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border14.grid(row=0, column=0, padx=(250,0), pady=(1, 240))

lbl_TbltVaryHop3 = ctk.CTkLabel(frame_with_border14, text="Sensor\nSilo 1", font=('Helvetica', 7))
lbl_TbltVaryHop3.grid(row=0, column=0,padx=3, pady=2)

btnTbltVaryHop0 = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop0.grid(row=0, column=0, padx=(640,0), pady=(1, 170))

btnTbltVaryHop1 = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop1.grid(row=0, column=0, padx=(510,0), pady=(1, 170))

btnTbltVaryHop2 = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop2.grid(row=0, column=0, padx=(380,0), pady=(1, 170))

btnTbltVaryHop3 = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop3.grid(row=0, column=0, padx=(250,0), pady=(1, 170))

frame_with_border13 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border13.grid(row=0, column=0, padx=(330,0), pady=(1, 100))

lbl_UpLadderCnvyr = ctk.CTkLabel(frame_with_border13, text="Incline Conveyor", font=('Helvetica', 7))
lbl_UpLadderCnvyr.grid(row=0, column=0, padx=3, pady=2)

frame_with_border12 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border12.grid(row=0, column=0, padx=(120,0), pady=(1, 100))

lbl_FrmRtaryCnvyr = ctk.CTkLabel(frame_with_border12, text="Conveyor FromRotary", font=('Helvetica', 7))
lbl_FrmRtaryCnvyr.grid(row=0, column=0,padx=3, pady=2)

btnUpLadderCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnUpLadderCnvyr.grid(row=0, column=0, padx=(330,0), pady=(1, 30))

btnFrmRtaryCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnFrmRtaryCnvyr.grid(row=0, column=0, padx=(120,0), pady=(1, 30))

btnTbltHoprDoor = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor.grid(row=0, column=0, padx=(860,0), pady=(1, 145))

btnToHopperCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyr.grid(row=0, column=0, padx=(860,0), pady=(1, 10))

frame_with_border11 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border11.grid(row=0, column=0, padx=(510,0), pady=(50, 1))

lbl_TbltVaryHop1 = ctk.CTkLabel(frame_with_border11, text="Modular Conveyor", font=('Helvetica', 7))
lbl_TbltVaryHop1.grid(row=0, column=0,padx=3, pady=2)

frame_with_border10 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border10.grid(row=0, column=0, padx=(380,0), pady=(50, 1))

lbl_TbltVaryHop2 = ctk.CTkLabel(frame_with_border10, text="Modular\nCnvyr Door", font=('Helvetica', 7))
lbl_TbltVaryHop2.grid(row=0, column=0, padx=3, pady=2)

btnPneumToRncenCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnPneumToRncenCnvyr.grid(row=0, column=0, padx=(510,0), pady=(120, 1))

btnMotorToRncenCnvyr = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorToRncenCnvyr.grid(row=0, column=0, padx=(380,0), pady=(120, 1))

frame_with_border9 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border9.grid(row=0, column=0, padx=(510,0), pady=(190, 1))

lbl_TbltVaryHop1 = ctk.CTkLabel(frame_with_border9, text="Sensor\nRncenMachHop 0", font=('Helvetica', 7))
lbl_TbltVaryHop1.grid(row=0, column=0,padx=3, pady=2)

frame_with_border8 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border8.grid(row=0, column=0, padx=(380,0), pady=(190, 1))

lbl_TbltVaryHop2 = ctk.CTkLabel(frame_with_border8, text="Sensor\nRncenMachHop 1", font=('Helvetica', 7))
lbl_TbltVaryHop2.grid(row=0, column=0, padx=3, pady=2)

btnRncenMachHop0 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRncenMachHop0.grid(row=0, column=0, padx=(510,0), pady=(260, 1))

btnRncenMachHop1 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRncenMachHop1.grid(row=0, column=0, padx=(380,0), pady=(260, 1))

frame_with_border7 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border7.grid(row=0, column=0,padx=(230,0), pady=(140,1))

lbl_ToRotaryCnvyr0 = ctk.CTkLabel(frame_with_border7, text="Conveyor Door 5", font=('Helvetica', 7))
lbl_ToRotaryCnvyr0.grid(row=0, column=0,padx=3, pady=2)

frame_with_border6 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border6.grid(row=0, column=0, padx=(20,0), pady=(140,1))

lbl_ToRotaryCnvyr1 = ctk.CTkLabel(frame_with_border6, text="Conveyor Door 4", font=('Helvetica', 7))
lbl_ToRotaryCnvyr1.grid(row=0, column=0, padx=3, pady=2)

frame_with_border5 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border5.grid(row=0, column=0,padx=(0,170), pady=(140,1))

lbl_ToRotaryCnvyr2 = ctk.CTkLabel(frame_with_border5, text="Conveyor Door 3", font=('Helvetica', 7))
lbl_ToRotaryCnvyr2.grid(row=0, column=0,padx=3, pady=2)

frame_with_border4 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border4.grid(row=0, column=0, padx=(0,380), pady=(140,1))

lbl_ToRotaryCnvyr3 = ctk.CTkLabel(frame_with_border4, text="Conveyor Door 2", font=('Helvetica', 7))
lbl_ToRotaryCnvyr3.grid(row=0, column=0, padx=3, pady=2)

frame_with_border3 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border3.grid(row=0, column=0,padx=(0,580), pady=(140,1))

lbl_ToRotaryCnvyr4 = ctk.CTkLabel(frame_with_border3, text="Conveyor Door 1", font=('Helvetica', 7))
lbl_ToRotaryCnvyr4.grid(row=0, column=0,padx=3, pady=2)

btnToRotaryCnvyr0 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr0.grid(row=0, column=0, padx=(230,0), pady=(210,1))

btnToRotaryCnvyr1 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr1.grid(row=0, column=0,  padx=(20,0), pady=(210,1))

btnToRotaryCnvyr2 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr2.grid(row=0, column=0, padx=(0,170), pady=(210,1))

btnToRotaryCnvyr3 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr3.grid(row=0, column=0, padx=(0,380), pady=(210,1))

btnToRotaryCnvyr4 = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr4.grid(row=0, column=0, padx=(0,580), pady=(210,1))


frame_with_border77 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border77.grid(row=0, column=0,padx=(230,0), pady=(280,1))

lbl_RtaryUnitHop0 = ctk.CTkLabel(frame_with_border77, text="Hopper Rotary 5", font=('Helvetica', 7))
lbl_RtaryUnitHop0.grid(row=0, column=0,padx=3, pady=2)

frame_with_border66 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border66.grid(row=0, column=0, padx=(20,0), pady=(280,1))

lbl_RtaryUnitHop1 = ctk.CTkLabel(frame_with_border66, text="Hopper Rotary 4", font=('Helvetica', 7))
lbl_RtaryUnitHop1.grid(row=0, column=0, padx=3, pady=2)

frame_with_border55 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border55.grid(row=0, column=0,padx=(0,170), pady=(280,1))

lbl_RtaryUnitHop2 = ctk.CTkLabel(frame_with_border55, text="Hopper Rotary 3", font=('Helvetica', 7))
lbl_RtaryUnitHop2.grid(row=0, column=0,padx=3, pady=2)

frame_with_border44 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border44.grid(row=0, column=0, padx=(0,380), pady=(280,1))

lbl_RtaryUnitHop3 = ctk.CTkLabel(frame_with_border44, text="Hopper Rotary 2", font=('Helvetica', 7))
lbl_RtaryUnitHop3.grid(row=0, column=0, padx=3, pady=2)

frame_with_border33 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border33.grid(row=0, column=0,padx=(0,580), pady=(280,1))

lbl_RtaryUnitHop4 = ctk.CTkLabel(frame_with_border33, text="Hopper Rotary 1", font=('Helvetica', 7))
lbl_RtaryUnitHop4.grid(row=0, column=0,padx=3, pady=2)

btnRtaryUnitHop0 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop0.grid(row=0, column=0, padx=(230,0), pady=(350,1))

btnRtaryUnitHop1 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop1.grid(row=0, column=0,  padx=(20,0), pady=(350,1))

btnRtaryUnitHop2 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop2.grid(row=0, column=0, padx=(0,170), pady=(350,1))

btnRtaryUnitHop3 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop3.grid(row=0, column=0, padx=(0,380), pady=(350,1))

btnRtaryUnitHop4 = ctk.CTkButton(label_with_image, text="Sensor", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop4.grid(row=0, column=0, padx=(0,580), pady=(350,1))


frame_with_border00 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border00.grid(row=0, column=0, padx=(0,480), pady=(10,1))

lbl_ToRotaryCnvyr1 = ctk.CTkLabel(frame_with_border00, text="Conveyor ToRotary", font=('Helvetica', 7))
lbl_ToRotaryCnvyr1.grid(row=0, column=0, padx=3, pady=2)

frame_with_border312 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border312.grid(row=0, column=0,padx=(0,770), pady=(10,1))

lbl_MatScrewCnvyr1 = ctk.CTkLabel(frame_with_border312, text="Motor Screw", font=('Helvetica', 7))
lbl_MatScrewCnvyr1.grid(row=0, column=0,padx=3, pady=2)

btnMotorToRotaryCnvyr = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorToRotaryCnvyr.grid(row=0, column=0, padx=(0,480), pady=(80,1))

btnMotorMatScrewCnvyr = ctk.CTkButton(label_with_image, text="Rev", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorMatScrewCnvyr.grid(row=0, column=0, padx=(0,770), pady=(80,1))



frame_with_border4p = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border4p.grid(row=0, column=0,padx=(0,950), pady=(10,1))

lbl_MateriVbrator = ctk.CTkLabel(frame_with_border4p, text="Motor Osciliating", font=('Helvetica', 7))
lbl_MateriVbrator.grid(row=0, column=0,padx=3, pady=2)



btnMateriVbrator = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMateriVbrator.grid(row=0, column=0, padx=(0,950), pady=(80,1))




# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabAutoLineB22, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=(0,1), pady=(45,0), sticky="ew")

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="blue", text_color="white",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2, state="normal")
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU









# ================================================================================
# LINE B - UI UX - SET B - .bset
# ================================================================================

frame_SetAutoB = ctk.CTkFrame(app, fg_color="white")
frame_SetAutoB.pack(fill="both", expand=True)

main_frame = ctk.CTkFrame(frame_SetAutoB, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=10, pady=0)

# Frame container untuk area di sebelah kiri
area_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
area_frame.pack(side="left", anchor="nw", padx=10, pady=0)

# Membuat frame container untuk area baris pertama (judul 1-4)
row1_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row1_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris pertama secara horizontal

# Membuat area frame untuk judul 1-4 di baris pertama
create_area_frame(row1_frame, "Pneum MaterMixDoor", "V0000")
create_area_frame(row1_frame, "Pneum TbletHoprDoor 0", "V0001")
create_area_frame(row1_frame, "Pneum TbletHoprDoor 1", "V0002")
create_area_frame(row1_frame, "Sensor RtaryUnitHop 0", "V0016")

# Membuat frame container untuk area baris kedua (judul 5-8)
row2_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row2_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris kedua di bawah baris pertama

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row2_frame, "Sensor RtaryUnitHop 1", "V0017")
create_area_frame(row2_frame, "Sensor RtaryUnitHop 2", "V0018")
create_area_frame(row2_frame, "Sensor RtaryUnitHop 3", "V0019")
create_area_frame(row2_frame, "Sensor RtaryUnitHop 4", "V0020")

# Membuat frame container untuk area baris kedua (judul 5-8)
row3_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row3_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris kedua di bawah baris pertama

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row3_frame, "Sensor TabletVaryHop 0", "V0021")
create_area_frame(row3_frame, "Sensor TabletVaryHop 1", "V0022")
create_area_frame(row3_frame, "Sensor TabletVaryHop 2", "V0023")
create_area_frame(row3_frame, "Sensor TabletVaryHop 3", "V0024")

# Membuat frame container untuk area baris kedua (judul 5-8)
row4_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row4_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris kedua di bawah baris pertama

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row4_frame, "Sensor RncenMachHop 0", "V0025")
create_area_frame(row4_frame, "Sensor RncenMachHop 1", "V0026")

row5_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row5_frame.pack(side="top", anchor="se", pady=0)

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row5_frame, "Mixing", "V0011")

# Frame untuk kalkulator di sebelah kanan
calculator_frame = ctk.CTkFrame(main_frame, width=330, height=410, corner_radius=10, fg_color="gray")
calculator_frame.pack(side="right", anchor="ne", padx=10, pady=120)

# Baris pertama: /, *, -, <-
row1_buttons = ["/", "*", "-", "←"]
for i, text in enumerate(row1_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=0, column=i, padx=7.5, pady=7.5, sticky="nsew")  # Menggunakan grid untuk penempatan

# Baris kedua: 7, 8, 9, +
row2_buttons = ["7", "8", "9"]
for i, text in enumerate(row2_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=1, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Tombol + yang menggabungkan baris kedua dan ketiga
button_plus = ctk.CTkButton(calculator_frame, text="+", command=lambda: on_calculator_button_click("+"), width=60, height=125, fg_color="white", text_color="black", font=("Helvetica", 24))
button_plus.grid(row=1, column=3, rowspan=2, padx=7.5, pady=7.5, sticky="nsew")

# Baris ketiga: 4, 5, 6
row3_buttons = ["4", "5", "6"]
for i, text in enumerate(row3_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=2, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Baris keempat: 1, 2, 3
row4_buttons = ["1", "2", "3"]
for i, text in enumerate(row4_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=3, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Menggabungkan tombol Backspace ke baris keempat dan kelima
button_backspace = ctk.CTkButton(calculator_frame, text="↵", command=lambda: on_calculator_button_click("↵"), width=60, height=125, fg_color="white", text_color="black", font=("Helvetica", 24))
button_backspace.grid(row=3, column=3, rowspan=2, padx=7.5, pady=7.5, sticky="nsew")

# Baris kelima: 0, .
button_zero = ctk.CTkButton(calculator_frame, text="0", command=lambda: on_calculator_button_click("0"), width=125, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
button_zero.grid(row=4, column=0, columnspan=2, padx=7.5, pady=7.5, sticky="nsew")

button_dot = ctk.CTkButton(calculator_frame, text=".", command=lambda: on_calculator_button_click("."), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 44))
button_dot.grid(row=4, column=2, padx=7.5, pady=7.5, sticky="nsew")


# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_SetAutoB, fg_color="transparent")
frm_MenuBawah.pack(side="bottom", anchor="s", fill="x", pady=0)

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB, state="normal")
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU
















# ================================================================================
# LINE C - UI UX - MANUAL 1/3 - .cman1
# ================================================================================

# -------------------------------------------------------------------------------------------------------------------------
frame_tabManualBola1 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualBola1.pack(fill="both", expand=True)
# START MatCol Line C
frm_MatColC = ctk.CTkFrame(frame_tabManualBola1, fg_color="white")
frm_MatColC.grid(row=0, column=0, padx=1, pady=1, sticky="w")

lbl_MatColC = ctk.CTkLabel(frm_MatColC, text="Material Color", font=('Helvetica', 16))
lbl_MatColC.grid(row=0, column=0, columnspan=7, pady=1)

frm_BtnWarnaC = ctk.CTkFrame(frm_MatColC)
frm_BtnWarnaC.grid(row=1, column=0, columnspan=6, pady=1)

if globals()['V0146'] == 512:
    btnAutoFeedPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="lime", text_color="black", border_color="black", border_width=5,
                                     height=btnSize)
    btnAutoFeedPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))
else:
    btnAutoFeedPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="light green", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnFeederCPutih, height=btnSize)
    btnAutoFeedPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))

if globals()['V0146'] == 256:
    btnAutoFeedWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="red", text_color="black", border_color="black", border_width=5,
                                     height=btnSize)
    btnAutoFeedWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))
else:
    btnAutoFeedWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                  command=cmdBtnFeederCWarna1, height=btnSize)
    btnAutoFeedWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))

if globals()['V0146'] == 128:
    btnAutoFeedWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="red", text_color="black", border_color="black", border_width=5,
                                    height=btnSize)
    btnAutoFeedWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))
else:
    btnAutoFeedWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnFeederCWarna2, height=btnSize)
    btnAutoFeedWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))

if globals()['V0146'] == 64:
    btnAutoFeedWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="red", text_color="black", border_color="black", border_width=5,
                                     height=btnSize)
    btnAutoFeedWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))
else:
    btnAutoFeedWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnFeederCWarna3, height=btnSize)
    btnAutoFeedWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))

if globals()['V0146'] == 32:
    btnAutoFeedWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="red", text_color="black", border_color="black", border_width=5,
                                     height=btnSize)
    btnAutoFeedWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))
else:
    btnAutoFeedWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnFeederCWarna4, height=btnSize)
    btnAutoFeedWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))

btnManFeedManualC = ctk.CTkButton(frm_MatColC, text="Auto", fg_color="red", border_color="black", border_width=5,
                                 command=showAutoBesarC2, height=btnSize)
btnManFeedManualC.grid(row=1, column=7, padx=20, pady=(10, 10))
# END MatCol
# START ProdType
frm_ProdTypeC = ctk.CTkFrame(frame_tabManualBola1, fg_color="white")
frm_ProdTypeC.grid(row=1, column=0, padx=1, pady=1, sticky="w")

lbl_ProdTypeC = ctk.CTkLabel(frm_ProdTypeC, text="Product Type", font=('Helvetica', 16))
lbl_ProdTypeC.grid(row=0, column=0, columnspan=7, pady=1)

frm_BtnWarnaC = ctk.CTkFrame(frm_ProdTypeC)
frm_BtnWarnaC.grid(row=1, column=0, columnspan=6, pady=1)

if globals()['V0147'] == 16:
    btnAutoHopperPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="lime", text_color="white", border_color="black", border_width=5,
                                     height=btnSize)
    btnAutoHopperPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))
else:
    btnAutoHopperPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="light green", border_color="black", border_width=5,
                                    command=cmdBtnHopperCPutih, height=btnSize)
    btnAutoHopperPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))

if globals()['V0147'] == 8:
    btnAutoHopperWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="red", text_color="black", border_color="black", border_width=5,
                                        height=btnSize)
    btnAutoHopperWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))
else:
    btnAutoHopperWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                        command=cmdBtnHopperCWarna1, height=btnSize)
    btnAutoHopperWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))

if globals()['V0147'] == 4:
    btnAutoHopperWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="red", text_color="black", border_color="black", border_width=5,
                                         height=btnSize)
    btnAutoHopperWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))
else:
    btnAutoHopperWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnHopperCWarna2, height=btnSize)
    btnAutoHopperWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))

if globals()['V0147'] == 2:
    btnAutoHopperWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="red", text_color="black", border_color="black", border_width=5,
                                         height=btnSize)
    btnAutoHopperWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))
else:
    btnAutoHopperWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                        command=cmdBtnHopperCWarna3, height=btnSize)
    btnAutoHopperWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))

if globals()['V0147'] == 1:
    btnAutoHopperWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="red", text_color="black", border_color="black", border_width=5,
                                         height=btnSize)
    btnAutoHopperWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))
else:
    btnAutoHopperWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                        command=cmdBtnHopperCWarna4, height=btnSize)
    btnAutoHopperWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))

btnManHopperManualC = ctk.CTkButton(frm_ProdTypeC, text="Auto", fg_color="red", border_color="black", border_width=5,
                                   command=showAutoBesarC2, height=btnSize)
btnManHopperManualC.grid(row=1, column=7, padx=20, pady=(10, 10))
# END ProdType
# START frm_BolaC1LineTengah
frm_BolaC1LineTengah = ctk.CTkFrame(frame_tabManualBola1, fg_color="white")
frm_BolaC1LineTengah.grid(row=2, column=0, padx=20, pady=1, sticky="w")

# ------------
# stateCManMateriVbrator = "up"

frmCManMateriVbrator = ctk.CTkFrame(frm_BolaC1LineTengah, fg_color="white")
frmCManMateriVbrator.grid(row=0, column=0, padx=30, pady=(0, 5))

frmCManMateriVbratorLbl = ctk.CTkFrame(frmCManMateriVbrator, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManMateriVbratorLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchCManMateriVbrator = ctk.CTkLabel(frmCManMateriVbratorLbl, text="Motor Osciliating", width=150)
lblSwitchCManMateriVbrator.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManMateriVbrator = ctk.CTkFrame(frmCManMateriVbrator, fg_color="transparent")
frmBtnCManMateriVbrator.grid(row=2, column=0, padx=1, pady=1)

# imgCManMateriVbratorUp = ImageTk.PhotoImage(switchUp)
# imgCManMateriVbratorLeft = ImageTk.PhotoImage(switchLeft)
# imgCManMateriVbratorRight = ImageTk.PhotoImage(switchRight)

# canvasCManMateriVbrator = ctk.CTkCanvas(frmBtnCManMateriVbrator, width=image_width, height=image_height, highlightthickness=0)
# canvasCManMateriVbrator.pack()
# imgCManMateriVbrator = canvasCManMateriVbrator.create_image(0, 0, anchor='nw', image=imgCManMateriVbratorUp)

# btnKiriCManMateriVbrator = canvasCManMateriVbrator.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManMateriVbrator = canvasCManMateriVbrator.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvasCManMateriVbrator.tag_bind(btnKananCManMateriVbrator, "<ButtonPress-1>", lambda event: changeCManMateriVbratorSwitch("right"))
# canvasCManMateriVbrator.tag_bind(btnKananCManMateriVbrator, "<ButtonRelease-1>", resetCManMateriVbratorSwicth)

imgCManMateriVbratorRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMateriVbratorRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananCManMateriVbrator = ctk.CTkButton(frmBtnCManMateriVbrator, image=imgCManMateriVbratorRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManMateriVbrator.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManMateriVbrator.bind("<Button-1>", lambda event: btnKananCManMateriVbratorClick())
btnKananCManMateriVbrator.bind("<ButtonRelease-1>", lambda event: btnKananCManMateriVbratorClickReset())

frmCManMateriVbratorBawah = ctk.CTkFrame(frmBtnCManMateriVbrator, fg_color="transparent", width=150)
frmCManMateriVbratorBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManMateriVbratorbawah = ctk.CTkFrame(frmCManMateriVbratorBawah, fg_color="transparent")
frmSwitchCManMateriVbratorbawah.grid(row=2, column=0, columnspan=2)
imageCManMateriVbratorbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MateriVbrator.png'))
imageCManMateriVbratorbawah = ctk.CTkImage(light_image=imageCManMateriVbratorbawah, size=(180, 50))
CManMateriVbratorbawahLbl = ctk.CTkLabel(frmSwitchCManMateriVbratorbawah, image=imageCManMateriVbratorbawah, text="")
CManMateriVbratorbawahLbl.pack(padx=1, pady=1)
# ------------
stateCManMatScrewCnvyr = "up"

frmCManMatScrewCnvyr = ctk.CTkFrame(frm_BolaC1LineTengah, fg_color="white")
frmCManMatScrewCnvyr.grid(row=0, column=1, padx=10, pady=(0, 5))

frmCManMatScrewCnvyrLbl = ctk.CTkFrame(frmCManMatScrewCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManMatScrewCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchCManMatScrewCnvyr = ctk.CTkLabel(frmCManMatScrewCnvyrLbl, text="Motor Screw", width=150)
lblSwitchCManMatScrewCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManMatScrewCnvyr = ctk.CTkFrame(frmCManMatScrewCnvyr, fg_color="transparent")
frmBtnCManMatScrewCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgCManMatScrewCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgCManMatScrewCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgCManMatScrewCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasCManMatScrewCnvyr = ctk.CTkCanvas(frmBtnCManMatScrewCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasCManMatScrewCnvyr.pack()
# imgCManMatScrewCnvyr = canvasCManMatScrewCnvyr.create_image(0, 0, anchor='nw', image=imgCManMatScrewCnvyrUp)

# btnKiriCManMatScrewCnvyr = canvasCManMatScrewCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManMatScrewCnvyr = canvasCManMatScrewCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# # Bind click events to transparent rectangles
# canvasCManMatScrewCnvyr.tag_bind(btnKiriCManMatScrewCnvyr, "<ButtonPress-1>", lambda event: changeCManMatScrewCnvyrSwitch("left"))
# canvasCManMatScrewCnvyr.tag_bind(btnKiriCManMatScrewCnvyr, "<ButtonRelease-1>", resetCManMatScrewCnvyrSwicth)

# canvasCManMatScrewCnvyr.tag_bind(btnKananCManMatScrewCnvyr, "<ButtonPress-1>", lambda event: changeCManMatScrewCnvyrSwitch("right"))
# canvasCManMatScrewCnvyr.tag_bind(btnKananCManMatScrewCnvyr, "<ButtonRelease-1>", resetCManMatScrewCnvyrSwicth)

imgCManMatScrewCnvyrLeftTrans = ctk.CTkImage(btnLeftTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMatScrewCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMatScrewCnvyrLeft = ctk.CTkImage(btnLeft, size=(btnRedGreenSize, btnRedGreenSize))
imgCManMatScrewCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKiriCManMatScrewCnvyr = ctk.CTkButton(frmBtnCManMatScrewCnvyr,  image=imgCManMatScrewCnvyrLeftTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKiriCManMatScrewCnvyr.grid(row=0, column=0, padx=(0, 1), pady=(0, 0))
btnKiriCManMatScrewCnvyr.bind("<Button-1>", lambda event: btnKiriCManMatScrewCnvyrClick())
btnKiriCManMatScrewCnvyr.bind("<ButtonRelease-1>", lambda event: btnKiriCManMatScrewCnvyrClickReset())

btnKananCManMatScrewCnvyr = ctk.CTkButton(frmBtnCManMatScrewCnvyr, image=imgCManMatScrewCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManMatScrewCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManMatScrewCnvyr.bind("<Button-1>", lambda event: btnKananCManMatScrewCnvyrClick())
btnKananCManMatScrewCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananCManMatScrewCnvyrClickReset())

frmCManMatScrewCnvyrBawah = ctk.CTkFrame(frmBtnCManMatScrewCnvyr, fg_color="transparent", width=150)
frmCManMatScrewCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManMatScrewCnvyrbawah = ctk.CTkFrame(frmCManMatScrewCnvyrBawah, fg_color="transparent")
frmSwitchCManMatScrewCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageCManMatScrewCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'MatScrewCnvyr.png'))
imageCManMatScrewCnvyrbawah = ctk.CTkImage(light_image=imageCManMatScrewCnvyrbawah, size=(180, 50))
CManMatScrewCnvyrbawahLbl = ctk.CTkLabel(frmSwitchCManMatScrewCnvyrbawah, image=imageCManMatScrewCnvyrbawah, text="")
CManMatScrewCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
# stateCManToRotaryCnvyr = "up"

frmCManToRotaryCnvyr = ctk.CTkFrame(frm_BolaC1LineTengah, fg_color="white")
frmCManToRotaryCnvyr.grid(row=0, column=2, padx=10, pady=(0, 5))

frmCManToRotaryCnvyrLbl = ctk.CTkFrame(frmCManToRotaryCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManToRotaryCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchCManToRotaryCnvyr = ctk.CTkLabel(frmCManToRotaryCnvyrLbl, text="Conveyor to Rotary", width=150)
lblSwitchCManToRotaryCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManToRotaryCnvyr = ctk.CTkFrame(frmCManToRotaryCnvyr, fg_color="transparent")
frmBtnCManToRotaryCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgCManToRotaryCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgCManToRotaryCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgCManToRotaryCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasCManToRotaryCnvyr = ctk.CTkCanvas(frmBtnCManToRotaryCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasCManToRotaryCnvyr.pack()
# imgCManToRotaryCnvyr = canvasCManToRotaryCnvyr.create_image(0, 0, anchor='nw', image=imgCManToRotaryCnvyrUp)

# btnKiriCManToRotaryCnvyr = canvasCManToRotaryCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManToRotaryCnvyr = canvasCManToRotaryCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasCManToRotaryCnvyr.tag_bind(btnKananCManToRotaryCnvyr, "<ButtonPress-1>", lambda event: changeCManToRotaryCnvyrSwitch("right"))
# canvasCManToRotaryCnvyr.tag_bind(btnKananCManToRotaryCnvyr, "<ButtonRelease-1>", resetCManToRotaryCnvyrSwicth)

imgCManToRotaryCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManToRotaryCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananCManToRotaryCnvyr = ctk.CTkButton(frmBtnCManToRotaryCnvyr, image=imgCManToRotaryCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManToRotaryCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManToRotaryCnvyr.bind("<Button-1>", lambda event: btnKananCManToRotaryCnvyrClick())
btnKananCManToRotaryCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananCManToRotaryCnvyrClickReset())

frmCManToRotaryCnvyrBawah = ctk.CTkFrame(frmBtnCManToRotaryCnvyr, fg_color="transparent", width=150)
frmCManToRotaryCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManToRotaryCnvyrbawah = ctk.CTkFrame(frmCManToRotaryCnvyrBawah, fg_color="transparent")
frmSwitchCManToRotaryCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageCManToRotaryCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr.png'))
imageCManToRotaryCnvyrbawah = ctk.CTkImage(light_image=imageCManToRotaryCnvyrbawah, size=(180, 50))
CManToRotaryCnvyrbawahLbl = ctk.CTkLabel(frmSwitchCManToRotaryCnvyrbawah, image=imageCManToRotaryCnvyrbawah, text="")
CManToRotaryCnvyrbawahLbl.pack(padx=1, pady=1)
# END frm_BolaC1LineTengah
# START frm_BolaC1Linebawah
frm_BolaC1Linebawah = ctk.CTkFrame(frame_tabManualBola1, fg_color="white")
frm_BolaC1Linebawah.grid(row=3, column=0, padx=20, pady=15, sticky="w")

# ------------
frmCManToRotaryCnvyr0 = ctk.CTkFrame(frm_BolaC1Linebawah, fg_color="white")
frmCManToRotaryCnvyr0.grid(row=0, column=0, padx=30, pady=1)

frmnCManRtaryUnitHop0 = ctk.CTkFrame(frmCManToRotaryCnvyr0, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnCManRtaryUnitHop0.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop0 = ctk.CTkLabel(frmnCManRtaryUnitHop0, text="Hopper Rotary 3", width=150)
lblSensornRtaryUnitHop0.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToRotaryCnvyr0 = ctk.CTkFrame(frmCManToRotaryCnvyr0, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToRotaryCnvyr0.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToRotaryCnvyr0.bind("<ButtonPress-1>", lambda event: btnGreenCManToRotaryCnvyr0Click())
btnGreenCManToRotaryCnvyr0.bind("<ButtonRelease-1>", lambda event: btnGreenCManToRotaryCnvyr0ClickReset())

frmSwitchCManToRotaryCnvyr0bawah = ctk.CTkFrame(frmCManToRotaryCnvyr0, fg_color="transparent")
frmSwitchCManToRotaryCnvyr0bawah.grid(row=2, column=0, columnspan=2)
imageCManToRotaryCnvyr0bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr2.png'))
imageCManToRotaryCnvyr0bawah = ctk.CTkImage(light_image=imageCManToRotaryCnvyr0bawah, size=(180, 50))
CManToRotaryCnvyr0bawahLbl = ctk.CTkLabel(frmSwitchCManToRotaryCnvyr0bawah, image=imageCManToRotaryCnvyr0bawah, text="")
CManToRotaryCnvyr0bawahLbl.pack(padx=1, pady=1)
# ------------
frmCManToRotaryCnvyr1 = ctk.CTkFrame(frm_BolaC1Linebawah, fg_color="white")
frmCManToRotaryCnvyr1.grid(row=0, column=1, padx=10, pady=1)

frmnCManRtaryUnitHop1 = ctk.CTkFrame(frmCManToRotaryCnvyr1, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnCManRtaryUnitHop1.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop1 = ctk.CTkLabel(frmnCManRtaryUnitHop1, text="Hopper Rotary 2", width=150)
lblSensornRtaryUnitHop1.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToRotaryCnvyr1 = ctk.CTkFrame(frmCManToRotaryCnvyr1, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToRotaryCnvyr1.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToRotaryCnvyr1.bind("<ButtonPress-1>", lambda event: btnGreenCManToRotaryCnvyr1Click())
btnGreenCManToRotaryCnvyr1.bind("<ButtonRelease-1>", lambda event: btnGreenCManToRotaryCnvyr1ClickReset())

frmSwitchCManToRotaryCnvyr1bawah = ctk.CTkFrame(frmCManToRotaryCnvyr1, fg_color="transparent")
frmSwitchCManToRotaryCnvyr1bawah.grid(row=2, column=0, columnspan=2)
imageCManToRotaryCnvyr1bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr3.png'))
imageCManToRotaryCnvyr1bawah = ctk.CTkImage(light_image=imageCManToRotaryCnvyr1bawah, size=(180, 50))
CManToRotaryCnvyr1bawahLbl = ctk.CTkLabel(frmSwitchCManToRotaryCnvyr1bawah, image=imageCManToRotaryCnvyr1bawah, text="")
CManToRotaryCnvyr1bawahLbl.pack(padx=1, pady=1)
# ------------
frmCManToRotaryCnvyr2 = ctk.CTkFrame(frm_BolaC1Linebawah, fg_color="white")
frmCManToRotaryCnvyr2.grid(row=0, column=2, padx=10, pady=1)

frmnCManRtaryUnitHop2 = ctk.CTkFrame(frmCManToRotaryCnvyr2, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnCManRtaryUnitHop2.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRtaryUnitHop2 = ctk.CTkLabel(frmnCManRtaryUnitHop2, text="Hopper Rotary 1", width=150)
lblSensornRtaryUnitHop2.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToRotaryCnvyr2 = ctk.CTkFrame(frmCManToRotaryCnvyr2, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToRotaryCnvyr2.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToRotaryCnvyr2.bind("<ButtonPress-1>", lambda event: btnGreenCManToRotaryCnvyr2Click())
btnGreenCManToRotaryCnvyr2.bind("<ButtonRelease-1>", lambda event: btnGreenCManToRotaryCnvyr2ClickReset())

frmSwitchCManToRotaryCnvyr2bawah = ctk.CTkFrame(frmCManToRotaryCnvyr2, fg_color="transparent")
frmSwitchCManToRotaryCnvyr2bawah.grid(row=2, column=0, columnspan=2)
imageCManToRotaryCnvyr2bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToRotaryCnvyr4.png'))
imageCManToRotaryCnvyr2bawah = ctk.CTkImage(light_image=imageCManToRotaryCnvyr2bawah, size=(180, 50))
CManToRotaryCnvyr2bawahLbl = ctk.CTkLabel(frmSwitchCManToRotaryCnvyr2bawah, image=imageCManToRotaryCnvyr2bawah, text="")
CManToRotaryCnvyr2bawahLbl.pack(padx=1, pady=1)

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualBola1, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=1, pady=(45,0),sticky="w")

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA, state="normal")
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU









# ================================================================================
# LINE C - UI UX - MANUAL 2/3 - .cman2
# ================================================================================

# -------------------------------------------------------------------------------------------------------------------------
frame_tabManualBola2 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualBola2.pack(fill="both", expand=True)
# START frm_BolaC2LineAtas
frm_BolaC2LineAtas = ctk.CTkFrame(frame_tabManualBola2, fg_color="white")
frm_BolaC2LineAtas.grid(row=0, column=0, padx=20, pady=1, sticky="w")
# ------------
# stateCManFrmRtaryCnvyr = "up"

frmCManRtaryCnvyr = ctk.CTkFrame(frm_BolaC2LineAtas, fg_color="white")
frmCManRtaryCnvyr.grid(row=0, column=0, padx=(0,20), pady=(0, 5))

frmCManRtaryCnvyrLbl = ctk.CTkFrame(frmCManRtaryCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManRtaryCnvyrLbl.grid(row=1, column=0, padx=1, pady=10)

lblSwitchCManFrmRtaryCnvyr = ctk.CTkLabel(frmCManRtaryCnvyrLbl, text="Conveyor\nfrom Rotary", width=150)
lblSwitchCManFrmRtaryCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManFrmRtaryCnvyr = ctk.CTkFrame(frmCManRtaryCnvyr, fg_color="transparent")
frmBtnCManFrmRtaryCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgCManFrmRtaryCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgCManFrmRtaryCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgCManFrmRtaryCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasCManFrmRtaryCnvyr = ctk.CTkCanvas(frmBtnCManFrmRtaryCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasCManFrmRtaryCnvyr.pack()
# imgCManFrmRtaryCnvyr = canvasCManFrmRtaryCnvyr.create_image(0, 0, anchor='nw', image=imgCManFrmRtaryCnvyrUp)

# btnKiriCManFrmRtaryCnvyr = canvasCManFrmRtaryCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManFrmRtaryCnvyr = canvasCManFrmRtaryCnvyr.create_rectangle(image_height + 24, 0, (image_height + 24) + image_height,
#                                                              image_height, outline='', fill='')

# canvasCManFrmRtaryCnvyr.tag_bind(btnKananCManFrmRtaryCnvyr, "<ButtonPress-1>", lambda event: changeCManFrmRtaryCnvyrSwitch("right"))
# canvasCManFrmRtaryCnvyr.tag_bind(btnKananCManFrmRtaryCnvyr, "<ButtonRelease-1>", resetCManFrmRtaryCnvyrSwicth)

imgCManFrmRtaryCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManFrmRtaryCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananCManFrmRtaryCnvyr = ctk.CTkButton(frmBtnCManFrmRtaryCnvyr, image=imgCManFrmRtaryCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManFrmRtaryCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManFrmRtaryCnvyr.bind("<Button-1>", lambda event: btnKananCManFrmRtaryCnvyrClick())
btnKananCManFrmRtaryCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananCManFrmRtaryCnvyrClickReset())

frmCManFrmRtaryCnvyrBawah = ctk.CTkFrame(frmBtnCManFrmRtaryCnvyr, fg_color="transparent", width=150)
frmCManFrmRtaryCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManFrmRtaryCnvyrbawah = ctk.CTkFrame(frmCManFrmRtaryCnvyrBawah, fg_color="transparent")
frmSwitchCManFrmRtaryCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageCManFrmRtaryCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'FrmRtaryCnvyr.png'))
imageCManFrmRtaryCnvyrbawah = ctk.CTkImage(light_image=imageCManFrmRtaryCnvyrbawah, size=(180, 50))
CManFrmRtaryCnvyrbawahLbl = ctk.CTkLabel(frmSwitchCManFrmRtaryCnvyrbawah, image=imageCManFrmRtaryCnvyrbawah, text="")
CManFrmRtaryCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
# stateCManUpLadderCnvyr = "up"

frmCManUpLadderCnvyr = ctk.CTkFrame(frm_BolaC2LineAtas, fg_color="white")
frmCManUpLadderCnvyr.grid(row=0, column=1, padx=(30,0), pady=10)

frmCManUpLadderCnvyrLbl = ctk.CTkFrame(frmCManUpLadderCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManUpLadderCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchCManUpLadderCnvyr = ctk.CTkLabel(frmCManUpLadderCnvyrLbl, text="Incline Conveyor", width=150)
lblSwitchCManUpLadderCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManUpLadderCnvyr = ctk.CTkFrame(frmCManUpLadderCnvyr, fg_color="transparent")
frmBtnCManUpLadderCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgCManUpLadderCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgCManUpLadderCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgCManUpLadderCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasCManUpLadderCnvyr = ctk.CTkCanvas(frmBtnCManUpLadderCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasCManUpLadderCnvyr.pack()
# imgCManUpLadderCnvyr = canvasCManUpLadderCnvyr.create_image(0, 0, anchor='nw', image=imgCManUpLadderCnvyrUp)

# btnKiriCManUpLadderCnvyr = canvasCManUpLadderCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManUpLadderCnvyr = canvasCManUpLadderCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasCManUpLadderCnvyr.tag_bind(btnKananCManUpLadderCnvyr, "<ButtonPress-1>", lambda event: changeCManUpLadderCnvyrSwitch("right"))
# canvasCManUpLadderCnvyr.tag_bind(btnKananCManUpLadderCnvyr, "<ButtonRelease-1>", resetCManUpLadderCnvyrSwicth)

imgCManUpLadderCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManUpLadderCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananCManUpLadderCnvyr = ctk.CTkButton(frmBtnCManUpLadderCnvyr, image=imgCManUpLadderCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManUpLadderCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManUpLadderCnvyr.bind("<Button-1>", lambda event: btnKananCManUpLadderCnvyrClick())
btnKananCManUpLadderCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananCManUpLadderCnvyrClickReset())

frmCManUpLadderCnvyrBawah = ctk.CTkFrame(frmBtnCManUpLadderCnvyr, fg_color="transparent", width=150)
frmCManUpLadderCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManUpLadderCnvyrbawah = ctk.CTkFrame(frmCManUpLadderCnvyrBawah, fg_color="transparent")
frmSwitchCManUpLadderCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageCManUpLadderCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'UpLadderCnvyr.png'))
imageCManUpLadderCnvyrbawah = ctk.CTkImage(light_image=imageCManUpLadderCnvyrbawah, size=(180, 50))
CManUpLadderCnvyrbawahLbl = ctk.CTkLabel(frmSwitchCManUpLadderCnvyrbawah, image=imageCManUpLadderCnvyrbawah, text="")
CManUpLadderCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
stateCManToHopperCnvyr = "up"

frmCManToHopperCnvyr = ctk.CTkFrame(frm_BolaC2LineAtas, fg_color="white")
frmCManToHopperCnvyr.grid(row=0, column=2, padx=(30,0), pady=10)

frmCManToHopperCnvyrLbl = ctk.CTkFrame(frmCManToHopperCnvyr, fg_color="white", corner_radius=0, border_color="light grey",
                                   border_width=5)
frmCManToHopperCnvyrLbl.grid(row=1, column=0, padx=5, pady=10)

lblSwitchCManToHopperCnvyr = ctk.CTkLabel(frmCManToHopperCnvyrLbl, text="Conveyor to Silo", width=150)
lblSwitchCManToHopperCnvyr.grid(row=0, column=0, padx=10, pady=5)

frmBtnCManToHopperCnvyr = ctk.CTkFrame(frmCManToHopperCnvyr, fg_color="transparent")
frmBtnCManToHopperCnvyr.grid(row=2, column=0, padx=1, pady=1)

# imgCManToHopperCnvyrUp = ImageTk.PhotoImage(switchUp)
# imgCManToHopperCnvyrLeft = ImageTk.PhotoImage(switchLeft)
# imgCManToHopperCnvyrRight = ImageTk.PhotoImage(switchRight)

# canvasCManToHopperCnvyr = ctk.CTkCanvas(frmBtnCManToHopperCnvyr, width=image_width, height=image_height, highlightthickness=0)
# canvasCManToHopperCnvyr.pack()
# imgCManToHopperCnvyr = canvasCManToHopperCnvyr.create_image(0, 0, anchor='nw', image=imgCManToHopperCnvyrUp)

# btnKiriCManToHopperCnvyr = canvasCManToHopperCnvyr.create_rectangle(0, 0, image_height, image_height, outline='', fill='')
# btnKananCManToHopperCnvyr = canvasCManToHopperCnvyr.create_rectangle(image_height + 20, 0, (image_height + 20) + image_height,
#                                                              image_height, outline='', fill='')

# canvasCManToHopperCnvyr.tag_bind(btnKananCManToHopperCnvyr, "<ButtonPress-1>", lambda event: changeCManToHopperCnvyrSwitch("right"))
# canvasCManToHopperCnvyr.tag_bind(btnKananCManToHopperCnvyr, "<ButtonRelease-1>", resetCManToHopperCnvyrSwicth)

imgCManToHopperCnvyrRightTrans = ctk.CTkImage(btnRightTrans, size=(btnRedGreenSize, btnRedGreenSize))
imgCManToHopperCnvyrRight = ctk.CTkImage(btnRight, size=(btnRedGreenSize, btnRedGreenSize))

btnKananCManToHopperCnvyr = ctk.CTkButton(frmBtnCManToHopperCnvyr, image=imgCManToHopperCnvyrRightTrans, text="", fg_color="transparent", width=btnRedGreenSize, height=btnRedGreenSize)
btnKananCManToHopperCnvyr.grid(row=0, column=1, padx=(1, 0), pady=(0, 0))
btnKananCManToHopperCnvyr.bind("<Button-1>", lambda event: btnKananCManToHopperCnvyrClick())
btnKananCManToHopperCnvyr.bind("<ButtonRelease-1>", lambda event: btnKananCManToHopperCnvyrClickReset())

frmCManToHopperCnvyrBawah = ctk.CTkFrame(frmBtnCManToHopperCnvyr, fg_color="transparent", width=150)
frmCManToHopperCnvyrBawah.grid(row=1, column=0, padx=1, pady=(1,0), columnspan=2)

frmSwitchCManToHopperCnvyrbawah = ctk.CTkFrame(frmCManToHopperCnvyrBawah, fg_color="transparent")
frmSwitchCManToHopperCnvyrbawah.grid(row=2, column=0, columnspan=2)
imageCManToHopperCnvyrbawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr.png'))
imageCManToHopperCnvyrbawah = ctk.CTkImage(light_image=imageCManToHopperCnvyrbawah, size=(180, 50))
CManToHopperCnvyrbawahLbl = ctk.CTkLabel(frmSwitchCManToHopperCnvyrbawah, image=imageCManToHopperCnvyrbawah, text="")
CManToHopperCnvyrbawahLbl.pack(padx=1, pady=1)
# ------------
frmCManToHopperCnvyr0 = ctk.CTkFrame(frm_BolaC2LineAtas, fg_color="white")
frmCManToHopperCnvyr0.grid(row=0, column=3, padx=(30,0), pady=1)

frmnCManTabletVaryHop0 = ctk.CTkFrame(frmCManToHopperCnvyr0, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnCManTabletVaryHop0.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornCManTabletVaryHop0 = ctk.CTkLabel(frmnCManTabletVaryHop0, text="Sensor Silo 5", width=150)
lblSensornCManTabletVaryHop0.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToHopperCnvyr0 = ctk.CTkFrame(frmCManToHopperCnvyr0, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToHopperCnvyr0.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToHopperCnvyr0.bind("<ButtonPress-1>", lambda event: btnGreenCManToHopperCnvyr0Click())
btnGreenCManToHopperCnvyr0.bind("<ButtonRelease-1>", lambda event: btnGreenCManToHopperCnvyr0ClickReset())

frmSwitchCManToHopperCnvyr0bawah = ctk.CTkFrame(frmCManToHopperCnvyr0, fg_color="transparent")
frmSwitchCManToHopperCnvyr0bawah.grid(row=2, column=0, columnspan=2)
imageCManToHopperCnvyr0bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr00.png'))
imageCManToHopperCnvyr0bawah = ctk.CTkImage(light_image=imageCManToHopperCnvyr0bawah, size=(180, 50))
CManToHopperCnvyr0bawahLbl = ctk.CTkLabel(frmSwitchCManToHopperCnvyr0bawah, image=imageCManToHopperCnvyr0bawah, text="")
CManToHopperCnvyr0bawahLbl.pack(padx=1, pady=1)
# END frm_BolaC2LineAtas
# START frm_BolaC2LineBawah
frm_BolaC2LineBawah = ctk.CTkFrame(frame_tabManualBola2, fg_color="white")
frm_BolaC2LineBawah.grid(row=1, column=0, padx=20, pady=(30,177), sticky="w")
# ------------
frmCManToHopperCnvyr1 = ctk.CTkFrame(frm_BolaC2LineBawah, fg_color="white")
frmCManToHopperCnvyr1.grid(row=0, column=0, padx=(0, 20), pady=1)

frmnCManTabletVaryHop1 = ctk.CTkFrame(frmCManToHopperCnvyr1, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnCManTabletVaryHop1.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornCManTabletVaryHop1 = ctk.CTkLabel(frmnCManTabletVaryHop1, text="Sensor Silo 4", width=150)
lblSensornCManTabletVaryHop1.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToHopperCnvyr1 = ctk.CTkFrame(frmCManToHopperCnvyr1, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToHopperCnvyr1.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToHopperCnvyr1.bind("<ButtonPress-1>", lambda event: btnGreenCManToHopperCnvyr1Click())
btnGreenCManToHopperCnvyr1.bind("<ButtonRelease-1>", lambda event: btnGreenCManToHopperCnvyr1ClickReset())

frmSwitchCManToHopperCnvyr1bawah = ctk.CTkFrame(frmCManToHopperCnvyr1, fg_color="transparent")
frmSwitchCManToHopperCnvyr1bawah.grid(row=2, column=0, columnspan=2)
imageCManToHopperCnvyr1bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr0.png'))
imageCManToHopperCnvyr1bawah = ctk.CTkImage(light_image=imageCManToHopperCnvyr1bawah, size=(180, 50))
CManToHopperCnvyr1bawahLbl = ctk.CTkLabel(frmSwitchCManToHopperCnvyr1bawah, image=imageCManToHopperCnvyr1bawah, text="")
CManToHopperCnvyr1bawahLbl.pack(padx=1, pady=1)
# ------------
frmCManToHopperCnvyr2 = ctk.CTkFrame(frm_BolaC2LineBawah, fg_color="white")
frmCManToHopperCnvyr2.grid(row=0, column=1, padx=(75, 20), pady=1)

frmnManCTabletVaryHop2 = ctk.CTkFrame(frmCManToHopperCnvyr2, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCTabletVaryHop2.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornManCTabletVaryHop2 = ctk.CTkLabel(frmnManCTabletVaryHop2, text="Sensor Silo 3", width=150)
lblSensornManCTabletVaryHop2.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToHopperCnvyr2 = ctk.CTkFrame(frmCManToHopperCnvyr2, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToHopperCnvyr2.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToHopperCnvyr2.bind("<ButtonPress-1>", lambda event: btnGreenCManToHopperCnvyr2Click())
btnGreenCManToHopperCnvyr2.bind("<ButtonRelease-1>", lambda event: btnGreenCManToHopperCnvyr2ClickReset())

frmSwitchCManToHopperCnvyr2bawah = ctk.CTkFrame(frmCManToHopperCnvyr2, fg_color="transparent")
frmSwitchCManToHopperCnvyr2bawah.grid(row=2, column=0, columnspan=2)
imageCManToHopperCnvyr2bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr1.png'))
imageCManToHopperCnvyr2bawah = ctk.CTkImage(light_image=imageCManToHopperCnvyr2bawah, size=(180, 50))
CManToHopperCnvyr2bawahLbl = ctk.CTkLabel(frmSwitchCManToHopperCnvyr2bawah, image=imageCManToHopperCnvyr2bawah, text="")
CManToHopperCnvyr2bawahLbl.pack(padx=1, pady=1)
# ------------
frmCManToHopperCnvyr3 = ctk.CTkFrame(frm_BolaC2LineBawah, fg_color="white")
frmCManToHopperCnvyr3.grid(row=0, column=2, padx=(75, 20), pady=1)

frmnManCTabletVaryHop3 = ctk.CTkFrame(frmCManToHopperCnvyr3, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCTabletVaryHop3.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornManCTabletVaryHop3 = ctk.CTkLabel(frmnManCTabletVaryHop3, text="Sensor Silo 2", width=150)
lblSensornManCTabletVaryHop3.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToHopperCnvyr3 = ctk.CTkFrame(frmCManToHopperCnvyr3, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToHopperCnvyr3.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToHopperCnvyr3.bind("<ButtonPress-1>", lambda event: btnGreenCManToHopperCnvyr3Click())
btnGreenCManToHopperCnvyr3.bind("<ButtonRelease-1>", lambda event: btnGreenCManToHopperCnvyr3ClickReset())

frmSwitchCManToHopperCnvyr3bawah = ctk.CTkFrame(frmCManToHopperCnvyr3, fg_color="transparent")
frmSwitchCManToHopperCnvyr3bawah.grid(row=2, column=0, columnspan=2)
imageCManToHopperCnvyr3bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr2.png'))
imageCManToHopperCnvyr3bawah = ctk.CTkImage(light_image=imageCManToHopperCnvyr3bawah, size=(180, 50))
CManToHopperCnvyr3bawahLbl = ctk.CTkLabel(frmSwitchCManToHopperCnvyr3bawah, image=imageCManToHopperCnvyr3bawah, text="")
CManToHopperCnvyr3bawahLbl.pack(padx=1, pady=1)
# ------------
frmCManToHopperCnvyr4 = ctk.CTkFrame(frm_BolaC2LineBawah, fg_color="white")
frmCManToHopperCnvyr4.grid(row=0, column=3, padx=(65, 0), pady=1)

frmnManCTabletVaryHop4 = ctk.CTkFrame(frmCManToHopperCnvyr4, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCTabletVaryHop4.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornManCTabletVaryHop3 = ctk.CTkLabel(frmnManCTabletVaryHop4, text="Sensor Silo 1", width=150)
lblSensornManCTabletVaryHop3.grid(row=0, column=0, padx=10, pady=5)

btnGreenCManToHopperCnvyr4 = ctk.CTkFrame(frmCManToHopperCnvyr4, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenCManToHopperCnvyr4.grid(row=1, column=0, padx=1, pady=1)
btnGreenCManToHopperCnvyr4.bind("<ButtonPress-1>", lambda event: btnGreenCManToHopperCnvyr4Click())
btnGreenCManToHopperCnvyr4.bind("<ButtonRelease-1>", lambda event: btnGreenCManToHopperCnvyr4ClickReset())

frmSwitchCManToHopperCnvyr4bawah = ctk.CTkFrame(frmCManToHopperCnvyr4, fg_color="transparent")
frmSwitchCManToHopperCnvyr4bawah.grid(row=2, column=0, columnspan=2)
imageCManToHopperCnvyr4bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'ToHopperCnvyr3.png'))
imageCManToHopperCnvyr4bawah = ctk.CTkImage(light_image=imageCManToHopperCnvyr4bawah, size=(180, 50))
CManToHopperCnvyr4bawahLbl = ctk.CTkLabel(frmSwitchCManToHopperCnvyr4bawah, image=imageCManToHopperCnvyr4bawah, text="")
CManToHopperCnvyr4bawahLbl.pack(padx=1, pady=1)

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualBola2, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=(0,1), pady=(56,0), sticky="w")

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB, state="normal")
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC)
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU





























# ================================================================================
# LINE C - UI UX - MANUAL 3/3 - .cman3
# ================================================================================

frame_tabManualBola3 = ctk.CTkFrame(app, fg_color="white")
frame_tabManualBola3.pack(fill="both", expand=True)
# START frm_BolaC3LineAtas
frm_BolaC3LineAtas = ctk.CTkFrame(frame_tabManualBola3, fg_color="white")
frm_BolaC3LineAtas.grid(row=0, column=0, padx=20, pady=20, sticky="w")
# ------------
frmManCTbletHoprDoor0 = ctk.CTkFrame(frm_BolaC3LineAtas, fg_color="white")
frmManCTbletHoprDoor0.grid(row=0, column=0, padx=(0,65), pady=(0, 5))

frmnManCRncenMachHop0 = ctk.CTkFrame(frmManCTbletHoprDoor0, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCRncenMachHop0.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop0 = ctk.CTkLabel(frmnManCRncenMachHop0, text="Sensor\nRncenMachHop 0", width=150)
lblSensornRncenMachHop0.grid(row=0, column=0, padx=10, pady=5)

frmManCTbletHoprDoor0Lbl = ctk.CTkFrame(frmManCTbletHoprDoor0, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManCTbletHoprDoor0Lbl.grid(row=1, column=0, padx=5, pady=(5, 5))

lblSwitchManCTbletHoprDoor0 = ctk.CTkLabel(frmManCTbletHoprDoor0Lbl, text="Silo Door 5", width=150)
lblSwitchManCTbletHoprDoor0.grid(row=1, column=0, padx=10, pady=5)

frmBtnManCTbletHoprDoor0 = ctk.CTkFrame(frmManCTbletHoprDoor0, fg_color="transparent")
frmBtnManCTbletHoprDoor0.grid(row=2, column=0, padx=1, pady=1)

btnRedManCTbletHoprDoor0 = ctk.CTkFrame(frmBtnManCTbletHoprDoor0, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='pink', border_color="black", border_width=5)
btnRedManCTbletHoprDoor0.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManCTbletHoprDoor0.bind("<Button-1>", lambda event: btnRedManCTbletHoprDoor0Click())
btnRedManCTbletHoprDoor0.bind("<ButtonRelease-1>", lambda event: btnRedManCTbletHoprDoor0ClickReset())

btnGreenManCTbletHoprDoor0 = ctk.CTkFrame(frmBtnManCTbletHoprDoor0, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='light green', border_color="black", border_width=5)
btnGreenManCTbletHoprDoor0.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManCTbletHoprDoor0.bind("<Button-1>", lambda event: btnGreenManCTbletHoprDoor0Click())
btnGreenManCTbletHoprDoor0.bind("<ButtonRelease-1>", lambda event: btnGreenManCTbletHoprDoor0ClickReset())

frmSwitchManCTbletHoprDoor0bawah = ctk.CTkFrame(frmBtnManCTbletHoprDoor0, fg_color="transparent")
frmSwitchManCTbletHoprDoor0bawah.grid(row=2, column=0, columnspan=2)
imageManCTbletHoprDoor0bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'SiloDoor5.png'))
imageManCTbletHoprDoor0bawah = ctk.CTkImage(light_image=imageManCTbletHoprDoor0bawah, size=(160, 50))
ManCTbletHoprDoor0bawahLbl = ctk.CTkLabel(frmSwitchManCTbletHoprDoor0bawah, image=imageManCTbletHoprDoor0bawah, text="")
ManCTbletHoprDoor0bawahLbl.pack(padx=1, pady=1)
# ------------
frmManCTbletHoprDoor1 = ctk.CTkFrame(frm_BolaC3LineAtas, fg_color="white")
frmManCTbletHoprDoor1.grid(row=0, column=1, padx=(0,65), pady=(0, 5))

frmnManCRncenMachHop1 = ctk.CTkFrame(frmManCTbletHoprDoor1, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCRncenMachHop1.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop1 = ctk.CTkLabel(frmnManCRncenMachHop1, text="Sensor\nRncenMachHop 1", width=150)
lblSensornRncenMachHop1.grid(row=0, column=0, padx=10, pady=5)

frmManCTbletHoprDoor1Lbl = ctk.CTkFrame(frmManCTbletHoprDoor1, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManCTbletHoprDoor1Lbl.grid(row=1, column=0, padx=5, pady=(5, 5))

lblSwitchManCTbletHoprDoor1 = ctk.CTkLabel(frmManCTbletHoprDoor1Lbl, text="Silo Door 4", width=150)
lblSwitchManCTbletHoprDoor1.grid(row=1, column=0, padx=10, pady=5)

frmBtnManCTbletHoprDoor1 = ctk.CTkFrame(frmManCTbletHoprDoor1, fg_color="transparent")
frmBtnManCTbletHoprDoor1.grid(row=2, column=0, padx=1, pady=1)

btnRedManCTbletHoprDoor1 = ctk.CTkFrame(frmBtnManCTbletHoprDoor1, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='red', border_color="black", border_width=5)
btnRedManCTbletHoprDoor1.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManCTbletHoprDoor1.bind("<Button-1>", lambda event: btnRedManCTbletHoprDoor1Click())
btnRedManCTbletHoprDoor1.bind("<ButtonRelease-1>", lambda event: btnRedManCTbletHoprDoor1ClickReset())

btnGreenManCTbletHoprDoor1 = ctk.CTkFrame(frmBtnManCTbletHoprDoor1, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenManCTbletHoprDoor1.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManCTbletHoprDoor1.bind("<Button-1>", lambda event: btnGreenManCTbletHoprDoor1Click())
btnGreenManCTbletHoprDoor1.bind("<ButtonRelease-1>", lambda event: btnGreenManCTbletHoprDoor1ClickReset())

frmSwitchManCTbletHoprDoor1bawah = ctk.CTkFrame(frmBtnManCTbletHoprDoor1, fg_color="transparent")
frmSwitchManCTbletHoprDoor1bawah.grid(row=2, column=0, columnspan=2)
imageManCTbletHoprDoor1bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'SiloDoor4.png'))
imageManCTbletHoprDoor1bawah = ctk.CTkImage(light_image=imageManCTbletHoprDoor1bawah, size=(160, 50))
ManCTbletHoprDoor1bawahLbl = ctk.CTkLabel(frmSwitchManCTbletHoprDoor1bawah, image=imageManCTbletHoprDoor1bawah, text="")
ManCTbletHoprDoor1bawahLbl.pack(padx=1, pady=1)
# ------------
frmManCTbletHoprDoor2 = ctk.CTkFrame(frm_BolaC3LineAtas, fg_color="white")
frmManCTbletHoprDoor2.grid(row=0, column=2, padx=(0,5), pady=(0, 5))

frmnManCRncenMachHop2 = ctk.CTkFrame(frmManCTbletHoprDoor2, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCRncenMachHop2.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop2 = ctk.CTkLabel(frmnManCRncenMachHop2, text="Sensor\nRncenMachHop 2", width=150)
lblSensornRncenMachHop2.grid(row=0, column=0, padx=10, pady=5)

frmManCTbletHoprDoor2Lbl = ctk.CTkFrame(frmManCTbletHoprDoor2, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManCTbletHoprDoor2Lbl.grid(row=1, column=0, padx=5, pady=(5, 5))

lblSwitchManCTbletHoprDoor2 = ctk.CTkLabel(frmManCTbletHoprDoor2Lbl, text="Silo Door 3", width=150)
lblSwitchManCTbletHoprDoor2.grid(row=1, column=0, padx=10, pady=5)

frmBtnManCTbletHoprDoor2 = ctk.CTkFrame(frmManCTbletHoprDoor2, fg_color="transparent")
frmBtnManCTbletHoprDoor2.grid(row=2, column=0, padx=1, pady=1)

btnRedManCTbletHoprDoor2 = ctk.CTkFrame(frmBtnManCTbletHoprDoor2, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='red', border_color="black", border_width=5)
btnRedManCTbletHoprDoor2.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManCTbletHoprDoor2.bind("<Button-1>", lambda event: btnRedManCTbletHoprDoor2Click())
btnRedManCTbletHoprDoor2.bind("<ButtonRelease-1>", lambda event: btnRedManCTbletHoprDoor2ClickReset())

btnGreenManCTbletHoprDoor2 = ctk.CTkFrame(frmBtnManCTbletHoprDoor2, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenManCTbletHoprDoor2.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManCTbletHoprDoor2.bind("<Button-1>", lambda event: btnGreenManCTbletHoprDoor2Click())
btnGreenManCTbletHoprDoor2.bind("<ButtonRelease-1>", lambda event: btnGreenManCTbletHoprDoor2ClickReset())

frmSwitchManCTbletHoprDoor2bawah = ctk.CTkFrame(frmBtnManCTbletHoprDoor2, fg_color="transparent")
frmSwitchManCTbletHoprDoor2bawah.grid(row=2, column=0, columnspan=2)
imageManCTbletHoprDoor2bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'SiloDoor3.png'))
imageManCTbletHoprDoor2bawah = ctk.CTkImage(light_image=imageManCTbletHoprDoor2bawah, size=(160, 50))
ManCTbletHoprDoor2bawahLbl = ctk.CTkLabel(frmSwitchManCTbletHoprDoor2bawah, image=imageManCTbletHoprDoor2bawah, text="")
ManCTbletHoprDoor2bawahLbl.pack(padx=1, pady=1)
# END frm_BolaC3LineAtas
# START frm_BolaC3LineBawah
frm_BolaC3LineBawah = ctk.CTkFrame(frame_tabManualBola3, fg_color="white")
frm_BolaC3LineBawah.grid(row=1, column=0, padx=20, pady=(40,44), sticky="w")
# ------------
frmManCTbletHoprDoor3 = ctk.CTkFrame(frm_BolaC3LineBawah, fg_color="white")
frmManCTbletHoprDoor3.grid(row=0, column=0, padx=(0,65), pady=(0, 5))

frmnManCRncenMachHop3 = ctk.CTkFrame(frmManCTbletHoprDoor3, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCRncenMachHop3.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop3 = ctk.CTkLabel(frmnManCRncenMachHop3, text="Sensor\nRncenMachHop 3", width=150)
lblSensornRncenMachHop3.grid(row=0, column=0, padx=10, pady=5)

frmManCTbletHoprDoor3Lbl = ctk.CTkFrame(frmManCTbletHoprDoor3, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManCTbletHoprDoor3Lbl.grid(row=1, column=0, padx=5, pady=(5, 5))

lblSwitchManCTbletHoprDoor3 = ctk.CTkLabel(frmManCTbletHoprDoor3Lbl, text="Silo Door 2", width=150)
lblSwitchManCTbletHoprDoor3.grid(row=1, column=0, padx=10, pady=5)

frmBtnManCTbletHoprDoor3 = ctk.CTkFrame(frmManCTbletHoprDoor3, fg_color="transparent")
frmBtnManCTbletHoprDoor3.grid(row=2, column=0, padx=1, pady=1)

btnRedManCTbletHoprDoor3 = ctk.CTkFrame(frmBtnManCTbletHoprDoor3, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='red', border_color="black", border_width=5)
btnRedManCTbletHoprDoor3.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManCTbletHoprDoor3.bind("<Button-1>", lambda event: btnRedManCTbletHoprDoor3Click())
btnRedManCTbletHoprDoor3.bind("<ButtonRelease-1>", lambda event: btnRedManCTbletHoprDoor3ClickReset())

btnGreenManCTbletHoprDoor3 = ctk.CTkFrame(frmBtnManCTbletHoprDoor3, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenManCTbletHoprDoor3.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManCTbletHoprDoor3.bind("<Button-1>", lambda event: btnGreenManCTbletHoprDoor3Click())
btnGreenManCTbletHoprDoor3.bind("<ButtonRelease-1>", lambda event: btnGreenManCTbletHoprDoor3ClickReset())

frmSwitchManCTbletHoprDoor3bawah = ctk.CTkFrame(frmBtnManCTbletHoprDoor3, fg_color="transparent")
frmSwitchManCTbletHoprDoor3bawah.grid(row=2, column=0, columnspan=2)
imageManCTbletHoprDoor3bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'SiloDoor2.png'))
imageManCTbletHoprDoor3bawah = ctk.CTkImage(light_image=imageManCTbletHoprDoor3bawah, size=(160, 50))
ManCTbletHoprDoor3bawahLbl = ctk.CTkLabel(frmSwitchManCTbletHoprDoor3bawah, image=imageManCTbletHoprDoor3bawah, text="")
ManCTbletHoprDoor3bawahLbl.pack(padx=1, pady=1)
# ------------
frmManCTbletHoprDoor4 = ctk.CTkFrame(frm_BolaC3LineBawah, fg_color="white")
frmManCTbletHoprDoor4.grid(row=0, column=1, padx=(0,65), pady=(0, 5))

frmnManCRncenMachHop4 = ctk.CTkFrame(frmManCTbletHoprDoor4, fg_color="white", corner_radius=0, border_color="light grey",
                                  border_width=5)
frmnManCRncenMachHop4.grid(row=0, column=0, padx=5, pady=(5, 5))

lblSensornRncenMachHop4 = ctk.CTkLabel(frmnManCRncenMachHop4, text="Sensor\nRncenMachHop 4", width=150)
lblSensornRncenMachHop4.grid(row=0, column=0, padx=10, pady=5)

frmManCTbletHoprDoor4Lbl = ctk.CTkFrame(frmManCTbletHoprDoor4, fg_color="white", corner_radius=0, border_color="light grey",
                                    border_width=5)
frmManCTbletHoprDoor4Lbl.grid(row=1, column=0, padx=5, pady=(5, 5))

lblSwitchManCTbletHoprDoor4 = ctk.CTkLabel(frmManCTbletHoprDoor4Lbl, text="Silo Door 1", width=150)
lblSwitchManCTbletHoprDoor4.grid(row=1, column=0, padx=10, pady=5)

frmBtnManCTbletHoprDoor4 = ctk.CTkFrame(frmManCTbletHoprDoor4, fg_color="transparent")
frmBtnManCTbletHoprDoor4.grid(row=2, column=0, padx=1, pady=1)

btnRedManCTbletHoprDoor4 = ctk.CTkFrame(frmBtnManCTbletHoprDoor4, width=btnRedGreenSize, height=btnRedGreenSize,
                                    corner_radius=100, fg_color='red', border_color="black", border_width=5)
btnRedManCTbletHoprDoor4.grid(row=0, column=0, padx=(1, 5), pady=1)
btnRedManCTbletHoprDoor4.bind("<Button-1>", lambda event: btnRedManCTbletHoprDoor4Click())
btnRedManCTbletHoprDoor4.bind("<ButtonRelease-1>", lambda event: btnRedManCTbletHoprDoor4ClickReset())

btnGreenManCTbletHoprDoor4 = ctk.CTkFrame(frmBtnManCTbletHoprDoor4, width=btnRedGreenSize, height=btnRedGreenSize,
                                      corner_radius=100, fg_color='lime', border_color="black", border_width=5)
btnGreenManCTbletHoprDoor4.grid(row=0, column=1, padx=(5, 1), pady=1)
btnGreenManCTbletHoprDoor4.bind("<Button-1>", lambda event: btnGreenManCTbletHoprDoor4Click())
btnGreenManCTbletHoprDoor4.bind("<ButtonRelease-1>", lambda event: btnGreenManCTbletHoprDoor4ClickReset())

frmSwitchManCTbletHoprDoor4bawah = ctk.CTkFrame(frmBtnManCTbletHoprDoor4, fg_color="transparent")
frmSwitchManCTbletHoprDoor4bawah.grid(row=2, column=0, columnspan=2)
imageManCTbletHoprDoor4bawah = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'SiloDoor1.png'))
imageManCTbletHoprDoor4bawah = ctk.CTkImage(light_image=imageManCTbletHoprDoor4bawah, size=(160, 50))
ManCTbletHoprDoor4bawahLbl = ctk.CTkLabel(frmSwitchManCTbletHoprDoor4bawah, image=imageManCTbletHoprDoor4bawah, text="")
ManCTbletHoprDoor4bawahLbl.pack(padx=1, pady=1)
# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabManualBola3, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=1, pady=(72,0), sticky="w")

btnMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Common\n1/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan)
btnMenuCommon.grid(row=1, column=0, padx=1, pady=(1, 5))

btnMenuCommo2 = ctk.CTkButton(frm_MenuBawah, text="Common\n2/2", fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=91, height=55, command=showCommonMan2)
btnMenuCommo2.grid(row=1, column=1, padx=1, pady=(1, 5))

btnKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA1.grid(row=1, column=2, padx=1, pady=(1, 5))

btnKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA2.grid(row=1, column=3, padx=1, pady=(1, 5))

btnKecilA3 = ctk.CTkButton(frm_MenuBawah, text="Kecil(A)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55)
btnKecilA3.grid(row=1, column=4, padx=1, pady=(1, 5))

btnBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n1/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarA)
btnBesarB1.grid(row=1, column=5, padx=1, pady=(1, 5))

btnBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n2/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarB)
btnBesarB2.grid(row=1, column=6, padx=1, pady=(1, 5))

btnBesarB3 = ctk.CTkButton(frm_MenuBawah, text="Besar(B)\n3/3", fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=91, height=55, command=showBesarC)
btnBesarB3.grid(row=1, column=7, padx=1, pady=(1, 5))

btnBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n1/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaA)
btnBolaC1.grid(row=1, column=8, padx=1, pady=(1, 5))

btnBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n2/3", fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaB)
btnBolaC2.grid(row=1, column=9, padx=1, pady=(1, 5))

btnBolaC3 = ctk.CTkButton(frm_MenuBawah, text="Bola(C)\n3/3", fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=91, height=55, command=showBolaC, state="normal")
btnBolaC3.grid(row=1, column=10, padx=1, pady=(1, 5))
# END Button MENU








# ================================================================================
# LINE C - UI UX - AUTO 1/2 .cauto1
# ================================================================================


frame_tabBesarCAuto = ctk.CTkFrame(app, fg_color="white")
frame_tabBesarCAuto.pack(fill="both", expand=True)



frmCAuto1 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto1.pack(padx=5, pady=(1, 1))
frmCAuto1.grid(row=0, column=0, padx=10, pady=1, sticky="w")


frmCAutoMotorMateriVbrator = ctk.CTkFrame(frmCAuto1, fg_color="white")
frmCAutoMotorMateriVbrator.grid(row=0, column=0, padx=1, pady=1)

imageCAutoMotorMateriVbrator = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMateriVbrator.png'))
imageCAutoMotorMateriVbrator = ctk.CTkImage(light_image=imageCAutoMotorMateriVbrator, size=(160, 20)) 
CAutoMotorMateriVbratorLbl = ctk.CTkLabel(frmCAutoMotorMateriVbrator, image=imageCAutoMotorMateriVbrator, text="")
CAutoMotorMateriVbratorLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnCAutoMotorMateriVbratorDoStart = ctk.CTkButton(frmCAutoMotorMateriVbrator, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMateriVbratorDoStart.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorMateriVbratorIsFault = ctk.CTkButton(frmCAutoMotorMateriVbrator, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMateriVbratorIsFault.grid(row=1, column=1, padx=1, pady=1)

frmCAutoMotorMatScrewCnvyr = ctk.CTkFrame(frmCAuto1, fg_color="white")
frmCAutoMotorMatScrewCnvyr.grid(row=0, column=1, padx=1, pady=1)

imageCAutoMotorMatScrewCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorMatScrewCnvyr.png'))
imageCAutoMotorMatScrewCnvyr = ctk.CTkImage(light_image=imageCAutoMotorMatScrewCnvyr, size=(240, 20)) 
CAutoMotorMatScrewCnvyrLbl = ctk.CTkLabel(frmCAutoMotorMatScrewCnvyr, image=imageCAutoMotorMatScrewCnvyr, text="")
CAutoMotorMatScrewCnvyrLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnCAutoMotorMatScrewCnvyrDoRev = ctk.CTkButton(frmCAutoMotorMatScrewCnvyr, text="Rev", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMatScrewCnvyrDoRev.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorMatScrewCnvyrDoFwd = ctk.CTkButton(frmCAutoMotorMatScrewCnvyr, text="Fwd", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMatScrewCnvyrDoFwd.grid(row=1, column=1, padx=1, pady=1)
btnCAutoMotorMatScrewCnvyrIsFault = ctk.CTkButton(frmCAutoMotorMatScrewCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorMatScrewCnvyrIsFault.grid(row=1, column=2, padx=1, pady=1)

frmCAutoMotorToRotaryCnvyr = ctk.CTkFrame(frmCAuto1, fg_color="white")
frmCAutoMotorToRotaryCnvyr.grid(row=0, column=2, padx=1, pady=1)

imageCAutoMotorToRotaryCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorToRotaryCnvyr.png'))
imageCAutoMotorToRotaryCnvyr = ctk.CTkImage(light_image=imageCAutoMotorToRotaryCnvyr, size=(160, 20)) 
CAutoMotorToRotaryCnvyrLbl = ctk.CTkLabel(frmCAutoMotorToRotaryCnvyr, image=imageCAutoMotorToRotaryCnvyr, text="")
CAutoMotorToRotaryCnvyrLbl.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btnCAutoMotorToRotaryCnvyrDoStart = ctk.CTkButton(frmCAutoMotorToRotaryCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorToRotaryCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorToRotaryCnvyrIsFault = ctk.CTkButton(frmCAutoMotorToRotaryCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorToRotaryCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)


# btnCAutoMixingDoStart = ctk.CTkButton(frmCAutoMixing, text="DoStart", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
# btnCAutoMixingDoStart.grid(row=1, column=0, padx=1, pady=1)
# btnCAutoMixingIsFault = ctk.CTkButton(frmCAutoMixing, text="IsFault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
# btnCAutoMixingIsFault.grid(row=1, column=1, padx=1, pady=1)
# ------------
frmCAuto2 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto2.pack(padx=5, pady=(1, 1))
frmCAuto2.grid(row=1, column=0, padx=10, pady=1, sticky="w")

frmCAutoPneumToRotaryCnvyr = ctk.CTkFrame(frmCAuto2, fg_color="white")
frmCAutoPneumToRotaryCnvyr.grid(row=0, column=0, padx=1, pady=1)

imageCAutoPneumToRotaryCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','ConveyorDoor3Col.png'))
imageCAutoPneumToRotaryCnvyr = ctk.CTkImage(light_image=imageCAutoPneumToRotaryCnvyr, size=(240, 20))
CAutoPneumToRotaryCnvyrLbl = ctk.CTkLabel(frmCAutoPneumToRotaryCnvyr, image=imageCAutoPneumToRotaryCnvyr, text="")
CAutoPneumToRotaryCnvyrLbl.grid(row=0, column=0, columnspan=10, padx=1, pady=1)
btnCAutoPneumToRotaryCnvyr0DoClose = ctk.CTkButton(frmCAutoPneumToRotaryCnvyr, text="Close 3", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToRotaryCnvyr0DoClose.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumToRotaryCnvyr1DoClose = ctk.CTkButton(frmCAutoPneumToRotaryCnvyr, text="Close 2", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToRotaryCnvyr1DoClose.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumToRotaryCnvyr2DoClose = ctk.CTkButton(frmCAutoPneumToRotaryCnvyr, text="Close 1", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToRotaryCnvyr2DoClose.grid(row=1, column=2, padx=1, pady=1)

frmCAutoSensorRtaryUnitHop = ctk.CTkFrame(frmCAuto2, fg_color="white")
frmCAutoSensorRtaryUnitHop.grid(row=0, column=1, padx=1, pady=1)

imageCAutoSensorRtaryUnitHop = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','HopperRotary3Col.png'))
imageCAutoSensorRtaryUnitHop = ctk.CTkImage(light_image=imageCAutoSensorRtaryUnitHop, size=(240, 20))
CAutoSensorRtaryUnitHopLbl = ctk.CTkLabel(frmCAutoSensorRtaryUnitHop, image=imageCAutoSensorRtaryUnitHop, text="")
CAutoSensorRtaryUnitHopLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
btnCAutoPneumSensorRtaryUnitHop0IsOn = ctk.CTkButton(frmCAutoSensorRtaryUnitHop, text="IsMany 3", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRtaryUnitHop0IsOn.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumSensorRtaryUnitHop1IsOn = ctk.CTkButton(frmCAutoSensorRtaryUnitHop, text="IsMany 2", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRtaryUnitHop1IsOn.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumSensorRtaryUnitHop2IsOn = ctk.CTkButton(frmCAutoSensorRtaryUnitHop, text="IsMany 1", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRtaryUnitHop2IsOn.grid(row=1, column=2, padx=1, pady=1)


# ------------
frmCAuto3 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto3.pack(padx=5, pady=(1, 1))
frmCAuto3.grid(row=2, column=0, padx=10, pady=1, sticky="w")
# ------------

frmCAutoMotorFrmRtaryCnvyr = ctk.CTkFrame(frmCAuto3, fg_color="white")
frmCAutoMotorFrmRtaryCnvyr.grid(row=0, column=1, padx=1, pady=1)

imageCAutoMotorFrmRtaryCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorFrmRtaryCnvyr.png'))
imageCAutoMotorFrmRtaryCnvyr = ctk.CTkImage(light_image=imageCAutoMotorFrmRtaryCnvyr, size=(160, 20)) 
CAutoMotorFrmRtaryCnvyrLbl = ctk.CTkLabel(frmCAutoMotorFrmRtaryCnvyr, image=imageCAutoMotorFrmRtaryCnvyr, text="")
CAutoMotorFrmRtaryCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnCAutoMotorFrmRtaryCnvyrDoStart = ctk.CTkButton(frmCAutoMotorFrmRtaryCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorFrmRtaryCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorFrmRtaryCnvyrIsFault = ctk.CTkButton(frmCAutoMotorFrmRtaryCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorFrmRtaryCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

frmCAutoMotorUpladderCnvyr = ctk.CTkFrame(frmCAuto3, fg_color="white")
frmCAutoMotorUpladderCnvyr.grid(row=0, column=2, padx=1, pady=1)

imageCAutoMotorUpladderCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorUpladderCnvyr.png'))
imageCAutoMotorUpladderCnvyr = ctk.CTkImage(light_image=imageCAutoMotorUpladderCnvyr, size=(160, 20)) 
CAutoMotorUpladderCnvyrLbl = ctk.CTkLabel(frmCAutoMotorUpladderCnvyr, image=imageCAutoMotorUpladderCnvyr, text="")
CAutoMotorUpladderCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnCAutoMotorUpladderCnvyrDoStart = ctk.CTkButton(frmCAutoMotorUpladderCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorUpladderCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorUpladderCnvyrIsFault = ctk.CTkButton(frmCAutoMotorUpladderCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorUpladderCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)

frmCAutoMotorToHopperCnvyr = ctk.CTkFrame(frmCAuto3, fg_color="white")
frmCAutoMotorToHopperCnvyr.grid(row=0, column=3, padx=1, pady=1)

imageCAutoMotorToHopperCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','MotorToHopperCnvyr.png'))
imageCAutoMotorToHopperCnvyr = ctk.CTkImage(light_image=imageCAutoMotorToHopperCnvyr, size=(160, 20)) 
CAutoMotorToHopperCnvyrLbl = ctk.CTkLabel(frmCAutoMotorToHopperCnvyr, image=imageCAutoMotorToHopperCnvyr, text="")
CAutoMotorToHopperCnvyrLbl.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
btnCAutoMotorToHopperCnvyrDoStart = ctk.CTkButton(frmCAutoMotorToHopperCnvyr, text="Start", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorToHopperCnvyrDoStart.grid(row=1, column=0, padx=1, pady=1)
btnCAutoMotorToHopperCnvyrIsFault = ctk.CTkButton(frmCAutoMotorToHopperCnvyr, text="Fault", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoMotorToHopperCnvyrIsFault.grid(row=1, column=1, padx=1, pady=1)
# ------------

frmCAuto4 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto4.pack(padx=5, pady=(1, 1))
frmCAuto4.grid(row=3, column=0, padx=10, pady=1, sticky="w")
# ------------
frmCAutoPneumToHopperCnvyr = ctk.CTkFrame(frmCAuto4, fg_color="white")
frmCAutoPneumToHopperCnvyr.grid(row=0, column=0, padx=1, pady=1)

imageCAutoPneumToHopperCnvyr = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','DoorSilo5Col.png'))
imageCAutoPneumToHopperCnvyr = ctk.CTkImage(light_image=imageCAutoPneumToHopperCnvyr, size=(400, 20)) 
CAutoPneumToHopperCnvyrLbl = ctk.CTkLabel(frmCAutoPneumToHopperCnvyr, image=imageCAutoPneumToHopperCnvyr, text="")
CAutoPneumToHopperCnvyrLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
btnCAutoPneumToHopperCnvyr0DoClose = ctk.CTkButton(frmCAutoPneumToHopperCnvyr, text="Close 5", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToHopperCnvyr0DoClose.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumToHopperCnvyr1DoClose = ctk.CTkButton(frmCAutoPneumToHopperCnvyr, text="Close 4", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToHopperCnvyr1DoClose.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumToHopperCnvyr2DoClose = ctk.CTkButton(frmCAutoPneumToHopperCnvyr, text="Close 3", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToHopperCnvyr2DoClose.grid(row=1, column=2, padx=1, pady=1)
btnCAutoPneumToHopperCnvyr3DoClose = ctk.CTkButton(frmCAutoPneumToHopperCnvyr, text="Close 2", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToHopperCnvyr3DoClose.grid(row=1, column=3, padx=1, pady=1)
btnCAutoPneumToHopperCnvyr4DoClose = ctk.CTkButton(frmCAutoPneumToHopperCnvyr, text="Close 1", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumToHopperCnvyr4DoClose.grid(row=1, column=4, padx=1, pady=1)

frmCAutoSensorTabletVaryHop = ctk.CTkFrame(frmCAuto4, fg_color="white")
frmCAutoSensorTabletVaryHop.grid(row=0, column=1, padx=1, pady=1)

imageCAutoSensorTabletVaryHop = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SensorSilo5Col.png'))
imageCAutoSensorTabletVaryHop = ctk.CTkImage(light_image=imageCAutoSensorTabletVaryHop, size=(400, 20)) 
CAutoSensorTabletVaryHopLbl = ctk.CTkLabel(frmCAutoSensorTabletVaryHop, image=imageCAutoSensorTabletVaryHop, text="")
CAutoSensorTabletVaryHopLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
btnCAutoPneumSensorTabletVaryHop0IsOn = ctk.CTkButton(frmCAutoSensorTabletVaryHop, text="IsMany 0", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorTabletVaryHop0IsOn.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumSensorTabletVaryHop1IsOn = ctk.CTkButton(frmCAutoSensorTabletVaryHop, text="IsMany 1", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorTabletVaryHop1IsOn.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumSensorTabletVaryHop2IsOn = ctk.CTkButton(frmCAutoSensorTabletVaryHop, text="IsMany 2", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorTabletVaryHop2IsOn.grid(row=1, column=2, padx=1, pady=1)
btnCAutoPneumSensorTabletVaryHop3IsOn = ctk.CTkButton(frmCAutoSensorTabletVaryHop, text="IsMany 3", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorTabletVaryHop3IsOn.grid(row=1, column=3, padx=1, pady=1)
btnCAutoPneumSensorTabletVaryHop4IsOn = ctk.CTkButton(frmCAutoSensorTabletVaryHop, text="IsMany 4", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorTabletVaryHop4IsOn.grid(row=1, column=4, padx=1, pady=1)
# ------------
frmCAuto5 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto5.pack(padx=5, pady=(1, 1))
frmCAuto5.grid(row=5, column=0, padx=10, pady=1, sticky="w")
# ------------
frmCAutoPneumTbletHoprDoor = ctk.CTkFrame(frmCAuto5, fg_color="white")
frmCAutoPneumTbletHoprDoor.grid(row=0, column=0, padx=1, pady=1)

imageCAutoPneumTbletHoprDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SiloDoor9Col.png'))
imageCAutoPneumTbletHoprDoor = ctk.CTkImage(light_image=imageCAutoPneumTbletHoprDoor, size=(720, 20)) 
CAutoPneumTbletHoprDoorLbl = ctk.CTkLabel(frmCAutoPneumTbletHoprDoor, image=imageCAutoPneumTbletHoprDoor, text="")
CAutoPneumTbletHoprDoorLbl.grid(row=0, column=0, columnspan=9, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor0IsOpen = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Open 5", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor0IsOpen.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor0IsClose = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Close 5", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor0IsClose.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor0IsFault = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Fault 5", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor0IsFault.grid(row=1, column=2, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor1IsOpen = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Open 4", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor1IsOpen.grid(row=1, column=3, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor1IsClose = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Close 4", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor1IsClose.grid(row=1, column=4, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor1IsFault = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Fault 4", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor1IsFault.grid(row=1, column=5, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor2IsOpen = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Open 3", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor2IsOpen.grid(row=1, column=6, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor2IsClose = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Close 3", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor2IsClose.grid(row=1, column=7, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor2IsFault = ctk.CTkButton(frmCAutoPneumTbletHoprDoor, text="Fault 3", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor2IsFault.grid(row=1, column=8, padx=1, pady=1)
# ------------
frmCAuto6 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto6.pack(padx=5, pady=(1, 1))
frmCAuto6.grid(row=6, column=0, padx=10, pady=1, sticky="w")
# ------------
frmCAutoPneumTbletHoprDoor2 = ctk.CTkFrame(frmCAuto6, fg_color="white")
frmCAutoPneumTbletHoprDoor2.grid(row=0, column=0, padx=1, pady=1)

imageCAutoMotorTbletHoprDoor = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SiloDoor6Col.png'))
imageCAutoMotorTbletHoprDoor = ctk.CTkImage(light_image=imageCAutoMotorTbletHoprDoor, size=(480, 20)) 
CAutoMotorTbletHoprDoorLbl = ctk.CTkLabel(frmCAutoPneumTbletHoprDoor2, image=imageCAutoMotorTbletHoprDoor, text="")
CAutoMotorTbletHoprDoorLbl.grid(row=0, column=0, columnspan=6, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor3IsOpen = ctk.CTkButton(frmCAutoPneumTbletHoprDoor2, text="Open 2", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor3IsOpen.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor3IsClose = ctk.CTkButton(frmCAutoPneumTbletHoprDoor2, text="Close 2", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor3IsClose.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor3IsFault = ctk.CTkButton(frmCAutoPneumTbletHoprDoor2, text="Fault 2", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor3IsFault.grid(row=1, column=2, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor4IsOpen = ctk.CTkButton(frmCAutoPneumTbletHoprDoor2, text="Open 1", text_color="black", fg_color="red", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor4IsOpen.grid(row=1, column=3, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor4IsClose = ctk.CTkButton(frmCAutoPneumTbletHoprDoor2, text="Close 1", text_color="black", fg_color="lime", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor4IsClose.grid(row=1, column=4, padx=1, pady=1)
btnCAutoPneumTbletHoprDoor4IsFault = ctk.CTkButton(frmCAutoPneumTbletHoprDoor2, text="Fault 1", text_color="black", fg_color="orange", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumTbletHoprDoor4IsFault.grid(row=1, column=5, padx=1, pady=1)

# ------------
frmCAuto7 = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="white")
# frmCAuto7.pack(padx=5, pady=(1, 1))
frmCAuto7.grid(row=7, column=0, padx=10, pady=1, sticky="w")
# ------------

frmCAutoSensorRncenMachHop = ctk.CTkFrame(frmCAuto7, fg_color="white")
frmCAutoSensorRncenMachHop.grid(row=0, column=0, padx=1, pady=1)

imageCAutoSensorRncenMachHop = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'BAutoLabel','SensorRncenMachHop5Col.png'))
imageCAutoSensorRncenMachHop = ctk.CTkImage(light_image=imageCAutoSensorRncenMachHop, size=(400, 20)) 
CAutoSensorRncenMachHopLbl = ctk.CTkLabel(frmCAutoSensorRncenMachHop, image=imageCAutoSensorRncenMachHop, text="")
CAutoSensorRncenMachHopLbl.grid(row=0, column=0, columnspan=5, padx=1, pady=1)
btnCAutoPneumSensorRncenMachHop0IsOn = ctk.CTkButton(frmCAutoSensorRncenMachHop, text="IsMany 0", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRncenMachHop0IsOn.grid(row=1, column=0, padx=1, pady=1)
btnCAutoPneumSensorRncenMachHop1IsOn = ctk.CTkButton(frmCAutoSensorRncenMachHop, text="IsMany 1", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRncenMachHop1IsOn.grid(row=1, column=1, padx=1, pady=1)
btnCAutoPneumSensorRncenMachHop2IsOn = ctk.CTkButton(frmCAutoSensorRncenMachHop, text="IsMany 2", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRncenMachHop2IsOn.grid(row=1, column=2, padx=1, pady=1)
btnCAutoPneumSensorRncenMachHop3IsOn = ctk.CTkButton(frmCAutoSensorRncenMachHop, text="IsMany 3", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRncenMachHop3IsOn.grid(row=1, column=3, padx=1, pady=1)
btnCAutoPneumSensorRncenMachHop4IsOn = ctk.CTkButton(frmCAutoSensorRncenMachHop, text="IsMany 4", text_color="black", fg_color="yellow", border_color="light grey", border_width=5, width=lampWidth, height=lampHeight)
btnCAutoPneumSensorRncenMachHop4IsOn.grid(row=1, column=4, padx=1, pady=1)  

# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabBesarCAuto, fg_color="transparent")
frm_MenuBawah.grid(row=8, column=0, padx=1, pady=(107,0), sticky="w")

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1, state="normal")
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU













# ================================================================================
# LINE C - UI UX - AUTO 2/2 .cauto2
# ================================================================================

# Membuka gambar dan mengubah ukurannya
img = Image.open(os.path.join(os.path.dirname(__file__), 'img', 'AutoC22.png'))  # Ganti dengan path gambar yang ingin kamu gunakan
resized_img = img.resize((1000, 242))  # Atur ukuran sesuai kebutuhan

# Konversi gambar agar bisa digunakan dalam tkinter
ctk_imageAutoC = ctk.CTkImage(resized_img, size=(1000, 242))

frame_tabAutoLineC22 = ctk.CTkFrame(app, fg_color="white")
frame_tabAutoLineC22.pack(fill="both", expand=True)

# START MatCol Line C
frm_MatColC = ctk.CTkFrame(frame_tabAutoLineC22, fg_color="white")
frm_MatColC.grid(row=0, column=0, padx=1, pady=1)

lbl_MatColC = ctk.CTkLabel(frm_MatColC, text="Material Color", font=('Helvetica', 16))
lbl_MatColC.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarnaC = ctk.CTkFrame(frm_MatColC)
frm_BtnWarnaC.grid(row=1, column=0, columnspan=5, pady=1)

btnAutoFeedPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="light green", text_color="white", border_color="black", border_width=5,
                                command=cmdBtnFeederCPutih, height=btnSize)
btnAutoFeedPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))
# if globals()['V0146'] == 512:
#     btnAutoFeedPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="lime", text_color="black", border_color="black", border_width=5,
#                                      height=btnSize)
#     btnAutoFeedPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))
# else:

btnAutoFeedWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                command=cmdBtnFeederCWarna1, height=btnSize)
btnAutoFeedWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))
# if globals()['V0146'] == 256:
#     btnAutoFeedWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                      height=btnSize)
#     btnAutoFeedWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))
# else:

btnAutoFeedWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                command=cmdBtnFeederCWarna2, height=btnSize)
btnAutoFeedWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))
# if globals()['V0146'] == 128:
#     btnAutoFeedWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                     height=btnSize)
#     btnAutoFeedWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))
# else:

btnAutoFeedWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                command=cmdBtnFeederCWarna3, height=btnSize)
btnAutoFeedWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))
# if globals()['V0146'] == 64:
#     btnAutoFeedWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                      height=btnSize)
#     btnAutoFeedWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))
# else:

btnAutoFeedWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                command=cmdBtnFeederCWarna4, height=btnSize)
btnAutoFeedWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))
# if globals()['V0146'] == 32:
#     btnAutoFeedWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                      height=btnSize)
#     btnAutoFeedWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))
# else:

btnManFeedManualC = ctk.CTkButton(frm_MatColC, text="Manual", fg_color="red", border_color="black", border_width=5,
                                 command=cmdBtnFeederCManual, height=btnSize)
btnManFeedManualC.grid(row=1, column=5, padx=20, pady=(10, 10))
# END MatCol
# START ProdType
frm_ProdTypeC = ctk.CTkFrame(frame_tabAutoLineC22, fg_color="white")
frm_ProdTypeC.grid(row=1, column=0, padx=1, pady=1)

lbl_ProdTypeC = ctk.CTkLabel(frm_ProdTypeC, text="Product Type", font=('Helvetica', 16))
lbl_ProdTypeC.grid(row=0, column=0, columnspan=6, pady=1)

frm_BtnWarnaC = ctk.CTkFrame(frm_ProdTypeC)
frm_BtnWarnaC.grid(row=1, column=0, columnspan=5, pady=1)

btnAutoHopperPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="light green", border_color="black", border_width=5,
                                command=cmdBtnHopperCPutih, height=btnSize)
btnAutoHopperPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))
# if globals()['V0147'] == 16:
#     btnAutoHopperPutihC = ctk.CTkButton(frm_BtnWarnaC, text="Putih", fg_color="lime", text_color="white", border_color="black", border_width=5,
#                                      height=btnSize)
#     btnAutoHopperPutihC.grid(row=1, column=0, padx=5, pady=(10, 10))
# else:

btnAutoHopperWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnHopperCWarna1, height=btnSize)
btnAutoHopperWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))
# if globals()['V0147'] == 8:
#     btnAutoHopperWarna1C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 1", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                         height=btnSize)
#     btnAutoHopperWarna1C.grid(row=1, column=1, padx=5, pady=(10, 10))
# else:

btnAutoHopperWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                command=cmdBtnHopperCWarna2, height=btnSize)
btnAutoHopperWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))
# if globals()['V0147'] == 4:
#     btnAutoHopperWarna2C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 2", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                          height=btnSize)
#     btnAutoHopperWarna2C.grid(row=1, column=2, padx=5, pady=(10, 10))
# else:

btnAutoHopperWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnHopperCWarna3, height=btnSize)
btnAutoHopperWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))
# if globals()['V0147'] == 2:
#     btnAutoHopperWarna3C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 3", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                          height=btnSize)
#     btnAutoHopperWarna3C.grid(row=1, column=3, padx=5, pady=(10, 10))
# else:

btnAutoHopperWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="pink", text_color="white", border_color="black", border_width=5,
                                    command=cmdBtnHopperCWarna4, height=btnSize)
btnAutoHopperWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))
# if globals()['V0147'] == 1:
#     btnAutoHopperWarna4C = ctk.CTkButton(frm_BtnWarnaC, text="Warna 4", fg_color="red", text_color="black", border_color="black", border_width=5,
#                                          height=btnSize)
#     btnAutoHopperWarna4C.grid(row=1, column=4, padx=5, pady=(10, 10))
# else:

btnManHopperManualC = ctk.CTkButton(frm_ProdTypeC, text="Manual", fg_color="red", border_color="black", border_width=5,
                                   command=cmdBtnFeederCManual, height=btnSize)
btnManHopperManualC.grid(row=1, column=5, padx=20, pady=(10, 10))
# END ProdType

frm_BesarC3LineBawah = ctk.CTkFrame(frame_tabAutoLineC22, fg_color="white")
frm_BesarC3LineBawah.grid(row=2, column=0, padx=10, pady=1)

label_with_image = ctk.CTkLabel(frm_BesarC3LineBawah, image=ctk_imageAutoC, text="")  # Kosongkan teks agar hanya gambar yang tampil
label_with_image.pack(pady=(1,0))


# Membuat frame untuk border
frame_with_border2234 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border2234.grid(row=0, column=0, padx=(740,0), pady=(1, 155))

lbl_ToHopperCnvyr = ctk.CTkLabel(frame_with_border2234, text="Conveyor ToSilo", font=('Helvetica', 7))
lbl_ToHopperCnvyr.grid(row=0, column=0,padx=2, pady=2)

frame_with_border21 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border21.grid(row=0, column=0, padx=(950,0), pady=(1, 480))

lbl_TbletHoprDoor0 = ctk.CTkLabel(frame_with_border21, text="Door Silo 5", font=('Helvetica', 7))
lbl_TbletHoprDoor0.grid(row=0, column=0, padx=2, pady=2)

frame_with_border20 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border20.grid(row=0, column=0, padx=(820,0), pady=(1, 480))

lbl_TbletHoprDoor1 = ctk.CTkLabel(frame_with_border20, text="Door Silo 4", font=('Helvetica', 7))
lbl_TbletHoprDoor1.grid(row=0, column=0,padx=2, pady=2)

frame_with_border19 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border19.grid(row=0, column=0, padx=(690,0), pady=(1, 480))

lbl_TbletHoprDoor2 = ctk.CTkLabel(frame_with_border19, text="Door Silo 3", font=('Helvetica', 7))
lbl_TbletHoprDoor2.grid(row=0, column=0, padx=2, pady=2)

frame_with_border18 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border18.grid(row=0, column=0, padx=(560,0), pady=(1, 480))

lbl_TbletHoprDoor3 = ctk.CTkLabel(frame_with_border18, text="Door Silo 2", font=('Helvetica', 7))
lbl_TbletHoprDoor3.grid(row=0, column=0,padx=2, pady=2)

frame_with_border188 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border188.grid(row=0, column=0, padx=(430,0), pady=(1, 480))

lbl_TbletHoprDoor4 = ctk.CTkLabel(frame_with_border188, text="Door Silo 1", font=('Helvetica', 7))
lbl_TbletHoprDoor4.grid(row=0, column=0,padx=2, pady=2)

btnTbltHoprDoor0C = ctk.CTkButton(label_with_image, text="Close", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor0C.grid(row=0, column=0, padx=(950,0), pady=(1, 410))

btnTbltHoprDoor1C = ctk.CTkButton(label_with_image, text="Close", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor1C.grid(row=0, column=0, padx=(820,0), pady=(1, 410))

btnTbltHoprDoor2C = ctk.CTkButton(label_with_image, text="Close", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor2C.grid(row=0, column=0, padx=(690,0), pady=(1, 410))

btnTbltHoprDoor3C = ctk.CTkButton(label_with_image, text="Close", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor3C.grid(row=0, column=0, padx=(560,0), pady=(1, 410))

btnTbltHoprDoor4C = ctk.CTkButton(label_with_image, text="Close", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltHoprDoor4C.grid(row=0, column=0, padx=(430,0), pady=(1, 410))

frame_with_border17 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border17.grid(row=0, column=0, padx=(950,0), pady=(1, 340))

lbl_RncenMachHop0 = ctk.CTkLabel(frame_with_border17, text="Sensor\nRncenMachHop 5", font=('Helvetica', 7))
lbl_RncenMachHop0.grid(row=0, column=0, padx=3, pady=2)

frame_with_border16 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border16.grid(row=0, column=0, padx=(820,0), pady=(1, 340))

lbl_RncenMachHop1 = ctk.CTkLabel(frame_with_border16, text="Sensor\nRncenMachHop 4", font=('Helvetica', 7))
lbl_RncenMachHop1.grid(row=0, column=0,padx=3, pady=2)

frame_with_border15 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border15.grid(row=0, column=0, padx=(690,0), pady=(1, 340))

lbl_RncenMachHop2 = ctk.CTkLabel(frame_with_border15, text="Sensor\nRncenMachHop 3", font=('Helvetica', 7))
lbl_RncenMachHop2.grid(row=0, column=0, padx=3, pady=2)

frame_with_border14 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border14.grid(row=0, column=0, padx=(560,0), pady=(1, 340))

lbl_RncenMachHop3 = ctk.CTkLabel(frame_with_border14, text="Sensor\nRncenMachHop 2", font=('Helvetica', 7))
lbl_RncenMachHop3.grid(row=0, column=0,padx=3, pady=2)

frame_with_border14 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border14.grid(row=0, column=0, padx=(430,0), pady=(1, 340))

lbl_RncenMachHop4 = ctk.CTkLabel(frame_with_border14, text="Sensor\nRncenMachHopp 1", font=('Helvetica', 7))
lbl_RncenMachHop4.grid(row=0, column=0,padx=3, pady=2)

btnTbltVaryHop0C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop0C.grid(row=0, column=0, padx=(950,0), pady=(1, 270))

btnTbltVaryHop1C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop1C.grid(row=0, column=0, padx=(820,0), pady=(1, 270))

btnTbltVaryHop2C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop2C.grid(row=0, column=0, padx=(690,0), pady=(1, 270))

btnTbltVaryHop3C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop3C.grid(row=0, column=0, padx=(560,0), pady=(1, 270))

btnTbltVaryHop4C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTbltVaryHop4C.grid(row=0, column=0, padx=(430,0), pady=(1, 270))

frame_with_border13 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border13.grid(row=0, column=0, padx=(330,0), pady=(1, 170))

lbl_UpLadderCnvyr = ctk.CTkLabel(frame_with_border13, text="Incline Conveyor", font=('Helvetica', 7))
lbl_UpLadderCnvyr.grid(row=0, column=0, padx=3, pady=2)

frame_with_border12 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border12.grid(row=0, column=0, padx=(0,150), pady=(1, 170))

lbl_FrmRtaryCnvyr = ctk.CTkLabel(frame_with_border12, text="Conveyor FrmRotary", font=('Helvetica', 7))
lbl_FrmRtaryCnvyr.grid(row=0, column=0,padx=3, pady=2)

btnUpLadderCnvyrC = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnUpLadderCnvyrC.grid(row=0, column=0, padx=(330,0), pady=(1, 90))

btnFrmRtaryCnvyrC = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnFrmRtaryCnvyrC.grid(row=0, column=0, padx=(0,150), pady=(1, 90))

btnToHopperCnvyrC = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyrC.grid(row=0, column=0, padx=(740,0), pady=(1, 90))


frame_with_border11 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border11.grid(row=0, column=0, padx=(950,0), pady=(50, 1))

lbl_ToHopperCnvyr0 = ctk.CTkLabel(frame_with_border11, text="Door Silo 5", font=('Helvetica', 7))
lbl_ToHopperCnvyr0.grid(row=0, column=0,padx=3, pady=2)

frame_with_border10 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border10.grid(row=0, column=0, padx=(820,0), pady=(50, 1))

lbl_ToHopperCnvyr1 = ctk.CTkLabel(frame_with_border10, text="Door Silo 4", font=('Helvetica', 7))
lbl_ToHopperCnvyr1.grid(row=0, column=0, padx=3, pady=2)

frame_with_border101 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border101.grid(row=0, column=0, padx=(690,0), pady=(50, 1))

lbl_ToHopperCnvyr2 = ctk.CTkLabel(frame_with_border101, text="Door Silo 3", font=('Helvetica', 7))
lbl_ToHopperCnvyr2.grid(row=0, column=0, padx=3, pady=2)

frame_with_border102 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border102.grid(row=0, column=0, padx=(560,0), pady=(50, 1))

lbl_ToHopperCnvyr3 = ctk.CTkLabel(frame_with_border102, text="Door Silo 2", font=('Helvetica', 7))
lbl_ToHopperCnvyr3.grid(row=0, column=0, padx=3, pady=2)

frame_with_border103 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border103.grid(row=0, column=0, padx=(430,0), pady=(50, 1))

lbl_ToHopperCnvyr4 = ctk.CTkLabel(frame_with_border103, text="Door Silo 1", font=('Helvetica', 7))
lbl_ToHopperCnvyr4.grid(row=0, column=0, padx=3, pady=2)

btnToHopperCnvyr0C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyr0C.grid(row=0, column=0, padx=(950,0), pady=(120, 1))

btnToHopperCnvyr1C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyr1C.grid(row=0, column=0, padx=(820,0), pady=(120, 1))

btnToHopperCnvyr2C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyr2C.grid(row=0, column=0, padx=(690,0), pady=(120, 1))

btnToHopperCnvyr3C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyr3C.grid(row=0, column=0, padx=(560,0), pady=(120, 1))

btnToHopperCnvyr4C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToHopperCnvyr4C.grid(row=0, column=0, padx=(430,0), pady=(120, 1))

frame_with_border9 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border9.grid(row=0, column=0, padx=(950,0), pady=(190, 1))

lbl_TbltVaryHop0 = ctk.CTkLabel(frame_with_border9, text="Sensor\nSilo 5", font=('Helvetica', 7))
lbl_TbltVaryHop0.grid(row=0, column=0,padx=3, pady=2)

frame_with_border8 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border8.grid(row=0, column=0, padx=(820,0), pady=(190, 1))

lbl_TbltVaryHop1 = ctk.CTkLabel(frame_with_border8, text="Sensor\nSilo 4", font=('Helvetica', 7))
lbl_TbltVaryHop1.grid(row=0, column=0, padx=3, pady=2)

frame_with_border81 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border81.grid(row=0, column=0, padx=(690,0), pady=(190, 1))

lbl_TbltVaryHop2 = ctk.CTkLabel(frame_with_border81, text="Sensor\nSilo 3", font=('Helvetica', 7))
lbl_TbltVaryHop2.grid(row=0, column=0, padx=3, pady=2)

frame_with_border82 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border82.grid(row=0, column=0, padx=(560,0), pady=(190, 1))

lbl_TbltVaryHop3 = ctk.CTkLabel(frame_with_border82, text="Sensor\nSilo 2", font=('Helvetica', 7))
lbl_TbltVaryHop3.grid(row=0, column=0, padx=3, pady=2)

frame_with_border83 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border83.grid(row=0, column=0, padx=(430,0), pady=(190, 1))

lbl_TbltVaryHop4 = ctk.CTkLabel(frame_with_border83, text="Sensor\nSilo 1", font=('Helvetica', 7))
lbl_TbltVaryHop4.grid(row=0, column=0, padx=3, pady=2)

btnTabletVaryHop0C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTabletVaryHop0C.grid(row=0, column=0, padx=(950,0), pady=(260, 1))

btnTabletVaryHop1C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTabletVaryHop1C.grid(row=0, column=0, padx=(820,0), pady=(260, 1))

btnTabletVaryHop2C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTabletVaryHop2C.grid(row=0, column=0, padx=(690,0), pady=(260, 1))

btnTabletVaryHop3C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTabletVaryHop3C.grid(row=0, column=0, padx=(560,0), pady=(260, 1))

btnTabletVaryHop4C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnTabletVaryHop4C.grid(row=0, column=0, padx=(430,0), pady=(260, 1))

frame_with_border7 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border7.grid(row=0, column=0,padx=(190,0), pady=(100,1))

lbl_ToRotaryCnvyr0 = ctk.CTkLabel(frame_with_border7, text="Conveyor Door 3", font=('Helvetica', 7))
lbl_ToRotaryCnvyr0.grid(row=0, column=0,padx=3, pady=2)

frame_with_border5 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border5.grid(row=0, column=0,padx=(0,140), pady=(100,1))

lbl_ToRotaryCnvyr1 = ctk.CTkLabel(frame_with_border5, text="Conveyor Door 2", font=('Helvetica', 7))
lbl_ToRotaryCnvyr1.grid(row=0, column=0,padx=3, pady=2)

frame_with_border4 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border4.grid(row=0, column=0, padx=(0,420), pady=(100,1))

lbl_ToRotaryCnvyr2 = ctk.CTkLabel(frame_with_border4, text="Conveyor Door 1", font=('Helvetica', 7))
lbl_ToRotaryCnvyr2.grid(row=0, column=0, padx=3, pady=2)

btnToRotaryCnvyr0C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr0C.grid(row=0, column=0, padx=(190,0), pady=(170,1))

btnToRotaryCnvyr1C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr1C.grid(row=0, column=0, padx=(0,140), pady=(170,1))

btnToRotaryCnvyr2C = ctk.CTkButton(label_with_image, text="Close", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnToRotaryCnvyr2C.grid(row=0, column=0, padx=(0,420), pady=(170,1))



frame_with_border77 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border77.grid(row=0, column=0,padx=(190,0), pady=(240,1))

lbl_RtaryUnitHop0 = ctk.CTkLabel(frame_with_border77, text="Hopper Rotary 3", font=('Helvetica', 7))
lbl_RtaryUnitHop0.grid(row=0, column=0,padx=3, pady=2)


frame_with_border55 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border55.grid(row=0, column=0,padx=(0,140), pady=(240,1))

lbl_RtaryUnitHop1 = ctk.CTkLabel(frame_with_border55, text="Hopper Rotary 2", font=('Helvetica', 7))
lbl_RtaryUnitHop1.grid(row=0, column=0,padx=3, pady=2)

frame_with_border44 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border44.grid(row=0, column=0, padx=(0,420), pady=(240,1))

lbl_RtaryUnitHop2 = ctk.CTkLabel(frame_with_border44, text="Hopper Rotary 1", font=('Helvetica', 7))
lbl_RtaryUnitHop2.grid(row=0, column=0, padx=3, pady=2)

btnRtaryUnitHop0C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop0C.grid(row=0, column=0, padx=(190,0), pady=(310,1))

btnRtaryUnitHop1C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop1C.grid(row=0, column=0, padx=(0,140), pady=(310,1))

btnRtaryUnitHop3C = ctk.CTkButton(label_with_image, text="IsMany", fg_color="yellow", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnRtaryUnitHop3C.grid(row=0, column=0, padx=(0,420), pady=(310,1))


frame_with_border00 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border00.grid(row=0, column=0, padx=(0,520), pady=(0,50))

lbl_ToRotaryCnvyr1 = ctk.CTkLabel(frame_with_border00, text="Conveyor ToRotary", font=('Helvetica', 7))
lbl_ToRotaryCnvyr1.grid(row=0, column=0, padx=3, pady=2)

frame_with_border312 = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border312.grid(row=0, column=0,padx=(0,770), pady=(0,30))

lbl_MatScrewCnvyr1 = ctk.CTkLabel(frame_with_border312, text="Motor Screw", font=('Helvetica', 7))
lbl_MatScrewCnvyr1.grid(row=0, column=0,padx=3, pady=2)

btnMotorToRotaryCnvyrC = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorToRotaryCnvyrC.grid(row=0, column=0, padx=(0,520), pady=(20,1))

btnMotorMatScrewCnvyrC = ctk.CTkButton(label_with_image, text="Rev", fg_color="red", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMotorMatScrewCnvyrC.grid(row=0, column=0, padx=(0,770), pady=(40,1))



frame_with_border4p = ctk.CTkFrame(label_with_image, corner_radius=0, border_width=1, border_color='black', fg_color="white")
frame_with_border4p.grid(row=0, column=0,padx=(0,950), pady=(0,30))

lbl_MateriVbrator = ctk.CTkLabel(frame_with_border4p, text="Motor Osciliating", font=('Helvetica', 7))
lbl_MateriVbrator.grid(row=0, column=0,padx=3, pady=2)

btnMateriVbratorC = ctk.CTkButton(label_with_image, text="Start", fg_color="lime", text_color="black",
                          border_color="gray", border_width=5, width=40, height=15)
btnMateriVbratorC.grid(row=0, column=0, padx=(0,950), pady=(40,1))



# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_tabAutoLineC22, fg_color="transparent")
frm_MenuBawah.grid(row=5, column=0, padx=(0,1), pady=(0,1), sticky="ew")

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2, state="normal")
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC)
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU




# ================================================================================
# LINE C - UI UX - SET C - .cset
# ================================================================================

frame_SetAutoC = ctk.CTkFrame(app, fg_color="white")
frame_SetAutoC.pack(fill="both", expand=True)

main_frame = ctk.CTkFrame(frame_SetAutoC, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=10, pady=0)

# Frame container untuk area di sebelah kiri
area_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
area_frame.pack(side="left", anchor="nw", padx=10, pady=0)

# Membuat frame container untuk area baris pertama (judul 1-4)
row1_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row1_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris pertama secara horizontal

# Membuat area frame untuk judul 1-4 di baris pertama
create_area_frame(row1_frame, "Pneum MaterMixDoor", "V0032")
create_area_frame(row1_frame, "Pneum TbletHoprDoor 0", "V0033")
create_area_frame(row1_frame, "Pneum TbletHoprDoor 1", "V0034")
create_area_frame(row1_frame, "Pneum TbletHoprDoor 2", "V0035")

# Membuat frame container untuk area baris kedua (judul 5-8)
row2_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row2_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris kedua di bawah baris pertama

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row2_frame, "Pneum TbletHoprDoor 3", "V0036")
create_area_frame(row2_frame, "Pneum TbletHoprDoor 4", "V0037")
create_area_frame(row2_frame, "Sensor RtaryUnitHop 0", "V0048")
create_area_frame(row2_frame, "Sensor RtaryUnitHop 1", "V0049")

# Membuat frame container untuk area baris kedua (judul 5-8)
row3_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row3_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris kedua di bawah baris pertama

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row3_frame, "Sensor RtaryUnitHop 2", "V0050")
create_area_frame(row3_frame, "Sensor TabletVaryHop 0", "V0051")
create_area_frame(row3_frame, "Sensor TabletVaryHop 1", "V0052")
create_area_frame(row3_frame, "Sensor TabletVaryHop 2", "V0053")

# Membuat frame container untuk area baris kedua (judul 5-8)
row4_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row4_frame.pack(side="top", anchor="nw", pady=0)  # Menyusun frame untuk baris kedua di bawah baris pertama

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row4_frame, "Sensor TabletVaryHop 3", "V0054")
create_area_frame(row4_frame, "Sensor TabletVaryHop 4", "V0055")
create_area_frame(row4_frame, "Sensor RncenmachHop 0", "V0056")
create_area_frame(row4_frame, "Sensor RncenmachHop 1", "V0057")

row5_frame = ctk.CTkFrame(area_frame,  fg_color="transparent")
row5_frame.pack(side="top", anchor="nw", pady=0)

# Membuat area frame untuk judul 5-8 di baris kedua
create_area_frame(row5_frame, "Sensor RncenmachHop 2", "V0058")
create_area_frame(row5_frame, "Sensor RncenmachHop 3", "V0059")
create_area_frame(row5_frame, "Sensor RncenmachHop 4", "V0060")
create_area_frame(row5_frame, "Mixing", "V0043")


# Frame untuk kalkulator di sebelah kanan
calculator_frame = ctk.CTkFrame(main_frame, width=330, height=410, corner_radius=10, fg_color="gray")
calculator_frame.pack(side="right", anchor="ne", padx=10, pady=120)

# Baris pertama: /, *, -, <-
row1_buttons = ["/", "*", "-", "←"]
for i, text in enumerate(row1_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=0, column=i, padx=7.5, pady=7.5, sticky="nsew")  # Menggunakan grid untuk penempatan

# Baris kedua: 7, 8, 9, +
row2_buttons = ["7", "8", "9"]
for i, text in enumerate(row2_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=1, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Tombol + yang menggabungkan baris kedua dan ketiga
button_plus = ctk.CTkButton(calculator_frame, text="+", command=lambda: on_calculator_button_click("+"), width=60, height=125, fg_color="white", text_color="black", font=("Helvetica", 24))
button_plus.grid(row=1, column=3, rowspan=2, padx=7.5, pady=7.5, sticky="nsew")

# Baris ketiga: 4, 5, 6
row3_buttons = ["4", "5", "6"]
for i, text in enumerate(row3_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=2, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Baris keempat: 1, 2, 3
row4_buttons = ["1", "2", "3"]
for i, text in enumerate(row4_buttons):
    button = ctk.CTkButton(calculator_frame, text=text, command=lambda t=text: on_calculator_button_click(t), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
    button.grid(row=3, column=i, padx=7.5, pady=7.5, sticky="nsew")

# Menggabungkan tombol Backspace ke baris keempat dan kelima
button_backspace = ctk.CTkButton(calculator_frame, text="↵", command=lambda: on_calculator_button_click("↵"), width=60, height=125, fg_color="white", text_color="black", font=("Helvetica", 24))
button_backspace.grid(row=3, column=3, rowspan=2, padx=7.5, pady=7.5, sticky="nsew")

# Baris kelima: 0, .
button_zero = ctk.CTkButton(calculator_frame, text="0", command=lambda: on_calculator_button_click("0"), width=125, height=60, fg_color="white", text_color="black", font=("Helvetica", 24))
button_zero.grid(row=4, column=0, columnspan=2, padx=7.5, pady=7.5, sticky="nsew")

button_dot = ctk.CTkButton(calculator_frame, text=".", command=lambda: on_calculator_button_click("."), width=60, height=60, fg_color="white", text_color="black", font=("Helvetica", 44))
button_dot.grid(row=4, column=2, padx=7.5, pady=7.5, sticky="nsew")


# START Button MENU
frm_MenuBawah = ctk.CTkFrame(frame_SetAutoC, fg_color="transparent")
frm_MenuBawah.pack(side="bottom", anchor="s", fill="x", pady=0)

btnAutoMenuCommon = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto)
btnAutoMenuCommon.grid(row=1, column=0, padx=1, pady=1)

btnAutoMenuCommon2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nCommon(Z)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                              border_color="black", border_width=5, width=84, height=55, command=showCommonAuto2)
btnAutoMenuCommon2.grid(row=1, column=1, padx=1, pady=1)

btnAutoKecilA1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA1.grid(row=1, column=2, padx=1, pady=1)

btnAutoKecilA2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nKecil(A)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55)
btnAutoKecilA2.grid(row=1, column=3, padx=1, pady=1)

btnAutoBesarB1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB1)
btnAutoBesarB1.grid(row=1, column=4, padx=1, pady=1)

btnAutoBesarB2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBesar(B)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                           border_color="black", border_width=5, width=84, height=55, command=showAutoBesarB2)
btnAutoBesarB2.grid(row=1, column=5, padx=1, pady=1)

btnAutoBolaC1 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n1/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC1)
btnAutoBolaC1.grid(row=1, column=7, padx=1, pady=1)

btnAutoBolaC2 = ctk.CTkButton(frm_MenuBawah, text="Auto\nBola(C)\n2/2", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoBesarC2)
btnAutoBolaC2.grid(row=1, column=8, padx=1, pady=1)

btnAutoSetCommon = ctk.CTkButton(frm_MenuBawah, text="Set\nCommon(Z)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetZ)
btnAutoSetCommon.grid(row=1, column=10, padx=1, pady=1)

btnAutoSetKecilA = ctk.CTkButton(frm_MenuBawah, text="Set\nKecil(A)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55)
btnAutoSetKecilA.grid(row=1, column=11, padx=1, pady=1)

btnAutoSetBesarB = ctk.CTkButton(frm_MenuBawah, text="Set\nBesar(B)", font=("Arial", 10), fg_color="light blue", text_color="blue",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetB)
btnAutoSetBesarB.grid(row=1, column=12, padx=1, pady=1)

btnAutoSetBolaC = ctk.CTkButton(frm_MenuBawah, text="Set\nBola(C)", font=("Arial", 10), fg_color="blue", text_color="white",
                          border_color="black", border_width=5, width=84, height=55, command=showAutoSetC, state="normal")
btnAutoSetBolaC.grid(row=1, column=13, padx=1, pady=1)
# END Button MENU










listenMongoThread = threading.Thread(target=listenMongo)
listenMongoThread.daemon = True
listenMongoThread.start()

app.bind("<ButtonPress>", on_touch)
app.bind("<ButtonRelease>", on_release)
check_touch_status()
showBolaB()




app.after(200, refreshGUI)
app.mainloop()