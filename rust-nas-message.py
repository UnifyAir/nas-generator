from docx import Document
import re, os, sys, string
import datetime
import getopt
import getpass

version = "0.2.0"

msg_list = {}
type_list = {}

verbosity = 0
filename = ""
outdir = './'
cachedir = './cache/'
currentdir = './'

FAIL = '\033[91m'
INFO = '\033[93m'
ENDC = '\033[0m'

def d_print(string):
    if verbosity > 0:
        sys.stdout.write(string)

def d_info(string):
    sys.stdout.write(INFO + string + ENDC + "\n")

def d_error(string):
    sys.stderr.write(FAIL + string + ENDC + "\n")
    sys.exit(0)

def write_file(f, string):
    f.write(string)
    d_print(string)

def output_header_to_file(f):
    now = datetime.datetime.now()

    f.write("/*******************************************************************************\n")
    f.write(" * This file had been created by rust-nas-message.py script v%s\n" % (version))
    f.write(" * Please do not modify this file but regenerate it via script.\n")
    f.write(" * Created on: %s by %s\n * from %s\n" % (str(now), getpass.getuser(), filename))
    f.write(" ******************************************************************************/\n\n")

def usage():
    print("Python generating NAS Message encoder/decoder v%s" % (version))
    print("Usage: python nas-message.py [options]")
    print("Available options:")
    print("-d        Enable script debug")
    print("-f [file] Input file to parse")
    print("-o [dir]  Output files to given directory")
    print("-c [dir]  Cache files to given directory")
    print("-h        Print this help and return")

def prefix_if_starts_with_digit(text: str) -> str:
    if text and text[0].isdigit():
        # Convert leading digit to English word
        digit_words = {
            '0': 'Zero',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }
        # Capitalize the first letter after the digit
        if len(text) > 1:
            return digit_words[text[0]] + text[1].upper() + text[2:]
        else:
            return digit_words[text[0]]
    return text    

def v_upper(v):
    return re.sub('\'', '_', re.sub('/', '_', re.sub('-', '_', re.sub(' ', '_', v)))).upper()

def v_lower(v):
    return re.sub('\'', '_', re.sub('/', '_', re.sub('-', '_', re.sub(' ', '_', v)))).lower()

def v_camel_case(v):
    parts = re.split(r'[^\w]+', v)
    parts = [part for part in parts if part]
    capitalized_parts = [part.capitalize() for part in parts]
    return "".join(capitalized_parts)

def get_value(v):
    return re.sub('5gs_', '', re.sub('5g_', '', re.sub('5gsm', 'gsm', re.sub('5gmm', 'gmm', re.sub('\'', '_', re.sub('/', '_', re.sub('-', '_', re.sub(' ', '_', v)))).lower()))))

def length_to_type(length, field_name, format):
    try:
        raw_length = int(length)
    except ValueError:
        return field_name
        # if length == "1/2":
        #     return field_name
        # else:
        #     return field_name + "<Vec<u8>>"

    if format == "TLV" or format == "TLV-E":
        raw_length -= 2;
    if format == "LV" or format == "LV-E":
        raw_length -= 1;
    if format == "TV" or format == "TV-E":
        raw_length -= 1;

    return field_name    
    # if raw_length == 1:
    #     return field_name
    # else:
    #     return field_name + "<Vec<u8>>"

def get_cells(cells):
    iei = cells[0].text
    value = cells[1].text.encode('ascii', 'ignore').decode('utf-8')
    value = re.sub("\s*$", "", re.sub("\s*\n*\s*\([^\)]*\)*", "", re.sub("\"|'s", "", value)))
    type = re.sub("^NAS ", "", re.sub("'s", "", re.sub('\s*\n\s*[a-zA-Z0-9.]*', '', cells[2].text)))
    reference = re.sub('[a-zA-Z0-9\'\-\s]*\n\s*', '', cells[2].text)
    presence = cells[3].text
    format = cells[4].text
    length = cells[5].text

# Spec errata - workaround
    if (type == "Request type" and value == "Request type"):
        iei = "8-"

    return { "iei" : iei, "value" : value, "type" : type, "reference" : reference, "presence" : presence, "format" : format, "length" : length }

