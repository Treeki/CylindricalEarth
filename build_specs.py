import bcsv
import json
import os
import sys

print('from bcsv import *')
print()

preset_names = {
	0x00244ce4: 'BeforeDays u8',
	0x0110b14c: 'MaxValue u16',
	0x0207a2af: 'SpNpcID u16',
	0x03200971: 'RainHat u16',
	0x0329d696: 'BonusFive u8',
	0x0424930f: 'UseExteriorLight u8',
	0x04a47035: 'NumberingId u16',
	0x04ac1bea: 'SpecialELink u8',
	0x06012035: 'CanGift u8',
	0x062ec6cf: 'WeatherPattern string32',
	0x0732bb98: 'CanNpcPresent u8',
	0x086f5f3a: 'LocalizeTexture u8',
	0x0909f3d4: 'Property u8',
	0x09b714f9: 'AnimeTypeWateringCan string64',
	0x09d75f40: 'IsUseXlink u8',
	0x0b52f5bb: 'FloorType u16',
	0x0b6d59d2: 'Size s8',
	0x0c98243c: 'AnimeTypeDrink string64',
	0x0eb7fa40: 'ToiletType u8',
	0x0f230d34: 'SilhouettePosX f32',
	0x0f30a50e: 'MusicNo u16',
	0x0f640691: 'PosterItemID s16',
	0x0f9f6747: 'WallTableId u16',
	0x110a7053: 'MessageLabel u16',
	0x127ccfd9: 'Reward u16',
	0x128a3d9b: 'ItemCategoryGroup u32',
	0x137dd804: 'AppearArea u8',
	0x147e658d: 'FrontSwitch u8',
	0x158a4c61: 'DemoDistance f32',
	0x1abe6e96: 'SelectSecond u16',
	0x1b53db71: 'WatchPosY f32',
	0x1bcd4858: 'CanSetCloset u8',
	0x1be772f0: 'MaxLevel u8',
	0x1d99c513: 'Studio u8',
	0x1e7ef977: 'SelectRate u8',
	0x200dd382: 'Priority u16',
	0x20cb67bc: 'ItemID u16',
	0x23e7c2a0: 'Social u32',
	0x24da7ada: 'Kind u8',
	0x2633f2c1: 'WatchPosX f32',
	0x26bd5137: 'EventObjUniqueID u16',
	0x26db5137: 'EventObjUniqueID u16',
	0x287db05d: 'Month u8',
	0x291a1b04: 'Cap u16',
	0x293ee089: 'SelectRate f32',
	0x2b09d942: 'EndMinute u8',
	0x2b57b24a: 'AcceEye u16',
	0x2c40799e: 'NameboardAngleY f32',
	0x2c447591: 'AsCommand string65',
	0x2c6a189e: 'GrowupFg u16',
	0x2e17a0a7: 'SoundAttribute u16',
	0x31450aa2: 'MainType u8',
	0x318ebbf2: 'TextureWindow u8',
	0x32432484: 'SilhouettePosY f32',
	0x32c0c064: 'HeadColor u16',
	0x32c643e6: 'Announce u8',
	0x33af13e1: 'NpcTalkType u8',
	0x344b17d7: 'MaxValue u32',
	0x3543c34a: 'Horizon u8',
	0x35ac1bb4: 'GrowLevel u8',
	0x35c78d62: 'LookAtType u8',
	0x35fd6466: 'ForbidOverwrite u8',
	0x36083c78: 'Level u16',
	0x364c173e: 'FlowFileName string32',
	0x368210c4: 'ItemCategory u32',
	0x374d00da: 'PosX s16',
	0x378b2f14: 'AppearStage u8',
	0x3835a9dd: 'StartMinute u8',
	0x38762eaa: 'ObjCheckRate f32',
	0x39b5a93d: 'ModelName string32',
	0x39cb9646: 'Material u16',
	0x39dede36: 'SerialID s16',
	0x39ed7f5a: 'Socks u16',
	0x3a14deea: 'NodeName string32',
	0x3a1fca06: 'Direction s8',
	0x3af6dfe2: 'BagID u16',
	0x3b94564c: 'OffsetZ s16',
	0x3ce2e8d8: 'PacketId s32',
	0x3d4f3f42: 'CanSell u8',
	0x3e78dc38: 'FtrPlace u8',
	0x3e884a6d: 'SilhouetteID u32',
	0x3f45f2bf: 'DebugName string64',
	0x3f858678: 'Smartphone u16',
	0x3fe43170: 'FlagLand s32',
	0x4154052c: 'OffsetX s16',
	0x4171a41d: 'FlagPlayer s32',
	0x41935ae1: 'AnimeTypeBook string64',
	0x41977699: 'NpcColor u8',
	0x41afe839: 'BodyColor u16',
	0x42739ab0: 'UseToolLeft u8',
	0x42ad246a: 'Misc u8',
	0x42bdd56f: 'DoorMaterial u16',
	0x430dbf65: 'FlagType u8',
	0x43d8a434: 'HasEigyoLight u8',
	0x443c0fb7: 'LabelLong string64',
	0x454b2adc: 'InitLive u8', # dunno
	0x46c45907: 'Value u16',
	0x46e66708: 'ItemFrom string32',
	0x46e8c73e: 'StaticField u8',
	0x472724ed: 'CanBury u8',
	0x4765b463: 'WatchPointID u16',
	0x478dd182: 'AccessoryID u16',
	0x49129b27: 'CanSetItem u8',
	0x49803457: 'MoveAs u8',
	0x499e42f9: 'ArchUniqueID u16',
	0x49cc96d0: 'ValidEffect u8',
	0x4c24f1cf: 'DefaultValue u32',
	0x4d8d53ba: 'PosZ s16',
	0x4e46c669: 'PropertyID u16',
	0x50edd045: 'BaseName string32',
	0x5195e4bd: 'FloorScale f32',
	0x524596a2: 'BottomsID u16',
	0x52f0badd: 'CalendarEventKey string32',
	0x54706054: 'UniqueID u16',
	0x55c343c4: 'AnimeTypeFirewood string64',
	0x57c98e5b: 'FootColor u16',
	0x58aff4fb: 'ItemTableId u16',
	0x58da05ed: 'WaterCheck u8',
	0x5971a42e: 'WaitFrame u32',
	0x5b7ca0b2: 'SeriesId u8',
	0x5ba37406: 'NpcSpLabel string32',
	0x5baf48a0: 'NpcNoEntry u8',
	0x5c1c3044: 'BridgeTypeId u16',
	0x5cf3a1a1: 'WatchPosZ f32',
	0x5d389fbf: 'CanPut u8',
	0x5e2aa87d: 'AnimeTypeUmbrella string64',
	0x5f384120: 'TextLotId s16',
	0x623dc307: 'Nature u8',
	0x64b8fff8: 'ColorIndex s8',
	0x675ca211: 'EndHour u8',
	0x68460c05: 'ScaleOffset f32',
	0x68cf5938: 'BridgeTypeName string32',
	0x68cf5938: 'BridgeTypeName string32',
	0x68db76c2: 'BreakDamage u16',
	0x69834ab9: 'NpcEnd u8',
	0x69a9bb3c: 'CastLabel u8',
	0x6aa33bf0: 'Name u16',
	0x6ab4b6fb: 'EffectAttribute u16',
	0x6ac5a6df: 'BuryItem u16',
	0x6e1ac981: 'FieldData string32',
	0x6efc082c: 'FloorHeight f32',
	0x70216bfa: 'AnimeTypeFood string64',
	0x718b024d: 'Price s32',
	0x71bf253b: 'BromideItemID s16',
	0x736adca8: 'FlagAnim u16', # possibly?
	0x73a932ae: 'EventEnd s8',
	0x7404ebb3: 'TouchRumble u8',
	0x74b2eb78: 'AttrCollectBit u8',
	0x75e35e54: 'SilhouettePosZ f32',
	0x76c190b2: 'ReleaseKey u16',
	0x76e7fe08: 'ChangeFg u16',
	0x797f5754: 'DefaultValue u16',
	0x79be959d: 'SeasonScore s32',
	0x7c6fde34: 'AnimeTypeFishingRod string64',
	0x7d016b27: 'RoomIndex s16',
	0x7d740fa4: 'EventName string32',
	0x81a43e76: 'NpcType u8',
	0x83b54e59: 'RoofMaterial u16',
	0x85e386bb: 'AnimeTypeBag string64',
	0x870f1e29: 'Tops u16',
	0x8771aa09: 'ItemNum s8',
	0x8792265f: 'AppearValue u16',
	0x87ff95cc: 'Output u8',
	0x895442dc: 'IsSpecial u8',
	0x89a3482c: 'Item u16',
	0x89be1d8f: 'UseMyDesign u8',
	0x8ae48661: 'StartHour u8',
	0x8d58a3bf: 'EventBegin u8',
	0x8f24f1a4: 'RotateOffsetY f32',
	0x8fb1ed85: 'SortID u32',
	0x8fced711: 'LandingUniqueID u16',
	0x8ff469e1: 'CapID u16',
	0x9067bb0e: 'WaitType u8',
	0x90bc0855: 'CanFtr u8',
	0x91eaeedd: 'BattlePoint u8',
	0x926d7dd8: 'UpdateParts u8',
	0x9403c267: 'AcceMouth u16',
	0x9456b6a3: 'BirthMonth u8',
	0x94d6cb5d: 'RuleColor u16',
	0x952cf32e: 'BbsDays u8',
	0x9611c929: 'NpcSpClothSet u16',
	0x973fae34: 'Tool u16',
	0x9951a44b: 'AnimeTypeHandGlass string64',
	0x9b0b7ce4: 'WindowName string64',
	0x9b433dd5: 'CanEat u8',
	0x9bc85bd0: 'SpotType u8',
	0x9c32cf82: 'CarpetMaterial s32',
	0x9c8a400b: 'Construction u8',
	0x9cb82a1e: 'Sand u8',
	0x9e19c94c: 'UseCurtain u8',
	0x9f253177: 'WallScale f32',
	0x9ff07c89: 'LocalizeModel u8',
	0xa0e569dc: 'CurtainUniqueID u16',
	0xa1b074dd: 'NpcLookAction u8',
	0xa2fe7f71: 'BackColor u16',
	0xa425d8a5: 'MsgFile string64',
	0xa4db9685: 'HasJmp u8',
	0xa4f6da11: 'FishPoint s8',
	0xa5f3bd28: 'NameboardPosZ f32',
	0xa6324d34: 'AcceptAccess u8',
	0xa8644472: 'ConditionType u8',
	0xa88f23cf: 'ResourceName string33',
	0xa9de0384: 'RainActive u8',
	0xa9f6fac2: 'BgmEnd u8',
	0xab51a3cf: 'DebugName string32',
	0xac4a3345: 'NfpType u8',
	0xac69956e: 'EventHalf s8',
	0xaf3beca5: 'ItemLayer u8',
	0xb109a778: 'AnimeTypeSitDown string64',
	0xb12e26da: 'GroupIndex s8',
	0xb12e26da: 'GroupIndex s8',
	0xb16c3035: 'CameraParamName string33',
	0xb1f384dc: 'FishPattern s16',
	0xb244d814: 'RotateOffsetX f32',
	0xb418fb3b: 'NearCulling u8',
	0xb5980451: 'ReFabric s16',
	0xb662662c: 'RideHeight f32',
	0xb694c63b: 'ContinuousTime u16',
	0xb76b7d37: 'WatchItem u16',
	0xb7a6c4a8: 'CastType u8',
	0xb7c9dd05: 'EscapeScale f32',
	0xba007e4f: 'ReadyDays u8',
	0xbace6554: 'AppearFg u8',
	0xbb9c816e: 'Umbrella u16',
	0xbd7682f5: 'MaxValue u8',
	0xbe782346: 'SpecialSLink u8',
	0xbfba247c: 'SlopeTableId u16',
	0xc05200e1: 'TexName string32',
	0xc17c7ca8: 'MainDays u8',
	0xc187c516: 'Height f32',
	0xc233727b: 'ItemRemakeType u8',
	0xc33a894e: 'ItemNameUniqueID u16',
	0xc35f78ed: 'TargetShadow u8',
	0xc61c279a: 'ReBody s16',
	0xc70be94f: 'LocalizeAnim u8',
	0xc733aa77: 'Variation u16',
	0xc7ad2fdf: 'CharacterId u32',
	0xc833b068: 'FloorTableId u16',
	0xc89fb7af: 'Storage u8',
	0xcad74e4e: 'ItemData string32',
	0xcb358e51: 'AnimeTypeBasket string64',
	0xcb5eb33f: 'RemakeID s16',
	0xcc136eb5: 'Bottoms u16',
	0xce827d47: 'Shoes u16',
	0xceb81aff: 'BoardDesign u8',
	0xd01f154e: 'TransOffsetY f32',
	0xd069f90c: 'StageName string32',
	0xd06d98dc: 'AnimeTypeSmartPhone string64',
	0xd086a528: 'TargetInsect u8',
	0xd15bdbb6: 'EquipGetRecipe s16',
	0xd1f6dae0: 'Type u8',
	0xd200ffd3: 'WatchAngleY f32',
	0xd2c59675: 'LightParamName string32',
	0xd4697ff8: 'CanPlant u8',
	0xd4892d19: 'AudioMusicID s16',
	0xd55938bd: 'DefaultValue u8',
	0xd5692bff: 'Day u8',
	0xd605c40d: 'NpcBegin u8',
	0xd6b82305: 'NeedType u8',
	0xd7ded52a: 'LabelType u8',
	0xd862189a: 'DefaultSwitch u8',
	0xd89a0db0: 'SelectWeight u8',
	0xd941db12: 'EquipRule string32',
	0xd9a1f501: 'RoomType u32',
	0xda63a0cc: 'WallType u16',
	0xdadfa19a: 'EnglishName string32',
	0xdae27694: 'CanSetChest u8',
	0xdca79149: 'Reaction u8',
	0xdcfb52e8: 'ResName string32',
	0xdf33ee48: 'NameboardPosX f32',
	0xdf881359: 'ResourceName string32',
	0xdfb46994: 'TopsID u16',
	0xe07863ab: 'SpecialSelect u8',
	0xe113ac8d: 'SocksID u16',
	0xe23c6453: 'InsectPattern s16',
	0xe24d9b0e: 'CaptureDiyIcon u8',
	0xe253c7f8: 'NameboardPosY f32',
	0xe2bff7f5: 'SendPlayReport u8',
	0xe3a28616: 'WindowUniqueID u16',
	0xe7e965db: 'PlayerNoEntry u8',
	0xecf95b05: 'Offset f32',
	0xecffb7c6: 'StructureData string32',
	0xed7f3cfe: 'TransOffsetX f32',
	0xee9ce68d: 'BridgeTypeUniqueID u16',
	0xf07156d2: 'ShoesID u16',
	0xf0cf80ff: 'Color u32',
	0xf196e054: 'NetPlay u8',
	0xf2ce6e17: 'AutoDisappear u8',
	0xf37316e6: 'AIFlowName string64',
	0xf429d772: 'HelmetID u16',
	0xf4678f13: 'DigItem u16',
	0xf489f3c5: 'HasDoorWindow u8',
	0xf58109f5: 'SilhouettePoint u8',
	0xf5a73337: 'Grow u8',
	0xf68a2366: 'MessageLabel string32',
	0xf6b34c16: 'SpNpcCloth s16',
	0xf75ddf51: 'Dummy u8',
	0xf8316716: 'Depth f32',
	0xf8a892fc: 'CliffCreate u8',
	0xf8be7f94: 'SmartphoneRemakePattern u16',
	0xfad4ff78: 'ModelResName string65',
	0xfbb451bf: 'PoseTrans u8',
	0xfc275e86: 'CapturePreset string32',
	0xfca98253: 'AnimeTypeNet string64',
	0xfd9af1e1: 'ItemUniqueID u16',
	0xfdeed09c: 'ModelID u16',
	0xffe069a3: 'CheckDonation u8',

	# field outside template
	0xd094759a: 'nw',
	0x1ed42314: 'n1',
	0x7bb31852: 'n2',
	0xd41a5598: 'n3',
	0xb17d6ede: 'n4',
	0x5039c84d: 'n5',
	0xfa9ca833: 'ne',
	0xef18bb10: 'w1',
	0x8a7f8056: 'w2',
	0x25d6cd9c: 'w3',
	0x40b1f6da: 'w4',
	0x19a9348c: 'se',
	0x4038a881: 'e1',
	0x255f93c7: 'e2',
	0x8af6de0d: 'e3',
	0xef91e54b: 'e4',
	0x33a1e925: 'sw',
	0xfde1bfab: 's1',
	0x988684ed: 's2',
	0x372fc927: 's3',
	0x5248f261: 's4',
	0xb30c54f2: 's5',

	# appear params
	0x655e327e: 'apr0816',
	0x57d5055c: 'apr1617',
	0x10757f8c: 'apr1719',
	0x77c808ae: 'apr2304',
	0x93a0aeb8: 'apr0408',
	0xd420d79d: 'apr1923',
	0xf588704d: 'aug0816',
	0xe895b208: 'aug1617',
	0xaf35c8d8: 'aug1719',
	0xc888bffa: 'aug2304',
	0x0376ec8b: 'aug0408',
	0x8d40260e: 'aug1923',
	0x995763a6: 'dec0816',
	0xdf2156eb: 'dec1617',
	0x98812c3b: 'dec1719',
	0xff3c5b19: 'dec2304',
	0x6fa9ff60: 'dec0408',
	0xdd1caee7: 'dec1923',
	0x4026fbe1: 'feb0816',
	0x3740f340: 'feb1617',
	0x70e08990: 'feb1719',
	0x175dfeb2: 'feb2304',
	0xb6d86727: 'feb0408',
	0x78a12603: 'feb1923',
	0x65270095: 'jan0816',
	0x600d479e: 'jan1617',
	0x27ad3d4e: 'jan1719',
	0x40104a6c: 'jan2304',
	0x93d99c53: 'jan0408',
	0x3a737394: 'jan1923',
	0x813dbbdc: 'jul0816',
	0x6fe9a411: 'jul1617',
	0x2849dec1: 'jul1719',
	0x4ff4a9e3: 'jul2304',
	0x77c3271a: 'jul0408',
	0x4f6db088: 'jul1923',
	0xe873aeea: 'jun0816',
	0xa03a7f9d: 'jun1617',
	0xe79a054d: 'jun1719',
	0x8027726f: 'jun2304',
	0x1e8d322c: 'jun0408',
	0x2a93682f: 'jun1923',
	0x06bcf848: 'mar0816',
	0x980c720f: 'mar1617',
	0xdfac08df: 'mar1719',
	0xb8117ffd: 'mar2304',
	0xf042648e: 'mar0408',
	0x7c00c111: 'mar1923',
	0xaebc09bc: 'may0816',
	0x227444fb: 'may1617',
	0x65d43e2b: 'may1719',
	0x02694909: 'may2304',
	0x5842957a: 'may0408',
	0x8feba08a: 'may1923',
	0x1538c8ac: 'nov0816',
	0x3f78d05e: 'nov1617',
	0x78d8aa8e: 'nov1719',
	0x1f65ddac: 'nov2304',
	0xe3c6546a: 'nov0408',
	0x6c66ea56: 'nov1923',
	0xa09fb609: 'oct0816',
	0x99712047: 'oct1617',
	0xded15a97: 'oct1719',
	0xb96c2db5: 'oct2304',
	0x56612acf: 'oct0408',
	0xdac2c157: 'oct1923',
	0x9ebf2c04: 'sep0816',
	0xe7fe7c60: 'sep1617',
	0xa05e06b0: 'sep1719',
	0xc7e37192: 'sep2304',
	0x6841b0c2: 'sep0408',
	0x339772b5: 'sep1923',
}
preset_enum_names = {
	0x9b7aa0a0: 'enum_GroundedItemType',
	0x19a9348c: 'enum_OuterMapChunkType',
	0xd5a8bf7e: 'enum_CompassNESW',
	0x7dcd5be1: 'enum_NoneHighNormalLow',
	0x64330cb0: 'enum_CompassNS',
	0xf80e9fee: 'enum_GenderBias',
	0xdda5d566: 'enum_TwoGenders',
}

