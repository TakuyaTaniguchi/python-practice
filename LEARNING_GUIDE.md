# Python学習ガイド: TypeScript/Ruby on Railsエンジニア向け

このガイドは、TypeScriptとRuby on Railsの経験があるWeb開発者がPythonとFastAPIを学ぶ際のポイントをまとめたものです。

## 言語の比較

### TypeScript → Python

| TypeScript | Python | 備考 |
|------------|--------|------|
| 静的型付け | 動的型付け + 型ヒント | Pythonは型アノテーションが任意だがMyPyなどで静的チェック可能 |
| `interface`, `type` | クラス、型ヒント | `from typing import TypedDict, Protocol` |
| クラス宣言 | クラス宣言 | 構文は異なるが概念は類似 |
| アロー関数 | ラムダ関数 | `lambda x: x * 2` |
| モジュールシステム | importシステム | `import module` や `from module import thing` |
| 非同期処理 (async/await) | 非同期処理 (async/await) | 同じキーワードだが実装が異なる |
| `undefined`/`null` | `None` | Pythonでは`None`のみ |
| `package.json` | `requirements.txt`/`pyproject.toml` | 依存関係管理 |

### Ruby on Rails → Python/FastAPI

| Ruby on Rails | Python/FastAPI | 備考 |
|---------------|----------------|------|
| Active Record | SQLAlchemy/Tortoise ORM | ORMの概念は同じだが構文が異なる |
| ルーティング (DSL) | デコレータベースのルート | `@app.get("/path")` |
| コントローラ | ルート関数 | 機能は同じだが実装方法が異なる |
| ビュー (ERB, Haml) | テンプレートエンジン (Jinja2) | APIのみの場合は不要 |
| 規約より設定 | 明示的な設定 | Railsより自由度が高い |
| Active Model | Pydantic | バリデーションとシリアライズ |
| `rails generate` | なし (手動) | スキャフォールディングがない |
| マイグレーション | Alembic | データベースマイグレーション |

## Python固有の学習ポイント

1. **インデントでスコープを表現**:
   - 波括弧 `{}` の代わりにインデント (スペース4つ推奨) を使用
   - コロン `:` で新しいブロックの開始を示す

2. **動的型付けと型ヒント**:
   ```python
   # 型ヒントなし
   def add(a, b):
       return a + b
   
   # 型ヒントあり
   def add(a: int, b: int) -> int:
       return a + b
   ```

3. **リスト内包表記**:
   ```python
   squares = [x * x for x in range(10) if x % 2 == 0]
   ```

4. **デコレータ**:
   - 関数やクラスの動作を拡張するパターン
   - FastAPIでルーティングに使用

5. **コンテキストマネージャ (`with` ステートメント)**:
   ```python
   with open('file.txt', 'r') as f:
       content = f.read()
   ```

6. **イテレータとジェネレータ**:
   ```python
   def fibonacci(n):
       a, b = 0, 1
       for _ in range(n):
           yield a
           a, b = b, a + b
   ```

## FastAPI学習ポイント

1. **デコレータベースのルーティング**:
   ```python
   @app.get("/items/{item_id}")
   async def read_item(item_id: int):
       return {"item_id": item_id}
   ```

2. **Pydanticモデル**:
   - TypeScriptの型定義に似た宣言的なデータモデリング
   - バリデーション、シリアライズ/デシリアライズを自動処理

3. **依存性注入システム**:
   ```python
   def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close()
   
   @app.get("/users/")
   def read_users(db: Session = Depends(get_db)):
       users = db.query(User).all()
       return users
   ```

4. **非同期サポート**:
   - `async def` と `await` を使用した非同期プログラミング
   - TypeScriptの非同期処理に似ているが、内部実装は異なる

5. **自動ドキュメント生成**:
   - Swagger UI (`/docs`) と ReDoc (`/redoc`) による自動ドキュメント
   - コードからAPIドキュメントを自動生成

6. **バリデーションシステム**:
   - Pydanticによる入力データの検証
   - 型変換、制約チェックなどが自動的に行われる

7. **HTTPステータスコードと例外処理**:
   ```python
   from fastapi import HTTPException, status
   
   @app.get("/items/{item_id}")
   async def read_item(item_id: int):
       if item_id not in items:
           raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Item not found"
           )
       return {"item": items[item_id]}
   ```

## プロジェクト構造の違い

### Ruby on Rails
```
app/
  controllers/
  models/
  views/
config/
  routes.rb
db/
  migrations/
```

### Python/FastAPI (一般的なパターン)
```
app/
  main.py       # アプリケーションのエントリポイント
  models.py     # Pydanticモデル
  schemas.py    # データスキーマ
  database.py   # データベース接続
  routers/      # ルーティングモジュール
  crud.py       # CRUDオペレーション
```

## サンプルコードの学習ポイント

このリポジトリのサンプルアプリケーションでは以下の点に注目してください：

1. **Pydanticモデルの定義と使用**:
   - `TodoCreate` と `Todo` モデルの継承関係
   - フィールドのバリデーションとデフォルト値

2. **FastAPIエンドポイントの定義**:
   - HTTPメソッドとパスの関連付け
   - リクエスト・レスポンスモデルの型付け
   - パスパラメータとクエリパラメータの使用

3. **Enumの使用**:
   - `Priority` 列挙型の定義と使用方法

4. **例外処理**:
   - `HTTPException` を使用したエラーハンドリング

5. **非同期関数**:
   - `async def` と `await` の使用パターン

6. **テストスクリプト**:
   - `requests` ライブラリを使ったAPI呼び出し

## 次のステップ

1. **データベース統合**:
   - SQLAlchemy ORM を使ったデータベース操作の学習
   - Alembic を使ったマイグレーション管理

2. **認証と認可**:
   - JWT, OAuth2 などの認証システムの実装
   - ロールベースのアクセス制御

3. **プロジェクト構造の拡張**:
   - 大規模アプリケーションのモジュール分割
   - 依存性注入パターンの活用

4. **テスト**:
   - Pytest を使った単体テストと統合テスト
   - テストカバレッジの測定

5. **デプロイメント**:
   - Docker と Docker Compose の活用
   - CI/CD パイプラインの構築