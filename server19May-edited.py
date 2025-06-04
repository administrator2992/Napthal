import customtkinter as ctk
from PIL import Image, ImageTk
import os
import threading
import datetime
import time
from bson.objectid import ObjectId
from pymongo import MongoClient, UpdateOne
import sys
import platform
import ctypes
import time
import signal

# Buat Variable I, J, V
for i in range(100):
    globals()[f'I000{str(i).zfill(2)}'] = False
for i in range(100, 257):
    globals()[f'I00{str(i).zfill(3)}'] = False

for i in range(100):
    globals()[f'J000{str(i).zfill(2)}'] = False
for i in range(100, 578):
    globals()[f'J00{str(i).zfill(3)}'] = False

for i in range(0, 9):
    globals()[f'V000{str(i).zfill(3)}'] = 0

for i in range(10, 99):
    globals()[f'V00{str(i).zfill(3)}'] = 0

for i in range(100, 192):
    globals()[f'V0{str(i).zfill(3)}'] = 0

threads = []
changed_keys = []
updated_queue = []
updated_var_names = []
autohistory = []

arrIntAuto = [False] * 28
timers = {}

firstBoot = True

# Variable Timer
K032 = False
K033 = False
K034 = False
K035 = False
K036 = False
K037 = False
U0032 = 0
U0033 = 0
U0034 = 0
U0035 = 0
U0036 = 0
U0037 = 0
K000V0000IsJam = False
K000V0000Start = 0
K001V0001IsJam = False
K001V0001Start = 0
K002V0002IsJam = False
K002V0002Start = 0
K032V0032IsJam = False
K032V0032Start = 0
K033V0033IsJam = False
K033V0033Start = 0
K034V0034IsJam = False
K034V0034Start = 0
K035V0035IsJam = False
K035V0035Start = 0
K036V0036IsJam = False
K036V0036Start = 0
K037V0037IsJam = False
K037V0037Start = 0
K064V0064IsJam = False
K064V0064Start = 0
K065V0065IsJam = False
K065V0065Start = 0
K043 = False
V0043 = 6
U0043 = 0
K043V0043Start = 0
K048 = False
V0048 = 6
U0048 = 0
K048V0048Start = 0
K049 = False
V0049 = 6
U0049 = 0
K049V0049Start = 0
K050 = False
V0050 = 6
U0050 = 0
K050V0050Start = 0
K051 = False
V0051 = 6
U0051 = 0
K051V0051Start = 0
K052 = False
V0052 = 6
U0052 = 0
K052V0052Start = 0
K053 = False
V0053 = 6
U0053 = 0
K053V0053Start = 0
K054 = False
V0054 = 6
U0054 = 0
K054V0054Start = 0
K055 = False
V0055 = 6
U0055 = 0
K055V0055Start = 0
K056 = False
V0056 = 6
U0056 = 0
K056V0056Start = 0
K057 = False
V0057 = 6
U0057 = 0
K057V0057Start = 0
K058 = False
V0058 = 6
U0058 = 0
K058V0058Start = 0
K059 = False
V0059 = 6
U0059 = 0
K059V0059Start = 0
K060s = False
V0060 = 6
U0060 = 0
K060V0060Start = 0
V0000 = 6
V0001 = 6
V0002 = 6
V0032 = 6
V0033 = 6
V0034 = 6
V0035 = 6
V0036 = 6
V0037 = 6
V0064 = 6
V0065 = 6

V0015 = 6
V0148 = 0


# Timer Line B
K011 = False
V0011 = 6
K016 = False
V0016 = 3
K017 = False
V0017 = 3
K018 = False
V0018 = 3
K019 = False
V0019 = 3
K020 = False
V0020 = 3
K021 = False
V0021 = 6
K022 = False
V0022 = 6
K023 = False
V0023 = 6
K024 = False
V0024 = 6
K025 = False
V0025 = 6
K026 = False
V0026 = 6

V0157ToPanelAlarmErrorSourcesZ0err = 0
V0159AlarmHoldOutputZ0err = 0  # AG8
V0158AlarmBuzrOutputZ0err = 0  # AG11

V0152 = "strtB0" # Fill RnCen Sequence Line B
V0153 = "strtB0" # Fill Rotary Sequence Line B
V0154 = "strtC0" # Fill Rotary Sequence Line C

queueToCall = []
queueToCallText = []

globals()['I00028'] = True
globals()['I00096'] = True
globals()['I00032'] = True
globals()['V0149'] = True

# # DIO RLY Setting
# YDU_RESULT_SUCCESS = 0
# YDU_OPEN_NORMAL = 0
# YDU_OPEN_OUT_NOT_INIT = 0x01

# pf = platform.system()
# if pf == 'Windows':
#     ydu = ctypes.windll.Ydu
# elif pf == 'Linux':
#     ydu = ctypes.CDLL('libydu.so')

# # Nomor ID DIO
# input_id = 0
# resInput = ydu.YduOpen(input_id, b'DIO-N128/00A-U', YDU_OPEN_NORMAL)
# # Nomor ID RLY
# output_id = 1
# resOutput = ydu.YduOpen(output_id, b'DIO-00/N128A-U', YDU_OPEN_NORMAL)

# if resInput != YDU_RESULT_SUCCESS:
#     print('DIO tidak terdeteksi')
#     sys.exit()

# if resOutput != YDU_RESULT_SUCCESS:
#     print('RLY tidak terdeteksi')
#     sys.exit()

qi0000glovar = (ctypes.c_ubyte * 128)()
qy0000output = (ctypes.c_ubyte * 128)()

globals()['I00028'] = True
globals()['I00096'] = True
globals()['I00032'] = True
globals()['V0149'] = True

# MongoDB Setting
client = MongoClient('mongodb://192.168.18.149:27017/')
# client = MongoClient('mongodb://localhost:27017/')
db_mongo = client['unitamaDB']
collection = db_mongo['napthalMachine']
objID = '68366b8cde0dc02539587580'

doc_antrian = collection.insert_one({})

def JQueue():
    return (
        [globals()[f"J{8 * group + offset:05d}"] for offset in range(8)]
        for group in range(16, 72)
    )

previous_jqueues = [jqueue[:] for jqueue in JQueue()]

def OQueue():
    return (
        [globals()[f"I{8 * group + offset:05d}"] for offset in range(8)]
        for group in range(128, 256)
    )

previous_oqueues = [oqueue[:] for oqueue in OQueue()]

def JlocalQueue():
    return (
        [globals()[f"J{8 * group + offset:05d}"] for offset in range(8)]
        for group in range(72)
    )

previous_localjqueues = [jqueue[:] for jqueue in JlocalQueue()]

def processQueue():
    updated_queue = []
    updated_var_names = []

    for jqueue_index, current_jqueue in enumerate(JQueue()):
        prev_jqueue = previous_jqueues[jqueue_index]
        for bit_index, (prev_val, curr_val) in enumerate(zip(prev_jqueue, current_jqueue)):
            if prev_val != curr_val:
                updated_queue.append((jqueue_index, bit_index))
                jqueue_index_real = 16 + jqueue_index
                global_index = 8 * jqueue_index_real + bit_index
                var_name = f"J{global_index:05d}"
                updated_var_names.append(var_name)

                previous_jqueues[jqueue_index][bit_index] = curr_val

    return updated_queue, updated_var_names

def localprocessQueue():
    updated_queue = []
    updated_var_names = []

    for jqueue_index, current_jqueue in enumerate(JlocalQueue()):
        prev_jqueue = previous_localjqueues[jqueue_index]
        for bit_index, (prev_val, curr_val) in enumerate(zip(prev_jqueue, current_jqueue)):
            if prev_val != curr_val:
                updated_queue.append((jqueue_index, bit_index))
                global_index = 8 * jqueue_index + bit_index
                var_name = f"J{global_index:05d}"
                updated_var_names.append(var_name)

                previous_localjqueues[jqueue_index][bit_index] = curr_val

    return updated_queue, updated_var_names

def outQueue():
    updated_queue = []
    updated_var_names = []

    for oqueue_index, current_oqueue in enumerate(OQueue()):
        prev_jqueue = previous_jqueues[oqueue_index]
        for bit_index, (prev_val, curr_val) in enumerate(zip(prev_jqueue, current_oqueue)):
            if prev_val != curr_val:
                updated_queue.append((oqueue_index, bit_index))
                oqueue_index_real = 128 + oqueue_index
                global_index = 8 * oqueue_index_real + bit_index
                var_name = f"I{global_index:05d}"
                updated_var_names.append(var_name)

                previous_jqueues[oqueue_index][bit_index] = curr_val

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
                
        # Key format: "qj{GROUP_NUMBER:04d}latchv" (GROUP_NUMBER = group_idx + 16)
        qi_key = f"qj{group_idx + 16:04d}latchv"
        packed_list[qi_key] = byte_value

    # Update database
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': packed_list}
    )

def updateOutput(updated_queue: list):
    if not updated_queue:
        return

    # Group changes by their queue index
    changed_groups = set()
    for group_idx, _ in updated_queue:
        changed_groups.add(group_idx)

    # Build dictionary of full byte values for changed groups
    packed_list = {}
    current_queues = list(OQueue())  # Get current state of all groups
    
    for group_idx in changed_groups:
        # Calculate the full byte value (0-255) for this group
        byte_value = 0
        for bit_idx, bit_val in enumerate(current_queues[group_idx]):
            if bit_val:
                byte_value |= (1 << bit_idx)  # Set bit if True
                
        qi_key = f"qi5{group_idx:03d}glovar"
        packed_list[qi_key] = byte_value

    # Update database
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': packed_list}
    )


def unpack_inputs(packed_inputs: dict) -> dict:
    global changed_keys
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
                changed_keys.append(f'I{input_idx:05d}')

    # Add corresponding Jxxxxx values
    j_to_i_map = {
        "J00543": "I00031",
        "J00521": "I00012",
        "J00520": "I00011",
        "J00517": "I00003",
        "J00522": "I00013",
        "J00523": "I00014",
        "J00519": "I00005",
        "J00516": "I00000",
        "J00518": "I00004",
    }

    for j_key, i_key in j_to_i_map.items():
        old_val = globals().get(j_key)
        if old_val != globals()[i_key]:
            globals()[j_key] = globals()[i_key]
            changed_keys.append(j_key)

def BITAND(a, b):
    return a & b

def BITOR(a, b):
    return a | b

def int_to_hex(val):
    return hex(val)[2:].upper()

def int_to_bin_array(val):
    return [int(bit) for bit in bin(val)[2:].zfill(32)]

def bin_array_to_hex(bin_array):
    # Gabungkan elemen-elemen dalam list bin_array menjadi satu string biner
    bin_str = ''.join(map(str, bin_array))

    # Pisahkan string biner menjadi setiap empat bit dan tambahkan padding ke kiri jika perlu
    separated_bits = [bits.zfill(4) for bits in [bin_str[i:i + 4] for i in range(0, len(bin_str), 4)]]

    # Buat mapping dari nilai biner empat bit ke nilai heksadesimal
    bin_to_hex = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }

    # Konversi setiap empat bit menjadi nilai heksadesimal
    hex_digits = [bin_to_hex[bits] for bits in separated_bits]

    # Gabungkan nilai heksadesimal menjadi nilai heksadesimal lengkap
    hex_value = ''.join(hex_digits)

    return hex_value

def hex_to_int(hex_val):
    return int(hex_val, 16)

def frame3and2or4and(a, b, c, d, e,):
    return bool(a and not b and ((bool(c) and d) or (not bool(c) and e)))

def CloseLogic(in1,in2,in3,in4,in5):
    value = bool(in1 and not in2 and ((bool(in3) and in4) or (not bool(in4) and in5))) 
    output = {
        'out1' : value
    }  
    return output

def frame4and2or4and(a, b, c, d, e, f):
    return bool(a and not b and not c and ((bool(d) and e) or (not bool(d) and f)))

def StartNStopLogic(in1,in2,in3,in4,in5,in6):
    value1 = bool(in1 and not in2 and not in3 and ((bool(in4) and in5) or (not bool(in4) and in6)))
    value2 = bool (not value1)
    output = {
        'out1' : value1,
        'out2' : value2
    }
    return output

def frame5and2or4and(a, b, c, d, e, f, g):
    return bool(a and not b and not c and ((bool(d) and e) or (not bool(d) and f)) and not g)

def MoveCtrlLogic(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10):
    value1 = bool (in1 and not in2 and not in3 and ((bool(in4) and in5) or (not bool(in4) and in6)) and not in7)
    value2 = bool (in1 and not in2 and not in3 and ((bool(in4) and in8) or (not bool(in4) and in9)) and not in10)
    value3 = bool (not (value1 or value2))
    output = {
        'out1' : value1,
        'out2' : value2,
        'out3' : value3   
        }
    return output

def OpenLogic(in1,in2,in3,in4,in5,in6):
    value1 = bool(in1 and not in2 and not in3 and ((bool(in4) and in5) or (not bool(in4) and in6)))
    output = {
        'out1' : value1
    }
    return output

def frame6and2or4and(a, b, c, d, e, f, g, h):
    return bool(a and not b and not c and ((bool(d) and e) or (not bool(d) and f)) and not g and not h)

def OpenCloseLogic(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12):
    value1 = bool(in1 and not in2 and not in3 and ((bool(in4) and in5) or (not bool(in4) and in6)) and not in7 and not in8)
    value2 = bool(in1 and not in2 and not in3 and ((bool(in4) and in9) or (not bool(in4) and in10)) and not in11 and not in12)
    # value1 = bool(in1 and not in2 and not in3 and ((bool(in4) and in5) or (not bool(in4) and in6)) and not value2 and not in8)
    output = {
        'out1' : value1,
        'out2' : value2
    }
    return output

def frameTimer2or2and2and(a, b, c, d):
    return bool((not a and b) or (not c and d))

def frame2or4and2or(a, b, c, d):
    return bool((a and (b or c)) or ((b or c) and d))

def frameFillMixer(a, b, c, d, e):
    return bool(a and (b or c) and not d and not e)

def frameDumpMixer(a, b, c):
    return bool(a and b and not c)

class MoveChecker:
    def __init__(self, in1, out1, v, u, k):
        """
        in1: input 1 key,
        out1: output 1 key,
        v: Vxxx key,
        u: Uxxx key,
        k: Kxxx key,
        """
        self.in1 = in1
        self.out1 = out1
        self.v = v
        self.u = u
        self.k = k
        threading.Thread(target=self.run)

    def run(self):
        if not globals()[self.in1]:
            self.timer()
        else:
            globals()[self.k] = False
        globals()[self.out1] = self.logic()
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         self.out1: bool(globals()[self.out1])
        # }})

    def logic(self):
        bool(globals()[self.in1] or (not globals()[self.k] and globals()[self.out1]))

    def timer(self):
        globals()[self.u] = time.time()
        globals()[self.v] = 0
        while globals()[self.v] <= 2:
            globals()[self.v] = round(time.time() - globals()[self.u])

        globals()[self.k] = True

class AutoSelectorB:
    def __init__(self):
        global autohistory

        self.not_faultmotors = not bool(globals()['J00517'] or globals()['J00518'] or globals()['J00519'] or globals()['J00520'] or globals()['J00521'] or globals()['J00522'])
        self.condition1 = bool(globals()['I00032'] and not globals()['J00543'] and self.not_faultmotors and not globals()['J00513'])
        self.condition2 = bool(globals()['I00032'] and not globals()['J00543'] and self.not_faultmotors and not globals()['J00514'])
        self.condition3 = bool(globals()['I00032'] and not globals()['J00543'] and not (globals()['J00515'] or globals()['J00523']) and not globals()['J00513'])
        self.condition4 = bool(globals()['I00032'] and not globals()['J00543'] and not (globals()['J00515'] or globals()['J00523']) and not globals()['J00514'])

        if [self.condition1, self.condition2, self.condition3, self.condition4] != autohistory:
            autohistory.clear()
            autohistory.extend([self.condition1, self.condition2, self.condition3, self.condition4])

            if (globals()['V0148'] & 32768) and not self.condition1:
                globals()['V0148'] &= ~32768
            elif not (globals()['V0148'] & 32768) and self.condition1:
                globals()['V0148'] |= 32768
            if (globals()['V0148'] & 16384) and not self.condition2:
                globals()['V0148'] &= ~16384
            elif not (globals()['V0148'] & 16384) and self.condition2:
                globals()['V0148'] |= 16384
            if (globals()['V0148'] & 8192) and not self.condition2:
                globals()['V0148'] &= ~8192
            elif not (globals()['V0148'] & 8192) and self.condition2:
                globals()['V0148'] |= 8192
            if (globals()['V0148'] & 4096) and not self.condition2:
                globals()['V0148'] &= ~4096
            elif not (globals()['V0148'] & 4096) and self.condition2:
                globals()['V0148'] |= 4096
            if (globals()['V0148'] & 2048) and not self.condition3:
                globals()['V0148'] &= ~2048
            elif not (globals()['V0148'] & 2048) and self.condition3:
                globals()['V0148'] |= 2048
            if (globals()['V0148'] & 1024) and not self.condition4:
                globals()['V0148'] &= ~1024
            elif not (globals()['V0148'] & 1024) and self.condition4:
                globals()['V0148'] |= 1024

            collection.update_one(
                {'_id': ObjectId(objID)},
                {'$set': {
                    'V0148': globals()['V0148']
                }})

def BuzzerStop():
    print("BuzzerStop")
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0158': 0
        }})
    # calculateV0157ToPanelAlarmErrorSourcesZ0err()
    errBuzzUpdated()
    # serror()

def AlarmReset():
    print("alarmreset")
    # BuzzerStop()
    globals()['K000V0000IsJam'] = False
    globals()['K001V0001IsJam'] = False
    globals()['K002V0002IsJam'] = False
    globals()['K032V0032IsJam'] = False
    globals()['K033V0033IsJam'] = False
    globals()['K034V0034IsJam'] = False
    globals()['K035V0035IsJam'] = False
    globals()['K036V0036IsJam'] = False
    globals()['K037V0037IsJam'] = False
    globals()['K064V0064IsJam'] = False
    globals()['K065V0065IsJam'] = False

    document = collection.find_one({"_id": ObjectId(objID)})
    if document:
        V0517 = document.get('V0157')  # Mengambil nilai V0157 dari dokumen
        if V0517 is not None:
            print(f"Nilai V0157: {V0517}")
            collection.update_one(
                {'_id': ObjectId(objID)},
                {'$set': {
                    'V0158': 0,
                    'V0159': V0517
                }})
            # serror()
        else:
            print("V0157 tidak ditemukan dalam dokumen.")
    else:
        print("Dokumen tidak ditemukan.")
    
    errBuzzUpdated()

def start_timer(name, delay):
    # Cek apakah timer sudah ada, jika iya, batalkan dulu (untuk mencegah timer ganda untuk 1 variable)
    if name in timers:
        timers[name]["timer"].cancel()
        timers[name]["countdown_active"] = False
    # Membuat timer baru dan menyimpannya di dictionary
    timer = threading.Timer(delay, timeup, args=(name,))
    # menset timer + value awal
    timers[name] = {"timer": timer, "result": False, "countdown_active": True}

    # Fungsi countdown untuk menampilkan waktu tersisa setiap detik
    def countdown():
        remaining = delay
        while remaining > 0  and timers[name]["countdown_active"]:  # Periksa jika timer masih aktif
            print(f"{name} - Waktu tersisa: {remaining} detik")
            time.sleep(1)
            remaining -= 1

    # Mulai timer
    timer.start()

    # Mulai countdown di thread terpisah
    threading.Thread(target=countdown).start()

    # untuk debug kalau ga dibutuhin hapus aja
    print(f"{name} dimulai...")

# Fungsi yang dijalankan saat waktu habis
def timeup(name):
    # set value dari variable jadi true apabila timer sudah beres
    timers[name]["result"] = True
    timers[name]["countdown_active"] = False
    # untuk debug, kalau ga dibutuhin bisa dihapus
    print(f"{name} selesai!")  # Cetak pesan saat timer selesai
    globals()[name] = True

    # match timers[name]:
    match name:
        # LINE B
        case "J00245":
            globals()['K011'] = True
        case "J00290":
            globals()['K014'] = True
        case "J00291":
            globals()['K015'] = True
        case "J00135":
            globals()['K016'] = True
        case "J00136":
            globals()['K017'] = True
        case "J00137":
            globals()['K018'] = True
        case "J00138":
            globals()['K019'] = True
        case "J00139":
            globals()['K020'] = True
        case "J00140":
            globals()['K021'] = True
        case "J00141":
            globals()['K022'] = True
        case "J00142":
            globals()['K023'] = True
        case "J00143":
            globals()['K024'] = True
        case "J00144":
            globals()['K025'] = True
        case "J00145":
            globals()['K026'] = True

        # LINE C
        case "J00251":
            globals()['K043'] = True
        case "J00208":
            globals()['K048'] = True
        case "J00209":
            globals()['K049'] = True
        case "J00210":
            globals()['K050'] = True
        case "J00203":
            globals()['K051'] = True
        case "J00204":
            globals()['K052'] = True
        case "J00205":
            globals()['K053'] = True
        case "J00206":
            globals()['K054'] = True
        case "J00207":
            globals()['K055'] = True
        case "J00198":
            globals()['K056'] = True
        case "J00199":
            globals()['K057'] = True
        case "J00200":
            globals()['K058'] = True
        case "J00201":
            globals()['K059'] = True
        case "J00202":
            globals()['K060'] = True        
        case _:
            print("")

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         name: globals()[name]
    #     }})
    calculateV0157ToPanelAlarmErrorSourcesZ0err()

# Fungsi untuk menghentikan timer
def stop_timer(name):
    if name in timers:
        # untuk cancel timer
        timers[name]["timer"].cancel()
        # untuk mereset value jadi false, kalau ga dibutuhin bisa dihapus aja
        timers[name]["result"] = False
        #untuk matiin countdown
        timers[name]["countdown_active"] = False  # Set countdown tidak aktif saat dihentikan

        # untuk debug, kalau ga dibutuhin bisa dihapus
        print(f"{name} dihentikan...")

# def oldsetOutputToRLY():

#     arrayY = [globals()[f'I{str(i).zfill(5)}'] for i in range(128, 192)] + [globals()[f'I{str(i).zfill(5)}'] for i in range(192, 256)]

#     globals()['qy0000output'] = (ctypes.c_ubyte * 128)(*map(int, arrayY))

#     resRLY = ydu.YduDioOutput(output_id, ctypes.byref(globals()['qy0000output']), 0, 128)

# def setInputFromDIO():
#     global qi0000glovar

#     if resInput == YDU_RESULT_SUCCESS:
#         while True:
#             resDIO = ydu.YduDioInput(input_id, ctypes.byref(qi0000glovar), 0, 128)

#             for i in range(128):
#                 globals()[f'I{str(i).zfill(5)}'] = globals()['qi0000glovar'][i]

#             # Remote ON - DEBUG - HAPUS jika sudah connect ke panel
#             globals()['I00028'] = True
#             globals()['I00096'] = True
#             globals()['I00032'] = True
            

#             # Running Mode
#             globals()['V0149'] = True

#             # Emergency Stop
#             # globals()['J00543'] = globals()['I00036']
#             # if not globals()['I00031']:
#             #     print(f"globals()['I00031']:{bool(globals()['I00031'])}")
#             # # else:
#             # #     print(f"else globals()['I00031']:{bool(globals()['I00031'])}")
#             # globals()['I00031'] = True
#             globals()['J00543'] = globals()['I00031']
#             # globals()['J00543'] = False 

#             # if globals()['I00031']:
#             lblinfo3.configure(text=f"globals()['I00031']:{bool(globals()['I00031'])}")

#             # IsFault LINE B
#             globals()['J00515'] = globals()['I00024']
#             globals()['J00516'] = globals()['I00000']
#             globals()['J00517'] = globals()['I00003']
#             globals()['J00518'] = globals()['I00004']
#             globals()['J00519'] = globals()['I00005']
#             globals()['J00520'] = globals()['I00011']
#             globals()['J00521'] = globals()['I00012']
#             globals()['J00522'] = globals()['I00013']
#             globals()['J00523'] = globals()['I00025']

#             # IsFault LINE C
#             globals()['J00534'] = globals()['I00064']
#             globals()['J00535'] = globals()['I00067']
#             globals()['J00536'] = globals()['I00068']
#             globals()['J00537'] = globals()['I00069']
#             globals()['J00538'] = globals()['I00083']
#             globals()['J00539'] = globals()['I00084']
#             globals()['J00540'] = globals()['I00085']

#             collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 # Local / Remote
#                 'I00028': bool(globals()['I00028']),
#                 # Buzzer Stop
#                 'I00029': bool(globals()['I00029']),
#                 # Alarm Reset
#                 'I00030': bool(globals()['I00030']),
#                 # Emergency Stop
#                 'J00543': bool(globals()['J00543']),
#                 # Save IsFault
#                 # 'I00064': bool(globals()['I00064']),
#                 # 'I00067': bool(globals()['I00067']),
#                 # 'I00068': bool(globals()['I00068']),
#                 # 'I00069': bool(globals()['I00069']),
#                 # 'I00083': bool(globals()['I00083']),
#                 # 'I00084': bool(globals()['I00084']),
#                 # 'I00085': bool(globals()['I00085']),

