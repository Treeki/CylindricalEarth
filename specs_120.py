from bcsv import *

enum_8c2aec6a = (
	('Before', '前日'),
	('Skip'  , '中止'),
	('Same'  , '同時開催'),
)

enum_GroundedItemType = (
	('All'            , '全部'),
	('TreeOak'        , '植物：木：広葉樹'),
	('TreeOakStump'   , '植物：木：広葉樹：切り株'),
	('TreeCedar'      , '植物：木：針葉樹'),
	('TreeCedarStump' , '植物：木：針葉樹：切り株'),
	('TreePalm'       , '植物：木：ヤシの木'),
	('TreePalmStump'  , '植物：木：ヤシの木：切り株'),
	('TreeBamboo'     , '植物：木：竹'),
	('TreeBambooStump', '植物：木：竹：切り株'),
	('TreeFruit'      , '植物：木：果物'),
	('TreeEasterEgg'  , '植物：木：イースターのタマゴ'),
	('WeedSpr'        , '植物：雑草：春'),
	('WeedSmr'        , '植物：雑草：夏'),
	('WeedAut0'       , '植物：雑草：秋０'),
	('WeedAut1'       , '植物：雑草：秋１'),
	('WeedAut2'       , '植物：雑草：秋２'),
	('WeedWin0'       , '植物：雑草：冬０'),
	('WeedWin1'       , '植物：雑草：冬１'),
	('TreeMoney'      , '植物：木：金のなる木'),
	('FlwCosmos'      , '植物：花：コスモス'),
	('FlwTulip'       , '植物：花：チューリップ'),
	('FlwPansy'       , '植物：花：パンジー'),
	('FlwRose'        , '植物：花：バラ'),
	('FlwLily'        , '植物：花：ユリ'),
	('FlwAnemones'    , '植物：花：アネモネ'),
	('FlwMum'         , '植物：花：キク'),
	('FlwHyacinth'    , '植物：花：ヒヤシンス'),
	('FlwSuzuran'     , '植物：花：スズラン'),
	('Hole'           , '穴'),
	('Fence'          , '柵'),
	('Stone'          , '岩'),
)

enum_OuterMapChunkType = (
	('N_Stone'      , 'N岩場'),
	('N_Tsunekiti'  , 'Nつねきち'),
	('NW_Stone'     , 'NW岩場'),
	('NE_Stone'     , 'NE岩場'),
	('W_Beach'      , 'W砂浜'),
	('W_UpEnd_Entry', 'W島(上)'),
	('W_DownEnd'    , 'W島(下)'),
	('W_River'      , 'W汽水地'),
	('W_Stone'      , 'W岩場'),
	('W_Promontory' , 'W岬'),
	('E_Beach'      , 'E砂浜'),
	('E_UpEnd_Entry', 'E島(上)'),
	('E_DownEnd'    , 'E島(下)'),
	('E_River'      , 'E汽水地'),
	('E_Stone'      , 'E岩場'),
	('E_Promontory' , 'E岬'),
	('S_Beach'      , 'S砂浜'),
	('S_River'      , 'S汽水地'),
	('S_Airport_L'  , 'S空港(左)'),
	('S_Airport_R'  , 'S空港(右)'),
	('SW_Beach'     , 'SW砂浜'),
	('SW_Jetty'     , 'SW砂浜桟橋'),
	('SE_Beach'     , 'SE砂浜'),
	('SE_Jetty'     , 'SE砂浜桟橋'),
	('OutsideSea'   , '外周海'),
	('S_Isolated'   , 'S離島桟橋'),
	('PhotoStudio'  , '撮影スタジオ'),
	('Dummy'        , 'ダミー'),
)

enum_7ec9ada7 = (
	('0', '1'),
	('1', '2'),
	('2', '3'),
	('3', '4'),
	('4', '5'),
)

enum_CompassNESW = (
	('S', '南'),
	('E', '東'),
	('N', '北'),
	('W', '西'),
)

enum_CompassNS = (
	('North', '北半球'),
	('South', '南半球'),
)

enum_0e0acf95 = (
	('None', 'なし'),
)

enum_0e6ca0d4 = (
	('AllYear', '通年'),
	('Spring' , '春'),
	('Summer' , '夏'),
	('Autumn' , '秋'),
	('Winter' , '冬'),
)

enum_NoneHighNormalLow = (
	('None'  , '未設定'),
	('High'  , '高'),
	('Normal', '中'),
	('Low'   , '低'),
)

enum_b6bafdfd = (
	('None'         , 'なし'),
	('Outdoor'      , 'アウトドア'),
	('Sea'          , 'うみ'),
	('Office'       , 'オフィス'),
	('Shop'         , 'おみせ'),
	('Music'        , 'おんがく'),
	('School'       , 'がっこう'),
	('Garage'       , 'ガレージ'),
	('Kitchen'      , 'キッチン'),
	('ChildrensRoom', 'こどもべや'),
	('Facility'     , 'しせつ'),
	('Study'        , 'しょさい'),
	('Oriental'     , 'とうようふう'),
	('Party'        , 'パーティー'),
	('BathAndToilet', 'バス・トイレ'),
	('Fitness'      , 'フィットネス'),
	('SnowAndIce'   , 'ごっかん'),
	('Concert'      , 'ライブ'),
	('LivingRoom'   , 'リビング'),
	('Space'        , 'うちゅう'),
	('FolkFcraft'   , 'みんげい'),
	('Horror'       , 'ホラー'),
	('Garden'       , 'にわ'),
	('Rich'         , 'リッチ'),
	('Fancy'        , 'ファンシー'),
)

enum_b7cccd84 = (
	('Orange'   , 'オレンジ'),
	('Red'      , 'レッド'),
	('Pink'     , 'ピンク'),
	('Purple'   , 'パープル'),
	('Blue'     , 'ブルー'),
	('LightBlue', 'みずいろ'),
	('Green'    , 'グリーン'),
	('Yellow'   , 'イエロー'),
	('Beige'    , 'ベージュ'),
	('Brown'    , 'ブラウン'),
	('Black'    , 'ブラック'),
	('Gray'     , 'グレー'),
	('White'    , 'ホワイト'),
	('Colorful' , 'カラフル'),
	('None'     , 'なし'),
)

enum_GenderBias = (
	('Free'   , '性別なし'),
	('Manly'  , '男性向け'),
	('Womanly', '女性向け'),
)

enum_c54eaad9 = (
	('None'     , 'なし'),
	('Warm'     , '暖色'),
	('White'    , 'ホワイト'),
	('Yellow'   , 'イエロー'),
	('Orange'   , 'オレンジ'),
	('Red'      , 'レッド'),
	('Pink'     , 'ピンク'),
	('Purple'   , 'パープル'),
	('Blue'     , 'ブルー'),
	('LightBlue', 'みずいろ'),
	('Green'    , 'グリーン'),
)

enum_be776e71 = (
	('IdrMuseumFish_0'  , '[サカナ]沿岸の部屋'),
	('IdrMuseumFish_1'  , '[サカナ]沖と深海の部屋'),
	('IdrMuseumFish_2'  , '[サカナ]淡水の部屋'),
	('IdrMuseumInsect_0', '[ムシ]大温室'),
	('IdrMuseumInsect_1', '[ムシ]バタフライガーデン'),
	('IdrMuseumInsect_2', '[ムシ]ラボ'),
	('IdrMuseumFossil_0', '[かせき]古生代の部屋'),
	('IdrMuseumFossil_1', '[かせき]中生代の部屋'),
	('IdrMuseumFossil_2', '[かせき]新生代の部屋'),
)

enum_b117eb21 = (
	('None' , 'なし'),
	('Scale', 'あり'),
)

enum_f74f3d2c = (
	('None'    , 'なし'),
	('Synchro' , '同期'),
	('Random'  , 'ランダム'),
	('LightOff', '消灯'),
)

enum_TwoGenders = (
	('Male'  , '男性'),
	('Female', '女性'),
)

enum_d6704d8b = (
	('House'   , '家'),
	('Facility', '施設'),
	('Bridge'  , '橋'),
	('Slope'   , '坂'),
)

enum_a988063c = (
	(''                       , '未設定'),
	('FtrTVProgramSandstorm'  , 'サンドストーム'),
	('FtrTVProgramColorbars'  , 'カラーバー'),
	('FtrTVProgramNews1'      , 'ニュース'),
	('FtrTVProgramWeather'    , '天気予報'),
	('FtrTVProgramDrama'      , 'ドラマ'),
	('FtrTVProgramMusic'      , '音楽番組'),
	('FtrTVProgramQuiz'       , 'クイズ'),
	('FtrTVProgramDocumentary', 'ドキュメンタリー'),
	('FtrTVProgramKids'       , '子ども番組'),
	('FtrTVProgramVariety'    , 'バラエティ'),
	('FtrTVProgramMovie'      , '映画'),
	('FtrTVProgramSports'     , 'スポーツ'),
	('FtrTVProgramTalk'       , '対談番組'),
	('FtrTVProgramAnime'      , 'アニメ'),
	('FtrTVProgramCooking'    , '料理番組'),
	('FtrTVProgramExercise'   , 'エクササイズ'),
	('FtrTVProgramCMCar'      , '季節のCM'),
	('FtrTVProgramCMOyatsu'   , 'おやつCM'),
	('FtrTVProgramCMCompany'  , '企業CM'),
	('FtrTVProgramCMFruits'   , 'フルーツCM'),
	('FtrTVProgramCMShopping' , 'ショッピングCM'),
	('FtrTVProgramSecret'     , '？'),
)

class AITag(Row):
	_a8eacf70 = Enum(0xa8eacf70, (
		('Season'     , '季節'),
		('MinorSeries', '裏シリーズ'),
		('Purpose'    , '目的'),
		('None'       , 'なし'),
	))
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 34

class AmiiboData(Row):
	CharacterId = U32(0xc7ad2fdf)
	NumberingId = U16(0x04a47035)
	SpNpcCloth = S16(0xf6b34c16)
	NfpType = U8(0xac4a3345)
	_34c8eed5 = String(0x34c8eed5) # size 8
	NpcType = U8(0x81a43e76)
	Reaction = U8(0xdca79149)
	SeriesId = U8(0x5b7ca0b2)
	Studio = U8(0x1d99c513) # size is 4, could this be an array?

class BgmPropertyControlParam(Row):
	PropertyID = U16(0x4e46c669)
	UniqueID = U16(0x54706054)
	Value = U16(0x46c45907)
	_85cf1615 = String(0x85cf1615) # size 130

class BgmPropertyParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x13ab5198) # string64

class CalendarEventCountryParam(Row):
	FlagAnim = U16(0x736adca8)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class CalendarEventJuneBrideExchange(Row):
	_598463c8 = U32(0x598463c8)
	_612bc6cf = U32(0x612bc6cf)
	_ad1e04ad = U16(0xad1e04ad)
	_a0bb7510 = U8(0xa0bb7510)
	_7c226372 = U8(0x7c226372)

class CalendarEventJuneBrideReward(Row):
	_612bc6cf = U32(0x612bc6cf)
	_60836eaa = U16(0x60836eaa) # possible string size 2
	_657550b3 = U16(0x657550b3) # possible string size 2
	_7c226372 = U32(0x7c226372)

class CalendarEventParam(Row):
	_70703269 = Enum(0x70703269, (
		('Global'  , 'グローバル'),
		('Region'  , 'リージョン'),
		('Other'   , 'その他（誕生日等）'),
		('Totakeke', 'とたけけライブ'),
		('None'    , 'なし'),
		('Term'    , '期間型'),
	))
	_a75689ff = U32(0xa75689ff)
	_e0f6f32f = U32(0xe0f6f32f)
	_52c75c1e = Enum(0x52c75c1e, enum_8c2aec6a)
	_8c2aec6a = Enum(0x8c2aec6a, enum_8c2aec6a)
	UniqueID = U16(0x54706054)
	Announce = U8(0x32c643e6)
	BbsDays = U8(0x952cf32e)
	_e5337bd9 = U8(0xe5337bd9)
	BoardDesign = U8(0xceb81aff)
	_a45750cc = U8(0xa45750cc)
	_1ceb37a9 = U8(0x1ceb37a9)
	_0e5e9847 = U8(0x0e5e9847)
	_b6e2ff22 = U8(0xb6e2ff22)
	_2b35c79b = U8(0x2b35c79b)
	_9389a0fe = U8(0x9389a0fe)
	_813c0f10 = U8(0x813c0f10)
	_39806875 = U8(0x39806875)
	_61e37823 = U8(0x61e37823)
	_d95f1f46 = U8(0xd95f1f46)
	_9937797c = U8(0x9937797c)
	_218b1e19 = U8(0x218b1e19)
	_333eb1f7 = U8(0x333eb1f7)
	_8b82d692 = U8(0x8b82d692)
	_1655ee2b = U8(0x1655ee2b)
	_aee9894e = U8(0xaee9894e)
	_bc5c26a0 = U8(0xbc5c26a0)
	_04e041c5 = U8(0x04e041c5)
	_5c835193 = U8(0x5c835193)
	_e43f36f6 = U8(0xe43f36f6)
	_de9703ac = U8(0xde9703ac)
	_662b64c9 = U8(0x662b64c9)
	_749ecb27 = U8(0x749ecb27)
	_cc22ac42 = U8(0xcc22ac42)
	_51f594fb = U8(0x51f594fb)
	_e949f39e = U8(0xe949f39e)
	_fbfc5c70 = U8(0xfbfc5c70)
	_43403b15 = U8(0x43403b15)
	_1b232b43 = U8(0x1b232b43)
	_a39f4c26 = U8(0xa39f4c26)
	_e3f72a1c = U8(0xe3f72a1c)
	_5b4b4d79 = U8(0x5b4b4d79)
	_49fee297 = U8(0x49fee297)
	_f14285f2 = U8(0xf14285f2)
	_6c95bd4b = U8(0x6c95bd4b)
	_d429da2e = U8(0xd429da2e)
	_c69c75c0 = U8(0xc69c75c0)
	_7e2012a5 = U8(0x7e2012a5)
	_264302f3 = U8(0x264302f3)
	_9eff6596 = U8(0x9eff6596)
	_51d7f60c = U8(0x51d7f60c)
	_e96b9169 = U8(0xe96b9169)
	_fbde3e87 = U8(0xfbde3e87)
	_436259e2 = U8(0x436259e2)
	_deb5615b = U8(0xdeb5615b)
	_6609063e = U8(0x6609063e)
	_74bca9d0 = U8(0x74bca9d0)
	_cc00ceb5 = U8(0xcc00ceb5)
	_9463dee3 = U8(0x9463dee3)
	_2cdfb986 = U8(0x2cdfb986)
	_6cb7dfbc = U8(0x6cb7dfbc)
	_d40bb8d9 = U8(0xd40bb8d9)
	_c6be1737 = U8(0xc6be1737)
	_7e027052 = U8(0x7e027052)
	_e3d548eb = U8(0xe3d548eb)
	_5b692f8e = U8(0x5b692f8e)
	_49dc8060 = U8(0x49dc8060)
	_f160e705 = U8(0xf160e705)
	_a903f753 = U8(0xa903f753)
	_11bf9036 = U8(0x11bf9036)
	_2b17a56c = U8(0x2b17a56c)
	_d8f76b76 = U8(0xd8f76b76)
	_224c7f34 = U8(0x224c7f34)
	EventBegin = U8(0x8d58a3bf)
	EventEnd = S8(0x73a932ae)
	EventHalf = S8(0xac69956e)
	LabelLong = String(0x443c0fb7) # string64
	_bb66edcb = String(0xbb66edcb) # size 128
	MainDays = U8(0xc17c7ca8)
	_5fd18fa7 = U8(0x5fd18fa7)
	_e76de8c2 = U8(0xe76de8c2)
	_f5d8472c = U8(0xf5d8472c)
	_4d642049 = U8(0x4d642049)
	_d0b318f0 = U8(0xd0b318f0)
	_680f7f95 = U8(0x680f7f95)
	_7abad07b = U8(0x7abad07b)
	_c206b71e = U8(0xc206b71e)
	_9a65a748 = U8(0x9a65a748)
	_22d9c02d = U8(0x22d9c02d)
	_62b1a617 = U8(0x62b1a617)
	_da0dc172 = U8(0xda0dc172)
	_c8b86e9c = U8(0xc8b86e9c)
	_700409f9 = U8(0x700409f9)
	_edd33140 = U8(0xedd33140)
	_556f5625 = U8(0x556f5625)
	_47daf9cb = U8(0x47daf9cb)
	_ff669eae = U8(0xff669eae)
	_a7058ef8 = U8(0xa7058ef8)
	_1fb9e99d = U8(0x1fb9e99d)
	_2511dcc7 = U8(0x2511dcc7)
	_9dadbba2 = U8(0x9dadbba2)
	_8f18144c = U8(0x8f18144c)
	_37a47329 = U8(0x37a47329)
	_aa734b90 = U8(0xaa734b90)
	_12cf2cf5 = U8(0x12cf2cf5)
	_007a831b = U8(0x007a831b)
	_b8c6e47e = U8(0xb8c6e47e)
	_e0a5f428 = U8(0xe0a5f428)
	_5819934d = U8(0x5819934d)
	_1871f577 = U8(0x1871f577)
	_a0cd9212 = U8(0xa0cd9212)
	_b2783dfc = U8(0xb2783dfc)
	_0ac45a99 = U8(0x0ac45a99)
	_97136220 = U8(0x97136220)
	_2faf0545 = U8(0x2faf0545)
	_3d1aaaab = U8(0x3d1aaaab)
	_85a6cdce = U8(0x85a6cdce)
	_ddc5dd98 = U8(0xddc5dd98)
	_6579bafd = U8(0x6579bafd)
	_aa512967 = U8(0xaa512967)
	_12ed4e02 = U8(0x12ed4e02)
	_0058e1ec = U8(0x0058e1ec)
	_b8e48689 = U8(0xb8e48689)
	_2533be30 = U8(0x2533be30)
	_9d8fd955 = U8(0x9d8fd955)
	_8f3a76bb = U8(0x8f3a76bb)
	_378611de = U8(0x378611de)
	_6fe50188 = U8(0x6fe50188)
	_d75966ed = U8(0xd75966ed)
	_973100d7 = U8(0x973100d7)
	_2f8d67b2 = U8(0x2f8d67b2)
	_3d38c85c = U8(0x3d38c85c)
	_8584af39 = U8(0x8584af39)
	_18539780 = U8(0x18539780)
	_a0eff0e5 = U8(0xa0eff0e5)
	_b25a5f0b = U8(0xb25a5f0b)
	_0ae6386e = U8(0x0ae6386e)
	_52852838 = U8(0x52852838)
	_ea394f5d = U8(0xea394f5d)
	_d0917a07 = U8(0xd0917a07)
	_026c5579 = U8(0x026c5579)
	_f8d7413b = U8(0xf8d7413b)
	MsgFile = String(0xa425d8a5) # string64
	_1144c9a1 = String(0x1144c9a1) # size 128
	_3c835e2c = String(0x3c835e2c) # size 128
	NpcBegin = U8(0xd605c40d)
	NpcEnd = U8(0x69834ab9)
	_4b4d3c12 = U8(0x4b4d3c12)
	Output = U8(0x87ff95cc)
	_b92288a3 = U8(0xb92288a3)
	ReadyDays = U8(0xba007e4f)
	_fe807868 = U8(0xfe807868)
	_4ac8ebbc = U8(0x4ac8ebbc)
	_ff468c5f = U8(0xff468c5f)
	_0f4323e2 = U8(0x0f4323e2)
	_c6ddbf67 = String(0xc6ddbf67) # size 64
	_06da20a1 = U8(0x06da20a1)
	_fc6134e3 = U8(0xfc6134e3)
	WeatherPattern = String(0x062ec6cf) # string32
	_4c8935ec = U8(0x4c8935ec)
	_b63221ae = U16(0xb63221ae)

class CalendarEventRegionParam(Row):
	_82bfcf29 = U32(0x82bfcf29) # possible string size 4
	_8b3c9137 = U32(0x8b3c9137)
	_af2602cd = U16(0xaf2602cd) # possible string size 2
	_92462b7d = U16(0x92462b7d) # possible string size 2
	_2066f76d = U16(0x2066f76d) # possible string size 2
	_1d06dedd = U16(0x1d06dedd) # possible string size 2
	UniqueID = U16(0x54706054)
	_be26d70e = String(0xbe26d70e) # size 64
	ItemFrom = String(0x46e66708) # string32

class CharaMakeCheekTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32
	TexName = String(0xc05200e1) # string32

class CharaMakeEyeColorParam(Row):
	_68bed0ef = U32(0x68bed0ef)
	_a05e5f9f = U32(0xa05e5f9f)
	_085e476d = U32(0x085e476d)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 34

class CharaMakeEyeTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32
	ResName = String(0xdcfb52e8) # string32
	_dfa56cb9 = String(0xdfa56cb9) # size 34

class CharaMakeHairColorParam(Row):
	_68bed0ef = U32(0x68bed0ef)
	_a05e5f9f = U32(0xa05e5f9f)
	_085e476d = U32(0x085e476d)
	_16c95acc = U32(0x16c95acc)
	_de29d5bc = U32(0xde29d5bc)
	_7629cd4e = U32(0x7629cd4e)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 34

class CharaMakeHairStyleParam(Row):
	_b22fcc5e = U32(0xb22fcc5e)
	_8f4fe5ee = U32(0x8f4fe5ee)
	_c8ef9f3e = U32(0xc8ef9f3e)
	_866b76fe = U32(0x866b76fe)
	_bb0b5f4e = U32(0xbb0b5f4e)
	_fcab259e = U32(0xfcab259e) # possible string size 4
	_c99ed56e = U32(0xc99ed56e)
	_f4fefcde = U32(0xf4fefcde)
	_b35e860e = U32(0xb35e860e)
	_8659e834 = U32(0x8659e834)
	_bb39c184 = U32(0xbb39c184)
	_fc99bb54 = U32(0xfc99bb54) # possible string size 4
	_c95b5e7d = U32(0xc95b5e7d)
	_f43b77cd = U32(0xf43b77cd)
	_b39b0d1d = U32(0xb39b0d1d)
	_43d2fb34 = U32(0x43d2fb34)
	_7eb2d284 = U32(0x7eb2d284)
	_3912a854 = U32(0x3912a854)
	_27563267 = U32(0x27563267)
	_1a361bd7 = U32(0x1a361bd7)
	_5d966107 = U32(0x5d966107)
	_40dfcd36 = U32(0x40dfcd36)
	_7dbfe486 = U32(0x7dbfe486)
	_3a1f9e56 = U32(0x3a1f9e56) # possible string size 4
	_29c748f7 = U32(0x29c748f7)
	_14a76147 = U32(0x14a76147)
	_53071b97 = U32(0x53071b97)
	_0a2d6f3e = U32(0x0a2d6f3e)
	_374d468e = U32(0x374d468e)
	_70ed3c5e = U32(0x70ed3c5e)
	_0ed6caf4 = U32(0x0ed6caf4)
	_33b6e344 = U32(0x33b6e344)
	_74169994 = U32(0x74169994)
	_19eec64f = U32(0x19eec64f)
	_248eefff = U32(0x248eefff)
	_632e952f = U32(0x632e952f) # possible string size 4
	UniqueID = U16(0x54706054)
	_683b0a91 = String(0x683b0a91) # size 32
	_617794ff = U8(0x617794ff)
	_d1b1b453 = U8(0xd1b1b453)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32
	ResName = String(0xdcfb52e8) # string32

class CharaMakeMouthTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32
	ResName = String(0xdcfb52e8) # string32

class CharaMakeNoseTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32
	NodeName = String(0x3a14deea) # string32

class CharaMakeSkinColorParam(Row):
	_c25cdc73 = U32(0xc25cdc73)
	_0abc5303 = U32(0x0abc5303)
	_a2bc4bf1 = U32(0xa2bc4bf1)
	_384e882c = U32(0x384e882c)
	_f0ae075c = U32(0xf0ae075c)
	_58ae1fae = U32(0x58ae1fae)
	_2dae0aa4 = U32(0x2dae0aa4)
	_e54e85d4 = U32(0xe54e85d4)
	_4d4e9d26 = U32(0x4d4e9d26)
	_5a52c5f4 = U32(0x5a52c5f4)
	_92b24a84 = U32(0x92b24a84)
	_3ab25276 = U32(0x3ab25276)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 34

class ColEffectAttributeParam(Row):
	UniqueID = U16(0x54706054)
	_977adfce = String(0x977adfce) # size 34

class ColGroundAttributeParam(Row):
	EffectAttribute = U16(0x6ab4b6fb)
	SoundAttribute = U16(0x2e17a0a7)
	UniqueID = U16(0x54706054)
	_b99c565a = U16(0xb99c565a)
	CanBury = U8(0x472724ed)
	DebugName = String(0xab51a3cf) # string32
	FtrPlace = U8(0x3e78dc38)
	_2e1e45c3 = String(0x2e1e45c3) # size 16
	_bd859433 = String(0xbd859433) # size 16
	_0254bd05 = U8(0x0254bd05)
	NpcNoEntry = U8(0x5baf48a0)
	PlayerNoEntry = U8(0xe7e965db)
	Sand = U8(0x9cb82a1e)
	WaterCheck = U8(0x58da05ed) # size is 2, could this be an array?

class ColSoundAttributeParam(Row):
	UniqueID = U16(0x54706054)
	_977adfce = String(0x977adfce) # size 34

class DuckingParam(Row):
	UniqueID = U16(0x54706054)
	_85cf1615 = String(0x85cf1615) # size 130

class EventFlagsAocParam(Row):
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	UniqueID = U16(0x54706054)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 129

class EventFlagsBcatParam(Row):
	FlagLand = S32(0x3fe43170)
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	UniqueID = U16(0x54706054)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 129

class EventFlagsHouseParam(Row):
	DefaultValue = U32(0x4c24f1cf)
	MaxValue = U32(0x344b17d7)
	UniqueID = U16(0x54706054)
	_5140e4b4 = U8(0x5140e4b4) # possible string size 1
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 128

class EventFlagsLandParam(Row):
	_fdb1f290 = Enum(0xfdb1f290, (
		('None' , 'クリアしない'),
		('Pre'  , '日またぎ成長処理前（経過日数が0以外）'),
		('Start', '起動時、日またぎ成長処理前'),
		('All'  , 'すべての成長処理（おすそわけ人数変更時を含む）'),
		('Plus' , '日が進んだときの日またぎ成長処理前（経過日数がプラス時）'),
	))
	DefaultValue = U32(0x4c24f1cf)
	_fca0adb0 = Enum(0xfca0adb0, (
		('DisableAccess'  , '×参照×書き込み'),
		('EnableReadOnly' , '○参照×書き込み'),
		('EnableReadWrite', '○参照○書き込み'),
	))
	_93f49ec4 = Enum(0x93f49ec4, (
		('SpNpcOnly'        , '特殊NPCの会話中のみ(自動通信あり)'),
		('ReadOnly'         , '参照のみ可能'),
		('ManualSend'       , '自動通信しない(送信を自前で対応する)'),
		('BitSend'          , 'ビット管理（無断使用不可）'),
		('NoCheck'          , '警告なし（無断使用不可）'),
		('HetHostOnly'      , '自分の村のみ書き換え可(自動通信あり)'),
		('ReadMyVillageOnly', '自分の村のみ参照のみ可能(AOC用)'),
	))
	MaxValue = U32(0x344b17d7)
	UniqueID = U16(0x54706054)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 128
	SendPlayReport = U8(0xe2bff7f5)
	_8b8c8093 = U8(0x8b8c8093)

class EventFlagsLandTempParam(Row):
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	UniqueID = U16(0x54706054)
	_5140e4b4 = U8(0x5140e4b4)
	_3dad9135 = U8(0x3dad9135)
	_3c7fb88f = U8(0x3c7fb88f)
	_fa93f14b = U8(0xfa93f14b)
	_4f7333fd = U8(0x4f7333fd)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 129

class EventFlagsLifeSupportAchievementParam(Row):
	FlagLand = S32(0x3fe43170)
	FlagPlayer = S32(0x4171a41d)
	_95cc0f22 = Enum(0x95cc0f22, (
		('Communication', 'F0：どうぶつ交流系'),
		('Money'        , 'F1：お金系'),
		('Insect'       , 'F2：ムシ系'),
		('DIY'          , 'F3：ＤＩＹ系'),
		('Event'        , 'F4：イベント系'),
		('Fish'         , 'F5：サカナ系'),
		('HHA'          , 'F6：道具系'),
		('LandMaking'   , 'F7：造成系'),
		('MyDesign'     , 'F8：マイデザイン系'),
		('Negative'     , 'F9：ネガティブ系'),
		('Plant'        , 'F10：植物系'),
		('Smartphone'   , 'F11：スマホ系'),
	))
	_ce0933fc = U32(0xce0933fc)
	_89a9492c = U32(0x89a9492c)
	_b4c9609c = U32(0xb4c9609c)
	_06e9bc8c = U32(0x06e9bc8c)
	_3b89953c = U32(0x3b89953c)
	_4e7f3849 = U32(0x4e7f3849)
	_09df4299 = U32(0x09df4299)
	_34bf6b29 = U32(0x34bf6b29)
	_869fb739 = U32(0x869fb739)
	_bbff9e89 = U32(0xbbff9e89)
	_fc5fe459 = U32(0xfc5fe459)
	WaitFrame = U32(0x5971a42e)
	UniqueID = U16(0x54706054)
	IsSpecial = U8(0x895442dc)
	_45f320f2 = String(0x45f320f2) # size 64
	MaxLevel = U8(0x1be772f0)
	_85cf1615 = String(0x85cf1615) # size 128

class EventFlagsLifeSupportDailyParam(Row):
	_b5761610 = Enum(0xb5761610, (
		('None' , 'なし'),
		('Num'  , '数'),
		('Money', '金額'),
	))
	WaitFrame = U32(0x5971a42e)
	AppearValue = U16(0x8792265f)
	_7eabefae = U16(0x7eabefae)
	ItemNameUniqueID = U16(0xc33a894e)
	MaxValue = U16(0x0110b14c)
	_74f1f060 = U16(0x74f1f060)
	Reward = U16(0x127ccfd9)
	UniqueID = U16(0x54706054)
	BonusFive = U8(0x0329d696)
	_0153341a = U8(0x0153341a)
	_679e3850 = U8(0x679e3850)
	_afb1f366 = U8(0xafb1f366)
	_fa93f14b = U8(0xfa93f14b)
	_c47fe703 = U8(0xc47fe703)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 128
	_60da5fef = U8(0x60da5fef)
	SpecialSelect = U8(0xe07863ab)
	_f163e8be = U16(0xf163e8be)

class EventFlagsNpcMemoryParam(Row):
	UniqueID = U16(0x54706054)
	_5f77b61a = U8(0x5f77b61a)
	_5140e4b4 = U8(0x5140e4b4)
	_8d401df7 = U8(0x8d401df7)
	DefaultValue = U8(0xd55938bd)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	MaxValue = U8(0xbd7682f5)
	_85cf1615 = String(0x85cf1615) # size 128

class EventFlagsNpcSaveParam(Row):
	DefaultValue = U32(0x4c24f1cf)
	MaxValue = U32(0x344b17d7)
	UniqueID = U16(0x54706054)
	_5140e4b4 = U8(0x5140e4b4)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 128

class EventFlagsNpcTempParam(Row):
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	UniqueID = U16(0x54706054)
	_5f77b61a = U8(0x5f77b61a) # possible string size 1
	_8d401df7 = U8(0x8d401df7)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 131

class EventFlagsPlayerActivityParam(Row):
	MaxValue = U16(0x0110b14c)
	MessageLabel = U16(0x110a7053)
	_ccd4c25f = U16(0xccd4c25f)
	_e6317726 = U16(0xe6317726)
	UniqueID = U16(0x54706054)
	_fa93f14b = U8(0xfa93f14b) # possible string size 1
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 129

class EventFlagsPlayerParam(Row):
	DefaultValue = U32(0x4c24f1cf)
	MaxValue = U32(0x344b17d7)
	UniqueID = U16(0x54706054)
	_5140e4b4 = U8(0x5140e4b4)
	_bed25a86 = U8(0xbed25a86)
	_c436ce69 = U8(0xc436ce69)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 128
	SendPlayReport = U8(0xe2bff7f5) # size is 2, could this be an array?

class EventFlagsPlayerTempParam(Row):
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	UniqueID = U16(0x54706054)
	_3dad9135 = U8(0x3dad9135)
	_3c7fb88f = U8(0x3c7fb88f)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 131

class EventFlagsPlayerVisitParam(Row):
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	UniqueID = U16(0x54706054)
	_fa93f14b = U8(0xfa93f14b)
	_45f320f2 = String(0x45f320f2) # size 64
	_85cf1615 = String(0x85cf1615) # size 129

class EventPlazaFtrParam(Row):
	_c150fba5 = Enum(0xc150fba5, enum_CompassNESW)
	_24726310 = Enum(0x24726310, (
		('OFF', 'OFF'),
		('ON' , 'ON'),
	))
	ItemNameUniqueID = U16(0xc33a894e)
	UniqueID = U16(0x54706054)

class EventPlazaGround(Row):
	UniqueID = U16(0x54706054)
	ModelName = String(0x39b5a93d) # string32

class EventPlazaObjModelParam(Row):
	DemoDistance = Float(0x158a4c61)
	_a9c1118b = Enum(0xa9c1118b, (
		('None'          , 'なし'),
		('SimpleTalk'    , 'SimpleTalk'),
		('StreetLamp'    , 'StreetLamp'),
		('InsectTent'    , 'InsectTent'),
		('FishTent'      , 'FishTent'),
		('CountdownBoard', 'CountdownBoard'),
		('CountdownStall', 'CountdownStall'),
		('BulletinBoard' , 'BulletinBoard'),
		('Campfire'      , 'Campfire'),
	))
	RoofMaterial = U16(0x83b54e59)
	UniqueID = U16(0x54706054)
	FlowFileName = String(0x364c173e) # string32
	NearCulling = U8(0xb418fb3b)
	ResourceName = String(0xdf881359) # string32

class EventPlazaPlacementParam(Row):
	_036dd90c = U32(0x036dd90c)
	_70703269 = Enum(0x70703269, (
		('PermanentObj'    , '常設オブジェ'),
		('CalendarEvent'   , 'カレンダーイベント'),
		('NpcGroupActivity', 'NPC集団行動'),
		('VisitorNpc'      , '来訪NPC'),
	))
	_24e5b19d = U32(0x24e5b19d)
	_65a97fab = Enum(0x65a97fab, (
		('EventObj', 'イベントオブジェ'),
		('Ftr'     , '家具'),
		('NPC'     , 'NPC'),
	))
	_20dd4435 = U16(0x20dd4435)
	EventObjUniqueID = U16(0x26db5137)
	OffsetX = S16(0x4154052c)
	OffsetZ = S16(0x3b94564c)
	UniqueID = U16(0x54706054)
	CalendarEventKey = String(0x52f0badd) # string32
	_e6c63c5c = String(0xe6c63c5c) # size 32
	_7215b154 = String(0x7215b154) # size 32
	NpcSpLabel = String(0x5ba37406) # string32
	_e2d0ac54 = String(0xe2d0ac54) # size 32
	_7e322ef0 = String(0x7e322ef0) # size 34

class FgFlowerHeredity(Row):
	_9b7aa0a0 = Enum(0x9b7aa0a0, enum_GroundedItemType)
	Name = U16(0x6aa33bf0)
	_753336dd = U16(0x753336dd) # possible string size 2
	_08d23365 = U8(0x08d23365)
	_c7208ade = U8(0xc7208ade)
	_d5952530 = U8(0xd5952530)
	_6d294255 = U8(0x6d294255)
	_f0fe7aec = U32(0xf0fe7aec)

class FgMainParam(Row):
	_0c315945 = U32(0x0c315945)
	_360b721a = Enum(0x360b721a, (
		('WhitishFlower'        , '白系の花'),
		('RedPinkFlower'        , '赤・桃系の花'),
		('BluePurpleBlackFlower', '青・紫・黒系の花'),
		('YellowFlower'         , '黄色系の花'),
		('MatureTreeOak'        , '広葉樹（成木）'),
		('MatureTreeCedar'      , '針葉樹（成木）'),
		('MatureTreePalm'       , 'ヤシの木（成木）'),
		('MatureTreeBamboo'     , '竹（成木）'),
		('TreeOakStump'         , '広葉樹：切り株'),
		('TreeCedarStump'       , '針葉樹：切り株'),
		('TreePalmStump'        , 'ヤシの木：切り株'),
		('TreeBambooStump'      , '竹：切り株'),
		('Trash'                , 'ゴミ（ハエ用）'),
		('TurnipExpired'        , '腐ったカブ'),
		('Candy'                , '飴（アリ用）'),
		('TreeAdhereHoneycomb'  , '蜂の巣付きの木'),
		('Stone'                , '岩'),
		('None'                 , 'なし'),
	))
	_9b7aa0a0 = Enum(0x9b7aa0a0, enum_GroundedItemType)
	_123efcf1 = U32(0x123efcf1) # possible string size 4
	BuryItem = U16(0x6ac5a6df)
	_d59ff85e = U16(0xd59ff85e)
	_e8ffd1ee = U16(0xe8ffd1ee)
	ChangeFg = U16(0x76e7fe08)
	DigItem = U16(0xf4678f13)
	EffectAttribute = U16(0x6ab4b6fb)
	GrowupFg = U16(0x2c6a189e)
	_be17c845 = U16(0xbe17c845)
	_b7a46956 = U16(0xb7a46956)
	SoundAttribute = U16(0x2e17a0a7)
	UniqueID = U16(0x54706054)
	ColorIndex = S8(0x64b8fff8)
	DebugName = String(0x3f45f2bf) # string64
	Grow = U8(0xf5a73337)
	Label = String(0x87bf00e8) # string32
	ModelName = String(0x39b5a93d) # string32
	Nature = U16(0x623dc307) # size is 2, could this be an array?
	_a4b2d66d = U8(0xa4b2d66d)
	_48ef0398 = String(0x48ef0398) # size 65

class FieldCreateParam(Row):
	_6654378d = Enum(0x6654378d, (
		('Default'          , 'Default'),
		('MainField'        , 'MainField'),
		('PlayerHouse'      , 'PlayerHouse'),
		('NpcHouse'         , 'NpcHouse'),
		('MysteryTourIsland', 'MysteryTourIsland'),
		('PhotoStudioIsland', 'PhotoStudioIsland'),
		('PhotoStudioHouse' , 'PhotoStudioHouse'),
	))
	_65d009e1 = Enum(0x65d009e1, (
		('Room0', '部屋0'),
		('Room1', '部屋1'),
		('Room2', '部屋2'),
		('Room3', '部屋3'),
		('Room4', '部屋4'),
		('Room5', '部屋5'),
	))
	_897261e3 = Enum(0x897261e3, (
		('Invalid', 'なし'),
		('Room0'  , 'エントランス'),
		('Room1'  , '奥部屋'),
		('Room2'  , '左部屋'),
		('Room3'  , '右部屋'),
		('Room4'  , '2F'),
		('Room5'  , '地下室'),
	))
	ItemLayer = U8(0xaf3beca5)
	StageName = String(0xd069f90c) # string32
	StaticField = U8(0x46e8c73e) # size is 3, could this be an array?

class FieldDistantViewParam(Row):
	UniqueID = U16(0x54706054)
	ResName = String(0xdcfb52e8) # string32

class FieldLandMakingActionParam(Row):
	_59485fad = Enum(0x59485fad, (
		('1x1', '1x1'),
		('3x3', '3x3'),
	))
	_75fee4b0 = Enum(0x75fee4b0, (
		('NoChange'     , '変更なし'),
		('AddCliffLevel', '崖レベル加算'),
		('RemoveHistory', '最終履歴削除'),
	))
	_0bcf172f = Enum(0x0bcf172f, (
		('RightToSlant', '直角 -> 斜め'),
		('SlantToRight', '斜め -> 直角'),
	))
	_281f90a8 = Enum(0x281f90a8, (
		('None'     , 'なし'),
		('MakeFall' , '崖 -> 滝'),
		('BreakFall', '滝 -> 崖'),
	))
	_ef79de0f = Enum(0xef79de0f, (
		('No0', 'レイヤ0'),
		('No1', 'レイヤ1'),
	))
	_e421a842 = Enum(0xe421a842, (
		('NoChange', '変更なし'),
		('CliffAll', '平地 -> 崖平地'),
	))
	_7674c4d6 = Enum(0x7674c4d6, (
		('None', 'なし'),
		('1x1' , '1x1'),
		('3x3' , '3x3'),
	))
	_4932f93e = Enum(0x4932f93e, (
		('Make' , 'Make'),
		('Break', 'Break'),
	))
	_7c8e7f81 = U8(0x7c8e7f81)
	_f9a37bdc = U8(0xf9a37bdc)
	MainType = U8(0x31450aa2)
	UpdateParts = U8(0x926d7dd8)

class FieldLandMakingError(Row):
	UniqueID = U16(0x54706054)
	_7703d2dd = String(0x7703d2dd) # size 50
	CliffCreate = U8(0xf8a892fc)
	_0b3be609 = U8(0x0b3be609) # possible string size 1
	_b92c3183 = String(0xb92c3183) # size 40
	Label = String(0x69b161c4) # string30
	_04034aa7 = String(0x04034aa7) # size 60

class FieldLandMakingRoadKindParam(Row):
	_2df085cc = U16(0x2df085cc)
	_af88956b = U8(0xaf88956b)
	MessageLabel = String(0xf68a2366) # string32

class FieldLandMakingUnitModelParam(Row):
	_d943e2bd = Enum(0xd943e2bd, (
		('None'  , 'なし'),
		('ToFall', '縦横滝'),
	))
	_9dfa9b39 = Enum(0x9dfa9b39, (
		('None' , 'なし'),
		('Right', '直角'),
		('Slant', '斜め'),
	))
	_0d54d810 = Enum(0x0d54d810, (
		('None'      , 'なし'),
		('Variation1', 'Variation1'),
		('Variation2', 'Variation2'),
		('Variation4', 'Variation4'),
	))
	_eb4430c7 = Enum(0xeb4430c7, (
		('Base'        , '地面'),
		('River'       , '川'),
		('RoadStone'   , '石道'),
		('Cliff'       , '崖'),
		('None'        , 'なし'),
		('Invalid'     , '無効値'),
		('Soil'        , '土'),
		('Brick'       , 'レンガ'),
		('DarkSoil'    , '黒土'),
		('StonePattern', '石畳'),
		('Sand'        , '砂'),
		('Tile'        , 'タイル'),
		('Wood'        , '木'),
	))
	_c01e47a7 = Enum(0xc01e47a7, (
		('Plane', '平地'),
		('River', '川'),
		('Road' , '道'),
		('Cliff', '崖'),
		('Fall' , '滝'),
	))
	_c7f82afd = Enum(0xc7f82afd, (
		('Level0', 'なし'),
		('Level1', '1段'),
	))
	_59d78633 = Enum(0x59d78633, (
		('Invalid'   , 'なし'),
		('UpperLeft' , '左上三角'),
		('LowerLeft' , '左下三角'),
		('LowerRight', '右下三角'),
		('UpperRight', '右上三角'),
	))
	UniqueID = U16(0x54706054)
	Variation = U16(0xc733aa77)
	FishPoint = S8(0xa4f6da11)
	_f85c61d4 = U8(0xf85c61d4)
	_eae9ce3a = U8(0xeae9ce3a)
	_5255a95f = U8(0x5255a95f)
	_7d802f01 = U8(0x7d802f01)
	_c53c4864 = U8(0xc53c4864)
	_d789e78a = U8(0xd789e78a)
	_6f3580ef = U8(0x6f3580ef)
	_3a2055d1 = U8(0x3a2055d1)
	_829c32b4 = U8(0x829c32b4)
	_90299d5a = U8(0x90299d5a)
	_2895fa3f = U8(0x2895fa3f)
	_07407c61 = U8(0x07407c61)
	_bffc1b04 = U8(0xbffc1b04)
	_ad49b4ea = U8(0xad49b4ea)
	_15f5d38f = U8(0x15f5d38f)
	_8bbcd514 = U8(0x8bbcd514)
	_3300b271 = U8(0x3300b271)
	_21b51d9f = U8(0x21b51d9f)
	_99097afa = U8(0x99097afa)
	_b6dcfca4 = U8(0xb6dcfca4)
	_0e609bc1 = U8(0x0e609bc1)
	_1cd5342f = U8(0x1cd5342f)
	_a469534a = U8(0xa469534a)
	_f17c8674 = U8(0xf17c8674)
	_49c0e111 = U8(0x49c0e111)
	_5b754eff = U8(0x5b754eff)
	_e3c9299a = U8(0xe3c9299a)
	_cc1cafc4 = U8(0xcc1cafc4)
	_74a0c8a1 = U8(0x74a0c8a1)
	_6615674f = U8(0x6615674f)
	_dea9002a = U8(0xdea9002a)
	ModelName = String(0x39b5a93d) # string32

class FieldMainFieldParam(Row):
	UniqueID = U16(0x54706054)
	FieldData = String(0x6e1ac981) # string32
	ItemData = String(0xcad74e4e) # string32
	Label = String(0x87bf00e8) # string32
	_948eb946 = U8(0x948eb946)
	StructureData = String(0xecffb7c6) # string32

class FieldOutsideParts(Row):
	_493eed57 = Enum(0x493eed57, enum_OuterMapChunkType)
	_b5a652fa = Enum(0xb5a652fa, (
		('N_convexity' , 'N凸'),
		('N_flat'      , 'N平'),
		('N_concavity' , 'N凹'),
		('NE_convexity', 'NE凸'),
		('NE_flat'     , 'NE平'),
		('NE_concavity', 'NE凹'),
		('E_convexity' , 'E凸'),
		('E_flat'      , 'E平'),
		('E_concavity' , 'E凹'),
		('SE_convexity', 'SE凸'),
		('SE_flat'     , 'SE平'),
		('SE_concavity', 'SE凹'),
		('S_convexity' , 'S凸'),
		('S_flat'      , 'S平'),
		('S_concavity' , 'S凹'),
		('SW_convexity', 'SW凸'),
		('SW_flat'     , 'SW平'),
		('SW_concavity', 'SW凹'),
		('W_convexity' , 'W凸'),
		('W_flat'      , 'W平'),
		('W_concavity' , 'W凹'),
		('NW_convexity', 'NW凸'),
		('NW_flat'     , 'NW平'),
		('NW_concavity', 'NW凹'),
	))
	UniqueID = U16(0x54706054)
	ModelName = String(0x39b5a93d) # string32

class FieldOutsideTemplate(Row):
	e1 = Enum(0x4038a881, enum_OuterMapChunkType)
	e2 = Enum(0x255f93c7, enum_OuterMapChunkType)
	e3 = Enum(0x8af6de0d, enum_OuterMapChunkType)
	e4 = Enum(0xef91e54b, enum_OuterMapChunkType)
	n1 = Enum(0x1ed42314, enum_OuterMapChunkType)
	n2 = Enum(0x7bb31852, enum_OuterMapChunkType)
	n3 = Enum(0xd41a5598, enum_OuterMapChunkType)
	n4 = Enum(0xb17d6ede, enum_OuterMapChunkType)
	n5 = Enum(0x5039c84d, enum_OuterMapChunkType)
	ne = Enum(0xfa9ca833, enum_OuterMapChunkType)
	nw = Enum(0xd094759a, enum_OuterMapChunkType)
	s1 = Enum(0xfde1bfab, enum_OuterMapChunkType)
	s2 = Enum(0x988684ed, enum_OuterMapChunkType)
	s3 = Enum(0x372fc927, enum_OuterMapChunkType)
	s4 = Enum(0x5248f261, enum_OuterMapChunkType)
	s5 = Enum(0xb30c54f2, enum_OuterMapChunkType)
	se = Enum(0x19a9348c, enum_OuterMapChunkType)
	sw = Enum(0x33a1e925, enum_OuterMapChunkType)
	_714d3f2e = Enum(0x714d3f2e, (
		('EC', '東進入禁止'),
		('WC', '西進入禁止'),
		('3B', '東西進入可'),
	))
	_29346c33 = Enum(0x29346c33, (
		('3B_S2', '南中州'),
		('3B_SE', '南東中州'),
		('3B_SW', '南西中州'),
	))
	w1 = Enum(0xef18bb10, enum_OuterMapChunkType)
	w2 = Enum(0x8a7f8056, enum_OuterMapChunkType)
	w3 = Enum(0x25d6cd9c, enum_OuterMapChunkType)
	w4 = Enum(0x40b1f6da, enum_OuterMapChunkType)
	_6971370a = Enum(0x6971370a, (
		('DNE_NNW', '昼：北東、夜：北西'),
		('DNW_NNE', '昼：北西、夜：北東'),
	))
	UniqueID = U16(0x54706054)
	EnglishName = String(0xdadfa19a) # string32

class FishAppearRiverParam(Row):
	ItemID = U16(0x20cb67bc)
	_9c4a43c0 = U16(0x9c4a43c0)
	_0dbbebb5 = U16(0x0dbbebb5)
	_1d790df7 = U16(0x1d790df7)
	_15de6a3f = U16(0x15de6a3f)
	_74ea1d73 = U16(0x74ea1d73)
	_ada9eb19 = U16(0xada9eb19)
	_267c99f7 = U16(0x267c99f7)
	_c11af347 = U16(0xc11af347)
	_9217f8b8 = U16(0x9217f8b8)
	_5cb71135 = U16(0x5cb71135)
	_0f095b88 = U16(0x0f095b88)
	_91ee0d19 = U16(0x91ee0d19)
	_b3f1a70f = U16(0xb3f1a70f)
	_51bcedfa = U16(0x51bcedfa)
	_3e01d394 = U16(0x3e01d394)
	_2b74f5dc = U16(0x2b74f5dc)
	_7ec203a5 = U16(0x7ec203a5)
	_24dbb4e0 = U16(0x24dbb4e0)
	_c74f6b43 = U16(0xc74f6b43)
	_5092ca25 = U16(0x5092ca25)
	_202e64dd = U16(0x202e64dd)
	_df2eadb2 = U16(0xdf2eadb2)
	_2cb125cc = U16(0x2cb125cc)
	_770b5b7d = U16(0x770b5b7d)
	may0816 = U16(0xaebc09bc)
	_ac8aae8c = U16(0xac8aae8c)
	may1923 = U16(0x8feba08a)
	_5aafbfa6 = U16(0x5aafbfa6)
	_c57d2eb8 = U16(0xc57d2eb8)
	_5b0802f1 = U16(0x5b0802f1)
	_b12179b4 = U16(0xb12179b4)
	_6aed60aa = U16(0x6aed60aa)
	_ce420c64 = U16(0xce420c64)
	_5e853057 = U16(0x5e853057)
	_1fe65c0c = U16(0x1fe65c0c)
	_260ec620 = U16(0x260ec620)
	AppearArea = U8(0x137dd804) # size is 2, could this be an array?

class FishAppearSeaParam(Row):
	ItemID = U16(0x20cb67bc)
	_9c4a43c0 = U16(0x9c4a43c0)
	_0dbbebb5 = U16(0x0dbbebb5)
	_1d790df7 = U16(0x1d790df7)
	_15de6a3f = U16(0x15de6a3f)
	_74ea1d73 = U16(0x74ea1d73)
	_ada9eb19 = U16(0xada9eb19)
	_267c99f7 = U16(0x267c99f7)
	_c11af347 = U16(0xc11af347)
	_9217f8b8 = U16(0x9217f8b8)
	_5cb71135 = U16(0x5cb71135)
	_0f095b88 = U16(0x0f095b88)
	_91ee0d19 = U16(0x91ee0d19)
	_b3f1a70f = U16(0xb3f1a70f)
	_51bcedfa = U16(0x51bcedfa)
	_3e01d394 = U16(0x3e01d394)
	_2b74f5dc = U16(0x2b74f5dc)
	_7ec203a5 = U16(0x7ec203a5)
	_24dbb4e0 = U16(0x24dbb4e0)
	_c74f6b43 = U16(0xc74f6b43)
	_5092ca25 = U16(0x5092ca25)
	_202e64dd = U16(0x202e64dd)
	_df2eadb2 = U16(0xdf2eadb2)
	_2cb125cc = U16(0x2cb125cc)
	_770b5b7d = U16(0x770b5b7d)
	may0816 = U16(0xaebc09bc)
	_ac8aae8c = U16(0xac8aae8c)
	may1923 = U16(0x8feba08a)
	_5aafbfa6 = U16(0x5aafbfa6)
	_c57d2eb8 = U16(0xc57d2eb8)
	_5b0802f1 = U16(0x5b0802f1)
	_b12179b4 = U16(0xb12179b4)
	_6aed60aa = U16(0x6aed60aa)
	_ce420c64 = U16(0xce420c64)
	_5e853057 = U16(0x5e853057)
	_1fe65c0c = U16(0x1fe65c0c)
	_260ec620 = U16(0x260ec620)
	AppearArea = U8(0x137dd804) # size is 2, could this be an array?

class FishBeyQuestParam(Row):
	UniqueID = U16(0x54706054)
	_748db6d8 = U8(0x748db6d8)
	_c44b9674 = U8(0xc44b9674)
	_fb867bc1 = U32(0xfb867bc1)

class FishStatusParam(Row):
	_64330cb0 = Enum(0x64330cb0, enum_CompassNS)
	_0de2a3be = Enum(0x0de2a3be, (
		('River'         , '川'),
		('RiverCliffTop' , '川：崖上'),
		('Pond'          , '池'),
		('BrackishWater' , '汽水池'),
		('Sea'           , '海'),
		('Anywhere'      , 'どこでも'),
		('SeaBeachBridge', '海：桟橋'),
	))
	_770288fd = Enum(0x770288fd, enum_7ec9ada7)
	EscapeScale = Float(0xb7c9dd05)
	_132dd5b9 = Enum(0x132dd5b9, (
		('KeepSwimming'  , '回遊：通常'),
		('Float'         , '待機'),
		('RoundsSwimming', '回遊：見回り'),
		('ChasePlayer'   , 'プレイヤーサーチ'),
		('Legion'        , '大群'),
		('Predator'      , '捕食者'),
		('AntiStream'    , '抗水流'),
		('SwimAndWait'   , '回遊＆待機'),
	))
	_4108715d = U32(0x4108715d)
	_7ec9ada7 = Enum(0x7ec9ada7, enum_7ec9ada7)
	_ac0ebe24 = Enum(0xac0ebe24, (
		('SS' , 'SS'),
		('S'  , 'S'),
		('M'  , 'M'),
		('L'  , 'L'),
		('LL' , 'LL'),
		('LLL', 'LLL'),
		('U'  , 'U'),
		('J'  , 'J'),
		('K'  , 'K'),
	))
	ItemID = U16(0x20cb67bc)
	_eac6a012 = U16(0xeac6a012)
	_daaf8ba0 = U16(0xdaaf8ba0)
	UniqueID = U16(0x54706054)
	DebugName = String(0xab51a3cf) # string32
	_3dc49bc2 = U8(0x3dc49bc2)
	_0e91fc27 = U8(0x0e91fc27)
	Label = String(0x87bf00e8) # string32
	_1f875d3d = String(0x1f875d3d) # size 32
	_48ef0398 = String(0x48ef0398) # size 64
	_1c8856db = String(0x1c8856db) # size 34

class GmoFootprintParam(Row):
	_6d4bd7da = Enum(0x6d4bd7da, (
		('Pad'     , '肉球'),
		('Circle'  , 'まる'),
		('Oval'    , '長まる'),
		('ThinOval', '細長まる'),
		('Bird'    , 'トリ'),
		('Bird2'   , 'トリ（太）'),
		('Hoof'    , 'ヒヅメ'),
		('None'    , 'なし'),
		('Pumps'   , 'パンプス'),
	))
	_0fd26913 = Enum(0x0fd26913, (
		('TestSoft', 'testやわらかいくつ'),
		('Naked'   , 'はだし'),
		('Socks'   , 'くつした'),
		('Bird'    , 'トリ'),
		('Soft'    , 'やわらかい靴'),
		('Hard'    , 'かたい靴'),
		('None'    , 'なし'),
		('Geta'    , 'げた'),
		('Pumps'   , 'パンプス'),
	))
	UniqueID = U16(0x54706054)
	_85cf1615 = String(0x85cf1615) # size 130

class HumanAnimParam(Row):
	_0b69ec1a = Enum(0x0b69ec1a, (
		('DisableOnlyLowerBody'     , '下半身再生不可'),
		('EnableOnlyLowerBody_Sit'  , '下半身再生可(座り系)'),
		('EnableOnlyLowerBody_Bed'  , '下半身再生可(寝る系)'),
		('EnableOnlyLowerBody_Stand', '下半身再生可(立ち系)'),
	))
	_2fe593c3 = U16(0x2fe593c3)
	UniqueID = U16(0x54706054)
	_9f5123d4 = U8(0x9f5123d4)
	_d5217761 = U8(0xd5217761)
	AsCommand = String(0x2c447591) # string65
	_84761fb6 = U8(0x84761fb6)
	_fc3116b5 = U8(0xfc3116b5)
	_96ba28fe = String(0x96ba28fe) # size 64
	Misc = U8(0x42ad246a) # size is 3, could this be an array?
	MoveAs = U8(0x49803457)
	_26911c10 = String(0x26911c10) # size 31

class IndoorIdrParam(Row):
	_607ccfce = U16(0x607ccfce) # possible string size 2
	_91b7e30b = U16(0x91b7e30b)
	_707e79ff = U16(0x707e79ff)
	UniqueID = U16(0x54706054)
	_4b9c4229 = String(0x4b9c4229) # size 64

class IndoorPhotoStudioItemParam(Row):
	_d5a8bf7e = Enum(0xd5a8bf7e, enum_CompassNESW)
	ItemID = U16(0x20cb67bc)
	PosX = S16(0x374d00da)
	PosZ = S16(0x4d8d53ba)
	ReBody = S16(0xc61c279a)
	ReFabric = S16(0xb5980451)
	RoomIndex = S16(0x7d016b27)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class InsectAppearParam(Row):
	ItemID = U16(0x20cb67bc)
	apr0816 = U16(0x655e327e)
	apr1617 = U16(0x57d5055c)
	apr1719 = U16(0x10757f8c)
	apr2304 = U16(0x77c808ae)
	apr0408 = U16(0x93a0aeb8)
	apr1923 = U16(0xd420d79d)
	aug0816 = U16(0xf588704d)
	aug1617 = U16(0xe895b208)
	aug1719 = U16(0xaf35c8d8)
	aug2304 = U16(0xc888bffa)
	aug0408 = U16(0x0376ec8b)
	aug1923 = U16(0x8d40260e)
	dec0816 = U16(0x995763a6)
	dec1617 = U16(0xdf2156eb)
	dec1719 = U16(0x98812c3b)
	dec2304 = U16(0xff3c5b19)
	dec0408 = U16(0x6fa9ff60)
	dec1923 = U16(0xdd1caee7)
	feb0816 = U16(0x4026fbe1)
	feb1617 = U16(0x3740f340)
	feb1719 = U16(0x70e08990)
	feb2304 = U16(0x175dfeb2)
	feb0408 = U16(0xb6d86727)
	feb1923 = U16(0x78a12603)
	jan0816 = U16(0x65270095)
	jan1617 = U16(0x600d479e)
	jan1719 = U16(0x27ad3d4e)
	jan2304 = U16(0x40104a6c)
	jan0408 = U16(0x93d99c53)
	jan1923 = U16(0x3a737394)
	jul0816 = U16(0x813dbbdc)
	jul1617 = U16(0x6fe9a411)
	jul1719 = U16(0x2849dec1)
	jul2304 = U16(0x4ff4a9e3)
	jul0408 = U16(0x77c3271a)
	jul1923 = U16(0x4f6db088)
	jun0816 = U16(0xe873aeea)
	jun1617 = U16(0xa03a7f9d)
	jun1719 = U16(0xe79a054d)
	jun2304 = U16(0x8027726f)
	jun0408 = U16(0x1e8d322c)
	jun1923 = U16(0x2a93682f)
	mar0816 = U16(0x06bcf848)
	mar1617 = U16(0x980c720f)
	mar1719 = U16(0xdfac08df)
	mar2304 = U16(0xb8117ffd)
	mar0408 = U16(0xf042648e)
	mar1923 = U16(0x7c00c111)
	may0816 = U16(0xaebc09bc)
	may1617 = U16(0x227444fb)
	may1719 = U16(0x65d43e2b)
	may2304 = U16(0x02694909)
	may0408 = U16(0x5842957a)
	may1923 = U16(0x8feba08a)
	nov0816 = U16(0x1538c8ac)
	nov1617 = U16(0x3f78d05e)
	nov1719 = U16(0x78d8aa8e)
	nov2304 = U16(0x1f65ddac)
	nov0408 = U16(0xe3c6546a)
	nov1923 = U16(0x6c66ea56)
	oct0816 = U16(0xa09fb609)
	oct1617 = U16(0x99712047)
	oct1719 = U16(0xded15a97)
	oct2304 = U16(0xb96c2db5)
	oct0408 = U16(0x56612acf)
	oct1923 = U16(0xdac2c157)
	sep0816 = U16(0x9ebf2c04)
	sep1617 = U16(0xe7fe7c60)
	sep1719 = U16(0xa05e06b0)
	sep2304 = U16(0xc7e37192)
	sep0408 = U16(0x6841b0c2)
	sep1923 = U16(0x339772b5)
	UniqueID = U16(0x54706054)
	AppearArea = U8(0x137dd804) # size is 4, could this be an array?

class InsectBattleParam(Row):
	Level = U16(0x36083c78)
	UniqueID = U16(0x54706054)
	_4d9888d3 = U32(0x4d9888d3)

class InsectStatusParam(Row):
	_64330cb0 = Enum(0x64330cb0, enum_CompassNS)
	_a103c985 = Enum(0xa103c985, (
		('AlwaysAppear'                   , '天気によらず発生'),
		('AppearInRain'                   , '雨天時のみ発生'),
		('AppearInSnowGroundTerm'         , '積雪期間のみ発生'),
		('NotAppearInRain'                , '雨天時は発生しない'),
		('NotAppearInRainAndSnow'         , '雨天時、降雪時は発生しない'),
		('AppearInCherryBlossomOpenUpTerm', '桜が咲いている期間のみ発生'),
		('AppearInAutumnLeavesTerm'       , '紅葉の期間のみ発生'),
	))
	_27450132 = U32(0x27450132)
	_9b7aa0a0 = Enum(0x9b7aa0a0, (
		('Ant'         , 'アリ'),
		('Beetle'      , '甲虫'),
		('Butterfly'   , 'チョウ'),
		('CastOffSkin' , 'セミノヌケガラ'),
		('Cicada'      , 'セミ'),
		('Dragonfly'   , 'トンボ'),
		('Feather'     , '羽'),
		('Firefly'     , 'ホタル'),
		('Flea'        , 'ノミ'),
		('Flower'      , '花の虫'),
		('Fly'         , 'ハエ'),
		('HermitCrab'  , 'ヤドカリ'),
		('HoneyBee'    , 'ミツバチ'),
		('Hornet'      , 'スズメバチ'),
		('Leaf'        , 'コノハムシ'),
		('Locust'      , 'バッタ'),
		('MoleCricket' , 'オケラ'),
		('Mosquito'    , 'カ'),
		('Moth'        , 'ガ'),
		('PillBug'     , 'ダンゴムシ'),
		('Scorpion'    , 'サソリ'),
		('SeaSlater'   , 'フナムシ'),
		('SnowCrystal' , '雪の結晶'),
		('Spider'      , 'クモ'),
		('Stump'       , '切り株'),
		('TigerBeetle' , 'ハンミョウ'),
		('Tumblebug'   , 'フンコロガシ'),
		('WaterBeetle' , 'ゲンゴロウ'),
		('WaterStrider', 'アメンボ'),
		('Wisp'        , '魂'),
		('Petal'       , '花弁'),
		('AutumnLeaf'  , '紅葉'),
	))
	_da0b5c29 = U32(0xda0b5c29)
	ItemID = U16(0x20cb67bc)
	_5d4ef312 = U16(0x5d4ef312)
	_daaf8ba0 = U16(0xdaaf8ba0)
	UniqueID = U16(0x54706054)
	AppearFg = U8(0xbace6554) # size is 3, could this be an array?
	DebugName = String(0x3f45f2bf) # string64
	Label = String(0x87bf00e8) # string32
	Property = U8(0x0909f3d4)
	_11b0b143 = String(0x11b0b143) # size 32
	_4c777e9e = String(0x4c777e9e) # size 32
	_e4b73f7d = String(0xe4b73f7d) # size 32

class ItemAct(Row):
	_ea6a09cc = Enum(0xea6a09cc, (
		('FtrLoopAuto'                 , 'FtrLoopAuto'),
		('FtrLoopFade'                 , 'FtrLoopFade'),
		('FtrLoopSwitch'               , 'FtrLoopSwitch'),
		('FtrTriggerOnOff'             , 'FtrTriggerOnOff'),
		('FtrTriggerOnce'              , 'FtrTriggerOnce'),
		('FtrTriggerToLoopOnOff'       , 'FtrTriggerToLoopOnOff'),
		('FtrTriggerToLoopWaitEndOnOff', 'FtrTriggerToLoopWaitEndOnOff'),
		('FtrChest'                    , 'FtrChest'),
		('FtrMailBox'                  , 'FtrMailBox'),
		('FtrTV'                       , 'FtrTV'),
		('FtrLoopTrigger'              , 'FtrLoopTrigger'),
		('FtrLoopTriggerWaitEndOnKeep' , 'FtrLoopTriggerWaitEndOnKeep'),
		('FtrInsectSing'               , 'FtrInsectSing'),
		('FtrActionMusicJacket'        , 'FtrMusicJacket'),
	))
	_a0839d12 = Enum(0xa0839d12, (
		('None'  , 'なし'),
		('Chair' , 'イス'),
		('Bed'   , 'ベッド'),
		('Closet', 'クローゼット'),
		('Chest' , 'タンス'),
	))
	_8b1904b9 = Enum(0x8b1904b9, (
		('Unknown'     , '未設定'),
		('MailBoxTypeA', 'ポスト：タイプA'),
		('MailBoxTypeB', 'ポスト：タイプB'),
		('MailBoxTypeC', 'ポスト：タイプC'),
		('MailBoxTypeD', 'ポスト：タイプD'),
		('MailBoxTypeE', 'ポスト：タイプE'),
	))
	UniqueID = U16(0x54706054)
	_31cb6b0a = U8(0x31cb6b0a)
	Label = String(0x87bf00e8) # string32
	_036e8ebe = String(0x036e8ebe) # size 65

class ItemClothGroup(Row):
	_e83c30be = Enum(0xe83c30be, enum_0e6ca0d4)
	_65503f9f = U16(0x65503f9f)
	UniqueID = U16(0x54706054)
	_52add71d = U8(0x52add71d)
	_47f8f099 = U8(0x47f8f099)
	_44718a37 = U8(0x44718a37)
	_97eba4fc = U8(0x97eba4fc)
	_811b386c = U8(0x811b386c)
	_93ddc6d7 = U8(0x93ddc6d7)
	_0cd7f9c5 = U8(0x0cd7f9c5)
	_1e996a76 = U8(0x1e996a76)
	_9079071d = U8(0x9079071d)
	_baa1115f = U8(0xbaa1115f)
	_8048a3a7 = U8(0x8048a3a7)
	_83ccbe0f = String(0x83ccbe0f) # size 64
	Label = String(0x13ab5198) # string64
	_036e8ebe = String(0x036e8ebe) # size 64
	_8d7f40e5 = U8(0x8d7f40e5)

class ItemColor(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 34

class ItemFilter(Row):
	_ab9b88d6 = U16(0xab9b88d6) # possible string size 2
	_d6424db4 = U16(0xd6424db4) # possible string size 2
	_eb226404 = U16(0xeb226404) # possible string size 2
	_ac821ed4 = U16(0xac821ed4) # possible string size 2
	_91e23764 = U16(0x91e23764) # possible string size 2
	_23c2eb74 = U16(0x23c2eb74) # possible string size 2
	_1ea2c2c4 = U16(0x1ea2c2c4) # possible string size 2
	_ec3bf206 = U16(0xec3bf206) # possible string size 2
	EquipGetRecipe = S16(0xd15bdbb6)
	_637b07a6 = U16(0x637b07a6) # possible string size 2
	_5e1b2e16 = U16(0x5e1b2e16) # possible string size 2
	_19bb54c6 = U16(0x19bb54c6) # possible string size 2
	_24db7d76 = U16(0x24db7d76) # possible string size 2
	_a68beaa7 = U16(0xa68beaa7) # possible string size 2
	_9bebc317 = U16(0x9bebc317) # possible string size 2
	UniqueID = U16(0x54706054)
	CheckDonation = U8(0xffe069a3)
	ItemNum = S8(0x8771aa09)
	Label = String(0x87bf00e8) # string32

class ItemFrom(Row):
	_d62525d0 = U16(0xd62525d0)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_036e8ebe = String(0x036e8ebe) # size 64

class ItemKind(Row):
	_1b936128 = Enum(0x1b936128, (
		('None'          , 'なし'),
		('OnCapture'     , 'あり'),
		('OnCaptureUIcon', 'あり(Uアイコン)'),
	))
	_d606a6c4 = Enum(0xd606a6c4, (
		('None'               , 'なし'),
		('Bells'              , 'お金'),
		('Turnip'             , 'カブ'),
		('Timer'              , 'タイマー'),
		('LostProperty'       , '落とし物'),
		('Present'            , 'プレゼント'),
		('Fassion'            , 'ファッション'),
		('HandyGoods'         , '手持ち品'),
		('Rug'                , 'ラグ'),
		('Medicine'           , 'おくすり'),
		('Insect'             , 'ムシ'),
		('Fish'               , 'サカナ・海の幸'),
		('HousingKit'         , 'ハウジングキット'),
		('UnknownFossil'      , '未鑑定化石'),
		('FishBait'           , '撒き餌'),
		('SnowCrystal'        , '雪の結晶'),
		('WallPaper'          , '壁紙'),
		('FloorBoard'         , '床板'),
		('TreasureCapsule'    , '宝探しカプセル'),
		('DoorDeco'           , 'ドア飾り'),
		('MessageBottle'      , 'メッセージボトル'),
		('DIYRecipe'          , 'レシピ'),
		('WrappingPaper'      , 'ラッピング'),
		('Fence'              , '柵'),
		('PlantKeepItemWindow', '植えるで持ち物閉じない'),
	))
	_6b749e8a = Enum(0x6b749e8a, (
		('None'      , 'なし'),
		('Ftr'       , '家具'),
		('Tool'      , '道具'),
		('Smartphone', 'スマホ'),
	))
	_29c41a0d = Enum(0x29c41a0d, (
		('99_Dummy'          , '99_Dummy'),
		('00_Ftr'            , '00_Ftr'),
		('01_Art'            , '01_Art'),
		('02_Dishes'         , '02_Dishes'),
		('10_Tops'           , '10_Tops'),
		('11_OnePiece'       , '11_OnePiece'),
		('12_Bottoms'        , '12_Bottoms'),
		('13_Socks'          , '13_Socks'),
		('14_Shoes'          , '14_Shoes'),
		('15_Cap'            , '15_Cap'),
		('16_Accessory'      , '16_Accessory'),
		('17_Helmet'         , '17_Helmet'),
		('18_Bag'            , '18_Bag'),
		('19_Umbrella'       , '19_Umbrella'),
		('20_Tool'           , '20_Tool'),
		('30_Insect'         , '30_Insect'),
		('31_Fish'           , '31_Fish'),
		('33_Shell'          , '33_Shell'),
		('34_Fossil'         , '34_Fossil'),
		('40_Plant'          , '40_Plant'),
		('41_Turnip'         , '41_Turnip'),
		('52_RoomRug'        , '52_RoomRug'),
		('61_HouseDoorDeco'  , '61_HouseDoorDeco'),
		('62_HousePost'      , '62_HousePost'),
		('70_Craft'          , '70_Craft'),
		('80_Etc'            , '80_Etc'),
		('81_Event'          , '81_Event'),
		('82_Music'          , '82_Music'),
		('83_Fence'          , '83_Fence'),
		('90_Money'          , '90_Money'),
		('50_RoomWall'       , '50_RoomWall'),
		('51_RoomFloor'      , '51_RoomFloor'),
		('84_Bromide'        , '84_Bromide'),
		('91_PhotoStudioList', '91_PhotoStudioList'),
		('85_BridgeSlope'    , '85_BridgeSlope'),
		('86_Poster'         , '86_Poster'),
		('36_InsectToy'      , '36_InsectToy'),
		('37_FishToy'        , '37_FishToy'),
	))
	_4d655154 = Enum(0x4d655154, (
		('FtrNoneUser'  , 'ユーザなし'),
		('FtrUniqueUser', '個別ユーザ'),
		('FtrCommonUser', '共通ユーザ'),
	))
	_4c9ba961 = U16(0x4c9ba961)
	_0ce69142 = U16(0x0ce69142) # possible string size 2
	UniqueID = U16(0x54706054)
	CanBury = U8(0x472724ed)
	CanEat = U8(0x9b433dd5)
	CanFtr = U8(0x90bc0855)
	CanGift = U8(0x06012035)
	_2c1b3b5b = U8(0x2c1b3b5b)
	CanNpcPresent = U8(0x0732bb98)
	CanPlant = U8(0xd4697ff8)
	CanPut = U8(0x5d389fbf)
	_d223f25c = U8(0xd223f25c)
	CanSell = U8(0x3d4f3f42)
	_b52fe52e = U8(0xb52fe52e)
	CanSetChest = U8(0xdae27694)
	CanSetCloset = U8(0x1bcd4858)
	_c8a5a762 = U8(0xc8a5a762)
	CanSetItem = U8(0x49129b27)
	_5218c48c = U8(0x5218c48c)
	_c37a683c = U8(0xc37a683c)
	_fd3b7c9a = U8(0xfd3b7c9a)
	Label = String(0x87bf00e8) # string32
	_036e8ebe = String(0x036e8ebe) # size 64

class ItemMailAttachCategoryGroup(Row):
	UniqueID = U16(0x54706054)
	_e4361c86 = String(0xe4361c86) # size 693
	Label = String(0x3febc642) # string50
	_036e8ebe = String(0x036e8ebe) # size 67

class ItemMenuIcon(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_036e8ebe = String(0x036e8ebe) # size 64
	ResName = String(0xdcfb52e8) # string32

class ItemNpcFtrActionParam(Row):
	_ae63cef0 = U32(0xae63cef0)
	_b422539e = Enum(0xb422539e, (
		('None'       , '未設定'),
		('FtrAccess'  , '家具アクセス'),
		('FtrSwitchOn', '家具スイッチ'),
		('RhythmSound', 'ノる'),
		('SingSong'   , '歌う'),
		('PlayMusic'  , '演奏する'),
	))
	_99667bf1 = Enum(0x99667bf1, (
		('None'      , 'なし'),
		('RainActive', '雨可'),
	))
	_2ca34410 = U16(0x2ca34410)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32
	_6c6fdb31 = String(0x6c6fdb31) # size 64

class ItemNpcOutfitInfo(Row):
	UniqueID = U16(0x54706054)
	_8e07b21e = U8(0x8e07b21e) # possible string size 1
	_e5c221d5 = U8(0xe5c221d5)
	Label = String(0x13ab5198) # string64
	_977adfce = String(0x977adfce) # size 32

class ItemNpcRoomReplaceCategory(Row):
	UniqueID = U16(0x54706054)
	_8a647661 = U8(0x8a647661)
	_9f9b91e9 = U8(0x9f9b91e9)
	_a604b7cf = U8(0xa604b7cf)
	_b2ac5428 = U8(0xb2ac5428)
	_ef1f311c = U8(0xef1f311c)
	_84432956 = U8(0x84432956)
	_aa4f6b89 = U8(0xaa4f6b89)
	_3594f417 = U8(0x3594f417)
	Label = String(0x87bf00e8) # string32

class ItemNpcTopsForm(Row):
	_afa7b084 = U32(0xafa7b084)
	_e807ca54 = U32(0xe807ca54) # possible string size 4
	_20e74524 = U32(0x20e74524)
	_88e75dd6 = U32(0x88e75dd6)
	_bd5eb43f = U32(0xbd5eb43f)
	_fafeceef = U32(0xfafeceef)
	_321e419f = U32(0x321e419f)
	_9a1e596d = U32(0x9a1e596d)
	_599ab542 = U32(0x599ab542)
	_1e3acf92 = U32(0x1e3acf92) # possible string size 4
	_d6da40e2 = U32(0xd6da40e2) # possible string size 4
	_7eda5810 = U32(0x7eda5810)
	_89dfed0e = U32(0x89dfed0e) # possible string size 4
	_ce7f97de = U32(0xce7f97de)
	_069f18ae = U32(0x069f18ae)
	_ae9f005c = U32(0xae9f005c)
	_d244561e = U32(0xd244561e) # possible string size 4
	_95e42cce = U32(0x95e42cce) # possible string size 4
	_5d04a3be = U32(0x5d04a3be)
	_f504bb4c = U32(0xf504bb4c)
	_c0bd52a5 = U32(0xc0bd52a5) # possible string size 4
	_871d2875 = U32(0x871d2875)
	_4ffda705 = U32(0x4ffda705)
	_e7fdbff7 = U32(0xe7fdbff7)
	_247953d8 = U32(0x247953d8) # possible string size 4
	_63d92908 = U32(0x63d92908) # possible string size 4
	_ab39a678 = U32(0xab39a678) # possible string size 4
	_0339be8a = U32(0x0339be8a)
	UniqueID = U16(0x54706054)
	_2f1b930d = String(0x2f1b930d) # size 8
	_977adfce = String(0x977adfce) # size 34

class ItemOutfitCategory(Row):
	UniqueID = U16(0x54706054)
	_7eb53ebb = U8(0x7eb53ebb)
	_555442aa = U8(0x555442aa)
	_03b7f760 = String(0x03b7f760) # size 32
	Label = String(0x87bf00e8) # string32
	Misc = U8(0x42ad246a) # size is 2, could this be an array?
	_977adfce = String(0x977adfce) # size 32
	_a9f8ee25 = String(0xa9f8ee25) # size 32
	_6ce1d85c = String(0x6ce1d85c) # size 20
	_4ec849ec = String(0x4ec849ec) # size 20
	_f71bffe7 = String(0xf71bffe7) # size 32
	_1b93daa9 = String(0x1b93daa9) # size 32
	UseToolLeft = U8(0x42739ab0) # size is 2, could this be an array?

class ItemOutfitInfo(Row):
	_90466afd = Enum(0x90466afd, (
		('None'          , 'なし'),
		('Cap'           , '帽子'),
		('AccessoryEye'  , 'アクセサリ：目'),
		('Tops'          , 'トップス'),
		('Bottoms'       , 'ボトムス'),
		('Socks'         , '靴下'),
		('Shoes'         , '靴'),
		('Scoop'         , 'スコップ'),
		('Axe'           , 'オノ'),
		('FishingRod'    , 'つりざお'),
		('Net'           , 'アミ'),
		('Umbrella'      , 'カサ'),
		('GroundMaker'   , '道造成キット'),
		('Watering'      , 'ジョウロ'),
		('Bag'           , 'カバン'),
		('CliffMaker'    , '崖造成キット'),
		('Ladder'        , 'はしご'),
		('ChangeStick'   , '変身ステッキ'),
		('Cracker'       , 'クラッカー'),
		('Slingshot'     , 'パチンコ'),
		('PinataStick'   , 'ピニャータ割り棒'),
		('FenceMaker'    , '柵造成キット'),
		('Book'          , '本'),
		('AccessoryMouth', 'アクセサリ：口'),
		('RiverMaker'    , '川造成キット'),
		('TkkGuitar'     , 'とたけけギター'),
		('PaperFan'      , 'うちわ'),
		('SmartPhone'    , 'スマホ'),
		('Firework'      , '花火'),
		('StickLight'    , 'スティックライト'),
		('SoapBubble'    , 'シャボン玉'),
		('BlowStick'     , 'ふきもどし'),
		('Ocarina'       , 'オカリナ'),
		('Panpipe'       , 'パンフルート'),
		('Tambourine'    , 'タンバリン'),
		('Broom'         , 'ほうき'),
		('Coffee'        , 'コーヒー'),
		('Ice'           , 'アイス'),
		('BagHand'       , '手提げカバン'),
		('JumpStick'     , 'ジャンプ棒'),
		('Dumbbell'      , 'ダンベル'),
		('Windmill'      , 'かざぐるま'),
		('RcmTourFlag'   , 'つぶまめツアー旗'),
		('Firewood'      , '薪'),
		('Spanner'       , 'スパナとかなづち'),
		('HandLens'      , '虫眼鏡'),
		('FruitBasket'   , '果物カゴ'),
		('Duster'        , 'はたき'),
		('CuteBagHand'   , '手提げかばん(キュート)'),
		('CoolBagHand'   , '手提げかばん(クール)'),
		('LowBagHand'    , '手提げかばん(生活度低)'),
		('HighBagHand'   , '手提げかばん(生活度高)'),
		('SmallBook'     , '本(小)'),
		('LightDumbbell' , 'ダンベル(軽い)'),
		('Candy'         , 'キャンディ'),
		('Canister'      , '缶'),
		('Sandwich'      , 'サンドウィッチ'),
		('Doughnut'      , 'ドーナッツ'),
		('Branch'        , 'えだ'),
		('Sketchbook'    , 'スケッチブック'),
		('Balloon'       , 'ふうせん'),
		('Sprayer'       , 'きりふき'),
		('Cop'           , 'コップ'),
		('Smoothie'      , 'スムージー'),
		('Hammer'        , 'かなづち'),
		('Brush'         , 'はけ'),
	))
	FloorScale = Float(0x5195e4bd)
	RotateOffsetX = Float(0xb244d814)
	RotateOffsetY = Float(0x8f24f1a4)
	_c8848b74 = U32(0xc8848b74)
	TransOffsetX = Float(0xed7f3cfe)
	TransOffsetY = Float(0xd01f154e)
	_97bf6f9e = U32(0x97bf6f9e)
	WallScale = Float(0x9f253177)
	BreakDamage = U16(0x68db76c2)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_036e8ebe = String(0x036e8ebe) # size 64
	SpecialELink = U8(0x04ac1bea)
	SpecialSLink = U8(0xbe782346)
	Storage = U8(0xc89fb7af) # size is 2, could this be an array?

class ItemParam(Row):
	_2654be7c = Enum(0x2654be7c, (
		('NoEffect', 'なし'),
		('Phono'   , 'ちくおんき'),
		('Retro'   , 'レトロ'),
		('Cheap'   , 'チープ'),
		('Hifi'    , 'ハイファイ'),
	))
	CarpetMaterial = S32(0x9c32cf82)
	_690e3379 = Enum(0x690e3379, (
		('None'                                    , '-'),
		('TopsTexTopCoatL'                         , 'トレンチコート'),
		('TopsTexTopTshirtsHKungfu'                , 'カンフーなふく'),
		('TopsTexOnepieceAlineNCheer'              , 'チアのコスチューム'),
		('TopsTexTopOuterLStajanBlue'              , 'スタジャン'),
		('TopsTexTopTshirtsHNumberball3'           , '３ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball2'           , '２ばんだまのふく'),
		('TopsTexOnepieceBalloonNSatin'            , 'サテンのワンピース'),
		('TopsTexTopTshirtsNCamisole'              , 'シンプルフリルキャミソール'),
		('TopsTexTopYshirtsLChina'                 , 'チャイナふく'),
		('TopsTexTopTshirtsLRaglan'                , 'ラグランＴシャツ'),
		('TopsTexOnepieceAlineLTweed'              , 'ツイードワンピース'),
		('TopsTexOnepieceAlineHPolkadotSpring'     , 'はるのみずたまワンピース'),
		('TopsTexOnepieceAlineNMuumuu'             , 'パインがらムームー'),
		('TopsTexOnepieceBoxLYosoiki'              , 'よそいきなふく'),
		('TopsTexOnepieceBoxNRetroGreen'           , 'レトロボックスワンピース'),
		('TopsTexTopTshirtsNBasketballshirtsPurple', 'バスケシャツ'),
		('TopsTexTopOuterNKnit'                    , 'ノースリーブのニット'),
		('TopsTexTopOuterLDownjacketBlue'          , 'ダウンジャケット'),
		('TopsTexOnepieceAlineHYumeiro'            , 'ゆめいろこうしワンピース'),
		('TopsTexOnepieceBoxLEnsembleBlue'         , 'せいそなアンサンブル'),
		('TopsTexTopYshirtsLWhite'                 , 'ワイシャツ'),
		('TopsTexOnepieceBalloonHPolkadotBlue'     , 'ベルトつきみずたまワンピース'),
		('TopsTexTopTshirtsHSailor'                , 'はんそでセーラーふく'),
		('TopsTexTopOuterLParkaGray'               , 'シンプルなパーカー'),
		('TopsTexTopTshirtsLSmockTulip'            , 'スモック'),
		('TopsTexOnepieceAlineHFlowerPink'         , 'はながらワンピース'),
		('TopsTexOnepieceBalloonLLolita'           , 'ロリータなワンピース'),
		('SocksTexTights'                          , 'ストッキング'),
		('SocksTexAmitights'                       , 'あみタイツ'),
		('TopsTexOnepieceBoxLChidori'              , 'ちどりごうしワンピース'),
		('TopsTexOnepieceBoxHParty'                , 'パーティーワンピ'),
		('TopsTexOnepieceBoxLBubbly'               , 'バブリーなセットアップ'),
		('TopsTexOnepieceBalloonNXmasRed'          , 'クリスマスなドレス'),
		('TopsTexOnepieceBalloonHHoodRed'          , 'メルヘンなドレス'),
		('TopsTexOnepieceBalloonHMaid'             , 'メイドのふく'),
		('TopsTexTopCoatLAcademicdress'            , 'がくしのふく'),
		('TopsTexOnepieceBalloonHWaitress'         , 'ダイナーのユニフォーム'),
		('TopsTexTopYshirtsHWhite'                 , 'はんそでワイシャツ'),
		('TopsTexTopYshirtsNWhite'                 , 'ノースリーブえりつきシャツ'),
		('TopsTexOnepieceAlineLRabbit'             , 'ウサギなふく'),
		('TopsTexOnepieceAlineLHeroine'            , 'ヒロインスーツ'),
		('TopsTexTopCoatLHanten'                   , 'はんてん'),
		('TopsTexOnepieceBoxLBathrobes'            , 'バスローブ'),
		('TopsTexOnepieceBalloonNBallet'           , 'バレエのいしょう'),
		('TopsTexOnepieceAlineLCat'                , 'ネコなふく'),
		('TopsTexOnepieceBalloonHTyrolean'         , 'チロリアンなドレス'),
		('TopsTexOnepieceAlineNXmastreeNormal'     , 'もみのきワンピース'),
		('TopsTexTopCoatLRain'                     , 'レインコート'),
		('TopsTexTopCoatLNoble'                    , 'きぞくのコート'),
		('TopsTexTopYshirtsHPolo'                  , 'ポロシャツ'),
		('TopsTexTopCoatLWhitecoat'                , 'はくい'),
		('TopsTexTopCoatHCock'                     , 'コックさんのふく'),
		('TopsTexTopCoatLCafe'                     , 'カフェのせいふく'),
		('TopsTexTopTshirtsHGym'                   , 'たいそうふく'),
		('TopsTexTopTshirtsNTanktop'               , 'タンクトップ'),
		('TopsTexTopYshirtsLComedian'              , 'コメディアンなふく'),
		('TopsTexTopYshirtsLRiders'                , 'ライダースジャケット'),
		('TopsTexTopTshirtsNCamisoleprint'         , 'はながらのプリントキャミ'),
		('TopsTexTopYshirtsLDenim'                 , 'デニムジャケット'),
		('TopsTexTopCoatHRubberapron'              , 'ゴムエプロン'),
		('TopsTexTopTshirtsHFishing'               , 'つりジャケット'),
		('TopsTexTopCoatLMouton'                   , 'ムートンコート'),
		('TopsTexTopYshirtsLFlannel'               , 'ネルシャツ'),
		('TopsTexTopYshirtsNDenim'                 , 'そでなしＧジャン'),
		('TopsTexTopCoatHApron'                    , 'エプロン'),
		('TopsTexTopCoatLInfantry'                 , 'へいたいのふく'),
		('TopsTexOnepieceBoxNPrimitive'            , 'げんしじんなふく'),
		('TopsTexTopCoatLGunknight'                , 'じゅうきしのふく'),
		('TopsTexTopYshirtsHAloha'                 , 'パインがらアロハシャツ'),
		('TopsTexTopTshirtsNCamisolelace'          , 'レースのキャミソール'),
		('TopsTexTopOuterLJersey'                  , 'ジャージ'),
		('TopsTexTopYshirtsLWestern'               , 'ウェスタンなふく'),
		('TopsTexTopTshirtsNEkiden'                , 'えきでんなふく'),
		('TopsTexTopYshirtsHChina'                 , 'はんそでチャイナふく'),
		('TopsTexTopTshirtsHSoccer'                , 'サッカーのユニフォーム'),
		('TopsTexTopOuterLSukajantiger'            , 'トラのスカジャン'),
		('TopsTexTopYshirtsHHappi'                 , 'はっぴ'),
		('TopsTexTopOuterLSukajandragon'           , 'ドラゴンのスカジャン'),
		('TopsTexTopTshirtsHCamouflage'            , 'めいさいなふく'),
		('TopsTexTopTshirtsHCycle'                 , 'サイクルジャージ'),
		('TopsTexTopTshirtsHChick'                 , 'ひよこがらＴシャツ'),
		('TopsTexOnepieceDressLPrincess'           , 'プリンセスなふく'),
		('TopsTexOnepieceRibNKnit'                 , 'そでなしニットワンピ'),
		('TopsTexTopYshirtsLArgyle'                , 'アーガイルベスト'),
		('TopsTexTopYshirtsHExplorer'              , 'たんけんふく'),
		('TopsTexTopYshirtsLJacketgaudy'           , 'ハデなジャケット'),
		('TopsTexTopYshirtsLNecktie'               , 'ネクタイつきワイシャツ'),
		('TopsTexTopCoatHItamae'                   , 'いたまえのふく'),
		('TopsTexTopYshirtsLBlazer'                , 'ブレザー'),
		('TopsTexTopCoatLKing'                     , 'おうさまのふく'),
		('TopsTexOnepieceAlineNStrawberry'         , 'イチゴのふく'),
		('TopsTexOnepieceAlineNWatermelon'         , 'スイカのふく'),
		('TopsTexOnepieceAlineNOrange'             , 'オレンジのふく'),
		('TopsTexOnepieceAlineNKiwi'               , 'キウイのふく'),
		('TopsTexOnepieceAlineNGrape'              , 'ぶどうのふく'),
		('TopsTexOnepieceAlineNPineapple'          , 'パイナップルのふく'),
		('BottomsTexPantsNormalSweat'              , 'スウェットパンツ'),
		('BottomsTexSkirtAlineTweed'               , 'ツイードスカート'),
		('BottomsTexPantsNormalLeather'            , 'レザーパンツ'),
		('BottomsTexPantsNormalSlacks'             , 'スラックス'),
		('BottomsTexPantsNormalJersey'             , 'ジャージズボン'),
		('BottomsTexPantsNormalBoder'              , 'ボーダーパンツ'),
		('BottomsTexPantsNormalDenimholes'         , 'あなあきデニム'),
		('TopsTexTopYshirtsLTwotone'               , 'ツートンのエリつきシャツ'),
		('TopsTexTopTshirtsHNumberball1'           , '１ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball4'           , '４ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball5'           , '５ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball6'           , '６ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball7'           , '７ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball8'           , '８ばんだまのふく'),
		('TopsTexTopTshirtsHNumberball9'           , '９ばんだまのふく'),
		('TopsTexTopYshirtsLTiedsweater'           , 'トレンディーなふく'),
		('TopsTexTopYshirtsLSportsjersey'          , 'スポーツジャージ'),
		('BottomsTexPantsNormalSportsjersey'       , 'スポーツジャージのズボン'),
		('BottomsTexSkirtAlineKilt'                , 'キルト'),
		('TopsTexTopYshirtsLGilet'                 , 'ベストつきワイシャツ'),
		('BottomsTexSkirtAlineSailorNavy'          , 'セーラーふくのスカート'),
		('BottomsTexPantsNormalCamouflage'         , 'めいさいパンツ'),
		('TopsTexOnepieceBoxHNurse'                , 'かんごしのワンピース'),
		('TopsTexTopYshirtsHNurse'                 , 'かんごしのジャケット'),
		('BottomsTexPantsWideCargo'                , 'カーゴパンツ'),
		('BottomsTexPantsWideSusomise'             , 'すそみせズボン'),
		('TopsTexOnepieceOverallLPajama'           , 'パジャマ'),
		('TopsTexTopTshirtsNBorder'                , 'ボーダーのタンクトップ'),
		('BottomsTexSkirtAlineLace'                , 'レーススカート'),
		('TopsTexOnepieceBalloonLCorsetPurple'     , 'コルセットドレス'),
		('TopsTexOnepieceBoxLShirt'                , 'シャツワンピ'),
		('TopsTexOnepieceAlineNShirt'              , 'そでなしシャツワンピ'),
		('TopsTexTopYshirtsLTuxedo'                , 'タキシード'),
		('TopsTexTopCoatLMorningcoat'              , 'モーニングコート'),
		('BottomsTexPantsWideSchool'               , 'せいふくのズボン'),
		('BottomsTexPantsNormalSlacksgaudy'        , 'ハデなスラックス'),
		('TopsTexOnepieceOverallLJockey'           , 'ジョッキーのふく'),
		('TopsTexOnepieceOverallLBear'             , 'クマなふく'),
		('TopsTexOnepieceOverallLFirefighter'      , 'しょうぼうしのふく'),
		('TopsTexOnepieceOverallLFrog'             , 'カエルなふく'),
		('TopsTexOnepieceOverallLKappa'            , 'カッパスーツ'),
		('TopsTexOnepieceDressLClassic'            , 'アントワネットなドレス'),
		('TopsTexOnepieceAlongNNile'               , 'ナイルなふく'),
		('TopsTexOnepieceOverallLWorkwear'         , 'さぎょうぎ'),
		('TopsTexOnepieceOverallLClown'            , 'ピエロのふく'),
		('TopsTexOnepieceOverallLHero'             , 'ヒーロースーツ'),
		('TopsTexOnepieceOverallHJinbei'           , 'じんべい'),
		('TopsTexOnepieceOverallLNinja'            , 'しのびのふく'),
		('TopsTexOnepieceOverallLDragon'           , 'ドラゴンスーツ'),
		('BottomsTexPantsWideCowboy'               , 'カウボーイパンツ'),
		('TopsTexOnepieceOverallLHotel'            , 'ホテルマンなふく'),
		('TopsTexTopYshirtsLTailored'              , 'テーラードジャケット'),
		('TopsTexOnepieceBoxLAttendant'            , 'フライトアテンダントのふく'),
		('TopsTexTopYshirtsLVest'                  , 'チョッキつきワイシャツ'),
		('TopsTexOnepieceAlongLWitch'              , 'まほうつかいのローブ'),
		('TopsTexOnepieceBlongLAodai'              , 'アオザイ'),
		('TopsTexOnepieceBlongLKappogi'            , 'かっぽうぎ'),
		('TopsTexOnepieceAlongLChimachogori'       , 'チマチョゴリ'),
		('AccessoryMouthBeakYellow'                , 'くちばし'),
		('AccessoryMouthBeard'                     , 'カイゼルひげ'),
		('TopsTexOnepieceOverallLPolice'           , 'けいかんのふく'),
		('TopsTexOnepieceBlongHToga'               , 'ローマなふく'),
		('TopsTexOnepieceKimonoLUme'               , 'ウメがらのきもの'),
		('TopsTexOnepieceAlongLGothic'             , 'ゴシックなふく'),
		('TopsTexOnepieceBoxNGreece'               , 'ギリシャなふく'),
		('TopsTexTopTshirtsHKanji'                 , 'かんじＴシャツ'),
		('TopsTexOnepieceAlineLMold'               , 'かびたワンピース'),
		('TopsTexOnepieceBlongHEgypt'              , 'エジプトのふく'),
		('TopsTexTopYshirtsLCardiganyshirt'        , 'カーディガン&シャツ'),
		('TopsTexTopOuterLArgyle'                  , 'アーガイルのセーター'),
		('TopsTexTopOuterLFlowerknit'              , 'はながらのニット'),
		('TopsTexTopOuterLTennis'                  , 'テニスセーター'),
		('TopsTexOnepieceOverallNArabia'           , 'アラビアなふく'),
		('TopsTexOnepieceOverallLMummy'            , 'ほうたいのふく'),
		('TopsTexOnepieceOverallLBone'             , 'ボーンなふく'),
		('TopsTexOnepieceOverallNWrestling'        , 'プロレススーツ'),
		('TopsTexOnepieceOverallLBaseball'         , 'やきゅうのふく'),
		('TopsTexOnepieceOverallLPilot'            , 'きちょうのふく'),
		('TopsTexOnepieceOverallLBull'             , 'マタドールなふく'),
		('TopsTexOnepieceDressHHolland'            , 'オランダなドレス'),
		('TopsTexTopOuterLNordic'                  , 'ノルディックなセーター'),
		('TopsTexTopOuterLSnow'                    , 'スノーセーター'),
		('TopsTexTopOuterLNordiccardigan'          , 'ノルディックなカーディガン'),
		('TopsTexTopOuterLAran'                    , 'アランセーター'),
		('TopsTexTopOuterLYumekawa'                , 'ゆめかわなセーター'),
		('TopsTexOnepieceOverallLSpace'            , 'うちゅうふく'),
		('TopsTexTopOuterLArancardigan'            , 'アランカーディガン'),
		('TopsTexOnepieceOverallLRacer'            , 'レーサーなふく'),
		('TopsTexOnepieceAlineHSuspendersskirt'    , 'つりスカート'),
		('TopsTexOnepieceBoxLJumperskirtuniform'   , 'ジャンパースカートのせいふく'),
		('TopsTexTopCoatLNocollar'                 , 'ノーカラーコート'),
		('TopsTexTopYshirtsLRugby'                 , 'ラガーシャツ'),
		('TopsTexOnepieceOverallLSaropetto'        , 'デニムのサロペット'),
		('TopsTexTopOuterLSweat'                   , 'シンプルなトレーナー'),
		('TopsTexOnepieceBalloonHMarine'           , 'マリンルックワンピース'),
		('TopsTexTopTshirtsLHenley'                , 'ヘンリーネックＴシャツ'),
		('TopsTexTopTshirtsHGillet'                , 'ジレコーデＴシャツ'),
		('TopsTexTopCoatHStripeshirts'             , 'オーバーストライプシャツ'),
		('TopsTexTopCoatLCoverall'                 , 'カバーオール'),
		('TopsTexOnepieceBlongHSally'              , 'サリー'),
		('TopsTexOnepieceBalloonHStrange'          , 'ふしぎなワンピース'),
		('TopsTexTopYshirtsHCuba'                  , 'キューバシャツ'),
		('TopsTexTopCoatLPcoat'                    , 'ピーコート'),
		('TopsTexTopYshirtsLNocollar'              , 'ノーカラーシャツ'),
		('TopsTexTopYshirtsLWork'                  , 'ワークシャツ'),
		('TopsTexOnepieceAlongLBustier'            , 'ビスチェワンピース'),
		('TopsTexTopYshirtsHBowling'               , 'ボウリングシャツ'),
		('TopsTexTopTshirtsLVnecksweater'          , 'Ｖネックセーター'),
		('TopsTexOnepieceBalloonNFairy'            , 'ようせいのふく'),
		('ShoesSandalGetaBlack'                    , 'げた'),
		('TopsTexTopYshirtsLFleece'                , 'ボアフリース'),
		('TopsTexTopYshirtsLTweed'                 , 'ツイードジャケット'),
		('TopsTexOnepieceOverallLSuspenders'       , 'サスペンダーなふく'),
		('BottomsTexPantsWideTweed'                , 'ツイードパンツ'),
		('TopsTexTopTshirtsLLayeredtshirts'        , 'かさねぎＴシャツ'),
		('TopsTexTopTshirtsHLace'                  , 'レースのシャツ'),
		('TopsTexTopCoatLChester'                  , 'チェスターコート'),
		('TopsTexTopCoatLChestercheck'             , 'チェックのチェスターコート'),
		('BottomsTexPantsHalfCargo'                , 'ハーフカーゴパンツ'),
		('TopsTexTopTshirtsHBigstole'              , 'おおばんストールＴシャツ'),
		('TopsTexOnepieceOverallHDwarf'            , 'こびとのふく'),
		('BottomsTexPantsHotRunning'               , 'ランニングパンツ'),
		('TopsTexTopYshirtsLPrince'                , 'おうじさまシャツ'),
		('TopsTexTopTshirtsNFitness'               , 'フィットネスタンクトップ'),
		('TopsTexTopOuterLFlight'                  , 'フライトジャケット'),
		('TopsTexTopTshirtsHTiedye'                , 'タイダイＴシャツ'),
		('TopsTexTopYshirtsLBoavest'               , 'ボアベスト'),
		('TopsTexTopCoatLQuilting'                 , 'キルティングダウン'),
		('BottomsTexSkirtLongPleats'               , 'ロングプリーツスカート'),
		('BottomsTexSkirtAlineTennis'              , 'テニススカート'),
		('AccessoryGlass'                          , 'まるめがね'),
		('AccessoryGlassSquare'                    , 'スクエアめがね'),
		('AccessoryGlassHeart'                     , 'ハートのサングラス'),
		('AccessoryGlassThurmont'                  , 'サーモントめがね'),
		('AccessoryGlassOctagon'                   , 'オクタゴンめがね'),
		('AccessoryGlassStar'                      , 'ほしのサングラス'),
		('AccessoryGlassBoston'                    , 'ボストンめがね'),
		('AccessoryGlassTriangle'                  , 'さんかくサングラス'),
		('BottomsTexSkirtBoxDenim'                 , 'デニムスカート'),
		('TopsTexTopTshirtsLPeasant'               , 'ペザントブラウス'),
		('TopsTexOnepieceAlongHNegligee'           , 'ネグリジェ'),
		('TopsTexOnepieceOverallLJudo'             , 'じゅうどうぎ'),
		('BottomsTexPantsHotDenimholes'            , 'あなあきショートデニム'),
		('BottomsTexSkirtLongDot'                  , 'みずたまロングスカート'),
		('TopsTexTopTshirtsNTubetop'               , 'チューブトップ'),
		('BottomsTexPantsWideHickory'              , 'ヒッコリーのペインターパンツ'),
		('BottomsTexPantsNormalChain'              , 'チェーンつきパンツ'),
		('BottomsTexPantsNormalDown'               , 'ダウンパンツ'),
		('BottomsTexSkirtLongChino'                , 'ロングチノスカート'),
		('TopsTexOnepieceAlineLBorder'             , 'ボーダーワンピース'),
		('AccessoryGlassDoublebridge'              , 'ダブルブリッジめがね'),
		('TopsTexOnepieceAlineHLinen'              , 'リネンワンピース'),
		('BottomsTexSkirtBoxDown'                  , 'ダウンスカート'),
		('TopsTexTopTshirtsNMuscle'                , 'マッスルタンクトップ'),
		('TopsTexOnepieceKimonoLWizard'            , 'まじゅつしのローブ'),
		('BottomsTexPantsHotDenim'                 , 'デニムショートパンツ'),
		('TopsTexTopTshirtsHBorder'                , 'はんそでボーダーＴシャツ'),
		('TopsTexTopOuterLDownvest'                , 'ダウンベスト'),
		('AccessoryGlassBottle'                    , 'ビンぞこめがね'),
		('BottomsTexSkirtBoxSweat'                 , 'スウェットスカート'),
		('TopsTexTopYshirtsLCoach'                 , 'コーチジャケット'),
		('TopsTexTopCoatLGowncoat'                 , 'ガウンコート'),
		('TopsTexTopTshirtsLChidori'               , 'ちどりのカーディガン'),
		('TopsTexOnepieceAlineNHalterneckstripe'   , 'ホルターネックのワンピース'),
		('TopsTexTopTshirtsHPocketshirts'          , 'ポケットつきＴシャツ'),
		('TopsTexOnepieceKimonoLMiko'              , 'みこしょうぞく'),
		('BottomsTexSkirtBoxCorduroy'              , 'コーデュロイスカート'),
		('BottomsTexPantsWideGaucho'               , 'ガウチョパンツ'),
		('TopsTexOnepieceBoxNModern'               , 'モガなワンピース'),
		('TopsTexTopYshirtsLSlimknit'              , 'スリムニット'),
		('BottomsTexSkirtBoxLeather'               , 'レザースカート'),
		('TopsTexTopOuterLCollegecardigan'         , 'カレッジカーディガン'),
		('BottomsTexSkirtBoxFringe'                , 'フリンジスカート'),
		('TopsTexOnepieceKimonoLHakama'            , 'はかま'),
		('TopsTexTopTshirtsHKnot'                  , 'まえむすびＴシャツ'),
		('TopsTexOnepieceOverallLTights'           , 'ぜんしんタイツ'),
		('BottomsTexPantsWideDenim'                , 'デニムのペインターパンツ'),
		('TopsTexTopTshirtsHGoldprint'             , 'ゴールドプリントＴシャツ'),
		('TopsTexOnepieceOverallLWaders'           , 'ウェーダー'),
		('BottomsTexPantsNormalChinashort'         , 'チャイナなクロップドパンツ'),
		('BottomsTexPantsNormalChina'              , 'チャイナなズボン'),
		('BottomsTexPantsWideKungfu'               , 'カンフーなズボン'),
		('TopsTexOnepieceBalloonHMagical'          , 'マジカルなドレス'),
		('BottomsTexSkirtBoxGrass'                 , 'こしみの'),
		('TopsTexOnepieceAlineLBolerocoat'         , 'ボレロコート'),
		('TopsTexOnepieceBoxLOffice'               , 'オフィスなふく'),
		('AccessoryGlassCrack'                     , 'ヒビわれめがね'),
		('TopsTexTopTshirtsLAlphabet'              , 'えいじＴシャツ'),
		('TopsTexOnepieceAlongNPearl'              , 'パールつきロングドレス'),
		('TopsTexOnepieceKimonoLKinagashi'         , 'きながし'),
		('TopsTexTopOuterLSukajanhawk'             , 'タカのスカジャン'),
		('TopsTexOnepieceBalloonHSimple'           , 'しっそなドレス'),
		('TopsTexOnepieceOverallLSimple'           , 'しっそなふく'),
		('TopsTexOnepieceBalloonNBunny'            , 'タキシードドレス'),
		('TopsTexOnepieceOverallLFleecepajama'     , 'フリースパジャマ'),
		('TopsTexOnepieceAlongLLeathercoat'        , 'レザーコート'),
		('TopsTexOnepieceBoxNBathtowel'            , 'バスタオル'),
		('TopsTexTopYshirtsLSuitsmen'              , 'スーツ'),
		('BottomsTexPantsWideBellbottoms'          , 'ベルボトムパンツ'),
		('TopsTexTopYshirtsLGakuran'               , 'がくせいふく'),
		('TopsTexTopYshirtsLGakuranopen'           , 'ヤンチャながくせいふく'),
		('TopsTexTopCoatLPoncho'                   , 'ポンチョコート'),
		('BottomsTexPantsWideFrilled'              , 'フリルつきパンツ'),
		('BottomsTexPantsHotYacht'                 , 'ヨットのショートパンツ'),
		('BottomsTexPantsHalfMulticolor'           , 'マルチカラーのハーフパンツ'),
		('BottomsTexPantsHalfFormal'               , 'きれいめハーフパンツ'),
		('BottomsTexSkirtBoxLeopard'               , 'ヒョウがらミニスカート'),
		('BottomsTexSkirtLongCheck'                , 'チェックのロングスカート'),
		('TopsTexTopCoatLVampire'                  , 'ヴァンパイアのふく'),
		('TopsTexOnepieceBoxLAutumncheck'          , 'あきいろチェックワンピース'),
		('BottomsTexPantsNormalNoble'              , 'きぞくのズボン'),
		('TopsTexOnepieceBalloonNBlockcheck'       , 'ブロックチェックワンピ'),
		('TopsTexTopOuterLMaone'                   , 'ＭＡ‐１'),
		('TopsTexTopOuterLCamo'                    , 'めいさいのＭＡ‐１'),
		('TopsTexOnepieceAlongLFrilled'            , 'フリフリワンピース'),
		('BottomsTexPantsHalfAloha'                , 'パインがらアロハパンツ'),
		('TopsTexOnepieceBalloonNIdleeightys'      , 'アイドルなふく'),
		('TopsTexTopYshirtsLHanten'                , 'うみのはんてん'),
		('BottomsTexPantsNormalCropped'            , 'クロップドパンツ'),
		('TopsTexOnepieceBoxLBohemian'             , 'ボヘミアンワンピ'),
		('BottomsTexSkirtAlineFrilled'             , 'フリルスカート'),
		('TopsTexTopOuterLMohair'                  , 'モヘアふうニット'),
		('TopsTexTopOuterLSpaceparker'             , 'スペースパーカー'),
		('TopsTexTopTshirtsHBaseball'              , 'ベースボールシャツ'),
		('TopsTexTopCoatLInparker'                 , 'パーカーオンコート'),
		('TopsTexTopTshirtsNTraining'              , 'ワークアウトトップス'),
		('TopsTexTopCoatLMod'                      , 'モッズコート'),
		('TopsTexTopOuterLParkertshirt'            , 'パーカーオンＴシャツ'),
		('TopsTexOnepieceRibLSwitchsweat'          , 'きりかえビッグスウェット'),
		('AccessoryGlassMask'                      , 'アイマスク'),
		('BottomsTexSkirtAlineTweedfrill'          , 'ツイードフリルスカート'),
		('TopsTexTopCoatLHeartapron'               , 'ハートのエプロン'),
		('BottomsTexPantsWideEasy'                 , 'ワイドイージーパンツ'),
		('TopsTexOnepieceRibNSheep'                , 'ひつじなふく'),
		('TopsTexOnepieceBalloonNSunflower'        , 'ひまわりのワンピース'),
		('TopsTexTopCoatLPrince'                   , 'プリンスなふく'),
		('BottomsTexSkirtBoxCamo'                  , 'めいさいスカート'),
		('TopsTexTopYshirtsHTraffic'               , 'こうつうゆうどうのふく'),
		('TopsTexTopCoatLTailcoat'                 , 'えんびふく'),
		('TopsTexOnepieceOverallHTyrolean'         , 'チロリアンなオーバーオール'),
		('BottomsTexPantsHotCulotte'               , 'キュロット'),
		('TopsTexTopOuterLNative'                  , 'ネイティブニット'),
		('TopsTexTopTshirtsHAmericanfootball'      , 'アメフトシャツ'),
		('TopsTexTopYshirtsLSki'                   , 'スキーウェア'),
		('TopsTexOnepieceOverallLStarsinger'       , 'スタアのふく'),
		('BottomsTexPantsWideSki'                  , 'スキーウェアのズボン'),
		('AccessoryMouthMask'                      , 'マスク'),
		('AccessoryGlassEyepatch'                  , 'がんたい'),
		('AccessoryGlassGogglesski'                , 'スキーゴーグル'),
		('AccessoryGlassGoggles'                   , 'すいえいゴーグル'),
		('AccessoryGlassRetro'                     , 'レトロなサングラス'),
		('AccessoryGlassPatch'                     , 'アイパッチ'),
		('AccessoryGlassSports'                    , 'スポーツサングラス'),
		('AccessoryGlassPilot'                     , 'パイロットサングラス'),
		('AccessoryGlassTortoiseshell'             , 'べっこうめがね'),
		('AccessoryGlassMini'                      , 'ちいさいサングラス'),
		('AccessoryGlassMonocle'                   , 'モノクル'),
		('AccessoryGlassThreed'                    , '3Dめがね'),
		('AccessoryGlassBlind'                     , 'ブラインドサングラス'),
		('TopsTexTopCoatLAnimal'                   , 'フェイクアニマルコート'),
		('TopsTexOnepieceBoxNLayered'              , 'レイヤーノースリーブワンピ'),
		('TopsTexOnepieceBoxHTiger'                , 'トラのＴシャツワンピ'),
		('TopsTexOnepieceRibLParkershirt'          , 'パーカーインシャツワンピ'),
		('TopsTexTopCoatLRetro'                    , 'レトロなコート'),
		('TopsTexOnepieceOverallLRompers'          , 'ロンパース'),
		('TopsTexOnepieceOverallLBondage'          , 'ボンテージ'),
		('BottomsTexPantsHalfOutdoor'              , 'アウトドアパンツ'),
		('TopsTexOnepieceOverallLSuper'            , 'スーパーヒーロースーツ'),
		('AccessoryMouthCat'                       , 'ネコのつけばな'),
		('TopsTexOnepieceDressHChinapoblana'       , 'チナポブラーナ'),
		('BottomsTexPantsNormalBondage'            , 'ボンテージパンツ'),
		('TopsTexTopTshirtsNHula'                  , 'フラダンスなトップス'),
		('BottomsTexPantsHalfEthnic'               , 'エスニックパンツ'),
		('TopsTexTopCoatLHippie'                   , 'ヒッピーなふく'),
		('TopsTexOnepieceRibLShawl'                , 'ショールコーデワンピ'),
		('BottomsTexPantsWideKnee'                 , 'ひざあてズボン'),
		('AccessoryMouthCucumber'                  , 'きゅうりパック'),
		('AccessoryGlassmouthNose'                 , 'つけばな'),
		('AccessoryGlassmouthBeard'                , 'ヒゲメガネ'),
		('BottomsTexSkirtLongTiered'               , 'ティアードスカート'),
		('TopsTexTopYshirtsLCareer'                , 'キャリアなジャケット'),
		('BottomsTexSkirtBoxCareer'                , 'キャリアなスカート'),
		('BottomsTexSkirtLongDrape'                , 'ドレープスカート'),
		('TopsTexOnepieceBalloonHDolly'            , 'ドーリーワンピース'),
		('TopsTexTopYshirtsLChimayo'               , 'チマヨベスト'),
		('AccessoryGlassBirthday'                  , 'バースデーサングラス'),
		('AccessoryGlassmouthPack'                 , 'パック'),
		('AccessoryGlassEyes'                      , 'をかしなめがね'),
		('BottomsTexPantsNormalCycle'              , 'サイクルボトム'),
		('BottomsTexPantsHalfSurf'                 , 'サーフパンツ'),
		('BottomsTexPantsHotLace'                  , 'レースショートパンツ'),
		('BottomsTexPantsHalfJersey'               , 'ジャージショートパンツ'),
		('TopsTexTopCoatLKuruta'                   , 'クルタ'),
		('TopsTexOnepieceBlongLShirt'              , 'ロングシャツワンピ'),
		('TopsTexTopOuterLPullover'                , 'プルオーバーアウター'),
		('BottomsTexPantsHotThai'                  , 'ムエタイパンツ'),
		('BottomsTexPantsHotDotgold'               , 'ゴールドドットパンツ'),
		('TopsTexTopYshirtsLTweedvest'             , 'ツイードベスト'),
		('BottomsTexSkirtLongWrap'                 , 'ベルトのまきスカート'),
		('BottomsTexSkirtLongEmbroidery'           , 'ししゅうのはながらスカート'),
		('BottomsTexSkirtLongGeometric'            , 'きかがくししゅうのスカート'),
		('AccessoryGlassCyber'                     , 'サイバーサングラス'),
		('TopsTexTopOuterLMuffler'                 , 'チェックマフラーつきセーター'),
		('TopsTexTopCoatLMuffler'                  , 'ロングデニムカーディガン'),
		('TopsTexOnepieceBoxNStandard'             , 'おおばんがらワンピ'),
		('TopsTexOnepieceAlineLRetro'              , 'レトロＡラインワンピース'),
		('TopsTexTopCoatHWaistshirt'               , 'こしまきシャツ'),
		('TopsTexOnepieceBoxHTshirts'              , 'Ｔシャツワンピ'),
		('TopsTexTopCoatNSequins'                  , 'ラメししゅうノースリーブ'),
		('TopsTexOnepieceOverallLVisual'           , 'ヴィジュアルけいコスチューム'),
		('TopsTexTopCoatLLeathertrench'            , 'レザートレンチ'),
		('TopsTexTopOuterLReindeer'                , 'トナカイセーター'),
		('TopsTexTopYshirtsHKnot'                  , 'まえむすびＹシャツ'),
		('TopsTexOnepieceBalloonHLace'             , 'はながらレースのワンピース'),
		('TopsTexTopCoatLSoutiencollar'            , 'ステンカラーコート'),
		('TopsTexTopOuterLHighsence'               , 'ハイセンスなセーター'),
		('TopsTexTopYshirtsLCowboy'                , 'カウボーイシャツ'),
		('TopsTexOnepieceRibNCaterpillar'          , 'あおむしのふく'),
		('TopsTexTopYshirtsLBustier'               , 'ビスチェキャミ'),
		('TopsTexOnepieceBoxLHouse'                , 'ハウスなプリントワンピ'),
		('TopsTexOnepieceBoxLForest'               , 'フォレストなワンピース'),
		('TopsTexOnepieceOverallHRugby'            , 'ラグビーのユニフォーム'),
		('TopsTexOnepieceOverallLPlatearmorIron'   , 'アイアンアーマー'),
		('TopsTexOnepieceAlongLDowncoat'           , 'ロングダウンコート'),
		('TopsTexOnepieceOverallLPlatearmorGold'   , 'ゴールデンアーマー'),
		('BottomsTexPantsWideSatin'                , 'サテンのパンツ'),
		('TopsTexOnepieceAlineLPcoat'              , 'スカートつきピーコート'),
		('TopsTexTopOuterLRainbow'                 , 'レインボーなニット'),
		('TopsTexOnepieceAlongHCachecoeur'         , 'カシュクールワンピース'),
		('AccessoryGlassLoose'                     , 'アンダーリムめがね'),
		('TopsTexTopOuterLBlouson'                 , 'ボアブルゾン'),
		('TopsTexTopCoatNShirt'                    , 'チュニックシャツ'),
		('AccessoryMouthRabbit'                    , 'ウサギのつけばな'),
		('TopsTexTopCoatLCoadigan'                 , 'コーディガン'),
		('BottomsTexPantsWideCorduroy'             , 'コーデュロイボトム'),
		('TopsTexOnepieceOverallLVolendam'         , 'オランダなコスチューム'),
		('TopsTexOnepieceRibLBore'                 , 'ボアパーカー'),
		('TopsTexTopCoatLPatchwork'                , 'パッチワークコート'),
		('TopsTexOnepieceBlongLBalmakarn'          , 'バルマカーンコート'),
		('AccessoryGlassRound'                     , 'ラウンドサングラス'),
		('AccessoryGlassButterfly'                 , 'バタフライサングラス'),
		('AccessoryGlassOval'                      , 'オーバルめがね'),
		('TopsTexTopTshirtsLEarphone'              , 'イヤフォンコーデ'),
		('TopsTexOnepieceOverallHArabia'           , 'アラビアひめなふく'),
		('BottomsTexSkirtBoxLace'                  , 'はながらレースのスカート'),
		('TopsTexTopTshirtsLMulti'                 , 'マルチボーダーニット'),
		('BottomsTexSkirtAlineFlare'               , 'フレアスカート'),
		('TopsTexTopYshirtsHMadras'                , 'マドラスチェックシャツ'),
		('TopsTexOnepieceAlongNEthnic'             , 'エスニックワンピ'),
		('TopsTexOnepieceOverallNCombinaison'      , 'ショートコンビネゾン'),
		('AccessoryGlassDot'                       , 'ドットサングラス'),
		('AccessoryMouthPig'                       , 'ブタのつけばな'),
		('TopsTexOnepieceKimonoLIcequeen'          , 'こおりのじょおうなドレス'),
		('AccessoryGlassmouthGasmask'              , 'ガスマスク'),
		('TopsTexOnepieceDressLNordic'             , 'さむいくにのドレス'),
		('AccessoryMouthRice'                      , 'ごはんつぶ'),
		('TopsTexOnepieceOverallLMariachi'         , 'マリアッチのいしょう'),
		('TopsTexOnepieceBoxLMarble'               , 'マーブルワンピース'),
		('TopsTexOnepieceAlongNMermaid'            , 'かいがらのドレス'),
		('TopsTexOnepieceBlongLHippie'             , 'ポンチョふうニット'),
		('AccessoryGlassVenetian'                  , 'ベネチアンマスク'),
		('TopsTexTopCoatNTanktunic'                , 'タンクトップチュニック'),
		('AccessoryGlassWood'                      , 'ウッドフレームめがね'),
		('AccessoryMouthCrow'                      , 'カラスマスク'),
		('AccessoryMouthRollingmustache'           , 'まきヒゲ'),
		('TopsTexOnepieceRibLCardigan'             , 'モールロングカーディガン'),
		('TopsTexTopYshirtsNRibnoncami'            , 'リボンショルダーキャミ'),
		('AccessoryMouthBeardChin'                 , 'アゴひげ'),
		('AccessoryMouthBandage'                   , 'ばんそうこう'),
		('AccessoryGlassmouthPierrot'              , 'ピエロのかめん'),
		('AccessoryMouthBeardRound'                , 'ラウンドひげ'),
		('TopsTexTopOuterLFleece'                  , 'がらものフリース'),
		('TopsTexTopCoatLDetective'                , 'めいたんていのふく'),
		('AccessoryMouthLeaf'                      , 'はっぱ'),
		('AccessoryGlassRhinestone'                , 'ラインストーンめがね'),
		('AccessoryGlassHeromask'                  , 'ヒーローマスク'),
		('AccessoryGlassSteampunk'                 , 'スチームパンクなゴーグル'),
		('TopsTexOnepieceBalloonHAngel'            , 'エンジェルなワンピース'),
		('TopsTexTopTshirtsLLoose'                 , 'ヨレヨレなシャツ'),
		('TopsTexOnepieceOverallLDevil'            , 'デビルなふく'),
		('ShoesSandalShower'                       , 'シャワーサンダル'),
		('TopsTexTopYshirtsLOpencollar'            , 'かいきんシャツ'),
		('ShoesLowcutLeathersneker'                , 'レザーのスニーカー'),
		('TopsTexTopTshirtsHMeme'                  , 'ミームなふく'),
		('SocksTexRibbon'                          , 'リボンソックス'),
		('ShoesHighcutMouton'                      , 'ムートンブーツ'),
		('ShoesLowcutEnamelpumps'                  , 'エナメルのパンプス'),
		('ShoesLowcutLoafers'                      , 'ローファー'),
		('ShoesSandalCrossbelt'                    , 'クロスベルトサンダル'),
		('TopsTexTopYshirtsLQuilting'              , 'キルティングジャケット'),
		('TopsTexOnepieceAlongNStripe'             , 'ストライプのマキシワンピ'),
		('ShoesLowcutBusiness'                     , 'ビジネスシューズ'),
		('TopsTexOnepieceAlineLJumperskirt'        , 'チェックのジャンパースカート'),
		('ShoesKneeVelour'                         , 'ベロアブーツ'),
		('ShoesKneeRainboots'                      , 'レインブーツ'),
		('ShoesSandalZori'                         , 'ぞうり'),
		('TopsTexTopOuterLSkidown'                 , 'スキーダウンジャケット'),
		('TopsTexOnepieceAlineNLace'               , 'レースのワンピース'),
		('CapHatSchool'                            , 'つうがくぼう'),
		('TopsTexOnepieceBalloonNClover'           , 'クローバーなワンピース'),
		('SocksTexSneakerin'                       , 'スニーカーインソックス'),
		('SocksTexAlan'                            , 'アランニットのソックス'),
		('SocksTexSequins'                         , 'スパンコールレギンス'),
		('SocksTexLeggings'                        , 'ストレッチレギンス'),
		('SocksTexDenimleggings'                   , 'デニムレギンス'),
		('SocksTexLine'                            , 'ラインソックス'),
		('SocksTexGarter'                          , 'ガーターつきストッキング'),
		('SocksTexNordic'                          , 'ノルディックなソックス'),
		('SocksTexTabi'                            , 'たび'),
		('TopsTexTopYshirtsLFactory'               , 'さぎょうふく'),
		('TopsTexTopOuterLBobble'                  , 'ポンポンセーター'),
		('TopsTexOnepieceDressLLady'               , 'しゅくじょなワンピース'),
		('TopsTexTopTshirtsLQuiet'                 , 'つつましいニット'),
		('TopsTexTopCoatLAnorak'                   , 'アノラック'),
		('TopsTexTopYshirtsLMultivest'             , 'たきのうベスト'),
		('CapHatNewyear'                           , 'ニューイヤーハット'),
		('CapHatBirthday'                          , 'バースデーハット'),
		('CapOrnamentTHyacinth1'                   , 'ヒヤシンスのかんむり'),
		('CapOrnamentTHyacinth2'                   , 'ヒヤシンスのかんむり・クール'),
		('CapOrnamentTHyacinth3'                   , 'ヒヤシンスのかんむり・パープル'),
		('CapOrnamentAnemones1'                    , 'アネモネのかんむり'),
		('CapOrnamentAnemones2'                    , 'アネモネのかんむり・クール'),
		('CapOrnamentAnemones3'                    , 'アネモネのかんむり・パープル'),
		('CapOrnamentTulip1'                       , 'チューリップのかんむり'),
		('CapOrnamentTulip2'                       , 'チューリップのかんむり・シック'),
		('CapOrnamentTulip3'                       , 'チューリップのかんむり・ダーク'),
		('CapOrnamentPansy1'                       , 'パンジーのかんむり'),
		('CapOrnamentPansy2'                       , 'パンジーのかんむり・クール'),
		('CapOrnamentPansy3'                       , 'パンジーのかんむり・パープル'),
		('CapOrnamentCosmos1'                      , 'コスモスのかんむり'),
		('CapOrnamentCosmos2'                      , 'コスモスのかんむり・ラブリー'),
		('CapOrnamentCosmos3'                      , 'コスモスのかんむり・ダーク'),
		('CapOrnamentRose1'                        , 'バラのかんむり'),
		('CapOrnamentRose2'                        , 'バラのかんむり・キュート'),
		('CapOrnamentRose3'                        , 'バラのかんむり・シック'),
		('CapOrnamentLily1'                        , 'ユリのかんむり'),
		('CapOrnamentLily2'                        , 'ユリのかんむり・キュート'),
		('CapOrnamentLily3'                        , 'ユリのかんむり・ダーク'),
		('CapOrnamentChrysanthemum1'               , 'キクのかんむり'),
		('CapOrnamentChrysanthemum2'               , 'キクのかんむり・シック'),
		('CapOrnamentChrysanthemum3'               , 'キクのかんむり・シンプル'),
		('TopsTexTopOuterLSnowcrystal'             , 'けっしょうのセーター'),
		('TopsTexTopTshirtsLDamage'                , 'ダメージニット'),
		('TopsTexOnepieceOverallNWrestler'         , 'レスリングのユニフォーム'),
		('CapHatSilkhat'                           , 'メッシュキャップ'),
		('CapHatMeshcap'                           , 'シルクハット'),
		('TopsTexTopCoatLSamurai'                  , 'かっちゅう'),
		('TopsTexOnepieceBlongLChina'              , 'チャイナドレス'),
		('TopsTexTopCoatLHandcover'                , 'うでカバーつきエプロン'),
		('TopsTexTopCoatLThiefBlack'               , 'かいとうのふく'),
		('TopsTexOnepieceAlineNSpace'              , 'スペースワンピース'),
		('CapHatExpedition'                        , 'たんけんぼう'),
		('CapHatBachelor'                          , 'がくしのぼうし'),
		('CapHatSombrero'                          , 'ソンブレロ'),
		('CapHatSafetyhat'                         , 'あんぜんヘルメット'),
		('CapHatCock'                              , 'コックさんのぼうし'),
		('CapHatPolice'                            , 'けいかんのぼうし'),
		('CapHatAjiro'                             , 'かさぼうし'),
		('CapHatUshanka'                           , 'フェイクファーハット'),
		('CapHatTriangle'                          , 'さんかくきん'),
		('CapHatKnitcap'                           , 'ニットキャップ'),
		('CapHatHunting'                           , 'ハンチング'),
		('CapHatWorkcap'                           , 'ワークキャップ'),
		('SocksTexFootcover'                       , 'フットカバー'),
		('SocksTexMixtweed'                        , 'ミックスツイードソックス'),
		('SocksTexLegwarmer'                       , 'レッグウォーマー'),
		('SocksTexCompression'                     , 'コンプレッションタイツ'),
		('SocksTexFolded'                          , 'みつおりソックス'),
		('SocksTexFrilledknee'                     , 'フリルつきニーハイソックス'),
		('SocksTexLace'                            , 'レースのソックス'),
		('SocksTexFrilled'                         , 'フリルソックス'),
		('SocksTexHoletights'                      , 'あなあきタイツ'),
		('SocksTexFootball'                        , 'サッカーソックス'),
		('SocksTexHole'                            , 'あなあきソックス'),
		('SocksTexBobble'                          , 'ポンポンソックス'),
		('SocksTexMultiblock'                      , 'マルチブロックソックス'),
		('SocksTexFluffy'                          , 'もこもこソックス'),
		('AccessoryGlassHmd'                       , 'HMD'),
		('AccessoryGlassNightvision'               , 'ナイトビジョン'),
		('TopsTexTopYshirtsLKids'                  , 'すこやかなセーター'),
		('CapHatSailor'                            , 'ふなのりのぼうし'),
		('CapHatViking'                            , 'バイキングのかぶと'),
		('SockstTexOverlapping'                    , 'かさねばきソックス'),
		('SocksTexHandknit'                        , 'てあみのソックス'),
		('SocksTexAerobics'                        , 'エアロビレギンス'),
		('SocksTexPucker'                          , 'くしゅくしゅソックス'),
		('SocksTexBorder'                          , 'ボーダーソックス'),
		('SocksTexOnepoint'                        , 'ワンポイントソックス'),
		('SocksTexKids'                            , 'キッズソックス'),
		('SocksTexCrocheting'                      , 'かぎばりあみソックス'),
		('SocksTexSpider'                          , 'スパイダーなタイツ'),
		('SocksTexEmbroidery'                      , 'はながらししゅうのタイツ'),
		('SocksTexRun'                             , 'ランニングタイツ'),
		('AccessoryMouthDog'                       , 'イヌのつけばな'),
		('CapHatWitch'                             , 'まじょのぼうし'),
		('CapHatDenim'                             , 'デニムキャップ'),
		('CapHatCycle'                             , 'サイクルキャップ'),
		('CapHatOutdoor'                           , 'アウトドアハット'),
		('CapHatKankanbo'                          , 'カンカンぼう'),
		('CapHatBeret'                             , 'ベレーぼう'),
		('CapHatOrange'                            , 'オレンジのぼうし'),
		('CapHatKiwi'                              , 'キウイのぼうし'),
		('CapHatStrawberry'                        , 'いちごのぼうし'),
		('CapHatGrape'                             , 'ぶどうのぼうし'),
		('CapHatPineapple'                         , 'パイナップルのぼうし'),
		('CapHatWatermelon'                        , 'スイカのぼうし'),
		('CapHatItamae'                            , 'わぼうし'),
		('CapHatCyclemet'                          , 'サイクルヘルメット'),
		('CapHatSwim'                              , 'すいえいキャップ'),
		('CapHatChina'                             , 'チャイナハット'),
		('BottomsTexPantsWideChino'                , 'ワイドチノ'),
		('BottomsTexPantsNormalChemical'           , 'ケミカルウォッシュデニム'),
		('TopsTexOnepieceOverallNHotdog'           , 'ホットドッグなふく'),
		('TopsTexOnepieceOverallLFarmer'           , 'うでカバーつきつなぎ'),
		('TopsTexTopOuterLChemical'                , 'ケミカルデニムジャケット'),
		('TopsTexTopTshirtsLLive'                  , 'ミュージックフェスなふく'),
		('TopsTexTopCoatLStraw'                    , 'みの'),
		('TopsTexTopOuterLRepresent'               , 'レペゼンなふく'),
		('CapHatTulip'                             , 'チューリップハット'),
		('CapHatBandana'                           , 'ペイズリーのバンダナ'),
		('CapHatTyrolean'                          , 'チロリアンハット'),
		('CapHatBowler'                            , 'リボンボーラーハット'),
		('CapHatStraw'                             , 'つばひろストローハット'),
		('CapHatShowercap'                         , 'みずたまシャワーキャップ'),
		('CapHatFelt'                              , 'なかおれハット'),
		('CapHatSimple'                            , 'しっそなぼうし'),
		('CapHatSports'                            , 'うんどうぼう'),
		('CapHatNightcap'                          , 'もこもこナイトキャップ'),
		('CapHatCrown'                             , 'おうかん'),
		('CapHatTowel'                             , 'タオル'),
		('CapHatAcorn'                             , 'どんぐりニット'),
		('CapHatCombat'                            , 'コンバットヘルメット'),
		('TopsTexTopYshirtsLCool'                  , 'ダンスジャージ'),
		('CapHatHokkamuri'                         , 'ほっかむり'),
		('CapHatCowl'                              , 'メルヘンなずきん'),
		('CapHatMummy'                             , 'ミイラのかぶりもの'),
		('CapHatRabbit'                            , 'ウサギのかぶりもの'),
		('CapHatCat'                               , 'ネコのかぶりもの'),
		('CapHatFaceknit'                          , 'めだしぼう'),
		('CapHatSkull'                             , 'ガイコツのかぶりもの'),
		('CapHatShallow'                           , 'あさいニットぼう'),
		('CapHatBear'                              , 'クマのかぶりもの'),
		('CapHatKappa'                             , 'カッパのおさら'),
		('CapHatCaptain'                           , 'キャプテンのぼうし'),
		('CapHatCasquette'                         , 'キャスケット'),
		('CapFullfaceKnightIron'                   , 'アイアンアーマーヘルメット'),
		('CapCostumeFrog'                          , 'カエルのかぶりもの'),
		('CapHatWizard'                            , 'とんがりぼうし'),
		('CapHatBalloon'                           , 'バルーンハット'),
		('BottomsTexPantsWideCool'                 , 'ダンスジャージズボン'),
		('CapFullfaceKnightGold'                   , 'ゴールデンアーマーヘルメット'),
		('TopsTexTopPuffHFrill'                    , 'フリルパフブラウス'),
		('TopsTexOnepieceSalopetteLAllinone'       , 'オールインワン'),
		('CapHatElegant'                           , 'エレガントなぼうし'),
		('CapCostumeFootball'                      , 'アメフトヘルメット'),
		('CapBangsFirefighter'                     , 'しょうぼうしのぼうし'),
		('CapMaskWelder'                           , 'ようせつマスク'),
		('TopsTexTopOuterLChristmas'               , 'クリスマスセーター'),
		('CapHatClown'                             , 'ピエロのぼうし'),
		('CapCostumeSamurai'                       , 'かぶと'),
		('TopsTexOnepieceOverallLMuscle'           , 'マッスルスーツ'),
		('CapHatVolendam'                          , 'オランダのぼうし'),
		('ShoesLowcutTrekking'                     , 'トレッキングシューズ'),
		('CapHelmetPilot'                          , 'ひこうぼう'),
		('CapBangsBonnet'                          , 'あかちゃんのぼうし'),
		('CapCostumeNinja'                         , 'にんじゃずきん'),
		('CapHelmetBaseballBlack'                  , 'やきゅうのヘルメット'),
		('CapCostumeJockey'                        , 'ジョッキーヘルメット'),
		('CapCostumeWrestling'                     , 'プロレスのマスク'),
		('CapBangsSausage'                         , 'ホットドッグマスク'),
		('CapBangsEarknit'                         , 'みみあてつきニット'),
		('CapHatDetective'                         , 'めいたんていのぼうし'),
		('TopsTexOnepieceOverallLCyber'            , 'サイバースーツ'),
		('TopsTexOnepieceFigure'                   , 'フィギュアのドレス'),
		('CapCostumeAstronaut'                     , 'アストロヘルメット'),
		('CapMaskPaint'                            , 'ペイントボールマスク'),
		('CapHatStrawhat'                          , 'むぎわらぼうし'),
		('CapHatTengallon'                         , 'テンガロンハット'),
		('TopsTexOnepieceOverallLFigure'           , 'フィギュアないしょう'),
		('SocksTexCharacter'                       , 'キャラクターソックス'),
		('CapHatSnowknit'                          , 'スノーニットぼう'),
		('CapHatColorful'                          , 'カラフルボーダーニットぼう'),
		('BottomsTexPantsHalfComic'                , 'アメコミがらハーフパンツ'),
		('BottomsTexPantsNormalMonpe'              , 'もんぺ'),
		('BottomsTexPantsWideRain'                 , 'レインパンツ'),
		('BottomsTexSkirtBoxAran'                  , 'ニットスカート'),
		('BottomsTexSkirtAlineFur'                 , 'ファースカート'),
		('BottomsTexPantsNormalSwewtfrill'         , 'スウェットフリルズボン'),
		('BottomsTexSkirtLongSweat'                , 'スウェットロングスカート'),
		('BottomsTexSkirtBoxBoa'                   , 'ボアスカート'),
		('BottomsTexPantsHalfBoa'                  , 'ボアハーフパンツ'),
		('BottomsTexSkirtAlineLeather'             , 'レザーのフレアスカート'),
		('BottomsTexSkirtLongLace'                 , 'まえボタンレースのスカート'),
		('BottomsTexSkirtAlineTutu'                , 'チュチュスカート'),
		('CapHelmetHero'                           , 'ヒーローヘルメット'),
		('TopsTexOnepieceOverallLPowered'          , 'パワードスーツ'),
		('TopsTexOnepieceAlongLRenaissance'        , 'ルネッサンスなドレス'),
		('CapHelmetTurban'                         , 'ターバン'),
		('CapCostumeGogglehelmet'                  , 'ゴーグルつきヘルメット'),
		('TopsTexTopYshirtsLGlass'                 , 'そうがんきょうつきベスト'),
		('TopsTexTopYshirtsLCamera'                , 'カメラつきワイシャツ'),
		('TopsTexTopTshirtsNEmbroidery'            , 'ししゅうのキャミソール'),
		('TopsTexOnepieceOverallLNordic'           , 'さむいくにのふく'),
		('CapCostumeRacing'                        , 'フルフェイスメット'),
		('SocksTexChimayo'                         , 'チマヨがらソックス'),
		('CapHatCow'                               , 'うしのほね'),
		('BottomsTexSkirtBoxChidori'               , 'ちどりのスカート'),
		('BottomsTexSkirtAlineShabby'              , 'シャビーなスカート'),
		('BottomsTexPantsWidePrintdenim'           , 'プリントデニム'),
		('BottomsTexPantsWideSuteteko'             , 'ステテコ'),
		('TopsTexOnepieceKimonoLHaregi'            , 'はれぎ'),
		('CapCostumeDevil'                         , 'デビルなかぶりもの'),
		('CapBangsSheep'                           , 'ひつじのかぶりもの'),
		('ShoesLowcutAnimal'                       , 'アニマルスリッパ'),
		('ShoesSandalBeachborder'                  , 'ビーチサンダル'),
		('ShoesLowcutStrap'                        , 'ストラップシューズ'),
		('ShoesKneeKnightIron'                     , 'アイアンアーマーシューズ'),
		('ShoesLowcutSchool'                       , 'うわばき'),
		('ShoesHighcutShortboots'                  , 'レザーのショートブーツ'),
		('ShoesSandalFlower'                       , 'フラワーなサンダル'),
		('ShoesHighcutFurboots'                    , 'ファーブーツ'),
		('ShoesLowcutLeopard'                      , 'アニマルパンプス'),
		('ShoesSandalBeads'                        , 'ビーズししゅうのサンダル'),
		('ShoesKneeRubberboots'                    , 'ながぐつ'),
		('TopsTexOnepieceKimonoLKanpukumen'        , 'ぐんしのふく'),
		('TopsTexOnepieceKimonoLKanpukuwomen'      , 'かんぷく'),
		('ShoesKneeAntique'                        , 'アンティークなブーツ'),
		('ShoesKneeKnightGold'                     , 'ゴールデンアーマーシューズ'),
		('ShoesLowcutSlipper'                      , 'スリッパ'),
		('ShoesHighcutWorkboots'                   , 'ワークブーツ'),
		('ShoesHighcutMoccasin'                    , 'モカシンブーツ'),
		('BottomsTexSkirtLongPatch'                , 'パッチワークスカート'),
		('ShoesHighcutBobbles'                     , 'ポンポンつきブーツ'),
		('ShoesKneeLegguard'                       , 'かっちゅうのすねあて'),
		('ShoesLowcutGlitter'                      , 'ストラップつきパンプス'),
		('ShoesSandalRoomborder'                   , 'ルームシューズ'),
		('ShoesSandalResin'                        , 'スリッポンサンダル'),
		('ShoesHighcutSlipon'                      , 'スリッポン'),
		('TopsTexOnepieceBoxLSchoolsmock'          , 'スクールスモック'),
		('ShoesLowcutLolita'                       , 'ロリータシューズ'),
		('ShoesLowcutBallet'                       , 'バレエシューズ'),
		('ShoesKneeVisual'                         , 'ヴィジュアルけいブーツ'),
		('TopsTexOnepieceSalopetteLRumba'          , 'ルンバないしょう'),
		('ShoesHighcutRubbertoe'                   , 'ラバートゥハイカットスニーカー'),
		('ShoesLowcutClog'                         , 'きぐつ'),
		('ShoesSandalComfort'                      , 'コンフォートサンダル'),
		('ShoesSandalGladiator'                    , 'グラディエーターサンダル'),
		('ShoesKneeHero'                           , 'ヒーローブーツ'),
		('ShoesHighcutBasket'                      , 'バスケットシューズ'),
		('ShoesKneeClown'                          , 'ピエロのくつ'),
		('ShoesSandalOutdoor'                      , 'アウトドアサンダル'),
		('CapHatEgg'                               , 'たまごのから'),
		('ShoesKneeWestern'                        , 'ウェスタンブーツ'),
		('TopsTexOnepieceRibNChick'                , 'ひよこなふく'),
		('TopsTexOnepieceAlongHRumba'              , 'ルンバなドレス'),
		('TopsTexTopTshirtsLSailor'                , 'セーラーシャツ'),
		('ShoesLowcutGgotshin'                     , 'コッシン'),
		('ShoesSandalAqua'                         , 'アクアサンダル'),
		('TopsTexOnepieceOverallLHighcollar'       , 'つめえりスーツ'),
		('ShoesLowcutSpike'                        , 'スパイク'),
		('ShoesLowcutPointedtoe'                   , 'トンがったクツ'),
		('TopsTexTopYshirtsLFischerhemd'           , 'フィッシャーヘムト'),
		('ShoesHighcutHightech'                    , 'ハイテクシューズ'),
		('ShoesKneeSki'                            , 'スキーブーツ'),
		('CapHatCavalier'                          , 'じゅうきしのぼうし'),
		('BottomsTexPantsHotShaggycheck'           , 'シャギーチェックのホットパンツ'),
		('BottomsTexSkirtLongEnaguas'              , 'エナグワス'),
		('AccessoryGlassmouthCatrina'              , 'スカルキャンディマスク'),
		('ShoesKneeLaceup'                         , 'あみあげブーツ'),
		('ShoesKneeRing'                           , 'リングシューズ'),
		('CapCostumeBangs'                         , 'のうぎょうぼう'),
		('TopsTexTopOuterLPsychedelic'             , 'ハデなカーディガン'),
		('CapCostumeHeadgear'                      , 'ヘッドギア'),
		('CapWigMohican'                           , 'モヒカン'),
		('CapWigRegent'                            , 'リーゼント'),
		('CapWigSamurai'                           , 'ちょんまげ'),
		('CapWigOnionhair'                         , 'たまねぎヘアー'),
		('CapWigDoublebun'                         , 'おだんごあたま'),
		('CapBangsHeadphone'                       , 'ヘッドホン'),
		('CapHelmetHeaddress'                      , 'ヘッドドレス'),
		('CapFullfaceVeil'                         , 'ベール'),
		('CapWigGeisya'                            , 'ゲイシャさん'),
		('CapHelmetMusic'                          , 'おんがくかのかつら'),
		('CapFullfacePowered'                      , 'パワードメット'),
		('ShoesKneePowered'                        , 'パワードブーツ'),
		('BottomsTexPantsWideTeared'               , 'やぶれたズボン'),
		('BottomsTexPantsNormalCroppedsweat'       , 'フィットネススウェットパンツ'),
		('BottomsTexSkirtBoxBoxpleats'             , 'ボックスプリーツスカート'),
		('BottomsTexSkirtBoxMouton'                , 'ムートンスカート'),
		('BottomsTexPantsHotMultistripe'           , 'マルチストライプのホットパンツ'),
		('BottomsTexPantsNormalKnit'               , 'ニットパンツ'),
		('BottomsTexSkirtLongDenim'                , 'ロングデニムスカート'),
		('BottomsTexSkirtBoxApron'                 , 'エプロンつきスカート'),
		('BottomsTexPantsHotFluffy'                , 'もこもこホットパンツ'),
		('BottomsTexPantsHalfBasketball'           , 'バスケットパンツ'),
		('BottomsTexPantsNormalTraining'           , 'ワークアウトパンツ'),
		('BottomsTexSkirtLongMaone'                , 'ＭＡ‐１スカート'),
		('BottomsTexPantsHotSequins'               , 'スパンコールのホットパンツ'),
		('BottomsTexPantsWideMultistripe'          , 'マルチストライプワイドパンツ'),
		('BottomsTexPantsNormalComedian'           , 'コメディアンのパンツ'),
		('BottomsTexSkirtAlinePearl'               , 'パールつきスカート'),
		('AccessoryMouthBubblegum'                 , 'ふうせんガム'),
		('AccessoryGlassFlower'                    , 'フラワーサングラス'),
		('BottomsTexPantsHotLeather'               , 'レザーのショートパンツ'),
		('BottomsTexPantsHalfGobelins'             , 'ゴブランハーフパンツ'),
		('BottomsTexPantsWideThail'                , 'タイパンツ'),
		('ShoesKneeSpace'                          , 'スペースブーツ'),
		('ShoesHighcutSports'                      , 'キッズなスニーカー'),
		('AccessoryGlassmouthStraw'                , 'ストローメガネ'),
		('TopsTexTopOuterNNosleeve'                , 'ノースリーブパーカー'),
		('ShoesLowcutHealth'                       , 'ウォーキングシューズ'),
		('BottomsTexSkirtLongCorte'                , 'コルテ'),
		('BottomsTexPantsNormalChimayo'            , 'チマヨがらフリースパンツ'),
		('TopsTexOnepieceBalloonHYumekawa'         , 'ゆめかわなドレス'),
		('TopsTexOnepieceKimonoLGaudy'             , 'ゴージャスなきもの'),
		('TopsTexOnepieceDressLNoble'              , 'きぞくのドレス'),
		('TopsTexOnepieceSalopetteLPsychedelic'    , 'サイケなつなぎ'),
		('ShoesLowcutToilet'                       , 'トイレスリッパ'),
		('TopsTexOnepieceKimonoLShitamachi'        , 'まちむすめのきもの'),
		('ShoesHighcutCute'                        , 'キュートなスニーカー'),
		('SocksTexFlowerdot'                       , 'フラワードットタイツ'),
		('SocksTexArgyle'                          , 'アーガイルソックス'),
		('ShoesLowcutMoccasin'                     , 'モカシン'),
		('ShoesLowcutMarine'                       , 'マリンシューズ'),
		('ShoesLowcutWing'                         , 'ウイングチップのシューズ'),
		('BottomsTexSkirtLongCutleather'           , 'カットレザースカート'),
		('BottomsTexSkirtAlinePatch'               , 'レザーパッチスカート'),
		('SocksTexSeethrough'                      , 'シースルーソックス'),
		('SocksTexWave'                            , 'せいがいはソックス'),
		('ShoesSandalRibbon'                       , 'リボンサンダル'),
		('TopsTexOnepieceBoxNTango'                , 'タンゴなドレス'),
		('BottomsTexSkirtLongWrapbicolor'          , 'ボタンのまきスカート'),
		('TopsTexOnepieceBoxNFlapper'              , 'フラッパードレス'),
		('TopsTexOnepieceKimonoLKorea'             , 'パジチョゴリ'),
		('TopsTexOnepieceKimonoLAsagao'            , 'あさがおのゆかた'),
		('ShoesSandalSports'                       , 'スポーツサンダル'),
		('TopsTexOnepieceOverallLSteampunk'        , 'スチームパンクなふく'),
		('BottomsTexSkirtLongTiedye'               , 'タイダイスカート'),
		('TopsTexOnepieceOverallLFarm'             , 'ファームなオーバーオール'),
		('TopsTexOnepieceSalopetteLHockey'         , 'アイスホッケーのユニフォーム'),
		('AccessoryMouthJokeDrip'                  , 'はなみず'),
		('CapFullfacePaperbag'                     , 'かみぶくろ'),
		('TopsTexTopTshirtsHStaff'                 , 'スタッフのふく'),
		('BottomsTexPantsHalfBotanical'            , 'ボタニカルハーフパンツ'),
		('TopsTexTopCoatLOilskin'                  , 'オイルスキンのジャケット'),
		('AccessoryMouthPasta'                     , 'たべこぼし'),
		('BottomsTexPantsWideGakuran'              , 'がくせいふくのズボン'),
		('BottomsTexSkirtLongLemon'                , 'レモンのスカート'),
		('BottomsTexPantsWideYumekawa'             , 'ゆめかわなズボン'),
		('BottomsTexSkirtLongFlower'               , 'はながらスカート'),
		('TopsTexTopYshirtsLGuide'                 , 'あんないがかりのふく'),
		('CapHatNewyearsilk'                       , 'ニューイヤーシルクハット'),
		('TopsTexTopOuterLBulldog'                 , 'ブルドッグジャージ'),
		('BottomsTexSkirtLongSailor'               , 'ロングセーラースカート'),
		('TopsTexOnepieceKimonoLHomongi'           , 'むじのほうもんぎ'),
		('TopsTexOnepieceKimonoLButterfly'         , 'ちょうがらのほうもんぎ'),
		('TopsTexOnepieceKimonoLYukatamen'         , 'かぶきなゆかた'),
		('TopsTexTopYshirtsLDoublet'               , 'ダブレット'),
		('CapMaskFox'                              , 'キツネのおめん'),
		('CapMaskOkina'                            , 'おきなののうめん'),
		('CapMaskNomen'                            , 'のうめん'),
		('AccessoryGlassMirror'                    , 'はんしゃきょう'),
		('AccessoryMouthLeather'                   , 'レザーマスク'),
		('AccessoryGlassmouthHockeyWhite'          , 'ホッケーのマスク'),
		('ShoesLowcutBrogues'                      , 'ギリー・ブローグズ'),
		('ShoesSandalBaboush'                      , 'バブーシュ'),
		('SocksTexCountry'                         , 'カントリーソックス'),
		('SocksTexStripe'                          , 'ストライプソックス'),
		('SocksTexStripedot'                       , 'デザインストッキング'),
		('CapHatKanbo'                             , 'かんぼう'),
		('CapHatGreenery'                          , 'グレンガリーぼう'),
		('CapFullfaceCatcher'                      , 'キャッチャーマスク'),
		('CapHelmetKandula'                        , 'アラビアのぼうし'),
		('CapFullfaceKuroko'                       , 'くろこ'),
		('CapHatKnitcasquette'                     , 'ボンボンつきキャスケット'),
		('CapHatScotlandRed'                       , 'スコットランドぼうし'),
		('ShoesHighcutSneaker_'                    , 'ハイカットスニーカー'),
		('TopsTexTopYshirtsLGingham'               , 'ギンガムチェックのシャツ'),
		('ShoesKneeEngineerboots_'                 , 'エンジニアブーツ'),
		('CapOrnamentRRibbonRed_'                  , 'リボン'),
		('TopsTexOnepieceRibNEgg'                  , 'たまごずし'),
		('TopsTexOnepieceRibNTuna'                 , 'まぐろずし'),
		('TopsTexOnepieceRibNKohada'               , 'こはだずし'),
		('ShoesLowcutRubbertoe'                    , 'ラバートゥスニーカー'),
		('ShoesKnee'                               , 'とんがりブーツ'),
		('TopsTexTopTshirtsN'                      , 'ビブス'),
		('CapOrnamentCAngel0'                      , 'てんしのわ'),
		('CapOrnamentTNurse'                       , 'ナースキャップ'),
		('CapHatIcecream'                          , 'ソフトクリームなぼうし'),
		('CapOrnamentCBunny'                       , 'バニーのみみ'),
		('CapHatSandogasa'                         , 'さんどがさ'),
		('CapOrnamentLMinistrawhat'                , 'ちいさめなぼうし'),
		('CapOrnamentLMinisilkhat'                 , 'ちいさめシルクハット'),
		('CapMaskLeaf'                             , 'はっぱのおめん'),
		('BagBackpackTown1'                        , 'タウンリュック'),
		('BagShoulderTravel'                       , 'トラベルポーチ'),
		('CapOrnamentRose4'                        , 'バラのかんむり・ブルー'),
		('CapOrnamentRose5'                        , 'バラのかんむり・ゴールド'),
		('CapOrnamentCTiara'                       , 'ティアラ'),
		('BagShoulderMessenger'                    , 'メッセンジャーバッグ'),
		('BagBackpackDry'                          , 'ドライサック'),
		('BagShoulderLeather'                      , 'レザーショルダー'),
		('BagShoulderFish'                         , 'おさかなポシェット'),
		('BagShoulderFishing'                      , 'フィッシングバッグ'),
		('BagShoulderCage'                         , 'ムシかご'),
		('BagShoulderFakefur'                      , 'フェイクファーバッグ'),
		('BagShoulderFringe'                       , 'フリンジレザーバッグ'),
		('BagShoulderRace'                         , 'てあみポーチ'),
		('BagShoulderBody'                         , 'ボディバッグ'),
		('BagShoulderBodybag'                      , 'レザーボディバッグ'),
		('BagShoulderDrum'                         , 'ななめかけボストン'),
		('BagShoulderPattern'                      , 'はるのみずたまショルダー'),
		('BagShoulderCanvas'                       , 'はんぷショルダー'),
		('BagShoulderRattan'                       , 'ラタンポシェット'),
		('BagShoulderStar'                         , 'スターなポシェット'),
		('BagShoulderCherryblossoms'               , 'さくらのポシェット'),
		('BagShoulderMaple'                        , 'もみじのポシェット'),
		('BagShoulderAcorn'                        , 'どんぐりポシェット'),
		('BagShoulderSnow'                         , 'スノーフレークポシェット'),
		('BagShoulderShell'                        , 'かいがらポシェット'),
		('BagShoulderTool'                         , 'ツールバッグ'),
		('BagShoulderSports'                       , 'スポーツバッグ'),
		('BagShoulderSacosh'                       , 'サコッシュ'),
		('BagShoulderParty'                        , 'パーティーバッグ'),
		('BagBackpackWood'                         , 'せおいばしご'),
		('BagBackpackJourney'                      , 'たびびとのリュック'),
		('BagBackpackSquare'                       , 'しかくいリュック'),
		('BagBackpackOutdoor'                      , 'アウトドアリュック'),
		('BagBackpackButterfly'                    , 'ちょうちょのバッグ'),
		('BagBackpackStuds'                        , 'スタッズリュック'),
		('BagBackpackSmall'                        , 'ミニレザーバッグ'),
		('BagBackpackMountain'                     , 'おおきめザック'),
		('BagBackpackBasket'                       , 'しょいこ'),
		('BagBackpackLid'                          , 'ふたつきリュック'),
		('BagBackpackKnapsack'                     , 'ナップサック'),
		('BagBackpackTote'                         , 'はんぷリュック'),
		('BagBackpackQuilt'                        , 'ははのナップサック'),
		('BagBackpackGrass'                        , 'くさあみリュック'),
		('BagBackpackHardshell'                    , 'ハードシェルリュック'),
		('SocksTexStandard'                        , 'ビビッドなソックス'),
		('ShoesLowcutSuede'                        , 'スエードスニーカー'),
		('TopsTexOnepieceAlineHOneflower'          , 'フラワーなワンピース'),
		('TopsTexTopTshirtsHMvp'                   , 'ＭＶＰなＴシャツ'),
		('TopsTexTopTshirtsHOne'                   , 'No.1のふく'),
		('CapWigPrincess'                          , 'おひめさま'),
		('CapWigTurban'                            , 'ヘアターバン'),
		('CapHelmetCoin'                           , 'コインヘッドピース'),
		('CapWigPigtail'                           , 'べんぱつ'),
		('CapWigVisual'                            , 'ヴィジュアルけいウィッグ'),
		('CapOrnamentCQueen0'                      , 'クイーンのかんむり'),
		('TopsTexOnepieceAlineNMarbledot'          , 'マーブルドットのワンピース'),
		('TopsTexOnepieceAlineNSimpledot'          , 'シンプルドットワンピース'),
		('TopsTexOnepieceAlineNHibiscus'           , 'ハイビスカスのムームー'),
		('TopsTexOnepieceAlineNPolynesia'          , 'ポリネシアンなムームー'),
		('TopsTexTopTshirtsNDanger'                , 'デンジャラスなタンクトップ'),
		('TopsTexTopOuterLHeart'                   , 'ハートのセーター'),
		('TopsTexTopOuterLTree'                    , 'きのセーター'),
		('TopsTexTopTshirtsHFrog'                  , 'かえるのＴシャツ'),
		('TopsTexTopTshirtsHBear'                  , 'くまのＴシャツ'),
		('TopsTexTopTshirtsHRabbit'                , 'うさぎのＴシャツ'),
		('TopsTexTopTshirtsHStripe'                , 'しましまＴシャツ'),
		('TopsTexTopTshirtsHLeopard'               , 'ヒョウがらＴシャツ'),
		('TopsTexTopTshirtsHMeat'                  , 'ボーンなＴシャツ'),
		('TopsTexTopTshirtsHHaze'                  , 'かすみのふく'),
		('TopsTexTopTshirtsHMarbledot'             , 'マーブルドットのＴシャツ'),
		('TopsTexTopTshirtsHSimpledot'             , 'シンプルドットのＴシャツ'),
		('TopsTexTopTshirtsLJagged'                , 'ギザギザのＴシャツ'),
		('TopsTexTopTshirtsHFlower'                , 'はながらのＴシャツ'),
		('TopsTexTopYshirtsHPolynesia'             , 'ポリネシアンなアロハ'),
		('TopsTexTopTshirtsHSpider'                , 'スパイダーなＴシャツ'),
		('TopsTexTopTshirtsHSkull'                 , 'ドクロＴシャツ'),
		('TopsTexTopTshirtsHAce'                   , 'エースのＴシャツ'),
		('TopsTexOnepieceAlineNPlaid'              , 'シンプルチェックのワンピ'),
		('CapCostumeSnowball0'                     , 'ゆきだるまのぼうし'),
		('CapOrnamentLTsumamizaiku'                , 'わかざり'),
		('CapOrnamentLGaudy'                       , 'はでなかみかざり'),
		('CapHatCaptainsky'                        , 'きちょうのぼうし'),
		('CapHatStudent'                           , 'がくせいぼう'),
		('CapOrnamentLHibiscus'                    , 'ハイビスカスのかみかざり'),
		('TopsTexTopTshirtsNStar'                  , 'ほしがらタンクトップ'),
		('TopsTexTopTshirtsHFire'                  , 'ファイアーなＴシャツ'),
		('TopsTexOnepieceAlineHPlaid'              , 'げんきなチェックのワンピ'),
		('SocksTexNuancetights'                    , 'ニュアンスタイツ'),
		('SocksTexDailytights'                     , 'デイリータイツ'),
		('SocksTexVividtights'                     , 'ビビッドなタイツ'),
		('SocksTexNeontights'                      , 'ネオンタイツ'),
		('SocksTexVividleggings'                   , 'ビビッドなレギンス'),
		('SocksTexNeonleggings'                    , 'ネオンレギンス'),
		('AcceMouthTest1_'                         , 'おしゃぶり'),
		('TopsTexTopOuterLMother'                  , 'ははのてあみセーター'),
		('TopsTexTopCoatLMother'                   , 'ははのてづくりエプロン'),
		('TopsTexTopOuterLKnit'                    , 'シンプルなニット'),
		('SocksTexDailysocks'                      , 'デイリーソックス'),
		('SocksTexNuancesocks'                     , 'ニュアンスソックス'),
		('CapHatBaseball'                          , 'ベースボールキャップ'),
		('TopsTexTopCoatLViking'                   , 'バイキングのふく'),
		('TopsTexTopCoatLRaindot'                  , 'みずたまレインコート'),
		('TopsTexOnepieceBlongLCandula'            , 'カンデューラ'),
		('CapHatTweed'                             , 'ツイードキャップ'),
		('TopsTexTopCoatHDiner'                    , 'ダイナーのエプロン'),
		('TopsTexTopTshirtsLLayeredlogoa'          , 'かさねぎプリントＴシャツ'),
		('TopsTexTopTshirtsLLogoa'                 , 'アームプリントＴシャツ'),
		('TopsTexTopPuffHPlaid'                    , 'ブロックチェックのパフスリーブ'),
		('TopsTexTopPuffHDolly'                    , 'ドーリーシャツ'),
		('TopsTexTopCoatHWorkapron'                , 'ワークエプロン'),
		('TopsTexTopTshirtsHBotanical'             , 'ボタニカルＴシャツ'),
		('TopsTexTopYshirtsLPsychedelic'           , 'サイケデリックシャツ'),
		('TopsTexOnepieceKimonoLTwelve'            , 'じゅうにひとえ'),
		('TopsTexOnepieceDressLMexico'             , 'セニョリータなドレス'),
		('TopsTexOnepieceKimonoLCrested'           , 'もんつきはかま'),
		('TopsTexOnepieceAlineNApple'              , 'リンゴのふく'),
		('TopsTexOnepieceAlineNPear'               , 'ナシのふく'),
		('TopsTexOnepieceAlineNCherry'             , 'さくらんぼのふく'),
		('TopsTexOnepieceAlineNPeach'              , 'モモのふく'),
		('BottomsTexPantsHalfSoccer'               , 'サッカーのズボン'),
		('BottomsTexPantsHalfExplorer'             , 'たんけんふくのズボン'),
		('BottomsTexSkirtBoxLStripe'               , 'アニマルがらスカート'),
		('BottomsTexPantsNormalAmericanfootball'   , 'アメフトズボン'),
		('ShoesLowcutKungfu'                       , 'カンフーシューズ'),
		('ShoesLowcutEmbroidery'                   , 'ししゅうのくつ'),
		('CapOrnamentLFlowerhairpin'               , 'おはなのヘアピン'),
		('CapOrnamentLHearthairpin'                , 'ハートのかみかざり'),
		('CapOrnamentLStarhairpin'                 , 'ほしのかみかざり'),
		('CapOrnamentTBarrette'                    , 'バレッタ'),
		('CapOrnamentTRibbon'                      , 'おおきなリボン'),
		('CapCostumeStar'                          , 'おほしさまのあたま'),
		('CapHatSkate'                             , 'スケボーヘルメット'),
		('CapHatAlan'                              , 'アランニットぼう'),
		('CapHatLogocap'                           , 'もじキャップ'),
		('CapHatGarlystrawhat'                     , 'リボンつきむぎわらぼうし'),
		('CapHatTulippatch'                        , 'パッチワークのチューリップぼう'),
		('CapHatApple'                             , 'リンゴのぼうし'),
		('CapHatPear'                              , 'ナシのぼうし'),
		('CapHatCherry'                            , 'さくらんぼのぼうし'),
		('CapHatPeach'                             , 'モモのぼうし'),
		('TopsTexTopTshirtsHKate'                  , 'ケイトのカットソー'),
		('TopsTexTopCoatLKate'                     , 'ケイトのコート'),
		('TopsTexOnepieceAlineNKate'               , 'ケイトのワンピース'),
		('BottomsTexPantsHalfKate'                 , 'ケイトのハーフパンツ'),
		('BottomsTexSkirtLongKate'                 , 'ケイトのスカート'),
		('CapHatKatecap'                           , 'ケイトのキャップ'),
		('CapHatKatehat'                           , 'ケイトのぼうし'),
		('SocksTexKatetights'                      , 'ケイトのタイツ'),
		('SocksTexKatesocks'                       , 'ケイトのソックス'),
		('ShoesHighcutKateboots'                   , 'ケイトのパンプス'),
		('ShoesHighcutKatesneaker'                 , 'ケイトのスニーカー'),
		('AccessoryGlassKate'                      , 'ケイトのサングラス'),
		('TopsTexTopOuterLRco'                     , 'たぬきかいはつブルゾン'),
		('TopsTexTopTshirtsHRco'                   , 'たぬきかいはつアロハ'),
		('CapHatMeshcapRco'                        , 'たぬきかいはつキャップ'),
		('CapHatBandanaRco'                        , 'たぬきかいはつバンダナ'),
		('SocksTexBorderRco'                       , 'たぬきかいはつソックス'),
		('ShoesSandalRco'                          , 'たぬきかいはつスリッパ'),
		('TopsTexTopTshirtsHStar'                  , 'いちばんぼしのふく'),
		('CapHatRain'                              , 'レインハット'),
		('AccessoryGlassNook0'                     , 'たぬきかいはつアイマスク'),
		('TopsTexTopTshirtsHNook0'                 , 'たぬきかいはつＴシャツ'),
		('BagBackpackNook0'                        , 'たぬきかいはつナップサック'),
		('TopsTexTopYshirtsHInsect'                , 'インセクトアロハ'),
		('TopsTexTopTshirtsHFish'                  , 'さかなＴシャツ'),
		('CapHatOutdoorpine'                       , 'パインがらアウトドアハット'),
		('TopsTexTopCoatLPajamas'                  , 'もこもこナイトガウン'),
		('TopsTexOnepieceBoxLPajamas'              , 'パジャマワンピ'),
		('TopsTexOnepieceBalloonHVisual'           , 'ヴィジュアルけいドレス'),
		('TopsTexOnepieceAlongLUzbek'              , 'ウズベクなふく'),
		('TopsTexOnepieceBlongLAttoushi'           , 'アットゥシ'),
		('TopsTexOnepieceKimonoLBingata'           , 'びんがたいしょう'),
		('TopsTexTopCoatLDoll'                     , 'ぬいぐるみマフラーつきコート'),
		('TopsTexOnepieceOverallLPaint'            , 'ペイントつなぎ'),
		('CapHatUzbek'                             , 'ウズベクなぼうし'),
		('CapHatMatampushi'                        , 'マタンプシ'),
		('TopsTexTopTshirtsHTwo0'                  , 'No.2のふく'),
		('TopsTexTopTshirtsHThree0'                , 'No.3のふく'),
		('TopsTexTopTshirtsHFour0'                 , 'No.4のふく'),
		('TopsTexTopTshirtsHHellojp0'              , 'こんにちはＴシャツ'),
		('TopsTexTopTshirtsHHellofr0'              , 'ボンジュールＴシャツ'),
		('TopsTexTopTshirtsHHelloen0'              , 'ハローＴシャツ'),
		('TopsTexTopTshirtsHHellokr0'              , 'アンニョンＴシャツ'),
		('TopsTexTopTshirtsHHelloch0'              , 'ニーハオＴシャツ'),
		('TopsTexTopTshirtsHHelloge0'              , 'ハーローＴシャツ'),
		('TopsTexTopTshirtsHHelloit0'              , 'チャオＴシャツ'),
		('TopsTexTopTshirtsHHellosp0'              , 'オラＴシャツ'),
		('TopsTexTopTshirtsHHellors0'              , 'プリヴェＴシャツ'),
		('TopsTexTopTshirtsHHellotw0'              , 'ハイＴシャツ'),
		('TopsTexTopTshirtsHHelloNr0'              , 'ホーイＴシャツ'),
		('TopsTexTopTshirtsHDal0'                  , 'ＤＡＬのＴシャツ'),
		('TopsTexTopCoatHDal0'                     , 'ＤＡＬエプロン'),
		('TopsTexTopOuterLDal0'                    , 'ＤＡＬのＭＡ‐１'),
		('AccessoryGlassDalmask0'                  , 'ＤＡＬアイマスク'),
		('AccessoryGlassDalglass0'                 , 'ＤＡＬサングラス'),
		('AccessoryGlassSlippers0'                 , 'ＤＡＬスリッパ'),
		('BagBackpackDal0'                         , 'ＤＡＬのバッグ'),
		('CapHatDal0'                              , 'ＤＡＬキャップ'),
		('BottomsTexSkirtAlineDot'                 , 'ドットミニスカート'),
		('SocksTexDotknee'                         , 'ドットのニーハイソックス'),
		('SocksTexSimpleknee'                      , 'シンプルなニーハイソックス'),
		('BottomsTexSkirtBoxGrass1'                , 'みどりのこしみの'),
		('ShoesKneeRecyclingboots0'                , 'リサイクルながぐつ'),
		('CapHatOkmotors'                          , 'OKモータースのキャップ'),
		('TopsTexTopYshirtsHOkmotors'              , 'OKモータースジャケット'),
		('TopsTexTopTshirtsHOkmotors'              , 'キャンパーのTシャツ'),
		('CapHatEggground'                         , 'じめんのたまごのから'),
		('CapHatEggrock'                           , 'いわのたまごのから'),
		('CapHatEggleaf'                           , 'はっぱのたまごのから'),
		('CapHatEggforest'                         , 'ウッディなたまごのから'),
		('CapHatEggsky'                            , 'そらとぶたまごのから'),
		('CapHatEggfish'                           , 'サカナのたまごのから'),
		('CapOrnamentEgg'                          , 'イースターなかんむり'),
		('CapHatEggparty'                          , 'たまごのパーティーハット'),
		('BagBackpackEgg'                          , 'イースターなバッグ'),
		('TopsTexOnepieceBalloonLEgg'              , 'たまごのパーティーワンピ'),
		('TopsTexOnepieceRibNEggground'            , 'じめんのたまごのふく'),
		('TopsTexOnepieceRibNEggrock'              , 'いわのたまごのふく'),
		('TopsTexOnepieceRibNEggleaf'              , 'はっぱのたまごのふく'),
		('TopsTexOnepieceRibNEggforest'            , 'ウッディなたまごのふく'),
		('TopsTexOnepieceRibNEggsky'               , 'そらとぶたまごのふく'),
		('TopsTexOnepieceRibNEggfish'              , 'サカナのたまごのふく'),
		('ShoesLowcutEggground'                    , 'じめんのたまごのくつ'),
		('ShoesLowcutEggrock'                      , 'いわのたまごのくつ'),
		('ShoesLowcutEggleaf'                      , 'はっぱのたまごのくつ'),
		('ShoesLowcutEggforest'                    , 'ウッディなたまごのくつ'),
		('ShoesLowcutEggsky'                       , 'そらとぶたまごのくつ'),
		('ShoesLowcutEggfish'                      , 'サカナのたまごのくつ'),
		('TopsTexTopTshirtsLBorder'                , 'ボーダーＴシャツ'),
		('TopsTexTopYshirtsLMountain'              , 'マウンテンパーカー'),
		('TopsTexTopCoatLDuffle'                   , 'ダッフルコート'),
		('TopsTexOnepieceRibLKnit'                 , 'ニットワンピース'),
		('TopsTexOnepieceRibLParka'                , 'パーカーワンピ'),
		('TopsTexOnepieceBoxHJumperskirt'          , 'ジャンパースカート'),
		('TopsTexOnepieceBoxHLayercamisole'        , 'レイヤーキャミワンピ'),
		('BottomsTexPantsNormalChino'              , 'チノパン'),
		('BottomsTexPantsNormalTwotone'            , 'ツートンなズボン'),
		('BottomsTexSkirtAlineGingham'             , 'ギンガムチェックのスカート'),
		('BottomsTexPantsNormalDenimNonwa'         , 'デニムパンツ'),
	))
	_a6b1a7fd = Enum(0xa6b1a7fd, enum_b7cccd84)
	_b7cccd84 = Enum(0xb7cccd84, enum_b7cccd84)
	_0e0acf95 = Enum(0x0e0acf95, enum_0e0acf95)
	Depth = Float(0xf8316716)
	_43507f0d = Enum(0x43507f0d, (
		('Light'     , '軽い'),
		('Normal'    , '通常'),
		('Heavy'     , '重い'),
		('VeryHeavy' , 'すごく重い'),
		('LightWheel', 'キャスター：軽い'),
		('HeavyWheel', 'キャスター：重い'),
		('Floated'   , '浮遊'),
	))
	_d7f212ea = Enum(0xd7f212ea, (
		('None'            , 'なし'),
		('Trex'            , 'Tレックス'),
		('Archelon'        , 'アーケロン'),
		('FootPrint'       , 'あしあとのかせき'),
		('Ankiro'          , 'アンキロ'),
		('Ammonite'        , 'アンモナイト'),
		('Ophthalmosaurus' , 'オフタルモサウルス'),
		('Iguanodon'       , 'イグアノドン'),
		('Droop'           , 'ウンコのかせき'),
		('Amber'           , 'コハク'),
		('Trilobite'       , 'さんようちゅう'),
		('Archeopteryx'    , 'しそちょう'),
		('Stego'           , 'ステゴ'),
		('Spino'           , 'スピノ'),
		('Diplodocus'      , 'ディプロドクス'),
		('Dimetro'         , 'ディメトロドン'),
		('Tricera'         , 'トリケラトプス'),
		('Pachy'           , 'パキケファロサウルス'),
		('Parasauro'       , 'パラサウロロフス'),
		('Futaba'          , 'フタバサウルス'),
		('Pterano'         , 'プテラノドン'),
		('Brontotherium'   , 'メガセロプス'),
		('Australopithecus', 'アウストラロピテクス'),
		('Mammoth'         , 'マンモス'),
		('Deinonychus'     , 'ディノニクス'),
		('Smilodon'        , 'スミロドン'),
		('Anomalocaris'    , 'アノマロカリス'),
		('Megaloceros'     , 'メガロケロス'),
		('Dunkleosteus'    , 'ダンクルオステウス'),
		('FirstFish'       , 'ミクロンミンギア'),
		('FirstAmphibian'  , 'ユーステノプテロン'),
		('FirstFourLegs'   , 'アカントステガ'),
		('FirstMammal'     , 'ジュラマイア'),
		('Brachiosaurus'   , 'ブラキオサウルス'),
		('Quetzalcoatlus'  , 'ケツァルコアトルス'),
		('Shark'           , 'サメのはのかせき'),
	))
	Height = Float(0xc187c516)
	_f1246e5f = Enum(0xf1246e5f, (
		('None'                      , 'なし'),
		('Chair'                     , 'イス：通常'),
		('ChairSp'                   , 'イス：SP'),
		('ChairAll'                  , 'イス：丸イス'),
		('ChairFL2Way'               , 'イス：前左2方向'),
		('ChairFB'                   , 'イス：前後'),
		('ChairLeftFB'               , 'イス：前後：左半分'),
		('ChairCenterF'              , 'イス：前：中央のみ'),
		('ChairFLRTouchSwitch'       , 'イス：SP：接触スイッチ'),
		('Bed'                       , 'ベッド：通常'),
		('BedSwitch'                 , 'ベッド：スイッチ'),
		('ChestPull'                 , 'タンス'),
		('ChestSingle'               , 'クローゼット：片開き'),
		('ChestDouble'               , 'クローゼット：両開き'),
		('ChestDoubleCenter'         , 'クローゼット：両開き：中央のみ'),
		('ChestFlip'                 , 'クローゼット：フリップ'),
		('Dresser'                   , 'ドレッサー'),
		('Audio'                     , 'オーディオ'),
		('RandomAudio'               , 'ラジオ'),
		('MusicalInstrument'         , '楽器'),
		('TV'                        , 'テレビ'),
		('Clock'                     , '時計：ノーマル'),
		('ClockPendulum'             , '時計：振り子'),
		('ClockPigeon'               , '時計：ハト'),
		('ClockDigital'              , '時計：デジタル'),
		('ClockSwitch'               , '時計：スイッチ'),
		('WorkBench'                 , '作業台'),
		('LoopAuto'                  , 'ループ'),
		('LoopSwitch'                , 'ループ：スイッチ'),
		('LoopOnOffFade'             , 'ループ：フェード'),
		('LoopTrigger'               , 'ループ：トリガー'),
		('LoopAutoOnOff'             , 'ループ：オンオフ'),
		('LoopTriggerOnOff'          , 'ループ：トリガー：オンオフ'),
		('TriggerOnce'               , 'トリガー'),
		('TriggerOnOff'              , 'トリガー：オンオフ'),
		('TriggerRestart'            , 'トリガー：上書き'),
		('TriggerOnOffAndLoop'       , 'トリガー：toループ オンオフ'),
		('TriggerOnOffAndLoopWaitEnd', 'トリガー：toループ終了待ちオンオフ'),
		('Pass'                      , '通過'),
		('Touch'                     , '接触'),
		('TouchTriggerWaitEndOnKeep' , '接触：ループ終了待ち：トリガー'),
		('GrabHoldLoopWaitEnd'       , '掴みホールド：ループ終了待ちオンオフ'),
		('GrabHold'                  , '掴みホールド'),
		('LightSensorSwitch'         , '外灯（明るさセンサー）'),
		('MailBoxTypeA'              , 'ポスト：タイプA'),
		('MailBoxTypeB'              , 'ポスト：タイプB'),
		('MailBoxTypeC'              , 'ポスト：タイプC'),
		('MailBoxTypeD'              , 'ポスト：タイプD'),
		('MailBoxTypeE'              , 'ポスト：タイプE'),
		('TrashBox'                  , 'ゴミ箱'),
		('SingInsect'                , '鳴くムシ'),
		('MoveBox'                   , '初期支給プレゼントBOX'),
		('MyDesignRug'               , 'マイデザインラグ'),
		('MusicJacket'               , 'ミュージックジャケット'),
		('Bromide'                   , 'ブロマイド'),
	))
	_daf0238c = Enum(0xdaf0238c, (
		('Sale'      , '販売品'),
		('NotForSale', '非売品'),
		('NotSee'    , '掲載不可'),
	))
	_8900b8a0 = U32(0x8900b8a0)
	_db1a2f07 = Enum(0xdb1a2f07, (
		('None'                     , 'なし'),
		('ShopDefault'              , '店_初期'),
		('ShopMiscGoods'            , '店_雑貨'),
		('ShopLargeGoods'           , '店_大型'),
		('ShopHighClass'            , '店_高級'),
		('ShopLv1'                  , '店_店舗小'),
		('ShopLv2'                  , '店_店舗大'),
		('ShopSeasonSale'           , '店_季節限定'),
		('MarketAlways'             , '店_固定'),
		('DefaultFtr'               , '初期支給家具'),
		('MarketingRouteA'          , '店_流通A(家具設定不可)'),
		('MarketingRouteC'          , '店_流通C(家具設定不可)'),
		('MarketingRouteB'          , '店_流通B(家具設定不可)'),
		('MarketingRouteD'          , '店_流通D(家具設定不可)'),
		('ShopUmbrellaLv1'          , '店_カサ小'),
		('ShopUmbrellaLv2'          , '店_カサ大'),
		('ShopWrappingPaper'        , '店_ラッピングペーパー'),
		('ShopCracker'              , '店_クラッカー'),
		('ShopTimer'                , '店_店舗大固定'),
		('ShopVarietyFishingRod'    , '店_店売り：つりざお'),
		('ShopVarietyNet'           , '店_店売り：あみ'),
		('ShopVarietyShovel'        , '店_店売り：スコップ'),
		('ShopVarietyWatering'      , '店_店売り：ジョウロ'),
		('ShopVarietySlingShot'     , '店_店売り：パチンコ'),
		('Shop_EnableShovel'        , '店_スコップ解禁'),
		('Shop_EnableAxe'           , '店_オノ解禁'),
		('ShopRecipeBook2'          , '店_レシピブック2'),
		('ShopRemakeKit'            , '店_リメイクキット'),
		('Shop_EnableRecipeWatering', '店_レシピ解禁(ジョウロ)'),
		('Shop_EnableRecipeScoop'   , '店_レシピ解禁(スコップ高跳び)'),
		('Shop_EnableRecipeLadder'  , '店_レシピ解禁(ハシゴ)'),
		('SonkatsuRewardTent'       , 'マイル交換_初期'),
		('SonkatsuRewardShop'       , 'マイル交換_プラス'),
		('MileExchangeOnce'         , 'マイル交換_プラス(買い切り)'),
		('SonkatsuReward2'          , 'マイル交換_案内所'),
		('MileExchangePhoneCase'    , 'マイル交換_スマホケース'),
		('MileExchangeLicense'      , 'マイル交換_工事ライセンス(買い切り)'),
		('MileExchangePocket40'     , 'マイル交換_持ち物欄40(買い切り)'),
		('MileExchangeRecipe1'      , 'マイル交換_家具レシピ800'),
		('MileExchangeRecipe2'      , 'マイル交換_家具レシピ1500'),
		('MileExchangeRecipe3'      , 'マイル交換_家具レシピ2000'),
		('MileExchangeRecipe4'      , 'マイル交換_家具レシピ3000'),
		('MileExchangeRecipe5'      , 'マイル交換_家具レシピ5000'),
		('MileExchangeNsoPresent'   , 'マイル交換_NSO加入特典'),
		('Bridge'                   , '案内所_橋'),
		('Slope'                    , '案内所_坂'),
		('OnlineShoppingOnly'       , '通信販売のみ'),
		('Tailor'                   , '仕立て屋'),
		('TailorMarketOnly'         , '仕立て屋_店舗'),
		('TailorXmas'               , '仕立て屋_クリスマス'),
		('TailorMarketOnlyXmas'     , '仕立て屋_店舗_クリスマス'),
		('RugS'                     , 'ローラン_S'),
		('RugM'                     , 'ローラン_M'),
		('RugL'                     , 'ローラン_L'),
		('LaurentWallFloor'         , 'ローラン壁床'),
		('ShoesBagShop'             , 'シャンク'),
		('HgcQuestReward'           , 'ことの報酬'),
		('TkkGood'                  , 'とたけけ_ゴキゲン！'),
		('TkkBad'                   , 'とたけけ_フキゲン'),
		('TkkRelax'                 , 'とたけけ_まったり'),
		('TkkBlue'                  , 'とたけけ_ブルーかも'),
		('TkkUnsure'                , 'とたけけ_よくわからない'),
		('TkkHidden'                , 'とたけけ_隠し曲'),
		('TkkMiss'                  , 'とたけけ_はずれ曲'),
		('TkkBirthday'              , 'とたけけ_誕生日曲'),
		('TkkFirst'                 , 'とたけけ_初ライブ曲'),
		('TkkNewGood'               , 'とたけけ新曲_ゴキゲン！'),
		('TkkNewBad'                , 'とたけけ新曲_フキゲン'),
		('TkkNewRelax'              , 'とたけけ新曲_まったり'),
		('TkkNewBlue'               , 'とたけけ新曲_ブルーかも'),
		('TkkNewUnsure'             , 'とたけけ新曲_よくわからない'),
		('TkkNew'                   , 'とたけけ_新曲'),
		('TreasureQuest'            , '宝探しクエスト'),
		('TreasureQuestDust'        , '宝探しクエストごみ'),
		('SnowmanReward'            , 'ゆきだるま'),
		('PcBday'                   , 'PC誕生日'),
		('JohnnyQuest'              , 'ジョニークエスト'),
		('JohnnyQuestDust'          , 'ジョニークエストごみ'),
		('JohnnyQuestReward'        , 'ジョニークエスト報酬'),
		('TournamentFishing'        , 'つり大会'),
		('TournamentInsect'         , 'ムシとり大会'),
		('CountDown'                , 'カウントダウン'),
		('BeyDailyFishModel'        , 'ジャスティン(来訪)'),
		('ChyDailyInsectModel'      , 'レオン(来訪)'),
		('RecycleBox'               , 'リサイクルBOX'),
		('ShopSeed_Chrysanthemum'   , '販売種_菊'),
		('ShopSeed_Lily'            , '販売種_ユリ'),
		('ShopSeed_Cosmos'          , '販売種_コスモス'),
		('ShopSeed_Hyacinth'        , '販売種_ヒヤシンス'),
		('ShopSeed_Rose'            , '販売種_バラ'),
		('ShopSeed_Anemone'         , '販売種_アネモネ'),
		('ShopSeed_Tulip'           , '販売種_チューリップ'),
		('ShopSeed_Pansy'           , '販売種_パンジー'),
		('FruitApple'               , '<フルーツ>リンゴ'),
		('FruitOrange'              , '<フルーツ>オレンジ'),
		('FruitPear'                , '<フルーツ>ナシ'),
		('FruitPeach'               , '<フルーツ>モモ'),
		('FruitCherry'              , '<フルーツ>サクランボ'),
		('Insect'                   , '生き物：ムシ'),
		('Fish'                     , '生き物：サカナ'),
		('Fossil'                   , '化石'),
		('Flower'                   , '植物：花'),
		('Bromide'                  , 'ブロマイド'),
		('Poster'                   , 'ポスター'),
		('HHAGift'                  , 'HHA報酬'),
		('Trophy'                   , 'トロフィー'),
		('Mother'                   , 'はは'),
		('AirportNovelty'           , '飛行場記念品'),
		('ShopDIY'                  , '<DIY素材>'),
		('DIYNormal'                , '<DIY>汎用'),
		('Fence'                    , '<DIY>柵'),
		('DIY_Mushroom'             , '<DIY>きのこ'),
		('DIYZodiac'                , '<DIY>12星座'),
		('DIYSpringBamboo'          , '<DIY>春の若竹'),
		('DIYSummerShell'           , '<DIY>夏の貝がら'),
		('DIYAutmnNuts'             , '<DIY>秋の木の実'),
		('DIYOrnament'              , '<DIY>オーナメント'),
		('DIYMapleLeaf'             , '<DIY>もみじのはっぱ'),
		('DIYCherryBrossom'         , '<DIY>桜の花びら'),
		('DIYSnowCrystal'           , '<DIY>雪の結晶'),
		('DIYEasterEgg'             , '<DIY>イースターのたまご'),
		('DeliveryPocketCamp'       , '<永続配信>ポケ森コラボ'),
		('Easter'                   , 'イースター'),
		('FutureItem'               , '■アップデート向け■'),
		('NotAvailable'             , '◆入手不可◆'),
	))
	_f80e9fee = Enum(0xf80e9fee, enum_GenderBias)
	_f17f8753 = Enum(0xf17f8753, (
		('None'             , 'なし'),
		('Pet'              , '生き物'),
		('Audio'            , 'オーディオ'),
		('MusicalInstrument', '楽器'),
		('Plant'            , '観葉植物'),
		('Trash'            , 'ゴミ箱'),
		('SmallGoods'       , '小物'),
		('Lighting'         , '照明'),
		('TV'               , 'テレビ'),
		('Clock'            , '時計'),
		('AC'               , '冷暖房'),
		('Dresser'          , 'ドレッサー'),
		('Appliance'        , '家電'),
		('Doll'             , '人形'),
	))
	_16a66e06 = Enum(0x16a66e06, (
		('None'         , 'なし'),
		('Chair'        , 'イス'),
		('ChestOrCloset', 'タンス・クロゼット'),
		('Table'        , 'テーブル'),
		('Bed'          , 'ベッド'),
	))
	_05639ab0 = Enum(0x05639ab0, (
		('None'  , 'なし'),
		('All'   , '通年'),
		('Spring', '春'),
		('Summer', '夏'),
		('Autum' , '秋'),
		('Winter', '冬'),
	))
	_059d1682 = Enum(0x059d1682, (
		('None'    , 'なし'),
		('Stone'   , 'いし'),
		('Office'  , 'オフィス'),
		('Learning', 'がくしゅう'),
		('Collage' , 'こうぎしつ'),
		('Study'   , 'しょさい'),
		('Birthday', 'バースデー'),
		('Apple'   , 'リンゴ'),
		('Peach'   , 'モモ'),
		('Cherry'  , 'さくらんぼ'),
		('Orange'  , 'オレンジ'),
		('Pear'    , 'ナシ'),
		('School'  , 'がっこう'),
		('Chinese' , 'ちゅうか'),
		('Panda'   , 'パンダ'),
		('Bear'    , 'クマ'),
		('Standee' , 'ハリボテ'),
		('Natural' , 'ナチュラル'),
		('Pet'     , 'ペット'),
		('Ring'    , 'リング'),
	))
	_a7c79784 = Enum(0xa7c79784, enum_b6bafdfd)
	_b6bafdfd = Enum(0xb6bafdfd, enum_b6bafdfd)
	_d61205d0 = Enum(0xd61205d0, (
		('None'         , 'なし'),
		('Iron'         , 'アイアン'),
		('IronWood'     , 'アイアンウッド'),
		('AmericanRetro', 'ダイナー'),
		('Antique'      , 'アンティーク'),
		('Gold'         , 'おうごん'),
		('Oriental'     , 'オリエンタル'),
		('Shell'        , 'かいがら'),
		('Mushroom'     , 'キノコ'),
		('Cute'         , 'キュート'),
		('Bamboo'       , 'たけ'),
		('Block'        , 'つみき'),
		('Halloween'    , 'ハロウィン'),
		('Fruit'        , 'フルーツ'),
		('Log'          , 'まるた'),
		('Wooden'       , 'もくせい'),
		('Rattan'       , 'ラタン'),
		('Rock'         , 'TOY'),
		('Ice'          , 'こおり'),
		('Star'         , 'ほし'),
		('Flower'       , 'はな'),
		('Nut'          , 'きのみ・おちば'),
		('CherryBlossom', 'さくら'),
		('Cardboard'    , 'ダンボール'),
		('Mother'       , 'はは'),
		('Christmas'    , 'クリスマス'),
		('Easter'       , 'イースター'),
	))
	_7b2fdfc1 = Enum(0x7b2fdfc1, enum_NoneHighNormalLow)
	_5270eb75 = Enum(0x5270eb75, (
		('Ftr'               , '家具'),
		('RoomWall'          , '内装：壁紙'),
		('RoomFloor'         , '内装：床板'),
		('Rug'               , 'ラグ'),
		('RugMyDesign'       , 'ラグマイデザイン'),
		('TopsDefault'       , '装備品：トップスデフォルト'),
		('Tops'              , '装備品：トップス'),
		('OnePiece'          , '装備品：ワンピース'),
		('BottomsDefault'    , '装備品：ボトムスデフォルト'),
		('Bottoms'           , '装備品：ボトムス'),
		('Socks'             , '装備品：くつした'),
		('Shoes'             , '装備品：くつ'),
		('Cap'               , '装備品：ぼうし'),
		('Helmet'            , '装備品：かぶりもの'),
		('Accessory'         , '装備品：アクセサリ'),
		('Bag'               , '装備品：バッグ'),
		('Umbrella'          , '装備品：かさ'),
		('FishingRod'        , '道具：つりざお'),
		('Net'               , '道具：あみ'),
		('Shovel'            , '道具：スコップ'),
		('Axe'               , '道具：オノ'),
		('Watering'          , '道具：じょうろ'),
		('Slingshot'         , '道具：パチンコ'),
		('ChangeStick'       , '道具：変身ステッキ'),
		('WoodenStickTool'   , '道具：川越えツール'),
		('Ladder'            , '道具：ハシゴ'),
		('GroundMaker'       , '道具：道造成キット'),
		('RiverMaker'        , '道具：川造成キット'),
		('CliffMaker'        , '道具：崖造成キット'),
		('PartyPopper'       , 'サブ道具：クラッカー'),
		('Ocarina'           , 'サブ道具：オカリナ'),
		('Panflute'          , 'サブ道具：パンフルート'),
		('Tambourine'        , 'サブ道具：タンバリン'),
		('FierworkHand'      , 'サブ道具：手持ち花火'),
		('StickLight'        , 'サブ道具：スティックライト'),
		('Uchiwa'            , 'サブ道具：うちわ'),
		('BlowBubble'        , 'サブ道具：シャボン玉'),
		('Partyhorn'         , 'サブ道具：ふきもどし'),
		('Timer'             , 'タイマー'),
		('TreeSeedling'      , '植物：木の苗'),
		('Tree'              , '植物：木'),
		('Vegetable'         , '植物：野菜'),
		('Weed'              , '植物：雑草'),
		('FlowerSeed'        , '植物：花の種'),
		('FlowerBud'         , '植物：花の茎、蕾、株'),
		('Flower'            , '植物：花'),
		('Fruit'             , 'フルーツ'),
		('Mushroom'          , 'キノコ'),
		('Turnip'            , 'カブ'),
		('TurnipExpired'     , 'カブ（くさったカブ）'),
		('FishBait'          , '撒き餌'),
		('PitFallSeed'       , 'おとしあなのタネ'),
		('Medicine'          , 'おくすり'),
		('CraftMaterial'     , '素材：DIY'),
		('CraftRemake'       , '素材：リメイクキット'),
		('Ore'               , '素材：鉱石'),
		('CraftPhoneCase'    , '素材：スマホケース'),
		('Honeycomb'         , 'ハチの巣'),
		('Trash'             , 'ゴミ'),
		('SnowCrystal'       , '雪の結晶'),
		('AutumnLeaf'        , '紅葉'),
		('Sakurapetal'       , '桜の花びら'),
		('XmasDeco'          , 'クリスマスオーナメント'),
		('StarPiece'         , '星のかけら'),
		('Insect'            , '生き物：ムシ'),
		('Fish'              , '生き物：サカナ'),
		('ShellDrift'        , '漂着貝'),
		('ShellFish'         , '生き物：潮干狩り貝'),
		('FishToy'           , 'サカナ模型'),
		('InsectToy'         , 'ムシ模型'),
		('Fossil'            , '化石'),
		('FossilUnknown'     , '化石（未鑑定）'),
		('Music'             , 'ミュージック'),
		('MusicMiss'         , 'ミュージック(入手不可)'),
		('Bromide'           , 'ブロマイド'),
		('Poster'            , 'ポスター'),
		('HousePost'         , '家パーツポスト'),
		('DoorDeco'          , 'ドア飾り'),
		('Fence'             , '柵'),
		('DummyRecipe'       , '陳列用：レシピブック'),
		('DummyDIYRecipe'    , '陳列用：単品DIYレシピ'),
		('DummyHowtoBook'    , '陳列用：ハウツー本'),
		('LicenseItem'       , '陳列用：工事ライセンス'),
		('BridgeItem'        , '陳列用：橋'),
		('SlopeItem'         , '陳列用：坂'),
		('DIYRecipe'         , 'DIYレシピ'),
		('MessageBottle'     , 'メッセージボトル'),
		('WrappingPaper'     , 'ラッピングペーパー'),
		('HousingKit'        , 'ハウジングキット'),
		('HousingKitRcoQuest', 'ハウジングキット：移住クエスト'),
		('HousingKitBirdge'  , 'ハウジングキット：橋用'),
		('Money'             , 'ベル（お金）'),
		('BdayCupcake'       , 'バースデーカップケーキ'),
		('YutaroWisp'        , 'ゆうたろうのたましい'),
		('JohnnyQuest'       , 'ジョニークエスト'),
		('JohnnyQuestDust'   , 'ジョニークエストごみ'),
		('QuestWrapping'     , 'クエスト配達プレゼントBOX'),
		('LostQuest'         , 'おとしもの'),
		('LostQuestDust'     , 'おとしものゴミ'),
		('TailorTicket'      , '仕立て屋クーポン'),
		('TreasureQuest'     , '宝探しカプセル'),
		('TreasureQuestDust' , '宝探しカプセルごみ'),
		('MilePlaneTicket'   , 'マイル航空券'),
		('RollanTicket'      , 'ローラン引換券'),
		('EasterEgg'         , 'イースターのたまご'),
		('Giftbox'           , '初期支給プレゼントBOX'),
		('PinataStick'       , '装備専用：ピニャータ割り棒'),
		('NpcOutfit'         , '装備品：NPC専用'),
		('PlayerDemoOutfit'  , '装備品：プレイヤ演出専用'),
		('SmartPhone'        , 'スマホ'),
		('DummyFtr'          , 'ダミー家具'),
		('SequenceOnly'      , 'シーケンス専用'),
		('MyDesignObject'    , 'マイデザインオブジェクト'),
		('MyDesignTexture'   , 'マイデザインテクスチャ'),
		('None'              , 'なし'),
		('DummyWrapping'     , 'ダミーラッピング済アイテム'),
		('DummyPresentbox'   , 'ダミープレゼントBOX'),
		('DummyCardboard'    , 'ダミーダンボール入りアイテム'),
		('EventObjFtr'       , 'イベントオブジェ家具'),
		('NnpcRoomMarker'    , 'NPC部屋マーカー'),
		('PhotoStudioList'   , '撮影スタジオ用アイテム'),
	))
	_9dcea17e = Enum(0x9dcea17e, (
		('Floor'            , '床置き'),
		('Floor_Downer'     , '台になる'),
		('Floor_DownerLeft' , '台になる：左半分'),
		('Floor_DownerRight', '台になる：右半分'),
		('Floor_DownerFront', '台になる：手前半分'),
		('Floor_DownerUpper', '台になる：上物可'),
		('Floor_Upper'      , '上物可'),
		('Floor_Gate'       , '床置き：門：3x1'),
		('Floor_Corner'     , '床置き：コーナー：3x3'),
		('Wall_NoCol'       , '壁掛け：0'),
		('Wall_HalfUnit'    , '壁掛け：0.5'),
		('Wall_1Unit'       , '壁掛け：1'),
		('Rug'              , 'ラグ'),
	))
	_a69385c1 = Enum(0xa69385c1, enum_c54eaad9)
	_7dcd5be1 = Enum(0x7dcd5be1, enum_NoneHighNormalLow)
	_70e19913 = Enum(0x70e19913, (
		('None'             , '-'),
		('BabyFtr'          , 'ベビーキッズ家具'),
		('ToyFtr'           , 'TOY家具'),
		('CostumeClothes'   , 'コスチューム'),
		('BorderClothes'    , 'ボーダー服'),
		('FitnessFtr'       , 'フィットネス家具'),
		('SportsFtr'        , 'スポーツ家具'),
		('SchoolFtr'        , '学校家具'),
		('SportClothes'     , 'スポーツウェア'),
		('OutdoorFtr'       , 'アウトドア家具'),
		('LongsleeveClothes', '長袖の服'),
		('CoolHats'         , 'おしゃれ帽子'),
		('CoolShoes'        , 'おしゃれ靴'),
		('CoolUmbrella'     , 'おしゃれカサ'),
		('CoolClothes'      , 'おしゃれ服'),
		('TeatimeFtr'       , 'ティータイム家具'),
		('StationeryFtr'    , '文具系家具'),
		('TidyClothes'      , '清楚系服'),
		('KitchenFtr'       , 'キッチン家具'),
		('AdultGlasses'     , 'オトナメガネ'),
		('LightFtr'         , '照明'),
		('BathGoods'        , 'バスグッズ'),
		('CardiganClothes'  , 'カーディガン'),
		('PlantsFtr'        , '植物'),
		('FlowerSeeds'      , '花の種'),
		('CuteUmbrella'     , 'カサ'),
		('CuteClothes'      , 'かわいい服'),
		('TeddyFtr'         , 'クマ家具'),
		('CuteFtr'          , 'キュート'),
		('DailyFtr'         , '生活用品'),
		('BadClothes'       , 'ヤンキー服'),
		('MusicFtr'         , '音楽プレイヤー'),
		('RockFtr'          , 'ロック家具'),
		('HHA1'             , 'HHA_1_汎用'),
		('HHA2'             , 'HHA_2_家電'),
		('HHA3'             , 'HHA_3_勉強部屋'),
		('HHA4'             , 'HHA_4_キッチン'),
		('HHA5_1'           , 'HHA_5_趣味_ライブ'),
		('HHA5_2'           , 'HHA_5_趣味_フィットネス'),
		('HHA5_3'           , 'HHA_5_趣味_音楽'),
		('HHA6'             , 'HHA_6_バス'),
		('HHA7'             , 'HHA_7_植物'),
		('HHA3_NPC'         , 'HHA_3_NPC_勉強部屋'),
		('HHA4_NPC'         , 'HHA_4_NPC_キッチン'),
		('HHA5_1_NPC'       , 'HHA_5_NPC_趣味_ライブ'),
		('HHA5_2_NPC'       , 'HHA_5_NPC_趣味_フィットネス'),
		('HHA5_3_NPC'       , 'HHA_5_NPC_趣味_音楽'),
		('HHA6_NPC'         , 'HHA_6_NPC_バス'),
		('HHA_FixesPoints1' , 'HHA_規定の点数1'),
		('HHA_FixesPoints2' , 'HHA_規定の点数2'),
		('HHA_FixesPoints3' , 'HHA_規定の点数3'),
		('HHA_FixesPoints4' , 'HHA_規定の点数4'),
		('HHA_FixesPoints5' , 'HHA_規定の点数5'),
		('HHA_FixesPoints6' , 'HHA_規定の点数6'),
		('HHA_FixesPoints7' , 'HHA_規定の点数7'),
		('CoolFurniture'    , 'おしゃれ家具'),
		('Clock'            , '時計'),
		('LittleFtr'        , '小さめの家具'),
		('RoughShoes'       , 'しぶい靴'),
		('UiniqueFtr'       , '珍家具'),
	))
	_348d7b06 = Enum(0x348d7b06, (
		('Leaf'                , '葉っぱ'),
		('LeafDesign'          , '葉っぱ（マイデザイン）'),
		('Wall'                , '壁紙'),
		('Floor'               , '床板'),
		('Carpet'              , 'ラグ'),
		('Tops'                , '装備品：トップス'),
		('Bottoms'             , '装備品：ボトムス'),
		('Onepiece'            , '装備品：ワンピース'),
		('Socks'               , '装備品：靴下'),
		('Shoes'               , '装備品：靴'),
		('Cap'                 , '装備品：帽子'),
		('Wig'                 , '装備品：かぶりもの'),
		('Glasses'             , '装備品：メガネ'),
		('Bag'                 , '装備品：バッグ'),
		('Umbrella'            , '装備品：かさ'),
		('Fishingrod'          , 'つりざお'),
		('GFishingrod'         , 'つりざお：金'),
		('Net'                 , 'あみ'),
		('GNet'                , 'あみ：金'),
		('Scoop'               , 'スコップ'),
		('Gscoop'              , 'スコップ：金'),
		('Axe'                 , 'オノ'),
		('GAxe'                , 'オノ：金'),
		('AxeDull'             , 'オノ（切れない）'),
		('Watering'            , 'じょうろ'),
		('GWatering'           , 'じょうろ：金'),
		('Pachinko'            , 'パチンコ'),
		('GPachinko'           , 'パチンコ：金'),
		('ToolChangeStick'     , '変身ステッキ'),
		('ToolRiverJump'       , '川越えツール'),
		('ToolLadder'          , 'ハシゴ'),
		('Bridge'              , '橋'),
		('Slope'               , '坂'),
		('ToolGroundMaker'     , '道造成キット'),
		('ToolRiverMaker'      , '川造成キット'),
		('ToolCliffMaker'      , '崖造成キット'),
		('Helmet'              , 'たぬき開発ヘルメット'),
		('Fence'               , '柵'),
		('Post'                , 'ポスト'),
		('Tent'                , 'ハウジングキット：黄'),
		('TentWhite'           , 'ハウジングキット：白'),
		('Cracker'             , 'クラッカー'),
		('Ocarina'             , 'オカリナ'),
		('Panflute'            , 'パンフルート'),
		('Tambourine'          , 'タンバリン'),
		('GlowStick'           , 'スティックライト'),
		('Uchiwa'              , 'うちわ'),
		('Music'               , 'ミュージック'),
		('Fossil'              , '化石'),
		('FossilJ'             , '鑑定済化石'),
		('SeedPitfall'         , 'おとしあなのタネ'),
		('RemakeKit'           , 'リメイクキット'),
		('SmartphoneCase'      , 'スマホケース'),
		('Medicine'            , 'おくすり'),
		('Timer'               , 'タイマー'),
		('Honeycomb'           , 'ハチの巣'),
		('FishBait'            , 'サカナの撒き餌'),
		('Cardboard'           , 'ダンボール'),
		('Present'             , 'プレゼントBOX'),
		('Present2'            , 'プレゼントBOX：クエスト用'),
		('WrappingPaper'       , 'ラッピング済みアイテム'),
		('WPaperYellow'        , 'ラッピングペーパー：イエロー'),
		('WPaperPink'          , 'ラッピングペーパー：ピンク'),
		('WPaperOrange'        , 'ラッピングペーパー：オレンジ'),
		('WPaperLightGreen'    , 'ラッピングペーパー：キミドリ'),
		('WPaperGreen'         , 'ラッピングペーパー：ミドリ'),
		('WPaperMint'          , 'ラッピングペーパー：ミント'),
		('WPaperLightBlue'     , 'ラッピングペーパー：ライトブルー'),
		('WPaperPurple'        , 'ラッピングペーパー：パープル'),
		('WPaperNavy'          , 'ラッピングペーパー：ネイビー'),
		('WPaperBlue'          , 'ラッピングペーパー：ブルー'),
		('WPaperWhite'         , 'ラッピングペーパー：ホワイト'),
		('WPaperRed'           , 'ラッピングペーパー：レッド'),
		('WPaperGold'          , 'ラッピングペーパー：ゴールド'),
		('WPaperBrown'         , 'ラッピングペーパー：ブラウン'),
		('WPaperGray'          , 'ラッピングペーパー：グレー'),
		('WPaperBlack'         , 'ラッピングペーパー：ブラック'),
		('WBagYellow'          , 'ラッピング袋：イエロー'),
		('WBagPink'            , 'ラッピング袋：ピンク'),
		('WBagOrange'          , 'ラッピング袋：オレンジ'),
		('WBagLightGreen'      , 'ラッピング袋：キミドリ'),
		('WBagGreen'           , 'ラッピング袋：ミドリ'),
		('WBagMint'            , 'ラッピング袋：ミント'),
		('WBagLightBlue'       , 'ラッピング袋：ライトブルー'),
		('WBagPurple'          , 'ラッピング袋：パープル'),
		('WBagNavy'            , 'ラッピング袋：ネイビー'),
		('WBagBlue'            , 'ラッピング袋：ブルー'),
		('WBagWhite'           , 'ラッピング袋：ホワイト'),
		('WBagRed'             , 'ラッピング袋：レッド'),
		('WBagGold'            , 'ラッピング袋：ゴールド'),
		('WBagBrown'           , 'ラッピング袋：ブラウン'),
		('WBagGary'            , 'ラッピング袋：グレー'),
		('WBagBlack'           , 'ラッピング袋：ブラック'),
		('YellowPaperBag'      , '汎用紙袋'),
		('Coin'                , 'ベル：コイン'),
		('MoneyBag010'         , 'ベル：金袋小'),
		('MoneyBag039'         , 'ベル：金袋中'),
		('MoneyBag069'         , 'ベル：金袋大'),
		('Book'                , '落とし物：本'),
		('LostQuestPorch'      , '落とし物：巾着'),
		('LostQuestMemo'       , '落とし物：本（かきもの）'),
		('Porch'               , '落とし物：ポーチ'),
		('OddGlove'            , '落とし物：片方の手袋'),
		('AutumnLeaf'          , 'もみじのはっぱ'),
		('SnowCrystal'         , '雪の結晶'),
		('SnowCrystalLarge'    , '雪の大結晶'),
		('Sakurapetal'         , 'さくらのはなびら'),
		('StarPiece'           , 'ほしのかけら'),
		('StarPieceRare'       , 'ほしのかけら：レア'),
		('StarPieceSeason'     , 'xほしのかけら：季節'),
		('ChristmasOrnamentA'  , 'クリスマスオーナメント赤'),
		('StarpieceCapricornus', 'やぎざのかけら'),
		('ChristmasOrnamentB'  , 'クリスマスオーナメント青'),
		('StarpieceAquarius'   , 'みずがめざのかけら'),
		('ChristmasOrnamentC'  , 'クリスマスオーナメント金'),
		('StarpiecePisces'     , 'うおざのかけら'),
		('StarpieceAries'      , 'おひつじざのかけら'),
		('JohnyParts'          , 'つうしんそうちのパーツ'),
		('StarpieceTaurus'     , 'おうしざのかけら'),
		('JohnnyQuestDust1'    , 'さびたパーツ'),
		('StarpieceGemini'     , 'ふたござのかけら'),
		('StarpieceCancer'     , 'かにざのかけら'),
		('StarpieceLeo'        , 'ししざのかけら'),
		('StarpieceVirgo'      , 'おとめざのかけら'),
		('StarpieceLibra'      , 'てんびんざのかけら'),
		('StarpieceScorpio'    , 'さそりざのかけら'),
		('StarpieceSagittarius', 'いてざのかけら'),
		('YutaroWisp'          , 'ゆうたろうのたましい'),
		('BdayCupcake'         , 'バースデーカップケーキ'),
		('BottleRecipe'        , 'メッセージボトル'),
		('PaperRecipe'         , 'レシピ'),
		('DIYRecipeFence'      , 'レシピ：柵'),
		('DIYRecipeFtr'        , 'レシピ：家具'),
		('BookRecipe'          , 'レシピ本'),
		('HowtoBookHair'       , 'ハウツー本：髪'),
		('HowtoBookExpansion'  , 'ハウツー本：機能拡張'),
		('MyDesignPro'         , 'マイデザインPRO'),
		('PlaneTicket'         , 'こうくうけん'),
		('TailorTicket'        , 'したてやひきかえけん'),
		('BellExchangeTicket'  , 'ベルひきかえけん'),
		('RollanTicket'        , 'ローランひきかえけん'),
		('OreStone'            , '鉱石：いし'),
		('OreClay'             , '鉱石：ねんど'),
		('OreIron'             , '鉱石：鉄鉱石'),
		('OreGold'             , '鉱石：金鉱石'),
		('Shell0'              , 'アコヤガイのかいがら'),
		('Oyster'              , 'カキのかいがら'),
		('Shell1'              , 'ホラガイ'),
		('Shell2'              , 'シャコガイ'),
		('Shell3'              , 'サンゴ'),
		('Shell4'              , 'ホネガイ'),
		('Shell5'              , 'ホタテガイ'),
		('Shell6'              , 'エビスガイ'),
		('Shell7'              , 'タカラガイ'),
		('Shell8'              , 'サンドダラー'),
		('ShellSummer'         , 'なつのかいがら'),
		('ShellFIshAsari'      , 'アサリ'),
		('InsAmenbo'           , 'アメンボ'),
		('InsAri'              , 'アリ'),
		('InsOkera'            , 'オケラ'),
		('InsKa'               , 'カ'),
		('InsGa'               , 'ガ'),
		('InsNishikiohtsu'     , 'ニシキオオツバメガ'),
		('InsKumo'             , 'クモ'),
		('InsMinomushi'        , 'ミノムシ'),
		('InsGengorou'         , 'ゲンゴロウ'),
		('InsKonohamushi'      , 'コノハムシ'),
		('InsSasori'           , 'サソリ'),
		('InsTaranchura'       , 'タランチュラ'),
		('InsHachi'            , 'ハチ'),
		('InsAburazemi'        , 'アブラゼミ'),
		('InsKumazemi'         , 'クマゼミ'),
		('InsTsukutsuku'       , 'ツクツクホウシ'),
		('InsHigurashi'        , 'ヒグラシ'),
		('InsMinminzemi'       , 'ミンミンゼミ'),
		('InsSeminonukegara'   , 'セミのぬけがら'),
		('InsDangomushi'       , 'ダンゴムシ'),
		('InsMukade'           , 'ムカデ'),
		('InsAosuji'           , 'アオスジアゲハ'),
		('InsAkaeri'           , 'アカエリアゲハ'),
		('InsAgehacho'         , 'アゲハチョウ'),
		('InsArekisandora'     , 'アレクサンドラアゲハ'),
		('InsOhkabamadara'     , 'オオカバマダラ'),
		('InsOhgomamadara'     , 'オオゴマダラ'),
		('InsOhmurasaki'       , 'オオムラサキ'),
		('InsKarasuageha'      , 'カラスアゲハ'),
		('InsMiirotateha'      , 'ミイロタテハ'),
		('InsMorufuocho'       , 'モルフォチョウ'),
		('InsMonkicho'         , 'モンキチョウ'),
		('InsMonshirocho'      , 'モンシロチョウ'),
		('InsAkiakane'         , 'アキアカネ'),
		('InsOniyanma'         , 'オニヤンマ'),
		('InsGinyanma'         , 'ギンヤンマ'),
		('Itotonbo'            , 'イトトンボ'),
		('InsNomi'             , 'ノミ'),
		('InsHae'              , 'ハエ'),
		('InsInago'            , 'イナゴ'),
		('InsKirigirisu'       , 'キリギリス'),
		('InsKohrogi'          , 'コオロギ'),
		('InsShoryobatta'      , 'ショウリョウバッタ'),
		('InsSuzumushi'        , 'スズムシ'),
		('InsTonosamabatta'    , 'トノサマバッタ'),
		('InsHanmyou'          , 'ハンミョウ'),
		('InsFunamushi'        , 'フナムシ'),
		('InsFunkorogashi'     , 'フンコロガシ'),
		('InsHotaru'           , 'ホタル'),
		('InsMitsubachi'       , 'ミツバチ'),
		('InsYadokari'         , 'ヤドカリ'),
		('InsGomadarakamikiri' , 'カミキリムシ'),
		('InsBaiorinmushi'     , 'バイオリンムシ'),
		('InsRuriboshikamikiri', 'ルリボシカミキリ'),
		('InsOugononikuwa'     , 'オウゴンオニクワガタ'),
		('InsOhkuwagata'       , 'オオクワガタ'),
		('InsOhsenchikogane'   , 'コガネムシ'),
		('InsKanabun'          , 'カナブン'),
		('InsKabutomushi'      , 'カブトムシ'),
		('InsKamemushi'        , 'カメムシ'),
		('InsGirafanokogiri'   , 'ギラファノコギリクワ'),
		('InsKohkasasu'        , 'コーカサスオオカブト'),
		('InsGoraiasu'         , 'ゴライアスハナムグリ'),
		('InsJinmenkamemushi'  , 'ジンメンカメムシ'),
		('InsZoukabuto'        , 'ゾウカブト'),
		('InsTamamushi'        , 'タマムシ'),
		('InsNanafushi'        , 'ナナフシ'),
		('InsNijiirokuwagata'  , 'ニジイロクワガタ'),
		('InsNokogirikuwagata' , 'ノコギリクワガタ'),
		('InsPurachinakogane'  , 'プラチナコガネ'),
		('InsHerakuresu'       , 'ヘラクレスオオカブト'),
		('InsHousekizoumushi'  , 'ホウセキゾウムシ'),
		('InsHosoakakuwagata'  , 'ホソアカクワガタ'),
		('InsMiyamakuwagata'   , 'ミヤマクワガタ'),
		('InsYonagunisan'      , 'ヨナグニサン'),
		('InsKatatsumuri'      , 'カタツムリ'),
		('InsKamakiri'         , 'カマキリ'),
		('FtrInsectTagame'     , 'タガメ'),
		('InsTentoumushi'      , 'テントウムシ'),
		('InsHanakamakiri'     , 'ハナカマキリ'),
		('FishAyu'             , 'アユ'),
		('FishArowana'         , 'アロワナ'),
		('FishYellowparch'     , 'イエローパーチ'),
		('FishUgui'            , 'ウグイ'),
		('FtrFishRanchu'       , 'ランチュウ'),
		('FishAngelfish'       , 'エンゼルフィッシュ'),
		('FishEndorikerii'     , 'エンドリケリー'),
		('FishOikawa'          , 'オイカワ'),
		('FishKamitsukigame'   , 'カミツキガメ'),
		('FishGuppi'           , 'グッピー'),
		('FishSyanhaigani'     , 'シャンハイガニ'),
		('FishSuppon'          , 'スッポン'),
		('FishTanago'          , 'タナゴ'),
		('FishThirapia'        , 'ティラピア'),
		('FishDemekin'         , 'デメキン'),
		('FishDokutaafish'     , 'ドクターフィッシュ'),
		('FishDojou'           , 'ドジョウ'),
		('FishDolado'          , 'ドラド'),
		('FishDonko'           , 'ドンコ'),
		('FishNeontetora'      , 'ネオンテトラ'),
		('FishPaiku'           , 'パイク'),
		('FishPirania'         , 'ピラニア'),
		('FishPiraruku'        , 'ピラルク'),
		('FishFuna'            , 'フナ'),
		('FishBlackbass'       , 'ブラックバス'),
		('FishBlueguill'       , 'ブルーギル'),
		('FishBeta'            , 'ベタ'),
		('FishRainbowfish'     , 'レインボーフィッシュ'),
		('FishWakasagi'        , 'ワカサギ'),
		('FishItou'            , 'イトウ'),
		('FishOoiwana'         , 'オオイワナ'),
		('FishGoldenTorauto'   , 'ゴールデントラウト'),
		('FishYamame'          , 'ヤマメ'),
		('FishOtamajakusi'     , 'オタマジャクシ'),
		('FishGa'              , 'ガー'),
		('FishKaeru'           , 'カエル'),
		('FishKingyo'          , 'キンギョ'),
		('FishKoi'             , 'コイ'),
		('FishZarigani'        , 'ザリガニ'),
		('FishNamazu'          , 'ナマズ'),
		('FishNishikigoi'      , 'ニシキゴイ'),
		('FishMedaka'          , 'メダカ'),
		('FishRaigyo'          , 'ライギョ'),
		('FishKingsalmon'      , 'キングサーモン'),
		('FishSake'            , 'サケ'),
		('FishTyouzame'        , 'チョウザメ'),
		('FishAji'             , 'アジ'),
		('FishAntyobi'         , 'アンチョビ'),
		('FishIka'             , 'イカ'),
		('FishIshidai'         , 'イシダイ'),
		('FishUtsubo'          , 'ウツボ'),
		('FishEi'              , 'エイ'),
		('FishKajiki'          , 'カジキ'),
		('FishKarei'           , 'カレイ'),
		('FishKumanomi'        , 'クマノミ'),
		('FishKurione'         , 'クリオネ'),
		('FishKobanzame'       , 'コバンザメ'),
		('FishSame'            , 'サメ'),
		('FishShiira'          , 'シイラ'),
		('FishSirakansu'       , 'シーラカンス'),
		('FishShumokuzame'     , 'シュモクザメ'),
		('FishJinbeezame'      , 'ジンベエザメ'),
		('FishSuzuki'          , 'スズキ'),
		('FishTai'             , 'タイ'),
		('FishTatsunootoshigo' , 'タツノオトシゴ'),
		('FishChouchouuo'      , 'チョウチョウウオ'),
		('FishChouchinankou'   , 'チョウチンアンコウ'),
		('FishDemenigisu'      , 'デメニギス'),
		('FishNaporeonfish'    , 'ナポレオンフィッシュ'),
		('FishNanyouhagi'      , 'ナンヨウハギ'),
		('FishNokogirizame'    , 'ノコギリザメ'),
		('FishHanahigeutubo'   , 'ハナヒゲウツボ'),
		('FishHarisenbon'      , 'ハリセンボン'),
		('FishHirame'          , 'ヒラメ'),
		('FishFugu'            , 'フグ'),
		('FishMaguro'          , 'マグロ'),
		('FishManbou'          , 'マンボウ'),
		('FishMinokasago'      , 'ミノカサゴ'),
		('FishRyuuguunotukai'  , 'リュウグウノツカイ'),
		('FishRouninaji'       , 'ロウニンアジ'),
		('Can'                 , 'あきカン'),
		('Boots'               , 'ながぐつ'),
		('Tire'                , 'タイヤ'),
		('Apple'               , 'リンゴ'),
		('Orange'              , 'オレンジ'),
		('Pear'                , 'ナシ'),
		('Peach'               , 'モモ'),
		('Cherry'              , 'さくらんぼ'),
		('Coconut'             , 'ヤシの実'),
		('BanbooShoot'         , 'たけのこ'),
		('Kabu'                , 'カブ'),
		('BadKabu'             , 'くさったカブ'),
		('SquashOrange'        , 'オレンジのカボチャ'),
		('SquashYellow'        , 'きいろいカボチャ'),
		('SquashGreen'         , 'みどりのカボチャ'),
		('SquashWhite'         , 'しろいカボチャ'),
		('Mush0'               , 'りっぱなキノコ'),
		('Mush1'               , 'まるいキノコ'),
		('Mush2'               , 'ほそいキノコ'),
		('Mush3'               , 'ひらたいキノコ'),
		('Mush4'               , 'めずらしいキノコ'),
		('DIYBranch'           , 'きのえだ'),
		('DIYPinecone'         , 'まつぼっくり'),
		('DIYAcorn'            , 'どんぐり'),
		('DIYWoodNormal'       , 'もくざい'),
		('DIYWoodSoft'         , 'やわらかいもくざい'),
		('DIYWoodHard'         , 'かたいもくざい'),
		('DIYBamboo'           , '竹材'),
		('DIYBambooSpring'     , 'はるのわかたけ'),
		('SeedPaperbag0'       , 'あかい種袋'),
		('SeedPaperbag1'       , 'しろい種袋'),
		('SeedPaperbag2'       , 'きいろい種袋'),
		('SeedPaperbag3'       , 'オレンジの種袋'),
		('Rose0'               , 'あかいバラ'),
		('Rose1'               , 'しろいバラ'),
		('Rose2'               , 'きいろいバラ'),
		('Rose3'               , 'ピンクのバラ'),
		('Rose4'               , 'オレンジのバラ'),
		('Rose5'               , 'むらさきのバラ'),
		('Rose6'               , 'くろいバラ'),
		('Rose7'               , 'あおいバラ'),
		('GoldenRose'          , '金のバラ'),
		('Cosmos0'             , 'しろいコスモス'),
		('Cosmos1'             , 'あかいコスモス'),
		('Cosmos2'             , 'きいろいコスモス'),
		('Cosmos3'             , 'ピンクのコスモス'),
		('Cosmos4'             , 'オレンジのコスモス'),
		('Cosmos5'             , 'くろいコスモス'),
		('Turip0'              , 'あかいチューリップ'),
		('Turip1'              , 'しろいチューリップ'),
		('Turip2'              , 'きいろいチューリップ'),
		('Turip3'              , 'ピンクのチューリップ'),
		('Turip4'              , 'むらさきチューリップ'),
		('Turip5'              , 'くろいチューリップ'),
		('Pansi0'              , 'しろいパンジー'),
		('Turip6'              , 'オレンジチューリップ'),
		('Pansi1'              , 'きいろいパンジー'),
		('Pansi2'              , 'あかいパンジー'),
		('Pansi3'              , 'むらさきのパンジー'),
		('Pansi4'              , 'あかきいろパンジー'),
		('Pansi5'              , 'あおいパンジー'),
		('Yuri0'               , 'しろいユリ'),
		('Yuri1'               , 'きいろいユリ'),
		('Yuri2'               , 'あかいユリ'),
		('Yuri3'               , 'オレンジのユリ'),
		('Yuri4'               , 'ピンクのユリ'),
		('Yuri5'               , 'くろいユリ'),
		('Anemone0'            , 'しろいアネモネ'),
		('Anemone1'            , 'あかいアネモネ'),
		('Anemone2'            , 'オレンジのアネモネ'),
		('Anemone3'            , 'ピンクのアネモネ'),
		('Anemone4'            , 'むらさきのアネモネ'),
		('Anemone5'            , 'あおいアネモネ'),
		('Hyacinth0'           , 'しろいヒヤシンス'),
		('Hyacinth1'           , 'きいろいヒヤシンス'),
		('Hyacinth2'           , 'あかいヒヤシンス'),
		('Hyacinth3'           , 'オレンジのヒヤシンス'),
		('Hyacinth4'           , 'ピンクのヒヤシンス'),
		('Hyacinth5'           , 'むらさきのヒヤシンス'),
		('Hyacinth6'           , 'あおいヒヤシンス'),
		('Mum0'                , 'しろいキク'),
		('Mum1'                , 'きいろいキク'),
		('Mum2'                , 'あかいキク'),
		('Mum3'                , 'ピンクのキク'),
		('Mum4'                , 'みどりのキク'),
		('Mum5'                , 'むらさきのキク'),
		('PltRose0'            , 'あかいバラのかぶ'),
		('PltRose1'            , 'しろいバラのかぶ'),
		('PltRose2'            , 'きいろいバラのかぶ'),
		('PltRose3'            , 'ピンクのバラのかぶ'),
		('PltRose4'            , 'オレンジのバラのかぶ'),
		('PltRose5'            , 'むらさきのバラのかぶ'),
		('PltRose6'            , 'くろいバラのかぶ'),
		('PltRose7'            , 'あおいバラのかぶ'),
		('PltGoldenRose'       , '金のバラのかぶ'),
		('PltCosmos0'          , 'しろいコスモスのかぶ'),
		('PltCosmos1'          , 'あかいコスモスのかぶ'),
		('PltCosmos2'          , 'きいろいコスモスのかぶ'),
		('PltCosmos3'          , 'ピンクのコスモスのかぶ'),
		('PltCosmos4'          , 'オレンジのコスモスのかぶ'),
		('PltCosmos5'          , 'くろいコスモスのかぶ'),
		('PltTurip0'           , 'あかいチューリップのかぶ'),
		('PltTurip1'           , 'しろいチューリップのかぶ'),
		('PltTurip2'           , 'きいろいチューリップのかぶ'),
		('PltTurip3'           , 'ピンクのチューリップのかぶ'),
		('PltTurip4'           , 'むらさきチューリップのかぶ'),
		('PltTurip5'           , 'くろいチューリップのかぶ'),
		('PltTurip6'           , 'オレンジのチューリップのかぶ'),
		('PltPansi0'           , 'しろいパンジーのかぶ'),
		('PltPansi1'           , 'きいろいパンジーのかぶ'),
		('PltPansi2'           , 'あかいパンジーのかぶ'),
		('PltPansi3'           , 'むらさきのパンジーのかぶ'),
		('PltPansi4'           , 'あかきいろパンジーのかぶ'),
		('PltPansi5'           , 'あおいパンジーのかぶ'),
		('PltYuri0'            , 'しろいユリのかぶ'),
		('PltYuri1'            , 'きいろいユリのかぶ'),
		('PltYuri2'            , 'あかいユリのかぶ'),
		('PltYuri3'            , 'オレンジのユリのかぶ'),
		('PltYuri4'            , 'ピンクのユリのかぶ'),
		('PltYuri5'            , 'くろいユリのかぶ'),
		('PltAnemone0'         , 'しろいアネモネのかぶ'),
		('PltAnemone1'         , 'あかいアネモネのかぶ'),
		('PltAnemone2'         , 'オレンジのアネモネのかぶ'),
		('PltAnemone3'         , 'ピンクのアネモネのかぶ'),
		('PltAnemone4'         , 'むらさきのアネモネのかぶ'),
		('PltAnemone5'         , 'あおいアネモネのかぶ'),
		('PltHyacinth0'        , 'しろいヒヤシンスのかぶ'),
		('PltHyacinth1'        , 'きいろいヒヤシンスのかぶ'),
		('PltHyacinth2'        , 'あかいヒヤシンスのかぶ'),
		('PltHyacinth3'        , 'オレンジのヒヤシンスのかぶ'),
		('PltHyacinth4'        , 'ピンクのヒヤシンスのかぶ'),
		('PltHyacinth5'        , 'むらさきのヒヤシンスのかぶ'),
		('PltHyacinth6'        , 'あおいヒヤシンスのかぶ'),
		('PltMum0'             , 'しろいキクのかぶ'),
		('PltMum1'             , 'きいろいキクのかぶ'),
		('PltMum2'             , 'あかいキクのかぶ'),
		('PltMum3'             , 'ピンクのキクのかぶ'),
		('PltMum4'             , 'みどりのキクのかぶ'),
		('PltMum5'             , 'むらさきのキクのかぶ'),
		('PltSuzuran'          , 'スズランのかぶ'),
		('Seedling'            , '木の苗'),
		('PltOak'              , '広葉樹'),
		('SeedlingConifer'     , '針葉樹の苗'),
		('PltConifer'          , '針葉樹'),
		('PltBamboo'           , '竹'),
		('PltPalm'             , 'ヤシの木'),
		('PltApple'            , 'リンゴの木'),
		('PltOrange'           , 'オレンジの木'),
		('PltPear'             , 'ナシの木'),
		('PltPeach'            , 'モモの木'),
		('PltCherry'           , 'さくらんぼの木'),
		('PltMoney'            , '金のなる木'),
		('Weed'                , 'ざっそう'),
		('EggGround'           , 'じめんのたまご'),
		('EggRock'             , 'いわのたまご'),
		('EggLeaf'             , 'はっぱのたまご'),
		('EggForest'           , 'もりのたまご'),
		('EggSky'              , 'そらとぶたまご'),
		('EggFish'             , 'サカナのたまご'),
		('MessageBottleEgg'    , 'たまごのメッセージボトル'),
	))
	_5032ef59 = Enum(0x5032ef59, (
		('None'          , 'なし'),
		('NotEquippedN'  , 'NPC装備不可'),
		('Pants'         , 'ズボン'),
		('Skirt'         , 'スカート'),
		('Tops'          , 'トップス'),
		('Onepiece'      , 'ワンピース'),
		('Kimono'        , 'きもの'),
		('Cap'           , 'ぼうし'),
		('HeadHairAcce'  , 'ヘアアクセサリ'),
		('EyeAcce'       , 'メガネ'),
		('EyeAcceSP'     , '特殊メガネ'),
		('EyeAcceBlind'  , 'ブラインド'),
		('Mask'          , 'おめん'),
		('DecorateFtr'   , '装飾系'),
		('HornedBeetle'  , 'カブトムシ'),
		('Stag'          , 'クワガタ'),
		('Cicada'        , 'セミ'),
		('Grasshopper'   , 'バッタ'),
		('Butterfly'     , 'チョウ'),
		('Dragonfly'     , 'トンボ'),
		('Sealouse'      , 'フナムシ'),
		('Beetle'        , '甲虫'),
		('FlowerInsect'  , '花の虫'),
		('Stump'         , '切り株'),
		('RiverFish'     , '川サカナ'),
		('SeaFish'       , '海サカナ'),
		('RiverMouthFish', '汽水池サカナ'),
		('OutofQuest'    , 'クエスト対象外'),
	))
	_164a5f24 = Enum(0x164a5f24, (
		('None'    , 'なし'),
		('Simple'  , 'シンプル'),
		('Gorgeous', 'ゴージャス'),
		('Cool'    , 'クール'),
		('Cute'    , 'キュート'),
		('Active'  , 'アクティブ'),
		('Elegant' , 'エレガント'),
	))
	_9ba040c2 = U32(0x9ba040c2)
	_aa6a39c6 = Enum(0xaa6a39c6, (
		('None'            , 'なし'),
		('Smartphone'      , '撮影'),
		('Switch'          , '駆動'),
		('RhythmSound'     , 'ノる'),
		('SingSong'        , '歌う'),
		('PlayMusicBoth'   , '演奏する（両手）'),
		('PlayMusic'       , '演奏する（片手）'),
		('SwitchWind'      , '駆動（扇風機）'),
		('SwitchWarm'      , '駆動（温まる）'),
		('SwitchSomen'     , '駆動（そうめん）'),
		('SwitchTakenAback', '駆動（ビックリ）'),
		('Watch'           , 'まじまじ見る'),
		('WatchWall'       , 'まじまじ見る（壁掛）'),
		('MirrorPosing'    , '鏡の前でポーズ'),
		('WaterSpray'      , '霧吹き'),
		('SmellFood'       , '匂いをかぐ'),
		('SwitchSmellFood' , '駆動（匂いをかぐ）'),
	))
	_d9855b4e = Enum(0xd9855b4e, (
		('All'  , '全方位'),
		('Front', '正面'),
		('Back' , '背面'),
	))
	_a812e496 = Enum(0xa812e496, (
		('None'      , '未設定'),
		('Bed'       , 'ベッド'),
		('TV'        , 'テレビ'),
		('Audio'     , 'オーディオ機器'),
		('Clock'     , '時計'),
		('Plant'     , '植物'),
		('Bathtub'   , '浴槽'),
		('Desk'      , '机'),
		('Chair'     , '椅子'),
		('Instrument', '楽器'),
		('Kitchen'   , 'キッチン'),
		('Exercise'  , '運動'),
		('Outdoor'   , 'アウトドア'),
	))
	_effadab6 = Enum(0xeffadab6, (
		('None'         , '未設定'),
		('Mushroom'     , 'きのこ'),
		('Ice'          , 'こおり'),
		('Japanese'     , '和風'),
		('Block'        , 'つみき'),
		('Antique'      , 'アンティーク'),
		('School'       , '学校'),
		('Resort'       , 'リゾート'),
		('Office'       , 'オフィス'),
		('Log'          , 'まるた'),
		('Cute'         , 'キュート'),
		('Fruit'        , 'フルーツ'),
		('AmericanRetro', 'アメリカンレトロ'),
		('Toy'          , 'TOY'),
		('Shell'        , 'かいがら'),
		('IronWood'     , 'アイアンウッド'),
		('Easter'       , 'イースター'),
	))
	_bf80f575 = Enum(0xbf80f575, (
		('None' , 'なし'),
		('Valid', 'あり'),
	))
	_ead62c46 = Enum(0xead62c46, (
		('None'             , 'なし'),
		('Kitchen'          , 'キッチン'),
		('Display'          , '上物_飾り'),
		('Food'             , '上物_飲食物'),
		('Insect'           , 'ムシ'),
		('Fish'             , 'サカナ'),
		('WorkStuff'        , '上物_作業用'),
		('Base_Desk'        , '台_机'),
		('Base_Table'       , '台_テーブル'),
		('Base_Display'     , '台_飾り棚'),
		('Base_Sp'          , '台_特殊'),
		('Base_Disable'     , '台_不可'),
		('Utility'          , 'ユーティリティ'),
		('Item_ForBase'     , '上物_原則床置'),
		('Bed'              , 'ベッド'),
		('Chair'            , 'イス・ソファ'),
		('Cushion'          , 'クッション'),
		('Closet'           , '収納'),
		('MusicalInstrument', '楽器系'),
		('DIYworkbench'     , 'DIY作業台'),
		('Fixed'            , '入替不可'),
	))
	_ba4fd546 = Enum(0xba4fd546, (
		('No' , 'No'),
		('Yes', 'Yes'),
	))
	_7724bf93 = Enum(0x7724bf93, (
		('AccessoryOneEye'               , 'アクセサリ：片目'),
		('AccessoryMouth'                , 'アクセサリ：口'),
		('AccessoryMouthInvisibleNose'   , 'アクセサリ：口(鼻なし)'),
		('AccessoryMouthEarJaw'          , 'アクセサリ：口耳アゴ'),
		('AccessoryEye'                  , 'アクセサリ：目'),
		('AcceEyeMouth'                  , 'アクセサリ：目/口'),
		('AccessoryEyeMouthInvisibleNose', 'アクセサリ：目/口(鼻なし)'),
		('HeadFace'                      , '頭：お面'),
		('Headgear_HasBang'              , '頭：被り物(前髪あり)'),
		('Headgear_HasEar'               , '頭：被り物(耳あり)'),
		('Headgear_NoEar'                , '頭：被り物(耳なし)'),
		('Headgear_NoEarNoJaw'           , '頭：被り物(耳なし/アゴなし)'),
		('HeadHairOrnament_Front'        , '頭：髪飾り(おでこ)'),
		('HeadHairOrnament_Back'         , '頭：髪飾り(後頭部)'),
		('HeadHairOrnament_Top'          , '頭：髪飾り(頭上)'),
		('HeadHairOrnament_Peak'         , '頭：髪飾り(頂上)'),
		('HeadHairOrnament_Left'         , '頭：髪飾り(左頭)'),
		('HeadHairOrnament_Right'        , '頭：髪飾り(右頭)'),
		('HeadFullFace'                  , '頭：フルフェイス'),
		('HeadCap'                       , '頭：帽子'),
		('BagShoulder'                   , 'カバン：ショルダー'),
		('BagBackpack'                   , 'カバン：バックパック'),
		('ShoesHard'                     , '靴：かたい'),
		('ShoesSlippers'                 , '靴：スリッパ'),
		('ShoesGeta'                     , '靴：げた'),
		('ShoesPumps'                    , '靴：パンプス'),
		('ShoesSoft'                     , '靴：やわらかい'),
		('Socks'                         , '靴下'),
		('Tops'                          , 'トップス'),
		('Onepiece'                      , 'ワンピース'),
		('None'                          , 'なし'),
		('Bottoms'                       , 'ボトムス'),
		('Ocarina'                       , 'オカリナ'),
		('Tambourine'                    , 'タンバリン'),
		('Panpipe'                       , 'パンフルート'),
		('CliffMaker'                    , '崖造成キット'),
		('RiverMaker'                    , '川造成キット'),
		('FenceMaker'                    , '柵造成キット'),
		('GroundMaker'                   , '道造成キット'),
		('Net'                           , 'アミ：下位'),
		('NetMiddleLevel'                , 'アミ：中位'),
		('NetUpperLevel'                 , 'アミ：上位'),
		('Axe'                           , 'オノ：下位'),
		('AxeMiddleLevel'                , 'オノ：中位'),
		('AxeUpperLevel'                 , 'オノ：上位'),
		('AxeDull'                       , '切れないオノ：下位'),
		('AxeDullMiddleLevel'            , '切れないオノ：中位'),
		('Watering'                      , 'ジョウロ：下位'),
		('WateringMiddleLevel'           , 'ジョウロ：中位'),
		('WateringUpperLevel'            , 'ジョウロ：上位'),
		('ScoopHandMade'                 , 'スコップ：てづくり'),
		('Scoop'                         , 'スコップ：下位'),
		('ScoopMiddleLevel'              , 'スコップ：中位'),
		('ScoopUpperLevel'               , 'スコップ：上位'),
		('FishingRod'                    , 'つりざお：下位'),
		('FishingRodMiddleLevel'         , 'つりざお：中位'),
		('FishingRodUpperLevel'          , 'つりざお：上位'),
		('FishingRodAndFloat'            , 'つりざお：一体型'),
		('Slingshot'                     , 'パチンコ：下位'),
		('SlingshotMiddleLevel'          , 'パチンコ：中位'),
		('SlingshotUpperLevel'           , 'パチンコ：上位'),
		('JumpStick'                     , 'ジャンプ棒'),
		('Ladder'                        , 'はしご'),
		('ChangeStick'                   , '変身ステッキ'),
		('PaperFan'                      , 'うちわ'),
		('Umbrella'                      , 'カサ'),
		('Umbrella_NoUseToolCommonAnim'  , 'カサ（自前アニメ）'),
		('Umbrella_NoSound'              , 'カサ_開閉音無し'),
		('Umbrella_Leaf'                 , 'カサ_葉っぱ'),
		('Umbrella_Flower'               , 'カサ_花'),
		('Windmill'                      , 'かざぐるま'),
		('Cracker'                       , 'クラッカー'),
		('SoapBubble'                    , 'シャボン玉'),
		('StickLight'                    , 'スティックライト'),
		('Spanner'                       , 'スパナとかなづち'),
		('SmartPhone'                    , 'スマホ'),
		('Brush'                         , 'はけ'),
		('Fireworks'                     , '手持ち花火'),
		('PinataStick'                   , 'ピニャータ割り棒'),
		('Balloon'                       , 'ふうせん'),
		('Blowouts'                      , 'ふきもどし'),
		('Ice'                           , 'アイス'),
		('Branch'                        , 'えだ'),
		('Hammer'                        , 'かなづち'),
		('Canister'                      , '缶'),
		('Candy'                         , 'キャンディ'),
		('Sprayer'                       , 'きりふき'),
		('FruitBasket'                   , '果物カゴ'),
		('Coffee'                        , 'コーヒー'),
		('Cop'                           , 'コップ'),
		('Sandwich'                      , 'サンドウィッチ'),
		('Sketchbook'                    , 'スケッチブック'),
		('Smoothie'                      , 'スムージー'),
		('Dumbbell'                      , 'ダンベル'),
		('LightDumbbell'                 , 'ダンベル(軽い)'),
		('RcmTourFlag'                   , 'つぶまめツアー旗'),
		('BagHand'                       , '手提げカバン'),
		('CuteBagHand'                   , '手提げかばん(キュート)'),
		('CoolBagHand'                   , '手提げかばん(クール)'),
		('HighBagHand'                   , '手提げかばん(生活度高)'),
		('LowBagHand'                    , '手提げかばん(生活度低)'),
		('Doughnut'                      , 'ドーナッツ'),
		('TkkGuitar'                     , 'とたけけギター'),
		('Duster'                        , 'はたき'),
		('Broom'                         , 'ほうき'),
		('Book'                          , '本'),
		('SmallBook'                     , '本(小)'),
		('Firewood'                      , '薪'),
		('HandLens'                      , '虫眼鏡'),
	))
	_9feb9da6 = Enum(0x9feb9da6, (
		('None'                               , 'なし'),
		('NpcSpTopsSzaTshirtsL'               , 'NpcSpTopsSzaTshirtsL'),
		('NpcSpBottomsRcmApronNS'             , 'NpcSpBottomsRcmApronNS'),
		('PlayerTopsOnepieceSalopetteN'       , 'PlayerTopsOnepieceSalopetteN'),
		('PlayerTopsOnepieceSalopetteH'       , 'PlayerTopsOnepieceSalopetteH'),
		('PlayerTopsOnepieceSalopetteL'       , 'PlayerTopsOnepieceSalopetteL'),
		('PlayerTopsTopPuffH'                 , 'PlayerTopsTopPuffH'),
		('PlayerTopsOnepieceAlinemydesign3dsL', 'PlayerTopsOnepieceAlinemydesign3dsL'),
		('NpcSpTopsRcoTshirtsL'               , 'NpcSpTopsRcoTshirtsL'),
		('NpcSpTopsRcmOuterL'                 , 'NpcSpTopsRcmOuterL'),
		('NpcSpTopsRcmYshirtsH'               , 'NpcSpTopsRcmYshirtsH'),
		('PlayerTopsTopYshirtsmydesignN'      , 'PlayerTopsTopYshirtsmydesignN'),
		('NpcSpTopsRcmYshirtsapronH'          , 'NpcSpTopsRcmYshirtsapronH'),
		('NpcSpTopsSzaYshirtsH'               , 'NpcSpTopsSzaYshirtsH'),
		('NpcSpTopsSzaOuterL'                 , 'NpcSpTopsSzaOuterL'),
		('PlayerTopsOnepieceKimonomydesignL'  , 'PlayerTopsOnepieceKimonomydesignL'),
		('PlayerTopsOnepieceRibmydesignN'     , 'PlayerTopsOnepieceRibmydesignN'),
		('PlayerTopsOnepieceBoxmydesignN'     , 'PlayerTopsOnepieceBoxmydesignN'),
		('PlayerTopsOnepieceDressmydesignL'   , 'PlayerTopsOnepieceDressmydesignL'),
		('PlayerTopsOnepieceBalloonmydesignH' , 'PlayerTopsOnepieceBalloonmydesignH'),
		('PlayerTopsTopCoatmydesignL'         , 'PlayerTopsTopCoatmydesignL'),
		('PlayerTopsTopTshirtsmydesignH'      , 'PlayerTopsTopTshirtsmydesignH'),
		('PlayerTopsTopTshirtsmydesignN'      , 'PlayerTopsTopTshirtsmydesignN'),
		('PlayerTopsTopOutermydesignL'        , 'PlayerTopsTopOutermydesignL'),
		('PlayerTopsOnepieceRobeL'            , 'PlayerTopsOnepieceRobeL'),
		('PlayerTopsTopTshirtsH'              , 'PlayerTopsTopTshirtsH'),
		('PlayerTopsTopOuterL'                , 'PlayerTopsTopOuterL'),
		('PlayerTopsTopCoatL'                 , 'PlayerTopsTopCoatL'),
		('PlayerTopsOnepieceBalloonN'         , 'PlayerTopsOnepieceBalloonN'),
		('PlayerBottomsPantsNormal'           , 'PlayerBottomsPantsNormal'),
		('PlayerTopsTopTshirtsL'              , 'PlayerTopsTopTshirtsL'),
		('PlayerTopsTopTshirtsN'              , 'PlayerTopsTopTshirtsN'),
		('PlayerTopsOnepieceBalloonH'         , 'PlayerTopsOnepieceBalloonH'),
		('PlayerTopsOnepieceBalloonL'         , 'PlayerTopsOnepieceBalloonL'),
		('PlayerTopsOnepieceAlineN'           , 'PlayerTopsOnepieceAlineN'),
		('PlayerTopsOnepieceAlineH'           , 'PlayerTopsOnepieceAlineH'),
		('PlayerTopsOnepieceAlineL'           , 'PlayerTopsOnepieceAlineL'),
		('PlayerTopsOnepieceBoxN'             , 'PlayerTopsOnepieceBoxN'),
		('PlayerTopsOnepieceBoxH'             , 'PlayerTopsOnepieceBoxH'),
		('PlayerTopsOnepieceBoxL'             , 'PlayerTopsOnepieceBoxL'),
		('PlayerTopsTopOuterN'                , 'PlayerTopsTopOuterN'),
		('PlayerTopsTopYshirtsL'              , 'PlayerTopsTopYshirtsL'),
		('PlayerTopsTopYshirtsH'              , 'PlayerTopsTopYshirtsH'),
		('PlayerTopsTopYshirtsN'              , 'PlayerTopsTopYshirtsN'),
		('PlayerTopsTopCoatH'                 , 'PlayerTopsTopCoatH'),
		('PlayerTopsTopCoatN'                 , 'PlayerTopsTopCoatN'),
		('PlayerTopsOnepieceRibN'             , 'PlayerTopsOnepieceRibN'),
		('PlayerTopsOnepieceRibH'             , 'PlayerTopsOnepieceRibH'),
		('PlayerTopsOnepieceRibL'             , 'PlayerTopsOnepieceRibL'),
		('PlayerTopsOnepieceDressN'           , 'PlayerTopsOnepieceDressN'),
		('PlayerTopsOnepieceDressH'           , 'PlayerTopsOnepieceDressH'),
		('PlayerTopsOnepieceDressL'           , 'PlayerTopsOnepieceDressL'),
		('PlayerBottomsSkirtAline'            , 'PlayerBottomsSkirtAline'),
		('PlayerBottomsPantsWide'             , 'PlayerBottomsPantsWide'),
		('PlayerTopsOnepieceOverallN'         , 'PlayerTopsOnepieceOverallN'),
		('PlayerTopsOnepieceOverallH'         , 'PlayerTopsOnepieceOverallH'),
		('PlayerTopsOnepieceOverallL'         , 'PlayerTopsOnepieceOverallL'),
		('PlayerTopsOnepieceAlongN'           , 'PlayerTopsOnepieceAlongN'),
		('PlayerTopsOnepieceAlongH'           , 'PlayerTopsOnepieceAlongH'),
		('PlayerTopsOnepieceAlongL'           , 'PlayerTopsOnepieceAlongL'),
		('PlayerTopsOnepieceBlongN'           , 'PlayerTopsOnepieceBlongN'),
		('PlayerTopsOnepieceBlongH'           , 'PlayerTopsOnepieceBlongH'),
		('PlayerTopsOnepieceBlongL'           , 'PlayerTopsOnepieceBlongL'),
		('PlayerTopsOnepieceKimonoL'          , 'PlayerTopsOnepieceKimonoL'),
		('PlayerBottomsSkirtBox'              , 'PlayerBottomsSkirtBox'),
		('PlayerBottomsSkirtLong'             , 'PlayerBottomsSkirtLong'),
		('PlayerBottomsPantsHalf'             , 'PlayerBottomsPantsHalf'),
		('PlayerBottomsPantsHot'              , 'PlayerBottomsPantsHot'),
		('NpcSpTopsRcoYshirtsH'               , 'NpcSpTopsRcoYshirtsH'),
		('NpcSpBottomsRcoPantsHalf'           , 'NpcSpBottomsRcoPantsHalf'),
		('NpcSpTopsSzaTshirtsH'               , 'NpcSpTopsSzaTshirtsH'),
		('NpcSpBottomsSzaSkirtBox'            , 'NpcSpBottomsSzaSkirtBox'),
		('NpcSpBottomsRcoPantsNormal'         , 'NpcSpBottomsRcoPantsNormal'),
		('NpcSpTopsRcoOuterL'                 , 'NpcSpTopsRcoOuterL'),
		('PlayerTopsOnepieceAlinemydesignH'   , 'PlayerTopsOnepieceAlinemydesignH'),
		('PlayerTopsTopYshirtsmydesignL'      , 'PlayerTopsTopYshirtsmydesignL'),
		('PlayerTopsOnepieceAlinemydesign3dsN', 'PlayerTopsOnepieceAlinemydesign3dsN'),
		('PlayerTopsOnepieceAlinemydesign3dsH', 'PlayerTopsOnepieceAlinemydesign3dsH'),
		('PlayerTopsTopTshirtsmydesign3dsH'   , 'PlayerTopsTopTshirtsmydesign3dsH'),
		('PlayerTopsTopTshirtsmydesign3dsL'   , 'PlayerTopsTopTshirtsmydesign3dsL'),
		('PlayerTopsTopTshirtsmydesign3dsN'   , 'PlayerTopsTopTshirtsmydesign3dsN'),
	))
	_510f21dc = Enum(0x510f21dc, (
		('None'            , '未設定'),
		('DirectionOutdoor', '屋外向き'),
		('DirectionIndoor' , '屋内向き'),
	))
	_5504464e = Enum(0x5504464e, (
		('None'                , 'なし'),
		('Series_Cute'         , 'キュート'),
		('Series_TOY'          , 'TOY'),
		('Series_Rattan'       , 'ラタン'),
		('Series_Oriental'     , 'オリエンタル'),
		('Series_AmericanRetro', 'アメリカンレトロ'),
		('Series_Antique'      , 'アンティーク'),
		('Series_Mom'          , '母'),
		('Set_Hero'            , 'ヒーローロボ'),
		('Set_Chinese'         , '中華テーブル'),
		('Set_Outdoortable'    , 'アウトドアテーブル'),
		('Set_School'          , '学校'),
		('Set_Collage'         , '講義室'),
		('Set_Study'           , '学習机'),
		('Set_Japaneseroom'    , '和室'),
		('Set_Boxsofa'         , 'ボックスソファ'),
		('Set_Shower'          , 'シャワーセット'),
		('Set_Flamingo'        , 'フラミンゴ'),
		('Tool_Outdoor'        , '道具アウトドア'),
		('Tool_Colorful'       , '道具カラフル'),
	))
	_ea9fc92a = Enum(0xea9fc92a, (
		('AllRegion'   , '全リージョン'),
		('ExceptEurope', '欧州以外'),
	))
	_e06fb090 = Enum(0xe06fb090, (
		('1_0x1_0'     , '1x1'),
		('2_0x1_0'     , '2x1'),
		('2_0x2_0'     , '2x2'),
		('3_0x1_0'     , '3x1'),
		('3_0x2_0'     , '3x2'),
		('3_0x3_0'     , '3x3'),
		('1_0x0_5'     , '1x0.5'),
		('2_0x0_5'     , '2x0.5'),
		('1_5x1_5'     , '1.5x1.5'),
		('1_0x0_5_Wall', '1x0.5(壁)'),
		('0_5x1_0_Wall', '0.5x1(壁)'),
		('1_0x1_0_Wall', '1x1(壁)'),
		('1_0x1_5_Wall', '1x1.5 (壁)'),
		('1_0x2_0_Wall', '1x2\u3000 (壁)'),
		('2_0x1_0_Wall', '2x1(壁)'),
		('2_0x1_5_Wall', '2x1.5 (壁)'),
		('2_0x2_0_Wall', '2x2(壁)'),
		('1_0x1_0_Rug' , '1x1(ラグ)'),
		('2_0x1_0_Rug' , '2x1(ラグ)'),
		('2_0x2_0_Rug' , '2x2(ラグ)'),
		('3_0x2_0_Rug' , '3x2(ラグ）'),
		('3_0x3_0_Rug' , '3x3(ラグ）'),
		('4_0x3_0_Rug' , '4x3(ラグ)'),
		('4_0x4_0_Rug' , '4x4(ラグ)'),
		('5_0x4_0_Rug' , '5x4(ラグ)'),
		('5_0x5_0_Rug' , '5x5(ラグ)'),
	))
	_28297660 = Enum(0x28297660, (
		('None'       , '未設定'),
		('Floor'      , 'かぐ'),
		('Upper'      , 'こもの'),
		('Wall'       , 'かべかけ'),
		('Ceiling_Rug', 'ラグ'),
		('Plant'      , 'しょくぶつ'),
		('Creature'   , 'いきもの'),
		('Food'       , 'たべもの'),
		('Material'   , 'そざい'),
		('Others'     , 'ほか'),
		('Tool'       , 'どうぐ'),
		('RoomFloor'  , 'ゆかいた'),
		('RoomWall'   , 'かべがみ'),
		('Unnecessary', '設定不要'),
		('Clothes'    , 'ファッション'),
	))
	_8221388c = Enum(0x8221388c, (
		('Chair'             , 'イス・スツール'),
		('Sofa'              , 'ソファ・ベンチ'),
		('Desk'              , '机'),
		('Table'             , 'テーブル'),
		('Bed'               , 'ベッド'),
		('Chest'             , 'タンス・クローゼット'),
		('Shelf'             , '棚'),
		('Dresser'           , 'ドレッサー'),
		('Screen'            , 'スクリーン'),
		('Arch'              , 'アーチ'),
		('WorkBench'         , '作業台'),
		('SewingTable'       , '裁縫台'),
		('Kitchen'           , 'キッチン'),
		('KitchenThings'     , '雑貨：キッチン'),
		('Dining'            , '雑貨：食卓'),
		('Lamp'              , '照明'),
		('TV'                , 'テレビ'),
		('GameConsole'       , 'ゲーム機'),
		('Audio'             , 'オーディオ機器'),
		('MusicalInstrument' , '楽器'),
		('Clock'             , '時計'),
		('HouseDoorDeco'     , 'ドア飾り'),
		('HomeAppliances'    , '生活家電'),
		('Fan'               , '扇風機系'),
		('AirConditioning'   , 'エアコン'),
		('Heating'           , '暖房'),
		('Fireplace'         , '暖炉'),
		('Toilet'            , '便器'),
		('Bathtub'           , '浴槽'),
		('BathroomThings'    , '雑貨：バス・トイレ'),
		('Beauty'            , '雑貨：美容系'),
		('Plants'            , '植物'),
		('Study'             , '雑貨：書斎'),
		('Supplies'          , '雑貨：家庭'),
		('School'            , '雑貨：学校'),
		('Office'            , '雑貨：オフィス'),
		('Hospital'          , '雑貨：病院'),
		('Museum'            , '雑貨：博物館系'),
		('Shop'              , '雑貨：お店'),
		('SuppliesFacility'  , '雑貨：施設'),
		('Seaside'           , '雑貨：海辺'),
		('Space'             , '雑貨：宇宙'),
		('Star'              , '雑貨：星'),
		('Vehicle'           , '雑貨：交通'),
		('Animal'            , '雑貨：動物'),
		('Fish'              , '雑貨：魚'),
		('FishSP'            , '雑貨：魚SP'),
		('Insect'            , '雑貨：昆虫'),
		('InsectSP'          , '雑貨：昆虫SP'),
		('Toy'               , '雑貨：玩具'),
		('Sports'            , '雑貨：スポーツ'),
		('Playground'        , '雑貨：公園'),
		('SuppliesOutdoors'  , '雑貨：アウトドア'),
		('Ranch'             , '雑貨：畑・牧場'),
		('Garden'            , '雑貨：庭'),
		('JapaneseStyle'     , '雑貨：和風'),
		('SuppliesFolkCraft' , '雑貨：民芸品'),
		('Easter'            , '雑貨：イースター'),
		('SuppliesSeason'    , '雑貨：季節イベント'),
		('Compass'           , 'ポケ森コラボ'),
		('Picture'           , '絵画'),
		('Sculpture'         , '彫刻'),
		('Bromide'           , 'ブロマイド'),
		('Posters'           , 'ポスター'),
		('None'              , '未設定'),
		('Unnecessary'       , '設定不要'),
		('Wood'              , '◆◆木'),
		('Herringbone'       , '◆ヘリンボーン'),
		('Country'           , '◆パーケットフローリング'),
		('DecoWood'          , '◆デコレーションフローリング'),
		('ColorfulWood'      , '◆カラフルフローリング'),
		('PaintWood'         , '◆ペイントフローリング'),
		('ParquetIron'       , '◆アイアンパーケット'),
		('Parquet'           , '◆スクエアな寄せ木'),
		('SimpleParquet'     , '◆シンプルな寄せ木'),
		('Tatami'            , '◆畳'),
		('TatamiPanel'       , '◆淵無し畳'),
		('Japanese'          , '◆和風'),
		('Stone'             , '◆◆石'),
		('Iron'              , '◆鉄'),
		('Brick'             , '◆レンガ'),
		('ArchBrick'         , '◆アーチレンガ'),
		('Tile'              , '◆◆タイル'),
		('Argyle'            , '◆アーガイル'),
		('Chocolate'         , '◆アソート'),
		('Honeycomb'         , '◆ハニカムタイル'),
		('FloorKitchen'      , '◆レトロなクロス'),
		('Morocco'           , '◆モロッカンタイル'),
		('FloorTile'         , '◆モザイクタイル'),
		('TileChecker'       , '◆ピータイル'),
		('Cloth'             , '◆◆布'),
		('Dot'               , '◆ドットカーペット'),
		('Panel'             , '◆パネルカーペット'),
		('PuzzleMat'         , '◆パズル'),
		('Rubber'            , '◆ラバー'),
		('SimpleCarpet'      , '◆シンプルカーペット'),
		('Camouflage'        , '◆迷彩'),
		('AnimalFloor'       , '◆動物柄'),
		('Neta'              , '◆◆ネタ：ハチミツ'),
		('Luxury'            , '◆ネタ：高級'),
		('Decadence'         , '◆ネタ：退廃'),
		('FloorMachine'      , '◆ネタ：機械'),
		('Sidewalk'          , '◆歩道'),
		('FloorSports'       , '◆ネタ：スポーツ'),
		('Grassland'         , '◆草'),
		('NatureGreen'       , '◆自然：緑'),
		('NatureFallenLeaves', '◆自然：落ち葉系'),
		('Nature'            , '◆◆自然'),
		('NatureBrown'       , '◆自然：茶'),
		('NatureWhite'       , '◆自然：白'),
		('SpNature'          , '◆◆特殊（自然）'),
		('SpInorganic'       , '◆◆特殊（無機質）'),
		('Sanrio'            , '◆◆サンリオ'),
		('WallWood'          , '■■木'),
		('WallHerringbone'   , '■ヘリンボーン'),
		('WallHall'          , '■ホール'),
		('WallMixPlankWood'  , '■寄せ木'),
		('WallPegbpard'      , '■パンチングボード'),
		('WallPaintWood'     , '■ペイントウッド'),
		('WallPanelMold'     , '■パネルモールド'),
		('WallStone'         , '■■石'),
		('WallBrick'         , '■レンガ'),
		('WallStucco'        , '■ペイントウォール'),
		('WallIron'          , '■■鉄'),
		('WallTin'           , '■トタン'),
		('WallTile'          , '■■タイル'),
		('WallTilee'         , '■タイル'),
		('WallTwoToneTile'   , '■ツートンタイル'),
		('WallMetro'         , '■メトロタイル'),
		('WallWoodTile'      , '■パターンタイル'),
		('WallMorocco'       , '■モロッカンタイル'),
		('WallHoneycomb'     , '■ハニカムタイル'),
		('WallChocolate'     , '■チョコ'),
		('WallCrown'         , '■クラウン'),
		('WallCloth'         , '■■布'),
		('WallSimple'        , '■シンプルクロス'),
		('WallDot'           , '■ドット'),
		('WallHeart'         , '■ハート'),
		('WallCute'          , '■キュート'),
		('WallStripe'        , '■ストライプ'),
		('WallFruit'         , '■フルーツ'),
		('WallFlower'        , '■花柄'),
		('WallManor'         , '■小花柄'),
		('WallCountry'       , '■草花模様'),
		('WallRose'          , '■バラ'),
		('WallFlowerPop'     , '■テキスタイルフラワー'),
		('WallArtDeco'       , '■アールデコ'),
		('WallCamouflage'    , '■迷彩'),
		('WallPuzzle'        , '■パズル'),
		('WallDollhouse'     , '■キルト'),
		('WallToy'           , '■おもちゃ'),
		('WallDiner'         , '■ダイナー'),
		('WallJapanese'      , '■和風'),
		('WallTeaRoom'       , '■茶室'),
		('Asia'              , '■グローバル系'),
		('WallLibrary'       , '■本棚'),
		('WallNeta'          , '■■ネタ'),
		('WallNature'        , '■■自然'),
		('WallSpNatureCool'  , '■■特殊（自然寒色）'),
		('WallSpNatureWarm'  , '■■特殊（自然暖色）'),
		('WallSpIndoor'      , '■■特殊（室内）'),
		('WallSpInorganic'   , '■■特殊（無機質）'),
		('WallSanrio'        , '■■サンリオ'),
		('RugSimple'         , '●●シンプル'),
		('RugPattern'        , '●●柄物：正方形'),
		('RugPatternSlender' , '●●柄物：細長'),
		('RugKitchen'        , '●●キッチンマット'),
		('RugSlender'        , '●●細長マット'),
		('RugWood'           , '●●木'),
		('RugRoundShaggymat' , '●まるいマット'),
		('RugRoundShaggy'    , '●まるいラグ'),
		('RugFruits'         , '●●果物'),
		('RugRose'           , '●●バラ'),
		('RugHeart'          , '●●ハート'),
		('RugStar'           , '●●星'),
		('RugMessageMat'     , '●●メッセージマット'),
		('RugIcon'           , '●●アイコン'),
		('RugPark'           , '●●どうぶつの森'),
		('RugSanrio'         , '●●サンリオ'),
	))
	_010d74a6 = Enum(0x010d74a6, (
		('None'                , '（なし）'),
		('MileCard'            , 'たぬきマイルカード'),
		('Leaf'                , '葉っぱ'),
		('LeafYellow'          , '葉っぱ：黄'),
		('RoomWall'            , '壁紙'),
		('RoomFloor'           , '床板'),
		('Rug'                 , 'ラグ'),
		('Tops'                , '装：トップス'),
		('Bottoms'             , '装：ボトムス'),
		('Socks'               , '装：くつした'),
		('Shoes'               , '装：くつ'),
		('Cap'                 , '装：ぼうし'),
		('Helmet'              , '装：かぶりもの'),
		('Accessory'           , '装：アクセサリ'),
		('Bag'                 , '装：バッグ'),
		('Umbrella'            , '装：カサ'),
		('FishingRod'          , '道具：つりざお'),
		('Stick'               , '変身ステッキ'),
		('Fence'               , '柵'),
		('TentSet'             , 'テントセット'),
		('HousingKit'          , 'ハウジングキット'),
		('FossilUnknown'       , '化石：未鑑定'),
		('FossilKnown'         , '化石：鑑定済み'),
		('Pitfall'             , 'おとしあなのタネ'),
		('Music'               , 'ミュージック'),
		('Medicine'            , 'おくすり'),
		('RemakeKit'           , 'リメイクキット'),
		('SmartphoneCase'      , 'スマホケース'),
		('Timer'               , 'タイマー'),
		('Honeycomb'           , 'ハチの巣'),
		('Weed'                , '雑草'),
		('Turnip'              , 'カブ'),
		('TurnipExpired'       , 'カブ腐れ'),
		('MessageBottle'       , 'メッセージボトル'),
		('Recipe'              , 'レシピ'),
		('FishBait'            , 'サカナのまきエサ'),
		('AirTicket'           , 'マイル航空券'),
		('TailorTicket'        , 'したてやひきかえけん'),
		('RollanTicket'        , 'ローランひきかえけん'),
		('BellExchangeTicket'  , 'ベルひきかえかん'),
		('PresentBoxRed'       , 'プレゼントBOX赤'),
		('PresentBoxGreen'     , 'プレゼントBOX青'),
		('Insect'              , '生物：ムシかご'),
		('Fish'                , '生物：サカナ'),
		('TrushTire'           , 'ゴミ：タイヤ'),
		('TrushCan'            , 'ゴミ：あきカン'),
		('TrushBoot'           , 'ゴミ：ながぐつ'),
		('Coin'                , 'コイン'),
		('MoneyBag'            , 'ベル袋'),
		('Parts'               , 'ジョニーのパーツ'),
		('PartsDust'           , 'さびたパーツ'),
		('LostQuestPouch'      , '落し物：袋'),
		('LostQuestBook'       , '落し物：本（読み物）'),
		('LostQuestNote'       , '落し物：本（書き物）'),
		('CupCake'             , 'バースデーカップケーキ'),
		('PinataStick'         , 'ピニャータぼう'),
		('Apple'               , 'リンゴ'),
		('Orange'              , 'オレンジ'),
		('Pear'                , 'ナシ'),
		('Peach'               , 'モモ'),
		('Cherry'              , 'サクランボ'),
		('Coconut'             , 'ヤシの実'),
		('Bambooshoot'         , 'タケノコ'),
		('SeedlingOak'         , '広葉樹の苗'),
		('PltOak'              , '広葉樹'),
		('SeedlingCedar'       , '針葉樹の苗'),
		('PltCedar'            , '針葉樹'),
		('PltPalm'             , 'ヤシの木'),
		('PltBamboo'           , '竹'),
		('SeedPaperbag'        , '花の種袋'),
		('Seed'                , '花の種'),
		('DIYBranch'           , 'D：枝'),
		('DIYWoodNormal'       , 'D：木材'),
		('DIYWoodSoft'         , 'D：木材（柔らかい）'),
		('DIYWoodHard'         , 'D：木材（硬い）'),
		('DIYBamboo'           , 'D：竹材'),
		('DIYBambooSpring'     , 'はるのわかたけ'),
		('ShellSummer'         , 'なつのかいがら'),
		('DIYAcorn'            , 'どんぐり'),
		('DIYPinecone'         , 'まつぼっくり'),
		('Sakurapetal'         , 'さくらのはなびら'),
		('AutumnLeaf'          , 'もみじのはっぱ'),
		('SnowCrystalLarge'    , 'ゆきのだいけっしょう'),
		('SnowCrystal'         , 'ゆきのけっしょう'),
		('DIYOrnamentRed'      , 'オーナメントあか'),
		('DIYOrnamentBlue'     , 'オーナメントあお'),
		('DIYOrnamentGold'     , 'オーナメントきん'),
		('MushSplendid'        , 'りっぱなキノコ'),
		('MushRound'           , 'まるいキノコ'),
		('MushSlender'         , 'ほそいキノコ'),
		('MushFlat'            , 'ひらたいキノコ'),
		('MushRare'            , 'めずらしいキノコ'),
		('DIYStone'            , 'D：石'),
		('DIYClay'             , 'D：粘土'),
		('DIYIron'             , 'D：鉄鉱石'),
		('DIYGold'             , 'D：金鉱石'),
		('ShellSnail'          , '貝：巻き貝'),
		('ShellBivalve'        , '貝：二枚貝'),
		('ShellCoral'          , '貝：サンゴ'),
		('SmartPhone'          , 'スマホ'),
		('Paper'               , '紙きれ1まい'),
		('Map'                 , '地図'),
		('GeneralBox'          , '汎用アイコン：箱'),
		('GeneralSack'         , '汎用アイコン：袋'),
		('Starpiece'           , 'ほしのかけら'),
		('StarpieceRare'       , 'ねがいのけっしょう'),
		('StarpieceCapricornus', 'やぎざのかけら'),
		('StarpieceAquarius'   , 'みずがめざのかけら'),
		('StarpiecePisces'     , 'うおざのかけら'),
		('StarpieceAries'      , 'おひつじざのかけら'),
		('StarpieceTaurus'     , 'おうしざのかけら'),
		('StarpieceGemini'     , 'ふたござのかけら'),
		('StarpieceCancer'     , 'かにざのかけら'),
		('StarpieceLeo'        , 'ししざのかけら'),
		('StarpieceVirgo'      , 'おとめざのかけら'),
		('StarpieceLibra'      , 'てんびんざのかけら'),
		('StarpieceScorpio'    , 'さそりざのかけら'),
		('StarpieceSagittarius', 'いてざのかけら'),
		('WPaperYellow'        , 'ラッピングペーパー：イエロー'),
		('WPaperPink'          , 'ラッピングペーパー：ピンク'),
		('WPaperOrange'        , 'ラッピングペーパー：オレンジ'),
		('WPaperLightGreen'    , 'ラッピングペーパー：キミドリ'),
		('WPaperGreen'         , 'ラッピングペーパー：ミドリ'),
		('WPaperMint'          , 'ラッピングペーパー：ミント'),
		('WPaperLightBlue'     , 'ラッピングペーパー：ライトブルー'),
		('WPaperPurple'        , 'ラッピングペーパー：パープル'),
		('WPaperNavy'          , 'ラッピングペーパー：ネイビー'),
		('WPaperBlue'          , 'ラッピングペーパー：ブルー'),
		('WPaperWhite'         , 'ラッピングペーパー：ホワイト'),
		('WPaperRed'           , 'ラッピングペーパー：レッド'),
		('WPaperGold'          , 'ラッピングペーパー：ゴールド'),
		('WPaperBrown'         , 'ラッピングペーパー：ブラウン'),
		('WPaperGray'          , 'ラッピングペーパー：グレー'),
		('WPaperBlack'         , 'ラッピングペーパー：ブラック'),
		('WParcelYellow'       , 'ラッピング袋：イエロー'),
		('WParcelPink'         , 'ラッピング袋：ピンク'),
		('WParcelOrange'       , 'ラッピング袋：オレンジ'),
		('WParcelLightGreen'   , 'ラッピング袋：キミドリ'),
		('WParcelGreen'        , 'ラッピング袋：ミドリ'),
		('WParcelMint'         , 'ラッピング袋：ミント'),
		('WParcelLightBlue'    , 'ラッピング袋：ライトブルー'),
		('WParcelPurple'       , 'ラッピング袋：パープル'),
		('WParcelNavy'         , 'ラッピング袋：ネイビー'),
		('WParcelBlue'         , 'ラッピング袋：ブルー'),
		('WParcelWhite'        , 'ラッピング袋：ホワイト'),
		('WParcelRed'          , 'ラッピング袋：レッド'),
		('WParcelGold'         , 'ラッピング袋：ゴールド'),
		('WParcelBrown'        , 'ラッピング袋：ブラウン'),
		('WParcelGary'         , 'ラッピング袋：グレー'),
		('WParcelBlack'        , 'ラッピング袋：ブラック'),
		('FlwTulip'            , '花：チューリップ'),
		('FlwPansy'            , '花：パンジー'),
		('FlwCosmos'           , '花：コスモス'),
		('FlwRose'             , '花：バラ'),
		('FlwRoseGold'         , '花：バラ金'),
		('FlwLily'             , '花：ユリ'),
		('FlwAnemone'          , '花：アネモネ'),
		('FlwMum'              , '花：キク'),
		('FlwHyacinth'         , '花：ヒヤシンス'),
		('EggGround'           , 'じめんのたまご'),
		('EggRock'             , 'いわのたまご'),
		('EggLeaf'             , 'はっぱのたまご'),
		('EggForest'           , 'もりのたまご'),
		('EggSky'              , 'そらとぶたまご'),
		('EggFish'             , 'サカナのたまご'),
		('MessageBottleEgg'    , 'たまごのメッセージボトル'),
	))
	_d65f862b = Enum(0xd65f862b, (
		('None'        , 'なし'),
		('FluorLamp'   , '電球'),
		('Candle'      , 'ろうそく'),
		('EmissionOnly', 'エミッションのみ'),
		('SpotLight'   , 'スポットライト'),
		('Monitor'     , 'モニター'),
	))
	_9a3fb47c = Enum(0x9a3fb47c, (
		('None'          , 'なし'),
		('Fan'           , 'せんぷうき'),
		('Airconditioner', 'エアコン'),
		('FanWall'       , 'かべかけせんぷうき'),
	))
	_85c63b71 = U32(0x85c63b71)
	_8392798c = Enum(0x8392798c, enum_GenderBias)
	_60c99a5e = Enum(0x60c99a5e, (
		('None'       , 'なし'),
		('C_Normal'   , '帽子・普通'),
		('C_Brim'     , '帽子・つば(横)'),
		('C_BrimUnder', '帽子・つば(横下)'),
		('C_Bandana'  , '帽子・バンダナ'),
		('C_Knit'     , '帽子・ニット帽'),
		('C_Mask'     , '帽子・おめん'),
		('C_Crown'    , '帽子・わっか'),
		('C_Forehead' , '帽子・おでこ'),
		('C_Top'      , '帽子・後頭部'),
		('C_LeftBig'  , '帽子・左(大)'),
		('C_Left'     , '帽子・左'),
		('C_Right'    , '帽子・右'),
		('G_Normal'   , 'メガネ・普通'),
		('G_Down'     , 'メガネ・普通(下)'),
		('G_UP'       , 'メガネ・普通(上)'),
		('G_Fit'      , 'メガネ・近い(強)'),
		('G_FitLittle', 'メガネ・近い(弱)'),
		('G_Left'     , 'メガネ・片目(左)'),
		('G_Beard'    , 'メガネ・ひげメガネ'),
	))
	_041c3234 = Enum(0x041c3234, enum_0e0acf95)
	Price = S32(0x718b024d)
	RideHeight = Float(0xb662662c)
	_0e6ca0d4 = Enum(0x0e6ca0d4, enum_0e6ca0d4)
	_e1bf0894 = Enum(0xe1bf0894, (
		('None'  , 'なし'),
		('Up'    , '上'),
		('Middle', '中'),
		('Down'  , '下'),
	))
	BridgeTypeId = U16(0x5c1c3044)
	_02169dc7 = U16(0x02169dc7)
	_c353ef20 = U16(0xc353ef20) # possible string size 2
	_bcf5d17a = U16(0xbcf5d17a)
	_bee071da = U16(0xbee071da)
	FloorTableId = U16(0xc833b068)
	_9ec34ed4 = U16(0x9ec34ed4)
	_9bd046a2 = U16(0x9bd046a2)
	RemakeID = S16(0xcb5eb33f)
	_88a6501c = U16(0x88a6501c)
	SlopeTableId = U16(0xbfba247c)
	UniqueID = U16(0x54706054)
	WallTableId = U16(0x0f9f6747)
	_e8c448b2 = U32(0xe8c448b2)
	_fa71e75c = U32(0xfa71e75c)
	_42cd8039 = U32(0x42cd8039) # possible string size 4
	_12d4d7a6 = U32(0x12d4d7a6)
	_fd415a4c = U8(0xfd415a4c)
	_e4697080 = U8(0xe4697080)
	CaptureDiyIcon = U8(0xe24d9b0e)
	_f179f796 = U8(0xf179f796)
	_e65df243 = U8(0xe65df243)
	CapturePreset = String(0xfc275e86) # string32
	DefaultSwitch = U8(0xd862189a)
	FrontSwitch = U8(0x147e658d)
	HasJmp = U8(0xa4db9685)
	_4b97cdab = U8(0x4b97cdab)
	_bea3e8b8 = U8(0xbea3e8b8)
	_3cda3274 = U8(0x3cda3274)
	_b8cc232c = String(0xb8cc232c) # size 64
	_805cdabb = U8(0x805cdabb)
	Label = String(0x3febc642) # string50
	_deb3f8dc = U8(0xdeb3f8dc)
	_48ef0398 = String(0x48ef0398) # size 64
	_86efa036 = U8(0x86efa036)
	ToiletType = U8(0x0eb7fa40)
	TouchRumble = U8(0x7404ebb3)
	ValidEffect = U8(0x49cc96d0) # size is 4, could this be an array?

class ItemPlayerInitialOutfitBoyAWParam(Row):
	AcceEye = U16(0x2b57b24a)
	AcceMouth = U16(0x9403c267)
	Bottoms = U16(0xcc136eb5)
	Cap = U16(0x291a1b04)
	Shoes = U16(0xce827d47)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class ItemPlayerInitialOutfitBoySSParam(Row):
	AcceEye = U16(0x2b57b24a)
	AcceMouth = U16(0x9403c267)
	Bottoms = U16(0xcc136eb5)
	Cap = U16(0x291a1b04)
	Shoes = U16(0xce827d47)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class ItemPlayerInitialOutfitGirlAWParam(Row):
	AcceEye = U16(0x2b57b24a)
	AcceMouth = U16(0x9403c267)
	Bottoms = U16(0xcc136eb5)
	Cap = U16(0x291a1b04)
	Shoes = U16(0xce827d47)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class ItemPlayerInitialOutfitGirlSSParam(Row):
	AcceEye = U16(0x2b57b24a)
	AcceMouth = U16(0x9403c267)
	Bottoms = U16(0xcc136eb5)
	Cap = U16(0x291a1b04)
	Shoes = U16(0xce827d47)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class ItemPlayerTopsForm(Row):
	_390f180d = U32(0x390f180d) # possible string size 4
	_7eaf62dd = U32(0x7eaf62dd) # possible string size 4
	_b64fedad = U32(0xb64fedad)
	_1e4ff55f = U32(0x1e4ff55f)
	UniqueID = U16(0x54706054)
	Label = String(0x13ab5198) # string64
	_036e8ebe = String(0x036e8ebe) # size 64
	_4e3ee3de = String(0x4e3ee3de) # size 64
	_df7ab4c3 = String(0xdf7ab4c3) # size 64
	_48ef0398 = String(0x48ef0398) # size 64
	_15d08d9a = String(0x15d08d9a) # size 34

class ItemRemake(Row):
	_35917e05 = Enum(0x35917e05, (
		('None'             , 'なし'),
		('MyDesign'         , 'マイデザ'),
		('CommonAndMyDesign', '汎用&マイデザ'),
	))
	_c54eaad9 = Enum(0xc54eaad9, enum_c54eaad9)
	_924c8d08 = U32(0x924c8d08)
	_8331e771 = U32(0x8331e771)
	_3aca3c99 = U32(0x3aca3c99)
	_a1cb3383 = U32(0xa1cb3383)
	_1830e86b = U32(0x1830e86b)
	_094d8212 = U32(0x094d8212)
	_b0b659fa = U32(0xb0b659fa)
	_9938d8a6 = U32(0x9938d8a6)
	_20c3034e = U32(0x20c3034e) # possible string size 4
	_31be6937 = U32(0x31be6937) # possible string size 4
	_8845b2df = U32(0x8845b2df) # possible string size 4
	_1344bdc5 = U32(0x1344bdc5) # possible string size 4
	_aabf662d = U32(0xaabf662d) # possible string size 4
	_bbc20c54 = U32(0xbbc20c54) # possible string size 4
	_0239d7bc = U32(0x0239d7bc) # possible string size 4
	_a86c26bb = Enum(0xa86c26bb, (
		('Normal'       , '通常'),
		('ForceOriginal', 'オリジナル強制'),
	))
	ItemUniqueID = U16(0xfd9af1e1)
	_29ecb129 = U16(0x29ecb129)
	UniqueID = U16(0x54706054)
	_d4f43b0b = U8(0xd4f43b0b)
	_1b98fdf8 = U8(0x1b98fdf8)
	_a3249a9d = U8(0xa3249a9d)
	_f45a96c6 = U8(0xf45a96c6)
	_4ce6f1a3 = U8(0x4ce6f1a3)
	_1f6d2dc5 = U8(0x1f6d2dc5)
	_a7d14aa0 = U8(0xa7d14aa0)
	_f0af46fb = U8(0xf0af46fb)
	_4813219e = U8(0x4813219e)
	_12735d82 = U8(0x12735d82)
	_aacf3ae7 = U8(0xaacf3ae7)
	_fdb136bc = U8(0xfdb136bc)
	_450d51d9 = U8(0x450d51d9)
	_16868dbf = U8(0x16868dbf)
	_ae3aeada = U8(0xae3aeada)
	_f944e681 = U8(0xf944e681)
	_41f881e4 = U8(0x41f881e4)
	_b0304b0d = U8(0xb0304b0d)
	_545f8769 = U8(0x545f8769)
	_ece3e00c = U8(0xece3e00c)
	_62c23ed0 = U8(0x62c23ed0)
	_bb9dec57 = U8(0xbb9dec57)
	_03218b32 = U8(0x03218b32)
	_50aa5754 = U8(0x50aa5754)
	_e8163031 = U8(0xe8163031)
	_bf683c6a = U8(0xbf683c6a)
	_07d45b0f = U8(0x07d45b0f)
	_5db42713 = U8(0x5db42713)
	_e5084076 = U8(0xe5084076)
	_b2764c2d = U8(0xb2764c2d)
	_0aca2b48 = U8(0x0aca2b48)
	_5941f72e = U8(0x5941f72e)
	_e1fd904b = U8(0xe1fd904b)
	_b6839c10 = U8(0xb6839c10)
	_0e3ffb75 = U8(0x0e3ffb75)
	_0cb402a3 = U16(0x0cb402a3)

class ItemRemakeCommonPattern(Row):
	_90466afd = Enum(0x90466afd, (
		('None'        , 'なし'),
		('Dot'         , 'ドット'),
		('Stripe'      , 'ストライプ'),
		('CheckA'      , 'チェックA'),
		('CheckB'      , 'チェックB'),
		('TraditionalA', 'トラディショナルA'),
		('TraditionalB', 'トラディショナルB'),
		('Retro'       , 'レトロ'),
		('Natural'     , 'ナチュラル'),
		('Toy'         , 'トイ'),
		('Cool'        , 'クール'),
	))
	_a6b1a7fd = Enum(0xa6b1a7fd, enum_b7cccd84)
	_b7cccd84 = Enum(0xb7cccd84, enum_b7cccd84)
	SortID = U32(0x8fb1ed85)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_5aebbfb5 = String(0x5aebbfb5) # size 66

class ItemRemakeCommonPatternCategory(Row):
	SortID = U32(0x8fb1ed85)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class ItemSeasonalityParam(Row):
	_a9b28820 = U16(0xa9b28820)
	_319a1388 = U16(0x319a1388)
	_859c3e3e = U16(0x859c3e3e)
	_1db4a596 = U16(0x1db4a596)
	_5fad728f = U16(0x5fad728f)
	_c785e927 = U16(0xc785e927)
	_f16b7305 = U16(0xf16b7305)
	_6943e8ad = U16(0x6943e8ad)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class ItemShareTexture(Row):
	UniqueID = U16(0x54706054)
	ResName = String(0xdcfb52e8) # string32

class ItemSize(Row):
	_801351e6 = U32(0x801351e6)
	_09b64264 = U16(0x09b64264)
	_3cf05708 = U16(0x3cf05708)
	UniqueID = U16(0x54706054)
	_16b8f524 = U8(0x16b8f524)
	_bcb13daf = U8(0xbcb13daf)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32

class ItemStrSort(Row):
	_a99eaf49 = U16(0xa99eaf49)
	_cb64c9a0 = U16(0xcb64c9a0)
	_77e82b14 = U16(0x77e82b14)
	_ef987827 = U16(0xef987827)
	_546c2339 = U16(0x546c2339)
	_2a7a644c = U16(0x2a7a644c)
	_67ef88b7 = U16(0x67ef88b7)
	_7e0bbfa4 = U16(0x7e0bbfa4)
	_8ff6331b = U16(0x8ff6331b)
	_a0af4f68 = U16(0xa0af4f68)
	_2da64e66 = U16(0x2da64e66)
	_68832f05 = U16(0x68832f05)
	_f0f37c36 = U16(0xf0f37c36)
	_4b072728 = U16(0x4b072728)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class ItemUIContextMenu(Row):
	Priority = U16(0x200dd382)
	UniqueID = U16(0x54706054)
	AutoDisappear = U8(0xf2ce6e17)
	Label = String(0x87bf00e8) # string32
	_026f0892 = String(0x026f0892) # size 32
	_036e8ebe = String(0x036e8ebe) # size 67

class ItemUnitIcon(Row):
	ScaleOffset = Float(0x68460c05)
	_fc86133a = U16(0xfc86133a)
	UniqueID = U16(0x54706054)
	ColorIndex = S8(0x64b8fff8)
	Label = String(0x87bf00e8) # string32
	ModelName = String(0x39b5a93d) # string32
	_036e8ebe = String(0x036e8ebe) # size 64
	_48ef0398 = String(0x48ef0398) # size 67

class JuneBrideWallFloor(Row):
	_23a01e5b = U32(0x23a01e5b)
	_4e718582 = U16(0x4e718582)
	_a1249129 = U16(0xa1249129)
	UniqueID = U16(0x54706054)
	_350e1ef9 = U16(0x350e1ef9)

class LocalizeNameConvertParam(Row):
	UniqueID = U16(0x54706054)
	BaseName = String(0x50edd045) # string32
	_d22a8fc9 = U8(0xd22a8fc9)
	_f551b995 = U8(0xf551b995)
	_1f301724 = U8(0x1f301724)
	_bd439866 = U8(0xbd439866)
	_425f85d3 = U8(0x425f85d3)
	_e5644dde = U8(0xe5644dde)
	_c2e9eebe = U8(0xc2e9eebe)
	_4ae88c28 = U8(0x4ae88c28)
	_638671f9 = U8(0x638671f9)
	_558685c5 = U8(0x558685c5)
	LocalizeAnim = U8(0xc70be94f)
	LocalizeModel = U8(0x9ff07c89)
	LocalizeTexture = U8(0x086f5f3a)
	_548a7eda = U8(0x548a7eda)
	_aeb768f7 = U8(0xaeb768f7)
	_0cc4e7b5 = U8(0x0cc4e7b5)
	_f3d8fa00 = U16(0xf3d8fa00)

class MannequinCoodinate(Row):
	_1c73934d = Enum(0x1c73934d, (
		('MannequinPause01', 'ポーズ1'),
		('MannequinPause02', 'ポーズ2'),
		('MannequinPause03', 'ポーズ3'),
		('MannequinPause04', 'ポーズ4'),
		('MannequinPause05', 'ポーズ5'),
		('MannequinPause06', 'ポーズ6'),
	))
	_b44dbf73 = U32(0xb44dbf73)
	_395b7795 = U16(0x395b7795)
	_79ad3f84 = U16(0x79ad3f84)
	Bottoms = U16(0xcc136eb5)
	Cap = U16(0x291a1b04)
	Shoes = U16(0xce827d47)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)

class MaterialType(Row):
	SoundAttribute = U16(0x2e17a0a7)
	UniqueID = U16(0x54706054)
	DebugName = String(0xab51a3cf) # string32

class MessageCardBoardDesignParam(Row):
	BackColor = U16(0xa2fe7f71)
	BodyColor = U16(0x41afe839)
	FootColor = U16(0x57c98e5b)
	HeadColor = U16(0x32c0c064)
	_990406a9 = U16(0x990406a9) # possible string size 2
	_dea47c79 = U16(0xdea47c79)
	_e3c455c9 = U16(0xe3c455c9)
	_51e489d9 = U16(0x51e489d9)
	RuleColor = U16(0x94d6cb5d)
	TextLotId = S16(0x5f384120)
	_84818e10 = U16(0x84818e10) # possible string size 2
	UniqueID = U16(0x54706054)
	_4b9c4229 = String(0x4b9c4229) # size 64

class MessageCardColorParam(Row):
	Color = U32(0xf0cf80ff)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class MessageCardDesignParam(Row):
	BackColor = U16(0xa2fe7f71)
	BodyColor = U16(0x41afe839)
	_63a46970 = U16(0x63a46970) # possible string size 2
	FootColor = U16(0x57c98e5b)
	HeadColor = U16(0x32c0c064)
	_990406a9 = U16(0x990406a9)
	_dea47c79 = U16(0xdea47c79)
	_e3c455c9 = U16(0xe3c455c9)
	_51e489d9 = U16(0x51e489d9)
	RuleColor = U16(0x94d6cb5d)
	_953983b4 = U16(0x953983b4)
	_d299f964 = U16(0xd299f964)
	_ada3644a = U16(0xada3644a)
	_ea031e9a = U16(0xea031e9a)
	TextLotId = S16(0x5f384120)
	_84818e10 = U16(0x84818e10) # possible string size 2
	UniqueID = U16(0x54706054)
	Kind = U8(0x24da7ada)
	_4b9c4229 = String(0x4b9c4229) # size 64
	_aa738fed = U8(0xaa738fed)
	_7a6965c5 = U32(0x7a6965c5)

class MessageCardSelectDesign(Row):
	_37571146 = U32(0x37571146)
	_e486805c = U16(0xe486805c)
	_a326fa8c = U16(0xa326fa8c)
	_9e46d33c = U16(0x9e46d33c)
	_2c660f2c = U16(0x2c660f2c)
	_d29880f2 = U16(0xd29880f2)
	_9538fa22 = U16(0x9538fa22)
	_8cc22007 = U16(0x8cc22007)
	_cb625ad7 = U16(0xcb625ad7)
	_ccc4afcb = U16(0xccc4afcb)
	_8b64d51b = U16(0x8b64d51b)
	_1bf6abea = U16(0x1bf6abea)
	_5c56d13a = U16(0x5c56d13a)

class MessageCardSelectDesignSp(Row):
	_37571146 = U32(0x37571146)
	_e486805c = U16(0xe486805c)
	_a326fa8c = U16(0xa326fa8c) # possible string size 2
	_9e46d33c = U16(0x9e46d33c) # possible string size 2
	_2c660f2c = U16(0x2c660f2c) # possible string size 2
	_d29880f2 = U16(0xd29880f2) # possible string size 2
	_9538fa22 = U16(0x9538fa22) # possible string size 2
	_8cc22007 = U16(0x8cc22007) # possible string size 2
	_cb625ad7 = U16(0xcb625ad7) # possible string size 2
	_ccc4afcb = U16(0xccc4afcb) # possible string size 2
	_8b64d51b = U16(0x8b64d51b) # possible string size 2
	_1bf6abea = U16(0x1bf6abea) # possible string size 2
	_5c56d13a = U16(0x5c56d13a) # possible string size 2

class MessageCardSelectPresent(Row):
	ItemCategory = U32(0x368210c4)
	ItemCategoryGroup = U32(0x128a3d9b)
	_37571146 = U32(0x37571146)
	_e060d3cd = U16(0xe060d3cd)
	ItemRemakeType = U8(0xc233727b) # size is 2, could this be an array?

class MessageCardSelectPresentSp(Row):
	ItemCategory = U32(0x368210c4)
	ItemCategoryGroup = U32(0x128a3d9b)
	_37571146 = U32(0x37571146)
	_e060d3cd = U16(0xe060d3cd)
	ItemRemakeType = U8(0xc233727b) # size is 2, could this be an array?

class MuseumArtDonateInfo(Row):
	_be776e71 = U32(0xbe776e71) # possible string size 4
	ModelID = U16(0xfdeed09c)
	UniqueID = U16(0x54706054)
	WatchItem = U16(0xb76b7d37)
	CameraParamName = String(0xb16c3035) # string33

class MuseumFossilDonateInfo(Row):
	_be776e71 = Enum(0xbe776e71, enum_be776e71)
	ModelID = U16(0xfdeed09c)
	UniqueID = U16(0x54706054)
	WatchItem = U16(0xb76b7d37)
	CameraParamName = String(0xb16c3035) # string33

class MuseumNPCLayoutInfo(Row):
	UniqueID = U16(0x54706054)
	WatchItem = U16(0xb76b7d37)
	WatchPointID = U16(0x4765b463)
	_e9812e07 = String(0xe9812e07) # size 25
	_b434805d = U32(0xb434805d) # possible string size 4
	_60e4e478 = String(0x60e4e478) # size 25
	_97be8767 = U32(0x97be8767) # possible string size 4

class MuseumNPCSilhouette(Row):
	_110ca7b2 = U32(0x110ca7b2)
	SilhouettePosX = Float(0x0f230d34)
	SilhouettePosY = Float(0x32432484)
	SilhouettePosZ = Float(0x75e35e54)
	UniqueID = U16(0x54706054)
	_7c6429ea = String(0x7c6429ea) # size 66

class MuseumNPCSpotTalk(Row):
	_be776e71 = Enum(0xbe776e71, enum_be776e71)
	UniqueID = U16(0x54706054)
	_8e768bd8 = String(0x8e768bd8) # size 25
	_9d9b3598 = U32(0x9d9b3598) # possible string size 4
	_b10b6bc8 = String(0xb10b6bc8) # size 65

class MuseumNameboardInfo(Row):
	NameboardAngleY = Float(0x2c40799e)
	NameboardPosX = Float(0xdf33ee48)
	NameboardPosY = Float(0xe253c7f8)
	NameboardPosZ = Float(0xa5f3bd28)
	_be776e71 = Enum(0xbe776e71, enum_be776e71)
	_1ef061dd = U16(0x1ef061dd)
	_3574933b = U16(0x3574933b)
	_dfacc347 = U16(0xdfacc347)
	_50650a2b = U16(0x50650a2b)
	_b58d7541 = U16(0xb58d7541)
	UniqueID = U16(0x54706054)
	ModelResName = String(0xfad4ff78) # string65
	_c1bb7d2d = U16(0xc1bb7d2d) # possible string size 3

class MuseumStampRackInfo(Row):
	_be776e71 = U32(0xbe776e71)
	_98ff7f38 = U32(0x98ff7f38)
	_e23f2c58 = U32(0xe23f2c58)
	_b02f0c17 = U16(0xb02f0c17)
	_f78f76c7 = U16(0xf78f76c7)
	_caef5f77 = U16(0xcaef5f77)
	_d4f5b3e6 = U16(0xd4f5b3e6)
	UniqueID = U16(0x54706054)
	_a90b807e = U8(0xa90b807e)
	_0512b63c = String(0x0512b63c) # size 32
	_4ab9b98a = String(0x4ab9b98a) # size 32
	_96d80132 = String(0x96d80132) # size 32
	_ed4b6070 = U8(0xed4b6070)

class MuseumWatchPoint(Row):
	SilhouetteID = U32(0x3e884a6d)
	_be776e71 = Enum(0xbe776e71, enum_be776e71)
	_35ac2c17 = Enum(0x35ac2c17, (
		('Always' , '常時'),
		('Daytime', '昼'),
		('Night'  , '夜'),
	))
	_1f3893e5 = U32(0x1f3893e5)
	_2258ba55 = U32(0x2258ba55)
	_65f8c085 = U32(0x65f8c085)
	WatchAngleY = Float(0xd200ffd3)
	WatchPosX = Float(0x2633f2c1)
	WatchPosY = Float(0x1b53db71)
	WatchPosZ = Float(0x5cf3a1a1)
	UniqueID = U16(0x54706054)
	BattlePoint = U8(0x91eaeedd)
	_85fb9dd5 = String(0x85fb9dd5) # size 65
	SilhouettePoint = U8(0xf58109f5) # size is 4, could this be an array?

class MysteryTourFieldParam(Row):
	_e8fa8b93 = Enum(0xe8fa8b93, (
		('NoRiver'  , '河口なし'),
		('WestRiver', '西河口'),
		('EastRiver', '東河口'),
	))
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class MysteryTourFishParam(Row):
	UniqueID = U16(0x54706054)
	TargetShadow = U8(0xc35f78ed) # size is 2, could this be an array?

class MysteryTourInsectParam(Row):
	UniqueID = U16(0x54706054)
	TargetInsect = U8(0xd086a528) # size is 14, could this be an array?

class MysteryTourItemParam(Row):
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class MysteryTourParam(Row):
	_dd59b554 = Enum(0xdd59b554, (
		('Normal'         , '普通'),
		('StoneMaterial'  , '素材岩'),
		('StoneCoin'      , 'コイン岩'),
		('StoneGold'      , 'きんこうせきの岩'),
		('Bamboo'         , '竹とタケノコ'),
		('TreeMoney'      , '小銭つきの木'),
		('TreeSisterFruit', '姉妹フルーツの木'),
		('FlowerRare'     , 'レアな花'),
	))
	_1c8d9dbc = Enum(0x1c8d9dbc, (
		('Normal', '通常'),
	))
	FishPattern = S16(0xb1f384dc)
	InsectPattern = S16(0xe23c6453)
	_bc5f2a7b = U16(0xbc5f2a7b)
	_813f03cb = U16(0x813f03cb)
	_72573f73 = U16(0x72573f73)
	_7a09986c = U16(0x7a09986c)
	UniqueID = U16(0x54706054)
	_7215b154 = String(0x7215b154) # size 32
	_88bd09c2 = String(0x88bd09c2) # size 32
	_4e5cd9f3 = String(0x4e5cd9f3) # size 32
	_8f2f4bf9 = String(0x8f2f4bf9) # size 32
	_0b3d1d54 = String(0x0b3d1d54) # size 32
	SelectWeight = U8(0xd89a0db0)
	_b1589411 = U8(0xb1589411)

class NmlNpcParam(Row):
	_a54f92fd = U32(0xa54f92fd)
	_e2efe82d = U32(0xe2efe82d)
	_5ef86f1f = U32(0x5ef86f1f)
	_195815cf = U32(0x195815cf)
	_bea84522 = Enum(0xbea84522, (
		('Prefer', '好む'),
		('Normal', '気にせず'),
		('Avoid' , '避ける'),
	))
	_9eea1288 = Enum(0x9eea1288, (
		('Undefined', '未設定'),
		('Play'     , 'あそび'),
		('Music'    , '音楽'),
		('Fitness'  , 'フィットネス'),
		('Fashion'  , 'ファッション'),
		('Education', '教養'),
		('Nature'   , '自然愛'),
	))
	_04f52f6a = Enum(0x04f52f6a, (
		('Boy_normal'  , 'ぼんやり男'),
		('Boy_active'  , 'ハキハキ男'),
		('Boy_pride'   , 'コワイ男'),
		('Boy_snobby'  , 'キザ男'),
		('Girl_normal' , '普通女'),
		('Girl_active' , '元気女'),
		('Girl_pride'  , 'オトナ女'),
		('Girl_big_sis', 'アネキ女'),
	))
	_aa4403ea = Enum(0xaa4403ea, (
		('Undefined', '未設定'),
		('Low'      , '低'),
		('Normal'   , '中'),
		('High'     , '高'),
	))
	_0e7ab6a6 = Enum(0x0e7ab6a6, (
		('Stop', 'ストップ'),
		('Tie' , 'タイ'),
	))
	_dd2d2adc = Enum(0xdd2d2adc, (
		('Normal' , 'イーブン'),
		('Shuffle', 'シャッフル'),
		('Random' , 'ランダム'),
	))
	_08238405 = U16(0x08238405) # possible string size 2
	BromideItemID = S16(0x71bf253b)
	FloorType = U16(0x0b52f5bb)
	PosterItemID = S16(0x0f640691)
	RainHat = U16(0x03200971)
	_1d69405f = U16(0x1d69405f)
	_57e889b2 = U16(0x57e889b2)
	SmartphoneRemakePattern = U16(0xf8be7f94)
	Tops = U16(0x870f1e29)
	Umbrella = U16(0xbb9c816e)
	UniqueID = U16(0x54706054)
	WallType = U16(0xda63a0cc)
	_919ea52a = U8(0x919ea52a)
	BirthMonth = U8(0x9456b6a3)
	_34eb5dc3 = U8(0x34eb5dc3)
	_265ef22d = U8(0x265ef22d)
	_4ce98793 = String(0x4ce98793) # size 64
	_c1fb0035 = String(0xc1fb0035) # size 64
	InitLive = U8(0x454b2adc)
	_566f1d31 = U8(0x566f1d31)
	_2f1b930d = String(0x2f1b930d) # size 8
	NpcColor = U8(0x41977699)
	NpcTalkType = U8(0x33af13e1)
	_48ef0398 = String(0x48ef0398) # size 64
	SpecialELink = U8(0x04ac1bea)
	SpecialSLink = U8(0xbe782346)
	_21c5bbd6 = U8(0x21c5bbd6)
	_e52f0037 = U8(0xe52f0037)
	_42f255d5 = U32(0x42f255d5)

class NmlNpcRaceParam(Row):
	AnimeTypeBag = String(0x85e386bb) # string64
	AnimeTypeBasket = String(0xcb358e51) # string64
	_9916cf87 = String(0x9916cf87) # size 64
	AnimeTypeBook = String(0x41935ae1) # string64
	AnimeTypeDrink = String(0x0c98243c) # string64
	AnimeTypeFirewood = String(0x55c343c4) # string64
	AnimeTypeFishingRod = String(0x7c6fde34) # string64
	AnimeTypeFood = String(0x70216bfa) # string64
	AnimeTypeHandGlass = String(0x9951a44b) # string64
	AnimeTypeNet = String(0xfca98253) # string64
	AnimeTypeSitDown = String(0xb109a778) # string64
	AnimeTypeSmartPhone = String(0xd06d98dc) # string64
	AnimeTypeUmbrella = String(0x5e2aa87d) # string64
	AnimeTypeWateringCan = String(0x09b714f9) # string64
	_2f1b930d = String(0x2f1b930d) # size 8

class NpcCastLabelData(Row):
	_02c2ac67 = String(0x02c2ac67) # size 32
	AIFlowName = String(0xf37316e6) # string64
	AppearStage = U8(0x378b2f14)
	CastType = U8(0xb7a6c4a8) # size is 3, could this be an array?

class NpcCastScheduleData(Row):
	_aaae3a0f = U8(0xaaae3a0f)
	_ac0593cc = U8(0xac0593cc)
	CastLabel = U8(0x69a9bb3c)
	_d507df3e = U8(0xd507df3e)
	EndHour = U8(0x675ca211)
	EndMinute = U8(0x2b09d942)
	EventName = String(0x7d740fa4) # string32
	_a78d0cc5 = U8(0xa78d0cc5)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd)
	_e76db92f = U16(0xe76db92f)

class NpcEquipRule(Row):
	_423d1c4d = Enum(0x423d1c4d, (
		('None'      , '×'),
		('Sometimes' , '△'),
		('Relatively', '〇'),
		('Always'    , '◎'),
	))
	_b219374f = Enum(0xb219374f, (
		('None' , '-'),
		('Limit', '限'),
	))
	_68d62ca8 = Enum(0x68d62ca8, (
		('None'     , '-'),
		('Enable'   , '可'),
		('Condition', '条'),
	))
	_1f401b52 = U32(0x1f401b52)
	_e765b554 = U32(0xe765b554)
	_cbbe9d2d = U32(0xcbbe9d2d)
	SeasonScore = S32(0x79be959d)
	_a3dc7c4c = U32(0xa3dc7c4c)
	UniqueID = U16(0x54706054)
	_f9cf603a = U8(0xf9cf603a)
	_2c2a379e = U8(0x2c2a379e)
	_a4396b29 = U8(0xa4396b29)
	_744b3452 = U8(0x744b3452)
	_a073aa81 = U8(0xa073aa81)
	_fdf8907b = U8(0xfdf8907b)
	Label = String(0x87bf00e8) # string32
	_74275e7a = U8(0x74275e7a) # possible string size 1
	_cc198281 = U8(0xcc198281) # possible string size 1
	_14767df7 = U8(0x14767df7) # possible string size 1
	_036e8ebe = String(0x036e8ebe) # size 65

class NpcInterest(Row):
	Offset = Float(0xecf95b05)
	ContinuousTime = U16(0xb694c63b)
	ItemUniqueID = U16(0xfd9af1e1)
	_40876b17 = U8(0x40876b17)
	ConditionType = U8(0xa8644472)
	FlagType = U8(0x430dbf65)
	_6bcf870d = U8(0x6bcf870d)
	_a0d9d29e = U8(0xa0d9d29e)
	LabelType = U8(0xd7ded52a)
	_604df507 = String(0x604df507) # size 32
	_a0efadac = U8(0xa0efadac)
	NeedType = U8(0xd6b82305)
	RainActive = U8(0xa9de0384)
	_154eee75 = U8(0x154eee75)
	_d2ab4a8f = U8(0xd2ab4a8f)
	_a0b3903d = U8(0xa0b3903d)
	_1cb2e5a6 = U8(0x1cb2e5a6)
	_cfca2366 = U8(0xcfca2366)
	_92827ae7 = U8(0x92827ae7)
	_fa3b3608 = U8(0xfa3b3608)
	_e4fe6719 = U8(0xe4fe6719)
	_b9e9f361 = U8(0xb9e9f361)
	_2ae7c830 = U8(0x2ae7c830)
	_1b6eaa53 = U8(0x1b6eaa53)
	_8d3bad84 = U8(0x8d3bad84)
	_ee0961fa = U8(0xee0961fa)
	_8eabc257 = String(0x8eabc257) # size 34

class NpcLife(Row):
	_3b27f030 = U32(0x3b27f030)
	ItemUniqueID = U16(0xfd9af1e1)
	_76e5e67a = U16(0x76e5e67a)
	_40876b17 = U8(0x40876b17)
	EquipRule = String(0xd941db12) # string32
	FlagType = U8(0x430dbf65)
	_bdd4dc0f = U8(0xbdd4dc0f)
	_cd61ce25 = U8(0xcd61ce25)
	_9fbbc76b = U8(0x9fbbc76b)
	_54ab2c62 = U8(0x54ab2c62)
	_a42b13ce = U8(0xa42b13ce)
	_1eb65d06 = U8(0x1eb65d06)
	_ebd71bbd = U8(0xebd71bbd)
	_630a25b4 = U8(0x630a25b4)
	_38954eb6 = U8(0x38954eb6)
	_1f3bcf5e = U8(0x1f3bcf5e)
	LookAtType = U8(0x35c78d62)
	_604df507 = String(0x604df507) # size 32
	NetPlay = U8(0xf196e054)
	RainActive = U8(0xa9de0384)
	_67850558 = U8(0x67850558)
	_7c1b4734 = U8(0x7c1b4734)
	_eaadf252 = U8(0xeaadf252)
	_2760bc87 = U8(0x2760bc87)
	_b2540403 = U8(0xb2540403)
	SpotType = U8(0x9bc85bd0) # size is 3, could this be an array?
	_154eee75 = U8(0x154eee75)
	_d2ab4a8f = U8(0xd2ab4a8f)
	_a0b3903d = U8(0xa0b3903d)
	_1cb2e5a6 = U8(0x1cb2e5a6)
	_cfca2366 = U8(0xcfca2366)
	_92827ae7 = U8(0x92827ae7)
	_fa3b3608 = U8(0xfa3b3608)
	_e4fe6719 = U8(0xe4fe6719)
	_b9e9f361 = U8(0xb9e9f361)
	_2ae7c830 = U8(0x2ae7c830)
	_1b6eaa53 = U8(0x1b6eaa53)
	_8d3bad84 = U8(0x8d3bad84)
	_ee0961fa = U8(0xee0961fa)
	_8eabc257 = String(0x8eabc257) # size 32

class NpcLooksParam(Row):
	_6ffec71e = U32(0x6ffec71e) # possible string size 4
	_529eeeae = U32(0x529eeeae) # possible string size 4
	_153e947e = U32(0x153e947e) # possible string size 4
	_a1e8d2bb = U32(0xa1e8d2bb) # possible string size 4
	_9c88fb0b = U32(0x9c88fb0b) # possible string size 4
	_db2881db = U32(0xdb2881db) # possible string size 4
	_c4bb5846 = U32(0xc4bb5846) # possible string size 4
	_f9db71f6 = U32(0xf9db71f6) # possible string size 4
	_be7b0b26 = U32(0xbe7b0b26) # possible string size 4
	_b305defd = U32(0xb305defd) # possible string size 4
	_8e65f74d = U32(0x8e65f74d) # possible string size 4
	_c9c58d9d = U32(0xc9c58d9d) # possible string size 4
	_c34424c7 = U32(0xc34424c7) # possible string size 4
	_fe240d77 = U32(0xfe240d77) # possible string size 4
	_b98477a7 = U32(0xb98477a7) # possible string size 4
	_20624ee7 = U32(0x20624ee7) # possible string size 4
	_1d026757 = U32(0x1d026757) # possible string size 4
	_5aa21d87 = U32(0x5aa21d87) # possible string size 4
	_48a92c68 = U32(0x48a92c68) # possible string size 4
	_75c905d8 = U32(0x75c905d8) # possible string size 4
	_32697f08 = U32(0x32697f08) # possible string size 4
	_effe09fe = U32(0xeffe09fe)
	_d29e204e = U32(0xd29e204e)
	_953e5a9e = U32(0x953e5a9e)
	_d598c60d = U32(0xd598c60d) # possible string size 4
	_e8f8efbd = U32(0xe8f8efbd) # possible string size 4
	_af58956d = U32(0xaf58956d) # possible string size 4
	_eb39552d = U32(0xeb39552d) # possible string size 4
	_d6597c9d = U32(0xd6597c9d) # possible string size 4
	_91f9064d = U32(0x91f9064d) # possible string size 4
	_6f9dd83d = U32(0x6f9dd83d) # possible string size 4
	_52fdf18d = U32(0x52fdf18d) # possible string size 4
	_155d8b5d = U32(0x155d8b5d) # possible string size 4
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class NpcMoveRoomTemplate(Row):
	RoomType = U32(0xd9a1f501)
	Direction = S8(0x3a1fca06)
	GroupIndex = S8(0xb12e26da)
	Size = S8(0x0b6d59d2)
	_ef0088e8 = U8(0xef0088e8)
	_8f5c3da3 = U32(0x8f5c3da3)

class NpcMsgBullfestParam(Row):
	_ddf1f8bf = Enum(0xddf1f8bf, (
		('None'                      , '無し'),
		('NpcRelatedTops'            , 'NPC関連服'),
		('NpcRelatedAccessory'       , 'NPC関連アクセサリ'),
		('CapOrHelmet'               , '帽子・被り物'),
		('Accessory'                 , 'アクセサリ'),
		('Bottoms'                   , 'ボトムス'),
		('Shoes'                     , '靴'),
		('MyDesignTopsByPlayer'      , 'P自作マイデザイン服'),
		('MyDesignTopsByOtherPlayer' , '他人作マイデザイン服'),
		('MyDesignTopsByOtherVillage', '他村製マイデザイン服'),
		('SprintTopsInSpring'        , '春に春服を着用'),
		('SummerTopsInSummer'        , '夏に夏服を着用'),
		('AutumnTopsInAutumn'        , '秋に秋服を着用'),
		('WinterTopsInWinter'        , '冬に冬服を着用'),
		('WinterTopsInSummer'        , '夏に冬服を着用'),
		('SummerTopsInWinter'        , '冬に夏服を着用'),
		('WearCuteTops'              , 'キュートな服を着用'),
		('WearCoolTops'              , 'クールな服を着用'),
		('WearSimpleTops'            , 'シンプルな服を着用'),
		('WearGorgeousTops'          , 'ゴージャスな服を着用'),
		('WearActiveTops'            , 'アクティブな服を着用'),
		('WearElegantTops'           , 'エレガントな服を着用'),
	))
	_754c57c7 = U16(0x754c57c7)
	_9e7becc4 = U16(0x9e7becc4) # possible string size 2
	AccessoryID = U16(0x478dd182)
	_c35c5af7 = U16(0xc35c5af7)
	_286be1f4 = U16(0x286be1f4) # possible string size 2
	BagID = U16(0x3af6dfe2)
	BottomsID = U16(0x524596a2)
	CapID = U16(0x8ff469e1)
	_cd89ffeb = U16(0xcd89ffeb) # possible string size 2
	_da01c243 = U16(0xda01c243) # possible string size 2
	_8c03fdc7 = U16(0x8c03fdc7)
	_673446c4 = U16(0x673446c4) # possible string size 2
	_b9507563 = U16(0xb9507563)
	_5267ce60 = U16(0x5267ce60) # possible string size 2
	_7b1d9990 = U16(0x7b1d9990)
	_902a2293 = U16(0x902a2293) # possible string size 2
	HelmetID = U16(0xf429d772)
	_5ef56066 = U16(0x5ef56066)
	_b5c2db65 = U16(0xb5c2db65) # possible string size 2
	_d0241896 = U16(0xd0241896)
	_3b13a395 = U16(0x3b13a395) # possible string size 2
	ShoesID = U16(0xf07156d2)
	SocksID = U16(0xe113ac8d)
	_ebb9a634 = U16(0xebb9a634) # possible string size 2
	TopsID = U16(0xdfb46994)
	_003c0210 = U16(0x003c0210) # possible string size 2
	UniqueID = U16(0x54706054)
	_7991b277 = U16(0x7991b277)
	_92a60974 = U32(0x92a60974) # possible string size 4

class NpcRoomTemplate(Row):
	RoomType = U32(0xd9a1f501)
	Direction = S8(0x3a1fca06)
	GroupIndex = S8(0xb12e26da)
	Size = S8(0x0b6d59d2)
	_ef0088e8 = U8(0xef0088e8)
	_8f5c3da3 = U32(0x8f5c3da3)

class NpcSpClothSetParam(Row):
	AcceEye = U16(0x2b57b24a)
	Bottoms = U16(0xcc136eb5)
	Cap = U16(0x291a1b04)
	Shoes = U16(0xce827d47)
	SpNpcID = U16(0x0207a2af)
	Tool = U16(0x973fae34)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_036e8ebe = String(0x036e8ebe) # size 64

class NpcSpModelScale(Row):
	_c7a5b572 = U32(0xc7a5b572)
	_8005cfa2 = U32(0x8005cfa2) # possible string size 4
	_48e540d2 = U32(0x48e540d2) # possible string size 4
	_e0e55820 = U32(0xe0e55820) # possible string size 4
	_91f4a29c = U32(0x91f4a29c) # possible string size 4
	_d654d84c = U32(0xd654d84c) # possible string size 4
	_1eb4573c = U32(0x1eb4573c)
	_b6b44fce = U32(0xb6b44fce)
	_0a65e08a = U32(0x0a65e08a) # possible string size 4
	_4dc59a5a = U32(0x4dc59a5a)
	_8525152a = U32(0x8525152a)
	_2d250dd8 = U32(0x2d250dd8)
	_47ad4181 = U32(0x47ad4181) # possible string size 4
	_000d3b51 = U32(0x000d3b51) # possible string size 4
	_c8edb421 = U32(0xc8edb421) # possible string size 4
	_60edacd3 = U32(0x60edacd3)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 34

class NpcSpServiceMotionRandom(Row):
	SelectSecond = U16(0x1abe6e96)
	UniqueID = U16(0x54706054)
	_9bee16d1 = String(0x9bee16d1) # size 66
	EndHour = U8(0x675ca211)
	Label = String(0x87bf00e8) # string32
	SelectRate = U8(0x1e7ef977)
	StartHour = U8(0x8ae48661)
	Type = U8(0xd1f6dae0) # size is 3, could this be an array?

class NpcSpServiceMotionWork(Row):
	UniqueID = U16(0x54706054)
	_cd16f843 = String(0xcd16f843) # size 66
	_26214340 = String(0x26214340) # size 66
	_c9e3287e = String(0xc9e3287e) # size 66
	_2b3f3307 = String(0x2b3f3307) # size 66
	_c4fd5839 = String(0xc4fd5839) # size 66
	_2fcae33a = String(0x2fcae33a) # size 66
	_c0088804 = String(0xc0088804) # size 66
	_3103d389 = String(0x3103d389) # size 66
	Label = String(0x87bf00e8) # string32
	_94113760 = U8(0x94113760)
	_86a4988e = U8(0x86a4988e)
	_3e18ffeb = U8(0x3e18ffeb)
	_a3cfc752 = U8(0xa3cfc752)
	_1b73a037 = U8(0x1b73a037)
	_09c60fd9 = U8(0x09c60fd9)
	_b17a68bc = U8(0xb17a68bc)
	_e91978ea = U16(0xe91978ea) # possible string size 3

class NpcSpServiceMotionWorkSp(Row):
	UniqueID = U16(0x54706054)
	_9bee16d1 = String(0x9bee16d1) # size 66
	EndHour = U8(0x675ca211)
	SelectRate = U8(0x1e7ef977)
	StartHour = U8(0x8ae48661) # size is 2, could this be an array?

class PlayerStateParam(Row):
	_4045796c = Enum(0x4045796c, (
		('Normal'                      , '通常'),
		('OnlyWallNoGravity'           , '壁のみ/重力無'),
		('OnlyWall'                    , '壁のみ/重力有'),
		('OnlyFloor'                   , '床のみ/重力有'),
		('OnlyOriginalFloor'           , '書き換え前の床のみ/重力有'),
		('NoBgCheckNoGravity'          , 'BGチェック無/重力無'),
		('NoBgCheckUseGravity'         , 'BGチェック無/重力有'),
		('OnlyWallNoGravity_SitSpecial', '立ちのとき壁のみ、座り時BGチェック無/重力無'),
	))
	_ccf68ebe = Enum(0xccf68ebe, (
		('Disable'               , 'デモ不可'),
		('EnableToDemoNetLock'   , 'デモネットロック可'),
		('EnableToDemoAll'       , 'デモ全部可'),
		('EnableToDemoStandSpeak', 'デモ立ちSpeak可'),
		('EnableToDemoSitSpeak'  , 'デモ座りSpeak可'),
		('EnableToDemoBedSpeak'  , 'デモベッドSpeak可'),
		('EnableToDemoSwimSpeak' , 'デモ泳ぎSpeak可'),
		('IsDemo'                , 'デモ状態'),
	))
	ObjCheckRate = Float(0x38762eaa)
	_c5567172 = Enum(0xc5567172, (
		('Normal', '通常'),
		('Heavy' , '動かない'),
		('None'  , 'なし'),
	))
	_f9dcdec7 = Enum(0xf9dcdec7, (
		('Overwrite' , '上書き'),
		('Sequential', '累積'),
	))
	_838b098c = Enum(0x838b098c, (
		('None'  , '追従なし'),
		('Auto'  , '自動追従'),
		('Manual', '手動追従'),
	))
	_f299f7fc = Enum(0xf299f7fc, (
		('Continue'               , '前ステート引継ぎ'),
		('Putaway'                , 'しまう'),
		('IfNotDemoDraw'          , 'デモでなければ表示'),
		('GiveOverKeepPutawayFlag', 'PlayerKeepFlagに従う'),
		('StageIn'                , 'ステージイン'),
	))
	AcceptAccess = U8(0xa6324d34)
	_f413acd2 = U8(0xf413acd2)
	_833e2942 = U8(0x833e2942)
	_730cefc8 = U8(0x730cefc8)
	BgmEnd = U8(0xa9f6fac2)
	_497ac4d6 = U8(0x497ac4d6)
	_63f77486 = U8(0x63f77486)
	_5dcf7b24 = U8(0x5dcf7b24)
	_16e483f0 = U8(0x16e483f0)
	_aa0070b7 = U8(0xaa0070b7)
	_ae3add79 = U8(0xae3add79)
	_1aaaddc1 = U8(0x1aaaddc1)
	_68daf155 = U8(0x68daf155)
	_ecfe9ddb = U8(0xecfe9ddb)
	ForbidOverwrite = U8(0x35fd6466)
	_e550abdf = U8(0xe550abdf)
	_5681a1c3 = U8(0x5681a1c3)
	_e1e934d5 = U8(0xe1e934d5)
	_ede0a8ca = U8(0xede0a8ca)
	_87438100 = U8(0x87438100)
	NpcLookAction = U8(0xa1b074dd)
	_5b6d5751 = U8(0x5b6d5751)
	PoseTrans = U8(0xfbb451bf)
	_65fd6b0d = U8(0x65fd6b0d)
	_2b6186a0 = U8(0x2b6186a0)
	_95798f28 = U8(0x95798f28)
	_2ae273e3 = String(0x2ae273e3) # size 48
	_fce7d916 = U8(0xfce7d916)
	_a84507aa = U8(0xa84507aa)
	_c033d95a = U8(0xc033d95a) # possible string size 1
	_ed32aade = U8(0xed32aade)
	WaitType = U8(0x9067bb0e) # size is 2, could this be an array?

class RadioCM(Row):
	SelectRate = Float(0x293ee089)
	_45ffea9a = U16(0x45ffea9a)
	MusicNo = U16(0x0f30a50e)
	UniqueID = U16(0x54706054)
	BeforeDays = U8(0x00244ce4)
	_806cfd72 = String(0x806cfd72) # size 128
	_627277e6 = U8(0x627277e6) # possible string size 1

class RadioJingle(Row):
	SelectRate = Float(0x293ee089)
	_fc7a1955 = Enum(0xfc7a1955, (
		('AllDay' , '一日中'),
		('Morning', '朝'),
		('Daytime', '昼'),
		('Night'  , '夜'),
	))
	_45ffea9a = U16(0x45ffea9a)
	MusicNo = U16(0x0f30a50e)
	UniqueID = U16(0x54706054)
	BeforeDays = U8(0x00244ce4)
	_806cfd72 = String(0x806cfd72) # size 129

class RecipeCraftParam(Row):
	_5f405bfb = U32(0x5f405bfb)
	_7f5b6179 = Enum(0x7f5b6179, (
		('Bamboo'     , 'はるのわかたけ'),
		('SakuraPetal', 'さくらのはなびら'),
		('Shell'      , 'なつのかいがら'),
		('Nut'        , 'どんぐり・まつぼっくり'),
		('Mushroom'   , 'きのこ'),
		('Maple'      , 'もみじ'),
		('XmasDeco'   , 'クリスマスオーナメント'),
		('SnowCrystal', 'ゆきのけっしょう'),
	))
	_478b74e4 = Enum(0x478b74e4, (
		('NoSelect'           , '指定無し'),
		('SelectRecipeSeason' , 'レシピ用季節'),
		('SelectCalendarEvent', 'カレンダーイベント'),
	))
	_34a742ad = Enum(0x34a742ad, (
		('None'                   , '※未設定'),
		('Shop'                   , 'お店'),
		('SeqRcoAlbeit'           , 'たぬきちアルバイト中'),
		('Sequence1'              , 'シーケンス専用1'),
		('Sza001'                 , 'しずえ1'),
		('Owl001'                 , 'フータ1'),
		('Slo001'                 , 'レイジ1'),
		('TV'                     , 'DIYテレビ番組'),
		('Sza002'                 , 'しずえ2(役場建設準備)'),
		('TownmakeLicenceLv5'     , '崖造成解禁時'),
		('NnpcHA000'              , '初期HA'),
		('NnpcAN000'              , '初期AN'),
		('DIYtutorial1'           , 'DIY体験会'),
		('DIYtutorial2'           , 'DIY体験会報酬'),
		('TrashRecipeTires'       , 'ゴミレシピ＜タイヤ＞'),
		('RcoDonationRewardA'     , 'たぬきち虫魚報酬A'),
		('Snowman'                , 'ゆきだるま'),
		('DIYbook1'               , 'DIYレシピブック1'),
		('DIYbook2'               , 'DIYレシピブック2'),
		('DIYbook3'               , 'DIYレシピブック3'),
		('DIYbookVariety'         , 'DIYレシピパーティグッズ'),
		('DIYbookFence1'          , 'DIYレシピ柵：木1'),
		('DIYbookFence2'          , 'DIYレシピ柵：木2'),
		('WoodBridge'             , 'まるたのはし(シーケンス)'),
		('CampSite'               , 'キャンプ場(シーケンス)'),
		('Ows01'                  , 'フーコ（星素材）'),
		('Ows02'                  , 'フーコ（12星座）'),
		('DIYbookNormalTools'     , 'DIYレシピいっぱし道具'),
		('DIYbookFence3'          , 'DIYレシピ柵：バラエティ'),
		('DIYbookFence4'          , 'DIYレシピ柵：鉄と石'),
		('SeasonSakura'           , '季節：桜の花びら'),
		('SeasonSpringBamboo'     , '季節：春のわかたけ'),
		('SeasonSummerShell'      , '季節：夏のかいがら'),
		('SeasonAutumnNuts'       , '季節：どんぐり'),
		('SeasonMomiji'           , '季節：紅葉の葉っぱ'),
		('SeasonChristmasOrnament', '季節：オーナメント'),
		('SeasonMushroom'         , '季節：きのこ'),
		('SeasonSnowCrystal'      , '季節：ゆきのけっしょう'),
		('RcoDonationRewardB'     , 'たぬきち虫魚報酬B'),
		('ImmigrationQuest'       , '移住クエスト'),
		('RemakeTutorial'         , 'リメイク体験'),
		('MileExchange'           , '＜マイル交換＞'),
		('Market'                 , '＜店売り＞'),
		('Inspire'                , '＜ひらめき＞'),
		('GoldTool'               , '＜金の道具＞'),
		('Broadcast'              , '＜島内放送＞'),
		('EasterPyn'              , 'イースター：ぴょんたろう会話'),
		('EasterNpc'              , 'イースター：アプローチ会話'),
		('EasterRand'             , 'イースター：風船・ボトル'),
		('EasterGround'           , 'イースター：ひらめき：じめん'),
		('EasterRock'             , 'イースター：ひらめき：いわ'),
		('EasterLeaf'             , 'イースター：ひらめき：はっぱ'),
		('EasterForest'           , 'イースター：ひらめき：もり'),
		('EasterSky'              , 'イースター：ひらめき：そらとぶ'),
		('EasterFish'             , 'イースター：ひらめき：サカナ'),
		('EasterCapHat'           , 'イースター：ひらめき：からコンプ'),
		('EasterTops'             , 'イースター：ひらめき：ふくコンプ'),
	))
	_cde5164f = Enum(0xcde5164f, (
		('BO'     , 'ぼんやり男'),
		('HA'     , 'ハキハキ男'),
		('KO'     , 'コワイ男'),
		('ZK'     , 'キザ男'),
		('FU'     , 'ふつう女'),
		('GE'     , 'ゲンキ女'),
		('OT'     , 'オトナ女'),
		('AN'     , 'アネキ女'),
		('ALL_NPC', 'NPC共通'),
		('NO_TAKE', '入手不可'),
	))
	_3711677b = U32(0x3711677b) # possible string size 4
	_13a65775 = U16(0x13a65775)
	_54062da5 = U16(0x54062da5)
	_69660415 = U16(0x69660415)
	_db46d805 = U16(0xdb46d805)
	_e626f1b5 = U16(0xe626f1b5)
	_a1868b65 = U16(0xa1868b65)
	Item = U16(0x89a3482c)
	_1bbfa75e = U16(0x1bbfa75e)
	_5c1fdd8e = U16(0x5c1fdd8e)
	_617ff43e = U16(0x617ff43e)
	_d35f282e = U16(0xd35f282e)
	_ee3f019e = U16(0xee3f019e)
	_a99f7b4e = U16(0xa99f7b4e)
	SerialID = S16(0x39dede36)
	UniqueID = U16(0x54706054)
	_33ddefc8 = String(0x33ddefc8) # size 66

class ReleaseVersionParam(Row):
	ReleaseKey = U16(0x76c190b2)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_977adfce = String(0x977adfce) # size 32

class RoomArchParam(Row):
	UniqueID = U16(0x54706054)
	_4b9c4229 = String(0x4b9c4229) # size 66

class RoomCeilingParam(Row):
	UniqueID = U16(0x54706054)
	_4b9c4229 = String(0x4b9c4229) # size 66

class RoomCurtainParam(Row):
	UniqueID = U16(0x54706054)
	_036e8ebe = String(0x036e8ebe) # size 64
	_4b9c4229 = String(0x4b9c4229) # size 66

class RoomCurtainTexParam(Row):
	UniqueID = U16(0x54706054)
	_036e8ebe = String(0x036e8ebe) # size 64
	_4b9c4229 = String(0x4b9c4229) # size 66

class RoomFloorParam(Row):
	_f74f3d2c = Enum(0xf74f3d2c, enum_f74f3d2c)
	Price = S32(0x718b024d)
	_49295020 = Enum(0x49295020, enum_b117eb21)
	_b117eb21 = Enum(0xb117eb21, enum_b117eb21)
	_ab771eae = U16(0xab771eae)
	ItemTableId = U16(0x58aff4fb)
	LandingUniqueID = U16(0x8fced711)
	UniqueID = U16(0x54706054)
	HasJmp = U8(0xa4db9685)
	Horizon = U8(0x3543c34a)
	_b8cc232c = String(0xb8cc232c) # size 64
	_4b9c4229 = String(0x4b9c4229) # size 64
	_05836619 = U8(0x05836619)
	_8ed948dd = U8(0x8ed948dd)

class RoomLandingParam(Row):
	_ab771eae = U16(0xab771eae)
	UniqueID = U16(0x54706054)
	_05038516 = String(0x05038516) # size 64
	_4b9c4229 = String(0x4b9c4229) # size 64

class RoomWallParam(Row):
	_8a377042 = Enum(0x8a377042, (
		('None' , 'なし'),
		('UseAO', 'あり'),
	))
	_f74f3d2c = Enum(0xf74f3d2c, enum_f74f3d2c)
	_85ed8743 = Enum(0x85ed8743, (
		('Orange', '白熱灯'),
		('White' , '蛍光灯'),
	))
	Price = S32(0x718b024d)
	ArchUniqueID = U16(0x499e42f9)
	_947875dd = U16(0x947875dd)
	_aa9bfc6e = U16(0xaa9bfc6e)
	CurtainUniqueID = U16(0xa0e569dc)
	ItemTableId = U16(0x58aff4fb)
	UniqueID = U16(0x54706054)
	WindowUniqueID = U16(0xe3a28616)
	_b8cc232c = String(0xb8cc232c) # size 64
	_4b9c4229 = String(0x4b9c4229) # size 64
	_05836619 = U8(0x05836619)
	TextureWindow = U8(0x318ebbf2)

class RoomWindowParam(Row):
	_c90ab4c4 = Enum(0xc90ab4c4, (
		('None'       , '無し'),
		('SquareCross', 'SquareCross'),
		('SquareHang' , 'SquareHang'),
		('Arch'       , 'Arch'),
		('Circle'     , 'Circle'),
	))
	_cbc01f0d = Enum(0xcbc01f0d, (
		('None'  , '無し'),
		('Square', '四角'),
		('Circle', '丸'),
		('Arch'  , 'アーチ'),
	))
	UniqueID = U16(0x54706054)
	_4b9c4229 = String(0x4b9c4229) # size 64
	WindowName = String(0x9b0b7ce4) # string64

class SeasonCalendar(Row):
	_4875e383 = U8(0x4875e383)
	_ea066cc1 = U8(0xea066cc1)
	_8b21a26b = U8(0x8b21a26b)
	_29522d29 = U8(0x29522d29)
	Day = U8(0xd5692bff)
	_61501334 = U8(0x61501334)
	_c3239c76 = U8(0xc3239c76)
	Month = U8(0x287db05d)
	_66b4a4c1 = U8(0x66b4a4c1)
	_c4c72b83 = U8(0xc4c72b83)
	_b5a8fc2e = U8(0xb5a8fc2e)
	_17db736c = U8(0x17db736c)
	_185d9096 = U8(0x185d9096)
	_ba2e1fd4 = U8(0xba2e1fd4)
	_5b8be707 = U8(0x5b8be707)
	_f9f86845 = U8(0xf9f86845)
	_80e1de38 = U8(0x80e1de38)
	_2292517a = U8(0x2292517a)
	_a155bc19 = U8(0xa155bc19)
	_0326335b = U8(0x0326335b)

class ShopItemRouteFlags(Row):
	FlagLand = S32(0x3fe43170)
	FlagPlayer = S32(0x4171a41d)
	_d3d4284e = Enum(0xd3d4284e, (
		('Shop'  , 'お店'),
		('Label1', 'タヌポート'),
	))
	AttrCollectBit = U8(0x74b2eb78)
	ItemFrom = String(0x46e66708) # string32

class SoundAmbientPlacementParam(Row):
	UniqueID = U16(0x54706054)
	_85cf1615 = String(0x85cf1615) # size 130

class SoundAttributeForGround(Row):
	_5e7a33b5 = U16(0x5e7a33b5)
	UniqueID = U16(0x54706054)

class SoundAttributeForPlacement(Row):
	_5e7a33b5 = U16(0x5e7a33b5)
	UniqueID = U16(0x54706054)

class SoundAudioMusic(Row):
	AudioMusicID = S16(0xd4892d19)
	_3637ebb9 = U16(0x3637ebb9)
	UniqueID = U16(0x54706054)
	_32bc8d59 = U8(0x32bc8d59) # possible string size 1
	Label = String(0x87bf00e8) # string32

class SoundInstruments(Row):
	_64bc65e7 = Enum(0x64bc65e7, (
		('Normal'   , '通常楽器'),
		('Drum'     , '打楽器'),
		('DrumSet'  , 'ドラムセット'),
		('FourHands', '連弾楽器'),
	))
	_3637ebb9 = U16(0x3637ebb9)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	_85cf1615 = String(0x85cf1615) # size 128

class SoundMaterialType(Row):
	SoundAttribute = U16(0x2e17a0a7)
	UniqueID = U16(0x54706054)
	DebugName = String(0xab51a3cf) # string32

class SpNpcParam(Row):
	_dda5d566 = Enum(0xdda5d566, enum_TwoGenders)
	_86ad0ce1 = Enum(0x86ad0ce1, enum_TwoGenders)
	PacketId = S32(0x3ce2e8d8)
	Social = U32(0x23e7c2a0)
	NpcSpClothSet = U16(0x9611c929)
	PosterItemID = S16(0x0f640691)
	Smartphone = U16(0x3f858678)
	Umbrella = U16(0xbb9c816e)
	UniqueID = U16(0x54706054)
	_919ea52a = U8(0x919ea52a)
	BirthMonth = U8(0x9456b6a3)
	_4ce98793 = String(0x4ce98793) # size 64
	_2f1b930d = String(0x2f1b930d) # size 8
	_07d60b3d = U8(0x07d60b3d)
	NpcColor = U8(0x41977699)
	_48ef0398 = String(0x48ef0398) # size 64
	SpecialELink = U8(0x04ac1bea)
	SpecialSLink = U8(0xbe782346)
	_21c5bbd6 = U8(0x21c5bbd6)
	_e52f0037 = U8(0xe52f0037)
	_42f255d5 = U8(0x42f255d5)
	_e7534ab5 = U8(0xe7534ab5)
	_9d1d8e45 = U32(0x9d1d8e45)

class StructureBridgeParam(Row):
	_74be6041 = Enum(0x74be6041, (
		('03'         , '橋03'),
		('04'         , '橋04'),
		('05'         , '橋05'),
		('Diagonal025', '斜め橋025'),
		('Diagonal030', '斜め橋030'),
		('Diagonal035', '斜め橋035'),
	))
	BridgeTypeUniqueID = U16(0xee9ce68d)
	UniqueID = U16(0x54706054)
	ModelName = String(0x39b5a93d) # string32

class StructureBridgeTypeParam(Row):
	_904611f3 = U32(0x904611f3)
	ItemNameUniqueID = U16(0xc33a894e)
	UniqueID = U16(0x54706054)
	BridgeTypeName = String(0x68cf5938) # string32
	_5c28c4db = String(0x5c28c4db) # size 32

class StructureDoorParam(Row):
	_e7e1c6cd = U32(0xe7e1c6cd)
	_b6f6977b = U32(0xb6f6977b) # possible string size 4
	_a1def3bb = U32(0xa1def3bb) # possible string size 4
	_98a65efb = U32(0x98a65efb) # possible string size 4
	_f0c9a20d = U32(0xf0c9a20d)
	_c9b10f4d = U32(0xc9b10f4d)
	_de996b8d = U32(0xde996b8d)
	_bb4055cd = U32(0xbb4055cd)
	_ac68310d = U32(0xac68310d)
	_95109c4d = U32(0x95109c4d) # possible string size 4
	_8238f88d = U32(0x8238f88d)
	_5ea2e0cd = U32(0x5ea2e0cd)
	_498a840d = U32(0x498a840d) # possible string size 4
	UniqueID = U16(0x54706054)
	_977adfce = String(0x977adfce) # size 32
	_bd37bfd7 = String(0xbd37bfd7) # size 32
	_52f5d4e9 = String(0x52f5d4e9) # size 32
	_12a20792 = String(0x12a20792) # size 32
	_fd606cac = String(0xfd606cac) # size 32
	_1657d7af = String(0x1657d7af) # size 32
	_b9c26fea = String(0xb9c26fea) # size 32
	_560004d4 = String(0x560004d4) # size 32
	_b4dc1fad = String(0xb4dc1fad) # size 32
	_5b1e7493 = String(0x5b1e7493) # size 32
	_b029cf90 = String(0xb029cf90) # size 32
	_5feba4ae = String(0x5feba4ae) # size 32
	_aee0ff23 = String(0xaee0ff23) # size 32
	_4122941d = String(0x4122941d) # size 34

class StructureFacilityModel(Row):
	_88ff5893 = U32(0x88ff5893)
	_85a0fa49 = U32(0x85a0fa49)
	_dd9617a2 = Enum(0xdd9617a2, (
		('A', 'タイプA'),
	))
	FloorHeight = Float(0x6efc082c)
	_0d664b5c = U16(0x0d664b5c)
	DoorMaterial = U16(0x42bdd56f)
	_9c2d6dc6 = U16(0x9c2d6dc6)
	RoofMaterial = U16(0x83b54e59)
	_00c1577d = U16(0x00c1577d)
	UniqueID = U16(0x54706054)
	Construction = U8(0x9c8a400b)
	GrowLevel = U8(0x35ac1bb4)
	_23e16936 = U8(0x23e16936)
	HasEigyoLight = U8(0x43d8a434)
	_42e82ded = U8(0x42e82ded)
	IsUseXlink = U8(0x09d75f40)
	ModelName = String(0x39b5a93d) # string32
	_397b2b54 = U8(0x397b2b54)
	UseMyDesign = U8(0x89be1d8f)

class StructureHouseDoorParam(Row):
	_b619ba5c = U32(0xb619ba5c)
	_712c43a7 = Enum(0x712c43a7, (
		('Invalid'   , '検討中'),
		('Knob'      , 'ノブ（回転なし）'),
		('KnobRotate', 'ノブ（回転あり）'),
		('PlayerTent', 'プレイヤテント'),
		('NpcTent'   , 'NPCテント'),
	))
	_0aa76edd = Enum(0x0aa76edd, (
		('Square', '四角い'),
		('Round' , '丸い'),
	))
	_37d4e515 = U16(0x37d4e515)
	Material = U16(0x39cb9646)
	UniqueID = U16(0x54706054)
	_c93db65a = U8(0xc93db65a)
	Dummy = U8(0xf75ddf51)
	HasDoorWindow = U8(0xf489f3c5)
	_960a51fe = U8(0x960a51fe)
	ModelName = String(0x39b5a93d) # string32

class StructureHouseRoofParam(Row):
	_a9424a50 = Enum(0xa9424a50, (
		('Invalid'  , '未使用'),
		('Red'      , '赤'),
		('Pink'     , 'ピンク'),
		('Yellow'   , '黄'),
		('Purple'   , '紫'),
		('Green'    , '緑'),
		('Blue'     , '青'),
		('LightBlue', '水色'),
		('Black'    , '黒'),
	))
	_37d4e515 = U16(0x37d4e515)
	_b6f501d2 = U16(0xb6f501d2)
	Material = U16(0x39cb9646)
	UniqueID = U16(0x54706054)
	Dummy = U8(0xf75ddf51)
	ModelName = String(0x39b5a93d) # string32

class StructureHouseShapeParam(Row):
	_10dbd8bb = Enum(0x10dbd8bb, (
		('Invalid', '無効値'),
		('Tent'   , 'テント'),
		('Level00', '成長段階00'),
		('Level01', '成長段階01'),
		('Level02', '成長段階02'),
		('Level03', '成長段階03'),
		('Level04', '成長段階04'),
	))
	_c86e60d5 = U16(0xc86e60d5)
	_0966fbe3 = U16(0x0966fbe3)
	_d8727d7d = U16(0xd8727d7d)
	_e6fc6624 = U16(0xe6fc6624)
	UniqueID = U16(0x54706054)
	_e3a73129 = String(0xe3a73129) # size 32
	_977adfce = String(0x977adfce) # size 34

class StructureHouseWallParam(Row):
	_60680c93 = Enum(0x60680c93, (
		('Normal', '通常の家'),
		('Tent'  , 'テント'),
		('None'  , 'なし'),
	))
	_37d4e515 = U16(0x37d4e515)
	_9c2d6dc6 = U16(0x9c2d6dc6)
	_b6f501d2 = U16(0xb6f501d2)
	UniqueID = U16(0x54706054)
	LightParamName = String(0xd2c59675) # string32
	ModelName = String(0x39b5a93d) # string32
	UseCurtain = U8(0x9e19c94c)
	UseExteriorLight = U8(0x0424930f) # size is 3, could this be an array?

class StructureInfoParam(Row):
	_1ff4093d = Enum(0x1ff4093d, (
		('Player', 'Player'),
		('Npc'   , 'Npc'),
	))
	_c01e47a7 = Enum(0xc01e47a7, enum_d6704d8b)
	_fec3548b = U32(0xfec3548b)
	_cc24374e = Enum(0xcc24374e, (
		('Player'     , 'プレイヤ家'),
		('Npc'        , 'NPC家'),
		('PhotoStudio', '撮影スタジオ'),
	))
	_d6704d8b = Enum(0xd6704d8b, enum_d6704d8b)
	_0d664b5c = U16(0x0d664b5c)
	UniqueID = U16(0x54706054)

class StructureSlopeParam(Row):
	ItemNameUniqueID = U16(0xc33a894e)
	UniqueID = U16(0x54706054)
	_08462f85 = String(0x08462f85) # size 32
	ModelName = String(0x39b5a93d) # string32

class TVProgram(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	_01481890 = U8(0x01481890)
	_43513d44 = U8(0x43513d44)
	_51e492aa = U8(0x51e492aa)
	_e958f5cf = U8(0xe958f5cf)
	_748fcd76 = U8(0x748fcd76)
	_cc33aa13 = U8(0xcc33aa13)
	_de8605fd = U8(0xde8605fd)
	_db216e77 = U8(0xdb216e77)
	_c994c199 = U8(0xc994c199)
	_7128a6fc = U8(0x7128a6fc)
	_ecff9e45 = U8(0xecff9e45)
	_5443f920 = U8(0x5443f920)
	_46f656ce = U8(0x46f656ce)
	_6a34f3f2 = U8(0x6a34f3f2)
	_78815c1c = U8(0x78815c1c)
	_c03d3b79 = U8(0xc03d3b79)
	_5dea03c0 = U8(0x5dea03c0)
	_e55664a5 = U8(0xe55664a5)
	_f7e3cb4b = U8(0xf7e3cb4b)
	_f244a0c1 = U8(0xf244a0c1)
	_e0f10f2f = U8(0xe0f10f2f)
	_584d684a = U8(0x584d684a)
	_c59a50f3 = U8(0xc59a50f3)
	_7d263796 = U8(0x7d263796)
	_6f939878 = U8(0x6f939878)
	ResourceName = String(0xa88f23cf) # string33
	_7834d5db = String(0x7834d5db) # size 33
	_93036ed8 = String(0x93036ed8) # size 33
	_7cc105e6 = String(0x7cc105e6) # size 33
	_9e1d1e9f = String(0x9e1d1e9f) # size 33
	_71df75a1 = String(0x71df75a1) # size 33
	_9ae8cea2 = String(0x9ae8cea2) # size 33
	_13b9f45c = U8(0x13b9f45c)
	_010c5bb2 = U8(0x010c5bb2)
	_b9b03cd7 = U8(0xb9b03cd7)
	_2467046e = U8(0x2467046e)
	_9cdb630b = U8(0x9cdb630b)
	_8e6ecce5 = U8(0x8e6ecce5)
	_8bc9a76f = U8(0x8bc9a76f)
	_997c0881 = U8(0x997c0881)
	_21c06fe4 = U8(0x21c06fe4)
	_bc17575d = U8(0xbc17575d)
	_04ab3038 = U8(0x04ab3038)
	_161e9fd6 = U8(0x161e9fd6)
	_878cd782 = U8(0x878cd782)
	_9539786c = U8(0x9539786c)
	_2d851f09 = U8(0x2d851f09)
	_b05227b0 = U8(0xb05227b0)
	_08ee40d5 = U8(0x08ee40d5)
	_1a5bef3b = U8(0x1a5bef3b)
	_1ffc84b1 = U8(0x1ffc84b1)
	_0d492b5f = U8(0x0d492b5f)
	_b5f54c3a = U8(0xb5f54c3a)
	_28227483 = U8(0x28227483)
	_909e13e6 = U8(0x909e13e6)
	_822bbc08 = U8(0x822bbc08)

class TVProgramFriday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramMonday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramSaturday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramSunday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramThursday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramTuesday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramWednesday(Row):
	_a988063c = Enum(0xa988063c, enum_a988063c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class VMMultistepNPC(Row):
	UniqueID = U16(0x54706054)
	_091b46f5 = String(0x091b46f5) # size 130

class WeatherPatternParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

lookup = {
	'AITag.bcsv': AITag,
	'AmiiboData.bcsv': AmiiboData,
	'BgmPropertyControlParam.bcsv': BgmPropertyControlParam,
	'BgmPropertyParam.bcsv': BgmPropertyParam,
	'CalendarEventCountryParam.bcsv': CalendarEventCountryParam,
	'CalendarEventJuneBrideExchange.bcsv': CalendarEventJuneBrideExchange,
	'CalendarEventJuneBrideReward.bcsv': CalendarEventJuneBrideReward,
	'CalendarEventParam.bcsv': CalendarEventParam,
	'CalendarEventRegionParam.bcsv': CalendarEventRegionParam,
	'CharaMakeCheekTypeParam.bcsv': CharaMakeCheekTypeParam,
	'CharaMakeEyeColorParam.bcsv': CharaMakeEyeColorParam,
	'CharaMakeEyeTypeParam.bcsv': CharaMakeEyeTypeParam,
	'CharaMakeHairColorParam.bcsv': CharaMakeHairColorParam,
	'CharaMakeHairStyleParam.bcsv': CharaMakeHairStyleParam,
	'CharaMakeMouthTypeParam.bcsv': CharaMakeMouthTypeParam,
	'CharaMakeNoseTypeParam.bcsv': CharaMakeNoseTypeParam,
	'CharaMakeSkinColorParam.bcsv': CharaMakeSkinColorParam,
	'ColEffectAttributeParam.bcsv': ColEffectAttributeParam,
	'ColGroundAttributeParam.bcsv': ColGroundAttributeParam,
	'ColSoundAttributeParam.bcsv': ColSoundAttributeParam,
	'DuckingParam.bcsv': DuckingParam,
	'EventFlagsAocParam.bcsv': EventFlagsAocParam,
	'EventFlagsBcatParam.bcsv': EventFlagsBcatParam,
	'EventFlagsHouseParam.bcsv': EventFlagsHouseParam,
	'EventFlagsLandParam.bcsv': EventFlagsLandParam,
	'EventFlagsLandTempParam.bcsv': EventFlagsLandTempParam,
	'EventFlagsLifeSupportAchievementParam.bcsv': EventFlagsLifeSupportAchievementParam,
	'EventFlagsLifeSupportDailyParam.bcsv': EventFlagsLifeSupportDailyParam,
	'EventFlagsNpcMemoryParam.bcsv': EventFlagsNpcMemoryParam,
	'EventFlagsNpcSaveParam.bcsv': EventFlagsNpcSaveParam,
	'EventFlagsNpcTempParam.bcsv': EventFlagsNpcTempParam,
	'EventFlagsPlayerActivityParam.bcsv': EventFlagsPlayerActivityParam,
	'EventFlagsPlayerParam.bcsv': EventFlagsPlayerParam,
	'EventFlagsPlayerTempParam.bcsv': EventFlagsPlayerTempParam,
	'EventFlagsPlayerVisitParam.bcsv': EventFlagsPlayerVisitParam,
	'EventPlazaFtrParam.bcsv': EventPlazaFtrParam,
	'EventPlazaGround.bcsv': EventPlazaGround,
	'EventPlazaObjModelParam.bcsv': EventPlazaObjModelParam,
	'EventPlazaPlacementParam.bcsv': EventPlazaPlacementParam,
	'FgFlowerHeredity.bcsv': FgFlowerHeredity,
	'FgMainParam.bcsv': FgMainParam,
	'FieldCreateParam.bcsv': FieldCreateParam,
	'FieldDistantViewParam.bcsv': FieldDistantViewParam,
	'FieldLandMakingActionParam.bcsv': FieldLandMakingActionParam,
	'FieldLandMakingError.bcsv': FieldLandMakingError,
	'FieldLandMakingRoadKindParam.bcsv': FieldLandMakingRoadKindParam,
	'FieldLandMakingUnitModelParam.bcsv': FieldLandMakingUnitModelParam,
	'FieldMainFieldParam.bcsv': FieldMainFieldParam,
	'FieldOutsideParts.bcsv': FieldOutsideParts,
	'FieldOutsideTemplate.bcsv': FieldOutsideTemplate,
	'FishAppearRiverParam.bcsv': FishAppearRiverParam,
	'FishAppearSeaParam.bcsv': FishAppearSeaParam,
	'FishBeyQuestParam.bcsv': FishBeyQuestParam,
	'FishStatusParam.bcsv': FishStatusParam,
	'GmoFootprintParam.bcsv': GmoFootprintParam,
	'HumanAnimParam.bcsv': HumanAnimParam,
	'IndoorIdrParam.bcsv': IndoorIdrParam,
	'IndoorPhotoStudioItemParam.bcsv': IndoorPhotoStudioItemParam,
	'InsectAppearParam.bcsv': InsectAppearParam,
	'InsectBattleParam.bcsv': InsectBattleParam,
	'InsectStatusParam.bcsv': InsectStatusParam,
	'ItemAct.bcsv': ItemAct,
	'ItemClothGroup.bcsv': ItemClothGroup,
	'ItemColor.bcsv': ItemColor,
	'ItemFilter.bcsv': ItemFilter,
	'ItemFrom.bcsv': ItemFrom,
	'ItemKind.bcsv': ItemKind,
	'ItemMailAttachCategoryGroup.bcsv': ItemMailAttachCategoryGroup,
	'ItemMenuIcon.bcsv': ItemMenuIcon,
	'ItemNpcFtrActionParam.bcsv': ItemNpcFtrActionParam,
	'ItemNpcOutfitInfo.bcsv': ItemNpcOutfitInfo,
	'ItemNpcRoomReplaceCategory.bcsv': ItemNpcRoomReplaceCategory,
	'ItemNpcTopsForm.bcsv': ItemNpcTopsForm,
	'ItemOutfitCategory.bcsv': ItemOutfitCategory,
	'ItemOutfitInfo.bcsv': ItemOutfitInfo,
	'ItemParam.bcsv': ItemParam,
	'ItemPlayerInitialOutfitBoyAWParam.bcsv': ItemPlayerInitialOutfitBoyAWParam,
	'ItemPlayerInitialOutfitBoySSParam.bcsv': ItemPlayerInitialOutfitBoySSParam,
	'ItemPlayerInitialOutfitGirlAWParam.bcsv': ItemPlayerInitialOutfitGirlAWParam,
	'ItemPlayerInitialOutfitGirlSSParam.bcsv': ItemPlayerInitialOutfitGirlSSParam,
	'ItemPlayerTopsForm.bcsv': ItemPlayerTopsForm,
	'ItemRemake.bcsv': ItemRemake,
	'ItemRemakeCommonPattern.bcsv': ItemRemakeCommonPattern,
	'ItemRemakeCommonPatternCategory.bcsv': ItemRemakeCommonPatternCategory,
	'ItemSeasonalityParam.bcsv': ItemSeasonalityParam,
	'ItemShareTexture.bcsv': ItemShareTexture,
	'ItemSize.bcsv': ItemSize,
	'ItemStrSort.bcsv': ItemStrSort,
	'ItemUIContextMenu.bcsv': ItemUIContextMenu,
	'ItemUnitIcon.bcsv': ItemUnitIcon,
	'JuneBrideWallFloor.bcsv': JuneBrideWallFloor,
	'LocalizeNameConvertParam.bcsv': LocalizeNameConvertParam,
	'MannequinCoodinate.bcsv': MannequinCoodinate,
	'MaterialType.bcsv': MaterialType,
	'MessageCardBoardDesignParam.bcsv': MessageCardBoardDesignParam,
	'MessageCardColorParam.bcsv': MessageCardColorParam,
	'MessageCardDesignParam.bcsv': MessageCardDesignParam,
	'MessageCardSelectDesign.bcsv': MessageCardSelectDesign,
	'MessageCardSelectDesignSp.bcsv': MessageCardSelectDesignSp,
	'MessageCardSelectPresent.bcsv': MessageCardSelectPresent,
	'MessageCardSelectPresentSp.bcsv': MessageCardSelectPresentSp,
	'MuseumArtDonateInfo.bcsv': MuseumArtDonateInfo,
	'MuseumFossilDonateInfo.bcsv': MuseumFossilDonateInfo,
	'MuseumNPCLayoutInfo.bcsv': MuseumNPCLayoutInfo,
	'MuseumNPCSilhouette.bcsv': MuseumNPCSilhouette,
	'MuseumNPCSpotTalk.bcsv': MuseumNPCSpotTalk,
	'MuseumNameboardInfo.bcsv': MuseumNameboardInfo,
	'MuseumStampRackInfo.bcsv': MuseumStampRackInfo,
	'MuseumWatchPoint.bcsv': MuseumWatchPoint,
	'MysteryTourFieldParam.bcsv': MysteryTourFieldParam,
	'MysteryTourFishParam.bcsv': MysteryTourFishParam,
	'MysteryTourInsectParam.bcsv': MysteryTourInsectParam,
	'MysteryTourItemParam.bcsv': MysteryTourItemParam,
	'MysteryTourParam.bcsv': MysteryTourParam,
	'NmlNpcParam.bcsv': NmlNpcParam,
	'NmlNpcRaceParam.bcsv': NmlNpcRaceParam,
	'NpcCastLabelData.bcsv': NpcCastLabelData,
	'NpcCastScheduleData.bcsv': NpcCastScheduleData,
	'NpcEquipRule.bcsv': NpcEquipRule,
	'NpcInterest.bcsv': NpcInterest,
	'NpcLife.bcsv': NpcLife,
	'NpcLooksParam.bcsv': NpcLooksParam,
	'NpcMoveRoomTemplate.bcsv': NpcMoveRoomTemplate,
	'NpcMsgBullfestParam.bcsv': NpcMsgBullfestParam,
	'NpcRoomTemplate.bcsv': NpcRoomTemplate,
	'NpcSpClothSetParam.bcsv': NpcSpClothSetParam,
	'NpcSpModelScale.bcsv': NpcSpModelScale,
	'NpcSpServiceMotionRandom.bcsv': NpcSpServiceMotionRandom,
	'NpcSpServiceMotionWork.bcsv': NpcSpServiceMotionWork,
	'NpcSpServiceMotionWorkSp.bcsv': NpcSpServiceMotionWorkSp,
	'PlayerStateParam.bcsv': PlayerStateParam,
	'RadioCM.bcsv': RadioCM,
	'RadioJingle.bcsv': RadioJingle,
	'RecipeCraftParam.bcsv': RecipeCraftParam,
	'ReleaseVersionParam.bcsv': ReleaseVersionParam,
	'RoomArchParam.bcsv': RoomArchParam,
	'RoomCeilingParam.bcsv': RoomCeilingParam,
	'RoomCurtainParam.bcsv': RoomCurtainParam,
	'RoomCurtainTexParam.bcsv': RoomCurtainTexParam,
	'RoomFloorParam.bcsv': RoomFloorParam,
	'RoomLandingParam.bcsv': RoomLandingParam,
	'RoomWallParam.bcsv': RoomWallParam,
	'RoomWindowParam.bcsv': RoomWindowParam,
	'SeasonCalendar.bcsv': SeasonCalendar,
	'ShopItemRouteFlags.bcsv': ShopItemRouteFlags,
	'SoundAmbientPlacementParam.bcsv': SoundAmbientPlacementParam,
	'SoundAttributeForGround.bcsv': SoundAttributeForGround,
	'SoundAttributeForPlacement.bcsv': SoundAttributeForPlacement,
	'SoundAudioMusic.bcsv': SoundAudioMusic,
	'SoundInstruments.bcsv': SoundInstruments,
	'SoundMaterialType.bcsv': SoundMaterialType,
	'SpNpcParam.bcsv': SpNpcParam,
	'StructureBridgeParam.bcsv': StructureBridgeParam,
	'StructureBridgeTypeParam.bcsv': StructureBridgeTypeParam,
	'StructureDoorParam.bcsv': StructureDoorParam,
	'StructureFacilityModel.bcsv': StructureFacilityModel,
	'StructureHouseDoorParam.bcsv': StructureHouseDoorParam,
	'StructureHouseRoofParam.bcsv': StructureHouseRoofParam,
	'StructureHouseShapeParam.bcsv': StructureHouseShapeParam,
	'StructureHouseWallParam.bcsv': StructureHouseWallParam,
	'StructureInfoParam.bcsv': StructureInfoParam,
	'StructureSlopeParam.bcsv': StructureSlopeParam,
	'TVProgram.bcsv': TVProgram,
	'TVProgramFriday.bcsv': TVProgramFriday,
	'TVProgramMonday.bcsv': TVProgramMonday,
	'TVProgramSaturday.bcsv': TVProgramSaturday,
	'TVProgramSunday.bcsv': TVProgramSunday,
	'TVProgramThursday.bcsv': TVProgramThursday,
	'TVProgramTuesday.bcsv': TVProgramTuesday,
	'TVProgramWednesday.bcsv': TVProgramWednesday,
	'VMMultistepNPC.bcsv': VMMultistepNPC,
	'WeatherPatternParam.bcsv': WeatherPatternParam,
}
