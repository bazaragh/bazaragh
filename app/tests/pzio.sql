-- MySQL dump 10.19  Distrib 10.3.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: pzio
-- ------------------------------------------------------
-- Server version	10.3.38-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE = @@TIME_ZONE */;
/*!40103 SET TIME_ZONE = '+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category`
(
    `id`          int(11)                                                       NOT NULL AUTO_INCREMENT,
    `name`        varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_polish_ci   NOT NULL,
    `description` varchar(4096) CHARACTER SET utf8mb4 COLLATE utf8mb4_polish_ci NOT NULL,
    `icon`        varchar(256)                                                  NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 9
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category`
    DISABLE KEYS */;
INSERT INTO `category`
VALUES (1, 'Moda',
        'Kategoria \"moda\" w Bazarze AGH to idealne miejsce dla osób szukających modnych ubrań, butów i akcesoriów w atrakcyjnych cenach. W naszej ofercie znajdziesz wiele ciekawych propozycji od innych użytkowników serwisu, którzy oferują ubrania i dodatki w bardzo dobrym stanie, często w bardzo przystępnych cenach.\n\nW naszej kategorii \"moda\" znajdziesz wiele ciekawych propozycji od użytkowników, którzy oferują różne rodzaje odzieży, butów oraz akcesoriów, takich jak torebki, zegarki, biżuteria i wiele innych. Produkty pochodzą od różnych marek i są w różnych rozmiarach, dzięki czemu każdy student znajdzie coś dla siebie.\n\nBazar AGH to także świetne miejsce, aby sprzedać swoje niepotrzebne ubrania i dodatki, co pozwoli na dodatkowe zarobki i miejsce w szafie na nowe zakupy. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"moda\" każdy student znajdzie coś dla siebie. Wszystkie oferty są starannie sprawdzane przez nasz zespół, aby zapewnić najwyższą jakość usług. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/fashion.png'),
       (2, 'Elektronika',
        'Kategoria \"elektronika\" w Bazarze AGH to miejsce, w którym znajdziesz szeroki wybór różnego rodzaju urządzeń elektronicznych w bardzo atrakcyjnych cenach. W naszej ofercie znajdziesz zarówno nowe, jak i używane urządzenia, dzięki czemu każdy student może znaleźć coś dla siebie.\n\nW naszej kategorii \"elektronika\" znajdziesz różnego rodzaju urządzenia, takie jak telewizory, laptopy, smartfony, tablety, konsole do gier, aparaty fotograficzne, kamery, słuchawki i wiele innych. Produkty pochodzą od różnych marek i są w różnych cenach, co pozwala na dopasowanie oferty do swojego budżetu.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne urządzenia elektroniczne, co pozwala na dodatkowe zarobki i miejsce na nowe zakupy. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"elektronika\" znajdziesz wiele ciekawych ofert, które z pewnością zainteresują każdego studenta. Wszystkie oferty są starannie sprawdzane przez nasz zespół, aby zapewnić najwyższą jakość usług. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/electronics.png'),
       (3, 'Edukacja',
        'Kategoria \"edukacja\" w Bazarze AGH to miejsce, w którym znajdziesz wiele ciekawych ofert związanych z nauką i edukacją. W naszej ofercie znajdziesz różnego rodzaju podręczniki, materiały dydaktyczne, kursy językowe, pomoce naukowe i wiele innych.\n\nW naszej kategorii \"edukacja\" oferujemy szeroki wybór materiałów edukacyjnych, które pomogą każdemu studentowi w zdobywaniu wiedzy i umiejętności. Wszystkie oferty są starannie przeglądane, aby zapewnić najwyższą jakość produktów.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne podręczniki, materiały dydaktyczne i pomoce naukowe. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"edukacja\" znajdziesz wiele ciekawych propozycji, które z pewnością pomogą w nauce i rozwoju. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/education.png'),
       (4, 'Zdrowie i uroda',
        'Kategoria \"zdrowie i uroda\" w Bazarze AGH to miejsce, w którym znajdziesz wiele interesujących ofert związanych z dbałością o zdrowie i urodę. W naszej ofercie znajdziesz produkty związane z kosmetyką, suplementami diety i wiele innych.\n\nW naszej kategorii \"zdrowie i uroda\" oferujemy szeroki wybór produktów, które pomogą każdemu studentowi w dbałości o swoje zdrowie i urodę. Wszystkie oferty są starannie przeglądane, aby zapewnić najwyższą jakość produktów.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne produkty związane z kosmetyką, suplementami diety lub innymi tego typu produktami. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"zdrowie i uroda\" znajdziesz wiele ciekawych propozycji, które z pewnością pomogą w dbałości o swoje zdrowie i urodę. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/health.png'),
       (5, 'Sport',
        'Kategoria \"sport\" w Bazarze AGH to miejsce, w którym znajdziesz wiele interesujących ofert związanych z aktywnym trybem życia i uprawianiem sportu. W naszej ofercie znajdziesz różnego rodzaju sprzęt sportowy, odzież sportową, buty sportowe, akcesoria sportowe i wiele innych.\n\nW naszej kategorii \"sport\" oferujemy szeroki wybór produktów, które pomogą każdemu studentowi w aktywnym spędzaniu wolnego czasu. Wszystkie oferty są starannie przeglądane, aby zapewnić najwyższą jakość produktów.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne produkty związane ze sportem. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"sport\" znajdziesz wiele ciekawych propozycji, które z pewnością pomogą w uprawianiu ulubionej dyscypliny sportowej. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/sports.png'),
       (6, 'Jedzenie',
        'Kategoria \"jedzenie\" w Bazarze AGH to miejsce, w którym znajdziesz wiele interesujących ofert związanych z kulinariami. W naszej ofercie znajdziesz różnego rodzaju produkty spożywcze, akcesoria kuchenne, sprzęt AGD i wiele innych.\n\nW naszej kategorii \"jedzenie\" oferujemy szeroki wybór produktów, które pomogą każdemu studentowi w przygotowaniu smacznych posiłków. Wszystkie oferty są starannie przeglądane, aby zapewnić najwyższą jakość produktów.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne produkty związane z kulinariami. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"jedzenie\" znajdziesz wiele ciekawych propozycji, które z pewnością pomogą w przygotowaniu ulubionych potraw. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/diet.png'),
       (7, 'Wnętrze',
        'Kategoria \"wnętrze\" w Bazarze AGH to miejsce, w którym znajdziesz wiele interesujących ofert związanych z aranżacją wnętrz. W naszej ofercie znajdziesz różnego rodzaju meble, dekoracje, oświetlenie i wiele innych.\n\nW naszej kategorii \"wnętrze\" oferujemy szeroki wybór produktów, które pomogą każdemu studentowi w urządzeniu swojego mieszkania lub pokoju w akademiku. Wszystkie oferty są starannie przeglądane, aby zapewnić najwyższą jakość produktów.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne produkty związane z aranżacją wnętrz. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"wnętrze\" znajdziesz wiele ciekawych propozycji, które z pewnością pomogą w urządzeniu przestrzeni w sposób funkcjonalny i estetyczny. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/shelf.png'),
       (8, 'Muzyka i hobby',
        'Kategoria \"muzyka i hobby\" w Bazarze AGH to miejsce, w którym znajdziesz wiele interesujących ofert związanych z twoimi pasjami i zainteresowaniami artystycznymi. W naszej ofercie znajdziesz różnego rodzaju instrumenty muzyczne, akcesoria muzyczne, płyty CD, winyle oraz wiele innych przedmiotów związanych z muzyką i hobby, a także akcesoria artystyczne takie jak farby, pędzle, bloki rysunkowe, modele do sklejania i wiele innych.\n\nW naszej kategorii \"muzyka i hobby\" oferujemy szeroki wybór produktów, które pomogą każdemu studentowi w realizacji swoich pasji artystycznych. Wszystkie oferty są starannie przeglądane, aby zapewnić najwyższą jakość produktów.\n\nBazar AGH to także idealne miejsce, aby sprzedać swoje niepotrzebne produkty związane z muzyką, hobby i sztuką. Dzięki temu, że oferty pochodzą od innych użytkowników serwisu, można liczyć na bardzo atrakcyjne ceny i interesujące okazje.\n\nW naszej kategorii \"muzyka i hobby\" znajdziesz wiele ciekawych propozycji, które z pewnością pomogą w realizacji twoich zainteresowań artystycznych. Zachęcamy do zapoznania się z ofertami i do skorzystania z naszego serwisu.',
        'categories-icons/music.png');