def write_cells_to_file(name, cells):
    write_file(f, name + ".append({ \"iei\" : \"" + cells["iei"] + \
        "\", \"value\" : \"" + cells["value"] + \
        "\", \"type\" : \"" + cells["type"] + \
        "\", \"reference\" : \"" + cells["reference"] + \
        "\", \"presence\" : \"" + cells["presence"] + \
        "\", \"format\" : \"" + cells["format"] + \
        "\", \"length\" : \"" + cells["length"] + "\"})\n")

try:
    opts, args = getopt.getopt(sys.argv[1:], "df:ho:c:", ["debug", "file", "help", "output", "cache"])
except getopt.GetoptError as err:
    # print help information and exit:
    usage()
    sys.exit(2)

for o, a in opts:
    if o in ("-d", "--debug"):
        verbosity = 1
    if o in ("-f", "--file"):
        filename = a
    if o in ("-o", "--output"):
        outdir = a
        if outdir.rfind('/') != len(outdir):
            outdir += '/'
    if o in ("-c", "--cache"):
        cache = a
        if cachedir.rfind('/') != len(cachedir):
            cachedir += '/'
    if o in ("-h", "--help"):
        usage()
        sys.exit(2)

# Message Type List

msg_list["REGISTRATION REQUEST"] = { "type" : "65" }
msg_list["REGISTRATION ACCEPT"] = { "type" : "66" }
msg_list["REGISTRATION COMPLETE"] = { "type" : "67" }
msg_list["REGISTRATION REJECT"] = { "type" : "68" }
msg_list["DEREGISTRATION REQUEST FROM UE"] = { "type" : "69" }
msg_list["DEREGISTRATION ACCEPT FROM UE"] = { "type" : "70" }
msg_list["DEREGISTRATION REQUEST TO UE"] = { "type" : "71" }
msg_list["DEREGISTRATION ACCEPT TO UE"] = { "type" : "72" }
msg_list["SERVICE REQUEST"] = { "type" : "76" }
msg_list["SERVICE REJECT"] = { "type" : "77" }
msg_list["SERVICE ACCEPT"] = { "type" : "78" }
msg_list["CONFIGURATION UPDATE COMMAND"] = { "type" : "84" }
msg_list["CONFIGURATION UPDATE COMPLETE"] = { "type" : "85" }
msg_list["AUTHENTICATION REQUEST"] = { "type" : "86" }
msg_list["AUTHENTICATION RESPONSE"] = { "type" : "87" }
msg_list["AUTHENTICATION REJECT"] = { "type" : "88" }
msg_list["AUTHENTICATION FAILURE"] = { "type" : "89" }
msg_list["AUTHENTICATION RESULT"] = { "type" : "90" }
msg_list["IDENTITY REQUEST"] = { "type" : "91" }
msg_list["IDENTITY RESPONSE"] = { "type" : "92" }
msg_list["SECURITY MODE COMMAND"] = { "type" : "93" }
msg_list["SECURITY MODE COMPLETE"] = { "type" : "94" }
msg_list["SECURITY MODE REJECT"] = { "type" : "95" }
msg_list["5GMM STATUS"] = { "type" : "100" }
msg_list["NOTIFICATION"] = { "type" : "101" }
msg_list["NOTIFICATION RESPONSE"] = { "type" : "102" }
msg_list["UL NAS TRANSPORT"] = { "type" : "103" }
msg_list["DL NAS TRANSPORT"] = { "type" : "104" }

