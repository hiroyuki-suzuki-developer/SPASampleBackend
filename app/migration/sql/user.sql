CREATE TABLE users (
    -- 主キー
    id SERIAL PRIMARY KEY,

    -- 必須フィールド
    name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL,

    -- 任意フィールド
    gender VARCHAR(10),

    -- 監査ログ (Audit Fields)
    created_datetime TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_user_id INTEGER,
    updated_datetime TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_user_id INTEGER,

    -- ソフトデリート (Soft Delete)
    deleted_datetime TIMESTAMP WITHOUT TIME ZONE,
    deleted_user_id INTEGER
);

-- インデックスの追加 (パフォーマンス向上のため)
CREATE INDEX ix_users_id ON users (id);
CREATE UNIQUE INDEX ix_users_email ON users (email);