/*!40000 ALTER TABLE `category`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dormitory`
--

DROP TABLE IF EXISTS `dormitory`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dormitory`
(
    `id`      varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_polish_ci  NOT NULL,
    `name`    varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_polish_ci NOT NULL,
    `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_polish_ci DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dormitory`
--

LOCK TABLES `dormitory` WRITE;
/*!40000 ALTER TABLE `dormitory`
    DISABLE KEYS */;
INSERT INTO `dormitory`
VALUES ('DS1', 'Olimp', 'Józefa Rostafińskiego 9, 30-072 Kraków'),
       ('DS10', 'Hajduczek', 'Witolda Budryka 10, 30-072 Kraków'),
       ('DS11', 'Bonus', 'Witolda Budryka 5, 30-072 Kraków'),
       ('DS12', 'Promyk', 'Witolda Budryka 3, 30-072 Kraków'),
       ('DS13', 'Straszny Dwór', 'Witolda Budryka 1, 30-072 Kraków'),
       ('DS14', 'Kapitol', 'Witolda Budryka 2, 30-072 Kraków'),
       ('DS15', 'Maraton', 'Juliana Tokarskiego 10, 30-065 Kraków'),
       ('DS16', 'Itaka', 'Juliana Tokarskiego 8, 30-065 Kraków'),
       ('DS17', 'Arkadia', 'Juliana Tokarskiego 6, 30-065 Kraków'),
       ('DS18', 'Odyseja', 'Juliana Tokarskiego 4, 30-065 Kraków'),
       ('DS19', 'Apollo', 'Juliana Tokarskiego 2, 30-065 Kraków'),
       ('DS2', 'Babilon', 'Józefa Rostafińskiego 11, 30-072 Kraków'),
       ('DS3', 'Akropol', 'Juliana Tokarskiego 1, 30-065 Kraków'),
       ('DS4', 'Filutek', 'Józefa Rostafińskiego 10, 30-072 Kraków'),
       ('DS5', 'Strumyk', 'Józefa Rostafińskiego 8, 30-072 Kraków'),
       ('DS6', 'Bratek', 'Józefa Rostafińskiego 6, 30-072 Kraków'),
       ('DS7', 'Zaścianek', 'Józefa Rostafińskiego 4, 30-072 Kraków'),
       ('DS8', 'Stokrotka', 'Józefa Rostafińskiego 2, 30-072 Kraków'),
       ('DS9', 'Omega', 'Witolda Budryka 9, 30-072 Kraków'),
       ('I DS', 'Alfa', 'Władysława Reymonta 17, 30-059 Kraków'),
       ('None', 'Spoza MS AGH', NULL);
