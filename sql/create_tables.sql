CREATE TABLE IF NOT EXISTS vendas (
    id INT,
    title VARCHAR(255),
    price DECIMAL(10,2),
    category VARCHAR(100),
    rating_rate DECIMAL(3,2),
    rating_count INT,
    processed_at DATETIME
);