/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50639
Source Host           : localhost:3306
Source Database       : flask_base_plus

Target Server Type    : MYSQL
Target Server Version : 50639
File Encoding         : 65001

Date: 2018-07-23 15:18:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('35b89fa314c0');

-- ----------------------------
-- Table structure for t_article
-- ----------------------------
DROP TABLE IF EXISTS `t_article`;
CREATE TABLE `t_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `cid` int(11) DEFAULT NULL,
  `cover_pic` varchar(128) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `content` text,
  `is_hot` int(11) DEFAULT '0',
  `is_top` int(11) DEFAULT NULL,
  `view_num` int(11) DEFAULT NULL,
  `description` text,
  `source` varchar(32) DEFAULT NULL,
  `source_site` varchar(32) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_article
-- ----------------------------
INSERT INTO `t_article` VALUES ('22', '二月，10, 2018：美國眾議員希望國會成員披露持有的加密資產', '18', 'http://dev.kerrygao.com/static/upload/1525707959.jpg', '9', '一位對比特幣友好的美國眾議院議員希望國會成員披露他們持有的加密貨幣資產。\r\n                                            <div>\r</div><div>\r在一封送交「眾議院倫理委員會」的請願書中，科羅拉多州眾議員 Jared Polis 主張因為加密貨幣被多個機構視為商品，國會成員應遵循與傳統資產相同的財務披露要求。', '0', '1', '12', '', '來源：coindesk', '圖片： venturebeat', '2018-05-07 23:48:19', '2018-05-08 21:24:13');
INSERT INTO `t_article` VALUES ('24', '区块客新闻：二月，10, 2018：美國眾議員希望國會成員披露持有的加密資產', '18', 'http://dev.kerrygao.com/static/upload/1525708281.jpg', '9', '<p>一位對比特幣友好的美國眾議院議員希望國會成員披露他們持有的加密貨幣資產</p><p><img src=\"http://dev.kerrygao.com/static/upload/1525708310.jpg\" style=\"width: 100%; float: none;\" class=\"\"><br></p><p>在一封送交「眾議院倫理委員會」的請願書中，科羅拉多州眾議員 Jared Polis 主張因為加密貨幣被多個機構視為商品，國會成員應遵循與傳統資產相同的財務披露要求。\r</p><p>\r</p><p>目前，美國兩大金融監管機構──商品期貨交易委員會 (CFTC) 和證管會 (SEC) 都把加密貨幣視為商品。同時，國稅局也要求來自加密貨幣的獲利要遵守聯邦所得稅法的規定。\r</p><p>\r</p><p>Polis 在信中聲稱：</p><blockquote><p>國會成員和相關僱員已被要求回報某些數量的持有資產，包括價值 1,000 美元以上的任何商品。國會成員和僱員應該回報持有的任何虛擬貨幣，就如同他們會回報黃金之類的其他商品。</p><p>Polis 是加密貨幣擁護者，長久以來一直在推動加密貨幣的正規化，而這份請願書是他最新的努力。</p><p>Polis 從 2014 年開始顯露出他對加密貨幣的友好態度，當時一位參議員 Joe Manchin 寫了一封公開信給聯邦監管機構，呼籲徹底禁止比特幣。</p><p>Polis 就這件事做出了回擊，他發出一封信給同一個機構要求禁用美元。他在信中表達了對美元的擔憂：「包括大面額鈔票在內的美鈔交易目前是不受監管的，且允許使用者用來參與非法活動」，這幾乎和 Manchin 對比特幣的描述一模一樣。</p><p>此外，Polis 也是美國第一批接受比特幣捐贈進行競選活動的政治家之一。他在去年 9 月更提出一項法案，希望為 600 美元以下的加密貨幣支付提供 免稅政策 。</p></blockquote><p>\n                                            </p>', '0', '1', '8', '磊哥，点进来了解 一下~', 'coindesk 图片：venturebeat', 'coindesk.com', '2018-05-07 23:53:41', '2018-06-16 22:19:20');
INSERT INTO `t_article` VALUES ('28', '五月 7, 2018 華爾街資深分析師：現在並非買入比特幣時機', '17', 'http://dev.kerrygao.com/static/upload/1525786049.jpg', '9', '投资分析公司 Data Trek 共同创办人、华尔街资深分析师 Nicholas Colas 在美国时间週五接受 CNBC 访谈时表示：「现在不是买入比特币的好时机。」 ', '0', '1', '8', '投资分析公司 Data Trek 共同创办人、华尔街资深分析师 Nicholas Colas 在美国时间週五接受 CNBC 访谈时表示：「现在不是买入比特币的好时机。」', '', '', '2018-05-08 21:27:42', '2018-05-16 23:49:14');
INSERT INTO `t_article` VALUES ('29', 'EOS 发起公司 Block.one 挖到澳洲联邦银行前 CFO 出任总裁兼 COO', '18', 'http://dev.kerrygao.com/static/upload/1526396060.jpg', '9', 'Jesudason 将取得 block.one 公司董事席位，负责扩大公司的全球化运营。他当天稍早从 CBA 辞职，今年稍晚将入职 block.one 公司。CBA 是位列全球前 12 位的大银行，市值达到 1,250 亿澳元。EOS 是市值排名前五的加密货币，市值约为 124 亿美元。\n                                            ', '0', '0', '2', 'EOS 背后的 block.one 公司 5 月 14 日发布公告称，任命澳洲联邦银行 CBA 前首席财务官 CFO Rob Jesudason 出任集团总裁兼首席运营官 COO。', '', '', '2018-05-15 22:54:36', '2018-05-15 22:58:40');
INSERT INTO `t_article` VALUES ('30', '五年内大企业能否采纳区块链技术？ Jimmy Song 与 Joseph Lubin 开出赌盘', '18', 'http://dev.kerrygao.com/static/upload/1526396183.jpg', '9', '在比特币世界最大盛会上，比特币开发者 Jimmy Song 愿意接住以太坊联合创始人 Joseph Lubin 开出的赌盘，他坚持没有加密货币的去中心化账本在五年内不会有吸引眼球的大企业客户。\r\n                                            <div>\r</div><div>Lubin 表示，愿意与 Song 对赌「任何数量的比特币」，去中心化账本五年内在大企业会得到有意义的应用。据福布斯杂志，Lubin 的资产约在 10-15 亿美元间。 长期对区块链持怀疑态度的 Song 的资产情况不明。</div>', '0', '1', '1', '在比特币世界最大盛会上，比特币开发者 Jimmy Song 愿意接住以太坊联合创始人 Joseph Lubin 开出的赌盘，他坚持没有加密货币的去中心化账本在五年内不会有吸引眼球的大企业客户。', '', '', '2018-05-15 22:56:32', '2018-05-17 17:28:52');
INSERT INTO `t_article` VALUES ('41', '俄聯儲投資銀行為電信龍頭啟動區塊鏈債券交易', '19', 'http://dev.kerrygao.com/static/upload/1526825799.jpg', '1', '<p style=\"box-sizing: inh_: justify;\">(16 日) 俄聯儲投資銀行 (SBERBANK CIB) 發佈該國首件區塊鏈商業債券應用， 經俄羅斯國家結算存管所 (NSD) 核准，讓該國電信業領導品牌 MTS 透過智能合約，發行以盧布計價的商業債券。</p><p style=\"box-sizing: inh_: justify;\">SBERBANK CIB 隸屬於俄羅斯聯邦儲備銀行 (SBERBANK)，主要業務為證券交易與銷售、投資銀行、私人資產管理、零售與其他種類投資。由於 NSD 允許使用區塊鏈 Hyperledger Fabric1.1 進行交易，因此 SBERBANK CIB 籌備發行了 MTS 債券，共值 7,500 億盧布 (約 1200 萬美金)，六個月到期。</p><p style=\"box-sizing: inh_: justify;\">據 SBERBANK CIB 定義，商業債券在場外交易市場中，是一種私下交易且無擔保的固定收入證券。透過區塊鏈能夠建構一個完整交付與付款結算模式，這可以使證券與金流能同時間轉移。</p><blockquote style=\"box-sizing: inh_d-color: rgb(255, 255, 255);\"><p style=\"box-sizing: inh_e;\">SBERBANK CIB 在公告中表示：從債券發行方的配售到履行投資者權益 (包含：盧布的支付)，都可以用基於區塊鏈的智能合約完成完整的證券生命週期。</p></blockquote><p style=\"box-sizing: inh_: justify;\">發行方、投資者與中央存款機構都透過去中心化平台完成交易，作業過程帳戶資訊都保持機密，並且符合俄羅斯法律。也由於此系統是透過數位資產進行操作，債券的配售、流通與過程紀錄都是高度透明的。每個參與者都能在線上追蹤交易狀況與查看交易文件。</p><p style=\"box-sizing: inh_: justify;\">三方參與者都對這項債券發行的創新計畫做出評論：</p><ul style=\"box-sizing: inh_e; color: rgb(85, 85, 85);\"><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square; text-align: justify;\">SBERBANK 的高級副總裁兼 CIB 負責人 Igor Bulantsev 表示：「SBERBANK 銀行在俄羅斯金融科技與數位創新處於領先地位。這次 MTS 的債券發行不僅應證了區塊鏈平台的可靠、效率與安全。除了點出證券交易的複雜結構，同時也展示這項技術有助於發展俄羅斯的數位經濟實力。」</li><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square; text-align: justify;\">MTS 副總裁 Andrey Kamensky 表示：「MTS 將繼續使用區塊鏈，尤其在金融市場部分。因為它增加了透明度，可以獲得市場投資者的信任，也優化了成本。」</li><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square; text-align: justify;\">NSD 主席 Eddie Astanin 表示：「我們的最終目標是與市場的領導者一起創建紀錄數位資產的基礎建設。這是將機構投資者推向市場，並確保能有動態成長與增加資本總額的第一步。」</li></ul>', '1', '1', '2', '(16 日) 俄聯儲投資銀行 (SBERBANK CIB) 發佈該國首件區塊鏈商業債券應用， 經俄羅斯國家結算存管所 (NSD) 核准，讓該國電信業領導品牌 MTS 透過智能合約，發行以盧布計價的商業債券。', 'sberbank-cib', '', '2018-05-20 22:17:04', '2018-07-10 21:02:17');
INSERT INTO `t_article` VALUES ('42', '防範 ICO 詐騙 SEC 利用假募資網站教育消費者', '19', 'http://dev.kerrygao.com/static/upload/1526826025.jpg', '9', '<p style=\"box-sizing: inh_: justify;\">美國證管會 (SEC) 為了教育 ICO 投資民眾出奇招，在本週三 (15) 推出了一個假的 ICO 網站-HoweyCoins，在內容極盡吹捧、看似完美的項目之後，試圖想要投資的民眾將會被轉向這個監管機構的教育內容。「言教不如身教」、「坐而言不如起而行」，這些話反倒在西方的消費者教育之中體現。</p><p style=\"box-sizing: inh_: justify;\"><a style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(205, 72, 60); outline-style: initial; outline-width: 0px; transition: all 0.2s ease;\" href=\"https://www.howeycoins.com/index.html\" target=\"_blank\" rel=\"external noopener noreferrer\">HoweyCoins</a>&nbsp;官網就是一個典型的 ICO 網站，它有著持續倒數的時間，然後提醒著你代幣優惠即將結束。這個假的旅遊區塊鏈代幣項目跟其他 ICO 項目並沒有兩樣，它還有 8 頁的&nbsp;<a style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(205, 72, 60); outline-style: initial; outline-width: 0px; transition: all 0.2s ease;\" href=\"https://www.howeycoins.com/files/howeycoin_white_paper.pdf\" target=\"_blank\" rel=\"external noopener noreferrer\">白皮書</a>&nbsp;，告訴你現在的產業有多少限制，區塊鏈又能帶來多少榮景。若你是個自認謹慎的投資者，HoweyCoins 也有了你想要的所有條件：於美國政府機關註冊在案、將在 SEC 監管下交易所上市、可跟現有的旅遊獎勵機制整合、能夠做幣幣交易與法幣兌現… 等等。</p><div style=\"box-sizing: inh_ter; color: rgb(85, 85, 85); width: 530px;\"><img src=\"http://cdn.blockcast.it/wp-content/uploads/2018/05/17121254/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7-2018-05-17-12.08.28.png\" style=\"box-sizing: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; max-width: 100%; height: auto; box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 3px;\" width=\"520\" alt=\"\" height=\"259\" /><p style=\"box-sizing: inh_e; color: rgb(153, 153, 153);\">HoweyCoins 的 ICO 募資網站，跟市場上大同小異</p></div><p style=\"box-sizing: inh_: justify;\">不過，當你按下「現在就購買！(75 折優惠)」時 (註：一旁還寫 6 月 1 日前投資，可以拿到雙倍。)，美夢即將被敲醒，消費者會被引導到 SEC 的消費者保護教育網站，裡頭盡是忠言逆耳的投資警示。</p><div style=\"box-sizing: inh_ter; color: rgb(85, 85, 85); width: 483px;\"><img src=\"http://cdn.blockcast.it/wp-content/uploads/2018/05/17121315/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7-2018-05-17-12.11.56.png\" style=\"box-sizing: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; max-width: 100%; height: auto; box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 3px;\" width=\"473\" alt=\"\" height=\"293\" /><p style=\"box-sizing: inh_e; color: rgb(153, 153, 153);\">按下投資購買之後，就會導向 SEC 消費者教育網站</p></div><blockquote style=\"box-sizing: inh_d-color: rgb(255, 255, 255);\"><p style=\"box-sizing: inh_e;\">「如果你回應了這樣一個投資機會，你可能已經被詐騙了。HoweyCoins 完全是假的！」按下 HoweyCoins 的購買連結之後，就會看到這麼一個明顯的標語。</p></blockquote><p style=\"box-sizing: inh_e; color: rgb(85, 85, 85);\">SEC 的消費者教育網站內容提示以下幾點：</p><ul style=\"box-sizing: inh_: justify;\"><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square;\">投資警示 (一)：聲稱保證高回報-大部分的詐騙項目，都會花許多時間來說服消費者有多少回報，而絕不容錯過。</li><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square;\">投資警示 (二)：名人背書-明星或運動員等名人代言，不代表那就是好的投資案，這不是一個好的判斷依據。</li><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square;\">投資警示 (三)：合乎 SEC 規範的交易所-儘管許多平台聲稱用嚴格標準來挑選上市幣種，但是 SEC 並未審查這些標準或是平台的幣種。</li><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square;\">投資警示 (四)：可用信用卡來支付投資-投資人應該了解，大多數的合法註冊投資公司並不允許客戶以信用卡來購買投資。</li><li style=\"box-sizing: inherit; margin-bottom: 0.5em; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; list-style-type: square;\">投資警示 (五)：炒高再倒貨詐騙-詐騙者常會透過散佈虛假或是誤導訊息引發瘋狂的購買行為，先是哄抬代幣價格，再以浮誇的價格出售自己的持有代幣。一旦詐欺者停止炒作，投資者將會因價格大幅下跌而賠錢。</li></ul><p style=\"box-sizing: inh_: justify;\">這個假的 ICO 網站，就是將許多經典的詐騙手法加總在一起，再藉機教育 ICO 投資者們，莫因這些誘因而上當受騙。</p><p style=\"box-sizing: inh_: justify;\">投資是一種自由行為，傳統投資市場中受到監管的投資方式，就已經是充滿詐騙與炒作，投資人無論在知情或不知情之下，都可能受到利誘而甘冒詐騙風險。加密貨幣給與人們更無限制的投資自由，跨國且快速、高回報，這種前所未見的風潮讓募資方與投資人都陷入瘋狂。可怕的是，詐騙集團、傳銷、資金盤也打著加密貨幣的名號紛紛入場，你或許進入了一個新的領域，但這裡還是充滿著傳統的騙局。畢竟，欺騙也是人類的本性，在我們將信任交給區塊鏈之前，會不會就在騙局的狂歡之中，提前結束這場烏托邦式的幻想？</p><p style=\"box-sizing: inh_e; color: rgb(85, 85, 85);\">註：Howey 一字，可指向「Howey Test」。美國最高法院依此來測試一項投資合同是否能視為債券，其中條件為：揭露公司的財務狀況以及業務目的、對於投資的債券有詳細描述、具有公司的管理營運資訊、公司具有獨立會計師認證的財務證明。</p>', '1', '0', '14', '美國證管會 (SEC) 為了教育 ICO 投資民眾出奇招，在本週三 (15) 推出了一個假的 ICO 網站-HoweyCoins，在內容極盡吹捧、看似完美的項目之後，試圖想要投資的民眾將會被轉向這個監管機構的教育內容。「言教不如身教」、「坐而言不如起而行」，這些話反倒在西方的消費者教育之中體現。', 'howeycoins', '', '2018-05-20 22:21:01', '2018-07-16 17:02:10');
INSERT INTO `t_article` VALUES ('43', '日本國產 Monacoin 遭受自私挖礦攻擊 損失逾 9 萬美元價值11', '22', 'http://127.0.0.1:5000/static/upload/1532317310.png', '1', '<p style=\"box-sizing: inh_: justify;\">日本國產的加密貨幣「Monacoin」(モナコイン) 疑因遭到被稱作 Block withholding attack(中譯：扣塊攻擊) 或稱 Selfish Mining(中譯：自私挖礦) 的攻擊，在 5 月 13-15 日間海外交易所 Livecoin 傳損失約 9 萬美元。</p><p style=\"box-sizing: inh_: justify;\">這場攻擊可能源於自私挖礦，某一礦工在發現了一個新塊之後，並不向其他礦工廣播此一區塊。因此獲得發現下一個區塊的時間優勢，這個秘密挖礦的礦工則可以比其他人都更有效率地創建更長的鏈。</p><p style=\"box-sizing: inh_: justify;\">在多數的區塊鏈協議所訂定的標準之中，具有越多區塊的鏈，在網路中就越被視為正確的鏈，因為它有最多的工作證明。也就是，當自私挖礦的礦工將他們挖出較長的鏈公開，它將會使得其他在自私挖礦期間的其他礦工發現的塊無效。</p><p style=\"box-sizing: inh_: justify;\">自私挖礦攻擊的可能出現兩種結果，一種只是純粹的破壞行為，讓自私挖礦期間其他礦工的成果白費，另一種則是自私挖礦的礦工，刻意在即將被銷毀的區塊上進行交易，那付出的費用就會被視為無效。</p><p style=\"box-sizing: inh_: justify;\">目前看起來攻擊者以半年時間，嘗試利用 Monacoin 調整難度方式的弱點發出攻擊。</p><p style=\"box-sizing: inh_: justify;\">截至 5 月 19 日，攻擊事件不再發生，但大多數的交易所都已暫停 Monacoin 的存款，他們也正在進行修復以防止未來的類似攻擊。目前在 Monacoin 錢包裡的存款都是安全的。33333333</p><p style=\"box-sizing: inh_: justify;\">目前所有區塊鏈，包括比特幣，都在不斷調整挖礦難度，讓它變得不會太難也不會太容易。不過像是比特幣的這種大規模的區塊鏈網路，事實上就很難被攻擊。</p><p style=\"box-sizing: inh_: justify;\">像是 Monacoin 它的規模或算法導致其變得脆弱，同樣來說，其他的加密貨幣也可能遭受相同的攻擊。許多加密社區都在透過這個事件，是如何發生攻擊，看看可以學到什麼經驗，從而加強自己的網路。</p><hr style=\"box-sizing: inherit; border-top: 0px; background: rgb(238, 238, 238); height: 3px; margin-top: 30px; margin-bottom: 30px; color: rgb(85, 85, 85); font-family: Roboto, Arial, sans-serif; font-size: 17px;\" /><p style=\"box-sizing: inh_e; color: rgb(85, 85, 85);\"><span style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;\">區塊客致力於發掘和整理各種與區塊鏈技術有關的內容，只要與區塊鏈或區塊客網站有關的合作和／或建議，我們都非常歡迎。請您發電郵至</span>&nbsp;<span style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;\">&nbsp;<a style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(205, 72, 60); outline-style: initial; outline-width: 0px; transition: all 0.2s ease;\" href=\"http://mailto:info@blockcast.it\" target=\"_blank\"><span style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;\"></span></a><a style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(205, 72, 60); outline-style: initial; outline-width: 0px; transition: all 0.2s ease;\" href=\"http://mailto:info@blockcast.it\" target=\"_blank\">info@blockcast.it</a></span>&nbsp;<span style=\"box-sizing: inherit; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;\">與我們聯繫。</span></p>', '1', '0', '11', '日本國產的加密貨幣「Monacoin」(モナコイン) 疑因遭到被稱作 Block withholding attack(中譯：扣塊攻擊) 或稱 Selfish Mining(中譯：自私挖礦) 的攻擊，在 5 月 13-15 日間海外交易所 Livecoin 傳損失約 9 萬美元。222', 'CCN', '12', '2018-05-24 11:20:00', '2018-07-23 11:42:11');

-- ----------------------------
-- Table structure for t_article_category
-- ----------------------------
DROP TABLE IF EXISTS `t_article_category`;
CREATE TABLE `t_article_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT '0',
  `name` varchar(32) NOT NULL,
  `cover_pic` varchar(128) DEFAULT NULL,
  `description` varchar(128) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_article_category