/*!40000 ALTER TABLE `dormitory`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faculty`
(
    `id`   varchar(10)  NOT NULL,
    `name` varchar(200) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty`
    DISABLE KEYS */;
INSERT INTO `faculty`
VALUES ('EAIiIB', 'Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej'),
       ('EiP', 'Energetyki i Paliw'),
       ('FiIS', 'Fizyki i Informatyki Stosowanej'),
       ('GGiIŚ', 'Geodezji Górniczej i Inżynierii Środowiska'),
       ('GGiOŚ', 'Geologii, Geofizyki i Ochrony Środowiska'),
       ('H', 'Humanistyczny'),
       ('IEiT', 'Informatyki, Elektroniki i Telekomunikacji'),
       ('ILiGZ', 'Inżynierii Lądowej i Gospodarki Zasobami'),
       ('IMiC', 'Inżynierii Materiałowej i Ceramiki'),
       ('IMiIP', 'Inżynierii Metali i Informatyki Przemysłowej'),
       ('IMiR', 'Inżynierii Mechanicznej i Robotyki'),
       ('MN', 'Metali Niezależnych'),
       ('MS', 'Matematyki Stosowanej'),
       ('None', 'Inna uczelnia'),
       ('O', 'Odlewnictwa'),
       ('WNiG', 'Wiertnictwa, Nafty i Gazu'),
       ('Z', 'Zarządzania');
/*!40000 ALTER TABLE `faculty`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favourite`
--

DROP TABLE IF EXISTS `favourite`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favourite`
(
    `id`    int(11) NOT NULL AUTO_INCREMENT,
    `user`  int(11) NOT NULL,
    `offer` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `favourite_offer_id_fk` (`offer`),
    KEY `favourite_user_id_fk` (`user`),
    CONSTRAINT `favourite_offer_id_fk` FOREIGN KEY (`offer`) REFERENCES `offer` (`id`) ON DELETE CASCADE,
    CONSTRAINT `favourite_user_id_fk` FOREIGN KEY (`user`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  AUTO_INCREMENT = 12
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favourite`
--

LOCK TABLES `favourite` WRITE;
/*!40000 ALTER TABLE `favourite`
    DISABLE KEYS */;
/*!40000 ALTER TABLE `favourite`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message`
(
    `id`        int(11)       NOT NULL AUTO_INCREMENT,
    `sender`    int(11)       NOT NULL,
    `recipient` int(11)       NOT NULL,
    `post_date` datetime      NOT NULL,
    `read_date` datetime DEFAULT NULL,
    `content`   varchar(2000) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `message_recipient_user_id_fk` (`recipient`),
    KEY `message_sender_user_id_fk` (`sender`),
    CONSTRAINT `message_recipient_user_id_fk` FOREIGN KEY (`recipient`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `message_sender_user_id_fk` FOREIGN KEY (`sender`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `content_not_empty` CHECK (octet_length(`content`) > 0)
) ENGINE = InnoDB
  AUTO_INCREMENT = 54
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message`
    DISABLE KEYS */;