msg_list["PDU SESSION ESTABLISHMENT REQUEST"] = { "type" : "193" }
msg_list["PDU SESSION ESTABLISHMENT ACCEPT"] = { "type" : "194" }
msg_list["PDU SESSION ESTABLISHMENT REJECT"] = { "type" : "195" }
msg_list["PDU SESSION AUTHENTICATION COMMAND"] = { "type" : "197" }
msg_list["PDU SESSION AUTHENTICATION COMPLETE"] = { "type" : "198" }
msg_list["PDU SESSION AUTHENTICATION RESULT"] = { "type" : "199" }
msg_list["PDU SESSION MODIFICATION REQUEST"] = { "type" : "201" }
msg_list["PDU SESSION MODIFICATION REJECT"] = { "type" : "202" }
msg_list["PDU SESSION MODIFICATION COMMAND"] = { "type" : "203" }
msg_list["PDU SESSION MODIFICATION COMPLETE"] = { "type" : "204" }
msg_list["PDU SESSION MODIFICATION COMMAND REJECT"] = { "type" : "205" }
msg_list["PDU SESSION RELEASE REQUEST"] = { "type" : "209" }
msg_list["PDU SESSION RELEASE REJECT"] = { "type" : "210" }
msg_list["PDU SESSION RELEASE COMMAND"] = { "type" : "211" }
msg_list["PDU SESSION RELEASE COMPLETE"] = { "type" : "212" }
msg_list["5GSM STATUS"] = { "type" : "214" }

# Payload type for message list
msg_list["REGISTRATION REQUEST"]["payload_type"] = "gmm"
msg_list["REGISTRATION ACCEPT"]["payload_type"] = "gmm"
msg_list["REGISTRATION COMPLETE"]["payload_type"] = "gmm"
msg_list["REGISTRATION REJECT"]["payload_type"] = "gmm"
msg_list["DEREGISTRATION REQUEST FROM UE"]["payload_type"] = "gmm"
msg_list["DEREGISTRATION ACCEPT FROM UE"]["payload_type"] = "gmm"
msg_list["DEREGISTRATION REQUEST TO UE"]["payload_type"] = "gmm"
msg_list["DEREGISTRATION ACCEPT TO UE"]["payload_type"] = "gmm"
msg_list["SERVICE REQUEST"]["payload_type"] = "gmm"
msg_list["SERVICE REJECT"]["payload_type"] = "gmm"
msg_list["SERVICE ACCEPT"]["payload_type"] = "gmm"
msg_list["CONFIGURATION UPDATE COMMAND"]["payload_type"] = "gmm"
msg_list["CONFIGURATION UPDATE COMPLETE"]["payload_type"] = "gmm"
msg_list["AUTHENTICATION REQUEST"]["payload_type"] = "gmm"
msg_list["AUTHENTICATION RESPONSE"]["payload_type"] = "gmm"
msg_list["AUTHENTICATION REJECT"]["payload_type"] = "gmm"
msg_list["AUTHENTICATION FAILURE"]["payload_type"] = "gmm"
msg_list["AUTHENTICATION RESULT"]["payload_type"] = "gmm"
msg_list["IDENTITY REQUEST"]["payload_type"] = "gmm"
msg_list["IDENTITY RESPONSE"]["payload_type"] = "gmm"
msg_list["SECURITY MODE COMMAND"]["payload_type"] = "gmm"
msg_list["SECURITY MODE COMPLETE"]["payload_type"] = "gmm"
msg_list["SECURITY MODE REJECT"]["payload_type"] = "gmm"
msg_list["5GMM STATUS"]["payload_type"] = "gmm"
msg_list["NOTIFICATION"]["payload_type"] = "gmm"
msg_list["NOTIFICATION RESPONSE"]["payload_type"] = "gmm"
msg_list["UL NAS TRANSPORT"]["payload_type"] = "gmm"
msg_list["DL NAS TRANSPORT"]["payload_type"] = "gmm"