-- ----------------------------
INSERT INTO `t_article_category` VALUES ('19', '0', '比特资讯', null, '比特资讯', '1', '2018-03-19 18:30:34', '2018-03-19 18:30:34');
INSERT INTO `t_article_category` VALUES ('22', '0', '热门新闻', null, '热门新闻', '1', '2018-05-16 23:42:40', '2018-05-20 22:26:55');

-- ----------------------------
-- Table structure for t_article_comment
-- ----------------------------
DROP TABLE IF EXISTS `t_article_comment`;
CREATE TABLE `t_article_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `customer_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `laud_no` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_article_comment
-- ----------------------------

-- ----------------------------
-- Table structure for t_article_keywords
-- ----------------------------
DROP TABLE IF EXISTS `t_article_keywords`;
CREATE TABLE `t_article_keywords` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `font_color` varchar(20) NOT NULL,
  `background_color` varchar(20) NOT NULL,
  `border_color` varchar(20) NOT NULL,
  `hot_no` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_article_keywords
-- ----------------------------
INSERT INTO `t_article_keywords` VALUES ('1', '1212', '#000000', '#000000', '#000000', '0', '2018-07-23 11:41:25', '2018-07-23 11:41:25');
INSERT INTO `t_article_keywords` VALUES ('2', '333', '#000000', '#000000', '#000000', '0', '2018-07-23 11:41:28', '2018-07-23 11:41:28');