INSERT INTO `message`
VALUES (2, 8, 1, '2023-05-19 22:20:07', '2023-05-20 11:47:18', 'Testowa wiadomość od Test1'),
       (4, 1, 8, '2023-05-20 10:38:55', NULL, 'Wiadomość od admina'),
       (6, 1, 8, '2023-05-20 10:46:21', NULL, 'test'),
       (8, 1, 8, '2023-05-20 10:48:23', NULL, 'Chyba działa'),
       (23, 1, 8, '2023-05-20 11:57:34', NULL, 'jeszcze jeden test'),
       (25, 1, 8, '2023-05-20 12:05:03', NULL, 'hop'),
       (27, 1, 8, '2023-05-29 12:32:58', NULL, 'Test'),
       (28, 1, 8, '2023-05-29 16:35:55', NULL, '<3');
/*!40000 ALTER TABLE `message`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer`
--

DROP TABLE IF EXISTS `offer`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer`
(
    `id`          int(11)                                            NOT NULL AUTO_INCREMENT,
    `author`      int(11)                                            NOT NULL,
    `description` varchar(4096)                                               DEFAULT NULL,
    `category`    int(11)                                            NOT NULL,
    `title`       varchar(128)                                       NOT NULL,
    `created_at`  datetime                                           NOT NULL DEFAULT current_timestamp(),
    `price`       float                                                       DEFAULT NULL,
    `is_used`     tinyint(1)                                         NOT NULL,
    `images`      longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
    PRIMARY KEY (`id`),
    KEY `offer_category_id_fk` (`category`),
    KEY `offer_user_id_fk` (`author`),
    CONSTRAINT `offer_category_id_fk` FOREIGN KEY (`category`) REFERENCES `category` (`id`),
    CONSTRAINT `offer_user_id_fk` FOREIGN KEY (`author`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `price_not_negative` CHECK (`price` > 0)
) ENGINE = InnoDB
  AUTO_INCREMENT = 98
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer`
--

LOCK TABLES `offer` WRITE;
/*!40000 ALTER TABLE `offer`
    DISABLE KEYS */;
