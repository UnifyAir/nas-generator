/*
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

/*******************************************************************************
 * This file had been created by rust-nas-message.py script v0.2.0
 * Please do not modify this file but regenerate it via script.
 * Created on: 2025-03-09 19:42:50.698547 by nr
 * from 24501-h90.docx
 ******************************************************************************/


use bitfield::bitfield;
use tlv::prelude::*;
use tlv_derive::{TlvDecode, TlvEncode};
use derive_more::{Into, From};


// ******************************************************************
// ExtendedProtocolDiscriminator
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ExtendedProtocolDiscriminator(u8);


// ******************************************************************
// SecurityHeaderType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SecurityHeaderType(u8);


// ******************************************************************
// SpareHalfOctet
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SpareHalfOctet(u8);


// ******************************************************************
// MessageType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MessageType(u8);


// ******************************************************************
// FivegsRegistrationType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsRegistrationType(u8);


// ******************************************************************
// KeySetIdentifier
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct KeySetIdentifier(u8);


// ******************************************************************
// FivegsMobileIdentity
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsMobileIdentity(Vec<u8>);


// ******************************************************************
// FivegmmCapability
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegmmCapability(Vec<u8>);


// ******************************************************************
// UeSecurityCapability
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeSecurityCapability(Vec<u8>);


// ******************************************************************
// Nssai
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Nssai(Vec<u8>);


// ******************************************************************
// FivegsTrackingAreaIdentity
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsTrackingAreaIdentity(Vec<u8>);


// ******************************************************************
// S1UeNetworkCapability
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct S1UeNetworkCapability(Vec<u8>);


// ******************************************************************
// UplinkDataStatus
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UplinkDataStatus(Vec<u8>);


// ******************************************************************
// PduSessionStatus
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionStatus(Vec<u8>);


// ******************************************************************
// MicoIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MicoIndication(u8);


// ******************************************************************
// UeStatus
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeStatus(u8);


// ******************************************************************
// AllowedPduSessionStatus
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AllowedPduSessionStatus(Vec<u8>);


// ******************************************************************
// UeUsageSetting
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeUsageSetting(u8);


// ******************************************************************
// FivegsDrxParameters
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsDrxParameters(u8);


// ******************************************************************
// EpsNasMessageContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct EpsNasMessageContainer(Vec<u8>);


// ******************************************************************
// LadnIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct LadnIndication(Vec<u8>);


// ******************************************************************
// PayloadContainerType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PayloadContainerType(u8);


// ******************************************************************
// PayloadContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PayloadContainer(Vec<u8>);


// ******************************************************************
// NetworkSlicingIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct NetworkSlicingIndication(u8);


// ******************************************************************
// FivegsUpdateType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsUpdateType(u8);


// ******************************************************************
// MobileStationClassmark2
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MobileStationClassmark2(Vec<u8>);


// ******************************************************************
// SupportedCodecList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SupportedCodecList(Vec<u8>);


// ******************************************************************
// MessageContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MessageContainer(Vec<u8>);


// ******************************************************************
// EpsBearerContextStatus
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct EpsBearerContextStatus(Vec<u8>);


// ******************************************************************
// ExtendedDrxParameters
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ExtendedDrxParameters(Vec<u8>);


// ******************************************************************
// GprsTimer3
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct GprsTimer3(u8);


// ******************************************************************
// UeRadioCapabilityId
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeRadioCapabilityId(Vec<u8>);


// ******************************************************************
// MappedNssai
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MappedNssai(Vec<u8>);


// ******************************************************************
// AdditionalInformationRequested
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AdditionalInformationRequested(u8);


// ******************************************************************
// WusAssistanceInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct WusAssistanceInformation(Vec<u8>);


// ******************************************************************
// N5gcIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct N5gcIndication(u8);


// ******************************************************************
// NbN1ModeDrxParameters
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct NbN1ModeDrxParameters(u8);


// ******************************************************************
// UeRequestType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeRequestType(u8);


// ******************************************************************
// PagingRestriction
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PagingRestriction(Vec<u8>);


// ******************************************************************
// ServiceLevelAaContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ServiceLevelAaContainer(Vec<u8>);


// ******************************************************************
// Nid
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Nid(Vec<u8>);


// ******************************************************************
// PlmnIdentity
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PlmnIdentity(Vec<u8>);


// ******************************************************************
// PeipsAssistanceInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PeipsAssistanceInformation(Vec<u8>);


// ******************************************************************
// FivegsRegistrationResult
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsRegistrationResult(u8);


// ******************************************************************
// PlmnList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PlmnList(Vec<u8>);