def analyse_value(key, value):
	maybe_string = True
	seen_zero = False
	nonzero_bytes = 0

	for index, byte in enumerate(value):
		if byte > 0:
			nonzero_bytes = index + 1

			if seen_zero:
				# non-zero char after a zero means this can't be a string
				maybe_string = False
			else:
				# unprintable char means this can't be a string
				if byte < 0x20:
					maybe_string = False
		else:
			seen_zero = True

	return maybe_string, nonzero_bytes


def infer_type(rows, key, size):
	# perform some S C I E N C E
	maybe_string = True
	max_size = 0
	for row in rows:
		_maybe_string, nonzero_bytes = analyse_value(key, row._data[key])
		maybe_string &= _maybe_string
		if nonzero_bytes > max_size:
			max_size = nonzero_bytes

	if size > 4:
		return ('String', ' # size %d' % size) if maybe_string else None
	else:
		tag = (' # possible string size %d' % size) if maybe_string else ''
		return ((None, 'U8', 'U16', 'U16', 'U32')[size], tag)



def print_enum(prefix, enum):
	en_names, jp_names = enum
	en_names = list(map(repr, en_names))
	jp_names = list(map(repr, jp_names))
	max_len = max(map(len, en_names))
	for e, j in zip(en_names, jp_names):
		print('%s(%s, %s),' % (prefix, e.ljust(max_len), j))