INSERT INTO `offer`
VALUES (84, 26, 'Oddam kotka', 7, 'Kotek', '2023-06-02 13:40:32', NULL, 1, '[\"1685706032_maxwell.jpg\"]'),
       (85, 26, 'Mam na sprzedaż krewetkę, która jako jedyna przeżyła wyprawę w kosmos rakietą AGH Space Systems.', 5,
        'Krewetka prosto z kosmosu', '2023-06-02 13:44:05', 999, 1,
        '[\"1685706245_krew2.jpg\", \"1685706245_krew.jpg\"]'),
       (86, 26,
        'Witam.\r\nMam do sprzedania 5 książek przedstawionych na  zdjęciu po 10zł za sztukę. W zestawie tylko 45zł!',
        3, 'Feynamana wykłady z fizyki', '2023-06-02 13:47:10', 10, 1, '[\"1685706430_fey.jpg\"]'),
       (87, 26,
        'ADIDAS ORIGINALS 3 STRIPES OLDSCHOOL\r\nDRES DAMSKI KOMPLETNY\r\nBLUZA + SPODNIE\r\nPRODUKT KLASY PREMIUM\r\nWYSZYWANE LOGO\r\n\r\nDostępne rozmiary :\r\nS - jeden komplet.\r\nL - jeden komplet.\r\nXL - jeden komplet.\r\nW wiadomości proszę napisać jaki rozmiar ma być wysłany.\r\n\r\nWymiary bluzy na płasko bez rozciągania :\r\nDługość całkowita : S 58 cm / L 62 cm / XL 64 cm.\r\nSzerokość od pachy do pachy : S 40 cm / L 44 cm / XL 46 cm.\r\nDługość rękawa od szwa na ramieniu : S 54 cm / L 58 cm / XL 60 cm.\r\n( tolerancja +/- 1 cm. )\r\n\r\nWymiary spodni na płasko bez rozciągania :\r\nDługość całkowita : S 90 cm / L 94 cm / XL 96 cm.\r\nSugerowany obwód pasa : S 60-75 cm / L 70-85 cm / XL 75-90 cm.\r\nW pasie dodatkowo znajduje się guma regulująca oraz sznurek.\r\n( tolerancja +/- 1 cm. )\r\n\r\nSkład materiałowy :\r\n90% poliester.\r\n10% elastan.\r\nŚwietnie dopasowuje się do ciała.\r\n\r\nProdukt Klasy Premium.\r\nStan nowy z kompletem wszystkich metek i opakowaniem.\r\nKolor czarny z białym jak na foto.\r\nWyjątkowy i modny design.\r\nŚwietna jakość wykonania.\r\nWyszywane logo na bluzie i spodniach.\r\nBluza na zamek, kaptur, dwie kieszenie po bokach na zamek.\r\nSpodnie dwie kieszenie po bokach na zamek.\r\nPas dodatkowo regulowany ściągaczem oraz sznurkiem.\r\nBardzo ładny, modny i wyjątkowy dres.\r\nIdealnie sprawdzi się do uprawiania sportu jak i do chodzenia na co dzień.\r\nSzybka wysyłka w dzień zakupu.\r\nSerdecznie polecam.\r\n\r\nDostawa kurier InPost pobranie 27 zł.\r\nPaczkomat InPost pobranie 21 zł. płatne blikiem przy odbiorze w paczkomacie.\r\nPrzy zakupie kilku rzeczy tylko jeden koszt wysyłki.\r\nW wiadomości proszę podać niezbędne dane do nadania paczki :\r\nImię i nazwisko.\r\nUlica, numer domu, numer mieszkania.\r\nKod pocztowy, miejscowość.\r\nNumer telefonu dla kuriera.\r\n\r\nWszystkie produkty przed wysyłką są odpowiednio zabezpieczone i starannie zapakowane, tak aby dotarły do Państwa w idealnym stanie.\r\nZachęcam do zakupu.',
        1, 'dresy adidas rozmiar M', '2023-06-02 13:49:22', 69, 0,
        '[\"1685706562_adidas2.jpg\", \"1685706562_adidas.jpg\"]'),
       (88, 26,
        'Zestaw rzęs Nagaraku.\r\n10 paletek.\r\nCena za całość, za cały zestaw.\r\nWszystko co widać na zdjęciu.', 4,
        'Rzęsy 100 sztuk', '2023-06-02 13:54:00', 170, 0, '[\"1685706840_rzes.jpeg\"]'),
       (89, 11,
        'Radiotelefon Baofeng UV-82 HT 8 WAT jest profesjonalnym radiem krótkofalarskim ( z zaprogramowanymi kanałami amatorskimi PMR) które idealnie sprawdzi się do rodzinnych wyjazdów, spacerów itp. Baofeng UV-82 to dwupasmowy radiotelefon (duobander) o mocy 8 watów z podwójnym wyświetlaczem, klawiaturą DTMF i funkcją Dual Watch.\r\n\r\nRadiotelefon Baofeng UV-82 HT 8 WAT to produkt z najnowszej produkcji\r\n\r\nDuobander wyposażono w podwójny wyświetlacz, 41 pozycyjne menu, selektywne wywołanie, Dual Watch, latarkę LED oraz wiele innych funkcji.\r\n\r\nWbudowane radio FM pozwala w przerwach rozmowy słuchać ulubionej stacji, automatycznie przełączając się na wybrany kanał po odebraniu sygnału od drugiej stacji.\r\n\r\nPodstawa zasilająca pozwala ładować tak radiotelefon jak i samą baterię\r\n\r\n\r\n\r\nRadio jest ROZBLOKOWANE - umożliwia pracę (odbiór i nadawanie) w PEŁNYM zakresie VHF 136-174MHz oraz UHF 400-520MHz. Kwestie zgodności z prawem na nadawanie zostawiamy dla kupującego - jednak radio technicznie umożliwia pracę na PMR, Zakresie amatorskim, Walkie Talkie, Policji, Straży, Pogotowia, PKP, TAXI, Ochrony, wszelkich innych służb mundurowych, komunalnych, prywatnych firm oraz wiele innych korzystających z tego zakresu częstotliwości !!!\r\n\r\nRadio posiada \'\'podwójny odbiornik- dual watch\'\' czyli możliwość nasłuchu na dwóch kanałach jednocześnie!\r\n\r\nObydwa aktywne kanały wyświetlają się na wyświetlaczu, dzięki czemu możemy mieć jeden ważny kanał w ciągłym nasłuchu, oraz drugi do łączności pomiędzy jednostkami, itd. Radio oczywiście odbiera \'\'używany\'\' kanał w pierwszej kolejności i go słucha do zakończenia transmisji (odbiór dwóch rozmów naraz nie miał by oczywiście sensu bo wszystko by się zlało w jeden jazgot).\r\n\r\nNadawanie odbywa się za pośrednictwem podwójnego przycisku PTT (nadawania) - jeżeli chcemy nadawać na \'\'górnym\'\' kanale na wyświetlaczu - naciskamy górny przycisk nadawania. Jeżeli chcemy nadawać na \'\'dolnym\'\' kanale na wyświetlaczu - naciskamy dolny przycisk nadawania - najbardziej intuicyjnie jak tylko się da\r\n\r\n\r\n\r\nSzczegółowy opis funkcji:\r\n\r\nDuży i czytelny 2 liniowy wyświetlacz\r\nPasma:\r\n136-174 MHz - nadawanie i odbiór FM\r\n400-520 MHz - nadawanie i odbiór FM\r\n65-108 MHz - odbiór radiowych stacji FM\r\nFirmware - minimum NUV82\r\n128 kanałów w pamięci\r\nTon 1750 Hz\r\nTony CTCSS i DTC tryb normal i invert\r\nWywołanie selektywne\r\nPraca z shiftem (dla przemienników)\r\nKrok 5, 6.25, 10, 12.5, 25 kHz\r\nBlokada klawiatury\r\nNasłuch dwóch częstotliwości (funkcja dual watch)\r\nFunkcja VOX\r\nLatarka\r\nMożliwość programowania z klawiatury lub z komputera\r\nPrzełączanie poziomu mocy nadawania: High/ Low\r\nMaksymalna moc nadawania 8 WAT\r\nBateria : 7,4V, 2800mAh\r\nW skład zestawu wchodzą:\r\n\r\nradiotelefon Baofeng UV-82 HT 8 WAT\r\nantena\r\nakumulator 2800mAh\r\nładowarka biurkowa\r\nzasilacz\r\nmikrofonosłuchawka PTT\r\nklips do paska\r\npasek na rękę\r\nInstrukcja obsługi w j. polskim',
        5, 'Baofeng Krótkofalówka Policyjna UV- 82 8W! ', '2023-06-02 13:57:18', NULL, 0, '[\"1685707038_image.jpg\"]'),
       (90, 11,
        'Witam\r\nSprzedam komplety bielizny satynowe pgładkie\r\nStan-nowe\r\n\r\nDostępne rozmiary:\r\n75b,80b\r\nXs s m L\r\n\r\nDostępne kolory:\r\nBiały\r\nCzarny\r\nCzerwony\r\nRóżowy\r\nPanterka\r\nBordo\r\nKawowy\r\nO dostępność proszę pisać :)\r\n\r\nMożliwość kupna torby prezentowej papierowej z VS-20zł\r\n\r\nRodzaje wysyłki\r\nOlx\r\nInpost-14,99 płatność całość\r\nPobranie-20 przedpłata za wysyłkę\r\n\r\nNa wszelkie pytania odpowiem w wiadomości prywatnej.\r\nZapraszam do innych ogłoszeń',
        1, 'Zestaw bielizny vs', '2023-06-02 13:58:57', 129.99, 0, '[\"1685707137_vic.jpg\"]'),
       (91, 11,
        'Witam\r\nSprzedam komplety bielizny satynowe pgładkie\r\nStan-nowe\r\n\r\nDostępne rozmiary:\r\n75b,80b\r\nXs s m L\r\n\r\nDostępne kolory:\r\nBiały\r\nCzarny\r\nCzerwony\r\nRóżowy\r\nPanterka\r\nBordo\r\nKawowy\r\nO dostępność proszę pisać :)\r\n\r\nMożliwość kupna torby prezentowej papierowej z VS-20zł\r\n\r\nRodzaje wysyłki\r\nOlx\r\nInpost-14,99 płatność całość\r\nPobranie-20 przedpłata za wysyłkę\r\n\r\nNa wszelkie pytania odpowiem w wiadomości prywatnej.\r\nZapraszam do innych ogłoszeń',
        1, 'Zestaw bielizny vs', '2023-06-03 13:58:57', 129.99, 0, '[\"1685707137_vic.jpg\"]'),
       (92, 11, 'Ładne. Wygodne. Wysokość obcasa idealna. Polecam', 1, 'Nowe buty', '2023-06-15 22:19:16', 95, 1,
        '[\"1686860175_butek.jpg\"]'),
       (93, 11,
        'Sukienka ekegancka na komunię wesele chrzest, rozmiar 40, biust 100cm, talia 82, długość 88cm. Zapraszam do zakupu i do pozostałych ogłoszeń.',
        1, 'Sukienka orsay piękna', '2023-06-17 10:41:40', 42, 1, '[\"1686991294_suk.jpg\"]'),
       (94, 11,
        'Sukuenka na lato, lekka zwiewna, mgiełka, na podszewce, rozmiar L/XL ukrywa niedoskonałości sylwetki. Biust 53x2 bez rozciągania, długość 87cm. Zapraszam do zakupu i do obejrzenia pozostałych ogłoszeń.',
        1, 'Letnia sukienka na ramiączka rozm. 44-46', '2023-06-17 10:50:06', 47, 0, '[\"1686991341_suk2.jpg\"]'),
       (95, 11, 'Sukienka letnia na szerokie ramiączka bialo czarna z różowymi kwiatami\nStanik na zakładkę', 1,
        'Sukienka XL na lato', '2023-06-17 10:42:26', 18, 1, '[\"1686991405_suk3.jpg\"]'),
       (96, 11,
        'Śliczna granatowo biała letnia sukienka maxi.Z miłego materiału.\n\nSkład: poliester 95% i elastyn 5 %\n\nRozmiar z metki XL',
        1, 'Sukienka letnia roz 50', '2023-06-17 10:43:31', 20, 1, '[\"1686991472_suk4.jpg\"]'),
       (97, 11, 'Słodka letnia nowa sukienka na ramiączka.\nRozmiar z metki XL', 1,
        'Świetna granatowo biała długa sukienka', '2023-06-17 10:44:37', 80, 0, '[\"1686991800_suk5.jpg\"]');
