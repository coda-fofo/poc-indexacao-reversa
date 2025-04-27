INSERT INTO Tatuador (nome_de_usuario, nome_de_exibicao, descricao) VALUES
('caio_porcel', 'Caio Henrique Porcel', 'Sou um tatuador especializado em Old School'),
('kauan_alexandre', 'Kauan Alexandre Mendes da Silva', 'Realismo mágico | SP'),
('joao_pedro', 'João Pedro de Oliveira', 'O tatuador mais fofo de fineline de Porto Alegre'),
('vinicius_rebelatto', 'Vinicius Rebelatto', 'Leões e relógios, praia e vôlei'),
('lara_ink', 'Lara Cristina Souza', 'Tatuagens delicadas e florais com alma feminina'),
('tatu_hugo', 'Hugo Martins', 'Preto e cinza com sombra pesada'),
('dani_skull', 'Daniele Rocha', 'Crânios, serpentes e tudo que é sombrio'),
('nando_pokes', 'Fernando Lima', 'Mini pokes autorais direto de BH'),
('mari_fineart', 'Mariana Costa', 'Arte fina, traço limpo, coração cheio'),
('edu_trad', 'Eduardo Pereira', 'Tradicional americano com um toque brasileiro'),
('bia_japantattoo', 'Beatriz Tanaka', 'Tatuagens orientais com traço preciso'),
('caiotattoo_rio', 'Caio Mendes', 'Do tribal ao neotradicional, tudo no Rio'),
('aline_pontilhismo', 'Aline Barreto', 'Pontilhismo e mandalas com propósito'),
('gustavo_neo', 'Gustavo Andrade', 'Neotradicional com cores vivas e muita energia'),
('ju_blackink', 'Juliana Ferreira', 'Especialista em blackwork geométrico'),
('leo_dotwork', 'Leonardo Matos', 'Dotwork intenso com simbologia oculta'),
('carol_aquarela', 'Carolina Dias', 'Aquarela viva na pele, pura emoção'),
('rafa_tribal', 'Rafael Albuquerque', 'Tribais modernos e culturais'),
('isadora_fine', 'Isadora Menezes', 'Fineline com referências botânicas'),
('thiago_real', 'Thiago Costa', 'Realismo preto e cinza com emoção real'),
('luci_dotsoul', 'Luciana Andrade', 'Pontilhismo espiritual e mandalas únicas'),
('dudu_sketch', 'Eduardo Rocha', 'Sketch tattoo com alma de artista'),
('nath_color', 'Nathalia Gomes', 'Colorido vibrante e traço ousado'),
('bruno_oldgold', 'Bruno Figueira', 'Old School raiz com traços marcantes');

INSERT INTO Hashtag (hashtag) VALUES
('oldschool'), ('curitiba'), ('brasil'), ('sao-paulo'), ('retro'),
('realismo'), ('sp'), ('rutz'), ('fineline'), ('fofura'),
('porto-alegre'), ('leão'), ('relógio'), ('praia'), ('volei'),
('delicada'), ('floral'), ('feminina'), ('blackandgrey'), ('sombra'),
('power'), ('rio'), ('rj'), ('dark'), ('skull'), ('serpente'),
('gótica'), ('minipoke'), ('bh'), ('autoral'), ('tattoo'),
('fineart'), ('amor'), ('japonesa'), ('oriental'), ('precisão'),
('riodejaneiro'), ('tribal'), ('neotradicional'), ('mandala'),
('espiritual'), ('sagrado'), ('cores'), ('vibrante'), ('blackwork'),
('geométrico'), ('simbólico'), ('tatuagem'), ('místico'), ('aquarela'),
('colorido'), ('emoção'), ('cultura'), ('ancestral'), ('botânico'),
('natural'), ('detalhado'), ('espiritualidade'), ('sketch'),
('criatividade'), ('minimalista'), ('arte'), ('minimal');

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('oldschool', 'curitiba', 'brasil', 'sao-paulo', 'retro')
WHERE t.nome_de_usuario = 'caio_porcel';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('realismo', 'sao-paulo', 'sp', 'rutz')
WHERE t.nome_de_usuario = 'kauan_alexandre';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('fineline', 'fofura', 'porto-alegre')
WHERE t.nome_de_usuario = 'joao_pedro';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('leão', 'relógio', 'praia', 'volei', 'curitiba')
WHERE t.nome_de_usuario = 'vinicius_rebelatto';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('delicada', 'floral', 'sp', 'sao-paulo', 'feminina')
WHERE t.nome_de_usuario = 'lara_ink';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('blackandgrey', 'sombra', 'power', 'rio', 'rj')
WHERE t.nome_de_usuario = 'tatu_hugo';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('dark', 'skull', 'serpente', 'gótica', 'sao-paulo')
WHERE t.nome_de_usuario = 'dani_skull';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('minipoke', 'bh', 'autoral', 'tattoo', 'minimalista')
WHERE t.nome_de_usuario = 'nando_pokes';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('fineline', 'fineart', 'amor', 'sp', 'minimal')
WHERE t.nome_de_usuario = 'mari_fineart';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('tradicional', 'oldschool', 'brasil', 'curitiba', 'tattoo')
WHERE t.nome_de_usuario = 'edu_trad';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('japonesa', 'oriental', 'precisão', 'sao-paulo', 'arte')
WHERE t.nome_de_usuario = 'bia_japantattoo';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('tribal', 'neotradicional', 'riodejaneiro', 'rj', 'brasil')
WHERE t.nome_de_usuario = 'caiotattoo_rio';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('pontilhismo', 'mandala', 'espiritual', 'sp', 'sagrado')
WHERE t.nome_de_usuario = 'aline_pontilhismo';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('neotradicional', 'cores', 'vibrante', 'porto-alegre', 'tattoo')
WHERE t.nome_de_usuario = 'gustavo_neo';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('blackwork', 'geométrico', 'sp', 'minimal', 'arte')
WHERE t.nome_de_usuario = 'ju_blackink';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('dotwork', 'simbólico', 'tatuagem', 'sp', 'místico')
WHERE t.nome_de_usuario = 'leo_dotwork';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('aquarela', 'colorido', 'emoção', 'rio', 'rj')
WHERE t.nome_de_usuario = 'carol_aquarela';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('tribal', 'cultura', 'ancestral', 'brasilia', 'arte')
WHERE t.nome_de_usuario = 'rafa_tribal';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('fineline', 'botânico', 'natural', 'curitiba', 'minimalista')
WHERE t.nome_de_usuario = 'isadora_fine';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('realismo', 'blackandgrey', 'detalhado', 'sp', 'sao-paulo')
WHERE t.nome_de_usuario = 'thiago_real';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('mandala', 'pontilhismo', 'espiritualidade', 'rj', 'arte')
WHERE t.nome_de_usuario = 'luci_dotsoul';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('sketch', 'autoral', 'arte', 'bh', 'criatividade')
WHERE t.nome_de_usuario = 'dudu_sketch';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('colorido', 'vibrante', 'sp', 'sao-paulo', 'tattoo')
WHERE t.nome_de_usuario = 'nath_color';

