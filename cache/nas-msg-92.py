ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "Security header type", "type" : "Security header type", "reference" : "9.3", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Spare half octet", "type" : "Spare half octet", "reference" : "9.5", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Identity response message identity", "type" : "Message type", "reference" : "9.7", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "Mobile identity", "type" : "5GS mobile identity", "reference" : "9.11.3.4", "presence" : "M", "format" : "LV-E", "length" : "3-n"})
msg_list[key]["ies"] = ies
