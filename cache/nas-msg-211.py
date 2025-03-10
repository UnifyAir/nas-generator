ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PDU session ID", "type" : "PDU session identity", "reference" : "9.4", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PTI", "type" : "Procedure transaction identity", "reference" : "9.6", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PDU SESSION RELEASE COMMAND message identity", "type" : "Message type", "reference" : "9.7", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "5GSM cause", "type" : "5GSM cause", "reference" : "9.11.4.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "37", "value" : "Back-off timer value", "type" : "GPRS timer 3", "reference" : "9.11.2.5", "presence" : "O", "format" : "TLV", "length" : "3"})
ies.append({ "iei" : "78", "value" : "EAP message", "type" : "EAP message", "reference" : "9.11.2.2", "presence" : "O", "format" : "TLV-E", "length" : "7-1503"})
ies.append({ "iei" : "61", "value" : "5GSM congestion re-attempt indicator", "type" : "5GSM congestion re-attempt indicator", "reference" : "9.11.4.21", "presence" : "O", "format" : "TLV", "length" : "3"})
ies.append({ "iei" : "7B", "value" : "Extended protocol configuration options", "type" : "Extended protocol configuration options", "reference" : "9.11.4.6", "presence" : "O", "format" : "TLV-E", "length" : "4-65538"})
ies.append({ "iei" : "D-", "value" : "Access type", "type" : "Access type", "reference" : "9.11.2.1A", "presence" : "O", "format" : "TV", "length" : "1"})
ies.append({ "iei" : "72", "value" : "Service-level-AA container", "type" : "Service-level-AA container", "reference" : "9.11.2.10", "presence" : "O", "format" : "TLV-E", "length" : "6-n"})
msg_list[key]["ies"] = ies