path = sys.argv[1]
files = os.listdir(path)

enum_uses = {}
shared_enums = []
shared_enum_names = []
enum_remaps = {}
assigned_names = set()

def assign_name(key):
	try:
		base = preset_enum_names[key]
	except KeyError:
		base = 'enum_%08x' % key
	if base not in assigned_names:
		assigned_names.add(base)
		return base
	else:
		for i in range(1, 1000):
			name = '%s_%03d' % (base, i)
			if name not in assigned_names:
				assigned_names.add(name)
				return name

with open(sys.argv[2], 'rb') as f:
	enums = json.load(f)
for filename, enum_list in enums.items():
	for key, enum in enum_list.items():
		key = int(key)
		enumkey = str(enum) # terrible hack
		if enumkey in enum_uses:
			if enum not in shared_enums:
				name = assign_name(key)
				shared_enums.append(enum)
				shared_enum_names.append(name)
				enum_remaps[enum_uses[enumkey]] = name
			enum_remaps[(filename, key)] = enum_remaps[enum_uses[enumkey]]
		else:
			enum_uses[enumkey] = (filename, key)

for name, enum in zip(shared_enum_names, shared_enums):
	print('%s = (' % name)
	print_enum('\t', enum)
	print(')')
	print()

for filename in sorted(files):
	if filename.endswith('.bcsv'):
		b = bcsv.File(bcsv.Row)
		print('class %s(Row):' % (filename[:-5]))
		with open('%s/%s' % (path, filename), 'rb') as f:
			b.load(f.read())
		it = b.fields.items()
		if '-sort' in sys.argv:
			it = sorted(it)
		for key, (offset, size) in it:
			try:
				name = preset_names[key]
			except KeyError:
				name = '_%08x' % key
			if ' ' in name:
				# this is something we know, for sure
				name, typ = name.split(' ')
				if typ.startswith('string'):
					print('\t%s = String(0x%08x) # %s' % (name, key, typ))
				else:
					types = dict(
						u8=('U8',1), s8=('S8',1), u16=('U16',2), s16=('S16',2),
						u32=('U32',4), s32=('S32',4), f32=('Float',4))
					typ, esize = types[typ]
					if size > esize:
						# TODO handle this correctly
						suffix = ' # size is %d, could this be an array?' % size
					else:
						suffix = ''
					print('\t%s = %s(0x%08x)%s' % (name, typ, key, suffix))

			elif filename in enums and str(key) in enums[filename]:
				assert(size == 4)
				try:
					remap = enum_remaps[(filename, key)]
					print('\t%s = Enum(0x%08x, %s)' % (name, key, remap))
				except KeyError:
					print('\t%s = Enum(0x%08x, (' % (name, key))
					print_enum('\t\t', enums[filename][str(key)])
					print('\t))')
			else:
				# let's make some assumptions
				typ = infer_type(b.rows, key, size)
				if typ is not None:
					print('\t%s = %s(0x%08x)%s' % (name, typ[0], key, typ[1]))
				else:
					print('\t%s = Field(0x%08x) # %d byte%s' % (name, key, size, '' if size == 1 else 's'))
		print()

print('lookup = {')
for filename in sorted(files):
	if filename.endswith('.bcsv'):
		print('\t%r: %s,' % (filename, filename[:-5]))
print('}')
