import sqlite3

conn = sqlite3.connect('cosmeticos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY,
    cliente TEXT,
    data_transacao TEXT,
    produto TEXT,
    valor REAL,
    quantidade INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS eventos_marketing (
    id INTEGER PRIMARY KEY,
    cliente TEXT,
    data_evento TEXT,
    canal TEXT,
    campanha TEXT,
    cliques INTEGER,
    visualizacoes INTEGER,
    custo REAL
)
''')

transacoes_data = [
    (1, 'Ana', '2025-07-01 10:00', 'Batom Vermelho', 29.90, 1),
    (2, 'Bruno', '2025-07-01 11:00', 'Shampoo Anticaspa', 39.90, 2),
    (3, 'Carla', '2025-07-02 14:30', 'Creme Facial', 59.90, 1),
    (4, 'Daniel', '2025-07-03 09:00', 'Perfume Floral', 89.90, 1),
    (5, 'Eduarda', '2025-07-03 13:45', 'Esmalte Azul', 9.90, 3),
    (6, 'Fábio', '2025-07-04 16:00', 'Gel para Cabelos', 24.90, 1),
    (7, 'Gabriela', '2025-07-04 17:15', 'Hidratante Corporal', 49.90, 1),
    (8, 'Henrique', '2025-07-05 12:00', 'Kit Maquiagem', 129.90, 1),
    (9, 'Isabela', '2025-07-05 15:00', 'Sabonete Facial', 19.90, 2),
    (10, 'João', '2025-07-06 18:00', 'Condicionador', 34.90, 1),
]

cursor.executemany('''
INSERT INTO transacoes (id, cliente, data_transacao, produto, valor, quantidade)
VALUES (?, ?, ?, ?, ?, ?)
''', transacoes_data)

eventos_data = [
    (1, 'Ana', '2025-06-30 09:00', 'Instagram', 'Campanha Batom', 10, 100, 50.0),
    (2, 'Bruno', '2025-06-30 10:00', 'Facebook', 'Campanha Shampoo', 5, 80, 30.0),
    (3, 'Carla', '2025-06-30 11:00', 'Google Ads', 'Campanha Creme', 7, 90, 45.0),
    (4, 'Daniel', '2025-07-01 08:00', 'Email', 'Campanha Perfume', 3, 60, 20.0),
    (5, 'Eduarda', '2025-07-01 09:00', 'Instagram', 'Campanha Esmalte', 12, 110, 55.0),
    (6, 'Fábio', '2025-07-02 10:00', 'YouTube', 'Campanha Gel', 8, 95, 40.0),
    (7, 'Gabriela', '2025-07-02 11:00', 'Facebook', 'Campanha Hidratante', 6, 85, 35.0),
    (8, 'Henrique', '2025-07-03 14:00', 'Google Ads', 'Campanha Kit', 4, 70, 28.0),
    (9, 'Isabela', '2025-07-03 15:00', 'Instagram', 'Campanha Sabonete', 9, 100, 48.0),
    (10, 'João', '2025-07-04 16:00', 'Email', 'Campanha Condicionador', 5, 75, 25.0),
]

cursor.executemany('''
INSERT INTO eventos_marketing (id, cliente, data_evento, canal, campanha, cliques, visualizacoes, custo)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', eventos_data)

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