// ******************************************************************
// FivegsTrackingAreaIdentityList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsTrackingAreaIdentityList(Vec<u8>);


// ******************************************************************
// RejectedNssai
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct RejectedNssai(Vec<u8>);


// ******************************************************************
// FivegsNetworkFeatureSupport
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsNetworkFeatureSupport(Vec<u8>);


// ******************************************************************
// PduSessionReactivationResult
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionReactivationResult(Vec<u8>);


// ******************************************************************
// PduSessionReactivationResultErrorCause
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionReactivationResultErrorCause(Vec<u8>);


// ******************************************************************
// LadnInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct LadnInformation(Vec<u8>);


// ******************************************************************
// ServiceAreaList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ServiceAreaList(Vec<u8>);


// ******************************************************************
// GprsTimer2
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct GprsTimer2(u8);


// ******************************************************************
// EmergencyNumberList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct EmergencyNumberList(Vec<u8>);


// ******************************************************************
// ExtendedEmergencyNumberList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ExtendedEmergencyNumberList(Vec<u8>);


// ******************************************************************
// SorTransparentContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SorTransparentContainer(Vec<u8>);


// ******************************************************************
// EapMessage
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct EapMessage(Vec<u8>);


// ******************************************************************
// NssaiInclusionMode
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct NssaiInclusionMode(u8);


// ******************************************************************
// OperatorDefinedAccessCategoryDefinitions
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct OperatorDefinedAccessCategoryDefinitions(Vec<u8>);


// ******************************************************************
// Non3gppNwProvidedPolicies
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Non3gppNwProvidedPolicies(u8);


// ******************************************************************
// UeRadioCapabilityIdDeletionIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeRadioCapabilityIdDeletionIndication(u8);


// ******************************************************************
// CipheringKeyData
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct CipheringKeyData(Vec<u8>);


// ******************************************************************
// CagInformationList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct CagInformationList(Vec<u8>);


// ******************************************************************
// Truncated5gSTmsiConfiguration
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Truncated5gSTmsiConfiguration(u8);


// ******************************************************************
// ExtendedRejectedNssai
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ExtendedRejectedNssai(Vec<u8>);


// ******************************************************************
// FivegsAdditionalRequestResult
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsAdditionalRequestResult(u8);


// ******************************************************************
// NssrgInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct NssrgInformation(Vec<u8>);


// ******************************************************************
// RegistrationWaitRange
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct RegistrationWaitRange(Vec<u8>);


// ******************************************************************
// ListOfPlmnsToBeUsedInDisasterCondition
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ListOfPlmnsToBeUsedInDisasterCondition(Vec<u8>);


// ******************************************************************
// ExtendedCagInformationList
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ExtendedCagInformationList(Vec<u8>);


// ******************************************************************
// NsagInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct NsagInformation(Vec<u8>);


// ******************************************************************
// FivegmmCause
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegmmCause(u8);


// ******************************************************************
// DeRegistrationType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct DeRegistrationType(u8);


// ******************************************************************
// ServiceType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ServiceType(u8);


// ******************************************************************
// ConfigurationUpdateIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ConfigurationUpdateIndication(u8);


// ******************************************************************
// NetworkName
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct NetworkName(Vec<u8>);


// ******************************************************************
// TimeZone
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct TimeZone(u8);


// ******************************************************************
// TimeZoneAndTime
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct TimeZoneAndTime(Vec<u8>);


// ******************************************************************
// DaylightSavingTime
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct DaylightSavingTime(u8);


// ******************************************************************
// SmsIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SmsIndication(u8);


// ******************************************************************
// AdditionalConfigurationIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AdditionalConfigurationIndication(u8);


// ******************************************************************
// PriorityIndicator
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PriorityIndicator(u8);


// ******************************************************************
// Abba
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Abba(Vec<u8>);


// ******************************************************************
// AuthenticationParameterRand
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AuthenticationParameterRand(Vec<u8>);


// ******************************************************************
// AuthenticationParameterAutn
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AuthenticationParameterAutn(Vec<u8>);


// ******************************************************************
// AuthenticationResponseParameter
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AuthenticationResponseParameter(Vec<u8>);


// ******************************************************************
// AuthenticationFailureParameter
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AuthenticationFailureParameter(Vec<u8>);


// ******************************************************************
// FivegsIdentityType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsIdentityType(u8);


// ******************************************************************
// SecurityAlgorithms
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SecurityAlgorithms(u8);


// ******************************************************************
// ImeisvRequest
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ImeisvRequest(u8);


// ******************************************************************
// EpsNasSecurityAlgorithms
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct EpsNasSecurityAlgorithms(u8);


