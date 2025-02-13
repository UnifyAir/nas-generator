ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "Security header type", "type" : "Security header type", "reference" : "9.3", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Spare half octet", "type" : "Spare half octet", "reference" : "9.5", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Security mode complete message identity", "type" : "Message type", "reference" : "9.6", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "77", "value" : "IMEISV", "type" : "5GS mobile identity", "reference" : "9.11.3.4", "presence" : "O", "format" : "TLV-E", "length" : "12"})
ies.append({ "iei" : "71", "value" : "NAS message container", "type" : "message container", "reference" : "9.11.3.33", "presence" : "O", "format" : "TLV-E", "length" : "4-n"})
ies.append({ "iei" : "78", "value" : "non-IMEISV PEI", "type" : "5GS mobile identity", "reference" : "9.11.3.4", "presence" : "O", "format" : "TLV-E", "length" : "7-n"})
msg_list[key]["ies"] = ies