-- ----------------------------
-- Table structure for t_article_keyword_relation
-- ----------------------------
DROP TABLE IF EXISTS `t_article_keyword_relation`;
CREATE TABLE `t_article_keyword_relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `keyword_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_article_keyword_relation
-- ----------------------------
INSERT INTO `t_article_keyword_relation` VALUES ('1', '43', '1');
INSERT INTO `t_article_keyword_relation` VALUES ('2', '44', '1');

-- ----------------------------
-- Table structure for t_banner_cfg
-- ----------------------------
DROP TABLE IF EXISTS `t_banner_cfg`;
CREATE TABLE `t_banner_cfg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `description` text,
  `img_url` varchar(150) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_banner_cfg
-- ----------------------------
INSERT INTO `t_banner_cfg` VALUES ('2', '12', '121', '1212', 'http://127.0.0.1:5000/static/upload/1532317474.png', '1', '2018-07-23 11:44:38', '2018-07-23 11:44:38');

-- ----------------------------
-- Table structure for t_friend_link
-- ----------------------------
DROP TABLE IF EXISTS `t_friend_link`;
CREATE TABLE `t_friend_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `link_type` varchar(10) DEFAULT 'link_type',
  `link_icon` varchar(128) DEFAULT NULL,
  `link_href` varchar(128) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of t_friend_link