/*!40000 ALTER TABLE `offer`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `offer_score`
--

DROP TABLE IF EXISTS `offer_score`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `offer_score`
(
    `id`       int(11) NOT NULL AUTO_INCREMENT,
    `offer`    int(11) DEFAULT NULL,
    `seller`   int(11) NOT NULL,
    `score`    int(11) NOT NULL,
    `customer` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `offer_score_offer_id_fk` (`offer`),
    KEY `offer_score_seller_id_fk` (`seller`),
    KEY `offer_score_customer_id_fk` (`customer`),
    CONSTRAINT `offer_score_customer_id_fk` FOREIGN KEY (`customer`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `offer_score_offer_id_fk` FOREIGN KEY (`offer`) REFERENCES `offer` (`id`) ON DELETE SET NULL,
    CONSTRAINT `offer_score_seller_id_fk` FOREIGN KEY (`seller`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `Offer score in <1,5>` CHECK (`score` >= 1 and `score` <= 5)
) ENGINE = InnoDB
  AUTO_INCREMENT = 3
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offer_score`
--

LOCK TABLES `offer_score` WRITE;
/*!40000 ALTER TABLE `offer_score`
    DISABLE KEYS */;
INSERT INTO `offer_score`
VALUES (2, NULL, 11, 3, 1);
/*!40000 ALTER TABLE `offer_score`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order`
(
    `id`   int(11) NOT NULL AUTO_INCREMENT,
    `info` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order`
    DISABLE KEYS */;
