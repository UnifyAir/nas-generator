ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "Security header type", "type" : "Security header type", "reference" : "9.3", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Spare half octet", "type" : "Spare half octet", "reference" : "9.5", "presence" : "M", "format" : "V", "length" : "1/2"})
ies.append({ "iei" : "", "value" : "Security mode reject message identity", "type" : "Message type", "reference" : "9.6", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "5GMM cause", "type" : "5GMM cause", "reference" : "9.11.3.2", "presence" : "M", "format" : "V", "length" : "1"})
msg_list[key]["ies"] = ies