-- ----------------------------
INSERT INTO `t_friend_link` VALUES ('46', '金色财经', 'pic_link', 'http://dev.kerrygao.com/static/upload/1529813997.png', 'http://www.jinse.com/', '1', '2018-06-24 12:20:16', '2018-06-24 12:20:16');

-- ----------------------------
-- Table structure for t_menu_auth
-- ----------------------------
DROP TABLE IF EXISTS `t_menu_auth`;
CREATE TABLE `t_menu_auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `method` varchar(50) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `icon` varchar(30) DEFAULT NULL,
  `is_show` int(11) DEFAULT '1' COMMENT '????',
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1982 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_menu_auth
-- ----------------------------
INSERT INTO `t_menu_auth` VALUES ('1', '0', '系统首页', 'admin/index', '0', '1', 'ti-home', '1', '2017-11-06 14:19:02', '2017-11-09 14:38:10');
INSERT INTO `t_menu_auth` VALUES ('2', '0', '权限菜单', 'admin/menu-auth', '0', '3', 'md md-menu', '1', '2017-11-06 14:20:37', '2018-03-08 14:55:10');
INSERT INTO `t_menu_auth` VALUES ('3', '2', '添加菜单', 'admin/menu-add', '1', '1', '', '0', '2017-11-06 14:22:13', '2018-02-06 09:57:37');
INSERT INTO `t_menu_auth` VALUES ('4', '2', '编辑菜单', 'admin/menu-edit', '1', '1', '', '0', '2017-11-06 14:23:17', '2018-02-06 09:57:43');
INSERT INTO `t_menu_auth` VALUES ('5', '0', '角色管理', 'admin/role-manage', '0', '4', 'fa fa-users', '1', '2017-11-06 14:24:33', '2018-03-08 14:55:18');
INSERT INTO `t_menu_auth` VALUES ('6', '5', '用户管理', 'admin/user-manage', '0', '1', '', '1', '2017-11-06 14:25:17', '2017-11-06 14:25:20');
INSERT INTO `t_menu_auth` VALUES ('7', '5', '用户分组', 'admin/user-group-manage', '0', '2', '', '1', '2017-11-06 14:25:51', '2017-11-06 14:25:53');
INSERT INTO `t_menu_auth` VALUES ('74', '2', '删除菜单', 'admin/menu-del', '1', '1', '', '0', '2017-11-09 11:12:26', '2018-02-06 09:57:48');
INSERT INTO `t_menu_auth` VALUES ('75', '6', '添加用户', 'admin/user-add', '1', '1', '', '0', '2017-11-09 11:14:26', '2018-02-06 09:58:02');
INSERT INTO `t_menu_auth` VALUES ('76', '6', '编辑用户', 'admin/user-edit', '1', '1', '', '0', '2017-11-09 11:15:48', '2018-02-06 09:58:08');
INSERT INTO `t_menu_auth` VALUES ('77', '6', '删除用户', 'admin/user-del', '1', '1', '', '0', '2017-11-09 11:16:31', '2018-02-06 09:58:15');
INSERT INTO `t_menu_auth` VALUES ('78', '7', '添加分组', 'admin/group-add', '1', '1', '', '0', '2017-11-09 11:17:36', '2018-02-06 09:58:23');
INSERT INTO `t_menu_auth` VALUES ('79', '7', '编辑分组', 'admin/group-edit', '1', '1', '', '0', '2017-11-09 11:18:04', '2018-02-06 09:58:30');
INSERT INTO `t_menu_auth` VALUES ('80', '7', '删除分组', 'admin/group-del', '1', '1', '', '0', '2017-11-09 11:19:00', '2018-02-06 09:58:35');
INSERT INTO `t_menu_auth` VALUES ('197', '0', '系统配置', 'admin/system_base_cfg', '0', '2', 'fa fa-cog fa-fw', '1', '2018-03-08 14:53:49', '2018-03-08 14:54:41');
INSERT INTO `t_menu_auth` VALUES ('198', '0', '文章管理', 'admin/article_manage', '0', '5', 'ti-files', '1', '2018-03-13 15:16:19', '2018-03-13 20:43:10');
INSERT INTO `t_menu_auth` VALUES ('199', '203', '添加文章', 'admin/article_add', '0', '1', '', '0', '2018-03-13 17:11:51', '2018-03-13 17:14:45');
INSERT INTO `t_menu_auth` VALUES ('202', '203', '编辑文章', 'admin/article_edit', '0', '2', '', '0', '2018-03-13 17:17:33', '2018-03-13 17:17:33');
INSERT INTO `t_menu_auth` VALUES ('203', '198', '文章列表', 'admin/article_list', '0', '2', '', '1', '2018-03-13 20:43:38', '2018-03-13 20:44:58');
INSERT INTO `t_menu_auth` VALUES ('204', '198', '文章分类', 'admin/article_category_list', '0', '1', '', '1', '2018-03-13 20:44:39', '2018-03-13 20:44:39');
INSERT INTO `t_menu_auth` VALUES ('205', '198', '文章关键词', 'admin/article_keywords_list', '0', '2', '', '1', '2018-03-15 14:50:23', '2018-03-15 14:51:15');
INSERT INTO `t_menu_auth` VALUES ('217', '0', '友情链接	', 'admin/friend-link', '0', '20', 'glyphicon glyphicon-link', '1', '2018-05-29 17:35:26', '2018-05-29 17:36:01');

-- ----------------------------
-- Table structure for t_operation_log
-- ----------------------------
DROP TABLE IF EXISTS `t_operation_log`;
CREATE TABLE `t_operation_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL,
  `operation` varchar(32) DEFAULT NULL,
  `operate_desc` varchar(1024) DEFAULT NULL,
  `login_ip` varchar(32) DEFAULT NULL,
  `request` varchar(500) DEFAULT NULL,
  `response` varchar(500) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_operation_log
