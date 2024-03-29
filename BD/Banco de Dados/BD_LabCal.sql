CREATE DATABASE cadastro_labcal;
USE cadastro_labcal;

CREATE TABLE empresas 
(
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    email VARCHAR(100) NOT NULL,
    CEP VARCHAR(10) NOT NULL,
    responsavel VARCHAR(100) NOT NULL
);

CREATE TABLE equipamentos
(
    id INT PRIMARY KEY, 
    id_empresa INT NOT NULL, 
    nome VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    fabricante VARCHAR(100) NOT NULL,
    numero_serie VARCHAR(50) NOT NULL,
    setor VARCHAR(100) NOT NULL,
    padrao BOOL NOT NULL,
    calibracao BOOL NOT NULL,
    FOREIGN KEY (id_empresa) REFERENCES empresas(id)
);

CREATE TABLE controle
(
    id INT PRIMARY KEY,
    id_equipamento INT NOT NULL,
    certificado VARCHAR(100) NOT NULL,
    data_cal DATE NOT NULL,
    validade_cal DATE NOT NULL,
    FOREIGN KEY (id_equipamento) REFERENCES equipamentos(id)
);

CREATE TABLE instrucoes 
(
    id INT PRIMARY KEY,
    valor FLOAT NOT NULL,
    unidade VARCHAR(50) NOT NULL,
    incerteza FLOAT(50) NOT NULL,
    k FLOAT NOT NULL,
    grau_de_liberdade VARCHAR(50) NOT NULL,
    multiplicador INT NOT NULL
);

INSERT INTO empresas (id, nome, telefone, endereco, email, cep, responsavel) VALUES (1, 'INATEL', '(35) 3471-9200', 'Av. João de Camargo, 510 - Centro', 'inatel@inatel.br', '37.540-000', 'Túlio Barroso Volpato');