#                 # Save IsMany LineB
#                 'I00006': bool(globals()['I00006']),
#                 'I00007': bool(globals()['I00007']),
#                 'I00008': bool(globals()['I00008']),
#                 'I00009': bool(globals()['I00009']),
#                 'I00010': bool(globals()['I00010']),
#                 'I00014': bool(globals()['I00014']),
#                 'I00015': bool(globals()['I00015']),
#                 'I00016': bool(globals()['I00016']),
#                 'I00017': bool(globals()['I00017']),
#                 'I00018': bool(globals()['I00018']),
#                 'I00019': bool(globals()['I00019']),

#                 # Save IsMany Line C
#                 # 'I00080': bool(globals()['I00080']),
#                 # 'I00081': bool(globals()['I00081']),
#                 # 'I00082': bool(globals()['I00082']),
#                 # 'I00086': bool(globals()['I00086']),
#                 # 'I00087': bool(globals()['I00087']),
#                 # 'I00088': bool(globals()['I00088']),
#                 # 'I00089': bool(globals()['I00089']),
#                 # 'I00090': bool(globals()['I00090']),
#                 # 'I00091': bool(globals()['I00091']),
#                 # 'I00092': bool(globals()['I00092']),
#                 # 'I00093': bool(globals()['I00093']),
#                 # 'I00094': bool(globals()['I00094']),
#                 'I00095': bool(globals()['I00095']),

#                 # 'I00065': bool(globals()['I00065']),
#                 'I00192': bool(globals()['I00192']),
#                 # 'I00066': bool(globals()['I00066']),
#                 'I00193': bool(globals()['I00193']),
#                 # 'I00070': bool(globals()['I00070']),
#                 'I00214': bool(globals()['I00214']),
#                 # 'I00071': bool(globals()['I00071']),
#                 'I00215': bool(globals()['I00215']),
#                 # 'I00072': bool(globals()['I00072']),
#                 'I00216': bool(globals()['I00216']),
#                 # 'I00073': bool(globals()['I00073']),
#                 'I00231': bool(globals()['I00231']),
#                 'I00233': bool(globals()['I00233']),
#                 'I00235': bool(globals()['I00235']),
#                 'I00199': bool(globals()['I00199']),
#                 'I00201': bool(globals()['I00201']),
#                 'I00203': bool(globals()['I00203']),
#                 'I00205': bool(globals()['I00205']),
#                 'I00207': bool(globals()['I00207']),
#                 'I00194': bool(globals()['I00194']),

#                 # LINE B
#                 'I00024': bool(globals()['I00024']),
#                 'I00000': bool(globals()['I00000']),
#                 'I00003': bool(globals()['I00003']),
#                 'I00004': bool(globals()['I00004']),
#                 'I00005': bool(globals()['I00005']),
#                 'I00011': bool(globals()['I00011']),
#                 'I00012': bool(globals()['I00012']),
#                 'I00013': bool(globals()['I00013']),
#                 'I00025': bool(globals()['I00025']),

#                 #Hopper door
#                 'I00020': bool(globals()['I00020']),
#                 'I00021': bool(globals()['I00021']),
#                 'I00022': bool(globals()['I00022']),
#                 'I00023': bool(globals()['I00023']),
#             }})

# def DummysetInputFromDIO():
#     pipeline = []
#     counterAntrian = 0
#     if objID:
#         pipeline = [{'$match': {'documentKey._id': ObjectId("672db90fe37f3e62157cdbd9")}}]    
    
#     with collection.watch(pipeline) as stream:
#         print("Memantau perubahan di DummyIO Software...")

#         for change in stream:
#             if change['operationType'] == 'update':
#                 try:
#                     # Ambil field yang diubah
#                     updated_fields = change['updateDescription']['updatedFields']
#                     # queueToCall = []

#                     print(f"{updated_fields}")

#                     document = collection.find_one({"_id": ObjectId("672db90fe37f3e62157cdbd9")})
#                     if document:
#                         var_nameI = f'I{i:05}'
#                         if var_nameI in document:
#                             # Setel nilai variabel global dengan nilai dari MongoDB
#                             globals()[var_nameI] = document[var_nameI]

#                         # Running Mode
#                         # globals()['V0149'] = 4194304

#                         # Remote ON - DEBUG - HAPUS jika sudah connect ke panel
#                         # globals()['I00028'] = True
#                         # globals()['I00096'] = True
#                         # globals()['I00032'] = True

#                         # Emergency Stop
#                         # globals()['J00543'] = not globals()['I00031']
#                         globals()['J00543'] = False

#                         # IsFault LINE B
#                         globals()['J00515'] = globals()['I00024']
#                         globals()['J00516'] = globals()['I00000']
#                         globals()['J00517'] = globals()['I00003']
#                         globals()['J00518'] = globals()['I00004']
#                         globals()['J00519'] = globals()['I00005']
#                         globals()['J00520'] = globals()['I00011']
#                         globals()['J00521'] = globals()['I00012']
#                         globals()['J00522'] = globals()['I00013']
#                         globals()['J00523'] = globals()['I00025']

#                         # IsFault LINE C
#                         globals()['J00534'] = globals()['I00064']
#                         globals()['J00535'] = globals()['I00067']
#                         globals()['J00536'] = globals()['I00068']
#                         globals()['J00537'] = globals()['I00069']
#                         globals()['J00538'] = globals()['I00083']
#                         globals()['J00539'] = globals()['I00084']
#                         globals()['J00540'] = globals()['I00085']

#                         collection.update_one(
#                         {'_id': ObjectId(objID)},
#                         {'$set': {
#                             # Local / Remote
#                             'I00028': bool(globals()['I00028']),
#                             'I00096': bool(globals()['I00096']),
#                             'I00032': bool(globals()['I00032']),
#                             # Buzzer Stop
#                             'I00029': bool(globals()['I00029']),
#                             # Alarm Reset
#                             'I00030': bool(globals()['I00030']),
#                             # Emergency Stop
#                             'J00543': bool(globals()['J00543']),
#                             # Save IsFault
#                             'I00064': bool(globals()['I00064']),
#                             'I00067': bool(globals()['I00067']),
#                             'I00068': bool(globals()['I00068']),
#                             'I00069': bool(globals()['I00069']),
#                             'I00083': bool(globals()['I00083']),
#                             'I00084': bool(globals()['I00084']),
#                             'I00085': bool(globals()['I00085']),

#                             # Save IsMany LineB
#                             'I00006': bool(globals()['I00006']),
#                             'I00007': bool(globals()['I00007']),
#                             'I00008': bool(globals()['I00008']),
#                             'I00009': bool(globals()['I00009']),
#                             'I00010': bool(globals()['I00010']),
#                             'I00014': bool(globals()['I00014']),
#                             'I00015': bool(globals()['I00015']),
#                             'I00016': bool(globals()['I00016']),
#                             'I00017': bool(globals()['I00017']),
#                             'I00018': bool(globals()['I00018']),
#                             'I00019': bool(globals()['I00019']),

#                             # Save IsMany Line C
#                             'I00080': bool(globals()['I00080']),
#                             'I00081': bool(globals()['I00081']),
#                             'I00082': bool(globals()['I00082']),
#                             'I00086': bool(globals()['I00086']),
#                             'I00087': bool(globals()['I00087']),
#                             'I00088': bool(globals()['I00088']),
#                             'I00089': bool(globals()['I00089']),
#                             'I00090': bool(globals()['I00090']),
#                             'I00091': bool(globals()['I00091']),
#                             'I00092': bool(globals()['I00092']),
#                             'I00093': bool(globals()['I00093']),
#                             'I00094': bool(globals()['I00094']),
#                             'I00095': bool(globals()['I00095']),

#                             'I00065': bool(globals()['I00065']),
#                             'I00192': bool(globals()['I00192']),
#                             'I00066': bool(globals()['I00066']),
#                             'I00193': bool(globals()['I00193']),
#                             'I00070': bool(globals()['I00070']),
#                             'I00214': bool(globals()['I00214']),
#                             'I00071': bool(globals()['I00071']),
#                             'I00215': bool(globals()['I00215']),
#                             'I00072': bool(globals()['I00072']),
#                             'I00216': bool(globals()['I00216']),
#                             'I00073': bool(globals()['I00073']),
#                             'I00231': bool(globals()['I00231']),
#                             'I00233': bool(globals()['I00233']),
#                             'I00235': bool(globals()['I00235']),
#                             'I00199': bool(globals()['I00199']),
#                             'I00201': bool(globals()['I00201']),
#                             'I00203': bool(globals()['I00203']),
#                             'I00205': bool(globals()['I00205']),
#                             'I00207': bool(globals()['I00207']),
#                             'I00194': bool(globals()['I00194']),

#                             # LINE B
#                             'I00024': bool(globals()['I00024']),
#                             'I00000': bool(globals()['I00000']),
#                             'I00003': bool(globals()['I00003']),
#                             'I00004': bool(globals()['I00004']),
#                             'I00005': bool(globals()['I00005']),
#                             'I00011': bool(globals()['I00011']),
#                             'I00012': bool(globals()['I00012']),
#                             'I00013': bool(globals()['I00013']),
#                             'I00025': bool(globals()['I00025'])
#                         }})

#                         lblinfo.configure(text=f"globals()['V0149']:{globals()['V0149']} - globals()['J00410']:{globals()['J00410']} - globals()['J00389']:{globals()['J00389']}")
#                         lblinfo2.configure(text=f"globals()['J00174']:{globals()['J00174']} - globals()['J00175']:{globals()['J00175']}")
#                         lblinfo3.configure(text=f"globals()['K033V0033IsJam']:{globals()['K033V0033IsJam']}")
                   

#                 except KeyError as e:
#                     print(f"Error accessing updated fields: {e}")

def setOutputToRLY():
    # global I00128, I00129, I00130, I00131, I00132, I00133, I00134, I00135, I00136, I00137, I00138, I00139
    # global I00140, I00141, I00142, I00143, I00144, I00145, I00146, I00147, I00148, I00149, I00150, I00151
    # global I00152, I00153, I00154, I00155, I00156, I00157, I00158, I00159, I00160, I00161, I00162, I00163
    # global I00164, I00165, I00166, I00167, I00168, I00169, I00170, I00171, I00172, I00173, I00174, I00175
    # global I00128, I00129, I00130, I00131, I00132, I00133, I00134, I00135, I00136, I00137, I00138, I00139
    # global I00140, I00141, I00142, I00143, I00192, I00193, I00194, I00195, I00196, I00197, I00198, I00199
    # global I00200, I00201, I00202, I00203, I00204, I00205, I00206, I00207, I00208, I00209, I00210, I00211
    # global I00212, I00213, I00214, I00215, I00216, I00217, I00218, I00219, I00220, I00221, I00222, I00223
    # global I00224, I00225, I00226, I00227, I00228, I00229, I00230, I00231, I00232, I00233, I00234, I00235
    # global I00236, I00237, I00238, I00239, I00240, I00241, I00242, I00243, I00244, I00245, I00246, I00247
    # global I00248, I00249, I00250, I00251, I00252, I00253, I00254, I00255
  
    # arrayY = [
    #             # globals()['I00228'], globals()['I00229'], globals()['I00231'], globals()['I00233'], globals()['I00235'], globals()['I00224'], globals()['I00225'], globals()['I00226'], globals()['I00227'], globals()['I00222'], globals()['I00223'], I00139,
    #             I00128, I00129, I00130, I00131, I00132, I00133, I00134, I00135, I00136, I00137, I00138, I00139,
    #             I00140, I00141, I00142, I00143, I00144, I00145, I00146, I00147, I00148, I00149, I00150, I00151,
    #             I00152, I00153, I00154, I00155, I00156, I00157, I00158, I00159, I00160, I00161, I00162, I00163,
    #             I00164, I00165, I00166, I00167, I00168, I00169, I00170, I00171, I00172, I00173, I00174, I00175,
    #             I00128, I00129, I00130, I00131, I00132, I00133, I00134, I00135, I00136, I00137, I00138, I00139,
    #             I00140, I00141, I00142, I00143, I00192, I00193, I00194, I00195, I00196, I00197, I00198, I00199, 
    #             I00200, I00201, I00202, I00203, I00204, I00205, I00206, I00207, I00208, I00209, I00210, I00211, 
    #             I00212, I00213, I00214, I00215, I00216, I00217, I00218, I00219, I00220, I00221, I00222, I00223,
    #             I00224, I00225, I00226, I00227, I00228, I00229, I00230, I00231, I00232, I00233, I00234, I00235,
    #             I00236, I00237, I00238, I00239, I00240, I00241, I00242, I00243, I00244, I00245, I00246, I00247,
    #             I00248, I00249, I00250, I00251, I00252, I00253, I00254, I00255
    #         ]

    # globals()['qy0000output'] = (ctypes.c_ubyte * 128)(*map(int, arrayY))

    # # resRLY = ydu.YduDioOutput(output_id, ctypes.byref(globals()['qy0000output']), 0, 128)


    # arrOuput0 = 0
    # arrOuput1 = 0
    # arrOuput2 = 0
    # arrOuput3 = 0
    
    # qy0000ouput = [
    #     globals()['I00128'], globals()['I00129'], globals()['I00130'], globals()['I00131'], globals()['I00132'], globals()['I00133'], globals()['I00134'], globals()['I00135'], globals()['I00136'], globals()['I00137'], globals()['I00138'], globals()['I00139'],
    #             globals()['I00140'], globals()['I00141'], globals()['I00142'], globals()['I00143'], #Ga kepakai
    #             globals()['I00144'], globals()['I00145'], globals()['I00146'], globals()['I00147'], globals()['I00148'], globals()['I00149'], globals()['I00150'], globals()['I00151'], # Akhir Baris 1
    #             globals()['I00152'], globals()['I00153'], globals()['I00154'], globals()['I00155'], globals()['I00156'], globals()['I00157'], globals()['I00158'], globals()['I00159']
    # ]
    
    # qy0001ouput = [
    #     globals()['I00160'], globals()['I00161'], globals()['I00162'], globals()['I00163'],
    #             globals()['I00164'], globals()['I00165'], globals()['I00166'], globals()['I00167'], globals()['I00168'], globals()['I00169'], globals()['I00170'], globals()['I00171'], globals()['I00172'], globals()['I00173'], globals()['I00174'], globals()['I00175'], 
    #             globals()['I00176'], globals()['I00177'], globals()['I00178'], globals()['I00179'], globals()['I00180'], globals()['I00181'], globals()['I00182'], globals()['I00183'], globals()['I00184'], globals()['I00185'], globals()['I00186'], globals()['I00187'], 
    #             globals()['I00188'], globals()['I00189'], globals()['I00190'], globals()['I00191']
    # ]

    # qy0002ouput = [
    #     globals()['I00192'], globals()['I00193'], globals()['I00194'], globals()['I00195'], globals()['I00196'], globals()['I00197'], globals()['I00198'], globals()['I00199'], globals()['I00200'], globals()['I00201'], globals()['I00202'], globals()['I00203'],
    #             globals()['I00204'], globals()['I00205'], globals()['I00206'], globals()['I00207'], globals()['I00208'], globals()['I00209'], globals()['I00210'], globals()['I00211'], globals()['I00212'], globals()['I00213'], globals()['I00214'], globals()['I00215'],
    #             globals()['I00216'], globals()['I00217'], globals()['I00218'], globals()['I00219'], globals()['I00220'], globals()['I00221'], globals()['I00222'], globals()['I00223']

    # ]

    # qy0003ouput = [
    #     globals()['I00224'], globals()['I00225'], globals()['I00226'], globals()['I00227'],
    #             globals()['I00228'], globals()['I00229'], globals()['I00230'], globals()['I00231'], globals()['I00232'], globals()['I00233'], globals()['I00234'], globals()['I00235'], globals()['I00236'], globals()['I00237'], globals()['I00238'], globals()['I00239'],
    #             globals()['I00240'], globals()['I00241'], globals()['I00242'], globals()['I00243'], globals()['I00244'], globals()['I00245'], globals()['I00246'], globals()['I00247'], globals()['I00248'], globals()['I00249'], globals()['I00250'], globals()['I00251'],
    #             globals()['I00252'], globals()['I00253'], globals()['I00254'], globals()['I00255'] 
    # ]
    
    # for i, value in enumerate(qy0000ouput):
    #     if value:
    #         arrOuput0 |= (1 << i)

    # for i, value in enumerate(qy0001ouput):
    #     if value:
    #         arrOuput1 |= (1 << i)

    # for i, value in enumerate(qy0002ouput):
    #     if value:
    #         arrOuput2 |= (1 << i)
    
    # for i, value in enumerate(qy0003ouput):
    #     if value:
    #         arrOuput3 |= (1 << i)

    # outputHex0 = int_to_hex(arrOuput0)
    # outputHex1 = int_to_hex(arrOuput1)
    # outputHex2 = int_to_hex(arrOuput2)
    # outputHex3 = int_to_hex(arrOuput3)

    # collection.update_one(
    #     {'_id': ObjectId("672db90fe37f3e62157cdbd9")},
    #     {'$set': {
    #         'Output0': outputHex0,
    #         'Output1': outputHex1,
    #         'Output2': outputHex2,
    #         'Output3': outputHex3
    #     }})
    return None
    

def calculateV0157ToPanelAlarmErrorSourcesZ0err():
    global V0157ToPanelAlarmErrorSourcesZ0err
    V0157ToPanelAlarmErrorSourcesZ0err = 0

    # print(f"v0157 exec - globals()['I00064'] : {globals()['I00064']} - globals()['I00067'] : {globals()['I00067']} - globals()['I00068'] : {globals()['I00068']} - globals()['I00069'] : {globals()['I00069']}")
    # errSource = [globals()['K000V0000IsFault'], globals()['K001V0001IsFault'], globals()['K002V0002IsFault'], globals()['I00024'], globals()['I00000'], globals()['I00003'], globals()['I00004'], globals()['I00005'],
    #             globals()['I00011'], globals()['I00012'], globals()['I00013'], globals()['I00025'], False, False,
    #             False, False, 
    #             globals()['K032V0032IsJam'], globals()['K033V0033IsJam'], globals()['K034V0034IsJam'], globals()['K035V0035IsJam'], globals()['K036V0036IsJam'], globals()['K037V0037IsJam'], 
    #             bool(globals()['I00064']), bool(globals()['I00067']), bool(globals()['I00068']), bool(globals()['I00069']), bool(globals()['I00083']), bool(globals()['I00084']), bool(globals()['I00085']), False]
    # errSource = [globals()['K000V0000IsJam'], globals()['K001V0001IsJam'], globals()['K002V0002IsJam'], globals()['I00024'], globals()['I00000'], globals()['I00003'], globals()['I00004'], globals()['I00005'], globals()['I00011'], globals()['I00012'], globals()['I00013'], globals()['I00025'], False, False, False, False, 
    #              globals()['K032V0032IsJam'], globals()['K033V0033IsJam'], globals()['K034V0034IsJam'], globals()['K035V0035IsJam'], globals()['K036V0036IsJam'], globals()['K037V0037IsJam'],
    #              globals()['J00534'], globals()['J00535'], globals()['J00536'], globals()['J00537'], globals()['J00538'], globals()['J00539'], globals()['J00540'], False]
    errSource = [globals()['K000V0000IsJam'], globals()['K001V0001IsJam'], globals()['K002V0002IsJam'], globals()['I00024'], globals()['I00000'], globals()['I00003'], globals()['I00004'], globals()['I00005'], globals()['I00011'], globals()['I00012'], globals()['I00013'], globals()['I00025'], False, False, 
                 globals()['K064V0064IsJam'], globals()['K065V0065IsJam'], 
                 globals()['K032V0032IsJam'], globals()['K033V0033IsJam'], globals()['K034V0034IsJam'], globals()['K035V0035IsJam'], globals()['K036V0036IsJam'], globals()['K037V0037IsJam'],
                 globals()['I00064'], globals()['I00067'], globals()['I00068'], globals()['I00069'], globals()['I00083'], globals()['I00084'], globals()['I00085'], globals()['J00543']]

    for i, value in enumerate(errSource):
        if value:
            V0157ToPanelAlarmErrorSourcesZ0err |= (1 << i)
    
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0157': V0157ToPanelAlarmErrorSourcesZ0err
        }})
    print(f"V0157={V0157ToPanelAlarmErrorSourcesZ0err}")

def errBuzzUpdated():
    global K000V0000IsFault, K001V0001IsFault, K002V0002IsFault, J00046, J00047
    global I00000, I00003, I00004, I00005, I00011, I00012, I00013, I00024, I00025, I00239
    global V0157ToPanelAlarmErrorSourcesZ0err, V0158, V0159, V0157
    global V0159AlarmHoldOutputZ0err, V0158AlarmBuzrOutputZ0err
    
    print("errBuzzUpdated exec")

    max_int = 4294967295

    document = collection.find_one({"_id": ObjectId(objID)})
    if document:
        V0158 = document.get('V0158')
        V0159 = document.get('V0159')
        V0158AlarmBuzrOutputZ0err = V0158
        V0159AlarmHoldOutputZ0err = V0159
    
    # errSource = [K000V0000IsFault, K001V0001IsFault, K002V0002IsFault, I00024, I00000, I00003, I00004, I00005,
    #             I00011, I00012, I00013, I00025, False, False,
    #             False, False, 
    #             globals()['K032V0032IsJam'], globals()['K033V0033IsJam'], globals()['K034V0034IsJam'], globals()['K035V0035IsJam'], globals()['K036V0036IsJam'], globals()['K037V0037IsJam'], 
    #             bool(globals()['I00064']), bool(globals()['I00067']), bool(globals()['I00068']), bool(globals()['I00069']), bool(globals()['I00083']), bool(globals()['I00084']), bool(globals()['I00085']), False]
    # errSource = [512-,513-,514-,515-,516-,517-,518-,519-,
    #              520-,521-,522-,523-,524,525,
    #              526,527,
    #              528-,529-,530-,531-,532-,533-,
    #              534,535,536,537,538,539,540,543]

    calculateV0157ToPanelAlarmErrorSourcesZ0err()

    if V0159AlarmHoldOutputZ0err:
        V159hold = max_int - V0159AlarmHoldOutputZ0err
    else:
        V159hold = 0
    
    # kemudian V0157ToPanelAlarmErrorSourcesZ0err di AND dengan bit-inverse V159hold tadi supaya hanya signal error yg baru yg didapatkan.
    V158bitand = BITAND(V0157ToPanelAlarmErrorSourcesZ0err, V159hold)
    
    # print(f"V158bitand : {V158bitand}") # V158bitand itu signal error baru
    # setelah itu di OR dgn V158buzz untuk menambahkan ke buzzer.

    if V158bitand and V0158AlarmBuzrOutputZ0err:
        V158bitor = BITOR(V0158AlarmBuzrOutputZ0err, V158bitand)
    else:
        V158bitor = 0
    
    # refresh V158buzz
    V0158AlarmBuzrOutputZ0err = V158bitor
    # V518V0158AlarmBuzrOutputZ0err DONE
    if V0159AlarmHoldOutputZ0err and V0158AlarmBuzrOutputZ0err:
        V159hold = BITOR(V0159AlarmHoldOutputZ0err, V0158AlarmBuzrOutputZ0err)
        V0159AlarmHoldOutputZ0err = V159hold
    # V0159AlarmHoldOutputZ0err DONE
    else:
        V159hold = 0
        V0159AlarmHoldOutputZ0err = 0
        V0158AlarmBuzrOutputZ0err = 0


    if V0157ToPanelAlarmErrorSourcesZ0err and V0159AlarmHoldOutputZ0err:
        V0157 = BITAND(V0157ToPanelAlarmErrorSourcesZ0err, V0159AlarmHoldOutputZ0err)
    else:
        V0157 = 0
        V0157ToPanelAlarmErrorSourcesZ0err = 0
        V0159AlarmHoldOutputZ0err = 0
    
    qj0016latchv = int_to_bin_array(V0159AlarmHoldOutputZ0err)
    
    for i, value in enumerate(reversed(qj0016latchv)):
        globals()[f'J00{512 + i}'] = bool(value)
    
    qj0017latchv = int_to_bin_array(V0158AlarmBuzrOutputZ0err)
    for i, value in enumerate(reversed(qj0017latchv)):
        globals()[f'J00{544 + i}'] = bool(value)

    # print(f"qj0017latchv : {qj0017latchv}")

    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0157': V0157,
            'V0158': V0158AlarmBuzrOutputZ0err,
            'V0159': V0159AlarmHoldOutputZ0err,
            # 'J00512': globals()['J00512'],
            # 'J00513': globals()['J00513'],
            # 'J00514': globals()['J00514'],
            # 'J00515': globals()['J00515'],
            # 'J00516': globals()['J00516'],
            # 'J00517': globals()['J00517'],
            # 'J00518': globals()['J00518'],
            # 'J00519': globals()['J00519'],
            # 'J00520': globals()['J00520'],
            # 'J00521': globals()['J00521'],
            # 'J00522': globals()['J00522'],
            # 'J00523': globals()['J00523'],
            # 'J00524': globals()['J00524'],
            # 'J00525': globals()['J00525'],
            # 'J00526': globals()['J00526'],
            # 'J00527': globals()['J00527'],
            # 'J00528': globals()['J00528'],
            # 'J00529': globals()['J00529'],
            # 'J00530': globals()['J00530'],
            # 'J00531': globals()['J00531'],
            # 'J00532': globals()['J00532'],
            # 'J00533': globals()['J00533'],
            # 'J00534': globals()['J00534'],
            # 'J00535': globals()['J00535'],
            # 'J00536': globals()['J00536'],
            # 'J00537': globals()['J00537'],
            # 'J00538': globals()['J00538'],
            # 'J00539': globals()['J00539'],
            # 'J00540': globals()['J00540'],
            # 'J00543': globals()['J00543'],
            # 'J00544': globals()['J00544'],
            # 'J00545': globals()['J00545'],
            # 'J00546': globals()['J00546'],
            # 'J00547': globals()['J00547'],
            # 'J00548': globals()['J00548'],
            # 'J00549': globals()['J00549'],
            # 'J00550': globals()['J00550'],
            # 'J00551': globals()['J00551'],
            # 'J00552': globals()['J00552'],
            # 'J00553': globals()['J00553'],
            # 'J00554': globals()['J00554'],
            # 'J00555': globals()['J00555'],
            # 'J00556': globals()['J00556'],
            # 'J00557': globals()['J00557'],
            # 'J00558': globals()['J00558'],
            # 'J00559': globals()['J00559'],
            # 'J00560': globals()['J00560'],
            # 'J00561': globals()['J00561'],
            # 'J00562': globals()['J00562'],
            # 'J00563': globals()['J00563'],
            # 'J00564': globals()['J00564'],
            # 'J00565': globals()['J00565'],
            # 'J00566': globals()['J00566'],
            # 'J00567': globals()['J00567'],
            # 'J00568': globals()['J00568'],
            # 'J00569': globals()['J00569'],
            # 'J00570': globals()['J00570'],
            # 'J00571': globals()['J00571'],
            # 'J00572': globals()['J00572'],
            # 'J00573': globals()['J00573'],
            # 'J00574': globals()['J00574'],
            # 'J00575': globals()['J00575']
            }})