// ******************************************************************
// Additional5gSecurityInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Additional5gSecurityInformation(u8);


// ******************************************************************
// S1UeSecurityCapability
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct S1UeSecurityCapability(Vec<u8>);


// ******************************************************************
// AccessType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AccessType(u8);


// ******************************************************************
// PduSessionIdentity2
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionIdentity2(u8);


// ******************************************************************
// RequestType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct RequestType(u8);


// ******************************************************************
// SNssai
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SNssai(Vec<u8>);


// ******************************************************************
// Dnn
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Dnn(Vec<u8>);


// ******************************************************************
// AdditionalInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AdditionalInformation(Vec<u8>);


// ******************************************************************
// MaPduSessionInformation
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MaPduSessionInformation(u8);


// ******************************************************************
// ReleaseAssistanceIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ReleaseAssistanceIndication(u8);


// ******************************************************************
// PduSessionIdentity
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionIdentity(u8);


// ******************************************************************
// ProcedureTransactionIdentity
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ProcedureTransactionIdentity(u8);


// ******************************************************************
// IntegrityProtectionMaximumDataRate
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct IntegrityProtectionMaximumDataRate(Vec<u8>);


// ******************************************************************
// PduSessionType
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionType(u8);


// ******************************************************************
// SscMode
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SscMode(u8);


// ******************************************************************
// FivegsmCapability
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsmCapability(Vec<u8>);


// ******************************************************************
// MaximumNumberOfSupportedPacketFilters
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MaximumNumberOfSupportedPacketFilters(Vec<u8>);


// ******************************************************************
// AlwaysOnPduSessionRequested
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AlwaysOnPduSessionRequested(u8);


// ******************************************************************
// SmPduDnRequestContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SmPduDnRequestContainer(Vec<u8>);


// ******************************************************************
// ExtendedProtocolConfigurationOptions
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ExtendedProtocolConfigurationOptions(Vec<u8>);


// ******************************************************************
// IpHeaderCompressionConfiguration
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct IpHeaderCompressionConfiguration(Vec<u8>);


// ******************************************************************
// DsTtEthernetPortMacAddress
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct DsTtEthernetPortMacAddress(Vec<u8>);


// ******************************************************************
// UeDsTtResidenceTime
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct UeDsTtResidenceTime(Vec<u8>);


// ******************************************************************
// PortManagementInformationContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PortManagementInformationContainer(Vec<u8>);


// ******************************************************************
// EthernetHeaderCompressionConfiguration
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct EthernetHeaderCompressionConfiguration(u8);


// ******************************************************************
// PduAddress
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduAddress(Vec<u8>);


// ******************************************************************
// RequestedMbsContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct RequestedMbsContainer(Vec<u8>);


// ******************************************************************
// PduSessionPairId
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct PduSessionPairId(u8);


// ******************************************************************
// Rsn
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct Rsn(u8);


// ******************************************************************
// QosRules
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct QosRules(Vec<u8>);


// ******************************************************************
// SessionAmbr
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct SessionAmbr(Vec<u8>);


// ******************************************************************
// FivegsmCause
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsmCause(u8);


// ******************************************************************
// GprsTimer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct GprsTimer(u8);


// ******************************************************************
// AlwaysOnPduSessionIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AlwaysOnPduSessionIndication(u8);


// ******************************************************************
// MappedEpsBearerContexts
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct MappedEpsBearerContexts(Vec<u8>);


// ******************************************************************
// QosFlowDescriptions
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct QosFlowDescriptions(Vec<u8>);


// ******************************************************************
// FivegsmNetworkFeatureSupport
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsmNetworkFeatureSupport(Vec<u8>);


// ******************************************************************
// ServingPlmnRateControl
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ServingPlmnRateControl(Vec<u8>);


// ******************************************************************
// AtsssContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AtsssContainer(Vec<u8>);


// ******************************************************************
// ControlPlaneOnlyIndication
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ControlPlaneOnlyIndication(u8);


// ******************************************************************
// ReceivedMbsContainer
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ReceivedMbsContainer(Vec<u8>);


// ******************************************************************
// AllowedSscMode
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct AllowedSscMode(u8);


// ******************************************************************
// FivegsmCongestionReAttemptIndicator
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct FivegsmCongestionReAttemptIndicator(u8);


// ******************************************************************
// ReAttemptIndicator
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct ReAttemptIndicator(u8);


// ******************************************************************
// HeaderCompressionConfiguration
// ******************************************************************

// Auto-generated
#[derive(Debug, TlvEncode, TlvDecode, Into, From, Clone)]
pub struct HeaderCompressionConfiguration(Vec<u8>);
