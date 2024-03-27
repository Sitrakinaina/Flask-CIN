DROP TABLE if EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_de_naissance TEXT NOT NULL ,
    lieu_de_naissance TEXT NOT NULL,
    signe TEXT NOT NULL,
    numero TEXT NOT NULL,
    lieu TEXT NOT NULL,
    arrondissement TEXT NOT NULL,
    profession TEXT NOT NULL,
    pere TEXT NOT NULL,
    mere TEXT NOT NULL,
    fait TEXT NOT NULL,
    le TEXT NOT NULL
);
-- DROP TABLE IF EXISTS posts;

-- CREATE TABLE posts (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     title TEXT NOT NULL,
--     content TEXT NOT NULL
-- );