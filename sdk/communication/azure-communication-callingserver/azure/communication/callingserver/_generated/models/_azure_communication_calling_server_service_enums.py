# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AudioRoutingMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The audio routing mode.
    """

    ONE_TO_ONE = "oneToOne"
    MULTICAST = "multicast"

class CallConnectionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the call connection.
    """

    CONNECTING = "connecting"
    CONNECTED = "connected"
    TRANSFERRING = "transferring"
    TRANSFER_ACCEPTED = "transferAccepted"
    DISCONNECTING = "disconnecting"
    DISCONNECTED = "disconnected"

class CallLocatorKindModel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The call locator kind.
    """

    GROUP_CALL_LOCATOR = "groupCallLocator"
    SERVER_CALL_LOCATOR = "serverCallLocator"

class CallRecordingState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the recording
    """

    ACTIVE = "active"
    INACTIVE = "inactive"

class CallRejectReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rejection reason.
    """

    NONE = "none"
    BUSY = "busy"
    FORBIDDEN = "forbidden"

class CommunicationCloudEnvironmentModel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The cloud that the identifier belongs to.
    """

    PUBLIC = "public"
    DOD = "dod"
    GCCH = "gcch"

class Enum0(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ONE_TO_ONE = "oneToOne"
    MULTICAST = "multicast"

class Enum2(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ONE_TO_ONE = "oneToOne"
    MULTICAST = "multicast"

class Enum3(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ONE_TO_ONE = "oneToOne"
    MULTICAST = "multicast"

class EventSubscriptionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PARTICIPANTS_UPDATED = "participantsUpdated"
    DTMF_RECEIVED = "dtmfReceived"

class MediaType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUDIO = "audio"
    VIDEO = "video"

class OperationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the operation
    """

    NOT_STARTED = "notStarted"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class RecordingChannelType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Channel type of call recording.
    """

    MIXED = "mixed"
    UNMIXED = "unmixed"

class RecordingContentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Content type of call recording.
    """

    AUDIO = "audio"
    AUDIO_VIDEO = "audioVideo"

class RecordingFormatType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Format type of call recording.
    """

    WAV = "wav"
    MP3 = "mp3"
    MP4 = "mp4"

class ToneValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The tone value.
    """

    TONE0 = "tone0"
    TONE1 = "tone1"
    TONE2 = "tone2"
    TONE3 = "tone3"
    TONE4 = "tone4"
    TONE5 = "tone5"
    TONE6 = "tone6"
    TONE7 = "tone7"
    TONE8 = "tone8"
    TONE9 = "tone9"
    STAR = "star"
    POUND = "pound"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    FLASH = "flash"