msg_list["PDU SESSION ESTABLISHMENT REQUEST"]["payload_type"] = "gsm"
msg_list["PDU SESSION ESTABLISHMENT ACCEPT"]["payload_type"] = "gsm"
msg_list["PDU SESSION ESTABLISHMENT REJECT"]["payload_type"] = "gsm"
msg_list["PDU SESSION AUTHENTICATION COMMAND"]["payload_type"] = "gsm"
msg_list["PDU SESSION AUTHENTICATION COMPLETE"]["payload_type"] = "gsm"
msg_list["PDU SESSION AUTHENTICATION RESULT"]["payload_type"] = "gsm"
msg_list["PDU SESSION MODIFICATION REQUEST"]["payload_type"] = "gsm"
msg_list["PDU SESSION MODIFICATION REJECT"]["payload_type"] = "gsm"
msg_list["PDU SESSION MODIFICATION COMMAND"]["payload_type"] = "gsm"
msg_list["PDU SESSION MODIFICATION COMPLETE"]["payload_type"] = "gsm"
msg_list["PDU SESSION MODIFICATION COMMAND REJECT"]["payload_type"] = "gsm"
msg_list["PDU SESSION RELEASE REQUEST"]["payload_type"] = "gsm"
msg_list["PDU SESSION RELEASE REJECT"]["payload_type"] = "gsm"
msg_list["PDU SESSION RELEASE COMMAND"]["payload_type"] = "gsm"
msg_list["PDU SESSION RELEASE COMPLETE"]["payload_type"] = "gsm"
msg_list["5GSM STATUS"]["payload_type"] = "gsm"

# Table number for Message List
msg_list["AUTHENTICATION REQUEST"]["table"] = 0
msg_list["AUTHENTICATION RESPONSE"]["table"] = 1
msg_list["AUTHENTICATION RESULT"]["table"] = 2
msg_list["AUTHENTICATION FAILURE"]["table"] = 3
msg_list["AUTHENTICATION REJECT"]["table"] = 4
msg_list["REGISTRATION REQUEST"]["table"] = 5
msg_list["REGISTRATION ACCEPT"]["table"] = 6
msg_list["REGISTRATION COMPLETE"]["table"] = 7
msg_list["REGISTRATION REJECT"]["table"] = 8
msg_list["UL NAS TRANSPORT"]["table"] = 9
msg_list["DL NAS TRANSPORT"]["table"] = 10
msg_list["DEREGISTRATION REQUEST FROM UE"]["table"] = 11
msg_list["DEREGISTRATION ACCEPT FROM UE"]["table"] = 12
msg_list["DEREGISTRATION REQUEST TO UE"]["table"] = 13
msg_list["DEREGISTRATION ACCEPT TO UE"]["table"] = 14
msg_list["SERVICE REQUEST"]["table"] = 15
msg_list["SERVICE ACCEPT"]["table"] = 16
msg_list["SERVICE REJECT"]["table"] = 17
msg_list["CONFIGURATION UPDATE COMMAND"]["table"] = 18
msg_list["CONFIGURATION UPDATE COMPLETE"]["table"] = 19
msg_list["IDENTITY REQUEST"]["table"] = 20
msg_list["IDENTITY RESPONSE"]["table"] = 21
msg_list["NOTIFICATION"]["table"] = 22
msg_list["NOTIFICATION RESPONSE"]["table"] = 23
msg_list["SECURITY MODE COMMAND"]["table"] = 24
msg_list["SECURITY MODE COMPLETE"]["table"] = 25
msg_list["SECURITY MODE REJECT"]["table"] = 26
msg_list["5GMM STATUS"]["table"] = 28

msg_list["PDU SESSION ESTABLISHMENT REQUEST"]["table"] = 38
msg_list["PDU SESSION ESTABLISHMENT ACCEPT"]["table"] = 39
msg_list["PDU SESSION ESTABLISHMENT REJECT"]["table"] = 40
msg_list["PDU SESSION AUTHENTICATION COMMAND"]["table"] = 41
msg_list["PDU SESSION AUTHENTICATION COMPLETE"]["table"] = 42
msg_list["PDU SESSION AUTHENTICATION RESULT"]["table"] = 43
msg_list["PDU SESSION MODIFICATION REQUEST"]["table"] = 44
msg_list["PDU SESSION MODIFICATION REJECT"]["table"] = 45
msg_list["PDU SESSION MODIFICATION COMMAND"]["table"] = 46
msg_list["PDU SESSION MODIFICATION COMPLETE"]["table"] = 47
msg_list["PDU SESSION MODIFICATION COMMAND REJECT"]["table"] = 48
msg_list["PDU SESSION RELEASE REQUEST"]["table"] = 49
msg_list["PDU SESSION RELEASE REJECT"]["table"] = 50
msg_list["PDU SESSION RELEASE COMMAND"]["table"] = 51
msg_list["PDU SESSION RELEASE COMPLETE"]["table"] = 52
msg_list["5GSM STATUS"]["table"] = 53