/*!40000 ALTER TABLE `order`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role`
(
    `id`              int(11)     NOT NULL AUTO_INCREMENT,
    `name`            varchar(80) NOT NULL,
    `description`     varchar(255)         DEFAULT NULL,
    `permissions`     text                 DEFAULT NULL,
    `update_datetime` timestamp   NOT NULL DEFAULT current_timestamp(),
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 4
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role`
    DISABLE KEYS */;
INSERT INTO `role`
VALUES (1, 'Admin', NULL, NULL, '2023-04-05 12:08:32'),
       (2, 'Moderator', NULL, NULL, '2023-04-05 12:08:32'),
       (3, 'User', NULL, NULL, '2023-04-05 12:08:32');
/*!40000 ALTER TABLE `role`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles_users`
--

DROP TABLE IF EXISTS `roles_users`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles_users`
(
    `user_id` int(11) DEFAULT NULL,
    `role_id` int(11) DEFAULT NULL,
    KEY `roles_users_role_id_fk` (`role_id`),
    KEY `roles_users_user_id_fk` (`user_id`),
    CONSTRAINT `roles_users_role_id_fk` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
    CONSTRAINT `roles_users_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles_users`
--

LOCK TABLES `roles_users` WRITE;
/*!40000 ALTER TABLE `roles_users`
    DISABLE KEYS */;
INSERT INTO `roles_users`
VALUES (1, 1), (8, 2);
/*!40000 ALTER TABLE `roles_users`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user`
(
    `id`                int(11)                                                       NOT NULL AUTO_INCREMENT,
    `email`             varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    `password`          varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
    `username`          varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci          DEFAULT NULL,
    `first_name`        varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci           DEFAULT NULL,
    `last_name`         varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci           DEFAULT NULL,
    `dorm`              varchar(4)                                                    NOT NULL,
    `faculty`           varchar(10)                                                   NOT NULL,
    `active`            tinyint(1)                                                    NOT NULL,
    `fs_uniquifier`     varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci  NOT NULL,
    `confirmed_at`      timestamp                                                     NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
    `last_login_at`     timestamp                                                     NOT NULL DEFAULT '0000-00-00 00:00:00',
    `current_login_at`  timestamp                                                     NOT NULL DEFAULT '0000-00-00 00:00:00',
    `last_login_ip`     varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci           DEFAULT NULL,
    `current_login_ip`  varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci           DEFAULT NULL,
    `login_count`       int(11)                                                                DEFAULT NULL,
    `tf_primary_method` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci           DEFAULT NULL,
    `tf_totp_secret`    varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci          DEFAULT NULL,
    `tf_phone_number`   varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci          DEFAULT NULL,
    `create_datetime`   timestamp                                                     NOT NULL DEFAULT current_timestamp(),
    `update_datetime`   timestamp                                                     NOT NULL DEFAULT current_timestamp(),
    `us_totp_secrets`   text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci                  DEFAULT NULL,
    `us_phone_number`   varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci          DEFAULT NULL,
    `email_change_new`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci          DEFAULT NULL,
    `email_change_code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci           DEFAULT NULL,
    `email_change_last` timestamp                                                     NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (`id`),
    KEY `user_dormitory_id_fk` (`dorm`),
    KEY `user_faculty_id_fk` (`faculty`),
    CONSTRAINT `user_dormitory_id_fk` FOREIGN KEY (`dorm`) REFERENCES `dormitory` (`id`),
    CONSTRAINT `user_faculty_id_fk` FOREIGN KEY (`faculty`) REFERENCES `faculty` (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 28
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user`
    DISABLE KEYS */;