-- Inserção dos equipamentos
INSERT INTO equipamentos (id, id_empresa, nome, modelo, fabricante, numero_serie, setor, padrao, calibracao)
VALUES
(1, 1, 'AC POWER SOURCE ANALYZER', '6812A', 'HP', '3712A00928', 'setor 1', 0, 0),
(2, 1, 'ACOPLAMENTO DE RF', '1530', 'JBM', '-----', 'setor 1', 0, 0),
(3, 1, 'ANALIZADOR DE MODULAÇÃO', '844A', 'TFT', '1351382', 'setor 1', 0, 0),
(4, 1, 'ANALIZADOR DE LINHAS', 'TN-10/BN', 'WGB', 'A-0045', 'setor 1', 0, 0),
(5, 1, 'ANALIZADOR DE LINHAS', 'TN-10/BN', 'WGB', 'A-0044', 'setor 1', 0, 0),
(6, 1, 'ANALISADOR DE ESPECTRO', '4396A', 'HP', '3413J01050', 'setor 1', 0, 0),
(7, 1, 'ANALIZADOR DE ESPECTRO', 'FS300', 'R&S', '100538', 'setor 1', 0, 0),
(8, 1, 'ANT - ADVANCED NETWORK TESTER', 'ANT-20', 'WG', 'AB0119', 'setor 1', 0, 0),
(9, 1, 'ATENUADOR 1000W', 'RFA1000NFFdB', 'RFA1000NFF30H', '268/2021', 'setor 1', 1, 1),
(10, 1, 'ATENUADOR 12dB VHF', '355C', 'HP', '3646A44899', 'setor 1', 0, 0),
(11, 1, 'ATENUADOR 120dB VHF', '355D', 'HP', '3646A46944', 'setor 1', 0, 0),
(12, 1, 'ATENUADOR 250W', '45-30-34', 'WEINSHEL', 'LF862', 'setor 1', 1, 1),
(13, 1, 'ATENUADOR 500W', '53-30-34', 'WEINSHEL', 'MT427', 'setor 1', 1, 1),
(14, 1, 'ATENUADOR VARIAVEL', 'TT4111', 'TEL-MÊS', '23247', 'setor 1', 0, 0),
(15, 1, 'ATTENUATOR ASSEMBLY 30dB', '30dB ATT ASSEMBLY', 'HP', '3318A09605', 'setor 1', 0, 0),
(16, 1, 'CAMARA CLIMÁTICA', '1250 H/315', 'SUPEROHM', '-----', 'setor 1', 0, 0),
(17, 1, 'KIT  FP "0"', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(18, 1, 'KIT FP "0,7"', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(19, 1, 'CARGA RESISTIVA', 'CR-60', 'ELETROTESTE', '119', 'setor 1', 1, 1),
(20, 1, 'CARGA RESISTIVA', 'CR-60', 'ELETROTESTE', '-----', 'setor 1', 0, 0),
(21, 1, 'CASADOR DE IMPEDANCIA', 'RF10', 'JBM', '-----', 'setor 1', 0, 0),
(22, 1, 'KIT CENTELHADOR DUPLO', 'KIT', 'LABCAL', '-----', 'setor 1', 1, 1),
(23, 1, 'COMPRESSOR DE AUDIO', 'COK2000', 'TELETRONIX', '-----', 'setor 1', 0, 0),
(24, 1, 'CRONOMETRO', 'TEC426', 'TECHNOS', '7891530019838', 'setor 1', 0, 0),
(25, 1, 'CURRENT SHUNT', '34330A', 'HP', '-----', 'setor 1', 1, 1),
(26, 1, 'PCM CHANNEL ANALYZER', 'PCM 40', 'WG', 'H-05040', 'setor 1', 1, 1),
(27, 1, 'DECADA RESISTIVA', 'TR-9403', 'FOK-GYEM', '70101', 'setor 1', 0, 0),
(28, 1, 'KIT DESACOPLADOR DE AUDIO', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(29, 1, 'DISTORTION METER', 'HM8027', 'HAMEG', '27952', 'setor 1', 0, 0),
(30, 1, 'DECIBELÍMETRO', 'MSL-1352A', 'MINIPA', '135200113', 'setor 1', 0, 0),
(31, 1, 'FLUKE 5500A CALIBRATOR', '5500A', 'FLUKE', '6630004', 'setor 1', 1, 1),
(32, 1, 'FONTE DC AJUSTÁVEL', 'FA2030', 'SUPLITEC', '2254', 'setor 1', 0, 0),
(33, 1, 'FONTE DC DUPLA', 'GPC 3030', 'GW', '7640635', 'setor 1', 1, 1),
(34, 1, 'FONTE AC DE ALTA TENSÃO', '35905', 'PEK', '-----', 'setor 1', 0, 0),
(35, 1, 'FONTE DC DUPLA', 'GPC 3030', 'GW', '7640613', 'setor 1', 1, 1),
(36, 1, 'FONTE DC DUPLA', 'HM8142', 'HAMEG', '3305', 'setor 1', 1, 1),
(37, 1, 'FONTE DC DUPLA', 'HM8142', 'HAMEG', '3350', 'setor 1', 1, 1),
(38, 1, 'FREQUENCIMETRO', '53131A', 'HP', '3546A13850', 'setor 1', 1, 1),
(39, 1, 'FREQUENCIMETRO', 'HM8021-3', 'HAMEG', '22177', 'setor 1', 0, 0),
(40, 1, 'GERADOR DE ESTEREO', 'FUTURE 2002', 'TELETRONIX', '0260FUT', 'setor 1', 0, 0),
(41, 1, 'GERADOR DE PADRÕES PAL-M', 'LCG396', 'LEADER', '7611151', 'setor 1', 0, 0),
(42, 1, 'GERADOR DE SINAIS', 'HM8130', 'HAMEG', '130971P- 2725', 'setor 1', 0, 0),
(43, 1, 'GERADOR DE SINAIS', '8648B', 'HP', '3642U00719', 'setor 1', 0, 0),
(44, 1, 'GERADOR DE SINAIS', 'HM8130', 'HAMEG', '04017', 'setor 1', 0, 0),
(45, 1, 'GERADOR DE SINAIS', 'AFG2020', 'SONY', 'J310494', 'setor 1', 0, 0),
(47, 1, 'KIT ACOPLADOR', 'KIT Inatel-047', 'Inatel', '297/2021', 'setor 1', 1, 1),
(48, 1, 'KIT BALUM', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(49, 1, 'KIT DC', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(50, 1, 'KIT TROCA DE POLARIDADE','KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(51, 1, 'KIT ALIMENTADOR 250OHM/20H/3Km', 'KIT Inatel-051', 'Inatel', '158/2021', 'setor 1', 1, 1),
(52, 1, 'KIT RESOLUÇÃO 238', 'KIT Inatel-052', 'Inatel', '348/2022', 'setor 1', 1, 1),
(55, 1, 'KIT SIMULADOR DUPLO DE LINHA DE 3Km', 'KIT Inatel-055', 'Inatel', '192/2022', 'setor 1', 1, 1),
(56, 1, 'KIT ALIMENTADOR 20H C/ BALANCEAMENTO', 'KIT Inatel-056', 'Inatel', '353/2022', 'setor 1', 1, 1),
(57, 1, 'KIT PERDA POR RETORNO 600OHM', 'KIT Inatel-057', 'Inatel', '042/2022', 'setor 1', 0, 0),
(58, 1, 'KIT RISCO DE CHOQUE ELÉTRICO', 'KIT Inatel-058', 'Inatel', '133/2023', 'setor 1', 1, 1),
(59, 1, 'MULTIMETRO DE BANCADA', '34401A', 'HP', 'US36013862', 'setor 1', 1, 1),
(61, 1, 'KIT DTH BOX', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(62, 1, 'LC METER', 'HM8018', 'HAMEG', 'F66668', 'setor 1', 0, 0),
(63, 1, 'MEGOMETRO', '500D', 'METRISO', 'M47270030Q39', 'setor 1', 1, 1),
(64, 1, 'MILLIVOLTIMETRO', 'URV5', 'ROHDE&SCHWARZ', '847111/007', 'setor 1', 0, 0),
(65, 1, 'THERMO HIGROMETRO DIGITAL', '175-H2', 'TESTO', '20033746/406', 'setor 1', 1, 1),
(66, 1, 'MULTIMETRO DE BANCADA', '45', 'FLUKE', '6846024', 'setor 1', 1, 1),
(67, 1, 'KIT RESOLUÇÃO 237-Titulo IV-Paragrafo 3o.', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(68, 1, 'KIT NET 001/92', 'KIT Inatel-068', 'Inatel', '154/2023', 'setor 1', 1, 1),
(69, 1, 'MULTIMETRO MANUAL', 'ET2001', 'MINIPA', '2138', 'setor 1', 0, 0),
(70, 1, 'MULTIMETRO MANUAL', 'ET2001', 'MINIPA', '2152', 'setor 1', 0, 0),
(71, 1, 'MULTIMETRO MANUAL', '87 III', 'FLUKE', '71940391', 'setor 1', 1, 1),
(72, 1, 'THERMO HIGROMETRO DIGITAL', '175-H1', 'TESTO', '20001098/208', 'setor 1', 0, 0),
(73, 1, 'OSCILOSCOPIO DIGITAL', '54603B', 'HP', 'US37300108', 'setor 1', 1, 1),
(74, 1, 'OSCILOSCOPIO DIGITAL (Infinium)', '54825A', 'HP', 'US39190305', 'setor 1', 1, 1),
(75, 1, 'OSCILOSCÓPIO DIGITAL 4 CANAIS', '54602B', 'HP', 'US37300151', 'setor 1', 1, 1),
(76, 1, 'TELEPHONE SET TESTER', '212', 'HASSELRIIS', '290', 'setor 1', 0, 0),
(77, 1, 'PARAMETER TEST SET', '85046A', 'HP', '3033A06919', 'setor 1', 0, 0),
(78, 1, 'DECADA RESISTIVA', 'TR_9403', 'FOK-GYEM', '70103', 'setor 1', 1, 1),
(79, 1, 'PONTA DE PROVA DE ALTA TENSÃO', 'HV15HF', 'MINIPA', '-----', 'setor 1', 0, 0),
(80, 1, 'PONTA DE PROVA DE ALTA TENSÃO', 'HV40', 'MINIPA', '-----', 'setor 1', 0, 0),
(81, 1, 'POWER METER', '437B', 'HP', '3125U22648', 'setor 1', 1, 1),
(82, 1, 'POWER METER', '437B', 'HP', '3125U26004', 'setor 1', 1, 1),
(83, 1, 'POWER SENSOR 8481A', '8481A', 'HP', 'US37290208', 'setor 1', 1, 1),
(84, 1, 'POWER SENSOR 8481A', '8481A', 'HP', 'US37290206', 'setor 1', 1, 1),
(85, 1, 'POWER SENSOR 8481A', '8481A', 'HP', 'US37290203', 'setor 1', 0, 0),
(86, 1, 'POWER SENSOR 8481B', '8481B', 'HP', '331BA09605', 'setor 1', 0, 0),
(87, 1, 'POWER SENSOR 8481D', '8481D', 'HP', '3643A14225', 'setor 1', 0, 0),
(88, 1, 'POWER SPLITTER', '11667A', 'HP', '21347', 'setor 1', 0, 0),
(89, 1, 'POWER SPLITTER', '11667A', 'HP', '21346', 'setor 1', 0, 0),
(90, 1, 'PSOFOMETRO', 'GMP-1', 'WGB', 'D-041', 'setor 1', 0, 0),
(91, 1, 'RANGE CALIBRATOR', '11683A', 'HP', '3303U00508', 'setor 1', 0, 0),
(92, 1, 'REFERENCE ATTENUATOR 30dB', '11708A', 'HP', '14653', 'setor 1', 0, 0),
(93, 1, 'RESISTENCIA VARIÁVEL', '90R1A', 'OHMA', '39561', 'setor 1', 0, 0),
(94, 1, 'RESISTENCIA VARIÁVEL', '56R1,7A', 'OHMA', '39562', 'setor 1', 0, 0),
(95, 1, 'KIT RESISTOR 600OHM', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(96, 1, 'RF COMMUNICATIONS TEST SET', '8920A', 'HP', '3633A08546', 'setor 1', 1, 1),
(97, 1, 'SOUND-LEVEL CALIBRATOR', '4230', 'B&K', '1440713', 'setor 1', 1, 1),
(98, 1, 'SOUND-LEVEL CALIBRATOR', '1356', 'MINIPA', 'TES00000124', 'setor 1', 0, 0),
(99, 1, 'DEDO MECÂNICO', '-----', 'LABCAL', 'Inatel-099', 'setor 1', 1, 1),
(100, 1, 'SURGE TEST', 'TST735', 'ELETROTESTE', '----', 'setor 1', 1, 1),
(101, 1, 'TELEFONE PADRÃO', 'VIP-CLASS', 'LEUCOTRON', '7701027774', 'setor 1', 0, 0),
(102, 1, 'PABX 2 TRONCOS 11 RAMAIS', 'SLIM211', 'LEUCOTRON', '229800437', 'setor 1', 0, 0),
(103, 1, 'TERMOMETRO INFRAVERMELHO', '61', 'FLUKE', '80770088', 'setor 1', 1, 1),
(104, 1, 'TERMOMETRO/ HIGRÔMETRO', '-----', 'THIES CLIMA', '797114', 'setor 1', 0, 0),
(105, 1, 'KIT TESTADOR DE CENTELHADORES', '-----', 'LABCAL', '-----', 'setor 1', 0, 0),
(106, 1, 'OSCILOSCOPIO DIGITAL', '54522A', 'HP', '36060356', 'setor 1', 0, 0),
(107, 1, 'TRANSFORMADOR 110/220   4000W   38A', 'WB4000', 'WB', '-----', 'setor 1', 0, 0),
(108, 1, 'TRANSFORMADOR 220/1500   100mA', 'INT001OB', 'WB', '-----', 'setor 1', 0, 0),
(109, 1, 'TRANSFORMADOR 110/220   100VA   1A', 'WB100VA', 'WB', '-----', 'setor 1', 0, 0),
(110, 1, 'VARIVOLT', '110VAC', 'SOC.TEC.PAULISTA', '50008', 'setor 1', 0, 0),
(111, 1, 'VARIVOLT', '220VAC', 'SOC.TEC.PAULISTA', '50025', 'setor 1', 0, 0),
(112, 1, 'KIT LINHA DE 3Km', 'KIT', 'LABCAL', 'Inatel-112', 'setor 1', 0, 0),
(113, 1, 'ACESSORI KIT 50 OHM BNC', '11854A', 'HP', '-----', 'setor 1', 0, 0),
(114, 1, 'CALIBRATION KIT TYPE N', '85032B', 'HP', '3217A09375', 'setor 1', 0, 1),
(115, 1, 'HIGH FREQUENCY PROBE', '85024A', 'HP', '-----', 'setor 1', 0, 0),
(116, 1, 'KIT RESISTOR 1MOHM', 'KIT', 'LABCAL', 'Inatel-116', 'setor 1', 0, 0),
(117, 1, 'BAROMETRO', '-----', 'THIES CLIMA', '98867', 'setor 1', 0, 0),
(118, 1, 'ATENUADOR 30dB 12,4GHz', '6830-17A', 'HUBER SUHNER', '7372', 'setor 1', 0, 0),
(119, 1, 'ATENUADOR 30dB 12,4GHz', '6830-17A', 'HUBER SUHNER', '300170', 'setor 1', 0, 0),
(120, 1, 'THERMO HIGROMETRO DIGITAL', '175-H2', 'TESTO', '20033741/406', 'setor 1', 1, 1),
(121, 1, 'ANALISADOR DE ESPECTRO', 'E4407B', 'Agilent', 'MY44210707', 'setor 1', 0, 0),
(122, 1, 'KIT RESISTOR PADRÃO', 'Res-01', 'LABCAL', '-----', 'setor 1', 0, 0),
(123, 1, 'DECADA DE INDUTANCIA', 'LD8', 'LIONMOUNT & Co', '5071/15', 'setor 1', 1, 1),
(124, 1, 'KIT CARGA DE 600ohm', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(125, 1, 'KIT 10kohm e 1uF', 'KIT', 'LABCAL', '125', 'setor 1', 0, 0),
(126, 1, 'KIT 820ohm e 6,2uF', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(127, 1, 'GERADOR DE SINAIS até 1,1GHz', 'SML01', 'ROHDE&SCHWARZ', '102486', 'setor 1', 0, 0),
(128, 1, 'PONTA DE PROVA DE ALTA TENSÃO', 'HV15HF', 'Minipa', '-----', 'setor 1', 0, 0),
(129, 1, 'CRONOMETRO', 'NI 129', 'Agilent', 'NI 129', 'setor 1', 0, 0),
(130, 1, 'ELECTRIC FIELD PROBE TYPE 8.3', 'EMR 20', 'NARDA', 'AU-0020', 'setor 1', 1, 1),
(131, 1, 'ACOPLADOR DIRECIONAL', 'C5982-10', 'WERLATONE', '15088', 'setor 1', 1, 1),
(132, 1, 'RF-MILLIVOLTMETER', 'URV55', 'ROHDE&SCHWARZ', '1029.1701K02', 'setor 1', 1, 1),
(133, 1, 'ELECTRICAL SAFETY ANALYZER', '19032', 'CHROMA', 'AAP190320376', 'setor 1', 1, 1),
(134, 1, 'TRANSIENT IMMUNITY TESTS', 'TRANSIENT 2000', 'EMC-PARTNER', '679', 'setor 1', 1, 1),
(135, 1, 'POWER AMPLIFIER', 'FLH-200/100', 'FRANKONIA', '0018', 'setor 1', 1, 1),
(136, 1, 'ANTENA BICONILOG', 'BTA-L 02005L', 'FRANKONIA', '-----', 'setor 1', 0, 0),
(137, 1, 'MULTÍMETRO DIGITAL', 'ET-2040', 'MINIPA', 'MD204007703', 'setor 1', 0, 0),
(138, 1, 'SOUND LEVEL METER - DECIBELÍMETRO', '2239A', 'B&K', '2516916', 'setor 1', 1, 1),
(139, 1, 'ANALISADOR DE ESPECTRO', 'E4411B', 'Agilent', 'MY45104799', 'setor 1', 0, 0),
(140, 1, 'GERADOR DE SINAIS até 2GHz', '8648B', 'Agilent', '3847M01525', 'setor 1', 1, 1),
(141, 1, 'MULTIMETRO DE BANCADA', '34401A', 'Agilent', 'MY45011296', 'setor 1', 1, 1),
(142, 1, 'ANALISADOR DE ESPECTRO', '4396B', 'Agilent', 'MY43100367', 'setor 1', 0, 0),
(143, 1, 'ANALISADOR DE PARAMETROS S', '85046A', 'Agilent', 'MY43001102', 'setor 1', 0, 0),
(144, 1, 'GERADOR DE FUNÇÕES', '33220A', 'Agilent', 'MY43004258', 'setor 1', 1, 1),
(145, 1, 'GERADOR DE FUNÇÕES', '33220A', 'Agilent', 'MY43004247', 'setor 1', 0, 0),
(146, 1, 'GERADOR DE SINAIS até 2GHz', '8648B', 'Agilent', '3847M01526', 'setor 1', 1, 1),
(147, 1, 'DIVISOR DE POTÊNCIA', '11636A', 'Keysight', '9403', 'setor 1', 0, 0),
(148, 1, 'OSCILOSCÓPIO 2 CANAIS TEKTRONIX', 'TDS320', 'TEKTRONIX', 'B047309', 'setor 1', 0, 0),
(149, 1, 'CONDUCTED IMMUNITY TEST SYSTEM', 'CIT-10/75', 'FRANKONIA', '102D1262', 'setor 1', 1, 1),
(150, 1, 'LISN - LINE IMPEDANCE STABILIZATION NETWORK', 'AFJ LS16C', 'AFJ EMC & SAFETY', '16010604157', 'setor 1', 1, 1),
(151, 1, 'DÉCADA RESISTIVA', 'K34Y6-10', 'SIEMENS', '080/2022', 'setor 1', 0, 0),
(152, 1, 'MULTÍMETRO DIGITAL', 'ET-2042A', 'MINIPA', 'ET204A003753', 'setor 1', 0, 0),
(153, 1, 'PONTA DE PROVA DE ALTA TENSÃO + O. TEKTRONIX', 'P6015A', 'TEKTRONIX', 'B055186', 'setor 1', 0, 0),
#(154, 1, 'PONTA DE PROVA DE ALTA TENSÃO + FLUKE', 'P6015A', 'TEKTRONIX', 'B055186', 'setor 1', 0, 0);
(154, 1, 'CÂMARA CLIMÁTICA (ESPEC)', 'SH-641', 'ESPEC', '92005117', 'setor 1', 0, 0),
(155, 1, 'CARGA 6dB 75WATTS', '75-A-FFN-06', 'FRANKONIA', '0545', 'setor 1', 1, 1),
(156, 1, 'ACOPLADOR', 'KEMZ 801', 'SCHAFFNER', '22037', 'setor 1', 1, 1),
(157, 1, 'ACOPLADOR CDN', 'CDN-M2+M3', 'FRANKONIA', 'A3011066', 'setor 1', 1, 1),
(158, 1, 'MULTIMETRO DE BANCADA', '34401A', 'Agilent', 'MY41036812', 'setor 1', 1, 1),
(159, 1, 'ALICATE AMPERÍMETRO', 'XL-1-MSZ808', 'EKM', '887154', 'setor 1', 0, 0),  -- Este equipamento não possui padrão e calibração
(160, 1, 'DÉCADA CAPACITIVA', 'DK4S', 'DANBRIDGE', '17005', 'setor 1', 1, 1),
(161, 1, 'DÉCADA RESISTIVA', '57.1.V.12.008', 'SIEMENS', '57.1.V.12.008', 'setor 1', 1, 1),
(162, 1, 'CARGA ELETRÔNICA', '6063B', 'HP', '3434A00981', 'setor 1', 1, 1),
(163, 1, 'DÉCADA RESISTIVA', '57.1.V.12.009', 'SIEMENS', '57.1.V.12.009', 'setor 1', 1, 1),
(164, 1, 'UMIDIFICADOR/PURIFICADOR DE AMIENTES', 'WATER CLEAR MAX TURBO', 'SONICLEAR', '38862', 'setor 1', 0, 0),
(165, 1, 'DESUMIDIFICADOR, UMIDIFICADOR E PURIFICADOR DE AR', 'DESIDRAT SUPER', 'GRAND PANDA/THERMOMATIC DO BRASIL', '20', 'setor 1', 0, 0),
(166, 1, 'ANTENA DIPOLO BICONICA', 'HK116', 'ROHDE&SCHWARZ', '100239', 'setor 1', 0, 0),
(167, 1, 'FIELD REFERENCE SOURCE', '1410', 'COMTEST', '07100 58', 'setor 1', 0, 0),
(168, 1, 'PCM CHANNEL ANALYZER', 'PCM 40', 'WG', 'BN 3039/01', 'setor 1', 1, 1),
(169, 1, 'AMPLIFICADOR DE BAIXO RUÍDO', 'ZFL-1000LN', 'Mini circuits', 'SF508900540', 'setor 1', 0, 0),
(170, 1, 'PCM CHANNEL SELECTOR PCS-40', 'PCS-40', 'WG', 'C0010', 'setor 1', 0, 0),
(171, 1, 'AMPLIFICADOR DE POTENCIA 800MHz a 2GHz', 'ZHL-5W-2G', 'Mini circuits', '-----', 'setor 1', 0, 0),
(172, 1, 'LEVEL GENERATOR', 'PS-33A', 'WANDEL & GOLTERMANN', 'AG-004', 'setor 1', 0, 0),
(173, 1, 'SELECTIVE LEVEL METER', 'SPM-33A', 'WANDEL & GOLTERMANN', 'A0-0157', 'setor 1', 0, 0),
(174, 1, 'TERMINAÇÃO 50 OHM', '909-F', 'HP', '9487', 'setor 1', 1, 1),
(175, 1, 'TERROMETRO', 'TM1000', 'Megabrás', '605055', 'setor 1', 0, 0),  -- Este equipamento não possui padrão e calibração
(176, 1, 'TERMINAÇÃO COAXIAL DE REFERÊNCIA', 'J2054', 'JBM', 'J2054-1132', 'setor 1', 1, 1),
(177, 1, 'ALVO 2 ohm - Calibração ESD', 'KIT', 'LABCAL', '17714', 'setor 1', 0, 0),
(178, 1, 'ESCI-EMI TESTE RECEIVER 9KHz A 16GHz', 'ESCI 3', 'ROHDE&SCHWARZ', '100914', 'setor 1', 0, 0),
(179, 1, 'KIT LABCAL DE RESISTENCIA (risco de incendio)', '-', 'LABCAL', '-----', 'setor 1', 0, 0),
(180, 1, 'AMPLIFICADOR DE POTENCIA 20MHz a 1GHz', '5127FE', 'OPHIR', '1079', 'setor 1', 0, 0),
(181, 1, 'GERADOR DE SINAIS DE ALTA POTENCIA PSG ATÉ 20GHz', 'E8257D', 'Agilent', 'MY49281336', 'setor 1', 1, 1),
(182, 1, 'UMIDIFICADOR/PURIFICADOR DE AMBIENTES', 'DESIDRAT SUPER', 'GRAND PANDA/THERMOMATIC DO BRASIL', '259', 'setor 1', 0, 0),
(183, 1, 'OSCILOSCÓPIO 500MHz 1GSa/s', '54615B', 'Agilent', 'US39151521', 'setor 1', 1, 1),
(184, 1, 'REDE DE ACOPLAMENTO ENY 21', 'ENY21', 'ROHDE&SCHWARZ', '101752', 'setor 1', 1, 1),
(185, 1, 'FONTE DC DUPLA', 'MPL-3303M', 'MINIPA', 'B3303M000882', 'setor 1', 0, 0),  -- Este equipamento não possui padrão e calibração
(186, 1, 'TRUE RMS CLAMP METER', '376', 'FLUKE', '18730456', 'setor 1', 1, 1),
(187, 1, 'MULTÍMETRO DIGITAL', '87V', 'FLUKE', '19190371', 'setor 1', 1, 1),
(188, 1, 'MULTÍMETRO DIGITAL', '87V', 'FLUKE', '19190368', 'setor 1', 1, 1),
(189, 1, 'THERMO HIGROMETRO DIGITAL', '175-H1', 'TESTO', '40304314-104', 'setor 1', 1, 1),
(190, 1, 'Programmable AC Source', '61511', 'CHROMA', '615110000157', 'setor 1', 1, 1),
(191, 1, 'MULTÍMETRO DIGITAL', 'ET-2040', 'MINIPA', 'MD204007706', 'setor 1', 0, 0),  -- Este equipamento não possui padrão e calibração
(192, 1, 'FLUKE 5500A SC600 CALIBRATOR', '5500A+SC600', 'FLUKE', '2127002', 'setor 1', 1, 1),
(193, 1, 'NO-BREAKE SMART-UPS', 'SURT6000XL', 'APC', 'BZFD1234', 'setor 1', 0, 0),
(194, 1, 'KIT SURGE IEC 1,2/ 50uSeg', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(195, 1, 'GTEM', '5407', 'ETS Lindgren', '143564', 'setor 1', 0, 0),
(196, 1, 'LISN - LINE IMPEDANCE STABILIZATION NETWORK', 'ESH2-Z5', 'ROHDE&SCHWARZ', '100391', 'setor 1', 0, 0),
(197, 1, 'NETWORK ANALYZER', 'E5071C', 'Agilent', 'MY46316180', 'setor 1', 1, 1),
(198, 1, 'PAQUÍMETRO', '-----', 'Maub', '-----', 'setor 1', 0, 0),
(199, 1, 'PAQUÍMETRO', '-----', 'MITUTOYO', 'BD016067', 'setor 1', 0, 0),
(200, 1, 'BOBINA (PADRÃO DE CORRENTE)', '5500A/COIL', 'FLUKE', '20081368', 'setor 1', 1, 1),
(201, 1, 'ESD-VERI-V', 'ESD-VERI-V', 'Inatel', 'ESD-VERI-V-1511', 'setor 1', 1, 1),
(202, 1, 'FREQUENCIMETRO', '53230A', 'Agilent', 'MY5000229253230A', 'setor 1', 1, 1),
(203, 1, 'KIT RESISTOR 5KOHM', '-----', 'LABCAL', '-----', 'setor 1', 1, 1),
(204, 1, 'MULTÍMETRO DIGITAL', 'MD-6111', 'ICEL', 'M61115194', 'setor 1', 1, 1),
(205, 1, 'BALUN/50 OHM/650MHz', '040-0092', 'Bheletronics', 'BH 2869', 'setor 1', 0, 0),
(206, 1, 'BALUN/50 OHM/30MHz', '040-0097', 'Bheletronics', 'BH 1072', 'setor 1', 0, 0),
(207, 1, 'BALUN/50 OHM/30MHz', '040-0097', 'Bheletronics', 'BH 1073', 'setor 1', 0, 0),
(208, 1, 'BALUN/50 OHM/350MHz', '040-0093', 'Bheletronics', 'BH 2919', 'setor 1', 0, 0),
(209, 1, 'BALUN/50 OHM/1GHz', '040-0229', 'Bheletronics', 'BH 0046', 'setor 1', 0, 0),
(210, 1, 'GERADOR DE SINAIS', 'SMB 100A', 'ROHDE&SCHWARZ', '1406.6000K02-107619-Zc', 'setor 1', 1, 1),
(211, 1, 'ACOPLADOR DIRECIONAL', '3022', 'NARDA', '5985-00-987-4655', 'setor 1', 1, 1),
(212, 1, 'AR FL Series Electric Field Probe Kit', 'FL7006 / FI7000', 'AR', '0342780 / 424751', 'setor 1', 1, 1),
(213, 1, 'MEDIDOR DE INTENSIDADE DE CAMPO', 'NBM-550/EHP-50', 'NARDA', 'E-0860/230WX30205', 'setor 1', 0, 0),
(214, 1, 'Amplificador de RF', '80S1G4', 'AR', '495959', 'setor 1', 1, 1),
(215, 1, 'THERMO HIGROMETRO DIGITAL', '175-H1', 'TESTO', '40327785-305', 'setor 1', 1, 1),
(216, 1, 'THERMO HIGROMETRO DIGITAL', '175-H1', 'TESTO', '40328024-305', 'setor 1', 1, 1),
(217, 1, 'TRANSFORMADOR 220V para 220V - 1/1', '1 para 1', '-------', '-----', 'setor 1', 1, 1),
(218, 1, 'TRANSFORMADOR 1/2 / 150W', '1 para 2', '-------', '-----', 'setor 1', 0, 0),
(219, 1, 'ANTENA BICONILOG', '3142E', 'ETS Lindgren', '154207', 'setor 1', 0, 0),
(220, 1, 'Gerador de Pulsos', '81110A', 'Agilent', 'ID81110A03611', 'setor 1', 0, 0),
(221, 1, 'Osciloscópio Infinium 4GHz', 'DSO9404A', 'Agilent', 'MY53450129', 'setor 1', 1, 1),
(222, 1, 'Adaptador GPIB to LAN', 'N4865A', 'ICS', 'US13111026', 'setor 1', 0, 0),
(223, 1, 'Terrômetro', 'MR-1505', 'MINIPA', '722', 'setor 1', 1, 1),
(224, 1, 'Harmonic and Flicker Analyzer', 'DPA500N', 'EM Test', 'P1249106144', 'setor 1', 1, 1),
(225, 1, 'Thermal Imager', 'Ti200', 'FLUKE', '14030492', 'setor 1', 1, 1),
(226, 1, 'Energy Analyzer', '435-II', 'FLUKE', '27473119', 'setor 1', 1, 1),
(227, 1, 'MULTIMETRO DE BANCADA', '34410A', 'Agilent', 'MY53007649', 'setor 1', 1, 1),
(228, 1, 'PONTA DE PROVA DE ALTA TENSÃO', 'P5100A', 'TEKTRONIX', 'C000512', 'setor 1', 0, 0),
(229, 1, 'WIDEBAND RADIO COMM. TESTER', 'CMW 500', 'ROHDE&SCHWARZ', '146933', 'setor 1', 1, 1),
(230, 1, 'CBT 32 BLUETOOTH TESTER', 'CBT', 'ROHDE&SCHWARZ', '22/10/2176', 'setor 1', 1, 1),
(231, 1, 'RF SHIELD BOX AND ANTENNA COUPLER', 'CMW-Z10', 'ROHDE&SCHWARZ', '----', 'setor 1', 0, 0),
(232, 1, 'DISPARADOR DE RIM', 'KIT', 'LABCAL', '-----', 'setor 1', 1, 1),
(233, 1, 'LogBox- RHT-LCD', 'LogBox-RHT-LCD', 'NOVUS', '15241116', 'setor 1', 1, 1),
(234, 1, 'LogBox- RHT-LCD', 'LogBox-RHT-LCD', 'NOVUS', '15241091', 'setor 1', 1, 1),
(235, 1, 'DRG Horn', '3115', 'ETS Lindgren', '164255', 'setor 1', 1, 1),
(236, 1, 'Ac Power Source', '6812B', 'Agilent', 'MY54000211', 'setor 1', 1, 1),
(237, 1, 'OSCILOSCÓPIO DIGITAL 4 CANAIS', 'DPO-5204B', 'Tektronix', 'C040264', 'setor 1', 1, 1),
(238, 1, 'Kit Fator de Potencia 0,7', 'Kit', 'LABCAL', '-----', 'setor 1', 0, 0),
(239, 1, 'Transformador 1:1 127/220 5kVA', 'WB5000', 'WB', '---', 'setor 1', 0, 0),
(240, 1, 'MULTIMETRO DE BANCADA', '34465A', 'Keysight', 'MY5450196734465A', 'setor 1', 1, 1),
(241, 1, 'Temperatura de referência (KIT)', 'KIT', 'LABCAL', '-----', 'setor 1', 0, 0),
(242, 1, 'Pulse Limiter (Emissão conduzida)', 'ESH3-Z2', 'ROHDE&SCHWARZ', '0357.8810.54', 'setor 1', 1, 1),
(243, 1, 'Surge Generator', 'SG61000-5', 'LISUN GROUP', '0506P1616072', 'setor 1', 1, 1),
(244, 1, 'PONTA DE PROVA DE ALTA TENSÃO', 'P6015A', 'TEKTRONIX', '-----', 'setor 1', 0, 0),
(245, 1, 'ATENUADOR 12dB', 'HS6812.17.AC', 'HUBER+SUHNER', '43608/46-502-1', 'setor 1', 1, 1),
(246, 1, 'POWER AMPLIFIER 20W (20MHZ-1GHZ)', 'Kit', 'LABCAL', '-----', 'setor 1', 0, 0),
(247, 1, 'Trena emborrachada 5000mm', 'Kit', 'Gold Tools', '-----', 'setor 1', 1, 1),
(248, 1, 'Trena emborrachada 5000mm', '5x25M', 'Gold Tools', '-----', 'setor 1', 1, 1),
(249, 1, 'KIT SURGE Porta externa Telecom 1kV 4x40ohms', 'Kit', 'LABCAL', '-----', 'setor 1', 1, 1),
(250, 1, '150Ω/50Ω ADAPTOR', '150Ω/50Ω ADAPTOR', 'FRANKONIA', '-----', 'setor 1', 1, 1),
(251, 1, 'POWER AMPLIFIER 30W 20MHz – 1GHz', '150Ω/50Ω ADAPTOR', 'LABCAL', '-----', 'setor 1', 0, 0),
(252, 1, 'Carga EFT 50 Ohm', 'VERI50', 'EMC - PARTNER', '49', 'setor 1', 1, 1),
(253, 1, 'Atenuador 10dB', 'J2001-75', 'JBM', 'J2001-275', 'setor 1', 1, 1),
(254, 1, 'Carga EFT 1 kOhm', 'VERI1k', 'EMC - PARTNER', '18', 'setor 1', 1, 1),
(255, 1, 'Cabo de RF 00 (Elétrica)', 'SUCOFLEX 104', 'HUBER+SUHNER', '509122/4', 'setor 1', 1, 1),
(256, 1, 'Digital Power Meter', '2100', 'ZENTECH', '921000043', 'setor 1', 1, 1),
(257, 1, 'LCR Meter', 'LCR-815B', 'GW', 'A120286', 'setor 1', 1, 1),
(258, 1, 'Programmable DC Power Supply', 'PPS-1203', 'MOTECH', '12033040020', 'setor 1', 1, 1),
(259, 1, 'Programmable DC Power Supply', 'PPS-1203', 'MOTECH', '12034050021', 'setor 1', 1, 1),
(260, 1, 'Câmara Climática -40ºC~105ºC (KSON)', 'THS-C4H+-100', 'KSON', '2446', 'setor 1', 1, 1),
(261, 1, 'OSCILOSCÓPIO 2 CANAIS HP', '54600B', 'HP', 'US37412391', 'setor 1', 1, 1),
(262, 1, 'Cabo de RF 01 (Câmara)', 'SUCOFLEX 104PE', 'HUBER+SUHNER', '34062/4PE', 'setor 1', 1, 1),
(263, 1, 'Cabo de RF 02 (Câmara)', 'SUCOFLEX 104PE', 'HUBER+SUHNER', '34060/4PE', 'setor 1', 1, 1),
(264, 1, 'Cabo de RF 03 (Câmara)', 'SUCOFLEX 104', 'HUBER+SUHNER', '511104/4', 'setor 1', 1, 1),
(265, 1, 'Cabo de RF 04 (Câmara)', 'SUCOFLEX 104', 'HUBER+SUHNER', '511111/4', 'setor 1', 1, 1),
(266, 1, 'Carga Imunidade Conduzida', 'CAL 801', 'Schaffner', '187881', 'setor 1', 1, 1),
(267, 1, 'Carga Imunidade Conduzida', 'CAL 801', 'Schaffner', '187882', 'setor 1', 1, 1),
(268, 1, 'Terminação 50 Ohms', '401-1F3', 'MECA', 'NC', 'setor 1', 1, 1),
(269, 1, 'Estação de Teste ESD7005', 'ESD7005', 'ESD Antiestáticos', '1680000616', 'setor 1', 1, 1),
(270, 1, 'Programmable DC Power Supply', 'PPS-1203', 'MOTECH', '12034050020', 'setor 1', 1, 1),
(271, 1, 'Cabo de RF 05 (Conduzida)', 'CABO DE RF', '----', '111/21', 'setor 1', 1, 1),
(272, 1, 'Cabo de RF 06 (Conduzida)', 'CABO DE RF', '----', '110/21', 'setor 1', 1, 1),
(273, 1, 'Cabo de RF 07 (Conduzida)', 'RG393', '----', '109/21', 'setor 1', 1, 1),
(274, 1, 'Cabo de RF 08 (Calibração)', 'SUCOFLEX 104PE', 'HUBER SUHBER', '34056/4PE', 'setor 1', 1, 1),
(275, 1, 'Cabo de RF 09 (Calibração)', 'SUCOFLEX 104PE', 'HUBER SUHBER', '34047/4PE', 'setor 1', 1, 1),
(276, 1, 'Cabo de RF 10 (Conduzida)', 'SUCOFLEX 104', 'HUBER SUHBER', '514469/4', 'setor 1', 1, 1),
(277, 1, 'Cabo de RF 11 (Conduzida)', 'SUCOFLEX 104A', 'HUBER SUHBER', '54159/4A', 'setor 1', 1, 1),
(278, 1, 'Cabo de RF 12 (Calibração)', 'RG393', 'HARBOUR INDUSTRIES', 'NT3P8004A0406871', 'setor 1', 1, 1),
(279, 1, 'Cabo de RF 13 (Calibração)', 'SUCOFLEX 104', 'HUBER SUHBER', '511105/4', 'setor 1', 1, 1),
(280, 1, 'Cabo de RF 14 (Calibração)', 'SUCOFLEX 104', 'HUBER SUHBER', '500451/4', 'setor 1', 1, 1),
(281, 1, 'Cabo de RF 15 (Calibração)', 'SUCOFLEX 104P', 'HUBER SUHBER', '501034/4P', 'setor 1', 1, 1),
(282, 1, 'POWER SENSOR 8481D', '8481D', 'HP', '3643A19540', 'setor 1', 0, 0),
(283, 1, 'POWER SENSOR 8481B', '8481B', 'HP', 'MY41090496', 'setor 1', 0, 0),
(284, 1, '50MHz Reference Attenuator 30dB', '11708A', 'HP', '22429', 'setor 1', 1, 1),
(285, 1, 'ATTENUATOR ASSEMBLY 30dB', '30dB ATT ASSEMBLY', 'Agilent', 'MY41090496', 'setor 1', 0, 0),
(286, 1, 'MEDIDOR DE NÍVEL', 'PMP-20', 'WG', 'CC-0077', 'setor 1', 0, 0),
(287, 1, 'GERADOR DE NÍVEL', 'PS-20', 'WG', 'CA-0037', 'setor 1', 0, 0),
(288, 1, 'Fonte 0V-30V 4A, 0-15V 7A (HW)', 'E3632A', 'Keysight', 'MY59056261', 'setor 1', 0, 0),
(289, 1, 'Data acquisition (HW) - CH104', '34972A', 'Keysight', 'MY57011005', 'setor 1', 0, 0),
(290, 1, 'Cronômetro JHD', 'XL-009', 'JHD', '-----', 'setor 1', 1, 1),
(291, 1, 'FONTE DC', 'PSH-3630A', 'GW INSTEK', 'EL200202', 'setor 1', 0, 0),
(292, 1, 'Data Acquisition System', 'DAQ970A', 'Keysight', '1-11853695981-1', 'setor 1', 1, 1),
(293, 1, 'PADRÃO DE PAQUÍMETRO', '515-555', 'MITUTOYO', '1810161', 'setor 1', 0, 0),
(294, 1, 'ATENUADOR 20dB', '8491B', 'HP', '29468', 'setor 1', 1, 1),
(295, 1, 'CARGA RESISTIVA', 'RESISTOR 100OHMS', 'LABCAL', '295', 'setor 1', 1, 1),
(296, 1, 'Sensor de temperatura', 'PT-100', 'ECIL', '-------', 'setor 1', 1, 1),
(297, 1, 'Sensor de temperatura', 'PT-100', 'ECIL', '-------', 'setor 1', 1, 1),
(298, 1, 'Sensor de temperatura', 'PT-100', 'ECIL', '-------', 'setor 1', 1, 1),
(299, 1, 'Sensor de temperatura', 'PT-100', 'ECIL', '-------', 'setor 1', 1, 1),
(300, 1, 'ALICATE AMPERÍMETRO', '376 FC', 'FLUKE', '5117393SV', 'setor 1', 1, 1),
(305, 1, 'PAQUÍMETRO', '-------', 'KINGTOOLS', 'D6456/23', 'setor 1', 1, 1),
(306, 1, 'ATENUADOR 10dB', '8491B', 'HP', '37958', 'setor 1', 1, 1),
(307, 1, 'ATENUADOR 20dB', '8491B', 'HP', '29475', 'setor 1', 1, 1),
(308, 1, 'ATENUADOR 3dB', '6803.17A', 'Huber Suhner', '29468', 'setor 1', 1, 1);

-- Inserção de informações de controle (quando aplicável)
INSERT INTO controle (id, id_equipamento, certificado, validade_cal, data_cal) 
VALUES
(1, 9, '268/2021', '2021-06-22', '2022-06-22'),
(2, 12, '567/2021', '2021-12-23', '2022-12-23'),
(3, 13, '132/2023', '2023-03-14', '2024-03-14'),
(4, 22, '148/2023', '2023-03-17', '2024-03-17'),
(5, 25, 'E2209/2021', '2021-12-15', '2023-12-15'),
(6, 26, '176/2020', '2020-04-15', '2022-04-15'),
(7, 31, 'CC-11104', '2020-10-20', '2022-10-20'),
(8, 33, '347/2022', '2022-08-05', '2023-08-05'),
(9, 35, '134/2023', '2023-03-14', '2024-03-14'),
(10, 36, '140/2023', '2023-03-16', '2024-03-16'),
(11, 37, '139/2023', '2023-03-16', '2024-03-16'),
(12, 38, '007/2020', '2019-08-23', '2022-08-23'),
(13, 47, '297/2021', '2021-07-14', '2022-07-14'),
(14, 51, '158/2021', '2022-08-05', '2023-08-05'),
(15, 52, '348/2022', '2022-08-05', '2023-08-05'),
(16, 55, '192/2022', '2022-04-20', '2023-04-20'),
(17, 56, '353/2022', '2022-08-08', '2023-08-08'),
(18, 58, '133/2023', '2023-03-14', '2024-03-14'),
(19, 59, 'E2208/2021', '2021-12-15', '2023-12-15'),
(20, 63, '278/2022', '2022-06-23', '2023-06-23'),
(21, 65, 'T1359/2022', '2022-09-23', '2024-09-23'),
(22, 66, 'E2211/2021', '2021-12-15', '2023-12-15'),
(23, 67, '380/2021', '2021-08-31', '2022-08-31'),
(24, 68, '154/2023', '2023-03-22', '2024-03-22'),
(25, 71, 'E2221/2021', '2021-12-17', '2023-12-17'),
(26, 73, '152/2021', '2021-04-14', '2022-04-14'),
(27, 74, '143/2023', '2023-03-16', '2024-03-16'),
(28, 75, '304/2021', '2021-07-21', '2022-07-21'),
(29, 78, '193/2022', '2022-04-20', '2023-04-20'),
(30, 81, '1-15193102379-1', '2021-08-31', '2024-08-31'),
(31, 82, 'R0092/2021', '2021-09-28', '2023-09-28'),
(32, 83, '1-15193102436-1', '2021-08-30', '2024-08-30'),
(33, 84, 'R0091/2021', '2021-09-27', '2023-09-27'),
(34, 96, '510/2021', '2021-11-24', '2022-11-24'),
(35, 97, 'CBR1800018', '2018-01-30', '2024-01-30'),
(36, 99, '275/2023', '2023-05-25', '2024-05-25'),
(37, 100, '104/2022', '2022-02-17', '2023-02-17'),
(38, 103, 'LV00857-33911-21-R0', '2021-10-01', '2023-10-01'),
(39, 107, '270/2021', '2021-06-22', '2022-06-22'),
(40, 112, '227/2022', '2022-05-13', '2023-05-13'),
(41, 116, '276/2023', '2023-05-25', '2024-05-25'),
(42, 118, '306/2021', '2021-07-22', '2022-07-22'),
(43, 120, 'T1358/2022', '2022-09-23', '2024-09-23'),
(44, 122, '226/2022', '2022-05-13', '2023-05-13'),
(45, 123, 'E2186/2021', '2021-12-10', '2023-12-10'),
(46, 124, '191/2022', '2022-04-20', '2023-04-20'),
(47, 130, 'PD.SM.11.22A.0840A/CC-01-AA', '2009-12-10', '2012-12-10'),
(48, 131, '166/2020', '2020-04-14', '2022-04-14'),
(49, 132, '239/2021', '2021-09-06', '2022-09-06'),
(50, 133, '305/2022', '2022-07-26', '2023-07-26'),
(51, 134, '11/12/2020', '2022-11-12', '2022-11-12'),
(52, 135, '293/2021', '2021-09-07', '2022-09-07'),
(53, 138, '31/01/2018', '2023-01-31', '2023-01-31'),
(54, 140, '242/2021', '2021-06-14', '2024-06-14'),
(55, 141, '07/10/2020', '2022-07-10', '2022-07-10'),
(56, 142, '26/05/2021', '2024-05-26', '2024-05-26'),
(57, 143, '24/05/2021', '2024-05-24', '2024-05-24'),
(58, 144, '05/08/2022', '2023-08-05', '2023-08-05'),
(59, 146, '105/2022', '2024-02-17', '2024-02-17'),
(60, 149, '168/2021', '2022-04-20', '2022-04-20'),
(61, 150, '275/2021', '2022-06-24', '2022-06-24'),
(62, 151, '080/2022', '2022-01-28', '2022-01-28'),
(63, 152, '019/2022', '2022-01-07', '2022-01-07'),
(64, 153, '01/10/2021', '2023-01-10', '2023-01-10'),
(65, 154, '555/2022', '202-12-16', '2023-12-16'),
(66, 155, '168/2021', '2021-04-20', '2022-04-20'),
(67, 156, '168/2021', '2021-04-20', '2022-04-20'),
(68, 157, '168/2021', '2021-04-20', '2022-04-20'),
(69, 158, 'CC-11217', '2022-09-19', '2024-09-19'),
(70, 160, 'E2188/2021', '2021-12-13', '2023-12-13'),
(71, 161, '195/2022', '2022-04-20', '2023-04-20'),
(72, 162, '166/2021', '2021-04-16', '2022-04-16'),
(73, 163, '020/2022', '2022-01-07', '2023-01-07'),
(74, 166, '4000.7752.01-T-07.00', '2007-03-27', '2022-03-27'),
(75, 168, '175/2020', '2020-04-15', '2022-04-15'),
(76, 174, '261/2023', '2023-05-16', '2024-05-16'),
(77, 175, '093/13', '2013-02-13', '2014-02-13'),
(78, 176, '277/2023', '2023-05-25', '2024-05-25'),
(79, 178, 'LIT33-LIT00-CC-10138', '2020-11-26', '2022-11-26'),
(80, 179, '096/2022', '2022-02-15', '2023-02-15'),
(81, 181, '1-14477920232-1', '2021-05-24', '2024-05-24'),
(82, 183, 'F0493/2021', '2021-09-29', '2023-09-29'),
(83, 184, '168/2021', '2021-04-20', '2022-04-20'),
(84, 186, 'E2191/2021', '2021-12-13', '2023-12-13'),
(85, 187, 'E1807/2021', '2021-09-29', '2023-09-29'),
(86, 188, '194/2022', '2022-04-20', '2023-04-20'),
(87, 189, 'T2513/2021', '2021-12-14', '2023-12-14'),
(88, 190, '378/2021', '2021-08-30', '2022-08-30'),
(89, 192, 'CC-10944/RC-10053/CC-11564', '2019-09-17', '2023-09-17'),
(90, 194, '379/2021', '2021-08-31', '2022-08-31'),
(91, 195, '293/2021', '2021-07-09', '2022-07-09'),
(92, 196, '169/2021', '2021-05-28', '2022-05-28'),
(93, 197, '1-15193102660-1', '2021-08-27', '2024-08-27'),
(94, 198, 'D6476-18', '2018-05-22', '2023-05-22'),
(95, 199, 'D6455/23', '2023-06-17', '2028-06-17'),
(96, 200, '282/2022', '2022-06-24', '2023-06-24'),
(97, 201, '522/2021', '2021-12-03', '2022-12-03'),
(98, 202, '1-15193102515-1', '2021-08-31', '2024-08-31'),
(99, 203, '141/2023', '2023-03-16', '2024-03-16'),
(100, 204, '274/2021', '2021-06-24', '2022-06-24'),
(101, 210, '298/2021', '2021-07-15', '2022-07-15'),
(102, 211, '168/18', '2020-04-22', '2022-04-22'),
(103, 212, 'CC-11031', '2019-11-19', '2022-11-19'),
(104, 214, '292/2021', '2021-07-08', '2022-07-08'),
(105, 215, 'T2512/2021', '2021-12-14', '2023-12-14'),
(106, 216, 'T2511/2021', '2021-12-14', '2023-12-14'),
(107, 217, '134/21', '2021-04-07', '2022-04-07'),
(108, 221, '389/2022', '2022-08-31', '2024-08-31'),
(109, 223, '515/21', '2021-11-30', '2022-11-30'),
(110, 224, '185/2020', '2020-04-20', '2022-04-20'),
(111, 225, 'LV00857-33912-21-R0', '2021-10-01', '2023-10-01'),
(112, 226, '680/23', '2023-08-24', '2024-08-24'),
(113, 227, '1-15193102591-1', '2021-08-27', '2024-08-27'),
(114, 229, '204/18', '2018-05-28', '2022-05-08'),
(115, 230, '158/18', '2018-05-03', '2022-05-03'),
(116, 232, '279/2022', '2022-06-24', '2023-06-24'),
(117, 233, 'T1061/2020', '2020-08-04', '2025-08-04'),
(118, 234, 'T1062/2020', '2020-08-04', '2025-08-04'),
(119, 235, '107597', '2015-03-24', '2025-03-24'),
(120, 236, '142/2023', '2023-03-16', '2024-03-16'),
(121, 237, 'F0498/2021', '2021-09-30', '2023-09-30'),
(122, 238, '-----', '2021-06-23', '2022-06-23'),
(123, 239, '151/2021', '2021-04-14', '2022-04-14'),
(124, 240, '1-11623527143-1', '2019-08-23', '2022-08-23'),
(125, 242, '176/2021', '2021-04-26', '2022-04-26'),
(126, 243, 'LIT33-LIT00-CC-10072', '2020-08-25', '2022-08-25'),
(127, 245, '569/2021', '2021-12-27', '2023-12-27'),
(128, 248, '079/19', '2020-01-22', '2022-01-22'),
(129, 249, '168/2021', '2021-04-20', '2022-04-20'),
(130, 250, '271/2021', '2021-06-23', '2022-06-23'),
(131, 252, '521/2021', '2021-12-03', '2022-12-03'),
(132, 253, '052/2023', '2023-02-01', '2024-02-01'),
(133, 254, '018/2022', '2022-01-07', '2023-01-07'),
(134, 255, '115/21', '2021-03-24', '2023-03-24'),
(135, 256, '055/2022', '2022-01-19', '2023-01-19'),
(136, 257, 'E2193/2021', '2021-12-13', '2023-12-13'),
(137, 258, '054/2022', '2022-01-19', '2023-01-19'),
(138, 259, '552/2021', '2021-12-17', '2022-12-17'),
(139, 260, '573/2021', '2021-12-23', '2022-12-23'),
(140, 261, '570/2021', '2021-12-27', '2022-12-27'),
(141, 262, '114/21', '2021-03-24', '2023-03-24'),
(142, 263, '113/21', '2021-03-24', '2023-03-24'),
(143, 264, '112/21', '2021-03-24', '2023-03-24'),
(144, 265, '116/21', '2021-03-24', '2023-03-24'),
(145, 266, '043/2022', '2022-01-14', '2023-01-14'),
(146, 267, '044/2022', '2022-01-14', '2023-01-14'),
(147, 268, '021/2022', '2022-01-07', '2023-01-07'),
(148, 269, '056/2022', '2022-01-21', '2023-01-21'),
(149, 270, '157/2021', '2021-04-15', '2022-04-15'),
(150, 271, '111/21', '2021-03-24', '2023-03-24'),
(151, 272, '110/21', '2021-03-24', '2023-03-24'),
(152, 273, '109/21', '2021-03-24', '2023-03-24'),
(153, 274, '108/21', '2021-03-24', '2023-03-24'),
(154, 275, '524/2021', '2021-12-03', '2023-12-03'),
(155, 276, '117/21', '2021-03-24', '2023-03-24'),
(156, 277, '118/21', '2021-03-24', '2023-03-24'),
(157, 278, '107/21', '2021-03-23', '2023-03-23'),
(158, 279, '106/21', '2021-03-23', '2023-03-23'),
(159, 280, '105/21', '2021-03-23', '2023-03-23'),
(160, 281, '104/21', '2021-03-23', '2023-03-23'),
(161, 284, '054/2022', '2023-02-02', '2024-02-02'),
(162, 290, 'F0499/2021', '2021-09-29', '2024-09-29'),
(163, 292, '1-11853695981-1', '2020-08-18', '2022-08-18'),
(164, 293, '01766/21', '2021-04-09', '2024-04-09'),
(165, 294, '053/2023', '2023-02-01', '2024-02-01'),
(166, 295, '249/2021', '2021-06-16', '2022-06-16'),
(167, 296, '7413/20', '2020-10-06', '2022-10-06'),
(168, 297, '7415/20', '2020-10-06', '2022-10-06'),
(169, 298, '7414/20', '2020-10-06', '2022-10-06'),
(170, 299, '7412/20', '2020-10-06', '2022-10-06'),
(171, 300, '568/2021', '2021-12-23', '2022-12-23'),
(172, 305, 'D6456/23', '2023-06-17', '2028-06-17'),
(173, 306, '678/23', '2023-08-24', '2024-08-24'),
(174, 307, '679/23', '2023-08-24', '2024-08-24'),
(175, 308, '676/23', '2023-08-24', '2024-08-24');

SELECT * FROM empresas;	
SELECT * FROM equipamentos;
SELECT * FROM controle;

DELETE FROM equipamentos; # esclui a tabela equipamentos 
DELETE FROM controle; # esclui a tabela controle