# penambahan update log secara terus menerus setiap 30 detik
def updateQueuelog():
    global doc_antrian
    while True:
        doc = collection.find_one({"_id": doc_antrian.inserted_id})
        if doc:
            time.sleep(30)
            fields_to_unset = {key: "" for key in doc if key != "_id"}
            collection.update_one(
                {"_id": doc_antrian.inserted_id},
                {"$unset": fields_to_unset} 
            )

def manualSelector():
    inf1 = bool(not ((globals()['V0148'] & 32768) == 32768)  and (globals()['V0144'] == 32768 or globals()['V0140'] == 32768))
    inf2 = bool(not ((globals()['V0148'] & 16384) == 16384) and (globals()['V0144'] == 16384 or globals()['V0140'] == 16384))
    inf3 = bool(not ((globals()['V0148'] & 8192) == 8192) and (globals()['V0144'] == 8192 or globals()['V0140'] == 8192))
    inf4 = bool(not ((globals()['V0148'] & 4096) == 4096) and (globals()['V0144'] == 4096 or globals()['V0140'] == 4096))
    inh1 = bool(not ((globals()['V0148'] & 2048) == 2048) and (globals()['V0145'] == 2048 or globals()['V0141'] == 2048))
    inh2 = bool(not ((globals()['V0148'] & 1024) == 1024) and (globals()['V0145'] == 1024 or globals()['V0141'] == 1024))

    if inf1 or inf2 or inf3 or inf4:
        globals()['V0144'] = 0
        globals()['V0140'] = 0
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0144': 0,
                'V0140': 0
            }})
    if inh1 or inh2:
        globals()['V0145'] = 0
        globals()['V0141'] = 0
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0145': 0,
                'V0141': 0
            }})

# penambahan filter anti double fungsi yang sama dalam satu waktu
def queueManage():
    global threads, queueToCall, queueToCallText, doc_antrian
    filtered_queueToCall = []
    filtered_queueToCalltext = []
    thread_log = threading.Thread(target=updateQueuelog)
    thread_log.start()
    while True:
        AutoSelectorB()
        manualSelector()
        updated_queue, _ = processQueue()
        updateProcess(updated_queue)
        updated_outputs , _ = processOQueue()
        updateOutput(updated_outputs)
        for queue in queueToCall:
            if queue not in [q[0] for q in filtered_queueToCall]:  # pastikan hanya dibandingkan dengan elemen fungsi (bukan tuple keseluruhan)
                filtered_queueToCall.append((queue, {"time": 0}))
        queueToCall.clear()

        # Filter queueToCallText -> filtered_queueToCalltext
        for queue in queueToCallText:
            if queue not in filtered_queueToCalltext:
                filtered_queueToCalltext.append(queue)
        queueToCallText.clear()

        # Eksekusi jika ada antrian
        if filtered_queueToCall:
            t1 = time.time()

            # Ambil fungsi dan parameter dari antrian
            if isinstance(filtered_queueToCall[0][0], list):
                targeted_call = filtered_queueToCall[0][0][0]
                targeted_params = filtered_queueToCall[0][0][1]
                if isinstance(targeted_params, tuple):
                    targeted_call(*targeted_params)
                else:
                    targeted_call(targeted_params)
            else:
                targeted_call = filtered_queueToCall[0][0]
                targeted_call()

            # Hitung waktu eksekusi
            t_over = (time.time() - t1) * 1000  # dalam milidetik
            filtered_queueToCall[0][1]["time"] = t_over

            # Log ke MongoDB
            ct = datetime.datetime.now()
            func_doc = [{str(ct): str(func)} for func in filtered_queueToCall]
            print(func_doc)
            collection.update_one(
                {"_id": doc_antrian.inserted_id},
                {"$set": func_doc[0]}
            )

            # Hapus yang sudah dieksekusi
            filtered_queueToCall.pop(0)
            if filtered_queueToCalltext:
                filtered_queueToCalltext.pop(0)

        AntrianLBL.configure(text="\n".join(queueToCallText))

        # for thread in threads:
        #     thread.join()
        threads = [thread for thread in threads if thread.is_alive()]
        # timerWorker()
        time.sleep(0.1)
        # time.sleep(1)

def unpack_processes(packed_processes: dict):
    # Unpack 8 bits per byte to Jxxxxx keys
    for j in range(16):
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

