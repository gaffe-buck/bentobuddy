
import math
import mathutils
from .presets import skeleton as skel





if True:
    collada = {}
    collada['URI'] ='http://www.collada.org/2005/11/COLLADASchema'
    collada['namespace'] = '{http://www.collada.org/2005/11/COLLADASchema}'

    
    
    version = (0, 0, 0)

    bone_roll = {
    "mHandThumb1Left": 0.7853981852531433,
    "mHandThumb2Left": 0.7853981852531433,
    "mHandThumb3Left": 0.7853981852531433,
    "mHandThumb1Right": -0.7853981852531433,
    "mHandThumb2Right": -0.7853981852531433,
    "mHandThumb3Right": -0.7853981852531433,
    "mHipRight": -0.13089969754219055,
    "mHipLeft": 0.13089969754219055,
    }

    Z90 = mathutils.Matrix.Rotation(math.radians(90.0), 4, 'Z')
    Z90I = Z90.inverted()
    Z180 = mathutils.Matrix.Rotation(math.radians(180.0), 4, 'Z')
    Z180I = Z180.inverted()




    BASE_PRIORITY_MAX = 6
    BASE_PRIORITY_MIN = -1
    BASE_PRIORITY_DEFAULT = 2
    JOINT_PRIORITY_MAX = 6
    JOINT_PRIORITY_MIN = -1
    JOINT_PRIORITY_DEFAULT = 2








    align_bones = {}
    align_bones['first'] = None
    align_bones['last'] = None








if True:
    
    legacy_parents = {}
    legacy_parents['mTorso'] = 'mPelvis'
    legacy_parents['mChest'] = 'mTorso'

    goofy_bones = ('PelvisInv', 'COG', 'Origin', 'Tinker')

    
    
    
    
    
    spine_chain = {
        "mSpine1": "mTorso",
        "mSpine2": "mPelvis",
        "mSpine3": "mChest",
        "mSpine4": "mTorso",
        "mPelvis": "mSpine2",
        "mTorso" : "mSpine1",
        "mChest" : "mSpine3",
        }

    
    
    
    
    
    
    
    
    bone_exceptions = {'Spine', 'Chest', 'Skull'}




if True:

    
    
    
    
    bb_mixer = {}
    bb_mixer['source'] = ""
    
    
    bb_mixer['bone_location_set'] = ""
    bb_mixer['bone_rotation_set'] = ""
    bb_mixer['bone_scale_set'] = ""

    
    
    
    
    
    
    
    
    
    bb_mixer['constraints'] = {}
    for bone in skel.avatar_skeleton:
        bone_type = skel.avatar_skeleton[bone]['type']
        
        
        
        

        
        if 1 == 1:
            bb_mixer['constraints'][bone] = {}
            bb_mixer['constraints'][bone]['location'] = None
            bb_mixer['constraints'][bone]['rotation'] = None
            bb_mixer['constraints'][bone]['scale'] = None
            
            bb_mixer['constraints'][bone]['child_of'] = None





    
    
    
    
    
    bb_paint = {}
    bb_paint['use_frontface'] = False
    bb_paint['use_frontface_falloff'] = False
    bb_paint['falloff_shape'] = 'PROJECTED'
    bb_paint['object'] = None 

    
    
    

    












    bb_alib = {}
    
    
    
    bb_alib['actions'] = {}

    bb_alib['active_action'] = None

    bb_alib['frame_start'] = 1

    bb_alib['count'] = 0




end_bones = {
    'mbones': {
        'mFaceJawShaper', 'mFaceLipUpperLeft', 'mFaceLipUpperRight', 'mHandPinky3Left', 'mFaceChin', 'mFaceEyeLidUpperRight', 'mFaceEyebrowCenterRight', 'mHandRing3Left', 'mHandMiddle3Right', 'mFaceLipCornerRight', 'mWing4FanLeft', 'mHandRing3Right', 'mHandIndex3Right', 'mFaceEyebrowCenterLeft', 'mHandMiddle3Left', 'mFaceLipUpperCenter', 'mFaceCheekLowerRight', 'mFaceLipCornerLeft', 'mFaceForeheadRight', 'mFaceEyeLidUpperLeft', 'mFaceEyecornerInnerLeft', 'mFaceEyebrowOuterRight', 'mFaceNoseBridge', 'mToeLeft', 'mFaceEar2Left', 'mFaceEyeLidLowerRight', 'mFaceNoseRight', 'mFaceForeheadLeft', 'mFaceForeheadCenter', 'mWing4FanRight', 'mFaceEyebrowOuterLeft', 'mHandPinky3Right', 'mFaceEyecornerInnerRight', 'mFaceCheekUpperLeft', 'mFaceEyebrowInnerLeft', 'mFaceLipLowerRight', 'mFaceEyebrowInnerRight', 'mToeRight', 'mFaceLipLowerLeft', 'mHandIndex3Left', 'mFaceLipLowerCenter', 'mFaceNoseLeft', 'mFaceCheekLowerLeft', 'mFaceCheekUpperRight', 'mFaceNoseCenter', 'mFaceEyeLidLowerLeft', 'mFaceNoseBase', 'mHandThumb3Right', 'mFaceEar2Right', 'mHandThumb3Left', 'mSkull',
        },
    'attach': {
        'Left Shoulder', 'R Lower Leg', 'Right Pec', 'Neck', 'Left Pec', 'Chest', 'Pelvis', 'L Forearm', 'Stomach', 'Alt Left Eye', 'Left Eyeball', 'Mouth', 'Jaw', 'Left Ring Finger', 'Right Foot', 'Left Ear', 'Alt Left Ear', 'Spine', 'Left Hip', 'Avatar Center', 'Right Shoulder', 'Right Hand', 'Left Wing', 'Right Hind Foot', 'Alt Right Ear', 'Right Ring Finger', 'Right Wing', 'R Upper Leg', 'L Lower Leg', 'L Upper Arm', 'R Upper Arm', 'Skull', 'Left Hind Foot', 'L Upper Leg', 'Right Ear', 'Right Hip', 'Alt Right Eye', 'Chin', 'Nose', 'Left Hand', 'Right Eyeball', 'Left Foot', 'Tail Tip', 'Tail Base', 'Groin', 'R Forearm', 'Tongue',
        },
    'volume': {
        'BUTT', 'UPPER_BACK', 'L_CLAVICLE', 'R_HAND', 'HEAD', 'LOWER_BACK', 'LEFT_PEC', 'R_UPPER_ARM', 'PELVIS', 'RIGHT_HANDLE', 'R_LOWER_LEG', 'L_LOWER_LEG', 'L_FOOT','R_UPPER_LEG', 'L_LOWER_ARM', 'R_CLAVICLE', 'L_UPPER_LEG', 'LEFT_HANDLE', 'NECK', 'RIGHT_PEC', 'R_LOWER_ARM', 'CHEST', 'BELLY', 'L_HAND', 'R_FOOT', 'L_UPPER_ARM',
        },
    }















