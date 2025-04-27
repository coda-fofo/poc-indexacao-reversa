CREATE TABLE Tatuador (
    id SERIAL PRIMARY KEY,
    nome_de_usuario VARCHAR(32) NOT NULL,
    nome_de_exibicao VARCHAR(64) NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

CREATE TABLE Hashtag (
    id SERIAL PRIMARY KEY,
    hashtag VARCHAR(128) NOT NULL
);

CREATE TABLE Tatuador_Hashtag (
    id SERIAL PRIMARY KEY,
    tatuador_id INT NOT NULL,
    hashtag_id INT NOT NULL,
    FOREIGN KEY (tatuador_id) REFERENCES Tatuador(id),
    FOREIGN KEY (hashtag_id) REFERENCES Hashtag(id)
);

CREATE TABLE TatuadorIndice (
    token VARCHAR(255) PRIMARY KEY,
    tatuadores_ids INT[] NOT NULL
);