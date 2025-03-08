# The MIT License

# Copyright (C) 2024-2025 by UnifyAir Inc. <team@unifyair.com>

# This file is part of Open5GS.

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
    f.write("""/*
 * The MIT License
 *
 * Copyright (C) 2019-2023 by UnifyAir Inc. <info@unifyair.com>
 *
 * This file is part of UnifyAir Core.
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

""")
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
        return digit_words[text[0]] + text[1:]
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

    iei_str = ie.get("iei", "")
    tag_part = ""
    if iei_present:
        iei_hex = f"0x{iei_str}"
        tag_part = f"tag = {iei_hex}, "

    length_str = ie.get("length", "")
    length_part = ""

    if length_present:
        try:
            if length_str == "1/2":
                raw_length = 0
                value_b_fmt = 0
            else:
                raw_length = int(length_str)
                # Subtract T if IEI is present
                if iei_present:
                    raw_length -= 1
                # Subtract the length bytes themselves
                raw_length -= len_b_fmt

            length_part = f", length = {raw_length}"
        except ValueError:
            pass

    # These are two exceptional cases for 1/2 V and 1/2 + 1/2 TV
    value_byte_format = ""
    if value_b_fmt == 0:
        value_byte_format = f"value_bytes_format = {value_b_fmt}, "   


    if "-" in tag_part:
        tag_part = tag_part.replace('-', '')
        tag_b_fmt = 0

    config = (
        f"#[tlv_config("
        f"{tag_part}"
        f"tag_bytes_format = {tag_b_fmt}"
        f"{length_part}, "
        f"length_bytes_format = {len_b_fmt}, "
        f"{value_byte_format}"
        f"format = \"{fmt}\""
        f")]"
    )

    return config


f = open(outdir + 'message.rs', 'w')
output_header_to_file(f)

f.write("""
use tlv::prelude::*;
use crate::types::*;
use tlv_derive::{TlvDecode, TlvEncode};
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
    
    f.write("\n\n#[derive(Debug, TlvEncode, TlvDecode)]\n")
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
            f.write("    " + create_tlv_config(ie) + "\n")
            f.write(f"    nas_{value}: {length_to_type(ie['length'], prefix_if_starts_with_digit(v_camel_case(ie['type'])), ie['format'])},\n\n")

        if ie["presence"] != "M":
            f.write("    " + create_tlv_config(ie) + "\n")
            f.write(f"    nas_{value}: Option<{length_to_type(ie['length'], prefix_if_starts_with_digit(v_camel_case(ie['type'])), ie['format'])}>,\n\n")

    f.write("} \n\n")