-- ----------------------------
INSERT INTO `t_operation_log` VALUES ('1', 'admin', 'login', '用户登陆', '127.0.0.1', '{\'username\': [u\'admin\'], \'remember_me\': [u\'y\'], \'password\': [u\'admin\'], \'submit\': [u\'\\u767b\\u9646\'], \'next\': [u\'/admin/\']}', 'current_user:admin', '2018-06-06 16:02:35', '2018-06-06 16:02:35');
INSERT INTO `t_operation_log` VALUES ('2', 'admin', 'add_menu', '添加菜单', '127.0.0.1', '{\'sort\': [u\'1\'], \'menu_name\': [u\'\\u5b66\\u751f\\u7ba1\\u7406\'], \'is_show\': [u\'1\'], \'parent_id\': [u\'0\'], \'type\': [u\'0\'], \'method\': [u\'admin/studen-list\'], \'icon\': [u\'ion-person\']}', 'method:admin/studen-list', '2018-06-06 16:09:53', '2018-06-06 16:09:53');
INSERT INTO `t_operation_log` VALUES ('3', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'10\'], \'method\': [u\'admin/studen-list\'], \'menu_name\': [u\'\\u5b66\\u751f\\u7ba1\\u7406\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'218\'], \'icon\': [u\'ion-person\']}', 'method:admin/studen-list', '2018-06-06 16:10:35', '2018-06-06 16:10:35');
INSERT INTO `t_operation_log` VALUES ('4', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'10\'], \'method\': [u\'admin/student-list\'], \'menu_name\': [u\'\\u5b66\\u751f\\u7ba1\\u7406\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'218\'], \'icon\': [u\'ion-person\']}', 'method:admin/student-list', '2018-06-06 16:25:31', '2018-06-06 16:25:31');
INSERT INTO `t_operation_log` VALUES ('5', 'admin', 'add_menu', '添加菜单', '127.0.0.1', '{\'sort\': [u\'12\'], \'menu_name\': [u\'\\u5bdd\\u5ba4\\u5e8a\\u4f4d\'], \'is_show\': [u\'1\'], \'parent_id\': [u\'0\'], \'type\': [u\'0\'], \'method\': [u\'admin/bed-info\'], \'icon\': [u\'md md-playlist-add\']}', 'method:admin/bed-info', '2018-06-08 13:47:45', '2018-06-08 13:47:45');
INSERT INTO `t_operation_log` VALUES ('6', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'12\'], \'method\': [u\'admin/bed-info-list\'], \'menu_name\': [u\'\\u5bdd\\u5ba4\\u5e8a\\u4f4d\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'219\'], \'icon\': [u\'md md-playlist-add\']}', 'method:admin/bed-info-list', '2018-06-08 14:03:07', '2018-06-08 14:03:07');
INSERT INTO `t_operation_log` VALUES ('7', 'admin', 'add_menu', '添加菜单', '127.0.0.1', '{\'sort\': [u\'1\'], \'menu_name\': [u\'\\u5bdd\\u5ba4\\u5206\\u914d\'], \'is_show\': [u\'1\'], \'parent_id\': [u\'0\'], \'type\': [u\'0\'], \'method\': [u\'admin/dorm-rule\'], \'icon\': [u\'glyphicon glyphicon-retweet\']}', 'method:admin/dorm-rule', '2018-06-12 14:10:56', '2018-06-12 14:10:56');
INSERT INTO `t_operation_log` VALUES ('8', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'13\'], \'method\': [u\'admin/dorm-rule\'], \'menu_name\': [u\'\\u5206\\u914d\\u89c4\\u5219\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'220\'], \'icon\': [u\'glyphicon glyphicon-retweet\']}', 'method:admin/dorm-rule', '2018-06-12 14:11:35', '2018-06-12 14:11:35');
INSERT INTO `t_operation_log` VALUES ('9', 'admin', 'login', '用户登陆', '127.0.0.1', '{\'username\': [u\'admin\'], \'password\': [u\'admin\'], \'submit\': [u\'\\u767b\\u9646\'], \'next\': [u\'/admin/menu-auth\']}', 'current_user:admin', '2018-06-14 14:27:30', '2018-06-14 14:27:30');
INSERT INTO `t_operation_log` VALUES ('10', 'admin', 'add_menu', '添加菜单', '127.0.0.1', '{\'sort\': [u\'13\'], \'menu_name\': [u\'\\u7f34\\u8d39\\u7edf\\u8ba1\'], \'is_show\': [u\'1\'], \'parent_id\': [u\'0\'], \'type\': [u\'0\'], \'method\': [u\'admin/payment_statistics\'], \'icon\': [u\'ti-bar-chart\']}', 'method:admin/payment_statistics', '2018-06-14 14:34:03', '2018-06-14 14:34:03');
INSERT INTO `t_operation_log` VALUES ('11', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'13\'], \'method\': [u\'admin/payment-statistics\'], \'menu_name\': [u\'\\u7f34\\u8d39\\u7edf\\u8ba1\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'221\'], \'icon\': [u\'ti-bar-chart\']}', 'method:admin/payment-statistics', '2018-06-14 14:44:22', '2018-06-14 14:44:22');
INSERT INTO `t_operation_log` VALUES ('12', 'admin', 'add_menu', '添加菜单', '127.0.0.1', '{\'sort\': [u\'1\'], \'menu_name\': [u\'\\u9662\\u7cfb\\u7edf\\u8ba1\'], \'is_show\': [u\'1\'], \'parent_id\': [u\'0\'], \'type\': [u\'0\'], \'method\': [u\'admin/academy-statistics\'], \'icon\': [u\'md md-account-balance\']}', 'method:admin/academy-statistics', '2018-06-19 10:16:04', '2018-06-19 10:16:04');
INSERT INTO `t_operation_log` VALUES ('13', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'15\'], \'method\': [u\'admin/academy-statistics\'], \'menu_name\': [u\'\\u9662\\u7cfb\\u7edf\\u8ba1\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'222\'], \'icon\': [u\'md md-account-balance\']}', 'method:admin/academy-statistics', '2018-06-19 10:16:15', '2018-06-19 10:16:15');
INSERT INTO `t_operation_log` VALUES ('14', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'14\'], \'method\': [u\'admin/academy-statistics\'], \'menu_name\': [u\'\\u9662\\u7cfb\\u7edf\\u8ba1\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'222\'], \'icon\': [u\'md md-account-balance\']}', 'method:admin/academy-statistics', '2018-06-19 10:16:25', '2018-06-19 10:16:25');
INSERT INTO `t_operation_log` VALUES ('15', 'admin', 'login', '用户登陆', '192.168.240.3', '{\'username\': [u\'admin\'], \'remember_me\': [u\'y\'], \'password\': [u\'admin\'], \'submit\': [u\'\\u767b\\u9646\'], \'next\': [u\'/admin/\']}', 'current_user:admin', '2018-06-27 14:27:21', '2018-06-27 14:27:21');
INSERT INTO `t_operation_log` VALUES ('16', 'admin', 'login', '用户登陆', '192.168.240.3', '{\'username\': [u\'admin\'], \'remember_me\': [u\'y\'], \'password\': [u\'admin\'], \'submit\': [u\'\\u767b\\u9646\'], \'next\': [u\'/admin/\']}', 'current_user:admin', '2018-06-27 17:43:50', '2018-06-27 17:43:50');
INSERT INTO `t_operation_log` VALUES ('17', 'admin', 'add_group', '添加分组', '127.0.0.1', '{\'status\': [u\'1\'], \'name\': [u\'\\u8fce\\u65b0\\u7ba1\\u7406\\u5458\']}', 'name:迎新管理员', '2018-06-29 09:50:33', '2018-06-29 09:50:33');
INSERT INTO `t_operation_log` VALUES ('18', 'admin', 'add_group', '添加分组', '127.0.0.1', '{\'status\': [u\'1\'], \'name\': [u\'\\u62db\\u751f\\u7ba1\\u7406\\u5458\']}', 'name:招生管理员', '2018-06-29 09:50:56', '2018-06-29 09:50:56');
INSERT INTO `t_operation_log` VALUES ('19', 'admin', 'add_group', '添加分组', '127.0.0.1', '{\'status\': [u\'0\'], \'name\': [u\'\\u8d22\\u52a1\\u7ba1\\u7406\\u5458\']}', 'name:财务管理员', '2018-06-29 09:51:09', '2018-06-29 09:51:09');
INSERT INTO `t_operation_log` VALUES ('20', 'admin', 'add_group', '添加分组', '127.0.0.1', '{\'status\': [u\'1\'], \'name\': [u\'\\u5bbf\\u7ba1\\u5458\']}', 'name:宿管员', '2018-06-29 09:51:36', '2018-06-29 09:51:36');
INSERT INTO `t_operation_log` VALUES ('21', 'admin', 'edit_group', '编辑分组', '127.0.0.1', '{\'status\': [u\'1\'], \'id\': [u\'5\'], \'name\': [u\'\\u8d22\\u52a1\\u7ba1\\u7406\\u5458\']}', 'name:财务管理员', '2018-06-29 09:51:43', '2018-06-29 09:51:43');
INSERT INTO `t_operation_log` VALUES ('22', 'admin', 'group_grant', '分组授权', '127.0.0.1', '{\'rules\': [u\'[1,218,219,220,221,222]\'], \'group_id\': [u\'3\']}', 'name:迎新管理员', '2018-06-29 09:52:10', '2018-06-29 09:52:10');
INSERT INTO `t_operation_log` VALUES ('23', 'admin', 'group_grant', '分组授权', '127.0.0.1', '{\'rules\': [u\'[1,221,222]\'], \'group_id\': [u\'5\']}', 'name:财务管理员', '2018-06-29 09:52:22', '2018-06-29 09:52:22');
INSERT INTO `t_operation_log` VALUES ('24', 'admin', 'group_grant', '分组授权', '127.0.0.1', '{\'rules\': [u\'[1,218]\'], \'group_id\': [u\'4\']}', 'name:招生管理员', '2018-06-29 09:52:43', '2018-06-29 09:52:43');
INSERT INTO `t_operation_log` VALUES ('25', 'admin', 'group_grant', '分组授权', '127.0.0.1', '{\'rules\': [u\'[1,219]\'], \'group_id\': [u\'6\']}', 'name:宿管员', '2018-06-29 09:52:53', '2018-06-29 09:52:53');
INSERT INTO `t_operation_log` VALUES ('26', 'admin', 'edit_user', '编辑用户', '127.0.0.1', '{\'username\': [u\'gaoyuan\'], \'confirm_password\': [u\'gaoyuan\'], \'group_id\': [u\'6\'], \'password\': [u\'gaoyuan\'], \'email\': [u\'1509699669@qq.com\'], \'id\': [u\'2\']}', 'username:gaoyuan', '2018-06-29 09:53:14', '2018-06-29 09:53:14');
INSERT INTO `t_operation_log` VALUES ('27', 'admin', 'logout', '用户登出', '127.0.0.1', '{}', 'current_user:admin', '2018-06-29 09:53:17', '2018-06-29 09:53:17');
INSERT INTO `t_operation_log` VALUES ('28', 'gaoyuan', 'login', '用户登陆', '127.0.0.1', '{\'username\': [u\'gaoyuan\'], \'remember_me\': [u\'y\'], \'password\': [u\'gaoyuan\'], \'submit\': [u\'\\u767b\\u9646\']}', 'current_user:gaoyuan', '2018-06-29 09:53:25', '2018-06-29 09:53:25');
INSERT INTO `t_operation_log` VALUES ('29', 'admin', 'del_menu', '删除菜单', '127.0.0.1', '{\'menu_id\': [u\'222\']}', 'name:院系统计', '2018-07-23 11:24:11', '2018-07-23 11:24:11');
INSERT INTO `t_operation_log` VALUES ('30', 'admin', 'edit_menu', '编辑菜单', '127.0.0.1', '{\'sort\': [u\'13\'], \'method\': [u\'admin/payment-statistics\'], \'menu_name\': [u\'\\u7f34\\u8d39\\u7edf\\u8ba11\'], \'parent_id\': [u\'0\'], \'is_show\': [u\'1\'], \'type\': [u\'0\'], \'id\': [u\'221\'], \'icon\': [u\'ti-bar-chart\']}', 'method:admin/payment-statistics', '2018-07-23 11:24:16', '2018-07-23 11:24:16');
INSERT INTO `t_operation_log` VALUES ('31', 'admin', 'del_menu', '删除菜单', '127.0.0.1', '{\'menu_id\': [u\'221\']}', 'name:缴费统计1', '2018-07-23 11:24:19', '2018-07-23 11:24:19');
INSERT INTO `t_operation_log` VALUES ('32', 'admin', 'del_menu', '删除菜单', '127.0.0.1', '{\'menu_id\': [u\'220\']}', 'name:分配规则', '2018-07-23 11:24:22', '2018-07-23 11:24:22');
INSERT INTO `t_operation_log` VALUES ('33', 'admin', 'del_menu', '删除菜单', '127.0.0.1', '{\'menu_id\': [u\'219\']}', 'name:寝室床位', '2018-07-23 11:24:25', '2018-07-23 11:24:25');
INSERT INTO `t_operation_log` VALUES ('34', 'admin', 'del_menu', '删除菜单', '127.0.0.1', '{\'menu_id\': [u\'218\']}', 'name:学生管理', '2018-07-23 11:24:29', '2018-07-23 11:24:29');

