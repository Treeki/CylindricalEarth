struct s_0244bd71 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveEventFlagPlayer {                       /* 0x1000 big, align 2 */
  s_eb93f5a5                         Flags;                                     // @0x0 size 0x1000, align 2
};
struct GSavePlayerOther {                           /* 0x37890 big, align 16 */
  s_7b602b39                         _d35a9251;                                 // @0x0 size 0x10, align 16
  GSavePlayerItemBaggage             ItemBaggage;                               // @0x10 size 0x17c, align 4
  GSavePlayerItemChest               ItemChest;                                 // @0x18c size 0x9c44, align 4
  GSavePlayerItemInsectFishBox       ItemInsectFishBox;                         // @0x9dd0 size 0x148, align 4
  GSavePlayerItemMaterial            ItemMaterial;                              // @0x9f18 size 0x140, align 4
  GSaveItemCollectBit                ItemCollectBit;                            // @0xa058 size 0x754, align 4
  GSaveItemRemakeCollectBit          ItemRemakeCollectBit;                      // @0xa7ac size 0x7d0, align 4
  GSavePlayerManpu                   Manpu;                                     // @0xaf7c size 0x88, align 1
  u8 gap_b004[4];
  GSaveMailUserInfo                  MailUserInfo;                              // @0xb008 size 0x13418, align 8
  GSaveDate                          _b58743fe;                                 // @0x1e420 size 0x4, align 2
  GSaveDate                          _a4e58b58;                                 // @0x1e424 size 0x4, align 2
  GSavePostingReserveList            PostingReserveList;                        // @0x1e428 size 0xabd0, align 4
  s_ac6c2327                         _69144a57;                                 // @0x28ff8 size 0x8c, align 4
  s_75f0022c                         _f209c449;                                 // @0x29084 size 0x10, align 4
  u8 gap_29094[4];
  GSaveFriendList                    FriendList;                                // @0x29098 size 0xb548, align 8
  GSaveSetting                       Setting;                                   // @0x345e0 size 0x1, align 1
  u8 gap_345e1[3];
  GSaveMoney                         Savings;                                   // @0x345e4 size 0x8, align 4
  GSaveMoney                         BoxSell;                                   // @0x345ec size 0x8, align 4
  GSaveCraftingRecipeCollect         CraftingRecipeCollect;                     // @0x345f4 size 0x1400, align 2
  GSaveDate                          MoveOutBoxMoney;                           // @0x359f4 size 0x4, align 2
  GSaveNetPlayerID                   NetPlayerID;                               // @0x359f8 size 0x58, align 8
  GSaveNetMailBox                    NetMailBox;                                // @0x35a50 size 0x660, align 8
  GSavePlayerVisitorNpc              VisitorInfo;                               // @0x360b0 size 0x90, align 8
  GSaveAudioRegister                 AudioRegister;                             // @0x36140 size 0x20, align 4
  s_79d059af                         RegionLanguageID;                          // @0x36160 size 0x4, align 4
  u8 gap_36164[4];
  GSavePersonalPlayReportInfo        PlayReportInfo;                            // @0x36168 size 0xd10, align 8
  GSaveFishCollection                FishCollection;                            // @0x36e78 size 0xd6, align 2
  GSaveInsectCollection              InsectCollection;                          // @0x36f4e size 0xd6, align 2
  GSaveDiveFishCollection            DiveFishCollection;                        // @0x37024 size 0x82, align 2
  u8 gap_370a6[2];
  s_2c3a15dc                         ReceivedAoC;                               // @0x370a8 size 0x104, align 4
  s_b16331d2                         ReceivedBCAT;                              // @0x371ac size 0x204, align 4
  GSaveMoney                         KabuBuy;                                   // @0x373b0 size 0x8, align 4
  GSaveMoney                         KabuSell;                                  // @0x373b8 size 0x8, align 4
  GSaveLandId                        PreviousLandId;                            // @0x373c0 size 0x1c, align 4
  GSaveAmiibo                        Amiibo;                                    // @0x373dc size 0xa0, align 4
  GSaveRemakeCommonPattern           RemakeCommonPattern;                       // @0x3747c size 0x10, align 1
  GSaveMoney                         BoxTransfer;                               // @0x3748c size 0x8, align 4
  u32                                _075e237a;                                 // @0x37494 size 0x4, align 4
  GSaveClockTimeList                 ClockTimeList;                             // @0x37498 size 0x180, align 1
  GSaveHashList                      HashList;                                  // @0x37618 size 0x40, align 4
  GSaveEventFlagPlayerTemp           EventFlagPlayerTemp;                       // @0x37658 size 0x100, align 2
  GSaveEventFlagPlayerVisit          EventFlagPlayerVisit;                      // @0x37758 size 0x100, align 2
  nn::util::Uuid                     DeviceId;                                  // @0x37858 size 0x10, align 1
  GSaveMailUserLog                   MailUserLog;                               // @0x37868 size 0x14, align 2
  GSaveDate                          _bbfb1a0c;                                 // @0x3787c size 0x4, align 2
  GSaveMoney                         FoxTotalBuy;                               // @0x37880 size 0x8, align 4
};
struct GSaveNormalNpcBitFlag {                      /* 0x8c big, align 4 */
  u32                                NormalNpcBitFlag[35];                      // @0x0 size 0x4, align 4
};
struct GSaveMyDesignPalette {                       /* 0x2d big, align 1 */
  u8                                 Colors[45];                                // @0x0 size 0x1, align 1
};
struct GSavePostingReserveMilage {                  /* 0x10 big, align 4 */
  bool                               Reserved;                                  // @0x0 size 0x1, align 1
  u8 gap_1[3];
  GSaveItemName                      Present;                                   // @0x4 size 0x8, align 4
  GSaveDate                          Date;                                      // @0xc size 0x4, align 2
};
struct GSaveDiveFishCollection {                    /* 0x82 big, align 2 */
  GSaveFirstCollection               DiveFish[60];                              // @0x0 size 0x2, align 2
  _14a85dac                          NewDiveFishFlag;                           // @0x78 size 0x8, align 1
  u8                                 Count;                                     // @0x80 size 0x1, align 1
};
struct GSavePlayerBaseId {                          /* 0x1c big, align 4 */
  u32                                Id;                                        // @0x0 size 0x4, align 4
  GSaveWordPlayerName                Name;                                      // @0x4 size 0x14, align 2
  s_88f8f5b0                         Gender;                                    // @0x18 size 0x4, align 4
};
struct GSavePostingReserveCommune {                 /* 0x2b8 big, align 4 */
  GSavePostingReserveBase            ReserveBase;                               // @0x0 size 0x2b0, align 4
  u8                                 ReserveType;                               // @0x2b0 size 0x1, align 1
  u8                                 FromType;                                  // @0x2b1 size 0x1, align 1
  Game::NpcNormalID                  FromNpcId;                                 // @0x2b2 size 0x3, align 1
  u8                                 FromSystemId;                              // @0x2b5 size 0x1, align 1
};
struct s_12731d40 {                                 /* 0x140 big, align 4 */
  u32                                Counter[80];                               // @0x0 size 0x4, align 4
};
struct GSaveMyDesignHeader {                        /* 0x70 big, align 8 */
  _eddfb1d6                          NetMyDesignID;                             // @0x0 size 0x8, align 8
  s_20b7a807                         Title;                                     // @0x8 size 0x28, align 2
  GSavePlayerId                      Author;                                    // @0x30 size 0x38, align 4
  u8                                 Flags;                                     // @0x68 size 0x1, align 1
  u8                                 ColorSet;                                  // @0x69 size 0x1, align 1
  u16                                HomePlace;                                 // @0x6a size 0x2, align 2
};
struct GSaveFriendData {                            /* 0x70 big, align 8 */
  _a8d2a4d4                          POPID;                                     // @0x0 size 0x8, align 8
  _010a9a24                          NSAID;                                     // @0x8 size 0x8, align 8
  GSavePlayerId                      PlayerId;                                  // @0x10 size 0x38, align 4
  GSaveTime                          UpdateTime;                                // @0x48 size 0x8, align 2
  GSaveTime                          SendTime;                                  // @0x50 size 0x8, align 2
  u32                                SendMailCountTotal;                        // @0x58 size 0x4, align 4
  u32                                SendGiftCountTotal;                        // @0x5c size 0x4, align 4
  Game::CharaMakeSetting             CharaMakeSetting;                          // @0x60 size 0xc, align 2
  u8                                 SendMailCountToday;                        // @0x6c size 0x1, align 1
  u8                                 SendGiftCountToday;                        // @0x6d size 0x1, align 1
  _44c6787c                          Status;                                    // @0x6e size 0x1, align 1
};
struct GSaveWordCoordinateName {                    /* 0x60 big, align 2 */
  s_1fc7814b                         CoordinateName;                            // @0x0 size 0x60, align 2
};
struct GSaveItemFreeParam {                         /* 0x4 big, align 4 */
  _2f681072                          Type;                                      // @0x0 size 0x4, align 4
};
struct s_1fc7814b {                                 /* 0x60 big, align 2 */
  char16                             Buffer[48];                                // @0x0 size 0x2, align 2
};
struct s_20b7a807 {                                 /* 0x28 big, align 2 */
  char16                             Buffer[20];                                // @0x0 size 0x2, align 2
};
struct GSaveMailUserLog {                           /* 0x14 big, align 2 */
  u16                                ListNpcSend[10];                           // @0x0 size 0x2, align 2
};
struct GSaveWordTownName {                          /* 0x14 big, align 2 */
  s_8aa46560                         TownName;                                  // @0x0 size 0x14, align 2
};
struct GSavePlayerTool {                            /* 0x8b8 big, align 8 */
  GSaveItemNameWithMyDesign          Tool;                                      // @0x0 size 0x8b0, align 8
  u8                                 LinkHolder;                                // @0x8b0 size 0x1, align 1
  s8                                 IndexInHolder;                             // @0x8b1 size 0x1, align 1
};
struct GSavePostingReserveList {                    /* 0xabd0 big, align 4 */
  GSavePostingReserveTomorrowNpc     ListTomorrowNpc[30];                       // @0x0 size 0x2b4, align 4
  GSavePostingReserveTomorrowSystem  ListTomorrowSystem[16];                    // @0x5118 size 0x2b4, align 4
  GSavePostingReserveInScene         ListInScene[4];                            // @0x7c58 size 0x2b8, align 4
  GSavePostingReserveMilage          ListMilage[5];                             // @0x8738 size 0x10, align 4
  GSavePostingReserveCatalog         ListCatalog[5];                            // @0x8788 size 0x2e8, align 4
  GSavePostingReserveCommune         ListCommune[8];                            // @0x9610 size 0x2b8, align 4
};
struct s_28557cb4 {                                 /* 0xb540 big, align 8 */
  GSaveFriendData                    Buffer[400];                               // @0x0 size 0x70, align 8
  s32                                IndexTable[400];                           // @0xaf00 size 0x4, align 4
};
struct s_2c3a15dc {                                 /* 0x104 big, align 4 */
  s16                                Id[128];                                   // @0x0 size 0x2, align 2
  s32                                AddPos;                                    // @0x100 size 0x4, align 4
};
struct GSavePlayerId {                              /* 0x38 big, align 4 */
  GSaveLandId                        LandId;                                    // @0x0 size 0x1c, align 4
  GSavePlayerBaseId                  BaseId;                                    // @0x1c size 0x1c, align 4
};
struct GSaveMyDesignPro {                           /* 0x8a8 big, align 8 */
  u32                                Hash;                                      // @0x0 size 0x4, align 4
  GSaveMyDesignVersion               Version;                                   // @0x4 size 0x4, align 4
  GSaveMyDesignHeader                Header;                                    // @0x8 size 0x70, align 8
  GSaveMyDesignPalette               Palette;                                   // @0x78 size 0x2d, align 1
  _d6acfb4d                          Sheets[4];                                 // @0xa5 size 0x200, align 1
  u8                                 Usage;                                     // @0x8a5 size 0x1, align 1
  u16                                _ba0d0cb9;                                 // @0x8a6 size 0x2, align 2
};
struct GSaveLifeSupport {                           /* 0x56ac big, align 4 */
  u16                                FlagsDaily[512];                           // @0x0 size 0x2, align 2
  bool                               EntryDaily[512];                           // @0x400 size 0x1, align 1
  bool                               ReadDaily[512];                            // @0x600 size 0x1, align 1
  bool                               RewardDaily[512];                          // @0x800 size 0x1, align 1
  bool                               CanSelectDaily[512];                       // @0xa00 size 0x1, align 1
  u16                                _397c2a8e[32];                             // @0xc00 size 0x2, align 2
  bool                               BonusDaily[512];                           // @0xc40 size 0x1, align 1
  s32                                BonusCount;                                // @0xe40 size 0x4, align 4
  u16                                _35f96941[8];                              // @0xe44 size 0x2, align 2
  u16                                _d8184fc5[32];                             // @0xe54 size 0x2, align 2
  u16                                TalkNpcBit;                                // @0xe94 size 0x2, align 2
  u8 gap_e96[2];
  u32                                CountAchievement[512];                     // @0xe98 size 0x4, align 4
  bool                               ReadAchievement[512][6];                   // @0x1698 size 0x1, align 1
  GSaveDate                          DateAchievement[512][6];                   // @0x2298 size 0x4, align 2
  _44c6787c                          NewAchievement[512];                       // @0x5298 size 0x1, align 1
  s_ec65e7b4                         NowPoint;                                  // @0x5498 size 0x8, align 4
  s_ec65e7b4                         TotalPoint;                                // @0x54a0 size 0x8, align 4
  bool                               BonusVDaily[512];                          // @0x54a8 size 0x1, align 1
  s32                                ChangedFirstFivePoint;                     // @0x56a8 size 0x4, align 4
};
struct s_341c3493 {                                 /* 0x60 big, align 2 */
  char16                             Buffer[48];                                // @0x0 size 0x2, align 2
};
struct GSavePlayerItemBag {                         /* 0xb8 big, align 4 */
  s_f89d9b67                         ItemHolder;                                // @0x0 size 0xa4, align 4
  s8                                 _7c3cae33[20];                             // @0xa4 size 0x1, align 1
};
struct GSavePlayerItemChest {                       /* 0x9c44 big, align 4 */
  s_8a06c9a5                         ItemHolder;                                // @0x0 size 0x9c44, align 4
};
struct GSaveMyDesignNormal {                        /* 0x2a8 big, align 8 */
  u32                                Hash;                                      // @0x0 size 0x4, align 4
  GSaveMyDesignVersion               Version;                                   // @0x4 size 0x4, align 4
  GSaveMyDesignHeader                Header;                                    // @0x8 size 0x70, align 8
  GSaveMyDesignPalette               Palette;                                   // @0x78 size 0x2d, align 1
  _d6acfb4d                          Sheets;                                    // @0xa5 size 0x200, align 1
  u8                                 _ba0d0cb9;                                 // @0x2a5 size 0x1, align 1
  u16                                _881e9e69;                                 // @0x2a6 size 0x2, align 2
};
struct GSaveItemName {                              /* 0x8 big, align 4 */
  u16                                UniqueID;                                  // @0x0 size 0x2, align 2
  GSaveItemSystemParam               SystemParam;                               // @0x2 size 0x1, align 1
  GSaveItemAdditionalParam           AdditionalParam;                           // @0x3 size 0x1, align 1
  GSaveItemFreeParam                 FreeParam;                                 // @0x4 size 0x4, align 4
};
struct GSaveProfileJPEG {                           /* 0x23020 big, align 16 */
  s_7b602b39                         _d35a9251;                                 // @0x0 size 0x10, align 16
  s32                                Size;                                      // @0x10 size 0x4, align 4
  u8                                 Buffer[143360];                            // @0x14 size 0x1, align 1
};
struct GSaveWordPlayerName {                        /* 0x14 big, align 2 */
  s_a0cb84dc                         PlayerName;                                // @0x0 size 0x14, align 2
};
struct GSavePersonal {                              /* 0x6d6d0 big, align 16 */
  GSaveVersion                       Version;                                   // @0x0 size 0x100, align 4
  u8                                 _5d1fcb04[8];                              // @0x100 size 0x1, align 1
  u8 gap_108[8];
  GSavePlayer                        Player;                                    // @0x110 size 0x35d30, align 16
  GSavePlayerOther                   PlayerOther;                               // @0x35e40 size 0x37890, align 16
};
struct GSaveBirthdayMessageList {                   /* 0x1180 big, align 8 */
  GSaveBirthdayMessage               List[8];                                   // @0x0 size 0x230, align 8
};
struct GSavePlayerItemPocket {                      /* 0xb8 big, align 4 */
  s_96c02c2e                         ItemHolder;                                // @0x0 size 0xa4, align 4
  s8                                 _7c3cae33[20];                             // @0xa4 size 0x1, align 1
};
struct GSavePlayerLook {                            /* 0x1fc8 big, align 8 */
  s_d06137a7                         _f0a37790;                                 // @0x0 size 0x1d00, align 8
  GSaveCharaMake                     CharaMake;                                 // @0x1d00 size 0x2b8, align 8
  GSaveItemName                      DefaultTops;                               // @0x1fb8 size 0x8, align 4
  GSaveItemName                      DefaultBottoms;                            // @0x1fc0 size 0x8, align 4
};
struct GSaveVersion {                               /* 0x100 big, align 4 */
  s_eafd2799                         CurrentVersionData;                        // @0x0 size 0x40, align 4
  s_eafd2799                         CreateVersionData;                         // @0x40 size 0x40, align 4
  u8                                 _5d1fcb04[128];                            // @0x80 size 0x1, align 1
};
struct s_5173e60a {                                 /* 0x40 big, align 2 */
  char16                             Buffer[32];                                // @0x0 size 0x2, align 2
};
struct GSaveCraftingRecipeCollect {                 /* 0x1400 big, align 2 */
  _7421b0a6                          RecipeCollectBit;                          // @0x0 size 0x100, align 1
  _7421b0a6                          RecipeMadeBit;                             // @0x100 size 0x100, align 1
  _7421b0a6                          RecipeNewBit;                              // @0x200 size 0x100, align 1
  _7421b0a6                          RecipeFavoriteBit;                         // @0x300 size 0x100, align 1
  u16                                RecipeOpenNum[2048];                       // @0x400 size 0x2, align 2
};
struct GSaveMyDesignVersion {                       /* 0x4 big, align 4 */
  u32                                SaveDataVersion;                           // @0x0 size 0x4, align 4
};
struct GSaveItemNameWithMyDesign {                  /* 0x8b0 big, align 8 */
  GSaveItemName                      ItemName;                                  // @0x0 size 0x8, align 4
  GSaveMyDesignPro                   MyDesign;                                  // @0x8 size 0x8a8, align 8
};
struct s_5700d3b2 {                                 /* 0x80 big, align 4 */
  u32                                Counter[32];                               // @0x0 size 0x4, align 4
};
struct GSaveSetting {                               /* 0x1 big, align 1 */
  u8                                 MiniMap;                                   // @0x0 size 0x1, align 1
};
struct GSaveMail {                                  /* 0x99d0 big, align 8 */
  GSaveMailText                      MailText;                                  // @0x0 size 0x2440, align 4
  bool                               HandWritingUsed;                           // @0x2440 size 0x1, align 1
  u8 gap_2441[3];
  GSaveHandWritten                   HandWritten;                               // @0x2444 size 0x7538, align 4
  u32                                UniqueId;                                  // @0x997c size 0x4, align 4
  _01851482                          MailId;                                    // @0x9980 size 0x8, align 8
  _a8d2a4d4                          FromPopId;                                 // @0x9988 size 0x8, align 8
  _010a9a24                          FromNsaId;                                 // @0x9990 size 0x8, align 8
  ::nn::settings::LanguageCode       LanguageCode;                              // @0x9998 size 0x8, align 1
  ::nn::time::PosixTime              SentAt;                                    // @0x99a0 size 0x8, align 8
  _13ff28ca                          Digest;                                    // @0x99a8 size 0x14, align 1
  u8                                 _5d1fcb04[16];                             // @0x99bc size 0x1, align 1
};
struct s_604fabb8 {                                 /* 0x20 big, align 4 */
  u32                                Bits[8];                                   // @0x0 size 0x4, align 4
};
struct GSaveNetMailData {                           /* 0x10 big, align 8 */
  _01851482                          MailID;                                    // @0x0 size 0x8, align 8
  s_0244bd71                         Status;                                    // @0x8 size 0x4, align 4
};
struct GSaveMailText {                              /* 0x2440 big, align 4 */
  GSaveMailPackage                   MailPackage;                               // @0x0 size 0xcc, align 4
  bool                               TextUsed;                                  // @0xcc size 0x1, align 1
  u8 gap_cd[1];
  s_9cfe48be                         TextHeader;                                // @0xce size 0x60, align 2
  s_87bef85e                         TextBody;                                  // @0x12e size 0x1e0, align 2
  s_341c3493                         TextFooter;                                // @0x30e size 0x60, align 2
  u16                                CardDesignId;                              // @0x36e size 0x2, align 2
  u16                                MelodyId;                                  // @0x370 size 0x2, align 2
  GSaveLandStamp                     Stamp;                                     // @0x372 size 0x2003, align 1
  u8 gap_2375[1];
  s_d18feb1f                         SealList[20];                              // @0x2376 size 0xa, align 2
};
struct GSavePostingReserveCatalog {                 /* 0x2e8 big, align 4 */
  GSavePostingReserveBase            ReserveBase;                               // @0x0 size 0x2b0, align 4
  GSavePlayerId                      ToPlayerId;                                // @0x2b0 size 0x38, align 4
};
struct GSavePlayer {                                /* 0x35d30 big, align 16 */
  s_7b602b39                         _d35a9251;                                 // @0x0 size 0x10, align 16
  s8                                 _18fdb93f;                                 // @0x10 size 0x1, align 1
  u8 gap_11[7];
  GSavePlayerLookPack                LookPack;                                  // @0x18 size 0xaf90, align 8
  GSavePlayerId                      PlayerId;                                  // @0xafa8 size 0x38, align 4
  GSaveEventFlagPlayer               EventFlag;                                 // @0xafe0 size 0x1000, align 2
  GSaveLifeSupport                   LifeSupport;                               // @0xbfe0 size 0x56ac, align 4
  GSaveDateMD                        BirthDay;                                  // @0x1168c size 0x2, align 1
  u16                                PastDaysFromMade;                          // @0x1168e size 0x2, align 2
  GSaveNetPlayerProfile              NetProfile;                                // @0x11690 size 0x8, align 8
  u8 gap_11698[8];
  GSaveProfileMain                   ProfileMain;                               // @0x116a0 size 0x234d0, align 16
  u8                                 _5d1fcb04[4];                              // @0x34b70 size 0x1, align 1
  GSaveDate                          LastPlayDate;                              // @0x34b74 size 0x4, align 2
  s16                                LastBirthdayYear;                          // @0x34b78 size 0x2, align 2
  GSaveDate                          BirthdayLiveDate;                          // @0x34b7a size 0x4, align 2
  u8 gap_34b7e[2];
  GSaveBirthdayMessageList           BirthdayLiveMsgList;                       // @0x34b80 size 0x1180, align 8
  GSaveItemName                      GalleryItem;                               // @0x35d00 size 0x8, align 4
  GSaveLandId                        GalleryLandId;                             // @0x35d08 size 0x1c, align 4
};
struct GSaveItemCollectBit {                        /* 0x754 big, align 4 */
  _2c4534e8                          CollectBitFlag;                            // @0x0 size 0x754, align 4
};
struct GSavePlayerOutfit {                          /* 0x1198 big, align 8 */
  GSaveCoordinateOutfit              CoordinateOutfit;                          // @0x0 size 0x1190, align 8
  GSaveItemName                      Marinesuit;                                // @0x1190 size 0x8, align 4
};
struct GSaveAmiibo {                                /* 0xa0 big, align 4 */
  GSaveSpecialNpcBitFlag             _e51f22f7;                                 // @0x0 size 0x10, align 4
  GSaveNormalNpcBitFlag              _2c6cce47;                                 // @0x10 size 0x8c, align 4
  _44c6787c                          FlagOther;                                 // @0x9c size 0x1, align 1
};
struct GSaveFriendList {                            /* 0xb548 big, align 8 */
  s_28557cb4                         FriendList;                                // @0x0 size 0xb540, align 8
  ::nn::time::PosixTime              _6ff0412c;                                 // @0xb540 size 0x8, align 8
};
struct GSaveClockTimeList {                         /* 0x180 big, align 1 */
  Game::ClockTimeBuffers             ClockTimeList[16];                         // @0x0 size 0x18, align 1
};
struct s_75f0022c {                                 /* 0x10 big, align 4 */
  GSaveSpecialNpcBitFlag             _920964e2;                                 // @0x0 size 0x10, align 4
};
struct GSaveCoordinateList {                        /* 0x8fc0 big, align 8 */
  GSaveCoordinate                    Coordinate[8];                             // @0x0 size 0x11f8, align 8
};
struct GSavePlayerItemBaggage {                     /* 0x17c big, align 4 */
  GSavePlayerItemBag                 ItemBag;                                   // @0x0 size 0xb8, align 4
  GSavePlayerItemPocket              ItemPocket;                                // @0xb8 size 0xb8, align 4
  GSaveMoney                         Wallet;                                    // @0x170 size 0x8, align 4
  u8                                 ExpandBaggage;                             // @0x178 size 0x1, align 1
};
struct s_79d059af {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveCoordinate {                            /* 0x11f8 big, align 8 */
  GSaveCoordinateOutfit              CoordinateOutfit;                          // @0x0 size 0x1190, align 8
  GSaveWordCoordinateName            CoordinateName;                            // @0x1190 size 0x60, align 2
  GSaveItemName                      CoordinateIconItem;                        // @0x11f0 size 0x8, align 4
};
struct GSaveMailPackage {                           /* 0xcc big, align 4 */
  u8                                 Status;                                    // @0x0 size 0x1, align 1
  bool                               Favorite;                                  // @0x1 size 0x1, align 1
  u8 gap_2[2];
  s_85955d55                         FromName;                                  // @0x4 size 0x5c, align 4
  s_85955d55                         ToName;                                    // @0x60 size 0x5c, align 4
  GSaveDate                          Date;                                      // @0xbc size 0x4, align 2
  GSaveItemName                      Present;                                   // @0xc0 size 0x8, align 4
  bool                               _5bac32e6;                                 // @0xc8 size 0x1, align 1
};
struct s_7b602b39 {                                 /* 0x10 big, align 16 */
  u32                                Code;                                      // @0x0 size 0x4, align 4
};
struct GSaveDate {                                  /* 0x4 big, align 2 */
  u16                                Year;                                      // @0x0 size 0x2, align 2
  u8                                 Month;                                     // @0x2 size 0x1, align 1
  u8                                 Day;                                       // @0x3 size 0x1, align 1
};
struct GSaveCharaMake {                             /* 0x2b8 big, align 8 */
  Game::CharaMakeSetting             CharaMakeSetting;                          // @0x0 size 0xc, align 2
  u8 gap_c[4];
  GSaveMyDesignNormal                FacePaintMyDesignNormal;                   // @0x10 size 0x2a8, align 8
};
struct s_85955d55 {                                 /* 0x5c big, align 4 */
  _e0b64e79                          NameInfo;                                  // @0x0 size 0x58, align 4
  u8                                 Type;                                      // @0x58 size 0x1, align 1
};
struct GSavePlayerLookPack {                        /* 0xaf90 big, align 8 */
  GSavePlayerLook                    Look;                                      // @0x0 size 0x1fc8, align 8
  GSaveCoordinateList                CoordinateList;                            // @0x1fc8 size 0x8fc0, align 8
  GSaveChangeStickInfo               ChangeStickInfo;                           // @0xaf88 size 0x2, align 1
};
struct s_87958bd4 {                                 /* 0xa4 big, align 4 */
  GSaveItemName                      Item[20];                                  // @0x0 size 0x8, align 4
  u32                                _4c5f8125;                                 // @0xa0 size 0x4, align 4
};
struct s_87bef85e {                                 /* 0x1e0 big, align 2 */
  char16                             Buffer[240];                               // @0x0 size 0x2, align 2
};
struct s_88464a80 {                                 /* 0x200 big, align 4 */
  u32                                Counter[128];                              // @0x0 size 0x4, align 4
};
struct s_88f8f5b0 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveHashList {                              /* 0x40 big, align 4 */
  u32                                HashList[16];                              // @0x0 size 0x4, align 4
};
struct s_8a06c9a5 {                                 /* 0x9c44 big, align 4 */
  GSaveItemName                      Item[5000];                                // @0x0 size 0x8, align 4
  u32                                _4c5f8125;                                 // @0x9c40 size 0x4, align 4
};
struct s_8aa46560 {                                 /* 0x14 big, align 2 */
  char16                             Buffer[10];                                // @0x0 size 0x2, align 2
};
struct GSaveSpecialNpcBitFlag {                     /* 0x10 big, align 4 */
  u32                                SpecialNpcBitFlag[4];                      // @0x0 size 0x4, align 4
};
struct GSavePlayerItemMaterial {                    /* 0x140 big, align 4 */
  GSaveItemName                      Item[32];                                  // @0x0 size 0x8, align 4
  u16                                Count[32];                                 // @0x100 size 0x2, align 2
};
struct GSaveChangeStickInfo {                       /* 0x2 big, align 1 */
  s8                                 LinkCoordinateIndex;                       // @0x0 size 0x1, align 1
  bool                               IsUseCoordinate;                           // @0x1 size 0x1, align 1
};
struct GSaveCoordinateOutfit {                      /* 0x1190 big, align 8 */
  GSaveItemNameWithMyDesign          Cap;                                       // @0x0 size 0x8b0, align 8
  GSaveItemName                      AcceEye;                                   // @0x8b0 size 0x8, align 4
  GSaveItemName                      AcceMouth;                                 // @0x8b8 size 0x8, align 4
  GSaveItemNameWithMyDesign          Tops;                                      // @0x8c0 size 0x8b0, align 8
  GSaveItemName                      Bottoms;                                   // @0x1170 size 0x8, align 4
  GSaveItemName                      Socks;                                     // @0x1178 size 0x8, align 4
  GSaveItemName                      Shoes;                                     // @0x1180 size 0x8, align 4
  GSaveItemName                      Bag;                                       // @0x1188 size 0x8, align 4
};
struct s_965e2bbb {                                 /* 0x100 big, align 4 */
  u32                                Counter[64];                               // @0x0 size 0x4, align 4
};
struct s_96c02c2e {                                 /* 0xa4 big, align 4 */
  GSaveItemName                      Item[20];                                  // @0x0 size 0x8, align 4
  u32                                _4c5f8125;                                 // @0xa0 size 0x4, align 4
};
struct GSavePostingReserveTomorrowNpc {             /* 0x2b4 big, align 4 */
  GSavePostingReserveBase            ReserveBase;                               // @0x0 size 0x2b0, align 4
  Game::NpcNormalID                  FromNpcId;                                 // @0x2b0 size 0x3, align 1
};
struct s_9cfe48be {                                 /* 0x60 big, align 2 */
  char16                             Buffer[48];                                // @0x0 size 0x2, align 2
};
struct s_9da53233 {                                 /* 0x40 big, align 4 */
  u32                                Counter[16];                               // @0x0 size 0x4, align 4
};
struct s_a0cb84dc {                                 /* 0x14 big, align 2 */
  char16                             Buffer[10];                                // @0x0 size 0x2, align 2
};
struct GSaveFirstCollection {                       /* 0x2 big, align 2 */
  u16                                UniqueID;                                  // @0x0 size 0x2, align 2
};
struct GSaveItemSystemParam {                       /* 0x1 big, align 1 */
  _bd508cb8                          Type;                                      // @0x0 size 0x1, align 1
};
struct s_ac6c2327 {                                 /* 0x8c big, align 4 */
  GSaveNormalNpcBitFlag              _920964e2;                                 // @0x0 size 0x8c, align 4
};
struct GSavePostingReserveTomorrowSystem {          /* 0x2b4 big, align 4 */
  GSavePostingReserveBase            ReserveBase;                               // @0x0 size 0x2b0, align 4
  u8                                 FromSystemId;                              // @0x2b0 size 0x1, align 1
};
struct s_b16331d2 {                                 /* 0x204 big, align 4 */
  s16                                Id[256];                                   // @0x0 size 0x2, align 2
  s32                                AddPos;                                    // @0x200 size 0x4, align 4
};
struct GSaveEventFlagPlayerVisit {                  /* 0x100 big, align 2 */
  s_dcf67314                         Flags;                                     // @0x0 size 0x100, align 2
};
struct GSavePersonalPlayReportInfo {                /* 0xd10 big, align 8 */
  s64                                MainPlayerTotalPlayTime;                   // @0x0 size 0x8, align 8
  s64                                TotalPlayTime;                             // @0x8 size 0x8, align 8
  s_ebd6060b                         PlayReportCounter;                         // @0x10 size 0x400, align 4
  s_965e2bbb                         _351a3f3f;                                 // @0x410 size 0x100, align 4
  s_12731d40                         _27a61057;                                 // @0x510 size 0x140, align 4
  s_9da53233                         _e11fda48;                                 // @0x650 size 0x40, align 4
  s_88464a80                         _4428a73a;                                 // @0x690 size 0x200, align 4
  s_5700d3b2                         ChatCounter;                               // @0x890 size 0x80, align 4
  u8                                 _165085c3[1024];                           // @0x910 size 0x1, align 1
};
struct GSaveNetPlayerID {                           /* 0x58 big, align 8 */
  _274348be                          Credential;                                // @0x0 size 0x50, align 8
  _010a9a24                          NSAID;                                     // @0x50 size 0x8, align 8
};
struct GSaveTime {                                  /* 0x8 big, align 2 */
  Calendar                           Calendar;                                  // @0x0 size 0x8, align 2
};
struct GSaveLandStamp {                             /* 0x2003 big, align 1 */
  u8                                 FrameID;                                   // @0x0 size 0x1, align 1
  u8                                 _cd842460;                                 // @0x1 size 0x1, align 1
  u8                                 ImageColorID;                              // @0x2 size 0x1, align 1
  u8                                 Image[8192];                               // @0x3 size 0x1, align 1
};
struct GSavePlayerHandleName {                      /* 0xa big, align 2 */
  u16                                ModifierId;                                // @0x0 size 0x2, align 2
  u8                                 ModifierLevel;                             // @0x2 size 0x1, align 1
  u8 gap_3[1];
  u16                                NounId;                                    // @0x4 size 0x2, align 2
  u8                                 NounLevel;                                 // @0x6 size 0x1, align 1
  u8                                 NounGenderType;                            // @0x7 size 0x1, align 1
  u8                                 NounGenderTypePrev;                        // @0x8 size 0x1, align 1
};
struct GSavePostingReserveBase {                    /* 0x2b0 big, align 4 */
  bool                               Reserved;                                  // @0x0 size 0x1, align 1
  bool                               TextUsed;                                  // @0x1 size 0x1, align 1
  u16                                CardDesignId;                              // @0x2 size 0x2, align 2
  GSaveItemName                      Present;                                   // @0x4 size 0x8, align 4
  GSaveDate                          Date;                                      // @0xc size 0x4, align 2
  s_9cfe48be                         Header;                                    // @0x10 size 0x60, align 2
  s_87bef85e                         Body;                                      // @0x70 size 0x1e0, align 2
  s_341c3493                         Footer;                                    // @0x250 size 0x60, align 2
};
struct s_ca6e8255 {                                 /* 0x100 big, align 2 */
  u16                                ValueArray[128];                           // @0x0 size 0x2, align 2
};
struct GSaveHandWritten {                           /* 0x7538 big, align 4 */
  u8                                 Image[30000];                              // @0x0 size 0x1, align 1
  u8                                 Palette[4];                                // @0x7530 size 0x1, align 1
  u32                                VerticesNum;                               // @0x7534 size 0x4, align 4
};
struct GSavePostingReserveInScene {                 /* 0x2b8 big, align 4 */
  GSavePostingReserveBase            ReserveBase;                               // @0x0 size 0x2b0, align 4
  u8                                 ReserveType;                               // @0x2b0 size 0x1, align 1
  u8                                 FromType;                                  // @0x2b1 size 0x1, align 1
  Game::NpcNormalID                  FromNpcId;                                 // @0x2b2 size 0x3, align 1
  u8                                 FromSystemId;                              // @0x2b5 size 0x1, align 1
};
struct GSaveProfileMain {                           /* 0x234d0 big, align 16 */
  GSaveProfileJPEG                   JPEG;                                      // @0x0 size 0x23020, align 16
  GSavePlayerId                      PlayerId;                                  // @0x23020 size 0x38, align 4
  GSaveDateMD                        BirthDay;                                  // @0x23058 size 0x2, align 1
  u8 gap_2305a[2];
  GSaveItemName                      SpecialityFruit;                           // @0x2305c size 0x8, align 4
  GSavePlayerHandleName              HandleName;                                // @0x23064 size 0xa, align 2
  s_5173e60a                         Comment;                                   // @0x2306e size 0x40, align 2
  Game::NpcNormalID                  NpcNormalIDArray[10];                      // @0x230ae size 0x3, align 1
  GSaveDate                          TimeStamp;                                 // @0x230cc size 0x4, align 2
  bool                               IsMakeVillagePlayer;                       // @0x230d0 size 0x1, align 1
  u8 gap_230d1[7];
  _7f75c347                          PlayerProfileReportInfo;                   // @0x230d8 size 0x28, align 8
  _11116f4e                          DesignerID;                                // @0x23100 size 0x8, align 8
  ::nn::settings::LanguageCode       LanguageCode;                              // @0x23108 size 0x8, align 1
  u8                                 _5d1fcb04[952];                            // @0x23110 size 0x1, align 1
};
struct s_d06137a7 {                                 /* 0x1d00 big, align 8 */
  GSavePlayerOutfit                  Outfit;                                    // @0x0 size 0x1198, align 8
  GSavePlayerTool                    ToolPack;                                  // @0x1198 size 0x8b8, align 8
  GSaveItemName                      SmartPhone;                                // @0x1a50 size 0x8, align 4
  GSaveMyDesignNormal                SmartPhoneMyDesign;                        // @0x1a58 size 0x2a8, align 8
};
struct s_d18feb1f {                                 /* 0xa big, align 2 */
  u16                                Id;                                        // @0x0 size 0x2, align 2
  s16                                PosX;                                      // @0x2 size 0x2, align 2
  s16                                PosY;                                      // @0x4 size 0x2, align 2
  u16                                Angle;                                     // @0x6 size 0x2, align 2
  u8                                 Scale;                                     // @0x8 size 0x1, align 1
  bool                               Used;                                      // @0x9 size 0x1, align 1
};
struct GSaveDateMD {                                /* 0x2 big, align 1 */
  u8                                 Month;                                     // @0x0 size 0x1, align 1
  u8                                 Day;                                       // @0x1 size 0x1, align 1
};
struct GSaveMoney {                                 /* 0x8 big, align 4 */
  s_ec65e7b4                         Wallet;                                    // @0x0 size 0x8, align 4
};
struct GSaveInsectCollection {                      /* 0xd6 big, align 2 */
  GSaveFirstCollection               Insect[100];                               // @0x0 size 0x2, align 2
  _4a7be1ce                          NewInsectFlag;                             // @0xc8 size 0xd, align 1
  u8                                 Count;                                     // @0xd5 size 0x1, align 1
};
struct GSaveItemRemakeCollectBit {                  /* 0x7d0 big, align 4 */
  _f941cca8                          CollectBitFlag;                            // @0x0 size 0x7d0, align 4
};
struct GSavePlayerItemInsectFishBox {               /* 0x148 big, align 4 */
  s_87958bd4                         ItemHolderMyVillage;                       // @0x0 size 0xa4, align 4
  s_87958bd4                         ItemHolderOtherVillage;                    // @0xa4 size 0xa4, align 4
};
struct GSaveItemAdditionalParam {                   /* 0x1 big, align 1 */
  _28a7a613                          Type;                                      // @0x0 size 0x1, align 1
};
struct s_dcf67314 {                                 /* 0x100 big, align 2 */
  u16                                ValueArray[128];                           // @0x0 size 0x2, align 2
};
struct GSavePlayerManpu {                           /* 0x88 big, align 1 */
  u8                                 ManpuBit[64];                              // @0x0 size 0x1, align 1
  u8                                 UIList[8];                                 // @0x40 size 0x1, align 1
  bool                               NewFlag[64];                               // @0x48 size 0x1, align 1
};
struct GSaveNetPlayerProfile {                      /* 0x8 big, align 8 */
  _11116f4e                          DesignerID;                                // @0x0 size 0x8, align 8
};
struct GSaveFishCollection {                        /* 0xd6 big, align 2 */
  GSaveFirstCollection               Fish[100];                                 // @0x0 size 0x2, align 2
  _9c6f52d5                          NewFishFlag;                               // @0xc8 size 0xd, align 1
  u8                                 Count;                                     // @0xd5 size 0x1, align 1
};
struct GSaveLandId {                                /* 0x1c big, align 4 */
  u32                                Id;                                        // @0x0 size 0x4, align 4
  GSaveWordTownName                  Name;                                      // @0x4 size 0x14, align 2
  u8                                 IslandRubyType;                            // @0x18 size 0x1, align 1
};
struct s_eafd2799 {                                 /* 0x40 big, align 4 */
  u32                                _e58767da;                                 // @0x0 size 0x4, align 4
  u32                                _d0c3cf50;                                 // @0x4 size 0x4, align 4
  u32                                SaveHeaderVersion;                         // @0x8 size 0x4, align 4
  u16                                _8593e326;                                 // @0xc size 0x2, align 2
  u16                                RomReleaseVersion;                         // @0xe size 0x2, align 2
  u8                                 _5d1fcb04[48];                             // @0x10 size 0x1, align 1
};
struct s_eb93f5a5 {                                 /* 0x1000 big, align 2 */
  u16                                ValueArray[2048];                          // @0x0 size 0x2, align 2
};
struct s_ebd6060b {                                 /* 0x400 big, align 4 */
  u32                                Counter[256];                              // @0x0 size 0x4, align 4
};
struct s_ec65e7b4 {                                 /* 0x8 big, align 4 */
  u32                                _71de9932;                                 // @0x0 size 0x4, align 4
  u16                                _79d56a0c;                                 // @0x4 size 0x2, align 2
  u8                                 _d69168be;                                 // @0x6 size 0x1, align 1
  u8                                 _c5b49f7e;                                 // @0x7 size 0x1, align 1
};
struct s_ed5e4786 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveEventFlagPlayerTemp {                   /* 0x100 big, align 2 */
  s_ca6e8255                         Flags;                                     // @0x0 size 0x100, align 2
};
struct GSaveRemakeCommonPattern {                   /* 0x10 big, align 1 */
  _9ac725f3                          Unlocks;                                   // @0x0 size 0x10, align 1
};
struct GSaveMailUserInfo {                          /* 0x13418 big, align 8 */
  s_341c3493                         _ec2a1361;                                 // @0x0 size 0x60, align 2
  s_ed5e4786                         _2b389b6f;                                 // @0x60 size 0x4, align 4
  u8 gap_64[4];
  GSaveMail                          TemporaryMail;                             // @0x68 size 0x99d0, align 8
  _a8d2a4d4                          TemporaryMailToPopId;                      // @0x9a38 size 0x8, align 8
  GSaveMail                          FutureMail;                                // @0x9a40 size 0x99d0, align 8
  GSaveDate                          FutureMailDate;                            // @0x13410 size 0x4, align 2
};
struct GSaveBirthdayMessage {                       /* 0x230 big, align 8 */
  bool                               Used;                                      // @0x0 size 0x1, align 1
  bool                               Displayed;                                 // @0x1 size 0x1, align 1
  bool                               MailSend;                                  // @0x2 size 0x1, align 1
  u8 gap_3[1];
  s_87bef85e                         Body;                                      // @0x4 size 0x1e0, align 2
  GSavePlayerId                      FromPlayerId;                              // @0x1e4 size 0x38, align 4
  u8 gap_21c[4];
  _a8d2a4d4                          FromPopId;                                 // @0x220 size 0x8, align 8
  _010a9a24                          FromNsaId;                                 // @0x228 size 0x8, align 8
};
struct GSaveNetMailBox {                            /* 0x660 big, align 8 */
  GSaveNetMailData                   DeleteList[100];                           // @0x0 size 0x10, align 8
  ::nn::time::SteadyClockTimePoint   ActivateTime;                              // @0x640 size 0x18, align 8
  u32                                OfficialMailCountTotal;                    // @0x658 size 0x4, align 4
  u8                                 OfficialMailCountToday;                    // @0x65c size 0x1, align 1
  u8                                 BgReceiveCount;                            // @0x65d size 0x1, align 1
};
struct GSaveAudioRegister {                         /* 0x20 big, align 4 */
  s_604fabb8                         RegisterBitList;                           // @0x0 size 0x20, align 4
};
struct GSavePlayerVisitorNpc {                      /* 0x90 big, align 8 */
  _d58a9885                          HgcOutfit;                                 // @0x0 size 0x48, align 4
  _382f646e                          HgcFashionThemeBit;                        // @0x48 size 0x8, align 8
  s32                                HgcTodayFashionTheme;                      // @0x50 size 0x4, align 4
  GSaveItemName                      GulRewardItem;                             // @0x54 size 0x8, align 4
  GSaveItemName                      HgcSampleItem;                             // @0x5c size 0x8, align 4
  GSaveItemName                      HgcRewardItem;                             // @0x64 size 0x8, align 4
  GSaveItemName                      CodeRecipeUser;                            // @0x6c size 0x8, align 4
  GSaveItemName                      _46d1ef70;                                 // @0x74 size 0x8, align 4
  GSaveItemName                      _24c43489;                                 // @0x7c size 0x8, align 4
  GSaveItemName                      GulBRewardItem;                            // @0x84 size 0x8, align 4
};
struct s_f89d9b67 {                                 /* 0xa4 big, align 4 */
  GSaveItemName                      Item[20];                                  // @0x0 size 0x8, align 4
  u32                                _4c5f8125;                                 // @0xa0 size 0x4, align 4
};
struct s_664fcb9a {                                 /* 0xb44470 big, align 8 */
  GSaveMail                          Buffer[300];                               // @0x0 size 0x99d0, align 8
  s32                                IndexTable[300];                           // @0xb43fc0 size 0x4, align 4
};
struct GSavePostBox {                               /* 0xb44590 big, align 16 */
  GSaveVersion                       Version;                                   // @0x0 size 0x100, align 4
  s_7b602b39                         _d35a9251;                                 // @0x100 size 0x10, align 16
  s_664fcb9a                         MailList;                                  // @0x110 size 0xb44470, align 8
  u32                                LatestUniqueId;                            // @0xb44580 size 0x4, align 4
};
struct GSaveRoomFloorWall {                         /* 0x24 big, align 4 */
  GSaveItemName                      AccentWallItem;                            // @0x0 size 0x8, align 4
  GSaveItemName                      WallItem;                                  // @0x8 size 0x8, align 4
  GSaveItemName                      FloorItem;                                 // @0x10 size 0x8, align 4
  GSaveMyDesignId                    AccentWallMyDesignID;                      // @0x18 size 0x2, align 2
  GSaveMyDesignId                    WallMyDesignID;                            // @0x1a size 0x2, align 2
  GSaveMyDesignId                    FloorMyDesignID;                           // @0x1c size 0x2, align 2
  s8                                 AccentWallDirection;                       // @0x1e size 0x1, align 1
  _44c6787c                          InfoBit;                                   // @0x1f size 0x1, align 1
  _44c6787c                          InfoBit2;                                  // @0x20 size 0x1, align 1
};
struct GSaveMyDesignId {                            /* 0x2 big, align 2 */
  u16                                MyDesignId;                                // @0x0 size 0x2, align 2
};
struct GSavePhotoStudioHouse {                      /* 0x2c8b0 big, align 4 */
  GSavePlayerHouseRoom               RoomList[6];                               // @0x0 size 0x65c8, align 4
  GSavePlayerHouseRoom               JuneBrideRoom;                             // @0x262b0 size 0x65c8, align 4
  GSaveJuneBrideSNpc                 JuneBrideSnpcList[2];                      // @0x2c878 size 0x10, align 4
  GSaveJuneBrideRoomExtra            JuneBrideRoomExtra;                        // @0x2c898 size 0x18, align 4
};
struct GSaveJuneBrideRoomExtra {                    /* 0x18 big, align 4 */
  GSaveItemName                      DefaultWallItem;                           // @0x0 size 0x8, align 4
  GSaveItemName                      DefaultFloorItem;                          // @0x8 size 0x8, align 4
  GSaveItemName                      DefaultRugItem;                            // @0x10 size 0x8, align 4
};
struct GSavePhotoStudioIsland {                     /* 0x2c9c0 big, align 16 */
  GSaveVersion                       Version;                                   // @0x0 size 0x100, align 4
  s_7b602b39                         _d35a9251;                                 // @0x100 size 0x10, align 16
  GSavePhotoStudioHouse              PhotoStudioHouse;                          // @0x110 size 0x2c8b0, align 4
};
struct GSaveAudioInfo {                             /* 0x4 big, align 2 */
  s16                                PlayingAudioMusicID;                       // @0x0 size 0x2, align 2
  s8                                 _749b78c2;                                 // @0x2 size 0x1, align 1
  _44c6787c                          IsShuffle;                                 // @0x3 size 0x1, align 1
};
struct GSaveJuneBrideSNpc {                         /* 0x10 big, align 4 */
  bool                               IsValid;                                   // @0x0 size 0x1, align 1
  u8                                 NpcPosture;                                // @0x1 size 0x1, align 1
  u8                                 Reaction;                                  // @0x2 size 0x1, align 1
  s8                                 AngleY;                                    // @0x3 size 0x1, align 1
  V3f                                Pos;                                       // @0x4 size 0xc, align 4
};
struct s_c20a4615 {                                 /* 0x34 big, align 4 */
  u32                                Bits[13];                                  // @0x0 size 0x4, align 4
};
struct s_d8bc748b {                                 /* 0xc80 big, align 4 */
  GSaveItemName                      ItemArray[20][20];                         // @0x0 size 0x8, align 4
};
struct GSavePlayerHouseRoom {                       /* 0x65c8 big, align 4 */
  s_d8bc748b                         ItemLayerList[8];                          // @0x0 size 0xc80, align 4
  s_c20a4615                         ItemSwitchList[8];                         // @0x6400 size 0x34, align 4
  GSaveAudioInfo                     AudioInfo;                                 // @0x65a0 size 0x4, align 2
  GSaveRoomFloorWall                 RoomFloorWall;                             // @0x65a4 size 0x24, align 4
};
struct GSaveProfile {                               /* 0x69560 big, align 16 */
  GSaveVersion                       Version;                                   // @0x0 size 0x100, align 4
  s_7b602b39                         _d35a9251;                                 // @0x100 size 0x10, align 16
  GSaveProfileJPEG                   StockJPEGArray[3];                         // @0x110 size 0x23020, align 16
  u8                                 MainIndex;                                 // @0x69170 size 0x1, align 1
  u8                                 _5d1fcb04[1003];                           // @0x69171 size 0x1, align 1
};
struct s_01e61348 {                                 /* 0x100 big, align 2 */
  u16                                ValueArray[128];                           // @0x0 size 0x2, align 2
};
struct GSaveShopGallery {                           /* 0x1ac big, align 4 */
  GSaveItemName                      ShopItem[6];                               // @0x0 size 0x8, align 4
  bool                               SoldOut[6];                                // @0x30 size 0x1, align 1
  u8 gap_36[2];
  GSavePlayerId                      PlayerId[6];                               // @0x38 size 0x38, align 4
  GSaveItemName                      VisitItem;                                 // @0x188 size 0x8, align 4
  u8                                 _5d1fcb04[28];                             // @0x190 size 0x1, align 1
};
struct GSaveLandOther {                             /* 0x5d4020 big, align 16 */
  GSavePersonal                      GuestPlayers[8];                           // @0x0 size 0x6d6d0, align 16
  s_7b602b39                         _d35a9251;                                 // @0x36b680 size 0x10, align 16
  GSaveFgOther                       Fg;                                        // @0x36b690 size 0x3fc, align 4
  u8 gap_36ba8c[4];
  GSavePostStock                     PostStock;                                 // @0x36ba90 size 0x2633d0, align 8
  GSaveShopOther                     ShopOther;                                 // @0x5cee60 size 0xc, align 4
  u8 gap_5cee6c[4];
  GSaveLandPlayReportInfo            PlayReportInfo;                            // @0x5cee70 size 0x480, align 8
  GSaveDebugLog                      DebugLog;                                  // @0x5cf2f0 size 0x100, align 8
  GSaveLostItemBox                   LostItemBox;                               // @0x5cf3f0 size 0x280, align 4
  GSaveNetLandID                     NetLandID;                                 // @0x5cf670 size 0x80, align 8
  GSavePlayerActivity                CurrentPlayerActivity[8];                  // @0x5cf6f0 size 0xd8, align 8
  GSavePlayerActivity                PreviousPlayerActivity[8];                 // @0x5cfdb0 size 0xd8, align 8
  GSavePlayerActivityPack            VisitorPlayerActivityPack[8];              // @0x5d0470 size 0x6c0, align 8
  GSaveSettlerQuest                  SettlerQuest;                              // @0x5d3a70 size 0xc0, align 4
  GSaveMyDesignHolderList            MyDesignHolderList;                        // @0x5d3b30 size 0x64, align 1
  GSaveLandHashValue                 GrowUpRandomFactor;                        // @0x5d3b94 size 0x4, align 4
  GSaveWeather                       TourWeather;                               // @0x5d3b98 size 0x14c, align 4
  GSaveMyDesignListOrder             MyDesignListOrder;                         // @0x5d3ce4 size 0x64, align 1
  GSaveTime                          LastSaveTime;                              // @0x5d3d48 size 0x8, align 2
  s32                                MoveKitPlayer;                             // @0x5d3d50 size 0x4, align 4
  s32                                MoveKitNpc;                                // @0x5d3d54 size 0x4, align 4
  GSaveHashList                      HashList;                                  // @0x5d3d58 size 0x40, align 4
  GSaveNetworkEventData              EventData;                                 // @0x5d3d98 size 0x280, align 4
};
struct GSaveShopOther {                             /* 0xc big, align 4 */
  u32                                PlayerTotalBuy;                            // @0x0 size 0x4, align 4
  u32                                PlayerTotalSell;                           // @0x4 size 0x4, align 4
  u32                                TotalTailor;                               // @0x8 size 0x4, align 4
};
struct GSaveDebugLog {                              /* 0x100 big, align 8 */
  _382f646e                          DebugPageLog[16];                          // @0x0 size 0x8, align 8
  _382f646e                          ShopFtrCount[16];                          // @0x80 size 0x8, align 8
};
struct GSaveRumorFavoriteData {                     /* 0x6c big, align 2 */
  GSaveWordTasteName                 TasteName;                                 // @0x0 size 0x60, align 2
  GSaveTime                          LastDenyTime;                              // @0x60 size 0x8, align 2
  u16                                NpcID;                                     // @0x68 size 0x2, align 2
  u8                                 SelectAnswer;                              // @0x6a size 0x1, align 1
};
struct GSaveQuestVisit {                            /* 0x38 big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  u8                                 IsTalk;                                    // @0x34 size 0x1, align 1
  u8                                 FailureReason;                             // @0x35 size 0x1, align 1
  u8                                 Enter;                                     // @0x36 size 0x1, align 1
};
struct GSaveLandPlayReportInfo {                    /* 0x480 big, align 8 */
  s64                                TotalPlayTime;                             // @0x0 size 0x8, align 8
  s_45f23180                         PlayReportCounter;                         // @0x8 size 0x400, align 4
  u8                                 _165085c3[120];                            // @0x408 size 0x1, align 1
};
struct s_10357ff1 {                                 /* 0x2c big, align 2 */
  char16                             Buffer[22];                                // @0x0 size 0x2, align 2
};
struct GSaveShopTailor {                            /* 0x12d4 big, align 4 */
  s_7501864a                         TailorLevel;                               // @0x0 size 0x4, align 4
  GSaveItemName                      ShopItem[128];                             // @0x4 size 0x8, align 4
  GSaveItemCollectBit                CollectBit;                                // @0x404 size 0x754, align 4
  GSaveItemCollectBit                ReserveItemBit;                            // @0xb58 size 0x754, align 4
  GSaveItemName                      TodayAddItem;                              // @0x12ac size 0x8, align 4
  GSaveItemName                      TorsoItem;                                 // @0x12b4 size 0x8, align 4
  s32                                MannequinCoodinate[2];                     // @0x12bc size 0x4, align 4
  s32                                CoodinateLog1[2];                          // @0x12c4 size 0x4, align 4
  s32                                CoodinateLog2[2];                          // @0x12cc size 0x4, align 4
};
struct GCamperData {                                /* 0x1c big, align 4 */
  u16                                NpcID;                                     // @0x0 size 0x2, align 2
  u8 gap_2[2];
  GSaveItemName                      ItemName[3];                               // @0x4 size 0x8, align 4
};
struct s_14166c92 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct s_17010e57 {                                 /* 0x180920 big, align 8 */
  GSaveMail                          Buffer[40];                                // @0x0 size 0x99d0, align 8
  s32                                IndexTable[40];                            // @0x180880 size 0x4, align 4
};
struct s_19abb3ec {                                 /* 0x800 big, align 2 */
  u16                                ValueArray[1024];                          // @0x0 size 0x2, align 2
};
struct GSaveGrowUpParam {                           /* 0x4 big, align 4 */
  u32                                GrowUpData;                                // @0x0 size 0x4, align 4
};
struct GSaveQuestDelivery {                         /* 0x40 big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  GSaveItemName                      DeliveryItem;                              // @0x34 size 0x8, align 4
  s8                                 ReceiverNpcVillagerIndex;                  // @0x3c size 0x1, align 1
  u8 gap_3d[1];
  u16                                Flag;                                      // @0x3e size 0x2, align 2
};
struct GSaveWeather {                               /* 0x14c big, align 4 */
  GSaveTime                          UpdateTime;                                // @0x0 size 0x8, align 2
  s32                                YesterdayWeatherPattern;                   // @0x8 size 0x4, align 4
  s32                                TodayWeatherPattern;                       // @0xc size 0x4, align 4
  s32                                TommorowWeatherPattern;                    // @0x10 size 0x4, align 4
  s_e4ba56bd                         WeatherArea;                               // @0x14 size 0x4, align 4
  u32                                _3bb101ca;                                 // @0x18 size 0x4, align 4
  s_99f29105                         CloudPattern[24];                          // @0x1c size 0x4, align 4
  s_c20f88d8                         RainbowPattern[24];                        // @0x7c size 0x4, align 4
  s_91441d11                         AuroraPattern[24];                         // @0xdc size 0x4, align 4
  s_ec5af5d2                         MorningGlow;                               // @0x13c size 0x4, align 4
  s_b53802e9                         EveningGlow;                               // @0x140 size 0x4, align 4
  bool                               NormalFog;                                 // @0x144 size 0x1, align 1
  bool                               WaterFog;                                  // @0x145 size 0x1, align 1
  u8 gap_146[2];
  s32                                ReserveWeatherPattern;                     // @0x148 size 0x4, align 4
};
struct GSaveSettlerNpc {                            /* 0x3c big, align 4 */
  Game::NpcNormalID                  Id;                                        // @0x0 size 0x3, align 1
  u8 gap_3[1];
  GSavePlayerBaseId                  PlayerBaseId;                              // @0x4 size 0x1c, align 4
  u8                                 Step;                                      // @0x20 size 0x1, align 1
  u8 gap_21[3];
  GSaveItemName                      FtrList[3];                                // @0x24 size 0x8, align 4
};
struct GSaveMyDesignHolder {                        /* 0x1 big, align 1 */
  s8                                 PlayerVillagerIndex;                       // @0x0 size 0x1, align 1
};
struct GSaveNpcVillager {                           /* 0x1d6d48 big, align 8 */
  GSaveAnimal                        Animal[10];                                // @0x0 size 0x12ab0, align 8
  u32                                GrowBitArray[35];                          // @0xbaae0 size 0x4, align 4
  u8 gap_bab6c[4];
  GSaveAnimal                        MoveInAnimal[4];                           // @0xbab70 size 0x12ab0, align 8
  GSaveAnimal                        MoveOutAnimal[10];                         // @0x105630 size 0x12ab0, align 8
  GSaveQuest                         Quest;                                     // @0x1c0110 size 0x1a8, align 4
  GSaveDate                          LastSurpriseDate;                          // @0x1c02b8 size 0x4, align 2
  GSaveNpcArchive                    NpcArchive[400];                           // @0x1c02bc size 0xe8, align 4
  s8                                 NpcBirthdayHouse;                          // @0x1d6d3c size 0x1, align 1
  s8                                 MoveOutVillagerIndex;                      // @0x1d6d3d size 0x1, align 1
  s8                                 MoveOutSkipCount;                          // @0x1d6d3e size 0x1, align 1
  s8                                 MoveOutTalkCount;                          // @0x1d6d3f size 0x1, align 1
  s8                                 MoveOutFixedFlag;                          // @0x1d6d40 size 0x1, align 1
  s8                                 NewestVillagerIndex;                       // @0x1d6d41 size 0x1, align 1
  s8                                 MoveStopVillagerIndex;                     // @0x1d6d42 size 0x1, align 1
  s8                                 DIYVillagerArray[3];                       // @0x1d6d43 size 0x1, align 1
  s8                                 _611f391f;                                 // @0x1d6d46 size 0x1, align 1
};
struct GSaveQuestLost {                             /* 0x3c big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  u8                                 IsRejected;                                // @0x34 size 0x1, align 1
  u8                                 IsUseHint;                                 // @0x35 size 0x1, align 1
  u8                                 OccurRatio;                                // @0x36 size 0x1, align 1
  u8 gap_37[1];
  s16                                DropUnitX;                                 // @0x38 size 0x2, align 2
  s16                                DropUnitZ;                                 // @0x3a size 0x2, align 2
};
struct s_33a3f71b {                                 /* 0x100 big, align 1 */
  u8                                 ValueArray[256];                           // @0x0 size 0x1, align 1
};
struct GSaveCampSite {                              /* 0x4 big, align 4 */
  s_9aae222a                         CampSiteLevel;                             // @0x0 size 0x4, align 4
};
struct GSaveLandTime {                              /* 0xe0 big, align 8 */
  GSaveTime                          LastGrowUpTime;                            // @0x0 size 0x8, align 2
  GSaveDate                          CreateDate;                                // @0x8 size 0x4, align 2
  bool                               SummerTimeFlag;                            // @0xc size 0x1, align 1
  bool                               InitializeFlag;                            // @0xd size 0x1, align 1
  u8 gap_e[2];
  nn::time::ClockSnapshot            ClockSnapshot;                             // @0x10 size 0xd0, align 8
};
struct GSaveSettlerQuest {                          /* 0xc0 big, align 4 */
  GSaveSettlerNpc                    NpcList[3];                                // @0x0 size 0x3c, align 4
  u8                                 MoveInOrder[3];                            // @0xb4 size 0x1, align 1
  u8                                 HouseIndex[3];                             // @0xb7 size 0x1, align 1
  u8                                 QuestSettlerIndex[3];                      // @0xba size 0x1, align 1
};
struct GSaveVillageMelodyData {                     /* 0x8 big, align 8 */
  u64                                OneValue;                                  // @0x0 size 0x8, align 8
};
struct GSaveNpcHouseList {                          /* 0x1248 big, align 4 */
  GSaveNpcHouse                      HouseList[10];                             // @0x0 size 0x1d4, align 4
};
struct s_3cec5cfe {                                 /* 0x24c00 big, align 2 */
  GSaveFieldLandMakingMapData        Map[112][96];                              // @0x0 size 0xe, align 2
};
struct GSaveItemMarketingRoute {                    /* 0x2 big, align 1 */
  u8                                 VillageMarketingType;                      // @0x0 size 0x1, align 1
  u8                                 VillageLotId;                              // @0x1 size 0x1, align 1
};
struct GSaveAnimal {                                /* 0x12ab0 big, align 8 */
  Game::NpcNormalID                  Id;                                        // @0x0 size 0x3, align 1
  u8 gap_3[1];
  GSaveMemory                        Memory[8];                                 // @0x4 size 0x5f0, align 4
  GSaveLightMemory                   LightMemory[160];                          // @0x2f84 size 0x14c, align 4
  GSaveLandId                        LastLandId[8];                             // @0xff04 size 0x1c, align 4
  _0382f336                          Place;                                     // @0xffe4 size 0x4, align 4
  GSaveWordPhrase                    Phrase;                                    // @0xffe8 size 0x1e4, align 2
  GSaveNpcStockItemData              WearStockList[24];                         // @0x101cc size 0x2c, align 4
  GSaveNpcStockItemData              FtrStockList[32];                          // @0x105ec size 0x2c, align 4
  GSaveNpcReleaseItemData            ReleaseItemList[64];                       // @0x10b6c size 0x4c, align 4
  GSaveNpcStockItemData              TopsData;                                  // @0x11e6c size 0x2c, align 4
  GSaveNpcStockItemData              AccessoryData;                             // @0x11e98 size 0x2c, align 4
  GSaveNpcStockItemData              CapData;                                   // @0x11ec4 size 0x2c, align 4
  GSaveDate                          PhraseSetDate;                             // @0x11ef0 size 0x4, align 2
  GSaveDate                          BirthDate;                                 // @0x11ef4 size 0x4, align 2
  s8                                 BirthType;                                 // @0x11ef8 size 0x1, align 1
  s8                                 InducementType;                            // @0x11ef9 size 0x1, align 1
  s8                                 MoveType;                                  // @0x11efa size 0x1, align 1
  u8 gap_11efb[1];
  GSaveEventFlagNpcSave              EventFlag;                                 // @0x11efc size 0x200, align 2
  s16                                PlayingAudioMusicID;                       // @0x120fc size 0x2, align 2
  u8 gap_120fe[2];
  GSaveRoomFloorWall                 RoomFloorWall;                             // @0x12100 size 0x24, align 4
  u8 gap_12124[4];
  GSaveMyDesignPro                   MyDesign;                                  // @0x12128 size 0x8a8, align 8
  u8                                 ClothBuyCount;                             // @0x129d0 size 0x1, align 1
  s8                                 DIYEndHour;                                // @0x129d1 size 0x1, align 1
  s8                                 DIYEndMinute;                              // @0x129d2 size 0x1, align 1
  s8                                 DIYEndSecond;                              // @0x129d3 size 0x1, align 1
  s16                                DIYRecipeIndex;                            // @0x129d4 size 0x2, align 2
  u8                                 FtrGetBit[5];                              // @0x129d6 size 0x1, align 1
  u8                                 EquipRuleID;                               // @0x129db size 0x1, align 1
  GSaveNpcStockItemData              Umbrella;                                  // @0x129dc size 0x2c, align 4
  GSaveNpcStockItemData              ToolNet;                                   // @0x12a08 size 0x2c, align 4
  GSaveNpcStockItemData              ToolAngling;                               // @0x12a34 size 0x2c, align 4
  GSaveNpcStockItemData              ToolWatering;                              // @0x12a60 size 0x2c, align 4
  GSaveItemName                      Music;                                     // @0x12a8c size 0x8, align 4
  GSaveItemName                      UsuallyTops;                               // @0x12a94 size 0x8, align 4
  GSaveItemName                      UsuallyCap;                                // @0x12a9c size 0x8, align 4
  GSaveItemName                      UsuallyAccessory;                          // @0x12aa4 size 0x8, align 4
};
struct GSaveEventFlagHouse {                        /* 0x100 big, align 2 */
  s_01e61348                         Flags;                                     // @0x0 size 0x100, align 2
};
struct s_3f77a59c {                                 /* 0x14 big, align 2 */
  char16                             Buffer[10];                                // @0x0 size 0x2, align 2
};
struct GSaveOutsideField {                          /* 0x92 big, align 2 */
  Game::FieldBlockData               FieldBlockData;                            // @0x0 size 0x90, align 2
  u16                                TemplateUniqueId;                          // @0x90 size 0x2, align 2
};
struct GSaveStructureData {                         /* 0x14 big, align 4 */
  u16                                StructureIndexUniqueID;                    // @0x0 size 0x2, align 2
  s16                                BaseUnitX;                                 // @0x2 size 0x2, align 2
  s16                                BaseUnitZ;                                 // @0x4 size 0x2, align 2
  s8                                 Angle;                                     // @0x6 size 0x1, align 1
  u8                                 Bit;                                       // @0x7 size 0x1, align 1
  u16                                FreeData;                                  // @0x8 size 0x2, align 2
  s8                                 Type;                                      // @0xa size 0x1, align 1
  u8 gap_b[1];
  u16                                UniqueID;                                  // @0xc size 0x2, align 2
  u8 gap_e[2];
  u32                                FreeParam;                                 // @0x10 size 0x4, align 4
};
struct GSaveQuestInvite {                           /* 0x38 big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  u8                                 IsTalk;                                    // @0x34 size 0x1, align 1
  u8                                 FailureReason;                             // @0x35 size 0x1, align 1
  u8                                 Enter;                                     // @0x36 size 0x1, align 1
};
struct s_42da144f {                                 /* 0x90 big, align 2 */
  u16                                ValueArray[72];                            // @0x0 size 0x2, align 2
};
struct GSaveShopShoes {                             /* 0x100 big, align 4 */
  GSaveItemName                      ShopItem[32];                              // @0x0 size 0x8, align 4
};
struct GSaveMuseum {                                /* 0x3404 big, align 4 */
  s_f7aa3e3a                         MuseumLevel;                               // @0x0 size 0x4, align 4
  GSaveDate                          DonationDate[1024];                        // @0x4 size 0x4, align 2
  GSaveItemName                      DonationItem[1024];                        // @0x1004 size 0x8, align 4
  s8                                 DonationUser[1024];                        // @0x3004 size 0x1, align 1
};
struct GSaveAudioInfoV2 {                           /* 0x20 big, align 4 */
  s16                                PlayingAudioMusicID;                       // @0x0 size 0x2, align 2
  s8                                 _749b78c2;                                 // @0x2 size 0x1, align 1
  _44c6787c                          IsShuffle;                                 // @0x3 size 0x1, align 1
  V3f                                PlayingPosition;                           // @0x4 size 0xc, align 4
  s16                                MainUnitIndexX;                            // @0x10 size 0x2, align 2
  s16                                MainUnitIndexZ;                            // @0x12 size 0x2, align 2
  s16                                MainUnitLayer;                             // @0x14 size 0x2, align 2
  s8                                 AudioType;                                 // @0x16 size 0x1, align 1
  s8                                 VolumeType;                                // @0x17 size 0x1, align 1
  f32                                _d910f3fb;                                 // @0x18 size 0x4, align 4
  f32                                Reserve;                                   // @0x1c size 0x4, align 4
};
struct GSaveLandHashValue {                         /* 0x4 big, align 4 */
  u32                                HashValue;                                 // @0x0 size 0x4, align 4
};
struct s_45f23180 {                                 /* 0x400 big, align 4 */
  u32                                Counter[256];                              // @0x0 size 0x4, align 4
};
struct GSavePlayerVillagerAccountTable {            /* 0x240 big, align 8 */
  GSavePlayerVillagerAccount         AccountTable[8];                           // @0x0 size 0x48, align 8
};
struct GSaveWordNickName {                          /* 0x14 big, align 2 */
  s_3f77a59c                         NickName;                                  // @0x0 size 0x14, align 2
};
struct GSaveNpcStockItemData {                      /* 0x2c big, align 4 */
  GSaveItemName                      ItemName;                                  // @0x0 size 0x8, align 4
  GSavePlayerBaseId                  SavePlayerBaseId;                          // @0x8 size 0x1c, align 4
  _e0ab16ca                          GetRoute;                                  // @0x24 size 0x4, align 4
  u8                                 PastDays;                                  // @0x28 size 0x1, align 1
  bool                               ShowFlag;                                  // @0x29 size 0x1, align 1
  bool                               LayoutFlag;                                // @0x2a size 0x1, align 1
};
struct GSaveMainFieldStructure {                    /* 0x398 big, align 4 */
  GSaveStructureData                 StructureList[46];                         // @0x0 size 0x14, align 4
};
struct GSaveObjectSnowManFamily {                   /* 0x1b8 big, align 4 */
  GSaveObjectSnowMan                 CreateSnowManList[4];                      // @0x0 size 0x6c, align 4
  bool                               IsCreateSnowMan;                           // @0x1b0 size 0x1, align 1
  u8 gap_1b1[3];
  s32                                CreateSnowManNum;                          // @0x1b4 size 0x4, align 4
};
struct s_5b202da4 {                                 /* 0x54000 big, align 4 */
  GSaveItemName                      ItemArray[224][192];                       // @0x0 size 0x8, align 4
};
struct s_5f609e7f {                                 /* 0xe2a90 big, align 4 */
  s_80f3284f                         Stock;                                     // @0x0 size 0xe2a90, align 4
};
struct GSaveWordGreeting {                          /* 0x420 big, align 2 */
  s_f6bf402b                         Greeting[11];                              // @0x0 size 0x60, align 2
};
struct GSaveObjectSnowMan {                         /* 0x6c big, align 4 */
  V3f                                HeadPos;                                   // @0x0 size 0xc, align 4
  s32                                HeadStatus;                                // @0xc size 0x4, align 4
  f32                                HeadScaleRate;                             // @0x10 size 0x4, align 4
  V3f                                BodyPos;                                   // @0x14 size 0xc, align 4
  s32                                BodyStatus;                                // @0x20 size 0x4, align 4
  f32                                BodyScaleRate;                             // @0x24 size 0x4, align 4
  GSavePlayerId                      MadePlayerID;                              // @0x28 size 0x38, align 4
  s32                                LapsedTime;                                // @0x60 size 0x4, align 4
  s32                                SnowManType;                               // @0x64 size 0x4, align 4
  s32                                SnowManGrade;                              // @0x68 size 0x4, align 4
};
struct GSaveMailReceiveInfo {                       /* 0x10 big, align 4 */
  u8                                 AnalyzeType;                               // @0x0 size 0x1, align 1
  u8                                 Point;                                     // @0x1 size 0x1, align 1
  u8 gap_2[2];
  GSaveItemName                      Present;                                   // @0x4 size 0x8, align 4
  u16                                CardDesignId;                              // @0xc size 0x2, align 2
  u16                                MelodyId;                                  // @0xe size 0x2, align 2
};
struct GSaveShopKabu {                              /* 0x44 big, align 4 */
  u32                                KaburibaKabuka;                            // @0x0 size 0x4, align 4
  u32                                ShopKabuka[14];                            // @0x4 size 0x4, align 4
  u32                                KabukaPattern;                             // @0x3c size 0x4, align 4
  s32                                FeverStart;                                // @0x40 size 0x4, align 4
};
struct GSaveLandMyDesign {                          /* 0x27e08 big, align 8 */
  GSaveMyDesignNormal                MyDesignNormals[50];                       // @0x0 size 0x2a8, align 8
  GSaveMyDesignPro                   MyDesignPros[50];                          // @0x84d0 size 0x8a8, align 8
  GSaveMyDesignNormal                FlagMyDesign;                              // @0x235a0 size 0x2a8, align 8
  GSaveMyDesignPro                   TailorMyDesigns[8];                        // @0x23848 size 0x8a8, align 8
  s_a92a1233                         ExhibitAccounts[8];                        // @0x27d88 size 0x10, align 8
};
struct GSaveNpcHouse {                              /* 0x1d4 big, align 4 */
  s_9a46020a                         HouseLevel;                                // @0x0 size 0x4, align 4
  s_e09b91b6                         HouseStatus;                               // @0x4 size 0x4, align 4
  u16                                WallUniqueID;                              // @0x8 size 0x2, align 2
  u16                                RoofUniqueID;                              // @0xa size 0x2, align 2
  u16                                DoorUniqueID;                              // @0xc size 0x2, align 2
  u16                                OrderWallUniqueID;                         // @0xe size 0x2, align 2
  u16                                OrderRoofUniqueID;                         // @0x10 size 0x2, align 2
  u16                                OrderDoorUniqueID;                         // @0x12 size 0x2, align 2
  GFtrData                           FtrList[36];                               // @0x14 size 0xc, align 4
  s8                                 NpcList[2];                                // @0x1c4 size 0x1, align 1
  u8 gap_1c6[2];
  GSaveItemName                      DoorDecoItemName;                          // @0x1c8 size 0x8, align 4
  s8                                 BuildPlayer;                               // @0x1d0 size 0x1, align 1
};
struct GSaveLand {                                  /* 0x4fac50 big, align 16 */
  GSaveNpc                           Npc;                                       // @0x0 size 0x1d6d60, align 16
  s_7b602b39                         _d35a9251;                                 // @0x1d6d60 size 0x10, align 16
  GSavePlayerVillagerAccountTable    PlayerVillagerAccountTable;                // @0x1d6d70 size 0x240, align 8
  GSaveWeather                       Weather;                                   // @0x1d6fb0 size 0x14c, align 4
  u8 gap_1d70fc[4];
  GSaveLandTime                      LandTime;                                  // @0x1d7100 size 0xe0, align 8
  GSaveLandId                        LandId;                                    // @0x1d71e0 size 0x1c, align 4
  u8 gap_1d71fc[4];
  GSaveLandMyDesign                  LandMyDesign;                              // @0x1d7200 size 0x27e08, align 8
  GSaveLandStamp                     LandStamp;                                 // @0x1ff008 size 0x2003, align 1
  u8 gap_20100b[1];
  GSaveEventFlagLand                 EventFlag;                                 // @0x20100c size 0x800, align 2
  GSaveMainField                     MainField;                                 // @0x20180c size 0xdaa2c, align 4
  GSavePlayerHouseList               PlayerHouseList;                           // @0x2dc238 size 0x132000, align 4
  GSaveNpcHouseList                  NpcHouseList;                              // @0x40e238 size 0x1248, align 4
  GSaveShop                          Shop;                                      // @0x40f480 size 0x3044, align 4
  GSaveMuseum                        Museum;                                    // @0x4124c4 size 0x3404, align 4
  GSaveVisitorNpc                    VisitorNpc;                                // @0x4158c8 size 0x78, align 4
  GSaveObjectSnowManFamily           SnowManFamily;                             // @0x415940 size 0x1b8, align 4
  GSaveFg                            Fg;                                        // @0x415af8 size 0x928, align 4
  GSaveItemMarketingRoute            ItemMarketingRoute;                        // @0x416420 size 0x2, align 1
  u8 gap_416422[6];
  GSaveVillageMelody                 VillageMelody;                             // @0x416428 size 0x10, align 8
  GSaveOffice                        Office;                                    // @0x416438 size 0x4, align 4
  u8 gap_41643c[4];
  GSaveBulletinBoard                 BulletinBoard;                             // @0x416440 size 0xe0ae8, align 8
  s_b0fdefc8                         RegionLanguage;                            // @0x4f6f28 size 0x4, align 4
  s_75befa81                         CalendarEventRegion;                       // @0x4f6f2c size 0x4, align 4
  GSaveCampSite                      CampSite;                                  // @0x4f6f30 size 0x4, align 4
  GSaveNpcCamp                       NpcCamp;                                   // @0x4f6f34 size 0x114, align 4
  u8                                 AirportThemeColor;                         // @0x4f7048 size 0x1, align 1
  u8 gap_4f7049[1];
  GSaveRumorFavorite                 RumorFavorite;                             // @0x4f704a size 0x2520, align 2
  u8 gap_4f956a[2];
  GSaveMoney                         PublicWorksLoan;                           // @0x4f956c size 0x8, align 4
  GSaveItemName                      PublicWorksName;                           // @0x4f9574 size 0x8, align 4
  GSaveVillageScore                  VillageScore;                              // @0x4f957c size 0x250, align 4
  u8 gap_4f97cc[4];
  GSaveNetLandProfile                NetLandProfile;                            // @0x4f97d0 size 0x38, align 8
  GSaveEventFlagLandTemp             EventFlagTemp;                             // @0x4f9808 size 0x100, align 2
  u8                                 _5d1fcb04[4934];                           // @0x4f9908 size 0x1, align 1
};
struct s_72af0177 {                                 /* 0x100 big, align 2 */
  u16                                ValueArray[128];                           // @0x0 size 0x2, align 2
};
struct s_730a24af {                                 /* 0x200 big, align 2 */
  u16                                ValueArray[256];                           // @0x0 size 0x2, align 2
};
struct GSaveEventFlagLand {                         /* 0x800 big, align 2 */
  s_19abb3ec                         Flags;                                     // @0x0 size 0x800, align 2
};
struct s_7501864a {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct s_75befa81 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveNpcReleaseItemData {                    /* 0x4c big, align 4 */
  GSaveItemName                      ItemName;                                  // @0x0 size 0x8, align 4
  GSavePlayerBaseId                  GetPlayerBaseId;                           // @0x8 size 0x1c, align 4
  GSavePlayerBaseId                  ReleasePlayerBaseId;                       // @0x24 size 0x1c, align 4
  _e0ab16ca                          GetRoute;                                  // @0x40 size 0x4, align 4
  _bb21ce23                          ReleaseType;                               // @0x44 size 0x4, align 4
  u8                                 PastDays;                                  // @0x48 size 0x1, align 1
};
struct GSaveNpcCamp {                               /* 0x114 big, align 4 */
  u16                                VisitNpcID;                                // @0x0 size 0x2, align 2
  u8 gap_2[2];
  GSavePlayerBaseId                  InvitePlayerID;                            // @0x4 size 0x1c, align 4
  s_e96a97e3                         QuestStatus;                               // @0x20 size 0x4, align 4
  GSaveItemName                      QuestFtr;                                  // @0x24 size 0x8, align 4
  GCamperData                        CamperList[8];                             // @0x2c size 0x1c, align 4
  GSaveTime                          LastVisitTime;                             // @0x10c size 0x8, align 2
};
struct GSaveShopCarpet {                            /* 0x28 big, align 4 */
  GSaveItemName                      ShopItem[5];                               // @0x0 size 0x8, align 4
};
struct GSaveBulletinBoard {                         /* 0xe0ae8 big, align 8 */
  GSaveDate                          BuiltDate;                                 // @0x0 size 0x4, align 2
  bool                               _3347e149;                                 // @0x4 size 0x1, align 1
  u8 gap_5[3];
  s_fa4606a3                         Stock;                                     // @0x8 size 0xe0ad8, align 8
  u32                                LatestUniqueId;                            // @0xe0ae0 size 0x4, align 4
};
struct s_80f3284f {                                 /* 0xe2a90 big, align 4 */
  GSaveMailText                      Buffer[100];                               // @0x0 size 0x2440, align 4
  s32                                IndexTable[100];                           // @0xe2900 size 0x4, align 4
};
struct GSaveWordPhrase {                            /* 0x1e4 big, align 2 */
  s_10357ff1                         Phrase[11];                                // @0x0 size 0x2c, align 2
};
struct GSaveCockroach {                             /* 0xe big, align 1 */
  u8                                 CockroachStock;                            // @0x0 size 0x1, align 1
  bool                               _9f0dcc1b[6];                              // @0x1 size 0x1, align 1
  u8                                 _b15ce7cc[6];                              // @0x7 size 0x1, align 1
  s8                                 GenerationCounter;                         // @0xd size 0x1, align 1
};
struct GSavePlayerActivityPack {                    /* 0x6c0 big, align 8 */
  GSavePlayerActivity                PlayerActivity[8];                         // @0x0 size 0xd8, align 8
};
struct s_8bac980d {                                 /* 0x1500 big, align 4 */
  u32                                Bits[1344];                                // @0x0 size 0x4, align 4
};
struct GSaveMemory {                                /* 0x5f0 big, align 4 */
  GSavePlayerId                      PlayerId;                                  // @0x0 size 0x38, align 4
  GSaveEventFlagNpcMemory            EventFlag;                                 // @0x38 size 0x100, align 1
  GSaveWordNickName                  NickName;                                  // @0x138 size 0x14, align 2
  GSaveWordGreeting                  Greeting;                                  // @0x14c size 0x420, align 2
  GSaveDate                          GreetingSetDate;                           // @0x56c size 0x4, align 2
  GSaveMailReceiveInfo               MailReceiveInfoStock[4];                   // @0x570 size 0x10, align 4
  GSaveDate                          LastMailSendDate;                          // @0x5b0 size 0x4, align 2
  GSaveItemName                      ClothesPTops;                              // @0x5b4 size 0x8, align 4
  s16                                _58b5e808;                                 // @0x5bc size 0x2, align 2
  s8                                 ClothesPTarget;                            // @0x5be size 0x1, align 1
  u8 gap_5bf[1];
  GSaveDate                          LastTalkDate;                              // @0x5c0 size 0x4, align 2
  GSaveLandId                        LastTalkLandId;                            // @0x5c4 size 0x1c, align 4
  GSavePlayerHandleName              HandleName;                                // @0x5e0 size 0xa, align 2
  GSaveDate                          HandleNameUpdateDate;                      // @0x5ea size 0x4, align 2
};
struct GSaveShopZakka {                             /* 0x16d0 big, align 4 */
  GSaveItemName                      ShopItem[7][64];                           // @0x0 size 0x8, align 4
  s32                                Stock[7][64];                              // @0xe00 size 0x4, align 4
  bool                               Display[7][64];                            // @0x1500 size 0x1, align 1
  GSaveItemName                      ExpensivePurchase[2];                      // @0x16c0 size 0x8, align 4
};
struct s_91441d11 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveQuest {                                 /* 0x1a8 big, align 4 */
  GSaveTime                          LastReserveTime;                           // @0x0 size 0x8, align 2
  GSaveQuestCatch                    Catch;                                     // @0x8 size 0x3c, align 4
  GSaveQuestLost                     Lost;                                      // @0x44 size 0x3c, align 4
  GSaveQuestDelivery                 Delivery;                                  // @0x80 size 0x40, align 4
  GSaveQuestTreasure                 Treasure;                                  // @0xc0 size 0x3c, align 4
  GSaveQuestVisit                    Visit;                                     // @0xfc size 0x38, align 4
  GSaveQuestInvite                   Invite;                                    // @0x134 size 0x38, align 4
  GSaveQuestSick                     Sick;                                      // @0x16c size 0x3c, align 4
};
struct GSaveWordTasteName {                         /* 0x60 big, align 2 */
  s_e898dfa7                         TasteName;                                 // @0x0 size 0x60, align 2
};
struct GSaveFgOther {                               /* 0x3fc big, align 4 */
  GSavePlayerId                      WateringVisitor[10];                       // @0x0 size 0x38, align 4
  GSaveGrowUpParam                   GrowUpData;                                // @0x230 size 0x4, align 4
  _54ed4ece                          BuildCelebrationHHA;                       // @0x234 size 0x4, align 4
  u32                                _f380f477;                                 // @0x238 size 0x4, align 4
  s16                                EventEasterBuryPlace[128];                 // @0x23c size 0x2, align 2
  s16                                EventEasterTreePlace[96];                  // @0x33c size 0x2, align 2
};
struct s_99f29105 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct s_9a291f01 {                                 /* 0x14 big, align 4 */
  bool                               IsValid;                                   // @0x0 size 0x1, align 1
  bool                               CheckNetworkTime;                          // @0x1 size 0x1, align 1
  bool                               _1a5a16df;                                 // @0x2 size 0x1, align 1
  u8 gap_3[1];
  u32                                Id;                                        // @0x4 size 0x4, align 4
  GSaveDate                          Start;                                     // @0x8 size 0x4, align 2
  GSaveDate                          End;                                       // @0xc size 0x4, align 2
  u32                                Hash;                                      // @0x10 size 0x4, align 4
};
struct s_9a46020a {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveLostItemBox {                           /* 0x280 big, align 4 */
  GSaveItemName                      LostItemArray[80];                         // @0x0 size 0x8, align 4
};
struct s_9aae222a {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSavePlayerActivity {                        /* 0xd8 big, align 8 */
  GSavePlayerId                      PlayerId;                                  // @0x0 size 0x38, align 4
  GSaveEventFlagPlayerActivityParam  EventFlag;                                 // @0x38 size 0x90, align 2
  GSaveDate                          PlayDate;                                  // @0xc8 size 0x4, align 2
  u8 gap_cc[4];
  _010a9a24                          NSAID;                                     // @0xd0 size 0x8, align 8
};
struct GSaveOffice {                                /* 0x4 big, align 4 */
  s_14166c92                         OfficeLevel;                               // @0x0 size 0x4, align 4
};
struct s_9e242739 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveNetLandID {                             /* 0x80 big, align 8 */
  _22afdb4c                          Credential;                                // @0x0 size 0x50, align 8
  _d61099ae                          ProfileReportInfo;                         // @0x50 size 0x28, align 8
  ::nn::settings::LanguageCode       LanguageCode;                              // @0x78 size 0x8, align 1
};
struct s_a92a1233 {                                 /* 0x10 big, align 8 */
  u64                                POPID;                                     // @0x0 size 0x8, align 8
  u64                                NSAID;                                     // @0x8 size 0x8, align 8
};
struct GSaveShop {                                  /* 0x3044 big, align 4 */
  s_9e242739                         ShopLevel;                                 // @0x0 size 0x4, align 4
  GSaveShopCarpet                    ShopCarpet;                                // @0x4 size 0x28, align 4
  GSaveShopTailor                    ShopTailor;                                // @0x2c size 0x12d4, align 4
  GSaveShopShoes                     ShopShoes;                                 // @0x1300 size 0x100, align 4
  GSaveShopZakka                     ShopZakka;                                 // @0x1400 size 0x16d0, align 4
  GSaveShopKabu                      ShopKabu;                                  // @0x2ad0 size 0x44, align 4
  GSaveShopCatalog                   ShopCatalog;                               // @0x2b14 size 0x200, align 4
  u8                                 HatPattern;                                // @0x2d14 size 0x1, align 1
  u8 gap_2d15[3];
  GSaveItemName                      PointExchangeItem[16];                     // @0x2d18 size 0x8, align 4
  GSaveShopGardening                 ShopGardening;                             // @0x2d98 size 0x100, align 4
  GSaveShopGallery                   ShopGallery;                               // @0x2e98 size 0x1ac, align 4
};
struct GSaveQuestSick {                             /* 0x3c big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  GSaveDate                          CureDate;                                  // @0x34 size 0x4, align 2
  u16                                _f04b63da;                                 // @0x38 size 0x2, align 2
  u8                                 OccurRatio;                                // @0x3a size 0x1, align 1
};
struct s_b0fdefc8 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct s_b4120216 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct s_b53802e9 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveMain {                                  /* 0xaced80 big, align 16 */
  GSaveVersion                       Version;                                   // @0x0 size 0x100, align 4
  u8                                 _5d1fcb04[8];                              // @0x100 size 0x1, align 1
  u8 gap_108[8];
  GSaveLand                          Land;                                      // @0x110 size 0x4fac50, align 16
  GSaveLandOther                     LandOther;                                 // @0x4fad60 size 0x5d4020, align 16
};
struct s_b77de181 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveVillageScore {                          /* 0x250 big, align 4 */
  u16                                CollisionNum[18][16];                      // @0x0 size 0x2, align 2
  f32                                NaturalPoint;                              // @0x240 size 0x4, align 4
  f32                                LifePoint;                                 // @0x244 size 0x4, align 4
  s32                                UnitIconNum;                               // @0x248 size 0x4, align 4
  s32                                TreeNum;                                   // @0x24c size 0x4, align 4
};
struct GSaveEventFlagNpcSave {                      /* 0x200 big, align 2 */
  s_730a24af                         Flags;                                     // @0x0 size 0x200, align 2
};
struct GSaveShopCatalog {                           /* 0x200 big, align 4 */
  GSaveItemName                      ShopItem[64];                              // @0x0 size 0x8, align 4
};
struct GSaveEventFlagNpcMemory {                    /* 0x100 big, align 1 */
  s_33a3f71b                         Flags;                                     // @0x0 size 0x100, align 1
};
struct GSaveNpc {                                   /* 0x1d6d60 big, align 16 */
  s_7b602b39                         _d35a9251;                                 // @0x0 size 0x10, align 16
  GSaveNpcVillager                   NpcVillager;                               // @0x10 size 0x1d6d48, align 8
};
struct GSaveRumorFavorite {                         /* 0x2520 big, align 2 */
  GSaveRumorFavoriteData             PlayerFavoriteData[8][11];                 // @0x0 size 0x6c, align 2
};
struct s_c20f88d8 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveQuestTreasure {                         /* 0x3c big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  u8                                 IsFind;                                    // @0x34 size 0x1, align 1
  u8 gap_35[1];
  s16                                BuryUnitX;                                 // @0x36 size 0x2, align 2
  s16                                BuryUnitZ;                                 // @0x38 size 0x2, align 2
};
struct GSaveFieldLandMakingPartsInfo {              /* 0x6 big, align 2 */
  u16                                UniqueID;                                  // @0x0 size 0x2, align 2
  u16                                Variation;                                 // @0x2 size 0x2, align 2
  u8                                 LandMakingAngle;                           // @0x4 size 0x1, align 1
};
struct GSavePlayerHouse {                           /* 0x26400 big, align 4 */
  s_b4120216                         HouseLevel;                                // @0x0 size 0x4, align 4
  u16                                WallUniqueID;                              // @0x4 size 0x2, align 2
  u16                                RoofUniqueID;                              // @0x6 size 0x2, align 2
  u16                                DoorUniqueID;                              // @0x8 size 0x2, align 2
  u16                                OrderWallUniqueID;                         // @0xa size 0x2, align 2
  u16                                OrderRoofUniqueID;                         // @0xc size 0x2, align 2
  u16                                OrderDoorUniqueID;                         // @0xe size 0x2, align 2
  GSaveMoney                         Loan;                                      // @0x10 size 0x8, align 4
  GSaveMoney                         ReturnsLoan;                               // @0x18 size 0x8, align 4
  GSaveEventFlagHouse                EventFlag;                                 // @0x20 size 0x100, align 2
  GSavePlayerHouseRoom               RoomList[6];                               // @0x120 size 0x65c8, align 4
  s8                                 PlayerList[2];                             // @0x263d0 size 0x1, align 1
  u8 gap_263d2[2];
  GSaveItemName                      DoorDecoItemName;                          // @0x263d4 size 0x8, align 4
  _44c6787c                          PlayerHouseFlag;                           // @0x263dc size 0x1, align 1
  u8 gap_263dd[3];
  GSaveItemName                      PostItemName;                              // @0x263e0 size 0x8, align 4
  GSaveItemName                      OrderPostItemName;                         // @0x263e8 size 0x8, align 4
  GSaveCockroach                     Cockroach;                                 // @0x263f0 size 0xe, align 1
};
struct GSaveMainField {                             /* 0xdaa2c big, align 4 */
  s_5b202da4                         ItemLayer0;                                // @0x0 size 0x54000, align 4
  s_5b202da4                         ItemLayer1;                                // @0x54000 size 0x54000, align 4
  s_8bac980d                         ItemSwitch0;                               // @0xa8000 size 0x1500, align 4
  s_8bac980d                         ItemSwitch1;                               // @0xa9500 size 0x1500, align 4
  s_3cec5cfe                         LandMakingMap;                             // @0xaaa00 size 0x24c00, align 2
  GSaveMainFieldStructure            MainFieldStructure;                        // @0xcf600 size 0x398, align 4
  GSaveOutsideField                  OutsideField;                              // @0xcf998 size 0x92, align 2
  u16                                MainFieldParamUniqueID;                    // @0xcfa2a size 0x2, align 2
  s32                                EventPlazaLeftUpX;                         // @0xcfa2c size 0x4, align 4
  s32                                EventPlazaLeftUpZ;                         // @0xcfa30 size 0x4, align 4
  GSaveMyDesignId                    MyDesignMap[112][96];                      // @0xcfa34 size 0x2, align 2
  u32                                MyDesignReserve[5375];                     // @0xd4e34 size 0x4, align 4
  GSaveAudioInfo                     AudioInfo[30];                             // @0xda230 size 0x4, align 2
  u16                                DistantViewUniqueID;                       // @0xda2a8 size 0x2, align 2
  u8 gap_da2aa[2];
  GSaveAudioInfoV2                   AudioInfoV2[60];                           // @0xda2ac size 0x20, align 4
};
struct GSaveLightMemory {                           /* 0x14c big, align 4 */
  GSavePlayerId                      PlayerId;                                  // @0x0 size 0x38, align 4
  GSaveEventFlagNpcMemory            EventFlag;                                 // @0x38 size 0x100, align 1
  GSaveDate                          LastTalkDate;                              // @0x138 size 0x4, align 2
  GSavePlayerHandleName              HandleName;                                // @0x13c size 0xa, align 2
  GSaveDate                          HandleNameUpdateDate;                      // @0x146 size 0x4, align 2
};
struct s_d7e35b57 {                                 /* 0x180920 big, align 8 */
  s_17010e57                         Stock;                                     // @0x0 size 0x180920, align 8
};
struct GSaveNetworkEventData {                      /* 0x280 big, align 4 */
  s_9a291f01                         DataList[32];                              // @0x0 size 0x14, align 4
};
struct GSaveNetLandProfile {                        /* 0x38 big, align 8 */
  _b9a8d05f                          DreamID;                                   // @0x0 size 0x8, align 8
  _d61099ae                          ProfileReportInfo;                         // @0x8 size 0x28, align 8
  ::nn::settings::LanguageCode       LanguageCode;                              // @0x30 size 0x8, align 1
};
struct GSaveVisitorNpc {                            /* 0x78 big, align 4 */
  s_b77de181                         VisitorNpc[7];                             // @0x0 size 0x4, align 4
  V3f                                CreatePos;                                 // @0x1c size 0xc, align 4
  V3f                                CreateBocPos;                              // @0x28 size 0xc, align 4
  bool                               IsNormalLive[7];                           // @0x34 size 0x1, align 1
  bool                               IsBirthdayLive[7];                         // @0x3b size 0x1, align 1
  u8 gap_42[2];
  s_b77de181                         InitSchedule[7];                           // @0x44 size 0x4, align 4
  bool                               _437619d8[14];                             // @0x60 size 0x1, align 1
  u8 gap_6e[2];
  s32                                _e2484556;                                 // @0x70 size 0x4, align 4
  s32                                _753479b1;                                 // @0x74 size 0x4, align 4
};
struct GSavePlayerVillagerAccount {                 /* 0x48 big, align 8 */
  nn::account::Uid                   AccountUid;                                // @0x0 size 0x10, align 8
  GSavePlayerId                      PlayerId;                                  // @0x10 size 0x38, align 4
};
struct s_e09b91b6 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveQuestBase {                             /* 0x34 big, align 4 */
  GSavePlayerBaseId                  PlayerBaseId;                              // @0x0 size 0x1c, align 4
  GSaveTime                          OccurTime;                                 // @0x1c size 0x8, align 2
  GSaveTime                          LimitTime;                                 // @0x24 size 0x8, align 2
  s8                                 ClientNpcVillagerIndex;                    // @0x2c size 0x1, align 1
  s8                                 Type;                                      // @0x2d size 0x1, align 1
  s8                                 Kind;                                      // @0x2e size 0x1, align 1
  s8                                 Step;                                      // @0x2f size 0x1, align 1
  s8                                 LimitType;                                 // @0x30 size 0x1, align 1
};
struct s_e4ba56bd {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveShopGardening {                         /* 0x100 big, align 4 */
  GSaveItemName                      ShopItem[32];                              // @0x0 size 0x8, align 4
};
struct s_e898dfa7 {                                 /* 0x60 big, align 2 */
  char16                             Buffer[48];                                // @0x0 size 0x2, align 2
};
struct GSaveVillageMelody {                         /* 0x10 big, align 8 */
  GSaveVillageMelodyData             MelodyDataList;                            // @0x0 size 0x8, align 8
  u8                                 UsingIndex;                                // @0x8 size 0x1, align 1
  u8                                 ValidMaxIndex;                             // @0x9 size 0x1, align 1
};
struct s_e96a97e3 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveEventFlagLandTemp {                     /* 0x100 big, align 2 */
  s_72af0177                         Flags;                                     // @0x0 size 0x100, align 2
};
struct GFtrData {                                   /* 0xc big, align 4 */
  GSaveItemName                      ItemName;                                  // @0x0 size 0x8, align 4
  s8                                 UnitX;                                     // @0x8 size 0x1, align 1
  s8                                 UnitZ;                                     // @0x9 size 0x1, align 1
  s8                                 Direction;                                 // @0xa size 0x1, align 1
  s8                                 Layer;                                     // @0xb size 0x1, align 1
};
struct s_ec5af5d2 {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSaveFg {                                    /* 0x928 big, align 4 */
  _7b9816fb                          _bc584dbe;                                 // @0x0 size 0x900, align 1
  u16                                SpecialityFruit;                           // @0x900 size 0x2, align 2
  u16                                SisterFruit;                               // @0x902 size 0x2, align 2
  u32                                TreeMoneyInfoList[8];                      // @0x904 size 0x4, align 4
  u8                                 VillageFlower;                             // @0x924 size 0x1, align 1
  u8                                 SpecialityFlower;                          // @0x925 size 0x1, align 1
};
struct GSaveMyDesignHolderList {                    /* 0x64 big, align 1 */
  GSaveMyDesignHolder                NormalHolders[50];                         // @0x0 size 0x1, align 1
  GSaveMyDesignHolder                ProHolders[50];                            // @0x32 size 0x1, align 1
};
struct GSaveEventFlagPlayerActivityParam {          /* 0x90 big, align 2 */
  s_42da144f                         EventFlags;                                // @0x0 size 0x90, align 2
};
struct GSaveNpcArchive {                            /* 0xe8 big, align 4 */
  GSaveDate                          MoveoutDate;                               // @0x0 size 0x4, align 2
  s8                                 MoveoutReason;                             // @0x4 size 0x1, align 1
  u8 gap_5[3];
  GSavePlayerBaseId                  PlayerBaseId[8];                           // @0x8 size 0x1c, align 4
};
struct s_f6bf402b {                                 /* 0x60 big, align 2 */
  char16                             Buffer[48];                                // @0x0 size 0x2, align 2
};
struct s_f7aa3e3a {                                 /* 0x4 big, align 4 */
  s32                                Enum;                                      // @0x0 size 0x4, align 4
};
struct GSavePostStock {                             /* 0x2633d0 big, align 8 */
  s_5f609e7f                         TextMailStock;                             // @0x0 size 0xe2a90, align 4
  s_d7e35b57                         SaveMailStock;                             // @0xe2a90 size 0x180920, align 8
  GSaveTime                          TimeStamp;                                 // @0x2633b0 size 0x8, align 2
  GSaveTime                          DeliveryTime;                              // @0x2633b8 size 0x8, align 2
  bool                               OccasionalFlag;                            // @0x2633c0 size 0x1, align 1
  u8 gap_2633c1[1];
  GSaveTime                          LastDeliveryTime;                          // @0x2633c2 size 0x8, align 2
};
struct GSaveFieldLandMakingMapData {                /* 0xe big, align 2 */
  GSaveFieldLandMakingPartsInfo      PartsInfoList[2];                          // @0x0 size 0x6, align 2
  u8                                 CliffLevel;                                // @0xc size 0x1, align 1
};
struct s_fa4606a3 {                                 /* 0xe0ad8 big, align 8 */
  GSaveBBS                           Buffer[30];                                // @0x0 size 0x77d0, align 8
  s32                                IndexTable[30];                            // @0xe0a60 size 0x4, align 4
};
struct GSaveMyDesignListOrder {                     /* 0x64 big, align 1 */
  s8                                 MyDesignListOrderNormals[50];              // @0x0 size 0x1, align 1
  s8                                 MyDesignListOrderPros[50];                 // @0x32 size 0x1, align 1
};
struct GSaveQuestCatch {                            /* 0x3c big, align 4 */
  GSaveQuestBase                     Base;                                      // @0x0 size 0x34, align 4
  GSaveItemName                      RequestItem;                               // @0x34 size 0x8, align 4
};
struct GSavePlayerHouseList {                       /* 0x132000 big, align 4 */
  GSavePlayerHouse                   HouseList[8];                              // @0x0 size 0x26400, align 4
};
struct GSaveBBS {                                   /* 0x77d0 big, align 8 */
  GSaveDate                          Date;                                      // @0x0 size 0x4, align 2
  s_87bef85e                         Body;                                      // @0x4 size 0x1e0, align 2
  s_341c3493                         Footer;                                    // @0x1e4 size 0x60, align 2
  GSaveHandWritten                   HandWrite;                                 // @0x244 size 0x7538, align 4
  GSavePlayerId                      PlayerId;                                  // @0x777c size 0x38, align 4
  u16                                _5d1fcb04;                                 // @0x77b4 size 0x2, align 2
  u16                                DesignId;                                  // @0x77b6 size 0x2, align 2
  _a8d2a4d4                          PopId;                                     // @0x77b8 size 0x8, align 8
  _010a9a24                          NsaId;                                     // @0x77c0 size 0x8, align 8
  u32                                UniqueId;                                  // @0x77c8 size 0x4, align 4
};
