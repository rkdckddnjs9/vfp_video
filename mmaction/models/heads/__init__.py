# Copyright (c) OpenMMLab. All rights reserved.
from .base import BaseHead
from .base_multi_task import BaseHead_MultiTask
from .feature_head import FeatureHead
from .gcn_head import GCNHead
from .i3d_head import I3DHead
from .i3d_head_multi_task import I3DHead_MultiTask
from .mvit_head import MViTHead
from .omni_head import OmniHead
from .rgbpose_head import RGBPoseHead
from .slowfast_head import SlowFastHead
from .timesformer_head import TimeSformerHead
from .timesformer_head_multi_task import TimeSformerHead_MultiTask
from .tpn_head import TPNHead
from .trn_head import TRNHead
from .tsm_head import TSMHead
from .tsn_audio_head import TSNAudioHead
from .tsn_head import TSNHead
from .uniformer_head import UniFormerHead
from .uniformer_head_multi_task import UniFormerHead_MultiTask
from .x3d_head import X3DHead

__all__ = [
    'BaseHead', 'BaseHead_MultiTask', 'GCNHead', 'I3DHead', 'I3DHead_MultiTask', 'MViTHead', 'OmniHead', 'SlowFastHead',
    'TPNHead', 'TRNHead', 'TSMHead', 'TSNAudioHead', 'TSNHead',
    'TimeSformerHead', 'TimeSformerHead_MultiTask', 'UniFormerHead', 'UniFormerHead_MultiTask', 'RGBPoseHead', 'X3DHead', 'FeatureHead'
]
