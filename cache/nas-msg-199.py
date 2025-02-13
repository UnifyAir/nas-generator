ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PDU session ID", "type" : "PDU session identity", "reference" : "9.4", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PTI", "type" : "Procedure transaction identity", "reference" : "9.6", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PDU SESSION AUTHENTICATION RESULT message identity", "type" : "Message type", "reference" : "9.7", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "78", "value" : "EAP message", "type" : "EAP message", "reference" : "9.11.2.2", "presence" : "O", "format" : "TLV-E", "length" : "7-1503"})
ies.append({ "iei" : "7B", "value" : "Extended protocol configuration options", "type" : "Extended protocol configuration options", "reference" : "9.11.4.6", "presence" : "O", "format" : "TLV-E", "length" : "4-65538"})
msg_list[key]["ies"] = ies