for key in msg_list.keys():
    if "table" not in msg_list[key].keys():
        continue;

    d_info("[" + key + "]")
    cachefile = cachedir + "nas-msg-" + msg_list[key]["type"] + ".py"
    if os.path.isfile(cachefile) and os.access(cachefile, os.R_OK):
        exec(open(cachefile).read())
        print("Read from " + cachefile)
    else:
        document = Document(filename)
        f = open(cachefile, 'w') 

        ies = []
        write_file(f, "ies = []\n")
        table = document.tables[msg_list[key]["table"]]

        start_row = 0
        for row in enumerate(table.rows):
            if start_row == 0:
                start_row = 1;
                continue;
            cells = get_cells(row[1].cells);
            write_cells_to_file("ies", cells)

        msg_list[key]["ies"] = ies
        write_file(f, "msg_list[key][\"ies\"] = ies\n")

        f.close()




tmp = [(k, v["type"]) for k, v in msg_list.items()]
sorted_msg_list = sorted(tmp, key=lambda tup: float(tup[1]))


for (k, v) in sorted_msg_list:
    print("    \"%s\" : %s," % (k, v))


def create_tlv_config(ie: dict) -> str:
    fmt = ie.get("format", "").upper()  # e.g. "TV", "LV-E", etc.

    byte_formats = {
        "T":     (1, 0),
        "V":     (0, 0),
        "TV":    (1, 0),
        "LV":    (0, 1),
        "TLV":   (1, 1),
        "LV-E":  (0, 2),
        "TLV-E": (1, 2),
    }

    tag_b_fmt, len_b_fmt = byte_formats.get(fmt, (1, 1))
    value_b_fmt = -1

    formats_with_IEI = {"T", "TV", "TLV", "TLV-E"}
    iei_present = (fmt in formats_with_IEI)

    formats_with_length = {"V", "TV", "LV", "TLV", "LV-E", "TLV-E"}
    length_present = (fmt in formats_with_length)

    # Build config parts as a list of strings, then join them at the end
    config_parts = []

    # Handle tag part
    iei_str = ie.get("iei", "")
    if iei_present:
        if "-" in iei_str:
            iei_str = iei_str.replace('-', '')
            tag_b_fmt = 0
        iei_hex = f"0x{iei_str}"
        config_parts.append(f"tag = {iei_hex}")
    
    # Always add tag_bytes_format
    config_parts.append(f"tag_bytes_format = {tag_b_fmt}")

    # Handle length part
    length_str = ie.get("length", "")
    if length_present:
        try:
            if length_str == "1/2":
                raw_length = 0
                value_b_fmt = 0
                config_parts.append(f"length = {raw_length}")
            elif "-" in length_str:
                parts = length_str.split("-")
                min_length = int(parts[0])
                
                if iei_present:
                    min_length -= 1
                min_length -= len_b_fmt
                
                config_parts.append(f"min_length = {min_length}")
                
                if parts[1].lower() != "n":
                    max_length = int(parts[1])
                    if iei_present:
                        max_length -= 1
                    max_length -= len_b_fmt
                    config_parts.append(f"max_length = {max_length}")
            else:
                raw_length = int(length_str)
                # Subtract T if IEI is present
                if iei_present:
                    raw_length -= 1
                # Subtract the length bytes themselves
                raw_length -= len_b_fmt
                config_parts.append(f"length = {raw_length}")
        except ValueError:
            pass

    # Always add length_bytes_format
    config_parts.append(f"length_bytes_format = {len_b_fmt}")

    # Add value_bytes_format if needed
    if value_b_fmt == 0:
        config_parts.append(f"value_bytes_format = {value_b_fmt}")

    # Always add format
    config_parts.append(f"format = \"{fmt}\"")

    # Join all parts with commas
    config = "#[tlv_config(" + ", ".join(config_parts) + ")]"
    return config