INSERT INTO `user`
VALUES (1, 'admin@bazaragh.pl', '$2b$12$m4VqYGANUQ7q0jdAXPAUj.fxFD0iUmAii/FCMw3sP2budBh7xkBC6', 'admin', 'Użytkownik',
        'Testowy', 'DS1', 'EAIiIB', 1, 'f8084f5d0fb04ab5b0baeccbde7a83a8', '2023-05-03 18:36:48', '2023-04-05 10:07:38',
        '2023-04-05 10:07:38', NULL, NULL, NULL, NULL, NULL, NULL, '2023-04-05 10:07:38', '2023-04-05 10:07:38', NULL,
        NULL, NULL, NULL, '0000-00-00 00:00:00'),
       (8, 'test1@bazaragh.pl', '$2b$12$m4VqYGANUQ7q0jdAXPAUj.fxFD0iUmAii/FCMw3sP2budBh7xkBC6', NULL, 'Test1',
        'Test1', 'DS1', 'EAIiIB', 1, 'c6a04d0809b7498fb7b8bcb6369e2218', '2023-05-03 18:36:47', '2023-04-20 19:20:22',
        '2023-04-20 19:20:22', NULL, NULL, NULL, NULL, NULL, NULL, '2023-04-20 19:20:22', '2023-04-20 19:20:22', NULL,
        NULL, NULL, NULL, '0000-00-00 00:00:00'),
       (11, 'test2@bazaragh.pl', '$2b$12$m4VqYGANUQ7q0jdAXPAUj.fxFD0iUmAii/FCMw3sP2budBh7xkBC6', NULL,
        'Test2', 'Test2', 'DS1', 'EAIiIB', 1, '10eb0de7627949e0856a168038a58991', '2023-05-12 18:53:20',
        '2023-05-12 17:24:00', '2023-05-12 17:24:00', NULL, NULL, NULL, NULL, NULL, NULL, '2023-05-12 17:24:00',
        '2023-05-12 16:53:21', NULL, NULL, NULL, NULL, '0000-00-00 00:00:00'),
       (26, 'test3@bazaragh.pl', '$2b$12$m4VqYGANUQ7q0jdAXPAUj.fxFD0iUmAii/FCMw3sP2budBh7xkBC6', NULL, 'Test3', 'Test3',
        'None',
        'None', 1, 'a718745d6a0540358b2c718159a75abf', '2023-05-29 14:38:22', '2023-05-29 14:38:22',
        '2023-05-29 14:38:22', NULL, NULL, NULL, NULL, NULL, NULL, '2023-05-29 14:38:22', '2023-05-29 14:38:22', NULL,
        NULL, NULL, NULL, '0000-00-00 00:00:00'),
       (27, 'test4@bazaragh.pl', '$2b$12$m4VqYGANUQ7q0jdAXPAUj.fxFD0iUmAii/FCMw3sP2budBh7xkBC6', NULL, 'test4', 'test4',
        'None', 'None', 1, '98431bccd1f442c4b327fc8e42489a7e', '2023-06-15 20:16:02', '2023-06-15 20:16:02',
        '2023-06-15 20:16:02', NULL, NULL, NULL, NULL, NULL, NULL, '2023-06-15 20:16:02', '2023-06-15 20:16:02', NULL,
        NULL, NULL, NULL, '0000-00-00 00:00:00');
/*!40000 ALTER TABLE `user`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_score`
--

DROP TABLE IF EXISTS `user_score`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_score`
(
    `id`       int(11) NOT NULL AUTO_INCREMENT,
    `seller`   int(11) NOT NULL,
    `score`    int(11) NOT NULL,
    `customer` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `user_score_customer_id_fk` (`customer`),
    KEY `user_score_seller_id_fk` (`seller`),
    CONSTRAINT `user_score_customer_id_fk` FOREIGN KEY (`customer`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    CONSTRAINT `user_score_seller_id_fk` FOREIGN KEY (`seller`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  AUTO_INCREMENT = 2
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_score`
--

LOCK TABLES `user_score` WRITE;
/*!40000 ALTER TABLE `user_score`
    DISABLE KEYS */;
/*!40000 ALTER TABLE `user_score`
    ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE = @OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;

-- Dump completed on 2023-06-25 18:41:36
