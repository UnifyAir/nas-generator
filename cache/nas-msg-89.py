ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "Security header type", "type" : "Security header type", "reference" : "9.3", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Spare half octet", "type" : "Spare half octet", "reference" : "9.5", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Authentication failure message identity", "type" : "Message type", "reference" : "9.7", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "5GMM cause", "type" : "5GMM cause", "reference" : "9.11.3.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "30", "value" : "Authentication failure parameter", "type" : "Authentication failure parameter", "reference" : "9.11.3.14", "presence" : "O", "format" : "TLV", "length" : "16"})
msg_list[key]["ies"] = ies