def create_auto_new_value(value) -> str:
    auto_new_value = f"#[auto_new_value = \"{value}\"]"
    return auto_new_value

f = open(outdir + 'message.rs', 'w')
output_header_to_file(f)

f.write("""
use tlv::prelude::*;
use crate::types::*;
use tlv::tlv_derive::*;
use auto_new_builder::auto_new_builder_derive::AutoNewBuilder;
"""
)

f.write("""

pub const NAS_EXTENDED_PROTOCOL_DISCRIMINATOR_5GSM: u8 = 0x2e;
pub const NAS_EXTENDED_PROTOCOL_DISCRIMINATOR_5GMM: u8 = 0x7e;

""")

for (k, v) in sorted_msg_list:
    f.write("pub const NAS_MESSAGE_TYPE_" + v_upper(k) + ": u8 = " + v.split('.')[0] + ";\n")
f.write("\n")






for (k, v) in sorted_msg_list:
    if "ies" not in msg_list[k]:
        continue;
    if len(msg_list[k]["ies"]) == 0:
        continue;

    f.write("\n/*******************************************************\n")
    f.write(" * %s\n" % k)
    f.write(" ******************************************************/")

    # for i, ie in enumerate([ies for ies in msg_list[k]["ies"] if ies["presence"] != "M"]):
        # f.write("\n#define OGS_NAS_5GS_%s_%s_PRESENT ((uint64_t)1<<%d)" % (v_upper(k), v_upper(ie["value"]), i))

    # for i, ie in enumerate([ies for ies in msg_list[k]["ies"] if ies["presence"] != "M"]):
        # f.write("\n#define OGS_NAS_5GS_%s_%s_TYPE 0x%s" % (v_upper(k), v_upper(ie["value"]), re.sub('-', '0', ie["iei"])))

    # f.write("\n\ntypedef struct ogs_nas_5gs_%s_s {\n" % v_lower(k))
    
    f.write("\n\n#[derive(Debug, TlvEncode, TlvDecode, Clone, AutoNewBuilder)]\n")
    f.write("pub struct Nas%s {\n" % v_camel_case(k))

    mandatory_fields = False
    optional_fields = False
    value_count = {}

    for ie in msg_list[k]["ies"]:
        if ie["presence"] == "M" and mandatory_fields is False:
            f.write("    /* Mandatory fields */\n")
            mandatory_fields = True

        if ie["presence"] != "M" and optional_fields is False:
            f.write("\n    /* Optional fields */\n")
            optional_fields = True

        value = v_lower(ie["value"])
    
        if value in value_count:
            value_count[value] += 1
            value = f"{value}_{value_count[value]}"
        else:
            value_count[value] = 0

        if ie["presence"] == "M":
            if v_camel_case(ie['type']) == "ExtendedProtocolDiscriminator":
                if msg_list[k]["payload_type"] == "gmm":
                    f.write("    " + create_auto_new_value("ExtendedProtocolDiscriminator::gmm()") + "\n")
                elif msg_list[k]["payload_type"] == "gsm":
                    f.write("    " + create_auto_new_value("ExtendedProtocolDiscriminator::gsm()") + "\n")
            elif v_camel_case(ie['type']) == "SpareHalfOctet":
                f.write("    " + create_auto_new_value("SpareHalfOctet::zero()") + "\n")
            elif v_camel_case(ie['type']) == "MessageType":
                f.write("    " + create_auto_new_value("MessageType::" + re.sub(r'^\d+', '', v_lower(k)) + "()") + "\n")

            f.write("    " + create_tlv_config(ie) + "\n")
            f.write(f"    pub nas_{value}: {length_to_type(ie['length'], prefix_if_starts_with_digit(v_camel_case(ie['type'])), ie['format'])},\n\n")

        if ie["presence"] != "M":
            f.write("    " + create_tlv_config(ie) + "\n")
            f.write(f"    pub nas_{value}: Option<{length_to_type(ie['length'], prefix_if_starts_with_digit(v_camel_case(ie['type'])), ie['format'])}>,\n\n")

    f.write("} \n\n")
