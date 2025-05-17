# katazuke-pro-navi
A sample project demonstrating the integration of Vue.js frontend with Python backend

```
django-vue-sample/
├── backend/           # Djangoプロジェクト
│   └── ...
└── frontend/          # Vueプロジェクト
    └── ...
```

```
backend/
├── manage.py
├── requirements.txt
├── myproject/         # Djangoプロジェクト設定
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/             # Djangoアプリケーション
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py      # データモデル定義
    ├── tests.py
    ├── urls.py        # API URLルーティング
    └── views.py       # API ビュー
```

```
frontend/
├── public/
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── assets/        # 画像などの静的ファイル
│   ├── components/    # Vueコンポーネント
│   │   ├── ItemList.vue
│   │   └── ItemForm.vue
│   ├── services/      # APIサービス
│   │   └── api.ts
│   ├── types/         # TypeScript型定義
│   │   └── item.ts
│   ├── App.vue        # ルートコンポーネント
│   └── main.ts        # エントリーポイント
├── .eslintrc.js
├── .gitignore
├── babel.config.js
├── package.json       # npm依存関係
├── tsconfig.json      # TypeScript設定
└── vue.config.js      # Vue CLI設定
```