INSERT INTO Tatuador_Hashtag (tatuador_id, hashtag_id)
SELECT t.id, h.id FROM Tatuador t
JOIN (SELECT id, hashtag FROM Hashtag) h
ON h.hashtag IN ('oldschool', 'tradicional', 'tattoo', 'retro', 'brasil')
WHERE t.nome_de_usuario = 'bruno_oldgold';

INSERT INTO TatuadorIndice (token, tatuadores_ids)
VALUES
('caio_porcel', ARRAY[1]),
('cai', ARRAY[1, 12]),
('henriqu', ARRAY[1]),
('porcel', ARRAY[1]),
('tatuador', ARRAY[1, 3]),
('especializ', ARRAY[1]),
('old', ARRAY[24, 1]),
('school', ARRAY[24, 1]),
('oldschool', ARRAY[24, 1, 10]),
('curitib', ARRAY[1, 10, 19, 4]),
('brasil', ARRAY[1, 10, 12, 18, 24]),
('saopaul', ARRAY[1, 2, 5, 7, 11, 20, 23]),
('retr', ARRAY[24, 1]),
('kauan_alexandr', ARRAY[2]),
('kauan', ARRAY[2]),
('alexandr', ARRAY[2]),
('mend', ARRAY[2, 12]),
('silv', ARRAY[2]),
('realism', ARRAY[2, 20]),
('mágic', ARRAY[2]),
('sp', ARRAY[2, 5, 9, 13, 15, 16, 20, 23]),
('rutz', ARRAY[2]),
('joao_pedr', ARRAY[3]),
('joã', ARRAY[3]),
('pedr', ARRAY[3]),
('oliveir', ARRAY[3]),
('fof', ARRAY[3]),
('finelin', ARRAY[19, 9, 3]),
('port', ARRAY[3]),
('alegr', ARRAY[3]),
('fofur', ARRAY[3]),
('portoalegr', ARRAY[3, 14]),
('vinicius_rebelatt', ARRAY[4]),
('vinicius', ARRAY[4]),
('rebelatt', ARRAY[4]),
('leõ', ARRAY[4]),
('relógi', ARRAY[4]),
('pra', ARRAY[4]),
('vôl', ARRAY[4]),
('leã', ARRAY[4]),
('vol', ARRAY[4]),
('lara_ink', ARRAY[5]),
('lar', ARRAY[5]),
('cristin', ARRAY[5]),
('souz', ARRAY[5]),
('tatuagens', ARRAY[11, 5]),
('delic', ARRAY[5]),
('flor', ARRAY[5]),
('alma', ARRAY[5, 22]),
('feminin', ARRAY[5]),
('floral', ARRAY[5]),
('tatu_hug', ARRAY[6]),
('hug', ARRAY[6]),
('martins', ARRAY[6]),
('pret', ARRAY[20, 6]),
('cinz', ARRAY[20, 6]),
('sombr', ARRAY[6]),
('pes', ARRAY[6]),
('blackandgrey', ARRAY[20, 6]),
('pow', ARRAY[6]),
('rio', ARRAY[17, 12, 6]),
('rj', ARRAY[17, 12, 21, 6]),
('dani_skull', ARRAY[7]),
('daniel', ARRAY[7]),
('roch', ARRAY[22, 7]),
('crâni', ARRAY[7]),
('serpent', ARRAY[7]),
('tud', ARRAY[12, 7]),
('sombri', ARRAY[7]),
('dark', ARRAY[7]),
('skull', ARRAY[7]),
('gótic', ARRAY[7]),
('nando_pok', ARRAY[8]),
('fern', ARRAY[8]),
('lim', ARRAY[8]),
('min', ARRAY[8]),
('pok', ARRAY[8]),
('autor', ARRAY[8]),
('diret', ARRAY[8]),
('bh', ARRAY[8, 22]),
('minipok', ARRAY[8]),
('autoral', ARRAY[8, 22]),
('tatto', ARRAY[8, 10, 14, 22, 23, 24]),
('minimal', ARRAY[8, 9, 19, 15]),
('mari_fineart', ARRAY[9]),
('marian', ARRAY[9]),
('cost', ARRAY[9, 20]),
('arte', ARRAY[9, 11, 15, 18, 21, 22]),
('fin', ARRAY[9]),
('trac', ARRAY[24, 9, 11, 23]),
('limp', ARRAY[9]),
('coraçã', ARRAY[9]),
('chei', ARRAY[9]),
('fineart', ARRAY[9]),
('amor', ARRAY[9]),
('edu_trad', ARRAY[10]),
('eduard', ARRAY[10, 22]),
('pereir', ARRAY[10]),
('tradicional', ARRAY[24, 10]),
('american', ARRAY[10]),
('toqu', ARRAY[10]),
('brasileir', ARRAY[10]),
('bia_japantatto', ARRAY[11]),
('beatriz', ARRAY[11]),
('tanak', ARRAY[11]),
('orient', ARRAY[11]),
('precis', ARRAY[11]),
('japones', ARRAY[11]),
('oriental', ARRAY[11]),
('precisã', ARRAY[11]),
('caiotattoo_ri', ARRAY[12]),
('tribal', ARRAY[18, 12]),
('neotradicional', ARRAY[12, 14]),
('riodejaneir', ARRAY[12]),
('aline_pontilh', ARRAY[13]),
('alin', ARRAY[13]),
('barret', ARRAY[13]),
('pontilh', ARRAY[21, 13]),
('mandal', ARRAY[21, 13]),
('propósit', ARRAY[13]),
('espiritual', ARRAY[21, 13]),
('sagr', ARRAY[13]),
('gustavo_n', ARRAY[14]),
('gustav', ARRAY[14]),
('andrad', ARRAY[21, 14]),
('cor', ARRAY[14]),
('viv', ARRAY[17, 14]),
('muit', ARRAY[14]),
('energ', ARRAY[14]),
('vibrant', ARRAY[14, 23]),
('ju_blackink', ARRAY[15]),
('julian', ARRAY[15]),
('ferreir', ARRAY[15]),
('especial', ARRAY[15]),
('blackwork', ARRAY[15]),
('geométr', ARRAY[15]),
('leo_dotwork', ARRAY[16]),
('leonard', ARRAY[16]),
('mat', ARRAY[16]),
('dotwork', ARRAY[16]),
('intens', ARRAY[16]),
('simbolog', ARRAY[16]),
('ocult', ARRAY[16]),
('simból', ARRAY[16]),
('tatuag', ARRAY[16]),
('místic', ARRAY[16]),
('carol_aquarel', ARRAY[17]),
('carolin', ARRAY[17]),
('dias', ARRAY[17]),
('aquarel', ARRAY[17]),
('pel', ARRAY[17]),
('pur', ARRAY[17]),
('emoçã', ARRAY[17, 20]),
('color', ARRAY[17, 23]),
('rafa_tribal', ARRAY[18]),
('rafael', ARRAY[18]),
('albuquerqu', ARRAY[18]),
('trib', ARRAY[18]),
('modern', ARRAY[18]),
('cultur', ARRAY[18]),
('ancestral', ARRAY[18]),
('isadora_fin', ARRAY[19]),
('isador', ARRAY[19]),
('menez', ARRAY[19]),
('referent', ARRAY[19]),
('botân', ARRAY[19]),
('natural', ARRAY[19]),
('thiago_real', ARRAY[20]),
('thiag', ARRAY[20]),
('real', ARRAY[20]),
('detalh', ARRAY[20]),
('luci_dotsoul', ARRAY[21]),
('lucian', ARRAY[21]),
('únic', ARRAY[21]),
('dudu_sketch', ARRAY[22]),
('sketch', ARRAY[22]),
('artist', ARRAY[22]),
('criativ', ARRAY[22]),
('nath_color', ARRAY[23]),
('nathal', ARRAY[23]),
('gom', ARRAY[23]),
('ous', ARRAY[23]),
('bruno_oldgold', ARRAY[24]),
('brun', ARRAY[24]),
('figueir', ARRAY[24]),
('raiz', ARRAY[24]),
('marcant', ARRAY[24]);