-- ----------------------------
-- Table structure for t_student
-- ----------------------------
DROP TABLE IF EXISTS `t_student`;
CREATE TABLE `t_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_card_no` varchar(20) DEFAULT NULL,
  `exam_no` varchar(32) DEFAULT NULL,
  `student_no` varchar(24) DEFAULT NULL,
  `name` varchar(24) DEFAULT NULL,
  `sex` smallint(6) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `teacher_name` varchar(24) DEFAULT NULL,
  `teacher_mobile` varchar(11) DEFAULT NULL,
  `cloth_id` int(11) DEFAULT NULL,
  `org_no` varchar(32) DEFAULT NULL,
  `bed_no` varchar(32) DEFAULT NULL,
  `is_loan` int(11) DEFAULT NULL,
  `loan_amt` decimal(12,2) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `bust` varchar(24) DEFAULT NULL,
  `height` varchar(24) DEFAULT NULL,
  `shoe_size` varchar(24) DEFAULT NULL,
  `waist` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `id_card_no` (`id_card_no`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_student
-- ----------------------------
INSERT INTO `t_student` VALUES ('1', '230707197903162738', '555555', '987156', '赵红缨', '1', '15208491440', null, null, null, '398e3ae879d911e8b5aa0242c0a8f002', null, null, null, '2018-06-27 15:10:52', '2018-06-27 17:40:56', null, '33', '22', '44', '44');
INSERT INTO `t_student` VALUES ('2', '610728197901049507', '666666', '987150', '李莉红', '0', '18188436392', null, null, null, '398ebf0e79d911e8b5aa0242c0a8f002', '7098fde079e111e8b5aa0242c0a8f002', null, null, '2018-06-27 15:10:52', '2018-06-27 16:30:58', null, null, null, null, null);
INSERT INTO `t_student` VALUES ('3', '430521198405205617', '777777', '987160', '吴赐晓', '1', '17318656017', null, null, null, '398e3ae879d911e8b5aa0242c0a8f002', null, '1', '1000.00', '2018-06-27 15:10:52', '2018-06-27 16:09:23', null, null, null, null, null);
INSERT INTO `t_student` VALUES ('4', '610301197903077577', '888888', '987155', '柳述俊', '1', '15208491442', null, null, null, '398fc8ae79d911e8b5aa0242c0a8f002', null, null, null, '2018-06-27 15:10:52', '2018-06-27 15:10:52', null, null, null, null, null);
INSERT INTO `t_student` VALUES ('5', '450981197207222907', '999999', '987158', '李小红', '1', '15208491443', null, null, null, '398e3ae879d911e8b5aa0242c0a8f002', null, null, null, '2018-06-27 15:10:52', '2018-06-27 15:10:52', null, null, null, null, null);

-- ----------------------------
-- Table structure for t_student_log
-- ----------------------------
DROP TABLE IF EXISTS `t_student_log`;
CREATE TABLE `t_student_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_no` varchar(24) DEFAULT NULL,
  `method` varchar(24) DEFAULT NULL,
  `req_data` varchar(1024) DEFAULT NULL,
  `resp_data` varchar(1024) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `remark` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_student_log
-- ----------------------------

-- ----------------------------
-- Table structure for t_system_cfg
-- ----------------------------
DROP TABLE IF EXISTS `t_system_cfg`;
CREATE TABLE `t_system_cfg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(32) DEFAULT NULL,
  `value` text,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `key` (`key`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_system_cfg
-- ----------------------------
INSERT INTO `t_system_cfg` VALUES ('1', 'site_name', '1');
INSERT INTO `t_system_cfg` VALUES ('2', 'site_keywords', '1111111111111');
INSERT INTO `t_system_cfg` VALUES ('3', 'site_description', '11111111111111');
INSERT INTO `t_system_cfg` VALUES ('4', 'third_code', '11111111111111');
INSERT INTO `t_system_cfg` VALUES ('5', 'email_smtp', '12');
INSERT INTO `t_system_cfg` VALUES ('6', 'email', '2');
INSERT INTO `t_system_cfg` VALUES ('7', 'email_password', '2121');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  `last_time` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `ix_t_user_email` (`email`) USING BTREE,
  UNIQUE KEY `ix_t_user_username` (`username`) USING BTREE,
  KEY `group_id` (`group_id`) USING BTREE,
  CONSTRAINT `t_user_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `t_user_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'admin', '1', 'pbkdf2:sha256:50000$BktW7bxC$5eb77497fbbcc6406cc5cfe6d8e1ce18d221c13fecef84e54bce7946b7060f7c', '2017-11-09 14:30:07', '2017-11-09 14:30:09', '1', null, 'admin', '1', '2017-11-09 14:30:16', '2017-11-09 14:30:19');
INSERT INTO `t_user` VALUES ('2', 'gaoyuan', '1509699669@qq.com', 'pbkdf2:sha256:50000$2xyUYadq$993fa59d45aa7685bd6fa4de92f58232e3369fb0f2c81056c87570f89a486301', '2017-11-09 06:37:37', '2017-11-09 06:37:37', '1', '0', 'gaoyuan', '6', '2017-11-09 14:37:37', '2018-06-29 09:53:14');
INSERT INTO `t_user` VALUES ('8', 'test', 'test@qq.com', 'pbkdf2:sha256:50000$3BnJtQ1O$c34bfef72d1d517fad0b990d38766ddfb2e6fd4d1558e6d8f3ddfdff1ee4b4ad', '2018-03-14 08:02:27', '2018-03-14 08:02:27', '1', '0', null, '2', '2018-03-14 16:02:27', '2018-03-14 16:02:27');
INSERT INTO `t_user` VALUES ('9', 'jinjie', 'jinjie@qq.com', 'pbkdf2:sha256:50000$oZffaqD8$aedaba5d7844e4fc90fe64af98e3e899270d7ba008110a27012a4f9c978a5f73', '2018-03-14 13:55:25', '2018-03-14 13:55:25', '1', '0', 'jinjie', '2', '2018-03-14 21:55:25', '2018-05-05 22:30:31');

-- ----------------------------
-- Table structure for t_user_group
-- ----------------------------
DROP TABLE IF EXISTS `t_user_group`;
CREATE TABLE `t_user_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `rules` text,
  `description` text,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of t_user_group
-- ----------------------------
INSERT INTO `t_user_group` VALUES ('1', '超级管理员', '1', '[1,2,3,4,74,5,6,75,76,77,7,78,79,80,81,83,97,101,121,103,112,113,126,115,116,117,118,119,84,87,95,96,127,88,89,90,91,92,93,94,132,133,85,86,111,122,128,129,130,131,99,100,105,106,114,102,107,108,120,104,109,110,124,125]', 'super role', '2017-11-06 15:18:39', '2018-01-09 09:49:22');
INSERT INTO `t_user_group` VALUES ('2', '编辑管理员', '1', '[1,197,198,203,199,202,204,205,206,207,208,209,210,211,212,213,214,215,216,217]', 'edit role', '2017-11-06 15:19:15', '2018-05-29 17:36:18');
INSERT INTO `t_user_group` VALUES ('3', '迎新管理员', '1', '[1,218,219,220,221,222]', null, '2018-06-29 09:50:33', '2018-06-29 09:52:10');
INSERT INTO `t_user_group` VALUES ('4', '招生管理员', '1', '[1,218]', null, '2018-06-29 09:50:56', '2018-06-29 09:52:43');
INSERT INTO `t_user_group` VALUES ('5', '财务管理员', '1', '[1,221,222]', null, '2018-06-29 09:51:09', '2018-06-29 09:52:22');
INSERT INTO `t_user_group` VALUES ('6', '宿管员', '1', '[1,219]', null, '2018-06-29 09:51:36', '2018-06-29 09:52:53');