def listenTriggerMongoDB():
    global changed_keys, updated_queue, updated_var_names

    pipeline = []
    counterAntrian = 0
    if objID:
        pipeline = [{'$match': {'documentKey._id': ObjectId(objID)}}]
    
    with collection.watch(pipeline, max_await_time_ms=1) as stream:
        print("Memantau perubahan di koleksi...")

        if globals()['firstBoot']:
            # Load Data dari Mongo DB disini nanti
            # Default Awal Start
            # globals()['I00195'] = True
            # globals()['I00197'] = True
            # globals()['I00209'] = True
            # globals()['I00212'] = True
            # globals()['I00225'] = True
            # globals()['I00227'] = True
            # globals()['I00229'] = True
            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'I00195': bool(globals()['I00195']),
            #         'I00197': bool(globals()['I00197']),
            #         'I00209': bool(globals()['I00209']),
            #         'I00212': bool(globals()['I00212']),
            #         'I00225': bool(globals()['I00225']),
            #         'I00227': bool(globals()['I00227']),
            #         'I00229': bool(globals()['I00229'])
            #     }})

            document = collection.find_one({"_id": ObjectId(objID)})
            if document:
                for i in range(578):
                    var_name = f'J{i:05}'
                    if var_name in document:
                        # Setel nilai variabel global dengan nilai dari MongoDB
                        globals()[var_name] = document[var_name]

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
            
            _, updated_var_names = localprocessQueue()

            setOutputToRLY()
            globals()['firstBoot'] = False
            globals()['I00032'] = True

        # print(f"globals()['firstBoot'] : {globals()['firstBoot']} - globals()['V0064'] : {globals()['V0064']} - globals()['V0011'] : {globals()['V0011']} - globals()['V0043'] : {globals()['V0043']}")

        for change in stream:
            changed_keys = []
            if change['operationType'] == 'update':
                try:
                    # updateProcess(updated_queue)
                    # Ambil field yang diubah
                    updated_fields = change['updateDescription']['updatedFields']
                    
                    print(f"{updated_fields}")

                    TARGET_QI_KEYS_0_TO_15 = {f"qi{str(j).zfill(4)}glovar" for j in range(16)}
                    TARGET_QJ_KEYS_0_TO_71 = {f"qj{str(j).zfill(4)}latchv" for j in range(72)}

                    for key, value in updated_fields.items():
                        if key in globals() and key not in TARGET_QI_KEYS_0_TO_15:
                            globals()[key] = value

                    if TARGET_QI_KEYS_0_TO_15 & updated_fields.keys():
                        unpack_inputs(updated_fields)

                    if TARGET_QJ_KEYS_0_TO_71 & updated_fields.keys():
                        unpack_processes(updated_fields)

                    _, updated_var_names = localprocessQueue()
                    _, updated_out_names = outQueue()
                    changed_keys.extend(updated_out_names)

                    # EmergencyStop
                    if ('J00543' in changed_keys or 'J00543' in updated_fields or 'J00543' in updated_var_names):
                        globals()['queueToCall'].append(StopAllBecauseEmergencyStop)
                        globals()['queueToCallText'].append(f"{counterAntrian}-StopAllBecauseEmergencyStop")

                    # BuzzeStop
                    if ('I00029' in changed_keys or 'I00029' in updated_fields):
                        globals()['queueToCall'].append(BuzzerStop)
                        globals()['queueToCallText'].append(f"{counterAntrian}-BuzzerStop")

                    # AlarmReset
                    if ('I00030' in changed_keys or 'I00030' in updated_fields):
                        globals()['queueToCall'].append(AlarmReset)
                        globals()['queueToCallText'].append(f"{counterAntrian}-AlarmReset")

                    # LINE Z

                    # # Common Auto
                    if ('V0149' in updated_fields):
                        globals()['queueToCall'].append(V0149func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-V0149func-V0149:{globals()['V0149']}")

                    if ('J00398' in updated_fields or 'J00398' in updated_var_names):
                        globals()['queueToCall'].append(J00398func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00398func-J00398:{globals()['J00398']}")

                    if ('J00399' in updated_fields or 'J00399' in updated_var_names):
                        globals()['queueToCall'].append(J00399func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00399func-J00399:{globals()['J00399']}")

                    if ('J00400' in updated_fields or 'J00400' in updated_var_names):
                        globals()['queueToCall'].append(J00400func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00400func-J00400:{globals()['J00400']}")

                    if ('J00046' in updated_fields or 'J00046' in updated_var_names):
                        globals()['queueToCall'].append(J00046func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00046func-J00046:{globals()['J00046']}")

                    if ('J00047' in updated_fields or 'J00047' in updated_var_names):
                        globals()['queueToCall'].append(J00047func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00047func-J00047:{globals()['J00047']}")

                    if ('J00048' in updated_fields or 'J00048' in updated_var_names):
                        globals()['queueToCall'].append(J00048func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00048func-J00048:{globals()['J00048']}")

                    if ('I00060' in changed_keys or 'I00060' in updated_fields):
                        globals()['queueToCall'].append(I00060func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00060func-I00060:{globals()['I00060']}")

                    if ('I00061' in changed_keys or 'I00061' in updated_fields):
                        globals()['queueToCall'].append(I00061func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00061func-I00061:{globals()['I00061']}")

                    if ('I00062' in changed_keys or 'I00062' in updated_fields):
                        globals()['queueToCall'].append(I00062func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00062func-I00062:{globals()['I00062']}")

                    if ('I00063' in changed_keys or 'I00063' in updated_fields):
                        globals()['queueToCall'].append(I00063func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00063func-I00063:{globals()['I00063']}")

                    if ('I00254' in changed_keys or 'I00254' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append(I00254func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00254func-I00254:{globals()['I00254']}")

                    if ('I00253' in changed_keys or 'I00253' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append(I00253func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00253func-I00253:{globals()['I00253']}")

                    if ('I00255' in changed_keys or 'I00255' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append(I00255func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00255func-I00255:{globals()['I00255']}")

                    if ('I00252' in changed_keys or 'I00252' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append(I00252func)
                        globals()['queueToCallText'].append(f"{counterAntrian}-I00252func-I00252:{globals()['I00252']}")


                    ---

                    ## LINE B
                    # IsJamFault
                    if ('I00024' in changed_keys or 'I00024' in updated_fields):
                        if not globals()['I00024']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00024")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00024:{globals()['I00024']}")

                    if ('I00000' in changed_keys or 'I00000' in updated_fields):
                        if not globals()['I00000']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I0000-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00000:{globals()['I00000']}")

                    if ('I00003' in changed_keys or 'I00003' in updated_fields):
                        if not globals()['I00003']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00003-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00003:{globals()['I00003']}")

                    if ('I00004' in changed_keys or 'I00004' in updated_fields):
                        if not globals()['I00004']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I0004-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00004:{globals()['I00004']}")

                    if ('I00005' in changed_keys or 'I00005' in updated_fields):
                        if not globals()['I00005']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00005-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00005:{globals()['I00005']}")

                    if ('I00011' in changed_keys or 'I00011' in updated_fields):
                        if not globals()['I00011']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00011-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00011:{globals()['I00011']}")

                    if ('I00012' in changed_keys or 'I00012' in updated_fields):
                        if not globals()['I00012']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00012-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00012:{globals()['I00012']}")

                    if ('I00013' in changed_keys or 'I00013' in updated_fields):
                        if not globals()['I00013']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00013-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00013:{globals()['I00013']}")

                    if ('I00025' in changed_keys or 'I00025' in updated_fields):
                        if not globals()['I00025']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        print("I00025-penyebab")
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00025:{globals()['I00025']}")

                    # MotorMaterMixRotorB0
                    if ('J00000' in updated_fields or 'J00352' in updated_fields or 'J00000' in updated_var_names or 'J00352' in updated_var_names or
                            ('J00516' in changed_keys or 'J00516' in updated_fields or 'J00516' in updated_var_names)):
                        globals()['queueToCall'].append(MoveCtrl_MotorMaterMixRotorB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMaterMixRotorB0DoFwd-J00000:{globals()['J00000']}")
                    if ('J00001' in updated_fields or 'J00353' in updated_fields or 'J00001' in updated_var_names or 'J00353' in updated_var_names or
                            ('J00516' in changed_keys or 'J00516' in updated_fields or 'J00516' in updated_var_names)):
                        globals()['queueToCall'].append(MoveCtrl_MotorMaterMixRotorB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMaterMixRotorB0DoRev-J00000:{globals()['J00000']}")

                    # PneumMaterMixDoorB0
                    if ('J00002' in updated_fields or 'J00354' in updated_fields or 'J00002' in updated_var_names or 'J00354' in updated_var_names):
                        globals()['queueToCall'].append(OpenClose_PneumMaterMixDoorB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumMaterMixDoorB0Open-J00002:{globals()['J00002']}")

                    if ('J00003' in updated_fields or 'J00355' in updated_fields or 'J00003' in updated_var_names or 'J00355' in updated_var_names):
                        globals()['queueToCall'].append(OpenClose_PneumMaterMixDoorB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumMaterMixDoorB0Close-J00003:{globals()['J00003']}")

                    if ('I00128' in changed_keys or 'I00128' in updated_fields or 'I00129' in changed_keys or 'I00129' in updated_fields): # Added 'I00129' in changed_keys
                        globals()['queueToCall'].append(TimerK000)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK000-I00128:{globals()['I00128']}")

                    if ('J00512' in updated_fields or 'J00512' in updated_var_names):
                        globals()['queueToCall'].append(PneumMaterMixDoorB0Fault)
                        globals()['queueToCallText'].append("PneumMaterMixDoorB0Fault")
                    if ('J00544' in updated_fields or 'J00544' in updated_var_names or 'I00544' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # MotorMateriVbratorB0
                    if ('J00004' in updated_fields or 'J00356' in updated_fields or 'J00004' in updated_var_names or 'J00356' in updated_var_names or
                            ('J00517' in changed_keys or 'J00517' in updated_fields or 'J00517' in updated_var_names)):
                        globals()['queueToCall'].append(StartNStop_MotorMateriVbratorB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMateriVbratorB0-J00004:{globals()['J00004']}")

                    # MotorMatScrewCnvyrB0
                    if ('J00017' in updated_fields or 'J00369' in updated_fields or 'J00017' in updated_var_names or 'J00369' in updated_var_names):
                        globals()['queueToCall'].append(MoveCtrl_MotorMatScrewCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrB0DoRev-J00017:{globals()['J00017']}")

                    if ('J00016' in updated_fields or 'J00368' in updated_fields or 'J00016' in updated_var_names or 'J00368' in updated_var_names):
                        globals()['queueToCall'].append(MoveCtrl_MotorMatScrewCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrB0DoFwd-J00016:{globals()['J00016']}")

                    if ('J00518' in changed_keys or 'J00518' in updated_fields or 'J00518' in updated_var_names):
                        globals()['queueToCall'].append(MotorMatScrewCnvyrB0Fault)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrB0Fault-J00518:{globals()['J00518']}")

                    # if 'I00147' in updated_fields: # Original commented block, keeping as is
                    #    globals()['queueToCall'].append([TimerK015, globals()['I00147']])
                    #    globals()['queueToCallText'].append(f"{counterAntrian}-TimerK015-I00147:{globals()['I00147']}")

                    # if 'I00149' in updated_fields: # Original commented block, keeping as is
                    #    globals()['queueToCall'].append([TimerK014, globals()['I00149']])
                    #    globals()['queueToCallText'].append(f"{counterAntrian}-TimerK014-I00149:{globals()['I00149']}")

                    # MotorToRotaryCnvyrB0
                    if 'J00005' in updated_fields or 'J00357' in updated_fields or 'J00005' in updated_var_names or 'J00357' in updated_var_names or ('J00519' in changed_keys or 'J00519' in updated_fields or 'J00519' in updated_var_names):
                        globals()['queueToCall'].append(StartNStop_MotorToRotaryCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorToRotaryCnvyrB0-J00005:{globals()['J00005']}")

                    # PneumToRotaryCnvyrB0
                    if 'J00007' in updated_fields or 'J00359' in updated_fields or 'J00007' in updated_var_names or 'J00359' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToRotaryCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrB0-J00007:{globals()['J00007']}")

                    # PneumToRotaryCnvyrB1
                    if 'J00009' in updated_fields or 'J00361' in updated_fields or 'J00009' in updated_var_names or 'J00361' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToRotaryCnvyrB1)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrB1-J00009:{globals()['J00009']}")

                    # PneumToRotaryCnvyrB2
                    if 'J00011' in updated_fields or 'J00363' in updated_fields or 'J00011' in updated_var_names or 'J00363' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToRotaryCnvyrB2)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrB2-J00011:{globals()['J00011']}")

                    # PneumToRotaryCnvyrB3
                    if 'J00013' in updated_fields or 'J00365' in updated_fields or 'J00013' in updated_var_names or 'J00365' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToRotaryCnvyrB3)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrB3-J00013:{globals()['J00013']}")

                    # PneumToRotaryCnvyrB4
                    if 'J00015' in updated_fields or 'J00367' in updated_fields or 'J00015' in updated_var_names or 'J00367' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToRotaryCnvyrB4)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrB4-J00015:{globals()['J00015']}")

                    # MotorFrmRtaryCnvyrB0
                    if 'J00032' in updated_fields or 'J00384' in updated_fields or 'J00032' in updated_var_names or 'J00384' in updated_var_names or ('J00520' in changed_keys or 'J00520' in updated_fields or 'J00520' in updated_var_names):
                        globals()['queueToCall'].append(StartNStop_MotorFrmRtaryCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorFrmRtaryCnvyrB0-J00032:{globals()['J00032']}")

                    # MotorUpladderCnvyrB0
                    if 'J00033' in updated_fields or 'J00385' in updated_fields or 'J00033' in updated_var_names or 'J00385' in updated_var_names or ('J00521' in changed_keys or 'J00521' in updated_fields or 'J00521' in updated_var_names):
                        globals()['queueToCall'].append(StartNStop_MotorUpladderCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorUpladderCnvyrB0-J00033:{globals()['J00033']}")

                    # MotorToHopperCnvyrB0
                    if 'J00018' in updated_fields or 'J00370' in updated_fields or 'J00018' in updated_var_names or 'J00370' in updated_var_names or ('J00522' in changed_keys or 'J00522' in updated_fields or 'J00522' in updated_var_names):
                        globals()['queueToCall'].append(StartNStop_MotorToHopperCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorToHopperCnvyrB0-J00018:{globals()['J00018']}")

                    # PneumToHopperCnvyrB0
                    if 'J00020' in updated_fields or 'J00372' in updated_fields or 'J00020' in updated_var_names or 'J00372' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToHopperCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrB0-J00020:{globals()['J00020']}")

                    # PneumToHopperCnvyrB1
                    if 'J00022' in updated_fields or 'J00374' in updated_fields or 'J00022' in updated_var_names or 'J00374' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToHopperCnvyrB1)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrB1-J00022:{globals()['J00022']}")

                    # PneumToHopperCnvyrB2
                    if 'J00024' in updated_fields or 'J00376' in updated_fields or 'J00024' in updated_var_names or 'J00376' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToHopperCnvyrB2)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrB2-J00024:{globals()['J00024']}")

                    # PneumToHopperCnvyrB3
                    if 'J00026' in updated_fields or 'J00378' in updated_fields or 'J00026' in updated_var_names or 'J00378' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToHopperCnvyrB3)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrB3-J00026:{globals()['J00026']}")

                    # PneumTbletHoprDoorB0
                    if 'J00027' in updated_fields or 'J00379' in updated_fields or 'J00027' in updated_var_names or 'J00379' in updated_var_names:
                        globals()['queueToCall'].append(Open_PneumTbletHoprDoorB0Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorB0Open-J00027:{globals()['J00027']}")

                    if ('I00020' in changed_keys or 'I00020' in updated_fields): # Modified, but kept commented in original and now includes changed_keys
                        if globals()['I00020'] and globals()['J00379']  :
                            globals()['queueToCall'].append(PneumTbletHoprDoorB0Open)
                            globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorB0Close-J00028:{globals()['J00028']}")
                    if ('I00021' in changed_keys or 'I00021' in updated_fields): # Modified, but kept commented in original and now includes changed_keys
                        if globals()['I00021'] and globals()['J00379']  :
                            globals()['queueToCall'].append(PneumTbletHoprDoorB0Open)
                            globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorB0Close-J00028:{globals()['J00028']}")
                    if ('I00164' in changed_keys or 'I00164' in updated_fields or 'I00165' in changed_keys or 'I00165' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK001)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK001-I00164:{globals()['I00164']}")

                    if 'J00513' in updated_fields or 'J00513' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorB0Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorB0Fault")
                    if ('J00545' in updated_fields or 'J00545' in updated_var_names or 'I00545' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # PneumTbletHoprDoorB1
                    if ('J00029' in updated_fields or 'J00029' in updated_var_names) or ('J00381' in updated_fields or 'J00381' in updated_var_names):
                        globals()['queueToCall'].append(Open_PneumTbletHoprDoorB1Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorB1Open-J00027:{globals()['J00027']}")
                    if ('I00022' in changed_keys or 'I00022' in updated_fields): # Modified, but kept commented in original and now includes changed_keys
                        if globals()['I00022'] and globals()['J00381']  :
                            globals()['queueToCall'].append(PneumTbletHoprDoorB1Open)
                            globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorB1Close-J00028:{globals()['J00028']}")
                    if ('I00023' in changed_keys or 'I00023' in updated_fields): # Modified, but kept commented in original and now includes changed_keys
                        if globals()['I00023'] and globals()['J00381']  :
                            globals()['queueToCall'].append(PneumTbletHoprDoorB1Open)
                            globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorB1Close-J00028:{globals()['J00028']}")
                    if ('I00166' in changed_keys or 'I00166' in updated_fields or 'I00167' in changed_keys or 'I00167' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK002)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK002-I00166:{globals()['I00166']}")

                    if 'J00514' in updated_fields or 'J00514' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorB1Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorB1Fault")
                    if ('J00546' in updated_fields or 'J00546' in updated_var_names or 'I00546' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # MotorTbletHoprDoorB0
                    if 'J00031' in updated_fields or 'J00383' in updated_fields or 'J00515' in updated_fields or \
                            'J00031' in updated_var_names or 'J00383' in updated_var_names or 'J00515' in updated_var_names:
                        globals()['queueToCall'].append(StartNStop_MotorTbletHoprDoorB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorTbletHoprDoorB0-J00031:{globals()['J00031']}")

                    # MotorToRnCenCnyrB0
                    if 'J00034' in updated_fields or 'J00386' in updated_fields or ('J00523' in changed_keys or 'J00523' in updated_fields) or \
                            'J00034' in updated_var_names or 'J00386' in updated_var_names or 'J00523' in updated_var_names:
                        globals()['queueToCall'].append(StartNStop_MotorToRncenCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorToRncenCnvyrB0-J00034:{globals()['J00034']}")

                    # PneumToRncenCnvyrB0
                    if 'J00036' in updated_fields or 'J00388' in updated_fields or \
                            'J00036' in updated_var_names or 'J00388' in updated_var_names:
                        globals()['queueToCall'].append(Close_PneumToRncenCnvyrB0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRncenCnvyrB0-J00036:{globals()['J00036']}")

                    # Timer K016 - K026
                    if ('I00006' in changed_keys or 'I00006' in updated_fields):
                        globals()['queueToCall'].append([TimerK016, globals()['I00006']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK016-I00006:{globals()['I00006']}")
                    if ('I00007' in changed_keys or 'I00007' in updated_fields):
                        globals()['queueToCall'].append([TimerK017, globals()['I00007']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK017-I00007:{globals()['I00007']}")
                    if ('I00008' in changed_keys or 'I00008' in updated_fields):
                        globals()['queueToCall'].append([TimerK018, globals()['I00008']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK018-I00008:{globals()['I00008']}")
                    if ('I00009' in changed_keys or 'I00009' in updated_fields):
                        globals()['queueToCall'].append([TimerK019, globals()['I00009']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK019-I00009:{globals()['I00009']}")
                    if ('I00010' in changed_keys or 'I00010' in updated_fields):
                        globals()['queueToCall'].append([TimerK020, globals()['I00010']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK020-I00010:{globals()['I00010']}")
                    if ('I00016' in changed_keys or 'I00016' in updated_fields):
                        globals()['queueToCall'].append([TimerK021, globals()['I00016']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK021-I00016:{globals()['I00016']}")
                    if ('I00017' in changed_keys or 'I00017' in updated_fields):
                        globals()['queueToCall'].append([TimerK022, globals()['I00017']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK022-I00017:{globals()['I00017']}")
                    if ('I00018' in changed_keys or 'I00018' in updated_fields):
                        globals()['queueToCall'].append([TimerK023, globals()['I00018']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK023-I00018:{globals()['I00018']}")
                    if ('I00019' in changed_keys or 'I00019' in updated_fields):
                        globals()['queueToCall'].append([TimerK024, globals()['I00019']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK024-I00019:{globals()['I00019']}")
                    if ('I00014' in changed_keys or 'I00014' in updated_fields):
                        globals()['queueToCall'].append([TimerK025, globals()['I00014']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK025-I00014:{globals()['I00014']}")
                    if ('I00015' in changed_keys or 'I00015' in updated_fields):
                        globals()['queueToCall'].append([TimerK026, globals()['I00015']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK026-I00015:{globals()['I00015']}")

                    # Line B - Feeder Auto
                    if 'V0144' in updated_fields or 'J00140' in updated_fields or 'J00141' in updated_fields or 'J00142' in updated_fields or 'J00143' in updated_fields or \
                            'J00140' in updated_var_names or 'J00141' in updated_var_names or 'J00142' in updated_var_names or 'J00143' in updated_var_names:
                        globals()['queueToCall'].append(autoFeederLineB)
                        globals()['queueToCallText'].append(f"{counterAntrian}-autoFeederLineB")

                    if 'V0153' in updated_fields:
                        globals()['queueToCall'].append(V0153change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-V0153change")

                    # Line B - Hopper Auto
                    if 'V0145' in updated_fields:
                        globals()['queueToCall'].append(autoHopperLineB)
                        globals()['queueToCallText'].append(f"{counterAntrian}-autoHopperLineB")
                    if 'V0152' in updated_fields:
                        globals()['queueToCall'].append(V0152change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-V0152change")
                    if 'J00135' in updated_fields or 'J00135' in updated_var_names:
                        globals()['queueToCall'].append(J00135change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00135change")
                    if 'J00136' in updated_fields or 'J00136' in updated_var_names:
                        globals()['queueToCall'].append(J00136change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00136change")
                    if 'J00137' in updated_fields or 'J00137' in updated_var_names:
                        globals()['queueToCall'].append(J00137change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00137change")
                    if 'J00138' in updated_fields or 'J00138' in updated_var_names:
                        globals()['queueToCall'].append(J00138change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00138change")
                    if 'J00139' in updated_fields or 'J00139' in updated_var_names:
                        globals()['queueToCall'].append(J00139change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00139change")
                    if 'J00144' in updated_fields or 'J00144' in updated_var_names:
                        globals()['queueToCall'].append(J00144change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00144change")
                    if 'J00145' in updated_fields or 'J00145' in updated_var_names:
                        globals()['queueToCall'].append(J00145change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00145change")

                    # Fill Mixer Line B
                    if 'J00037' in updated_fields or 'J00389' in updated_fields or 'J00244' in updated_fields or 'J00245' in updated_fields or \
                            'J00037' in updated_var_names or 'J00389' in updated_var_names or 'J00244' in updated_var_names or 'J00245' in updated_var_names:
                        globals()['queueToCall'].append(FillerMixerBLogic)
                        globals()['queueToCallText'].append(f"{counterAntrian}-FillerMixerBLogic")

                    # Dump Mixer Line B
                    if 'J00038' in updated_fields or 'J00245' in updated_fields or 'J00243' in updated_fields or \
                            'J00038' in updated_var_names or 'J00245' in updated_var_names or 'J00243' in updated_var_names:
                        globals()['queueToCall'].append(DumpMixerBLogic)
                        globals()['queueToCallText'].append(f"{counterAntrian}-DumpMixerBLogic")

                    # Line B - Timer K011 Auto update pemisah parameter
                    if ('I00144' in changed_keys or 'I00144' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([TimerK011, globals()['I00144']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-autoFeederLineB")
                        globals()['queueToCall'].append([MoveChecker, ('I00144', 'J00289', 'V0013', 'U0013', 'K013')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoFwdMotorMaterMixerRotorB0Checker")
                        
                    if ('I00146' in changed_keys or 'I00146' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00146', 'J00288', 'V0012', 'U0012', 'K012')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoRevMotorMaterMixerRotorB0Checker")

                    if ('I00147' in changed_keys or 'I00147' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00147', 'J00291', 'V0015', 'U0015', 'K015')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoFwdToMotorMatScrewCnvyrB0Checker")

                    if ('I00149' in changed_keys or 'I00149' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00149', 'J00290', 'V0014', 'U0014', 'K014')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoRevToMotorMatScrewCnvyrB0Checker")

                    if ('I00208' in changed_keys or 'I00208' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00208', 'J00295', 'V0045', 'U0045', 'K045')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoFwdMotorMaterMixerRotorC0Checker")

                    if ('I00210' in changed_keys or 'I00210' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00210', 'J00294', 'V0044', 'U0044', 'K044')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoRevMotorMaterMixerRotorC0Checker")

                    if ('I00211' in changed_keys or 'I00211' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00211', 'J00297', 'V0047', 'U0047', 'K047')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoFwdToMotorMatScrewCnvyrC0Checker")
                        
                    if ('I00213' in changed_keys or 'I00213' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([MoveChecker, ('I00213', 'J00296', 'V0046', 'U0046', 'K046')])
                        globals()['queueToCallText'].append(f"{counterAntrian}-DoRevMotorMaterMixerRotorC0Checker")

                    if 'J00244' in updated_fields or 'J00244' in updated_var_names:
                        globals()['queueToCall'].append(ResetTimerK011)
                        globals()['queueToCallText'].append(f"{counterAntrian}-ResetTimerK011")

                    ---

                    ## LINE C
                    # IsJamFault
                    if ('I00064' in changed_keys or 'I00064' in updated_fields):
                        if not globals()['I00064']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00064:{globals()['I00064']}")
                    if ('I00067' in changed_keys or 'I00067' in updated_fields):
                        if not globals()['I00067']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00067:{globals()['I00067']}")
                    if ('I00068' in changed_keys or 'I00068' in updated_fields):
                        if not globals()['I00068']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00068:{globals()['I00068']}")
                    if ('I00069' in changed_keys or 'I00069' in updated_fields):
                        if not globals()['I00069']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00069:{globals()['I00069']}")
                    if ('I00083' in changed_keys or 'I00083' in updated_fields):
                        if not globals()['I00083']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00083:{globals()['I00083']}")
                    if ('I00084' in changed_keys or 'I00084' in updated_fields):
                        if not globals()['I00084']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00084:{globals()['I00084']}")
                    if ('I00085' in changed_keys or 'I00085' in updated_fields):
                        if not globals()['I00085']:
                            calculateV0157ToPanelAlarmErrorSourcesZ0err()
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append(f"{counterAntrian}-calculateV0157z-I00085:{globals()['I00085']}")

                    # MotorMaterMixRotorC0
                    if 'J00059' in updated_fields or 'J00411' in updated_fields or \
                            'J00059' in updated_var_names or 'J00411' in updated_var_names:
                        globals()['queueToCall'].append(MotorMaterMixRotorC0DoFwd)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMaterMixRotorC0DoFwd-J00059:{globals()['J00059']}")
                    if 'J00060' in updated_fields or 'J00412' in updated_fields or \
                            'J00060' in updated_var_names or 'J00412' in updated_var_names:
                        globals()['queueToCall'].append(MotorMaterMixRotorC0DoRev)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMaterMixRotorC0DoRev-J00060:{globals()['J00060']}")
                    if ('I00209' in changed_keys or 'I00209' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append(MotorMaterMixRotorC0DoStop)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMaterMixRotorC0DoStop-I00209:{globals()['I00209']}")
                    if 'J00534' in updated_fields or 'J00534' in updated_var_names:
                        globals()['queueToCall'].append(MotorMaterMixRotorC0Fault)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMaterMixRotorC0Fault-J00534:{globals()['J00534']}")

                    # PneumMaterMixDoorC0
                    if 'J00061' in updated_fields or 'J00413' in updated_fields or \
                            'J00061' in updated_var_names or 'J00413' in updated_var_names:
                        globals()['queueToCall'].append(PneumMaterMixDoorC0Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumMaterMixDoorC0Open-J00061:{globals()['J00061']}")
                    if 'J00062' in updated_fields or 'J00414' in updated_fields or \
                            'J00062' in updated_var_names or 'J00414' in updated_var_names:
                        globals()['queueToCall'].append(PneumMaterMixDoorC0Close)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumMaterMixDoorC0Close-J00062:{globals()['J00062']}")
                    if ('I00192' in changed_keys or 'I00192' in updated_fields or 'I00193' in changed_keys or 'I00193' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK032)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK032-I00192:{globals()['I00192']}")
                    if 'J00528' in updated_fields or 'J00528' in updated_var_names:
                        globals()['queueToCall'].append(PneumMaterMixDoorC0Fault)
                        globals()['queueToCallText'].append("PneumMaterMixDoorC0Fault")
                    if ('J00560' in updated_fields or 'J00560' in updated_var_names or 'I00560' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # MotorMateriVbratorC0
                    if 'J00080' in updated_fields or 'J00432' in updated_fields or 'J00535' in updated_fields or \
                            'J00080' in updated_var_names or 'J00432' in updated_var_names or 'J00535' in updated_var_names:
                        globals()['queueToCall'].append(MotorMateriVbratorC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMateriVbratorC0-J00080:{globals()['J00080']}")

                    # MotorMatScrewCnvyrC0
                    if 'J00082' in updated_fields or 'J00434' in updated_fields or \
                            'J00082' in updated_var_names or 'J00434' in updated_var_names:
                        globals()['queueToCall'].append(MotorMatScrewCnvyrC0DoRev)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrC0DoRev-J00082:{globals()['J00082']}")
                    if 'J00081' in updated_fields or 'J00433' in updated_fields or \
                            'J00081' in updated_var_names or 'J00433' in updated_var_names:
                        globals()['queueToCall'].append(MotorMatScrewCnvyrC0DoFwd)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrC0DoFwd-J00081:{globals()['J00081']}")
                    if ('I00212' in changed_keys or 'I00212' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append(MotorMatScrewCnvyrC0DoStop)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrC0DoStop-I00212:{globals()['I00212']}")
                    if 'J00536' in updated_fields or 'J00536' in updated_var_names:
                        globals()['queueToCall'].append(MotorMatScrewCnvyrC0Fault)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorMatScrewCnvyrC0Fault-J00536:{globals()['J00536']}")

                    # MotorToRotaryCnvyrC0
                    if 'J00063' in updated_fields or 'J00415' in updated_fields or 'J00537' in updated_fields or \
                            'J00063' in updated_var_names or 'J00415' in updated_var_names or 'J00537' in updated_var_names:
                        globals()['queueToCall'].append(MotorToRotaryCnvyrC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorToRotaryCnvyrC0-J00063:{globals()['J00063']}")

                    # PneumToRotaryCnvyrC0
                    if 'J00065' in updated_fields or 'J00417' in updated_fields or \
                            'J00065' in updated_var_names or 'J00417' in updated_var_names:
                        globals()['queueToCall'].append(PneumToRotaryCnvyrC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrC0-J00065:{globals()['J00065']}")

                    # PneumToRotaryCnvyrC1
                    if 'J00067' in updated_fields or 'J00419' in updated_fields or \
                            'J00067' in updated_var_names or 'J00419' in updated_var_names:
                        globals()['queueToCall'].append(PneumToRotaryCnvyrC1)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrC1-J00067:{globals()['J00067']}")

                    # PneumToRotaryCnvyrC2
                    if 'J00069' in updated_fields or 'J00421' in updated_fields or \
                            'J00069' in updated_var_names or 'J00421' in updated_var_names:
                        globals()['queueToCall'].append(PneumToRotaryCnvyrC2)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToRotaryCnvyrC2-J00069:{globals()['J00069']}")

                    # MotorFrmRtaryCnvyrC0
                    if 'J00083' in updated_fields or 'J00435' in updated_fields or 'J00538' in updated_fields or \
                            'J00083' in updated_var_names or 'J00435' in updated_var_names or 'J00538' in updated_var_names:
                        globals()['queueToCall'].append(MotorFrmRtaryCnvyrC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorFrmRtaryCnvyrC0-J00083:{globals()['J00083']}")

                    # MotorUpladderCnvyrC0
                    if 'J00084' in updated_fields or 'J00436' in updated_fields or 'J00539' in updated_fields or \
                            'J00084' in updated_var_names or 'J00436' in updated_var_names or 'J00539' in updated_var_names:
                        globals()['queueToCall'].append(MotorUpladderCnvyrC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorUpladderCnvyrC0-J00084:{globals()['J00084']}")

                    # MotorToHopperCnvyrC0
                    if 'J00085' in updated_fields or 'J00437' in updated_fields or 'J00540' in updated_fields or \
                            'J00085' in updated_var_names or 'J00437' in updated_var_names or 'J00540' in updated_var_names:
                        globals()['queueToCall'].append(MotorToHopperCnvyrC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-MotorToHopperCnvyrC0-J00085:{globals()['J00085']}")

                    # PneumToHopperCnvyrC0
                    if 'J00087' in updated_fields or 'J00439' in updated_fields or \
                            'J00087' in updated_var_names or 'J00439' in updated_var_names:
                        globals()['queueToCall'].append(PneumToHopperCnvyrC0)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrC0-J00087:{globals()['J00087']}")

                    # PneumToHopperCnvyrC1
                    if 'J00089' in updated_fields or 'J00441' in updated_fields or \
                            'J00089' in updated_var_names or 'J00441' in updated_var_names:
                        globals()['queueToCall'].append(PneumToHopperCnvyrC1)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrC1-J00089:{globals()['J00089']}")

                    # PneumToHopperCnvyrC2
                    if 'J00091' in updated_fields or 'J00443' in updated_fields or \
                            'J00091' in updated_var_names or 'J00443' in updated_var_names:
                        globals()['queueToCall'].append(PneumToHopperCnvyrC2)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrC2-J00091:{globals()['J00091']}")

                    # PneumToHopperCnvyrC3
                    if 'J00093' in updated_fields or 'J00445' in updated_fields or \
                            'J00093' in updated_var_names or 'J00445' in updated_var_names:
                        globals()['queueToCall'].append(PneumToHopperCnvyrC3)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrC3-J00093:{globals()['J00093']}")

                    # PneumToHopperCnvyrC4
                    if 'J00095' in updated_fields or 'J00447' in updated_fields or \
                            'J00095' in updated_var_names or 'J00447' in updated_var_names:
                        globals()['queueToCall'].append(PneumToHopperCnvyrC4)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumToHopperCnvyrC4-J00095:{globals()['J00095']}")

                    # PneumTbletHoprDoorC0
                    if 'J00070' in updated_fields or 'J00070' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC0Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC0Open-J00070:{globals()['J00070']}")
                    if 'J00071' in updated_fields or 'J00071' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC0Close)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC0Close-J00071:{globals()['J00071']}")
                    if ('I00214' in changed_keys or 'I00214' in updated_fields or 'I00215' in changed_keys or 'I00215' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK033)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK033-I00214:{globals()['I00214']}")
                    if 'J00529' in updated_fields or 'J00529' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC0Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorC0Fault")
                    if ('J00561' in updated_fields or 'J00561' in updated_var_names or 'I00561' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # PneumTbletHoprDoorC1
                    if 'J00072' in updated_fields or 'J00072' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC1Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC1Open-J00072:{globals()['J00072']}")
                    if 'J00073' in updated_fields or 'J00073' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC1Close)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC1Close-J00073:{globals()['J00073']}")
                    if ('I00216' in changed_keys or 'I00216' in updated_fields or 'I00217' in changed_keys or 'I00217' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK034)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK034-I00216:{globals()['I00216']}")
                    if 'J00530' in updated_fields or 'J00530' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC1Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorC1Fault")
                    if ('J00562' in updated_fields or 'J00562' in updated_var_names or 'I00562' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # PneumTbletHoprDoorC2
                    if 'J00074' in updated_fields or 'J00074' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC2Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC2Open-J00074:{globals()['J00074']}")
                    if 'J00075' in updated_fields or 'J00075' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC2Close)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC2Close-J00075:{globals()['J00075']}")
                    if ('I00218' in changed_keys or 'I00218' in updated_fields or 'I00219' in changed_keys or 'I00219' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK035)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK035-I00218:{globals()['I00218']}")
                    if 'J00531' in updated_fields or 'J00531' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC2Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorC2Fault")
                    if ('J00563' in updated_fields or 'J00563' in updated_var_names or 'I00563' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # PneumTbletHoprDoorC3
                    if 'J00076' in updated_fields or 'J00076' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC3Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC3Open-J00076:{globals()['J00076']}")
                    if 'J00077' in updated_fields or 'J00077' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC3Close)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC3Close-J00077:{globals()['J00077']}")
                    if ('I00220' in changed_keys or 'I00220' in updated_fields or 'I00221' in changed_keys or 'I00221' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK036)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK036-I00220:{globals()['I00220']}")
                    if 'J00532' in updated_fields or 'J00532' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC3Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorC3Fault")
                    if ('J00564' in updated_fields or 'J00564' in updated_var_names or 'I00564' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # PneumTbletHoprDoorC4
                    if 'J00078' in updated_fields or 'J00078' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC4Open)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC4Open-J00078:{globals()['J00078']}")
                    if 'J00079' in updated_fields or 'J00079' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC4Close)
                        globals()['queueToCallText'].append(f"{counterAntrian}-PneumTbletHoprDoorC4Close-J00079:{globals()['J00079']}")
                    if ('I00222' in changed_keys or 'I00222' in updated_fields or 'I00223' in changed_keys or 'I00223' in updated_fields): # Added changed_keys for both
                        globals()['queueToCall'].append(TimerK037)
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK037-I00222:{globals()['I00222']}")
                    if 'J00533' in updated_fields or 'J00533' in updated_var_names:
                        globals()['queueToCall'].append(PneumTbletHoprDoorC4Fault)
                        globals()['queueToCallText'].append("PneumTbletHoprDoorC4Fault")
                    if ('J00565' in updated_fields or 'J00565' in updated_var_names or 'I00565' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # Timer K048 - K060 Update Pemisah parameter dengan fungsi
                    if ('I00080' in changed_keys or 'I00080' in updated_fields):
                        globals()['queueToCall'].append([TimerK048, globals()['I00080']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK048-I00080:{globals()['I00080']}")
                    if ('I00081' in changed_keys or 'I00081' in updated_fields):
                        globals()['queueToCall'].append([TimerK049, globals()['I00081']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK049-I00081:{globals()['I00081']}")
                    if ('I00082' in changed_keys or 'I00082' in updated_fields):
                        globals()['queueToCall'].append([TimerK050, globals()['I00082']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK050-I00082:{globals()['I00082']}")
                    if ('I00086' in changed_keys or 'I00086' in updated_fields):
                        globals()['queueToCall'].append([TimerK051, globals()['I00086']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK051-I00086:{globals()['I00086']}")
                    if ('I00087' in changed_keys or 'I00087' in updated_fields):
                        globals()['queueToCall'].append([TimerK052, globals()['I00087']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK052-I00087:{globals()['I00087']}")
                    if ('I00088' in changed_keys or 'I00088' in updated_fields):
                        globals()['queueToCall'].append([TimerK053, globals()['I00088']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK053-I00088:{globals()['I00088']}")
                    if ('I00089' in changed_keys or 'I00089' in updated_fields):
                        globals()['queueToCall'].append([TimerK054, globals()['I00089']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK054-I00089:{globals()['I00089']}")
                    if ('I00090' in changed_keys or 'I00090' in updated_fields):
                        globals()['queueToCall'].append([TimerK055, globals()['I00090']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK055-I00090:{globals()['I00090']}")
                    if ('I00091' in changed_keys or 'I00091' in updated_fields):
                        globals()['queueToCall'].append([TimerK056, globals()['I00091']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK056-I00091:{globals()['I00091']}")
                    if ('I00092' in changed_keys or 'I00092' in updated_fields):
                        globals()['queueToCall'].append([TimerK057, globals()['I00092']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK057-I00092:{globals()['I00092']}")
                    if ('I00093' in changed_keys or 'I00093' in updated_fields):
                        globals()['queueToCall'].append([TimerK058, globals()['I00093']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK058-I00093:{globals()['I00093']}")
                    if ('I00094' in changed_keys or 'I00094' in updated_fields):
                        globals()['queueToCall'].append([TimerK059, globals()['I00094']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK059-I00094:{globals()['I00094']}")
                    if ('I00095' in changed_keys or 'I00095' in updated_fields):
                        globals()['queueToCall'].append([TimerK060, globals()['I00095']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK060-I00095:{globals()['I00095']}")

                    # Line C - Feeder Auto
                    if 'V0146' in updated_fields or 'J00203' in updated_fields or 'J00204' in updated_fields or 'J00205' in updated_fields or 'J00206' in updated_fields or 'J00207' in updated_fields or \
                            'J00203' in updated_var_names or 'J00204' in updated_var_names or 'J00205' in updated_var_names or 'J00206' in updated_var_names or 'J00207' in updated_var_names:
                        globals()['queueToCall'].append(autoFeederLineC)
                        globals()['queueToCallText'].append(f"{counterAntrian}-autoFeederLineC")
                    if 'V0154' in updated_fields:
                        globals()['queueToCall'].append(V0154change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-V0154change")
                    if 'J00208' in updated_fields or 'J00209' in updated_fields or 'J00210' in updated_fields or \
                            'J00208' in updated_var_names or 'J00209' in updated_var_names or 'J00210' in updated_var_names:
                        globals()['queueToCall'].append(J00208change)
                        globals()['queueToCallText'].append(f"{counterAntrian}-J00208change")

                    # Fill Mixer Line C
                    if 'J00057' in updated_fields or 'J00410' in updated_fields or 'J00250' in updated_fields or 'J00251' in updated_fields or \
                            'J00057' in updated_var_names or 'J00410' in updated_var_names or 'J00250' in updated_var_names or 'J00251' in updated_var_names:
                        globals()['queueToCall'].append(FillerMixerCLogic)
                        globals()['queueToCallText'].append(f"{counterAntrian}-FillerMixerCLogic")

                    # Dump Mixer Line C
                    if 'J00058' in updated_fields or 'J00254' in updated_fields or 'J00249' in updated_fields or \
                            'J00058' in updated_var_names or 'J00254' in updated_var_names or 'J00249' in updated_var_names:
                        globals()['queueToCall'].append(DumpMixerCLogic)
                        globals()['queueToCallText'].append(f"{counterAntrian}-DumpMixerCLogic")

                    # Line C - Timer K043 Auto
                    if ('I00208' in changed_keys or 'I00208' in updated_fields): # Added changed_keys
                        globals()['queueToCall'].append([TimerK043, globals()['I00208']])
                        globals()['queueToCallText'].append(f"{counterAntrian}-TimerK043")
                    if 'J00249' in updated_fields or 'J00249' in updated_var_names:
                        globals()['queueToCall'].append(ResetTimerK043)
                        globals()['queueToCallText'].append(f"{counterAntrian}-ResetTimerK043")

                    # Line C - Hopper Auto
                    if 'V0147' in updated_fields or 'J00198' in updated_fields or 'J00199' in updated_fields or 'J00200' in updated_fields or 'J00201' in updated_fields or 'J00202' in updated_fields or \
                            'J00198' in updated_var_names or 'J00199' in updated_var_names or 'J00200' in updated_var_names or 'J00201' in updated_var_names or 'J00202' in updated_var_names:
                        globals()['queueToCall'].append(autoHopperLineC)
                        globals()['queueToCallText'].append(f"{counterAntrian}-autoHopperLineC")

                    ---

                    ## ERROR BUZZER
                    if ('V0157' in updated_fields or 'V0157' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")
                    if ('V0158' in updated_fields or 'V0158' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")
                    if ('V0159' in updated_fields or 'V0159' in changed_keys):
                        globals()['queueToCall'].append(errBuzzUpdated)
                        globals()['queueToCallText'].append("errBuzzUpdated")

                    # AntrianLBL.configure(text="\n".join(queueToCallText))
                    # updated_queue, updated_var_names = processQueue()

                except KeyError as e:
                    print(f"Error accessing updated fields: {e}")


# EMERGENCY CODE
def StopAllBecauseEmergencyStop():
    print("--->1")
    globals()['V0144'] = 0
    print("--->2")
    globals()['V0145'] = 0
    print("--->3")
    globals()['V0146'] = 0
    print("--->4")
    globals()['V0147'] = 0
    print("--->5")
    globals()['V0149'] = 0
    print("--->6")
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0144': 0,
            'V0145': 0,
            'V0146': 0,
            'V0147': 0,
            'V0149': 0
        }})

    # Line Z
    # PneumFeedThreeDoorZ0Close()
    # PneumFeedThreeDoorZ0Open()
    # PneumFeedThreeDoorZ1Close()
    # PneumFeedThreeDoorZ1Open()

    # Line B
    print("--->7")
    MoveCtrl_MotorMaterMixRotorB0()
    MoveCtrl_MotorMatScrewCnvyrB0()
    print("--->8")
    StartNStop_MotorMateriVbratorB0()
    StartNStop_MotorToRotaryCnvyrB0()
    StartNStop_MotorFrmRtaryCnvyrB0()
    StartNStop_MotorUpladderCnvyrB0()
    StartNStop_MotorToHopperCnvyrB0()
    print("--->9")
    OpenClose_PneumMaterMixDoorB0()
    Close_PneumToRotaryCnvyrB0()
    Close_PneumToRotaryCnvyrB2()
    Close_PneumToRotaryCnvyrB1()
    Close_PneumToRotaryCnvyrB3()
    Close_PneumToRotaryCnvyrB4()
    Close_PneumToHopperCnvyrB0()
    Close_PneumToHopperCnvyrB1()
    Close_PneumToHopperCnvyrB2()
    Close_PneumToHopperCnvyrB3()
    StartNStop_MotorTbletHoprDoorB0()
    StartNStop_MotorToRncenCnvyrB0()
    print("--->10")
    # PneumTbletHoprDoorB0Close()
    Open_PneumTbletHoprDoorB0Open()
    # PneumTbletHoprDoorB1Close()
    Open_PneumTbletHoprDoorB1Open()
    Close_PneumToRncenCnvyrB0()
    print("--->11")
    # Line C
    MotorMaterMixRotorC0DoFwd()
    MotorMaterMixRotorC0DoRev()
    MotorMatScrewCnvyrC0DoFwd()
    MotorMatScrewCnvyrC0DoRev()
    MotorMateriVbratorC0()
    MotorToRotaryCnvyrC0()
    MotorFrmRtaryCnvyrC0()
    MotorUpladderCnvyrC0()
    MotorToHopperCnvyrC0()
    PneumMaterMixDoorC0Open()
    PneumMaterMixDoorC0Close()
    PneumToRotaryCnvyrC0()
    PneumToRotaryCnvyrC1()
    PneumToRotaryCnvyrC2()
    PneumToHopperCnvyrC0()
    PneumToHopperCnvyrC1()
    PneumToHopperCnvyrC2()
    PneumToHopperCnvyrC3()
    PneumToHopperCnvyrC4()
    PneumTbletHoprDoorC0Close()
    PneumTbletHoprDoorC0Open()
    PneumTbletHoprDoorC1Close()
    PneumTbletHoprDoorC1Open()
    PneumTbletHoprDoorC2Close()
    PneumTbletHoprDoorC2Open()
    PneumTbletHoprDoorC3Close()
    PneumTbletHoprDoorC3Open()
    PneumTbletHoprDoorC4Close()
    PneumTbletHoprDoorC4Open()
    print("--->12")

# LOGIC CODE LINE COMMON
def J00398func():
    DoCloseZ0()
    DoOpenZ1()
    J00302func()

def J00399func():
    DoCloseZ1()
    DoOpenZ0()
    J00303func()

def J00400func():
    DoCloseZ0()
    DoCloseZ1()
    J00304func()

def J00046func():
    DoCloseZ0()
    DoOpenZ1()
    J00302func()

def J00047func():
    print("exec J00047func")
    DoCloseZ1()
    DoOpenZ0()
    J00303func()

def J00048func():
    DoCloseZ0()
    DoCloseZ1()
    J00304func()

def I00060func():
    DoOpenZ0()
    J00175func()
    # TimerK064()

def I00061func():
    DoCloseZ0()
    DoOpenZ1()
    J00176func()
    J00174func()
    # TimerK064()

def I00062func():
    DoOpenZ1()
    J00174func()
    # TimerK065()

def I00063func():
    DoCloseZ1()
    DoOpenZ0()
    J00176func()
    J00175func()
    # TimerK065()

def I00254func():
    J00302func()
    TimerK065()

def I00253func():
    J00302func()
    J00304func()
    TimerK064()

def I00255func():
    J00304func()
    J00303func()
    TimerK065()

def I00252func():
    J00303func()
    TimerK064()

def DoCloseZ0():
    syaratAtas = frame5and2or4and(globals()['I00028'], globals()['J00543'], globals()['J00526'], globals()['V0149'], globals()['J00400'], globals()['J00048'], globals()['I00061'])
    syaratBawah = frame5and2or4and(globals()['I00028'], globals()['J00543'], globals()['J00526'], globals()['V0149'], globals()['J00398'], globals()['J00046'], globals()['I00061'])
    # globals()['I00253'] = syaratAtas or syaratBawah
    if syaratAtas or syaratBawah:
        globals()['I00253'] = True
    else:
        globals()['I00253'] = False
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00253': bool(globals()['I00253'])
    #     }})
        
    setOutputToRLY()

def TimerK064():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00060'], globals()['I00252'], globals()['I00061'], globals()['I00253']):
        
        print("TimerK064 RUN")
        start_timer("K064V0064IsJam", globals()['V0064'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00060'], globals()['I00252'], globals()['I00061'], globals()['I00253']):
        print("jidTimerK064 STOOOP")
        stop_timer("K064V0064IsJam")

def TimerK065():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00062'], globals()['I00254'], globals()['I00063'], globals()['I00255']):
        
        print("TimerK065 RUN")
        start_timer("K065V0065IsJam", globals()['V0065'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00062'], globals()['I00254'], globals()['I00063'], globals()['I00255']):
        print("jidTimerK065 STOOOP")
        stop_timer("K065V0065IsJam")

def DoCloseZ1():
    orZ0Close = ((bool(globals()['V0149']) and globals()['J00400']) or (not bool(globals()['V0149']) and globals()['J00048']))
    syaratAtas = bool(globals()['I00028']) and not bool(globals()['J00543']) and not bool(globals()['J00527']) and orZ0Close and not bool(globals()['I00063'])

    orZ0Open = ((bool(globals()['V0149']) and globals()['J00399']) or (not bool(globals()['V0149']) and globals()['J00047']))
    syaratBawah = bool(globals()['I00028']) and not bool(globals()['J00543']) and not bool(globals()['J00527']) and orZ0Open and not bool(globals()['I00063'])

    # globals()['I00255'] = syaratAtas or syaratBawah

    if syaratAtas or syaratBawah:
        globals()['I00255'] = True
    else:
        globals()['I00255'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00255': bool(globals()['I00255'])
    #     }})
        
    setOutputToRLY()

def DoOpenZ0():

    globals()['I00252'] = bool(globals()['I00028'] and not globals()['J00543'] and not globals()['J00526'] and ((bool(globals()['V0149']) and globals()['J00399']) or (not bool(globals()['V0149']) and bool(globals()['J00047']))) and bool(globals()['I00163']) and not bool(globals()['I00060']))

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00252': bool(globals()['I00252'])
    #     }})
        
    setOutputToRLY()

def DoOpenZ1():
    globals()['I00254'] = bool(globals()['I00028'] and not globals()['J00543'] and not globals()['J00527'] and ((bool(globals()['V0149']) and globals()['J00398']) or (not bool(globals()['V0149']) and bool(globals()['J00046']))) and bool(globals()['I00161']) and not bool(globals()['I00062']))

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00254': bool(globals()['I00254'])
    #     }})
        
    setOutputToRLY()

# def IsLineAans():
#     globals()['J00176'] = bool(globals()['I00061'] and globals()['I00063'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'J00176': bool(globals()['J00176'])
#         }})
        
#     setOutputToRLY()

# def ToLineChld():
#     globals()['J00302'] = bool((globals()['I00254'] and (globals()['J00398'] or globals()['J00046'])) or ((globals()['J00398'] or globals()['J00046']) and globals()['I00253']))

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'J00302': bool(globals()['J00302'])
#         }})
        
#     setOutputToRLY()

# def IsLineBans():
#     globals()['J00175'] = bool(globals()['I00060'] and globals()['I00063'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'J00175': bool(globals()['J00175'])
#         }})
        
#     setOutputToRLY()

# def ToLineAhld():
#     globals()['J00304'] = bool((globals()['I00253'] and (globals()['J00400'] or globals()['J00048'])) or ((globals()['J00400'] or globals()['J00048']) and globals()['I00255']))

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'J00304': bool(globals()['J00304'])
#         }})
        
#     setOutputToRLY()

# def IsLineCans():
#     globals()['J00174'] = bool(globals()['I00061'] and globals()['I00062'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'J00174': bool(globals()['J00174'])
#         }})
        
#     setOutputToRLY()

def ToLineBhld():
    globals()['J00303'] = bool((globals()['I00255'] and (globals()['J00399'] or globals()['J00047'])) or ((globals()['J00399'] or globals()['J00047']) and globals()['I00252']))

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00303': bool(globals()['J00303'])
    #     }})
        
    setOutputToRLY()

def J00176func():
    globals()['J00176'] = bool(globals()['I00061'] and globals()['I00063'])
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00176': bool(globals()['J00176'])
    #     }})
    
def J00175func():
    globals()['J00175'] = bool(globals()['I00060'] and globals()['I00063'])
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00175': bool(globals()['J00175'])
    #     }})

def J00174func():
    globals()['J00174'] = bool(globals()['I00061'] and globals()['I00062'])
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00174': bool(globals()['J00174'])
    #     }})

def J00302func():
    globals()['J00302'] = frame2or4and2or(globals()['I00254'], globals()['J00398'], globals()['J00046'], globals()['I00253'])
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00302': bool(globals()['J00302'])
    #     }})

def J00304func():
    globals()['J00304'] = frame2or4and2or(globals()['I00253'], globals()['J00400'], globals()['J00048'], globals()['I00255'])
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00304': bool(globals()['J00304'])
    #     }})

def J00303func():
    globals()['J00303'] = frame2or4and2or(globals()['I00255'], globals()['J00399'], globals()['J00047'], globals()['I00252'])
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00303': bool(globals()['J00303'])
    #     }})

def V0149func():
    # if not globals()['V0149'] == 0:
    DoCloseZ0()
    DoCloseZ1()
    DoOpenZ0()
    DoOpenZ1()
    commonAuto()
    FillerMixerCLogic()
    FillerMixerBLogic()
    autoFeederLineC()


    if not bool(globals()['V0149']):
    # Stop Timer Mixing B
        print("TimerK011 STOP")
        stop_timer("J00245")
        globals()['J00245'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00245': False
        #     }})
        
    # Stop Timer Mixing C
        print("TimerK043 STOP - V0149func")
        stop_timer("J00251")
        globals()['J00251'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00251': False
        #     }})

def commonAuto():

    FillerMixerBLogic()
    FillerMixerCLogic()

    if globals()['V0149'] == 4194304:
        globals()['J00410'] = True 

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00410': True
        #     }})
        print(f"while J00174 ON")
        while not globals()['J00174']:
            globals()['J00399'] = False
            globals()['J00400'] = False
            globals()['J00398'] = True 

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00399': False,
            #         'J00400': False,
            #         'J00398': True
            #     }})
        
        print(f"exit while J00174 : True")
        globals()['J00410'] = False 

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00410': False
        #     }})

        elseCommonAuto()
            
    elif globals()['V0149'] == 8388608:
        globals()['J00389'] = True 

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00389': True
        #     }})

        print("masuk ke Auto Line B - WHILE J00175isLine B False")
        while not globals()['J00175']:
            globals()['J00398'] = False
            globals()['J00400'] = False
            globals()['J00399'] = True 
            # if globals()['I00060'] and globals()['I00063']:
            #     globals()['J00175'] = True
            #     collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00175': True
            #     }})

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00398': False,
            #         'J00400': False,
            #         'J00399': True
            #     }})
        
        print("EXIT WHILE J00175isLine B : True")

        globals()['J00410'] = False 

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00410': False
        #     }})

        elseCommonAuto()

    elif globals()['V0149'] == 16777216:
        while not globals()['J00176']:
            globals()['J00398'] = False
            globals()['J00399'] = False
            globals()['J00400'] = True 

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00398': False,
            #         'J00399': False,
            #         'J00400': True
            #     }})
        
        elseCommonAuto()

    else:
        elseCommonAuto()

def elseCommonAuto():
    globals()['J00398'] = False
    globals()['J00399'] = False
    globals()['J00400'] = False 

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00398': False,
    #         'J00399': False,
    #         'J00400': False
    #     }})
# END LOGIC CODE LINE COMMON

# LOGIC CODE LINE B - MANUAL AUTO
def MotorMaterMixRotorB0Fault():
    MoveCtrl_MotorMaterMixRotorB0()

def MotorMatScrewCnvyrB0Fault():
    MoveCtrl_MotorMatScrewCnvyrB0

def PneumMaterMixDoorB0Fault():
    errBuzzUpdated()
    OpenClose_PneumMaterMixDoorB0()

def PneumTbletHoprDoorB0Fault():
    errBuzzUpdated()
    Open_PneumTbletHoprDoorB0Open()
    # PneumTbletHoprDoorB0Close()

def PneumTbletHoprDoorB1Fault():
    errBuzzUpdated()
    Open_PneumTbletHoprDoorB1Open()
    # PneumTbletHoprDoorB1Close()

def MoveCtrlLogicFunc(target_var1,target_var2,target_var3,in1,in2,in3,in4,in5,in6,in7,in8,in9,in10):
    val1 = globals().get(in1, False)
    val2 = globals().get(in2, False)
    val3 = globals().get(in3, False)
    val4 = globals().get(in4, False)
    val5 = globals().get(in5, False)
    val5 = globals().get(in5, False)
    val6 = globals().get(in6, False)
    val7 = globals().get(in7, False)
    val8 = globals().get(in8, False)
    val9 = globals().get(in9, False)
    val10 = globals().get(in10, False)

    result = MoveCtrlLogic(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10)

    globals()[target_var1] = result.get('out1')
    globals()[target_var2] = result.get('out2')
    globals()[target_var3] = result.get('out3')

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         target_var1: bool(globals()[target_var1]),
    #         target_var2: bool(globals()[target_var2]),
    #         target_var3: bool(globals()[target_var3])
    #     }})
    
    # setOutputToRLY()

def MoveCtrl_MotorMatScrewCnvyrB0():
    MoveCtrlLogicFunc('I00147','I00149','I00148','I00032','J00543','J00518','V0144','J00368','J00016','J00290','J00369','J00017','J00291')

def MoveCtrl_MotorMaterMixRotorB0():
    MoveCtrlLogicFunc('I00144','I00146','I00145','I00028','J00543','J00516','V0149','J00352','J00000','J00288','J00353','J00001',"J00289")

# def TimerK015(val):
#     if val:
#         # jalankan timer jid
#         print("TimerK015 RUN")
#         start_timer("J00291", globals()['V0015'])
#     else:
#         # reset
#         print("TimerK015 STOP")
#         globals()['J00291'] = False
#         stop_timer("J00291")
#         globals()['K015'] = False
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00291': bool(globals()['J00135'])
#             }})

# def TimerK014(val):
#     if val:
#         # jalankan timer jid
#         print("TimerK014 RUN")
#         start_timer("J00290", globals()['V0015'])
#     else:
#         # reset
#         print("TimerK015 STOP")
#         globals()['J00290'] = False
#         stop_timer("J00290")
#         globals()['K014'] = False
#         collection.update_one(
#             {'_id': ObjectId(objID)},
#             {'$set': {
#                 'J00290': bool(globals()['J00290'])
#             }})

# def MotorMaterMixRotorB0DoFwd():
#     globals()['I00144'] = globals()['I00145'] = globals()['I00146'] = False

#     globals()['I00144'] = frame5and2or4and(globals()['I00028'], globals()['J00543'], globals()['J00516'], globals()['V0149'], globals()['J00352'], globals()['J00000'], globals()['I00146'])
#     globals()['I00145'] = not globals()['I00144'] 
    
#     print(f"globals()['I00144'] : {globals()['I00144']}")
#     print(f"globals()['I00028'], globals()['J00543'], globals()['J00516'], globals()['V0149'], globals()['J00352'], globals()['J00000'], globals()['I00146'] \n{globals()['I00028'], globals()['J00543'], globals()['J00516'], globals()['V0149'], globals()['J00352'], globals()['J00000'], globals()['I00146']}")

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00144': bool(globals()['I00144']),
#             'I00145': bool(globals()['I00145'])
#         }})


#     setOutputToRLY()

# def MotorMaterMixRotorB0DoRev():
#     globals()['I00144'] = globals()['I00145'] = globals()['I00146'] = False

#     globals()['I00146'] = frame5and2or4and(globals()['I00028'], globals()['J00543'], globals()['J00516'], globals()['V0149'], globals()['J00353'], globals()['J00001'], globals()['I00144'])
#     globals()['I00145'] = not globals()['I00146'] 

#     # print(f"globals()['I00146'] : {globals()['I00146']}")
#     # print(f"globals()['I00028'], globals()['J00543'], globals()['J00516'], globals()['V0149'], globals()['J00353'], globals()['J00001'], globals()['I00144'] \n{globals()['I00028'], globals()['J00543'], globals()['J00516'], globals()['V0149'], globals()['J00353'], globals()['J00001'], globals()['I00144']}")


#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00146': bool(globals()['I00146']),
#             'I00145': bool(globals()['I00145'])
#         }})

#     setOutputToRLY()

# def MotorMaterMixRotorB0DoStop():
#     globals()['I00145'] = not globals()['I00144'] or not globals()['I00146']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00145': bool(globals()['I00145'])
#         }})
    
#     setOutputToRLY()

# def MotorMatScrewCnvyrB0DoFwd():
#     globals()['I00147'] = globals()['I00148'] = globals()['I00149'] = False

#     # DoFwdMotorMatScrewCnvyrB0
#     globals()['I00147'] = frame5and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00518'], globals()['V0144'], globals()['J00368'], globals()['J00016'], globals()['I00149'])
#     # DoStopMotorMatScrewCnvyrB0
#     globals()['I00148'] = not globals()['I00147']

#     # print(f"globals()['I00147'] : {globals()['I00147']}")
#     # print(f"globals()['I00032'], globals()['J00543'], globals()['J00518'], globals()['V0144'], globals()['J00368'], globals()['J00016'], globals()['I00149'] \n {globals()['I00032'], globals()['J00543'], globals()['J00518'], globals()['V0144'], globals()['J00368'], globals()['J00016'], globals()['I00149']}")

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00148': bool(globals()['I00148']),
#             'I00147': bool(globals()['I00147'])
#         }})
    
#     setOutputToRLY()

# def MotorMatScrewCnvyrB0DoRev():
#     globals()['I00147'] = globals()['I00148'] = globals()['I00149'] = False

#     # DoRevMotorMatScrewCnvyrB0
#     globals()['I00149'] = frame5and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00518'], globals()['V0144'], globals()['J00369'], globals()['J00017'], globals()['I00147'])
#     # DoStopMotorMatScrewCnvyrB0
#     globals()['I00148'] = not globals()['I00149']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00148': bool(globals()['I00148']),
#             'I00149': bool(globals()['I00149'])
#         }})
    
#     setOutputToRLY()

# def MotorMatScrewCnvyrB0DoStop():
#     globals()['I00148'] = not globals()['I00147'] or not globals()['I00149']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00148': bool(globals()['I00148'])
#         }})
    
#     setOutputToRLY()

def StartNStopFunc(target_var1, target_var2, in1, in2, in3, in4, in5, in6):
    val1 = globals().get(in1)
    val2 = globals().get(in2)
    val3 = globals().get(in3)
    val4 = globals().get(in4)
    val5 = globals().get(in5)
    val5 = globals().get(in5)
    val6 = globals().get(in6)

    # Call your StartNStop function with these inputs
    resultStartNStop = StartNStopLogic(val1, val2, val3, val4, val5, val6)

    # Update the output global variable and MongoDB
    globals()[target_var1] = resultStartNStop.get('out1')
    globals()[target_var2] = resultStartNStop.get('out2')
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': 
    #      {target_var1: bool(globals()[target_var1]),
    #       target_var2: bool(globals()[target_var2]
    #     )}}
    # )

def StartNStop_MotorMateriVbratorB0():
    StartNStopFunc('I00130','I00131','I00032','J00543','J00517','V0144','J00356','J00004')
def StartNStop_MotorToRotaryCnvyrB0():
    StartNStopFunc('I00132','I00133','I00032','J00543','J00519','V0144','J00357','J00004')
def StartNStop_MotorFrmRtaryCnvyrB0():
    StartNStopFunc('I00160','I00161','I00032','J00543','J00520','V0144','J00384','J00032')
def StartNStop_MotorUpladderCnvyrB0():
    StartNStopFunc('I00162','I00163','I00032','J00543','J00521','V0144','J00385','J00033')
def StartNStop_MotorToHopperCnvyrB0():
    StartNStopFunc('I00150','I00151','I00032','J00543','J00522','V0144','J00370','J00018')
def StartNStop_MotorTbletHoprDoorB0():
    StartNStopFunc('I00168','I00169','I00032','J00543','J00515','V0145','J00383','J00031')
def StartNStop_MotorToRncenCnvyrB0():
    StartNStopFunc('I00170','I00171','I00032','J00543','J00523','V0145','J00386','J00034')

# def MotorMateriVbratorB0():

#     globals()['I00130'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00517'], globals()['V0144'], globals()['J00356'], globals()['J00004'])
#     globals()['I00131'] = not globals()['I00130']

#     setOutputToRLY()

# def MotorToRotaryCnvyrB0():

#     globals()['I00132'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00519'], globals()['V0144'], globals()['J00357'], globals()['J00005'])
#     globals()['I00133'] = not globals()['I00132']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00132': bool(globals()['I00132']),
#             'I00133': bool(globals()['I00133'])
#         }})

#     setOutputToRLY()

# def MotorFrmRtaryCnvyrB0():

#     globals()['I00160'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00520'], globals()['V0144'], globals()['J00384'], globals()['J00032'])
#     globals()['I00161'] = not globals()['I00160']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00160': bool(globals()['I00160']),
#             'I00161': bool(globals()['I00161'])
#         }})

#     setOutputToRLY()

# def MotorUpladderCnvyrB0():

#     globals()['I00162'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00521'], globals()['V0144'], globals()['J00385'], globals()['J00033'])
#     globals()['I00163'] = not globals()['I00162']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00162': bool(globals()['I00162']),
#             'I00163': bool(globals()['I00163'])
#         }})

#     setOutputToRLY()

# def MotorToHopperCnvyrB0():

#     globals()['I00150'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00522'], globals()['V0144'], globals()['J00370'], globals()['J00018'])
#     globals()['I00151'] = not globals()['I00150']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00150': bool(globals()['I00150']),
#             'I00151': bool(globals()['I00151'])
#         }})

#     setOutputToRLY()

# def MotorTbletHoprDoorB0():

#     globals()['I00168'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00515'], globals()['V0145'], globals()['J00383'], globals()['J00031'])
#     globals()['I00169'] = not globals()['I00168']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00168': bool(globals()['I00168']),
#             'I00169': bool(globals()['I00169'])
#         }})

#     setOutputToRLY()

# def MotorToRncenCnvyrB0():

#     globals()['I00170'] = frame4and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00523'], globals()['V0145'], globals()['J00386'], globals()['J00034'])
#     globals()['I00171'] = not globals()['I00170']

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00170': bool(globals()['I00170']),
#             'I00171': bool(globals()['I00171'])
#         }})

#     setOutputToRLY()

# def Close_PneumToRotaryCnvyrB0():

#     globals()['I00135'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00359'], globals()['J00007'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00135': bool(globals()['I00135'])
#         }})

#     setOutputToRLY()

def TimerK016(val):
    if val:
        # jalankan timer jid
        print("TimerK016 RUN")
        start_timer("J00135", globals()['V0016'])
    else:
        # reset
        print("TimerK016 STOP")
        globals()['J00135'] = False
        stop_timer("J00135")
        globals()['K016'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00135': bool(globals()['J00135'])
        #     }})

# def Close_PneumToRotaryCnvyrB1():

#     globals()['I00137'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00361'], globals()['J00009'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00137': bool(globals()['I00137'])
#         }})

#    setOutputToRLY()

def TimerK017(val):
    if val:
        # jalankan timer jid
        print("TimerK017 RUN")
        start_timer("J00136", globals()['V0017'])
    else:
        # reset
        print("TimerK017 STOP")
        globals()['J00136'] = False
        stop_timer("J00136")
        globals()['K017'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00136': bool(globals()['J00136'])
        #     }})

# def Close_PneumToRotaryCnvyrB2():

#     globals()['I00139'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00363'], globals()['J00011'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00139': bool(globals()['I00139'])
#         }})

#     setOutputToRLY()

def TimerK018(val):
    if val:
        # jalankan timer jid
        print("TimerK018 RUN")
        start_timer("J00137", globals()['V0018'])
    else:
        # reset
        print("TimerK018 STOP")
        globals()['J00137'] = False
        stop_timer("J00137")
        globals()['K018'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00137': bool(globals()['J00137'])
        #     }})

# def Close_PneumToRotaryCnvyrB3():

#     globals()['I00141'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00365'], globals()['J00013'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00141': bool(globals()['I00141'])
#         }})

#     setOutputToRLY()

def TimerK019(val):
    if val:
        # jalankan timer jid
        print("TimerK019 RUN")
        start_timer("J00138", globals()['V0019'])
    else:
        # reset
        print("TimerK019 STOP")
        globals()['J00138'] = False
        stop_timer("J00138")
        globals()['K019'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00138': bool(globals()['J00138'])
        #     }})

# def Close_PneumToRotaryCnvyrB4():

#     globals()['I00143'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00367'], globals()['J00015'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00143': bool(globals()['I00143'])
#         }})

#     print ('I00143:', globals()['I00143'])
#     print (globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00367'], globals()['J00015'])

#     setOutputToRLY()

def TimerK020(val):
    if val:
        # jalankan timer jid
        print("TimerK020 RUN")
        start_timer("J00139", globals()['V0020'])
    else:
        # reset
        print("TimerK020 STOP")
        globals()['J00139'] = False
        stop_timer("J00139")
        globals()['K020'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00139': bool(globals()['J00139'])
        #     }})

def CloseLogicFunc(target_var, in1, in2, in3, in4, in5):
    # Retrieve input values safely from globals, defaulting to False if missing
    val1 = globals().get(in1)
    val2 = globals().get(in2)
    val3 = globals().get(in3)
    val4 = globals().get(in4)
    val5 = globals().get(in5)

    # Call your CloseLogic function with these inputs
    ResultCloseLogic = CloseLogic(val1, val2, val3, val4, val5)
    globals()[target_var]  = ResultCloseLogic.get('out1')

    # Update the output global variable and MongoDB
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {target_var: bool(globals()[target_var])}}
    # )

def Close_PneumToRotaryCnvyrB0():
     CloseLogicFunc('I00135', 'I00032', 'J00543', 'V0144', 'J00359', 'J00007')
def Close_PneumToRotaryCnvyrB1():
     CloseLogicFunc('I00137', 'I00032', 'J00543', 'V0144', 'J00361', 'J00009')
def Close_PneumToRotaryCnvyrB2():
     CloseLogicFunc('I00139', 'I00032', 'J00543', 'V0144', 'J00363', 'J00011')
def Close_PneumToRotaryCnvyrB3():
     CloseLogicFunc('I00141', 'I00032', 'J00543', 'V0144', 'J00365', 'J00013')
def Close_PneumToRotaryCnvyrB4():
     CloseLogicFunc('I00143', 'I00032', 'J00543', 'V0144', 'J00367', 'J00015')
def Close_PneumToRncenCnvyrB0():
     CloseLogicFunc('I00173','I00032','J00543','V0145','J00388','J00036')
def Close_PneumToHopperCnvyrB0():
     CloseLogicFunc('I00153', 'I00032', 'J00543', 'V0144', 'J00372', 'J00020')
def Close_PneumToHopperCnvyrB1():
     CloseLogicFunc('I00155', 'I00032', 'J00543', 'V0144', 'J00374', 'J00022')
def Close_PneumToHopperCnvyrB2():
     CloseLogicFunc('I00157', 'I00032', 'J00543', 'V0144', 'J00376', 'J00024')
def Close_PneumToHopperCnvyrB3():
     CloseLogicFunc('I00159', 'I00032', 'J00543', 'V0144', 'J00378', 'J00026')

# def PneumToHopperCnvyrB0():

#     globals()['I00153'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00372'], globals()['J00020'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00153': bool(globals()['I00153'])
#         }})

#     setOutputToRLY()

def TimerK021(val):
    if val:
        # jalankan timer jid
        print("TimerK021 RUN")
        start_timer("J00140", globals()['V0021'])
    else:
        # reset
        print("TimerK021 STOP")
        globals()['J00140'] = False
        stop_timer("J00140")
        globals()['K021'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00140': bool(globals()['J00140'])
        #     }})

# def PneumToHopperCnvyrB1():

#     globals()['I00155'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00374'], globals()['J00022'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00155': bool(globals()['I00155'])
#         }})

#     setOutputToRLY()

def TimerK022(val):
    if val:
        # jalankan timer jid
        print("TimerK022 RUN")
        start_timer("J00141", globals()['V0022'])
    else:
        # reset
        print("TimerK022 STOP")
        globals()['J00141'] = False
        stop_timer("J00141")
        globals()['K022'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00141': bool(globals()['J00141'])
        #     }})

# def PneumToHopperCnvyrB2():

#     globals()['I00157'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00376'], globals()['J00024'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00157': bool(globals()['I00157'])
#         }})

#     setOutputToRLY()

def TimerK023(val):
    if val:
        # jalankan timer jid
        print("TimerK023 RUN")
        start_timer("J00142", globals()['V0023'])
    else:
        # reset
        print("TimerK023 STOP")
        globals()['J00142'] = False
        stop_timer("J00142")
        globals()['K023'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00142': bool(globals()['J00142'])
        #     }})

# def PneumToHopperCnvyrB3():

#     globals()['I00159'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0144'], globals()['J00378'], globals()['J00026'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00159': bool(globals()['I00159'])
#         }})

#     setOutputToRLY()

def TimerK024(val):
    if val:
        # jalankan timer jid
        print("TimerK024 RUN")
        start_timer("J00143", globals()['V0024'])
    else:
        # reset
        print("TimerK024 STOP")
        globals()['J00143'] = False
        stop_timer("J00143")
        globals()['K024'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00143': bool(globals()['J00143'])
        #     }})

def OpenCloseLogicFunc(target_var1,target_var2, in1, in2, in3, in4, in5, in6,in7,in8,in9,in10,in11,in12 ):
    val1 = globals().get(in1)
    val2 = globals().get(in2)
    val3 = globals().get(in3)
    val4 = globals().get(in4)
    val5 = globals().get(in5)
    val5 = globals().get(in5)
    val6 = globals().get(in6)
    val7 = globals().get(in7)
    val8 = globals().get(in8)
    val9 = globals().get(in9)
    val10 = globals().get(in10)
    val11 = globals().get(in11)
    val12= globals().get(in12)

    resultOpenCloseLogic = OpenCloseLogic(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12)

    # Update the output global variable and MongoDB
    globals()[target_var1] = resultOpenCloseLogic.get('out1')
    globals()[target_var1] = resultOpenCloseLogic.get('out2')  
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': 
    #      {target_var1: bool(globals()[target_var1]),
    #       target_var2: bool(globals()[target_var2])}}
    # )

def OpenClose_PneumMaterMixDoorB0():
    OpenCloseLogicFunc('I00128','I00129','I00032','J00543','J00512','V0144','J00354','J00002','I00129','I00001','J00355','J00003','I000128','I00002')

# def PneumMaterMixDoorB0Open():

#     globals()['I00128'] = frame6and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00512'], globals()['V0144'], globals()['J00354'], globals()['J00002'], globals()['I00129'], globals()['I00001'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00128': bool(globals()['I00128'])
#         }})
        
#     # print(f"buka pintu matermix B: {globals()['I00128']}")   
#     # print(f"globals()['I00032'], globals()['J00543'], globals()['J00512'], globals()['V0144'], globals()['J00354'], globals()['J00002'], globals()['I00129'], globals()['I00001']\n{globals()['I00032'], globals()['J00543'], globals()['J00512'], globals()['V0144'], globals()['J00354'], globals()['J00002'], globals()['I00129'], globals()['I00001']}")
#     setOutputToRLY()

# def PneumMaterMixDoorB0Close():     

#     globals()['I00129'] = frame6and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00512'], globals()['V0144'], globals()['J00355'], globals()['J00003'], globals()['I00128'], globals()['I00002'])


#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00129': bool(globals()['I00129'])
#         }})
    
#     setOutputToRLY()

def TimerK000():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00001'], globals()['I00128'], globals()['I00002'], globals()['I00129']):
        
        print("TimerK000 RUN")
        start_timer("K000V0000IsJam", globals()['V0000'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00001'], globals()['I00128'], globals()['I00002'], globals()['I00129']):
        print("jidTimerK000 STOOOP")
        stop_timer("K000V0000IsJam")

def OpenLogicFunc(target_var1, in1, in2, in3, in4, in5, in6):
    val1 = globals().get(in1, False)
    val2 = globals().get(in2, False)
    val3 = globals().get(in3, False)
    val4 = globals().get(in4, False)
    val5 = globals().get(in5, False)
    val5 = globals().get(in5, False)
    val6 = globals().get(in6, False)

    # Call your OpenLgic function with these inputs
    resultOpenLogic = OpenLogic(val1, val2, val3, val4, val5, val6)

    # Update the output global variable and MongoDB
    globals()[target_var1] = resultOpenLogic.get('out1') 
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': 
    #      {target_var1: bool(globals()[target_var1])}}
    # )

def Open_PneumTbletHoprDoorB0Open():
    OpenLogicFunc('I00164','I00032','J00543','J00513','V0145','J00379','J00027')

def Open_PneumTbletHoprDoorB1Open():
    OpenLogicFunc('I00166','I00032','J00543','J00514','V0145','J00381','J00029')

# def PneumTbletHoprDoorB0Open():
#     print("trigger Hopper 2 open On")

#     globals()['I00164'] = frame6and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00513'], globals()['V0145'], globals()['J00379'], globals()['J00027'], globals()['I00165'], globals()['I00020'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00164': bool(globals()['I00164'])
#         }})
        
#     setOutputToRLY()
#     print("silo2",globals()['I00032'], globals()['J00543'], globals()['J00513'], globals()['V0145'], globals()['J00379'], globals()['J00027'], globals()['I00165'], globals()['I00020'])

# def PneumTbletHoprDoorB0Close():

#     print("trigger Hopper 2  close On")     

#     globals()['I00165'] = frame6and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00513'], globals()['V0145'], globals()['J00380'], globals()['J00028'], globals()['I00164'], globals()['I00021'])


#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00165': bool(globals()['I00165'])
#         }})
    
#     setOutputToRLY()

def TimerK001():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00020'], globals()['I00164'], globals()['I00021'], globals()['I00165']):
        
        print("TimerK001 RUN")
        start_timer("K001V0001IsJam", globals()['V0001'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00020'], globals()['I00164'], globals()['I00021'], globals()['I00165']):
        print("jidTimerK001 STOOOP")
        stop_timer("K001V0001IsJam")

# def PneumTbletHoprDoorB1Open():

#     print("trigger Hopper 1 open On")

#     globals()['I00166'] = frame6and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00514'], globals()['V0145'], globals()['J00381'], globals()['J00029'], globals()['I00167'], globals()['I00022'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00166': bool(globals()['I00166'])
#         }})
        
#     setOutputToRLY()
#     print("silo1",globals()['I00032'], globals()['J00543'], globals()['J00514'], globals()['V0145'], globals()['J00381'], globals()['J00029'], globals()['I00167'], globals()['I00022'])

# def PneumTbletHoprDoorB1Close():     

#     print("trigger Hopper 2 close On")
    
#     globals()['I00167'] = frame6and2or4and(globals()['I00032'], globals()['J00543'], globals()['J00514'], globals()['V0145'], globals()['J00382'], globals()['J00030'], globals()['I00166'], globals()['I00023'])


#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00167': bool(globals()['I00167'])
#         }})
    
#     setOutputToRLY()

def TimerK002():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00022'], globals()['I00166'], globals()['I00023'], globals()['I00167']):
        
        print("TimerK002 RUN")
        start_timer("K002V0002IsJam", globals()['V0002'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00022'], globals()['I00166'], globals()['I00023'], globals()['I00167']):
        print("jidTimerK002 STOOOP")
        stop_timer("K002V0002IsJam")

# def PneumToRncenCnvyrB0():

#     globals()['I00173'] = frame3and2or4and(globals()['I00032'], globals()['J00543'], globals()['V0145'], globals()['J00388'], globals()['J00036'])

#     collection.update_one(
#         {'_id': ObjectId(objID)},
#         {'$set': {
#             'I00173': bool(globals()['I00173'])
#         }})

#     setOutputToRLY()

def TimerK025(val):
    if val:
        # jalankan timer jid
        print("TimerK025 RUN")
        start_timer("J00144", globals()['V0025'])
    else:
        # reset
        print("TimerK025 STOP")
        globals()['J00144'] = False
        stop_timer("J00144")
        globals()['K025'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00144': bool(globals()['J00144'])
        #     }})

def TimerK026(val):
    if val:
        # jalankan timer jid
        print("TimerK026 RUN")
        start_timer("J00145", globals()['V0026'])
    else:
        # reset
        print("TimerK026 STOP")
        globals()['J00145'] = False
        stop_timer("J00145")
        globals()['K026'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00145': bool(globals()['J00145'])
        #     }})

def autoFeederLineB():
    # Map each V0144 value to the corresponding J0037x values and the K0XX flag to check
    feeder_map = {
        32768: ((True, False, False, False), 'K021', "feeder B putih"),
        16384: ((True, True, False, False), 'K022', "feeder B Warna1"),
        8192:  ((True, True, True, False), 'K023', "feeder B Warna2"),
        4096:  ((True, True, True, True), 'K024', "feeder B Warna3"),
    }

    V0144 = globals().get('V0144')
    mapping = feeder_map.get(V0144)

    if mapping:
        j_values, k_flag, message = mapping
        print('V0144 : ', V0144, message)
        if not globals().get(k_flag, False):
            globals()['J00372'], globals()['J00374'], globals()['J00376'], globals()['J00378'] = j_values
            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00372': j_values[0],
            #         'J00374': j_values[1],
            #         'J00376': j_values[2],
            #         'J00378': j_values[3],
            #     }}
            # )
            AutoRotaryUnitHopLineB()
        else:
            AutoFeederLineBState(False)
    else:
        AutoFeederLineBState(False)


def AutoRotaryUnitHopLineB():
    # Map each V0153 state to the corresponding J003xx values
    state_map= {
        "strtB0": (True, False, False, False, False),
        "strtB1": (True, True, False, False, False),
        "strtB2": (True, True, True, False, False),
        "strtB3": (True, True, True, True, False),
        "strtB4": (True, True, True, True, True),
        }

    values = state_map.get( V0153 )
    print('V0153 : ',V0153,values)
    if values:
        updates = {
            'J00359': values[0],
            'J00361': values[1],
            'J00363': values[2],
            'J00365': values[3],
            'J00367': values[4],
        }
        globals()['J00359'], globals()['J00361'], globals()['J00363'], globals()['J00365'], globals()['J00367'] = values[0], values[1], values[2], values[3], values[4]
        # collection.update_one(
        # {'_id': ObjectId(objID)},
        # {'$set': {
        #     'J00359': values[0],
        #     'J00361': values[1],
        #     'J00363': values[2],
        #     'J00365': values[3],
        #     'J00367': values[4],}
        # })
        AutoFeederLineBState(True)
    else:
        AutoFeederLineBState(False)

def AutoFeederLineBState(active: bool):
    # Define the keys and their values for active True and False
    states_true = {
        'J00370': True,
        'J00385': True,
        'J00384': True,
        'J00357': True,
        'J00369': False,
        'J00368': True,
        'J00356': True,
    }
    states_false = {
        'J00356': False,
        'J00368': False,
        'J00369': False,
        'J00357': False,
        'J00367': False,
        'J00365': False,
        'J00363': False,
        'J00361': False,
        'J00359': False,
        'J00384': False,
        'J00385': False,
        'J00370': False,
        'J00378': False,
        'J00376': False,
        'J00374': False,
        'J00372': False,
    }

    if active:
        print ("State Auto Feeder Line B Active")
        # Set globals for True states
        for key, value in states_true.items():
            globals()[key] = value
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': states_true}
        # )
    else:
        print ("State Auto Feeder Line B Inactive")
        # Set globals for False states
        for key, value in states_false.items():
            globals()[key] = value
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': states_false}
        # )

def TimerK011(val):
    if val and bool(globals()['V0149']):
        # jalankan timer jid
        print("TimerK011 RUN")
        start_timer("J00245", globals()['V0011'])
    else:
        # reset
        print("TimerK011 STOP - TimerK011")
        stop_timer("J00245")
        globals()['J00245'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00245': False
        #     }})

def ResetTimerK011():
    if globals()['J00243']:
        print("TimerK011 STOP-ResetTimerK011")
        stop_timer("J00245")
        globals()['J00245'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00245': False
        #     }})

def autoHopperLineB():
    print(f"innn - globals()['V0152'] {globals()['V0152']}")
    if bool(globals()['V0145']):
        # HopperC Putih
        # if not globals()['K025']:
        if globals()['V0152'] == "strtB0":
            print("aaaa")
            globals()['J00388'] = False
            globals()['J00386'] = True
            globals()['J00383'] = True
            # collection.update_one(
            # {'_id': ObjectId(objID)},
            # {'$set': {
            #     'J00388': False,
            #     'J00386': True,
            #     'J00383': True
            #     }})
            
            cekHopperWarna()

        # elif not globals()['K026']:
        elif globals()['V0152'] == "strtB1":
            print("bbb")
            globals()['J00388'] = True
            globals()['J00386'] = True
            globals()['J00383'] = True
            # collection.update_one(
            # {'_id': ObjectId(objID)},
            # {'$set': {
            #     'J00388': True,
            #     'J00386': True,
            #     'J00383': True
            #     }})

            cekHopperWarna()

        else:
            hopperElseFalseLineB()
    else:
        hopperElseFalseLineB()

def cekHopperWarna():
    if globals()['V0145'] == 1024:
        print("masuk while buka pintu tblethopdoorB1")
        # while not globals()['I00022']:
        globals()['J00382'] = False
        globals()['J00381'] = True
        # collection.update_one(
        # {'_id': ObjectId(objID)},
        # {'$set': {
        #     'J00382': False,
        #     'J00381': True,
        #     'J00379': False
        #     }})
        print("exit while buka pintu tblethopdoorB1")
    else:
        print("masuk while buka pintu tblethopdoorB0")
        # while not globals()['I00020']:
        globals()['J00380'] = False
        globals()['J00379'] = True
        globals()['J00381'] = False
        # collection.update_one(
        # {'_id': ObjectId(objID)},
        # {'$set': {
        #    'J00380': False,
        #    'J00379': True,
        #    'J00381': False
        #      }})
        print("exit while buka pintu tblethopdoorB0")

def hopperElseFalseLineB():
    globals()['J00379'] = False
    globals()['J00380'] = False
    globals()['J00381'] = False
    globals()['J00382'] = False
    globals()['J00383'] = False
    globals()['J00386'] = False
    globals()['J00388'] = False

    # collection.update_one(
    # {'_id': ObjectId(objID)},
    # {'$set': {
    #     'J00379': False,
    #     'J00380': False,
    #     'J00381': False,
    #     'J00382': False,
    #     'J00383': False,
    #     'J00386': False,
    #     'J00388': False
    #     }})

    print("All Hooper Line B False")

def v0153staB3():
    in0 = bool(globals()['V0153'] == "stopB0" and globals()['J00136'] and globals()['J00137'] and not globals()['J00138'])
    in1 = bool(globals()['V0153'] == "stopB1" and globals()['J00137'] and not globals()['J00138'])
    in2 = bool(globals()['V0153'] == "stopB2" and not globals()['J00138'])
    in3 = bool(globals()['V0153'] == "stopB4" and globals()['J00135'] and globals()['J00136'] and globals()['J00137'] and not globals()['J00138'])

    if in0 or in1 or in2 or in3:
        globals()['V0153'] = "strtB3"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})

def v0153stopB0():
    if globals()['J00135'] and globals()['V0153'] == "strtB0":
        globals()['V0153'] = "stopB0"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})
        
def v0153staB4():
    in0 = bool(globals()['V0153'] == "stopB1" and globals()['J00137'] and globals()['J00138'] and not globals()['J00139'])
    in1 = bool(globals()['V0153'] == "stopB2" and globals()['J00138'] and not globals()['J00139'])
    in2 = bool(globals()['V0153'] == "stopB3" and not globals()['J00139'])
    in3 = bool(globals()['V0153'] == "stopB0" and globals()['J00136'] and globals()['J00137'] and globals()['J00138'] and not globals()['J00139'])

    if in0 or in1 or in2 or in3:
        globals()['V0153'] = "strtB4"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})

def v0153stopB1():
    if globals()['J00136'] and globals()['V0153'] == "strtB1":
        globals()['V0153'] = "stopB1"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})

def v0153staB0():
    in0 = bool(globals()['V0153'] == "stopB4" and not globals()['J00135'])
    in1 = bool(globals()['V0153'] == "stopB2" and globals()['J00138'] and globals()['J00139'] and not globals()['J00135'])
    in2 = bool(globals()['V0153'] == "stopB3" and globals()['J00139'] and not globals()['J00135'])
    in3 = bool(globals()['V0153'] == "stopB1" and globals()['J00137'] and globals()['J00138'] and globals()['J00139'] and not globals()['J00135'])

    if in0 or in1 or in2 or in3:
        globals()['V0153'] = "strtB0"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})

def v0153stopB2():
    if globals()['J00137'] and globals()['V0153'] == "strtB2":
        globals()['V0153'] = "stopB2"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})

def v0153staB1():
    in0 = bool(globals()['V0153'] == "stopB4" and globals()['J00135'] and not globals()['J00136'])
    in1 = bool(globals()['V0153'] == "stopB0" and not globals()['J00136'])
    in2 = bool(globals()['V0153'] == "stopB3" and globals()['J00139'] and globals()['J00135'] and not globals()['J00136'])
    in3 = bool(globals()['V0153'] == "stopB2" and globals()['J00138'] and globals()['J00139'] and globals()['J00135'] and not globals()['J00136'])

    if in0 or in1 or in2 or in3:
        globals()['V0153'] = "strtB1"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})
        
def v0153stopB3():
    if globals()['J00138'] and globals()['V0153'] == "strtB3":
        globals()['V0153'] = "stopB3"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})
        
def v0153staB2():
    in0 = bool(globals()['V0153'] == "stopB4" and globals()['J00135'] and globals()['J00136'] and not globals()['J00137'])
    in1 = bool(globals()['V0153'] == "stopB0" and globals()['J00136'] and not globals()['J00137'])
    in2 = bool(globals()['V0153'] == "stopB1" and not globals()['J00137'])
    in3 = bool(globals()['V0153'] == "stopB3" and globals()['J00139'] and globals()['J00135'] and globals()['J00136'] and not globals()['J00137'])

    print(f"{in0} - {in1} - {in2} - {in3}")

    if in0 or in1 or in2 or in3:
        globals()['V0153'] = "strtB2"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})
        
def v0153stopB4():
    if globals()['J00139'] and globals()['V0153'] == "strtB4":
        globals()['V0153'] = "stopB4"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0153': globals()['V0153']
                }})

def v0152staB0():
    if globals()['V0152'] == "stopB1" and not globals()['J00144']:
        globals()['V0152'] = "strtB0"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0152': globals()['V0152']
                }})
    
def v0152stopB0():
    if globals()['V0152'] == "strtB0" and globals()['J00144']:
        globals()['V0152'] = "stopB0"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0152': globals()['V0152']
                }})    

def v0152staB1():
    if globals()['V0152'] == "stopB0" and not globals()['J00145']:
        globals()['V0152'] = "strtB1"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0152': globals()['V0152']
                }})

def v0152stopB1():
    if globals()['V0152'] == "strtB1" and globals()['J00145']:
        globals()['V0152'] = "stopB1"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0152': globals()['V0152']
                }})

def V0153change():
    v0153staB3()
    v0153stopB0()
    v0153staB4()
    v0153stopB1()
    v0153staB2()
    v0153staB0()
    v0153stopB2()
    v0153staB1()
    v0153stopB3()
    v0153stopB4()
    autoFeederLineB()

def J00135change():
    v0153staB0()
    v0153staB1()
    v0153staB2()
    v0153staB3()
    v0153stopB0()

def J00136change():
    v0153staB1()
    v0153staB2()
    v0153staB3()
    v0153staB4()
    v0153stopB1()

def J00137change():
    v0153staB3()
    v0153staB2()
    v0153staB4()
    v0153staB0()
    v0153stopB2()

def J00138change():
    v0153staB3()
    v0153staB4()
    v0153staB0()
    v0153staB1()
    v0153stopB3()

def J00139change():
    v0153staB4()
    v0153staB0()
    v0153staB1()
    v0153staB2()
    v0153stopB4()

def V0152change():
    v0152staB0()
    v0152stopB0()
    v0152staB1()
    v0152stopB1()
    autoHopperLineB()

def J00144change():
    v0152staB0()
    v0152stopB0()

def J00145change():
    v0152staB1()
    v0152stopB1()

def FillerMixerBLogic():

    runFillMixerB = frameFillMixer(globals()['V0149'], globals()['J00389'], globals()['J00037'], globals()['J00244'], globals()['J00245'])

    print(f"runFillMixerB : {runFillMixerB}")
    print(f"globals()['V0149'], globals()['J00389'], globals()['J00037'], globals()['J00244'], globals()['J00245']\n{globals()['V0149'], globals()['J00389'], globals()['J00037'], globals()['J00244'], globals()['J00245']}")


    if runFillMixerB:
        FillMixerBStart()

def FillMixerBStart():
    globals()['J00243'] = True

    print("------->FillMixerBStart")

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00243': globals()['J00243']
    #     }})
    
    print(f"masuk While tutup pintu :  globals()['I00002'] { globals()['I00002']}")
    while not bool(globals()['I00002']):
        globals()['J00354'] = False
        globals()['J00355'] = True
        # collection.update_one(
        # {'_id': ObjectId(objID)},
        # {'$set': {
        #     'J00354': False,
        #     'J00355': True
        #     }})
    print(f"exit While tutup pintu")
    globals()['J00354'] = False
    globals()['J00355'] = False
    globals()['J00353'] = False
    globals()['J00352'] = True

    globals()['J00243'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00354': False,
    #         'J00355': False,
    #         'J00353': False,
    #         'J00352': True,
    #         'J00243': False
    #         }})

def DumpMixerBLogic():
    runDumpMixerC = frameDumpMixer(globals()['J00038'], globals()['J00245'], globals()['J00243'])

    print(f"globals()['J00038'], globals()['J00245'], globals()['J00243']\n{globals()['J00038'], globals()['J00245'], globals()['J00243']}")

    if runDumpMixerC:
        DumpMixerBStart()

def DumpMixerBStart():
    globals()['J00244'] = True

    globals()['J00352'] = False
    globals()['J00353'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00244': globals()['J00244'],
    #         'J00352': globals()['J00352'],
    #         'J00353': globals()['J00353']
    #     }})
    
    print(f"masuk While BUKA pintu :  globals()['I00001'] { globals()['I00001']}")
    while not bool(globals()['I00001']):
        globals()['J00355'] = False
        globals()['J00354'] = True

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00355': globals()['J00355'],
        #         'J00354': globals()['J00354']
        #     }})
    
    print(f">> EXIT While BUKA pintu :  globals()['I00001'] { globals()['I00001']}")

    globals()['J00355'] = False
    globals()['J00354'] = False
    globals()['J00244'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00355': globals()['J00355'],
    #         'J00354': globals()['J00354'],
    #         'J00244': globals()['J00244']
    #     }})

# END LOGIC CODE LINE B - MANUAL AUTO


# LOGIC CODE LINE C - MANUAL AUTO
def MotorMaterMixRotorC0Fault():
    MotorMaterMixRotorC0DoFwd()
    MotorMaterMixRotorC0DoRev()

def MotorMatScrewCnvyrC0Fault():
    MotorMatScrewCnvyrC0DoFwd()
    MotorMatScrewCnvyrC0DoRev()

def PneumMaterMixDoorC0Fault():
    errBuzzUpdated()
    PneumMaterMixDoorC0Open()
    PneumMaterMixDoorC0Close()

def PneumTbletHoprDoorC0Fault():
    errBuzzUpdated()
    PneumTbletHoprDoorC0Open()
    PneumTbletHoprDoorC0Close()

def PneumTbletHoprDoorC1Fault():
    errBuzzUpdated()
    PneumTbletHoprDoorC1Open()
    PneumTbletHoprDoorC1Close()

def PneumTbletHoprDoorC2Fault():
    errBuzzUpdated()
    PneumTbletHoprDoorC2Open()
    PneumTbletHoprDoorC2Close()

def PneumTbletHoprDoorC3Fault():
    errBuzzUpdated()
    PneumTbletHoprDoorC3Open()
    PneumTbletHoprDoorC3Close()

def PneumTbletHoprDoorC4Fault():
    errBuzzUpdated()
    PneumTbletHoprDoorC4Open()
    PneumTbletHoprDoorC4Close()

def MotorMaterMixRotorC0DoFwd():
    globals()['I00208'] = globals()['I00209'] = globals()['I00210'] = False

    globals()['I00208'] = frame5and2or4and(globals()['I00028'], globals()['J00543'], globals()['J00534'], globals()['V0149'], globals()['J00411'], globals()['J00059'], globals()['I00210'])
    globals()['I00209'] = not globals()['I00208'] 


    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00208': bool(globals()['I00208']),
    #         'I00209': bool(globals()['I00209']),
    #         'I00210': bool(globals()['I00210'])
    #     }})

    print(f"MotorMaterMixRotorB0DoFwd - globals()['I00208'] : {globals()['I00208']}")
    print(f"globals()['I00028'], globals()['J00543'], globals()['J00534'], globals()['V0149'], globals()['J00411'], globals()['J00059'], globals()['I00210'] \n {globals()['I00028'], globals()['J00543'], globals()['J00534'], globals()['V0149'], globals()['J00411'], globals()['J00059'], globals()['I00210']}")

    setOutputToRLY()

def MotorMaterMixRotorC0DoRev():
    globals()['I00208'] = globals()['I00209'] = globals()['I00210'] = False

    globals()['I00210'] = frame5and2or4and(globals()['I00028'], globals()['J00543'], globals()['J00534'], globals()['V0149'], globals()['J00412'], globals()['J00060'], globals()['I00208'])
    globals()['I00209'] = not globals()['I00210'] 

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00208': bool(globals()['I00208']),
    #         'I00209': bool(globals()['I00209']),
    #         'I00210': bool(globals()['I00210'])
    #     }})

    setOutputToRLY()

def MotorMaterMixRotorC0DoStop():
    globals()['I00209'] = not (globals()['I00210'] or globals()['I00208'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00209': bool(globals()['I00209'])
    #     }})

    setOutputToRLY()

def PneumMaterMixDoorC0Open():

    globals()['I00192'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00528'], globals()['V0146'], globals()['J00413'], globals()['J00061'], globals()['I00193'], globals()['I00065'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00192': bool(globals()['I00192']),
    #         # 'I00193': bool(globals()['I00193'])
    #     }})
        
    setOutputToRLY()

def PneumMaterMixDoorC0Close():     

    globals()['I00193'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00528'], globals()['V0146'], globals()['J00414'], globals()['J00062'], globals()['I00192'], globals()['I00066'])

    # print(f"globals()['I00193'] PneumMaterMixDoorC0Close: {globals()['I00193']}")
    # print(f"globals()['I00096'], globals()['J00543'], globals()['J00528'], globals()['V0146'], globals()['J00414'], globals()['J00062'], globals()['I00192'], globals()['I00066']\n{globals()['I00096'], globals()['J00543'], globals()['J00528'], globals()['V0146'], globals()['J00414'], globals()['J00062'], globals()['I00192'], globals()['I00066']}")


    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         # 'I00192': bool(globals()['I00192']),
    #         'I00193': bool(globals()['I00193'])
    #     }})
    
    setOutputToRLY()

def TimerK032():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00065'], globals()['I00192'], globals()['I00066'], globals()['I00193']):
        
        print("TimerK032 RUN")
        start_timer("K032V0032IsJam", globals()['V0032'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00065'], globals()['I00192'], globals()['I00066'], globals()['I00193']):
        print("jidTimerK032 STOOOP")
        stop_timer("K032V0032IsJam")

def MotorMateriVbratorC0():

    globals()['I00194'] = frame4and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00535'], globals()['V0146'], globals()['J00432'], globals()['J00080'])
    globals()['I00195'] = not globals()['I00194']

    setOutputToRLY()

def MotorMatScrewCnvyrC0DoFwd():

    globals()['I00211'] = globals()['I00212'] = globals()['I00213'] = False

    # DoFwdMotorMatScrewCnvyrC0
    globals()['I00211'] = frame5and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00536'], globals()['V0146'], globals()['J00433'], globals()['J00081'], globals()['I00213'])
    # DoStopMotorMatScrewCnvyrC0

    globals()['I00212'] = not globals()['I00211']

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00212': bool(globals()['I00212']),
    #         'I00211': bool(globals()['I00211'])
    #     }})
    
    setOutputToRLY()

def MotorMatScrewCnvyrC0DoRev():

    globals()['I00211'] = globals()['I00212'] = globals()['I00213'] = False

    # DoRevMotorMatScrewCnvyrC0
    globals()['I00213'] = frame5and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00536'], globals()['V0146'], globals()['J00434'], globals()['J00082'], globals()['I00211'])
    # DoStopMotorMatScrewCnvyrC0
    globals()['I00212'] = not globals()['I00213']
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00212': bool(globals()['I00212']),
    #         'I00213': bool(globals()['I00213'])
    #     }})
    
    setOutputToRLY()

def MotorMatScrewCnvyrC0DoStop():

    globals()['I00212'] = not (globals()['I00211'] or globals()['I00213'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00212': bool(globals()['I00212'])
    #     }})

    
    setOutputToRLY()

def MotorToRotaryCnvyrC0():

    globals()['I00228'] = frame4and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00537'], globals()['V0146'], globals()['J00415'], globals()['J00063'])
    globals()['I00229'] = not globals()['I00228']

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00228': bool(globals()['I00228']),
    #         'I00229': bool(globals()['I00229'])
    #     }})

    setOutputToRLY()

def PneumToRotaryCnvyrC0():

    globals()['I00231'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00417'], globals()['J00065'])
    # print(f"globals()['I00231'] PneumToRotaryCnvyrC0: {globals()['I00231']}")
    # print(f"globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00417'], globals()['J00065']\n{globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00417'], globals()['J00065']}")

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00231': bool(globals()['I00231'])
    #     }})

    setOutputToRLY()

def TimerK048(val):
    if val:
        # jalankan timer jid
        print("TimerK048 RUN")
        start_timer("J00208", globals()['V0048'])
    else:
        # reset
        print("TimerK048 STOP")
        globals()['J00208'] = False
        stop_timer("J00208")
        globals()['K048'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00208': bool(globals()['J00208'])
        #     }})

def PneumToRotaryCnvyrC1():

    globals()['I00233'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00419'], globals()['J00067'])
    print(f"globals()['I00233'] : {globals()['I00233']}")
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00233': bool(globals()['I00233'])
    #     }})

    setOutputToRLY()

def TimerK049(val):
    if val:
        # jalankan timer jid
        print("TimerK049 RUN")
        start_timer("J00209", globals()['V0049'])
    else:
        # reset
        print("TimerK049 STOP")
        globals()['J00209'] = False
        stop_timer("J00209")
        globals()['K049'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00209': bool(globals()['J00209'])
        #     }})

def PneumToRotaryCnvyrC2():

    globals()['I00235'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00421'], globals()['J00069'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00235': bool(globals()['I00235'])
    #     }})

    setOutputToRLY()

def TimerK050(val):
    if val:
        # jalankan timer jid
        print("TimerK050 RUN")
        start_timer("J00210", globals()['V0050'])
    else:
        # reset
        print("TimerK050 STOP")
        globals()['J00210'] = False
        stop_timer("J00210")
        globals()['K050'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00210': bool(globals()['J00210'])
        #     }})

def MotorFrmRtaryCnvyrC0():

    globals()['I00224'] = frame4and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00538'], globals()['V0146'], globals()['J00435'], globals()['J00083'])
    globals()['I00225'] = not globals()['I00224']

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00224': bool(globals()['I00224']),
    #         'I00225': bool(globals()['I00225'])
    #     }})

    setOutputToRLY()

def MotorUpladderCnvyrC0():

    globals()['I00226'] = frame4and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00539'], globals()['V0146'], globals()['J00436'], globals()['J00084'])
    globals()['I00227'] = not globals()['I00226']

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00226': bool(globals()['I00226']),
    #         'I00227': bool(globals()['I00227'])
    #     }})

    setOutputToRLY()

def MotorToHopperCnvyrC0():

    globals()['I00196'] = frame4and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00540'], globals()['V0146'], globals()['J00437'], globals()['J00085'])
    globals()['I00197'] = not globals()['I00196']

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00196': bool(globals()['I00196']),
    #         'I00197': bool(globals()['I00197'])
    #     }})

    setOutputToRLY()

def PneumToHopperCnvyrC0():

    globals()['I00199'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00439'], globals()['J00087'])
    # print(f"globals()['I00199'] PneumToHopperCnvyrC0: {globals()['I00199']}")
    # print(f"globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00439'], globals()['J00087']\n{globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00439'], globals()['J00087']}")

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00199': bool(globals()['I00199'])
    #     }})

    setOutputToRLY()

def TimerK051(val):
    if val:
        # jalankan timer jid
        print("TimerK051 RUN")
        start_timer("J00203", globals()['V0051'])
    else:
        # reset
        print("TimerK051 STOP")
        globals()['J00203'] = False
        stop_timer("J00203")
        globals()['K051'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00203': bool(globals()['J00203'])
        #     }})

def PneumToHopperCnvyrC1():

    globals()['I00201'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00441'], globals()['J00089'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00201': bool(globals()['I00201'])
    #     }})

    setOutputToRLY()

def TimerK052(val):
    if val:
        # jalankan timer jid
        print("TimerK052 RUN")
        start_timer("J00204", globals()['V0052'])
    else:
        # reset
        print("TimerK052 STOP")
        globals()['J00204'] = False
        stop_timer("J00204")
        globals()['K052'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00204': bool(globals()['J00204'])
        #     }})

def PneumToHopperCnvyrC2():

    globals()['I00203'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00443'], globals()['J00091'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00203': bool(globals()['I00203'])
    #     }})

    setOutputToRLY()

def TimerK053(val):
    if val:
        # jalankan timer jid
        print("TimerK053 RUN")
        start_timer("J00205", globals()['V0053'])
    else:
        # reset
        print("TimerK053 STOP")
        globals()['J00205'] = False
        stop_timer("J00205")
        globals()['K053'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00205': bool(globals()['J00205'])
        #     }})

def PneumToHopperCnvyrC3():


    globals()['I00205'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00445'], globals()['J00093'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00205': bool(globals()['I00205'])
    #     }})

    setOutputToRLY()

def TimerK054(val):
    if val:
        # jalankan timer jid
        print("TimerK054 RUN")
        start_timer("J00206", globals()['V0054'])
    else:
        # reset
        print("TimerK054 STOP")
        globals()['J00206'] = False
        stop_timer("J00206")
        globals()['K054'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00206': bool(globals()['J00206'])
        #     }})

def PneumToHopperCnvyrC4():

    globals()['I00207'] = frame3and2or4and(globals()['I00096'], globals()['J00543'], globals()['V0146'], globals()['J00447'], globals()['J00095'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00207': bool(globals()['I00207'])
    #     }})

    # setOutputToRLY()

def TimerK055(val):
    if val:
        # jalankan timer jid
        print("TimerK055 RUN")
        start_timer("J00207", globals()['V0055'])
    else:
        # reset
        print("TimerK055 STOP")
        globals()['J00207'] = False
        stop_timer("J00207")
        globals()['K055'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00207': bool(globals()['J00207'])
        #     }})

def PneumTbletHoprDoorC0Open():

    globals()['I00214'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00529'], globals()['V0147'], globals()['J00422'], globals()['J00070'], globals()['I00215'], globals()['I00070'])

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00214': bool(globals()['I00214']),
    #         'I00215': bool(globals()['I00215'])
    #     }})


    # setOutputToRLY()

def PneumTbletHoprDoorC0Close():
 
    globals()['I00215'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00529'], globals()['V0147'], globals()['J00423'], globals()['J00071'], globals()['I00214'], globals()['I00071'])
 
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00214': bool(globals()['I00214']),
    #         'I00215': bool(globals()['I00215'])
    #     }})

 
    setOutputToRLY()

def TimerK033():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00070'], globals()['I00214'], globals()['I00071'], globals()['I00215']):
        
        print("TimerK033 RUN")
        start_timer("K033V0033IsJam", globals()['V0033'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00070'], globals()['I00214'], globals()['I00071'], globals()['I00215']):
        print("jidTimerK033 STOOOP")
        stop_timer("K033V0033IsJam")

def TimerK056(val):
    if val:
        # jalankan timer jid
        print("TimerK056 RUN")
        start_timer("J00198", globals()['V0056'])
    else:
        # reset
        print("TimerK056 STOP")
        globals()['J00198'] = False
        stop_timer("J00198")
        globals()['K056'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00198': bool(globals()['J00198'])
        #     }})

def PneumTbletHoprDoorC1Open():
   

    globals()['I00216'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00530'], globals()['V0147'], globals()['J00424'], globals()['J00072'], globals()['I00217'], globals()['I00072'])
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00216': bool(globals()['I00216']),
    #         'I00217': bool(globals()['I00217'])
    #     }})

   
    setOutputToRLY()

def PneumTbletHoprDoorC1Close():
   
    globals()['I00217'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00530'], globals()['V0147'], globals()['J00425'], globals()['J00073'], globals()['I00216'], globals()['I00073'])
   
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00216': bool(globals()['I00216']),
    #         'I00217': bool(globals()['I00217'])
    #     }})

    
    setOutputToRLY()

def TimerK034():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00072'], globals()['I00216'], globals()['I00073'], globals()['I00217']):
        
        print("TimerK034 RUN")
        start_timer("K034V0034IsJam", globals()['V0034'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00072'], globals()['I00216'], globals()['I00073'], globals()['I00217']):
        print("jidTimerK034 STOOOP")
        stop_timer("K034V0034IsJam")

def TimerK057(val):
    if val:
        # jalankan timer jid
        print("TimerK057 RUN")
        start_timer("J00199", globals()['V0057'])
    else:
        # reset
        print("TimerK057 STOP")
        globals()['J00199'] = False
        stop_timer("J00199")
        globals()['K057'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00199': bool(globals()['J00199'])
        #     }})

def PneumTbletHoprDoorC2Open():
   
    globals()['I00218'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00531'], globals()['V0147'], globals()['J00426'], globals()['J00074'], globals()['I00219'], globals()['I00074'])
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00218': bool(globals()['I00218']),
    #         'I00219': bool(globals()['I00219'])
    #     }})

   
    setOutputToRLY()

def PneumTbletHoprDoorC2Close():
   
    globals()['I00219'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00531'], globals()['V0147'], globals()['J00427'], globals()['J00075'], globals()['I00218'], globals()['I00075'])
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00218': bool(globals()['I00218']),
    #         'I00219': bool(globals()['I00219'])
    #     }})


    setOutputToRLY()

def TimerK035():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00074'], globals()['I00218'], globals()['I00075'], globals()['I00219']):
        
        print("TimerK035 RUN")
        start_timer("K035V0035IsJam", globals()['V0035'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00074'], globals()['I00218'], globals()['I00075'], globals()['I00219']):
        print("jidTimerK035 STOOOP")
        stop_timer("K035V0035IsJam")

def TimerK058(val):
    if val:
        # jalankan timer jid
        print("TimerK058 RUN")
        start_timer("J00200", globals()['V0058'])
    else:
        # reset
        print("TimerK058 STOP")
        globals()['J00200'] = False
        stop_timer("J00200")
        globals()['K058'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00200': bool(globals()['J00200'])
        #     }})

def PneumTbletHoprDoorC3Open():
   
    globals()['I00220'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00532'], globals()['V0147'], globals()['J00428'], globals()['J00076'], globals()['I00221'], globals()['I00076'])
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00220': bool(globals()['I00220']),
    #         'I00221': bool(globals()['I00221'])
    #     }})

   
    setOutputToRLY()

def PneumTbletHoprDoorC3Close():
   
    globals()['I00221'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00532'], globals()['V0147'], globals()['J00429'], globals()['J00077'], globals()['I00220'], globals()['I00077'])
    
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00220': bool(globals()['I00220']),
    #         'I00221': bool(globals()['I00221'])
    #     }})

   
    setOutputToRLY()

def TimerK036():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00076'], globals()['I00220'], globals()['I00077'], globals()['I00221']):
        globals()['K036'] = True
        if globals()['K036V0036Start'] == 0:
            globals()['K036V0036Start'] = int(time.time())

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00076'], globals()['I00220'], globals()['I00077'], globals()['I00221']):
        globals()['K036'] = False
        globals()['K036V0036IsJam'] = False
        globals()['K036V0036Start'] = 0
        globals()['U0036'] = 0

def TimerK036():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00076'], globals()['I00220'], globals()['I00077'], globals()['I00221']):
        
        print("TimerK036 RUN")
        start_timer("K036V0036IsJam", globals()['V0036'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00076'], globals()['I00220'], globals()['I00077'], globals()['I00221']):
        print("jidTimerK036 STOOOP")
        stop_timer("K036V0036IsJam")

def TimerK059(val):
    if val:
        # jalankan timer jid
        print("TimerK059 RUN")
        start_timer("J00201", globals()['V0059'])
    else:
        # reset
        print("TimerK059 STOP")
        globals()['J00201'] = False
        stop_timer("J00201")
        globals()['K059'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00201': bool(globals()['J00201'])
        #     }})

def PneumTbletHoprDoorC4Open():
 
    globals()['I00222'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00533'], globals()['V0147'], globals()['J00430'], globals()['J00078'], globals()['I00223'], globals()['I00078'])


    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00222': bool(globals()['I00222']),
    #         'I00223': bool(globals()['I00223'])
    #     }})

   
    setOutputToRLY()

def PneumTbletHoprDoorC4Close():
   
    globals()['I00223'] = frame6and2or4and(globals()['I00096'], globals()['J00543'], globals()['J00533'], globals()['V0147'], globals()['J00431'], globals()['J00079'], globals()['I00222'], globals()['I00079'])


    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00222': bool(globals()['I00222']),
    #         'I00223': bool(globals()['I00223'])
    #     }})

   
    setOutputToRLY()

def TimerK037():
    # Timer Berjalan
    if frameTimer2or2and2and(globals()['I00078'], globals()['I00222'], globals()['I00079'], globals()['I00223']):
        
        print("TimerK037 RUN")
        start_timer("K037V0037IsJam", globals()['V0037'])

    # # Timer Berhenti
    if not frameTimer2or2and2and(globals()['I00078'], globals()['I00222'], globals()['I00079'], globals()['I00223']):
        print("jidTimerK037 STOOOP")
        stop_timer("K037V0037IsJam")

def TimerK060(val):
    if val:
        # jalankan timer jid
        print("TimerK060 RUN")
        start_timer("J00202", globals()['V0060'])
    else:
        # reset
        print("TimerK060 STOP")
        globals()['J00202'] = False
        stop_timer("J00202")
        globals()['K060'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00202': bool(globals()['J00202'])
        #     }})

def autoFeederLineC():
    # time.sleep(3)
    if globals()['V0146'] == 512:
        print("feeder putih")
        # FeederB Putih 
        if not  globals()['K051']:
            globals()['J00439'] = True
            globals()['J00441'] = False
            globals()['J00443'] = False
            globals()['J00445'] = False
            globals()['J00447'] = False

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00439': True,
            #         'J00441': False,
            #         'J00443': False,
            #         'J00445': False,
            #         'J00447': False
            #     }})

            rotaryUnitHopLineC()
        else:
            motorMaterMixOffLineC()    
                   

    elif globals()['V0146'] == 256:
        print(f"globals()['K052'] : {globals()['K052']}") 
        # FeederB Warna1
        if not globals()['K052']:
            globals()['J00439'] = True
            globals()['J00441'] = True
            globals()['J00443'] = False
            globals()['J00445'] = False
            globals()['J00447'] = False

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00439': True,
            #         'J00441': True,
            #         'J00443': False,
            #         'J00445': False,
            #         'J00447': False
            #     }})
            
            rotaryUnitHopLineC()

    elif globals()['V0146'] == 128:
        # Feeder Warna2
        if not globals()['K053']:
            globals()['J00439'] = True
            globals()['J00441'] = True
            globals()['J00443'] = True
            globals()['J00445'] = False
            globals()['J00447'] = False

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00439': True,
            #         'J00441': True,
            #         'J00443': True,
            #         'J00445': False,
            #         'J00447': False
            #     }})
            
            rotaryUnitHopLineC()


    elif globals()['V0146'] == 64:
        # Feeder Warna3
        if not globals()['K054']:
            globals()['J00439'] = True
            globals()['J00441'] = True
            globals()['J00443'] = True
            globals()['J00445'] = True
            globals()['J00447'] = False

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00439': True,
            #         'J00441': True,
            #         'J00443': True,
            #         'J00445': True,
            #         'J00447': False
            #     }})
            
            rotaryUnitHopLineC()
    
    elif globals()['V0146'] == 32:
        # Feeder Warna4
        if not globals()['K055']:
            globals()['J00439'] = True
            globals()['J00441'] = True
            globals()['J00443'] = True
            globals()['J00445'] = True
            globals()['J00447'] = True

            # collection.update_one(
            #     {'_id': ObjectId(objID)},
            #     {'$set': {
            #         'J00439': True,
            #         'J00441': True,
            #         'J00443': True,
            #         'J00445': True,
            #         'J00447': True
            #     }})
            
            rotaryUnitHopLineC()
    
    else:
        motorMaterMixOffLineC()

def rotaryUnitHopLineC():
    print(f"rotaryUnitHopLineC :  globals()['V0154'] { globals()['V0154']}")
    # if not globals()['K048']:
    if globals()['V0154'] == "strtC0":
        globals()['J00417'] = True
        globals()['J00419'] = False
        globals()['J00421'] = False

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00417': True,
        #         'J00419': False,
        #         'J00421': False
        #     }})
        
        K043TrueI00066While()
    elif globals()['V0154'] == "strtC1":
        globals()['J00417'] = True
        globals()['J00419'] = True
        globals()['J00421'] = False

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00417': True,
        #         'J00419': True,
        #         'J00421': False
        #     }})
    
        K043TrueI00066While()
    elif globals()['V0154'] == "strtC2":
        globals()['J00417'] = True
        globals()['J00419'] = True
        globals()['J00421'] = True

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00417': True,
        #         'J00419': True,
        #         'J00421': True
        #     }})
        
        K043TrueI00066While()
    else:
        motorMaterMixOffLineC()

def K043TrueI00066While():
    globals()['J00437'] = True
    globals()['J00436'] = True
    globals()['J00435'] = True
    globals()['J00415'] = True
    globals()['J00434'] = False
    globals()['J00433'] = True
    globals()['J00432'] = True

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00437': True,
    #         'J00436': True,
    #         'J00435': True,
    #         'J00415': True,
    #         'J00434': False,
    #         'J00433': True,
    #         'J00432': True
    #     }})
 
def motorMaterMixOffLineC():
    # globals()['J00413'] = False
    # globals()['J00414'] = False
    globals()['J00432'] = False
    globals()['J00433'] = False
    globals()['J00434'] = False
    globals()['J00415'] = False
    globals()['J00421'] = False
    globals()['J00419'] = False
    globals()['J00417'] = False
    globals()['J00435'] = False
    globals()['J00436'] = False
    globals()['J00437'] = False
    globals()['J00447'] = False
    globals()['J00445'] = False
    globals()['J00443'] = False
    globals()['J00441'] = False
    globals()['J00439'] = False

    # collection.update_one(
    # {'_id': ObjectId(objID)},
    # {'$set': {
    #     'J00413': False,
    #     'J00414': False,
    #     'J00432': False,
    #     'J00433': False,
    #     'J00434': False,
    #     'J00415': False,
    #     'J00421': False,
    #     'J00419': False,
    #     'J00417': False,
    #     'J00435': False,
    #     'J00436': False,
    #     'J00437': False,
    #     'J00447': False,
    #     'J00445': False,
    #     'J00443': False,
    #     'J00441': False,
    #     'J00439': False

    #     }})

    # if bool(globals()['V0146']):
    #     print("ulang keatas")
    #     autoFeederLineC()

def autoHopperLineC():
    if globals()['V0147'] == 16:
        # HopperC Putih
        if not globals()['K056']:
            print("masuk while buka pintu tblethopdoor0")
            while not globals()['I00070']:
                globals()['J00423'] = False
                globals()['J00422'] = True
                # collection.update_one(
                # {'_id': ObjectId(objID)},
                # {'$set': {
                #     'J00423': False,
                #     'J00422': True
                #     }})
            print("Exit while buka pintu tblethopdoor0")
        else:
            hopperElseFalseLineC()

    elif globals()['V0147'] == 8:
        # HopperC Warna1    
        if not globals()['K057']:
            print("masuk while buka pintu tblethopdoor1")
            while not globals()['I00072']:
                globals()['J00425'] = False
                globals()['J00424'] = True
                # collection.update_one(
                # {'_id': ObjectId(objID)},
                # {'$set': {
                #     'J00425': False,
                #     'J00424': True
                #     }})
            print("exit while buka pintu tblethopdoor1")
        else:
            hopperElseFalseLineC()

    elif globals()['V0147'] == 3:
        # HopperC Warna2
        if not globals()['K058']:
            print("masuk while buka pintu tblethopdoor2")
            while not globals()['I00074']:
                globals()['J00427'] = False
                globals()['J00426'] = True
                # collection.update_one(
                # {'_id': ObjectId(objID)},
                # {'$set': {
                #     'J00427': False,
                #     'J00426': True
                #     }})
            print("exit while buka pintu tblethopdoor2")
        else:
            hopperElseFalseLineC()
    elif globals()['V0147'] == 2:
        # HopperC Warna3
        if not globals()['K059']:
            print("masuk while buka pintu tblethopdoor3")
            while not globals()['I00076']:
                globals()['J00429'] = False
                globals()['J00428'] = True
                # collection.update_one(
                # {'_id': ObjectId(objID)},
                # {'$set': {
                #     'J00429': False,
                #     'J00428': True
                #     }})
            print("exit while buka pintu tblethopdoor3")
        else:
            hopperElseFalseLineC()

    elif globals()['V0147'] == 1:
        # HopperC Warna4
        if not globals()['K060']:
            print("masuk while buka pintu tblethopdoor4")
            while not globals()['I00078']:
                globals()['J00431'] = False
                globals()['J00430'] = True
                # collection.update_one(
                # {'_id': ObjectId(objID)},
                # {'$set': {
                #     'J00431': False,
                #     'J00430': True
                #     }})
            print("masuk while buka pintu tblethopdoor4")
        else:
            hopperElseFalseLineC()
    # else:
    #     hopperElseFalseLineC()

def hopperElseFalseLineC():
    globals()['J00430'] = False
    globals()['J00431'] = False
    globals()['J00428'] = False
    globals()['J00429'] = False
    globals()['J00426'] = False
    globals()['J00427'] = False
    globals()['J00424'] = False
    globals()['J00425'] = False
    globals()['J00422'] = False
    globals()['J00423'] = False

    # collection.update_one(
    # {'_id': ObjectId(objID)},
    # {'$set': {
    #     'J00430': False,
    #     'J00431': False,
    #     'J00428': False,
    #     'J00429': False,
    #     'J00426': False,
    #     'J00427': False,
    #     'J00424': False,
    #     'J00425': False,
    #     'J00422': False,
    #     'J00423': False
    #     }})

    print("All Hooper False")

def TimerK043(val):
    if val and bool(globals()['V0149']):
        # jalankan timer jid
        print("TimerK043 RUN")
        start_timer("J00251", globals()['V0043'])
    else:
        # reset
        print("TimerK043 STOP - TimerK043")
        stop_timer("J00251")
        globals()['J00251'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00251': False
        #     }})

def ResetTimerK043():
# Stop Timer Mixing C
    if globals()['J00249']:
        print("TimerK043 STOP - ResetTimerK043")
        stop_timer("J00251")
        globals()['J00251'] = False
        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00251': False
        #     }})

def v0154staC0():
    in0 = bool(globals()['V0154'] == "stopC2" and not globals()['J00208'])
    in1 = bool(globals()['V0154'] == "stopC1" and globals()['J00210'] and not globals()['J00208'])

    print(f"in0 {in0} . in1 {in1}")

    if in0 or in1:
        globals()['V0154'] = "strtC0"
        collection.update_one(
                {'_id': ObjectId(objID)},
                {'$set': {
                    'V0154': globals()['V0154']
                    }})
        
def v0154stopC0():
    if globals()['J00208'] and globals()['V0154'] == "strtC0":
        globals()['V0154'] = "stopC0"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0154': globals()['V0154']
                }})   
    
def v0154staC1():
    in0 = bool(globals()['V0154'] == "stopC0" and not globals()['J00209'])
    in1 = bool(globals()['V0154'] == "stopC2" and globals()['J00208'] and not globals()['J00209'])

    print(f"staC1 : in0 {in0} . in1 {in1}")

    if in0 or in1:
        globals()['V0154'] = "strtC1"
        collection.update_one(
                {'_id': ObjectId(objID)},
                {'$set': {
                    'V0154': globals()['V0154']
                    }})

def v0154stopC1():
    if globals()['J00209'] and globals()['V0154'] == "strtC1":
        globals()['V0154'] = "stopC1"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0154': globals()['V0154']
                }})   

def v0154staC2():
    in0 = bool(globals()['V0154'] == "stopC1" and not globals()['J00210'])
    in1 = bool(globals()['V0154'] == "stopC0" and globals()['J00209'] and not globals()['J00210'])

    if in0 or in1:
        globals()['V0154'] = "strtC2"
        collection.update_one(
                {'_id': ObjectId(objID)},
                {'$set': {
                    'V0154': globals()['V0154']
                    }})

def v0154stopC2():
    if globals()['J00210'] and globals()['V0154'] == "strtC2":
        globals()['V0154'] = "stopC2"
        collection.update_one(
            {'_id': ObjectId(objID)},
            {'$set': {
                'V0154': globals()['V0154']
                }}) 

def V0154change():
    v0154staC0()
    v0154stopC0()
    v0154staC1()
    v0154stopC1()
    v0154staC2()
    v0154stopC2()
    autoFeederLineC()

def J00208change():
    print(f"J00208change start : {globals()['V0154']}")
    v0154stopC0()
    v0154staC1()
    v0154staC0()
    print(f"J00208change trigger : {globals()['V0154']}")

def J00209change():
    print(f"J00209change start : {globals()['V0154']}")
    v0154staC1()
    v0154stopC1()
    v0154staC2()
    print(f"J00209change trigger : {globals()['V0154']}")

def J00210change():
    print(f"J00210change start : {globals()['V0154']}")
    v0154staC2()
    print(f". . {globals()['V0154']}")
    v0154stopC2()
    print(f". . . {globals()['V0154']}")
    v0154staC0()
    print(f"J00210change trigger : {globals()['V0154']}")

def FillerMixerCLogic():

    runFillMixerC = frameFillMixer(globals()['V0149'], globals()['J00410'], globals()['J00057'], globals()['J00250'], globals()['J00251'])

    print(f"runFillMixerC : {runFillMixerC}")
    print(f"globals()['V0149'], globals()['J00410'], globals()['J00057'], globals()['J00250'], globals()['J00251']\n{globals()['V0149'], globals()['J00410'], globals()['J00057'], globals()['J00250'], globals()['J00251']}")

    if runFillMixerC:
        FillMixerCStart()

def FillMixerCStart():
    globals()['J00249'] = True
    print(f"------> FillMixerCStart")
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00249': globals()['J00249']
    #     }})
    
    print(f"masuk While tutup pintu :  globals()['I00066'] { globals()['I00066']}")
    while not bool(globals()['I00066']):
        globals()['J00413'] = False
        globals()['J00414'] = True
        # collection.update_one(
        # {'_id': ObjectId(objID)},
        # {'$set': {
        #     'J00413': False,
        #     'J00414': True
        #     }})
    print(f"exit While tutup pintu")
    globals()['J00413'] = False
    globals()['J00414'] = False
    globals()['J00412'] = False
    globals()['J00411'] = True

    globals()['J00249'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00413': False,
    #         'J00414': False,
    #         'J00412': False,
    #         'J00411': True,
    #         'J00249': False
    #         }})

def DumpMixerCLogic():
    runDumpMixerC = frameDumpMixer(globals()['J00058'], globals()['J00251'], globals()['J00249'])

    if runDumpMixerC:
        DumpMixerCStart()

def DumpMixerCStart():
    globals()['J00250'] = True

    globals()['J00411'] = False
    globals()['J00412'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00250': globals()['J00250'],
    #         'J00411': globals()['J00411'],
    #         'J00412': globals()['J00412']
    #     }})
    
    print(f"masuk While BUKA pintu :  globals()['I00065'] { globals()['I00065']}")
    while not bool(globals()['I00065']):
        globals()['J00414'] = False
        globals()['J00413'] = True

        # collection.update_one(
        #     {'_id': ObjectId(objID)},
        #     {'$set': {
        #         'J00414': globals()['J00414'],
        #         'J00413': globals()['J00413']
        #     }})
    
    print(f">> EXIT While BUKA pintu :  globals()['I00065'] { globals()['I00065']}")

    globals()['J00414'] = False
    globals()['J00413'] = False
    globals()['J00250'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00414': globals()['J00414'],
    #         'J00413': globals()['J00413'],
    #         'J00250': globals()['J00250']
    #     }})

# END LOGIC CODE LINE C - MANUAL AUTO

# CODE DEBU
def isManytoFull():
    # globals()['J00211'] = True
    
    # globals()['I00080'] = True

    globals()['I00006'] = True
    globals()['I00007'] = True
    globals()['I00008'] = True
    globals()['I00009'] = True
    globals()['I00010'] = True
    globals()['I00014'] = True
    globals()['I00015'] = True
    globals()['I00016'] = True
    globals()['I00017'] = True
    globals()['I00018'] = True
    globals()['I00019'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00006': True,
    #         'I00007': True,
    #         'I00008': True,
    #         'I00009': True,
    #         'I00010': True,
    #         'I00014': True,
    #         'I00015': True,
    #         'I00016': True,
    #         'I00017': True,
    #         'I00018': True,
    #         'I00019': True
    #     }})

def oldisManytoFullReset():
    globals()['I00006'] = False
    globals()['I00007'] = False
    globals()['I00008'] = False
    globals()['I00009'] = False
    globals()['I00010'] = False
    globals()['I00014'] = False
    globals()['I00015'] = False
    globals()['I00016'] = False
    globals()['I00017'] = False
    globals()['I00018'] = False
    globals()['I00019'] = False
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00006': False,
    #         'I00007': False,
    #         'I00008': False,
    #         'I00009': False,
    #         'I00010': False,
    #         'I00014': False,
    #         'I00015': False,
    #         'I00016': False,
    #         'I00017': False,
    #         'I00018': False,
    #         'I00019': False
    #     }})
    # print(f"{globals()['J00528']}")
    # print(f"{globals()['K032V0032IsJam']}")

def isManytoFullReset():
    globals()['J00175'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00175': True
    #     }})
    # print(f"{globals()['J00528']}")
    # print(f"{globals()['K032V0032IsJam']}")


def isJam():
    # globals()['J00528'] = True
    # globals()['J00529'] = True
    # globals()['J00530'] = True
    # globals()['J00531'] = True
    # globals()['J00532'] = True
    # globals()['J00533'] = True
    # globals()['J00534'] = True
    # globals()['J00535'] = True
    # globals()['J00536'] = True
    # globals()['J00537'] = True
    # globals()['J00538'] = True
    # globals()['J00539'] = True
    # globals()['J00540'] = True

    globals()['I00064'] = True
    globals()['I00067'] = True
    globals()['I00068'] = True
    globals()['I00069'] = True
    globals()['I00083'] = True
    globals()['I00084'] = True
    globals()['I00085'] = True

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00064': True,
    #         'I00067': True,
    #         'I00068': True,
    #         'I00069': True,
    #         'I00083': True,
    #         'I00084': True,
    #         'I00085': True
    #     }})
    
def on1fault():
    globals()['J00139'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00139': True
    #     }})

def on2fault():
    globals()['I00081'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00081': True
    #     }})

def on3fault():
    globals()['I00082'] = True
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00082': True
    #     }})

def isJamReset():
    globals()['I00064'] = False
    globals()['I00067'] = False
    globals()['I00068'] = False
    globals()['I00069'] = False
    globals()['I00083'] = False
    globals()['I00084'] = False
    globals()['I00085'] = False

    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'I00064': False,
    #         'I00067': False,
    #         'I00068': False,
    #         'I00069': False,
    #         'I00083': False,
    #         'I00084': False,
    #         'I00085': False
    #     }})

def oldresetAuto():
    globals()['V0146'] = 0
    globals()['V0147'] = 0
    globals()['V0144'] = 0
    globals()['V0145'] = 0
    # globals()['J00439'] = False
    # globals()['J00417'] = False
    # LINE B
    globals()['J00352'] = False
    globals()['J00353'] = False
    globals()['J00354'] = False
    globals()['J00355'] = False
    globals()['J00356'] = False
    globals()['J00368'] = False
    globals()['J00369'] = False
    globals()['J00357'] = False
    globals()['J00367'] = False
    globals()['J00365'] = False
    globals()['J00363'] = False
    globals()['J00361'] = False
    globals()['J00359'] = False
    globals()['J00384'] = False
    globals()['J00385'] = False
    globals()['J00370'] = False
    globals()['J00378'] = False
    globals()['J00376'] = False
    globals()['J00374'] = False
    globals()['J00372'] = False


    # LINE C
    globals()['J00411'] = False
    globals()['J00413'] = False
    globals()['J00414'] = False
    globals()['J00432'] = False
    globals()['J00433'] = False
    globals()['J00434'] = False
    globals()['J00415'] = False
    globals()['J00421'] = False
    globals()['J00419'] = False
    globals()['J00417'] = False
    globals()['J00435'] = False
    globals()['J00436'] = False
    globals()['J00437'] = False
    globals()['J00447'] = False
    globals()['J00445'] = False
    globals()['J00443'] = False
    globals()['J00441'] = False
    globals()['J00439'] = False
    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         # LINE B
    #         'J00352' : False,
    #         'J00353' : False,
    #         'J00354' : False,
    #         'J00355' : False,
    #         'J00356' : False,
    #         'J00368' : False,
    #         'J00369' : False,
    #         'J00357' : False,
    #         'J00367' : False,
    #         'J00365' : False,
    #         'J00363' : False,
    #         'J00361' : False,
    #         'J00359' : False,
    #         'J00384' : False,
    #         'J00385' : False,
    #         'J00370' : False,
    #         'J00378' : False,
    #         'J00376' : False,
    #         'J00374' : False,
    #         'J00372' : False,

    #         # 'J00439': False,
    #         # 'J00417': False,
    #         # LINE C
    #         'J00411': False,
    #         'J00413': False,
    #         'J00414': False,
    #         'J00432': False,
    #         'J00433': False,
    #         'J00434': False,
    #         'J00415': False,
    #         'J00421': False,
    #         'J00419': False,
    #         'J00417': False,
    #         'J00435': False,
    #         'J00436': False,
    #         'J00437': False,
    #         'J00447': False,
    #         'J00445': False,
    #         'J00443': False,
    #         'J00441': False,
    #         'J00439': False,
    #         'V0146': 0,
    #         'V0147': 0,
    #         'V0144': 0,
    #         'V0145': 0
    #     }})
    
def resetAuto():
    # Filler C
    globals()['J00249'] = False
    # Dump C
    globals()['J00250'] = False

    globals()['J00413'] = False
    globals()['J00414'] = False
    globals()['J00412'] = False
    globals()['J00411'] = False

    # Filler B
    globals()['J00243'] = False
    # Dump B
    globals()['J00244'] = False
    globals()['J00354'] = False
    globals()['J00355'] = False
    globals()['J00353'] = False
    globals()['J00352'] = False

    globals()['J00389'] = False
    globals()['J00410'] = False


    # collection.update_one(
    #     {'_id': ObjectId(objID)},
    #     {'$set': {
    #         'J00249' : False,
    #         'J00250' : False,
    #         'J00413' : False,
    #         'J00414' : False,
    #         'J00412' : False,
    #         'J00411' : False,
    #         'J00243' : False,
    #         'J00244' : False,
    #         'J00354' : False,
    #         'J00355' : False,
    #         'J00353' : False,
    #         'J00352' : False,
    #         'J00389' : False,
    #         'J00410' : False,
    #     }})
    
def AllAlarmReset():
    collection.update_one(
        {'_id': ObjectId(objID)},
        {'$set': {
            'V0157': 0,
            'V0158': 0,
            'V0159': 0
        }})
# END CODE DEBUG

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Unitama Machine Server")
app.geometry("1000x400")

setOutputToRLY()

frm1 = ctk.CTkFrame(app)
frm1.pack(padx=5, pady=(1, 1))
AntrianLBL = ctk.CTkLabel(frm1, text="[]")
AntrianLBL.grid(row=0, column=0, padx=1, pady=1)
# button2 = ctk.CTkButton(frm1, text="ErrIsMany", fg_color="green", command=isManytoFull)
# button2.grid(row=1, column=0, padx=5, pady=10)
# button2o = ctk.CTkButton(frm1, text="isManyReset", fg_color="green", command=isManytoFullReset)
# button2o.grid(row=1, column=1, padx=5, pady=10)
# button2oa = ctk.CTkButton(frm1, text="resetAuto", fg_color="red", command=resetAuto)
# button2oa.grid(row=1, column=2, padx=5, pady=10)
# button3 = ctk.CTkButton(frm1, text="AllAlarmReset", fg_color="green", command=AllAlarmReset)
# button3.grid(row=2, column=0, padx=5, pady=10)
# button3o = ctk.CTkButton(frm1, text="isJamAll", fg_color="green", command=isJam)
# button3o.grid(row=2, column=1, padx=5, pady=10)
# button3r = ctk.CTkButton(frm1, text="isJamAllReset", fg_color="green", command=isJamReset)
# button3r.grid(row=2, column=2, padx=5, pady=10)
button4a = ctk.CTkButton(frm1, text="1", fg_color="orange", command=on1fault)
button4a.grid(row=3, column=0, padx=5, pady=10)
# button4b = ctk.CTkButton(frm1, text="2", fg_color="orange", command=on2fault)
# button4b.grid(row=3, column=1, padx=5, pady=10)
# button4c = ctk.CTkButton(frm1, text="3", fg_color="orange", command=on3fault)
# button4c.grid(row=3, column=2, padx=5, pady=10)
lblinfo = ctk.CTkLabel(frm1, text="[]")
lblinfo.grid(row=4, column=0, padx=1, pady=5)
lblinfo2 = ctk.CTkLabel(frm1, text="[]")
lblinfo2.grid(row=5, column=0, padx=1, pady=5)
lblinfo3 = ctk.CTkLabel(frm1, text="[]")
lblinfo3.grid(row=6, column=0, padx=1, pady=5)
lblinfo4 = ctk.CTkLabel(frm1, text="[]")
lblinfo4.grid(row=7, column=0, padx=1, pady=5)

listenTriggerMongoDBThread = threading.Thread(target=listenTriggerMongoDB)
listenTriggerMongoDBThread.daemon = True
listenTriggerMongoDBThread.start()

# setInputFromDIOThread = threading.Thread(target=setInputFromDIO)
# setInputFromDIOThread.daemon = True
# setInputFromDIOThread.start()

queueManageThread = threading.Thread(target=queueManage)
queueManageThread.daemon = True
queueManageThread.start()

def handle_sigterm(signum, frame):
    print("\n🔚 Received termination signal")
    collection.delete_one({"_id": doc_antrian.inserted_id})
    sys.exit(0)
    
signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigterm)

try:
    app.mainloop()  # Start your Tkinter application
except KeyboardInterrupt:
    print("\n🚨 Application terminated by user (Ctrl+C)")
    collection.delete_one({"_id": doc_antrian.inserted_id})
    sys.exit(1)
except Exception as e:
    print(f"\n🔥 Application crashed: {str(e)}")
    collection.delete_one({"_id": doc_antrian.inserted_id})

# result = ydu.YduClose(input_id)
# result = ydu.YduClose(output_id)
