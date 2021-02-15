# -*- coding: utf-8 -*-
from gi.repository import Gst


class WebRTCDTLSSetup:
    """"""
    NONE = 0
    ACTPASS = 1
    ACTIVE = 2
    PASSIVE = 3


class WebRTCDTLSTransportState:
    """"""
    NEW = 0
    CLOSED = 1
    FAILED = 2
    CONNECTING = 3
    CONNECTED = 4


class WebRTCFECType:
    """"""
    NONE = 0
    ULP_RED = 1


class WebRTCICEComponent:
    """"""
    RTP = 0
    RTCP = 1


class WebRTCICEConnectionState:
    """"""
    NEW = 0
    CHECKING = 1
    CONNECTED = 2
    COMPLETED = 3
    FAILED = 4
    DISCONNECTED = 5
    CLOSED = 6


class WebRTCICEGatheringState:
    """"""
    NEW = 0
    GATHERING = 1
    COMPLETE = 2


class WebRTCICERole:
    """"""
    CONTROLLED = 0
    CONTROLLING = 1


class WebRTCPeerConnectionState:
    """"""
    NEW = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTED = 3
    FAILED = 4
    CLOSED = 5


class WebRTCRTPTransceiverDirection:
    """"""
    NONE = 0
    INACTIVE = 1
    SENDONLY = 2
    RECVONLY = 3
    SENDRECV = 4


class WebRTCSDPType:
    """"""
    OFFER = 1
    PRANSWER = 2
    ANSWER = 3
    ROLLBACK = 4


class WebRTCSignalingState:
    """"""
    STABLE = 0
    CLOSED = 1
    HAVE_LOCAL_OFFER = 2
    HAVE_REMOTE_OFFER = 3
    HAVE_LOCAL_PRANSWER = 4
    HAVE_REMOTE_PRANSWER = 5


class WebRTCStatsType:
    """"""
    CODEC = 1
    INBOUND_RTP = 2
    OUTBOUND_RTP = 3
    REMOTE_INBOUND_RTP = 4
    REMOTE_OUTBOUND_RTP = 5
    CSRC = 6
    PEER_CONNECTION = 7
    DATA_CHANNEL = 8
    STREAM = 9
    TRANSPORT = 10
    CANDIDATE_PAIR = 11
    LOCAL_CANDIDATE = 12
    REMOTE_CANDIDATE = 13
    CERTIFICATE = 14

def webrtc_sdp_type_to_string(type=None):
    """"""
    return object


class WebRTCDTLSTransport(Gst.Object):
    """"""
    
    def __init__(self, session_id=None, rtcp=None):
        """"""
        return object
    @staticmethod
    def new(session_id=None, rtcp=None):
        """"""
        return object
    
    def set_transport(self, ice=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def transport(self):
        return object

    @property
    def state(self):
        return object

    @property
    def is_rtcp(self):
        return object

    @property
    def client(self):
        return object

    @property
    def session_id(self):
        return object

    @property
    def dtlssrtpenc(self):
        return object

    @property
    def dtlssrtpdec(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCDTLSTransportClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCICETransport(Gst.Object):
    """"""
    
    def gather_candidates(self):
        """"""
        return object
    
    def connection_state_change(self, new_state=None):
        """"""
        return object
    
    def gathering_state_change(self, new_state=None):
        """"""
        return object
    
    def new_candidate(self, stream_id=None, component=None, attr=None):
        """"""
        return object
    
    def selected_pair_change(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def role(self):
        return object

    @property
    def component(self):
        return object

    @property
    def state(self):
        return object

    @property
    def gathering_state(self):
        return object

    @property
    def src(self):
        return object

    @property
    def sink(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCICETransportClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def gather_candidates(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCRTPReceiver(Gst.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def set_rtcp_transport(self, transport=None):
        """"""
        return object
    
    def set_transport(self, transport=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def transport(self):
        return object

    @property
    def rtcp_transport(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCRTPReceiverClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCRTPSender(Gst.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def set_rtcp_transport(self, transport=None):
        """"""
        return object
    
    def set_transport(self, transport=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def transport(self):
        return object

    @property
    def rtcp_transport(self):
        return object

    @property
    def send_encodings(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCRTPSenderClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCRTPTransceiver(Gst.Object):
    """"""

    @property
    def parent(self):
        return object

    @property
    def mline(self):
        return object

    @property
    def mid(self):
        return object

    @property
    def stopped(self):
        return object

    @property
    def sender(self):
        return object

    @property
    def receiver(self):
        return object

    @property
    def direction(self):
        return object

    @property
    def current_direction(self):
        return object

    @property
    def codec_preferences(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCRTPTransceiverClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class WebRTCSessionDescription():
    """"""
    
    def __init__(self, type=None, sdp=None):
        """"""
        return object
    @staticmethod
    def new(type=None, sdp=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object

    @property
    def type(self):
        return object

    @property
    def sdp(self):
        return object
