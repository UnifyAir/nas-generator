ies = []
ies.append({ "iei" : "", "value" : "Extended protocol discriminator", "type" : "Extended protocol discriminator", "reference" : "9.2", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PDU session ID", "type" : "PDU session identity", "reference" : "9.4", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PTI", "type" : "Procedure transaction identity", "reference" : "9.6", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "", "value" : "PDU SESSION MODIFICATION COMMAND message identity", "type" : "Message type", "reference" : "9.7", "presence" : "M", "format" : "V", "length" : "1"})
ies.append({ "iei" : "59", "value" : "5GSM cause", "type" : "5GSM cause", "reference" : "9.11.4.2", "presence" : "O", "format" : "TV", "length" : "2"})
ies.append({ "iei" : "2A", "value" : "Session AMBR", "type" : "Session-AMBR", "reference" : "9.11.4.14", "presence" : "O", "format" : "TLV", "length" : "8"})
ies.append({ "iei" : "56", "value" : "RQ timer value", "type" : "GPRS timer", "reference" : "9.11.2.3", "presence" : "O", "format" : "TV", "length" : "2"})
ies.append({ "iei" : "8-", "value" : "Always-on PDU session indication", "type" : "Always-on PDU session indication", "reference" : "9.11.4.3", "presence" : "O", "format" : "TV", "length" : "1"})
ies.append({ "iei" : "7A", "value" : "Authorized QoS rules", "type" : "QoS rules", "reference" : "9.11.4.13", "presence" : "O", "format" : "TLV-E", "length" : "7-65538"})
ies.append({ "iei" : "75", "value" : "Mapped EPS bearer contexts", "type" : "Mapped EPS bearer contexts", "reference" : "9.11.4.8", "presence" : "O", "format" : "TLV-E", "length" : "7-65538"})
ies.append({ "iei" : "79", "value" : "Authorized QoS flow descriptions", "type" : "QoS flow descriptions", "reference" : "9.11.4.12", "presence" : "O", "format" : "TLV-E", "length" : "6-65538"})
ies.append({ "iei" : "7B", "value" : "Extended protocol configuration options", "type" : "Extended protocol configuration options", "reference" : "9.11.4.6", "presence" : "O", "format" : "TLV-E", "length" : "4-65538"})
ies.append({ "iei" : "77", "value" : "ATSSS container", "type" : "ATSSS container", "reference" : "9.11.4.22", "presence" : "O", "format" : "TLV-E", "length" : "3-65538"})
ies.append({ "iei" : "66", "value" : "IP header compression configuration", "type" : "IP header compression configuration", "reference" : "9.11.4.24", "presence" : "O", "format" : "TLV", "length" : "5-257"})
ies.append({ "iei" : "74", "value" : "Port management information container", "type" : "Port management information container", "reference" : "9.11.4.27", "presence" : "O", "format" : "TLV-E", "length" : "4-65538"})
ies.append({ "iei" : "1E", "value" : "Serving PLMN rate control", "type" : "Serving PLMN rate control", "reference" : "9.11.4.20", "presence" : "O", "format" : "TLV", "length" : "4"})
ies.append({ "iei" : "1F", "value" : "Ethernet header compression configuration", "type" : "Ethernet header compression configuration", "reference" : "9.11.4.28", "presence" : "O", "format" : "TLV", "length" : "3"})
ies.append({ "iei" : "71", "value" : "Received MBS container", "type" : "Received MBS container", "reference" : "9.11.4.31", "presence" : "O", "format" : "TLV-E", "length" : "9-65538"})
ies.append({ "iei" : "72", "value" : "Service-level-AA container", "type" : "Service-level-AA container", "reference" : "9.11.2.10", "presence" : "O", "format" : "TLV-E", "length" : "6-n"})
msg_list[key]["ies"] = ies
